# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 31

**DOSSIER 1 – ÉCLAIRER LA STRATÉGIE DU SYSTÈME D'INFORMATION ET PRÉPARER LE PROJET DE DOSSIER UNIQUE (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 11, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mai 2027. La Fondation VERLANDRE est une fondation reconnue d'utilité publique, dont le siège est à Tours. Elle est née en 2019 de la réunion de trois associations de parents créées dans les années 1960 et 1970 en Indre-et-Loire et dans le Loir-et-Cher. Elle accompagne environ 2 400 enfants et adultes en situation de handicap dans 40 établissements et services répartis sur 28 sites : instituts médico-éducatifs et services d'éducation spéciale pour les enfants, foyers d'hébergement et maisons d'accueil spécialisées ouverts jour et nuit, services d'accompagnement à domicile et cinq établissements et services d'aide par le travail (blanchisserie, espaces verts, restauration, conditionnement). La Fondation emploie 1 800 salariés (éducateurs, accompagnants, soignants, moniteurs d'atelier, services généraux et siège). Ses produits ont atteint 125 millions d'euros en 2026, financés pour l'essentiel par l'agence régionale de santé et par les deux départements ; les établissements d'aide par le travail réalisent en outre 12 millions d'euros de chiffre d'affaires. Les organisations, les personnes et les données de ce cas sont fictives.

Le projet stratégique « Horizon 2030 », adopté par le conseil d'administration en janvier 2027, fixe quatre orientations : passer d'une logique de places à une logique de parcours, en coordonnant autour de chaque personne les professionnels, la famille et les partenaires ; garantir la qualité et la sécurité de l'accompagnement ; rendre les métiers plus attractifs en redonnant du temps auprès des personnes ; développer un numérique responsable, accessible et éthique. Le projet de « dossier unique de la personne accompagnée », qui doit remplacer les trois logiciels hérités des associations et les dossiers papier, en est le chantier numérique principal.

Vous êtes responsable du contrôle interne et de la performance de la Fondation VERLANDRE depuis 2025, rattaché à la directrice générale, Mme Nathalie BRÉCHEVAL. Elle vous demande trois travaux : éclairer la stratégie du système d'information et préparer le projet de dossier unique (dossier 1) ; organiser et exploiter les données des parcours (dossier 2) ; sécuriser l'accès aux données, préparer la Fondation à une crise cyber et rendre son numérique plus responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de la Fondation VERLANDRE et chiffres clés

La Fondation VERLANDRE est une fondation reconnue d'utilité publique dont le siège est à Tours. Elle est née en 2019 de la réunion de trois associations de parents : l'association GERVELLE, créée en 1962 à Tours, l'association MIRANDELLE, créée en 1968 dans le Loir-et-Cher, et l'association LUMERANDE, créée en 1974 dans le sud de l'Indre-et-Loire. Son conseil d'administration, présidé par M. Henri LABASTROU, réunit un collège des familles et des personnalités qualifiées. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Les établissements et services en 2026**

| Pôle | Établissements et services | Nombre | Personnes accompagnées |
|---|---|---|---|
| Enfance | instituts médico-éducatifs, services d'éducation spéciale | 12 | 700 enfants et adolescents |
| Hébergement | foyers d'hébergement, maisons d'accueil spécialisées, ouverts jour et nuit | 14 | 600 adultes hébergés |
| Domicile | services d'accompagnement à domicile | 9 | 550 adultes accompagnés à domicile |
| Travail | établissements et services d'aide par le travail (blanchisserie, espaces verts, restauration, conditionnement) | 5 | 550 travailleurs handicapés |
| **Total** | 28 sites, en Indre-et-Loire et dans le Loir-et-Cher | **40** | **2 400** |

Environ 900 personnes sont inscrites sur les listes d'attente des établissements et services.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Produits | 125 M€ : environ 110 M€ de financements publics (agence régionale de santé et deux départements), 12 M€ de chiffre d'affaires des établissements d'aide par le travail, 3 M€ de dons, legs et autres produits |
| Effectif | 1 800 salariés : environ 1 100 professionnels de l'accompagnement éducatif et social (dont l'encadrement et les secrétariats des établissements), beaucoup en horaires alternés, de jour, de nuit et le week-end ; 250 soignants et paramédicaux ; 150 moniteurs et encadrants d'atelier ; 200 salariés des services généraux (cuisine, entretien, transport) ; 100 salariés au siège, dont une direction des systèmes d'information de 14 personnes |
| Dépenses du système d'information | environ 3 M€ (2,4 % des produits) |
| Projet stratégique « Horizon 2030 » (janvier 2027) | logique de parcours coordonnés autour de chaque personne ; qualité et sécurité de l'accompagnement ; attractivité des métiers et temps redonné auprès des personnes ; numérique responsable, accessible et éthique ; chantier numérique principal : le dossier unique de la personne accompagnée |

**Le système d'information en quelques lignes**

Chaque association a apporté son logiciel de dossier de la personne accompagnée, d'éditeurs et de versions différents : celui de l'association GERVELLE est utilisé par 18 de ses 20 établissements et services, celui de l'association MIRANDELLE par 9 de ses 13 établissements et services, celui de l'association LUMERANDE par 5 de ses 7 établissements et services ; les huit autres établissements et services tiennent des dossiers papier. La Fondation utilise en outre un progiciel de gestion de la production et de la facturation des établissements d'aide par le travail, un progiciel de paie et de gestion des ressources humaines, un logiciel de planning des équipes, un progiciel comptable, ainsi qu'une messagerie et une suite bureautique en ligne. Les serveurs sont installés dans une salle du siège ; un réseau relie les sites. Le parc compte environ 1 400 ordinateurs, dont beaucoup sont partagés dans les unités, et 600 tablettes et smartphones.

**Organigramme simplifié (mai 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil d'administration | président | M. Henri LABASTROU |
| Direction générale | directrice générale | Mme Nathalie BRÉCHEVAL |
| Siège, rattaché à la directrice générale | directeur administratif et financier | M. Pascal DURANTEL |
| Siège, rattaché au directeur administratif et financier | directeur des systèmes d'information (direction de 14 personnes) | M. Laurent TRÉVENEC |
| Siège, rattachée à la directrice générale | directrice des ressources humaines | Mme Valérie OSMONDE |
| Siège, rattaché à la directrice générale | responsable du contrôle interne et de la performance | vous |
| Siège, rattachée à la directrice générale | déléguée à la protection des données | Mme Agnès PELLEGRAIN |
| Pôles, rattachés à la directrice générale | directrice du pôle Enfance | Mme Corinne LÉVRAUD |
| | directeur du pôle Hébergement | M. Stéphane MARCILHAC |
| | directrice du pôle Domicile | Mme Élodie FARGEAS |
| | directeur du pôle Travail | M. Rémi CAZENOVE |
| Établissements, rattachés au directeur de leur pôle | directeurs d'établissement | — |

Le comité de direction réunit chaque mois la directrice générale, le directeur administratif et financier, la directrice des ressources humaines et les quatre directeurs de pôle.

### ANNEXE 1.2 – Le système d'information de la Fondation trois ans après la réunion des associations (note de M. Laurent TRÉVENEC, directeur des systèmes d'information, et témoignages recueillis en avril 2027)

**A. Des informations saisies plusieurs fois**

La personne accompagnée n'a pas de dossier commun : quand elle passe d'un institut médico-éducatif à un foyer, ou d'un établissement de l'ancienne association GERVELLE à un établissement de l'ancienne association MIRANDELLE, son dossier est imprimé, transmis, puis ressaisi. Une enquête menée auprès des établissements en mars 2027 estime les ressaisies à environ 4 000 jours de travail par an :

| Ressaisie | Estimation (jours par an) |
|---|---|
| Établissement des états d'activité demandés par les financeurs, à partir des trois logiciels de dossier et des dossiers papier | 1 500 |
| Report, entre le dossier et le logiciel de planning des équipes, des présences et des activités des personnes accompagnées | 1 000 |
| Report des présences des travailleurs dans les ateliers vers le progiciel de production et de facturation des établissements d'aide par le travail | 500 |
| Saisie, dans les établissements qui tiennent des dossiers papier, des informations demandées par le siège | 1 000 |
| **Total** | **4 000** |

**B. Les échanges avec les partenaires**

| Partenaire (type d'organisme) | Informations échangées | Mode d'échange aujourd'hui |
|---|---|---|
| Maison départementale des personnes handicapées | décisions d'orientation, demandes d'admission | courrier et courriel, ressaisie dans chaque logiciel |
| Les deux départements et l'agence régionale de santé | états d'activité, informations sur les personnes accueillies | tableurs envoyés par courriel |
| Hôpitaux | informations utiles lors d'une hospitalisation et à la sortie | papier remis à l'ambulance, téléphone |
| Écoles | emplois du temps, comptes rendus des réunions de suivi des enfants scolarisés | courriel |
| Familles et représentants légaux | projet personnalisé, informations sur la vie quotidienne, rendez-vous | courrier, téléphone, cahier de liaison |

Chaque établissement a organisé ses propres échanges. Aucun ne dispose d'un moyen d'échange structuré avec un partenaire.

**C. Huit projets demandés, aucun ordre de priorité**

| Repère | Projet | Demandé par | Objectif annoncé | Charge estimée pour la DSI (jours) | Échéance souhaitée | Remarque de la DSI |
|---|---|---|---|---|---|---|
| P1 | Dossier unique de la personne accompagnée | directrice générale | un dossier par personne tout au long de son parcours (annexe 1.3) | 1 400 | 2028 | remplace les trois logiciels de dossier et le papier ; suppose des postes et un réseau adaptés |
| P2 | Portail des familles | pôle Enfance, représentants des familles au conseil d'administration | consulter le projet personnalisé et les informations de la vie quotidienne, prendre rendez-vous | 300 | 2027 | n'a de sens que s'il puise ses informations dans le dossier unique |
| P3 | Planning en ligne des équipes | directrice des ressources humaines | permettre aux salariés de consulter leur planning et d'accepter un remplacement depuis leur smartphone | 400 | 2027 | le logiciel actuel n'est consultable que sur les postes des unités ; doit échanger avec la paie et avec le dossier |
| P4 | Gestion de la production des ateliers | pôle Travail | planifier la production des ateliers, suivre les commandes des clients | 350 | 2028 | le progiciel actuel facture mais ne planifie pas ; il reste maintenu par son éditeur jusqu'en 2030 |
| P5 | Signature électronique | directeur administratif et financier, directrice des ressources humaines | signer à distance les contrats, les devis des ateliers et les documents remis aux familles | 100 | 2027 | service en ligne simple à mettre en place |
| P6 | Téléaccompagnement à domicile | pôle Domicile | entretiens par visioconférence et messages entre les accompagnants et les personnes accompagnées à domicile | 250 | 2027 | proposé par un éditeur ; suppose que les personnes soient équipées et accompagnées |
| P7 | Renouvellement des postes | DSI | remplacer environ 400 ordinateurs des unités trop anciens pour les services en ligne récents | 300 | 2027-2028 | préalable au dossier unique dans une partie des établissements |
| P8 | Outil de pilotage | directeur administratif et financier, conseil d'administration | tableaux de bord de l'activité et des parcours | 500 | 2027 | les données sont aujourd'hui dispersées dans trois logiciels et sur papier |

Si tous ces projets étaient lancés ensemble, ils représenteraient environ 3 600 jours de travail pour la DSI. Une fois l'exploitation et le support assurés, la DSI peut consacrer aux projets environ 1 200 jours par an.

**D. L'organisation de la fonction système d'information**

- La direction des systèmes d'information est installée au siège et rattachée au directeur administratif et financier. Elle compte 14 personnes : le directeur, 6 techniciens de support et de proximité qui se déplacent sur les 28 sites, 3 administrateurs des infrastructures et du réseau, 3 chargés d'applications (dossiers des personnes, ressources humaines et paie, gestion et ateliers) et 1 assistante chargée des achats. Elle décide seule des choix techniques et des achats de matériel. Le directeur des systèmes d'information n'assiste pas au comité de direction.
- En 2026, la DSI a reçu environ 600 demandes d'évolution ou de nouvel outil, par courriel ou par téléphone, sans formulaire ni circuit de validation ; 40 % n'ont reçu aucune réponse. Le délai moyen d'intervention d'un technicien sur un site est de 3 jours ouvrés ; aucun support n'est assuré la nuit ni le week-end.
- Les établissements ont souscrit eux-mêmes, sur leur budget, une trentaine de services en ligne (messageries instantanées pour les transmissions entre équipes, partage de photos avec les familles, outils de planning d'unité), sans avis de la DSI. Dans plusieurs établissements, un salarié à l'aise avec l'informatique dépanne ses collègues, sans mission définie ni temps reconnu.

**E. Témoignages**

- **Mme Nathalie BRÉCHEVAL, directrice générale** : « Chaque semaine, un directeur vient me demander son outil, et la DSI me dit qu'elle ne peut pas tout faire. Je veux une feuille de route numérique 2027-2030 que le conseil d'administration puisse comprendre et qui serve "Horizon 2030". Le dossier unique passe avant tout le reste. »
- **M. Laurent TRÉVENEC, directeur des systèmes d'information** : « Je découvre les projets des pôles quand ils sont décidés et les services souscrits par les établissements quand ils tombent en panne. Je reçois des demandes contradictoires que personne n'arbitre. Avec 14 personnes, je ne peux être ni sur les 28 sites ni sur huit projets à la fois. »
- **M. Yann BOSSERAND, directeur d'un foyer d'hébergement** : « Il faut trois jours pour qu'un technicien vienne, et la nuit il n'y a personne. Mes équipes ont créé un groupe de messagerie pour les transmissions : ce n'est pas bien, mais c'est ce qui marche. On ne m'a jamais demandé mon avis sur un projet informatique. »
- **Mme Corinne LÉVRAUD, directrice du pôle Enfance** : « Le portail des familles est promis depuis 2024. Je veux qu'on décide avec les établissements, pas pour eux. »
- **Mme Martine ROUSSELIÈRE, représentante des familles au conseil d'administration** : « Quand mon fils est passé de l'institut médico-éducatif au foyer, j'ai raconté son histoire trois fois. Je voudrais lire son projet personnalisé et le signer sans me déplacer. »
- **M. Pascal DURANTEL, directeur administratif et financier** : « Les dépenses du système d'information représentent 2,4 % de nos produits ; les abonnements pris par les établissements n'y figurent même pas. Nous ne pourrons pas tout financer en même temps. »

### ANNEXE 1.3 – Le projet de dossier unique de la personne accompagnée (note de cadrage de Mme Laure DESVIGNAC, cheffe de projet, avril 2027)

**A. Objectifs**

1. Un seul dossier par personne, de l'admission à la sortie et d'un établissement à l'autre, quelle que soit l'ancienne association.
2. Des transmissions écrites entre les équipes de jour et de nuit, saisies au plus près des personnes, sur tablette ou sur smartphone.
3. Le projet personnalisé de chaque personne, construit avec elle et sa famille, suivi et révisé dans le dossier.
4. La consultation d'une partie du dossier par la famille ou le représentant légal, selon des droits définis pour chaque personne.
5. La fin des dossiers papier et des ressaisies, et des informations fiables pour le pilotage.

**B. L'offre retenue**

Après la consultation de quatre éditeurs à la fin de 2026, le comité de direction a retenu l'offre en ligne de la société ORLINÈVE. Elle couvre le dossier de la personne, le projet personnalisé, les transmissions et l'agenda des activités des personnes, ainsi qu'un module de portail des familles, en option. Elle ne couvre ni le planning des équipes, ni la production et la facturation des ateliers, ni la paie. Elle propose des interfaces de programmation (API) documentées pour échanger des données avec d'autres applications, et une application pour tablette et smartphone qui fonctionne brièvement sans connexion. L'éditeur met à jour son offre quatre fois par an, pour tous ses clients à la fois.

L'offre satisfait aux exigences légales applicables à l'hébergement des données de santé ; ce point n'est pas à analyser.

| Élément | Proposition de l'éditeur |
|---|---|
| Abonnement | 25 € par compte utilisateur et par mois, pour environ 1 600 comptes (utilisateurs formés et remplaçants), soit environ 480 k€ par an |
| Durée | engagement de cinq ans, renouvelable par tacite reconduction |
| Mise en service | paramétrage et reprise des données des trois logiciels : forfait de 300 k€ ; la formation est chiffrée à part (annexe 1.4) |

**C. Les points encore ouverts du projet de contrat**

| Point | Rédaction proposée par l'éditeur | Observation de la cheffe de projet |
|---|---|---|
| Niveaux de service et plages de disponibilité | disponibilité visée de 99 %, mesurée du lundi au vendredi de 8 heures à 18 heures ; support joignable aux mêmes heures | 14 établissements fonctionnent jour et nuit, toute l'année |
| Pénalités | aucune pénalité ; geste commercial possible en cas d'incident majeur | — |
| Confidentialité | engagement général de confidentialité ; l'éditeur peut utiliser des données « rendues anonymes » pour améliorer ses services | dossiers de personnes vulnérables |
| Sous-traitance ultérieure | l'éditeur peut recourir aux sous-traitants de son choix, dont l'hébergeur, sans en informer la Fondation | — |
| Localisation des données | données hébergées dans l'Union européenne ; copies de sauvegarde « dans les centres de l'hébergeur » | lieu des copies non précisé |
| Réversibilité | en fin de contrat, export des données sur demande, au format de l'éditeur, facturé sur devis ; suppression des données 30 jours après la fin du contrat | — |
| Limitation de responsabilité | responsabilité de l'éditeur plafonnée à trois mois d'abonnement ; exclusion des dommages indirects, dont la perte de données | — |

### ANNEXE 1.4 – Les contraintes du déploiement (note de Mme Laure DESVIGNAC, cheffe de projet, et de Mme Valérie OSMONDE, directrice des ressources humaines, avril 2027)

**A. Les utilisateurs à former**

| Profil | Personnes | Formation par personne |
|---|---|---|
| Professionnels de l'accompagnement de terrain | 1 000 | 6 heures |
| Encadrement et secrétariats des établissements | 100 | 10 heures |
| Soignants et paramédicaux | 250 | 4 heures |
| Moniteurs et encadrants d'atelier | 150 | 2 heures |
| Salariés du siège (admissions, qualité, directions) | 50 | 2 heures |
| Référents numériques (formation complémentaire, voir E) | 40 | 15 heures |

Convention : une heure de formation coûte en moyenne 40 €, charges comprises, remplacement des professionnels compris. La formation des formateurs internes et des référents par l'éditeur coûte en outre 40 k€ (40 jours à 1 000 €). Les heures des référents s'ajoutent à celles de leur profil.

**B. Les contraintes d'organisation**

- Dans les foyers et les maisons d'accueil spécialisées, ouverts jour et nuit toute l'année, les professionnels travaillent en trois équipes (matin, après-midi, nuit) et un week-end sur deux ; les équipes se relaient lors d'une relève d'une demi-heure. Aucune unité ne peut fonctionner avec moins de professionnels que prévu.
- La directrice des ressources humaines fixe deux règles : pas plus d'un professionnel sur dix d'une même unité en formation au même moment ; des séances de trois heures au plus.
- Dans les huit établissements et services qui tiennent des dossiers papier, la plupart des professionnels n'utilisent pas d'ordinateur dans leur travail.
- Six sites éloignés ont un accès à internet lent, coupé plusieurs fois par mois.
- La DSI peut accompagner sur place au plus 15 établissements et services à la fois pendant leur mise en service ; l'éditeur met à disposition six formateurs.

**C. Deux options de déploiement**

| | Option 1 : tous les établissements en une fois | Option 2 : par vagues de pôles |
|---|---|---|
| Calendrier | mise en service des 40 établissements et services en janvier 2028 ; formation de tous les utilisateurs entre octobre et décembre 2027 | pilote sur un site de trois établissements et services (un service à domicile, un institut médico-éducatif, un foyer) en octobre 2027 ; vague 1 : pôles Travail et Domicile (13 établissements et services) en février 2028 ; vague 2 : pôle Enfance (11) en juin 2028 ; vague 3 : pôle Hébergement (13) en octobre 2028 |
| Fin du déploiement | mars 2028 | décembre 2028 |
| Anciens logiciels | arrêtés en mars 2028 | maintenus jusqu'à la dernière vague, soit environ neuf mois de plus ; les trois anciens logiciels coûtent ensemble environ 20 k€ par mois |
| Parcours | — | pendant le déploiement, une personne qui passe d'un pôle déjà équipé à un pôle qui ne l'est pas encore change d'outil |

**D. Les risques signalés par l'équipe projet**

- **Reprise des données** : trois logiciels aux contenus différents, des doublons, des dossiers papier ; les extractions des anciens logiciels sont fournies par leurs éditeurs sous forme de fichiers de tableur.
- **Réseau** : six sites dont l'accès à internet est insuffisant pour un service en ligne utilisé en continu.
- **Appropriation** : des professionnels peu à l'aise avec l'écrit et avec l'informatique ; des équipes de nuit isolées ; la crainte que l'écran prenne le temps passé auprès des personnes.
- **Dépendance à l'éditeur** : engagement de cinq ans, mises à jour imposées quatre fois par an, aucune solution de remplacement si l'éditeur disparaît.
- Les essais de paramétrage réalisés en mars 2027 ont utilisé des copies de vrais dossiers de personnes accompagnées.

**E. Les référents numériques envisagés**

- Un référent numérique par établissement ou service (40 au total), volontaire, choisi parmi les professionnels de l'accompagnement ; 10 % de son temps (une demi-journée par semaine) pendant le déploiement, puis 5 %.
- Missions envisagées : aide de premier niveau aux collègues, relais des besoins et des difficultés vers l'équipe projet, formation des nouveaux arrivants.
- Réserves exprimées : des directeurs d'établissement craignent que ce temps soit pris sur l'accompagnement ; des référents de nuit ou de sites éloignés se sentiront seuls. En 2021, l'ancienne association MIRANDELLE avait désigné des « super-utilisateurs » lors d'un changement de logiciel : faute d'animation, de temps reconnu et de lieu d'échange, le réseau s'était éteint en moins d'un an.
- La suite bureautique en ligne de la Fondation comprend des espaces d'équipe, une messagerie instantanée et la visioconférence, peu utilisés hors du siège.

### ANNEXE 1.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Le responsable du traitement ne fait appel qu'à un sous-traitant présentant des garanties suffisantes ; un contrat encadre le traitement (objet, durée, instructions du responsable, confidentialité des personnes autorisées, sécurité, aide au responsable, sort des données à la fin de la prestation, mise à disposition des informations et audits). Le sous-traitant ne recrute un autre sous-traitant qu'avec l'autorisation écrite, préalable, spécifique ou générale, du responsable, qui peut s'opposer aux changements. Un transfert de données hors de l'Union européenne n'est possible que dans les conditions prévues par le règlement. | Applicable depuis le 25/05/2018. Une proposition européenne de simplification (« omnibus numérique », 19/11/2025) modifiant ce règlement est en discussion et n'est pas applicable. |
| ITIL (PeopleCert) | Référentiel de bonnes pratiques de gestion des services informatiques : gestion des niveaux de service, des incidents et des changements. | En vigueur |

Il n'est demandé aucune analyse juridique du contrat ni des obligations de la Fondation.

### Travail à faire

Trois ans après la réunion des trois associations, le système d'information de la Fondation VERLANDRE reste celui de trois organisations, et les demandes des établissements s'accumulent sans être arbitrées. Mme BRÉCHEVAL vous demande d'éclairer la stratégie du système d'information au service du projet « Horizon 2030 », d'organiser la fonction système d'information entre le siège et les établissements, de dessiner l'architecture cible autour du dossier unique, puis de préparer le contrat avec l'éditeur, le déploiement et l'accompagnement des professionnels. Vous mobiliserez pour cela les annexes 1.1 à 1.5 ainsi que vos connaissances professionnelles.

**1.1 – La stratégie du système d'information et la feuille de route numérique 2027-2030 (3 points)**

a) Après avoir précisé ce qu'est une stratégie du système d'information alignée sur la stratégie de l'organisation, montrez, à partir de l'annexe 1.2, en quoi le système d'information actuel freine trois des quatre orientations du projet « Horizon 2030 ».

b) Proposez la démarche de construction de la feuille de route numérique 2027-2030 : ses étapes, ses acteurs et quatre critères de priorisation des projets. Appliquez ensuite ces critères aux huit projets de l'annexe 1.2 C en les classant en trois horizons (second semestre 2027 et 2028 ; 2029 ; 2030), et justifiez votre classement. Aucun calcul de rentabilité n'est attendu.

**1.2 – L'organisation de la fonction système d'information (2,5 points)**

a) Caractérisez le modèle d'organisation actuel de la fonction système d'information de la Fondation, puis analysez trois tensions entre la direction des systèmes d'information, la direction générale et les directeurs d'établissement, révélées par l'annexe 1.2.

b) Recommandez, en la justifiant, l'organisation cible de la fonction système d'information entre le siège et les établissements : le modèle retenu et le rattachement du directeur des systèmes d'information, le rôle des référents numériques des établissements, et trois règles de demande et d'arbitrage des projets.

**1.3 – L'architecture cible autour du dossier unique (2,5 points)**

Après avoir défini l'urbanisation du système d'information, représentez, sous la forme d'un schéma ou d'un tableau, l'architecture cible du système d'information de la Fondation autour du dossier unique, en faisant apparaître le référentiel des personnes accompagnées, le dossier unique, le planning des équipes, la production et la facturation des ateliers, le portail des familles et les échanges avec les partenaires. Montrez ensuite, en trois arguments, comment l'urbanisation assure la cohérence entre le système d'information de la Fondation et ceux de ses partenaires extérieurs. Ni le contenu du référentiel ni le détail des échanges ne sont attendus.

**1.4 – Le contrat de service en ligne avec ORLINÈVE (2 points)**

À partir des annexes 1.3 et 1.5, proposez quatre clauses à négocier dans le contrat de service en ligne : les niveaux de service et les pénalités ; la confidentialité et la sous-traitance au sens du RGPD ; la responsabilité ; la réversibilité. Pour chacune, précisez le contenu que vous demanderez et reliez-la à un risque pour la Fondation, tiré des annexes. Aucune analyse juridique n'est attendue.

**1.5 – Le déploiement du dossier unique (2 points)**

a) Comparez les deux options de déploiement de l'annexe 1.4 C, puis recommandez l'une d'elles en la justifiant.

b) Établissez de tête, en milliers d'euros, l'enveloppe de la formation des utilisateurs, puis indiquez comment planifier les formations et les ressources du déploiement sans interrompre l'accompagnement des personnes.

c) Identifiez trois risques du projet, portant respectivement sur la maintenance, l'évolutivité et la sécurité, en les appuyant sur les annexes 1.3 et 1.4, et proposez pour chacun une mesure de traitement.

**1.6 – La communauté de pratiques des référents numériques (2 points)**

Après avoir défini une communauté de pratiques et précisé ce qu'elle apporte à la gestion des connaissances, proposez celle des référents numériques qui accompagnera le déploiement du dossier unique : ses objectifs, son animation, ses outils, les rôles et responsabilités de ses acteurs, et un indicateur de pilotage précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Vous tiendrez compte des réserves exprimées dans l'annexe 1.4 E. La gestion des compétences n'est pas à traiter.
