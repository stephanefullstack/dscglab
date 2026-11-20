# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 57 — Dossier 3 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F02 coût du capital, F06 marchés et finance comportementale, F10 auteurs et théories, F11 données de marché d'octobre 2026, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (flux annuels des scénarios central et fort, VAN, TRI et indice de profitabilité du scénario central, VAN des trois scénarios, espérance, écart-type, coefficient de variation et probabilité d'une VAN négative, plans de financement, tableau du prêt d'équipement et son coût après IS, rentabilités moyennes, variances, écarts-types, covariances et bêta des fonds, rentabilité et risque des deux allocations, portefeuille de variance minimale, variance et écart-type d'un portefeuille équipondéré de N actions, MEDAF, rentabilité espérée d'une part et valeur au taux exigé, barème, liste noire, hors-programme ; flux du scénario faible, effet des deux solutions sur la dette financière nette et la marge de la clause, parts du risque spécifique, écart au MEDAF et illustrations vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une espérance de VAN calculée avec une VAN centrale erronée à la question 3.1).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Flux du projet d'automatisation, VAN, TRI et indice de profitabilité du scénario central | `7.1.a` Évaluer et classer des projets en milieu certain | 2 |
| 3.2 VAN des scénarios faible et fort, espérance, écart-type, coefficient de variation, probabilité d'une VAN négative, conclusion | `7.1.b` Évaluer et classer des projets en milieu incertain | 2 |
| 3.3 Montant à financer, effet des deux solutions sur la dette financière nette et la clause financière, financement hiérarchique et théorie du compromis, recommandation | `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives ; `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière et identifier ses déterminants | 3 |
| 3.4 Rentabilité et risque des fonds obligataire et actions, deux allocations, portefeuille de variance minimale, rôle de la corrélation, allocation du salarié type | `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres ; `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) | 3 |
| 3.5 Diversification d'un portefeuille équipondéré de N actions, risque spécifique et risque systématique | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique | 2 |
| 3.6 Bêta du fonds actions, MEDAF, rentabilité espérée d'une part sur un an, limites du MEDAF | `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance ; `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier | 2 |
| 3.7 Biais des salariés épargnants, apports et limites de l'affectation par défaut à la gestion pilotée | `5.1.d` Maîtriser les grands enseignements de la finance comportementale | 2 |
| **Total** | | **16** |

Part du calcul : environ 8,75 points (3.1-01 à 3.1-03, 3.2-01 et 3.2-02, 3.3-01 et 3.3-02, 3.4-01 à 3.4-03, 3.5-01 et 3.5-02, 3.6-01 et 3.6-02). Part de l'analyse : environ 7,25 points. Les questions 3.5 à 3.7 valent 6 points et se traitent vite : elles ne doivent pas être sacrifiées faute de temps en fin d'épreuve (`JUR-T15`).

---

### 3.1 Flux du projet d'automatisation, VAN, TRI et indice de profitabilité du scénario central (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Investissement **3 150 k€** (2 800 + 350), dotation **450** ; économies nettes 9 × 50 − 120 − 30 = **300** ; marge 45 % × 1 200 = 540 ; EBE **840** ; IS 25 % × (840 − 450) = 97,5 ; flux annuel **742,5 k€** ; date 0 : − 3 150 − BFR 180 = **− 3 330** ; 2035 : 742,5 + 180 + 140 × 75 % = **1 027,5** | 0,75 |
| 3.1-02 | VAN à 7,50 % = 742,5 × 5,296601 + 285 × 0,602755 − 3 330 = **775 k€** | 0,5 |
| 3.1-03 | TRI = **13,70 %** (interpolation entre 13 % et 14 %) ; indice de profitabilité = 4 104,51 / 3 330 = **1,23** | 0,5 |
| 3.1-04 | Conclusion : VAN positive, TRI supérieur au CMPC, 0,23 € de valeur créée par euro engagé : projet rentable dans le scénario central, sous réserve des contrats (question 3.2) | 0,25 |

**Construction des flux (0,75 pt).** Les économies de charges et la marge sur le chiffre d'affaires supplémentaire forment l'EBE du projet ; l'impôt est calculé sur le résultat d'exploitation, après la dotation aux amortissements ; le BFR est un décaissement de la date 0, récupéré à la fin.

| k€ | Calcul | Scénario central |
|---|---|---:|
| Économies de personnel | 9 postes × 50 | 450 |
| Maintenance et consommables de la chaîne | 120 + 30 | − 150 |
| Économies nettes de charges | | 300 |
| Marge sur coûts variables du chiffre d'affaires supplémentaire | 45 % × 1 200 | 540 |
| **EBE du projet** | | **840** |
| Dotation aux amortissements | 3 150 / 7 | − 450 |
| Résultat d'exploitation | | 390 |
| IS à 25 % | | − 97,5 |
| **Flux annuel** (EBE − IS), 2029 à 2035 | | **742,5** |

| k€ | Date 0 (31/12/2028) | 2029 à 2034 | 2035 |
|---|---:|---:|---:|
| Investissement (2 800 + 350) | − 3 150 | | |
| BFR (15 % × 1 200) constitué, puis récupéré | − 180 | | + 180 |
| Flux annuel | | 742,5 | 742,5 |
| Prix de revente net d'impôt (140 × 75 %) | | | + 105 |
| **Flux du projet** | **− 3 330** | **742,5** | **1 027,5** |

**VAN (0,5 pt).** Coefficient d'actualisation de sept flux constants à 7,50 % : [1 − 1,075^−7] / 0,075 = 5,296601 ; 1,075^−7 = 0,602755.
VAN = 742,5 × 5,296601 + (180 + 105) × 0,602755 − 3 330 = 3 932,73 + 171,79 − 3 330 = **775 k€** (774,51).

**TRI et indice de profitabilité (0,5 pt).** À 13 % : VAN = 742,5 × 4,422610 + 285 × 0,425061 − 3 330 = 75 k€ ; à 14 % : 742,5 × 4,288305 + 285 × 0,399637 − 3 330 = − 32 k€ (non exigés). Par interpolation : 13 % + 74,93 / (74,93 + 32,04) × 1 % = **13,70 %**. Indice de profitabilité = valeur actuelle des flux des années 1 à 7 / décaissement initial = (774,51 + 3 330) / 3 330 = **1,23**.

**Conclusion (0,25 pt).** Dans le scénario central, le projet crée de la valeur : VAN de 775 k€, TRI de 13,70 % supérieur au CMPC de 7,50 %, chaque euro investi rapporte 1,23 € en valeur actuelle. Mais près des deux tiers de l'EBE (540 sur 840) viennent de contrats qui ne sont pas encore signés : la question 3.2 en mesure le risque. Le projet apporte aussi des avantages non chiffrés : délai d'analyse divisé par plus de deux, moins d'erreurs d'identification et de tubes perdus, moindre dépendance à des postes de techniciens difficiles à pourvoir.

**Réponses tolérées** : VAN de 774 à 776 k€ selon les arrondis ; TRI de 13,7 % ; flux annuel présenté sous la forme 75 % × EBE + 25 % × dotation = 630 + 112,5 ; revente comptée après impôt dans le flux de 2035 sous une autre présentation.

**Erreurs fréquentes**
- Oublier le BFR (VAN de 846 k€) ou ne pas le récupérer en 2035.
- Ne pas imposer le prix de revente alors que la valeur nette comptable est nulle (VAN de 796 k€).
- Déduire les intérêts du prêt des flux du projet : le financement est jugé à part (question 3.3).
- Appliquer l'IS à l'EBE sans déduire la dotation.
- `JUR-T04` — VAN, TRI et indice de profitabilité sont des acquis du DCG.

**Références** : F01 § 4 (VAN, TRI par interpolation, indice de profitabilité) [V programme 7.1.a ; guide p. 81].

---

### 3.2 VAN des scénarios, espérance, écart-type et probabilité d'une VAN négative (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Faible : EBE 300, résultat d'exploitation − 150, économie d'impôt 37,5, flux **337,5**, pas de BFR, VAN = **− 1 299 k€** ; fort : EBE 1 200, flux **1 012,5**, BFR 300, VAN = **2 157 k€** | 0,75 |
| 3.2-02 | Espérance de la VAN **602 k€** ; écart-type **1 234 k€** ; coefficient de variation **2,05** ; probabilité d'une VAN négative **25 %** | 0,75 |
| 3.2-03 | Conclusion : projet rentable en espérance mais très risqué ; le risque tient aux contrats (les économies seules ne paient pas la chaîne) ; sécuriser les contrats avant la commande ; la possibilité d'étendre l'automatisation plus tard ajoute une flexibilité non chiffrée | 0,5 |

**VAN des scénarios (0,75 pt).**

| k€ | Faible | Central | Fort |
|---|---:|---:|---:|
| Chiffre d'affaires supplémentaire | 0 | 1 200 | 2 000 |
| EBE = 300 + 45 % × CA | 300 | 840 | 1 200 |
| Résultat d'exploitation (EBE − 450) | − 150 | 390 | 750 |
| IS à 25 % (économie d'impôt si négatif) | + 37,5 | − 97,5 | − 187,5 |
| **Flux annuel** | **337,5** | **742,5** | **1 012,5** |
| BFR (15 % du CA) | 0 | 180 | 300 |
| Flux de la date 0 | − 3 150 | − 3 330 | − 3 450 |
| Flux de 2035 (flux annuel + BFR + 105) | 442,5 | 1 027,5 | 1 417,5 |
| **VAN à 7,50 %** | **− 1 299** | **775** | **2 157** |
| Probabilité | 25 % | 50 % | 25 % |

- Faible : 337,5 × 5,296601 + 105 × 0,602755 − 3 150 = 1 787,60 + 63,29 − 3 150 = **− 1 299 k€**. Le résultat d'exploitation du projet est négatif : l'économie d'impôt de 37,5 k€ est imputée sur les autres bénéfices du groupe (annexe 3.7).
- Fort : 1 012,5 × 5,296601 + 405 × 0,602755 − 3 450 = 5 362,81 + 244,12 − 3 450 = **2 157 k€**.

**Espérance et risque (0,75 pt).**
- E(VAN) = 0,25 × (− 1 299,11) + 0,50 × 774,51 + 0,25 × 2 156,92 = − 324,78 + 387,26 + 539,23 = **602 k€**.
- Variance = 0,25 × (− 1 900,82)² + 0,50 × (172,80)² + 0,25 × (1 555,21)² = 903 277 + 14 930 + 604 673 = 1 522 880 ; écart-type = **1 234 k€**.
- Coefficient de variation = 1 234,05 / 601,71 = **2,05**. La VAN n'est négative que dans le scénario faible : **probabilité de 25 %**, lue sur les scénarios.

**Conclusion (0,5 pt).**
- Le projet est rentable **en espérance** (602 k€), mais son risque est élevé : l'écart-type vaut plus de deux fois l'espérance et une fois sur quatre le groupe perdrait 1 299 k€ de valeur.
- Le risque ne vient pas de la technique, mais des **contrats** : les économies de personnel (300 k€ nets par an) ne paient pas à elles seules une chaîne de 3 150 k€. Chaque tranche de 100 k€ de chiffre d'affaires supplémentaire ajoute 172,80 k€ de VAN ; la VAN s'annule vers 752 k€ de chiffre d'affaires supplémentaire par an, soit environ 63 % du scénario central (calcul non exigé).
- Recommandation : investir, mais **après avoir obtenu des engagements** des cliniques et des établissements (lettres d'engagement, contrats signés avant la commande), ce qui déplace l'essentiel du risque avant la décision. La **possibilité d'étendre l'automatisation plus tard** (module d'archivage de 400 k€ décidé en 2031 au vu des contrats) ajoute une flexibilité : le groupe n'engage la deuxième étape que si l'activité la justifie. Cette flexibilité a une valeur que la VAN des trois scénarios ne mesure pas ; elle n'est pas chiffrée ici.
- Limites : trois scénarios et des probabilités subjectives ; une baisse des tarifs nationaux réduirait aussi la marge des nouveaux contrats ; les économies supposent que les départs de techniciens permettent de ne pas remplacer neuf postes, et le groupe doit organiser le redéploiement des autres.

**Réponses tolérées** : écart-type de 1 233 à 1 235 k€ selon les arrondis des VAN ; variance calculée sur les VAN arrondies (1 522 921) ; recommandation de différer le projet si elle s'appuie sur le risque des contrats et sur la probabilité de 25 %.

**Erreurs fréquentes**
- Calculer l'espérance avec des probabilités égales (544 k€).
- Garder le BFR du scénario central dans les trois scénarios.
- Calculer l'écart-type sur n − 1 ou sans pondérer par les probabilités : la variance de l'énoncé est pondérée.
- Recourir à une distribution de probabilité théorique pour la probabilité d'une VAN négative : elle se lit sur les scénarios.
- Ne pas accorder l'économie d'impôt du scénario faible, contrairement à l'annexe 3.7.

**Références** : F01 § 5 (milieu probabilisable : espérance et écart-type de la VAN) [V programme 7.1.b ; guide p. 81].

---

### 3.3 Montant à financer, effet sur la dette financière nette et la clause, théories du financement (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Montant à financer **3 330 k€** (investissement 3 150 + BFR 180) ; solution A : autofinancement 1 330 + prêt 2 000 ; solution B : autofinancement 1 330 + capital 2 000 | 0,5 |
| 3.3-02 | Effet au 31/12/2028 : A, dette financière nette **+ 3 330 k€**, au-delà de la marge de 3 000 (dépassement de **330 k€**, rapport supérieur à 2,00, remboursement anticipé possible des 5 000 k€) ; B, **+ 1 330 k€**, marge restante **1 670 k€**, capitaux propres + 2 000 | 0,75 |
| 3.3-03 | Financement hiérarchique (Myers et Majluf, 1984) : autofinancement, puis dette, puis capital en dernier, à cause de l'asymétrie d'information ; appliqué au fonds (rentabilité visée de 14 % contre 3,15 % après IS pour le prêt, droits de contrôle) et aux associés | 0,5 |
| 3.3-04 | Théorie du compromis (Myers, 1977) : économie d'impôt sur les intérêts (21 k€ en 2029) contre coûts de détresse financière (clause, remboursement anticipé, baisse des tarifs) ; le groupe est à son plafond d'endettement en 2028 | 0,5 |
| 3.3-05 | Recommandation argumentée et déterminants de la structure financière : solution A aménagée (réduire la distribution de 2028 ou décaler une partie de la dépense, obtenir de la banque un aménagement de la clause), solution B en dernier recours ; dépassement temporaire (EBE de la chaîne à partir de 2029, remboursement de 400 par an, service de la dette de 484 en 2029 : arguments possibles, non exigés) ; actif nantissable, flux stables, groupe non coté, contrôle des associés | 0,75 |

**Montant à financer et plan de financement (0,5 pt).**

| k€ au 31/12/2028 | Solution A | Solution B |
|---|---:|---:|
| Investissement (2 800 + 350) | 3 150 | 3 150 |
| BFR du projet (scénario central) | 180 | 180 |
| **Montant à financer** | **3 330** | **3 330** |
| Autofinancement disponible en 2028 | 1 330 | 1 330 |
| Prêt d'équipement de la Banque VELMONDE | 2 000 | — |
| Actions nouvelles souscrites par TILVANE Santé Partenaires | — | 2 000 |
| **Total des ressources** | **3 330** | **3 330** |

**Effet sur la dette financière nette et la clause (0,75 pt).** Dans la prévision de M. SAUZELLE, l'autofinancement de 1 330 k€ réduit la dette financière nette ; s'il est consacré au projet, la dette financière nette est plus élevée d'autant.

| k€ au 31/12/2028 | Solution A | Solution B |
|---|---:|---:|
| Autofinancement consacré au projet | + 1 330 | + 1 330 |
| Nouvelle dette | + 2 000 | — |
| **Hausse de la dette financière nette** | **+ 3 330** | **+ 1 330** |
| Marge de la clause sans le projet | 3 000 | 3 000 |
| **Marge restante** | **− 330** (dépassement) | **+ 1 670** |
| Part de la marge consommée | 111 % | 44,33 % |
| Capitaux propres | inchangés | + 2 000 |

- **Solution A** : au 31 décembre 2028, la dette financière nette dépasse de 330 k€ le plafond de 2,00 fois l'EBE, alors que la chaîne n'apporte encore aucun EBE. La Banque VELMONDE pourrait exiger le remboursement anticipé de l'emprunt d'acquisition (5 000 k€ restant dus) : le prêt d'équipement accordé par la même banque mettrait le groupe en défaut au regard de son autre contrat. Le dépassement est **temporaire** (élément non exigé à cet item) : dans le scénario central, et sous l'hypothèse d'un EBE et d'une dette du groupe inchangés par ailleurs, l'EBE du projet (840 k€ par an à partir de 2029) accroît de 2 × 840 = 1 680 k€ la dette financière nette admise, et le prêt se rembourse de 400 k€ par an. Le service de la dette de 2029 (84 d'intérêts + 400 de capital = 484 k€) est couvert 1,53 fois par le flux annuel du scénario central (742,5 k€), mais pas dans le scénario faible (337,5 k€).
- **Solution B** : la dette financière nette n'augmente que de 1 330 k€ et le groupe garde 1 670 k€ de marge ; les capitaux propres augmentent de 2 000 k€, ce qui renforce l'autonomie financière. Le coût est ailleurs : dilution des 28 associés à un prix non encore négocié, droits de contrôle et distribution minimale de 40 % du résultat.

**Financement hiérarchique (0,5 pt).** Selon Myers et Majluf (1984), l'asymétrie d'information entre les dirigeants, qui connaissent la valeur des projets, et les apporteurs extérieurs conduit l'entreprise à se financer d'abord par **autofinancement**, puis par **dette**, et en dernier lieu par **émission d'actions**. Ici :
- l'autofinancement (1 330 k€) est mobilisé en premier dans les deux solutions ;
- le fonds ne connaît ni la qualité du plateau ni les chances d'obtenir les contrats des cliniques : il se protège par une rentabilité visée d'environ 14 % par an, un accord préalable sur les investissements et les dettes et une distribution minimale. Le prêt, garanti par le nantissement de la chaîne, coûte 4,20 %, soit 3,15 % après IS ;
- si les associés jugent le projet rentable, ouvrir le capital revient à partager avec un tiers la valeur qu'ils attendent ; à l'inverse, accepter l'entrée d'un fonds au moment où le groupe est proche de sa capacité d'endettement peut être lu comme un signal de difficulté. Pour un groupe non coté, sans accès au marché financier, la hiérarchie se lit dans le coût et les conditions demandées par le fonds plutôt que dans une baisse de cours.
- La théorie conduit donc à préférer la solution A, conforme aussi à l'opposition de onze associés à l'entrée d'un investisseur extérieur.

**Théorie du compromis (0,5 pt).** Selon la théorie du compromis (Myers, 1977), l'entreprise vise un endettement cible qui équilibre l'**avantage fiscal de la dette** et les **coûts de détresse financière** et d'agence. Ici :
- l'avantage fiscal est réel mais modeste : 84 × 25 % = 21 k€ d'économie d'impôt en 2029, puis de moins en moins à mesure du remboursement ;
- les coûts de détresse sont élevés et proches : le groupe atteint son plafond d'endettement en 2028 (marge consommée à 111 %) ; un dépassement de la clause peut entraîner l'exigibilité de 5 000 k€ ; la baisse annoncée des tarifs nationaux peut réduire l'EBE et donc la marge ; le projet lui-même est risqué (VAN négative une fois sur quatre) ;
- la clause fixe en pratique la cible d'endettement du groupe. La théorie du compromis invite donc à **ne pas ajouter toute la dette en 2028**, ce que la théorie du financement hiérarchique ne dit pas.

**Recommandation et déterminants de la structure financière (0,75 pt).**
- Les **déterminants** jouent pour la dette : la chaîne est un actif corporel que la banque accepte en nantissement ; les flux du groupe sont réglés à 62 % par l'assurance maladie obligatoire, payeur sûr ; le groupe est non coté et détenu par des associés qui exercent dans le groupe et tiennent à garder la maîtrise des décisions. Ils jouent contre une dette supplémentaire immédiate : endettement déjà élevé depuis le rachat de MÉRANDOL, tarifs orientés à la baisse, projet dont la rentabilité dépend de contrats non signés.
- **Recommandation** : retenir la **solution A aménagée**, qui respecte l'ordre du financement hiérarchique et la clause :
  - réduire la hausse de la dette financière nette de 2028 d'au moins 330 k€, et en pratique davantage pour garder une marge de sécurité : distribution aux associés réduite d'environ 0,4 à 0,5 M€ en 2028, ou paiement d'une partie de la chaîne et constitution du BFR décalés au début de 2029, ou réalisation par tranches ;
  - demander à la Banque VELMONDE, prêteur des deux emprunts, d'apprécier la clause de 2028 en tenant compte de l'EBE attendu de la chaîne, ou de l'aménager pour un an, contrat de prêt d'équipement à l'appui ;
  - ne signer le prêt et la commande qu'avec des engagements de cliniques (question 3.2), pour que le service de la dette soit couvert ;
  - garder l'entrée de TILVANE Santé Partenaires en dernier recours, si la banque refusait tout aménagement : elle coûte cher, limite l'autonomie des associés, divise le groupe et prépare une cession de la participation dans six ans.

**Réponses tolérées** : recommandation de la solution B si elle est fondée sur le respect de la clause et accompagnée des coûts du capital apporté ; recommandation d'un financement mixte (prêt réduit et apport partiel) ; analyse de la clause par le rapport plutôt que par la marge, si le raisonnement est juste.

**Erreurs fréquentes**
- Ne compter que le prêt dans la hausse de la dette financière nette (2 000 k€, marge restante de 1 000 k€) : l'autofinancement consacré au projet ne réduit plus la dette.
- Oublier le BFR dans le montant à financer (3 150 k€).
- Attribuer le financement hiérarchique à Modigliani et Miller, ou inverser l'ordre (actions avant dette) : `JUR-T14`.
- Confondre théorie du compromis (ratio cible) et financement hiérarchique (pas de cible).
- Développer les règles de détention du capital d'une société d'exercice libéral : hors sujet (UE 1).
- `JUR-T13` — théories récitées sans les montants du cas.

**Références** : F10 (Myers et Majluf, 1984 ; Myers, 1977, attribution retenue par le programme) [V programme 7.2.d] ; F06 § 1 (choix des sources selon la taille et l'accès au marché) [S].

---

### 3.4 Fonds obligataire et actions, allocations, variance minimale (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Rentabilités moyennes : obligataire **3,00 %**, actions **9,00 %** ; écarts-types (n − 1) : **6,00 %** et **18,00 %** ; covariance = 0,00 × 6 × 18 = **0** | 0,75 |
| 3.4-02 | Allocation prudente (30 % actions) : **4,80 %**, variance 46,80 %², écart-type **6,84 %** ; gestion pilotée à plus de 15 ans (80 % actions) : **7,80 %**, variance 208,80 %², écart-type **14,45 %** | 0,75 |
| 3.4-03 | Variance minimale : obligataire 324 / 360 = **90 %**, actions **10 %** ; rentabilité **3,60 %** ; écart-type **5,69 %** | 0,5 |
| 3.4-04 | Markowitz (1952) : le risque d'un portefeuille dépend de la corrélation ; ici, avec une corrélation nulle, 10 % d'actions réduisent le risque et augmentent la rentabilité : le fonds obligataire seul est dominé ; l'écart-type de l'allocation prudente (6,84 %) est très inférieur à la moyenne pondérée des écarts-types (9,60 %) ; corrélation estimée sur cinq ans, instable | 0,5 |
| 3.4-05 | M. LAVERGNAS (31 ans, horizon d'une vingtaine d'années) : allocation de la gestion pilotée à 80 % d'actions ; ni le monétaire, ni le portefeuille de variance minimale, ni une allocation unique pour tous ne tiennent compte de son horizon | 0,5 |

**Rentabilités et risques des deux fonds (0,75 pt).**

| % | 2022 | 2023 | 2024 | 2025 | 2026 | Moyenne | Somme des carrés des écarts | Variance (n − 1) | Écart-type |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Obligations Euro (O) | − 4 | 8 | 6 | − 3 | 8 | **3,00** | 144 | 36,00 %² | **6,00** |
| Actions Europe (A) | − 10 | 14 | 24 | 27 | − 10 | **9,00** | 1 296 | 324,00 %² | **18,00** |

Covariance des deux fonds = coefficient de corrélation fourni × σ(O) × σ(A) = 0,00 × 6 × 18 = **0**. Les rentabilités des deux fonds varient indépendamment l'une de l'autre sur la période : les actions ont perdu 10 % en 2022 et en 2026, quand les obligations ont perdu 4 % en 2022 et gagné 8 % en 2026.

**Deux allocations (0,75 pt).**
- Allocation prudente suggérée par la commission (30 % A, 70 % O) : rentabilité = 0,7 × 3 + 0,3 × 9 = **4,80 %** ; variance = 0,7² × 36 + 0,3² × 324 + 0 = 17,64 + 29,16 = 46,80 %² ; écart-type = **6,84 %**.
- Gestion pilotée pour un horizon de plus de 15 ans (80 % A, 20 % O) : rentabilité = 0,2 × 3 + 0,8 × 9 = **7,80 %** ; variance = 0,2² × 36 + 0,8² × 324 = 1,44 + 207,36 = 208,80 %² ; écart-type = **14,45 %**.

**Portefeuille de variance minimale (0,5 pt).** Poids du fonds obligataire = (σ_A² − cov) / (σ_O² + σ_A² − 2 cov) = (324 − 0) / (36 + 324 − 0) = **90 %** ; actions **10 %**. Rentabilité = 0,9 × 3 + 0,1 × 9 = **3,60 %** ; variance = 0,81 × 36 + 0,01 × 324 = 29,16 + 3,24 = 32,40 %² ; écart-type = **5,69 %**.

**Rôle de la corrélation (0,5 pt).** Selon Markowitz (1952), le risque d'un portefeuille ne dépend pas seulement du risque de chaque titre, mais de la **covariance** entre leurs rentabilités. Tant que la corrélation est inférieure à 1, l'écart-type d'un portefeuille est inférieur à la moyenne pondérée des écarts-types : pour l'allocation prudente, 6,84 % au lieu de 0,7 × 6 + 0,3 × 18 = 9,60 % si la corrélation était de 1. Avec une corrélation nulle, ajouter 10 % d'actions, pourtant trois fois plus risquées, **réduit** le risque du fonds obligataire seul (5,69 % au lieu de 6,00 %) tout en augmentant la rentabilité (3,60 % au lieu de 3,00 %) : placer toute son épargne en obligations est un choix dominé. La corrélation de 0,00 est toutefois estimée sur cinq rentabilités annuelles : elle peut changer, et les deux classes d'actifs ont déjà baissé ensemble (2022).

**Allocation qui convient à M. LAVERGNAS (0,5 pt).**
- Il a 31 ans et n'envisage pas d'utiliser son épargne avant une vingtaine d'années : il peut supporter des baisses annuelles et attendre que les cours se redressent. L'allocation de la gestion pilotée pour un horizon de plus de 15 ans (80 % actions) lui offre la rentabilité espérée la plus élevée (7,80 %) ; ses plus mauvaises années de la période auraient été − 8,80 % en 2022 et − 6,40 % en 2026 (calcul non exigé).
- Son épargne est aujourd'hui entièrement dans le fonds monétaire (rentabilité moyenne de 2,20 % sur 2022-2026, non exigée), par défaut et non par choix. Sur vingt ans, 9 600 € deviendraient environ 14 835 € au rythme du monétaire, 24 519 € au rythme de l'allocation prudente et 43 117 € à celui de l'allocation pilotée, si les rentabilités passées se répétaient chaque année, ce qui n'est pas garanti (illustration non exigée).
- Le portefeuille de variance minimale convient à un épargnant qui cherche d'abord à limiter les fluctuations, par exemple à quelques années de l'utilisation de son épargne ; l'allocation prudente unique ignore l'horizon de chacun. Le choix final dépend aussi de la tolérance de M. LAVERGNAS aux baisses : s'il risquait de tout vendre après une mauvaise année (question 3.7), une part d'actions plus faible (60 %) serait préférable.

**Réponses tolérées** : allocation par défaut de dix ans (40 % d'actions, 60 % d'obligations : rentabilité 5,40 %, variance 64,80 %², écart-type 8,05 %) si le candidat l'a justifiée par l'absence de choix de M. LAVERGNAS ; l'item 3.4-05 reste noté sur l'horizon d'une vingtaine d'années ; variances exprimées en fraction (0,0036 ; 0,0324) ; écart-type de 14,4 % ou 14,5 % ; recommandation d'une allocation à 60 % d'actions si elle est justifiée par la tolérance au risque du salarié.

**Erreurs fréquentes**
- Calculer les écarts-types sur n (5,37 % et 16,10 %) alors que l'énoncé impose n − 1.
- Calculer l'écart-type du portefeuille comme moyenne pondérée des écarts-types (9,60 % pour l'allocation prudente).
- Inverser les poids dans la formule de variance minimale (10 % d'obligations).
- Recommander le portefeuille de variance minimale à tous les salariés, sans tenir compte de l'horizon.
- Calculer des ratios de Sharpe ou de Treynor, non demandés.

**Références** : F10 (Markowitz, 1952) [V programme 5.3.b] ; F01 § 1 (variance sur n − 1) [V corrigé 2023] ; coefficient de corrélation fourni par l'énoncé [V programme 5.3.c, `fourni_dans_sujet`].

---

### 3.5 Diversification d'un portefeuille d'actions, risque spécifique et risque systématique (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Variances et écarts-types pour 1, 5, 10, 20 et 50 actions : 0,102400 (**32,00 %**) ; 0,040960 (**20,24 %**) ; 0,033280 (**18,24 %**) ; 0,029440 (**17,16 %**) ; 0,027136 (**16,47 %**) | 0,75 |
| 3.5-02 | Part du risque spécifique : **75,00 %**, **37,50 %**, **23,08 %**, **13,04 %**, **5,66 %** ; plancher = covariance moyenne 0,0256, écart-type **16,00 %** | 0,5 |
| 3.5-03 | Interprétation : risque spécifique diversifiable et non rémunéré, risque systématique non diversifiable et seul rémunéré ; pour un salarié : préférer un fonds diversifié à quelques lignes, ne pas concentrer son épargne sur ce dont dépend déjà son emploi | 0,75 |

**Calcul (1,25 pt).** Variance (N) = 0,1024 / N + (1 − 1 / N) × 0,0256 ; risque spécifique = (0,1024 − 0,0256) / N = 0,0768 / N.

| Nombre d'actions N | Variance | Écart-type | Risque spécifique | Part du risque spécifique dans la variance |
|---:|---:|---:|---:|---:|
| 1 | 0,102400 | **32,00 %** | 0,076800 | **75,00 %** |
| 5 | 0,040960 | **20,24 %** | 0,015360 | **37,50 %** |
| 10 | 0,033280 | **18,24 %** | 0,007680 | **23,08 %** |
| 20 | 0,029440 | **17,16 %** | 0,003840 | **13,04 %** |
| 50 | 0,027136 | **16,47 %** | 0,001536 | **5,66 %** |
| N très grand | 0,025600 | **16,00 %** | 0 | 0 % |

Quand N augmente, le premier terme tend vers zéro : la variance tend vers la **covariance moyenne** (0,0256), soit un écart-type plancher de **16,00 %**, égal à celui de l'indice des actions européennes. De 1 à 50 lignes, l'écart-type baisse de 48,52 % ; l'essentiel du gain est acquis avec 10 à 20 lignes (non exigé).

**Interprétation (0,75 pt).**
- Le **risque spécifique** tient à chaque société (résultats, dirigeants, litiges, perte d'un client) : les chocs propres à des sociétés différentes se compensent en partie, et ce risque disparaît presque dans un portefeuille diversifié. Le **risque systématique** tient à ce qui touche toutes les sociétés en même temps (conjoncture, taux d'intérêt, inflation, crise) : il est mesuré par la covariance moyenne et ne peut pas être éliminé par la diversification.
- Le lien entre les deux : le risque total d'une action seule est fait aux trois quarts de risque spécifique ; la diversification ne laisse que le risque systématique. Comme un investisseur peut éliminer le risque spécifique sans coût, le marché ne le rémunère pas : seul le risque systématique donne droit à une prime (MEDAF, question 3.6).
- Pour un salarié : acheter deux ou trois actions qu'il « connaît » lui fait supporter un risque (écart-type d'environ 23 % à 25 % : 25,30 % pour deux actions, 22,63 % pour trois) que rien ne rémunère. Le fonds QUIRANDE Actions Europe, avec une soixantaine de lignes, est proche du plancher : son risque est presque entièrement systématique (bêta de 1,10, question 3.6). Le salarié doit aussi tenir compte de son emploi : son salaire dépend déjà de CLAVÉRINE et de la biologie médicale. Le plan, qui n'investit pas en titres du groupe, évite de concentrer sur la même entreprise son revenu et son épargne.

**Réponses tolérées** : écarts-types arrondis à 0,1 point ; plancher exprimé par la corrélation moyenne de 0,25 ; part du risque spécifique exprimée en écart-type, si elle est clairement définie.

**Erreurs fréquentes**
- Faire tendre le risque vers zéro avec N : la diversification ne supprime pas le risque de marché.
- Diviser la variance moyenne par N sans ajouter le terme de covariance.
- Confondre risque spécifique (propre à la société) et risque systématique (commun au marché), ou dire que le risque spécifique est rémunéré.

**Références** : F10 (Markowitz, 1952 : le risque spécifique se diversifie, le risque systématique non) [V programme 5.3.a et 5.3.b] ; formule de l'équipondération fournie par l'annexe 3.5.

---

### 3.6 Bêta, MEDAF et rentabilité espérée d'une part (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Covariance avec l'indice = 1 129 / 4 = **282,25 %²** ; variance de l'indice = 1 024 / 4 = **256,00 %²** ; bêta = 1,1025, arrondi à **1,10** | 0,5 |
| 3.6-02 | MEDAF : 4,0 % + 1,10 × 5,0 % = **9,50 %** ; rentabilité espérée d'une part : (135,50 − 125,00) / 125,00 = **8,40 %** | 0,5 |
| 3.6-03 | Interprétation : rentabilité espérée inférieure de 1,10 point à la rentabilité exigée ; l'écart correspond à peu près aux frais de gestion (9,60 % avant frais) ; le fonds offre une exposition au risque de marché à son juste prix, diminuée de ses frais ; valeur de la part au taux exigé 123,74 € (non exigée) | 0,5 |
| 3.6-04 | Limites du MEDAF : bêta estimé sur cinq années, instable ; facteur unique (Fama et French) ; taux sans risque et prime posés par hypothèse ; prévision de la société de gestion incertaine ; marchés efficients et investisseurs diversifiés supposés | 0,5 |

**Bêta (0,5 pt).** Écarts à la moyenne : fonds A (− 19 ; 5 ; 15 ; 18 ; − 19), indice M (− 17 ; 6 ; 17 ; 11 ; − 17).
Covariance = (323 + 30 + 255 + 198 + 323) / 4 = 1 129 / 4 = **282,25 %²** ; variance de l'indice = (289 + 36 + 289 + 121 + 289) / 4 = 1 024 / 4 = **256,00 %²** (écart-type 16,00 %).
Bêta = 282,25 / 256 = 1,1025, arrondi à **1,10** : le fonds amplifie d'environ 10 % les variations du marché (corrélation de 0,98 avec l'indice, non exigée).

**MEDAF et rentabilité espérée (0,5 pt).**
- Rentabilité exigée = 4,0 % + 1,10 × 5,0 % = **9,50 %**.
- Rentabilité espérée d'une part sur un an, le fonds ne distribuant rien : (135,50 − 125,00) / 125,00 = **8,40 %**.

**Interprétation (0,5 pt).**
- D'après la prévision de QUIRANDE Gestion, la part rapporterait 1,10 point de moins que ce que son risque systématique justifie selon le MEDAF. Au taux exigé, la part vaudrait aujourd'hui 135,50 / 1,095 = 123,74 €, un peu moins que sa valeur de 125,00 € (non exigé).
- L'écart s'explique presque entièrement par les **frais de gestion** : avant les frais de 1,20 %, la rentabilité espérée serait de 9,60 %, proche des 9,50 % exigés. Le fonds n'est donc ni une bonne affaire ni un mauvais placement : il procure au salarié l'exposition au risque du marché européen, diversifiée, au prix de ses frais. Sur la période 2022-2026, sa rentabilité moyenne (9,00 %) est elle aussi inférieure à la rentabilité exigée.
- Pour le salarié, la prime de risque rémunère le seul risque systématique (question 3.5) ; sur un horizon de vingt ans, les frais pèsent lourd : 1,20 % par an, contre 0,70 % pour le fonds obligataire.

**Limites du MEDAF (0,5 pt).**
- Le bêta est estimé sur cinq rentabilités annuelles : il est fragile et peut changer d'une période à l'autre.
- Le MEDAF retient un seul facteur de risque, le marché ; le modèle à trois facteurs de Fama et French (1993) ajoute la taille et la valeur, et donnerait une autre rentabilité exigée à un fonds de grandes sociétés.
- Le taux sans risque et la prime de risque sont des hypothèses : une prime de 4 % ou de 6 % changerait la conclusion.
- La prévision de la société de gestion est une estimation, peut-être optimiste, et non une rentabilité certaine.
- Le modèle suppose des marchés efficients et des investisseurs rationnels et diversifiés : les propos des salariés (question 3.7) montrent que ces hypothèses ne décrivent pas toujours les épargnants.

**Réponses tolérées** : bêta non arrondi (1,1025) et rentabilité exigée de 9,51 % ; covariance exprimée en fraction (0,028225) ; interprétation en termes de sur-évaluation de la part si elle est nuancée par les frais et les limites.

**Erreurs fréquentes**
- Calculer le bêta comme rapport des écarts-types (18 / 16 = 1,125) : le bêta est la covariance rapportée à la variance de l'indice.
- Ajouter la prime au taux sans risque sans la multiplier par le bêta (9,00 %).
- Comparer la rentabilité espérée à la rentabilité historique de l'indice (8,00 %) au lieu de la rentabilité exigée.
- Conclure que le fonds est « mauvais » sans voir le rôle des frais.

**Références** : F02 § 2 (MEDAF et ses limites ; Fama et French, § 7) [V programme 5.2.c] ; F10 (Sharpe, 1964) ; F11 § 1 et § 2 (taux sans risque de 4 % et prime de 5 %, valeurs repères) [V] ; programme 5.2.b (rentabilité espérée sur une période) [V].

---

### 3.7 Biais des salariés épargnants et affectation par défaut à la gestion pilotée (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Biais rattachés aux propos : aversion aux pertes et point de référence (propos 1, ventes après la baisse, retour « quand elles auront retrouvé leur niveau ») ; statu quo, inertie et report du choix (propos 2, 58 % de salariés sans choix) ; excès de confiance et attribution de la réussite à son talent (propos 3) ; extrapolation des bonnes années et oubli de l'horizon (propos 4, besoin dans deux ans) ; nuance de la rationalité supposée (Kahneman et Tversky, 1973 ; simplexité, Berthoz, 2009) | 1 |
| 3.7-02 | Ce que l'affectation par défaut corrige : l'inertie travaille pour le salarié (allocation liée à un horizon au lieu du monétaire), rééquilibrage annuel automatique sans recherche du « bon moment », baisse progressive des actions à l'approche de l'horizon, aucun frais supplémentaire | 0,5 |
| 3.7-03 | Limites : horizon de dix ans retenu par défaut inadapté à beaucoup de salariés (M. LAVERGNAS, secrétaire de 61 ans), sortie possible après une baisse, grille identique pour tous, frais plus élevés des fonds actions, information et conseil toujours nécessaires, responsabilité du groupe dans le choix proposé | 0,5 |

**Biais des salariés (1 pt).** La finance comportementale part des écarts entre la décision rationnelle supposée par la théorie standard et les heuristiques qu'utilisent réellement les épargnants (Kahneman et Tversky, 1973) ; confrontés à un choix complexe, ils recourent à des règles simples (simplexité, Berthoz, 2009).
- **Propos 1 (technicienne)** : **aversion aux pertes**, la baisse de 10 % de 2026 pèse plus qu'un gain équivalent ; **disponibilité** de la dernière année ; **point de référence** fixé au niveau de fin 2025. Elle vend après la baisse et ne rachètera qu'après la hausse : elle rend la perte définitive et risque de manquer le redressement. Juger une épargne de long terme sur une seule année la rend plus sensible aux baisses qu'elle ne devrait l'être.
- **Propos 2 (coursier)** : **biais de statu quo** et **inertie** : le choix est jugé complexe et reporté (« je remets toujours à plus tard ») ; c'est alors l'affectation par défaut qui décide. Le comportement est général : 58 % des salariés n'ont jamais choisi et 64 % des sommes du plan sont dans le fonds monétaire, dont la rentabilité moyenne (2,20 %) est faible pour des horizons longs.
- **Propos 3 (technicien)** : **excès de confiance** et **attribution de la réussite à son propre talent** : un épisode réussi est pris pour une compétence, alors qu'il peut tenir au hasard ; il croit pouvoir anticiper le marché, ce que l'hypothèse d'efficience rend peu probable de façon durable. Sortir et revenir fait courir le risque de manquer les meilleures séances.
- **Propos 4 (secrétaire médicale)** : **représentativité** et **extrapolation** des bonnes années (24 % et 27 % en 2024 et 2025), en oubliant 2022 et 2026 (− 10 %) ; **excès de confiance** (« finissent toujours par remonter »), vrai en moyenne sur de longues périodes, mais pas sur deux ans : une baisse juste avant le retrait ne pourrait pas être rattrapée. Son allocation, entièrement en actions, ne correspond pas à son horizon.

**Ce que l'affectation par défaut à la gestion pilotée peut corriger (0,5 pt).**
- Elle **utilise l'inertie** au lieu de la subir : le salarié qui ne choisit pas reçoit une allocation liée à un horizon (40 % d'actions, 60 % d'obligations pour dix ans) au lieu du fonds monétaire. Il garde sa liberté : il est informé et peut tout modifier.
- Le **rééquilibrage annuel automatique** supprime la recherche du « bon moment » et les arbitrages émotionnels après une baisse (propos 1 et 3) : il conduit même à racheter des actions quand elles ont baissé.
- La **baisse progressive de la part des actions** à l'approche de l'horizon répond au propos 4 : à deux ans ou moins, 80 % de monétaire et 20 % d'obligations, sans actions.
- La gestion pilotée n'entraîne pas de frais supplémentaires ; elle applique une grille de répartition fixée à l'avance, et non une gestion par algorithme.

**Limites (0,5 pt).**
- L'**horizon de dix ans retenu par défaut** ne convient pas à tous : M. LAVERGNAS, à vingt ans de l'utilisation de son épargne, aurait 40 % d'actions au lieu des 80 % de la grille ; un salarié qui a besoin de ses fonds dans deux ans en aurait trop. L'affectation par défaut n'est utile que si les salariés indiquent ensuite leur horizon réel.
- Elle ne supprime pas les biais : un salarié peut sortir de la gestion pilotée après une baisse ; la grille est la même pour tous, quelle que soit la tolérance de chacun aux pertes ou son autre patrimoine.
- Les fonds actions ont les frais les plus élevés (1,20 % contre 0,30 % pour le monétaire) : le teneur de compte a intérêt à une plus grande part d'actions, ce qui appelle une information claire sur les frais.
- En proposant un choix par défaut, le groupe et la commission du comité social et économique engagent leur responsabilité vis-à-vis des salariés : une information compréhensible et des réunions de conseil restent nécessaires. L'allocation « prudente » unique suggérée par la commission (30 % d'actions) a le défaut inverse : elle ignore l'horizon de chacun.

**Réponses tolérées** : biais de « procrastination » ou « surcharge de choix » pour le propos 2 ; « illusion de contrôle » pour le propos 3 ; « comptabilité mentale » pour le propos 1, si l'explication est liée au cas ; vocabulaire « allocation par défaut » ou « choix par défaut ».

**Erreurs fréquentes**
- Réciter une liste de biais sans les rattacher aux propos : `JUR-T13`.
- Chiffrer l'aversion aux pertes (coefficient) : approfondissement hors programme.
- Attribuer les biais à Fama, ou se tromper sur les distinctions reçues par les auteurs (F99, F10).
- Présenter la gestion pilotée comme une gestion par algorithme ou par intelligence artificielle.
- Développer les règles juridiques de l'épargne salariale ou son imposition : hors programme (UE 1).

**Références** : F06 § 4 (finance comportementale, biais à rattacher au cas, simplexité) [V programme 5.1.d ; guide p. 74] ; F10 (Kahneman et Tversky, 1973 ; Berthoz, 2009) [V programme 5.1].

---

**Points d'attention pour le correcteur**
- Aux questions 3.1 et 3.2, la valeur de revente et le BFR peuvent être présentés sur une ligne distincte ; seule la cohérence avec l'annexe 3.7 est exigée.
- À la question 3.3, la conclusion dépend de la lecture de la marge de la clause : un candidat qui ne compte que le prêt (+ 2 000) se trompe sur l'effet de la solution A ; la suite de son raisonnement est notée en cohérence, mais l'item 3.3-02 n'est pas acquis.
- Aux questions 3.4 et 3.6, les variances peuvent être exprimées en %² ou en fraction ; le coefficient de corrélation est fourni et n'a pas à être recalculé.
