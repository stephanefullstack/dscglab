# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 47

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES SÉJOURS, ÉCLAIRER DEUX PROJETS (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 2.1 – Les besoins d'analyse et les données disponibles (note de M. Loïc FERDANNE, responsable des données à la direction des systèmes d'information, février 2027)

**A. La situation actuelle**

Chaque mois, deux personnes de la direction commerciale et de la relation résidents extraient les données du logiciel de gestion locative, du portail de réservation et du logiciel de suivi des demandes d'intervention, puis les rapprochent dans un tableur : il leur faut quatre jours, soit huit jours-personne par mois. Chaque extraction remplace la précédente : l'historique n'est conservé que dans les tableurs des mois passés, dont les colonnes ont changé plusieurs fois. Un logement n'a pas le même numéro dans le logiciel de gestion locative et dans le logiciel des demandes d'intervention ; le rapprochement se fait à la main, par l'adresse.

Chaque direction calcule ses propres chiffres, selon ses propres règles, qui ne sont écrites nulle part. Pour 2026, le taux d'occupation vaut 93 % dans le rapport du directoire (tiré du logiciel de gestion locative), 91 % dans le tableau de la direction commerciale (annexe 2.2) et 95 % pour la direction financière, qui le calcule à partir des redevances facturées.

**B. Les questions que le directoire veut pouvoir poser**

- Quels sont l'occupation et la vacance par résidence, par ville, par type de logement et par mois ?
- Quelle part de l'occupation de l'été vient des séjours courts ?
- Par quel canal les résidents ont-ils réservé ?
- Les résidents venus de l'étranger occupent-ils les mêmes logements, aux mêmes périodes, que les résidents de France ?
- Quelles redevances chaque résidence a-t-elle facturées ?
- Combien de demandes d'intervention chaque logement suscite-t-il ?

**C. Les règles de gestion de l'entrepôt des séjours**

- **RG1** – Un logement est identifié par un numéro unique, commun à toutes les applications. On connaît son type (studio, logement de deux pièces, colocation) et son nombre de places : une pour un studio ou un logement de deux pièces, autant que de chambres pour une colocation, chaque chambre étant louée par un bail distinct. Un logement appartient à une seule résidence.
- **RG2** – Une résidence est identifiée par un code ; on connaît son nom et sa date d'ouverture. Elle est située dans une seule ville.
- **RG3** – Le mois est identifié par un code (année et mois) ; on connaît l'année, le numéro du mois, la saison (année universitaire, de septembre à juin, ou été, en juillet et août) et l'année universitaire à laquelle il appartient.
- **RG4** – Un profil de séjour est identifié par un code ; il combine le type de séjour (année universitaire, séjour court d'été, aucun séjour) et l'origine du résident (résident en France, résident venu de l'étranger, sans objet).
- **RG5** – Un canal de réservation est identifié par un code ; on connaît son libellé (portail, centre de relation résidents, accueil de la résidence, établissement d'enseignement partenaire, sans objet).
- **RG6** – L'occupation est suivie par logement et par mois, pour chaque profil de séjour et chaque canal de réservation. Un logement occupé le même mois par des séjours de profils ou de canaux différents (fin d'année universitaire puis séjour court d'été ; chambres d'une même colocation) donne une ligne par profil et par canal. Les jours où le logement pouvait être loué mais est resté libre sont rattachés au profil « aucun séjour » et au canal « sans objet ».
- **RG7** – Chaque ligne porte le nombre de jours-places ouverts à la location, le nombre de jours-places occupés, la redevance facturée et le nombre de demandes d'intervention. Un jour-place est une place disponible pendant un jour. Un logement n'est ouvert à la location ni avant l'ouverture de sa résidence, ni pendant des travaux.
- **RG8** – L'entrepôt ne contient aucune donnée nominative et aucune donnée sensible : le résident n'y figure que par son profil de séjour.

### ANNEXE 2.2 – L'occupation et la relocation des logements en 2025 et 2026 (tableau de la direction commerciale et de la relation résidents, janvier 2027)

**A. Par ville**

Taux d'occupation annuel = jours occupés / (logements en fin d'année × 365). Toutes les valeurs sont arrondies.

| Ville | Logements fin 2025 | Logements fin 2026 | Taux d'occupation annuel 2025 | Taux d'occupation annuel 2026 |
|---|---|---|---|---|
| Lyon | 1 500 | 1 500 | 96 % | 96 % |
| Montpellier | 1 200 | 1 200 | 95 % | 95 % |
| Toulouse | 1 000 | 1 000 | 94 % | 88 % |
| Rennes | — | 400 | — | 30 % |
| Onze autres villes | 4 900 | 4 900 | 93 % | 94 % |
| **Ensemble** | **8 600** | **9 000** | **94 %** | **91 %** |

**B. Par type de logement**

Taux d'occupation de l'été : jours occupés en juillet et août / (logements en fin d'année × 62). Part des séjours courts : jours occupés par des séjours courts d'été / jours occupés en juillet et août. Délai de relocation : jours entre le départ d'un résident et l'entrée du suivant.

| Indicateur | Studios 2025 | Studios 2026 | Deux pièces 2025 | Deux pièces 2026 | Colocations 2025 | Colocations 2026 | Ensemble 2025 | Ensemble 2026 |
|---|---|---|---|---|---|---|---|---|
| Logements en fin d'année | 7 000 | 7 200 | 900 | 900 | 700 | 900 | 8 600 | 9 000 |
| Taux d'occupation annuel | 95 % | 93 % | 93 % | 92 % | 84 % | 74 % | 94 % | 91 % |
| Taux d'occupation de l'été | 72 % | 70 % | 66 % | 66 % | 78 % | 61 % | 72 % | 69 % |
| Part des séjours courts dans l'occupation de l'été | 30 % | 30 % | 40 % | 40 % | 70 % | 70 % | — | — |
| Délai moyen de relocation (jours) | 10 | 10 | 15 | 14 | 30 | 35 | 12 | 13 |
| Part des réservations faites sur le portail | 65 % | 70 % | 60 % | 60 % | 30 % | 30 % | 62 % | 65 % |

**C. L'affirmation du directeur commercial et de la relation résidents**

M. Adrien CALVÉRAC : « Les chiffres sont clairs : les colocations se louent mal, de plus en plus mal, et mettent trois fois plus de temps que les studios à se relouer. Il faut les transformer en studios. »

**D. Les limites signalées par M. FERDANNE**

- Les deux résidences de Rennes (400 logements, dont 200 colocations et 200 studios) ont ouvert le 1er septembre 2026 ; elles sont comptées sur toute l'année 2026, été compris.
- À Toulouse, 120 logements d'une résidence ont été fermés pour travaux de janvier à juin 2026 ; ils sont comptés comme vacants.
- Les 900 colocations comptent 2 700 chambres. Le tableau compte les colocations par logement, et non par chambre : une colocation n'est comptée occupée que les jours où toutes ses chambres sont louées, et relouée que lorsque sa dernière chambre libre l'est.
- Le portail ne permet de réserver une colocation qu'entière ; une chambre seule se réserve par courriel auprès du centre de relation résidents.
- L'été, les colocations accueillent surtout des groupes en séjour court.

### ANNEXE 2.3 – Les demandes d'intervention des résidents (constats de Mme Clémence ROUSTAGNE, directrice des résidences, février 2027)

**A. Les constats**

- En 2026, les résidences ont reçu 36 000 demandes d'intervention, soit en moyenne quatre par logement : 30 000 saisies par les résidents dans l'application, en texte libre, et 6 000 enregistrées par les chargés d'accueil.
- Environ 10 000 des demandes saisies dans l'application, soit un tiers, ne sont pas rédigées en français : anglais surtout, mais aussi espagnol, italien, chinois, arabe et une quinzaine d'autres langues.
- Le résident choisit une catégorie dans une liste de huit (plomberie, électricité et chauffage, serrures et accès, internet, électroménager et laverie, ménage, nuisibles, autre). La catégorie « autre » a été choisie pour 12 000 demandes. Sur 500 demandes relues en janvier 2027, une sur quatre était classée dans une mauvaise catégorie.
- Chaque responsable de résidence ne voit que les demandes de sa résidence, une à une. Personne ne sait quelles pannes reviennent, ni dans quelles résidences : le même chauffe-eau défaillant peut donner vingt demandes, classées dans trois catégories différentes.
- Certaines demandes mentionnent un problème de santé, le nom d'un voisin ou un numéro de téléphone.
- Les interventions confiées à des entreprises extérieures ont coûté environ 2 M€ en 2026.

**B. Cinq extraits de demandes (fictives) saisies dans l'application en décembre 2026**

| Demande | Catégorie choisie par le résident |
|---|---|
| « Depuis trois jours, l'eau de la douche est froide le matin. Mon voisin du même étage a le même problème. » | autre |
| "The heater makes a loud noise all night and the room stays cold." | électroménager et laverie |
| « Il y a de la moisissure au plafond de la salle de bains, comme l'hiver dernier. Je suis asthmatique, merci de faire vite. Mon numéro : (numéro de téléphone). » | ménage |
| « El wifi se corta todas las noches entre las 21 h y las 23 h. » | autre |
| « La machine n° 2 de la laverie prend l'argent et ne démarre pas. » | autre |

**C. Le projet de l'équipe données**

M. FERDANNE propose de souscrire un service en ligne d'analyse des textes, proposé par un éditeur, fondé sur l'apprentissage automatique : il attribuerait à chaque demande une catégorie, quelle que soit sa langue, et regrouperait les demandes semblables d'une même résidence pour signaler les problèmes récurrents. Le service serait d'abord ajusté sur 3 000 demandes de 2026, reclassées à la main par des responsables de résidence. Le texte des demandes serait transmis à l'éditeur, qui le conserverait douze mois. Mme ROUSTAGNE : « Si l'outil me dit où sont les pannes qui reviennent, je change les chauffe-eau d'une résidence au lieu d'envoyer vingt fois un plombier. »

### ANNEXE 2.4 – Le projet d'entrepôt des séjours présenté au directoire (note de Mme Solène VARQUIGNY, directrice des systèmes d'information, février 2027)

**A. Le projet**

Construire, d'avril à décembre 2027, un entrepôt des séjours alimenté chaque nuit par le logiciel de gestion locative actuel, le portail de réservation et le logiciel de suivi des demandes d'intervention, et le restituer dans un outil décisionnel en ligne, sur abonnement. Mise en service : janvier 2028. Les définitions des indicateurs seront arrêtées avec les directions lors d'ateliers ; la formation des utilisateurs sera assurée par l'équipe données.

**B. Les coûts de 2027 à 2029** (en k€, sommes rondes)

| Poste | Montant |
|---|---|
| Construction (modèle, chargements des trois sources, premiers tableaux de bord), en 2027 | 300 |
| Abonnement à l'outil décisionnel en ligne, de 2027 à 2029 | 40 k€ par an |
| Exploitation et évolutions de l'entrepôt, de 2027 à 2029 | 60 k€ par an |

Le temps des directions consacré aux ateliers et à la formation n'est pas compté.

**C. Les gains annoncés**

- **Un point de taux d'occupation**, de 93 % à 94 %, soit 90 logements loués de plus sur l'année, grâce à des décisions mieux éclairées. La redevance annuelle moyenne d'un logement est d'environ 8 000 € (680 € par mois, arrondi). « Compté de 2027 à 2029, le gain cumulé représente plus de trois fois le coût du projet : le gain d'une seule année suffit à le couvrir. »
- Le temps des deux personnes qui préparent chaque mois le tableau d'occupation (huit jours-personne par mois) ; ce gain n'est pas chiffré.
- Des interventions mieux ciblées ; ce gain n'est pas chiffré.

**D. L'avis de M. Bastien LORMIÈRE, membre du directoire chargé des finances et du développement**

« Je ne conteste pas l'utilité de l'entrepôt. Mais un point d'occupation dépend des prix, des équipes commerciales, des résidences que nous ouvrons et du marché : un entrepôt ne loue aucun logement. Et 720 k€ de redevances ne font pas 720 k€ de résultat. »

### ANNEXE 2.5 – Les attestations de logement et la proposition d'un prestataire (constats de M. Adrien CALVÉRAC, proposition reçue et note de Mme Solène VARQUIGNY, février 2027)

**A. Les constats**

- En 2026, le centre de relation résidents a établi, à la demande des résidents, 20 000 attestations de logement et 10 000 copies de quittances. Les résidents venus de l'étranger en demandent 60 % : pour des préfectures et des consulats, des banques, des établissements d'enseignement, des organismes de bourses et des employeurs, en France et à l'étranger.
- Ces documents sont produits à partir d'un modèle de traitement de texte, en PDF, avec la signature scannée du responsable de résidence.
- Environ 1 500 organismes nous demandent chaque année de confirmer une attestation, par courriel ou par téléphone ; il faut en moyenne deux jours pour leur répondre.
- En 2026, 40 attestations falsifiées au nom d'ORVANELLE nous ont été signalées, dont 25 par des banques : logements inexistants, personnes jamais accueillies, dates modifiées.

**B. La proposition d'ANCRALYS**

ANCRALYS, prestataire de services d'horodatage, propose :

- de calculer l'empreinte numérique de chaque attestation et de chaque quittance au moment où elle est produite, puis d'inscrire chaque jour ces empreintes dans une transaction d'une chaîne de blocs publique, ouverte à tous, qui fonctionne par preuve d'enjeu ;
- d'imprimer sur chaque document un code qui renvoie à la page de vérification d'ANCRALYS : l'organisme y dépose le document reçu, et la page indique s'il a été inscrit, à quelle date, et s'il a été modifié depuis ;
- en option, d'inscrire aussi dans la chaîne, en clair, le nom du résident et l'adresse du logement, « pour faciliter les recherches ».

ANCRALYS paie elle-même, en crypto-actifs, les frais de transaction de la chaîne de blocs, et facture ORVANELLE en euros : 15 k€ de mise en place, puis 25 k€ par an, soit environ 90 k€ sur trois ans. Son argument : « La chaîne de blocs garde la preuve pour toujours, même si notre société disparaît. »

**C. L'alternative de la direction des systèmes d'information** (note de Mme VARQUIGNY)

Produire automatiquement les attestations et les quittances à partir du logiciel de gestion locative et les signer d'un cachet électronique qualifié au nom d'ORVANELLE, reposant sur un certificat qualifié délivré par un prestataire de services de confiance qualifié : tout lecteur de PDF courant affiche que le document émane d'ORVANELLE et qu'il n'a pas été modifié. Chaque document porterait un numéro et un code renvoyant à une page de vérification du site d'ORVANELLE, qui indique si l'attestation existe, si elle est toujours valable et pour quelles dates. Coût : 40 k€ de mise en place, puis 10 k€ par an, soit environ 70 k€ sur trois ans. « Une attestation de logement peut cesser d'être vraie : un résident part plus tôt que prévu. Il faut pouvoir la retirer. »

### ANNEXE 2.6 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2023/1114 sur les marchés de crypto-actifs (MiCA) | Encadre l'offre au public et l'admission à la négociation de crypto-actifs, l'émission de jetons qui visent une valeur stable (jetons se référant à des actifs, jetons de monnaie électronique) et l'agrément des prestataires de services sur crypto-actifs (PSCA), par exemple la conservation de crypto-actifs pour le compte de clients ou leur échange contre des fonds. Les prestataires enregistrés sous l'ancien régime français (PSAN) ne peuvent plus exercer sans agrément MiCA depuis le 02/07/2026. | Applicable depuis le 30/12/2024 ; dispositions relatives aux jetons se référant à des actifs et aux jetons de monnaie électronique applicables depuis le 30/06/2024 |
| ISO 22739:2024 | Vocabulaire des chaînes de blocs et des technologies de registres distribués (bloc, nœud, consensus, registre, empreinte…). Norme de terminologie : elle ne fixe aucune exigence. | 2e édition (janvier 2024), qui remplace l'édition de 2020 |
| Règlement (UE) n° 910/2014 (eIDAS), révisé par le règlement (UE) 2024/1183 du 11/04/2024 | Cadre européen de l'identification électronique et des services de confiance : signature électronique (personne physique), cachet électronique (personne morale), horodatage électronique, registres électroniques. Une signature ou un cachet qualifiés reposent sur un certificat qualifié délivré par un prestataire de services de confiance qualifié. | En vigueur |
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Une donnée à caractère personnel est toute information se rapportant à une personne physique identifiée ou identifiable. Les données sont collectées pour des finalités déterminées, explicites et légitimes ; elles sont limitées à ce qui est nécessaire (minimisation) et conservées pendant une durée limitée ; certaines données, dont les données concernant la santé, sont soumises à des règles plus strictes. Un prestataire qui traite des données pour le compte d'ORVANELLE est un sous-traitant, lié par un contrat. | Applicable depuis le 25/05/2018 |

Il n'est demandé aucune analyse juridique.

### Travail à faire

Le directoire veut piloter l'occupation des 9 000 logements, et bientôt des 12 000, avec des chiffres fiables et communs à toutes les directions, alors qu'ils sont aujourd'hui rapprochés à la main chaque mois et diffèrent d'une direction à l'autre. Deux projets touchent aux données des séjours : l'entrepôt des séjours, dont la direction des systèmes d'information annonce un fort retour sur investissement, et la certification des attestations de logement, menacée par des falsifications. Mme TRÉVARDIN vous demande de concevoir l'entrepôt des séjours, d'en exploiter les premières analyses, d'apprécier le retour sur investissement annoncé et d'éclairer le choix d'une solution pour les attestations. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.6 ainsi que vos connaissances professionnelles.

**2.1 – L'entrepôt des séjours (3,5 points)**

a) Après avoir défini l'entrepôt de données, montrez, à partir de l'annexe 2.1, trois raisons pour lesquelles il répondrait mieux que les extractions mensuelles aux questions du directoire.

b) À partir des règles de gestion de l'annexe 2.1 C, concevez le schéma en étoile de l'entrepôt des séjours : la table des faits et sa granularité, les dimensions et leurs attributs, les mesures. Traduisez-le ensuite en modèle logique. Aucune requête n'est attendue.

**2.2 – L'analyse de l'occupation et des demandes d'intervention (4 points)**

a) Après avoir présenté les étapes de la chaîne de traitement des données, décrivez celle qui alimentera l'entrepôt et produira les indicateurs d'occupation, en montrant à quelle étape et comment elle corrige chacune des trois limites de mesure du tableau actuel (annexe 2.2 D) et l'écart entre les taux d'occupation des directions (annexe 2.1 A).

b) Formulez trois constats argumentés tirés de l'annexe 2.2, puis appréciez l'affirmation de M. CALVÉRAC. Aucun calcul statistique n'est attendu.

c) À partir de l'annexe 2.3, montrez deux apports de l'exploitation du texte des demandes d'intervention pour ORVANELLE et précisez la méthode d'analyse qu'elle mobilise (descriptive, exploratoire), en la justifiant. Indiquez ensuite deux précautions à prendre avant de lancer le service proposé par l'équipe données. Aucun développement d'algorithme n'est attendu.

**2.3 – Le retour sur investissement du projet d'entrepôt (3 points)**

a) Après avoir défini le retour sur investissement d'un projet de système d'information, calculez de tête, à partir de l'annexe 2.4, le gain annoncé sur trois ans, le coût du projet sur trois ans et le retour sur investissement qui en résulte.

b) Appréciez ce calcul : discutez l'attribution du point d'occupation à l'entrepôt, en répondant à M. LORMIÈRE, puis relevez deux coûts cachés du projet. Aucun calcul actualisé n'est attendu.

c) Proposez deux indicateurs de suivi des bénéfices du projet, précisés chacun par sa formule, sa source, sa fréquence, sa cible et son axe.

**2.4 – Les attestations de logement et la chaîne de blocs (2,5 points)**

a) Après avoir expliqué le fonctionnement d'une chaîne de blocs publique et ce que garantit l'inscription de l'empreinte d'un document, situez la proposition d'ANCRALYS dans la typologie des applications de la chaîne de blocs.

b) Appréciez deux apports et deux limites de la proposition d'ANCRALYS face au cachet électronique proposé par la direction des systèmes d'information, puis recommandez l'une des deux solutions, en la justifiant.

c) Indiquez, d'après les repères de l'annexe 2.6, si le règlement MiCA s'applique à ORVANELLE dans ce projet, et pourquoi.
