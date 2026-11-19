# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 35

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES ARTICLES ET DES VENTES (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 2.1 – Les données des articles aujourd'hui (note de Mme Clémence DUVERNAIS, responsable du catalogue, et témoignages recueillis en avril 2027)

**A. Un article unique, décrit trois fois**

Chaque article est un exemplaire unique : un sac, une montre ou un bijou n'est vendu qu'une fois. Il est pourtant décrit dans trois logiciels, par trois équipes.

| Où l'article est décrit | Ce qui est saisi | Par qui | Numéro de l'article |
|---|---|---|---|
| Logiciel « maison » de gestion des dépôts, des rachats et des stocks | vendeur, date de réception, dépôt-vente ou rachat, catégorie, marque et modèle, état noté par l'atelier, emplacement en stock, prix convenu avec le vendeur | accueil de l'atelier et authentificateurs | numéro de réception, attribué à chaque arrivée : un article retourné par un client puis remis en vente reçoit un nouveau numéro |
| Site marchand et application | fiche de l'article : titre, marque, modèle, matière, couleur, dimensions, état, description en français et en anglais, prix, photographies | rédacteurs du catalogue, qui ressaisissent les informations du logiciel des dépôts | référence du site, attribuée à la mise en ligne |
| Connecteurs vers les places de marché A, B et C | annonce adaptée aux catégories, aux champs et à l'échelle d'état de chaque place de marché | rédacteurs du catalogue, qui complètent à la main les champs propres à chaque place de marché | référence attribuée par chaque place de marché |

**B. Les constats de mars 2027**

- **Marques et modèles** : ils sont saisis en texte libre. Le logiciel des dépôts compte 2 300 libellés de marque différents pour environ 400 marques réelles ; le modèle de sac le plus vendu d'une maison de maroquinerie parisienne y apparaît sous 17 libellés différents (abréviations, fautes de frappe, nom du modèle en français ou en anglais).
- **État de l'article** : un contrôle de 500 fiches publiées sur le site en mars 2027 a montré que 100 d'entre elles affichaient un état plus favorable que celui noté par l'atelier.
- **Authentification** : le résultat (« authentique », « refusé », « second avis demandé »), le nom de l'authentificateur et ses observations sont saisis dans un tableur partagé, une ligne par numéro de réception ; le logiciel des dépôts n'en garde aucune trace. Le site affiche « authentifié par ORSALIE » pour tout article en ligne. En septembre 2026, le tableur a été écrasé par une copie erronée : deux jours de résultats ont été ressaisis à partir des notes papier des authentificateurs.
- **Photographies** : elles sont rangées dans les dossiers d'un espace de stockage partagé, nommés d'après le numéro de réception, puis renommées à la main lors de leur chargement sur le site. Quand un article retourné par un client reçoit un nouveau numéro de réception, ses photographies et son historique (état, authentification) ne lui sont plus rattachés.
- **Disponibilité** : le site, les boutiques et les places de marché proposent les mêmes articles. Le site enregistre ses ventes en temps réel ; les boutiques signalent les leurs au catalogue par messagerie ; les connecteurs transmettent aux places de marché, chaque nuit, un fichier des articles disponibles. En 2026, 900 articles ont été vendus deux fois (annexe 2.2 B) : la seconde commande a été annulée et le client remboursé.
- **Places de marché** : chacune impose ses catégories, ses champs, son échelle d'état et son format. Les places de marché A et C proposent une interface de programmation (API) documentée, qui permet de publier une annonce et de mettre à jour sa disponibilité à tout moment ; ORSALIE ne l'utilise pas. La place de marché B n'accepte que des fichiers, mais admet depuis 2026 un format ouvert et un dépôt jusqu'à une fois par heure.
- **Données des vendeurs** : le fichier transmis chaque nuit à la place de marché B contient, pour chaque article, le nom et la commune du vendeur particulier, que la place de marché B n'utilise pas.
- **Responsabilités** : personne n'est chargé des données des articles. Chaque équipe corrige dans son logiciel les erreurs qu'elle voit, sans prévenir les autres.
- **Demain** : à partir de 2028, les vendeurs particuliers publieront eux-mêmes leurs annonces sur la place de marché d'ORSALIE ; l'article ne sera envoyé à l'atelier et authentifié qu'après sa vente.

**C. Témoignages**

- **Mme Clémence DUVERNAIS, responsable du catalogue** : « Mes rédacteurs ressaisissent dans le site ce que l'atelier a déjà saisi, puis le recopient pour chaque place de marché. Quand l'atelier corrige une marque, la fiche du site ne change pas. Et le nombre d'articles "disponibles" n'est jamais le même : le logiciel des dépôts compte tous les articles reçus et non vendus, même ceux qui attendent l'authentification ; le site, ceux qui sont en ligne et ne sont pas dans le panier d'un client ; les places de marché, ceux du fichier de la nuit précédente. »
- **Mme Sabine VERCHAMP, responsable de l'atelier** : « Nos authentificateurs notent l'état de 1 à 5, avec un commentaire libre. Le catalogue le traduit en quatre mentions ("neuf", "très bon état", "bon état", "état correct"), et les places de marché A, B et C utilisent trois, cinq et six niveaux. Pour les montres, un seul horloger fait à la fois l'authentification et le contrôle du fonctionnement. »
- **Mme Léa CORVENNAT, analyste de données** : « La "date de mise en vente" n'a pas le même sens partout : pour le logiciel des dépôts, c'est la date à laquelle l'atelier a terminé son travail ; pour le site, la date de publication de la fiche ; pour les places de marché, la date de publication de l'annonce, de un à dix jours plus tard. Je ne peux donc pas comparer les délais d'un canal à l'autre. »
- **M. Damien ROCHAMBEL, directeur commercial** : « Chaque vente annulée sur une place de marché nous vaut une pénalité et une mauvaise note. En novembre 2026, la place de marché B a suspendu notre compte pendant huit jours, parce que notre taux d'annulation dépassait son seuil. »
- **M. Karim BELLASTRE, responsable du service clients** : « Un tiers des retours viennent d'une fiche inexacte : une couleur, une rayure, une dimension. Et quand un client demande la preuve de l'authentification de son article, mes conseillers la cherchent dans le tableur de l'atelier. »
- **M. Hugo LAMBRESCOT, responsable technique** : « Les connecteurs ont été écrits en 2016 pour des fichiers de nuit. Les API des places de marché A et C existent depuis longtemps ; nous n'avons jamais eu le temps de nous en servir. »

### ANNEXE 2.2 – Les délais de vente et les retours en 2026 (relevé de Mme Léa CORVENNAT, analyste de données, mars 2027)

**A. Par catégorie**

| Catégorie | Articles mis en vente en 2026 | Délai moyen de mise en vente (de la réception à la mise en vente) | Délai moyen de vente (de la mise en vente à la vente) | Part des articles invendus 90 jours après leur mise en vente | Taux de retour des ventes en ligne | Premier motif de retour |
|---|---|---|---|---|---|---|
| Maroquinerie | 55 000 | 17 jours | 30 jours | 10 % | 13 % | article différent de la fiche |
| Montres | 15 000 | 35 jours | 60 jours | 25 % | 6 % | défaut de fonctionnement |
| Bijoux | 20 000 | 25 jours | 45 jours | 20 % | 9 % | taille |
| Accessoires | 10 000 | 14 jours | 40 jours | 15 % | 10 % | changement d'avis |
| **Ensemble** | **100 000** | **21 jours** | — | — | — | — |

Les délais sont calculés à partir de la date de réception enregistrée dans le logiciel des dépôts et de la date de publication de la fiche sur le site ; la date de réception est parfois saisie plusieurs jours après l'arrivée du colis. La part des invendus ne porte que sur les articles mis en vente avant le 1er octobre 2026.

**B. Par canal de vente**

| Canal | Articles vendus en 2026 | Délai moyen de vente | Taux de retour | Ventes annulées (article déjà vendu sur un autre canal) |
|---|---|---|---|---|
| Site marchand et application | 66 000 | 35 jours | 10 % | 300 |
| Places de marché A, B et C | 16 000 | 20 jours (1) | 15 % (2) | 600 |
| Boutiques | 14 000 (3) | 50 jours | non mesuré (3) | — |
| **Total** | **96 000** | — | — | **900** |

(1) Délai compté à partir de la publication de l'annonce sur la place de marché, qui intervient de un à dix jours après la mise en ligne sur le site ; la place de marché C n'a transmis ses données que d'avril à décembre 2026.
(2) Les places de marché comptent comme retour toute réclamation ouverte par un acheteur, même si l'article n'est pas renvoyé.
(3) Les boutiques n'acceptent que des échanges, qui ne sont pas enregistrés ; à la suite d'une panne, le logiciel de caisse de la boutique de Paris n'a transmis aucune vente pour le mois d'août 2026.

**C. Les motifs des 9 000 retours des ventes en ligne**

| Motif | Retours |
|---|---|
| Article différent de la fiche (état, couleur, dimensions, matière) | 3 000 |
| Changement d'avis | 2 700 |
| Taille ou dimensions ne convenant pas | 1 800 |
| Défaut de fonctionnement (montres surtout) | 900 |
| Article abîmé pendant le transport | 400 |
| Autres ou non renseigné | 200 |
| **Total** | **9 000** |

Le motif était saisi en texte libre par le service clients jusqu'en juin 2026, puis choisi dans une liste ; l'analyste a classé à la main les motifs du premier semestre. Un retour entraîne en moyenne environ 40 € de dépenses pour ORSALIE (transport aller et retour facturé par le prestataire logistique, emballage, frais de remboursement), sans compter le temps de l'atelier et du catalogue pour contrôler l'article et le remettre en ligne, ni la vente perdue.

**D. Où passent les 21 jours de la mise en vente** (échantillon de 1 000 articles reçus en février 2027, d'après les dates du logiciel des dépôts, du tableur de l'atelier et des dossiers de photographies)

| Étape | Durée moyenne |
|---|---|
| Attente avant l'authentification | 6 jours |
| Authentification | 1 jour |
| Remise en état (40 % des articles ; durée ramenée à l'ensemble des articles) | 4 jours |
| Attente avant la photographie | 5 jours |
| Photographie, rédaction de la fiche et fixation du prix | 3 jours |
| Validation et publication sur le site (les places de marché suivent ensuite) | 2 jours |
| **Total** | **21 jours** |

**E. La question de la présidente**

Mme Inès VELDRANE : « Nous voulons ramener le délai de mise en vente de 21 à 7 jours et doubler nos ventes à l'étranger. Avant de décider des investissements, je veux savoir où nous perdons du temps et de l'argent. »

### ANNEXE 2.3 – Les outils d'analyse (note de Mme Léa CORVENNAT, analyste de données, et attentes recueillies en avril 2027)

**A. La situation**

- Chaque mois, je prépare le rapport des ventes et des stocks : un classeur de tableur de douze onglets, construit à partir d'extractions du logiciel des dépôts, du site, du logiciel de caisse, des fichiers des places de marché et de l'outil de gestion de la relation client. Il me prend quatre jours et part vers le 15 du mois suivant.
- En 2026, j'ai reçu 150 demandes d'extraction des responsables ; j'y réponds en six jours en moyenne. Chacun retravaille ensuite les données dans son propre tableur.
- Pour mars 2027, trois montants des ventes circulent : 3,8 M€ pour les finances (ventes enregistrées, retours déduits), 4,2 M€ pour le commerce (commandes passées, y compris celles qui ont été annulées), 4,0 M€ pour le catalogue (articles passés au statut « vendu »).
- Je suis la seule à connaître les règles de préparation des données ; elles ne sont écrites nulle part.

**B. Les attentes**

- **M. Damien ROCHAMBEL, directeur commercial** : « Je veux voir chaque matin les ventes de la veille par canal et par pays, sans attendre le rapport. »
- **Mme Clémence DUVERNAIS, responsable du catalogue** : « Je veux suivre chaque semaine les articles en attente à chaque étape et le délai par catégorie. »
- **Mme Sabine VERCHAMP, responsable de l'atelier** : « Je veux savoir combien d'articles attendent l'authentification, et depuis quand. »
- **Mme Inès VELDRANE, présidente** : « Je veux quelques chiffres sûrs chaque semaine, les mêmes pour tout le monde. »

**C. Deux options proposées par M. Hugo LAMBRESCOT, responsable technique**

| | Option 1 : outil décisionnel en libre-service relié aux données | Option 2 : tableaux de bord intégrés aux logiciels existants |
|---|---|---|
| Principe | service en ligne d'un éditeur, relié par des connecteurs au logiciel des dépôts, au site, au logiciel de caisse, aux places de marché et à l'outil de gestion de la relation client ; une base d'analyse commune, alimentée chaque nuit, puis toutes les heures ; l'analyste prépare et documente des jeux de données « certifiés », à partir desquels chaque responsable compose ses propres analyses et tableaux de bord | écrans de statistiques déjà fournis par le logiciel de caisse, l'outil de gestion de la relation client et les espaces vendeurs des places de marché ; six écrans de statistiques ajoutés au logiciel des dépôts et au site par l'équipe numérique |
| Coût | mise en place : 90 k€ (préparation et rapprochement des données : 60 k€ ; paramétrage : 20 k€ ; formation des utilisateurs : 10 k€) ; abonnement : 20 k€ par an pour 25 utilisateurs | développement : 30 k€ ; maintenance : 10 k€ par an |
| Délai | quatre mois | trois mois, quand l'équipe numérique, mobilisée par la refonte du site, sera disponible |
| Points d'attention | chaque responsable pourra créer ses propres indicateurs ; les données ne seront pas plus justes que celles des logiciels qui les produisent | chaque logiciel calcule ses chiffres selon ses propres définitions ; aucune vue ne croise les canaux ni les étapes de la mise en vente ; les écrans du site devront être refaits après la refonte |

### ANNEXE 2.4 – Le projet de studio de mise en ligne (note de Mme Clémence DUVERNAIS, responsable du catalogue, avril 2027)

**A. Aujourd'hui**

- Les 20 personnes du catalogue, dont sept photographes, photographient les articles, rédigent les fiches, fixent les prix et gèrent les annonces des places de marché. En 2026, 100 000 articles ont été mis en vente.
- La photographie et sa retouche prennent en moyenne 7 minutes par article, la rédaction de la fiche en français et en anglais 5 minutes : 12 minutes au total. Le coût horaire d'une personne du catalogue, charges comprises, est d'environ 40 € ; une personne à temps plein y travaille environ 1 600 heures par an.
- Un article attend en moyenne 5 jours avant d'être photographié (annexe 2.2 D).

**B. Le projet**

- **Deux plateaux de prise de vue automatisés** : l'article est posé sur un plateau tournant, l'éclairage est réglé selon la catégorie, les photographies sont prises et détourées automatiquement, puis rattachées à l'article sans renommage.
- **Rédaction assistée** : un outil d'IA générative, proposé en service en ligne par un éditeur, rédige la fiche en cinq langues à partir des photographies et des informations saisies par l'atelier (marque, modèle, matière, état) ; un rédacteur relit et valide chaque fiche.
- **Temps prévu** : 3 minutes de prise de vue et 3 minutes de relecture, soit 6 minutes par article.

**C. Les coûts**

| Poste | Montant |
|---|---|
| Investissement : plateaux, matériel et logiciel de détourage | 150 k€ |
| Investissement : raccordement au logiciel des dépôts et au site | 60 k€ |
| Investissement : formation et accompagnement des équipes | 40 k€ |
| **Total de l'investissement**, pour une durée d'utilisation prévue de cinq ans | **250 k€** |
| Coût annuel : abonnement à la rédaction assistée (jusqu'à 120 000 fiches par an ; au-delà, 0,30 € par fiche) | 30 k€ par an |
| Coût annuel : maintenance des plateaux | 20 k€ par an |

**D. Les gains attendus (estimations de Mme DUVERNAIS)**

- Temps de catalogue : 6 minutes par article au lieu de 12.
- Délai de mise en vente : 6 jours de moins (attente avant la photographie, photographie et rédaction).
- Ventes supplémentaires, grâce à une mise en vente plus rapide et à des photographies plus homogènes : une marge supplémentaire d'environ 90 k€ par an.
- Retours pour fiche inexacte (annexe 2.2 C) divisés par deux.
- « Je ne prévois aucun départ : le temps libéré servira à absorber la croissance des ventes à l'étranger et les annonces de la future place de marché. »

**E. Les points relevés lors d'un essai de mars 2027**

- Sur 200 fiches rédigées par l'outil, 20 contenaient une erreur (matière, couleur ou année du modèle), repérée à la relecture.
- Le détourage automatique échoue sur les bijoux brillants : une photographie sur dix doit être reprise à la main.
- Les photographies du studio sont trois fois plus lourdes que les photographies actuelles.
- Les sept photographes du catalogue craignent la disparition de leur métier.
- La présidente envisage de proposer la rédaction assistée aux vendeurs de la future place de marché, qui vise environ 300 000 annonces par an en 2030.
- Mme VELDRANE : « Le studio sera-t-il rentable, et en combien de temps ? »

### ANNEXE 2.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Les données personnelles sont collectées pour des finalités déterminées et ne sont pas traitées ultérieurement de manière incompatible avec elles ; elles sont adéquates, pertinentes et limitées à ce qui est nécessaire (minimisation) ; elles sont exactes et tenues à jour ; elles sont conservées pendant une durée n'excédant pas celle nécessaire aux finalités ; elles sont protégées contre l'accès non autorisé, la perte et la destruction (intégrité et confidentialité). Le responsable du traitement doit pouvoir démontrer le respect de ces principes. | Applicable depuis le 25/05/2018. Une proposition européenne de simplification (« omnibus numérique », 19/11/2025) modifiant ce règlement est en discussion et n'est pas applicable. |
| DAMA-DMBOK (DAMA International), 2e édition | Référentiel de bonnes pratiques de gestion des données, organisé en onze domaines autour de la gouvernance des données, dont les données de référence, la qualité des données, les métadonnées, l'intégration et l'interopérabilité, l'entreposage et l'informatique décisionnelle. | 2e édition (2017), révisée en 2024 |
| ISO/IEC 25012 | Norme internationale qui définit un modèle de qualité des données, dont les caractéristiques d'exactitude, de complétude, de cohérence, d'actualité et d'accessibilité. | Publiée en 2008 |

Il n'est demandé aucune analyse juridique.

### Travail à faire

Chaque article d'ORSALIE est décrit trois fois, ses données ne sont pas fiables, le délai de mise en vente reste loin de l'objectif du plan « ORSALIE 2030 », et chaque responsable attend ses propres analyses. Mme VELDRANE vous demande d'organiser les données des articles autour d'un référentiel unique et de fiabiliser les échanges avec les places de marché, d'exploiter les données des délais et des retours pour éclairer ses décisions, de proposer une gouvernance des données et d'évaluer le projet de studio de mise en ligne. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.5 ainsi que vos connaissances professionnelles.

**2.1 – Le référentiel des articles et les échanges avec les places de marché (4 points)**

a) Après avoir défini les données de référence, proposez, en vous appuyant sur l'annexe 2.1, l'organisation des données qui fera d'un référentiel des articles la source unique de leur description : l'identifiant de l'article, trois attributs à normaliser, l'enregistrement du résultat de l'authentification et les étapes du cycle de l'article, de sa réception (ou, demain, de l'annonce du vendeur) à sa vente. Aucun modèle des données (entités, associations, cardinalités) n'est attendu.

b) Après avoir défini un dictionnaire de données, rédigez-en un extrait pour les trois notions des témoignages de l'annexe 2.1 C (« état de l'article », « article disponible », « date de mise en vente ») : pour chacune, sa définition commune, sa règle d'enregistrement ou de calcul, son propriétaire et une règle de qualité.

c) Après avoir défini l'interopérabilité, proposez les solutions d'échange d'ORSALIE avec les places de marché A, B et C qui supprimeront presque toutes les ventes en double, puis deux conditions organisationnelles de ces échanges. Le détail technique des échanges n'est pas attendu.

**2.2 – Les délais de vente, les retours et les outils d'analyse (4,5 points)**

a) Décrivez les étapes de la chaîne de traitement qui permettra de produire chaque mois l'analyse des délais et des retours à partir des sources d'ORSALIE, puis justifiez la combinaison d'analyse descriptive et d'analyse exploratoire que vous retiendrez.

b) Formulez trois constats argumentés tirés de l'annexe 2.2, en précisant pour chacun une précaution de lecture. Aucun calcul statistique n'est attendu.

c) Répondez de tête, en chiffres ronds, à la question de la présidente (annexe 2.2 E), puis proposez deux représentations visuelles adaptées pour lui présenter ces résultats, en justifiant chacune.

d) Comparez les deux options de l'annexe 2.3 C selon quatre critères, recommandez-en une et présentez deux conditions de sa réussite. Aucune manipulation d'outil n'est attendue.

**2.3 – La gouvernance des données (2 points)**

Après avoir défini la gouvernance des données, proposez celle d'ORSALIE : trois enjeux (qualité, conformité, usage des données pour la future place de marché) appliqués au cas, l'instance de gouvernance (composition, fréquence, décisions), le propriétaire et l'intendant de trois domaines de données, et l'usage que vous ferez du DAMA-DMBOK (annexe 2.5).

**2.4 – Le projet de studio de mise en ligne (2,5 points)**

a) Après avoir défini le retour sur investissement et le délai de récupération, calculez de tête le coût d'une fiche aujourd'hui, puis avec le studio, en ajoutant au coût du temps les coûts annuels et l'investissement réparti sur sa durée d'utilisation. Calculez ensuite le délai de récupération et le retour sur investissement simple sur cinq ans du studio, en ne retenant que les gains qui se traduisent en trésorerie, et commentez le traitement du temps libéré. Aucun autre calcul financier n'est attendu.

b) Présentez trois coûts indirects ou cachés que l'estimation de l'annexe 2.4 omet ou sous-estime.

c) Proposez un indicateur de suivi du projet de studio, précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
