# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 11 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F06 marchés financiers et innovations, F09 éthique, conformité et réglementation bancaire, F10 auteurs et théories, F11 données de marché (toutes à jour au 23/10/2026) ; fiche commune Sapin II, LCB-FT et MiCA, § 3.5 sur le financement participatif (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (levées de fonds sur les plateformes, tableau d'amortissement, coûts actuariels, répartition du capital, plan de financement, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un coût actuariel calculé à partir d'un tableau d'amortissement erroné à la question 2.3).

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
