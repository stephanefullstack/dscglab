# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 10 — Dossier 1 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F05 ingénierie financière, F10 auteurs et théories, F11 données de marché (toutes à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (bilan, multiples, levée de fonds, MEDAF et modèle à trois facteurs, TRI, répartitions du capital, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une répartition du capital calculée avec un autre prix par action à la question 1.2).

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Multiples de l'échantillon et choix de l'inducteur | `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP ; `3.2.b` Savoir déterminer le multiple d'un échantillon pour valoriser l'entreprise | 5 |
| 1.2 Pré-money, prix par action, post-money et dilution | `3.2.a` ; `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital | 4,5 |
| 1.3 Rentabilité exigée : MEDAF, Fama et French, TRI du fonds | `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance ; `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier | 4,5 |
| 1.4 Limites des modèles et stratégie de gestion du capital | `5.2.c` ; `4.2.a` | 3 |
| **Total** | | **17** |

Part du calcul : environ 9 points (1.1-01 à 1.1-03, 1.2-01 à 1.2-04, 1.3-01 à 1.3-03, 1.4-02). Part de l'analyse : environ 8 points. Les questions 1.3 et 1.4, plus rédactionnelles, valent autant que les calculs de la question 1.1 : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 1.1 Multiples de l'échantillon et choix de l'inducteur (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Multiples des quatre sociétés cotées (VGE = capitalisation + dette nette) et médianes : VGE / CA 1,65 ; VGE / EBITDA 11,70 ; PER 20,00 | 1,5 |
| 1.1-02 | Valeurs de NAVÉLIA par les sociétés cotées : VGE 62,7 M€ (CA) et 26,9 M€ (EBITDA), VCP 64,7 et 28,9 M€ ; VCP 8,0 M€ par le PER, soit une VGE de 6,0 M€ | 1 |
| 1.1-03 | Opérations récentes : VGE / CA 2,60 ; 2,25 ; 3,20 ; médiane 2,60 ; VGE 98,8 M€ ; multiples d'EBITDA non calculables ou non significatifs | 0,5 |
| 1.1-04 | Fourchette de VGE (6,0 à 98,8 M€) ; distinction des inducteurs de VGE et de VCP | 0,5 |
| 1.1-05 | Pertinence des inducteurs au regard de la croissance et de la maturité de NAVÉLIA ; choix motivé | 1,5 |

**Conventions rappelées** : VGE d'une société cotée = capitalisation boursière + dette financière nette ; PER = capitalisation / résultat net ; multiple de l'échantillon = médiane (pour quatre sociétés, moyenne des deux valeurs centrales) des multiples arrondis à deux décimales ; agrégats 2026 ; VCP de NAVÉLIA = VGE + 2,0 M€ de trésorerie nette ; valeurs en M€ à une décimale.

**Multiples des sociétés cotées (1,5 pt).**

| Société | VGE (M€) | VGE / CA | VGE / EBITDA | PER |
|---|---:|---:|---:|---:|
| NORELVA Marine | 480 + 150 = 630 | 630 / 525 = 1,20 | 630 / 70 = 9,00 | 480 / 30 = 16,00 |
| KESTRAVO | 380 + 115 = 495 | 495 / 330 = 1,50 | 495 / 45 = 11,00 | 380 / 20 = 19,00 |
| AVELMOR Power | 462 + 96 = 558 | 558 / 310 = 1,80 | 558 / 45 = 12,40 | 462 / 22 = 21,00 |
| BRYZALE Electric | 300 + 60 = 360 | 360 / 150 = 2,40 | 360 / 12 = 30,00 | 300 / 5 = 60,00 |
| **Médiane** | | **(1,50 + 1,80) / 2 = 1,65** | **(11,00 + 12,40) / 2 = 11,70** | **(19,00 + 21,00) / 2 = 20,00** |
| Moyenne (pour comparaison) | | 1,73 | 15,60 | 29,00 |

**Valeurs de NAVÉLIA par les sociétés cotées (1 pt).**

| Inducteur | Nature | Calcul | VGE (M€) | VCP (M€) |
|---|---|---|---:|---:|
| Chiffre d'affaires | VGE | 38,0 × 1,65 | 62,7 | 62,7 + 2,0 = 64,7 |
| EBITDA | VGE | 2,3 × 11,70 = 26,91 | 26,9 | 26,9 + 2,0 = 28,9 |
| Résultat net (PER) | VCP | 0,4 × 20,00 | 8,0 − 2,0 = 6,0 | 8,0 |

La trésorerie nette s'ajoute à la VGE : la dette financière nette de NAVÉLIA est négative (− 2,0 M€), les actionnaires détiennent donc, en plus de l'actif économique, une trésorerie excédentaire.

**Opérations récentes (0,5 pt).**

| Société | Croissance | VGE / CA | VGE / EBITDA |
|---|---:|---:|---|
| OSTRALIS | 70 % | 62,4 / 24,0 = 2,60 | EBITDA négatif : non calculable |
| VELMARIS | 45 % | 45,0 / 20,0 = 2,25 | 45,0 / 0,6 = 75 : non significatif |
| TIDÉVO | 80 % | 112,0 / 35,0 = 3,20 | EBITDA négatif : non calculable |
| **Médiane** | | **2,60** | |

VGE de NAVÉLIA = 38,0 × 2,60 = **98,8 M€** ; VCP = 98,8 + 2,0 = **100,8 M€**.

**Fourchette et inducteurs (0,5 pt).** Les valeurs obtenues vont de **6,0 M€ (PER) à 98,8 M€ (CA des opérations)** de VGE : un rapport de 1 à 16, qui montre qu'un multiple n'a de sens que si l'inducteur est représentatif de la performance de l'entreprise évaluée.
- Les **inducteurs de VGE** (CA, EBITDA, résultat d'exploitation) sont mesurés avant la rémunération des prêteurs : ils valorisent l'actif économique, quelle que soit la structure financière. On en déduit la VCP en retranchant la dette financière nette (ici en ajoutant la trésorerie nette).
- Les **inducteurs de VCP** (résultat net, résultat courant avant impôt) sont mesurés après les charges financières et l'impôt : ils donnent directement la valeur des capitaux propres, mais dépendent de l'endettement et de la fiscalité. NAVÉLIA ne paie pas d'impôt (déficits antérieurs imputés), alors que le résultat net des sociétés cotées supporte normalement l'impôt : son résultat net n'est pas comparable au leur.
- Il faut rapprocher un multiple de VGE d'un inducteur de VGE et un multiple de VCP d'un inducteur de VCP : appliquer le multiple d'EBITDA puis comparer le résultat à une VCP sans tenir compte de la trésorerie est une erreur.

**Pertinence au regard de la croissance et de la maturité (1,5 pt).**
- **EBITDA et résultat net ne sont pas représentatifs.** 2026 est le premier exercice à EBITDA positif ; la marge d'EBITDA (2,3 / 38,0 = 6,1 %) est deux fois plus faible que celle des sociétés cotées matures (13 à 15 %) et le résultat net (0,4 M€, 1,1 % du CA) est presque nul. Capitaliser un résultat transitoire, encore pénalisé par les coûts de démarrage, sous-évalue fortement une entreprise dont le CA a crû de 58,3 % en 2026 (VGE de 26,9 et 6,0 M€ ; la VCP de 8,0 M€ obtenue par le PER est même inférieure aux capitaux propres comptables de 22 M€). Ces inducteurs redeviendront pertinents quand NAVÉLIA sera mature.
- **Le CA est le seul agrégat positif et significatif**, mais il ignore la rentabilité : appliquer un multiple de CA suppose que NAVÉLIA atteindra la marge des sociétés de l'échantillon. Le plan d'affaires le rend plausible : la marge d'EBITDA passerait à 16,0 % en 2029 (14,4 / 90,0).
- **Les sociétés cotées sont plus matures et plus grandes** : leur croissance est de 4 à 9 %, sauf BRYZALE (35 %), dont les multiples sont justement les plus élevés (2,40 fois le CA, 30 fois l'EBITDA, PER de 60). Le lien entre croissance et multiple apparaît clairement ; la médiane neutralise cette valeur extrême, alors que la moyenne la reflète (15,60 contre 11,70 pour l'EBITDA). Le multiple de CA médian des sociétés cotées (1,65) sous-estime donc la valeur d'une entreprise qui croît de 58 % par an : 62,7 M€ constitue un **plancher**.
- **Les opérations récentes sont les plus comparables par la maturité** : sociétés non cotées de taille voisine (CA de 20 à 35 M€), en forte croissance (45 à 80 %), valorisées lors de levées de fonds minoritaires de série B ou C, comme celle que prépare NAVÉLIA ; leur VGE ne contient pas de prime de contrôle. Leurs limites : trois opérations seulement, des valeurs issues de négociations et sensibles au moment du marché.
- **Recoupements** : la VGE de 98,8 M€ représente 1,83 fois le CA prévu pour 2027 (54,0 M€), proche du multiple médian des sociétés cotées, et 6,9 fois l'EBITDA prévu pour 2029 (14,4 M€), inférieur à leur multiple médian d'EBITDA (11,70) : elle anticipe la croissance du plan sans l'escompter entièrement.
- **Conclusion** : retenir le **multiple de CA des opérations récentes (VGE 98,8 M€)** comme référence de la négociation, le multiple de CA des sociétés cotées (62,7 M€) comme plancher, et écarter les multiples d'EBITDA et de résultat net, non représentatifs à ce stade de développement.

**Réponses tolérées** : pour 1.1-05, trois arguments liés au cas suffisent pour la totalité des points ; médiane mal calculée sur quatre valeurs (valeur la plus proche du centre retenue) : 1.1-01 réduit de moitié ; multiples arrondis à une décimale si la méthode est juste ; moyenne calculée en complément de la médiane ; VGE implicite de la méthode du PER non présentée si la nature de l'inducteur est expliquée ; choix d'un multiple de CA intermédiaire entre les sociétés cotées et les opérations s'il est justifié par la croissance et la taille.

**Erreurs fréquentes**
- Calculer la VGE des sociétés cotées sans la dette nette (VGE / CA de NORELVA à 480 / 525 = 0,91) ou rapporter la capitalisation à l'EBITDA.
- Retrancher la trésorerie nette de la VGE de NAVÉLIA (98,8 − 2,0 = 96,8 M€) au lieu de l'ajouter : la dette financière nette est négative.
- Appliquer le PER pour obtenir une VGE, ou un multiple d'EBITDA pour obtenir directement une VCP (`JUR-E03` : croiser des méthodes sans homogénéiser VGE et VCP).
- Retenir la moyenne des valeurs obtenues par les quatre méthodes (48,6 M€ de VGE) sans discuter leur pertinence.
- `JUR-T13` — discussion générale sur les multiples sans les données de NAVÉLIA (marge de 6,1 %, croissance de 58,3 %, premier EBITDA positif).

---

### 1.2 Pré-money, prix par action, post-money et dilution (4,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | Valeur pré-money = VCP = 98,8 + 2,0 = 100,8 M€ | 0,5 |
| 1.2-02 | Base entièrement diluée : 2 400 000 + 120 000 = 2 520 000 actions ; prix par action = 100 800 000 / 2 520 000 = 40,00 € | 1 |
| 1.2-03 | Actions nouvelles : 18 000 000 / 40 = 450 000 ; post-money 118,8 M€ ; 2 970 000 actions après l'opération | 1 |
| 1.2-04 | Tableau de répartition du capital après l'opération | 1 |
| 1.2-05 | Dilution : taux de 15,15 % ; fondateurs de 46 % à 43,81 % puis 37,17 % ; dilution du contrôle sans perte de valeur ; trois fonds à 50,71 % | 1 |

**Conventions rappelées** : prix par action = pré-money / (actions existantes + bons de créateur attribués), produit d'exercice des bons négligé ; actions nouvelles = montant / prix, rompus arrondis à l'unité inférieure ; post-money = pré-money + montant ; prix au centime ; pourcentages à deux décimales sur les nombres d'actions exacts.

**Pré-money (0,5 pt).** Les parties retiennent la VCP issue du multiple de CA médian des opérations : VCP = VGE − dette financière nette = 98,8 − (− 2,0) = **100,8 M€**. C'est la valeur des capitaux propres **avant** l'apport du fonds.

**Prix par action (1 pt).** Les 120 000 bons de créateur, attribués et exerçables à 12 €, bien en dessous de la valeur de l'action, seront exercés : ils doivent supporter leur part de la valeur. Base entièrement diluée : 2 400 000 + 120 000 = 2 520 000 actions. Prix = 100 800 000 / 2 520 000 = **40,00 €**.

**Actions nouvelles et post-money (1 pt).** Actions nouvelles = 18 000 000 / 40 = **450 000** (aucun rompu). Valeur post-money = 100,8 + 18,0 = **118,8 M€**, soit 2 970 000 actions × 40 € : le fonds paie le même prix que la valeur attribuée aux actions existantes.

**Répartition du capital (1 pt).**

| Actionnaires | Actions | Capital actuel | Base diluée avant l'opération | Après l'opération |
|---|---:|---:|---:|---:|
| M. Erwan KERDAVID | 600 000 | 25,00 % | 23,81 % | **20,20 %** |
| Mme Lise ANTONETTI | 504 000 | 21,00 % | 20,00 % | **16,97 %** |
| *Fondateurs* | *1 104 000* | *46,00 %* | *43,81 %* | ***37,17 %*** |
| MARVENE Capital | 624 000 | 26,00 % | 24,76 % | **21,01 %** |
| SOLENTE Ventures | 432 000 | 18,00 % | 17,14 % | **14,55 %** |
| Salariés | 240 000 | 10,00 % | 9,52 % | **8,08 %** |
| Bons de créateur (premier plan) | 120 000 | — | 4,76 % | **4,04 %** |
| BRÉCALDE Growth II | 450 000 | — | — | **15,15 %** |
| **Total** | **2 970 000** | 100 % (2 400 000) | 100 % (2 520 000) | **100,00 %** |

(Les pourcentages arrondis de la base diluée totalisent 99,99 %, écart d'arrondi.)

**Dilution des fondateurs (1 pt).**
- Taux de dilution = actions nouvelles / actions après l'opération = 450 000 / 2 970 000 = **15,15 %** : chaque actionnaire existant conserve 84,85 % de sa part sur base diluée (43,81 % × 0,8485 = 37,17 %).
- Les fondateurs passent de **46 %** du capital actuel à **43,81 %** sur base diluée (exercice des bons de créateur, − 2,19 points), puis à **37,17 %** après la série C (− 6,64 points), soit 8,83 points de moins au total.
- **Dilution du contrôle, pas de la valeur** : les actions nouvelles sont émises au prix de la valeur pré-money (40 €), si bien que la participation des fondateurs vaut toujours 1 104 000 × 40 = 44,2 M€ ; la société dispose en plus de 18,0 M€ de trésorerie pour financer sa croissance. Une émission à un prix inférieur à la valeur aurait au contraire transféré de la richesse vers le nouvel investisseur.
- **Pouvoir** : les fondateurs restent le premier bloc d'actionnaires pris isolément, mais les trois fonds réunis détiennent désormais **50,71 %** du capital (21,01 + 14,55 + 15,15), contre 44 % aujourd'hui : s'ils votent ensemble, les fondateurs perdent la maîtrise des décisions à la majorité. Les bons de créateur non exercés ne votent pas : en droits de vote (2 850 000 actions émises), les trois fonds détiennent 52,84 % et les fondateurs 38,74 %. La conclusion est la même.

**Réponses tolérées** : prix calculé sur 2 400 000 actions (42,00 €, 428 571 actions nouvelles) : item 1.2-02 non accordé, la convention de l'annexe imposant la base diluée, items suivants notés en cohérence ; raisonnement sur le contrôle mené sur la base diluée ou sur les droits de vote, si la base est précisée ; répartition présentée par catégorie (fondateurs, fonds, salariés et bons) ; dilution exprimée en points perdus ou en taux, si la notion est expliquée.

**Erreurs fréquentes**
- Confondre pré-money et post-money : calculer le prix sur 118,8 M€ (47,14 €) ou retenir 100,8 M€ comme valeur après l'opération.
- Oublier les actions nouvelles dans le dénominateur de la répartition (fondateurs à 43,81 % « après »), ou oublier les bons de créateur.
- Prendre la VGE (98,8 M€) comme pré-money, sans la trésorerie nette (prix de 39,21 €).
- `JUR-I03` — ne pas tirer les conséquences de la nouvelle structure du capital (fonds majoritaires ensemble).
- `JUR-T07` — répartition du capital sans tableau.

---

### 1.3 Rentabilité exigée : MEDAF, Fama et French, TRI du fonds (4,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | MEDAF : 4 % + 1,60 × 5 % = 12,00 % | 0,5 |
| 1.3-02 | Fama et French : 4 % + 1,30 × 5 % + 1,50 × 3 % − 0,50 × 4 % = 13,00 % (marché 6,50 ; taille + 4,50 ; valeur − 2,00 points) | 1 |
| 1.3-03 | TRI du fonds : 18,0 × (1 + TRI)⁵ = 54,0, soit TRI = 3,0^(1/5) − 1 = 24,57 % | 0,5 |
| 1.3-04 | Comparaison et explication de l'écart entre le TRI visé et la rentabilité exigée par les modèles | 1 |
| 1.3-05 | Interprétation des effets taille et valeur pour NAVÉLIA | 1,5 |

**Conventions rappelées** : taux sans risque 4 % ; prime de risque du marché 5 % ; SMB 3 % ; HML 4 % ; sensibilités données ; flux en fin d'année ; taux à deux décimales.

**MEDAF (0,5 pt).** Selon le MEDAF (Sharpe, 1964), seul le risque systématique, mesuré par le bêta, est rémunéré : rentabilité exigée = 4 % + 1,60 × 5 % = **12,00 %**.

**Modèle à trois facteurs (1 pt).** Fama et French (1993) ajoutent au facteur de marché un facteur de taille (SMB) et un facteur de valeur (HML) :

| Facteur | Sensibilité | Prime | Contribution |
|---|---:|---:|---:|
| Taux sans risque | | | 4,00 % |
| Marché | 1,30 | 5 % | 6,50 % |
| Taille (SMB) | 1,50 | 3 % | + 4,50 % |
| Valeur (HML) | − 0,50 | 4 % | − 2,00 % |
| **Rentabilité exigée** | | | **13,00 %** |

**TRI visé par le fonds (0,5 pt).** BRÉCALDE Growth II investit 18,0 M€ en 2027 et vise 3,0 × 18,0 = 54,0 M€ en 2032, sans dividende : 18,0 × (1 + TRI)⁵ = 54,0, d'où TRI = 3,0^(1/5) − 1 = **24,57 %**.

**Comparaison (1 pt).** Le TRI visé (24,57 %) est presque le double de la rentabilité exigée par les modèles (12,00 % et 13,00 %) : l'écart atteint 11,57 points avec le modèle à trois facteurs. Placée à 13,00 % pendant cinq ans, la mise ne serait multipliée que par 1,13⁵ = 1,84, et non par 3,0. Cet écart tient à ce que les modèles ignorent :
- **l'illiquidité** : le fonds ne pourra pas céder ses actions avant la sortie, alors que les modèles supposent des titres cotés, cessibles à tout moment ;
- **le risque d'échec** : le multiple de 3,0 est un objectif en cas de réussite ; dans un portefeuille de capital-risque, certaines participations sont perdues, et les réussites doivent compenser ces pertes ; la rentabilité espérée du portefeuille est donc inférieure au TRI visé sur chaque ligne ;
- **le risque spécifique** : le fonds détient un petit nombre de participations et n'est pas totalement diversifié, alors que le MEDAF et le modèle de Fama et French ne rémunèrent que les risques communs à tous les titres ;
- **l'asymétrie d'information** (Akerlof, 1970) : les fondateurs connaissent mieux que le fonds la société et la crédibilité du plan d'affaires (CA multiplié par 2,4 de 2026 à 2029) ; le fonds s'en protège par un taux élevé ;
- **les frais du fonds et son rôle actif** (présence au comité stratégique, réseau aux États-Unis), qu'il fait rémunérer.

Pour NAVÉLIA, ces fonds propres coûtent donc bien plus cher que ce qu'indiquent les modèles : c'est une raison de limiter le montant levé auprès du fonds.

**Effets taille et valeur (1,5 pt).**
- **Effet taille** (s = 1,50 > 0) : NAVÉLIA se comporte comme une petite capitalisation. Fama et French (1993) constatent que les petites sociétés ont dégagé en moyenne une rentabilité supérieure à celle des grandes, à bêta égal ; cette prime rémunère une information plus rare, une liquidité moindre et une plus grande fragilité face aux chocs. Avec une valeur post-money de 118,8 M€, 140 salariés et un seul exercice bénéficiaire, NAVÉLIA est bien plus petite que les sociétés cotées de l'échantillon (300 à 480 M€ de capitalisation) : le facteur de taille ajoute **4,50 points**.
- **Effet valeur** (h = − 0,50 < 0) : NAVÉLIA est une **valeur de croissance**. Ses capitaux propres comptables (22 M€) ne représentent que 21,8 % de la valeur pré-money (100,8 M€) : les investisseurs paient sa croissance future, non ses actifs. Les sociétés « de valeur », à rapport valeur comptable / valeur de marché élevé, ont historiquement rapporté plus que les sociétés de croissance, ce qui rémunère notamment leur risque de difficultés financières ; la sensibilité négative **retranche 2,00 points**.
- **Bilan des deux effets** : la sensibilité au marché (1,30) est plus faible que le bêta du MEDAF (1,60), ce qui peut s'expliquer par le fait qu'une partie du risque que le MEDAF attribue au marché relève de la taille (le bêta et la sensibilité b proviennent d'échantillons différents). Au total, le modèle à trois facteurs donne une rentabilité exigée supérieure d'un point à celle du MEDAF (13,00 % contre 12,00 %) : le MEDAF sous-estime le risque d'une petite société, même si l'effet de croissance en compense une partie.

**Réponses tolérées** : TRI obtenu par essais successifs à la calculatrice (24,5 % à 24,6 %) ; interprétation de l'effet valeur fondée sur la seule préférence des investisseurs pour la croissance si le signe de la sensibilité est expliqué ; comparaison fondée sur le multiple (3,0 contre 1,84) plutôt que sur les taux.

**Erreurs fréquentes**
- Utiliser le bêta du MEDAF (1,60) dans le modèle à trois facteurs (14,50 %), ou ajouter les primes sans les multiplier par les sensibilités.
- Ajouter le terme de valeur au lieu de le retrancher (17,00 %) : la sensibilité est négative.
- Calculer le TRI comme (3,0 − 1) / 5 = 40 % : c'est un rendement moyen non composé.
- `JUR-T14` — présenter Fama et French comme une théorie d'équilibre, ou ignorer qu'il prolonge le MEDAF en lui ajoutant deux facteurs.
- `JUR-T13` — interprétation des facteurs sans les données de NAVÉLIA.

---

### 1.4 Limites des modèles et stratégie de gestion du capital (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Limites du MEDAF et du modèle de Fama et French pour une start-up non cotée | 1 |
| 1.4-02 | Nouveau plan de 150 000 bons de créateur : 3 120 000 actions ; fondateurs 35,38 % ; trois fonds réunis 48,27 % | 0,5 |
| 1.4-03 | Stratégie de gestion du capital : augmentation de capital réservée, plans de bons de créateur, maîtrise de la dilution, demandes du fonds | 1 |
| 1.4-04 | Recommandation argumentée à M. KERDAVID | 0,5 |

**Limites des modèles (1 pt).**
- **MEDAF** : il repose sur des hypothèses fortes (marchés efficients, investisseurs rationnels et diversifiés, horizon d'une seule période, un seul facteur de risque) ; le bêta n'est pas stable dans le temps et le portefeuille de marché n'est pas observable (critique de Roll). Pour NAVÉLIA, non cotée, aucun cours ne permet de mesurer un bêta : celui de 1,60 est transposé de sociétés cotées plus grandes et plus matures.
- **Modèle de Fama et French** : c'est un modèle empirique, qui constate des écarts de rentabilité sans en donner un fondement théorique incontesté ; les primes de taille et de valeur varient selon les périodes et les pays, et ont parfois été négatives pendant de longues années ; les sensibilités de NAVÉLIA sont transposées d'un portefeuille de sociétés cotées. D'autres facteurs ont été proposés depuis, par exemple le momentum (Carhart, 1997).
- **Limites communes pour une start-up** : les deux modèles mesurent la rentabilité exigée d'un titre coté et liquide par un investisseur diversifié ; ils ignorent l'illiquidité, le risque d'échec et la concentration du patrimoine des fondateurs, qui détiennent 37,17 % d'une seule société. En pratique, le prix de la série C se fixe par la négociation, à partir des multiples et du TRI visé par le fonds ; les modèles fournissent seulement un plancher de rentabilité exigée.

**Nouveau plan de bons de créateur (0,5 pt).** Après la création de 150 000 bons : 2 970 000 + 150 000 = 3 120 000 actions sur base entièrement diluée.

| Actionnaires | Actions | Après la série C | Après le nouveau plan |
|---|---:|---:|---:|
| Fondateurs | 1 104 000 | 37,17 % | **35,38 %** |
| Trois fonds (MARVENE, SOLENTE, BRÉCALDE) | 1 506 000 | 50,71 % | **48,27 %** |
| dont BRÉCALDE Growth II | 450 000 | 15,15 % | 14,42 % |
| Salariés et premier plan de bons | 360 000 | 12,12 % | 11,54 % |
| Nouveau plan de bons | 150 000 | — | 4,81 % |
| **Total** | **3 120 000** | | **100,00 %** |

Les fondateurs auront perdu au total 10,62 points depuis 46 % ; les trois fonds réunis repassent sous la moitié du capital sur base entièrement diluée. Mais tant que les bons ne sont pas exercés, ils gardent 52,84 % des droits de vote (1 506 000 / 2 850 000) : le nouveau plan ne rend pas le contrôle aux fondateurs. Le plan étant créé **après** l'opération, il dilue aussi le fonds ; s'il avait été compté dans la base pré-money, le prix par action aurait baissé et toute la dilution aurait pesé sur les actionnaires actuels.

**Stratégie de gestion du capital (1 pt).**
- **Augmentation de capital réservée** : elle permet de choisir l'investisseur et d'apporter 18,0 M€ de fonds propres sans endettement, alors que l'autofinancement est faible (EBITDA de 2,3 M€) et que les banques limitent leurs concours. Ce choix est conforme au financement hiérarchique de Myers et Majluf (1984), l'émission d'actions venant après l'autofinancement et la dette, épuisés ici. L'arrivée d'un nouveau fonds qui accepte un prix de 40 € sert aussi de signal sur la valeur de la société et atténue l'asymétrie d'information pour les futurs partenaires.
- **Plans de bons de créateur** : ils attirent et fidélisent les cadres, notamment aux États-Unis, sans décaissement. Ils alignent leurs intérêts sur ceux des actionnaires et réduisent les coûts d'agence (Jensen et Meckling, 1976). En contrepartie, ils diluent les actionnaires (4,81 % pour le nouveau plan).
- **Maîtrise de la dilution** :
  - lever auprès du fonds le seul montant nécessaire (18 M€ sur 25 M€) et financer le complément par des ressources qui ne diluent pas, étudiées séparément ;
  - prévoir une levée en deux tranches liées à des étapes du plan (mise en service de la deuxième ligne), la seconde à un prix plus élevé ;
  - négocier la valeur pré-money dans le haut de la fourchette ;
  - réserver une partie du nouveau plan aux dirigeants, sous condition de performance.
- **Demandes du fonds**, évoquées sans développement juridique :
  - le siège au comité stratégique et le droit d'information sont des outils de surveillance usuels, qui réduisent l'asymétrie d'information ;
  - la priorité de récupération de la mise protège le fonds si la société est cédée à bas prix : les fondateurs supportent alors l'essentiel de la perte ;
  - la protection contre une levée future à un prix inférieur à 40 € reporte sur les fondateurs le risque d'une valorisation en baisse au prochain tour ;
  - le droit de céder aux mêmes conditions que les fondateurs protège le fonds minoritaire en cas de changement de contrôle ;
  - l'engagement de rester quatre ans attache la valeur de la société à ses dirigeants.

**Recommandation (0,5 pt).** Toute recommandation cohérente est acceptée. Une réponse possible :
- **accepter la série C** au prix de 40 €. La valeur pré-money de 100,8 M€ est en haut de la fourchette des multiples. Elle valorise la participation des fondateurs à 44,2 M€ et finance la deuxième ligne d'assemblage sans endettement supplémentaire ;
- **limiter la dilution** :
  - ne pas lever plus de 18 M€ auprès du fonds ;
  - maintenir la création du nouveau plan après l'opération ;
  - en réserver une partie aux fondateurs, pour qu'ils restent au-dessus de 35 % ;
- **négocier les protections du fonds** :
  - limiter la priorité de récupération à la mise investie ;
  - encadrer la protection contre une baisse de prix ;
  - organiser la gouvernance pour que les trois fonds, majoritaires ensemble après l'opération, ne puissent pas décider sans les fondateurs des orientations stratégiques.

**Réponses tolérées** : pour 1.4-03, trois arguments liés au cas suffisent pour la totalité des points ; limites présentées sous forme de tableau ; recommandation de lever moins auprès du fonds et davantage par d'autres moyens, ou d'associer MARVENE et SOLENTE à la série C, si l'effet sur la dilution est expliqué ; calcul de la part des fondateurs sur 2 970 000 + 150 000 actions présenté sans le détail des fonds : 1.4-02 réduit de moitié.

**Erreurs fréquentes**
- Calculer la part des fondateurs après le nouveau plan sur 2 520 000 + 150 000 actions, en oubliant la série C.
- Confondre dilution du contrôle et perte de valeur : une émission au prix de la valeur ne réduit pas la richesse des fondateurs.
- Développer le régime juridique et fiscal des bons de créateur ou rédiger des clauses : c'est hors du champ de l'épreuve.
- `JUR-T02` — recommandation sans lien avec la répartition du capital calculée.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 64-65 | inducteurs de VGE et de VCP, échantillon de comparables, multiple moyen ou médian, choix selon la maturité, approche comparative et non normative | [V] | F03 § 0 et 3 ; `perimetre_ue2.yaml` |
| Programme UE 2, l. 521-528 | méthodes par les comparables : inducteurs de VGE (CA, EBITDA, EBIT) et de VCP (RN, RCAI), échantillons | [V] | F03 § 0 |
| Guide pédagogique DSCG, juillet 2026, p. 68 | gestion du capital : augmentation de capital, gestion de la dilution | [V] | F05 § 0 et 4 |
| Guide pédagogique DSCG, juillet 2026, p. 74-75 ; programme l. 580-582 | MEDAF et ses limites ; modèle à trois facteurs pour interpréter le risque d'un titre, sans estimation des facteurs | [V] | F02 § 0, 2 et 7 |
| Sharpe (1964) | MEDAF | [V contexte] | F10 § 2 |
| Fama et French (1993) | modèle à trois facteurs : marché, taille (SMB), valeur (HML) | [V programme 5.2] | F10 § 1 ; F02 § 7 |
| Critique de Roll ; Carhart (1997) | limites du MEDAF ; facteur momentum | [S] | F02 § 2 et 7 |
| Akerlof (1970) | asymétrie d'information entre fondateurs et investisseurs | [V programme 5.1] | F10 § 1 |
| Jensen et Meckling (1976) | coûts d'agence, alignement des intérêts des cadres | [V programme 2.1] | F10 § 3 |
| Myers et Majluf (1984) | financement hiérarchique | [V programme 7.2] | F10 § 3 |
| Taux sans risque 4 %, prime de risque du marché 5 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 |
| Primes SMB 3 % et HML 4 %, sensibilités, bêta de 1,60 | hypothèses d'énoncé, sans valeur de marché | — | annexe 1.4 |
