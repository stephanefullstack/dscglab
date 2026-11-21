# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 41

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES DOSSIERS ET DU RÉSEAU DE PRESTATAIRES (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 14, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. VALMÉRIS Assistance est une société anonyme créée en 1994, dont le siège est à Limoges. Entreprise d'assurance agréée pour la branche assistance, elle organise et finance, pour le compte de ses partenaires, l'aide apportée à leurs assurés jour et nuit : dépannage et remorquage des véhicules, véhicule de remplacement, intervention d'urgence au domicile après un dégât des eaux ou une effraction, aide à domicile et garde d'enfants après un accident. Elle est détenue à 70 % par le groupe d'assurance mutualiste TERRANDÈLE et à 30 % par un réseau bancaire coopératif. Ses garanties sont vendues par le groupe TERRANDÈLE et par quatorze partenaires (assureurs, banques, deux constructeurs automobiles et un loueur de véhicules), qui lui transmettent les contrats de leurs clients. En 2026, ses trois plateaux d'assistance de Limoges, Metz et Valence ont reçu 3,2 millions d'appels et ouvert 520 000 dossiers, confiés à un réseau de 3 400 prestataires agréés ; son chiffre d'affaires a atteint 310 M€. Elle emploie 820 salariés. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan stratégique « Assister 2030 », adopté en décembre 2026 par le conseil d'administration, fixe cinq objectifs : déclencher l'assistance sans appel quand un véhicule connecté signale une panne ou un accident ; informer chaque bénéficiaire en temps réel de l'arrivée de son prestataire ; réduire de 20 % d'ici 2029 le délai moyen d'arrivée sur place ; garantir la continuité du service jour et nuit et respecter durablement le règlement européen sur la résilience opérationnelle numérique du secteur financier (DORA), applicable à VALMÉRIS depuis le 17 janvier 2025 ; fournir au groupe TERRANDÈLE des données de durabilité fiables et réduire l'empreinte des interventions. Le logiciel de gestion des dossiers d'assistance, développé en interne en 2008, doit être remplacé avant la fin de 2028 par une solution du marché, dans le cadre du projet PASSERELLE.

Vous êtes directeur(rice) de la stratégie et des projets de VALMÉRIS Assistance depuis 2024, rattaché(e) au directeur général, M. Étienne MARVÉJOL ; vous animez le plan stratégique, le portefeuille de projets et les relations avec les principaux prestataires informatiques. M. MARVÉJOL vous demande trois travaux : préparer la transformation numérique de l'assistance et le projet PASSERELLE (dossier 1) ; organiser et exploiter les données des dossiers et du réseau de prestataires (dossier 2) ; renforcer la résilience opérationnelle numérique et fiabiliser les données de durabilité (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de VALMÉRIS Assistance et chiffres clés

VALMÉRIS Assistance est une société anonyme créée en 1994, dont le siège est à Limoges. Entreprise d'assurance agréée pour la branche assistance, elle organise et finance l'aide apportée jour et nuit aux assurés de ses distributeurs. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**L'activité, les actionnaires et les distributeurs**

| Donnée | Valeur |
|---|---|
| Actionnaires | groupe d'assurance mutualiste TERRANDÈLE : 70 % ; réseau bancaire coopératif : 30 % |
| Prestations d'assistance | dépannage et remorquage des véhicules, véhicule de remplacement ; intervention d'urgence au domicile après un dégât des eaux ou une effraction ; aide à domicile, garde d'enfants et transport après un accident |
| Distributeurs | 15 : le groupe TERRANDÈLE et 14 partenaires (assureurs, banques, deux constructeurs automobiles et un loueur de véhicules), qui vendent les garanties d'assistance à leurs clients et transmettent à VALMÉRIS les contrats et les bénéficiaires couverts |
| Réseau de prestataires | 3 400 prestataires agréés : dépanneurs et garages, serruriers, plombiers et vitriers, taxis et loueurs, services d'aide à domicile |

**L'activité en 2026**

| Donnée | Valeur |
|---|---|
| Appels reçus par les trois plateaux | 3,2 millions |
| Dossiers d'assistance ouverts | 520 000 : automobile 60 % ; habitation 25 % ; aide aux personnes 15 % |
| Chiffre d'affaires | 310 M€ |
| Dépenses du système d'information | environ 22 M€, dont 9 M€ de prestations externes |

**L'effectif au 31/12/2026**

| Direction ou service | Salariés |
|---|---|
| Plateaux d'assistance (chargés d'assistance et superviseurs) : Limoges 300, Metz 170, Valence 90 | 560 |
| Réseau de prestataires (sélection, suivi de la qualité, règlement des factures) | 90 |
| Direction des systèmes d'information | 70 |
| Fonctions support (finances, ressources humaines, juridique, risques et conformité, audit interne, relations avec les partenaires) | 100 |
| **Total** | **820** |

**Le système d'information en quelques lignes**

- Logiciel de gestion des dossiers d'assistance, développé en interne en 2008, à remplacer par une solution du marché avant la fin de 2028 (projet PASSERELLE).
- Téléphonie et distribution des appels en ligne, fournies par un opérateur sous forme de service.
- Application mobile des prestataires : acceptation des missions, géolocalisation, photos.
- Progiciel de règlement des prestataires ; progiciels de comptabilité et de paie ; messagerie et bureautique en ligne.
- Échanges quotidiens de fichiers avec les partenaires (contrats et bénéficiaires couverts) ; interfaces de programmation avec les deux constructeurs partenaires (alertes des véhicules connectés).
- Serveurs hébergés par un infogéreur dans deux centres de données situés en France.

**Organigramme simplifié (mars 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil d'administration, présidé par un représentant du groupe TERRANDÈLE | — |
| Nommé par le conseil d'administration | directeur général | M. Étienne MARVÉJOL |
| Rattachés au directeur général | direction des plateaux d'assistance (Limoges, Metz, Valence) | M. Damien CORTHELAY |
| | direction du réseau de prestataires | Mme Sophie GALANDRET |
| | direction des systèmes d'information | Mme Anne-Laure FERVIGNAC |
| | direction de la stratégie et des projets | vous |
| | direction des risques et de la conformité | Mme Isabelle KERDALOU |
| | direction administrative et financière (finances, ressources humaines, juridique, relations avec les partenaires) | M. Franck SALVEDOUX |
| | audit interne | Mme Laure VENDROUX |

### ANNEXE 2.1 – Les règles de gestion des dossiers et le modèle actuel (note de M. Damien CORTHELAY, directeur des plateaux, établie avec la direction des systèmes d'information, février 2027)

**A. Les règles de gestion**

Les plateaux ont écrit, avec la DSI, les règles de gestion suivantes, que la future solution du projet PASSERELLE devra respecter :

- **RG1** – Un bénéficiaire est identifié par un numéro attribué par VALMÉRIS ; on connaît son nom, son prénom et son téléphone. Il est couvert par un ou plusieurs contrats.
- **RG2** – Un contrat est identifié par un numéro attribué par VALMÉRIS. On connaît la référence que lui donne son distributeur, le code de ce distributeur, sa date d'effet et sa date de fin. Le code du distributeur renvoie à la liste des quinze distributeurs, tenue par la direction administrative et financière, qui n'est pas à modéliser. Pour simplifier, un contrat couvre un seul bénéficiaire.
- **RG3** – Un contrat comprend une ou plusieurs garanties ; une garantie appartient à un seul contrat. Une garantie est identifiée par un numéro ; on connaît son code dans la liste des garanties de VALMÉRIS (par exemple « remorquage », « véhicule de remplacement », « serrurerie d'urgence », « aide à domicile »), son libellé et son plafond, montant maximal pris en charge par événement.
- **RG4** – Un dossier est identifié par un numéro. On connaît la date et l'heure de son ouverture, le plateau qui le traite, le type d'événement (panne, accident, dégât des eaux, effraction, perte de clés, immobilisation du bénéficiaire après un accident), la date et l'heure de l'événement et son lieu. Un dossier est ouvert pour un bénéficiaire, au titre d'une seule garantie de l'un de ses contrats ; une garantie peut n'avoir donné lieu à aucun dossier.
- **RG5** – Un dossier donne lieu à une ou plusieurs missions : par exemple un remorquage, puis un taxi et un véhicule de remplacement. Une mission est identifiée par un numéro ; elle porte sur une seule spécialité. On enregistre la date et l'heure de sa création, la date et l'heure de l'arrivée du prestataire sur place, et l'origine de cette heure d'arrivée (géolocalisation de l'application ou saisie par le prestataire).
- **RG6** – Une mission est proposée à un ou plusieurs prestataires, l'un après l'autre, jusqu'à ce que l'un d'eux l'accepte. Pour chaque proposition, on enregistre la date et l'heure de son envoi, la réponse du prestataire (acceptation ou refus), la date et l'heure de cette réponse et, en cas de refus, son motif. Un même prestataire ne reçoit qu'une proposition pour une mission donnée. La mission est réalisée par le prestataire qui l'a acceptée ; tant qu'aucun ne l'a acceptée, elle n'est réalisée par aucun. Un prestataire nouvellement agréé peut n'avoir encore reçu aucune proposition.
- **RG7** – Un prestataire est identifié par son numéro d'agrément ; on connaît sa raison sociale, son téléphone et sa zone d'intervention, décrite par la commune de son dépôt et un rayon en kilomètres. Il est habilité pour une ou plusieurs spécialités.
- **RG8** – Une spécialité est identifiée par un code ; on connaît son libellé (remorquage, dépannage sur place, serrurerie, plomberie, vitrerie, taxi, location de véhicule, aide à domicile, garde d'enfants). Une spécialité nouvellement créée peut n'être exercée par aucun prestataire.
- **RG9** – Les appels, les factures et les règlements des prestataires ne sont pas concernés par ces règles.

**B. Extrait du modèle logique du logiciel actuel**

Clé primaire en gras ; # : clé étrangère.

- BENEFICIAIRE (**num_beneficiaire**, nom, prenom, telephone, code_distributeur, ref_contrat, date_fin_contrat)
- GARANTIE (**code_garantie**, libelle_garantie)
- PRESTATAIRE (**num_agrement**, raison_sociale, telephone, specialite, commune_depot)
- DOSSIER (**num_dossier**, date_heure_ouverture, plateau, type_evenement, date_heure_evenement, lieu_evenement, #num_beneficiaire, #code_garantie, prestataire, heure_demande, heure_arrivee, commentaire)

Précisions de M. CORTHELAY :
- « Le champ "prestataire" du dossier est un texte : le chargé y tape le nom du dépanneur ou de l'artisan. »
- « Quand un dossier appelle une seconde mission, par exemple un taxi après le remorquage, le chargé la décrit dans le champ "commentaire". »
- « Quand un prestataire refuse une mission, le chargé efface son nom et saisit celui du suivant. »
- « Le chargé choisit la garantie dans la liste de toutes les garanties de VALMÉRIS. »

**C. Les constats de 2026**

- Le progiciel de règlement a payé environ 700 000 missions pour 520 000 dossiers : les 180 000 missions qui suivent la première ne sont connues du logiciel des dossiers que par le champ « commentaire ».
- Les 3 400 prestataires agréés apparaissent sous environ 5 000 noms différents dans les dossiers de 2026 : on ne sait pas dire combien de missions chacun a reçues.
- D'après l'application des prestataires, une mission sur cinq a été refusée au moins une fois avant d'être acceptée. Le logiciel des dossiers n'en garde aucune trace : on ne sait ni quels prestataires refusent, ni pourquoi.
- Environ 5 000 dossiers, soit à peu près 1 %, ont été ouverts au titre d'une garantie que le contrat du bénéficiaire ne comportait pas : les prestations ont été organisées et payées sans être dues.
- Un bénéficiaire couvert par deux contrats est enregistré deux fois, une fois par contrat.

### ANNEXE 2.2 – Les échanges de données (constats de Mme Anne-Laure FERVIGNAC, directrice des systèmes d'information, février 2027)

**A. Les flux de données en 2026**

| Flux | Émetteur et destinataire | Forme actuelle | Volume |
|---|---|---|---|
| Contrats et bénéficiaires couverts | 15 distributeurs → logiciel des dossiers | un fichier par distributeur, déposé chaque nuit sur un serveur d'échange ; neuf formes de fichiers différentes (tableurs, fichiers texte à séparateurs, formats propres à un distributeur) ; chaque distributeur emploie ses propres codes de garanties | environ 6 millions de bénéficiaires couverts ; de 20 000 à 40 000 mises à jour par nuit |
| Alertes des véhicules connectés | 2 constructeurs → serveur d'échange de VALMÉRIS | une interface de programmation par constructeur, chacune dans le format de ce constructeur ; le logiciel des dossiers ne sait pas lire ces alertes : le serveur d'échange les transmet aux plateaux par courriel automatique, et les chargés les ressaisissent ; les douze autres partenaires ne transmettent aucune alerte | environ 30 000 alertes |
| Missions, acceptations, refus et heures d'arrivée | logiciel des dossiers ↔ application des prestataires | la mission part vers l'application, où le prestataire l'accepte ou la refuse ; l'acceptation et l'heure d'arrivée reviennent au logiciel des dossiers par un fichier transmis chaque nuit, les refus restent dans l'application ; pendant l'intervention, le chargé suit la mission par téléphone | environ 700 000 missions |
| Factures des prestataires | prestataires → progiciel de règlement | factures en PDF envoyées par courriel ou sur papier, ressaisies par 25 agents de la direction du réseau de prestataires, puis rapprochées à la main des dossiers | environ 700 000 factures |

**B. Les anomalies relevées en 2026**

- Environ 300 000 bénéficiaires figurent en double, soit un sur vingt : le même bénéficiaire a été transmis par deux distributeurs, ou par le même distributeur sous une autre orthographe ou avec un autre téléphone.
- Pour environ 26 000 dossiers (5 %), le chargé n'a pas trouvé le bénéficiaire au moment de l'appel : fiche en double, fichier du distributeur arrivé en retard ou rejeté. Il ouvre alors le dossier « sous réserve » et appelle le distributeur, ce qui allonge l'appel d'environ cinq minutes.
- Les quinze distributeurs emploient au total environ 1 200 codes pour les 40 garanties de VALMÉRIS. Deux informaticiens tiennent à la main une table de correspondance ; environ 3 % des contrats reçus portent un code inconnu ou mal traduit.
- Les dates arrivent sous trois formes (jour/mois/année, mois/jour/année, année-mois-jour) : en 2026, environ 15 000 contrats ont été enregistrés avec une date de fin erronée, le 3 avril étant par exemple lu comme le 4 mars.
- Environ 4 % des factures ressaisies comportent une erreur (montant, numéro de dossier), le plus souvent découverte quand le prestataire réclame son paiement.

**C. Des mots qui n'ont pas le même sens**

Il n'existe aucun dictionnaire des données commun aux distributeurs, aux plateaux et au réseau de prestataires. Trois exemples :
- « bénéficiaire » : pour certains distributeurs, le seul titulaire du contrat ; pour d'autres, toutes les personnes de son foyer, transmises comme autant de bénéficiaires ;
- « délai d'arrivée » : à Limoges et à Metz, il est compté à partir de l'ouverture du dossier ; à Valence, à partir de l'acceptation de la mission par le prestataire, qui intervient en moyenne une dizaine de minutes après l'ouverture du dossier ;
- « dossier clos » : pour les plateaux, à la fin de la dernière mission ; pour le réseau de prestataires, au paiement de la dernière facture.

**D. Les responsabilités**

Aucune direction n'est responsable de ces données. La DSI corrige chaque nuit les fichiers rejetés ; les plateaux découvrent les erreurs pendant l'appel ; le service des relations avec les partenaires, rattaché à la direction administrative et financière, négocie les conventions de distribution sans aucune clause sur la qualité des fichiers transmis. Mme FERVIGNAC : « Nous réparons chaque nuit les fichiers des autres, et personne ne nous dit quelle version est la bonne. »

### ANNEXE 2.3 – Les délais d'arrivée des prestataires (tableaux préparés par la direction des plateaux, février 2027)

**A. Les indicateurs par plateau, 2025 et 2026**

Toutes les valeurs sont arrondies.

| Indicateur | Limoges 2025 | Limoges 2026 | Metz 2025 | Metz 2026 | Valence 2025 | Valence 2026 | Ensemble 2025 | Ensemble 2026 |
|---|---|---|---|---|---|---|---|---|
| Missions | 420 000 | 380 000 | 150 000 | 210 000 | 110 000 | 110 000 | 680 000 | 700 000 |
| Délai moyen d'arrivée (minutes) | 52 | 47 | 50 | 56 | 40 | 38 | 50 | 48 |
| Délai médian d'arrivée (minutes) | 42 | 38 | 40 | 42 | 32 | 30 | 40 | 38 |
| Part des arrivées au-delà de 60 minutes | 26 % | 22 % | 24 % | 30 % | 16 % | 15 % | 24 % | 23 % |
| Part des missions refusées au moins une fois | 18 % | 17 % | 20 % | 28 % | 16 % | 15 % | 18 % | 20 % |
| Part des heures d'arrivée saisies à la main par le prestataire | 30 % | 30 % | 30 % | 35 % | 60 % | 70 % | 35 % | 38 % |
| Part des bénéficiaires satisfaits du délai (enquête) | 80 % | 83 % | 82 % | 74 % | 80 % | 79 % | 80 % | 80 % |

Délai moyen d'arrivée, ensemble des plateaux : pendant les trois mois d'hiver (janvier, février et décembre), qui représentent environ un quart des missions de l'année, 60 minutes en 2025 et 52 minutes en 2026 ; de mars à novembre, 47 minutes en 2025 comme en 2026.

**B. Les missions de 2026 par type de zone**

| Plateau | Part des missions en zone urbaine | en zone périurbaine | en zone rurale | Délai moyen en zone urbaine (minutes) | en zone périurbaine | en zone rurale |
|---|---|---|---|---|---|---|
| Limoges | 40 % | 35 % | 25 % | 32 | 46 | 72 |
| Metz | 30 % | 30 % | 40 % | 34 | 50 | 76 |
| Valence | 70 % | 20 % | 10 % | 30 | 48 | 74 |
| Ensemble | 42 % | 31 % | 27 % | 32 | 47 | 74 |

En 2025, les missions se répartissaient ainsi entre zones urbaine, périurbaine et rurale : Limoges 35 %, 35 % et 30 % ; Metz 40 %, 35 % et 25 % ; Valence 70 %, 20 % et 10 %.

**C. L'affirmation du directeur des plateaux**

M. Damien CORTHELAY : « Valence est notre meilleur plateau : ses délais sont les plus courts depuis deux ans et, avec 38 minutes, il a déjà le délai que vise "Assister 2030" pour 2029. Je propose d'organiser Limoges et Metz sur son modèle et de verser à chaque plateau une prime liée à son délai moyen. Je présenterai ces résultats au comité de direction du mois prochain. »

**D. Les limites signalées par la DSI**

- L'heure d'arrivée est soit la position relevée par l'application du prestataire, soit l'heure qu'il saisit lui-même, à la main, quand la géolocalisation est désactivée ou qu'il le préfère.
- Chaque plateau calcule le délai selon ses propres règles (annexe 2.2 C).
- Les mois de janvier, février et décembre 2026 ont été nettement plus doux que ceux de 2025 : moins de batteries à plat, presque pas de neige.
- Depuis janvier 2026, quatre départements ruraux de l'Est, traités jusque-là par Limoges, sont confiés à Metz ; le réseau de prestataires y est encore peu dense.
- La satisfaction est mesurée par un message envoyé au bénéficiaire après l'intervention ; environ 15 % des bénéficiaires y répondent.

### ANNEXE 2.4 – La proposition de registre commun des missions (note du consortium, reçue en janvier 2027, et objections de la DSI)

**A. La proposition du consortium**

Deux assisteurs concurrents de VALMÉRIS et deux fédérations régionales de dépanneurs, qui réunissent environ 1 000 entreprises de dépannage et de remorquage, invitent VALMÉRIS à former avec eux un consortium. Environ 600 de ces entreprises appartiennent aussi au réseau de VALMÉRIS, qui compte environ 1 400 dépanneurs et garages parmi ses 3 400 prestataires.

Le consortium propose un **registre commun des missions**, fondé sur une chaîne de blocs privée et permissionnée :
- chacun des cinq membres (trois assisteurs, deux fédérations) exploite un nœud qui détient une copie complète du registre ; les dépanneurs y accèdent par le nœud de leur fédération ;
- chaque assisteur y inscrit ses missions de dépannage et de remorquage ; le dépanneur y inscrit l'acceptation, l'arrivée et la fin de l'intervention, relevées par son application, puis sa facture ; chaque inscription est signée par son auteur ;
- les inscriptions sont regroupées en blocs ; chaque bloc contient l'empreinte du bloc précédent et n'est ajouté au registre qu'avec l'accord d'au moins trois des cinq nœuds ; il n'y a ni minage, ni jeton, ni cryptoactif ;
- pour éviter toute contestation, chaque mission comprend le lieu de l'intervention, l'immatriculation du véhicule, le nom et le téléphone du bénéficiaire et les photos du véhicule ;
- un contrat automatisé, inscrit dans le registre, compare la facture au barème de la mission et, si elle le respecte, déclenche l'ordre de virement en euros de l'assisteur dès que la fin de l'intervention est inscrite : le dépanneur serait payé en 48 heures, au lieu de 35 jours en moyenne aujourd'hui chez VALMÉRIS ;
- les règles du registre (admission des membres, barèmes, évolution du contrat automatisé) seraient décidées à la majorité des cinq membres.

Coût pour VALMÉRIS : 300 k€ de participation à la construction du registre en 2027, et 150 k€ par an de participation au fonctionnement, dès 2027. La DSI estime à 250 k€ le raccordement du registre au logiciel des dossiers et au progiciel de règlement.

Arguments du consortium : « Une seule version des faits, partagée et infalsifiable : la confiance entre assisteurs et dépanneurs, et la fin des litiges sur les factures. » En 2026, VALMÉRIS a reçu environ 300 000 factures de dépannage et de remorquage ; environ 15 000, soit 5 %, ont été contestées, le plus souvent sur l'heure d'arrivée, la distance de remorquage ou la majoration de nuit. Dix agents du réseau de prestataires, dont le coût complet est d'environ 50 k€ par an chacun, consacrent l'essentiel de leur temps à ces contestations.

**B. Les objections de Mme FERVIGNAC**

- « Le registre n'enregistre que ce qu'on lui donne : si l'heure d'arrivée est saisie à la main, elle sera inscrite à la main, mais pour toujours. »
- « Nos deux concurrents verraient nos missions, nos bénéficiaires et nos barèmes. »
- « Qui décide quand les cinq membres ne sont pas d'accord ? Et si un assisteur quitte le consortium ? »
- « Le registre ne concerne que les dépanneurs de deux fédérations, pas les serruriers, les plombiers ni les services d'aide à domicile. »
- « Le raccordement à l'ancien logiciel serait à refaire avec la solution retenue par le projet PASSERELLE. »
- « Une plateforme d'échange centralisée ferait-elle aussi bien ? » La DSI propose d'étendre l'application des prestataires : tous les prestataires y déposeraient leur facture, rattachée automatiquement à la mission et contrôlée par rapport au barème et aux heures géolocalisées ; les factures conformes seraient payées sous dix jours. Coût : 300 k€ en 2027, et 50 k€ par an de maintenance, dès 2027.

### ANNEXE 2.5 – Le coût du système d'information des dossiers (note de M. Franck SALVEDOUX, directeur administratif et financier, février 2027)

**A. Les coûts de 2026**

| Poste | Coût annuel (k€) |
|---|---|
| Logiciel interne de gestion des dossiers : maintenance et évolutions, prestations comprises | 2 400 |
| Téléphonie et distribution des appels en ligne (abonnement à l'opérateur, facturé selon le nombre d'appels) | 3 200 |
| Application mobile des prestataires (abonnement, facturé selon le nombre de missions) | 700 |
| Hébergement des serveurs du logiciel des dossiers chez l'infogéreur | 1 100 |
| Échanges avec les distributeurs et les constructeurs (serveur d'échange, interfaces) | 400 |
| Part des autres coûts de la DSI (support aux plateaux, sécurité, postes de travail des chargés) | 2 600 |
| **Total** | **10 400** |

Ne sont comptées que les dépenses que la comptabilité analytique rattache au système d'information des dossiers.

**B. Les dossiers de 2026 par type**

| Donnée | Automobile | Habitation | Aide aux personnes |
|---|---|---|---|
| Dossiers ouverts | 312 000 | 130 000 | 78 000 |
| Appels reçus par dossier, en moyenne | 6 | 4 | 9 |
| Missions par dossier, en moyenne | 1,5 | 1 | 1,3 |
| Durée moyenne du suivi d'un dossier, de son ouverture à sa clôture | 1 jour | 2 jours | 15 jours |

Environ 100 000 appels n'ont donné lieu à aucun dossier (demandes de renseignements). Un dossier d'aide aux personnes (aide à domicile, garde d'enfants, transport) est suivi pendant plusieurs jours, avec des appels réguliers au bénéficiaire et au service d'aide à domicile.

**C. Le tableau de bord actuel du comité de direction**

Chaque mois, le comité de direction reçoit une page : le nombre d'appels reçus par chaque plateau, comparé au même mois de l'année précédente. M. MARVÉJOL : « Ce tableau me dit si nous sommes débordés. Il ne me dit ni si nous aidons bien nos bénéficiaires, ni ce que cela nous coûte, ni les risques que nous courons. »

### ANNEXE 2.6 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Une donnée à caractère personnel est toute information se rapportant à une personne physique identifiée ou identifiable, directement ou indirectement (nom, numéro d'identification, données de localisation…). Les données sont collectées pour des finalités déterminées ; elles sont adéquates et limitées à ce qui est nécessaire (minimisation), exactes et tenues à jour, et conservées pendant une durée n'excédant pas celle nécessaire aux finalités. Le responsable du traitement ne fait appel qu'à des sous-traitants qui présentent des garanties suffisantes, liés à lui par un contrat. | Applicable depuis le 25/05/2018 |
| ISO 22739:2024 – Chaînes de blocs et technologies de registres distribués – Vocabulaire | Norme de vocabulaire : elle définit les termes du domaine (registre distribué, bloc, nœud, consensus, contrat intelligent, jeton…). Ce n'est pas une norme d'exigences. | 2e édition, publiée en 2024 |
| DAMA-DMBOK (DAMA International), 2e édition | Référentiel de bonnes pratiques de gestion des données, organisé en onze domaines autour de la gouvernance des données, dont l'intégration et l'interopérabilité des données, les métadonnées, les données de référence et la qualité des données. | 2e édition (2017), révision engagée en 2024 |

Il n'est demandé aucune analyse juridique.

### Travail à faire

Les données des dossiers d'assistance sont mal structurées et arrivent de quinze distributeurs, de deux constructeurs et de 3 400 prestataires sous des formes qui ne s'accordent pas, alors qu'« Assister 2030 » veut informer les bénéficiaires en temps réel et réduire de 20 % le délai moyen d'arrivée. M. MARVÉJOL vous demande de préparer le modèle des données du futur logiciel, d'organiser les échanges de données, d'analyser les délais d'arrivée, de donner votre avis sur la proposition du consortium et d'éclairer le coût du système d'information des dossiers et son pilotage. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.6 ainsi que vos connaissances professionnelles.

**2.1 – Le modèle des données des dossiers et des missions (3 points)**

a) Relevez trois défauts du modèle logique actuel (annexe 2.1 B) au regard des règles de gestion de l'annexe 2.1 A, en reliant chacun à un constat de l'annexe 2.1 C.

b) Après avoir rappelé ce que traduisent les cardinalités d'un modèle conceptuel des données, construisez le modèle conceptuel des données des dossiers et des missions (entités, identifiants, attributs, associations et cardinalités) à partir des règles de gestion de l'annexe 2.1 A, en montrant comment il conserve l'historique des propositions refusées. Déduisez-en le modèle logique, en énonçant les règles de passage utilisées. Aucune requête n'est attendue.

**2.2 – Les échanges de données avec les distributeurs, les constructeurs et les prestataires (2,5 points)**

a) Après avoir défini l'interopérabilité et la qualité des données, analysez trois problèmes tirés de l'annexe 2.2. Rattachez chacun à un niveau d'interopérabilité (technique, syntaxique, sémantique ou organisationnel) et à une dimension de la qualité des données, et précisez sa conséquence pour les plateaux, le réseau de prestataires ou les bénéficiaires.

b) Proposez l'organisation cible des échanges de données de VALMÉRIS en quatre mesures : les formats et les canaux d'échange ; la codification commune des garanties et le dictionnaire des données ; les contrôles à l'entrée des données ; les responsabilités sur les données reçues des partenaires. Le détail technique des échanges n'est pas attendu.

**2.3 – Les délais d'arrivée des prestataires (3,5 points)**

a) Justifiez la démarche que vous retenez pour exploiter l'annexe 2.3, en distinguant l'analyse descriptive et l'analyse exploratoire, puis formulez trois constats argumentés tirés de cette annexe, chacun assorti d'une précaution de lecture. Aucun calcul statistique n'est attendu.

b) Appréciez l'affirmation et la proposition du directeur des plateaux (annexe 2.3 C), au regard de la mesure des délais (moyenne et médiane, origine de l'heure d'arrivée, définition du délai) et des effets de structure (zones, météo). Indiquez ensuite deux évolutions de la chaîne de traitement des données (collecte, nettoyage, structuration) qui permettront de comparer les plateaux de façon juste.

c) Proposez deux représentations visuelles adaptées au comité de direction, en justifiant chacune par son message et par le piège de lecture qu'elle évite.

**2.4 – Le registre commun des missions (2 points)**

a) Expliquez le fonctionnement du registre proposé par le consortium (annexe 2.4 A) : registre partagé entre les membres, blocs chaînés par des empreintes, consensus, clés et signatures, contrat automatisé. Distinguez-le d'une base de données centralisée.

b) Appréciez la valeur ajoutée, les coûts et les limites du projet pour VALMÉRIS, par rapport à la plateforme d'échange centralisée proposée par la DSI, en estimant de tête le coût de chacune des deux solutions sur trois ans (2027 à 2029). Donnez ensuite un avis motivé à M. MARVÉJOL. Aucune analyse juridique ni aucun développement informatique ne sont attendus.

**2.5 – Le coût du système d'information des dossiers et son pilotage (2 points)**

a) Après avoir défini un inducteur de coût, calculez de tête le coût annuel du système d'information des dossiers par dossier à partir de l'annexe 2.5 A. Montrez ensuite, par deux arguments tirés de l'annexe 2.5, pourquoi ce coût moyen unique ne reflète pas le coût d'un dossier automobile, d'habitation ou d'aide aux personnes. Aucune répartition chiffrée n'est attendue.

b) Proposez deux indicateurs qui, aux côtés des appels reçus, équilibreront le tableau de bord du comité de direction (annexe 2.5 C) entre performance, risque et coût : l'un de coût, l'autre de qualité du service rendu aux bénéficiaires. Précisez pour chacun sa formule, sa source, sa fréquence, sa cible et son axe, ainsi que le risque qu'il permet de surveiller.
