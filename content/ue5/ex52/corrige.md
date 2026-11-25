# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 52 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique (§ 0, veille technologique ; § 5, maturité numérique), F02 gouvernance et référentiels (§ 1, norme, référentiel et solution ; § 2, gouvernance et management ; § 3, COBIT 2019 ; § 6, comitologie), F03 architecture et urbanisation (§ 1, urbanisation et rationalisation des processus ; § 3, intégration entre applications), F05 projets et changement (§ 1, acteurs et RACI ; § 2, méthodes ; § 4, planification ; § 6, qualité, recette et mise en production), glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 La veille technologique et deux technologies de l'alerte | `1.1.d` Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 3 |
| 1.2 La capacité des processus et les parties prenantes de la gouvernance du système d'information | `1.2.d` Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) ; `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité | 3 |
| 1.3 Le processus des volontaires et sa rationalisation | `1.3.f` Analyse des processus métiers et rôle des architectures SI dans leur rationalisation ; `1.3.a` Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) | 2,5 |
| 1.4 La méthode et l'organisation du projet VIGIE | `1.5.b` Méthodologies de gestion de projet (cycle en V, agile, hybride) ; `1.5.a` Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable | 3 |
| 1.5 La planification et le plan qualité du projet VIGIE | `1.5.d` Planification des ressources, délais, coûts et qualité ; `1.5.f` Mise en œuvre et contrôle du plan qualité | 2,5 |
| **Dossier 1 – Préparer la gouvernance du système d'information et la conduite du projet VIGIE** |  | **14** |

Répartition indicative : connaissances (veille technologique, modèles de maturité et de capacité, processus métier, méthodes de projet, plan qualité) environ 2,5 points (items 1.1 a-1, 1.2 a-1, 1.3 a-1 pour moitié, 1.4 a-1, 1.5 b-1 pour moitié, et les définitions incluses dans les autres items) ; analyse des annexes et recommandations environ 11,5 points, soit environ 82 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – La veille technologique et deux technologies de l'alerte (3 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.d` « Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limite : « Ne pas se limiter à une veille passive : intégrer l'analyse prospective dans l'évaluation des opportunités SI. »

**Annexes mobilisées** : annexes 1.2 (deux technologies, absence de veille), 1.1 (activité, délais d'arrivée, organigramme) et 1.3 (absence d'instance consacrée au SI).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Veille technologique définie : surveillance **active**, organisée et continue des technologies et des usages, pour en anticiper les effets sur l'organisation et éclairer des décisions ; distinguée de la simple réception d'informations (veille passive, situation actuelle du SDIS, annexe 1.2 C) | 0,5 |
| a-2 | Objets surveillés et sources adaptés au SDIS (technologies de l'alerte, de la mobilité et de l'engagement des volontaires ; autres SDIS, partenaires, publications, données internes des appels), avec un regard critique sur les éditeurs | 0,5 |
| a-3 | Acteurs (pilote, contributeurs des groupements, du centre de traitement de l'alerte et du service de santé), diffusion (fiche courte, rythme) et décision (instance qui écarte, surveille, expérimente ou adopte, selon des critères tirés du projet d'établissement) | 0,5 |
| b-1 | Vidéo transmise par l'appelant : effets sur la prise de l'appel, la décision d'engagement et la charge des opérateurs, tirés des chiffres de l'annexe 1.2 A, et contribution aux objectifs (délai et gestes en attendant les secours, partage avec le centre de régulation médicale), limites (réseau du Haut-Aurande, images de personnes) | 0,5 |
| b-2 | Alertes automatiques : même analyse (3 000 alertes, doublées depuis 2024, six sur dix fausses, cinq minutes de levée de doute, formats hétérogènes, 40 personnes seules secourues grâce à elles) et contribution aux objectifs | 0,5 |
| b-3 | Une suite recommandée et justifiée pour chacune : expérimentation encadrée de la vidéo, avec des critères et des règles sur les images ; organisation du filtrage et d'un format commun des alertes automatiques avec leurs émetteurs, puis étude de leur intégration | 0,5 |

**Réponse attendue**

*1.1 a) – La veille technologique et son organisation*

La **veille technologique** est une démarche **active**, organisée et continue de recherche, de sélection, d'analyse et de diffusion d'informations sur les technologies et sur leurs usages, afin d'anticiper leurs effets sur l'organisation, son modèle et ses métiers, et d'éclairer des décisions : écarter, surveiller, expérimenter ou adopter. Elle se distingue d'une **veille passive**, qui se contente de recevoir ce qui arrive. C'est la situation du SDIS : « Personne n'en est chargé » ; l'information vient des éditeurs qui démarchent, de collègues ou d'un écho dans la presse, et aucune instance ne décide (annexe 1.2 C) (0,5 pt).

**Organisation proposée pour le SDIS** :

| Composante | Proposition pour le SDIS du Val-d'Aurande |
|---|---|
| **Ce qu'elle surveille** (0,5 pt avec les sources) | technologies de la réception et du traitement de l'alerte (vidéo, alertes automatiques, localisation de l'appelant, messages écrits) ; technologies de terrain et de mobilité des équipages ; outils d'engagement et de gestion des volontaires ; usages des appelants et des partenaires ; offres des éditeurs du marché ; résultats des essais des autres SDIS |
| **Sources** | retours d'expérience des SDIS voisins et réseaux professionnels ; partenaires (centre de régulation médicale du SAMU, plateformes de téléassistance, opérateurs de réseaux mobiles) ; publications professionnelles et salons, avec un regard critique sur les présentations des éditeurs, qui vendent ; **données internes** : statistiques des appels et des alertes automatiques, cahier des incidents, réclamations des volontaires |
| **Acteurs** (0,5 pt avec la diffusion et la décision) | pilote : le groupement « Pilotage et systèmes d'information » (observatoire de l'activité et service des systèmes d'information et de communication), avec un correspondant nommé ; contributeurs : centre de traitement de l'alerte (Mme TOURNEVAL), groupement des opérations, groupement du volontariat, service de santé et de secours médical pour les usages médicaux de la vidéo, déléguée à la protection des données pour les images et les données personnelles ; un référent par groupement territorial |
| **Diffusion** | une fiche courte par technologie (description, maturité, essais connus, effets attendus sur l'alerte et sur les objectifs du projet d'établissement, risques, avis) ; une synthèse trimestrielle ; un espace partagé où sont rangées les fiches |
| **Décision** | les fiches sont présentées à l'instance de gouvernance du SI (question 1.2 c), qui décide d'**écarter**, de **surveiller**, d'**expérimenter** (avec des critères de réussite et une durée) ou d'**adopter** (le projet entre alors dans les projets du SI) ; chaque décision est notée et revue |

La veille devient ainsi **prospective** : elle évalue chaque technologie au regard des objectifs de « Val-d'Aurande Secours 2031 », au lieu de subir l'offre des éditeurs.

*1.1 b) – Les effets des deux technologies et leur suite*

**La vidéo transmise par l'appelant** (0,5 pt) :
- **prise de l'appel** : l'opérateur voit la scène au lieu de l'imaginer ; il évalue mieux la gravité et peut guider les gestes de l'appelant en attendant les secours (massage cardiaque, position de la victime) ;
- **décision d'engagement** : la décision change une fois sur huit quand la vidéo fonctionne, dans les deux sens : un moyen plus lourd pour une détresse sous-estimée, ou un simple conseil sans engin, ce qui préserve des engins et des volontaires disponibles ;
- **charge des opérateurs** : deux minutes de plus par appel avec vidéo ; à généraliser, il faudrait cibler les appels (détresse vitale, incendie, accident) pour ne pas allonger l'attente des autres appelants ;
- **contribution aux objectifs** : elle sert d'abord la qualité de la réponse et le délai « utile » (gestes réalisés avant l'arrivée des secours), plus que le délai d'arrivée lui-même ; elle peut nourrir le partage avec le centre de régulation médicale du SAMU ;
- **limites** : elle fonctionne quatre fois sur dix seulement en montagne, c'est-à-dire dans le Haut-Aurande, là où les secours arrivent en plus de 20 minutes et où elle serait la plus utile ; les images de personnes blessées ou en détresse appellent des règles d'affichage, d'accès et de conservation, à fixer avec la déléguée à la protection des données.

**Les alertes automatiques des objets connectés** (0,5 pt) :
- **prise de l'appel** : un nouveau canal sans voix humaine, en forte croissance (3 000 alertes en 2026 contre 1 500 en 2024, soit 2 % des 150 000 appels), qui arrive par des voies et des formats différents, hors du logiciel de traitement de l'alerte : l'opérateur ressaisit, avec un risque d'erreur sur la position ;
- **décision d'engagement** : six alertes sur dix sont fausses ; chacune exige une **levée de doute** avant d'engager ; mais la position transmise peut accélérer la localisation, et 40 fois en 2026, dont une vingtaine dans le Haut-Aurande, l'alerte automatique a été le seul signal d'une personne seule ;
- **charge des opérateurs** : 1 800 fausses alertes × cinq minutes, soit environ 150 heures d'opérateur par an (environ 250 heures pour l'ensemble des 3 000 levées de doute) : une charge encore modeste, mais qui a doublé en deux ans ; la fiabilité dépend de l'émetteur : neuf sur dix fausses pour les montres, une sur quatre pour la téléassistance, qui filtre déjà ;
- **contribution aux objectifs** : délai d'arrivée des secours pour des personnes âgées ou isolées, en particulier dans le Haut-Aurande ; continuité du traitement de l'alerte, à condition que ces alertes ne saturent pas les opérateurs.

**Suites recommandées** (0,5 pt) :
- **vidéo : expérimenter, de façon encadrée**, pendant six mois au centre de traitement de l'alerte, sur des appels ciblés, avec des critères fixés d'avance (part des vidéos réussies par secteur, décisions modifiées, durée des appels, avis des opérateurs et du médecin-chef) et des règles sur les images (affichage limité au poste de l'opérateur, accès restreint, pas de conservation par défaut), puis décider de l'adopter ou non devant l'instance de gouvernance du SI ; ne pas en attendre une réponse au délai du Haut-Aurande, faute de réseau ;
- **alertes automatiques : organiser plutôt que subir** : demander aux émetteurs, d'abord aux plateformes de téléassistance, puis aux services associés aux montres et aux voitures, une première levée de doute et un **format commun** (identité, position, type d'événement) ; écrire au centre une procédure unique de levée de doute ; suivre leur volume et leur part de fausses alertes ; étudier ensuite, dans la veille, leur réception directe dans le logiciel de traitement de l'alerte.

**Réponses tolérées**
- Veille organisée autour d'un cycle (cibler, collecter, analyser, diffuser, décider), si chaque étape est appliquée au SDIS.
- Pilotage de la veille confié au centre de traitement de l'alerte ou au groupement des opérations, si la décision reste à une instance de direction et si le SI y est associé.
- Vidéo recommandée en adoption progressive plutôt qu'en expérimentation, si la charge des opérateurs et les règles sur les images sont traitées.
- Alertes automatiques analysées sous l'angle d'un partenariat avec les plateformes de téléassistance : accepté.

**Erreurs fréquentes**
- *Veille réduite à une liste de sources ou à un abonnement* (ET-39 morceau de cours ; limite du programme 1.1 : « ne pas se limiter à une veille passive ») — sans acteurs, diffusion et décision, la veille reste ce qu'elle est aujourd'hui.
- *Technologies présentées par leurs seuls avantages* (ET-19 opportunités sans risques) — la vidéo échoue six fois sur dix en montagne, et six alertes automatiques sur dix sont fausses.
- *Effets décrits sans les chiffres de l'annexe 1.2 ni lien avec les objectifs* (`JUR-T08` exploiter toutes les annexes ; `JUR-T03` analyser et argumenter) — l'analyse doit dire ce que chaque technologie change à la prise de l'appel, à l'engagement et à la charge.
- *Choix technique du produit vidéo, ou analyse juridique des images* (`JUR-T07` répondre à la seule question posée) — non demandés ; les images appellent des règles, à fixer avec la déléguée à la protection des données.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Veille technologique | veille active et prospective, effets sur le modèle de l'organisation | F01 § 0 ; glossaire | notion de cours |
| Technologies émergentes et stratégie du SI | opportunités et risques, décision d'expérimenter | F01 § 0 ; `erreurs_types.md` ET-19 | notion de cours |

---

### 1.2 – La capacité des processus et les parties prenantes de la gouvernance du système d'information (3 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.d` « Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) » ; `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ».

**Annexes mobilisées** : annexes 1.3 (témoignages), 1.4 (grille de capacité), 1.7 (COBIT 2019), 1.1 (gouvernance, organigramme, dépenses du SI) et 1.5 (volontaires).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Modèle de maturité (niveaux successifs de maîtrise d'un ensemble de pratiques ou d'une organisation) et modèle de capacité (aptitude d'un processus pris isolément à atteindre son objectif, COBIT 2019 de 0 à 5) définis et distingués ; usages : diagnostic partagé, cible, priorités, suivi des progrès, communication à la direction | 0,5 |
| a-2 | Deux processus positionnés, chacun justifié par un constat de l'annexe 1.3 confronté à la grille de l'annexe 1.4 | 0,5 |
| a-3 | Les deux autres processus, même exigence ; positionnement différencié et cohérent avec la règle de l'annexe 1.4 | 0,5 |
| b-1 | Niveaux cibles à deux ans réalistes (un ou deux niveaux de progrès), plus ambitieux pour les processus qui touchent la continuité de l'alerte et le projet VIGIE ; niveaux 4 et 5 écartés et justifiés le cas échéant | 0,5 |
| b-2 | Une action prioritaire par processus, concrète et reliée au constat | 0,5 |
| c-1 | Deux instances ou mesures qui associent le conseil d'administration, les groupements territoriaux et les volontaires (composition, fréquence, rôle), en réponse aux témoignages | 0,5 |

**Réponse attendue**

*1.2 a) – Maturité, capacité et positionnement des quatre processus*

Un **modèle de maturité** décrit, par une échelle de niveaux successifs, le degré d'organisation et de maîtrise atteint par une organisation ou par un ensemble de pratiques (un domaine), du plus informel au plus maîtrisé ; MAGNum 2026, du Cigref, de l'IFACI et de l'ISACA France, en est un exemple pour la gouvernance du numérique. Un **modèle de capacité** évalue un **processus pris isolément** : son aptitude à atteindre son objectif, de façon plus ou moins organisée, mesurée et améliorée ; COBIT 2019, référentiel de gouvernance de l'ISACA et non norme, note la capacité des processus de 0 (incomplet) à 5 (optimisé) (annexes 1.4 et 1.7). Les deux notions se complètent : la maturité d'un domaine se déduit de la capacité des processus qui le composent. **Usages** : établir un diagnostic partagé et objectivé, fixer une cible, choisir les priorités d'action, suivre les progrès d'une année à l'autre et en rendre compte à la direction et au conseil d'administration. Limite : une auto-évaluation peut être complaisante ; elle doit s'appuyer sur des faits (0,5 pt).

**Positionnement** (0,5 pt pour deux processus, 0,5 pt pour les deux autres) :

| Processus | Constats (annexe 1.3) | Niveau | Justification par la grille (annexe 1.4) |
|---|---|---|---|
| **Gestion des projets** | aucune méthode écrite ; chaque groupement lance ses projets puis demande au service de les installer ; deux projets abandonnés depuis 2022 (planning des gardes non relié au logiciel des disponibilités, portail des formations doublé par la plateforme de formation) ; des projets aboutissent pourtant (tablettes) | **1 – Initial** | l'objectif est atteint en partie, au cas par cas, selon les personnes ; ni planification ni suivi communs, donc pas le niveau 2 |
| **Gestion des incidents et des changements** | astreinte jour et nuit des quatre agents du soutien, incidents toujours pris en charge et notés dans un cahier ; mais cahier jamais relu, pannes qui reviennent ; mises à jour des éditeurs installées le soir, sans test ni retour arrière, avec deux interruptions d'une heure de la transmission des disponibilités en 2026 | **1 – Initial** | la prise en charge des incidents approche le niveau 2 (activité planifiée, responsables identifiés), mais la gestion des changements n'atteint pas son objectif ; le processus, pris comme un tout, reste au niveau 1 |
| **Gestion de la sécurité** | une charte d'usage signée par chaque agent à son arrivée ; aucune analyse des risques ; personne n'est désigné | **1 – Initial** | la charte, signée par chaque agent à son arrivée, atteint en partie l'objectif (faire connaître aux agents leurs obligations), mais au cas par cas, sans responsable ni analyse des risques : pas le niveau 2 |
| **Gestion des données** | chaque groupement tient ses tableurs ; aucun propriétaire désigné ; trois chiffres pour les volontaires : 3 900 au groupement du volontariat, 4 300 comptes actifs dans le logiciel des disponibilités, 3 800 dans les tableurs des groupements territoriaux | **0 – Incomplet** | les tableurs sont des activités locales, utiles à chaque groupement seulement ; l'objectif du processus, une donnée de référence fiable et partagée, n'est pas atteint, même en partie : trois chiffres différents, et aucune donnée ne fait foi |

Conclusion : la gouvernance du SI est faiblement maîtrisée ; aucun processus n'atteint le niveau 2, alors que le SI porte un service critique, ouvert jour et nuit.

*1.2 b) – Niveaux cibles à deux ans et actions prioritaires*

**Principe** (0,5 pt) : progresser d'un ou deux niveaux en deux ans, jusqu'en mai 2029, un niveau ne s'atteignant qu'après les précédents ; viser plus haut là où la continuité de l'alerte et le projet VIGIE l'exigent ; écarter les niveaux 4 et 5, qui supposent une mesure et une amélioration continues hors de portée de 12 informaticiens et inutiles à ce stade.

**Cibles et actions** (0,5 pt pour les actions) :

| Processus | Niveau actuel → cible à deux ans | Justification de l'ambition | Action prioritaire |
|---|---|---|---|
| Gestion des projets | 1 → **3** | VIGIE doit aboutir avant la fin de 2028 ; les échecs viennent de projets lancés sans cadre commun | adopter une **méthode de projet écrite et commune** (note de cadrage, commanditaire, comité de pilotage, jalons, bilan), appliquée d'abord à VIGIE, et soumettre tout projet du SI à l'instance de gouvernance avant son lancement |
| Gestion des incidents et des changements | 1 → **3** | objectif de continuité du traitement de l'alerte, jour et nuit ; les bases existent (astreinte, cahier) | remplacer le cahier par un **registre partagé des incidents**, classés par gravité et analysés chaque mois pour traiter les pannes qui reviennent ; **tester toute mise à jour** avant son installation, avec un retour arrière prévu et l'accord du centre de traitement de l'alerte |
| Gestion de la sécurité | 1 → **2** | partir d'une activité isolée : il faut d'abord un responsable et des activités planifiées | **désigner un responsable de la sécurité du SI** et lui confier un plan d'actions suivi par la direction, fondé sur une première analyse des risques |
| Gestion des données | 0 → **2** | VIGIE va créer une source fiable des disponibilités et des heures ; un niveau 3 en deux ans serait irréaliste | **désigner un propriétaire pour chaque domaine de données** (volontaires : groupement du volontariat ; interventions : groupement des opérations…) et fixer la source qui fait foi pour l'effectif des volontaires, en retirant les comptes des partants |

*1.2 c) – Associer le conseil d'administration, les groupements territoriaux et les volontaires*

(0,5 pt ; deux parmi les suivantes)
1. **Un comité du système d'information**, instance du comité de direction présidée par le directeur départemental, réuni chaque trimestre : chefs des groupements fonctionnels **et des quatre groupements territoriaux**, cheffe du service des systèmes d'information et de communication, déléguée à la protection des données, et un **administrateur référent du numérique** désigné par le conseil d'administration. Il arbitre les projets du SI, examine les fiches de veille, suit la capacité des processus et les risques. Le conseil d'administration reçoit chaque année, avant le vote du budget, un **rapport sur le système d'information** : projets et résultats (les tablettes, par exemple), capacité des processus, indicateurs de performance et d'empreinte environnementale. C'est la réponse au président : le conseil ne verra plus les 3,6 M€ comme « une ligne parmi d'autres ».
2. **Un comité des utilisateurs du SI**, prolongement du panel de VIGIE : chefs de centre et volontaires des quatre groupements territoriaux, réunis deux fois par an le soir, consultés avant tout projet qui les touche (outils des volontaires, des centres, des engins) et associés aux essais ; deux de ses membres siègent au comité du SI. C'est la réponse au chef de centre du Haut-Aurande, qui a découvert les tablettes le jour de leur livraison.
3. Variante : une **consultation annuelle des volontaires** sur leurs outils (questionnaire sur l'application, réunions dans les centres), dont les résultats sont présentés au comité du SI et au conseil d'administration.

**Réponses tolérées**
- Gestion des incidents et des changements placée au niveau 2, si le candidat distingue la prise en charge des incidents (planifiée, avec une astreinte) et les changements non testés, et en fait le premier point à corriger.
- Gestion de la sécurité placée au niveau 0, si le candidat juge que la charte ne suffit pas à constituer un processus ; gestion des données placée au niveau 1, si les tableurs sont vus comme des activités au cas par cas.
- Cibles différentes (sécurité à 3, données à 3), si elles sont justifiées et si la progression reste réaliste ; cible de 2 pour tous, si elle est présentée comme une première étape.
- Modèle de maturité illustré par CMMI ou par MAGNum 2026, sans en faire la grille de positionnement, qui est celle de l'annexe 1.4.
- Mention d'ITIL pour la gestion des incidents et des changements, s'il est présenté comme un référentiel de bonnes pratiques de gestion des services, et non comme une norme.

**Erreurs fréquentes**
- *Maturité et capacité confondues sans explication* (F01 § 5 et F02 § 3 : COBIT 2019 évalue la capacité de chaque processus, de 0 à 5 ; `JUR-T01` contextualiser chaque notion) — la grille de l'annexe 1.4 évalue des processus, un par un.
- *Niveaux attribués sans constat, ou tous identiques* (`JUR-T08` exploiter toutes les annexes ; `JUR-T03` analyser et argumenter) — chaque niveau se justifie par un fait de l'annexe 1.3 confronté à la description du niveau.
- *Cibles irréalistes* (niveau 4 ou 5 en deux ans, saut de trois niveaux) (`JUR-G05` recommander de façon réaliste) — un niveau ne s'atteint qu'après les précédents.
- *COBIT 2019 présenté comme une norme ou comme un logiciel* (ET-01 norme, référentiel et solution ; `JUR-S06`) — c'est un référentiel de gouvernance, publié par l'ISACA.
- *Instances sans les volontaires ni le conseil d'administration* (`JUR-T07` répondre à la question posée) — la question vise précisément ces parties prenantes.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| COBIT 2019 (ISACA) | référentiel de gouvernance ; capacité des processus de 0 à 5 | `cobit_2019` ; F02 § 3 | en vigueur |
| MAGNum 2026 (Cigref, IFACI, ISACA France) | exemple de modèle de maturité de la gouvernance du numérique | `magnum_2026` ; F01 § 5 | en vigueur |
| CMMI (réponse tolérée) | modèle de maturité en cinq niveaux | `cmmi_v3` ; F01 § 5 | en vigueur |
| ITIL (réponse tolérée) | gestion des incidents et des changements | `itil_4`, `itil_5` ; F02 § 5 | en vigueur |
| Comitologie du SI | comité du SI, parties prenantes | F02 § 6 | notion de cours |

---

### 1.3 – Le processus des volontaires et sa rationalisation (2,5 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.f` « Analyse des processus métiers et rôle des architectures SI dans leur rationalisation » ; `1.3.a` « Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) ». Limite : « Ne pas réduire l'urbanisation à une vision strictement technique : elle s'inscrit dans une stratégie globale. »

**Annexes mobilisées** : annexes 1.5 (processus actuel), 1.6 (objectif de VIGIE et lots), 1.3 (trois chiffres des volontaires, interruptions après mise à jour) et 1.1 (système d'information, centres, indemnités).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Processus métier défini (suite ordonnée d'activités, réalisées par des acteurs avec des outils, qui produit un résultat pour un bénéficiaire) ; processus actuel représenté de façon lisible : acteurs, étapes, outils, ressaisies signalées | 0,5 |
| a-2 | Trois dysfonctionnements tirés de l'annexe 1.5, chacun avec ses effets sur l'engagement, sur les volontaires ou sur l'établissement | 0,5 |
| b-1 | Processus cible avec VIGIE : déclaration par l'application, disponibilité vue aussitôt au centre, équipage enregistré une fois au départ, heures transmises et validées, rôle des chefs de centre et des finances recentré sur le contrôle | 0,5 |
| b-2 | Rationalisation par l'architecture : échanges automatiques entre VIGIE, le logiciel de traitement de l'alerte et le logiciel des indemnités (nature et rythme), donnée saisie une seule fois à la source | 0,5 |
| b-3 | Deux conditions de réussite parmi : source unique de la liste des volontaires, fonctionnement en zone mal couverte, mode dégradé si une interface tombe (sans lequel la ressaisie reviendrait) | 0,5 |

**Réponse attendue**

*1.3 a) – Le processus actuel et ses dysfonctionnements*

Un **processus métier** est une suite ordonnée d'activités, réalisées par des acteurs avec des outils et des informations, qui transforme une demande en un résultat pour un bénéficiaire : ici, un volontaire disponible, engagé à bon escient, puis indemnisé de ses heures. On le représente par ses étapes, ses acteurs et ses outils, pour en repérer les ruptures (0,5 pt avec la représentation).

**Représentation du processus actuel** (format libre lisible : tableau, schéma en couloirs ou logigramme) :

| Étape | Acteur | Outil | Ressaisie ou rupture |
|---|---|---|---|
| 1. Déclarer sa disponibilité | volontaire | SMS codé (45 %), site web (35 %), téléphone au chef de centre (20 %) | **ressaisie** par le chef de centre des déclarations téléphoniques ; SMS mal formés rejetés sans toujours prévenir |
| 2. Transmettre les disponibilités au centre de traitement de l'alerte | logiciel des disponibilités | fichier toutes les trente minutes vers le logiciel de traitement de l'alerte | **décalage** : disponibilités parfois périmées |
| 3. Proposer et engager les moyens, alerter les volontaires | opérateur du centre de traitement de l'alerte | logiciel de traitement de l'alerte | un appel sur dix vers un volontaire qui n'est plus disponible : alerter un autre centre |
| 4. Partir : noter l'équipage | chef d'agrès | feuille de départ papier | **rupture numérique** |
| 5. Enregistrer l'équipage | chef de centre | logiciel de traitement de l'alerte | **ressaisie** de la feuille |
| 6. Chaque mois, établir les états d'heures | chefs de centre (dix heures par mois chacun pour les 48 centres de volontaires, soit environ 480 heures par mois) | relevé dans le logiciel de traitement de l'alerte et plannings de garde sur tableur → logiciel des indemnités | **ressaisie** (recopie des heures d'intervention et de garde) |
| 7. Contrôler et corriger | groupement des finances | logiciel des indemnités | un état sur cinq corrigé, échanges avec les centres |
| 8. Payer | groupement des finances, paie | fichier mensuel vers le logiciel de paie | versement deux mois après le mois de l'intervention |
| 9. Réclamer | volontaire → groupement du volontariat | courrier, courriel | 1 200 réclamations en 2026 |

**Trois dysfonctionnements et leurs effets** (0,5 pt ; trois parmi les suivants) :
1. **Des disponibilités périmées au centre de traitement de l'alerte** : transfert par fichier toutes les trente minutes, déclarations oubliées ou rejetées ; environ un appel sur dix adressé à un volontaire qui n'est plus disponible oblige à alerter un autre centre : du temps perdu, contraire à l'objectif d'arrivée des secours sous 20 minutes, surtout dans le Haut-Aurande.
2. **Des ressaisies en cascade** : déclarations téléphoniques, feuille de départ, équipage, puis heures recopiées chaque mois ; chaque ressaisie crée des erreurs (un état sur cinq corrigé) et consomme environ 480 heures par mois de chefs de centre volontaires, prises sur leur temps et sur la formation.
3. **Un paiement lent et contesté** : versement deux mois après le mois de l'intervention, 1 200 réclamations ; c'est le premier motif d'insatisfaction des volontaires, à l'opposé de l'objectif de fidélisation par la simplification de leur engagement.
4. **Des canaux de déclaration multiples et peu fiables** : trois canaux, un code SMS à respecter, aucun retour au volontaire en cas de rejet ; la déclaration, que le projet d'établissement veut simplifier « au premier rang », est la plus compliquée.
5. **Aucune source unique des volontaires** : 3 900, 4 300 ou 3 800 selon l'outil (annexe 1.3) ; les comptes des partants restent actifs dans le logiciel des disponibilités.

*1.3 b) – Le processus cible et l'architecture qui le rationalise*

**Processus cible avec VIGIE** (0,5 pt) :
1. le volontaire déclare ou modifie sa disponibilité dans l'application VIGIE, en quelques gestes, et reçoit une confirmation ; la déclaration téléphonique au chef de centre devient l'exception ;
2. la disponibilité est transmise aussitôt au logiciel de traitement de l'alerte : l'opérateur voit l'état réel, en moins d'une minute ;
3. l'opérateur engage les moyens et alerte les volontaires par les moyens d'alerte actuels ;
4. au départ, le chef d'agrès confirme l'équipage dans VIGIE, **une seule fois** ; le logiciel de traitement de l'alerte le reçoit et horodate l'intervention ;
5. les heures d'intervention, reçues du logiciel de traitement de l'alerte, et les heures de garde, issues du planning de VIGIE, sont rapprochées automatiquement ; le chef de centre **valide** au lieu de recopier, le volontaire consulte ses heures ;
6. les heures validées sont transmises au logiciel des indemnités ; le groupement des finances contrôle les seuls écarts signalés ; le fichier mensuel vers la paie reste inchangé.

**Rôle de l'architecture du SI dans la rationalisation** (0,5 pt) :
- **des échanges automatiques** remplacent les fichiers et les recopies : VIGIE → logiciel de traitement de l'alerte (disponibilités, au fil de l'eau ; équipage confirmé au départ) ; logiciel de traitement de l'alerte → VIGIE (heures d'intervention, à la clôture de chaque intervention) ; VIGIE → logiciel des indemnités (heures validées, chaque mois ou au fil de l'eau) ; le lien existant entre le logiciel des indemnités et la paie est conservé ;
- **chaque donnée est saisie une seule fois, à sa source**, par la personne qui la connaît : la disponibilité par le volontaire, l'équipage par le chef d'agrès au départ, les heures d'intervention par le logiciel de traitement de l'alerte ; les autres applications la reçoivent au lieu de la ressaisir ;
- chaque application garde son rôle : VIGIE pour les volontaires, le logiciel de traitement de l'alerte pour l'engagement, le logiciel des indemnités pour le calcul ; c'est une démarche d'urbanisation au service d'un objectif du projet d'établissement, et non un simple changement d'outil.

**Deux conditions de réussite** (0,5 pt ; deux parmi les suivantes) :
- **une source unique de la liste des volontaires** : une source unique, désignée (par exemple le logiciel de ressources humaines), alimente VIGIE ; un départ ferme le compte partout, ce qui règle les écarts entre 3 900, 4 300 et 3 800 ;
- **un fonctionnement en zone mal couverte** : la déclaration est enregistrée sur le téléphone et transmise dès le retour du réseau, avec un message de secours ;
- **un mode dégradé** si une interface tombe : file d'attente des échanges, alerte au soutien du centre de traitement de l'alerte, reprise sans ressaisie ; sinon, la feuille de départ et la recopie reviendraient (les deux interruptions de 2026 après une mise à jour en montrent le risque).

**Réponses tolérées**
- Représentation en couloirs (BPMN ou format libre), logigramme ou tableau, si les acteurs, les outils et les ressaisies apparaissent.
- Équipage enregistré au centre de traitement de l'alerte plutôt que par le chef d'agrès, si la saisie reste unique.
- Heures transmises au logiciel des indemnités au fil de l'eau plutôt que chaque mois : accepté.
- Mention d'une plateforme d'échanges entre applications, si elle est présentée comme une option et non comme une obligation.

**Erreurs fréquentes**
- *Processus décrit sans les ressaisies ni les outils* (`JUR-G07` cartographie de processus ; `JUR-T10` schémas lisibles) — la rationalisation se voit précisément aux ressaisies supprimées.
- *Dysfonctionnements sans effets* (`JUR-T03` analyser et argumenter) — chacun se rattache à l'engagement, aux volontaires ou à l'établissement.
- *Rationalisation réduite au remplacement d'un logiciel* (ET-20 urbanisation réduite à une vision technique ; limite du programme 1.3) — c'est l'organisation des échanges et de la saisie unique qui rationalise le processus.
- *Règles de calcul des indemnités discutées* (`JUR-T07` répondre à la seule question posée) — elles ne changent pas (annexe 1.6) et ne sont pas l'objet du dossier.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Analyse des processus et urbanisation | processus métier, échanges entre applications, donnée saisie à la source | F03 § 1 et § 3 ; `erreurs_types.md` ET-20 | notion de cours |

---

### 1.4 – La méthode et l'organisation du projet VIGIE (3 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.b` « Méthodologies de gestion de projet (cycle en V, agile, hybride) » ; `1.5.a` « Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ».

**Annexes mobilisées** : annexes 1.6 (lots, acteurs, contraintes), 1.7 (The Scrum Guide), 1.5 (volontaires et chefs de centre) et 1.1 (organigramme).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cycle en V (phases descendantes de spécification et de conception, phases montantes de tests en miroir, adapté à un besoin stable), méthodes agiles (cycles courts, incréments, priorisation par la valeur, utilisateurs impliqués ; Scrum en exemple) et approche hybride (combinaison des deux selon les composants) présentés, avec leurs conditions | 0,5 |
| a-2 | Lot 1 en agile, justifié par les besoins mal connus et les essais avec les volontaires ; adaptation aux disponibilités du panel | 0,5 |
| a-3 | Lots 2 et 3 en cycle en V, justifiés par la fiabilité, les tests imposés et la stabilité du format et des règles ; projet hybride dans son ensemble, avec des jalons communs | 0,5 |
| b-1 | Maîtrise d'ouvrage (groupement du volontariat, avec le centre de traitement de l'alerte et les finances), maîtrise d'œuvre (éditeur de VIGIE et service des systèmes d'information et de communication), commanditaire et comité de pilotage (composition, fréquence, décisions) | 0,5 |
| b-2 | Place du panel : utilisateurs clés du lot 1, essais à chaque itération, représentation au comité de pilotage, relais auprès des autres volontaires | 0,5 |
| b-3 | Tableau de répartition des responsabilités (RACI ou équivalent) : cinq acteurs, quatre activités, un seul approbateur par activité, cohérent avec l'organisation proposée | 0,5 |

**Réponse attendue**

*1.4 a) – Les méthodes et le choix par lot*

**Les trois approches** (0,5 pt) :
- le **cycle en V**, méthode prédictive, enchaîne l'expression du besoin, les spécifications, la conception et la réalisation, puis remonte par des tests en miroir de chaque niveau (tests unitaires, d'intégration, recette, mise en service) ; il convient à un besoin **stable** et à une forte exigence de fiabilité et de traçabilité, mais découvre tard les écarts (effet tunnel) ;
- les **méthodes agiles** livrent le produit par **incréments** au cours de cycles courts, priorisent par la valeur et impliquent les utilisateurs en continu, pour s'adapter au besoin qui se précise ; dans Scrum, selon The Scrum Guide (novembre 2020), un Product Owner tient le carnet du produit, un Scrum Master garantit le cadre, des Developers réalisent un incrément à chaque Sprint d'un mois au plus ; elles exigent des utilisateurs disponibles ;
- l'**approche hybride** combine les deux : cycle en V pour les composants stables ou critiques, agile pour ceux dont le besoin doit être découvert, avec des jalons communs.

**Choix par lot** (0,5 pt pour le lot 1, 0,5 pt pour les lots 2 et 3 et l'ensemble) :

| Lot | Méthode | Justification tirée de l'annexe 1.6 |
|---|---|---|
| Lot 1 – Application mobile des volontaires | **agile** (Scrum) | besoins mal connus (« plus simple », sans savoir quelles fonctions seront utilisées), écrans à essayer avec les volontaires au fur et à mesure ; Sprints de trois à quatre semaines, revues le soir ou le samedi avec le panel ; priorité à la déclaration de disponibilité, objectif du projet d'établissement |
| Lot 2 – Interface avec le logiciel de traitement de l'alerte | **cycle en V** | exigences de fiabilité très fortes : le traitement de l'alerte ne peut pas être perturbé ; huit semaines de tests sur la plateforme de l'éditeur puis deux semaines d'essais au centre, imposées ; spécifications à figer et tests à tracer |
| Lot 3 – Interface avec le logiciel des indemnités | **cycle en V** | règles de calcul inchangées, format d'échange connu et stable : besoin entièrement spécifiable ; l'enjeu est le contrôle de l'exactitude (zéro écart), qui se prête à des tests en miroir des spécifications |

Le projet est donc **hybride** : les incréments du lot 1 avancent en Sprints, les interfaces en cycle en V, et des **jalons communs** (spécification des données échangées, début des tests d'intégration, mise en service) synchronisent les trois lots.

*1.4 b) – L'organisation du projet*

**Organisation** (0,5 pt) :
- **commanditaire** : le directeur départemental, qui a validé la note de cadrage, arbitre et préside le comité de pilotage ;
- **maîtrise d'ouvrage** : le **groupement du volontariat**, principal bénéficiaire, qui exprime le besoin, tient le carnet du lot 1 par un **Product Owner** de son équipe et prononce la recette ; le **centre de traitement de l'alerte** (lot 2) et le **groupement des finances** (lot 3) sont maîtrises d'ouvrage associées pour leurs exigences ; le groupement « Pilotage et systèmes d'information » assure la direction du projet et la cohérence avec la gouvernance du SI ;
- **maîtrise d'œuvre** : l'**éditeur de VIGIE** (réalisation de l'application et de ses interfaces) et le **service des systèmes d'information et de communication** (intégration aux deux logiciels existants, comptes, exploitation, coordination avec l'éditeur du logiciel de traitement de l'alerte pour ses tests) ;
- **comité de pilotage**, mensuel, présidé par le directeur départemental : chefs du groupement du volontariat, du centre de traitement de l'alerte, des finances et du service des systèmes d'information et de communication, vous-même, l'éditeur de VIGIE et deux représentants du panel ; il suit l'avancement, les risques et la qualité, arbitre le périmètre et décide des mises en service ; un **comité de projet** hebdomadaire réunit les équipes.

**Place du panel des 40 volontaires** (0,5 pt) : ce sont les **utilisateurs clés** du lot 1 ; ils participent aux revues de fin de Sprint et essaient chaque version sur leur téléphone, y compris en zone mal couverte du Haut-Aurande ; ils couvrent les quatre groupements territoriaux et comptent des chefs de centre, qui valideront l'enregistrement de l'équipage et des heures ; deux d'entre eux siègent au comité de pilotage ; ils deviennent ensuite les relais du déploiement auprès des 3 900 volontaires. Leur participation est organisée le soir et le week-end.

**Répartition des responsabilités** (0,5 pt ; R = réalise, A = approuve, un seul par activité, C = consulté, I = informé) :

| Activité | Groupement du volontariat | Centre de traitement de l'alerte | Service des SI et de communication | Groupement des finances | Éditeur de VIGIE |
|---|---|---|---|---|---|
| Priorisation du carnet du lot 1 | **A**, R (Product Owner) | C | C | I | C |
| Spécification et tests de l'interface avec le logiciel de traitement de l'alerte (lot 2) | C | **A** | R | I | R |
| Spécification et contrôle des heures transmises aux indemnités (lot 3) | C | I | R | **A** | R |
| Recette fonctionnelle et préparation de la mise en service | **A**, R | R (lot 2) | R | R (lot 3) | C |

La décision de mise en service relève du comité de pilotage, présidé par le directeur départemental ; le panel est consulté pour le lot 1 et la recette.

**Réponses tolérées**
- Kanban pour le lot 1, ou méthode itérative non nommée, si les essais avec les volontaires sont au cœur de la démarche.
- Lot 3 conduit en agile court, si le candidat justifie la simplicité du lot et maintient des tests de contrôle stricts ; tout choix agile non encadré pour le lot 2 n'est pas accepté, faute de fiabilité et en raison des tests imposés.
- Maîtrise d'ouvrage confiée au groupement « Pilotage et systèmes d'information », si le groupement du volontariat est désigné comme principal représentant du métier et approbateur de la recette.
- Autres activités dans le tableau (formation, déploiement, conduite du changement) et autre choix de cinq acteurs (directeur départemental, panel), si la règle d'un seul approbateur est respectée.

**Erreurs fréquentes**
- *Une seule méthode pour tout le projet* (`JUR-P02` deux méthodes comparées dans le contexte) — les trois lots n'ont ni le même besoin ni les mêmes contraintes.
- *Agile présenté comme une absence de méthode ou de spécification* (ET-32 agile « sans cahier des charges » ; F05 § 9) — l'agilité suppose un Product Owner disponible et des incréments testés.
- *Maîtrise d'ouvrage et maîtrise d'œuvre inversées* (ET-32 MOA / MOE inversées) — le métier exprime et recette, l'éditeur et le service réalisent et intègrent.
- *Tableau avec plusieurs approbateurs par activité, ou sans lien avec les acteurs du cas* (`JUR-T01` contextualiser chaque notion) — un seul « A » par activité, et les acteurs de l'annexe 1.6.
- *Choix de l'éditeur ou contrat discutés* (`JUR-T07` répondre à la seule question posée) — l'éditeur est retenu ; aucune procédure n'est à organiser.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| The Scrum Guide (Ken Schwaber et Jeff Sutherland, novembre 2020) | Product Owner, Scrum Master, Developers ; Sprint d'un mois au plus | `scrum_guide_2020` ; F05 § 2.2 | en vigueur |
| Cycle en V, approche hybride ; acteurs, RACI | choix de la méthode par composant ; MOA, MOE, comités | F05 § 1 et § 2 ; F02 § 6 | notion de cours |

---

### 1.5 – La planification et le plan qualité du projet VIGIE (2,5 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.d` « Planification des ressources, délais, coûts et qualité » ; `1.5.f` « Mise en œuvre et contrôle du plan qualité ». Limite : « L'aspect budgétaire détaillé ne relève pas du programme de l'UE. »

**Annexes mobilisées** : annexes 1.6 (contraintes, calendrier de l'éditeur, exigences de qualité), 1.7 (ISO 9001), 1.1 (service des systèmes d'information et de communication, tablettes) et 1.5 (situation actuelle, pour les cibles).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux tensions tirées de l'annexe 1.6, chacune avec un arbitrage explicite entre ressources, délais, coûts et qualité | 0,5 |
| a-2 | Troisième tension, même exigence ; arbitrages compatibles avec les contraintes de l'annexe 1.6 (tests imposés du lot 2 maintenus, aucune mise en service touchant l'alerte entre le 15 juin et le 15 septembre) | 0,5 |
| b-1 | Plan qualité défini (document qui fixe, pour un projet, les exigences de qualité, l'organisation, les règles, les contrôles et les critères d'acceptation) ; contenu pour VIGIE : exigences rendues mesurables, rôles, revues, plan de tests, anomalies et changements, critères de mise en service | 0,5 |
| b-2 | Deux indicateurs de qualité tirés des exigences de l'annexe 1.6, chacun avec formule, source, fréquence, cible et axe | 0,5 |
| b-3 | Contrôle avant la mise en service (tests en miroir des exigences, essais en zone mal couverte, rapprochement des heures en double circuit, procès-verbal de recette) et après (suivi des indicateurs en comité, traitement des écarts) | 0,5 |

**Réponse attendue**

*1.5 a) – Trois tensions de planification et leurs arbitrages*

(0,5 pt pour deux tensions, 0,5 pt pour la troisième ; trois parmi les suivantes)

| Tension | Constat de l'annexe 1.6 | Arbitrage proposé |
|---|---|---|
| **Ressources du service des systèmes d'information et de communication** | 12 informaticiens, dont la moitié du temps va à la maintenance courante ; renouvellement des 300 tablettes de septembre à décembre 2027 ; deux informaticiens au plus pour VIGIE jusqu'à la fin de 2027, quatre ensuite | **délai plutôt que coût** : faire porter l'essentiel de 2027 par le lot 1, réalisé par l'éditeur de VIGIE avec le panel, qui demande peu au service ; lancer les interfaces (lots 2 et 3), qui le mobilisent, en janvier 2028 ; ne recourir à un renfort de l'éditeur (coût supplémentaire) que si un jalon glisse ; ne pas réduire les tests (qualité) |
| **Disponibilité du panel** | volontaires disponibles le soir et le week-end seulement | **délai plutôt que qualité** : Sprints de trois à quatre semaines au lieu de deux, revues le soir ou le samedi matin dans les centres, essais à distance sur les téléphones entre deux revues ; accepter un léger surcoût des séances de l'éditeur hors des heures de bureau plutôt que valider des écrans sans les volontaires |
| **Saison des feux** | du 15 juin au 15 septembre, aucune mise en service touchant le traitement de l'alerte, et le centre est en effectif renforcé | **délai** : placer les huit semaines de tests sur la plateforme de l'éditeur du logiciel de traitement de l'alerte pendant l'été 2028, puis les deux semaines d'essais au centre après le 15 septembre ; ou, si le projet est en avance, achever les dix semaines de tests avant le 15 juin ; le lot 1 et le lot 3 peuvent être essayés pendant l'été sans toucher au centre |
| **Échéance du support** | support de l'outil actuel jusqu'au 31/12/2028 ; l'éditeur propose douze mois à partir de juillet 2027, soit une fin en juillet 2028, au cœur de la saison des feux | **périmètre et délai plutôt que qualité** : viser une mise en service au début d'octobre 2028, après les essais au centre, en gardant l'ancien logiciel jusque-là ; conserver une marge de près de trois mois avant la fin du support ; prioriser le carnet du lot 1 (fonctions indispensables d'abord, les autres après la mise en service) plutôt que de raccourcir les tests du lot 2 ; prévoir, en repli, une prolongation courte du support de l'outil actuel (coût), décidée par le comité de pilotage au plus tard au printemps 2028 |

*1.5 b) – Le plan qualité, deux indicateurs et le contrôle*

Le **plan qualité** (ou plan d'assurance qualité) est le document qui fixe, pour un projet donné, les **exigences de qualité** à atteindre, l'**organisation** et les **responsabilités** qui y concourent, les **règles** de travail (documents, versions, changements), les **contrôles** (revues, tests, recette) et les **critères d'acceptation** de chaque livrable. ISO 9001 (édition 2026), norme d'application volontaire de management de la qualité, en fournit le cadre de principe (0,5 pt avec le contenu).

**Contenu pour VIGIE** :
- **exigences rendues mesurables** : disponibilité affichée au centre de traitement de l'alerte en moins d'une minute ; déclaration enregistrée même sans réseau et transmise dès son retour ; zéro écart entre heures enregistrées et heures indemnisées ;
- **organisation** : un responsable de la qualité côté maîtrise d'ouvrage, au contrôle de gestion, indépendant du service des systèmes d'information et de communication, un correspondant chez l'éditeur, le rôle du panel dans les essais ;
- **règles** : critères d'acceptation de chaque élément du carnet du lot 1 et « définition de terminé » ; spécifications validées des lots 2 et 3 ; gestion des versions et des demandes de changement, arbitrées en comité de pilotage ;
- **plan de tests** : tests de l'éditeur, tests d'intégration et essais au centre imposés pour le lot 2, tests du rapprochement des heures pour le lot 3, essais de bout en bout dans des centres du Haut-Aurande, recette par la maîtrise d'ouvrage ;
- **anomalies** : classement (bloquante, majeure, mineure), délais de correction, suivi ;
- **critères de mise en service** : aucune anomalie bloquante, les trois exigences atteintes en recette, formation des chefs de centre faite, retour à l'ancien logiciel possible pendant un mois ;
- **suivi après la mise en service** : indicateurs, revue mensuelle en comité de pilotage, puis au comité du SI.

**Deux indicateurs** (0,5 pt ; deux parmi les suivants) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des disponibilités affichées au centre de traitement de l'alerte en moins d'une minute | déclarations affichées dans le logiciel de traitement de l'alerte moins d'une minute après leur enregistrement dans VIGIE / déclarations enregistrées × 100 | journaux horodatés de VIGIE et du logiciel de traitement de l'alerte | quotidienne pendant les essais et le premier mois, puis mensuelle | au moins 99 % | processus |
| Taux d'écart entre heures enregistrées et heures indemnisées | heures d'intervention et de garde indemnisées différentes des heures enregistrées dans VIGIE et le logiciel de traitement de l'alerte / heures enregistrées × 100 | rapprochement automatique entre VIGIE, le logiciel de traitement de l'alerte et le logiciel des indemnités ; réclamations des volontaires | mensuelle | 0 % (zéro écart) | processus |
| Part des déclarations faites sans réseau transmises sans perte | déclarations enregistrées hors connexion puis transmises au retour du réseau / déclarations enregistrées hors connexion × 100 | journaux de l'application VIGIE, par groupement territorial | mensuelle | 100 % | client |

**Contrôle du respect des exigences** (0,5 pt) :
- **avant la mise en service** : chaque exigence a ses cas de test ; mesure du délai d'affichage pendant les huit semaines de tests et les deux semaines d'essais au centre ; essais réels par le panel dans des zones mal couvertes du Haut-Aurande, téléphone sans réseau puis reconnecté ; **double circuit** pendant un mois pour le lot 3 : les heures transmises par VIGIE sont comparées aux états établis par les chefs de centre, et tout écart est expliqué avant la bascule ; **procès-verbal de recette** signé par la maîtrise d'ouvrage, avec ou sans réserves ; décision de mise en service par le comité de pilotage au vu des critères ;
- **après la mise en service** : les indicateurs sont suivis chaque mois en comité de pilotage, puis au comité du SI ; tout écart d'heures ouvre une anomalie et une correction avant le paiement ; une revue de projet à trois mois mesure aussi les effets attendus (délai de paiement, réclamations, heures de ressaisie des chefs de centre).

**Réponses tolérées**
- Autres tensions (formation de 3 900 volontaires, dépendance aux tests de l'éditeur du logiciel de traitement de l'alerte), si l'arbitrage est explicite ; une tension qui réunit saison des feux et échéance du support compte pour une si elle est traitée en un seul arbitrage.
- Mise en service progressive (lots 1 et 3 au printemps 2028 avec l'ancien lien vers le logiciel de traitement de l'alerte, lot 2 en octobre 2028), si la cohérence des disponibilités est assurée pendant la transition.
- Report du renouvellement des tablettes pour libérer des informaticiens, si le candidat en mesure les conséquences pour les équipages.
- Autres indicateurs complets tirés des exigences (part des déclarations confirmées au volontaire, délai moyen de paiement des indemnités), s'ils portent les cinq champs ; axe « financier » pour le taux d'écart des heures, s'il est justifié.

**Erreurs fréquentes**
- *Diagramme de Gantt, chemin critique ou chiffrage construits* (`JUR-T07` répondre à la seule question posée ; limite du programme 1.5 sur l'aspect budgétaire) — non demandés.
- *Arbitrage qui sacrifie les tests du lot 2 pour tenir la date* (`JUR-G05` recommander de façon réaliste) — l'alerte est un service critique, et les tests sont imposés.
- *Mise en service prévue en juillet 2028, comme le propose l'éditeur* (`JUR-T08` exploiter toutes les annexes) — elle tombe dans la saison des feux.
- *Plan qualité réduit à la recette, ou indicateurs génériques et incomplets* (ET-18 indicateurs génériques ; `JUR-A02` distinguer performance et qualité, justifier) — chaque indicateur traduit une exigence de l'annexe 1.6.
- *Tests de sécurité ou démarche de certification proposés* (`JUR-T07`) — hors du sujet et hors programme.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO 9001 — Systèmes de management de la qualité — Exigences, 2026 (6e édition) | cadre de principe du plan qualité | `iso_9001_2026` ; F05 § 6 | en vigueur |
| Planification, plan qualité, recette et mise en production | arbitrage ressources, délais, coûts et qualité ; plan de tests ; critères de mise en service | F05 § 4 et § 6 | notion de cours |
