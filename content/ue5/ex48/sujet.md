# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 48

**DOSSIER 3 – SÉCURISER LA CAMPAGNE DE RENTRÉE, AUDITER LE TRAITEMENT DES CANDIDATURES ET PILOTER L'ÉNERGIE DES RÉSIDENCES (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 16, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. ORVANELLE Résidences est une société anonyme à directoire et conseil de surveillance, créée en 2004, dont le siège est à Montpellier. Elle exploite 60 résidences pour étudiants, soit 9 000 logements meublés, dans quinze villes universitaires, sans en être propriétaire : elle loue les logements aux étudiants et leur propose des services (laveries, salles communes, parkings, ménage), et accueille l'été des séjours courts de stagiaires et de groupes. La famille fondatrice QUILLOREAU détient 60 % de son capital, la foncière KERDALAN Patrimoine 40 %. En 2026, ORVANELLE a signé 7 000 baux, dont 70 % entre juin et septembre, pour un taux d'occupation moyen de 93 % ; un quart des résidents viennent de l'étranger. Elle a réalisé un chiffre d'affaires de 76 M€ et emploie 380 salariés. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « ORVANELLE 2030 », adopté en janvier 2027 par le directoire après avis du conseil de surveillance, fixe cinq objectifs : porter le parc à 12 000 logements dans vingt villes en 2030 ; offrir un parcours entièrement en ligne, de la candidature à la remise des accès au logement ; maintenir un taux d'occupation d'au moins 95 % ; réduire de 20 % la consommation d'énergie des résidences entre 2025 et 2030 ; garantir la sécurité des résidents et de leurs données. Le logiciel de gestion locative, installé en 2009, ne suit plus : son remplacement doit être achevé avant la rentrée universitaire de 2028.

Vous êtes membre du directoire, chargé(e) des opérations (résidences, relation avec les résidents, direction des systèmes d'information), depuis 2025. La présidente du directoire, Mme Ombeline TRÉVARDIN, vous demande trois travaux : préparer la stratégie du système d'information et le projet de remplacement du logiciel de gestion locative (dossier 1) ; organiser et exploiter les données des séjours, et éclairer deux projets qui les concernent (dossier 2) ; sécuriser la campagne de rentrée, auditer le traitement des candidatures et piloter l'énergie des résidences (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation d'ORVANELLE Résidences et chiffres clés

ORVANELLE Résidences est une société anonyme à directoire et conseil de surveillance créée en 2004, dont le siège est à Montpellier. Gestionnaire privé de résidences pour étudiants, elle exploite des résidences qui appartiennent à d'autres : elle loue les logements meublés aux étudiants, leur vend des services et accueille l'été des séjours courts. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Le modèle et les actionnaires**

| Donnée | Valeur |
|---|---|
| Résidences | 60 résidences exploitées sans en être propriétaire : 25 appartiennent à la foncière KERDALAN Patrimoine, 35 à d'autres propriétaires |
| Résidents | étudiants, qui signent un bail pour un logement meublé ; un quart des résidents viennent de l'étranger ; durée moyenne d'un séjour : onze mois |
| Services | laveries, salles communes, parkings, ménage ; l'été, séjours courts de stagiaires et de groupes |
| Actionnaires | famille fondatrice QUILLOREAU : 60 % ; foncière KERDALAN Patrimoine : 40 % |
| Conseil de surveillance | présidé par M. Gaspard QUILLOREAU ; KERDALAN Patrimoine y a deux sièges ; il donne son avis sur la stratégie et sur les investissements importants |
| Directoire | trois membres : la présidente, Mme Ombeline TRÉVARDIN ; le (la) membre chargé(e) des opérations (vous) ; le membre chargé des finances et du développement, M. Bastien LORMIÈRE |

**Le parc et l'activité en 2026**

| Donnée | Valeur |
|---|---|
| Parc | 60 résidences, 9 000 logements meublés (studios 80 % ; logements de deux pièces et colocations 20 %), dans quinze villes universitaires |
| Baux signés | 7 000, dont 70 % entre juin et septembre |
| Taux d'occupation moyen | 93 % |
| Redevance mensuelle moyenne, charges comprises | 680 € |
| Chiffre d'affaires | 76 M€ : redevances et charges 68 M€ ; services et séjours courts d'été 8 M€ |
| Dépenses du système d'information | environ 4,5 M€, dont 1,5 M€ de services en ligne et de prestations |

**L'effectif au 31/12/2026**

| Direction ou service | Salariés |
|---|---|
| Direction des résidences : responsables de résidence, chargés d'accueil, agents techniques et de ménage | 230 |
| Direction commerciale et de la relation résidents, dont le centre de relation résidents, ouvert sept jours sur sept de juin à octobre | 60 |
| Développement : recherche de nouvelles résidences, relations avec les propriétaires | 20 |
| Direction des systèmes d'information | 16 |
| Fonctions support : finances, ressources humaines, achats, juridique, services techniques et énergie | 54 |
| **Total** | **380** |

**Le système d'information en quelques lignes**

- **Logiciel de gestion locative** installé en 2009 dans le centre de données d'un hébergeur régional, à client lourd : candidatures, logements, baux, quittancement, dépôts de garantie, états des lieux saisis après coup.
- **Portail de réservation** en ligne développé en 2018 par une agence web, relié au logiciel de gestion locative par des échanges de fichiers chaque nuit.
- Signature électronique des baux par un prestataire en ligne ; paiement en ligne des redevances et des dépôts de garantie par un prestataire de paiement.
- **Application des résidents** : clé virtuelle sur téléphone dans les 22 résidences équipées de serrures connectées, demandes d'intervention, réservation des laveries ; badges dans les 38 autres résidences.
- Logiciel en ligne de suivi des demandes d'intervention ; progiciel de gestion intégré (finances, achats) ; bureautique en ligne.

**Organigramme simplifié (mars 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil de surveillance | président : M. Gaspard QUILLOREAU |
| — | directoire | présidente : Mme Ombeline TRÉVARDIN |
| Membre du directoire chargé(e) des opérations (vous) | direction des résidences | Mme Clémence ROUSTAGNE |
| | direction commerciale et de la relation résidents | M. Adrien CALVÉRAC |
| | direction des systèmes d'information | Mme Solène VARQUIGNY |
| Membre du directoire chargé des finances et du développement (M. Bastien LORMIÈRE) | développement | — |
| | fonctions support (finances, ressources humaines, achats, juridique, services techniques et énergie) | — |

### ANNEXE 3.1 – La rentrée 2026 (relevé établi par M. Adrien CALVÉRAC, directeur commercial et de la relation résidents, et Mme Solène VARQUIGNY, directrice des systèmes d'information, janvier 2027)

**A. Les événements de la rentrée 2026**

Il n'existe pas de registre des incidents : ce relevé a été reconstitué à partir des réclamations, des notes du centre de relation résidents et des messages échangés avec les prestataires. Chiffres ronds.

| Période | Ce qui s'est passé | Conséquences |
|---|---|---|
| Lundi 1er juin 2026, ouverture des réservations de la rentrée | 8 000 candidats se connectent au portail de réservation dans la première heure. Le portail, prévu pour 1 500 connexions simultanées, reste inaccessible ou très lent de 10 h à 15 h. | 3 000 appels au centre de relation résidents dans la journée, dont 1 200 seulement ont pu être pris ; une centaine de candidats écrivent qu'ils ont réservé ailleurs ; nombreux messages négatifs sur les réseaux sociaux |
| Juin à août 2026 | Le portail affiche un logement comme libre jusqu'à l'échange de fichiers de la nuit suivante avec le logiciel de gestion locative : des logements déjà attribués sont proposés à d'autres candidats. | 150 logements promis à deux candidats ; les seconds candidats ont été relogés dans une autre résidence, parfois dans une autre ville, ou ont renoncé ; 40 réclamations écrites |
| Juillet et août 2026 | Des familles de candidats reçoivent des courriels qui imitent ceux du centre de relation résidents (logo, signature d'une chargée d'accueil, adresse d'expédition presque identique) : le dépôt de garantie serait à verser par virement sur de « nouvelles coordonnées bancaires ». Ces courriels citent le nom du candidat et la résidence choisie ; on ignore comment les fraudeurs les ont obtenus. Le véritable lien de paiement du dépôt de garantie est, lui aussi, envoyé par courriel par le centre de relation résidents. | 50 familles ont versé chacune environ 700 €, soit environ 35 k€, qui n'ont pas été récupérés ; 400 appels et courriels de familles inquiètes ; écho dans la presse régionale : « Logement étudiant : de faux courriels pour détourner les dépôts de garantie » |
| Samedi 5 septembre 2026 | Le service en ligne de la clé virtuelle, exploité par son prestataire, est en panne de 10 h à 16 h. Les clés déjà activées continuent de fonctionner, mais aucune nouvelle clé ne peut être activée. Le prestataire n'assure aucune assistance le week-end ; les chargés d'accueil n'ont aucune clé de secours. | dans les trois résidences équipées qui accueillaient ce jour-là le plus d'arrivées, 120 nouveaux résidents attendent jusqu'à six heures dans le hall avec leurs bagages ; 30 nuits d'hôtel prises en charge par ORVANELLE, environ 3 k€ ; les 19 autres résidences équipées ont eu peu d'arrivées ce jour-là |
| Septembre et octobre 2026 | 200 comptes de résidents de l'application des résidents sont ouverts par des tiers, avec des identifiants (adresse électronique et mot de passe) dérobés sur d'autres sites où ces résidents utilisaient le même mot de passe. L'application ne demande que l'adresse électronique et le mot de passe. | réservations de laveries détournées, coordonnées de résidents consultées ; 15 de ces comptes portaient une clé virtuelle active, qui ouvre la porte d'un logement : aucune intrusion n'a été signalée, mais les journaux des serrures ne sont conservés que sept jours |
| Toute l'année | Les pièces justificatives des candidats et de leurs garants arrivent par courriel. Elles restent sans limite de durée dans les boîtes de messagerie du centre de relation résidents et des chargés d'accueil, y compris celles des candidats non retenus. Les comptes de messagerie des 40 saisonniers de l'été 2026 sont restés ouverts après leur départ. | environ 1,5 million de pièces jointes recensées en janvier 2027 dans les boîtes de la messagerie en ligne, utilisée depuis 2016 |

**B. Deux points de vue**

**M. Adrien CALVÉRAC** : « La fraude aux dépôts de garantie, c'est l'affaire des familles et de leurs banques : nous n'y pouvons rien. Ma priorité, c'est que le portail tienne le jour de l'ouverture des réservations. »

**Mme Clémence ROUSTAGNE, directrice des résidences** : « Mon pire scénario, c'est un résident devant une porte qui ne s'ouvre pas, un samedi soir de septembre, quand l'accueil est fermé. Ou une porte qui s'ouvre pour quelqu'un qui n'est pas le résident. »

**C. Les échelles retenues par le directoire pour l'évaluation des risques**

| Niveau | Probabilité | Impact |
|---|---|---|
| 1 | rare : jamais survenu, peu plausible | faible : gêne passagère de quelques personnes, sans perte |
| 2 | possible : jamais survenu chez ORVANELLE, mais plausible | moyen : moins de 200 résidents ou candidats touchés, pertes inférieures à 10 k€, sans écho public |
| 3 | probable : survenu en 2026, et sa cause est toujours là | fort : 200 personnes ou plus touchées, ou pertes de 10 k€ ou plus, ou écho dans la presse |
| 4 | très probable : survenu des dizaines de fois en 2026, ou facile à provoquer, et sa cause est toujours là | très fort : sécurité des résidents en cause, ou données personnelles de milliers de personnes exposées, ou campagne de rentrée compromise |

La criticité d'un risque est le produit de sa probabilité par son impact (de 1 à 16). Le directoire veut traiter avant la rentrée 2027 les risques dont la criticité atteint au moins 12.

### ANNEXE 3.2 – Le calendrier et les processus de la rentrée (tableau établi avec les directions et note de Mme Solène VARQUIGNY, février 2027)

**A. Les six processus de la rentrée en 2026**

| Processus | Applications et prestataires utilisés | De juin à septembre | D'octobre à mai | Ce que provoque une interruption, selon les directions |
|---|---|---|---|---|
| 1. Réservation (choix du logement et candidature en ligne) | portail de réservation, hébergé par l'agence web qui l'a développé | 24 000 candidatures commencées ; 8 000 candidats connectés dans la première heure de l'ouverture, le 1er juin | 6 000 candidatures commencées | « En été, un candidat qui ne peut pas réserver se tourne vers une autre offre dans la journée ; le reste de l'année, il réessaie le lendemain. » (direction commerciale et de la relation résidents) |
| 2. Contrôle des pièces justificatives | messagerie du centre de relation résidents ; logiciel de gestion locative | jusqu'à 2 000 courriels par jour en juillet | moins de 100 courriels par jour | « Deux ou trois jours de retard se rattrapent, au prix d'heures supplémentaires. » (centre de relation résidents) |
| 3. Signature du bail | logiciel de gestion locative et traitement de texte pour préparer le bail ; prestataire de signature électronique en ligne | 4 900 baux, en moyenne 40 par jour et jusqu'à 80 par jour fin août | 2 100 baux, une dizaine par jour | « Un logement attribué est réservé 48 heures au candidat ; sans bail signé dans ce délai, il est proposé à un autre candidat. » (direction commerciale et de la relation résidents) |
| 4. Encaissement du dépôt de garantie | prestataire de paiement en ligne ; rapprochement hebdomadaire dans le logiciel de gestion locative | 4 900 dépôts de garantie | 2 100 dépôts de garantie | « Les accès ne sont remis qu'une fois le bail signé et le dépôt de garantie payé. » (direction financière) |
| 5. Remise des accès | application des résidents (clé virtuelle) dans les 22 résidences équipées de serrures connectées ; badges programmés à l'accueil, sur un poste local, dans les 38 autres | 4 900 arrivées, dont environ 2 000 sur les quatre samedis du 22 août au 12 septembre, jusqu'à 40 par résidence le même jour | 2 100 arrivées, étalées et surtout en semaine | « Un résident qui ne peut pas entrer dans son logement le jour de son arrivée est hébergé aux frais d'ORVANELLE. Le samedi, nos chargés d'accueil quittent la résidence à 19 h. » (direction des résidences) |
| 6. État des lieux d'entrée | papier, puis saisie dans le logiciel de gestion locative | 4 900 | 2 100 | « Il se fait sur papier et peut être saisi plus tard ; c'est déjà le cas. » (direction des résidences) |

**B. Le dispositif actuel (note de Mme Solène VARQUIGNY)**

- ORVANELLE n'a ni plan de continuité d'activité, ni procédure de fonctionnement dégradé.
- Le logiciel de gestion locative est sauvegardé chaque nuit, à 2 h, dans le centre de données de l'hébergeur régional qui l'héberge. Aucune sauvegarde n'a jamais été restaurée pour essai. En cas de panne, l'hébergeur s'engage à intervenir « dans le jour ouvré suivant ».
- Le portail de réservation est prévu pour 1 500 connexions simultanées ; il n'a jamais été adapté aux pointes de l'ouverture des réservations.
- La clé virtuelle est un service en ligne de son prestataire, choisi en 2023 par les services techniques. Le contrat ne comporte aucun engagement de délai de rétablissement ; l'assistance est joignable du lundi au vendredi, de 9 h à 18 h. Une clé ne peut être activée qu'à l'arrivée du résident, par le chargé d'accueil, une fois l'état des lieux fait. Chaque serrure connectée peut aussi s'ouvrir avec une clé mécanique de secours ; ces clés sont rangées dans le local des services techniques de chaque ville, fermé le week-end.
- Le prestataire de la clé virtuelle propose deux options : l'activation des clés la veille de l'arrivée, chaque clé ne fonctionnant qu'à partir du jour d'arrivée prévu ; une assistance sept jours sur sept de juin à octobre, avec un rétablissement du service en deux heures au plus, pour environ 20 k€ par an.
- Le prestataire de signature électronique et le prestataire de paiement annoncent chacun une disponibilité de 99,9 % ; ils conservent, l'un les baux signés, l'autre l'historique des paiements.

### ANNEXE 3.3 – Le traitement des dossiers de candidature (note de Mme Hortense PELVENNE, déléguée à la protection des données, et demande du directoire, février 2027)

**A. Le traitement**

- En 2026, environ 12 000 dossiers de candidature complets ont été examinés, pour 7 000 baux signés. Chaque dossier comprend les pièces du candidat et celles de son garant, soit une douzaine de documents en moyenne. Les pièces arrivent par courriel au centre de relation résidents, qui les contrôle puis les enregistre dans le logiciel de gestion locative.
- La liste des pièces demandées a été fixée en 2019 par la direction commerciale et de la relation résidents, sans avis de la déléguée à la protection des données :

| Pièces du candidat | Pièces du garant |
|---|---|
| pièce d'identité ; justificatif d'inscription dans un établissement d'enseignement ; photo d'identité ; relevé d'identité bancaire | pièce d'identité ; justificatif de domicile ; trois derniers bulletins de salaire ; dernier avis d'imposition ; relevés de compte bancaire des trois derniers mois ; copie du livret de famille |

- Selon la déléguée, trois de ces pièces ne servent à aucune étape de la décision ni de la gestion du séjour : la photo d'identité du candidat, les relevés de compte bancaire du garant et la copie de son livret de famille. M. Adrien CALVÉRAC : « Plus on en demande, moins on se trompe sur les garants. »

**B. Les constats de la déléguée**

- Le registre des activités de traitement, qu'elle tient, n'a pas été mis à jour depuis 2022. Il ne mentionne ni l'application des résidents et la clé virtuelle (2024), ni la vérification des garants par un prestataire (2025), ni la conservation des pièces dans les boîtes de messagerie.
- Depuis 2025, les pièces des garants sont transmises par courriel à un prestataire de vérification des garants, qui contrôle l'authenticité des bulletins de salaire et des avis d'imposition : 3 000 dossiers lui ont été transmis en 2026. Il n'existe qu'un bon de commande : aucun contrat écrit ne précise ce que le prestataire peut faire des données, comment il les protège, où et combien de temps il les conserve.
- Le profil « chargé d'accueil » du logiciel de gestion locative, attribué à 120 personnes, dont les saisonniers, donne accès aux dossiers des 60 résidences. Les comptes des 40 saisonniers de l'été 2026 n'ont pas été fermés à la fin de leur contrat. Aucune revue des comptes n'a eu lieu depuis 2021.
- Aucune durée de conservation n'est appliquée : le logiciel de gestion locative conserve environ 150 000 dossiers de candidature depuis 2009, dont environ 60 000 de candidats qui ne sont jamais devenus résidents ; les boîtes de messagerie contiennent environ 1,5 million de pièces jointes.
- La déléguée, seule pour toute l'entreprise et rattachée à la direction juridique, n'a été consultée sur aucun projet depuis 2023.

**C. La demande du directoire**

« Le paramétrage du nouveau logiciel de gestion locative commencera en septembre 2027 : les règles du traitement des candidatures (pièces demandées, accès, durées de conservation) doivent être arrêtées avant. ORVANELLE n'a pas d'audit interne : nous confierons un audit de conformité du traitement des dossiers de candidature à un auditeur des systèmes d'information externe. La mission durera six semaines, du lundi 12 avril au vendredi 21 mai 2027, pour que le directoire puisse décider avant l'ouverture des réservations de la rentrée 2027, le 1er juin. Préparez-en le cadrage. »

### ANNEXE 3.4 – L'énergie des résidences (note de M. Thibaut COSTAMIGNE, responsable technique et énergie, février 2027)

**A. Les consommations**

ORVANELLE paie l'énergie des résidences (chauffage, eau chaude, électricité des logements et des parties communes) ; les charges sont comprises dans la redevance, et les résidents ne connaissent pas leur consommation.

| Donnée | 2025 (référence du plan) | 2026 |
|---|---|---|
| Consommation d'énergie des résidences | 45 000 MWh | 44 100 MWh |
| Logements gérés | 9 000 | 9 000 |
| Consommation par logement | 5 000 kWh | 4 900 kWh |
| Répartition | chauffage 60 % ; eau chaude 20 % ; autres usages (éclairage, prises, laveries, parties communes) 20 % | identique |
| Facture d'énergie | environ 7 M€ | environ 7 M€ |

- L'hiver 2026 a été plus doux que celui de 2025 : selon le fournisseur d'énergie, la baisse de 2026 s'explique surtout par la météo.
- Le plan « ORVANELLE 2030 » ne précise pas si la baisse de 20 % porte sur la consommation totale des résidences ou sur la consommation par logement, alors que le parc doit passer de 9 000 à 12 000 logements.
- Quatre résidences de studios, construites entre 2005 et 2012 dans la même ville, avec des équipements comparables, consommaient en 2026 :

| Résidence | Logements | Consommation par logement en 2026 |
|---|---|---|
| A | 150 | 3 000 kWh |
| B | 120 | 4 500 kWh |
| C | 180 | 6 000 kWh |
| D | 140 | 9 000 kWh |

- Dans la plupart des résidences, le chauffage est réglé à la main par l'agent technique, deux fois par an. Les radiateurs chauffent les logements vides, dont les quelque 630 logements vacants, et ceux dont la fenêtre est ouverte ; dans la résidence D, des résidents ouvrent leur fenêtre en plein hiver pour faire baisser la température.
- Les travaux sur les bâtiments (isolation, chaudières) ne sont pas décidés par ORVANELLE seule.

**B. Le projet de pilotage de l'énergie (proposition d'un prestataire spécialisé, janvier 2027)**

- Un boîtier dans chacun des 9 000 logements, avec trois capteurs : température, présence, ouverture de la fenêtre.
- Des robinets de radiateur commandés à distance, qui baissent le chauffage quand le logement est vide ou que la fenêtre est ouverte.
- Une plateforme de données énergétiques, fournie en service en ligne par le prestataire, qui reçoit les mesures, commande le chauffage et compare chaque jour la consommation de chaque logement à celle des logements semblables.
- L'affichage, dans l'application des résidents, de la consommation de leur logement, comparée à celle des logements semblables, et d'une alerte « fenêtre ouverte, chauffage baissé ».
- Gain annoncé par le prestataire : de 15 à 25 % de la consommation de chauffage, constaté dans des résidences comparables.
- Déploiement envisagé en 2027 et en 2028.

**C. Les choix proposés par le prestataire, à arrêter avant la commande**

- Chaque capteur transmet sa mesure toutes les minutes : la plateforme recevrait environ 40 millions de mesures par jour ; à une mesure par quart d'heure, elle en recevrait environ 2,6 millions.
- Toutes les mesures sont conservées, au détail, pendant dix ans, « pour affiner les modèles ».
- Les boîtiers ont une pile non remplaçable et sont renouvelés entiers tous les cinq ans ; le prestataire propose aussi, un peu plus cher, un boîtier à pile remplaçable, garanti dix ans.
- La plateforme est hébergée dans deux centres de données du prestataire, qui ne communique ni leur consommation d'électricité ni l'origine de cette électricité ; toutes les mesures sont copiées dans les deux.

Ces données ne permettent pas de calculer une empreinte environnementale, et aucun calcul n'est demandé.

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| ISO/IEC 27005:2022 | Lignes directrices de gestion des risques liés à la sécurité de l'information : identification, analyse, évaluation et traitement des risques. | En vigueur |
| ISO 22301:2019 | Norme d'exigences du système de management de la continuité d'activité : analyse d'impact sur l'activité, stratégie et plans de continuité, exercices. | En vigueur |
| ISO/IEC 27001:2022 | Norme d'exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques ; 93 mesures en annexe A, dont le contrôle d'accès, la sauvegarde et la sécurité des relations avec les fournisseurs. | En vigueur |
| Règlement (UE) 2016/679 sur la protection des données (RGPD) | En principe : les données collectées sont limitées à ce qui est nécessaire au regard des finalités (minimisation) et ne sont pas conservées plus longtemps que nécessaire ; leur sécurité est assurée par des mesures appropriées ; le responsable du traitement et le sous-traitant tiennent chacun un registre des activités de traitement ; un prestataire qui traite des données pour le compte d'ORVANELLE agit en sous-traitant, dans le cadre d'un contrat écrit (instructions, sécurité, sort des données en fin de contrat, audit). ORVANELLE est responsable du traitement des dossiers de candidature. | Applicable depuis le 25/05/2018 |
| Règlement (UE) 2024/2847 sur la cyberrésilience (CRA) | Exigences de cybersécurité pour les produits comportant des éléments numériques, à la charge de leurs fabricants : sécurité dès la conception, gestion des vulnérabilités, fourniture de mises à jour de sécurité. Les serrures connectées et les boîtiers de capteurs comportent des éléments numériques ; l'application du règlement à chaque produit n'est pas à déterminer. | Signalement par les fabricants des vulnérabilités activement exploitées et des incidents graves depuis le 11/09/2026 ; application générale le 11/12/2027 |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | Critères d'écoconception des services numériques publiés par l'Arcep et l'Arcom, avec l'ADEME, regroupés par thèmes (stratégie, spécifications, architecture, contenus, hébergement, algorithmie…). | Version 2 publiée en 2024 |

ORVANELLE ne publie pas d'état de durabilité ; aucun cadre de durabilité n'est à déterminer. Il n'est demandé aucune analyse juridique.

### Travail à faire

À la rentrée 2026, de faux courriels ont détourné des dépôts de garantie, le portail a cédé le jour de l'ouverture des réservations, une panne de la clé virtuelle a laissé des résidents dans le hall et des comptes de l'application ont été pris en main ; ORVANELLE n'a pas de plan de continuité. Le directoire veut aussi un audit du traitement des dossiers de candidature avant le paramétrage du nouveau logiciel de gestion locative, et un projet de capteurs doit servir l'objectif de baisse de 20 % de la consommation d'énergie des résidences. Mme TRÉVARDIN vous demande d'analyser les risques de la rentrée et leur impact, d'organiser la continuité de la rentrée 2027, de cadrer l'audit et d'éclairer le projet de pilotage de l'énergie. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – Les risques de la rentrée et l'analyse d'impact (4 points)**

a) Après avoir présenté une typologie des risques liés aux systèmes d'information, identifiez cinq risques révélés par l'annexe 3.1, formulés comme des événements redoutés, et classez-les selon cette typologie.

b) Après avoir défini l'analyse d'impact sur l'activité, appréciez, à partir de l'annexe 3.2, l'impact d'une interruption de trois processus de la rentrée, dont la remise des accès, selon la période de l'année. Déduisez-en les processus critiques et la durée maximale d'interruption admissible de chacun.

c) Évaluez la probabilité et l'impact de vos cinq risques selon les échelles de l'annexe 3.1 C et retenez-en deux prioritaires. Proposez pour chacun une option de traitement (réduire, transférer, accepter, éviter) et une mesure, en répondant à M. CALVÉRAC.

**3.2 – La continuité et la sécurité de la rentrée 2027 (3 points)**

a) Après avoir distingué le plan de continuité d'activité et le plan de reprise d'activité, proposez le dispositif de continuité de la remise des accès aux logements et de la signature des baux pendant la rentrée : le fonctionnement en mode dégradé, les objectifs de durée maximale d'interruption et de perte de données maximale admissibles, l'engagement à obtenir du prestataire de la clé virtuelle et les exercices. Aucun paramétrage ni aucun test technique de sécurité ne sont attendus.

b) Hiérarchisez trois mesures de sécurité à engager avant la rentrée 2027, chacune reliée à un risque différent de la question 3.1, dont une contre la fraude au dépôt de garantie, en justifiant le rang de la première.

**3.3 – L'audit du traitement des dossiers de candidature (3 points)**

a) Après avoir défini l'audit de conformité d'un processus du système d'information, cadrez l'audit du traitement des dossiers de candidature que conduira l'auditeur externe : ses objectifs, son périmètre, ses étapes, ses livrables, son calendrier sur les six semaines de la mission et les preuves à demander.

b) Proposez quatre critères de conformité et de sécurité de cet audit, choisis parmi les thèmes suivants : minimisation des pièces demandées, registre des activités de traitement, encadrement du sous-traitant, accès aux dossiers, durée de conservation. Pour chacun, précisez ce qui est attendu et appréciez la situation actuelle à partir de l'annexe 3.3. Aucune analyse juridique n'est attendue.

**3.4 – Le pilotage de l'énergie des résidences (3 points)**

a) Après avoir distingué le Green IT et l'IT for green, montrez comment le projet de l'annexe 3.4 peut servir l'objectif de réduire de 20 % la consommation d'énergie des résidences entre 2025 et 2030, et à quelles conditions.

b) Proposez deux indicateurs de suivi, dont l'un rapporté à la référence de 2025 et à une cible de 2030, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

c) Appréciez l'empreinte environnementale du dispositif lui-même, puis proposez trois mesures de sobriété portant sur les choix de l'annexe 3.4 C (fréquence de transmission des mesures, durée de conservation, durée de vie des boîtiers, hébergement). Aucun calcul d'empreinte n'est attendu.
