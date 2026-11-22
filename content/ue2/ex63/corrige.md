# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 63 — Dossier 3 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F02 coût du capital, F05 ingénierie financière, F06 marchés et finance comportementale, F10 auteurs et théories, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (VAN, TRI, indices de profitabilité, VAN globales et TRI globaux des projets A et B, VAN d'encadrement des TRI ; VAN des trois scénarios d'été, espérance, écart-type, coefficient de variation et probabilité d'une VAN négative du projet A ; VAN du désinvestissement par scénario et son espérance ; annuité et tableau d'amortissement de l'emprunt, coût actuariel avant et après IS ; coût des fonds propres ; actions nouvelles, montant net, décote, dilution et résultat par action de l'augmentation de capital ; résultat par action pro forma des solutions S1, S3 et de la combinaison recommandée ; barème, liste noire, hors-programme ; investissement du projet B, fonds libérés, seuil de probabilité des étés très chauds, rapports de la dette financière nette à l'EBITDA, sommes conservées, taux de distribution et variations du cours de SARTENAY Villages comparées à celles de l'indice vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VAN du projet B erronée à la question 3.1, reprise dans la VAN du désinvestissement à la question 3.4, ou un montant emprunté erroné à la question 3.5, repris dans le rapport de la dette à l'EBITDA et dans le résultat par action).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 VAN, TRI et indice de profitabilité des projets A et B, conflit de classement et explication | `7.1.a` Évaluer et classer des projets en milieu certain | 2,5 |
| 3.2 VAN globale et TRI global au taux de réinvestissement, projet retenu | `7.1.a` | 1 |
| 3.3 VAN du projet A dans trois scénarios d'été, espérance, écart-type, coefficient de variation, probabilité d'une VAN négative, risque comparé des deux projets | `7.1.b` Évaluer et classer des projets en milieu incertain | 2 |
| 3.4 Projet B lu comme un désinvestissement des thermes, VAN du désinvestissement par scénario, création de valeur et conclusion pour Lhérens | `7.1.c` Déterminer la création de valeur à travers la décision d'investissement ou de désinvestissement | 1,5 |
| 3.5 Coût de l'emprunt, des fonds propres et de l'autofinancement ; dette financière nette / EBITDA et résultat par action pro forma de trois solutions ; combinaison recommandée | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière | 3,5 |
| 3.6 Financement hiérarchique et théorie du compromis | `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives | 1 |
| 3.7 Taux de distribution, réaction du cours de SARTENAY Villages comparée à celle de l'indice, signal, effet cliquet, clientèles, coûts d'agence, neutralité, efficience, politique de dividende et communication | `4.1.a` Déchiffrer la politique de dividende et les signaux associés ; `5.1.c` Maîtriser les grands enseignements de l'efficience informationnelle des marchés | 4,5 |
| 3.8 Asymétrie d'information et annonce d'une augmentation de capital | `5.1.b` Maîtriser les enseignements des asymétries d'information | 1 |
| **Total** | | **17** |

Part du calcul : environ 8,5 points (3.1-01 à 3.1-03, 3.2-01, 3.3-01 et 3.3-02, 3.4-01 et 3.4-02, 3.5-01 à 3.5-04, 3.7-01 et 3.7-02). Part de l'analyse : environ 8,5 points. Les questions 3.6 à 3.8, en grande partie rédactionnelles, valent 6,5 points : elles ne doivent pas être sacrifiées faute de temps en fin d'épreuve (`JUR-T15`).

---

### 3.1 VAN, TRI et indice de profitabilité des projets A et B (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Flux : A − 16,00 à la date 0, 1,95 de 2028 à 2036, 15,95 en 2037 ; B : investissement net 8,10 − 3,20 + 2,10 = **7,00**, 1,25 de 2028 à 2036, 2,25 en 2037 ; VAN à 7 % : A **4,81 M€**, B **2,29 M€** | 0,75 |
| 3.1-02 | TRI par interpolation : A **11,47 %** (entre 11 % et 12 %), B **13,27 %** (entre 13 % et 14 %) | 0,75 |
| 3.1-03 | Indices de profitabilité : A **1,30**, B **1,33** | 0,25 |
| 3.1-04 | Conflit : la VAN classe A en tête, le TRI et l'indice de profitabilité classent B ; explication par la taille (16,00 contre 7,00), la chronologie des flux (valeur résiduelle de A) et l'hypothèse de réinvestissement implicite de chaque critère ; taux d'indifférence voisin de 10,50 % | 0,75 |

Les flux de chaque projet sont pris en totalité (annexe 3.1) : sans l'un des deux projets, la station ne fonctionnerait plus à partir de 2028, si bien que les VAN sont calculées par rapport à une station sans flux, et non en écart avec le flux de 2026.

**Flux des projets (M€).**

| Date | 0 (31/12/2027) | 2028 à 2036 (années 1 à 9) | 2037 (année 10) |
|---|---:|---:|---:|
| Projet A | − 16,00 | 1,95 | 1,95 + 14,00 = 15,95 |
| Projet B | − 8,10 + 3,20 − 2,10 = − 7,00 | 1,25 | 1,25 + 1,00 = 2,25 |

**VAN (0,75 pt).** Coefficients à 7 % : [1 − 1,07^−10] / 0,07 = 7,023582 ; 1,07^−10 = 0,508349.
- VAN(A) = 1,95 × 7,023582 + 14,00 × 0,508349 − 16,00 = 13,70 + 7,12 − 16,00 = **4,81 M€**.
- VAN(B) = 1,25 × 7,023582 + 1,00 × 0,508349 − 7,00 = 8,78 + 0,51 − 7,00 = **2,29 M€**.

**TRI (0,75 pt).**
- Projet A : VAN à 11 % = + 0,415 ; VAN à 12 % = − 0,474 (non exigées). TRI = 11 % + 0,415 / (0,415 + 0,474) × 1 % = **11,47 %**.
- Projet B : VAN à 13 % = + 0,077 ; VAN à 14 % = − 0,210. TRI = 13 % + 0,077 / (0,077 + 0,210) × 1 % = **13,27 %**.

**Indice de profitabilité (0,25 pt).** IP(A) = (4,81 + 16,00) / 16,00 = **1,30** ; IP(B) = (2,29 + 7,00) / 7,00 = **1,33**.

**Conflit et explication (0,75 pt).**

| Critère | Projet A | Projet B | Classement |
|---|---:|---:|---|
| VAN à 7 % | 4,81 | 2,29 | A |
| TRI | 11,47 % | 13,27 % | B |
| Indice de profitabilité | 1,30 | 1,33 | B |

Les deux projets sont acceptables isolément (VAN positives, TRI supérieurs au CMPC de 7 %), mais ils sont mutuellement exclusifs et les critères ne les classent pas de la même façon. Trois raisons :
- **la taille** : A engage 16,00 M€, B 7,00 M€. La VAN mesure une création de valeur en euros, le TRI et l'indice de profitabilité une rentabilité par euro investi. Un projet plus petit peut être plus rentable par euro et créer moins de valeur au total ;
- **la chronologie des flux** : 34 % de la valeur actuelle des flux de A vient de la valeur résiduelle de 2037 (7,12 sur 20,81), contre 5 % pour B (0,51 sur 9,29). Les flux de A sont plus tardifs : leur valeur actuelle baisse plus vite quand le taux monte, si bien que la VAN de A, plus forte à 7 %, s'annule à un taux plus faible ;
- **l'hypothèse de réinvestissement** : le TRI suppose implicitement que les flux intermédiaires sont réinvestis au TRI lui-même (13,27 % pour B), la VAN qu'ils le sont au taux d'actualisation (7 %). Les deux critères ne comparent donc pas les projets dans les mêmes conditions.

Le flux différentiel A − B (− 9,00 à la date 0, + 0,70 par an, + 13,70 en 2037) a un TRI voisin de **10,50 %** : c'est le taux d'indifférence, pour lequel les deux VAN sont égales. En dessous de ce taux, A a la VAN la plus forte ; au CMPC de 7 %, A l'emporte. La question 3.2 lève le conflit avec un taux de réinvestissement explicite.

**Réponses tolérées** : VAN de 4,81 ou 4,82 et de 2,28 ou 2,29 selon les arrondis ; TRI de 11,46 % et 13,26 % (TRI exact) ou de 13,28 % (VAN d'encadrement arrondies à deux décimales), et plus largement de 11,4 % à 11,5 % et de 13,2 % à 13,3 % selon les taux d'encadrement ; indice de profitabilité calculé sur l'investissement brut du projet B (8,10, si le candidat traite la cession et les coûts de sortie comme des flux distincts), soit 1,28 en cohérence, s'il est expliqué ; taux d'indifférence seulement évoqué, sans calcul.

**Erreurs fréquentes**
- Oublier la valeur résiduelle dans le flux de 2037, ou l'ajouter à chaque année.
- Retenir 8,10 M€ comme investissement de B en oubliant le prix de cession et les coûts de sortie de la date 0.
- Choisir B parce que son TRI est le plus élevé, sans discuter la taille des projets : `JUR-I05` — divergence VAN / TRI non analysée.
- Actualiser au coût des fonds propres plutôt qu'au CMPC donné.

---

### 3.2 VAN globale et TRI global (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Valeurs acquises en 2037 à 4 % : A 1,95 × 12,006107 + 14,00 = **37,41** ; B 1,25 × 12,006107 + 1,00 = **16,01** ; VAN globales : A **3,02 M€**, B **1,14 M€** ; TRI globaux : A **8,87 %**, B **8,62 %** | 0,75 |
| 3.2-02 | Conclusion : les deux critères globaux classent A en tête ; avec un taux de réinvestissement réaliste et sans rationnement du capital, A est retenu sur la base des flux de l'annexe 3.1 | 0,25 |

**Calcul (0,75 pt).** Coefficient de capitalisation de dix flux à 4 % : (1,04^10 − 1) / 0,04 = 12,006107. La valeur résiduelle, perçue en 2037, n'est pas capitalisée.

| M€ | Projet A | Projet B |
|---|---:|---:|
| Flux capitalisés en 2037 à 4 % | 1,95 × 12,006107 = 23,41 | 1,25 × 12,006107 = 15,01 |
| Valeur résiduelle | 14,00 | 1,00 |
| **Valeur acquise en 2037** | **37,41** | **16,01** |
| Valeur acquise actualisée à 7 % (× 0,508349) | 19,02 | 8,14 |
| **VAN globale** (− investissement) | **3,02** | **1,14** |
| **TRI global** = (valeur acquise / investissement)^(1/10) − 1 | (37,41 / 16,00)^0,1 − 1 = **8,87 %** | (16,01 / 7,00)^0,1 − 1 = **8,62 %** |

**Conclusion (0,25 pt).** Les VAN globales sont plus faibles que les VAN, parce que les flux sont réinvestis à 4 % et non à 7 % ; B, dont presque toute la valeur vient des flux annuels, perd la moitié de sa VAN (2,29 → 1,14), A, dont une grande part de la valeur vient de la valeur résiduelle, un peu plus d'un tiers (4,81 → 3,02). Avec cette hypothèse explicite de réinvestissement, la VAN globale **et** le TRI global classent A en tête : le conflit tenait à l'hypothèse implicite de réinvestissement au TRI. Le groupe n'étant pas rationné en capital, le projet qui crée le plus de valeur, **le projet A**, est retenu en avenir certain.

**Réponses tolérées** : valeur acquise de A de 37,41 ou 37,42 ; TRI globaux de 8,86 % à 8,87 % et de 8,61 % à 8,62 % ; conclusion fondée sur la seule VAN globale, si le candidat note que le TRI global la confirme.

**Erreurs fréquentes**
- Capitaliser la valeur résiduelle, ou capitaliser les flux au CMPC (la VAN globale est alors égale à la VAN).
- Calculer le TRI global sur la valeur acquise actualisée au lieu de la valeur acquise.

---

### 3.3 Projet A dans trois scénarios d'été (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | VAN du projet A : étés tempérés **8,64 M€**, étés chauds **4,81 M€**, étés très chauds **− 3,00 M€** | 0,75 |
| 3.3-02 | Espérance **3,24 M€** ; variance 18,74 ; écart-type **4,33 M€** ; coefficient de variation **1,34** ; probabilité d'une VAN négative **30 %** | 0,75 |
| 3.3-03 | Commentaire : espérance positive mais inférieure à la VAN des étés chauds ; risque élevé (écart-type supérieur à l'espérance, perte de 3,00 M€ dans un cas sur trois environ) ; projet B peu exposé aux étés (VAN de 2,29 M€ dans les trois scénarios) ; A garde la plus forte espérance, B le risque le plus faible : pas de dominance, le choix dépend de l'aversion au risque | 0,5 |

**VAN par scénario (0,75 pt).**

| M€ | Probabilité | Flux actualisés (× 7,023582) | Valeur résiduelle actualisée (× 0,508349) | VAN |
|---|---:|---:|---:|---:|
| Étés tempérés | 20 % | 2,35 → 16,51 | 16,00 → 8,13 | **8,64** |
| Étés chauds | 50 % | 1,95 → 13,70 | 14,00 → 7,12 | **4,81** |
| Étés très chauds | 30 % | 1,20 → 8,43 | 9,00 → 4,58 | **− 3,00** |

**Espérance et risque (0,75 pt).**
- E(VAN) = 0,20 × 8,64 + 0,50 × 4,81 + 0,30 × (− 3,00) = 1,73 + 2,41 − 0,90 = **3,24 M€**.
- Variance = 0,20 × (8,64 − 3,24)² + 0,50 × (4,81 − 3,24)² + 0,30 × (− 3,00 − 3,24)² = 5,84 + 1,24 + 11,65 = **18,74** ; écart-type = **4,33 M€**.
- Coefficient de variation = 4,33 / 3,24 = **1,34** ; probabilité d'une VAN négative = probabilité des étés très chauds = **30 %**.

**Commentaire (0,5 pt).**
- Les flux de l'annexe 3.1, établis avec des étés comme ceux de 2025 et de 2026, donnent une VAN de 4,81 M€ ; l'espérance n'est que de 3,24 M€, parce que les étés très chauds (30 %) sont plus probables que les étés tempérés (20 %) et qu'ils détruisent de la valeur (− 3,00 M€ : les flux baissent de 38 % et la valeur de la station en 2037 de 36 %).
- Le risque est élevé : l'écart-type dépasse l'espérance (coefficient de variation de 1,34) et la VAN est négative dans près d'un cas sur trois. Ce risque n'est pas propre à Lhérens : les cinq stations du groupe dépendent des étés, si bien que le projet A **renforce** une exposition que le groupe a déjà.
- Le projet B, dont les flux dépendent peu des étés, a une VAN de 2,29 M€ dans les trois scénarios : son risque est presque nul dans cette analyse. A offre la plus forte espérance (3,24 contre 2,29), B le risque le plus faible : aucun projet ne domine l'autre selon le couple espérance-risque. Un décideur neutre au risque retient A ; un décideur très averse au risque ou soucieux de réduire la dépendance du groupe aux étés peut préférer B. La question 3.4 mesure cet arbitrage.

**Réponses tolérées** : espérance de 3,23 ou 3,24 selon les arrondis des VAN ; variance calculée sur n − 1 si le candidat le signale (la convention de l'annexe 3.8 retient la variance pondérée par les probabilités) ; espérance calculée à partir du flux espéré (1,805) et de la valeur résiduelle espérée (12,90), qui donne le même résultat.

**Erreurs fréquentes**
- Calculer l'écart-type sans pondérer par les probabilités.
- Conclure sur la seule espérance, sans le risque, ou présenter le coefficient de variation sans l'interpréter.
- Évoquer une méthode hors programme (tables statistiques, tirages aléatoires répétés) : l'analyse repose sur les trois scénarios donnés.

---

### 3.4 Le projet B comme désinvestissement des thermes (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Flux du désinvestissement (B − A) : fonds libérés à la date 0 = 16,00 (investissement évité) + 3,20 (cession) − 2,10 (coûts de sortie) − 8,10 (reconversion) = **+ 9,00 M€** ; flux abandonnés par an : 1,10 (tempérés), **0,70** (chauds), − 0,05 (très chauds) ; valeur résiduelle abandonnée : 15,00, 13,00, 8,00 | 0,5 |
| 3.4-02 | VAN du désinvestissement : **− 6,35** (tempérés), **− 2,53** (chauds), **+ 5,28** (très chauds) ; espérance **− 0,95 M€** (= 2,29 − 3,24) | 0,5 |
| 3.4-03 | Création de valeur et conclusion : les deux projets ont une VAN positive en avenir certain ; en espérance, fermer les thermes détruit 0,95 M€ ; le désinvestissement n'en crée que si les étés sont très chauds (probabilité seuil voisine de 42 %) ; recommandation de rénover (projet A), avec ses conditions | 0,5 |

**Lecture du projet B comme un désinvestissement (0,5 pt).** Choisir B plutôt que A, c'est sortir de l'activité thermale à Lhérens : le groupe renonce aux flux futurs des thermes et à la valeur de la station rénovée, contre des fonds disponibles tout de suite et les flux de la résidence de tourisme.

| M€ | Date 0 | Années 1 à 9, par an | Année 10 |
|---|---:|---:|---:|
| Investissement de rénovation évité | + 16,00 | | |
| Prix de cession du bâtiment thermal, net d'impôt | + 3,20 | | |
| Coûts de fermeture et de départ des salariés, nets | − 2,10 | | |
| Travaux de reconversion de la résidence | − 8,10 | | |
| **Fonds libérés à la date 0** | **+ 9,00** | | |
| Flux de la résidence de tourisme | | + 1,25 | + 1,25 + 1,00 |
| Flux de la station rénovée abandonnés (étés chauds) | | − 1,95 | − 1,95 − 14,00 |
| **Flux du désinvestissement, étés chauds** | **+ 9,00** | **− 0,70** | **− 13,70** |

Les flux abandonnés varient avec les étés : 1,10 par an et 15,00 en 2037 (tempérés), 0,70 et 13,00 (chauds), − 0,05 et 8,00 (très chauds : la résidence de tourisme rapporterait alors un peu plus chaque année que la station rénovée).

**VAN du désinvestissement (0,5 pt).** VAN = 9,00 − flux abandonnés × 7,023582 − valeur résiduelle abandonnée × 0,508349, soit la VAN de B moins celle de A :
- étés tempérés : 2,29 − 8,64 = **− 6,35 M€** ;
- étés chauds : 9,00 − 0,70 × 7,023582 − 13,00 × 0,508349 = 9,00 − 4,92 − 6,61 = **− 2,53 M€** ;
- étés très chauds : 2,29 − (− 3,00) = **+ 5,28 M€** ;
- espérance : 0,20 × (− 6,35) + 0,50 × (− 2,53) + 0,30 × 5,28 = **− 0,95 M€**, soit 2,29 − 3,24.

**Création de valeur et conclusion (0,5 pt).**
- Les deux projets créent de la valeur : leurs VAN sont positives au CMPC en avenir certain, et la VAN de B reste positive dans tous les scénarios. Le projet A crée davantage de valeur en espérance (3,24 contre 2,29 M€) ; fermer les thermes en détruirait donc 0,95 M€ en espérance : la valeur de cession nette des coûts de sortie (1,10 M€) et l'investissement évité ne compensent pas les flux et la valeur résiduelle abandonnés.
- Le désinvestissement ne crée de la valeur que si les étés deviennent très chauds (+ 5,28 M€). En gardant 20 % aux étés tempérés, l'espérance de VAN de A tombe au niveau de la VAN de B quand la probabilité des étés très chauds atteint environ **42 %** (contre 30 % retenus) : la décision est sensible à cette hypothèse climatique.
- **Recommandation** : rénover l'établissement thermal de Lhérens (projet A), qui crée le plus de valeur en espérance, en le concevant pour réduire sa dépendance aux étés (espaces rafraîchis, saison avancée en mars et prolongée en novembre, report des cures de juillet et d'août vers le printemps et l'automne) et en suivant la fréquentation des étés à venir. Si les étés très chauds se répétaient, la reconversion resterait possible plus tard, mais à des conditions moins bonnes (travaux de rénovation engagés, bâtiment thermal non vendu). La décision tient aussi compte de l'emploi des salariés des thermes et de l'activité de la commune, sans que ces éléments soient chiffrés ici.

**Réponses tolérées** : flux du désinvestissement présentés dans le sens A − B (investissement différentiel de 9,00 M€, VAN de + 2,53 en étés chauds), si la conclusion est cohérente ; VAN des étés chauds de − 2,52 (différence des VAN arrondies) ; probabilité seuil seulement évoquée ; recommandation du projet B si elle est argumentée par une aversion au risque explicite ou par une probabilité d'étés très chauds jugée plus forte que celle de l'annexe 3.2.

**Erreurs fréquentes**
- Traiter le prix de cession sans les coûts de sortie, ou oublier l'investissement de rénovation évité.
- Comparer la valeur de cession du bâtiment (3,20 M€) à la VAN de A, sans raisonner sur les flux abandonnés : `JUR-T13`.
- Développer les règles applicables à la fermeture d'un établissement ou au départ des salariés : hors programme (UE 1) ; le coût de sortie est donné en un montant global.

---

### 3.5 Financement du programme : coûts, structure financière et résultat par action (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Emprunt : annuité = 40,00 × 0,046 / (1 − 1,046^−7) = **6,81 M€** ; coût actuariel avant IS (fonds reçus 39,76) **4,77 %** ; après IS (fonds nets 39,82, intérêts déductibles) **3,57 %** | 1 |
| 3.5-02 | Coût des fonds propres : 4,0 % + 0,90 × 5,0 % = **8,50 %**, pour l'augmentation de capital (frais de 1,80 M€, soit 4,31 % du brut ; décote de 10,93 % ; 1 900 000 actions nouvelles, dilution de 18,89 %) et pour l'autofinancement (coût d'opportunité, sans frais ni dilution) ; la dette est la ressource la moins chère | 0,5 |
| 3.5-03 | Dette financière nette / EBITDA pro forma (EBITDA 39,20) : S1 **2,85** ; S2 **1,83** ; S3 (emprunt 30,21, dividendes conservés 9,79) **2,60** ; 2,08 avant le programme ; S1 au-dessus de l'objectif de 2,75 et à 3,09 après un été très chaud | 0,75 |
| 3.5-04 | Résultat par action pro forma : S1 **1,41 €** ; S2 **1,28 €** (10 060 000 actions) ; S3 **1,45 €** ; 1,30 € en 2026 | 0,75 |
| 3.5-05 | Recommandation : combiner l'autofinancement et la dette dans la limite de l'objectif de 2,75, sans augmentation de capital ; par exemple dividende de 0,60 € et emprunt de 35,10 M€ (rapport 2,73, résultat par action 1,43 €), ou S3 si la direction veut une marge plus large | 0,5 |

**Emprunt bancaire (1 pt).**
- Annuité constante : a = 40,00 × 0,046 / (1 − 1,046^−7) = 40,00 / 5,871197 = **6,81 M€**. Première année : intérêts 1,84, amortissement 4,97, capital restant dû 35,03 ; deuxième année : intérêts 1,61, amortissement 5,20, capital restant dû 29,83.
- **Coût avant IS** : fonds reçus 40,00 − 0,24 = 39,76 M€, puis sept annuités de 6,81. Le taux t vérifie 39,76 = 6,81 × [1 − (1 + t)^−7] / t, soit un coefficient de 5,835970 : à 4,70 %, la valeur actuelle des flux de l'emprunteur vaut − 0,09 ; à 4,80 %, + 0,05 ; par interpolation, t = **4,77 %**.
- **Coût après IS** : à la date 0, 39,76 + 25 % × 0,24 = 39,82 ; chaque année, annuité − 25 % × intérêts (− 6,35 en 2028, − 6,41, − 6,47, − 6,53, − 6,60, − 6,67, − 6,74 en 2034). À 3,50 %, la valeur actuelle vaut − 0,10 ; à 3,60 %, + 0,05 ; par interpolation, **3,57 %**, très proche de 4,77 % × (1 − 25 %) = 3,58 %.

**Fonds propres et autofinancement (0,5 pt).**
- Coût des fonds propres selon le MEDAF : 4,0 % + 0,90 × 5,0 % = **8,50 %** : c'est la rentabilité qu'exigent les actionnaires, que les fonds viennent d'une émission ou des bénéfices conservés.
- **Augmentation de capital** : 1 900 000 × 22,00 = 41,80 M€ bruts, 40,00 M€ nets après 1,80 M€ de frais (4,31 % du brut), sans économie d'impôt. Les frais relèvent le coût effectif au-dessus de 8,50 % (environ 8,50 % / (1 − 4,31 %) = 8,88 %). La décote de 10,93 % sur le cours, nécessaire pour placer les titres, et la dilution des actionnaires qui ne souscrivent pas (1 900 000 / 10 060 000 = 18,89 % du capital après l'opération) s'y ajoutent.
- **Autofinancement** : les sommes conservées appartiennent aux actionnaires ; leur coût est le même coût d'opportunité de 8,50 %, sans frais, sans dilution ni économie d'impôt. Sa limite est son montant : 0,40 × 8 160 000 × 3 = **9,79 M€**, soit le quart du programme.
- Classement par le coût : dette (3,57 % après IS) < autofinancement (8,50 %) < augmentation de capital (8,50 % plus frais, décote et dilution).

**Effet sur la structure financière et sur le résultat par action (1,5 pt).**

| M€ (lecture pro forma) | S1 – emprunt | S2 – augmentation de capital | S3 – dividende 0,40 € + emprunt | *Dividende 0,60 € + emprunt* |
|---|---:|---:|---:|---:|
| Emprunt | 40,00 | 0 | 40,00 − 9,79 = 30,21 | *40,00 − 4,90 = 35,10* |
| Fonds propres (levés ou conservés) | 0 | 40,00 | 9,79 | *4,90* |
| Dette financière nette pro forma (71,80 + emprunt) | 111,80 | 71,80 | 102,01 | *106,90* |
| EBITDA pro forma (34,60 + 4,60) | 39,20 | 39,20 | 39,20 | *39,20* |
| **Dette financière nette / EBITDA** | **2,85** | **1,83** | **2,60** | ***2,73*** |
| Même rapport après un été très chaud (EBITDA 36,20) | 3,09 | 1,98 | 2,82 | *2,95* |
| Intérêts de la première année (× 4,60 %) | 1,84 | 0 | 1,39 | *1,61* |
| Résultat net pro forma : 10,61 + (3,00 − intérêts) × 0,75 | 11,48 | 12,86 | 11,82 | *11,65* |
| Nombre d'actions (millions) | 8,16 | 10,06 | 8,16 | *8,16* |
| **Résultat par action pro forma (€)** | **1,41** | **1,28** | **1,45** | ***1,43*** |

- **S1, tout emprunt** : la ressource la moins chère et le résultat par action le plus élevé après S3 (1,41 €), mais le rapport de 2,85 dépasse l'objectif de 2,75 annoncé aux investisseurs, et un seul été très chaud le porterait à 3,09, au-delà de la clause bancaire de 3,00. Si l'EBITDA du programme tardait (rénovations de 2029 en année pleine en 2030 seulement), le rapport atteindrait 111,80 / 34,60 = 3,23. Ce financement n'est pas soutenable seul.
- **S2, augmentation de capital** : la structure la plus solide (1,83), mais le financement le plus coûteux, une dilution de 18,89 % et un résultat par action en baisse (1,28 € contre 1,30 €) : le résultat du programme ne compense pas les actions nouvelles. Son annonce ferait probablement baisser le cours (question 3.8).
- **S3, baisse du dividende et emprunt** : rapport de 2,60, sous l'objectif même après un été très chaud (2,82), et le meilleur résultat par action (1,45 €), sans dilution. Son coût est le signal envoyé par la baisse de moitié du dividende (question 3.7).

**Recommandation (0,5 pt).** Financer le programme par l'autofinancement et par la dette, sans augmentation de capital, en restant sous l'objectif de 2,75. Le dividende n'a pas besoin d'être réduit de moitié : un dividende de **0,60 €** pendant trois ans conserve 4,90 M€, l'emprunt est de 35,10 M€, le rapport atteint **2,73** (2,95 après un été très chaud, encore sous la clause de 3,00) et le résultat par action **1,43 €**. Si la direction veut une marge plus large face aux étés, S3 (2,60) reste préférable à S1 et à S2. Le tirage de l'emprunt peut être étalé sur 2027-2029, au rythme des travaux, et le remboursement (6,81 M€ par an pour 40,00 M€) doit être rapproché de la trésorerie dégagée par le groupe.

**Réponses tolérées** : coût avant IS de 4,76 % ou 4,77 % ; coût après IS approché par 4,77 % × 0,75 = 3,58 % (approximation admise par l'énoncé si elle est justifiée) ou par 4,60 % × 0,75 = 3,45 % si le candidat signale que les frais l'augmentent ; coût des fonds propres de l'augmentation de capital présenté à 8,50 % ou relevé des frais ; recommandation de S3, ou d'une autre combinaison sous l'objectif de 2,75 (par exemple un emprunt et une petite augmentation de capital), si elle est chiffrée et argumentée.

**Erreurs fréquentes**
- Calculer l'annuité comme capital / durée + intérêts constants : `JUR-I01`.
- Retenir le taux nominal de 4,60 % comme coût de l'emprunt, sans frais ni économie d'impôt, ou un coût nul pour l'autofinancement.
- Compter la décote comme un coût pour la société au lieu d'un transfert entre anciens et nouveaux actionnaires, ou calculer un droit préférentiel de souscription : non demandé.
- Rapporter la dette aux capitaux propres sans répondre sur la dette financière nette rapportée à l'EBITDA, ou y inclure les dettes locatives, exclues de la clause et de l'objectif.
- Recommander S1 parce qu'il est le moins cher, sans tenir compte de l'objectif de levier et du risque climatique sur l'EBITDA.

---

### 3.6 Théories du financement (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Financement hiérarchique (Myers et Majluf, 1984) : autofinancement, puis dette, puis augmentation de capital en dernier recours, à cause de l'asymétrie d'information ; la combinaison recommandée suit cet ordre | 0,5 |
| 3.6-02 | Théorie du compromis (Myers, 1977) : endettement cible entre l'économie d'impôt sur les intérêts (0,40 M€ la première année pour 35,10 M€) et les coûts de difficultés financières, élevés pour un groupe dont l'EBITDA dépend des étés ; l'objectif de 2,75 joue le rôle d'un ratio cible ; S1 le dépasse | 0,5 |

**Financement hiérarchique (0,5 pt).** Selon Myers et Majluf (1984), les dirigeants en savent plus que les investisseurs sur la valeur de l'entreprise : une émission d'actions est lue comme le signe que l'action est surévaluée, si bien que l'entreprise se finance d'abord par l'autofinancement, puis par la dette, et en dernier lieu par l'augmentation de capital. La combinaison recommandée suit cet ordre : les bénéfices conservés (4,90 M€, ou 9,79 M€ dans S3) puis l'emprunt bancaire, sans émission d'actions. ONDAVÈRE a la capacité d'endettement nécessaire (2,08 avant le programme) : rien ne justifie de recourir à l'augmentation de capital, la ressource la plus chère et la plus mal reçue par le marché. Selon Ross (1977), un endettement maîtrisé signale aussi que la direction croit à sa capacité de rembourser.

**Théorie du compromis (0,5 pt).** Selon la théorie du compromis (Myers, 1977), il existe un endettement cible : la dette crée une économie d'impôt sur les intérêts (Modigliani et Miller, 1963), soit 25 % × 1,61 = **0,40 M€** la première année pour 35,10 M€ empruntés (0,46 M€ pour 40,00 M€), mais au-delà d'un certain niveau les coûts de difficultés financières (clause bancaire, frais financiers plus élevés, investissements reportés, défiance des clients et des salariés) l'emportent. Pour ONDAVÈRE, ces coûts sont élevés : l'EBITDA dépend des étés (− 3,00 M€ lors d'un été très chaud) et la clause de 3,00 serait franchie avec S1 après un seul été très chaud. L'objectif de 2,75 annoncé par le conseil joue le rôle d'un ratio cible ; la combinaison recommandée exploite l'économie d'impôt de la dette jusqu'à cet objectif, puis complète par l'autofinancement.

**Réponses tolérées** : théorie du compromis présentée sous le nom de « théorie de l'arbitrage » ou de « compromis statique » ; argument du signal par la dette rattaché à Ross (1977), non exigé.

**Erreurs fréquentes**
- Attribuer le financement hiérarchique à Modigliani et Miller, ou présenter la dette comme gratuite.
- Réciter les théories sans les appliquer aux chiffres du cas : `JUR-T13` ; `JUR-T14` — théories fondamentales mal connues.

---

### 3.7 Politique de dividende, signal et réaction du marché (4,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Taux de distribution : 50,82 % (2018), **58,18 %** (2019), 51,56 %, 52,24 %, 52,11 %, 52,70 %, 55,17 %, **58,82 %** (2025) ; 2026 : **61,54 %** avec 0,80 €, **30,77 %** avec 0,40 € ; dividende jamais réduit, même quand le résultat par action a baissé (2019, 2024, 2025) : lissage et effet cliquet | 0,5 |
| 3.7-02 | SARTENAY Villages : le jour de l'annonce, − **8,50 %** contre + 0,50 % pour l'indice, soit un écart de − **9,00 %** ; dans les cinq séances suivantes, écart de − 0,61 % ; du 19 mars 2025 au 11 mars 2026, + 11,57 % contre + 3,38 %, écart de + 8,19 % ; transposé à ONDAVÈRE (capitalisation de 201,55 M€) : − **18,14 M€**, contre 9,79 M€ de dividendes conservés en trois ans ; lecture au regard de l'efficience au sens semi-fort (Fama, 1970) | 1 |
| 3.7-03 | Signal et effet cliquet : une baisse du dividende est un signal (Spence, 1973) d'autant plus fort que les dirigeants lissent le dividende (Lintner, 1956) ; neutralité de Modigliani et Miller (1961) en marché parfait, et frictions qui la contredisent | 1 |
| 3.7-04 | Clientèles et coûts d'agence : fonds de rendement (VOLMÉRANDE Gestion), fonds de pension indifférent mais exigeant (Aldervik Pension Fund), salariés au travers du FCPE, public ; société sans actionnaire de contrôle : la conservation des flux accroît les coûts d'agence (Jensen et Meckling, 1976) si elle n'est pas encadrée | 1 |
| 3.7-05 | Proposition : baisse limitée (0,60 €, taux de distribution de 46,15 %) ou dividende maintenu financé autrement, encadrée par une règle chiffrée, un plancher, une durée et une date de retour ; communication avec le programme et ses VAN, aux salariés avant le marché, puis aux investisseurs | 1 |

**Taux de distribution (0,5 pt).**

| Exercice | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 (0,80 €) | 2026 (0,40 €) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Résultat par action (€) | 1,22 | 1,10 | 1,28 | 1,34 | 1,42 | 1,48 | 1,45 | 1,36 | 1,30 | 1,30 |
| Dividende (€) | 0,62 | 0,64 | 0,66 | 0,70 | 0,74 | 0,78 | 0,80 | 0,80 | 0,80 | 0,40 |
| Taux de distribution | 50,82 % | 58,18 % | 51,56 % | 52,24 % | 52,11 % | 52,70 % | 55,17 % | 58,82 % | 61,54 % | 30,77 % |

Le dividende a augmenté chaque année jusqu'en 2024, y compris en 2019 et en 2024, années où le résultat par action a baissé (d'environ 10 % en 2019), puis il a été maintenu à 0,80 € en 2025, malgré un nouveau recul du résultat. Le taux de distribution absorbe les variations du résultat : la direction lisse le dividende et ne l'a jamais réduit. Passer à 0,40 € diviserait le taux de distribution par deux (30,77 %), une rupture nette avec la politique suivie depuis l'introduction en bourse.

**Réaction du cours de SARTENAY Villages (1 pt).**

| Période | Variation du cours de SARTENAY Villages | Variation de l'indice | Écart (cours − indice) |
|---|---:|---:|---:|
| 11 → 12 mars 2025 (annonce) | 29,28 / 32,00 − 1 = − 8,50 % | 6 030 / 6 000 − 1 = + 0,50 % | **− 9,00 %** |
| 12 → 19 mars 2025 (cinq séances) | 29,13 / 29,28 − 1 = − 0,51 % | + 0,10 % | − 0,61 % |
| 19 mars 2025 → 11 mars 2026 | 32,50 / 29,13 − 1 = + 11,57 % | + 3,38 % | + 8,19 % |

- **Le jour de l'annonce**, l'action baisse de 8,50 % alors que l'indice monte de 0,50 % : un écart de − 9,00 % que les résultats, conformes aux prévisions, n'expliquent pas. Le marché a réagi à la seule baisse du dividende, et beaucoup plus que ne le voudrait l'effet mécanique : 0,55 € de dividende en moins représente 1,72 % du cours de la veille. Il a lu la baisse comme une information sur les flux futurs.
- **Efficience au sens semi-fort** (Fama, 1970) : le cours intègre l'information publique dès sa publication ; après le jour de l'annonce, l'écart avec l'indice reste faible (− 0,61 % en cinq séances, soit − 0,49 % dès le lendemain) : pas de dérive durable, ce qui est compatible avec une intégration immédiate de l'information. Le rattrapage suivant (+ 8,19 % par rapport à l'indice jusqu'au 11 mars 2026) accompagne une information nouvelle, la hausse des résultats et de la fréquentation des villages rénovés : le marché a révisé son jugement quand les flux promis se sont vérifiés. Il ne s'agit pas d'une erreur exploitable, mais d'informations successives.
- **Transposition à ONDAVÈRE** : capitalisation au 31 mars 2027 = 8 160 000 × 24,70 = 201,55 M€ ; un écart de − 9,00 % ferait perdre environ **18,14 M€** de capitalisation, soit près du double des 9,79 M€ que la baisse conserverait en trois ans. Les deux montants ne mesurent pas la même chose (une perte de valeur boursière n'est pas une sortie de trésorerie), mais l'ordre de grandeur montre que le signal peut coûter plus cher aux actionnaires que l'autofinancement ne rapporte à la société. La transposition reste fragile : une seule société, d'un autre secteur, une annonce sans cadre.

**Signal, effet cliquet et neutralité (1 pt).**
- **Neutralité** : selon Modigliani et Miller (1961), dans un marché parfait (sans impôt, sans coûts de transaction, avec une information partagée et une politique d'investissement donnée), la politique de dividende n'affecte pas la valeur. Ce qu'ONDAVÈRE ne verserait pas resterait investi dans des projets qui créent de la valeur (VAN positives aux questions 3.1 à 3.4) ; l'actionnaire qui veut un revenu peut vendre une partie de ses actions. La réaction de SARTENAY Villages montre que le marché réel n'est pas neutre.
- **Signal** : selon Spence (1973), un signal est crédible quand il est coûteux à émettre ; le dividende en est un, parce qu'une société fragile ne peut pas maintenir durablement un dividende élevé. Les dirigeants en savent plus que le marché sur les flux futurs ; une baisse du dividende révèle qu'ils les jugent insuffisants.
- **Effet cliquet** : les dirigeants lissent le dividende et ne le baissent qu'en dernier recours (Lintner, 1956). Chez ONDAVÈRE, qui n'a jamais réduit son dividende et en fait un argument auprès des investisseurs, une baisse de moitié serait d'autant plus remarquée ; la remonter ensuite sera difficile, car le marché attendra des preuves.
- **Frictions** : l'asymétrie d'information, les coûts d'agence, les coûts de transaction du « dividende fabriqué » par la vente d'actions et les différences d'imposition chez l'actionnaire expliquent pourquoi la politique de dividende compte en pratique.

**Clientèles d'actionnaires et coûts d'agence (1 pt).**
- **Effet de clientèle** : chaque politique de dividende attire des actionnaires différents. VOLMÉRANDE Gestion (6,5 %) gère des fonds de rendement dont les souscripteurs attendent un revenu : une baisse de moitié la conduirait à vendre, et la pression vendeuse s'ajouterait au signal. Aldervik Pension Fund (7,8 %), investisseur de long terme, est indifférent à la forme du rendement (raisonnement de Modigliani et Miller) et préfère la conservation des bénéfices à la dilution, mais il pose des conditions. Le public (33 %) compte de nombreux épargnants sensibles au revenu. Changer brutalement de politique, c'est changer de clientèle, avec des ventes et une baisse du cours pendant la transition.
- **Salariés** : le FCPE (6 %) réinvestit les dividendes en actions ; les salariés regardent surtout la valeur de leurs parts. Ils seraient doublement exposés : à la baisse du cours qui suivrait le signal, et, à Lhérens, à la décision sur leurs thermes. Leur conseil de surveillance demande d'être informé avant le marché : c'est une condition de leur adhésion au programme.
- **Coûts d'agence** : sans actionnaire de contrôle, les actionnaires dispersés surveillent mal les dirigeants (Jensen et Meckling, 1976). Distribuer les flux disponibles limite le risque qu'ils soient investis dans des projets qui ne rapportent pas le coût du capital, ce que redoute Aldervik Pension Fund (« projets de prestige ») ; conserver les bénéfices accroît ce risque. La conservation n'est acceptable que si elle finance des projets créateurs de valeur (projet A, VAN espérée de 3,24 M€) et si le conseil, où siègent cinq administrateurs indépendants, en contrôle l'emploi.

**Politique proposée et communication (1 pt).**
- **Politique** : une baisse limitée plutôt qu'une baisse de moitié, par exemple **0,60 €** par action au titre de 2026, 2027 et 2028 (taux de distribution de 46,15 % en 2026, rendement de 2,43 %), qui suffit à respecter l'objectif de levier (question 3.5) ; présentée comme un **plancher** pendant le programme, avec une **règle** de distribution (environ 45 à 50 % du résultat par action) et une **date de retour** à 0,80 € au titre de 2029, une fois les trois rénovations en service et le rapport dette financière nette / EBITDA revenu sous l'objectif. Le maintien de 0,80 €, financé par un emprunt plus élevé, est défendable si la direction accepte un levier proche de l'objectif.
- **Communication** : annoncer le dividende en même temps que le programme, avec sa VAN, son calendrier, son financement et l'objectif de levier, pour que la baisse soit lue comme un choix d'investissement et non comme un aveu de faiblesse (SARTENAY Villages l'avait annoncée « sans autre information ») ; informer d'abord les salariés et le conseil de surveillance du FCPE, puis le marché le même jour, avant l'assemblée générale du 17 juin 2027 ; rencontrer les principaux investisseurs institutionnels (VOLMÉRANDE Gestion, Aldervik Pension Fund) ; rendre compte chaque année de l'avancement des rénovations et de l'emploi des sommes conservées, comme l'a fait SARTENAY Villages en 2026.

**Réponses tolérées** : taux de distribution arrondis au dixième ; écart du jour de l'annonce présenté comme une « sous-performance » de 9 points ; transposition faite sur les 9,79 M€ annuels au lieu de trois ans si le candidat la nuance ; proposition d'un dividende maintenu à 0,80 €, ou réduit à 0,40 € avec un cadre chiffré et une date de retour, si elle est cohérente avec le financement retenu à la question 3.5 ; paiement d'une partie du dividende en actions évoqué comme piste, sans développement.

**Erreurs fréquentes**
- Interpréter la baisse du cours comme la seule conséquence mécanique du dividende versé en moins.
- Conclure à l'inefficience du marché à partir du rattrapage de 2026, qui suit une information nouvelle.
- Présenter un calcul de rentabilité anormale avec un bêta ou une méthode statistique : la comparaison simple à l'indice suffit et la mesure statistique de l'efficience n'est pas au programme.
- Citer Modigliani et Miller sans dire pourquoi la neutralité ne tient pas ici, ou réciter les théories sans les actionnaires du cas : `JUR-T13` ; `JUR-I04` — revenu immédiat et renforcement des fonds propres non opposés.

---

### 3.8 Asymétrie d'information et annonce d'une augmentation de capital (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.8-01 | Mécanisme : asymétrie d'information (Akerlof, 1970) ; les dirigeants émettent plus volontiers quand l'action est surévaluée ; le marché, qui le sait, lit l'annonce comme une mauvaise nouvelle et baisse le cours (Myers et Majluf, 1984) ; les sociétés de bonne qualité renoncent parfois à émettre (sélection adverse) | 0,5 |
| 3.8-02 | Application : émission de 1 900 000 actions à 22,00 € alors que la dette est disponible et moins chère ; dilution de 18,89 % ; question posée par l'analyste ; réponses possibles : préférer la dette et l'autofinancement, ou, si l'émission est nécessaire, la justifier par des projets chiffrés | 0,5 |

**Mécanisme (0,5 pt).** Selon Akerlof (1970), quand le vendeur connaît mieux la qualité de ce qu'il vend que l'acheteur, l'acheteur paie un prix moyen et se méfie : les vendeurs des meilleurs biens se retirent, la qualité moyenne baisse (sélection adverse). Sur le marché financier, la société qui émet des actions est le vendeur : ses dirigeants connaissent mieux que les investisseurs la valeur de ses actifs et de ses projets. Myers et Majluf (1984) en tirent la conséquence : agissant pour les actionnaires actuels, les dirigeants émettent plutôt quand ils jugent l'action surévaluée, et ils préfèrent la dette quand ils la jugent sous-évaluée. Les investisseurs l'anticipent : ils lisent l'annonce d'une augmentation de capital comme le signe que l'action vaut moins que son cours, et ils la paient moins cher. Le cours baisse à l'annonce, même si le projet financé a une VAN positive ; certaines sociétés de bonne qualité renoncent alors à émettre et à investir.

**Application à ONDAVÈRE (0,5 pt).** Le programme peut être financé par la dette (rapport de 2,08 avant le programme) et par les bénéfices : si ONDAVÈRE émettait malgré tout 1 900 000 actions à 22,00 € (décote de 10,93 %, dilution de 18,89 %), le marché se demanderait, comme l'écrit l'analyste, pourquoi la direction choisit la ressource la plus chère : il en déduirait qu'elle juge le cours de 24,70 € élevé, ou qu'elle redoute de ne pas pouvoir rembourser une dette. Pour éviter ce coût, la direction privilégie l'autofinancement et la dette ; si une émission devenait nécessaire (par exemple après des étés très chauds), elle devrait réduire l'asymétrie d'information en publiant les projets financés, leurs VAN et leurs hypothèses climatiques, et en montrant que les dirigeants et le FCPE y souscrivent.

**Réponses tolérées** : sélection adverse présentée à partir de l'exemple des voitures d'occasion, si elle est appliquée à l'émission d'actions ; lien avec le financement hiérarchique déjà développé à la question 3.6, sans répétition.

**Erreurs fréquentes**
- Expliquer la baisse du cours par la seule décote ou par la dilution du résultat par action, sans l'asymétrie d'information.
- Confondre la baisse liée à l'annonce et l'ajustement mécanique du cours lors du détachement du droit préférentiel.
- `JUR-M01` — théories fondatrices (asymétrie d'information, signal) non mobilisées.

---

**Points d'attention pour le correcteur**
- Aux questions 3.1 et 3.2, l'investissement du projet B est le décaissement net de la date 0 (annexe 3.8) ; un candidat qui traite la cession et les coûts de sortie à part obtient une VAN identique et un indice de profitabilité différent, admis s'il l'explique.
- À la question 3.4, la VAN du désinvestissement se déduit directement des VAN des questions 3.1 et 3.3 ; un candidat qui ne reconstruit pas les flux mais calcule VAN(B) − VAN(A) dans chaque scénario obtient l'item 3.4-02, et l'item 3.4-01 s'il identifie les fonds libérés et les flux abandonnés.
- À la question 3.5, la combinaison à 0,60 € n'est pas exigée : toute combinaison chiffrée qui respecte l'objectif de 2,75 et justifie le renoncement à l'augmentation de capital obtient l'item 3.5-05. La question 3.7 doit rester cohérente avec la combinaison choisie.
- À la question 3.7, la transposition de la réaction de SARTENAY Villages n'est qu'un ordre de grandeur : le candidat qui en discute les limites est valorisé.
