# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 40

**DOSSIER 1 – PRÉPARER LA TRANSFORMATION NUMÉRIQUE DE L'ASSISTANCE ET LE PROJET PASSERELLE (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 1.2 – Ce qui change dans l'assistance (note de veille de la direction de la stratégie et des projets et témoignages recueillis en février 2027)

**A. Les évolutions relevées**

1. **Les véhicules connectés.** En 2026, VALMÉRIS a reçu environ 30 000 alertes des véhicules connectés de ses deux constructeurs partenaires, soit à peu près un dossier automobile sur dix. Ces alertes arrivent d'abord chez le constructeur, qui décide de les transmettre ou non. Depuis 2025, l'application des véhicules des deux constructeurs comporte un bouton « assistance » : le conducteur y déclare sa panne sans appeler. L'autre constructeur partenaire, qui n'est pas Automobiles VIRANDOR (témoignage en B), a créé en 2026, dans un autre pays européen, sa propre filiale d'assistance, qui traite les pannes de ses clients sans assisteur.
2. **Les détecteurs de fuite d'eau.** Un assureur partenaire équipe en 2027, à titre d'essai, 20 000 logements de ses clients de détecteurs de fuite connectés. Il demande si VALMÉRIS peut recevoir les alertes et envoyer un plombier avant que le dégât des eaux ne s'étende.
3. **Les attentes des bénéficiaires.** Dans l'enquête de satisfaction de 2026, huit réclamations sur dix portent sur l'absence de nouvelles pendant l'attente du prestataire. Beaucoup de bénéficiaires rappellent le plateau pendant cette attente : « Pour un colis, je vois le livreur arriver sur une carte ; pour ma voiture en panne sur l'autoroute, je ne sais rien. » En 2026, 10 % des dossiers ont été ouverts en ligne (application ou site d'un partenaire), contre 2 % en 2022.
4. **Les plateformes de mise en relation avec des artisans.** Trois plateformes en ligne proposent aux particuliers un plombier ou un serrurier en moins de deux heures, payé directement par le client. Environ 300 des 3 400 prestataires agréés de VALMÉRIS y sont aussi inscrits ; un assureur partenaire étudie une offre de l'une d'elles pour ses propres clients.
5. **Les assistants conversationnels et la transcription automatique.** Deux assisteurs concurrents ouvrent désormais les demandes simples (crevaison, perte de clés) par un assistant conversationnel accessible jour et nuit ; un autre fait transcrire et résumer automatiquement les appels.
6. **Le recrutement des chargés d'assistance.** En 2026, un appel sur cinq a été reçu entre 22 h et 7 h. Sur les 560 chargés d'assistance et superviseurs, 120 ont quitté l'entreprise en 2026 ; 25 postes de nuit restent vacants. La formation initiale d'un chargé dure huit semaines.

**B. Témoignages**

**M. Hugo BRÉCHANDOT, directeur des services connectés d'Automobiles VIRANDOR, constructeur partenaire** : « En octobre 2028, nous choisirons, pour cinq ans, un seul assisteur pour nos clients français. Le candidat retenu devra recevoir nos alertes en temps réel dans son logiciel de gestion des dossiers, ouvrir le dossier sans appel du conducteur et nous renvoyer l'heure d'arrivée du dépanneur, et cela sur tous ses plateaux dès le 30 juin 2028. Aujourd'hui, vous recevez nos alertes par courriel automatique et vos chargés les ressaisissent. » VIRANDOR a représenté en 2026 environ 50 000 dossiers et 30 M€ du chiffre d'affaires de VALMÉRIS.

**M. Damien CORTHELAY, directeur des plateaux** : « Notre métier, c'est la voix humaine au moment où tout va mal. Mais nos chargés passent la moitié de l'appel à saisir, et la nuit nous manquons de monde. »

**Mme Sophie GALANDRET, directrice du réseau de prestataires** : « Les meilleurs dépanneurs reçoivent des missions de trois assisteurs et de deux plateformes. Ils choisissent celui qui leur donne les missions les plus claires et les paie le plus vite. »

**Le représentant d'un assureur partenaire** : « Nous ne voulons plus seulement réparer : nous voulons éviter le sinistre. Si VALMÉRIS ne sait pas traiter nos alertes, nous trouverons quelqu'un qui le sait. »

### ANNEXE 1.3 – L'IA d'aide aux chargés d'assistance (note de Mme Anne-Laure FERVIGNAC, directrice des systèmes d'information, février 2027)

**A. Le fonctionnement de l'outil pilote**

D'octobre à décembre 2026, 20 chargés du plateau de Valence ont utilisé un outil d'aide sur environ 6 000 appels. L'outil :
- **transcrit** l'appel pendant la conversation et en **rédige un résumé**, versé au dossier : un modèle de langage fourni par un éditeur, utilisé sous forme de service en ligne hébergé dans l'Union européenne, produit ce texte ;
- **qualifie** le dossier : il propose le type de panne ou d'événement, le lieu et la garantie applicable ;
- **propose les trois prestataires** jugés les plus adaptés parmi les plus proches.

La qualification et la proposition de prestataires reposent sur un modèle entraîné par la DSI et un prestataire sur environ 3 millions de dossiers des années 2018 à 2025 : le modèle a appris, à partir de ces dossiers, quelle qualification et quels prestataires avaient été retenus dans des situations comparables. Le chargé peut modifier chaque proposition avant de la valider.

**B. Les résultats du pilote**

| Mesure | Sans l'outil (même plateau, automne 2025) | Avec l'outil (pilote, automne 2026) |
|---|---|---|
| Temps moyen de traitement d'un appel | 10 minutes | 8 minutes |
| dont saisie du dossier après l'appel | 4 minutes | 1 minute |
| Qualification proposée erronée (type de panne, lieu ou garantie) | — | 1 dossier sur 10 |
| Erreurs de qualification restées dans le dossier validé | 2 % des dossiers | 3 % des dossiers |
| Propositions de prestataires inadaptées (dépanneur fermé la nuit, non équipé pour le véhicule, hors de sa zone) | — | 15 % des propositions ; 40 % pour les véhicules électriques |
| Résumés contenant une information qui n'a pas été dite pendant l'appel | — | 4 % des résumés, davantage pour les appels passés depuis le bord d'une route bruyante |

Les véhicules électriques représentaient 2 % des dossiers d'entraînement et 12 % des dossiers automobiles du pilote. Les règles de codage des garanties ont changé en 2021.

**C. Les réactions des chargés et la proposition de la DSI**

**Une chargée expérimentée du plateau de Valence** : « Le résumé me fait gagner un temps fou. Mais je relis tout : une fois, il a écrit que la voiture était sur l'autoroute alors que la cliente était sur un parking. »

**Un chargé recruté en 2026** : « La nuit, quand les appels s'enchaînent, je valide les trois dépanneurs proposés sans regarder. C'est l'outil qui sait. »

**Une superviseure du plateau de Valence** : « Personne ne nous a dit qui corrige l'outil quand il se trompe, ni comment on lui signale ses erreurs. Les plateaux de Limoges et de Metz n'ont jamais vu l'outil. »

**Proposition de Mme FERVIGNAC** : « Les gains sont nets : je propose d'étendre l'outil, tel quel, aux trois plateaux en janvier 2028. »

**D. Repère donné par la direction des risques et de la conformité (au 31/12/2026)**

Le règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744, suit une approche par les risques. Depuis le 2 février 2025, les fournisseurs et les déployeurs de systèmes d'IA (organisations qui les utilisent sous leur propre autorité) prennent des mesures pour favoriser la maîtrise de l'IA de leur personnel (article 4, dans sa rédaction issue du règlement (UE) 2026/1744, en vigueur depuis le 27 juillet 2026). La situation de l'outil au regard de ce règlement a été examinée par la direction des risques et de la conformité ; elle n'est pas à analyser.

### ANNEXE 1.4 – Le projet PASSERELLE (note de M. Bastien ROUVIGNAC, chef de projet, rattaché à la direction de la stratégie et des projets, mars 2027)

**A. Les tâches**

Le projet commence la première semaine d'avril 2027. Pour simplifier, on compte quatre semaines par mois : les semaines 1 à 4 correspondent à avril 2027, les semaines 5 à 8 à mai 2027, et ainsi de suite (semaines 33 à 36 : décembre 2027 ; semaines 37 à 40 : janvier 2028 ; semaines 57 à 60 : juin 2028). Une tâche commencée n'est pas interrompue.

| Tâche | Contenu | Durée | Antériorités | Ressources | Charge (jours) |
|---|---|---|---|---|---|
| A | Cadrage et spécifications : exigences des plateaux, des partenaires et du réseau, adaptation de la solution retenue | 16 semaines | — | DSI, équipe métier des plateaux | DSI 400 ; métier 300 |
| B | Paramétrage de la solution (dossiers, garanties, règles de choix des prestataires) | 10 semaines | A | ESN, DSI, équipe métier | ESN 1 200 ; DSI 200 ; métier 300 |
| C | Reprise des données (dossiers en cours, contrats et bénéficiaires couverts, prestataires) | 10 semaines | A | ESN, DSI | ESN 400 ; DSI 400 |
| D | Interfaces avec les partenaires, les deux constructeurs, l'application des prestataires et la téléphonie | 14 semaines | A | ESN, DSI | ESN 1 400 ; DSI 400 |
| E | Recette | 6 semaines | B, C, D | superviseurs, ESN, DSI | ESN 300 ; DSI 200 ; métier 600 |
| F | Formation des 560 chargés d'assistance et superviseurs | 8 semaines | B | superviseurs, ESN | ESN 100 ; métier 600 |
| G | Bascule des trois plateaux, l'un après l'autre | 6 semaines | E, F | DSI, ESN, superviseurs | ESN 200 ; DSI 400 ; métier 200 |

**B. Les ressources et les contraintes**

- Trente superviseurs, désignés comme utilisateurs clés, conduisent la recette et forment les chargés : ils ne peuvent pas mener les deux tâches en même temps.
- La recette de la solution précède normalement la formation, afin de former les chargés sur la version recettée.
- Échéance : Automobiles VIRANDOR exige que ses alertes soient reçues dans le nouveau logiciel, sur tous les plateaux, au plus tard le 30 juin 2028 (fin de la semaine 60) ; l'ancien logiciel doit être arrêté avant la fin de 2028.

**C. Les coûts (en k€)**

| Poste | Montant |
|---|---|
| Intégration par l'ESN au forfait : 3 600 jours à 500 € | 1 800 |
| Temps de la DSI : 2 000 jours valorisés à 400 € | 800 |
| Temps de l'équipe métier des plateaux : 2 000 jours valorisés à 300 € | 600 |
| Abonnement à la solution pendant le projet | 600 |
| Réserve pour aléas | 200 |
| **Total** | **4 000** |

**D. Les leviers étudiés par le chef de projet**

- **Levier 1** : la tâche A comprend six semaines de spécifications détaillées de l'ensemble des écrans et des règles, voulues par la DSI. Spécifier seulement les exigences clés et les écarts avec la solution retenue ramènerait la tâche A à 12 semaines ; le paramétrage risquerait alors de demander davantage d'ajustements en recette.
- **Levier 2** : l'ESN propose de ramener la tâche D de 14 à 10 semaines en ajoutant une équipe, soit 300 jours supplémentaires, facturés 150 k€.

**E. Les tensions relatées**

**Mme Anne-Laure FERVIGNAC, DSI** : « On ne paramètre rien avant d'avoir tout spécifié. La dernière fois qu'on a fait vite, en 2008, on l'a payé dix ans. »

**M. Damien CORTHELAY, directeur des plateaux** : « De décembre à février, c'est la saison d'hiver : batteries à plat, neige, accidents. Je ne libérerai aucun superviseur pendant ces trois mois. Personne ne m'a demandé mon avis sur le calendrier. »

**Le responsable informatique d'un assureur partenaire**, qui parle aussi au nom d'un second partenaire : « Nous voulons valider les nouvelles interfaces avant toute bascule. Nous l'avons appris par une lettre circulaire. »

**M. Bastien ROUVIGNAC, chef de projet** : « Chaque direction me donne ses priorités, mais aucun comité ne tranche. Le directeur général n'a pas encore réuni les directeurs sur le projet. »

### ANNEXE 1.5 – Le projet de contrat avec l'ESN LOMBREVAL Intégration (extraits commentés par la direction juridique et rappel de la direction des risques et de la conformité, mars 2027)

**A. L'objet du contrat**

À l'issue d'une consultation close en février 2027, VALMÉRIS a retenu une solution du marché et l'ESN LOMBREVAL Intégration, qui l'intégrera au forfait (1 800 k€), puis en assurera la maintenance applicative corrective et évolutive pendant trois ans, pour 300 k€ par an.

**B. Extraits du projet de contrat et commentaires de la direction juridique**

| Article | Extrait du projet rédigé par l'ESN | Commentaire de la direction juridique |
|---|---|---|
| 6 – Niveaux de service | « Les anomalies bloquantes sont prises en charge dans un délai de quatre heures ouvrées, du lundi au vendredi, de 8 h à 18 h. » | Aucun engagement la nuit, le week-end ni les jours fériés, alors que les plateaux fonctionnent jour et nuit. Aucun délai de rétablissement, seulement un délai de prise en charge. |
| 7 – Pénalités | « Chaque manquement mesuré donne lieu à une pénalité de 1 % de la redevance annuelle de maintenance, dans la limite de 3 % de cette redevance par an. » | Le plafond représente 9 k€ par an. La mesure des manquements repose sur le seul rapport mensuel de l'ESN. |
| 9 – Sous-traitance | « Le prestataire peut confier tout ou partie des travaux à ses filiales et partenaires, en France ou à l'étranger. » | Aucune information ni autorisation préalable de VALMÉRIS ; aucun lieu de traitement des données indiqué. |
| 11 – Données | « Le client garantit la conformité des données qu'il confie au prestataire. » Pour la reprise et la recette, l'ESN recevra une copie des dossiers des bénéficiaires (nom, adresse, position géolocalisée, immatriculation, contrat). | Aucune clause de sous-traitance des données personnelles : ni instructions documentées, ni mesures de sécurité, ni sort des données en fin de contrat. |
| 14 – Fin du contrat | « À l'échéance, le prestataire remet au client la documentation de la solution. » | Aucune réversibilité : ni restitution des données et des paramétrages dans un format exploitable, ni assistance au transfert vers un autre prestataire. Les interfaces développées pour VALMÉRIS restent la propriété de l'ESN. |
| — | — | Aucune clause d'audit ni d'accès aux locaux, aux systèmes et aux documents de l'ESN. |
| — | — | Aucune instance de suivi du contrat n'est prévue ; l'ESN propose « un point annuel ». |

**C. Rappel de Mme Isabelle KERDALOU, directrice des risques et de la conformité (au 31/12/2026)**

« Le règlement (UE) 2022/2554 (DORA) s'applique à VALMÉRIS depuis le 17 janvier 2025, sans transposition. Il repose sur cinq piliers : la gestion du risque lié aux TIC, la gestion des incidents liés aux TIC, les tests de résilience opérationnelle numérique, la gestion des risques liés aux prestataires tiers de services TIC et le partage d'informations. Pour les prestataires de services TIC, il demande en principe de tenir un registre des accords contractuels, de prévoir dans les contrats des droits d'audit et d'accès et de définir une stratégie de sortie. La future solution de gestion des dossiers, que l'ESN intégrera puis maintiendra, soutient l'activité principale de VALMÉRIS. »

### Travail à faire

« Assister 2030 » veut déclencher l'assistance sans appel et informer les bénéficiaires en temps réel, alors que les constructeurs, les objets connectés et les plateformes bousculent le métier d'assisteur ; le projet PASSERELLE doit remplacer le logiciel de gestion des dossiers avant la fin de 2028. M. MARVÉJOL vous demande d'analyser ce qui change pour VALMÉRIS et d'en déduire les orientations de la stratégie du système d'information, d'apprécier l'extension de l'IA d'aide aux chargés, de planifier et d'organiser le projet PASSERELLE, et de sécuriser le contrat avec l'ESN. Vous mobiliserez pour cela les annexes 1.1 à 1.5 ainsi que vos connaissances professionnelles.

**1.1 – Les effets des évolutions de l'assistance et la stratégie du système d'information (4 points)**

a) Après avoir défini le modèle économique d'une entreprise, analysez les effets de trois évolutions de votre choix, tirées de l'annexe 1.2, sur le modèle économique de VALMÉRIS : sa place entre les distributeurs, les bénéficiaires et les prestataires, le risque de désintermédiation et les nouveaux services possibles. Il n'est demandé aucun dispositif de veille.

b) Après avoir défini la stratégie du système d'information, déduisez de votre analyse trois orientations de la stratégie du système d'information au service d'« Assister 2030 », chacune justifiée par une évolution de l'annexe 1.2 et rattachée à un objectif du plan. Il n'est demandé ni schéma directeur, ni feuille de route, ni analyse selon un modèle d'alignement nommé.

**1.2 – L'IA d'aide aux chargés d'assistance (2 points)**

a) Expliquez le fonctionnement de l'outil pilote décrit dans l'annexe 1.3, en distinguant la transcription et le résumé de l'appel, d'une part, la qualification et la proposition de prestataires, d'autre part. Relevez deux limites de l'outil, dont une qui tient aux données d'entraînement.

b) Appréciez la proposition de la DSI d'étendre l'outil « tel quel » aux trois plateaux, en présentant deux conditions de cette extension, dont le contrôle humain. Aucune analyse juridique ni aucune classification de l'outil au regard du règlement sur l'intelligence artificielle ne sont attendues.

**1.3 – La planification et le pilotage du projet PASSERELLE (5 points)**

a) À partir de l'annexe 1.4 A, présentez, sous forme de diagramme de Gantt ou de tableau, les dates au plus tôt de chaque tâche, la durée du projet et son chemin critique, sans tenir compte des superviseurs. Montrez ensuite l'effet, sur la durée du projet, de la contrainte qui pèse sur les superviseurs (annexe 1.4 B), et justifiez l'ordre que vous retenez entre la recette et la formation.

b) Appréciez la possibilité de respecter l'échéance du 30 juin 2028 si le directeur des plateaux maintient son refus de libérer les superviseurs de décembre à février (annexe 1.4 E). Proposez ensuite un arbitrage entre délai, coût et qualité, en vous appuyant sur les leviers de l'annexe 1.4 D et sur les enjeux de l'annexe 1.2.

c) Proposez l'organisation du pilotage du projet qui répond aux tensions relatées dans l'annexe 1.4 E : le sponsor, le comité de pilotage (composition, fréquence, décisions), le rôle des plateaux, de la DSI, de l'ESN et des partenaires, et deux règles d'arbitrage.

**1.4 – Le contrat avec l'ESN et la gouvernance de la relation (3 points)**

a) Relevez quatre faiblesses du projet de contrat de l'annexe 1.5 et proposez, pour chacune, la clause qui sécurise la relation, en tenant compte du rappel de la direction des risques et de la conformité. Aucune analyse juridique au-delà des clauses ni aucun registre à remplir ne sont attendus.

b) Proposez la gouvernance de la relation avec LOMBREVAL Intégration pendant la maintenance : les instances (participants, fréquence, objet) et un indicateur de suivi, précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
