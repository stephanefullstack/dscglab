# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 3 – Contrôle de gestion et stratégie — Exercice d'entraînement n° 27 — Dossier 2 (7 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F05 pilotage des projets, F08 gestion des risques et contrôle interne, F13 registre des auteurs (toutes à jour au 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (planning, charge des méthodes au plus tôt et lissée, budget par tâche recalculés ; budget par lot et par nature, cotation des risques, réserve pour aléas et parades : calculs divers recalculés par script ; barème partiel sur 7 ; liste noire ; hors-programme).

Bien que le corrigé mentionne des auteurs, des textes et des données, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur le choix et la justification des outils, la justesse des calculs, la pertinence de l'analyse au regard du cas et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet) ; pour chaque question, la présentation des concepts et outils avant leur mobilisation puis la conclusion sont notées. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Planning du projet tiré du compte rendu : antériorités, dates au plus tôt et au plus tard, marges totales et libres, chemin critique, durée, marge sur le jalon de septembre 2028 | `2.2.b` Élaborer la planification du projet | 2 |
| 2.2 Charge de l'équipe des méthodes au plus tôt, dépassements, lissage dans les marges, marges consommées, solutions écartées | `2.2.b` Élaborer la planification du projet ; `2.2.d` Analyser les résultats obtenus | 1,5 |
| 2.3 Budget par tâche et par lot ; criticité des risques, hiérarchisation, réserve pour aléas ; comparaison à l'enveloppe ; appréciation chiffrée de deux parades | `2.2.a` Concevoir le plan de financement d'un projet ; `2.5.b` Analyser les risques rencontrés par l'organisation | 2 |
| 2.4 Note au comité de pilotage (20 lignes au maximum) | `2.2.e` Produire une synthèse rédigée et structurée concernant le pilotage du projet ; `2.2.d` Analyser les résultats obtenus ; `2.5.d` Élaborer des préconisations permettant de gérer les risques | 1,5 |
| **Dossier 2 – Piloter le projet de nouvelle ligne d'assemblage : planning, charge des équipes, budget et risques** | | **7** |

---

## DOSSIER 2 – PILOTER LE PROJET DE NOUVELLE LIGNE D'ASSEMBLAGE : PLANNING, CHARGE DES ÉQUIPES, BUDGET ET RISQUES (7 points)

### 2.1 Établir le planning du projet à partir du compte rendu, dire si les premières séries pourront être produites en septembre 2028 et mesurer la marge sur le jalon (2 pts)

**Compétence visée :**
- `2.2.b` — Élaborer la planification du projet (réseau ou diagramme de Gantt construit à partir d'un texte, dates au plus tôt et au plus tard, marges, chemin critique, jalons ; triptyque QCD et risques du projet)

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Concepts présentés (tâche, antériorité, date au plus tôt et au plus tard, marge totale et libre, chemin critique, jalon) ; tableau des tâches tiré du texte, avec les antériorités multiples : B, E et F après A ; C et D après B ; G après F ; **H après C et E** ; **I après D et E** ; **J après H et I** ; **K après G et J** ; L après K ; réseau ou diagramme de Gantt cohérent | 0,5 |
| 2.1-02 | Dates de début et de fin au plus tôt et au plus tard de chaque tâche (tableau ci-dessous), dates au plus tard calculées en repartant de la durée totale | 0,5 |
| 2.1-03 | Marges totales et libres : D (8 et 0), E (12 et 6), F (16 et 0), G (16 et 16), I (8 et 8), les autres nulles ; lecture : la marge libre nulle de F signifie qu'un retard des gammes consomme d'abord la marge des outillages, celle de D qu'un retard de la cellule consomme celle de son installation | 0,5 |
| 2.1-04 | Durée **70 semaines**, chemin critique **A-B-C-H-J-K-L** ; fin le vendredi 4 août 2028 ; **marge de 4 semaines** sur le jalon de la fin de la semaine 74 (vendredi 1er septembre 2028) : les premières séries peuvent être produites en septembre 2028 ; lecture valorisée, non exigée : le chemin critique dépend pour 28 semaines d'un fournisseur extérieur (postes de brasage), et la marge sur le jalon ne représente que 5,71 % de la durée du projet | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **réseau des antécédents** (tâches, durées, antériorités), parcouru en avant pour les dates au plus tôt et en arrière, depuis la durée totale, pour les dates au plus tard, suivi du **diagramme de Gantt**, qui sert à lire le calendrier, les jalons et les marges. Il faut d'abord transformer le compte rendu de l'annexe 2.1 en tableau des antériorités : c'est ce que le programme attend (« construire des diagrammes à partir de données brutes (textes) »).
- Alternatives acceptées : réseau en tâches sur les nœuds (méthode des potentiels) ou sur les flèches (avec des tâches fictives correctement placées) ; Gantt seul s'il porte les dates au plus tôt et au plus tard et les marges ; semaines numérotées de 1 (début de A en semaine 1, fin de L en semaine 70) au lieu des dates à partir de 0, si l'écriture est cohérente.

**Conventions rappelées** (annexe 2.1)

- Semaines entières ; date 0 = début de la semaine 1 (lundi 5 avril 2027) ; une tâche commencée en *t* et de durée *d* occupe les semaines *t* + 1 à *t* + *d* et finit en *t* + *d* ; pas d'interruption.
- Marge totale = début au plus tard − début au plus tôt ; marge libre = plus petit début au plus tôt des successeurs (ou fin du projet) − fin au plus tôt ; chemin critique = tâches de marge totale nulle ; jalon : qualification terminée à la fin de la semaine 74 (vendredi 1er septembre 2028).

**Réponse attendue**

*Concepts (2.1-01).* Le planning d'un projet ordonne ses tâches selon leurs antériorités. La **date au plus tôt** d'une tâche est la plus grande des fins au plus tôt de ses prédécesseurs. La **date au plus tard** est la date à laquelle elle doit commencer pour ne pas retarder la fin du projet. La **marge totale** mesure le retard qu'une tâche peut prendre sans retarder le projet. La **marge libre** mesure celui qu'elle peut prendre sans retarder aucun de ses successeurs. Le **chemin critique**, formé des tâches sans marge totale, fixe la durée du projet : tout retard sur l'une d'elles la retarde d'autant. Un **jalon** est une date clé ; l'écart entre la fin prévue et le jalon mesure la marge dont dispose le projet.

*Application (2.1-02 et 2.1-03).*

| Tâche | Durée | Antériorités | Début au plus tôt | Fin au plus tôt | Début au plus tard | Fin au plus tard | Marge totale | Marge libre |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| A Implantation et cahiers des charges | 10 | — | 0 | 10 | 0 | 10 | **0** | 0 |
| B Consultation et commandes | 8 | A | 10 | 18 | 10 | 18 | **0** | 0 |
| C Fabrication et livraison des postes de brasage | 28 | B | 18 | 46 | 18 | 46 | **0** | 0 |
| D Construction de la cellule d'essais | 22 | B | 18 | 40 | 26 | 48 | 8 | 0 |
| E Aménagement du bâtiment | 24 | A | 10 | 34 | 22 | 46 | 12 | 6 |
| F Gammes d'assemblage et postes de travail | 12 | A | 10 | 22 | 26 | 38 | 16 | 0 |
| G Outillages et montages d'assemblage | 20 | F | 22 | 42 | 38 | 58 | 16 | 16 |
| H Installation et réglage des postes de brasage | 6 | C, E | 46 | 52 | 46 | 52 | **0** | 0 |
| I Installation et mise en service de la cellule | 4 | D, E | 40 | 44 | 48 | 52 | 8 | 8 |
| J Formation des opérateurs | 6 | H, I | 52 | 58 | 52 | 58 | **0** | 0 |
| K Présérie de 30 pompes à chaleur | 5 | G, J | 58 | 63 | 58 | 63 | **0** | 0 |
| L Qualification du produit et du procédé | 7 | K | 63 | 70 | 63 | 70 | **0** | 0 |

*Lecture des marges.* L'aménagement du bâtiment (E) peut prendre 12 semaines de retard sans retarder le projet, dont 6 sans gêner aucune autre tâche (marge libre) : au-delà, il retarde l'installation de la cellule (I). Les gammes (F) ont 16 semaines de marge totale mais **aucune marge libre** : tout retard des gammes se reporte sur les outillages (G), qui disposent eux-mêmes de 16 semaines. De même, un retard de la cellule (D) consomme la marge de son installation (I), qui n'a que 8 semaines.

*Chemin critique, jalon et robustesse (2.1-04).* Le projet dure **70 semaines** ; le chemin critique est **A → B → C → H → J → K → L** (10 + 8 + 28 + 6 + 6 + 5 + 7 = 70). La qualification se termine à la fin de la semaine 70, le **vendredi 4 août 2028**. Le jalon de la fin de la semaine 74 (vendredi 1er septembre 2028) est tenu avec une **marge de 4 semaines** : les premières séries pourront être produites à partir du lundi 4 septembre 2028, avant la saison de chauffe. La marge est mince : 5,71 % de la durée du projet. Surtout, 28 des 70 semaines du chemin critique dépendent d'un **fournisseur extérieur**, celui des postes de brasage : un retard de livraison de plus de 4 semaines suffit à faire glisser les premières séries après septembre. Jalons à suivre : cahiers des charges arrêtés fin semaine 10 (vendredi 11 juin 2027), commandes passées fin semaine 18 (6 août 2027), postes livrés fin semaine 46 (18 février 2028), postes réglés fin semaine 52 (31 mars 2028), opérateurs formés fin semaine 58 (12 mai 2028), présérie terminée fin semaine 63 (16 juin 2028), qualification prononcée fin semaine 70 (4 août 2028). Conclusion : la date de septembre 2028 est tenable, mais elle dépend de la livraison des postes de brasage.

**Calculs détaillés**

| Chemin | Durée (semaines) | Écart à la durée du projet |
|---|---:|---:|
| A-B-C-H-J-K-L | 70 | 0 (critique) |
| A-B-D-I-J-K-L | 62 | 8 |
| A-E-H-J-K-L | 58 | 12 |
| A-E-I-J-K-L | 56 | 14 |
| A-F-G-K-L | 54 | 16 |

Contrôle : la marge totale d'une tâche est l'écart entre la durée du projet et le plus long chemin qui passe par elle (D et I : 70 − 62 = 8 ; E : 70 − 58 = 12 ; F et G : 70 − 54 = 16).

**Réponses tolérées**
- Semaines numérotées de 1 à 70 au lieu des dates à partir de 0, si l'écriture est cohérente.
- Dates au plus tard exprimées seulement en début ou seulement en fin de tâche, si les marges totales sont justes.
- Marge sur le jalon exprimée en jours ou en dates (4 août contre 1er septembre 2028), si elle vaut 4 semaines.

**Erreurs fréquentes**
- `JUR-T10` — Oublier une antériorité multiple (H après C **et** E ; I après D **et** E ; K après G **et** J) et trouver un autre chemin critique ; calculer les dates au plus tard sans repartir de la durée totale ; confondre marge totale et marge libre.
- `JUR-T07` — Dessiner un Gantt sans dates au plus tard ni marges, ou conclure sans confronter la fin du projet au jalon de septembre 2028.
- `JUR-T03` — Recopier le tableau sans lire les marges ni relever la dépendance du chemin critique à un fournisseur.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 791-801 : « construire des diagrammes à partir de données brutes (textes) » ; Gantt, marges, jalons, chemin critique ; triptyque QCD, risques du projet) | planification | [V] | F05 § 0, § 4 |
| `ue3/00_LISEZMOI.md`, convention d'ordonnancement ; marge libre : formule de cours | dates, marges | [V] ; [S] marge libre | F05 § 1 |
| Diagramme de Gantt (Henry L. Gantt, années 1910) | lecture calendaire | [V] programme ; [S] origine | F13 § 8 |

---

### 2.2 Calculer la charge de l'équipe des méthodes au plus tôt, repérer les dépassements, proposer un calendrier lissé dans les marges et l'apprécier (1,5 pt)

**Compétences visées :**
- `2.2.b` — Élaborer la planification du projet (ressources des tâches, marges, jalons)
- `2.2.d` — Analyser les résultats obtenus (risques du projet, actions correctives)

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Charge au plus tôt par période (tableau ci-dessous) ; dépassements des cinq techniciens en **semaines 11 à 18** (6 : B 2 + E 1 + F 3) et en **semaines 41 et 42** (6 : G 2 + I 4), soit 10 semaines-technicien en excès ; charge totale de 252 semaines-technicien (72,00 % de la capacité affectée au projet) | 0,5 |
| 2.2-02 | Lissage : B est critique ; décaler F ne marche pas (les outillages G, repoussés d'autant, viennent chevaucher l'installation de la cellule I) ; **E décalée de 8 semaines** (semaines 19 à 42), le décalage minimal pour libérer les semaines 11 à 18, ce qui repousse **I de 2 semaines** (semaines 43 à 46) et supprime aussi le second dépassement ; charge lissée au plus de 5 techniciens ; **fin du projet inchangée (semaine 70)**, chemin critique inchangé | 0,5 |
| 2.2-03 | Marges consommées : E passe de 12 à **4 semaines** de marge totale (marge libre de 6 à 0), I de 8 à **6** ; D gagne 2 semaines de marge libre ; l'équipe est **saturée 12 semaines** (semaines 11 à 22) ; un retard du bâtiment de plus de 4 semaines retarde désormais le projet (risque R3 : 7 semaines) ; solutions écartées : sixième technicien prêté (prélevé sur les lignes actuelles, en janvier en pleine saison de chauffe) ou intérimaire (350 h × (80 − 50) € = **10,5 k€** de surcoût pour le projet, sur 28 k€ décaissés) ; conclusion : lisser, garder l'intérimaire comme solution de secours | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **profil de charge** d'une ressource partagée, construit sur le diagramme de Gantt au plus tôt (techniciens mobilisés semaine par semaine, regroupés en périodes où la charge est constante), comparé à la capacité, puis le **lissage** : on décale des tâches non critiques dans leurs marges, sans interruption ni fractionnement, pour ramener la charge sous la capacité sans retarder la fin du projet.
- Alternatives acceptées : profil présenté semaine par semaine, par période ou sous forme d'histogramme sous le Gantt ; tout calendrier qui respecte les antériorités, la capacité de 5 et la fin en semaine 70 : c'est le cas des variantes qui décalent en outre la construction de la cellule (D) d'une ou deux semaines, sans utilité ; présentation du lissage en deux temps (I décalée de 2 semaines dans sa marge libre, puis E décalée de 8 semaines) si le calendrier final est le même. Non accepté : décaler une tâche critique (B), interrompre ou fractionner une tâche, réduire le nombre de techniciens d'une tâche, ou retarder la fin du projet.

**Conventions rappelées** (annexe 2.2)

- Charge d'une semaine = techniciens mobilisés par les tâches en cours ; dépassement au-delà de 5 ; une tâche décalée garde sa durée et ses besoins ; 35 heures par technicien et par semaine de tâche.

**Réponse attendue**

*Concepts.* Un projet consomme des **ressources** dont la capacité est limitée. Le **profil de charge** additionne, période par période, les besoins des tâches en cours selon le planning retenu. Lorsqu'il dépasse la capacité, deux voies s'offrent : **lisser** la charge en décalant des tâches non critiques dans leurs marges, ce qui ne coûte rien mais consomme des marges, ou **augmenter la capacité**, ce qui coûte. Le lissage n'allonge pas le projet tant que chaque tâche décalée reste dans sa marge totale ; il rend le planning plus fragile.

*Charge au plus tôt (2.2-01).*

| Semaines | 1-10 | 11-18 | 19-22 | 23-34 | 35-40 | 41-42 | 43-44 | 45-46 | 47-52 | 53-58 | 59-63 | 64-70 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Tâches en cours (techniciens) | A 4 | B 2, E 1, F 3 | D 1, E 1, F 3 | D 1, E 1, G 2 | D 1, G 2 | G 2, I 4 | I 4 | — | H 3 | J 1 | K 4 | L 2 |
| **Charge** | 4 | **6** | 5 | 4 | 3 | **6** | 4 | 0 | 3 | 1 | 4 | 2 |
| Dépassement | | **1** | | | | **1** | | | | | | |

La charge dépasse l'effectif affecté au projet pendant **10 semaines** : en semaines 11 à 18 (juin à début août 2027), où la consultation, le suivi du bâtiment et les gammes se cumulent, et en semaines 41 et 42 (janvier 2028), où les outillages chevauchent l'installation de la cellule. L'excès est de 10 semaines-technicien. Sur l'ensemble du projet, la charge totale est de 252 semaines-technicien pour une capacité de 5 × 70 = 350, soit **72,00 %** : le problème n'est pas le volume de travail, mais sa **répartition dans le temps**.

*Lissage (2.2-02).* La consultation (B) est critique et ne peut pas bouger. Deux tâches non critiques sont en cause dans le premier dépassement :
- décaler les **gammes (F)**, qui n'ont pas de marge libre, repousse d'autant les outillages (G). Avec F décalée de 8 semaines, G occupe les semaines 31 à 50 et chevauche l'installation de la cellule (I, 4 techniciens) : la charge atteint 6 en semaines 41 à 44, et I ne peut pas finir après la semaine 52. Cette voie échoue ;
- décaler l'**aménagement du bâtiment (E)**, qui ne mobilise qu'un technicien, suffit. Comme la tâche ne peut être ni interrompue ni fractionnée, il faut la faire commencer après la semaine 18, soit un décalage de **8 semaines** : E occupe les semaines 19 à 42. Ce décalage dépasse sa marge libre (6 semaines) : l'installation de la cellule (I), qui attend la fin de E, est repoussée de **2 semaines**, aux semaines 43 à 46. Elle ne chevauche plus les outillages, qui finissent en semaine 42 : le second dépassement disparaît aussi.

| Semaines | 1-10 | 11-22 | 23-40 | 41-42 | 43-46 | 47-52 | 53-58 | 59-63 | 64-70 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Tâches en cours (techniciens) | A 4 | B 2 (11-18), F 3, E 1 (19-22), D 1 (19-22) | D 1, E 1, G 2 | E 1, G 2 | I 4 | H 3 | J 1 | K 4 | L 2 |
| **Charge lissée** | 4 | **5** | 4 | 3 | 4 | 3 | 1 | 4 | 2 |

La charge ne dépasse plus cinq techniciens. Le chemin critique et la fin du projet (semaine 70, vendredi 4 août 2028) sont inchangés : le lissage ne coûte rien et ne retarde pas les premières séries.

*Marges consommées et appréciation (2.2-03).*
- **Marges.** L'aménagement du bâtiment perd 8 de ses 12 semaines de marge totale : il ne lui en reste que **4**, et aucune marge libre. L'installation de la cellule passe de 8 à **6 semaines** de marge. La construction de la cellule (D) gagne 2 semaines de marge libre. Le risque R3 de l'annexe 2.4 change de nature : un retard de 7 semaines du bâtiment, absorbé dans le planning au plus tôt, retarderait désormais la fin du projet de 3 semaines et consommerait presque toute la marge sur le jalon (sa criticité passerait de 4 à 6 avec les marges du planning lissé).
- **Saturation.** L'équipe travaille à pleine capacité pendant **12 semaines** (semaines 11 à 22). Une absence prolongée d'un technicien dans cette période (risque R5) ne serait plus absorbable : elle retarderait les gammes ou, pire, la consultation, qui est critique.
- **Solutions écartées.** Le sixième technicien proposé par le directeur industriel manquerait aux lignes actuelles, et le second dépassement tombe en janvier 2028, en pleine saison de chauffe. Un intérimaire couvrirait l'excès, soit 10 semaines-technicien × 35 h = 350 h. CALDÉRINE décaisserait 350 × 80 € = 28 000 €, mais ces heures sont déjà budgétées à 50 € et les techniciens ainsi libérés retournent aux lignes actuelles : le surcoût pour le projet est de 350 × (80 − 50) € = **10,5 k€** (annexe 2.2). Ce surcoût épuiserait presque l'enveloppe (question 2.3).
- Conclusion : retenir le lissage, qui est gratuit et tient la date, mais suivre de près l'avancement du bâtiment et garder l'intérimaire comme **solution de secours** en cas d'absence d'un technicien pendant les semaines 11 à 22.

**Réponses tolérées**
- Décalages supplémentaires de D d'une ou deux semaines, sans effet sur la charge, s'ils sont justifiés.
- Lissage obtenu en deux temps (I dans sa marge libre, puis E), si le calendrier final et la charge sont justes.
- Préférence argumentée pour un intérimaire ou un technicien prêté afin de garder la marge du bâtiment, si son coût (10,5 k€ de surcoût pour le projet) ou son effet sur les lignes actuelles est mesuré et confronté à l'enveloppe.
- Coût de l'intérimaire chiffré à 28 k€, s'il est présenté comme le décaissement supplémentaire de l'entreprise et non comme le surcoût imputé au projet.
- Proposition de la cheffe du projet (ramener la qualification de sept à cinq semaines) écartée dès cette question : valorisée, car la qualification (L) ne participe à aucun dépassement et la responsable qualité s'y oppose.

**Erreurs fréquentes**
- `JUR-T10` — Compter la charge d'une tâche sur ses semaines sans tenir compte du chevauchement exact (G finit en semaine 42, I commence en semaine 41 au plus tôt) ; décaler une tâche critique ou fractionner une tâche pour « remplir » les creux.
- `JUR-T05` — Lisser sans dire ce que coûtent les solutions de capacité, ou sans relier le lissage aux risques du projet.
- `JUR-T03` — Présenter le calendrier lissé sans mesurer les marges consommées.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 799-801 : Gantt, marges de temps, jalons, **ressources**, chemin critique ; l. 806 : tableau de bord du projet) | charge d'une ressource | [V] | F05 § 0, § 4, § 7 |
| Profil de charge et lissage dans les marges : technique de cours, non développée dans F05 | charge par période, lissage | [S] | — |

---

### 2.3 Établir le budget par tâche et par lot, coter les risques, constituer la réserve pour aléas, la comparer à l'enveloppe et apprécier les parades (2 pts)

**Compétences visées :**
- `2.2.a` — Concevoir le plan de financement d'un projet (budget du projet : coûts par tâche et par lot, ressources, réserve pour aléas)
- `2.5.b` — Analyser les risques rencontrés par l'organisation (criticité = probabilité × gravité, échelles de cotation, hiérarchisation)

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Budget par tâche (tableau ci-dessous) : heures des méthodes 8 820 h × 50 € = 441,0 k€, heures des opérateurs 3 900 h × 40 € = 156,0 k€ ; composants de la présérie 30 × 18 000 € = 540 k€ ; **budget de 5 800,0 k€** | 0,5 |
| 2.3-02 | Budget par lot : études, méthodes et outillages **601,0** ; bâtiment **1 302,0** ; postes de brasage **1 821,5** ; cellule d'essais **1 069,5** ; formation **172,5** ; présérie et qualification **833,5** k€ ; lecture valorisée, non exigée : poids des postes de brasage et du bâtiment (53,85 %), part des coûts externes (89,71 %), engagements à la fin de la consultation (3 940 k€, 67,93 % du budget), donc budget à piloter surtout avant la signature des commandes | 0,5 |
| 2.3-03 | Cotation : retard sur la fin du projet calculé avec les marges de la question 2.1 (R1 : 6 − 0 = 6 ; R4 : 3 ; R7 : 2 ; les autres nuls) ; gravité = plus haut des deux niveaux ; criticités **R1 12, R4 9** (majeurs), R2 6, R8 6, R3 4, R6 4 (significatifs), R5 3, R7 2 (faibles) ; hiérarchie présentée (matrice ou tableau trié) | 0,5 |
| 2.3-04 | Réserve **165,0 k€** (24 + 30 + 18 + 48 + 24 + 21 ; R5 et R7 exclus), 2,84 % du budget ; total **5 965,0 k€** pour une enveloppe de 6 000 k€ : **35,0 k€** de reste (0,58 %) ; parades : R1 (50 k€) sort le risque de la réserve (criticité 3), surcoût net **26 k€**, mais retard possible ramené à 3 semaines : **jalon protégé** (sans parade, perte espérée de 0,30 × 2 × 60 = 36 k€ de marge) ; R4 (20 k€) ramène la criticité à 6 et le coût espéré à 24 k€ : **gain net de 4 k€** ; avec les deux, total **5 987,0 k€**, reste **13,0 k€** (0,22 %) : les deux parades sont à décider ; l'intérimaire (10,5 k€ de surcoût) porterait le total à 5 997,5 k€ et épuiserait l'enveloppe (2,5 k€ de reste) | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **budget du projet** (plan de financement au sens du programme), construit par tâche à partir des ressources consommées (heures internes valorisées au coût horaire, achats, sous-traitance, essais), puis agrégé par lot. Il est complété par une **réserve pour aléas** tirée du **registre des risques** du projet : cotation de la **criticité** (probabilité × gravité) sur les échelles de CALDÉRINE, hiérarchisation, puis coût espéré (probabilité × surcoût) des risques retenus. La réserve est ainsi justifiée risque par risque, et non fixée en pourcentage forfaitaire, comme le demande la directrice administrative et financière.
- Alternatives acceptées : budget présenté directement par lot si le détail par tâche est vérifiable ; cartographie présentée en matrice probabilité × gravité ; criticité cotée sans le retard sur la fin du projet si le candidat le signale comme une hypothèse et la corrige ensuite (gravité de R1 de 2 au lieu de 4 : criticité 6) : la lecture par les marges est attendue et valorisée.

**Conventions rappelées** (annexes 2.3 et 2.4)

- Heures des méthodes = techniciens × durée × 35 h, à 50 € ; opérateurs à 40 € ; montants en k€ à une décimale, pourcentages à deux décimales.
- Retard sur la fin = retard possible − marge totale du planning au plus tôt (nul si négatif) ; gravité = plus haut niveau entre surcoût et retard ; criticité = probabilité × gravité ; majeur ≥ 9, significatif 4 à 8, faible 1 à 3 ; réserve = Σ probabilité × surcoût des risques majeurs et significatifs ; enveloppe de 6 000 k€, parades décidées comprises.

**Réponse attendue**

*Concepts.* Le **budget d'un projet** valorise les ressources de chaque tâche : heures internes, achats, sous-traitance, prestations. Le découpage en **lots** confie chaque partie du projet à un responsable et permet de suivre les engagements. Le budget ne couvre que les coûts prévus ; les aléas sont couverts par une **réserve**, calculée à partir des risques identifiés. Chaque risque est coté par sa **criticité**, produit de sa probabilité et de sa gravité, sur des échelles données. La criticité hiérarchise les risques : les plus critiques appellent une parade, les plus faibles sont acceptés. Le **coût espéré** d'un risque (probabilité × surcoût) mesure ce qu'il faut mettre en réserve pour le couvrir en moyenne.

*Budget par tâche (2.3-01).*

| Tâche | Heures des méthodes | Méthodes (k€) | Heures des opérateurs | Opérateurs (k€) | Achats (k€) | Sous-traitance (k€) | Essais et formation (k€) | **Total (k€)** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 1 400 | 70,0 | | | | | | **70,0** |
| B | 560 | 28,0 | | | | | | **28,0** |
| C | 0 | | | | 1 720 | | | **1 720,0** |
| D | 770 | 38,5 | | | | 960 | | **998,5** |
| E | 840 | 42,0 | | | | 1 260 | | **1 302,0** |
| F | 1 260 | 63,0 | | | | | | **63,0** |
| G | 1 400 | 70,0 | | | 370 | | | **440,0** |
| H | 630 | 31,5 | | | | 70 | | **101,5** |
| I | 560 | 28,0 | | | | | 43 | **71,0** |
| J | 210 | 10,5 | 1 800 | 72,0 | | | 90 | **172,5** |
| K | 700 | 35,0 | 2 100 | 84,0 | 540 | | | **659,0** |
| L | 490 | 24,5 | | | | | 150 | **174,5** |
| **Total** | **8 820** | **441,0** | **3 900** | **156,0** | **2 630** | **2 290** | **283** | **5 800,0** |

Heures des méthodes : techniciens × durée × 35 (A : 4 × 10 × 35 = 1 400 h). Heures des opérateurs : 24 × 75 = 1 800 h pour la formation, 12 × 175 = 2 100 h pour la présérie.

*Budget par lot (2.3-02), et par nature en prolongement (valorisé, non exigé).*

| Lot | Tâches | k€ | Part |
|---|---|---:|---:|
| 1 Études, méthodes et outillages | A, B, F, G | 601,0 | 10,36 % |
| 2 Bâtiment | E | 1 302,0 | 22,45 % |
| 3 Postes de brasage | C, H | 1 821,5 | 31,41 % |
| 4 Cellule d'essais | D, I | 1 069,5 | 18,44 % |
| 5 Formation des opérateurs | J | 172,5 | 2,97 % |
| 6 Présérie et qualification | K, L | 833,5 | 14,37 % |
| **Total** | | **5 800,0** | **100,00 %** |

| Nature | k€ | Part |
|---|---:|---:|
| Heures des techniciens des méthodes | 441,0 | 7,60 % |
| Heures des opérateurs | 156,0 | 2,69 % |
| Achats | 2 630,0 | 45,34 % |
| Sous-traitance | 2 290,0 | 39,48 % |
| Essais et formation réalisés par des prestataires | 283,0 | 4,88 % |
| **Total** | **5 800,0** | **100,00 %** |

Les postes de brasage et le bâtiment font 53,85 % du budget. Les coûts externes en représentent **89,71 %** (5 203 k€) ; les heures internes, 10,29 % (597 k€). D'ici la fin de la consultation (semaine 18, août 2027), les commandes des postes de brasage et de la cellule, ainsi que la commande des travaux du bâtiment (lancés en semaine 11 au plus tôt, en semaine 19 après lissage), engagent **3 940 k€**, soit 67,93 % du budget. La maîtrise des coûts se joue donc à la consultation : après, le contrôle de gestion ne pourra plus guère agir que sur les avenants et les aléas.

*Cotation des risques (2.3-03).*

| Risque | Tâche (marge totale) | Retard sur la fin | Niveau de probabilité | Niveau de surcoût | Niveau de retard | Gravité | **Criticité** | Classe | Coût espéré (k€) |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| R1 Livraison des postes de brasage | C (0) | 6 | 3 | 2 | 4 | 4 | **12** | majeur | 24,0 |
| R4 Fuites aux brasures en qualification | L (0) | 3 | 3 | 3 | 3 | 3 | **9** | majeur | 48,0 |
| R2 Cellule non conforme | D (8) | 0 | 2 | 3 | 1 | 3 | **6** | significatif | 30,0 |
| R8 Retard des outillages | G (16) | 0 | 3 | 2 | 1 | 2 | **6** | significatif | 21,0 |
| R3 Dérive des travaux du bâtiment | E (12) | 0 | 2 | 2 | 1 | 2 | **4** | significatif | 18,0 |
| R6 Hausse des composants de la présérie | K (0) | 0 | 4 | 1 | 1 | 1 | **4** | significatif | 24,0 |
| R5 Absence d'un technicien des méthodes | F (16) | 0 | 3 | 1 | 1 | 1 | **3** | faible | (13,5) |
| R7 Échec d'opérateurs à la formation | J (0) | 2 | 1 | 1 | 2 | 2 | **2** | faible | (2,0) |

Les deux **risques majeurs** touchent des tâches critiques. R1 est le seul dont le retard possible (6 semaines) dépasse la marge sur le jalon (4 semaines) : c'est le risque qui menace la saison de chauffe. R4 combine une probabilité élevée et un retard de 3 semaines sur la fin du projet, qui consommerait presque toute cette marge. Les risques R2, R3 et R8 portent sur des tâches qui ont des marges : leur gravité ne vient que de leur coût. R6 est probable mais peu coûteux. R5 et R7 sont faibles et acceptés.

*Réserve, enveloppe et parades (2.3-04).* La réserve pour aléas est la somme des coûts espérés des six risques retenus : 24 + 48 + 30 + 21 + 18 + 24 = **165,0 k€**, soit 2,84 % du budget. Le budget, réserve comprise, atteint **5 965,0 k€** : il tient dans l'enveloppe de 6 000 k€ avec **35,0 k€** de reste (0,58 %).

| | Sans parade | Parade R1 seule | Parade R4 seule | Deux parades |
|---|---:|---:|---:|---:|
| Budget (k€) | 5 800,0 | 5 800,0 | 5 800,0 | 5 800,0 |
| Parades décidées (k€) | 0 | 50,0 | 20,0 | 70,0 |
| Réserve pour aléas (k€) | 165,0 | 141,0 | 141,0 | 117,0 |
| **Total (k€)** | **5 965,0** | **5 991,0** | **5 961,0** | **5 987,0** |
| Reste sous l'enveloppe de 6 000 k€ | 35,0 | 9,0 | 39,0 | 13,0 |

- **Parade R1** (fabrication prioritaire et livraison en deux lots, 50 k€). Le risque devient : probabilité 10 % (niveau 1), retard sur la fin de 3 semaines (niveau 3), surcoût de 80 k€ (niveau 2), gravité 3, **criticité 3** : il devient faible et sort de la réserve (− 24 k€). Le surcoût net est de 50 − 24 = **26 k€**. Mais le retard possible ne dépasse plus la marge sur le jalon : même si le risque survient, les premières séries sortent en septembre 2028. Sans parade, il y a 30 % de chances de perdre 2 semaines de saison de chauffe, soit une perte espérée de 0,30 × 2 × 60 = **36 k€** de marge, que le budget du projet ne montre pas. La parade se justifie donc.
- **Parade R4** (éprouvettes brasées et contrôlées pendant la formation, 20 k€). La probabilité tombe à 20 % (niveau 2) : la **criticité passe de 9 à 6**, et le coût espéré de 48 à 24 k€. La parade coûte 20 k€ et réduit la réserve de 24 k€ : elle **rapporte 4 k€** et améliore la qualité, puisque les défauts de brasage sont repérés avant la qualification.
- Avec les deux parades, le total atteint **5 987,0 k€** : il reste **13,0 k€** sous l'enveloppe (0,22 %). Avec en plus l'intérimaire envisagé à la question 2.2 (10,5 k€ de surcoût), le total serait de 5 997,5 k€ : il ne resterait que 2,5 k€, l'enveloppe serait épuisée.

Conclusion : le projet tient dans l'enveloppe de VESTRAHOLM, parades comprises, mais sans réserve supplémentaire. Les deux parades sont à décider ; tout nouvel aléa devra être couvert par la réserve, et non par l'enveloppe.

**Réponses tolérées**
- Réserve calculée en incluant les risques faibles (180,5 k€ : total 5 980,5 k€), si le candidat l'annonce comme une prudence et conclut de façon cohérente ; la convention de l'annexe 2.4 les exclut.
- Appréciation de la parade R1 sans la perte de marge du directeur industriel, si la protection du jalon est mise en avant.
- Budget présenté par lot sans le tableau par tâche, si les calculs intermédiaires (heures, composants) sont visibles.

**Erreurs fréquentes**
- `JUR-P02` — Ne pas appliquer la convention de l'annexe : coter la gravité sur le seul surcoût, ou prendre le retard de la tâche au lieu du retard sur la fin du projet (marge non déduite).
- `JUR-T10` — Additionner les surcoûts au lieu des coûts espérés ; multiplier le pourcentage de probabilité par la gravité ; oublier les heures internes dans le budget.
- `JUR-T05` — Juger une parade sur son seul coût, sans son effet sur la réserve, sur l'enveloppe et sur le jalon de septembre 2028.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 791-798 : plan de financement (budget) du projet ; triptyque QCD ; risques du projet) ; guide p. 121 | budget par tâche et par lot, réserve pour aléas | [V] | F05 § 2, § 3, § 6 |
| Programme UE 3, partie 2.5 (l. 837 : « notion de criticité des risques ») ; guide p. 123 (cartographie et criticité) | cotation, hiérarchisation | [V] | F08 § 2 ; F13 § 6 |
| Criticité = probabilité × gravité (pratique sans auteur) ; risque net après les parades déjà décidées | registre des risques | [S] | F08 § 2.1 |

---

### 2.4 Note au comité de pilotage (20 lignes au maximum) (1,5 pt)

**Compétences visées :**
- `2.2.e` — Produire une synthèse rédigée et structurée concernant le pilotage du projet (reporting au comité de pilotage : avancement, dérives, décisions proposées)
- `2.2.d` — Analyser les résultats obtenus (risques du projet, actions correctives, revues d'avancement)
- `2.5.d` — Élaborer des préconisations permettant de gérer les risques (préconisations hiérarchisées selon la criticité)

**Barème (1,5 pt)** — grille de notation d'une réponse rédigée (six critères : concept défini et attribué ; mobilisation pertinente ; faits du cas ; analyse et non description ; préconisation faisable ; forme et longueur).

| Note | Descripteur |
|---:|---|
| 0 | Absence de réponse, hors sujet ou cours récité sans aucun fait du cas |
| 0,5 | Note qui résume les calculs sans prise de position, ou qui dépasse nettement les 20 lignes |
| 1 | Date, ressource critique, budget et réserve présentés avec leurs chiffres clés, mais sans décisions sur les parades, sans revues de projet ou sans arbitrage entre qualité, coût et délai |
| 1,5 | Six critères satisfaits : note structurée (objet, délai, ressource critique, budget et risques, décisions et revues, conclusion) ; chiffres clés repris sans recalcul (70 semaines et 4 de marge, E décalée de 8 semaines, 5 800 k€, réserve de 165 k€, 5 987 k€ avec les parades pour 6 000 k€, R1 et R4 majeurs) ; parades et arbitrages argumentés ; revues de projet datées jusqu'au bilan de fin de projet ; 20 lignes au maximum |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : une note de **reporting de projet** au comité de pilotage, organisée selon le triptyque **qualité, coût, délai** : situation, risques, décisions demandées, revues prévues. Elle hiérarchise les décisions selon la criticité des risques.
- Alternatives acceptées : présentation par feux (vert, orange, rouge) sur les axes qualité, coût et délai, si les phrases de liaison et la conclusion existent ; une seule parade recommandée, ou le recours à un intérimaire, si le choix est argumenté par les chiffres de la question 2.3 et confronté à l'enveloppe ; un calendrier des revues différent, s'il couvre le lancement, les étapes clés, la qualification et le bilan de fin de projet.

**Réponse attendue** (modèle de note, 20 lignes au maximum)

**Objet : projet « ligne C-NAT », planning, budget et risques.**

**1. Délai.** Le projet dure 70 semaines : qualification le 4 août 2028, 4 semaines avant le jalon du 1er septembre. Les premières séries sortiront en septembre, mais le chemin critique dépend pour 28 semaines du fournisseur des postes de brasage.

**2. Ressource critique.** Les cinq techniciens des méthodes sont le goulet : au plus tôt, il en faudrait six pendant 10 semaines. Décaler de 8 semaines l'aménagement du bâtiment lève ce dépassement, sans coût ni retard ; le bâtiment ne garde que 4 semaines de marge.

**3. Budget et risques.** Budget de 5 800 k€ ; la réserve de 165 k€, tirée du registre des risques, porte le total à 5 965 k€ pour une enveloppe de 6 000 k€. Deux risques sont majeurs : livraison des postes (R1), fuites aux brasures (R4).

**4. Décisions.** Décider les deux parades : postes en fabrication prioritaire (50 k€), qui protège la saison de chauffe, et éprouvettes en formation (20 k€), qui se paie ; total 5 987 k€. Garder sept semaines de qualification.

**5. Revues.** Aux jalons : commandes (août 2027), postes livrés (février 2028), présérie (juin 2028), qualification (août 2028) ; point mensuel chez le fournisseur ; bilan de fin de projet fin 2028.

**Conclusion.** Projet tenable et finançable, à piloter sur les postes de brasage et la charge des méthodes.

*Éléments attendus dans la note.*
- **Arbitrages entre qualité, coût et délai.** Raccourcir la qualification de 7 à 5 semaines (proposition de la cheffe du projet) gagnerait du délai au détriment de la qualité, sur un produit chargé d'un fluide inflammable, alors que la marge de 4 semaines existe et que R4 est déjà majeur : à refuser. Dépenser 50 k€ pour protéger le délai (parade R1) est justifié par l'enjeu de la saison de chauffe. Le lissage préserve le coût au prix de la marge du bâtiment.
- **Revues de projet.** Revue de lancement (comité de mars 2027) ; revues aux jalons du chemin critique et aux fins de lot ; revue des engagements à la fin de la consultation, quand 68 % du budget est engagé ; revue de qualification, qui autorise ou non les premières séries ; **bilan de fin de projet** (post-mortem), quelques mois après les premières séries : coûts réels par lot contre budget, réserve consommée, risques survenus, retour d'expérience pour les prochaines lignes.

**Réponses tolérées**
- Décision différente sur les parades ou sur l'intérimaire, si elle est argumentée par les chiffres de la question 2.3 et respecte l'enveloppe.
- Calendrier des revues différent, s'il suit les jalons du projet et se termine par un bilan de fin de projet.

**Erreurs fréquentes**
- `JUR-T05` — Traiter le délai, le coût et les risques séparément, sans arbitrage entre qualité, coût et délai.
- `JUR-T06` — Dépasser les 20 lignes ; absence de structure ou de conclusion.
- `JUR-T03` — Résumer les calculs sans décisions demandées au comité ni revues de projet.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 794 : revues d'avancement ; l. 797-798 : cycle de vie, conception, exécution et post-mortem ; l. 806 : tableau de bord du projet et reporting) ; guide p. 121 | note de reporting, revues, bilan de fin de projet | [V] | F05 § 2, § 7 |
| Programme UE 3, partie 2.5 ; guide p. 123 (préconisations hiérarchisées selon la criticité) | parades à décider | [V] | F08 § 2.1, § 5 |
| Grille à six critères des réponses rédigées | notation | [V] | gabarits/corrige_ue3_template.md ; bareme_grille.yaml |

---

## Contrôles avant publication

- [x] `python3 -I outils/dscgcheck ue3/exercices/ex27_industrialisation_ligne_assemblage/corrige.yaml` : 0 erreur, 0 avertissement ; planning, charge des méthodes au plus tôt et lissée (profil recalculé en semaines-technicien), budget par tâche recalculés ; budget par lot et par nature, cotation des risques, réserve pour aléas et parades : calculs divers recalculés par script (`/paperclip/shared/dscglab-travail/DSC-761/calculs.py`, qui énumère aussi tous les calendriers lissés possibles) ; barème partiel sur 7 ; liste noire ; hors-programme.
- [x] Données partagées du sujet n° 10 respectées : 36 salariés au bureau d'études et aux méthodes (24 + 12), premières séries en septembre 2028, enveloppe accordée par VESTRAHOLM ; présentation commune reprise mot pour mot.
- [x] Compétences visées présentes dans `programme/perimetre_ue3.yaml` ; aucun outil prescrit dans l'énoncé ; chaque question présente le concept, l'applique au cas, conclut ; synthèse bornée (2.4, 20 lignes au maximum).
- [x] Entités et personnes fictives (Mme Maëlle CORBASSIÈRE, M. Grégoire VALDORIEUX, Mme Inès LAUZARDIÈRE ; fournisseurs, sous-traitant et entreprise de travaux non nommés) ; attributions limitées à F13 ; aucune réglementation réelle des fluides inflammables ni des équipements ; ni valeur acquise, ni accélération au moindre coût, ni budget des décaissements par période, ni actualisation ou critère de choix d'investissement, ni règle de droit des contrats ou du travail.
