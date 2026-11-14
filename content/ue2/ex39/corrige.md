# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 39 — Dossier 3 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F06 marchés et finance comportementale, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (espérances, écarts types, covariance, bêta et décomposition du risque de l'action, écart type du patrimoine de la holding dans ses deux compositions, rentabilité exigée par le MEDAF et par le modèle à trois facteurs, rentabilité implicite de Gordon-Shapiro, barème, liste noire, hors-programme ; rentabilités du jour de l'annonce, taux de distribution et montants du dividende vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une rentabilité exigée fondée sur un bêta erroné, ou une décomposition du risque fondée sur un écart type erroné).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Réaction des deux titres le jour de l'annonce et efficience | `5.1.c` Maîtriser les grands enseignements de l'efficience informationnelle des marchés (Fama, 1970) | 1,5 |
| 3.2 Biais comportementaux et conséquences pour l'offre | `5.1.d` Maîtriser les grands enseignements de la finance comportementale | 1,5 |
| 3.3 Espérance, écart type, covariance et bêta | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier | 3 |
| 3.4 Rentabilité exigée : MEDAF et modèle à trois facteurs | `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance ; `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché | 3 |
| 3.5 Rentabilité implicite dans le cours (Gordon-Shapiro) | `5.2.b` ; `5.2.a` | 2 |
| 3.6 Proposition de dividende et financement de l'offre | `4.1.a` Déchiffrer la politique de dividende et les signaux associés | 3 |
| 3.7 Risque de l'action et concentration du patrimoine familial | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) | 3 |
| **Total** | | **17** |

Part du calcul : environ 8 points (3.1-01, la moitié de 3.1-03, 3.3-01 à 3.3-03, 3.4-01, 3.4-02, 3.5-01, 3.6-01, 3.7-01 et 3.7-02). Part de l'analyse : environ 9 points. Ce dossier, placé en fin d'épreuve, rapporte autant qu'un dossier calculatoire : il ne doit pas être bâclé faute de temps (`JUR-T15`).

---

### 3.1 Réaction des deux titres le jour de l'annonce et efficience (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Séance du 6 avril : indice + 0,50 % ; VAUDRAN & Cie − 4,00 % observée, + 0,45 % expliquée, écart − 4,45 % ; AUDIVERNE + 20,00 % observée, + 0,60 % expliquée, écart + 19,40 % | 0,5 |
| 3.1-02 | Lecture au sens semi-fort : ajustement en une séance, sans dérive ; baisse de l'initiatrice (doute sur la valeur créée, prime transférée à la cible) ; cours de la cible sous la valeur de l'offre | 0,5 |
| 3.1-03 | Hausse d'AUDIVERNE avant l'annonce (+ 6,28 % contre + 0,51 % pour l'indice, volumes 2,5 à 4,7 fois la moyenne) : fuite ou anticipation ; efficience forte non vérifiée | 0,5 |

**Rentabilités de la séance du 6 avril 2027 (0,5 pt).**

| | VAUDRAN & Cie | AUDIVERNE |
|---|---:|---:|
| Rentabilité observée | 40,80 / 42,50 − 1 = **− 4,00 %** | 30,48 / 25,40 − 1 = **+ 20,00 %** |
| Rentabilité de l'indice | 7 879,20 / 7 840,00 − 1 = + 0,50 % | + 0,50 % |
| Rentabilité qu'expliquerait le marché (bêta × indice) | 0,90 × 0,50 % = **+ 0,45 %** | 1,20 × 0,50 % = **+ 0,60 %** |
| **Écart attribuable à l'annonce** | **− 4,45 %** | **+ 19,40 %** |

Rapportés aux capitalisations de la veille (8 000 000 × 42,50 = 340,00 M€ ; 3 600 000 × 25,40 = 91,44 M€), ces écarts représentent environ − 15,13 M€ pour les actionnaires de VAUDRAN & Cie et + 17,74 M€ pour ceux d'AUDIVERNE (calculs facultatifs) : le marché estime que l'opération crée peu de valeur au total (+ 2,61 M€) et que l'essentiel de ce que gagnent les actionnaires de la cible est perdu par ceux de l'initiatrice.

**Lecture au sens semi-fort (0,5 pt).** Selon Fama (1970), un marché efficient au sens semi-fort intègre toute l'information publique dès sa publication.
- Les deux cours s'ajustent dès la séance de l'annonce, avec un volume exceptionnel (310 000 actions AUDIVERNE, plus de cinquante fois la moyenne), puis restent à peu près stables : AUDIVERNE évolue entre 30,48 € et 30,75 € ; VAUDRAN & Cie recule encore de 1,96 % de J à J+5, alors que l'indice baisse de 0,99 % : environ la moitié de ce recul s'explique par le marché, le reste peut traduire un ajustement prolongé (question 3.2). Ce profil est compatible avec l'efficience semi-forte : la réaction mesure l'information nouvelle contenue dans l'annonce.
- **Baisse de l'initiatrice** : le marché révise la valeur de VAUDRAN & Cie, pas seulement par réflexe. Il doute que les synergies, non chiffrées par la gérance, justifient le prix offert ; il anticipe une dette supplémentaire de 50 M€ et l'émission d'actions nouvelles ; il intègre le risque que l'initiatrice paie trop cher une cible qu'elle connaît moins bien que ses dirigeants (asymétrie d'information, Akerlof, 1970). Ce constat est fréquent pour les initiateurs d'offres publiques.
- **Hausse de la cible** : AUDIVERNE ne monte pas jusqu'à la valeur de l'offre. Au cours de VAUDRAN & Cie du jour, l'offre vaut 18,00 + 40,80 / 3 = 31,60 € ; le 13 avril, 18,00 + 40,00 / 3 = 31,33 €, pour un cours de 30,70 € (calculs facultatifs). L'écart rémunère le risque d'échec de l'offre et le délai jusqu'au règlement ; comme une partie du prix est payée en actions, la valeur offerte baisse avec le cours de l'initiatrice.

**Avant l'annonce (0,5 pt).** Du 30 mars au 5 avril, AUDIVERNE passe de 23,90 € à 25,40 € (+ 6,28 %) alors que l'indice progresse de 0,51 %, avec des volumes de 14 000 à 26 000 actions, soit 2,5 à 4,7 fois la moyenne de 5 500 actions, sans information publiée. Deux lectures :
- certains investisseurs ont utilisé une information non publique (fuite lors de la préparation de l'offre) : le cours n'en a intégré qu'une petite partie (+ 6,28 %), puisqu'il a encore bondi de 20 % le jour de la publication ; ceux qui la détenaient ont pu acheter sous la valeur de l'offre et réaliser un gain. Si le marché était efficient au sens fort, toute l'information, même privée, serait déjà dans les cours : AUDIVERNE aurait atteint la valeur de l'offre avant l'annonce, et la séance du 6 avril n'aurait pas connu ce saut. L'**efficience au sens fort** n'est donc pas vérifiée ;
- ou le marché a anticipé l'opération à partir d'indices publics (rumeurs, rapprochement attendu dans le secteur) : la hausse resterait compatible avec l'efficience semi-forte.
Le volume anormal plaide pour la première lecture, sans la prouver ; quelques séances ne permettent pas de conclure sur l'efficience d'un marché.

**Réponses tolérées** : écart calculé en différence de rentabilités sans le libellé « attribuable à l'annonce » ; efficience semi-forte jugée « non contredite » plutôt que « vérifiée » ; recul de VAUDRAN & Cie après J interprété comme une réaction prolongée (lecture comportementale, question 3.2) ; mention de la « malédiction du vainqueur » ou de l'*hubris* des dirigeants (Roll, 1986, référence facultative) pour expliquer la baisse de l'initiatrice ; constat que la forme forte n'est pas vérifiée, justifié par le saut de 20 % du 6 avril ou par le gain possible des détenteurs de l'information.

**Erreurs fréquentes**
- Calculer la rentabilité de la séance par rapport au cours de J−5 ou au cours moyen des trois mois ; oublier de retrancher la rentabilité expliquée par le marché.
- Utiliser pour la question 3.1 le bêta annuel de la question 3.3, contrairement à l'énoncé.
- Comparer le cours d'AUDIVERNE au prix de 32,00 € sans voir que la part en actions vaut moins de 14,00 € après la baisse de VAUDRAN & Cie.
- Développer le régime juridique des informations privilégiées ou la procédure de l'offre : hors programme (UE 1).
- `JUR-M01` — analyse de la réaction sans référence à l'efficience (Fama, 1970).

---

### 3.2 Biais comportementaux et conséquences pour l'offre (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Excès de confiance des dirigeants de l'initiatrice, appuyé sur les propos de M. Arnaud VAUDRAN | 0,5 |
| 3.2-02 | Ancrage (et aversion aux pertes) des actionnaires d'AUDIVERNE ; mimétisme des gérants et des actionnaires individuels | 0,5 |
| 3.2-03 | Conséquences nuancées pour l'offre | 0,5 |

**Excès de confiance des dirigeants (0,5 pt).** La finance comportementale (Kahneman et Tversky, 1973) montre que les décideurs recourent à des heuristiques qui produisent des biais systématiques. M. Arnaud VAUDRAN se dit plus compétent que quiconque, promet des synergies « dès la première année » sans les chiffrer et extrapole deux petites acquisitions réussies à une opération dix fois plus grosse : c'est un **excès de confiance** (surestimation de ses compétences et de la précision de ses prévisions), renforcé par une généralisation à partir de deux cas peu comparables (représentativité). Les dirigeants acquéreurs trop confiants tendent à surpayer leurs cibles ; la baisse du cours de l'initiatrice (question 3.1) traduit ce soupçon.

**Ancrage et mimétisme (0,5 pt).**
- **Ancrage** : l'actionnaire qui refuse d'apporter à 32 € parce qu'il a acheté à 36 € et que le titre a valu 38 € prend un prix passé comme référence, alors que ce prix n'a pas d'influence sur la valeur actuelle de la société (Tversky et Kahneman, 1974). Il refuse aussi de constater une perte : **aversion aux pertes**, effet de disposition (Shefrin et Statman, 1985, facultatif).
- **Mimétisme** : Mme BRIVADIER vend parce qu'elle a vu les grands fonds vendre ; sur le forum, on garde ses titres « comme les autres », dans l'attente d'une surenchère que rien n'annonce. Les erreurs individuelles ne se compensent plus : elles s'additionnent. La formule « l'acheteur paie toujours trop cher » relève d'une règle simple appliquée sans examen du cas (simplexité, Berthoz, 2009, ou représentativité).
- La préférence pour un paiement « tout en numéraire » après la baisse du titre VAUDRAN relève du cadrage (comptabilité mentale, Thaler, 1985, facultatif).

**Conséquences nuancées pour l'offre (0,5 pt).**
- **Risques** : le mimétisme peut amplifier la baisse de VAUDRAN & Cie au-delà de ce que justifie l'information, ce qui réduit la valeur de la part payée en actions et donc l'attrait de l'offre ; les actionnaires ancrés sur 36 ou 38 € peuvent refuser d'apporter et faire échouer l'offre si elle exige un nombre minimal de titres ; la gérance, trop confiante, pourrait être tentée de relever son prix pour vaincre ces résistances et accroître la valeur transférée à la cible.
- **Nuances** : le fondateur s'est engagé à apporter ses 24 % ; les investisseurs qui achètent AUDIVERNE à 30,70 € pour apporter à l'offre (31,33 €) jouent le succès de l'opération, et le faible écart montre que le marché ne croit guère à une surenchère ; un marché efficient corrige en général les excès des investisseurs individuels. Les biais n'invalident donc pas l'offre, mais ils plaident pour une communication chiffrée des synergies et du plan de désendettement, et pour la discipline de prix de la gérance.

**Réponses tolérées** : biais de disponibilité pour la réaction à la baisse de 4 % de la première séance ; biais de confirmation chez le dirigeant ; mention de la sur-réaction (De Bondt et Thaler, 1985, facultatif) ; toute nuance fondée sur l'engagement du fondateur ou sur le paiement en partie en numéraire.

**Erreurs fréquentes**
- Réciter une liste de biais sans les rattacher aux propos cités (`JUR-T13`).
- Attribuer la finance comportementale à Fama, ou commettre les autres erreurs d'attribution relevées dans F10 et F99.
- Conclure que les biais rendent l'offre impossible, sans tenir compte de l'engagement du fondateur.

---

### 3.3 Espérance, écart type, covariance et bêta (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Espérances : VAUDRAN & Cie 9,00 % ; marché 8,00 % | 0,5 |
| 3.3-02 | Variances 0,0400 et 0,0225 ; écarts types 20,00 % et 15,00 % (n − 1) | 1 |
| 3.3-03 | Covariance 0,0180 ; bêta = 0,0180 / 0,0225 = 0,80 | 1 |
| 3.3-04 | Interprétation du bêta et de sa fiabilité | 0,5 |

**Calculs (2,5 pts).** Espérance de VAUDRAN & Cie : (25,0 + 13,4 − 29,4 + 6,2 + 15,8 + 23,0) / 6 = 54,0 / 6 = **9,00 %** ; marché : (5,5 − 6,5 − 12,5 + 19,5 + 24,0 + 18,0) / 6 = 48,0 / 6 = **8,00 %**.

| Année | Écart V (points) | Écart M (points) | Écart V² | Écart M² | Écart V × écart M |
|---|---:|---:|---:|---:|---:|
| 2021 | 16,0 | − 2,5 | 256,00 | 6,25 | − 40,00 |
| 2022 | 4,4 | − 14,5 | 19,36 | 210,25 | − 63,80 |
| 2023 | − 38,4 | − 20,5 | 1 474,56 | 420,25 | 787,20 |
| 2024 | − 2,8 | 11,5 | 7,84 | 132,25 | − 32,20 |
| 2025 | 6,8 | 16,0 | 46,24 | 256,00 | 108,80 |
| 2026 | 14,0 | 10,0 | 196,00 | 100,00 | 140,00 |
| **Total** | 0 | 0 | **2 000,00** | **1 125,00** | **900,00** |

- Variance de l'action : 2 000 / 5 = 400 (%²) = **0,0400** ; écart type **20,00 %**.
- Variance du marché : 1 125 / 5 = 225 (%²) = **0,0225** ; écart type **15,00 %**.
- Covariance : 900 / 5 = 180 (%²) = **0,0180**.
- Bêta = covariance / variance du marché = 0,0180 / 0,0225 = **0,80**.

**Interprétation (0,5 pt).**
- Le bêta mesure la sensibilité de la rentabilité de l'action à celle du marché : quand le marché varie de 1 %, l'action varie en moyenne de 0,80 %. L'action est **moins sensible au marché** que la moyenne des actions (bêta inférieur à 1), ce qui est cohérent avec une demande d'instruments de musique moins liée à la conjoncture que celle de nombreuses industries.
- Pourtant, l'action est plus volatile que le marché (20 % contre 15 %) : une grande part de son risque ne vient pas du marché mais de la société elle-même (question 3.7).
- **Fiabilité** : six observations seulement ; l'année 2023 (− 29,4 % pour l'action, − 12,5 % pour le marché) apporte à elle seule 787,20 des 900,00 points de la somme des produits ; le bêta quotidien de l'annexe 3.1 (0,90) diffère du bêta annuel. Le bêta est une estimation historique, fragile, établie avant l'acquisition.

**Réponses tolérées** : calculs en pourcentage (variance 400 %², covariance 180 %²) ; corrélation de 0,60 (0,0180 / (0,20 × 0,15)) calculée à titre de commentaire, facultative ; écarts types notés σ.

**Erreurs fréquentes**
- Diviser par n (6) au lieu de n − 1 (5) contrairement à l'énoncé : variance du marché 0,01875, covariance 0,0150 ; le bêta reste 0,80 si la même convention est appliquée aux deux termes, mais les écarts types sont faux (18,26 % et 13,69 %).
- Diviser la covariance par la variance de l'action (0,0180 / 0,0400 = 0,45) ou par l'écart type du marché.
- Calculer le bêta par une autre méthode que la covariance et la variance : seul ce calcul est attendu.
- Interpréter un bêta inférieur à 1 comme un titre « peu risqué » sans regarder son écart type.

---

### 3.4 Rentabilité exigée : MEDAF et modèle à trois facteurs (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | MEDAF : 4,0 % + 0,80 × 5,0 % = 8,00 % | 0,5 |
| 3.4-02 | Trois facteurs : 8,00 % + 0,50 × 2,0 % + 0,20 × 2,5 % = 9,50 % | 0,5 |
| 3.4-03 | Explication de l'écart de 1,50 point : taille et valeur, risques que le bêta ne capte pas | 0,5 |
| 3.4-04 | Ce que mesure la prime de risque | 0,5 |
| 3.4-05 | Limites du MEDAF appliquées au cas | 1 |

**Calculs (1 pt).**
- MEDAF (Sharpe, 1964) : rentabilité exigée = 4,0 % + 0,80 × 5,0 % = **8,00 %**.
- Modèle à trois facteurs (Fama et French, 1993) : 4,0 % + 0,80 × 5,0 % + 0,50 × 2,0 % + 0,20 × 2,5 % = 8,00 % + 1,00 % + 0,50 % = **9,50 %**.

**Explication de l'écart (0,5 pt).** Le modèle à trois facteurs ajoute au risque de marché deux sources de rentabilité que le MEDAF ignore : la **taille** (les petites capitalisations ont historiquement procuré une rentabilité supérieure à celle des grandes) et la **valeur** (les actions dont la valeur comptable est élevée par rapport à la capitalisation ont fait mieux que les actions « de croissance »). VAUDRAN & Cie, dont la capitalisation est de l'ordre de 320 M€ au cours de 40,00 €, est sensible au facteur de taille (0,50), plus faiblement au facteur de valeur (0,20) : elle supporte des risques (liquidité du titre, dépendance à quelques marchés, fragilité d'une valeur moyenne) que l'investisseur exige de voir rémunérés, d'où 1,50 point de plus.

**La prime de risque (0,5 pt).** La prime de risque est le supplément de rentabilité que les investisseurs exigent pour détenir un actif risqué plutôt qu'un actif sans risque : 5,0 % pour le marché, 0,80 × 5,0 % = 4,0 % pour l'action VAUDRAN & Cie. Plus l'incertitude sur les flux futurs est grande, plus la rentabilité exigée est élevée. Dans le MEDAF, seule la part du risque liée au marché (risque systématique) est rémunérée, parce que l'investisseur diversifié élimine le reste. Pour la gérance, cette rentabilité exigée est le coût des capitaux propres : un projet, comme l'acquisition d'AUDIVERNE, ne crée de valeur pour les actionnaires que s'il rapporte au moins ce taux.

**Limites du MEDAF (1 pt).**
- **Hypothèses** : marchés parfaits et efficients, investisseurs rationnels et **diversifiés**, emprunt et prêt possibles au taux sans risque, horizon d'une période ; or la première actionnaire, VAUDRAN Participations, est très peu diversifiée (question 3.7).
- **Un seul facteur** : le bêta n'explique pas tout l'écart de rentabilité entre les titres ; les anomalies de taille et de valeur ont conduit au modèle à trois facteurs, qui donne ici 1,50 point de plus.
- **Estimation du bêta** : six observations annuelles dominées par l'année 2023 ; 0,80 en données annuelles contre 0,90 en données quotidiennes (annexe 3.1) ; bêta historique, mesuré avant une acquisition qui modifie le profil de risque (part plus forte du matériel audio, plus sensible à la conjoncture des salles et des studios ; endettement accru, qui augmente le risque supporté par les actionnaires).
- **Paramètres** : taux sans risque et prime de marché sont des estimations ; avec une prime de 4 % ou de 6 %, la rentabilité exigée varie de 7,20 % à 8,80 % (calcul facultatif).
- Le modèle à trois facteurs a ses propres limites : primes des facteurs instables, sensibilités estimées, et, dans l'énoncé, sensibilité au marché prise égale au bêta du MEDAF par simplification.

**Réponses tolérées** : rentabilité exigée notée ke ou k ; MEDAF présenté sous la forme E(R) = rf + β [E(Rm) − rf] avec E(Rm) = 9 % ; mention de primes additives de taille ou d'illiquidité comme traduction pratique du modèle à trois facteurs ; calcul de la rentabilité exigée avec le bêta quotidien (8,50 %) en complément, si le candidat discute le choix.

**Erreurs fréquentes**
- Multiplier le bêta par la rentabilité du marché au lieu de la prime de risque (4,0 % + 0,80 × 9,0 % = 11,20 %).
- Ajouter les primes des facteurs sans les multiplier par les sensibilités (8,00 % + 2,0 % + 2,5 % = 12,50 %).
- Prétendre estimer les sensibilités aux facteurs : elles sont fournies.
- `JUR-T14` — limites du MEDAF récitées sans lien avec VAUDRAN & Cie et l'acquisition.

---

### 3.5 Rentabilité implicite dans le cours (Gordon-Shapiro) (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Rentabilité implicite = 1,10 / 40,00 + 5,0 % = 2,75 % + 5,00 % = 7,75 % | 0,5 |
| 3.5-02 | Comparaison avec 8,00 % et 9,50 % et conclusion (croissance implicite ou valeurs théoriques à l'appui) | 1 |
| 3.5-03 | Limites du modèle de Gordon-Shapiro dans le cas | 0,5 |

**Calcul (0,5 pt).** Du modèle de Gordon-Shapiro, cours = prochain dividende / (k − g), on tire k = prochain dividende / cours + g = 1,10 / 40,00 + 5,0 % = 2,75 % + 5,00 % = **7,75 %**. Un investisseur qui achète l'action au cours du 13 avril 2027 et dont les anticipations sont celles des analystes obtient une rentabilité annuelle de 7,75 % : 2,75 % de rendement du dividende et 5,00 % de croissance.

**Comparaison et conclusion (1 pt).**
- La rentabilité implicite (7,75 %) est **inférieure** à la rentabilité exigée selon le MEDAF (8,00 %, écart de 0,25 point) et nettement inférieure à celle du modèle à trois facteurs (9,50 %, écart de 1,75 point). Au cours de 40,00 €, l'acheteur accepte une rentabilité plus faible que celle que justifie le risque : l'action paraît plutôt chère.
- Autre lecture : le cours suppose une croissance du dividende supérieure à 5,0 %. Pour obtenir 8,00 %, il faut une croissance de 8,00 % − 2,75 % = 5,25 % ; pour 9,50 %, une croissance de 6,75 %, peu plausible à l'infini (calculs facultatifs). Valeurs théoriques correspondantes : 1,10 / (8,00 % − 5,0 %) = 36,67 € et 1,10 / (9,50 % − 5,0 %) = 24,44 € (facultatif).
- **Conclusion** : avec le MEDAF, l'écart (0,25 point) reste dans la marge d'erreur des estimations : le cours est à peu près cohérent avec les hypothèses des analystes, même après la baisse qui a suivi l'annonce (la rentabilité implicite était de 7,59 % au cours de 42,50 € de la veille, facultatif). Avec le modèle à trois facteurs, le cours serait nettement surévalué, sauf à croire à une croissance durable de près de 7 %. Le verdict dépend du modèle de rentabilité exigée retenu, ce qui invite à la prudence.

**Limites (0,5 pt).** Croissance constante à l'infini, alors que 5,0 % dépasse sans doute la croissance nominale de l'économie à long terme ; très forte sensibilité de la valeur à l'écart k − g (au taux de 8,00 %, une variation de g de 0,5 point fait varier la valeur théorique de 14 à 20 % : 31,43 € pour 4,5 %, 44,00 € pour 5,5 %) ; dividende de 1,10 € encore à décider (question 3.6) ; croissance attendue établie avant de connaître les synergies et le coût de l'intégration d'AUDIVERNE.

**Réponses tolérées** : rentabilité implicite calculée au cours de J−1 ou de J si le candidat le justifie, sans pénalité sur la comparaison ; conclusion « cours cohérent avec le MEDAF » ou « action légèrement surévaluée », si elle est argumentée.

**Erreurs fréquentes**
- Faire croître une seconde fois le dividende proposé (1,10 × 1,05 = 1,155 €), alors qu'il est déjà le prochain dividende : 7,89 %.
- Calculer une valeur théorique sans comparer les rentabilités demandées.
- Utiliser une rentabilité exigée inférieure ou égale au taux de croissance.

---

### 3.6 Proposition de dividende et financement de l'offre (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Taux de distribution 2020-2026 ; dividende 2026 : 8,80 M€ à 1,10 €, 4,40 M€ à 0,55 € ; économie de 4,40 M€, soit 6,79 % de la part en numéraire | 1 |
| 3.6-02 | Caractérisation de la politique, signal et effet cliquet appuyés sur 2023 | 0,5 |
| 3.6-03 | Neutralité (Modigliani et Miller, 1961) et frictions, dont les coûts d'agence propres à la SCA | 1 |
| 3.6-04 | Réaction probable du marché à une baisse et recommandation | 0,5 |

**Calculs (1 pt).**

| Exercice | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Taux de distribution | 60,7 % | 58,1 % | 58,6 % | **95,0 %** | 65,8 % | 61,8 % | **54,2 %** |

- Dividende au titre de 2026 proposé par la gérance : 8 000 000 × 1,10 = **8,80 M€** (hausse de 4,76 % du dividende par action).
- Dividende suggéré par M. ESCARVEL : 8 000 000 × 0,55 = **4,40 M€** (taux de distribution 27,1 %).
- Économie de trésorerie : **4,40 M€**, soit 4,40 / 64,8 = **6,79 %** de la part en numéraire de l'offre (8,80 % de la nouvelle dette de 50 M€, facultatif).
- Repères facultatifs : croissance annuelle moyenne du dividende de 2020 à 2026 : (1,10 / 0,85)^(1/6) − 1 = 4,39 % ; taux de distribution moyen 64,9 % ; rendement du dividende au cours du 13 avril : 2,75 %.

**Politique, signal et effet cliquet (0,5 pt).**
- La politique est celle d'un **dividende stable et régulièrement croissant** (+ 0,05 € par an), lissé par rapport à des bénéfices plus irréguliers (Lintner, 1956, référence facultative). En 2023, le bénéfice par action a chuté de 38 % et la gérance a maintenu le dividende, au prix d'un taux de distribution de 95,0 % : c'est l'**effet cliquet**, la réticence à baisser un dividende une fois atteint, que le marché a appris à attendre.
- **Signal** (Spence, 1973 ; Ross, 1977) : les dirigeants connaissent mieux que le marché les flux futurs. Maintenir la progression du dividende au moment où le groupe s'endette est un signal coûteux, donc crédible : la gérance montre qu'elle compte sur des flux suffisants pour servir la dette et le dividende. Le taux de distribution de 2026 (54,2 %) est le plus bas de la période : la hausse est couverte par la croissance des bénéfices (+ 19,4 % de bénéfice par action).

**Neutralité et frictions (1 pt).**
- **Neutralité** (Modigliani et Miller, 1961) : sur un marché parfait, la politique de dividende ne modifie pas la valeur de l'action ; ce que l'actionnaire reçoit en dividende, il le perd en valeur du titre, et il peut se créer lui-même un revenu en cédant des actions. Verser 1,10 € et emprunter 4,40 M€ de plus, ou verser 0,55 € et emprunter moins, serait indifférent.
- **Frictions** qui rendent le choix important : coûts de transaction du « dividende maison » ; imposition du dividende chez l'actionnaire (non développée) ; asymétrie d'information, d'où le signal ; et surtout **coûts d'agence** (Jensen et Meckling, 1976).
- **Coûts d'agence dans une SCA** : les associés commanditaires ne peuvent pas révoquer le gérant, et l'achat de la majorité des actions ne donne pas le contrôle de la gestion ; les mécanismes habituels de discipline des dirigeants (vote, menace d'une prise de contrôle) ne jouent pas. Le dividende devient l'un des rares moyens de limiter la trésorerie laissée à la discrétion d'une gérance inamovible, tentée par la croissance externe et les projets de prestige. M. ESCARVEL le dit lui-même, mais sa proposition semble contredire son argument, puisque réduire le dividende laisse davantage de trésorerie à la gérance, sauf si l'économie sert à rembourser plus vite la dette de l'offre. Sa crainte porte en réalité sur le financement d'une acquisition par la dette ; or la dette, qu'il faudra rembourser, discipline aussi la gestion. La famille, qui détient 42 % des actions par la holding, perçoit le même dividende par action que le public : sur ce point, les intérêts de la commandité et des commanditaires convergent.

**Réaction à une baisse et recommandation (0,5 pt).**
- **Réaction probable** : une baisse de moitié, après une progression ininterrompue et un maintien même en 2023, serait lue comme l'aveu que la gérance doute de ses flux ou de l'opération ; les marchés réagissent en général plus fortement à une baisse qu'à une hausse du dividende. Une baisse du cours de quelques pour cent (5 % représenteraient 16 M€ de capitalisation au cours de 40,00 €) effacerait largement l'économie de 4,40 M€, au moment même où le cours de l'action détermine la valeur de la part de l'offre payée en actions.
- **Recommandation** : maintenir le dividende de 1,10 €, couvert par les bénéfices et modeste au regard du financement de l'offre, et l'accompagner d'une communication sur les synergies chiffrées et le calendrier de désendettement. Si la gérance veut marquer la prudence, un dividende stable à 1,05 € préserve l'effet cliquet sans envoyer de signal de rupture.

**Réponses tolérées** : taux de distribution à deux décimales ; recommandation d'un dividende de 1,05 € ou d'un dividende payable en actions, s'il est justifié ; recommandation d'une baisse si le candidat en mesure le signal négatif et propose une communication pour l'atténuer ; référence à Jensen (1986) sur les flux de trésorerie disponibles, facultative ; lecture selon laquelle la baisse du dividende sert à accélérer le désendettement, qui discipline aussi la gérance ; remarque, fondée sur le dossier 1, qu'un financement assorti d'un plafond de dividende pourrait interdire un taux de distribution supérieur à 50 % : non attendue, valorisée si elle est exacte.

**Erreurs fréquentes**
- Calculer le dividende total sur 9 200 000 actions en y incluant les actions nouvelles de l'offre, contrairement à l'hypothèse de l'annexe.
- Présenter la neutralité comme une démonstration (hors programme) ou en conclure que le dividende est sans importance pour la gérance.
- Évoquer les coûts d'agence de façon générique, sans le statut de SCA ni l'impossibilité de révoquer le gérant (`JUR-T13`).
- Développer le droit de la SCA ou l'imposition des dividendes : hors programme (UE 1).
- `JUR-I04` — ne pas opposer revenu immédiat des actionnaires et financement de la croissance.

---

### 3.7 Risque de l'action et concentration du patrimoine familial (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Risque systématique 0,80² × 0,0225 = 0,0144 (36,00 %), écart type 12,00 % ; spécifique 0,0256 (64,00 %), écart type 16,00 % | 1 |
| 3.7-02 | Poids 80 % / 20 % puis 60 % / 40 % ; covariance 0,0075 ; écart type du patrimoine 17,00 % puis 14,70 % | 1 |
| 3.7-03 | Coût de la concentration, apport de la diversification, statut de SCA et signal d'une cession | 1 |

**Décomposition du risque de l'action (1 pt).** σ² = β² × σ²(marché) + σ²(spécifique).
- Variance totale : 0,20² = **0,0400**.
- Risque systématique : 0,80² × 0,0225 = 0,64 × 0,0225 = **0,0144**, soit **36,00 %** de la variance totale ; écart type 0,80 × 15 % = **12,00 %**.
- Risque spécifique : 0,0400 − 0,0144 = **0,0256**, soit **64,00 %** ; écart type √0,0256 = **16,00 %**.
- Près des deux tiers de la variance de l'action viennent de la société elle-même (prix du bois, ventes de pianos, intégration d'AUDIVERNE), et non du marché.

**Patrimoine de VAUDRAN Participations (1 pt).** Participation : 3 360 000 × 40,00 = 134,40 M€ ; fonds : 33,60 M€ ; total 168,00 M€. Covariance entre l'action et le fonds : 0,25 × 0,20 × 0,15 = **0,0075**.

| | Composition actuelle | Après la cession de 840 000 actions |
|---|---:|---:|
| Actions VAUDRAN & Cie (M€) | 134,40 | 100,80 |
| Fonds diversifié (M€) | 33,60 | 67,20 |
| Poids de l'action / du fonds | **80 % / 20 %** | **60 % / 40 %** |
| w² × 0,0400 | 0,0256 | 0,0144 |
| (1 − w)² × 0,15² = (1 − w)² × 0,0225 | 0,0009 | 0,0036 |
| 2w(1 − w) × 0,0075 | 0,0024 | 0,0036 |
| **Variance** | **0,0289** | **0,0216** |
| **Écart type** | **17,00 %** | **14,70 %** |
| Moyenne pondérée des écarts types (facultatif) | 19,00 % | 18,00 % |

**Analyse (1 pt).**
- **Ce que coûte la concentration** : selon le MEDAF, le marché ne rémunère que le risque systématique, parce que l'investisseur diversifié élimine le risque spécifique. La rentabilité exigée de 8,00 % rémunère un écart type de 12 % ; la holding, placée à 80 % sur l'action, supporte aussi les 16 % de risque spécifique, sans rémunération supplémentaire (environ 21,50 M€ d'écart type spécifique sur une participation de 134,40 M€, facultatif). S'y ajoutent la dépendance du patrimoine, des revenus et de l'histoire familiale à une seule entreprise, au moment où l'acquisition et la dette nouvelle en augmentent le risque.
- **Ce que change la diversification (Markowitz, 1952)** : parce que la corrélation (0,25) est faible, l'écart type du patrimoine (17,00 %) est déjà inférieur à la moyenne pondérée des écarts types (19,00 %) ; céder le quart de la participation le ramène à 14,70 %, soit 2,30 points de moins, en réduisant surtout le risque spécifique, qui n'est pas rémunéré. La diversification ne supprime pas le risque de marché.
- **Le contrôle de la gestion ne dépend pas de la part du capital** : dans la SCA, le gérant est nommé et révoqué par l'associée commandité, VAUDRAN Gérance SAS, détenue par la famille. Après la cession, la holding détiendrait 2 520 000 actions, soit 31,50 % du capital actuel, et la famille garderait la maîtrise de la gestion. La crainte de M. Arnaud VAUDRAN n'est pas fondée : la famille peut se diversifier à un coût plus faible que dans une société anonyme, où elle devrait conserver une participation élevée pour garder le pouvoir.
- **Nuances** : une cession par la famille juste après une offre payée en partie en actions peut être lue comme un signal défavorable (les initiés vendent ; Myers et Majluf, 1984 pour la lecture des émissions d'actions) : la cession doit intervenir après le règlement de l'offre, être expliquée par un motif patrimonial et réalisée auprès d'investisseurs de long terme. Moins investie, la famille supporterait une part plus faible des conséquences de ses décisions de gestion tout en les contrôlant : l'écart entre pouvoir et capital, donc le risque de coûts d'agence pour les commanditaires, augmenterait (Jensen et Meckling, 1976). L'attachement exprimé (« nos ancêtres ont tout misé ») relève en partie d'un biais de familiarité ou de statu quo. Une diversification partielle et progressive concilie la réduction du risque et l'engagement de la famille.

**Réponses tolérées** : poids et écarts types arrondis à une décimale ; décomposition présentée par les écarts types (12² + 16² = 20²) ; part systématique obtenue par le carré de la corrélation entre l'action et le marché (0,60² = 36 %) ; analyse qui propose une cession plus faible (par exemple 10 % de la participation) si elle est chiffrée ou justifiée.

**Erreurs fréquentes**
- Additionner les écarts types systématique et spécifique (12 % + 16 % = 28 %) au lieu des variances.
- Oublier le terme de covariance dans la variance du patrimoine (variance actuelle 0,0265, écart type 16,28 %) ou calculer l'écart type comme moyenne pondérée des écarts types.
- Calculer la covariance avec le coefficient de corrélation et les variances au lieu des écarts types.
- Affirmer que la famille perdrait le contrôle du groupe en passant sous un seuil de capital : c'est ignorer le statut de SCA.
- Calculer la part de la holding après l'offre ou développer les règles juridiques de la SCA : non demandé (UE 1).
- `JUR-T14` — citer Markowitz sans montrer l'effet de la corrélation sur les chiffres du cas.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 67-68 | dividende : signal, neutralité, effet cliquet, réactions des investisseurs, frictions (coûts d'agence) ; Modigliani et Miller limités à leurs grands enseignements | [V] | `perimetre_ue2.yaml` 4.1.a |
| Guide pédagogique DSCG, juillet 2026, p. 73-75 | efficience et ses trois formes, sans vérification chiffrée ; biais comportementaux ; rentabilité exigée, prime de risque, bêta, MEDAF et modèle à trois facteurs, Gordon-Shapiro | [V] | F06 § 3 et 4 ; F02 § 2, 6 et 7 ; `perimetre_ue2.yaml` 5.1.c à 5.2.c |
| Programme UE 2, l. 589-592 ; guide p. 76 | risque spécifique et systématique ; diversification, corrélation fournie | [V] | `perimetre_ue2.yaml` 5.3.a, 5.3.b |
| Fama (1970) | efficience informationnelle, trois formes | [V programme 5.1] | F10 § 1 ; F06 § 3 |
| Kahneman et Tversky (1973) ; Tversky et Kahneman (1974) | heuristiques et biais ; ancrage | [V programme 5.1] ; [S] | F10 § 1 ; F06 § 4.2 |
| Berthoz (2009) | simplexité | [V programme 5.1] ; contenu [S] | F10 § 1 |
| Akerlof (1970) | asymétrie d'information entre l'initiatrice et la cible | [V programme 5.1] | F10 § 1 |
| Sharpe (1964) | MEDAF | [V programme 5.2, sans année] | F10 § 2 ; F02 § 2 |
| Fama et French (1993) | modèle à trois facteurs : taille et valeur | [V programme 5.2] | F10 § 2 ; F02 § 7 |
| Gordon et Shapiro (1956) | rentabilité implicite k = prochain dividende / cours + g | [V programme 5.2, sans année] | F10 § 2 ; F02 § 6 |
| Markowitz (1952) | diversification, rôle de la corrélation | [V programme 5.3] | F10 § 2 |
| Modigliani et Miller (1961) | neutralité de la politique de dividende | [V programme 4.1] | F10 § 2 |
| Spence (1973) ; Ross (1977) | théorie du signal | [V programme 4.1] | F10 § 3 |
| Jensen et Meckling (1976) | coûts d'agence | [V programme 2.1] | F10 § 3 |
| Myers et Majluf (1984) | lecture d'une émission ou d'une cession d'actions par des initiés | [V programme 7.2] | F10 § 3 |
| Lintner (1956) ; Roll (1986) ; Shefrin et Statman (1985) ; Thaler (1985) ; De Bondt et Thaler (1985) ; Jensen (1986), facultatifs | lissage du dividende ; *hubris* des acquéreurs ; effet de disposition ; comptabilité mentale ; sur-réaction ; flux de trésorerie disponibles | [S] | F10 § 1 à 3 ; F06 § 4.2 |
| Taux sans risque 4,0 %, prime de risque du marché 5,0 % | hypothèses d'énoncé, plausibles fin 2026 | [V] pour l'OAT 10 ans de septembre 2026 (4,44 %) ; [S] pour la prime | F11 § 1 et 2 |
| Primes des facteurs de taille (2,0 %) et de valeur (2,5 %), sensibilités | hypothèses d'énoncé, aucune donnée de marché dans F11 | hypothèse | F02 § 7 |
