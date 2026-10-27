# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 12 — Dossier 3 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 risques de taux et de change et trésorerie de groupe, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (vente à terme, avances en devises, barème, liste noire, hors-programme ; position de change, termaillage, clause d'indexation et assurance prospection vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une valeur acquise calculée à partir d'un montant emprunté erroné à la question 3.3).

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
