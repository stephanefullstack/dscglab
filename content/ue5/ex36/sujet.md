# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 36

**DOSSIER 3 – SÉCURISER LES TRANSACTIONS ET MESURER L'IMPACT ENVIRONNEMENTAL DU NUMÉRIQUE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 12, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en avril 2027. ORSALIE est une société par actions simplifiée créée en 2015 à Lille par Mme Inès VELDRANE, qui en est la présidente et l'actionnaire majoritaire. Elle achète à des particuliers, ou vend pour leur compte en dépôt-vente, des articles de luxe d'occasion (maroquinerie, montres, bijoux, accessoires), qu'elle authentifie et remet en état dans son atelier lillois avant de les revendre sur son site marchand et son application, dans deux boutiques à Paris et à Lille et sur trois places de marché en ligne. En 2026, elle a vendu environ 96 000 articles à 70 000 clients de 40 pays, pour un montant de ventes de 48 millions d'euros, dont 52 % à l'étranger. Elle emploie 130 salariés, dont 35 authentificateurs et artisans ; la préparation et l'expédition des commandes sont confiées à un prestataire logistique. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « ORSALIE 2030 », adopté en janvier 2027, fixe cinq objectifs : doubler les ventes à l'étranger ; ouvrir en 2028 une place de marché sur laquelle des particuliers vendront directement à d'autres particuliers des articles authentifiés par l'atelier, contre une commission ; ramener de 21 à 7 jours le délai entre la réception d'un article et sa mise en vente ; protéger les clients et l'entreprise contre les contrefaçons et la fraude ; mesurer et réduire l'impact environnemental du numérique, en cohérence avec la promesse d'économie circulaire de la marque. Le site marchand, développé sur mesure en 2016 et devenu difficile à faire évoluer, doit être refondu avec une entreprise de services du numérique.

Vous êtes secrétaire général(e) d'ORSALIE depuis 2026, rattaché(e) à la présidente ; vous supervisez les finances, les ressources humaines, les achats et l'équipe numérique. Mme VELDRANE vous demande trois travaux : préparer la refonte du site et l'ouverture de la place de marché (dossier 1) ; organiser et exploiter les données des articles et des ventes (dossier 2) ; sécuriser les transactions et mesurer l'impact environnemental du numérique (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation d'ORSALIE et chiffres clés

ORSALIE est une société par actions simplifiée créée en 2015 à Lille par Mme Inès VELDRANE, sa présidente fondatrice et actionnaire majoritaire. Son siège et son atelier sont à Lille ; elle exploite deux boutiques, l'une à Paris, l'autre à Lille. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Le modèle d'activité**

- **Approvisionnement** : des particuliers confient leurs articles à ORSALIE en dépôt-vente (ORSALIE les vend pour leur compte et leur reverse le prix de vente diminué de sa commission) ou les lui vendent (ORSALIE les rachète et les revend pour son propre compte).
- **Authentification et remise en état** : chaque article, unique, est examiné par les authentificateurs de l'atelier de Lille, puis nettoyé ou réparé si nécessaire par les artisans ; les articles reconnus comme des contrefaçons ou jugés non conformes sont refusés.
- **Mise en vente** : l'équipe du catalogue photographie l'article, rédige sa fiche et fixe son prix.
- **Vente** : sur le site marchand et l'application d'ORSALIE, dans les deux boutiques et sur trois places de marché en ligne (désignées A, B et C) ; la préparation et l'expédition des commandes sont confiées à un prestataire logistique.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Ventes | 48 M€ ; environ 96 000 articles vendus, à un prix moyen d'environ 500 € ; environ 70 000 clients acheteurs dans 40 pays |
| Ventes par canal | site marchand et application : 70 % ; places de marché A, B et C : 15 % ; boutiques : 15 % |
| Ventes par catégorie | maroquinerie : 55 % ; montres : 25 % ; bijoux : 15 % ; accessoires : 5 % |
| Ventes par zone | France : 48 % ; étranger : 52 % (Union européenne, Royaume-Uni, Suisse, Moyen-Orient, Asie) |
| Approvisionnement | environ 110 000 articles reçus de 30 000 vendeurs particuliers, deux tiers en dépôt-vente et un tiers rachetés ; environ 6 % des articles présentés refusés comme contrefaçons ou non conformes |
| Délai de mise en vente | 21 jours en moyenne entre la réception d'un article et sa mise en vente |
| Dépenses du numérique | environ 2,4 M€ (5 % des ventes), dont la moitié pour l'équipe numérique |

**Effectif au 31/12/2026**

| Équipe | Effectif |
|---|---|
| Atelier : authentificateurs et artisans | 35 |
| Catalogue : photographie, rédaction des fiches, fixation des prix | 20 |
| Vendeurs en boutique et conseillers du service clients | 25 |
| Marketing et développement commercial | 15 |
| Équipe numérique : un responsable technique, quatre développeurs, deux personnes à l'exploitation et au support, deux chefs de produit, une analyste de données | 10 |
| Fonctions support : finances, ressources humaines, achats auprès des vendeurs, juridique | 25 |
| **Total** | **130** |

**Le système d'information en quelques lignes**

Le site marchand et l'application ont été développés sur mesure en 2016 par une agence aujourd'hui disparue ; ils forment une application d'un seul tenant, maintenue par l'équipe numérique et hébergée chez un hébergeur en nuage. ORSALIE utilise en outre un logiciel « maison » de gestion des dépôts, des rachats et des stocks, un logiciel de caisse dans les boutiques, des connecteurs vers les trois places de marché, les services d'un prestataire de paiement en ligne agréé, un outil de gestion de la relation client et des campagnes en ligne, un progiciel comptable et de paie, ainsi que des outils de bureautique et de messagerie en ligne.

**Organigramme simplifié (avril 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | présidente | Mme Inès VELDRANE |
| Rattaché(e) à la présidente | secrétaire général(e) : finances, ressources humaines, achats, équipe numérique | vous |
| Rattaché au (à la) secrétaire général(e) | responsable technique de l'équipe numérique | M. Hugo LAMBRESCOT |
| Rattaché à la présidente | directeur commercial : marketing et développement commercial, boutiques, places de marché | M. Damien ROCHAMBEL |
| Rattachée à la présidente | responsable de l'atelier | Mme Sabine VERCHAMP |
| Rattachée à la présidente | responsable du catalogue | Mme Clémence DUVERNAIS |
| Rattaché à la présidente | responsable du service clients | M. Karim BELLASTRE |

### ANNEXE 3.1 – Le reversement aux vendeurs en dépôt-vente (note de Mme Aurélie MONTCAZEL, responsable financière, mars 2027)

**A. Les règles du dépôt-vente**

Le contrat de dépôt-vente signé par chaque vendeur prévoit qu'ORSALIE conserve une commission de 30 % du prix de vente et reverse le solde au vendeur par virement **30 jours après la livraison de l'article à l'acheteur**. Ce délai couvre les 14 jours pendant lesquels, selon les conditions générales de vente d'ORSALIE, un acheteur en ligne peut retourner l'article : un article retourné est remis en vente et rien n'est dû au vendeur. En 2026, environ 64 000 articles en dépôt-vente ont été vendus et environ 22 M€ ont été reversés à quelque 18 000 vendeurs.

**B. Le processus actuel**

1. Chaque lundi, une comptable extrait du site la liste des articles livrés la semaine précédente (statut transmis par le prestataire logistique) et, du logiciel des dépôts, la liste des articles en dépôt-vente avec le vendeur, le prix de vente et ses coordonnées bancaires.
2. Elle rapproche les deux listes dans un tableur, à l'aide de la référence du site et du numéro de réception, calcule le montant dû à chaque vendeur et retient les articles livrés depuis plus de 30 jours. Les formules du tableur sont souvent corrigées à la main ; l'ancien tableur est écrasé chaque semaine.
3. Le service clients signale les retours à la comptable par courriel, quand il y pense.
4. La comptable saisit les virements sur le portail de la banque et les valide elle-même ; une seconde validation par la responsable financière n'est exigée qu'au-delà de 20 000 € par virement.
5. Un vendeur qui change de banque envoie ses nouvelles coordonnées bancaires par courriel ou les dicte par téléphone au service clients, qui les saisit dans le logiciel des dépôts ; aucun contrôle n'est fait et le logiciel ne garde pas trace de l'auteur de la modification.
6. Le progiciel comptable reçoit chaque mois le seul total des virements, sans le détail par vendeur.

**C. Les constats de l'année 2026**

| Constat | Nombre | Montant |
|---|---|---|
| Reversements en double (même article payé deux fois après une correction du tableur) | 200 | 70 k€, dont 30 k€ récupérés auprès des vendeurs |
| Reversements effectués avant la fin du délai de retour, l'article ayant ensuite été retourné par l'acheteur | 400 | 140 k€, dont 60 k€ récupérés |
| Modifications de coordonnées bancaires | 2 500, dont aucune vérifiée | 6 reversements, soit 15 k€, versés sur les comptes de fraudeurs qui se faisaient passer pour des vendeurs |
| Sommes dues aux vendeurs au 31/12/2026 | — | 2 750 k€ selon le logiciel des dépôts, 2 600 k€ selon la comptabilité : écart de 150 k€ non expliqué |
| Délai moyen de reversement | — | 45 jours après la livraison, contre 30 jours prévus au contrat |
| Réclamations de vendeurs au service clients pour un reversement en retard ou erroné | 2 000 | — |

La préparation des reversements occupe une comptable à temps plein et la moitié du temps d'une autre.

**D. La demande de la présidente**

« Sur la place de marché, nous reverserons demain leur part à des dizaines de milliers de particuliers. Avant de reprendre ce processus, je veux un audit de nos reversements, conduit par vous avec la responsable financière, et ses conclusions fin juillet 2027. »

### ANNEXE 3.2 – Le projet de séquestre programmable et de règlement en jetons (proposition de la société SCELLIDE, jeune entreprise lyonnaise, et avis recueillis en mars 2027)

**A. Le séquestre programmable pour les ventes entre particuliers de la place de marché**

« Sur votre place de marché, l'acheteur paiera par carte sur votre site. Le prestataire de paiement nous versera le montant, que nous convertirons en jetons de monnaie électronique adossés à l'euro (un jeton vaut un euro), émis par un établissement de monnaie électronique agréé. Les jetons seront bloqués dans un **contrat intelligent**, programme inscrit sur une **chaîne de blocs publique** dont la validation repose sur la preuve d'enjeu. Le contrat libérera les fonds automatiquement quand deux conditions seront remplies : votre atelier aura enregistré que l'article est authentique et conforme à l'annonce, et l'acheteur aura confirmé la réception dans l'application (ou sept jours après la livraison, sans réclamation). La commission d'ORSALIE et la part du vendeur seront alors versées en même temps ; le vendeur recevra des euros sur son compte bancaire sous 48 heures, après conversion par un prestataire de services sur crypto-actifs agréé, notre partenaire. Si l'atelier enregistre que l'article n'est pas authentique, l'acheteur est remboursé automatiquement.

Pour une transparence totale, chaque vente (identifiants de l'acheteur et du vendeur, prix, photographies de l'article, résultat de l'authentification) sera inscrite sur la chaîne, consultable par tous et impossible à modifier. La chaîne de blocs rend toute fraude impossible et garantit l'authenticité des articles. »

Précisions obtenues par M. Hugo LAMBRESCOT, responsable technique, auprès de SCELLIDE :
- une fois libérés, les fonds ne peuvent plus être repris par le contrat : un litige ultérieur (défaut découvert après la confirmation de la réception) devra être réglé par ORSALIE, hors du contrat intelligent ;
- toute modification des règles (délai de sept jours, partage d'une vente entre plusieurs vendeurs) suppose qu'un nouveau contrat intelligent soit écrit et publié par SCELLIDE, en trois semaines environ ;
- SCELLIDE n'est pas elle-même prestataire de services sur crypto-actifs.

**B. Le règlement en jetons pour les négociants professionnels étrangers**

Une quarantaine de négociants professionnels du Moyen-Orient et d'Asie achètent sur le site d'ORSALIE, par lots, environ 4 M€ d'articles par an. Ils paient par virement international : les fonds arrivent en deux à cinq jours, ORSALIE n'expédie qu'après leur réception et supporte environ 40 k€ de frais bancaires et de change par an. SCELLIDE propose qu'ils paient en jetons de monnaie électronique adossés à l'euro : les jetons arriveraient en quelques minutes, tous les jours de l'année ; ils seraient conservés pour le compte d'ORSALIE par le prestataire de services sur crypto-actifs partenaire, qui les convertirait en euros sur demande. Frais annoncés : 0,25 % des sommes reçues et un abonnement de 5 k€ par an. Douze des quarante négociants déclarent utiliser déjà de tels jetons.

**C. Comparaison avec la solution classique (estimations de M. LAMBRESCOT pour les ventes entre particuliers)**

Dans la solution classique, le prestataire de paiement agréé d'ORSALIE, qui applique déjà l'authentification forte exigée par la réglementation des paiements, conserve les fonds de l'acheteur sur un compte dédié et les verse au vendeur et à ORSALIE sur instruction d'ORSALIE, quand l'atelier a validé l'article et que l'acheteur a confirmé la réception.

| | Séquestre programmable (SCELLIDE) | Séquestre tenu par le prestataire de paiement agréé |
|---|---|---|
| Ventes entre particuliers prévues | 30 000 en 2028, 150 000 en 2030 | idem |
| Mise en place (raccordement au site et au logiciel de l'atelier) | 300 k€ | 60 k€ |
| Coûts annuels (abonnement, frais de chaîne et de conversion, ou commissions du prestataire) | 150 k€ par an | 80 k€ par an |
| Versement au vendeur après la confirmation de la réception | sous 48 heures | sous deux jours ouvrés |
| Modification des règles de libération | nouveau contrat intelligent écrit par SCELLIDE (trois semaines) | réglage par ORSALIE dans l'espace du prestataire (une journée) |
| Remboursement de l'acheteur après le versement au vendeur | impossible par le contrat ; à la charge d'ORSALIE | possible tant que le vendeur n'a pas été payé ; ensuite à la charge d'ORSALIE |

**D. Avis recueillis**

- **M. Damien ROCHAMBEL, directeur commercial** : « Le mot "blockchain" rassurera nos acheteurs d'Asie, et les négociants veulent être servis plus vite. »
- **Mme Sabine VERCHAMP, responsable de l'atelier** : « Mes authentificateurs se trompent rarement, mais ils se trompent : en 2026, 30 articles que nous avions authentifiés se sont révélés être des contrefaçons après la vente. »
- **M. Hugo LAMBRESCOT** : « Personne dans l'équipe ne connaît les chaînes de blocs, et c'est nous qui enverrons au contrat le résultat de l'authentification. »

### ANNEXE 3.3 – La fraude sur le site et sur la future place de marché (note de M. Karim BELLASTRE, responsable du service clients, et constats de M. Hugo LAMBRESCOT, avril 2027)

**A. Les fraudes constatées en 2026**

| Fraude | Cas en 2026 | Pertes pour ORSALIE |
|---|---|---|
| Paiements par carte contestés par le titulaire de la carte (carte volée, surtout des cartes émises hors de l'Union européenne) | 400 | 200 k€ |
| Comptes de clients piratés : connexion avec un mot de passe dérobé, avoir utilisé ou commande livrée à une autre adresse | 300 comptes | 60 k€ |
| Réclamations « article non reçu » alors que le transporteur a prouvé la livraison | 250 | 125 k€ |
| Retours d'une contrefaçon à la place de l'article original vendu (montres, sacs) | 60 | 150 k€ |
| Contrefaçons présentées par des vendeurs : 6 600 articles refusés par l'atelier comme contrefaçons ou non conformes, mais 30 contrefaçons non détectées, vendues puis remboursées | 30 | 45 k€, sans compter l'atteinte à l'image de la marque |
| **Total** | | **580 k€** |

Sur la place de marché, les vendeurs particuliers publieront eux-mêmes leurs annonces et recevront leurs fonds ; l'atelier continuera d'examiner chaque article avant sa livraison à l'acheteur.

**B. Les règles actuelles**

Quinze règles fixes sont appliquées aux commandes passées sur le site (par exemple : commande de plus de 3 000 € livrée dans un pays différent de celui de la carte ; plus de trois commandes en une heure depuis le même compte). Les commandes concernées sont bloquées et vérifiées une à une par deux conseillers du service clients, en heures ouvrées. En 2026, sur environ 65 000 commandes passées sur le site, 12 000 ont été bloquées, dont 480 étaient frauduleuses ; le délai moyen de vérification a été de 20 heures et 1 200 clients ont annulé leur commande pendant l'attente. Les règles ont laissé passer les 400 paiements frauduleux du tableau A.

**C. L'outil de détection proposé par un éditeur spécialisé (abonnement de 90 k€ par an)**

- Un **score de risque** de 0 à 100 est attribué à chaque commande, à chaque connexion et, demain, à chaque annonce, par un modèle d'apprentissage automatique entraîné sur les transactions des autres clients de l'éditeur (surtout des sites européens de mode), puis sur l'historique d'ORSALIE.
- Une **analyse des photographies** des annonces les compare à des photographies d'articles authentiques et repère les photographies copiées sur d'autres sites.
- Réglage proposé par l'éditeur : commande refusée automatiquement au-delà d'un score de 80 ; annonce retirée et compte du vendeur suspendu automatiquement au-delà de 70, sans intervention d'un conseiller.
- Essai rejoué sur les commandes de novembre et décembre 2026 : 85 % des paiements frauduleux auraient été détectés, et 3 % des commandes légitimes auraient été bloquées : 2 % pour les clients domiciliés en Europe, 9 % pour ceux du Moyen-Orient et d'Asie.
- Essai sur 500 photographies de contrefaçons conservées par l'atelier : 70 % ont été signalées. L'outil n'examine pas l'article lui-même.
- L'éditeur ne communique pas les raisons d'un score (« secret de fabrication »).
- Pour s'améliorer, l'outil a besoin que chaque fraude confirmée lui soit signalée. Aujourd'hui, le service clients note les fraudes dans un tableur, en texte libre, et ne distingue pas les retours de contrefaçons des autres retours.

**D. Les accès au site et leur surveillance (constats de M. LAMBRESCOT)**

- **Clients** : le compte est protégé par un mot de passe seul, de six caractères au minimum, sans limite du nombre d'essais. Un samedi soir de novembre 2026, 40 000 tentatives de connexion ont été faites avec des identifiants dérobés sur d'autres sites ; 300 comptes ont été ouverts. L'attaque n'a été découverte que le lundi matin : personne ne surveille le site la nuit ni le week-end.
- **Paiement** : le prestataire de paiement agréé applique l'authentification forte exigée par la réglementation des paiements ; ORSALIE ne conserve aucun numéro de carte. En revanche, un client connecté peut utiliser ses avoirs et changer l'adresse de livraison sans nouvelle vérification.
- **Vendeurs en dépôt-vente** : un espace en ligne, protégé par un mot de passe seul, leur permet de suivre leurs articles et leurs reversements.
- **Administration du site** (commandes, remboursements, avoirs, prix, fiches des articles) : accessible depuis Internet avec un mot de passe seul ; 60 comptes, dont 3 comptes partagés par les quatre développeurs, qui ont tous les droits, y compris sur la base des clients en exploitation. Aucune trace des actions n'est conservée : personne ne sait qui a accordé 25 avoirs de 500 € en octobre 2026.
- **Organisation technique** : les pages du site, l'administration, la base des clients et la fonction de remboursement forment une seule application, dans un même environnement chez l'hébergeur en nuage. Les échanges entre le navigateur des clients et le site sont chiffrés ; la base des clients et les copies de pièces d'identité des vendeurs (exigées pour le rachat) ne le sont pas.
- **Sauvegardes** : une sauvegarde quotidienne de la base, conservée sur le même compte de l'hébergeur ; aucune restauration n'a jamais été essayée.

### ANNEXE 3.4 – Le site et son impact environnemental (premières mesures de M. Hugo LAMBRESCOT et projet du marketing, mars 2027)

**A. L'usage du site et de l'application en 2026**

- 30 millions de visites et 150 millions de pages vues, dont 60 % sur smartphone ; environ 1 500 téraoctets de données transférées depuis l'hébergeur.
- Une fiche d'article affiche jusqu'à 40 photographies en haute définition, toutes chargées dès l'ouverture de la page, et une vidéo de 30 secondes lue automatiquement : une page d'article pèse en moyenne 12 mégaoctets et appelle 160 éléments.
- Les photographies et vidéos de tous les articles depuis 2016, y compris ceux qui ont été vendus (environ 700 000), sont conservées en trois formats et ne sont jamais supprimées : 80 téraoctets en 2027, deux fois plus qu'en 2024.
- L'application ne fonctionne que sur les smartphones de moins de quatre ans ; des clients s'en plaignent régulièrement.

**B. Les premières mesures disponibles (ordres de grandeur)**

| Mesure | Résultat |
|---|---|
| EcoIndex de dix pages types (mars 2027) | page d'accueil : G ; fiche d'article : G ; liste de résultats : F ; panier : D ; moyenne des dix pages : F |
| Consommation électrique et émissions attribuées à ORSALIE par l'hébergeur pour 2026 | 180 MWh et 30 tonnes équivalent CO2, selon un rapport annuel dont la méthode n'est pas communiquée |
| Équipements | 90 ordinateurs portables (un par salarié de bureau) renouvelés tous les trois ans ; les sept photographes du catalogue disposent d'écrans et d'appareils renouvelés tous les deux ans |

Aucune mesure ne porte sur les terminaux des clients ni sur les réseaux.

**C. Le projet du marketing et les avis recueillis**

- **M. Damien ROCHAMBEL, directeur commercial** : « Dès juin 2027, je veux afficher un badge "site éco-conçu" en bas de chaque page et lancer une campagne "Le luxe circulaire, jusque dans nos pages". C'est cohérent avec notre promesse. »
- **Mme Clémence DUVERNAIS, responsable du catalogue** : « Nos acheteurs veulent voir chaque rayure avant d'acheter un sac de 2 000 € : moins de photographies, ce seront plus de retours. »
- **M. Hugo LAMBRESCOT** : « La refonte du site est l'occasion de reprendre le poids des pages ; aujourd'hui, personne n'en est chargé. »

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2023/1114 sur les marchés de crypto-actifs (MiCA) | Encadre l'offre au public de crypto-actifs, l'émission de jetons stables, dont les jetons de monnaie électronique (qui visent à conserver une valeur stable en se référant à une seule monnaie officielle et dont l'émetteur doit être agréé comme établissement de crédit ou établissement de monnaie électronique), ainsi que l'agrément et les obligations des prestataires de services sur crypto-actifs (conservation pour le compte de clients, échange contre des fonds, etc.). Il ne traite ni de la comptabilité ni de la fiscalité de ces actifs, qui relèvent d'autres règles. | Applicable depuis le 30/12/2024 (jetons stables depuis le 30/06/2024). La période transitoire des prestataires enregistrés sous l'ancien régime français a pris fin le 01/07/2026 : depuis le 02/07/2026, seuls les prestataires agréés selon MiCA peuvent exercer. |
| ISO 22739:2024 | Norme qui fixe le vocabulaire des chaînes de blocs et des technologies de registres distribués (bloc, nœud, consensus, contrat intelligent, jeton…). | 2e édition, janvier 2024 |
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Les données sont limitées à ce qui est nécessaire (minimisation) et la personne peut en obtenir l'effacement dans les cas prévus. Une personne a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé, y compris le profilage, qui produit des effets juridiques à son égard ou l'affecte de manière significative de façon similaire ; lorsqu'une telle décision est admise, notamment parce qu'elle est nécessaire à la conclusion ou à l'exécution d'un contrat, la personne peut obtenir une intervention humaine, exprimer son point de vue et contester la décision. Un traitement susceptible d'engendrer un risque élevé (évaluation ou notation de personnes à grande échelle, par exemple) est précédé d'une analyse d'impact. | Applicable depuis le 25/05/2018 |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | Depuis le 2 février 2025, les organisations qui utilisent des systèmes d'IA prennent des mesures pour assurer un niveau suffisant de maîtrise de l'IA à leur personnel. Les obligations relatives aux systèmes d'IA à haut risque de l'annexe III s'appliqueront à compter du 2 décembre 2027. | En vigueur, application échelonnée |
| ISO/IEC 27001:2022 et ISO/IEC 27002:2022 | La première spécifie les exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation des risques, avec 93 mesures en annexe A (dont le contrôle d'accès, l'authentification, la journalisation, la surveillance, la sauvegarde, la cryptographie) ; la seconde est le guide de mise en œuvre de ces mesures. | En vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | 42 mesures de bonnes pratiques, dont l'identification nominative de chaque utilisateur, l'authentification renforcée des comptes d'administration, la séparation des usages d'administration, la journalisation et la sauvegarde. | En vigueur |
| Loi n° 2021-1485 du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique en France (REEN) | Sensibilisation au numérique responsable, allongement de la durée de vie des équipements, écoconception des services numériques, centres de données et réseaux moins énergivores. | En vigueur |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | Critères d'écoconception regroupés par thèmes (stratégie, spécifications, architecture, expérience utilisateur, contenus, interface, serveur, hébergement…), dont l'usage du service sur des équipements anciens et la publication d'une déclaration d'écoconception. | Version 2 publiée le 17/05/2024 |
| EcoIndex | Indicateur de la performance environnementale d'une page web, noté de A à G, calculé à partir de la complexité de la page, du poids des données transférées et du nombre de requêtes ; ce n'est pas une mesure de l'empreinte complète du service. | Outil en ligne |

Il n'est demandé aucune analyse juridique, fiscale ou comptable.

### Travail à faire

Avant d'ouvrir sa place de marché, ORSALIE doit fiabiliser les reversements à ses vendeurs, choisir la manière de sécuriser les fonds des ventes entre particuliers, lutter contre une fraude qui lui a coûté 580 k€ en 2026, protéger les accès à son site et mesurer l'impact environnemental de pages devenues très lourdes. Mme VELDRANE vous demande de préparer l'audit des reversements, d'apprécier la proposition de SCELLIDE, d'analyser la fraude et l'outil de détection proposé, de concevoir l'architecture de confiance du site et de proposer une démarche de mesure et de réduction de son impact environnemental. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – L'audit du processus de reversement aux vendeurs (2 points)**

a) Après avoir défini l'audit d'un processus du système d'information, présentez la démarche de l'audit demandé par la présidente (étapes et livrables dans le calendrier fixé). Représentez ensuite, sous la forme d'un tableau, trois étapes du processus de reversement : pour chacune, l'acteur, l'application, le risque et le contrôle interne attendu. Indiquez enfin deux tests que vous mènerez, chacun relié à un constat de l'annexe 3.1. Les diligences attendues sont des rapprochements, des sondages, des entretiens et des observations.

b) Proposez quatre critères de performance et de conformité au regard desquels l'audit appréciera le processus ; pour chacun, précisez ce qui est attendu et appréciez la situation actuelle à partir des constats de l'annexe 3.1.

**3.2 – Le projet de séquestre programmable et de règlement en jetons (2,5 points)**

a) Après avoir défini une chaîne de blocs et un contrat intelligent, expliquez comment fonctionnerait le séquestre programmable proposé par SCELLIDE pour une vente entre particuliers, du paiement de l'acheteur au versement au vendeur, en précisant ce que la chaîne de blocs garantit et ce qu'elle ne garantit pas. Aucune description technique au-delà des principes n'est attendue.

b) À l'aide d'une grille d'opportunité, appréciez le projet de séquestre programmable face à la solution classique : deux apports, quatre limites tirées de l'annexe 3.2 (dont le coût sur trois ans des deux solutions), puis votre recommandation argumentée.

c) D'après les repères de l'annexe 3.5, indiquez deux éléments du règlement en jetons des négociants que le règlement MiCA encadre, et deux questions qu'il n'encadre pas, en précisant pour chacun la conséquence pratique pour ORSALIE.

**3.3 – La fraude et l'apport de l'intelligence artificielle (3 points)**

a) Après avoir présenté une typologie des risques liés aux systèmes d'information, classez les cinq fraudes de l'annexe 3.3 A et un risque nouveau propre à la place de marché, en précisant pour chacun le maillon du parcours ou du système d'information exploité par le fraudeur.

b) Après avoir distingué l'apprentissage automatique de l'IA générative, appréciez l'outil de détection proposé : deux apports par rapport aux règles actuelles, puis quatre limites ou risques (faux positifs, biais, explicabilité, place de la décision humaine, données nécessaires), en vous appuyant sur l'essai de l'annexe 3.3 C et sur les repères de l'annexe 3.5. Le fonctionnement interne du modèle n'est pas attendu.

c) Proposez trois mesures de traitement des risques de fraude, autres que celles qui relèvent de l'architecture de confiance (question 3.4), chacune reliée à une fraude de l'annexe 3.3 A et assortie de son responsable.

**3.4 – L'architecture de confiance et la surveillance du site (3 points)**

a) Après avoir défini l'architecture de confiance, proposez celle du site et de la future place de marché, en principe : l'authentification des clients, des vendeurs et des administrateurs, le chiffrement des données et le cloisonnement des fonctions de paiement, de remboursement et d'administration. Reliez chaque proposition à un constat de l'annexe 3.3. Aucun paramétrage n'est attendu.

b) Proposez les dispositifs de surveillance et de résilience qui manquent aujourd'hui : la gestion des identités et des accès, la journalisation, la supervision et les sauvegardes. Pour chacun, indiquez ce qu'il change au regard des constats de l'annexe 3.3. Le contenu détaillé des plans de continuité et de reprise n'est pas attendu.

**3.5 – La mesure et la réduction de l'impact environnemental du site (2,5 points)**

a) Proposez une démarche de mesure de l'impact environnemental du site et de l'application, puis deux indicateurs de suivi, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Aucun calcul d'empreinte n'est attendu.

b) Après avoir défini l'écoconception d'un service numérique, proposez quatre mesures d'écoconception ou de bonnes pratiques adaptées à l'annexe 3.4, en tenant compte de l'objection de la responsable du catalogue.

c) Indiquez à quelles conditions le marketing pourrait afficher un « site éco-conçu ».
