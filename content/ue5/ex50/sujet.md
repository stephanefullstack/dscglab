# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 50

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES ACHETEURS ET DES FLUX, REVOIR LE PILOTAGE (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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
