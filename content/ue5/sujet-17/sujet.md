# DSCG UE 5 — Management des systèmes d'information — Sujet d'entraînement complet n° 17

Durée de l'épreuve : 3 heures – Coefficient : 1

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026.

**Document et matériel autorisés** : Aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Le sujet se présente sous la forme de 3 dossiers indépendants :

| Dossier | Intitulé | Points | Durée conseillée |
|---|---|---:|---|
| DOSSIER 1 | PRÉPARER LA STRATÉGIE ET L'ORGANISATION DU SYSTÈME D'INFORMATION | 14 points | 1 h 03 |
| DOSSIER 2 | ORGANISER ET EXPLOITER LES DONNÉES DES ACHETEURS ET DES FLUX, REVOIR LE PILOTAGE | 13 points | 59 min |
| DOSSIER 3 | FIABILISER LA FACTURATION, MAÎTRISER LES ACCÈS, AUDITER LE CARREAU ET RÉPONDRE AUX DEMANDES DE DONNÉES DE DURABILITÉ | 13 points | 58 min |

Le sujet comporte 18 annexes, dont 1 communes aux dossiers.

| Dossier | Annexe | Intitulé |
|---|---|---|
| Tous les dossiers | Annexe 1.1 | Présentation de BRÉVALIM et chiffres clés |
| DOSSIER 1 | Annexe 1.2 | Le système d'information vu par les directions et par les actionnaires (témoignages recueillis en mars 2027) |
|  | Annexe 1.3 | Les projets demandés pour 2027-2029 (tableau établi par la direction générale, mars 2027) |
|  | Annexe 1.4 | Les applications et leurs échanges (description établie par M. Corentin LAVEYRAC, mars 2027) |
|  | Annexe 1.5 | L'extraction automatique des documents d'arrivage (note de Mme Nadège QUÉRINEL, responsable commerciale et des relations avec les entreprises, mars 2027) |
|  | Annexe 1.6 | Les savoirs partagés avec les entreprises installées (constats de M. Loïc PERRAGUÈS, directeur technique, et de Mme Nadège QUÉRINEL, mars 2027) |
|  | Annexe 1.7 | Le contrat d'infogérance (extraits du contrat et note de M. Corentin LAVEYRAC, mars 2027) |
|  | Annexe 1.8 | Repères (au 31/12/2026) |
| DOSSIER 2 | Annexe 2.1 | Les cartes d'acheteur et les passages au péage (note de Mme Armelle DUCHÉRAN, directrice de l'exploitation, mars 2027) |
|  | Annexe 2.2 | La fréquentation des acheteurs en 2025 et 2026 (tableaux de la direction de l'exploitation, tirés du système de péage, février 2027) |
|  | Annexe 2.3 | Les données des flux alimentaires (note de Mme Nadège QUÉRINEL, responsable commerciale et des relations avec les entreprises, et extraits de deux courriers, mars 2027) |
|  | Annexe 2.4 | Le tableau de bord trimestriel du conseil d'administration (tableau présenté au conseil du 15/02/2027 et remarques des administrateurs) |
|  | Annexe 2.5 | Repères (au 31/12/2026) |
| DOSSIER 3 | Annexe 3.1 | La facturation des contrats d'emplacement (note de M. Fabrice MORVÉLAN, directeur administratif et financier, mars 2027) |
|  | Annexe 3.2 | Les badges et les comptes (relevé de M. Rodolphe MARCHEVIEL, responsable de la sûreté, et de M. Corentin LAVEYRAC, responsable des systèmes d'information, mars 2027) |
|  | Annexe 3.3 | L'attribution des emplacements du carreau des producteurs (note de Mme Josiane TRÉMOULAC, chef des placiers, extraits de plaintes et demande du conseil d'administration, mars 2027) |
|  | Annexe 3.4 | Les demandes de données de durabilité et le projet d'affichage dynamique (note de M. Loïc PERRAGUÈS, directeur technique, mars 2027) |
|  | Annexe 3.5 | Repères (au 31/12/2026) |

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

---

## DOSSIER 1 – PRÉPARER LA STRATÉGIE ET L'ORGANISATION DU SYSTÈME D'INFORMATION (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES ACHETEURS ET DES FLUX, REVOIR LE PILOTAGE (13 points)

### ANNEXE 2.1 – Les cartes d'acheteur et les passages au péage (note de Mme Armelle DUCHÉRAN, directrice de l'exploitation, mars 2027)

**A. Le fonctionnement actuel**

Une entreprise qui veut acheter sur le marché (restaurant, commerce de détail, marché forain, restauration collective) se présente à l'accueil du péage. L'agent de péage crée sa fiche dans le système de péage, puis une carte d'acheteur pour chaque personne de l'entreprise qui viendra au marché. Le titulaire présente sa carte, en plastique ou sur son téléphone grâce à l'application des acheteurs, au lecteur d'une borne d'entrée : la barrière se lève et le passage est enregistré. Un acheteur sans carte peut aussi payer son entrée à la borne, par carte bancaire : il indique sa catégorie sur l'écran, mais son passage n'est rattaché à aucune carte ni à aucune entreprise. Le site compte deux entrées de véhicules, au nord et au sud, équipées chacune de plusieurs bornes, et une entrée des piétons, sans borne.

Le serveur du système de péage conserve toutes les fiches et tous les passages depuis 2019, avec le nom et le prénom des titulaires des cartes et l'immatriculation de leur véhicule.

**B. Les problèmes de qualité relevés en janvier 2027**

- **Doublons** : le système de péage contient 6 000 fiches d'entreprises acheteuses. Une même entreprise est souvent saisie une deuxième fois, sous une autre orthographe de sa raison sociale (« Le Comptoir de Brévaline », « COMPTOIR BREVALINE SARL »), quand un autre de ses salariés vient demander une carte : on compte environ 400 doublons. Le numéro SIREN n'est pas obligatoire.
- **Catégories** : la catégorie est saisie en texte libre ; 800 fiches, plus d'une sur dix, sont classées « autre », souvent faute de temps à l'accueil.
- **Cartes d'entreprises fermées** : un contrôle de 1 000 cartes actives tirées au hasard a trouvé 50 cartes, une sur vingt, au nom d'entreprises fermées depuis plus d'un an. Aucune carte n'est désactivée quand une entreprise ferme.
- **Passages sans carte** : en 2026, environ un passage sur dix a été payé à la borne ; ces passages ne sont rattachés à aucune entreprise.

**C. Les règles de gestion des cartes d'acheteur et des passages au péage**

- **RG1** – Une entreprise acheteuse est identifiée par un numéro attribué par BRÉVALIM ; on connaît sa raison sociale, son numéro SIREN, sa commune et, le cas échéant, sa date de fermeture.
- **RG2** – Une entreprise acheteuse appartient à une seule catégorie. Une catégorie est identifiée par un code et porte un libellé (restaurant, commerce de détail, marché forain, restauration collective, autre) ; elle peut ne compter encore aucune entreprise.
- **RG3** – Une entreprise acheteuse détient une ou plusieurs cartes ; une carte appartient à une seule entreprise. Une carte est identifiée par un numéro ; on connaît le nom et le prénom de son titulaire, l'immatriculation du seul véhicule enregistré sur la carte, ses dates d'émission et de fin de validité, et son statut (active, suspendue, désactivée).
- **RG4** – Une carte relève d'un seul type d'abonnement. Un type d'abonnement est identifié par un code ; il porte un libellé (annuel, mensuel, à la nuit) et le tarif d'un passage en vigueur. Les tarifs changent au 1er janvier de chaque année.
- **RG5** – Une borne d'entrée est identifiée par un numéro ; on connaît l'entrée où elle est installée (nord ou sud) et sa date de mise en service.
- **RG6** – Un passage est identifié par un numéro ; on connaît sa date et son heure. Il est rattaché à une seule carte et enregistré par une seule borne d'entrée ; il conserve le tarif appliqué le jour du passage. Une carte peut n'avoir encore aucun passage ; une borne enregistre zéro, un ou plusieurs passages.

### ANNEXE 2.2 – La fréquentation des acheteurs en 2025 et 2026 (tableaux de la direction de l'exploitation, tirés du système de péage, février 2027)

**A. Passages, entreprises acheteuses actives et paiement à la borne, par catégorie d'acheteurs**

| Catégorie d'acheteurs | Passages par nuit 2025 | Passages par nuit 2026 | Entreprises actives 2025 | Entreprises actives 2026 | Passages payés à la borne 2025 | Passages payés à la borne 2026 |
|---|---|---|---|---|---|---|
| Restaurants | 800 | 720 | 1 500 | 1 800 | 5 % | 10 % |
| Commerces de détail | 600 | 620 | 1 200 | 1 200 | 5 % | 10 % |
| Marchés forains | 350 | 360 | 600 | 600 | 10 % | 10 % |
| Restauration collective | 150 | 160 | 200 | 200 | 0 % | 0 % |
| Autre | 160 | 140 | 1 000 | 600 | 20 % | 20 % |
| **Ensemble** | **2 060** | **2 000** | **4 500** | **4 400** | **environ 7 %** | **environ 10 %** |

Conventions : un passage est l'entrée d'un véhicule enregistrée par une borne ; les passages par nuit sont la moyenne des nuits d'ouverture (six nuits sur sept). Les passages payés à la borne sont rangés dans la catégorie que l'acheteur a indiquée sur l'écran. Une entreprise est active si l'une de ses cartes a enregistré au moins un passage dans l'année. La catégorie retenue est celle de la fiche de l'entreprise au 31 décembre de l'année.

**B. Passages par nuit, par saison**

| Catégorie d'acheteurs | Été 2025 | Été 2026 | Hiver 2025 | Hiver 2026 |
|---|---|---|---|---|
| Restaurants | 900 | 760 | 700 | 680 |
| Commerces de détail | 640 | 660 | 560 | 580 |
| Marchés forains | 450 | 460 | 250 | 260 |
| Restauration collective | 100 | 110 | 200 | 210 |
| Autre | 170 | 150 | 150 | 130 |
| **Ensemble** | **2 260** | **2 140** | **1 860** | **1 860** |

L'été va d'avril à septembre ; l'hiver regroupe les mois de janvier à mars et d'octobre à décembre de la même année. Chaque saison compte environ 150 nuits d'ouverture.

**C. Ce que l'on sait des chiffres de 2026**

- **Reclassement** : en janvier 2026, le service commercial a revu les fiches classées « autre » ; 400 entreprises (traiteurs, bars de quartier, snacks) ont été reclassées « restaurant ». Elles font ensemble une vingtaine de passages par nuit, en 2025 comme en 2026, l'été comme l'hiver. Les chiffres de 2025 n'ont pas été recalculés.
- **Panne** : une borne de l'entrée sud, qui enregistre en temps normal 500 véhicules par nuit, est restée en panne pendant trois semaines de juillet 2026, soit 18 nuits d'ouverture. Sa barrière est restée levée : environ 9 000 passages n'ont pas été enregistrés.
- **Véhicules partagés** : depuis le printemps 2026, des restaurateurs d'un même quartier viennent à deux ou trois dans un seul véhicule, avec une seule carte, pour partager les frais de route et le tarif d'entrée. Ce tarif a augmenté de 10 % au 1er janvier 2026 pour les cartes annuelles et mensuelles ; celui du paiement à la borne n'a pas changé. Les agents de péage comptent environ 100 véhicules partagés par nuit l'été 2026 et 40 l'hiver, contre presque aucun en 2025.
- **Piétons** : l'entrée des piétons n'a pas de borne. Depuis l'ouverture d'une station de tramway devant le marché, en septembre 2026, les agents de sûreté voient arriver à pied, avec un chariot, des restaurateurs du centre-ville ; personne ne les a comptés.

**D. L'affirmation de Mme Évelyne GARBUSSAC, présidente de l'Union des grossistes, au conseil d'administration du 15/02/2027**

« Les chiffres sont clairs : les restaurateurs désertent le marché au profit des plateformes de livraison. Nous avons perdu 80 restaurants par nuit en un an. BRÉVALIM doit lancer une campagne pour les faire revenir. »

### ANNEXE 2.3 – Les données des flux alimentaires (note de Mme Nadège QUÉRINEL, responsable commerciale et des relations avec les entreprises, et extraits de deux courriers, mars 2027)

**A. La demande de Brévaline Métropole (courrier de sa direction de l'agriculture et de l'alimentation, février 2027)**

« Pour son observatoire de l'alimentation, Brévaline Métropole souhaite recevoir chaque trimestre, à partir des chiffres du deuxième trimestre 2027, les tonnages entrés sur le marché par filière alimentaire (fruits et légumes, produits de la mer, viandes, produits laitiers) et par origine (région, reste de la France, étranger), ainsi que la part des produits régionaux, que le plan « Marché de Brévaline 2031 » veut porter de 30 % à 40 %. L'observatoire publiera ces chiffres sur son site. Il serait utile que nous recevions aussi la déclaration de chaque grossiste, pour nos propres analyses. »

**B. La collecte actuelle des tonnages**

- Les 150 grossistes (80 en fruits et légumes, 25 en produits de la mer, 25 en viandes, 12 en produits laitiers, 8 en fleurs) déclarent chaque mois leurs tonnages entrés, par produit et par origine, dans un tableur qu'ils remplissent chacun à leur façon et envoient par courriel au service commercial, avant le 10 du mois suivant.
- En 2026, sur 1 800 déclarations attendues, 1 350 sont arrivées dans le délai, 270 en retard et 180 jamais. Pour une déclaration manquante, on reprend à la main le chiffre du mois précédent, sans le signaler.
- La colonne « origine » est remplie en texte libre : elle est vide pour 20 % des tonnages déclarés ; pour 15 %, elle indique « France », sans distinguer la région du reste de la France.
- Il n'existe aucune définition écrite du « produit régional ». Un grossiste compte les produits cultivés ou élevés dans la région ; un autre, les produits conditionnés dans la région ; un troisième, tout ce qu'il achète aux producteurs du carreau.
- La part de 30 % de produits régionaux de 2026 rapporte les tonnages déclarés « région » à l'ensemble des tonnages déclarés, origines vides comprises.
- Personne n'est chargé de ces données : une assistante du service commercial rassemble les tableurs quand elle en a le temps. Les fichiers, qui portent aussi le nom et le téléphone du déclarant de chaque grossiste, sont conservés depuis 2012, sans limite de durée, dans un dossier de la bureautique en ligne ouvert aux 15 personnes du service commercial et à plusieurs placiers.
- En octobre 2025, un tableau des tonnages de chaque grossiste a été envoyé par erreur à toute la liste de diffusion des entreprises installées.

**C. L'avis de l'Union des grossistes (courrier de Mme Évelyne GARBUSSAC, mars 2027)**

« Nos volumes, par produit et par origine, sont des données commerciales sensibles : un concurrent qui les connaîtrait saurait d'où viennent nos produits et quelle part du marché nous tenons. Depuis l'envoi d'octobre 2025, plusieurs de nos membres hésitent à déclarer. Nous acceptons que la métropole reçoive des totaux par filière, jamais les chiffres d'une entreprise. Mais dans les produits laitiers, deux grossistes font à eux seuls les trois quarts des volumes : le total de la filière, origine par origine, révélerait presque leurs chiffres. »

**D. Ce que ces données pourraient apporter, selon Mme QUÉRINEL**

« Des tonnages fiables nous serviraient à suivre l'objectif de 40 % de produits régionaux, à expliquer à l'Union des grossistes l'évolution des redevances d'emplacement, à montrer l'attractivité du marché aux grossistes qui envisagent de s'installer et aux acheteurs, et à dialoguer avec la métropole, notre premier actionnaire. Je crains aussi que l'observatoire publie un chiffre faux : l'Union conteste déjà la part de 30 %. »

### ANNEXE 2.4 – Le tableau de bord trimestriel du conseil d'administration (tableau présenté au conseil du 15/02/2027 et remarques des administrateurs)

**A. Le tableau de bord du quatrième trimestre 2026**

| Indicateur | T4 2025 | T4 2026 |
|---|---|---|
| Chiffre d'affaires du trimestre (k€) | 6 800 | 7 300 |
| Entreprises installées | 238 | 240 |
| Cartes d'acheteur actives | 8 800 | 9 000 |
| Véhicules d'acheteurs par nuit (moyenne du trimestre) | 1 850 | 1 850 |
| Tonnes entrées sur le marché | 220 000 | 225 000 |
| Demandes techniques des entreprises installées | 1 100 | 1 300 |
| Connexions à l'application des acheteurs | 50 000 | 70 000 |
| Effectif au dernier jour du trimestre | 205 | 210 |
| Nuits d'ouverture | 78 | 78 |

**B. Sa production**

Le tableau de bord n'a pas changé depuis 2015. Chaque trimestre, l'assistante de direction reçoit des extractions du logiciel de gestion du marché, du système de péage, de l'application des acheteurs, du tableur des tonnages et du progiciel comptable et de paie, qu'elle recopie à la main dans un tableur : il lui faut trois jours. Le tableau est envoyé aux administrateurs la veille du conseil, sans commentaire. Aucune ligne n'indique d'où vient le chiffre ni comment il est calculé.

**C. Les remarques des administrateurs (procès-verbal du conseil du 15/02/2027)**

- M. Bastien FERRANDOU, président : « Nous avons adopté en janvier un plan à cinq objectifs ; je n'en retrouve aucun dans ce tableau. »
- Le représentant de la Banque VERDELIN : « 7 300 k€ de chiffre d'affaires au trimestre : est-ce une bonne nouvelle ? Je n'ai aucun point de comparaison avec ce qui était attendu. »
- M. Fabrice MORVÉLAN, directeur administratif et financier, invité : « La comptabilité arrête le chiffre d'affaires du quatrième trimestre à 7 000 k€ ; je ne sais pas d'où vient le chiffre de 7 300 k€. »
- Mme Évelyne GARBUSSAC : « La panne du péage de juillet et l'envoi de nos tonnages à tout le marché n'ont jamais figuré dans ce tableau. »
- Une administratrice représentant le Département : « Que coûte notre informatique, et ce coût augmente-t-il ? »

### ANNEXE 2.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Gestion des données | DAMA-DMBOK (Data Management Body of Knowledge), DAMA International, 2e édition (2017), révision engagée en 2024 | référentiel de bonnes pratiques de gestion des données, ni norme ni logiciel ; onze domaines de connaissance organisés autour de la gouvernance des données, dont la qualité des données, les métadonnées, les données de référence et la sécurité des données |
| Qualité des données | ISO/IEC 25012, modèle de qualité des données | norme qui décrit les caractéristiques de la qualité des données, dont l'exactitude, la complétude, la cohérence, l'actualité et l'accessibilité |
| Données personnelles | règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | une donnée à caractère personnel est toute information se rapportant à une personne physique identifiée ou identifiable ; les données sont collectées pour des finalités déterminées, limitées à ce qui est nécessaire (minimisation) et conservées pendant une durée limitée ; BRÉVALIM a désigné une déléguée à la protection des données, Mme Inès TALMONDIER ; aucune analyse juridique n'est attendue |

### Travail à faire

Le système de péage enregistre chaque nuit 2 000 passages, mais ses fiches sont mal tenues et personne ne sait dire si les restaurateurs quittent le marché, comme l'affirme la présidente de l'Union des grossistes. Brévaline Métropole veut recevoir chaque trimestre les tonnages entrés sur le marché, que les grossistes déclarent dans des tableurs sans règles communes et qu'ils jugent sensibles. Le conseil d'administration, enfin, reçoit un tableau de bord qui ne lui permet pas de suivre le plan « Marché de Brévaline 2031 ». Mme VAUCLERC vous demande d'organiser les données des cartes et des passages, d'en tirer une analyse fiable de la fréquentation, d'organiser la gouvernance des données des flux et de revoir le tableau de bord du conseil. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.5 ainsi que vos connaissances professionnelles.

**2.1 – Les données des cartes d'acheteur et des passages au péage (3,5 points)**

a) À partir des règles de gestion de l'annexe 2.1 C, établissez le modèle conceptuel des données des cartes d'acheteur et des passages au péage, puis traduisez-le en modèle logique, en énonçant les règles de passage que vous appliquez. Aucune requête n'est attendue.

b) Après avoir défini le dictionnaire des données, rédigez-en quatre entrées pour des données de votre modèle. Proposez ensuite trois règles de qualité qui traitent chacune l'un des problèmes de l'annexe 2.1 B, en précisant la dimension de la qualité des données concernée.

**2.2 – L'analyse de la fréquentation des acheteurs (3,5 points)**

a) Après avoir présenté les étapes de la chaîne de traitement des données, décrivez celle qui produira les indicateurs de fréquentation des acheteurs, en montrant, à chaque étape, une limite des chiffres de l'annexe 2.2 qu'elle doit traiter.

b) Formulez trois constats argumentés tirés de l'annexe 2.2, puis appréciez l'affirmation de Mme GARBUSSAC. Aucun calcul statistique n'est attendu.

c) Après avoir distingué l'analyse descriptive et l'analyse exploratoire, indiquez laquelle convient pour répondre à la question « les restaurateurs désertent-ils le marché ? », en justifiant votre choix. Proposez ensuite la représentation visuelle qui montrerait le mieux au conseil d'administration l'évolution de la fréquentation par catégorie d'acheteurs.

**2.3 – La gouvernance des données des flux alimentaires (3,5 points)**

a) Après avoir défini la gouvernance des données, proposez, à partir de l'annexe 2.3 et en vous appuyant sur le référentiel DAMA-DMBOK, l'organisation de la gouvernance des données des flux : les rôles de propriétaire, d'intendant et de responsable du référentiel, et leurs titulaires chez BRÉVALIM et chez les grossistes.

b) Décrivez le cycle de vie des données des flux, de la déclaration par les grossistes à la suppression, en fixant une règle à chaque étape, dont la règle de diffusion des chiffres à Brévaline Métropole.

c) Appréciez la valeur de ces données pour BRÉVALIM, puis deux risques qui s'y attachent. Aucune analyse juridique n'est attendue.

**2.4 – Le tableau de bord du conseil d'administration (2,5 points)**

a) Après avoir défini le tableau de bord, appréciez celui de l'annexe 2.4 en relevant trois défauts.

b) Proposez trois indicateurs qui le complètent, dont un indicateur d'un objectif du plan « Marché de Brévaline 2031 » et un indicateur de risque, en précisant pour chacun sa formule, sa source, sa fréquence, sa cible et son axe.

c) Proposez deux mesures pour que le tableau de bord soit revu et amélioré dans la durée.

---

## DOSSIER 3 – FIABILISER LA FACTURATION, MAÎTRISER LES ACCÈS, AUDITER LE CARREAU ET RÉPONDRE AUX DEMANDES DE DONNÉES DE DURABILITÉ (13 points)

### ANNEXE 3.1 – La facturation des contrats d'emplacement (note de M. Fabrice MORVÉLAN, directeur administratif et financier, mars 2027)

**A. La chaîne de facturation**

1. **Le contrat.** Le service commercial saisit dans le logiciel de gestion du marché le contrat annuel d'emplacement de chaque entreprise installée : cases, bureaux et cellules occupés, surfaces, tarifs, dates. Les changements en cours d'année (case supplémentaire, agrandissement, déménagement dans un autre pavillon) lui sont signalés par les placiers ou par l'entreprise, par téléphone ou par courriel.
2. **La facture.** Chaque mois, le logiciel émet une facture par entreprise installée, soit 240 factures : redevance d'emplacement et loyer du mois, refacturation de l'énergie, de l'eau et du froid du mois précédent. Les factures sont déposées en PDF sur le portail des entreprises installées ou envoyées sur papier.
3. **Le fichier des écritures.** Chaque mois, le logiciel produit un fichier des écritures des factures et des avoirs, d'environ 2 000 lignes, que la comptabilité charge dans le progiciel comptable.
4. **L'encaissement et les relances.** 200 entreprises paient par prélèvement, 40 par virement. La comptabilité rapproche les encaissements et prépare les relances dans un tableur, à partir d'une extraction du progiciel comptable.

**B. Les constats de 2026 et du début de 2027**

- En 2026, 60 changements d'emplacement ont été demandés. Un relevé de terrain mené en février 2027 par le service commercial a trouvé 15 cases ou cellules occupées par une entreprise dont le contrat n'avait pas été mis à jour. Le manque à facturer est estimé à 150 k€ par an.
- La révision annuelle des tarifs, au 1er janvier, est saisie à la main, contrat par contrat. En janvier 2027, 20 contrats ont été mal révisés : 12 entreprises ont été trop facturées, 8 n'ont pas été facturées au nouveau tarif. L'erreur a été découverte grâce aux réclamations transmises par l'Union des grossistes.
- Les 3 agents de la facturation créent les factures et les avoirs ; un avoir n'exige ni validation ni motif. En 2026, ils ont créé 300 avoirs, pour 400 k€.
- En 2026, 480 lignes du fichier mensuel des écritures, soit 2 %, ont été rejetées par le progiciel comptable (entreprise inconnue, compte absent, montant nul). La comptable les corrige ou les supprime directement dans le progiciel comptable ; rien n'est corrigé dans le logiciel de gestion du marché, et aucune liste des rejets n'est conservée.
- Pour 2026, le logiciel de gestion du marché donne 22 900 k€ de redevances, de loyers et de refacturations ; la comptabilité arrête les mêmes rubriques à 22 000 k€ (17 000 k€ de redevances et de loyers, 5 000 k€ de refacturations). Personne n'a encore expliqué l'écart. Le compte rendu trimestriel aux actionnaires prévu par le plan « Marché de Brévaline 2031 » reprendra ce chiffre d'affaires.
- Le logiciel ne conserve que la dernière version de chaque contrat : on ne sait ni qui a modifié une surface ou un tarif, ni quand. Les 15 personnes du service commercial et les 3 agents de la facturation ont tous les droits sur les contrats, les factures et les avoirs.
- En 2026, 25 entreprises ont été relancées pour des factures déjà payées ou annulées par un avoir.
- Pour 30 entreprises installées, l'identifiant de l'entreprise (numéro SIREN) enregistré dans le logiciel est absent ou ne correspond plus à l'entreprise, après un rachat ou un changement de nom.

**C. L'échéance de septembre 2027**

BRÉVALIM devra émettre ses factures sous forme électronique à compter du 1er septembre 2027 (annexe 3.5). L'éditeur du logiciel de gestion du marché livrera en juin 2027 une version qui transmet les factures à une plateforme agréée. Selon lui, « chaque facture partira avec ses données structurées : identifiant de l'entreprise, contrat, montants ; une facture fausse sera transmise telle quelle à l'entreprise et à la plateforme ».

**D. Les échelles retenues par la direction générale pour apprécier les risques**

| Niveau | Probabilité | Impact |
|---|---|---|
| faible | jamais constaté, peu plausible | moins de 50 k€ par an, sans réclamation |
| moyen | constaté quelques fois en 2026 | de 50 à 200 k€ par an, ou réclamations d'entreprises installées |
| fort | constaté chaque mois en 2026, ou facile à provoquer, ou quasi certain à l'échéance si rien ne change ; dans tous les cas, sa cause est toujours là | plus de 200 k€ par an, ou chiffre d'affaires présenté aux actionnaires inexact, ou factures électroniques erronées en série |

La direction générale traite en priorité les risques dont la probabilité et l'impact sont tous deux forts.

### ANNEXE 3.2 – Les badges et les comptes (relevé de M. Rodolphe MARCHEVIEL, responsable de la sûreté, et de M. Corentin LAVEYRAC, responsable des systèmes d'information, mars 2027)

**A. Les badges d'accès**

| Population | Badges actifs | Dont badges au nom de personnes parties (estimation de mars 2027) | Création du badge | Fin du badge |
|---|---|---|---|---|
| Salariés de BRÉVALIM | 230 | 20 | demande du service des ressources humaines, par courriel | aucune date de fin ; le badge est rendu au départ « quand on y pense » |
| Salariés des entreprises installées | 2 150 | environ 350 | formulaire papier rempli par l'entreprise | aucune date de fin ; aucune entreprise ne signale les départs de ses salariés |
| Saisonniers d'été recrutés par BRÉVALIM pour le carreau (renfort des placiers, propreté) | 80 | 80 | liste remise en mai par la direction de l'exploitation | contrats terminés fin septembre 2026 ; badges toujours actifs |
| Prestataires de nettoyage et de maintenance du froid | 140 | environ 50 | demande du prestataire | aucune date de fin ; 10 badges « prestataire », sans nom, circulent entre les intervenants |
| **Total** | **2 600** | **environ 500** | | |

- Tous les badges ouvrent, à toute heure et tous les jours, les pavillons, les quais et les couloirs de l'entrepôt frigorifique, les portes des 40 cellules et les locaux techniques (salle des machines du froid, locaux électriques). Les portes des cellules s'ouvrent ainsi au badge « pour que les agents de nuit et les techniciens du froid puissent intervenir ». Seuls la salle informatique du siège et le local de la caisse du péage ont un accès réservé.
- Les agents de sûreté constatent chaque semaine des badges prêtés : à un collègue qui a oublié le sien, à un chauffeur, à un salarié qui vient d'arriver et n'a pas encore de badge.
- Le système des badges enregistre chaque passage (badge, porte, heure) ; personne ne consulte ce journal, sauf après un incident.

**B. Les comptes des applications**

- Les 90 entreprises qui ont un compte sur le portail des entreprises installées en ont un seul chacune, créé par l'éditeur à la demande du service commercial. L'identifiant et le mot de passe sont partagés entre le dirigeant, le comptable et des salariés, et ne changent pas quand l'un d'eux quitte l'entreprise. Le compte donne accès à toutes les factures et à toutes les demandes techniques de l'entreprise.
- Les 12 placiers et les saisonniers d'été utilisent sur les tablettes deux comptes génériques du logiciel de gestion du marché, « placier 1 » et « placier 2 », dont le mot de passe n'a pas changé depuis 2019 et figure au dos des tablettes.
- Les comptes du logiciel de gestion du marché et du progiciel comptable sont nominatifs ; le service des systèmes d'information les crée sur demande par courriel, sans profil type.
- Personne n'est chargé de revoir les droits : M. MARCHEVIEL gère les badges, M. LAVEYRAC les comptes des applications, l'éditeur ceux du portail. La liste des personnes autorisées n'a jamais été comparée à celle des badges et des comptes actifs.

**C. Les incidents de 2026**

- 12 vols de marchandises dans des cellules de l'entrepôt, la nuit. Dans 5 cas, le journal des badges montre l'ouverture de la cellule avec le badge d'une personne partie : deux saisonniers de l'été, trois anciens salariés d'entreprises installées.
- En novembre 2026, un grossiste a découvert qu'un salarié d'un concurrent, qui avait travaillé chez lui jusqu'en juin, consultait encore ses factures sur le portail, avec l'identifiant et le mot de passe qu'il connaissait.
- Une nuit d'octobre, un saisonnier de l'été, dont le contrat avait pris fin en septembre, a été trouvé dans la salle des machines du froid.

**D. Deux points de vue**

**Mme Armelle DUCHÉRAN, directrice de l'exploitation** : « Si on limite les badges, mes agents de nuit ne pourront plus ouvrir une cellule en alarme à 4 heures du matin. »

**Mme Évelyne GARBUSSAC, présidente de l'Union des grossistes** : « Nos entreprises n'ont pas le temps de remplir un formulaire à chaque départ : un salarié sur trois change dans l'année. »

### ANNEXE 3.3 – L'attribution des emplacements du carreau des producteurs (note de Mme Josiane TRÉMOULAC, chef des placiers, extraits de plaintes et demande du conseil d'administration, mars 2027)

**A. Les règles écrites (règlement du carreau de 2018)**

- Les 300 emplacements sont attribués chaque nuit, à partir de minuit, par les placiers, qui saisissent chaque attribution sur tablette dans le logiciel de gestion du marché.
- Ordre de priorité : d'abord les abonnés de la saison, qui ont réservé un emplacement fixe pour toute la saison (100 emplacements en été) ; l'emplacement d'un abonné absent à 3 heures est remis en attribution. Ensuite, les autres producteurs, selon leur ancienneté sur le carreau. Enfin, à ancienneté égale, l'ordre d'arrivée constaté au péage.
- Après 3 heures, un placier peut modifier une attribution sans motif (échange d'emplacements, producteur arrivé en retard).
- Les 40 emplacements les plus proches de l'entrée des acheteurs sont les plus recherchés.

**B. Ce que l'on sait de l'été 2026 (180 producteurs par nuit en moyenne)**

- Le logiciel tient un journal des attributions et de leurs modifications : date, heure, compte utilisé, emplacement, producteur. Avec les deux comptes génériques des tablettes, il ne dit pas quel placier a fait la modification. Ce journal est conservé treize mois : les nuits de juin 2026 seront effacées à partir de juillet 2027.
- 40 % des modifications d'attribution ont été faites après 3 heures ; aucune ne porte de motif.
- Sur 10 nuits d'août 2026, Mme TRÉMOULAC a comparé les attributions enregistrées au relevé des emplacements fait à 5 heures par les agents de sûreté : sur 1 800 occupations relevées, 270, soit 15 %, ne correspondent pas à l'attribution enregistrée (autre producteur, emplacement occupé sans attribution, emplacement attribué mais vide).
- Sur les 40 emplacements proches de l'entrée, 30 ont été occupés plus de huit nuits sur dix par les mêmes 25 producteurs ; 10 de ces 25 producteurs ne sont ni abonnés, ni parmi les plus anciens du carreau.
- Six nuits, les tablettes n'ayant plus accès au logiciel, l'attribution s'est faite sur papier, puis a été ressaisie le lendemain ; une partie des feuilles n'a pas été conservée.
- Les 12 placiers travaillent de minuit à 8 heures ; le service des systèmes d'information n'est présent qu'en journée.

**C. Les plaintes (35 plaintes écrites de producteurs en 2026)**

- « Les places près de l'entrée sont toujours données aux mêmes, qui arrivent pourtant après nous. » (un producteur de légumes, juillet 2026)
- « Certains emplacements sont réservés aux habitués : on nous dit qu'ils sont pris, et ils restent vides jusqu'à 4 heures. » (une productrice de fruits, août 2026)
- Mme TRÉMOULAC : « Mes placiers appliquent les règles. Les échanges après 3 heures, c'est pour rendre service. Un audit, ils vont le prendre comme une accusation. »

**D. La demande du conseil d'administration (séance du 22/03/2027)**

« Avant la saison d'été 2027, qui commence le mardi 1er juin, le conseil veut savoir si les emplacements du carreau sont attribués selon les règles écrites et si les données enregistrées sont fiables. BRÉVALIM n'a pas d'audit interne : un auditeur des systèmes d'information externe conduira la mission pendant quatre semaines, du lundi 3 au vendredi 28 mai 2027 (jeudi 6 mai et lundi 17 mai fériés), et présentera ses conclusions au conseil du lundi 31 mai. Préparez-en le cadrage. »

### ANNEXE 3.4 – Les demandes de données de durabilité et le projet d'affichage dynamique (note de M. Loïc PERRAGUÈS, directeur technique, mars 2027)

**A. Les demandes de trois entreprises installées**

Trois entreprises installées, un logisticien qui loue 8 cellules de l'entrepôt frigorifique, un grossiste en produits de la mer et un grossiste en fruits et légumes, appartiennent à des groupes qui établissent leur état de durabilité conformément aux normes ESRS. Chaque année, en janvier, elles nous demandent, pour l'année écoulée et pour leurs cellules et leurs cases, l'électricité et l'eau consommées, le froid fourni et les déchets triés, par type de déchet.

| Donnée demandée | Où elle se trouve aujourd'hui | Comment elle est obtenue |
|---|---|---|
| Électricité et eau consommées | compteurs relevés chaque mois par les techniciens et saisis dans le logiciel de gestion du marché pour la refacturation | extraction du logiciel, puis tri à la main par entreprise |
| Froid fourni | supervision du froid, cellule par cellule | relevé à l'écran, cellule par cellule |
| Déchets triés par type | pont-bascule : une pesée par benne ; chaque benne sert à toutes les entreprises d'un pavillon | aucune donnée par entreprise : le poids du pavillon est réparti selon la surface occupée, sans que l'entreprise en soit informée |

- Une assistante de la direction technique rassemble ces données dans un tableur, qu'elle envoie par courriel : les trois demandes lui prennent 15 jours de travail par an. Rien n'est gardé de ce qui a été envoyé, ni de la façon dont les chiffres ont été obtenus.
- En 2026, un groupe a relevé que l'électricité envoyée pour 2025 comptait deux fois le mois de décembre ; un autre a reçu le froid d'une cellule voisine ; le troisième a demandé pourquoi ses déchets avaient augmenté de moitié, alors qu'il n'avait rien changé.
- Deux autres entreprises installées ont annoncé des demandes semblables pour 2028.
- M. PERRAGUÈS : « Ce n'est pas à BRÉVALIM de faire le reporting de ses clients. Mais si nous répondons mal, ils iront chercher ailleurs des cellules mieux suivies. »

**B. Le projet d'affichage dynamique (proposition du service de la communication, février 2027)**

- 60 écrans de grande taille, achetés neufs, dans les pavillons et au péage, pour afficher les cours du jour, les informations du marché (horaires, travaux, consignes) et des publicités des grossistes.
- Les écrans restent allumés jour et nuit, sept jours sur sept, alors que le marché est ouvert de 3 heures à 11 heures, six nuits sur sept.
- Des vidéos en haute définition passent en boucle ; un serveur rafraîchit tous les écrans toutes les minutes. Les cours du jour sont mis à jour deux fois par nuit par le service commercial.
- BRÉVALIM a déjà 20 écrans d'affichage, installés en 2022 au péage et dans deux pavillons, qui fonctionnent : le projet prévoit de les remplacer et de les mettre au rebut.
- Les horaires, le plan et les informations du marché figurent déjà dans l'application des acheteurs.
- Le service de la communication : « Les écrans rendront le marché plus moderne, et la publicité des grossistes les paiera. »

Aucune mesure de la consommation ni de l'empreinte du projet n'a été faite, et aucun calcul n'est demandé.

**C. La durabilité dans les décisions sur le système d'information**

Aucun comité ni aucune règle ne fait entrer la durabilité dans les décisions sur le système d'information. Le projet d'affichage n'a été examiné que par le service de la communication et par le fournisseur des écrans. Aucune demande d'achat d'équipement ou de logiciel ne comporte de critère environnemental ou social, et personne n'est chargé des demandes de données de durabilité.

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Facturation électronique | généralisation de la facturation électronique et du e-reporting, calendrier issu de l'article 91 de la loi de finances pour 2024 | depuis le 01/09/2026, toutes les entreprises assujetties à la TVA doivent pouvoir recevoir des factures électroniques ; BRÉVALIM devra émettre les siennes sous forme électronique à compter du 01/09/2027 ; les factures transitent par une plateforme agréée par l'administration, dans un format structuré (Factur-X, UBL ou CII) ; aucune règle de facturation n'est à connaître |
| Sécurité de l'information | ISO/IEC 27001:2022 ; ISO/IEC 27002:2022 | la norme ISO/IEC 27001 fixe les exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques ; son annexe A compte 93 mesures en quatre thèmes (organisationnelles, liées aux personnes, physiques, technologiques), dont la gestion des identités, le contrôle d'accès et la sécurité physique des locaux ; ISO/IEC 27002 est le guide de mise en œuvre de ces mesures |
| Données personnelles | règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | les données sont limitées à ce qui est nécessaire (minimisation), conservées pendant une durée limitée et protégées par des mesures de sécurité appropriées ; les badges, les comptes et les journaux de passage ou de modification se rapportent à des personnes identifiées ; BRÉVALIM a désigné une déléguée à la protection des données, Mme Inès TALMONDIER ; aucune analyse juridique n'est attendue |
| Information de durabilité | directive (UE) 2022/2464 (CSRD), modifiée en 2025 et en 2026 ; règlement délégué (UE) 2026/1563 du 3 juillet 2026 (ESRS révisées) ; règlement délégué (UE) 2026/1560 (norme volontaire VSME) | les entreprises dans le champ de la CSRD établissent un état de durabilité selon les normes ESRS, fondé sur la double matérialité (impacts de l'entreprise sur l'environnement et les personnes, effets des enjeux de durabilité sur l'entreprise) et couvrant sa chaîne de valeur ; les ESRS révisées s'appliquent aux exercices ouverts à compter du 01/01/2027 ; la norme volontaire VSME permet à une entreprise hors du champ de présenter des informations de durabilité ; les groupes des trois entreprises installées de l'annexe 3.4 établissent leur état de durabilité conformément aux normes ESRS ; BRÉVALIM n'établit pas d'état de durabilité, et aucun assujettissement n'est à déterminer |

### Travail à faire

La facturation des contrats d'emplacement, qui porte l'essentiel du chiffre d'affaires, accumule les erreurs à quelques mois de l'émission des factures électroniques. Près d'un badge sur cinq appartient à une personne partie, et des comptes sont partagés. Des producteurs contestent l'attribution des emplacements du carreau, et le conseil d'administration veut un audit avant la saison d'été. Enfin, trois entreprises installées demandent chaque année des données de durabilité que BRÉVALIM rassemble à la main, pendant que le service de la communication propose 60 écrans d'affichage dynamique. Mme VAUCLERC vous demande d'analyser les risques de la facturation et d'en organiser les contrôles, de proposer le dispositif de gestion des badges et des comptes, de cadrer l'audit de l'attribution du carreau et de faire entrer la durabilité dans les décisions sur le système d'information. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – Les risques et la fiabilisation de la facturation (3,5 points)**

a) Après avoir présenté une typologie des risques liés aux systèmes d'information, identifiez quatre risques de la chaîne de facturation de l'annexe 3.1, formulés comme des événements redoutés, et classez-les selon cette typologie.

b) Après avoir défini la fiabilisation d'un système d'information comptable et décisionnel, proposez la cartographie des contrôles de la chaîne de facturation, du contrat d'emplacement au chiffre d'affaires présenté aux actionnaires : pour cinq points de contrôle, précisez le risque traité, le contrôle, sa nature (préventif ou détectif, manuel ou automatisé) et son responsable. L'un de ces contrôles rapproche l'occupation constatée des emplacements et les contrats facturés. Aucune règle comptable ni fiscale de la facturation n'est attendue.

c) Appréciez la probabilité et l'impact de vos quatre risques selon les échelles de l'annexe 3.1 D, puis indiquez les deux actions à mener en priorité avant l'émission des factures électroniques, en les justifiant.

**3.2 – La gestion des badges et des comptes (3,5 points)**

a) Après avoir défini la gestion des identités et des accès, proposez, à partir de l'annexe 3.2, le dispositif de gestion des badges et des comptes de BRÉVALIM : le cycle de vie des identités (arrivée, changement, départ) pour chacune des quatre populations de badges ; l'application du principe du moindre privilège aux zones d'accès du site et aux comptes ; la revue périodique des droits ; la fin des comptes partagés et génériques. Répondez aux objections de Mme DUCHÉRAN et de Mme GARBUSSAC. Aucun paramétrage d'équipement ni aucun test technique n'est attendu.

b) Présentez, dans un tableau, les rôles et les responsabilités dans ce dispositif de la direction générale, du responsable de la sûreté, du responsable des systèmes d'information, des directions métiers, des entreprises installées et des prestataires.

**3.3 – L'audit de l'attribution des emplacements du carreau (2 points)**

a) Après avoir défini l'audit d'un processus du système d'information, cadrez l'audit de l'attribution des emplacements du carreau que conduira l'auditeur externe : ses trois objectifs, son périmètre, ses étapes sur les quatre semaines de la mission et quatre preuves à demander, dont les journaux des modifications faites sur les tablettes.

b) Proposez trois critères d'appréciation de l'attribution, l'équité, la traçabilité et la fiabilité des données, en précisant pour chacun ce qui est attendu et ce que l'annexe 3.3 laisse craindre. Indiquez enfin deux facteurs de succès et deux points de vigilance propres à cet audit. Aucune analyse juridique n'est attendue.

**3.4 – Les données de durabilité, l'affichage dynamique et la gouvernance responsable du système d'information (4 points)**

a) Après avoir rappelé ce qu'est un état de durabilité établi conformément aux normes ESRS, expliquez, à partir des annexes 3.4 et 3.5, pourquoi des entreprises installées demandent des données de durabilité à BRÉVALIM, qui n'établit pas d'état de durabilité, et quel rôle le système d'information doit jouer dans leur collecte, leur traçabilité et leur fiabilité. Proposez trois mesures. Aucun assujettissement n'est à déterminer.

b) Après avoir défini la sobriété numérique, appréciez le projet d'affichage dynamique de l'annexe 3.4 B au regard de ce principe, puis proposez trois mesures. Aucun calcul d'empreinte n'est attendu.

c) Proposez une gouvernance du système d'information orientée vers la responsabilité sociétale de BRÉVALIM : l'instance, sa composition et son rôle, trois critères de durabilité à faire entrer dans les décisions sur les projets, et un indicateur de suivi précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
