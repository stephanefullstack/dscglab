# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 49

**DOSSIER 1 – PRÉPARER LA STRATÉGIE ET L'ORGANISATION DU SYSTÈME D'INFORMATION (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 17, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en avril 2027. BRÉVALIM est une société d'économie mixte locale, société anonyme à conseil d'administration créée en 1994, qui exploite le marché de gros alimentaire de Brévaline, une métropole de l'ouest de la France. Sur un site de 60 hectares, 240 entreprises (grossistes en fruits et légumes, en produits de la mer, en viandes, en produits laitiers et en fleurs, transformateurs, logisticiens, services) louent à BRÉVALIM des cases dans des pavillons, des bureaux et des cellules d'un entrepôt frigorifique ; chaque nuit, des producteurs de la région vendent leurs récoltes sur le carreau des producteurs, et 2 000 véhicules d'acheteurs professionnels (restaurateurs, commerçants, marchés forains, restauration collective) passent le péage entre 3 heures et 11 heures. Brévaline Métropole détient 60 % du capital, le Département 6 %, la Banque VERDELIN 14 %, la chambre de commerce et d'industrie 8 % et l'Union des grossistes du marché de Brévaline 12 %. En 2026, BRÉVALIM a réalisé un chiffre d'affaires de 28 M€ ; elle emploie 210 salariés. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « Marché de Brévaline 2031 », adopté en janvier 2027 par le conseil d'administration, fixe cinq objectifs : porter de 30 % à 40 % la part des produits régionaux dans les volumes entrés sur le marché ; dématérialiser d'ici 2029 toute la relation avec les entreprises installées et les acheteurs ; valoriser 80 % des déchets du site en 2031, contre 60 % en 2026 ; fiabiliser la facturation et le pilotage, en rendant compte chaque trimestre aux actionnaires ; garantir la sûreté du site et la sécurité des données. Le système d'information s'est construit par morceaux : chaque direction a choisi ses outils, qui ne se parlent pas, et Brévaline Métropole demande désormais des données sur les flux alimentaires du marché.

Vous êtes directeur(rice) général(e) délégué(e) de BRÉVALIM depuis 2025, chargé(e) de l'exploitation du marché et du système d'information. La directrice générale, Mme Héloïse VAUCLERC, vous demande trois travaux : préparer la stratégie et l'organisation du système d'information (dossier 1) ; organiser et exploiter les données des acheteurs et des flux, et revoir le pilotage présenté au conseil d'administration (dossier 2) ; fiabiliser la facturation, maîtriser les accès au site et aux applications, auditer l'attribution du carreau et répondre aux demandes de données de durabilité (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de BRÉVALIM et chiffres clés

BRÉVALIM est une société d'économie mixte locale, société anonyme à conseil d'administration créée en 1994, dont le siège est sur le site du marché de gros de Brévaline, métropole de l'ouest de la France. Elle exploite le marché : elle loue des emplacements aux entreprises installées, organise chaque nuit la vente des producteurs sur le carreau, accueille les acheteurs professionnels au péage et fournit l'énergie, l'eau et le froid du site. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Le modèle, les actionnaires et la gouvernance**

| Donnée | Valeur |
|---|---|
| Entreprises installées | 240 entreprises, titulaires d'un contrat annuel d'emplacement : cases dans les pavillons, bureaux, cellules de l'entrepôt frigorifique |
| Carreau des producteurs | 300 emplacements, attribués chaque nuit par les placiers de BRÉVALIM aux producteurs de la région qui viennent vendre leurs récoltes |
| Acheteurs | acheteurs professionnels (restaurateurs, commerçants, marchés forains, restauration collective), titulaires d'une carte d'acheteur, qui entrent sur le site par le péage |
| Entrepôt frigorifique | 12 000 m² en 40 cellules louées aux entreprises installées ; BRÉVALIM produit le froid et le refacture |
| Actionnaires | Brévaline Métropole 60 % ; Département 6 % ; Banque VERDELIN 14 % ; chambre de commerce et d'industrie 8 % ; Union des grossistes du marché de Brévaline 12 %, présidée par Mme Évelyne GARBUSSAC, grossiste en fruits et légumes |
| Conseil d'administration | douze membres, dont huit représentants des collectivités ; président : M. Bastien FERRANDOU, vice-président de Brévaline Métropole |
| Direction | directrice générale : Mme Héloïse VAUCLERC ; directeur(rice) général(e) délégué(e) chargé(e) de l'exploitation et du système d'information : vous |

**L'activité en 2026**

| Donnée | Valeur |
|---|---|
| Site | 60 hectares |
| Entreprises installées | 240 : 150 grossistes, 50 transformateurs et logisticiens, 40 entreprises de services |
| Carreau des producteurs | 300 emplacements, occupés chaque nuit par 180 producteurs en moyenne l'été et 70 l'hiver |
| Acheteurs | 9 000 cartes d'acheteur actives ; 2 000 véhicules d'acheteurs par nuit, six nuits sur sept |
| Horaires | activité de 3 heures à 11 heures |
| Produits | 900 000 tonnes entrées sur le marché dans l'année, dont 30 % de produits régionaux |
| Déchets | 60 % des déchets du site valorisés |
| Chiffre d'affaires | 28 M€ : redevances d'emplacement et loyers 17 M€ ; droits d'entrée et cartes d'acheteur 4 M€ ; refacturation de l'énergie, de l'eau et du froid 5 M€ ; services 2 M€ |
| Dépenses du système d'information | environ 1,3 M€, dont 0,3 M€ d'infogérance |

**L'effectif au 31/12/2026**

| Direction ou service | Salariés |
|---|---|
| Direction de l'exploitation : placiers, agents de péage, agents de sûreté, agents de nuit | 95 |
| Direction technique : froid, maintenance, propreté, déchets | 60 |
| Service commercial et des relations avec les entreprises | 15 |
| Service des systèmes d'information | 7 |
| Fonctions support : finances, ressources humaines, juridique, achats | 25 |
| Direction générale et communication | 8 |
| **Total** | **210** |

**Le système d'information en quelques lignes**

- **Logiciel de gestion du marché**, installé en 2011, édité par un petit éditeur régional : contrats d'emplacement, facturation des redevances et des refacturations, attribution des emplacements du carreau, saisie par les placiers sur tablette. Il est installé sur des serveurs de la salle informatique du siège, dont l'exploitation (supervision, sauvegardes, astreinte) est confiée depuis 2024 à un infogérant.
- **Système de péage et de contrôle d'accès** (barrières, lecteurs de cartes, bornes de paiement), choisi en 2019 par la direction de l'exploitation chez un fournisseur spécialisé, avec son propre serveur.
- **Application des acheteurs** (carte d'acheteur sur téléphone, horaires, plan), développée en 2023 par une agence web.
- **Portail des entreprises installées** (factures, demandes techniques).
- **Supervision du froid** de l'entrepôt, choisie par la direction technique.
- **Badges** d'accès aux pavillons, à l'entrepôt et aux locaux techniques.
- Pont-bascule et suivi des déchets ; progiciel comptable et de paie ; bureautique en ligne.

**Organigramme simplifié (avril 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil d'administration | président : M. Bastien FERRANDOU |
| — | direction générale | directrice générale : Mme Héloïse VAUCLERC |
| Directeur(rice) général(e) délégué(e) chargé(e) de l'exploitation et du système d'information (vous) | direction de l'exploitation | Mme Armelle DUCHÉRAN |
| | direction technique | M. Loïc PERRAGUÈS |
| Directrice générale | service commercial et des relations avec les entreprises | Mme Nadège QUÉRINEL |
| | direction administrative et financière : fonctions support (finances, ressources humaines, juridique, achats) | M. Fabrice MORVÉLAN |
| | communication | — |
| Direction administrative et financière | service des systèmes d'information | M. Corentin LAVEYRAC, responsable des systèmes d'information |
| | déléguée à la protection des données, juriste | Mme Inès TALMONDIER |

### ANNEXE 1.2 – Le système d'information vu par les directions et par les actionnaires (témoignages recueillis en mars 2027)

**M. Corentin LAVEYRAC, responsable des systèmes d'information** : « Nous sommes sept, rattachés à la direction administrative et financière. Nous passons nos journées à dépanner et à installer : postes, tablettes, imprimantes, comptes. Le péage a été choisi en 2019 par l'exploitation, la supervision du froid en 2025 par la direction technique : nous n'avons été associés à aucun des deux choix, et nous découvrons leurs serveurs quand ils tombent en panne. J'apprends les projets quand les factures arrivent à la comptabilité. Sur 1,3 M€ de dépenses du système d'information en 2026, 0,5 M€ passent par le budget de mon service, dont l'infogérance ; les 0,8 M€ restants sont engagés directement par les directions. Aucune réunion ne rassemble les directions sur le système d'information : les demandes nous arrivent par courriel, sans priorité. Après 18 heures, il n'y a plus personne au service. »

**Mme Armelle DUCHÉRAN, directrice de l'exploitation** : « Le péage et les tablettes des placiers marchent. Quand j'ai besoin d'un outil, je le choisis avec mes équipes : je ne vais pas attendre l'informatique. Mes agents travaillent la nuit, les placiers dès minuit, quand le service des systèmes d'information n'est pas là. Si une borne du péage tombe en panne à 4 heures, j'appelle le fournisseur ; si les tablettes ne répondent plus, nous passons au papier et nous attendons 8 heures. »

**Mme Évelyne GARBUSSAC, présidente de l'Union des grossistes du marché de Brévaline** : « Sur 240 entreprises installées, 90 seulement ont un compte sur le portail ; les autres reçoivent leurs factures sur papier. Chaque demande technique, une porte de cellule qui ferme mal, une fuite d'eau, se règle par courrier ou par téléphone, et on ne sait jamais où elle en est. Les entreprises veulent tout trouver sur le portail : factures, demandes, consignes du marché. »

**M. Bastien FERRANDOU, président du conseil d'administration** : « Brévaline Métropole veut des données sur les flux alimentaires du marché et un compte rendu chaque trimestre. Or le conseil ne voit jamais les projets du système d'information avant qu'ils soient engagés : la supervision du froid, 90 k€, ne lui a jamais été présentée. Le plan "Marché de Brévaline 2031" ne réussira pas si ses projets numériques se décident direction par direction. »

### ANNEXE 1.3 – Les projets demandés pour 2027-2029 (tableau établi par la direction générale, mars 2027)

| Projet | Demandeur | Coût estimé sur 2027-2029 (k€) | Objectif du plan invoqué par le demandeur | Durée | Dépendances et éléments connus |
|---|---|---|---|---|---|
| P1. Remplacement du logiciel de gestion du marché | direction administrative et financière et service commercial | 450 | fiabiliser la facturation et le pilotage | 18 mois | l'éditeur, une entreprise de huit personnes, cessera de maintenir la version installée à la fin de 2029 ; la facturation, le portail des entreprises et l'attribution du carreau reposent sur ce logiciel |
| P2. Nouvelle version de l'application des acheteurs : commandes passées aux grossistes avant l'arrivée sur le marché | Union des grossistes | 250 | dématérialiser la relation avec les acheteurs | 12 mois | ne peut commencer qu'une fois le nouveau logiciel de gestion du marché en service (P1) ; 25 grossistes sur 150 se disent prêts à publier leurs offres et leurs prix dans l'application |
| P3. Extraction automatique des données des documents d'arrivage | service commercial | 120 | porter à 40 % la part des produits régionaux | 6 mois | aucune ; outil proposé par un éditeur (annexe 1.5) |
| P4. Renouvellement du péage : barrières, lecteurs et bornes | direction de l'exploitation | 600 | garantir la sûreté du site | 12 mois | aucune ; le système de 2019 fonctionne, et son fournisseur s'engage à le maintenir jusqu'en 2031 |
| P5. Wifi du site pour les entreprises | Union des grossistes | 150 | dématérialiser la relation avec les entreprises installées | 6 mois | aucune ; les tablettes des placiers passent aujourd'hui par le réseau mobile, saturé les nuits de forte affluence ; dans les pavillons, les salariés des entreprises n'ont aucun accès au portail |
| P6. Outil de suivi des déchets par entreprise | direction technique | 180 | valoriser 80 % des déchets du site | 9 mois | comprend le raccordement du pont-bascule : chaque pesée serait attribuée à une entreprise et publiée sur le portail des entreprises |
| **Total demandé** | | **1 750** | | | |

Conventions :
- les coûts sont des coûts totaux sur 2027-2029, en sommes rondes ; on admet qu'ils se répartissent sur la durée de chaque projet ; l'étalement des dépenses d'une année à l'autre n'est pas à étudier ;
- les dépenses du système d'information ne pourront pas augmenter de plus de 0,3 M€ par an par rapport à 2026 : les nouveaux projets disposent ensemble de 900 k€ au plus sur les trois ans ;
- aucun projet ne peut démarrer avant septembre 2027 ; les sept personnes du service des systèmes d'information ne peuvent pas conduire plus de deux projets à la fois.

### ANNEXE 1.4 – Les applications et leurs échanges (description établie par M. Corentin LAVEYRAC, mars 2027)

1. **Logiciel de gestion du marché** (2011, petit éditeur régional). Utilisateurs : service commercial (contrats d'emplacement), comptabilité (facturation des redevances et des refacturations), placiers (attribution des emplacements du carreau sur tablette, la nuit). Hébergement : serveurs de la salle informatique du siège, exploités par l'infogérant. Échanges : chaque mois, un fichier des factures est transmis au progiciel comptable ; chaque mois, les factures sont déposées en PDF sur le portail des entreprises.
2. **Péage et contrôle d'accès** (2019, fournisseur spécialisé). Utilisateurs : agents de péage, qui créent les cartes d'acheteur à l'accueil du péage. Hébergement : serveur propre installé dans le local du péage, maintenu à distance par son fournisseur, hors du contrat d'infogérance. Échanges : chaque nuit, un fichier des cartes actives est envoyé à l'application des acheteurs ; les cartes créées au péage sont ressaisies par le service commercial dans le logiciel de gestion du marché pour facturer les abonnements.
3. **Application des acheteurs** (2023, agence web). Utilisateurs : acheteurs, sur leur téléphone (carte d'acheteur, horaires, plan). Hébergement : chez un hébergeur choisi par l'agence web. Échanges : reçoit le fichier des cartes actives envoyé chaque nuit par le péage ; aucun autre échange.
4. **Portail des entreprises installées** (module fourni par l'éditeur du logiciel de gestion du marché). Utilisateurs : 90 entreprises installées qui y ont un compte, surtout leurs dirigeants et leurs services administratifs ; contenu en français seulement. Hébergement : mêmes serveurs que le logiciel de gestion du marché. Échanges : reçoit chaque mois les factures en PDF ; les demandes techniques déposées sur le portail sont imprimées par la direction technique, puis ressaisies dans son tableur de suivi des interventions ; la réponse est envoyée par courrier.
5. **Supervision du froid** (2025, choisie par la direction technique). Utilisateurs : techniciens du froid ; les alarmes de température des 40 cellules sont envoyées par SMS au technicien d'astreinte. Hébergement : service en ligne de son éditeur. Échanges : aucun ; chaque mois, les consommations de froid de chaque cellule sont relevées à l'écran et ressaisies dans le logiciel de gestion du marché pour la refacturation du froid.
6. **Badges d'accès** aux pavillons, à l'entrepôt et aux locaux techniques. Utilisateurs : responsable de la sûreté et agents de sûreté. Hébergement : serveur propre installé au poste de sûreté. Échanges : aucun ; les badges sont créés à partir de formulaires papier remplis par les entreprises installées.
7. **Pont-bascule et suivi des déchets**. Utilisateurs : agents de la direction technique. Hébergement : poste dédié à l'entrée de la déchetterie du site. Échanges : aucun ; le pont-bascule imprime un ticket par pesée de benne ; chaque mois, les totaux sont recopiés dans un tableur de la direction technique.
8. **Progiciel comptable et de paie** (service en ligne). Utilisateurs : finances et ressources humaines. Échanges : reçoit chaque mois le fichier des factures du logiciel de gestion du marché ; les éléments variables de la paie des agents de nuit sont saisis à partir des plannings tenus dans des tableurs par la direction de l'exploitation.
9. **Bureautique en ligne** (messagerie, traitement de texte, tableurs partagés). Utilisateurs : tous les salariés qui disposent d'un poste. Échanges : sert de lien entre les applications par des tableurs envoyés par courriel.

### ANNEXE 1.5 – L'extraction automatique des documents d'arrivage (note de Mme Nadège QUÉRINEL, responsable commerciale et des relations avec les entreprises, mars 2027)

**La situation actuelle.** Pour justifier les tonnages qu'ils déclarent et l'origine de leurs produits, les grossistes nous envoient chaque mois leurs documents d'arrivage : bons de livraison et lettres de voiture des transporteurs. Ils arrivent par courriel, en PDF ou en photo prise au téléphone, sous 25 formats différents ; nous en recevons environ 6 000 par mois. Deux personnes du service commercial en saisissent le produit, l'origine, le poids et la date dans un tableur. Les données d'un mois ne sont complètes que six semaines après sa fin. Les documents portent aussi le nom et le numéro de téléphone des chauffeurs et, pour certains grossistes, le prix d'achat des produits.

**L'outil proposé.** Un éditeur nous propose un outil qui lit automatiquement ces documents et en extrait les quatre données : produit, origine, poids, date. Il repose sur l'apprentissage automatique : avant la mise en service, il serait entraîné sur 20 000 documents de 2025 et 2026 que nous avons déjà saisis, en comparant ce qu'il lit à ce que nous avons saisi. Pour chaque donnée extraite, il donne un indice de confiance de 0 à 100 ; sous le seuil que nous fixerons, la donnée est signalée pour vérification. Les corrections faites par nos équipes peuvent servir à l'entraîner de nouveau.

**Les résultats annoncés par l'éditeur**, sur des documents d'autres clients :
- documents dactylographiés : 2 % des données extraites sont erronées ;
- documents manuscrits, environ un document sur cinq chez nos grossistes : 25 % des données extraites sont erronées ;
- une photo floue ou un format jamais vu donne des indices de confiance bas.

L'éditeur héberge l'outil et les documents dans son propre service en ligne.

### ANNEXE 1.6 – Les savoirs partagés avec les entreprises installées (constats de M. Loïc PERRAGUÈS, directeur technique, et de Mme Nadège QUÉRINEL, mars 2027)

**Des bonnes pratiques dispersées.** Les règles de bon usage du site existent, mais chacune est ailleurs :
- chaîne du froid dans les cellules : fermer les portes et les rideaux à lanières, ne pas bloquer les portes avec une palette, charger sans arrêter le froid ;
- tri des déchets : cinq bennes par pavillon (cartons, bois et palettes, déchets alimentaires, polystyrène, déchets non recyclables), avec des règles qui changent selon les filières ;
- sûreté de nuit : fermeture des cases, signalement d'une personne ou d'un véhicule suspect ;
- consignes en cas de panne du péage : qui lève les barrières, comment noter les passages.

Ces règles figurent sur des affiches en français dans les pavillons, dans des courriels envoyés aux dirigeants des entreprises, rarement transmis à leurs équipes, et dans la réunion annuelle avec les entreprises installées (40 présentes sur 240 en 2026). Une partie n'est écrite nulle part : quelques agents de nuit savent quelles portes de cellules ferment mal, comment relancer une borne du péage ou quel transporteur arrive avant l'heure.

**Des incidents qui se répètent en 2026.**
- 40 ruptures de froid dues à des portes de cellules laissées ouvertes, dont 6 ont conduit des grossistes à détruire des marchandises.
- 300 bennes refusées par le prestataire de collecte pour mauvais tri, sur 12 000 bennes collectées, soit 2,5 % : leur contenu n'est pas valorisé.
- 8 pannes du péage la nuit, pendant lesquelles les agents ont appliqué des consignes différentes : barrières levées sans contrôle certaines nuits, acheteurs refoulés d'autres nuits.

**Les personnes à toucher.** Selon l'Union des grossistes, un salarié sur trois des entreprises installées est remplacé dans l'année. Beaucoup travaillent la nuit, sur les quais et dans les cellules, sans ordinateur, mais avec un téléphone ; une douzaine de langues sont parlées sur le marché. Certains grossistes ont leurs propres savoir-faire, sur le mûrissage des fruits, la conservation des produits de la mer ou la préparation des commandes de la restauration collective, et ne veulent pas les partager avec leurs concurrents.

**Les outils existants.** Le portail des entreprises installées (90 entreprises ont un compte) ; l'application des acheteurs, installée par la plupart des acheteurs ; les tablettes des placiers, utilisées chaque nuit sur le carreau.

### ANNEXE 1.7 – Le contrat d'infogérance (extraits du contrat et note de M. Corentin LAVEYRAC, mars 2027)

**A. Extraits du contrat signé en mars 2024 pour quatre ans (échéance en mars 2028)**

| Article | Contenu |
|---|---|
| Objet | exploitation des serveurs de la salle informatique du siège, qui portent le logiciel de gestion du marché et le portail des entreprises installées : supervision, sauvegardes, mises à jour, astreinte ; le serveur du péage, celui des badges et les services en ligne en sont exclus |
| Prix | 0,3 M€ par an |
| Plage de service | jours ouvrés, du lundi au vendredi hors jours fériés, de 8 heures à 18 heures |
| Astreinte | joignable par téléphone les jours ouvrés de 18 heures à 20 heures ; aucune astreinte la nuit, le samedi, le dimanche ni les jours fériés |
| Incidents | prise en charge dans un délai de quatre heures ouvrées après le signalement ; aucun délai de rétablissement n'est fixé |
| Disponibilité | 99 % du temps de la plage de service, mesurée par l'infogérant |
| Suivi | rapport d'activité annuel ; aucune pénalité |
| Accès | l'infogérant administre les serveurs avec des comptes à tous les droits |
| Sauvegardes | l'infogérant peut confier les sauvegardes à un prestataire de son choix |

Le contrat ne contient aucune clause sur les données personnelles ni sur la confidentialité des données.

**B. Note de M. Corentin LAVEYRAC**

- Les serveurs portent les contrats d'emplacement, les factures et les redevances de chaque entreprise installée, les attributions du carreau, ainsi que les nom, adresse et coordonnées des titulaires des cartes d'acheteur facturées par abonnement.
- L'infogérant a confié les sauvegardes à un autre prestataire, qui les conserve dans son propre centre de données ; nous ne connaissons ni son nom ni le lieu de conservation.
- En 2026, nous avons relevé 14 incidents entre minuit et 8 heures. Six fois, vers 3 heures, le logiciel de gestion du marché est devenu inaccessible aux tablettes des placiers : le carreau a été attribué sur papier, puis ressaisi le lendemain ; le service a été rétabli en moyenne vers 11 heures, huit heures après la panne, à la fin du marché. Quatre incidents survenus un samedi n'ont été traités que le lundi.
- Le rapport annuel 2026 de l'infogérant indique une disponibilité de 99,9 % et conclut qu'« aucun engagement n'a été manqué ».
- Les conditions du renouvellement seront discutées avec l'infogérant actuel à partir de septembre 2027 ; aucune procédure de choix du prestataire n'est à organiser.

### ANNEXE 1.8 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Gestion des services informatiques | ITIL 4, PeopleCert (ex-AXELOS), 2019 ; coexiste depuis 2026 avec ITIL (version 5) | référentiel de bonnes pratiques, ni norme ni logiciel : accord de niveau de service, gestion des incidents, amélioration continue |
| Données personnelles | règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | un prestataire qui traite des données personnelles pour le compte de BRÉVALIM agit en sous-traitant ; un contrat écrit fixe ses obligations ; il ne peut recourir à un autre sous-traitant qu'avec l'autorisation écrite préalable de BRÉVALIM, qui reste responsable du traitement ; aucune analyse juridique n'est attendue |
| Intelligence artificielle | règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | approche par les risques ; depuis le 02/02/2025, les organisations qui utilisent des systèmes d'intelligence artificielle doivent assurer à leur personnel un niveau suffisant de maîtrise de ces systèmes |

### Travail à faire

Le plan « Marché de Brévaline 2031 » repose sur le système d'information, alors que celui-ci s'est construit direction par direction, que le service des systèmes d'information n'est associé à aucun choix et que le conseil d'administration découvre les projets une fois engagés. Mme VAUCLERC vous demande de proposer les orientations de la stratégie du système d'information et d'arbitrer les projets demandés, de revoir l'organisation de la fonction système d'information, de cartographier les applications et d'éclairer le projet d'extraction automatique des documents d'arrivage, de proposer un dispositif de partage des bonnes pratiques avec les entreprises installées, enfin de préparer les niveaux de service et les clauses du contrat d'infogérance renouvelé. Vous mobiliserez pour cela les annexes 1.1 à 1.8 ainsi que vos connaissances professionnelles.

**1.1 – Les orientations de la stratégie du système d'information et le portefeuille de projets (3,5 points)**

a) Après avoir défini la planification stratégique du système d'information et la gestion d'un portefeuille de projets, proposez trois orientations de la stratégie du système d'information de BRÉVALIM, chacune justifiée par un objectif du plan « Marché de Brévaline 2031 » et par un constat des annexes. Il n'est demandé ni schéma directeur, ni feuille de route.

b) Construisez une grille d'arbitrage de trois ou quatre critères, dont la contribution au plan et le risque du projet, et appliquez-la aux six projets de l'annexe 1.3. Retenez les projets à conduire de 2027 à 2029 dans la limite de dépenses fixée, en justifiant leur ordre de lancement, puis indiquez le rôle du conseil d'administration dans cet arbitrage. Aucun calcul financier n'est attendu.

**1.2 – L'organisation de la fonction système d'information (3 points)**

a) Après avoir présenté les principaux modèles d'organisation de la fonction système d'information (centralisée, décentralisée, fédérée, externalisée), analysez, à partir des annexes 1.1 et 1.2, l'organisation actuelle de BRÉVALIM et ses effets. Recommandez ensuite, en les justifiant, un modèle d'organisation et un rattachement du service des systèmes d'information.

b) Proposez trois mesures qui améliorent les relations entre le service des systèmes d'information, la direction générale, les directions métiers et le conseil d'administration, portant respectivement sur les instances, sur le rôle du responsable des systèmes d'information et sur l'information des actionnaires.

**1.3 – La cartographie applicative et l'extraction automatique des documents d'arrivage (2,5 points)**

a) Après avoir défini la cartographie applicative et la cartographie fonctionnelle, représentez, à partir de l'annexe 1.4, la cartographie applicative de BRÉVALIM : applications regroupées par domaine fonctionnel, échanges entre elles et nature de ces échanges. Relevez ensuite trois faiblesses qu'elle révèle.

b) Expliquez le fonctionnement de l'outil d'extraction présenté à l'annexe 1.5 (apprentissage à partir des documents déjà saisis, indice de confiance, erreurs), puis proposez deux conditions de son usage par BRÉVALIM. Aucune classification de l'outil au titre du règlement sur l'intelligence artificielle n'est attendue.

**1.4 – Le partage des bonnes pratiques avec les entreprises installées (3 points)**

a) Après avoir défini la gestion des connaissances et distingué connaissances tacites et connaissances explicites, fixez, à partir de l'annexe 1.6, les objectifs d'un dispositif de partage des bonnes pratiques entre BRÉVALIM et les entreprises installées, en distinguant les contenus partagés avec toutes les entreprises et les contenus réservés à chacune.

b) Montrez comment ce dispositif s'intègre aux outils existants de BRÉVALIM.

c) Proposez la gouvernance du dispositif (rôles, animation) et deux indicateurs de suivi, chacun avec sa formule, sa source, sa fréquence, sa cible et son axe.

d) Proposez trois leviers d'appropriation adaptés à des salariés qui travaillent la nuit, sans ordinateur, et parlent plusieurs langues.

**1.5 – Les niveaux de service du contrat d'infogérance (2 points)**

a) Analysez, à partir de l'annexe 1.7, l'adéquation des niveaux de service du contrat d'infogérance à l'activité de nuit du marché, puis proposez trois niveaux de service à inscrire dans le contrat renouvelé, en choisissant parmi la plage de service, le délai de rétablissement, l'astreinte et la mesure de la disponibilité.

b) Indiquez, en principe, les deux clauses à prévoir sur les données : la sous-traitance des données personnelles, y compris le recours à un autre sous-traitant, et la confidentialité des données commerciales des grossistes. Aucune analyse juridique des clauses ni aucune procédure de choix du prestataire n'est attendue.
