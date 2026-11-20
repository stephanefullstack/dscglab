# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 3 – Contrôle de gestion et stratégie — Exercice d'entraînement n° 49 — Dossier 3 (6 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F05 pilotage des projets (§ 0, § 1, § 2, § 3, § 4, § 5, § 6, § 7), F11 pilotage stratégique de la durabilité (§ 0, § 1, § 3.1, § 4, § 6), F12 performance globale (§ 5), F13 registre des auteurs (toutes à jour au 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (réseau sans contrainte, planning retenu et variante écartée, budget du projet par semaine et budget cumulé de fin de trimestre, plan de financement présenté après financement relais, émissions par voyageur-kilomètre et indicateurs recalculés ; comparaison des deux ordres de l'équipe d'électriciens, fermeture des quais et scénarios de délai, budget par tâche et par trimestre, plan de financement avant financement relais et ses variantes, émissions par source : calculs divers recalculés par script ; barème partiel sur 6 ; liste noire ; hors-programme).

Bien que le corrigé mentionne des auteurs, des textes et des données, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur le choix et la justification des outils, la justesse des calculs, la pertinence de l'analyse au regard du cas et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet) ; pour chaque question, la présentation des concepts et outils avant leur mobilisation puis la conclusion sont notées. Une erreur n'est sanctionnée qu'une fois : les calculs et les analyses qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Réseau du projet à partir du descriptif (antériorité imposée par l'exploitation des quais), dates, marges, chemin critique ; conflit de l'équipe d'électriciens, choix de l'ordre, date de fin et marge avant le 31 août 2029, commentaire du planning | `2.2.b` Élaborer la planification du projet | 1,5 |
| 3.2 Budget du projet par trimestre et budget cumulé ; plan de financement trimestriel, point bas du solde cumulé et besoin de trésorerie | `2.2.a` Concevoir le plan de financement d'un projet | 1,5 |
| 3.3 Périmètre des émissions des services du dépôt et sélection des données ; émissions par voyageur-kilomètre en 2026 et en 2030, comparaison à l'objectif ; quatre ou cinq indicateurs de durabilité | `3.2.a` Sélectionner les données nécessaires au reporting en fonction du périmètre défini ; `3.2.c` Concevoir des indicateurs de durabilité pertinents | 1,5 |
| 3.4 Note au comité de pilotage (20 lignes au maximum) | `2.2.d` Analyser les résultats obtenus ; `2.2.e` Produire une synthèse rédigée et structurée concernant le pilotage du projet ; `3.2.c` Concevoir des indicateurs de durabilité pertinents | 1,5 |
| **Dossier 3 – Électrifier le dépôt de Lasvérac : planification, budget et plan de financement du projet, indicateurs de durabilité** | | **6** |

---

## DOSSIER 3 – ÉLECTRIFIER LE DÉPÔT DE LASVÉRAC : PLANIFICATION, BUDGET ET PLAN DE FINANCEMENT DU PROJET, INDICATEURS DE DURABILITÉ (6 points)

### 3.1 Établir le planning du projet et tenir compte de l'équipe d'électriciens (1,5 pt)

**Compétence visée :**
- `2.2.b` — Élaborer la planification du projet

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Réseau construit à partir du descriptif : B et C après A ; D après C ; F après E ; G après B ; H après D ; I après D, G et H ; J après I ; L après F, J et K ; K sans antériorité (semaines 1 à 68) ; antériorité d'exploitation **E après D**, déduite de la règle des quais (la tranche 2 ne peut fermer qu'à la réouverture de la tranche 1, à la fin de la pose de ses bornes) ; dates de début au plus tôt et au plus tard de chaque tâche | 0,5 |
| 3.1-02 | Marges totales (C, D, E et F : **14** ; H : **20** ; K : **8** ; A, B, G, I, J et L : 0) ; chemin critique **A-B-G-I-J-L** ; durée **80 semaines** (fin le vendredi 13 juillet 2029) ; lecture : le délai est dicté par le raccordement, réalisé par un tiers, puis par le poste ; les travaux des quais ont 14 semaines de marge et les autocars 8 | 0,5 |
| 3.1-03 | Équipe d'électriciens : D (semaines 25 à 36) ne gêne personne, mais **F (51 à 62) et G (55 à 66) se chevauchent 8 semaines** ; F après G : F commence à la date 66, décalée de 16 semaines pour 14 de marge, le projet s'allonge de **2 semaines** ; G après F : G, critique, est décalée de 8 semaines et le projet dure 88 semaines, au-delà de l'échéance ; planning retenu **F après G**, fin à la date **82** (vendredi 27 juillet 2029), **5 semaines de marge** avant le 31 août 2029 ; nouveau chemin critique A-B-G-F-L (l'équipe d'électriciens devient la ressource critique) ; commentaire : tranche 2 fermée 42 semaines (E au plus tard la ramènerait à 26 semaines sans allonger le projet), formation en mai et juin, marge faible au regard du risque sur le raccordement | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **réseau des antériorités** (méthode des potentiels), complété d'un **diagramme de Gantt** sur l'échelle des semaines. Le programme demande de construire ces diagrammes « à partir de données brutes (textes) » : il faut ici traduire en antériorités les tâches décrites, mais aussi une règle d'exploitation (les quais) qui n'est pas présentée comme une antériorité. Le réseau donne les dates, les marges et le chemin critique ; le Gantt fait voir les tâches qui se disputent la même équipe. La contrainte d'une ressource unique se traite ensuite par un **lissage** (ou nivellement) : on ordonne les tâches en conflit en décalant, de préférence, celle qui a de la marge.
- Alternatives acceptées : réseau en graphe potentiels-étapes (PERT) ; Gantt seul, si les dates au plus tard et les marges sont calculées ; numérotation des semaines de début (semaine 11 au lieu de la date 10), si la convention est dite et appliquée partout.

**Conventions rappelées** (annexe 3.5)

Date 0 = début de la semaine 1 (lundi 3 janvier 2028) ; une tâche commencée à la date t et de durée d occupe les semaines t + 1 à t + d ; date t = fin de la semaine t ; échéance : date 87 (vendredi 31 août 2029) ; marge totale = début au plus tard − début au plus tôt ; chemin critique = tâches de marge totale nulle ; une tâche commencée n'est pas interrompue ; planning retenu : chaque tâche au plus tôt après prise en compte de l'équipe d'électriciens.

**Calculs détaillés**

*Réseau sans contrainte d'électriciens* (semaines)

| Tâche | Durée | Antériorités | Début au plus tôt | Fin au plus tôt | Début au plus tard | Fin au plus tard | Marge totale |
|---|---:|---|---:|---:|---:|---:|---:|
| A Études et dossier technique | 10 | — | 0 | 10 | 0 | 10 | **0** |
| B Renforcement du raccordement | 44 | A | 10 | 54 | 10 | 54 | **0** |
| C Génie civil, tranche 1 | 14 | A | 10 | 24 | 24 | 38 | 14 |
| D Armoires et bornes, tranche 1 | 12 | C | 24 | 36 | 38 | 50 | 14 |
| E Génie civil, tranche 2 | 14 | D (règle des quais) | 36 | 50 | 50 | 64 | 14 |
| F Armoires et bornes, tranche 2 | 12 | E | 50 | 62 | 64 | 76 | 14 |
| G Poste et armoire générale | 12 | B | 54 | 66 | 54 | 66 | **0** |
| H Logiciel de pilotage | 10 | D | 36 | 46 | 56 | 66 | 20 |
| I Essais de la tranche 1 | 4 | D, G, H | 66 | 70 | 66 | 70 | **0** |
| J Formation | 6 | I | 70 | 76 | 70 | 76 | **0** |
| K Autocars (fabrication, livraison, réception) | 68 | — | 0 | 68 | 8 | 76 | 8 |
| L Essais de la tranche 2 et mise en service | 4 | F, J, K | 76 | 80 | 76 | 80 | **0** |

Durée : **80 semaines** ; chemin critique **A-B-G-I-J-L** (10 + 44 + 12 + 4 + 6 + 4 = 80). Les dates au plus tard se calculent à rebours depuis 80 : par exemple, F doit finir au plus tard au début au plus tard de L (76) ; D doit finir au plus tard à 50, plus petit début au plus tard de ses successeurs E (50) et H (56).

*Équipe d'électriciens* (dates au plus tôt du réseau sans contrainte)

| Tâche | Semaines occupées | Marge totale |
|---|---|---:|
| D Armoires et bornes, tranche 1 | 25 à 36 | 14 |
| F Armoires et bornes, tranche 2 | 51 à 62 | 14 |
| G Poste et armoire générale | 55 à 66 | 0 |

D ne chevauche ni F ni G. F et G se chevauchent de la semaine 55 à la semaine 62, soit **8 semaines**. Deux ordres sont possibles :

| Ordre | Tâche décalée | Nouveau début | Décalage | Marge totale | Allongement | Durée du projet | Fin du projet |
|---|---|---:|---:|---:|---:|---:|---|
| **G puis F** (retenu) | F | 66 | 16 | 14 | **+ 2** | **82** | vendredi 27 juillet 2029 |
| F puis G | G | 62 | 8 | 0 | + 8 | 88 | vendredi 7 septembre 2029 |

*Planning retenu* (G puis F, chaque tâche au plus tôt)

| Tâche | Semaines | Marge totale |
|---|---|---:|
| A | 1 à 10 | 0 |
| B | 11 à 54 (13 mars 2028 – 12 janvier 2029) | 0 |
| C | 11 à 24 | 16 |
| D | 25 à 36 | 16 |
| E | 37 à 50 | 16 |
| G | 55 à 66 (15 janvier – 6 avril 2029) | 0 |
| H | 37 à 46 | 22 |
| F | 67 à 78 (9 avril – 29 juin 2029) | 0 |
| I | 67 à 70 | 2 |
| J | 71 à 76 (7 mai – 15 juin 2029) | 2 |
| K | 1 à 68 (livraison le 6 avril 2029) | 10 |
| L | 79 à 82 (2 – 27 juillet 2029) | 0 |

Durée **82 semaines** ; chemin critique **A-B-G-F-L** (10 + 44 + 12 + 12 + 4 = 82), qui passe par le lien de ressource G → F ; marge avant l'échéance : 87 − 82 = **5 semaines**.

*Fermeture des quais.* Tranche 1 fermée des semaines 11 à 36 (26 semaines) ; tranche 2 fermée des semaines 37 à 78 (**42 semaines**), dont 16 semaines d'attente entre la fin de son génie civil (semaine 50) et le début de la pose de ses bornes (semaine 67). En décalant E au plus tard (semaines 53 à 66, marge de 16 entièrement consommée), la tranche 2 n'est plus fermée que 26 semaines, sans allonger le projet.

**Réponse attendue**

*Concepts.* Planifier un projet, c'est ordonner ses tâches dans le temps sous la contrainte du triptyque qualité, coût, délai. Le réseau des antériorités donne, pour chaque tâche, une date de début au plus tôt (calcul en avant) et au plus tard (calcul à rebours depuis la durée du projet) ; la marge totale mesure le retard qu'une tâche peut prendre sans retarder le projet ; les tâches sans marge forment le chemin critique, sur lequel tout retard se reporte sur la date de fin. Le planning au plus tôt suppose des ressources illimitées : quand une ressource unique est demandée par deux tâches simultanées, il faut les ordonner (lissage), en décalant de préférence la tâche qui a assez de marge.

*Application.* Le descriptif contient une antériorité qui n'est pas écrite comme telle : puisque la moitié des quais au plus peut être fermée et que les quais d'une tranche restent fermés jusqu'à la fin de la pose de ses bornes, la tranche 2 ne peut ouvrir son chantier qu'à la fin de D. Sans autre contrainte, le projet dure 80 semaines et son chemin critique passe par le raccordement, réalisé par le gestionnaire du réseau, puis par le poste, les essais de la tranche 1 et la formation : CAZALVÈRE ne maîtrise pas la tâche la plus longue (44 semaines). L'équipe d'électriciens est demandée en même temps par F et par G pendant 8 semaines. Décaler G, tâche critique, retarderait le projet de 8 semaines et ferait manquer l'échéance (date 88). Décaler F, qui a 14 semaines de marge, ne coûte que 2 semaines, parce que F doit attendre la fin de G (date 66), soit 16 semaines après sa date au plus tôt : la solution retenue fait finir le projet le vendredi 27 juillet 2029, avec 5 semaines de marge. L'équipe d'électriciens devient critique : tout retard du raccordement se reporte sur le poste, puis sur la tranche 2. Le planning retenu a deux défauts. La tranche 2 reste fermée 42 semaines, alors que le chef du dépôt demande des fermetures courtes ; repousser E au plus tard ramènerait la fermeture à 26 semaines sans allonger le projet, mais E perdrait sa marge de 16 semaines. La formation tombe en mai et juin 2029, juste avant l'été, comme le redoute le conducteur.

**Conclusion** : le dépôt peut être en service le 27 juillet 2029, avec 5 semaines de marge seulement, alors que le gestionnaire du réseau annonce un risque de 4 à 8 semaines de retard sur une tâche critique : un retard de 4 semaines laisse 1 semaine de marge, un retard de 8 semaines fait finir le projet le 21 septembre 2029, après la rentrée. La date du raccordement est le premier point à suivre en revue d'avancement.

**Réponses tolérées**
- E au plus tard proposé dans le commentaire pour réduire la fermeture de la tranche 2, si le candidat le justifie ; la date de fin (82) est inchangée, E perd sa marge ; le planning de référence, qui sert au budget de la question 3.2, reste au plus tôt (annexe 3.5).
- Planning présenté en semaines de début et de fin (semaines 1 à 10, 11 à 54…) plutôt qu'en dates, si la convention est appliquée de façon cohérente.
- Comparaison des deux ordres par leur durée seulement (82 contre 88), sans détailler le décalage et la marge, si le choix est justifié.

**Erreurs fréquentes**
- `JUR-P02` — Ne pas appliquer la règle d'exploitation des quais : E placé après C (ou après A), ce qui fait fermer les deux tranches en même temps.
- `JUR-T07` — Résoudre le conflit en décalant la tâche critique, ou conclure que F « a 14 semaines de marge » sans voir qu'elle doit être décalée de 16.
- `JUR-T03` — Donner les dates sans lire le chemin critique, sans dire qui maîtrise les tâches critiques ni quelle marge reste avant l'échéance.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 791-792 : diagrammes « à partir de données brutes (textes) » ; l. 799-801 : Gantt, tâches, durées, marges, jalons, ressources, chemin critique) | réseau, Gantt, marges, chemin critique | [V] | F05 § 0, § 4 |
| Triptyque qualité, coût, délai (programme l. 795) | arbitrage du planning | [V] | F05 § 2 |
| Dates au plus tôt et au plus tard, marge totale | calcul du réseau | [S] | F05 § 1, § 4 |
| Ressources du projet (programme l. 799-801) ; lissage d'une ressource unique | ordonnancement sous contrainte | [V] programme ; [S] lissage | F05 § 0 (ligne 2.2.b) |

---

### 3.2 Établir le budget du projet et son plan de financement (1,5 pt)

**Compétence visée :**
- `2.2.a` — Concevoir le plan de financement d'un projet

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Coût de chaque tâche tiré des ressources (A 1 500 h × 80 € = **120** ; B **880** ; C et E 26 × 7 + 28 = **210** ; D et F 12 × 40 + 2 × 60 = **600** ; G 280 + 80 = **360** ; H 400 h × 150 € + 20 = **80** ; I **40** ; J 60 × 10 h × 45 € + 8 × 75 h × 55 € = 27 + 33 = **60** ; L **60** ; autocars 24 × 470 = **11 280**, acompte **1 128** la semaine 1, solde **10 152** la semaine 66) ; budget par trimestre sur le planning retenu : **1 353 ; 525 ; 829 ; 481 ; 370 ; 10 882 ; 60** k€ ; budget total **14 500 k€** | 0,5 |
| 3.2-02 | Budget cumulé de fin de trimestre (1 353 ; 1 878 ; 2 707 ; 3 188 ; 3 558 ; 14 440 ; 14 500) et en pourcentage (9,33 % ; 12,95 % ; 18,67 % ; 21,99 % ; **24,54 %** ; **99,59 %** ; 100 %) ; commentaire : la courbe n'a pas la forme en S d'un chantier, elle fait une marche au T2 2029 (75,05 % du budget, solde des autocars) ; les autocars font 77,79 % du budget ; hors autocars, les travaux suivent une courbe en S à deux paliers (49,04 % fin septembre 2028, seconde hausse au T2 2029) et le lissage reporte les 600 k€ des bornes de la tranche 2 au T2 2029 | 0,5 |
| 3.2-03 | Plan de financement : ressources (2 960 ; 400 ; 400 ; 400 ; 400 ; 8 400 ; 1 760, soit 14 720), emplois, soldes (1 607 ; − 125 ; − 429 ; − 81 ; 30 ; − 2 482 ; 1 700) et solde cumulé (1 607 ; 1 482 ; 1 053 ; 972 ; 1 002 ; **− 1 480** ; 220) ; point bas au **T2 2029** : **besoin de trésorerie de 1 480 k€** pendant un trimestre, parce que le solde des autocars (10 152) dépasse l'emprunt débloqué à la livraison (8 000) et que l'aide et la reprise ne viennent qu'à la mise en service (les mesures de couverture sont notées en 3.4) | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **budget du projet** (le programme parle de « plan de financement (budget) du projet ») établi sur le planning retenu, par tâche et par trimestre, puis son cumul, qui forme la courbe du budget du projet servant de référence aux revues d'avancement ; ensuite, le **plan de financement** trimestriel, qui confronte ces emplois aux ressources prévues et fait apparaître, par le solde cumulé, le moment où le projet manque de trésorerie.
- Alternatives acceptées : budget hebdomadaire regroupé ensuite par trimestre ; présentation des travaux et des autocars sur deux lignes distinctes ; plan de financement présenté directement avec une ligne de financement relais au T2 2029, si le besoin de 1 480 k€ est identifié. Non accepté : un budget obtenu en divisant 14 500 k€ par sept trimestres, ou un plan de financement qui compte les ressources à une autre date que celle de leur versement.

**Conventions rappelées** (annexes 3.2 et 3.5)

Trimestres de 13 semaines (T1 2028 = semaines 1 à 13 … T3 2029 = semaines 79 à 91) ; coût d'une tâche = somme de ses ressources, réparti uniformément sur ses semaines ; autocars : 10 % la semaine 1, solde la semaine 66 ; emplois = budget du trimestre ; ressources au trimestre de leur versement ; solde cumulé depuis 0 ; k€ sans décimale.

**Calculs détaillés**

*Budget du projet par tâche et par trimestre* (k€ ; coût hebdomadaire × semaines de la tâche dans le trimestre)

| Tâche (coût hebdomadaire) | T1 2028 | T2 2028 | T3 2028 | T4 2028 | T1 2029 | T2 2029 | T3 2029 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A (12 ; semaines 1 à 10) | 120 | | | | | | | 120 |
| B (20 ; 11 à 54) | 60 | 260 | 260 | 260 | 40 | | | 880 |
| C (15 ; 11 à 24) | 45 | 165 | | | | | | 210 |
| D (50 ; 25 à 36) | | 100 | 500 | | | | | 600 |
| E (15 ; 37 à 50) | | | 45 | 165 | | | | 210 |
| F (50 ; 67 à 78) | | | | | | 600 | | 600 |
| G (30 ; 55 à 66) | | | | | 330 | 30 | | 360 |
| H (8 ; 37 à 46) | | | 24 | 56 | | | | 80 |
| I (10 ; 67 à 70) | | | | | | 40 | | 40 |
| J (10 ; 71 à 76) | | | | | | 60 | | 60 |
| L (15 ; 79 à 82) | | | | | | | 60 | 60 |
| **Travaux et prestations** | 225 | 525 | 829 | 481 | 370 | 730 | 60 | **3 220** |
| K Autocars (acompte, solde) | 1 128 | | | | | 10 152 | | 11 280 |
| **Budget du trimestre** | **1 353** | **525** | **829** | **481** | **370** | **10 882** | **60** | **14 500** |
| Budget cumulé | 1 353 | 1 878 | 2 707 | 3 188 | 3 558 | 14 440 | 14 500 | |
| Budget cumulé en % | 9,33 % | 12,95 % | 18,67 % | 21,99 % | 24,54 % | 99,59 % | 100 % | |
| Travaux seuls, cumul en % | 6,99 % | 23,29 % | 49,04 % | 63,98 % | 75,47 % | 98,14 % | 100 % | |

Sans la contrainte d'électriciens (F en semaines 51 à 62, L en 77 à 80), le budget aurait été de 1 353 ; 525 ; 829 ; 581 ; 870 ; 10 312 ; 30 : le lissage reporte 600 k€ de bornes au T2 2029.

*Plan de financement trimestriel* (k€)

| | T1 2028 | T2 2028 | T3 2028 | T4 2028 | T1 2029 | T2 2029 | T3 2029 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Autofinancement | 400 | 400 | 400 | 400 | 400 | 400 | 400 | 2 800 |
| Aide de la région (60 % semaine 11, 40 % fin de L) | 960 | | | | | | 640 | 1 600 |
| Emprunt bancaire | 1 600 | | | | | 8 000 | | 9 600 |
| Reprise des 24 autocars au gazole (24 × 30) | | | | | | | 720 | 720 |
| **Total des ressources** | **2 960** | **400** | **400** | **400** | **400** | **8 400** | **1 760** | **14 720** |
| Travaux et prestations | 225 | 525 | 829 | 481 | 370 | 730 | 60 | 3 220 |
| Autocars électriques | 1 128 | | | | | 10 152 | | 11 280 |
| **Total des emplois** | **1 353** | **525** | **829** | **481** | **370** | **10 882** | **60** | **14 500** |
| Solde du trimestre | 1 607 | − 125 | − 429 | − 81 | 30 | − 2 482 | 1 700 | 220 |
| **Solde cumulé** | 1 607 | 1 482 | 1 053 | 972 | 1 002 | **− 1 480** | 220 | |

Si le besoin du T2 2029 est couvert par un financement relais de 1 480 k€ remboursé au T3 2029, le solde cumulé devient 1 607 ; 1 482 ; 1 053 ; 972 ; 1 002 ; 0 ; 220.

*Variantes du point bas (T2 2029).* Reprise des autocars au gazole à la livraison des électriques : − 1 480 + 720 = **− 760** ; versement de la seconde part de l'aide à la livraison : − 1 480 + 640 = − 840 ; les deux : **− 120**.

**Réponse attendue**

*Concepts.* Le budget d'un projet traduit le planning en coûts : chaque tâche reçoit un coût, calculé à partir de ses ressources, réparti sur ses périodes selon une règle connue ; son cumul de fin de période forme la courbe du budget (courbe en S), qui servira de référence aux revues d'avancement. Le plan de financement confronte, période par période, ces emplois aux ressources prévues (autofinancement, aide, emprunt, cessions) ; le solde cumulé doit rester positif, sinon le projet fait naître un besoin de trésorerie qu'il faut couvrir.

*Application.* Le projet coûte 14 500 k€, dont 11 280 k€ d'autocars (77,79 %) et 3 220 k€ de travaux et de prestations. Le budget cumulé n'a pas la forme en S d'un chantier : un quart du budget seulement (24,54 %) est consommé avant la livraison, puis le solde des autocars fait passer le cumul à 99,59 % au T2 2029. Hors autocars, les travaux suivent une courbe en S à deux paliers : un pic au T3 2028 (bornes de la tranche 1), puis une seconde hausse au T2 2029, due au report des bornes de la tranche 2. Le lissage de la question 3.1 déplace 600 k€ de bornes vers le T2 2029, trimestre déjà le plus lourd. Jusqu'à la livraison, les ressources (4 560 k€) couvrent les emplois (3 558 k€). Au T2 2029, l'emprunt débloqué à la livraison (8 000 k€) ne couvre pas le solde des autocars (10 152 k€), et la seconde part de l'aide (640 k€) comme la reprise des autocars au gazole (720 k€) n'arrivent qu'à la mise en service, au T3 2029 : le solde cumulé tombe à − 1 480 k€. Ce besoin dure un trimestre, puisque le plan finit à + 220 k€.

**Conclusion** : le projet est financé sur sa durée (14 720 k€ de ressources pour 14 500 k€ d'emplois), mais il fait naître un besoin de trésorerie de 1 480 k€ au T2 2029, que M. PEYRANNE doit couvrir avant la livraison. Le plus simple est de caler les ressources sur la livraison : faire payer la reprise des autocars au gazole à la livraison des électriques ramène le besoin à 760 k€, et obtenir aussi la seconde part de l'aide à la réception des autocars le ramène à 120 k€. À défaut, il faudra un financement relais sur un trimestre.

**Réponses tolérées**
- Budget du T1 2028 présenté sans l'acompte des autocars, porté sur une ligne d'emplois distincte, si le total des emplois est juste.
- Pourcentages cumulés calculés sur les seuls travaux, si le candidat le dit et commente la marche du T2 2029.
- Besoin de trésorerie mesuré par le solde du trimestre le plus négatif (− 2 482 au T2 2029) plutôt que par le solde cumulé, si le candidat montre ensuite que l'excédent des trimestres antérieurs en couvre une partie (besoin net de 1 480).

**Erreurs fréquentes**
- `JUR-P02` — Ne pas appliquer la règle de répartition : coût de B étalé sur les trimestres au lieu des semaines, autocars répartis sur toute la durée de K.
- `JUR-T03` — Présenter le plan sans repérer le point bas ni dire comment le couvrir.
- `JUR-T05` — Établir le budget sur le planning au plus tôt sans contrainte, alors que la question demande le planning retenu à la question 3.1.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 791-794 : « plan de financement (budget) du projet », revues d'avancement) ; guide p. 121 | budget du projet par tâche et par période | [V] | F05 § 0, § 3 |
| Courbe en S du budget cumulé (guide p. 121) | budget de référence | [V] | F05 § 5 |
| Plan de financement : emplois, ressources, trésorerie cumulée jamais négative sans financement relais | point bas et besoin | [S] | F05 § 1, § 3 |

---

### 3.3 Délimiter le périmètre, mesurer les émissions et proposer des indicateurs de durabilité (1,5 pt)

**Compétences visées :**
- `3.2.a` — Sélectionner les données nécessaires au reporting en fonction du périmètre défini
- `3.2.c` — Concevoir des indicateurs de durabilité pertinents

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Périmètre justifié : les **services du dépôt**, c'est-à-dire les autocars du dépôt (gazole et électricité de recharge) **et les services affrétés**, qui rendent le même service sous les mêmes contrats et que la région comptera ; énergies prises **amont compris** (facteurs fournis), pour comparer équitablement gazole et électricité ; données écartées et pourquoi : déplacements domicile-travail et locaux (sans lien avec l'électrification, à suivre ailleurs), fabrication des batteries (amont de la chaîne de valeur, émission ponctuelle : information complémentaire), disponibilité et écoconduite (données d'indicateurs, pas d'émissions) | 0,5 |
| 3.3-02 | Émissions : 2026 : 900 000 × 3,00 = 2 700 t + 100 000 × 1,20 = 120 t, soit **2 820 t** pour 51 800 000 voyageurs-km, **54,44 g** ; 2030 : 1 326 t + 1 440 000 × 0,05 = 72 t + 360 t, soit **1 758 t** pour 55 400 000 voyageurs-km, **31,73 g** (− 41,71 %) ; objectif de 30 g **non atteint** (+ 1,73 g) ; sur les seuls autocars du dépôt, 27,96 g (− 48,22 %) : l'affrètement, triplé, absorbe une partie du gain (360 t, 20,48 % des émissions de 2030) | 0,5 |
| 3.3-03 | Quatre ou cinq indicateurs reliés à la stratégie et aux attentes de la région, chacun avec formule, cible, sens, périodicité et, si possible, valeur prévue : émissions par voyageur-km (31,73 g pour 30), part des kilomètres en électrique (**42,86 %** pour 40 %), part des kilomètres affrétés (**10,71 %** en 2030 contre 3,85 % en 2026), disponibilité des autocars électriques (94,00 % à Vaulmérac pour 95 %), consommation aux 100 km (36,00 → 34,00 L ; 120,00 kWh) ou part des conducteurs formés à l'écoconduite (30,00 %) ; lecture des cibles non atteintes | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : la **délimitation du périmètre** du reporting (quelles activités, quelles sources, quelle partie de la chaîne de valeur), puis le calcul des émissions par la règle « donnée d'activité × facteur d'émission fourni », rapportées au service rendu (voyageur-kilomètre). Le périmètre suit la question posée : mesurer l'effet de l'électrification sur les services que la région attribue au dépôt. Viennent ensuite quelques **indicateurs de durabilité** déduits de la stratégie (renouveler les lots grâce à un parc moins émetteur) et des facteurs clés de succès de l'électrification (disponibilité des autocars, conduite adaptée, maîtrise de l'affrètement), chacun avec sa formule, sa cible et sa périodicité.
- Alternatives acceptées : intensité exprimée en kg CO2e par kilomètre de service (1,08 kg en 2026, 0,63 kg en 2030) en complément ; périmètre élargi aux batteries, présenté en sensibilité (120 t par an, 33,90 g par voyageur-km en 2030) ; présentation en émissions directes (gazole) et indirectes (électricité, affrètement), sans bilan complet. Non accepté : un périmètre limité aux autocars du dépôt présenté comme mesure de l'effet de l'électrification, sans évoquer l'affrètement ; une liste d'indicateurs sans formule ni cible.

**Conventions rappelées** (annexes 3.3 et 3.5)

Émissions (t CO2e) = donnée d'activité × facteur / 1 000 ; gazole 3,00 kg par litre, électricité 0,05 kg par kWh, affrètement 1,20 kg par kilomètre (valeurs pédagogiques, amont compris) ; g CO2e par voyageur-kilomètre = t × 1 000 000 / voyageurs-km ; indicateur = numérateur / dénominateur (× 100) ; cible et sens ; deux décimales.

**Calculs détaillés**

*Sélection des données*

| Donnée de l'annexe 3.3 | Retenue ? | Justification |
|---|---|---|
| Gazole et électricité de recharge des autocars du dépôt | oui | activités propres, directement modifiées par l'électrification |
| Kilomètres et voyageurs-km des services affrétés | oui | même service, sous les mêmes contrats ; la région les comptera ; les exclure flatterait l'indicateur à mesure que l'affrètement croît |
| Voyageurs-km des autocars du dépôt | oui | dénominateur du service rendu |
| Kilomètres par énergie | oui, pour les indicateurs | part de l'électrique, consommations |
| Fabrication des batteries | non (information complémentaire) | amont de la chaîne de valeur, émise une fois ; utile pour juger l'électrification sur la durée de vie, pas pour piloter l'exploitation |
| Domicile-travail (220 t), locaux (150 t) | non | sans lien avec l'électrification ; à suivre dans d'autres indicateurs |
| Disponibilité des autocars de Vaulmérac, écoconduite | non pour les émissions ; oui pour les indicateurs | facteurs de réussite de l'électrification |

*Émissions des services du dépôt* (t CO2e)

| Source | 2026 | 2030 (prévision) |
|---|---:|---:|
| Gazole des autocars du dépôt (litres × 3,00) | 2 700 | 1 326 |
| Électricité de recharge (kWh × 0,05) | 0 | 72 |
| Services affrétés (km × 1,20) | 120 | 360 |
| **Total** | **2 820** | **1 758** |
| Voyageurs-kilomètres (dépôt + affrétés) | 51 800 000 | 55 400 000 |
| **g CO2e par voyageur-kilomètre** | **54,44** | **31,73** |
| Autocars du dépôt seuls (g CO2e par voyageur-km) | 54,00 | 27,96 |

Variation 2030 / 2026 : émissions − 37,66 % ; par voyageur-km − 41,71 % (autocars du dépôt seuls : − 48,22 %). Objectif de la direction : 30 g, dépassé de 1,73 g.

*Indicateurs proposés* (exemple ; valeurs prévues en 2030 quand l'annexe le permet)

| Indicateur | Formule | Cible et sens | Périodicité | Valeur |
|---|---|---|---|---|
| Émissions par voyageur-km des services du dépôt | (litres × 3,00 + kWh × 0,05 + km affrétés × 1,20) en g / voyageurs-km, affrètement compris | 30 g au plus en 2030 (baisse) | trimestrielle (suivi demandé par la région) | 54,44 g en 2026 ; 31,73 g en 2030 : non atteinte |
| Part des kilomètres parcourus en électrique | km électriques / km de tous les services du dépôt × 100 | 40 % au moins (hausse) | mensuelle | 42,86 % en 2030 : atteinte |
| Part des kilomètres affrétés | km affrétés / km de tous les services du dépôt × 100 | 4 % au plus (baisse), niveau de 2026 | mensuelle | 3,85 % en 2026 ; 10,71 % en 2030 : non atteinte |
| Disponibilité des autocars électriques | journées disponibles / journées d'exploitation prévues × 100 | 95 % au moins (hausse) | mensuelle | 94,00 % à Vaulmérac en 2026 : non atteinte |
| Part des conducteurs formés à l'écoconduite et à la conduite électrique | conducteurs formés / conducteurs du dépôt × 100 | 100 % avant la rentrée 2029 (hausse) | trimestrielle | 30,00 % en 2027 |

Autres indicateurs acceptés : consommation aux 100 km (gazole : 36,00 L en 2026, 34,00 L prévus en 2030 ; électrique : 120,00 kWh prévus) ; part des véhicules à faibles émissions de l'entreprise (3,70 % en 2027, 8,64 % à la rentrée 2029) ou affectés aux lots (46,15 % au dépôt de Lasvérac).

**Réponse attendue**

*Concepts.* Le reporting de durabilité commence par la délimitation du périmètre : l'entité et les activités retenues (périmètre organisationnel), puis les sources d'émissions et la part de la chaîne de valeur prises en compte (périmètre opérationnel). Le périmètre dépend de la question posée, et ne retient que les données qui y répondent. Les émissions se calculent ensuite comme le produit d'une donnée d'activité et d'un facteur d'émission fourni. Un indicateur de durabilité pertinent découle de la stratégie et d'un facteur clé de succès ; il a une formule, une cible et une périodicité, et ne se réduit pas à une liste.

*Application.* Pour mesurer l'effet de l'électrification, le périmètre utile est celui des services du dépôt : ses autocars, et les services qu'il confie à d'autres autocaristes, qui relèvent des mêmes lots et que la région comptera. Les facteurs d'émission « amont compris » permettent de comparer le gazole et l'électricité. La fabrication des batteries relève de l'amont de la chaîne de valeur : elle compte pour juger l'électrification sur la durée de vie des autocars (120 t par an, soit 33,90 g en 2030), pas pour piloter l'exploitation. Le domicile-travail et les locaux ne dépendent pas de l'électrification. Sur ce périmètre, les émissions par voyageur-kilomètre baissent de 54,44 g à 31,73 g (− 41,71 %), sans atteindre l'objectif de 30 g. Sur les seuls autocars du dépôt, elles tomberaient à 27,96 g : ce périmètre trop étroit aurait affiché la réussite. L'écart vient de l'affrètement, triplé faute de conducteurs (360 t, 20,48 % des émissions de 2030). Les indicateurs à suivre relient l'électrification à ses conditions de réussite : disponibilité des autocars (94 % à Vaulmérac), formation des conducteurs, part de l'affrètement.

**Conclusion** : l'électrification divise presque par deux les émissions des autocars du dépôt, mais l'objectif de 30 g ne sera atteint que si l'affrètement redescend : le recrutement des conducteurs (deuxième axe du plan) conditionne le résultat du troisième. Le tableau de bord du dépôt retient les émissions par voyageur-kilomètre, affrètement compris, et quatre indicateurs de pilotage, suivis chaque mois ou chaque trimestre et transmis à la région.

**Réponses tolérées**
- Périmètre limité aux autocars du dépôt, si le candidat montre que l'affrètement doit être suivi à part et en tire la même conclusion sur l'objectif.
- Batteries intégrées au périmètre, en annuités (120 t par an), si le choix est justifié : 33,90 g en 2030, objectif non atteint.
- Cibles différentes de celles du corrigé (disponibilité de 97 %, affrètement de 3 %), si elles sont justifiées par le cas.
- Part des kilomètres en électrique calculée sur les seuls kilomètres des autocars du dépôt (1 200 000 / 2 500 000 = 48,00 % en 2030), si le dénominateur est dit ; la cible de 40 % est atteinte.

**Erreurs fréquentes**
- `JUR-T02` — Proposer des indicateurs génériques de RSE sans lien avec l'électrification du dépôt ni avec les attentes de la région.
- `JUR-T03` — Calculer les émissions sans comparer le résultat à l'objectif ni expliquer l'écart par l'affrètement.
- `JUR-T05` — Traiter les émissions sans voir qu'elles dépendent du recrutement des conducteurs et de la disponibilité des autocars, c'est-à-dire de la stratégie et des coûts.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 3.2 (l. 880-883 : « sélectionner les données nécessaires au reporting en fonction du périmètre défini », « concevoir des indicateurs de durabilité pertinents ») ; guide p. 126 | périmètre, données, indicateurs | [V] | F11 § 0 |
| Données d'activité × facteur d'émission fourni (valeurs pédagogiques) | calcul des émissions | [V] | F11 § 1, § 3.1 |
| Indicateurs reliés aux facteurs clés de succès, avec formule, cible et périodicité ; « listes à la Prévert » refusées (guide p. 126) | conception des indicateurs | [V] | F11 § 4, § 6 |

---

### 3.4 Rédiger une note au comité de pilotage (20 lignes au maximum) (1,5 pt)

**Compétences visées :**
- `2.2.d` — Analyser les résultats obtenus
- `2.2.e` — Produire une synthèse rédigée et structurée concernant le pilotage du projet
- `3.2.c` — Concevoir des indicateurs de durabilité pertinents

**Barème (1,5 pt)** — grille de notation d'une réponse rédigée

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Délai, budget et trésorerie : mise en service le 27 juillet 2029 (semaine 82), 5 semaines de marge avant le 31 août 2029, grâce à l'ordre poste puis bornes de la tranche 2 ; budget de 14 500 k€ (autocars 11 280, travaux 3 220), financé sur la durée, mais besoin de 1 480 k€ au T2 2029 et moyens de le réduire (reprise à la livraison, aide à la réception) ou de le couvrir (financement relais) | 0,5 |
| 3.4-02 | Risques du projet classés selon le triptyque qualité, coût, délai et actions : retard du raccordement (tâche critique d'un tiers : + 4 semaines laissent 1 semaine, + 8 font finir le 21 septembre ; engagement de date et suivi mensuel ; repli possible, par exemple : rentrée avec 12 autocars électriques sur la tranche 1, en service fin juin, formation achevée le 10 août, et 12 autocars au gazole gardés jusqu'à la fin de la mise en service) ; livraison des autocars (10 semaines de marge) ; équipe d'électriciens devenue critique (une seconde équipe rendrait les 2 semaines perdues) ; disponibilité et pièces (stock, mécaniciens formés) ; formation trop tardive (la commencer à Vaulmérac) ; fermeture de la tranche 2 (décaler E) | 0,5 |
| 3.4-03 | Indicateurs suivis et apport au renouvellement des lots : émissions par voyageur-km affrètement compris (31,73 g pour 30), part de l'électrique (42,86 %), affrètement (10,71 %), disponibilité ; preuves chiffrées et vérifiables pour la région, qui comptera aussi les services affrétés ; lien avec le recrutement des conducteurs ; structure, longueur respectée, conclusion qui prend position | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : une note de reporting de projet, structurée comme une revue (situation, risques, décisions demandées, suivi), qui reprend les résultats des questions 3.1 à 3.3 sans les recalculer et relie le pilotage du projet (qualité, coût, délai) à l'enjeu stratégique, le renouvellement des lots de 2029, et aux attentes des parties prenantes : la région, VALDORÈNE Capital, le chef du dépôt et les conducteurs.
- Alternatives acceptées : présentation par feux (délai orange, trésorerie orange, durabilité orange), si chaque feu est justifié par un chiffre ; cotation des risques par probabilité et gravité, si elle reste brève.

**Réponse attendue** (exemple de note, 20 lignes au maximum)

> **Note au comité de pilotage du projet d'électrification du dépôt de Lasvérac — 9 décembre 2027**
>
> **1. Délai.** En confiant le poste puis les bornes de la tranche 2 à l'équipe d'électriciens, le dépôt sera en service le 27 juillet 2029, avec 5 semaines de marge avant le 31 août. Le chemin critique passe par le raccordement, réalisé par le gestionnaire du réseau.
>
> **2. Budget et trésorerie.** Le projet coûte 14 500 k€, dont 11 280 k€ d'autocars. Il est financé sur la durée, mais au T2 2029 le solde des autocars précède l'aide et la reprise : il manque 1 480 k€ pendant un trimestre. Je propose de négocier la reprise des autocars au gazole à la livraison et le versement du solde de l'aide à la réception (besoin ramené à 120 k€), et de prévoir un financement relais pour le reste.
>
> **3. Risques et actions.** Délai : un retard de 8 semaines du raccordement repousserait la fin au 21 septembre ; demander un engagement de date au gestionnaire et le suivre chaque mois ; en repli, démarrer la rentrée avec 12 autocars électriques sur la tranche 1, en service fin juin, et garder 12 autocars au gazole jusqu'à la fin des travaux. Livraison des autocars : 10 semaines de marge, point mensuel avec le constructeur. Qualité : former les conducteurs dès l'automne 2028 à Vaulmérac, former les mécaniciens et constituer un stock de pièces avant la livraison (disponibilité de 94 % à Vaulmérac). Exploitation : décaler le génie civil de la tranche 2 pour ne la fermer que 26 semaines.
>
> **4. Durabilité et lots de 2029.** Nous suivrons chaque trimestre les émissions par voyageur-kilomètre, affrètement compris (54,44 g en 2026, 31,73 g prévus en 2030 pour un objectif de 30 g), la part des kilomètres en électrique (42,86 %), la part de l'affrètement (10,71 %) et la disponibilité des autocars. Ces chiffres prouveront à la région ce qu'elle examinera ; ils montrent aussi que l'objectif dépend du recrutement des conducteurs.

**Grille** : critères 1 à 6 de la grille de notation (concept, mobilisation, faits du cas, analyse, préconisation, forme). La note doit prendre position sur la couverture du besoin de trésorerie et sur la réponse au risque du raccordement ; elle relie les indicateurs au renouvellement des lots.

**Réponses tolérées**
- Plan différent (situation, risques, décisions, suivi), si les quatre éléments demandés sont présents.
- Proposition de commencer certains travaux plus tôt, ou de financer le besoin par un découvert autorisé, si la proposition est cohérente avec les annexes et chiffrée.
- Cotation des risques par probabilité et gravité, si elle reste brève et conduit aux mêmes priorités.

**Erreurs fréquentes**
- `JUR-T03` — Note qui résume les calculs sans dire ce qui est demandé au comité.
- `JUR-T06` — Longueur dépassée, absence de structure.
- `JUR-T05` — Note purement technique (dates et montants), sans lien avec le renouvellement des lots et les attentes de la région, ou purement stratégique, sans chiffres.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 795-796 : triptyque qualité, coût, délai, risques du projet ; l. 806 : tableau de bord du projet et reporting) ; guide p. 113 et p. 121 | risques, actions, note au comité | [V] | F05 § 2, § 6, § 7 |
| Indicateurs de durabilité reliés à la stratégie (guide p. 126) | indicateurs suivis | [V] | F11 § 4 |
| Attentes des parties prenantes : « selon les travaux de Edward Freeman », une partie prenante est tout acteur pouvant affecter ou être affecté par l'activité de l'entreprise (Freeman, 1984) | région, fonds, salariés | [S] | F12 § 5 ; F13 |

---

## Contrôles avant publication

- [x] `python3 -I outils/dscgcheck ue3/exercices/ex49_electrification_depot_durabilite/corrige.yaml` : 0 erreur, 0 avertissement ; réseau sans contrainte, planning retenu et variante écartée, budget du projet par semaine et cumul de fin de trimestre, plan de financement après financement relais, émissions par voyageur-kilomètre et indicateurs recalculés par l'outil ; comparaison des deux ordres, fermeture des quais, scénarios de délai, budget par tâche et par trimestre, plan de financement avant financement relais (solde cumulé négatif au T2 2029, que le bloc de trésorerie signalerait par un avertissement) et variantes, émissions par source recalculés par script (`/paperclip/shared/dscglab-travail/DSC-1052/calculs.py`).
- [x] Données partagées du sujet n° 17 respectées : présentation commune reprise mot pour mot ; 18 autocars électriques à Vaulmérac depuis 2025 (disponibilité de 2026, prêt de deux autocars pour les essais et la formation) ; échéance des lots au 31 août 2029 ; attention de la région à la part de véhicules à faibles émissions ; affrètement faute de conducteurs ; Lasvérac, l'un des quatre dépôts de Corrèze ; 486 véhicules ; autocars électriques livrés dix-huit mois après la commande, comme dans le dossier 1.
- [x] Compétences visées présentes dans `programme/perimetre_ue3.yaml` ; outil non prescrit dans l'énoncé ; chaque question présente le concept, l'applique au cas, conclut ; synthèse bornée (3.4, 20 lignes au maximum) ; ressources du plan de financement données : aucun choix de financement, aucune actualisation, aucun critère de choix d'investissement ; ni valeur acquise, ni accélération, ni coût à terminaison ; ni bilan complet des émissions, ni matrice de double matérialité ; aucune norme de reporting.
- [x] Conventions écrites dans les annexes : planning (dates, marges, règle des quais, équipe unique sans interruption, planning retenu au plus tôt), budget (trimestres de 13 semaines, répartition uniforme, acompte et solde des autocars), plan de financement (emplois, ressources, solde cumulé), émissions et indicateurs, arrondis.
- [x] Entités et personnes fictives (M. Rémi FONTAJOU, Mme Sylvie CORBELANGE, M. Kévin ARNOUILLAC ; Mme Corinne LASCABANNE et M. Pascal BRAVELLON, déjà présents dans le dossier 2) ; gestionnaire du réseau, constructeur, éditeur du logiciel, négociant et banque non nommés ; aucune règle réelle du raccordement, des aides publiques ni de la mise en concurrence ; facteurs d'émission présentés comme valeurs pédagogiques du cas ; attribution d'auteur limitée à F13 (Freeman, 1984).
