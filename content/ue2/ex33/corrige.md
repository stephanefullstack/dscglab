# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 33 — Dossier 3 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (bilan, ANC et ANCC, impôt latent, rente du goodwill, valeur patrimoniale, bêtas de l'échantillon, coût des fonds propres et CMPC, flux actualisés, valeur terminale, VGE et VCP, prix par action, actions nouvelles et répartition du capital, barème, liste noire, hors-programme ; méthode du capital-risque, indicateurs du cycle de vie et comparaisons vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VCP calculée avec un CMPC erroné, ou une comparaison des méthodes fondée sur une valeur erronée).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Cycle de vie et choix des méthodes | `3.3.c` Savoir calculer la valeur d'une entreprise en fonction de son cycle de vie | 1,5 |
| 3.2 ANC, ANCC, goodwill et limites de l'approche patrimoniale | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine ; `3.3.b` Savoir calculer la survaleur de l'entreprise à partir de ses actifs intangibles (goodwill) | 4,5 |
| 3.3 CMPC, flux actualisés, valeur terminale, VGE et VCP | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance ; `3.1.d` Distinguer la valeur globale de l'entreprise (VGE) de la valeur des capitaux propres (VCP) | 5,5 |
| 3.4 Méthode du capital-risque et comparaison des méthodes | `3.3.c` | 2,5 |
| 3.5 Fourchette, prix d'entrée et négociation | `3.3.c` ; `3.1.d` | 2 |
| **Total** | | **16** |

Part du calcul : environ 10 points (3.2-01 à 3.2-04, 3.3-01 à 3.3-06, 3.4-01 et 3.4-02, la moitié de 3.5-01 et de 3.5-02). Part de l'analyse : environ 6 points. Les questions 3.1, 3.4 et 3.5 relient les calculs au stade de développement de la société : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 Cycle de vie et choix des méthodes (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Stade de croissance, sortie de la phase de création, justifié par des indicateurs chiffrés : chiffre d'affaires + 200 %, + 116,67 % puis + 73,08 % ; clients + 72,22 % en 2026 ; premier résultat positif (0,05 M€) après 3,75 M€ de pertes ; flux négatifs en 2027 et 2028 (− 1,60 M€) ; croissance prévue ramenée de 55,56 % à 12,90 % | 0,5 |
| 3.1-02 | Méthodes adaptées et pourquoi : capital-risque (horizon de sortie, TRI exigé, risque d'échec) ; flux actualisés utiles mais fragiles (valeur terminale dominante) ; approche patrimoniale réduite à un plancher (valeur portée par l'immatériel) ; croiser les méthodes | 1 |

**Stade du cycle de vie (0,5 pt).** Le guide (p. 67) distingue quatre stades : création, croissance, maturité, déclin. ALTIMOISSON est **en croissance**, au sortir de la phase de création :
- **une croissance très rapide qui ralentit** : chiffre d'affaires de 0,40 M€ en 2023 à 4,50 M€ en 2026 (+ 200 % en 2024, + 116,67 % en 2025, + 73,08 % en 2026) ; exploitations clientes de 300 à 6 200 (+ 72,22 % en 2026) ; effectif de 6 à 41 personnes. Les prévisions gardent une forte croissance, en baisse régulière : + 55,56 % en 2027, + 12,90 % en 2031 ;
- **une rentabilité à peine atteinte** : 2026 est le premier exercice bénéficiaire (0,05 M€, soit 1,11 % du chiffre d'affaires), après 3,75 M€ de pertes cumulées de 2022 à 2025 ; la marge nette prévue atteint 14,86 % en 2031 ;
- **des besoins de financement** : les flux de trésorerie disponibles restent négatifs en 2027 et en 2028 (− 1,60 M€ au total), pour financer de nouveaux modules et des recrutements ; aucun dividende avant 2032 ;
- **une valeur surtout immatérielle et des risques élevés** : plateforme logicielle, fichier de clients, équipe, données ; dépendance envers trois assureurs (62 % du chiffre d'affaires) et quelques personnes clés.

Ce n'est plus une création (le produit est vendu, la société est rentable), ce n'est pas encore la maturité (croissance supérieure à 10 % par an, flux négatifs, résultat très faible).

**Méthodes adaptées à ce stade (1 pt).**
- **Méthode du capital-risque** : c'est la méthode d'évaluation propre aux jeunes sociétés au programme (guide, p. 67). Elle part de la valeur espérée à l'horizon de sortie de l'investisseur et l'actualise au TRI qu'il exige, qui rémunère le risque d'échec et l'illiquidité. Elle correspond exactement à la situation de la mutuelle : un apport minoritaire, une sortie envisagée dans cinq ans, un TRI fixé par son conseil.
- **Flux de trésorerie actualisés** : méthode de référence pour une entreprise en croissance, puisque sa valeur vient de ses flux futurs. Mais les premiers flux sont négatifs ou faibles, si bien que la valeur repose surtout sur la valeur terminale, et les prévisions sont établies par les dirigeants : la méthode est utile, à condition d'en mesurer la sensibilité.
- **Approche patrimoniale** : peu pertinente pour une société dont la valeur tient à l'immatériel et à la croissance. Elle donne un **plancher** (valeur des actifs si la croissance ne venait pas) ; le goodwill ne capte qu'une partie des perspectives.
- **Comparables** : possibles en théorie, mais les sociétés cotées comparables sont plus grandes et matures, et les agrégats d'ALTIMOISSON (résultat de 0,05 M€) sont trop faibles pour être multipliés ; le dossier ne les retient pas.
- Aucune méthode ne suffit seule : il faut **croiser** les approches pour bâtir une fourchette de négociation (`JUR-E03`).

**Réponses tolérées** : société qualifiée de « fin de création » ou de « début de croissance », si les indicateurs sont cités ; mention de l'approche par les multiples comme méthode de recoupement, sans calcul ; méthode des flux actualisés présentée comme méthode principale du stade de croissance (guide, p. 67), et méthode du capital-risque comme approche de l'investisseur minoritaire qui prévoit une sortie : réponse acceptée pour la totalité des points.

**Erreurs fréquentes**
- Qualifier la société de mature parce qu'elle a atteint l'équilibre, ou de start-up en création alors qu'elle réalise 4,50 M€ de chiffre d'affaires.
- Citer d'autres méthodes d'évaluation des jeunes sociétés, hors programme : seule la méthode du capital-risque est attendue.
- `JUR-T13` — exposé général sur le cycle de vie sans les chiffres de l'annexe 3.1.

---

### 3.2 ANC, ANCC, goodwill et limites de l'approche patrimoniale (4,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | ANC = 5,20 − 0,80 − 0,90 = 3,50 M€, soit 7,00 € par action | 0,5 |
| 3.2-02 | Corrections + 1,60 (plateforme) et + 1,20 (fichier de clients) ; impôt latent 0,70 ; ANCC = 3,50 + 2,80 − 0,70 = 5,60 M€, soit 11,20 € par action | 1 |
| 3.2-03 | Rentes du goodwill = bénéfice associé − 6 % × 5,00 : 0,10 ; 0,60 ; 1,20 ; 1,80 ; 2,30 M€ | 0,5 |
| 3.2-04 | Rentes actualisées à 12 % : 0,09 ; 0,48 ; 0,85 ; 1,14 ; 1,31 ; goodwill 3,87 M€ ; valeur patrimoniale = 5,60 + 3,87 = 9,47 M€ (par action : 18,94 €, non exigé) | 1 |
| 3.2-05 | Interprétation du goodwill et limites de l'approche pour une société en croissance (croissance après 2031 et immatériel non inscrit ignorés, rente sur cinq ans, valeurs estimées, valeur d'une entreprise qui continue) | 1,5 |

**Conventions rappelées** (annexes 3.2 et 3.6) : liste limitative des corrections ; impôt latent de 25 % sur chaque correction ; CPNE de 5,00 M€ et bénéfices associés fournis ; rémunération normale de 6 % ; actualisation de la rente à 12 % sur cinq ans ; 500 000 actions.

**ANC (0,5 pt).** ANC = total de l'actif − dettes = 5,20 − (0,80 + 0,90) = **3,50 M€**, égal aux capitaux propres comptables (7,20 − 3,75 + 0,05). Par action : 3,50 M€ / 500 000 = **7,00 €**. Les pertes accumulées pendant la création (3,75 M€) ont absorbé une grande partie des 7,20 M€ apportés par les actionnaires.

**ANCC (1 pt).**

| | M€ |
|---|---:|
| ANC | 3,50 |
| + Plateforme logicielle : 3,20 − 1,60 | + 1,60 |
| + Fichier des exploitations clientes (non inscrit) | + 1,20 |
| − Impôt latent : 25 % × (1,60 + 1,20) | − 0,70 |
| **= ANCC** | **5,60** |

Par action : 5,60 M€ / 500 000 = **11,20 €**. Les corrections portent sur les deux actifs qui font la valeur de la société et que le bilan sous-évalue : la plateforme, inscrite au coût de développement amorti, et le fichier de clients, créé par la société et donc absent du bilan. L'impôt latent traduit l'impôt qui serait dû si ces plus-values étaient réalisées.

**Rente du goodwill (0,5 pt).** La rente (ou superprofit) est le bénéfice qui dépasse la rémunération normale des capitaux nécessaires à l'exploitation : rente = bénéfice associé − 6 % × 5,00 = bénéfice associé − 0,30.

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Bénéfice associé (résultat net prévu) | 0,40 | 0,90 | 1,50 | 2,10 | 2,60 |
| − Rémunération normale des CPNE (6 % × 5,00) | − 0,30 | − 0,30 | − 0,30 | − 0,30 | − 0,30 |
| **= Rente du goodwill** | **0,10** | **0,60** | **1,20** | **1,80** | **2,30** |
| Coefficient 1,12^−t | 0,8929 | 0,7972 | 0,7118 | 0,6355 | 0,5674 |
| Rente actualisée | 0,09 | 0,48 | 0,85 | 1,14 | 1,31 |

**Goodwill et valeur patrimoniale (1 pt).**
- Goodwill = 0,09 + 0,48 + 0,85 + 1,14 + 1,31 = **3,87 M€**.
- Valeur patrimoniale = ANCC + goodwill = 5,60 + 3,87 = **9,47 M€**, soit **18,94 €** par action.

**Interprétation et limites pour une société en croissance (1,5 pt).**
- **Ce que mesure le goodwill** : la capacité d'ALTIMOISSON à rapporter plus que la rémunération normale de ses capitaux d'exploitation, grâce à des éléments qui ne figurent pas, ou mal, à l'actif : savoir-faire de l'équipe, modèles d'estimation des dommages, données accumulées, relations avec les assureurs, marque auprès des exploitants (guide, p. 66). Il représente 40,87 % de la valeur patrimoniale (3,87 / 9,47).
- **Ce que l'approche laisse de côté** :
  - **la croissance après 2031** : la rente est limitée à cinq ans, alors que la société a toutes les chances d'exister et de croître au-delà ; le plan fait passer le résultat de 0,40 à 2,60 M€, et la valeur créée ensuite est ignorée ;
  - **la montée progressive des bénéfices** : la rente de 2027 (0,10 M€) est presque nulle, et l'essentiel du goodwill vient des années les plus lointaines, donc les plus incertaines ;
  - **l'immatériel non retenu** : seuls deux actifs sont réévalués ; l'équipe, les données et les contrats avec les assureurs ne le sont pas ;
  - **les besoins de financement** : la rente se calcule sur des CPNE constants de 5,00 M€, alors que la société va investir (flux négatifs en 2027 et 2028) ; ce que coûte la croissance n'apparaît pas ;
  - **des valeurs estimées et une hypothèse de continuité** : le coût de reconstitution de la plateforme et la valeur du fichier n'ont de sens que si l'activité continue ; en cas d'échec, ils vaudraient beaucoup moins.
- **Conclusion** : l'ANCC (5,60 M€) est un **plancher** de négociation ; la valeur patrimoniale avec goodwill (9,47 M€) rapproche le patrimoine de la rentabilité, sans mesurer la croissance qui fait l'essentiel de la valeur d'une jeune société.

**Réponses tolérées** : ANC présenté comme capitaux propres comptables ; rentes actualisées non arrondies (goodwill 3,87 M€, valeur 9,47 M€) ; goodwill calculé en une seule expression ; mention du goodwill négatif possible (badwill) si la rente l'était, sans calcul.

**Erreurs fréquentes**
- Oublier l'impôt latent (ANCC de 6,30 M€) ou ne l'appliquer qu'à la plateforme (5,90 M€).
- Ajouter le goodwill à l'ANC au lieu de l'ANCC (7,37 M€).
- Actualiser la rente au taux de rémunération de 6 % (goodwill de 4,78 M€) ou additionner les rentes sans les actualiser (6,00 M€).
- Refaire, à partir du bilan, les bases du goodwill (capitaux permanents nécessaires à l'exploitation, bénéfices associés) au lieu d'utiliser les montants fournis de l'annexe 3.2.
- `JUR-E03` — présenter la valeur patrimoniale sans dire ce qu'elle ne mesure pas pour une société en croissance.
- `JUR-T07` — rentes présentées sans tableau.

---

### 3.3 CMPC, flux actualisés, valeur terminale, VGE et VCP (5,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Bêtas désendettés : 1,2000 ; 1,0000 ; 1,0800 ; 1,2000 ; moyenne 1,1200 | 0,5 |
| 3.3-02 | D/CP cible = 20 / 80 = 0,25 ; bêta réendetté = 1,1200 × 1,1875 = 1,3300 | 0,5 |
| 3.3-03 | ke = 4 % + 1,3300 × 5 % + 3 % = 13,65 % ; kd après impôt = 3,75 % ; CMPC = 80 % × 13,65 % + 20 % × 3,75 % = 11,67 % | 1 |
| 3.3-04 | Flux actualisés à 11,67 % : − 1,25 ; − 0,16 ; 0,57 ; 0,90 ; 1,04, soit 1,10 M€ | 1 |
| 3.3-05 | Valeur terminale 2031 = 1,80 × 1,02 / 0,0967 = 18,99 M€, actualisée 10,93 M€ | 0,5 |
| 3.3-06 | VGE = 1,10 + 10,93 = 12,03 M€ ; trésorerie nette = 2,10 − 0,80 = 1,30 M€ ; VCP = 12,03 + 1,30 = 13,33 M€ (par action : 26,66 €, non exigé), avant l'apport | 1 |
| 3.3-07 | Part de la valeur terminale : 90,86 % de la VGE ; commentaire (sensibilité au CMPC et à la croissance, plan établi par les dirigeants, risque d'échec non pris en compte par les flux d'un scénario de réussite) | 1 |

**Conventions rappelées** (annexes 3.3, 3.4 et 3.6) : formule de Hamada avec impôt ; moyenne arithmétique ; bêtas à quatre décimales ; ke arrondi dans le CMPC, CMPC arrondi pour l'actualisation ; flux de trésorerie disponibles fournis, à utiliser tels quels ; croissance de 2 % à l'infini ; VCP = VGE + trésorerie nette au 31/12/2026.

**Bêtas désendettés de l'échantillon (0,5 pt).** β désendetté = β des capitaux propres / [1 + (1 − 25 %) × D/CP] :

| Société | β des capitaux propres | D/CP | 1 + 0,75 × D/CP | β désendetté |
|---|---:|---:|---:|---:|
| ASSURELLO | 1,38 | 0,20 | 1,15 | 1,2000 |
| KLARVIK | 1,30 | 0,40 | 1,30 | 1,0000 |
| MEDORAN Courtage | 1,08 | 0,00 | 1,00 | 1,0800 |
| HOLTVEER | 1,74 | 0,60 | 1,45 | 1,2000 |
| **Moyenne** | | | | **1,1200** |

Le bêta désendetté mesure le risque économique du métier (distribution d'assurance en ligne et logiciels de sinistres), sans l'effet de la dette propre à chaque société. MEDORAN Courtage, sans dette, a un bêta désendetté égal à son bêta des capitaux propres.

**Bêta réendetté (0,5 pt).** D/CP cible = 20 % / 80 % = **0,25** ; β des capitaux propres = 1,1200 × (1 + 0,75 × 0,25) = 1,1200 × 1,1875 = **1,3300**.

**Coût des fonds propres et CMPC (1 pt).**
- ke = 4 % + 1,3300 × 5 % + 3 % = 4,00 % + 6,65 % + 3,00 % = **13,65 %** (MEDAF de Sharpe, 1964, majoré de la prime de taille et d'illiquidité).
- kd après impôt = 5 % × (1 − 25 %) = **3,75 %**.
- CMPC = 80 % × 13,65 % + 20 % × 3,75 % = 10,92 % + 0,75 % = **11,67 %**.

Le CMPC actualise les flux de trésorerie disponibles parce que ces flux reviennent à tous les apporteurs de capitaux, actionnaires et prêteurs (guide, p. 64). La prime de 3 % traduit la petite taille et l'illiquidité des titres d'ALTIMOISSON, que le bêta de sociétés cotées ne mesure pas.

**Flux actualisés (1 pt).**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| FTD (M€) | − 1,40 | − 0,20 | 0,80 | 1,40 | 1,80 |
| Coefficient 1,1167^−t | 0,8955 | 0,8019 | 0,7181 | 0,6431 | 0,5759 |
| FTD actualisé | − 1,25 | − 0,16 | 0,57 | 0,90 | 1,04 |

Somme des flux actualisés : **1,10 M€**. Les flux négatifs de 2027 et de 2028 effacent presque la valeur des trois années suivantes.

**Valeur terminale (0,5 pt).** Flux de 2032 = 1,80 × 1,02 = 1,836 M€ ; VT au 31/12/2031 = 1,836 / (11,67 % − 2 %) = 1,836 / 0,0967 = **18,99 M€** (Gordon et Shapiro) ; actualisée : 18,9866 × 1,1167^−5 = **10,93 M€**.

**VGE et VCP (1 pt).**
- VGE = 1,10 + 10,93 = **12,03 M€** : valeur de l'actif économique, qui revient à tous les apporteurs de capitaux.
- Trésorerie nette au 31/12/2026 = disponibilités − dettes financières = 2,10 − 0,80 = **1,30 M€** : ALTIMOISSON a plus de trésorerie que de dettes ; on l'ajoute donc à la VGE au lieu de retrancher une dette.
- VCP = 12,03 + 1,30 = **13,33 M€**, soit 26,66 € par action. C'est une valeur **avant l'apport** de la mutuelle : les 2,50 M€ apportés augmenteront la trésorerie et donc la VCP après l'opération, sans rien changer à la VGE, qui ne dépend que des flux d'exploitation.

**Part de la valeur terminale et commentaire (1 pt).**
- Part : 10,93 / 12,03 = **90,86 %** de la VGE (90,88 % sans arrondi, accepté) : plus de neuf dixièmes de la valeur viennent d'après 2031.
- **Sensibilité** (calculs facultatifs, sans arrondi intermédiaire) : VCP en M€ selon le CMPC et la croissance à l'infini.

| CMPC \ g | 1 % | 2 % | 3 % |
|---|---:|---:|---:|
| 10,67 % | 13,80 | 15,24 | 17,04 |
| 11,67 % | 12,21 | 13,33 | 14,71 |
| 12,67 % | 10,90 | 11,80 | 12,88 |

Un point de CMPC ou de croissance déplace la VCP de 1,1 à 1,9 M€, soit 8 % à 14 % de sa valeur.
- **Lecture pour une société en croissance** : c'est la situation typique d'une jeune société, dont les flux sont négatifs au début et dont la valeur dépend de sa réussite future. La valeur terminale suppose que le flux de 2031 est normatif, alors que la croissance prévue y est encore de 12,90 % et que la société investit ; elle dépend d'une prévision à cinq ans établie par les dirigeants, qui ont intérêt à présenter un plan favorable (asymétrie d'information, Akerlof, 1970).
- Les flux de l'annexe 3.3 correspondent à un **scénario de réussite**, et non à une espérance tenant compte du risque d'échec. Le CMPC, fondé sur le bêta de sociétés cotées et établies, ne rémunère pas ce risque : la VCP de 13,33 M€ est donc plutôt un **plafond**.

**Réponses tolérées** : coefficients d'actualisation arrondis à quatre décimales, avec des écarts de 0,01 M€ ; valeur terminale actualisée à partir de la valeur arrondie (10,94 M€, VGE de 12,04 M€ et VCP de 13,34 M€) ; part de la valeur terminale calculée sans arrondi intermédiaire (90,88 %).

**Erreurs fréquentes**
- Réendetter avec D/VGE (0,20) au lieu de D/CP (0,25) : bêta de 1,2880, ke de 13,44 %, CMPC de 11,50 % et VCP de 13,62 M€ (13,63 M€ sans arrondi intermédiaire).
- Faire la moyenne des bêtas des capitaux propres (1,3750) sans les désendetter, ou appliquer la formule sans impôt (bêta désendetté moyen de 1,0615, ke de 13,63 %) alors que l'annexe impose la formule avec impôt.
- Multiplier la prime de taille et d'illiquidité par le bêta, ou l'oublier (ke de 10,65 % et CMPC de 9,27 %).
- Actualiser les flux au coût des fonds propres de 13,65 % : VGE de 9,26 M€ et VCP de 10,56 M€.
- Oublier de multiplier le flux de 2031 par (1 + g) : VT de 18,61 M€ et VCP de 13,12 M€ ; actualiser la valeur terminale sur six ans (9,79 M€, VCP de 12,19 M€).
- Retrancher la trésorerie nette au lieu de l'ajouter (VCP de 10,73 M€), ou ajouter l'apport de 2,50 M€ à la VCP (15,83 M€) et confondre ainsi valeur avant et après l'opération.
- `JUR-E02` — coût du capital d'une société non cotée mal construit à partir de l'échantillon.
- `JUR-T07` — flux actualisés présentés sans tableau.

---

### 3.4 Méthode du capital-risque et comparaison des méthodes (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Valeur de sortie fin 2031 = 15 × 2,60 = 39,00 M€ ; valeur post-money = 39,00 / 1,30^5 = 39,00 / 3,71293 = 10,50 M€ | 0,5 |
| 3.4-02 | Valeur pré-money = 10,50 − 2,50 = 8,00 M€ ; prix par action = 8,00 M€ / 500 000 = 16,00 € ; actions nouvelles = 2 500 000 / 16,00 = 156 250 ; part de la mutuelle = 156 250 / 656 250 = 23,81 % | 1 |
| 3.4-03 | Comparaison : 8,00 M€ contre 5,60 (ANCC), 9,47 (valeur patrimoniale) et 13,33 M€ (flux) ; explication des écarts (TRI de 30 % contre CMPC de 11,67 %, risque d'échec, illiquidité, horizon de l'investisseur, croissance ignorée par l'approche patrimoniale) | 1 |

**Conventions rappelées** (annexes 3.5 et 3.6) : sortie le 31/12/2031, cinq ans après l'apport ; aucune émission ni dividende d'ici là ; valeurs post-money et pré-money arrondies à deux décimales, la pré-money arrondie servant au prix par action.

**Valeur de sortie et valeur post-money (0,5 pt).**
- Valeur de sortie des capitaux propres à la fin de 2031 = 15 × 2,60 = **39,00 M€**.
- La mutuelle exige un TRI de 30 % par an : la valeur aujourd'hui de la société **après** l'apport est la valeur de sortie actualisée à ce taux, soit 39,00 / 1,30^5 = 39,00 / 3,71293 = **10,50 M€** (valeur post-money).

**Valeur pré-money, prix et part du capital (1 pt).**
- Valeur pré-money = valeur post-money − apport = 10,50 − 2,50 = **8,00 M€** : c'est la valeur des capitaux propres **avant** l'apport, comparable à la VCP de la question 3.3.
- Prix par action = 8 000 000 / 500 000 = **16,00 €** ; actions nouvelles = 2 500 000 / 16,00 = **156 250** ; total après l'opération : 656 250 actions.
- Part de la mutuelle = 156 250 / 656 250 = **23,81 %** (= 2,50 / 10,50) : une participation minoritaire. Les fondateurs passeraient de 70 % à 53,33 % (350 000 / 656 250) et FERNIQUE Amorçage de 30 % à 22,86 %.
- Vérification : à la sortie, la mutuelle détiendrait 23,81 % de 39,00 M€, soit 9,29 M€, environ 3,7 fois sa mise (1,30^5 = 3,71) : le TRI de 30 % est obtenu si le plan se réalise.

**Comparaison avec les autres méthodes (1 pt).**

| Méthode | Valeur des capitaux propres avant l'apport (M€) | Par action (€) |
|---|---:|---:|
| ANCC | 5,60 | 11,20 |
| Méthode du capital-risque (pré-money) | 8,00 | 16,00 |
| Valeur patrimoniale (ANCC + goodwill) | 9,47 | 18,94 |
| Flux de trésorerie actualisés (VCP) | 13,33 | 26,66 |

- La valeur pré-money dépasse l'ANCC de 42,86 % (8,00 / 5,60 = 1,43) : l'investisseur paie une partie de la croissance, au-delà du patrimoine.
- Elle est **inférieure de 5,33 M€ à la valeur par les flux**, alors que les deux méthodes reposent sur le même plan. L'écart vient du taux : la mutuelle exige 30 % par an, contre un CMPC de 11,67 %. Ce TRI élevé rémunère ce que le CMPC ne prend pas en compte : le **risque d'échec** (le plan est un scénario de réussite ; dans un portefeuille de participations de ce type, une partie des lignes est perdue), l'**illiquidité** d'une participation minoritaire non cotée, et le temps que l'investisseur consacre à accompagner la société. Elle retient aussi un horizon court (cinq ans) et une valeur de sortie par un multiple, au lieu d'une croissance à l'infini.
- Entrer à la VCP par les flux (13,33 M€) donnerait à la mutuelle 15,79 % du capital pour 2,50 M€ et un TRI de 19,76 % seulement si le plan se réalise, loin de l'exigence de son conseil.
- Elle est **inférieure de 1,47 M€ à la valeur patrimoniale** : le goodwill est actualisé à 12 %, un taux bien plus faible que 30 %.
- Chaque méthode répond à une question différente : l'ANCC mesure ce que vaut le patrimoine ; la méthode des flux, ce que vaut le plan s'il réussit ; la méthode du capital-risque, le prix qu'un investisseur minoritaire peut payer pour obtenir la rentabilité qu'il exige.

**Réponses tolérées** : valeur post-money non arrondie (10,5038 M€), avec une pré-money de 8,0038 M€, un prix de 16,01 € et 156 152 actions nouvelles (23,80 % du capital), notée en cohérence ; part du capital calculée par 2,50 / 10,50 (23,81 %) sans le nombre d'actions ; comparaison présentée en valeurs par action.

**Erreurs fréquentes**
- Confondre post-money et pré-money : prix calculé sur 10,50 M€ (21,00 €), ou part de la mutuelle calculée sur la pré-money (2,50 / 8,00 = 31,25 %).
- Actualiser la valeur de sortie au CMPC (22,46 M€, pré-money de 19,96 M€) : le TRI exigé est le taux de la méthode.
- Appliquer un taux simple (39,00 / (1 + 5 × 30 %) = 15,60 M€) au lieu d'un taux composé.
- Comparer la valeur post-money (10,50 M€) à la VCP de la question 3.3, qui est une valeur avant l'apport.
- `JUR-E03` — juxtaposer les valeurs sans expliquer leurs écarts.

---

### 3.5 Fourchette, prix d'entrée et négociation (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Note à la directrice générale : fourchette de valeur **des capitaux propres** avant l'apport argumentée (la borne tirée des flux est la VCP de 13,33 M€, et non la VGE de 12,03 M€ ; par exemple de 5,60 M€, ANCC, à 8,00 M€, capital-risque, les flux donnant un plafond de 13,33 M€) ; prix d'entrée par action et part du capital qui en résulte (par exemple 12,50 €, pré-money de 6,25 M€, 200 000 actions nouvelles, 28,57 % du capital, fondateurs à 50,00 %) | 1 |
| 3.5-02 | Cycle de vie et synergies : valeur pré-money sans les agences de VERCÈNE (sortie 15 × 1,70 = 25,50 M€, post-money 6,87 M€, pré-money 4,37 M€) ; la mutuelle ne doit pas payer seule la valeur qu'elle apporte (3,63 M€) ; risques et conditions de l'entrée (information, gouvernance, contrôle des fondateurs, financement par étapes) | 1 |

**Synergies de distribution** (annexe 3.5). Sans les agences de VERCÈNE, le résultat net de 2031 serait de 1,70 M€ : valeur de sortie 15 × 1,70 = **25,50 M€** ; post-money 25,50 / 3,71293 = 6,87 M€ ; pré-money 6,87 − 2,50 = **4,37 M€** (8,74 € par action ; 36,39 % du capital pour 2,50 M€). La distribution dans les agences apporte donc **3,63 M€** à la valeur pré-money (8,00 − 4,37), près de la moitié.

**Exemple de note** (exemple développé ; une note de dix à quinze lignes reprenant ces éléments, avec le chiffrage de la valeur sans les agences, obtient la totalité des points)

> **À** : Mme Claire ESTAGNOL, directrice générale — **De** : cabinet — **Objet** : entrée au capital d'ALTIMOISSON SAS
>
> **1. Fourchette de valeur.** Avant votre apport, les capitaux propres d'ALTIMOISSON valent de 5,60 M€ (ANCC, plancher qui ne paie aucune croissance) à 8,00 M€ (méthode du capital-risque, au TRI de 30 % exigé par le conseil). La valeur par les flux (13,33 M€) et la valeur patrimoniale avec goodwill (9,47 M€) supposent la réussite du plan et un taux bien inférieur à votre exigence : ce sont des plafonds, que les fondateurs mettront en avant. Hormis l'ANCC, ces valeurs reposent sur le plan des dirigeants, qui suppose la vente de l'offre dans vos agences à partir de 2028.
>
> **2. Prix d'entrée proposé.** Je vous propose d'ouvrir la négociation à **12,50 € par action**, soit une valeur pré-money de 6,25 M€ : 200 000 actions nouvelles pour 2,50 M€, **28,57 %** du capital. Ce prix partage à peu près à parts égales la valeur apportée par vos agences ((4,37 + 8,00) / 2 = 6,185 M€). Il reste supérieur à l'ANCC et laisse aux fondateurs **50,00 %** du capital (350 000 / 700 000), le seuil qu'ils souhaitent conserver. Si le plan se réalise, la participation vaudrait 39,00 × 28,57 % = 11,14 M€ en 2031, soit un TRI de 34,83 %, qui offre une marge de sécurité face au risque d'échec. Le prix maximal acceptable est de 16,00 € (8,00 M€, 23,81 % du capital), au-delà duquel le TRI tombe sous 30 %.
>
> **3. Ce qu'impliquent le cycle de vie et les synergies.**
> - La société est en croissance : son résultat vient d'atteindre l'équilibre, ses flux restent négatifs jusqu'en 2028 et plus de 90 % de sa valeur par les flux viennent d'après 2031. Le prix doit donc rémunérer un risque élevé. Plutôt que de payer d'avance une croissance incertaine, un apport **en deux étapes** est préférable : une partie en 2027, le reste quand la distribution dans les agences aura donné ses premiers résultats.
> - La distribution par vos 64 agences apporte près de la moitié de la valeur pré-money (3,63 M€ sur 8,00). C'est la mutuelle qui apporte cette valeur : elle ne doit pas la payer une seconde fois dans le prix. C'est votre principal argument face à des fondateurs qui partiront de la valeur par les flux.
> - Les fondateurs connaissent mieux que vous la société et leur plan (asymétrie d'information, Akerlof, 1970). En tant qu'actionnaire minoritaire, vous devrez suivre la gestion (Jensen et Meckling, 1976) : un siège au conseil, une information régulière sur les indicateurs du plan (clients, sinistres gérés, part des ventes en agence) et l'accord de la mutuelle pour les décisions importantes. La dépendance envers trois assureurs et quelques personnes clés justifie aussi d'en faire des conditions de l'opération.
> - Enfin, la valeur de la participation n'est pas seulement financière : la plateforme peut améliorer le service rendu aux sociétaires agricoles et la gestion des sinistres climatiques de la mutuelle. Ce gain ne figure pas dans le TRI ; il peut justifier, à la marge, d'accepter un prix plus proche de 16,00 €.

**Réponses tolérées** : toute fourchette et tout prix cohérents avec les calculs du candidat et justifiés (par exemple une entrée à 16,00 €, pré-money de 8,00 M€, si le candidat considère que le TRI de 30 % rémunère déjà le risque, ou une fourchette de 8,00 à 13,33 M€ si les synergies sont laissées aux fondateurs pour préserver la relation) ; prix d'entrée exprimé par la seule valeur pré-money et la part du capital ; partage des synergies dans une autre proportion, s'il est expliqué.

**Erreurs fréquentes**
- Proposer comme prix d'entrée la valeur par les flux (13,33 M€) sans voir que le TRI obtenu (19,76 %) est inférieur à l'exigence du conseil.
- Proposer une fourchette qui mêle la valeur post-money et des valeurs avant l'apport.
- Retenir la VGE (12,03 M€) comme borne d'une fourchette de valeur des capitaux propres.
- Ignorer que les valeurs fondées sur le plan (goodwill, flux, capital-risque) incluent les synergies apportées par la mutuelle.
- Développer le régime juridique de l'augmentation de capital réservée ou de l'intermédiation en assurance : hors du champ de l'épreuve.
- `JUR-T01` — note sans posture de conseil (prix, part du capital, conditions) ; `JUR-T02` — recommandation sans lien avec les chiffres (4,37 ; 8,00 ; 13,33 M€).

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 64 ; programme l. 509-519 | flux de trésorerie disponibles, CMPC, MEDAF avec prime de taille, valeur terminale, passage de la VGE à la VCP | [V] | F03 § 2 ; F02 § 2, 3 et 5 |
| Guide pédagogique DSCG, juillet 2026, p. 65-66 ; programme l. 531-532 | ANC et ANCC, corrections indiquées par l'énoncé, rente du goodwill à partir des CPNE et des bénéfices associés fournis, limites | [V] | F03 § 4 et 5 |
| Guide pédagogique DSCG, juillet 2026, p. 67 ; programme l. 535-536 | cycle de vie et choix de la méthode ; méthode du capital-risque (valeur de sortie, TRI exigé, post-money, pré-money, part de l'investisseur) | [V] | F03 § 7 et 8 |
| Sujet 2025, annexe 1 (désendettement et réendettement du bêta d'un échantillon) | structure du calcul de la question 3.3 | [S] | F02 § 3 |
| Sharpe (1964) | MEDAF | [V contexte] | F10 § 2 |
| Gordon et Shapiro (1956) | valeur terminale à croissance constante | [V programme 3.1] | F10 § 2 |
| Akerlof (1970) | asymétrie d'information entre fondateurs et investisseur | [V programme 5.1] | F10 § 1 |
| Jensen et Meckling (1976) | théorie de l'agence (suivi de la gestion par l'actionnaire minoritaire) | [V programme 2.1] | F10 § 3 |
| Taux sans risque 4,0 %, prime de risque du marché 5,0 %, prime de taille et d'illiquidité 3,0 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 |
| Échantillon de sociétés cotées, corrections patrimoniales, CPNE, prévisions, multiple de sortie, TRI exigé | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 3.2 à 3.5 |
