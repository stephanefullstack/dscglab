# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 12

**DOSSIER 3 – AUDITER LE PORTAIL DES ABONNÉS ET ORIENTER LA STRATÉGIE DE LA RELATION NUMÉRIQUE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 4, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. La Régie des eaux de l'agglomération de MORVÈZE est un établissement public local à caractère industriel et commercial, créé en 2016 par la communauté d'agglomération de Morvèze (32 communes, 310 000 habitants) pour gérer en direct le service public de l'eau potable et de l'assainissement. Elle emploie 380 agents et dessert 160 000 abonnés. Elle exploite deux usines de production d'eau potable, cinq stations de traitement des eaux usées et 2 400 kilomètres de canalisations ; 120 sites (réservoirs, stations de pompage, usines) sont pilotés à distance par un système de supervision centralisé. Ses recettes de l'exercice 2026 s'élèvent à 70 millions d'euros, dont 38 millions pour l'eau potable et 32 millions pour l'assainissement ; 3,5 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Après l'été 2026, marqué par une sécheresse et par des restrictions d'usage de l'eau, le conseil d'administration de la régie a adopté en décembre 2026 le plan stratégique « MORVÈZE EAU 2032 ». Il fixe trois priorités : réduire les pertes du réseau grâce aux données des compteurs en télérelève, qui équipent 60 000 abonnés et seront généralisés d'ici 2029 ; renforcer la sécurité des installations, après une connexion suspecte détectée en novembre 2026 sur le système de supervision ; moderniser la relation avec les abonnés, dont 40 % utilisent déjà le portail en ligne de la régie. La directrice générale, Mme Mathilde ROCHEVAL, rend compte de la mise en œuvre du plan au conseil d'administration, présidé par M. Gilles VAUQUIERS, vice-président de la communauté d'agglomération.

Vous venez de rejoindre la régie comme chargé(e) de mission auprès de la directrice générale. Mme ROCHEVAL vous confie trois travaux : exploiter les données de télérelève pour réduire les pertes et piloter le programme qui leur est consacré (dossier 1) ; sécuriser le système de supervision des installations et les accès à celui-ci (dossier 2) ; auditer le portail des abonnés et orienter la stratégie de la relation numérique (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de la Régie des eaux de l'agglomération de MORVÈZE et chiffres clés

La Régie des eaux de l'agglomération de MORVÈZE est un établissement public local à caractère industriel et commercial, créé en 2016 par la communauté d'agglomération de Morvèze, qui lui a confié la gestion directe du service public de l'eau potable et de l'assainissement sur ses 32 communes. Elle est administrée par un conseil d'administration, présidé par M. Gilles VAUQUIERS, vice-président de la communauté d'agglomération, et dirigée par une directrice générale. Ses abonnés sont des particuliers, des entreprises et des collectivités. Son exercice coïncide avec l'année civile.

**Chiffres clés de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Activité | production et distribution d'eau potable ; collecte et traitement des eaux usées |
| Territoire desservi | communauté d'agglomération de Morvèze : 32 communes, 310 000 habitants |
| Abonnés | 160 000 (particuliers, entreprises, collectivités) |
| Agents | 380 |
| Recettes | 70 M€ : eau potable 38 M€, assainissement 32 M€ |
| Budget du système d'information | 3,5 M€ (5 % des recettes) |
| Installations | deux usines de production d'eau potable ; cinq stations de traitement des eaux usées ; 2 400 km de canalisations |
| Supervision | 120 sites (réservoirs, stations de pompage, usines) pilotés à distance par un système de supervision centralisé |
| Télérelève | 60 000 abonnés équipés de compteurs en télérelève fin 2026 ; généralisation aux 160 000 abonnés d'ici 2029 |
| Plan « MORVÈZE EAU 2032 » (adopté en décembre 2026) | réduire les pertes du réseau grâce aux données de télérelève ; renforcer la sécurité des installations après la connexion suspecte de novembre 2026 sur la supervision ; moderniser la relation avec les abonnés (40 % utilisent le portail en ligne) |

**Organigramme simplifié (mars 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil d'administration | président, vice-président de la communauté d'agglomération | M. Gilles VAUQUIERS |
| Direction générale | directrice générale, qui rend compte au conseil d'administration de la mise en œuvre du plan « MORVÈZE EAU 2032 » | Mme Mathilde ROCHEVAL |
| Rattaché(e) à la directrice générale | chargé(e) de mission (poste créé en 2027) | vous |
| Rattachée à la directrice générale | déléguée à la protection des données | Mme Hélène BARJOLLE |
| Comité de direction | directeur de l'exploitation (usines, stations de traitement des eaux usées, réseaux, équipes d'intervention, centre de supervision) | M. Thierry SALVANHAC |
| Comité de direction | directrice de la clientèle (accueil, facturation, relève des compteurs, portail des abonnés) | Mme Élodie FARGEMONT |
| Comité de direction | responsable de la direction des systèmes d'information (DSI, 14 agents) | Mme Nathalie CORVESSE |
| Rattaché à la responsable de la DSI | responsable de la sécurité des systèmes d'information (fonction exercée à mi-temps) | M. Yannick LORBEL |
| Comité de direction | directeur administratif et financier (budget, comptabilité, contrôle de gestion) | M. Laurent CHAZELON |
| Rattaché au directeur administratif et financier | responsable du contrôle de gestion | M. Sébastien VELOUZE |
| Comité de direction | directrice des ressources humaines | Mme Claire AUBRESPIN |

### ANNEXE 3.1 – Le portail des abonnés

**Note de Mme Élodie FARGEMONT, directrice de la clientèle, à la directrice générale (février 2027)**

**A. Fonctions et organisation**

Ouvert en 2020, le portail des abonnés est une solution en ligne de l'éditeur VELIZANE, utilisée sur abonnement (120 000 € par an). Il propose six fonctions : souscription et résiliation d'un contrat (emménagement, déménagement) ; mensualisation des paiements ; paiement en ligne des factures, par l'intermédiaire du prestataire de paiement de la banque de la régie ; suivi de la consommation (index relevés deux fois par an ou, pour les abonnés équipés en télérelève, consommation mensuelle importée chaque mois de la plateforme de télérelève) ; dépôt et suivi des réclamations ; alertes par courriel ou par SMS (facture disponible, échéance de paiement, travaux, restrictions d'usage de l'eau, conseils d'économie d'eau, lettre d'information, enquêtes).

Le logiciel de facturation, installé dans les locaux de la régie et administré par la DSI, reste la référence des contrats, des index, des factures et des paiements. Chaque nuit, un échange de fichiers transmet au logiciel de facturation les souscriptions, résiliations, changements de coordonnées et paiements saisis sur le portail, et transmet au portail les factures et les situations de compte. Un agent de la DSI suit ces échanges, parmi d'autres tâches.

La direction de la clientèle compte 60 agents, dont 35 agents de l'accueil (ouvert du lundi au vendredi de 8 h 30 à 17 h) et du centre d'appels (de 8 h à 18 h), qui consultent et modifient les comptes du portail pour le compte des abonnés.

**B. Chiffres de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Comptes ouverts sur le portail (fin 2026) | 82 000 : 70 000 comptes d'abonnés actuels, détenus par 66 000 abonnés, et 12 000 comptes d'anciens abonnés |
| Abonnés qui se sont connectés au moins une fois en 2026 | 64 000, soit 40 % des 160 000 abonnés |
| Démarches en ligne | 90 000 paiements de factures ; 6 000 des 16 000 emménagements et déménagements |
| Réclamations reçues | 12 000 : 6 000 sur le portail, 4 000 par téléphone, 2 000 à l'accueil ou par courrier ; délai moyen de traitement de 18 jours, pour un engagement de 8 jours inscrit dans la charte de service de la régie |
| Disponibilité du portail mesurée par l'éditeur | 99 % de l'année, soit près de 90 heures d'interruption ; le contrat prévoit 99,5 %, soit environ 45 heures au plus |
| Appels reçus par le centre d'appels | 150 000, dont 30 % portent sur une difficulté du portail (mot de passe, facture non visible, paiement non pris en compte) ; aux heures de pointe, un appel sur quatre n'aboutit pas |
| Satisfaction (enquête d'octobre 2026) | 62 % des utilisateurs du portail satisfaits ; 75 % des abonnés reçus à l'accueil ou au téléphone satisfaits |
| Demandes d'évolution du portail adressées par la direction de la clientèle à la DSI | 40 demandes : 12 réalisées, 10 refusées ou reportées, 18 en attente sans décision |

**C. Les relations entre les directions**

Faute d'instance pour trancher, les désaccords entre la direction de la clientèle et la DSI sont remontés à la directrice générale, qui a rendu six arbitrages en 2026, le plus souvent par courriel. En juin 2026, la direction de la clientèle a commandé directement à VELIZANE un module de prise de rendez-vous en ligne (15 000 €), sans associer la DSI ni la déléguée à la protection des données ; ce module n'est pas relié à l'agenda de l'accueil : en janvier 2027, 200 abonnés se sont présentés à un rendez-vous que les agents ne voyaient pas.

**Mme Élodie FARGEMONT, directrice de la clientèle** : « Nos abonnés attendent le service qu'ils trouvent auprès de leur banque. Cela fait deux ans que je demande les alertes de surconsommation ; chaque demande s'enlise à la DSI. »

**Mme Nathalie CORVESSE, responsable de la DSI** : « Chaque fonction nouvelle ajoute un échange avec la facturation que personne ne documente ; les interruptions de mars et de septembre viennent de là. Je ne mettrai rien en service sans recette ni examen de ses effets sur la facturation et sur la protection des données. »

**Mme Hélène BARJOLLE, déléguée à la protection des données** : « Je découvre les nouvelles fonctions du portail quand elles sont déjà en ligne. »

**Mme Mathilde ROCHEVAL, directrice générale** : « Je ne veux plus arbitrer seule, au cas par cas, des sujets dont je ne connais ni les coûts ni les risques, ni découvrir un désaccord le jour de la mise en service. Le conseil d'administration n'a jamais examiné le portail, alors que le plan en fait une priorité. »

### ANNEXE 3.2 – Constats préalables à l'audit et repères au 31/12/2026

**A. Constats relevés en février 2027 auprès de la direction de la clientèle, de la DSI et de la déléguée à la protection des données**

| N° | Constat |
|---|---|
| 1 | **Doublons et échanges avec la facturation** : 4 000 abonnés détiennent deux comptes, ouverts lors d'un emménagement sans rapprochement avec le contrat existant. L'échange de la nuit rejette en moyenne 150 enregistrements, repris à la main par le service de la facturation dans un délai moyen de huit jours ; aucun total n'est comparé entre le portail et la facturation. En 2026, 900 paiements en ligne ont été enregistrés en retard dans la facturation, ce qui a provoqué 600 relances envoyées à tort. |
| 2 | **Interruptions pendant les périodes de facturation** : sur les près de 90 heures d'interruption de 2026, 60 heures se situent pendant les deux vagues de facturation semestrielle (mars et septembre), quand les connexions triplent. La régie ne mesure pas elle-même la disponibilité du portail : elle reçoit chaque année le relevé de l'éditeur. |
| 3 | **Choix des abonnés en matière d'alertes** : 25 000 abonnés reçoivent les alertes facultatives (conseils d'économie d'eau, lettre d'information, enquêtes) ; la case correspondante est cochée d'avance lors de la création du compte ; le portail ne conserve ni la date ni le contenu du choix exprimé ; pour ne plus recevoir ces alertes, l'abonné doit appeler le centre d'appels. |
| 4 | **Comptes des anciens abonnés** : les 12 000 comptes d'anciens abonnés ouverts depuis 2020 restent consultables par les agents, avec les coordonnées, l'historique des consommations et des réclamations et, pour 5 000 d'entre eux, les coordonnées bancaires. Aucune durée de conservation n'est fixée ; le registre des activités de traitement de la régie ne comporte pas de fiche pour le portail, dont les données sont rattachées à la fiche « facturation » ; le contrat conclu avec VELIZANE ne précise pas le sort des données à la fin du contrat. |
| 5 | **Droits des agents de l'accueil et du centre d'appels** : les 35 agents disposent d'un profil unique qui permet de consulter tous les comptes, de modifier les coordonnées bancaires et l'adresse de facturation, de clore un compte et de clôturer une réclamation. Une modification de coordonnées bancaires n'est ni validée par un second agent ni signalée à l'abonné ; les droits n'ont jamais été revus depuis 2020. En 2026, deux abonnés ont signalé une modification de leurs coordonnées bancaires qu'ils n'avaient pas demandée. |
| 6 | **Réclamations non suivies** : 1 500 des 6 000 réclamations déposées sur le portail ont été clôturées automatiquement au bout de 30 jours sans réponse, selon un réglage d'origine de l'éditeur ; les réclamations reçues par téléphone sont suivies dans un tableur ; aucun indicateur de délai n'est produit. |

**B. Repères méthodologiques et réglementaires (au 31/12/2026)**

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Désignation obligatoire d'un délégué à la protection des données par les organismes publics ; il informe et conseille le responsable du traitement et contrôle le respect du règlement. Tenue d'un registre des activités de traitement, qui indique pour chaque traitement ses finalités, les catégories de personnes, de données et de destinataires, les délais prévus pour l'effacement des données et les mesures de sécurité. Protection des données dès la conception et par défaut : seules les données nécessaires sont traitées, durées de conservation comprises. Recours à un sous-traitant (par exemple un éditeur de solution en ligne) encadré par un contrat qui prévoit notamment les instructions, la sécurité, le sort des données à la fin du contrat et les audits. | Applicable depuis le 25/05/2018. Une proposition européenne de simplification (« omnibus numérique », 19/11/2025) modifiant ce règlement est en discussion et n'est pas applicable. |
| COBIT 2019 (ISACA) | Référentiel de gouvernance et de management de l'informatique : 40 objectifs répartis en cinq domaines (évaluer, diriger et surveiller ; aligner, planifier et organiser ; construire, acquérir et mettre en œuvre ; délivrer, servir et soutenir ; surveiller, évaluer et apprécier). | En vigueur |
| ITIL (PeopleCert) | Référentiel de bonnes pratiques de gestion des services informatiques : gestion des niveaux de service, des incidents, des changements, amélioration continue. | En vigueur |

Il n'est demandé aucune analyse juridique des obligations de la régie ni des droits des abonnés.

### ANNEXE 3.3 – Technologies émergentes signalées

**A. Deux propositions reçues par la direction de la clientèle (janvier 2027)**

1. **Assistant conversationnel fondé sur l'IA générative**, proposé par VELIZANE en option du portail : il répondrait jour et nuit, en langage courant, aux questions des abonnés (factures, mensualisation, emménagement et déménagement, restrictions d'usage), à partir de la documentation de la régie et des données du compte de l'abonné connecté, et transmettrait les demandes complexes à un conseiller aux heures d'ouverture. Il repose sur le modèle de langage d'un fournisseur tiers ; l'offre ne précise pas où les échanges sont hébergés. Coût : 60 000 € de mise en place, puis 90 000 € par an. L'éditeur annonce que 40 % des appels pourraient être traités sans conseiller. Une régie d'une autre région, qui l'utilise depuis 2026, indique qu'environ une réponse sur dix a été jugée inexacte pendant les trois premiers mois (démarches de déménagement, dates des restrictions d'usage).
2. **Alertes personnalisées de surconsommation et espace abonné enrichi grâce à la télérelève**, module de VELIZANE : consommation affichée jour par jour, comparaison avec des foyers semblables, alerte en cas de consommation continue pendant la nuit (signe d'une fuite après compteur, chez l'abonné), alerte au dépassement d'un seuil choisi par l'abonné, messages ciblés en période de restriction d'usage. Il suppose de transmettre chaque jour au portail les index de la plateforme de télérelève, au lieu d'un import mensuel. Il concerne les 60 000 abonnés équipés aujourd'hui, et les 160 000 abonnés en 2029. Coût : 80 000 € de mise en place, puis 30 000 € par an. En 2026, 1 200 abonnés ont découvert une fuite après compteur à la réception de leur facture semestrielle, en moyenne quatre mois après son début ; ces fuites sont à l'origine de 1 500 réclamations.

**B. Attentes exprimées**

**Mme Élodie FARGEMONT, directrice de la clientèle** : « Le centre d'appels est saturé. Avec l'assistant, nous pourrions répondre la nuit et le week-end dès cet été. »

**Mme Odile BRESSANDE, présidente du comité des usagers** (instance créée par la régie en 2021, qui réunit des représentants d'associations de consommateurs, de locataires et de quartiers) : « Nous voulons être prévenus d'une fuite avant la facture. Mais beaucoup d'abonnés âgés n'ont pas internet : il faut garder l'accueil et pouvoir toujours parler à un agent, pas à une machine. Et qui verra nos consommations jour par jour ? On saura quand une maison est vide. »

**M. Gilles VAUQUIERS, président du conseil d'administration** : « Après la sécheresse, les élus veulent que chaque abonné puisse suivre sa consommation et soit prévenu à temps d'une restriction. Mais ils ne veulent pas d'un service public déshumanisé, ni de dépenses dont on ne mesure pas l'utilité. »

**Mme Nathalie CORVESSE, responsable de la DSI** : « Un échange quotidien avec la télérelève, sur des échanges avec la facturation qui ne sont pas fiables, c'est fragile. Et si nous empilons les modules d'un seul éditeur, nous ne pourrons plus jamais en changer. »

**C. Les sources de veille aujourd'hui disponibles**

- **Abonnements** : deux revues professionnelles (l'une consacrée aux services d'eau, l'autre aux collectivités), reçues par la direction de l'exploitation et lues selon le temps disponible.
- **Salons** : le congrès annuel de la profession de l'eau, où se rendent le directeur de l'exploitation et la directrice de la clientèle ; aucun compte rendu n'est diffusé.
- **Échanges entre régies** : un réseau informel de régies de l'eau de la région se réunit deux fois par an ; la DSI n'y est pas invitée.
- **Éditeurs** : lettres d'information et démonstrations commerciales de VELIZANE, d'où proviennent les deux propositions.

Personne n'est chargé de la veille ; les informations recueillies ne sont ni conservées dans un espace commun ni présentées à la direction générale.

### Travail à faire

Mme ROCHEVAL veut présenter au conseil d'administration de juin 2027 les conclusions d'un audit du portail des abonnés, les orientations de la relation numérique avec les abonnés et la gouvernance qui la pilotera. Vous mobiliserez pour cela les annexes 1.1, 3.1, 3.2 et 3.3 ainsi que vos connaissances professionnelles.

**3.1 – Démarche de la mission d'audit du portail (2 points)**

a) Après avoir défini l'audit du système d'information, présentez la démarche de la mission d'audit du portail des abonnés : objectifs de performance et de conformité, périmètre et étapes.

b) Représentez sous forme de cartographie le processus « de la souscription au paiement » en cinq étapes, en précisant pour chacune l'acteur et l'application concernés, puis indiquez trois contrôles internes à vérifier, chacun rattaché à une étape.

**3.2 – Appréciation et diagnostic d'audit (3 points)**

a) Définissez les quatre critères d'appréciation du portail (fiabilité, efficacité, sécurité, conformité au RGPD) et rattachez à chacun au moins un constat de l'annexe 3.2.

b) Rédigez le diagnostic d'audit sous forme de tableau (constat, critère, risque, recommandation, priorité) pour quatre constats de l'annexe 3.2, puis justifiez l'ordre de priorité retenu.

**3.3 – Veille technologique et stratégie de la relation numérique (5 points)**

a) Après avoir défini la veille technologique active, proposez un dispositif de veille pour la régie, en précisant ses axes, ses sources, ses outils, ses acteurs, sa fréquence et sa diffusion, au regard de la situation décrite à l'annexe 3.3 C.

b) Analysez l'impact de chacune des deux technologies de l'annexe 3.3 sur le modèle de service de la régie, sous trois angles : la valeur pour les abonnés, les coûts et les risques.

c) Après avoir précisé ce qu'est une stratégie du système d'information alignée sur les objectifs métiers, déduisez-en deux orientations de la stratégie du système d'information de la relation avec les abonnés, alignées sur les priorités du plan « MORVÈZE EAU 2032 », et indiquez pour chacune la suite à donner à l'une des technologies de l'annexe 3.3.

**3.4 – Gouvernance de la relation numérique (3 points)**

a) Analysez, en trois points, les enjeux relationnels entre la DSI, la direction de la clientèle et la direction générale que révèle l'annexe 3.1.

b) Après avoir défini la gouvernance du système d'information, proposez une gouvernance de la relation numérique qui associe les parties prenantes clés (conseil d'administration, comité des usagers, directions concernées, déléguée à la protection des données), en précisant pour chaque instance sa composition, son rôle et sa fréquence.

c) Proposez, pour piloter cette gouvernance, un indicateur de performance et un critère de durabilité, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
