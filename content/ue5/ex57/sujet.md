# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 57

**DOSSIER 3 – MAÎTRISER LES COÛTS, LA FIABILITÉ ET LA SÉCURITÉ DU SYSTÈME D'INFORMATION DE CONDUITE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 19, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en juin 2027. ESTRAVENT Énergies SA est un producteur indépendant d'électricité renouvelable, fondé en 2004 à Reims par trois ingénieurs. Société anonyme à conseil d'administration, elle est cotée sur Euronext Growth depuis 2015 ; ses fondateurs en détiennent 34 % du capital, un fonds d'infrastructure 21 %, et 45 % sont détenus par le public. Elle développe, construit et exploite en France 64 parcs éoliens terrestres (420 éoliennes, 1 000 MW) et 38 centrales solaires au sol (400 MW), portés chacun par une société de projet qu'elle détient à 100 %. En 2026, ses installations ont produit 2,7 TWh, et son chiffre d'affaires a atteint 250 M€. ESTRAVENT emploie 520 salariés, au siège de Reims, au centre de conduite qui surveille les installations jour et nuit, et dans quatre agences régionales. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « ESTRAVENT 2031 », adopté en mars 2027 par le conseil d'administration, fixe quatre objectifs : porter la puissance installée à 2 500 MW, en renouvelant les éoliennes des parcs les plus anciens et en développant de nouveaux projets ; vendre 40 % de la production à des industriels par des contrats d'achat direct, contre 10 % en 2026, à mesure que les parcs sortent de leurs contrats de vente à prix garanti ; porter la disponibilité des éoliennes de 95 % à 97 %, en assurant elle-même la maintenance des machines sorties des contrats des constructeurs ; maîtriser les données et la sécurité de ses installations. Le système d'information s'est construit en deux mondes séparés : l'informatique de gestion, confiée à la DSI, et l'informatique de conduite des installations, gérée par la direction de l'exploitation avec les constructeurs et une entreprise de services du numérique.

Vous êtes directeur (directrice) de la performance et des systèmes d'information d'ESTRAVENT depuis janvier 2027 ; vous dirigez la DSI et le contrôle de gestion et vous rendez compte au directeur financier. La présidente-directrice générale, Mme Sidonie VARLAMBERT, vous demande trois travaux : préparer l'évolution de la stratégie et de l'organisation du SI, la renégociation d'un contrat et la transmission des savoirs (dossier 1) ; organiser et exploiter les données des installations, et en garder la maîtrise (dossier 2) ; maîtriser les coûts, la fiabilité et la sécurité du SI de conduite (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation d'ESTRAVENT Énergies et chiffres clés

ESTRAVENT Énergies SA développe, construit et exploite des parcs éoliens terrestres et des centrales solaires au sol en France, dans quatre régions : Grand Est, Hauts-de-France, Centre-Val de Loire et Occitanie. Son siège est à Reims (Marne). Chaque parc éolien et chaque centrale solaire est porté par une société de projet, détenue à 100 % par ESTRAVENT : les 102 sociétés de projet n'ont aucun salarié, et ESTRAVENT leur facture ses services. Les communes où sont implantés les parcs sont fictives. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**L'actionnariat et la gouvernance**

| Donnée | Valeur |
|---|---|
| Forme et cotation | société anonyme à conseil d'administration, cotée sur Euronext Growth depuis 2015 |
| Capital | fondateurs 34 % ; fonds d'infrastructure 21 % ; public 45 % |
| Conseil d'administration | 9 membres ; un comité d'audit ; présidente-directrice générale : Mme Sidonie VARLAMBERT, cofondatrice |
| Plan stratégique | « ESTRAVENT 2031 », adopté en mars 2027 par le conseil d'administration |

**Les installations et l'activité en 2026**

| Donnée | Valeur |
|---|---|
| Parcs éoliens terrestres | 64 parcs, 420 éoliennes, 1 000 MW ; les éoliennes viennent de trois constructeurs, désignés dans ce cas par les lettres A, B et C |
| Centrales solaires au sol | 38 centrales, 400 MW |
| Puissance installée | 1 400 MW ; objectif du plan : 2 500 MW en 2031 |
| Production | 2,7 TWh, dont éolien 2,2 TWh et solaire 0,5 TWh |
| Disponibilité moyenne des éoliennes | 95 % ; objectif du plan : 97 % |
| Chiffre d'affaires | 250 M€ |
| Projets en développement | 70 projets ; sept à neuf ans s'écoulent entre la recherche d'un site et la mise en service |

**La vente de l'électricité en 2026**

| Mode de vente | Part de l'électricité vendue |
|---|---|
| Contrats de vente à prix garanti de quinze ans | 70 % |
| Vente sur le marché par un agrégateur | 20 % |
| Trois contrats d'achat direct de dix ans avec des industriels, signés en 2025 et 2026 | 10 % ; objectif du plan : 40 % en 2031 |

18 parcs éoliens sortent de leur contrat de vente à prix garanti entre 2026 et 2029.

**L'effectif (520 salariés)**

| Direction | Effectif |
|---|---|
| Exploitation | 210 : centre de conduite 40, techniciens de maintenance 150, ingénieurs de la performance 20 ; la cellule supervision (8 personnes) fait partie de la direction de l'exploitation |
| Développement | 130, dans quatre agences régionales |
| Construction | 60 |
| Énergie (vente de l'électricité) | 25 |
| Fonctions support | 95, dont 22 à la DSI et 6 au contrôle de gestion |

**Le système d'information en quelques lignes**

En 2026, les dépenses du système d'information ont atteint 9 M€ : 5 M€ pour la DSI et 4 M€ pour l'informatique de conduite, dont 1,5 M€ pour le contrat de l'entreprise de services du numérique (ESN).

- **Informatique de conduite**, gérée par la direction de l'exploitation : dans chaque parc éolien, un système de supervision et d'acquisition de données fourni par le constructeur des éoliennes (trois constructeurs, trois systèmes), dont les données remontent aussi dans le nuage de chaque constructeur ; une **plateforme de supervision** commune au centre de conduite, développée en 2016 pour ESTRAVENT et maintenue par une ESN au forfait jusqu'au 31/12/2027 ; des systèmes de supervision propres aux centrales solaires.
- **Informatique de gestion**, confiée à la DSI : progiciel de gestion intégré (comptabilité, achats, immobilisations, facturation) ; paie ; logiciel de gestion de la maintenance en mode SaaS ; outil de prévision de la production fourni par un prestataire ; gestion des contrats de vente et facturation de l'électricité (tableurs et module du progiciel) ; système d'information géographique et gestion électronique des documents des projets ; gestion des relations avec les propriétaires des terrains et les communes ; messagerie et bureautique en ligne.
- Les données de production sont stockées dans une base de données relationnelle au siège.

**Organigramme simplifié (juin 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil d'administration, avec un comité d'audit | présidente : Mme Sidonie VARLAMBERT ; président du comité d'audit : M. Bernard ESCOLIÈRE, administrateur indépendant |
| Conseil d'administration | présidence-direction générale | Mme Sidonie VARLAMBERT |
| Présidente-directrice générale | direction financière | M. Thibault ORLANCOURT, directeur financier |
| | direction de l'exploitation : centre de conduite, cellule supervision, maintenance, ingénieurs de la performance | Mme Gaëlle MONTREVIAU, directrice de l'exploitation ; responsable du centre de conduite : M. Yannick FERRASSOT ; responsable de la cellule supervision : Mme Nadège QUILLEBRAND ; responsable des ingénieurs de la performance : M. Fabien LACROUZE |
| | direction de l'énergie (vente de l'électricité) | M. Arnaud VELDRIMONT, directeur de l'énergie |
| | direction du développement, avec quatre agences régionales | Mme Isaure TRÉMOLLAC, directrice du développement |
| | direction de la construction | M. Jérôme CALVIGNAC, directeur de la construction |
| | déléguée à la protection des données | Mme Léa VINCHEREAU |
| Directeur financier | direction de la performance et des systèmes d'information : DSI et contrôle de gestion | vous ; responsable de la DSI : M. Olivier SAUVERNAY ; responsable du contrôle de gestion : Mme Agnès DORMEVAL |

### ANNEXE 3.1 – Les coûts du système d'information et leur refacturation (note de Mme Agnès DORMEVAL, responsable du contrôle de gestion, mai 2027, et extrait du reporting annuel)

**A. Les dépenses du système d'information en 2026, par ensemble de services.** Je les ai reconstituées pour la première fois, à partir des factures et des temps déclarés.

| Ensemble de services | Contenu | Dépenses 2026 (k€) |
|---|---|---|
| Informatique de gestion (DSI) | progiciel de gestion intégré, paie, logiciel de gestion de la maintenance, prévision de la production, gestion des contrats de vente et facturation de l'électricité, système d'information géographique et gestion électronique des documents des projets, relations avec les propriétaires et les communes, messagerie et bureautique, postes de travail, réseau du siège et des agences ; 22 personnes | 5 000 |
| *dont services rendus aux sociétés de projet* | *facturation de l'électricité, gestion des contrats de vente et tenue de la comptabilité de chaque société de projet* | *1 500* |
| Supervision des éoliennes | plateforme de supervision et ses serveurs, contrat de l'ESN (1 500 k€), liens avec les systèmes des trois constructeurs, part de la cellule supervision | 2 600 |
| Supervision des centrales solaires | systèmes de supervision propres aux centrales, part de la cellule supervision | 400 |
| Liaisons de télécommunication des sites | liaisons des 64 parcs et des 38 centrales avec le centre de conduite | 800 |
| Centre de conduite | postes et équipements du centre de conduite | 200 |
| **Total** | | **9 000** |

La plateforme de supervision et le contrat de l'ESN servent pour l'essentiel aux éoliennes : chaque centrale solaire n'y remonte qu'une alarme générale, et elle est suivie par son propre système.

**B. La refacturation actuelle.** Depuis 2015, la totalité des dépenses du système d'information est refacturée chaque année aux 102 sociétés de projet, au prorata de leur chiffre d'affaires.
- En 2026, les 38 sociétés de projet des centrales solaires ont réalisé 50 M€ de chiffre d'affaires, et les 64 sociétés de projet des parcs éoliens 200 M€. Les centrales solaires ont donc payé 20 % des dépenses du système d'information, y compris de la supervision des éoliennes, qu'elles n'utilisent pas.
- Un parc éolien du Centre-Val de Loire, arrêté quatre mois en 2026 après la casse d'un multiplicateur, a vu son chiffre d'affaires passer de 4 M€ en 2025 à 2 M€ en 2026, et sa part refacturée baisser de moitié. Ses alarmes sont passées de 2 000 à 6 000, et le centre de conduite l'a suivi de près pendant tout l'arrêt.
- Deux parcs voisins de même puissance paient des montants différents selon que leur électricité est vendue à prix garanti ou sur le marché.
- Les dépenses des outils des projets en développement (système d'information géographique, gestion électronique des documents des projets) sont refacturées aux sociétés de projet des installations en service.

Les règles comptables, fiscales et juridiques de la refacturation ne sont pas à traiter.

**C. Les inducteurs disponibles (2026)**

| Inducteur | Parcs éoliens | Centrales solaires | Source |
|---|---|---|---|
| Puissance installée | 1 000 MW | 400 MW | inventaire technique des installations |
| Sites raccordés au centre de conduite | 64 parcs | 38 centrales | inventaire des liaisons |
| Machines supervisées | 420 éoliennes | 2 000 onduleurs | systèmes de supervision |
| Alarmes reçues par le centre de conduite | 180 000 | 20 000 | plateforme de supervision et systèmes des centrales |
| Utilisateurs des applications | 520 salariés d'ESTRAVENT, toutes directions confondues ; les sociétés de projet n'ont aucun salarié | | annuaire de la DSI |

**D. Ce que nos chiffres ne montrent pas**
- Les 150 techniciens de maintenance passent chacun environ trois heures par semaine à exporter des données des portails des constructeurs et des systèmes des centrales, puis à les recopier dans des tableurs pour préparer leurs interventions.
- Chaque matin, deux opérateurs du centre de conduite passent deux heures à recopier dans un tableur les arrêts de la nuit, pour le point quotidien de la direction de l'exploitation. Une trentaine de tableurs de ce genre circulent dans l'exploitation ; personne n'en tient la liste.
- En 2026, la direction de l'exploitation a acheté sur ses propres frais généraux des abonnements en ligne, des logiciels et des boîtiers de connexion pour environ 350 k€ ; ces achats ne figurent pas dans les dépenses du système d'information.

**E. Extrait du reporting annuel du système d'information (présenté au comité de direction en février 2027)**

| Nature des dépenses | 2026 (k€) |
|---|---|
| Personnel | 2 700 |
| Prestations externes | 2 300 |
| Licences et abonnements | 1 900 |
| Matériel | 1 100 |
| Télécommunications | 1 000 |
| **Total des dépenses du système d'information** | **9 000** |

Ce reporting est établi une fois par an, pour la préparation du budget. Il ne présente ni l'année précédente, ni objectif, ni la répartition entre l'informatique de gestion et l'informatique de conduite, ni aucun indicateur.

**F. Deux avis**

**M. Thibault ORLANCOURT, directeur financier** : « La clé du chiffre d'affaires a un mérite : elle est simple, et personne ne la discute. »

**Mme Gaëlle MONTREVIAU, directrice de l'exploitation** : « Si l'on refacture au nombre d'alarmes, nos parcs les plus anciens paieront pour les défauts de leurs machines. »

### ANNEXE 3.2 – Du comptage au chiffre d'affaires (note de M. Thibault ORLANCOURT, directeur financier, mai 2027)

**A. La chaîne de facturation des contrats d'achat direct.** En 2026, nos trois contrats d'achat direct ont porté sur 10 % de l'électricité vendue et sur environ 20 M€ de chiffre d'affaires ; le plan « ESTRAVENT 2031 » en suppose une quinzaine en 2031. Chaque contrat est adossé à deux à quatre parcs éoliens, et chaque facture mensuelle porte sur l'énergie livrée heure par heure.

1. **Comptage.** Au point de livraison de chaque parc, un compteur mesure l'énergie injectée sur le réseau. Le gestionnaire du réseau de distribution le relève et met à disposition chaque mois, sur son portail, un fichier par parc, avec la valeur de chaque heure : environ 720 valeurs par mois.
2. **Supervision.** La plateforme de supervision enregistre de son côté la production de chaque éolienne. Pour un même parc, elle dépasse normalement le comptage d'environ 2 %, du fait des pertes dans les câbles du parc.
3. **Calcul.** Chaque contrat a son tableur. Une chargée de facturation de la direction de l'énergie y copie les fichiers de comptage des parcs du contrat et calcule l'énergie livrée à l'industriel, heure par heure. Quand le fichier d'un parc manque ou n'est pas reconnu, elle reprend les données de la supervision. Elle a sous les yeux la production enregistrée par la supervision, mais aucun seuil d'écart n'est fixé, et rien n'oblige à expliquer un écart avant d'envoyer la facture.
4. **Facturation.** Le montant de la facture est saisi à la main dans le module de facturation du progiciel de gestion intégré, qui émet la facture ; le détail horaire est joint en PDF.
5. **Chiffre d'affaires.** Le chiffre d'affaires de chaque semestre, publié par ESTRAVENT, est établi à partir des factures du progiciel. La direction financière ne rapproche ni les volumes facturés des volumes comptés, ni le chiffre d'affaires des contrats de leurs tableurs.

**B. Ce qui s'est passé en 2026**
- En avril 2026, le fichier de comptage de mars d'un parc a été copié deux fois dans le tableur d'un contrat : l'énergie de ce parc a été comptée deux fois, et la facture a été majorée d'environ 300 k€. L'industriel l'a contestée ; elle a été refaite.
- De juin à août 2026, pour un parc d'un autre contrat, la production enregistrée par la supervision a dépassé de 8 % le comptage, sans que personne en cherche la cause. Le gestionnaire du réseau avait remplacé le compteur ; son fichier portait un nouveau numéro, que le tableur ne reconnaissait pas, et les volumes de ce parc ont été repris de la supervision pendant trois mois. L'industriel a contesté la facture d'août ; les trois factures ont été refaites.
- Dans le tableur du troisième contrat, une formule erronée, recopiée d'une ligne à l'autre, a omis pendant six mois une partie des heures livrées : l'industriel a été sous-facturé d'environ 150 k€. L'erreur n'a été découverte qu'en février 2027, après la publication du chiffre d'affaires de 2026.
- Les tableurs sont corrigés directement, sans historique. Les factures refaites ont remplacé les premières dans le dossier de chaque contrat, sans mention du motif. Pour une facture de 2026, nous ne savons plus dire quelles données ont servi, ni qui les a modifiées.
- Deux chargées de facturation préparent les factures horaires. L'une d'elles a construit les trois tableurs, et elle seule sait les modifier ou en créer un pour un nouveau contrat. Chacune prépare, vérifie et envoie ses propres factures ; personne ne relit ses calculs. Les tableurs sont rangés dans un dossier partagé auquel accèdent les 25 salariés de la direction de l'énergie.

**C. Les échelles retenues par le comité de direction**

| Niveau | Probabilité | Impact |
|---|---|---|
| 1 – faible | jamais constaté et peu plausible | erreur corrigée avant l'envoi de la facture, sans effet pour l'industriel |
| 2 – moyen | plausible, sans avoir été constaté chez ESTRAVENT | facture retardée, ou chiffre d'affaires impossible à justifier sans recherches longues, sans facture fausse envoyée |
| 3 – fort | constaté chez ESTRAVENT en 2026, ou certain en l'état | facture fausse envoyée à un industriel, ou chiffre d'affaires publié inexact |

Quand plusieurs niveaux conviennent, on retient le plus élevé. Le comité de direction traite en priorité les risques dont la probabilité et l'impact sont tous deux de niveau 3. Ni règle comptable, ni écriture, ni contrôle des comptes ne sont à traiter.

### ANNEXE 3.3 – Les accès à distance aux installations (constats de Mme Nadège QUILLEBRAND, responsable de la cellule supervision, et de M. Olivier SAUVERNAY, responsable de la DSI, mai 2027)

**A. Qui se connecte, et comment**
- Huit entreprises extérieures se connectent à distance aux installations : les constructeurs A, B et C, aux systèmes de supervision de leurs parcs, pour dépanner et régler leurs machines ; quatre sous-traitants de maintenance, aux systèmes des centrales solaires et des postes électriques des parcs ; l'ESN qui maintient la plateforme de supervision, à cette plateforme.
- Chacune utilise son propre outil de connexion à distance, soit huit outils différents. 110 boîtiers de connexion ont été installés dans les parcs et les centrales au fil des mises en service ; 20 boîtiers ne sont rattachés à aucune entreprise connue.
- Les huit entreprises disposent de 60 comptes d'accès, dont 50 sont partagés par tous les techniciens d'une même entreprise. La plupart des mots de passe n'ont jamais changé depuis la mise en service des installations.
- Les accès sont ouverts en permanence, jour et nuit ; le centre de conduite n'est pas prévenu des connexions.
- D'après les entreprises extérieures, il y a eu environ 9 000 connexions à distance en 2026. ESTRAVENT n'en conserve aucune trace : seuls les constructeurs gardent les journaux de leurs systèmes.
- Les postes du centre de conduite servent aussi à la messagerie et à la navigation sur internet. Ils sont reliés au réseau de bureautique du siège, comme les serveurs de la plateforme de supervision.
- Plusieurs systèmes de supervision des parcs les plus anciens fonctionnent sur des systèmes d'exploitation qui ne reçoivent plus de correctifs de sécurité ; les constructeurs n'en autorisent aucune modification.

**B. Deux événements**
- En septembre 2026, le compte partagé d'un sous-traitant de maintenance, dont le contrat avait pris fin en juin et qui n'intervenait que sur les postes électriques, a servi à se connecter un dimanche, à 3 heures, au système de supervision d'un parc du constructeur C, pendant 40 minutes. Aucune commande n'a été envoyée aux éoliennes. C'est le constructeur C qui l'a signalé, trois semaines plus tard ; on ne sait toujours pas qui s'est connecté.
- En février 2027, selon l'écho qu'en a donné la presse, un autre producteur d'électricité a vu plusieurs de ses parcs arrêtés à distance pendant deux jours ; l'attaque serait passée par l'accès d'un prestataire de maintenance.

**C. L'organisation de la sécurité aujourd'hui**
- La politique de sécurité de la DSI, approuvée par le comité de direction en 2022, ne couvre que l'informatique de gestion ; M. SAUVERNAY en a la charge. L'informatique de conduite n'a ni politique de sécurité, ni analyse des risques.
- Personne n'est chargé de la sécurité de l'informatique de conduite : la cellule supervision en traite les incidents « quand ils se présentent ».
- Les contrats des constructeurs, des sous-traitants et de l'ESN ne disent rien de la sécurité des accès à distance.
- Le centre de conduite fonctionne jour et nuit ; c'est lui qui décide d'arrêter ou de redémarrer une installation.

**D. Ce qu'en disent les responsables**

**Mme Gaëlle MONTREVIAU, directrice de l'exploitation** : « Si nous fermons les accès, les constructeurs ne pourront plus dépanner la nuit, et la disponibilité baissera. Or le plan nous demande 97 %. »

**M. Yannick FERRASSOT, responsable du centre de conduite** : « Mes opérateurs voient tout ce qui se passe sur les machines, mais pas qui s'y connecte. »

Aucun paramétrage d'équipement ni aucun essai technique n'est attendu ; aucune procédure de choix d'un fournisseur n'est à organiser, et aucune analyse juridique des contrats n'est demandée.

### ANNEXE 3.4 – La demande du comité d'audit (courriel de M. Bernard ESCOLIÈRE, président du comité d'audit, mai 2027)

« Le comité d'audit a examiné, le 12 mai, l'incident de septembre 2026 et l'attaque subie par un autre producteur. Il a pris acte de votre intention de mettre en place, d'ici la fin de 2027, de nouvelles règles pour les accès à distance des entreprises extérieures.

Le comité souhaite qu'un auditeur des systèmes d'information externe en vérifie l'application six mois après leur mise en place, et lui en rende compte. Avant de lancer cette mission, il voudrait savoir sur quels critères l'auditeur jugera ces accès, sur quels éléments il s'appuiera, et à quoi il faudra veiller.

Je rappelle nos contraintes : nos installations produisent jour et nuit, et aucune ne doit être arrêtée pour l'audit ; les systèmes des constructeurs ne peuvent pas être modifiés ; huit entreprises extérieures et 102 sites, dans quatre régions, sont concernés ; les journaux des systèmes des parcs sont chez les constructeurs. Le choix de l'auditeur viendra ensuite. »

Ni la démarche détaillée de l'audit, ni son calendrier, ni aucun essai technique ne sont demandés.

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Sécurité de l'information | ISO/IEC 27001:2022 | norme d'exigences d'un système de management de la sécurité de l'information, fondé sur l'appréciation et le traitement des risques, dans une logique d'amélioration continue ; son annexe A compte 93 mesures en quatre thèmes (organisationnelles, liées aux personnes, physiques, technologiques) |
| Gestion des risques | ISO/IEC 27005:2022 | lignes directrices de gestion des risques liés à la sécurité de l'information : établir le contexte, identifier, analyser, évaluer puis traiter les risques, et les surveiller ; quatre options de traitement : réduire le risque, l'accepter, l'éviter ou le transférer ; elle ne prescrit pas de méthode particulière |
| Bonnes pratiques | Guide d'hygiène informatique de l'ANSSI, version de 2017 | guide de 42 mesures de sécurité, en niveau standard et renforcé, qui portent notamment sur l'authentification, les mises à jour, le cloisonnement des réseaux, les appareils nomades et les sauvegardes |
| Architecture de confiance | Le modèle Zero Trust, avis de l'ANSSI (2021) | modèle d'architecture, et non un produit : aucune confiance n'est accordée d'office selon la place sur le réseau ; chaque accès est authentifié, autorisé et vérifié selon le contexte ; démarche progressive, qui ne remplace pas la défense en profondeur |
| Gouvernance et audit du système d'information | COBIT 2019 (ISACA) | cadre de gouvernance et de management de l'information et des technologies, ni norme ni logiciel ; 40 objectifs de gouvernance et de management en cinq domaines ; il peut servir de référentiel à un audit du système d'information |

### Travail à faire

Les dépenses du système d'information sont refacturées aux sociétés de projet selon une clé qui ne dit rien de leur usage, et le reporting n'en dit guère plus. La facturation des contrats d'achat direct, appelés à se multiplier, repose sur des tableurs qui ont produit trois erreurs en 2026. Huit entreprises extérieures se connectent jour et nuit aux installations avec des comptes partagés, et le compte d'un sous-traitant parti a servi en 2026. Mme VARLAMBERT vous demande de revoir le pilotage et la refacturation des coûts du système d'information, de fiabiliser la chaîne qui va du comptage au chiffre d'affaires, de fonder la sécurité de l'informatique de conduite et des accès à distance, et de répondre au comité d'audit. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – Les coûts du système d'information et leur refacturation aux sociétés de projet (3,5 points)**

a) Après avoir présenté les fondamentaux du contrôle de gestion appliqué au système d'information (centre de coûts ou centre de services, refacturation interne, inducteurs), critiquez par trois arguments tirés de l'annexe 3.1 la refacturation actuelle des dépenses du système d'information aux sociétés de projet. Proposez ensuite une répartition fondée sur des inducteurs : associez un inducteur, ou l'absence de refacturation, à chacun des ensembles de services de l'annexe 3.1 A, et justifiez le choix de deux de ces inducteurs. Aucun calcul de répartition n'est demandé.

b) Relevez, à partir de l'annexe 3.1 D, trois coûts cachés du système d'information de conduite. Pour chacun, expliquez pourquoi il échappe au suivi actuel et comment le mesurer.

c) Proposez trois améliorations du reporting annuel des coûts du système d'information (annexe 3.1 E), portant respectivement sur les comparaisons, les objectifs et la revue périodique. Deux d'entre elles s'appuient sur un indicateur, précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

**3.2 – La fiabilité de la chaîne du comptage au chiffre d'affaires (3,5 points)**

a) Après avoir présenté la typologie des risques liés aux systèmes d'information, suivez la chaîne « comptage → facturation → chiffre d'affaires » de l'annexe 3.2 étape par étape et retenez-y quatre risques, chacun formulé comme un événement redouté et rattaché à l'étape où il naît. Indiquez la catégorie de chacun dans cette typologie, puis cotez leur probabilité et leur impact selon les échelles de l'annexe 3.2 C.

b) Après avoir défini la fiabilisation d'un système d'information de gestion, choisissez, pour les deux risques les plus graves, un traitement parmi les options de l'ISO/IEC 27005 (annexe 3.5), puis proposez, pour chacun d'eux, deux contrôles qui fiabilisent les données de facturation et le chiffre d'affaires publié. Pour chaque contrôle, précisez sa nature (préventive ou détective, manuelle ou automatisée), son responsable et ce qu'il garantit. Indiquez enfin comment rendre les corrections traçables et réduire la dépendance envers une seule personne. Aucune règle comptable ni aucune écriture n'est attendue.

**3.3 – La sécurité de l'informatique de conduite et des accès à distance (3,5 points)**

a) Après avoir défini une politique de sécurité du système d'information fondée sur l'analyse des risques, présentez, à partir de l'annexe 3.3, quatre principes de la politique de sécurité de l'informatique de conduite d'ESTRAVENT, en montrant en quoi ils se distinguent de ceux de l'informatique de gestion. Précisez ensuite le rôle que doivent y tenir la présidente-directrice générale, vous-même, la directrice de l'exploitation, la responsable de la cellule supervision, le responsable du centre de conduite et les entreprises extérieures.

b) Après avoir présenté le modèle Zero Trust, proposez quatre mesures d'architecture de confiance pour les accès à distance des entreprises extérieures, portant respectivement sur l'authentification et les comptes, le point d'accès aux installations, la séparation entre l'informatique de conduite et la bureautique, l'ouverture et la traçabilité des accès. Pour chacune, précisez le constat de l'annexe 3.3 auquel elle répond et le risque qu'elle traite. Répondez enfin à la crainte de Mme MONTREVIAU. Aucun paramétrage d'équipement ni aucun essai technique n'est attendu.

**3.4 – La réponse au comité d'audit (2,5 points)**

a) Après avoir défini un critère d'appréciation et un élément probant en audit des systèmes d'information, présentez à M. ESCOLIÈRE trois critères sur lesquels l'auditeur jugera les accès à distance — la sécurité, la fiabilité des traces et la conformité à la politique de sécurité — en indiquant pour chacun ce qui sera attendu et un élément probant que l'auditeur demandera.

b) Présentez trois points de vigilance propres à l'audit des accès à distance d'installations qui produisent jour et nuit, en indiquant pour chacun la manière d'y répondre. La démarche détaillée de l'audit et son calendrier ne sont pas demandés.
