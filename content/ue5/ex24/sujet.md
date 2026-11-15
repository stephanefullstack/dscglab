# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 24

**DOSSIER 3 – SÉCURISER LE SYSTÈME D'INFORMATION DU RÉSEAU, TRANSMETTRE LES SAVOIR-FAIRE ET RENDRE LE NUMÉRIQUE PLUS RESPONSABLE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 8, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. QUENTALIS Emploi est une entreprise de travail temporaire indépendante dont le siège est à Amiens. Fondée en 1994 par M. Arnaud VERQUELLE, qui la préside toujours, elle est constituée en société par actions simplifiée, détenue à 70 % par la famille fondatrice et à 30 % par vingt-cinq cadres et directeurs d'agence. Elle exploite un réseau de 46 agences en Hauts-de-France et en Normandie, qui délèguent des intérimaires auprès d'environ 3 200 entreprises clientes de l'industrie, de la logistique, du bâtiment et du tertiaire ; un centre de services installé à Amiens assure la paie des intérimaires, la facturation et la relation avec les intérimaires. QUENTALIS Emploi emploie 310 salariés permanents et a délégué en 2026 environ 19 000 intérimaires différents, soit 5 800 personnes en équivalent temps plein. Son chiffre d'affaires de 2026 s'élève à 290 millions d'euros ; 3,5 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « QUENTALIS 2030 », adopté par le comité de direction en décembre 2026, fixe trois priorités : défendre et moderniser le modèle d'agence de proximité face aux plateformes numériques de mise en relation ; mieux exploiter les données des commandes, des missions et des intérimaires pour servir plus vite et plus sûrement les clients ; sécuriser le système d'information, transmettre les savoir-faire des équipes et réduire l'empreinte du numérique. La directrice générale, Mme Nadia BRÉQUEMONT, en rend compte chaque trimestre au président.

Vous êtes contrôleur de gestion de QUENTALIS Emploi depuis 2025, rattaché à la directrice administrative et financière, et chargé du pilotage économique du système d'information et des projets de transformation. Mme BRÉQUEMONT vous demande trois travaux : éclairer la stratégie du système d'information et en piloter les coûts (dossier 1) ; organiser et exploiter les données des commandes et des missions (dossier 2) ; sécuriser le système d'information du réseau, transmettre les savoir-faire et rendre le numérique plus responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de QUENTALIS Emploi et chiffres clés

QUENTALIS Emploi est une société par actions simplifiée, entreprise de travail temporaire indépendante fondée en 1994, dont le siège est à Amiens. Elle est détenue à 70 % par la famille fondatrice et à 30 % par vingt-cinq cadres et directeurs d'agence. Ses agences recrutent des intérimaires et les délèguent auprès d'entreprises clientes ; le centre de services d'Amiens établit la paie des intérimaires et la facturation des clients et répond aux questions des intérimaires. L'exercice social coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires | 290 M€ : industrie 40 % (116 M€), logistique 30 % (87 M€), bâtiment 20 % (58 M€), tertiaire 10 % (29 M€) |
| Clients | environ 3 200 entreprises clientes, dont une trentaine de grands comptes qui représentent environ 35 % du chiffre d'affaires |
| Intérimaires et candidats | environ 19 000 intérimaires différents délégués dans l'année, soit 5 800 personnes en équivalent temps plein ; environ 80 000 candidats inscrits dans le fichier |
| Réseau | 46 agences en Hauts-de-France et en Normandie ; un centre de services à Amiens ; le siège à Amiens |
| Effectif permanent | 310 salariés : environ 200 dans les agences (directeurs d'agence, chargés de recrutement, assistants), 70 au centre de services (paie des intérimaires, facturation, relation avec les intérimaires), 40 au siège, dont une équipe informatique de 9 personnes ; forte rotation des chargés de recrutement |
| Système d'information | un logiciel de gestion du travail temporaire, en mode SaaS, fourni par un éditeur spécialisé (commandes des clients, contrats de mission, relevés d'heures, paie des intérimaires, facturation) ; un portail et une application mobile des intérimaires ; un portail des clients |
| Budget du système d'information | 3,5 M€ (environ 1,2 % du chiffre d'affaires) |
| Plan « QUENTALIS 2030 » (adopté en décembre 2026) | défendre et moderniser le modèle d'agence de proximité face aux plateformes numériques de mise en relation ; mieux exploiter les données des commandes, des missions et des intérimaires pour servir plus vite et plus sûrement les clients ; sécuriser le système d'information, transmettre les savoir-faire des équipes et réduire l'empreinte du numérique |

**Organigramme simplifié (mars 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Présidence | président fondateur | M. Arnaud VERQUELLE |
| Direction générale | directrice générale, qui porte le plan « QUENTALIS 2030 » et anime le comité de direction | Mme Nadia BRÉQUEMONT |
| Rattaché à la directrice générale | directeur du réseau et des agences (46 directeurs d'agence) | M. Julien HAVERCQ |
| Rattaché à la directrice générale | directeur commercial et des grands comptes | M. Stéphane DUQUESNEL |
| Rattachée à la directrice générale | responsable du centre de services (paie des intérimaires, facturation, relation avec les intérimaires) | Mme Aurélie CAMBRELIN |
| Rattachée à la directrice générale | directrice administrative et financière (comptabilité, contrôle de gestion, juridique, achats) | Mme Claire MAUBRECQ |
| Rattaché à la directrice administrative et financière | contrôleur de gestion | vous |
| Rattaché à la directrice générale | directeur des systèmes d'information (équipe informatique de 9 personnes) | M. Thomas ROUVELIN |
| Rattachée à la directrice générale | responsable des ressources humaines des salariés permanents | Mme Virginie DORVELLE |

Le comité de direction réunit chaque mois la directrice générale et les six responsables qui lui sont rattachés.

### ANNEXE 3.1 – Le système d'information du réseau et deux incidents de 2026 (note de M. Thomas ROUVELIN, directeur des systèmes d'information, février 2027)

**A. Ce que nous protégeons**

| Composant | Utilisateurs | Données traitées |
|---|---|---|
| Postes de travail des agences : environ 200 postes des collaborateurs, souvent partagés entre un chargé de recrutement et un assistant, et 46 bornes d'inscription des candidats en libre-service (une par agence, dans l'espace d'accueil) | environ 200 salariés des agences ; candidats de passage sur les bornes | dossiers de candidats enregistrés sur les postes, messagerie, accès aux applications |
| Logiciel de gestion du travail temporaire, en mode SaaS, utilisé depuis un navigateur | agences et centre de services (270 utilisateurs), ainsi que quelques utilisateurs du siège | commandes, contrats de mission, relevés d'heures, paie des intérimaires, facturation |
| Portail et application mobile des intérimaires | environ 6 000 intérimaires actifs | identité et pièces d'identité, coordonnées bancaires, contrats de mission (la signature en ligne, proposée depuis 2025, a concerné environ 30 % des contrats de 2026), bulletins de paie |
| Portail des clients | utilisateurs des entreprises clientes | commandes, validation des relevés d'heures, factures |
| Messagerie et partage de fichiers, en ligne | tous les salariés permanents | courriels, dossiers partagés des agences et du centre de services |

**B. Qui intervient**

| Acteur | Rôle actuel |
|---|---|
| Direction des systèmes d'information (9 personnes) | choix des applications, administration des comptes du logiciel de gestion, assistance aux agences ; aucune personne n'est chargée de la sécurité |
| Directeurs d'agence (46) | organisent le travail de leur agence, achètent sur leur budget certains équipements et services, décident de qui utilise quel poste |
| Centre de services d'Amiens | paie des intérimaires, facturation, relation avec les intérimaires (téléphone, courriel) ; traite les changements de coordonnées bancaires |
| SOLVÉRANE, éditeur du logiciel de gestion | fournit, maintient et fait évoluer le logiciel ; en confie l'hébergement à un hébergeur établi en France |
| Hébergeur choisi par SOLVÉRANE | exploite les centres de données où tournent le logiciel de gestion et ses sauvegardes ; QUENTALIS Emploi n'a aucun contact direct avec lui |
| Prestataire régional de maintenance des postes | installe et dépanne les postes des agences, à distance ou sur place |
| Délégué à la protection des données | fonction confiée depuis 2018 à un cabinet extérieur, consulté une fois par an |

**C. Incident A – L'arrêt du logiciel de gestion le jour de la paie (6 octobre 2026)**

Le 6 octobre 2026, jour de paie, le logiciel de gestion est resté indisponible pendant 10 heures, soit toute la journée de travail. La paie de 3 000 intérimaires et les acomptes demandés par 1 000 autres, soit 4 000 intérimaires, ont été versés avec deux jours de retard. Le centre de services a reçu environ 3 000 appels en deux jours, contre 500 habituellement, et les agences ont établi à la main des acomptes d'urgence ; ces deux journées ont coûté environ 600 heures de travail supplémentaire. Une centaine de messages critiques ont été publiés sur les réseaux sociaux, et une soixantaine d'intérimaires ont dit à leur agence qu'ils travailleraient désormais pour une autre entreprise de travail temporaire. SOLVÉRANE a expliqué oralement que l'arrêt venait d'une opération de maintenance chez son hébergeur ; nous ignorions qu'une telle opération était prévue un jour de paie, et personne chez nous n'avait été désigné pour décider de la conduite à tenir. Un premier arrêt, de 7 heures, avait déjà eu lieu le 6 mars 2026.

**D. Incident B – Des dossiers de candidats accessibles par un lien public (novembre 2026)**

Le 2 novembre 2026, pour envoyer quinze profils à un client, une chargée de recrutement de l'agence de Beauvais a créé, dans l'outil de partage de fichiers, un lien d'accès public au dossier partagé de l'agence, sans savoir que ce dossier contenait aussi les dossiers complets de 1 200 candidats (curriculum vitae, copies de pièces d'identité, coordonnées, attestations). Le client a transmis le lien à l'un de ses sous-traitants. Le 30 novembre, soit 28 jours plus tard, un candidat qui avait reçu ce lien d'un ami a alerté l'agence ; le lien a été supprimé le jour même. Nous ne savons pas qui a consulté ou téléchargé les dossiers. L'incident n'a été consigné nulle part, le délégué à la protection des données n'en a pas été informé, et aucune décision n'a été prise sur une notification à l'autorité de contrôle ou sur une information des candidats.

### ANNEXE 3.2 – Les pratiques de sécurité constatées (relevé de M. ROUVELIN après la visite de dix agences et du centre de services, janvier 2027)

1. **Comptes partagés** : dans 30 agences sur 46, les collaborateurs se connectent au logiciel de gestion avec un compte unique par agence, dont le mot de passe, inscrit sur un papier près des postes, n'a pas changé depuis 2023 ; on ne sait pas qui a fait quoi.
2. **Pas de politique écrite** : QUENTALIS Emploi n'a pas de politique de sécurité du système d'information ; la charte informatique date de 2016, ne parle ni des portails ni du partage de fichiers, et n'est pas remise aux nouveaux arrivants.
3. **Portail des intérimaires** : la connexion se fait par un identifiant et un mot de passe, sans autre vérification. En 2026, les coordonnées bancaires de 12 intérimaires ont été modifiées par des tiers qui avaient obtenu leur mot de passe : leur paie a été versée sur d'autres comptes.
4. **Changements de coordonnées bancaires** : le centre de services a traité en 2026 une vingtaine de demandes de changement reçues par simple courriel, sans rappeler l'intérimaire.
5. **Données des candidats sur les postes** : les chargés de recrutement enregistrent les dossiers des candidats (dont les copies de pièces d'identité) sur leur poste, sans chiffrement, pour « travailler plus vite » ; deux ordinateurs portables d'agence ont été volés en 2026.
6. **Bornes en libre-service** : les bornes d'inscription des candidats sont reliées au même réseau que les postes des collaborateurs ; dans une agence visitée, une borne permettait d'ouvrir le dossier partagé de l'agence.
7. **Partage de fichiers** : tout salarié peut créer un lien public, sans date d'expiration ; environ 300 liens publics étaient actifs en janvier 2027.
8. **Prestataire de maintenance** : il accède à distance à tous les postes des agences, à tout moment, avec un compte d'administration commun à ses techniciens.
9. **Postes non mis à jour** : environ 40 postes d'agence fonctionnent avec un système d'exploitation qui ne reçoit plus de mises à jour de sécurité de son éditeur.
10. **Responsabilités floues** : les directeurs d'agence considèrent que « la sécurité, c'est l'informatique » ; la direction des systèmes d'information considère que l'usage des postes et des dossiers relève des agences. Douze agences ont souscrit, sans en informer la direction des systèmes d'information, leur propre service d'envoi de SMS aux intérimaires, auquel elles transmettent les numéros de téléphone des intérimaires.
11. **Sensibilisation et incidents** : aucune action de sensibilisation n'a eu lieu depuis 2022 ; aucun registre des incidents n'est tenu ; SOLVÉRANE n'a jamais été interrogée sur la sécurité de son hébergeur.

### ANNEXE 3.3 – Les savoir-faire du réseau (note de Mme Virginie DORVELLE, responsable des ressources humaines des salariés permanents, et témoignages, février 2027)

**A. Le constat**

Les agences comptent environ 100 chargés de recrutement, 46 directeurs d'agence et 54 assistants. En 2026, 35 chargés de recrutement sur 100 ont quitté QUENTALIS Emploi ; leur ancienneté moyenne est de deux ans, et un nouveau chargé de recrutement n'est pleinement autonome qu'au bout de six mois environ. Au centre de services, trois gestionnaires expérimentés traitent l'essentiel des quelque 4 000 anomalies de paie signalées chaque année ; l'un d'eux, M. Olivier DUFRESCQ, part à la retraite fin 2027.

Les savoir-faire les plus difficiles à transmettre sont :
- la connaissance des métiers et des sites des clients (conditions d'accès, équipements de protection, horaires, consignes propres à chaque site) ;
- la qualification des candidats : ce qu'un client entend par « cariste confirmé » ou « soudeur qualifié », les questions à poser en entretien ;
- les règles propres aux grands comptes (circuits de commande, interlocuteurs, exigences de délai) ;
- le traitement des anomalies de paie au centre de services (une trentaine de cas types).

**B. Les outils existants**

- Un intranet ouvert en 2019 : environ 1 500 documents, dont 40 % n'ont pas été mis à jour depuis plus de trois ans ; 15 % des salariés permanents s'y connectent au moins une fois par mois ; le moteur de recherche donne rarement le bon document.
- Des documents dispersés dans les dossiers partagés de chaque agence, dans les messageries et dans des carnets personnels.
- Un forum interne ouvert en 2022 : une trentaine de messages, presque tous sans réponse ; plus aucun message depuis 2023.
- Le logiciel de gestion permet d'associer à chaque fiche client un lien vers un document ; cette possibilité n'est pas utilisée.

**C. Le projet de la direction du réseau**

M. Julien HAVERCQ, directeur du réseau et des agences, souhaite que « ce que savent les meilleurs ne parte plus avec eux ». Il envisage de désigner des référents par grand secteur d'activité (industrie, logistique, bâtiment, tertiaire) et de rendre les informations sur les clients accessibles depuis le logiciel de gestion, mais il ne veut « ni un nouvel outil que personne n'ouvrira, ni des procédures que personne n'aura le temps d'écrire ».

**D. Témoignages**

- Mme Léa FOUQUERELLE, chargée de recrutement à l'agence de Beauvais depuis deux ans : « Quand ma collègue est partie, j'ai mis trois mois à comprendre ce que notre premier client appelle un "cariste confirmé". Tout était dans sa tête. »
- M. Mehdi SANVOISIN, chargé de recrutement à l'agence d'Évreux depuis quatre mois : « Je n'ouvre pas l'intranet : je ne sais pas si ce que j'y trouve est à jour. Quand j'ai une question, j'appelle une ancienne d'une autre agence, si elle a le temps. »
- Mme Chantal LOMBRECQ, directrice de l'agence d'Abbeville depuis vingt-deux ans : « Je connais chaque site de mes clients, mais je n'ai pas le temps d'écrire des procédures. Montrer, oui ; rédiger, non. »
- M. Olivier DUFRESCQ, gestionnaire de paie au centre de services : « Les anomalies, je les règle de tête. Quand je suis absent, les dossiers attendent. Je veux bien transmettre, mais à qui, et quand ? »

### ANNEXE 3.4 – Le projet d'audit de la paie des intérimaires (courriel de Mme Nadia BRÉQUEMONT, directrice générale, mars 2027)

« En 2026, nous avons établi environ 2 400 bulletins de paie rectificatifs sur 120 000 et corrigé par un avoir environ 2 500 factures, dont 1 500 de grands comptes. Les intérimaires s'en plaignent et deux grands comptes nous ont demandé des explications. Je souhaite faire auditer la chaîne qui va du relevé d'heures à la paie et à la facturation : transmission et validation des relevés, saisies et contrôles dans le logiciel de gestion, traitement des anomalies au centre de services.

Deux options sont sur la table : confier l'audit à une équipe interne, composée de notre contrôleur de gestion et d'une gestionnaire de paie du centre de services, puisque nous n'avons pas d'auditeur interne ; ou le confier à un cabinet spécialisé dans l'audit des systèmes d'information, que nous n'avons encore jamais consulté.

Je veux les conclusions pour le comité de direction de fin mai 2027, soit environ huit semaines, en pleine période de forte activité des agences. J'attends de savoir d'où viennent les erreurs (le logiciel, les saisies, les agences ou les clients), et des recommandations que je puisse présenter au président. Je ne veux pas que le centre de services, déjà sous tension, se sente mis en accusation. Enfin, nous n'avons jamais demandé à SOLVÉRANE d'accéder aux journaux du logiciel ni à la description de ses contrôles. »

### ANNEXE 3.5 – Dématérialisation et parc des agences (note conjointe de M. ROUVELIN et de Mme Aurélie CAMBRELIN, responsable du centre de services, février 2027)

**A. Le projet de dématérialisation**

À compter du 1er septembre 2027, la direction générale prévoit que tous les contrats de mission seront signés dans l'application des intérimaires et que tous les relevés d'heures seront saisis par les clients sur le portail des clients ; l'envoi des documents papier aux intérimaires sera supprimé.

- Enquête de décembre 2026 auprès de 1 000 intérimaires : 20 % n'ont pas de smartphone ou ne savent pas s'en servir pour une démarche en ligne ; 10 % n'ont pas d'adresse électronique personnelle ; 15 % déclarent des difficultés à lire un document écrit en français.
- Pilote de signature exclusivement en ligne dans cinq agences, de septembre à décembre 2026 : sur 6 000 contrats de mission, 20 %, soit 1 200, ont finalement été signés en agence avec l'aide d'un assistant ; 240 réclamations ont été reçues (lien de signature non reçu ou expiré, impossibilité de se connecter, document incompris).
- Mme CAMBRELIN : « Les intérimaires qui ont le plus de mal avec le numérique sont souvent ceux qui ont le plus besoin de nous. Si l'application devient le seul moyen de signer, certains renonceront à des missions. »
- L'application des intérimaires ne fonctionne pas sur les smartphones de plus de cinq ans environ, et sa page d'accueil charge de nombreuses images et vidéos.

**B. Le parc des agences**

| Équipement | Nombre | Âge et usage | Pratique actuelle |
|---|---|---|---|
| Postes des collaborateurs | environ 200 | environ 70 ont plus de six ans et 120 plus de cinq ans ; 40 ne reçoivent plus de mises à jour de sécurité (annexe 3.2) | remplacés à la panne ou à la demande du directeur d'agence ; les anciens postes sont stockés dans les agences ou jetés |
| Écrans | environ 250 | la plupart en bon état | remplacés avec les postes |
| Bornes d'inscription en libre-service | 46 | quatre ans | allumées en permanence, nuits et week-ends compris |
| Imprimantes | environ 150 | deux à quatre par agence, dont des imprimantes individuelles | environ 5 millions de pages imprimées en 2026 (contrats, relevés d'heures, dossiers de candidats) |

Aucune politique de renouvellement n'est écrite. Le prestataire de maintenance propose de remplacer en 2027 les 120 postes de plus de cinq ans par des postes neufs, à 1 k€ pièce, soit 120 k€ ; un fournisseur de postes reconditionnés, garantis trois ans, propose des postes équivalents à 0,5 k€ pièce.

### ANNEXE 3.6 – Repères sur la sécurité et le numérique responsable (au 31/12/2026)

| Texte ou référentiel | Repères utiles | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 du 27 avril 2016 (RGPD) | Le responsable du traitement met en œuvre des mesures techniques et organisationnelles appropriées pour garantir un niveau de sécurité adapté au risque (article 32). Une violation de données personnelles est notifiée à l'autorité de contrôle dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance, sauf si elle n'est pas susceptible d'engendrer un risque pour les personnes (article 33) ; les personnes concernées sont informées si le risque est élevé (article 34). | Applicable depuis le 25/05/2018 |
| ISO/IEC 27001:2022 | Norme internationale qui spécifie les exigences d'un système de management de la sécurité de l'information, fondé sur l'appréciation et le traitement des risques ; son annexe A énumère 93 mesures de sécurité. | En vigueur |
| ISO/IEC 27002:2022 | Guide de mise en œuvre des mesures de sécurité de l'information (mesures organisationnelles, liées aux personnes, physiques et technologiques). | En vigueur |
| ISO/IEC 27005:2022 | Lignes directrices pour la gestion des risques liés à la sécurité de l'information. | En vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI) | Méthode d'appréciation et de traitement des risques numériques, en cinq ateliers, qui intègre les parties prenantes de l'écosystème (prestataires, partenaires). | En vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | 42 mesures de bonnes pratiques (sensibilisation, gestion des comptes, mises à jour, réseau, nomadisme…). | En vigueur |
| Le modèle Zero Trust, avis de l'ANSSI (2021) | Modèle d'architecture qui n'accorde aucune confiance implicite liée à la position sur le réseau et vérifie chaque accès ; l'ANSSI le présente comme une évolution progressive, qui ne remplace pas la défense en profondeur. | En vigueur |
| Loi n° 2021-1485 du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique en France (REEN) | Sensibilisation au numérique responsable, lutte contre le renouvellement trop fréquent des terminaux et soutien au réemploi et au reconditionnement, écoconception des services numériques. | En vigueur |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | Critères d'écoconception des services numériques, dont la compatibilité avec des terminaux anciens et la sobriété des contenus. | En vigueur |

QUENTALIS Emploi n'entre ni dans le champ de la directive (UE) 2022/2555 dite NIS 2, ni dans celui de la directive CSRD sur la publication d'informations en matière de durabilité : ces deux points sont des données de l'énoncé, qui ne sont pas à discuter. Aucune analyse juridique n'est attendue.

### Travail à faire

Les incidents de 2026 ont montré que la sécurité du système d'information du réseau n'est organisée par personne, alors que QUENTALIS Emploi détient les données de 80 000 candidats et verse chaque semaine la paie de plusieurs milliers d'intérimaires. Mme BRÉQUEMONT veut traiter la troisième priorité du plan « QUENTALIS 2030 » : sécuriser le système d'information, transmettre les savoir-faire des équipes et réduire l'empreinte du numérique, sans laisser de côté les intérimaires éloignés du numérique. Elle vous demande aussi de l'éclairer sur l'audit de la paie qu'elle envisage. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.6 ainsi que vos connaissances professionnelles.

**3.1 – Les risques du système d'information du réseau (2,5 points)**

a) Après avoir présenté les trois catégories de risques liés aux systèmes d'information (cybermenaces, défaillances opérationnelles, risques réglementaires et métiers), classez dans ces catégories six risques révélés par les annexes 3.1 et 3.2, deux par catégorie.

b) Retenez trois risques prioritaires en justifiant votre choix, puis indiquez pour chacun le référentiel ou la méthode de l'annexe 3.6 sur lequel vous appuieriez son traitement, en précisant la nature de ce référentiel (norme, guide, méthode ou texte réglementaire).

**3.2 – La politique de sécurité du système d'information du réseau (4 points)**

a) Après avoir défini la politique de sécurité du système d'information et ses objectifs, présentez les trois principes sur lesquels vous la fonderiez, puis six règles prioritaires, deux pour les agences, deux pour le centre de services et deux pour les portails et le partage de fichiers, chacune reliée à un constat des annexes 3.1 et 3.2.

b) Après avoir expliqué ce qu'est une architecture de confiance, présentez, sans entrer dans le détail technique ni dans le paramétrage, trois mesures pour le réseau : l'authentification des intérimaires sur leur portail, la protection des données des candidats, la séparation entre les bornes en libre-service et les postes des collaborateurs. Pour chacune, précisez le risque traité et la limite ou la condition de la mesure.

c) Répartissez les rôles et les responsabilités de la sécurité entre la direction générale, le directeur des systèmes d'information, les directeurs d'agence, SOLVÉRANE et son hébergeur, puis indiquez qui devrait piloter la politique de sécurité au quotidien et à qui cette personne devrait être rattachée.

**3.3 – La transmission des savoir-faire du réseau (2 points)**

a) Après avoir distingué connaissances tacites et connaissances explicites, montrez, à partir de l'annexe 3.3, pourquoi les outils existants n'ont pas suffi, puis proposez un dispositif de gestion des connaissances adapté à un réseau à forte rotation, en présentant deux dispositifs et leur intégration dans l'environnement de travail des chargés de recrutement.

b) Précisez le pilotage et la gouvernance de ce dispositif (rôles, règles de mise à jour), puis proposez trois leviers d'appropriation par les chargés de recrutement et les directeurs d'agence, en répondant aux réserves exprimées dans les témoignages. La gestion des compétences et le recrutement ne sont pas à traiter.

**3.4 – L'audit de la paie des intérimaires (2 points)**

Après avoir défini l'audit du système d'information, exposez à Mme BRÉQUEMONT quatre facteurs de succès et trois points de vigilance de l'audit envisagé à l'annexe 3.4, puis indiquez, en le justifiant, l'option d'auditeur que vous recommandez. La démarche détaillée de la mission n'est pas demandée.

**3.5 – Inclusion et numérique responsable (2,5 points)**

a) Après avoir expliqué ce qu'est une gouvernance du système d'information orientée vers la responsabilité sociétale, montrez comment elle traiterait l'inclusion des intérimaires éloignés du numérique dans le projet de dématérialisation de l'annexe 3.5 : trois mesures (accompagnement, solution de substitution, éthique) et l'instance qui en déciderait.

b) Proposez trois bonnes pratiques de numérique responsable pour le parc des agences et pour l'application des intérimaires, en vous appuyant sur l'annexe 3.5 et sur les repères de l'annexe 3.6, et en tenant compte des constats de sécurité de l'annexe 3.2.

c) Proposez deux indicateurs de suivi, l'un pour l'inclusion, l'autre pour le parc des agences, en précisant pour chacun sa formule, sa source, sa fréquence, sa cible et son axe.
