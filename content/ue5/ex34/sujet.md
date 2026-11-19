# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 34

**DOSSIER 1 – PRÉPARER LA REFONTE DU SITE ET L'OUVERTURE DE LA PLACE DE MARCHÉ (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 1.2 – Le projet de place de marché et l'état du numérique (note de Mme Inès VELDRANE, présidente, et témoignages recueillis en avril 2027)

**A. Le projet de place de marché (note de la présidente)**

« Aujourd'hui, ORSALIE fait tout elle-même : elle reçoit ou rachète l'article, l'authentifie, le photographie, le décrit, fixe son prix, le stocke, le vend et le fait expédier. Demain, sur notre place de marché, le vendeur particulier publiera lui-même son annonce depuis son téléphone (photos, description, prix), aidé par une estimation du prix que nous lui proposerons. L'acheteur paiera sur notre site ; le vendeur enverra alors l'article à l'atelier de Lille, qui l'authentifiera avant de le faire livrer à l'acheteur. Si l'article n'est pas authentique ou ne correspond pas à l'annonce, la vente sera annulée et l'acheteur remboursé. ORSALIE prélèvera une commission de 20 % du prix de vente et reversera le reste au vendeur. Nous proposerons aussi de nouveaux services : l'estimation du prix, une garantie d'authenticité d'ORSALIE et la revente facilitée d'un article acheté chez nous. Le dépôt-vente et le rachat seront maintenus pour les articles de grande valeur. »

| Repère | 2026 | Objectif 2030 |
|---|---|---|
| Articles proposés à la vente | environ 110 000 articles reçus à l'atelier | environ 300 000 annonces publiées par an |
| Vendeurs particuliers | 30 000 | 120 000 |
| Articles rachetés et détenus en stock par ORSALIE | un tiers des articles reçus | moins de 10 % des articles vendus |
| Revenus | marge sur les articles rachetés, commission sur le dépôt-vente | commissions sur les ventes entre particuliers, services payants (estimation, garantie, revente) |
| Ventes réalisées en ligne (site, application, places de marché) | 85 % | plus de 90 % |

**B. Les limites du site actuel (témoignage de M. Hugo LAMBRESCOT, responsable technique)**

« Le catalogue, les comptes des clients, le panier, le paiement, les promotions et les connecteurs vers les places de marché forment une seule application : modifier une page oblige à remettre en ligne l'ensemble. Nous ne le faisons qu'une fois par mois, le dimanche soir ; en 2026, sur 12 mises en ligne, 4 ont été suivies d'un incident et 2 ont imposé un retour à la version précédente. Lors de la "Semaine du luxe circulaire" de novembre 2026, le site a reçu jusqu'à 4 000 visiteurs simultanés : le temps d'affichage d'une page d'article est passé de 2 à 9 secondes pendant six heures, et les ventes du jour ont été inférieures de 30 % à la prévision. Les connecteurs vers les places de marché se sont interrompus 30 fois en 2026, et un développeur a dû les relancer à la main à chaque fois. Le code de 2016 est peu documenté, et seuls deux des quatre développeurs connaissent la partie paiement. »

**C. Les décisions et l'organisation de l'équipe numérique (constats d'avril 2027)**

- Les choix numériques sont décidés par la présidente seule, au fil des demandes du commerce, de l'atelier et du catalogue ; il n'existe ni instance, ni critère de priorité. Le budget du numérique est arrêté chaque année par la présidente.
- L'équipe numérique reçoit les demandes par courriel, par messagerie instantanée ou de vive voix. En 2026, elle en a reçu environ 900 (commerce : 400 ; catalogue : 250 ; atelier : 150 ; autres : 100). En avril 2027, 400 demandes sont en attente, dont 150 depuis plus de six mois ; elles sont traitées dans l'ordre d'arrivée, ou selon l'insistance du demandeur.
- En 2026, les développeurs ont consacré 60 % de leur temps à corriger des anomalies et à traiter des urgences, 30 % aux évolutions demandées, 10 % à l'amélioration du code existant.
- Les deux chefs de produit enregistrent les demandes dans la file et relancent les développeurs ; ils ne décident d'aucune priorité. L'analyste de données répond aux demandes d'extraction des responsables.

**D. Deux technologies proposées par l'équipe numérique**

| | Recherche d'articles par photo | Assistant conversationnel d'IA générative pour le service clients |
|---|---|---|
| Principe | le client charge la photo d'un article (vu dans la rue, sur un réseau social) ; un modèle de reconnaissance d'images, entraîné sur des millions de photos, lui propose les articles semblables disponibles chez ORSALIE ; le vendeur pourrait aussi l'utiliser pour préremplir son annonce (marque, modèle) | un grand modèle de langage, proposé en service en ligne par un éditeur, répond par écrit aux clients, à toute heure et dans leur langue (suivi de commande, état d'un article, retours, conditions du dépôt-vente) |
| Situation actuelle | les clients cherchent par mots clés ; beaucoup ne connaissent pas le nom exact du modèle qu'ils cherchent | en 2026, le service clients a reçu 180 000 messages, dont 40 % rédigés dans une autre langue que le français ; délai moyen de première réponse : 30 heures ; les 10 conseillers écrivent en français et en anglais et copient les autres messages dans un traducteur gratuit en ligne |
| Essai de mars 2027 | sur 1 000 photos d'articles du catalogue, le modèle exact a été reconnu 8 fois sur 10, mais seulement 6 fois sur 10 pour les montres ; l'outil ne permet pas d'authentifier un article | sur 200 questions de clients, 170 réponses justes, 20 incomplètes, 10 erronées, dont une qui promettait un remboursement sans retour de l'article ; l'outil d'essai, gratuit, conserve les conversations pour améliorer son modèle |
| Avis recueillis | M. ROCHAMBEL : « Nos concurrents l'auront avant nous. » | M. BELLASTRE : « Mes conseillers ont peur d'être remplacés ; nos clients du luxe attendent une relation personnelle. » |

**E. Repères (au 31/12/2026)**

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2024/1689 sur l'intelligence artificielle (AI Act), modifié par le règlement (UE) 2026/1744 | Depuis le 2 février 2025, les organisations qui utilisent des systèmes d'IA prennent des mesures pour assurer un niveau suffisant de maîtrise de l'IA à leur personnel. Depuis le 2 août 2026, les systèmes d'IA destinés à échanger directement avec des personnes doivent être conçus pour que celles-ci soient informées qu'elles échangent avec une IA, sauf si cela est évident. | En vigueur, application échelonnée |
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Le prestataire qui traite des données personnelles pour le compte d'ORSALIE est un sous-traitant : un contrat encadre le traitement (instructions d'ORSALIE, confidentialité, sécurité, sort des données à la fin de la prestation). | Applicable depuis le 25/05/2018 |

### ANNEXE 1.3 – L'architecture envisagée (note de M. Hugo LAMBRESCOT, responsable technique, avril 2027)

**A. Le principe**

« Je propose d'abandonner l'application d'un seul tenant pour une architecture composable : le site est découpé en services indépendants, chacun chargé d'un domaine (catalogue, annonces, paiements, recherche, relation client), qui échangent leurs données par des interfaces de programmation (API) documentées. Chaque service peut être modifié, mis en ligne et renforcé séparément. Les pages vues par les clients (site et application) sont séparées des services. Les services seraient détachés un à un de l'application actuelle, qui serait arrêtée à la fin de la refonte. »

**B. Les services envisagés**

| Service | Rôle | Réalisation envisagée |
|---|---|---|
| Pages du site et de l'application | affichage pour les clients, en plusieurs langues | développement sur mesure |
| Catalogue des articles | fiches, photos, prix, disponibilité des articles authentifiés | développement sur mesure |
| Annonces des particuliers | dépôt et suivi des annonces, estimation du prix | logiciel en ligne de place de marché, acheté par abonnement à un éditeur spécialisé |
| Commandes, commissions et paiements | panier, commande, calcul des commissions, remboursements ; paiement par le prestataire agréé | logiciel en ligne de place de marché et prestataire de paiement actuel |
| Recherche | recherche par mots clés et par filtres | service en ligne d'un éditeur de moteurs de recherche, par abonnement |
| Relation client | comptes des clients et des vendeurs, messages, campagnes | outil actuel de gestion de la relation client |
| Atelier et stocks | réception, authentification, remise en état, stocks | logiciel « maison » actuel, relié par API |

**C. Les conséquences que je signale**

- **Compétences** : l'équipe ne connaît que la technologie de 2016 ; il faudra concevoir des API, intégrer des services d'éditeurs, surveiller des échanges entre services et piloter des fournisseurs.
- **Fournisseurs** : nous dépendrons de six fournisseurs techniques (entreprise de services du numérique de la refonte, éditeur du logiciel de place de marché, éditeur du moteur de recherche, prestataire de paiement, hébergeur en nuage, éditeur de l'outil de relation client), contre trois aujourd'hui ; les abonnements sont révisables chaque année et les mises à jour des éditeurs sont imposées à tous leurs clients ; l'éditeur du logiciel de place de marché restitue les données à la fin du contrat « dans son propre format ».
- **Responsabilités** : quand un paiement échouera, il faudra savoir si la cause est dans nos pages, dans le logiciel de place de marché, chez le prestataire de paiement ou chez l'hébergeur ; aujourd'hui, personne n'est chargé de coordonner la résolution d'un incident qui touche plusieurs fournisseurs.
- **Données** : les informations sur un article, un vendeur ou un acheteur seront réparties entre plusieurs services et plusieurs fournisseurs, dont certaines données personnelles des vendeurs et des acheteurs.

### ANNEXE 1.4 – La consultation des entreprises de services du numérique et le projet de contrat (synthèse du service des achats et du service juridique, avril 2027)

**A. L'objet de la consultation**

Refonte du site marchand et de l'application selon l'architecture de l'annexe 1.3 : cadrage et architecture, développement des pages, du catalogue et des échanges entre services, intégration du logiciel de place de marché et du moteur de recherche, reprise des fiches existantes. Ouverture de la place de marché au printemps 2028 ; arrêt de l'application actuelle à l'automne 2028. La présidente a fixé une enveloppe de 2 000 k€ pour la refonte.

**B. Les deux offres retenues après la consultation de cinq entreprises**

| | Offre 1 – ESCARVÈNE Numérique | Offre 2 – NORIVANE Conseil |
|---|---|---|
| Forme | forfait global sur un périmètre figé : le cahier des charges est arrêté à la fin du cadrage, en août 2027 | cadrage et architecture au forfait (juin à août 2027), puis une équipe dédiée qui travaille avec l'équipe numérique d'ORSALIE par itérations de deux semaines, de septembre 2027 à septembre 2028 |
| Équipe | désignée par l'ESN, dans ses locaux à Lyon | six personnes (une responsable d'équipe, quatre développeurs, une testeuse), présentes à Lille trois jours par semaine |
| Prix | 1 800 k€, cadrage compris ; toute modification du périmètre fait l'objet d'un avenant au taux de 800 € par jour | cadrage : 150 k€ ; 60 k€ par itération, 25 itérations estimées ; plafond de 1 900 k€, qui ne peut être dépassé que par avenant |
| Livraisons | la place de marché en mai 2028, le reste du site en novembre 2028 ; recette par ORSALIE dans les 15 jours suivant chaque livraison | une version utilisable à la fin de chaque itération ; le contenu de chaque itération est fixé avec ORSALIE à son début, sans engagement de l'ESN sur ce qui sera achevé |
| Pénalités | 0,5 % du prix par semaine de retard, plafonnées à 5 % | aucune |
| Code développé | cédé à ORSALIE au paiement de la dernière facture ; documentation remise à la fin | propriété non précisée ; les composants réutilisables de l'ESN restent sa propriété, ORSALIE en reçoit une licence d'utilisation |
| Équipe et transfert de compétences | rotation annoncée des consultants : environ 15 % par an ; aucun transfert prévu | rotation annoncée : environ 25 % par an ; l'ESN peut remplacer un consultant avec un préavis d'une semaine ; en option, chaque développeur de l'ESN travaille en binôme avec un développeur d'ORSALIE : 5 k€ par itération |
| Fin anticipée | résiliation pour faute seulement | ORSALIE peut arrêter la prestation à la fin de chaque série de cinq itérations, avec un préavis d'une itération |

**C. Les risques relevés**

- **Dérive du périmètre** : le carnet des besoins n'est pas stabilisé (annexe 1.5) et les besoins de la place de marché se préciseront avec les premiers vendeurs. En 2023, la refonte du logiciel de caisse, confiée au forfait à un autre prestataire, a été livrée avec quatre mois de retard ; les avenants ont augmenté son prix de plus d'un tiers.
- **Rotation des consultants** : un consultant remplacé emporte la connaissance du code qu'il a écrit.
- **Dépendance** : l'équipe numérique ne connaît pas les technologies de la nouvelle architecture.
- **Propriété du code** : selon le service juridique, sans clause de cession des droits, ORSALIE ne pourrait ni modifier librement le code développé par l'ESN, ni le confier à un autre prestataire.
- **Transfert de compétences** : à la fin de la refonte, l'équipe numérique devra faire évoluer seule les services développés sur mesure.

**D. Le projet de gouvernance de la relation (à compléter)**

| Élément | Offre 1 | Offre 2 |
|---|---|---|
| Comités | à définir | à définir |
| Indicateurs de suivi | à définir | à définir |
| Pénalités | retard seulement | aucune |
| Clause d'audit | absente | absente |
| Transfert de compétences | absent | en option |

Il n'est demandé aucune analyse juridique du contrat ni de la propriété du code.

### ANNEXE 1.5 – L'organisation du projet de refonte (note de la présidente et constats de l'équipe numérique, avril 2027)

**A. La démarche décidée par la présidente**

- **Phase 1 – cadrage et architecture (juin à août 2027), planifiée** : objectifs, périmètre, architecture cible, choix des logiciels en ligne, premier carnet des besoins.
- **Phase 2 – développement par itérations de deux semaines (septembre 2027 à septembre 2028)**, en trois lots : lot 1, annonces des particuliers et place de marché ; lot 2, catalogue, recherche, pages du site et de l'application ; lot 3, relation client et boutiques.
- **Phase 3 – mise en service par étapes** : lot 1 en avril 2028, d'abord pour 2 000 vendeurs invités ; lot 2 en juin 2028 ; lot 3 en octobre 2028, avec l'arrêt de l'application actuelle.
- **Rôles envisagés** : la présidente souhaite être elle-même « propriétaire du produit » de tout le site, mais ne dispose que de deux heures par semaine ; M. LAMBRESCOT serait « Scrum Master » tout en restant le responsable hiérarchique des développeurs et en décidant seul des mises en ligne ; les deux chefs de produit continueraient d'enregistrer les demandes ; la responsable d'équipe proposée par NORIVANE Conseil propose d'être elle aussi « Scrum Master ».

**B. Extrait du carnet des besoins (rédigé en mars 2027 par le commerce, l'atelier et le catalogue)**

| Repère | Besoin exprimé | Émis par |
|---|---|---|
| B1 | « Le site doit être rapide, même pendant les opérations commerciales. » | commerce |
| B2 | « Le vendeur doit pouvoir déposer son annonce facilement depuis son téléphone. » | commerce |
| B3 | « L'atelier doit voir les articles qui arrivent. » | atelier |
| B4 | « Il faut que ce soit sécurisé. » | commerce |
| B5 | « Des fiches belles et complètes avec de vraies photos, pouvoir changer les prix en masse, et aussi voir les ventes par catégorie. » | catalogue |
| B6 | « Les clients étrangers doivent pouvoir tout faire dans leur langue. » | commerce |
| B7 | « Plus jamais de paiement débité deux fois. » | finances |
| B8 | « Comme sur les grandes plateformes. » | commerce |

Aucun besoin ne précise d'exigence de performance, de sécurité ou d'accessibilité ; aucun n'a de priorité ni de critère d'acceptation.

**C. Les incidents de la mise en ligne du dimanche 7 mars 2027**

- **Paiements en double** : pendant trois heures, 240 clients ont été débités deux fois, pour environ 130 k€, remboursés en dix jours. La modification du panier n'avait été essayée que par son développeur, sur son poste, et jamais avec l'environnement d'essai du prestataire de paiement.
- **Fiches disparues** : une mise à jour des prix a rendu 1 800 fiches d'articles invisibles sur le site pendant deux jours ; ce sont des clients qui l'ont signalé. Personne du catalogue n'avait vérifié le résultat avant ou après la mise en ligne.
- Le retour à la version précédente a pris 6 heures, faute de procédure écrite. Le service clients a reçu 60 réclamations ; la note moyenne des avis des clients est passée de 4,6 à 4,1 sur 5 en mars 2027.

**D. Les pratiques actuelles de vérification**

Les développeurs essaient eux-mêmes leurs modifications sur leur poste ; il n'existe pas d'environnement de recette semblable au site en service ; ni le commerce ni le catalogue ne vérifient une évolution avant sa mise en ligne ; les anomalies sont suivies dans un tableur ; la date de mise en ligne est fixée la veille par le responsable technique. Aucune recette n'a jamais été organisée.

### Travail à faire

Le site d'ORSALIE ne suit plus la croissance de l'entreprise, et la place de marché entre particuliers doit ouvrir au printemps 2028. Mme VELDRANE vous demande de montrer ce que ce projet change pour le système d'information, d'organiser les décisions et l'équipe numérique, d'éclairer l'architecture proposée, de préparer le choix et le pilotage de l'entreprise de services du numérique, puis d'organiser le projet et sa recette. Vous mobiliserez pour cela les annexes 1.1 à 1.5 ainsi que vos connaissances professionnelles.

**1.1 – La place de marché, le rôle stratégique du système d'information et la veille technologique (3,5 points)**

a) Après avoir caractérisé une place de marché entre particuliers, montrez, à partir des annexes 1.1 et 1.2, en quoi le passage d'ORSALIE du modèle de revendeur à celui de place de marché change le rôle stratégique de son système d'information, selon trois axes : les sources de valeur, les processus clés et la dépendance au numérique.

b) Après avoir défini la veille technologique, proposez le dispositif de veille d'ORSALIE (objets, sources, acteurs, diffusion et décision). Évaluez ensuite l'impact des deux technologies de l'annexe 1.2 D sur le modèle d'ORSALIE (apports, limites et risques, conditions de réussite) et recommandez une décision pour chacune. Aucun calcul de rentabilité n'est attendu.

**1.2 – La gouvernance des choix numériques et l'organisation de l'équipe numérique (3 points)**

a) Après avoir défini la gouvernance du système d'information, proposez la gouvernance des choix numériques d'ORSALIE, associant la présidente, les responsables des métiers et l'équipe numérique : deux instances (composition, fréquence, décisions), le rôle de chaque acteur et quatre critères d'arbitrage des demandes.

b) Comparez l'organisation actuelle de l'équipe numérique à une organisation en équipes produit, proposez une répartition des dix personnes de l'équipe numérique en équipes produit, puis présentez trois limites de cette organisation pour une équipe de dix personnes, avec pour chacune une parade.

**1.3 – L'architecture composable et ses impacts (2 points)**

a) Après avoir défini l'urbanisation du système d'information, expliquez ce qu'est l'architecture composable de l'annexe 1.3 et présentez trois apports de cette architecture, par rapport à l'application actuelle, pour la place de marché et le plan « ORSALIE 2030 », ainsi qu'une limite.

b) Analysez les impacts organisationnels et juridiques de cette architecture selon quatre axes : les compétences et les métiers de l'équipe numérique, la multiplication des contrats, les responsabilités en cas d'incident, la répartition des données. Proposez une mesure pour chacun. Aucun schéma technique détaillé ni aucune analyse juridique ne sont attendus.

**1.4 – Le choix et le pilotage de l'entreprise de services du numérique (2,5 points)**

a) Comparez les deux offres de l'annexe 1.4 au regard des risques relevés, en établissant de tête le coût estimé de l'offre 2 et sa marge par rapport à son plafond. Recommandez une offre, puis présentez votre démarche de négociation : trois points à obtenir et deux concessions possibles.

b) Proposez le dispositif de pilotage de la relation avec l'ESN retenue : les instances, deux indicateurs de suivi précisés chacun par sa formule, sa source, sa fréquence, sa cible et son axe, la clause d'audit et le transfert de compétences.

**1.5 – Le projet hybride, les exigences et la recette (3 points)**

a) Organisez le projet hybride décidé par la présidente (annexe 1.5 A) : l'objet et les livrables de chaque phase, l'attribution des trois responsabilités définies par le Scrum Guide aux acteurs du cas, en corrigeant les choix envisagés, et la méthode de priorisation du carnet.

b) Réécrivez trois besoins de l'annexe 1.5 B en exigences vérifiables, dont au moins une exigence non fonctionnelle, en associant à chacune son critère d'acceptation.

c) Proposez le plan qualité et la stratégie de recette qui auraient évité les incidents du 7 mars 2027 : les niveaux de tests fonctionnels, les responsabilités et quatre critères de mise en service d'un lot. Aucun test technique de sécurité n'est attendu.
