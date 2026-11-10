# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 26 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F04 diagnostic financier consolidé, F07 risques de change et de taux, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (ratios de diagnostic, flux de l'usine, VAN, TRI, indice de profitabilité, délai de récupération actualisé, VAN par scénario, espérance et écart-type, achat à terme, contrats à terme sur devises, swap de devises et coûts actuariels, barème, liste noire, hors-programme ; cours à terme par la parité des taux, coût de l'usine, flux différentiels et première échéance vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VAN calculée à partir de flux en dollars erronés, ou des VAN de scénario calculées avec un coût de l'usine erroné).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Capacité du groupe à financer l'usine | `1.a` Réaliser une analyse financière des comptes consolidés ; `1.c` Apprécier la performance opérationnelle et financière d'un groupe | 3 |
| 2.2 Incertitude, rentabilité exigée et prime de risque du projet | `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique | 1 |
| 2.3 Cours à terme, flux du projet et critères de choix | `7.1.a` Évaluer et classer des projets en milieu certain ; `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) | 4 |
| 2.4 VAN dans trois scénarios de cours du dollar | `7.1.b` Évaluer et classer des projets en milieu incertain | 2 |
| 2.5 Couverture du paiement de la construction | `6.3.a` Caractériser la position de change ; `6.3.b` Comprendre le fonctionnement du marché des changes ; `6.3.d` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (change) | 4 |
| 2.6 Financement de l'usine et exposition durable au dollar | `6.3.c` Maîtriser les techniques internes et les garanties externes ; `6.3.d` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (change) ; `7.2.a` Comparer les sources de financement et notamment leurs coûts | 3 |
| **Total** | | **17** |

Part du calcul : 10 points (2.1-01 à 2.1-03, 2.1-04 pour moitié, 2.3-01 à 2.3-05, 2.4-01, 2.4-02, 2.5-02 à 2.5-04, 2.6-02). Part de l'analyse : 7 points (question 2.2 entière, 2.1-04 pour moitié, 2.3-06, 2.4-03, 2.5-01, 2.5-05, 2.5-06, 2.6-01, 2.6-03, 2.6-04). Les commentaires valent plus de 40 % des points : un calcul sans conclusion pour la direction ne rapporte qu'une partie de la question (`JUR-T13`).

---

### 2.1 Capacité du groupe à financer l'usine (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | CAF : 49,00 M€ (2025) et 52,80 M€ (2026) ; flux de trésorerie disponible : 19,00 et 17,80 M€ | 0,5 |
| 2.1-02 | DFN / EBITDA : 1,65 puis 1,39 avec les dettes locatives ; 1,52 puis 1,25 sans les dettes locatives (EBITDA hors effet de la norme : 58,50 et 62,20 M€) ; DFN / capitaux propres : 34,46 % puis 28,93 % | 1 |
| 2.1-03 | Rentabilité économique après IS : 7,54 % puis 7,68 %, supérieure au CMPC de 7,00 % de 0,54 puis 0,68 point | 0,5 |
| 2.1-04 | Ratio de l'engagement bancaire après financement de l'usine par dette : 1,94 (≤ 2,50) ; conclusion argumentée sur la capacité de financement | 1 |

**Autofinancement et flux disponible (0,5 pt).**

| M€ | 2025 | 2026 |
|---|---:|---:|
| Résultat net + dotations aux amortissements = **CAF** | 27,00 + 22,00 = **49,00** | 28,80 + 24,00 = **52,80** |
| − Augmentation du BFR | − 3,00 | − 3,80 |
| = Flux net lié à l'activité | 46,00 | 49,00 |
| − Acquisitions d'immobilisations | − 24,00 | − 28,00 |
| − Remboursements des dettes locatives | − 3,00 | − 3,20 |
| = **Flux de trésorerie disponible** | **19,00** | **17,80** |
| − Dividendes versés | − 6,00 | − 6,80 |
| = Flux disponible après dividendes | 13,00 | 11,00 |

La CAF progresse (12,6 % puis 12,9 % du chiffre d'affaires) ; le flux disponible baisse légèrement parce que les investissements augmentent (28 M€, plus que les 20,8 M€ de dotations hors droits d'utilisation) : le groupe investit déjà au-delà du renouvellement. Les dettes locatives sont remboursées avant de mesurer le flux disponible : elles financent des actifs d'exploitation (entrepôts, véhicules).

**Endettement (1 pt).**

| | 2025 | 2026 |
|---|---:|---:|
| DFN = emprunts + dettes locatives − trésorerie | 115 + 13 − 26 = 102,00 | 108 + 14 − 30 = 92,00 |
| **DFN / EBITDA** | 102 / 62 = **1,65** | 92 / 66 = **1,39** |
| DFN hors dettes locatives | 89,00 | 78,00 |
| EBITDA hors effet de la norme (EBITDA − loyers) | 62 − (3,00 + 0,50) = 58,50 | 66 − (3,20 + 0,60) = 62,20 |
| **DFN hors dettes locatives / EBITDA hors effet de la norme** | **1,52** | **1,25** |
| **DFN / capitaux propres** | 102 / 296 = **34,46 %** | 92 / 318 = **28,93 %** |

L'endettement est modéré et en baisse : la dette recule de 10 M€ en 2026, alors que les capitaux propres augmentent du résultat mis en réserve. Les deux lectures de la DFN / EBITDA donnent le même diagnostic ; la lecture « hors norme » est celle des banques (engagement des crédits) et elle retire au numérateur et au dénominateur l'effet des contrats de location.

**Rentabilité économique et CMPC (0,5 pt).** ROCE après IS = résultat opérationnel × (1 − 25 %) / capitaux employés : 40 × 0,75 / 398 = **7,54 %** en 2025 ; 42 × 0,75 / 410 = **7,68 %** en 2026. La rentabilité des capitaux employés dépasse le CMPC de **0,54** puis **0,68 point** : le groupe crée de la valeur, mais avec une marge étroite ; un nouvel investissement doit offrir une rentabilité au moins égale au CMPC pour ne pas la diluer. Le TRI de l'usine (10,00 %, question 2.3) l'améliorerait.

**Engagement bancaire et conclusion (1 pt).**
- Si les 42,54 M€ de l'usine (question 2.3) étaient entièrement empruntés, sur la base de 2026 : (78,00 + 42,54) / 62,20 = **1,94**, sous le plafond de 2,50 ; avec les dettes locatives, la DFN / EBITDA passerait à 134,54 / 66 = 2,04 et la DFN / capitaux propres à 42,31 % (valorisé, non exigé). Le calcul est prudent : il ignore le flux disponible de 2027 et l'EBITDA que l'usine apportera à partir de 2028 (10 M$ puis 18 M$).
- Le flux disponible après dividendes (11 M€ en 2026) ne paierait l'usine qu'en près de quatre ans : l'autofinancement ne suffit pas en 2027, mais le groupe a une capacité d'endettement inemployée. Financer l'usine par dette, sans augmentation de capital, est cohérent avec le financement hiérarchique de Myers et Majluf (1984) et convient à des actionnaires (fondation et famille) qui ne souhaitent pas être dilués.
- Limites : la marge de manœuvre restante sous l'engagement (environ 35 M€ de dette supplémentaire à EBITDA constant) serait réduite en cas de baisse de l'EBITDA ; le plan stratégique doit garder des réserves pour un démarrage plus lent de l'usine.
- **Conclusion** : le groupe peut financer l'usine par endettement sans menacer sa solidité financière.

**Réponses tolérées** : CAF calculée à partir du flux lié à l'activité (46 + 3 et 49 + 3,8) ; flux disponible défini avant remboursement des dettes locatives s'il est cohérent avec la DFN retenue ; pro forma calculé sur l'EBITDA publié et la DFN totale (2,04), si l'écart avec la définition de l'engagement est relevé ; DFN pro forma diminuée du flux disponible de 2027 estimé, si l'hypothèse est écrite.

**Erreurs fréquentes**
- Retrancher les dividendes ou la variation des emprunts pour obtenir le flux de trésorerie disponible.
- Mélanger les deux lectures : DFN hors dettes locatives rapportée à l'EBITDA publié, ou l'inverse.
- Calculer la rentabilité économique avant impôt, ou sur le résultat net, avant de la comparer au CMPC, qui est un taux après impôt.
- Construire un bilan économique : les capitaux employés sont fournis.
- `JUR-E01` — confusion entre CAF, flux lié à l'activité et flux disponible ; `JUR-T07` — ratios en ligne, sans tableau sur deux années.

---

### 2.2 Incertitude, rentabilité exigée et prime de risque du projet (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Relation incertitude – rentabilité exigée : aversion au risque, prime de risque, seul le risque systématique rémunéré (MEDAF) | 0,5 |
| 2.2-02 | Discussion de la prime de 1,5 point : risques spécifiques déjà traités par les flux, les scénarios et les couvertures ; double prise en compte ; effet sur les flux lointains ; méthode préférable (CMPC du groupe et scénarios, ou bêta de projet) | 0,5 |

**Incertitude et rentabilité exigée (0,5 pt).** Les apporteurs de capitaux sont averses au risque : ils n'acceptent un placement incertain que s'il leur promet, en moyenne, une rentabilité supérieure au taux sans risque (3,5 % ici). La rentabilité exigée est le taux sans risque augmenté d'une prime de risque, d'autant plus forte que l'incertitude des flux est grande ; c'est elle qui sert de taux d'actualisation, et la VAN n'est positive que si le projet rapporte plus que cette rentabilité exigée. Selon le MEDAF (Sharpe, 1964), seul le **risque systématique**, lié à la conjoncture et mesuré par le bêta, est rémunéré, car le **risque spécifique** peut être éliminé par la diversification (Markowitz, 1952) : k = rf + β × prime de risque du marché (5,5 %). Le CMPC du groupe (7,00 %) rémunère ainsi les risques systématiques des métiers des arômes et des ingrédients de parfumerie, pondérés entre fonds propres et dette.

**La prime de 1,5 point (0,5 pt).**
- **Ce que la prime prétend couvrir** : le change, le démarrage industriel et la nouvelle main-d'œuvre. Ces risques sont surtout **spécifiques** au projet : ils ne dépendent pas du marché dans son ensemble et un actionnaire diversifié ne les ferait pas payer. Le métier de l'usine est celui du groupe (arômes vendus à ses clients nord-américains) : son risque systématique est voisin de celui du groupe, et les États-Unis sont un pays développé, sans risque pays particulier ; rien n'indique que le bêta du projet soit plus élevé.
- **Double prise en compte** : le risque de change est déjà intégré dans les flux (conversion aux cours à terme, question 2.3), mesuré par les scénarios (question 2.4) et réduit par les couvertures (questions 2.5 et 2.6) ; majorer aussi le taux le compterait deux fois. Les risques de démarrage relèvent de flux prudents (montée en charge en 2028-2029) et de l'analyse de sensibilité, pas du taux.
- **Effet mécanique** : une prime appliquée chaque année pénalise d'autant plus un flux qu'il est lointain (facteur 1,085^n au lieu de 1,07^n), ici la valeur résiduelle de 2033, alors que le risque de démarrage porte sur les premières années.
- **Nuance** : l'actionnaire principal, une fondation qui détient 64 % du capital, est peu diversifié et a un horizon long ; sa prudence est légitime, mais elle s'exprime mieux par l'analyse des scénarios et par un seuil d'acceptation explicite que par une prime forfaitaire.
- **Conclusion** : retenir le CMPC du groupe (7,00 %), et mesurer les risques propres au projet par les scénarios. Le débat ne change pas la décision : le TRI de 10,00 % dépasse aussi 8,50 % (VAN de 2,52 M€ à ce taux, question 2.3 ; valorisé si la question 2.3 est traitée, la décision étant notée à l'item 2.3-06).

**Réponses tolérées** : maintien d'une prime réduite, si le candidat la justifie par un risque systématique plus élevé du marché nord-américain ou par la faible diversification de la fondation et s'il signale le risque de double prise en compte ; référence à un bêta de projet ou à des comparables américains comme meilleure méthode que la prime forfaitaire.

**Erreurs fréquentes**
- Justifier la prime par le risque total du projet, sans distinguer le risque spécifique, diversifiable, du risque systématique.
- Ajouter la prime et pénaliser aussi les flux dans les scénarios sans voir la double prise en compte.
- Actualiser au coût de la dette ou au coût des fonds propres seuls : les flux du projet sont des flux d'exploitation, à actualiser au CMPC.
- `JUR-T14` — prime de risque définie sans le MEDAF ni la diversification ; `JUR-T13` — discussion générale sans le métier du projet ni les scénarios du cas.

---

### 2.3 Cours à terme, flux du projet et critères de choix (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Cours à terme F(2) à F(7) : 1,1425 ; 1,1539 ; 1,1655 ; 1,1771 ; 1,1889 ; 1,2008 ; euro en report, dollar en déport | 0,5 |
| 2.3-02 | Coût de l'usine 21,32 + 21,22 = 42,54 M€ ; flux différentiels en dollars : 2,60 ; 8,75 ; 11,40 ; 12,00 ; 12,00 ; 29,00 M$ | 1 |
| 2.3-03 | Contre-valeur en euros : 2,28 ; 7,58 ; 9,78 ; 10,19 ; 10,09 ; 24,15 M€ | 0,5 |
| 2.3-04 | VAN au CMPC de 7,00 % : 5,25 M€ ; indice de profitabilité : 1,12 | 0,5 |
| 2.3-05 | TRI : 10,00 % ; délai de récupération actualisé : 5,67 ans | 0,5 |
| 2.3-06 | Commentaire : création de valeur, poids de la valeur résiduelle, marge perdue à l'export, décision inchangée à 8,50 % | 1 |

**Cours à terme (0,5 pt).** F(n) = 1,1200 × (1,0403 / 1,03)^n = 1,1200 × 1,01^n.

| Fin d'année | 2027 (n = 1) | 2028 (2) | 2029 (3) | 2030 (4) | 2031 (5) | 2032 (6) | 2033 (7) |
|---|---:|---:|---:|---:|---:|---:|---:|
| F(n), 1 EUR = x USD | 1,1312 | **1,1425** | **1,1539** | **1,1655** | **1,1771** | **1,1889** | **1,2008** |

Le cours à terme est supérieur au comptant (1,1200) : il faut plus de dollars pour un euro à terme qu'au comptant ; l'**euro est en report** et le **dollar en déport**, parce que le taux d'intérêt du dollar (4,03 %) dépasse celui de l'euro (3,00 %). Ce déport n'est pas une prévision de baisse du dollar : il égalise le rendement d'un placement en euros et celui d'un placement en dollars couvert à terme (absence d'arbitrage). Les flux en dollars du projet sont donc convertis en un peu moins d'euros chaque année.

**Coût de l'usine et flux différentiels en dollars (1 pt).** Coût en euros = 24 / 1,1256 + 24 / 1,1312 = 21,32 + 21,22 = **42,54 M€**.

| M$ | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 |
|---|---:|---:|---:|---:|---:|---:|
| Chiffre d'affaires | 34,00 | 44,00 | 50,00 | 50,00 | 50,00 | 50,00 |
| − Charges variables (50 %) et fixes (7,00) | − 24,00 | − 29,00 | − 32,00 | − 32,00 | − 32,00 | − 32,00 |
| = EBITDA | 10,00 | 15,00 | 18,00 | 18,00 | 18,00 | 18,00 |
| − Amortissement | − 6,00 | − 6,00 | − 6,00 | − 6,00 | − 6,00 | − 6,00 |
| = Résultat d'exploitation | 4,00 | 9,00 | 12,00 | 12,00 | 12,00 | 12,00 |
| IS à 25 % | − 1,00 | − 2,25 | − 3,00 | − 3,00 | − 3,00 | − 3,00 |
| BFR (10 % du CA) | 3,40 | 4,40 | 5,00 | 5,00 | 5,00 | 5,00 |
| Flux de l'usine = EBITDA − IS − variation du BFR | 5,60 | 11,75 | 14,40 | 15,00 | 15,00 | 15,00 |
| − Marge perdue à l'export | − 3,00 | − 3,00 | − 3,00 | − 3,00 | − 3,00 | − 3,00 |
| + Valeur résiduelle et récupération du BFR | | | | | | + 17,00 |
| **Flux différentiel** | **2,60** | **8,75** | **11,40** | **12,00** | **12,00** | **29,00** |

Les variations du BFR sont de 3,40, 1,00 et 0,60 M$ en 2028, 2029 et 2030, puis nulles ; les 5,00 M$ sont récupérés en 2033 avec la valeur résiduelle (12,00 M$, égale à la valeur nette comptable 48 − 6 × 6, sans impôt). Le projet se mesure par rapport à la poursuite des exportations : la marge que Grasse perdra est un coût du projet (effet de cannibalisation).

**Contre-valeur en euros (0,5 pt).**

| M€ | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 |
|---|---:|---:|---:|---:|---:|---:|
| Flux en € = flux en $ / F(n) | 2,28 | 7,58 | 9,78 | 10,19 | 10,09 | 24,15 |
| Facteur d'actualisation à 7 % | 0,9346 | 0,8734 | 0,8163 | 0,7629 | 0,7130 | 0,6663 |
| Flux actualisé | 2,13 | 6,62 | 7,98 | 7,77 | 7,19 | 16,09 |
| Cumul (depuis − 42,54) | − 40,41 | − 33,79 | − 25,81 | − 18,03 | − 10,84 | + 5,25 |

**VAN et indice de profitabilité (0,5 pt).** VAN au 31 décembre 2027 = − 42,54 + 47,79 = **5,25 M€** ; indice de profitabilité = 47,79 / 42,54 = **1,12** : chaque euro investi rapporte 1,12 € de valeur actuelle.

**TRI et délai de récupération actualisé (0,5 pt).** VAN à 10 % : 0,00 M€ : le **TRI est bien de 10,00 %** (pour mémoire, VAN à 9 % : 1,66 M€). Délai de récupération actualisé : à la fin de 2032, il reste 10,84 M€ à récupérer, sur un flux actualisé de 16,09 M€ en 2033 : 5 + 10,84 / 16,09 = **5,67 ans** (environ huit mois après le début de 2033).

**Commentaire (1 pt).**
- Le projet **crée de la valeur** : VAN positive de 5,25 M€, TRI de 10,00 % supérieur de 3 points au CMPC, ce qui améliorerait la rentabilité économique du groupe (7,68 %, question 2.1).
- **Décision inchangée au taux majoré** : le TRI dépasse aussi 8,50 % ; la VAN à 8,50 % reste positive (2,52 M€). Le débat de la question 2.2 porte sur le montant de la valeur créée, pas sur la décision.
- Le projet est **fragile** : le délai de récupération actualisé (5,67 ans) est presque égal à l'horizon de six ans ; la valeur actuelle de la valeur résiduelle et du BFR récupéré (environ 9,43 M€) dépasse la VAN : sans elle, la VAN serait négative (environ − 4,2 M€). La décision repose sur la valeur de l'usine à la fin de 2033, donc sur sa capacité à produire au-delà de l'horizon étudié, qui joue plutôt en faveur du projet (l'usine est amortie sur huit ans).
- La **marge perdue à l'export** pèse lourd : l'usine seule aurait une VAN d'environ 17,5 M€ ; la cannibalisation des ventes de Grasse (valeur actuelle d'environ 12,2 M€) en retire plus des deux tiers. Il faut vérifier que les clients américains ne seraient pas perdus sans usine locale : si les exportations devaient de toute façon reculer, la marge perdue serait surestimée et la VAN sous-estimée.
- La conversion aux cours à terme intègre le déport du dollar, mais pas le risque d'un cours très différent : c'est l'objet de la question 2.4.

**Réponses tolérées** : flux en dollars actualisés au taux de 8,07 % (taux en dollars équivalent : 1,07 × 1,01 − 1), puis convertis au cours F(1) de 1,1312, ce qui donne la même VAN aux arrondis près (5,26 M€) ; TRI par interpolation entre 9 % et 10 % (10,00 %) ; flux en euros non arrondis (VAN de 5,25 ou 5,26 M€) ; délai de récupération exprimé en années et en mois.

**Erreurs fréquentes**
- Oublier la marge perdue à l'export : la VAN de l'usine seule surestime la valeur créée par la décision.
- Retrancher le niveau du BFR au lieu de sa variation, ou oublier de le récupérer en 2033.
- Calculer l'impôt sur l'EBITDA, ou retrancher des frais financiers des flux.
- Convertir tous les flux au cours comptant de 1,1200, ou inverser la formule (diviser par 1,01^n) : le dollar est en déport, les cours à terme montent.
- Multiplier un flux en dollars par le cours : avec une cotation au certain, montant en euros = montant en dollars / cours.
- `JUR-T04` — VAN, TRI et délai de récupération mal maîtrisés ; `JUR-T07` — flux sans tableau annuel.

---

### 2.4 VAN dans trois scénarios de cours du dollar (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Valeur actuelle à 7 % des flux en dollars : 56,41 M$ ; VAN : 11,19 M€ (dollar fort), 6,51 M€ (dollar stable), − 0,75 M€ (dollar faible) | 0,5 |
| 2.4-02 | Espérance de la VAN : 5,87 M€ ; variance 18,24 ; écart-type : 4,27 M€ | 0,5 |
| 2.4-03 | Lecture du risque : dispersion, probabilité de VAN négative de 25 %, cours qui annule la VAN, rôle des couvertures | 1 |

**VAN par scénario (0,5 pt).** Avec un cours constant, la conversion se fait après l'actualisation : VAN = (valeur actuelle à 7 % des flux en dollars) / cours − 42,54. Valeur actuelle des flux en dollars : 2,60 × 0,9346 + 8,75 × 0,8734 + 11,40 × 0,8163 + 12,00 × 0,7629 + 12,00 × 0,7130 + 29,00 × 0,6663 = **56,41 M$**.

| Scénario | Cours | Valeur actuelle en € | VAN (M€) | Probabilité |
|---|---:|---:|---:|---:|
| Dollar fort | 1,0500 | 53,73 | **11,19** | 25 % |
| Dollar stable | 1,1500 | 49,05 | **6,51** | 50 % |
| Dollar faible | 1,3500 | 41,79 | **− 0,75** | 25 % |

**Espérance et écart-type (0,5 pt).** E(VAN) = 0,25 × 11,19 + 0,50 × 6,51 + 0,25 × (− 0,75) = **5,87 M€**. Variance = 0,25 × (11,19 − 5,87)² + 0,50 × (6,51 − 5,87)² + 0,25 × (− 0,75 − 5,87)² = 7,08 + 0,20 + 10,96 = **18,24** ; écart-type = **4,27 M€**.

**Lecture du risque (1 pt).**
- L'espérance de la VAN est positive (5,87 M€), voisine de la VAN aux cours à terme (5,25 M€). Le scénario « dollar stable » (1,1500) donne une VAN supérieure à celle de la question 2.3, parce que les cours à terme montent de 1,1425 à 1,2008 : ils intègrent le déport du dollar ; mais l'écart-type (4,27 M€) atteint près des trois quarts de l'espérance (coefficient de variation de 0,73) : la valeur créée dépend fortement du dollar.
- Le projet ne détruit de la valeur que dans le scénario du dollar faible, avec une probabilité de **25 %**, et la perte reste faible (− 0,75 M€) au regard du gain possible (+ 11,19 M€) : l'asymétrie est favorable. Le cours constant qui annule la VAN est de 56,41 / 42,54 ≈ **1,3261** (valorisé, non exigé) : le dollar devrait se déprécier de près de 16 % par rapport au comptant d'aujourd'hui (1,1200) et rester à ce niveau six ans.
- Le projet est **long en dollars** : ses recettes nettes en dollars perdent de la valeur en euros quand le dollar baisse. Le coût de l'usine, couvert à terme, est fixé en euros ; les charges de l'usine, payées en dollars (matières achetées localement, personnel), réduisent déjà l'exposition à la seule marge.
- Les scénarios ne mesurent que le risque de change, avec un cours constant : ils n'intègrent ni le volume, ni le prix des matières, ni le démarrage. Pour la direction, l'exposition au dollar ne remet pas en cause le projet ; elle justifie de l'atténuer par un financement en dollars (question 2.6) plutôt que par une prime sur le taux (question 2.2).

**Réponses tolérées** : VAN de scénario calculées année par année (flux en dollars convertis au cours du scénario, puis actualisés), écarts d'arrondi de 0,01 M€ ; variance calculée sur les VAN arrondies (18,24) ; lecture par le coefficient de variation ou par l'intervalle espérance ± écart-type ; probabilité de VAN négative lue sur les scénarios (25 %).

**Erreurs fréquentes**
- Convertir aussi le coût de l'usine au cours du scénario alors qu'il est couvert à terme.
- Calculer une moyenne simple des trois VAN, sans les probabilités.
- Conclure sur l'espérance seule, sans mesurer la dispersion ni la probabilité de perte.
- Inverser le sens du risque : une hausse du cours au certain (1,35) est une baisse du dollar, défavorable pour des recettes en dollars.
- `JUR-T13` — risque commenté en termes généraux, sans les scénarios du cas.

---

### 2.5 Couverture du paiement de la construction (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Position courte en dollars de 48 M$ (24 M$ au 30 juin et 24 M$ au 31 décembre 2027), ouverte ; risque de hausse du dollar (baisse du cours au certain) | 0,5 |
| 2.5-02 | Achat à terme : 21 321 962 € et 21 216 407 €, soit 42 538 369 € ; comparaison avec le comptant (report favorable à l'acheteur de dollars) | 0,5 |
| 2.5-03 | Contrats à terme : vente de contrats libellés en euros ; 169 contrats (169,31 arrondis) ; 23 955 750 $ couverts, 44 250 $ non couverts ; dépôt de garantie de 507 000 € | 1 |
| 2.5-04 | Baisse du dollar : perte de 1 457 625 $ (1 214 688 €), coût net 21 214 688 €, cours effectif 1,1313 ; hausse du dollar : gain de 1 719 575 $ (1 637 690 €), coût net 21 219 453 €, cours effectif 1,1310 | 1 |
| 2.5-05 | Couverture imparfaite (arrondi, base, appels de marge) ; marché organisé et gré à gré | 0,5 |
| 2.5-06 | Recommandation argumentée | 0,5 |

**Position et risque (0,5 pt).** Le contrat crée une dette de 48 M$ sans créance en dollars de même échéance : la position est **courte en dollars** (24 M$ au 30 juin et 24 M$ au 31 décembre 2027) et **ouverte**. AURÉVANCE craint la **hausse du dollar**, c'est-à-dire la baisse du cours au certain : à 1,0500, les 48 M$ coûteraient 45,71 M€, contre 42,86 M€ au comptant du jour ; à 1,2000, 40,00 M€ seulement. C'est un risque de transaction, sur un montant élevé (près des deux tiers de l'EBITDA de 2026).

**Achat à terme (0,5 pt).**

| Échéance | Montant | Cours à terme | Coût garanti |
|---|---:|---:|---:|
| 30 juin 2027 | 24 000 000 $ | 1,1256 | **21 321 962 €** |
| 31 décembre 2027 | 24 000 000 $ | 1,1312 | **21 216 407 €** |
| **Total** | 48 000 000 $ | | **42 538 369 €** |

L'achat à terme ferme la position : le coût est connu dès aujourd'hui, quel que soit le cours à l'échéance. Parce que l'euro est en report, acheter les dollars à terme coûte 318 774 € de moins qu'au comptant du jour (42 857 143 €) : le report reflète l'écart de taux (l'entreprise garde ses euros, placés à 3,00 %, alors que le dollar rapporte 4,03 %), il ne constitue pas un gain de change. En contrepartie, AURÉVANCE renonce au gain si le dollar baisse.

**Contrats à terme : mise en place (1 pt).** Le contrat porte sur 125 000 € et est coté en dollars pour un euro. AURÉVANCE doit acheter des dollars, donc vendre des euros : elle **vend** des contrats de mars 2028 au cours de 1,1340, et les rachète le 31 décembre 2027. Si le dollar monte, le cours du contrat baisse et la vente dégage un gain qui compense le surcoût de l'achat au comptant.
- Nombre de contrats = 24 000 000 / (125 000 × 1,1340) = 169,31, arrondi à **169 contrats**.
- Dollars couverts : 169 × 125 000 × 1,1340 = **23 955 750 $** ; non couverts : **44 250 $**, achetés au comptant le 31 décembre.
- Dépôt de garantie : 169 × 3 000 = **507 000 €**, versé à l'ouverture et restitué au dénouement ; s'y ajoutent des appels de marge quotidiens en cas d'évolution défavorable.

**Contrats à terme : résultats (1 pt).** Résultat en dollars = 169 × 125 000 × (1,1340 − cours de dénouement), converti au comptant du 31 décembre 2027.

| | Baisse du dollar | Hausse du dollar |
|---|---:|---:|
| Cours comptant / cours du contrat de mars 2028 | 1,2000 / 1,2030 | 1,0500 / 1,0526 |
| Résultat sur contrats (dollars) | − 1 457 625 $ | + 1 719 575 $ |
| Résultat sur contrats (euros, au comptant) | − 1 214 688 € | + 1 637 690 € |
| Achat de 24 M$ au comptant | 20 000 000 € | 22 857 143 € |
| **Coût net de l'échéance** | **21 214 688 €** | **21 219 453 €** |
| **Cours effectif** (24 M$ / coût net) | **1,1313** | **1,1310** |
| Pour mémoire, achat à terme bancaire | 21 216 407 € | 21 216 407 € |

Dans les deux scénarios, le coût net reste très proche de celui de l'achat à terme (écart de − 1 719 € et + 3 046 €, calculés sur les montants arrondis à l'euro) : la couverture neutralise le mouvement du dollar (2,86 M€ d'écart entre les deux coûts sans couverture).

**Couverture imparfaite, marché organisé et gré à gré (0,5 pt).**
- **Arrondi** : 169 contrats ne couvrent pas exactement 24 M$ ; 44 250 $ restent exposés.
- **Base** : le contrat de mars 2028 n'a pas encore convergé vers le comptant le 31 décembre (base de − 0,0030 et − 0,0026) ; le cours effectif sur la partie couverte est le cours de dénouement du contrat, et non le comptant, d'où un résultat qui dépend de la base à cette date, inconnue aujourd'hui. Le cours initial de 1,1340 contient trois mois de report de plus que le terme du 31 décembre (1,1312), que la base restitue au dénouement.
- **Trésorerie** : si le dollar baisse, les appels de marge cumulés atteignent environ 1,46 M$, à financer au fil de l'année, en plus du dépôt de 507 000 €.
- **Marché organisé** : contrats standardisés (montant, échéances), cotés et liquides, prix transparent, chambre de compensation qui supprime le risque de contrepartie, en échange du dépôt de garantie et des appels de marge ; possibilité de dénouer à tout moment. **Gré à gré** : l'achat à terme de la Banque ORLÉMAR est sur mesure (montant et date exacts), sans dépôt ni appel de marge, mais il expose au risque de contrepartie de la banque et ne se dénoue qu'en négociant avec elle.

**Recommandation (0,5 pt).** Couvrir les deux échéances par l'**achat à terme bancaire** : coût garanti de 42 538 369 €, adapté exactement aux montants et aux dates du contrat, sans immobilisation de trésorerie ni gestion quotidienne des appels de marge, pour un coût équivalent à celui des contrats cotés. Les contrats à terme ne se justifieraient que pour garder la possibilité de dénouer facilement, par exemple si le calendrier des paiements est incertain. Si la direction souhaitait profiter d'une baisse du dollar, une option d'achat de dollars (prime à payer) serait l'alternative, au prix de cette prime. Le choix du financement (question 2.6) peut toutefois rendre l'essentiel de cette couverture inutile.

**Réponses tolérées** : présentation du sens de l'opération comme un « achat de dollars à terme sur le marché organisé », si le candidat vend bien des contrats libellés en euros ; nombre de contrats arrondi à 170 avec une sur-couverture correctement mesurée ; résultats à l'euro près ; recommandation des contrats à terme pour leur liquidité, si le candidat mesure le dépôt, les appels de marge et la base.

**Erreurs fréquentes**
- Acheter des contrats libellés en euros : c'est la position d'un exportateur qui vend des dollars.
- Calculer le nombre de contrats en divisant 24 M$ par 125 000, sans convertir la taille du contrat en dollars.
- Convertir le résultat des contrats au cours initial au lieu du comptant du 31 décembre.
- Présenter le report comme un gain de change, ou la couverture comme un coût certain.
- `JUR-T07` — résultats des deux scénarios sans tableau ; `JUR-T13` — avantages généraux des marchés organisés sans le montant, la date et le dépôt du cas.

---

### 2.6 Financement de l'usine et exposition durable au dollar (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Exposition durable : position longue structurelle (usine de 48 M$, recettes nettes en dollars de 2028 à 2033), risque de baisse du dollar, que des ventes à terme successives de dollars ne couvrent que partiellement (montants incertains, horizon long) | 0,5 |
| 2.6-02 | Swap : nominal 44,80 M$, intérêts 2,24 M$ par an, échange final ; flux 44,80 ; − 2,24 (quatre ans) ; − 47,04 M$ ; contre-valeurs 40,0000 ; − 1,9802 ; − 1,9606 ; − 1,9412 ; − 1,9219 ; − 39,9626 M€ ; coût en euros 3,96 % | 1 |
| 2.6-03 | Comparaison des trois montages ; adossement des dettes aux actifs et aux flux, achats locaux | 1 |
| 2.6-04 | Articulation avec la couverture de la construction et recommandation | 0,5 |

**Exposition durable (0,5 pt).** À partir de 2028, le groupe détiendra un actif en dollars (l'usine, 48 M$) et recevra chaque année des flux nets en dollars (question 2.3) : il sera **long en dollars** de façon structurelle et craindra la **baisse** du dollar, qui réduirait la contre-valeur en euros des flux et de l'actif (scénario « dollar faible » de la question 2.4). Ce risque, durable et de montant incertain, ne se couvre pas raisonnablement par des ventes à terme successives de dollars : il se réduit d'abord en logeant en dollars une partie des charges et des dettes.

**Emprunt en euros associé au swap de devises (1 pt).** Nominal en dollars : 40 × 1,1200 = **44,80 M$** ; intérêts reçus en euros : 40 × 3,90 % = 1,56 M€, qui paient l'emprunt ; intérêts payés en dollars : 44,80 × 5,00 % = **2,24 M$**.

| Date | Jambe euro du swap (M€) | Jambe dollar du swap (M$) | Flux nets d'AURÉVANCE après emprunt et swap (M$) | Cours | Contre-valeur (M€) |
|---|---:|---:|---:|---:|---:|
| 4 janvier 2027 | − 40,00 (remis) | + 44,80 | **+ 44,80** | 1,1200 | **40,0000** |
| 4 janvier 2028 | + 1,56 | − 2,24 | **− 2,24** | 1,1312 | **− 1,9802** |
| 4 janvier 2029 | + 1,56 | − 2,24 | **− 2,24** | 1,1425 | **− 1,9606** |
| 4 janvier 2030 | + 1,56 | − 2,24 | **− 2,24** | 1,1539 | **− 1,9412** |
| 4 janvier 2031 | + 1,56 | − 2,24 | **− 2,24** | 1,1655 | **− 1,9219** |
| 4 janvier 2032 | + 41,56 | − 47,04 | **− 47,04** | 1,1771 | **− 39,9626** |

Les flux en euros de l'emprunt et de la jambe euro s'annulent : l'emprunt en euros est transformé en une dette de 44,80 M$ à 5,00 %. Coût actuariel en euros : taux r tel que 40 = 1,9802 / (1 + r) + … + 39,9626 / (1 + r)^5, soit **r = 3,96 %**. Les cours croissent de 1 % par an, d'où r ≈ 1,05 / 1,01 − 1 = 3,96 %.

**Comparaison des montages, adossement et achats locaux (1 pt).**

| | A. Euros seuls | B. Euros + swap | C. Dollars directs |
|---|---|---|---|
| Dette du groupe | 40 M€ à 3,90 % | 44,80 M$ à 5,00 % | 44,80 M$ à 5,40 % |
| Coût en euros aux cours à terme | 3,90 % | 3,96 % | 4,36 % (valorisé) |
| Paiement de la construction | 48 M$ à couvrir (question 2.5) | 44,80 M$ disponibles dès janvier 2027 | idem B |
| Exposition durable | entière : actif et flux en dollars, dette en euros | réduite : dette et intérêts en dollars | réduite, comme B |

- **Coût** : aux cours à terme, le swap coûte presque le même taux que l'emprunt en euros (3,96 % contre 3,90 %) : la parité des taux fait que s'endetter en dollars à 5,00 % revient à s'endetter en euros à un peu plus de 3,90 %, l'écart de 0,06 point rémunérant la banque. Il n'y a pas de gain de taux à attendre d'une dette en dollars : son intérêt est la couverture. Par rapport à l'emprunt direct en dollars, le swap économise 0,40 point, soit 0,18 M$ par an : le groupe, connu des banques européennes, emprunte mieux en euros que sa filiale auprès d'une banque américaine.
- **Adossement** : avec B ou C, l'actif en dollars (usine de 48 M$) est financé pour l'essentiel par une dette en dollars (44,80 M$) ; une baisse du dollar diminue à la fois la valeur en euros de l'actif et celle de la dette. Les intérêts (2,24 M$ par an) sont payés avec les dollars de l'usine ; le remboursement de 47,04 M$ en 2032, bien supérieur aux flux d'une année, sera payé avec les dollars accumulés ou refinancé en dollars : l'exposition nette annuelle passe, par exemple en 2031, de 12,00 M$ à 9,76 M$.
- **Achats locaux** : en achetant aux États-Unis ses matières premières naturelles et de synthèse et en employant du personnel local (charges de 32 M$ par an), l'usine aligne la devise de ses charges sur celle de ses ventes : seule sa marge est exposée, alors que les exportations depuis Grasse exposent tout le chiffre d'affaires en dollars à des coûts en euros. C'est une couverture interne, sans coût ni contrepartie bancaire.
- **Limites** : risque de contrepartie sur la Banque ORLÉMAR (swap) ; engagement de cinq ans, alors que l'usine produira plus longtemps (remboursement de 47,04 M$ en 2032, avant la fin de l'étude) ; si le projet était retardé ou abandonné, la dette en dollars deviendrait une position courte non adossée.

**Articulation et recommandation (0,5 pt).**
- Avec B (ou C), les 44,80 M$ reçus le 4 janvier 2027, placés jusqu'aux échéances, paient le constructeur : la position courte de la question 2.5 est fermée pour 44,80 M$. Seuls 3,20 M$ restent à couvrir, par exemple par un achat à terme au 31 décembre 2027 (environ 2,83 M€ au cours de 1,1312). La couverture de la question 2.5 ne doit pas s'ajouter au swap : elle créerait une position longue en dollars.
- **Recommandation à Mme CARVAILHE** : retenir l'**emprunt en euros associé au swap de devises** (montage B), le moins cher des financements en dollars (3,96 % en euros, 5,00 % en dollars), qui ferme dès aujourd'hui l'essentiel du risque du paiement et adosse durablement une dette en dollars à l'actif et aux flux de l'usine ; le compléter par un achat à terme des 3,20 M$ restants et par une politique d'achats locaux. Signer le swap le jour de la signature du contrat de construction : sans contrat, la dette en dollars deviendrait une position courte non adossée. L'exposition résiduelle sur les flux nets restera à suivre chaque année.

**Réponses tolérées** : choix de l'emprunt direct en dollars (C) au nom de la simplicité ou d'une relation bancaire locale pour la filiale, si le candidat mesure son surcoût de 0,40 point ; choix de l'emprunt en euros (A) avec couverture à terme du paiement, si le candidat montre que l'exposition durable reste ouverte ; coût en euros obtenu par interpolation (3,95 % à 3,97 %) ou par la formule 1,05 / 1,01 − 1 ; mention d'un prêt en dollars de la société mère à sa filiale.

**Erreurs fréquentes**
- Croire que le swap réduit le coût de l'emprunt : il change sa devise, pas son coût actuariel aux cours à terme.
- Échanger les nominaux à l'échéance au cours à terme : l'échange final se fait au cours initial (1,1200).
- Présenter les achats locaux et l'adossement comme des instruments de marché : ce sont des techniques internes, sans contrepartie.
- Cumuler le swap et la couverture à terme des 48 M$ : la position deviendrait longue.
- Calculer les comptes de la filiale en euros : la conversion des comptes relève de la consolidation (UE 4) et n'est pas demandée.
- `JUR-T13` — avantages généraux du swap sans le montant, les taux et les dates du cas ; `JUR-T02` — couverture naturelle citée sans application aux charges de l'usine.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme DSCG UE 2 (arrêté du 4 août 2025), partie 1 ; guide pédagogique DSCG, juillet 2026, p. 57-58 | diagnostic des comptes consolidés, flux de trésorerie, rentabilité économique, retraitements fournis et non recalculés | [V] | F04 ; `perimetre_ue2.yaml` (1.a, 1.c) |
| Programme DSCG UE 2, partie 5.2 ; guide pédagogique DSCG, juillet 2026, p. 74-75 | lien entre incertitude, risque et rentabilité exigée ; prime de risque | [V] | F02 § 2 ; `perimetre_ue2.yaml` (5.2.a) |
| Markowitz (1952) ; Sharpe (1964) | diversification du risque spécifique ; MEDAF, risque systématique seul rémunéré | [V programme 5.3] ; [S] pour Sharpe (MEDAF au programme 5.2, sans auteur) | F10 § 2 ; F02 § 2 |
| Myers et Majluf (1984) | financement hiérarchique | [V programme 7.2] | F10 § 3 |
| Programme DSCG UE 2, partie 7.1 ; guide pédagogique DSCG, juillet 2026, p. 80-81 | VAN, TRI, indice de profitabilité, délai de récupération actualisé ; scénarios, espérance et écart-type de la VAN | [V] | `perimetre_ue2.yaml` (7.1.a, 7.1.b) |
| Programme DSCG UE 2, partie 6.3 ; guide pédagogique DSCG, juillet 2026, p. 78-79 | position de change, marché au comptant et à terme, parité des taux, contrats à terme sur devises, swap de devises, techniques internes ; modèles de valorisation des options exclus | [V] | F07 § 0 et 3 ; `perimetre_ue2.yaml` (6.3.a à 6.3.d) |
| Cours à terme par la parité des taux ; contrats à terme sur devises ; swap de devises | mécanismes et calculs | [S] | F07 § 3.3 |
| Taux sans risque 3,5 % ; prime de risque du marché 5,5 % ; cours EUR/USD 1,1200 | hypothèses plausibles début 2027, posées par l'énoncé (cours de référence BCE de 1,1205 le 22/10/2026) | [V] séries BCE (valeurs arrondies) | F11 § 1 et 4 |
| Comptes du groupe, CMPC, données de l'usine, taux à moyen terme, cours à terme bancaires, contrats à terme, scénarios, conditions des emprunts et du swap | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 2.1 à 2.6 |
