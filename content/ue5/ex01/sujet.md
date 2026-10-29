# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 1

**DOSSIER 1 – GOUVERNER ET MODÉLISER LES DONNÉES DE PILOTAGE (16 points)**

Durée conseillée : 1 h 10 (16 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 1, construits sur un même cas : la présentation et les annexes sont communes aux trois dossiers.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. Comptoirs Ligériens est une société coopérative de commerçants détaillants créée en 1998 à Tours. Elle fédère 46 épiceries indépendantes spécialisées dans les produits locaux et biologiques, installées en Centre-Val de Loire et en Pays de la Loire. Chaque magasin est une entreprise autonome dont le gérant est associé de la coopérative. La coopérative, qui emploie 140 salariés, assure pour son réseau la centrale d'achat, la plateforme logistique de Tours, le référencement de quelque 410 producteurs locaux, des services mutualisés (informatique, ressources humaines, communication) et le pilotage commercial du réseau. Les organisations, les personnes, les produits et les données de ce cas sont fictifs.

Le système d'information de la coopérative et de ses magasins est porté par une direction des systèmes d'information (DSI) de neuf personnes, dirigée par Mme Claire VASSEUR. Trois sujets dominent son agenda de 2027 :
- les gérants réclament un pilotage plus rapide et plus fiable : le tableau de bord mensuel du réseau, consolidé à la main, est diffusé douze jours après la fin du mois et ses chiffres sont contestés ;
- le contrat de régie qui assure l'exploitation de l'ERP de la centrale prend fin le 30 juin 2027, le jour où part à la retraite le technicien qui connaît seul l'interface entre les caisses des magasins et l'ERP ;
- l'assemblée générale de juin 2026 a adopté une charte du numérique responsable, alors que plusieurs projets d'intelligence artificielle et de traçabilité sont proposés à la coopérative.

Vous venez de rejoindre la DSI comme adjoint(e) de Mme VASSEUR, chargé(e) des données et des projets. Le directeur général, M. Hervé GALLIEN, vous confie une mission articulée autour de trois axes : gouverner et modéliser les données de pilotage du réseau (dossier 1) ; réussir le passage de la régie à l'infogérance sans perdre les savoirs du technicien sortant (dossier 2) ; encadrer les projets d'intelligence artificielle et de traçabilité et mesurer l'empreinte du système d'information (dossier 3).

Les annexes 1.1 à 3.3 sont communes aux trois dossiers, qui sont indépendants. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de Comptoirs Ligériens et chiffres clés

La coopérative est administrée par un conseil d'administration de neuf gérants associés, présidé par M. Yann LE GOFF, gérant du magasin d'Angers. Autour du directeur général, M. Hervé GALLIEN, se répartissent la direction des achats et de l'offre (Mme Sonia BENALI), la direction du réseau, chargée de l'animation commerciale des magasins (M. Paul ARNAUD), la direction logistique, la direction administrative et financière, dont relève le contrôle de gestion (M. Loïc FERNANDES), les ressources humaines mutualisées (Mme Agnès PERRAULT) et la DSI (Mme Claire VASSEUR).

Aucun responsable des données n'est désigné. Les fiches des produits et des fournisseurs sont créées dans l'ERP par deux assistantes de la DSI, à partir des formulaires transmis par la direction des achats ; les magasins peuvent aussi créer des « articles locaux » directement dans leur logiciel de caisse.

| Chiffres clés | 2024 | 2026 |
|---|---|---|
| Magasins associés | 42 | 46 |
| Chiffre d'affaires hors taxes cumulé des magasins | 150 M€ | 168 M€ |
| Chiffre d'affaires hors taxes de la coopérative (ventes aux magasins et services) | 84 M€ | 96 M€ |
| Salariés de la coopérative (dont DSI) | 125 (8) | 140 (9) |
| Références actives au catalogue de la centrale | 8 200 | 9 000 |
| dont produits de producteurs situés à moins de 150 km de la plateforme de Tours | 3 100 | 3 600 |
| Producteurs locaux référencés | 360 | 410 |
| Porteurs de la carte de fidélité commune aux magasins | 170 000 | 210 000 |
| Budget du système d'information de la coopérative (fonctionnement et investissement) | 2,0 M€ | 2,4 M€ (2,5 % du chiffre d'affaires de la coopérative) |

### ANNEXE 1.2 – Projet d'entrepôt de pilotage : note de la DSI (février 2027)

Aujourd'hui, le contrôleur de gestion consolide chaque mois des extractions de l'ERP de la centrale, des logiciels de caisse des 46 magasins et d'un tableur de démarque tenu par les magasins ; le tableau de bord du réseau est diffusé à J+12. Le projet « Boussole » vise un entrepôt de données alimenté chaque nuit par les caisses et par l'ERP, qui permettra de diffuser le tableau de bord à J+2 et de comparer les magasins entre eux. Le grain retenu est mensuel : le détail des tickets reste dans le logiciel de caisse. L'entrepôt ne contiendra aucune donnée relative aux porteurs de la carte de fidélité.

Règles de gestion retenues, validées avec la direction des achats et le contrôle de gestion :
- RG1 – Un magasin associé est identifié par un code (ex. M027) ; on conserve son nom, sa ville, sa surface de vente et sa date d'adhésion.
- RG2 – Un produit est identifié par un code article attribué par la centrale (ex. P104520) ; on conserve son libellé, son code EAN lorsqu'il existe et son label (biologique, local, sans label).
- RG3 – Chaque produit appartient à une et une seule famille (crèmerie, fruits et légumes, épicerie, boissons, vrac…), identifiée par un code et dotée d'un libellé ; une famille regroupe au moins un produit.
- RG4 – Chaque produit est fourni par un et un seul fournisseur référencé ; un fournisseur fournit au moins un produit. Un fournisseur est identifié par un code ; on conserve sa raison sociale, sa commune, son type (producteur local ou grossiste) et la distance, en kilomètres, entre son exploitation ou son entrepôt et la plateforme de Tours.
- RG5 – Le mois est identifié par un code (ex. 2027-01) ; on conserve l'année, le numéro du mois et le trimestre.
- RG6 – Pour chaque magasin, chaque produit et chaque mois, l'entrepôt conserve la quantité vendue, le chiffre d'affaires hors taxes et la quantité démarquée (produits jetés ou donnés). Un produit peut n'être vendu dans aucun magasin un mois donné, et un magasin qui vient d'adhérer peut ne pas encore avoir de ventes ; chaque mois chargé dans l'entrepôt comporte au moins une vente.

Constats du profilage des données sources (février 2027) :

| Constat | Données concernées | Mesure |
|---|---|---|
| Fiches de fournisseurs en double (ex. « Ferme des Noues » et « EARL des Noues », même numéro SIRET) | référentiel des fournisseurs de l'ERP | 430 fiches pour environ 410 producteurs réels, soit une vingtaine de doublons |
| Distance à la plateforme non renseignée | fiches des producteurs locaux | 12 % des fiches |
| Articles créés dans les caisses des magasins, hors catalogue de la centrale, sans famille ni fournisseur, aux libellés libres (ex. « Tomme vache 200g » et « TOMME DE VACHE 200 G » pour un même produit) | articles locaux des caisses | 1 700 articles, 4 % du chiffre d'affaires du réseau |
| Démarque saisie dans le tableur commun | quantité démarquée | 31 magasins sur 46 |
| Écart entre le chiffre d'affaires du tableau de bord et celui des caisses | chiffre d'affaires hors taxes de décembre 2026 | 1,8 %, dû aux ressaisies manuelles lors de la consolidation |
| Délai de mise à disposition du tableau de bord | toutes | J+12 |

### ANNEXE 1.3 – Extrait du tableau de bord mensuel du réseau (janvier 2027)

**Graphique 1 – Chiffre d'affaires hors taxes du réseau.** Histogramme ; l'axe vertical est gradué de 13,5 M€ à 16 M€.

| Mois | Octobre 2026 | Novembre 2026 | Décembre 2026 | Janvier 2027 |
|---|---|---|---|---|
| Chiffre d'affaires HT (M€) | 14,1 | 14,3 | 15,9 | 13,8 |

Commentaire publié avec le graphique : « Effondrement des ventes en janvier : la barre de janvier est huit fois plus courte que celle de décembre. » Le chiffre d'affaires de janvier 2026 (13,2 M€) n'est pas présenté dans le tableau de bord.

**Graphique 2 – Répartition du chiffre d'affaires de janvier 2027 par magasin.** Diagramme circulaire en trois dimensions, 46 secteurs, légende par code de magasin.

**Graphique 3 – Carte de fidélité et performance des magasins.** Nuage de points, un point par magasin : en abscisse, la part des ventes réalisées avec la carte de fidélité ; en ordonnée, le chiffre d'affaires par mètre carré. Les huit magasins de centre-ville des quatre plus grandes agglomérations du réseau occupent le coin supérieur droit du nuage. Commentaire publié avec le graphique : « Les magasins où la carte est la plus utilisée vendent le plus au mètre carré : la carte fait vendre. Proposition : porter la remise de fidélité de 3 % à 5 % dans tout le réseau. »

**Indicateurs du mois**

| Indicateur | Janvier 2027 | Signal |
|---|---|---|
| Taux de démarque | 2,9 % | vert |
| Panier moyen | 31 € | orange |
| Part des ventes de produits locaux (fournisseur à moins de 150 km) | 38 % | vert |
| Nombre de références vendues | 8 450 | — |

Notes : le taux de démarque est calculé sur les 31 magasins qui saisissent leur démarque ; les seuils qui déclenchent les signaux ne sont pas documentés.

### ANNEXE 1.4 – Témoignages (recueillis en février 2027)

**Mme Sonia BENALI, directrice des achats et de l'offre** : « Les fiches des produits et des fournisseurs, c'est la DSI qui les saisit à partir de nos formulaires : quand un chiffre est faux, c'est un problème informatique. Je veux bien valider des règles, mais je n'ai personne pour corriger 9 000 fiches. Et quand un gérant crée un article pour le fromager de son village, nous ne l'apprenons qu'au moment où le producteur demande à être référencé. »

**M. Loïc FERNANDES, contrôleur de gestion** : « Je passe huit jours par mois à rapprocher les extractions. Les associés m'ont demandé des graphiques plus parlants, alors j'en ajoute à chaque comité. Le taux de démarque, je le calcule avec les magasins qui la saisissent : les autres ne doivent pas en avoir beaucoup. »

**Mme Nadia OUHIBI, gérante du magasin de Saumur, administratrice** : « Je veux me comparer à des magasins de ma taille, pas à la moyenne du réseau. Et à J+12, mes commandes du mois suivant sont déjà passées. Quant à la blockchain qu'on nous propose, nos clients nous croient sur parole ; ce qu'il faut, c'est qu'aucun magasin ne vende plus de fraises importées comme des fraises locales. »

**M. Bernard LEMOINE, technicien de la DSI depuis 1998, en retraite le 30 juin 2027** : « L'interface des caisses, Altinéa l'a livrée en 2019 et je l'ai reprise depuis. Quand le fichier d'un magasin arrive incomplet, je le corrige à la main avant le chargement de 6 heures : je sais quels magasins posent problème. Ce n'est écrit nulle part. Pour la clôture mensuelle des stocks, c'est pareil. Les ingénieurs d'Altinéa changent tous les six mois. »

**Mme Agnès PERRAULT, responsable des ressources humaines mutualisées** : « Nous recrutons pour les magasins 150 saisonniers et 60 salariés en contrat à durée indéterminée par an. L'éditeur de notre logiciel de recrutement propose un module d'IA qui note les candidatures, et une option qui analyse les vidéos d'entretien pour évaluer la motivation des candidats à partir des expressions de leur visage. Les gérants seraient ravis de gagner du temps. »

**Mme Claire VASSEUR, directrice des systèmes d'information** : « Avec neuf personnes, la DSI doit piloter des prestataires et des données, pas surveiller des serveurs la nuit. Mais je ne veux pas remplacer une dépendance envers Bernard par une dépendance envers un infogérant. »

### ANNEXE 2.1 – Exploitation du SI : architecture, niveaux de service de 2026, projet de contrat d'infogérance et plan de transition

**A. Architecture actuelle**
- Logiciel de caisse des 46 magasins en mode SaaS (éditeur Encaisso), qui gère aussi la carte de fidélité ; les tickets sont transmis chaque nuit à l'ERP de la centrale par une interface spécifique livrée en 2019.
- ERP de la centrale (achats, ventes aux magasins, stocks, comptabilité) et portail de commande des magasins, installés dans la salle informatique du siège ; sauvegarde quotidienne, copiée chaque semaine sur un support conservé hors du siège.
- Logiciel de gestion de la plateforme logistique en mode SaaS ; messagerie et bureautique en ligne.
- Exploitation de l'ERP, du portail et des sauvegardes : contrat de régie avec l'ESN Altinéa Services (deux ingénieurs à temps partiel, 90 jours facturés en 2026 à 650 € HT par jour), qui prend fin le 30 juin 2027 ; M. LEMOINE assure le suivi quotidien.
- Les gérants passent leurs commandes sur le portail 7 jours sur 7, de 6 h à 22 h ; les commandes du samedi et du dimanche préparent les livraisons du lundi, les plus importantes de la semaine.

**B. Niveaux de service constatés en 2026 (ERP et portail de commande)**

| Indicateur | 2026 |
|---|---|
| Disponibilité du portail sur la plage 6 h – 22 h, 7 jours sur 7 | 98,6 % |
| Incidents bloquants (commande impossible pour au moins un magasin) | 14 |
| dont incidents survenus un samedi ou un dimanche | 9 |
| Délai moyen de rétablissement d'un incident bloquant | 7 heures |
| Nuits où l'interface caisses-ERP a échoué ou a été corrigée à la main | 22 |
| Tests de restauration des sauvegardes réalisés | 0 |

**C. Extraits du projet de contrat d'infogérance proposé par l'ESN Nexalis (offre du 15 février 2027)**
- Article 2 – Objet : hébergement de l'ERP et du portail dans le centre de données de Nexalis, situé dans l'Union européenne ; exploitation, supervision, sauvegardes et support de niveau 2. Durée : quatre ans. Redevance : 14 000 € HT par mois. Une offre distincte prévoit la migration de l'ERP et du portail au prix forfaitaire de 36 000 € HT, environnement recetté livré.
- Article 6 – Niveaux de service : « Disponibilité mensuelle de 99,5 %, mesurée du lundi au vendredi de 8 h à 18 h, hors maintenances programmées. Prise en charge d'un incident bloquant dans un délai de 4 heures ouvrées. Rétablissement : le prestataire met en œuvre ses meilleurs efforts. Le prestataire adresse au client un rapport trimestriel. »
- Article 7 – Pénalités : « 1 % de la redevance mensuelle par tranche de 0,1 point de disponibilité manquant, dans la limite de 5 % de la redevance mensuelle, sous réserve d'une réclamation écrite du client dans les 15 jours qui suivent le rapport trimestriel. »
- Article 9 – Sauvegardes : « Sauvegardes quotidiennes, conservées sept jours. »
- Article 12 – Fin du contrat : « À l'expiration du contrat, le prestataire restitue les données du client, sur demande de celui-ci, selon des modalités et à un prix à convenir entre les parties. »
- Article 14 – Sous-traitance : « Le prestataire peut confier tout ou partie des prestations à des sous-traitants de son choix. »
- Observation de la DSI : le projet ne comporte ni clause d'audit ni stipulation relative aux données personnelles (comptes des utilisateurs du portail, coordonnées des producteurs exploitants individuels), ni engagement de notification des incidents de sécurité.

**D. Plan de transition préparé par la DSI (semaine 1 = semaine du lundi 1er mars 2027)**

| Tâche | Description | Durée | Tâches antérieures | Intervenants |
|---|---|---|---|---|
| A | Négociation et signature du contrat d'infogérance et du forfait de migration | 3 semaines | – | DSI, direction financière |
| B | Inventaire de l'existant ; documentation de l'interface caisses-ERP et de la clôture mensuelle des stocks | 4 semaines | – | M. LEMOINE, DSI |
| C | Préparation de l'environnement d'hébergement | 3 semaines | A | Nexalis |
| D | Migration à blanc de l'ERP et du portail, recette par les utilisateurs | 4 semaines | B, C | Nexalis, DSI, achats |
| E | Transfert de compétences vers Nexalis et la DSI (interface, clôture des stocks) | 3 semaines | B | M. LEMOINE, Nexalis, DSI |
| F | Test de restauration des sauvegardes et répétition générale de la bascule | 2 semaines | D | Nexalis, DSI, M. LEMOINE |
| G | Bascule en production (un week-end), puis accompagnement renforcé des magasins | 2 semaines | E, F | Nexalis, DSI |
| H | Fin de la régie Altinéa et bilan du projet | 1 semaine | G | DSI |

M. LEMOINE ne peut pas travailler sur deux tâches au cours de la même semaine. La bascule doit être achevée avant son départ et la fin de la régie, le mercredi 30 juin 2027 (semaine 18).

### ANNEXE 3.1 – Projets d'intelligence artificielle et de traçabilité à l'étude (mars 2027)

| Projet | Description | Porteur | Données utilisées |
|---|---|---|---|
| A – Prévision des commandes de produits frais | Module proposé par l'éditeur du logiciel de caisse : à partir de l'historique des ventes, de la démarque, de la météo et du calendrier, il établit chaque matin une proposition de commande de fruits et légumes, de crèmerie et de pain pour chaque magasin ; le gérant valide ou corrige. Abonnement : 1 500 € HT par mois pour le réseau. | Direction du réseau | ventes par article et par magasin, démarque, météo |
| B – Présélection des candidatures | Module du logiciel de recrutement : il attribue à chaque candidature une note de 0 à 100 et propose au gérant une liste restreinte. Option « entretien vidéo augmenté » : analyse des expressions du visage et de la voix pendant l'entretien vidéo pour estimer la motivation et la résistance au stress du candidat. | Ressources humaines mutualisées | CV, lettres de motivation, vidéos d'entretien |
| C – Assistant de rédaction et agent conversationnel | Outil d'IA générative accessible par abonnement : rédaction des fiches des 3 600 produits locaux sur le site de retrait en magasin ; réponses automatiques aux questions des clients du site (horaires, disponibilité des produits, allergènes). | Communication | fiches produits, questions des clients |

En 2026, la démarque des produits frais a représenté 4,8 % de leurs ventes dans les 31 magasins qui la mesurent ; la direction du réseau vise 3,5 % en 2028 grâce au projet A.

**Proposition de la jeune entreprise Tracéo.** En septembre 2026, un journaliste local a révélé qu'un magasin du réseau vendait des fraises importées sous l'étiquette « producteur local » ; l'étiquetage des produits frais est réalisé dans chaque magasin. Tracéo propose une blockchain de consortium réservée aux producteurs, à la coopérative et aux magasins : chaque lot de produit local est enregistré par le producteur sur une application mobile (date de récolte ou de fabrication, lieu, quantité), puis complété par la plateforme logistique et par le magasin ; un QR code imprimé sur l'étiquette permet au client de consulter l'origine du lot. Les blocs sont validés par cinq nœuds tenus par la coopérative et par Tracéo, selon un vote des nœuds autorisés, sans minage. Coût : 45 000 € HT de mise en place, puis 1 200 € HT par mois. Les deux tiers des 410 producteurs locaux sont des exploitations de moins de trois personnes, et 40 % d'entre eux n'utilisent pas de smartphone pour leur activité. La DSI suggère une autre piste : ajouter à l'ERP la gestion des lots et des attestations d'origine des producteurs, contrôlées par sondage.

### ANNEXE 3.2 – Indicateurs de durabilité du SI : situation de 2026 et engagements de la charte pour 2029

La charte du numérique responsable adoptée en juin 2026 engage la coopérative à réduire de 25 % d'ici 2029 les émissions de gaz à effet de serre de son système d'information par rapport à 2026.

| Indicateur | 2026 | Engagement 2029 |
|---|---|---|
| Émissions de gaz à effet de serre du SI de la coopérative et des magasins (estimation 2026 selon la méthode Bilan Carbone, scopes 1 à 3) | 310 tCO2e, dont 72 % liés à la fabrication des équipements et moins de 1 % lié à l'électricité de la salle informatique du siège | − 25 % |
| Postes de travail et terminaux de caisse en service (siège et magasins) | 420 | — |
| Durée d'usage moyenne des postes de travail remplacés | 4 ans | 6 ans |
| Part d'équipements reconditionnés dans les achats de l'année | 5 % | 30 % |
| Électricité consommée par la salle informatique du siège | 38 MWh | salle fermée après la migration (annexe 2.1) |
| Volume de données stockées, sauvegardes comprises | 42 To (+ 30 % par an depuis 2024) | stabilisé |
| Tickets de caisse imprimés | 9,5 millions | − 50 % (ticket dématérialisé proposé au client) |
| EcoIndex moyen des pages du site de retrait en magasin | E | C |
| Salariés de la coopérative et des magasins sensibilisés au numérique responsable | 10 % | 80 % |

Notes : après la migration, l'électricité nécessaire à l'ERP sera consommée dans le centre de données de Nexalis, dont l'offre ne mentionne aucun indicateur environnemental. Les projets A et C de l'annexe 3.1 n'ont fait l'objet d'aucune estimation de consommation.

### ANNEXE 3.3 – Repères réglementaires (au 31/12/2026)

| Texte | Objet principal | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2024/1689 sur l'intelligence artificielle (« AI Act »), modifié par le règlement (UE) 2026/1744 du 8 juillet 2026 (omnibus numérique sur l'IA) | Approche par les risques : pratiques interdites, systèmes à haut risque, obligations de transparence, modèles d'IA à usage général. Sont notamment interdites la notation sociale et la reconnaissance des émotions sur le lieu de travail, sauf pour des raisons médicales ou de sécurité. Relèvent notamment du haut risque (annexe III) les systèmes destinés au recrutement et à la sélection des candidats, ou à l'évaluation des salariés. | Pratiques interdites : depuis le 02/02/2025 ; deux interdictions ajoutées par le règlement (UE) 2026/1744 (contenus sexuels générés sans consentement, matériel pédopornographique) : depuis le 02/12/2026. Maîtrise de l'IA (article 4, modifié par le règlement (UE) 2026/1744 : les fournisseurs et les déployeurs prennent des mesures pour favoriser la maîtrise de l'IA de leur personnel) : depuis le 02/02/2025. Modèles d'IA à usage général : depuis le 02/08/2025. Transparence (information des personnes qui dialoguent avec une IA, marquage des contenus générés) : depuis le 02/08/2026 ; marquage par les systèmes génératifs mis sur le marché avant le 02/08/2026 : au plus tard le 02/12/2026. Haut risque de l'annexe III : à compter du 02/12/2027, date reportée par l'omnibus ; haut risque de l'annexe I (produits réglementés) : 02/08/2028. |
| Règlement (UE) 2016/679 (RGPD) | Protection des données personnelles : registre des traitements, contrat écrit avec tout sous-traitant (article 28), analyse d'impact pour les traitements susceptibles d'engendrer un risque élevé, notification des violations de données à l'autorité de contrôle dans les 72 heures | Applicable depuis le 25/05/2018 |
| Directive (UE) 2022/2555 (« NIS 2 ») | Cybersécurité des entités essentielles et importantes, dont les prestataires de services informatiques gérés et certaines entreprises du secteur alimentaire : gestion des risques, y compris la sécurité de la chaîne d'approvisionnement ; notification des incidents importants (alerte sous 24 heures, notification sous 72 heures, rapport final sous un mois) ; responsabilité des organes de direction | Délai de transposition expiré le 17/10/2024. En France, le projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité, adopté par le Sénat le 12/03/2025, n'est ni adopté par l'Assemblée nationale ni promulgué à la date de rédaction du sujet (octobre 2026) ; le candidat retiendra cette situation au 31/12/2026. |
| Règlement (UE) 2023/2854 (« Data Act ») | Accès aux données et changement de fournisseur de services d'informatique en nuage (portabilité des données, assistance à la sortie) | Applicable depuis le 12/09/2025 |
| Loi n° 2021-1485 du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique (REEN) ; référentiel général d'écoconception de services numériques (RGESN, version 2 de 2024) | Réduction de l'empreinte environnementale du numérique ; écoconception des services numériques | Loi REEN : en vigueur. RGESN : référentiel publié le 17/05/2024, d'application volontaire pour les entreprises. |

### Travail à faire

Le directeur général veut que le projet « Boussole » (annexe 1.2) ne se réduise pas à un chantier informatique : à la fin de 2027, les gérants doivent disposer de chiffres fiables, comparables et diffusés à J+2. Vous mobiliserez pour cela les annexes 1.1 à 1.4 ainsi que vos connaissances professionnelles.

**1.1 – Modélisation de l'entrepôt de pilotage (5 points)**

a) À partir des règles de gestion de l'annexe 1.2, établissez le modèle conceptuel des données (MCD) de l'entrepôt de pilotage, en précisant les identifiants, les attributs et les cardinalités.

b) Déduisez-en le modèle logique des données (MLD), en explicitant les règles de passage appliquées.

c) Après avoir défini l'entrepôt de données, expliquez pourquoi la DSI a retenu un entrepôt plutôt qu'un lac de données, et montrez en quoi le modèle obtenu s'apparente à un schéma en étoile.

**1.2 – Gouvernance des données (4 points)**

a) Après avoir défini la gouvernance des données, présentez l'apport du référentiel DAMA-DMBOK pour Comptoirs Ligériens.

b) Distinguez le propriétaire et l'intendant des données, puis proposez, pour les domaines « produits », « fournisseurs » et « ventes », une répartition des rôles justifiée par les annexes 1.1 et 1.4, ainsi que l'instance chargée des arbitrages.

c) Rédigez l'entrée du dictionnaire de données pour les données « distance du fournisseur » et « quantité démarquée ».

**1.3 – Qualité des données (4 points)**

a) Après avoir défini la qualité des données, rattachez quatre constats de l'annexe 1.2 à la dimension de la qualité qu'ils dégradent, en précisant leur conséquence pour le pilotage du réseau.

b) Proposez un plan d'action hiérarchisé pour fiabiliser les données avant l'ouverture de l'entrepôt, assorti de deux indicateurs de qualité. Pour chaque indicateur, précisez la formule, la source, la fréquence, la cible et l'axe du tableau de bord.

**1.4 – Critique du tableau de bord mensuel (3 points)**

a) Après avoir défini le tableau de bord de pilotage, identifiez trois défauts de représentation ou d'interprétation dans l'extrait de l'annexe 1.3 et expliquez le risque de décision erronée que chacun fait courir.

b) Proposez les principes de la nouvelle restitution destinée aux gérants (contenu, représentations, comparaisons, délai), en tenant compte des témoignages de l'annexe 1.4.
