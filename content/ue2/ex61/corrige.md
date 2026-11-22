# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 61 — Dossier 1 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F04 diagnostic financier consolidé, F07 risques de taux, de change, trésorerie, climat et matières premières, F08 gouvernance, finance durable et ESG, F10 auteurs et théories, F11 données de marché (octobre 2026), F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (sommes des chiffres d'affaires et des EBITDA par entité et par station, marges d'EBITDA, intérêts de chaque entité sans centralisation, solde net mensuel, résultat financier de la convention et gain, intérêts internes des filiales, effet d'une hausse d'un point des taux courts, indemnités, résultats et effets totaux de l'option et de l'assurance dans les trois scénarios, barème, liste noire, hors-programme ; croissances et poids, besoins de pointe, partage du gain, coût du programme de titres et encours d'équilibre, placement de l'excédent, fonds obligataire, indemnités moyennes des étés passés et taux de compensation vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un gain de la convention calculé avec un solde net mensuel erroné à la question 1.2, ou un effet de la hausse des taux calculé avec des sommes de besoins erronées à la question 1.4).

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Poids, croissance et marge d'EBITDA des entités, croissance des stations et des massifs, saisonnalité et trésorerie | `1.c` Apprécier la performance opérationnelle et financière d'un groupe ; `1.a` Réaliser une analyse financière des comptes consolidés | 2,5 |
| 1.2 Intérêts sans centralisation, solde net, résultat de la convention, gain et partage par les taux internes, besoins de pointe, apports et exigences | `6.1.a` Appliquer les mécanismes de centralisation de trésorerie | 3 |
| 1.3 Ligne confirmée ou programme de titres, encours d'équilibre, répartition de l'excédent d'automne entre les supports | `6.1.b` Discerner les différents types de financement et de placement | 2,5 |
| 1.4 Hausse d'un point des taux courts, valeur du fonds obligataire, exposition du groupe au risque de taux | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 1,5 |
| 1.5 Indemnités moyennes des étés passés, trois scénarios de l'été 2027, comparaison de l'option et de l'assurance paramétrique, place dans la gestion du risque climatique | `6.4.a` Sensibiliser aux instruments de couverture des risques physiques et financiers liés au changement climatique et à la raréfaction des ressources naturelles | 4 |
| 1.6 Éléments extra-financiers du modèle d'affaires qui comptent pour les investisseurs et les banques | `2.1.a` Identifier les éléments extra-financiers pour le diagnostic, dans la lignée du modèle d'affaires de l'entreprise | 1,5 |
| **Total** | | **15** |

Part du calcul : environ 9 points (1.1-01 et 1.1-02, 1.2-01 à 1.2-04, 1.3-01, 1.3-03, 1.4-01, 1.4-02, 1.5-01 à 1.5-03). Part de l'analyse : environ 6 points. Les sommes mensuelles évitent de calculer douze intérêts par entité : le candidat qui additionne d'abord les soldes négatifs et les soldes positifs de chaque entité gagne du temps (`JUR-T07`).

---

### 1.1 Activité et performance des entités et des stations, saisonnalité (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Entités : poids 2026 (Thermes Pyrénées **39,88 %**, Thermes Savoie **27,07 %**, Résidences **33,05 %**), croissance (**+ 0,78 %**, **+ 5,18 %**, **+ 2,57 %** ; groupe + 2,53 %), marge d'EBITDA 2025 et 2026 (**27,93 % → 26,01 %**, **25,18 % → 25,08 %**, **19,73 % → 19,99 %** ; groupe 22,22 % → 21,36 %), frais centraux de 2,41 % du chiffre d'affaires | 1 |
| 1.1-02 | Stations : Esquèdes **+ 3,24 %**, Lhérens **− 4,44 %**, Ussères **+ 0,55 %**, Brévannaz **+ 6,63 %**, Montrevaz **+ 4,83 %** ; Pyrénées **+ 0,28 %**, Savoie **+ 5,82 %** | 0,5 |
| 1.1-03 | Analyse : croissance tirée par la Savoie, marge des thermes des Pyrénées en baisse (chaleur, Lhérens), résidences moins rentables mais régulières ; saisonnalité opposée des thermes et des résidences de Savoie, décalage des encaissements, besoins d'hiver et excédents d'automne, conséquence pour la trésorerie du groupe | 1 |

**Calculs (1,5 pt).**

| Entité | Poids du CA 2026 | Croissance du CA 2026 | Marge d'EBITDA 2025 | Marge d'EBITDA 2026 | Variation de l'EBITDA |
|---|---:|---:|---:|---:|---:|
| Thermes Pyrénées | 39,88 % | + 0,78 % | 27,93 % | 26,01 % | − 6,15 % |
| Thermes Savoie | 27,07 % | + 5,18 % | 25,18 % | 25,08 % | + 4,76 % |
| Résidences | 33,05 % | + 2,57 % | 19,73 % | 19,99 % | + 3,88 % |
| Société de tête (frais centraux nets / CA consolidé) | — | — | 2,28 % | 2,41 % | + 8,33 % |
| **Groupe** | **100 %** | **+ 2,53 %** | **22,22 %** | **21,36 %** | **− 1,42 %** |

Exemples : poids des Thermes Pyrénées = 64,60 / 162,00 = 39,88 % ; croissance = 64,60 / 64,10 − 1 = 0,78 % ; marge 2026 = 16,80 / 64,60 = 26,01 %.

| Station | CA 2025 | CA 2026 | Croissance | Dont thermes | Dont résidence |
|---|---:|---:|---:|---:|---:|
| Esquèdes-les-Bains | 33,90 | 35,00 | + 3,24 % | + 3,88 % | + 1,87 % |
| Lhérens-les-Bains | 23,40 | 22,36 | − 4,44 % | − 4,97 % | − 3,29 % |
| Ussères-les-Bains | 36,40 | 36,60 | + 0,55 % | + 1,61 % | − 1,72 % |
| **Pyrénées** | **93,70** | **93,96** | **+ 0,28 %** | | |
| Brévannaz-les-Bains | 35,30 | 37,64 | + 6,63 % | + 6,84 % | + 6,24 % |
| Montrevaz-les-Bains | 29,00 | 30,40 | + 4,83 % | + 3,17 % | + 7,92 % |
| **Savoie** | **64,30** | **68,04** | **+ 5,82 %** | | |

Les colonnes « dont » ne sont pas exigées. La part des Pyrénées passe de 59,30 % à 58 % du chiffre d'affaires.

**Analyse de la performance (0,5 pt).**
- La croissance du groupe (+ 2,53 %) vient surtout de la Savoie (+ 3,74 M€ sur + 4,00 M€) : les thermes de Brévannaz et la résidence de Montrevaz progressent, cette dernière grâce à la saison d'hiver. Les Pyrénées stagnent (+ 0,28 %). Lhérens recule de 4,44 %, thermes (− 4,97 %) comme résidence (− 3,29 %) ; l'annexe n'en donne pas la cause : le candidat peut avancer, en le présentant comme une hypothèse, l'âge des établissements évoqué par la présentation. Ussères, la station la plus basse, ne progresse que de 0,55 %, avec une résidence en recul, après les annulations de cures pendant les épisodes de chaleur.
- Les thermes sont les plus rentables : en 2026, les deux filiales thermales font 66,95 % du chiffre d'affaires et 72,21 % de l'EBITDA des filiales (43,64 % + 28,57 %). Mais la marge des Thermes Pyrénées perd près de deux points (27,93 % → 26,01 %) et leur EBITDA baisse de 6,15 % pour un chiffre d'affaires presque stable : les charges des établissements sont en grande partie fixes (personnel, énergie des bassins, entretien), et chaque cure annulée en été se perd presque entièrement en marge.
- Les résidences, moins rentables (19,99 %), améliorent un peu leur marge et diversifient la clientèle (skieurs en Savoie). Les frais centraux nets augmentent plus vite que l'activité (+ 8,33 %). La marge d'EBITDA du groupe baisse de 0,86 point : la croissance ne compense pas la sensibilité des thermes des Pyrénées à la chaleur.

**Saisonnalité et trésorerie (0,5 pt).**
- Les thermes n'encaissent rien de décembre à février, alors qu'ils paient les travaux d'entretien et, dès février, le recrutement et la formation des saisonniers ; la part des soins prise en charge par l'assurance maladie et par les organismes complémentaires est encaissée environ 45 jours après la cure, ce qui décale les excédents vers septembre et octobre. Les thermes ont donc un **besoin de trésorerie de décembre à mai** et des **excédents de fin de saison**.
- Les résidences de Savoie réalisent environ les deux tiers de leur chiffre d'affaires de décembre à février : leurs excédents d'hiver coïncident avec les besoins des thermes, d'où l'intérêt de **compenser des saisons opposées** au niveau du groupe (question 1.2).
- La société de tête supporte des frais centraux toute l'année : elle a un besoin permanent.
- La chaleur réduit les encaissements d'été des Pyrénées, donc l'excédent d'automne qui doit financer l'hiver suivant : le risque climatique est aussi un **risque de liquidité** (questions 1.4 et 1.5).

**Réponses tolérées** : poids calculés sur l'EBITDA plutôt que sur le chiffre d'affaires, s'ils sont présentés en complément ; croissance par station limitée au total.

**Erreurs fréquentes**
- Calculer la marge d'EBITDA du groupe en additionnant les marges des entités, ou oublier les frais centraux de la société de tête (EBITDA des filiales de 38,50 M€ au lieu de 34,60 M€).
- Commenter les chiffres sans lien avec la saisonnalité et la trésorerie : `JUR-T13` — réponse sans lien avec le cas.

---

### 1.2 Convention de trésorerie avec la société de tête (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | Intérêts sans centralisation (k€) : société de tête **− 108,0** ; Thermes Pyrénées **− 150,5** ; Thermes Savoie **− 113,0** ; Résidences **+ 2,5** ; total **− 369,0** | 0,75 |
| 1.2-02 | Solde net mensuel du groupe (− 12 ; − 14 ; − 11 ; − 9 ; − 7 ; − 3 ; 5 ; 11 ; 15 ; 15 ; 8 ; − 6) ; besoin de pointe du groupe **14 M€** (février) contre **27 M€** pour la somme des pointes des entités, soit 13 M€ de moins (− 48,15 %) | 0,5 |
| 1.2-03 | Convention : ligne **− 186,0**, fonds monétaire **+ 108,0**, commission − 45,0, résultat financier **− 123,0 k€** ; gain **246,0 k€** | 0,75 |
| 1.2-04 | Taux internes : Thermes Pyrénées **− 64,5**, Thermes Savoie **− 44,0**, Résidences **+ 25,0**, société de tête **− 39,5** ; chaque entité y gagne (86,0 ; 69,0 ; 22,5 ; 68,5) | 0,5 |
| 1.2-05 | Apports (coût, pointe, visibilité, négociation) et exigences (prévisions, systèmes, taux internes de marché, autonomie et responsabilité des filiales, dépendance à un seul prêteur) | 0,5 |

**Sommes des soldes mensuels (M€ × mois) et intérêts sans centralisation (k€).** Avec un mois = 1/12 d'année, les intérêts d'une entité = (− somme des découverts × taux débiteur + somme des excédents × taux créditeur) / 12.

| Entité | Somme des découverts | Somme des excédents | Intérêts débiteurs | Intérêts créditeurs | Intérêts nets | Besoin de pointe |
|---|---:|---:|---:|---:|---:|---:|
| Société de tête | 27 | 0 | 27 × 4,80 % / 12 = − 108,0 | 0 | **− 108,0** | 3 (avril à juin) |
| Thermes Pyrénées | 43 | 43 | − 193,5 | + 43,0 | **− 150,5** | 12 (février) |
| Thermes Savoie | 28 | 27 | − 140,0 | + 27,0 | **− 113,0** | 8 (février) |
| Résidences | 10 | 30 | − 42,5 | + 45,0 | **+ 2,5** | 4 (novembre) |
| **Total** | | | | | **− 369,0** | **27** |

**Solde net du groupe (M€).**

| | janv. | févr. | mars | avr. | mai | juin | juil. | août | sept. | oct. | nov. | déc. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Solde net | − 12 | − 14 | − 11 | − 9 | − 7 | − 3 | 5 | 11 | 15 | 15 | 8 | − 6 |

Somme des besoins : 62 ; somme des excédents : 54. Le besoin de pointe du groupe (14 M€ en février) est inférieur de 13 M€ (48,15 %) à la somme des besoins de pointe des entités (27 M€) : les pointes ne tombent pas le même mois et les excédents d'hiver des résidences compensent une partie des découverts des thermes. Avec des comptes séparés, chaque entité doit négocier une autorisation de découvert à hauteur de sa propre pointe ; centralisée, la trésorerie n'a besoin que d'une ligne de 15 M€.

**Résultat financier de la convention (k€).**
- Ligne confirmée : − 62 × 3,60 % / 12 = **− 186,0** ;
- fonds monétaire : 54 × 2,40 % / 12 = **+ 108,0** ;
- intérêts nets : − 78,0 ; commission d'engagement : − 45,0 ; **résultat financier : − 123,0 k€**.
- **Gain = − 123,0 − (− 369,0) = 246,0 k€**, soit les deux tiers du coût actuel. Le gain vient de deux effets : les excédents d'une entité ne restent plus rémunérés à 1,20 % pendant qu'une autre paie 5,40 % ou 6,00 % sur son découvert, et le besoin net est financé à 3,60 % au lieu de 4,80 % à 6,00 %.

**Partage du gain par les taux internes (k€).**

| Entité | Sans centralisation | Avec la convention | Gain |
|---|---:|---:|---:|
| Thermes Pyrénées | − 150,5 | − 43 × 4,20 % / 12 + 43 × 2,40 % / 12 = **− 64,5** | 86,0 |
| Thermes Savoie | − 113,0 | − 98,0 + 54,0 = **− 44,0** | 69,0 |
| Résidences | + 2,5 | − 35,0 + 60,0 = **+ 25,0** | 22,5 |
| Société de tête (résultat de la convention − intérêts internes des filiales) | − 108,0 | − 123,0 − (− 83,5) = **− 39,5** | 68,5 |
| **Total** | **− 369,0** | **− 123,0** | **246,0** |

Les taux internes (4,20 % et 2,40 %) sont plus favorables que ceux des banques actuelles pour chaque filiale : toutes y gagnent, y compris les Résidences, prêteuses nettes, dont les excédents sont mieux rémunérés. La société de tête garde l'écart entre les taux internes et les conditions de marché, qui couvre son propre besoin et la commission de la ligne. Le choix des taux internes ne change pas le gain du groupe : il le répartit, ce qui compte pour l'appréciation de la performance de chaque filiale et pour l'adhésion de leurs dirigeants.

**Ce qu'apporte la centralisation et ce qu'elle exige (0,5 pt).**
- **Apports** : moins de frais financiers (246,0 k€) ; une ligne dimensionnée sur la pointe du groupe (14 M€) et non sur la somme des pointes (27 M€) ; une vision consolidée et quotidienne de la trésorerie ; un seul interlocuteur bancaire et un meilleur pouvoir de négociation ; la possibilité de placer des montants plus importants (question 1.3).
- **Exigences** : des prévisions fiables et transmises à temps par les filiales ; des outils de remontée automatique des soldes et de suivi des comptes courants ; des taux internes proches des conditions de marché et acceptés par les dirigeants des filiales, qui perdent la gestion autonome de leur trésorerie ; une ligne confirmée suffisante et durable, puisque toute la liquidité du groupe passe par la société de tête et par une seule banque ; la convention est un fait d'énoncé, analysée ici sous l'angle financier.

**Réponses tolérées** : intérêts calculés mois par mois puis additionnés (mêmes résultats) ; gain présenté avant commission (369,0 − 78,0 = 291,0 k€) s'il est signalé comme tel ; partage du gain non présenté pour la société de tête si les trois filiales sont traitées.

**Erreurs fréquentes**
- Appliquer les taux internes au solde net du groupe : ils s'appliquent aux soldes des filiales ; le groupe, lui, paie les conditions de la ligne et du fonds monétaire.
- Additionner les besoins de pointe de chaque mois (somme des soldes négatifs) au lieu de retenir le solde le plus négatif.
- Oublier la commission d'engagement, due que la ligne soit tirée ou non.

---

### 1.3 Ligne confirmée ou programme de titres, placement de l'excédent d'automne (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | Ligne seule : 186,0 + 45,0 = **231,0 k€** ; programme : titres 59 × 3,00 % / 12 = **147,5**, juin sur la ligne **9,0**, frais fixes 72,0, commission 45,0, soit **273,5 k€** ; surcoût du programme **42,5 k€** | 1 |
| 1.3-02 | Encours d'équilibre : 72 / 0,60 % = **12,00 M€** d'encours moyen annuel, contre **4,92 M€** prévus ; choix de la ligne et conditions dans lesquelles le programme deviendrait intéressant | 0,5 |
| 1.3-03 | Excédent d'août à novembre : noyau stable de **8 M€** sur quatre mois au compte à terme, le reste en fonds monétaire ; supplément **8,0 k€** ; fonds obligataire écarté (horizon, risque de perte, question 1.4) | 1 |

**Coût du financement du besoin net (k€).**

| | Ligne confirmée seule | Programme de titres |
|---|---:|---:|
| Intérêts des titres (janvier à mai et décembre : 12 + 14 + 11 + 9 + 7 + 6 = 59) | — | 59 × 3,00 % / 12 = 147,5 |
| Intérêts de la ligne | 62 × 3,60 % / 12 = 186,0 | juin : 3 × 3,60 % / 12 = 9,0 |
| Frais fixes du programme | — | 72,0 |
| Commission d'engagement | 45,0 | 45,0 |
| **Coût annuel** | **231,0** | **273,5** |

Le programme coûte 42,5 k€ de plus. L'écart de taux (0,60 point) ne rapporte que 59 × 0,60 % / 12 = 29,5 k€ pour 72 k€ de frais fixes, la commission de la ligne de secours restant due dans les deux cas. **Encours moyen d'équilibre** : 72 / 0,60 % = **12,00 M€** par an, contre 59 / 12 = **4,92 M€** prévus : il faudrait un encours presque permanent, proche du plafond de 15 M€, pour que le programme soit moins cher. Les titres négociables à court terme conviennent à un besoin important et durable d'un émetteur connu des investisseurs, en pratique une grande entreprise notée (F07 § 4.2) : pour un groupe de 162 M€ de chiffre d'affaires, la notation à court terme est un coût fixe lourd (compris dans les 72 k€) ; ils exposent aussi au risque de ne pas pouvoir renouveler les émissions quand le marché se ferme, d'où la ligne de secours exigée. Le besoin d'ONDAVÈRE est modeste et saisonnier (six mois sur douze) : **la ligne confirmée est la solution la plus adaptée**. Le programme pourrait se justifier plus tard si le besoin moyen augmentait durablement, par exemple pour financer des investissements en attendant un financement à moyen terme (hors du champ de ce dossier).

**Placement de l'excédent d'août à novembre.** Les excédents nets sont de 11, 15, 15 et 8 M€ ; le besoin revient en décembre (− 6 M€). Le montant présent les quatre mois est donc de **8 M€** (novembre).

| Support | Horizon et liquidité | Rendement | Risque | Usage proposé |
|---|---|---:|---|---|
| Compte à terme (1er août – 30 novembre) | quatre mois, fonds bloqués | 2,70 % fixe | capital garanti ; défaillance de la banque | **noyau stable de 8 M€** (au-dessus du minimum de 5 M€) |
| Fonds monétaire | chaque jour | 2,40 %, variable | très faible | **le reste** : 5 M€ en juillet, 3 M€ en août, 7 M€ en septembre et en octobre, et toute somme à mobiliser rapidement |
| Fonds obligataire court terme | rachat sous trois jours | 3,10 % si les taux sont stables | sensibilité 1,80 : perte en capital possible | **écarté** : horizon de quatre mois trop court pour un support de sensibilité 1,80 |

Supplément du compte à terme : 8 × (2,70 % − 2,40 %) × 4 / 12 = **8,0 k€** (72,0 k€ au lieu de 64,0 k€). Le gain est faible, mais sans risque si les prévisions sont tenues ; placer plus de 8 M€ au compte à terme obligerait à le rompre en novembre et à perdre les intérêts. Le fonds obligataire rapporterait 8 × 0,70 % × 4 / 12 = 18,7 k€ de plus que le fonds monétaire, mais une hausse des taux de 0,13 point suffirait à l'effacer (question 1.4) : la trésorerie d'exploitation, qui doit financer l'hiver, ne doit pas porter de risque de perte en capital. Le compte à terme est ouvert à la Banque SÉRAVONNE, déjà prêteuse et contrepartie de l'option de la question 1.5 : le risque de contrepartie se concentre sur une seule banque.

**Réponses tolérées** : compte à terme limité à 5 M€ ou à un montant entre 5 et 8 M€ par prudence sur les prévisions (supplément calculé en cohérence) ; recours partiel au programme écarté pour les mêmes raisons ; encours d'équilibre exprimé en somme mensuelle (144 M€ × mois).

**Erreurs fréquentes**
- Oublier la commission de la ligne de secours dans le coût du programme, ou l'oublier pour la seule ligne.
- Comparer les taux (3,00 % et 3,60 %) sans tenir compte des frais fixes.
- Placer tout l'excédent de septembre (15 M€) au compte à terme, alors qu'il n'en reste que 8 M€ en novembre et que le besoin reprend en décembre.
- Retenir le fonds obligataire pour son rendement sans parler de sa sensibilité : `JUR-T13`.

---

### 1.4 Exposition du groupe au risque de taux (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Hausse d'un point : ligne 62 × 1 % / 12 = **+ 51,7 k€** de charges ; fonds monétaire 54 × 1 % / 12 = **+ 45,0 k€** de produits ; effet net **− 6,7 k€** (résultat financier − 129,7 k€ au lieu de − 123,0 k€) | 0,5 |
| 1.4-02 | Fonds obligataire : − 1,80 × 1 % × 8 M€ = **− 144,0 k€** ; supplément sur quatre mois **18,7 k€**, effacé par une hausse de **0,13 point** | 0,5 |
| 1.4-03 | Exposition : risque sur les flux (ligne et placements à taux variable) qui se compense presque, risque sur la valeur (titre à taux fixe), relation inverse valeur-taux ; taux internes fixes portés par la société de tête ; recommandation | 0,5 |

**Effet d'une hausse d'un point des taux courts.**
- Les tirages de la ligne passent à 4,60 % : 62 × 1 % / 12 = **51,7 k€** de charges en plus ;
- le fonds monétaire rapporte 3,40 % : 54 × 1 % / 12 = **45,0 k€** de produits en plus ;
- intérêts nets : − 84,7 k€ au lieu de − 78,0 k€ ; **effet net − 6,7 k€** ; résultat financier de la convention − 129,7 k€.

Le groupe emprunte l'hiver et place l'automne à taux variable : ses positions empruntrices et prêteuses se compensent presque (62 contre 54 M€ × mois). L'exposition nette porte sur 8 M€ × mois, soit un encours moyen de 0,67 M€ : le risque de taux de la trésorerie à court terme est faible. Pour la ligne seule, sans placement, la hausse coûterait 51,7 k€ (282,7 k€ au lieu de 231,0 k€).

**Fonds obligataire court terme.** La valeur d'un titre à taux fixe baisse quand les taux montent (relation inverse valeur-taux). Variation de valeur ≈ − sensibilité × variation des taux × montant = − 1,80 × 1 % × 8 M€ = **− 144,0 k€**, soit près de huit fois (7,71 fois) le supplément de rendement attendu sur quatre mois (18,7 k€). Hausse qui efface ce supplément : 18,7 / (1,80 × 8 000) = **0,13 point**. La sensibilité mesure la variation relative de valeur pour une variation d'un point du taux ; elle découle de la duration (durée de vie moyenne des flux actualisés) : un fonds de sensibilité 1,80 convient à un horizon proche de deux ans, pas à quatre mois.

**Conclusion.** La trésorerie à court terme expose surtout les **flux** (intérêts de la ligne et produits des placements à taux variable), et cette exposition se compense presque grâce aux saisons opposées. Un placement à taux fixe et de sensibilité élevée créerait au contraire un risque sur la **valeur** sans rapport avec l'horizon des excédents. Deux points restent à traiter : les taux internes, fixés pour 2027, laissent la société de tête porter seule la hausse des taux du marché (il est préférable de les indexer sur l'Euribor 3 mois) ; la dette à moyen et long terme du groupe (71,80 M€ de dette financière nette au 31/12/2026) n'est pas décrite dans le dossier et devrait être analysée de la même façon (part à taux fixe et à taux variable). Une couverture de la ligne n'est pas nécessaire à ce stade.

**Réponses tolérées** : effet de la hausse calculé avec la répartition retenue à la question 1.3, s'il est signalé comme tel (par exemple 8 M€ au compte à terme à taux fixe : produits + 45,0 − 8 × 1 % × 4 / 12 = + 18,3 k€, effet net − 33,3 k€ ; le compte à terme réduit alors la compensation naturelle) ; effet de la hausse calculé sans centralisation (sur les découverts de chaque entité), s'il est présenté en complément ; variation de valeur exprimée en pourcentage (− 1,80 %).

**Erreurs fréquentes**
- Appliquer la hausse au seul coût de la ligne, sans voir que les placements en profitent.
- Présenter la hausse des taux comme favorable au détenteur d'obligations à taux fixe.
- Confondre sensibilité et rendement, ou multiplier la sensibilité par le rendement.

---

### 1.5 Option d'achat sur l'indice de chaleur et assurance paramétrique (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | Étés 2017 à 2026 : indemnités de l'option (2019 : 0,75 ; 2022 : 1,50 ; 2023 : 0,25 ; 2025 : 1,75 ; 2026 : 2,50) et de l'assurance (2019 : 0,30 ; 2022 : 1,20 ; 2025 : 1,50 ; 2026 : 2,40) ; moyennes sur dix ans **0,68** et **0,54 M€**, sur cinq ans **1,20** et **1,02 M€**, comparées aux primes de 0,70 et 0,75 M€ ; indice moyen passé de 6,0 à 12,4 jours | 0,5 |
| 1.5-02 | Pertes de marge A **0**, B **3,00**, C **6,00 M€** ; indemnités de l'option A **0**, B **2,00**, C **3,00** (plafond) ; de l'assurance A **0**, B **1,80**, C **4,50** (plafond) | 1 |
| 1.5-03 | Résultats des protections (option − 0,70 / + 1,30 / + 2,30 ; assurance − 0,75 / + 1,05 / + 3,75) et effets totaux sur le résultat avant impôt (sans protection 0 / − 3,00 / − 6,00 ; option **− 0,70 / − 1,70 / − 3,70** ; assurance **− 0,75 / − 1,95 / − 2,25**) | 0,75 |
| 1.5-04 | Comparaison : coût et point de déclenchement, plafond (atteint à 20 et 25 jours), protection selon le scénario, risque de base commun (Savoie, sensibilité estimée), contrepartie et concentration sur la Banque SÉRAVONNE, renouvellement de l'assurance, délai de paiement ; recommandation argumentée | 1,25 |
| 1.5-05 | Place dans la gestion du risque climatique : transfert d'un été, pas réduction du risque ; tendance de l'indice ; adaptation des stations (saisons, altitude, bâtiments, eau, énergie), rétention par la trésorerie | 0,5 |

**Étés passés (M€).**

| Été | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 | Moyenne 10 ans | Moyenne 2022-2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Indice (jours) | 4 | 7 | 11 | 5 | 3 | 14 | 9 | 6 | 15 | 18 | 9,20 | 12,40 |
| Indemnité de l'option | 0 | 0 | 0,75 | 0 | 0 | 1,50 | 0,25 | 0 | 1,75 | 2,50 | **0,68** | **1,20** |
| Indemnité de l'assurance | 0 | 0 | 0,30 | 0 | 0 | 1,20 | 0 | 0 | 1,50 | 2,40 | **0,54** | **1,02** |
| *Perte de marge (pour mémoire)* | *0* | *0,30* | *1,50* | *0* | *0* | *2,40* | *0,90* | *0* | *2,70* | *3,60* | *1,14* | *1,92* |

La prime de l'option (0,70) est voisine de l'indemnité moyenne des dix derniers étés (0,675) ; celle de l'assurance (0,75) la dépasse de près de 40 %, ce qui reflète le chargement de l'assureur et sa prudence. Mais l'indice a doublé entre 2017-2021 (6,0 jours en moyenne) et 2022-2026 (12,4 jours) : sur les cinq derniers étés, les deux protections auraient versé plus que leur prime (1,20 et 1,02 M€). Si la tendance se poursuit, les primes paraissent peu élevées en 2027, mais elles seront revues à la hausse : l'assureur l'annonce, et la banque fera de même au renouvellement. La moyenne du passé sous-estime un risque qui s'aggrave.

**Été 2027 : trois scénarios (M€).**

| | A – 6 jours | B – 16 jours | C – 26 jours |
|---|---:|---:|---:|
| Perte de marge : 0,30 × max (0 ; indice − 6) | 0 | 3,00 | 6,00 |
| Indemnité de l'option : min [3,00 ; 0,25 × max (0 ; indice − 8)] | 0 | 2,00 | 4,50 → **3,00** |
| Résultat de l'option (indemnité − 0,70) | − 0,70 | + 1,30 | + 2,30 |
| **Effet total avec l'option** | **− 0,70** | **− 1,70** | **− 3,70** |
| Indemnité de l'assurance : min [4,50 ; 0,30 × max (0 ; indice − 10)] | 0 | 1,80 | 4,80 → **4,50** |
| Résultat de l'assurance (indemnité − 0,75) | − 0,75 | + 1,05 | + 3,75 |
| **Effet total avec l'assurance** | **− 0,75** | **− 1,95** | **− 2,25** |
| *Pour mémoire : avec les deux protections* | *− 1,45* | *− 0,65* | *+ 0,05* |

Pour éclairer la comparaison, taux de compensation (résultat de la protection / perte ; non exigé) : B, option 43,33 %, assurance 35,00 % ; C, option 38,33 %, assurance 62,50 %. Le plafond de l'option est atteint dès 20 jours (8 + 3,00 / 0,25), celui de l'assurance à 25 jours (10 + 4,50 / 0,30). Dans le scénario C, la perte de 6,00 M€ représente 17,34 % de l'EBITDA de 2026 ; celle de 2026 (3,60 M€) en représentait déjà 10,40 %.

**Comparaison des deux protections (1,25 pt).**
- **Coût et déclenchement.** L'option coûte un peu moins (0,70 contre 0,75 M€) et se déclenche plus tôt (8 jours contre 10), mais ne compense que 0,25 M€ par jour, soit 83 % de la perte d'un jour (0,30 M€) ; l'assurance compense toute la perte d'un jour au-delà de sa franchise. L'option protège mieux un été chaud (B : − 1,70 contre − 1,95), l'assurance une canicule longue (C : − 2,25 contre − 3,70).
- **Plafond.** Le plafond de l'option (3,00 M€, atteint à 20 jours) laisse au groupe toute la perte au-delà, alors que l'été 2026 a déjà compté 18 jours. L'assurance protège jusqu'à 25 jours (4,50 M€) : elle traite mieux la queue du risque, la plus dangereuse pour la trésorerie et pour les prêteurs.
- **Risque de base.** Les deux contrats reposent sur le même indice : leur risque de base est le même. La station de Varagnol, en plaine pyrénéenne, ne mesure pas la chaleur des stations de Savoie (en 2023, des cures ont été annulées en Savoie avec un indice de 9 jours seulement) ; la sensibilité de 0,30 M€ par jour est une estimation moyenne, établie surtout sur les Pyrénées. En contrepartie, l'indice est objectif, publié vite et sans expertise : les deux contrats paient en septembre ou au début d'octobre, quand la trésorerie de fin de saison est en jeu.
- **Contrepartie.** L'option est un contrat de gré à gré avec la Banque SÉRAVONNE, qui serait aussi le prêteur de la ligne et la dépositaire du compte à terme : le groupe concentrerait ses risques sur un seul établissement. L'assurance diversifie la contrepartie (assureur soumis à un contrôle prudentiel), mais son prix et sa franchise seront revus chaque année : risque de renouvellement.
- **Recommandation.** Pour un groupe dont la trésorerie dépend des recettes d'été et dont l'indice s'aggrave, l'assurance paramétrique est préférable : elle protège mieux les étés extrêmes et diversifie les contreparties. L'option se défend si le groupe craint surtout les étés chauds fréquents ; le cumul des deux (1,45 M€ de primes) surcouvrirait le scénario C (+ 0,05) et coûterait cher les étés habituels.

**Place dans la gestion du risque climatique (0,5 pt).** La chaleur est un risque physique **chronique** (l'indice moyen a doublé) qui se manifeste par des épisodes **aigus**. Une protection financière transfère la perte d'un été ; elle ne réduit pas l'exposition et deviendra plus chère à mesure que le risque s'aggrave (F07 § 5). Elle se combine avec :
- l'**adaptation** des stations : déplacer une partie des cures vers le printemps et l'automne (ouverture prolongée, offres incitatives), soins aux heures fraîches, ombrage et rafraîchissement des bâtiments et des résidences, développement des stations de Savoie, plus hautes, rénovation des établissements les plus exposés ; ces mesures ont un coût d'énergie et d'investissement (question 1.6) ;
- la **rétention** des pertes modérées : la ligne confirmée et la centralisation (question 1.2) absorbent un automne moins excédentaire ;
- le **transfert** des pertes graves : assurance ou option, choisies selon la perte que le groupe peut supporter.

**Réponses tolérées** : effet total présenté en valeur absolue (« coût de la canicule ») ; recommandation de l'option ou du cumul des deux, si elle est argumentée par le profil des étés et le coût ; indemnités moyennes arrondies à 0,67 ou 0,68 M€.

**Erreurs fréquentes**
- Oublier les plafonds dans le scénario C : retenir 4,50 M€ pour l'option au lieu de 3,00 M€, ou 4,80 M€ pour l'assurance au lieu de 4,50 M€.
- Calculer l'indemnité de l'assurance à partir du seuil de 6 jours de la perte de marge au lieu de la franchise de 10 jours.
- Déduire deux fois la prime, ou l'oublier dans l'effet total.
- Discuter le montant de la prime au lieu de l'utiliser : l'annexe la donne, à utiliser telle quelle (aucune valorisation d'option n'est attendue).
- Présenter la couverture comme une réduction du risque climatique : `JUR-T05` — performance durable absente du raisonnement.

---

### 1.6 Éléments extra-financiers du modèle d'affaires (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 1.6-01 | Éléments relevés et reliés au modèle d'affaires : ressource thermale, chaleur et curistes âgés, emplois saisonniers, énergie des bassins, gouvernance du risque (comité des risques, rémunération sans critère climatique) | 1 |
| 1.6-02 | Pourquoi ils comptent : pour les investisseurs (valeur et durabilité des flux, capital dispersé, information et asymétrie, agence) et pour les banques (capacité de remboursement, saisonnalité, valeur des stations, demande d'information de mars 2027) | 0,5 |

**Éléments liés au modèle d'affaires (1 pt).** Le modèle d'ONDAVÈRE repose sur une ressource naturelle localisée (l'eau thermale), sur des soins prescrits à une clientèle âgée pendant une saison, et sur des établissements à charges fixes élevées. Les informations extra-financières utiles au diagnostic sont donc :
- **la ressource thermale (environnement)** : sans eau en quantité et en qualité suffisantes, pas de soins. Le débit d'été d'Ussères a baissé de 12 % depuis 2020 et l'offre de soins y a été réduite de 8 % en août 2026 ; les prélèvements du groupe baissent (2,05 → 1,92 million de m³) ; deux fermetures de bassins pour qualité de l'eau. C'est un risque physique chronique, qui touche l'actif principal de la station la plus exposée à la chaleur ;
- **la chaleur et les curistes (social et environnement)** : 3 400 cures annulées ou reportées en 2026 (2 600 en 2025), dont 70 % dans les Pyrénées ; six curistes sur dix ont plus de 65 ans, donc une clientèle vulnérable aux épisodes de chaleur ; trois résidences sur cinq ne sont pas climatisées. Ces éléments expliquent la baisse de marge des Thermes Pyrénées (question 1.1) et la perte de marge de la question 1.5 ;
- **les emplois saisonniers (social)** : 430 salariés sur 1 250, soit 34,40 % ; 9 % des postes non pourvus au 1er juillet 2026 et 58 % de retour d'une saison sur l'autre ; logement rare en Savoie. Faute de personnel formé, le groupe ne peut pas ouvrir toute sa capacité : risque sur l'activité, la qualité des soins et les coûts ;
- **l'énergie des bassins (environnement)** : 41 GWh, dont 62 % de gaz naturel ; 7 900 t d'équivalent CO2 ; 4,90 M€ de coût, soit 3,02 % du chiffre d'affaires et 14,16 % de l'EBITDA de 2026. Risque de transition (prix du gaz et du carbone, attentes des financeurs) et levier : la chaleur récupérée sur l'eau d'Esquèdes (14 % des besoins) montre une piste de réduction ; la climatisation, réponse à la chaleur, augmenterait la consommation ;
- **la gouvernance du risque** : le comité des risques suit la chaleur et la ressource depuis 2025, mais la rémunération variable de la directrice générale ne comporte aucun critère climatique ou énergétique : l'incitation des dirigeants n'est pas alignée sur les risques principaux du modèle (théorie de l'agence, Jensen et Meckling, 1976).

**Pourquoi ils comptent pour les investisseurs et les banques (0,5 pt).**
- **Investisseurs** : la valeur de l'action dépend de la durabilité des flux des stations, donc de l'eau, de la chaleur et du personnel ; le capital est dispersé entre des institutionnels (61 %), qui n'ont pas accès à l'information de gestion et dont beaucoup appliquent des politiques d'investissement responsable : l'information extra-financière réduit l'asymétrie d'information et le risque perçu, donc la rentabilité exigée. Sans actionnaire de contrôle, la surveillance des dirigeants repose sur le conseil et sur cette information.
- **Banques** : la capacité de remboursement dépend des recettes d'été et de l'excédent d'automne (questions 1.2 et 1.5) ; une station dont la ressource s'épuise perd de sa valeur ; la Banque SÉRAVONNE demande, avant d'accorder la ligne, l'exposition de chaque station à la chaleur et à la baisse des débits, et les mesures d'adaptation.
- Dans une lecture partenariale (Freeman, 1984), curistes, saisonniers, communes thermales et financeurs sont des parties prenantes dont dépend la création de valeur : l'information extra-financière éclaire la performance durable, au-delà du seul EBITDA.

**Réponses tolérées** : classement des éléments par lettre E, S, G ; mention d'autres éléments de la présentation (actionnariat salarié de 6 %, administrateurs indépendants) s'ils sont reliés au modèle d'affaires ; intensité énergétique calculée par curiste (41 GWh / 71 000 ≈ 0,58 MWh).

**Erreurs fréquentes**
- Énumérer les données de l'annexe sans les relier au modèle d'affaires, à la performance ni aux risques : `JUR-T13`.
- Confondre la démarche RSE de l'entreprise et les critères ESG des investisseurs : `JUR-D01`.
- Oublier la gouvernance et ses théories : `JUR-D02`.
