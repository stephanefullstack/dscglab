# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 1 – Gestion juridique, fiscale et sociale — Exercice d'entraînement n° 4 — Dossier 4 (10 points sur 40)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire ; année de référence des faits : exercice 2026 et opérations de 2026.

Bien que le corrigé mentionne des textes juridiques, il n'est pas attendu des candidats qu'ils en citent les références.

**Remarque à l'attention des correcteurs** : la référence aux textes de lois ou articles de codes n'est pas exigée des candidats. Elle est indiquée dans le corrigé à titre informatif. L'évaluation porte avant tout sur la pertinence et la cohérence des éléments de réponse : énoncé de la règle, application aux faits, conclusion.

| Question | Compétence visée | Points |
|---|---|---:|
| 4.1 | `2.2.f` — Constitution et gouvernance des organismes à but non lucratif (fondation d'entreprise, mécénat) | 3 |
| 4.2 | `1.2.e` — Évaluer les dispositifs de lutte contre la corruption ; `1.2.f` — Accompagner leur mise en place | 3 |
| 4.3 | `3.1.a` — Anticiper et organiser la transmission (cession de droits sociaux : plus-value, droits) | 3 |
| 4.4 | `3.1.a` — Transmission (option pour le barème) | 1 |
| **Dossier 4 – Mécénat, conformité et fiscalité du dirigeant** | | **10** |

---

### 4.1 Mécénat en faveur de la fondation d'entreprise (3 points)

**Type de question** : exploitation d'une annexe, calcul de tête et analyse.

| Item | Attendu | Temps | Points |
|---|---|---|---:|
| 4.1-01 | Éligibilité : versement à une fondation d'entreprise d'intérêt général (caractère éducatif), même portant le nom de l'entreprise fondatrice ; association du nom admise ; absence de contrepartie | annexe | 0,5 |
| 4.1-02 | Plafond : 20 000 € ou 5 ‰ du CA HT si plus élevé : 5 ‰ × 52 000 000 = 260 000 € | calcul | 0,5 |
| 4.1-03 | Réduction 2026 : 260 000 × 60 % = 156 000 € (fraction ≤ 2 M€) ; excédent 140 000 € reportable sur les cinq exercices suivants, au taux de 60 % | calcul | 1 |
| 4.1-04 | Obligations : versements non déductibles du résultat ; déclaration des dons (plus de 10 000 € dans l'exercice) | annexe | 0,5 |
| 4.1-05 | Dons des clients : interdits pour une fondation d'entreprise (pas d'appel à la générosité publique ; seuls les salariés, mandataires, actionnaires du groupe fondateur) → proposition à écarter | conclusion | 0,5 |

**Réponse attendue**

*Règle.* Ouvrent droit à une réduction d'impôt les versements des entreprises soumises à l'IR ou à l'IS au profit d'organismes d'**intérêt général** notamment à caractère éducatif, y compris une **fondation d'entreprise, même si elle porte le nom de l'entreprise fondatrice**, et même si le nom de l'entreprise versante est associé aux opérations de l'organisme ; la réduction est de **60 %** pour la fraction des versements inférieure ou égale à **2 M€** (40 % au-delà) ; les versements sont retenus dans la limite de **20 000 €** ou de **5 ‰ du chiffre d'affaires** si ce montant est plus élevé ; l'**excédent** ouvre droit à réduction au titre des **cinq exercices suivants**, au taux auquel il a ouvert droit ; les versements **ne sont pas déductibles** du bénéfice ; l'entreprise qui verse plus de **10 000 €** dans l'exercice les **déclare** à l'administration (CGI 238 bis, 1, 2, 3, 6 et 8, annexe 4.1). (1 pt)

*Application (calcul de tête).* La fondation poursuit un but éducatif ouvert à tous les jeunes du département, avec une gestion désintéressée : versement éligible ; le logo de la SA sur ses documents n'est pas une contrepartie excluant le mécénat (association du nom admise par le texte). (1,5 pt)
- plafond : 5 ‰ × 52 000 000 = **260 000 €**, supérieur à 20 000 € : plafond retenu **260 000 €** ;
- versement retenu en 2026 : 260 000 € (sur 400 000 €), dans la fraction ≤ 2 M€ : réduction = 260 000 × 60 % = **156 000 €** ;
- excédent : 400 000 − 260 000 = **140 000 €**, reportable sur les exercices 2027 à 2031 dans la limite annuelle du plafond, au taux de 60 % (soit au plus 84 000 € de réduction future).

*Conclusion et proposition du directeur commercial.* La SA bénéficie d'une réduction d'impôt de 156 000 € au titre de 2026 ; elle ne déduit pas les 400 000 € de son résultat et déclare ses versements. La proposition de collecter des dons des **clients** est à écarter : une fondation d'entreprise ne peut faire **appel à la générosité publique** ni recevoir de dons, à l'exception de ceux des salariés, mandataires sociaux, sociétaires, adhérents ou actionnaires de l'entreprise fondatrice ou des sociétés du groupe (loi n° 87-571, art. 19-8) ; sa durée minimale est de cinq ans (art. 19-2). (0,5 pt)

Bloc `corrige.yaml` : `calculs_divers` — « Réduction d'impôt mécénat 2026 » ; `regles_utilisees` : `mecenat_taux`, `mecenat_taux_au_dela`, `mecenat_entreprise_seuil_taux`, `mecenat_plafond_fixe`, `mecenat_plafond_ca`, `mecenat_report`, `mecenat_entreprise_declaration_seuil`, `fondation_entreprise_duree_min`.

**Note à l'attention des correcteurs**
- Accepter « 0,5 % du CA » pour « 5 ‰ ».
- Ne pas exiger le calcul de la réduction future (84 000 €) ; la mention du report sur cinq exercices suffit.
- La distinction mécénat / parrainage peut être valorisée dans 4.1-01.

**Erreurs fréquentes**
- `JUR-J09` — oublier le plafond alternatif de 20 000 € ou appliquer 60 % à la totalité du versement (400 000 × 60 %) sans plafonnement.
- `JUR-F06` — déduire le don du résultat fiscal en plus de la réduction.

**Références**

| Référence | Contenu mobilisé |
|---|---|
| CGI 238 bis (version loi n° 2026-602) | éligibilité, taux, plafond, report, déclaration, non-déductibilité |
| Loi n° 87-571, art. 19-2 et 19-8 | durée minimale, ressources de la fondation d'entreprise |

---

### 4.2 Programme de prévention de la corruption (3 points)

**Type de question** : qualification (champ), évaluation d'un dispositif et conseil.

| Item | Attendu | Temps | Points |
|---|---|---|---:|
| 4.2-01 | Champ (Sapin II, art. 17) : dirigeants d'une société d'au moins 500 salariés, ou appartenant à un groupe dont la mère a son siège en France et comptant au moins 500 salariés, dont le CA ou le CA consolidé dépasse 100 M€ | regle | 0,5 |
| 4.2-02 | Application : groupe de 1 931 salariés, mère en France, CA consolidé 168 M€ → M. CASTELVIEL et la SA sont tenus | application | 0,5 |
| 4.2-03 | Huit mesures : code de conduite, alerte interne, cartographie des risques, évaluation des clients, fournisseurs et intermédiaires, contrôles comptables, formation, régime disciplinaire, contrôle et évaluation internes (seuil : 6 sur 8) | regle | 0,5 |
| 4.2-04 | Évaluation : code et alerte existants ; manquent cartographie, évaluation des tiers (agent marocain : commission élevée, clients publics, compte dans un autre pays = signaux d'alerte), formation, contrôles comptables et internes | application | 0,5 |
| 4.2-05 | Sanctions : contrôle de l'AFA ; commission des sanctions : injonction (trois ans au plus), sanctions pécuniaires (200 000 € dirigeant, 1 M€ personne morale), publication | regle | 0,5 |
| 4.2-06 | Conclusion et priorités : cartographie, évaluation et suspension de l'agent, formation ; risque pénal distinct (corruption d'agent public, CJIP) | conclusion | 0,5 |

**Réponse attendue**

*Règle.* Les présidents, directeurs généraux et gérants d'une société employant **au moins 500 salariés**, ou appartenant à un **groupe** dont la société mère a son siège en France et dont l'effectif comprend au moins 500 salariés, et dont le **chiffre d'affaires ou le chiffre d'affaires consolidé est supérieur à 100 M€**, doivent prendre des mesures destinées à prévenir et détecter la corruption et le trafic d'influence ; la société en est également responsable (loi n° 2016-1691 « Sapin II », art. 17, I). (0,5 pt)

*Application.* La SA emploie seule 281 salariés (au 31/12/2025), mais elle est la **société mère**, dont le siège est en France, d'un groupe de **1 931 salariés** ; le chiffre d'affaires consolidé (**168 M€**) dépasse 100 M€. M. CASTELVIEL, PDG, et la SA CASTELVIEL sont donc tenus de mettre en œuvre le programme. (0,5 pt)

*Les huit mesures et l'évaluation du dispositif.* Le programme comprend : 1° un **code de conduite** ; 2° un **dispositif d'alerte interne** ; 3° une **cartographie des risques** ; 4° des procédures d'**évaluation des clients, fournisseurs de premier rang et intermédiaires** ; 5° des **contrôles comptables** ; 6° un dispositif de **formation** des cadres et personnels les plus exposés ; 7° un **régime disciplinaire** ; 8° un dispositif de **contrôle et d'évaluation interne** des mesures (art. 17, II). (0,5 pt) Le code de conduite doit en outre être **intégré au règlement intérieur** après consultation des représentants du personnel (art. 17, II, 1°) : l'énoncé ne dit pas que cette formalité a été accomplie, ce qu'il faut vérifier. Au cas présent, seuls le code de conduite et la procédure d'alerte (au demeurant obligatoire dans toute entreprise d'au moins 50 salariés : loi n° 2016-1691, art. 8) existent. Manquent la cartographie, la formation, les contrôles comptables et internes et surtout l'**évaluation des intermédiaires** : l'agent marocain cumule les signaux d'alerte (commission de 8 % sur des marchés publics, versement sur un compte ouvert dans un pays tiers, absence de vérification). (0,5 pt)

*Sanctions.* L'**Agence française anticorruption** (AFA) contrôle la mise en œuvre du programme ; en cas de manquement, sa **commission des sanctions** peut enjoindre de mettre les procédures en conformité (dans un délai de **trois ans** au plus) et prononcer une sanction pécuniaire d'au plus **200 000 €** pour le dirigeant personne physique et **1 M€** pour la personne morale, avec publication possible (art. 17). (0,5 pt)

*Conclusion.* Priorités : établir la cartographie des risques, évaluer l'agent marocain (identité, bénéficiaire du compte, justification de la commission) et suspendre les paiements dans l'attente, former les cadres exposés, renforcer les contrôles comptables. Ces sanctions administratives sont distinctes du risque **pénal** si des faits de corruption d'agent public étaient établis ; la SA pourrait alors conclure une **convention judiciaire d'intérêt public** (C. proc. pén. 41-1-2). (0,5 pt)

Bloc `corrige.yaml` : `seuils` — « Programme anticorruption (Sapin II, art. 17) » ; `regles_utilisees` : `sapin2_effectif`, `sapin2_ca`, `sapin2_sanction_pm`, `sapin2_sanction_pp`, `lanceur_alerte_canal_interne_seuil`.

**Note à l'attention des correcteurs**
- Totalité des points de 4.2-03 dès que six des huit mesures sont citées.
- Valoriser dans 4.2-04 le candidat qui relève que le code de conduite doit être intégré au règlement intérieur après consultation des représentants du personnel.
- Le montant des sanctions n'est pas exigé ; ne pas pénaliser le candidat qui ne détaille pas la CJIP.
- Le régime pénal de la corruption n'est pas demandé ; aucun développement de droit pénal général n'est attendu.

**Erreurs fréquentes**
- `JUR-S08` — traiter les seuils de Sapin II comme alternatifs (« 500 salariés **ou** 100 M€ ») : ils sont cumulatifs.
- `JUR-J06` — confondre la sanction administrative de la commission des sanctions de l'AFA et la peine pénale.

**Références**

| Référence | Contenu mobilisé |
|---|---|
| Loi n° 2016-1691, art. 17 (version loi n° 2025-532) | champ, huit mesures, AFA, sanctions |
| Loi n° 2016-1691, art. 8 | procédure interne de signalement (50 salariés) |
| C. proc. pén. 41-1-2 | CJIP |

---

### 4.3 Cession des actions par M. CASTELVIEL (3 points)

**Type de question** : calcul de tête et qualification fiscale.

| Item | Attendu | Temps | Points |
|---|---|---|---:|
| 4.3-01 | Règle : plus-value de cession de valeurs mobilières des particuliers = prix de cession − prix d'acquisition (souscription) − frais ; PFU 12,8 % + prélèvements sociaux 18,6 % (31,4 %) | regle | 0,5 |
| 4.3-02 | Plus-value : 5 000 × (240 − 40) = 1 200 000 − 200 000 = 1 000 000 € | calcul | 0,5 |
| 4.3-03 | IR 128 000 € ; PS 186 000 € ; total 314 000 € ; prix net conservé, hors contributions sur les hauts revenus, 886 000 € | calcul | 1 |
| 4.3-04 | Droits d'enregistrement : 0,1 % × 1 200 000 = 1 200 €, à la charge de l'acquéreur sauf convention contraire | calcul | 0,5 |
| 4.3-05 | Abattement des dirigeants partant à la retraite : non applicable (pas de cessation des fonctions ni de départ à la retraite ; la SA n'est pas une PME au sens européen) | conclusion | 0,5 |

**Réponse attendue**

*Règle.* Les gains nets retirés par un particulier de la cession de valeurs mobilières et droits sociaux sont soumis à l'impôt sur le revenu (CGI 150-0 A) ; le gain est égal au prix de cession diminué du prix d'acquisition ou de souscription et des frais ; il supporte le **prélèvement forfaitaire unique** d'impôt sur le revenu de **12,8 %** et les **prélèvements sociaux** de **18,6 %**, soit **31,4 %**, sauf option globale pour le barème (CGI 200 A ; CSS L. 136-8, LFSS 2026). (0,5 pt)

*Application (calcul de tête).* (1,5 pt)
- prix de cession : 5 000 × 240 = **1 200 000 €** ; prix de souscription : 5 000 × 40 = **200 000 €** ;
- plus-value : 1 200 000 − 200 000 = **1 000 000 €** ;
- impôt sur le revenu : 1 000 000 × 12,8 % = **128 000 €** ;
- prélèvements sociaux : 1 000 000 × 18,6 % = **186 000 €** ;
- total : **314 000 €** (31,4 % de la plus-value) ; prix net conservé, hors contributions sur les hauts revenus : 1 200 000 − 314 000 = **886 000 €**.

*Droits d'enregistrement.* Les cessions d'actions de sociétés non cotées sont soumises à un droit de **0,1 %** (CGI 726) : 1 200 000 × 0,1 % = **1 200 €**, en principe à la charge de l'acquéreur, le fonds Massif Croissance. (0,5 pt)

*Abattement des dirigeants partant à la retraite.* L'abattement fixe de l'article 150-0 D ter suppose notamment que le cédant **cesse toute fonction** dans la société et **fasse valoir ses droits à la retraite** dans les deux ans qui précèdent ou suivent la cession : M. CASTELVIEL reste PDG et n'envisage pas sa retraite. En outre, la société dont les titres sont cédés doit être une **petite ou moyenne entreprise** au sens du droit de l'Union (CGI 150-0 D ter, II, 3°, a) : la SA CASTELVIEL, qui emploie 281 salariés et appartient à un groupe de 1 931 salariés, ne l'est pas. L'abattement est **inapplicable**. (0,5 pt)

Bloc `corrige.yaml` : `fiscal` — « Plus-value de cession des 5 000 actions » et « Droit d'enregistrement de la cession d'actions » ; `regles_utilisees` : `pfu_taux_ir`, `ps_taux_capitaux`, `pfu_taux_global`, `droits_actions_taux`.

**Note à l'attention des correcteurs**
- L'énoncé écarte la contribution exceptionnelle sur les hauts revenus (CGI 223 sexies) et la contribution différentielle sur les hauts revenus (CGI 224) ; valoriser, sans dépasser le maximum, le candidat qui en signale l'existence.
- Ne pas exiger le montant de l'abattement de 150-0 D ter ni sa date limite d'application (non nécessaires : condition de départ à la retraite non remplie).
- Accepter « droits à la charge du cessionnaire » ou « à la charge de l'acquéreur sauf clause contraire ».

**Erreurs fréquentes**
- `JUR-F01` — appliquer le PFU à 30 % : les prélèvements sociaux sur les plus-values de cession de valeurs mobilières sont de 18,6 % depuis la LFSS 2026 (hausse applicable dès l'imposition des revenus du patrimoine de 2025), soit 31,4 % avec l'impôt sur le revenu de 12,8 %. <!-- dscgcheck:ignorer -->
- `JUR-D03` — appliquer le régime des titres de participation (société cédante à l'IS) à un cédant personne physique.

**Références**

| Référence | Contenu mobilisé |
|---|---|
| CGI 150-0 A (version LF 2026) | imposition des gains de cession |
| CGI 200 A ; CSS L. 136-8 (LFSS 2026) | PFU 12,8 % ; prélèvements sociaux 18,6 % |
| CGI 726 | droit de 0,1 % sur les cessions d'actions |
| CGI 150-0 D ter, II, 2° c et 3° a | abattement des dirigeants partant à la retraite (retraite ; PME au sens européen) |
| CGI 223 sexies, 224 | contributions sur les hauts revenus (écartées par l'énoncé) |

---

### 4.4 Option pour le barème progressif (1 point)

**Type de question** : connaissance et conseil.

| Item | Attendu | Temps | Points |
|---|---|---|---:|
| 4.4-01 | Conditions : option expresse, annuelle, globale (ensemble des revenus et gains de l'année relevant du PFU) et irrévocable, exercée lors de la déclaration des revenus | regle | 0,5 |
| 4.4-02 | Effets : imposition au barème après abattement pour durée de détention possible pour les titres acquis avant 2018 (cas des actions souscrites en 1999) ; prélèvements sociaux inchangés sur la totalité, dont 6,8 % de CSG déductible l'année suivante ; intérêt à comparer selon le taux marginal (avec un gain de 1 000 000 €, le PFU reste probablement plus favorable) | conclusion | 0,5 |

**Réponse attendue**

*Règle et application.* Le contribuable peut **opter** pour l'imposition au **barème progressif** ; l'option est **expresse**, **globale** (elle s'applique à l'ensemble des revenus et gains de l'année entrant dans le champ du PFU), **annuelle** et **irrévocable** pour l'année, et s'exerce lors du dépôt de la déclaration des revenus (CGI 200 A). (0,5 pt) En cas d'option, les actions ayant été **souscrites avant le 1er janvier 2018** (en 1999), la plus-value peut bénéficier de l'**abattement pour durée de détention** pour l'impôt sur le revenu ; les **prélèvements sociaux** restent dus sur la totalité du gain ; en cas d'option, **6,8 %** de la CSG sont déductibles du revenu imposable de l'année de leur paiement, soit l'année suivante (CGI 154 quinquies, II). Avec un gain de 1 000 000 €, la plus-value serait largement imposée dans la tranche supérieure du barème : l'intérêt de l'option doit être chiffré au cas par cas, et le PFU reste en principe plus favorable pour un contribuable fortement imposé. (0,5 pt)

**Note à l'attention des correcteurs**
- Aucun taux d'abattement ni aucun calcul n'est demandé.
- Accepter une conclusion prudente (« à comparer selon la situation fiscale du foyer ») si le caractère global et irrévocable de l'option est énoncé.

**Erreurs fréquentes**
- `JUR-J04` — affirmer que l'option peut être limitée à la seule plus-value (elle est globale).

**Références**

| Référence | Contenu mobilisé |
|---|---|
| CGI 200 A | option globale pour le barème |
| Abattement pour durée de détention (titres acquis avant 2018) | conditions |
| CGI 154 quinquies, II | CSG déductible (6,8 points) en cas d'imposition au barème |

---

## Points à vérifier avant publication

> **À vérifier** :
> - Prélèvements sociaux de 18,6 % (`ps_taux_capitaux`, statut S : CRDS et prélèvement de solidarité non relus) et PFU global de 31,4 % (`pfu_taux_global`, statut S) ; règles fiscales de l'année : revérifier en janvier 2027 (délai de vérification d'un mois pour un chiffre fiscal ou social).
> - 150-0 D ter : la date limite des cessions (`pv150dter_fin`, statut ?) n'est pas vérifiée ; le corrigé n'utilise pas l'abattement (condition de départ à la retraite non remplie).
> - Loi n° 87-571, art. 19-8 (dons à la fondation d'entreprise) : lu selon F09, à relire sur Légifrance.
> - Abattement pour durée de détention sur option pour le barème : [S].
>
> Aucune règle de ce corrigé ne repose sur un texte non promulgué. <!-- dscgcheck:ignorer -->
