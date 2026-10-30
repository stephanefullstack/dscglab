# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 7

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22 et le 30/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.6 | `exercices/ex16_consolidation_ifrs_capitaux_propres` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.8 | `exercices/ex17_fusion_renonciation_boni` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.9 | `exercices/ex18_audit_litiges_evenements_posterieurs_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 a Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 1,25 |
| 1.1 b Cadre conceptuel de l'IASB, IASB et adoption européenne | `2.1.a` Cadre conceptuel de l'IASB | 2 |
| 1.1 c Contrôle de VINÉALOG par droits de vote potentiels | `2.1.c` Périmètre, instruments particuliers ; `2.1.d` Méthodes | 1,5 |
| 1.1 d Tableau du périmètre | `2.1.c` Périmètre ; `2.1.d` Méthodes | 0,75 |
| 1.1 e Processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 0,5 |
| 1.2 Droits de mutation et frais d'acte du chai | `2.2.c` Homogénéisation, thèmes communs | 5 |
| 1.3 a Écarts de conversion : comptes individuels et IFRS | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 2 |
| 1.3 b Incidence et impôt différé | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 2 |
| 1.3 c Écritures de change | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 3 |
| 1.4 a Rapprochement des comptes réciproques | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.4 b Élimination des opérations réciproques | `2.2.f` Comptes réciproques et résultats internes | 2,25 |
| 1.4 c Élimination du dividende | `2.2.f` Comptes réciproques et résultats internes | 0,75 |
| 1.5 a Actif net identifiable de MERRANDIÈRE | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.5 b Frais d'acquisition des titres | `2.2.g` Goodwill ; `2.2.c` Frais d'acquisition | 1,5 |
| 1.5 c Goodwill partiel | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.5 d Écarts d'évaluation en 2026 et résultat retraité | `2.2.g` ; `2.2.h` Partage des capitaux propres | 1,5 |
| 1.5 e Tableaux de partage | `2.2.h` Partage des capitaux propres | 3,5 |
| 1.5 f Écritures d'évaluation, d'élimination des titres et de partage | `2.2.h` Partage des capitaux propres | 3 |
| 1.6 a Résultat net consolidé et répartition | `2.3.a` Documents de synthèse consolidés ; `2.2.h` | 1,5 |
| 1.6 b État des variations des capitaux propres | `2.3.a` Documents de synthèse consolidés | 4 |
| 1.6 c Résultat par action | `2.3.a` Documents de synthèse consolidés | 3 |
| 1.6 d Différences de présentation avec le règlement ANC | `2.3.a` ; `2.1.d` | 1,5 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = participations ne donnant pas le contrôle (PNC) ; `CAP_ELIM` = capital de la filiale éliminé ; `EA` = goodwill ; `IDP` = impôt différé passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat de l'écriture de bilan.

---

### 1.1 Cadre et périmètre de la consolidation (6 pts)

#### a. Obligation de consolider et référentiel (1,25 pt)

**Obligation (0,75 pt).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. VERCHAMBRE, SA, contrôle exclusivement MERRANDIÈRE et VINÉALOG (question c) (0,25 pt). Aucune exemption ne s'applique (0,5 pt) :
- VERCHAMBRE n'est contrôlée par aucune société : l'exemption de la société incluse dans les comptes consolidés d'une entité qui la contrôle ne la concerne pas [V L. 233-17, 1° ; F03 § 1.1] ;
- l'exemption des ensembles qui ne constituent pas un « grand groupe » est fermée : l'ensemble dépasse au moins deux des trois seuils (30 M€ de total du bilan, 60 M€ de chiffre d'affaires, 250 salariés) à la clôture de deux exercices consécutifs, 2025 (bilan 132 M€ et chiffre d'affaires 134 M€ ; 236 salariés, sous le seuil) et 2026 (les trois seuils) [V L. 230-2, 3° ; D. 230-2 ; F03 § 1.1].

**Référentiel (0,5 pt).** Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que si les titres de la société sont admis aux négociations sur un **marché réglementé** d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Euronext Growth est un système multilatéral de négociation, non réglementé, et aucun autre titre de VERCHAMBRE n'est admis sur un marché réglementé : le groupe pourrait appliquer le règlement ANC n° 2020-01 ; il a opté, depuis 2020, pour les IFRS adoptées par l'Union européenne, comme le permet le Code de commerce [V L. 233-24 ; F03 § 1.2].

#### b. Cadre conceptuel de l'IASB, IASB et adoption européenne (2 pts)

| Niveau | Attendu |
|---|---|
| 0 | Absence de réponse ou réponse non pertinente |
| 0,5 | Objectif de l'information financière et principaux utilisateurs |
| 1 | En plus, caractéristiques qualitatives fondamentales (pertinence, représentation fidèle) |
| 1,5 | En plus, caractéristiques auxiliaires et rôle de l'IASB |
| 2 | En plus, procédure d'adoption européenne (avis de l'EFRAG, règlement de la Commission) et application au cas |

**Objectif et utilisateurs (0,5 pt).** L'information financière à usage général a pour objectif de fournir, sur l'entité, une information utile aux investisseurs, prêteurs et autres créanciers, actuels et potentiels, pour prendre leurs décisions de lui fournir des ressources (acheter, conserver ou vendre des titres, accorder des crédits) [S présentation du cadre de 2018 ; V utilisateurs cités par la page « Conceptual Framework », ifrs.org ; F03 § 7.2]. Pour VERCHAMBRE, ce sont d'abord les actionnaires du flottant et les investisseurs d'Euronext Growth, puis les banques qui financent les stocks de vins en élevage.

**Caractéristiques qualitatives (0,75 pt).** Deux caractéristiques fondamentales : la **pertinence** (l'information peut influer sur les décisions, par sa valeur prédictive ou de confirmation ; elle intègre l'importance relative) et la **représentation fidèle** (information complète, neutre, exempte d'erreurs) (0,5 pt). Quatre caractéristiques auxiliaires, qui renforcent l'utilité : **comparabilité**, **vérifiabilité**, **rapidité**, **compréhensibilité** (0,25 pt) [S présentation du cadre de 2018 ; IAS 1 § 15 pour la représentation fidèle, V ; F03 § 7.2].

**Rôle du cadre et de l'IASB (0,25 pt).** L'IASB, groupe indépendant d'experts au sein de l'IFRS Foundation, élabore et publie les normes IFRS et approuve les interprétations du comité d'interprétation [V page « International Accounting Standards Board », ifrs.org ; F03 § 7.2]. Le cadre conceptuel, révisé en mars 2018, guide l'IASB dans l'élaboration de normes cohérentes ; il aide les entités à définir une méthode comptable lorsqu'aucune norme ne s'applique [V page « Conceptual Framework », ifrs.org ; IAS 8 § 11 ; F03 § 7.2]. Ce n'est pas une norme : il ne prévaut pas sur une IFRS [S].

**Adoption européenne (0,5 pt).** Les normes de l'IASB ne s'appliquent dans l'Union qu'après leur adoption par un règlement de la Commission européenne pris en application du règlement (CE) n° 1606/2002 (par exemple le règlement (UE) 2023/1803) [V intitulé du règlement ; F03 § 7.2]. L'EFRAG fait valoir les positions européennes auprès de l'IASB et conseille la Commission sur la conformité de chaque norme nouvelle ou modifiée aux critères du règlement IAS, y compris l'intérêt public européen [V page « Financial reporting », efrag.org ; F03 § 7.2]. Les comptes de VERCHAMBRE sont donc établis selon les « IFRS adoptées par l'Union européenne ».

#### c. Contrôle de VINÉALOG (1,5 pt)

**Critères (0,25 pt).** En IFRS, l'investisseur contrôle une entité s'il détient le pouvoir sur elle, s'il est exposé ou a droit à des rendements variables et s'il peut utiliser son pouvoir pour influer sur ces rendements [V IFRS 10 § 7 ; F03 § 2]. Pour apprécier le pouvoir, il tient compte de ses droits de vote potentiels (instruments convertibles, options) s'ils sont substantiels [V IFRS 10 B47 ; F03 § 7.1].

**Application (0,75 pt).**
- Avec 45 % des droits de vote, VERCHAMBRE n'a pas la majorité ; mais elle peut, à tout moment et à son seul choix, convertir ses 20 000 obligations en 20 000 actions nouvelles : elle détiendrait alors (13 500 + 20 000) / (30 000 + 20 000) = **67 %** des droits de vote.
- Ces droits sont **substantiels** : ils sont exerçables immédiatement, donc au moment où se prennent les décisions sur les activités pertinentes (élection annuelle du président, calendrier des mises en bouteille, investissements) [V B24] ; ni la loi ni les statuts ne s'y opposent, et VERCHAMBRE dispose de l'information nécessaire [V B23 a)] ; la conversion est **dans le cours** (une action vaut 190 € pour un prix de conversion de 100 €) et VERCHAMBRE en tirerait des synergies (VINÉALOG embouteille tous ses vins) [V B23 c) ; F03 § 7.1]. Les autres associés, une quarantaine, ne détiennent pas plus de 3 % chacun et ne sont liés par aucun pacte, ni par des droits potentiels.
- VERCHAMBRE est exposée à des rendements variables (dividendes, intérêts, synergies d'approvisionnement) et peut les influencer par son pouvoir. La situation est proche de celle que la norme illustre (40 % des droits de vote et une option substantielle sur 20 % supplémentaires) [V B50 ; F03 § 7.1].

**Conclusion (0,5 pt).** VERCHAMBRE contrôle VINÉALOG : **intégration globale** [V IFRS 10 § 22 ; F03 § 3]. Le pourcentage d'intérêt est déterminé sur la seule base des actions détenues, sans tenir compte de la conversion possible des obligations : **45 %**, et 55 % pour les PNC [V IFRS 10 B89 ; F03 § 7.1]. Les droits potentiels servent à qualifier le contrôle, pas à partager les capitaux propres et le résultat.

#### d. Périmètre au 31/12/2026 (0,75 pt)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % des PNC |
|---|---:|---|---|---:|---:|
| VERCHAMBRE | — | Société mère | — | 100 % | — |
| MERRANDIÈRE (0,25 pt) | 75 % | Contrôle exclusif (majorité des droits de vote, nomination du président) | Intégration globale | 75 % | 25 % |
| VINÉALOG (0,5 pt) | 45 % (67 % après conversion potentielle) | Contrôle exclusif (droits de vote potentiels substantiels) | Intégration globale | 45 % | 55 % |

#### e. Processus de consolidation (0,5 pt)

| Étape | Travaux du dossier |
|---|---|
| 1. Cadre et périmètre : obligation, référentiel, contrôle, méthodes, pourcentages | 1.1 |
| 2. Comptes individuels retraités aux méthodes du groupe, impôts différés compris ; juste valeur des actifs et passifs de l'entité acquise | 1.2, 1.3, 1.5 a, b et d |
| 3. Cumul des comptes des trois sociétés intégrées globalement | service consolidation |
| 4. Élimination des opérations internes (comptes réciproques, dividende) | 1.4 |
| 5. Élimination des titres, goodwill, partage des capitaux propres | 1.5 c, e et f |
| 6. États de synthèse : état de la situation financière, état du résultat net et des autres éléments du résultat global, état des variations des capitaux propres, tableau des flux, notes | 1.6 |

(0,25 pt pour l'enchaînement des étapes, 0,25 pt pour le rattachement des questions.)

**Réponses tolérées (1.1)**
- En b, toute présentation exacte du cadre conceptuel qui distingue objectif, utilisateurs et caractéristiques qualitatives ; citation de l'IFRIC (aujourd'hui IFRS Interpretations Committee) valorisée sans être exigée.
- En c, une conclusion fondée sur le seul exemple de la norme (40 % + option) si l'analyse du caractère substantiel est faite.

**Erreurs fréquentes (1.1)**
- IFRS présentées comme obligatoires parce que les actions sont « cotées » : Euronext Growth n'est pas un marché réglementé.
- VINÉALOG mise en équivalence (influence notable présumée à 45 %), alors que les droits de vote potentiels substantiels donnent le contrôle ; ou, à l'inverse, pourcentage d'intérêt porté à 67 % : la conversion potentielle ne modifie pas le partage.
- Seuils de grand groupe périmés (antérieurs au décret de décembre 2023) ou appréciés sur un seul exercice ; passage des comptes individuels aux comptes consolidés mal compris (`JUR-G01`).

**Références normatives (1.1)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 233-16, L. 233-17, L. 230-2, D. 230-2, L. 233-24 | Obligation de consolider, exemptions, seuils du grand groupe, option IFRS | [V] | F03 § 1 |
| Règlement (CE) n° 1606/2002, art. 4 | IFRS obligatoires pour les sociétés dont les titres sont admis sur un marché réglementé | [V] | F03 § 1.2 |
| Cadre conceptuel de l'IASB (2018) ; IAS 8 § 11 ; IAS 1 § 15 | Rôle du cadre ; objectif, utilisateurs, caractéristiques qualitatives | [V] rôle, [S] détail des caractéristiques | F03 § 7.2 |
| Pages IASB (ifrs.org) et EFRAG (efrag.org) ; règlement (UE) 2023/1803 | Rôle de l'IASB et de l'EFRAG, adoption par l'Union | [V] | F03 § 7.2 |
| IFRS 10 § 7, 22, B23, B24, B47, B50, B89 | Contrôle, droits de vote potentiels substantiels, intérêt sur les actions existantes | [V] | F03 § 2, § 7.1 |

---

### 1.2 Droits de mutation et frais d'acte du chai de Savigny (5 pts)

**Justification (0,75 pt).** Dans les comptes individuels, les droits de mutation, honoraires, commissions et frais d'actes liés à l'acquisition d'une immobilisation peuvent être portés en charges ou rattachés au coût d'acquisition [V PCG art. 213-8 ; F04 R4] : VERCHAMBRE a choisi les charges. Le manuel du groupe impose leur incorporation au coût (annexe 1.9, point 1), comme IAS 16, qui inclut dans le coût d'une immobilisation corporelle les coûts directement attribuables à son acquisition [V IAS 16 § 16 b) ; F04 R4]. Les méthodes du groupe s'appliquant de manière uniforme, les comptes de VERCHAMBRE sont retraités [V IFRS 10 § 19 ; F04 § 1].

**Ventilation des frais (0,5 pt).** Au prorata des prix : terrain 180 000 × 480 000 / 2 400 000 = **36 000 €**, non amortissable ; construction 180 000 × 1 920 000 / 2 400 000 = **144 000 €**, amortie sur 20 ans à compter du 01/01/2026 : 144 000 / 20 = **7 200 €** par an.

**Tableau d'incidence**

| | Ouverture au 01/01/2026 (réserves) | Variation de 2026 (résultat) | Clôture au 31/12/2026 (bilan) |
|---|---:|---:|---:|
| Frais incorporés au terrain | 36 000 | — | 36 000 |
| Frais incorporés à la construction | 144 000 | — | 144 000 |
| Amortissement de la construction | — | – 7 200 | – 7 200 |
| **Écart avant impôt** (3 × 0,25 pt) | **180 000** | **– 7 200** | **172 800** |
| Impôt différé passif, 25 % (3 × 0,25 pt) | – 45 000 | + 1 800 | – 43 200 |
| **Incidence nette** (2 × 0,25 pt) | **+ 135 000 réserves** | **– 5 400 résultat** | **+ 129 600** |

Contrôle : 135 000 – 5 400 = 129 600 = 172 800 × 75 %.

Les frais ont été déduits fiscalement en 2025 : la base fiscale de leur part dans le terrain et la construction est nulle, alors que leur valeur consolidée est de 172 800 € au 31/12/2026 ; cette différence imposable donne un impôt différé passif [V IAS 12 § 15 ; F04 R4]. La part du terrain n'est pas amortie mais garde son impôt différé, comme le prévoient les hypothèses générales (0,25 pt). L'incidence de 2025 (frais annulés, nets d'impôt) figure dans les réserves : elle avait déjà été retraitée dans les comptes consolidés de 2025.

**CH1 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2115 Terrains bâtis | 36 000 | |
| 2131 Bâtiments | 144 000 | |
| RST.VERCHAMBRE Résultat VERCHAMBRE | 5 400 | |
| 28131 Amortissements des bâtiments | | 7 200 |
| IDP Impôt différé passif | | 43 200 |
| RSV.VERCHAMBRE Réserves VERCHAMBRE | | 135 000 |
| **Total** | **185 400** | **185 400** |
| | *Libellé : incorporation des droits de mutation et frais d'acte au coût du chai* | | |

**CH1R (compte de résultat, 0,5 pt)** : débit 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles 7 200 ; crédit CH_ID Produit d'impôt différé 1 800 ; crédit RES_CR Résultat 5 400.

**Réponses tolérées** : terrain enregistré au compte 2111 ou au compte 213 regroupé ; écriture de bilan décomposée en une écriture d'ouverture (réserves) et une écriture de l'exercice (résultat), si les montants sont justes.

**Erreurs fréquentes** : frais de 2025 annulés en résultat de 2026 au lieu des réserves (`JUR-G04`) ; amortissement de la part du terrain ; impôt différé omis ou calculé sur les seuls frais de la construction ; absence de tableau d'incidence (`JUR-F05`) ; retraitement non justifié (`JUR-G06`).

**Références normatives (1.2)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 213-8 | Option charges / coût d'acquisition pour les frais d'acquisition des immobilisations | [V] | F04 R4 |
| IAS 16 § 16 b) | Coûts directement attribuables inclus dans le coût | [V] | F04 R4 |
| IFRS 10 § 19 | Méthodes comptables uniformes | [V] | F04 § 1 |
| IAS 12 § 15 | Passif d'impôt différé | [V] | F04 § 1 |

---

### 1.3 Écarts de change latents (7 pts)

#### a. Traitement dans les comptes individuels et dans les comptes consolidés (2 pts)

**Comptes individuels (1 pt).** Les créances et dettes en devises sont converties au dernier cours de change à la clôture (0,25 pt) ; les différences avec le montant initial sont inscrites dans des comptes transitoires, 476 à l'actif pour une perte latente et 477 au passif pour un gain latent (0,25 pt) ; le gain latent n'est pas comptabilisé en résultat (0,25 pt) ; la perte latente donne lieu à une provision pour risques (0,25 pt) [V PCG art. 420-5 ; F04 R12].

**Comptes consolidés (1 pt).** Les éléments monétaires en devises (créances, dettes) sont convertis au cours de clôture et les écarts de change sont comptabilisés en résultat, qu'il s'agisse de gains ou de pertes [V IAS 21 § 23 a) et § 28 ; F04 R12 ; annexe 1.9, point 2] (0,5 pt). La perte de VERCHAMBRE devient une charge de change, la provision n'a plus d'objet ; le gain de MERRANDIÈRE devient un produit de change ; les comptes 476, 477 et 1515 disparaissent (0,5 pt).

#### b. Incidence et impôt différé (2 pts)

**Calculs (0,5 pt)**

| | Cours de l'opération (1 € = 1,20 USD) | Cours de clôture (1 € = 1,25 USD) | Écart |
|---|---:|---:|---:|
| Créance de VERCHAMBRE (1 200 000 USD) | 1 000 000 | 960 000 | perte 40 000 (476 ; provision 1515) |
| Dette de MERRANDIÈRE (600 000 USD) | 500 000 | 480 000 | gain 20 000 (477) |

**Incidence sur le résultat (0,5 pt)**
- VERCHAMBRE : la perte de change de 40 000 € remplace la dotation à la provision de 40 000 € : **aucune incidence** sur le résultat (0,25 pt) ; seul le bilan change (476 et 1515 annulés).
- MERRANDIÈRE : gain de change de **+ 20 000 €**, absent du résultat des comptes individuels (0,25 pt) ; il revient pour 15 000 € au groupe et pour 5 000 € aux PNC (question 1.5 d).

**Impôt différé (1 pt).** Une différence temporelle n'existe que si la base fiscale d'un actif ou d'un passif diffère de sa valeur comptable consolidée [V IAS 12 § 5 et 15 ; F04 R12]. D'après l'hypothèse fiscale de l'annexe 1.4, les écarts de conversion sont compris dans le résultat imposable de 2026 : la base fiscale de la créance est de 960 000 € (perte déduite) et celle de la dette de 480 000 € (gain imposé), soit exactement leurs valeurs en IFRS (0,5 pt). La provision, non déductible, a été réintégrée et disparaît en IFRS. **Aucun impôt différé** n'est donc à constater : l'impôt exigible de 2026 des deux sociétés tient déjà compte de la perte et du gain ; le retraitement IFRS remet seulement le résultat comptable en accord avec cet impôt (0,5 pt).

#### c. Écritures (3 pts)

**X1 (bilan, 0,75 pt)** : débit 1515 Provisions pour pertes de change 40 000 ; crédit 476 Différence de conversion – Actif 40 000. *Libellé : créance en dollars de VERCHAMBRE, annulation de l'écart de conversion actif et de la provision.* La créance reste inscrite à 960 000 € au compte 411.

**X1R (compte de résultat, 0,75 pt)** : débit 666 Pertes de change financières 40 000 ; crédit 6865 Dotations aux provisions financières 40 000.

**X2 (bilan, 0,75 pt)** : débit 477 Différences de conversion – Passif 20 000 ; crédit RST.MERRANDIÈRE Résultat MERRANDIÈRE 20 000. *Libellé : dette en dollars de MERRANDIÈRE, gain de change latent porté en résultat.*

**X2R (compte de résultat, 0,75 pt)** : débit RES_CR Résultat 20 000 ; crédit 766 Gains de change financiers 20 000.

**Réponses tolérées** : X1 et X1R regroupées en une écriture si le candidat montre l'absence d'incidence sur le résultat ; perte de change de VERCHAMBRE présentée par l'annulation de la provision au crédit d'un compte de reprise (7865) plutôt que de la dotation, si le résultat est inchangé.

**Erreurs fréquentes** : impôt différé constaté par réflexe (passif de 5 000 € sur le gain, actif de 10 000 € sur la perte), alors que l'hypothèse fiscale aligne la base fiscale sur la valeur IFRS ; gain de MERRANDIÈRE attribué en totalité au groupe ; provision maintenue en IFRS en plus de la perte (double comptage) ; impôt différé non justifié (`JUR-G06`).

**Références normatives (1.3)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 420-5 | Conversion au cours de clôture, comptes 476 et 477, provision pour perte de change | [V] | F04 R12 |
| IAS 21 § 23 a), 28 | Éléments monétaires au cours de clôture, écarts de change en résultat | [V] | F04 R12 |
| IAS 12 § 5, 15 | Différence temporelle : base fiscale différente de la valeur comptable | [V] | F04 § 1, R12 |

---

### 1.4 Opérations internes entre VINÉALOG et VERCHAMBRE (4 pts)

#### a. Rapprochement des comptes réciproques (1 pt)

| | Montant |
|---|---:|
| Créance de VINÉALOG sur VERCHAMBRE (411) | 420 000 |
| Dette de VERCHAMBRE envers VINÉALOG (401) | 300 000 |
| **Écart** (0,25 pt) | **120 000** |

L'écart s'explique par le virement de 120 000 € émis et comptabilisé par VERCHAMBRE le 30/12/2026, reçu et enregistré par VINÉALOG le 04/01/2027 : à la clôture, les fonds sont en cours de transfert entre deux sociétés du groupe (0,25 pt). Avant l'élimination, on constate en consolidation le règlement en cours : la trésorerie du groupe comprend ces 120 000 € (virement interne en cours), et la créance de VINÉALOG est ramenée à 300 000 € (0,25 pt). Les comptes réciproques ainsi rapprochés (300 000 €) sont éliminés ; l'écart n'a aucune incidence sur le résultat (0,25 pt).

#### b. Élimination des opérations réciproques (2,25 pts)

**Principe (0,25 pt).** VINÉALOG étant intégrée globalement, les actifs, passifs, produits et charges réciproques sont éliminés **en totalité**, quel que soit le pourcentage d'intérêt [V IFRS 10 B86 c) ; F04 R14]. Sont concernés : les prestations d'embouteillage (3 600 000 €) et le solde fournisseurs (300 000 €) ; les obligations convertibles (2 000 000 €) et leurs intérêts de 2026 (2 000 000 × 3 % = **60 000 €**, payés le 31/12/2026, sans intérêts courus).

**I1 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 58 Virements internes (virement en cours) | 120 000 | |
| 401 Fournisseurs | 300 000 | |
| 161 Emprunts obligataires convertibles | 2 000 000 | |
| 411 Clients | | 420 000 |
| 2721 Obligations | | 2 000 000 |
| **Total** | **2 420 000** | **2 420 000** |
| | *Libellé : virement en cours et élimination des créances et dettes réciproques* | | |

**I1R (compte de résultat, 0,75 pt)** : débit 706 Prestations de services 3 600 000 ; débit 7621 Revenus des titres immobilisés 60 000 ; crédit 604 Achats d'études et prestations de services 3 600 000 ; crédit 6611 Intérêts des emprunts et dettes 60 000. Total 3 660 000.

**Incidence (0,25 pt).** Le produit de l'une est la charge de l'autre et l'annexe 1.5 écarte toute marge stockée : les éliminations ne modifient ni le résultat consolidé, ni la répartition entre groupe et PNC, et ne créent aucun impôt différé. Elles réduisent le chiffre d'affaires consolidé de 3 600 000 € : 128 000 000 + 9 600 000 + 14 000 000 – 3 600 000 = **148 000 000 €**, le chiffre annoncé.

#### c. Dividende reçu de VINÉALOG (0,75 pt)

Le dividende reçu par VERCHAMBRE (45 % × 400 000 = **180 000 €**) est un transfert interne de résultats déjà compris dans les réserves consolidées : il est éliminé du résultat de VERCHAMBRE et reclassé en réserves [V élimination des dividendes intra-groupe, ANC art. 251-2 ; F04 R14] (0,25 pt). La part versée aux associés extérieurs (55 % × 400 000 = 220 000 €) réduit les PNC (question 1.6 b).

**D1 (bilan, 0,25 pt)** : débit RST.VERCHAMBRE 180 000 ; crédit RSV.VERCHAMBRE 180 000. **D1R (compte de résultat, 0,25 pt)** : débit 7611 Revenus des titres de participation 180 000 ; crédit RES_CR 180 000.

**Réponses tolérées (1.4)** : virement en cours constaté au compte 512 ou dans un compte de trésorerie « fonds en transit » ; élimination des comptes réciproques sur la base de 420 000 € après avoir constaté la trésorerie en transit dans la même écriture (solution retenue) ou en deux écritures ; prestations enregistrées au compte 611 chez VERCHAMBRE si le candidat le justifie.

**Erreurs fréquentes (1.4)** : élimination limitée à 45 % ; élimination de 420 000 € de dette alors que VERCHAMBRE n'en doit que 300 000 € (écriture déséquilibrée, `JUR-F04`) ; oubli des obligations convertibles et de leurs intérêts ; impôt différé constaté sur une élimination sans incidence sur le résultat ; dividende éliminé pour 400 000 € au lieu de la seule part reçue par VERCHAMBRE.

**Références normatives (1.4)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 B86 c) | Élimination complète des opérations intragroupe | [V] | F04 R14 |
| ANC 2020-01 art. 251-1, 251-2 | Comptes réciproques ; dividendes intra-groupe éliminés (principe identique) | [V] | F04 R14 |

---

### 1.5 Regroupement d'entreprises et partage des capitaux propres (13 pts)

#### a. Actif net identifiable de MERRANDIÈRE au 01/01/2026 (2 pts)

| Élément | Montant |
|---|---:|
| Capitaux propres de MERRANDIÈRE (2 000 000 + 3 200 000) | 5 200 000 |
| Écart d'évaluation de l'atelier (1 800 000 – 1 200 000) (0,5 pt) | + 600 000 |
| Marque « Merrandière », non comptabilisée par l'acquise (0,5 pt) | + 800 000 |
| Impôt différé passif sur les écarts (1 400 000 × 25 %) (0,5 pt) | – 350 000 |
| **Actif net identifiable à la juste valeur** (0,5 pt) | **6 250 000** |

Les actifs identifiables et les passifs repris sont évalués à la juste valeur à la date d'acquisition, y compris les incorporels que l'acquise n'avait pas comptabilisés, comme une marque déposée et cessible séparément ; l'impôt différé sur les écarts est constaté selon IAS 12, y compris sur la marque non amortie, la base fiscale restant celle des comptes individuels [V IFRS 3 § 24 ; IAS 12 § 66 ; F05 § 2 et § 5 ; annexe 1.6].

#### b. Frais d'acquisition des titres (1,5 pt)

**Principe (0,5 pt).** En IFRS, les frais connexes à l'acquisition (honoraires de conseil, d'audit, d'avocats) sont des charges de l'exercice et n'entrent pas dans la contrepartie transférée [V IFRS 3 § 53 ; F04 R4 ; F05 § 2 ; annexe 1.9, point 3]. VERCHAMBRE les a inclus dans le coût des titres : le coût est ramené à 6 000 000 € et les frais de 150 000 € sont portés en charges de 2026, sans impôt différé (hypothèse de l'annexe 1.6). En règlement ANC n° 2020-01, ils seraient au contraire inclus dans le coût d'acquisition, nets d'impôt [V art. 231-2 ; F05 § 1.1].

**F1 (bilan, 0,5 pt)** : débit RST.VERCHAMBRE Résultat VERCHAMBRE 150 000 ; crédit 261.VERCHAMBRE Titres de participation MERRANDIÈRE 150 000.

**F1R (compte de résultat, 0,5 pt)** : débit 6226 Honoraires 150 000 ; crédit RES_CR Résultat 150 000.

#### c. Goodwill partiel (1,5 pt)

| Élément | Montant |
|---|---:|
| Contrepartie transférée, hors frais (0,25 pt) | 6 000 000 |
| – Quote-part du groupe dans l'actif net identifiable : 75 % × 6 250 000 (0,25 pt) | – 4 687 500 |
| **Goodwill partiel** (0,5 pt) | **1 312 500** |
| PNC à l'acquisition : 25 % × 6 250 000 | 1 562 500 |

[V IFRS 3 § 19 et 32 ; F05 § 2.1]

**Autre méthode (0,5 pt).** IFRS 3 laisse, pour chaque regroupement, le choix d'évaluer les PNC à leur juste valeur (goodwill « complet ») ou à leur quote-part de l'actif net identifiable (goodwill « partiel », retenu par le manuel) [V IFRS 3 § 19 ; F05 § 2]. Le goodwill complet ajouterait la part du goodwill revenant aux PNC (juste valeur des PNC – 1 562 500 €) ; les PNC au bilan seraient augmentées d'autant. Le goodwill partiel ne retient que le goodwill acquis par le groupe. Dans les deux cas, le goodwill n'est pas amorti ; aucune perte de valeur n'est à constater (annexe 1.6).

#### d. Écarts d'évaluation en 2026 et résultat retraité de MERRANDIÈRE (1,5 pt)

**Incidence des écarts d'évaluation (0,75 pt)**

| | 01/01/2026 | Résultat 2026 | 31/12/2026 |
|---|---:|---:|---:|
| Écart sur l'atelier | 600 000 | – 40 000 (600 000 / 15) | 560 000 |
| Marque (non amortie) | 800 000 | — | 800 000 |
| Impôt différé passif | – 350 000 | + 10 000 | – 340 000 |
| **Net** | **1 050 000** | **– 30 000** | **1 020 000** |

**Résultat retraité de MERRANDIÈRE (0,75 pt)** : 900 000 – 30 000 (amortissement net de l'écart sur l'atelier) + 20 000 (gain de change, question 1.3, sans impôt différé) = **890 000 €**.

#### e. Tableaux de partage au 31/12/2026 (3,5 pts)

**MERRANDIÈRE (2 pts)**

| Capitaux propres retraités au 31/12/2026 | Total | Groupe (75 %) | PNC (25 %) |
|---|---:|---:|---:|
| Capital | 2 000 000 | 1 500 000 | 500 000 |
| Réserves (comptes individuels) | 3 200 000 | 2 400 000 | 800 000 |
| Écarts d'évaluation nets à l'acquisition | 1 050 000 | 787 500 | 262 500 |
| **Sous-total : actif net identifiable à l'acquisition** (0,5 pt) | **6 250 000** | **4 687 500** | **1 562 500** (0,5 pt) |
| – Titres MERRANDIÈRE éliminés (coût IFRS) | | – 6 000 000 | |
| Goodwill (6 000 000 – 4 687 500) (0,5 pt) | | **+ 1 312 500** | |
| Réserves consolidées issues de MERRANDIÈRE | | **0** | |
| Résultat retraité 2026 (0,5 pt) | 890 000 | **667 500** | **222 500** |

Acquise le 01/01/2026, MERRANDIÈRE n'apporte aucune réserve consolidée au groupe : la différence entre le coût des titres et la quote-part de l'actif net est le goodwill. PNC au 31/12/2026 : 1 562 500 + 222 500 = **1 785 000 €** = 25 % × (6 250 000 + 890 000).

**VINÉALOG (1,5 pt)**

| Capitaux propres au 31/12/2026 | Total | Groupe (45 %) | PNC (55 %) |
|---|---:|---:|---:|
| Capital | 3 000 000 | 1 350 000 | 1 650 000 |
| Réserves | 1 600 000 | 720 000 | 880 000 |
| – Titres VINÉALOG éliminés | | – 1 350 000 | |
| **Réserves consolidées / PNC hors résultat** (2 × 0,5 pt) | | **720 000** | **2 530 000** |
| Résultat 2026 (0,5 pt) | 1 000 000 | **450 000** | **550 000** |

Souscription au pair à la constitution : ni écart d'évaluation, ni goodwill. Les éliminations de la question 1.4 sont sans incidence sur le résultat de VINÉALOG. PNC au 31/12/2026 : 2 530 000 + 550 000 = **3 080 000 €** = 55 % × 5 600 000. Les réserves consolidées issues de VINÉALOG (720 000 € + 180 000 € reclassés par D1 = 900 000 €) correspondent à 45 % des résultats accumulés depuis 2019 (1 200 000 + 800 000).

#### f. Écritures (3 pts)

**L1 (bilan, écarts d'évaluation à l'acquisition, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments (atelier) | 600 000 | |
| 205 Concessions et droits similaires, brevets, licences, marques (marque Merrandière) | 800 000 | |
| IDP Impôt différé passif | | 350 000 |
| RSV.MERRANDIÈRE Réserves MERRANDIÈRE (écarts d'évaluation nets) | | 1 050 000 |
| **Total** | **1 400 000** | **1 400 000** |

**L2 (bilan, amortissement 2026 de l'écart, 0,25 pt)** : débit RST.MERRANDIÈRE 30 000 ; débit IDP 10 000 ; crédit 28131 Amortissements des bâtiments 40 000.

**L2R (compte de résultat, 0,25 pt)** : débit 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles 40 000 ; crédit CH_ID Produit d'impôt différé 10 000 ; crédit RES_CR Résultat 30 000.

**L3 (bilan, élimination des titres MERRANDIÈRE et partage, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.MERRANDIÈRE Capital MERRANDIÈRE | 2 000 000 | |
| RSV.MERRANDIÈRE Réserves MERRANDIÈRE (3 200 000 + 1 050 000) | 4 250 000 | |
| RST.MERRANDIÈRE Résultat MERRANDIÈRE retraité | 890 000 | |
| EA Goodwill | 1 312 500 | |
| 261.VERCHAMBRE Titres de participation MERRANDIÈRE | | 6 000 000 |
| RST_G Résultat consolidé – part du groupe | | 667 500 |
| RSV_M PNC – quote-part de l'actif net identifiable | | 1 562 500 |
| RST_M PNC – résultat | | 222 500 |
| **Total** | **8 452 500** | **8 452 500** |

Le résultat éliminé (890 000 €) est celui que laissent les écritures X2 (+ 20 000) et L2 (– 30 000) ; le titre éliminé (6 000 000 €) est celui que laisse l'écriture F1.

**B1 (bilan, élimination des titres VINÉALOG et partage, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.VINÉALOG Capital VINÉALOG | 3 000 000 | |
| RSV.VINÉALOG Réserves VINÉALOG | 1 600 000 | |
| RST.VINÉALOG Résultat VINÉALOG | 1 000 000 | |
| 261.VERCHAMBRE Titres de participation VINÉALOG | | 1 350 000 |
| RSV_G Réserves consolidées – part du groupe | | 720 000 |
| RST_G Résultat consolidé – part du groupe | | 450 000 |
| RSV_M PNC – réserves | | 2 530 000 |
| RST_M PNC – résultat | | 550 000 |
| **Total** | **5 600 000** | **5 600 000** |

Au compte de résultat, le résultat net est ensuite attribué au groupe et aux PNC, sans écriture supplémentaire.

**Réponses tolérées (1.5)**
- L1 et L3 regroupées en une seule écriture si les montants sont justes ; écarts d'évaluation crédités à un compte « écarts d'évaluation » repris dans le partage.
- En d à f, résultat retraité de MERRANDIÈRE sans le gain de change si la question 1.3 n'a pas été traitée (870 000 €, soit 652 500 et 217 500) : appliquer la cohérence et ne pénaliser qu'une fois.
- Partage de VINÉALOG à 67 / 33 si le candidat a retenu ce pourcentage en 1.1 c : l'erreur n'est pénalisée qu'en 1.1 c et au premier item du tableau.

**Erreurs fréquentes (1.5)**
- Frais d'acquisition laissés dans le coût des titres (goodwill de 1 462 500 €), ou inclus nets d'impôt comme en règlement ANC (goodwill de 1 425 000 €) : en IFRS ils sont en charges (erreur symétrique de `JUR-G02`).
- Marque oubliée, ou marque sans impôt différé parce qu'elle n'est pas amortie ; amortissement de la marque.
- Goodwill calculé sur 100 % de l'actif net, ou PNC portées à une juste valeur que l'énoncé ne donne pas.
- Partage effectué sur les capitaux propres des comptes individuels, sans écarts d'évaluation ni retraitements (`JUR-G04`).
- Écritures déséquilibrées ou sans libellé (`JUR-F03`, `JUR-F04`).

**Références normatives (1.5)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 19, 24, 32, 53 | Évaluation des PNC (option), impôts différés, goodwill, frais connexes en charges | [V] | F05 § 2 |
| IAS 12 § 66 | Impôts différés d'un regroupement affectant le goodwill | [V] | F05 § 2 |
| IFRS 10 § 22, B86 | PNC dans les capitaux propres ; élimination des titres | [V] | F03 § 3, F05 § 3 |
| ANC 2020-01 art. 231-2 | Frais inclus dans le coût d'acquisition, nets d'impôt (comparaison) | [V] | F05 § 1.1 |

---

### 1.6 Documents de synthèse (10 pts)

#### a. Résultat net consolidé de 2026 et répartition (1,5 pt)

| Élément | Montant |
|---|---:|
| Résultat net de VERCHAMBRE (comptes individuels) | 5 337 900 |
| Résultat net de MERRANDIÈRE (comptes individuels) | 900 000 |
| Résultat net de VINÉALOG (comptes individuels) | 1 000 000 |
| Amortissement des frais incorporés au chai (CH1) | – 5 400 |
| Écarts de change : VERCHAMBRE (X1) / MERRANDIÈRE (X2) | 0 / + 20 000 |
| Opérations réciproques (I1) | 0 |
| Élimination du dividende de VINÉALOG (D1) | – 180 000 |
| Frais d'acquisition des titres MERRANDIÈRE en charges (F1) | – 150 000 |
| Amortissement de l'écart d'évaluation de l'atelier (L2) | – 30 000 |
| **Résultat net consolidé** (1 pt) | **6 892 500** |
| dont PNC : 25 % × 890 000 + 55 % × 1 000 000 = 222 500 + 550 000 (0,25 pt) | 772 500 |
| dont part du groupe (0,25 pt) | **6 120 000** |

Contrôle de la part du groupe : 5 337 900 – 5 400 – 180 000 – 150 000 + 667 500 (MERRANDIÈRE) + 450 000 (VINÉALOG) = 6 120 000. Le groupe n'a aucun autre élément du résultat global en 2026 : le résultat global est égal au résultat net.

#### b. État des variations des capitaux propres consolidés de 2026 (4 pts)

| | Capital | Primes | Réserves et résultats consolidés | Total part du groupe | PNC | Total |
|---|---:|---:|---:|---:|---:|---:|
| Capitaux propres au 31/12/2025 (0,25 pt) | 12 000 000 | 4 000 000 | 42 000 000 | 58 000 000 | 2 750 000 | 60 750 000 |
| Résultat net 2026 (= résultat global) (0,75 pt) | | | 6 120 000 | 6 120 000 | 772 500 | 6 892 500 |
| Dividendes versés (0,75 pt) | | | – 1 080 000 | – 1 080 000 | – 220 000 | – 1 300 000 |
| Augmentation de capital du 01/10/2026 (0,75 pt) | 3 000 000 | 4 500 000 | | 7 500 000 | | 7 500 000 |
| Acquisition de MERRANDIÈRE (entrée des PNC) (0,75 pt) | | | | | 1 562 500 | 1 562 500 |
| **Capitaux propres au 31/12/2026** (0,75 pt) | **15 000 000** | **8 500 000** | **47 040 000** | **70 540 000** | **4 865 000** | **75 405 000** |

Explications :
- dividendes du groupe : 0,90 € × 1 200 000 actions = 1 080 000 €, les actions nouvelles n'y ayant pas droit ; dividendes des PNC : 55 % × 400 000 = 220 000 €, versés par VINÉALOG à ses associés extérieurs. Le dividende reçu par VERCHAMBRE (180 000 €) est interne : il n'apparaît pas ;
- augmentation de capital : 300 000 actions × 10 € = 3 000 000 € de capital et 300 000 × (25 – 10) = 4 500 000 € de prime d'émission ; c'est une transaction avec les propriétaires [V IAS 1 § 106 ; F14 § 2.4] ;
- acquisition de MERRANDIÈRE : seules les PNC varient (25 % × 6 250 000), puisque le goodwill est partiel ; le prix payé par VERCHAMBRE ne modifie pas les capitaux propres part du groupe ;
- contrôle des PNC de clôture : 3 080 000 (VINÉALOG) + 1 785 000 (MERRANDIÈRE) = 4 865 000 €, montant des écritures L3 et B1.

L'état rapproche, pour chaque composante, les capitaux propres d'ouverture et de clôture en distinguant le résultat global, séparé entre propriétaires de la mère et PNC, et les transactions avec les propriétaires [V IAS 1 § 106 ; F14 § 2.4].

#### c. Résultat par action (3 pts)

**Obligation (0,5 pt).** IAS 33 s'applique aux états consolidés d'un groupe dont les actions ordinaires sont négociées sur un marché public [V IAS 33 § 2 b) ; F14 § 5]. Euronext Growth, système multilatéral de négociation ouvert au public, est un marché public même s'il n'est pas réglementé [S] : VERCHAMBRE présente un résultat de base et un résultat dilué par action dans l'état du résultat global [V IAS 33 § 66 ; F14 § 5]. Selon le règlement ANC n° 2020-01, l'information serait aussi obligatoire pour une entité dont les instruments sont négociés sur Euronext Growth [V art. 281-2, note 4 ; F14 § 1.4].

**Numérateur (0,75 pt).** Résultat attribuable aux porteurs d'actions ordinaires de la société mère : **6 120 000 €**, et non le résultat de l'ensemble consolidé (6 892 500 €) [V IAS 33 § 10 ; F14 § 5 et § 7].

**Dénominateur (1,25 pt).** Nombre moyen pondéré d'actions en circulation, les actions nouvelles étant prises en compte à compter de leur libération [V IAS 33 § 19 à 21 ; F14 § 5] :
1 200 000 × 12/12 + 300 000 × 3/12 = 1 200 000 + 75 000 = **1 275 000 actions**.

**Résultat de base par action (0,5 pt)** : 6 120 000 / 1 275 000 = **4,80 €**. VERCHAMBRE n'ayant émis aucun instrument donnant accès à son capital (annexe 1.1), le résultat dilué par action est égal au résultat de base et peut être présenté sur la même ligne [V IAS 33 § 67 ; F14 § 5].

#### d. Différences de présentation avec le règlement ANC n° 2020-01 (1,5 pt, 0,75 pt par différence)

- **Statut de l'état des variations des capitaux propres** : en IFRS, c'est l'un des états financiers du jeu complet, au même rang que l'état de la situation financière et l'état du résultat global [V IAS 1 § 10 et 106 ; F14 § 2.1, § 2.4]. Selon le règlement ANC, les états de synthèse sont le bilan et le compte de résultat ; la variation des capitaux propres est une information de l'**annexe**, sous forme de tableau, l'analyse des intérêts minoritaires étant facultative [V art. 111-4 et 282-26 ; F14 § 1.1, § 1.4].
- **Place des minoritaires** : en IFRS, les participations ne donnant pas le contrôle font partie des **capitaux propres**, présentées séparément de la part des propriétaires de la mère [V IAS 1 § 54 q) ; IFRS 10 § 22 ; F14 § 2.2]. Selon le règlement ANC, les « intérêts minoritaires » forment une rubrique distincte des capitaux propres part du groupe [V art. 281-1 ; F14 § 1.2, § 4].

Accepter toute autre différence exacte et justifiée, par exemple : absence d'état des autres éléments du résultat global en ANC, les variations directes de capitaux propres (écarts de conversion) étant analysées dans l'annexe [V F14 § 1.1, § 4].

**Réponses tolérées (1.6)**
- Cohérence avec les résultats du candidat aux questions 1.2 à 1.5 : la méthode est notée, une erreur reportée n'est pénalisée qu'une fois.
- Nombre moyen pondéré calculé en jours (1 200 000 + 300 000 × 92/365 = 1 275 616) : résultat par action de 4,80 € également.
- Primes et capital regroupés dans une colonne « capital et primes » (23 500 000 € à la clôture) si l'augmentation de capital est correctement ventilée dans les explications.

**Erreurs fréquentes (1.6)**
- Résultat par action calculé sur le résultat de l'ensemble consolidé (6 892 500 / 1 275 000 = 5,41 €), ou sur le nombre d'actions de clôture (6 120 000 / 1 500 000 = 4,08 €) [V F14 § 7].
- Dividende de VINÉALOG à VERCHAMBRE porté dans l'état des variations, ou dividendes versés aux PNC oubliés.
- Entrée de MERRANDIÈRE portée en part du groupe, ou goodwill inscrit dans les PNC alors que le manuel retient le goodwill partiel.
- PNC présentées hors des capitaux propres en IFRS [V F14 § 7].

**Références normatives (1.6)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 1 § 10, 54 q), 106 | Jeu complet d'états financiers ; PNC dans les capitaux propres ; contenu de l'état des variations | [V] | F14 § 2 |
| IAS 33 § 2, 10, 19-21, 66, 67 | Champ, résultat de base, nombre moyen pondéré, présentation | [V] ; Euronext Growth « marché public » [S] | F14 § 5 |
| ANC 2020-01 art. 111-4, 281-1, 281-2, 282-26 | États de synthèse, intérêts minoritaires, résultat par action, variation des capitaux propres en annexe | [V] | F14 § 1 |
| IFRS 10 § 22 | Participations ne donnant pas le contrôle | [V] | F03 § 3 |

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, renonciation, différence avec un rachat, référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2,5 |
| 2.2 Mode de valorisation et actif net apporté | `1.2.c` Déterminer le mode de valorisation des apports ; `1.2.d` Calculer et composer les apports | 2 |
| 2.3 Parité, parts à créer, augmentation de capital, prime | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 2 |
| 2.4 Boni : calcul, analyse, comptabilisation | `1.2.e` Calculer et analyser le boni ou mali de fusion ; `1.3.b` Adapter les écritures aux détentions préalables | 3,5 |
| 2.5 Régime fiscal de faveur | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 3,5 |
| 2.6 Écritures chez INOXANE | `1.3.a` Passer les écritures de base chez l'absorbante et l'absorbée | 2,5 |
| 2.7 Écritures chez VENDANGEL | `1.3.a` Écritures de base ; `1.3.b` Détentions préalables (annulation des parts, boni) ; `1.3.c` Écritures complémentaires (amortissements dérogatoires, opérations réciproques) | 5,5 |
| 2.8 Note de synthèse au gérant | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 3,5 |
| **Total** | | **25** |

---

### 2.1 Qualification, sort des parts détenues, différence avec un rachat, référentiel (2,5 pts)

**Qualification et modalités (1 pt).** L'opération est une **fusion-absorption** entre deux sociétés commerciales : INOXANE transmet l'ensemble de son patrimoine à une société existante, VENDANGEL [V PCG art. 710-2 ; C. com. L. 236-1, F01 § 1]. Ses modalités :
- **transmission universelle** : VENDANGEL reçoit tous les actifs et toutes les dettes d'INOXANE, y compris son emprunt bancaire, sa provision pour garanties, sa dette d'impôt de la période et sa créance sur VENDANGEL elle-même ;
- INOXANE est **dissoute sans liquidation** et disparaît ;
- VENDANGEL rémunère les apports par une **augmentation de capital** : elle crée des parts sociales qu'elle remet aux associés d'INOXANE en échange de leurs parts, selon la parité convenue.

**Sort des parts détenues par VENDANGEL (0,5 pt).** VENDANGEL ne peut pas se remettre ses propres parts : il n'est pas procédé à l'échange des parts d'INOXANE qu'elle détient [V C. com. L. 236-3 II 1°, F01 § 5.1]. C'est une **fusion-renonciation**. Seules les 4 000 parts de M. MAUBLANC et de Mme FERRAGUT sont rémunérées ; l'augmentation de capital et la prime de fusion correspondent aux seuls droits des associés autres que VENDANGEL [V BOI-IS-FUS-10-20-40-10 § 340, F01 § 5.1]. Les 6 000 parts détenues par VENDANGEL sont annulées. La quote-part des apports qui leur correspond n'est pas rémunérée ; sa comparaison avec la valeur comptable des parts annulées fait apparaître un boni ou un mali [V PCG art. 745-1, F01 § 5.1].

**Transmission universelle de patrimoine impossible (0,25 pt).** La dissolution sans liquidation par confusion de patrimoine suppose que toutes les parts soient réunies entre les mains d'un associé unique [V C. civ. art. 1844-5, F02 § 1]. VENDANGEL ne détient que 60 % des parts d'INOXANE : il lui faudrait d'abord racheter les 40 % restants.

**Différence avec un rachat des parts (0,5 pt)**
- *Rachat* : c'est une acquisition de titres, pas une restructuration. VENDANGEL paierait les 4 000 parts en trésorerie ou par emprunt, pour environ 40 % × 5 000 000 = 2 000 000 €. INOXANE subsisterait comme filiale à 100 %, avec ses propres comptes. M. MAUBLANC et Mme FERRAGUT quitteraient l'entreprise avec le prix de cession.
- *Fusion* : aucune sortie de trésorerie ; les apports sont rémunérés par 10 000 parts VENDANGEL nouvelles (voir 2.3). INOXANE disparaît et VENDANGEL reprend directement ses actifs et ses dettes. M. MAUBLANC et Mme FERRAGUT deviennent associés de VENDANGEL, conformément à leur souhait. En contrepartie, M. ROCHEVAL et Mme ARMANDIER voient leur participation diluée (voir 2.8).

**Référentiel et date (0,25 pt).** La fusion est enregistrée dans les comptes individuels des deux sociétés selon le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe la valeur d'inscription des apports [V PCG art. 710-1 et 720-1, F01 § 1]. La fusion prend effet à la date de sa réalisation : les écritures sont datées du **1er avril 2027**.

---

### 2.2 Mode de valorisation et actif net apporté (2 pts)

**Situation de contrôle (0,5 pt).** VENDANGEL détient 6 000 / 10 000 = 60 % des parts et des droits de vote d'INOXANE (une voix par part). Elle dispose de la majorité des droits de vote : elle contrôle INOXANE de manière **exclusive**. Une des sociétés participant à l'opération contrôlant préalablement l'autre de manière exclusive, l'opération est réalisée **sous contrôle commun** [V PCG art. 741-1 et 741-2, F01 § 2.1]. Le contrôle s'apprécie au niveau des personnes morales : que les associés de VENDANGEL soient des personnes physiques est sans incidence.

**Règle et exception (0,5 pt)**
- En situation de contrôle commun, les apports sont évalués à la **valeur comptable**, que l'opération soit à l'endroit ou à l'envers [V PCG art. 743-1 et tableau, F01 § 2.3] (0,25 pt). Le sens est donc sans incidence ; pour information, M. ROCHEVAL, associé principal de VENDANGEL, conserve 60 % du capital après l'opération (voir 2.8).
- La valeur réelle ne s'impose que si l'actif net comptable apporté est insuffisant pour libérer l'augmentation de capital [V PCG art. 743-3, F01 § 2.4]. Ici, l'actif net comptable apporté (3 200 000 €), et même sa seule part rémunérée (1 280 000 €, voir 2.3), excède largement l'augmentation de capital (500 000 €) : l'exception ne joue pas (0,25 pt).
- Les valeurs réelles fournies servent seulement à calculer la parité : les règles d'évaluation des apports ne visent pas celles du calcul de la parité [V PCG art. 740-1, F01 § 1].

**Composition des apports (0,5 pt).** VENDANGEL reprend chaque actif et chaque passif pour sa valeur dans les comptes d'INOXANE au 31 mars 2027, en distinguant les **valeurs brutes et les amortissements** [V PCG art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2]. Les deux sociétés ayant les mêmes méthodes comptables, aucun ajustement préalable n'est nécessaire [V PCG art. 744-3, F01 § 3.2].

| Élément apporté | Valeur brute | Amortissements | Valeur apportée |
|---|---:|---:|---:|
| Terrain | 300 000 | | 300 000 |
| Constructions | 1 500 000 | 600 000 | 900 000 |
| Matériels industriels | 2 000 000 | 800 000 | 1 200 000 |
| Stocks de matières premières | 640 000 | | 640 000 |
| Clients | 860 000 | | 860 000 |
| Disponibilités | 600 000 | | 600 000 |
| **Total de l'actif apporté** | **5 900 000** | **1 400 000** | **4 500 000** |
| Provision pour garanties données aux clients | | | – 50 000 |
| Emprunts bancaires | | | – 700 000 |
| Fournisseurs | | | – 380 000 |
| Dettes sociales | | | – 140 000 |
| État – impôt sur les bénéfices de la période | | | – 30 000 |
| **Actif net comptable apporté** | | | **3 200 000** |

**Actif net apporté (0,5 pt).** 4 500 000 – 1 300 000 = **3 200 000 €**. Contrôle par les capitaux propres d'INOXANE : 1 000 000 + 100 000 + 1 800 000 + 130 000 + 90 000 + 80 000 = 3 200 000 €. Les amortissements dérogatoires sont des provisions réglementées, classées dans les capitaux propres : ils font partie de l'actif net apporté [V PCG art. 214-8 et 313-1, F01 § 8].

---

### 2.3 Parité, parts à créer, augmentation de capital et prime de fusion (2 pts)

**Valeurs unitaires et parité (0,5 pt)**
- VENDANGEL : 8 000 000 / 40 000 = **200 €** par part ;
- INOXANE : 5 000 000 / 10 000 = **500 €** par part ;
- rapport d'échange : 500 / 200 = 5 / 2, soit **5 parts VENDANGEL pour 2 parts INOXANE**, la parité proposée [F01 § 4].

**Caractère équitable (0,5 pt).** Deux parts INOXANE valent 2 × 500 = 1 000 € et cinq parts VENDANGEL valent 5 × 200 = 1 000 € : les valeurs échangées sont égales, sans soulte [F01 § 4]. Pour l'ensemble des parts rémunérées : 4 000 × 500 = 10 000 × 200 = **2 000 000 €**. La valeur de VENDANGEL comprend déjà sa participation de 60 % dans INOXANE (3 000 000 €) : après la fusion, la société vaut 8 000 000 + 2 000 000 = 10 000 000 € pour 50 000 parts, soit toujours 200 € par part. Aucun groupe d'associés ne s'enrichit au détriment de l'autre : la parité est équitable.

**Parts à créer (0,5 pt).** Seules les parts des associés autres que VENDANGEL sont rémunérées (renonciation) : 10 000 – 6 000 = 4 000 parts INOXANE, échangées contre 4 000 × 5 / 2 = **10 000 parts VENDANGEL**.

**Augmentation de capital et prime de fusion (0,5 pt)**
- Augmentation de capital : 10 000 × 50 = **500 000 €** ;
- apport rémunéré (part de M. MAUBLANC et de Mme FERRAGUT) : 40 % × 3 200 000 = 1 280 000 € ;
- prime de fusion avant toute imputation : 1 280 000 – 500 000 = **780 000 €** [F01 § 4 et § 5.1].

La prime se calcule sur la **valeur comptable** de l'apport rémunéré, valeur d'inscription des apports, et non sur sa valeur d'échange (2 000 000 €).

---

### 2.4 Boni : calcul, analyse et comptabilisation (3,5 pts)

**Quote-part non rémunérée (0,5 pt).** Actif net apporté correspondant aux parts détenues par VENDANGEL : 60 % × 3 200 000 = **1 920 000 €** [V PCG art. 745-1, F01 § 5.1].

**Résultat d'annulation (0,5 pt).** 1 920 000 – 900 000 (valeur comptable des parts annulées) = **+ 1 020 000 €** : l'actif net reçu à hauteur de la participation excède la valeur comptable de celle-ci, c'est un **boni de fusion** [V PCG art. 745-2, F01 § 5.2].

**Résultats accumulés par INOXANE depuis l'acquisition et non distribués (0,75 pt).** Le boni est comptabilisé en résultat financier à hauteur de la quote-part des résultats accumulés par l'absorbée depuis l'acquisition et non distribués, et en capitaux propres pour le surplus [V PCG art. 745-2, F01 § 5.2]. D'après l'annexe 2.4 :
- résultats depuis le 2 janvier 2019 : – 60 000 + 40 000 + 150 000 + 210 000 + 240 000 + 260 000 + 280 000 + 300 000 + 90 000 = 1 510 000 € ;
- dividendes distribués : 120 000 + 150 000 + 120 000 = 390 000 € ;
- résultats accumulés non distribués : 1 510 000 – 390 000 = **1 120 000 €**.

Contrôle par les capitaux propres : réserve légale, autres réserves, report à nouveau et résultat de la période au 31/03/2027 (100 000 + 1 800 000 + 130 000 + 90 000 = 2 120 000 €), moins les mêmes postes au 02/01/2019 (100 000 + 880 000 + 20 000 = 1 000 000 €) = 1 120 000 €. La hausse des amortissements dérogatoires (80 000 – 30 000 = 50 000 €) n'est pas un résultat : elle est exclue.

**Part en résultat financier (0,5 pt).** 60 % × 1 120 000 = **672 000 €**. Ce sont les bénéfices réalisés par INOXANE depuis que VENDANGEL la contrôle, et que VENDANGEL n'a pas reçus sous forme de dividendes : la fusion les lui fait recueillir.

**Part en capitaux propres (0,5 pt).** 1 020 000 – 672 000 = **348 000 €**.

**Analyse du surplus (0,5 pt).** Le surplus ne provient pas de l'activité d'INOXANE sous le contrôle de VENDANGEL :
- 60 % × 2 030 000 (capitaux propres au 02/01/2019) – 900 000 (prix payé) = **318 000 €** : en 2019, VENDANGEL a acquis ses parts pour un prix inférieur à leur quote-part de capitaux propres, INOXANE sortant de deux exercices difficiles ;
- 60 % × 50 000 = **30 000 €** : quote-part de la hausse des amortissements dérogatoires depuis l'acquisition ;
- total : 318 000 + 30 000 = 348 000 €.

La fusion étant comptabilisée à la valeur comptable, le boni ne tient pas compte des plus-values latentes d'INOXANE (valeur réelle de 5 000 000 € contre un actif net comptable de 3 200 000 €) : il n'y a ni mali technique ni plus-value à affecter.

**Comptes (0,25 pt).** Le PCG ne prévoit pas de compte « boni de fusion » [V liste des comptes, F01 § 5.2]. Par convention, la part en résultat est portée au compte **768 Autres produits financiers** et la part en capitaux propres au compte **1042 Primes de fusion** [F01 § 5.2, convention de rédaction]. Écriture V3 en 2.7.

---

### 2.5 Régime fiscal de faveur (3,5 pts)

**Application du régime (0,5 pt).** Les deux sociétés participant à la fusion sont des SARL passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1]. La fusion relève du **régime de faveur de l'art. 210 A** du CGI, qui s'applique sauf option pour le droit commun [V CGI art. 210 A ; BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1]. VENDANGEL n'y renonce pas (annexe 2.1). INOXANE n'ayant pas de déficit reportable à transférer, aucune demande d'agrément n'est en jeu [V CGI art. 209 II, F02 § 3].

**Engagements de VENDANGEL dans le traité (1 pt ; 0,25 par engagement correctement appliqué, dans la limite de 1 pt)** [V CGI art. 210 A-3, F02 § 4] :
- **a)** reprendre à son passif les provisions d'INOXANE dont l'imposition est différée : ici la **provision pour garanties** (50 000 €) ;
- **b)** se substituer à INOXANE pour la réintégration des résultats dont la prise en compte avait été différée ;
- **c)** calculer les plus-values de cession ultérieure des immobilisations non amortissables, comme le **terrain**, d'après leur valeur fiscale chez INOXANE ;
- **d)** réintégrer dans ses bénéfices imposables les plus-values dégagées sur les biens amortissables : les apports étant repris à la valeur comptable, avec leurs valeurs brutes et leurs amortissements, **aucune plus-value** n'apparaît et il n'y a rien à réintégrer ; les amortissements se poursuivent sur les bases d'INOXANE ;
- **e)** inscrire les éléments non immobilisés, comme les **stocks** (640 000 €), à leur valeur fiscale chez INOXANE ; la reprise à la valeur comptable satisfait cette condition.

**a. Résultat de la période du 1er janvier au 31 mars 2027 (0,5 pt).** Le régime de faveur ne porte que sur les plus-values et profits dégagés sur les éléments apportés [V CGI art. 210 A-1, F02 § 2]. Le bénéfice de la dernière période d'INOXANE (120 000 € avant impôt) est **imposé immédiatement au nom d'INOXANE**, quel que soit le régime, par une déclaration spéciale de résultat [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2]. L'impôt correspondant (30 000 €), déjà comptabilisé, fait partie des dettes transmises : VENDANGEL le paiera.

**b. Provision pour garanties et amortissements dérogatoires (0,75 pt)**
- La **provision pour garanties**, déduite chez INOXANE, n'est pas réintégrée lors de la fusion : sous le régime de faveur, les provisions ne sont imposables que si elles deviennent sans objet [V CGI art. 210 A-2, F02 § 2]. VENDANGEL la reprend à son passif (engagement a) (0,25 pt).
- Les **amortissements dérogatoires** sont des provisions réglementées. En principe, les provisions réglementées sont imposées lors de la fusion [V BOI-IS-FUS-10-20-30 § 320, F02 § 2] ; l'administration admet que la reprise des amortissements dérogatoires chez INOXANE ne soit pas imposée si VENDANGEL les **reconstitue** à son bilan et les réintègre ensuite dans les mêmes conditions qu'INOXANE, au rythme de l'amortissement des presses et des rouleuses [V BOI-IS-FUS-30-20 § 10, F02 § 2] ; l'annexe 2.1 confirme ce sursis d'imposition. VENDANGEL les reconstitue par prélèvement sur la prime de fusion (écriture V4) (0,5 pt).

**c. Boni de fusion (0,75 pt).** Sous le régime de faveur, le profit dégagé par VENDANGEL lors de l'annulation des parts INOXANE qu'elle détenait n'est pas soumis à l'impôt sur les sociétés [V CGI art. 210 A-1, paraphrase, F02 § 2] :
- la part comptabilisée en résultat financier (672 000 €) est **déduite extra-comptablement** du résultat fiscal 2027 de VENDANGEL (0,5 pt). Ces bénéfices ont déjà été imposés chez INOXANE : leur imposition chez VENDANGEL serait une double imposition ;
- la part inscrite en prime de fusion (348 000 €) ne transite pas par le résultat : aucun retraitement n'est nécessaire (0,25 pt).

---

### 2.6 Écritures chez INOXANE au 1er avril 2027 (2,5 pts)

Les apports étant évalués à la valeur comptable, INOXANE ne dégage aucun résultat sur leur transmission.

**A1 — Apport de l'actif et du passif à VENDANGEL (1,25 pt).** INOXANE sort ses actifs (valeurs brutes et amortissements) et ses dettes ; sa créance sur VENDANGEL représente l'actif net apporté.

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – VENDANGEL, compte d'apport | 3 200 000 | |
| 28131 Amortissements des bâtiments | 600 000 | |
| 28154 Amortissements des matériels industriels | 800 000 | |
| 1512 Provisions pour garanties données aux clients | 50 000 | |
| 164 Emprunts auprès des établissements de crédit | 700 000 | |
| 401 Fournisseurs | 380 000 | |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | 140 000 | |
| 444 État – Impôts sur les bénéfices | 30 000 | |
| 211 Terrains | | 300 000 |
| 2131 Bâtiments | | 1 500 000 |
| 2154 Matériels industriels | | 2 000 000 |
| 31 Matières premières et fournitures | | 640 000 |
| 411 Clients | | 860 000 |
| 512 Banques | | 600 000 |
| **Total** | **5 900 000** | **5 900 000** |

**A2 — Droits des associés sur l'actif net (0,75 pt).** Les capitaux propres, amortissements dérogatoires compris, sont virés aux comptes des associés, au prorata de leurs parts.

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 1 000 000 | |
| 1061 Réserve légale | 100 000 | |
| 1068 Autres réserves | 1 800 000 | |
| 110 Report à nouveau – solde créditeur | 130 000 | |
| 120 Résultat de l'exercice – bénéfice (période du 01/01 au 31/03/2027) | 90 000 | |
| 145 Amortissements dérogatoires | 80 000 | |
| 456 Associés – Opérations sur le capital (VENDANGEL, 60 %) | | 1 920 000 |
| 456 Associés – Opérations sur le capital (M. MAUBLANC et Mme FERRAGUT, 40 %) | | 1 280 000 |
| **Total** | **3 200 000** | **3 200 000** |

**A3 — Remise des parts VENDANGEL et extinction des droits de VENDANGEL (0,5 pt).** VENDANGEL remet directement 10 000 parts nouvelles à M. MAUBLANC et à Mme FERRAGUT ; pour sa propre quote-part, elle renonce à recevoir des parts, et sa dette d'apport s'éteint avec sa créance d'associée.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital (M. MAUBLANC et Mme FERRAGUT) | 1 280 000 | |
| 456 Associés – Opérations sur le capital (VENDANGEL) | 1 920 000 | |
| 467 Divers comptes débiteurs – VENDANGEL, compte d'apport | | 3 200 000 |

Après A3, tous les comptes d'INOXANE sont soldés.

---

### 2.7 Écritures chez VENDANGEL au 1er avril 2027 (5,5 pts)

**V1 — Augmentation de capital rémunérant les apports (1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (40 % × 3 200 000) | 1 280 000 | |
| 101 Capital (10 000 parts × 50 €) | | 500 000 |
| 1042 Primes de fusion | | 780 000 |

**V2 — Réalisation des apports à la valeur comptable (1,5 pt).** Valeurs brutes et amortissements repris (0,75 pt) ; provision et dettes reprises (0,5 pt) ; compte d'apport crédité de l'actif net total (0,25 pt).

| Compte | Débit | Crédit |
|---|---:|---:|
| 211 Terrains | 300 000 | |
| 2131 Bâtiments | 1 500 000 | |
| 2154 Matériels industriels | 2 000 000 | |
| 31 Matières premières et fournitures | 640 000 | |
| 411 Clients | 860 000 | |
| 512 Banques | 600 000 | |
| 28131 Amortissements des bâtiments | | 600 000 |
| 28154 Amortissements des matériels industriels | | 800 000 |
| 1512 Provisions pour garanties données aux clients | | 50 000 |
| 164 Emprunts auprès des établissements de crédit | | 700 000 |
| 401 Fournisseurs | | 380 000 |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | | 140 000 |
| 444 État – Impôts sur les bénéfices | | 30 000 |
| 4561 Associés – Comptes d'apport en société | | 3 200 000 |
| **Total** | **5 900 000** | **5 900 000** |

**V3 — Annulation des parts INOXANE et boni (1,5 pt).** Quote-part non rémunérée et annulation des parts (0,5 pt) ; boni ventilé entre le résultat financier et les capitaux propres (2 × 0,5 pt) [V PCG art. 745-2, F01 § 5.2].

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (60 % × 3 200 000) | 1 920 000 | |
| 261 Titres de participation (6 000 parts INOXANE) | | 900 000 |
| 768 Autres produits financiers (boni : 60 % des résultats accumulés et non distribués) | | 672 000 |
| 1042 Primes de fusion (boni, part en capitaux propres) | | 348 000 |

Après V1 à V3, le compte 4561 est soldé : 1 280 000 + 1 920 000 = 3 200 000 €.

**V4 — Reconstitution des amortissements dérogatoires (0,75 pt).** Engagement du régime de faveur (voir 2.5), par prélèvement sur la prime de fusion [V corrigé du sujet zéro ; F01 § 8].

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion | 80 000 | |
| 145 Amortissements dérogatoires | | 80 000 |

**V5 — Extinction de la dette et de la créance réciproques (0,75 pt).** VENDANGEL devient à la fois créancière (créance d'INOXANE reçue par l'apport) et débitrice (sa dette fournisseur) de la même obligation : la confusion éteint la créance [V C. civ. art. 1349, F01 § 8].

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette de VENDANGEL envers INOXANE) | 60 000 | |
| 411 Clients (créance d'INOXANE sur VENDANGEL reçue par l'apport) | | 60 000 |

---

### 2.8 Note de synthèse à M. ROCHEVAL (3,5 pts)

**a. Capitaux propres de VENDANGEL juste après la fusion (1,5 pt).** Conformément à l'annexe 2.1, les capitaux propres avant la fusion sont ceux du 31/12/2026 ; le résultat de la période du 1er janvier au 31 mars 2027 n'est pas pris en compte.

| Poste | Avant la fusion | Variation | Après la fusion |
|---|---:|---:|---:|
| Capital (0,25 pt) | 2 000 000 | + 500 000 | 2 500 000 |
| Prime de fusion : 780 000 + 348 000 – 80 000 (0,5 pt) | 0 | + 1 048 000 | 1 048 000 |
| Réserve légale | 200 000 | | 200 000 |
| Autres réserves | 2 600 000 | | 2 600 000 |
| Report à nouveau | 150 000 | | 150 000 |
| Résultat : boni porté en résultat financier (0,25 pt) | 0 | + 672 000 | 672 000 |
| Amortissements dérogatoires (0,25 pt) | 0 | + 80 000 | 80 000 |
| **Total (0,25 pt)** | **4 950 000** | **+ 2 300 000** | **7 250 000** |

Contrôle : la hausse des capitaux propres (2 300 000 €) est égale à l'actif net comptable reçu (3 200 000 €) diminué de la valeur des parts INOXANE annulées (900 000 €).

**b. Répartition du capital après la fusion (1 pt ; 0,25 par associé)** — 40 000 + 10 000 = 50 000 parts :

| Associé | Parts avant | Parts après | % après |
|---|---:|---:|---:|
| M. Damien ROCHEVAL | 30 000 (75 %) | 30 000 | **60 %** |
| Mme Sylvie ARMANDIER | 10 000 (25 %) | 10 000 | **20 %** |
| M. Thierry MAUBLANC | – | 2 500 × 5 / 2 = 6 250 | **12,5 %** |
| Mme Nadia FERRAGUT | – | 1 500 × 5 / 2 = 3 750 | **7,5 %** |
| **Total** | **40 000** | **50 000** | **100 %** |

**Commentaire (1 pt, grille de niveaux)**

| Niveau | 0 | 0,5 | 1 |
|---|---|---|---|
| Attendu | Absence de commentaire ou commentaire hors sujet | Une ou deux idées pertinentes, sans lien avec les chiffres | Note structurée qui commente les capitaux propres, le résultat 2027 et le contrôle, chiffres à l'appui |

Idées attendues :
- **Capitaux propres** : ils augmentent de 2 300 000 € et atteignent 7 250 000 €. Les parts INOXANE (900 000 €) sont remplacées par les actifs et les dettes de l'atelier d'INOXANE, repris à leur valeur comptable ; les plus-values latentes d'INOXANE n'apparaissent pas au bilan.
- **Résultat 2027** : le boni augmente le résultat financier de 672 000 €. Ce produit est **non récurrent**, ne s'accompagne d'aucun encaissement et n'est pas imposable (déduction extra-comptable) : il faudra l'isoler pour apprécier la performance de 2027, notamment auprès du banquier. Les 348 000 € inscrits en prime ne passent pas par le résultat. Le résultat d'INOXANE à compter du 1er avril 2027 sera intégré directement dans celui de VENDANGEL.
- **Contrôle** : M. ROCHEVAL est dilué de 75 % à 60 %, mais garde la majorité des droits de vote et donc le contrôle de VENDANGEL ; Mme ARMANDIER passe de 25 % à 20 %. M. MAUBLANC et Mme FERRAGUT détiennent ensemble 20 % des parts. La parité étant équitable, la dilution ne fait perdre aucune valeur aux associés de VENDANGEL : leur part vaut toujours 200 €.
- **Tiers** : les créanciers d'INOXANE, en particulier sa banque, deviennent créanciers de VENDANGEL, dont l'endettement augmente de 700 000 € d'emprunts bancaires.

---

### Réponses tolérées
- **Amortissements dérogatoires repris directement au crédit du compte 145 dans l'écriture V2** : l'actif net apporté retenu est alors de 3 120 000 €, la prime avant imputation de 748 000 € et le boni de 972 000 €, dont 672 000 € en résultat et 300 000 € en capitaux propres. Cette méthode n'est pas la méthode de référence [F01 § 8] : les montants de l'actif net, de la prime et du boni des questions 2.2 à 2.4 sont comptés faux. Les écritures sont acceptées si elles sont cohérentes sur l'ensemble du dossier ; la prime finale (1 048 000 €) et les capitaux propres après la fusion sont alors identiques.
- **Écritures de VENDANGEL** : présentation en une seule écriture de V1 et V3 (promesse d'apport, annulation des parts et boni), ou dettes sociales ventilées entre 421 et 431.
- **Écritures d'INOXANE** : tout compte de tiers cohérent pour la créance sur VENDANGEL (par exemple 458) ou pour les droits des associés ; regroupement de A2 et A3 ; passage par un compte de titres VENDANGEL reçus puis remis aux associés ; écriture A1 passée par masses (immobilisations brutes, amortissements, actif circulant, provision et dettes), dès lors que les comptes d'amortissement sont soldés.
- **Comptes du boni** : un autre compte de produits financiers (classe 76) pour la part en résultat, ou un sous-compte de la prime de fusion intitulé « boni de fusion » pour la part en capitaux propres, dès lors que la ventilation est juste.
- **Engagements fiscaux** : présentation regroupée des engagements a) à e), dès lors que la provision pour garanties, le terrain, les biens amortissables et les stocks sont traités.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion mal calculée : calculée sur la valeur d'échange des parts rémunérées (2 000 000 – 500 000 = 1 500 000 €) ou sur la totalité de l'actif net apporté (3 200 000 – 500 000 = 2 700 000 €) au lieu de sa seule part rémunérée.
- `JUR-R02` Boni non analysé : comptabilisé en totalité en résultat ou en totalité en capitaux propres, ou ventilé sans calcul des résultats accumulés depuis l'acquisition.
- `JUR-R03` Oubli de la reconstitution des amortissements dérogatoires par prélèvement sur la prime de fusion.
- `JUR-R05` Difficulté à s'adapter : 25 000 parts créées pour les 10 000 parts INOXANE, oubli de la renonciation ; recherche d'un mali technique ou d'une affectation de plus-values latentes alors que la fusion est à la valeur comptable et dégage un boni.
- `JUR-F07` Annexe 2.4 mal exploitée : perte de 2019 ou dividendes oubliés ; hausse des amortissements dérogatoires comptée dans les résultats accumulés (60 % × 1 170 000 = 702 000 € en résultat au lieu de 672 000 €).
- Erreurs propres à ce cas : valeur réelle retenue au motif que les associés de VENDANGEL et les minoritaires d'INOXANE sont des personnes physiques ; prime calculée avant d'avoir vérifié la parité ; boni déclaré imposable ; écritures datées du 31 mars 2027.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 236-1 ; PCG art. 710-1, 710-2, 720-1 | Définition de la fusion, champ du titre VII, inscription des apports | [V] | F01 § 1 |
| C. com. L. 236-3 II 1° ; BOI-IS-FUS-10-20-40-10 § 340 | Pas d'échange des parts détenues par l'absorbante ; augmentation de capital limitée aux autres associés | [V] | F01 § 5.1 |
| C. civ. art. 1844-5 | Confusion de patrimoine réservée à l'associé unique | [V] | F02 § 1 |
| PCG art. 740-1, 741-1, 741-2, 743-1, 743-3 | Parité indépendante de l'évaluation des apports ; contrôle commun ; valeur comptable ; exception | [V] p. 82-85 | F01 § 1 et § 2 |
| PCG art. 744-2, 744-3 ; BOI-IS-FUS-10-20-40-20 § 170-180 | Reprise des valeurs comptables, valeurs brutes et amortissements | [V] | F01 § 3.2 |
| PCG art. 214-8, 313-1 | Amortissements dérogatoires : provisions réglementées, en capitaux propres | [V] p. 24 et 32 | F01 § 8 |
| PCG art. 745-1, 745-2 | Quote-part non rémunérée ; boni en résultat financier à hauteur des résultats accumulés non distribués, surplus en capitaux propres | [V] p. 86 | F01 § 5.1 et § 5.2 |
| Comptes 768 et 1042 pour le boni | Aucun compte dédié dans le PCG 2026 : convention de rédaction | [V] absence de compte ; choix = convention | F01 § 5.2 |
| CGI art. 210 A, 210 C-1 ; BOI-IS-FUS-10-10-10 § 10 et 20 | Champ du régime de faveur, application sauf option | [V] | F02 § 1 |
| CGI art. 210 A-1, 210 A-2, 210 A-3 a à e | Exonération des profits d'apport et du boni ; provisions ; engagements de l'absorbante | [V] (210 A-1 : paraphrase de la fiche) | F02 § 2 et § 4 |
| BOI-IS-FUS-10-20-30 § 210, 320 et 330 ; BOI-IS-FUS-30-20 § 10 | Imposition du résultat de la dernière période ; provisions réglementées ; reconstitution des amortissements dérogatoires | [V] | F02 § 2 |
| C. civ. art. 1349 | Extinction par confusion des créances réciproques | [V] | F01 § 8 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Cadres d'exercice de l'expert-comptable, du commissaire aux comptes et de l'auditeur de durabilité ; demandes de la présidente | `3.1.a` Cadres d'exercice professionnel ; `3.1.c` Principes déontologiques ; `3.2.a` Typologie des missions | 4 |
| 3.2 Refus de la présidente et moyens d'action sur les litiges | `3.2.b` Moyens d'action du CAC ; `3.1.d` Appliquer la norme pertinente | 3 |
| 3.3 Cycle provisions et litiges : risques, assertions, procédures, appréciation des provisions | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit | 4 |
| 3.4 Norme sur les événements postérieurs : corpus, identification, trois événements, écriture | `3.1.d` Référentiel normatif et application de la norme ; `3.2.d` Démarche d'audit (fin de mission) | 4 |
| 3.5 Opinion avec observation ; observation et réserve | `3.2.e` Portée des opinions ; `3.2.c` Caractère significatif | 3 |
| 3.6 ISSB, EFRAG, GRI ; demande de PENDRAVEN ; étendue et limites | `3.3.a` Contexte et architecture des normes de durabilité | 3 |
| 3.7 Exigences générales, principes des informations à publier ; impact, risque, opportunité | `3.3.b` Principes de construction du reporting | 3 |
| 3.8 Objectifs, assurance limitée, axes et étapes de la mission | `3.4.a` Objectifs de la mission d'audit de durabilité ; `3.4.b` Démarche | 3 |
| 3.9 Taux de calcin : procédures, recalcul ; avis par axe | `3.4.b` Démarche ; `3.4.c` Portée des avis | 3 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes annuels (18 points)

### 3.1 Cadres d'exercice comparés ; demandes de la présidente (4 pts)

**Comparaison des trois cadres d'exercice (2,5 pts)**

| | Expert-comptable | Commissaire aux comptes | Auditeur de durabilité | Points |
|---|---|---|---|---:|
| Nature de l'intervention | Mission **contractuelle** : tenir, centraliser, arrêter, réviser et apprécier les comptabilités, analyser la situation de l'entité [V ord. 45-2138 art. 2] ; contrat écrit (lettre de mission), honoraires convenus par écrit [V décret 2012-432 art. 151 ; ord. art. 24] | **Missions** confiées par la loi, dont la certification des comptes, mission d'intérêt général délivrant une assurance raisonnable, et **prestations** hors mission [V L. 821-2 III-IV, L. 821-53 ; NEP principes § 08] ; désignation par l'organe délibérant, mandat de six exercices [V L. 821-40 I, L. 821-44] | Certification des informations en matière de durabilité, sur la base d'une **assurance limitée** [V L. 821-54 II ; L. 822-1 ; LD 2026] ; mandat de six exercices, ou trois si la désignation n'est pas imposée par la loi, comme ici [V L. 821-44, L. 821-46 ; L. 822-20] | 0,75 |
| Conditions d'exercice | Inscription au **tableau de l'ordre** : droits civils, honorabilité, **diplôme d'expertise comptable** [V ord. art. 3] ; serment [V décret art. 143] | Inscription sur la **liste tenue par la H2A** : honorabilité, stage de trois ans, certificat d'aptitude ou diplôme d'expertise comptable [V L. 821-13 I, L. 821-14 ; R. 821-46] ; serment [V L. 821-23] | Soit un **CAC** inscrit sur la **liste spéciale** de la H2A (stage d'au moins huit mois auprès d'un professionnel de la durabilité et **épreuve** sur la certification de durabilité) [V L. 821-13 II, L. 821-18 I] ; soit un **organisme tiers indépendant** (OTI), personne morale **accréditée** par le comité français d'accréditation, dont l'auditeur personne physique (master, stage de huit mois, même épreuve) est inscrit sur une liste de la H2A [V L. 822-3, L. 822-4] | 1 |
| Instances | **CROEC** (tableau, surveillance, conciliation) et **CNOEC** [V ord. art. 1, 28, 31, 33] ; discipline : chambres régionales et nationale de discipline [V ord. art. 49-50] | **H2A**, autorité publique indépendante (inscription, normes, contrôles, sanctions) ; **CNCC** (représentation de la profession) et **CRCC** [V L. 820-1, L. 821-12] | **H2A** (listes, normes, contrôles, commission des sanctions) [V L. 820-1, L. 822-37] ; même **code de déontologie** que les CAC [V L. 822-7] | 0,75 |

On valorise la conclusion d'ensemble : l'expert-comptable **produit** les comptes pour son client ; le commissaire aux comptes et l'auditeur de durabilité **vérifient**, pour les utilisateurs, une information produite par d'autres, ce qui fonde leur exigence d'indépendance en réalité et en apparence [V code de déontologie art. 5 ; S, synthèse F10 § 3].

**Demande 1 : tenue de la comptabilité et établissement des comptes à partir de 2027 (0,75 pt)**
- Ce sont des **prestations** relevant de l'expertise comptable. ARNÉVAL, société d'expertise comptable et de commissariat aux comptes, peut les fournir à d'autres clients, mais pas à une entité dont il certifie les comptes : il se prononcerait sur des comptes qu'il a lui-même établis. C'est le **risque d'autorévision**, qu'aucune mesure de sauvegarde ne peut réduire, une autre équipe du même cabinet restant le même cabinet [V code de déontologie art. 5 II ; F10 § 3, application : S].
- CHAMPLOVERRE n'est pas une EIP : aucune liste fermée de services interdits ne s'applique, mais le commissaire aux comptes ne peut **ni accepter ni poursuivre** une mission de certification des comptes ou des informations en matière de durabilité en cas de risque d'autorévision sans sauvegarde possible [V L. 821-28 IV]. Les deux missions d'ARNÉVAL seraient touchées : l'état de durabilité reprend des données comptables (connectivité).
- **Réponse** : ARNÉVAL refuse par écrit et documente son analyse [V NEP documentation § 04-08]. La présidente peut confier la tenue à un expert-comptable extérieur au cabinet et à son réseau, ou réorganiser son service comptable. L'argument « vous gagnerez du temps pour les certifier » montre le risque : une certification qui s'appuierait sur son propre travail perdrait sa valeur.

**Demande 2 : signature par M. SERMAISE ou recours à un OTI (0,75 pt)**
- M. SERMAISE **ne peut pas signer** : dans une société de commissaires aux comptes, le rapport de certification des informations en matière de durabilité est signé par un **commissaire aux comptes personne physique**, associé, actionnaire ou dirigeant de la société et **inscrit sur la liste spéciale** [V L. 821-26]. Il n'est ni commissaire aux comptes, ni inscrit, ni associé ; son inscription au tableau de l'ordre ne l'habilite pas. Il peut en revanche participer aux travaux comme **collaborateur** désigné, sous la responsabilité de Mme LOMBARDET [V L. 821-60 al. 2].
- Mme LOMBARDET répond à la demande de PENDRAVEN : elle est indépendante, inscrite sur la liste des commissaires aux comptes habilités à certifier les informations en matière de durabilité et soumise au même code de déontologie qu'un OTI [V L. 821-13 II, L. 822-7].
- Un **OTI** est une autre voie possible, avec un niveau d'assurance et des règles identiques. Le mandat d'ARNÉVAL court jusqu'à l'exercice 2028 : un OTI ne pourrait être désigné par les associés qu'à son expiration, sauf cessation anticipée dans les cas prévus (démission pour motif légitime, relèvement en justice pour faute ou empêchement), qu'aucun élément du cas ne caractérise [V L. 822-17 ; F09 § 3.7 et 4.2 ; S, application par hypothèse : mission conduite dans les conditions de la certification légale].
- Le cumul de la certification des comptes et de celle des informations en matière de durabilité par ARNÉVAL est **compatible** : le même commissaire aux comptes peut exercer les deux missions [V L. 821-26 ; F09 § 4.3]. Les honoraires de la mission de durabilité sont fixés d'un commun accord, hors barème [V R. 821-194].

**Réponses tolérées**
- Une comparaison rédigée plutôt qu'un tableau, si les trois critères sont traités pour les trois professions.
- Le seul motif « M. SERMAISE n'est pas commissaire aux comptes inscrit sur la liste spéciale », sans la condition de qualité d'associé : points accordés.
- Une intervention complémentaire d'un OTI, contractuelle, la publication étant volontaire, si le candidat note qu'elle ferait double emploi avec la certification confiée à ARNÉVAL et ne la remplace pas.
- La mention de la démission d'ARNÉVAL comme moyen de libérer le mandat, si le candidat ajoute qu'elle doit reposer sur un motif légitime et ne peut pas servir à accepter une prestation [V code de déontologie art. 28].

**Erreurs fréquentes**
- Accepter la tenue au motif que CHAMPLOVERRE n'est pas une EIP, ou que le cabinet est aussi expert-comptable (`JUR-A03`).
- Transposer à l'expert-comptable l'exigence d'indépendance du commissaire aux comptes, ou l'inverse (`JUR-A03`).
- Confondre l'inscription au tableau de l'ordre avec l'inscription sur les listes de la H2A (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 1-3, 24, 28, 31, 33, 49-50 ; décret 2012-432 art. 143, 151 | Expert-comptable : mission, conditions, instances | [V] | F09 § 1, 2 |
| C. com. L. 820-1, L. 821-12 à L. 821-14, L. 821-18, L. 821-23, L. 821-26, L. 821-40, L. 821-44, L. 821-46, L. 822-3, L. 822-4, L. 822-7, L. 822-17, L. 822-20, R. 821-46, R. 821-194 | CAC et auditeur de durabilité : listes, conditions, signature, durée, honoraires | [V] | F09 § 1, 3, 4 ; F11 § 2 |
| C. com. L. 821-2, L. 821-28 IV ; code de déontologie art. 5, 28 | Missions et prestations ; autorévision hors EIP ; démission | [V] ; application : [S] | F10 § 3, 5 ; F09 § 3.7 |

### 3.2 Refus de la présidente et moyens d'action sur les litiges (3 pts)

**Refus 1 : interroger l'avocate de la société (1,25 pt)**
- **Droit applicable (0,5 pt)** : le commissaire aux comptes peut recueillir toutes informations utiles auprès des **tiers** qui ont accompli des opérations pour le compte de l'entité ; la communication des pièces détenues par ces tiers suppose une décision de justice [V L. 821-61 al. 2]. Le secret professionnel ne lui est pas opposable, **sauf par les auxiliaires de justice** [V L. 821-61 al. 3] : Me ORMOY, avocate, peut lui opposer son secret [S, qualification de l'avocat].
- **Norme pertinente (0,5 pt)** : c'est pourquoi la norme relative aux applications spécifiques du caractère probant prévoit que, lorsqu'il a identifié des litiges susceptibles d'engendrer des anomalies significatives, le commissaire aux comptes **demande à la direction** d'obtenir de ses avocats des informations sur ces litiges et de les lui communiquer [V NEP applications spécifiques § 7]. La demande est signée par la présidente, qui délie ainsi son avocate du secret envers ARNÉVAL, et la réponse est adressée **directement** au cabinet, comme le 28/01/2027 [S, pratique ; cohérent avec NEP éléments probants § 6].
- **Portée du refus (0,25 pt)** : l'offre de la présidente (« je vous transmettrai moi-même ») ne suffit pas : une information sélectionnée par la direction est moins fiable qu'un élément obtenu directement d'un tiers [V NEP éléments probants § 6]. Si la direction refuse de demander ou de communiquer les informations des avocats, le commissaire aux comptes en tire les conséquences dans son rapport [V NEP applications spécifiques § 8] : limitation de l'étendue des travaux, donc réserve ou impossibilité de certifier selon que les incidences sont ou non circonscrites [V NEP rapport § 11, 14].

**Refus 2 : compte rendu du comité de direction (1 pt)**
- Le droit de communication n'est pas limité aux pièces comptables : le commissaire aux comptes se fait communiquer **sur place toutes les pièces qu'il estime utiles**, notamment les contrats, livres, documents comptables et **registres des procès-verbaux** [V L. 821-60 al. 1]. Un compte rendu qui examine un litige de 1 150 000 € est utile : il renseigne sur l'appréciation du risque par la direction. La norme sur les événements postérieurs prévoit d'ailleurs la consultation des comptes rendus des réunions de direction [V NEP événements postérieurs § 06].
- Le refus de communiquer une pièce constitue un **obstacle aux vérifications**, délit puni de cinq ans d'emprisonnement et de 75 000 € d'amende pour les dirigeants [V L. 821-6 3°]. Il crée aussi une **limitation**, avec ses conséquences sur l'opinion.

**Conduite à tenir par ARNÉVAL (0,75 pt)**
- Rappeler par écrit à la présidente ses droits et les conséquences d'un refus, après un entretien ; consigner les échanges dans le dossier [V NEP documentation § 04-08].
- Identifier tous les litiges par d'autres moyens : examen des comptes d'honoraires (6226) pour recenser **tous les avocats** consultés, ici deux cabinets, du tableur des réclamations du service qualité, de la correspondance juridique et des assignations [V NEP applications spécifiques § 7 ; S, procédures].
- Obtenir une **déclaration écrite** de la présidente sur l'exhaustivité des litiges et sur les événements postérieurs, en sachant qu'elle ne remplace pas les éléments que la direction refuse de fournir et doit être corroborée [V NEP déclarations écrites § 4, 6-7].
- Porter à la connaissance de la présidente les modifications qui lui paraissent devoir être apportées aux comptes et les irrégularités relevées [V L. 821-63 I 2°, 5°]. En l'espèce, la présidente a accepté le 25/01/2027 : la limitation est levée.

**Réponses tolérées**
- La « demande de confirmation des tiers » adressée aux avocats, si le candidat précise qu'elle passe par la direction et que la réponse revient directement au cabinet.
- L'absence de mention du délit d'obstacle, si la limitation et ses conséquences sont présentées.

**Erreurs fréquentes**
- Écrire que le secret professionnel n'est jamais opposable au commissaire aux comptes, en oubliant l'exception des auxiliaires de justice (`JUR-A01`).
- Accepter le refus du compte rendu au motif qu'il ne s'agit pas d'une pièce comptable.
- Énumérer les moyens d'action sans dire ce qu'ils permettent d'obtenir dans le cas (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-6 3°, L. 821-60, L. 821-61, L. 821-63 I | Communication, tiers, secret, délit d'obstacle, communication avec les organes | [V] | F09 § 5 ; F11 § 2, 5 |
| NEP applications spécifiques § 7-8 ; NEP éléments probants § 6 ; NEP déclarations écrites § 4, 6-7 | Litiges : avocats ; fiabilité ; déclarations | [V] ; application : [S] | F11 § 6.1, 6.4, 12.3, 12.4 |
| NEP rapport § 11, 14 | Conséquences d'une limitation | [V] | F11 § 8 |

### 3.3 Cycle provisions et litiges (4 pts)

**a. Risque d'anomalies significatives et orientation des travaux (1,25 pt)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41]
- **Risque inhérent élevé (0,5 pt)** :
  - les provisions pour litiges sont des **estimations**, qui reposent sur le jugement et sur des événements futurs incertains ; la présidente les fixe seule, avec un **biais** apparent (« DURANCET exagère ») ;
  - le litige DURANCET porte sur 1 150 000 €, soit **3,8 fois** le seuil de signification ;
  - l'incident de production de juin 2026 a touché **trois** clients, dont deux n'avaient pas encore réclamé : risque d'**exhaustivité** ;
  - des événements de l'exercice (transaction CARVÉLIS du 18/12/2026) peuvent ne pas être traduits dans les comptes.
- **Risque lié au contrôle élevé (0,25 pt)** : le tableur des réclamations n'est pas transmis à la comptabilité ; aucune procédure écrite ne régit l'estimation des provisions ; la présidente décide seule. Sans test des contrôles, le risque d'anomalies significatives au niveau des assertions correspond au risque inhérent évalué [V NEP risques § 41].
- **Orientation (0,5 pt)** : le risque d'anomalies significatives étant élevé, le risque de non-détection acceptable est **faible**. ARNÉVAL met en œuvre des **procédures de substance**, privilégie les éléments **externes** (avocats, jugements, tiers), examine les événements postérieurs jusqu'à la signature du rapport et confie le cycle à un membre expérimenté de l'équipe [V NEP principes § 13 ; NEP réponses § 03-13 ; NEP éléments probants § 6].

**b. Risques, assertions et procédures (1,5 pt : 0,5 pt par risque pertinent, avec son assertion et une procédure justifiée, dans la limite de trois)**

| Risque | Assertion | Procédure et justification |
|---|---|---|
| Litiges non recensés ou non provisionnés (autres maisons livrées en bouteilles défectueuses, litiges suivis par le second cabinet d'avocats) | **Exhaustivité** des provisions (solde) et des informations de l'annexe | **Demande à la direction d'interroger tous ses avocats**, recensés à partir du compte 6226 ; examen du tableur des réclamations, des comptes rendus du comité de direction et de la correspondance juridique ; liste des clients livrés en bouteilles de la série du 2 au 20 juin 2026 ; **déclaration écrite** sur l'exhaustivité des litiges. Ces éléments, dont certains sont externes, révèlent les litiges que la comptabilité ignore |
| Provision DURANCET sous-évaluée par rapport à la meilleure estimation | **Évaluation** (solde) | Comparaison de la provision avec la **réponse de l'avocate** et le rapport d'expertise ; examen critique des hypothèses de la présidente ; suivi du **jugement** attendu en février 2027 (événement postérieur). La réponse de l'avocate est un élément externe, obtenu directement |
| Provision CARVÉLIS maintenue alors que le litige est éteint par la transaction du 18/12/2026 | **Existence** et **droits et obligations** de la provision ; **exhaustivité** des dettes (solde) | Examen de la **transaction** et du paiement du 08/01/2027 sur le relevé bancaire ; contrôle de la reprise de la provision et de la comptabilisation de la dette de 30 000 € au 31/12/2026 |
| Litige prud'homal absent de l'annexe | **Exhaustivité** et **présentation** des informations de l'annexe | Réponse du second cabinet d'avocats ; lecture de l'annexe ; vérification de la mention du passif éventuel |

Autres réponses acceptées : classement des dotations (charges d'exploitation, et non financières) ; **séparation des exercices** des honoraires d'avocats (examen des factures reçues en janvier 2027) ; **réalité** des reprises de provisions.

**c. Appréciation au 28/01/2027 (1,25 pt)**
- **Litige DURANCET (0,75 pt)** :
  - l'**obligation existe à la clôture** : les bouteilles défectueuses ont été livrées en juin 2026 et DURANCET a assigné la société le 14/10/2026 ; la sortie de ressources est **probable** selon l'avocate. Une provision est donc requise [V PCG art. 322-2, 322-8] ;
  - pour une obligation unique, le montant à provisionner est en général celui de l'**hypothèse la plus probable**, soit **700 000 €**, et les incertitudes (fourchette de 550 000 € à 850 000 €) sont mentionnées dans l'annexe [V PCG art. 323-2 ; annexe 3.3]. Le préjudice commercial, peu probable, n'est pas provisionné ;
  - la provision de 380 000 € est **insuffisante de 320 000 €** (700 000 − 380 000), soit 1,1 fois le seuil de signification de 300 000 € : c'est une **anomalie significative**, dont ARNÉVAL demande la correction. L'argument de la présidente n'est pas une estimation : il n'est étayé par aucun élément, alors que l'expertise judiciaire établit le défaut [V NEP déclarations écrites § 4-5 ; NEP anomalies § 8-17].
- **Litige prud'homal (0,5 pt)** : une condamnation est **peu probable** : la sortie de ressources n'étant pas probable, l'obligation est un **passif éventuel**. Elle n'est pas provisionnée, mais elle doit être **mentionnée dans l'annexe** [V PCG art. 321-6, 322-5]. L'absence de provision est correcte ; l'absence de mention est une omission d'information, que la société doit corriger. Son montant (85 000 €, 28,3 % du seuil) n'enlève rien à l'obligation d'informer.

**Réponses tolérées**
- Pour DURANCET, une provision au haut de la fourchette (850 000 €), si le candidat la justifie par la prudence et conclut aussi à une insuffisance significative : 0,5 pt sur 0,75. La règle de l'hypothèse la plus probable est attendue.
- Le classement du risque CARVÉLIS sous l'« évaluation » de la provision, si le candidat voit que la provision doit être reprise et la dette comptabilisée.

**Erreurs fréquentes**
- Confondre réalité (flux) et existence (solde), ou exhaustivité et séparation des exercices (`JUR-A01`).
- Provisionner le montant réclamé par DURANCET (1 150 000 €) ou le litige prud'homal (`JUR-F07`).
- Proposer des procédures sans les relier au risque identifié (`JUR-A05`, `JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 10-13 ; NEP risques § 02, 39-41 ; NEP réponses § 03-13 | RAS, risque de non-détection, procédures de substance | [V] | F11 § 4.1, 5 |
| NEP éléments probants § 6, 9 ; NEP applications spécifiques § 7 ; NEP déclarations écrites § 4-7 | Assertions ; fiabilité ; avocats ; déclarations | [V] | F11 § 4.3, 6.1, 12.3, 12.4 |
| PCG art. 321-6, 322-2, 322-5, 322-8, 323-2 | Provision, hypothèse la plus probable, passif éventuel | [V] | F11 § 12.5 |
| NEP anomalies § 8-17 | Demande de correction des anomalies | [V] | F11 § 5 |

### 3.4 Norme sur les événements postérieurs : corpus, identification, trois événements, écriture (4 pts)

**Place de la norme dans le corpus (0,5 pt)**
- C'est une **norme d'exercice professionnel**, de la famille des normes relatives aux **éléments probants**, à côté des normes sur les procédures analytiques, les estimations, la continuité d'exploitation ou les déclarations de la direction [V F11 § 3.3 ; S, lecture par familles].
- Comme toute NEP, elle relève de la procédure suivante : projet préparé par la **commission de normalisation** placée auprès de la H2A, **avis de la CNCC**, **adoption** par le collège de la H2A, **homologation par arrêté du garde des sceaux** ; elle est codifiée dans la partie « Arrêtés » du Code de commerce. Les NEP s'appliquent à défaut de normes internationales adoptées par la Commission européenne, aucune ne l'ayant été [V L. 820-4, L. 820-23, L. 821-11 I ; F11 § 3.1-3.2].

**Identification des événements postérieurs (0,5 pt)** [V NEP événements postérieurs § 05-07]
- Prendre connaissance de la façon dont la présidente recense les événements postérieurs ; consulter les **comptes rendus** du comité de direction et les décisions tenues depuis le 01/01/2027 ; examiner les situations mensuelles de janvier et février 2027 et le **budget 2027** ; s'enquérir de l'évolution des **litiges** auprès de la présidente et des **avocats** ; lire le registre des réclamations clients après la clôture ; interroger la présidente.
- Mettre en œuvre ces procédures **jusqu'à une date aussi proche que possible du 06/04/2027** et obtenir une **déclaration écrite** de la présidente, datée au plus près de la signature, attestant qu'aucun autre événement postérieur n'appelle de traitement ou de mention [V NEP déclarations écrites § 7, 10].

**Événement 1 : jugement DURANCET du 16/02/2027 (1 pt)**
- **Date** : survenu et identifié **entre la clôture et l'arrêté des comptes** (12/03/2027).
- **Lien avec la clôture** : le jugement **confirme et chiffre** une obligation qui existait au 31/12/2026 (bouteilles défectueuses livrées en juin 2026, assignation d'octobre). Il appelle un **enregistrement comptable** : il est tenu compte des passifs nés au cours de l'exercice même s'ils sont connus entre la clôture et l'établissement des comptes, et les provisions sont ajustées à la meilleure estimation à la date d'établissement des comptes [V C. com. L. 123-20 al. 3 ; PCG art. 322-2, 323-10 ; NEP événements postérieurs § 02].
- **Montant** : la décision de ne pas faire appel fixe le montant dû à **760 000 €** (745 000 + 15 000). La provision du projet (380 000 €) est insuffisante de **380 000 €**, soit 1,3 fois le seuil : anomalie significative.
- **Diligences** : ARNÉVAL a vérifié le traitement comptable, demandé la modification des comptes, obtenue avant l'arrêté [V NEP événements postérieurs § 08] ; en cas de refus, il aurait évalué l'incidence sur son opinion [V § 09]. Il vérifie le paiement d'avril 2027 lors de ses dernières procédures, s'il intervient avant la signature.

**Écriture passée au 31/12/2026 (0,5 pt)**

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 6815 | Dotations aux provisions d'exploitation | 380 000 | |
| 1511 | Provisions pour litiges | | 380 000 |

Libellé : complément de provision pour le litige DURANCET, porté au montant de la condamnation du 16/02/2027. Le résultat courant avant impôt passe de 6 000 000 € à **5 620 000 €**.

**Événement 2 : incident du four n° 2 du 08/02/2027 (0,75 pt)**
- **Date** : survenu entre la clôture et l'arrêté des comptes. **Pas de lien direct** avec une situation existant à la clôture : l'inspection de décembre 2026 était normale et l'expert conclut que rien ne laissait prévoir l'incident au 31/12/2026.
- **Comptes 2026** : aucun ajustement. Aucune dépréciation du four n° 2 (valeur nette comptable de 3 100 000 €) n'est à constater au 31/12/2026, faute d'indice à cette date ; les pertes d'exploitation futures, qui ne sont pas un passif, ne sont pas provisionnées [V PCG art. 322-12]. La reconstruction et la sortie éventuelle des éléments détruits relèvent de 2027.
- **Information** : l'événement est **important** (baisse attendue du chiffre d'affaires de 14 000 000 €, soit 11,1 % du chiffre d'affaires de 2026 ; reconstruction de 7 200 000 €, soit 6,4 % du total du bilan). Il est décrit dans l'**annexe** et dans le **rapport de gestion** [V PCG art. 831-1, 4° ; NEP événements postérieurs § 02-03]. ARNÉVAL vérifie que ces informations sont données et cohérentes avec le rapport de l'expert, le devis et le budget 2027 [V § 10] ; à défaut de mention dans le rapport de gestion, il aurait formulé une observation [V § 11]. Il apprécie aussi ses conséquences sur la **continuité d'exploitation** : le prêt du 05/03/2027 et la trésorerie écartent toute incertitude significative [V NEP continuité d'exploitation § 2].

**Événement 3 : réclamation VERGELOT du 24/03/2027 (0,75 pt)**
- **Date** : survenue **après l'arrêté des comptes** (12/03/2027) et identifiée avant la signature du rapport. Au-delà de l'arrêté, **aucun traitement comptable** n'est prévu, sauf si la société arrête de nouveau ses comptes, ce qu'elle refuse [V NEP événements postérieurs § 02]. À la date d'établissement des comptes, aucune réclamation des deux autres maisons n'était connue et le risque ne pouvait pas être estimé : l'absence de provision au 31/12/2026 n'est pas une anomalie [V PCG art. 322-2, 322-4]. Ce risque figure dans l'annexe comme **passif éventuel** (annexe 3.5) ; la réclamation, survenue après l'arrêté, le précise sans appeler de traitement comptable [V PCG art. 321-6, 322-5].
- **Diligence** : ARNÉVAL s'enquiert auprès de la présidente de son **intention d'informer les associés** ; elle le fera lors de la décision du 10/06/2027. Le rapport n'a donc pas à en faire mention ; si cette communication n'était pas prévue, ARNÉVAL en ferait **mention dans son rapport** [V § 14].
- **Portée** : 150 000 €, soit 50 % du seuil. ARNÉVAL étend ses procédures à la troisième maison livrée et fait figurer ces réclamations dans la déclaration écrite [V NEP déclarations écrites § 7].

**Réponses tolérées**
- Pour l'événement 1, une **dette** de 760 000 € (charge à payer) au lieu d'une provision, au motif que le montant et l'échéance sont fixés, si le candidat présente une écriture équilibrée et le même effet sur le résultat (380 000 €) [S, débat de classement ; PCG art. 321-4, 321-5].
- Pour l'événement 3, une recommandation de procéder volontairement à un nouvel arrêté des comptes, si le candidat indique que la société n'y est pas tenue.
- Pour l'événement 3, un traitement comme révélation d'une situation existant à la clôture (événement survenu avant l'arrêté, identifié avant la signature) : si le candidat cumule les 150 000 € avec les anomalies non corrigées, la surévaluation nette du résultat est de 123 000 € (150 000 + 18 000 − 45 000), soit 41,0 % du seuil, et de 213 000 € en valeur absolue, soit 71,0 % : le cumul n'est pas significatif et l'opinion ne change pas. Points accordés si le raisonnement est complet.

**Erreurs fréquentes**
- Traiter les trois événements de la même façon, sans distinguer la date de survenance (avant ou après l'arrêté) et le lien avec la situation à la clôture (`JUR-A05`).
- Déprécier le four n° 2 ou provisionner les pertes d'exploitation de 2027 dans les comptes de 2026.
- Citer les règles de l'annexe 3.4 sans les appliquer aux faits et aux dates du cas (`JUR-A06`, `JUR-F07`).
- Oublier le numéro, l'intitulé ou le libellé de l'écriture (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 820-4, L. 820-23, L. 821-11 I | Élaboration et homologation des NEP | [V] | F11 § 3.1-3.3 |
| NEP événements postérieurs § 02-03, 05-11, 14 ; NEP déclarations écrites § 7, 10 ; NEP continuité d'exploitation § 2 | Identification et incidences des événements postérieurs | [V] ; application : [S] | F11 § 5, 12.1, 12.3 |
| C. com. L. 123-20 al. 3 ; PCG art. 321-4, 321-5, 321-6, 322-2, 322-4, 322-5, 322-12, 323-10, 831-1 (4°) | Passifs connus après la clôture ; ajustement ; pertes futures ; information de l'annexe | [V] | F11 § 12.5 |

### 3.5 Opinion avec observation ; observation et réserve (3 pts)

**a. Opinion et forme du rapport (2 pts)**

*Anomalies non corrigées (0,75 pt)*

| Anomalie non corrigée | Effet sur le résultat avant impôt | Rapport au seuil (300 000 €) |
|---|---:|---:|
| Provision CARVÉLIS maintenue | sous-évaluation de 45 000 € | 15,0 % |
| Honoraires d'avocats de décembre 2026 | surévaluation de 18 000 € | 6,0 % |
| **Effet net** | **sous-évaluation de 27 000 €** | 9,0 % |
| **Cumul en valeur absolue** | 63 000 € | 21,0 % |

- Les anomalies non corrigées, seules ou cumulées, restent **largement inférieures** au seuil, y compris si le seuil est révisé pour tenir compte du résultat corrigé (5 % de 5 620 000 € = 281 000 €) [V NEP caractère significatif § 22-23]. Aucune n'est significative par sa **nature** ou par les **circonstances**, et aucune ne subsiste des exercices antérieurs [V NEP caractère significatif § 9 ; NEP anomalies § 14].
- L'argument de la présidente sur la provision CARVÉLIS est inexact : la prudence ne justifie pas une provision devenue sans objet, qui doit être reprise [V PCG art. 323-12 ; C. com. L. 123-20]. ARNÉVAL joint l'état des anomalies non corrigées à la **déclaration écrite** de la présidente, qui les juge non significatives [V NEP déclarations écrites § 7 ; NEP anomalies § 15-17].

*Opinion (0,5 pt)* : les anomalies significatives ont été corrigées (provision DURANCET, mention du litige prud'homal et du risque lié aux deux autres maisons livrées), aucune limitation ne subsiste et aucune incertitude significative ne pèse sur la continuité d'exploitation : Mme LOMBARDET formule une **certification sans réserve** : ARNÉVAL a obtenu l'assurance raisonnable que les comptes, pris dans leur ensemble, ne comportent pas d'anomalies significatives [V NEP rapport § 08 ; R. 821-180].

*Observation (0,75 pt)*
- L'incident du four n° 2 est correctement traité et décrit dans l'annexe, mais il est **important** pour la compréhension des comptes et de la situation de la société : production interrompue douze semaines, baisse attendue du chiffre d'affaires de 11,1 %, reconstruction de 7 200 000 € financée par emprunt. Mme LOMBARDET formule une **observation**, faculté que lui reconnaissent les textes (« toute observation utile ») : elle **attire l'attention** des associés sur la note « Événements postérieurs à la clôture » de l'annexe [V R. 821-180 ; NEP rapport § 07 ; S, jugement professionnel].
- L'observation figure dans une **partie distincte**, placée après le fondement de l'opinion et **avant la justification des appréciations** ; formulation d'usage : sans remettre en cause l'opinion exprimée, nous attirons votre attention sur la note de l'annexe qui expose l'incident survenu le 08/02/2027 et ses conséquences estimées [V NEP rapport § 07, 18 ; S, formulation d'usage].
- Mme LOMBARDET en **communique les motifs** au préalable à la présidente [V NEP rapport § 07 ; L. 821-63 I]. Le souhait d'un rapport « le même que l'an dernier » est sans portée : le contenu du rapport relève du seul commissaire aux comptes.
- Le rapport comporte aussi l'opinion, son fondement (référentiel d'audit, indépendance), la **justification des appréciations** (par exemple sur l'estimation de la provision DURANCET), la vérification du rapport de gestion, le rappel des responsabilités, la date et la signature de Mme LOMBARDET [V NEP rapport § 15, 18].

**b. Observation et réserve ; refus hypothétique de la présidente (1 pt)**
- **Distinction (0,5 pt)** :

| | Observation | Réserve |
|---|---|---|
| Effet sur l'opinion | Aucun : la certification reste sans réserve | Modifie l'opinion : certification avec réserve |
| Motif | Attirer l'attention sur une information **déjà fournie dans l'annexe** ; obligatoire si un texte la prévoit (changement de méthode) | **Désaccord** (anomalie significative non corrigée) ou **limitation** des travaux, aux incidences clairement circonscrites |
| Place dans le rapport | Partie distincte, avant la justification des appréciations | Motifs exposés dans le « Fondement de l'opinion », incidences quantifiées au mieux |
| Contenu | Ne peut pas apporter d'information que la direction n'a pas donnée | Décrit et chiffre ce qui ne va pas |

  [V NEP rapport § 06-11]
- **Refus hypothétique de décrire l'incident dans l'annexe (0,5 pt)** : l'annexe omettrait une information requise sur un événement important [V PCG art. 831-1, 4°]. Ce serait une **anomalie** (exhaustivité de l'information de l'annexe) significative par sa nature, que la présidente refuserait de corriger. Une observation serait impossible, puisqu'elle ne peut que renvoyer à une information de l'annexe et que le commissaire aux comptes ne peut pas fournir lui-même une information dont la diffusion relève des dirigeants [V NEP rapport § 07]. L'incidence étant circonscrite à une information identifiée, Mme LOMBARDET formulerait une **certification avec réserve pour désaccord**, en décrivant l'omission dans le fondement de l'opinion [V NEP rapport § 09-10 ; S, qualification]. Si le rapport de gestion omettait aussi l'incident, elle formulerait en outre une observation à ce titre [V NEP événements postérieurs § 11].

**Réponses tolérées**
- Un **refus de certifier**, si le candidat soutient qu'une réserve ne suffirait pas à informer l'utilisateur sur un événement de cette ampleur : 0,25 pt sur 0,5 au dernier point.
- L'absence d'observation, si le candidat discute expressément la faculté d'en formuler une et justifie son choix : 0,25 pt sur 0,75 au point de l'observation.

**Erreurs fréquentes**
- Formuler une réserve pour l'incident du four, alors que les comptes ne comportent aucune anomalie à ce titre (`JUR-A02`).
- Confondre observation et incertitude significative sur la continuité d'exploitation, qui n'existe pas ici.
- Comparer au seuil une seule anomalie, sans cumul ni appréciation de la nature (`JUR-F02`).
- Donner l'opinion sans ses motifs ni la forme du rapport (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP caractère significatif § 9, 22-23 ; NEP anomalies § 14-17 ; NEP déclarations écrites § 7 | Appréciation des anomalies non corrigées ; déclaration écrite | [V] | F11 § 4.2, 5, 12.3 |
| NEP rapport § 06-11, 15, 18 ; C. com. R. 821-180, L. 821-63 I | Opinions, observation, structure du rapport | [V] ; application : [S] | F11 § 8, 12.2 |
| PCG art. 323-12, 831-1 (4°) ; C. com. L. 123-20 | Reprise d'une provision sans objet ; information de l'annexe | [V] | F11 § 12.5 |
| NEP événements postérieurs § 11 ; NEP continuité d'exploitation § 2 | Observation pour défaut d'information du rapport de gestion ; continuité | [V] | F11 § 5, 12.1 |

---

### Partie B – Durabilité (12 points)

### 3.6 ISSB, EFRAG, GRI ; demande de PENDRAVEN ; étendue et limites (3 pts)

**Normalisateurs, normes et matérialité (1,5 pt : 0,5 pt par normalisateur)**

| Normalisateur | Statut et normes | Approche de la matérialité |
|---|---|---|
| **ISSB** (International Sustainability Standards Board) | Organisme de normalisation de la Fondation IFRS ; **IFRS S1** (exigences générales) et **IFRS S2** (climat), publiées le 26/06/2023 ; elles reprennent les recommandations de la TCFD [S] | **Financière** : risques et opportunités liés à la durabilité susceptibles d'affecter les flux de trésorerie, l'accès au financement ou le coût du capital ; destinataires : les **investisseurs** [S] |
| **EFRAG** (European Financial Reporting Advisory Group) | **Conseiller technique** de la Commission européenne : il prépare les projets d'**ESRS**, que la Commission adopte par règlements délégués (2023/2772, puis ESRS révisées par 2026/1563) ; architecture : normes transversales (ESRS 1 exigences générales, ESRS 2 informations générales) et normes thématiques environnementales, sociales et de gouvernance [V règl. délégué 2026/1563, consid. 3 ; ESRS 1 (2026) § 8-10] | **Double matérialité** : matérialité d'impact et matérialité financière ; utilisateurs à usage général (investisseurs et prêteurs, mais aussi partenaires commerciaux, partenaires sociaux, société civile) [V ESRS 1 (2026) § 3-4, 35] |
| **GRI** (Global Reporting Initiative) | Normes universelles, normes par secteur et normes par thème [S] | **Impact** : impacts de l'organisation sur l'économie, l'environnement et les personnes [S] |

**Interopérabilité (0,5 pt)**
- **ESRS et GRI** : déclaration commune de l'EFRAG et de la GRI (fin août et début septembre 2023) : définitions et indicateurs d'impact alignés ; une entité qui publie selon les ESRS est considérée comme publiant « with reference to » les normes GRI [V page EFRAG ; F12 § 1].
- **ESRS et ISSB** : guide d'interopérabilité de la Fondation IFRS et de l'EFRAG (mai 2024) : la matérialité financière des ESRS est alignée sur la définition de la matérialité d'IFRS S1, avec une forte convergence sur le climat [S]. Les ESRS révisées recherchent, dans toute la mesure du possible, l'interopérabilité avec les normes mondiales [V règl. délégué 2026/1563, consid. 2].
- Formule de synthèse : GRI = impact ; ISSB = financier ; ESRS = double matérialité, qui réunit les deux angles [S, cohérent avec ESRS 1 (2026) § 2 et 23].

**Réponse à la présidente : étendue et limites (1 pt)**
- **Pas de second rapport obligatoire** : aucun texte n'impose à CHAMPLOVERRE de publier selon les normes de l'ISSB ; c'est une exigence commerciale de PENDRAVEN [S]. L'état de durabilité permet de répondre en grande partie à sa demande :
  - **demande 1** : les risques et opportunités liés au climat sont analysés au titre de la **matérialité financière**, à court, moyen et long terme (prix du gaz, accès au calcin, exigences des clients, four hybride) [V ESRS 1 (2026) § 47-48, 50]. CHAMPLOVERRE peut transmettre ces informations en signalant le référentiel suivi ;
  - **demande 3** : les informations ESRS répondent à l'approche de la GRI (« with reference to ») et, pour la matérialité financière, à celle de l'ISSB. CHAMPLOVERRE ne peut toutefois pas affirmer qu'elle applique les normes de l'ISSB sans en respecter toutes les exigences [S, déduction].
- **Étendue** : l'état de durabilité présente tous les impacts, risques et opportunités **matériels**, pour les activités propres de CHAMPLOVERRE et pour sa **chaîne de valeur** amont et aval dans la mesure nécessaire [V ESRS 1 (2026) § 3, 60-65].
- **Limites** :
  - informations **matérielles** seulement : un enjeu jugé non matériel n'y figure pas [V ESRS 1 (2026) § 24] ;
  - informations établies **au niveau de l'entité** : la **demande 2**, sur les émissions des seules bouteilles livrées à PENDRAVEN, appelle un calcul propre à ce client. Ce calcul ne figure pas dans l'état de durabilité et n'est pas couvert par la certification d'ARNÉVAL [S] ;
  - certaines données de la chaîne de valeur sont des **estimations**, comme les émissions des transporteurs [V ESRS 1 (2026) § 62-65] ;
  - assurance **limitée** seulement, sans informations relatives à la taxonomie.

**Réponses tolérées**
- La mention de l'adoption des normes de l'ISSB par certaines juridictions, sans la détailler.
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences », « déclaration relative à la durabilité »).

**Erreurs fréquentes**
- Présenter l'EFRAG comme l'auteur juridique des ESRS : c'est la Commission qui les adopte.
- Discuter l'obligation de publier ou son calendrier, alors que l'énoncé l'écarte par hypothèse (`JUR-F07`).
- Affirmer que les ESRS et les normes de l'ISSB sont identiques, ou au contraire incompatibles (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règl. délégué 2026/1563, consid. 2-3 ; ESRS 1 (2026) § 2-4, 8-10, 23-24, 35, 47-50, 60-65 | EFRAG, architecture, double matérialité, étendue et limites | [V] | F12 § 1, 3, 6, 7 |
| Pages ISSB et GRI ; guide IFRS-EFRAG (mai 2024) | Normalisateurs ; interopérabilité ISSB | [S] | F12 § 1 |
| Déclaration EFRAG-GRI (2023) | Interopérabilité GRI | [V] | F12 § 1 |

### 3.7 Exigences générales, principes des informations à publier ; impact, risque et opportunité (3 pts)

**Exigences générales (1 pt)**
- **Objectif** : l'état de durabilité, pris comme un tout, donne une **image fidèle** des impacts, risques et opportunités matériels et de la manière dont l'entreprise les gère [V ESRS 1 (2026) § 3].
- **Caractéristiques qualitatives** : pertinence, représentation fidèle, comparabilité, vérifiabilité, compréhensibilité [V LD 2026 § 2 ; dir. 2013/34 art. 29 ter § 2 ; ESRS 1 (2026), chap. 2].
- **Architecture** : l'ESRS 1 fixe les exigences générales ; l'ESRS 2 s'applique **toujours**, quel que soit le résultat de l'analyse de matérialité ; les normes thématiques s'appliquent pour les thèmes matériels ; des **informations spécifiques** complètent les normes si un enjeu matériel n'est pas couvert [V ESRS 1 (2026) § 8-11, 29].
- **Analyse de matérialité** : double matérialité, dont le point de départ est en général l'analyse des impacts [V ESRS 1 (2026) § 35-36] ; **horizons** de court, moyen et long terme [V ESRS 1 (2026), chap. 6 ; § 39, 47] ; **chaîne de valeur** amont et aval, avec recours possible à des estimations [V § 62-65].

**Principes généraux sur les informations à publier (0,5 pt)**
- Deux étapes : identifier les thèmes liés à des impacts, risques ou opportunités matériels, puis déterminer les informations à publier sur chacun [V ESRS 1 (2026) § 25] ; pour chaque thème matériel : politiques, actions, indicateurs et cibles, et exigences thématiques pertinentes [V § 29-30].
- Pas d'information non matérielle tirée d'une exigence des ESRS ; les informations issues d'autres référentiels sont signalées comme telles [V § 24, 107-109].
- Section **clairement distinguée** du rapport de gestion ; quatre parties dans l'ordre : informations générales, environnementales, sociales, de gouvernance [V § 104-105].
- **Connectivité** avec les états financiers : renvoi aux montants communs, explication des liens indirects, cohérence des hypothèses [V § 112-116].

**Impact, risque et opportunité de CHAMPLOVERRE (1,5 pt : 0,5 pt par élément justifié)**

| Élément | Nature et localisation | Dimension de la matérialité |
|---|---|---|
| Émissions de gaz à effet de serre des fours (combustion du gaz, décomposition du carbonate de soude et du calcaire ; 396 000 MWh de gaz en 2026) | **Impact négatif réel** sur l'environnement, issu des **activités propres** de l'usine | **Matérialité d'impact** : gravité élevée par l'ampleur et le caractère continu des émissions [V ESRS 1 (2026) § 39-40] |
| Hausse du prix du gaz (+ 35 % depuis 2021), concurrence pour le calcin (+ 30 % en deux ans), sélection des fournisseurs selon leurs émissions à partir de 2028 | **Risques** de transition : ils naissent d'une **dépendance** à des ressources (gaz, calcin) dans la **chaîne de valeur amont** et des attentes des clients dans la **chaîne de valeur aval** | **Matérialité financière** : effets probables sur les coûts, la marge et le chiffre d'affaires, à court et moyen terme [V ESRS 1 (2026) § 47-48, 50] |
| Hausse du taux de calcin, bouteilles allégées, four hybride en 2029 | **Opportunités** : baisse de la consommation de gaz et de matières premières, conquête de clients exigeants ; elles concernent les **activités propres** et les **clients** | **Matérialité financière**, avec des effets positifs sur l'impact (moins d'émissions) |

Autres réponses acceptées : l'exposition des salariés à la chaleur et aux brûlures, impact négatif réel sur le **personnel de l'entreprise** (neuf accidents avec arrêt) ; les émissions des transporteurs, impact de la **chaîne de valeur** ; la collecte du verre ménager, impact positif dans la chaîne de valeur amont.

**Réponses tolérées**
- Les émissions des fours présentées comme un enjeu doublement matériel (impact et risque de transition), si les deux dimensions sont justifiées.
- Le vocabulaire des ESRS de 2023 (« incidences »).

**Erreurs fréquentes**
- Confondre impact (effet de l'entreprise sur son environnement) et risque (effet de l'environnement sur l'entreprise) (`JUR-A01`).
- Détailler les exigences d'une norme thématique ou des points de données, qui ne sont pas attendus.
- Citer des enjeux génériques sans exploiter les chiffres de l'annexe 3.6 (`JUR-F07`, `JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 3, 8-11, 24-25, 29-30, 35-36, 39-40, 47-50, 62-65, 104-109, 112-116 | Exigences générales ; principes des informations ; IRO | [V] | F12 § 2, 3, 5, 6, 7, 8, 9 |
| LD 2026 § 2 ; dir. 2013/34 art. 29 ter § 2 | Caractéristiques qualitatives | [V] | F12 § 5 |

### 3.8 Objectifs, assurance limitée, axes et étapes de la mission (3 pts)

**Objectifs et nature de l'assurance (1 pt)**
- **Objectifs (0,5 pt)** : ARNÉVAL émet un **avis** sur la conformité aux ESRS du **processus** mis en œuvre par CHAMPLOVERRE pour déterminer les informations publiées et sur la conformité des **informations** publiées. Son rapport de certification est destiné aux associés, organe appelé à statuer sur les comptes [V L. 821-54 II ; LD 2026 § 2 ; S, application par hypothèse : mission volontaire conduite dans les conditions de la certification légale].
- **Assurance limitée (0,5 pt)** : les vérifications sont moindres en **nature**, en **étendue** et en **durée** que pour une assurance raisonnable ; la conclusion est exprimée sous une **forme négative** : ARNÉVAL n'a pas relevé d'erreurs, omissions ou incohérences importantes. La certification des comptes repose, elle, sur une **assurance raisonnable**, exprimée sous une forme positive [V LD 2026, niveau d'assurance ; dir. 2013/34 art. 34 ; NEP principes § 08].

**Axes en l'espèce (0,5 pt)**
1. **Processus** de détermination des informations (double matérialité) : vérifié ; la consultation du comité social et économique n'est pas en cause, la société publiant volontairement (hypothèse) [V LD 2026 § 2, 7 ; F12 § 11.3 (b)].
2. **Informations** publiées : vérifiées.
3. Informations relatives à la **taxonomie** : non examinées (hypothèse ; CHAMPLOVERRE n'y est pas soumise).
4. **Balisage** : non exigible tant que ses règles ne sont pas adoptées ; écarté par hypothèse [V LD 2026 § 2, 10].

**Étapes de la démarche (1 pt)** [V LD 2026, § 4 à 17 ; guide p. 186-187]
- **Lettre de mission** : objectif, étendue (deux axes), calendrier, accès aux personnes et documents, lettre d'affirmation, honoraires.
- **Prise de connaissance** de l'entité et de son environnement : modèle d'affaires (fusion du verre, calcin, gaz), chaîne de valeur (centres de traitement, transporteurs, maisons de vin), gouvernance et processus de collecte des données.
- **Planification** : identification des informations qui présentent un **risque important de non-conformité** ou de fortes attentes des utilisateurs, ici le taux de calcin, lié à un objectif public et attendu par les clients, et les émissions estimées des transporteurs.
- **Vérification du processus** (axe 1) : identification et évaluation des impacts, risques et opportunités, couverture de la chaîne de valeur, association des parties prenantes, justification des seuils.
- **Vérification des informations** (axe 2) : rapprochements, recalculs, examen des méthodes et des estimations (voir 3.9).
- **Lecture finale** de l'état de durabilité et des comptes annuels, **appréciation** des éléments collectés, **événements postérieurs**, communication avec la présidente, **documentation**, puis **rapport** organisé par axe.

**Prise en compte de l'incident du four n° 2 (0,5 pt)**
- L'incident est un **événement postérieur** au sens de la mission : ARNÉVAL vérifie que l'état de durabilité en tient compte dans la mesure où il modifie l'information, ici les effets attendus sur la consommation de gaz et les émissions de 2027, mention ajoutée à sa demande [V LD 2026 § 13 ; annexe 3.7].
- C'est aussi un point de **connectivité** : la description de l'incident dans l'état de durabilité doit être cohérente avec la note de l'annexe des comptes (durée de l'arrêt, coût de reconstruction) ; les équipes d'ARNÉVAL chargées des deux missions échangent sur ce point [V ESRS 1 (2026) § 116 ; LD 2026 § 3.2, 11].

**Réponses tolérées**
- Le vocabulaire « auditeur de durabilité » ou « vérificateur ».
- Une présentation des étapes regroupée en trois temps (prise de connaissance et planification, vérifications par axe, conclusion et rapport), si le contenu essentiel figure.

**Erreurs fréquentes**
- Présenter l'assurance limitée comme une assurance raisonnable « allégée » exprimée sous une forme positive (`JUR-A01`).
- Faire porter l'avis sur la taxonomie, la consultation du comité social et économique ou le balisage, que l'énoncé écarte (`JUR-F07`).
- Réciter les étapes sans les illustrer par le cas (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II ; dir. 2013/34 art. 34 ; LD 2026, niveau d'assurance, § 2, 7, 10 | Objet de l'avis ; assurance limitée ; axes | [V] ; application : [S] | F13 § 2 |
| LD 2026 § 3.2, 4 à 17 | Étapes ; échanges entre équipes ; événements postérieurs | [V] | F13 § 3 |
| ESRS 1 (2026) § 116 ; NEP principes § 08 | Cohérence des hypothèses ; assurance raisonnable des comptes | [V] | F12 § 9 ; F11 § 1.1 |

### 3.9 Taux de calcin : procédures et recalcul ; avis par axe (3 pts)

**Procédures de vérification (1 pt : 0,25 pt par procédure justifiée, dans la limite de quatre)**
- **Rapprochement** du calcin acheté (126 000 t) avec les **bons de pesée** et les **factures** des centres de traitement, et avec les achats comptabilisés : éléments externes et connectés aux comptes.
- **Stocks** : rapprochement des stocks d'ouverture et de clôture avec les **inventaires physiques**, dont celui du 31/12/2026 auquel ARNÉVAL a assisté pour l'audit des comptes (connectivité).
- **Calcin interne et matières vierges** : rapprochement avec les rapports de production et les relevés de consommation des fours.
- **Recalcul** du taux selon la méthode publiée par la société, et vérification que le tableau de calcul applique bien cette méthode.
- **Procédure analytique** : cohérence de l'évolution du taux (de 52,0 % à 60,0 %) avec celle de la consommation de gaz par tonne enfournée (396 000 / 240 000 = 1,65 MWh par tonne) et des achats de calcin ; entretien avec les responsables de production.

**Recalcul et conclusion (1 pt)**

| Élément | Tonnes |
|---|---:|
| Stock de calcin au 01/01/2026 | 10 000 |
| + Calcin acheté et réceptionné | 126 000 |
| + Calcin issu des rebuts | 18 000 |
| − Stock de calcin au 31/12/2026 | 22 000 |
| **= Calcin enfourné** | **132 000** |
| Matières premières vierges enfournées | 108 000 |
| **Total des matières enfournées** | **240 000** |

- **Taux de calcin selon la méthode publiée** : 132 000 / 240 000 = **55,0 %** (0,5 pt).
- Le tableau de la société retient au numérateur le calcin **réceptionné** (126 000 + 18 000 = 144 000 t), soit 144 000 / 240 000 = 60,0 %. Il compte ainsi l'**augmentation du stock** (22 000 − 10 000 = 12 000 t), qui n'a pas été enfournée en 2026 : le numérateur est surévalué de 9,1 %. Le calcul est **incohérent avec la méthode publiée** (0,25 pt).
- **Conclusion** : le taux publié est surévalué de **5,0 points** ; la progression réelle est de 3,0 points (de 52,0 % à 55,0 %) et non de 8,0 points ; l'objectif de 60 % **n'est pas atteint**. L'argument de la présidente est inopérant : le calcin en stock sera enfourné en 2027 et comptera dans le taux de 2027 (0,25 pt).

**Avis par axe et traitement du transport (1 pt)**
- **Axe 1 – processus (0,25 pt)** : processus documenté, chaîne de valeur couverte, parties prenantes associées, seuils justifiés, événement postérieur pris en compte ; aucune erreur, omission ou incohérence : **avis de conformité**.
- **Axe 2 – informations (0,5 pt)** : l'erreur sur le taux de calcin n'est pas corrigée. Elle est importante : elle porte sur un indicateur lié à un **objectif public**, la société affirme à tort l'avoir atteint, et les clients choisiront leurs fournisseurs selon leurs émissions. Ses incidences sont **clairement circonscrites** (un indicateur, dont l'écart est chiffré) et toutes les autres informations vérifiées sont conformes. ARNÉVAL émet un **avis de conformité assorti d'une réserve motivée**, qui décrit l'erreur et indique le taux recalculé [V LD 2026 § 17 ; F13 § 4.2-4.3 ; S, appréciation de l'importance].
- **Transport des bouteilles (0,25 pt)** : la méthode d'estimation est décrite par la société, appliquée sans erreur et acceptable au regard des ESRS, qui admettent des estimations pour la chaîne de valeur [V ESRS 1 (2026) § 62-65]. ARNÉVAL peut formuler une **observation** dans la partie relative à l'axe 2, pour attirer l'attention sur cette méthode et sur ses limites de mesure. Une observation est possible avec un avis de conformité, avec ou sans réserve ; ce n'est **pas une réserve** [V LD 2026 § 17 ; F13 § 4.4].

**Réponses tolérées**
- Un avis de **non-conformité** sur l'axe 2, si le candidat soutient que l'affirmation d'un objectif atteint, au cœur de la communication de la société, empêche de circonscrire les incidences : 0,25 pt sur 0,5. La réserve motivée est la réponse attendue [S, F13 § 4.3].
- Le calcul 144 000 / (144 000 + 108 000) = 57,1 %, présenté comme la variante de la société, si le taux de 55,0 % selon la méthode publiée est trouvé.
- Le traitement du transport comme un **élément ayant fait l'objet d'une attention particulière**, si le candidat montre qu'il ne modifie pas l'avis [V LD 2026 § 17].

**Erreurs fréquentes**
- Reprendre sans le vérifier le taux du tableau de la société, ou oublier la variation de stock (`JUR-F02`, `JUR-F07`).
- Transformer l'observation sur le transport en réserve, ou accepter le taux au motif que le calcin en stock sera enfourné en 2027.
- Émettre un avis global au lieu d'un avis par axe.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 8, 12, 17 | Vérification des informations ; appréciation ; avis et observations par axe | [V] | F13 § 3, 4.2-4.4 |
| Table de décision des avis ; appréciation de l'importance | Application | [S, jugement professionnel] | F13 § 4.3 |
| ESRS 1 (2026) § 62-65 | Estimations pour la chaîne de valeur | [V] | F12 § 7 |
| Données de l'annexe 3.7 | Stocks, achats, rebuts, matières vierges | données de l'énoncé | — |
