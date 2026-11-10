# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 8

**DOSSIER 2 – FIABILISER LE SYSTÈME D'INFORMATION FINANCIER ET ÉVALUER L'APPORT DES NOUVELLES TECHNOLOGIES (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 3, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mai 2027. Le groupe ALTIVERNE est un groupe familial non coté, constitué autour d'une société par actions simplifiée créée en 1962 à Lyon. Il conçoit, installe, modernise et entretient des ascenseurs, des monte-charges et des portes automatiques pour des bailleurs sociaux, des syndics de copropriété, des établissements de santé et des centres commerciaux. Il emploie 2 400 salariés, dont 1 500 techniciens de maintenance répartis dans 34 agences en France, une usine de fabrication des cabines et des armoires de commande à Roanne et deux filiales, en Belgique et en Suisse. Son chiffre d'affaires consolidé de l'exercice 2026 s'élève à 590 millions d'euros, dont 55 % pour la maintenance, 25 % pour la modernisation et 20 % pour les installations neuves ; 14 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le groupe entretient 52 000 appareils, dont 31 000 sont reliés à son centre de télésurveillance : chacun remonte en continu ses alarmes, ses pannes et ses données de fonctionnement. La présidente, Mme Claire ALTIVERNE, petite-fille du fondateur, et le directeur général, M. Hugo DESMAREST, ont adopté en janvier 2027 le plan « ALTIVERNE 2030 » : passer d'une maintenance qui répare à une maintenance qui anticipe, proposer de nouveaux services fondés sur les données des appareils, fiabiliser les processus financiers et faire de la durabilité un argument commercial. Le groupe a décidé de publier volontairement, dès l'exercice 2026, un état de durabilité conforme aux ESRS. Il doit aussi transmettre le savoir-faire de ses techniciens expérimentés, dont 300 partiront à la retraite d'ici 2030.

Vous venez de rejoindre le groupe comme responsable de la transformation numérique, rattaché(e) au directeur général. M. DESMAREST vous confie trois chantiers : organiser et valoriser les données des appareils connectés (dossier 1) ; fiabiliser le système d'information financier et évaluer l'apport des nouvelles technologies (dossier 2) ; inscrire le système d'information dans la démarche de durabilité du groupe et capitaliser les savoir-faire des techniciens (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation du groupe ALTIVERNE et chiffres clés

Le groupe ALTIVERNE est un groupe familial non coté. Sa société mère, une société par actions simplifiée créée en 1962 à Lyon, où se trouve le siège, détient l'usine de Roanne, qui fabrique les cabines et les armoires de commande, ainsi que les 34 agences françaises ; deux filiales exercent le même métier en Belgique et en Suisse. Ses clients sont des bailleurs sociaux, des syndics de copropriété, des établissements de santé et des centres commerciaux. Son exercice coïncide avec l'année civile.

**Chiffres clés de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Activité | conception, installation, modernisation et maintenance d'ascenseurs, de monte-charges et de portes automatiques |
| Chiffre d'affaires consolidé | 590 M€ : maintenance 55 %, modernisation 25 %, installations neuves 20 % |
| Salariés | 2 400, dont 1 500 techniciens de maintenance |
| Implantations | siège à Lyon ; usine à Roanne ; 34 agences en France ; filiales en Belgique et en Suisse |
| Parc entretenu | 52 000 appareils, dont 31 000 reliés au centre de télésurveillance du groupe (alarmes, pannes et données de fonctionnement remontées en continu) |
| Budget du système d'information | 14 M€ (environ 2,4 % du chiffre d'affaires) |
| Plan « ALTIVERNE 2030 » (adopté en janvier 2027) | maintenance qui anticipe ; nouveaux services fondés sur les données des appareils ; processus financiers fiabilisés ; durabilité comme argument commercial |
| Durabilité | le groupe publie volontairement, dès l'exercice 2026, un état de durabilité conforme aux ESRS |
| Savoir-faire | 300 techniciens expérimentés partiront à la retraite d'ici 2030 |

**Organigramme simplifié de la direction (mai 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Présidence | présidente, petite-fille du fondateur | Mme Claire ALTIVERNE |
| Direction générale | directeur général, qui porte le plan « ALTIVERNE 2030 » | M. Hugo DESMAREST |
| Rattaché(e) au directeur général | responsable de la transformation numérique (poste créé en 2027) | vous |
| Rattachée au directeur général | responsable RSE | Mme Amélie TESSANDIER |
| Comité de direction | directeur de la maintenance et des services (34 agences, dirigées chacune par un responsable d'agence ; centre de télésurveillance de Lyon) | M. Julien PRADELLE |
| Comité de direction | directrice des installations neuves et de la modernisation | Mme Agathe RIBOULET |
| Comité de direction | directeur industriel (usine de Roanne, achats de composants, pièces détachées) | M. Patrick VIALLARD |
| Comité de direction | directeur commercial et des grands comptes | M. Nicolas BERTHOLON |
| Comité de direction | directeur administratif et financier | M. Thibault MARSANGE |
| Comité de direction | directrice des systèmes d'information | Mme Isabelle CHAMBRUN |
| Comité de direction | directrice des ressources humaines | Mme Céline MAUFRAS |
| Filiales | directeurs des filiales belge et suisse, rattachés au directeur général | — |

### ANNEXE 2.1 – Le système d'information financier et ses incidents

**A. Note de M. Thibault MARSANGE, directeur administratif et financier, au directeur général (avril 2027)**

Objet : état du système d'information financier et incidents de l'exercice 2026.

1. **Les outils.** La société mère tient sa comptabilité, ses achats, ses contrats de maintenance et sa facturation dans le progiciel de gestion intégré (PGI) du groupe, en place depuis 2012. Les bons d'intervention des techniciens, saisis dans le logiciel de gestion des interventions, sont exportés chaque soir dans un fichier intégré au PGI le lendemain matin, après un contrôle visuel par le service de facturation ; les interventions hors contrat sont ressaisies dans le PGI par les assistantes d'agence. Les avenants aux contrats (ajout ou retrait d'un appareil, résiliation) sont signés en agence et transmis au siège par courriel une fois par mois. Les filiales belge et suisse utilisent chacune un logiciel comptable différent ; leurs comptes remontent au siège par tableur chaque mois. Le reporting mensuel du chiffre d'affaires de maintenance par agence est établi sur tableur à partir d'extractions du PGI et du logiciel des interventions ; il s'écarte d'environ 2 % du chiffre d'affaires enregistré en comptabilité, sans que l'écart soit expliqué.

2. **Les volumes (société mère, 2026).** 120 000 factures clients émises : 84 000 factures trimestrielles pour 21 000 contrats de maintenance et 36 000 factures d'interventions hors contrat. 90 000 factures fournisseurs reçues de 6 000 fournisseurs actifs, dont 4 800 PME et micro-entreprises ; elles sont traitées par 18 comptables fournisseurs. Les règlements fournisseurs sont payés par virement, en deux campagnes par mois d'environ 1 200 virements chacune.

3. **Les incidents de 2026.**

| N° | Incident | Constat |
|---|---|---|
| 1 | Tentative de fraude au changement de coordonnées bancaires | En octobre, un courriel imitant un fabricant de moteurs demande la modification de son relevé d'identité bancaire. Une comptable fournisseurs modifie les coordonnées dans le PGI ; elle prépare aussi les campagnes de virements. Le directeur administratif et financier valide la campagne dans son ensemble, sans liste des coordonnées modifiées. Un virement de 350 000 € part vers le compte frauduleux ; la banque en récupère 100 000 €. Aucun contre-appel du fournisseur n'est prévu par les procédures. |
| 2 | Écarts entre le chiffre d'affaires de maintenance facturé et les contrats actifs | Un rapprochement mené en novembre entre les contrats signés en agence et les factures de l'année révèle 600 contrats encore facturés après leur résiliation (0,9 M€ d'avoirs à émettre) et 400 appareils ajoutés par avenant mais jamais facturés (0,6 M€ par an de chiffre d'affaires non facturé). |
| 3 | Doublons de factures fournisseurs | 220 factures payées deux fois (0,4 M€), reçues à la fois par courriel et par courrier ; 1 500 avoirs clients émis pour corriger des erreurs de ressaisie des interventions hors contrat. |
| 4 | Retards de clôture | Clôture mensuelle à J+12, pour une cible de J+5 fixée par le plan « ALTIVERNE 2030 ». Les comptes de l'exercice 2026 ont été arrêtés avec quatre semaines de retard, en raison des rapprochements manuels entre le logiciel des interventions, le PGI et les relevés bancaires. |
| 5 | Remarques des auditeurs externes sur le contrôle interne informatique (lettre de recommandations sur l'exercice 2026) | 14 personnes de la comptabilité disposent de droits d'administration du PGI ; 30 comptes d'anciens salariés sont encore actifs ; aucune revue des habilitations depuis 2022 ; les modifications du paramétrage du PGI (conditions de paiement, taux de TVA) sont faites directement en production par le prestataire de maintenance du PGI, sans trace ni validation ; les fichiers d'interface peuvent être modifiés avant leur intégration et ne comportent ni nombre de lignes ni total de contrôle. |

**B. Le passage à la facturation électronique**

La société mère, entreprise de taille intermédiaire, a souscrit en juillet 2026, dans l'urgence, l'abonnement d'une plateforme agréée par l'administration fiscale :
- **émission** : depuis le 1er septembre 2026, les factures émises par le PGI sont transmises à la plateforme au format Factur-X ; en revanche, environ 3 000 factures d'interventions hors contrat sont encore établies chaque année sur papier par les agences, à partir de carnets de factures ;
- **réception** : depuis septembre 2026, 30 % des factures fournisseurs reçues chaque mois, émises par de grandes entreprises et des ETI, arrivent par la plateforme ; les comptables les téléchargent en PDF, puis les ressaisissent dans le PGI, comme les factures reçues par courrier et par courriel ;
- les statuts que la plateforme renvoie sur le traitement des factures (reçue, refusée, approuvée, payée…) ne sont exploités par personne ;
- les factures des filiales belge et suisse relèvent du droit de leur pays, non étudié ici.

Mme Odile FRESSINAUD, responsable de la comptabilité fournisseurs : « Chaque comptable traite environ 5 000 factures par an, et nous en ressaisissons la plupart. À partir de septembre, presque toutes les factures de nos fournisseurs arriveront par la plateforme : si nous continuons à les ressaisir, nous ne tiendrons pas, et nous ne saurons toujours pas rapprocher la facture de la commande et de la réception des pièces. »

**C. Repères réglementaires sur la facturation électronique (au 31/12/2026)**

| Texte | Objet principal | Situation au 31/12/2026 |
|---|---|---|
| Généralisation de la facturation électronique et du e-reporting (article 91 de la loi de finances pour 2024 ; code général des impôts) | Les factures entre entreprises assujetties à la TVA établies en France sont émises, transmises et reçues sous forme électronique par l'intermédiaire d'une plateforme agréée par l'administration ; les formats admis sont Factur-X, UBL et CII. Les données des opérations non concernées (ventes aux particuliers, opérations internationales) et certaines données de paiement sont transmises à l'administration par la plateforme (e-reporting). Le portail public de facturation tient l'annuaire des entreprises et concentre les données transmises à l'administration ; il n'est pas une plateforme d'échange des factures. | Depuis le 01/09/2026 : réception obligatoire pour toutes les entreprises ; émission et e-reporting obligatoires pour les grandes entreprises et les entreprises de taille intermédiaire. À compter du 01/09/2027 : émission et e-reporting obligatoires pour les PME et les micro-entreprises. |

### ANNEXE 2.2 – Proposition de l'ESN LUMIGRÈS (mars 2027)

**A. Objet et prix**

L'entreprise de services du numérique LUMIGRÈS, intégratrice du PGI du groupe depuis 2019, propose un contrat d'intégration au forfait de 900 000 € hors taxes, en trois lots : raccordement du PGI à la plateforme agréée, avec intégration automatique des factures fournisseurs reçues et transmission de toutes les factures émises (400 000 €) ; interface automatisée entre le logiciel des interventions et le PGI, avec suppression des ressaisies des interventions hors contrat (250 000 €) ; déploiement d'un module de détection des anomalies par intelligence artificielle (250 000 €). S'y ajoutent un abonnement annuel au module de 100 000 € et une maintenance corrective de 60 000 € par an.

**B. Le module de détection des anomalies**

Le module repose sur l'apprentissage automatique : il apprend, à partir de l'historique des factures fournisseurs, des fiches fournisseurs et des paiements de 2024 à 2026, ce qu'est une opération habituelle, puis attribue à chaque opération nouvelle un score de risque de 0 à 100 ; au-delà d'un seuil, il émet une alerte. Il vise trois familles d'anomalies : paiements inhabituels (montant, bénéficiaire, date), changements de coordonnées bancaires, doublons de factures. Lors d'une démonstration sur les paiements de 2026 de la société mère, il a émis 6 000 alertes ; elles comprenaient le changement de coordonnées bancaires frauduleux d'octobre et 150 des 220 doublons de l'année ; les 5 849 autres alertes, examinées ensuite par la comptabilité fournisseurs, se sont révélées sans fondement. LUMIGRÈS indique que le module « ne fournit pas de justification détaillée de chaque score » et que l'historique d'apprentissage n'a pas été nettoyé (doublons non corrigés, fournisseurs créés deux fois).

**C. Extrait des clauses proposées (résumé en langage courant)**

| N° | Thème | Clause proposée |
|---|---|---|
| 1 | Périmètre | Les trois lots ci-dessus, pour la société mère. Les filiales, la reprise des données antérieures à 2024 et la formation des utilisateurs ne sont pas comprises ; toute demande nouvelle fera l'objet d'un devis. |
| 2 | Délais | Mise en service du raccordement à la plateforme et de l'interface avant le 1er septembre 2027. LUMIGRÈS fera ses meilleurs efforts pour tenir cette date, qui dépend aussi de la disponibilité des équipes d'ALTIVERNE. |
| 3 | Résultats du module d'IA | Le module signalera les opérations inhabituelles. Aucun taux de détection ni aucun taux maximal de fausses alertes n'est garanti. Les seuils d'alerte sont réglés par LUMIGRÈS. |
| 4 | Recette | La recette est réputée prononcée dix jours ouvrés après chaque livraison, sauf réserve écrite d'ALTIVERNE ; toute mise en production vaut recette. |
| 5 | Pénalités | En cas de retard de livraison, pénalité de 1 500 € par semaine, plafonnée à 9 000 €. |
| 6 | Maintenance corrective | Prise en charge des anomalies bloquantes en quatre heures ouvrées et correction sous deux jours ouvrés ; rapport mensuel des anomalies. |
| 7 | Propriété | Les développements spécifiques (interfaces) et les paramétrages du module, y compris les règles de détection apprises sur les données d'ALTIVERNE, restent la propriété de LUMIGRÈS, qui en concède l'usage pendant la durée du contrat. |
| 8 | Accès aux données | LUMIGRÈS peut réutiliser les données transmises (factures, fiches fournisseurs, paiements), après anonymisation, pour améliorer les modèles proposés à ses autres clients. Le module est hébergé par un sous-traitant de LUMIGRÈS, dont la localisation n'est pas précisée. |
| 9 | Pilotage | Un comité de pilotage mensuel réunit le chef de projet de LUMIGRÈS et la DSI d'ALTIVERNE. |
| 10 | Durée et sortie | Contrat de trois ans, renouvelable par tacite reconduction. L'abonnement au module est révisable chaque année par LUMIGRÈS. En fin de contrat, les données sont restituées dans le format du module ; aucune assistance à la reprise par un autre prestataire n'est prévue. |

**D. Témoignage de Mme Isabelle CHAMBRUN, directrice des systèmes d'information**

« LUMIGRÈS connaît bien notre PGI, et nous n'avons pas le temps de lancer une nouvelle consultation avant septembre. Mais je ne signerai pas un contrat qui nous laisse sans prise sur la date, sur la qualité du module et sur nos propres paramétrages. »

### ANNEXE 2.3 – Trois propositions « nouvelles technologies » et repères (au 31/12/2026)

**A. Les propositions remontées au comité de direction (avril 2027)**

| Proposition | Porteur | Description | Données et coûts annoncés |
|---|---|---|---|
| (a) Rapports de visite certifiés | M. Julien PRADELLE, directeur de la maintenance et des services | Inscrire dans une blockchain publique, par l'intermédiaire d'un prestataire d'ancrage, l'empreinte numérique de chaque rapport de visite d'entretien et de sécurité remis aux clients ; le client pourrait vérifier, à partir d'un code imprimé sur le rapport, que le document n'a pas été modifié depuis sa date d'émission. En 2026, après deux accidents en cabine, deux bailleurs ont contesté l'authenticité des rapports de visite produits par le groupe. | environ 400 000 rapports par an, qui mentionnent l'appareil, la date, les opérations réalisées et le nom du technicien ; 40 000 € par an |
| (b) Paiements en jeton stable | M. Nicolas BERTHOLON, directeur commercial et des grands comptes | Un groupe de centres commerciaux établi hors de l'Union européenne, client du groupe pour 1,2 M€ de chiffre d'affaires par an, propose de régler ses factures en jetons de monnaie électronique se référant à l'euro. Un prestataire de paiement en crypto-actifs, enregistré en 2022 sous l'ancien régime français des prestataires de services sur actifs numériques (ancien PSAN), et dont la demande d'agrément au titre de MiCA est toujours en cours d'instruction, offre de conserver les jetons pour le compte d'ALTIVERNE et de les convertir en euros. | commission de 1 % des montants encaissés |
| (c) Certificat d'appareil et fidélité sous forme de NFT | Mme Agathe RIBOULET, directrice des installations neuves et de la modernisation | Remettre au propriétaire de chaque appareil modernisé un « certificat numérique » sous forme de jeton non fongible (NFT) émis sur une blockchain publique, décrivant les composants installés et les interventions, transférable à un nouveau propriétaire ou à un nouveau syndic ; une agence de communication propose en outre de distribuer aux syndics fidèles des NFT « de collection » émis en série, échangeables entre eux sur une place de marché en ligne. | environ 2 000 appareils modernisés par an ; 60 000 € la première année ; les clients ne disposent aujourd'hui d'aucun portefeuille de crypto-actifs |

**B. Repères réglementaires et normatifs (au 31/12/2026)**

| Texte ou norme | Objet principal | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2023/1114 sur les marchés de crypto-actifs (« MiCA ») | Encadre l'offre au public et l'admission à la négociation de crypto-actifs, l'émission des jetons qui visent une valeur stable (jetons se référant à un ou des actifs ; jetons de monnaie électronique, se référant à une seule monnaie officielle, qui ne peuvent être émis que par un établissement de crédit ou un établissement de monnaie électronique) et l'agrément des prestataires de services sur crypto-actifs (PSCA), parmi lesquels la conservation de crypto-actifs pour le compte de clients et leur échange contre des fonds. Sont exclus de son champ les crypto-actifs uniques et non fongibles avec d'autres crypto-actifs, ainsi que les instruments financiers. Il ne fixe ni traitement comptable ni régime fiscal pour ces actifs. | Applicable depuis le 30/12/2024 ; dispositions relatives aux jetons stables applicables depuis le 30/06/2024. La période transitoire des prestataires enregistrés sous l'ancien régime français (PSAN) a pris fin le 01/07/2026 : depuis le 02/07/2026, seuls les PSCA agréés au titre de MiCA peuvent exercer. |
| Règlement (UE) 2024/1183 (« eIDAS 2 ») | Cadre européen des services de confiance : signature électronique, horodatage électronique, registres électroniques. | En vigueur |
| Règlement (UE) 2016/679 (RGPD) | Protection des données à caractère personnel : minimisation, conservation limitée à la durée nécessaire, effacement des données dans les cas prévus par le règlement. | Applicable depuis le 25/05/2018 |
| ISO 22739:2024 | Norme de vocabulaire des chaînes de blocs et des technologies de registres distribués (bloc, nœud, consensus, jeton, contrat intelligent…) ; ce n'est pas une norme d'exigences. | En vigueur (2e édition) |
| Normes d'exercice professionnel (NEP) des auditeurs légaux | Aucune norme n'est propre à la blockchain : lorsqu'une entité utilise un registre distribué dans ses processus, ses auditeurs prennent connaissance de ce système d'information comme de tout autre. | En vigueur |

### Travail à faire

M. DESMAREST vous demande de fiabiliser les processus financiers du groupe avant l'échéance du 1er septembre 2027, de sécuriser le contrat proposé par l'ESN et de lui donner un avis sur les trois propositions « nouvelles technologies » remontées par les directions. Vous mobiliserez pour cela les annexes 1.1, 2.1, 2.2 et 2.3 ainsi que vos connaissances professionnelles.

**2.1 – Fiabilité des données comptables et décisionnelles (3 points)**

a) Après avoir défini la fiabilité d'un système d'information comptable et décisionnel, identifiez, à partir de l'annexe 2.1, quatre risques qui pèsent sur la fiabilité des données comptables et décisionnelles du groupe ALTIVERNE.

b) Proposez quatre mesures de fiabilisation, portant respectivement sur les contrôles applicatifs, la séparation des tâches, la traçabilité, et les interfaces automatisées et les rapprochements, en reliant chacune à l'un des risques identifiés. Assortissez l'une d'elles d'un indicateur (formule, source, fréquence, cible et axe du tableau de bord).

**2.2 – Facturation électronique et architecture du SI financier (3 points)**

a) Analysez les impacts organisationnels, juridiques et comptables du passage à la facturation électronique pour la société mère, en distinguant la comptabilité fournisseurs et la facturation des clients.

b) Schématisez, en format libre, l'architecture cible du système d'information financier de la société mère (PGI, plateforme agréée, logiciel des interventions, banque, module de détection des anomalies, liaison avec les filiales) en la situant dans les zones d'une cartographie urbanisée du SI, puis justifiez deux règles d'urbanisation qu'elle respecte.

**2.3 – Intelligence artificielle et prévention des fraudes (2 points)**

Après avoir présenté le principe de la détection d'anomalies par apprentissage automatique, montrez deux apports et trois limites du module proposé par LUMIGRÈS pour prévenir les fraudes et les anomalies de l'annexe 2.1, puis précisez les conditions de la supervision humaine de ses alertes.

**2.4 – Sécurisation du contrat avec l'ESN (3 points)**

a) Après avoir caractérisé le type de contrat proposé par LUMIGRÈS, relevez trois clauses de l'annexe 2.2 à renégocier ou à ajouter pour sécuriser la relation sur les plans opérationnel et juridique ; pour chacune, justifiez votre demande au regard du cas et proposez une formulation de principe.

b) Proposez une instance de pilotage de la relation et un indicateur de suivi de la prestation (formule, source, fréquence, cible et axe du tableau de bord).

**2.5 – Blockchain et crypto-actifs : trois propositions (3 points)**

a) Après avoir défini la blockchain, rattachez chacune des trois propositions de l'annexe 2.3 à la typologie des applications de la blockchain (traçabilité, certification, finance décentralisée, NFT).

b) Évaluez, pour chacune, les opportunités, les risques et le cadre réglementaire à partir des repères de l'annexe 2.3, puis recommandez, en le justifiant, la suite à lui donner.
