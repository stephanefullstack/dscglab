# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 3 – Contrôle de gestion et stratégie — Exercice d'entraînement n° 69 — Dossier 2 (7 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F06 pilotage des processus support et approvisionnements (§ 0, compétences 2.3.a à 2.3.g ; § 2, modèle de Wilson ; § 5, stock de sécurité et point de commande ; § 6, plannings d'approvisionnement ; § 7, processus support ; § 8, pièges), F08 gestion des risques (§ 0 ; § 1, typologie ; § 2.1, criticité et traitement ; § 5, gabarit de réponse), F09 ressources humaines (GEPP), F12 performance globale (§ 3, tableaux de bord), F13 registre des auteurs (toutes à jour au 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (quantité économique d'illustration recalculée ; plannings des deux politiques et planning avec une livraison retardée recalculés, ruptures et mois sous le stock de sécurité déclarés ; mois sans rupture et occupation du magasin recalculés comme indicateurs ; consommations, capacité du magasin, coûts des politiques, criticités et coûts des pistes recalculés par script ; barème partiel sur 7 ; liste noire ; hors-programme).

Bien que le corrigé mentionne des auteurs, des textes et des données, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur le choix et la justification des outils, la justesse des calculs, la pertinence de l'analyse au regard du cas et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet) ; pour chaque question, la présentation des concepts et outils avant leur mobilisation puis la conclusion sont notées. Une erreur n'est sanctionnée qu'une fois : les calculs et les analyses qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Processus de maintenance et d'approvisionnement en semelles : place parmi les activités, enjeux de coût, de délai, de qualité et de continuité, causes des incidents de 2027 ; outil adapté à une consommation saisonnière et limites d'une quantité économique annuelle | `2.3.a` Analyser la situation de gestion ; `2.3.b` Sélectionner des outils de gestion adaptés à l'organisation | 1,5 |
| 2.2 Consommations de mai à décembre 2028, plannings des deux politiques (commandes, livraisons, stocks), ruptures, mois sous le stock de sécurité, capacité du magasin, coût de chaque politique et choix au regard du service rendu | `2.3.d` Mettre en œuvre ces outils ; `2.3.e` Évaluer les résultats obtenus | 2,5 |
| 2.3 Criticité des six risques du processus, hiérarchie, matrice et lien avec les plannings | `2.5.b` Analyser les risques rencontrés par l'organisation | 1 |
| 2.4 Note au directeur administratif et financier et au directeur des opérations (20 lignes au maximum) | `2.3.f` Élaborer des préconisations afin de mieux piloter la performance des activités hors production ; `2.3.g` Produire une synthèse rédigée et structurée concernant les décisions liées aux processus support ; `2.5.e` Produire une synthèse rédigée et structurée sur la gestion des risques | 2 |
| **Dossier 2 – Fiabiliser la maintenance des locomotives : processus d'approvisionnement, planning de deux politiques de commande et risques** | | **7** |

---

## DOSSIER 2 – FIABILISER LA MAINTENANCE DES LOCOMOTIVES : PROCESSUS D'APPROVISIONNEMENT, PLANNING DE DEUX POLITIQUES DE COMMANDE ET RISQUES (7 points)

### 2.1 Le processus de maintenance et d'approvisionnement, et l'outil adapté (1,5 pt)

**Compétences visées :**
- `2.3.a` — Analyser la situation de gestion (place du processus support, enjeux, causes des incidents de 2027)
- `2.3.b` — Sélectionner des outils de gestion adaptés à l'organisation (planning d'approvisionnement plutôt qu'une quantité économique annuelle)

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Processus présenté puis situé : la **production** de TERNAVAL Fret est la traction des trains ; la maintenance des locomotives et l'approvisionnement de son magasin sont des **processus support**, dont le client interne est l'exploitation (le nombre de locomotives demandé chaque matin) ; chaîne de valeur de Porter (1985) : approvisionnements parmi les activités de soutien ; ce support est **critique** ici, parce qu'une semelle manquante immobilise une locomotive et fait perdre un train pendant la campagne (38 trains de céréales perdus en 2027), alors que le plan « TERNAVAL 2031 » fait de la fiabilité avant la campagne de 2028 son deuxième axe | 0,5 |
| 2.1-02 | Enjeux et causes : **coût** (possession de 24 € par semelle et par an, 30 % du prix ; rupture de 1 500 € par mois et 200 € par semelle manquante, sans commune mesure) ; **délai** (deux mois, fournisseur unique étranger qui fabrique par séries) ; **qualité** (semelle conforme au modèle, sécurité des circulations, contrôle à l'arrivée) ; **continuité** (une locomotive dont la visite attend ses pièces ne repart pas ; en campagne, chaque locomotive passe à l'atelier chaque mois) ; causes de 2027 : commandes constantes, égales au douzième de la consommation annuelle, face à une consommation saisonnière (**68,33 %** des semelles de l'année consommées de juillet à novembre ; 90 en septembre contre 25 en mars, **3,6 fois plus**), d'où un magasin qui déborde au printemps et des ruptures à l'automne ; délai long sans prévision des besoins ; stock mal suivi | 0,5 |
| 2.1-03 | Outil justifié : **planning d'approvisionnement** mensuel (besoins déduits du programme des kilomètres, stock de sécurité, délai, capacité, règle de lancement) ; limites de la quantité économique de Wilson montrées, au moins par le raisonnement : demande supposée régulière, délai et capacité ignorés ; calcul d'illustration accepté (**Q\* = 100 semelles, 6 commandes par an, une tous les 60 jours, 2 400 €**) : un lot de 100 couvre 5 mois en janvier mais 1,11 mois en septembre, moins que le délai de deux mois ; un point de commande fixe (130 semelles en moyenne) est trop haut l'hiver (70) et trop bas en pointe (210) | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **planning d'approvisionnement**, c'est-à-dire la programmation, mois par mois, des besoins, des commandes, des livraisons et des stocks, avec un stock de sécurité, un délai de livraison et une capacité de stockage. Il est adapté parce que la consommation est **connue à l'avance mais irrégulière** : elle se déduit du programme des kilomètres, qui triple pendant la campagne. Il permet aussi de tenir compte d'un délai de deux mois et d'un magasin limité. Deux logiques sont possibles : des quantités constantes commandées à des dates variables (lots fixes déclenchés par le stock prévisionnel, la proposition de M. VERLOMBE), ou des dates fixes avec des quantités variables (recomplètement).
- Alternatives acceptées : un raisonnement par le point de commande (consommation pendant le délai + stock de sécurité), à condition de le recalculer mois par mois d'après le programme ; une quantité économique de Wilson **utilisée seulement pour dimensionner le lot**, son déclenchement restant celui du planning. Non accepté : une quantité économique annuelle présentée comme la solution, avec des commandes régulières tous les 60 jours ; un modèle avec pénurie admise, qui supposerait que l'exploitation accepte d'attendre ses locomotives.

**Conventions rappelées** (annexes 2.1 à 2.3)

1 semelle par millier de kilomètres ; consommation annuelle 600 semelles ; coût de passation 200 € ; coût de possession 2 € par semelle et par mois, soit 24 € par an ; année de 360 jours ; délai de deux mois ; stock de sécurité de 30 semelles.

**Calculs détaillés** (illustration des limites)

*Saisonnalité.* Consommation de 2028 = 600 000 km / 1 000 = **600 semelles**, soit 50 par mois en moyenne ; de juillet à novembre, 410 semelles, soit **68,33 %** de l'année en cinq mois. Moyenne mensuelle de la campagne : 82 semelles, contre 27,14 hors campagne (rapport de 3,02) ; septembre (90) contre mars (25) : 3,6.

*Quantité économique sur la consommation annuelle supposée régulière.* Q\* = √(2 × 600 × 200 / 24) = **100 semelles** ; nombre de commandes = 600 / 100 = **6** ; périodicité = 360 / 6 = **60 jours** ; coût de gestion = √(2 × 600 × 200 × 24) = **2 400 €** (1 200 € de passation, 1 200 € de possession).

*Ce que ce résultat ne dit pas.* Un lot de 100 semelles couvre 100 / 20 = 5 mois de consommation en janvier, mais 100 / 90 = **1,11 mois** en septembre, moins que le délai de livraison de deux mois. Un point de commande fixe calculé sur la moyenne vaut 50 × 2 + 30 = **130 semelles** ; il faudrait 20 + 20 + 30 = 70 semelles en hiver, mais 90 + 90 + 30 = **210** pour couvrir deux mois de pointe. Le stock de sécurité de 30 semelles ne représente que 10 jours de consommation de pointe.

**Réponse attendue**

*Concepts.* Un processus est un enchaînement d'activités qui produit un résultat pour un client, interne ou externe. Un processus de production réalise l'offre vendue ; un processus support fournit les ressources dont il a besoin. La distinction dépend de l'organisation : la logistique est un processus de production chez un transporteur. Dans la chaîne de valeur de Porter (1985), les approvisionnements figurent parmi les activités de soutien. La gestion des approvisionnements arbitre entre les coûts de passation, les coûts de possession et le risque de rupture ; le modèle de Wilson en donne la quantité économique pour une demande **certaine et régulière**.

*Application.* TERNAVAL Fret vend la traction de trains : la conduite et la circulation des trains forment son processus de production. La maintenance des locomotives et l'approvisionnement du magasin en semelles sont des processus support, dont le client est l'exploitation de M. QUERVILLAC. Ce support est pourtant **critique**, parce que la société n'a que neuf locomotives, dont deux louées : une locomotive qui attend ses semelles est un train perdu au moment où les chargeurs comparent le rail et la route. En 2027, 38 trains de céréales sont partis par la route, et ce sont les associés eux-mêmes qui les ont perdus.
- **Coût.** Une semelle en stock coûte 24 € par an, soit 30 % de son prix ; une semelle manquante coûte 200 € par mois, plus 1 500 € de commande urgente par mois de rupture. Le coût de la rupture est sans commune mesure avec celui du stock.
- **Délai.** Le fournisseur unique fabrique par séries pour toute l'Europe et livre en deux mois : chaque erreur de prévision se paie deux mois plus tard, sans recours.
- **Qualité.** La semelle doit être conforme au modèle des locomotives, parce que la sécurité des circulations en dépend : d'où le contrôle à l'arrivée.
- **Continuité.** Une visite due bloque la locomotive. Or, pendant la campagne, chaque locomotive parcourt 10 000 km par mois et passe donc à l'atelier tous les mois.

Les **incidents de 2027** ont une cause commune : l'atelier commande chaque mois le douzième de la consommation annuelle, comme si celle-ci était régulière. Or 68,33 % des semelles de l'année sont consommées de juillet à novembre, et septembre consomme 3,6 fois plus que mars. Les commandes constantes remplissent donc le magasin au printemps, au point de louer un conteneur, puis le vident à l'automne. Le délai de deux mois interdit de corriger à temps. Un stock tenu à la main, qui s'écarte de l'inventaire, aggrave encore la situation.

L'outil adapté est le **planning d'approvisionnement**. Les besoins se déduisent du programme des kilomètres, les commandes sont lancées deux mois avant le mois qui en a besoin, et le stock de sécurité ainsi que la capacité du magasin sont contrôlés mois par mois. La quantité économique de Wilson (100 semelles tous les 60 jours) ne convient pas comme règle de commande. Elle suppose une demande régulière, alors qu'un lot de 100 dure cinq mois en hiver et un peu plus d'un mois en septembre. Elle ignore aussi le délai et la capacité. Elle peut seulement donner un ordre de grandeur du lot : le lot de 90 semelles proposé en est proche.

**Conclusion** : la maintenance des locomotives est un processus support dont dépend directement la production. Sa performance se mesure par la disponibilité des locomotives pendant la campagne plus que par le coût du stock, et sa consommation saisonnière appelle un planning calé sur le programme des kilomètres, pas une quantité économique annuelle.

**Réponses tolérées**
- Maintenance présentée comme un processus de production « au sens large » (sans elle, pas de traction), si le candidat montre qu'elle sert l'exploitation et en tire les enjeux.
- Limites de Wilson montrées sans calcul, par les hypothèses du modèle (demande certaine et régulière, livraison instantanée, pas de rupture), si elles sont confrontées aux faits du cas.
- Analyse des enjeux en coût, qualité et délai (triangle coût-qualité-délai), complétée par la continuité.

**Erreurs fréquentes**
- `JUR-T07` — Appliquer le modèle de Wilson parce que la question parle d'approvisionnement, sans voir que la demande est saisonnière.
- `JUR-T09` — Considérer qu'un transporteur n'a ni stock ni fournisseur à piloter.
- `JUR-T03` — Paraphraser les incidents de 2027 sans en expliquer la cause (commandes constantes face à une consommation saisonnière et un délai de deux mois).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.3 (l. 808-812 : outils classiques de gestion des approvisionnements, plannings, exploitation dans divers processus) ; guide p. 121-122 (distinction production et support selon l'organisation ; plannings d'approvisionnement) | processus support, choix de l'outil | [V] | F06 § 0, § 6, § 7 |
| Porter, *Competitive Advantage*, 1985 | chaîne de valeur, activités de soutien | [S] | F13 |
| Modèle de Wilson (DCG) | quantité économique, hypothèses, point de commande | [S] | F06 § 2, § 5 ; F13 |

---

### 2.2 Plannings des deux politiques de commande et choix (2,5 pts)

**Compétences visées :**
- `2.3.d` — Mettre en œuvre ces outils (consommations, plannings de commandes, de livraisons et de stocks)
- `2.3.e` — Évaluer les résultats obtenus (ruptures, stock de sécurité, capacité, coût et service rendu)

**Barème (2,5 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Consommations de mai à décembre : **30, 35, 75, 85, 90, 90, 70 et 35 semelles** (510 sur la période) | 0,5 |
| 2.2-02 | Politique actuelle : livraisons de 50 semelles chaque mois (les commandes de mai à octobre sont livrées de juillet à décembre ; celles de novembre et décembre le seront en 2029) ; stocks de fin **105, 120, 95, 60, 20, − 20, − 40 et − 25** ; **ruptures en octobre, novembre et décembre** (85 semelles manquantes au total des trois fins de mois) ; septembre sous le stock de sécurité (20) ; **magasin dépassé en juillet** (170 semelles après livraison, 10 de trop) | 0,5 |
| 2.2-03 | Politique proposée : lots de 90 commandés en **juin, juillet, août et septembre**, livrés d'août à novembre ; stocks de fin **105, 120, 45, 50, 50, 50, 70 et 35** ; aucune rupture, aucun mois sous le stock de sécurité ; capacité respectée (155 semelles au plus, en juin, avec les livraisons déjà attendues) | 0,5 |
| 2.2-04 | Coûts sur la période : politique actuelle **23 500 €** (passation 1 200, possession 800, rupture 21 500 = 4 500 + 17 000) ; politique proposée **1 850 €** (passation 800, possession 1 050) ; économie de **21 650 €** ; hors rupture, 2 000 € contre 1 850 € | 0,5 |
| 2.2-05 | Choix argumenté : **politique proposée** retenue ; service rendu : 8 mois sur 8 sans rupture contre 5 (62,50 %), aucune locomotive en attente de semelles pendant la campagne, magasin respecté ; limites relevées : stock de fin de 45 à 50 semelles pendant la campagne, à peine au-dessus du stock de sécurité (10 jours de pointe), commandes chaque mois de juin à septembre, dépendance à l'exactitude du stock prévisionnel et à la ponctualité du fournisseur ; 60 semelles de plus livrées, qui correspondent au manque de 25 et au stock de 35 à la fin de décembre | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : un **planning d'approvisionnement** par politique, présenté en tableau mensuel (stock de début, livraison, stock après livraison, consommation, stock de fin, commande passée), suivi d'une comparaison des coûts de passation, de possession et de rupture et du service rendu (mois sans rupture, semelles manquantes, capacité).
- Alternatives acceptées : un seul tableau qui juxtapose les deux politiques ; une comparaison en semelles-mois de stock et en semelles manquantes avant leur valorisation ; un planning de la politique proposée qui fait apparaître le « besoin net » de chaque mois (stock de sécurité − stock de fin sans commande) avant le nombre de lots. Non accepté : une livraison placée le mois de la commande (délai ignoré), ou une commande déclenchée le mois où le stock est déjà négatif.

**Conventions rappelées** (annexes 2.2 et 2.3)

Livraison au début du mois ; stock de fin = stock de début + livraisons − consommations ; commande du début du mois p livrée au début du mois p + 2 ; politique proposée : lot de 90 commandé deux mois avant le premier mois dont le stock de fin, sans ce lot, passerait strictement sous 30 ; stock négatif reporté ; capacité de 160 semelles après livraison ; passation 200 € par commande passée de mai à octobre ; possession 2 € par semelle en stock à la fin du mois ; rupture 1 500 € par mois de stock négatif + 200 € par semelle manquante à la fin de chaque mois.

**Calculs détaillés**

*Consommations* (1 semelle par millier de kilomètres)

| | mai | juin | juil. | août | sept. | oct. | nov. | déc. | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Kilomètres | 30 000 | 35 000 | 75 000 | 85 000 | 90 000 | 90 000 | 70 000 | 35 000 | 510 000 |
| **Semelles consommées** | **30** | **35** | **75** | **85** | **90** | **90** | **70** | **35** | **510** |

*Politique actuelle : 50 semelles commandées au début de chaque mois* (semelles)

| | mai | juin | juil. | août | sept. | oct. | nov. | déc. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Stock de début | 85 | 105 | 120 | 95 | 60 | 20 | − 20 | − 40 |
| Livraison (début de mois) | 50 (déjà attendue) | 50 (déjà attendue) | 50 | 50 | 50 | 50 | 50 | 50 |
| Stock après livraison (capacité 160) | 135 | 155 | **170** | 145 | 110 | 70 | 30 | 10 |
| Consommation | 30 | 35 | 75 | 85 | 90 | 90 | 70 | 35 |
| **Stock de fin** | **105** | **120** | **95** | **60** | **20** | **− 20** | **− 40** | **− 25** |
| Commande passée (livrée deux mois plus tard) | 50 | 50 | 50 | 50 | 50 | 50 | 50 (janv. 2029) | 50 (févr. 2029) |
| Lecture | | | magasin dépassé de 10 | | sous la sécurité | rupture | rupture | rupture |

*Politique proposée : lots de 90 semelles déclenchés par le stock prévisionnel* (semelles)

| | mai | juin | juil. | août | sept. | oct. | nov. | déc. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Stock de début | 85 | 105 | 120 | 45 | 50 | 50 | 50 | 70 |
| Stock de fin sans nouvelle livraison | 105 | 120 | 45 | **− 40** | **− 40** | **− 40** | **− 20** | 35 |
| Livraison (début de mois) | 50 (déjà attendue) | 50 (déjà attendue) | – | 90 | 90 | 90 | 90 | – |
| Stock après livraison (capacité 160) | 135 | 155 | 120 | 135 | 140 | 140 | 140 | 70 |
| Consommation | 30 | 35 | 75 | 85 | 90 | 90 | 70 | 35 |
| **Stock de fin** | **105** | **120** | **45** | **50** | **50** | **50** | **70** | **35** |
| Commande passée (lot de 90) | – | **90** | **90** | **90** | **90** | – | – | – |

Lecture de la règle de lancement : en août, le stock de fin sans livraison serait 45 − 85 = − 40, sous 30 : un lot est livré au début d'août, donc commandé au début de juin ; le même raisonnement conduit aux lots livrés en septembre (50 − 90 = − 40), en octobre (− 40) et en novembre (50 − 70 = − 20). En juillet (45) et en décembre (35), le stock de fin reste au-dessus de 30 : aucune livraison. Un lot suffit chaque fois.

*Coût de chaque politique, mai à décembre 2028* (€)

| | Politique actuelle | Politique proposée |
|---|---:|---:|
| Commandes passées de mai à octobre (livrées pendant la période) | 6 | 4 |
| Passation (× 200 €) | 1 200 | 800 |
| Semelles en stock à la fin des mois (stocks de fin positifs) | 400 | 525 |
| Possession (× 2 €) | 800 | 1 050 |
| Mois de rupture × 1 500 € | 3 × 1 500 = 4 500 | 0 |
| Semelles manquantes à la fin des mois (20 + 40 + 25) × 200 € | 85 × 200 = 17 000 | 0 |
| Rupture | 21 500 | 0 |
| **Coût total** | **23 500** | **1 850** |
| Coût hors rupture | 2 000 | 1 850 |

Économie de la politique proposée : 23 500 − 1 850 = **21 650 €**. Service rendu : mois sans rupture 5 / 8 = **62,50 %** contre 8 / 8 = 100 % ; occupation maximale du magasin 170 / 160 = **106,25 %** contre 155 / 160 = 96,88 %. Livraisons de juillet à décembre : 300 semelles contre 360 ; l'écart de 60 correspond aux 25 semelles qui manquent encore à la fin de décembre avec la politique actuelle et aux 35 en stock avec la politique proposée.

**Réponse attendue**

*Concepts.* Un planning d'approvisionnement programme les commandes et les livraisons pour que le stock de chaque période couvre les besoins sans descendre sous le stock de sécurité ni dépasser la capacité de stockage. Une politique se juge par son coût (passation, possession, rupture) **et** par le service rendu au processus servi.

*Application.* La **politique actuelle** livre 50 semelles chaque mois, alors que la consommation passe de 30 en mai à 90 en septembre et en octobre. Le stock monte jusqu'en juin, puis le magasin déborde en juillet (170 semelles pour 160 places). Le stock passe sous la sécurité en septembre, puis tombe en rupture d'octobre à décembre : 20, puis 40, puis 25 semelles manquent à la fin du mois, au cœur de la campagne. C'est le scénario de 2027 reproduit en 2028. La **politique proposée** suit le programme : aucun lot en juillet, puis un lot de 90 chaque mois d'août à novembre, commandé deux mois avant. Elle ne connaît ni rupture, ni mois sous la sécurité, ni dépassement du magasin.

Le coût confirme le choix : 1 850 € contre 23 500 €, parce que la rupture représente 21 500 € des 23 500 € de la politique actuelle. Même sans compter la rupture, la politique proposée coûte un peu moins (1 850 € contre 2 000 €) : deux commandes de moins compensent 125 semelles-mois de stock en plus. Le service rendu à l'exploitation est l'argument décisif : aucune locomotive n'attend ses semelles pendant la campagne. La politique proposée a pourtant des **limites**. Pendant la campagne, le stock de fin n'est que de 45 à 50 semelles, soit 15 à 20 au-dessus d'un stock de sécurité qui couvre dix jours. Elle exige une commande chaque mois de juin à septembre, alors que le délai reste de deux mois. Elle repose sur un stock prévisionnel exact et sur un fournisseur ponctuel (question 2.3).

**Conclusion** : la politique proposée est retenue, parce qu'elle supprime les ruptures de la campagne pour un coût de gestion plus faible (1 850 €, contre 23 500 € avec les ruptures). Elle laisse toutefois une marge étroite, qui rend la maîtrise du stock et du fournisseur décisive.

**Réponses tolérées**
- Coût de passation compté pour les huit commandes de la politique actuelle (1 600 €, total 23 900 €), si le candidat le dit : le classement ne change pas.
- Semelles manquantes comptées une seule fois (manque nouveau de chaque mois : 20 en octobre, 20 de plus en novembre, aucun nouveau en décembre), avec une hypothèse écrite ; l'annexe compte chaque mois les semelles qui manquent encore.
- Dépassement du magasin traité par une hypothèse (livraison de juillet réduite ou décalée, conteneur loué comme en 2027), s'il est d'abord repéré.
- Stocks présentés sans la ligne « stock après livraison », si le dépassement de juillet est relevé.

**Erreurs fréquentes**
- `JUR-P02` — Ne pas appliquer la règle de lancement donnée : commande passée le mois de la livraison, ou lot déclenché quand le stock est déjà négatif.
- `JUR-T10` — Comparer les politiques sur le seul coût de gestion (passation et possession), sans valoriser les ruptures ni parler du service rendu.
- `JUR-T03` — Présenter les plannings sans lecture : ni mois de rupture, ni mois sous la sécurité, ni dépassement du magasin.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.3 (l. 808-810 et 814 : plannings d'approvisionnement, évaluer les résultats obtenus) ; guide p. 122 (« programmation des approvisionnements à travers l'élaboration de plannings ») | planning, règle de lancement, comparaison des politiques | [V] | F06 § 0, § 6, § 8 |
| Stock de sécurité, quantités constantes et périodes variables | conventions du planning | [S] | F06 § 1, § 5, § 6 |

---

### 2.3 Criticité des risques du processus et lien avec les plannings (1 pt)

**Compétence visée :**
- `2.5.b` — Analyser les risques rencontrés par l'organisation (criticité, hiérarchie, représentation)

**Barème (1 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Criticité définie puis calculée : **R2 16, R1 12, R3 9, R4 8, R5 6, R6 4** ; classes : R2 et R1 **critiques**, R3, R4 et R5 majeurs, R6 mineur ; matrice probabilité × gravité (4 × 4) qui place chaque risque ; hiérarchie écrite | 0,5 |
| 2.3-02 | Lien avec la question 2.2 : R2 est le risque que mesure le planning de la politique actuelle (ruptures d'octobre à décembre, 21 500 €) et que la politique proposée traite (probabilité ramenée à 1 ou 2, criticité de 4 à 8) ; R1 devient alors le premier risque : avec un stock de fin de 45 à 50 semelles en campagne, **une livraison d'août retardée d'un mois** crée une rupture de **40 semelles** et un coût de rupture de **9 500 €** ; R3 compromet la règle de lancement elle-même (l'écart d'inventaire de 12 semelles vaut **40 %** du stock de sécurité) ; limite relevée : R6, mineur par le produit, a la gravité maximale | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : la **criticité** (probabilité × gravité) sur les échelles et les seuils de l'annexe 2.4, représentée sur une **matrice** probabilité × gravité (cartographie des risques du processus). Elle est adaptée parce que la question demande de hiérarchiser des risques déjà cotés, puis de rapprocher la hiérarchie des plannings.
- Alternatives acceptées : un tableau classé par criticité décroissante, sans matrice, si les classes sont indiquées ; une lecture qui distingue risque brut (cotation de l'annexe) et risque après la politique proposée (probabilité de R2 recotée par le candidat). Non accepté : une FFOM, qui ne hiérarchise pas ; une probabilité chiffrée en pourcentage, absente de l'énoncé, multipliée par un coût.

**Conventions rappelées** (annexe 2.4)

Criticité = probabilité × gravité, échelles de 1 à 4 ; critique si ≥ 12, majeur de 6 à 9, mineur si ≤ 4.

**Calculs détaillés**

| Rang | Risque | Probabilité | Gravité | Criticité | Classe |
|---:|---|---:|---:|---:|---|
| 1 | R2 Commandes qui ne suivent pas le programme → rupture en campagne | 4 | 4 | **16** | critique |
| 2 | R1 Retard ou défaillance du fournisseur unique | 3 | 4 | **12** | critique |
| 3 | R3 Erreur de stock (stock enregistré supérieur au stock réel) | 3 | 3 | **9** | majeur |
| 4 | R4 Retard d'une visite, atelier saturé en campagne | 2 | 4 | **8** | majeur |
| 5 | R5 Départ d'un technicien spécialiste du freinage | 2 | 3 | **6** | majeur |
| 6 | R6 Lot de semelles non conforme | 1 | 4 | **4** | mineur |

*Matrice* (probabilité en lignes, gravité en colonnes)

| Probabilité \ Gravité | 1 faible | 2 modérée | 3 forte | 4 très forte |
|---|---|---|---|---|
| 4 très probable | | | | **R2 (16)** |
| 3 probable | | | R3 (9) | **R1 (12)** |
| 2 possible | | | R5 (6) | R4 (8) |
| 1 rare | | | | R6 (4) |

*Lien avec les plannings.*
- **Retard d'un mois de la livraison d'août** (politique proposée ; lot commandé en juin, livré en septembre) : stock de fin d'août 45 − 85 = **− 40**, puis septembre − 40 + 90 + 90 − 90 = 50 ; les mois suivants ne changent pas, et le magasin reste dans sa capacité (140 semelles en septembre). Coût de rupture : 1 500 + 40 × 200 = **9 500 €**, plus de cinq fois le coût de gestion de la politique sur la période (1 850 €) ; net de la possession évitée en août (50 semelles-mois, 100 €), le retard coûte 9 400 € et porte le coût de la politique à 11 250 €.
- **Erreur de stock** : 12 semelles / 30 semelles de stock de sécurité = **40 %**. Un stock enregistré trop haut retarde la commande qui aurait dû partir deux mois plus tôt.

**Réponse attendue**

*Concepts.* Un risque est un événement incertain qui compromet un objectif ; il s'énonce par sa cause et sa conséquence. Sa criticité combine sa probabilité et sa gravité, ce qui permet de hiérarchiser les risques et de concentrer les actions sur les plus critiques. La matrice probabilité × gravité, ou cartographie, les situe d'un coup d'œil. La cotation de l'annexe est brute : elle ne tient pas compte des mesures qui seront prises.

*Application.* Deux risques sont **critiques**.
- **R2 (16).** Il est très probable, puisqu'il s'est réalisé en 2027, et la question 2.2 montre qu'il se reproduirait en 2028 si la politique actuelle était maintenue : trois mois de rupture, 85 semelles manquantes et 21 500 € de coût. C'est précisément le risque que la politique proposée traite. Avec des lots calés sur le programme des kilomètres, sa probabilité tombe à 1 ou 2, et sa criticité à 4 ou 8.
- **R1 (12).** Le fournisseur unique devient alors le premier risque. La politique proposée laisse un stock de fin de 45 à 50 semelles pendant la campagne, pour une consommation de 85 à 90 semelles par mois : un seul lot livré avec un mois de retard en août crée une rupture de 40 semelles, soit un coût de rupture de 9 500 €. Or le fournisseur reconnaît un retard de trois semaines en 2027 et ne peut pas fabriquer plus vite.

Trois risques sont **majeurs**.
- **R3 (9).** Il touche le cœur de la nouvelle politique, puisque la règle de lancement repose sur le stock prévisionnel : l'écart de 12 semelles constaté à l'inventaire représente 40 % du stock de sécurité.
- **R4 (8) et R5 (6).** Ils relèvent de la capacité et de l'expertise de l'atelier en campagne : neuf visites par mois, et deux spécialistes du freinage, dont l'un part en 2029.

**R6** est mineur par le produit (4), mais il a la gravité maximale, puisque la sécurité des circulations est en cause. Le contrôle à l'arrivée doit donc être maintenu, même si le risque n'est pas prioritaire.

**Conclusion** : la politique proposée fait passer le premier risque du processus d'un risque interne, la façon de commander, à un risque externe, la dépendance au fournisseur unique, aggravé par l'exactitude du stock. Ce sont ces deux risques que les préconisations doivent viser.

**Réponses tolérées**
- Recotation de R2 après la politique proposée à une autre valeur (probabilité 1 ou 2), si elle est justifiée par les plannings.
- Lien avec la question 2.2 établi sans chiffrer le retard d'une livraison, si le candidat relève la marge étroite du stock de fin pendant la campagne.
- R4 rapproché de la politique proposée (les visites ne doivent pas attendre les semelles), si l'argument est développé.

**Erreurs fréquentes**
- `JUR-T03` — Recopier la cotation sans hiérarchie ni lecture, ou classer les risques sans les relier aux plannings.
- `JUR-T07` — Traiter la criticité comme une fin en soi, sans voir qu'un risque mineur par le produit peut avoir une gravité extrême (R6).
- `JUR-T02` — Énoncer des risques génériques (« risque fournisseur ») sans les faits du cas : délai de deux mois, retard de 2027, écart d'inventaire.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.5 (l. 835-837 : cartographie des risques, notion de criticité) ; guide p. 123 | criticité, matrice, lien avec les processus | [V] | F08 § 0, § 2.1 |
| Typologie des risques, formulation en événements | risques opérationnels du processus | [S] | F08 § 1, § 5 |

---

### 2.4 Note à M. VORANCHE et à M. QUERVILLAC (20 lignes au maximum) (2 pts)

**Compétences visées :**
- `2.3.f` — Élaborer des préconisations afin de mieux piloter la performance des activités hors production (approvisionnement des semelles, atelier)
- `2.3.g` — Produire une synthèse rédigée et structurée concernant les décisions liées aux processus support
- `2.5.e` — Produire une synthèse rédigée et structurée sur la gestion des risques

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Politique retenue (lots de 90 déclenchés par le stock prévisionnel, appliquée dès les commandes de mai) et chiffres clés (aucune rupture, 1 850 € contre 23 500 €) ; lien avec la stratégie : la fiabilité pendant la campagne est la condition pour garder les trafics céréaliers face à la route, satisfaire des associés qui sont aussi les clients, maintenir le trafic dont dépend le financement de la Région, et préparer le service vers le port maritime de 2029 ; arbitrage explicite coût du stock / coût de la rupture et délai | 0,5 |
| 2.4-02 | Risques hiérarchisés (fournisseur unique et exactitude du stock en tête, une fois les commandes calées) et préconisations sur le processus : inventaire des semelles avant chaque date de commande et chaque mois de campagne ; prévision mensuelle des besoins revue avec l'exploitation à partir du programme des kilomètres ; visites anticipées avant juillet pour lisser la charge de l'atelier ; transmission de l'expertise freinage avant le départ de 2029 (binôme, formation d'un troisième technicien, démarche de GEPP) ; contrôle à l'arrivée maintenu | 0,5 |
| 2.4-03 | Pistes de l'annexe 2.5 appréciées et choix argumenté : **A** coûte 3 600 € par an (plus 100 € par prélèvement), livre en 24 heures, mais l'opérateur voisin connaît sa pointe de septembre à décembre, en même temps que TERNAVAL Fret, si bien que le stock commun risque d'être vide au moment où il serait utile ; **B** coûte **2 160 €** par an de surcoût d'achat (180 semelles × 12 €), au plus 2 760 € avec trois commandes supplémentaires de 60 (majorant : ces lots remplacent une partie des commandes au fournisseur actuel), réduit la dépendance au fournisseur unique (R1) et raccourcit le délai à un mois pour une partie des besoins ; les deux coûtent moins que le coût de rupture d'un seul retard de livraison en campagne (9 500 €) ; choix de B, éventuellement complété par A en dehors de la pointe du voisin | 0,5 |
| 2.4-04 | Deux ou trois indicateurs avec formule, cible et sens (par exemple : taux de disponibilité des locomotives pendant la campagne ; taux de visites terminées sans attente de pièces ; écart d'inventaire des semelles ; taux de livraisons du fournisseur à la date convenue) ; note structurée, qui prend position, 20 lignes au maximum | 0,5 |

**Calculs détaillés** (pistes, annexe 2.5)

Piste B : 30 % × 600 = **180 semelles** par an ; surcoût d'achat 180 × (92 − 80) = **2 160 €** ; avec trois commandes supplémentaires au lot minimal de 60 semelles, 2 160 + 3 × 200 = **2 760 €** au plus (29,05 % du coût de rupture d'un retard de livraison, 9 500 €) : c'est un majorant, car les 180 semelles du second fournisseur évitent environ deux lots de 90 chez le fournisseur actuel (400 € de passation) ; un calcul net (environ 2 360 €) est accepté. Piste A : cotisation de 3 600 € (37,89 % de ce même coût), plus 100 € par prélèvement.

**Réponse attendue** (exemple de note, 20 lignes)

> **À M. Romain VORANCHE et à M. Bastien QUERVILLAC — Objet : approvisionnement des semelles de frein et risques de la maintenance pour la campagne de 2028**
>
> **1. La politique retenue.** J'applique dès les commandes de mai la politique de M. VERLOMBE : des lots de 90 semelles, commandés deux mois avant le mois où le stock passerait sous 30. Elle évite toute rupture et tient dans le magasin, pour 1 850 € de passation et de possession. Garder 50 semelles par mois reproduirait 2027 : rupture d'octobre à décembre et 23 500 € de coût, dont 21 500 € de rupture. Une semelle en stock coûte 2 € par mois ; une semelle qui manque en coûte 200 et fait perdre des trains face à la route. La fiabilité en campagne conditionne la fidélité des chargeurs associés, le trafic qui fonde l'aide de la Région et le service vers le port maritime de 2029.
>
> **2. Les risques.** Les commandes étant calées sur les kilomètres, le premier risque devient le fournisseur unique : notre stock de campagne ne dépasse pas 50 semelles, et une livraison d'août retardée d'un mois coûterait 9 500 € de rupture. Vient ensuite l'exactitude du stock, qui fixe la date des commandes : l'écart de 12 semelles de janvier vaut 40 % du stock de sécurité. Je préconise un inventaire avant chaque commande, une prévision revue chaque mois avec l'exploitation, des visites anticipées en juin et la formation d'un troisième technicien du freinage avant 2029.
>
> **3. Les pistes.** Le second fournisseur (B : 2 160 € de surcoût par an pour 30 % des besoins, livrés en un mois) réduit notre dépendance là où elle coûte le plus. Le stock commun (A : 3 600 € par an) serait vide quand nous en aurions besoin, notre voisin ayant sa pointe de septembre à décembre. Je recommande B dès 2028.
>
> **4. Le suivi.** Disponibilité des locomotives en campagne = locomotives disponibles chaque matin / locomotives demandées × 100, cible 100 % (hausse) ; visites sans attente de pièces = visites terminées sans attente / visites, cible 100 % ; écart d'inventaire = (stock enregistré − stock compté) / stock enregistré, cible 0 % (baisse).

**Réponses tolérées**
- Piste A retenue, ou A et B combinées, si le candidat relève le chevauchement des pointes et en tient compte (par exemple, stock commun utilisé hors campagne, ou conditions de réservation négociées pour la campagne).
- Stock de sécurité relevé pendant la campagne (par exemple à 60 semelles de juillet à novembre), s'il est justifié par le délai et le risque fournisseur, et si le candidat relève la capacité du magasin.
- Autres indicateurs pertinents (couverture du stock en jours de consommation prévue, taux de livraisons à la date convenue, coût des ruptures par campagne), s'ils ont une formule, une cible et un sens.
- Note en trois parties (politique, risques et préconisations, suivi), si tous les éléments demandés y figurent.

**Erreurs fréquentes**
- `JUR-T05` — Note qui présente la politique de commande sans la relier à la stratégie de la société (trafics céréaliers, chargeurs associés, plan « TERNAVAL 2031 »).
- `JUR-T06` — Note de plus de 20 lignes, non structurée, ou indicateurs sans formule ni cible.
- `JUR-P02` — Pistes comparées sans utiliser leurs conditions (chevauchement des pointes pour A, part minimale de 30 % et lots de 60 pour B).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.3 (l. 815-820 : préconisations pour les activités hors production, synthèse sur les processus support) | préconisations sur le processus, décision argumentée | [V] | F06 § 0, § 7, § 8 |
| Programme UE 3, partie 2.5 (l. 843-844 : synthèse sur la gestion des risques) ; guide p. 123 | traitement des risques, indicateurs de risque | [V] | F08 § 0, § 2.1, § 5 |
| GEPP (transmission de l'expertise avant un départ) | départ d'un technicien spécialiste | [S] | F09 |
| Indicateurs de tableau de bord (formule, cible, sens) | indicateurs de suivi | [S] | F12 § 3 |
