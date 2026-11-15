# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 22

**DOSSIER 1 – ÉCLAIRER LA STRATÉGIE DU SYSTÈME D'INFORMATION FACE AUX PLATEFORMES ET EN PILOTER LES COÛTS (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 1.2 – Les plateformes numériques de mise en relation (note de veille de M. Julien HAVERCQ, directeur du réseau et des agences, février 2027)

**A. Ce que nous avons appris, et quand**

En novembre 2026, le directeur logistique de notre premier client du secteur m'a annoncé qu'il passait désormais une partie de ses commandes de missions courtes par une application de réservation. Nous avons alors découvert que deux plateformes de ce type étaient actives dans la région depuis le printemps 2025. Aucune personne n'est chargée de la veille chez QUENTALIS Emploi : les directeurs d'agence remontent ce qu'ils apprennent quand ils y pensent, lors du séminaire annuel du réseau, et je suis le seul à lire la presse professionnelle.

**B. Article de presse (fictif)**

> **« Intérim : les applications de missions express gagnent les entrepôts »** — *La Lettre de l'emploi en Hauts-de-France* (publication fictive), 18 janvier 2027
>
> Elles promettent un renfort « en moins de dix minutes ». Les plateformes numériques de mise en relation s'installent dans les entrepôts de la région. Sur une application, l'entreprise décrit la mission, le jour et l'horaire ; des travailleurs déjà inscrits et notés par les entreprises précédentes l'acceptent d'un geste, à toute heure et sept jours sur sept. Selon les cas, il s'agit d'intérimaires délégués par la plateforme elle-même ou de travailleurs indépendants. La plateforme facture une commission sur chaque mission, présentée comme inférieure à la marge d'une agence traditionnelle, et paie les travailleurs dans les quarante-huit heures. Les entreprises notent les travailleurs, qui notent les entreprises. Les missions de quelques heures à quelques jours, les remplacements du lendemain et les pics du week-end sont les premiers concernés. « Pour une mission de six mois sur une ligne de production, je garde mon agence ; pour un pic de commandes le samedi, j'ouvre l'application le vendredi soir », résume un responsable d'entrepôt.

**C. Effets observés chez deux grands comptes de la logistique (chiffre d'affaires réalisé par QUENTALIS Emploi, en milliers d'euros)**

| Client | 2024 | 2025 | 2026 | Part de ses commandes de missions confiées à une plateforme en 2026 (estimation du client) |
|---|---|---|---|---|
| Client A, logisticien de la grande distribution (entrepôts près d'Arras) | 6 000 | 5 500 | 4 500 | 30 %, surtout des missions de moins de trois jours |
| Client B, prestataire de messagerie (plateforme de tri près de Rouen) | 3 000 | 2 900 | 2 500 | 20 %, surtout des pics du week-end |

En 2024, aucun de ces deux clients n'utilisait de plateforme.

**D. Notre dispositif actuel**

- Les commandes des clients arrivent pour 90 % par téléphone ou par courriel, aux heures d'ouverture des agences (8 h 30 – 18 h 30 en semaine). Le portail des clients permet de commander une mission, mais le formulaire est long et l'agence rappelle le client avant de confirmer : il ne reçoit que 10 % des commandes ; il sert surtout à consulter les factures et à valider les relevés d'heures.
- L'application des intérimaires est utilisée par environ 6 000 des 19 000 intérimaires délégués en 2026, pour consulter leurs bulletins de paie et leurs contrats. Elle ne permet ni d'indiquer ses disponibilités ni de choisir ou d'accepter une mission : les propositions se font par téléphone.
- Selon une enquête de décembre 2026 auprès d'un échantillon d'intérimaires, environ 15 % travaillent aussi par l'intermédiaire d'une plateforme.

**E. Réactions des directeurs d'agence (séminaire du réseau, janvier 2027)**

- M. Patrice HOCQUELET, directeur de l'agence d'Arras : « Ces applications ne font que des missions de quelques heures, sans sélection ni suivi. Les clients reviendront vers nous à la première erreur. »
- Mme Laetitia BRAQUENIER, directrice de l'agence de Fécamp : « Mon client du port veut réserver le soir un cariste pour le lendemain matin ; nous, nous le rappelons le lendemain à 9 heures. »
- M. Franck TILLOMBRE, directeur de l'agence de Compiègne : « Dans l'industrie, nos clients nous paient pour la sélection et le suivi des intérimaires qualifiés. Mais nos meilleurs intérimaires s'inscrivent aussi sur ces applications : ils y choisissent leurs missions. »

**F. Une proposition reçue en février 2027**

APPARIEL, jeune entreprise lilloise fondée en 2024, propose à QUENTALIS Emploi un outil d'intelligence artificielle de rapprochement des candidats et des missions :
- l'outil repose sur l'apprentissage automatique : il apprend, à partir de l'historique des missions de QUENTALIS Emploi de 2019 à 2026 (environ un million de missions), quels profils de candidats ont été retenus par les clients, puis renouvelés ou non ; il utilise les qualifications, l'expérience, les missions passées, la distance entre le domicile et le lieu de mission, les disponibilités déclarées et les évaluations des clients ;
- pour chaque commande, il propose au chargé de recrutement une liste classée des dix candidats qu'il juge les plus adaptés, avec un score de 0 à 100 et l'indication des trois critères qui ont le plus pesé ; APPARIEL ne communique pas davantage sur la manière dont le score est obtenu ;
- APPARIEL annonce un temps de recherche des candidats « divisé par deux » et propose un pilote de six mois dans six agences, pour 60 000 €, raccordement au logiciel de gestion compris.

Remarques de M. Thomas ROUVELIN, directeur des systèmes d'information : « Dans notre historique, les candidats proposés sont ceux que les chargés de recrutement connaissaient : 60 % des 80 000 candidats inscrits n'ont jamais été proposés pour une mission. Dans la logistique et le bâtiment, neuf intérimaires délégués sur dix sont des hommes. Et une chargée de recrutement m'a dit : "Je sais qui vient à l'heure ; un score ne me dira pas pourquoi." »

### ANNEXE 1.3 – Les coûts du système d'information et leur refacturation aux agences (note de Mme Claire MAUBRECQ, directrice administrative et financière, février 2027)

**A. Coûts du système d'information en 2026 (en milliers d'euros)**

| Nature | Montant |
|---|---|
| Redevance du logiciel de gestion du travail temporaire (SaaS) | 1 200 |
| Postes de travail, réseau et téléphonie des agences | 600 |
| Postes de travail, réseau et téléphonie du siège et du centre de services | 100 |
| Portail et application des intérimaires (abonnement et maintenance) | 300 |
| Portail des clients (abonnement et maintenance) | 100 |
| Équipe informatique (9 personnes) | 700 |
| Projets (prestations externes) | 500 |
| **Total** | **3 500** |

**B. La refacturation actuelle**

Chaque agence est un centre de profit : son directeur est évalué sur la marge de l'agence après refacturation des coûts du siège. Depuis 2015, les coûts du système d'information, hors projets et hors postes du siège et du centre de services, soit 2 900 k€ en 2026, sont refacturés aux agences au prorata de leur chiffre d'affaires, soit 1 % du chiffre d'affaires de chaque agence. La clé a été choisie pour sa simplicité, quand le système d'information coûtait environ 1,5 M€. Les agences ne reçoivent qu'une ligne « informatique » sur leur compte de résultat mensuel, sans détail.

**C. Deux contestations (courriels de janvier 2027)**

| Agence | Chiffre d'affaires 2026 | Postes de travail | Contrats de mission établis en 2026 | Bulletins de paie des intérimaires en 2026 | Refacturation 2026 |
|---|---|---|---|---|---|
| Compiègne, spécialisée dans les métiers techniques de l'industrie (missions longues d'intérimaires qualifiés) | 12 000 k€ | 6 | 1 200 | 3 000 | 120 k€ |
| Fécamp, agence généraliste (missions courtes, forte rotation des intérimaires) | 4 000 k€ | 5 | 5 000 | 2 500 | 40 k€ |

- M. Franck TILLOMBRE, directeur de l'agence de Compiègne : « Je paie 120 k€ par an, trois fois plus que Fécamp, pour des intérimaires qui restent six mois en mission et ne nous demandent presque rien. Je finance les agences qui enchaînent les missions d'une journée. »
- Mme Laetitia BRAQUENIER, directrice de l'agence de Fécamp : « On nous facture 40 k€ sans jamais nous dire pour quoi. Quand le logiciel de gestion s'est arrêté le jour de paie d'octobre, mes trois chargées de recrutement ont passé deux jours au téléphone avec les intérimaires ; personne ne l'a compté. Et si vous facturez au contrat, vous pénaliserez les agences qui font des missions courtes, c'est-à-dire le métier de proximité que le plan veut défendre. »

**D. Les services rendus aux agences (estimation de la direction des systèmes d'information)**

La direction des systèmes d'information a rattaché les 2 900 k€ refacturés aux trois services qu'elle rend aux agences ; l'équipe informatique, dont le temps consacré au siège et aux projets est négligé ici, consacre l'équivalent de 400 k€ au support des postes des agences et de 300 k€ à l'assistance sur les commandes, les contrats et les portails.

| Service | Coûts rattachés en 2026 | Contenu | Volume du réseau en 2026 |
|---|---|---|---|
| Poste de travail en agence | 1 000 k€ | postes, réseau et téléphonie des agences (600 k€) ; support des agences par l'équipe informatique (400 k€) | 250 postes de travail, dont une borne d'inscription des candidats par agence |
| Contrat de mission | 700 k€ | portail et application des intérimaires (300 k€) ; portail des clients (100 k€) ; assistance de l'équipe informatique sur les commandes, les contrats et les portails (300 k€) | 140 000 contrats de mission |
| Bulletin de paie | 1 200 k€ | redevance du logiciel de gestion, facturée par l'éditeur au bulletin de paie | 120 000 bulletins de paie des intérimaires |

**E. Autres constats de 2026**

- Les deux arrêts du logiciel de gestion un jour de paie ont mobilisé environ 1 000 heures de travail supplémentaire dans les agences et au centre de services (appels des intérimaires, acomptes établis à la main, ressaisies) ; ces heures ne figurent dans aucun coût du système d'information.
- Environ 40 % des petits clients transmettent encore les relevés d'heures sur papier ; les assistants des agences les ressaisissent dans le logiciel de gestion, soit environ 8 000 heures de travail par an.
- Douze agences ont souscrit leur propre service d'envoi de SMS aux intérimaires, payé sur leurs frais généraux (environ 30 k€ en 2026 au total), hors du budget du système d'information.
- Un tiers des postes de travail des agences ont plus de six ans ; les chargés de recrutement se plaignent de leur lenteur.

**F. Le tableau de bord du système d'information présenté chaque trimestre au comité de direction (établi par la direction des systèmes d'information)**

| Indicateur | 3e trimestre 2026 | 4e trimestre 2026 |
|---|---|---|
| Disponibilité du réseau des agences | 99,7 % | 99,6 % |
| Nombre de demandes d'assistance reçues | 3 400 | 3 900 |
| Délai moyen de traitement des demandes d'assistance | 7 heures | 9 heures |
| Postes de travail gérés | 360 | 360 |
| Taux d'occupation de l'espace de stockage du siège | 70 % | 75 % |
| Mises à jour du logiciel de gestion installées par l'éditeur | 3 | 2 |

Aucun indicateur n'a de cible. Le tableau de bord ne comporte aucune donnée de coût. Lors de la séance de janvier 2027, aucun membre du comité de direction ne l'a commenté.

### ANNEXE 1.4 – Le contrat du logiciel de gestion du travail temporaire (extraits du contrat et note de M. Thomas ROUVELIN, directeur des systèmes d'information, février 2027)

**A. Extraits du contrat conclu avec SOLVÉRANE, éditeur du logiciel**

- *Objet* : mise à disposition, en mode SaaS, du logiciel de gestion du travail temporaire (commandes, contrats de mission, relevés d'heures, paie des intérimaires, facturation), hébergement et maintenance compris.
- *Durée* : cinq ans, du 1er janvier 2023 au 31 décembre 2027. Le contrat est reconduit tacitement pour trois ans, sauf dénonciation par l'une des parties au plus tard six mois avant son échéance, soit le 30 juin 2027.
- *Prix* : redevance de 10 € par bulletin de paie établi, facturée chaque mois.
- *Disponibilité* : « L'éditeur s'efforce d'assurer une disponibilité du service de 99,5 % par mois. » Aucune pénalité n'est prévue. L'éditeur communique ses relevés de disponibilité à la demande du client.
- *Suivi* : une réunion annuelle avec le directeur commercial de l'éditeur.
- *Fin du contrat* : « À l'expiration du contrat, l'éditeur restitue les données du client dans un format standard du marché, selon des modalités et à un prix convenus le moment venu. »
- Le contrat ne comporte aucune clause d'audit.

**B. Note de M. ROUVELIN**

- *Incidents de 2026* : deux arrêts du logiciel un jour de paie, le 6 mars (7 heures) et le 6 octobre (10 heures, la journée entière) ; en octobre, environ 3 000 bulletins de paie ont été établis avec deux jours de retard. L'éditeur n'a fourni aucune explication écrite ; nous ne mesurons pas nous-mêmes la disponibilité du logiciel.
- *Nos autres contrats* : aucun de nos trois contrats principaux (logiciel de gestion, portails, réseau des agences) ne prévoit de pénalités, de clause d'audit ou de plan de réversibilité.
- *Intention de l'éditeur* : par un courrier du 15 février 2027, SOLVÉRANE annonce une redevance de 12 € par bulletin à compter du 1er janvier 2028, soit, à volume constant de 120 000 bulletins, 1 440 k€ par an au lieu de 1 200 k€. Elle propose un renouvellement pour cinq ans.
- *Option 1 – Renouveler en renégociant* : je juge possible d'obtenir 11 € par bulletin (1 320 k€ par an), à condition d'accepter en échange l'engagement de cinq ans qu'elle demande.
- *Option 2 – Consulter d'autres éditeurs* : deux éditeurs interrogés de manière informelle annoncent des redevances de 9 à 11 € par bulletin. Le changement de logiciel coûterait environ 600 k€ (reprise des données, paramétrage, formation de 270 utilisateurs dans les agences et au centre de services) et demanderait environ douze mois ; il ne pourrait donc pas aboutir avant le 31 décembre 2027 et supposerait une prolongation du contrat actuel, que SOLVÉRANE accepterait « aux nouvelles conditions tarifaires ».

### ANNEXE 1.5 – Repères sur l'intelligence artificielle (au 31/12/2026)

| Texte ou norme | Repères utiles | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2024/1689 du 13 juin 2024 établissant des règles harmonisées concernant l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | Approche par les niveaux de risque. Depuis le 2 février 2025, certaines pratiques d'intelligence artificielle sont interdites, et les fournisseurs et les déployeurs (organisations qui utilisent un système d'IA sous leur propre autorité) prennent des mesures pour assurer un niveau suffisant de maîtrise de l'IA de leur personnel. Depuis le 2 août 2025, les fournisseurs de modèles d'IA à usage général ont des obligations propres. Depuis le 2 août 2026, le règlement s'applique de manière générale, notamment ses obligations de transparence. | En vigueur ; application échelonnée |
| Règlement (UE) 2026/1744 du 8 juillet 2026 (omnibus numérique sur l'IA) | Report des obligations relatives aux systèmes d'IA à haut risque : à compter du 2 décembre 2027 pour les systèmes à haut risque énumérés à l'annexe III du règlement 2024/1689, et du 2 août 2028 pour ceux de son annexe I (produits réglementés). | En vigueur depuis le 27/07/2026 |
| ISO/IEC 42001:2023 | Norme internationale qui spécifie les exigences d'un système de management de l'intelligence artificielle (politique, rôles, appréciation des risques, contrôle des systèmes d'IA, amélioration continue) ; son adoption est volontaire. | En vigueur |

QUENTALIS Emploi a demandé à son avocat si l'outil proposé par APPARIEL relèverait des systèmes à haut risque ; la réponse n'est pas encore connue, et cette question n'est pas à traiter.

### Travail à faire

Mme BRÉQUEMONT veut que le système d'information serve la première priorité du plan « QUENTALIS 2030 » : défendre le modèle d'agence de proximité face aux plateformes numériques de mise en relation. Elle vous demande d'éclairer les choix du système d'information qui en découlent, d'apprécier l'outil proposé par APPARIEL, de remettre à plat la refacturation des coûts du système d'information aux agences et son pilotage, et de préparer la renégociation du contrat du logiciel de gestion avant l'échéance du 30 juin 2027. Vous mobiliserez pour cela les annexes 1.1 à 1.5 ainsi que vos connaissances professionnelles.

**1.1 – Plateformes numériques, veille et stratégie du système d'information (4 points)**

a) À partir de l'annexe 1.2, analysez l'impact des plateformes numériques de mise en relation sur le modèle économique de QUENTALIS Emploi, selon trois composantes : la proposition de valeur, la relation avec les clients et avec les intérimaires, les sources de revenus.

b) Après avoir défini la veille technologique, présentez la démarche de veille et quatre outils ou méthodes qui auraient permis à QUENTALIS Emploi d'anticiper cette évolution, en montrant, à partir de l'annexe 1.2, ce qui a manqué.

c) Déduisez de votre analyse trois orientations de la stratégie du système d'information alignées sur le plan « QUENTALIS 2030 », en justifiant chacune par l'enjeu métier auquel elle répond.

**1.2 – L'outil d'IA de rapprochement des candidats et des missions (2 points)**

a) Présentez le fonctionnement, en principe, de l'outil proposé par APPARIEL (données d'apprentissage, classement des candidats, explicabilité) et trois de ses usages pour les agences, en précisant à quelle famille d'intelligence artificielle il appartient.

b) Appréciez deux apports et trois limites de cet outil pour les agences, puis formulez trois conditions de conduite du pilote, en vous appuyant sur les repères de l'annexe 1.5.

**1.3 – Contrôle de gestion du système d'information et refacturation aux agences (4 points)**

a) Après avoir rappelé les fondamentaux du contrôle de gestion appliqué au système d'information (centre de coûts ou centre de services, refacturation interne, responsabilisation), critiquez la clé de refacturation actuelle par deux arguments tirés de l'annexe 1.3.

b) Proposez une refacturation fondée sur les trois unités d'œuvre de l'annexe 1.3 D : calculez le coût unitaire de chaque service, appliquez-le aux agences de Compiègne et de Fécamp, puis formulez deux conditions de mise en œuvre, en répondant à l'objection de Mme BRAQUENIER.

c) Identifiez deux coûts cachés du système d'information, puis, après avoir critiqué le tableau de bord actuel par deux arguments, proposez la revue du dispositif de pilotage des coûts du système d'information (fréquence, acteurs, démarche d'amélioration continue).

**1.4 – Tableau de bord de gouvernance du système d'information (2 points)**

Proposez le tableau de bord de gouvernance du système d'information destiné au comité de direction, qui remplacera celui de l'annexe 1.3 F : précisez ses parties prenantes (destinataires, contributeurs, instance de revue), puis proposez quatre indicateurs, un pour chacune des dimensions suivantes : valeur pour les métiers, coûts, risques, dimension ESG. Pour chaque indicateur, vous préciserez sa formule, sa source, sa fréquence, sa cible et son axe.

**1.5 – Renégociation du contrat du logiciel de gestion (2 points)**

a) Présentez la méthode de négociation que vous proposez à Mme BRÉQUEMONT pour ce contrat (objectifs, marges de négociation, solution de repli, calendrier), en l'appliquant aux données de l'annexe 1.4.

b) Identifiez trois risques du contrat actuel, puis proposez le dispositif de pilotage de la relation avec l'éditeur : comité de suivi, deux indicateurs de niveau de service (formule et cible), clause d'audit, pénalités, réversibilité.
