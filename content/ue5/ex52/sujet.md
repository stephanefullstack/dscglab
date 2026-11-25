# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 52

**DOSSIER 1 – PRÉPARER LA GOUVERNANCE DU SYSTÈME D'INFORMATION ET LA CONDUITE DU PROJET VIGIE (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 18, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mai 2027. Le service départemental d'incendie et de secours (SDIS) du Val-d'Aurande est un établissement public administratif départemental chargé de la prévention, de la protection et de la lutte contre les incendies et des secours aux personnes dans un département de 640 000 habitants, rural pour l'essentiel, qui s'étend du massif du Haut-Aurande aux plaines de la vallée de l'Aurande. Son conseil d'administration réunit des élus du département, des communes et des intercommunalités, qui le financent à hauteur de 55 % et 45 %. En 2026, le centre de traitement de l'alerte, installé au siège de Montcerneau, a reçu 150 000 appels, et les 60 centres d'incendie et de secours du département ont réalisé 50 000 interventions avec 420 engins. Le SDIS compte 700 sapeurs-pompiers professionnels, 250 personnels administratifs et techniques et 3 900 sapeurs-pompiers volontaires ; son budget de fonctionnement s'est élevé à 105 M€. Les organisations, les personnes et les données de ce cas sont fictives.

Le projet d'établissement « Val-d'Aurande Secours 2031 », adopté en mars 2027 par le conseil d'administration, fixe cinq objectifs : maintenir le délai moyen d'arrivée des premiers secours sous 20 minutes dans toutes les communes ; fidéliser les volontaires en simplifiant leur engagement, au premier rang leur déclaration de disponibilité ; garantir la continuité du traitement de l'alerte, jour et nuit ; partager les données utiles avec les partenaires (centre de régulation médicale du SAMU, communes, département) ; réduire de 20 % l'empreinte environnementale de l'établissement d'ici 2031. Le système d'information s'est construit autour du logiciel de traitement de l'alerte, installé en 2012 ; les autres outils ont été ajoutés au fil des besoins, et plusieurs arrivent en fin de vie.

Vous êtes chef(fe) du groupement « Pilotage et systèmes d'information » du SDIS depuis 2026 ; vous dirigez le contrôle de gestion, le service des systèmes d'information et de communication et l'observatoire de l'activité. Le directeur départemental, le colonel hors classe Étienne GRANVOISE, vous demande trois travaux : préparer la gouvernance du SI et la conduite du projet VIGIE (dossier 1) ; organiser et exploiter les données des interventions, et en maîtriser la conservation (dossier 2) ; tirer les conclusions d'un audit, maîtriser les risques et la sécurité du SI opérationnel et en réduire l'empreinte (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation du SDIS du Val-d'Aurande et chiffres clés

Le SDIS du Val-d'Aurande est un établissement public administratif départemental. Il assure la prévention, la protection et la lutte contre les incendies et les secours aux personnes dans le département fictif du Val-d'Aurande, dans le centre-est de la France : 640 000 habitants, un territoire rural pour l'essentiel, du massif du Haut-Aurande aux plaines de la vallée de l'Aurande. Son siège et son centre de traitement de l'alerte sont à Montcerneau, chef-lieu du département. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**La gouvernance et le financement**

| Donnée | Valeur |
|---|---|
| Conseil d'administration | 22 membres, élus du département, des communes et des intercommunalités ; président : M. Lucien FERMONTEIL, vice-président du conseil départemental |
| Direction | directeur départemental : le colonel hors classe Étienne GRANVOISE |
| Financement | département 55 % ; communes et intercommunalités 45 % |
| Budget 2026 | fonctionnement 105 M€, dont dépenses de personnel 80 % (indemnités des sapeurs-pompiers volontaires : 14 M€) ; investissement 15 M€ ; dépenses du système d'information, hors réseau radio : 3,6 M€ |

**L'activité en 2026**

| Donnée | Valeur |
|---|---|
| Centres d'incendie et de secours | 60, répartis en quatre groupements territoriaux : 12 centres mixtes, avec des professionnels et des volontaires, et 48 centres armés par des volontaires seulement |
| Appels reçus au centre de traitement de l'alerte | 150 000 |
| Interventions | 50 000 : secours d'urgence aux personnes 78 % ; accidents de la circulation 7 % ; incendies 7 % ; opérations diverses 8 % |
| Engins | 420 |
| Délai moyen d'arrivée des premiers secours | 14 minutes dans le département ; plus de 20 minutes dans une trentaine de communes du Haut-Aurande |

**L'effectif**

| Catégorie | Effectif |
|---|---|
| Sapeurs-pompiers professionnels | 700 |
| Personnels administratifs et techniques | 250, dont 24 au service des systèmes d'information et de communication (12 en informatique, 8 aux transmissions, 4 au soutien du centre de traitement de l'alerte) |
| Sapeurs-pompiers volontaires | 3 900, dont 600 professionnels également volontaires dans leur centre |

**Le système d'information en quelques lignes**

- **Logiciel de traitement de l'alerte et de gestion opérationnelle**, installé en 2012 et édité par un petit éditeur spécialisé : réception des appels, localisation, proposition des engins à engager, suivi des interventions. Il est hébergé sur des serveurs de la salle informatique du siège, doublée par une salle de secours au centre de Montcerneau-Sud.
- **Enregistreur des appels** du centre de traitement de l'alerte.
- **Logiciel de gestion des disponibilités des volontaires** (site web et messages SMS), installé en 2010 ; le support de son éditeur est assuré jusqu'à la fin de 2028.
- **Logiciel de gestion des indemnités des volontaires**, relié au logiciel de paie par un fichier mensuel.
- **Application de comptes rendus de secours** sur 300 tablettes embarquées dans les engins (2021).
- **Logiciel de gestion du parc** des engins et des équipements de protection individuelle.
- **Base des points d'eau d'incendie**, avec un système d'information géographique.
- Logiciel de ressources humaines et de paie ; progiciel financier ; plateforme de formation ; bureautique.

**Organigramme simplifié (mai 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil d'administration | président : M. Lucien FERMONTEIL |
| Conseil d'administration | direction départementale | directeur départemental : le colonel hors classe Étienne GRANVOISE |
| Direction départementale | déléguée à la protection des données | Mme Coralie FAVERJON |
| | groupement « Pilotage et systèmes d'information » : contrôle de gestion, service des systèmes d'information et de communication, observatoire de l'activité | vous ; cheffe du service des systèmes d'information et de communication : Mme Solène VARANGEOT ; chef de l'observatoire de l'activité : M. Rémi TRÉVIGNAN |
| | groupement des opérations, dont le centre de traitement de l'alerte | lieutenant-colonel Bertrand OSSELIN ; cheffe du centre de traitement de l'alerte : commandante Maëlle TOURNEVAL |
| | groupement du volontariat | lieutenant-colonel Hervé DOMBRESSAC |
| | service de santé et de secours médical | médecin-chef : Dr Agathe MÉRIGNOLLE |
| | groupement technique et logistique | M. Pascal LAUZERAC |
| | groupement des finances | Mme Laure CHAMBREUIL |
| | quatre groupements territoriaux | un chef de groupement territorial pour chacun |
| Groupements territoriaux | 60 centres d'incendie et de secours | un chef de centre pour chacun |

### ANNEXE 1.2 – Deux technologies à l'étude (note de la commandante Maëlle TOURNEVAL, cheffe du centre de traitement de l'alerte, avril 2027)

**A. La vidéo transmise par l'appelant.** Pendant l'appel, l'opérateur envoie un lien par SMS sur le téléphone de l'appelant ; en l'ouvrant, l'appelant filme la victime ou le sinistre, et l'opérateur voit les images en direct sur son poste. Deux SDIS voisins l'essaient depuis 2025. Ils nous ont communiqué leurs premiers résultats, sur environ 10 000 appels de secours d'urgence aux personnes pour lesquels un lien a été envoyé :
- la vidéo a fonctionné sept fois sur dix en ville, mais quatre fois sur dix seulement dans les zones de montagne, mal couvertes par le réseau mobile ;
- quand elle a fonctionné, les opérateurs ont modifié leur décision une fois sur huit : un moyen plus lourd engagé pour une détresse sous-estimée au téléphone, ou au contraire un simple conseil sans engin ;
- les opérateurs guident mieux les gestes de l'appelant en attendant les secours (massage cardiaque, position d'une victime) ;
- le traitement d'un appel avec vidéo dure en moyenne deux minutes de plus ;
- les images montrent des personnes blessées ou en détresse, parfois des enfants ; nos voisins s'interrogent sur leur affichage dans la salle et sur ce qu'il faut en garder.

**B. Les alertes automatiques des objets connectés.** En 2026, le centre a reçu environ 3 000 alertes déclenchées sans appel d'une personne, contre 1 500 en 2024 :
- 1 500 venaient de montres ou de téléphones qui détectent une chute ou un choc, dont neuf sur dix étaient de fausses alertes (geste brusque, téléphone tombé) ;
- 1 200 venaient de plateformes de téléassistance des personnes âgées, qui appellent après avoir tenté de joindre la personne ; une sur quatre était fausse ;
- 300 venaient de voitures qui appellent seules après un choc ; une sur deux était fausse.

Au total, six sur dix étaient de fausses alertes. Toutes ces alertes arrivent par un appel, un message vocal automatique ou un courriel, chacune dans son format, avec une position plus ou moins précise ; aucune n'entre directement dans le logiciel de traitement de l'alerte. Pour chacune, l'opérateur doit rappeler la personne ou un proche afin de lever le doute, ce qui prend en moyenne cinq minutes. Mais 40 fois en 2026, dont une vingtaine dans le Haut-Aurande, une alerte automatique a été le seul signal d'une personne seule, tombée ou blessée.

**C. Qui suit ces évolutions ?** Personne n'en est chargé. Nous les découvrons quand un éditeur vient nous présenter un produit, quand un collègue d'un autre SDIS nous en parle, ou par un écho dans la presse. Aucune instance ne décide de les étudier ni de les écarter.

### ANNEXE 1.3 – La gouvernance du système d'information vue par les acteurs (témoignages recueillis en avril 2027)

**M. Lucien FERMONTEIL, président du conseil d'administration** : « Le conseil ne voit les projets du système d'information qu'une fois par an, au vote du budget : 3,6 M€, une ligne parmi d'autres. On nous a demandé de voter les tablettes en 2020 ; personne ne nous a dit ensuite si elles avaient tenu leurs promesses. »

**Mme Solène VARANGEOT, cheffe du service des systèmes d'information et de communication** : « Au comité de direction, le système d'information n'a pas d'instance à lui : on en parle quand un problème remonte. Il n'existe aucune méthode de projet écrite : chaque groupement lance ses projets, puis vient nous demander de les installer. Depuis 2022, deux projets ont été abandonnés : un logiciel de planning des gardes choisi par un groupement territorial, arrêté au bout de dix-huit mois parce qu'il ne communiquait pas avec le logiciel des disponibilités, et un portail des formations, doublé par la plateforme de formation achetée ensuite par un autre groupement. Pour la sécurité, nous avons une charte d'usage, signée par chaque agent à son arrivée ; il n'y a jamais eu d'analyse des risques, et personne n'est désigné pour s'en occuper. »

**Commandante Maëlle TOURNEVAL, cheffe du centre de traitement de l'alerte** : « Les quatre agents du soutien assurent une astreinte jour et nuit, et un incident est toujours pris en charge. Nous notons chaque incident dans un cahier, au centre : l'heure, ce qui s'est passé, ce qui a été fait. Mais personne ne relit le cahier, et les mêmes pannes reviennent. Les mises à jour que nous envoient les éditeurs des autres logiciels, celui des disponibilités par exemple, sont installées le soir par l'agent d'astreinte, sans test et sans retour arrière prévu ; deux fois en 2026, les disponibilités ne sont plus arrivées pendant une heure après une mise à jour. »

**Lieutenant-colonel Hervé DOMBRESSAC, chef du groupement du volontariat** : « Combien avons-nous de volontaires ? Mon groupement en compte 3 900 ; le logiciel des disponibilités affiche 4 300 comptes actifs, parce que ceux qui partent ne sont pas toujours retirés ; les tableurs des groupements territoriaux en totalisent 3 800. Chaque groupement tient ses tableurs, et personne n'est chargé de dire quelle donnée fait foi. »

**Un chef de centre du Haut-Aurande, volontaire** : « Ni les groupements territoriaux ni les volontaires ne sont jamais consultés sur les outils. Nous avons découvert les tablettes le jour de leur livraison. Pourtant, ce sont nous qui déclarons nos disponibilités, nous qui partons en intervention et nous qui remplissons les états d'heures. »

### ANNEXE 1.4 – Grille de capacité des processus (d'après COBIT 2019, résumée par le groupement « Pilotage et systèmes d'information »)

| Niveau | Intitulé | Ce qui caractérise le processus |
|---|---|---|
| 0 | Incomplet | le processus n'est pas mis en œuvre, ou il n'atteint pas son objectif ; au mieux, quelques activités isolées existent |
| 1 | Initial | le processus atteint en partie son objectif, par des activités menées au cas par cas, de façon intuitive, qui dépendent des personnes |
| 2 | Géré | le processus atteint son objectif par un ensemble d'activités de base complet, planifié et suivi, avec des responsables identifiés |
| 3 | Défini | le processus suit une démarche écrite, commune à toute l'organisation, appuyée sur des règles et des outils partagés |
| 4 | Quantitativement géré | la performance du processus est mesurée par des indicateurs, et il est piloté à partir de ces mesures |
| 5 | Optimisé | le processus est amélioré en continu, à partir de ses mesures et des évolutions des besoins |

Un processus n'atteint un niveau que si les exigences des niveaux inférieurs sont satisfaites.

### ANNEXE 1.5 – Le processus actuel des volontaires (description du lieutenant-colonel Hervé DOMBRESSAC, chef du groupement du volontariat, avril 2027)

**Déclarer sa disponibilité.** Chaque volontaire indique les périodes où il peut partir en intervention depuis son domicile ou son travail, ou être de garde au centre. Il le fait par SMS, selon un code à respecter (45 % des déclarations), sur le site web du logiciel des disponibilités (35 %), ou par téléphone à son chef de centre, qui ressaisit la déclaration (20 %). Un SMS mal formé est rejeté sans que le volontaire le sache toujours.

**Être alerté et partir.** Le logiciel des disponibilités transmet les disponibilités au logiciel de traitement de l'alerte par un fichier, toutes les trente minutes. Le centre de traitement de l'alerte voit donc des disponibilités parfois périmées : un volontaire parti au travail sans mettre à jour sa disponibilité, ou une déclaration faite dans la dernière demi-heure. Selon les opérateurs, environ un appel sur dix adressé à un volontaire tombe sur quelqu'un qui n'est plus disponible, et il faut alerter un autre centre. Au départ de l'engin, le chef d'agrès note l'équipage sur une feuille de départ, conservée au centre ; le chef de centre ressaisit ensuite l'équipage dans le logiciel de traitement de l'alerte.

**Être indemnisé.** Chaque mois, les chefs de centre recopient dans le logiciel des indemnités les heures d'intervention, qu'ils relèvent dans le logiciel de traitement de l'alerte, et les heures de garde, qu'ils tirent de leurs plannings tenus sur tableur. Les chefs des 48 centres armés par des volontaires seulement, eux-mêmes volontaires, y consacrent chacun environ dix heures par mois, le soir. Le groupement des finances contrôle les états : un sur cinq est corrigé, souvent après un échange avec le centre. Le logiciel des indemnités transmet ensuite un fichier mensuel au logiciel de paie. Les indemnités sont versées en moyenne deux mois après le mois de l'intervention. En 2026, le groupement du volontariat a reçu 1 200 réclamations pour des heures oubliées ou erronées.

**Ce que disent les volontaires.** Lors des réunions de 2026, le délai de paiement et les déclarations « qui ne passent pas » sont les deux premiers motifs d'insatisfaction cités par les volontaires, avec le temps passé par les chefs de centre « à faire de l'administratif plutôt que de la formation ».

### ANNEXE 1.6 – Le projet VIGIE (note de cadrage validée par le comité de direction, avril 2027)

**Objectif.** Remplacer, avant la fin du support de son éditeur le 31/12/2028, le logiciel de gestion des disponibilités par VIGIE, une application mobile pour les volontaires, reliée au logiciel de traitement de l'alerte et au logiciel des indemnités. Le volontaire déclare sa disponibilité en quelques gestes ; le centre de traitement de l'alerte la voit aussitôt ; l'équipage est enregistré une seule fois, au départ ; les heures d'intervention et de garde alimentent le logiciel des indemnités sans ressaisie.

**Trois lots.**

| Lot | Contenu | Éléments connus |
|---|---|---|
| Lot 1 – Application mobile des volontaires | déclaration et modification des disponibilités, planning des gardes, enregistrement de l'équipage au départ, consultation de ses heures | les besoins sont mal connus : les volontaires veulent « plus simple », sans que l'on sache encore quelles fonctions ils utiliseront ; les écrans sont à essayer avec eux au fur et à mesure |
| Lot 2 – Interface avec le logiciel de traitement de l'alerte | envoi des disponibilités et des équipages enregistrés au départ ; réception des heures d'intervention | exigences de fiabilité très fortes ; l'éditeur du logiciel de traitement de l'alerte impose, avant toute mise en service d'une interface, huit semaines de tests sur sa plateforme de test, puis deux semaines d'essais au centre de traitement de l'alerte |
| Lot 3 – Interface avec le logiciel des indemnités | envoi des heures d'intervention et de garde validées | les règles de calcul des indemnités ne changent pas ; le format d'échange du logiciel des indemnités est connu et stable |

**Acteurs.** Le directeur départemental, commanditaire ; le groupement du volontariat ; le centre de traitement de l'alerte ; le service des systèmes d'information et de communication ; le groupement des finances ; l'éditeur de VIGIE, retenu en mars 2027 (aucune procédure de choix de l'éditeur n'est à organiser) ; un panel de 40 volontaires des quatre groupements territoriaux, dont des chefs de centre.

**Contraintes.**
- Les 12 informaticiens du service des systèmes d'information et de communication consacrent la moitié de leur temps à la maintenance courante ; de septembre à décembre 2027, le renouvellement des 300 tablettes embarquées mobilisera la plupart des autres. Deux informaticiens au plus pourront travailler sur VIGIE jusqu'à la fin de 2027, quatre ensuite.
- Les volontaires du panel ont un métier : ils ne sont disponibles que le soir et le week-end.
- Du 15 juin au 15 septembre, pendant la saison des feux de forêt, le centre de traitement de l'alerte fonctionne en effectif renforcé, et le directeur interdit toute mise en service touchant le traitement de l'alerte.
- L'éditeur de VIGIE propose douze mois de projet à partir de juillet 2027.

**Exigences de qualité énoncées par les acteurs.**
- Centre de traitement de l'alerte : « Une disponibilité déclarée doit être affichée chez nous en moins d'une minute. »
- Panel des volontaires : « Dans le Haut-Aurande, le réseau passe mal : l'application doit fonctionner même quand on capte mal. »
- Groupement des finances : « Zéro écart entre les heures d'intervention et de garde enregistrées et les indemnités payées. »

Aucun chiffrage du projet n'est demandé.

### ANNEXE 1.7 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Gouvernance du système d'information | COBIT 2019, ISACA (évolution de COBIT 5) | référentiel de gouvernance et de management de l'information et des technologies, ni norme ni logiciel ; 40 objectifs de gouvernance et de management répartis en cinq domaines (EDM, APO, BAI, DSS, MEA) ; capacité des processus évaluée de 0 à 5 (annexe 1.4) |
| Méthode agile | The Scrum Guide, Ken Schwaber et Jeff Sutherland, novembre 2020 | cadre agile de référence : Product Owner, Scrum Master, Developers ; Sprint d'un mois au plus |
| Management de la qualité | ISO 9001 — Systèmes de management de la qualité — Exigences, édition 2026 (6e édition), qui remplace l'édition de 2015 | norme d'application volontaire ; sert de cadre de principe au plan qualité d'un projet |

### Travail à faire

Le projet d'établissement « Val-d'Aurande Secours 2031 » compte sur le système d'information pour fidéliser les volontaires, tenir les délais d'arrivée des secours et garantir la continuité du traitement de l'alerte. Or personne ne suit les technologies qui transforment l'alerte, la gouvernance du système d'information reste informelle, et le remplacement du logiciel des disponibilités doit aboutir avant la fin de 2028. Le colonel hors classe GRANVOISE vous demande d'organiser une veille technologique et d'éclairer deux technologies, d'évaluer la capacité des processus de gouvernance du système d'information et d'associer les parties prenantes à cette gouvernance, d'analyser le processus des volontaires et le processus cible, puis de préparer la conduite du projet VIGIE : méthode, organisation, planification et plan qualité. Vous mobiliserez pour cela les annexes 1.1 à 1.7 ainsi que vos connaissances professionnelles.

**1.1 – La veille technologique et deux technologies de l'alerte (3 points)**

a) Après avoir défini la veille technologique, proposez l'organisation d'une veille technologique pour le SDIS : ce qu'elle surveille, ses sources, ses acteurs, la diffusion de ses résultats et la manière dont elle conduit à une décision.

b) Analysez, à partir de l'annexe 1.2, l'effet de chacune des deux technologies sur le modèle opérationnel du SDIS (prise de l'appel, décision d'engagement, charge des opérateurs) et leur contribution aux objectifs du projet d'établissement. Recommandez une suite pour chacune.

**1.2 – La capacité des processus et les parties prenantes de la gouvernance du système d'information (3 points)**

a) Après avoir défini un modèle de maturité et un modèle de capacité, et indiqué leurs usages, positionnez les quatre processus décrits à l'annexe 1.3 (gestion des projets, gestion des incidents et des changements, gestion de la sécurité, gestion des données) sur la grille de l'annexe 1.4, en justifiant chaque niveau par un constat.

b) Fixez pour chacun de ces quatre processus un niveau cible à deux ans, en justifiant votre ambition, et une action prioritaire.

c) Proposez deux instances ou deux mesures qui associent le conseil d'administration, les groupements territoriaux et les volontaires à la gouvernance du système d'information.

**1.3 – Le processus des volontaires et sa rationalisation (2,5 points)**

a) Après avoir défini un processus métier, représentez, à partir de l'annexe 1.5, le processus actuel « déclaration de disponibilité → engagement → indemnisation » sous la forme de votre choix (acteurs, étapes, outils, ressaisies). Relevez ensuite trois dysfonctionnements, avec leurs effets.

b) Décrivez le processus cible avec VIGIE, puis montrez comment l'architecture du système d'information le rationalise : échanges automatiques entre les trois logiciels, donnée saisie une seule fois. Indiquez enfin deux conditions de réussite de cette architecture. Il n'est demandé ni cartographie applicative complète, ni modèle des données.

**1.4 – La méthode et l'organisation du projet VIGIE (3 points)**

a) Après avoir présenté le cycle en V, les méthodes agiles et l'approche hybride, choisissez et justifiez, à partir de l'annexe 1.6, une méthode pour chacun des trois lots du projet VIGIE.

b) Proposez l'organisation du projet : maîtrise d'ouvrage, maîtrise d'œuvre, comité de pilotage et place du panel de volontaires. Présentez dans un tableau la répartition des responsabilités de cinq acteurs de l'annexe 1.6 sur quatre activités du projet de votre choix.

**1.5 – La planification et le plan qualité du projet VIGIE (2,5 points)**

a) Identifiez, à partir de l'annexe 1.6, trois tensions de planification du projet et proposez, pour chacune, un arbitrage entre les ressources, les délais, les coûts et la qualité. Il n'est demandé ni diagramme de Gantt, ni calcul de chemin critique, ni chiffrage.

b) Après avoir défini le plan qualité d'un projet, présentez son contenu pour VIGIE. Proposez deux indicateurs de qualité tirés des exigences de l'annexe 1.6, chacun avec sa formule, sa source, sa fréquence, sa cible et son axe, puis indiquez comment le respect de ces exigences sera contrôlé avant et après la mise en service.
