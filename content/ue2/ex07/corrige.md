# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 7 — Dossier 1 (18 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 évaluation, F05 ingénierie financière, F10 auteurs et théories, F11 données de marché (toutes à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (bilans, approche immobilière, ANC et ANCC, goodwill, multiples implicites, emprunts, levier, parité, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un ANCC calculé avec une autre valeur des terrains à la question 1.2).

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Approche immobilière et cycle de vie | `3.3.c` Calculer la valeur d'une entreprise en fonction de son cycle de vie | 2,5 |
| 1.2 ANC et ANCC consolidés | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine | 3 |
| 1.3 Goodwill par la rente actualisée | `3.3.b` Calculer la survaleur de l'entreprise à partir de ses actifs intangibles (goodwill) | 3,5 |
| 1.4 LBO secondaire | `4.2.d` Décrypter les montages financiers avec et sans levier financier | 3,5 |
| 1.5 Offre mixte de KAVELIA | `4.2.c` Analyser les opérations de fusions et d'acquisitions ; `4.2.b` Analyser les motifs des opérations de réorganisation | 3 |
| 1.6 Introduction en bourse et choix de la voie de sortie | `4.2.e` Analyser les introductions en bourse, les retraits de la cotation et les offres publiques ; `4.2.b` | 2,5 |
| **Total** | | **18** |

Part du calcul : environ 11 points (1.1-01 et 1.1-02, 1.2-01 à 1.2-04, 1.3-01 à 1.3-04, 1.4-02 à 1.4-04, 1.5-01 à 1.5-03, 1.6-01). Part de l'analyse : environ 7 points. Les questions de comparaison et de recommandation (1.5 et 1.6) valent autant que les calculs : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 1.1 Approche immobilière et cycle de vie (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Cessions comparables : A4 (constructible) et C4 (agricole) écartées ; prix de référence : zone A 950 k€/ha, zone B 400 k€/ha, zone C 750 k€/ha | 0,5 |
| 1.1-02 | Valeur des terrains : 38,0 + 12,0 + 18,0 = 68,0 M€ ; plus-value latente : 68,0 − 32,0 = 36,0 M€ | 1 |
| 1.1-03 | Place de l'approche patrimoniale pour un groupe mature riche en actifs fonciers : complément et valeur plancher, les flux et les multiples restant la référence | 0,5 |
| 1.1-04 | Limites de l'approche immobilière et de l'approche patrimoniale | 0,5 |

**Prix de référence (0,5 pt).** Les cessions A4 (terrain constructible à usage d'habitation, 4 200 / 1,5 = 2 800 k€/ha) et C4 (terrain agricole, 120 / 8,0 = 15 k€/ha) n'ont pas le même classement que les sites du groupe : leur prix reflète un autre usage possible du sol. Elles sont écartées.

| Zone | Prix à l'hectare des cessions comparables (k€/ha) | Prix de référence (k€/ha) |
|---|---|---:|
| A – Littoral atlantique | 1 800 / 2,0 = 900 ; 3 500 / 3,5 = 1 000 ; 3 800 / 4,0 = 950 | **950** |
| B – Arrière-pays atlantique | 1 900 / 5,0 = 380 ; 1 050 / 2,5 = 420 ; 2 400 / 6,0 = 400 | **400** |
| C – Littoral d'Occitanie | 2 100 / 3,0 = 700 ; 1 600 / 2,0 = 800 ; 3 000 / 4,0 = 750 | **750** |

**Valeur et plus-value (1 pt).**

| Zone | Surface (ha) | Prix de référence (k€/ha) | Valeur (M€) | Valeur au bilan (M€) | Plus-value (M€) |
|---|---:|---:|---:|---:|---:|
| A | 40 | 950 | 38,0 | 18,0 | 20,0 |
| B | 30 | 400 | 12,0 | 6,0 | 6,0 |
| C | 24 | 750 | 18,0 | 8,0 | 10,0 |
| **Total** | **94** | | **68,0** | **32,0** | **36,0** |

Les terrains valent plus du double de leur valeur au bilan : la plus-value latente de **36,0 M€** représente plus de la moitié des capitaux propres consolidés (64 M€).

**Place de l'approche patrimoniale (0,5 pt).** Le choix d'une méthode dépend du stade du cycle de vie : la méthode du venture capital à la création, sans actifs ni flux positifs ; l'actualisation des flux en croissance ; les multiples et les flux à maturité ; l'approche patrimoniale en déclin ou en difficulté. SOLVÉRAN est un groupe **mature** : fondé en 1996, il croît modérément (+ 7,1 % de chiffre d'affaires en 2026), dégage une marge d'EBITDA de 25 % et a déjà connu un LBO. Ses méthodes de référence sont donc les flux et les multiples (questions 1.3 et 1.5). L'approche patrimoniale garde pourtant une place, non en raison de son cycle de vie mais de la **nature de ses actifs** : son activité repose sur un **patrimoine tangible**, les terrains de 16 sites sur 24 et 5 000 hébergements. Ces actifs ont une valeur propre, indépendante de l'exploitation (un terrain littoral classé en zone de loisirs est rare et cessible), qui fonde la confiance des prêteurs. L'approche patrimoniale sert alors de **complément** et de **valeur plancher** dans la négociation avec les acquéreurs. La méthode du venture capital, conçue pour une start-up, n'aurait ici aucun sens.

**Limites (0,5 pt).**
- L'approche immobilière repose sur peu de transactions (trois par zone), hétérogènes par la taille et la localisation ; elle ne remplace pas une évaluation site par site et suppose que les terrains pourraient être vendus au prix de référence, alors qu'un terrain de 40 hectares en un seul ensemble ne se cède pas comme une parcelle de 2 hectares.
- La valeur d'un terrain de camping dépend de son classement : un changement des règles d'urbanisme ou des risques littoraux (érosion, submersion) peut la réduire fortement.
- L'approche patrimoniale est statique : elle ignore la rentabilité future, la marque, la clientèle et le savoir-faire d'exploitation. Les 8 sites en bail de longue durée, dont les terrains n'appartiennent pas au groupe, n'y apparaissent que par leurs aménagements. Elle doit donc être complétée par une méthode fondée sur la rentabilité (question 1.3).

**Réponses tolérées** : prix de référence calculé en moyenne pondérée par les surfaces (A : 9 100 / 9,5 = 958 k€/ha ; B : 5 350 / 13,5 = 396 k€/ha ; C : 6 700 / 9,0 = 744 k€/ha ; valeur 68,1 M€) : l'item 1.1-01 n'est pas accordé, la convention de l'annexe n'étant pas respectée, mais l'item 1.1-02 est noté en cohérence ; analyse du cycle de vie présentée sous forme de tableau.

**Erreurs fréquentes**
- Garder les cessions A4 et C4 dans les moyennes (zone A : 1 412,5 k€/ha ; zone C : 566,25 k€/ha ; valeur 82,1 M€) : un terrain constructible ou agricole n'est pas comparable à un terrain de camping.
- Calculer la moyenne des prix de cession au lieu de la moyenne des prix à l'hectare.
- Présenter la valeur des terrains comme une plus-value, ou oublier de retrancher la valeur au bilan.
- `JUR-T13` — exposé général sur le cycle de vie sans lien avec SOLVÉRAN (patrimoine foncier, maturité, LBO).

---

### 1.2 ANC et ANCC consolidés (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | ANC = 64,0 − 1,6 = 62,4 M€, soit 31,20 € par action | 0,5 |
| 1.2-02 | Retraitements : goodwill − 6,0 ; terrains + 36,0 ; hébergements − 4,0 (62,0 − 66,0) | 1 |
| 1.2-03 | Impôt latent : 25 % × (36,0 − 4,0) = 8,0 M€ | 0,5 |
| 1.2-04 | ANCC = 80,4 M€, soit 40,20 € par action | 0,5 |
| 1.2-05 | Commentaire de l'écart entre l'ANCC et les capitaux propres | 0,5 |

**ANC (0,5 pt).** Les actifs fictifs (frais d'établissement et frais d'émission d'emprunts) n'ont aucune valeur de cession : ANC = 64,0 − 1,6 = **62,4 M€**, soit 62 400 000 / 2 000 000 = **31,20 €** par action.

**ANCC (2 pts).**

| Élément | M€ |
|---|---:|
| ANC | 62,4 |
| − Goodwill inscrit au bilan (éliminé, sans effet d'impôt) | − 6,0 |
| + Plus-value sur terrains (question 1.1) | + 36,0 |
| − Moins-value sur hébergements (62,0 − 66,0) | − 4,0 |
| − Impôt latent : 25 % × (36,0 − 4,0) | − 8,0 |
| **ANCC** | **80,4** |
| **Valeur par action** (80 400 000 / 2 000 000) | **40,20 €** |

- Le goodwill comptable correspond au prix payé en 2021 au-delà des actifs identifiés : ce n'est pas un actif que l'on pourrait céder séparément. La survaleur actuelle du groupe est mesurée à part, par la rente du goodwill (question 1.3) ; la conserver ici la compterait deux fois.
- L'impôt latent traduit l'impôt que le groupe supporterait s'il réalisait ses plus-values : un acquéreur ne paierait pas pour une plus-value dont une partie reviendrait à l'État. La moins-value sur les hébergements réduit cet impôt.
- Les provisions, justifiées, et les autres actifs et passifs, retenus pour leur valeur au bilan, ne sont pas retraités.

**Commentaire (0,5 pt).** L'ANCC (80,4 M€) dépasse les capitaux propres consolidés (64,0 M€) de 16,4 M€, soit 25,6 % : la plus-value sur les terrains, nette d'impôt (27,0 M€), fait plus que compenser l'élimination du goodwill et des actifs fictifs (7,6 M€) et la moins-value nette sur les hébergements (3,0 M€). Le bilan consolidé sous-estime donc le patrimoine du groupe, surtout le patrimoine foncier du littoral. L'ANCC de 40,20 € par action constitue un **plancher de négociation** pour la famille DORVAL et le fonds : toutes les offres de l'annexe (75 € à 84 €) le dépassent largement, ce qui confirme qu'elles rémunèrent surtout la rentabilité du groupe, et pas seulement son patrimoine.

**Réponses tolérées** : présentation par différence entre actifs réels réévalués et dettes (211,6 − 1,6 − 6,0 + 36,0 − 4,0 − 8,0 − 3,6 − 118,0 − 26,0 = 80,4 M€) ; impôt latent calculé séparément sur chaque écart (9,0 − 1,0 = 8,0 M€) ; ANCC calculé avec la valeur des terrains obtenue par le candidat à la question 1.1.

**Erreurs fréquentes**
- Oublier l'impôt latent (ANCC de 88,4 M€, 44,20 € par action) ou le calculer sur les seuls terrains (9,0 M€).
- Maintenir le goodwill comptable dans l'ANCC (86,4 M€) puis ajouter la survaleur de la question 1.3 : double comptabilisation.
- Appliquer un impôt latent à l'élimination des actifs fictifs ou du goodwill, contraire à l'annexe.
- `JUR-E03` — conclure sur la seule valeur patrimoniale, sans indiquer qu'elle sert de plancher dans une fourchette de négociation.

---

### 1.3 Goodwill par la rente actualisée (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | Rémunération normale de l'ANCCE : 4 % × 75,0 = 3,0 M€ ; rentes : 8,0 ; 9,0 ; 10,0 ; 11,0 ; 12,0 M€ | 0,5 |
| 1.3-02 | Goodwill = somme des rentes actualisées à 10 % = 37,2 M€ | 1 |
| 1.3-03 | Valeur globale = 80,4 + 37,2 = 117,6 M€, soit 58,79 € par action | 0,5 |
| 1.3-04 | Valeur par les flux : VCP = 240,0 − 96,0 = 144,0 M€, soit 72,00 € par action | 0,5 |
| 1.3-05 | Explication de l'écart et cohérence des deux valeurs ; sources du goodwill | 1 |

**Rente et goodwill (1,5 pt).** La rente du goodwill est le bénéfice que le groupe dégage au-delà de la rémunération normale de son actif d'exploitation : rente = bénéfice économique − 4 % × 75,0 = bénéfice − 3,0.

| Exercice | 2027 | 2028 | 2029 | 2030 | 2031 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Bénéfice économique (M€) | 11,0 | 12,0 | 13,0 | 14,0 | 15,0 | |
| Rémunération normale de l'ANCCE (M€) | 3,0 | 3,0 | 3,0 | 3,0 | 3,0 | |
| **Rente du goodwill (M€)** | **8,0** | **9,0** | **10,0** | **11,0** | **12,0** | |
| Coefficient d'actualisation à 10 % | 1,1⁻¹ | 1,1⁻² | 1,1⁻³ | 1,1⁻⁴ | 1,1⁻⁵ | |
| Rente actualisée (M€) | 7,27 | 7,44 | 7,51 | 7,51 | 7,45 | **37,19** |

Goodwill = **37,2 M€** (somme calculée sans arrondi intermédiaire : 37,19 M€).

**Valeur globale (0,5 pt).** Valeur globale = ANCC + goodwill = 80,4 + 37,19 = **117,6 M€**, soit 117,59 M€ / 2 000 000 actions = **58,79 €** par action.

**Valeur par les flux (0,5 pt).** L'annexe donne une valeur de l'entreprise (VGE), qui revient à tous les apporteurs de capitaux : il faut en retirer la dette financière nette pour obtenir la valeur des capitaux propres (VCP). VCP = 240,0 − 96,0 = **144,0 M€**, soit **72,00 €** par action.

**Écart et cohérence (1 pt).**
- La valeur par les flux dépasse la valeur patrimoniale corrigée du goodwill de 26,4 M€ (18,3 % de 144,0 M€). Elle suppose une survaleur implicite de 144,0 − 80,4 = 63,6 M€, contre 37,2 M€ par la rente.
- **Durée** : la rente est limitée à cinq ans, comme si les avantages du groupe disparaissaient après 2031 ; l'évaluation par les flux suppose au contraire une croissance de 2 % à l'infini, et 80 % de sa VGE vient de la valeur terminale.
- **Hypothèses** : la rente reprend les bénéfices du plan de la direction, l'évaluation par les flux un scénario plus prudent ; l'écart tient donc surtout à la durée et aux taux.
- **Taux** : la rente est actualisée à 10 %, taux majoré pour l'incertitude de la survaleur ; les flux le sont au CMPC de 7,0 %.
- Les deux valeurs ne se contredisent pas : elles reposent sur des hypothèses différentes sur la durabilité des avantages du groupe. La valeur patrimoniale corrigée du goodwill (58,79 €) est prudente ; la valeur par les flux (72,00 €), plus sensible aux hypothèses de long terme, est la référence des acquéreurs.
- **Sources du goodwill** : emplacements littoraux rares et protégés par les règles d'urbanisme, notoriété et classement quatre et cinq étoiles, fichier de clients fidèles, savoir-faire de gestion des sites et des saisonniers ; ces actifs immatériels n'apparaissent pas au bilan, d'où un goodwill économique (37,2 M€) très supérieur au goodwill comptable (6,0 M€).

**Réponses tolérées** : goodwill à 37,19 M€ et valeur globale à 117,59 M€ ; valeur par action de 58,80 € à partir de montants arrondis à une décimale ; actualisation par coefficients arrondis à quatre décimales (écart inférieur à 0,01 M€) ; écart exprimé par rapport à la valeur patrimoniale (22,5 %).

**Erreurs fréquentes**
- Actualiser la rente au taux de rémunération de 4 % (goodwill de 44,17 M€), ou calculer la rente sur l'ANCC de la question 1.2 au lieu de l'ANCCE fourni.
- Ajouter le goodwill à l'ANCCE (75,0 + 37,2 = 112,2 M€) au lieu de l'ANCC.
- Comparer la VGE de 240,0 M€ à une valeur des capitaux propres sans retrancher la dette financière nette.
- `JUR-T14` — affirmer qu'une des deux méthodes est « fausse » au lieu d'expliquer l'écart par la durée de la rente et les taux.

---

### 1.4 LBO secondaire (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Schéma du montage : actionnaires de SOLVÉRAN Invest, dettes de la holding, détention de SOLVÉRAN Holding, remontée des dividendes, vendeurs | 0,5 |
| 1.4-02 | Bilan d'ouverture : titres 150,0 M€ ; fonds propres 105,0 M€ (MONTRIVE 73,5 ; DORVAL 21,0 ; cadres 10,5) ; dette senior 30,0 M€ ; dette junior 15,0 M€ | 0,5 |
| 1.4-03 | Tableau d'amortissement de la dette senior : annuité 6,93 M€ | 1 |
| 1.4-04 | Capacité de remboursement : service de la dette 8,28 M€ par an ; dividendes 8,8 à 12,0 M€ ; couverture de 1,06 à 1,45 ; trésorerie cumulée 10,60 M€ en 2032, inférieure aux 15,0 M€ de dette junior dus en 2033 | 0,5 |
| 1.4-05 | Effets de levier et risques | 1 |

**Schéma du montage (0,5 pt).**

```
  MONTRIVE Capital IV     Famille DORVAL     14 cadres dirigeants          Banques           Fonds de dette privée
        73,5 (70 %)         21,0 (20 %)          10,5 (10 %)             senior 30,0          junior 15,0
             \                  |                   /                         |                     |
              +-------- fonds propres 105,0 -------+                          |                     |
                                |                                             |                     |
                      SOLVÉRAN Invest SAS (nouvelle holding)  <---------------+---------------------+
                                |  achète 100 % des titres pour 150,0 M€
                                |  ^ dividendes = 80 % du résultat net consolidé
                                v  |
                      SOLVÉRAN Holding SAS (garde la dette du groupe, DFN 96 M€)
                                | 100 %
                      SOLVÉRAN Plein Air SAS ---> trois filiales régionales (100 %)

  Vendeurs : ARVELINE Capital III 93,0 M€ (62 %), famille DORVAL 42,0 M€ (28 %), cadres 15,0 M€ (10 %)
```

**Bilan d'ouverture de SOLVÉRAN Invest au 1er juillet 2027 (0,5 pt).** Prix : 75 × 2 000 000 = 150,0 M€.

| Actif | M€ | Passif | M€ |
|---|---:|---|---:|
| Titres SOLVÉRAN Holding (100 %) | 150,0 | Capital et primes (70 %) | 105,0 |
| | | dont MONTRIVE Capital IV (70 %) | 73,5 |
| | | dont famille DORVAL (20 %) | 21,0 |
| | | dont cadres dirigeants (10 %) | 10,5 |
| | | Dette senior (20 %) | 30,0 |
| | | Dette junior (10 %) | 15,0 |
| **Total** | **150,0** | **Total** | **150,0** |

La famille réinvestit la moitié du produit de sa cession (21,0 M€ sur 42,0 M€) et les cadres 70 % du leur (10,5 M€ sur 15,0 M€). ARVELINE Capital III encaisse 93,0 M€ et sort entièrement.

**Tableau d'amortissement de la dette senior (1 pt).** Annuité constante = 30,0 × 0,05 / (1 − 1,05⁻⁵) = **6,93 M€**.

| Échéance (30 juin) | Capital début (M€) | Intérêts 5 % (M€) | Amortissement (M€) | Annuité (M€) | Capital restant dû (M€) |
|---|---:|---:|---:|---:|---:|
| 2028 | 30,00 | 1,50 | 5,43 | 6,93 | 24,57 |
| 2029 | 24,57 | 1,23 | 5,70 | 6,93 | 18,87 |
| 2030 | 18,87 | 0,94 | 5,99 | 6,93 | 12,88 |
| 2031 | 12,88 | 0,64 | 6,29 | 6,93 | 6,60 |
| 2032 | 6,60 | 0,33 | 6,60 | 6,93 | 0,00 |

(Les amortissements arrondis totalisent 30,01 M€ ; calculés sans arrondi, ils totalisent exactement 30,00 M€.)

**Capacité de remboursement (0,5 pt).** Dette junior : intérêts de 15,0 × 9 % = 1,35 M€ par an, capital de 15,0 M€ le 30 juin 2033. Service de la dette de 2028 à 2032 : 6,93 + 1,35 = 8,28 M€.

| Juin | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|
| Résultat net consolidé de l'exercice précédent (M€) | 11,00 | 12,00 | 13,00 | 14,00 | 15,00 |
| Dividende reçu : 80 % (M€) | 8,80 | 9,60 | 10,40 | 11,20 | 12,00 |
| Service de la dette (M€) | 8,28 | 8,28 | 8,28 | 8,28 | 8,28 |
| Excédent de l'année (M€) | 0,52 | 1,32 | 2,12 | 2,92 | 3,72 |
| Trésorerie cumulée de SOLVÉRAN Invest (M€) | 0,52 | 1,84 | 3,96 | 6,88 | 10,60 |
| Taux de couverture | 1,06 | 1,16 | 1,26 | 1,35 | 1,45 |

Les dividendes couvrent le service de la dette chaque année, mais de justesse en 2028 (marge de 6 %). En juin 2033, la trésorerie accumulée (10,60 M€) ne suffit pas à rembourser les 15,0 M€ de dette junior : il faudra le dividende de 2033, un refinancement ou le produit de la revente par MONTRIVE.

**Effets de levier et risques (1 pt).**
- **Levier financier** : MONTRIVE et ses coactionnaires financent 70 % du prix ; le reste est remboursé par les dividendes du groupe. Chaque euro de dette remboursé accroît la valeur des fonds propres de la holding ; tant que la rentabilité de la participation dépasse le coût de la dette (5 % et 9 %), la rentabilité des fonds propres investis dépasse celle d'un achat sans dette. Mais le levier joue dans les deux sens : un recul du résultat réduit les dividendes alors que le service de la dette est fixe.
- **Levier juridique** : avec 73,5 M€, MONTRIVE contrôle un groupe dont la valeur d'entreprise implicite est de 150,0 + 96,0 = 246,0 M€ (8,2 fois l'EBITDA 2026).
- **Levier managérial** : la famille (20 %) et les cadres (10 %) réinvestissent ; leurs intérêts restent alignés sur ceux du fonds, ce qui réduit les coûts d'agence au sens de Jensen et Meckling (1976). Selon Ross (1977), l'acceptation d'une dette élevée signale aussi la confiance des dirigeants dans les flux futurs. Le levier fiscal éventuel n'est pas étudié.
- **Risques** :
  - **dette empilée** : la dette du groupe (96,0 M€) et celle de la holding (45,0 M€) atteignent 141,0 M€, soit 4,70 fois l'EBITDA 2026 et 57 % de la valeur d'entreprise ; la clause bancaire (3,5) ne porte que sur le groupe, mais les deux dettes dépendent des mêmes flux ;
  - **concurrence entre dividendes et investissements** : distribuer 80 % du résultat chaque année laisse peu d'autofinancement au groupe alors qu'il doit investir 54,0 M€ de 2027 à 2029 (dont le programme de 42 M€) et rembourser sa propre dette ; l'endettement du groupe pourrait monter et approcher le plafond de 3,5 fois l'EBITDA ;
  - **dépendance aux prévisions** : le résultat net doit progresser de 9,6 M€ en 2026 à 15,0 M€ en 2031 ; une mauvaise saison (météo, risques climatiques sur le littoral) ou une hausse des taux réduirait les dividendes, alors que la marge de 2028 n'est que de 0,52 M€ ;
  - **remboursement de la dette junior en 2033** : il dépend d'un refinancement ou de la sortie de MONTRIVE ;
  - **dépendance au maintien des dirigeants** : la réussite repose sur l'équipe en place.

**Réponses tolérées** : schéma présenté sous une autre forme lisible (cases et flèches) s'il fait apparaître les trois niveaux, les apports et les dettes ; tableau d'amortissement en k€ ou à une décimale ; couverture appréciée par la différence plutôt que par le rapport ; dette junior qualifiée d'obligations ou de dette subordonnée ; conclusion sur le remboursement de la dette junior en 2033 fondée sur un dividende 2033 extrapolé, si l'hypothèse est écrite.

**Erreurs fréquentes**
- `JUR-I01` — annuité calculée comme capital / 5 + intérêts constants (6,0 + 1,5 = 7,5 M€), ou intérêts calculés sur le capital initial chaque année.
- `JUR-I02` — confondre le prix (150,0 M€) avec la dette de la holding (45,0 M€) ; amortir la dette junior ; comparer les dividendes à la seule annuité senior.
- Prendre 100 % du résultat net comme dividende, au lieu des 80 % prévus.
- Oublier la dette du groupe (96 M€) dans l'analyse du risque : le levier se cumule sur deux niveaux.
- `JUR-T07` — tableaux d'amortissement et de capacité de remboursement absents ou incomplets.

---

### 1.5 Offre mixte de KAVELIA (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | Parité : 84 / 28 = 3 actions KAVELIA pour 1 action SOLVÉRAN, soit, avec la moitié en numéraire, 42 € et 1,5 action KAVELIA par action ; 3 000 000 actions créées ; augmentation de capital de 3,0 M€ de nominal et 81,0 M€ de prime d'émission ; numéraire 84,0 M€ | 1 |
| 1.5-02 | Capital de KAVELIA après l'opération : 48 000 000 actions ; anciens actionnaires de KAVELIA 93,75 %, anciens actionnaires de SOLVÉRAN 6,25 % (famille DORVAL 1,75 %) | 0,5 |
| 1.5-03 | Prime : 84 / 72 − 1 = 16,7 % ; prime totale 24,0 M€, inférieure aux synergies de 30 M€ | 0,5 |
| 1.5-04 | Motifs économiques et financiers de l'acquisition | 1 |

**Parité et actions à créer (1 pt).**
- Prix total : 84 × 2 000 000 = 168,0 M€, dont la moitié en numéraire (**84,0 M€**) et la moitié en actions (84,0 M€).
- Parité d'échange = 84 / 28 = **3** : une action SOLVÉRAN vaut trois actions KAVELIA. Comme la moitié du prix est payée en numéraire, chaque action SOLVÉRAN est échangée contre **42 € et 1,5 action KAVELIA** (soit 2 actions SOLVÉRAN pour 3 actions KAVELIA et 84 €).
- Actions KAVELIA à créer : 2 000 000 × 1,5 = **3 000 000** (ou 84 000 000 / 28).
- Augmentation de capital : 3 000 000 × 1 € = **3,0 M€** de nominal et 3 000 000 × (28 − 1) = **81,0 M€** de prime d'émission, soit 84,0 M€ de fonds propres nouveaux.

**Capital de KAVELIA après l'opération (0,5 pt).** 45 000 000 + 3 000 000 = 48 000 000 actions.

| Actionnaires | Actions | % du capital |
|---|---:|---:|
| Anciens actionnaires de KAVELIA | 45 000 000 | **93,75 %** |
| Anciens actionnaires de SOLVÉRAN | 3 000 000 | **6,25 %** |
| dont ARVELINE Capital III (62 %) | 1 860 000 | 3,88 % |
| dont famille DORVAL (28 %) | 840 000 | 1,75 % |
| dont cadres dirigeants (10 %) | 300 000 | 0,63 % |

La famille DORVAL passerait de 28 % d'un groupe indépendant à 1,75 % d'un groupe européen : elle perdrait toute influence sur la stratégie de l'entreprise qu'elle a fondée.

**Prime et synergies (0,5 pt).**
- Prime offerte = 84 / 72 − 1 = **16,7 %** par rapport à la valeur par les flux ; 12,0 % par rapport au prix du LBO secondaire (75 €) ; 42,9 % par rapport à la valeur patrimoniale corrigée du goodwill (58,79 €).
- Prime totale : (84 − 72) × 2 000 000 = **24,0 M€**, inférieure à la valeur actuelle des synergies (30 M€). Si les synergies se réalisent, l'opération crée 6,0 M€ de valeur pour les actionnaires de KAVELIA ; les vendeurs captent 80 % des synergies (24 / 30). L'acquéreur ne crée de la valeur que si la prime payée reste inférieure aux synergies.

**Motifs (1 pt).**
- **Croissance externe** : acheter 24 sites et 9 000 emplacements sur la façade atlantique et en Occitanie, rares en raison des règles d'urbanisme du littoral, est plus rapide et plus sûr que d'en créer.
- **Synergies opérationnelles** : achats groupés de mobil-homes, centrale de réservation commune, clientèle d'Europe du Nord qui allonge la saison, réduction des frais de structure (le siège de La Rochelle devient une direction régionale).
- **Consolidation du secteur** : un marché fragmenté se concentre autour de quelques groupes ; la taille renforce le pouvoir de négociation avec les fournisseurs et les plateformes de réservation.
- **Motifs financiers** : un groupe coté accède plus facilement aux marchés de capitaux ; payer pour moitié en actions préserve son endettement et fait partager aux vendeurs le risque de l'intégration ; le groupe pourra financer le programme de 42 M€ de SOLVÉRAN sans contrainte de distribution à une holding.
- **Effets sur la valeur et la gouvernance** : la VGE implicite (168,0 + 96,0 = 264,0 M€, 8,8 fois l'EBITDA 2026) est la plus élevée des trois voies ; le paiement en actions dilue faiblement les actionnaires de KAVELIA (6,25 %) et l'opération est un signal stratégique de leadership européen.

**Réponses tolérées** : parité exprimée « 1,5 action KAVELIA et 42 € pour 1 action SOLVÉRAN » sans mention de la parité de 3, si le calcul est juste ; détail des anciens actionnaires de SOLVÉRAN facultatif, arrondi indifféremment (3,875 % donne 3,87 % ou 3,88 % ; 0,625 % donne 0,62 % ou 0,63 %) ; prime également calculée par rapport à la valeur patrimoniale ou au prix du LBO ; augmentation de capital présentée par sa seule valeur d'émission (84,0 M€).

**Erreurs fréquentes**
- Inverser la parité (28 / 84 = 1/3 d'action KAVELIA par action SOLVÉRAN).
- Créer 6 000 000 actions en oubliant que la moitié du prix est payée en numéraire.
- Calculer la répartition du capital sur 45 000 000 actions au lieu de 48 000 000.
- Conclure que l'offre crée de la valeur pour KAVELIA sans comparer la prime aux synergies.
- `JUR-T13` — motifs génériques (« croissance », « synergies ») sans les rattacher aux données du cas.

---

### 1.6 Introduction en bourse et choix de la voie de sortie (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.6-01 | Prix d'introduction : 80 × (1 − 10 %) = 72 € ; 36 000 000 / 72 = 500 000 actions nouvelles ; capital après : ARVELINE 24,80 %, famille DORVAL 22,40 %, cadres 8,00 %, public 44,80 % | 0,5 |
| 1.6-02 | Fixation du prix, décote d'introduction et asymétrie d'information ; contraintes de transparence | 0,5 |
| 1.6-03 | Comparaison des trois voies du point de vue du fonds, de la famille et des cadres | 1 |
| 1.6-04 | Recommandation argumentée | 0,5 |

**Calculs (0,5 pt).**
- Prix d'introduction : 80 × (1 − 0,10) = **72 €**.
- Actions nouvelles : 36 000 000 / 72 = **500 000** ; capital après l'introduction : 2 500 000 actions.
- ARVELINE cède 620 000 actions et en conserve 1 240 000 − 620 000 = 620 000 ; produit de cession : 620 000 × 72 = 44,6 M€. Le public détient 500 000 + 620 000 = 1 120 000 actions.
- Le prix de 72 € coïncide avec la valeur par les flux (question 1.3) : la décote ramène la valeur par comparaison (80 €) au niveau de la valeur intrinsèque estimée par le cabinet.

| Actionnaires | Actions | % du capital |
|---|---:|---:|
| ARVELINE Capital III | 620 000 | **24,80 %** |
| Famille DORVAL | 560 000 | **22,40 %** |
| Cadres dirigeants | 200 000 | **8,00 %** |
| Public | 1 120 000 | **44,80 %** |
| **Total** | **2 500 000** | **100,00 %** |

**Mécanismes (0,5 pt).**
- **Fixation du prix** : les banques chargées de l'introduction évaluent la société par comparaison avec les sociétés cotées, proposent une fourchette, puis recueillent les intentions d'achat des investisseurs (livre d'ordres) ; le prix est fixé au vu de la demande.
- **Décote** : le prix (72 €) est inférieur de 10 % à la valeur estimée (80 €). Les investisseurs connaissent moins bien la société que les vendeurs, qui ont intérêt à vendre cher : c'est l'asymétrie d'information décrite par Akerlof (1970). Pour attirer les acheteurs, malgré le risque de sélection adverse, la société et les vendeurs consentent une décote, qui coûte ici 620 000 × 8 = 5,0 M€ à ARVELINE. Par extension du raisonnement de Myers et Majluf (1984) sur l'émission d'actions, la cession de titres existants par le fonds peut être lue comme un signal de surévaluation : l'engagement de conservation de 12 mois et le maintien de la famille et des cadres limitent ce signal.
- **Transparence** : une fois cotée, la société publie des comptes semestriels et annuels et informe le marché sans délai ; ces obligations coûtent 0,8 M€ par an et exposent la stratégie aux concurrents, mais elles réduisent l'asymétrie d'information et donc, à terme, le coût du capital.

**Comparaison des trois voies (1 pt).**

| | LBO secondaire (MONTRIVE) | Cession à KAVELIA | Introduction en bourse |
|---|---|---|---|
| Prix par action | 75 € | 84 € (moitié en actions) | 72 € |
| **ARVELINE Capital III** (1 240 000 actions) | 93,0 M€ en numéraire, sortie totale et immédiate | 104,2 M€, dont 52,1 M€ en numéraire et 52,1 M€ en actions KAVELIA incessibles six mois : prix le plus élevé, mais exposé au cours de KAVELIA | 44,6 M€ immédiatement ; 620 000 actions conservées 12 mois au moins, dont la valeur dépendra du marché : sortie partielle et différée |
| **Famille DORVAL** (560 000 actions) | 42,0 M€, dont 21,0 M€ réinvestis : garde 20 % de la nouvelle holding et la direction du groupe | 47,0 M€, dont 23,5 M€ en numéraire ; 1,75 % de KAVELIA : perte de l'indépendance et de la direction | aucune cession ; 22,40 % du capital, actionnaire de référence d'une société cotée, valorisée et liquide |
| **Cadres dirigeants** (200 000 actions) | 15,0 M€, dont 10,5 M€ réinvestis : nouveau partage de la création de valeur | 16,8 M€ ; avenir incertain (siège transformé en direction régionale) | 8,00 % du capital, cessible sur le marché après l'introduction |
| **Groupe** | dette empilée, 80 % du résultat distribué : investissements contraints | intégré à un groupe plus solide ; programme financé | 36 M€ de fonds propres nouveaux pour le programme ; coûts de cotation |

**Recommandation (0,5 pt).** Toute recommandation cohérente avec l'analyse est acceptée. Une réponse possible :
- Pour **ARVELINE**, la cession à KAVELIA donne le prix le plus élevé (84 €, prime de 16,7 %), mais la moitié est payée en actions ; le LBO secondaire offre une sortie totale en numéraire, certaine et immédiate, à un prix supérieur à la valeur par les flux (75 € contre 72 €). L'introduction en bourse est la moins favorable au fonds : prix le plus bas après décote et sortie seulement partielle.
- Pour la **famille DORVAL**, le LBO secondaire permet de rester au capital et à la direction tout en encaissant 21,0 M€ ; l'introduction en bourse préserve aussi son rôle et finance le programme d'investissements ; la cession à KAVELIA met fin à l'indépendance du groupe.
- **Recommandation** : retenir le **LBO secondaire**, qui concilie la sortie totale du fonds en numéraire et la continuité familiale et managériale, à condition de renégocier la distribution de 80 % du résultat (ou de financer une partie du programme par fonds propres) pour ne pas compromettre les investissements ni la clause bancaire ; utiliser l'offre de KAVELIA comme référence de prix dans la négociation avec MONTRIVE. Si la famille accepte de céder le contrôle, l'offre de KAVELIA maximise la valeur pour tous les vendeurs, sous réserve de pouvoir céder rapidement les actions reçues.

**Réponses tolérées** : recommandation de la cession à KAVELIA (prix le plus élevé, groupe plus solide pour financer le programme) ou de l'introduction en bourse (indépendance, financement du programme, sortie progressive du fonds) si elle est argumentée du point de vue des trois catégories d'actionnaires ; comparaison présentée sans tableau si elle est structurée.

**Erreurs fréquentes**
- Calculer le nombre d'actions nouvelles sur la valeur avant décote (36 000 000 / 80 = 450 000).
- Oublier les actions nouvelles dans la répartition du capital (calcul sur 2 000 000 actions).
- `JUR-I03` — ne pas tirer les conséquences de la nouvelle structure d'actionnariat : plus d'actionnaire majoritaire (ARVELINE 24,80 %, famille DORVAL 22,40 %), dilution de la famille de 28 % à 22,40 %, flottant de 44,80 %.
- `JUR-T02` — recommandation sans lien avec les intérêts différents du fonds, de la famille et des cadres.
- Développer la procédure de l'introduction (documents à faire viser, calendrier réglementaire), hors du champ de l'épreuve.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 65-67 | approche patrimoniale (ANC, ANCC, retraitements indiqués et limités) ; goodwill à partir de l'ANCCE, de la VSB ou des CPNE fournis ; approche immobilière à partir des données de l'administration fiscale, sans expertise approfondie ; choix de la méthode selon le cycle de vie | [V] | F03 § 0, 4, 5, 6 et 8 ; `perimetre_ue2.yaml` |
| Programme UE 2, l. 531-536 | ANC et ANCC ; rente du goodwill et goodwill ; ANCCE, VSB, CPNE et bénéfices associés indiqués lors de l'épreuve ; approche immobilière ; méthode du venture capital | [V] | F03 § 0 |
| Guide pédagogique DSCG, juillet 2026, p. 69-71 | parité d'échange et augmentation de capital ; motifs des réorganisations, synergies, prime ; holdings et LBO (schéma, bilan de la holding, tableaux d'amortissement, condition de réussite) ; introductions en bourse (titres nouveaux, cession, prix, asymétrie d'information) ; aspects juridiques et fiscaux exclus | [V] | F05 § 0, 1, 5 et 6 |
| Formules de l'annuité constante et de la rente actualisée | tableaux d'amortissement, goodwill | [S] | F01 ; F03 § 5 ; F05 § 1.2 |
| Données de cessions publiées par l'administration fiscale | source de l'approche immobilière (données de l'exercice fictives) | [S] | F03 § 6 |
| Akerlof (1970) | asymétrie d'information et sélection adverse | [V programme 5.1] | F10 § 1 |
| Jensen et Meckling (1976) | coûts d'agence, alignement des dirigeants actionnaires | [V programme 2.1] | F10 § 3 |
| Ross (1977) | signal par l'endettement | [V programme 4.1] | F10 § 3 |
| Myers et Majluf (1984) | émission d'actions perçue comme un signal de surévaluation (appliquée par extension à la cession de titres par le fonds) | [V programme 7.2] | F10 § 3 |
| Taux sans risque de 4 % | hypothèse d'énoncé, plausible fin 2026 | [S] | F11 |
