# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 45 — Dossier 3 (18 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F03 évaluation, F05 ingénierie financière, F08 gouvernance et ESG, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026) ; fiche commune CSRD, ESRS et double matérialité (extraite le 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (bilan, ANC et ANCC, valeur de sortie et TRI obtenu de la méthode du capital-risque, valeurs actuelles au TRI exigé et aux TRI de sensibilité, flux actualisés, valeur terminale, VGE et VCP et leur sensibilité, valeur actuelle des synergies, multiple des transactions, complément de prix par scénario, VAN de l'acquisition par scénario avec et sans complément, espérance et écart-type, flux de l'acquisition, coûts actuariels de l'emprunt et de la trésorerie, barème, liste noire, hors-programme ; prix espéré, prime, multiples implicites, interpolations, situation du groupe après l'opération et coût de portage vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une création de valeur calculée à partir d'une VCP erronée à la question 3.4).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Motifs et risques du rachat d'un studio indépendant | `4.2.b` Analyser les motifs des opérations de réorganisation | 1,5 |
| 3.2 Cycle de vie, choix des méthodes, ANC et ANCC, portée de l'approche patrimoniale | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine ; `3.3.c` Savoir calculer la valeur d'une entreprise en fonction de son cycle de vie | 2 |
| 3.3 Méthode du capital-risque pour 100 % du capital, sensibilité au TRI, pertinence et limites | `3.3.c` | 2 |
| 3.4 Flux de trésorerie disponibles actualisés, valeur terminale, VGE et VCP | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance ; `3.1.d` Distinguer la VGE de la VCP | 2,5 |
| 3.5 Multiple des transactions et fourchette de valeur | `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP | 1 |
| 3.6 Complément de prix, synergies, création de valeur, prime payée et VAN de l'acquisition par scénario | `7.1.b` Évaluer et classer des projets en milieu incertain ; `7.1.c` Déterminer la création de valeur à travers la décision d'investissement ; `4.2.c` Analyser les opérations de fusions et d'acquisitions | 5 |
| 3.7 Coût de l'emprunt et de la trésorerie, effets sur la structure financière, financement hiérarchique | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière ; `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives | 2 |
| 3.8 Double matérialité des enjeux de l'audit d'acquisition et publication après l'intégration | `2.1.b` Interpréter le reporting RSE et de durabilité ; `2.1.d` Maîtriser le principe de double matérialité | 2 |
| **Total** | | **18** |

Part du calcul : environ 9,4 points (3.2-02, 3.2-03, 3.3-01, 3.3-02, 3.4-01 à 3.4-03, 3.5-01, 3.6-01, 3.6-03, 3.6-05, la moitié de 3.6-04, 3.7-01 et 3.7-02). Part de l'analyse : environ 8,6 points. Le dossier est le dernier de l'épreuve : les questions 3.6 à 3.8, qui demandent une conclusion et une recommandation, ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 Motifs et risques du rachat d'un studio indépendant (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Motifs reliés au cas : croissance externe plus rapide que le recrutement (61 développeurs formés), propriété intellectuelle (licence des « Lanternes de Morvaigne », moteur de jeu), moindre dépendance à une seule licence, synergies d'édition et de distribution (consoles, boutiques numériques), occasion créée par la sortie du fonds et par la concurrence d'un autre éditeur | 0,75 |
| 3.1-02 | Risques : départ des fondateurs et des développeurs (19 % de départs, 3 responsables sur 9, directeur technique après 2029), succès incertain du second jeu, intégration de deux cultures de production, prime payée et surenchère face à PARVIGNE Entertainment, information limitée sur un studio non audité, risques extra-financiers (achats intégrés, fins de production) | 0,75 |

**Motifs (0,75 pt).** Une acquisition est une décision d'investissement : elle n'a de sens que si elle crée de la valeur pour les actionnaires de l'acheteur, par des synergies ou par une croissance plus rapide que la croissance interne (guide p. 69).
- **Acheter des talents** : dans un secteur où la valeur tient aux équipes, recruter et former des développeurs expérimentés est long ; VELTRANE apporte d'un coup 61 développeurs qui ont déjà sorti un jeu à succès.
- **Acheter de la propriété intellectuelle** : la licence des « Lanternes de Morvaigne » (2,1 millions d'exemplaires) et le moteur de jeu du studio, que NOCTÉVAL pourrait exploiter (suites, adaptations).
- **Réduire la dépendance à un titre** : « Les Brumes d'Aldrec » et sa suite portent l'essentiel du chiffre d'affaires et des perspectives du groupe ; un second studio, avec sa propre licence et un jeu coopératif en ligne, diversifie le portefeuille de jeux et le risque d'échec d'une sortie.
- **Synergies d'édition et de distribution** : VELTRANE n'est présent que sur ordinateurs et édite seul ; NOCTÉVAL peut adapter le jeu aux consoles, le commercialiser et négocier avec les boutiques numériques (synergies de 2,20 M€ d'EBITDA par an, annexe 3.5).
- **Une occasion** : le fonds KESTRALIA Capital veut sortir et les fondateurs cherchent un éditeur ; la présence de PARVIGNE Entertainment oblige à se décider. NOCTÉVAL dispose de 268 M€ de trésorerie pour payer en numéraire.

**Risques (0,75 pt).**
- **Départ des talents** : la valeur rachetée « sort par la porte » chaque soir. Le taux de départs volontaires est passé de 9 % à 19 % et trois responsables d'équipe sur neuf sont partis en 2026 ; M. Bastien CORDEIL, qui a conçu le moteur, veut partir après 2029. Les fondateurs ne s'engagent à rester que jusqu'à la fin de 2029.
- **Risque du second jeu** : une large part de la valeur dépend du succès des « Cartographes d'Ysmer » (écart de − 18,00 à + 27,00 M€ selon le scénario).
- **Risque d'intégration** : un studio indépendant de 74 personnes et un groupe coté de 760 salariés n'ont ni les mêmes méthodes de production ni la même culture ; une intégration maladroite accélère les départs ; coûts d'intégration de 4,00 M€.
- **Prime payée** : la concurrence de PARVIGNE Entertainment pousse à payer trop cher (« malédiction du vainqueur ») ; si les synergies ne se réalisent pas, la prime détruit de la valeur pour les actionnaires de NOCTÉVAL.
- **Asymétrie d'information** : le studio n'est pas coté, son plan d'affaires est établi par les vendeurs et il ne publie aucune information extra-financière ; l'audit d'acquisition révèle des risques sociaux et de réputation (achats intégrés dans un jeu pour enfants, fins de production).

**Réponses tolérées** : motifs présentés selon la typologie synergies opérationnelles, financières et stratégiques ; mention du risque de dilution de la culture créative de NOCTÉVAL ; mention de la théorie de l'agence (dirigeants de l'acheteur qui privilégient la taille), si elle est reliée au cas.

**Erreurs fréquentes**
- Énumérer des motifs généraux de croissance externe sans les données du cas.
- Analyser la forme juridique de l'opération ou les conditions du contrat de cession (UE 1).
- `JUR-T13` — réponses non contextualisées ; `JUR-T01` — absence de posture de conseil.

---

### 3.2 Cycle de vie, choix des méthodes, ANC et ANCC, portée de l'approche patrimoniale (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Stade : jeune entreprise en croissance (créée en 2020, un seul succès, chiffre d'affaires en baisse après la sortie, second jeu décisif) ; méthodes adaptées : flux de trésorerie actualisés et méthode du capital-risque, recoupées par les comparables ; approche patrimoniale peu pertinente | 0,5 |
| 3.2-02 | ANC = 22,50 − 1,80 − 4,70 = **16,00 M€** (égal aux capitaux propres comptables) | 0,25 |
| 3.2-03 | Plus-value sur le moteur 5,00 − 1,40 = 3,60 ; impôt latent **0,90** ; projet abandonné − 0,60 ; ANCC = 16,00 + 3,60 − 0,90 − 0,60 = **18,10 M€** | 0,75 |
| 3.2-04 | Portée limitée : l'ANCC ignore les talents, la licence, la communauté de joueurs et la capacité à produire des jeux ; il donne au mieux un plancher | 0,5 |

**Cycle de vie et choix des méthodes (0,5 pt).** La méthode d'évaluation dépend du stade de développement (guide p. 67 ; F03 § 8) : création → méthode du capital-risque ; croissance → flux actualisés ; maturité → multiples et flux ; déclin ou difficulté → approche patrimoniale.
- VELTRANE est une **jeune entreprise en croissance** : créée en 2020, elle a sorti un seul jeu, dont le chiffre d'affaires baisse déjà (26,0 M€ puis 22,0 M€) ; sa valeur dépend d'un second jeu qui n'est pas sorti et d'une équipe de 61 développeurs. Ses résultats passés disent peu de ses résultats futurs.
- Méthodes pertinentes : la **méthode du capital-risque**, qui traite l'incertitude d'un projet jeune par un TRI exigé élevé ; les **flux de trésorerie disponibles actualisés**, possibles parce que le studio est déjà rentable et que des prévisions existent ; les **comparables de transactions**, pour recouper. L'approche patrimoniale est calculée comme plancher.

**ANC (0,25 pt).** ANC = total de l'actif − dettes = 22,50 − 1,80 − 4,70 = **16,00 M€**, égal aux capitaux propres (2,00 + 8,60 + 5,40).

**ANCC (0,75 pt).** Corrections limitatives de l'annexe 3.2 :

| Élément | Montant (M€) |
|---|---:|
| ANC | 16,00 |
| + Plus-value sur le moteur de jeu (5,00 − 1,40) | + 3,60 |
| − Impôt latent sur cette plus-value (25 % × 3,60) | − 0,90 |
| − Projet de jeu abandonné (sans valeur, sans effet d'impôt) | − 0,60 |
| **ANCC** | **18,10** |

**Portée limitée de l'approche patrimoniale (0,5 pt).**
- L'ANCC mesure ce que valent les actifs et les dettes pris un à un ; il ignore la capacité du studio à **produire des jeux rentables**, qui fait l'essentiel de sa valeur : l'équipe, la licence des « Lanternes de Morvaigne », la communauté des joueurs et le savoir-faire ne sont pas au bilan.
- L'écart est massif : 18,10 M€ contre 62,00 M€ par les flux (question 3.4), soit 29 % (comparaison non exigée ici) ; le prix espéré (64,49 M€, question 3.6) représente 3,56 fois l'ANCC. La différence est un goodwill qui rémunère des actifs immatériels non inscrits et la rentabilité future.
- L'ANCC reste utile comme **plancher** (valeur en cas d'échec du second jeu, si l'équipe se disperse) et pour repérer les actifs à expertiser (moteur de jeu, coûts de développement de 5,20 M€, dont la valeur dépend du succès du jeu).

**Réponses tolérées** : ANC calculé à partir des capitaux propres (2,00 + 8,60 + 5,40) ; mention de la valeur d'un studio « en déclin » si le second jeu échoue, qui rendrait l'approche patrimoniale plus pertinente ; sans le pourcentage de 29 %, si l'écart est commenté.

**Erreurs fréquentes**
- Appliquer l'impôt latent à l'élimination du projet abandonné, ou oublier l'impôt latent sur le moteur (ANCC de 19,00).
- Ajouter une valeur des talents ou de la licence à l'ANCC : la liste des corrections est limitative.
- Calculer un goodwill par la rente : la méthode n'est pas demandée et les données ne sont pas fournies.
- `JUR-E03` — croiser les méthodes ; `JUR-T12` — réponse superficielle sur le choix des méthodes.

---

### 3.3 Méthode du capital-risque pour 100 % du capital, sensibilité au TRI, pertinence et limites (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Valeur de sortie = 16 × 7,75 = **124,00 M€** au 31/12/2031 ; valeur actuelle au TRI exigé de 20 % = 124,00 / 1,20^5 = 124,00 / 2,48832 = **49,83 M€** | 0,75 |
| 3.3-02 | Sensibilité : **61,65 M€** à 15 % et **40,63 M€** à 25 % ; TRI obtenu au prix fixe de 58,00 = (124,00 / 58,00)^(1/5) − 1 = **16,41 %** < 20 % : la partie fixe dépasse de 8,17 M€ la valeur au TRI exigé | 0,75 |
| 3.3-03 | Pertinence : jeune entreprise, valeur concentrée à l'horizon, incertitude traitée par un TRI élevé ; limites : flux intermédiaires (24,20 M€) et trésorerie ignorés, dépendance au plan des vendeurs et au multiple de sortie, synergies ignorées, TRI arbitraire, pas de probabilités | 0,5 |

**Calcul (0,75 pt).** La méthode du capital-risque (F03 § 7 ; guide p. 67) actualise la valeur de sortie attendue au TRI exigé. NOCTÉVAL rachetant 100 % du capital sans augmentation de capital, il n'y a ni valeur avant ni valeur après l'apport à distinguer : la valeur actuelle est celle de la totalité des capitaux propres.
- Valeur de sortie au 31/12/2031 = multiple × résultat net de 2031 = 16 × 7,75 = **124,00 M€**.
- Valeur actuelle au 31/12/2026, au TRI exigé de 20 % : 124,00 / 1,20^5 = 124,00 / 2,48832 = **49,83 M€**.

**Sensibilité et TRI obtenu (0,75 pt).**

| TRI | 15 % | 20 % | 25 % |
|---|---:|---:|---:|
| Facteur (1 + TRI)^5 | 2,011357 | 2,488320 | 3,051758 |
| Valeur actuelle de 100 % du capital (M€) | **61,65** | **49,83** | **40,63** |
| Écart avec la partie fixe de 58,00 (M€) | + 3,65 | − 8,17 | − 17,37 |

- La valeur est très sensible au TRI : 5 points de TRI déplacent la valeur de 9 à 12 M€, soit près d'un cinquième.
- TRI obtenu si NOCTÉVAL paie la seule partie fixe : (124,00 / 58,00)^(1/5) − 1 = 2,1379^0,2 − 1 = **16,41 %**, inférieur aux 20 % exigés. Avec le complément de prix espéré (prix de 64,49 M€, question 3.6), le TRI tomberait à environ 14 % (non exigé). Selon le critère du comité, le prix demandé est trop élevé, alors même que la valeur de sortie repose sur le plan, jugé optimiste, des vendeurs.

**Pertinence et limites (0,5 pt).**
- **Pertinence pour une jeune entreprise** : la valeur d'un studio jeune est concentrée dans un avenir incertain (succès du second jeu, troisième jeu en 2030) ; ses résultats passés ne sont pas représentatifs. La méthode raisonne comme un investisseur : prix d'entrée, valeur de sortie, TRI. Le TRI élevé (20 % contre un CMPC de 11 %) intègre le risque d'échec et l'optimisme du plan d'affaires, sans avoir à construire des flux annuels.
- **Ce qu'elle laisse de côté** : les **flux intermédiaires** (24,20 M€ de flux disponibles de 2027 à 2031 selon l'annexe 3.4, qui reviennent à NOCTÉVAL) et la trésorerie nette actuelle de 8,30 M€ ; les **synergies** propres à l'acheteur ; la **dispersion** des issues (un seul chiffre de sortie, sans scénarios ni probabilités) ; elle dépend entièrement du **résultat de 2031 des vendeurs** et du **multiple de sortie** supposé, et le TRI exigé est une norme interne, en partie arbitraire.

**Réponses tolérées** : valeur actuelle présentée comme une « valeur post-money » de 100 % du capital, si le candidat précise qu'il n'y a pas d'apport ; TRI obtenu avec le prix espéré (13,97 %) au lieu de la partie fixe, s'il est justifié ; sensibilité exprimée en pourcentage.

**Erreurs fréquentes**
- Calculer une valeur avant apport et une part du capital, comme pour l'entrée d'un fonds minoritaire : NOCTÉVAL rachète 100 % des actions existantes.
- Actualiser sur six ans (de 2026 à 2031 inclus) ou au CMPC de 11 % (valeur de 73,59 M€).
- `JUR-E03` — comparer la méthode aux autres ; `JUR-T12` — réponse superficielle sur la pertinence de la méthode pour une jeune entreprise.

---

### 3.4 Flux de trésorerie disponibles actualisés, valeur terminale, VGE et VCP (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Flux actualisés à 11 % : 1,80 ; 4,87 ; 3,95 ; 3,56 ; 3,20 ; somme **17,38 M€** | 0,75 |
| 3.4-02 | Valeur terminale à la fin de 2031 = 5,40 × 1,02 / (11 % − 2 %) = 5,508 / 0,09 = **61,20 M€** ; valeur actuelle = 61,20 × 1,11^−5 = **36,32 M€** | 0,75 |
| 3.4-03 | VGE = 17,38 + 36,32 = **53,70 M€** ; dette financière nette = 1,80 − 10,10 = − 8,30 (trésorerie nette) ; VCP = 53,70 + 8,30 = **62,00 M€** | 0,5 |
| 3.4-04 | Poids de la valeur terminale **67,63 %** de la VGE ; sensibilité au CMPC et à la croissance (VCP de 56,46 à 68,93 pour un CMPC de 12 % à 10 % ; de 58,05 à 66,94 pour une croissance de 1 % à 3 %) ; flux d'exploitation actualisés au CMPC, pas au coût des fonds propres | 0,5 |

**Flux actualisés (0,75 pt).** Les flux de trésorerie disponibles reviennent à tous les apporteurs de capitaux : ils s'actualisent au **CMPC** du studio (11,00 %, fourni), en fin d'année.

| Année | 2027 | 2028 | 2029 | 2030 | 2031 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Flux de trésorerie disponible (M€) | 2,00 | 6,00 | 5,40 | 5,40 | 5,40 | 24,20 |
| Coefficient 1,11^−n | 0,900901 | 0,811622 | 0,731191 | 0,658731 | 0,593451 | |
| Flux actualisé (M€) | 1,80 | 4,87 | 3,95 | 3,56 | 3,20 | **17,38** |

**Valeur terminale (0,75 pt).** Modèle de Gordon et Shapiro (F10 § 2) appliqué au flux de 2032 : VT(2031) = 5,40 × 1,02 / (0,11 − 0,02) = 5,508 / 0,09 = **61,20 M€** ; valeur actuelle = 61,20 × 0,593451 = **36,32 M€**.

**VGE et VCP (0,5 pt).**
- VGE = 17,38 + 36,32 = **53,70 M€**.
- Dette financière nette au 31/12/2026 (annexe 3.2) = emprunt − disponibilités = 1,80 − 10,10 = **− 8,30 M€** : le studio a une trésorerie nette, qui s'ajoute à la VGE.
- **VCP = VGE − dette financière nette = 53,70 + 8,30 = 62,00 M€**, pour 100 % du capital.

**Commentaire (0,5 pt).**
- La valeur terminale représente 36,32 / 53,70 = **67,63 %** de la VGE : l'essentiel de la valeur tient à la capacité du studio à produire des jeux après 2031, au-delà de l'horizon des prévisions. C'est typique d'une entreprise en croissance, et c'est une fragilité.
- La valeur est sensible aux hypothèses : avec un CMPC de 10 % ou de 12 %, la VCP passe à 68,93 ou 56,46 M€ ; avec une croissance de 1 % ou de 3 %, à 58,05 ou 66,94 M€ (calculs non exigés ; une seule variante suffit).
- Les flux sont ceux du **scénario central** et du **studio seul** : ils ne comprennent pas les synergies, traitées à la question 3.6, et ne disent rien de la dispersion des issues du second jeu.
- Ils sont actualisés au CMPC parce qu'ils sont avant rémunération des prêteurs : un coût des fonds propres, plus élevé, sous-évaluerait la VGE.

**Réponses tolérées** : valeur terminale arrondie (61,20) actualisée, sans effet ici ; VGE obtenue directement par la somme des six termes ; sensibilité commentée sans calcul, si elle est expliquée (effet du dénominateur CMPC − g).

**Erreurs fréquentes**
- Calculer la valeur terminale sur le flux de 2031 sans croissance (5,40 / 0,09 = 60,00) ou avec CMPC + g au dénominateur.
- Actualiser la valeur terminale sur six ans, ou oublier de l'actualiser.
- Retrancher la trésorerie nette au lieu de l'ajouter (VCP de 45,40).
- `JUR-E01` — flux de trésorerie disponibles mal compris ; `JUR-T04` — actualisation non maîtrisée.

---

### 3.5 Multiple des transactions et fourchette de valeur (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | VGE = 8,5 × 7,40 = **62,90 M€** ; VCP = 62,90 + 8,30 = **71,20 M€** | 0,5 |
| 3.5-02 | Comparaison : ANCC 18,10 (plancher) ; capital-risque 49,83 (40,63 à 61,65) ; flux 62,00 ; transactions 71,20, qui incorpore les synergies et la prime de contrôle payées par des éditeurs ; fourchette argumentée, par exemple **50 à 71 M€**, valeur centrale 62 M€ | 0,5 |

**Multiple des transactions (0,5 pt).** Le multiple VGE / EBITDA est un inducteur de **VGE** (guide p. 65) : VGE = 8,5 × 7,40 = **62,90 M€** ; VCP = VGE − dette financière nette = 62,90 + 8,30 = **71,20 M€**.

**Comparaison et fourchette (0,5 pt).**

| Méthode | VCP de 100 % du capital (M€) | Lecture |
|---|---:|---|
| ANCC | 18,10 | plancher, ignore les immatériels |
| Capital-risque (TRI de 20 % ; 25 % à 15 %) | 49,83 (40,63 à 61,65) | point de vue prudent du comité, plan des vendeurs |
| Flux actualisés (scénario central) | 62,00 | valeur intrinsèque du studio seul |
| Transactions récentes | 71,20 | prix payés par des éditeurs, synergies et prime de contrôle comprises |

- Le multiple des transactions donne la valeur la plus haute : il reflète des **prix payés** par des acheteurs, en général des éditeurs, qui ont intégré une partie de leurs synergies et une prime de contrôle ; il s'applique à l'EBITDA d'une année qui suit un succès et qui n'intègre pas la baisse du chiffre d'affaires. Le DCF implique un multiple de 53,70 / 7,40 = 7,26 fois l'EBITDA.
- Fourchette retenue (exemple) : **de 50 à 71 M€** pour 100 % des capitaux propres, avec une valeur centrale de **62 M€** (flux actualisés) ; l'ANCC est écarté comme méthode de valeur. La partie fixe demandée (58,00 M€) se situe dans la fourchette, sous la valeur par les flux.

**Réponses tolérées** : fourchette resserrée (par exemple 56 à 69 M€, sensibilité du DCF) ou moyenne pondérée justifiée ; capital-risque retenu comme borne basse ou écarté, s'il est justifié.

**Erreurs fréquentes**
- Présenter 62,90 comme une valeur des capitaux propres, ou retrancher la trésorerie nette.
- Faire la moyenne de toutes les méthodes, ANCC compris, sans justification.
- `JUR-E03` — fourchette de négociation non construite à partir de plusieurs méthodes.

---

### 3.6 Complément de prix, synergies, création de valeur, prime payée et VAN de l'acquisition par scénario (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Complément espéré = 0,30 × 0 + 0,50 × 8,00 + 0,20 × 20,00 = **8,00 M€** ; valeur actuelle = 8,00 × 1,11^−2 = **6,49 M€** (0 ; 6,49 ; 16,23 par scénario) ; prix espéré = 58,00 + 6,49 = **64,49 M€** | 0,75 |
| 3.6-02 | Partage du risque (le prix suit la valeur réelle du second jeu ; écart-type de la VAN ramené de 15,59 à 9,97) et réduction de l'asymétrie d'information (les vendeurs, mieux informés et optimistes, acceptent d'être payés selon les résultats : signal crédible ; Akerlof, 1970 ; Spence, 1973) ; incitation des fondateurs à rester et à réussir le jeu | 0,75 |
| 3.6-03 | Synergies nettes = 2,20 × 0,75 = 1,65 ; valeur actuelle = 1,65 / 0,11 = **15,00 M€** ; intégration nette = 4,00 × 0,75 = **3,00** ; création de valeur espérée = 62,00 + 15,00 − 3,00 − 64,49 = **9,51 M€** | 1 |
| 3.6-04 | Prime payée = 64,49 − 62,00 = **2,49 M€**, soit **4,02 %** de la VCP du studio seul ; environ 17 % des synergies cédées aux vendeurs ; multiple implicite de 7,59 fois l'EBITDA (contre 8,5 pour les transactions) ; création = synergies − prime − intégration | 0,75 |
| 3.6-05 | VAN avec complément : **− 2,00 ; 9,51 ; 26,77** ; espérance **9,51**, écart-type **9,97** ; prix fixe de 64,49 sans complément : − 8,49 ; 9,51 ; 36,51 ; même espérance, écart-type **15,59** ; le complément réduit la perte du scénario faible et la dispersion | 1 |
| 3.6-06 | Conclusion : opération opportune si les synergies sont crédibles (création positive dès 0,81 M€ de synergies annuelles avant impôt) et si les talents restent ; négative sans synergies (− 5,49) ; critère du capital-risque non atteint ; conditions : fidélisation, présence des fondateurs, plafond de prix, traitement des risques de l'audit | 0,75 |

**Complément de prix espéré (0,75 pt).** Convention de l'annexe 3.7 : complément payé le 31/12/2028, actualisé au CMPC du studio sur deux ans (1,11^−2 = 0,811622).

| Scénario | Probabilité | Complément (M€) | Valeur actuelle (M€) |
|---|---:|---:|---:|
| Faible (CA de 10 M€ < 15) | 0,30 | 0,00 | 0,00 |
| Central (CA de 22 M€) | 0,50 | 8,00 | 6,49 |
| Fort (CA de 36 M€ > 30) | 0,20 | 20,00 | 16,23 |
| **Espérance** | | **8,00** | **6,49** |

Prix espéré = partie fixe + valeur actuelle du complément espéré = 58,00 + 6,49 = **64,49 M€** ; le prix maximal serait de 78,00 M€ en montant nominal (74,23 M€ en valeur actuelle), dans le scénario fort.

**Partage du risque et asymétrie d'information (0,75 pt).**
- **Partage du risque** : le complément rend une partie du prix **conditionnelle** au succès du second jeu, dont dépend la valeur du studio. NOCTÉVAL paie davantage quand le studio vaut davantage (scénario fort : 20,00 M€ pour une valeur supérieure de 27,00 M€) et ne paie rien de plus quand il vaut moins (scénario faible). Le risque d'avoir surpayé est en partie transféré aux vendeurs, qui partagent en contrepartie le gain du scénario fort. Le calcul de la VAN par scénario le mesure : l'écart-type passe de 15,59 à 9,97 M€ (item 3.6-05).
- **Asymétrie d'information** : les fondateurs connaissent mieux que NOCTÉVAL l'état du second jeu et l'engagement de l'équipe, et leur plan d'affaires est jugé optimiste. Selon Akerlof (1970), l'acheteur qui ne peut pas distinguer un bon studio d'un mauvais propose un prix moyen, et les meilleurs vendeurs se retirent. En acceptant qu'une part du prix dépende des ventes futures, les vendeurs confiants émettent un **signal crédible**, parce qu'il leur coûterait cher s'ils se trompaient (Spence, 1973) ; le désaccord sur les prévisions devient un pari sur un indicateur observable, ce qui rend l'accord possible.
- **Incitation** : les fondateurs restant à la direction jusqu'à la fin de 2029, le complément les intéresse au succès du jeu et à la rétention de l'équipe, comme un mécanisme d'alignement des intérêts (Jensen et Meckling, 1976). Limites : un indicateur de chiffre d'affaires de 2028 peut pousser à sacrifier la marge ou le jeu à plus long terme, et la mesure peut devenir une source de conflit.

**Synergies et création de valeur espérée (1 pt).**
- Synergies nettes d'impôt : 2,20 × (1 − 25 %) = 1,65 M€ par an ; valeur actuelle d'une rente perpétuelle au CMPC du studio : 1,65 / 0,11 = **15,00 M€**.
- Coûts d'intégration nets d'impôt : 4,00 × 0,75 = **3,00 M€**.
- **Création de valeur espérée** = VCP du studio seul + valeur actuelle des synergies − coûts d'intégration − prix espéré = 62,00 + 15,00 − 3,00 − 64,49 = **9,51 M€**.

**Prime payée (0,75 pt).**
- Prime = prix espéré − VCP du studio seul = 64,49 − 62,00 = **2,49 M€**, soit 2,49 / 62,00 = **4,02 %**.
- La création de valeur se lit aussi : synergies (15,00) − prime (2,49) − intégration (3,00) = 9,51 M€. NOCTÉVAL cède environ 17 % de la valeur des synergies aux vendeurs (guide p. 69-70 : la création de valeur dépend de la comparaison entre synergies et prime payée).
- Le prix espéré correspond à (64,49 − 8,30) / 7,40 = **7,59 fois l'EBITDA** de 2026 (6,72 fois pour la seule partie fixe), en dessous du multiple de 8,5 des transactions récentes : la prime reste modérée.

**VAN de l'acquisition par scénario (1 pt).** VAN = 62,00 + écart de valeur + 15,00 − 3,00 − 58,00 − valeur actuelle du complément.

| Scénario | Probabilité | VCP du studio seul | VA du complément | VAN avec complément | VAN avec un prix fixe de 64,49 |
|---|---:|---:|---:|---:|---:|
| Faible | 0,30 | 44,00 | 0,00 | **− 2,00** | − 8,49 |
| Central | 0,50 | 62,00 | 6,49 | **9,51** | 9,51 |
| Fort | 0,20 | 89,00 | 16,23 | **26,77** | 36,51 |
| **Espérance** | | 62,00 | 6,49 | **9,51** | **9,51** |
| **Écart-type** | | | | **9,97** | **15,59** |

- Avec le complément : variance = 0,30 × (− 2,00 − 9,51)² + 0,50 × 0² + 0,20 × (26,77 − 9,51)² = 39,74 + 0 + 59,58 = 99,32 (99,31 sur les VAN non arrondies) ; écart-type = **9,97 M€** (coefficient de variation 1,05). La VAN est négative avec une probabilité de 30 %, mais la perte est limitée à 2,00 M€.
- Avec un prix fixe de même espérance : écart-type = **15,59 M€** ; la perte du scénario faible atteint 8,49 M€. L'espérance est la même (9,51) : le complément ne crée pas de valeur en moyenne, il **réduit le risque** de l'acheteur, ce qui a de la valeur pour une entreprise dont les fondateurs détiennent 44 % du capital et dont la trésorerie finance aussi la suite des « Brumes d'Aldrec ».

**Conclusion (0,75 pt)** (exemple de réponse).
- L'opération est **opportune** : création de valeur espérée de 9,51 M€, prix espéré dans la fourchette de valeur (50 à 71 M€) et inférieur au multiple des transactions, risque partagé par le complément.
- Mais elle ne crée de valeur que **grâce aux synergies** : sans elles, elle détruirait 5,49 M€ (62,00 − 3,00 − 64,49). La création est positive dès 0,81 M€ de synergies annuelles avant impôt ((2,49 + 3,00) × 0,11 / 0,75), soit 37 % des 2,20 M€ prévus : la marge de sécurité est confortable si l'adaptation aux consoles est réaliste. Au regard du critère du comité (TRI de 20 %), le prix est trop élevé (TRI obtenu de 16,41 % au prix fixe) : le comité devra arbitrer entre son critère et la valeur par les flux.
- **Conditions** : préserver les talents (primes de fidélisation, organisation des fins de production, maintien des fondateurs au-delà de 2029 si possible) ; ne pas surenchérir face à PARVIGNE Entertainment au-delà de la valeur des synergies ; traiter avant la signature les risques de l'audit d'acquisition (achats intégrés, question 3.8), dont l'effet sur la valeur n'est pas compris dans les flux.

**Réponses tolérées** : création de valeur calculée par les flux de l'acquisition (date 0 : − 58,00 − 3,00 + 8,30 ; années 1 à 5 : flux disponibles + 1,65, moins le complément espéré de 8,00 en 2028, plus en 2031 les valeurs terminales du studio et des synergies, 61,20 et 15,00), qui donne la même VAN de 9,51 M€ ; complément espéré non actualisé (prix espéré de 66,00 M€, création de 8,00 M€), sanctionné une fois à l'item 3.6-01 ; conclusion défavorable si elle s'appuie sur le critère du comité et sur la fragilité des talents, chiffres à l'appui.

**Erreurs fréquentes**
- Additionner la partie fixe et le complément maximal (78,00 M€) comme prix de l'opération.
- Oublier les coûts d'intégration, ou les compter avant impôt.
- Comparer le prix à la valeur des transactions (71,20 M€), qui comprend déjà des synergies, et conclure à une « bonne affaire » de 6,71 M€.
- Analyser la rédaction du complément ou son traitement comptable (UE 1 et UE 4).
- `JUR-T04` — actualisation et espérance non maîtrisées ; `JUR-M01` — asymétrie d'information et signal non mobilisés ; `JUR-T10` — commentaire sans calcul, ou l'inverse.

---

### 3.7 Coût de l'emprunt et de la trésorerie, effets sur la structure financière, financement hiérarchique (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Flux de l'emprunt (59,70 ; − 14,64 ; − 14,11 ; − 13,58 ; − 13,06 ; − 12,53) ; coût actuariel avant impôt **4,58 %** (4,59 % par interpolation entre 4 % et 5 %), après impôt **3,44 %** (4,58 % × 0,75, approximation admise par l'énoncé) ; trésorerie : 3,00 % avant impôt, **2,25 %** après impôt ; la trésorerie est moins chère | 0,75 |
| 3.7-02 | Après l'opération : solution 1 trésorerie **216,10**, dette **1,80**, trésorerie nette **214,30** ; solution 2 trésorerie **275,80**, dette **61,80**, trésorerie nette **214,00** ; même position nette (à 0,30 près) ; coût de portage la première année **0,84 M€** avant impôt, **0,63 M€** après impôt | 0,5 |
| 3.7-03 | Financement hiérarchique : autofinancement d'abord, puis dette, puis émission d'actions, à cause de l'asymétrie d'information ; recommandation argumentée (trésorerie, ou emprunt pour garder une réserve de liquidité avant la sortie de 2028) ; théorie du compromis peu applicable à un groupe sans dette nette | 0,75 |

**Coûts comparés (0,75 pt).** Emprunt de 60,00 M€ à 4,40 %, amortissement constant de 12,00 M€ par an ; frais de 0,30 M€ déduits du montant reçu, économie d'impôt à la date 0.

| Année | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Capital restant dû en début d'année | | 60,00 | 48,00 | 36,00 | 24,00 | 12,00 |
| Intérêts (4,40 %) | | 2,64 | 2,11 | 1,58 | 1,06 | 0,53 |
| Flux avant impôt | 59,70 | − 14,64 | − 14,11 | − 13,58 | − 13,06 | − 12,53 |
| Flux après impôt (intérêts et frais × 0,75) | 59,78 | − 13,98 | − 13,58 | − 13,19 | − 12,79 | − 12,40 |

- Coût actuariel avant impôt : VAN des flux de 0,6656 à 5 % et de − 0,9578 à 4 % ; taux exact **4,58 %** (4,59 % par interpolation). Après impôt, l'approximation permise par l'énoncé donne 4,58 % × 0,75 = **3,44 %**, égal au taux exact de 3,44 % (VAN de 0,9262 à 4 % et de − 0,7294 à 3 %, calcul non exigé).
- **Trésorerie** : son coût est le rendement auquel le groupe renonce, 3,00 % avant impôt, soit 3,00 % × 0,75 = **2,25 %** après impôt. Financer par la trésorerie coûte environ 1,2 point de moins après impôt.

**Effets sur la structure financière (0,5 pt).** Situation juste après l'opération, studio compris (convention de l'annexe 3.7, M€).

| | Solution 1 : trésorerie | Solution 2 : emprunt |
|---|---:|---:|
| Trésorerie (268,00 − 62,00 [+ 60,00 − 0,30] + 10,10) | **216,10** | **275,80** |
| Dette financière (emprunt du studio 1,80 [+ 60,00]) | **1,80** | **61,80** |
| Trésorerie nette | **214,30** | **214,00** |

- La trésorerie nette du groupe est la même dans les deux cas, aux frais près : l'emprunt n'apporte aucun financement net, il garde **59,70 M€ de liquidité** en contrepartie d'une dette. Le rachat consomme 62,00 / 268 = 23,13 % de la trésorerie.
- **Coût de portage** de la première année : intérêts de 60,00 × 4,40 % = 2,64 M€ contre 60,00 × 3,00 % = 1,80 M€ de produits de placement sur le montant emprunté (convention de l'annexe 3.7), soit **0,84 M€** avant impôt et **0,63 M€** après impôt ; il décroît avec le remboursement (7,92 M€ d'intérêts sur cinq ans).
- Le service de la dette de la première année (14,64 M€) représente près de deux fois l'EBITDA du studio (7,40 M€) : il serait payé par le groupe, pas par la cible. La dette reste faible au regard de la trésorerie : le groupe ne prend pas de risque de solvabilité.

**Financement hiérarchique et recommandation (0,75 pt).**
- Selon Myers et Majluf (1984), l'asymétrie d'information entre dirigeants et investisseurs fait préférer l'**autofinancement**, puis la **dette**, et en dernier l'**émission d'actions**, que le marché interprète comme le signe d'actions surévaluées. NOCTÉVAL dispose de 268 M€ de trésorerie : la théorie conduit à financer le rachat par la trésorerie, la solution la moins chère (2,25 % contre 3,44 % après impôt). L'émission d'actions, au dernier rang, est d'ailleurs écartée par les fondateurs, qui y perdraient aussi du contrôle.
- La théorie du compromis (Myers, 1977) apporte peu : avec une trésorerie nette, l'économie d'impôt sur les intérêts est compensée par l'impôt sur les placements conservés ; seul l'écart de taux compte, et il est défavorable.
- **Recommandation** (exemple) : financer le rachat par la **trésorerie**. L'emprunt se justifierait seulement comme une assurance de liquidité, payée 0,63 M€ après impôt la première année, si le conseil retenait aussi d'importants retours aux actionnaires et la réserve de la suite des « Brumes d'Aldrec » : NOCTÉVAL garderait alors une marge de sécurité jusqu'à la sortie de l'automne 2028 et le paiement éventuel du complément (jusqu'à 20,00 M€).

**Réponses tolérées** : recommandation de l'emprunt fondée sur la liquidité et la prudence avant la sortie de 2028, si le coût de portage est chiffré ; coût après impôt calculé sur les flux après impôt arrondis (3,43 %) ; interpolations au centième près ; coût de portage calculé sur les 59,70 M€ nets des frais (0,85 et 0,64 M€).

**Erreurs fréquentes**
- Calculer des intérêts constants sur 60,00 M€ alors que l'emprunt s'amortit (`JUR-T04` : tableau d'amortissement de l'emprunt, acquis du DCG).
- Considérer la trésorerie comme gratuite : son coût est le rendement perdu.
- Attribuer le financement hiérarchique à Modigliani et Miller.
- `JUR-T06` — théorie citée sans application au cas ; `JUR-T14` — confusion entre financement hiérarchique et compromis.

---

### 3.8 Double matérialité des enjeux de l'audit d'acquisition et publication après l'intégration (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.8-01 | Pour chaque enjeu (fins de production, départs et dépendance aux personnes clés, achats intégrés dans un jeu pour enfants, consommation des serveurs) : impact sur les personnes ou l'environnement et effet sur la valeur, chiffres du cas à l'appui (340 h ; 19 % de départs ; 6,82 M€ dont 2,64 M€ de coffres, 12 % du chiffre d'affaires ; 1 450 demandes de remboursement ; 1 200 à 4 000 MWh) ; enjeux matériels sur les deux plans sauf l'énergie, surtout d'impact ; information non vérifiée | 1,25 |
| 3.8-02 | Après l'intégration : VELTRANE entre dans le périmètre de l'état de durabilité consolidé de NOCTÉVAL (publication poursuivie à partir de 2027 par décision du conseil, sans discussion de l'assujettissement) ; mise à jour de l'analyse de double matérialité (protection des jeunes joueurs et énergie des serveurs à réexaminer) ; impacts, risques et opportunités, politiques, actions, objectifs et indicateurs couvrant le studio ; collecte et fiabilité des données ; le studio n'a pas à publier son propre rapport | 0,75 |

**Double matérialité des enjeux (1,25 pt).** Un enjeu est matériel par ses **impacts** (effets de l'entreprise sur les personnes et l'environnement) ou par ses **effets financiers** (flux, risques, accès au financement, coût du capital), ou par les deux (fiche commune § 1).

| Enjeu | Matérialité d'impact (le studio sur les personnes et l'environnement) | Matérialité financière (effet sur la valeur du studio) |
|---|---|---|
| Charge de travail en fin de production | élevée : 340 heures supplémentaires par développeur en six mois, risques pour la santé ; aucun plan de charge pour le second jeu | élevée : épuisement et départs qui retardent ou dégradent le second jeu (scénario faible : − 18,00 M€), coûts de recrutement, réputation d'employeur |
| Départs et dépendance aux personnes clés | moyenne : stabilité de l'emploi et des équipes | élevée : 19 % de départs, 3 responsables sur 9 partis, directeur technique sur le départ ; la valeur tient aux talents (ANCC de 18,10 contre 62,00) |
| Achats intégrés dans un jeu classé à partir de 7 ans | élevée : dépenses d'enfants non maîtrisées (contrôle parental désactivé, 1 450 demandes de remboursement), incitation au jeu par les coffres au contenu aléatoire | élevée : 6,82 M€, soit 31 % du chiffre d'affaires, dont 2,64 M€ de coffres (12 % du chiffre d'affaires ; la marge perdue pèserait une part notable de l'EBITDA de 7,40 M€) menacés par les règles des boutiques en 2028 ; risque de réputation, qui toucherait aussi NOCTÉVAL, et risque pour le modèle du second jeu |
| Consommation des serveurs | moyenne : électricité de 1 200 MWh en 2026 ; le second jeu consommerait à lui seul 4 000 MWh par an, 3,33 fois plus que le premier (5 200 MWh si les deux restent en ligne, 4,33 fois la consommation de 2026) ; émissions inconnues, chez le prestataire (chaîne de valeur) | faible à moyenne : coût de l'hébergement refacturé par le prestataire, exigences futures des parties prenantes ; données à constituer |

- Les deux premiers enjeux et les achats intégrés sont matériels sur les deux plans ; la consommation des serveurs relève surtout de l'impact, et sa mesure manque. L'effet financier de ces enjeux n'est **pas** compris dans les flux de l'annexe 3.4 : il justifie de la prudence dans le prix, une part conditionnelle et des engagements des vendeurs.
- Ces informations n'ont été vérifiées par aucun tiers et le studio ne publie rien : l'asymétrie d'information porte aussi sur l'extra-financier, d'où l'intérêt de l'audit d'acquisition.

**Ce que l'état de durabilité consolidé de NOCTÉVAL devra présenter (0,75 pt).**
- VELTRANE, filiale détenue à 100 %, entrera dans le **périmètre de l'état de durabilité consolidé** de NOCTÉVAL, qui couvre le même périmètre que les comptes consolidés et que le conseil a décidé de continuer à publier à partir de 2027 ; le studio n'aura pas à publier son propre rapport. L'assujettissement du groupe n'est pas à discuter.
- NOCTÉVAL devra **mettre à jour son analyse de double matérialité** : la protection des jeunes joueurs, jugée non matérielle parce que ses jeux visent les adultes, le devient avec un jeu classé à partir de 7 ans et ses achats intégrés ; la consommation d'énergie des serveurs prend du poids avec un jeu en ligne ; les conditions de travail, déjà matérielles, s'étendent au studio.
- Pour ces enjeux, l'état de durabilité présentera les **impacts, risques et opportunités**, les politiques, les actions et les objectifs du groupe (organisation des fins de production, contrôle parental activé par défaut, abandon des coffres payants dans les jeux pour enfants, choix de l'hébergeur), et des **indicateurs** couvrant le studio (effectif, départs, heures supplémentaires, achats intégrés et remboursements, électricité consommée) ; il faudra organiser la collecte et la fiabilité de données que le studio ne produit pas aujourd'hui.

**Réponses tolérées** : classement différent d'un enjeu (par exemple énergie des serveurs jugée non matérielle) s'il est justifié par les deux dimensions ; référence aux thèmes « personnel de l'entreprise », « consommateurs et utilisateurs finaux » et « changement climatique » des ESRS, sans numérotation ; mention de la VSME comme norme volontaire possible pour le studio s'il restait indépendant.

**Erreurs fréquentes**
- Ne présenter qu'une matérialité (l'impact ou le risque financier).
- Traiter les achats intégrés comme une question de morale professionnelle du cabinet, au lieu d'un enjeu extra-financier du studio.
- Affirmer que le studio devra publier son propre rapport de durabilité, ou détailler les exigences techniques des normes.
- `JUR-D01` — confusion entre démarche RSE et critères ESG ; `JUR-T05` — extra-financier sans lien avec la valeur ; `JUR-T15` — dernière question bâclée.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 69-70 ; programme l. 548-554 | motifs des acquisitions, synergies, création de valeur, prime payée | [V] | F05 § 5 |
| Guide pédagogique DSCG, juillet 2026, p. 65-67 ; programme l. 530-536 | ANC, ANCC, retraitements, cycle de vie, méthode du capital-risque | [V] | F03 § 4, 7 et 8 |
| Guide pédagogique DSCG, juillet 2026, p. 64-65 ; programme l. 508-528 | flux de trésorerie disponibles, CMPC, valeur terminale, VGE et VCP, multiples de transactions | [V] | F03 § 2 et 3 |
| Guide pédagogique DSCG, juillet 2026, p. 80-81 ; programme l. 642-648 | scénarios, espérance et écart-type de la VAN, création de valeur | [V] | F01 § 4 et 5 |
| Guide pédagogique DSCG, juillet 2026, p. 81-82 ; programme l. 653-663 | coût actuariel des financements, structure financière, théories du financement | [V] | F01 § 3 |
| Guide pédagogique DSCG, juillet 2026, p. 59-60 ; programme l. 476-490 | lecture du reporting de durabilité, double matérialité | [V] | F08 § 2 |
| Fiche commune CSRD, ESRS et double matérialité, § 1, 2 et 5 | matérialité d'impact et matérialité financière ; thèmes des ESRS ; norme volontaire VSME | [V dans la fiche commune] | fiche commune |
| Gordon et Shapiro (1956) | valeur terminale à croissance constante | [V programme 3.1] | F10 § 2 |
| Akerlof (1970) ; Spence (1973) | asymétrie d'information ; signal coûteux et crédible | [V programme 5.1 et 4.1] | F10 § 1 et 3 |
| Jensen et Meckling (1976) | alignement des intérêts des dirigeants | [V programme 2.1] | F10 § 3 |
| Myers et Majluf (1984) ; Myers (1977) | financement hiérarchique ; théorie du compromis | [V programme 7.2] | F10 § 3 |
| CMPC du studio de 11,00 %, croissance de 2,0 %, multiple de 8,5 fois l'EBITDA, multiple de sortie de 16, TRI exigé de 20 %, rendement des placements de 3,00 %, taux de l'emprunt de 4,40 % | hypothèses d'énoncé, cohérentes avec F11 | [S] | F11 § 1 et 3 |
| Bilan, corrections, flux, scénarios, synergies, coûts d'intégration, informations de l'audit d'acquisition | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 3.1 à 3.6 |
