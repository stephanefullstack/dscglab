# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 42 — Dossier 3 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F02 coût du capital, F06 marchés, fintech et crypto-actifs, F08 gouvernance et ESG, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026) ; fiche commune CSRD, ESRS et double matérialité (extraite le 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (intensités carbone, note extra-financière et scores des piliers, bêta réendetté, MEDAF et CMPC, VAN et TRI des deux propulsions, flux différentiels, VAN au voisinage du TRI, VAN probabilisée, espérance et écart-type, coûts actuariels des deux obligations, barème, liste noire, hors-programme ; émissions par passager, coût des quotas, prix du quota d'indifférence, interpolations et écarts entre les offres vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple des VAN calculées avec un CMPC erroné à la question 3.3, ou une note fondée sur des intensités erronées).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Enjeux extra-financiers, intensités carbone, communication et double matérialité du prix du carbone | `2.1.a` Identifier les éléments extra-financiers pour le diagnostic, dans la lignée du modèle d'affaires de l'entreprise ; `2.1.b` Interpréter le reporting RSE et de durabilité ; `2.1.d` Maîtriser le principe de double matérialité | 3 |
| 3.2 Note extra-financière de HALVARÈNE Gestion, portée et limites | `2.1.c` Utiliser les outils de notation financière et extra-financière | 1,5 |
| 3.3 Bêta, rentabilité exigée des fonds propres et CMPC du projet | `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 2 |
| 3.4 VAN, TRI, VAN probabilisée et choix de la propulsion | `7.1.a` Évaluer et classer des projets en milieu certain ; `7.1.b` Évaluer et classer des projets en milieu incertain | 5 |
| 3.5 Coût actuariel des deux obligations vertes, conditions de l'appellation | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `7.2.c` Analyser les nouveaux outils de financement | 1,5 |
| 3.6 Émission enregistrée sur une blockchain, nouveaux acteurs et recommandation | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs ; `7.2.c` | 3 |
| **Total** | | **16** |

Part du calcul : environ 7,5 points (3.1-02, la moitié de 3.1-04, 3.2-01, 3.3-01, 3.3-02, 3.4-01 à 3.4-04, 3.5-01 et le tiers de 3.6-02). Part de l'analyse : environ 8,5 points. Le dossier est le dernier de l'épreuve : les questions 3.4 et 3.6, qui demandent une recommandation, ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 Enjeux extra-financiers, intensités carbone, communication et double matérialité du prix du carbone (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Enjeux reliés au modèle d'affaires d'un armateur de ferries : E (émissions et prix du carbone, pollution de l'air dans les ports, biodiversité marine) ; S (sécurité des passagers et des navigants, conditions de travail et recrutement des navigants, desserte des territoires) ; G (actionnaire majoritaire et collectivité concédante, conseil de surveillance, rémunération du directoire sans critère climatique) ; liens avec la rentabilité, les risques et l'accès au financement | 0,75 |
| 3.1-02 | Intensités (tableau) : passagers **150,00 ; 152,00 ; 150,00** g par passager-km ; fret **50,00 ; 51,00 ; 52,00** g par tonne-km | 0,75 |
| 3.1-03 | Commentaire : intensité des passagers stable (0,00 %), intensité du fret en hausse (+ 4,00 %), émissions totales en hausse (+ 6,23 %) ; affirmation trop flatteuse : la baisse de 10 % par passager (63,00 → 56,70 kg) vient de la baisse de 10 % de la distance moyenne, pas d'un progrès de la flotte ; « trajectoire d'une flotte décarbonée » non étayée (aucun navire remplacé, flotte de 21 ans) ; risque d'écoblanchiment | 0,75 |
| 3.1-04 | Double matérialité du prix du carbone : impact (380 950 t de CO2 en 2026) et effet financier (quotas **17,10 M€**, soit **20,85 %** de l'EBITDA ; surcharge de 6,84 M€, 40 % du coût ; coût net **10,26 M€**, **12,51 %** de l'EBITDA) ; le classement « faible » de la matérialité financière n'est pas défendable : l'enjeu est élevé sur les deux plans | 0,75 |

**Les enjeux extra-financiers d'un armateur de ferries (0,75 pt).** L'information extra-financière complète le diagnostic financier : elle éclaire les risques et les opportunités qui pèseront sur les flux futurs et sur l'accès au financement. Les enjeux se lisent à partir du modèle d'affaires de KERNAVEL : des navires lourds en capitaux, à longue durée de vie, qui brûlent du carburant pour transporter des passagers (62 % du chiffre d'affaires) et du fret.
- **Environnement** : le **climat** est l'enjeu central (380 950 t de CO2 en 2026, coût des quotas, exigences des chargeurs et des financeurs, risque d'actifs dépréciés pour des navires de vingt ans) ; la **pollution de l'air** dans les ports (soufre, oxydes d'azote, particules) touche les riverains de Kervalan et des ports d'escale ; la **biodiversité marine** (bruit, collisions avec les cétacés).
- **Social** : la **sécurité** des passagers et des navigants (le taux de fréquence baisse de 24,5 à 20,5, mais reste élevé), enjeu humain, de réputation et d'assurance ; les **conditions de travail** des 1 450 navigants (rotations longues, officiers difficiles à recruter), qui conditionnent la capacité à armer les navires ; la desserte des territoires et l'emploi local, attendus par le syndicat mixte du port.
- **Gouvernance** : un fonds majoritaire (65 %) et une collectivité concédante (30 %), aux horizons différents ; un conseil de surveillance où siège un seul membre indépendant ; une rémunération variable du directoire fondée sur l'EBITDA et le flux de trésorerie, sans critère climatique, alors que la décarbonation conditionne la valeur à long terme. Dans la lecture de Jensen et Meckling (1976), la rémunération est un mécanisme d'alignement : elle oriente ici les dirigeants vers la performance de court terme. La lecture partenariale de Freeman (1984) rappelle que chargeurs, passagers, salariés et collectivités sont aussi des parties prenantes du choix du navire.

**Intensités carbone (0,75 pt).** Convention de l'annexe 3.6 : intensité = émissions (t) / activité (millions de passagers-km ou de tonnes-km), soit des grammes par passager-km ou par tonne-km ; deux décimales.

| | 2024 | 2025 | 2026 | Variation 2024-2026 |
|---|---:|---:|---:|---:|
| Passagers : 138 600 / 924 ; 142 880 / 940 ; 141 750 / 945 (g par passager-km) | **150,00** | **152,00** | **150,00** | 0,00 % |
| Fret : 220 000 / 4 400 ; 229 500 / 4 500 ; 239 200 / 4 600 (g par tonne-km) | **50,00** | **51,00** | **52,00** | + 4,00 % |
| Émissions par passager transporté (kg) : 138 600 / 2,20 ; … | 63,00 | 60,80 | 56,70 | − 10,00 % |
| Émissions totales (t) | 358 600 | 372 380 | 380 950 | + 6,23 % |

**Commentaire et affirmation trop flatteuse (0,75 pt).**
- L'intensité carbone des **passagers** ne baisse pas : 150 g par passager-km en 2024 comme en 2026, après une hausse en 2025. Celle du **fret** augmente de 4,00 %. Les émissions totales progressent de 6,23 %, plus vite que l'activité de fret (+ 4,55 % de tonnes-km) et autant que la consommation de carburant (+ 6,28 %).
- L'affirmation « nos émissions par passager ont baissé de 10 % » est **exacte mais trompeuse** : la baisse (63,00 kg à 56,70 kg) s'explique entièrement par la **baisse de 10 % de la distance moyenne** (420 km à 378 km), parce que la croissance du trafic vient de la ligne la plus courte. Rapportées au passager-km, seule mesure de l'efficacité de la flotte, les émissions sont stables. L'indicateur choisi dans la communication mesure le mix des lignes, pas la performance environnementale.
- La « trajectoire d'une flotte décarbonée » n'est étayée par aucun indicateur : aucun navire n'a été remplacé depuis 2023, les navires en propriété ont 21 ans en moyenne, et la part des escales branchées à quai ne dépasse pas 9 %.
- Le choix d'un indicateur flatteur expose le groupe à un reproche d'**écoblanchiment**, au moment même où il veut convaincre des chargeurs et des investisseurs de financer un navire bas carbone. L'information extra-financière doit être cohérente avec les indicateurs publiés (2.1.b).

**Double matérialité du prix du carbone (0,75 pt).** Selon le principe de double matérialité (fiche commune § 1), un enjeu est matériel s'il l'est par ses **impacts** (effets de l'entreprise sur les personnes et l'environnement) ou par ses **effets financiers** (sur la performance, les flux de trésorerie, l'accès au financement ou le coût du capital), ou par les deux.
- **Matérialité d'impact** : les navires de KERNAVEL ont émis 380 950 t de CO2 en 2026, en hausse ; le groupe contribue au changement climatique. Le classement « élevée » est justifié.
- **Matérialité financière** : le prix du carbone touche directement la marge. Coût des quotas 2026 = 228 000 × 75 € = **17,10 M€**, soit 17,10 / 82 = **20,85 %** de l'EBITDA. La surcharge carbone n'en couvre que 6,84 / 17,10 = **40 %** : le coût net est de **10,26 M€**, soit **12,51 %** de l'EBITDA et 2,18 points de marge d'EBITDA (17,45 % en 2026). Une hausse de 10 € du quota coûterait 2,28 M€ de plus par an (2,78 % de l'EBITDA). S'y ajoutent les effets sur l'accès au financement : les chargeurs, les banques et les investisseurs (HALVARÈNE Gestion) demandent des preuves de décarbonation.
- Le classement « faible » retenu pour la matérialité financière n'est donc **pas défendable** : la surcharge ne couvre pas le coût, les passagers n'en paient aucune, et le prix du quota est appelé à augmenter (annexe 3.3). L'enjeu climatique est matériel sur les deux plans, et c'est précisément ce qui justifie d'étudier la propulsion du navire de remplacement.

**Réponses tolérées** : intensités exprimées en kg par millier de passagers-km ; variation des émissions par passager calculée sur 2025-2026 si le candidat compare aussi à la distance ; enjeux présentés sans le classement E, S, G s'ils sont reliés au modèle d'affaires ; coût net rapporté au chiffre d'affaires (2,18 %) plutôt qu'à l'EBITDA.

**Erreurs fréquentes**
- Recalculer les émissions à partir de la consommation de carburant : elles sont fournies.
- Valider l'affirmation au motif que le chiffre de 10 % est exact, sans voir l'effet de la distance moyenne.
- Rapporter les émissions du fret aux passagers-km, ou additionner passagers-km et tonnes-km.
- `JUR-D01` — confondre la démarche RSE de l'entreprise et les critères ESG des investisseurs ; `JUR-T05` — traiter l'extra-financier sans lien avec la marge ; `JUR-T13` — enjeux génériques, sans les données du cas.

---

### 3.2 Note extra-financière de HALVARÈNE Gestion, portée et limites (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Points des critères (2 ; 2 ; 2 ; 3 ; 4 ; 3 ; 1) ; scores des piliers : E **2,00**, S **3,50**, G **2,00** ; score global **2,45**, note **C** | 0,75 |
| 3.2-02 | Portée : note inférieure au seuil B des fonds de HALVARÈNE Gestion, effet sur l'accès aux investisseurs verts et sur le coût ; faiblesses à corriger (intensités, branchement à quai, rémunération) ; limites : grille propre à un investisseur, pondérations et appréciations subjectives, indicateurs d'une année passée, intensités et non émissions totales, divergence entre agences, règlement européen de 2024 sur la notation ESG | 0,75 |

**Calcul de la note (0,75 pt).** Règles de l'annexe 3.2 : borne incluse ; score global = Σ poids × points ; échelle A ≥ 4,00, B ≥ 3,00, C ≥ 2,00, D.

| Pilier | Critère | Valeur 2026 | Points | Poids | Poids × points |
|---|---|---:|---:|---:|---:|
| E | Intensité carbone des passagers | 150,00 g (≤ 170) | 2 | 20 % | 0,40 |
| E | Intensité carbone du fret | 52,00 g (≤ 60) | 2 | 20 % | 0,40 |
| E | Escales branchées à quai | 9 % (≥ 5 %) | 2 | 10 % | 0,20 |
| S | Taux de fréquence des navigants | 20,5 (≤ 25) | 3 | 15 % | 0,45 |
| S | Conditions de travail à bord | analyste | 4 | 15 % | 0,60 |
| G | Équilibre du conseil de surveillance | analyste | 3 | 10 % | 0,30 |
| G | Rémunération variable liée au climat | aucun critère | 1 | 10 % | 0,10 |
| | **Score global** | | | 100 % | **2,45** |

- Scores des piliers : E = (0,40 + 0,40 + 0,20) / 0,50 = **2,00** ; S = (0,45 + 0,60) / 0,30 = **3,50** ; G = (0,30 + 0,10) / 0,20 = **2,00**.
- Score global 2,45 : note **C** (de 2,00 à moins de 3,00).

**Portée et limites (0,75 pt).**
- **Portée pour le groupe** : avec la note C, KERNAVEL n'atteint pas le seuil B que retiennent les fonds de HALVARÈNE Gestion ; une obligation verte ne leur serait proposable qu'à la condition dérogatoire de l'annexe 3.5 (actif qui réduit d'au moins 80 % les émissions). Une note faible restreint le cercle des investisseurs et peut renchérir le financement. La grille montre aussi où agir : les deux intensités carbone et le branchement à quai (pilier E à 2,00) et la rémunération du directoire (critère à 1 point), qu'un critère climatique d'au moins 20 % de la part variable porterait à 5 points (+ 0,40 point de score global, non exigé). Le social est le point fort (3,50).
- **Limites** : la note dépend d'une grille propre à un investisseur (choix des critères, pondérations, paliers) ; deux critères sur sept reposent sur l'appréciation d'un analyste ; elle mesure l'année 2026 et ne voit pas le navire de remplacement, qui entrera en service en 2030 ; les intensités ne disent rien de la hausse des émissions totales ; les notations ESG des différents fournisseurs divergent souvent. Parce qu'elle publie ses notes, HALVARÈNE Gestion entre dans le champ du règlement européen sur la notation ESG : depuis le 2 juillet 2026, les fournisseurs de notations ESG exerçant dans l'Union doivent être agréés par l'AEMF, qui les surveille (les fournisseurs déjà actifs relèvent d'un régime transitoire le temps de leur demande d'agrément) : publication des méthodes, notes E, S et G distinctes ou information sur la pondération (ici, les trois scores de pilier sont publiés), information de l'entité notée avant publication pour corriger une erreur de fait (F08 § 3.2). La note éclaire la décision ; elle ne remplace pas l'analyse.

**Réponses tolérées** : score global calculé pilier par pilier (0,50 × 2,00 + 0,30 × 3,50 + 0,20 × 2,00 = 2,45) ; scores des piliers non calculés si le score global et la note sont justes (0,5 sur 0,75 à l'item 3.2-01) ; limites présentées sans référence au règlement européen.

**Erreurs fréquentes**
- Placer l'intensité carbone des passagers (150) dans le palier « ≤ 140 », ou noter 9 % d'escales branchées dans le palier inférieur.
- Faire la moyenne simple des points (2,43) au lieu de la moyenne pondérée.
- `JUR-T10` — commenter la note sans la calculer, ou l'inverse ; `JUR-T13` — limites générales des notations, sans les critères de la grille.

---

### 3.3 Bêta, rentabilité exigée des fonds propres et CMPC du projet (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Bêta d'actif moyen (0,64 + 0,70 + 0,76) / 3 = **0,70** ; bêta des capitaux propres = 0,70 × (1 + 0,75 × 40 / 60) = **1,05** | 0,5 |
| 3.3-02 | Rentabilité exigée des fonds propres = 4,0 % + 1,05 × 5,0 % = **9,25 %** ; coût net de la dette 5,00 % × 0,75 = 3,75 % ; CMPC = 60 % × 9,25 % + 40 % × 3,75 % = **7,05 %** | 0,75 |
| 3.3-03 | Lien risque / rentabilité : seul le risque systématique (bêta) est rémunéré ; risque d'exploitation des armateurs et risque financier de la dette ; taux propre au projet : le CMPC du groupe mêle le terminal et les lignes ; l'incertitude sur le prix du quota est traitée par les scénarios, pas par le taux ; les flux d'exploitation s'actualisent au CMPC | 0,75 |

**Bêta et rentabilité exigée (1,25 pt).** Formule de l'annexe 3.4 (Hamada, avec impôt, dette sans risque) ; structure cible en valeur : dette / capitaux propres = 40 / 60.
- Bêta de l'actif économique retenu : (0,64 + 0,70 + 0,76) / 3 = **0,70**.
- Bêta des capitaux propres du projet : 0,70 × [1 + (1 − 0,25) × 40 / 60] = 0,70 × 1,50 = **1,05**.
- MEDAF (Sharpe, 1964) : rentabilité exigée des fonds propres = 4,0 % + 1,05 × 5,0 % = **9,25 %**.
- Coût de la dette après impôt : 5,00 % × (1 − 0,25) = 3,75 %.
- **CMPC du projet** = 0,60 × 9,25 % + 0,40 × 3,75 % = 5,55 % + 1,50 % = **7,05 %**.

**Lien entre le risque du projet et la rentabilité exigée (0,75 pt).**
- Un investisseur n'accepte un risque plus élevé que contre une rentabilité espérée plus élevée. Dans le MEDAF, seul le **risque systématique**, mesuré par le bêta, est rémunéré : le risque propre à une entreprise peut être éliminé par la diversification. Le bêta d'actif de 0,70 mesure la sensibilité de l'activité d'armateur de ferries à la conjoncture (tourisme, échanges de marchandises), amplifiée par des coûts fixes élevés.
- Sans dette, les actionnaires exigeraient 4,0 % + 0,70 × 5,0 % = 7,50 % (non exigé). La dette (40 %) ajoute un **risque financier** : le bêta des capitaux propres passe à 1,05 et la rentabilité exigée à 9,25 %. Le CMPC (7,05 %) est inférieur à 7,50 % parce que les intérêts sont déductibles.
- **Pourquoi un taux propre au navire** : le taux d'actualisation doit refléter le risque du projet, pas celui de l'entreprise qui l'entreprend. Le CMPC du groupe mêle les lignes maritimes et le terminal, exploité en concession jusqu'en 2049 avec des recettes plus régulières : un taux unique sous-estimerait le risque des navires et ferait accepter des projets maritimes trop risqués (et rejeter à tort des projets peu risqués). D'où le recours au bêta d'armateurs comparables, réendetté à la structure financière cible du navire.
- Les flux du navire sont des flux d'exploitation, avant rémunération des prêteurs et des actionnaires : ils s'actualisent au **CMPC**, pas à la rentabilité exigée des fonds propres (9,25 %). L'incertitude sur le prix du quota, propre au projet, est traitée par les **scénarios** de la question 3.4 et non par une prime ajoutée au taux, ce qui la compterait deux fois.

**Réponses tolérées** : bêta réendetté écrit 0,70 × (1 + 0,75 × 0,6667) ; CMPC de 7,05 % présenté directement comme 9,25 % × 0,6 + 5 % × 0,75 × 0,4.

**Erreurs fréquentes**
- Réendetter avec dette / valeur totale (0,40) au lieu de dette / capitaux propres (0,6667) : bêta de 0,91 et rentabilité exigée de 8,55 %.
- Pondérer le CMPC par 40 / 60 au lieu de 40 % et 60 %, ou oublier l'impôt sur le coût de la dette (CMPC de 7,55 %).
- Actualiser les flux du navire à 9,25 %.
- `JUR-E02` — coût du capital d'un projet sans cotation par comparables : bêtas d'actif, réendettement, MEDAF, CMPC, avec la formule donnée ; `JUR-T04` — acquis du DCG.

---

### 3.4 VAN, TRI, VAN probabilisée et choix de la propulsion (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Flux nets annuels (EBITDA × 0,75 + 0,25 × amortissement) : A **17,85 ; 16,35 ; 14,10** M€ ; B **21,02 ; 20,90 ; 20,72** M€ (scénarios bas, central, haut) ; valeur résiduelle ajoutée en année 20 | 1 |
| 3.4-02 | VAN au CMPC de 7,05 %, scénario central : A **32,23 M€** ; B **35,42 M€** | 0,75 |
| 3.4-03 | TRI, scénario central : A **9,73 %** ; B **9,30 %** (9,75 % et 9,31 % par interpolation entre 9 % et 10 %) | 0,75 |
| 3.4-04 | VAN par scénario : A 48,06 ; 32,23 ; 8,48 ; B 36,69 ; 35,42 ; 33,52 ; espérance A **30,25**, B **35,26** ; écart-type A **14,13**, B **1,13** | 1 |
| 3.4-05 | Classement et conflit : la VAN classe B, le TRI classe A ; causes (tailles différentes, mesure absolue ou relative, hypothèse de réinvestissement) ; résolution par les flux différentiels B − A : 46,00 M€ de plus, VAN **3,19 M€** > 0 (TRI de 7,90 % > 7,05 %) | 0,75 |
| 3.4-06 | Recommandation : B, plus forte espérance de VAN et risque bien plus faible (B domine A) ; B ne perd que dans le scénario bas ; risques non chiffrés (prix du méthanol après dix ans, prime des chargeurs après cinq ans, technologie nouvelle) | 0,75 |

**Conventions rappelées** (annexes 3.3 et 3.6) : date 0 = 1er janvier 2030 ; investissement payé à la date 0 ; vingt flux de fin d'année ; amortissement linéaire sur 20 ans (A : 7,20 M€, B : 9,50 M€) ; IS de 25 % ; valeur résiduelle nette d'impôt ajoutée au flux de l'année 20 ; CMPC de 7,05 % ; coefficients non arrondis, flux et VAN au centième.

**Flux nets de trésorerie (1 pt).** EBITDA du navire = recettes − charges − énergie − quotas ; flux = EBITDA − IS, avec IS = 25 % × (EBITDA − amortissement), soit EBITDA × 0,75 + 0,25 × amortissement.

| M€ par an | A bas (60 €) | A central (100 €) | A haut (160 €) | B bas (60 €) | B central (100 €) | B haut (160 €) |
|---|---:|---:|---:|---:|---:|---:|
| Recettes − charges − énergie | 24,40 | 24,40 | 24,40 | 25,10 | 25,10 | 25,10 |
| − Quotas (50 000 t ou 4 000 t × prix) | − 3,00 | − 5,00 | − 8,00 | − 0,24 | − 0,40 | − 0,64 |
| = EBITDA du navire | 21,40 | 19,40 | 16,40 | 24,86 | 24,70 | 24,46 |
| − IS : 25 % × (EBITDA − amortissement de 7,20 ou 9,50) | − 3,55 | − 3,05 | − 2,30 | − 3,84 | − 3,80 | − 3,74 |
| **= Flux net (années 1 à 20)** | **17,85** | **16,35** | **14,10** | **21,02** | **20,90** | **20,72** |
| Flux de l'année 20, valeur résiduelle comprise (14,4 ou 19,0) | 32,25 | 30,75 | 28,50 | 40,02 | 39,90 | 39,72 |

**VAN du scénario central (0,75 pt).** Les flux étant constants, VAN = − I + F × [1 − 1,0705^−20] / 0,0705 + VR × 1,0705^−20, avec un facteur d'annuité de 10,5530 et un coefficient de 0,2560 (valeurs non arrondies dans le calcul).
- A : − 144,00 + 16,35 × 10,5530 + 14,4 × 0,2560 = − 144,00 + 172,54 + 3,69 = **32,23 M€** ;
- B : − 190,00 + 20,90 × 10,5530 + 19,0 × 0,2560 = − 190,00 + 220,56 + 4,86 = **35,42 M€**.

Les deux propulsions créent de la valeur au CMPC du projet.

**TRI du scénario central (0,75 pt).**
- A : VAN à 9 % = 7,82 ; à 10 % = − 2,66 ; TRI = 9 % + 1 % × 7,82 / (7,82 + 2,66) = 9,75 % par interpolation (**9,73 %** pour la valeur exacte).
- B : VAN à 9 % = 4,18 ; à 10 % = − 9,24 ; TRI = 9 % + 1 % × 4,18 / (4,18 + 9,24) = 9,31 % par interpolation (**9,30 %**).

Les deux TRI dépassent le CMPC de 7,05 %.

**VAN probabilisée (1 pt).** VAN de chaque scénario, même méthode ; espérance = Σ probabilité × VAN ; variance = Σ probabilité × (VAN − espérance)².

| | Bas (p = 0,25) | Central (p = 0,50) | Haut (p = 0,25) | Espérance | Écart-type | Coefficient de variation |
|---|---:|---:|---:|---:|---:|---:|
| VAN de A (M€) | 48,06 | 32,23 | 8,48 | **30,25** | **14,13** | 0,47 |
| VAN de B (M€) | 36,69 | 35,42 | 33,52 | **35,26** | **1,13** | 0,03 |

- A : espérance = 0,25 × 48,06 + 0,50 × 32,23 + 0,25 × 8,48 = **30,25 M€** ; variance = 0,25 × 17,81² + 0,50 × 1,98² + 0,25 × (− 21,77)² = 199,74 ; écart-type **14,13 M€**.
- B : espérance = 0,25 × 36,69 + 0,50 × 35,42 + 0,25 × 33,52 = **35,26 M€** ; variance = 1,28 ; écart-type **1,13 M€**.
- La VAN de A dépend fortement du prix du quota (chaque euro de plus par tonne retire 0,05 × 0,75 × 10,5530 = 0,40 M€ de VAN) ; celle de B, qui émet 92 % de moins, y est presque insensible.

**Classement et conflit entre la VAN et le TRI (0,75 pt).**

| Critère (scénario central) | A : gazole marin | B : méthanol et batteries | Classement |
|---|---:|---:|---|
| VAN (M€) | 32,23 | 35,42 | B |
| TRI | 9,73 % | 9,30 % | A |
| Espérance de la VAN (M€) | 30,25 | 35,26 | B |
| Écart-type de la VAN (M€) | 14,13 | 1,13 | B (moins risqué) |

- **Le conflit** : la VAN, mesure **absolue** de la valeur créée, classe B en tête ; le TRI, mesure **relative** (rentabilité par euro investi), classe A. Les deux projets n'ont pas la même taille (190,00 contre 144,00 M€). Le TRI suppose en outre que les flux sont réinvestis au TRI du projet, la VAN qu'ils le sont au CMPC, hypothèse plus prudente et commune aux deux projets.
- **La résolution** : choisir B revient à investir **46,00 M€ de plus** pour obtenir des flux supplémentaires de 4,55 M€ par an (9,15 M€ en année 20, valeur résiduelle comprise). Ce supplément a une VAN de 35,42 − 32,23 = **3,19 M€** et un TRI de 7,90 %, supérieur au CMPC : il crée de la valeur. Les deux VAN sont égales pour un taux de 7,90 % (taux d'indifférence) ; au CMPC de 7,05 %, B l'emporte. Les projets étant exclusifs et le groupe pouvant financer l'une ou l'autre propulsion (annexe 3.3), il n'y a pas de rationnement du capital : on retient la plus forte VAN.

**Recommandation (0,75 pt).** Exemple de réponse : retenir la **propulsion B**.
- B a la plus forte **espérance de VAN** (35,26 contre 30,25 M€) et un risque beaucoup plus faible (écart-type de 1,13 contre 14,13 M€) : au sens de la relation rentabilité-risque, B domine A. Elle ne perd que dans le scénario bas (VAN de 36,69 contre 48,06 M€) ; à 160 €, l'écart atteint 25,04 M€ en sa faveur. Les VAN sont égales pour un prix moyen du quota de 91,23 € (non exigé) : B l'emporte dès que le prix dépasse ce niveau, soit avec une probabilité de 0,75 selon les scénarios.
- B réduit l'exposition du groupe au prix du carbone, priorité du directoire (protéger les marges), et rend le navire éligible à un financement vert (questions 3.5 et 3.6) ; elle répond aux attentes des chargeurs et améliorera les intensités carbone notées par HALVARÈNE Gestion.
- **Réserves**, qui ne sont pas dans les scénarios : le prix du méthanol n'est garanti que dix ans et un seul des deux producteurs européens est sous contrat ; la prime bas carbone (2,5 M€ par an, soit 2,5 × 0,75 × 10,5530 = 19,79 M€ de VAN, non exigé) n'est assurée que cinq ans ; la technologie est nouvelle pour les équipages (formation, entretien des batteries) ; le prix du contrat d'énergie, environ 48 % au-dessus de celui du gazole à énergie égale (14,0 M€ pour l'équivalent de 12 000 t, contre 12,6 M€ pour 16 000 t), est favorable au regard des prix actuels du méthanol renouvelable. Le directoire devrait sécuriser l'approvisionnement et allonger les engagements des chargeurs avant de commander le navire.

**Réponses tolérées** : TRI de 9,75 % et 9,31 %, résultats de l'interpolation prévue par l'annexe 3.6 ; TRI par interpolation entre d'autres taux encadrants ; VAN différentielle calculée directement sur les flux B − A ; écart-type calculé sur les VAN arrondies (mêmes résultats) ; recommandation de A si le candidat la fonde sur une anticipation explicite d'un prix du quota inférieur à 91 € ou sur le risque technologique, en reconnaissant que B a la plus forte espérance de VAN (0,25 sur 0,75 à l'item 3.4-06).

**Erreurs fréquentes**
- Déduire l'amortissement des flux, ou oublier l'économie d'impôt qu'il procure (flux de A de 14,55 M€ au lieu de 16,35 M€ dans le scénario central).
- Oublier la valeur résiduelle, ou l'actualiser comme un flux annuel.
- Calculer la variance avec n − 1, ou sans les probabilités.
- Retenir A au motif que son TRI est le plus élevé, sans voir la différence de taille.
- `JUR-I05` — calculer la VAN et le TRI sans analyser leur divergence ; `JUR-T04` — actualisation ou interpolation non maîtrisées ; `JUR-T07` — flux présentés sans tableau.

---

### 3.5 Coût actuariel des deux obligations vertes, conditions de l'appellation (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Flux de l'émetteur : offre 1 + 75,088 puis − 3,774 par an et − 79,774 en année 7, coût **5,17 %** ; offre 2 + 75,62 puis − 3,69 et − 79,69, coût **4,94 %** ; l'offre 2 coûte 0,23 point de moins | 0,75 |
| 3.5-02 | Obligation verte : fonds affectés à des projets environnementaux, sélection des projets, gestion des fonds, rapport d'affectation et d'impact revu par un examinateur externe ; appellation européenne facultative (taxonomie comme grille de lecture, examinateur enregistré auprès de l'AEMF) ; conditions pour KERNAVEL : fonds affectés au navire B, qui réduit les émissions de 92 % (≥ 80 %), d'où l'accès aux fonds de HALVARÈNE Gestion malgré la note C ; avec la propulsion A, pas d'obligation verte | 0,75 |

**Coût actuariel (0,75 pt).** Annexe 3.6 : flux de l'émetteur, montant net reçu positif ; coupons et frais annuels en fin d'année ; remboursement in fine en année 7.

| M€ | Année 0 | Années 1 à 6 | Année 7 |
|---|---:|---:|---:|
| Offre 1 : 76 × (1 − 1,20 %) ; − (76 × 4,90 % + 0,05) ; − 76 | + 75,088 | − 3,774 | − 79,774 |
| Offre 2 : 76 × (1 − 0,50 %) ; − (76 × 4,75 % + 0,08) ; − 76 | + 75,620 | − 3,690 | − 79,690 |

- Offre 1 : valeur actuelle des flux à 5 % = − 0,7616 ; à 6 % = + 3,4758 ; par interpolation 5,18 % (**5,17 %** pour la valeur exacte).
- Offre 2 : à 4 % = − 4,2813 ; à 5 % = + 0,2565 ; par interpolation **4,94 %**.
- L'offre 2 est moins chère de **0,23 point** : coupon plus bas (4,75 % contre 4,90 %) et frais initiaux plus faibles (0,38 contre 0,912 M€), malgré 0,03 M€ par an de tenue du registre. Après impôt, le classement est le même : tous les frais et les coupons sont déductibles (non exigé). Les deux coûts sont proches du coût de la dette retenu dans le CMPC (5,00 %).

**Ce qui fait une obligation verte (0,75 pt).**
- Une obligation verte est une obligation classique dont les fonds sont **affectés** à des projets ayant un bénéfice environnemental. Les standards de marché (Green Bond Principles de l'ICMA) en retiennent quatre composantes : **utilisation des fonds**, **sélection** des projets, **gestion** des fonds jusqu'à leur affectation, **rapport** (reporting) d'affectation et d'impact, avec une revue externe (F08 § 5.1). Elle se distingue d'une obligation liée à la durabilité, dont les fonds sont libres et le coupon indexé sur des objectifs.
- L'**obligation verte européenne** est une appellation facultative mais protégée : fonds affectés à des activités conformes à la taxonomie (qui sert de grille de lecture de la « part verte »), fiche d'information et rapports d'affectation revus par un examinateur externe enregistré auprès de l'AEMF (règlement (UE) 2023/2631, F08 § 5.2).
- **Conditions pour KERNAVEL** : les 76 M€ financeraient le seul navire à propulsion au méthanol, qui réduit les émissions donnant lieu à restitution de 50 000 à 4 000 t par an, soit **− 92 %** par rapport au navire de référence ; le groupe publierait chaque année l'affectation des fonds et les émissions évitées, revues par un examinateur externe. Noté C par HALVARÈNE Gestion (question 3.2), le groupe reste admis dans ses fonds grâce à la règle dérogatoire (réduction d'au moins 80 %). Avec la propulsion A, l'émission ne pourrait pas être présentée comme verte : le choix de la question 3.4 conditionne aussi l'accès à ces investisseurs.

**Réponses tolérées** : coût de l'offre 1 de 5,18 % par interpolation ; coûts estimés par la formule approchée (coupon + frais annuels / nominal + frais initiaux / durée), si le classement est juste et la méthode signalée comme approchée (0,5 sur 0,75 à l'item 3.5-01) ; coûts après impôt calculés en plus.

**Erreurs fréquentes**
- Oublier les frais annuels (coûts de 5,11 % et 4,84 %) ou les frais initiaux.
- Confondre obligation verte (fonds affectés) et prêt ou obligation indexés sur la durabilité.
- `JUR-T04` — taux actuariel non maîtrisé ; `JUR-T12` — définition approximative du financement vert.

---

### 3.6 Émission enregistrée sur une blockchain, nouveaux acteurs et recommandation (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Principe : les obligations sont émises et inscrites sur un registre partagé et infalsifiable (blockchain) sous forme de jetons ; elles restent des obligations ; règlement et paiement des coupons automatisés par un programme ; cadre expérimental européen (régime pilote) | 0,75 |
| 3.6-02 | Apports, chiffrés : règlement le jour même au lieu de cinq jours ouvrés ; coût plus bas (0,532 M€ de frais initiaux et 0,084 M€ par an en moins ; 4,94 % contre 5,17 %) ; accès à de nouveaux investisseurs (souscription minimale de 100 000 €, gestionnaires d'actifs européens dont HALVARÈNE Gestion) ; préparation plus courte | 0,75 |
| 3.6-03 | Risques : placement non garanti (annulation sous 60 M€, aucune émission de plus de 50 M€ sur la plateforme) ; liquidité réelle faible ; risque opérationnel et cyber (programme, portefeuilles numériques, dépendance à la plateforme) ; cadre encore expérimental ; risque de réputation | 0,75 |
| 3.6-04 | Rôle des nouveaux acteurs (plateforme de négociation et de règlement, banque agent, teneurs de portefeuilles numériques, supervision de l'AMF) et recommandation argumentée | 0,75 |

**Principe (0,75 pt).** Une blockchain est un registre partagé entre plusieurs participants, dont les inscriptions, validées selon des règles communes, ne peuvent pas être modifiées après coup ; elle permet de se passer d'un teneur de registre central. La **tokenisation** consiste à émettre et à inscrire sur ce registre des titres financiers sous forme de **jetons** : ici, chaque jeton représente une obligation de KERNAVEL. Les droits des investisseurs ne changent pas : il s'agit toujours d'une obligation verte à 4,75 %, remboursable in fine dans sept ans ; seuls le registre, la livraison et le paiement changent. Le règlement-livraison est simultané (les jetons contre les euros, le jour même) et les coupons sont versés automatiquement par un programme inscrit sur la blockchain (« contrat intelligent »). TALMERAN Titres Numériques opère dans le cadre du **régime pilote européen**, cadre d'expérimentation des infrastructures de marché fondées sur ces registres (F06 § 6). L'approche reste celle des principes et des enjeux financiers, sans technique informatique.

**Apports (0,75 pt).**
- **Règlement plus rapide** : le jour même, contre cinq jours ouvrés ; les fonds sont disponibles plus tôt et le risque de défaut d'une contrepartie entre la signature et le paiement disparaît.
- **Coût** : moins d'intermédiaires (pas d'arrangeur, registre et paiements automatisés) ; frais initiaux de 0,38 M€ contre 0,912 M€ (**0,532 M€** de moins), coupon plus bas de 0,15 point ; au total **0,084 M€** par an de moins malgré la tenue du registre, et un coût actuariel de **4,94 %** contre **5,17 %**.
- **Nouveaux investisseurs** : la souscription minimale de 100 000 € et l'accès des gestionnaires d'actifs européens, des banques privées et des trésoreries d'entreprises élargissent la base d'investisseurs au-delà de quelques assureurs français ; HALVARÈNE Gestion n'est présente que dans l'offre 2. La possibilité de revendre les jetons sur le système de TALMERAN explique en partie le coupon plus bas.
- **Délai** de préparation plus court (6 semaines contre 10) et, non exigé, **traçabilité** : le registre pourrait porter l'affectation des fonds et les données du rapport vert, ce qui rend l'engagement environnemental plus vérifiable et réduit l'asymétrie d'information avec les investisseurs (Akerlof, 1970).

**Risques (0,75 pt).**
- **Risque de placement** : l'offre 2 n'est pas garantie ; l'émission est annulée si les souscriptions n'atteignent pas 60 M€, alors que TALMERAN n'a jamais placé plus de 50 M€. Or le financement du navire doit être certain. Les investisseurs de l'offre 1 sont déjà engagés sur la totalité.
- **Liquidité** : la négociation est possible mais les échanges sont encore peu nombreux ; un investisseur pourrait ne pas trouver d'acheteur, ce qui limitera la demande ou le prix lors d'une prochaine émission.
- **Risque opérationnel et cyber** : erreur dans le programme qui paie les coupons, perte ou vol des accès aux portefeuilles numériques, panne ou attaque de la plateforme ; **dépendance** à un acteur jeune, qui concentre des fonctions habituellement séparées ; si TALMERAN cessait son activité, il faudrait transférer le registre.
- **Cadre encore expérimental** : le régime pilote est un cadre d'expérimentation, limité, dont les règles peuvent évoluer pendant les sept ans de l'obligation. Une difficulté sur une première émission « verte et numérique » serait aussi un **risque de réputation** pour le groupe.

**Les nouveaux acteurs et la recommandation (0,75 pt).**
- **Rôle des nouveaux acteurs** : TALMERAN Titres Numériques, fintech autorisée par l'AMF, réunit l'émission, la tenue du registre, le règlement-livraison et la négociation, fonctions que se partagent d'ordinaire l'arrangeur, le dépositaire central, la banque teneur de comptes et le marché ; la **banque agent** fait le lien avec les paiements en euros ; des banques ou des prestataires agréés tiennent les **portefeuilles numériques** des investisseurs ; l'**AMF** autorise et surveille la plateforme. Ces acteurs désintermédient en partie le financement obligataire et le rendent accessible à des émetteurs de taille moyenne non cotés comme KERNAVEL. Les banques traditionnelles ne disparaissent pas : elles deviennent agents, conservateurs ou investisseurs.
- **Recommandation** (exemple de réponse) : retenir l'**offre 2**, moins chère de 0,23 point et seule à ouvrir l'accès à HALVARÈNE Gestion et à de nouveaux investisseurs, **à condition** de sécuriser le montant : obtenir de la banque VAUNOIRE ou d'une autre banque un engagement de prendre la part non souscrite, ou prévoir de lancer l'offre 1 si les souscriptions n'atteignent pas 76 M€. L'avantage de coût (0,084 M€ par an et 0,532 M€ de frais initiaux) est réel mais modeste à l'échelle d'un navire de 190 M€ : il ne justifie pas de prendre un risque sur le financement. Une émission verte, transparente et vérifiable, est aussi un signal de l'engagement climat du groupe, crédible parce qu'il est coûteux (Spence, 1973). À défaut d'une solution de repli, l'offre 1, plus chère mais certaine, est préférable.

**Réponses tolérées** : recommandation de l'offre 1 pour la certitude du placement et la simplicité, si elle est justifiée par les risques et chiffrée (écart de 0,23 point) ; recommandation de l'offre 2 sans solution de repli, si le risque de placement est reconnu (0,5 sur 0,75 à l'item 3.6-04) ; présentation de la blockchain comme « registre distribué » ou « technologie des registres partagés ».

**Erreurs fréquentes**
- Présenter les jetons comme des crypto-actifs spéculatifs : ce sont des obligations, avec les droits d'un créancier ; leur statut juridique n'est pas à analyser (UE 1).
- Développer la technique informatique (consensus, cryptographie, clés) au lieu des enjeux financiers (UE 5).
- Retenir l'offre 2 sur le seul coût, sans voir que le placement n'est pas garanti.
- `JUR-M02` — nouveaux acteurs du financement à comparer selon le profil de l'entreprise et des investisseurs ; `JUR-T01` — recommandation sans posture de conseil ; `JUR-T15` — dernière question bâclée faute de temps.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 59-61 ; programme l. 475-490 | information extra-financière du diagnostic, lecture des indicateurs ESG, cohérence entre engagements et indicateurs, score sur une grille fournie, double matérialité | [V] | F08 § 0, 2 et 3 |
| Fiche commune CSRD, ESRS et double matérialité, § 1 et 5 | matérialité d'impact et matérialité financière (accès au financement, coût du capital) ; état de durabilité publié volontairement | [V dans la fiche commune] | fiche commune |
| Règlement (UE) 2024/3005, art. 2, 15, 23 et 51 à 53 | notation ESG réglementée depuis le 2 juillet 2026 (agrément par l'AEMF, régime transitoire pour les fournisseurs déjà actifs), notes E, S, G distinctes, information de l'entité notée avant publication | [V] | F08 § 3.2 |
| Guide pédagogique DSCG, juillet 2026, p. 74-75 ; F02 § 2, 3 et 5 | lien entre risque et rentabilité exigée, MEDAF, réendettement du bêta (Hamada avec IS), CMPC | [V] | F02 |
| Guide pédagogique DSCG, juillet 2026, p. 80-81 ; programme l. 643-647 | VAN, TRI, projets mutuellement exclusifs, conflit de classement, espérance et écart-type de la VAN | [V] | F01 § 4 et 5 |
| Guide pédagogique DSCG, juillet 2026, p. 81-82 ; programme l. 653-666 | coût actuariel des financements, financements durables et verts | [V] | F01 § 3 ; F08 § 5 |
| Green Bond Principles (ICMA) | quatre composantes d'une obligation verte | [S] | F08 § 5.1 |
| Règlement (UE) 2023/2631, art. 1, 3, 4, 10, 11 et 22 | obligation verte européenne : appellation protégée, fonds conformes à la taxonomie, examinateur externe enregistré auprès de l'AEMF | [V] | F08 § 5.2 |
| Programme l. 599-604 | numérique, blockchain, systèmes privés d'échange de titres, nouveaux acteurs | [V] | F06 § 0 et 6 |
| Régime pilote européen des infrastructures de marché fondées sur la blockchain (règlement (UE) 2022/858) | cadre d'expérimentation de la négociation et du règlement de titres tokenisés | [S] | F06 § 6 |
| Jensen et Meckling (1976) | théorie de l'agence, alignement des dirigeants par la rémunération | [V programme 2.1] | F10 § 3 |
| Freeman (1984) | parties prenantes, valeur partenariale | [V programme 2.1] | F10 § 3 |
| Sharpe (1964) | MEDAF | [S] | F10 § 2 |
| Akerlof (1970) ; Spence (1973) | asymétrie d'information ; signal coûteux et crédible | [V programme 5.1 et 4.1] | F10 § 1 et 3 |
| Taux sans risque de 4,0 % et prime de risque du marché de 5,0 % ; bêtas d'actif de 0,64 à 0,76 ; coût de la dette de 5,00 % | hypothèses d'énoncé, dans les fourchettes de F11 | [S] | F11 § 1 à 3 |
| Indicateurs, quotas et prix du quota, grille de notation, propulsions, scénarios, offres d'obligation | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 3.1 à 3.5 |
