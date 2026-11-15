# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 20

**DOSSIER 2 – GOUVERNER LE NUMÉRIQUE DU CLUB ET ÉVALUER LE PROJET DE JETONS DE SUPPORTERS (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 7, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en juin 2027. MONTALBRET XV est le club de rugby professionnel de l'agglomération de Montalbret, ville fictive du Sud-Ouest de 180 000 habitants. Il est exploité par une société anonyme sportive professionnelle détenue à 80 % par la holding familiale de son président, M. Damien ROQUESSOL, et à 20 % par l'association MONTALBRET XV, qui gère la formation et les équipes amateurs. Le club dispute la deuxième division professionnelle et vise l'accession à l'élite d'ici 2030. Il emploie 150 salariés permanents, dont 48 joueurs et entraîneurs, et fait appel les jours de match à environ 400 intervenants extérieurs (accueil, sécurité, restauration). Il joue dans un stade de 16 000 places appartenant à la communauté d'agglomération et compte 7 000 abonnés. Son chiffre d'affaires de la saison 2025-2026 s'élève à 28 millions d'euros ; 0,9 million d'euros est consacré au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « MONTALBRET 2030 », adopté par le conseil d'administration en janvier 2027, fixe trois priorités : mieux connaître les supporters et les partenaires pour développer les recettes hors droits sportifs ; structurer la gouvernance du numérique du club et étudier de nouvelles formes de relation avec les supporters ; fiabiliser l'organisation des jours de match dans un stade modernisé et réduire son empreinte environnementale. La directrice générale, Mme Inès LAFERRADE, en rend compte chaque trimestre au conseil d'administration.

Vous êtes responsable administratif et financier de MONTALBRET XV depuis 2025. Mme LAFERRADE vous a aussi confié la responsabilité du système d'information du club, et elle vous demande trois travaux : organiser et valoriser les données des supporters (dossier 1) ; gouverner le numérique du club et évaluer le projet de jetons de supporters (dossier 2) ; maîtriser les risques des jours de match et l'empreinte du stade connecté (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de MONTALBRET XV et chiffres clés

MONTALBRET XV est une société anonyme sportive professionnelle qui exploite le club de rugby professionnel de l'agglomération de Montalbret, ville fictive du Sud-Ouest de 180 000 habitants. Elle est détenue à 80 % par la holding familiale de son président et à 20 % par l'association MONTALBRET XV, qui gère la formation et les équipes amateurs. La saison sportive court de juillet à juin : la saison 2025-2026 est la dernière saison close, la saison 2026-2027 est en cours de clôture. Le club dispute la deuxième division professionnelle et vise l'accession à l'élite d'ici 2030.

**Chiffres clés de la saison 2025-2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires | 28 M€ : partenariats et publicité 11 M€ ; billetterie et abonnements 6 M€ ; droits audiovisuels et dotations 5 M€ ; hospitalités (loges, salons) 4 M€ ; boutique et licences 2 M€ |
| Matchs à domicile | 15 par saison, environ 12 000 spectateurs en moyenne |
| Effectif | 150 salariés permanents, dont 48 joueurs et entraîneurs ; environ 400 intervenants extérieurs les jours de match (accueil, sécurité, restauration), fournis par des prestataires |
| Stade | 16 000 places, propriété de la communauté d'agglomération, mis à la disposition du club ; modernisation en cours (écran géant, éclairage, réseau sans fil pour le public, contrôle d'accès par billet dématérialisé) |
| Supporters et clients | 7 000 abonnés ; environ 120 000 contacts dans les fichiers du club (billetterie, boutique en ligne, application mobile, lettre d'information) ; 250 entreprises partenaires |
| Budget du système d'information | 0,9 M€ (environ 3 % du chiffre d'affaires) |
| Plan « MONTALBRET 2030 » (adopté en janvier 2027) | mieux connaître les supporters et les partenaires pour développer les recettes hors droits sportifs ; structurer la gouvernance du numérique du club et étudier de nouvelles formes de relation avec les supporters ; fiabiliser l'organisation des jours de match dans un stade modernisé et réduire son empreinte environnementale |

**Organigramme simplifié (juin 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil d'administration | représentants de la holding familiale et de l'association MONTALBRET XV ; se réunit chaque trimestre | — |
| Présidence | président du conseil d'administration | M. Damien ROQUESSOL |
| Direction générale | directrice générale, qui porte le plan « MONTALBRET 2030 » | Mme Inès LAFERRADE |
| Rattaché à la directrice générale | directeur sportif (équipe professionnelle, staff technique et médical, lien avec le centre de formation de l'association) | M. Xavier TOURNEBIAU |
| Rattaché à la directrice générale | directeur commercial et des partenariats (partenaires, hospitalités, loges et salons) | M. Cédric BARRALOU |
| Rattachée à la directrice générale | responsable du pôle marketing et numérique (communication, lettre d'information, réseaux sociaux, application mobile, boutique en ligne) | Mme Léa SOUBIRAC |
| Rattachée à la directrice générale | responsable de la billetterie (abonnements, billets, accueil du public au guichet) | Mme Nathalie ARRIBEUX |
| Rattaché(e) à la directrice générale | responsable administratif et financier (comptabilité, contrôle de gestion, ressources humaines, achats, juridique, système d'information) | vous |
| Rattaché au responsable administratif et financier | responsable informatique | M. Bastien PEYRASTRE |
| Rattaché à la directrice générale | responsable du stade et de la sécurité (exploitation du stade, organisation des jours de match, relations avec les prestataires d'accueil et de sécurité) | M. Franck DOUMERGAT |

### ANNEXE 2.1 – Le numérique du club aujourd'hui (note de synthèse interne, mai 2027)

Note établie à votre demande par le contrôle de gestion, à partir des factures et des notes de frais de la saison 2025-2026 et d'entretiens avec les directeurs.

**A. Qui fait quoi**
- **L'informatique** compte deux personnes, M. Bastien PEYRASTRE, responsable informatique, et un technicien, rattachées au responsable administratif et financier. Un prestataire d'infogérance de l'agglomération assure le support des postes de travail, la messagerie, les serveurs des bureaux et le réseau. L'équipe consacre environ 80 % de son temps au support et à l'exploitation ; une demande d'évolution d'une direction attend en moyenne quatre mois une réponse.
- **Le pôle marketing et numérique** (huit personnes, dont Mme Léa SOUBIRAC, sa responsable) choisit et souscrit lui-même ses outils en ligne : l'application mobile, développée et hébergée par une agence de communication, la boutique en ligne, l'outil d'envoi de la lettre d'information et des courriels, les outils de publication sur les réseaux sociaux et une plateforme de vidéos.
- **La direction sportive** (M. Xavier TOURNEBIAU) gère seule ses outils d'analyse des performances : un logiciel d'analyse vidéo des matchs et un service de suivi physique des joueurs par capteurs portés à l'entraînement, consultés par le staff sur des tablettes, dont certaines sont personnelles.
- **La billetterie** utilise un logiciel de billetterie et d'abonnements en mode SaaS, choisi en 2022 avec l'informatique ; la **direction commerciale et des partenariats** gère les partenaires et les loges sur un tableur et trois services en ligne.

Au total, 23 services en ligne sont souscrits directement par les directions (14 par le pôle marketing et numérique, 6 par la direction sportive, 3 par la direction commerciale et des partenariats), par carte bancaire ou sur note de frais, en acceptant les conditions générales des fournisseurs. Aucun n'a été examiné par l'informatique avant sa souscription ; l'informatique ne détient les accès d'administration que de 11 d'entre eux.

**B. Les dépenses numériques de la saison 2025-2026 (en milliers d'euros)**

| Direction bénéficiaire | Dépenses portées par le budget du SI | Dépenses numériques payées sur le budget propre de la direction |
|---|---|---|
| Administration et finance (dont le socle commun : postes de travail, messagerie, réseau des bureaux, infogérance, équipe informatique) | 400 | 0 |
| Billetterie (logiciel de billetterie et d'abonnements) | 200 | 0 |
| Stade et sécurité (réseau et contrôle d'accès du stade) | 100 | 0 |
| Pôle marketing et numérique (site internet du club) | 100 | 250 (application mobile 120, boutique en ligne 70, réseaux sociaux et vidéos 40, courriels 20) |
| Direction commerciale et des partenariats | 50 | 30 |
| Direction sportive | 50 | 120 (analyse vidéo 70, suivi physique 50) |
| **Total** | **900** | **400** |

Les dépenses numériques du club atteignent ainsi 1,3 M€, dont près d'un tiers échappe au budget du SI et n'est suivi par personne. Par nature, le budget du SI se répartit ainsi : infogérance 250 ; logiciels de gestion et de billetterie 220 ; réseau, télécoms et matériel 200 ; équipe informatique 130 ; projets décidés en cours d'année 100.

**C. Comment les projets sont décidés**
- Il n'existe ni plan pluriannuel du système d'information, ni instance qui examine les projets numériques ; le conseil d'administration n'a jamais inscrit le numérique à son ordre du jour. Chaque direction présente ses demandes à Mme LAFERRADE quand l'occasion se présente, et la directrice générale tranche au cas par cas.
- 2024 : refonte de l'application mobile, décidée par le pôle marketing et numérique sur proposition de l'agence de communication, découverte par l'informatique à sa mise en ligne.
- 2025 : logiciel d'analyse vidéo acheté pendant l'été sur proposition d'un fournisseur rencontré par le staff, sans avis de l'informatique.
- 2026 : modernisation du stade (écran géant, réseau sans fil, contrôle d'accès par billet dématérialisé), conduite par le responsable du stade et de la sécurité avec la communauté d'agglomération ; l'informatique a été associée au contrôle d'accès trois mois avant sa mise en service.
- Avril 2027 : projet de jetons de supporters (annexe 2.3), présenté directement au président par le pôle marketing et numérique.
- En 2026, 10 des 102 salariés permanents qui ne sont ni joueurs ni entraîneurs ont suivi une formation aux outils numériques ; aucune formation commune n'est organisée.

**D. Ce que disent les acteurs**

**Mme Inès LAFERRADE, directrice générale** : « Je découvre les projets numériques quand la facture arrive. Je n'ai aucun moyen de comparer une demande du marketing à une demande du staff sportif, et le conseil d'administration me demande où nous en sommes du deuxième axe du plan. »

**M. Bastien PEYRASTRE, responsable informatique** : « On nous appelle quand ça ne marche plus, souvent un soir de match. Je ne connais pas la moitié des outils du marketing ; quand une salariée part, ses accès restent ouverts. Nous sommes deux : nous ne pouvons pas tout faire nous-mêmes, mais nous devrions au moins savoir ce qui existe. »

**Mme Léa SOUBIRAC, responsable du pôle marketing et numérique** : « Si j'attends l'informatique, la saison est finie. Nos supporters vivent sur leur téléphone : il faut tester vite et arrêter vite ce qui ne marche pas. Je veux bien des règles, pas un guichet qui dit non. »

**M. Xavier TOURNEBIAU, directeur sportif** : « Nos outils d'analyse sont un avantage sportif. Je ne veux pas qu'ils attendent un comité, mais je reconnais qu'on ne sait pas où sont stockées les données physiques des joueurs. »

### ANNEXE 2.2 – Autodiagnostic de maturité numérique (avril 2027)

À la demande de Mme LAFERRADE, chaque directeur a positionné le club, seul et sans justificatif, sur six domaines, à l'aide de l'échelle suivante : **1** pratiques individuelles, non documentées ; **2** pratiques répétées au sein d'une direction, non partagées ; **3** règles communes écrites, appliquées par toutes les directions ; **4** règles communes suivies par des indicateurs et des cibles ; **5** amélioration continue à partir des mesures.

| Domaine | Directrice générale | Informatique | Marketing et numérique | Direction sportive | Direction commerciale et des partenariats | Billetterie | Moyenne | Écart entre la note la plus haute et la plus basse |
|---|---|---|---|---|---|---|---|---|
| Stratégie numérique | 2 | 1 | 3 | 2 | 2 | 2 | 2 | 2 |
| Gouvernance et arbitrage des projets | 2 | 1 | 2 | 2 | 1 | 1 | 1,5 | 1 |
| Applications et outils | 3 | 2 | 5 | 5 | 1 | 2 | 3 | 4 |
| Données | 2 | 2 | 3 | 4 | 1 | 3 | 2,5 | 3 |
| Compétences et usages | 3 | 3 | 4 | 4 | 2 | 2 | 3 | 2 |
| Pilotage et mesure | 1 | 2 | 2 | 2 | 1 | 1 | 1,5 | 1 |

Commentaires portés sur les grilles : « nos outils sont les plus modernes du club » (marketing et numérique) ; « nos données de performance sont suivies à chaque entraînement » (direction sportive) ; « je note ce que je vois remonter au support » (informatique) ; « nous travaillons sur un tableur » (direction commerciale et des partenariats).

### ANNEXE 2.3 – Le projet de jetons de supporters (avril-mai 2027)

**A. La proposition de TOKAVÉRA, jeune entreprise créée en 2025 (présentation du 14 avril 2027)**

*Volet 1 – Les jetons de supporters.* Le club émettrait des jetons « MONTALBRET XV », tous identiques et interchangeables, enregistrés sur une blockchain publique que TOKAVÉRA présente comme « l'une des plus utilisées au monde », sans en préciser le mécanisme de consensus. Les supporters les achèteraient en euros, 10 € le jeton, dans une application de TOKAVÉRA, qui leur ouvrirait un portefeuille électronique dont ils détiendraient seuls les clés. Les jetons donneraient accès à trois avantages :
- des votes consultatifs sur des choix secondaires (musique d'entrée des joueurs, maillot de la troisième tenue, nom de la mascotte), une voix par jeton détenu ;
- des tirages au sort, parmi les détenteurs d'au moins 20 jetons, pour des rencontres avec les joueurs ;
- une priorité d'achat de 48 heures sur les billets des matchs les plus demandés.

Les jetons pourraient être revendus entre supporters, à un prix libre, sur les plateformes d'échange de crypto-actifs. TOKAVÉRA n'est pas elle-même prestataire de services sur crypto-actifs : la conservation des jetons pour le compte des supporters qui le souhaitent et leur échange contre des euros seraient assurés par un prestataire partenaire, que TOKAVÉRA présente comme « agréé au titre de MiCA depuis mars 2026 » ; ce prestataire facturerait aux supporters 1 € par mois de frais de tenue de portefeuille. Les votes, avec l'adresse du portefeuille de chaque votant, seraient inscrits sur la blockchain « pour garantir leur transparence ».

*Volet 2 (option) – Les billets enregistrés sur le registre distribué.* Chaque billet serait émis sous la forme d'un jeton unique, inscrit sur la même blockchain avec le numéro de client et le pseudonyme de l'acheteur. La revente ne serait possible que dans l'application de TOKAVÉRA, au prix d'achat majoré de 10 % au plus, avec une commission de 5 € par revente versée au club. Le logiciel de billetterie et le contrôle d'accès du stade devraient être adaptés pour lire ces jetons ; TOKAVÉRA n'a pas chiffré cette adaptation, qui serait à la charge du club.

**B. Coûts et recettes annoncés (en milliers d'euros hors taxes, saisons 2027-2028 à 2029-2030, sans actualisation)**

| Poste | 2027-2028 | 2028-2029 | 2029-2030 |
|---|---|---|---|
| Volet 1 : forfait de mise en place | 150 | — | — |
| Volet 1 : abonnement à la plateforme | 50 | 50 | 50 |
| Volet 1 : commission de TOKAVÉRA | 20 % des ventes de jetons | 20 % des ventes de jetons | 20 % des ventes de jetons |
| Option billets : mise en place | 80 | — | — |
| Option billets : abonnement | 40 | 40 | 40 |
| Ventes de jetons espérées par TOKAVÉRA (15 000 acheteurs à 100 € la première saison) | 1 500 | 250 | 250 |
| Commissions sur les reventes de billets espérées par TOKAVÉRA (6 000 reventes par saison à 5 €) | 30 | 30 | 30 |

**C. Sondage du pôle marketing et numérique (mai 2027)**

Un questionnaire adressé par courriel à tous les abonnés a reçu 1 000 réponses. 15 % des répondants se disent prêts à acheter des jetons, pour 50 € en moyenne la première saison ; 60 % souhaitent pouvoir donner leur avis sur des choix du club « sans avoir à payer » ; 70 % ne possèdent aucun portefeuille de crypto-actifs.

**D. Avis recueillis**

**Mme Léa SOUBIRAC, responsable du pôle marketing et numérique** : « C'est la relation de demain avec les supporters de 20 ans, et 1,5 M€ dès la première saison ! Il faut signer avant la campagne d'abonnement de juillet. Il faudra une vraie campagne de lancement, environ 30 000 € par saison, mais cela vaut le coup. »

**Mme Nathalie ARRIBEUX, responsable de la billetterie** : « Notre logiciel de billetterie propose déjà une bourse de revente entre supporters, à prix plafonné, comprise dans l'abonnement : 1 500 billets y ont été revendus cette saison. Notre problème, ce sont les quelque 300 billets revendus sur les réseaux sociaux, et un jeton sur une blockchain ne me dit pas qui se présente au contrôle d'accès. Et chaque nouveauté se paie au guichet : pour les codes perdus et les portefeuilles bloqués, il faudra un mi-temps, soit environ 30 000 € par saison. »

**M. Alain BORDAVIEILLE, administrateur représentant l'association MONTALBRET XV** : « Le club appartient aussi à son association et à ses supporters. Un vote où celui qui a acheté le plus de jetons pèse le plus, c'est vendre la voix des supporters. Et si le prix des jetons s'effondre sur ces plateformes, ce sont nos familles qui auront perdu de l'argent sous les couleurs du club. »

**Mme Camille ESTRABOUL, abonnée de la tribune Sud depuis huit ans** : « Voter pour le maillot, pourquoi pas. Mais je ne vais pas ouvrir un portefeuille de cryptomonnaie, et si je perds mon téléphone ? Réserver la priorité des billets à ceux qui achètent des jetons, c'est passer devant les abonnés fidèles. »

**E. Extrait du projet de contrat transmis par TOKAVÉRA**

- *Article 1 – Objet.* TOKAVÉRA met à la disposition du club, sous la forme d'un service en ligne accessible par abonnement, la plateforme de création et de vente des jetons, l'application des supporters et un tableau de bord ; elle en assure la mise en place moyennant un forfait.
- *Article 2 – Durée.* Trois saisons, du 1er juillet 2027 au 30 juin 2030, reconduites tacitement par périodes de trois saisons, sauf dénonciation par le club douze mois avant l'échéance.
- *Article 3 – Prix.* Selon le tableau B ci-dessus.
- *Article 4 – Service.* TOKAVÉRA met en œuvre ses meilleurs efforts pour assurer la disponibilité de la plateforme et peut l'interrompre à tout moment pour maintenance.
- *Article 5 – Données.* Les données collectées auprès des supporters (identité, coordonnées, adresses de portefeuille, achats, votes) sont la propriété de TOKAVÉRA, qui peut les utiliser pour ses propres offres et pour celles de ses partenaires. Le club dispose d'un accès en consultation au tableau de bord.
- *Article 6 – Fin du contrat.* À l'échéance ou en cas de résiliation, l'accès du club au tableau de bord est fermé. Les jetons émis demeurent sur la blockchain.
- *Article 7 – Responsabilité.* La responsabilité de TOKAVÉRA est limitée au montant d'une saison d'abonnement. TOKAVÉRA ne répond pas de l'évolution du prix des jetons.
- *Article 8 – Obligations réglementaires.* Le club, en sa qualité d'émetteur des jetons, assume seul les obligations réglementaires liées à leur offre au public, ainsi que les frais de conseil correspondants (le cabinet d'avocats du club estime à 20 000 € un premier avis sur le projet).

### ANNEXE 2.4 – Repères réglementaires et normatifs (au 31/12/2026)

| Texte ou norme | Objet principal | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2023/1114 sur les marchés de crypto-actifs (« MiCA ») | Définit le crypto-actif comme une représentation numérique d'une valeur ou d'un droit pouvant être transférée et stockée de manière électronique au moyen de la technologie des registres distribués ou d'une technologie similaire. Encadre l'offre au public et l'admission à la négociation de crypto-actifs (information des acheteurs par un livre blanc établi par une personne morale), l'émission des jetons qui visent une valeur stable, et l'agrément des prestataires de services sur crypto-actifs (PSCA), parmi lesquels la conservation de crypto-actifs pour le compte de clients et leur échange contre des fonds. Sont exclus de son champ les crypto-actifs uniques et non fongibles avec d'autres crypto-actifs, ainsi que les instruments financiers. Il ne fixe ni traitement comptable ni régime fiscal pour ces actifs. | Applicable depuis le 30/12/2024. La période transitoire des prestataires enregistrés sous l'ancien régime français des prestataires de services sur actifs numériques (PSAN) a pris fin le 01/07/2026 : depuis le 02/07/2026, seuls les PSCA agréés au titre de MiCA peuvent exercer. |
| Règlement (UE) 2016/679 (RGPD) | Protection des données à caractère personnel : données limitées à ce qui est nécessaire aux finalités, conservées pendant une durée limitée, effacées dans les cas prévus par le règlement. | Applicable depuis le 25/05/2018 |
| ISO 22739:2024 | Norme de vocabulaire des chaînes de blocs et des technologies de registres distribués (bloc, nœud, consensus, jeton, contrat intelligent…) ; ce n'est pas une norme d'exigences. | En vigueur (2e édition) |

### Travail à faire

Mme LAFERRADE veut que le numérique serve le plan « MONTALBRET 2030 » au lieu de suivre les opportunités de chaque direction, et que le conseil d'administration puisse suivre le deuxième axe du plan. Elle vous demande de proposer une gouvernance du numérique adaptée à la taille du club, un tableau de bord et une démarche de planification, puis de lui donner un avis argumenté sur le projet de jetons de supporters avant toute signature. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.4 ainsi que vos connaissances professionnelles.

**2.1 – Gouvernance et organisation du numérique du club (3 points)**

a) Après avoir défini la gouvernance du système d'information, caractérisez le modèle organisationnel de fait de la fonction numérique du club et trois de ses effets, puis analysez les enjeux relationnels entre la direction générale, l'informatique et les directions métiers, à partir de l'annexe 2.1.

b) Recommandez, en le justifiant, un modèle organisationnel adapté à un club de cette taille, puis proposez deux instances de gouvernance (composition, fréquence, décisions) et trois règles d'achat et d'usage des services en ligne par les directions.

**2.2 – Maturité numérique et tableau de bord du SI (2 points)**

a) Présentez l'intérêt et deux limites d'une évaluation de la maturité numérique, en vous référant à un modèle ou à un référentiel de maturité, puis interprétez la grille de l'annexe 2.2 : deux forces, deux faiblesses et deux biais de cet autodiagnostic.

b) Proposez le tableau de bord du SI que vous présenterez chaque trimestre à Mme LAFERRADE, en quatre indicateurs dont au moins un de dimension environnementale, sociale ou de gouvernance (ESG) ; pour chacun, précisez la formule, la source, la fréquence, la cible et l'axe du tableau de bord.

**2.3 – Chaîne de valeur et planification stratégique du SI (2,5 points)**

a) Après avoir présenté la chaîne de valeur et son intérêt pour aligner le SI sur la stratégie, appliquez-la à MONTALBRET XV pour désigner les trois activités que le SI doit soutenir en priorité au service du plan « MONTALBRET 2030 », en justifiant chaque choix par les annexes 1.1 et 2.1.

b) Proposez la démarche de planification stratégique du SI qui remplacera les décisions prises au fil des opportunités : étapes, horizon, acteurs et trois critères d'arbitrage des projets.

**2.4 – Le projet de jetons de supporters (3,5 points)**

a) Après avoir présenté le fonctionnement d'une blockchain (registre distribué, consensus, clés, blockchain publique ou permissionnée) et ce qui la distingue d'une base de données centralisée, rattachez chacun des deux volets du projet de l'annexe 2.3 à la typologie des applications de la blockchain.

b) Appréciez, à l'aide d'une grille d'opportunité de cinq critères, la valeur ajoutée et les limites de chacun des deux volets, en tenant compte notamment de l'énergie, de la qualité des données inscrites, de la gouvernance, des données personnelles et de l'image du club.

c) À partir des repères de l'annexe 2.4, identifiez deux éléments du projet que le règlement MiCA encadre et un élément qu'il n'encadre pas, puis concluez par une recommandation argumentée à Mme LAFERRADE.

**2.5 – Coût du projet et projet de contrat (2 points)**

a) Après avoir défini le coût total de possession, estimez de tête, en sommes rondes, le coût du projet sur trois saisons, d'abord pour le volet 1 puis avec l'option, en y intégrant les coûts cachés que révèle l'annexe 2.3, et comparez-le aux recettes espérées par TOKAVÉRA puis à celles que laisse attendre le sondage.

b) Caractérisez le type de contrat proposé, puis relevez trois clauses de l'extrait de l'annexe 2.3 à négocier avant tout engagement ; pour chacune, justifiez votre demande et proposez une formulation de principe.
