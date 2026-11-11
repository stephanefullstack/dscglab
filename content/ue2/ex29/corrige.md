# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 29 — Dossier 2 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F09 éthique, conformité et cybersécurité, F10 auteurs et théories, F99 liste noire (à jour au 23/10/2026) et fiche commune Sapin II, LCB-FT, MiCA (à jour au 23/10/2026, numérotation du devoir de vigilance mise à jour le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (chiffrage de l'incident et clause financière, VAN probabilisée, indice de profitabilité, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Chiffrage du préjudice, EBITDA, trésorerie et clause financière | `2.2.e` Sensibiliser au risque d'attaque cyber et de récupération des flux financiers internationaux | 3 |
| 2.2 Services de l'État et fonds convertis en crypto-actifs | `2.2.e` Sensibiliser au risque d'attaque cyber et de récupération des flux financiers internationaux | 1 |
| 2.3 Fraude, corruption, Sapin II, devoir de vigilance et prévention | `2.2.d` Sensibiliser au risque de corruption et de fraude interne et externe | 3 |
| 2.4 Morale, éthique, déontologie et conformité | `2.2.a` Distinguer l'éthique, de la morale, de la déontologie et de la conformité | 1 |
| 2.5 Obligations LCB-FT du cabinet et rôle de Tracfin | `2.2.c` Appliquer la réglementation pour la lutte contre le blanchiment et le financement du terrorisme (LCB-FT) | 2 |
| 2.6 VAN probabilisée du programme de sécurisation | `7.1.a` Évaluer et classer des projets en milieu certain ; `7.1.b` Évaluer et classer des projets en milieu incertain | 5 |
| **Total** | | **15** |

Part du calcul : environ 6 points (2.1-01 à 2.1-05, 2.6-01 à 2.6-05). Part de l'analyse : environ 9 points. Les questions 2.2 à 2.5 sont rédactionnelles : elles valent ensemble 7 points et doivent être traitées avec les données du cas (`JUR-T13`, `JUR-T15`).

---

### 2.1 Chiffrage du préjudice, EBITDA, trésorerie et clause financière (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Fonds non récupérés 2,70 M€ (4,20 − 1,50) ; coûts directs 1,00 M€ ; perte brute 3,70 M€ ; les factures réglées ensuite à LUNSHEO ne sont pas un coût de l'incident | 0,5 |
| 2.1-02 | Marge perdue 0,90 M€ (5 jours) ; marge indemnisable 0,54 M€ (3 jours après carence) | 0,5 |
| 2.1-03 | Postes garantis 4,14 M€ (communication exclue) ; après franchise 3,64 M€ ; indemnité plafonnée à 3,00 M€ | 0,5 |
| 2.1-04 | Perte nette 1,60 M€ ; EBITDA 2027 : 102,00 → 100,40 M€ ; sortie de trésorerie de 2027 : 4,60 M€ (trésorerie 38,00 → 33,40 M€), car l'indemnité n'est encaissée qu'en 2028 | 0,5 |
| 2.1-05 | Ratio de la clause : 2,30 avant l'incident ; 96,60 / 38,40 = 2,52 après, au-dessus du seuil de 2,50 ; dépassement équivalent à 0,60 M€ de dette | 0,5 |
| 2.1-06 | Commentaire et mesures avant la clôture : avance sur indemnité d'au moins 0,60 M€, discussion préalable avec les banques, autres leviers de trésorerie | 0,5 |

**Fonds non récupérés et coûts directs (0,5 pt).**

| Poste (M€) | Montant |
|---|---:|
| Virements frauduleux (1,80 + 2,40) | 4,20 |
| Fonds restitués grâce au rappel de fonds | − 1,50 |
| **Fonds non récupérés** | **2,70** |
| Experts | 0,40 |
| Remise en état du système d'information | 0,50 |
| Communication de crise | 0,10 |
| **Coûts directs** | **1,00** |
| **Perte brute (hors marge perdue)** | **3,70** |

Les 0,60 M€ convertis en crypto-actifs, dont 0,25 M€ bloqués chez un prestataire agréé, ne sont pas comptés comme récupérés : leur restitution est incertaine (annexe 2.1). Les deux factures payées à LUNSHEO en février 2027 correspondent à des achats déjà prévus : ce sont les virements détournés qui constituent la perte, pas le second paiement au vrai fournisseur.

**Marge perdue (0,5 pt).** Marge perdue par jour d'arrêt = 0,60 × (1 − 25 %) × 40 % = 0,18 M€.
- Marge perdue sur les cinq jours d'arrêt : 0,18 × 5 = **0,90 M€**.
- Marge indemnisable, au-delà des deux jours de carence : 0,18 × 3 = **0,54 M€**.

**Indemnité de l'assurance (0,5 pt).**

| Postes garantis (M€) | Montant |
|---|---:|
| Fonds détournés nets des sommes récupérées | 2,70 |
| Experts | 0,40 |
| Remise en état | 0,50 |
| Pertes d'exploitation après carence | 0,54 |
| **Total des postes garantis** | **4,14** |
| Franchise | − 0,50 |
| Montant après franchise | 3,64 |
| **Indemnité, limitée au plafond** | **3,00** |

La communication de crise (0,10 M€), exclue, et les deux premiers jours de marge perdue (0,36 M€) restent à la charge du groupe. Le plafond est atteint : 0,64 M€ de postes garantis ne sont pas indemnisés.

**Perte nette, EBITDA et trésorerie de 2027 (0,5 pt).**
- **Perte nette** restant à la charge du groupe = 3,70 + 0,90 − 3,00 = **1,60 M€**, soit environ 1,6 % de l'EBITDA prévu (calcul facultatif).
- **EBITDA de 2027** : l'indemnité, acceptée par l'assureur, est comptabilisée en 2027 ; l'effet est donc de − 1,60 M€ : 102,00 → **100,40 M€**.
- **Trésorerie de 2027** : toutes les pertes et tous les coûts sont décaissés (ou non encaissés) en 2027, alors que l'indemnité ne sera versée qu'en février 2028 ; la sortie nette est de 2,70 + 1,00 + 0,90 = **4,60 M€** : trésorerie 38,00 → **33,40 M€**, et dette financière nette hors dettes locatives 92,00 → **96,60 M€**.

L'écart entre l'effet sur l'EBITDA (1,60 M€) et l'effet sur la trésorerie (4,60 M€) est la créance sur l'assureur (3,00 M€) : le préjudice est modeste en résultat, mais il pèse près de trois fois plus sur la trésorerie de 2027.

**Clause financière au 31 décembre 2027 (0,5 pt).**

| M€ | Avant l'incident | Après l'incident |
|---|---:|---:|
| Dette financière nette hors dettes locatives (130,00 − trésorerie) | 92,00 | 96,60 |
| EBITDA − loyers décaissés (102,00 − 62,00 ; puis − 1,60) | 40,00 | 38,40 |
| **Ratio** | **2,30** | **2,52** |
| Marge avant le seuil : 2,50 × (EBITDA − loyers) − dette nette | 8,00 | − 0,60 |

Le ratio passe de 2,30 à 2,52 et **dépasse le seuil de 2,50** : la clause serait rompue à la clôture de 2027. La marge de 8,00 M€ de dette dont disposait le groupe a disparu ; il manque 0,60 M€. Sans le décalage d'encaissement, le ratio serait de (96,60 − 3,00) / 38,40 = 2,44 (calcul facultatif) : c'est le **délai de règlement de l'indemnité**, et non le montant de la perte, qui fait franchir le seuil.

**Commentaire et mesures (0,5 pt).**
- Un incident dont le coût net (1,60 M€) ne représente que 4 % de l'EBITDA diminué des loyers peut mettre en cause le crédit syndiqué, parce que la clause est déjà tendue par les investissements du plan « ERVIDANE 2030 » (ratio de 2,30 contre 1,90 fin 2026) et que la sortie de trésorerie précède l'indemnisation.
- **Demander à ALCERNE une avance sur indemnité** d'au moins 0,60 M€ encaissée avant le 31 décembre 2027 : avec 0,60 M€, le ratio revient à 96,00 / 38,40 = 2,50, au seuil ; une avance de 1,00 M€ le ramène à 2,49 et laisse une petite marge.
- **Informer les banques sans attendre** et, si l'avance n'est pas obtenue, négocier avant la clôture une renonciation ponctuelle à se prévaloir du dépassement : son coût (commission, hausse de la marge) est plus faible en amont qu'après la rupture constatée. Les deux banques qui ont demandé une présentation des mesures (annexe 2.6) sont les interlocuteurs naturels.
- Leviers complémentaires : décaler une partie des investissements de fin 2027 du plan, réduire le BFR (stocks de vélos neufs), prudence sur les distributions de 2027.
- Pour une société cotée, la cohérence de la communication financière sur l'incident et ses effets compte autant que le chiffre : le marché et les banques jugent la maîtrise du risque.

**Réponses tolérées** : perte nette présentée après impôt (1,60 × 0,75 = 1,20 M€) si elle est donnée en complément du montant avant impôt imposé par l'annexe 2.7 ; trésorerie et clause recalculées en supposant l'indemnité encaissée en 2027, si l'hypothèse est écrite et commentée (ratio de 2,44) — 2.1-04 et 2.1-05 sont alors notés à moitié, la lecture de l'annexe 2.2 étant manquée ; ratio exprimé au seuil (« 2,52 > 2,50 ») sans calcul de la marge de 0,60 M€.

**Erreurs fréquentes**
- `JUR-T03` — oublier le délai de carence, l'exclusion de la communication ou le plafond, qui figurent dans l'annexe 2.2 ; appliquer la franchise après le plafond (3,00 − 0,50 = 2,50).
- Compter comme récupérés les fonds convertis en crypto-actifs ou bloqués par le prestataire ; compter le paiement des factures de LUNSHEO comme un coût supplémentaire.
- Confondre l'effet sur l'EBITDA et l'effet sur la trésorerie (le corrigé du sujet zéro additionne décaissements et pertes ; une bonne copie les distingue) ; retenir l'EBITDA de 102,00 M€ au lieu de l'EBITDA diminué des loyers dans le ratio de la clause.
- `JUR-T13` — calculs sans conclusion opérationnelle sur la clause et sur ce que la direction doit faire avant la clôture.

---

### 2.2 Services de l'État et fonds convertis en crypto-actifs (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Rôle de l'ANSSI, de la DGSI, du COMCYBER-MI et du SISSE, et services que le groupe peut solliciter | 0,5 |
| 2.2-02 | Récupération des fonds : rapidité du rappel de fonds ; crypto-actifs : prestataire agréé MiCA identifiable et soumis à la LCB-FT, plateforme hors Union beaucoup plus difficile à atteindre | 0,5 |

**Les services de l'État (0,5 pt).**

| Service | Rôle | Pour ERVIDANE |
|---|---|---|
| **ANSSI** (Agence nationale de la sécurité des systèmes d'information, rattachée au secrétaire général de la défense et de la sécurité nationale) | autorité nationale de la sécurité des systèmes d'information : prévention, alerte (CERT-FR), qualification de prestataires de réponse aux incidents, recommandations d'hygiène informatique | conseils pour la remise en état et choix d'un prestataire qualifié ; le groupe n'est pas un opérateur sensible, l'ANSSI l'oriente surtout vers ses guides et le dispositif d'assistance aux victimes (Cybermalveillance.gouv.fr) |
| **DGSI** (direction générale de la sécurité intérieure, ministère de l'Intérieur) | contre-espionnage, protection du patrimoine économique, lutte contre les ingérences étrangères | utile si l'intrusion visait aussi des informations stratégiques (fournisseurs, prix d'achat) ; peu concernée par une escroquerie de nature financière |
| **COMCYBER-MI** (commandement du ministère de l'Intérieur dans le cyberespace) | coordonne la lutte de la police et de la gendarmerie contre la cybercriminalité : plainte, enquête, coopération internationale pour suivre les fonds | **interlocuteur principal** : la plainte ouvre une enquête, dans le cadre de laquelle l'autorité judiciaire peut demander, par la coopération internationale, le gel des comptes et des portefeuilles de crypto-actifs |
| **SISSE** (service de l'information stratégique et de la sécurité économiques, ministère de l'Économie) | politique de sécurité économique, protection des entreprises, guichet de la loi de blocage | peut accompagner le groupe dans ses relations avec des autorités étrangères (demandes d'informations, procédures) |

La récupération repose d'abord sur la **rapidité** : le rappel de fonds a permis de retrouver 1,50 M€ parce que la fraude a été découverte le lendemain du second virement ; le premier virement, transféré le jour même, est perdu.

**Conversion en crypto-actifs (0,5 pt).**
- La conversion vise à faire sortir les fonds du circuit bancaire. Le règlement européen MiCA (règlement (UE) 2023/1114, applicable depuis le 30 décembre 2024) soumet les **prestataires de services sur crypto-actifs** à un agrément (en France, par l'AMF ; seuls les prestataires agréés peuvent exercer depuis la fin de la période transitoire, le 1er juillet 2026), à des règles de conduite et de conservation des actifs des clients ; ces prestataires sont aussi **assujettis à la LCB-FT** : ils identifient leurs clients et doivent répondre aux réquisitions.
- Pour les **0,25 M€** passés par un prestataire agréé dans l'Union, le titulaire du compte est identifié et les actifs ont été bloqués : une restitution est possible, au terme de la procédure judiciaire, sans être certaine (cours des crypto-actifs, délais).
- Pour les **0,35 M€** transférés vers une plateforme établie hors de l'Union, MiCA ne s'applique pas : sans coopération de la plateforme ni de son pays, la récupération est très improbable. Les transactions restent néanmoins traçables sur le registre distribué, ce qui aide l'enquête.
- Conséquence pour le chiffrage : aucune récupération supplémentaire ne doit être retenue tant qu'elle n'est pas acquise (prudence) ; une restitution ultérieure serait un produit de 2027 ou de 2028.

Une ligne par service et deux idées sur MiCA suffisent pour la totalité des points (la question vaut 1 point, soit environ 4 minutes).

**Réponses tolérées** : mention de la DGE, de Cybermalveillance.gouv.fr ou de la CNIL (si des données personnelles avaient été atteintes) ; présentation de Tracfin comme destinataire possible d'informations des banques et des prestataires sur les flux en cause.

**Erreurs fréquentes**
- `JUR-T13` — liste des services sans dire lesquels aident ERVIDANE à récupérer les fonds (COMCYBER-MI, banque, prestataire agréé) et lesquels relèvent surtout de la sécurité (ANSSI, DGSI, SISSE).
- Présenter MiCA comme une directive, ou comme un texte qui garantit la restitution des fonds ; développer la technique des registres distribués (hors sujet, UE 5).
- Analyse informatique de l'intrusion : hors programme en UE 2 (« approche non technique »).

---

### 2.3 Fraude, corruption, Sapin II, devoir de vigilance et prévention (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Qualification des risques : fraude externe (faux fournisseur, détournement de paiement), fraude interne (détournement d'actifs par remboursements fictifs), proposition de corruption (active de la part de l'assembleur, qui propose ; passive si l'acheteur accepte) ; faiblesses du contrôle interne en cause | 0,5 |
| 2.3-02 | Sapin II : 4 600 salariés ≥ 500 et 860 M€ > 100 M€, société mère en France → obligation de prévention ; responsabilité de la présidente-directrice générale ; extension aux filiales | 0,5 |
| 2.3-03 | Devoir de vigilance : 4 150 salariés en France (< 5 000) et 4 600 au total (< 10 000) en 2025 et 2026 → non soumis ; démarche volontaire utile pour les fournisseurs asiatiques | 0,5 |
| 2.3-04 | Appréciation du dispositif au regard des huit mesures et propositions (cartographie, code de conduite, évaluation des tiers, double validation des coordonnées bancaires, séparation des tâches, alerte, formation, contrôle) | 1 |
| 2.3-05 | Enjeux pour la performance et la réputation, chiffrés avec les données du cas | 0,5 |

**Qualification des risques (0,5 pt).** Sans analyse de droit pénal, trois risques de nature différente :
- **Fraude externe** : la fraude au virement est une fraude au faux fournisseur (changement de coordonnées bancaires) précédée d'une compromission de messagerie ; c'est un **détournement de flux financiers** par des tiers. Elle a réussi parce qu'un seul salarié pouvait faire modifier un compte fournisseur sans contre-appel.
- **Fraude interne** : les remboursements fictifs sur cartes cadeaux sont un **détournement d'actifs** par des salariés (0,18 M€ sur deux ans). L'opportunité vient de l'absence de séparation des tâches (même personne pour saisir, valider et clôturer) et de contrôle à distance. Le triangle de la fraude (Cressey) le résume : pression, **opportunité**, rationalisation ; le contrôle interne agit sur l'opportunité.
- **Corruption** : VINHARO propose un avantage indu à un acheteur pour obtenir un contrat : c'est une proposition de corruption, **active** du côté de l'assembleur, qui propose, **passive** du côté de l'acheteur s'il accepte. Le silence de M. DARMEYRAC, qui n'a pas signalé la proposition, montre que le risque n'est pas maîtrisé, même si la commission n'a pas été versée.

**Loi Sapin II (0,5 pt).** L'article 17 vise les sociétés d'au moins 500 salariés, ou les groupes dont la société mère a son siège en France et dont l'effectif atteint 500 salariés, et dont le chiffre d'affaires consolidé dépasse 100 M€. ERVIDANE SA, société mère française d'un groupe de **4 600 salariés** réalisant **860 M€** de chiffre d'affaires, est **soumise** à l'obligation de prévention de la corruption. L'obligation pèse sur la présidente-directrice générale et sur la société, et s'étend aux filiales contrôlées, dont ERVIDANE Benelux. L'AFA peut contrôler le dispositif et prononcer une sanction pécuniaire (jusqu'à 1 M€ pour la société et 200 000 € pour la dirigeante), avec publication possible.

**Devoir de vigilance (0,5 pt).** Le plan de vigilance est obligatoire à partir de 5 000 salariés en France (société et filiales françaises) ou de 10 000 salariés en France et à l'étranger, à la clôture de deux exercices consécutifs. ERVIDANE emploie **4 250 puis 4 150** salariés en France et **4 720 puis 4 600** au total en 2025 et 2026 : le groupe **n'est pas soumis** au devoir de vigilance. Une démarche volontaire inspirée du plan de vigilance (cartographie des risques chez les fournisseurs et sous-traitants d'Asie, évaluation, alerte) reste utile : elle rejoint la mission (« pour longtemps ») et prépare le groupe à des exigences de ses parties prenantes.

**Appréciation du dispositif et mesures de prévention (1 pt).**

| Mesure de l'article 17 | Situation chez ERVIDANE (annexe 2.4) | Proposition |
|---|---|---|
| Cartographie des risques | de 2020, sans les achats en Asie | la refaire en couvrant les achats, les paiements, les caisses des magasins et les zones à risque ; la mettre à jour chaque année |
| Code de conduite | de 2019, silencieux sur les cadeaux, commissions et paiements | le compléter (cadeaux et avantages, conflits d'intérêts, relations avec les fournisseurs) et l'intégrer au règlement intérieur |
| Évaluation des tiers | aucune | évaluer les fournisseurs de premier rang et intermédiaires avant le contrat (VINHARO, LUNSHEO), clause anticorruption dans les contrats |
| Dispositif d'alerte | connu du seul siège | l'étendre aux magasins, aux acheteurs et aux franchisés, avec garantie de confidentialité |
| Contrôles comptables | changement de coordonnées bancaires et remboursements sans contrôle | **double validation** et contre-appel de tout changement de coordonnées bancaires ; **séparation des tâches** en caisse ; contrôle à distance des remboursements et des cartes cadeaux |
| Formation | aucune pour les acheteurs | former en priorité les acheteurs, la comptabilité fournisseurs et les responsables de magasin |
| Régime disciplinaire | non mentionné | sanctions prévues et appliquées (remboursements fictifs, absence de signalement) |
| Contrôle et évaluation interne | aucun rapport au comité d'audit depuis 2021 | rapport annuel de l'audit interne au comité d'audit sur la prévention de la fraude et de la corruption |

Le dispositif existe sur le papier mais n'est ni à jour ni appliqué : il ne répond pas aux exigences de l'article 17 et laisse ouvertes les failles qu'ont exploitées les fraudeurs. Le contrat avec VINHARO doit être suspendu jusqu'à l'évaluation de ce fournisseur.

**Enjeux pour la performance et la réputation (0,5 pt).**
- **Performance** : pertes directes (fraude externe : 1,60 M€ net en 2027 ; fraude interne : 0,18 M€) ; une commission de 2 % sur 12 M€ d'achats, soit environ 0,24 M€ par an, finit dans le prix payé au fournisseur et dégrade la marge brute ; risque de sanction de l'AFA (jusqu'à 1 M€) ; tension sur la clause financière (question 2.1) et hausse possible du coût de la dette ; franchise et prime d'assurance en hausse.
- **Réputation et valeur** : pour une société cotée et à mission, la confiance des clients, des franchisés, des banques et des investisseurs est un actif immatériel ; une affaire de corruption chez un fournisseur asiatique contredirait la raison d'être et nourrirait la critique de BRESKANE Capital sur la gouvernance. Un risque mal maîtrisé augmente la prime de risque exigée et donc le coût du capital.
- **Gouvernance** : le comité d'audit doit suivre le dispositif ; la prévention de la fraude relève de la responsabilité de la direction devant les actionnaires (théorie de l'agence) et les parties prenantes.

**Réponses tolérées** : qualification de la fraude au virement comme « fraude au président » si le candidat précise qu'il s'agit ici d'une usurpation de fournisseur ; mention de la loi de blocage ou du dispositif de protection des lanceurs d'alerte, si elle est reliée au cas ; enjeux de réputation chiffrés autrement (perte de valeur boursière, multiple d'EBITDA) s'ils restent des ordres de grandeur.

**Erreurs fréquentes**
- Se lancer dans une analyse de droit pénal (nature des infractions, peines) : hors programme (guide, p. 62) ; la question porte sur le risque et l'organisation.
- Conclure que le groupe est soumis au devoir de vigilance parce que ses salariés sont nombreux, sans comparer aux seuils de 5 000 et 10 000 ; oublier la condition des deux exercices consécutifs.
- `JUR-T13` — énumérer les huit mesures sans les confronter au dispositif décrit par l'audit interne.
- `JUR-T05` — ne pas relier la prévention de la fraude à la performance durable, à la mission et à la gouvernance.

---

### 2.4 Morale, éthique, déontologie et conformité (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Définitions distinctes des quatre notions | 0,5 |
| 2.4-02 | Application : l'usage local ne justifie rien ; comportement attendu de l'acheteur (refuser, signaler) et du groupe (règle claire, formation, suites) | 0,5 |

**Définitions (0,5 pt).**
- **Morale** : ensemble de devoirs et d'interdits à prétention universelle, qui distingue le bien du mal et s'impose à chacun indépendamment de son intérêt.
- **Éthique** : réflexion sur les valeurs qui guident l'action ; en entreprise, valeurs que l'organisation se donne (charte, raison d'être) et qui vont au-delà de la règle.
- **Déontologie** : règles de conduite propres à une profession, codifiées et contrôlées par cette profession (par exemple celles des experts-comptables).
- **Conformité** : organisation qui assure le respect des normes externes (lois, règlements) et internes (code de conduite) : cartographie, procédures, contrôles, formation, alerte, sanctions.

**Application (0,5 pt).**
- L'argument de l'acheteur (« c'est l'usage dans ce pays ») confond un fait (une pratique répandue) et une norme. Il ne vaut ni moralement (accepter un avantage personnel au détriment de son employeur est mal partout), ni au regard de la **conformité** : le groupe, soumis à Sapin II, doit prévenir la corruption dans toutes ses relations, en France comme à l'étranger ; le code de conduite doit s'appliquer aux achats en Asie.
- L'acheteur n'a pas de déontologie professionnelle codifiée comme un expert-comptable ; c'est au groupe de lui donner des règles écrites (code de conduite, politique des cadeaux) et une **éthique** cohérente avec la raison d'être.
- **Comportement attendu** : refuser la proposition, la **signaler** sans délai par le dispositif d'alerte ou à sa hiérarchie, ne pas attribuer le contrat dans ces conditions. Pour le groupe : rappeler la règle, former, évaluer VINHARO et tirer les conséquences de l'absence de signalement (régime disciplinaire), sans faire de l'acheteur le seul responsable d'un dispositif défaillant.

**Réponses tolérées** : recours à la hiérarchie des ordres de Comte-Sponville : la logique économique (obtenir un contrat, une commission) ne peut régir l'ordre juridique ni l'ordre moral (« barbarie » si l'usage économique dicte ce qui est permis) ; mention de l'ordre de l'amour (loyauté envers l'équipe et l'entreprise).

**Erreurs fréquentes**
- Long développement philosophique sans lien avec l'acheteur et le groupe : le guide demande une « analyse conceptuelle et appliquée » (p. 60-61).
- Confondre morale et conformité (« c'est interdit donc c'est immoral ») ou présenter l'éthique comme une simple obligation légale.
- `JUR-T13` — définitions récitées sans conclure sur le comportement attendu.

---

### 2.5 Obligations LCB-FT du cabinet et rôle de Tracfin (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Le cabinet est assujetti ; enjeux de la LCB-FT ; signaux d'alerte relevés chez ROVELIA | 0,5 |
| 2.5-02 | Vigilance : connaissance du client et du bénéficiaire effectif de l'apport, examen renforcé des opérations inhabituelles, justificatifs, conservation | 0,5 |
| 2.5-03 | Déclaration de soupçon à Tracfin si le doute persiste ; rôle de Tracfin ; interdiction d'informer le gérant comme ERVIDANE | 0,5 |
| 2.5-04 | Conséquences d'un manquement : pour le cabinet (sanctions disciplinaires, responsabilité, réputation) et pour le réseau ERVIDANE | 0,5 |

**Assujettissement et signaux d'alerte (0,5 pt).** Les experts-comptables figurent parmi les professionnels assujettis au dispositif LCB-FT. La LCB-FT vise à empêcher que des capitaux d'origine illicite soient introduits dans l'économie légale et à protéger l'intégrité du système financier. Chez ROVELIA, trois signaux convergent :
- des dépôts d'espèces multipliés par plus de cinq (0,21 M€ contre 0,04 M€), alors que le chiffre d'affaires stagne (1,90 M€), que 92 % des ventes sont réglées par carte ou virement et que les ventes en espèces représentent environ 2 % du chiffre d'affaires (0,04 M€) ; les dépôts de 2026 dépassent même l'ensemble des ventes non réglées par carte ou par virement (8 % × 1,90 = 0,15 M€) : ils ne peuvent pas provenir des seules recettes du magasin ; des dépôts fractionnés juste sous 10 000 €, sur quatre mois ;
- un apport en compte courant de 0,15 M€ venu d'une société étrangère dont ni l'activité ni les associés ne sont connus, sans convention ;
- la pression du gérant pour que le collaborateur ne pose pas de questions.

**Vigilance (0,5 pt).** Le cabinet doit :
- **connaître son client** et l'objet de la relation, et identifier le **bénéficiaire effectif** de l'apport (qui se trouve derrière la société étrangère) ;
- exercer une **vigilance constante** : comparer les opérations à la connaissance qu'il a de l'activité (un magasin de vélos encaisse peu d'espèces) ;
- mener un **examen renforcé** des opérations inhabituelles, sans justification économique apparente : demander l'origine des espèces (pièces de caisse, relevés), la convention et les justificatifs de l'apport, l'identité des associés de l'apporteur ;
- consigner ses diligences et conserver les documents.
Le cabinet n'enquête pas et ne qualifie pas les faits : il vérifie la cohérence des opérations.

**Déclaration de soupçon et Tracfin (0,5 pt).**
- Si les justifications sont absentes ou insuffisantes, le cabinet doit adresser une **déclaration de soupçon à Tracfin** : il suffit de soupçonner, ou d'avoir de bonnes raisons de soupçonner, que les sommes proviennent d'une infraction grave ; la déclaration se fait sans attendre de certitude.
- **Tracfin**, cellule de renseignement financier rattachée aux ministres de l'économie et du budget, reçoit et analyse les déclarations, complète l'information et transmet, s'il y a lieu, à la justice ou aux administrations ; il peut s'opposer à l'exécution d'une opération.
- La déclaration est **confidentielle** : le collaborateur ne doit en informer **ni M. SOLVIGNAC, ni la direction d'ERVIDANE**, bien que le groupe soit aussi client du cabinet et qu'il renouvelle les contrats de franchise. Il peut seulement demander au gérant les justificatifs, sans évoquer la déclaration. Le déclarant de bonne foi est protégé.
- Le collaborateur agit dans le cadre des procédures du cabinet (déclarant et correspondant Tracfin désignés) ; il ne peut pas, face aux pressions, accepter de « ne pas compliquer les choses ».

**Conséquences d'un manquement (0,5 pt).**
- **Pour le cabinet** : sanctions disciplinaires par l'institution professionnelle qui contrôle les experts-comptables, mise en cause de sa responsabilité, voire poursuites s'il a apporté son concours à des opérations de blanchiment ; perte de confiance des clients et des banques, atteinte durable à sa réputation.
- **Pour le réseau ERVIDANE** : un franchisé utilisé pour blanchir des fonds expose l'enseigne à un risque de réputation (presse, clients, banques), à des relations bancaires plus difficiles et à une remise en cause de la confiance dans le réseau ; c'est aussi un sujet de conformité pour le groupe, qui doit évaluer ses partenaires (question 2.3). Le groupe ne sera pas informé de la déclaration : il doit renforcer de lui-même l'évaluation de ses franchisés.

**Réponses tolérées** : mention de l'approche par les risques (vigilance renforcée en présence d'un pays tiers à risque) ; possibilité de mettre fin à la mission si le client refuse de répondre, en plus (et non à la place) de la déclaration ; mention de l'autorité européenne de lutte contre le blanchiment (AMLA) sans développement.

**Erreurs fréquentes**
- Penser qu'il faut une preuve avant de déclarer, ou que le collaborateur doit prévenir ERVIDANE pour protéger le réseau : c'est précisément interdit.
- Développer les peines ou la procédure de déclaration (formulaires, délais) : hors programme en UE 2 (« détail procédural et pénal »), relève de l'UE 1.
- `JUR-T13` — réciter les obligations sans relever les signaux du cas (espèces, fractionnement, apport étranger, pression du gérant).

---

### 2.6 VAN probabilisée du programme de sécurisation (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Pertes évitées : 0,60 ; 1,20 ; 1,80 M€ par an | 0,5 |
| 2.6-02 | Flux nets annuels après IS, avec l'économie d'impôt sur l'amortissement (0,125 M€) : 0,35 ; 0,80 ; 1,25 M€ | 1 |
| 2.6-03 | VAN : − 1,10 ; 0,69 ; 2,49 M€ | 0,5 |
| 2.6-04 | Espérance de la VAN 0,51 M€ ; écart-type 1,26 M€ | 1 |
| 2.6-05 | Probabilité d'une VAN négative 30 % ; indice de profitabilité 1,21 | 0,5 |
| 2.6-06 | Lecture du risque : dispersion forte, fréquence d'équilibre, limites des probabilités | 0,5 |
| 2.6-07 | Recommandation intégrant les éléments non chiffrés | 1 |

**Pertes évitées et flux nets annuels (1,5 pt).** Économie d'impôt sur l'amortissement = 2,50 / 5 × 25 % = 0,125 M€ par an.

| M€ par an | Faible | Central | Élevé |
|---|---:|---:|---:|
| Incidents significatifs par an sans le programme | 0,5 | 1,0 | 1,5 |
| **Pertes évitées** (fréquence × 60 % × 2,00) | **0,60** | **1,20** | **1,80** |
| + baisse de la prime d'assurance | 0,10 | 0,10 | 0,10 |
| − coûts de fonctionnement | − 0,40 | − 0,40 | − 0,40 |
| = gain annuel avant IS | 0,30 | 0,90 | 1,50 |
| × (1 − 25 %) | 0,225 | 0,675 | 1,125 |
| + économie d'IS sur l'amortissement | 0,125 | 0,125 | 0,125 |
| **Flux net annuel (années 1 à 5)** | **0,35** | **0,80** | **1,25** |

**VAN par scénario (0,5 pt).** Facteur d'actualisation d'une annuité de 5 ans à 8 % : (1 − 1,08^−5) / 0,08 = 3,9927.
- Faible : 0,35 × 3,9927 − 2,50 = **− 1,10 M€** ;
- Central : 0,80 × 3,9927 − 2,50 = **0,69 M€** ;
- Élevé : 1,25 × 3,9927 − 2,50 = **2,49 M€**.

**Espérance et écart-type (1 pt).**
- E(VAN) = 0,30 × (− 1,1026) + 0,50 × 0,6942 + 0,20 × 2,4909 = − 0,3308 + 0,3471 + 0,4982 = **0,51 M€**.
- Variance = 0,30 × (− 1,6170)² + 0,50 × 0,1797² + 0,20 × 1,9764² = 0,7845 + 0,0161 + 0,7812 = 1,5818 ; **écart-type = 1,26 M€**.

**Probabilité d'une VAN négative et indice de profitabilité (0,5 pt).**
- La VAN n'est négative que dans le scénario faible : probabilité **30 %**.
- IP = 1 + 0,5145 / 2,50 = **1,21** : chaque euro investi rapporte en espérance 1,21 € de valeur actuelle. On obtient le même résultat en actualisant le flux espéré (0,30 × 0,35 + 0,50 × 0,80 + 0,20 × 1,25 = 0,755 M€ par an, soit une valeur actuelle de 3,0145 M€), la VAN étant linéaire dans les flux.

**Lecture du risque (0,5 pt).**
- L'espérance est positive mais faible au regard de la dispersion : l'écart-type (1,26 M€) vaut près de deux fois et demie l'espérance (coefficient de variation d'environ 2,4, calcul facultatif). Le résultat dépend surtout de la fréquence des incidents.
- Le programme crée de la valeur dès que le groupe subirait, sans lui, plus de 0,81 incident significatif par an environ (flux annuel d'équilibre : 2,50 / 3,9927 = 0,63 M€ ; calcul facultatif). Le scénario central (1,0) est au-dessus, le scénario faible (0,5) en dessous.
- Limites : probabilités et fréquences estimées avec l'assureur, sur un risque qui évolue vite ; coût moyen d'un incident après assurance supposé constant alors qu'ALCERNE annonce une franchise doublée ; horizon de cinq ans sans valeur résiduelle, alors que les procédures mises en place (double validation, contre-appel) dureront au-delà.

**Recommandation (1 pt).**
- **Engager le programme.** En espérance, il crée 0,51 M€ de valeur (IP de 1,21) ; le scénario défavorable (− 1,10 M€, probabilité de 30 %) correspond à un groupe peu attaqué, ce qui n'est pas la situation observée en 2027.
- **Les éléments non chiffrés vont dans le même sens et pèsent davantage** :
  - **assurabilité** : sans mesures, ALCERNE doublerait la franchise (1,00 M€) et pourrait exclure la fraude au virement ; le coût d'un incident restant à charge augmenterait alors fortement, ce qui relève la VAN de tous les scénarios ;
  - **financement** : un nouvel incident en 2027 ou 2028 ferait de nouveau franchir le seuil de la clause financière (question 2.1) ; les banques attendent des mesures ;
  - **continuité de l'activité** : le site marchand pèse le quart du chiffre d'affaires et les franchisés dépendent des outils de commande ;
  - **réputation, conformité et mission** : après une fraude relayée par la presse, la confiance des clients, des franchisés et des investisseurs est en jeu ; le programme sert aussi le dispositif Sapin II (contrôles des paiements, question 2.3) et la raison d'être.
- **Conditions** : mettre en place immédiatement les mesures peu coûteuses (double validation et contre-appel de tout changement de coordonnées bancaires, séparation des tâches) ; négocier avec ALCERNE le maintien de la franchise et des garanties en contrepartie du programme ; suivre chaque année, devant le comité d'audit, le nombre d'incidents et les pertes évitées.

**Réponses tolérées** : VAN calculées avec un facteur arrondi (3,99) et résultats arrondis à 0,01 près ; écart-type calculé à partir des VAN arrondies (1,26) ; IP calculé comme valeur actuelle espérée des flux / investissement (3,0145 / 2,50 = 1,21) ; IP de 1,20 obtenu à partir de l'espérance arrondie (1 + 0,51 / 2,50), noté comme 1,21 ; recommandation de refus si elle est argumentée par la dispersion et la probabilité de 30 %, et accompagnée des mesures non coûteuses — 2.6-07 est alors noté à moitié au plus si les éléments non chiffrés de l'annexe 2.6 sont ignorés.

**Erreurs fréquentes**
- Oublier l'économie d'impôt sur l'amortissement, ou ne pas imposer les pertes évitées et la baisse de la prime.
- Calculer l'écart-type avec n − 1 ou sans pondérer par les probabilités : la variance est pondérée par les probabilités des scénarios (annexe 2.7).
- `JUR-T04` — erreur de facteur d'actualisation ou d'annuité, acquis du DCG.
- `JUR-T13` — conclure sur la seule espérance de la VAN sans intégrer le risque (écart-type, probabilité de perte) ni les éléments non chiffrés.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 60-63 | morale, éthique, déontologie, conformité ; LCB-FT (vigilance, déclaration de soupçon, connaissance du client, Tracfin) ; fraude et corruption, sans analyse de droit pénal ; risque cyber, services de l'État, MiCA, approche non technique | [V] | F09 § 0 ; `perimetre_ue2.yaml` 2.2 |
| Guide pédagogique DSCG, juillet 2026, p. 81 | scénarios probabilisés, espérance et écart-type de la VAN, indice de profitabilité | [V] | `perimetre_ue2.yaml` 7.1 |
| Loi n° 2016-1691 du 9 décembre 2016 (Sapin II), article 17 | seuils (500 salariés, 100 M€), huit mesures, contrôle de l'AFA, sanctions pécuniaires | [V] | fiche commune § 1.2 ; F09 § 4.2 |
| Loi n° 2017-399 du 27 mars 2017 (devoir de vigilance) | seuils de 5 000 et 10 000 salariés sur deux exercices, plan de vigilance | [V] | fiche commune § 1.3 et § 4 point 1 |
| Dispositif LCB-FT : liste des assujettis (experts-comptables), déclaration de soupçon, Tracfin | assujettissement du cabinet, déclaration au service de renseignement financier, confidentialité | [V] liste des assujettis, déclaration et Tracfin ; [S] vigilance, confidentialité, droit d'opposition | fiche commune § 2 ; F09 § 3 |
| Règlement (UE) 2023/1114 (MiCA) ; communiqué de l'AMF du 06/07/2026 | agrément des prestataires de services sur crypto-actifs, application depuis le 30/12/2024, fin de la période transitoire le 01/07/2026 | [V] | fiche commune § 3 |
| Décret n° 2009-834 du 7 juillet 2009 (ANSSI) | rattachement et missions de l'ANSSI | [V] | F09 § 5.2 |
| DGSI, COMCYBER-MI, SISSE, Cybermalveillance.gouv.fr | rôles résumés | [S] | F09 § 5.2 |
| Cressey (triangle de la fraude), facultatif | pression, opportunité, rationalisation | [S] | F09 § 4.1 |
| André Comte-Sponville, facultatif | hiérarchie des ordres, barbarie | [V programme 2.2] | F10 ; F09 § 1 |
| Sujet zéro 2027, dossier 2 (guide p. 86-88 et 102-105) | chiffrage d'un incident, distinction des décaissements et des pertes ; non reproduit (pas de rançongiciel ni de rançon dans ce dossier) | [V] | F09 § 5.1 et § 7 |
| Taux d'actualisation de 8 %, scénarios, conditions d'assurance | hypothèses d'énoncé | — | annexes 2.2, 2.6, 2.7 |
