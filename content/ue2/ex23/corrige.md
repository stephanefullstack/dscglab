# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 23 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 risques de taux et trésorerie de groupe, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (centralisation notionnelle et origine du gain, coûts effectifs annuels, valeur actuelle de la jambe fixe du swap, swap et cap dans trois scénarios, valeur intrinsèque et valeur temps de la prime, barème, liste noire, hors-programme ; besoin cumulé, détail des coûts des offres, exposition et valeur du swap vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un gain de centralisation calculé à partir d'intérêts sans convention erronés, ou des coûts effectifs calculés sur une utilisation moyenne erronée à la question 2.3).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Centralisation notionnelle de la trésorerie des quatre sociétés | `6.1.a` Appliquer les mécanismes de centralisation de trésorerie | 4 |
| 2.2 Placement des acomptes du constructeur | `6.1.b` Discerner les différents types de financement et de placement | 2 |
| 2.3 Financement du besoin lié à la montée en cadence | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `6.1.b` Discerner les différents types de financement et de placement | 4 |
| 2.4 Exposition au risque de taux et valeur du contrat d'échange de taux | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 2 |
| 2.5 Couverture du crédit de l'atelier : swap ou cap | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux ; `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) | 5 |
| **Total** | | **17** |

Part du calcul : 8,5 points (2.1-01, 2.1-02, 2.3-01, 2.3-02, 2.4-02, 2.4-03, 2.5-01 à 2.5-04). Part de l'analyse : 8,5 points (question 2.2 entière, 2.1-03 à 2.1-05, 2.3-03, 2.3-04, 2.4-01, 2.4-04, 2.5-05 à 2.5-07). Les commentaires valent la moitié des points : un calcul sans conclusion pour Mme VOLTERRE ne rapporte que la moitié de la question (`JUR-T13`).

---

### 2.1 Centralisation notionnelle de la trésorerie des quatre sociétés (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Intérêts sans convention : MAURVEL SA − 349 138 € ; Freinage + 102 788 € ; Ibérica − 45 900 € ; Bahntechnik + 38 545 € ; total − 253 705 € | 1 |
| 2.1-02 | Soldes fusionnés (− 900, + 1 800, − 4 500, + 8 100 k€) ; intérêts avec la convention − 3 125 € ; frais 24 000 € ; total − 27 125 € ; gain net 226 580 € | 1 |
| 2.1-03 | Origine du gain : compensation des soldes de signes opposés et meilleures conditions, nettes des frais | 0,5 |
| 2.1-04 | Différences entre centralisation notionnelle et centralisation physique | 0,5 |
| 2.1-05 | Prérequis et limites du dispositif pour des filiales en Espagne et en Allemagne | 1 |

**Intérêts sans convention (1 pt).** Intérêts du trimestre = solde × taux × jours / 360 ; taux débiteur sur un solde négatif, taux créditeur sur un solde positif.

| € | T1 (90 j) | T2 (91 j) | T3 (92 j) | T4 (92 j) | Total 2027 |
|---|---:|---:|---:|---:|---:|
| MAURVEL SA (4,25 % / 1,50 %) | − 76 500 | − 96 688 | − 117 300 | − 58 650 | **− 349 138** |
| MAURVEL Freinage (4,25 % / 1,50 %) | 20 250 | 23 888 | 27 600 | 31 050 | **102 788** |
| MAURVEL Ibérica (4,75 % / 1,20 %) | − 21 375 | 2 730 | − 32 775 | 5 520 | **− 45 900** |
| MAURVEL Bahntechnik (4,55 % / 1,30 %) | 8 775 | 11 830 | 5 980 | 11 960 | **38 545** |
| **Groupe** | | | | | **− 253 705** |

Par exemple, MAURVEL SA au T2 : − 9 000 000 × 4,25 % × 91 / 360 = − 96 687,50, soit − 96 688 € ; Ibérica au T2 : 900 000 × 1,20 % × 91 / 360 = 2 730 €. Le groupe paie 403 288 € d'intérêts débiteurs et ne reçoit que 149 583 € d'intérêts créditeurs, alors que ses excédents (8,1 à 13,5 M€ selon les trimestres) sont du même ordre que ses découverts (5,4 à 13,5 M€).

**Intérêts avec la convention et gain (1 pt).**

| | T1 | T2 | T3 | T4 | Total |
|---|---:|---:|---:|---:|---:|
| Solde fusionné (k€) | − 900 | + 1 800 | − 4 500 | + 8 100 | |
| Taux appliqué | 3,90 % | 2,00 % | 3,90 % | 2,00 % | |
| Intérêts (€) | − 8 775 | + 9 100 | − 44 850 | + 41 400 | **− 3 125** |
| Frais de la convention | − 6 000 | − 6 000 | − 6 000 | − 6 000 | **− 24 000** |
| **Total avec la convention** | | | | | **− 27 125** |

Gain net = − 27 125 − (− 253 705) = **226 580 €** par an. La charge financière nette de la trésorerie d'exploitation du groupe est presque supprimée.

**Origine du gain (0,5 pt).** Le gain a deux sources :
- la **fusion des échelles** : un découvert de MAURVEL SA rémunéré à 4,25 % ne coexiste plus avec un excédent de Freinage rémunéré à 1,50 % ; les intérêts portent sur le seul solde net, de signe variable et beaucoup plus faible (au plus 8,1 M€ au lieu de 13,5 M€ de découverts). Si chaque solde était seulement placé aux conditions de la convention, sans fusion, le groupe paierait 154 745 € : la fusion apporte 151 620 € (154 745 − 3 125) ;
- les **meilleures conditions** de la convention (3,90 % au lieu de 4,25 à 4,75 % ; 2,00 % au lieu de 1,20 à 1,50 %), obtenues parce que la Banque ORMESSAN capte l'ensemble des flux du groupe : 98 960 € (253 705 − 154 745) ;
- diminués des **frais** de la convention (24 000 €). Le gain est un gain pour le groupe : la convention de trésorerie doit le répartir entre les sociétés (intérêts internes), sinon les filiales créditrices financeraient MAURVEL SA sans contrepartie.

**Centralisation notionnelle et centralisation physique (0,5 pt).**
- **Notionnelle** : aucun mouvement de fonds ; chaque société garde son compte, son solde et sa signature ; la banque calcule seulement les intérêts sur la somme fictive des soldes. Pas de prêts ni d'emprunts intragroupe, pas d'intérêts internes à facturer chaque jour ; mise en place plus légère, autonomie apparente des filiales préservée. Elle suppose que tous les comptes soient dans la même banque, qui porte le risque des soldes débiteurs et exige des garanties croisées.
- **Physique** (*cash pooling* à mise à zéro) : les soldes des filiales sont virés chaque jour vers un compte centralisateur (et les découverts y sont couverts) ; la société pivot place l'excédent ou finance le besoin ; les remontées créent des prêts et emprunts intragroupe rémunérés selon la convention de trésorerie. Elle donne une maîtrise réelle de la liquidité et permet de rembourser des dettes ou de placer l'excédent net à l'extérieur, mais crée une créance de chaque filiale sur la société pivot et demande une gestion plus lourde (comptes courants, intérêts internes).

**Prérequis et limites pour des filiales en Espagne et en Allemagne (1 pt).**
- **Prérequis** : ouverture des comptes d'Ibérica et de Bahntechnik dans les agences de Saragosse et de Leipzig de la Banque ORMESSAN et transfert de leurs flux (fin ou réduction de la relation avec le Banco RIBELAR et la HELMRATH Bank) ; garanties croisées des quatre sociétés ; convention de trésorerie signée par les quatre sociétés (répartition des intérêts, conditions de marché pour chaque société, durée, sortie) ; système d'information qui donne chaque jour la position du groupe ; une seule devise, l'euro, ce qui évite toute conversion.
- **Limites** :
  - le dispositif dépend de la **réglementation locale** de chaque pays et de l'accord des dirigeants des filiales, qui doivent s'assurer que la garantie donnée et la répartition du gain respectent l'intérêt de leur propre société (ces questions sont traitées par les juristes du groupe, hors de l'analyse financière) ;
  - **concentration bancaire** : toute la trésorerie du groupe chez la Banque ORMESSAN, déjà prêteuse du crédit de l'atelier et proposante des offres de financement et de couverture (annexes 2.3 et 2.4) : moindre mise en concurrence, dépendance, risque de contrepartie ;
  - les **garanties croisées** exposent les filiales créditrices (Freinage, Bahntechnik) au découvert de MAURVEL SA, qui est débitrice toute l'année ;
  - la notionnelle ne finance rien : le solde fusionné reste débiteur au T1 et au T3 (− 4,5 M€) et elle ne couvre ni le besoin du contrat-cadre ni l'atelier ; la banque facture le service (24 000 € par an) et exige des garanties croisées ;
  - gain fondé sur des **soldes prévisionnels** : il dépend de la persistance des excédents de Freinage et de Bahntechnik.
- **Conclusion** : la convention est rentable (226 580 € par an, plus de neuf fois ses frais) et adaptée à un groupe monodevise ; elle doit s'accompagner d'une convention de trésorerie qui rémunère équitablement les filiales et d'une vigilance sur la dépendance envers la Banque ORMESSAN.

**Réponses tolérées** : intérêts sans arrondi par trimestre (total à 1 € près) ; gain présenté sans décomposition chiffrée de son origine, si les deux sources sont expliquées ; décomposition faite dans l'autre ordre (d'abord la fusion aux conditions actuelles, puis les conditions) si elle est justifiée ; mention du *target balancing* comme variante de la centralisation physique.

**Erreurs fréquentes**
- Appliquer à chaque société les taux de la convention et oublier la fusion des soldes, ou fusionner les soldes en gardant les taux des banques.
- Oublier les frais de la convention, ou les compter une seule fois au lieu de quatre.
- Décrire des virements quotidiens vers un compte centralisateur : c'est la centralisation physique, pas la notionnelle.
- Développer le droit applicable aux conventions de trésorerie entre sociétés du groupe ou leur imposition : hors programme.
- `JUR-T07` — intérêts calculés en ligne, sans tableau par société et par trimestre ; `JUR-T13` — avantages génériques de la centralisation sans les soldes du cas.

---

### 2.2 Placement des acomptes du constructeur (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Horizon et contraintes : 4,20 M€ employés en trois échéances (fin juin, fin juillet, fin août), soit 3 à 5 mois ; sécurité du capital et liquidité prioritaires | 0,5 |
| 2.2-02 | Choix des supports au regard du couple rentabilité-risque : supports retenus et supports écartés, justifiés | 1 |
| 2.2-03 | Recommandation : répartition des 4,20 M€ entre supports, alignée sur les trois dates d'emploi (montants, durées, produit attendu) | 0,5 |

**Horizon et contraintes (0,5 pt).** Les 4,20 M€ ne sont pas un excédent durable : ils seront employés à payer les premiers achats et les premiers coûts de production, 0,65 M€ fin juin (3 mois), 1,55 M€ fin juillet (4 mois) et 2,00 M€ fin août (5 mois) ; dès septembre, le contrat devient consommateur de trésorerie (besoin de 1,15 M€ fin septembre, annexe 2.3). Ces fonds doivent donc être :
- **sûrs** : ce sont des avances du client, garanties par une garantie bancaire de restitution ; une perte en capital devrait être compensée par MAURVEL, alors que le prix du contrat est ferme ;
- **disponibles aux dates prévues**, voire plus tôt si les fonderies livrent en avance ;
- la **rentabilité** est secondaire : 4,20 M€ placés en moyenne quatre mois à 2,35 % rapportent environ 33 k€.

**Choix des supports (1 pt).**

| Support | Adéquation | Décision |
|---|---|---|
| Compte à vue (1,50 %) | liquidité totale, sans risque, mais le rendement le plus faible | solde de précaution seulement |
| Comptes à terme (2,30 à 2,40 %) | capital garanti, taux connu ; durées de 3 à 5 mois qui correspondent aux échéances ; pénalité en cas de retrait anticipé | **retenus** pour les montants dont la date d'emploi est sûre |
| OPCVM monétaire (2,35 %) | liquidité quotidienne, risque très faible, rendement proche de l'€STR, non garanti | **retenu** pour la part dont la date est incertaine |
| NEU CP (2,70 %) | meilleur rendement des supports courts, mais échéance au 1er octobre, après la date d'emploi de tous les fonds ; revente sur un marché étroit, à un prix incertain ; risque de crédit | écarté |
| OPCVM obligataire (3,10 %) | durée recommandée de 3 ans ; une hausse des taux ferait baisser sa valeur liquidative au moment de l'emploi (relation inverse valeur-taux) | écarté |
| Fonds d'actions (7 %) | horizon de 5 ans, volatilité de 18 % : une perte de plusieurs points en quelques mois est probable | écarté |

Le couple rentabilité-risque ne se lit qu'à horizon donné : sur 3 à 5 mois, les supports à rendement plus élevé exposent le capital à un risque (taux, crédit, marché) sans rapport avec le gain attendu, quelques dixièmes de point sur quelques mois.

**Recommandation (0,5 pt).** Échelonner les échéances sur les paiements : par exemple 2,00 M€ en compte à terme de 4 mois (2,35 %, échéance le 1er août, avant le paiement de fin août) et 2,20 M€ en OPCVM monétaire, racheté pour les paiements de fin juin et de fin juillet ; un compte à terme de 3 mois pour 0,65 M€ échoirait le 1er juillet, après le paiement de fin juin. Produit attendu d'environ 15,7 k€ sur le compte à terme (2,00 M€ × 2,35 % × 4 / 12) et d'environ 16 k€ sur l'OPCVM (0,65 M€ pendant 3 mois et 1,55 M€ pendant 4 mois à 2,35 %). Remarque, valorisée mais non exigée : MAURVEL SA est débitrice toute l'année à 4,25 % (annexe 2.1). Laisser les acomptes sur son compte pour réduire ce découvert rapporterait environ 1,9 point de plus que le meilleur placement sûr, si la garantie de restitution n'impose pas de les isoler : l'exclusion des acomptes de la gestion de trésorerie mérite d'être discutée avec la banque.

**Réponses tolérées** : tout échelonnement cohérent avec les trois dates (comptes à terme de 3, 4 et 5 mois ; tout en OPCVM monétaire au nom de la souplesse) ; NEU CP retenu pour une petite part si le candidat mesure le risque de revente ; recommandation d'employer les acomptes à réduire le découvert, si elle est justifiée par le coût d'opportunité ; la remarque sur le coût d'opportunité face au découvert de MAURVEL SA (4,25 %) est valorisée, mais non exigée.

**Erreurs fréquentes**
- Choisir le support au rendement le plus élevé sans considérer l'horizon et le risque en capital.
- Traiter les acomptes comme un excédent durable, alors qu'ils seront employés dans les cinq mois.
- `JUR-T13` — liste générale des placements sans les dates d'emploi du cas ; `JUR-T02` — couple rentabilité-risque énoncé sans application.

---

### 2.3 Financement du besoin lié à la montée en cadence (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Flux nets et besoin cumulé par trimestre ; besoin maximal de 8,40 M€ fin T1 2028 ; utilisation moyenne de 6,00 M€ | 1 |
| 2.3-02 | Coûts de la période de référence et coût effectif annuel : A 282,00 k€, 4,70 % (3,53 % après IS) ; B 243,00 k€, 5,40 % (4,05 %) ; C 300,00 k€, 5,00 % (3,75 %) | 1,5 |
| 2.3-03 | Comparaison qualitative : profil du besoin, souplesse, garanties et engagements, relation avec le constructeur | 1 |
| 2.3-04 | Recommandation argumentée | 0,5 |

**Besoin de financement (1 pt).**

| M€ | T1 2027 | T2 2027 | T3 2027 | T4 2027 | T1 2028 | T2 2028 | T3 2028 | T4 2028 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Flux net du trimestre | 0,60 | 2,95 | − 4,70 | − 5,65 | − 1,60 | 4,10 | − 0,20 | − 0,40 |
| Trésorerie cumulée | 0,60 | 3,55 | − 1,15 | − 6,80 | − 8,40 | − 4,30 | − 4,50 | − 4,90 |
| **Besoin cumulé** | – | – | **1,15** | **6,80** | **8,40** | **4,30** | **4,50** | **4,90** |

- **Besoin maximal** : **8,40 M€** fin mars 2028. Les acomptes couvrent les premiers mois ; le besoin naît en juillet 2027, avant toute facture, parce que l'acier et les pièces sont payés environ trois mois et demi avant la livraison des bogies et le règlement du constructeur deux mois après ; il culmine pendant la montée en cadence (production de 2028 lancée, peu de règlements encore reçus). Il peut dépasser 8,40 M€ en cours de trimestre.
- Le besoin ne disparaît pas : il se stabilise autour de 4,5 à 5 M€ en 2028, puisque chaque bogie est payé plus de cinq mois après le paiement de ses matières, et il croîtra avec les cadences de 2029-2030 (39 M€ par an). Une **part temporaire** (pointe de 2027-2028) se distingue d'une **part durable** tant que dure le contrat.
- **Utilisation moyenne** de la période de référence = (6,80 + 8,40 + 4,30 + 4,50) / 4 = **6,00 M€**.

**Coûts effectifs annuels (1,5 pt).** Euribor 2,65 % ; une année.

| k€ | A. Préfinancement (10 M€) | B. Affacturage | C. Crédit renouvelable (15 M€) |
|---|---:|---:|---:|
| Intérêts ou commission de financement | 6,00 M€ × 4,25 % = 255,00 | 4,50 M€ × 3,75 % = 168,75 | 6,00 M€ × 3,90 % = 234,00 |
| Commission sur la part non utilisée | 4,00 M€ × 0,30 % = 12,00 | – | 9,00 M€ × 0,40 % = 36,00 |
| Commission d'affacturage | – | 29,70 M€ × 0,25 % = 74,25 | – |
| Frais de mise en place étalés | 10 M€ × 0,30 % / 2 = 15,00 | – | 15 M€ × 0,60 % / 3 = 30,00 |
| **Coût de la période** | **282,00** | **243,00** | **300,00** |
| Montant moyen financé | 6,00 M€ | 4,50 M€ | 6,00 M€ |
| **Coût effectif annuel avant IS** | **4,70 %** | **5,40 %** | **5,00 %** |
| **Après IS (× 0,75)** | **3,53 %** | **4,05 %** | **3,75 %** |

Créances cédées sur la période : livraisons d'octobre 2027 à septembre 2028 = 6 + 9 × 3 = 33 M€, nettes de l'acompte imputé de 10 % : 33 × 0,90 = **29,70 M€**. Le coût de l'affacturage rémunère aussi des services (gestion et recouvrement des créances, garantie contre l'insolvabilité) : il n'est pas un pur coût de financement.

**Comparaison qualitative (1 pt).**
- **Adéquation au profil du besoin** : l'offre A suit le besoin (tirages au fur et à mesure des paiements du contrat, remboursements par les règlements du constructeur), dès juillet 2027 ; son autorisation de 10 M€ couvre la pointe de 8,40 M€ avec une marge pour les dépassements en cours de trimestre. L'offre B ne finance que des factures émises : rien avant octobre 2027 alors que le besoin atteint 1,15 M€ fin septembre, puis 4,50 M€ en moyenne, très en dessous de la pointe ; elle ne finance pas la phase de fabrication, qui fait l'essentiel du besoin. L'offre C couvre tout le besoin, et au-delà.
- **Souplesse et durée** : C est la plus souple (usage libre, trois ans, tirages renouvelables) ; A est réservée au contrat et s'arrête le 30 juin 2029, alors que le contrat court jusqu'en 2030 et que la part durable du besoin (environ 5 M€) subsiste ; B suit le chiffre d'affaires sans plafond fixe.
- **Garanties et engagements** : A demande la cession des créances du contrat et leur domiciliation à la Banque ORMESSAN, qui renforce encore sa position (annexes 2.1 et 2.4). C impose un engagement DFN / EBITDA ≤ 3,00 : le ratio de 2026 est de 1,73 (38 / 22), mais l'endettement augmente fortement en 2027 (travaux de l'atelier, besoin du contrat) ; un manquement rendrait l'autorisation exigible au plus mauvais moment. Ces engagements protègent les prêteurs contre les décisions des actionnaires et des dirigeants qui accroîtraient leur risque (conflit actionnaires-créanciers décrit par Jensen et Meckling, 1976).
- **Relation avec le constructeur** : l'affacturage notifié informe le constructeur, client d'un contrat de 120 M€ sur quatre ans, que ses factures sont cédées à un factor, ce qui peut être lu comme un signe de tension de trésorerie ; la garantie contre l'insolvabilité a peu de valeur sur un grand constructeur européen. La cession en garantie de l'offre A est moins visible pour le client.
- Toutes les offres sont à **taux variable** : une hausse de l'Euribor renchérirait le coût du besoin (environ 60 k€ par an pour un point sur 6 M€).

**Recommandation (0,5 pt).** Retenir le **crédit de préfinancement (offre A)**, le moins cher (4,70 % avant IS, 3,53 % après IS), adossé au contrat et dimensionné pour sa pointe. Il convient de prévoir dès maintenant le relais de la part durable du besoin après juin 2029 : un crédit renouvelable de montant plus faible, ou l'autofinancement dégagé par le contrat. Recourir à la dette plutôt qu'à des fonds propres pour un besoin d'exploitation lié à un contrat ferme est cohérent avec le financement hiérarchique (Myers et Majluf, 1984). L'affacturage est écarté : il est le plus cher, ne couvre pas la phase de fabrication et expose la relation avec le constructeur.

**Réponses tolérées** : choix du crédit renouvelable, s'il est justifié par sa souplesse, sa durée de trois ans et la couverture de la part durable, et si le candidat mesure son surcoût (0,30 point) et le risque lié à l'engagement financier ; combinaison A + C ; coût de l'affacturage calculé sur les créances cédées et commenté ; utilisation moyenne calculée sur une autre période si la convention est respectée ensuite.

**Erreurs fréquentes**
- Retenir le besoin de fin d'année (4,90 M€) au lieu du besoin maximal pour dimensionner le financement.
- Oublier la commission sur la part non utilisée, ou rattacher les frais de mise en place en totalité à la première année.
- Comparer le taux d'intérêt affiché (Euribor + marge) au lieu du coût effectif.
- Calculer la commission d'affacturage sur le montant des commandes (36 M€) ou sur les factures avant imputation des acomptes.
- `JUR-T07` — besoin cumulé sans tableau trimestriel ; `JUR-T13` — avantages généraux de l'affacturage sans constater qu'il ne finance pas la fabrication.

---

### 2.4 Exposition au risque de taux et valeur du contrat d'échange de taux (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Exposition : emprunteur à taux variable, risque sur la charge d'intérêts (flux) et non sur la valeur du crédit ; aggravé par le prix ferme du contrat et le budget de 4,50 % | 0,5 |
| 2.4-02 | Hausse d'un point : + 360 000 € par an avant IS, + 270 000 € après IS | 0,5 |
| 2.4-03 | Valeur actuelle de la jambe fixe : 36,00 M€ au taux de 2,80 %, 34,39 M€ au taux de 3,80 % ; valeur du swap : 0 puis + 1,61 M€ | 0,5 |
| 2.4-04 | Commentaire : relation inverse valeur-taux, effet compensateur, symétrie en cas de baisse | 0,5 |

**Exposition (0,5 pt).** Le crédit de 36 M€ est à taux variable, révisé chaque trimestre : sa valeur reste proche de son nominal (le taux suit le marché), mais sa **charge d'intérêts** suit l'Euribor. MAURVEL craint la **hausse** des taux. L'exposition est sensible pour trois raisons : le prix ferme du contrat-cadre ne permet pas de répercuter une hausse des frais financiers ; le budget retient un coût de 4,50 % au plus, à 0,35 point seulement du taux actuel (4,15 %) ; le besoin du contrat (annexe 2.3) est lui aussi financé à taux variable. S'y ajoute un risque de refinancement en 2032, quand le crédit devra être remboursé en une fois. Les autres dettes du groupe, à taux fixe, exposent au contraire à un risque de valeur (coût d'opportunité en cas de baisse).

**Effet d'une hausse d'un point (0,5 pt).** 36 000 000 × 1 % = **360 000 €** de charges supplémentaires par an avant impôt, soit 360 000 × (1 − 25 %) = **270 000 €** après impôt.

**Valeur du swap (0,5 pt).**
- Au taux de swap de 2,80 % : la jambe fixe verse 36 × 2,80 % = 1,008 M€ par an pendant cinq ans puis 36 M€ ; actualisée à son propre taux, elle vaut **36,00 M€** ; valeur du swap = 36 − 36,00 = **0** : à la signature, un swap conclu au taux du marché ne coûte et ne rapporte rien.
- Au taux de 3,80 % : valeur actuelle = 1,008 × [1 − (1,038)^−5] / 0,038 + 36 × (1,038)^−5 = 1,008 × 4,4769 + 36 × 0,8299 = **34,39 M€** ; valeur du swap pour MAURVEL = 36 − 34,39 = **+ 1,61 M€**.

**Commentaire (0,5 pt).** La valeur actuelle de flux fixes **baisse quand le taux d'actualisation monte** : la jambe fixe que MAURVEL s'est engagée à payer vaut 1,61 M€ de moins. Le swap payeur du taux fixe prend donc de la valeur quand les taux montent, ce qui compense, en valeur, le surcoût de 0,36 M€ par an du crédit pendant cinq ans (1,61 M€ ≈ 0,36 M€ × 4,4769 : la valeur du swap est la valeur actuelle des différentiels futurs). Inversement, une baisse d'un point (1,80 %) donnerait une valeur de − 1,71 M€ : le swap fige le coût, et MAURVEL renoncerait au bénéfice de la baisse ; s'il fallait dénouer le swap par anticipation (remboursement anticipé du crédit, cession de l'atelier), cette valeur négative serait à payer. Le crédit variable est exposé sur ses flux ; le swap le transforme en dette à taux fixe, exposée sur sa valeur.

**Réponses tolérées** : valeur du swap calculée directement comme valeur actuelle des différentiels (36 × 1 % × 4,4769 = 1,61 M€) ; facteurs d'actualisation arrondis (écart de 0,01 M€) ; mention de la sensibilité sans calcul.

**Erreurs fréquentes**
- Conclure que la hausse des taux fait baisser la valeur du crédit à taux variable : sa valeur reste proche du nominal.
- Signe de la valeur du swap inversé : pour le payeur du taux fixe, une hausse des taux est favorable.
- Actualiser au taux de 2,80 % après la hausse.
- `JUR-T13` — exposition décrite sans le prix ferme et le budget de 4,50 %.

---

### 2.5 Couverture du crédit de l'atelier : swap ou cap (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Risque de hausse ; positions : payeur du taux fixe, acheteur du cap ; sans couverture : 469 200, 381 800 et 303 600 € (5,10 %, 4,15 %, 3,30 %) | 0,5 |
| 2.5-02 | Swap : différentiels + 73 600, − 13 800 et − 92 000 € ; charge nette 395 600 €, taux effectif 4,30 % dans les trois scénarios | 1 |
| 2.5-03 | Cap : versements 101 200, 13 800 et 0 € ; prime 41 400 € ; charge nette 409 400, 409 400 et 345 000 € ; taux effectif 4,45 %, 4,45 % et 3,75 % | 1 |
| 2.5-04 | Prime de la période 41 400 € = valeur intrinsèque 13 800 € + valeur temps 27 600 € ; cap dans la monnaie | 0,5 |
| 2.5-05 | Comparaison : coût (aucune prime pour le swap, 0,45 % l'an pour le cap ; taux effectifs selon les scénarios), flexibilité, risque résiduel ; le point mort de 2,35 % est valorisé, mais non exigé | 1 |
| 2.5-06 | Gré à gré et marché organisé | 0,5 |
| 2.5-07 | Recommandation argumentée | 0,5 |

**Risque, positions et coût sans couverture (0,5 pt).** MAURVEL craint la hausse : elle se couvre comme **payeur du taux fixe** du swap (elle reçoit l'Euribor, qui compense les intérêts de son crédit) ou comme **acheteur du cap** (elle reçoit la différence au-dessus de 2,50 %). Intérêts du crédit = 36 000 000 × (Euribor + 1,50 %) × 92 / 360 :

| Euribor constaté le 1er juillet | 3,60 % | 2,65 % | 1,80 % |
|---|---:|---:|---:|
| Taux du crédit | 5,10 % | 4,15 % | 3,30 % |
| Intérêts de la période (€) | 469 200 | 381 800 | 303 600 |

**Swap (1 pt).** Différentiel = 36 000 000 × (Euribor − 2,80 %) × 92 / 360.

| Swap payeur de 2,80 % | 3,60 % | 2,65 % | 1,80 % |
|---|---:|---:|---:|
| Intérêts du crédit | 469 200 | 381 800 | 303 600 |
| Différentiel reçu (+) ou versé (−) | + 73 600 | − 13 800 | − 92 000 |
| **Charge d'intérêts nette** | **395 600** | **395 600** | **395 600** |
| **Taux effectif** | **4,30 %** | **4,30 %** | **4,30 %** |

Le swap fixe le coût à 2,80 % + 1,50 % = 4,30 %, quel que soit l'Euribor.

**Cap (1 pt).** Versement = 36 000 000 × max(0 ; Euribor − 2,50 %) × 92 / 360 ; prime de la période = 36 000 000 × 0,45 % × 92 / 360 = 41 400 €.

| Cap 2,50 % | 3,60 % | 2,65 % | 1,80 % |
|---|---:|---:|---:|
| Intérêts du crédit | 469 200 | 381 800 | 303 600 |
| Versement reçu du cap | − 101 200 | − 13 800 | 0 |
| Prime de la période | + 41 400 | + 41 400 | + 41 400 |
| **Charge d'intérêts nette** | **409 400** | **409 400** | **345 000** |
| **Taux effectif** | **4,45 %** | **4,45 %** | **3,75 %** |

Le taux effectif ne dépasse jamais 2,50 % + 1,50 % + 0,45 % = 4,45 %, et suit la baisse de l'Euribor sous 2,50 % (Euribor + 1,95 %).

**Décomposition de la prime (0,5 pt).** Au 1er avril 2027, l'Euribor (2,65 %) dépasse le prix d'exercice (2,50 %) : le cap est **dans la monnaie**. Valeur intrinsèque = 36 000 000 × 0,15 % × 92 / 360 = **13 800 €** (ce que rapporterait l'exercice au taux du jour) ; valeur temps = 41 400 − 13 800 = **27 600 €**. La valeur temps rémunère la possibilité que l'Euribor monte d'ici au 1er juillet et au-delà ; elle est d'autant plus forte que la volatilité des taux et la durée restante sont grandes, et elle disparaît à l'échéance. La prime n'est pas à calculer : elle est donnée.

**Comparaison (1 pt).**

| Euribor constaté le 1er juillet | Sans couverture | Swap | Cap |
|---|---:|---:|---:|
| 3,60 % | 5,10 % | 4,30 % | 4,45 % |
| 2,65 % | 4,15 % | 4,30 % | 4,45 % |
| 1,80 % | 3,30 % | 4,30 % | 3,75 % |

- **Coût** : le swap ne demande aucune prime ; le cap coûte 0,45 % l'an, soit environ 162 000 € par an (41 400 € par trimestre de 92 jours). Le cap n'est moins cher que le swap que si l'Euribor descend sous **2,35 %**, soit le taux fixe du swap (2,80 %) diminué de la prime annuelle du cap ; au niveau actuel, le swap est meilleur de 0,15 point.
- **Flexibilité** : le swap est un engagement ferme : MAURVEL renonce à la baisse (92 000 € versés par trimestre si l'Euribor tombe à 1,80 %) et un dénouement anticipé se fait à la valeur de marché, négative si les taux ont baissé (question 2.4). Le cap est une option : il protège contre la hausse et laisse profiter de la baisse ; MAURVEL n'a rien d'autre à payer que la prime.
- **Risque résiduel** : avec le swap, le coût est connu (4,30 %), sous le budget de 4,50 % ; le risque qui reste est un coût d'opportunité en cas de baisse et le risque de contrepartie sur la banque (faible). Avec le cap, le coût peut monter jusqu'à 4,45 %, sous le budget, et la prime est perdue si les taux baissent ; risque de contrepartie sur les versements du cap. Dans les deux cas, la couverture s'arrête en 2032 : le refinancement du crédit à cette date reste exposé, et le nominal de 36 M€ correspond au crédit remboursable en une fois (pas de surcouverture).

**Gré à gré et marché organisé (0,5 pt).** Le swap et le cap sont des contrats **de gré à gré** négociés avec la Banque ORMESSAN : sur mesure (nominal de 36 M€, dates et durée du crédit, Euribor 3 mois), sans dépôt de garantie ni appels de marge, mais avec un **risque de contrepartie** sur la banque, une liquidité réduite (le dénouement se négocie avec elle) et un prix moins transparent. Sur un **marché organisé**, les contrats à terme et les options sur Euribor 3 mois sont **standardisés** (montant unitaire, échéances trimestrielles fixes), cotés en continu et liquides ; une chambre de compensation s'interpose entre acheteur et vendeur et supprime le risque de contrepartie, en contrepartie d'un dépôt de garantie et d'appels de marge quotidiens à financer. Les échéances standard ne coïncident pas exactement avec les dates du crédit (risque de base) et la liquidité se concentre sur les échéances les plus proches : couvrir cinq ans demanderait des contrats lointains peu liquides ou des renouvellements successifs. Pour une ETI qui couvre un crédit de cinq ans, le gré à gré est plus adapté.

**Recommandation (0,5 pt).** Le **swap** est la solution la plus adaptée : il fixe le coût du crédit à 4,30 % pendant cinq ans, sous le budget de 4,50 %, sans prime, pour un groupe qui vend à prix ferme et ne peut pas répercuter une hausse des frais financiers. Le cap ne serait préférable que si la direction anticipait une baisse marquée de l'Euribor (sous 2,35 %) ; il coûte cher parce qu'il est dans la monnaie. Une solution intermédiaire peut couvrir une partie du nominal par le swap et garder l'autre au taux variable ou sous un cap. Il est prudent de demander une offre à une autre banque, la Banque ORMESSAN concentrant déjà la trésorerie, le crédit et les financements du groupe.

**Réponses tolérées** : recommandation du cap si le candidat la justifie par une anticipation de baisse des taux et par la flexibilité, et chiffre son coût ; couverture partielle ; présentation de la charge par période de 90 jours si l'hypothèse est indiquée ; mention des options sur contrats à terme d'Euribor comme alternative, sans calcul.

**Erreurs fréquentes**
- Recevoir le taux fixe du swap, ou vendre le cap : MAURVEL est emprunteuse et craint la hausse.
- Oublier la marge de 1,50 % dans les intérêts et dans le taux effectif, ou oublier la prime du cap.
- Annualiser la prime sur 360 jours pour une seule période.
- Calculer la valeur intrinsèque avec l'Euribor d'un scénario au lieu de celui du 1er avril 2027.
- Chercher à valoriser le cap par un modèle : la prime est donnée.
- `JUR-T07` — résultats sans tableau par scénario ; `JUR-T13` — recommandation sans lien avec le prix ferme du contrat et le budget de 4,50 %.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme DSCG UE 2 (arrêté du 4 août 2025), partie 6.1 ; guide pédagogique DSCG, juillet 2026, p. 77 | centralisations de trésorerie (cash pooling notionnel ou physique), intérêt, prérequis et effets sur le coût de financement, sans traitement juridique ni fiscal ; supports de placement et de financement selon l'horizon et le couple rendement-risque ; conditions bancaires fournies | [V] | F07 § 0 et 4 ; `perimetre_ue2.yaml` (6.1.a, 6.1.b) |
| Cash pooling notionnel (fusion d'échelles) et physique | mécanismes, avantages, limites | [S] | F07 § 4.1 |
| Supports de placement à court terme (comptes à terme, OPCVM monétaires, NEU CP), affacturage, crédit renouvelable | caractéristiques usuelles | [S] | F07 § 4.2 |
| Programme DSCG UE 2, partie 7.2 ; guide pédagogique DSCG, juillet 2026, p. 81-82 | comparaison chiffrée et argumentée de solutions de financement par leur coût (frais, coût net d'IS) | [V] | `perimetre_ue2.yaml` (7.2.a) |
| Jensen et Meckling (1976) | conflits entre actionnaires et créanciers, engagements financiers | [V programme 2.1] | F10 § 3 |
| Myers et Majluf (1984) | financement hiérarchique | [V programme 7.2] | F10 § 3 |
| Programme DSCG UE 2, partie 6.2 ; guide pédagogique DSCG, juillet 2026, p. 77-78 | relation inverse valeur-taux, diagnostic d'une exposition à taux variable, swap de taux, cap (prime donnée), valeur intrinsèque et valeur temps, marchés organisés et de gré à gré ; modèles de valorisation des options exclus | [V] | F07 § 0 et 2 ; `perimetre_ue2.yaml` (6.2.a, 6.2.b, 6.2.c) |
| Swap payeur du taux fixe, cap, contrats à terme et options négociés sur un marché organisé | mécanismes et calculs | [S] | F07 § 2.2 à 2.4 |
| Euribor 3 mois 2,65 % ; €STR de l'ordre de 2,4 % | hypothèses plausibles fin 2026, posées par l'énoncé | [V] séries BCE (valeurs arrondies) | F11 § 1 |
| Soldes et conditions bancaires, règles et flux du contrat-cadre, supports, offres de financement, crédit de l'atelier, swap et cap | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 2.1 à 2.4 |
