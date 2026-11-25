# DSCG UE 5 — Management des systèmes d'information — Sujet d'entraînement complet n° 18

Durée de l'épreuve : 3 heures – Coefficient : 1

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026.

**Document et matériel autorisés** : Aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Le sujet se présente sous la forme de 3 dossiers indépendants :

| Dossier | Intitulé | Points | Durée conseillée |
|---|---|---:|---|
| DOSSIER 1 | PRÉPARER LA GOUVERNANCE DU SYSTÈME D'INFORMATION ET LA CONDUITE DU PROJET VIGIE | 14 points | 1 h 03 |
| DOSSIER 2 | ORGANISER ET EXPLOITER LES DONNÉES DES INTERVENTIONS, EN MAÎTRISER LA CONSERVATION | 13 points | 59 min |
| DOSSIER 3 | TIRER LES CONCLUSIONS D'UN AUDIT, MAÎTRISER LES RISQUES ET LA SÉCURITÉ DU SYSTÈME D'INFORMATION OPÉRATIONNEL ET EN RÉDUIRE L'EMPREINTE | 13 points | 58 min |

Le sujet comporte 17 annexes, dont 1 communes aux dossiers.

| Dossier | Annexe | Intitulé |
|---|---|---|
| Tous les dossiers | Annexe 1.1 | Présentation du SDIS du Val-d'Aurande et chiffres clés |
| DOSSIER 1 | Annexe 1.2 | Deux technologies à l'étude (note de la commandante Maëlle TOURNEVAL, cheffe du centre de traitement de l'alerte, avril 2027) |
|  | Annexe 1.3 | La gouvernance du système d'information vue par les acteurs (témoignages recueillis en avril 2027) |
|  | Annexe 1.4 | Grille de capacité des processus (d'après COBIT 2019, résumée par le groupement « Pilotage et systèmes d'information ») |
|  | Annexe 1.5 | Le processus actuel des volontaires (description du lieutenant-colonel Hervé DOMBRESSAC, chef du groupement du volontariat, avril 2027) |
|  | Annexe 1.6 | Le projet VIGIE (note de cadrage validée par le comité de direction, avril 2027) |
|  | Annexe 1.7 | Repères (au 31/12/2026) |
| DOSSIER 2 | Annexe 2.1 | Les interventions, les engins et les équipages (note de M. Rémi TRÉVIGNAN, chef de l'observatoire de l'activité, avril 2027) |
|  | Annexe 2.2 | La sollicitation opérationnelle de 2022 à 2026 (tableaux de l'observatoire de l'activité, mars 2027) |
|  | Annexe 2.3 | Les enregistrements des appels et les comptes rendus de secours (note de Mme Coralie FAVERJON, déléguée à la protection des données, et du Dr Agathe MÉRIGNOLLE, médecin-chef, avril 2027) |
|  | Annexe 2.4 | La proposition d'un fournisseur d'équipements de protection individuelle (note de M. Pascal LAUZERAC, chef du groupement technique et logistique, avril 2027) |
|  | Annexe 2.5 | Repères (au 31/12/2026) |
| DOSSIER 3 | Annexe 3.1 | Les constats de l'audit de la base des points d'eau d'incendie (rapport de M. Gaël VORMESSAC, auditeur des systèmes d'information externe, avril 2027) |
|  | Annexe 3.2 | Le logiciel de traitement de l'alerte et son éditeur (note de Mme Solène VARANGEOT, cheffe du service des systèmes d'information et de communication, avril 2027) |
|  | Annexe 3.3 | Les tablettes embarquées et la transmission des comptes rendus de secours (constats de Mme Solène VARANGEOT et de Mme Coralie FAVERJON, déléguée à la protection des données, avril 2027) |
|  | Annexe 3.4 | Les salles informatiques et la proposition du département (note de M. Pascal LAUZERAC, chef du groupement technique et logistique, avril 2027) |
|  | Annexe 3.5 | Repères (au 31/12/2026) |

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

---

## DOSSIER 1 – PRÉPARER LA GOUVERNANCE DU SYSTÈME D'INFORMATION ET LA CONDUITE DU PROJET VIGIE (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES INTERVENTIONS, EN MAÎTRISER LA CONSERVATION (13 points)

### ANNEXE 2.1 – Les interventions, les engins et les équipages (note de M. Rémi TRÉVIGNAN, chef de l'observatoire de l'activité, avril 2027)

**A. Le fonctionnement actuel**

À chaque appel qui donne lieu à un départ de secours, l'opérateur du centre de traitement de l'alerte crée une intervention dans le logiciel de traitement de l'alerte : il en choisit la nature, localise le lieu et engage les engins que le logiciel lui propose. L'équipage de chaque engin est enregistré au départ du centre d'incendie et de secours. Pendant l'intervention, le chef d'agrès, qui commande l'engin, signale sur la tablette de l'engin son arrivée sur les lieux en appuyant sur un bouton ; les heures de départ et d'arrivée sont transmises au logiciel. Chaque mois, l'observatoire extrait les interventions du logiciel dans un tableur pour produire les chiffres de l'activité. En 2026, les 50 000 interventions ont donné lieu à 70 000 départs d'engins.

**B. Les problèmes de qualité relevés sur les données de 2026**

- **Heures d'arrivée manquantes** : sur 70 000 départs d'engins, 7 000, un sur dix, n'ont pas d'heure d'arrivée sur les lieux : le chef d'agrès a oublié d'appuyer sur le bouton de la tablette, souvent parce qu'il était occupé par la victime.
- **Natures « autre »** : l'opérateur peut choisir la nature « autre » quand la situation est confuse au moment de l'appel ; il l'a fait pour 2 500 interventions, une sur vingt. En janvier 2027, l'observatoire les a reclassées à la main, d'après les comptes rendus, dans l'une des quatre natures ; ce travail a pris 15 jours.
- **Équipages incomplets** : quand un sapeur-pompier remplace un autre au dernier moment, l'équipage enregistré au départ n'est pas corrigé ; le chef de centre le ressaisit ensuite dans un tableur. C'est arrivé pour 3 500 départs, un sur vingt.
- **Communes** : quand la localisation automatique échoue, l'opérateur saisit la commune en texte libre ; c'est le cas pour 4 000 interventions. La base compte ainsi 1 100 libellés différents (« Montcerneau », « MONTCERNEAU », « Mtcerneau », « Montcerneau Sud »…) pour les 480 communes du département.

**C. Les règles de gestion des interventions, des engins et des équipages**

- **RG1** – Une intervention est identifiée par un numéro attribué par le logiciel de traitement de l'alerte ; on connaît la date et l'heure de l'appel et l'adresse du lieu.
- **RG2** – Une intervention relève d'une seule nature. Une nature est identifiée par un code et porte un libellé (secours d'urgence aux personnes, accident de la circulation, incendie, opération diverse) ; une nature peut ne compter encore aucune intervention.
- **RG3** – Une intervention a lieu dans une seule commune. Une commune est identifiée par un code ; on connaît son nom et sa population. Une commune peut n'avoir connu aucune intervention.
- **RG4** – Une commune relève d'un seul centre de premier appel, qui envoie les premiers secours ; un centre est le centre de premier appel d'une ou de plusieurs communes. Un centre est identifié par un code ; on connaît son nom, son type (mixte ou volontaire) et son groupement territorial.
- **RG5** – Un engin est identifié par un numéro ; on connaît son type (ambulance de secours, fourgon d'incendie, camion-citerne, véhicule de secours routier…) et sa date de mise en service. Un engin appartient à un seul centre ; un centre possède un ou plusieurs engins.
- **RG6** – Une intervention mobilise un ou plusieurs engins ; un engin peut n'avoir encore été engagé sur aucune intervention. Pour chaque engin engagé sur une intervention, on connaît l'heure de départ et l'heure d'arrivée sur les lieux.
- **RG7** – Un agent est identifié par un matricule ; on connaît son nom, son prénom et son statut (professionnel, volontaire, ou professionnel et volontaire). Un agent est rattaché à un ou plusieurs centres ; un centre compte un ou plusieurs agents.
- **RG8** – Sur une intervention, un agent arme un engin dans un seul rôle : chef d'agrès, conducteur ou équipier. Sur une même intervention, un agent peut armer successivement plusieurs engins (par exemple lors d'une relève), dans un rôle pour chacun. Une intervention compte au moins un agent armant un engin ; un agent ou un engin peut n'avoir encore participé à aucune intervention.

### ANNEXE 2.2 – La sollicitation opérationnelle de 2022 à 2026 (tableaux de l'observatoire de l'activité, mars 2027)

**A. Interventions par nature et par an (chiffres publiés, en nombre d'interventions)**

| Nature | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Secours d'urgence aux personnes | 31 000 | 32 000 | 35 000 | 36 000 | 39 000 |
| Accidents de la circulation | 3 500 | 3 500 | 3 500 | 3 400 | 3 500 |
| Incendies | 3 500 | 3 000 | 3 000 | 3 100 | 3 500 |
| Opérations diverses | 5 000 | 5 500 | 3 500 | 3 500 | 4 000 |
| **Ensemble** | **43 000** | **44 000** | **45 000** | **46 000** | **50 000** |

**B. Quelques séries complémentaires**

| Série | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Carences (comprises dans les secours d'urgence aux personnes) | 3 000 | 3 500 | 4 500 | 5 000 | 6 000 |
| Interventions pour des personnes de 80 ans et plus, à leur domicile (toutes natures) | 10 000 | 10 500 | 11 000 | 11 500 | 12 500 |
| Part des secours d'urgence aux personnes entre 18 heures et 8 heures | 40 % | 41 % | 42 % | 44 % | 45 % |
| Interventions par mois, en moyenne, en juillet et août | 4 200 | 4 300 | 4 400 | 4 500 | 5 000 |
| Interventions par mois, en moyenne, en janvier et février | 3 300 | 3 400 | 3 500 | 3 600 | 3 800 |

Conventions : une **carence** est une intervention de secours d'urgence aux personnes demandée par le centre de régulation médicale du SAMU, sans caractère d'urgence, parce qu'aucun autre moyen (ambulance privée, médecin de garde) n'était disponible. L'âge de la victime est celui noté sur le compte rendu de secours. Les séries se recoupent : une carence peut concerner une personne âgée à domicile.

**C. Ce que l'on sait de ces chiffres**

- **Reclassement de 2024** : au 1er janvier 2024, le SDIS a revu la liste des natures d'intervention. Les relevages de personnes tombées à leur domicile sans blessure apparente, environ 2 000 par an, sont passés des opérations diverses aux secours d'urgence aux personnes. Les chiffres de 2022 et de 2023 n'ont pas été recalculés.
- **Interface défaillante en 2025** : en mars et avril 2025, l'interface entre le logiciel de traitement de l'alerte et la base de l'observatoire a mal fonctionné ; environ 1 000 interventions de ces deux mois, surtout des secours d'urgence aux personnes, n'ont pas été transmises et manquent dans les chiffres de 2025.
- **Touristes** : le Haut-Aurande accueille jusqu'à 100 000 touristes en juillet et en août. Les chiffres rapportés aux habitants sont calculés sur la population résidente, 640 000 habitants.
- **Épisodes de chaleur** : en juillet 2026, deux épisodes de forte chaleur ont porté les interventions à 1 500 par semaine, contre 1 100 environ pour une semaine d'été ordinaire.

**D. L'affirmation de M. Thibaut PRUNEVAUX, administrateur, maire d'une commune du Haut-Aurande, au conseil d'administration du 30/03/2027**

« Si les interventions augmentent, c'est parce que la population vieillit. Il suffit de recruter des volontaires. »

### ANNEXE 2.3 – Les enregistrements des appels et les comptes rendus de secours (note de Mme Coralie FAVERJON, déléguée à la protection des données, et du Dr Agathe MÉRIGNOLLE, médecin-chef, avril 2027)

**A. Les enregistrements des appels**

Tous les appels reçus au centre de traitement de l'alerte, 150 000 en 2026, sont enregistrés par l'enregistreur des appels, installé en 2017 ; il en conserve environ 1,5 million, sans aucune suppression. Un enregistrement est retrouvé par la date, l'heure et le poste de l'opérateur : il n'est pas relié au numéro de l'intervention. Pour répondre à des demandes, des enregistrements sont copiés sur des clés USB ou envoyés par messagerie.

En septembre 2026, la justice a demandé l'enregistrement d'un appel de novembre 2024 relatif à un accident de la circulation. Après trois jours de recherche, le centre de traitement de l'alerte ne l'a pas retrouvé : l'horloge de l'enregistreur avait été décalée après une panne, et l'appel ne pouvait pas être rapproché de l'intervention.

**B. Les comptes rendus de secours**

Depuis la fin de 2021, le chef d'agrès rédige sur la tablette de l'engin un compte rendu de secours pour chaque victime : identité, état de la victime, gestes réalisés. Le compte rendu est envoyé au centre de régulation médicale du SAMU et à l'hôpital qui accueille la victime, puis stocké sur un serveur du siège. Le serveur en conserve plus de 200 000, à raison d'environ 40 000 par an ; il est occupé à 85 %. Aucun compte rendu n'a jamais été trié ni supprimé. Pour préparer les retours d'expérience ou répondre à des demandes, des chefs de centre et des médecins en exportent des copies en PDF dans leur messagerie : un contrôle de dix messageries, en mars 2027, en a trouvé 3 000.

Le Dr MÉRIGNOLLE rappelle que les comptes rendus contiennent des données de santé ; un compte rendu peut être demandé plusieurs années après l'intervention, notamment en cas de litige.

**C. Les demandes de copies en 2026**

| Demandeur | Nombre de demandes |
|---|---|
| Avocats | 150 |
| Assureurs | 150 |
| Familles des victimes | 80 |
| Justice | 20 |
| **Ensemble** | **400** |

Chaque demande est traitée par celui qui la reçoit (centre, centre de traitement de l'alerte, médecin-chef), sans registre ; le délai moyen de réponse est de deux mois.

**D. Les durées de conservation fixées par le SDIS**

Par une décision du 15/03/2027, prise après l'avis de la déléguée à la protection des données et du médecin-chef, le directeur départemental a fixé les durées suivantes, qui ne sont pas à discuter :
- **enregistrements des appels** : deux ans après l'appel, puis destruction, sauf si une demande portant sur l'intervention est en cours ;
- **comptes rendus de secours** : consultation courante pendant deux ans après l'intervention, puis archivage jusqu'à vingt ans après l'intervention, puis destruction.

Aucune règle n'a encore été mise en œuvre.

### ANNEXE 2.4 – La proposition d'un fournisseur d'équipements de protection individuelle (note de M. Pascal LAUZERAC, chef du groupement technique et logistique, avril 2027)

**A. Le suivi actuel des tenues de feu**

Le SDIS dispose de 8 000 tenues de feu (veste et surpantalon), deux par sapeur-pompier. Le fabricant garantit leur protection pendant dix ans ou 50 lavages, au premier des deux termes atteint. Chaque tenue suit le même parcours : livraison par le fournisseur, attribution à un sapeur-pompier par le magasin du groupement, lavage par le blanchisseur après chaque incendie, contrôle annuel par le magasin, réparation par le fournisseur, réforme. Les six magasiniers enregistrent ces événements à la main dans le logiciel de gestion du parc, à partir des bons du fournisseur et du blanchisseur.

Constats de l'inventaire de 2026 : 400 tenues, une sur vingt, n'ont pas été localisées ; une tenue sur quatre n'a aucun historique de lavage ; le blanchisseur LAVORDÈNE a facturé 30 000 lavages, alors que le logiciel de gestion du parc n'en a enregistré que 24 000 ; 1 000 contrôles annuels sont en retard. Après un accident survenu lors d'un incendie en 2026, il a fallu une semaine pour reconstituer l'historique de la tenue de l'agent blessé.

**B. La proposition de PROTÉVANCE**

PROTÉVANCE, fournisseur des tenues du SDIS et de deux SDIS voisins de la région, propose de coudre une puce dans chaque tenue. À chaque événement de sa vie, la puce est lue par un lecteur, chez le fournisseur, au magasin ou chez le blanchisseur, et l'événement est inscrit dans une chaîne de blocs partagée entre cinq acteurs : les trois SDIS, PROTÉVANCE et LAVORDÈNE, qui lave aussi les tenues des deux SDIS voisins. Chaque acteur disposerait d'un nœud ; PROTÉVANCE propose d'héberger les nœuds des SDIS qui le souhaitent. Selon PROTÉVANCE, les événements sont validés par les participants identifiés, sans minage, et ne peuvent plus être modifiés une fois inscrits ; aucune monnaie ni aucun jeton n'est utilisé. L'événement « attribution » enregistrerait le matricule du sapeur-pompier.

Les deux SDIS voisins n'ont pas encore pris position.

**C. Les coûts pour le SDIS du Val-d'Aurande et une autre solution**

| Poste | Chaîne de blocs de PROTÉVANCE | Base de données partagée |
|---|---|---|
| Lecteurs de puces (une fois) | 20 k€ | 20 k€ |
| Puces pour les tenues existantes (une fois) | 5 € par tenue | 5 € par tenue |
| Abonnement annuel | 30 k€ | 10 k€ |

La **base de données partagée** serait hébergée et administrée par un prestataire de services informatiques, retenu par les trois SDIS ; les cinq acteurs y enregistreraient les mêmes événements, lus par les mêmes puces, et le prestataire en tiendrait le journal des modifications. Aucun chiffrage du projet au-delà de ce tableau n'est attendu, et aucune procédure de choix du fournisseur n'est à organiser.

### ANNEXE 2.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Données personnelles | règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | les données à caractère personnel sont collectées pour des finalités déterminées, limitées à ce qui est nécessaire (minimisation), conservées pendant une durée limitée, fixée selon la finalité (limitation de la conservation) et protégées contre la perte et l'accès non autorisé (intégrité et confidentialité) ; les données de santé sont des données sensibles, protégées de façon renforcée ; le registre des activités de traitement indique, pour chaque traitement, les délais prévus pour l'effacement des données ; le SDIS a désigné une déléguée à la protection des données, Mme Coralie FAVERJON ; aucune analyse juridique n'est attendue |
| Archivage électronique | NF Z42-013 (AFNOR) et son équivalent international ISO 14641 | normes d'application volontaire qui fixent les spécifications de conception et d'exploitation d'un système d'archivage électronique, pour assurer la conservation et l'intégrité des documents : intégrité, pérennité de la lecture, traçabilité des opérations ; elles servent de référence pour conserver des documents qui pourront servir de preuve |
| Gestion des documents d'activité | ISO 15489-1 — Information et documentation : gestion des documents d'activité (concepts et principes), édition de 2016 | norme qui pose les concepts et les principes de la gestion des documents d'activité : les documents sont gérés selon des règles écrites, de leur création à leur sort final (destruction ou conservation) |
| Chaînes de blocs | ISO 22739:2024 — Chaînes de blocs et technologies de registres distribués — Vocabulaire | norme de vocabulaire (bloc, nœud, consensus, registre distribué…), ni norme d'exigences ni solution |

### Travail à faire

Le SDIS produit chaque année 50 000 interventions, 150 000 enregistrements d'appels et 40 000 comptes rendus de secours, mais ses données ne lui permettent ni de mesurer sûrement sa sollicitation, ni de retrouver un enregistrement demandé par la justice. Le colonel hors classe GRANVOISE vous demande d'organiser les données des interventions, d'en tirer une analyse fiable de la sollicitation opérationnelle à présenter au conseil d'administration, de maîtriser la conservation des enregistrements et des comptes rendus, et de donner votre avis sur la proposition de PROTÉVANCE. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.5 ainsi que vos connaissances professionnelles.

**2.1 – Les données des interventions, des engins et des équipages (3,5 points)**

a) À partir des règles de gestion de l'annexe 2.1 C, établissez le modèle conceptuel des données des interventions, des engins et des équipages, puis traduisez-le en modèle logique, en énonçant les règles de passage que vous appliquez. Aucune requête n'est attendue.

b) Après avoir défini le dictionnaire des données, rédigez-en trois entrées pour des données de votre modèle. Proposez ensuite trois règles de qualité qui traitent chacune l'un des problèmes de l'annexe 2.1 B, en précisant la dimension de la qualité des données concernée.

**2.2 – L'analyse de la sollicitation opérationnelle (4,5 points)**

a) Après avoir défini la chaîne de valeur des données, décrivez la chaîne de traitement qui produira l'analyse de la sollicitation opérationnelle, en montrant, à chaque étape, une limite des chiffres de l'annexe 2.2 ou un problème de qualité de l'annexe 2.1 B qu'elle doit traiter.

b) Formulez trois constats argumentés tirés de l'annexe 2.2, puis appréciez l'affirmation de M. PRUNEVAUX. Aucun calcul statistique n'est attendu.

c) Après avoir défini l'analyse prédictive, indiquez ce qu'elle apporterait au SDIS, en précisant deux conditions de sa réussite et deux de ses limites. Proposez enfin la représentation visuelle qui montrerait le mieux au conseil d'administration la sollicitation opérationnelle par commune, et justifiez-la.

**2.3 – La conservation des enregistrements et des comptes rendus de secours (3 points)**

a) Décrivez le cycle de vie des enregistrements des appels et des comptes rendus de secours, de leur création à leur destruction, en fixant une règle à chaque étape.

b) Après avoir distingué le stockage et l'archivage électronique, indiquez ce que le RGPD et les normes d'archivage électronique imposent ou apportent au SDIS pour ces données, puis proposez trois mesures. Aucune analyse juridique n'est attendue.

**2.4 – La proposition de PROTÉVANCE (2 points)**

a) Après avoir défini la chaîne de blocs, expliquez le fonctionnement de la chaîne de blocs de consortium proposée par PROTÉVANCE et précisez le type d'application dont il s'agit.

b) Appréciez la valeur ajoutée, les coûts et les limites de cette proposition au regard de la base de données partagée de l'annexe 2.4 C, puis concluez.

---

## DOSSIER 3 – TIRER LES CONCLUSIONS D'UN AUDIT, MAÎTRISER LES RISQUES ET LA SÉCURITÉ DU SYSTÈME D'INFORMATION OPÉRATIONNEL ET EN RÉDUIRE L'EMPREINTE (13 points)

### ANNEXE 3.1 – Les constats de l'audit de la base des points d'eau d'incendie (rapport de M. Gaël VORMESSAC, auditeur des systèmes d'information externe, avril 2027)

**A. La mission et la base**

À la demande du directeur départemental, M. VORMESSAC a audité, de janvier à mars 2027, la base des points d'eau d'incendie et sa transmission au logiciel de traitement de l'alerte. La mission est terminée : la réunion de clôture s'est tenue le 15/04/2027.

La base recense 14 000 points d'eau : 10 000 poteaux et bouches d'incendie raccordés aux réseaux d'eau, 3 000 citernes et réserves, 1 000 points d'aspiration aménagés sur des étangs ou des rivières. Elle est tenue, avec le système d'information géographique, par la cellule cartographie du groupement des opérations, qui compte trois agents. Chaque mois, un fichier extrait de la base est chargé dans le logiciel de traitement de l'alerte, dont la carte indique aux opérateurs et aux équipages les points d'eau proches du sinistre et leur état (disponible ou indisponible).

L'organisation fixée par le SDIS, qui n'est pas à discuter, est la suivante : chaque point d'eau est contrôlé au moins une fois tous les deux ans ; les communes et les gestionnaires des réseaux d'eau font les contrôles et en transmettent les résultats au SDIS ; toute indisponibilité (poteau hors service, citerne vide, travaux) est signalée au SDIS dès qu'elle est connue. Aucune règle de droit n'est à connaître.

**B. Les constats (notes brutes, dans l'ordre où ils ont été relevés)**

- 3 500 points d'eau, un sur quatre, n'ont aucun contrôle enregistré depuis plus de deux ans ; la plupart sont des citernes et des points d'aspiration du Haut-Aurande.
- En 2026, le SDIS a reçu 6 000 résultats de contrôles, envoyés par courriel par les 480 communes du département et par les 6 gestionnaires des réseaux d'eau, dans des tableurs de formats différents (colonnes, codes des points, libellés des états). Les trois agents de la cellule cartographie les ressaisissent un par un. Au 31/03/2027, 1 500 de ces résultats, un sur quatre, n'avaient pas encore été saisis.
- En 2026, 800 indisponibilités ont été signalées, par téléphone, par courriel ou au cours d'une réunion, à des interlocuteurs différents : le centre de traitement de l'alerte, un centre d'incendie et de secours ou la cellule cartographie. Il s'est écoulé en moyenne 12 jours entre le signalement et la saisie dans la base ; s'y ajoute l'attente du chargement mensuel suivant dans le logiciel de traitement de l'alerte.
- Le 01/03/2027, l'auditeur a comparé la base et la carte du logiciel de traitement de l'alerte : 600 points d'eau diffèrent (état, position ou caractéristiques), dont 150 points indisponibles dans la base qui figurent comme disponibles sur la carte. Le fichier mensuel est chargé à la main par un agent du soutien du centre de traitement de l'alerte, sans contrôle du nombre de points chargés. Le chargement de septembre 2026 a échoué, et personne ne s'en est aperçu avant celui d'octobre.
- Un relevé sur le terrain de 200 points d'eau du Haut-Aurande a trouvé 20 points, un sur dix, placés sur la carte à plus de 100 mètres de leur position réelle.
- Les 1 200 comptes de la bureautique ont le droit de modifier la base : tout agent peut changer l'état, la position ou le débit d'un point d'eau.
- La base ne conserve que la dernière valeur de chaque donnée : on ne peut savoir ni qui a modifié un point d'eau, ni quand, ni quelle était la valeur précédente.
- La base est sauvegardée chaque nuit sur un disque de la salle informatique du siège, où se trouve aussi son serveur. Aucune restauration n'a jamais été essayée.
- Le 12/08/2026, lors de l'incendie d'un hangar agricole dans le Haut-Aurande, le premier engin s'est rendu au poteau d'incendie que la carte indiquait comme le plus proche. Ce poteau était hors service depuis trois semaines ; la commune l'avait signalé par courriel à un centre d'incendie et de secours. L'engin a dû rejoindre une réserve située à 2 km : l'alimentation en eau a été retardée d'environ 15 minutes, et le hangar a été détruit. Il n'y a pas eu de victime.

**C. Les réactions recueillies à la réunion de clôture**

**Lieutenant-colonel Bertrand OSSELIN, chef du groupement des opérations** : « Mes chefs d'agrès connaissent leur secteur : la carte n'est qu'une aide. Et la cellule cartographie n'a que trois agents. »

**Mme Solène VARANGEOT, cheffe du service des systèmes d'information et de communication** : « Une liaison automatique entre la base et le logiciel de l'alerte passe par l'éditeur de ce logiciel, et son calendrier est déjà chargé. »

**D. La demande du directeur départemental**

« Je veux une note de synthèse d'une page, que je présenterai au comité de direction du 7 juin 2027. Elle doit me dire ce qui est grave, ce que l'on fait, qui le fait et pour quand. »

### ANNEXE 3.2 – Le logiciel de traitement de l'alerte et son éditeur (note de Mme Solène VARANGEOT, cheffe du service des systèmes d'information et de communication, avril 2027)

**A. Le logiciel et son éditeur**

- Le logiciel de traitement de l'alerte, installé en 2012 et mis à niveau en 2019, reçoit les appels, localise l'appelant, propose les engins à engager et suit les interventions. Il échange des données avec l'enregistreur des appels, le logiciel des disponibilités des volontaires, la base des points d'eau et les tablettes des engins.
- Son éditeur est une société de 40 salariés, qui équipe une quinzaine de SDIS ; le nôtre est l'un de ses trois principaux clients. Il a annoncé que la version que nous utilisons ne serait plus maintenue après le 31/12/2029. Sa nouvelle version, proposée en ligne, était annoncée pour 2028 ; elle l'est désormais « à partir de 2029 », et aucun SDIS ne l'utilise encore.
- Chez l'éditeur, deux développeurs seulement connaissent nos interfaces, et l'un d'eux part à la retraite en 2028. Aucune documentation de ces interfaces ne nous a été remise.
- Le contrat de maintenance, renouvelé chaque année, ne prévoit ni la remise du code source si l'éditeur cessait son activité, ni d'aide à la sortie. L'éditeur intervient à distance sur nos serveurs par un accès ouvert en permanence, avec un compte commun à tous ses techniciens.

**B. Les serveurs et les pannes de 2026**

- Le logiciel fonctionne sur quatre serveurs dans la salle informatique du siège et sur deux serveurs dans la salle de secours de Montcerneau-Sud. Ces six serveurs ont été installés en 2017. Leur système d'exploitation ne reçoit plus de correctifs de sécurité depuis 2025 ; selon l'éditeur, notre version du logiciel ne fonctionne pas avec un système plus récent.
- Ces serveurs sont reliés au même réseau informatique que les postes de bureautique du siège et que les tablettes des engins (annexe 3.3).
- En juillet 2026, pendant un épisode de forte chaleur, la climatisation de la salle du siège est tombée en panne et les serveurs se sont arrêtés. La bascule sur la salle de secours a pris 45 minutes, pendant lesquelles une trentaine d'appels ont été traités sur papier ; la salle du siège n'est revenue en service qu'après 2 h 30.
- En novembre 2026, un correctif de l'éditeur, installé le même soir dans les deux salles, a bloqué pendant 2 heures la proposition des engins à engager. Les opérateurs ont choisi eux-mêmes les engins, à partir de tableaux imprimés. Un seul des deux développeurs a pu être joint.

**C. L'analyse demandée et les échelles du comité de direction**

Aucune analyse des risques du logiciel n'a été formalisée. Le directeur départemental veut présenter les principaux risques et leur traitement au conseil d'administration du 1er juillet 2027. Les échelles retenues par le comité de direction sont les suivantes :

| Niveau | Probabilité | Impact |
|---|---|---|
| 1 – faible | jamais constaté et peu plausible | gêne interne, sans effet sur le traitement des appels ni sur l'engagement des secours |
| 2 – moyen | constaté dans un autre SDIS, ou plausible sans être facile à provoquer | traitement de l'alerte dégradé (bascule sur la salle de secours, procédure sur papier, engins choisis à la main), sans arrêt de la réception des appels |
| 3 – fort | constaté au SDIS en 2026, certain à une date connue, ou facile à provoquer en l'état | réception des appels ou engagement des secours arrêtés dans les deux salles, ou impossibles à rétablir rapidement |

Quand plusieurs niveaux conviennent, on retient le plus élevé. Le comité de direction traite en priorité les risques dont la probabilité et l'impact sont tous deux de niveau 3. Aucune procédure de choix d'un nouvel éditeur n'est à organiser, et aucun chiffrage n'est demandé.

### ANNEXE 3.3 – Les tablettes embarquées et la transmission des comptes rendus de secours (constats de Mme Solène VARANGEOT et de Mme Coralie FAVERJON, déléguée à la protection des données, avril 2027)

**A. Les tablettes et les comptes rendus**

- Les 300 tablettes, installées en 2021, équipent les ambulances et les premiers engins de départ des 60 centres. Chacune est partagée par tous les équipages de son engin. Elle s'ouvre avec un code à quatre chiffres, le même pour toutes les tablettes d'un centre, inchangé depuis 2021 et connu des agents partis comme des nouveaux. L'application de comptes rendus de secours ne demande aucun identifiant : le chef d'agrès tape son nom au bas du compte rendu.
- Le chef d'agrès rédige sur la tablette un compte rendu par victime : identité, état de la victime, gestes réalisés ; environ 40 000 sont rédigés chaque année. La tablette l'envoie, en pièce jointe d'un courriel non chiffré, au centre de régulation médicale du SAMU et au service des urgences de l'hôpital qui accueille la victime, parmi les six hôpitaux du département. Une copie reste dans la tablette, qui n'est jamais vidée.
- 120 des 300 tablettes ont un système qui ne reçoit plus de mises à jour de sécurité. Le service des systèmes d'information et de communication ne peut ni localiser une tablette, ni la bloquer, ni l'effacer à distance.
- Les tablettes se connectent par le réseau mobile au réseau informatique du siège, le même que celui des postes de bureautique et des serveurs du logiciel de traitement de l'alerte.
- Les 300 tablettes seront remplacées de septembre à décembre 2027. Les besoins des nouvelles tablettes sont en cours de rédaction ; aucune procédure de choix du fournisseur n'est à organiser.

**B. Les pertes, les vols et deux incidents**

- 6 tablettes ont été perdues ou volées en 2025, 10 en 2026 : 8 oubliées sur les lieux d'une intervention ou perdues, 2 volées dans un engin.
- En octobre 2026, une tablette a été volée dans une ambulance pendant une intervention. Elle contenait plus de 1 000 comptes rendus de secours. Le centre a porté plainte ; Mme FAVERJON ne l'a appris que trois semaines plus tard, par hasard. Le code des tablettes du centre n'a pas été changé.
- En février 2027, le SDIS d'un département voisin a subi une attaque par rançongiciel. Selon l'écho qu'en a donné la presse, l'attaque, partie d'un courriel piégé ouvert sur un poste de bureautique, a gagné les serveurs de son traitement de l'alerte, arrêté pendant une journée ; ses appels ont été pris par les centres de traitement de l'alerte des départements voisins, dont le nôtre.

**C. Qui fait quoi aujourd'hui**

- Aucune politique de sécurité n'a été approuvée par la direction ; seule existe une charte d'usage, signée par chaque agent à son arrivée.
- Aucun responsable de la sécurité des systèmes d'information n'est désigné : Mme VARANGEOT et l'informaticien d'astreinte traitent les incidents « quand ils remontent ».
- Les chefs de centre communiquent le code des tablettes aux nouveaux arrivants et signalent les pertes « quand ils y pensent ».
- La cheffe du centre de traitement de l'alerte, la commandante Maëlle TOURNEVAL, décide de la bascule sur la salle de secours ; elle n'est pas consultée avant l'installation des correctifs du logiciel.
- L'éditeur du logiciel de traitement de l'alerte installe ses correctifs à distance, à la date qu'il choisit.
- La déléguée à la protection des données n'est informée ni des pertes de tablettes, ni des incidents.

### ANNEXE 3.4 – Les salles informatiques et la proposition du département (note de M. Pascal LAUZERAC, chef du groupement technique et logistique, avril 2027)

**A. Les deux salles du SDIS**

| Donnée | Salle du siège (Montcerneau) | Salle de secours (Montcerneau-Sud) |
|---|---|---|
| Serveurs | 40 : 10 pour le traitement de l'alerte, l'enregistreur des appels et la base des points d'eau ; 30 pour les applications de gestion | 4, pour le traitement de l'alerte et l'enregistreur des appels |
| Climatisation | installée en 2008, tombée en panne en juillet 2026 | installée en 2017 |
| Électricité consommée en 2026 | 400 MWh, dont 200 MWh pour les équipements informatiques | 30 MWh |

- Les 30 serveurs des applications de gestion portent la messagerie et la bureautique, les ressources humaines et la paie, le progiciel financier, la plateforme de formation, la gestion du parc, les indemnités des volontaires et les comptes rendus de secours. Seuls 8 d'entre eux sont virtualisés. Les processeurs des 30 serveurs sont utilisés en moyenne à 10 % de leur capacité.
- Les 900 postes de travail et les serveurs sont renouvelés tous les quatre ans. Les équipements remplacés sont remis à une entreprise de recyclage, qui les détruit. Les 300 tablettes de 2021 seront remplacées à la fin de 2027 (annexe 3.3).
- L'empreinte environnementale du système d'information n'a jamais été mesurée. Le projet d'établissement vise une baisse de 20 % de l'empreinte environnementale de l'établissement d'ici 2031.

**B. La proposition du département (courrier de la direction du numérique du département, mars 2027)**

- Le département a mis en service en 2024, à Montcerneau, une salle informatique où il héberge ses propres applications et celles de plusieurs collectivités. Il propose d'y héberger, à partir de 2028, les 30 serveurs des applications de gestion du SDIS, sous la forme de serveurs virtuels installés sur ses équipements.
- Cette salle est refroidie en grande partie par l'air extérieur. Sa consommation est mesurée en continu, et son indicateur d'efficacité énergétique (énergie totale consommée par la salle / énergie consommée par les équipements informatiques) est de 1,3. La chaleur qu'elle dégage chauffe un collège voisin.
- La salle est exploitée par les agents du département, présents les jours ouvrés de 8 heures à 18 heures ; en dehors de ces heures, aucune astreinte n'est prévue.
- Le traitement de l'alerte, l'enregistreur des appels et la base des points d'eau resteraient dans les salles du SDIS.
- Une convention entre le SDIS et le département fixerait les conditions de l'hébergement ; elle n'est pas rédigée. Aucun chiffrage n'est demandé.

**C. Deux avis**

**Mme Solène VARANGEOT** : « Nous gagnerions de la place et du temps. Mais la messagerie sert aussi à envoyer les comptes rendus de secours, jour et nuit. »

**M. Pascal LAUZERAC** : « Sans les 30 serveurs de gestion, la salle du siège consommerait beaucoup moins. Mais sa climatisation de 2008 resterait à remplacer pour les serveurs de l'alerte. »

Aucune mesure ni aucun calcul de l'empreinte n'est demandé.

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Sécurité de l'information | ISO/IEC 27001:2022 | norme d'exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques, dans une logique d'amélioration continue ; son annexe A compte 93 mesures en quatre thèmes (organisationnelles, liées aux personnes, physiques, technologiques) |
| Gestion des risques | ISO/IEC 27005:2022 | lignes directrices de gestion des risques liés à la sécurité de l'information : établir le contexte, identifier, analyser, évaluer puis traiter les risques, et les surveiller ; quatre options de traitement : réduire le risque, l'accepter, l'éviter ou le transférer (par exemple par une assurance) ; elle ne prescrit pas de méthode particulière |
| Appréciation des risques | EBIOS Risk Manager, version 1.5 (ANSSI, 2024) | méthode française d'appréciation et de traitement des risques numériques, compatible avec l'ISO/IEC 27005, en cinq ateliers : cadrage et socle de sécurité ; sources de risque et objectifs qu'elles visent ; scénarios stratégiques, qui passent par l'écosystème (éditeurs, prestataires, partenaires) ; scénarios opérationnels ; traitement du risque |
| Bonnes pratiques | Guide d'hygiène informatique de l'ANSSI, version de 2017 | guide de 42 mesures de sécurité, en niveau standard et renforcé, qui portent notamment sur l'authentification, les mises à jour, le cloisonnement des réseaux, les appareils nomades et les sauvegardes |
| Architecture de confiance | Le modèle Zero Trust, avis de l'ANSSI (2021) | modèle d'architecture, et non un produit : aucune confiance accordée d'office selon la place sur le réseau ; chaque accès est authentifié, autorisé et vérifié selon le contexte ; démarche progressive, qui ne remplace pas la défense en profondeur |
| Données personnelles | règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | les données personnelles sont protégées par des mesures de sécurité appropriées ; les données de santé sont des données sensibles, protégées de façon renforcée ; toute violation de données personnelles est inscrite dans un registre et, si elle présente un risque pour les personnes, notifiée à l'autorité de contrôle dans les meilleurs délais et, si possible, dans les 72 heures ; les personnes concernées sont informées en cas de risque élevé, sauf si les données étaient rendues incompréhensibles, par exemple par un chiffrement ; un organisme qui traite des données pour le compte du SDIS est un sous-traitant, lié par un contrat qui fixe notamment les mesures de sécurité ; le SDIS a désigné une déléguée à la protection des données, Mme Coralie FAVERJON ; aucune analyse juridique n'est attendue |

### Travail à faire

La base des points d'eau d'incendie n'est plus fiable, et un engin s'est rendu en 2026 à un poteau hors service. Le logiciel de traitement de l'alerte dépend d'un petit éditeur et d'une version qui ne sera plus maintenue après 2029. Les tablettes des engins transportent des données de santé sans protection, sur le réseau du siège. Les salles informatiques consomment beaucoup d'énergie pour des serveurs peu utilisés, alors que le projet d'établissement vise une baisse de 20 % de l'empreinte. Le colonel hors classe GRANVOISE vous demande de tirer les conclusions de l'audit de la base des points d'eau, d'analyser les risques du logiciel de traitement de l'alerte, de sécuriser les tablettes et la transmission des comptes rendus en clarifiant les rôles de chacun, et d'apprécier la proposition du département. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – Les conclusions de l'audit de la base des points d'eau d'incendie (3 points)**

a) Rédigez, à l'attention du colonel hors classe GRANVOISE, la note de synthèse de l'audit de la base des points d'eau (20 lignes au maximum) : une appréciation d'ensemble, puis quatre constats, regroupés à partir des notes brutes de l'annexe 3.1 B et hiérarchisés, chacun assorti du risque, de la recommandation, de son responsable et de son échéance. La note répond à l'objection du lieutenant-colonel OSSELIN. La démarche de l'audit n'est pas demandée.

b) Après avoir défini un critère d'appréciation en audit des systèmes d'information, présentez les trois critères que l'auditeur a mobilisés, la fiabilité des données, la sécurité et l'efficacité du processus : pour chacun, indiquez ce qui est attendu de la base et de sa mise à jour, et rattachez-y deux constats de l'annexe 3.1.

**3.2 – Les risques du logiciel de traitement de l'alerte (3 points)**

a) Identifiez, à partir de l'annexe 3.2, quatre risques liés au logiciel de traitement de l'alerte et à la dépendance envers son éditeur, formulés comme des événements redoutés. Classez-les selon la typologie des risques liés aux systèmes d'information, que vous présenterez brièvement, puis cotez leur probabilité et leur impact selon les échelles de l'annexe 3.2 C.

b) Après avoir comparé en quelques lignes l'approche de l'ISO/IEC 27005 et la méthode EBIOS Risk Manager (annexe 3.5), indiquez celle que le SDIS devrait employer pour l'analyse demandée par le directeur départemental, et justifiez votre choix.

c) Proposez un traitement pour chacun des deux risques les plus graves, en choisissant parmi les options de traitement (réduire, transférer, accepter, éviter) et en justifiant ce choix par leur probabilité et leur impact.

**3.3 – La sécurité des tablettes et la gouvernance du traitement de l'alerte (4 points)**

a) Après avoir défini l'architecture de confiance, proposez, à partir de l'annexe 3.3, quatre mesures de sécurité pour les tablettes et la transmission des comptes rendus de secours, portant respectivement sur l'authentification des équipages, le chiffrement, la séparation des réseaux et l'effacement à distance. Rattachez chaque mesure au risque qu'elle traite, dans le cadre d'une politique de sécurité fondée sur l'analyse des risques, et associez-lui un indicateur d'efficacité précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Aucun réglage d'équipement ni aucun essai technique n'est attendu.

b) Présentez, dans un tableau, les rôles et les responsabilités, dans la gouvernance du traitement de l'alerte, système critique, du directeur départemental, du (de la) chef(fe) du groupement « Pilotage et systèmes d'information », de la cheffe du service des systèmes d'information et de communication, de la cheffe du centre de traitement de l'alerte, des chefs de centre, de l'éditeur du logiciel de traitement de l'alerte et de la déléguée à la protection des données. Proposez la désignation d'un responsable de la sécurité des systèmes d'information et justifiez son positionnement.

**3.4 – Les salles informatiques et la transition numérique responsable (3 points)**

a) Après avoir défini la transition numérique responsable, appréciez la proposition du département de l'annexe 3.4 B : ce qu'elle apporte (mutualisation, efficacité de la salle, chaleur récupérée) et ses limites (dépendance, sécurité et confidentialité, système critique conservé dans les salles du SDIS). Indiquez à quelles conditions vous la recommanderiez.

b) Proposez deux autres bonnes pratiques de Green IT, l'une sur l'allongement de la durée de vie des équipements, l'autre sur leur réemploi, puis deux indicateurs de mesure de l'impact environnemental du système d'information, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Aucun calcul d'empreinte n'est attendu.
