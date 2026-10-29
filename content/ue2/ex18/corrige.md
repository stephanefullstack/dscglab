# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 18 — Dossier 3 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F04 diagnostic financier consolidé, F06 marchés et financement, F07 risques de taux et trésorerie de groupe, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (netting, FRA, coût de l'emprunt couvert, collar et tunnel à prime nulle, DFN / EBITDA et gearing, barème, liste noire, hors-programme ; frais du netting, exposition au risque de taux et endettement prévu vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple des frais après netting calculés à partir de règlements erronés à la question 3.1, ou des ratios du covenant obtenus à partir d'un endettement prévu erroné à la question 3.5).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Netting multilatéral des flux intragroupe | `6.1.a` Appliquer les mécanismes de centralisation de trésorerie | 3 |
| 3.2 Prêt bancaire ou appel direct au marché | `5.1.a` Appréhender le rôle des sources de financement (direct sur les marchés, indirect avec les intermédiaires) et le rôle des banques dans l'économie réelle ; `5.1.b` Maîtriser les enseignements des asymétries d'information (Akerlof, 1970) | 4 |
| 3.3 Exposition du groupe au risque de taux | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 2 |
| 3.4 Couverture du prêt à taux variable : FRA et collar | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux | 4 |
| 3.5 Covenant bancaire prévu fin 2027 | `1.c` Apprécier la performance opérationnelle et financière d'un groupe ; `1.a` Réaliser une analyse financière des comptes consolidés (structure financière) | 2 |
| **Total** | | **15** |

Part du calcul : environ 7 points (3.1-01 à 3.1-03, 3.3-01, 3.3-02, 3.4-02 à 3.4-04, 3.5-01 à 3.5-03, et le coût sans couverture de 3.4-01). Part de l'analyse : environ 8 points (question 3.2 entière, 3.1-04, 3.1-05, 3.3-03, 3.3-04, 3.4-05, 3.5-04). Ce dossier est le dernier de l'épreuve : la question 3.2, entièrement rédigée, et les commentaires valent plus de la moitié des points et ne doivent pas être sacrifiés faute de temps (`JUR-T15`).

---

### 3.1 Netting multilatéral des flux intragroupe (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Positions nettes : ONDÉRIS SA − 830 k€ ; Épuration Sud + 540 k€ ; Biométhane − 140 k€ ; Ressources + 430 k€ (somme nulle) | 0,5 |
| 3.1-02 | Règlements après netting (ONDÉRIS SA → Épuration Sud 540 ; ONDÉRIS SA → Ressources 290 ; Biométhane → Ressources 140) ; 15 virements et 1 630 k€ avant, 3 virements et 970 k€ après (− 660 k€, soit − 40,49 %) | 0,5 |
| 3.1-03 | Frais : 1 040 € avant, 530 € après ; économie de 510 € par mois, 6 120 € par an, 2 520 € par an nette du module | 0,5 |
| 3.1-04 | Prérequis du netting, appliqués au groupe | 0,5 |
| 3.1-05 | Limites au regard des chiffres et conclusion | 1 |

**Positions nettes (0,5 pt).** Position nette = montants à recevoir − montants à payer sur le mois.

| k€ | À recevoir | À payer | Position nette |
|---|---:|---:|---:|
| ONDÉRIS SA | 180 + 60 + 90 = 330 | 520 + 640 = 1 160 | **− 830** |
| ONDÉRIS Épuration Sud | 640 + 110 = 750 | 180 + 30 = 210 | **+ 540** |
| Valcroze Biométhane | 30 | 60 + 110 = 170 | **− 140** |
| ONDÉRIS Ressources | 520 | 90 | **+ 430** |
| **Total** | **1 630** | **1 630** | **0** |

La somme des positions est nulle : ce qu'une société du groupe paie, une autre le reçoit. ONDÉRIS SA, qui achète l'eau brute et rémunère le traitement des eaux usées, est le principal payeur net ; Valcroze Biométhane l'est aussi, pour un montant plus faible.

**Règlements et flux avant et après (0,5 pt).** La plus forte position débitrice (ONDÉRIS SA, 830) règle d'abord la plus forte position créditrice (Épuration Sud, 540), puis le reste de sa dette (290) à Ressources ; Biométhane règle ses 140 k€ à Ressources (290 + 140 = 430).

| | Nombre de virements | Montant viré (k€) |
|---|---:|---:|
| Avant netting (une facture, un virement) | 1 + 1 + 1 + 4 + 4 + 3 + 1 = 15 | 1 630 |
| Après netting | 3 | 970 |
| Réduction | − 12 (− 80 %) | − 660 (− 40,49 %) |

Avec n sociétés, le netting multilatéral ramène les règlements à n − 1 virements au plus ; le montant viré est égal à la somme des positions créditrices (540 + 430 = 970 k€).

**Économie de frais (0,5 pt).**
- Avant : 15 × 15 € + 0,05 % × 1 630 000 € = 225 + 815 = **1 040 €** par mois.
- Après : 3 × 15 € + 0,05 % × 970 000 € = 45 + 485 = **530 €** par mois.
- Économie : **510 €** par mois, soit **6 120 €** par an ; nette du module de netting (3 600 €), **2 520 €** par an.

**Prérequis (0,5 pt).**
- Une **convention de netting** signée par les quatre sociétés : périmètre des factures compensées, calendrier (date de coupure, règlement le dernier jour ouvré), rôle d'ONDÉRIS SA comme centre de compensation, règles de règlement des soldes.
- Des **factures intragroupe validées** par le payeur et le bénéficiaire avant la date de coupure (rapprochement des créances et des dettes, gestion des litiges) et un **outil partagé** (le module du logiciel de trésorerie) ; une discipline de calendrier commune aux quatre sociétés.
- L'accord d'**OSTRALE Infrastructures**, associé minoritaire de Valcroze Biométhane : le netting change les dates de règlement de la filiale et doit respecter son intérêt propre (conditions de marché, pas de financement caché des autres sociétés du groupe).

**Limites et conclusion (1 pt).**
- **Gain financier faible** : 2 520 € par an, pour près de 20 M€ de flux intragroupe annuels (12 × 1 630 k€), soit environ 0,01 %. Toutes les sociétés sont françaises et tous les flux sont en euros : le netting n'économise ici ni frais de change ni couverture, alors que c'est son principal intérêt dans un groupe international, où il réduit aussi la position de change à couvrir.
- **Décalage des règlements** : l'eau brute et le traitement des eaux usées, réglés chaque semaine, ne le seraient plus qu'une fois par mois. ONDÉRIS SA, payeur net, conserve sa trésorerie plus longtemps ; Ressources et Épuration Sud, créditrices nettes, attendent jusqu'à trois semaines de plus et voient leur besoin de trésorerie augmenter. Le groupe n'y gagne rien globalement : c'est un transfert de trésorerie entre sociétés, qui pèse sur Biométhane et ses minoritaires si les dates lui sont défavorables.
- **Le netting ne finance rien** : il réduit le nombre de règlements, pas le besoin de financement du groupe ni le coût des découverts ; il ne remplace pas la recherche des 40 M€.
- **Intérêt réel** : simplification administrative (12 virements de moins par mois, rapprochements plus simples), **visibilité** de la direction financière sur les flux du groupe, discipline de facturation interne, base d'une centralisation plus poussée de la trésorerie.
- **Conclusion** : un dispositif peu coûteux, utile pour l'organisation, dont le gain financier est marginal dans un groupe monodevise de quatre sociétés. Il est justifié si son coût reste faible et si le calendrier ne pénalise pas les filiales créditrices nettes.

**Réponses tolérées** : positions nettes présentées dans une matrice payeurs × bénéficiaires ; règlements organisés autrement (par exemple ONDÉRIS SA centralisant les règlements : Biométhane lui verse 140 k€, elle verse 540 k€ et 430 k€), si le candidat l'indique et compte les virements et les frais en cohérence (3 virements, 1 110 k€ : 600 € par mois) ; économie exprimée seulement par mois ou par an ; mention du termaillage (avance ou retard des règlements) pour les décalages de dates.

**Erreurs fréquentes**
- Calculer le montant après netting comme la somme des valeurs absolues des positions (1 940 k€) au lieu de la somme des seules positions créditrices.
- Oublier la commission proportionnelle, ou ne pas déduire le coût du module de netting.
- Présenter le netting comme une source de financement ou de rémunération des excédents (confusion avec la centralisation des soldes bancaires).
- `JUR-T07` — positions nettes calculées en ligne, sans tableau ; `JUR-T13` — avantages génériques du netting (risque de change) sans constater que le groupe est monodevise.

---

### 3.2 Prêt bancaire ou appel direct au marché (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Financement intermédié et financement direct : caractéristiques et coûts, appliqués aux deux offres | 0,5 |
| 3.2-02 | Rôle des banques dans l'économie réelle (production d'information, contrôle, transformation, relation de long terme), appliqué à ONDÉRIS | 1 |
| 3.2-03 | Asymétries d'information : sélection adverse (Akerlof, 1970), aléa moral, signal, et leurs conséquences pour le choix d'ONDÉRIS | 1 |
| 3.2-04 | Banque SORNAY actionnaire et chef de file : avantage informationnel et conflits d'intérêts | 1 |
| 3.2-05 | Recommandation argumentée | 0,5 |

**Financement intermédié et financement direct (0,5 pt).**
- **Prêt bancaire (financement indirect)** : la banque collecte des ressources (dépôts, épargne) et prête à son propre risque ; relation bilatérale de long terme, contrat négocié (covenants, information trimestrielle), conditions ajustables en cours de vie. Coût : marge de 1,40 % sur l'Euribor 3 mois. Taux de la première période aux conditions actuelles : 4,05 % ; commission d'arrangement de 0,40 % (160 000 €) ; le taux est variable.
- **Émission obligataire (financement direct)** : ONDÉRIS lève les fonds directement auprès d'investisseurs (assureurs, fonds de dette), qui portent le risque ; l'arrangeur ne prête pas, il organise l'émission. Coût : taux fixe de 4,30 % et frais de 0,90 % (360 000 €) ; documentation détaillée et présentation aux investisseurs ; remboursement in fine sur 10 ans, contre 15 ans amortissables pour le prêt. Une émission cotée est hors de portée (notation et 250 M€ au moins, plus de six fois le besoin) : seul un placement auprès de quelques investisseurs est possible.
- **Critères de choix** : la taille du groupe (156 M€ de chiffre d'affaires), l'absence de notation et le montant (40 M€) le situent du côté du financement intermédié ; l'appel au marché reste ouvert pour un placement privé, à un coût fixe plus élevé.

**Rôle des banques dans l'économie réelle (1 pt).**
- **Production d'information** : la banque évalue le risque de l'emprunteur avant de prêter, à partir d'informations privées issues de la relation (comptes des sociétés, flux sur les comptes, connaissance du secteur et des collectivités). Les trois banques du pool connaissent déjà ONDÉRIS, dont elles financent la dette actuelle (152 M€ bruts) : elles prêtent sans exiger la documentation lourde d'une émission.
- **Contrôle (surveillance)** : après le prêt, la banque surveille l'emprunteur pour le compte de ses déposants : covenants (DFN / EBITDA ≤ 4,00, gearing ≤ 130 %), situation trimestrielle, suivi de l'avancement des investissements. Ce contrôle délégué évite que chaque prêteur ait à surveiller l'entreprise.
- **Transformation** : la banque prête sur 15 ans des ressources collectées à plus court terme ; elle accepte un amortissement progressif après un différé de deux ans, adapté à des ouvrages qui produisent leurs flux pendant des décennies.
- **Relation de long terme et souplesse** : en cas de difficulté (sécheresse, retard de travaux, covenant tendu, question 3.5), trois banques connues peuvent renégocier une échéance ou un seuil ; une dizaine de porteurs d'obligations, beaucoup plus difficilement (accord d'une majorité).
- Les banques financent ainsi les entreprises qui n'ont pas accès aux marchés cotés ou qui n'y accèdent qu'à un coût élevé (PME, ETI non notées, entités de taille moyenne comme ONDÉRIS).

**Asymétries d'information (1 pt).**
- **Sélection adverse** (Akerlof, 1970) : avant le contrat, les investisseurs qui ne connaissent pas le groupe ne distinguent pas une bonne signature d'une mauvaise ; ils exigent une prime de risque moyenne, trop chère pour une bonne entreprise, ou se retirent (rationnement). Pour les convaincre, ONDÉRIS doit produire une documentation détaillée, se présenter aux investisseurs et payer 0,90 % de frais : c'est le coût de la réduction de cette asymétrie. La banque, qui connaît ONDÉRIS, la réduit à moindre coût (0,40 %).
- **Aléa moral** : après le contrat, l'emprunteur peut prendre plus de risques que prévu (investissements non prévus, dividendes, endettement supplémentaire) au détriment des prêteurs. Les covenants, l'information trimestrielle et le suivi des travaux du prêt bancaire limitent ce risque ; l'émission ne prévoit qu'un covenant plus lâche (DFN / EBITDA ≤ 4,50) et une information annuelle. Ce conflit entre actionnaires et créanciers est l'un des coûts d'agence décrits par Jensen et Meckling (1976).
- **Signal** : le choix du financement informe les tiers. L'endettement est un signal de confiance dans les flux futurs (Ross, 1977) ; l'obtention d'un prêt de banques qui connaissent le groupe et qui acceptent d'en porter le risque **certifie** sa qualité auprès des autres partenaires. Le financement hiérarchique (Myers et Majluf, 1984), qui découle aussi de l'asymétrie d'information, place la dette avant l'émission d'actions : le recours à l'emprunt plutôt qu'à une augmentation de capital est cohérent avec cette logique.
- **Conséquence pour ONDÉRIS** : groupe non noté, inconnu des investisseurs, au métier régulier mais dont le prix est fixé avec la métropole : l'asymétrie d'information est forte vis-à-vis du marché, faible vis-à-vis de ses banques ; le financement intermédié est le moins coûteux pour la réduire.

**Banque SORNAY, actionnaire et chef de file (1 pt).**
- **Avantage informationnel** : actionnaire à 12 %, administratrice et membre du comité d'audit, la Banque SORNAY connaît le groupe de l'intérieur (budgets, programme d'investissement, risques). Elle peut évaluer le prêt plus vite et mieux que les autres prêteurs et accepter des conditions plus favorables : l'asymétrie d'information est presque nulle pour elle. Sa présence rassure les deux autres banques (effet de certification).
- **Conflits d'intérêts** :
  - entre ses rôles de **prêteur et d'actionnaire** : comme prêteur, elle préfère un groupe peu risqué, peu distributeur et des covenants serrés ; comme actionnaire, elle profite d'un rendement plus élevé ; au conseil, ses votes sur le programme d'investissement ou les dividendes peuvent servir l'un ou l'autre intérêt ;
  - entre son rôle d'**administrateur et de conseil intéressé** : elle perçoit la commission d'arrangement (160 000 €), les intérêts sur 40 % du prêt et demande la domiciliation de la moitié des encaissements du groupe : elle a intérêt à recommander le prêt bancaire plutôt que l'émission, et à capter les flux du groupe, ce qui réduit la mise en concurrence des banques ;
  - vis-à-vis des **autres banques du pool** : elle détient une information privilégiée qu'elles n'ont pas (asymétrie entre prêteurs) ; en cas de difficulté, elle pourrait utiliser cette information pour se protéger en priorité.
- **Mesures de gouvernance** : le représentant de la banque ne prend part ni aux délibérations ni au vote du conseil sur le choix du financement et sur les conditions du prêt ; mise en concurrence avec l'offre de marché et d'autres banques ; information égale de tous les prêteurs ; refus ou limitation de la domiciliation exclusive des encaissements.

**Recommandation (0,5 pt).** Le **prêt bancaire** est le mieux adapté : montant trop faible et groupe non noté pour un appel au marché coté, asymétrie d'information réduite par des banques qui connaissent le groupe, amortissement sur 15 ans plus cohérent avec la durée des ouvrages qu'un remboursement in fine sur 10 ans, frais deux fois plus faibles, possibilité de renégocier. Il présente deux inconvénients : un **taux variable**, qu'il faut couvrir (questions 3.3 et 3.4), et des **covenants plus stricts**, à vérifier (question 3.5). Le conflit d'intérêts de la Banque SORNAY doit être encadré (abstention au conseil, mise en concurrence, domiciliation négociée). L'émission obligataire reste un **complément** à envisager plus tard pour diversifier les prêteurs et allonger la dette, quand l'endettement du groupe aura atteint une taille suffisante.

**Réponses tolérées** : recommandation de l'émission obligataire si le candidat la justifie par le taux fixe (absence de risque de taux), la diversification des prêteurs, le covenant moins strict et l'indépendance vis-à-vis de la Banque SORNAY, et s'il en mesure le coût et les contraintes ; recommandation mixte (une partie en prêt, une partie en placement privé) ; mention de Spence (1973) pour la théorie du signal en général ; présentation des trois rôles des banques sous d'autres termes (sélection et surveillance des emprunteurs, transformation des échéances, mutualisation des risques).

**Erreurs fréquentes**
- Confondre sélection adverse (avant le contrat, Akerlof) et aléa moral (après le contrat).
- Présenter l'arrangeur de l'émission comme un prêteur, ou l'émission comme un financement intermédié.
- Développer le régime juridique des sociétés d'économie mixte ou des emprunts des collectivités : le sujet ne le demande pas.
- `JUR-M01` — analyse sans les théories attendues (asymétrie d'information, agence, signal) ; `JUR-T02` et `JUR-T13` — théories récitées sans les données du cas (12 % du capital, siège au conseil, 40 % du pool, domiciliation demandée, absence de notation, seuil de 250 M€).

---

### 3.3 Exposition du groupe au risque de taux (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Part de la dette brute à taux variable : 36,84 % avant le prêt, 50,00 % après | 0,5 |
| 3.3-02 | Hausse de 100 points de base : + 960 000 € d'intérêts, + 100 000 € de produits de trésorerie en déduction, soit + 860 000 € avant IS et + 645 000 € après IS | 0,5 |
| 3.3-03 | Dette à taux fixe : charge inchangée, valeur de marché en baisse (relation inverse valeur-taux) ; lecture du coût d'opportunité | 0,5 |
| 3.3-04 | Caractérisation de l'exposition : risque principal de hausse, risque sur les flux et non sur la valeur pour la dette variable, contrainte du prix de l'eau ; besoin de couverture | 0,5 |

**Part à taux variable (0,5 pt).**

| M€ | Au 31/12/2026 | Après le prêt de 40 M€ |
|---|---:|---:|
| Dette à taux fixe | 96 | 96 |
| Dette à taux variable | 56 | 56 + 40 = 96 |
| Dette financière brute | 152 | 192 |
| **Part à taux variable** | **56 / 152 = 36,84 %** | **96 / 192 = 50,00 %** |

**Effet d'une hausse de 100 points de base (0,5 pt).** Sur une année pleine :
- intérêts de la dette à taux variable : 96 000 000 × 1 % = **+ 960 000 €** de charges ;
- produits de la trésorerie placée à des taux qui suivent l'Euribor : 10 000 000 × 1 % = **+ 100 000 €** de produits ;
- effet net : **+ 860 000 €** de charge d'intérêts nette avant IS, **+ 645 000 €** après IS (860 000 × 0,75). La position nette exposée est de 96 − 10 = 86 M€.

Pour un ordre de grandeur, ces 0,86 M€ représentent 2,26 % de l'EBITDA de 2026 (38 M€) et 14,33 % des frais financiers nets prévus en 2027 (6 M€, annexe 3.4).

**Dette à taux fixe (0,5 pt).** La hausse des taux ne change pas sa charge d'intérêts : le taux de 3,10 % est contractuel. Mais sa **valeur de marché baisse** : la valeur d'une dette est la somme de ses flux futurs actualisés au taux du marché, qui monte (relation inverse valeur-taux). Déjà, au taux de 4,30 % que le groupe paierait aujourd'hui pour une dette fixe nouvelle, ses emprunts à 3,10 % valent moins que leur nominal : le groupe bénéficie d'un financement bon marché, qu'une hausse des taux rend plus avantageux encore. Ce gain est latent (le groupe rembourse le nominal) ; à l'inverse, une **baisse** des taux augmenterait la valeur de la dette fixe : le groupe paierait plus cher que le marché (coût d'opportunité) et un remboursement anticipé pour se refinancer serait pénalisé.

**Caractérisation de l'exposition (0,5 pt).** Après le prêt, le groupe est **emprunteur net à taux variable** (86 M€ nets) : son risque principal est la **hausse** de l'Euribor, qui augmente ses charges (risque sur les flux), sans effet sur la valeur de la dette variable, révisée chaque trimestre ; la dette fixe expose à l'inverse à un risque de valeur et de coût d'opportunité en cas de baisse. Le risque est aggravé par deux traits du cas : le **prix de l'eau**, fixé chaque année avec la métropole, ne peut pas répercuter immédiatement une hausse des frais financiers, et le covenant DFN / EBITDA est tendu (question 3.5). La moitié variable de la dette, et d'abord le nouveau prêt, doit donc être couverte au moins en partie contre la hausse (question 3.4).

**Réponses tolérées** : part variable calculée en dette nette (86 / 182 = 47,25 %) si le candidat le précise ; effet de la hausse calculé sur la seule dette variable (960 000 €) si l'effet sur la trésorerie placée est mentionné, item 3.3-02 accordé pour moitié sinon ; effet après IS non calculé mais signalé ; estimation de la variation de valeur de la dette fixe non demandée.

**Erreurs fréquentes**
- Appliquer la hausse des taux à la dette à taux fixe pour calculer une hausse des charges.
- Conclure que la hausse des taux « fait perdre de la valeur » au groupe sur sa dette fixe : elle réduit la valeur d'une dette, ce qui est favorable à l'emprunteur.
- Oublier le nouveau prêt de 40 M€ dans la dette à taux variable.
- `JUR-T07` — exposition décrite sans tableau fixe / variable.

---

### 3.4 Couverture du prêt à taux variable : FRA et collar (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Risque de hausse ; positions justifiées : achat du FRA, achat du cap et vente du floor ; coût sans couverture : 515 000, 430 000 et 330 000 € (5,15 %, 4,30 %, 3,30 %) | 0,5 |
| 3.4-02 | FRA : différentiel de + 95 000, + 10 000 et − 90 000 € ; coût net de 420 000 €, taux effectif de 4,20 % dans les trois scénarios | 1 |
| 3.4-03 | Collar : prime nette de 10 000 € par période ; bornes du taux effectif 3,75 % et 4,75 % ; tunnel à prime nulle : 3,90 % et 4,65 % | 0,5 |
| 3.4-04 | Collar : versement du cap de 50 000 € (scénario haut), du floor de 35 000 € (scénario bas) ; coût net de 475 000, 440 000 et 375 000 € ; taux effectif de 4,75 %, 4,40 % et 3,75 % | 1 |
| 3.4-05 | Comparaison (coût, flexibilité, risque résiduel, durée de la protection) et recommandation | 1 |

**Risque et positions (0,5 pt).** ONDÉRIS paiera sur 40 M€ un taux variable, constaté le 1er juillet ; elle craint la **hausse** de l'Euribor. Elle **achète** le FRA (elle reçoit le différentiel si le taux constaté dépasse le taux garanti) et met en place un collar en **achetant** un cap (elle reçoit la différence au-dessus de 3,25 %) et en **vendant** un floor (elle verse la différence sous 2,25 %, ce qui finance une partie de la prime du cap).

Sans couverture, intérêts = 40 000 000 × (taux constaté + 1,40 %) × 90 / 360 :

| Taux constaté le 1er juillet | 3,75 % | 2,90 % | 1,90 % |
|---|---:|---:|---:|
| Taux de l'emprunt (constaté + 1,40 %) | 5,15 % | 4,30 % | 3,30 % |
| Intérêts de la période (€) | 515 000 | 430 000 | 330 000 |

**FRA (1 pt).** Différentiel réglé le 29 septembre = 40 000 000 × (taux constaté − 2,80 %) × 90 / 360.

| FRA acheté à 2,80 % | 3,75 % | 2,90 % | 1,90 % |
|---|---:|---:|---:|
| Intérêts du prêt | 515 000 | 430 000 | 330 000 |
| Différentiel : reçu (+) ou versé (−) | + 95 000 | + 10 000 | − 90 000 |
| **Coût net** | **420 000** | **420 000** | **420 000** |
| **Taux effectif** | **4,20 %** | **4,20 %** | **4,20 %** |

Le FRA fixe le coût de la période à 2,80 % + 1,40 % = 4,20 %, quel que soit le taux constaté : il protège contre la hausse et fait renoncer au bénéfice de la baisse (90 000 € versés dans le scénario bas).

**Collar : prime nette et bornes (0,5 pt).** Prime nette = (0,30 % − 0,20 %) × 40 000 000 × 90 / 360 = **10 000 €** par période, soit 0,10 % l'an. Taux effectif :
- maximal (taux constaté au-dessus de 3,25 %) : 3,25 % + 1,40 % + 0,10 % = **4,75 %** ;
- minimal (taux constaté au-dessous de 2,25 %) : 2,25 % + 1,40 % + 0,10 % = **3,75 %** ;
- tunnel à prime nulle (floor vendu à 2,50 %) : entre 2,50 % + 1,40 % = **3,90 %** et 3,25 % + 1,40 % = **4,65 %**, sans prime.

**Collar : résultats (1 pt).**

| Collar 2,25 % - 3,25 % | 3,75 % | 2,90 % | 1,90 % |
|---|---:|---:|---:|
| Intérêts du prêt | 515 000 | 430 000 | 330 000 |
| Versement reçu du cap : 40 000 000 × (taux − 3,25 %) × 90 / 360 | − 50 000 | 0 | 0 |
| Versement payé au floor : 40 000 000 × (2,25 % − taux) × 90 / 360 | 0 | 0 | + 35 000 |
| Prime nette | + 10 000 | + 10 000 | + 10 000 |
| **Coût net** | **475 000** | **440 000** | **375 000** |
| **Taux effectif** | **4,75 %** | **4,40 %** | **3,75 %** |

Entre les bornes (2,90 %), aucune option n'est exercée : le groupe paie le taux du marché majoré de la prime nette (4,30 % + 0,10 %).

**Comparaison et recommandation (1 pt).**

| Taux constaté le 1er juillet | Sans couverture | FRA | Collar | Tunnel à prime nulle |
|---|---:|---:|---:|---:|
| 3,75 % | 5,15 % | 4,20 % | 4,75 % | 4,65 % |
| 2,90 % | 4,30 % | 4,20 % | 4,40 % | 4,30 % |
| 1,90 % | 3,30 % | 4,20 % | 3,75 % | 3,90 % |

- **Coût** : le FRA ne coûte rien à la mise en place, mais fait renoncer à toute baisse ; le collar coûte une prime nette faible (10 000 € par trimestre, 0,10 % l'an), réduite par la vente du floor, et nulle pour le tunnel. Le collar est moins cher que le FRA tant que le taux constaté reste inférieur à 2,70 % (2,80 % − 0,10 %) ; au-dessus, le FRA est meilleur sur la période.
- **Flexibilité** : le FRA est un engagement ferme ; le collar laisse profiter de la baisse jusqu'au plancher, mais au-dessous le groupe paie au moins 3,75 % (3,90 % pour le tunnel) : la vente du floor abandonne l'essentiel de la baisse. Le tunnel à prime nulle, avec un plancher plus haut, protège au même plafond pour un coût nul, mais renonce à davantage de baisse.
- **Risque résiduel** : avec le FRA, nul sur la première période, mais **total sur les onze périodes suivantes**, puisque le FRA ne couvre qu'un trimestre (il faudrait une série de FRA, ou un autre instrument, pour couvrir les années suivantes) ; avec le collar, le groupe supporte la hausse de l'Euribor jusqu'au plafond, son taux effectif pouvant monter jusqu'à 4,75 %, mais ce coût maximal est connu pour trois ans. Le collar porte sur un nominal constant de 40 M€, alors que le prêt s'amortit après le différé de deux ans : la troisième année, il couvre un peu plus que l'encours (environ 37 à 40 M€), et le floor vendu porte en partie sur un montant qui n'est plus emprunté ; un collar à nominal amortissable éviterait cette surcouverture. Les deux instruments sont de gré à gré avec la Banque SORNAY : risque de contrepartie sur la banque, faible, et dépendance accrue à l'égard d'une banque déjà actionnaire et prêteuse (question 3.2).
- **Recommandation** : le collar (ou le tunnel à prime nulle) sur trois ans est la solution la plus adaptée : le groupe connaît son coût maximal (4,75 % ou 4,65 %) pendant la phase la plus lourde du programme d'investissement, alors qu'il ne peut pas répercuter une hausse des frais financiers sur le prix de l'eau et que son covenant est tendu (question 3.5) ; il garde une partie de la baisse. Le FRA seul ne protège qu'un trimestre : il ne convient que si la direction veut fixer immédiatement le coût de la première période, ou en complément. Il est prudent de comparer les primes proposées par la Banque SORNAY à celles d'une autre banque.

**Réponses tolérées** : recommandation du FRA (renouvelé chaque trimestre) si le candidat souligne l'absence de protection au-delà du premier trimestre ; préférence motivée pour le tunnel à prime nulle ou pour le collar ; couverture d'une partie seulement du nominal ; mention d'autres instruments (swap de taux, cap seul) comme alternatives, sans calcul ; points morts exprimés en coût de la période plutôt qu'en taux.

**Erreurs fréquentes**
- Vendre le FRA, ou acheter le floor, comme un prêteur : ONDÉRIS est emprunteuse et craint la hausse.
- Oublier la marge de 1,40 % dans les intérêts et dans les bornes du taux effectif, ou oublier la prime nette.
- Croire que le FRA porte sur le prêt : seul le différentiel est réglé, le prêt reste au taux variable.
- Chercher à calculer la valeur des options : les primes sont données.
- `JUR-T07` — résultats des couvertures sans tableau par scénario ; `JUR-T13` — recommandation sans lien avec la durée du prêt, le prix de l'eau et le covenant.

---

### 3.5 Covenant bancaire prévu fin 2027 (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Résultat net 2027 de 9 M€ ; DFN au 31/12/2027 de 156 M€ ; capitaux propres de 133 M€ | 0,5 |
| 3.5-02 | DFN / EBITDA = 3,90 ≤ 4,00 ; gearing = 117,29 % ≤ 130 % : seuils respectés (comparaison avec 2026 : 3,74 et 112,70 %) | 0,5 |
| 3.5-03 | Marge de manœuvre : 4 M€ de DFN ou 1 M€ d'EBITDA (2,5 %) pour le premier ratio ; 16,9 M€ de DFN pour le gearing | 0,5 |
| 3.5-04 | Lecture et mesures pour préserver la marge | 0,5 |

**Endettement et capitaux propres prévus (0,5 pt).**

| M€ | 2027 |
|---|---:|
| EBITDA | 40 |
| − Impôt | − 3 |
| − Augmentation du BFR | − 1 |
| − Frais financiers nets | − 6 |
| − Dividendes versés | − 2 |
| = Flux disponible avant investissements | 28 |
| − Investissements | − 42 |
| = **Augmentation de l'endettement financier net** | **14** |

- DFN au 31/12/2027 = 142 + 42 − 28 = **156 M€** (le prêt de 40 M€ augmente la dette brute, mais il est dépensé : c'est l'investissement non autofinancé qui fait monter la DFN).
- Résultat net 2027 = (40 − 22 − 6) × 0,75 = **9 M€** (l'impôt de 3 M€ de l'annexe est cohérent : 12 × 25 %).
- Capitaux propres au 31/12/2027 = 126 + 9 − 2 = **133 M€**.

**Ratios et seuils (0,5 pt).**

| | 31/12/2026 | 31/12/2027 prévu | Seuil |
|---|---:|---:|---:|
| DFN / EBITDA | 142 / 38 = 3,74 | 156 / 40 = **3,90** | ≤ 4,00 |
| Gearing (DFN / capitaux propres) | 142 / 126 = 112,70 % | 156 / 133 = **117,29 %** | ≤ 130 % |

Les deux seuils seraient respectés fin 2027, mais les deux ratios se dégradent : la dette augmente plus vite que l'EBITDA et que les capitaux propres, parce que le programme d'investissement n'est autofinancé qu'aux deux tiers (28 / 42).

**Marge de manœuvre (0,5 pt).**
- DFN / EBITDA : avec un EBITDA de 40 M€, la DFN peut atteindre 4,00 × 40 = 160 M€, soit **4 M€** de plus seulement ; à DFN de 156 M€, l'EBITDA ne doit pas descendre sous 156 / 4 = 39 M€, soit une baisse de **1 M€ (− 2,5 %)**.
- Gearing : la DFN peut atteindre 1,30 × 133 = 172,9 M€, soit **16,9 M€** de plus : ce ratio n'est pas contraignant.

**Lecture et mesures (0,5 pt).** La marge du covenant DFN / EBITDA est **très faible** : une sécheresse qui ferait baisser les volumes vendus, un retard de facturation, un dépassement du budget d'investissement de 4 M€ ou une hausse des taux non couverte (+ 0,65 M€ de charges après IS pour 100 points de base, question 3.3) suffiraient à approcher le seuil, ce qui permettrait aux banques d'exiger le remboursement anticipé du prêt. Mesures possibles : étaler une partie des investissements de 2027 (le programme court jusqu'en 2031) ; réduire ou suspendre le dividende pendant le programme ; couvrir le risque de taux (question 3.4) ; négocier avec le pool un seuil plus élevé (4,50, comme l'offre obligataire) pendant la période de travaux ou un test sur un EBITDA moyen ; suivre le ratio chaque trimestre et prévenir les banques en amont. La relation de long terme avec les banques (question 3.2) rend cette négociation plus facile qu'avec des porteurs d'obligations.

**Réponses tolérées** : DFN obtenue par un tableau de flux plus détaillé (capacité d'autofinancement, variation du BFR, investissements, dividendes, variation de la dette nette) avec le même résultat ; gearing exprimé en multiple (1,17) ; marge de manœuvre exprimée seulement en EBITDA ou seulement en dette ; DFN de 2027 augmentée par erreur des 40 M€ du prêt (196 M€, ratio de 4,90) : item 3.5-01 non accordé, items suivants notés en cohérence.

**Erreurs fréquentes**
- Ajouter le prêt de 40 M€ à la DFN sans tenir compte de sa dépense en investissements, ou l'ajouter en plus des investissements.
- Calculer le gearing sur les seuls capitaux propres part du groupe alors que le covenant porte sur les capitaux propres consolidés, intérêts minoritaires compris.
- Conclure au respect du covenant sans mesurer la marge.
- `JUR-T13` — mesures générales sans lien avec le programme d'investissement, le dividende et le risque de sécheresse.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme DSCG UE 2 (arrêté du 4 août 2025), partie 6.1 ; guide pédagogique DSCG, juillet 2026, p. 77 | centralisations de trésorerie, opérations intragroupe (netting, cash pooling) ; intérêt, schémas usuels, prérequis, sans traitement juridique ni fiscal | [V] | F07 § 0 ; `perimetre_ue2.yaml` (6.1.a) |
| Netting bilatéral et multilatéral | positions nettes, réduction des règlements et des frais, centre de compensation | [S] | F07 § 3 et 4 |
| Programme DSCG UE 2, partie 5.1 ; guide pédagogique DSCG, juillet 2026, p. 72-73 | financement direct et indirect, rôle des banques, coûts du financement de marché ou intermédié, choix selon la taille et la notation ; asymétries d'information, sans démonstration du modèle | [V] | F06 § 1 et 2 ; `perimetre_ue2.yaml` (5.1.a, 5.1.b) |
| Production d'information, contrôle et transformation par les banques | lecture usuelle du rôle des intermédiaires | [S] | F06 § 1 |
| Akerlof (1970) | sélection adverse, prime de risque, rationnement du crédit | [V programme 5.1] | F10 § 1 |
| Jensen et Meckling (1976) | coûts d'agence, conflits entre actionnaires et créanciers | [V programme 2.1] | F10 § 3 |
| Ross (1977) ; Spence (1973) | signal par l'endettement ; théorie du signal | [V programme 4.1] | F10 § 3 |
| Myers et Majluf (1984) | financement hiérarchique | [V programme 7.2] | F10 § 3 |
| Programme DSCG UE 2, partie 6.2 ; guide pédagogique DSCG, juillet 2026, p. 77-78 | relation inverse valeur-taux ; diagnostic d'une exposition à taux fixe ou variable ; FRA, cap, floor, collar, primes données ; choix d'une couverture selon le coût, la flexibilité et le risque résiduel | [V] | F07 § 0 et 2 ; `perimetre_ue2.yaml` (6.2.a, 6.2.b) |
| FRA (différentiel), cap, floor, collar, tunnel à prime nulle | mécanismes et calculs | [S] | F07 § 2 |
| Programme DSCG UE 2, partie 1 ; corrigé du sujet zéro, p. 104 | structure financière, DFN / EBITDA (seuil d'alerte bancaire de l'ordre de 3 fois l'EBITDA), gearing | [V] | F04 § 4 |
| Euribor 3 mois 2,65 % | hypothèse plausible fin 2026, posée par l'énoncé | [V] séries BCE (valeur arrondie) | F11 § 1 |
| Flux intragroupe, offres de financement, dette, instruments de couverture, prévisions 2027 | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 3.1 à 3.4 |
