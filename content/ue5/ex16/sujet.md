# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 16

**DOSSIER 1 – SÉCURISER LE SYSTÈME D'INFORMATION D'UN CABINET QUI TRAVAILLE À DISTANCE (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 6, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mai 2027. CORLANDEAU Expertise est une société par actions simplifiée d'expertise comptable, détenue par ses quatorze associés experts-comptables. Son siège est à Poitiers et elle compte cinq autres bureaux, à Niort, La Rochelle, Angoulême, Saintes et Châtellerault. Elle emploie 180 salariés et accompagne environ 3 000 clients, surtout des TPE et des PME, mais aussi des associations et des professions libérales : tenue et révision de la comptabilité, comptes annuels, déclarations fiscales, paie et conseil aux dirigeants. Son chiffre d'affaires de l'exercice 2026 s'élève à 22 millions d'euros ; 1,1 million d'euros est consacré au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « CORLANDEAU 2030 », adopté par les associés en décembre 2026, fixe trois priorités : sécuriser l'organisation de travail hybride, puisque la moitié des collaborateurs travaillent à distance deux jours par semaine et que les échanges avec les clients sont presque tous dématérialisés ; tirer parti des données que les clients confient au cabinet pour développer une offre de conseil, alors que les honoraires de tenue comptable baissent sous l'effet de l'automatisation ; capitaliser la connaissance technique du cabinet, aujourd'hui dispersée entre les bureaux et concentrée chez quelques associés. La présidente, Mme Hélène VARENNAT, en rend compte chaque trimestre au comité des associés.

Vous avez rejoint CORLANDEAU Expertise en janvier 2027 comme chargé(e) de mission « systèmes d'information et transformation numérique », rattaché(e) à Mme VARENNAT. Elle vous confie trois travaux : sécuriser le système d'information d'un cabinet qui travaille à distance (dossier 1) ; exploiter les données des clients au service du conseil (dossier 2) ; évaluer le pilote de la base de connaissances du cabinet et en conduire la généralisation (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de CORLANDEAU Expertise et chiffres clés

CORLANDEAU Expertise est une société par actions simplifiée d'expertise comptable, détenue par ses quatorze associés experts-comptables. Elle accompagne environ 3 000 clients, surtout des TPE et des PME, mais aussi des associations et des professions libérales, depuis son siège de Poitiers et cinq autres bureaux, à Niort, La Rochelle, Angoulême, Saintes et Châtellerault. Son exercice coïncide avec l'année civile. Son activité connaît une forte période de janvier à mai, qui réunit les clôtures des comptes au 31 décembre et les déclarations fiscales. Les experts-comptables sont tenus au secret professionnel, qui s'étend aux informations que les clients confient au cabinet.

**Chiffres clés de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Activité | tenue et révision de la comptabilité, comptes annuels, déclarations fiscales, paie, conseil aux dirigeants |
| Clients | environ 3 000 : TPE et PME surtout, associations, professions libérales |
| Chiffre d'affaires | 22 M€ |
| Effectif | 180 salariés, dont les 14 associés experts-comptables |
| Organisation du travail | la moitié des collaborateurs travaillent à distance deux jours par semaine ; les échanges avec les clients sont presque tous dématérialisés |
| Budget du système d'information | 1,1 M€ (5 % du chiffre d'affaires) |
| Plan « CORLANDEAU 2030 » (adopté en décembre 2026) | sécuriser l'organisation de travail hybride ; tirer parti des données des clients pour développer une offre de conseil ; capitaliser la connaissance technique du cabinet |

**Répartition des salariés entre les bureaux (décembre 2026)**

| Bureau | Salariés |
|---|---|
| Poitiers (siège) | 60 |
| Niort | 30 |
| La Rochelle | 30 |
| Angoulême | 25 |
| Saintes | 20 |
| Châtellerault | 15 |
| **Total** | **180** |

**Organigramme simplifié (mai 2027)**

| Niveau | Fonction | Rôle |
|---|---|---|
| Direction | présidente, Mme Hélène VARENNAT | dirige le cabinet, met en œuvre le plan « CORLANDEAU 2030 » et en rend compte chaque trimestre au comité des associés |
| Direction | comité des associés (les 14 associés) | adopte les orientations et le budget, arbitre les décisions qui engagent le cabinet |
| Production | six bureaux, chacun dirigé par un associé responsable de bureau | chefs de mission et collaborateurs comptables : tenue, révision, comptes annuels, déclarations fiscales, conseil aux clients du bureau |
| Expertise | pôle technique, au siège, animé par un associé | veille juridique, fiscale et comptable, réponse aux questions techniques des bureaux |
| Expertise | pôle social, au siège, animé par un associé | paie et déclarations sociales des clients, conseil en droit social |
| Fonctions support | rattachées à la présidente | administration et finances, ressources humaines, informatique |

### ANNEXE 1.2 – Le système d'information du cabinet et les usages à distance

*Note de M. Damien QUINTAREL, responsable informatique du cabinet, à Mme VARENNAT (mars 2027)*

**A. Les composants du système d'information**

| Composant | Usage | Fourniture et hébergement |
|---|---|---|
| Logiciel de production comptable | tenue, révision, comptes annuels et déclarations fiscales des 3 000 clients ; pour 300 d'entre eux, le cabinet tient aussi les fiches des fournisseurs et prépare les paiements dans le logiciel de gestion du client, auquel il accède à distance | en mode SaaS, chez un premier éditeur ; données des clients hébergées dans des centres de données situés en France |
| Portail d'échange de pièces et application mobile | les clients y déposent leurs factures, relevés et justificatifs ; les collaborateurs les consultent et les rattachent aux dossiers | fournis par le même éditeur, intégrés au logiciel de production comptable |
| Logiciel de paie | paie et déclarations sociales de 900 clients, soit environ 15 000 bulletins par mois | en mode SaaS, chez un second éditeur ; données des clients et de leurs salariés hébergées hors de l'Union européenne, chez un fournisseur d'informatique en nuage dont le siège est situé hors de l'Union européenne ; le contrat ne dit rien du lieu d'hébergement ; l'éditeur indique qu'un hébergement dans l'Union européenne « est à l'étude » |
| Messagerie et outils collaboratifs | courriels, agendas, visioconférence, partage de fichiers | abonnement auprès d'un éditeur |
| Postes de travail | 180 ordinateurs portables fournis par le cabinet, un par salarié | installés et entretenus par un prestataire informatique local |

Les deux éditeurs proposent, sans supplément de prix, une authentification forte à deux facteurs ; elle n'a été activée chez aucun des deux. Sur la messagerie, elle n'est activée que pour les 14 associés.

**B. Usages constatés (revue que j'ai menée en février 2027)**

1. **Smartphones personnels.** Le cabinet ne fournit de smartphone qu'aux associés. 120 collaborateurs consultent la messagerie du cabinet et l'application mobile du portail sur leur smartphone personnel, sans aucun outil de gestion de ces appareils. En 2026, 6 de ces smartphones ont été perdus ou volés, dont un sans code de verrouillage.
2. **Stockage personnel.** Le partage de fichiers du cabinet est lent depuis le domicile et refuse les fichiers de plus de 20 Mo. Pour travailler sur des pièces volumineuses (grands livres, relevés annuels), des collaborateurs les déposent sur des services de stockage en ligne personnels : 25 dépôts relevés en février.
3. **Lieux publics.** Environ 30 % des connexions à distance aux logiciels du cabinet partent de réseaux sans fil publics (gares, hôtels, cafés), y compris pendant les déplacements chez les clients.
4. **Renforts temporaires.** De janvier à mai 2026, les bureaux ont accueilli 20 renforts temporaires (contrats courts, intérimaires, stagiaires). Les associés responsables de bureau les recrutent et m'en informent par courriel, souvent la veille de leur arrivée ; je crée leurs comptes en copiant les droits d'un collaborateur du même bureau. Personne ne me signale leur départ : au 1er mars 2027, 12 comptes de renforts partis en mai 2026 étaient encore actifs ; l'un d'eux affiche une dernière connexion au portail en septembre 2026, sans que l'on sache par qui.
5. **Mots de passe.** L'accès aux logiciels de production comptable et de paie et au portail repose sur un identifiant et un mot de passe. Aucune revue des droits d'accès n'a jamais été faite.
6. **Règles écrites.** Le cabinet n'a pas de politique de sécurité écrite. La charte informatique date de 2015 : elle ne traite ni du travail à distance, ni des appareils personnels. Aucune action de sensibilisation n'a été organisée depuis 2023.

**C. Les moyens**

L'équipe informatique compte 3 personnes au siège : moi-même et deux techniciens, qui assurent l'assistance aux 180 utilisateurs des six bureaux. Je suis rattaché à la présidente ; je n'ai aucune autorité sur les bureaux, dont chaque associé décide de l'organisation. Le prestataire informatique local s'engage, par contrat, sur l'installation et l'entretien des ordinateurs portables, le réseau des bureaux et les sauvegardes des fichiers du siège ; il ne s'engage sur rien d'autre. Les éditeurs indiquent que « la sécurité des accès des utilisateurs relève du client ». Le cabinet consacre environ 30 k€ par an à la sécurité (logiciels de protection des postes, sauvegardes).

### ANNEXE 1.3 – Deux incidents

**A. Un faux changement de coordonnées bancaires chez un client (février 2027)**

La société Menuiseries FALVERGNE, PME de 40 salariés cliente du bureau de Saintes, confie au cabinet la tenue de sa comptabilité, la mise à jour des fiches de ses fournisseurs et la préparation de ses paiements dans son logiciel de gestion, auquel les collaborateurs du bureau accèdent à distance.

*Le processus en vigueur (décrit par le chef de mission)*
1. Les fournisseurs adressent leurs factures et leurs courriers soit au gérant de la société, soit directement au collaborateur du cabinet chargé du dossier.
2. Lorsqu'un fournisseur annonce un changement de coordonnées bancaires, le collaborateur qui reçoit le courrier modifie lui-même la fiche du fournisseur. Tout collaborateur du bureau qui a accès au dossier peut modifier une fiche. Le logiciel du client conserve la date de la dernière modification d'une fiche, mais ni l'auteur ni les anciennes coordonnées.
3. Chaque vendredi, le même collaborateur prépare, dans le logiciel du client, le fichier des factures fournisseurs arrivées à échéance et le dépose sur l'espace bancaire en ligne de la société.
4. Le gérant valide le virement global dans cet espace bancaire. Il en contrôle le montant total, mais ni le détail des bénéficiaires, ni leurs coordonnées bancaires.
5. Les paiements sont lettrés en comptabilité à la réception des relevés bancaires. Aucun état des fiches fournisseurs modifiées n'est produit, ni rapproché des paiements.

*L'incident*
Le 2 février 2027, le collaborateur chargé du dossier a reçu un courriel paraissant venir du principal fournisseur de bois de la société : son adresse ne différait de l'adresse habituelle que par une lettre. Le courriel annonçait un changement de banque et joignait un relevé d'identité bancaire à l'en-tête du fournisseur. Le collaborateur, en télétravail ce jour-là, a modifié la fiche du fournisseur le jour même. Les 5 et 12 février, deux factures de ce fournisseur, de 18 000 € et de 12 000 €, ont été payées sur le nouveau compte. La fraude a été découverte trois semaines plus tard, lorsque le véritable fournisseur a relancé la société pour ses factures impayées. La banque n'a pu récupérer aucune somme. Le gérant a demandé au cabinet « comment une telle erreur a pu se produire et comment éviter qu'elle se reproduise, chez lui comme chez les autres clients ».

**B. Une tentative d'hameçonnage au cabinet (mars 2027)**

Le 15 mars 2027, en pleine période fiscale, 40 collaborateurs ont reçu un courriel imitant une notification du portail d'échange de pièces : « Votre client a déposé 12 pièces urgentes. Reconnectez-vous pour les consulter. » Le lien ouvrait une fausse page de connexion au portail. Mme Inès BOURGALAT, collaboratrice comptable du bureau de Niort, en télétravail ce jour-là, a remarqué que l'adresse de l'expéditeur ne correspondait pas à celle de l'éditeur ; elle n'a rien saisi et, faute de savoir à qui le signaler, a cherché le numéro du responsable informatique dans l'annuaire et l'a appelé. Celui-ci a bloqué l'expéditeur en fin de matinée. Il a ensuite constaté que 3 collaborateurs avaient cliqué sur le lien et que l'un d'eux avait saisi son identifiant et son mot de passe ; ce mot de passe a été changé le jour même. Les journaux de connexion du portail, conservés 30 jours, ne montrent pas d'accès suspect.

### ANNEXE 1.4 – Positions, proposition d'un éditeur et repères

**A. Positions recueillies en avril 2027**

**Mme Hélène VARENNAT, présidente** : « Après l'affaire FALVERGNE, deux clients m'ont demandé comment nous protégeons leurs données. Je veux que la sécurité devienne l'affaire du comité des associés, et pas seulement celle de l'informatique. Mais je ne veux pas de règles que personne n'appliquera. »

**M. Gérard MONTCLAVEL, associé responsable du bureau de Poitiers** : « Interdisons purement et simplement les smartphones personnels : plus aucune messagerie du cabinet sur un téléphone privé. Le secret professionnel ne se négocie pas. Pour le reste, la sécurité, c'est le travail de l'informatique et du prestataire. »

**Mme Claire FÉRANDOUX, associée responsable du bureau de La Rochelle** : « Interdire est irréaliste : en période fiscale, mes collaborateurs répondent aux clients depuis leur téléphone, le soir comme dans les déplacements. Équiper de smartphones professionnels les 120 collaborateurs concernés coûterait environ 50 k€ à l'achat et 20 k€ par an d'abonnements, à renouveler tous les trois ans. Et ne nous imposez pas une double authentification à chaque connexion en pleine saison. »

**M. Damien QUINTAREL, responsable informatique** : « Un outil de gestion des terminaux mobiles permettrait de séparer, sur le smartphone personnel, un espace professionnel chiffré, que l'on peut effacer à distance sans toucher aux données privées ; il coûterait environ 10 k€ par an pour tous les appareils, installation comprise. Mais je ne peux rien imposer aux bureaux, et je ne suis informé ni des arrivées, ni des départs. »

**Mme Inès BOURGALAT, collaboratrice comptable, bureau de Niort** : « On ne nous a jamais formés : le 15 mars, je ne savais pas à qui signaler ce courriel. Si nous déposons des pièces sur nos espaces personnels, c'est parce que l'outil du cabinet ne fonctionne pas bien depuis la maison. Donnez-nous des outils qui marchent, et nous suivrons les règles. »

**B. Proposition de l'éditeur du logiciel de production comptable (mars 2027)**

L'éditeur propose un module optionnel, présenté comme « l'IA qui met fin à la fraude » :

| Fonction | Ce qu'annonce l'éditeur |
|---|---|
| 1. Détection des anomalies dans les dossiers des clients | Un modèle, entraîné sur l'historique des écritures de tous les cabinets qui utilisent le logiciel, attribue à chaque écriture et à chaque modification de fiche de tiers un score de risque de 0 à 100 : montant ou horaire inhabituel, compte rarement utilisé, facture en double, changement de coordonnées bancaires suivi d'un paiement. Dans les tests de l'éditeur, 9 fraudes sur 10 ont été signalées. L'alerte indique le score, sans détailler les critères qui l'ont produit. |
| 2. Analyse des courriels entrants | Un modèle d'IA générative, fourni par un tiers et hébergé hors de l'Union européenne, lit le texte des courriels reçus par les boîtes du cabinet, repère les tentatives d'hameçonnage et les demandes de changement de coordonnées bancaires, et rédige pour chaque alerte une explication en langage naturel. |

Conditions annoncées : pour un cabinet de la taille de CORLANDEAU, environ 3 000 alertes par mois la première année, dont neuf sur dix ne correspondent à aucune anomalie réelle, avant une baisse « grâce à l'apprentissage » ; en souscrivant, le cabinet accepte que les écritures de ses dossiers, rendues anonymes, servent à améliorer le modèle ; le module signale, mais ne bloque aucun paiement ; prix : 5 k€ d'installation, puis 15 k€ par an. « Avec notre IA, vous pourrez alléger vos contrôles manuels. »

**C. Repères au 31/12/2026**

| Référence | Contenu utile au dossier | Situation au 31/12/2026 |
|---|---|---|
| Directive (UE) 2022/2555 du 14 décembre 2022 (dite « NIS 2 ») | Elle impose aux entités essentielles et importantes, définies selon leur secteur et leur taille, des mesures de gestion des risques (analyse des risques, gestion des incidents, sécurité de la chaîne d'approvisionnement, formation, chiffrement, authentification multifacteur) et engage la responsabilité des organes de direction, qui doivent approuver ces mesures et se former. | Les États membres devaient la mettre en œuvre au plus tard le 17 octobre 2024. En France, le projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité, adopté par le Sénat le 12 mars 2025, est en cours d'examen à l'Assemblée nationale : la loi de mise en œuvre n'est pas promulguée. |
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | L'organisation qui traite des données personnelles pour le compte d'une autre (le cabinet pour la paie de ses clients, l'éditeur pour le cabinet) en assure la sécurité ; toute violation de données présentant un risque est notifiée à l'autorité de contrôle dans les 72 heures. | Applicable depuis le 25/05/2018. |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser la maîtrise de l'IA de leur personnel (article 4, dans sa rédaction issue du règlement (UE) 2026/1744). | Obligation applicable depuis le 2 février 2025 ; rédaction modifiée en vigueur depuis le 27 juillet 2026. |
| SecNumCloud, version 3.2 (ANSSI) | Référentiel d'exigences qui permet de qualifier des offres d'informatique en nuage, notamment au regard de leur protection contre l'application de lois extra-européennes. | En vigueur. |

Aucune analyse de l'assujettissement du cabinet à la directive NIS 2, ni aucune analyse juridique des transferts de données hors de l'Union européenne, de la réglementation de la profession ou du règlement sur l'intelligence artificielle n'est attendue.

### Travail à faire

Mme VARENNAT veut présenter au comité des associés de juin 2027 une politique de sécurité adaptée à un cabinet dont la moitié des collaborateurs travaillent à distance, qui réponde aux incidents du début d'année et que les bureaux appliqueront. Elle attend de vous une analyse des risques, des dispositifs de sécurité et une organisation de la sécurité, la fiabilisation du processus révélé par l'incident FALVERGNE et un avis sur la proposition de l'éditeur. Vous mobiliserez pour cela les annexes 1.1, 1.2, 1.3 et 1.4 ainsi que vos connaissances professionnelles.

**1.1 – Risques et principes de la politique de sécurité (3 points)**

a) Après avoir défini la politique de sécurité du système d'information et précisé en quoi elle doit être fondée sur l'analyse des risques, identifiez, à partir des annexes 1.2 et 1.3, cinq vulnérabilités du cabinet, en particulier celles que le travail à distance crée ou aggrave ; pour chacune, précisez la menace qui peut l'exploiter et le critère de sécurité principalement atteint (confidentialité, intégrité, disponibilité ou traçabilité).

b) Déduisez-en quatre principes de la politique de sécurité du cabinet, en justifiant chacun par les annexes.

**1.2 – Architecture de confiance et appareils personnels (3 points)**

a) Après avoir présenté le modèle Zero Trust, proposez quatre dispositifs d'une architecture de confiance adaptée au travail à distance, portant respectivement sur l'authentification, le chiffrement, le cloisonnement des données du cabinet sur les smartphones et la gestion des identités et des accès des collaborateurs et des renforts temporaires (arrivées, départs, revue des droits) ; reliez chacun à un constat des annexes. Aucun paramétrage technique n'est attendu.

b) Tranchez, en le justifiant par trois arguments tirés des annexes, entre l'interdiction des smartphones personnels et leur usage encadré, et indiquez deux conditions de réussite de la solution retenue.

**1.3 – Gouvernance de la sécurité, souveraineté et sensibilisation (3 points)**

a) Précisez les rôles et responsabilités de cinq acteurs dans la gouvernance de la sécurité du cabinet — la présidente et le comité des associés, le responsable informatique, le prestataire informatique, les éditeurs, les collaborateurs —, puis proposez deux mesures d'organisation qui répondent aux tensions exprimées à l'annexe 1.4.

b) Après avoir défini la souveraineté numérique, appréciez l'hébergement des données de paie hors de l'Union européenne et proposez deux mesures.

c) Proposez un programme de sensibilisation des collaborateurs en trois actions, adapté au travail à distance et aux incidents du début d'année, et un indicateur de son efficacité, précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

**1.4 – Fiabiliser le processus de paiement des fournisseurs (3 points)**

a) Après avoir défini une donnée de référence et expliqué pourquoi sa modification est un point de contrôle clé d'un système d'information comptable, représentez, dans le format de votre choix, le processus actuel de modification des coordonnées bancaires et de paiement des fournisseurs chez Menuiseries FALVERGNE, puis identifiez quatre failles qui ont permis la fraude.

b) Proposez un processus rationalisé et fiabilisé comportant cinq contrôles — contrôle de la modification des données de référence, séparation des tâches, contre-appel, piste d'audit, rapprochement —, en précisant pour chacun qui l'exerce, au cabinet ou chez le client. Aucune écriture comptable n'est attendue.

**1.5 – L'intelligence artificielle au service de la détection des fraudes (2 points)**

a) Distinguez l'apprentissage automatique et l'IA générative, en rattachant chacune des deux fonctions du module de l'annexe 1.4 B à l'une de ces familles.

b) Évaluez ce module en présentant deux apports et trois limites tirés des annexes, puis recommandez, en la justifiant, la suite à donner à la proposition et deux conditions de sa mise en œuvre.
