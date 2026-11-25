# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 18

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Préparer la gouvernance du système d'information et la conduite du projet VIGIE | 14 | 1.1 à 1.5 | `exercices/ex52_veille_maturite_projet_disponibilites` |
| 2 – Organiser et exploiter les données des interventions, en maîtriser la conservation | 13 | 2.1 à 2.4 | `exercices/ex53_interventions_sollicitation_archivage_epi` |
| 3 – Tirer les conclusions d'un audit, maîtriser les risques et la sécurité du système d'information opérationnel et en réduire l'empreinte | 13 | 3.1 à 3.4 | `exercices/ex54_audit_points_eau_alerte_mobilite_salles` |
| **Total** | **40** | | |

---

## DOSSIER 1 – PRÉPARER LA GOUVERNANCE DU SYSTÈME D'INFORMATION ET LA CONDUITE DU PROJET VIGIE (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES INTERVENTIONS, EN MAÎTRISER LA CONSERVATION (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Les données des interventions, des engins et des équipages | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 3,5 |
| 2.2 L'analyse de la sollicitation opérationnelle | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model | 4,5 |
| 2.3 La conservation des enregistrements et des comptes rendus de secours | `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `2.3.e` Aspects réglementaires (RGPD, archivage légal) et monétisation des données | 3 |
| 2.4 La proposition de PROTÉVANCE | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain | 2 |
| **Dossier 2 – Organiser et exploiter les données des interventions, en maîtriser la conservation** |  | **13** |

Répartition indicative : connaissances (modèle conceptuel, règles de passage, dictionnaire et dimensions de la qualité, chaîne de valeur et chaîne de traitement, analyse prédictive, cycle de vie, stockage et archivage électronique, principes du RGPD, chaîne de blocs de consortium) environ 2,25 points (la moitié des items 2.1 a-4, 2.1 b-1, 2.2 a-1, 2.2 c-1, 2.3 a-1, 2.3 b-1, 2.3 b-2, 2.4 a-1 et 2.4 a-2, qui mêlent définition et application) ; analyse des annexes et recommandations environ 10,75 points, soit environ 83 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Les données des interventions, des engins et des équipages (3,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) », modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites, avec une association ternaire ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données » ; `2.1.a` « Structurer et organiser les données […] afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité […] ». Aucune requête ; modèle physique seulement nommé.

**Annexes mobilisées** : annexe 2.1 (fonctionnement actuel, problèmes de qualité de 2026, règles de gestion RG1 à RG8) ; annexe 1.1 (logiciel de traitement de l'alerte, application de comptes rendus sur tablettes, 60 centres, 420 engins, 50 000 interventions).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Six entités, avec leur identifiant et des attributs élémentaires tirés de RG1 à RG8 ; nature et commune traitées en entités (listes de référence), et non en texte libre | 0,5 |
| a-2 | Associations binaires et leurs cardinalités, justifiées par les règles de gestion et lues dans les deux sens (classer, situer, desservir, appartenir, mobiliser avec ses deux heures, rattacher) | 0,5 |
| a-3 | Association ternaire « armer » entre l'agent, l'engin et l'intervention, porteuse du rôle, avec ses cardinalités (une intervention au moins un armement) | 0,5 |
| a-4 | Règles de passage énoncées ; modèle logique de neuf tables, clés primaires, clés étrangères (#) et trois tables d'association à clé composée | 0,5 |
| b-1 | Dictionnaire des données défini et appliqué ; trois entrées complètes (définition, format, règle de validité, source, propriétaire) | 0,5 |
| b-2 | Deux règles de qualité, chacune rattachée à un problème de l'annexe 2.1 B et à une dimension de la qualité | 0,5 |
| b-3 | Troisième règle de qualité, rattachée à un problème de l'annexe 2.1 B, et sa dimension (la correction à la source, le responsable désigné et le référentiel des communes partagé avec les partenaires sont valorisés, sans être exigés) | 0,5 |

**Réponse attendue**

*2.1 a) – Le modèle conceptuel et le modèle logique*

**Le modèle conceptuel** (0,5 pt pour les entités, 0,5 pt pour les associations binaires, 0,5 pt pour l'association ternaire) représente les objets de gestion (entités), leurs propriétés et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique (F07 § 1 et 2). Les identifiants sont soulignés.

Entités et attributs :
- **Intervention** (<u>num_intervention</u>, date_appel, heure_appel, adresse) (RG1) ;
- **Nature** (<u>code_nature</u>, libelle_nature) (RG2) ;
- **Commune** (<u>code_commune</u>, nom_commune, population) (RG3) ;
- **Centre** (<u>code_centre</u>, nom_centre, type_centre, groupement_territorial) (RG4) ;
- **Engin** (<u>num_engin</u>, type_engin, date_mise_service) (RG5) ;
- **Agent** (<u>matricule</u>, nom_agent, prenom_agent, statut_agent) (RG7).

La nature et la commune sont des **entités**, et non de simples attributs de l'intervention : ce sont des listes de référence, avec un code et un libellé, qui imposent une valeur parmi des valeurs connues ; c'est la réponse aux 2 500 natures « autre » et aux 1 100 libellés de communes de l'annexe 2.1 B. La commune porte en outre ses propres propriétés (population) et un lien vers son centre de premier appel.

| Association | Entités et cardinalités | Lecture (règle de gestion) |
|---|---|---|
| classer | Intervention **1,1** — Nature **0,n** | une intervention relève d'une seule nature ; une nature peut ne compter aucune intervention (RG2) |
| situer | Intervention **1,1** — Commune **0,n** | une intervention a lieu dans une seule commune ; une commune peut n'avoir connu aucune intervention (RG3) |
| desservir | Commune **1,1** — Centre **1,n** | une commune relève d'un seul centre de premier appel ; un centre est le centre de premier appel d'au moins une commune (RG4) |
| appartenir | Engin **1,1** — Centre **1,n** | un engin appartient à un seul centre ; un centre possède au moins un engin (RG5) |
| mobiliser (heure_depart, heure_arrivee) | Intervention **1,n** — Engin **0,n** | une intervention mobilise au moins un engin ; un engin peut n'avoir été engagé sur aucune intervention ; les deux heures dépendent du couple intervention-engin (RG6) |
| rattacher | Agent **1,n** — Centre **1,n** | un agent est rattaché à au moins un centre ; un centre compte au moins un agent (RG7) |
| armer (role) | Agent **0,n** — Engin **0,n** — Intervention **1,n** | sur une intervention, un agent arme un engin dans un seul rôle ; une intervention compte au moins un armement ; un agent ou un engin peut n'en avoir aucun (RG8) |

L'association **armer** est **ternaire** : le rôle ne dépend pas du seul couple agent-intervention, car sur une même intervention un agent peut armer successivement deux engins, dans des rôles différents (RG8) ; il ne dépend pas non plus du seul couple agent-engin, car un agent qui arme le même engin sur deux interventions peut y être conducteur puis chef d'agrès ; il dépend du triplet agent-engin-intervention. Un même agent n'a qu'un rôle sur un engin donné d'une intervention donnée. Les heures de départ et d'arrivée sont, elles, des attributs de l'association binaire **mobiliser** : elles dépendent de l'engin et de l'intervention, pas de l'agent. Le modèle n'exprime pas, par ses seules clés, qu'un agent n'arme qu'un engin effectivement engagé sur l'intervention : c'est une contrainte d'inclusion (armer ⊂ mobiliser) à contrôler par une règle applicative (valorisé, non exigé).

**Le modèle logique** (0,5 pt) s'obtient par les règles de passage (F07 § 4) :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire et dont les attributs deviennent des colonnes ;
2. pour une association binaire dont une patte a une cardinalité maximale 1 (classer, situer, desservir, appartenir), l'identifiant de l'entité du côté n migre comme clé étrangère dans la table de l'entité du côté 1, toujours renseignée si la cardinalité est 1,1 ;
3. une association dont toutes les pattes ont une cardinalité maximale n (mobiliser, rattacher), et toute association ternaire (armer), devient une table dont la clé primaire est composée des identifiants des entités reliées, chacun clé étrangère ; les attributs de l'association en deviennent des colonnes.

- Nature (<u>code_nature</u>, libelle_nature)
- Centre (<u>code_centre</u>, nom_centre, type_centre, groupement_territorial)
- Commune (<u>code_commune</u>, nom_commune, population, #code_centre)
- Engin (<u>num_engin</u>, type_engin, date_mise_service, #code_centre)
- Agent (<u>matricule</u>, nom_agent, prenom_agent, statut_agent)
- Intervention (<u>num_intervention</u>, date_appel, heure_appel, adresse, #code_nature, #code_commune)
- Engagement (<u>#num_intervention, #num_engin</u>, heure_depart, heure_arrivee)
- Rattachement (<u>#matricule, #code_centre</u>)
- Armement (<u>#matricule, #num_engin, #num_intervention</u>, role)

Dans Commune, `#code_centre` désigne le centre de premier appel ; dans Engin, le centre d'appartenance : ce sont deux associations différentes vers la même table. Le modèle physique (types, index sur les clés étrangères, liste fermée des rôles) se déduirait du modèle logique ; il n'est pas demandé. Les noms et prénoms des agents sont des données personnelles : le modèle s'en tient à ce qui sert à l'activité opérationnelle (minimisation).

*2.1 b) – Le dictionnaire des données et les règles de qualité*

**Le dictionnaire des données** (0,5 pt avec les trois entrées) est le référentiel qui décrit chaque donnée : nom, définition, type et format, domaine de valeurs ou règle de validité, source, propriétaire, sensibilité (F07 § 1). Il donne à tous, au centre de traitement de l'alerte, dans les centres et à l'observatoire, le même sens d'une donnée : c'est lui qui dira ce qu'est l'« heure d'arrivée » ou une « nature ». Trois entrées parmi les suivantes :

| Donnée | Définition | Type et format | Règle de validité | Source | Propriétaire |
|---|---|---|---|---|---|
| heure_arrivee | heure à laquelle l'engin arrive sur les lieux de l'intervention | date et heure, jj/mm/aaaa hh:mm | obligatoire pour clôturer l'engagement ; postérieure à l'heure de départ ; toute saisie après coup est tracée (auteur, date) | tablette de l'engin (bouton du chef d'agrès) | groupement des opérations |
| code_nature | nature de l'intervention | code de la table Nature (quatre valeurs) | valeur de la liste ; une nature provisoire choisie à l'appel est confirmée ou corrigée à la clôture ; tout changement de liste est daté | logiciel de traitement de l'alerte (opérateur), confirmée par le chef d'agrès | groupement des opérations |
| code_commune | commune du lieu de l'intervention | code de la table Commune (480 communes) | valeur du référentiel des communes ; aucune saisie libre | localisation du logiciel, ou choix dans la liste | observatoire de l'activité |
| role | rôle de l'agent sur l'engin pour l'intervention | liste : chef d'agrès, conducteur, équipier | un seul chef d'agrès et un seul conducteur par engin et par intervention | équipage enregistré au départ, corrigé dans le logiciel | groupement des opérations |

**Trois règles de qualité** (0,5 pt pour deux règles, 0,5 pt pour la troisième), chacune rattachée à un problème de l'annexe 2.1 B et à une dimension de la qualité des données (F07 § 8.3) :

1. **Contre les heures d'arrivée manquantes – complétude.** La tablette ne permet pas de clôturer l'engagement sans heure d'arrivée ; si le chef d'agrès a oublié le bouton, il la saisit à la clôture, et la saisie est marquée « déclarée après coup ». Un départ sur dix (7 000) n'a aujourd'hui pas d'heure d'arrivée : ce sont autant de données manquantes pour mesurer le délai d'arrivée, premier objectif du projet d'établissement.
2. **Contre les natures « autre » – exactitude.** La nature « autre » disparaît de la liste : l'opérateur choisit une nature provisoire, que le chef d'agrès confirme ou corrige à la clôture, d'après le compte rendu ; la correction est tracée. Les 15 jours de reclassement à la main de janvier deviennent inutiles, et une intervention sur vingt n'est plus classée au jugé.
3. **Contre les équipages incomplets – exactitude et cohérence.** Un remplacement au dernier moment est corrigé dans le logiciel de traitement de l'alerte, avant ou juste après le départ, par le chef d'agrès ou le centre, et non dans un tableur ; il n'existe qu'une source de l'équipage. Les 3 500 départs, un sur vingt, ressaisis aujourd'hui dans des tableurs de centre, sont autant de versions divergentes de la même donnée.
4. **Contre les communes mal orthographiées – unicité et cohérence.** La commune est choisie dans le référentiel des 480 communes (table Commune, identifiée par un code), jamais saisie en texte libre ; les 1 100 libellés actuels sont rapprochés une fois de ce référentiel, avec une table de correspondance conservée. Le même code de commune, partagé avec le département et les communes, rend les données échangeables avec eux (interopérabilité sémantique), comme le veut le projet d'établissement.

**Conclusion** : ces règles corrigent les données **à la source**, au moment où elles naissent (alerte, tablette, départ), plutôt qu'à chaque extraction mensuelle de l'observatoire ; elles supposent un propriétaire désigné pour chaque donnée (groupement des opérations, observatoire) et des listes de référence uniques.

**Réponses tolérées**
- Rôle traité en entité (Role, avec un code et un libellé) : l'association armer relie alors quatre entités, ou le rôle devient une clé étrangère de la table Armement, si le candidat le justifie par la liste fermée des rôles.
- Armement modélisé comme une association entre l'agent et l'engagement (association mobiliser traitée en entité, ou agrégation), si la clé reste agent-engin-intervention et le rôle porté par elle ; cette solution exprime d'ailleurs mieux la contrainte d'inclusion.
- Groupement territorial traité en entité reliée au centre ; attributs supplémentaires plausibles (dates de rattachement, coordonnées du lieu, immatriculation de l'engin).
- Cardinalité 0,n du centre dans desservir ou appartenir, si le candidat suppose un centre sans commune de premier appel ou sans engin propre, et le dit.
- Représentation graphique en notation Merise ou en « pattes de corbeau », si elle est lisible (`JUR-T10`).
- Autres entrées du dictionnaire (num_intervention, heure_depart, population), si elles portent les mêmes rubriques ; trois règles parmi les quatre, ou une autre dimension justifiée (actualité pour les équipages).

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dans le modèle conceptuel, ou clé étrangère placée du mauvais côté (#num_engin dans Centre).
- *Association ternaire décomposée en deux binaires* — agent-engin et agent-intervention séparées : on ne sait plus quel agent a armé quel engin sur quelle intervention, ni dans quel rôle.
- *Heures de départ et d'arrivée placées dans Intervention ou dans Engin* — elles dépendent du couple intervention-engin (RG6).
- *Morceau de cours* (`JUR-T01`) — définition du dictionnaire ou des dimensions de la qualité sans les problèmes chiffrés de l'annexe 2.1 B ; règles « vérifier la qualité » sans contrôle précis.
- *Requêtes écrites* (`JUR-T07`) — la question n'en demande aucune.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, cardinalités, association ternaire, règles de passage, modèle logique | définitions et méthode | F07 § 1 à 4 | notion de cours |
| Dictionnaire des données ; dimensions de la qualité (complétude, exactitude, unicité, cohérence, actualité) | définitions | F07 § 1 et 8.3 ; F08 § 4 | notion de cours |
| Interopérabilité sémantique (référentiel commun) | principe | F07 § 7 | notion de cours |

---

### 2.2 – L'analyse de la sollicitation opérationnelle (4,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique […] » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ». Limites : aucun calcul statistique, aucun développement d'algorithme ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexe 2.2 (interventions par nature et par an, séries complémentaires, reclassement de 2024, interface défaillante de 2025, touristes, épisodes de chaleur, affirmation de M. PRUNEVAUX) ; annexe 2.1 (extraction mensuelle dans un tableur, problèmes de qualité) ; annexe 1.1 (640 000 habitants, projet d'établissement).

**Barème indicatif (4,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de valeur des données définie ; collecte et nettoyage, chacune avec une limite de l'annexe 2.2 ou un problème de qualité de l'annexe 2.1 B (interface défaillante de 2025 ; natures « autre », communes) | 0,5 |
| a-2 | Structuration et analyse, chacune avec une limite (reclassement de 2024 ; touristes, séries qui se recoupent) | 0,5 |
| a-3 | Restitution et décision, avec une limite (ruptures non signalées) ; conclusion | 0,5 |
| b-1 | Deux constats argumentés et chiffrés, avec leur portée | 0,5 |
| b-2 | Troisième constat argumenté et chiffré | 0,5 |
| b-3 | Affirmation appréciée : part réelle du vieillissement (environ un tiers de la hausse) ; carences, reclassement, nuit, saisonnalité ; corrélation et causalité ; conclusion sur le recrutement | 0,5 |
| c-1 | Analyse prédictive définie et distinguée de la descriptive ; apport au SDIS (pics de l'été et des épisodes de chaleur, gardes) | 0,5 |
| c-2 | Deux conditions de réussite et deux limites, appliquées au cas | 0,5 |
| c-3 | Carte des communes en taux pour 1 000 habitants, justifiée (comparaison de communes de tailles différentes) ; précautions (touristes, petites communes) | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de valeur des données et la chaîne de traitement de la sollicitation*

**La chaîne de valeur des données** (0,5 pt avec la collecte et le nettoyage) est l'ensemble des étapes par lesquelles une donnée brute devient une information utile, puis une décision et une action : collecte, nettoyage, structuration et stockage, analyse, restitution, décision (F08 § 1). La valeur ne se crée qu'au bout de la chaîne, mais elle se perd à chaque étape mal tenue : une erreur de collecte n'est pas rattrapée par l'analyse. La chaîne de traitement en est le cœur technique et organisationnel. Pour la sollicitation opérationnelle :

| Étape | Ce que fera la chaîne | Limite traitée (annexe 2.2) |
|---|---|---|
| **Collecte** | extraction des interventions du logiciel de traitement de l'alerte, avec la nature, la commune, les heures ; âge de la victime tiré des comptes rendus ; population résidente et fréquentation touristique, données externes ; contrôle d'exhaustivité (chaque numéro d'intervention du logiciel est retrouvé dans la base) | l'interface défaillante de mars et avril 2025 a fait perdre environ 1 000 interventions sans que personne ne s'en aperçoive ; elles existent dans le logiciel et doivent être rechargées |
| **Nettoyage** | application des règles de la question 2.1 : natures « autre » corrigées, communes rapprochées du référentiel, heures manquantes marquées ; journal des rejets | une intervention sur vingt classée « autre » et 1 100 libellés de communes faussent la répartition par nature et par commune |
| **Structuration** | chargement dans une base historisée, alimentée automatiquement et non plus par un tableur ; table de correspondance des natures qui recalcule 2022 et 2023 selon la liste de 2024 ; définitions écrites (carence, nuit de 18 heures à 8 heures, âge) | le reclassement de 2024 (environ 2 000 relevages par an) rend 2022 et 2023 incomparables avec les années suivantes |
| **Analyse** | comparaisons à nomenclature constante, par saison, par tranche horaire, par commune ; taux rapportés à la population présente l'été ; séries croisées sans les additionner | jusqu'à 100 000 touristes en juillet et août ne sont pas dans les 640 000 habitants ; carences et personnes âgées se recoupent |
| **Restitution et décision** | tableaux et graphiques pour la direction et le conseil d'administration, annotés des ruptures (2024, 2025) et accompagnés d'une note de méthode ; décisions sur les gardes et les partenariats | des chiffres publiés sans ces annotations font croire à une hausse du secours d'urgence aux personnes de 8 000 interventions, au lieu de 6 000 |

**Conclusion** (0,5 pt avec la restitution) : les limites de l'annexe 2.2 ne sont pas des erreurs de calcul, mais des ruptures non documentées (reclassement, interface, population de référence). La chaîne les traite en amont, par des contrôles et des règles écrites, plutôt que par des corrections à la main dans le tableur de l'observatoire ; c'est la condition pour que le conseil d'administration décide sur des chiffres fiables.

*2.2 b) – Trois constats et l'affirmation de M. PRUNEVAUX*

**Trois constats** parmi les suivants (0,5 pt pour deux constats, 0,5 pt pour le troisième : le fait chiffré, son interprétation et sa portée) :
1. **Une hausse réelle, portée par les secours d'urgence aux personnes.** Les interventions passent de 43 000 à 50 000 en quatre ans (+ 7 000, environ + 16 %). À nomenclature constante, le secours d'urgence aux personnes passe de 33 000 à 39 000 (+ 6 000, environ + 18 %), et non de 31 000 à 39 000 : 2 000 de la hausse apparente viennent du reclassement de 2024. Les autres natures sont presque stables (de 10 000 à 11 000 à nomenclature constante).
2. **Les carences ont doublé.** De 3 000 à 6 000, elles expliquent à elles seules la moitié de la hausse réelle du secours d'urgence aux personnes et en représentent environ 15 % en 2026. Ce sont des interventions sans caractère d'urgence, faites faute d'autre moyen : une partie de la hausse ne relève pas de l'urgence.
3. **Les personnes âgées pèsent davantage.** Les interventions pour des personnes de 80 ans et plus à domicile passent de 10 000 à 12 500 (+ 2 500, environ + 25 %), plus vite que l'ensemble ; une partie de ces interventions sont aussi des carences.
4. **La sollicitation se déplace vers la nuit et vers l'été.** La part de nuit du secours d'urgence aux personnes passe de 40 % à 45 % ; l'écart entre les mois d'été et d'hiver passe de 900 à 1 200 interventions par mois, et les épisodes de chaleur de juillet 2026 ont porté l'activité à 1 500 interventions par semaine, contre 1 100 environ. Les pics, plus que la moyenne, dimensionnent les besoins.
5. **2025 est sous-estimée.** Environ 1 000 interventions manquent : 2025 compte en réalité environ 47 000 interventions, et la hausse de 2025 à 2026 est d'environ 3 000, et non de 4 000.

**L'affirmation de M. PRUNEVAUX** (0,5 pt) est en partie fondée, mais incomplète et sa conclusion ne suit pas :
- le vieillissement joue : + 2 500 interventions pour des personnes de 80 ans et plus, soit environ un tiers de la hausse de 7 000 ; il n'explique pas les deux autres tiers ;
- deux évolutions qui vont de pair ne prouvent pas que l'une cause l'autre : le vieillissement, les carences et la hausse des interventions évoluent ensemble, et les séries se recoupent (`ET-26`) ;
- les carences (+ 3 000) traduisent un manque d'autres moyens (ambulances privées, médecins de garde) : la réponse passe par la coordination avec le centre de régulation médicale du SAMU et le partage des données avec lui, objectif du projet d'établissement, plus que par de nouveaux volontaires ;
- une partie de la hausse **du secours d'urgence aux personnes** est artificielle : 2 000 relevages reclassés en 2024, sans effet sur le total ; et le saut de 2025 à 2026 (+ 4 000) est gonflé par une année 2025 sous-estimée d'environ 1 000 ; la hausse totale de 7 000 entre 2022 et 2026, elle, est réelle ;
- la pression se concentre la nuit et l'été (touristes, chaleur) : recruter des volontaires augmente les moyens, mais ne réduit pas la demande, et ne règle rien si ces moyens ne sont pas présents aux bonnes heures, aux bonnes saisons et dans les bonnes communes.

Conclusion : le recrutement peut faire partie de la réponse, mais le conseil d'administration doit d'abord disposer de chiffres à nomenclature constante, distinguer l'urgence des carences, et traiter celles-ci avec les partenaires.

*2.2 c) – L'analyse prédictive et la représentation par commune*

**L'analyse prédictive** (0,5 pt avec l'apport) estime ce qui va probablement se produire (combien d'interventions, où, quand), à partir de l'historique et de facteurs explicatifs (calendrier, météo, fréquentation touristique), avec une marge d'incertitude. Elle se distingue de l'analyse descriptive, qui dit ce qui s'est passé, et de l'analyse exploratoire, qui explore les données pour y repérer des profils, des motifs ou des anomalies (F08 § 2). Pour le SDIS, elle permettrait d'anticiper, semaine par semaine et par groupement territorial, les pics de l'été et des épisodes de chaleur (1 500 interventions par semaine en juillet 2026), d'adapter les gardes et le nombre d'agents d'astreinte aux heures de nuit et aux semaines chargées, de prépositionner des engins dans le Haut-Aurande l'été et de prévenir les partenaires.

**Deux conditions** parmi (0,5 pt avec les deux limites) : un historique fiable et homogène sur plusieurs années (règles de la question 2.1, nomenclature recalculée, 2025 complétée) ; des données externes obtenues des partenaires (prévisions météorologiques, fréquentation touristique) ; des compétences d'analyse à l'observatoire et une validation humaine des prévisions par le groupement des opérations, qui garde la décision ; des données agrégées, sans donnée personnelle des victimes.
**Deux limites** parmi : l'avenir ne reproduit pas forcément le passé (épisode exceptionnel, changement des pratiques des partenaires, `JUR-D06`) ; les petites communes comptent trop peu d'interventions pour une prévision fiable ; les biais des données passées (sous-enregistrement de 2025, natures « autre ») se retrouvent dans les prévisions ; une prévision donne un ordre de grandeur, pas une certitude, et ne dit pas pourquoi. Aucun développement d'algorithme n'est attendu.

**La représentation** (0,5 pt) : une **carte des 480 communes colorée selon le taux d'interventions pour 1 000 habitants** (carte choroplèthe), en quatre ou cinq classes, avec la légende, la source et l'année ; de préférence deux cartes à la même échelle, l'été et l'hiver. La carte montre la géographie de la sollicitation, que lit immédiatement un conseil composé d'élus des communes ; le taux permet de comparer des communes de tailles très différentes, alors qu'une carte en nombre d'interventions ne montrerait que Montcerneau et les grandes communes. Précautions : l'été, le taux calculé sur les seuls résidents surestime la sollicitation des communes touristiques du Haut-Aurande ; les petites communes, aux chiffres faibles, peuvent être regroupées. À éviter : un graphique en secteurs à 480 parts, un tableau de chiffres bruts.

**Réponses tolérées**
- Autres étapes de la chaîne (stockage distinct de la structuration, décision et action en étape propre), si chacune porte une limite de l'annexe 2.2.
- Autres constats tirés de l'annexe (incendies en hausse en 2026, accidents stables), s'ils sont chiffrés et interprétés.
- Appréciation de l'affirmation plus ou moins sévère, si elle s'appuie sur les chiffres de l'annexe et distingue la part du vieillissement du reste.
- Carte en symboles proportionnels complétée d'un taux, ou carte par groupement territorial assortie d'un tableau des communes les plus sollicitées, si le choix est justifié.
- Analyse prescriptive évoquée en complément (proposer le nombre d'agents de garde), si elle reste une aide à la décision humaine.

**Erreurs fréquentes**
- *Corrélation présentée comme causalité* (`ET-26`) — « la population vieillit, donc les interventions augmentent », sans mesurer la part du vieillissement.
- *Reclassement présenté comme une cause de la hausse totale* — il déplace 2 000 interventions des opérations diverses vers le secours d'urgence aux personnes, sans changer le total de 43 000 à 50 000.
- *Chiffres lus sans les ruptures* (`JUR-D06`) — hausse du secours d'urgence aux personnes de 8 000 prise telle quelle ; baisse des opérations diverses en 2024 interprétée comme une amélioration.
- *Chaîne réduite à un outil* (`ET-05`, `JUR-D01`) — « il suffit d'un logiciel de tableaux de bord », sans collecte, nettoyage ni structuration.
- *Calcul statistique ou algorithme* (`JUR-T07`) — coefficients, régressions ou modèle à programmer : hors attente.
- *Carte en valeurs absolues* — elle reflète la taille des communes, non leur sollicitation.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de valeur des données, chaîne décisionnelle (collecte, nettoyage, structuration, analyse, restitution) | définitions et méthode | F08 § 1 | notion de cours |
| Analyses descriptive, exploratoire, prédictive | définitions | F08 § 2 | notion de cours |
| Choix d'une représentation, carte en taux, biais, corrélation et causalité | méthode | F08 § 5 | notion de cours |

---

### 2.3 – La conservation des enregistrements et des comptes rendus de secours (3 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression », durées de conservation données par l'énoncé ; `2.3.e` « Aspects réglementaires (RGPD, archivage légal) […] », en principe, sans analyse juridique. Limites : ni prérogatives des personnes sur leurs données, ni fondement juridique des traitements (UE 1) ; aucune durée tirée d'un texte.

**Annexes mobilisées** : annexe 2.3 (enregistrements, comptes rendus, demandes de copies, enregistrement non retrouvé, durées fixées par le SDIS) ; annexe 2.5 (principes du RGPD, NF Z42-013 et ISO 14641, ISO 15489-1) ; annexe 1.1 (enregistreur des appels, application de comptes rendus, déléguée à la protection des données, médecin-chef).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cycle de vie des enregistrements, de la création à la destruction, une règle par étape (horodatage et lien avec l'intervention, accès, gel, destruction à deux ans) | 0,5 |
| a-2 | Cycle de vie des comptes rendus, une règle par étape (création structurée, usage courant deux ans, archivage jusqu'à vingt ans, destruction) | 0,5 |
| a-3 | Règles transversales appliquées au cas : demandes de copies centralisées et tracées, fin des copies en PDF et sur clés, rattrapage du stock existant | 0,5 |
| b-1 | Stockage et archivage électronique distingués et appliqués (serveur et enregistreur actuels : du stockage) | 0,5 |
| b-2 | Ce que le RGPD impose (limitation de la conservation, sécurité renforcée des données de santé, registre) et ce que les normes apportent (intégrité, pérennité, traçabilité, preuve), en principe | 0,5 |
| b-3 | Trois mesures précises, rattachées aux constats de l'annexe 2.3 | 0,5 |

**Réponse attendue**

*2.3 a) – Le cycle de vie des enregistrements et des comptes rendus*

Le cycle de vie d'une donnée va de sa **création** à sa **suppression**, en passant par le **stockage**, l'**usage** et l'**archivage** (F07 § 8.4) ; chaque étape a une règle, une durée et un responsable. Les durées sont celles que le SDIS a fixées le 15/03/2027 (annexe 2.3 D).

| Étape | Enregistrements des appels | Comptes rendus de secours |
|---|---|---|
| **Création** | enregistrement automatique de l'appel ; règle : horloge de l'enregistreur synchronisée sur une heure de référence, et numéro de l'intervention associé à l'enregistrement dès sa création (métadonnée) | rédaction sur la tablette, dans des champs structurés, rattachée au numéro de l'intervention ; règle : une fois validé, le compte rendu n'est plus modifié, toute correction crée une nouvelle version datée |
| **Stockage et usage courant** | conservation dans l'enregistreur pendant deux ans ; règle : écoute réservée aux personnes habilitées du centre de traitement de l'alerte, chaque écoute et chaque copie journalisées | consultation courante pendant deux ans, sur le serveur ; règle : accès réservé au service de santé et aux personnes habilitées, selon leur profil, journalisé ; aucune copie en PDF dans les messageries |
| **Gel en cas de demande** | si une demande portant sur l'intervention est en cours (justice, litige), l'enregistrement est copié, avec son empreinte, dans l'archive, et exclu de la destruction jusqu'à la fin de la procédure | même règle : le compte rendu demandé est gelé, et la copie remise est tracée |
| **Archivage** | sans objet, sauf enregistrement gelé | au-delà de deux ans, versement dans un système d'archivage électronique jusqu'à vingt ans après l'intervention ; règle : format pérenne, empreinte, journal des accès, consultation sur demande motivée seulement, validée par le médecin-chef |
| **Destruction** | à deux ans, destruction automatique, consignée dans un journal (quoi, quand, par qui), sauf gel | à vingt ans, destruction proposée automatiquement, validée par le médecin-chef, sous le contrôle de la déléguée à la protection des données, et consignée |

**Règles transversales** (0,5 pt) : les 400 demandes de copies de 2026 passent par un point d'entrée unique (une cellule rattachée à la direction, avec le centre de traitement de l'alerte et le médecin-chef), la déléguée à la protection des données étant consultée sur les règles et en contrôlant l'application ; elles sont inscrites dans un registre, avec un délai cible ; les copies sur clés USB et par messagerie cessent ; les 3 000 PDF trouvés dans dix messageries, et ceux des autres, sont supprimés. Le stock existant est remis en ordre une fois : les enregistrements de plus de deux ans, ceux de 2017 à 2024 environ, de l'ordre de 1,2 million, sont détruits, sauf ceux qui font l'objet d'une demande en cours ; les comptes rendus de plus de deux ans sont versés à l'archive. Avec ces règles, l'appel de novembre 2024 demandé en septembre 2026, encore dans le délai de deux ans, aurait été retrouvé par le numéro de l'intervention.

*2.3 b) – Stockage et archivage électronique, ce qu'imposent et apportent le RGPD et les normes, trois mesures*

**Stockage et archivage électronique** (0,5 pt) ne se confondent pas. Le **stockage** conserve des données sur un support pour leur usage courant : elles restent modifiables, se copient et se perdent, sans garantie dans la durée. L'**archivage électronique** conserve, pour une durée fixée, des documents qui ne sont plus d'usage courant, dans un système qui en garantit l'intégrité (aucune modification non tracée), la pérennité (lisibilité dans le temps, formats pérennes) et la traçabilité (journaux de toutes les opérations), et qui en organise le sort final (F06 § 4 et 5). Une sauvegarde, qui sert à restaurer un système, n'est pas un archivage. Au SDIS, l'enregistreur et le serveur des comptes rendus ne font que du **stockage** : 1,5 million d'enregistrements sans tri, un serveur occupé à 85 %, des copies partout et un enregistrement introuvable le jour où la justice le demande.

**Ce que le RGPD impose** (0,5 pt avec les normes ; en principe, annexe 2.5, sans analyse juridique) : les enregistrements, qui contiennent la voix et souvent l'identité des appelants, et les comptes rendus, qui contiennent des données de santé, sont des données personnelles ; ils ne peuvent être conservés que pendant une durée limitée, fixée selon la finalité : la conservation sans limite actuelle ne respecte pas ce principe, alors que le SDIS a désormais des durées. Le registre des activités de traitement doit les indiquer (F15 § 2). La minimisation proscrit les copies inutiles en PDF ; les données de santé appellent une protection renforcée (accès restreints, journalisés) ; la déléguée à la protection des données conseille et contrôle.
**Ce que les normes apportent** : NF Z42-013 et son équivalent international ISO 14641 sont des normes d'application volontaire, et non des obligations ; elles décrivent comment concevoir et exploiter un système d'archivage électronique qui garantit l'intégrité, la pérennité et la traçabilité, ce qui permet de produire, quinze ans après, un compte rendu qui puisse servir de preuve dans un litige. ISO 15489-1 donne le principe d'ensemble : des règles écrites pour chaque catégorie de documents, de la création au sort final.

**Trois mesures** parmi (0,5 pt) :
1. **Une politique de conservation écrite et appliquée** : les durées du 15/03/2027 sont inscrites au registre des activités de traitement, paramétrées dans l'enregistreur et sur le serveur (purge automatique et journalisée), avec la procédure de gel ; la déléguée à la protection des données en contrôle l'application chaque année.
2. **Un système d'archivage électronique conforme aux principes de NF Z42-013** pour les comptes rendus de plus de deux ans et les enregistrements gelés : formats pérennes, empreintes, journal des accès, accès réservé au service de santé.
3. **Un point d'entrée unique des demandes de copies** : registre des 400 demandes annuelles, copie tracée et remise par un canal sécurisé, fin des clés USB et des copies en messagerie, suppression des PDF existants.
4. **Des métadonnées qui rendent les données retrouvables** : numéro d'intervention associé à chaque enregistrement et à chaque compte rendu, horloges synchronisées sur une heure de référence, contrôle de l'horloge après chaque panne.
5. **Des habilitations par profil** : écoute des enregistrements réservée au centre de traitement de l'alerte, lecture des comptes rendus au service de santé, revue annuelle des droits.

**Réponses tolérées**
- Cycle en trois âges (courant, intermédiaire, définitif ou destruction) au lieu des cinq étapes du programme, s'il est appliqué aux deux catégories avec une règle par étape.
- Archivage intermédiaire des enregistrements entre six mois et deux ans, si la durée totale de deux ans est respectée.
- Responsable différent du point d'entrée des demandes (centre de traitement de l'alerte pour les enregistrements, médecin-chef pour les comptes rendus), si la demande est enregistrée et tracée. Valorisé : la déléguée à la protection des données conseille et contrôle sans traiter elle-même les demandes ni décider des destructions (indépendance, F15 § 1).
- Prestataire d'archivage externe évoqué, si le candidat garde les exigences d'intégrité, d'accès restreint et de réversibilité, sans développer l'hébergement.
- Trois mesures parmi les cinq, ou d'autres mesures précises et rattachées à l'annexe 2.3.

**Erreurs fréquentes**
- *Stockage et archivage confondus* — « le serveur archive les comptes rendus », ou sauvegarde présentée comme un archivage.
- *Durée tirée d'un texte de loi* (`JUR-T07`) — les durées sont celles fixées par le SDIS et données par l'annexe ; aucune n'est à citer ni à discuter.
- *Dérive juridique* (`JUR-T07`) — développements sur les prérogatives des familles ou des avocats, ou sur le fondement juridique des traitements (UE 1) : la question porte sur l'organisation de la conservation.
- *Norme présentée comme une obligation ou comme une solution* (`ET-01`) — norme d'archivage présentée comme imposée au SDIS, ou comme un produit à installer : elle est d'application volontaire et décrit des exigences, que l'outil choisi doit respecter.
- *Destruction sans gel* — détruire à deux ans un enregistrement qui fait l'objet d'une demande en cours.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cycle de vie des données (création, stockage, usage, archivage, suppression) | définition et méthode | F07 § 8.4 ; F06 § 4 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) : minimisation, limitation de la conservation, données de santé, registre des activités de traitement | principes donnés en annexe 2.5 | `rgpd` / F15 § 2 | applicable depuis le 25/05/2018 |
| NF Z42-013, archivage électronique | intégrité, pérennité, traçabilité, en principe | `nf_z42_013` / F06 § 5 | en vigueur, norme volontaire |
| ISO 14641, archivage électronique | équivalent international de NF Z42-013 | `iso_14641` / F06 § 5 | en vigueur |
| ISO 15489-1, gestion des documents d'activité (2016) | concepts et principes | `iso_15489_1` / F06 § 4 | en vigueur |

---

### 2.4 – La proposition de PROTÉVANCE (2 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ». Limites : aucun développement ; effets énergétiques intégrés à l'analyse ; aucun cryptoactif.

**Annexes mobilisées** : annexe 2.4 (suivi actuel des tenues, constats de l'inventaire, proposition de PROTÉVANCE, coûts, base de données partagée) ; annexe 2.5 (ISO 22739:2024, principes du RGPD) ; annexe 1.1 (logiciel de gestion du parc, effectif).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de blocs définie ; fonctionnement de la chaîne de consortium appliqué à la proposition (nœuds des cinq acteurs, événements signés, validation par les participants identifiés, blocs chaînés, inaltérabilité pratique) ; distinction avec une base de données distribuée | 0,5 |
| a-2 | Type d'application : traçabilité d'un bien physique dans une chaîne d'acteurs (preuve horodatée des événements), sans cryptoactif | 0,5 |
| b-1 | Valeur ajoutée (historique commun, lavages contestés, accident) et coûts comparés (150 k€ contre 90 k€ sur trois ans) ; limites (donnée d'entrée, gouvernance à cinq, nœuds hébergés par le fournisseur, matricule inscrit, énergie) | 0,5 |
| b-2 | Conclusion argumentée et conditions | 0,5 |

**Réponse attendue**

*2.4 a) – Le fonctionnement et le type d'application*

**La chaîne de blocs** (0,5 pt avec le fonctionnement) est un registre distribué : il est partagé et synchronisé entre plusieurs nœuds, les transactions y sont regroupées en blocs chaînés par des empreintes (chaque bloc contient l'empreinte du précédent), et un mécanisme de consensus valide chaque ajout ; une fois inscrite, une transaction est horodatée et pratiquement inaltérable (F11 § 1). Elle permet à des acteurs qui ne se font pas pleinement confiance de partager un même historique sans qu'aucun d'eux ne puisse le modifier seul. C'est ce qui la distingue d'une **base de données distribuée**, qui répartit les données d'un même gestionnaire, lequel peut les modifier (`ET-08`).

Dans la proposition de PROTÉVANCE, la chaîne est **de consortium** (permissionnée) : seuls cinq acteurs identifiés (les trois SDIS, PROTÉVANCE, LAVORDÈNE) disposent d'un nœud et d'une copie du registre. Quand le blanchisseur lit la puce d'une tenue lavée, il émet une transaction « lavage », signée par sa clé ; les participants autorisés la valident, sans minage, puis elle est ajoutée à un bloc et recopiée sur tous les nœuds. Chaque événement (livraison, attribution, lavage, contrôle, réparation, réforme) s'ajoute ainsi à l'historique de la tenue, que chaque acteur lit sans pouvoir le réécrire.

**Le type d'application** (0,5 pt) : il s'agit d'une application de **traçabilité** : suivre un bien physique, la tenue, tout au long de sa vie et entre plusieurs organisations, avec une preuve horodatée de chaque événement, proche de la certification d'événements (nombre de lavages, date du dernier contrôle). Ce n'est ni de la finance décentralisée, ni un jeton non fongible, ni un cryptoactif : aucune monnaie ni aucun jeton n'est émis.

*2.4 b) – Valeur ajoutée, coûts, limites et conclusion*

**Valeur ajoutée, coûts et limites** (0,5 pt) :
- **valeur ajoutée** : un historique commun et infalsifiable, que ni le fournisseur ni le blanchisseur ne peuvent retoucher ; il réglerait les contestations sur les lavages (30 000 facturés, 24 000 enregistrés), dirait sans délai qui portait quelle tenue et quand elle a été contrôlée (une semaine de recherche après l'accident de 2026), et suivrait le terme de dix ans ou de 50 lavages ; il serait commun aux trois SDIS. Mais l'essentiel du gain vient de la **puce**, qui supprime la saisie à la main, et non de la chaîne : la base partagée l'apporte aussi ;
- **coûts** : sur trois ans, la chaîne coûterait au SDIS 20 + 40 + 3 × 30 = 150 k€, la base partagée 20 + 40 + 3 × 10 = 90 k€, soit 60 k€ de plus pour la chaîne ;
- **limites** : la chaîne garantit que l'événement inscrit n'a pas été modifié, pas qu'il est vrai : une puce lue ne prouve pas que la tenue a été bien lavée (donnée d'entrée) ; la gouvernance à cinq reste à construire (admission des nœuds, évolution des règles, partage des coûts, sortie d'un acteur), alors que les deux SDIS voisins n'ont pas pris position ; si PROTÉVANCE héberge les nœuds des SDIS, la confiance redevient centrée sur le fournisseur, qui est aussi partie aux contestations, et le SDIS en dépend ; le matricule inscrit dans un registre inaltérable est une donnée personnelle qu'on ne pourra plus supprimer au terme de sa durée de conservation : il faut n'y inscrire qu'un identifiant de tenue et garder le lien avec l'agent dans le logiciel de gestion du parc ; la validation sans minage consomme peu, mais cinq copies du registre consomment davantage qu'une base unique ; il faut enfin relier la chaîne au logiciel de gestion du parc pour éviter une double saisie.

**Conclusion** (0,5 pt) : les acteurs sont peu nombreux, identifiés et liés par des contrats, et un tiers de confiance peut être désigné : le prestataire que retiendraient les trois SDIS, à condition que PROTÉVANCE et LAVORDÈNE l'acceptent aussi. Selon la grille d'opportunité (F11 § 2.2), une base de données partagée, avec un journal des modifications tenu par ce tiers, des droits d'écriture propres à chaque acteur et des exports réguliers, répond au besoin pour 60 k€ de moins sur trois ans. Il est recommandé d'équiper les tenues de puces et de retenir la base partagée, en prévoyant la récupération des données en fin de contrat ; la chaîne de blocs ne serait à réexaminer que si le consortium s'élargissait sans qu'un tiers soit accepté de tous, avec des nœuds tenus par chaque acteur et sans matricule inscrit.

**Réponses tolérées**
- Conclusion en faveur d'un essai limité de la chaîne de blocs, si le candidat pose des conditions précises (adhésion des deux SDIS voisins, nœud propre au SDIS, aucun matricule inscrit, comparaison au bout d'un an avec la base partagée).
- Consensus nommé « preuve d'autorité » ou « tolérance aux pannes byzantines », en principe, sans développement technique.
- Coût comparé par an (20 k€ de plus par an) plutôt que sur trois ans.
- Certification citée comme type d'application, si la traçabilité est reconnue comme l'usage principal.

**Erreurs fréquentes**
- *Chaîne de blocs confondue avec une base de données distribuée* (`ET-08`) — « une base partagée sur plusieurs serveurs ».
- *Opportunités sans limites* (`ET-19`) — chaîne présentée comme la solution aux oublis de saisie, alors qu'elle ne garantit pas la donnée d'entrée.
- *Oubli de l'énergie ou de la gouvernance* — le programme impose d'intégrer les effets énergétiques ; la gouvernance à cinq est la difficulté principale.
- *Cryptoactif ou jeton évoqué* (`JUR-T07`) — la proposition n'en comporte aucun.
- *Morceau de cours* (`JUR-T01`) — définition sans les chiffres de l'annexe 2.4 ni la comparaison avec la base partagée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Registre distribué, chaîne de blocs de consortium, consensus, distinction avec une base distribuée | définitions | F11 § 1 | notion de cours |
| Usages (traçabilité, certification), grille d'opportunité, limites (donnée d'entrée, gouvernance, énergie, données personnelles) | méthode | F11 § 2 | notion de cours |
| ISO 22739:2024, vocabulaire des chaînes de blocs et des registres distribués | terminologie, donnée en annexe 2.5 | `iso_22739_2024` / F11 § 3.4 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) : minimisation, limitation de la conservation | principe donné en annexe 2.5 | `rgpd` / F15 | applicable depuis le 25/05/2018 |

---

## DOSSIER 3 – TIRER LES CONCLUSIONS D'UN AUDIT, MAÎTRISER LES RISQUES ET LA SÉCURITÉ DU SYSTÈME D'INFORMATION OPÉRATIONNEL ET EN RÉDUIRE L'EMPREINTE (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les conclusions de l'audit de la base des points d'eau d'incendie | `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse | 3 |
| 3.2 Les risques du logiciel de traitement de l'alerte | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. | 3 |
| 3.3 La sécurité des tablettes et la gouvernance du traitement de l'alerte | `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 4 |
| 3.4 Les salles informatiques et la transition numérique responsable | `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 3 |
| **Dossier 3 – Tirer les conclusions d'un audit, maîtriser les risques et la sécurité du système d'information opérationnel et en réduire l'empreinte** |  | **13** |

Répartition indicative : connaissances (critère d'appréciation, typologie des risques, ISO/IEC 27005 et EBIOS Risk Manager, architecture de confiance, transition numérique responsable) environ 3 points (items 3.1 b-1, 3.2 a-1, 3.2 b-1, 3.3 a-1, 3.3 b-1 et 3.4 a-1, chacun en partie appliqué au cas) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – Les conclusions de l'audit de la base des points d'eau d'incendie (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la mission est terminée, ni son cadrage ni sa démarche ne sont demandés ; l'organisation des contrôles des points d'eau est donnée par l'annexe, et aucune règle de droit n'est à connaître.

**Annexes mobilisées** : annexe 3.1 (base, organisation fixée par le SDIS, neuf notes brutes, réactions, demande du directeur) et annexe 1.1 (base des points d'eau et système d'information géographique, logiciel de traitement de l'alerte, 60 centres dont 48 armés par des volontaires seulement, Haut-Aurande).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Note adressée au directeur, tournée vers la décision, bornée à 20 lignes ; appréciation d'ensemble nette (base non fiable, risque opérationnel direct) | 0,5 |
| a-2 | Quatre constats regroupés à partir des notes brutes et hiérarchisés de façon justifiée : la carte de l'alerte et le circuit des indisponibilités en premier, au vu de l'incendie du 12/08/2026 | 0,5 |
| a-3 | Pour chaque constat, le risque et une recommandation concrète, avec un responsable et une échéance réalistes | 0,5 |
| a-4 | Réponse à l'objection du lieutenant-colonel OSSELIN ; suivi du plan d'action | 0,5 |
| b-1 | Critère d'appréciation défini ; fiabilité des données, sécurité et efficacité du processus définies et appliquées à la base et à sa mise à jour | 0,5 |
| b-2 | Deux constats justement rattachés à chacun des trois critères | 0,5 |

**Réponse attendue**

*3.1 a) – La note de synthèse*

La note de synthèse d'audit s'adresse à un décideur : elle tient en une page, donne une appréciation d'ensemble, ne retient que les constats qui appellent une décision, les **hiérarchise**, et assortit chacun du risque, de la recommandation, du responsable et de l'échéance (F10 § 1.2 et § 5). Elle ne recopie pas les notes brutes : elle les **regroupe**.

Regroupement attendu des neuf notes brutes de l'annexe 3.1 B :
- **la carte de l'alerte ne reflète pas l'état réel des points d'eau** : indisponibilités signalées à des interlocuteurs différents et saisies en 12 jours en moyenne, chargement mensuel à la main sans contrôle, chargement de septembre 2026 échoué sans que personne le voie, 600 écarts dont 150 points indisponibles affichés disponibles, incendie du 12/08/2026 ;
- **la base n'est ni protégée ni tracée** : 1 200 comptes ont le droit de la modifier, aucun historique, sauvegarde jamais restaurée et gardée dans la salle où se trouve le serveur ;
- **les données sont périmées ou inexactes** : 3 500 points, un sur quatre, sans contrôle depuis plus de deux ans ; un point sur dix mal placé dans le Haut-Aurande ;
- **la collecte des contrôles est artisanale** : tableurs de formats différents envoyés par 480 communes et 6 gestionnaires, ressaisis par trois agents, 1 500 résultats, un sur quatre, en attente.

Hiérarchie : la **carte de l'alerte** vient en priorité 1, car c'est elle que suivent les équipages et l'incendie du 12/08/2026 montre que le risque s'est déjà réalisé. La **sécurité de la base** vient aussi en priorité 1 : une modification erronée ou malveillante d'un point d'eau serait invisible, et la base peut être perdue avec la salle. Les **données périmées** et la **collecte** viennent en priorité 2 : elles demandent plusieurs mois de rattrapage et un changement de processus, et la note leur donne une échéance plus lointaine.

Note modèle (environ 20 lignes, à la borne) :

<!-- note -->
**Au colonel hors classe GRANVOISE – Audit de la base des points d'eau (comité de direction du 07/06/2027)**
**Appréciation d'ensemble** : base non fiable ; la carte de l'alerte peut envoyer un engin vers un point d'eau hors service.
**1. Carte de l'alerte en retard (priorité 1).** Indisponibilités saisies en 12 jours, carte rechargée chaque mois sans contrôle ; 150 points hors service affichés disponibles. Risque : alimentation en eau retardée. Recommandation : tout signalement adressé au centre de traitement de l'alerte et saisi le jour même ; chargement hebdomadaire contrôlé, puis liaison automatique. Lt-col OSSELIN, Mme VARANGEOT : 30/06/2027.
**2. Base ouverte et sans trace (priorité 1).** 1 200 comptes peuvent la modifier ; aucun historique ; sauvegarde jamais restaurée, gardée sur place. Risque : erreur ou malveillance invisible, base perdue. Recommandation : droits réservés à la cellule cartographie, journal des modifications, copie hors du siège et restauration essayée. Mme VARANGEOT, 30/09/2027.
**3. Données périmées (priorité 2).** 3 500 points sans contrôle depuis deux ans ; un point sur dix mal placé dans le Haut-Aurande. Risque : point d'eau à sec ou introuvable. Recommandation : rattrapage, d'abord dans le Haut-Aurande. Lt-col OSSELIN et chefs de centre, 30/06/2028.
**4. Collecte artisanale (priorité 2).** Tableurs de formats différents, ressaisis par trois agents ; 1 500 en attente. Risque : retards et erreurs durables. Recommandation : modèle unique, puis saisie directe par les communes et les gestionnaires. Lt-col OSSELIN, 2028.
**Objection** : connaître son secteur ne dit pas qu'un poteau est hors service ; le 12/08/2026, l'engin a suivi la carte. La collecte simplifiée (4) soulage les trois agents.
**Suivi** : point trimestriel, audit de suivi en 2028.
<!-- /note -->

**Réponse à l'objection du lieutenant-colonel OSSELIN** (a-4) :
- l'état d'un point d'eau change (poteau en panne, citerne vide, travaux) et ne s'apprend pas par l'expérience du secteur : le 12/08/2026, l'engin a suivi la carte vers un poteau hors service depuis trois semaines. La carte sert aussi aux opérateurs du centre de traitement de l'alerte, qui ne connaissent pas chaque secteur ;
- c'est la ressaisie de 6 000 résultats en tableurs qui absorbe les trois agents de la cellule : le modèle unique et la saisie directe par les communes et les gestionnaires libèrent leur temps, et le rattrapage commence par le Haut-Aurande pour tenir compte de leurs moyens.

La liaison automatique entre la base et le logiciel de l'alerte n'a pas d'échéance ferme : le calendrier de l'éditeur est chargé (réaction de Mme VARANGEOT), deux développeurs seulement connaissent les interfaces et la version actuelle n'est plus maintenue après 2029 (annexe 3.2). Elle est inscrite dans les besoins de la suite du logiciel, ou demandée à l'éditeur avec la documentation des interfaces ; le chargement hebdomadaire contrôlé, dès le 30/06/2027, tient lieu de mesure immédiate.

*3.1 b) – Les trois critères d'appréciation*

**Définition** (b-1) : un **critère d'appréciation** est la référence (objectif, exigence, règle interne, norme) au regard de laquelle l'auditeur compare la situation constatée et qualifie un écart. Il rend le jugement de l'audit explicite, vérifiable et discutable par les audités ; en audit des systèmes d'information, les critères usuels portent sur la fiabilité, l'efficacité et l'efficience, la sécurité et la conformité (F10 § 1.1). Ici, la référence est l'organisation fixée par le SDIS (contrôle tous les deux ans, signalement immédiat des indisponibilités) et le besoin opérationnel : une carte juste au moment de l'alerte.

| Critère | Ce qui est attendu de la base et de sa mise à jour | Deux constats de l'annexe 3.1 (b-2) |
|---|---|---|
| **Fiabilité des données** | les données sont exactes, complètes, à jour et cohérentes entre la base et la carte de l'alerte | 3 500 points sans contrôle depuis plus de deux ans ; 600 écarts entre la base et la carte, dont 150 points indisponibles affichés disponibles ; un point sur dix placé à plus de 100 mètres de sa position |
| **Sécurité** | seules les personnes autorisées modifient la base (intégrité), chaque modification est imputable (traçabilité), la base peut être restaurée après un sinistre (disponibilité) | 1 200 comptes ont le droit de modifier ; aucune trace des modifications ; sauvegarde jamais restaurée, dans la même salle que le serveur |
| **Efficacité du processus** | le processus atteint son objectif, une carte à jour au moment de l'alerte, dans des délais courts et avec des moyens raisonnables | indisponibilités saisies en 12 jours, puis attente du chargement mensuel ; 6 000 résultats reçus en tableurs de formats différents et ressaisis un par un, 1 500 en attente ; chargement manuel sans contrôle, échec de septembre 2026 inaperçu |

**Réponses tolérées**
- Note présentée en tableau (constat, risque, recommandation, responsable, priorité, échéance), si elle tient dans les 20 lignes et commence par une appréciation d'ensemble.
- Trois ou cinq regroupements au lieu de quatre, si chacun rassemble plusieurs notes brutes et si la carte de l'alerte vient en tête ; sécurité de la base en priorité 2, si la priorité 1 donnée à la carte est justifiée par l'incendie.
- Autres responsables plausibles : chef du groupement des opérations seul propriétaire de la base, service des systèmes d'information et de communication pour l'outil, cheffe du centre de traitement de l'alerte pour le circuit des signalements ; échéances différentes si elles sont datées et cohérentes avec la priorité.
- Réponse à l'objection placée en conclusion de la note, ou intégrée au premier constat ; liaison automatique fixée à la fin de 2027, si un chargement contrôlé la précède.
- Efficience à la place de l'efficacité pour la ressaisie, ou critère de conformité à l'organisation fixée par le SDIS ajouté, si les trois critères demandés sont traités ; un constat rattaché à deux critères (l'échec du chargement de septembre relève de la fiabilité et de l'efficacité), si c'est justifié.

**Erreurs fréquentes**
- *Note qui dépasse 20 lignes, recopie les notes brutes dans leur ordre, ou omet le responsable et l'échéance* (`JUR-T07`, `JUR-T04`) — juste : quatre constats regroupés, hiérarchisés, chacun avec son risque, sa recommandation, son responsable et son échéance.
- *Constats sans conséquence opérationnelle* (`JUR-T03`) — juste : le risque d'un point d'eau faux est un retard de l'alimentation en eau sur un feu, déjà constaté.
- *Critères récités sans être reliés aux constats* (`JUR-T01`) — juste : ce qui est attendu de la base, puis deux constats par critère.
- *Démarche ou méthodologie de l'audit exposée* — non demandée : la mission est terminée.
- *Règles de droit sur les points d'eau, répartition légale des contrôles entre le SDIS et les communes* — non attendues : l'organisation est donnée par l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Note de synthèse d'audit | appréciation d'ensemble, constats hiérarchisés, recommandation, responsable, échéance | F10 § 1.2 et § 5 | notion de cours |
| Critères d'audit du SI | fiabilité, efficacité, sécurité, conformité | F10 § 0 et § 1.1 | notion de cours |

---

### 3.2 – Les risques du logiciel de traitement de l'alerte (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; ISO/IEC 27005 et EBIOS Risk Manager sont présentées en principe, sans conduire les ateliers ; aucune analyse d'impact détaillée d'une panne, aucune procédure de choix d'un nouvel éditeur, aucun chiffrage.

**Annexes mobilisées** : annexe 3.2 (logiciel, éditeur, contrat, serveurs, pannes de 2026, échelles), annexe 3.3 (réseau commun, rançongiciel du SDIS voisin), annexe 3.5 (ISO/IEC 27005:2022, EBIOS Risk Manager, guide d'hygiène, RGPD) et annexe 1.1 (logiciel installé en 2012, petit éditeur spécialisé, salle de secours de Montcerneau-Sud, 150 000 appels).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers, dont la dépendance envers un fournisseur) ; risques formulés comme des événements redoutés | 0,5 |
| a-2 | Quatre risques tirés de l'annexe 3.2, chacun avec sa cause et ses chiffres, et classés | 0,5 |
| a-3 | Probabilité et impact cotés de façon justifiée selon les échelles de l'annexe 3.2 C ; les deux risques de niveau 3 × 3 dégagés | 0,5 |
| b-1 | ISO/IEC 27005 (lignes directrices, processus générique, sans méthode imposée) et EBIOS Risk Manager (méthode en cinq ateliers, sources de risque et écosystème) comparées ; choix justifié par le cas, avec sa limite | 0,5 |
| c-1 | Traitement de la fin de maintenance sans solution prête, justifié par la probabilité et l'impact (réduire, ou éviter défini comme l'abandon de la version avant la fin de sa maintenance, justifié ; accepter et transférer écartés) | 0,5 |
| c-2 | Traitement du rançongiciel, justifié (réduire ; transfert discuté et jugé partiel) | 0,5 |

**Réponse attendue**

*3.2 a) – Quatre risques, leur classement et leur cotation*

**Typologie** (a-1) : les risques liés aux systèmes d'information se classent en **cybermenaces** (rançongiciel, hameçonnage, attaque par la chaîne d'approvisionnement, c'est-à-dire par un éditeur ou un prestataire), **défaillances opérationnelles** non intentionnelles (panne, erreur, correctif défectueux), **risques réglementaires** (manquement à une obligation, par exemple la sécurité des données personnelles) et **risques métiers**, qui touchent la mission ou la stratégie, dont la **dépendance envers un fournisseur** (F12 § 0 et § 5). Un risque se formule comme un **événement redouté**, avec sa cause et sa conséquence ; ici, le critère dominant est la **disponibilité** du traitement de l'alerte, mission que le projet d'établissement veut garantir jour et nuit.

**Risques, classement et cotation** (a-2 et a-3 ; quatre sont attendus, cinq sont proposés) :

| Risque (événement redouté) et cause | Nature | Probabilité | Impact |
|---|---|---|---|
| R1 – **Au 01/01/2030, le SDIS exploite un logiciel que l'éditeur ne maintient plus**, sans solution de remplacement en service : plus aucun correctif, fonctionnel ou de sécurité. Causes : fin de maintenance annoncée au 31/12/2029 ; nouvelle version reportée « à partir de 2029 » et utilisée par aucun SDIS ; moins de trois ans pour préparer un changement de logiciel critique | risque métier, dépendance envers l'éditeur | **3** : certain à une date connue si rien n'est fait | **3** : toute panne ou faille deviendrait impossible à corriger, donc impossible à rétablir rapidement |
| R2 – **Un rançongiciel chiffre les serveurs du traitement de l'alerte dans les deux salles.** Causes : système d'exploitation sans correctifs de sécurité depuis 2025 ; serveurs sur le même réseau que la bureautique et les tablettes ; accès de l'éditeur ouvert en permanence avec un compte commun | cybermenace, par la bureautique ou par l'éditeur ; volet réglementaire : violation de données personnelles des appelants (annexe 3.5) | **3** : facile à provoquer en l'état ; scénario réalisé chez le SDIS voisin en février 2027 | **3** : réception des appels et engagement des secours arrêtés dans les deux salles ; une journée chez le voisin |
| R3 – **Une anomalie du logiciel, installée dans les deux salles, bloque une fonction essentielle, et l'éditeur ne peut la corriger vite.** Causes : correctif installé le même soir dans les deux salles ; deux développeurs seulement connaissent les interfaces, dont un part en 2028 ; aucune documentation | défaillance opérationnelle ; dépendance envers les compétences de l'éditeur | **3** : constaté en novembre 2026 | **2** : 2 heures de choix des engins à la main, sans arrêt de la réception des appels ; il deviendrait de niveau 3 si l'éditeur ne pouvait plus corriger |
| R4 – **Les serveurs du siège s'arrêtent** (climatisation de 2008, matériels de 2017) **et la bascule est lente** | défaillance opérationnelle | **3** : constaté en juillet 2026 | **2** : bascule en 45 minutes, une trentaine d'appels sur papier |
| R5 – **L'éditeur cesse son activité ou abandonne le logiciel**, sans remise du code source ni aide à la sortie | risque métier, dépendance envers l'éditeur | **2** : société de 40 salariés dont le SDIS est un des trois principaux clients ; plausible, non constaté | **3** : plus personne ne peut corriger le logiciel |

Les deux risques dont la probabilité et l'impact sont tous deux de niveau 3, à traiter en priorité selon la règle du comité de direction, sont **R1** et **R2**. R3 et R4 sont fréquents mais leur effet reste un mode dégradé ; R5 est grave mais moins probable. Plusieurs risques ont une cause commune : la dépendance envers un petit éditeur, que l'on retrouve dans R1, R3 et R5.

*3.2 b) – ISO/IEC 27005 ou EBIOS Risk Manager*

**Comparaison** (b-1) :
- l'**ISO/IEC 27005:2022** donne des **lignes directrices** internationales : elle décrit le processus de gestion des risques liés à la sécurité de l'information (établir le contexte, identifier, analyser, évaluer, traiter, surveiller) et les options de traitement, dans la logique du système de management de l'ISO/IEC 27001:2022. Elle ne prescrit **aucune méthode** : l'organisation choisit ses échelles et ses techniques. Elle n'est ni une norme d'exigences ni une solution ;
- **EBIOS Risk Manager** (ANSSI, version 1.5 de 2024) est une **méthode** française, compatible avec l'ISO/IEC 27005, qui outille ce processus en cinq ateliers : le cadrage et le **socle de sécurité**, les **sources de risque** et leurs objectifs, les **scénarios stratégiques**, qui passent par l'**écosystème** (éditeurs, prestataires, partenaires), les scénarios opérationnels, puis le traitement (F12 § 2 ; annexe 3.5).

**Choix** : EBIOS Risk Manager, inscrite dans le processus de l'ISO/IEC 27005. Elle convient au SDIS pour trois raisons tirées du cas :
- les risques les plus graves passent par l'**écosystème** : un éditeur dont l'accès est ouvert en permanence et dont dépendent les correctifs, les SDIS voisins, le centre de régulation médicale du SAMU et les hôpitaux qui reçoivent les comptes rendus ;
- la menace est en partie **intentionnelle** : le rançongiciel du SDIS voisin appelle une analyse des sources de risque, que l'ISO/IEC 27005 prévoit sans fournir de démarche détaillée pour la conduire ;
- l'atelier de **socle de sécurité**, appuyé sur le guide d'hygiène de l'ANSSI, fait apparaître tout de suite les écarts évidents (mises à jour, cloisonnement, sauvegardes), et les scénarios sont lisibles pour le conseil d'administration.

**Limite** : la méthode demande du temps et des compétences, alors que le SDIS n'a ni analyse formalisée ni responsable de la sécurité. Il faut donc restreindre le périmètre au traitement de l'alerte et à ses interfaces, se faire accompagner et présenter au conseil du 01/07/2027 un premier résultat (cadrage, socle, scénarios principaux, mesures prioritaires), à compléter ensuite.

*3.2 c) – Le traitement des deux risques les plus graves*

| Risque | Option retenue et justification | Mesures |
|---|---|---|
| **R1 – Logiciel non maintenu au 01/01/2030** (probabilité 3, impact 3) | **Réduire** d'ici 2030, en préparant **l'évitement** : le risque disparaît si le SDIS quitte la version actuelle avant le 31/12/2029, mais aucune solution de remplacement n'est prête (nouvelle version reportée, utilisée par aucun SDIS). Il faut donc d'ici là réduire la probabilité (préparer le remplacement, calendrier ferme) et l'impact (maintenance prolongée, documentation des interfaces). **Accepter** est exclu : le risque est certain et son impact touche une mission que le projet d'établissement veut garantir jour et nuit. **Transférer** est sans objet : aucun contrat ni aucune assurance ne prend en charge un traitement de l'alerte arrêté | lancer dès 2027 la préparation du remplacement, avec une décision en 2028 sur la suite (nouvelle version de l'éditeur ou autre solution), sans organiser ici le choix ; exiger de l'éditeur un calendrier ferme, une période de recouvrement et une maintenance prolongée en filet de sécurité ; obtenir la documentation des interfaces avant le départ du développeur en 2028 ; prévoir, à la prochaine reconduction du contrat, la remise du code source en cas de défaillance et l'aide à la sortie, ce qui réduit aussi R5 ; informer le conseil d'administration du 01/07/2027 de l'échéance |
| **R2 – Rançongiciel dans les deux salles** (probabilité 3, impact 3) | **Réduire** d'abord la probabilité, car elle tient à des faiblesses connues et corrigeables, puis l'impact. **Transférer** n'est que partiel : une assurance peut couvrir des frais de reconstruction et de gestion de crise, jamais l'arrêt de l'alerte ni ses conséquences pour les victimes ; elle complète les mesures, sans les remplacer. **Accepter** est inadmissible pour un système critique ; **éviter** est impossible | séparer le réseau du traitement de l'alerte de celui de la bureautique et des tablettes, en n'ouvrant que les flux nécessaires (question 3.3) ; remplacer le compte commun de l'éditeur par des accès nominatifs, ouverts à la demande, avec une authentification forte et une trace ; tant que le système d'exploitation ne peut être mis à jour, isoler davantage ces serveurs et exiger de l'éditeur une version compatible ; sauvegardes hors ligne dont la restauration est essayée ; procédure de repli sur papier et entraide des centres de traitement de l'alerte voisins, exercées, comme en février 2027 |

Après traitement, le **risque résiduel** est présenté au directeur départemental, qui l'accepte formellement, puis au conseil d'administration.

**Réponses tolérées**
- Autres risques tirés de l'annexe 3.2, si chacun est formulé comme un événement redouté et coté selon les échelles : interfaces arrêtées au départ du développeur ; intervention malveillante par le compte commun de l'éditeur.
- R2 coté 2 en probabilité au titre du « constaté dans un autre SDIS », si le candidat retient ensuite R1 et un autre risque de niveau 3 × 3 qu'il justifie, ou s'il explique pourquoi il traite quand même R2 ; R3 coté 3 en impact si le candidat montre qu'une anomalie plus longue arrêterait l'engagement des secours.
- ISO/IEC 27005 retenue seule, pour sa simplicité et le délai court avant le conseil du 01/07/2027, si la nature des deux référentiels est juste et si l'écosystème est pris en compte.
- « Éviter » seul pour R1, s'il est défini comme l'abandon de la situation à l'origine du risque (exploiter la version actuelle après le 31/12/2029) et si le candidat montre comment le SDIS tient jusqu'au remplacement.

**Erreurs fréquentes**
- *Risques réduits à des constats ou génériques (« risque informatique »)* (`JUR-T01`, `JUR-T03`) — juste : des événements redoutés, avec leur cause et leurs chiffres, cotés selon les échelles de l'annexe.
- *Norme, lignes directrices, méthode et solution confondues ; « installer EBIOS »* (`ET-01`, `JUR-S06`) — juste : ISO/IEC 27005, lignes directrices ; EBIOS Risk Manager, méthode ; ISO/IEC 27001, norme d'exigences.
- *Risque « transféré à l'éditeur » ou à l'assureur* (`JUR-T03`) — juste : la responsabilité du traitement de l'alerte reste au SDIS ; l'assurance ne couvre qu'une part financière.
- *Risque de niveau 3 × 3 accepté* — juste : réduire, et faire accepter le seul risque résiduel par le directeur.
- *Choix d'un nouvel éditeur organisé, analyse d'impact détaillée des pannes, chiffrage* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI, événement redouté | cybermenaces, défaillances, risques réglementaires et métiers, dépendance | F12 § 0 et § 5 | notion de cours |
| ISO/IEC 27005:2022 | lignes directrices de gestion des risques, options de traitement | `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI) | méthode en cinq ateliers, sources de risque, écosystème | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| ISO/IEC 27001:2022 | système de management fondé sur l'appréciation des risques | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | socle de sécurité : mises à jour, cloisonnement, sauvegardes | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |

---

### 3.3 – La sécurité des tablettes et la gouvernance du traitement de l'alerte (4 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique des solutions de cybersécurité n'est pas exigée ; aucun réglage d'équipement ni aucun essai technique ; le Zero Trust est un cadre d'architecture, non un produit ; aucune démarche de conformité formelle à une norme.

**Annexes mobilisées** : annexe 3.3 (tablettes, comptes rendus, réseau, renouvellement de 2027, pertes et vols, incidents, répartition actuelle des rôles), annexe 3.2 (accès permanent de l'éditeur, correctifs), annexe 3.5 (modèle Zero Trust, guide d'hygiène, ISO/IEC 27001:2022, RGPD) et annexe 1.1 (300 tablettes de 2021, 60 centres, organigramme, déléguée à la protection des données).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Architecture de confiance définie (authentification, chiffrement, segmentation ; Zero Trust comme modèle, non comme produit) ; mesures rattachées à une politique de sécurité fondée sur l'analyse des risques | 0,5 |
| a-2 | Authentification personnelle des équipages et chiffrement du stockage et de la transmission, chacun rattaché au risque traité | 0,5 |
| a-3 | Séparation des réseaux et effacement à distance, chacun rattaché au risque traité ; remplacement des tablettes de la fin de 2027 mis à profit | 0,5 |
| a-4 | Quatre indicateurs d'efficacité complets (formule, source, fréquence, cible, axe) | 0,5 |
| b-1 | Désignation d'un responsable de la sécurité des systèmes d'information, rattaché au directeur et indépendant de l'exploitation du système d'information, avec ses missions | 0,5 |
| b-2 | Rôles du directeur départemental, du (de la) chef(fe) du groupement et de la cheffe du service des systèmes d'information et de communication, distingués | 0,5 |
| b-3 | Rôles de la cheffe du centre de traitement de l'alerte et des chefs de centre | 0,5 |
| b-4 | Rôles de l'éditeur et de la déléguée à la protection des données, distingué du responsable de la sécurité | 0,5 |

**Réponse attendue**

*3.3 a) – L'architecture de confiance et quatre mesures*

**Définition** (a-1) : une **architecture de confiance** organise les identités, les terminaux, les réseaux, les applications et les données de façon que seules des personnes et des équipements **authentifiés** accèdent, selon leurs droits, à des ressources **cloisonnées**, et que les données restent **confidentielles et intègres**, y compris hors des locaux. Elle repose sur l'authentification, le chiffrement et la segmentation. Le **Zero Trust** en est un modèle : aucune confiance n'est accordée d'office à une tablette parce qu'elle est connectée au réseau du siège, chaque accès est vérifié. C'est un **cadre d'architecture**, conduit pas à pas, et non un produit que l'on achète (F12 § 3 ; annexe 3.5). Ces mesures s'inscrivent dans une **politique de sécurité fondée sur l'analyse des risques** : approuvée par le directeur, elle fixe les objectifs (confidentialité des données de santé, intégrité des comptes rendus, disponibilité de l'alerte, traçabilité), le périmètre, les règles, l'organisation et les contrôles ; chaque mesure y répond à un risque apprécié, et la charte d'usage n'en est que la déclinaison pour les utilisateurs (F12 § 1).

Risques à traiter, tirés de l'annexe 3.3 : la **divulgation de données de santé** par une tablette perdue ou volée (10 en 2026 ; plus de 1 000 comptes rendus dans la tablette volée en octobre) ou par un courriel non chiffré ; l'**usage d'une tablette par n'importe qui**, avec un code partagé par centre, inchangé depuis 2021 et connu d'agents partis, et des comptes rendus non imputables ; la **propagation d'une attaque** des tablettes ou de la bureautique vers le traitement de l'alerte, comme chez le SDIS voisin ; des **tablettes sans mises à jour de sécurité** (120 sur 300). Le remplacement des 300 tablettes, de septembre à décembre 2027, est l'occasion d'inscrire ces mesures dans les besoins des nouvelles tablettes, et de traiter les anciennes jusque-là.

| Mesure (a-2 et a-3) | Risque traité | Indicateur d'efficacité (a-4) : formule ; source ; fréquence ; cible ; axe |
|---|---|---|
| **1. Authentification personnelle des équipages** : chaque agent ouvre l'application de comptes rendus avec sa carte professionnelle sans contact et un code personnel, soit deux facteurs de nature différente (ce qu'il possède, ce qu'il sait) ; la tablette, partagée par l'équipage, ne compte pas comme facteur personnel ; fin du code commun à un centre ; fermeture automatique de la session | usage par un tiers d'une tablette perdue ou volée ; compte rendu non imputable (confidentialité, traçabilité) | **Part des comptes rendus rédigés après une authentification personnelle** : nombre de comptes rendus rédigés après authentification personnelle / nombre de comptes rendus rédigés × 100 ; journaux de l'application de comptes rendus ; mensuelle ; 100 % dès la mise en service des nouvelles tablettes à la fin de 2027 ; processus |
| **2. Chiffrement** : stockage des tablettes chiffré ; comptes rendus transmis au centre de régulation médicale du SAMU et aux six hôpitaux par une messagerie ou un espace d'échange chiffrés, et non plus en pièce jointe d'un courriel ordinaire | divulgation des données de santé en cas de vol ou d'interception (confidentialité, intégrité) ; une donnée chiffrée volée reste incompréhensible, ce qui évite d'informer les personnes (annexe 3.5) | **Part des comptes rendus transmis par un canal chiffré** : nombre de comptes rendus transmis par un canal chiffré / nombre de comptes rendus transmis × 100 ; journaux de la messagerie ou de l'espace d'échange ; mensuelle ; 100 % au 31/12/2027 ; processus |
| **3. Séparation des réseaux** : les tablettes n'accèdent qu'à une zone réservée à l'application de comptes rendus et à l'échange avec le logiciel de l'alerte ; les serveurs du traitement de l'alerte forment une zone à part, séparée de la bureautique ; seuls les flux nécessaires sont autorisés entre les zones | propagation d'un rançongiciel de la bureautique ou d'une tablette vers le traitement de l'alerte, comme chez le SDIS voisin (disponibilité, intégrité) | **Part des équipements rattachés à la zone de réseau prévue par la politique de sécurité** : nombre de tablettes, de postes et de serveurs dans leur zone / nombre d'équipements inventoriés × 100 ; inventaire du parc et revue des zones par le service des systèmes d'information et de communication ; trimestrielle ; 100 % au 31/12/2027 ; processus |
| **4. Effacement à distance** : toutes les tablettes inscrites dans un outil de gestion de flotte mobile (MDM, *Mobile Device Management*) qui permet de les localiser, de les bloquer, de les effacer à distance et d'imposer les mises à jour ; copie locale effacée dès que la transmission du compte rendu est confirmée ; toute perte déclarée sans délai au centre de traitement de l'alerte, ouvert jour et nuit, qui fait bloquer et effacer la tablette | divulgation des données d'une tablette perdue ou volée ; tablettes sans mises à jour (confidentialité) | **Part des tablettes perdues ou volées bloquées dans l'heure** : nombre de tablettes perdues ou volées dont le blocage et l'effacement ont été ordonnés moins d'une heure après la déclaration / nombre de tablettes perdues ou volées × 100 ; outil de gestion de flotte et registre des incidents ; mensuelle ; 100 %, contre 0 % aujourd'hui (aucun blocage possible) ; processus. Une tablette hors ligne ne s'efface qu'à sa reconnexion : le SDIS mesure l'ordre qu'il maîtrise |

Chaque indicateur est suivi par le responsable de la sécurité et présenté au comité de sécurité ; une cible manquée déclenche une action.

*3.3 b) – Les rôles et les responsabilités dans la gouvernance du traitement de l'alerte*

**Le responsable de la sécurité des systèmes d'information** (b-1) : le directeur départemental désigne un **responsable de la sécurité des systèmes d'information**, aujourd'hui absent. Il le **rattache directement à la direction départementale**, et non au service des systèmes d'information et de communication ni au groupement « Pilotage et systèmes d'information » qui exploite le système d'information : celui qui contrôle la sécurité ne doit pas contrôler son propre travail, et il doit pouvoir alerter le directeur sans filtre. Ce n'est pas un technicien : il pilote la politique de sécurité, conduit l'analyse des risques, organise la gestion des incidents et des crises, la sensibilisation et le suivi des indicateurs. Le système critique qu'est le traitement de l'alerte justifie un poste à part entière, avec un correspondant au service des systèmes d'information et de communication.

| Acteur | Rôle et responsabilités dans la gouvernance du traitement de l'alerte |
|---|---|
| **Directeur départemental** (colonel hors classe GRANVOISE) (b-2) | responsable de la sécurité de l'établissement : approuve la politique de sécurité et les niveaux de risque acceptables, accepte formellement les risques résiduels, désigne le responsable de la sécurité, donne les moyens, préside un comité de sécurité semestriel, rend compte au conseil d'administration (01/07/2027) |
| **Chef(fe) du groupement « Pilotage et systèmes d'information »** (vous) (b-2) | intègre la sécurité dans les projets (remplacement des tablettes, suite du logiciel de traitement de l'alerte, hébergement des serveurs), veille à ce que le service applique les mesures, suit la relation avec l'éditeur et prépare avec le responsable de la sécurité les décisions du directeur ; n'est pas le contrôleur de la sécurité |
| **Cheffe du service des systèmes d'information et de communication** (Mme VARANGEOT) (b-2) | met en œuvre les mesures : séparation des réseaux, gestion de flotte des tablettes, comptes et accès, mises à jour, sauvegardes ; ouvre et ferme les accès de l'éditeur ; traite les incidents techniques et les signale au responsable de la sécurité |
| **Cheffe du centre de traitement de l'alerte** (commandante TOURNEVAL) (b-3) | propriétaire métier du système critique : exprime les besoins de disponibilité, valide la date et l'ordre d'installation des correctifs (d'abord une salle, puis l'autre, jamais aux heures chargées), décide de la bascule et du mode dégradé, reçoit jour et nuit les déclarations de perte de tablettes et fait déclencher l'effacement |
| **Chefs de centre** (b-3) | correspondants de sécurité dans les 60 centres : font respecter l'authentification personnelle et l'interdiction de partager les codes, déclarent sans délai toute perte ou tout vol, signalent les arrivées et les départs des agents, relaient la sensibilisation |
| **Éditeur du logiciel de traitement de l'alerte** (b-4) | prestataire : livre des correctifs essayés sur sa plateforme et installés à une date validée par le centre de traitement de l'alerte, une salle après l'autre ; intervient par des accès nominatifs, ouverts à la demande et tracés ; signale ses incidents et les failles connues ; remet la documentation des interfaces ; s'engage sur le calendrier de fin de maintenance |
| **Déléguée à la protection des données** (Mme FAVERJON) (b-4) | conseille sur la protection des données de santé (aucune copie durable sur les tablettes, chiffrement) ; est informée sans délai de toute perte, de tout vol et de tout incident ; tient le registre des violations et prépare, si la violation présente un risque, la notification à l'autorité de contrôle dans les meilleurs délais et, si possible, dans les 72 heures (annexe 3.5) ; distincte du responsable de la sécurité, qui protège tous les systèmes, elle veille aux droits des personnes |
| **Responsable de la sécurité des systèmes d'information** (à désigner) (b-1) | rédige et fait vivre la politique de sécurité, conduit l'analyse des risques (question 3.2), contrôle l'application des mesures et les indicateurs, organise la gestion des incidents et des crises et les exercices, alerte le directeur |

**Réponses tolérées**
- Autres mesures de même objet : code personnel seul, carte seule ou reconnaissance biométrique, si l'authentification est personnelle et que le candidat ne la présente pas comme une authentification à deux facteurs ; espace d'échange sécurisé à la place d'une messagerie chiffrée ; gestion des applications seules plutôt que de toute la tablette, si l'effacement à distance des données est assuré.
- Indicateurs différents s'ils mesurent l'efficacité de la mesure et sont complets : part des tablettes dont le stockage est chiffré ; nombre de flux non autorisés constatés vers la zone de l'alerte (cible zéro) ; part des tablettes à jour de leurs correctifs de sécurité.
- Responsable de la sécurité rattaché au (à la) chef(fe) du groupement, avec un accès direct au directeur et une indépendance garantie vis-à-vis du service qui exploite le système d'information ; poste partagé avec un autre établissement public, si la disponibilité qu'exige un système critique est discutée.
- Comité de sécurité, sapeurs-pompiers utilisateurs ou centre de régulation médicale du SAMU et hôpitaux ajoutés au tableau.

**Erreurs fréquentes**
- *Zero Trust présenté comme un produit à acheter* (`ET-04`, `JUR-S03`) — juste : un cadre d'architecture, appliqué pas à pas aux tablettes et au réseau.
- *Code à quatre chiffres « plus long » présenté comme une authentification forte* (`ET-28`) — juste : un moyen personnel, et deux facteurs de nature différente.
- *Mesures sans indicateur, ou indicateurs génériques* (`ET-18`, `JUR-S05`) — juste : un indicateur par mesure, avec sa formule, sa source, sa fréquence, sa cible et son axe.
- *Responsable de la sécurité présenté comme un technicien, ou placé sous la cheffe du service qui exploite le système d'information* (`ET-15`) — juste : rattaché au directeur, il pilote et contrôle.
- *Déléguée à la protection des données confondue avec le responsable de la sécurité* (`ET-29`) — juste : deux rôles distincts, qui travaillent ensemble.
- *Réglage des équipements, essais techniques, analyse juridique de la violation de données* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Architecture de confiance, authentification à deux facteurs, gestion de flotte mobile | authentification, chiffrement, segmentation | F12 § 3 | notion de cours |
| Le modèle Zero Trust, avis de l'ANSSI (2021) | cadre d'architecture, non un produit | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | authentification, cloisonnement, appareils mobiles, mises à jour | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Politique de sécurité, acteurs | objectifs, périmètre, règles, organisation ; responsable de la sécurité, déléguée à la protection des données | F12 § 1 ; F15 § 1 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | sécurité des données de santé, registre et notification des violations, en principe | `rgpd` ; F15 § 6 | applicable depuis le 25/05/2018 |

---

### 3.4 – Les salles informatiques et la transition numérique responsable (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : aucun calcul d'empreinte, aucun chiffre d'étude sur l'empreinte du numérique, aucun assujettissement à un cadre de durabilité ; la durabilité est intégrée à la gouvernance du système d'information.

**Annexes mobilisées** : annexe 3.4 (deux salles, consommations, serveurs peu utilisés, renouvellement, proposition du département, deux avis), annexe 3.3 (remplacement des tablettes à la fin de 2027, données de santé), annexe 3.5 (RGPD : sous-traitant) et annexe 1.1 (salle du siège et salle de secours, financement par le département à 55 %, président du conseil d'administration vice-président du conseil départemental, objectif de baisse de 20 % de l'empreinte).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Transition numérique responsable définie ; apports de la proposition appliqués au cas (30 serveurs utilisés à 10 %, virtualisation, indicateur de 1,3 contre environ 2 au siège, chaleur récupérée, mesure continue) | 0,5 |
| a-2 | Limites appliquées au cas : dépendance envers le département, exploitation sans astreinte alors que la messagerie sert jour et nuit, données de santé et sous-traitance, salle du siège conservée avec sa climatisation de 2008, empreinte déplacée | 0,5 |
| a-3 | Conclusion : proposition recommandée sous conditions précises (périmètre, convention, sécurité, réversibilité, mesure partagée, redimensionnement de la salle du siège) | 0,5 |
| b-1 | Allongement de la durée de vie justifié (900 postes renouvelés tous les quatre ans ; fabrication), avec ses conditions | 0,5 |
| b-2 | Réemploi justifié (équipements détruits aujourd'hui ; tablettes de 2021 et serveurs libérés), avec un effacement sûr des données | 0,5 |
| b-3 | Deux indicateurs complets (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.4 a) – La proposition du département*

**Définition** (a-1) : la **transition numérique responsable** est la trajectoire par laquelle une organisation réduit durablement l'empreinte environnementale de son système d'information sur tout son cycle de vie (fabrication, usage, fin de vie). Elle combine la sobriété, qui interroge d'abord le besoin, les bonnes pratiques du Green IT (mutualisation, virtualisation, centres de données efficaces, durée de vie des équipements) et une gouvernance qui mesure, fixe des cibles et arbitre, sans dégrader le service rendu ni la sécurité (F14 § 3 et § 5). Pour le SDIS, elle sert l'objectif d'une baisse de 20 % de l'empreinte d'ici 2031, que rien ne permet aujourd'hui de suivre, l'empreinte du système d'information n'ayant jamais été mesurée.

**Ce qu'apporte la proposition** :
- la **mutualisation** et la **virtualisation** : 30 serveurs de gestion, dont 8 seulement virtualisés, utilisés en moyenne à 10 % de leur capacité, deviendraient des serveurs virtuels sur des équipements partagés. Moins de machines à fabriquer et à alimenter, à service égal ;
- une **salle plus efficace** : l'indicateur d'efficacité énergétique de la salle du département est de 1,3, contre environ 2 au siège (400 MWh consommés pour 200 MWh d'équipements informatiques). Au siège, la moitié de l'électricité sert à autre chose que l'informatique, surtout à une climatisation de 2008 ;
- la **chaleur récupérée** pour chauffer un collège voisin : l'énergie dissipée par les serveurs remplace une partie du chauffage d'un autre bâtiment ;
- la **mesure continue** de la consommation : elle fournit la donnée de départ qui manque pour suivre l'objectif de 2031.

**Ses limites** (a-2) :
- la **dépendance** envers le département, déjà financeur à 55 % : ses priorités passeraient d'abord, et la convention n'est pas écrite (niveaux de service, retour en arrière, sortie) ;
- l'**exploitation** : les agents du département ne sont présents que les jours ouvrés, de 8 heures à 18 heures, sans astreinte, alors que la messagerie sert jour et nuit à envoyer les comptes rendus de secours. Ces serveurs « de gestion » servent donc aussi l'activité opérationnelle ;
- la **sécurité et la confidentialité** : les comptes rendus contiennent des données de santé. Le département deviendrait un sous-traitant, lié par un contrat qui fixe les mesures de sécurité (annexe 3.5). Ses agents ne doivent pas accéder aux données, et la liaison entre les deux réseaux ne doit pas propager une attaque ;
- le **système critique conservé** dans les salles du SDIS : c'est un bon choix pour la maîtrise de l'alerte, mais la salle du siège garde ses 10 serveurs opérationnels et une climatisation de 2008, déjà tombée en panne en juillet 2026 : il faudra la remplacer, redimensionnée ;
- l'**empreinte déplacée** plutôt que supprimée : la part de la salle du département imputable au SDIS doit être comptée dans son empreinte, et la facilité de créer des serveurs virtuels peut en multiplier le nombre (effet rebond).

**Conclusion** (a-3) : recommander la proposition, **sous conditions** :
1. un **périmètre** limité aux applications de gestion qui peuvent attendre un jour ouvré (ressources humaines et paie, finances, formation, parc, indemnités) ; la messagerie et les comptes rendus de secours ne partent que si une astreinte jour et nuit et le chiffrement des données sont garantis, sinon ils restent dans les salles du SDIS ;
2. une **convention** qui fixe les niveaux de service, l'astreinte, les règles de sécurité, le contrat de sous-traitance, la notification des incidents, la réversibilité, et la communication chaque mois de la consommation imputable au SDIS ;
3. le **démontage** des 30 serveurs physiques, réemployés plutôt que détruits, puis le **redimensionnement** de la salle du siège et de sa climatisation pour les seuls serveurs de l'alerte ;
4. l'inscription de l'opération dans la trajectoire de 2031, avec une mesure de départ en 2027.

*3.4 b) – Deux bonnes pratiques et deux indicateurs*

**Allonger la durée de vie des équipements** (b-1) : passer de quatre à six ans pour les 900 postes de travail, et au-delà de quatre ans pour les serveurs conservés. Les achats de postes tomberaient d'environ 225 à 150 par an, soit un tiers de moins. Or c'est la **fabrication** qui pèse souvent le plus dans l'empreinte d'un équipement, plus que son électricité (F14 § 1 et § 3). Conditions : réparation et remplacement des pièces d'usure (batteries, disques), logiciels qui restent compatibles, choix de matériels réparables et mis à jour longtemps, en particulier pour les nouvelles tablettes de 2027.

**Réemployer plutôt que détruire** (b-2) : aujourd'hui, tous les équipements remplacés sont détruits. Les postes et les tablettes encore utilisables sont réemployés en interne (formation, centres armés par des volontaires), reconditionnés par une entreprise spécialisée ou donnés à des associations ou à des établissements scolaires ; seuls les équipements irréparables vont au recyclage. Les premiers candidats sont les 300 tablettes de 2021, remplacées à la fin de 2027, et les serveurs libérés par l'hébergement. Condition propre au SDIS : un **effacement sûr et attesté** des données avant toute sortie, car les tablettes ont contenu des comptes rendus de secours (question 3.3).

**Deux indicateurs de l'impact environnemental du système d'information** (b-3) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Électricité consommée par l'hébergement du système d'information** | somme des MWh consommés par les deux salles du SDIS et des MWh imputés au SDIS par la salle du département | compteurs des salles du SDIS ; relevé mensuel de la consommation imputée au SDIS par le département | mensuelle, bilan annuel | au moins − 30 % en 2029 par rapport à 2026 (430 MWh pour les deux salles du SDIS) | environnement |
| **Taux de réemploi des équipements retirés** | nombre d'équipements retirés réemployés ou reconditionnés / nombre d'équipements retirés × 100 | inventaire du parc informatique et attestations de reprise et d'effacement | annuelle | 70 % en 2028, contre 0 % aujourd'hui | environnement |

**Réponses tolérées**
- Proposition refusée, ou limitée à quelques applications, si l'argument est la sécurité des données de santé ou l'absence d'astreinte, et si une autre voie de réduction est proposée (virtualisation des 30 serveurs dans la salle du siège, puis remplacement de sa climatisation).
- Durée de vie portée à cinq ans, ou à sept ans pour les serveurs, si elle est justifiée et assortie de conditions.
- Autres indicateurs complets : âge moyen des postes à leur retrait (cible six ans) ; indicateur d'efficacité énergétique de la salle du siège après le remplacement de sa climatisation ; taux d'utilisation moyen des serveurs ; « PUE » employé pour l'indicateur d'efficacité énergétique de la salle ; part des achats d'équipements assortis de critères de durabilité.
- Cible de consommation différente si elle est datée, chiffrée et rapportée à une valeur de départ.

**Erreurs fréquentes**
- *Empreinte du système d'information réduite à l'électricité* (`ET-38`) — juste : la fabrication des équipements renouvelés tous les quatre ans et leur destruction pèsent au moins autant ; d'où la durée de vie et le réemploi.
- *Sobriété ou Green IT confondus avec une simple économie d'énergie* (`ET-12`) — juste : interroger le besoin (30 serveurs à 10 %), mutualiser, allonger la durée de vie.
- *Hébergement chez le département présenté comme sans risque, ou « tout externaliser »* (`ET-30`, `JUR-G11`) — juste : astreinte, données de santé, dépendance, convention.
- *Indicateurs incomplets ou génériques* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe, reliés à l'objectif de 2031.
- *Calcul d'empreinte, chiffres d'études, assujettissement du SDIS à un cadre de durabilité* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Green IT, mutualisation, virtualisation, durée de vie, réemploi | bonnes pratiques et leviers | F14 § 3 | notion de cours |
| Indicateur d'efficacité énergétique d'une salle, consommation, durée de vie | indicateurs de l'impact environnemental du SI | F14 § 4 | notion de cours |
| Centres de données efficaces, chaleur récupérée, hébergement mutualisé | transition numérique responsable | F14 § 5 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | sous-traitant lié par un contrat qui fixe les mesures de sécurité, en principe | `rgpd` ; F15 § 5 | applicable depuis le 25/05/2018 |
