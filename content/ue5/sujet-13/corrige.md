# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 13

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Préparer le schéma directeur numérique et la transmission des savoirs | 14 | 1.1 à 1.4 | `exercices/ex37_schema_directeur_maturite_savoirs` |
| 2 – Organiser et exploiter les données de la redevance incitative | 13 | 2.1 à 2.5 | `exercices/ex38_donnees_redevance_incitative` |
| 3 – Fiabiliser, sécuriser et rendre plus sobre le système d'information | 13 | 3.1 à 3.4 | `exercices/ex39_audit_piscines_facturation_objets_sobriete` |
| **Total** | **40** | | |

---

## DOSSIER 1 – PRÉPARER LE SCHÉMA DIRECTEUR NUMÉRIQUE ET LA TRANSMISSION DES SAVOIRS (14 points)

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Le schéma directeur numérique 2028-2032 et l'alignement du système d'information mutualisé | `1.1.c` Méthodologies de planification stratégique du SI ; `1.1.b` Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) | 4 |
| 1.2 La maturité numérique et la gouvernance de la direction du numérique mutualisée | `1.2.d` Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) ; `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité | 3,5 |
| 1.3 Les demandes des usagers et le guichet unique | `1.3.f` Analyse des processus métiers et rôle des architectures SI dans leur rationalisation ; `1.3.a` Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) | 3 |
| 1.4 La transmission des savoirs des agents qui partent | `1.6.a` Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle ; `1.6.d` Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums ; `1.6.e` Leviers d'appropriation et de transformation des pratiques professionnelles | 3,5 |
| **Dossier 1 – Préparer le schéma directeur numérique et la transmission des savoirs** |  | **14** |

Répartition indicative : connaissances (schéma directeur, alignement stratégique, maturité et modèles de maturité, gouvernance du SI, urbanisation, savoirs tacites et explicites) environ 3 points (items 1.1 a-1, 1.1 b-1, 1.2 a-1, la moitié de 1.2 b-1, la moitié de 1.3 b-1, la moitié de 1.4 a-1) ; analyse des annexes et recommandations environ 11 points, soit environ 79 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – Le schéma directeur numérique 2028-2032 et l'alignement du système d'information mutualisé (4 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.c` « Méthodologies de planification stratégique du SI » ; `1.1.b` « Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 1.2 (bilan du schéma 2022-2026, arbitrages, comité de pilotage, délais par collectivité, consultation des communes, témoignages des élus, du maire et d'une responsable de service) et 1.1 (deux collectivités, 30 communes, 18 communes du service commun, 600 agents de terrain).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Schéma directeur défini (planification du SI sur trois à cinq ans à partir de la stratégie : diagnostic, orientations, cible, portefeuille priorisé, moyens, pilotage), distingué d'un plan de projet ; horizon 2028-2032 calé sur « Castelrive 2032 » et commun aux deux collectivités | 0,5 |
| a-2 | Étapes ordonnées et datées de façon réaliste (cadrage et gouvernance de la démarche, diagnostic partagé, orientations tirées du projet de territoire, cible et scénarios, portefeuille et moyens, validation et révision annuelle) | 0,5 |
| a-3 | Acteurs et rôle de chacun : élus des deux collectivités, directions générales, DGA ressources, direction du numérique, directions métiers, 30 communes (dont les 18 du service commun), agents dont ceux du terrain, usagers | 0,5 |
| a-4 | Livrables par étape (note de cadrage, diagnostic, orientations, cible, schéma directeur et portefeuille, dispositif de suivi) | 0,5 |
| b-1 | Alignement stratégique défini (mise en cohérence permanente de la stratégie du SI et de celle de l'organisation, qui n'est pas une simple adéquation technique ; dimension organisationnelle et de gouvernance) ; ici, alignement sur les objectifs d'un projet de territoire commun à deux collectivités | 0,5 |
| b-2 | Premier décalage, rattaché à un objectif de « Castelrive 2032 » et appuyé sur les faits de l'annexe 1.2 | 0,5 |
| b-3 | Deuxième décalage, rattaché à un objectif et appuyé sur les faits | 0,5 |
| b-4 | Troisième décalage, rattaché à un objectif et appuyé sur les faits ; conclusion d'ensemble (alignement faible, d'abord pour des raisons de gouvernance) | 0,5 |

**Réponse attendue**

*1.1 a) – La démarche d'élaboration du schéma directeur 2028-2032*

Le **schéma directeur numérique** (schéma directeur du système d'information) est le document de planification qui fixe, pour trois à cinq ans et à partir de la stratégie de l'organisation, les orientations du système d'information, sa cible (applications, données, organisation, compétences), le portefeuille de projets priorisé, les moyens en ordre de grandeur et le dispositif de pilotage. Il se distingue du plan de projet, qui organise un projet particulier (tâches, ressources, délais). Ici, son horizon 2028-2032 coïncide avec celui de « Castelrive 2032 », et il doit être **commun à la ville et à l'agglomération**, puisqu'une seule direction du numérique sert les deux collectivités (0,5 pt).

L'annexe 1.2 montre ce qu'il faut éviter : un schéma 2022-2026 **rédigé par la seule direction du numérique**, sans élus, sans communes et sans pilotage (comité réuni une seule fois depuis 2022). La démarche proposée part du projet de territoire et associe toutes les parties prenantes.

| Étape (calendrier indicatif) | Contenu | Acteurs principaux | Livrable |
|---|---|---|---|
| 1. Cadrage et gouvernance de la démarche (mai-juin 2027) | mandat commun des deux exécutifs ; périmètre (deux collectivités, services aux 18 communes) ; comité de pilotage commun présidé par les élus, équipe projet ; calendrier et méthode de concertation | président, vice-présidente chargée du numérique et élu de la ville ; directrices et directeurs généraux des deux collectivités ; DGA ressources (pilotage côté agglomération) ; directeur du numérique | note de cadrage validée par le comité de pilotage |
| 2. Diagnostic partagé (juin-septembre 2027) | bilan du schéma 2022-2026 (18 projets, 11 projets hors schéma) ; cartographie des applications et des processus ; maturité réévaluée avec les services (question 1.2) ; coûts en ordre de grandeur ; écoute des usagers, des agents et des communes | direction du numérique, directions métiers, service de la relation aux usagers, ressources humaines ; enquête auprès des 30 communes ; ateliers d'agents, y compris de terrain, aux heures de prise de poste | rapport de diagnostic et synthèse des attentes |
| 3. Orientations (septembre-octobre 2027) | traduction des cinq objectifs de « Castelrive 2032 », et des priorités de la ville, en axes numériques ; ateliers par politique publique (déchets, piscines, relation aux usagers, services techniques) | élus et directions métiers, avec la direction du numérique | axes stratégiques validés par les élus |
| 4. Cible et scénarios (octobre-novembre 2027) | architecture cible (guichet unique, référentiels communs), organisation et compétences, gouvernance ; deux ou trois scénarios d'effort | direction du numérique, directions métiers ; RSSI et DPO consultés | cible et scénarios comparés |
| 5. Portefeuille et moyens (novembre-décembre 2027) | projets priorisés selon des critères partagés (question 1.2 b), moyens en ordre de grandeur, répartition de la capacité entre les collectivités, risques | comité de pilotage commun | document du schéma directeur 2028-2032 |
| 6. Validation et pilotage (fin 2027, puis chaque année) | présentation aux élus des deux collectivités et aux communes ; indicateurs de suivi ; revue annuelle et révision à mi-parcours | comité stratégique (question 1.2 b) | tableau de suivi et bilan annuel |

**Acteurs et rôles** (0,5 pt) : les **élus** (président, vice-présidente chargée du numérique, élu de la ville) commanditent et arbitrent, ce que demande le président (« celui de nos deux collectivités ») ; les **directions générales** des deux collectivités coordonnent ; le (la) **DGA ressources** pilote la démarche pour l'agglomération et veille à l'équilibre entre les deux collectivités ; la **direction du numérique** apporte le diagnostic technique, la cible et les estimations, sans être le seul rédacteur ; les **directions métiers** expriment les besoins et portent les projets ; les **30 communes**, et non les seules 18 du service commun, sont consultées par une enquête et des ateliers par taille de commune, avec des représentants au comité de pilotage, parce que le guichet unique passe par leurs mairies ; les **agents**, dont les 600 agents de terrain, sont écoutés sur leurs outils et sur la transmission des savoirs ; les **usagers** sont associés par une enquête, un panel et l'exploitation des demandes reçues par le service de la relation aux usagers.

**Livrables** (0,5 pt) : note de cadrage, rapport de diagnostic, axes validés, cible et scénarios, schéma directeur et portefeuille priorisé, tableau de suivi et bilans annuels.

*1.1 b) – L'alignement du système d'information mutualisé sur « Castelrive 2032 »*

L'**alignement stratégique** est la mise en cohérence permanente de la stratégie du système d'information avec la stratégie de l'organisation : il est dynamique (il se refait quand la stratégie change), réciproque et autant organisationnel que technique ; il ne se réduit ni au choix d'un logiciel ni à une adéquation technique. Ici, la stratégie de référence est un projet de territoire, et le SI est partagé par deux collectivités : l'alignement suppose que les priorités du numérique soient décidées à partir de « Castelrive 2032 » et arbitrées entre les deux collectivités (0,5 pt).

**Trois décalages** (0,5 pt chacun ; trois parmi les suivants) :

| Objectif de « Castelrive 2032 » | Faits de l'annexe 1.2 | Décalage |
|---|---|---|
| Simplifier les démarches par un guichet unique, en ligne et dans les mairies | portail unique des démarches prévu pour 2024, abandonné en 2026 « faute de service pour le porter » ; une quarantaine de formulaires en ligne ; la vice-présidente « ne sait pas qui doit porter le guichet unique » ; les secrétaires de mairie transfèrent des courriels « sans savoir ce qu'elles deviennent » | l'objectif premier du projet de territoire n'a ni projet ni porteur métier ; le SI a numérisé des formulaires sans transformer le service rendu |
| Tous les objectifs (le schéma comme traduction du projet de territoire) | 11 projets hors schéma, lancés à la demande d'un service, ont absorbé environ 30 % du temps des équipes de projet ; billetterie des piscines choisie par leur responsable, découverte par l'élue dans la presse ; arbitrages faits chaque lundi par le directeur du numérique « selon l'urgence et l'insistance » ; 9 projets réalisés sur 18 | le portefeuille est tiré par la demande des services et par l'insistance, non par les priorités politiques : la direction du numérique décide seule de ce qui sert la stratégie |
| Un projet pour toutes les communes et les deux collectivités (président : « toutes les communes, et pas seulement la ville-centre ») | demandes traitées en 3 mois pour la ville et en 7 mois pour l'agglomération ; comité de pilotage commun réuni une seule fois depuis 2022 au lieu de deux fois par an ; communes consultées une seule fois, 6 réponses sur 18 ; clé de répartition contestée | le SI mutualisé est aligné de fait sur la ville, qui est proche et relance ; l'agglomération et les communes ne disposent d'aucune instance pour faire valoir leurs priorités |
| Garantir la continuité et la sécurité des services publics | plan de continuité du SI reporté deux fois | un objectif du projet de territoire reste sans traduction, alors que le SI porte des services quotidiens (collecte, déchèteries, piscines) |
| Piloter par les données ; réduire l'empreinte du numérique | « aucun projet du schéma ne portait sur les données ni sur l'empreinte environnementale du numérique » ; numérique responsable noté 1 | deux objectifs nouveaux du projet de territoire n'ont aucun point d'appui dans le SI actuel |
| Un tiers des agents techniques en retraite d'ici 2032 (savoirs, continuité) | accès des agents de terrain à l'intranet depuis un téléphone abandonné en 2025 ; 600 agents sans poste | le SI est conçu pour les agents de bureau ; il ne soutient pas les métiers de terrain qui portent les services |

**Conclusion** (0,5 pt avec le troisième décalage) : l'alignement est faible. La cause principale n'est pas technique : c'est l'absence de gouvernance commune (élus absents, comité qui ne se réunit pas, arbitrages par le directeur du numérique), qui laisse le portefeuille se former au fil des demandes et favorise la ville. Le schéma 2028-2032 doit donc partir des objectifs de « Castelrive 2032 », être porté par les élus des deux collectivités et s'accompagner d'instances d'arbitrage (question 1.2 b) ; le guichet unique en est le projet structurant.

**Réponses tolérées**
- Démarche présentée en quatre ou cinq étapes, ou selon un autre découpage cohérent (diagnostic, vision, trajectoire, pilotage), si les acteurs et les livrables sont précisés ; appui sur une assistance à maîtrise d'ouvrage extérieure, si le pilotage reste aux collectivités.
- Calendrier différent, s'il permet d'adopter le schéma avant 2028.
- Alignement analysé à l'aide du modèle de Henderson et Venkatraman (1993) : décalage d'**intégration fonctionnelle** entre la stratégie de l'organisation (projet de territoire) et la stratégie du SI (schéma rédigé par la direction du numérique), et d'**ajustement** entre stratégie et organisation (pas d'instance, pas de porteur) ; le modèle est valorisé mais non exigé.
- Autres décalages tirés de l'annexe 1.2, s'ils sont rattachés à un objectif et appuyés sur des faits.

**Erreurs fréquentes**
- *Alignement réduit à un choix technique ou logiciel* (`ET-06` ; `JUR-G02` alignement réduit à un choix technique ou à une standardisation logicielle) — « il suffit d'acheter un portail de démarches » ; juste : l'alignement est d'abord une question de priorités et de gouvernance partagées.
- *Schéma directeur confondu avec un plan de projet* (`ET-07`) — liste de tâches ou planning détaillé d'un projet ; juste : démarche de planification stratégique, acteurs et livrables.
- *Démarche conduite par la seule direction du numérique* (`JUR-T01` contextualiser chaque notion) — démarche générique qui oublie les élus, les communes, les agents de terrain ou les usagers, alors que l'annexe 1.2 en fait la cause de l'échec du schéma précédent.
- *Décalages sans faits* (`JUR-T08` exploiter toutes les annexes) — objectifs repris sans les chiffres de l'annexe 1.2 (11 projets hors schéma, 3 et 7 mois, une seule réunion depuis 2022).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Schéma directeur du SI | planification sur trois à cinq ans ; démarche ; distinction avec le plan de projet | F01 § 3.1 ; `erreurs_types.md` ET-07 | notion de cours |
| Alignement stratégique | mise en cohérence permanente, non réduite à l'adéquation technique | F01 § 1 ; `erreurs_types.md` ET-06 | notion de cours |
| Henderson et Venkatraman, *IBM Systems Journal*, 1993 (modèle SAM) | ajustement stratégique et intégration fonctionnelle (réponse tolérée) | `henderson_venkatraman_1993` ; F01 § 1 | publié |

---

### 1.2 – La maturité numérique et la gouvernance de la direction du numérique mutualisée (3,5 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.d` « Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) » ; `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ».

**Annexes mobilisées** : annexes 1.2 (auto-évaluation, échelle, justifications et conclusion ; bilan, arbitrages, comité, délais, communes, témoignages) et 1.3 (ressaisies, absence de suivi, relances, délais).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Principe d'une évaluation de la maturité (domaines, niveaux décrits, positionnement fondé sur des preuves, cible et plan de progression) en référence à un modèle (CMMI, niveaux de capacité de COBIT 2019, MAGNum 2026) | 0,5 |
| a-2 | Deux limites de la méthode suivie (évaluation par le seul prestataire interne, juge et partie ; note unique pour deux collectivités ; justification par l'existence d'un document ; absence de cible, conclusion orientée) | 0,5 |
| a-3 | Deux écarts entre notes et faits, chacun avec le niveau défendable (gouvernance, services aux usagers, compétences, stratégie) | 0,5 |
| a-4 | Deux domaines prioritaires justifiés par « Castelrive 2032 » et par les annexes | 0,5 |
| b-1 | Gouvernance du SI définie (évaluer, orienter, surveiller ; distincte du management) ; deux instances communes avec composition, fréquence et décisions | 0,5 |
| b-2 | Place des 18 petites communes membres (représentation, consultation, relais dans les mairies), et non leur simple information | 0,5 |
| b-3 | Quatre critères d'arbitrage explicites et applicables aux deux collectivités, dont un critère de durabilité ou de coût global, et une règle d'équité ou de circuit unique des demandes | 0,5 |

**Réponse attendue**

*1.2 a) – L'interprétation de l'auto-évaluation de maturité*

Évaluer la **maturité numérique**, c'est situer l'organisation, domaine par domaine, sur une échelle de niveaux décrits de façon observable, à partir de **preuves** (pratiques constatées, mesures), pour fixer une cible et un plan de progression. Le modèle **CMMI** propose cinq niveaux de maturité (initial, géré, défini, géré quantitativement, en optimisation) ; **COBIT 2019** évalue la capacité des processus de 0 à 5 ; le modèle MAGNum 2026 du Cigref, de l'IFACI et de l'ISACA France applique cette logique à la gouvernance du numérique. L'échelle de l'annexe 1.2 B s'inspire du CMMI : le niveau 3 suppose des règles communes **appliquées** par les deux collectivités, le niveau 4 des indicateurs et des cibles **connus de tous** (0,5 pt).

**Deux limites de la méthode** (0,5 pt ; deux parmi les suivantes) :
- **Une auto-évaluation par le seul prestataire interne** : la direction du numérique s'est notée elle-même, sans entretien avec les services, les élus ou les communes ; elle est juge et partie, et sa conclusion (« ce qui nous manque, ce sont des moyens ») sert sa demande de moyens.
- **Une note unique pour deux collectivités** dont la situation diffère (3 mois contre 7 mois pour une demande d'évolution) : la moyenne masque l'inégalité de service, et les communes membres ne sont pas évaluées.
- **Des justifications fondées sur l'existence d'un document ou d'une intention**, non sur les pratiques : un schéma « adopté », un comité « prévu », une politique « rédigée » ne prouvent pas que les règles sont appliquées (niveau 3).
- **Aucune cible ni aucun lien avec « Castelrive 2032 »** : l'évaluation ne dit pas quel niveau viser, ni dans quels domaines.

**Deux écarts entre notes et faits** (0,5 pt ; deux parmi les suivants) :

| Domaine | Note | Faits relatés | Niveau défendable |
|---|---|---|---|
| Gouvernance | 3 | comité de pilotage réuni une seule fois depuis 2022 au lieu de deux fois par an ; priorités arbitrées chaque lundi par le directeur du numérique « selon l'urgence et l'insistance » ; élus non associés | 1 (dépend d'une personne) ou 2 au mieux |
| Services aux usagers | 4 | formulaires ressaisis à la main, emménagement saisi trois fois, trois logiciels non reliés, aucun numéro de suivi, 35 % des demandes relancées, 15 jours pour un bac au lieu des 5 jours affichés (annexe 1.3) : aucun indicateur ni aucune cible ne sont suivis | 2 |
| Compétences | 4 | la justification ne porte que sur les 45 agents de la direction du numérique ; 600 agents de terrain sans poste, accès à l'intranet depuis un téléphone abandonné en 2025 (annexe 1.2) ; GED utilisée par 2 services (annexe 1.4, accepté) | 2 |
| Stratégie numérique | 3 | 9 projets réalisés sur 18, 11 projets hors schéma pour environ 30 % du temps, schéma rédigé par la direction du numérique sans les élus | 2 |
| Sécurité | 3 | politique « rédigée en 2023 », mais plan de continuité du SI reporté deux fois (annexe 1.2 A) | 2 |

**Deux domaines prioritaires** (0,5 pt) : la **gouvernance**, parce qu'elle conditionne tous les autres (sans instance ni critères, le prochain schéma subira le même sort que le précédent) et parce que l'agglomération et les communes n'ont aucun moyen de faire valoir leurs priorités ; les **services aux usagers**, parce que le guichet unique est le premier objectif de « Castelrive 2032 » et que l'écart entre la note (4) et les faits y est le plus fort. La première action est de **refaire l'évaluation de façon contradictoire** : entretiens avec les services des deux collectivités, les élus et un échantillon de communes, preuves pour chaque note, une note par collectivité, cible à 2032.

*1.2 b) – La gouvernance de la direction du numérique mutualisée*

La **gouvernance du système d'information** est le dispositif (instances, rôles, règles) par lequel les dirigeants **évaluent** les besoins et les options, **orientent** les choix et les priorités et **surveillent** la mise en œuvre et la performance du SI ; elle se distingue du **management**, confié ici au directeur du numérique, qui planifie et exécute. Dans une direction mutualisée, elle doit permettre à chaque collectivité de peser sur des choix qu'elle finance, alors qu'aujourd'hui le directeur du numérique arbitre seul (0,5 pt avec les instances).

| Instance | Composition | Fréquence | Décisions |
|---|---|---|---|
| **Comité stratégique du numérique mutualisé** | coprésidé par la vice-présidente de l'agglomération chargée du numérique et l'élu de la ville chargé du numérique ; directrices et directeurs généraux des deux collectivités ; DGA ressources ; directeur du numérique ; deux représentants des communes membres ; RSSI et DPO invités | deux fois par an au moins (comme le prévoit la convention), trimestrielle pendant l'élaboration du schéma | adopte le schéma directeur et le portefeuille annuel ; répartit la capacité de la direction du numérique entre les collectivités ; tranche les conflits remontés par le comité d'arbitrage ; suit l'avancement, la qualité de service et les risques ; demande une étude de la clé de répartition (sans la recalculer ici) |
| **Comité d'arbitrage des demandes et des projets** | DGA ressources de l'agglomération et son homologue de la ville ; directeur du numérique ; un représentant par direction métier concernée ; un correspondant des communes | mensuelle | instruit toute demande au-delà d'un seuil d'effort fixé ; la classe selon les critères ci-dessous ; publie la file des demandes et leur rang ; lance ou arrête les projets dans l'enveloppe fixée par le comité stratégique ; remonte les désaccords |

**La place des 18 petites communes membres** (0,5 pt) : deux élus désignés par les maires des communes membres siègent au comité stratégique (par exemple un pour les communes moyennes, un pour les communes rurales) ; un correspondant au comité d'arbitrage ; une consultation annuelle sur le catalogue des services proposés et sur leur qualité, et non un questionnaire unique tous les cinq ans (6 réponses en 2021) ; un réseau des secrétaires de mairie, relais du guichet unique, réuni deux fois par an. Les communes deviennent ainsi parties prenantes des choix, et non simples destinataires d'une offre (« on ne nous demande jamais notre avis »).

**Quatre critères d'arbitrage** (0,5 pt avec la règle) :
1. **Contribution aux objectifs de « Castelrive 2032 »** et du schéma directeur (le guichet unique avant une application demandée par un seul service).
2. **Valeur pour les usagers et les agents** : nombre de personnes concernées, gain de délai ou de qualité (par exemple 20 % des demandes des usagers portent sur un emménagement ou un départ).
3. **Obligation et risque** : continuité et sécurité d'un service public, obligation réglementaire, fin de support d'un logiciel.
4. **Coût global et effort**, y compris l'empreinte environnementale de la solution, au regard de la capacité disponible.

**Règles associées** : toute demande passe par un **circuit unique** (fiche de demande portée par un responsable métier, enregistrée dans la file commune), y compris pour la ville, malgré la proximité des bureaux ; **une part de la capacité est réservée à chaque collectivité**, dans une proportion fixée par le comité stratégique (sans recalculer ici la clé de répartition), avec une part pour les projets communs aux deux collectivités et une part pour les demandes des 18 communes membres, pour que la proximité ou l'insistance ne décident plus de l'ordre de traitement ; les petites demandes sous le seuil restent traitées par la direction du numérique, qui en rend compte. Le délai de traitement des demandes par collectivité, aujourd'hui de 3 et 7 mois, est suivi par le comité stratégique.

**Réponses tolérées**
- Grille de lecture fondée sur les niveaux de capacité de COBIT 2019 (0 à 5) ou sur MAGNum 2026, si elle est appliquée aux notes de l'annexe.
- Autres domaines prioritaires (compétences, au regard des départs de l'annexe 1.4 ; données, au regard de l'objectif de pilotage par les données) s'ils sont justifiés par le projet de territoire et par les faits.
- Autres instances (conférence des maires sur le numérique, comité de suivi de la convention), si la composition, la fréquence et les décisions sont précisées et si les élus des deux collectivités y siègent.
- Critère d'équité entre collectivités présenté comme un cinquième critère plutôt que comme une règle.
- Référence à ISO/IEC 38500:2024 (évaluer, diriger, surveiller ; principe de responsabilité) pour définir la gouvernance.

**Erreurs fréquentes**
- *Note recopiée sans la confronter aux faits* (`JUR-T03` analyser et argumenter, ne pas décrire) — « la maturité est de 3 sur 5 » ; juste : les notes de gouvernance et de services aux usagers sont démenties par les annexes.
- *CMMI présenté comme une certification obligatoire, ou COBIT confondu avec une norme* (`ET-01` ; `JUR-S06` confondre référentiels, normes et solutions) — juste : modèles et référentiels d'évaluation, adaptables.
- *Gouvernance confondue avec l'organisation interne de la direction du numérique* (`JUR-G06` vocabulaire précis de la gouvernance) — organigramme de la direction au lieu d'instances communes aux deux collectivités.
- *Analyse juridique de la convention ou calcul de la clé de répartition* (`JUR-T07` répondre à la seule question posée) — hors du sujet et hors du programme.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| CMMI (CMMI Institute, ISACA) | cinq niveaux de maturité | `cmmi_v3` ; F01 § 5 ; F09 § 5 | en vigueur |
| COBIT 2019 (ISACA) | niveaux de capacité de 0 à 5 ; distinction gouvernance / management | `cobit_2019` ; F02 § 2 et § 3 | en vigueur |
| MAGNum 2026 (Cigref, IFACI, ISACA France) | maturité de la gouvernance du numérique (réponse tolérée) | `magnum_2026` ; F01 § 5 | en vigueur |
| ISO/IEC 38500:2024 | évaluer, diriger, surveiller (réponse tolérée) | `iso_38500_2024` ; F02 § 4 | en vigueur |
| Comitologie du SI | comité stratégique, comité d'arbitrage du portefeuille | F02 § 6 | notion de cours |

---

### 1.3 – Les demandes des usagers et le guichet unique (3 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des SI : `1.3.f` « Analyse des processus métiers et rôle des architectures SI dans leur rationalisation » ; `1.3.a` « Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) ». Limite : « Ne pas réduire l'urbanisation à une vision strictement technique : elle s'inscrit dans une stratégie globale. »

**Annexes mobilisées** : annexes 1.3 (canaux, demandes, logiciels, constats, délais, guichet unique) et 1.1 (logiciels de facturation, de contrôle d'accès et de billetterie ; communes ; direction du numérique mutualisée).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Premier dysfonctionnement, appuyé sur les faits chiffrés, avec ses effets pour les usagers et pour les services | 0,5 |
| a-2 | Deuxième dysfonctionnement, avec ses effets | 0,5 |
| a-3 | Troisième dysfonctionnement, avec ses effets | 0,5 |
| b-1 | Urbanisation définie (découpage en zones, quartiers, îlots faiblement couplés, couches métier à technique, règles : donnée de référence à propriétaire unique, échanges par une zone d'échange) et rattachée à la stratégie (guichet unique de « Castelrive 2032 ») | 0,5 |
| b-2 | Processus cible de la demande à la réponse : point d'entrée unique quel que soit le canal, identification une seule fois, numéro de suivi, routage, traitement sans ressaisie, information de l'usager et de la mairie, clôture et mesure | 0,5 |
| b-3 | Architecture cible en principe : portail, gestion de la relation usager, référentiel commun des usagers, échanges avec les logiciels métiers et les mairies ; apports et une condition | 0,5 |

**Réponse attendue**

*1.3 a) – Les dysfonctionnements du processus actuel*

Les quelque 120 000 demandes reçues en 2026 suivent toutes le même circuit : le traitement d'une demande enchaîne la réception par l'un des cinq canaux, une ressaisie dans le logiciel concerné, le traitement par le service et une réponse, sans suivi d'ensemble. Trois dysfonctionnements (0,5 pt chacun ; trois parmi les suivants) :

| Dysfonctionnement | Faits de l'annexe 1.3 | Effets pour les usagers | Effets pour les services |
|---|---|---|---|
| **Ressaisies entre logiciels cloisonnés** | formulaires du site ressaisis à la main ; pour un emménagement, la même information saisie trois fois ; trois logiciels non reliés | délais (3 semaines pour un emménagement ou un départ), erreurs ; factures contestées : une contestation sur trois vient d'un emménagement enregistré trop tard | charge sans valeur ajoutée, risque d'incohérence entre facturation et badges, contestations à traiter (6 semaines) |
| **Aucun suivi des demandes** | aucun numéro de suivi ; 35 % des demandes relancées, le plus souvent par téléphone | l'usager ne sait pas où en est sa demande et doit rappeler | le téléphone (40 % des demandes) est encombré par les relances ; aucune mesure des délais par demande, objectif de 5 jours pour un bac non tenu (15 jours) sans que la cause soit connue |
| **Rupture avec les mairies** | demandes transmises par courriel sans modèle ; 30 % incomplètes ; la secrétaire de mairie « ne sait pas ce qu'elles deviennent » (annexe 1.2) | les habitants des communes rurales, qui passent par la mairie, sont moins bien servis | rappels, doubles saisies, mairies réduites au rôle de boîte aux lettres |
| **Démarches séparées entre la ville et l'agglomération** | formulaires des deux sites gérés séparément | un habitant de Castelrive qui déménage fait plusieurs démarches | doublons entre deux collectivités qui partagent pourtant la même direction du numérique |

Conclusion : le processus est organisé par logiciel et par canal, non autour de l'usager ; c'est l'architecture actuelle (logiciels métiers isolés, aucun outil commun de suivi) qui produit les ressaisies et l'opacité.

*1.3 b) – Le processus cible du guichet unique et l'architecture urbanisée*

L'**urbanisation du système d'information** consiste à organiser le SI, par analogie avec l'urbanisme d'une ville, en **zones**, **quartiers** et **îlots** faiblement couplés et reliés par des échanges maîtrisés, en mettant en correspondance les couches métier, fonctionnelle, applicative et technique, afin que le SI évolue avec la stratégie sans tout reconstruire. Ses règles : une donnée de référence a un seul propriétaire ; une fonction n'est implantée qu'une fois ; les échanges passent par une **zone d'échange** plutôt que par des liens ou des ressaisies au cas par cas. Ce n'est pas un inventaire technique : ici, elle sert l'objectif du guichet unique (0,5 pt).

**Processus cible** (0,5 pt) :
1. **Dépôt** de la demande par n'importe quel canal, dans un point d'entrée unique : l'usager en ligne ; l'agent d'accueil du siège ou la personne qui répond au téléphone ; la **secrétaire de mairie**, qui saisit elle-même la demande dans le même outil au lieu d'écrire un courriel. Les formulaires guidés imposent les informations utiles (bac identifié, adresse), ce qui supprime les demandes incomplètes.
2. **Identification** de l'usager (foyer ou professionnel) dans le référentiel commun : ses données sont préremplies, il ne les donne qu'une fois.
3. **Enregistrement** avec un **numéro de suivi** et un accusé de réception indiquant le délai prévu.
4. **Routage** automatique vers le service compétent selon le type de demande.
5. **Traitement** dans le logiciel métier, alimenté sans ressaisie ; un emménagement déclaré une fois met à jour la facturation et les droits d'accès aux déchèteries.
6. **Information** de l'usager, et de la mairie si elle a déposé la demande, à chaque changement d'état ; réponse et **clôture** ; mesure du délai et de la satisfaction.

**Architecture urbanisée, en principe** (0,5 pt) :

| Zone | Composant | Rôle |
|---|---|---|
| Zone des canaux et de la relation aux usagers | **portail des démarches** (site et téléphone mobile), commun à la ville et à l'agglomération ; postes d'accueil du siège et des mairies | point d'entrée unique ; formulaires guidés ; espace de suivi de l'usager ; accès des mairies par un profil dédié |
| | **outil de gestion de la relation avec les usagers** | dossier de chaque demande (numéro, état, historique des contacts), routage vers les services, alertes de délai, mesures |
| Zone des référentiels | **référentiel commun des usagers** (foyers et professionnels, coordonnées), avec un propriétaire désigné (le service de la relation aux usagers) | donnée de référence saisie une fois, partagée par tous les logiciels |
| Zone des métiers (un îlot par fonction) | logiciel de facturation de la redevance, logiciel de contrôle d'accès des déchèteries, logiciel de billetterie des piscines ; démarches de la ville raccordées ensuite | traitement de la demande par le service compétent, sans ressaisie |
| Zone d'échange | interfaces de programmation (API) ou bus d'échange entre l'outil de relation, le référentiel et les logiciels métiers | transmet la demande au logiciel métier et renvoie son état ; remplace les courriels et les ressaisies |

Apports : une seule saisie, un suivi de bout en bout, des mairies intégrées au service, des délais mesurables ; la mutualisation devient un atout, puisque le portail et le référentiel peuvent servir les deux collectivités. Condition : un **porteur métier** du guichet unique désigné par les élus (l'absence de porteur a fait échouer le portail de 2024), un propriétaire pour chaque donnée de référence, le DPO associé pour limiter les données collectées aux besoins de chaque démarche, et un accueil maintenu pour les usagers qui ne passent pas par internet.

**Réponses tolérées**
- Processus cible représenté sous forme de diagramme en couloirs (usager, mairie, relation aux usagers, service métier), en format libre lisible ou inspiré de BPMN 2.0.2.
- Architecture présentée en couches (accès, applications, données, échanges) plutôt qu'en zones, si les quatre composants demandés et les échanges sont présents.
- Mention d'un connecteur avec l'outil de démarches de la ville ou d'une identification de l'usager par un compte unique, si elle reste de principe.
- Dysfonctionnement « délais non tenus » (15 jours au lieu de 5 pour un bac, 6 semaines pour une contestation), s'il est relié à sa cause.

**Erreurs fréquentes**
- *Urbanisation réduite à une vision technique* (`ET-20` ; `JUR-G07` urbanisation : le pourquoi puis le comment) — liste de serveurs ou de logiciels ; juste : découpage fonctionnel au service du processus et de la stratégie.
- *Interopérabilité seulement technique* (`ET-36`) — « il suffit de relier les logiciels » ; juste : référentiel commun, propriétaires des données, circuit des mairies.
- *Processus cible qui reproduit l'existant en ligne* (`JUR-T03` analyser et argumenter) — un formulaire de plus sans suivi ni routage.
- *Choix d'un logiciel ou schéma technique détaillé* (`JUR-T07` répondre à la seule question posée) — non demandé.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Urbanisation du SI | zones, quartiers, îlots ; couches ; règles d'urbanisme ; zone d'échange | F03 § 1 et § 3 ; `erreurs_types.md` ET-20 et ET-36 | notion de cours |
| BPMN 2.0.2 (OMG) | diagramme en couloirs (réponse tolérée) | `bpmn_2_0_2` ; F03 § 2 | en vigueur |

---

### 1.4 – La transmission des savoirs des agents qui partent (3,5 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du SI : `1.6.a` « Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle » ; `1.6.d` « Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums » ; `1.6.e` « Leviers d'appropriation et de transformation des pratiques professionnelles ». Limites : « La gestion des connaissances dépasse la seule numérisation de l'information. » « Le pilotage nécessite une approche systémique : outils, processus, culture. » « Le lien avec la gestion des compétences (RH) est complémentaire mais distinct. »

**Annexes mobilisées** : annexes 1.4 (départs, règle de remplacement, six savoirs critiques, outils de terrain, GED et intranet, conditions de travail, témoignages) et 1.1 (600 agents de terrain sans poste, ordinateurs embarqués des camions, télégestion, contrôle d'accès des déchèteries).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Savoirs tacites et explicites distingués et illustrés par le cas ; deux critères de classement explicites (gravité de l'effet de la perte ; urgence, qui combine l'échéance du départ, l'absence de successeur et le faible degré de formalisation) ; classement des six savoirs cohérent avec ces critères | 0,5 |
| a-2 | Trois savoirs prioritaires, chacun avec une forme de transmission adaptée, la personne qui la conduit et une échéance antérieure au départ | 0,5 |
| b-1 | Intégration de chacun des trois savoirs à l'outil de terrain concerné (ordinateur embarqué, téléphone d'astreinte, écran du contrôle d'accès ou code sur l'installation) ; GED comme référentiel des versions validées, en arrière-plan ; intranet comme point d'entrée des encadrants | 0,5 |
| b-2 | Gouvernance : sponsor, pilote, référents, détenteurs et successeurs, responsables de service, direction du numérique ; règles de validation, de mise à jour et de retrait ; un indicateur complet (formule, source, fréquence, cible, axe) | 0,5 |
| c-1 | Premier levier, en réponse à une réticence ou à une difficulté citée | 0,5 |
| c-2 | Deuxième levier, en réponse à une autre réticence ou difficulté | 0,5 |
| c-3 | Troisième levier, en réponse à une troisième réticence ou difficulté | 0,5 |

**Réponse attendue**

*1.4 a) – Le classement des savoirs critiques et leur transmission*

Un **savoir tacite** est incorporé dans la personne, acquis par l'expérience et difficile à formaliser : M. SERVOLLE l'a « appris sur le tas » ; la réponse des techniciens d'astreinte aux alarmes n'est écrite nulle part. Un **savoir explicite** est formalisé et transmissible sans son détenteur : les consignes de sécurité de 2018 (S5) ou la note de service de 2019 (S4). Les deux appellent des actions différentes : un savoir tacite se transmet en situation ou s'explicite avec l'aide d'un tiers ; un savoir explicite doit surtout être tenu à jour et mis à la disposition de ceux qui en ont besoin. Comme un poste n'est remplacé qu'après le départ de son titulaire, un savoir tacite non transmis est perdu (0,5 pt avec les critères et le classement).

**Deux critères** : (1) la **gravité de l'effet de la perte** : sécurité des personnes et continuité du service public d'abord, relations avec les usagers, les communes et les entreprises ensuite ; (2) l'**urgence**, qui combine la date du départ, l'absence de successeur désigné et le faible degré de formalisation.

| Repère | Gravité | Urgence | Rang |
|---|---|---|---|
| S3 Alarmes de la télégestion | forte (continuité : bassins fermés) | forte : premier départ en 2028, rien d'écrit, aucun successeur | 1 |
| S1 Points de vigilance des tournées | forte (sécurité des équipes et des riverains) | forte : juin 2028, rien d'écrit, aucun successeur | 2 |
| S2 Traitement de l'eau | très forte (sécurité sanitaire) | moyenne : mars 2029, successeur désigné, carnet personnel | 3 |
| S6 Contacts du secteur rural | moyenne (relations) | forte : décembre 2027, mais successeur désigné | 4 : passation simple et rapide |
| S4 Apports des professionnels | moyenne (litiges) | moyenne : départs étalés, note de 2019 | 5 |
| S5 Consignes de sécurité | forte | faible pour la transmission : déjà écrites ; il faut les mettre à jour et les rendre accessibles | 6, mise à jour immédiate |

**Formes de transmission des trois savoirs prioritaires** (0,5 pt) :

| Savoir | Forme de transmission | Qui la conduit | Échéance |
|---|---|---|---|
| S3 | entretiens d'explicitation des deux techniciens d'astreinte, conduits par un référent, pour établir une conduite à tenir par type d'alarme ; astreintes en doublon avec le successeur une fois celui-ci désigné | responsable des équipements, avec la DRH qui désigne les successeurs | conduites à tenir validées fin 2027 ; doublon pendant les six mois qui précèdent le premier départ |
| S1 | désignation du successeur, puis tuilage de trois à six mois : tournées faites ensemble, points de vigilance relevés sur place, photographiés et localisés au fil des tournées | responsable de la collecte du secteur nord ; M. SERVOLLE comme tuteur | successeur désigné fin 2027 ; tuilage achevé avant juin 2028 |
| S2 | plannings alignés pour que M. TARNÈDE et le technicien arrivé en 2026 soient de service ensemble chaque semaine ; interventions faites à deux ; carnet transcrit en fiches de réglage par bassin, validées par le responsable des piscines | responsable des piscines | fiches validées et successeur autonome fin 2028, avant mars 2029 |

*1.4 b) – L'intégration aux outils de terrain et la gouvernance du dispositif*

**Intégration aux outils déjà utilisés** (0,5 pt) : le savoir doit apparaître dans l'outil que l'agent a sous les yeux au moment où il en a besoin, et non dans une base à consulter à part.
- **S1** : les points de vigilance s'affichent dans l'**ordinateur embarqué**, sur l'itinéraire de la tournée, à l'approche du lieu concerné ; l'équipage peut signaler un nouveau point, que le chef d'équipe valide.
- **S3** : chaque alarme reçue sur le **téléphone d'astreinte** renvoie à sa conduite à tenir.
- **S2** : la fiche de réglage du bassin s'ouvre depuis le local technique, par un code à scanner sur l'installation, ou depuis le téléphone de service.
- Pour les autres savoirs : à la lecture d'un badge de professionnel, l'**écran du contrôle d'accès** affiche ses droits et la consigne utile (S4) ; les consignes de sécurité mises à jour (S5) sont affichées dans les locaux par un code à scanner.
- **GED** : elle devient le **référentiel en arrière-plan** des versions validées (propriétaire, date de revue, versions antérieures archivées) ; les outils de terrain affichent toujours la version en vigueur. L'**intranet** reste le point d'entrée des encadrants et des référents, qui y consultent l'ensemble des contenus et leur état de mise à jour. La direction du numérique organise, en principe, les liens entre la GED et les outils de terrain, sans nouvel outil pour les agents.

**Gouvernance du dispositif** (0,5 pt avec l'indicateur) :
- **Rôles** : sponsor, la directrice générale des services, avec le (la) DGA ressources qui porte le dispositif ; pilote, la directrice des ressources humaines, qui tient la cartographie des savoirs et décide des désignations anticipées ; la direction du numérique pour les liens avec les outils de terrain ; un **référent** par métier, qui conduit les entretiens et valide les contenus ; les **détenteurs**, reconnus comme tuteurs, et leurs **successeurs** ; les responsables de service, qui libèrent le temps et vérifient l'application ; la prévention valide les consignes de sécurité.
- **Règles** : chaque contenu a un propriétaire et une date de revue ; il est revu après tout changement de tournée, d'installation ou de paramétrage d'alarme, et au moins une fois par an ; il est validé par le référent avant d'être publié ; les versions périmées sont retirées des outils de terrain et les classeurs papier repris puis retirés ; les vidéos et les enregistrements ne servent qu'à la formation. Le dispositif est complémentaire de la gestion des compétences par les ressources humaines, sans se confondre avec elle.
- **Indicateur** :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des postes clés en tuilage avant le départ | nombre de postes clés dont le titulaire part dans les douze mois et dont le successeur travaille avec lui depuis au moins trois mois / nombre de postes clés dont le titulaire part dans les douze mois | tableau des départs de la DRH et plannings des services | trimestrielle, présentée au comité de direction | 100 % pour les postes qui détiennent les savoirs classés prioritaires ; au moins 80 % pour l'ensemble des postes clés | apprentissage |

*1.4 c) – Trois leviers d'appropriation*

(0,5 pt par levier relié à une réticence ou à une difficulté ; trois parmi les suivants)
1. **La crainte que les contenus servent à juger le travail** (M. SERVOLLE) : une **règle d'usage écrite et annoncée** limite les vidéos, les photos et les relevés à la formation, sans aucune évaluation individuelle ; l'agent relit et valide ce qui est publié et en est cité comme auteur ; son rôle de tuteur est reconnu. Le savoir « appris sur le tas » est valorisé au lieu d'être contrôlé.
2. **« Encore un outil ? »** (Mme PELLOUAN) : **aucun outil nouveau** ; l'information est poussée dans les écrans déjà utilisés (écran des badges, téléphone de service, ordinateur embarqué), au moment où elle sert, en contenus courts. C'est la réponse à « si l'information n'est pas sous mes yeux, je ne la chercherai pas ».
3. **L'impossibilité de libérer du temps** (responsable de la collecte du secteur nord) : la transmission est faite **pendant le travail réel** (tournées en binôme plutôt que séances au siège), réservée aux savoirs prioritaires ; pour ces postes, un successeur est affecté en doublure quelques mois avant le départ, ce qui relève d'une décision de la direction générale et des ressources humaines, et non du seul chef d'équipe.
4. **Un successeur qui arrive après le départ et n'est jamais de service avec le détenteur** (technicien arrivé en 2026) : la **règle de remplacement change** pour les postes clés : désignation anticipée et plannings alignés, suivis par l'indicateur de tuilage.

**Réponses tolérées**
- Autres critères de classement (rareté du savoir, degré de formalisation pris comme critère distinct, nombre d'agents ou d'usagers concernés), et autre ordre des savoirs prioritaires (par exemple S2 en premier pour la gravité, ou S6 parmi les trois premiers pour l'échéance de décembre 2027), si le classement découle des critères énoncés.
- Formes de transmission présentées selon le modèle SECI de Nonaka et Takeuchi (1995) : socialisation (tuilage, astreintes en doublon), externalisation (entretiens, conduites à tenir, fiches de réglage), combinaison (GED), internalisation (pratique accompagnée), si elles sont appliquées aux savoirs du cas.
- Leviers présentés à l'aide du modèle ADKAR de Prosci (Hiatt), ou bien des huit étapes de la conduite du changement de Kotter (1995-1996), s'ils répondent aux réticences et aux difficultés citées.
- Autre indicateur complet, par exemple la part des savoirs critiques consultables depuis l'outil de terrain concerné, s'il porte ses cinq champs.

**Erreurs fréquentes**
- *Gestion des connaissances réduite à la GED ou à la numérisation* (`ET-21`) — « mettre les classeurs dans la GED » ; juste : transmission en situation, savoirs intégrés aux outils de terrain, gouvernance et culture.
- *Classement sans critères explicites* (`JUR-T03` analyser et argumenter, ne pas décrire) — savoirs repris dans l'ordre de l'annexe ; juste : deux critères énoncés, puis appliqués à chaque savoir.
- *Base de connaissances à consulter à part, conçue pour des agents de bureau* (`JUR-T01` contextualiser chaque notion) — intranet consultable au siège, formation en salle ; juste : agents sans poste, horaires décalés, outils de terrain existants.
- *Leviers génériques, sans lien avec les réticences* (`JUR-P04` conduite du changement adaptée) — « communiquer et former » ; juste : un levier par réticence ou difficulté citée.
- *Confusion avec la gestion des compétences* (limite du programme 1.6) — plan de recrutement ou de formation traité comme objet du dossier ; juste : lien complémentaire mais distinct.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Savoirs tacites et explicites ; dispositif de gestion des connaissances ; GED et intranet | cartographie des savoirs critiques, rôles, règles, appropriation | F06 § 1 à § 3 ; `erreurs_types.md` ET-21 | notion de cours |
| Nonaka et Takeuchi, *The Knowledge-Creating Company*, 1995 (modèle SECI) | quatre modes de conversion (réponse tolérée) | `nonaka_takeuchi_seci` ; F06 § 1 | publié |
| ADKAR (Prosci) | leviers d'appropriation (réponse tolérée) | `adkar` ; F05 | publié |
| Huit étapes de Kotter (1995-1996) | conduite du changement (réponse tolérée) | `kotter_8_etapes` ; F05 | publié |

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DE LA REDEVANCE INCITATIVE (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le modèle des données de la redevance | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) | 2,5 |
| 2.2 L'architecture des données et le référentiel des adresses et des logements | `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) ; `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) | 2 |
| 2.3 L'effet de la redevance incitative | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 4 |
| 2.4 L'ouverture et la valorisation des données | `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `2.3.e` Aspects réglementaires (RGPD, archivage légal) et monétisation des données | 2,5 |
| 2.5 Le coût du dispositif numérique de la redevance et son pilotage | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) | 2 |
| **Dossier 2 – Organiser et exploiter les données de la redevance incitative** |  | **13** |

Répartition indicative : connaissances (modèles conceptuel et logique et règles de passage, entrepôt et lac de données, données de référence, chaîne de traitement, analyses descriptive et exploratoire, anonymisation et pseudonymisation, rôle du délégué à la protection des données, cycle de vie, coût complet) environ 3,5 points (la moitié des items 2.1 b-1, 2.1 b-3, 2.2 a-1, 2.2 b-1, 2.3 a-1, 2.3 b-1, 2.4 a-1, 2.4 c-1, 2.4 c-2 et 2.5 a-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 9,5 points, soit environ 73 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le modèle des données de la redevance (2,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) ». Modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites ; modèle physique seulement nommé ; aucune requête.

**Annexes mobilisées** : annexe 2.1 (règles de gestion, extrait du modèle logique actuel, précisions de la responsable de la facturation, anomalies de 2026).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux défauts du modèle actuel, chacun rapporté à une règle de gestion et relié à une anomalie chiffrée de l'annexe 2.1 C | 0,5 |
| a-2 | Troisième défaut, rapporté à une règle et à une anomalie ; conclusion : les anomalies viennent de la structure des données, pas seulement des saisies | 0,5 |
| b-1 | Modèle conceptuel et modèle logique distingués ; six entités avec identifiant et attributs élémentaires (logement, foyer, bac, tournée, levée, facture) | 0,5 |
| b-2 | Cinq associations et leurs cardinalités, justifiées par les règles : occupation n:m porteuse des dates d'arrivée et de départ, bac affecté au logement, levée rattachée à un bac et à une tournée, facture adressée à un foyer | 0,5 |
| b-3 | Modèle logique de sept tables déduit par les règles de passage énoncées (clé étrangère côté 1,1 ; table d'association à clé composée pour l'occupation) | 0,5 |

**Réponse attendue**

*2.1 a) – Trois défauts du modèle logique actuel*

Trois défauts parmi les suivants (0,5 pt pour deux défauts, 0,5 pt pour le troisième et la conclusion), chacun rapporté à une règle de gestion et à une anomalie :

1. **Le bac est rattaché au redevable, et non au logement.** Le numéro de puce et le volume du bac sont des colonnes de la table REDEVABLE, alors que la règle RG4 affecte le bac à un logement, où il reste quand le foyer déménage. À chaque emménagement, l'agent écrase l'ancien occupant ou recopie la puce dans une nouvelle fiche : deux fiches portent alors la même puce, et les levées du nouvel occupant peuvent être imputées à l'ancien. Ce défaut explique une partie des **2 000 doublons** et des **1 700 factures** adressées à un foyer parti. Il manque en outre au bac un identifiant propre : la puce sert d'identifiant de fait, si bien qu'une puce remplacée rend ses levées orphelines (RG4 : la puce peut changer sans que le bac change).
2. **L'historique des occupants est perdu.** Le modèle ne connaît ni le logement (RG1) ni l'occupation datée (RG3) : une seule date d'arrivée, aucune date de départ, et une fiche écrasée à chaque changement d'occupant. On ne peut donc pas savoir quel foyer occupait un logement à une date passée (annexe 2.1 C), ni attribuer à coup sûr une levée au foyer présent ce jour-là : d'où les factures adressées à d'anciens occupants et les contestations impossibles à trancher.
3. **L'adresse est saisie en texte libre.** RG1 situe le logement à une adresse désignée par son code dans le référentiel des adresses, alors que le logiciel stocke une chaîne libre (« 12 r. des Lilas », « Les Lilas, 12 »). Le même logement apparaît sous plusieurs formes : c'est la cause la plus fréquente des **2 000 doublons**, et elle rend impossible tout rapprochement avec les fichiers des communes. Le défaut pèse surtout dans la ville-centre, où les compléments d'adresse (bâtiment, porte) sont nombreux, et qui concentre les trois quarts des levées non rattachées.
4. **Les levées n'ont ni heure, ni tournée, ni lien contrôlé avec un bac.** La table LEVEE ne garde que la puce et la date, alors que RG5 et RG6 rattachent chaque levée à une tournée, effectuée par un camion, à une date et à une heure. De plus, le numéro de puce n'y est pas une clé étrangère : rien ne garantit qu'il désigne un bac connu. D'où les **40 000 levées non rattachées** (une sur cinquante), rapprochées à la main par deux agents, et l'impossibilité de « prouver une levée » lors d'une contestation.

**Conclusion** : les anomalies de 2026 ne sont pas d'abord des erreurs de saisie ; elles viennent de la **structure des données**, qui ne traduit pas les règles de gestion. Les corriger à la main chaque semaine ne les fera pas disparaître : il faut corriger le modèle.

*2.1 b) – Le modèle conceptuel et le modèle logique des données de la redevance*

**Les deux modèles** : le **modèle conceptuel des données** représente les objets de gestion (entités), leurs propriétés et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique ; il ne comporte aucune clé étrangère. Le **modèle logique** le traduit en tables, avec leurs clés primaires et leurs clés étrangères, selon des règles de passage, indépendamment du logiciel de gestion de base de données ; le modèle physique, propre à ce logiciel (types, index), n'est pas demandé (F07 § 1 et 2).

**Les entités** (0,5 pt avec la distinction ; identifiant souligné dans la copie, ici en premier) :
- **Logement** (num_logement, code_adresse, complement_adresse, type_logement) ;
- **Foyer** (num_foyer, nom_titulaire, telephone, courriel) ;
- **Bac** (num_bac, num_puce, volume_litres, date_mise_service) : l'identifiant est le numéro gravé sur la cuve, et non la puce, qui peut être remplacée (RG4) ;
- **Tournee** (num_tournee, date_tournee, secteur, immatriculation_camion) : le camion est un attribut de la tournée, aucune règle ne lui donnant d'autres propriétés (RG5) ;
- **Levee** (num_levee, date_levee, heure_levee) ;
- **Facture** (num_facture, semestre, date_emission, montant).

Le code de l'adresse est un attribut du logement, qui renvoie au référentiel des adresses (question 2.2 b) ; le montant est enregistré tel qu'il a été facturé, son calcul n'étant pas modélisé (RG8).

**Les associations et leurs cardinalités** (0,5 pt) :

| Association | Entités et cardinalités | Règle de gestion |
|---|---|---|
| *occuper* (date_arrivee, date_depart) | Foyer (1,n) — Logement (0,n) | RG3 : un logement est occupé successivement par zéro, un ou plusieurs foyers (il peut être vacant) ; un foyer occupe ou a occupé au moins un logement, parfois plusieurs ; les dates dépendent du couple foyer-logement : ce sont des attributs de l'association |
| *etre_affecte* | Bac (1,1) — Logement (0,n) | RG4 : un bac est affecté à un seul logement ; un logement dispose d'aucun, d'un ou de plusieurs bacs |
| *concerner* | Levee (1,1) — Bac (0,n) | RG6 : une levée concerne un seul bac ; un bac peut n'avoir fait l'objet d'aucune levée |
| *etre_lue_lors_de* | Levee (1,1) — Tournee (1,n) | RG6 : une levée est lue lors d'une seule tournée ; une tournée comporte au moins une levée |
| *etre_adressee* | Facture (1,1) — Foyer (0,n) | RG7 : une facture est adressée à un seul foyer ; un foyer qui vient d'arriver peut n'en avoir reçu aucune |

Le foyer n'est pas relié directement au bac ni à la levée : on retrouve le foyer facturé pour une levée en passant par le bac, le logement et l'occupation en cours à la date de la levée. C'est ce qui permet de facturer le bon occupant après un déménagement.

**Le modèle logique** (0,5 pt), obtenu par les règles de passage :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire ;
2. pour une association dont l'une des pattes a pour cardinalité maximale 1 (*etre_affecte*, *concerner*, *etre_lue_lors_de*, *etre_adressee*), la clé primaire de l'entité du côté « n » migre comme clé étrangère dans la table de l'entité du côté 1,1 (obligatoire, puisque la cardinalité minimale est 1) ;
3. l'association *occuper*, dont les deux cardinalités maximales sont n, devient une table dont la clé primaire est composée des clés des deux entités, chacune clé étrangère, et qui porte les attributs de l'association.

- Logement (<u>num_logement</u>, code_adresse, complement_adresse, type_logement)
- Foyer (<u>num_foyer</u>, nom_titulaire, telephone, courriel)
- Occupation (<u>#num_foyer, #num_logement</u>, date_arrivee, date_depart)
- Bac (<u>num_bac</u>, num_puce, volume_litres, date_mise_service, #num_logement)
- Tournee (<u>num_tournee</u>, date_tournee, secteur, immatriculation_camion)
- Levee (<u>num_levee</u>, date_levee, heure_levee, #num_bac, #num_tournee)
- Facture (<u>num_facture</u>, semestre, date_emission, montant, #num_foyer)

Le numéro de bac devient une clé étrangère de la table des levées : une levée ne peut plus être enregistrée sans un bac connu. Une levée lue avec une puce inconnue est alors rejetée dans un journal et traitée à la source (puce remplacée à enregistrer), au lieu d'être « mise de côté ». Le numéro de puce, attribut du bac, doit être unique : c'est une contrainte du modèle physique.

**Réponses tolérées**
- Formalisme différent (notation « pattes de corbeau », schéma relationnel dessiné), s'il est lisible et cohérent (`JUR-T10`).
- Entité Camion distincte de la tournée, ou entité Adresse distincte du logement, si le modèle reste dans la limite de six entités ou si le candidat justifie la septième ; entité Occupation (1,1 vers le foyer et vers le logement) au lieu de l'association porteuse, si le modèle logique obtenu est équivalent.
- Date d'arrivée incluse dans la clé de l'occupation, pour admettre qu'un foyer revienne dans un logement qu'il a déjà occupé, si le candidat l'explique.
- Facture rattachée aussi au logement, ou lignes de facture par levée, si une règle est posée en hypothèse.
- Date et heure de la levée réunies en un seul horodatage.

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dessinées dans le modèle conceptuel, ou modèle logique qui ne découle pas du modèle conceptuel.
- *Bac rattaché au foyer* — le défaut de l'annexe 2.1 B reproduit dans le modèle corrigé : c'est précisément ce qui crée les doublons et les factures adressées aux anciens occupants.
- *Puce retenue comme identifiant du bac* — contraire à RG4 : un remplacement de puce rendrait de nouveau les levées orphelines.
- *Table d'occupation oubliée* — association n:m traduite par une clé étrangère simple, qui fait perdre l'historique des occupants ; dates d'arrivée et de départ placées dans la table du foyer.
- *Morceau de cours ou requête hors attente* (`JUR-T01`, `JUR-T07`) — règles de passage récitées sans les appliquer, ou requêtes écrites alors que la question n'en demande pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, modèle logique, modèle physique ; règles de passage ; lecture des cardinalités | définitions et méthode | F07 § 1 à 4 | notion de cours |

---

### 2.2 – L'architecture des données et le référentiel des adresses et des logements (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) ». Entrepôt, lac, architecture « lakehouse » et référentiel de données maîtres : comparaison et choix justifié ; aucune expertise des infrastructures (serveurs, réseaux), aucun choix de produit.
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) », mobilisée pour la gouvernance du lac et les responsabilités du référentiel (propriétaire, intendant).

**Annexes mobilisées** : annexes 1.1 (territoire, 30 communes, système d'information, direction du numérique mutualisée), 2.1 (anomalies d'adresses), 2.2 (données à réunir, deux options, positions), 2.4 D (durées de conservation) et 2.6 (Data Act, DAMA-DMBOK).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Entrepôt et lac de données définis et distingués ; premier critère (volume et variété) appliqué aux deux options | 0,5 |
| a-2 | Deuxième et troisième critères (qualité et historique, usages) appliqués aux deux options | 0,5 |
| a-3 | Recommandation argumentée (option B, lac associé à un entrepôt, en deux étapes) et deux conditions, dont la gouvernance qui évite le « marécage » et le respect des durées de conservation | 0,5 |
| b-1 | Données de référence définies ; référentiel des adresses et des logements justifié par les anomalies et par le rôle des communes ; deux règles de fonctionnement | 0,5 |

**Réponse attendue**

*2.2 a) – Les deux options*

**Définitions** : un **entrepôt de données** est une base orientée sujet, intégrée, historisée et non volatile, structurée pour l'analyse (faits et dimensions) ; ses données sont nettoyées et mises en forme avant leur chargement (schéma défini à l'écriture). Un **lac de données** stocke des données brutes et hétérogènes (structurées, textes, images, mesures de capteurs), dont la structure n'est définie qu'à la lecture, pour l'exploration ; sans gouvernance, il devient un « marécage » de données inutilisables. Les deux se complètent plus qu'ils ne s'opposent ; une architecture **« lakehouse »** les réunit sur une même plateforme (F07 § 1 et 6).

**Comparaison** (0,5 pt pour le premier critère avec les définitions, 0,5 pt pour les deux autres) :

| Critère | Option A : entrepôt de données classique | Option B : lac associé à un entrepôt (ou « lakehouse ») et référentiel |
|---|---|---|
| Volume et variété des données | adapté aux données structurées (2 millions de levées, 300 000 passages, tonnages, factures), dont le volume reste modeste ; mais il écarte la variété : les mesures horaires des 300 capteurs sont réduites à une moyenne journalière, les textes des réclamations et les photographies des dépôts sauvages ne sont pas repris | accueille toutes les formes de données : mesures en continu (environ 2,6 millions par an), textes, photographies géolocalisées, tableurs des communes et du syndicat ; c'est la **variété** plus que le volume qui justifie le lac |
| Qualité et historique | données nettoyées avant chargement, donc indicateurs fiables ; mais la cause des anomalies demeure, les adresses étant toujours rapprochées à la main à partir des fichiers des communes ; seuls les extraits mensuels sont historisés : si une règle change (méthode des refus de tri, tonnages de 2024 reconstitués), on ne peut pas recalculer | conserve les données brutes et leur historique, ce qui permet de recalculer une série après un changement de méthode ; le **référentiel des adresses et des logements** traite la cause des doublons et des levées non rattachées ; en revanche, la qualité n'est pas garantie par l'outil : sans règles, le lac accumule des données non documentées |
| Usages attendus | le rapport trimestriel et les tableaux de bord récurrents (tonnages, levées par commune) | les mêmes tableaux de bord, plus l'**analyse exploratoire** des effets de report (dépôts sauvages, colonnes de verre pleines, réclamations : question 2.3), la publication des données du territoire (question 2.4) et le partage avec les communes |

On retient aussi que l'option A est plus rapide (neuf mois contre quinze) et que la direction du numérique sait la mettre en œuvre, ce qui réduit le risque de projet.

**Recommandation : l'option B, dans sa forme « lac associé à un entrepôt »** (0,5 pt), parce qu'elle seule réunit les données nécessaires aux objectifs de « Castelrive 2032 » (pilotage par les données, ouverture des données du territoire, baisse des ordures ménagères résiduelles mesurée avec ses effets de report) et qu'elle traite, par le référentiel, la cause des anomalies de l'annexe 2.1. Deux conditions, parmi :
- **procéder en deux étapes**, en commençant par le référentiel et l'entrepôt des données de la redevance, qui répondent aux besoins urgents (facturation fiable, rapport aux élus), puis le lac pour les capteurs, les réclamations et les photographies : on limite ainsi le risque lié aux compétences de l'équipe, qui penche pour l'option A ;
- **gouverner le lac dès le départ** : un propriétaire et une description (catalogue, dictionnaire de données) pour chaque source, des droits d'accès, une qualité contrôlée à l'entrée, faute de quoi il devient un marécage (DAMA-DMBOK : architecture des données, métadonnées, qualité, annexe 2.6) ;
- **respecter les durées de conservation** : « conserver toutes les données brutes avec leur historique » ne vaut pas pour les données personnelles ; les levées détaillées doivent être détruites deux ans au plus après l'émission de la facture, seuls des agrégats par commune et par mois étant conservés au-delà (annexe 2.4 D) ;
- **récupérer les données des capteurs** : le fabricant les garde sur sa plateforme et facture l'export de l'historique ; le Data Act donne à l'utilisateur d'un produit connecté un droit d'accès aux données que génère son utilisation (annexe 2.6) : les conditions d'accès, y compris les frais d'export de 15 k€ par an, sont à discuter avec le fabricant au regard de ce droit, sans analyse juridique ici.

*2.2 b) – Le référentiel des adresses et des logements*

**Définition** (0,5 pt avec la justification et les règles) : les **données de référence** (ou données maîtres) sont des données partagées et stables, utilisées par plusieurs processus et plusieurs applications ; elles sont gérées dans un **référentiel unique**, qui fait foi, et que les autres applications consultent au lieu d'en tenir leur propre copie (F07 § 1).

**Justification** : l'adresse et le logement sont utilisés par la facturation, par les déchèteries (accès des foyers et des professionnels), par les tournées de collecte et par les analyses par commune ; ils sont créés par les **communes**, qui connaissent les premières les nouvelles adresses et les nouveaux logements. Or chacune les tient à sa façon, et 6 communes n'ont pas de liste à jour. Un référentiel partagé supprime la cause des 2 000 doublons et d'une grande partie des 40 000 levées non rattachées. Il permet aussi d'attribuer chaque levée au bon logement, donc au bon occupant, et de produire des données par commune comparables d'un service à l'autre.

**Deux règles de fonctionnement**, parmi :
- **une seule source** : une adresse ou un logement n'est créé, modifié ou fermé que dans le référentiel, et jamais dans le logiciel de facturation ou dans celui des déchèteries, qui le consultent ;
- **des responsabilités partagées** : chaque commune est responsable de ses adresses et de ses logements (propriétaire local), l'agglomération les valide et contrôle les doublons (intendant), dans un délai fixé, par exemple dès l'attribution d'une nouvelle adresse ; les communes sans liste à jour sont accompagnées ;
- **un identifiant unique, non signifiant et stable** pour chaque logement, jamais réattribué, avec un format commun de l'adresse (numéro, voie choisie dans une liste, complément : bâtiment, étage, porte) ;
- **un historique** : chaque adresse et chaque logement portent une date de création et, le cas échéant, de fermeture ; les changements sont tracés, et des indicateurs de qualité (doublons, adresses incomplètes) sont suivis.

**Réponses tolérées**
- Option A recommandée, si le candidat la justifie par la simplicité, le délai et les compétences disponibles, l'accompagne du référentiel des adresses et des logements et prévoit d'y ajouter plus tard les données non structurées.
- Option B retenue sous sa forme « lakehouse », si la gouvernance commune et le respect des durées de conservation sont traités.
- Autres critères ou conditions tirés des annexes (délai, compétences, dépendance envers le fabricant des capteurs).
- Référentiel présenté comme une démarche de gestion des données de référence (données maîtres), si le sigle anglais est écrit en toutes lettres (`ET-13`).

**Erreurs fréquentes**
- *Entrepôt et lac confondus* (`ET-24`) — lac présenté comme un « entrepôt moderne », ou entrepôt comme une simple grosse base.
- *Choix technique hors attente* (`JUR-T07`) — serveurs, capacités de stockage, logiciels ou produits du marché détaillés, alors que l'expertise des infrastructures est exclue.
- *Lac sans gouvernance* — « tout garder » sans propriétaires ni description, et sans regard pour les durées de conservation des données personnelles.
- *Référentiel sans les communes* — référentiel tenu par la seule agglomération, alors que les communes créent les adresses : la cause des anomalies demeure.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines architecture des données, données de référence et données maîtres, métadonnées, qualité | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Règlement (UE) 2023/2854 (Data Act), applicable depuis le 12/09/2025 | accès de l'utilisateur aux données des capteurs (annexe 2.6) | `data_act` / F07 § 8.5 | en vigueur |
| Entrepôt, lac de données, architecture « lakehouse », données de référence | définitions et comparaison | F07 § 1 et 6 | notion de cours |

---

### 2.3 – L'effet de la redevance incitative (4 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Aucun calcul statistique ni aucune manipulation d'outil ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexes 1.1 (territoire, redevance, effectif, « Castelrive 2032 » dans la présentation), 2.2 (sources), 2.3 (indicateurs 2024 et 2026, affirmation du vice-président, limites) et, pour la conclusion, 2.1 (levées non rattachées concentrées dans la ville-centre).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Collecte et nettoyage appliqués aux sources et aux limites des annexes (doublons, ruptures de méthode, données de 2024 reconstituées, signalements hétérogènes) | 0,5 |
| a-2 | Structuration (faits, dimensions, définitions communes), analyse et restitution appliquées ; rôles | 0,5 |
| b-1 | Analyses descriptive et exploratoire définies et distinguées, prédictive écartée ; combinaison justifiée par l'annexe 2.3 | 0,5 |
| b-2 | Premier constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-3 | Deuxième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-4 | Troisième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| c-1 | Affirmation appréciée : ordures ménagères résiduelles et déchets confondus, causalité non établie (biais), effets de report, base de l'objectif non fixée ; formulation juste proposée | 0,5 |
| c-2 | Deux représentations adaptées aux élus, chacune justifiée par son message et assortie d'un piège évité | 0,5 |

**Réponse attendue**

*2.3 a) – La chaîne de traitement*

La **chaîne de traitement** transforme des données brutes en informations utiles à la décision ; c'est une démarche, et non un outil (F08 § 1). Pour mesurer l'effet de la redevance :
- **collecte** (0,5 pt avec le nettoyage) : extraction automatique des levées avec leur heure, leur tournée et leur camion (et non plus la seule date gardée par le logiciel de facturation), des passages et des pesées des déchèteries, des mesures des capteurs (à obtenir du fabricant), des tonnages et des refus de tri du syndicat, chaque mois malgré deux mois de retard, des réclamations, des signalements de dépôts sauvages (application de la ville et tableur des mairies) ; on y ajoute les données de contexte qui manquent aujourd'hui : population de chaque commune, résidences secondaires, liste des professionnels passés à un collecteur privé ;
- **nettoyage** : dédoublonnage des foyers et rattachement des levées aux bacs et aux logements à l'aide du référentiel (question 2.2 b) ; repérage des valeurs manquantes et aberrantes ; **signalement des ruptures de série** (méthode des refus de tri changée en 2025, signalements comptés autrement dans la ville-centre depuis l'application) ; marquage des tonnages de 2024 comme **reconstitués** ; journal des rejets et correction à la source ;
- **structuration** (0,5 pt avec l'analyse et la restitution) : chargement dans l'entrepôt de faits (levées, tonnages, passages, signalements, réclamations), à un grain défini (le mois, la commune, le flux), selon des dimensions communes (date, commune et type de commune, flux de déchets, type de logement, foyer ou professionnel) et des **définitions écrites** dans le dictionnaire de données : ce qu'est une ordure ménagère résiduelle collectée, un habitant (avec ou sans les résidences secondaires), un refus de tri ;
- **analyse** : descriptive, puis exploratoire (question b) ;
- **restitution** : tableau de bord trimestriel des élus (question 2.5 b), tableau de bord détaillé de la direction de la collecte, données publiées sur le portail (question 2.4), chaque fois avec les sources, les dates et les limites ; puis **décision** et actions de prévention.

Le chargé d'études conçoit et documente la chaîne ; les directions qui produisent les données en sont propriétaires et valident les définitions ; la direction du numérique en assure l'exploitation ; la déléguée à la protection des données est consultée sur les données personnelles.

*2.3 b) – La méthode et trois constats*

**La méthode** (0,5 pt) : l'**analyse descriptive** résume ce qui s'est passé (niveaux, évolutions, répartitions, écarts à un objectif) ; l'**analyse exploratoire** recherche, sans hypothèse arrêtée, des croisements, des profils et des valeurs atypiques qui orientent vers des explications ; l'**analyse prédictive** estime ce qui va se passer (F08 § 2). On retient :
- l'**analyse descriptive d'abord**, parce que les élus demandent ce qui a changé entre 2024 et 2026, et parce qu'il faut établir des chiffres fiables avant de les expliquer ;
- puis l'**analyse exploratoire**, pour chercher où sont allés les déchets et pourquoi les résultats diffèrent selon les communes : croiser la baisse des ordures ménagères résiduelles avec le tri, les déchèteries, les refus de tri et les dépôts sauvages ; rapprocher les contestations de factures de la qualité des données ;
- une analyse **prédictive** (l'atteinte de l'objectif de 2030) serait prématurée : deux années seulement, une base de 2024 reconstituée, des séries rompues en 2025.

**Trois constats** parmi les suivants (0,5 pt chacun : le fait chiffré, son interprétation au regard de « Castelrive 2032 », la précaution de lecture) :

1. **Les ordures ménagères résiduelles collectées ont nettement baissé, d'autant plus que la commune est petite.** Elles passent d'environ 42 000 à 34 000 tonnes, soit près d'un cinquième de moins ; par habitant, − 10 % dans la ville-centre (250 à 225 kg), − 20 % dans les communes moyennes (240 à 192 kg), − 30 % dans les communes rurales et périurbaines (220 à 154 kg). Les levées suivent la même pente : 24 par foyer et par an dans la ville-centre, 13 dans les communes rurales, à peine plus que le forfait de 12. *Précaution* : la base de 2024 est reconstituée à partir des pesées de camions dont les tournées traversent plusieurs communes, et la répartition par type de commune est donc fragile ; une partie de la baisse de la ville-centre vient du départ d'environ 500 professionnels vers un collecteur privé, dont les déchets ne sont plus comptés.
2. **La quantité totale de déchets par habitant n'a presque pas changé.** En additionnant ordures ménagères résiduelles, emballages et papiers et apports en déchèterie, on passe de 450 à 445 kg par habitant dans la ville-centre, de 505 à 502 kg dans les communes moyennes, de 520 à 524 kg dans les communes rurales. La redevance a donc surtout **déplacé** les déchets vers le tri (+ 10 à + 20 kg) et les déchèteries (+ 10 à + 50 kg) ; elle n'a pas, à ce stade, réduit les déchets produits. *Précaution* : les apports en déchèterie mêlent ceux des professionnels et les végétaux, sensibles à la météo ; les quantités par habitant ignorent les résidences secondaires, nombreuses dans dix communes rurales, qui gonflent les ratios de ces communes.
3. **Des effets de report apparaissent là où la baisse est la plus forte.** Dans les communes rurales, les refus de tri passent de 15 % à 28 % et les signalements de dépôts sauvages sont multipliés par quatre (100 à 400) : des ordures sont mises dans les bacs de tri ou déposées dans la nature pour éviter des levées. *Précaution* : le nouveau prestataire du centre de tri mesure les refus autrement depuis 2025 (rupture de série) ; les signalements ruraux dépendent des appels des mairies, et le triplement dans la ville-centre (300 à 900) tient en partie à l'application lancée en 2025, qui facilite le signalement : une hausse des signalements n'est pas forcément une hausse des dépôts. Une concomitance n'est pas une causalité.
4. **Les contestations de factures sont les plus nombreuses dans la ville-centre**, avec 260 pour 1 000 redevables contre 170 dans les communes rurales. Deux explications sont possibles. D'une part, les foyers y dépassent le plus le forfait (24 levées contre 13, pour un forfait de 12) et paient donc la part variable la plus élevée. D'autre part, la ville-centre concentre les trois quarts des levées non rattachées (annexe 2.1) : les contestations traduisent aussi la **qualité des données**. *Précaution* : on ne peut pas départager ces explications ; il n'existe aucune donnée de 2024, et les réclamations, en texte libre dans un tableur, ne sont pas classées par motif.

*2.3 c) – L'affirmation du vice-président et deux représentations*

**L'affirmation de M. BASTÉROLE** (0,5 pt) : « la redevance a fait baisser nos déchets de 20 % » est à corriger sur quatre points :
- **ce qui a baissé**, ce sont les ordures ménagères résiduelles collectées, d'environ un cinquième (42 000 à 34 000 tonnes), et non « nos déchets » : leur total par habitant est stable (constat 2) ;
- **la cause n'est pas établie** : la redevance est la cause la plus plausible, mais la comparaison ne porte que sur deux années, sans groupe de comparaison, sur une base reconstituée, avec le départ de professionnels et des changements de mesure ; un élu qui porte la réforme est exposé au **biais de confirmation**, qui consiste à retenir le chiffre qui conforte sa conviction ;
- **les effets de report** (tri moins bon, dépôts sauvages, apports en déchèterie) ont un coût : le ramassage des dépôts sauvages occupe l'équivalent de trois agents (annexe 2.5) ;
- **l'objectif de « Castelrive 2032 »** (− 15 % d'ici 2030), adopté en janvier 2027, n'indique pas son année de référence : s'il part de 2026, il reste entièrement à atteindre ; s'il part de 2024, la baisse affichée doit encore être confirmée.

Formulation proposée au conseil : « Depuis la redevance, les ordures ménagères résiduelles collectées ont baissé d'environ un cinquième, surtout dans les communes rurales. Une partie s'est reportée vers le tri, les déchèteries et des dépôts sauvages, et la quantité totale de déchets n'a pas diminué. L'objectif de 2030 doit être mesuré à partir d'une base que nous fixons aujourd'hui. »

**Deux représentations** (0,5 pt), parmi :
- **Barres empilées par type de commune, en 2024 et en 2026**, des kilogrammes par habitant d'ordures ménagères résiduelles, d'emballages et papiers et d'apports en déchèterie. *Message* : la hauteur totale ne change presque pas, seule sa composition change. *Piège évité* : axe partant de zéro, quantités par habitant plutôt qu'en tonnes, pour comparer des communes de tailles différentes.
- **Courbe des ordures ménagères résiduelles collectées** par habitant, avec la **trajectoire de l'objectif** de − 15 % tracée depuis l'année de référence retenue. *Message* : où en est-on de l'objectif, et ce qui reste à faire. *Piège évité* : le point de 2024 est signalé comme reconstitué, et l'année de référence est écrite.
- **Barres groupées des refus de tri et des signalements de dépôts sauvages** par type de commune, en 2024 et en 2026. *Message* : les effets de report sont les plus forts dans les communes rurales. *Piège évité* : une mention de la rupture de méthode de 2025 et du lancement de l'application dans la ville-centre.
- **Carte des communes** colorée selon la baisse des ordures ménagères résiduelles par habitant, ou selon les levées par foyer. *Message* : la géographie de l'effet de la redevance. *Piège évité* : une carte en taux et non en tonnes, qui ferait ressortir la seule ville-centre.

Un chiffre isolé de « − 20 % » en grand caractère, ou un histogramme dont l'axe est tronqué pour accentuer la baisse, sont de mauvais choix.

**Réponses tolérées**
- Chaîne de traitement présentée avec l'extraction, la transformation et le chargement comme étape intermédiaire, si les cinq étapes de la question sont couvertes.
- Analyse diagnostique présentée comme une variante de l'analyse exploratoire.
- Autres constats tirés de l'annexe 2.3 (levées par foyer selon le type de commune, hausse des apports en déchèterie), s'ils sont chiffrés et assortis d'une précaution ; baisse globale lue comme « environ 20 % » ou « 19 % ».
- Constat sur les contestations de factures expliqué par la seule part variable plus élevée dans la ville-centre, ou par la seule qualité des données, si l'explication est argumentée.
- Autres représentations adaptées aux élus (jauge de l'objectif, petits multiples par type de commune), si le message et le piège évité sont précisés.

**Erreurs fréquentes**
- *Corrélation présentée comme une causalité* (`ET-26`) — baisse des ordures ménagères résiduelles imputée à la seule redevance, ou hausse des signalements prise pour une hausse des dépôts.
- *Prudence d'interprétation oubliée* (`JUR-D06`) — base de 2024 reconstituée et ruptures de méthode ignorées, objectif de 2030 jugé atteint sans année de référence.
- *Informatique décisionnelle réduite à un outil* (`ET-05`, `JUR-D02`) — logiciel de tableaux de bord proposé sans la chaîne de traitement ni les définitions communes.
- *Calcul hors attente* (`JUR-T07`) — moyennes pondérées ou tests statistiques, alors que la question demande des constats argumentés en chiffres ronds.
- *Morceau de cours* (`JUR-T01`) — définitions des méthodes d'analyse sans les appliquer aux communes et aux années de l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement, analyses descriptive, exploratoire et prédictive, choix des graphiques, biais de lecture, corrélation et causalité | définitions et méthode | F08 § 1, 2 et 5 | notion de cours |
| Faits, dimensions, grain, dictionnaire de données | structuration | F07 § 1 et 6 | notion de cours |

---

### 2.4 – L'ouverture et la valorisation des données (2,5 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression » ; `2.3.e` « Aspects réglementaires (RGPD, archivage légal) et monétisation des données ». Délégué à la protection des données et registre des traitements, archivage, monétisation analysée de façon critique ; le principe d'ouverture des données publiques est donné par l'énoncé ; ni prérogatives des usagers sur leurs données, ni fondement juridique des traitements, ni pouvoirs de l'autorité de contrôle (UE 1), ni analyse juridique.

**Annexes mobilisées** : annexes 1.1 (collectivités, direction du numérique mutualisée), 2.2 (capteurs, signalements), 2.4 (règle d'ouverture, six jeux de données, proposition de KOMPAVEL, délégué à la protection des données, durées de conservation) et 2.6 (RGPD, anonymisation, monétisation, Data Governance Act).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Anonymisation et pseudonymisation définies et distinguées ; jeux J1, J2 et J6 publiables, avec leurs conditions | 0,5 |
| a-2 | Jeux J3, J4 et J5 appréciés selon les trois critères : J3 non publiable tel quel, J4 publiable avec un seuil, J5 publiable après retrait des éléments identifiants | 0,5 |
| b-1 | Proposition de KOMPAVEL appréciée de façon critique (données personnelles non anonymisables pour cet usage, finalité, monétisation, exclusivité, confiance, prix dérisoire) ; recommandation | 0,5 |
| c-1 | Rôle du DPO mutualisé (missions, désignation commune possible) et deux points à corriger (conflit d'intérêts, rattachement, moyens, consultation, registre) | 0,5 |
| c-2 | Cycle de vie et règles de conservation et d'archivage appliquées aux données de la redevance, écarts aux pratiques actuelles corrigés | 0,5 |

**Réponse attendue**

*2.4 a) – Les six jeux de données*

**Définitions** (0,5 pt avec J1, J2 et J6) : l'**anonymisation** rend impossible, en pratique et de façon irréversible, l'identification des personnes ; les données anonymisées ne sont plus des données personnelles. La **pseudonymisation** remplace les éléments directement identifiants (nom, numéro de foyer) par un pseudonyme : la personne reste identifiable par recoupement, et les données restent personnelles (annexe 2.6 ; F07 § 8.6). Une donnée qui permet d'identifier une personne indirectement, comme l'adresse d'un logement individuel, est une donnée personnelle.

| Jeu | Publication | Conditions et justification |
|---|---|---|
| J1 – tonnages mensuels par commune et par flux | **oui** | données agrégées par commune et par flux, qui ne se rapportent à aucun foyer ; publiées dans un format ouvert, avec une description : tonnages de 2024 reconstitués, rupture de méthode des refus de tri en 2025 |
| J2 – colonnes de verre et taux de remplissage | **oui** | mesures de capteurs sur des équipements publics, sans donnée personnelle ; l'agglomération doit d'abord obtenir les données auprès du fabricant (annexe 2.2) |
| J6 – horaires et fréquentation des déchèteries par tranche horaire | **oui** | décomptes de passages agrégés, sans numéro de badge ni plaque d'immatriculation |
| J3 – levées par bac avec l'adresse, la date et l'heure | **non, tel quel** | l'adresse d'un logement désigne un foyer (individualisation, même sans le nom : un simple pseudonyme du bac n'y change rien) ; on peut la relier à d'autres sources (corrélation) ; les dates et heures révèlent les habitudes et les absences (inférence), ce qui fait aussi courir un risque aux occupants ; seul un agrégat par commune ou par quartier et par mois peut être publié |
| J4 – levées moyennes par foyer, par commune et par semestre | **oui, avec un seuil** | moyenne sur au moins 80 foyers dans la plus petite commune : aucun foyer n'est isolé ; la publication à la rue est exclue (40 rues de moins de cinq logements, où l'on pourrait déduire le comportement d'un foyer) ; un seuil minimal de foyers par case est fixé, et les petites communes sont regroupées si nécessaire |
| J5 – signalements de dépôts sauvages | **oui, après retrait des éléments identifiants** | les photographies montrant des personnes, des plaques ou des courriers nominatifs identifient des personnes ; les commentaires peuvent désigner un auteur supposé, ce qui revient à publier un soupçon (inférence) ; on publie la date, la commune ou le quartier, une position arrondie hors des domiciles et la nature des déchets, sans photographie ni commentaire |

(0,5 pt pour J3, J4 et J5.) Avant publication, la déléguée à la protection des données vérifie les trois critères, et chaque jeu publié est décrit (définition, source, fréquence de mise à jour, limites).

*2.4 b) – La proposition de KOMPAVEL*

**Appréciation critique** (0,5 pt avec la recommandation), en quatre arguments parmi :
- **un fichier de données personnelles qu'on ne peut pas anonymiser pour cet usage** : nom, adresse et nombre de levées par mois décrivent le comportement de chaque foyer ; le ciblage commercial exige précisément d'identifier les foyers (individualisation), si bien que l'anonymisation viderait l'offre de son intérêt ;
- **une autre finalité** : les levées sont collectées pour facturer la redevance ; les céder pour une prospection commerciale par une entreprise est une finalité différente, a priori incompatible avec la finalité initiale (annexe 2.6), et les usagers y verraient une surveillance de leurs poubelles : la **confiance** dans la redevance, déjà contestée, en souffrirait, avec un risque pour l'image de l'agglomération ;
- **la monétisation des données personnelles a des limites** : une personne ne peut ni céder la propriété de ses données ni renoncer à ses garanties (annexe 2.6) ; l'agglomération n'est pas « propriétaire » des données des foyers et ne peut pas les vendre comme une marchandise ;
- **l'exclusivité** demandée pendant trois ans va à l'encontre du principe, posé par le Data Governance Act, selon lequel les accords qui accordent un droit exclusif de réutilisation de données protégées détenues par le secteur public sont en principe interdits ; elle favoriserait aussi une entreprise au détriment des autres, à l'inverse de l'ouverture décidée par le conseil ;
- **un gain dérisoire et une logique fragile** : 30 k€ par an, soit moins de 40 centimes par foyer, au regard du risque pris ; et un foyer qui présente souvent son bac n'est pas forcément celui qui produit le plus de déchets ou qui peut composter (volume du bac, taille du foyer, appartement sans jardin).

**Recommandation** : refuser la vente du fichier, et répondre à l'intérêt réel de la proposition, la prévention, autrement : publier les données agrégées (J1, J4), utilisables par KOMPAVEL comme par toute autre entreprise ; conduire, au besoin, une campagne de compostage portée par l'agglomération elle-même, auprès de tous les foyers ou des communes où les levées sont les plus nombreuses, sans transmettre de fichier nominatif ; consulter la déléguée à la protection des données avant toute nouvelle utilisation des données de la redevance.

*2.4 c) – Le délégué à la protection des données mutualisé, la conservation et l'archivage*

**Le rôle du délégué** (0,5 pt avec deux points à corriger) : la désignation d'un délégué à la protection des données est obligatoire pour l'agglomération comme pour la ville, organismes publics ; un **même délégué** peut être désigné pour les deux, compte tenu de leur structure et de leur taille, ce qui est cohérent avec la direction du numérique mutualisée (annexe 2.6). Le délégué **informe et conseille** les deux collectivités et leurs agents, **contrôle** le respect du règlement (registre, durées de conservation, sous-traitants), conseille les projets dès leur conception et coopère avec l'autorité de contrôle. Il n'est pas responsable du traitement : c'est l'agglomération qui l'est, pour la redevance, et qui tient son registre avec son aide (F15 § 1 et 2).

**Deux points à corriger**, parmi :
- **le conflit d'intérêts** : Mme VILLEROUSSE a été cheffe du projet du logiciel de facturation, dont elle a contribué à fixer les moyens ; elle ne peut pas contrôler en toute indépendance un traitement qu'elle a conduit. Ses missions doivent être séparées de la conduite de projets ;
- **le rattachement** : rattachée au directeur du numérique mutualisé, qui décide des moyens des traitements, elle ne peut pas lui rendre compte de leur conformité ; elle doit rendre compte au plus haut niveau de chacune des deux collectivités (les directions générales) ;
- **les moyens** : un mi-temps pour deux collectivités, dont l'une emploie 1 100 agents et tient 35 fiches de registre, avec des projets de données d'envergure, ne suffit pas ; on peut prévoir des référents dans les directions ;
- **sa consultation** : elle n'a été consultée ni sur les options d'architecture ni sur la proposition de KOMPAVEL, alors que la protection des données doit être prise en compte dès la conception ;
- **le registre** : la fiche de la redevance, de 2023, est à mettre à jour (levées horodatées, hébergement chez l'éditeur, qui agit comme sous-traitant, échanges avec les communes, entrepôt et lac, publication de données, durées de conservation).

**La conservation et l'archivage** (0,5 pt) : le cycle de vie des données comprend leur **création**, leur **stockage**, leur **usage**, leur **archivage** et leur **suppression** ; à chaque catégorie de données sont associées une durée d'utilité courante, une durée de conservation et un sort final (F07 § 8.4). Appliqué à la redevance :
- **les levées détaillées** sont détruites deux ans au plus après l'émission de la facture qu'elles justifient ; au-delà, seules des données agrégées par commune et par mois sont conservées pour l'analyse. Les levées qui justifient les premières factures, émises en 2025, atteignent ce délai dès 2027 : la purge doit être programmée maintenant. Le logiciel de l'éditeur, qui garde tout depuis 2025, doit être purgé, et la règle s'impose aussi au futur lac de données ;
- **les factures** restent deux ans dans le logiciel de facturation, puis passent en **archivage intermédiaire** (accès restreint, intégrité garantie) jusqu'à dix ans après leur émission, avant une destruction tracée ;
- **les fiches des foyers partis** sont détruites deux ans après le départ et le paiement de la dernière facture, une fois les doublons fusionnés ;
- **les tonnages annuels et les rapports aux élus** sont conservés définitivement dans les archives de l'agglomération ;
- **les copies non maîtrisées** sont supprimées : le tableur des réclamations est purgé selon les mêmes durées, et les extractions de levées conservées dans les messageries sont effacées, puis remplacées par un partage sécurisé, limité aux données nécessaires aux communes ;
- **le contrat avec l'éditeur** doit prévoir les purges sur instruction de l'agglomération et la restitution des données à son terme, en 2029.

Le service de la facturation, propriétaire des données, décide de ces règles avec l'archiviste ; la direction du numérique les met en œuvre ; la déléguée à la protection des données en contrôle l'application.

**Réponses tolérées**
- J4 jugé publiable sans seuil, si le candidat montre que la plus petite commune compte encore 80 foyers ; J2 jugé publiable avec un délai ou une moyenne horaire.
- J5 jugé non publiable, si le candidat propose une version agrégée (nombre de signalements par commune et par mois).
- Recommandation d'une convention de prévention avec plusieurs entreprises, sans transmission de données nominatives, après avis du délégué.
- Autres points à corriger tirés de l'annexe 2.4 C, s'ils sont justifiés.
- Cycle de vie présenté en sept étapes (collecte, stockage, traitement, partage, archivage, destruction…), si les durées de l'annexe sont appliquées.

**Erreurs fréquentes**
- *Anonymisation et pseudonymisation confondues* — fichier des levées jugé publiable une fois le nom ou le numéro du bac retirés, alors que l'adresse et les heures suffisent à identifier le foyer.
- *Monétisation présentée sans regard critique* (programme 2.3, limite : « la monétisation doit être abordée de façon critique ») — « 30 k€ de recettes » acceptés sans examiner la finalité, la confiance des usagers et l'exclusivité.
- *Délégué confondu avec le responsable du traitement ou avec le RSSI* (`ET-29`, `JUR-D05`) — délégué présenté comme celui qui « décide » des traitements, ou mutualisation jugée impossible.
- *Analyse juridique hors programme* (`JUR-T07`) — développement sur les prérogatives des usagers sur leurs données, les fondements juridiques des traitements ou les pouvoirs de l'autorité de contrôle, au lieu de l'application des repères fournis.
- *Durées inventées ou discutées* — remise en cause des durées de l'annexe 2.4 D, qui sont données.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | donnée personnelle, finalité, minimisation, conservation, registre, délégué (désignation commune, missions, conflit d'intérêts) | `rgpd` / F15 § 1 et 2 | en vigueur |
| Proposition « omnibus numérique » du 19/11/2025 | projet, non applicable | `omnibus_numerique_donnees` / F15 § 8 | projet |
| Publication de l'autorité de contrôle sur l'anonymisation, 19/05/2020 | trois critères : individualisation, corrélation, inférence ; pseudonymisation | `cnil_anonymisation_2020` / F07 § 8.6 | publiée |
| Publication de l'autorité de contrôle sur la monétisation, 17/11/2025 | limites de la monétisation des données personnelles | `cnil_monetisation_2025` / F07 § 8.6 | publiée |
| Règlement (UE) 2022/868 (Data Governance Act), applicable depuis le 24/09/2023 | réutilisation des données protégées du secteur public, exclusivité en principe interdite | `dga` / F07 | en vigueur |
| Cycle de vie des données, archivage intermédiaire et définitif | règles de conservation appliquées | F07 § 8.4 | notion de cours |

---

### 2.5 – Le coût du dispositif numérique de la redevance et son pilotage (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ». Total de tête en sommes rondes ; aucun calcul actualisé, aucune règle de finances locales.

**Annexes mobilisées** : annexes 1.1 (78 000 foyers et 6 000 professionnels redevables, collecte), 2.1 (rapprochement manuel des levées, factures erronées), 2.2 (export des données des capteurs), 2.3 (dépôts sauvages) et 2.5 (coûts de 2026, contrat avec l'éditeur, rapport trimestriel).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Coût complet défini ; 840 k€ / 84 000 redevables = 10 € par redevable et par an ; poids du temps du service | 0,5 |
| a-2 | Deux coûts cachés tirés des annexes, chacun expliqué | 0,5 |
| b-1 | Indicateur de coût complet, avec ses cinq champs | 0,5 |
| b-2 | Indicateur de risque complet, avec ses cinq champs ; complémentarité avec les tonnages du rapport actuel | 0,5 |

**Réponse attendue**

*2.5 a) – Le coût par redevable et deux coûts cachés*

**Le coût complet** (0,5 pt avec le calcul) : le **coût complet**, ou coût total de possession (TCO), d'un système d'information réunit tous les coûts supportés sur sa durée de vie : acquisition ou abonnement, exploitation et maintenance, matériel, personnel interne, support, formation, et jusqu'à la sortie (restitution des données, migration) ; il comprend des coûts directs, des coûts indirects et des coûts cachés, et ne se réduit pas au prix du logiciel (F09 § 3.1).

**Le calcul, de tête** : 240 + 80 + 40 + 20 + 100 + 360 = **840 k€** par an ; pour 78 000 foyers et 6 000 professionnels, soit **84 000 redevables** : 840 000 € / 84 000 = **10 € par redevable et par an**. Le premier poste est le **temps du service** de la facturation et des réclamations (360 k€, plus de 40 % du total), devant l'abonnement au logiciel (240 k€) : une grande partie du coût est humaine, et elle dépend directement de la qualité des données, puisque les doublons, les levées non rattachées et les factures adressées à d'anciens occupants alimentent les réclamations.

**Deux coûts cachés** (0,5 pt), parmi ceux que la comptabilité analytique ne rattache pas au dispositif :
- **le rapprochement manuel des levées non rattachées** : deux agents de la direction de la collecte y consacrent chacun une journée par semaine, soit une centaine de journées par an, comptées dans la collecte et non dans le dispositif (annexe 2.1) ;
- **la sortie du contrat avec l'éditeur** : le contrat, qui prend fin en 2029, ne prévoit pas la restitution des données ; leur récupération et leur reprise dans un nouveau logiciel auront un coût, qui n'est pas provisionné (réversibilité) ;
- **le traitement des factures erronées** : 1 700 factures adressées à des foyers partis entraînent des annulations, de nouvelles factures et des relances, ainsi qu'une perte de confiance des usagers ;
- **les effets de report de la redevance** : le ramassage des dépôts sauvages mobilise l'équivalent de trois agents des services techniques (annexe 2.5) ; c'est un coût indirect de la politique plutôt que du dispositif numérique, à signaler aux élus ;
- **l'accès aux données des capteurs**, facturé 15 k€ par an par le fabricant pour l'export de l'historique, dès lors que ces données doivent être réunies avec celles de la redevance (annexe 2.2) ; montant à discuter avec le fabricant au regard du droit d'accès du Data Act (annexe 2.6).

*2.5 b) – Deux indicateurs pour compléter le rapport trimestriel*

Le rapport actuel ne mesure que la **performance** (tonnages). Les deux indicateurs proposés y ajoutent le **coût** et le **risque**, pour équilibrer le pilotage, comme le demande Mme VARSANGE (0,5 pt par indicateur complet) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Coût complet du dispositif numérique par redevable** | (coûts annuels du dispositif, y compris les coûts cachés identifiés : rapprochement manuel, traitement des factures erronées) / nombre de redevables actifs | comptabilité analytique (contrôle de gestion) et logiciel de facturation (redevables actifs) | trimestrielle, sur douze mois glissants | au plus 10 € par redevable en 2028, coûts cachés compris (10 € en 2026 sans eux) | financier |
| **Taux de levées non rattachées** | levées non rattachées à un bac affecté à un logement / levées lues × 100 | logiciel de facturation (journal des levées rejetées), puis entrepôt de données | mensuelle, présentée chaque trimestre | au plus 0,5 % fin 2027 (2 % en 2026) | processus |

Le premier suit l'**efficience** du dispositif : il doit baisser à mesure que la qualité des données réduit le temps de correction et de réclamation. Le second mesure le **risque** de facturer à tort, ou de ne pas facturer, et de perdre la confiance des usagers : il vérifie que le modèle corrigé et le référentiel des adresses produisent leur effet. Présentés à côté des tonnages, avec leur tendance et leur cible, ils remplacent une page de chiffres par un tableau de bord qui relie le coût, le risque et le résultat.

**Réponses tolérées**
- Coût par foyer seul (840 k€ / 78 000, un peu moins de 11 €), si l'hypothèse est écrite ; coût calculé hors temps du service (480 k€, soit un peu moins de 6 € par redevable), si le candidat le signale comme partiel.
- Autres coûts cachés tirés des annexes (formation des agents, temps de la déléguée à la protection des données, mise à jour du registre), s'ils sont expliqués.
- À la place de l'indicateur de risque : part des factures adressées à un foyer parti (factures adressées à un foyer parti / factures émises ; logiciel de facturation et référentiel des logements ; semestrielle ; au plus 0,2 % en 2028, environ 1 % en 2026 ; axe client) ; signalements de dépôts sauvages pour 10 000 habitants (signalements / population × 10 000 ; application de la ville et tableur des mairies ; trimestrielle ; en baisse chaque année à partir de 2027 ; axe environnement), qui mesure le risque d'effets de report. Comme indicateur complémentaire de performance seulement : délai de réponse aux réclamations sur les levées (somme des jours entre réception et réponse / réclamations ; tableur puis outil de suivi ; mensuelle ; au plus quinze jours ; axe client).

**Erreurs fréquentes**
- *Coût complet réduit au prix du logiciel* (`ET-33`) — seul l'abonnement de 240 k€ retenu, en oubliant le temps du service, qui pèse davantage.
- *Calcul hors attente* (`JUR-T07`) — actualisation ou retour sur investissement calculés, alors que la question demande un coût par redevable de tête.
- *Indicateur incomplet ou générique* (`ET-18`, `JUR-A02`) — « suivre les coûts » sans formule, source, fréquence, cible ni axe, ou deux indicateurs de tonnages qui doublent le rapport actuel.
- *Finances locales hors attente* — discussion du tarif de la redevance ou de son équilibre budgétaire, que la question n'appelle pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Coût complet (TCO), coûts directs, indirects et cachés, réversibilité | définition et calcul de tête | F09 § 3.1 | notion de cours |
| Indicateur à cinq champs, équilibre performance, risque et coût, axes du tableau de bord prospectif | deux indicateurs du rapport trimestriel | F08 § 3 ; F09 § 4 | notion de cours |

---

## DOSSIER 3 – FIABILISER, SÉCURISER ET RENDRE PLUS SOBRE LE SYSTÈME D'INFORMATION (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 La note de synthèse de l'audit des piscines et ses suites | `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 2,5 |
| 3.2 La fiabilité de la chaîne « levée → facture » | `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels (ici, le système de facturation de la redevance) | 3 |
| 3.3 Les risques et la sécurité des équipements connectés et des systèmes techniques | `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 3,5 |
| 3.4 La stratégie numérique responsable de l'agglomération | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) (ici, la tension entre l'IA et la sobriété, la trajectoire et la grille de maturité numérique durable) ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI | 4 |
| **Dossier 3 – Fiabiliser, sécuriser et rendre plus sobre le système d'information** |  | **13** |

Répartition indicative : connaissances (note de synthèse et rapport d'audit, fiabilisation et familles de contrôles, typologie des risques, architecture de confiance, sobriété numérique, Green IT et IT for green) environ 2,5 points (items 3.1 a-1, 3.2-1, 3.3 a-1, la définition de l'item 3.3 b-1 et l'item 3.4 a-1) ; analyse des annexes et recommandations environ 10,5 points, soit environ 80 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – La note de synthèse de l'audit des piscines et ses suites (2,5 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la conformité financière et comptable n'est pas traitée par l'UE 5.

**Annexes mobilisées** : annexe 3.1 (cadre de la mission, constats, réactions, demande de la directrice générale des services), annexe 3.5 (guide d'hygiène de l'ANSSI, COSO 2013, RGPD) et annexe 1.1 (piscines, système d'information, organigramme, direction du numérique mutualisée portée par la ville).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Note de synthèse distinguée du rapport (destinataire décideur, brève, hiérarchisée, tournée vers la décision ; le rapport est détaillé, exhaustif et documenté) ; appréciation globale nette ; 20 lignes au maximum | 0,5 |
| a-2 | Deux constats de priorité 1, chacun complet : constat chiffré, risque, recommandation, responsable nommé, échéance datée | 0,5 |
| a-3 | Deux autres constats complets ; hiérarchie justifiée (gravité, récurrence, exposition) ; suivi du plan d'action annoncé | 0,5 |
| b-1 | Deux facteurs de succès reliés aux réactions de l'annexe 3.1 ou à la mutualisation | 0,5 |
| b-2 | Deux points de vigilance reliés au cas, dont l'indépendance de l'auditrice rattachée à la ville | 0,5 |

**Réponse attendue**

*3.1 a) – La note de synthèse*

Le **rapport d'audit** expose de façon complète le périmètre, la méthode, chaque constat avec ses éléments probants, ses causes et ses recommandations ; il s'adresse aux audités et documente la mission. La **note de synthèse** en extrait, pour un décideur qui n'a pas le temps de lire le rapport, l'appréciation globale et les constats qui appellent une décision, **hiérarchisés**, chacun assorti du risque, de la recommandation, du responsable, de la priorité et de l'échéance ; elle tient en une page et prépare une décision (F10 § 1.2 et § 5).

Hiérarchie attendue : les **comptes partagés et les annulations sans validation** (risque de fraude non détectable, relevé déjà en 2021 et en 2023) et le **réseau sans fil du public relié aux caisses**, aggravé par des logiciels sans mises à jour (porte d'entrée ouverte à n'importe quel visiteur, alors qu'une collectivité voisine vient de subir un rançongiciel) viennent en priorité 1 ; l'**écart de 18 k€**, d'un montant limité mais non expliqué, et la **conservation sans limite** des fiches d'anciens abonnés viennent en priorité 2. Le non-suivi des audits précédents ne forme pas un cinquième constat : il justifie le dispositif de suivi qui conclut la note.

Note modèle (environ 17 lignes) :

<!-- note -->
**À Mme VARSANGE – Audit des caisses et de la billetterie des piscines (2026) – Note de synthèse pour le comité de direction du 18/05/2027**
**Appréciation globale** : les encaissements et la sécurité des caisses sont mal maîtrisés ; les faiblesses de 2021 et 2023 persistent.
**1. Comptes partagés et annulations libres (priorité 1).** 45 agents sur 60 sur des comptes communs ; 6 000 tickets annulés (30 k€) sans motif ni validation. Risque : fraude impossible à détecter et à imputer. Recommandation : un identifiant par agent, annulation validée par un responsable, revue hebdomadaire. M. SALVÉRAC, 30/06/2027.
**2. Caisses exposées (priorité 1).** Wi-Fi du public sur le réseau des caisses ; logiciel et système sans mises à jour. Risque : intrusion, vol de données de paiement, caisses arrêtées. Recommandation : séparer les réseaux, corriger, remplacer les postes hors support. M. LANDOUSSE, 30/06/2027 ; postes fin 2027.
**3. Écarts non expliqués (priorité 2).** 18 k€ d'encaissements manquants. Risque : pertes, recettes non fiables. Recommandation : rapprochement quotidien, écart justifié au-delà d'un seuil, revue mensuelle des finances. M. SALVÉRAC et finances, 30/09/2027.
**4. Données conservées sans limite (priorité 2).** 32 000 fiches d'anciens abonnés, dont 25 000 de plus de trois ans. Risque : non-conformité au RGPD, fuite aggravée. Recommandation : durée fixée avec le DPO, purge. M. SALVÉRAC, 31/12/2027.
**Suivi** : plan d'action validé en comité de direction, point trimestriel, audit de suivi en janvier 2028.
<!-- /note -->

*3.1 b) – Facteurs de succès et points de vigilance*

**Deux facteurs de succès** (b-1) :
1. **Un portage par la direction générale et un suivi formalisé des recommandations.** Les plans de 2021 et de 2023 ont été acceptés puis oubliés, faute de suivi. Il faut que Mme VARSANGE fasse valider le plan d'action par le comité de direction, désigne un responsable et une échéance par recommandation, tienne un tableau de suivi présenté chaque trimestre et prévoie un audit de suivi en janvier 2028. C'est la composante « pilotage » du COSO 2013 (annexe 3.5).
2. **L'adhésion des audités, obtenue par des constats établis contradictoirement et des recommandations réalistes.** M. SALVÉRAC conteste : les constats chiffrés doivent lui être présentés comme des faiblesses du dispositif, et non comme un soupçon sur ses agents. Les comptes nominatifs **protègent les agents honnêtes**, puisqu'une annulation n'est plus imputable à toute l'équipe. La recommandation doit tenir compte de sa contrainte d'accueil : changement d'utilisateur rapide (code court ou badge plutôt qu'une nouvelle connexion), validation seulement au-delà d'un seuil.

**Deux points de vigilance** (b-2) :
1. **L'indépendance et la légitimité de l'auditrice.** Mme TRÉVAZIN est une agente de la ville, dont le directeur général arrête son programme et dirige aussi la direction du numérique mise en cause par deux constats (réseau, mises à jour). Elle risque d'être gênée pour critiquer sa propre collectivité, et d'être perçue par l'agglomération comme « l'audit de la ville ». Il faut une lettre de mission signée par la directrice générale de l'agglomération, une restitution directe à celle-ci, une charte d'audit commune aux deux collectivités, et la possibilité de faire revoir par un tiers les constats qui touchent la direction mutualisée.
2. **La dilution des responsabilités entre les directions et l'attentisme.** La direction du numérique renvoie au schéma directeur de 2028 ; la billetterie a été choisie sans elle ; chaque constat peut rebondir entre la direction des piscines, la direction mutualisée et l'éditeur. Il faut désigner **un seul responsable** par recommandation et décider tout de suite des mesures transitoires qui ne dépendent pas du schéma directeur : la séparation du réseau sans fil du public et l'installation des correctifs, demandées à la direction mutualisée par un arbitrage de la directrice générale.

**Réponses tolérées**
- Autre ordre de priorité justifié (par exemple l'écart de 18 k€ en priorité 1 avec les annulations, au titre du risque de détournement de fonds publics), si les quatre constats sont complets.
- Regroupement de la conservation des données et de l'accès tardif à l'extraction de l'éditeur dans un constat de « maîtrise de l'éditeur de billetterie ».
- Note présentée en tableau (constat, risque, recommandation, responsable, priorité, échéance) si elle reste dans les 20 lignes et comporte une appréciation globale.
- Autres facteurs de succès : accès aux données garanti par une clause des contrats des éditeurs (six semaines pour obtenir l'extraction) ; compétences en systèmes d'information de l'auditrice ou appui de la direction mutualisée ; information des élus. Autres points de vigilance : proportionnalité du coût des contrôles aux enjeux (18 k€), conduite du changement des 60 agents d'accueil, confidentialité des constats de sécurité.
- Responsables désignés par leur fonction (directeur des piscines, directeur du numérique mutualisé, responsable de la sécurité des systèmes d'information) plutôt que par leur nom.

**Erreurs fréquentes**
- *Démarche ou tests d'audit développés au lieu de la note* (`JUR-T07`) — juste : la note et ses suites ; la démarche n'est pas demandée.
- *Constats non hiérarchisés ou sans responsable ni échéance* (`JUR-T03`) — juste : une priorité, une personne et une date pour chaque recommandation.
- *Note qui dépasse 20 lignes ou qui recopie les notes brutes* (`JUR-T07`) — juste : une appréciation globale et quatre constats regroupés.
- *Audit du SI confondu avec l'audit légal des comptes* (`ET-34`) — juste : audit interne des caisses et de leur sécurité, sans opinion sur les comptes.
- *Facteurs de succès génériques* (`JUR-T01`) — juste : reliés aux deux audits sans suite, à la contestation de M. SALVÉRAC, à l'attentisme de la direction du numérique et au rattachement de l'auditrice à la ville.
- *Réactions des responsables ignorées* (`JUR-T08`) — juste : elles fondent les facteurs de succès et les points de vigilance.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Note de synthèse, diagnostic d'audit, facteurs de succès | constat, risque, recommandation, priorité, échéance ; indépendance, suivi | F10 § 1.2 et § 5 | notion de cours |
| COSO 2013 | pilotage du contrôle interne, suivi des faiblesses relevées | `coso_2013` ; F10 § 2 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | identification nominative, mises à jour, cloisonnement du réseau | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | durée de conservation limitée, sécurité | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.2 – La fiabilité de la chaîne « levée → facture » (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels » (contrôles applicatifs, séparation des tâches, piste d'audit, intégrité des interfaces, sauvegardes et restauration éprouvées). Limite : la conformité financière et comptable n'est pas traitée ; aucune règle de comptabilité publique ni de finances locales n'est mobilisée.

**Annexes mobilisées** : annexe 3.2 (déroulement, constats de 2026, échéance de juillet 2027), annexe 3.5 (ISO/IEC 27001:2022 et 27002:2022, COSO 2013) et annexe 1.1 (redevance incitative, logiciel de facturation hébergé par l'éditeur, camions).

**Barème indicatif (3 pts)**

| Item | Attendu | Points |
|---|---|---|
| 1 | Fiabilisation définie (données exactes, exhaustives, autorisées, traçables et disponibles) ; contrôles généraux informatiques et contrôles applicatifs distingués | 0,5 |
| 2 | Contrôle de l'interface camions → logiciel : constat, risque, nature, responsable | 0,5 |
| 3 | Contrôle des tarifs et du calcul, avec séparation des tâches : constat, risque, nature, responsable | 0,5 |
| 4 | Traçabilité des corrections (comptes nominatifs, journal) : constat, risque, nature, responsable | 0,5 |
| 5 | Sauvegarde et restauration éprouvée : constat, risque, nature, responsable | 0,5 |
| 6 | Contrôle à mettre en place en premier, justifié par l'échéance de juillet 2027 | 0,5 |

**Réponse attendue**

**Définitions** (item 1). **Fiabiliser** un système d'information de gestion, c'est organiser les traitements et les contrôles pour que les données qu'il produit, ici les levées et les factures, soient **exactes, exhaustives, autorisées, traçables** et **disponibles**, et qu'on puisse reconstituer le chemin de chaque facture jusqu'aux levées qui la justifient (piste d'audit). Les **contrôles généraux informatiques** portent sur l'environnement du système : gestion des accès, gestion des changements, exploitation (sauvegardes, supervision). Les **contrôles applicatifs** sont propres à un traitement : contrôles à la saisie, au traitement, aux interfaces et en sortie (F10 § 2 et § 3). La chaîne « levée → facture » en a besoin des deux.

**Quatre contrôles** (items 2 à 5) :

| Contrôle | Constat de l'annexe 3.2 | Risque traité | Nature | Qui le met en œuvre |
|---|---|---|---|---|
| **Intégrité de l'interface** : chaque fichier porte l'identifiant de la tournée et le nombre de levées ; l'ordinateur embarqué le conserve jusqu'à l'accusé de réception du serveur d'échange ; le logiciel refuse un fichier déjà importé ; chaque matin, un **rapprochement** automatique compare la liste des tournées réalisées, les fichiers reçus et les levées importées, et chaque écart ou rejet est traité et tracé | 120 tournées et environ 20 000 levées perdues ; 300 fichiers réimportés à la main, 5 000 levées facturées deux fois ; aucun rapprochement | facturation **incomplète** (levées perdues, usagers traités inégalement) ou **en double** (réclamations, perte de confiance) | préventive (accusé de réception, refus des doublons) et détective (rapprochement quotidien) | direction du numérique mutualisée (serveur d'échange), fabricant des équipements embarqués et éditeur (évolutions à demander) ; le rapprochement est revu chaque matin par le service de la facturation |
| **Tarifs et calcul des factures** : séparation des tâches entre l'agent qui saisit les tarifs et la responsable du service, qui les valide en les comparant aux tarifs votés avant tout lancement ; contrôles de vraisemblance bloquants (tarif hors d'une plage admise, facture qui dépasse un multiple de celle du semestre précédent) ; revue d'un échantillon de factures et des montants les plus élevés avant l'envoi | un même agent saisit les tarifs et lance la facturation ; tarif saisi à 25 € au lieu de 2,50 € ; 3 000 factures erronées, 900 réclamations | **facturation erronée de masse**, coût de traitement des réclamations, atteinte à l'acceptation de la redevance | préventive (double validation, contrôles bloquants) et détective (revue avant envoi) | Mme DARNÉZAN valide ; l'éditeur sépare les profils de saisie des tarifs et de lancement |
| **Traçabilité des corrections** : un compte nominatif par agent ; un journal des modifications (auteur, date, motif, valeur avant et après) que l'on ne peut pas modifier ; motif obligatoire, validation des corrections au-delà d'un montant ; revue mensuelle d'un échantillon | six agents sur le même compte « facturation » ; 4 000 factures modifiées sans trace | **fraude interne** (dette effacée), **erreurs non détectées**, impossibilité de justifier une facture devant l'usager | préventive (comptes nominatifs, validation) et détective (journal, revue) | l'éditeur (fonction de journalisation, à exiger), la direction du numérique (comptes), le service de la facturation (revue) |
| **Sauvegarde et restauration éprouvée** : sauvegarde du serveur d'échange hors de la salle du siège (par exemple dans la salle de l'hôtel de ville) et copie hors ligne ; alerte en cas d'échec d'une sauvegarde ; **test de restauration** au moins annuel, pour le serveur et pour la base de l'éditeur ; délai de restauration et perte de données admissible fixés avec l'éditeur | aucune restauration essayée ; sauvegarde dans la même salle ; sauvegarde arrêtée depuis l'été sans que personne le voie ; contrat muet | **perte définitive** des levées ou des factures d'un semestre, impossibilité de facturer ou de répondre aux réclamations | préventive (sauvegarde déportée), détective (alerte, test) | direction du numérique mutualisée (serveur d'échange), éditeur (base, preuve du test), service de la facturation (exigences de délai et de perte admissible) |

**Le contrôle à mettre en place en premier** (item 6) : le **contrôle des tarifs et du calcul**. Il se met en place **avant juillet 2027** sans évolution du logiciel : une organisation (double validation, comparaison aux tarifs votés) et une revue avant l'envoi suffisent ; l'erreur qu'il prévient touche des milliers de factures d'un coup (3 000 en juillet 2026). En attendant les évolutions de l'interface, qui dépendent du fabricant et de l'éditeur, un **rapprochement manuel** des tournées réalisées et des fichiers reçus peut compenser.

**Réponses tolérées**
- Le contrôle de l'interface placé en premier, si le candidat justifie par la perte continue de levées (1 % des tournées) et par les doublons, et prévoit un contrôle compensatoire des tarifs pour juillet 2027.
- Séparation des tâches présentée comme un cinquième contrôle, à condition que les quatre contrôles demandés soient traités.
- Référence au COSO 2013 (activités de contrôle) ou aux mesures de journalisation et de sauvegarde de l'ISO/IEC 27002:2022.
- Exigences envers l'éditeur exprimées comme des engagements de service (délai de restauration, perte admissible, preuve des tests), sans analyse juridique du contrat.
- Délai de restauration et perte de données admissible désignés par les sigles RTO et RPO, correctement définis.

**Erreurs fréquentes**
- *Contrôles génériques, sans lien avec les constats* (`JUR-T01`, `JUR-T08`) — juste : chaque contrôle répond à un chiffre de l'annexe 3.2.
- *Sauvegarde sans test de restauration* (`JUR-S02`) — juste : une sauvegarde qu'on n'a jamais restaurée ne prouve rien ; l'été 2026 le montre.
- *Dérive vers la comptabilité publique ou le recouvrement* (limite du programme) — juste : la transmission au comptable public n'est pas à étudier.
- *Confusion entre un contrôle et un outil* (« acheter un logiciel ») (`ET-01`) — juste : un contrôle est une règle, avec un responsable et une trace.
- *Nature préventive ou détective omise* — juste : elle est demandée pour chaque contrôle.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Fiabilisation, contrôles généraux et applicatifs, séparation des tâches, piste d'audit | définitions et contrôles | F10 § 2 et § 3 | notion de cours |
| COSO 2013 | activités de contrôle (toléré) | `coso_2013` ; F10 § 2 | en vigueur |
| ISO/IEC 27002:2022 | mesures de journalisation, de sauvegarde et de contrôle d'accès | `iso_27002_2022` ; F12 § 2 | en vigueur |

---

### 3.3 – Les risques et la sécurité des équipements connectés et des systèmes techniques (3,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information… ». Limite : l'analyse de sécurité technique détaillée n'est pas attendue.
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique et les démarches de certification ne sont pas attendues ; le Zero Trust est un cadre, pas un produit.

**Annexes mobilisées** : annexe 3.3 (inventaire, incidents, témoignages), annexe 3.5 (ISO/IEC 27001:2022, guide d'hygiène, Zero Trust, Cyber Resilience Act, RGPD) et annexe 1.1 (camions, déchèteries, piscines, direction du numérique mutualisée portée par la ville).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée : trois catégories définies ; risque = événement redouté apprécié par sa probabilité et son impact | 0,5 |
| a-2 | Cinq risques tirés de l'annexe 3.3, formulés comme des événements, couvrant les trois catégories | 0,5 |
| a-3 | Deux risques prioritaires justifiés par leur probabilité et leur impact | 0,5 |
| b-1 | Architecture de confiance définie ; principes de séparation des réseaux et d'accès à distance des mainteneurs, reliés aux constats | 0,5 |
| b-2 | Principes de chiffrement et de mises à jour (inventaire, mots de passe d'usine), reliés aux constats | 0,5 |
| c-1 | Rôles des quatre acteurs (agglomération, direction du numérique et RSSI, éditeurs et fabricants, mainteneurs) | 0,5 |
| c-2 | Formalisation (politique étendue, matrice des rôles, clauses de sécurité, instance) et positionnement du RSSI | 0,5 |

**Réponse attendue**

*3.3 a) – Typologie, cinq risques et deux priorités*

Un **risque** lié au système d'information est un événement redouté qui atteint la disponibilité, l'intégrité, la confidentialité ou la traçabilité de l'information et des traitements ; il s'apprécie par sa **probabilité** et son **impact**. On distingue : les **cybermenaces**, actes malveillants (rançongiciel, intrusion, usurpation d'un compte) ; les **défaillances opérationnelles**, pannes, erreurs ou défauts d'exploitation et de maintenance, y compris la dépendance à un prestataire ; les **risques réglementaires et métiers**, non-respect d'une obligation et atteinte à la mission elle-même, ici le service public (F12 § 0 et § 5).

| N° | Risque (événement redouté) | Catégorie | Faits de l'annexe 3.3 |
|---|---|---|---|
| R1 | Rançongiciel entré par l'accès à distance du mainteneur, qui chiffre la télégestion des piscines puis se propage aux réseaux de bureau de l'agglomération et de la ville | cybermenace | accès permanent, compte unique de 12 techniciens, mot de passe de 2019, messagerie sur le poste de supervision, réseaux non séparés ; scénario survenu chez la voisine en novembre 2026 |
| R2 | Prise de contrôle des ordinateurs embarqués des camions, qui fausse ou supprime les levées et sert de porte d'entrée | cybermenace | même mot de passe d'usine sur 40 ordinateurs, faille publiée en 2026 non corrigée, accès au réseau mobile |
| R3 | Arrêt des six déchèteries par la panne du serveur unique du contrôle d'accès | défaillance opérationnelle | un samedi bloqué en septembre 2026, 2 000 usagers refoulés ou admis sans contrôle ; aucun inventaire de la direction du numérique |
| R4 | Panne ou dysfonctionnement durable d'un équipement non maintenu (camions, contrôle d'accès, télégestion), faute d'un responsable de ses mises à jour, les contrats ne traitant pas de la sécurité | défaillance opérationnelle (dépendance aux prestataires) | « c'est au client de les installer » ; « notre contrat ne porte pas sur l'informatique » |
| R5 | Mise en cause de l'agglomération pour la conservation sans limite des images de plaques d'immatriculation des véhicules des professionnels, qui permettent d'identifier des personnes (RGPD : conservation limitée, sécurité adaptée, annexe 3.5) | risque réglementaire | images des plaques conservées sans limite de durée ; caméras sur le réseau de bureau |
| R6 | Fermeture des piscines ou mauvais traitement de l'eau, mettant en jeu la santé des baigneurs et la continuité du service public | risque métier | télégestion non pilotable chez la voisine ; objectif « continuité et sécurité des services publics, numériques et techniques » de « Castelrive 2032 » |

Cinq risques suffisent, dont au moins un par catégorie.

**Deux risques prioritaires** (a-3) :
- **R1** : **probabilité élevée**. L'accès est ouvert en permanence, avec un compte partagé et un mot de passe inchangé depuis 2019, et le scénario vient de se réaliser chez une voisine. **Impact très fort** : fermeture des quatre piscines pendant des semaines, risque sanitaire, propagation à toute l'agglomération et à la ville par des réseaux non séparés.
- **R2** : **probabilité élevée**, avec un mot de passe d'usine identique sur 40 ordinateurs et une faille connue non corrigée. **Impact fort** : la collecte et la facturation de 84 000 redevables reposent sur ces levées.
On peut aussi retenir R6, conséquence métier de R1, si le choix est justifié.

*3.3 b) – Quatre principes d'architecture de confiance*

Une **architecture de confiance** organise les systèmes pour que la confiance accordée à un utilisateur, à un équipement ou à une connexion soit **vérifiée à chaque accès et limitée au nécessaire** : authentification, autorisation au moindre privilège, chiffrement, cloisonnement, traçabilité. Le modèle **Zero Trust** en est le cadre de référence : aucune confiance implicite liée à la place dans le réseau. C'est un modèle d'architecture que l'on adopte progressivement, en complément de la défense en profondeur, et non un produit (annexe 3.5 ; F12 § 3).

| Principe | Application aux équipements de l'agglomération | Constat de l'annexe 3.3 |
|---|---|---|
| (b-1) **Séparation des réseaux techniques et du réseau de bureau** | placer la télégestion, le contrôle d'accès et le serveur d'échange des camions dans des zones distinctes du réseau de bureau et du réseau de la ville, avec des échanges limités au strict nécessaire et contrôlés ; un poste de supervision dédié, sans messagerie ni navigation | équipements sur le même réseau que les bureaux, lui-même relié à la ville ; caméras sur le réseau de bureau ; messagerie sur le poste de supervision |
| (b-1) **Authentification et traçabilité des accès à distance** | un compte nominatif par technicien du mainteneur, une authentification à plusieurs facteurs, un accès ouvert à la demande pour une intervention et refermé ensuite, par un point d'entrée unique contrôlé par l'agglomération plutôt qu'un logiciel de prise de main installé sur le poste ; sessions journalisées et revues | compte unique de 12 techniciens, mot de passe de 2019, accès à tout moment |
| (b-2) **Chiffrement** | chiffrer les échanges entre les capteurs et la plateforme, entre les camions et le serveur d'échange, et les données sensibles stockées (images des plaques) ; en faire une exigence envers les fabricants | mesures des capteurs transmises sans chiffrement ; levées transmises par le réseau mobile |
| (b-2) **Mises à jour et durcissement** | inventaire de tous les équipements connectés et techniques ; mots de passe d'usine changés et distincts pour chaque équipement ; politique de mise à jour avec calendrier et responsable ; à l'achat, exiger une durée de support et des mises à jour de sécurité, que le Cyber Resilience Act imposera aux fabricants à partir du 11/12/2027 | ordinateurs jamais mis à jour, faille non corrigée, mot de passe d'usine identique sur 40 ordinateurs, aucun équipement dans l'inventaire |

*3.3 c) – Rôles, responsabilités et formalisation*

Ces équipements sont des **systèmes critiques** du service public : la collecte, la facturation, les déchèteries et la sécurité des baigneurs en dépendent. Leur sécurité ne peut être laissée « au technique ».

| Acteur | Rôles et responsabilités |
|---|---|
| **Directrice générale des services de l'agglomération** | approuve l'extension de la politique de sécurité aux systèmes techniques, fixe le niveau de risque accepté, arbitre les moyens avec la ville au sein de l'instance commune, rend compte aux élus |
| **Directions utilisatrices** (collecte, piscines) | propriétaires de leurs systèmes et des risques métier : déclarent leurs équipements à l'inventaire, autorisent les accès de leurs mainteneurs, prévoient le mode dégradé (conduite manuelle des chaufferies, ouverture manuelle des barrières), font inscrire les exigences de sécurité dans leurs contrats |
| **Direction du numérique mutualisée** | exploite la séparation des réseaux, le point d'entrée des accès à distance, les sauvegardes et la supervision ; installe les mises à jour ou en contrôle l'installation |
| **RSSI mutualisé** | définit les règles, conduit l'analyse des risques, conseille les directions, revoit les accès, pilote le traitement des incidents, rend compte de l'état de sécurité |
| **Éditeurs et fabricants** | fournissent des produits sûrs, publient et signalent les correctifs de sécurité, informent l'agglomération des vulnérabilités et des incidents (obligations du Cyber Resilience Act, échelonnées de 2026 à 2027), respectent les exigences de chiffrement et de comptes |
| **Mainteneurs** | n'accèdent qu'avec des comptes nominatifs et sur demande, tracent leurs interventions, sécurisent leurs propres postes et signalent sans délai tout incident |

**Formalisation et suivi** (c-2) : (1) la **politique de sécurité de 2023 étendue** aux équipements connectés et aux systèmes techniques ; (2) une **matrice des responsabilités** (réalise, approuve, consulté, informé) pour l'inventaire, les accès à distance, les mises à jour et les incidents ; (3) des **clauses de sécurité** ajoutées aux contrats de maintenance et aux contrats des éditeurs (mises à jour, accès, signalement des incidents, droit d'audit) ; (4) un **comité de sécurité commun** à la ville et à l'agglomération, qui se réunit chaque trimestre et suit les risques et le plan d'action.

**Positionnement du RSSI** : rattaché au directeur du numérique, il contrôle ce que sa propre hiérarchie exploite, et il n'a aucune autorité sur l'agglomération. Il devrait relever **fonctionnellement des deux directions générales**, ou de leur comité de sécurité commun, avec une mission écrite qui couvre les systèmes techniques des deux collectivités, un droit d'alerte direct auprès de Mme VARSANGE et des **correspondants sécurité** dans les directions de la collecte et des piscines.

**Réponses tolérées**
- Transmission sans chiffrement des mesures des capteurs présentée comme un risque d'intégrité (mesures faussées, tournées mal calculées), en cybermenace ou en défaillance ; elle ne relève pas du RGPD, ces mesures ne se rapportant à aucune personne.
- Autres risques pertinents : usurpation du compte partagé de la plateforme des capteurs ; dépendance à un mainteneur unique pour la nuit ; fraude à l'accès aux déchèteries ; risque d'image auprès des usagers et des élus.
- Cotation qualitative (faible, moyen, fort) ou matrice probabilité × impact, sans calcul.
- Référence aux mesures du guide d'hygiène de l'ANSSI (identification nominative, changement des éléments d'authentification par défaut, cloisonnement, mises à jour, maîtrise des risques liés aux prestataires) ou à l'annexe A de l'ISO/IEC 27001:2022.
- Matrice des responsabilités présentée en tableau croisé (activités × acteurs).
- Mention de NIS 2 comme cadre de gouvernance possible, si elle est datée correctement (directive non transposée en France au 31/12/2026) et si le candidat ne cherche pas à qualifier l'agglomération au regard de ce texte.

**Erreurs fréquentes**
- *Zero Trust présenté comme un produit à acheter* (`ET-04`, `JUR-S03`) — juste : un cadre d'architecture, progressif.
- *Mesures techniques détaillées ou paramétrages* (limite du programme 4.2) — juste : des principes, reliés aux constats.
- *Risques non classés ou catégorie manquante* (`JUR-T03`) — juste : cinq risques, trois catégories.
- *Sécurité des systèmes techniques laissée aux mainteneurs ou à la seule direction du numérique* (`JUR-T11`) — juste : responsabilités partagées, propriétaires métier dans les directions.
- *RSSI présenté comme un technicien ou maintenu sous le seul directeur du numérique* (`ET-15`) — juste : une autorité fonctionnelle sur les deux collectivités.
- *Référentiels, normes et solutions confondus* (`ET-01`, `JUR-S06`) — juste : ISO/IEC 27001 (norme), guide d'hygiène (guide), Zero Trust (modèle), Cyber Resilience Act (règlement).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques, architecture de confiance, rôles | définitions, principes | F12 § 0, § 1, § 3 et § 5 | notion de cours |
| ISO/IEC 27001:2022 et ISO/IEC 27002:2022 | mesures de l'annexe A (accès, vulnérabilités, séparation des réseaux, fournisseurs) | `iso_27001_2022`, `iso_27002_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | identification nominative, authentification par défaut, cloisonnement, mises à jour, prestataires | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Modèle Zero Trust (avis de l'ANSSI, 2021) | cadre d'architecture | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| Règlement (UE) 2024/2847 (Cyber Resilience Act) | obligations des fabricants : sécurité dès la conception, mises à jour, signalement | `cra` ; F12 § 7 | signalement depuis le 11/09/2026 ; application générale le 11/12/2027 |
| Règlement (UE) 2016/679 (RGPD) | conservation limitée, sécurité | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.4 – La stratégie numérique responsable de l'agglomération (4 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable… » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI ». Limites : la durabilité doit être intégrée à la gouvernance globale du SI et non traitée comme un ajout marginal ; les résultats d'empreinte sont donnés, jamais calculés.

**Annexes mobilisées** : annexe 3.4 (obligation non remplie, état des lieux, premières mesures, projet de tournées optimisées), annexe 3.5 (loi REEN, RGESN, étude ADEME-Arcep) et annexe 1.1 (projet « Castelrive 2032 », direction du numérique mutualisée, dépenses du numérique).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Sobriété numérique définie (interroger le besoin d'abord) ; Green IT et IT for green distingués ; pour au moins trois dimensions, niveau actuel décrit de façon observable et justifié par l'annexe 3.4, et niveau visé en 2030, sur l'échelle à quatre niveaux donnée par la question | 0,5 |
| a-2 | Deux premiers axes, reliés chacun à un constat chiffré | 0,5 |
| a-3 | Deux autres axes, et ordre de priorité justifié (part de la fabrication, gains rapides) | 0,5 |
| a-4 | Gouvernance (adoption, portage, instance commune avec la ville, intégration au futur schéma directeur) et trajectoire datée jusqu'en 2030 | 0,5 |
| b-1 | Deux arguments en faveur du projet et deux limites tirées de l'annexe 3.4 D | 0,5 |
| b-2 | Conditions de la recommandation (expérimentation, mesure du bilan net, sobriété du dispositif) | 0,5 |
| c-1 | Premier indicateur complet (formule, source, fréquence, cible, axe) | 0,5 |
| c-2 | Second indicateur complet | 0,5 |

**Réponse attendue**

*3.4 a) – Définitions, grille de maturité et stratégie*

La **sobriété numérique** consiste à interroger d'abord le **besoin** (cet équipement, ce service, ce calcul, cette impression sont-ils utiles ?) avant de chercher l'efficacité ; elle ne se réduit pas à une économie d'énergie. Le **Green IT** réduit l'empreinte du système d'information lui-même (équipements, salles informatiques, logiciels, usages). L'**IT for green** mobilise le numérique pour réduire l'empreinte d'une autre activité de l'organisation : le projet de tournées optimisées en relève (F14 § 3).

**Grille de maturité du numérique responsable** (F09 § 5 ; F14). Les quatre niveaux sont donnés par la question ; la grille complète figure ici à titre de référence, et le candidat n'a qu'à décrire, pour chaque dimension, le niveau actuel et le niveau visé :

| Dimension | 1 – Initial | 2 – Engagé | 3 – Structuré | 4 – Piloté | Agglomération en 2027 → cible 2030 |
|---|---|---|---|---|---|
| Équipements et achats | renouvellement à date fixe, achat au prix | actions ponctuelles (réemploi occasionnel) | durée de vie allongée, critères environnementaux dans les achats | durée de vie et achats suivis par des indicateurs, revus chaque année | **1** (postes tous les quatre ans par lots, téléphones tous les deux ans, prix seul, 30 % des tablettes inutilisées) → **3** |
| Infrastructures | aucune mesure | consommation connue | serveurs inutiles retirés, consolidation, PUE suivi | PUE et consommation pilotés selon une cible | **1 à 2** (PUE 2,2 et 2,0, 40 serveurs inutiles, utilisation de 15 %, 900 MWh connus) → **3** |
| Usages et services | aucune règle | « écogestes » affichés | règles d'impression et de stockage, sensibilisation, écoconception des nouveaux services | évaluation environnementale de chaque projet avant décision | **2** (écogestes de 2023, 4 millions de pages) → **3** |
| Gouvernance et mesure | ni responsable ni mesure | première mesure isolée | stratégie adoptée, responsable désigné, bilan annuel | objectifs intégrés au schéma directeur et au projet de territoire, rendus aux élus | **2** (bilan de fin 2026, mais aucune stratégie, aucun responsable, rien présenté aux élus) → **4** |

**Quatre axes priorisés** :

| Rang | Axe | Constat de l'annexe 3.4 | Contenu |
|---|---|---|---|
| 1 (a-2) | **Allonger la durée de vie des équipements et acheter de façon responsable** | la fabrication pèse environ 70 % de l'empreinte ; postes tous les quatre ans, téléphones tous les deux ans, achat au prix ; 400 postes et 900 téléphones stockés | passer à six ans pour les postes (un tiers d'achats en moins) et à quatre ans pour les téléphones (moitié moins), renouveler au cas par cas ; critères de garantie, de réparabilité, de reconditionnement et de reprise ; réaffecter les tablettes inutilisées ; réemploi des équipements stockés avant leur enlèvement |
| 2 (a-2) | **Rationaliser les salles informatiques, avec la ville** | 120 serveurs utilisés à 15 %, 40 sans application ; PUE de 2,2 et 2,0 ; environ 20 % de l'empreinte | retirer les serveurs inutiles, virtualiser et consolider, moderniser la climatisation, puis regrouper l'hébergement dans la salle la plus efficace, avec un PUE cible |
| 3 (a-3) | **Évaluer et écoconcevoir les projets et les services numériques** | projet de tournées sans estimation d'empreinte ; services des éditeurs sans aucune donnée | évaluer chaque projet (besoin, empreinte de ses équipements et de ses calculs) avant décision, appliquer les critères du RGESN et exiger des éditeurs leurs données de consommation, pour compléter le bilan : selon l'étude ADEME-Arcep, les centres de données, y compris ceux situés à l'étranger, pèsent près de la moitié de l'empreinte du numérique en France, alors que le bilan de l'agglomération exclut les services hébergés |
| 4 (a-3) | **Rendre les usages plus sobres et former** | 4 millions de pages, 150 imprimantes individuelles ; écogestes sans suite | retirer les imprimantes individuelles au profit des copieurs, impression recto verso par défaut, dématérialisation pertinente ; former les agents et les élus au numérique responsable, comme le prévoit la loi REEN |

**Ordre de priorité** (a-3) : la fabrication domine l'empreinte, ici environ 70 % ; les terminaux restent, selon l'étude ADEME-Arcep, la première source de l'empreinte du numérique, surtout par leur fabrication. L'allongement de la durée de vie passe donc en premier : il est aussi le moins coûteux. Les salles viennent ensuite, car le retrait des serveurs inutiles est un gain rapide ; l'évaluation des projets doit précéder la décision sur les tournées ; la sobriété des usages accompagne le tout.

**Gouvernance et trajectoire** (a-4) : la stratégie est **adoptée par le conseil communautaire** et portée par un(e) vice-président(e). Elle est construite **avec la ville**, elle aussi tenue d'en avoir une et qui partage la direction du numérique et les salles informatiques. Elle est pilotée par un **comité du numérique responsable commun** aux deux collectivités, qui réunit chaque semestre la direction générale, la direction du numérique, Mme PRÉVILLAN, les achats, les directions utilisatrices et des représentants des agents, autour d'un référent désigné à la direction du numérique. Elle est **intégrée au futur schéma directeur** et à l'objectif « réduire l'empreinte environnementale du numérique » de « Castelrive 2032 », et non ajoutée à côté. Trajectoire :
- **2027** : adoption avant la fin de l'année ; retrait des serveurs inutiles ; téléphones conservés quatre ans ; réemploi du stock ; bilan complété des services hébergés ;
- **2028** : critères d'achat et évaluation environnementale des projets inscrits au schéma directeur ;
- **2029** : consolidation des salles informatiques ;
- **2030** : postes conservés six ans et empreinte réduite d'environ 30 % (environ 210 tCO2e contre 300), mesurée chaque année avec la même méthode.

*3.4 b) – Le projet de tournées optimisées et la sobriété*

**Deux arguments en sa faveur** (b-1) : (1) c'est de l'**IT for green** à fort enjeu : 150 tCO2e de gazole évitées chaque année, ordre de grandeur plausible pour 120 000 km de camions, soit la moitié de l'empreinte du numérique ; s'y ajoutent moins de bruit et d'usure des camions ; (2) il **cible un besoin réel** : le remplissage des bacs collectifs des immeubles et des professionnels varie, et les tournées fixes passent devant des bacs à moitié vides.

**Deux limites** (b-1) : (1) l'**empreinte du dispositif n'est pas mesurée**. Il faudrait 2 000 capteurs à pile, près de sept fois le parc actuel de 300 ; leur renouvellement tous les cinq ans produirait environ 400 capteurs et leurs piles à traiter chaque année. S'y ajoutent de nouvelles tablettes, alors que 30 % des tablettes existantes dorment, et un calcul chaque nuit dans le cloud, sans aucune donnée : le bilan net est inconnu, et le gain annoncé vient du vendeur lui-même ; (2) le **besoin n'est pas uniforme** : dans les communes rurales, les tournées changent peu, donc l'optimisation y apporterait peu. À cela s'ajoutent un risque d'effet rebond, 2 000 objets connectés de plus à sécuriser (question 3.3) et la dépendance à une jeune entreprise et à son cloud.

**Recommandation et conditions** (b-2) : recommander le projet **à titre d'expérimentation**, pas les 2 000 capteurs dès 2027 :
- un essai d'un an sur les secteurs à bacs collectifs de la ville-centre, avec une mesure des kilomètres avant et après ;
- un **bilan net** établi avec la même méthode que celui du bureau d'études (fabrication des capteurs et des tablettes, calcul, gazole évité), exigé de la jeune entreprise ;
- la sobriété du dispositif : capteurs seulement là où le remplissage varie ; tournées transmises aux ordinateurs embarqués ou aux tablettes existantes ; calcul hebdomadaire plutôt que quotidien si les gains sont proches ; modèle adapté à la tâche, comme le recommande le thème « algorithmie et intelligence artificielle » du RGESN ;
- des exigences de sécurité et de durée de vie dans le contrat ;
- une généralisation décidée par le comité du numérique responsable au vu du bilan net.

*3.4 c) – Deux indicateurs de suivi*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| (c-1) **Durée de vie moyenne des postes de travail au retrait** | somme des âges des postes retirés dans l'année / nombre de postes retirés | inventaire du parc de la direction du numérique mutualisée (dates d'achat et de retrait) | annuelle | 6 ans en 2030, contre 4 ans en 2026 | environnement |
| (c-2) **Empreinte carbone annuelle du numérique de l'agglomération** | somme des émissions estimées de la fabrication, de l'électricité, des impressions et des autres usages, puis des services hébergés quand les éditeurs fournissent leurs données (tCO2e) | bilan annuel tenu par la chargée de mission avec le bureau d'études (inventaire, relevés d'électricité, données des éditeurs) | annuelle, avec une méthode constante | 210 tCO2e au plus en 2030, contre environ 300 en 2026 (− 30 %), à périmètre comparable | environnement |

**Réponses tolérées**
- Grille de quatre ou cinq niveaux inspirée de CMMI, ou d'autres dimensions (données, compétences, inclusion), si chaque niveau est décrit de façon observable et si l'agglomération y est située à partir des annexes.
- Autres axes pertinents : sobriété des données (stockage, purge), réemploi et dons d'équipements, critères environnementaux dans le choix des éditeurs et des hébergeurs ; ordre différent s'il est justifié.
- Gouvernance portée par le comité de direction ou par l'élu(e) chargé(e) du numérique ; trajectoire découpée autrement.
- Projet rejeté si la justification tient au bilan net inconnu et au besoin non démontré, ou accepté sans expérimentation si la mesure du bilan net est exigée avant la généralisation.
- Autres indicateurs complets : PUE des salles informatiques (énergie totale consommée par la salle / énergie consommée par les équipements informatiques ; cible 1,6 au plus en 2029) ; nombre de pages imprimées par agent ; part des achats de matériels assortis de critères environnementaux ; part des serveurs utilisés ; part des agents formés au numérique responsable (axe social) ; bilan net de l'expérimentation des tournées (gazole évité − empreinte du dispositif).

**Erreurs fréquentes**
- *Sobriété réduite à une économie d'énergie* (`ET-12`) — juste : interroger le besoin (renouvellements, serveurs inutiles, capteurs, impressions).
- *Empreinte réduite à l'électricité ou au PUE* (`ET-38`) — juste : la fabrication représente environ 70 % ; le PUE ne mesure ni la fabrication ni l'origine de l'électricité.
- *Tension entre l'IA et la sobriété ignorée*, ou projet accepté sur la seule foi du gain annoncé (F14 § 8) — juste : bilan net et expérimentation.
- *Calcul d'empreinte tenté* — non attendu : les résultats sont donnés.
- *Grille de maturité « plate »* (F09 § 5) — juste : des niveaux distincts et observables.
- *Durabilité traitée en ajout marginal* (limite du programme) — juste : intégrée au schéma directeur, au projet de territoire et à une gouvernance commune.
- *Indicateurs génériques, sans cible ni source* (`ET-18`, `JUR-A02`) — juste : deux indicateurs complets, avec leur valeur de départ.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Sobriété, Green IT et IT for green, indicateurs, grille de maturité | définitions, PUE, durée de vie, part de la fabrication | F14 § 1 à 4 ; F09 § 5 | notion de cours |
| Loi n° 2021-1485 du 15 novembre 2021 (REEN) | stratégie numérique responsable des collectivités de plus de 50 000 habitants au 01/01/2025, durée de vie, sensibilisation | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | écoconception, interrogation du besoin, thème de l'algorithmie et de l'IA | `rgesn_2024` ; F14 § 2 | version 2 publiée le 17/05/2024 |
| Étude ADEME-Arcep | poids du numérique (4,4 %), part des terminaux (environ la moitié, surtout par leur fabrication) et des centres de données (environ 46 %) dans l'empreinte | `etude_ademe_arcep_numerique` ; F14 § 1 | mise à jour du 17/01/2025 |
| CMMI (toléré pour les niveaux de la grille) | niveaux de maturité | `cmmi_v3` ; F09 § 5 | en vigueur |
