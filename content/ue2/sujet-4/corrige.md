# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Sujet d'entraînement complet n° 4

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue2/fiches/`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (investissement, emprunts, coût du capital, DCF, multiples, portefeuille, LBO, BPA, équilibre des bilans, couvertures, barème sur 50, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Valorisation et levée de fonds de série C | 17 | 1.1 à 1.4 | `exercices/ex10_levee_serie_c` |
| 2 – Financer la croissance hors du circuit bancaire | 17 | 2.1 à 2.5 | `exercices/ex11_financements_alternatifs` |
| 3 – Techniques internes et garanties du risque de change à l'export | 16 | 3.1 à 3.5 | `exercices/ex12_risque_change_export` |
| **Total** | **50** | | |

---

## DOSSIER 1 – VALORISATION ET LEVÉE DE FONDS DE SÉRIE C (17 points)

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

---

## DOSSIER 2 – FINANCER LA CROISSANCE HORS DU CIRCUIT BANCAIRE (17 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Réglementation bancaire et accès de NAVÉLIA au crédit | `2.2.b` Mettre en œuvre la déontologie, la conformité et l'organisation déontologique (réglementation bancaire : principes du comité de Bâle) | 3,5 |
| 2.2 Financement participatif en capital : comparaison de deux plateformes | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs | 5 |
| 2.3 Coût de la dette de croissance | `7.2.a` Comparer les sources de financement et notamment leurs coûts | 4 |
| 2.4 Fintechs, notation par algorithme, tokenisation | `5.4.a` ; `5.4.b` | 2 |
| 2.5 Recommandation d'un ensemble de financements | `7.2.c` Analyser les nouveaux outils de financement ; `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives | 2,5 |
| **Total** | | **17** |

Part du calcul : environ 6 points (2.2-01 à 2.2-03, 2.3-01 à 2.3-03, 2.5-03). Part de l'analyse : environ 11 points. Les questions 2.1, 2.4 et 2.5, entièrement rédigées, valent 8 points : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 2.1 Réglementation bancaire et accès de NAVÉLIA au crédit (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Principes de Bâle III et de sa finalisation : objectifs, exigences de fonds propres proportionnées au risque, exigences de liquidité, transposition européenne | 1 |
| 2.1-02 | Notation interne de NAVÉLIA (catégorie 7 sur 10) expliquée par les données du cas, et lien entre notation, fonds propres mobilisés par la banque et décision de crédit | 1 |
| 2.1-03 | Conséquences sur l'accès au crédit : refus, montant limité, garanties, durée, engagements | 0,5 |
| 2.1-04 | Conséquences sur le coût du crédit | 0,5 |
| 2.1-05 | Conséquences sur la stratégie de financement de NAVÉLIA | 0,5 |

**Principes de la réglementation bancaire (1 pt).** Le comité de Bâle, hébergé par la Banque des règlements internationaux, fixe des normes minimales pour les banques. Ces normes sont transposées par chaque juridiction. Les accords de Bâle III ont été adoptés à partir de 2010, en réponse à la crise financière de 2007-2009, pour rendre les banques plus solides. Leur finalisation date de décembre 2017. Dans l'Union européenne, elle est appliquée par le règlement CRR3, applicable depuis le 1er janvier 2025. Les principes à connaître sont les suivants.
- **Exigences de fonds propres** : une banque doit détenir un montant minimal de fonds propres, de meilleure qualité qu'avant la crise, **proportionné aux risques** de ses crédits. Plus un emprunteur est risqué, plus le crédit qui lui est consenti mobilise de fonds propres. S'y ajoutent des coussins de sécurité et un plafond d'endettement de la banque, non pondéré par le risque.
- **Exigences de liquidité** : la banque doit détenir assez d'actifs liquides pour résister à une crise de trente jours, et financer ses emplois longs par des ressources stables. Les crédits longs sont donc plus coûteux à porter.
- **Mesure du risque** : la banque mesure le risque de chaque emprunteur par une méthode standard ou par sa propre notation. La finalisation de 2017 limite l'écart entre les deux méthodes.
- **Trois piliers** : exigences minimales, surveillance prudentielle par le superviseur, discipline de marché par la publication d'informations.

**Notation interne et décision de la banque (1 pt).** La banque principale classe NAVÉLIA en catégorie 7 sur 10 (8 en 2025). Les raisons sont dans l'annexe 2.1 :
- la société est jeune (créée en 2019) ;
- elle n'a qu'un exercice d'EBITDA positif (2,3 M€ en 2026, contre − 1,1 M€ en 2025) et un résultat net faible (0,4 M€, après − 2,6 M€) ;
- elle n'a pas d'historique de remboursement long ;
- ses actifs à donner en garantie se limitent à ses équipements ;
- son BFR croît avec le chiffre d'affaires (+ 58 %).

Les points forts du dossier (croissance, trésorerie nette positive de 2,0 M€, fonds de capital-risque au capital) ne suffisent pas à compenser ce manque d'historique.

Pour la banque, un crédit long et sans garantie à une entreprise de catégorie 7 mobilise beaucoup de fonds propres réglementaires. Or ces fonds propres doivent être rémunérés au niveau exigé par ses actionnaires. Le crédit doit donc rapporter assez pour couvrir à la fois le risque de non-remboursement et ce coût des fonds propres, ce qui le rend peu rentable aux conditions de marché. La banque applique en outre des limites d'engagement par catégorie de risque, fixées par son comité des crédits. Pour NAVÉLIA, cette limite est atteinte.

**Accès au crédit (0,5 pt).** Le prêt de 7 M€ sur 7 ans est refusé. La banque principale propose seulement 1,5 M€ sur 5 ans. Ce prêt est garanti à 50 % par une garantie publique, ce qui réduit le risque retenu par la banque et donc les fonds propres qu'elle mobilise. Il est assorti d'un nantissement des équipements et d'un engagement de trésorerie minimale. La seconde banque se limite à un découvert d'un an. Les banques privilégient les crédits courts (découvert, affacturage), garantis par des actifs ou des créances : ils mobilisent moins de fonds propres et posent moins de problèmes de liquidité.

**Coût du crédit (0,5 pt).** Le taux intègre une marge qui reflète la notation : prime de risque de défaut, rémunération des fonds propres mobilisés, coût des ressources stables. S'y ajoutent des coûts indirects : commission de garantie publique, nantissements, engagements à respecter, information à fournir. Le prêt proposé coûte 5,20 % avant IS (annexe 2.3), soit 2,55 points de plus que l'Euribor 3 mois (2,65 %, annexe 2.3) ; cet écart est indicatif, car il compare un taux fixe à 5 ans à un taux à 3 mois et comprend donc aussi une prime de durée et le coût de la garantie. Une meilleure notation, après un ou deux exercices rentables, permettrait d'obtenir un taux plus bas et des montants plus élevés.

**Stratégie de financement (0,5 pt).**
- **Renforcer d'abord les fonds propres**, comme le fait la série C. Ils améliorent la notation et donc la capacité d'emprunt future.
- **Diversifier les financeurs hors des banques** (désintermédiation) : plateformes de financement participatif, fonds de dette de croissance, fintechs de prêt. Ces financeurs ne sont pas soumis aux mêmes exigences de fonds propres, mais demandent une rémunération plus élevée (question 2.3).
- **Utiliser les leviers qui réduisent le risque perçu par la banque** : garanties publiques, financements courts adossés à des actifs (affacturage des créances), financement d'équipements.
- **Préparer la relation bancaire** : information régulière (budget, tableau de bord), présentation des comptes de 2027, demande de révision de la notation. L'objectif est de revenir vers le crédit bancaire, moins cher, quand la rentabilité sera établie.

**Réponses tolérées** : présentation en tableau (règle prudentielle → effet pour la banque → conséquence pour NAVÉLIA) ; mention de la cotation de la Banque de France ou des agences de notation comme autres notations, sans détail technique ; mention de la sélection adverse et du rationnement du crédit (Akerlof, 1970) pour expliquer le refus, si elle est appliquée au cas.

**Erreurs fréquentes**
- `JUR-T12` — confondre les exigences de fonds propres **de la banque** avec les capitaux propres de NAVÉLIA, ou présenter Bâle III comme une règle qui s'impose aux entreprises.
- Calculer un ratio prudentiel ou une probabilité de défaut, ce que la question exclut ; citer des pourcentages réglementaires inexacts ou employer l'appellation informelle de la finalisation de Bâle III au lieu de son nom.
- `JUR-T13` — exposé général sur Bâle III sans les données de NAVÉLIA (catégorie 7, un seul EBITDA positif, garantie publique de 50 %, limite d'engagement atteinte).

---

### 2.2 Financement participatif en capital : comparaison de deux plateformes (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Frais supportés à l'émission, part dans le montant collecté et montant net levé, pour les deux plateformes | 1 |
| 2.2-02 | Actions émises ; parts du capital des nouveaux investisseurs et des fondateurs après l'opération (base entièrement diluée) | 1 |
| 2.2-03 | Montant net levé par action émise et lecture du prix (décote de CAPSELLE) | 0,5 |
| 2.2-04 | Gouvernance : investisseurs en direct ou regroupés dans une holding | 1 |
| 2.2-05 | Profil des investisseurs, effet de communication et rôle de la plateforme comme nouvel acteur | 0,5 |
| 2.2-06 | Choix argumenté d'une plateforme | 1 |

**Conventions rappelées** : frais à l'émission = commission de succès + frais fixes ; montant net = montant collecté − frais à l'émission ; frais annuels exclus ; base entièrement diluée avant l'offre retenue à 3 100 000 actions (valeur arrondie), dont 1 104 000 aux fondateurs ; montants en M€ à trois décimales ; pourcentages à deux décimales.

**Frais et montant net (1 pt).**

| | LIMARÉO | CAPSELLE |
|---|---:|---:|
| Actions offertes × prix | 70 000 × 45 € | 75 000 × 42 € |
| Montant collecté (M€) | 3,150 | 3,150 |
| Commission de succès (M€) | 6 % × 3,150 = 0,189 | 4 % × 3,150 = 0,126 |
| Frais fixes (M€) | 0,050 | 0,030 |
| **Frais à l'émission (M€)** | **0,239** | **0,156** |
| Part du montant collecté | **7,59 %** | **4,95 %** |
| **Montant net levé (M€)** | **2,911** | **2,994** |
| Frais annuels (pour mémoire) | 0,020 par an | aucun |

CAPSELLE coûte moins cher et procure 0,083 M€ de plus. Sur quatre ans, les frais annuels de LIMARÉO portent son coût total à 0,239 + 4 × 0,020 = 0,319 M€.

**Actions émises et dilution (1 pt).**

| Base entièrement diluée | Avant l'offre | Après LIMARÉO | Après CAPSELLE |
|---|---:|---:|---:|
| Fondateurs (actions) | 1 104 000 | 1 104 000 | 1 104 000 |
| Autres actionnaires et bons | 1 996 000 | 1 996 000 | 1 996 000 |
| Nouveaux investisseurs | – | **70 000** | **75 000** |
| **Total** | **3 100 000** | **3 170 000** | **3 175 000** |
| Part des fondateurs | 35,61 % | **34,83 %** | **34,77 %** |
| Part des nouveaux investisseurs (taux de dilution) | – | **2,21 %** | **2,36 %** |

Les fondateurs perdent 0,79 point avec LIMARÉO et 0,84 point avec CAPSELLE. La dilution est faible dans les deux cas : 3,15 M€ représentent environ 2 % d'une société valorisée 130 à 140 M€ avant l'opération (42 € ou 45 € × 3 100 000 actions). Le contrôle n'est pas en jeu.

**Montant net par action émise (0,5 pt).** LIMARÉO : 2 911 000 / 70 000 = **41,59 €** ; CAPSELLE : 2 994 000 / 75 000 = **39,92 €**. Malgré des frais plus élevés, LIMARÉO procure plus de trésorerie par action cédée, parce que ses investisseurs paient un prix plus élevé. La décote de 3 € demandée par le club de CAPSELLE représente, au prix de LIMARÉO, un manque à gagner de 75 000 × 3 = 0,225 M€ pour les actionnaires existants. C'est plus que l'économie de frais à l'émission (0,083 M€). CAPSELLE est moins chère en frais, mais plus chère en dilution.

**Gouvernance (1 pt).**
- **LIMARÉO (en direct)** : environ 2 500 nouveaux actionnaires, chacun avec ses droits de vote et son droit à l'information.
  - Il faut convoquer et faire voter un actionnariat dispersé et l'informer régulièrement, d'où les frais annuels de 20 k€.
  - Les fonds de capital-risque, qui préparent des levées futures et une sortie, se méfient d'un capital éclaté (annexe 2.4) : chaque opération future (nouvelle levée, cession) suppose de réunir ces actionnaires.
  - L'engagement de céder aux mêmes conditions en cas de vente du contrôle limite ce risque à la sortie, mais ne règle pas la gestion courante.
  - Le poids de ces investisseurs (2,21 %) ne menace pas le contrôle.
- **CAPSELLE (holding)** : un seul nouvel actionnaire, la holding, qui vote pour tous les investisseurs. La table de capital reste simple, ce qui facilite les levées futures et la sortie.
  - En contrepartie, CAPSELLE obtient un siège d'observateur au comité stratégique, ce qui ajoute un interlocuteur et un droit d'information.
  - Le représentant de la holding peut défendre les intérêts des investisseurs du club plutôt que ceux de la société, ce qui crée un coût d'agence supplémentaire.

**Profil des investisseurs, communication et rôle de la plateforme (0,5 pt).**
- **LIMARÉO** réunit des particuliers, dont beaucoup de plaisanciers et d'habitants de la façade atlantique. Ce sont des **clients potentiels et des ambassadeurs de la marque**. La campagne publique (vidéo, réunions à Saint-Nazaire et à La Rochelle) a une valeur commerciale et rend l'entreprise visible. En revanche :
  - ces investisseurs, souvent non professionnels, connaissent mal le risque d'une start-up ;
  - ils n'apporteront pas de fonds à nouveau en cas de difficulté ;
  - leur déception éventuelle exposerait la réputation de NAVÉLIA ;
  - l'opération est **incertaine** : elle est annulée si moins de 2,0 M€ sont collectés.
- **CAPSELLE** réunit des investisseurs avertis, dont d'anciens cadres de l'industrie nautique. Ils apportent un **réseau et une expertise** et analysent le risque. L'opération est plus sûre : 2,0 M€ d'intentions sont déjà reçues et la campagne est plus courte. L'effet de communication est en revanche faible, puisque la campagne est réservée aux membres du club.
- **Rôle de la plateforme**, nouvel acteur du financement (`JUR-M02`) :
  - elle réunit l'épargne de nombreux investisseurs autour d'un projet sans banque intermédiaire, et elle est agréée par l'AMF comme prestataire de services de financement participatif ;
  - elle **sélectionne** les projets, documente l'offre et réduit ainsi l'asymétrie d'information entre la société et des investisseurs dispersés ;
  - elle **organise** la souscription et parfois la liquidité (tableau d'annonces de LIMARÉO).
  Le cadre européen limite toutefois ces offres à 5 M€ sur douze mois : le financement participatif ne peut couvrir seul les 7 M€.

**Choix argumenté (1 pt).** Toute conclusion cohérente avec les calculs et les critères est acceptée. Une réponse possible : retenir **LIMARÉO**.
- Le prix est plus élevé : 41,59 € nets par action contre 39,92 €, et le transfert de valeur de 0,225 M€ lié à la décote de CAPSELLE est évité.
- L'effet de communication est utile à une marque qui vend à des plaisanciers.
- La dilution est un peu plus faible (2,21 % contre 2,36 %).

Ce choix est assorti de trois conditions :
- informer les fonds actionnaires et obtenir leur accord sur l'actionnariat dispersé ;
- prévoir le recours à CAPSELLE si la campagne n'atteint pas le seuil de 2,0 M€ ;
- intégrer les 20 k€ annuels au budget.

À l'inverse, **CAPSELLE** se défend si NAVÉLIA privilégie la certitude du financement, la simplicité de la table de capital avant les prochaines levées et l'apport d'investisseurs expérimentés.

**Réponses tolérées** : calcul de la dilution sur les seules actions existantes, hors bons, ou sur une autre base, si l'hypothèse est écrite et appliquée aux deux plateformes ; perte des fondateurs obtenue par différence des pourcentages arrondis (0,78 point avec LIMARÉO, 0,84 point avec CAPSELLE) ; candidat qui rapproche les prix de 45 € et 42 € du prix de la série C (dossier 1) et en conclut que les deux offres se font avec une prime : raisonnement accepté, la valeur de 0,225 M€ s'entendant alors comme un manque à gagner par rapport à LIMARÉO ; frais annuels intégrés au coût comparé (sur quatre ans ou actualisés), si la convention est écrite ; choix de CAPSELLE argumenté.

**Erreurs fréquentes**
- `JUR-I06` — comparer les plateformes sur les seules commissions, sans la dilution, la gouvernance ni le profil des investisseurs.
- Oublier que le montant net, et non le montant collecté, finance le besoin ; ou calculer le nombre d'actions sur le montant net.
- Négliger l'écart de prix : le coût d'une levée en capital comprend la valeur cédée aux nouveaux investisseurs, pas seulement les frais.
- `JUR-M02` — présenter la plateforme comme une banque, qui prêterait ou souscrirait pour son propre compte.

---

### 2.3 Coût de la dette de croissance (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Tableau d'amortissement (amortissement constant de 1,000 M€) et flux avant IS : montant reçu net de frais et de la valeur des bons (3,680) | 1 |
| 2.3-02 | Flux après IS : économies d'IS sur les intérêts et sur les frais étalés (0,005 M€ par an) | 0,5 |
| 2.3-03 | Coûts actuariels : avant IS sans bons 10,98 % (0,5) ; avant IS bons compris 14,13 % (0,5) ; après IS bons compris 11,25 % (0,5) | 1,5 |
| 2.3-04 | Comparaison avec le prêt de référence (5,20 % et 3,90 %) et limites | 1 |

**Conventions rappelées** : flux annuels en fin d'année ; date 0 = versement ; point de vue de l'emprunteur ; IS 25 %, économie d'IS à la fin de l'année de la charge, NAVÉLIA supposée imposable dès 2027 ; frais d'arrangement de 0,080 M€ déduits par quarts ; valeur des bons (0,24 M€) retranchée du montant reçu, sans effet fiscal ; flux en M€ à trois décimales ; taux à deux décimales.

**Tableau d'amortissement et flux avant IS (1 pt).** L'amortissement constant est de 4,0 / 4 = 1,000 M€ par an, et les intérêts sont égaux à 10 % du capital restant dû.

| Année | Capital début | Intérêts (10 %) | Amortissement | Échéance | Capital fin |
|---:|---:|---:|---:|---:|---:|
| 1 | 4,000 | 0,400 | 1,000 | 1,400 | 3,000 |
| 2 | 3,000 | 0,300 | 1,000 | 1,300 | 2,000 |
| 3 | 2,000 | 0,200 | 1,000 | 1,200 | 1,000 |
| 4 | 1,000 | 0,100 | 1,000 | 1,100 | 0,000 |
| **Total** | | **1,000** | **4,000** | **5,000** | |

Montant reçu à la date 0 : 4,000 − 0,080 de frais = 3,920 M€ hors bons ; 3,920 − 0,240 = **3,680 M€** bons compris.

**Flux après IS (0,5 pt).** Chaque année, il faut retrancher de l'échéance l'économie d'IS sur les intérêts (25 % × intérêts) et sur les frais (25 % × 0,080 / 4 = 0,005).

| Année | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| Flux avant IS, hors bons | 3,920 | −1,400 | −1,300 | −1,200 | −1,100 |
| Flux avant IS, bons compris | **3,680** | −1,400 | −1,300 | −1,200 | −1,100 |
| Économie d'IS sur intérêts | | 0,100 | 0,075 | 0,050 | 0,025 |
| Économie d'IS sur frais | | 0,005 | 0,005 | 0,005 | 0,005 |
| **Flux après IS, bons compris** | **3,680** | **−1,295** | **−1,220** | **−1,145** | **−1,070** |

**Coûts actuariels (1,5 pt).** Le coût actuariel est le taux qui annule la valeur actuelle des flux.
- **Avant IS, hors bons** : à 10 %, la valeur actuelle des échéances est exactement de 4,000 (le taux nominal), d'où un écart de 3,920 − 4,000 = − 0,080. À 11 %, l'écart est de + 0,002. Par interpolation, **t = 10,98 %** : les frais de 2 % ajoutent près d'un point au taux nominal sur une durée courte.
- **Avant IS, bons compris** : à 14 %, l'écart est de − 0,010 ; à 15 %, de + 0,062. Par interpolation linéaire, t ≈ 14,14 % ; le taux exact, obtenu à la calculatrice, est de **14,13 %**. Les bons, qui valent 6 % du montant prêté, ajoutent plus de 3 points au coût.
- **Après IS, bons compris** : à 11 %, l'écart est de − 0,019 ; à 12 %, de + 0,056. Par interpolation, **t = 11,25 %**. Pour mémoire, hors bons, le coût après IS serait de 8,24 % (non demandé).

**Comparaison et limites (1 pt).**

| Financement | Montant | Coût avant IS | Coût après IS |
|---|---:|---:|---:|
| Prêt bancaire de référence (garanti à 50 %) | 1,5 M€ | 5,20 % | 3,90 % |
| Dette de croissance KORVANE, bons compris | 4,0 M€ | 14,13 % | **11,25 %** |

La dette de croissance coûte presque trois fois plus que le prêt de référence : 7,35 points de plus après IS. Ce surcoût rémunère un risque que la banque refuse de porter. Le fonds prête davantage, sans garantie publique ni garantie personnelle des fondateurs, et décide en trois semaines. Les bons lui donnent une part de la hausse de valeur de la société. La comparaison a toutefois des limites.
- **Les montants ne sont pas comparables** : la banque ne prête que 1,5 M€. La vraie alternative à la dette de croissance n'est pas le prêt bancaire, mais un supplément de fonds propres, plus coûteux (rentabilité exigée par les fonds de capital-risque) et plus dilutif.
- **Le coût des bons est incertain et supporté par les actionnaires**, pas par la trésorerie. Les 0,24 M€ sont une estimation : si la société réussit, les 12 000 bons, soit 0,39 % de la base diluée, coûteront plus aux actionnaires ; si elle échoue, ils ne coûteront rien.
- **L'économie d'IS est hypothétique** : NAVÉLIA dispose encore de déficits reportables. Tant qu'elle les impute, les intérêts n'économisent pas d'impôt immédiatement. Le coût réel se rapproche alors du coût avant IS : 14,13 % contre 5,20 % pour le prêt de référence.
- **Les profils diffèrent** : remboursement rapide sur 4 ans (1,4 M€ la première année) contre 5 ans pour le prêt bancaire ; nantissement des marques et brevets, actifs essentiels de la société ; trésorerie minimale de 2 M€ dans les deux cas.
- **Les flux sont annuels par convention**, alors que ce type de dette se rembourse en général par mensualités : le coût réel serait un peu plus élevé.

**Réponses tolérées** : taux obtenus par interpolation, quelles que soient les bornes, ou à la calculatrice (écart de 0,05 point au plus avec le taux exact) ; frais déduits fiscalement en totalité la première année (coût après IS d'environ 11,21 %), si l'hypothèse est écrite : l'item 2.3-02 n'est pas accordé, l'item 2.3-03 est noté en cohérence ; valeur des bons répartie sur la durée au lieu d'être retranchée à la date 0, si la convention est écrite et le résultat cohérent ; coût après IS obtenu par 14,13 % × 0,75 = 10,60 % : approximation non actuarielle, qui applique à tort l'économie d'IS à la valeur des bons ; le demi-point « après IS » n'est pas accordé.

**Erreurs fréquentes**
- `JUR-T04` — tableau d'amortissement constant confondu avec un tableau à annuités constantes (échéance de 1,262 M€), ou intérêts calculés sur le capital initial chaque année.
- Ajouter la valeur des bons aux décaissements de l'année 4 ou la considérer comme déductible.
- Oublier les frais d'arrangement dans le montant reçu (coût avant IS de 10,00 % hors bons).
- `JUR-T13` — conclure sur le seul taux (« la dette de croissance est trop chère ») sans voir qu'aucun financement bancaire de 4 M€ n'est disponible.

---

### 2.4 Fintechs, notation par algorithme, tokenisation (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Rôle des fintechs et de la notation par algorithme et intelligence artificielle dans l'octroi de crédit : apports | 0,5 |
| 2.4-02 | Limites de la notation par algorithme : biais, opacité, données, encadrement | 0,5 |
| 2.4-03 | Plateformes et tokenisation des titres : principe, apports, limites | 0,5 |
| 2.4-04 | Conclusion appliquée à NAVÉLIA | 0,5 |

**Notation par algorithme : apports (0,5 pt).** Les fintechs sont de jeunes entreprises qui utilisent le numérique pour offrir des services financiers : paiement, prêt, gestion de trésorerie. Leur arrivée réduit en partie le rôle des intermédiaires traditionnels. Les prêteurs en ligne analysent, avec l'accord du dirigeant, des données en temps réel (comptes bancaires, factures, commandes, paiements), là où la notation bancaire classique repose sur les derniers comptes annuels. Un modèle d'intelligence artificielle en déduit une note de risque et une décision rapide (quarante-huit heures, annexe 2.4). Pour une entreprise jeune, dont les comptes reflètent mal la dynamique, ces données peuvent **réduire l'asymétrie d'information** et ouvrir l'accès au crédit. NAVÉLIA, en forte croissance avec un carnet de commandes, en profiterait.

**Limites (0,5 pt).**
- **Biais** : un modèle appris sur des entreprises différentes, par exemple des commerces en ligne, juge mal une start-up industrielle.
- **Opacité** : une note qu'on ne peut ni expliquer ni contester (« boîte noire ») pose des questions de responsabilité et de loyauté.
- **Données** : confidentialité et cybersécurité des données bancaires transmises ; risque de comportements identiques entre prêteurs qui utilisent des modèles proches.
- **Encadrement** : un règlement européen encadre désormais l'usage de l'intelligence artificielle ; les prêteurs restent soumis à la conformité, dont la lutte contre le blanchiment.
- **Coût et montants** : ces prêts sont plus chers que le crédit bancaire et portent rarement sur plus de quelques centaines de milliers d'euros. Ils servent surtout au financement court (BFR, créances).

**Plateformes et tokenisation (0,5 pt).** Les plateformes de financement participatif, en capital ou en prêt, mettent en relation directe entreprises et épargnants (question 2.2). La **tokenisation** consiste à émettre des actions ou des obligations sous forme de jetons inscrits sur une chaîne de blocs, registre partagé et infalsifiable, dans le cadre du régime pilote européen. Elle promet :
- des titres fractionnables ;
- un règlement plus rapide et moins coûteux, sans intermédiaire central ;
- à terme, un marché secondaire qui rendrait liquides les titres d'une société non cotée.

Pour l'instant, la liquidité reste théorique (échanges très rares). Les coûts juridiques et techniques sont élevés pour une première émission, l'encadrement est expérimental, et des risques s'y ajoutent : cybersécurité, conservation des jetons, protection des investisseurs.

**Conclusion pour NAVÉLIA (0,5 pt).**
- Les fintechs de prêt peuvent financer une partie du **besoin en fonds de roulement** (5 M€ du besoin 2027), en complément de l'affacturage bancaire. Elles ne financent pas une ligne d'assemblage de 14 M€.
- La notation par algorithme est un complément, non un substitut, à la relation bancaire et aux fonds propres.
- La tokenisation n'est pas adaptée aujourd'hui : son coût, l'absence de marché secondaire et la méfiance des fonds actionnaires l'écartent. Elle pourrait servir plus tard à rendre liquides les titres des salariés ou des investisseurs participatifs.

**Réponses tolérées** : mention des néo-bourses, des crypto-actifs ou du trading à haute fréquence comme autres innovations, si la réponse reste centrée sur le financement de NAVÉLIA ; lecture de la notation par algorithme comme réponse à la sélection adverse (Akerlof, 1970).

**Erreurs fréquentes**
- `JUR-T13` — exposé technique sur l'intelligence artificielle ou la chaîne de blocs sans lien avec le besoin de NAVÉLIA.
- Confondre la tokenisation de titres financiers et l'émission de crypto-actifs.
- `JUR-M02` — présenter les fintechs comme une solution miracle, sans leurs coûts ni leurs limites.

---

### 2.5 Recommandation d'un ensemble de financements (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Théorie du choix de financement présentée et appliquée au cas : financement hiérarchique (Myers et Majluf, 1984) ou théorie du compromis (Myers, 1977) | 1 |
| 2.5-02 | Caractéristiques des outils mobilisés : conditions d'accès, avantages, limites, coûts | 0,5 |
| 2.5-03 | Ensemble chiffré couvrant les 7 M€ | 0,5 |
| 2.5-04 | Conditions à négocier et conclusion | 0,5 |

**Théorie (1 pt).** Selon le **financement hiérarchique** (Myers et Majluf, 1984), l'asymétrie d'information conduit l'entreprise à préférer l'autofinancement, puis la dette, et en dernier lieu l'émission d'actions, que les investisseurs extérieurs interprètent comme le signe d'une surévaluation. NAVÉLIA ne peut pas suivre cet ordre :
- son autofinancement est faible (EBITDA de 2,3 M€ pour un besoin de 25 M€) ;
- les banques, mal informées sur une entreprise sans historique, rationnent la dette.

La société a donc d'abord émis des actions (série C) auprès d'investisseurs **spécialisés et informés**, pour qui le signal négatif joue peu. Elle complète par les financements accessibles les moins dilutifs. La hiérarchie s'applique aux financements extérieurs encore disponibles : dette d'abord, puis capital pour la part que la dette ne couvre pas.

La **théorie du compromis** (Myers, 1977) apporte la limite. Une dette supplémentaire apporte une économie d'impôt, mais cette économie est faible ici, puisque la société dispose de déficits reportables. Elle crée en outre des coûts de difficultés financières, élevés pour une start-up : remboursements de 1,4 M€ dès 2028, nantissement des brevets, trésorerie minimale. L'endettement doit donc rester modéré : environ 10,5 M€ de dettes après l'opération (5,0 + 4,0 + 1,5), à rapprocher de capitaux propres renforcés par la série C.

**Caractéristiques des outils (0,5 pt).**

| Outil | Accès et conditions | Avantages | Limites et coût |
|---|---|---|---|
| Prêt bancaire garanti | 1,5 M€, garantie publique de 50 %, nantissement, trésorerie minimale | coût le plus bas (3,90 % après IS) ; relation bancaire entretenue | montant limité ; engagements |
| Dette de croissance | 4,0 M€ en trois semaines, sans garantie personnelle | non dilutive, sauf les bons (0,39 %) ; rapide | 11,25 % après IS, 14,13 % avant ; remboursement sur 4 ans ; nantissement des brevets |
| Financement participatif en capital | jusqu'à 5 M€ sur douze mois ; 3,15 M€ proposés | fonds propres sans remboursement ; communauté et communication | frais de 7,59 % (LIMARÉO) ; dilution de 2,21 % ; actionnariat dispersé ; risque d'échec de la campagne |
| Fintechs de prêt, affacturage | financement du BFR | rapidité, adossé aux créances | coût élevé, montants faibles, courte durée |

**Ensemble chiffré (0,5 pt).** Une réponse possible, en montants nets (M€) :

| Ressource | Montant net |
|---|---:|
| Financement participatif LIMARÉO (3,150 collectés − 0,239 de frais) | 2,911 |
| Dette de croissance KORVANE (4,000 − 0,080 de frais) | 3,920 |
| Prêt bancaire garanti | 1,5 |
| **Total** | **8,331** |
| Besoin restant | 7,0 |
| **Marge de sécurité** | **1,331** |

La marge de 1,3 M€ protège la trésorerie minimale de 2 M€ exigée par la banque et par KORVANE, alors que le BFR (5 M€ prévus) peut dépasser les prévisions en cas de croissance plus forte. Sans le prêt bancaire, les deux premières ressources (6,831 M€) couvriraient à peine le besoin.

**Conditions à négocier et conclusion (0,5 pt).**
- **Avec KORVANE** : un différé d'amortissement d'un an, pour faire coïncider les remboursements avec la montée en charge de la deuxième ligne ; moins de bons ; un nantissement limité aux marques, sans les brevets ; le remboursement anticipé sans pénalité après une prochaine levée.
- **Avec la banque** : un montant porté à 2 M€ après la série C ; un réexamen de la notation sur les comptes de 2027.
- **Avec la plateforme** : l'accord préalable des fonds actionnaires ; un plan de repli vers CAPSELLE si la campagne échoue.

Cet ensemble finance la croissance sans nouvelle dilution significative des fondateurs. Il garde la dette dans des limites supportables et prépare le retour au crédit bancaire, moins cher, quand la rentabilité sera établie.

**Réponses tolérées** : ensemble sans prêt bancaire, ou avec CAPSELLE (montant net de 2,994 M€), ou réduisant la dette de croissance au profit de fonds propres, si les montants couvrent le besoin et si le choix est justifié par la théorie ; mobilisation de la théorie du signal (Ross, 1977) ou de l'asymétrie d'information (Akerlof, 1970) en complément, appliquée au cas ; mention d'un financement vert ou d'aides publiques à l'innovation (moteurs électriques) comme piste complémentaire.

**Erreurs fréquentes**
- `JUR-T14` — attribuer le financement hiérarchique à Modigliani et Miller, ou confondre l'ordre hiérarchique (sans ratio cible) et la théorie du compromis (ratio cible).
- `JUR-T02` — théorie récitée sans les chiffres du cas (EBITDA de 2,3 M€, coûts de 3,90 % et 11,25 %, dilution de 2,21 %).
- Additionner les montants collectés bruts au lieu des montants nets, ou proposer de lever plus de 5 M€ sur une plateforme.
- `JUR-M01` — recommandation sans aucune référence théorique.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 2, partie 2.2 ; guide pédagogique DSCG, juillet 2026, p. 61 | principes du comité de Bâle, sans aucun ratio à calculer ; conséquences sur la disponibilité et le coût du crédit ; influence de la notation | [V] | F09 § 0 et 2.2 ; `perimetre_ue2.yaml` (2.2.b) |
| Comité de Bâle, Bâle III (2010), finalisation du 7 décembre 2017 | exigences de fonds propres et de liquidité, encadrement des modèles internes | [V pour les dates ; S pour les mécanismes] | F09 § 2.1 |
| Règlement (UE) 2024/1623 « CRR3 », art. 2 | applicable à partir du 1er janvier 2025 | [V] | F09 § 2.1 |
| Règlement (UE) 2020/1503, art. 1, 12 et 51 | prestataires de services de financement participatif agréés ; offres jusqu'à 5 000 000 EUR sur douze mois ; applicable depuis le 10 novembre 2021 ; agrément par l'AMF en France | [V ; S pour l'AMF] | fiche commune Sapin II, LCB-FT et MiCA § 3.5 ; F06 § 6 |
| Programme UE 2, partie 5.4 (l. 599-604) ; sujet 2025, dossier 3 ; rapport du jury 2025 | fintechs, plateformes, intelligence artificielle, chaîne de blocs ; comparaison de plateformes (coût, gouvernance, profil des investisseurs) | [V programme ; S sujet 2025] | F06 § 6 ; `JUR-I06`, `JUR-M02` |
| Régime pilote européen des infrastructures de marché DLT (règlement (UE) 2022/858) | tokenisation de titres financiers | [S] | F06 § 6 |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle | encadrement de l'IA, cité sans détail | [S] | F06 § 6 |
| Myers et Majluf (1984) | financement hiérarchique | [V programme 7.2] | F10 § 3 |
| Myers (1977) | théorie du compromis (attribution du programme) | [V programme 7.2] | F10 § 3 |
| Akerlof (1970) | asymétrie d'information, sélection adverse, rationnement du crédit | [V programme 5.1] | F10 § 1 |
| Formules du tableau d'amortissement et du taux actuariel | coût de la dette de croissance | [S] | F01 ; F02 |
| Euribor 3 mois 2,65 % (annexe 2.3) | repère du coût du prêt bancaire | hypothèse d'énoncé plausible fin 2026 (moyenne de septembre 2026 : 2,635 % [V]) | F11 § 1 |

---

## DOSSIER 3 – TECHNIQUES INTERNES ET GARANTIES DU RISQUE DE CHANGE À L'EXPORT (16 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Position de change du deuxième trimestre 2027 | `6.3.a` Caractériser la position de change courte ou longue, ouverte ou fermée | 2,5 |
| 3.2 Techniques internes : devise de facturation, termaillage, clause d'indexation, compensation | `6.3.c` Maîtriser les techniques internes et les garanties externes | 4 |
| 3.3 Avance en devises et vente à terme de la créance en livres | `6.3.c` Maîtriser les techniques internes et les garanties externes ; `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) | 5 |
| 3.4 Garanties publiques à l'export : assurance prospection et assurance change | `6.3.c` Maîtriser les techniques internes et les garanties externes | 2,5 |
| 3.5 Stratégie de couverture recommandée | `6.3.c` Maîtriser les techniques internes et les garanties externes | 2 |
| **Total** | | **16** |

Part du calcul : environ 8,5 points (3.1-01, 3.1-02, 3.1-04, 3.2-02, 3.2-03, 3.2-05, 3.3-01 à 3.3-07, 3.4-02, 3.4-03). Part de l'analyse : environ 7,5 points. Les questions 3.4 et 3.5 et les items d'analyse des autres questions ne doivent pas être sacrifiés faute de temps : ce dossier est le dernier de l'épreuve (`JUR-T15`).

---

### 3.1 Position de change du deuxième trimestre 2027 (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Positions par devise et par échéance (créances − dettes) et positions du trimestre : + 2 400 000 USD et + 700 000 GBP | 1 |
| 3.1-02 | Contre-valeurs au comptant du 1er avril : 2 142 857 € et 813 953 € | 0,5 |
| 3.1-03 | Qualification : deux positions longues et ouvertes ; risque de dépréciation du dollar et de la livre, c'est-à-dire de hausse des cours EUR/USD et EUR/GBP cotés au certain | 0,5 |
| 3.1-04 | Perte dans le scénario défavorable : 55 901 € sur le dollar, 27 437 € sur la livre, 83 337 € au total | 0,5 |

**Positions (1 pt).** La position de change d'une devise est la différence entre les avoirs et créances et les dettes et engagements dans cette devise, par échéance. Le contrat TARNMOUTH, encore en négociation, n'est pas une créance : il n'entre pas dans la position du trimestre (il crée un risque sur offre, étudié aux questions 3.2 et 3.4).

| Position (devise) | 30 avril | 31 mai | 30 juin | Trimestre |
|---|---:|---:|---:|---:|
| Créances USD | 1 400 000 | 1 500 000 | 1 600 000 | 4 500 000 |
| Dettes USD | — | − 1 200 000 | − 900 000 | − 2 100 000 |
| **Position USD** | **+ 1 400 000** | **+ 300 000** | **+ 700 000** | **+ 2 400 000** |
| Créances GBP | — | 250 000 | 600 000 | 850 000 |
| Dettes GBP | — | − 150 000 | — | − 150 000 |
| **Position GBP** | — | **+ 100 000** | **+ 600 000** | **+ 700 000** |

**Contre-valeurs (0,5 pt).** Au certain, montant en euros = montant en devise / cours. Dollar : 2 400 000 / 1,12 = **2 142 857 €** (1 250 000 € en avril, 267 857 € en mai, 625 000 € en juin). Livre : 700 000 / 0,86 = **813 953 €** (116 279 € en mai, 697 674 € en juin). L'exposition du trimestre représente près de 3 M€, soit plus que l'EBITDA de 2026 (2,3 M€).

**Qualification (0,5 pt).** Les deux positions sont **longues** (créances supérieures aux dettes) et **ouvertes** (non couvertes, non compensées) à chaque échéance où elles ne sont pas nulles. NAVÉLIA SAS craint la **dépréciation** du dollar et de la livre : au certain, une **hausse** du cours (1 EUR = 1,15 USD au lieu de 1,12) signifie qu'un euro coûte plus de dollars, donc que chaque dollar encaissé rapporte moins d'euros. Le risque est un risque de transaction, sur des flux certains et datés. Les dettes envers KESTAVO ferment déjà une partie de la position en dollars (2,1 M USD sur 4,5 M USD de créances), mais seulement si les dollars encaissés servent à les payer, ce qui n'est pas le cas aujourd'hui (conversion systématique au comptant).

**Scénario défavorable (0,5 pt).**
- Dollar : 2 400 000 / 1,15 = 2 086 957 € ; perte = 2 142 857 − 2 086 957 = **55 901 €** (calcul direct : 2 400 000 / 1,12 − 2 400 000 / 1,15).
- Livre : 700 000 / 0,89 = 786 517 € ; perte = 813 953 − 786 517 = **27 437 €**.
- Total : **83 337 €** (83 338 € en additionnant les montants arrondis, accepté) sur un seul trimestre, soit 3,6 % de l'EBITDA de 2026 : un montant significatif pour une société qui vient d'atteindre l'équilibre et prépare une levée de fonds.

**Réponses tolérées** : position présentée en cumul au fil du trimestre ; contre-valeurs arrondies au k€ ; perte calculée sur les seules positions de fin de période, si l'hypothèse est écrite ; risque exprimé à l'incertain (le dollar passe de 0,8929 € à 0,8696 €), si la cotation est précisée.

**Erreurs fréquentes**
- Qualifier de courte la position d'un exportateur, ou dire qu'il craint la hausse du cours sans préciser la cotation : au certain, la hausse du cours EUR/USD est une dépréciation du dollar, défavorable à l'exportateur.
- Ajouter le contrat TARNMOUTH, non signé, à la position du trimestre.
- `JUR-T03` — oublier les dettes en devises (KESTAVO, agent britannique) et raisonner sur les seules créances.
- `JUR-T07` — positions présentées en ligne, sans tableau par devise et par échéance.

---

### 3.2 Techniques internes (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Devise de facturation : l'euro transférerait le risque à la filiale sans le faire sortir du groupe ; imposer l'euro aux clients britanniques est un choix commercial risqué | 0,5 |
| 3.2-02 | Termaillage : 1 428 571 € encaissés le 1er avril contre 1 391 304 € le 30 juin au cours anticipé, soit un gain de change anticipé de 37 267 € | 0,5 |
| 3.2-03 | Coût de portage pour le groupe (16 000 USD d'intérêts perdus, 8 571 € d'intérêts gagnés) et effet net : + 31 925 € si le dollar baisse à 1,15, − 5 714 € si le cours reste à 1,12 | 0,5 |
| 3.2-04 | Autres possibilités de termaillage (retarder KESTAVO, accélérer les clients britanniques) et limites, dont le caractère spéculatif | 0,5 |
| 3.2-05 | Clause d'indexation : variations, prix révisés (528 900, 503 100 et 516 000 GBP) et euros encaissés avec et sans clause (585 714 / 571 429 ; 615 789 / 631 579 ; 594 059) | 1 |
| 3.2-06 | Appréciation de la clause pour NAVÉLIA et pour TARNMOUTH | 0,5 |
| 3.2-07 | Compensation des flux en dollars (compte en USD) et netting avec la filiale : apport limité | 0,5 |

**Devise de facturation (0,5 pt).**
- **NAVÉLIA Inc.** : facturer la filiale en euros supprimerait le risque de NAVÉLIA SAS mais le transférerait à NAVÉLIA Inc., qui revend en dollars : le risque resterait entier au niveau du groupe, détenu à 100 %, et se retrouverait dans une filiale de distribution sans compétence de trésorerie. Il est plus efficace de le concentrer chez NAVÉLIA SAS, qui traite avec la banque et peut compenser les dollars reçus avec ses achats en dollars.
- **Clients britanniques** : TARNMOUTH exige la livre et les concurrents locaux facturent en livres ; imposer l'euro ferait porter le risque au client et pourrait coûter des contrats sur un marché qui représente 9 % du chiffre d'affaires. La clause d'indexation est un compromis : la devise reste la livre, le risque est partagé.

**Termaillage avec la filiale : calcul (0,5 + 0,5 pt).** Le termaillage consiste à avancer (*leads*) ou retarder (*lags*) les règlements en devises selon l'évolution anticipée des cours. Le dollar étant anticipé en baisse, NAVÉLIA SAS a intérêt à encaisser ses dollars le plus tôt possible.
- Facture de 1 600 000 USD réglée le 1er avril : 1 600 000 / 1,12 = **1 428 571 €** ; réglée le 30 juin au cours anticipé : 1 600 000 / 1,15 = **1 391 304 €** ; gain de change anticipé : **37 267 €**.
- Coût de portage pour le groupe : NAVÉLIA Inc. prélève les dollars sur sa trésorerie placée à 4,00 % et perd 1 600 000 × 4,00 % × 90 / 360 = **16 000 USD** d'intérêts, soit 13 913 € au cours de 1,15 (14 286 € au cours de 1,12) ; NAVÉLIA SAS place les euros à 2,40 % et gagne 1 428 571 × 2,40 % × 90 / 360 = **8 571 €**.

| Effet pour le groupe (€) | Dollar à 1,15 le 30 juin | Cours inchangé à 1,12 |
|---|---:|---:|
| Gain de change | + 37 267 | 0 |
| Intérêts perdus par NAVÉLIA Inc. | − 13 913 | − 14 286 |
| Intérêts gagnés par NAVÉLIA SAS | + 8 571 | + 8 571 |
| **Effet net** | **+ 31 925** | **− 5 714** |

Le règlement anticipé n'est gagnant que si le cours du 30 juin dépasse environ 1,1245, valeur proche du cours à terme du dollar à 3 mois (1,1238 par la parité des taux) : l'écart de taux entre le dollar (4 %) et l'euro est le prix de l'anticipation, comme il est celui d'une vente à terme.

**Autres possibilités et limites (0,5 pt).**
- **Retarder le paiement de KESTAVO** (*lags* sur une dette en dollars dont on anticipe la baisse) : exclu, les conditions du fournisseur prévoient des pénalités de retard et la suspension des livraisons de cellules, vitales pour la production.
- **Accélérer les règlements des clients britanniques** : aucun escompte n'est prévu ; il faudrait en accorder un, coûteux, et les prévisions sur la livre sont partagées, ce qui ne justifie pas d'anticiper.
- **Limites générales** : le termaillage n'est pas une couverture mais un pari sur l'évolution du cours ; si le dollar s'apprécie, l'anticipation fait perdre (le groupe aurait dû au contraire retarder le règlement de la filiale). Il est simple dans un groupe détenu à 100 % (décision interne, sans contrepartie à convaincre), mais il ponctionne la trésorerie de la filiale (2 000 000 USD avant l'opération, 400 000 USD après) au moment où elle finance le développement américain ; les règles de prix et de délais intragroupe ne sont pas développées ici.

**Clause d'indexation : calcul (1 pt).** Variation = (cours − 0,8600) / 0,8600 ; hors de la bande de ± 2 %, prix révisé = 516 000 × (1 + variation / 2) ; euros = prix / cours.

| Cours au 30/09/2027 | Variation | Révision du prix | Prix (GBP) | Euros avec clause | Euros sans clause | Effet de la clause |
|---|---:|---:|---:|---:|---:|---:|
| 0,9030 (livre dépréciée) | + 5,00 % | + 2,50 % | 528 900 | **585 714** | 571 429 | + 14 286 |
| 0,8170 (livre appréciée) | − 5,00 % | − 2,50 % | 503 100 | **615 789** | 631 579 | − 15 789 |
| 0,8686 | + 1,00 % | aucune (dans la bande) | 516 000 | **594 059** | 594 059 | 0 |

Au cours de référence, NAVÉLIA encaisserait 600 000 € (40 × 15 000 €). Avec la clause, la perte de change est ramenée de 28 571 € à 14 286 € si la livre se déprécie de 5 % ; en contrepartie, la société ne garde que la moitié du gain si elle s'apprécie.

**Appréciation de la clause (0,5 pt).**
- **Pour NAVÉLIA** : technique sans coût bancaire et simple à appliquer ; elle partage le risque mais ne le supprime pas : la société supporte seule les variations comprises dans la bande de ± 2 % (jusqu'à environ 11 800 € de perte sur ce contrat), puis la moitié de la variation totale dès que la bande est franchie ; cette discontinuité crée un effet de seuil (à + 2 %, aucun ajustement et 11 765 € de perte ; juste au-delà, le prix est relevé d'environ 1 % et la perte retombe vers 5 900 €), source de contestation sur le cours constaté. Elle abandonne la moitié des gains. La clause ne joue qu'à la livraison : pendant la validité de l'offre en livres (jusqu'au 31 mai), le risque reste entier.
- **Pour TARNMOUTH** : le client conserve un prix en livres, mais ce prix devient incertain (± 2,5 % dans les scénarios) ; il porte la moitié d'un risque qu'il n'avait pas, ce qui complique son budget et peut le conduire à refuser la clause ou à demander une remise. La symétrie de la clause (baisse du prix si la livre s'apprécie) la rend plus acceptable. Sa négociation dépend du rapport de force commercial.

**Compensation et netting (0,5 pt).**
- **Compensation des flux de même devise** : en conservant les dollars reçus de NAVÉLIA Inc. sur le compte en dollars pour payer KESTAVO, NAVÉLIA SAS ferme sans coût 2 100 000 USD de sa position (en mai et en juin), n'a plus à convertir que le solde (2 400 000 USD) et économise deux marges de change (vente puis rachat de dollars).
- **Netting** avec la filiale : il compense des dettes et créances réciproques pour ne régler que le solde. Ici, les flux vont dans un seul sens (la filiale paie les moteurs), il n'y a rien à compenser : le netting n'apporterait rien tant que NAVÉLIA Inc. ne facture pas de prestations à la société mère ; il est surtout utile dans les groupes comptant plusieurs filiales qui commercent entre elles.

**Réponses tolérées** : intérêts perdus par la filiale convertis au cours du jour (14 286 €) dans les deux scénarios (effet net de + 31 553 € si le dollar baisse) si la convention est écrite ; effet net à − 5 715 € (somme de montants arrondis) ; termaillage étudié sur une autre facture de la filiale avec un raisonnement identique ; clause appréciée à partir de l'écart en pourcentage plutôt qu'en euros ; effet de seuil de la clause aux bornes de la bande (valorisé en 3.2-06) ; mention de la théorie de l'agence (Jensen et Meckling, 1976) pour analyser la décision imposée à la filiale par la société mère.

**Erreurs fréquentes**
- Présenter le termaillage comme une couverture sans risque, ou oublier le coût de portage (intérêts perdus par la filiale).
- Retarder l'encaissement des dollars alors que la baisse du dollar est anticipée (sens inversé).
- Appliquer la révision au prix en euros, ou réviser le prix de la variation entière au lieu de la moitié ; réviser le prix dans la bande de ± 2 %.
- Croire que facturer la filiale en euros supprime le risque du groupe.
- `JUR-T13` — réciter les techniques internes sans les relier au cas (KESTAVO, trésorerie de la filiale, exigence de TARNMOUTH).

---

### 3.3 Avance en devises et vente à terme de la créance en livres (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Cours à terme 0,8629 et points de terme + 29 ; euro en report, livre en déport | 0,5 |
| 3.3-02 | Vente à terme : 695 330 € le 30 juin (697 674 € au comptant du jour) | 0,5 |
| 3.3-03 | Montant emprunté 593 178 GBP ; intérêts 6 822 GBP | 0,5 |
| 3.3-04 | Euros obtenus au comptant : 689 742 € | 0,5 |
| 3.3-05 | Hypothèse « placement » : intérêts 4 138 € ; valeur acquise 693 881 € | 0,5 |
| 3.3-06 | Hypothèse « crédit de trésorerie » : intérêts économisés 7 156 € ; valeur acquise 696 898 € | 0,5 |
| 3.3-07 | Cours à terme implicites de l'avance : 0,8647 et 0,8610 | 0,5 |
| 3.3-08 | Comparaison : vente à terme meilleure de 1 449 € si les euros sont placés ; avance meilleure de 1 569 € s'ils réduisent le crédit de trésorerie | 0,5 |
| 3.3-09 | Ce que l'avance apporte de plus (financement immédiat) et ses limites ; conclusion selon le plan de trésorerie | 0,5 |
| 3.3-10 | Pourquoi les résultats sont proches : les deux solutions fixent le cours ; le terme se déduit des taux d'intérêt (vente à terme = emprunt en livres + placement en euros), sans anticipation | 0,5 |

**Cours à terme (0,5 pt).** Par la parité des taux d'intérêt, en cotation au certain (1 EUR = x GBP) :
F = 0,8600 × (1 + 4,00 % × 90 / 360) / (1 + 2,65 % × 90 / 360) = 0,8600 × 1,01 / 1,006625 = 0,862883, soit **0,8629**.
Points de terme : 0,8629 − 0,8600 = **+ 29 points**. À terme, un euro vaut plus de livres qu'au comptant : l'**euro est en report** et la **livre en déport**. Ce n'est pas une prévision : la livre, dont le taux d'intérêt (4,00 %) dépasse celui de l'euro (2,65 % pour l'Euribor 3 mois), cote en déport pour qu'aucun arbitrage entre un placement en livres couvert à terme et un placement en euros ne soit possible.

**Vente à terme (0,5 pt).** Le 30 juin, NAVÉLIA livre les 600 000 GBP payés par ORMSBRIDGE et reçoit 600 000 / 0,8629 = **695 330 €**, quel que soit le cours du jour. Au comptant du 1er avril, la créance vaudrait 697 674 € : l'écart de 2 345 € est le déport, c'est-à-dire l'écart de taux sur 90 jours, et non une perte. Dans le scénario défavorable (0,89), la créance non couverte ne rapporterait que 674 157 €.

**Avance en devises (0,5 + 0,5 pt).** NAVÉLIA emprunte aujourd'hui les livres que la créance remboursera, intérêts compris, le 30 juin :
- montant emprunté = 600 000 / (1 + 4,60 % × 90 / 360) = 600 000 / 1,0115 = **593 178 GBP** ; intérêts = 600 000 − 593 178 = **6 822 GBP** ;
- livres vendues au comptant : 593 178,45 / 0,86 = **689 742 €** disponibles dès le 1er avril.

Le 30 juin, ORMSBRIDGE paie 600 000 GBP qui remboursent l'avance : NAVÉLIA n'a plus aucune livre à convertir, son cours est fixé dès aujourd'hui.

**Emploi des euros (0,5 + 0,5 pt).**

| Au 30 juin 2027 | Placement à 2,40 % | Réduction du crédit de trésorerie à 4,15 % |
|---|---:|---:|
| Euros obtenus le 1er avril | 689 742 | 689 742 |
| Intérêts reçus ou économisés (× taux × 90 / 360) | 4 138 | 7 156 |
| **Valeur acquise** | **693 881** | **696 898** |
| Cours à terme implicite (600 000 / valeur acquise) | 0,8647 | 0,8610 |
| Vente à terme (600 000 / 0,8629) | 695 330 | 695 330 |
| **Avantage de l'avance sur la vente à terme** | **− 1 449** | **+ 1 569** |

**Cours implicites (0,5 pt).** Le cours implicite est le cours à terme qui donnerait, pour 600 000 GBP, la même somme en euros que l'avance : 600 000 / 693 881 = **0,8647** (placement) et 600 000 / 696 898 = **0,8610** (crédit de trésorerie). En cotation au certain, le cours le plus bas est le plus favorable pour l'exportateur (moins de livres par euro).

**Comparaison (0,5 pt).** Si NAVÉLIA reste excédentaire et place ses euros à 2,40 %, la **vente à terme** l'emporte (0,8629 contre 0,8647, soit 1 449 €) : l'avance coûte 4,60 % en livres, plus que le taux de 4,00 % retenu par la parité, et les euros rapportent moins que l'Euribor. Si les euros réduisent un crédit de trésorerie à 4,15 %, l'**avance** l'emporte (0,8610, soit 1 569 €). Le seuil se situe à un taux d'emploi des euros d'environ 3,24 %.

**Ce que l'avance apporte de plus et conclusion (0,5 pt).** L'avance couvre **et finance** : elle mobilise la créance dès le 1er avril (689 742 €), comme un escompte, ce qui est précieux pour une société dont les banques limitent les concours et qui engage des dépenses avant l'encaissement de sa levée. En revanche, elle augmente les dettes financières et consomme une partie des lignes accordées par la banque ; si ORMSBRIDGE paie en retard ou ne paie pas, NAVÉLIA doit acheter des livres au comptant pour rembourser (le même risque existe pour la vente à terme, qui oblige à livrer les livres). Conclusion : **vente à terme** si le plan de trésorerie reste excédentaire, **avance en devises** si la société utilise sa ligne de crédit de trésorerie au deuxième trimestre.

**Pourquoi les résultats sont proches (0,5 pt).** Les deux solutions fixent le cours dès aujourd'hui et suppriment le risque de change sur la créance, sans prime ni possibilité de profiter d'une appréciation de la livre (engagements fermes). Le cours à terme se déduit de l'écart de taux entre les deux devises : une vente à terme équivaut à emprunter des livres et à placer des euros aux taux du marché, ce que l'avance réalise avec les taux propres à NAVÉLIA (marge de 0,60 point sur la livre, taux de placement ou de crédit sur l'euro). C'est pourquoi les deux résultats sont proches : la différence tient aux seules conditions bancaires.

**Réponses tolérées** : valeur acquise de 693 880 € (somme des montants arrondis) ; cours à terme non arrondi (0,862883, montant de 695 343 €) si le candidat l'écrit ; comparaison faite sur les cours (0,8629 contre 0,8647 ou 0,8610) plutôt que sur les montants ; comparaison avec le comptant du jour présentée comme le coût de la couverture.

**Erreurs fréquentes**
- Emprunter 600 000 GBP au lieu de leur valeur actuelle : la créance doit rembourser capital et intérêts.
- Multiplier par le cours au lieu de diviser (cotation au certain) ; conclure sur le cours le plus élevé.
- Calculer le cours à terme avec les taux inversés (0,8571) ou affirmer que le déport de la livre traduit une anticipation de baisse du marché.
- Comparer l'avance au terme sans tenir compte de l'emploi des euros entre le 1er avril et le 30 juin.
- `JUR-T07` — absence de tableau comparatif des deux emplois et de la vente à terme.
- `JUR-T13` — conclusion générale, sans lien avec l'incertitude du plan de trésorerie de NAVÉLIA.

---

### 3.4 Garanties publiques à l'export (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Rôle des garanties publiques à l'export et organisme gestionnaire : Bpifrance Assurance Export, pour le compte de l'État | 0,5 |
| 3.4-02 | Prime de 60 000 € ; perte garantie dans le scénario d'échec : 1 450 000 € | 0,5 |
| 3.4-03 | Indemnité de 942 500 € ; charge nette de 567 500 € avec assurance contre 1 450 000 € sans assurance | 0,5 |
| 3.4-04 | Scénario de succès : pas d'indemnité, la prime est le coût de la protection ; intérêt pour NAVÉLIA | 0,5 |
| 3.4-05 | Principe de l'assurance change et intérêt pour l'offre et le contrat TARNMOUTH | 0,5 |

**Rôle des garanties publiques (0,5 pt).** L'État prend en charge, à travers des garanties, des risques de l'exportation que le marché couvre mal ou pas du tout, notamment pour les PME et les entreprises de taille intermédiaire : échec d'une prospection, risque de change pendant la remise d'une offre et l'exécution d'un contrat, risque de non-paiement de certains crédits à l'export. Ces garanties publiques sont gérées par **Bpifrance Assurance Export pour le compte de l'État**. Elles complètent les techniques internes et les instruments bancaires : elles couvrent des risques conditionnels (offre non encore acceptée, ventes futures incertaines) que les instruments fermes ne savent pas traiter.

**Assurance prospection : prime et perte garantie (0,5 pt).**
- Prime = 3 % × 2 000 000 = **60 000 €**, payée à la signature et acquise dans tous les cas.
- Scénario d'échec : perte garantie = 1 800 000 − 14 % × 2 500 000 = 1 800 000 − 350 000 = **1 450 000 €**.

**Indemnité et charge nette (0,5 pt).**
- Indemnité = 65 % × 1 450 000 = **942 500 €**.
- Charge nette de prospection sans assurance : **1 450 000 €** ; avec assurance : 1 450 000 − 942 500 + 60 000 = **567 500 €**. L'assurance réduit la perte de 882 500 € : sans elle, l'échec absorberait près des deux tiers de l'EBITDA de 2026 (63 %) ; avec elle, moins d'un quart (24,7 %).

**Scénario de succès (0,5 pt).** 14 % × 15 000 000 = 2 100 000 €, montant supérieur aux 2 000 000 € de dépenses : la perte garantie est nulle, NAVÉLIA ne reçoit pas d'indemnité et la prime de 60 000 € est le coût de la protection, comme pour toute assurance dont le sinistre ne survient pas. La quotité de 65 % laisse 35 % de la perte à la charge de l'entreprise, ce qui la maintient intéressée au succès de sa prospection. Pour NAVÉLIA, dont le développement américain mobilise 6 M€ et dont la rentabilité est récente, transférer à l'État les deux tiers du risque d'échec d'une prospection auprès d'une nouvelle clientèle sécurise le plan présenté aux investisseurs de la levée, pour un coût limité (3 % du budget garanti).

**Assurance change (0,5 pt).** Moyennant une prime, l'assurance change garantit à l'exportateur un cours fixé au moment de la remise de l'offre en devises, pendant la négociation puis pendant l'exécution du contrat ; certaines formules lui laissent une partie du gain si la devise évolue favorablement. Elle convient au contrat TARNMOUTH : l'offre en livres est ferme jusqu'au 31 mai, mais le contrat n'est pas encore signé. Une vente à terme de 516 000 GBP créerait une position de change de sens contraire si le client renonçait, alors que l'assurance change ne porte que sur l'opération effectivement conclue. Combinée à la clause d'indexation, qui partage le risque hors de la bande de ± 2 %, elle protégerait la part du risque restant à NAVÉLIA entre l'offre et le paiement ; son intérêt dépend de la prime, non encore chiffrée.

**Réponses tolérées** : rôle des garanties présenté à travers les seuls produits de l'annexe ; charge nette exprimée sans la prime si le candidat la traite à part ; rapprochement de l'assurance change d'une option de change (protection contre une prime, gain partiellement conservé) sans aucun calcul de prime.

**Erreurs fréquentes**
- Attribuer ces garanties à Coface, assureur-crédit privé, au lieu de Bpifrance Assurance Export, qui les gère pour le compte de l'État.
- Calculer l'indemnité sur le budget (2 000 000 €) ou sur les dépenses brutes sans déduire la part du chiffre d'affaires réalisé.
- Juger l'assurance « inutile » dans le scénario de succès : la prime rémunère la protection contre l'échec.
- `JUR-T12` — confondre l'assurance prospection (risque d'échec commercial) et l'assurance change (risque de cours).

---

### 3.5 Stratégie de couverture recommandée (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Stratégie par devise et par risque, cohérente avec les calculs des questions 3.1 à 3.4 | 1 |
| 3.5-02 | Comparaison des solutions selon le coût, la souplesse, la simplicité et le risque résiduel | 0,5 |
| 3.5-03 | Risques qui demeurent et mise en œuvre (politique écrite, absence de spéculation) | 0,5 |

**Stratégie recommandée (1 pt).** Une réponse possible :
1. **Techniques internes d'abord**, sans coût : garder les dollars reçus de la filiale sur le compte en dollars pour payer KESTAVO (2,1 M USD de position fermée) ; fixer avec NAVÉLIA Inc. un calendrier de règlement régulier plutôt que des anticipations au gré des prévisions, le termaillage restant un pari sur le cours.
2. **Position résiduelle en dollars** (2,4 M USD au trimestre) : la couvrir à chaque échéance par des ventes à terme auprès de la banque, ou par une avance en dollars si la trésorerie devient tendue, selon la même logique qu'à la question 3.3.
3. **Créance ORMSBRIDGE** (600 000 GBP) : vente à terme si NAVÉLIA reste excédentaire, avance en livres si elle utilise sa ligne de crédit de trésorerie ; le solde de mai (100 000 GBP) peut rester ouvert ou être vendu à terme, compte tenu de son faible montant.
4. **Contrat TARNMOUTH** : clause d'indexation négociée avec le client ; assurance change pendant la validité de l'offre si sa prime est raisonnable ; à défaut, vente à terme dès la signature. Le montant en livres dépend alors de la clause : la vente à terme de 516 000 GBP laisse un écart si le prix est révisé.
5. **Développement américain** : assurance prospection de Bpifrance Assurance Export sur le budget de 2 M€.

**Comparaison (0,5 pt).**

| Solution | Coût | Souplesse | Simplicité | Risque résiduel |
|---|---|---|---|---|
| Compensation des flux en dollars | nul ; économie de marges de change | totale | très simple (compte en dollars) | décalage de dates et de montants |
| Termaillage avec la filiale | coût de portage (− 5 714 € si le cours ne bouge pas) | décision interne | simple dans le groupe | pari : perte si l'anticipation est fausse |
| Clause d'indexation | nul ; concession commerciale | négociée contrat par contrat | simple à appliquer | variations jusqu'à ± 2 %, puis moitié de la variation ; effet de seuil ; offre non couverte |
| Vente à terme | aucun coût explicite ; déport de 2 345 € par rapport au comptant du jour (écart de taux, non une perte) | ferme : livraison obligatoire | simple, sans décaissement | nul sur le cours ; défaut ou retard du client |
| Avance en devises | intérêts à 4,60 % ; gagnante si les euros réduisent un crédit | ferme | simple, mais utilise les lignes bancaires | nul sur le cours ; endettement ; défaut du client |
| Assurance prospection | prime de 60 000 € | couvre un risque incertain | dossier à constituer | 35 % de la perte d'échec |
| Assurance change | prime à chiffrer | adaptée à une offre non encore acceptée | dossier à constituer | selon la formule retenue |

**Risques qui demeurent et mise en œuvre (0,5 pt).** Ces solutions couvrent le risque de transaction du trimestre, pas le risque de change économique : une baisse durable du dollar ou de la livre réduirait la compétitivité des moteurs face aux concurrents américains et britanniques et devrait être traitée par la politique de prix, les achats en dollars ou un assemblage local à terme. Le risque de crédit des clients reste entier. La direction devrait formaliser une politique de couverture écrite (part des flux certains couverte, horizon de trois à six mois, instruments autorisés, interdiction de positions spéculatives), présentée au conseil où siègent MARVENE Capital et SOLENTE Ventures : réduire la variabilité du résultat d'une société qui prépare une levée de fonds est un argument auprès des investisseurs.

**Réponses tolérées** : couverture d'une partie seulement de la position (50 à 80 %) en gardant une exposition au gain possible, si le risque résiduel est mesuré ; mention des options de change comme alternative pour la position en dollars, écartée à ce stade par la direction (coût de la prime, complexité) ; présentation de la comparaison en rédaction plutôt qu'en tableau, si les quatre critères sont traités.

**Erreurs fréquentes**
- Recommander une solution unique pour toutes les expositions, sans distinguer flux certains (créances), flux conditionnels (offre TARNMOUTH) et risque d'échec commercial (prospection).
- Proposer de « spéculer » sur la baisse du dollar par le termaillage au lieu de couvrir.
- `JUR-T13` — recommandation générale sans lien avec la trésorerie, la taille et la levée de fonds de NAVÉLIA.
- `JUR-T15` — question de synthèse bâclée alors qu'elle vaut 2 points.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme DSCG UE 2 (arrêté du 4 août 2025), partie 6.3 | position de change courte ou longue, ouverte ou fermée ; marché au comptant et à terme ; techniques internes (termaillage, netting, indexation monétaire) ; garanties publiques à l'export et avances en devises ; exclusion des modèles de valorisation des options de change | [V] | F07 § 0 ; `perimetre_ue2.yaml` (6.3) |
| Guide pédagogique DSCG, juillet 2026, p. 78-79 | mesure de l'exposition à partir de flux en devises ; choix d'une couverture selon le coût, la simplicité, la souplesse et le risque résiduel ; conditions des garanties et des avances fournies | [V] | F07 § 0 et 3.3 ; `perimetre_ue2.yaml` |
| Position de change, cotation au certain, sens du risque | définitions usuelles | [S] | F07 § 3.1 |
| Termaillage, compensation, netting, clause d'indexation monétaire, choix de la devise de facturation | mécanismes | [S] | F07 § 3.2 |
| Garanties publiques à l'export gérées par Bpifrance Assurance Export pour le compte de l'État ; principe de l'assurance change | organisme gestionnaire et principe | [S] | F07 § 3.2 ; F99 § 2 |
| Assurance prospection : mécanisme et conditions | posés par l'énoncé (conditions simplifiées, ne reproduisant pas le barème en vigueur) ; produit non documenté dans les fiches | [?] | — |
| Avance en devises, parité des taux d'intérêt, report et déport | formules usuelles | [S] | F07 § 3.2 et 3.3 |
| Euribor 3 mois 2,65 % ; EUR/USD 1,12 | hypothèses plausibles fin 2026, posées par l'énoncé | [V] séries BCE (valeurs arrondies) | F11 § 1 et 4 |
| Taux USD et GBP à 3 mois, cours EUR/GBP | hypothèses d'énoncé | — | F11 § 4 |
| Jensen et Meckling (1976) | théorie de l'agence (réponse tolérée, relation entre la société mère et sa filiale) | [V programme 2.1] | F10 § 3 |
