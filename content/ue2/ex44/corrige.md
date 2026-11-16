# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 44 — Dossier 2 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F06 marchés, efficience, finance comportementale et fintech, F07 risques et trésorerie, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (rentabilités espérées, écarts-types, covariances et bêtas des séries, décomposition de la variance, MEDAF, covariance, rentabilité espérée, écart-type et bêta des deux allocations, ratios de Sharpe et de Treynor, écarts-types à corrélation 1, barème, liste noire, hors-programme ; produits des placements à court terme, variations de cours, gain net de l'offre de la fintech et encours d'équilibre vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple des allocations calculées avec un écart-type ou un bêta erronés à la question 2.2).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Placements à court terme : produit net, rendement annualisé, retrait anticipé et répartition des 90 M€ | `6.1.b` Discerner les différents types de financement et de placement | 2 |
| 2.2 Rentabilité espérée, écart-type et bêta de l'action LUDÉRIAN et du fonds diversifié, MEDAF | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 2,5 |
| 2.3 Risque systématique et spécifique, deux allocations, Sharpe et Treynor, diversification et recommandation | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) ; `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres | 5 |
| 2.4 Réaction du cours aux deux annonces et affirmation de sous-évaluation | `5.1.c` Maîtriser les grands enseignements de l'efficience informationnelle des marchés (Fama, 1970) | 2 |
| 2.5 Biais comportementaux de la proposition et du forum, nuance de l'efficience, règles de placement | `5.1.d` Maîtriser les grands enseignements de la finance comportementale | 1,5 |
| 2.6 Gestion de trésorerie par algorithme, trading à haute fréquence, nouveaux acteurs et recommandation | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs | 3 |
| **Total** | | **16** |

Part du calcul : environ 7 points (2.1-01, 2.1-02, 2.2-01, 2.2-02, la moitié de 2.2-03, 2.3-01, 2.3-03, 2.3-04, le tiers de 2.4-01 et de 2.4-02, 2.6-02). Part de l'analyse : environ 9 points. Les questions 2.4 à 2.6 sont rédactionnelles mais valent 6,5 points : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 2.1 Placements à court terme : produit net, rendement annualisé, retrait anticipé et répartition des 90 M€ (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Placement de 30 000 k€ sur 240 jours : compte à terme **570 k€**, soit **2,85 %** ; OPC monétaire 480 − 12 = **468 k€**, soit **2,34 %** ; NEU CP 630 − 18 = **612 k€**, soit **3,06 %** | 1 |
| 2.1-02 | Retrait le 31 août 2027 (120 jours) : compte à terme **120 k€** (taux de 1,20 %), OPC monétaire 240 − 12 = **228 k€** ; le compte à terme n'est rentable que s'il va à son échéance | 0,25 |
| 2.1-03 | Rapprochement avec le calendrier et la politique de placement : OPC pour les décaissements de 2027 et le minimum de 20 M€ disponible ; NEU CP limités à 10 M€ (plafond par émetteur, pas de sortie, risque de défaut) ; comptes à terme échelonnés sur les échéances de 2028 (au plus 18 mois) dans la limite de 50 M€ par banque ; répartition chiffrée cohérente, liquidité avant rendement | 0,75 |

**Produit net et rendement net annualisé (1 pt).** Conventions de l'annexe 2.5 : intérêts simples, Exact/360, 240 jours du 3 mai au 29 décembre 2027 ; produits en k€ arrondis à l'unité.

| Support | Intérêts ou rendement (k€) | Commissions (k€) | Produit net (k€) | Taux net annualisé |
|---|---:|---:|---:|---:|
| Compte à terme : 30 000 × 2,85 % × 240 / 360 | 570 | 0 | **570** | **2,85 %** |
| OPC monétaire : 30 000 × (2,60 % − 0,20 %) × 240 / 360 | 480 | 30 000 × 0,04 % = 12 | **468** | 468 / 30 000 × 360 / 240 = **2,34 %** |
| NEU CP : 30 000 × 3,15 % × 240 / 360 | 630 | 30 000 × 0,06 % = 18 | **612** | 612 / 30 000 × 360 / 240 = **3,06 %** |

Les NEU CP rapportent le plus, l'OPC monétaire le moins : il paie sa liquidité quotidienne par ses frais de gestion (0,20 point par an) et sa commission de rachat (0,06 point en rythme annuel sur 240 jours).

**Retrait anticipé au 31 août 2027 (0,25 pt).** Sur 120 jours, le compte à terme ne rapporte plus que 30 000 × 1,20 % × 120 / 360 = **120 k€**, contre 30 000 × 2,40 % × 120 / 360 − 12 = **228 k€** pour l'OPC monétaire. Sur la même durée de 120 jours, la pénalité du retrait anticipé est de 30 000 × (2,85 % − 1,20 %) × 120 / 360 = 165 k€ ; l'OPC, lui, rapporte 228 k€. Un compte à terme ne doit donc porter que des fonds dont la date de besoin est connue ; un NEU CP ne peut même pas être remboursé avant l'échéance (revente seulement, à un prix incertain).

**Rapprochement avec le calendrier et répartition (0,75 pt).** Le placement d'une trésorerie de projet se choisit d'abord selon l'horizon du besoin, puis selon le couple rendement-risque (6.1.b) : les 90 M€ seront décaissés en moins de dix-huit mois, la politique du groupe impose un capital garanti ou un risque très faible et 20 M€ disponibles le jour ouvré suivant (ou la totalité de ce qui reste à décaisser, quand il reste moins de 20 M€).
- **OPC monétaire** : seul support liquide au jour le jour ; il porte les décaissements réguliers du 2e semestre 2027 (24 M€, dont la date exacte peut avancer) et le minimum de 20 M€ disponible, qui financera la fin de la production et la campagne de lancement de septembre et d'octobre 2028 : à partir de septembre 2028, il reste moins de 20 M€ à décaisser, et la charte n'exige plus que la totalité du solde soit disponible.
- **NEU CP d'AUBRAVEL Industrie** : meilleur rendement, mais risque de défaut d'un émetteur unique, aucune sortie anticipée et plafond de 10 M€ par émetteur non bancaire. Le gain sur l'OPC n'est que de 10 000 × (3,06 % − 2,34 %) × 240 / 360 = 48 k€ : il ne justifie pas de dépasser le plafond. Échéance au 29 décembre 2027, pour financer janvier et février 2028.
- **Comptes à terme de la Banque MERVAUDIN** : capital garanti par la banque, taux fixe ; adaptés aux décaissements datés de 2028 en plusieurs comptes d'au moins 5 M€ aux échéances échelonnées (de 10 à 18 mois, la dernière au plus tard le 3 novembre 2028), dans la limite de 50 M€ par banque.

| Support | Montant (M€) | Besoins financés |
|---|---:|---|
| OPC monétaire | 44 | 2e semestre 2027 (24) ; minimum disponible de 20, utilisé en septembre et octobre 2028 |
| NEU CP AUBRAVEL, échéance 29/12/2027 | 10 | janvier et février 2028 |
| Comptes à terme MERVAUDIN, échéances échelonnées de mars à septembre 2028 | 36 | mars à juin 2028 (20) ; juillet et août 2028, début de septembre 2028 (16) |
| **Total** | **90** | |

Toute répartition qui respecte le calendrier, le minimum de 20 M€ disponible, le plafond de 10 M€ en NEU CP et la limite de 50 M€ par banque est acceptée ; la logique attendue est d'adosser les échéances aux besoins et de ne chercher le rendement que sur les fonds dont la date est certaine.

**Réponses tolérées** : taux annualisés rapportés à 365 jours s'ils sont signalés ; commission de rachat de l'OPC calculée sur le montant racheté (468 k€ à 1 k€ près) ; plusieurs NEU CP de 10 M€ chacun auprès d'émetteurs différents s'ils sont présentés comme une extension de l'offre ; OPC monétaire pour une part plus grande au détriment du rendement, si la liquidité est justifiée.

**Erreurs fréquentes**
- Calculer les intérêts sur une année entière, ou sur 240 / 365 sans le signaler.
- Oublier la commission de rachat de l'OPC ou la commission de placement des NEU CP, ou comparer des taux bruts.
- Placer la totalité en NEU CP au motif du meilleur rendement, sans voir le plafond par émetteur, l'absence de sortie et le risque de défaut.
- `JUR-T13` — répartition générale, sans les dates et les montants du calendrier.

---

### 2.2 Rentabilité espérée, écart-type et bêta de l'action LUDÉRIAN et du fonds diversifié, MEDAF (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Rentabilités espérées : LUDÉRIAN **12,00 %**, GIRONVAL Actions Monde **8,50 %**, indice **9,00 %** ; écarts-types (n − 1) : **40,00 %**, **14,00 %**, **15,00 %** | 1 |
| 2.2-02 | Covariances avec l'indice : **315,00 %²** et **202,50 %²** ; bêtas = 315 / 225 = **1,40** et 202,5 / 225 = **0,90** | 0,5 |
| 2.2-03 | MEDAF : LUDÉRIAN 4,0 % + 1,40 × 5,0 % = **11,00 %** (écart + 1,00 point) ; fonds 4,0 % + 0,90 × 5,0 % = **8,50 %** (écart nul) ; commentaire : le surcroît de LUDÉRIAN tient à 2026 (+ 64 %), sur cinq années très dispersées, et ne rémunère pas un risque total de 40 % ; le fonds rapporte ce que son risque systématique exige, après frais | 1 |

**Rentabilités espérées et écarts-types (1 pt).** Moyenne arithmétique des cinq rentabilités ; variances sur n − 1 = 4.

| | LUDÉRIAN | GIRONVAL Actions Monde | Indice |
|---|---:|---:|---:|
| Somme des rentabilités (%) | 60,0 | 42,5 | 45,0 |
| Rentabilité espérée | **12,00 %** | **8,50 %** | **9,00 %** |
| Somme des carrés des écarts (%²) | 6 400 | 784 | 900 |
| Variance (÷ 4) | 1 600 %² (0,160000) | 196 %² (0,019600) | 225 %² (0,022500) |
| Écart-type | **40,00 %** | **14,00 %** | **15,00 %** |

Écarts à la moyenne de LUDÉRIAN : − 37,6 ; − 42,4 ; 20,8 ; 7,2 ; 52,0. Du fonds : − 22,8 ; 3,8 ; − 2,6 ; 8,6 ; 13,0. De l'indice : − 24 ; 9 ; − 3 ; 3 ; 15.

**Covariances et bêtas (0,5 pt).**
- Covariance LUDÉRIAN-indice = [(− 37,6)(− 24) + (− 42,4)(9) + (20,8)(− 3) + (7,2)(3) + (52,0)(15)] / 4 = (902,4 − 381,6 − 62,4 + 21,6 + 780,0) / 4 = 1 260 / 4 = **315,00 %²** ; bêta = 315 / 225 = **1,40**.
- Covariance fonds-indice = (547,2 + 34,2 + 7,8 + 25,8 + 195,0) / 4 = 810 / 4 = **202,50 %²** ; bêta = 202,5 / 225 = **0,90**.

**MEDAF et commentaire (1 pt).** Le MEDAF (Sharpe, 1964) fixe la rentabilité qu'exige un investisseur diversifié en fonction du seul risque systématique.
- LUDÉRIAN : 4,0 % + 1,40 × 5,0 % = **11,00 %**, pour une rentabilité espérée de 12,00 % : écart de **+ 1,00 point**.
- GIRONVAL Actions Monde : 4,0 % + 0,90 × 5,0 % = **8,50 %**, égale à sa rentabilité espérée (écart nul).
- L'indice rapporte 9,00 %, soit le taux sans risque plus la prime de marché : les hypothèses sont cohérentes.
- Commentaire : le surcroît de 1 point de LUDÉRIAN repose sur cinq années très dispersées (de − 30,4 % à + 64,0 %) et presque entièrement sur 2026 ; sans 2026, la moyenne des quatre premières années est de − 1,00 %. Avec un écart-type de 40 %, un tel écart ne prouve aucune capacité durable à battre le marché : le passé est un estimateur fragile de la rentabilité espérée. Le fonds, lui, rémunère exactement son risque systématique, net de ses frais : c'est ce qu'on attend d'un placement diversifié sur un marché efficient.

**Réponses tolérées** : calculs en fraction (variance de 0,16 et covariance de 0,0315) ; bêta obtenu par la corrélation × écart-type du titre / écart-type de l'indice si les étapes sont justes.

**Erreurs fréquentes**
- Écarts-types calculés sur n (35,78 % ; 12,52 % ; 13,42 %), contraires à la convention de l'annexe.
- Bêta calculé comme rapport des écarts-types (40 / 15 = 2,67), qui ignore la corrélation.
- Utiliser la rentabilité de l'indice (9 %) à la place de la prime de risque (5 %) dans le MEDAF.
- `JUR-T14` — MEDAF appliqué sans dire qu'il ne rémunère que le risque systématique.

---

### 2.3 Risque systématique et spécifique, deux allocations, Sharpe et Treynor, diversification et recommandation (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | LUDÉRIAN : variance systématique 1,40² × 225 = **441 %²** (**27,56 %**), spécifique **1 159 %²** (**72,44 %**) ; fonds : 0,90² × 225 = **182,25 %²** (**92,98 %**), spécifique **13,75 %²** (**7,02 %**) | 0,75 |
| 2.3-02 | Différence : risque systématique (marché, non diversifiable, seul rémunéré par le MEDAF) et risque spécifique (propre à l'émetteur : succès ou échec d'un jeu, diversifiable, non rémunéré) | 0,5 |
| 2.3-03 | A : covariance 0,20 × 40 × 6 = **48,00 %²**, rentabilité espérée **7,44 %**, variance 292,00 %², écart-type **17,09 %**, bêta **0,74** ; B : covariance 0,60 × 14 × 6 = **50,40 %²**, **6,04 %**, variance 68,51 %², **8,28 %**, bêta **0,54** | 1,25 |
| 2.3-04 | Sharpe : A **0,20**, B **0,25** ; Treynor : A **4,65 %**, B **3,78 %** ; classements opposés | 0,75 |
| 2.3-05 | Markowitz (1952) : le risque d'une allocation dépend de la corrélation ; à corrélation 1, écarts-types de 19,60 % et 9,20 % ; gain de diversification de 2,51 et 0,92 points ; la faible corrélation de A ne compense pas le risque spécifique de LUDÉRIAN | 0,5 |
| 2.3-06 | Ratio pertinent : Sharpe (risque total), car la réserve n'est pas une ligne d'un portefeuille diversifié ; Treynor ignore le risque spécifique et flatte A | 0,25 |
| 2.3-07 | Risque propre : corrélation de 0,65 avec NOCTÉVAL, chocs communs du secteur (boutiques numériques, demande, coûts des équipes), réserve qui baisse quand elle est nécessaire (retard de la sortie), perte de 3 648 k€ sur la poche en 2023 ; les actionnaires peuvent se diversifier eux-mêmes ; recommandation : allocation B, avec une part actions éventuellement réduite, rejet de A | 1 |

**Décomposition de la variance (0,75 pt).** Convention : variance = bêta² × variance de l'indice + variance spécifique ; parts calculées sur la variance.

| | Variance totale | Variance systématique | Variance spécifique | Part systématique | Part spécifique |
|---|---:|---:|---:|---:|---:|
| LUDÉRIAN | 1 600 %² | 1,40² × 225 = **441,00 %²** | 1 600 − 441 = **1 159,00 %²** | **27,56 %** | **72,44 %** |
| GIRONVAL Actions Monde | 196 %² | 0,90² × 225 = **182,25 %²** | 196 − 182,25 = **13,75 %²** | **92,98 %** | **7,02 %** |

En écarts-types : risque systématique de 21,00 % et risque spécifique de 34,04 % pour LUDÉRIAN ; 13,50 % et 3,71 % pour le fonds (non exigé).

**Différence entre les deux risques (0,5 pt).** Le **risque systématique** vient des fluctuations de l'ensemble du marché (conjoncture, taux, prime de risque) : il touche tous les titres, ne se diversifie pas, et c'est le seul que le MEDAF rémunère, par le bêta. Le **risque spécifique** tient à l'émetteur : pour un éditeur, le succès ou l'échec d'un jeu (− 30,4 % en 2023, + 64,0 % en 2026), un report, le départ d'une équipe. Il disparaît presque dans un portefeuille diversifié (7 % de la variance du fonds, investi dans 400 sociétés) et n'est pas rémunéré : un investisseur qui garde 72 % de risque spécifique supporte un risque pour lequel le marché ne paie aucune prime.

**Les deux allocations (1,25 pt).** Poids de 40 % pour le support actions et de 60 % pour le fonds obligataire (espérance 4,40 %, écart-type 6,00 %, bêta 0,30).

| | Allocation A (LUDÉRIAN) | Allocation B (fonds diversifié) |
|---|---:|---:|
| Covariance avec le fonds obligataire | 0,20 × 40 × 6 = **48,00 %²** | 0,60 × 14 × 6 = **50,40 %²** |
| Rentabilité espérée | 0,4 × 12 + 0,6 × 4,4 = **7,44 %** | 0,4 × 8,5 + 0,6 × 4,4 = **6,04 %** |
| Variance | 0,16 × 1 600 + 0,36 × 36 + 2 × 0,4 × 0,6 × 48 = 256 + 12,96 + 23,04 = **292,00 %²** | 0,16 × 196 + 12,96 + 0,48 × 50,4 = 31,36 + 12,96 + 24,19 = **68,51 %²** |
| Écart-type | **17,09 %** | **8,28 %** |
| Bêta | 0,4 × 1,40 + 0,6 × 0,30 = **0,74** | 0,4 × 0,90 + 0,6 × 0,30 = **0,54** |

**Ratios de Sharpe et de Treynor (0,75 pt).**

| | Sharpe = (E − 4 %) / écart-type | Treynor = (E − 4 %) / bêta |
|---|---:|---:|
| Allocation A | 3,44 / 17,09 = **0,20** | 3,44 / 0,74 = **4,65 %** |
| Allocation B | 2,04 / 8,28 = **0,25** | 2,04 / 0,54 = **3,78 %** |
| Pour mémoire : LUDÉRIAN seule ; fonds seul ; indice | 0,20 ; 0,32 ; 0,33 | 5,71 % ; 5,00 % ; 5,00 % |

Les deux ratios classent les allocations en sens contraire : B l'emporte par le ratio de Sharpe, A par le ratio de Treynor.

**Corrélation et diversification au sens de Markowitz (1952) (0,5 pt).** Le risque d'une allocation n'est pas la moyenne pondérée des risques de ses supports : il dépend de leur covariance. Si les rentabilités étaient parfaitement corrélées (coefficient de 1), l'écart-type serait la moyenne pondérée : 0,4 × 40 + 0,6 × 6 = 19,60 % pour A et 0,4 × 14 + 0,6 × 6 = 9,20 % pour B. Avec les corrélations fournies, il tombe à 17,09 % et 8,28 % : la diversification retire 2,51 points à A et 0,92 point à B. La faible corrélation de LUDÉRIAN avec le fonds obligataire (0,20) rend la diversification plus efficace dans A, mais elle ne compense pas l'ampleur du risque de LUDÉRIAN : A reste deux fois plus risquée que B pour 1,40 point de rentabilité espérée en plus. Combiner seulement deux supports ne diversifie pas le risque spécifique d'une action isolée : c'est le fonds de 400 valeurs qui le fait, à l'intérieur de B.

**Quel ratio pour NOCTÉVAL ? (0,25 pt).** Le ratio de Treynor mesure la prime par unité de risque systématique : il convient pour une ligne d'un portefeuille déjà diversifié, dont le risque spécifique disparaît dans l'ensemble. Il flatte ici A, parce qu'il ignore les 72 % de risque spécifique de LUDÉRIAN. La réserve pour aléas, elle, est un placement isolé, qui doit être disponible si la production prend du retard : c'est son risque total qui compte, donc le **ratio de Sharpe**, qui favorise B.

**Risque ajouté au risque propre de NOCTÉVAL et recommandation (1 pt).**
- LUDÉRIAN vend sur les mêmes boutiques numériques, aux mêmes joueurs, avec les mêmes contraintes de coûts des équipes : sa rentabilité est corrélée à 0,65 avec celle de l'action NOCTÉVAL. Une hausse de la commission des boutiques, un recul de la demande de jeux ou une tension sur les salaires des développeurs toucheraient à la fois l'activité du groupe et la réserve censée le protéger.
- La réserve sert précisément en cas de **retard de la sortie** : c'est dans les mauvais scénarios du secteur qu'elle serait mobilisée, et c'est alors que la poche LUDÉRIAN risquerait d'avoir baissé. En 2023, l'échec d'un seul jeu a fait perdre 30,4 % au titre : 12 000 × (− 30,4 %) = **− 3 648 k€** sur la poche, soit plus de deux tiers d'un mois de production. Le pari concentre le risque au lieu de le réduire.
- Les actionnaires de NOCTÉVAL, déjà exposés au jeu vidéo, peuvent acheter eux-mêmes des actions LUDÉRIAN s'ils le souhaitent : l'entreprise ne crée aucune valeur en prenant ce pari pour eux, et le marché ne rémunère pas le risque spécifique.
- L'argument d'une future prise de participation relève d'une décision stratégique, à étudier comme telle ; il ne justifie pas de placer une réserve de sécurité en actions d'un concurrent.
- **Recommandation** : rejeter A et retenir **B**, dont le ratio de Sharpe est meilleur et le risque deux fois plus faible. B respecte la limite de 40 % d'actions fixée par la charte pour la réserve pour aléas (A aussi, mais en une seule action d'un concurrent) ; la charte n'interdit pas une part actions plus faible. Comme la réserve peut être appelée dès l'automne 2028 si la sortie est retardée, une part actions plus faible que 40 %, ou le placement des premiers mois de retard possibles (environ 15 M€) sur des supports à court terme, serait défendable.

**Réponses tolérées** : covariances et variances en fraction (0,0048 ; 0,0292) ; écart-type de B à 8,27 % ou 8,28 % selon l'arrondi de la variance ; recommandation d'une allocation encore plus prudente que B si elle est justifiée par l'horizon, y compris placer toute la réserve sur des supports sans actions si elle est justifiée par une mobilisation possible dès l'automne 2028 ; ratios des supports isolés non calculés.

**Erreurs fréquentes**
- Calculer l'écart-type de l'allocation comme moyenne pondérée des écarts-types (19,60 % et 9,20 %), ou oublier le facteur 2 de la covariance.
- Parts systématique et spécifique calculées sur les écarts-types (21 / 40 = 52,50 %) au lieu des variances.
- Retenir A sur le seul ratio de Treynor, sans voir qu'il ignore le risque spécifique.
- Recalculer les corrélations, qui sont fournies.
- `JUR-T13` — exposé de la diversification sans les chiffres des deux allocations ni le lien avec l'activité de NOCTÉVAL.

---

### 2.4 Réaction du cours aux deux annonces et affirmation de sous-évaluation (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Annonce n° 1 : + 17,24 % du 19 mars au 8 avril (indice + 0,21 %), information publique des classements déjà intégrée ; + 14,05 % le jour de l'annonce (indice + 0,31 %), surprise intégrée dans la séance ; + 0,57 % ensuite (indice + 0,51 %), pas de dérive : efficience au sens semi-fort ; hausse de + 31,05 % jusqu'au 29 mai sans information nouvelle, que l'efficience n'explique pas (valorisée, non exigée) | 0,75 |
| 2.4-02 | Annonce n° 2 : − 15,88 % le lendemain (indice − 0,10 %), plus bas de − 21,84 % à l'ouverture ; rebond de + 8,55 % en quinze jours ; perte de capitalisation de 153,6 M€ très supérieure au coût annoncé : sur-réaction partielle, mais aussi révision du risque d'exécution de la suite | 0,75 |
| 2.4-03 | Sous-évaluation : en efficience semi-forte, le cours reflète l'information publique ; l'affirmation repose sur une information privée (avancement de la production) que le marché n'a pas ; elle ne vaut que si elle est rendue publique et vérifiable ou appuyée par un signal coûteux (Spence, 1973) ; optimisme des dirigeants à relativiser (report de « Valsombre ») | 0,5 |

**Rappel (Fama, 1970).** Un marché est efficient si les cours reflètent à tout instant l'information disponible. Au sens **faible**, l'information contenue dans les cours passés ; au sens **semi-fort**, toute l'information publique ; au sens **fort**, toute l'information, y compris privée. Sur un marché efficient au sens semi-fort, une annonce est intégrée dès sa publication, sans dérive ensuite : seule sa part inattendue fait bouger le cours. La comparaison avec l'indice isole la part propre au titre.

**Annonce n° 1 du 9 avril 2026 (0,75 pt).**

| Période | NOCTÉVAL | Indice | Écart |
|---|---:|---:|---:|
| Du 19 mars au 8 avril 2026 (avant l'annonce) | + 17,24 % | + 0,21 % | + 17,04 points |
| Du 8 au 9 avril 2026 (jour de l'annonce) | **+ 14,05 %** | + 0,31 % | + 13,74 points |
| Du 9 au 16 avril 2026 | + 0,57 % | + 0,51 % | + 0,06 point |
| Du 16 avril au 29 mai 2026 | + 31,05 % | + 1,22 % | + 29,83 points |
| Du 29 mai au 31 décembre 2026 | − 14,78 % | + 0,60 % | − 15,39 points |

- La hausse d'avant l'annonce n'est pas une anomalie : les classements des meilleures ventes étaient publics depuis la sortie, et le marché les a intégrés au fil des semaines.
- Le jour de l'annonce, le titre gagne 14,05 % (+ 103,2 M€ de capitalisation), contre 0,31 % pour l'indice : la part inattendue (3,2 millions d'exemplaires au lieu de 2 millions) est intégrée dans la séance, puis le cours ne dérive plus (+ 0,06 point d'écart en une semaine). C'est le profil d'un marché efficient au sens semi-fort.
- En revanche, la hausse de 31,05 % jusqu'au 29 mai, sans aucune information nouvelle de la société, puis la baisse de 14,78 % jusqu'à la fin de l'année ne s'expliquent pas par l'information : elles évoquent un emballement des actionnaires individuels (forum du 12 mai, question 2.5).

**Annonce n° 2 du 13 janvier 2027 (0,75 pt).**

| Période | NOCTÉVAL | Indice | Écart |
|---|---:|---:|---:|
| Du 13 au 14 janvier 2027 (lendemain de l'annonce) | **− 15,88 %** | − 0,10 % | − 15,78 points |
| Plus bas du 14 janvier à 9 h 04 | − 21,84 % | | |
| Du 14 au 29 janvier 2027 | + 8,55 % | + 0,70 % | + 7,86 points |
| Du 13 janvier au 31 mars 2027 | − 6,95 % | + 1,59 % | − 8,54 points |

- Publiée après la clôture, l'annonce est intégrée dès l'ouverture suivante : la vitesse de réaction est conforme à l'efficience.
- L'ampleur interroge : la capitalisation perd 24 × (40,30 − 33,90) = **153,6 M€** en une séance, alors que la direction chiffre le report à 4 M€ de coûts et au décalage d'un an de 30 M€ de chiffre d'affaires. Le plongeon de 21,84 % en quatre minutes, puis le rebond de 8,55 % en deux semaines, traduisent une **sur-réaction** que le marché corrige en partie, amplifiée par le retrait des opérateurs à haute fréquence (question 2.6).
- Une partie de la baisse reste au 31 mars (− 6,95 %, contre + 1,59 % pour l'indice) : le marché a aussi révisé un risque que l'annonce révèle, celui de la capacité des studios à tenir leurs calendriers, qui pèse sur la suite des « Brumes d'Aldrec ». Cette révision est rationnelle.

**L'action est-elle sous-évaluée ? (0,5 pt).**
- Si le marché est efficient au sens semi-fort, le cours de 37,50 € (900 M€ de capitalisation) est la meilleure estimation de la valeur compte tenu de l'information publique : il ne peut pas être durablement sous-évalué au vu de cette information.
- Mme VARLOTTE invoque une information **privée** (« nous savons où en est la production »). L'efficience au sens fort n'est pas vérifiée : le marché ne connaît pas cette information, et les dirigeants ne peuvent pas l'exploiter. L'écart qu'elle perçoit est un problème d'**asymétrie d'information** (Akerlof, 1970).
- Une déclaration ne coûte rien : pour être crue, l'information doit être rendue publique et vérifiable (étapes de la production, démonstrations, calendrier) ou appuyée par un signal coûteux à imiter (Spence, 1973).
- Enfin, la confiance des dirigeants est à relativiser : le report de « Valsombre », annoncé deux mois plus tôt, montre que les calendriers internes peuvent glisser, et le marché intègre ce risque.

**Réponses tolérées** : variations calculées sur d'autres dates proches si elles sont cohérentes ; écart avec l'indice présenté comme une différence de variations ou comme une comparaison qualitative ; référence à la forme forte pour l'information privée sans le mot « asymétrie ».

**Erreurs fréquentes**
- Conclure à l'inefficience à cause de la hausse d'avant l'annonce, alors que l'information (classements des ventes) était publique.
- Conclure à l'efficience sans relever la hausse de mai 2026 ni la sur-réaction de janvier 2027.
- Confondre efficience et « juste prix » ou prévisibilité des cours.
- `JUR-M01` — analyse sans référence à Fama (1970) et aux formes d'efficience ; `JUR-T13` — exposé théorique sans les dates et les variations de l'annexe.

---

### 2.5 Biais comportementaux de la proposition et du forum, nuance de l'efficience, règles de placement (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Proposition de M. ESCAMBRE : biais de familiarité, excès de confiance, extrapolation d'une année exceptionnelle (64 % en 2026, moyenne de 12 % qui masque − 30,4 % en 2023 et une rentabilité composée d'environ 6,1 % par an, non exigée), ancrage sur la moyenne | 0,5 |
| 2.5-02 | Forum : mimétisme (12 mai 2026), familiarité et excès de confiance avec concentration de l'épargne (20 mai), sur-réaction et heuristique de disponibilité (14 janvier 2027), ancrage sur le prix d'achat et aversion aux pertes (20 mars 2027) | 0,5 |
| 2.5-03 | Nuance de l'efficience : heuristiques et biais (Kahneman et Tversky, 1973), erreurs corrélées qui ne se compensent pas, limites de l'arbitrage sur une valeur moyenne détenue par des particuliers ; écarts temporaires (mai 2026, 14 janvier 2027) corrigés ensuite | 0,25 |
| 2.5-04 | Deux règles : interdiction des lignes isolées et des titres du secteur dans les placements de trésorerie, diversification obligatoire ; décision collégiale sur analyse écrite (horizon, ratio de Sharpe, perte dans une année défavorable), rééquilibrage mécanique, sans recherche du « bon moment » | 0,25 |

**Biais de la proposition de M. ESCAMBRE (0,5 pt).**
- **Familiarité** : préférer ce que l'on connaît (« les jeux vidéo, c'est notre métier ») plutôt qu'un portefeuille diversifié ; connaître les jeux d'un concurrent ne donne aucun avantage sur le cours, qui intègre déjà l'information publique (question 2.4).
- **Excès de confiance** : surestimer sa capacité à juger LUDÉRIAN (« personne ne connaît mieux que nous ») et à prévoir ses succès.
- **Extrapolation d'un passé récent et marquant** (représentativité, disponibilité) : les 64 % de 2026 occupent tout le raisonnement ; la moyenne arithmétique de 12 % masque l'année 2023 (− 30,4 %) et une rentabilité composée d'environ 6,1 % par an (non exigée), inférieure à celle du fonds diversifié (environ 7,7 %). Le chiffre de 12 % sert d'**ancre**.

**Biais des actionnaires individuels (0,5 pt).**
- 12 mai 2026 : **mimétisme** (« tout le forum est rentré », objectif de 60 € relayé par des vidéastes) et peur de manquer la hausse ; il éclaire la hausse de 31 % sans information nouvelle.
- 20 mai 2026 : **familiarité** et **excès de confiance** du joueur qui croit mieux connaître le studio que les analystes, avec une épargne concentrée à 80 % sur un seul titre.
- 14 janvier 2027 : **sur-réaction** fondée sur une information marquante (heuristique de disponibilité) : un report d'un jeu moyen est extrapolé à la suite des « Brumes d'Aldrec », dont le calendrier est pourtant confirmé ; ces ventes à l'ouverture alimentent le plus bas de 31,50 €.
- 20 mars 2027 : **ancrage** sur le prix d'achat de 46 € et **aversion aux pertes** (« vendre maintenant, ce serait accepter ma perte ») : l'investisseur garde un titre perdant pour ne pas constater la perte (effet de disposition), sans rapport avec sa valeur.

**La finance comportementale nuance l'efficience (0,25 pt).** L'efficience suppose des investisseurs rationnels ou, à défaut, des erreurs individuelles qui se compensent et des arbitragistes qui corrigent les écarts. Kahneman et Tversky (1973) montrent que les décisions reposent sur des heuristiques qui produisent des biais **systématiques** : lorsque de nombreux actionnaires individuels, « souvent joueurs eux-mêmes », partagent les mêmes biais et s'imitent sur un forum, leurs erreurs sont corrélées et déplacent le cours (mai 2026, ouverture du 14 janvier 2027). Sur une valeur moyenne du compartiment B, l'arbitrage est limité. Les données montrent toutefois que ces écarts restent temporaires (baisse après le 29 mai, rebond après le 14 janvier) : l'efficience reste une bonne approximation de la tendance, pas de chaque séance.

**Règles pour la politique de placement (0,25 pt).** Deux règles attendues parmi :
- interdire, pour les placements de trésorerie, les actions isolées et les titres d'entreprises du même secteur que le groupe ; n'admettre les actions qu'au travers de fonds diversifiés et dans une limite fixée selon l'horizon ;
- décider collégialement (comité de trésorerie associant un administrateur indépendant), sur une analyse écrite qui fixe l'horizon, le risque total (ratio de Sharpe, perte possible dans une année défavorable) et compare au moins deux solutions ;
- fixer des poids cibles et un rééquilibrage mécanique annuel, sans chercher le « bon moment » pour entrer ou sortir ;
- côté communication financière, informer régulièrement les actionnaires individuels (calendrier, risques de la production) pour limiter les rumeurs.

**Réponses tolérées** : autres biais pertinents et justifiés par les extraits (biais de confirmation, cadrage) ; cygnes noirs (Taleb, 2007) ou simplexité (Berthoz, 2009) s'ils sont reliés au cas ; rentabilité composée non calculée.

**Erreurs fréquentes**
- Réciter une liste de biais sans les rattacher à un message daté.
- Attribuer la finance comportementale à Fama, ou se tromper sur les auteurs et leur date (F10).
- Chiffrer l'aversion aux pertes, approfondissement exclu du programme.
- `JUR-M01` — biais sans référence aux auteurs ; `JUR-T13` — exposé psychologique sans lien avec les placements de NOCTÉVAL.

---

### 2.6 Gestion de trésorerie par algorithme, trading à haute fréquence, nouveaux acteurs et recommandation (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Principe : prévision des besoins par intelligence artificielle et répartition automatique selon des règles fixées par l'entreprise ; apports (prévision, plus de supports et de contreparties, réactivité, discipline sans biais, suivi continu) ; risques (modèle calé sur des taux stables et des besoins réguliers, opacité, absence de validation, données bancaires et cyber, jeune prestataire, responsabilité limitée à 90 k€, sortie à l'échéance pour une partie des fonds) | 0,75 |
| 2.6-02 | Gain brut 0,25 % × 60 000 = 150 k€ ; frais 60 + 30 = 90 k€ ; gain net **60 k€** par an (0,10 % de l'encours, 0,05 % de la réserve) ; encours d'équilibre 30 / (0,25 % − 0,10 %) = **20 M€** | 0,5 |
| 2.6-03 | Trading à haute fréquence : liquidité accrue en temps normal (capitaux échangés de 0,8 à 6,2 M€, écart entre prix d'achat et de vente de 0,38 % à 0,11 %), coût de transaction plus faible, intégration rapide de l'information ; mais liquidité qui disparaît dans la tension (14 janvier 2027 : − 21,84 % en quatre minutes, écart de 2,5 %) et amplitude des séances en hausse (2,1 % à 3,4 %) | 0,75 |
| 2.6-04 | Rôle des nouveaux acteurs (fintech prestataire de trésorerie, en partenariat avec les banques ; opérateurs algorithmiques devenus teneurs de marché) et conséquences pour NOCTÉVAL (coût de la liquidité du titre, communication hors séance) ; recommandation argumentée : ne pas confier la réserve de production en l'état, ou seulement avec des conditions (règles adossées au calendrier, seuils de validation, responsabilité, réversibilité) | 1 |

**Principe, apports, risques et coût (0,75 pt).**
- **Principe** : une gestion pilotée par algorithme remplace les arbitrages quotidiens du trésorier par des règles exécutées automatiquement. Un premier algorithme d'intelligence artificielle apprend, sur les données passées des comptes et sur le budget, à prévoir les besoins de trésorerie ; un second répartit chaque jour les excédents entre les supports, dans les limites fixées par l'entreprise.
- **Apports** : prévision plus fine des besoins ; accès à un plus grand nombre de supports et de contreparties (15 OPC, 6 banques, 40 émetteurs), donc moins de concentration qu'avec trois supports ; réaction rapide aux variations des taux ; application des règles sans les biais de la question 2.5 ; suivi en continu ; gain de temps pour l'équipe financière. Une société de gestion agréée par l'AMF et adossée à une grande banque offre des garanties d'organisation.
- **Risques** : le modèle a été calé sur 2024-2026, période de taux courts stables, et sur des entreprises aux besoins réguliers, alors que ceux d'une production sont irréguliers et qu'un retard en est précisément le risque principal ; fonctionnement peu lisible (« boîte noire ») et réallocations sans validation préalable ; accès aux données bancaires du groupe, donc risque de cyberattaque et dépendance à un prestataire jeune ; responsabilité limitée à une année de frais (90 k€) pour un encours de 60 M€ ; en cas de fin du mandat, les fonds en comptes à terme et en NEU CP ne reviennent qu'à leur échéance, jusqu'à douze mois plus tard, ce qui peut heurter le calendrier et le minimum de 20 M€ disponible ; rendement supplémentaire non garanti.

**Gain net et encours d'équilibre (0,5 pt).** Sur un encours moyen de 60 000 k€ :
- rendement supplémentaire avant frais : 60 000 × 0,25 % = 150 k€ ;
- frais : 60 000 × 0,10 % + 30 = 60 + 30 = 90 k€ ;
- **gain net : 60 k€ par an**, soit 0,10 % de l'encours confié et 0,05 % de la réserve de 120 M€ ;
- encours à partir duquel l'offre devient rentable : 30 / (0,25 % − 0,10 %) = 20 000 k€ = **20 M€**. Un essai limité à 20 M€ ne rapporterait donc rien.

**Trading à haute fréquence et action NOCTÉVAL (0,75 pt).**
- **En temps normal, plus de liquidité** : la part des opérateurs à haute fréquence passe de 14 % à 41 % des échanges, les capitaux échangés par séance de 0,8 à 6,2 M€ et l'écart entre meilleurs prix d'achat et de vente de 0,38 % à 0,11 % du cours. Les actionnaires, y compris individuels, achètent et vendent à moindre coût ; une meilleure liquidité réduit la prime de liquidité que les investisseurs exigent, donc le coût des fonds propres. La rapidité des ordres accélère aussi l'intégration de l'information (question 2.4).
- **Dans la tension, une liquidité fragile et plus de volatilité** : ces opérateurs ne détiennent pas le titre et retirent leurs ordres quand l'incertitude monte. Le 14 janvier 2027, le cours a perdu 21,84 % en quatre minutes, l'écart a atteint 2,5 % et la cotation a été interrompue ; l'amplitude moyenne des séances est passée de 2,1 % à 3,4 %. Les algorithmes peuvent amplifier un mouvement de vente : la liquidité disparaît au moment où les vendeurs en ont besoin.

**Rôle des nouveaux acteurs et recommandation (1 pt).**
- **Nouveaux acteurs** : les fintechs comme TRÉSALGO offrent aux entreprises des services autrefois rendus par les banques ou par le trésorier, souvent en partenariat avec elles (une grande banque est au capital de TRÉSALGO) ; elles réduisent les coûts et élargissent l'accès aux supports, mais déplacent une partie du risque vers des algorithmes et des prestataires récents. Les opérateurs de trading à haute fréquence sont devenus les principaux teneurs de marché du titre : ils déterminent le coût et la qualité de sa liquidité.
- **Conséquences pour NOCTÉVAL** : continuer à publier les informations importantes hors séance, comme le 13 janvier, avec une communication claire et chiffrée, pour limiter les réactions excessives à l'ouverture ; suivre la liquidité du titre, qui conditionne l'intérêt des investisseurs et le coût des fonds propres.
- **Recommandation** : ne pas confier, en l'état, la réserve de la production à TRÉSALGO. Le gain attendu (60 k€ par an, non garanti) est faible au regard des risques pendant la phase la plus sensible de la production : liquidité au jour le jour imposée par la politique, calendrier irrégulier, réallocations sans validation, responsabilité plafonnée à 90 k€. Si le groupe veut néanmoins l'essayer, il doit négocier des règles adossées au calendrier de l'annexe 2.1 (minimum de 20 M€ en OPC, échéances au plus tard aux dates de décaissement), une validation au-delà d'un seuil, une responsabilité relevée et un examen préalable de la sécurité des accès ; l'offre pourrait être réexaminée après la sortie du jeu, pour une trésorerie plus stable.

**Réponses tolérées** : recommandation d'accepter l'offre sur une partie de l'encours, si les conditions de liquidité et de contrôle sont posées et si le candidat voit que l'essai doit dépasser 20 M€ pour être rentable ; mention de l'encadrement européen des algorithmes de négociation ou de l'intelligence artificielle sans détail juridique.

**Erreurs fréquentes**
- Comparer le gain brut (150 k€) aux frais proportionnels seulement, en oubliant l'abonnement.
- Décrire le fonctionnement technique des algorithmes au lieu de leurs effets financiers (hors du programme de l'UE 2).
- Présenter le trading à haute fréquence comme seulement nuisible ou seulement favorable, sans les données des deux périodes.
- `JUR-M02` — nouveaux acteurs évoqués sans les comparer aux intermédiaires traditionnels ; `JUR-T13` — recommandation sans chiffre du cas.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 77 ; programme l. 612-613 | supports de placement (actions, obligations, OPCVM), choix selon l'horizon, le couple rendement-risque et les contraintes de trésorerie | [V] | F07 § 0 et 4.2 |
| Guide pédagogique DSCG, juillet 2026, p. 74-77 ; programme l. 578-592 | rentabilité espérée, écart-type et bêta à partir de séries, MEDAF, risque spécifique et systématique, portefeuille de deux titres, Sharpe et Treynor, corrélations fournies | [V] | F10 § 2 |
| Guide pédagogique DSCG, juillet 2026, p. 73-74 ; programme l. 564-576 | efficience et ses trois formes, lecture d'une chronologie sans démarche statistique, biais et finance comportementale | [V] | F06 § 3 et 4 |
| Programme l. 599-604 ; guide p. 51 | numérique et algorithmes en finance, intelligence artificielle, trading à haute fréquence, nouveaux acteurs | [V] | F06 § 0 et 6 |
| Fama (1970) | efficience informationnelle, formes faible, semi-forte et forte | [V programme 5.1] | F10 § 1 |
| Kahneman et Tversky (1973) | heuristiques et biais | [V programme 5.1] | F10 § 1 |
| Markowitz (1952) | diversification et rôle de la corrélation | [V programme 5.3] | F10 § 2 |
| Sharpe (1964) ; Treynor (1965) | MEDAF ; ratios de Sharpe et de Treynor | [S] | F10 § 2 |
| Akerlof (1970) ; Spence (1973) | asymétrie d'information ; signal coûteux et crédible | [V programme 5.1 et 4.1] | F10 § 1 et 3 |
| Taux sans risque de 4,0 % et prime de risque du marché de 5,0 % ; taux des placements à court terme de 2,60 % à 3,15 % | hypothèses d'énoncé : taux sans risque et prime dans les fourchettes de F11 ; taux au jour le jour voisin de l'€STR de F11 (2,44 % en octobre 2026), majoré d'une prime de durée (compte à terme) et de crédit (NEU CP notés A-2) | [S] | F11 § 1 et 2 |
| Séries de rentabilité, corrélations, conditions des supports, cours, annonces, forum, offre de la fintech, note sur le trading à haute fréquence | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 2.1 à 2.5 |
