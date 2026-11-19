# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 15

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 17/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.8 | `exercices/ex40_consolidation_ifrs_acquisition_avantageuse_retraites_subvention` |
| 2 – Opérations de restructuration | 25 | 2.1  à 2.5 | `exercices/ex41_apport_partiel_controle_commun_reconstitution` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.11 | `exercices/ex42_audit_tresorerie_fraude_gie_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 a Référentiel IFRS, comptes individuels en PCG, retraitements | `2.1.b` Contexte réglementaire et légal de la consolidation | 2 |
| 1.1 b Cadre conceptuel et profit sur acquisition | `2.1.a` Cadre conceptuel de l'IASB ; `2.2.g` Goodwill (badwill) | 2 |
| 1.1 c Cadre conceptuel et option d'IAS 20 | `2.1.a` Cadre conceptuel de l'IASB ; `2.2.d` Subventions en IFRS | 1 |
| 1.2 a Tableau du périmètre et rupture de chaîne | `2.1.c` Périmètre de consolidation | 1,5 |
| 1.2 b Ce que montre la mise en équivalence | `2.1.d` Méthodes et information financière | 1 |
| 1.3 a Engagements de retraite : PCG et IAS 19 | `2.2.c` Homogénéisation, thèmes communs | 1,5 |
| 1.3 b Intérêt net, écart actuariel, tableau d'incidence | `2.2.c` Homogénéisation, thèmes communs | 3 |
| 1.3 c Écritures des engagements de retraite | `2.2.c` Homogénéisation, thèmes communs | 2,5 |
| 1.4 a Subvention : reprises, ligne d'impression, incidence | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 2 |
| 1.4 b Subvention : impôt différé | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 1,5 |
| 1.4 c Subvention : écritures et partage | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 2 |
| 1.5 a Comptes réciproques et lot en transit | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.5 b Marge interne descendante | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.5 c Écritures de la marge interne | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.5 d Dividendes internes | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.6 a Frais d'acquisition des titres TRÉVANCE | `2.2.g` Goodwill ; `2.2.c` Frais d'acquisition | 1,5 |
| 1.6 b Actif net identifiable avant et après réexamen | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.6 c Profit sur acquisition, PNC, comparaison ANC | `2.2.g` Écarts d'évaluation et goodwill (badwill) | 2,5 |
| 1.6 d Écritures des écarts d'évaluation | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.7 a Partage de la CARTONNERIE DU BESSIN et de TRÉVANCE | `2.2.h` Partage des capitaux propres | 1,5 |
| 1.7 b Mise en équivalence de la MINOTERIE et de FARINES ET MIX | `2.2.h` Partage des capitaux propres (MEE) | 1 |
| 1.7 c Écritures d'élimination, de partage et de mise en équivalence | `2.2.h` ; `2.2.g` | 2 |
| 1.8 a Phases du processus et lignes du tableau de variation | `2.2.a` Processus d'élaboration d'une consolidation | 2,5 |
| 1.8 b Résultat net consolidé et tableau de variation des capitaux propres | `2.3.a` Documents de synthèse ; `2.2.a` | 2,5 |
| 1.8 c État du résultat net et des autres éléments du résultat global | `2.3.a` Documents de synthèse consolidés | 2,5 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = participations ne donnant pas le contrôle (PNC) ; `CAP_ELIM` = capital de la filiale éliminé ; `EA` = goodwill ; `PROFIT_ACQ` = profit sur acquisition à des conditions avantageuses, comptabilisé en résultat à la date d'acquisition ; `TME` = participation mise en équivalence ; `QP_MEE` = quote-part du résultat net des entités mises en équivalence ; `AERG` = autres éléments du résultat global ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat de l'écriture de bilan. Un suffixe désigne la société concernée (`RST.TREVANCE`, `261.CROQUENVILLE` : titres détenus par CROQUENVILLE ; `CARTONNERIE` : CARTONNERIE DU BESSIN).

---

### 1.1 Référentiel et cadre conceptuel (5 pts)

#### a. Référentiel IFRS et comptes individuels en PCG (2 pts)

**Obligation de consolider (0,25 pt).** CROQUENVILLE, société commerciale, contrôle de manière exclusive la CARTONNERIE DU BESSIN et TRÉVANCE (majorité des droits de vote, nomination du président) : elle doit établir et publier des comptes consolidés [V C. com. L. 233-16 ; F03 § 1.1].

**Référentiel (0,5 pt).** Les IFRS adoptées par l'Union européenne sont obligatoires pour les comptes consolidés des sociétés dont les titres sont admis aux négociations sur un marché réglementé d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Les actions de CROQUENVILLE sont admises sur Euronext Paris, marché réglementé : le groupe n'a pas le choix du règlement ANC n° 2020-01, ouvert aux seules sociétés dont les titres ne sont pas admis sur un tel marché.

**Comptes individuels (0,25 pt).** Le règlement européen ne vise que les comptes consolidés [V art. 4] : les comptes annuels de chaque société française, cotée ou non, restent établis selon le plan comptable général, qui sert aussi de base à leur résultat imposable [S].

**Conséquence pour la consolidation (1 pt).** Les comptes consolidés doivent être établis selon des méthodes comptables uniformes [V IFRS 10 § 19 ; F04 § 1]. Chaque filiale remonte ses comptes individuels, établis selon le PCG, puis ceux-ci sont **retraités** pour être mis en conformité avec les IFRS et le manuel du groupe, avant toute élimination et tout partage (0,5 pt). Le dossier en donne trois exemples, où le PCG permet ou impose ce que les IFRS interdisent : indemnités de départ à la retraite non provisionnées (option du PCG ; provision imposée par IAS 19) ; subvention inscrite en capitaux propres (impossible selon IAS 20) ; frais d'acquisition incorporés au coût des titres (en charges selon IFRS 3) ; s'y ajoute, à l'acquisition de TRÉVANCE, l'évaluation de ses actifs et passifs à la juste valeur (0,5 pt). Chaque retraitement crée un écart entre la valeur consolidée et la base fiscale, qui suit les comptes individuels : il donne lieu à un **impôt différé**.

#### b. Réponse au membre du conseil de surveillance (2 pts)

**Objectif de l'information financière (0,5 pt).** L'information financière à usage général doit être utile aux investisseurs, prêteurs et autres créanciers, actuels et potentiels, pour leurs décisions de fournir des ressources à l'entité [S cadre conceptuel de 2018 ; F03 § 7.2]. Le 01/01/2026, CROQUENVILLE a obtenu, pour 6 300 000 €, 90 % d'un actif net identifiable évalué à 8 000 000 €, soit 7 200 000 € : l'enrichissement de 900 000 € est acquis à cette date, par l'échange lui-même ; les actionnaires d'une société cotée doivent le voir dans la performance de l'exercice où il se produit.

**Représentation fidèle et neutralité (0,5 pt).** Une information fidèle est complète, neutre et exempte d'erreurs ; la neutralité exclut tout parti pris dans le choix ou la présentation de l'information [S cadre de 2018 ; F03 § 12]. Étaler le profit « au fur et à mesure des bénéfices de TRÉVANCE » lisserait les résultats futurs avec un gain de 2026 ; le laisser au passif ferait apparaître une dette qui n'en est pas une, aucune obligation de payer ne résultant de l'acquisition [V définition du passif, IAS 37 § 10 ; F03 § 8]. Les deux solutions seraient biaisées. La norme applicable tranche d'ailleurs la question : le profit est comptabilisé **en résultat à la date d'acquisition** et attribué à l'acquéreur [V IFRS 3 § 34 ; F05 § 11] ; lorsqu'une IFRS s'applique spécifiquement, c'est elle qui détermine la méthode [V IAS 8 § 7 ; F03 § 12].

**Place de la prudence (0,5 pt).** La prudence est l'exercice de la précaution dans les jugements portés en situation d'incertitude ; elle soutient la neutralité, mais ne permet ni de sous-évaluer des actifs ou des produits, ni de surévaluer des passifs ou des charges [S cadre de 2018 ; F03 § 12 ; même idée dans IAS 37 § 43, V]. Ne pas constater un profit acquis reviendrait à sous-évaluer les capitaux propres et le résultat. La précaution s'exerce **avant** la comptabilisation : la norme impose de réexaminer l'identification et l'évaluation de tous les actifs et passifs [V IFRS 3 § 36 ; F05 § 11]. C'est ce qui a été fait : le réexamen a ramené le bâtiment de 2 400 000 € à 2 000 000 € et le profit de 1 170 000 € à 900 000 € (question 1.6).

**Application aux circonstances (0,5 pt).** Le profit ne révèle pas une erreur d'évaluation : il s'explique par une **vente forcée**, le vendeur s'étant engagé à quitter la France avant le 31/12/2025 et n'ayant reçu qu'une offre [V IFRS 3 § 35 ; F05 § 11]. Les notes indiqueront son montant, le poste du compte de résultat où il figure et les raisons qui y ont conduit [V IFRS 3 B64 n) ; F05 § 11] : c'est par l'information, et non par le report du gain, que le lecteur est éclairé.

#### c. Option d'IAS 20 et cohérence des méthodes (1 pt)

**Pourquoi pas les capitaux propres (0,25 pt).** Une subvention n'est pas un apport des actionnaires : elle est comptabilisée en résultat sur les périodes où sont constatées les charges qu'elle compense, et jamais directement en capitaux propres [V IAS 20 § 12, 15 a) ; F03 § 8]. Pour un actif, la norme laisse deux présentations acceptables : produits différés ou déduction de la valeur de l'actif [V IAS 20 § 24, 25 ; F04 R10, § 12].

**Comparabilité et cohérence (0,5 pt).** Le manuel retient la déduction pour tout le groupe : les méthodes doivent être uniformes entre les sociétés consolidées [V IFRS 10 § 19] et appliquées avec cohérence à des transactions similaires [V IAS 8 § 13 ; F03 § 12]. Laisser chaque filiale choisir rendrait les capitaux propres, les immobilisations et la dotation aux amortissements consolidés hétérogènes et incomparables ; la comparabilité, à laquelle concourt la cohérence, fait partie des qualités de l'information utile [S cadre de 2018 ; F03 § 7.2]. La CARTONNERIE garde sa présentation dans ses comptes individuels ; c'est en consolidation qu'elle est retraitée.

**Permanence (0,25 pt).** Le groupe conserve la présentation et le classement d'une période à l'autre [V IAS 1 § 45] et ne change de méthode que si une norme l'impose ou si l'information devient fiable et plus pertinente [V IAS 8 § 14 ; F03 § 12] : un choix variable d'un exercice à l'autre empêcherait la comparaison dans le temps.

**Réponses tolérées (1.1)**
- En a, référence au « règlement IAS » sans numéro ; conséquence formulée comme la nécessité d'une « liasse de consolidation » ou d'un « manuel de procédures » appliqué par chaque filiale, si les retraitements sont cités.
- En b, réponse fondée sur la définition d'un passif (aucune obligation, donc pas de produit différé) ou sur les caractéristiques qualitatives sans le mot « neutralité », si la conclusion (profit en résultat de 2026, après réexamen) est justifiée.
- En c, argument de la « permanence des méthodes » seul, s'il est relié à la comparaison d'un exercice à l'autre (0,25 pt perdu sans la comparabilité entre sociétés).

**Erreurs fréquentes (1.1)**
- IFRS présentées comme une option pour une société cotée ; IFRS présentées comme obligatoires dans les comptes individuels ; IFRS 18 appliquée à 2026.
- Prudence invoquée pour approuver l'étalement du profit (confusion avec l'ancienne notion de prudence des règles nationales) ; profit « reporté au passif comme un écart d'acquisition négatif » (traitement de l'ANC hors conditions avantageuses).
- Réexamen ignoré : profit comptabilisé sur la première évaluation (1 170 000 €).

**Références normatives (1.1)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 233-16 ; règlement (CE) n° 1606/2002, art. 4 | Obligation de consolider ; IFRS obligatoires (marché réglementé) | [V] | F03 § 1.1, § 1.2 |
| IFRS 10 § 19 | Méthodes comptables uniformes | [V] | F04 § 1 |
| Cadre conceptuel de 2018 | Objectif, représentation fidèle, neutralité, prudence, comparabilité | [S] | F03 § 7.2, § 12 |
| IAS 8 § 7, 10, 13, 14 ; IAS 1 § 45 ; IAS 37 § 10, 43 | Hiérarchie des sources ; neutralité et prudence ; cohérence ; permanence ; passif | [V] | F03 § 8, § 12 |
| IFRS 3 § 34, 35, 36, B64 n) | Profit en résultat, vente forcée, réexamen, information | [V] | F05 § 11 |
| IAS 20 § 12, 15, 24, 25 | Subvention en résultat, jamais en capitaux propres ; deux présentations | [V] | F03 § 8 ; F04 R10, § 12 |

---

### 1.2 Périmètre et méthodes (2,5 pts)

#### a. Tableau du périmètre (1,5 pt)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe |
|---|---:|---|---|---:|
| CARTONNERIE DU BESSIN | 75 % | Contrôle exclusif | Intégration globale | 75 % |
| TRÉVANCE | 90 % | Contrôle exclusif | Intégration globale | 90 % |
| MINOTERIE DE SOULEUVRE | 30 % | Influence notable | Mise en équivalence | 30 % |
| FARINES ET MIX DU BOCAGE | 25 % | Influence notable | Mise en équivalence | 25 % |

(1 pt, 0,25 pt par ligne.) Pour la CARTONNERIE et TRÉVANCE, la majorité des droits de vote et la nomination du président donnent le pouvoir [V IFRS 10 § 7 ; F03 § 2] ; pour la MINOTERIE, 30 % des droits de vote et deux sièges sur sept font présumer l'influence notable [V IAS 28 § 5, 6 ; F03 § 2].

**FARINES ET MIX DU BOCAGE (0,5 pt).**
- **Contrôle : 25 %.** On n'additionne aux droits de CROQUENVILLE que ceux des entités qu'elle contrôle ; les 20 % de la MINOTERIE, simple entreprise associée, ne comptent pas [V ANC art. 211-6 ; en IFRS, IAS 28 § 5 ne retient que les droits détenus directement ou par le biais de filiales ; F03 § 2, § 4.1]. La coopérative, majoritaire et maîtresse du comité de direction, contrôle la société ; CROQUENVILLE, avec 25 % et deux sièges, exerce une influence notable [V IAS 28 § 5, 6] : mise en équivalence [V IAS 28 § 16].
- **Intérêt : 25 % en IFRS.** La part du groupe dans une entreprise associée est l'agrégation des participations détenues par la société mère et ses filiales ; les participations détenues par d'autres entreprises associées ne sont pas prises en compte [V IAS 28 § 27 ; F03 § 4.2]. La MINOTERIE n'étant pas une filiale, la chaîne qui passe par elle est « rompue ». Le raisonnement suivi en règlement ANC n° 2020-01, qui additionne toutes les chaînes, donnerait **25 % + 30 % × 20 % = 31 %** [S corrigé du sujet zéro ; F03 § 4.1, § 4.2].
- La participation de la MINOTERIE dans FARINES ET MIX ne disparaît pas pour autant. IAS 28 retiendrait normalement, pour la mise en équivalence de la MINOTERIE, ses chiffres y compris sa quote-part dans FARINES ET MIX [V IAS 28 § 27, troisième phrase ; F03 § 12]. L'hypothèse de l'annexe 1.7 retient ses comptes individuels, où cette participation figure au coût : elle n'atteint alors le groupe que par les dividendes que la MINOTERIE en recevrait [application, S ; F03 § 12].

#### b. Ce que montre la mise en équivalence (1 pt)

**Ce qu'elle montre (0,5 pt).** Une seule ligne à l'actif, la participation mise en équivalence (4 380 000 € au 31/12/2026, question 1.7), et une ligne du compte de résultat, la quote-part du résultat net (480 000 €) [V IAS 1 § 54 e), 82 c) ; F14 § 2.2, § 2.3] : le résultat consolidé et les capitaux propres part du groupe intègrent la part du groupe dans les résultats et l'actif net de la MINOTERIE.

**Ce qu'elle ne montre pas (0,5 pt).** Le chiffre d'affaires de la MINOTERIE (46 000 000 €, dont 30 % représenteraient 13 800 000 €) n'entre pas dans les 356 M€ du chiffre d'affaires consolidé ; ses dettes financières (11 500 000 €, dont 30 % représenteraient 3 450 000 €) n'apparaissent pas au passif consolidé. Les marges et l'endettement du groupe sont donc lus sans cette activité, alors que la MINOTERIE est son principal fournisseur. Seules les notes donnent, pour une entreprise associée significative, des informations financières résumées [V IFRS 12 § 21 ; F03 § 12]. (La méthode est la même en règlement ANC pour une entreprise sous influence notable [V art. 221-1 ; F03 § 3].)

**Réponses tolérées (1.2)** : % des minoritaires de la MINOTERIE et de FARINES ET MIX indiqué « sans objet » ou 0 % ; intérêt dans FARINES ET MIX présenté comme « 25 % direct ; 6 % indirect non retenu en IFRS ».

**Erreurs fréquentes (1.2)** : contrôle de FARINES ET MIX fixé à 45 % (25 % + 20 %) et intégration globale ; intérêt de 31 % retenu en IFRS (`JUR-F07` : annexe non exploitée) ; FARINES ET MIX mise en équivalence deux fois, directement et à travers la MINOTERIE ; mise en équivalence présentée comme « une intégration à 30 % du chiffre d'affaires ».

**Références normatives (1.2)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 7 ; IAS 28 § 5, 6, 16 | Contrôle ; influence notable ; mise en équivalence | [V] | F03 § 2, § 3 |
| ANC 2020-01 art. 211-6, 221-1 | Pourcentage de contrôle ; méthode en ANC | [V] | F03 § 3, § 4.1 |
| IAS 28 § 27 | Rupture de chaîne ; chiffres de l'entreprise associée, y compris sa quote-part dans ses propres entreprises associées | [V] | F03 § 4.2, § 12 |
| Hypothèse de l'annexe 1.7 (participation au coût chez la MINOTERIE) | Seuls les dividendes atteignent le groupe | [S] | F03 § 12 |
| Somme des chaînes en ANC (25 % + 30 % × 20 %) | Pourcentage d'intérêt selon le corrigé du sujet zéro | [S] | F03 § 4.1 |
| IAS 1 § 54 e), 82 c) ; IFRS 12 § 21 | Lignes de la mise en équivalence ; informations sur les entreprises associées | [V] | F14 § 2.2, § 2.3 ; F03 § 12 |

---

### 1.3 Engagements de retraite de CROQUENVILLE (7 pts)

#### a. Comptes individuels et IAS 19 (1,5 pt)

**Comptes individuels (0,5 pt).** Le provisionnement des engagements de retraite est la méthode de référence du PCG, mais il reste une option [V PCG art. 324-1, 121-5 ; F04 R8] : CROQUENVILLE ne provisionne pas, mentionne l'engagement dans l'annexe et passe en charges (compte 6414) les indemnités versées.

**IAS 19 (0,75 pt).** Le régime est à prestations définies : l'obligation est évaluée selon la méthode des unités de crédit projetées et, en l'absence d'actif du régime, provisionnée pour sa valeur actuelle [V IAS 19 § 57 ; F04 R8]. Le coût des services rendus et l'intérêt net sont comptabilisés en résultat ; les réévaluations (écarts actuariels) en **autres éléments du résultat global**, sans reclassement ultérieur en résultat [V § 120, 122 ; F04 R8, § 7]. Les indemnités versées réduisent l'obligation [V § 141 ; F04 § 7] : la charge comptabilisée par CROQUENVILLE au compte 6414 est annulée.

**Impôt différé (0,25 pt).** Les indemnités ne sont déductibles qu'à leur versement : la provision a une base fiscale nulle ; différence temporelle déductible, **impôt différé actif** [V IAS 12 § 24 ; F04 R8 ; annexe 1.3], dont la part liée aux écarts actuariels suit les autres éléments du résultat global [V IAS 12 § 61A ; F04 R8].

#### b. Calculs et tableau d'incidence (3 pts)

**Intérêt net (0,5 pt)** : obligation d'ouverture × taux d'actualisation d'ouverture [V IAS 19 § 123, 123A], les flux étant réputés intervenir le 31/12/2026 : 3 600 000 × 3,5 % = **126 000 €**.

**Écart actuariel (0,75 pt)**

| Rapprochement de l'obligation | Montant |
|---|---:|
| Obligation au 01/01/2026 | 3 600 000 |
| + Coût des services rendus de 2026 | 252 000 |
| + Intérêt net | 126 000 |
| – Indemnités versées | – 180 000 |
| = Obligation attendue au 31/12/2026 | 3 798 000 |
| Obligation au 31/12/2026 (actuaire) | 3 900 000 |
| **Écart actuariel : perte** | **102 000** |

**Tableau d'incidence (1,75 pt)**

| | Ouverture 01/01/2026 (réserves) | Résultat de 2026 | Autres éléments du résultat global de 2026 | Clôture 31/12/2026 |
|---|---:|---:|---:|---:|
| Provision avant impôt | – 3 600 000 | – 198 000 | – 102 000 | – 3 900 000 |
| Impôt différé actif, 25 % | + 900 000 | + 49 500 | + 25 500 | + 975 000 |
| **Incidence nette sur les capitaux propres** | **– 2 700 000** | **– 148 500** | **– 76 500** | **– 2 925 000** |

(0,5 pt pour la colonne d'ouverture, 0,5 pt pour le résultat, 0,5 pt pour les autres éléments du résultat global, 0,25 pt pour la clôture.) Résultat avant impôt : 252 000 + 126 000 – 180 000 = **198 000 €** : le coût des services et l'intérêt net remplacent les indemnités déjà passées en charges. Contrôle : 3 600 000 + 198 000 + 102 000 = 3 900 000 €.

#### c. Écritures (2,5 pts)

**C1 (bilan, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RSV.CROQUENVILLE Réserves CROQUENVILLE (3 600 000 net d'impôt : × (1 – 25 %)) | 2 700 000 | |
| RST.CROQUENVILLE Résultat CROQUENVILLE (198 000 net d'impôt) | 148 500 | |
| AERG Autres éléments du résultat global – réévaluations du régime (102 000 net d'impôt) | 76 500 | |
| IDA Impôt différé actif (3 900 000 × 25 %) | 975 000 | |
| 1521 Provisions pour pensions et obligations similaires | | 3 900 000 |
| **Total** | **3 900 000** | **3 900 000** |
| | *Libellé : engagement de retraite provisionné selon IAS 19* | | |

**C1R (compte de résultat, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6815 Dotations aux provisions d'exploitation (coût des services rendus) | 252 000 | |
| 6865 Dotations aux provisions financières (intérêt net) | 126 000 | |
| 6414 Indemnités et avantages divers (indemnités imputées sur la provision) | | 180 000 |
| CH_ID Produit d'impôt différé (198 000 × 25 %) | | 49 500 |
| RES_CR Résultat | | 148 500 |
| **Total** | **378 000** | **378 000** |

L'écart actuariel et son impôt (102 000 € et 25 500 €) ne passent pas par le compte de résultat : ils figurent dans la section des autres éléments du résultat global (question 1.8 c).

**Réponses tolérées (1.3)**
- Indemnités versées présentées en reprise de provision (compte 7815) plutôt qu'en diminution du compte 6414 ; intérêt net présenté en charges de personnel, s'il est isolé.
- C1 scindée (ouverture, puis mouvements de 2026) ; impôt différé de l'écart actuariel porté directement en autres éléments du résultat global (AERG – 102 000 et IDA 25 500 sur deux lignes).
- Intérêt calculé en tenant compte des versements en cours d'année, si l'hypothèse est écrite : seul le point de l'intérêt est perdu, l'écart actuariel en découlant étant accepté (`JUR-F08`).

**Erreurs fréquentes (1.3)**
- Écart actuariel porté en résultat, ou laissé dans le résultat « par différence » (charge de 300 000 €) ; indemnités versées laissées en charges (double comptage : charge de 378 000 €).
- Engagement d'ouverture porté au résultat de 2026 (`JUR-G06`) ; impôt différé omis ou présenté en passif.

**Références normatives (1.3)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 121-5, 324-1 | Provision, méthode de référence optionnelle | [V] | F04 R8 |
| IAS 19 § 57, 120, 122, 123, 123A, 141 | Unités de crédit projetées ; composantes du coût ; OCI non recyclables ; intérêt net ; prestations payées | [V] | F04 R8, § 7 |
| IAS 12 § 24, 61A | Impôt différé actif ; impôt suivant les OCI | [V] | F04 R8 |

---

### 1.4 Subvention de la CARTONNERIE DU BESSIN (5,5 pts)

#### a. Reprises, ligne d'impression et incidence (2 pts)

**Reprises dans les comptes individuels (0,5 pt).** Subvention : 30 % × 2 400 000 = 720 000 €, reprise au rythme de l'amortissement.

| | 2025 (9 mois) | 2026 |
|---|---:|---:|
| Dotation aux amortissements : 2 400 000 / 10 × 9/12, puis / 10 | 180 000 | 240 000 |
| Quote-part de subvention (747) : 720 000 × dotation / 2 400 000 | **54 000** | **72 000** |

**Ligne d'impression au 31/12/2026 (1 pt)**

| | Comptes individuels | Comptes consolidés (subvention déduite) | Écart |
|---|---:|---:|---:|
| Valeur brute | 2 400 000 | 1 680 000 | – 720 000 |
| Amortissements cumulés | 420 000 | 294 000 | – 126 000 |
| **Valeur nette** | **1 980 000** | **1 386 000** | **– 594 000** |
| Subvention en capitaux propres (131 – 139) | 594 000 | — | – 594 000 |
| Dotation de 2026 / quote-part 747 | 240 000 / 72 000 | 168 000 / — | |

La subvention est déduite pour arriver à la valeur comptable de l'actif ; son effet en résultat passe par la réduction de la dotation aux amortissements [V IAS 20 § 24, 27 ; F04 R10, § 12]. Amortissement consolidé : 1 680 000 / 10 × 21/12 = 294 000 €.

**Incidence sur les réserves et le résultat (0,5 pt).** **Aucune** : en 2026, la charge nette est de 240 000 – 72 000 = 168 000 € dans les deux référentiels ; le cumul de 2025 est le même. Le retraitement est un reclassement : il retire des capitaux propres la subvention non encore reprise (594 000 €) et diminue d'autant la valeur nette de la ligne.

#### b. Impôt différé (1,5 pt)

- **Ligne d'impression (0,5 pt).** Sa base fiscale est sa valeur nette fiscale, calculée sur le coût total : 1 980 000 €, supérieure à sa valeur consolidée de 1 386 000 € ; isolée, cette différence de 594 000 € serait déductible [V IAS 12 § 5, 7 ; F04 § 12].
- **Subvention restant à imposer (0,5 pt).** Selon l'hypothèse de l'annexe 1.4, les 594 000 € non encore repris seront rapportés au résultat imposable au même rythme que l'amortissement : différence imposable d'égal montant, qui se résorbe sur les mêmes exercices, chez la même société.
- **Conclusion (0,5 pt).** Les deux effets s'annulent : le montant net que la CARTONNERIE déduira à l'avenir (1 980 000 – 594 000 = 1 386 000 €) égale la valeur consolidée de la ligne. **Aucun impôt différé** n'est à constater [application, S ; F04 § 12]. C'est la même conclusion qu'en présentation en produits différés, quand la subvention est imposée au rythme de sa reprise [F04 § 7] : le choix de présentation ne crée pas d'impôt. L'exception d'IAS 12 § 33, propre aux subventions non imposables, ne s'applique pas ici.

#### c. Écritures et partage (2 pts)

**C2 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 131 Subventions d'investissement octroyées | 720 000 | |
| 28154 Amortissements des matériels industriels (54 000 + 72 000) | 126 000 | |
| 139 Subventions d'investissement inscrites au compte de résultat | | 126 000 |
| 2154 Matériels industriels (subvention déduite) | | 720 000 |
| **Total** | **846 000** | **846 000** |
| | *Libellé : subvention présentée en déduction de la ligne d'impression (IAS 20)* | | |

**C2R (compte de résultat, 0,5 pt)** : débit 747 Quote-part des subventions d'investissement virée au résultat de l'exercice 72 000 ; crédit 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles 72 000. *Libellé : quote-part de 2026 portée en réduction de la dotation.*

**Partage (0,75 pt).** Les capitaux propres retraités de la CARTONNERIE sont ses capitaux propres individuels sans la subvention : 9 954 000 – 594 000 = **9 360 000 €** (dont résultat 1 360 000 €), partagés 75 % / 25 % : 7 020 000 € pour le groupe, 2 340 000 € pour les PNC (question 1.7). Sans le retraitement, la subvention aurait accru les capitaux propres part du groupe de 445 500 € (75 %) et les PNC de 148 500 € (25 %) ; en IFRS, ni le groupe ni les minoritaires n'en reçoivent de part, puisqu'elle n'est plus dans les capitaux propres. Le résultat partagé n'est pas modifié. Les PNC d'ouverture (2 200 000 € = 25 % × (3 000 000 + 4 600 000 + 1 200 000)) étaient déjà calculées hors subvention.

**Réponses tolérées (1.4)**
- En b, impôt différé actif et impôt différé passif de 148 500 € chacun présentés sans compensation, s'il est conclu à un effet nul sur les capitaux propres et le résultat.
- En c, C2 écrite en deux écritures (annulation des comptes 131 et 139 ; déduction du coût et des amortissements) ; C2R omise si le candidat indique que la dotation consolidée est de 168 000 € : 0,25 pt perdu.

**Erreurs fréquentes (1.4)**
- Subvention reclassée en produits différés (option non retenue par le manuel) ; subvention laissée en capitaux propres ; retraitement présenté comme modifiant le résultat (`JUR-G06`).
- Impôt différé actif ou passif de 148 500 € constaté seul, sans voir l'effet inverse ; calcul de la reprise de 2025 sur douze mois (72 000 €).

**Références normatives (1.4)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG, comptes 131, 139, 747 | Subvention en capitaux propres, quote-part virée au résultat | [V] | F04 R10 |
| IAS 20 § 24, 25, 27 | Déduction de la valeur de l'actif ; effet par la dotation | [V] | F04 R10, § 12 |
| IAS 12 § 5, 7, 33 | Base fiscale d'un actif ; subvention non imposable | [V] | F04 R10, § 7, § 12 |
| Conséquence pour la présentation en déduction | Aucun impôt différé net | [S] | F04 § 12 |

---

### 1.5 Opérations internes (5 pts)

#### a. Comptes réciproques (1 pt)

**Rapprochement (0,25 pt).** Créance de CROQUENVILLE : 540 000 € ; dette de TRÉVANCE : 420 000 € ; écart **120 000 €** : le lot de fourrages expédié et facturé le 31/12/2026 n'a été enregistré par TRÉVANCE qu'à sa réception, le 04/01/2027. Vendu départ usine, il appartient au groupe : le manuel l'inscrit dans les stocks de TRÉVANCE (annexe 1.2, point 4).

**C3 (bilan, 0,25 pt)** : débit 31 Matières premières et fournitures (lot en transit) 120 000 ; crédit 401 Fournisseurs 120 000. **C3R** : débit 601 Achats stockés – Matières premières et fournitures 120 000 ; crédit 6031 Variation des stocks de matières premières et fournitures 120 000 (sans effet sur le résultat). *Libellé : lot en transit inscrit chez TRÉVANCE.*

**C4 (bilan, 0,25 pt)** : débit 401 Fournisseurs 540 000 ; crédit 411 Clients 540 000. **C4R (compte de résultat, 0,25 pt)** : débit 701 Ventes de produits finis 2 400 000 ; crédit 601 Achats stockés 2 400 000 (2 280 000 enregistrés par TRÉVANCE + 120 000 du lot en transit). *Libellé : élimination des soldes réciproques et des ventes internes.* Ces éliminations sont sans incidence sur le résultat [V IFRS 10 B86 c) ; F04 R14].

#### b. Marge interne descendante (1,5 pt)

| Élément | Montant |
|---|---:|
| Stock compté chez TRÉVANCE | 360 000 |
| + Lot en transit (question a) | 120 000 |
| = Stock de produits achetés à CROQUENVILLE | 480 000 |
| **Marge interne : 25 % × 480 000** | **120 000** |
| Impôt différé actif, 25 % | 30 000 |
| **Élimination nette** | **90 000** |

(0,75 pt.) Les profits internes compris dans des actifs sont éliminés en totalité [V IFRS 10 B86 c) ; F04 R14]. Le stock est ramené au coût de revient du groupe (360 000 €), inférieur à sa base fiscale chez TRÉVANCE (480 000 €) : différence déductible, **impôt différé actif** [V IAS 12 § 24 ; F04 R14].

**Répartition (0,5 pt).** La marge a été réalisée par CROQUENVILLE, la vendeuse : l'élimination est imputée à son résultat [V principe ANC art. 251-2 ; F04 R14 ; annexe 1.2, point 4]. CROQUENVILLE étant la société mère, l'élimination porte **en totalité sur la part du groupe** ; les 10 % de minoritaires de TRÉVANCE n'en supportent rien, bien que le stock soit chez TRÉVANCE : le résultat de TRÉVANCE, qui a payé ses achats à leur prix, n'est pas modifié. Dans une vente « ascendante » de TRÉVANCE à CROQUENVILLE, 10 % de l'élimination auraient réduit les PNC.

**Stock au 01/01/2026 (0,25 pt).** Les 150 000 € de produits achetés en 2025 l'ont été quand TRÉVANCE n'appartenait pas au groupe : la marge de CROQUENVILLE a été réalisée avec un tiers et n'est pas interne. Ces stocks font partie de l'actif net acquis, pour leur juste valeur, égale à leur valeur comptable (annexe 1.6) : aucune élimination, ni en réserves ni en résultat.

#### c. Écritures de la marge (1,5 pt)

**C5 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.CROQUENVILLE Résultat CROQUENVILLE (120 000 net d'impôt) | 90 000 | |
| IDA Impôt différé actif (120 000 × 25 %) | 30 000 | |
| 31 Matières premières et fournitures (stocks de TRÉVANCE) | | 120 000 |
| **Total** | **120 000** | **120 000** |
| | *Libellé : élimination de la marge de CROQUENVILLE sur les stocks de TRÉVANCE* | | |

**C5R (compte de résultat, 0,75 pt)** : débit 6031 Variation des stocks de matières premières et fournitures 120 000 ; crédit CH_ID Produit d'impôt différé 30 000 ; crédit RES_CR Résultat 90 000.

#### d. Dividendes internes (1 pt)

**C6 (bilan, 0,25 pt)** : débit RST.CROQUENVILLE 720 000 ; crédit RSV.CROQUENVILLE 720 000. **C6R (0,25 pt)** : débit 7611 Revenus des titres de participation 720 000 ; crédit RES_CR 720 000. *Libellé : élimination des dividendes reçus de la CARTONNERIE DU BESSIN (600 000) et de la MINOTERIE (120 000).*

**Justification (0,5 pt).** Les dividendes reçus de sociétés consolidées sont des transferts internes de résultats déjà compris dans les réserves consolidées : les laisser en produits les compterait deux fois [V IFRS 10 B86 c) ; F04 R14]. Pour la CARTONNERIE, seuls les 200 000 € versés à la famille du fondateur sortent du groupe : ils réduisent les PNC (question 1.8). Pour la MINOTERIE, la distribution **réduit la valeur de la participation mise en équivalence** [V IAS 28 § 10 ; F05 § 4] : 30 % × 13 400 000 = 4 020 000 au 31/12/2025, + 480 000, – 120 000 = 4 380 000 €.

**Réponses tolérées (1.5)**
- C3 et C4 regroupées (débit 31 120 000 et 401 420 000 ; crédit 411 540 000) ; ventes internes éliminées pour 2 280 000 € seulement, si le lot en transit est enregistré directement en stock sans passer par les achats (C3R et C4R regroupées).
- Taux de 25 % appliqué au seul stock compté (marge de 90 000 €) : 0,25 pt perdu en b, les écritures cohérentes étant acceptées (`JUR-F08`).

**Erreurs fréquentes (1.5)**
- Écart de 120 000 € éliminé en annulant une partie de la vente de CROQUENVILLE ; lot en transit oublié dans la marge.
- Marge partagée 90 / 10 « parce que le stock est chez TRÉVANCE » ; marge calculée sur le coût (25 % × 480 000 / 1,25) ; impôt différé omis (`JUR-G06`).
- Marge éliminée sur le stock d'ouverture acheté en 2025 ; dividende de la MINOTERIE laissé en produits et ajouté à la valeur d'équivalence.

**Références normatives (1.5)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 B86 c) | Élimination complète des opérations intragroupe | [V] | F04 R14 |
| ANC 2020-01 art. 251-2 | Résultat interne imputé à la société qui l'a réalisé (principe identique) | [V] | F04 R14 |
| IAS 12 § 24 | Impôt différé actif | [V] | F04 § 1 |
| IAS 28 § 10 | Distributions d'une entreprise associée | [V] | F05 § 4 |

---

### 1.6 Acquisition de TRÉVANCE (8 pts)

#### a. Frais d'acquisition (1,5 pt)

**Traitement (0,5 pt).** En IFRS, les frais connexes à une acquisition (banque d'affaires, avocats, audit d'acquisition) sont des charges de la période où ils sont engagés ; ils ne font pas partie de la contrepartie transférée [V IFRS 3 § 53 ; F05 § 2 ; annexe 1.2, point 3]. Dus lors de la réalisation, le 01/01/2026, ce sont des charges de 2026.

**Incidence (0,5 pt).** Résultat consolidé de 2026 : **– 240 000 €**, sans impôt différé (hypothèse de l'annexe 1.6) ; titres ramenés à 6 300 000 €, montant retenu pour le calcul de la question c.

**C7 (bilan, 0,25 pt)** : débit RST.CROQUENVILLE 240 000 ; crédit 261.CROQUENVILLE Titres de participation TRÉVANCE 240 000. **C7R (0,25 pt)** : débit 6226 Honoraires 240 000 ; crédit RES_CR 240 000. *Libellé : frais d'acquisition des titres TRÉVANCE passés en charges.*

#### b. Actif net identifiable à la juste valeur (2 pts)

**Identification (0,5 pt).** Les actifs identifiables sont évalués à leur juste valeur à la date d'acquisition [V IFRS 3 § 18 ; F05 § 11], y compris la marque, que TRÉVANCE n'avait pas inscrite à son bilan : déposée, elle résulte d'un droit légal et est donc identifiable [V IAS 38 § 12 ; IFRS 3 B31 ; F03 § 11]. Les impôts différés des écarts sont constatés et affectent le profit [V IFRS 3 § 24 ; IAS 12 § 66 ; F05 § 2].

| Élément | Première évaluation | Après réexamen |
|---|---:|---:|
| Capitaux propres de TRÉVANCE au 01/01/2026 | 6 350 000 | 6 350 000 |
| Marque « Trévance » : 1 200 000 – 0 | + 1 200 000 | + 1 200 000 |
| Terrain : 500 000 – 300 000 | + 200 000 | + 200 000 |
| Bâtiment : 2 400 000 (puis 2 000 000) – 1 400 000 | + 1 000 000 | + 600 000 |
| Stocks de produits finis : 1 100 000 – 900 000 | + 200 000 | + 200 000 |
| Total des écarts d'évaluation | 2 600 000 | 2 200 000 |
| Impôt différé passif, 25 % | – 650 000 | – 550 000 |
| **Actif net identifiable à la juste valeur** | **8 300 000** | **8 000 000** |

(0,75 pt pour les écarts et l'impôt différé ; 0,75 pt pour les deux totaux.)

#### c. Profit sur acquisition et PNC (2,5 pts)

| Élément | Première évaluation | Après réexamen |
|---|---:|---:|
| Contrepartie transférée (22 500 × 280 €) | 6 300 000 | 6 300 000 |
| PNC : 10 % de l'actif net identifiable | 830 000 | 800 000 |
| Total (a) | 7 130 000 | 7 100 000 |
| Actif net identifiable (b) | 8 300 000 | 8 000 000 |
| **Excédent de (b) sur (a)** | **1 170 000** | **900 000** |

Formulation équivalente : 90 % × 8 000 000 = 7 200 000 €, supérieur de 900 000 € au prix payé (0,5 pt).

**Traitement (1 pt).** L'actif net excède le total de la contrepartie et des PNC : c'est une acquisition à des conditions avantageuses. Avant tout profit, le groupe doit réexaminer l'identification des actifs et des passifs et les procédures d'évaluation [V IFRS 3 § 36 ; F05 § 11] (0,25 pt) ; le réexamen, qui n'a trouvé aucun élément omis mais a corrigé le bâtiment, ramène l'excédent à 900 000 € (0,25 pt). L'excédent qui subsiste est un **profit comptabilisé en résultat à la date d'acquisition**, soit en 2026, et **attribué à l'acquéreur**, donc en totalité au groupe [V § 34] (0,25 pt). Il s'explique par une vente forcée : vendeur contraint par son calendrier de sortie de France, une seule offre [V § 35] (0,25 pt).

**PNC à la date d'acquisition (0,5 pt)** : 10 % × 8 000 000 = **800 000 €**, évaluées à leur quote-part de l'actif net identifiable selon le manuel [V IFRS 3 § 19 ; annexe 1.2, point 3] ; elles ne reçoivent aucune part du profit.

**Comparaison avec le règlement ANC (0,5 pt).** Le coût d'acquisition comprendrait les frais, nets de l'économie d'impôt, nulle ici puisque ces frais n'ont aucun effet fiscal (annexe 1.6) : 6 300 000 + 240 000 = 6 540 000 €. L'écart d'acquisition négatif (7 200 000 – 6 540 000 = 660 000 €) serait inscrit au passif et, l'acquisition ayant été réalisée dans des conditions avantageuses, repris immédiatement en résultat [V ANC art. 231-2, 231-12 et IR3 ; F05 § 1.1, § 1.3, § 8].

#### d. Écritures des écarts d'évaluation (2 pts)

**C8 (bilan, écarts au 01/01/2026, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Concessions et droits similaires, brevets, licences, marques (marque Trévance) | 1 200 000 | |
| 2115 Terrains bâtis | 200 000 | |
| 2131 Bâtiments | 600 000 | |
| 355 Produits finis | 200 000 | |
| IDP Impôt différé passif (2 200 000 × 25 %) | | 550 000 |
| RSV.TREVANCE Réserves TRÉVANCE – écarts d'évaluation nets | | 1 650 000 |
| **Total** | **2 200 000** | **2 200 000** |
| | *Libellé : écarts d'évaluation de TRÉVANCE à la date d'acquisition, après réexamen* | | |

**C9 (bilan, incidences de 2026, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.TREVANCE Résultat TRÉVANCE (230 000 net d'impôt) | 172 500 | |
| IDP Impôt différé passif (230 000 × 25 %) | 57 500 | |
| 355 Produits finis (stocks acquis, vendus en 2026) | | 200 000 |
| 28131 Amortissements des bâtiments (600 000 / 20) | | 30 000 |
| **Total** | **230 000** | **230 000** |

**C9R (compte de résultat, 0,5 pt)** : débit 7135 Variation des stocks de produits 200 000 ; débit 6811 Dotations aux amortissements 30 000 ; crédit CH_ID Produit d'impôt différé 57 500 ; crédit RES_CR Résultat 172 500.

La marque, à durée d'utilité indéterminée, n'est pas amortie [V IAS 38 § 88, 107 ; F05 § 11] ; son impôt différé passif (300 000 €) demeure, comme celui du terrain (50 000 €). Les stocks réévalués ayant été vendus, leur écart passe en charges en 2026 et son impôt différé est soldé.

**Réponses tolérées (1.6)**
- En a, retraitement des frais regroupé avec l'élimination des titres (titres crédités pour 6 540 000 € et charge de 240 000 €).
- En c, profit présenté en « autres produits opérationnels » ou sur une ligne distincte ; comparaison ANC sans le chiffre de 660 000 €, si la reprise immédiate en résultat et l'inclusion des frais dans le coût sont dites ; écart négatif de 720 000 € accepté si le candidat écrit l'hypothèse d'une économie d'impôt de 25 % sur les frais.
- En d, C8 et C9 regroupées en une écriture nette au 31/12/2026 (stocks soldés, bâtiment net de 570 000 €), si les montants de résultat et de réserves sont distingués.

**Erreurs fréquentes (1.6)**
- Frais inclus dans la contrepartie selon le raisonnement de l'ANC (`JUR-G02`, erreur symétrique), ce qui ramène le profit à 660 000 € (montant de l'écart négatif en ANC, pas du profit en IFRS) ; profit calculé sur la première évaluation (1 170 000 €).
- Profit réparti 90 / 10, ou PNC évaluées à 10 % du prix « implicite » ; écart négatif inscrit au passif et étalé.
- Marque amortie ; impôt différé omis sur les écarts (`JUR-G06`) ; écart sur les stocks maintenu au bilan au 31/12/2026.

**Références normatives (1.6)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 18, 19, 24, 32, 34, 35, 36, 53, B31 | Juste valeur, PNC, impôts différés, acquisition à des conditions avantageuses, frais, marque | [V] | F05 § 2, § 11 ; F03 § 11 |
| IAS 12 § 66 | Impôts différés d'un regroupement | [V] | F05 § 2 |
| IAS 38 § 12, 88, 107 | Marque identifiable ; durée indéterminée, non amortie | [V] | F03 § 11 ; F05 § 11 |
| ANC 2020-01 art. 231-2, 231-12 et IR3 | Coût avec frais nets d'impôt ; écart négatif, reprise immédiate | [V] | F05 § 1.1, § 1.3, § 8 |

---

### 1.7 Partage des capitaux propres et mise en équivalence (4,5 pts)

#### a. Tableaux de partage au 31/12/2026 (1,5 pt)

**CARTONNERIE DU BESSIN (intérêt 75 %) (0,75 pt)**

| Capitaux propres retraités (subvention exclue) | Total | Groupe (75 %) | PNC (25 %) |
|---|---:|---:|---:|
| Capital | 3 000 000 | 2 250 000 | 750 000 |
| Réserves | 5 000 000 | 3 750 000 | 1 250 000 |
| **Sous-total** | **8 000 000** | **6 000 000** | **2 000 000** |
| – Titres CARTONNERIE | | – 4 260 000 | |
| + Goodwill de 2019 | | + 360 000 | |
| **Réserves consolidées / PNC hors résultat** | | **2 100 000** | **2 000 000** |
| Résultat de 2026 (retraitement de la subvention sans effet) | 1 360 000 | **1 020 000** | **340 000** |

Contrôle : 75 % × (8 000 000 – 5 200 000) = 2 100 000 €, part du groupe dans les réserves accumulées depuis 2019.

**TRÉVANCE (intérêt 90 %) (0,75 pt)**

| Capitaux propres retraités | Total | Groupe (90 %) | PNC (10 %) |
|---|---:|---:|---:|
| Capital | 2 500 000 | 2 250 000 | 250 000 |
| Réserves (comptes individuels) | 3 850 000 | 3 465 000 | 385 000 |
| Écarts d'évaluation nets | 1 650 000 | 1 485 000 | 165 000 |
| **Sous-total = actif net identifiable au 01/01/2026** | **8 000 000** | **7 200 000** | **800 000** |
| – Titres TRÉVANCE (6 540 000 – 240 000) | | – 6 300 000 | |
| **Profit sur acquisition (groupe, résultat de 2026) / PNC à l'entrée** | | **900 000** | **800 000** |
| Résultat retraité : 1 100 000 – 172 500 | 927 500 | **834 750** | **92 750** |

TRÉVANCE, acquise le 01/01/2026, n'apporte aucune réserve consolidée : l'excédent de 900 000 € est le profit de l'exercice, porté au **résultat consolidé de 2026** part du groupe (834 750 + 900 000 = 1 734 750 €). PNC au 31/12/2026 : 800 000 + 92 750 = **892 750 €**.

#### b. Mise en équivalence (1 pt, 0,5 pt par société)

| | MINOTERIE (30 %) | FARINES ET MIX (25 %) |
|---|---:|---:|
| Capitaux propres hors résultat au 31/12/2026 | 13 000 000 | 3 200 000 |
| Quote-part du groupe | 3 900 000 | 800 000 |
| – Titres éliminés | – 2 700 000 | – 500 000 |
| **Réserves consolidées** | **1 200 000** | **300 000** |
| **Quote-part du résultat de 2026** | **480 000** | **120 000** |
| **Valeur de la participation mise en équivalence** | **4 380 000** | **920 000** |

Les titres ayant été acquis (MINOTERIE) ou souscrits (FARINES ET MIX) pour la quote-part de capitaux propres évalués à leur juste valeur, il n'y a ni goodwill ni écart d'évaluation à inclure dans la valeur d'équivalence [V IAS 28 § 32 ; F05 § 4]. FARINES ET MIX est mise en équivalence à 25 % seulement (rupture de chaîne, question 1.2) ; à 31 %, la valeur aurait été de 1 140 800 € et la quote-part de 148 800 €.

#### c. Écritures (2 pts)

**C10 (bilan, TRÉVANCE, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.TREVANCE Capital TRÉVANCE | 2 500 000 | |
| RSV.TREVANCE Réserves (3 850 000 + écarts nets 1 650 000) | 5 500 000 | |
| RST.TREVANCE Résultat retraité | 927 500 | |
| 261.CROQUENVILLE Titres TRÉVANCE (après C7) | | 6 300 000 |
| RST_G Résultat consolidé – part du groupe (834 750 + 900 000) | | 1 734 750 |
| RSV_M PNC – quote-part de l'actif net identifiable (10 % × 8 000 000) | | 800 000 |
| RST_M PNC – résultat (10 % × 927 500) | | 92 750 |
| **Total** | **8 927 500** | **8 927 500** |
| | *Libellé : élimination des titres TRÉVANCE, profit sur acquisition et partage* | | |

**C10R (compte de résultat, 0,25 pt)** : débit RES_CR Résultat 900 000 ; crédit PROFIT_ACQ Profit sur acquisition à des conditions avantageuses 900 000.

**C11 (bilan, CARTONNERIE DU BESSIN, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.CARTONNERIE Capital | 3 000 000 | |
| RSV.CARTONNERIE Réserves (subvention exclue, après C2) | 5 000 000 | |
| RST.CARTONNERIE Résultat | 1 360 000 | |
| EA Goodwill de 2019 | 360 000 | |
| 261.CROQUENVILLE Titres CARTONNERIE | | 4 260 000 |
| RSV_G Réserves consolidées – part du groupe | | 2 100 000 |
| RST_G Résultat consolidé – part du groupe | | 1 020 000 |
| RSV_M PNC – réserves | | 2 000 000 |
| RST_M PNC – résultat | | 340 000 |
| **Total** | **9 720 000** | **9 720 000** |

**C12 (bilan, MINOTERIE, 0,25 pt)** : débit TME Titres mis en équivalence 4 380 000 ; crédit 261.CROQUENVILLE Titres MINOTERIE 2 700 000 ; crédit RSV_G 1 200 000 ; crédit RST_G 480 000. **C12R** : débit RES_CR 480 000 ; crédit QP_MEE Quote-part du résultat net des entités mises en équivalence 480 000.

**C13 (bilan, FARINES ET MIX, 0,25 pt)** : débit TME 920 000 ; crédit 261.CROQUENVILLE Titres FARINES ET MIX 500 000 ; crédit RSV_G 300 000 ; crédit RST_G 120 000. **C13R (0,25 pt avec C12R)** : débit RES_CR 120 000 ; crédit QP_MEE 120 000.

**Réponses tolérées (1.7)**
- Excédent de TRÉVANCE crédité d'abord à un compte d'écart d'acquisition négatif, puis viré en résultat part du groupe par une seconde écriture ; profit présenté sur une ligne « autres produits opérationnels ».
- Goodwill de la CARTONNERIE présenté hors du tableau de partage ; mise en équivalence présentée en une seule écriture pour les deux sociétés.
- Cohérence avec un résultat erroné aux questions 1.3 à 1.6 : l'erreur n'est pénalisée qu'une fois (`JUR-F08`).

**Erreurs fréquentes (1.7)**
- Subvention de 594 000 € partagée avec les capitaux propres de la CARTONNERIE (`JUR-G04`) ; profit de 900 000 € porté en réserves consolidées ou partagé avec les PNC.
- Valeur d'équivalence de FARINES ET MIX calculée à 31 % ; titres de FARINES ET MIX détenus par la MINOTERIE éliminés dans les comptes consolidés ; dividende de la MINOTERIE ajouté à la valeur d'équivalence (`JUR-G03`).
- Écritures déséquilibrées (`JUR-F04`).

**Références normatives (1.7)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 22, B86 | PNC dans les capitaux propres ; élimination des titres | [V] | F03 § 3, F05 § 3 |
| IFRS 3 § 19, 34 | PNC à la quote-part ; profit attribué à l'acquéreur | [V] | F05 § 2, § 11 |
| IAS 28 § 10, 27, 32 | Mise en équivalence ; rupture de chaîne ; goodwill inclus dans la participation | [V] | F05 § 4 ; F03 § 4.2 |

---

### 1.8 Processus et documents de synthèse (7,5 pts)

#### a. Phases du processus et tableau de variation des capitaux propres (2,5 pts)

| Phase | Élément (question) | Ligne du tableau de variation de 2026 | Colonne |
|---|---|---|---|
| 1. Retraitements des comptes individuels | Engagements de retraite (1.3) | Ouverture (– 2 700 000, déjà compris) ; résultat net (– 148 500) ; autres éléments du résultat global (– 76 500) | Part du groupe |
| | Subvention de la CARTONNERIE (1.4) | Aucune : reclassement sans effet sur le résultat ; la subvention est déjà exclue des capitaux propres d'ouverture | Part du groupe et PNC (dans l'ouverture) |
| | Frais d'acquisition des titres TRÉVANCE (1.6 a) | Résultat net (– 240 000) | Part du groupe |
| 2. Éliminations des opérations internes | Lot en transit, soldes et ventes réciproques (1.5 a) | Aucune | — |
| | Marge interne descendante (1.5 b) | Résultat net (– 90 000) | Part du groupe |
| | Dividendes internes (1.5 d) | Résultat net (– 720 000 par rapport aux résultats individuels) ; pas de ligne « dividendes », la distribution restant dans le groupe | Part du groupe |
| 3. Regroupement d'entreprises (TRÉVANCE) | Écarts d'évaluation à la date d'acquisition et PNC (1.6 b, c) | Entrée de TRÉVANCE dans le périmètre (+ 800 000) | PNC |
| | Incidences de 2026 des écarts d'évaluation (1.6 d) | Résultat net (– 172 500, réparti 90 / 10) | Part du groupe et PNC |
| | Profit sur acquisition (1.6 c) | Résultat net (+ 900 000) | Part du groupe |
| 4. Partage et mise en équivalence | Partage de la CARTONNERIE et de TRÉVANCE (1.7 a) | Résultat net (parts de 75 / 25 et 90 / 10) ; dividendes versés à la famille du fondateur (– 200 000) | Part du groupe et PNC |
| | Mise en équivalence de la MINOTERIE et de FARINES ET MIX (1.7 b) | Résultat net (+ 600 000) ; le dividende de la MINOTERIE réduit la participation, sans ligne propre | Part du groupe |

**Barème** : 0,25 pt par groupe de lignes correctement classé et rattaché à sa ligne et à sa colonne (retraites ; subvention ; frais d'acquisition ; opérations réciproques ; marge ; dividendes internes ; entrée de TRÉVANCE ; écarts et profit ; partage ; mise en équivalence). L'ordre des phases traduit la logique du processus : les comptes individuels sont d'abord rendus conformes aux méthodes du groupe, puis les opérations internes sont éliminées, avant la comptabilisation du regroupement, l'élimination des titres et le partage, qui portent sur des capitaux propres **retraités** [V IFRS 10 § 19, B86 ; F04 § 1 ; F03 § 3]. Le tableau de variation ne fait apparaître que les opérations avec des tiers : résultat global, distributions aux actionnaires de CROQUENVILLE et aux minoritaires, entrée d'une filiale.

#### b. Résultat net consolidé et tableau de variation des capitaux propres (2,5 pts)

**Résultat net consolidé de 2026 (1,5 pt)**

| Élément | Ensemble | Part du groupe | PNC |
|---|---:|---:|---:|
| Résultats individuels des sociétés intégrées : 14 260 000 + 1 360 000 + 1 100 000 | 16 720 000 | 16 270 000 | 450 000 |
| Engagements de retraite (1.3) | – 148 500 | – 148 500 | 0 |
| Subvention (1.4) | 0 | 0 | 0 |
| Frais d'acquisition (1.6 a) | – 240 000 | – 240 000 | 0 |
| Marge interne descendante (1.5 b) | – 90 000 | – 90 000 | 0 |
| Dividendes internes (1.5 d) | – 720 000 | – 720 000 | 0 |
| Incidences de 2026 des écarts d'évaluation de TRÉVANCE (1.6 d) | – 172 500 | – 155 250 | – 17 250 |
| Profit sur acquisition (1.6 c) | + 900 000 | + 900 000 | 0 |
| Quote-part des entités mises en équivalence : 480 000 + 120 000 | + 600 000 | + 600 000 | 0 |
| **Résultat net consolidé** | **16 849 000** | **16 416 250** | **432 750** |

Répartition de départ : CROQUENVILLE au groupe ; CARTONNERIE 1 020 000 / 340 000 ; TRÉVANCE 990 000 / 110 000. Contrôle par les partages : CROQUENVILLE 14 260 000 – 148 500 – 240 000 – 90 000 – 720 000 = 13 061 500 ; CARTONNERIE 1 020 000 ; TRÉVANCE 834 750 + 900 000 ; mises en équivalence 600 000 ; total **16 416 250 €**. PNC : 340 000 + 92 750 = **432 750 €**.

**Extrait du tableau de variation des capitaux propres consolidés de 2026 (1 pt)**

| | Part du groupe | PNC | Total |
|---|---:|---:|---:|
| Capitaux propres au 01/01/2026 (fournis) | 123 020 000 | 2 200 000 | 125 220 000 |
| Résultat net de 2026 | 16 416 250 | 432 750 | 16 849 000 |
| Autres éléments du résultat global (réévaluations du régime de retraite, nettes d'impôt) | – 76 500 | — | – 76 500 |
| **Résultat global de 2026** | **16 339 750** | **432 750** | **16 772 500** |
| Dividendes distribués | – 5 400 000 | – 200 000 | – 5 600 000 |
| Entrée de TRÉVANCE dans le périmètre | — | 800 000 | 800 000 |
| **Capitaux propres au 31/12/2026** | **133 959 750** | **3 232 750** | **137 192 500** |

Le tableau rapproche, pour chaque composante, l'ouverture et la clôture, en distinguant le résultat net, les autres éléments du résultat global et les transactions avec les propriétaires, et sépare la part des propriétaires de la société mère de celle des PNC [V IAS 1 § 106 ; F14 § 2.4]. Contrôle des PNC de clôture : CARTONNERIE 25 % × 9 360 000 = 2 340 000 ; TRÉVANCE 10 % × (8 000 000 + 927 500) = 892 750 ; total 3 232 750 €.

#### c. État du résultat net et des autres éléments du résultat global (2,5 pts)

**Extrait de l'état de 2026 (présentation selon IAS 1)**

| Poste | Montant |
|---|---:|
| … (produits et charges opérationnels, dont frais d'acquisition de 240 000 €) | … |
| Profit sur acquisition à des conditions avantageuses (TRÉVANCE) | 900 000 |
| … (résultat financier, charge d'impôt) | … |
| Quote-part du résultat net des entités mises en équivalence | 600 000 |
| **Résultat net de l'ensemble consolidé** | **16 849 000** |
| – attribuable aux propriétaires de la société mère | 16 416 250 |
| – attribuable aux participations ne donnant pas le contrôle | 432 750 |
| *Autres éléments du résultat global* | |
| Éléments qui ne seront pas reclassés en résultat net : réévaluations du passif net au titre des régimes à prestations définies | – 102 000 |
| Impôt sur ces éléments | + 25 500 |
| Éléments qui pourront être reclassés en résultat net | — |
| **Total des autres éléments du résultat global, nets d'impôt** | **– 76 500** |
| **Résultat global de l'exercice** | **16 772 500** |
| – attribuable aux propriétaires de la société mère | 16 339 750 |
| – attribuable aux participations ne donnant pas le contrôle | 432 750 |

**Barème** : profit sur acquisition et quote-part des entités mises en équivalence sur leurs lignes (0,5 pt) ; résultat net et sa répartition (0,5 pt) ; section des autres éléments du résultat global : écart actuariel parmi les éléments non reclassables (0,5 pt), avec son impôt et le total net (0,5 pt) ; résultat global et sa répartition (0,5 pt).

**Justification.** L'état présente le résultat net, le total des autres éléments du résultat global et le résultat global, chacun réparti entre les propriétaires de la société mère et les PNC [V IAS 1 § 81A, 81B ; F14 § 2.3] ; la quote-part des entités mises en équivalence est un poste obligatoire [V § 82 c)] ; le profit sur acquisition peut figurer sur un poste supplémentaire [V § 85] et les notes en indiquent le poste [V IFRS 3 B64 n)]. Les autres éléments du résultat global sont classés entre éléments non reclassables et reclassables [V IAS 1 § 82A] ; les réévaluations d'IAS 19 ne sont jamais reclassées [V IAS 19 § 122 ; F14 § 2.3] ; leur impôt est présenté dans l'état ou en note [V IAS 1 § 90, 91]. CROQUENVILLE, mère, porte seule le régime de retraite : les PNC n'ont aucune part des autres éléments du résultat global. La présentation suit **IAS 1** : IFRS 18, qui remplacera IAS 1 pour les exercices ouverts à compter du 01/01/2027, n'est pas appliquée par anticipation [V F14 § 0].

**Réponses tolérées (1.8)**
- En a, frais d'acquisition rangés dans la phase du regroupement d'entreprises ; dividendes internes rangés dans la phase de partage ; écarts d'évaluation rangés dans les retraitements (évaluation à la juste valeur des actifs acquis), si la justification est donnée.
- En b, tableau de variation présentant le résultat global sur une seule ligne, avec le détail en note ; tableau partant du résultat de chaque société retraitée, s'il aboutit aux mêmes totaux.
- En c, deux états distincts (état du résultat net, puis état du résultat global commençant par le résultat net) [V IAS 1 § 10A] ; autres éléments du résultat global présentés nets d'impôt (– 76 500 €) avec l'impôt en note.

**Erreurs fréquentes (1.8)**
- Dividendes internes (720 000 €) portés en diminution des capitaux propres consolidés ; dividende de la CARTONNERIE versé aux minoritaires oublié.
- Entrée de TRÉVANCE dans le périmètre présentée dans la colonne du groupe (prix payé) ; profit de 900 000 € présenté en autres éléments du résultat global.
- Écart actuariel présenté parmi les éléments reclassables, ou réparti entre groupe et PNC ; quote-part des mises en équivalence à 31 % pour FARINES ET MIX ; présentation selon IFRS 18 (`JUR-G01`).

**Références normatives (1.8)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 19, B86 | Méthodes uniformes ; procédures de consolidation | [V] | F04 § 1 ; F03 § 3 |
| IAS 1 § 10A, 81A, 81B, 82 c), 82A, 85, 90, 91, 106 | Résultat global, attribution, postes, OCI, impôt, variation des capitaux propres | [V] | F14 § 2.1, § 2.3, § 2.4 |
| IAS 19 § 122 | Réévaluations non reclassées | [V] | F14 § 2.3 ; F04 § 7 |
| IFRS 3 B64 n) | Poste du profit sur acquisition | [V] | F05 § 11 |
| Règlement (UE) 2026/338 ; IFRS 18 § C1 | IFRS 18 applicable à compter de 2027 | [V] | F14 § 0 |

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 a) Qualification, distinctions et référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2 |
| 2.1 b) Branche complète, régime de faveur et valeur fiscale des actions reçues | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 3 |
| 2.2 Contrôle, sens de l'opération et mode d'évaluation des apports | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 2,5 |
| 2.3 a) Actif net apporté et composition | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 3 |
| 2.3 b) Actions émises, prime, répartition du capital et équité | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 3,5 |
| 2.4 a) Écritures chez VERGERS DE LA PASSAIS | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) ; `1.3.c` Passer les écritures complémentaires | 2,5 |
| 2.4 b) Augmentation de capital et réalisation des apports chez JUS DU BOCAGE | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 3 |
| 2.4 c) Écritures complémentaires chez JUS DU BOCAGE | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 3 |
| 2.5 Note à la présidente de VERGERS DE LA PASSAIS | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2,5 |
| **Total** | | **25** |

---

### 2.1 Analyse de l'opération (5 pts)

**a) Qualification, distinctions et référentiel (2 pts)**
- *Qualification (0,75 pt).* L'opération est un **apport partiel d'actif constituant une branche d'activité** : VERGERS DE LA PASSAIS apporte à JUS DU BOCAGE un ensemble d'actifs et de passifs qui forme une branche autonome, celle des jus, et reçoit en échange des **actions de la bénéficiaire** [V PCG art. 710-2, F01 § 1 ; annexe 2.5]. JUS DU BOCAGE rémunère l'apport par une **augmentation de capital** réservée à l'apporteuse. Contrairement à une fusion, l'apporteuse **n'est pas dissoute** : elle poursuit ses activités cidricoles, et ce sont ses actifs qui changent de nature, la branche étant remplacée à son bilan par des titres de participation. Ses propres actionnaires, la famille VAUFLEURY, ne reçoivent rien.
- *Différence avec une cession (0,5 pt).* Dans une cession, JUS DU BOCAGE paierait la branche en numéraire : VERGERS DE LA PASSAIS encaisserait un prix, constaterait un résultat de cession et ne garderait aucun lien avec l'activité. Ici, elle est rémunérée en actions : elle reste exposée à l'activité des jus, désormais par l'intermédiaire de sa filiale, et sa participation dans JUS DU BOCAGE se renforce.
- *Différence avec un apport à une société nouvelle (0,5 pt).* Une société créée pour recevoir la branche n'aurait ni activité ni associé autre que VERGERS DE LA PASSAIS, qui en détiendrait tout le capital. JUS DU BOCAGE, au contraire, a une **activité préexistante** (jus de fruits et nectars) et un **associé minoritaire**, ANDAINE Capital : le nombre d'actions à émettre dépend du rapport entre la valeur de la branche et celle de la bénéficiaire, et l'opération modifie la répartition de son capital (voir 2.3 b).
- *Référentiel (0,25 pt).* L'opération est enregistrée dans les comptes individuels des deux sociétés selon le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe la valeur d'inscription des apports [V art. 710-1 et 720-1, F01 § 1]. Le nombre d'actions se calcule, lui, sur les valeurs d'échange [V art. 740-1, F01 § 1 ; annexe 2.5].

**b) Branche complète, régime de faveur et valeur fiscale des actions reçues (3 pts)**
- *Branche complète d'activité (1 pt).* Le régime de faveur s'applique de plein droit à l'apport d'une **branche complète d'activité** entre sociétés passibles de l'impôt sur les sociétés [V CGI art. 210 B-1 et 210 C-1, F02 § 1] ; les deux sociétés le sont (annexe 2.1). La branche complète est l'ensemble des éléments d'actif et de passif d'une division qui constituent une exploitation autonome, capable de fonctionner par ses propres moyens [V BOI-IS-FUS-20-20 § 10, F02 § 1]. Appréciée selon l'organisation de **VERGERS DE LA PASSAIS** [V même BOI § 20 et 90], la branche des jus en a les caractéristiques :
  - une activité réellement exercée, sur un **site propre** (Flers), distinct de la cidrerie de Domfront-en-Poiraie, avec ses installations, son bâtiment et sa ligne ;
  - un **personnel** affecté (26 salariés et deux commerciaux), qui suit la branche [V même BOI § 60] ;
  - une **clientèle** propre, sa marque, ses conditions de vente et ses contrats ;
  - les **services communs** du siège (comptabilité, paie, informatique) rattachés pour leur quote-part : le poste de l'assistante qui traite les commandes de jus et les licences du logiciel commercial suivent la branche [V même BOI § 80]. Que JUS DU BOCAGE dispose de ses propres services comptables et administratifs est sans incidence : la branche s'apprécie selon l'organisation de l'apporteuse, non de la bénéficiaire [V même BOI § 20 et 90] ; c'est le rattachement de la quote-part des services communs qui assure son autonomie ;
  - la branche emporte les éléments d'actif et de passif qui s'y rattachent (stocks, clients, fournisseurs, dettes sociales, provision pour risque de retrait) ; la trésorerie, gérée par le siège, n'en est pas un élément nécessaire.
- *Terrain voisin (0,5 pt).* Il **ne doit pas être apporté**. La branche comprend tous les éléments liés à l'exploitation apportée et **aucun patrimoine étranger** à cette exploitation [V BOI-IS-FUS-20-20, partie I-B, F02 § 1] : ce terrain nu n'est pas utilisé par la branche et VERGERS DE LA PASSAIS envisage de le vendre. Le joindre « pour simplifier » ferait entrer dans l'apport un élément isolé, sans lien avec l'activité, et mettrait en cause la qualification de branche complète, donc le régime de plein droit ; c'est au contraire le **terrain du site**, qui porte l'atelier, qui doit être apporté. Le projet de traité est conforme.
- *Régime de plein droit (0,25 pt).* Les conditions étant remplies, l'apport relève du régime de faveur **de plein droit**, **sans engagement de conservation** des actions reçues depuis 2018 ; un **agrément** ne serait nécessaire que si la branche n'était pas complète [V BOI-IS-FUS-20-40 ; CGI art. 210 B-3, F02 § 1].
- *Effets pour VERGERS DE LA PASSAIS (0,5 pt).* La plus-value latente de la branche (valeur d'échange 3 200 000 € – actif net comptable 1 785 000 € = 1 415 000 €, voir 2.3 a) **n'est pas imposée** [V CGI art. 210 A-1, applicable aux apports par 210 B-1, F02 § 2]. La provision pour risque de retrait n'est pas réintégrée tant qu'elle n'est pas devenue sans objet, et les résultats de la branche ne sont pas imposés immédiatement [V BOI-IS-FUS-20-40-30 § 100 et 110, F02 § 1]. La reprise en résultat des amortissements dérogatoires de la ligne est déduite extra-comptablement, puisqu'ils sont reconstitués chez JUS DU BOCAGE [V BOI-IS-FUS-30-20 § 10, F02 § 1], et l'option du traité reporte sur JUS DU BOCAGE l'imposition du solde de la subvention, 180 000 € [V CGI art. 42 septies, 1, al. 5, F02 § 1]. En droit commun, l'apport serait une cessation partielle d'entreprise : l'écart entre la valeur réelle de la branche et sa valeur fiscale (3 200 000 – 1 599 000 = 1 601 000 €) et le solde de la subvention seraient imposés immédiatement.
- *Effets pour JUS DU BOCAGE (0,5 pt).* Elle prend les engagements du régime [V CGI art. 210 A-3, F02 § 4] : reprendre à son passif la provision et les **amortissements dérogatoires** de la ligne et les réintégrer dans les mêmes conditions que VERGERS DE LA PASSAIS (engagement a) ; apports inscrits à la valeur comptable, avec les valeurs d'origine, les amortissements et les dépréciations, donc aucune plus-value à réintégrer et des amortissements calculés sur les bases de l'apporteuse [V BOI-IS-FUS-30-20 § 10, F01 § 3.2] ; terrain et stocks repris à leur valeur fiscale (engagements c et e). Par l'option du traité, elle rapporte à son résultat imposable le **solde de la subvention** (180 000 €) au rythme de l'amortissement de la ligne [V CGI art. 42 septies ; BOI-IS-FUS-10-20-40-10 § 180, F02 § 1].
- *Valeur fiscale des actions reçues (0,25 pt).* En cas de cession ultérieure, la plus-value sur les 50 000 actions reçues sera calculée d'après la valeur que les biens apportés avaient, du point de vue fiscal, dans les écritures de VERGERS DE LA PASSAIS [V CGI art. 210 B-2, F02 § 1]. La ligne de Flers ayant été amortie plus vite fiscalement, sa valeur fiscale est inférieure de 186 000 € (les amortissements dérogatoires) à sa valeur comptable : valeur fiscale des actions = 1 785 000 – 186 000 = **1 599 000 €**, pour une valeur comptable de 1 785 000 €.

---

### 2.2 Contrôle, sens de l'opération et mode d'évaluation des apports (2,5 pts)

- *Situation de contrôle (0,75 pt).* VERGERS DE LA PASSAIS détient 80 % des droits de vote de JUS DU BOCAGE (une voix par action, aucun pacte, aucun droit particulier d'ANDAINE Capital) : elle la contrôle **de manière exclusive** [V PCG art. 741-2, renvoi à l'art. 211-3 du règlement ANC 2020-01, F01 § 2.1]. L'une des sociétés participantes contrôlant préalablement l'autre, l'opération est réalisée **sous contrôle commun** [V art. 741-1, F01 § 2.1]. La présence d'un associé minoritaire, ici une société de capital-investissement, ne change rien : le contrôle s'apprécie entre les sociétés participantes.
- *Règle (0,5 pt).* Sous contrôle commun, les apports sont évalués à la **valeur comptable**, que l'opération soit à l'endroit ou à l'envers : l'opération ne fait que maintenir ou renforcer un contrôle existant, il convient de ne pas réévaluer [V art. 743-1, tableau, cas 1 et 2, F01 § 2.3 ; annexe 2.5]. JUS DU BOCAGE reprend donc chaque actif et chaque passif de la branche pour sa valeur dans les comptes de VERGERS DE LA PASSAIS au 31/03/2027 [V art. 744-2, F01 § 3.2].
- *Sens de l'opération (0,75 pt).* L'apport est **à l'envers** lorsque l'apporteuse prend ou renforce le contrôle de la bénéficiaire [V art. 742-2, F01 § 2.2]. VERGERS DE LA PASSAIS passe de 80 % à **90 %** du capital de JUS DU BOCAGE (voir 2.3 b) : elle renforce son contrôle, l'apport est à l'envers. Le sens ne modifie pas la conclusion : sous contrôle commun, la valeur comptable s'impose dans les deux sens. (Sous contrôle distinct, un apport à l'envers serait aussi évalué à la valeur comptable.)
- *Exception (0,5 pt).* La valeur réelle ne s'imposerait que si l'actif net comptable apporté ne suffisait pas à libérer l'augmentation de capital [V art. 743-3, F01 § 2.4 ; annexe 2.5]. Ici l'actif net comptable, **1 785 000 €** (voir 2.3 a), dépasse l'augmentation de capital, **1 000 000 €** (voir 2.3 b) : l'exception ne joue pas. La valeur d'échange de la branche (3 200 000 €) ne sert qu'au calcul du nombre d'actions.

---

### 2.3 Apports, actions émises et équité (6,5 pts)

**a) Actif net apporté et composition (3 pts)**
- *Actifs apportés (1 pt)* — valeurs d'origine, amortissements et dépréciations repris de VERGERS DE LA PASSAIS [V art. 744-2 ; BOI-IS-FUS-30-20 § 10, F01 § 3.2] :

| Élément apporté | Valeur brute | Amortissements et dépréciations | Valeur apportée |
|---|---:|---:|---:|
| Terrain du site de Flers | 120 000 | | 120 000 |
| Bâtiment (atelier et chai) | 900 000 | 405 000 | 495 000 |
| Ligne de pressage, de pasteurisation et d'embouteillage | 1 200 000 | 480 000 | 720 000 |
| Cuves de stockage et matériel de manutention | 340 000 | 220 000 | 120 000 |
| Matières premières et emballages | 110 000 | | 110 000 |
| Produits finis | 170 000 | 20 000 | 150 000 |
| Clients | 486 000 | 36 000 | 450 000 |
| **Total de l'actif apporté** | **3 326 000** | **1 161 000** | **2 165 000** |

- *Passifs et actif net (0,75 pt)* :

| | Montant |
|---|---:|
| Total de l'actif apporté (valeurs nettes) | 2 165 000 |
| Provision pour risque de retrait d'un lot | – 30 000 |
| Fournisseurs (dont 42 000 envers JUS DU BOCAGE) | – 290 000 |
| Dettes sociales | – 60 000 |
| **Actif net comptable apporté** | **1 785 000** |

- *Amortissements dérogatoires et subvention (0,75 pt).* Les amortissements dérogatoires (186 000 €) sont des **provisions réglementées**, classées dans les capitaux propres, comme la subvention d'investissement (300 000 – 120 000 = 180 000 €) [V PCG art. 214-8 et 313-1, F01 § 8]. Ni l'une ni l'autre n'est un actif ou un passif de la branche : elles **ne sont pas déduites** pour calculer l'actif net apporté, qui les **comprend** (elles font partie des capitaux propres de VERGERS DE LA PASSAIS qui financent les éléments apportés), et elles ne figurent pas dans l'écriture de réalisation des apports. JUS DU BOCAGE les **reconstituera ensuite par prélèvement sur la prime d'apport**, en application de ses engagements et de l'option du traité (voir 2.4 c) [F01 § 8 ; annexe 2.4].
- *Éléments sans valeur ou non apportés (0,5 pt).* La **marque** « Bulles du Passais », créée en interne et non inscrite au bilan, est apportée pour une valeur comptable nulle : la valeur comptable ne fait apparaître aucun élément non comptabilisé chez l'apporteuse. Le **terrain voisin** et la **trésorerie** ne sont pas apportés (voir 2.1 b). La valeur d'échange de la branche (3 200 000 €) dépasse l'actif net comptable de 1 415 000 €, écart qui n'est pas comptabilisé.

**b) Actions émises, prime, répartition du capital et équité (3,5 pts)**
- *Nombre d'actions (0,75 pt).* Pour un apport partiel d'actif, le nombre d'actions se calcule directement à partir de la valeur d'échange de l'apport [V méthode, F01 § 4]. Valeur unitaire de JUS DU BOCAGE : 3 200 000 / 50 000 = **64 €** ; actions à émettre : 3 200 000 / 64 = **50 000 actions**.
- *Augmentation de capital et prime (0,75 pt).* Augmentation de capital : 50 000 × 20 = **1 000 000 €** ; prime d'apport avant toute imputation = actif net comptable apporté – augmentation de capital = 1 785 000 – 1 000 000 = **785 000 €** [F01 § 4 et § 9]. La prime se calcule sur la valeur d'inscription des apports (comptable), non sur leur valeur d'échange.
- *Répartition du capital (0,75 pt)* — 50 000 + 50 000 = 100 000 actions :

| Associé | Actions avant | % avant | Actions après | % après |
|---|---:|---:|---:|---:|
| SA VERGERS DE LA PASSAIS | 40 000 | 80,00 % | 90 000 | 90,00 % |
| SAS ANDAINE Capital | 10 000 | 20,00 % | 10 000 | 10,00 % |
| **Total** | **50 000** | **100 %** | **100 000** | **100 %** |

- *Équité pour ANDAINE Capital (1,25 pt).* Sa part du capital est divisée par deux, mais elle porte sur une société dont la valeur double : avant l'apport, 10 000 × 64 = **640 000 €** ; après, la valeur de JUS DU BOCAGE est 3 200 000 + 3 200 000 = 6 400 000 €, soit 64 € par action, et sa part vaut 10 % × 6 400 000 = **640 000 €**. Symétriquement, VERGERS DE LA PASSAIS détenait 80 % × 3 200 000 + la branche (3 200 000) = 5 760 000 € et détient 90 % × 6 400 000 = 5 760 000 €. Les actions sont émises à leur valeur (64 €) en échange d'un apport évalué à sa valeur : **aucun associé ne s'enrichit au détriment de l'autre**, à condition que les deux valeurs d'échange soient justes. Si la branche ne valait en réalité que 2 800 000 €, la part d'ANDAINE Capital ne vaudrait que 10 % × 6 000 000 = 600 000 €, soit une perte de 40 000 € ; d'où l'intérêt pour l'associé minoritaire du rapport de l'évaluateur indépendant. La baisse de la valeur comptable par action (2 350 000 / 50 000 = 47 € avant, 4 111 000 / 100 000 = 41,11 € après, voir 2.5) tient seulement à l'inscription de l'apport à sa valeur comptable : ce n'est pas une perte de valeur.

*Pour aller plus loin (sans points).* Une rémunération calculée sur l'actif net comptable (1 785 000 / 64 = 27 890,625, soit 27 891 actions) aurait donné 12,84 % du capital à ANDAINE Capital, soit 821 661 € de valeur au lieu de 640 000 €, au détriment de VERGERS DE LA PASSAIS. Fiscalement, lorsque la valeur réelle des titres reçus est inférieure à celle de l'apport, l'apporteuse doit constater un produit imposable à hauteur de la différence ; la tolérance pour une rémunération sur l'actif net comptable suppose une détention d'au moins 99,99 % de la bénéficiaire [V BOI-IS-FUS-30-20 § 20 à 40, F02 § 1].

---

### 2.4 Écritures (8,5 pts)

**a) Chez VERGERS DE LA PASSAIS, le 1er avril 2027 (2,5 pts)**

L'apport étant évalué à la valeur comptable, les actions reçues sont inscrites pour la valeur d'apport [V PCG art. 1212-26, F01 § 9], égale à la valeur nette des éléments qui sortent : l'apport ne dégage **aucun résultat**. La reprise en résultat des amortissements dérogatoires et du solde de la subvention (A3) est une conséquence distincte de la sortie de la ligne, et non un résultat d'apport : un candidat qui écrit « aucun résultat sur l'apport » n'est pas pénalisé sur ce point, l'écriture A3 étant notée à part.

**A1 — Sortie des éléments de la branche (1 pt).** Valeurs brutes et amortissements et dépréciations soldés (0,5) ; provision et dettes (0,25) ; compte d'apport (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – JUS DU BOCAGE, compte d'apport | 1 785 000 | |
| 28131 Amortissements des bâtiments | 405 000 | |
| 28154 Amortissements des matériels industriels (ligne de Flers) | 480 000 | |
| 28153 Amortissements des installations à caractère spécifique (cuves, manutention) | 220 000 | |
| 395 Dépréciations des stocks de produits | 20 000 | |
| 491 Dépréciations des comptes de clients | 36 000 | |
| 1518 Autres provisions pour risques (retrait d'un lot) | 30 000 | |
| 401 Fournisseurs | 290 000 | |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales de la branche, personnel compris) | 60 000 | |
| 211 Terrains (site de Flers) | | 120 000 |
| 2131 Bâtiments | | 900 000 |
| 2154 Matériels industriels (ligne de Flers) | | 1 200 000 |
| 2153 Installations à caractère spécifique (cuves, manutention) | | 340 000 |
| 31 Matières premières et fournitures (pommes, emballages) | | 110 000 |
| 355 Produits finis | | 170 000 |
| 411 Clients | | 486 000 |
| **Total** | **3 326 000** | **3 326 000** |

**A2 — Réception des actions (0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation JUS DU BOCAGE (50 000 actions) | 1 785 000 | |
| 467 Divers comptes débiteurs – JUS DU BOCAGE, compte d'apport | | 1 785 000 |

**Sort des amortissements dérogatoires et de la subvention (1,25 pt)**
- *Justification (0,5 pt).* Après l'apport, VERGERS DE LA PASSAIS ne possède plus la ligne de Flers : les amortissements dérogatoires et la subvention qui s'y rattachent ne peuvent pas rester dans ses capitaux propres. Ils sont **repris en résultat** : produit de reprise des amortissements dérogatoires (186 000 €) et virement au résultat du solde de la subvention (180 000 €) [conséquence directe de la sortie du bien ; le produit de reprise des dérogatoires chez la société qui transmet les biens est visé par BOI-IS-FUS-30-20 § 10, F02 § 1]. Ces 366 000 € ne sont **pas imposés** chez VERGERS DE LA PASSAIS : la reprise des dérogatoires est déduite extra-comptablement, puisque JUS DU BOCAGE les reconstitue et les réintègre dans les mêmes conditions, et l'imposition du solde de la subvention est reportée sur JUS DU BOCAGE par l'option du traité [V BOI-IS-FUS-30-20 § 10 ; CGI art. 42 septies, 1, al. 5, F02 § 1]. Les capitaux propres totaux de VERGERS DE LA PASSAIS sont inchangés : 366 000 € passent des provisions réglementées et de la subvention au résultat de l'exercice.

**A3 — Reprise des dérogatoires et du solde de la subvention (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 145 Amortissements dérogatoires (ligne de Flers) | 186 000 | |
| 131 Subventions d'investissement octroyées | 300 000 | |
| 78725 Reprises sur provisions réglementées – amortissements dérogatoires | | 186 000 |
| 139 Subventions d'investissement inscrites au compte de résultat | | 120 000 |
| 747 Quote-part des subventions d'investissement virée au résultat de l'exercice (solde) | | 180 000 |
| **Total** | **486 000** | **486 000** |

**b) Chez JUS DU BOCAGE, le 1er avril 2027 : augmentation de capital et réalisation des apports (3 pts)**

**A4 — Augmentation de capital (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 1 785 000 | |
| 101 Capital (50 000 × 20) | | 1 000 000 |
| 1043 Primes d'apport (1 785 000 – 1 000 000) | | 785 000 |

**A5 — Réalisation des apports à la valeur comptable (2,25 pts).** Valeurs brutes (0,75) ; amortissements et dépréciations repris (0,75) ; provision, dettes et compte d'apport (0,75).

| Compte | Débit | Crédit |
|---|---:|---:|
| 211 Terrains (site de Flers) | 120 000 | |
| 2131 Bâtiments | 900 000 | |
| 2154 Matériels industriels (ligne de Flers) | 1 200 000 | |
| 2153 Installations à caractère spécifique (cuves, manutention) | 340 000 | |
| 31 Matières premières et fournitures (pommes, emballages) | 110 000 | |
| 355 Produits finis | 170 000 | |
| 411 Clients | 486 000 | |
| 28131 Amortissements des bâtiments | | 405 000 |
| 28154 Amortissements des matériels industriels (ligne de Flers) | | 480 000 |
| 28153 Amortissements des installations à caractère spécifique | | 220 000 |
| 395 Dépréciations des stocks de produits | | 20 000 |
| 491 Dépréciations des comptes de clients | | 36 000 |
| 1518 Autres provisions pour risques (retrait d'un lot) | | 30 000 |
| 401 Fournisseurs (dont 42 000 envers JUS DU BOCAGE) | | 290 000 |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | | 60 000 |
| 4561 Associés – Comptes d'apport en société | | 1 785 000 |
| **Total** | **3 326 000** | **3 326 000** |

La reprise des valeurs d'origine, des amortissements et des dépréciations est aussi la condition de l'admission fiscale des valeurs comptables [V BOI-IS-FUS-30-20 § 10, F01 § 3.2] : JUS DU BOCAGE poursuit l'amortissement de la ligne sur la base de 1 200 000 € et sur la durée restant à courir.

**c) Écritures complémentaires chez JUS DU BOCAGE (3 pts)**

*Reconstitution des amortissements dérogatoires et de la subvention (1,25 pt).* L'actif net apporté (1 785 000 €), donc la prime d'apport, comprend les 186 000 € d'amortissements dérogatoires et les 180 000 € de subvention nette (voir 2.3 a). JUS DU BOCAGE s'est engagée à reprendre les dérogatoires et à les réintégrer comme l'aurait fait VERGERS DE LA PASSAIS, et à rapporter à son résultat le solde de la subvention selon le plan d'amortissement de la ligne [V CGI art. 210 A-3 a ; BOI-IS-FUS-30-20 § 10 ; CGI art. 42 septies, 1, al. 5 ; BOI-IS-FUS-10-20-40-10 § 180, F02 § 1]. Elle les **reconstitue par prélèvement sur la prime d'apport** [V programme UE 4, compétence 1.3.c ; corrigé du sujet zéro p. imprimée 217, F01 § 8 ; écriture de la subvention : convention de rédaction, F01 § 8], la subvention pour son montant brut, diminué des 120 000 € déjà virés au résultat (annexe 2.4), par cohérence avec la reprise des valeurs brutes et des amortissements de la ligne (justification 0,5 ; écriture 0,75).

**A6 — Reconstitution (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1043 Primes d'apport (186 000 + 180 000) | 366 000 | |
| 139 Subventions d'investissement inscrites au compte de résultat | 120 000 | |
| 145 Amortissements dérogatoires | | 186 000 |
| 131 Subventions d'investissement octroyées | | 300 000 |
| **Total** | **486 000** | **486 000** |

*Frais d'apport (0,5 pt).* Ils peuvent être imputés sur les primes [V PCG art. 212-9, F01 § 7] ; JUS DU BOCAGE les impute sur la prime d'apport pour leur montant **net d'impôt** [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 32 000 × 75 % = **24 000 €** ; l'économie d'impôt (8 000 €) diminue l'impôt de 2027, les 32 000 € étant déduits extra-comptablement.

**A7 — Frais d'apport**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1043 Primes d'apport (32 000 × 75 %) | 24 000 | |
| 444 État – Impôts sur les bénéfices (32 000 × 25 %) | 8 000 | |
| 512 Banques | | 32 000 |

*Opération entre la branche et JUS DU BOCAGE (0,5 pt).* Avec la branche, JUS DU BOCAGE reçoit la dette de 42 000 € envers elle-même, alors qu'elle détient la créance correspondante sur VERGERS DE LA PASSAIS : elle devient créancière et débitrice de la même obligation, qui s'éteint par **confusion** [V C. civ. art. 1349, F01 § 8], sans effet sur le résultat.

**A8 — Extinction par confusion**

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette de la branche envers JUS DU BOCAGE) | 42 000 | |
| 411 Clients (créance de façonnage sur VERGERS DE LA PASSAIS) | | 42 000 |

*Subvention au 31 décembre 2027 (0,75 pt).* Comme la ligne, amortie 1 200 000 / 10 = 120 000 € par an, soit 90 000 € du 1er avril au 31 décembre 2027, la subvention est virée au résultat : 300 000 × 90 000 / 1 200 000 = **22 500 €** (calcul 0,5). Ce montant est aussi rapporté au résultat imposable de 2027, l'option du traité imposant à JUS DU BOCAGE de suivre le plan d'amortissement de VERGERS DE LA PASSAIS [V BOI-IS-FUS-10-20-40-10 § 180, F02 § 1] : aucun retraitement extra-comptable (0,25). Subvention nette au 31/12/2027 : 180 000 – 22 500 = 157 500 €.

**A9 — Quote-part de la subvention, 31 décembre 2027**

| Compte | Débit | Crédit |
|---|---:|---:|
| 139 Subventions d'investissement inscrites au compte de résultat | 22 500 | |
| 747 Quote-part des subventions d'investissement virée au résultat de l'exercice | | 22 500 |

Prime d'apport après imputations : 785 000 – 366 000 – 24 000 = **395 000 €**.

---

### 2.5 Note à Mme VAUFLEURY, présidente de VERGERS DE LA PASSAIS (2,5 pts)

**Capitaux propres de JUS DU BOCAGE juste après l'opération (1 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (50 000 → 100 000 actions de 20 €) | 1 000 000 | + 1 000 000 | 2 000 000 |
| Prime d'apport | 0 | + 785 000 – 366 000 – 24 000 | 395 000 |
| Réserve légale | 100 000 | | 100 000 |
| Autres réserves | 1 210 000 | | 1 210 000 |
| Report à nouveau | 40 000 | | 40 000 |
| Subvention d'investissement (300 000 – 120 000) | 0 | + 180 000 | 180 000 |
| Amortissements dérogatoires | 0 | + 186 000 | 186 000 |
| **Total** | **2 350 000** | **+ 1 761 000** | **4 111 000** |

Contrôle : + 1 761 000 = actif net comptable reçu (1 785 000) – frais nets d'impôt (24 000). La reconstitution déplace 366 000 € de la prime vers les provisions réglementées et la subvention, sans changer le total. Barème : tableau (0,75), total et contrôle (0,25).

**Effets sur VERGERS DE LA PASSAIS (0,75 pt)**
- *Bilan.* Les éléments de la branche sortent pour leur valeur nette (2 165 000 € d'actifs, 380 000 € de provision et de dettes) et sont remplacés par des titres de participation de 1 785 000 € : la participation dans JUS DU BOCAGE passe de 1 680 000 à **3 465 000 €** ; le total du bilan baisse de 380 000 €. VERGERS DE LA PASSAIS ne détient plus d'outil de production de jus, mais 90 % d'une société qui réunit les deux activités de jus.
- *Capitaux propres et résultat.* L'apport lui-même ne dégage aucun résultat. Le total des capitaux propres est **inchangé** (5 384 000 €) ; seule leur composition change : les amortissements dérogatoires de la ligne (186 000 €) et le solde de la subvention (180 000 €) sont repris en résultat le 1er avril 2027 : le résultat de l'exercice 2027 passe de 120 000 € au 31 mars à 486 000 € juste après l'opération. Ces **366 000 € de produits** sont sans encaissement, non récurrents et non imposables (déduits extra-comptablement) : il faudra les isoler pour apprécier la performance de 2027. À compter du 1er avril, les résultats des jus ne reviendront à VERGERS DE LA PASSAIS que par les dividendes de JUS DU BOCAGE, dont 10 % iront à ANDAINE Capital.

**Enjeux pour les parties prenantes (0,75 pt)**
- *ANDAINE Capital (0,25 pt).* Sa part passe de 20 % à 10 % et pèse moins dans les décisions, mais la valeur de ses actions est inchangée (640 000 €) si les valeurs d'échange sont justes ; elle détient désormais une part d'une société deux fois plus importante, qui réunit les deux activités de jus. Elle doit s'assurer de la valeur retenue pour la branche.
- *Créanciers de la branche (0,25 pt).* Les fournisseurs (248 000 € après extinction de la dette envers JUS DU BOCAGE), les organismes sociaux et le personnel ont désormais pour débiteur JUS DU BOCAGE, dont les capitaux propres passent de 2 350 000 € à 4 111 000 € et qui reçoit en même temps les actifs de la branche, dont 450 000 € de créances clients et 260 000 € de stocks nets.
- *Banque de VERGERS DE LA PASSAIS (0,25 pt).* Les emprunts (2 600 000 €) restent à VERGERS DE LA PASSAIS, dont les capitaux propres sont inchangés : le rapport des emprunts aux capitaux propres reste de 0,48. Mais le site de Flers, la ligne, les stocks et les créances des jus, qui pouvaient garantir ces emprunts, sont remplacés par des titres de participation, et les flux de la branche ne remonteront plus que sous forme de dividendes ; le bénéfice de 2027 comprend 366 000 € de produits sans trésorerie. La banque appréciera la capacité de remboursement sur les seuls flux des cidres et sur les dividendes de JUS DU BOCAGE.

---

### Réponses tolérées
- **2.1 a** : toute formulation qui distingue la rémunération en actions (et non en numéraire) et l'existence d'une activité et d'un associé minoritaire chez la bénéficiaire.
- **2.1 b** : valeur fiscale des actions égale à 1 785 000 €, si le principe de la valeur fiscale des biens apportés est énoncé : 0,25 pt de moins sur le dernier item seulement ; en droit commun, imposition de l'écart entre valeur réelle et valeur comptable (1 415 000 €) si la cessation partielle d'entreprise est indiquée.
- **2.2** : sens de l'opération non traité, si la règle de la valeur comptable sous contrôle commun « quel que soit le sens » est énoncée : 0,25 pt de moins.
- **2.3 a** : actif net apporté diminué des amortissements dérogatoires et de la subvention (1 419 000 €), avec ces éléments repris directement dans l'écriture de réalisation des apports et une prime de 419 000 € sans reconstitution ultérieure, si la méthode est cohérente dans tout le dossier [F01 § 8, réponse tolérée] ; l'item « amortissements dérogatoires et subvention » est alors compté à moitié.
- **2.4 a** : A1 et A2 regroupées (débit direct du compte 261) ; A3 passée en deux écritures, ou avec le compte 7872 ; compte d'apport en 458 ou 4561 si les deux écritures le soldent ; dettes sociales ventilées entre 421 et 431.
- **2.4 b** : réalisation des apports passée par masses, dès lors que les valeurs brutes, les amortissements et les dépréciations sont distingués.
- **2.4 c** : subvention reconstituée pour son montant net (crédit du compte 131 pour 180 000 €, sans mouvement du compte 139), si le prélèvement sur la prime (180 000 €) est juste : 0,25 pt de moins sur l'écriture ; frais en deux écritures ou passés par 6226 puis portés sur la prime.
- **2.5** : toute présentation chiffrée et cohérente.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime d'apport mal calculée : sur la valeur d'échange (3 200 000 – 1 000 000 = 2 200 000 €), ou sur l'actif net diminué des dérogatoires et de la subvention alors que ceux-ci sont ensuite reconstitués (double imputation).
- `JUR-R03` Reconstitution des amortissements dérogatoires et de la subvention oubliée : prime laissée à 761 000 € après les seuls frais, provisions réglementées absentes du bilan de JUS DU BOCAGE.
- `JUR-R05` Difficulté à s'adapter : valeur réelle retenue au motif que JUS DU BOCAGE a un associé minoritaire ; nombre d'actions calculé sur l'actif net comptable (27 891 actions) ; plus-value d'apport de 1 415 000 € constatée chez VERGERS DE LA PASSAIS ; amortissements dérogatoires et subvention laissés dans les capitaux propres de VERGERS DE LA PASSAIS.
- `JUR-F07` Annexes mal exploitées : terrain voisin compris dans l'apport ; quote-part de subvention de 2027 calculée sur douze mois (30 000 €) ; frais imputés pour leur montant brut (prime finale 387 000 €) ; dette de 42 000 € laissée au bilan de JUS DU BOCAGE ; dépréciations des stocks et des clients compensées avec les valeurs brutes.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1 et A5.
- `JUR-F06` Hypothèses non écrites (montant brut ou net de la subvention reconstituée, frais nets d'impôt).
- Erreurs propres à ce cas : régime de faveur subordonné à un engagement de conservation des actions reçues ; apport qualifié « à l'endroit » parce que VERGERS DE LA PASSAIS contrôlait déjà JUS DU BOCAGE ; reprise des dérogatoires et de la subvention chez VERGERS DE LA PASSAIS déclarée imposable malgré les engagements et l'option du traité ; autonomie de la branche justifiée par les services administratifs de JUS DU BOCAGE.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 710-1, 710-2, 720-1, 740-1 | Apport partiel d'actif d'une branche autonome, champ du titre VII, inscription des apports, rémunération indépendante de leur évaluation | [V] p. 81-82 | F01 § 1 |
| PCG art. 741-1, 741-2, 742-2, 743-1, 743-3 | Contrôle commun, apport à l'envers, valeur comptable, exception de l'actif net insuffisant | [V] p. 82-85 | F01 § 2 |
| PCG art. 744-2 ; BOI-IS-FUS-30-20 § 10 | Reprise des valeurs comptables, valeurs d'origine, amortissements et dépréciations | [V] p. 85 ; BOFiP | F01 § 3.2 |
| PCG art. 1212-26 | Titres de participation inscrits pour la valeur d'apport chez l'apporteuse | [V] p. 160 | F01 § 9 |
| PCG art. 214-8, 313-1 ; corrigé du sujet zéro | Provisions réglementées en capitaux propres, comprises dans l'actif net apporté ; reconstitution par prélèvement sur la prime | [V] p. 24 et 32 ; p. imprimée 217 | F01 § 8 |
| Reconstitution de la subvention (1043 / 131, 139) ; reprise en résultat chez l'apporteuse | Écritures | Convention de rédaction ; conséquence directe de la sortie du bien | F01 § 8 ; F02 § 1 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion des créances réciproques | [V] | F01 § 8 |
| CGI art. 210 A, 210 B-1, 210 B-2, 210 B-3, 210 C-1 ; BOI-IS-FUS-20-20 § 10 à 90 ; BOI-IS-FUS-20-40 ; BOI-IS-FUS-20-40-30 § 100 et 110 | Branche complète, régime de plein droit sans engagement de conservation, agrément, effets chez l'apporteuse, valeur fiscale des titres reçus | [V] | F02 § 1, § 2 et § 4 |
| CGI art. 42 septies, 1, al. 5 ; BOI-IS-FUS-10-20-40-10 § 180 | Option dans l'acte d'apport : solde de la subvention rapporté aux résultats de la bénéficiaire selon le plan d'amortissement | [V] CGI lu le 16/11/2026 | F02 § 1 ; F01 § 8 |
| BOI-IS-FUS-30-20 § 10 à 40 | Reprise des dérogatoires déduite si reconstitués chez la bénéficiaire ; rémunération sur les valeurs réelles | [V] BOFiP relu le 16/11/2026 | F02 § 1 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Commissaire aux comptes d'un groupement d'intérêt économique : obligation, durée du mandat, fin de l'obligation ; H2A, CNCC, compagnies régionales, ordre des experts-comptables ; contrôle d'activité | `3.1.b` Nomination et cessation ; `3.1.a` Cadres d'exercice professionnel | 3,5 |
| 3.2 Mission demandée par un membre contre le groupement : impartialité, conflit d'intérêts, secret | `3.1.c` Principes déontologiques | 1,5 |
| 3.3 Objectif de la certification, assurance raisonnable et fraude ; mission d'enquête | `3.2.a` Notion d'audit et typologie des missions | 1,5 |
| 3.4 Extrait de la NEP fraudes, facteurs de risque ; risque du cycle trésorerie et assertions ; procédures | `3.1.d` Référentiel normatif (NEP) ; `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit | 6 |
| 3.5 Refus de communication, d'entretien et de confirmation | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.6 Détournement comptabilisé comme règlement, créance non acquise, écriture, annexe, opinion selon les corrections, parties du rapport | `3.2.e` Portée des opinions | 2,5 |
| 3.7 Responsabilités civile, pénale et disciplinaire | `3.1.e` Mise en cause de la responsabilité | 1,5 |
| 3.8 Informations spécifiques à l'entité ; étendue et limites d'un état volontaire ; part durable du chiffre d'affaires et des investissements | `3.3.a` Contexte et architecture des normes de durabilité | 2,5 |
| 3.9 Informations connectées : connexions directes et indirectes, cohérence des hypothèses | `3.3.b` Principes de construction du reporting | 3,5 |
| 3.10 Objectifs de la mission, assurance limitée, axes ; procédures sur les informations connectées | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4 |
| 3.11 Avis sur les informations : conformité avec ou sans réserve ; structure du rapport | `3.4.c` Portée des avis | 2 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Commissaire aux comptes du groupement et acteurs de la profession (3,5 pts)

**a. Obligation de désignation, durée du mandat et fin de l'obligation (2 pts)**
- **Règle (0,75 pt)** : dans un groupement d'intérêt économique, le contrôle des comptes est en principe exercé dans les conditions prévues par le contrat constitutif. Il doit être exercé par un ou plusieurs **commissaires aux comptes**, choisis sur la liste de la H2A et nommés **par l'assemblée pour six exercices**, dans les groupements qui émettent des obligations et dans ceux qui comptent **cent salariés ou plus à la clôture d'un exercice**. Les règles applicables aux commissaires aux comptes des sociétés anonymes (incompatibilités, pouvoirs, fonctions, obligations, responsabilité, récusation, révocation, rémunération) s'appliquent [V L. 251-12 al. 1 et 3].
- **Application (0,5 pt)** : le texte retient l'effectif **présent à la clôture**, et non l'effectif moyen. Le groupement comptait 94 salariés au 31/12/2023, puis **112 au 31/12/2024** : l'obligation est née à la clôture de 2024, et l'assemblée du 12/06/2025 devait désigner un commissaire aux comptes. L'effectif moyen de 98 personnes en 2024 est sans incidence [S, lecture du texte]. Le contrat constitutif, muet sur le contrôle des comptes, n'y change rien.
- **Durée et fin anticipée (0,25 pt)** : le mandat couvre les exercices **2025 à 2030**. Les fonctions expirent après l'assemblée qui statue sur les comptes de 2030, en 2031 [V L. 251-12 al. 3 ; L. 821-44 al. 1]. Le passage sous cent salariés en cours de mandat n'y met pas fin. Les membres ne peuvent pas révoquer le cabinet à leur gré : le commissaire aux comptes n'est relevé de ses fonctions que **par décision de justice**, en cas de faute ou d'empêchement [V L. 821-50]. La proposition de mettre fin au mandat en 2028 n'est donc pas réalisable.
- **Fin de l'obligation (0,5 pt)** : le groupement cesse d'être tenu de désigner un commissaire aux comptes dès lors qu'il compte **moins de cent salariés pendant les deux exercices précédant l'expiration du mandat** [V R. 251-1], soit 2029 et 2030 [S, application]. Avec 96 salariés fin 2029 et 94 fin 2030, l'obligation prendrait fin à l'expiration du mandat, en 2031 : l'assemblée pourrait ne pas renouveler le cabinet, ou désigner volontairement un commissaire aux comptes ; le contrôle des comptes relèverait alors du contrat constitutif [S]. Si l'effectif atteignait de nouveau cent salariés à la clôture de 2029 ou de 2030, un nouveau mandat de six exercices s'imposerait [S].

**b. Acteurs de la profession et contrôle annoncé (1,5 pt)**
- **H2A (0,5 pt)** : autorité publique indépendante. Elle inscrit les commissaires aux comptes et les auditeurs des informations en matière de durabilité et tient leurs listes. Elle **adopte les normes** de déontologie et d'exercice professionnel, homologuées ensuite par arrêté du garde des sceaux après avis de la CNCC sur les projets. Elle définit les orientations de la formation continue, le **cadre et les orientations des contrôles**, qu'elle réalise directement ou par délégation. Elle diligente les **enquêtes** et prononce les **sanctions** [V L. 820-1 I-II ; L. 820-23 IV-V].
- **CNCC et compagnies régionales (0,5 pt)** : la CNCC, établissement d'utilité publique placé auprès du garde des sceaux, **représente la profession** auprès des pouvoirs publics. Elle concourt au bon exercice de la profession, à sa surveillance et à la défense de l'honneur et de l'indépendance de ses membres [V L. 821-12]. Une **compagnie régionale** est désignée par ressort de cour d'appel, ici celle de Caen [V L. 821-12]. Le commissaire aux comptes y est rattaché et lui notifie ses nominations ; son président concilie les litiges sur les honoraires [V R. 821-44, D. 821-173, R. 821-196].
- **Ordre des experts-comptables (0,25 pt)** : le conseil national et les conseils régionaux de l'ordre tiennent le tableau et surveillent l'exercice de la profession d'**expert-comptable** [V ord. 45-2138 art. 1, 28, 31, 40]. Ils interviennent pour l'activité d'expertise comptable du cabinet, et non pour son mandat auprès du groupement.
- **Contrôle annoncé (0,25 pt)** : c'est un contrôle de l'**activité professionnelle du cabinet**, et non du groupement. Pour un commissaire aux comptes sans mandat d'entité d'intérêt public, il peut être réalisé par des contrôleurs de la H2A ou **délégué à la CNCC** par une convention homologuée, comme ici [V L. 820-14]. Les contrôleurs examineront le dossier de travail du cabinet sur les comptes de 2025 ; le groupement n'a pas de démarche à accomplir [S].

**Réponses tolérées**
- En a., l'identification des deux exercices précédant l'expiration comme 2029 et 2030, ou une formulation équivalente (« les deux derniers exercices du mandat »).
- En b., la présentation du conseil régional de l'ordre de Normandie, sans organisation détaillée.

**Erreurs fréquentes**
- Appliquer au groupement les seuils de bilan, de chiffre d'affaires et d'effectif moyen des sociétés commerciales, ou raisonner sur l'effectif moyen (`JUR-A05`).
- Croire que l'assemblée peut révoquer le cabinet, ou que le mandat prend fin dès que l'effectif repasse sous cent salariés (`JUR-A01`).
- Décrire l'organisation interne et les élections des instances, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 251-12 al. 1 et 3 ; R. 251-1 | Contrôle des comptes du groupement ; cent salariés à la clôture ; six exercices ; fin de l'obligation | [V] ; application : [S] | F09 § 16 |
| C. com. L. 821-44, L. 821-50 | Expiration des fonctions ; relèvement judiciaire | [V] | F09 § 3.5, § 3.7 |
| C. com. L. 820-1, L. 820-14, L. 820-23, L. 821-12 ; R. 821-44, D. 821-173, R. 821-196 ; ord. 45-2138 | Rôles de la H2A, de la CNCC, des compagnies régionales et de l'ordre ; contrôle délégué | [V] | F09 § 3.2, § 2.2, § 16 ; F11 § 3.2 |

### 3.2 Demande de la SAS ROUVELIN Agricole (1,5 pt)

- **Qualification (0,5 pt)** : la mission demandée est une **prestation** pour un membre, dirigée contre le groupement, entité dont le cabinet certifie les comptes, et contre son directeur. Le commissaire aux comptes conserve en toutes circonstances une attitude **impartiale**, sans préjugé ni parti pris [V code de déontologie art. 4]. Il doit être indépendant et éviter toute situation qui pourrait être **perçue** comme de nature à compromettre l'exercice impartial de sa mission ; ses conclusions doivent être exemptes de tout **conflit d'intérêts** [V code de déontologie art. 5 I-II]. Un tiers objectif, raisonnable et informé douterait de l'impartialité d'un cabinet qui chiffre, pour un membre, la perte qu'il audite, et qui prépare sa réclamation contre l'entité qu'il certifie [V A. 821-55 § 03, § 11 ; S, application].
- **Secret professionnel (0,25 pt)** : le cabinet ne peut pas utiliser, au profit d'un membre, les documents obtenus pendant l'audit. Il est tenu au secret pour les faits et renseignements connus dans l'exercice de sa profession, et aucune levée du secret ne vise un membre du groupement [V L. 821-35 al. 1 ; code de déontologie art. 9]. Les membres sont informés par le rapport du cabinet à l'assemblée.
- **Absence de sauvegarde (0,5 pt)** : avant toute nouvelle prestation, le cabinet vérifie qu'il pourra la réaliser et poursuivre sa mission en toute indépendance et impartialité. Face à une situation à risque, il recherche une mesure de sauvegarde ; à défaut, il n'accepte pas la prestation [V A. 821-55 § 15, § 23-30 ; code de déontologie art. 5 III, art. 19 I]. Aucune mesure (équipe distincte, par exemple) ne supprime l'apparence de parti pris dans un différend entre l'entité et l'un de ses membres. L'expert-comptable, de son côté, ne doit jamais se trouver en situation de conflit d'intérêts [V décret 2012-432 art. 145]. Le cabinet doit **refuser**.
- **Réponse au membre (0,25 pt)** : refus motivé par l'indépendance et le secret, sans communication d'information. La société peut s'adresser à un autre expert-comptable ou à un avocat. L'enquête que l'assemblée envisage de confier à un autre cabinet est la voie adaptée.

**Réponses tolérées**
- Une analyse en termes de risque d'autorévision (le cabinet se prononcerait sur un montant qu'il a lui-même chiffré), si elle conclut au refus.

**Erreurs fréquentes**
- Accepter la mission en invoquant la seule casquette d'expert-comptable du cabinet, ou confondre l'indépendance du commissaire aux comptes et celle de l'expert-comptable (`JUR-A03`).
- Oublier le secret professionnel (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 4, 5, 9, 19 ; A. 821-55 § 03, § 11, § 15, § 23-30 | Impartialité, indépendance en apparence, conflit d'intérêts, sauvegardes | [V] ; application : [S] | F10 § 2.1, § 12, § 13 |
| C. com. L. 821-35 al. 1 ; décret 2012-432 art. 145 | Secret professionnel ; conflit d'intérêts de l'expert-comptable | [V] | F10 § 2.2, § 7 ; F09 § 14 |

### 3.3 Certification, fraude et mission d'enquête (1,5 pt)

- **Objectif de la certification (0,5 pt)** : le commissaire aux comptes certifie, en justifiant de ses appréciations, que les comptes annuels sont **réguliers et sincères et donnent une image fidèle** du résultat, de la situation financière et du patrimoine. Il exprime une **opinion** après avoir conduit un audit des comptes [V L. 821-53 al. 1 ; NEP principes § 01]. La certification ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].
- **Assurance raisonnable et fraude (0,5 pt)** : l'audit procure une **assurance raisonnable**, élevée mais non absolue, que les comptes **pris dans leur ensemble** ne comportent pas d'anomalies significatives, qu'elles résultent d'erreurs ou de fraudes. Ses limites tiennent aux sondages, aux limites des procédures de l'entité et à des éléments qui conduisent davantage à des présomptions qu'à des certitudes [V NEP principes § 08-09]. Le risque de ne pas détecter une fraude est plus élevé, car elle s'accompagne de procédés de **dissimulation** [V NEP fraudes § 05]. La prévention et la détection des fraudes incombent à la direction, responsable des procédures de l'entité et de la préparation des comptes [V NEP fraudes § 13]. La certification n'est donc pas une garantie : le cabinet avait d'ailleurs signalé, le 26/10/2026, la faiblesse exploitée par les escrocs [S].
- **Mission d'enquête (0,5 pt)** : c'est une **mission contractuelle** confiée par les membres à un autre professionnel. Son objet est fixé par le contrat : reconstituer les opérations, identifier les défaillances et les responsabilités, recommander. Elle porte sur un champ limité, examiné de manière approfondie, et non sur les comptes pris dans leur ensemble. Elle n'aboutit à aucune opinion sur les comptes, et son rapport est remis aux seuls membres. Confiée à un commissaire aux comptes, ce serait une **prestation** et non une mission légale [V L. 821-2 III-IV ; A. 821-55 § 08 ; S pour la description]. Elle complète la certification sans la remplacer.

**Erreurs fréquentes**
- Présenter l'assurance raisonnable comme une garantie d'absence de fraude, ou confondre audit légal et audit contractuel (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-55 ; NEP principes § 01, § 08-09 | Objectif, assurance raisonnable, limites | [V] | F11 § 1.1 |
| NEP fraudes § 05, § 13 ; L. 821-2 III-IV ; A. 821-55 § 08 | Dissimulation ; responsabilité de la direction ; mission et prestation ; audit contractuel | [V] ; description de l'enquête : [S] | F11 § 1.2, § 13.2, § 20.1 |

### 3.4 Risque de fraude, risque du cycle trésorerie et procédures (6 pts)

**a. Diligences imposées par la norme et facteurs de risque de fraude (2 pts)**
- **Diligences (1 pt ; 0,25 pt par groupe de diligences appliqué au cas, dans la limite de 1 pt)** [V NEP fraudes § 01-28] :
  - **esprit critique** et **échanges au sein de l'équipe** sur les éléments exposés à la fraude : ici, les paiements des fournisseurs et le fichier des fournisseurs ;
  - **demandes d'information** auprès du directeur, de Mme GOUPIL et de l'assemblée sur le risque de fraude et sur les fraudes connues ; **analyse des facteurs** de risque ; **évaluation des contrôles** de l'entité relatifs au risque identifié (modification des coordonnées bancaires, validation des virements) ;
  - **réponses générales** : équipe expérimentée et supervision renforcée, **élément d'imprévisibilité** ; **procédures complémentaires** au niveau des assertions ; **contrôle des écritures** (journaux de banque) et des opérations inhabituelles ;
  - **réévaluation** en fin de mission, **déclarations écrites** de la direction sur la fraude de 2026 et sur l'absence d'autres fraudes connues, **communication** de la fraude au directeur et à l'assemblée des membres.
- **Facteurs de risque (1 pt ; 0,25 pt par facteur rattaché aux faits, dans la limite de 1 pt)** : la norme distingue les **incitations ou pressions** et les **opportunités** [V NEP fraudes § 09, § 16] ; la doctrine ajoute la **justification** de l'acte (triangle de la fraude) [S].
  - Pressions : rémunération variable du directeur liée aux escomptes, exigence des membres sur les escomptes, qui incitent à payer vite et à contourner les vérifications ; charge de travail de Mme GOUPIL, arrivée en septembre avec un retard de saisie.
  - Opportunités : modification des coordonnées bancaires par une seule personne, **sans contre-appel ni validation** ; validation des virements par le directeur sans voir le compte du bénéficiaire ; journal des modifications jamais consulté ; rapprochements bancaires établis par la même personne, en retard et rarement revus ; écritures manuelles passées par elle ; volume des paiements centralisés (41 380 000 € en 1 840 virements).
  - Changements : départ du comptable expérimenté après deux semaines de passation ; recommandation du cabinet du 26/10/2026 reportée à 2027.
  - Attitude de la direction : volonté de minimiser la fraude (refus de communication, créance sur l'assureur, annexe muette), à prendre en compte au titre de la justification [S].

**b. Risque d'anomalies significatives du cycle trésorerie (1,5 pt)**
- **Risque inhérent élevé (0,5 pt)** : les disponibilités et les paiements sont, par nature, exposés au détournement ; volume et montants élevés ; changements de personnel et de procédure ; fraude **réalisée** en 2026, qui fait craindre d'autres modifications frauduleuses ; pression des escomptes [V NEP risques § 02 ; S, application].
- **Risque lié au contrôle élevé (0,25 pt)** : les faiblesses relevées ci-dessus ne sont compensées par aucun contrôle, et la recommandation du cabinet n'est pas mise en œuvre. Le cabinet ne peut pas s'appuyer sur ces contrôles : il met en œuvre des **procédures de substance étendues** [V NEP principes § 13].
- **Principaux risques et assertions (0,75 pt ; 0,25 pt par risque rattaché à la bonne assertion, dans la limite de 0,75 pt)** :

| Risque | Assertion | Lien avec les annexes |
|---|---|---|
| Virements détournés enregistrés comme règlements des fournisseurs | **Réalité** et **classification** des règlements (flux) ; **exhaustivité** et **droits et obligations** des dettes fournisseurs (soldes) | Débit du compte 4011 alors que HYDRALIS et PNEUMAGRI n'ont rien reçu |
| Autres modifications frauduleuses, autres paiements à des tiers | **Réalité** des paiements | 23 modifications non revues |
| Soldes bancaires faussés ou suspens masqués par des écritures manuelles | **Existence** et **exhaustivité** de la trésorerie | Rapprochements tardifs, passés par la même personne |
| Dettes ou paiements mal rattachés à l'exercice | **Séparation des exercices** | Rapprochement de novembre établi en janvier |
| Créance sur l'assureur inscrite sans garantie acquise | **Existence**, **droits et obligations** (soldes) | Position du directeur ; courrier de l'assureur |
| Fraude et sinistre non décrits dans l'annexe | Présentation : **exhaustivité**, **présentation et intelligibilité** | Projet d'annexe muet |

**c. Procédures (2,5 pts ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 2,5 pts)**
- **Confirmation directe des deux banques**, envoyée et reçue par le cabinet : soldes des trois comptes, comptes ouverts ou clos dans l'exercice, personnes habilitées (existence, exhaustivité, droits et obligations) [V NEP confirmations § 5, § 9].
- **Rapprochements bancaires au 31/12/2026** : vérification, examen des suspens et de leur dénouement en janvier 2027 (existence, exhaustivité, séparation des exercices).
- **Revue des 23 modifications de coordonnées bancaires de 2026**, à partir du journal du progiciel : justificatifs, appel du cabinet à un interlocuteur connu de chaque fournisseur ou confirmation écrite (réalité des paiements ultérieurs).
- **Contrôle des paiements d'octobre 2026 à la date des travaux** : comparaison du compte bénéficiaire porté sur les relevés bancaires avec les coordonnées vérifiées du fournisseur (réalité, classification).
- **Demandes de confirmation des soldes fournisseurs**, ouvertes, auprès d'HYDRALIS, de PNEUMAGRI et des principaux fournisseurs (exhaustivité, droits et obligations des dettes).
- **Recherche de dettes non comptabilisées** : relances et factures reçues après la clôture, paiements de 2027 (exhaustivité, séparation des exercices).
- **Test des écritures manuelles** des journaux de banque et des écritures d'inventaire, sélectionnées selon des critères de risque (auteur, date, montant, comptes inhabituels) [V NEP fraudes § 22].
- **Élément d'imprévisibilité** : sondage sur des paiements ou des fournisseurs non testés lors de l'intervention intermédiaire, contrôle à une date non annoncée [V NEP fraudes § 20].
- **Inspection du rapport interne, du dossier de sinistre et confirmation de l'assureur** : chiffrage de la perte, état de la garantie (existence et droits de la créance revendiquée ; information de l'annexe).
- **Entretiens** avec Mme GOUPIL, le directeur et d'autres salariés sur d'éventuelles autres fraudes [V NEP fraudes § 13-14].
- **Déclarations écrites** de la direction et **lecture du projet d'annexe** (présentation) [V NEP fraudes § 27].

**Réponses tolérées**
- En a., la présentation du triangle « pression, occasion, justification » comme cadre d'analyse, si les facteurs sont rattachés aux faits.
- En c., des tests sur l'efficacité des contrôles, s'ils sont présentés comme sans objet en 2026 (contrôles absents) et prévus après la mise en place du contre-appel.

**Erreurs fréquentes**
- Réciter l'extrait de norme sans l'appliquer aux faits (`JUR-A06`).
- Confondre réalité (flux) et existence (solde), ou omettre l'exhaustivité des dettes fournisseurs (`JUR-A01`).
- Proposer des procédures sans objectif ni assertion (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP fraudes § 01-28 | Objet, dissimulation, échanges, demandes d'information, facteurs, réponses, écritures, déclarations, communication | [V] ; triangle de la fraude : [S] | F11 § 20.1 |
| NEP principes § 11-13 ; NEP risques § 02 | Risque inhérent, risque lié au contrôle ; facteurs | [V] ; application : [S] | F11 § 4.1 |
| NEP éléments probants § 9-10 ; NEP confirmations § 5, § 9 | Assertions ; techniques ; confirmation | [V] | F11 § 4.3, § 6.2-6.3 |

### 3.5 Refus du directeur et moyens d'action du commissaire aux comptes (1,5 pt)

- **Droit de communication (0,5 pt)** : les pouvoirs du commissaire aux comptes des sociétés anonymes s'appliquent au groupement [V L. 251-12 al. 3]. Le cabinet se fait communiquer **sur place toutes les pièces qu'il estime utiles** [V L. 821-60]. C'est lui qui apprécie l'utilité, et non le directeur : le rapport interne et la correspondance avec l'assureur servent à chiffrer la perte, à apprécier la créance revendiquée et à rechercher d'autres fraudes. Le secret professionnel ne peut lui être opposé, sauf par les auxiliaires de justice [V L. 821-61 al. 3]. Le secret des affaires ne lui est pas opposable, et le cabinet est lui-même tenu au secret [V L. 821-35 al. 1].
- **Entretiens et confirmations (0,5 pt)** : le cabinet opère à toute époque les vérifications et contrôles qu'il juge opportuns [V L. 821-60]. La norme lui impose d'interroger, outre la direction, les autres personnes de l'entité qu'il estime utile d'interroger sur les fraudes [V NEP fraudes § 14] : l'entretien avec Mme GOUPIL ne peut lui être refusé. Il peut recueillir des informations auprès des tiers qui ont accompli des opérations pour le compte du groupement, comme les banques, qui tiennent ses comptes et exécutent ses virements [V L. 821-61 al. 2]. Les fournisseurs et l'assureur, qui contractent avec le groupement, ne sont pas dans ce cas : pour eux, la demande de confirmation relève de la norme, et non d'un droit légal. C'est une technique que le cabinet maîtrise : si la direction s'y oppose, il examine si ses motifs sont valables et collecte des éléments à ce sujet ; à défaut, il en tire les conséquences dans son rapport [V NEP confirmations § 9-12]. Vouloir rester le seul interlocuteur n'est pas un motif fondé.
- **Maintien du refus (0,5 pt)** : délit d'obstacle (cinq ans, 75 000 €) pour le dirigeant qui fait obstacle aux vérifications ou refuse la communication sur place des pièces utiles [V L. 821-6 3°]. Sur l'opinion : **limitation**, qui conduit à une réserve pour limitation si ses incidences sont circonscrites, sinon à une **impossibilité de certifier** [V NEP rapport § 11, § 14]. Le cabinet porte la difficulté à la connaissance de l'assemblée des membres, comme l'a fait Mme GRANDVAL (annexe 3.7) [S].

**Erreurs fréquentes**
- Admettre que la confidentialité ou le secret des affaires justifie le refus (`JUR-A01`).
- Oublier la conséquence sur l'opinion (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 251-12 al. 3, L. 821-60, L. 821-61, L. 821-35 al. 1, L. 821-6 3° | Pouvoirs ; communication ; tiers ; secret ; obstacle | [V] | F09 § 5, § 14, § 16 ; F11 § 2, § 13.3 |
| NEP fraudes § 14 ; NEP confirmations § 9-12 ; NEP rapport § 11, § 14 | Entretiens ; refus de confirmation ; limitation | [V] | F11 § 6.3, § 8.1, § 20.1 |

### 3.6 Anomalies et opinion sur les comptes annuels de 2026 (2,5 pts)

**Anomalies et caractère significatif (1 pt)**
- **Dettes non comptabilisées (0,25 pt)** : les deux virements ont bénéficié aux escrocs. HYDRALIS et PNEUMAGRI n'ont pas été payées et le groupement leur doit toujours 186 400 + 143 600 = **330 000 €**. Le passif existe à la clôture : il doit être comptabilisé [V L. 123-20 ; PCG art. 513-4]. Les dettes fournisseurs sont sous-évaluées et le résultat surévalué de 330 000 €.
- **Caractère significatif (0,25 pt)** : 330 000 / 230 000 = **1,43 fois** le seuil de signification. L'anomalie est significative par son montant, et aussi par sa **nature** : un détournement d'actifs, qui intéresse directement les membres qui supportent la perte [V NEP caractère significatif § 9 ; NEP anomalies § 14].
- **Créance sur l'assureur (0,25 pt)** : le groupement ne contrôle aucune ressource. La garantie est subordonnée à un contre-appel qui n'a pas été fait, et l'assureur indique qu'aucune indemnité n'est acquise. Ce n'est pas un actif, et l'indemnité n'est pas un bénéfice réalisé à la clôture [V PCG art. 211-1, 513-3 ; L. 123-21]. Inscrite, cette créance de 300 000 € (1,30 fois le seuil) serait une anomalie significative ; cumulée avec les autres anomalies non corrigées, elle atteindrait 346 000 €.
- **Annexe (0,25 pt)** : l'omission de toute information sur la fraude et sur le sinistre est une anomalie d'information significative [V PCG art. 831-1 5° ; NEP caractère significatif § 9].

**Écriture de correction (0,5 pt)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 678 | Autres charges exceptionnelles | 330 000 | |
| | 4011 | Fournisseurs - Achats de biens et prestations de services | | 330 000 |

Libellé : rétablissement des dettes envers HYDRALIS (186 400 €) et PNEUMAGRI (143 600 €), réglées par les virements détournés (écriture X1, équilibrée). Le classement en résultat exceptionnel suit la convention de l'annexe 3.7. Le résultat corrigé est une perte de 41 000 − 330 000 = **289 000 €**, soit 72 250 € pour chaque membre.

**Information dans l'annexe (0,25 pt)** : une note décrit la fraude (modification frauduleuse des coordonnées bancaires de deux fournisseurs, deux virements), son montant de 330 000 € et son classement en charges exceptionnelles [V PCG art. 832-21]. Elle indique la déclaration de sinistre, la position de l'assureur et l'absence de créance comptabilisée, la garantie n'étant pas acquise, ainsi que les mesures prises sur la procédure de paiement [S]. Une indemnité éventuelle sera un produit de l'exercice où elle sera acquise [S, application de l'art. 513-3].

**Opinion selon les corrections (0,75 pt)**
- **Le groupement accepte les corrections** (écriture X1, aucune créance sur l'assureur, note de l'annexe) (0,25 pt) : il ne subsiste que 46 000 € d'anomalies non corrigées, sous le seuil de signification et sans caractère significatif par leur nature : **certification sans réserve**. Le cabinet les communique à l'administrateur et à l'assemblée et obtient une déclaration écrite à laquelle est joint leur état [V NEP anomalies § 15-17 ; NEP rapport § 08]. Il peut formuler une **observation** qui attire l'attention sur la note relative à la fraude ; elle ne modifie pas l'opinion [V NEP rapport § 07].
- **Le groupement retient la position du directeur** (dettes rétablies, créance de 300 000 € inscrite, annexe muette) (0,25 pt) : les anomalies significatives non corrigées sont la créance de 300 000 €, cumulée avec les 46 000 €, et l'omission d'information. Leurs incidences sont **clairement circonscrites** : une créance identifiée, un résultat qui serait une perte de 289 000 € et non un bénéfice de 11 000 €, une information précise à fournir. Une réserve qui les décrit et les quantifie peut suffire à l'utilisateur : **certification avec réserve pour désaccord** [V NEP rapport § 09-10]. Un **refus de certifier** est également défendable : le signe du résultat que les membres se répartissent s'inverse (bénéfice de 11 000 € au lieu d'une perte de 289 000 €, et même de 335 000 € avec les 46 000 € non corrigés), et l'annexe omet une fraude ; la formulation d'une réserve peut alors être jugée insuffisante pour l'utilisateur [V NEP rapport § 12-13]. Les deux conclusions sont acceptées si elles sont motivées par le critère des incidences circonscrites et de la suffisance de la réserve.
- **Parties du rapport (0,25 pt)** : la partie « **Opinion avec réserve** » indique que, sous cette réserve, le cabinet certifie que les comptes sont réguliers et sincères et donnent une image fidèle. La partie « **Fondement de l'opinion avec réserve** » expose les motifs et quantifie leurs incidences. En cas de refus, les parties « **Refus de certifier** » et « **Fondement du refus de certifier** » sont acceptées. Les motifs sont communiqués au préalable à l'administrateur et à l'assemblée ; le rapport est destiné à l'assemblée des membres [V NEP rapport § 06 ; R. 821-180].

**Réponses tolérées**
- L'utilisation d'un sous-compte de 401 par fournisseur, ou d'un compte de charges d'exploitation si le candidat motive un autre classement que la convention de l'annexe 3.7 (0,25 pt sur 0,5 pour l'écriture).
- Un refus de certifier, dans le second cas, motivé par l'inversion du signe du résultat et par l'omission d'information sur la fraude (insuffisance d'une réserve) : points complets. Une conclusion, réserve ou refus, sans motivation par ces critères : 0,25 pt sur 0,5 pour les deux derniers items.

**Erreurs fréquentes**
- Corriger la trésorerie au lieu des dettes fournisseurs : les fonds sont bien sortis du compte bancaire (`JUR-A01`).
- Inscrire l'indemnité attendue en produit à recevoir au motif que le groupement est assuré (`JUR-A06`).
- Écritures sans libellé ou sans numéro de compte (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 123-20, L. 123-21 ; PCG art. 211-1, 513-3, 513-4, 513-5, 831-1 5°, 832-21 | Passif, actif, bénéfices réalisés, résultat exceptionnel, annexe | [V] ; application : [S] | F11 § 20.2 |
| NEP caractère significatif § 9 ; NEP anomalies § 14-17 | Montant et nature ; cumul ; communication ; déclaration écrite | [V] | F11 § 4.2, § 14.1 |
| NEP rapport § 06-10 ; R. 821-180 | Opinions ; observation ; parties du rapport | [V] | F11 § 8, § 12.2 |

### 3.7 Responsabilités du cabinet et de Mme GRANDVAL (1,5 pt)

**Responsabilité civile (0,75 pt)**
- Les règles de responsabilité du commissaire aux comptes des sociétés anonymes s'appliquent au groupement [V L. 251-12 al. 3]. Le commissaire aux comptes est responsable, envers l'entité **et les tiers**, des conséquences dommageables des **fautes et négligences** commises dans l'exercice de sa profession [V L. 821-37 al. 1]. GRÉVILLON, membre, agit comme tiers. Elle doit prouver une faute, un préjudice et un lien de causalité [S].
- **Faute** : la mission est une obligation de moyens, fondée sur une assurance raisonnable. L'intervention intermédiaire portait sur les paiements de janvier à septembre. Les modifications frauduleuses des 06/10 et 21/10 étaient récentes ou postérieures aux tests, et les virements datent de novembre. Le cabinet a surtout **signalé la faiblesse** et recommandé d'y remédier le 26/10/2026, ce que le directeur a reporté. Aucune faute n'apparaît [S].
- **Préjudice et lien de causalité** : la perte de GRÉVILLON, quart de la perte due à la fraude (330 000 / 4 = 82 500 €), résulte de l'escroquerie et de l'absence de contre-appel que le groupement n'a pas mis en place malgré la recommandation, et non de l'audit [S]. C'est en outre sa quote-part de la perte du groupement : le caractère personnel de ce préjudice, distinct de celui du groupement, serait discuté [S].
- Conclusion : risque faible. Le cabinet est couvert par l'assurance obligatoire des commissaires aux comptes [V R. 821-85].

**Responsabilité pénale (0,5 pt)**
- Le délit visé par GRÉVILLON est le fait, pour un commissaire aux comptes, de **donner ou de confirmer des informations mensongères** sur la situation de la personne morale (cinq ans, 75 000 €) [V L. 821-9]. C'est un délit intentionnel [S].
- Le seul rapport émis, sur les comptes de 2025, date du 05/05/2026, avant la fraude ; le cabinet n'a encore rien certifié sur 2026 ; son silence n'est pas une information mensongère. Le délit n'est pas constitué [S].

**Responsabilité disciplinaire (0,25 pt)**
- La H2A sanctionne les manquements aux conditions légales d'exercice, la **négligence grave** et les faits contraires à la probité ou à l'honneur, de l'avertissement à la radiation, avec d'éventuelles sanctions pécuniaires [V L. 821-70 I, L. 821-71]. Cette responsabilité est indépendante de l'action civile. Les diligences et la recommandation du cabinet excluent ici une négligence grave [S].

**Réponses tolérées**
- Une réponse qui retient la responsabilité contractuelle du cabinet envers le groupement et délictuelle envers le membre, si les trois conditions sont analysées.

**Erreurs fréquentes**
- Confondre les trois responsabilités et leurs sanctions (`JUR-A01`).
- Présenter l'audit comme une obligation de résultat de découvrir toute fraude (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 251-12 al. 3, L. 821-37 ; R. 821-85 | Responsabilité civile ; assurance | [V] ; conditions : [S] | F09 § 7.1, § 13, § 16 |
| C. com. L. 821-9 | Informations mensongères | [V] ; élément intentionnel : [S] | F09 § 7.3 |
| C. com. L. 821-70 I, L. 821-71 | Faute disciplinaire ; sanctions | [V] | F09 § 7.2 |

---

### Partie B – Durabilité (12 points)

### 3.8 Indicateur spécifique, étendue des informations et part durable du chiffre d'affaires (2,5 pts)

**Informations spécifiques à l'entité (1,25 pt)**
- **Règle (0,5 pt)** : si un thème lié à des impacts, risques et opportunités matériels n'est pas couvert, ou pas assez, par une norme ESRS, l'entreprise fournit des **informations spécifiques à l'entité**, qui respectent les exigences d'image fidèle [V ESRS 1 (2026) § 11]. Elle tient compte de leur **comparabilité dans le temps** et avec les entreprises du même secteur [V § 12]. Ces informations présentent les caractéristiques qualitatives de l'appendice B [V AR 3]. Un indicateur spécifique doit être **pertinent** pour un impact, un risque ou une opportunité matériel. Sa mesure doit être une **représentation fidèle**, fondée sur des informations et des hypothèses raisonnables, justifiables et **vérifiables**, et il doit être accompagné d'**informations contextuelles suffisantes** [V AR 4].
- **Appréciation de l'indicateur proposé (0,5 pt)** : le reconditionnement relève d'un thème que le groupement juge matériel (économie circulaire : impact positif et opportunité). L'indicateur est donc pertinent, et sa publication est permise, voire attendue [S]. En revanche, le publier seul, sans définition, ni périmètre, ni source des données, ne permet ni de le comprendre ni de le vérifier : la proposition du directeur ne respecte pas l'AR 4. La première publication n'impose pas de comparatif [V § 87 b)], mais le chiffre de 2025 (11,8 %), établi selon la même définition, sert la comparabilité dans le temps [S].
- **Conclusion (0,25 pt)** : indicateur admis s'il est présenté avec sa définition (nombre de pièces reconditionnées vendues rapporté au nombre total de pièces vendues), son périmètre et ses sources, dans la partie consacrée à l'économie circulaire, et signalé comme spécifique au groupement [S].

**Étendue et limites des informations publiées (0,75 pt)**
- En déclarant son état conforme aux ESRS, le groupement s'oblige à les appliquer comme un tout : ESRS 1 et ESRS 2, puis, pour chaque thème matériel, les informations requises sur les politiques, les actions, les indicateurs et les cibles, complétées si besoin d'informations spécifiques [V ESRS 1 (2026) § 25, § 29 ; ESRS 2 BP-1]. L'information est **complète et neutre**, sans sélection des seuls aspects favorables [V appendice B, QC6-QC7].
- Limites : il ne publie pas les informations sans importance matérielle, sauf informations supplémentaires signalées comme telles [V § 24, § 107-109] ; une omission n'est admise que dans les cas prévus [V § 100-101]. Le caractère volontaire de la publication ne permet pas une application partielle des ESRS sous la mention « conforme aux ESRS » [S].

**Part durable du chiffre d'affaires et des investissements (0,5 pt)**
- Les informations prévues par l'article 8 du règlement (UE) 2020/852 (part du chiffre d'affaires, des dépenses d'investissement et des dépenses d'exploitation associée à des activités durables sur le plan environnemental) ne s'imposent qu'aux entreprises tenues de publier des informations en matière de durabilité. Elles figurent alors dans leur état de durabilité, sans relever des ESRS [V règl. 2020/852 art. 8 § 1-2 ; ESRS 1 (2026) § 106].
- Le groupement, qui publie volontairement, n'est **pas tenu** de les publier ; l'axe correspondant de la vérification est **sans objet**, ce que traduit la lettre de mission [V F13 § 2.2, § 5 ; S, application]. Publiées volontairement, elles seraient des informations supplémentaires signalées comme telles [S].

**Réponses tolérées**
- La mention de la norme volontaire européenne comme référentiel alternatif, si le candidat ne remet pas en cause le choix des ESRS.

**Erreurs fréquentes**
- Interdire tout indicateur qui n'est pas prévu par une norme, ou au contraire l'admettre sans définition (`JUR-A05`).
- Développer le calendrier de la réglementation européenne ou le calcul de la part durable (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 11-12, AR 2 à AR 5, § 87 b) | Informations spécifiques à l'entité ; comparabilité ; indicateurs ; première publication | [V] ; application : [S] | F12 § 3.3, § 19, § 20 |
| ESRS 1 (2026) § 24-25, § 29, § 100-101, § 106-109, appendice B ; ESRS 2 BP-1 | Étendue, matérialité, omission, informations supplémentaires, neutralité ; déclaration de conformité | [V] | F12 § 5, § 8, § 14, § 17 |
| Règl. (UE) 2020/852 art. 8 | Entreprises concernées ; contenu | [V] | F12 § 9 ; F13 § 5 |

### 3.9 Informations connectées avec les comptes annuels (3,5 pts)

**Exigences des ESRS (1 pt)**
- L'entreprise fournit des informations qui permettent de comprendre les **connexions** au sein de l'état de durabilité et entre cet état et ses autres documents, dont les **états financiers** [V ESRS 1 (2026) § 112].
- **Connexion directe** : un montant présent aussi dans les états financiers est accompagné d'un **renvoi** aux états financiers [V § 114].
- **Connexion indirecte** : un montant qui est la somme ou une partie de montants des états financiers est accompagné d'une **explication du lien** avec les montants les plus pertinents [V § 115].
- **Cohérence** : données et hypothèses concordent, dans la mesure du possible, avec celles des états financiers ; toute **différence significative** d'hypothèses est expliquée [V § 116] ; même monnaie [V AR 50].

**Affirmation sur la fraude (0,75 pt)**
- L'affirmation « aucun incident de fraude » est **contredite par les comptes** : une perte de 330 000 € est comptabilisée en charges exceptionnelles et décrite dans l'annexe. Sur un thème jugé matériel (prévention de la fraude), l'information est inexacte, ni neutre ni complète [V appendice B, QC6-QC7 ; S, application].
- Le groupement décrit l'incident (détournement par modification frauduleuse des coordonnées bancaires de deux fournisseurs), indique son montant avec un **renvoi à la note de l'annexe** (connexion directe), et présente fidèlement les mesures : le directeur avait renvoyé le contre-appel au nouveau progiciel de 2027 ; une mesure non encore mise en œuvre est présentée comme prévue, et non comme réalisée [S].

**Investissements photovoltaïques (1 pt)**
- Les comptes font apparaître, pour 2026, 780 000 € de tranche 1 mise en service et 270 000 € de tranche 2 en cours, soit **1 050 000 €**. Le 1,2 M€ annoncé correspond au budget total, dont **150 000 €** de travaux qui ne seront commandés qu'en 2027 ; l'investissement de 2026 est surévalué de 14,3 % et la toiture n'est pas « entièrement en service » (tranche 2 prévue en juin 2027).
- Le montant de l'état est une somme de deux montants du tableau des immobilisations : c'est une **connexion indirecte**. Le groupement publie 1 050 000 € investis en 2026, explique le lien (780 000 € en immobilisations corporelles, 270 000 € en immobilisations en cours) et présente séparément les 150 000 € prévus pour 2027 [V § 115 ; S, application].

**Durée d'exploitation de l'entrepôt (0,75 pt)**
- Le plan d'action suppose une exploitation jusqu'en **2050**. Les comptes amortissent l'entrepôt et les installations photovoltaïques jusqu'au 31/12/**2035**, en cohérence avec la décision de l'assemblée d'étudier un transfert à cet horizon. L'écart de quinze ans porte sur une hypothèse importante, commune aux deux documents [V § 116 ; S, application].
- Le groupement aligne ses hypothèses ou explique la différence et ses conséquences (bénéfices du plan au-delà de 2035 incertains en cas de transfert) ; le directeur l'accepte (annexe 3.9). L'équipe qui certifie les comptes en est informée : l'écart intéresse aussi les comptes [S].

**Erreurs fréquentes**
- Confondre connexion directe et indirecte, ou se contenter d'un renvoi pour un montant composé (`JUR-A01`).
- Recalculer des émissions évitées ou discuter le plan d'amortissement, ce qui n'est pas demandé (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 112, § 114-116, AR 50 | Informations connectées ; connexions directes et indirectes ; cohérence ; monnaie | [V] ; application : [S] | F12 § 9 |
| ESRS 1 (2026) appendice B, QC6-QC7 | Complétude, neutralité | [V] | F12 § 17 |

### 3.10 Mission, assurance limitée et procédures sur les informations connectées (4 pts)

**a. Réponse au directeur (2 pts)**
- **Objectifs et axes (0,75 pt)** : le cabinet émet un **avis** sur la conformité aux ESRS du **processus** mis en œuvre pour déterminer les informations publiées (analyse de double matérialité) et sur la conformité des **informations** publiées [V L. 821-54 II ; LD 2026 § 2]. La mission est volontaire, conduite dans les conditions de la certification légale (hypothèse) ; le rapport est destiné à l'assemblée des membres. L'axe relatif aux informations de l'article 8 du règlement (UE) 2020/852 est **sans objet**, le groupement n'y étant pas soumis ; le **balisage** n'est pas exigible [V LD 2026 § 2, § 10 ; F13 § 5 ; S, application]. La mission ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].
- **Assurance limitée (0,75 pt)** : les vérifications sont moindres en **nature, étendue et durée** que pour une assurance raisonnable. La conclusion s'exprime sous une **forme négative** : le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes [V LD 2026, « Niveau d'assurance »]. La certification des comptes procure une **assurance raisonnable**, élevée mais non absolue, exprimée sous une **forme positive** [V NEP principes § 08 ; L. 821-53].
- **Les montants communs aux deux documents (0,5 pt)** : la perte et les immobilisations sont couvertes par l'assurance raisonnable de la certification des comptes, comme éléments des comptes pris dans leur ensemble. Reprises dans l'état, elles relèvent de l'avis d'assurance limitée sur les informations : l'état n'est pas « certifié » au niveau des comptes. Le cabinet s'appuie sur les travaux de l'équipe qui certifie les comptes pour vérifier la cohérence [V LD 2026 § 3.2]. Deux missions distinctes donnent deux rapports distincts, avec leur vocabulaire propre : opinion sur les comptes, avis par axe sur la durabilité [V LD 2026 § 17 ; S].

**b. Procédures sur les informations connectées (2 pts ; 0,25 pt par procédure justifiée, dans la limite de 2 pts)**
- **Rapprochement** des 780 000 € et 270 000 € avec le tableau des immobilisations audité, et vérification de l'explication du lien (connexion indirecte).
- **Inspection** du budget approuvé par l'assemblée, du procès-verbal de réception de la tranche 1 et de l'état d'avancement de la tranche 2 : réalité de la mise en service, montant restant à engager.
- **Échanges avec l'équipe qui certifie les comptes** : note de synthèse, écriture X1, note de l'annexe sur la fraude, pour vérifier la description de l'incident et le renvoi [V LD 2026 § 3.2].
- **Demandes d'information et inspection** sur les mesures annoncées (nouveau progiciel, contre-appel) : présentation fidèle des actions réalisées et prévues.
- **Contrôle des hypothèses** : comparaison de la durée de 2050 avec le plan d'amortissement, la décision de l'assemblée du 23/06/2026 et l'explication publiée [V ESRS 1 (2026) § 116].
- **Vérification de la présentation** : renvois, monnaie, cohérence des montants entre les parties de l'état.
- **Lecture d'ensemble** de l'état, du rapport de gestion et des comptes annuels [V LD 2026 § 11].
- **Lettre d'affirmation** couvrant ces informations, et communication des erreurs relevées à l'administrateur et à l'assemblée [V LD 2026 § 4, § 14]. Également admis : contrôle de la définition et des données de l'indicateur de reconditionnement.

**Erreurs fréquentes**
- Affirmer que l'état est certifié avec une assurance raisonnable parce que ses montants viennent des comptes (`JUR-A01`).
- Retenir l'axe relatif à la part durable du chiffre d'affaires pour une publication volontaire (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; LD 2026 § 2, § 10, « Niveau d'assurance » | Objectifs, axes, assurance limitée | [V] ; application à une mission volontaire : [S] | F13 § 2 ; F12 § 11 |
| NEP principes § 08 ; L. 821-53 | Assurance raisonnable | [V] | F11 § 1.1 |
| LD 2026 § 3.2, § 4, § 11, § 14, § 17 | Échanges avec les commissaires aux comptes des comptes ; lettre d'affirmation ; lecture d'ensemble ; communication ; rapport | [V] ; procédures : [S] | F13 § 3, § 4 |

### 3.11 Avis sur les informations publiées et structure du rapport (2 pts)

**Le groupement corrige ses informations (0,5 pt)**
- L'incident est décrit avec son montant et un renvoi à l'annexe ; les investissements de 2026 sont ramenés à 1 050 000 €, avec l'explication du lien et la mention des 150 000 € prévus en 2027 ; la différence de durée est expliquée. Aucune erreur, omission ou incohérence importante ne subsiste : **avis de conformité** sur les informations, comme sur le processus [V LD 2026 § 17].
- Le cabinet peut présenter les informations connectées parmi les **éléments ayant fait l'objet d'une attention particulière**, ou formuler une **observation** sur la première publication de l'indicateur spécifique [V LD 2026 § 17].

**Le groupement ne corrige pas (0,75 pt)**
- L'affirmation sur la fraude, contredite par les comptes, et le montant surévalué des investissements, présentés comme entièrement en service, sont des **erreurs non corrigées** d'une importance telle qu'elles remettent en cause la conformité des informations [V LD 2026 § 17 ; S, qualification].
- Leurs incidences sont **clairement circonscrites** à deux informations identifiées, et la réserve peut indiquer les faits exacts (perte de 330 000 €, investissements de 1 050 000 €) : **avis de conformité assorti de réserves motivées** [V F13 § 4.3].
- Ce n'est pas un avis de non-conformité : le reste de l'état et le processus sont conformes. Ce n'est pas une impossibilité : il n'y a aucune limitation. Une observation ne peut pas remplacer la réserve. Si une seule des deux informations était corrigée, la réserve porterait sur l'autre [S].

**Structure de la partie du rapport (0,75 pt)**
- Le rapport est destiné à l'**assemblée des membres**. Il comprend une partie introductive : qualité du cabinet, informations couvertes, responsabilités respectives, règles déontologiques et lignes directrices appliquées, **limites de la mission** [V LD 2026 § 17].
- Il comporte ensuite **une partie par axe**, ici le processus et les informations. La partie sur les informations présente la **nature des vérifications**, la **conclusion** (avis, et réserves motivées avec leurs motifs), les **observations** éventuelles et les **éléments ayant fait l'objet d'une attention particulière**. Le rapport est daté et signé par Mme GRANDVAL, inscrite sur la liste des commissaires aux comptes habilités à certifier les informations en matière de durabilité [V LD 2026 § 17 ; L. 821-26].

**Réponses tolérées**
- Un avis de non-conformité dans le second cas, s'il est motivé par le caractère sensible de l'affirmation sur la fraude et par l'impossibilité d'en circonscrire les effets, avec application du critère des incidences circonscrites : 0,5 pt sur 0,75.

**Erreurs fréquentes**
- Proposer une observation à la place d'une réserve, ou une non-conformité pour deux erreurs circonscrites (`JUR-A02`).
- Présenter le rapport selon la structure du rapport sur les comptes, sans parties par axe (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 | Avis, réserve, observation, éléments d'attention particulière, structure par axe | [V] ; qualification : [S] | F13 § 4 |
| C. com. L. 821-26 | Signature par l'associé inscrit | [V] | F09 § 4.3 |
