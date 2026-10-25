# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 6 — Dossier 3 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F05 ingénierie financière, F06 marchés et finance comportementale, F10 auteurs et théories, F11 données de marché (toutes à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (BPA, structure financière, Gordon-Shapiro, portefeuille, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Politique de dividende et théories | `4.1.a` Déchiffrer la politique de dividende et les signaux associés | 3 |
| 3.2 Dividende exceptionnel ou rachat d'actions | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital ; `4.1.a` | 3 |
| 3.3 Valeur de l'action par Gordon-Shapiro | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique d'un titre | 2 |
| 3.4 Réaction du cours à l'avertissement sur résultats | `5.1.c` Efficience informationnelle (Fama, 1970) ; `5.1.d` Finance comportementale | 3 |
| 3.5 Portefeuille de la holding familiale | `5.3.a` Risque spécifique et risque systématique ; `5.3.b` Diversification (Markowitz, 1952) ; `5.3.c` Rentabilité et risque d'un portefeuille | 4 |
| **Total** | | **15** |

Part du calcul : environ 7 points (3.1-01, 3.2-01 et 3.2-02, 3.3-01 et 3.3-02, 3.5-01 à 3.5-03). Part de l'analyse : environ 8 points. Ce dossier, placé en fin d'épreuve, vaut autant qu'un dossier calculatoire : il ne doit pas être bâclé faute de temps (`JUR-T15`).

---

### 3.1 Politique de dividende et théories (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Taux de distribution : 33,3 % de 2022 à 2025, 44,4 % en 2026 ; rendements : 2,50 % ; 2,33 % ; 2,20 % ; 2,43 % ; 2,86 % | 1 |
| 3.1-02 | Caractérisation : taux de distribution cible d'un tiers et dividende croissant jusqu'en 2025 ; en 2026, maintien à 1,20 € au lieu de 0,90 € : effet cliquet | 0,5 |
| 3.1-03 | Neutralité (Modigliani et Miller, 1961) appliquée au cas | 0,5 |
| 3.1-04 | Théorie du signal (Spence, 1973 ; Ross, 1977) appliquée à la proposition | 0,5 |
| 3.1-05 | Frictions (fiscalité, coûts d'agence, coûts de transaction) et conclusion | 0,5 |

**Calculs (1 pt).** Taux de distribution = dividende par action / BPA ; rendement = dividende par action au titre de l'exercice / cours au 31 décembre.

| Exercice | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|
| BPA (€) | 3,00 | 3,15 | 3,30 | 3,60 | 2,70 |
| Dividende par action (€) | 1,00 | 1,05 | 1,10 | 1,20 | 1,20 (proposé) |
| **Taux de distribution** | **33,3 %** | **33,3 %** | **33,3 %** | **33,3 %** | **44,4 %** |
| Cours au 31/12 (€) | 40,00 | 45,00 | 50,00 | 49,40 | 42,00 |
| **Rendement de l'action** | **2,50 %** | **2,33 %** | **2,20 %** | **2,43 %** | **2,86 %** |

**Caractérisation (0,5 pt).**
- De 2022 à 2025, TERRALBE distribue exactement un tiers de son résultat : le dividende suit le BPA et progresse chaque année (+ 20 % en trois ans). C'est une politique de taux de distribution cible, rassurante pour les actionnaires.
- En 2026, le BPA baisse de 25 % (3,60 € → 2,70 €). Appliquer le taux habituel donnerait 2,70 / 3 = **0,90 €**, soit un dividende en baisse de 25 %. Le conseil propose au contraire de **maintenir 1,20 €**, ce qui porte le taux de distribution à 44,4 % : c'est l'**effet cliquet**. Une entreprise hésite à baisser un dividende, car le marché interprète une baisse comme une mauvaise nouvelle durable (lissage décrit par Lintner, 1956).
- La hausse du rendement (2,86 % contre 2,43 %) ne vient pas d'un dividende plus élevé mais de la baisse du cours (− 15 %).

**Neutralité (0,5 pt).** Selon Modigliani et Miller (1961), en marché parfait (sans impôt ni coûts de transaction, information partagée, politique d'investissement donnée), la politique de dividende n'affecte pas la valeur : ce que l'actionnaire reçoit en dividende, il le perd en valeur de l'action (le cours baisse du dividende lors du détachement). En l'espèce, maintenir 1,20 € plutôt que 0,90 € ne crée pas de valeur : les 3 M€ supplémentaires (0,30 € × 10 000 000) sortent de la trésorerie du groupe. Un actionnaire qui a besoin de liquidités peut se fabriquer un « dividende maison » en cédant des titres : LESTRADEC Participations pourrait couvrir son besoin de 5,5 M€ en vendant une partie de ses parts du fonds indiciel (97,2 M€, annexe 3.4).

**Signal (0,5 pt).** La politique de dividende n'est pas neutre en pratique, parce que les dirigeants en savent plus que le marché sur les perspectives de l'entreprise.
- Au sens de Spence (1973), un signal est crédible s'il est coûteux à imiter : maintenir le dividende malgré un résultat en baisse de 25 % signale que la direction juge la baisse temporaire (récolte exceptionnellement mauvaise) et croit au redressement, puisqu'elle s'engage à verser 12,0 M€ sur un résultat de 27,0 M€.
- Ross (1977) a construit la théorie du signal sur la structure financière : un dirigeant qui accroît l'endettement signale sa confiance dans les flux futurs, car il supporte le risque de défaillance. Appliquée au dividende, la logique est la même : un dividende maintenu au prix d'une trésorerie moindre, donc d'une dette nette plus élevée, engage la direction de la même façon.
- Le signal a déjà été envoyé : le communiqué du 14 octobre 2026 (annexe 3.3) a confirmé un dividende « au moins égal » à celui de l'exercice précédent. Revenir à 0,90 € décevrait un engagement public et serait lu comme un aveu de difficultés durables.

**Frictions et conclusion (0,5 pt).**
- **Fiscalité** : l'imposition du dividende chez l'actionnaire peut être plus lourde que celle d'une plus-value réalisée plus tard ; certains actionnaires préfèrent donc un dividende faible (effet de clientèle). Aucun calcul n'est attendu.
- **Coûts d'agence** (Jensen et Meckling, 1976) : distribuer réduit la trésorerie laissée à la discrétion des dirigeants. Chez TERRALBE, l'enjeu porte aussi sur la relation entre l'actionnaire de contrôle et les minoritaires : avec 0,90 €, LESTRADEC Participations recevrait 5 400 000 × 0,90 = 4,86 M€, moins que ses besoins (5,5 M€), contre 6,48 M€ avec 1,20 €. Le conseil, présidé par Mme LESTRADEC, doit montrer que le maintien sert tous les actionnaires et pas seulement la holding.
- **Coûts de transaction** : céder des titres pour se créer un dividende a un coût ; les petits porteurs préfèrent un revenu régulier.
- **Conclusion** : le maintien à 1,20 € est défendable comme signal de confiance et pour la stabilité attendue par les actionnaires, à condition que le redressement soit crédible : un taux de distribution de 44 % durablement supérieur au taux cible réduirait l'autofinancement du plan « Horizon 2030 ». La revue de la politique de distribution annoncée par le plan devrait fixer une règle claire (dividende ordinaire stable, retour de l'excédent par des opérations exceptionnelles).

**Réponses tolérées** : taux de distribution calculés en masse (dividendes / résultat net part du groupe, mêmes résultats) ; taux de distribution donnés à deux décimales (un tiers, 44,44 %) ; rendement calculé sur un autre cours si le candidat le précise ; référence à Lintner (1956) facultative ; signal présenté seulement par Spence si le raisonnement est juste.

**Erreurs fréquentes**
- `JUR-I04` — ne pas opposer le revenu immédiat de l'actionnaire et le renforcement des fonds propres du groupe.
- `JUR-T14` et `JUR-M01` — citer « Ross » pour un signal par le dividende sans préciser qu'il s'agit à l'origine d'un signal par l'endettement ; confondre neutralité et absence d'intérêt du dividende.
- Conclure que la hausse du rendement en 2026 traduit une politique plus généreuse, alors qu'elle vient de la baisse du cours.
- `JUR-T13` — exposé des théories sans lien avec TERRALBE (taux de 44,4 %, besoins de la holding, communiqué d'octobre).

---

### 3.2 Dividende exceptionnel ou rachat d'actions (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | BPA pro forma : 2,70 € avant ; option A : 2,63 € ; option B : 909 090 actions rachetées, 9 090 910 actions, 2,89 € | 1 |
| 3.2-02 | Effets : capitaux propres 320 → 280 M€ dans les deux options ; dette financière nette 150 → 190 M€ et ratio du crédit syndiqué 2,23 → 2,83 ; LESTRADEC Participations 54 % → 59,40 % (option B), inchangé avec l'option A | 1 |
| 3.2-03 | Signal de chaque option et recommandation argumentée | 1 |

**Conventions rappelées** (annexe 3.2) : opération supposée réalisée le 1er janvier 2026 pour le BPA ; produits financiers perdus sur 40 M€ à 2,4 %, après IS à 25 % ; actions rachetées arrondies à l'unité inférieure ; effets sur la structure au 31/12/2026, hors dividende ordinaire.

**BPA pro forma (1 pt).**
- Produits financiers perdus, nets d'impôt : 40 M€ × 2,4 % × (1 − 25 %) = **0,72 M€** ; résultat pro forma : 27,0 − 0,72 = **26,28 M€**.
- **Option A** (dividende exceptionnel de 40 / 10 = 4,00 € par action) : le nombre d'actions ne change pas. BPA = 26,28 / 10 = **2,63 €** (− 2,7 %).
- **Option B** (rachat à 44 €) : 40 000 000 / 44 = 909 090,9, soit **909 090 actions** rachetées (9,09 % du capital) pour 39 999 960 €. Actions restantes : 10 000 000 − 909 090 = **9 090 910**. BPA = 26 280 000 / 9 090 910 = **2,89 €** (+ 7,1 %).
- Le rachat est relutif parce que le rendement bénéficiaire de l'action au prix de rachat (BPA / prix = 2,70 / 44 = 6,14 %) dépasse le coût après impôt de la trésorerie utilisée (2,4 % × 0,75 = 1,80 %).

**Effets sur la structure et le contrôle (1 pt).**

| | Avant | Option A | Option B |
|---|---:|---:|---:|
| Capitaux propres consolidés (M€) | 320,0 | 280,0 | 280,0 |
| Trésorerie (M€) | 50,0 | 10,0 | 10,0 |
| Dette financière nette hors obligations locatives (M€) | 150,0 | 190,0 | 190,0 |
| Ratio du crédit syndiqué (DFN / 67,2) | 2,23 | 2,83 | 2,83 |
| Ratio d'endettement net (DFN / capitaux propres), facultatif | 46,88 % | 67,86 % | 67,86 % |
| Part du capital de LESTRADEC Participations | 54 % | 54 % | 59,40 % |

- Les deux options réduisent les capitaux propres de 40 M€ (dividende prélevé sur les réserves, ou annulation des actions rachetées) et augmentent d'autant la dette financière nette, puisque la trésorerie diminue.
- **Ratio du crédit syndiqué** : 190 / 67,2 = **2,83**, sous le plafond de 3,0, mais la marge devient étroite. Le ratio atteindrait 3,0 si l'EBITDA hors effet de la norme tombait à 190 / 3 = 63,3 M€, soit une baisse de 5,75 % seulement (contre une baisse admissible de 25,6 % avant l'opération : 150 / 3 = 50 M€). Après une année de marges en recul, ce risque n'est pas théorique.
- **Contrôle** : avec l'option B, LESTRADEC Participations conserve 5 400 000 actions sur 9 090 910, soit **59,40 %**, sans rien débourser ; le flottant diminue (le public passerait de 43 % à 37,30 % si toutes les actions rachetées venaient de lui, calcul facultatif). Avec l'option A, sa part reste de 54 % et elle reçoit 5 400 000 × 4,00 = **21,6 M€**.

**Signal et recommandation (1 pt).**
- **Le BPA n'est pas la valeur.** La hausse du BPA de l'option B est mécanique : selon Modigliani et Miller, en marché parfait, la richesse des actionnaires est la même dans les deux options et la même qu'avant. Le BPA augmente, mais l'endettement aussi : le risque par action augmente et le PER devrait baisser. Le rachat ne crée de valeur pour les actionnaires restants que si l'action est achetée sous sa valeur : il transfère alors de la valeur des vendeurs vers ceux qui restent. Si la valeur est de 42 €, payer 44 € transfère de la valeur aux vendeurs (cours théorique après rachat : (420 − 40) / 9,09 M ≈ 41,80 €) ; si elle est de 48 € (question 3.3), les actionnaires restants y gagnent (cours théorique ≈ 48,40 €).
- **Signal de l'option A** : un dividende qualifié d'exceptionnel n'engage pas l'avenir, ce qui évite l'effet cliquet. Il peut toutefois être lu comme l'aveu d'un manque de projets rentables, au moment où le groupe annonce une usine. Il traite tous les actionnaires à égalité et procure à la holding 21,6 M€, qu'elle peut diversifier (question 3.5).
- **Signal de l'option B** : racheter ses actions à 44 € signale que la direction juge le cours de 42 € trop bas, au lendemain d'une baisse jugée excessive (annexe 3.3). Le signal est crédible parce que coûteux : il mobilise la trésorerie et accroît l'endettement (Ross, 1977). Le rachat est aussi plus souple qu'un dividende : il peut être étalé ou interrompu.
- **Points de vigilance** : le rachat renforce le contrôle de la famille sans contrepartie et réduit la liquidité du titre, ce que les minoritaires peuvent contester ; les deux options rapprochent le groupe du plafond du crédit syndiqué au moment où il doit financer le plan « Horizon 2030 ».
- **Recommandation type** : préférer le rachat d'actions, pour le signal et la souplesse, mais l'exécuter progressivement et pour un montant compatible avec une marge de sécurité sur le ratio du crédit syndiqué (par exemple une première tranche de 20 M€, à compléter si l'EBITDA de 2027 se redresse). Une recommandation de dividende exceptionnel est acceptée si elle est argumentée : égalité de traitement, absence de renforcement du contrôle, liquidités permettant à la holding de diversifier son patrimoine.

**Réponses tolérées** : nombre d'actions arrondi à 909 091 (BPA 2,89 €, part de LESTRADEC 59,40 %) ; BPA calculé sans la perte de produits financiers s'il est présenté comme une première approche, puis corrigé (2,70 € et 2,97 €) : 0,5 point sur l'item 3.2-01 ; capitaux propres part du groupe (296 → 256 M€) au lieu des capitaux propres consolidés ; toute recommandation argumentée qui tient compte du signal, du contrôle et de la contrainte du crédit syndiqué.

**Erreurs fréquentes**
- Oublier les produits financiers perdus : le rachat paraît plus relutif (2,97 €) et le dividende exceptionnel neutre pour le BPA (2,70 €).
- Présenter la hausse du BPA comme une création de valeur.
- Calculer la nouvelle part de LESTRADEC sur 10 000 000 actions, ou supposer qu'elle apporte ses titres au rachat.
- Développer la procédure juridique du rachat (autorisation, plafonds légaux) : hors programme.
- `JUR-T13` — recommandation sans lien avec la situation du groupe (ratio du crédit syndiqué, cours après l'avertissement, contrôle familial).

---

### 3.3 Valeur de l'action par le modèle de Gordon-Shapiro (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Valeur théorique : 1,20 / (8,5 % − 6 %) = 48,00 € | 0,5 |
| 3.3-02 | Rentabilité implicite au cours de 42 € : 1,20 / 42 + 6 % = 8,86 % | 0,5 |
| 3.3-03 | Interprétation de l'écart | 1 |

**Valeur théorique (0,5 pt).** Le modèle de Gordon-Shapiro actualise à l'infini un dividende qui croît à un taux constant g, inférieur à la rentabilité exigée k. Le prochain dividende (1,20 €) est perçu dans un an :

P0 = D1 / (k − g) = 1,20 / (0,085 − 0,06) = 1,20 / 0,025 = **48,00 €**.

**Rentabilité implicite (0,5 pt).** Un investisseur qui achète l'action 42 € obtient, si le dividende croît de 6 % par an, une rentabilité égale au rendement du dividende plus la croissance : 1,20 / 42 + 6 % = 2,86 % + 6 % = **8,86 %**.

**Interprétation (1 pt).**
- Selon les hypothèses de la direction, l'action vaut 48,00 €, soit 14,3 % de plus que le cours. De même, la rentabilité implicite (8,86 %) dépasse la rentabilité exigée par le MEDAF (8,5 %) : l'action paraît sous-évaluée.
- Le marché ne partage pas ces hypothèses. Au cours de 42 € et pour une rentabilité exigée de 8,5 %, la croissance implicite du dividende est de 8,5 % − 2,86 % = **5,64 %** : le marché anticipe une croissance un peu plus faible, ou exige une rentabilité plus élevée après l'avertissement de 2026.
- Le modèle est très sensible à l'écart k − g, ici de 2,5 points seulement : avec une croissance de 5,5 %, la valeur tombe à 40,00 € ; avec 5 %, à 34,29 €. Une différence d'un demi-point sur la croissance suffit à expliquer l'écart avec le cours.
- La croissance de 6 % est discutable. Elle est supposée constante et illimitée, alors qu'elle dépasse la croissance de long terme de l'économie. Elle n'est finançable sans ressources nouvelles qu'au prix d'un retour au taux de distribution cible : rentabilité des capitaux propres part du groupe × taux de rétention = 27,0 / 296 × (1 − 44,4 %) = 9,12 % × 55,6 % = 5,07 % avec le taux de 2026, mais 9,12 % × 2/3 = 6,08 % avec le taux cible d'un tiers (calcul facultatif). Maintenir durablement un taux de distribution de 44,4 % et une croissance de 6 % n'est donc pas compatible, sauf si le plan « Horizon 2030 » relève la rentabilité.
- **Conclusion** : l'écart ne prouve pas une erreur du marché ; il mesure la différence entre les anticipations de la direction et celles des investisseurs, que la communication du plan devra réduire. Il éclaire la question 3.2 : racheter à 44 € n'enrichit les actionnaires restants que si la valeur réelle dépasse 44 €, ce qui suppose une croissance d'au moins 5,77 % (8,5 % − 1,20 / 44, calcul facultatif).

**Réponses tolérées** : croissance implicite présentée à la place de la sensibilité ; rentabilité implicite arrondie à 8,9 % ; autres valeurs de sensibilité, si elles sont justes.

**Erreurs fréquentes**
- Augmenter de 6 % le dividende proposé alors que l'annexe donne directement le prochain dividende : 1,20 × 1,06 = 1,272 € et une valeur de 50,88 €. L'item 3.3-01 est perdu ; la suite est notée en cohérence.
- Appliquer la formule sans vérifier que la rentabilité exigée dépasse la croissance.
- Conclure que l'action « doit » remonter à 48 € : la valeur dépend d'une hypothèse de croissance que le marché ne partage pas.
- `JUR-T13` — calcul sans interprétation, ou interprétation sans lien avec le cours de 42 € et le rachat envisagé.

---

### 3.4 Réaction du cours à l'avertissement sur résultats (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Définition de l'efficience et de ses trois formes (Fama, 1970) | 0,5 |
| 3.4-02 | Réaction de J+1 : intégration rapide de l'information publique, cohérente avec la forme semi-forte | 0,5 |
| 3.4-03 | Mouvements de J−3 et J−2 sans information publique : forme forte mise en défaut | 0,5 |
| 3.4-04 | Poursuite de la baisse puis rebond : sur-réaction et biais comportementaux (Kahneman et Tversky, 1973) | 1 |
| 3.4-05 | Conséquences pour la communication financière de TERRALBE | 0,5 |

**Efficience (0,5 pt).** Selon Fama (1970), un marché est efficient si les cours reflètent à tout instant l'information disponible, si bien qu'aucun investisseur ne peut obtenir durablement une rentabilité anormale. Trois formes : **faible** (les cours intègrent l'information contenue dans les cours passés), **semi-forte** (ils intègrent toute l'information publique), **forte** (ils intègrent toute l'information, y compris non publique).

**Le jour de la réaction (0,5 pt).** Le communiqué est publié le 14 octobre après la clôture. Dès la séance suivante (J+1), la rentabilité anormale est de − 9,0 % et 412 000 titres s'échangent, près de 19 fois le volume moyen de septembre (22 000). L'information publique est intégrée en une séance : c'est conforme à l'efficience au sens semi-fort. L'ampleur est cohérente avec la nouvelle : le résultat attendu passe de 34 M€ à 27 M€ (− 21 %).

**Avant l'annonce (0,5 pt).** Les 9 et 12 octobre (J−3 et J−2), le titre perd 3,3 points de rentabilité anormale, avec des volumes triples de la normale (64 000 et 71 000 titres), alors qu'aucune information n'est publiée. Des investisseurs semblent avoir agi sur une information non publique (fuite, initiés) : la forme forte n'est pas vérifiée, ce qui est le cas général. Nuance : l'article du 30 septembre sur les récoltes était public, mais il ne permettait pas de chiffrer l'impact sur le résultat ; on ne peut pas affirmer que le marché l'a ignoré.

**Après l'annonce (1 pt).**
- La baisse se poursuit en J+2 et J+3 (− 2,6 % et − 1,6 % de rentabilité anormale) alors qu'aucune information nouvelle sur TERRALBE n'est publiée, hormis des commentaires d'analystes et de forums. Au plus bas (19 octobre), la rentabilité anormale cumulée atteint − 16,5 %. Le titre regagne ensuite 5,5 points de J+4 à J+10, après l'article du 21 octobre, pour finir à − 11,0 %.
- Ce profil (chute, prolongement, rebond partiel) évoque une **sur-réaction** puis une correction, difficile à concilier avec un ajustement instantané et juste des cours. La sanction paraît forte pour une baisse de résultat présentée comme liée à une récolte exceptionnelle : un an de résultat amputé de 7 M€ représente environ 0,70 € par action, bien moins que les 7,79 € perdus par le cours entre le 6 et le 19 octobre (49,20 € → 41,41 €).
- **Biais en jeu** (Kahneman et Tversky, 1973) : **représentativité**, les investisseurs extrapolent une mauvaise année en tendance (« 2027 ne sera-t-il pas pire encore ? ») ; **disponibilité**, les informations frappantes et récentes (pluies, chute du cours, forums) pèsent plus que les données de long terme ; **ancrage**, sur l'objectif de 34 M€ annoncé en juillet (surprise amplifiée) puis sur les objectifs de cours abaissés à 38 € ; **mimétisme**, les ventes entraînent les ventes (188 000 titres en J+2). La finance comportementale (rationalité limitée, comportements mimétiques) explique pourquoi les prix peuvent s'écarter un temps de la valeur.
- Nuance : la baisse résiduelle (− 11 %) peut aussi être rationnelle si le marché révise la croissance de long terme (pression des marques de distributeurs, coûts de l'énergie), comme le suggère la croissance implicite de 5,64 % (question 3.3).

**Conséquences pour TERRALBE (0,5 pt).**
- Publier sans délai et de façon égale pour tous les investisseurs toute information susceptible d'influencer le cours : les mouvements des 9 et 12 octobre montrent un coût de l'asymétrie d'information (soupçon d'initiés, perte de confiance). L'AMF veille à cette égalité d'information.
- Donner des objectifs prudents ou en fourchette, et expliquer la part conjoncturelle (récolte) et la part durable (marges) de la baisse, pour limiter les sur-réactions.
- Présenter le plan « Horizon 2030 » avec des hypothèses vérifiables, pour rapprocher les anticipations du marché de celles de la direction (question 3.3).
- Dans un marché efficient, choisir le moment d'une opération sur le capital n'apporte rien ; si le cours a sur-réagi, un rachat d'actions après la baisse peut au contraire profiter aux actionnaires restants, à condition que la direction ne dispose pas d'une information défavorable non publiée.

**Réponses tolérées** : lecture des volumes comme une anticipation par des analystes à partir de l'information publique (forme semi-forte discutée), si elle est argumentée ; autres biais pertinents reliés à une donnée de l'annexe (aversion aux pertes, excès de confiance des investisseurs avant l'annonce) ; référence facultative à d'autres auteurs (Shiller, De Bondt et Thaler) si elle est reliée au cas.

**Erreurs fréquentes**
- Calculer ou recalculer les rentabilités anormales : elles sont données, aucun calcul n'est demandé.
- Affirmer qu'Euronext est efficient au sens fort, ou que Fama a fondé la finance comportementale.
- Réciter une liste de biais sans les relier aux dates, aux volumes et aux articles de l'annexe (`JUR-T13`).
- `JUR-M01` — oublier les références aux théories fondatrices (efficience, asymétrie d'information) dans une question de réflexion.

---

### 3.5 Portefeuille de LESTRADEC Participations (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Poids 70 % / 30 % ; rentabilité espérée 9,35 % ; écart-type 20,29 % ; bêta 0,93 | 1,5 |
| 3.5-02 | Sharpe : 0,22 (TERRALBE), 0,33 (fonds), 0,26 (portefeuille) ; Treynor : 6,11 %, 5,00 %, 5,75 % | 1 |
| 3.5-03 | Risque de l'action TERRALBE : systématique 29,16 % de la variance (écart-type 13,50 %), spécifique 70,84 % (21,04 %) | 0,5 |
| 3.5-04 | Lecture au sens de Markowitz (1952) et conseil à la holding | 1 |

**Rentabilité, risque et bêta du portefeuille (1,5 pt).**
- Poids : actions TERRALBE 5 400 000 × 42 = 226,8 M€ ; fonds 97,2 M€ ; total 324,0 M€. Poids : **70 %** et **30 %**.
- Rentabilité espérée : 0,70 × 9,5 % + 0,30 × 9,0 % = **9,35 %**.
- Variance : 0,70² × 0,25² + 0,30² × 0,15² + 2 × 0,70 × 0,30 × 0,54 × 0,25 × 0,15 = 0,030625 + 0,002025 + 0,008505 = 0,041155. Écart-type = √0,041155 = **20,29 %**.
- Bêta : 0,70 × 0,90 + 0,30 × 1,00 = **0,93**.

**Ratios de performance (1 pt).**

| | Rentabilité espérée | Écart-type | Bêta | Sharpe = (E − 4 %) / σ | Treynor = (E − 4 %) / β |
|---|---:|---:|---:|---:|---:|
| Action TERRALBE | 9,50 % | 25,00 % | 0,90 | 0,22 | 6,11 % |
| Fonds indiciel | 9,00 % | 15,00 % | 1,00 | 0,33 | 5,00 % |
| Portefeuille | 9,35 % | 20,29 % | 0,93 | 0,26 | 5,75 % |

**Risque systématique et risque spécifique de l'action TERRALBE (0,5 pt).** Variance totale : 0,25² = 0,0625. Risque systématique : 0,90² × 0,15² = 0,018225, soit **29,16 %** de la variance (écart-type 13,50 %). Risque spécifique : 0,0625 − 0,018225 = 0,044275, soit **70,84 %** de la variance (écart-type 21,04 %). Pour le portefeuille (facultatif) : risque systématique 0,93² × 0,0225 = 0,019460 et risque spécifique 0,70² × 0,044275 = 0,021695, soit 52,71 % de la variance.

**Lecture et conseil (1 pt).**
- **Diversification** : l'écart-type du portefeuille (20,29 %) est inférieur à la moyenne pondérée des écarts-types (0,70 × 25 % + 0,30 × 15 % = 22,00 %) parce que la corrélation (0,54) est inférieure à 1. Selon Markowitz (1952), le risque d'un portefeuille dépend des corrélations entre ses titres : en combiner de faiblement corrélés réduit le risque sans réduire la rentabilité espérée en proportion.
- **Deux ratios, deux classements** : le ratio de Treynor place l'action TERRALBE en tête (6,11 %), parce qu'il ne retient que le risque systématique et que la holding attend 9,5 %, plus que les 8,5 % exigés par le MEDAF. Le ratio de Sharpe la place en dernier (0,22), parce qu'il retient le risque total, dont 71 % est spécifique. Le ratio de Treynor convient à un investisseur déjà diversifié ; pour LESTRADEC Participations, dont 70 % du patrimoine est investi dans TERRALBE, c'est le risque total qui compte : le ratio de Sharpe est le bon critère.
- **Risque non rémunéré** : le marché ne rémunère que le risque systématique. La holding supporte un risque spécifique important (récoltes, marques de distributeurs, avertissement d'octobre) qui n'est pas rémunéré : c'est le prix du contrôle familial. Le fonds seul offrirait un meilleur ratio de Sharpe (0,33) que le portefeuille (0,26).
- **Conseil** : la holding ne peut pas céder de titres TERRALBE sans menacer son contrôle (54 %). Elle peut réduire son risque en orientant vers le fonds les liquidités qu'elle reçoit au-delà de ses besoins, en particulier les 21,6 M€ du dividende exceptionnel si l'option A est retenue. Avec un cours ex-dividende théorique de 38 €, ses actions TERRALBE vaudraient 205,2 M€ et le fonds 118,8 M€ : le poids de TERRALBE tomberait à 63 % et l'écart-type du portefeuille à 19,36 % (calcul facultatif). Le rachat (option B) va dans le sens inverse : il renforce le poids de TERRALBE dans le contrôle familial et l'endettement du groupe, donc le risque de l'action. L'estimation de 9,5 % mérite aussi d'être discutée : un actionnaire familial peut surestimer les perspectives de sa propre société (excès de confiance).

**Réponses tolérées** : écart-type à 20,29 % ou 20,3 % ; ratio de Sharpe à trois décimales (0,220 ; 0,333 ; 0,264) ; Treynor exprimé en fraction (0,0611) ; décomposition présentée par le carré du coefficient de corrélation (0,54² = 29,16 %), le fonds étant assimilé au marché ; conseil fondé sur d'autres moyens de diversification (placements de la holding, recours à l'emprunt limité) s'il est argumenté.

**Erreurs fréquentes**
- Calculer l'écart-type du portefeuille comme la moyenne pondérée des écarts-types (22,00 %) : c'est ignorer la corrélation, cœur de l'apport de Markowitz.
- Oublier le facteur 2 dans le terme de covariance, ou utiliser la corrélation au lieu de la covariance (ρ × σT × σM = 0,02025).
- Inverser les dénominateurs des ratios : Sharpe sur l'écart-type, Treynor sur le bêta.
- Conclure que la diversification supprime tout risque : le risque systématique demeure.
- `JUR-T02` — résultats sans conseil adapté à la situation d'une holding de contrôle.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 67-69 | politique de dividende (signal, neutralité, effet cliquet, frictions) ; rachats d'actions (effets sur le nombre d'actions, le BPA, les capitaux propres, signal) ; aspects juridiques exclus | [V] | F05 § 0, 2 et 3 |
| Guide pédagogique DSCG, juillet 2026, p. 73-77 | efficience (trois formes, rôle de l'information, timing) ; finance comportementale ; Gordon-Shapiro ; portefeuille de deux titres, corrélation fournie, Sharpe et Treynor ; vérifications empiriques et calcul de la frontière exclus | [V] | F06 § 0 et 3 ; `perimetre_ue2.yaml` |
| Modigliani et Miller (1961) | neutralité du dividende en marché parfait, « dividende maison » | [V programme 4.1] | F10 § 3 |
| Spence (1973) ; Ross (1977) | signal coûteux ; signal par la structure financière | [V programme 4.1] | F10 § 3 |
| Lintner (1956), facultatif | lissage du dividende, effet cliquet | [S] | F10 § 2 |
| Jensen et Meckling (1976) | coûts d'agence | [V programme 2.1] | F10 § 3 |
| Gordon et Shapiro | valeur d'une action à croissance constante du dividende | [V programme 5.2, sans année] | F10 § 2 |
| Fama (1970) | efficience informationnelle, trois formes | [V programme 5.1] | F10 § 1 ; F06 § 3 |
| Kahneman et Tversky (1973) | représentativité, disponibilité, ancrage | [V programme 5.1 pour la référence ; S pour le contenu] | F10 § 1 ; F06 § 4 |
| Markowitz (1952) | diversification, rôle de la corrélation | [V programme 5.3] | F10 § 2 |
| MEDAF (Sharpe, 1964) ; ratio de Treynor (1965) ; ratio de Sharpe (1966) | risque systématique rémunéré ; mesures de performance | [S] | F10 § 2 ; F02 § 2 |
| Taux sans risque 4 % et prime de risque du marché 5 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 |
| Placement de trésorerie à 2,4 % | hypothèse d'énoncé, proche de l'€STR d'octobre 2026 (2,44 %) | [V] pour l'€STR | F11 § 1 |
