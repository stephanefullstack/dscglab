# DSCG UE 5 — Management des systèmes d'information — Sujet d'entraînement complet n° 14

Durée de l'épreuve : 3 heures – Coefficient : 1

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026.

**Document et matériel autorisés** : Aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Le sujet se présente sous la forme de 3 dossiers indépendants :

| Dossier | Intitulé | Points | Durée conseillée |
|---|---|---:|---|
| DOSSIER 1 | PRÉPARER LA TRANSFORMATION NUMÉRIQUE DE L'ASSISTANCE ET LE PROJET PASSERELLE | 14 points | 1 h 03 |
| DOSSIER 2 | ORGANISER ET EXPLOITER LES DONNÉES DES DOSSIERS ET DU RÉSEAU DE PRESTATAIRES | 13 points | 59 min |
| DOSSIER 3 | RENFORCER LA RÉSILIENCE OPÉRATIONNELLE NUMÉRIQUE ET FIABILISER LES DONNÉES DE DURABILITÉ | 13 points | 58 min |

Le sujet comporte 16 annexes, dont 1 communes aux dossiers.

| Dossier | Annexe | Intitulé |
|---|---|---|
| Tous les dossiers | Annexe 1.1 | Présentation de VALMÉRIS Assistance et chiffres clés |
| DOSSIER 1 | Annexe 1.2 | Ce qui change dans l'assistance (note de veille de la direction de la stratégie et des projets et témoignages recueillis en février 2027) |
|  | Annexe 1.3 | L'IA d'aide aux chargés d'assistance (note de Mme Anne-Laure FERVIGNAC, directrice des systèmes d'information, février 2027) |
|  | Annexe 1.4 | Le projet PASSERELLE (note de M. Bastien ROUVIGNAC, chef de projet, rattaché à la direction de la stratégie et des projets, mars 2027) |
|  | Annexe 1.5 | Le projet de contrat avec l'ESN LOMBREVAL Intégration (extraits commentés par la direction juridique et rappel de la direction des risques et de la conformité, mars 2027) |
| DOSSIER 2 | Annexe 2.1 | Les règles de gestion des dossiers et le modèle actuel (note de M. Damien CORTHELAY, directeur des plateaux, établie avec la direction des systèmes d'information, février 2027) |
|  | Annexe 2.2 | Les échanges de données (constats de Mme Anne-Laure FERVIGNAC, directrice des systèmes d'information, février 2027) |
|  | Annexe 2.3 | Les délais d'arrivée des prestataires (tableaux préparés par la direction des plateaux, février 2027) |
|  | Annexe 2.4 | La proposition de registre commun des missions (note du consortium, reçue en janvier 2027, et objections de la DSI) |
|  | Annexe 2.5 | Le coût du système d'information des dossiers (note de M. Franck SALVEDOUX, directeur administratif et financier, février 2027) |
|  | Annexe 2.6 | Repères (au 31/12/2026) |
| DOSSIER 3 | Annexe 3.1 | La panne du 14 janvier 2027 (récit de M. Damien CORTHELAY, directeur des plateaux, février 2027) |
|  | Annexe 3.2 | Le dispositif de gestion du risque lié aux TIC (constats de Mme Isabelle KERDALOU, directrice des risques et de la conformité, février 2027) |
|  | Annexe 3.3 | L'opérateur de téléphonie en ligne (fiche établie par la direction de la stratégie et des projets, mars 2027, et demande de l'auditrice interne) |
|  | Annexe 3.4 | Les données de durabilité demandées par le groupe (note de Mme Claire HAUDEMARE, directrice de la durabilité du groupe TERRANDÈLE, janvier 2027, et constats de la direction administrative et financière de VALMÉRIS) |
|  | Annexe 3.5 | Repères (au 31/12/2026) |

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

---

## DOSSIER 1 – PRÉPARER LA TRANSFORMATION NUMÉRIQUE DE L'ASSISTANCE ET LE PROJET PASSERELLE (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES DOSSIERS ET DU RÉSEAU DE PRESTATAIRES (13 points)

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

---

## DOSSIER 3 – RENFORCER LA RÉSILIENCE OPÉRATIONNELLE NUMÉRIQUE ET FIABILISER LES DONNÉES DE DURABILITÉ (13 points)

### ANNEXE 3.1 – La panne du 14 janvier 2027 (récit de M. Damien CORTHELAY, directeur des plateaux, février 2027)

**A. La chronologie**

| Heure | Ce qui s'est passé |
|---|---|
| 19 h 50 | Le jeudi 14 janvier 2027, la neige tombe depuis l'après-midi sur l'est et le centre de la France. CALVÉNIS Télécom, l'opérateur qui fournit la téléphonie et la distribution des appels en ligne (annexe 3.3), installe une mise à jour de son logiciel de distribution des appels, sans en avoir averti VALMÉRIS. |
| 20 h | Les postes des chargés des trois plateaux ne reçoivent plus aucun appel. Les appels sont renvoyés vers une messagerie générique : « Nos services sont momentanément indisponibles, laissez votre numéro, nous vous rappellerons. » |
| 20 h 35 | Une superviseure de Limoges, surprise par le silence du plateau, prévient l'astreinte de la DSI. VALMÉRIS ne surveille pas elle-même le fonctionnement de la téléphonie. |
| 21 h | Trente chargés commencent à rappeler, depuis les téléphones mobiles de service, les bénéficiaires qui ont laissé un message. Le logiciel des dossiers n'ouvre un dossier qu'avec l'identifiant de l'appel transmis par la téléphonie : les chargés ouvrent les dossiers sur papier. |
| 21 h 10 | Le service d'assistance de CALVÉNIS répond enfin à la DSI. Croyant d'abord à une attaque par saturation de sa plateforme, l'opérateur isole ses équipements pendant une heure avant de mettre en cause sa mise à jour. |
| 22 h 30 | Le directeur général est informé par un SMS de la DSI. Aucune cellule de crise n'est réunie. |
| 23 h 55 | CALVÉNIS revient à la version précédente de son logiciel. Les appels arrivent de nouveau sur les postes à minuit. |
| 0 h à 6 h | Les chargés ressaisissent dans le logiciel les 1 200 dossiers ouverts sur papier, grâce à une procédure d'exception ouverte par la DSI à minuit. |
| Lendemain, 10 h | Les partenaires sont informés par un courriel de la direction des plateaux. |

**B. Les conséquences, en chiffres ronds**

- Environ 4 000 appels ont été présentés entre 20 h et minuit, contre 1 500 un jeudi soir ordinaire de janvier. 2 500 appelants ont laissé un message ; 1 500 ont raccroché sans laisser de message.
- 1 200 dossiers ont été ouverts sur papier, puis ressaisis ; 40 l'ont été en double ou de façon incomplète.
- Sur les 900 dépannages demandés pendant la panne, 600 ont été réalisés plus de trois heures après le premier appel du bénéficiaire. 150 bénéficiaires immobilisés ont été conduits en taxi ou logés à l'hôtel aux frais de VALMÉRIS : environ 40 k€ de frais supplémentaires.
- Les chargés rappelés et ceux qui ont prolongé leur service ont effectué environ 1 200 heures supplémentaires et de nuit, soit environ 50 k€.
- L'accord conclu avec un assureur partenaire prévoit une pénalité quand moins de 85 % des appels d'une journée sont décrochés : il réclame 60 k€. L'accord avec le loueur de véhicules partenaire prévoit une pénalité pour chaque véhicule immobilisé plus de quatre heures : il réclame 40 k€. Ce loueur a représenté environ 12 M€ du chiffre d'affaires de VALMÉRIS en 2026.
- 700 réclamations ont été reçues dans les quinze jours qui ont suivi, contre 350 environ sur une même période d'hiver.
- La presse régionale s'en est fait l'écho : « Une nuit de neige sans assistance : des automobilistes bloqués sans réponse ».

**C. Ce que nous avions prévu**

Le plan de continuité d'activité date de 2019. Il prévoit l'incendie d'un plateau, qui serait relayé par les deux autres, et la panne du logiciel des dossiers ; il ne prévoit pas la défaillance de l'opérateur de téléphonie, qui sert les trois plateaux à la fois. Il n'a jamais été exercé. VALMÉRIS ne dispose d'aucun second opérateur ni d'aucun renvoi automatique des appels vers un autre fournisseur. Dans le tableur des incidents de la DSI, la panne est inscrite sous le libellé « panne téléphonie, 4 h », sans autre précision.

**D. Les réactions**

**Le directeur de la relation client de l'assureur partenaire** : « Nos assurés nous ont appelés toute la nuit, et nous ne savions rien. Nous avons appris la cause de la panne par la presse. »

**La directrice des opérations du loueur de véhicules partenaire** : « Une panne peut arriver. Mais si cela se reproduit, nous réexaminerons notre accord. »

**M. CORTHELAY** : « Mes équipes ont été remarquables. Mais nous avons improvisé : personne ne savait qui devait décider quoi. »

### ANNEXE 3.2 – Le dispositif de gestion du risque lié aux TIC (constats de Mme Isabelle KERDALOU, directrice des risques et de la conformité, février 2027)

**A. Les constats**

| Domaine | Constat |
|---|---|
| Politique de sécurité | La politique de sécurité du système d'information date de 2018. Rédigée par la DSI, elle n'a jamais été mise à jour et ne s'appuie sur aucune analyse des risques. Elle ne cite ni la téléphonie en ligne, ni l'application mobile des prestataires, ni les interfaces avec les constructeurs, apparues depuis. |
| Conseil d'administration et direction générale | Le conseil d'administration n'a jamais validé de cadre de gestion du risque lié aux TIC et ne reçoit aucun compte rendu sur ces risques ; son comité d'audit et des risques n'examine que les rapports de l'audit interne. Le comité de direction n'a jamais traité le sujet avant la panne du 14 janvier 2027. |
| Responsable de la sécurité des SI | M. Nicolas BRESTAVIN, responsable de la sécurité des systèmes d'information (RSSI), est rattaché à la directrice des systèmes d'information, Mme Anne-Laure FERVIGNAC. Il administre aussi les serveurs et les comptes des utilisateurs ; son budget est une ligne du budget de la DSI. |
| Fonction de gestion des risques | La cartographie des risques de VALMÉRIS comporte une seule ligne « risque informatique », cotée une fois par an par la DSI elle-même. La direction des risques et de la conformité n'exerce aucun contrôle sur les risques liés aux TIC. |
| Incidents | En 2026, 160 incidents ont été inscrits dans un tableur tenu par le support de la DSI, sans classification par gravité, sans critère commun, sans mesure de leur effet sur les plateaux ni recherche de leurs causes. Aucun n'a été signalé au directeur général. |
| Objectifs de reprise | Aucun objectif de reprise n'est fixé par activité. Le contrat de l'infogéreur prévoit un rétablissement « dans les meilleurs délais » ; la DSI applique un objectif unique de 24 heures à toutes les applications, du logiciel des dossiers, utilisé jour et nuit, à la paie. En moyenne, environ 60 dossiers sont ouverts chaque heure, davantage en journée et les soirs d'hiver. |
| Sauvegardes | Le logiciel des dossiers est sauvegardé chaque nuit à 2 h, et la copie est conservée dans le second centre de données de l'infogéreur. Aucune sauvegarde n'a jamais été restaurée pour essai. En 2023, après une erreur de manipulation, la restauration d'une partie de la base a demandé 30 heures. |
| Identités et accès | Les plateaux utilisent 80 comptes génériques (« renfort1 », « renfort2 »…), partagés par les intérimaires et par les chargés en formation. Sur les 120 chargés partis en 2026, 45 ont encore un compte actif. Les droits sont demandés par courriel ; aucune revue des droits n'a eu lieu depuis 2024. |
| Tests | Aucun exercice du plan de continuité depuis 2019, aucun essai de bascule entre les deux centres de données de l'infogéreur, aucun test de résilience. |
| Prestataires | Le registre des accords conclus avec les prestataires de services TIC, établi en 2025, recense 30 accords ; il ne distingue pas ceux dont dépend la continuité des plateaux. |

**B. Le point de vue de Mme KERDALOU**

« La conformité au règlement DORA n'est pas un projet de la DSI. Le premier pilier du règlement, la gestion du risque lié aux TIC, suppose à mes yeux un cadre approuvé et suivi par le conseil d'administration, et un contrôle exercé par une fonction indépendante de ceux qui exploitent le système d'information. Le comité de direction a réservé 600 k€ en 2027 pour la sécurité et la résilience ; le conseil d'administration du 24 juin 2027 attend une proposition. »

### ANNEXE 3.3 – L'opérateur de téléphonie en ligne (fiche établie par la direction de la stratégie et des projets, mars 2027, et demande de l'auditrice interne)

**A. La fiche du prestataire**

| Rubrique | Situation |
|---|---|
| Prestataire | CALVÉNIS Télécom, opérateur de téléphonie et de distribution des appels en ligne |
| Service rendu | réception des appels composés sur les numéros d'assistance des 15 distributeurs ; distribution des appels aux 560 postes des trois plateaux selon le distributeur, la langue et la file d'attente ; messagerie ; enregistrement des conversations, conservées 90 jours (lieu et nature de la panne ou de l'urgence au domicile, immatriculation, composition de la famille) ; statistiques d'appels ; transmission de l'identifiant de chaque appel au logiciel des dossiers |
| Criticité | service critique : sans lui, aucun appel n'est reçu sur aucun plateau |
| Contrat | signé en mars 2021 pour cinq ans, reconduit tacitement en 2026 pour trois ans ; abonnement de 3 200 k€ en 2026, facturé selon le nombre d'appels |
| Engagement de service | disponibilité contractuelle de 99,9 % par mois, soit environ 43 minutes d'indisponibilité admise par mois, mesurée par l'opérateur ; un rapport mensuel de disponibilité est prévu, mais aucun n'a été reçu depuis un an ; VALMÉRIS ne mesure pas elle-même la disponibilité du service |
| Incidents connus | outre la panne du 14 janvier 2027, les plateaux ont relevé en 2026 cinq interruptions de 10 à 40 minutes, que l'opérateur n'a jamais expliquées |
| Hébergement | un seul centre de données, situé en France ; l'offre « deux sites » de l'opérateur n'a pas été souscrite en 2021 |
| Supervision | la supervision de la plateforme, jour et nuit, est confiée par CALVÉNIS à un sous-traitant établi hors de l'Union européenne, qui y accède à distance, y compris aux enregistrements, pour diagnostiquer les anomalies ; VALMÉRIS l'a appris en 2026 par une brochure commerciale |
| Mises à jour | installées par l'opérateur, en soirée, sans préavis à ses clients |
| Sécurité | l'opérateur présente un certificat de conformité à ISO/IEC 27001:2022, valable jusqu'en 2028, dont le périmètre couvre l'hébergement dans son centre de données, mais ni la supervision ni le développement de son logiciel ; il affirme disposer d'un plan de continuité, qu'il n'a jamais communiqué |
| Données personnelles | VALMÉRIS est responsable du traitement des données des appelants ; CALVÉNIS agit comme sous-traitant |
| Audit | le contrat permet à VALMÉRIS de faire auditer, une fois par an et avec un préavis de 30 jours, les moyens affectés au service ; cette faculté n'a jamais été exercée |
| Fin du contrat | le contrat ne prévoit ni la restitution des paramétrages de distribution des appels, des enregistrements et des statistiques, ni l'assistance de l'opérateur en cas de changement de prestataire |

**B. La demande de Mme Laure VENDROUX, auditrice interne**

« Le comité d'audit et des risques m'a demandé d'auditer CALVÉNIS Télécom au deuxième trimestre de 2027. J'y consacrerai 25 jours, avec l'appui d'un auditeur spécialisé dans les systèmes d'information, et je remettrai mon rapport en septembre 2027. Le commercial de CALVÉNIS m'a déjà dit que "le certificat suffit". Aidez-moi à préparer la démarche et les critères de cet audit. »

### ANNEXE 3.4 – Les données de durabilité demandées par le groupe (note de Mme Claire HAUDEMARE, directrice de la durabilité du groupe TERRANDÈLE, janvier 2027, et constats de la direction administrative et financière de VALMÉRIS)

**A. La demande du groupe**

« Le groupe TERRANDÈLE publie depuis l'exercice 2024 un état de durabilité consolidé conforme aux ESRS, qui inclut VALMÉRIS. Son analyse de double matérialité a retenu, pour l'activité d'assistance, le climat (les émissions liées aux interventions, mais aussi les épisodes de neige, de tempête et d'inondation, de plus en plus fréquents, qui font croître les demandes d'assistance et leur coût), le personnel et la relation avec les bénéficiaires. Deux assureurs partenaires demandent désormais l'empreinte des interventions dans leurs consultations. L'état de durabilité du groupe est vérifié par un auditeur de durabilité, qui exprime un avis sur l'état consolidé et peut demander, pour chaque information, comment elle a été obtenue.

Pour l'exercice 2026, VALMÉRIS transmettra avant le 31 mars 2027 :

| Thème | Informations attendues |
|---|---|
| Climat | émissions liées aux kilomètres parcourus par les prestataires pour les missions (dépanneurs, taxis, artisans) et aux véhicules de remplacement ; consommation d'énergie des trois plateaux et des serveurs |
| Personnel | effectif au 31 décembre, départs, heures de formation |
| Bénéficiaires | satisfaction, réclamations |

Chaque information sera accompagnée de sa méthode d'obtention, de ses sources et du nom de la personne qui l'a validée. »

**B. Les constats de la direction administrative et financière (M. Franck SALVEDOUX, février 2027)**

- Les informations sont collectées auprès de cinq services (plateaux, réseau de prestataires, DSI, ressources humaines, services généraux), chacun par un tableur envoyé par courriel ; un salarié de la direction administrative et financière les rassemble dans un tableur de synthèse.
- Les kilomètres des dépanneurs sont estimés à partir de leurs factures : frais de déplacement facturés, divisés par le prix moyen du kilomètre du barème. Les taxis et les artisans ne facturent pas de kilomètres : on retient 20 km par mission.
- L'application mobile des prestataires enregistre la position du prestataire quand il accepte la mission et quand il arrive sur place ; ces données ne sont pas utilisées et sont effacées au bout de 3 mois.
- Les loueurs indiquent le nombre de jours de location des véhicules de remplacement, mais pas le type de motorisation des véhicules.
- L'infogéreur ne fournit aucune donnée sur la consommation des serveurs de VALMÉRIS ; la DSI retient une estimation forfaitaire.
- Les tableurs sont écrasés d'une année à l'autre ; aucune correction n'est tracée.
- Pour 2025, les émissions des interventions ont été transmises en mars 2026 pour 9 000 tCO2e, corrigées en avril à 12 000 tCO2e (les taxis avaient été oubliés), puis en mai à 11 000 tCO2e (des missions avaient été comptées deux fois). Le groupe a dû corriger deux fois son chiffre consolidé. L'auditeur de durabilité du groupe a demandé comment le chiffre initial avait été obtenu : VALMÉRIS n'a pas pu le reconstituer.

**C. Les premières informations de 2026 (provisoires)**

| Information | Valeur 2026 |
|---|---|
| Missions confiées aux prestataires | environ 700 000 |
| Kilomètres parcourus pour les missions (estimation selon la méthode actuelle) | environ 40 millions |
| Émissions liées aux interventions (méthode et facteurs d'émission du groupe) | environ 10 000 tCO2e |
| Véhicules de remplacement | 90 000 locations, 300 000 jours de location |
| Électricité des trois plateaux | 2 400 MWh |
| Électricité des serveurs | non connue |
| Heures de formation | 28 000 |
| Réclamations ; bénéficiaires satisfaits ou très satisfaits | 9 000 réclamations ; 82 % |

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique du secteur financier (DORA) | Règlement d'application directe, sans transposition. Il repose sur cinq piliers : la gestion du risque lié aux technologies de l'information et de la communication (TIC) ; la gestion, la classification et la notification des incidents liés aux TIC ; les tests de résilience opérationnelle numérique ; la gestion des risques liés aux prestataires tiers de services TIC ; le partage d'informations. Pour les prestataires de services TIC, il demande en principe de tenir un registre des accords contractuels, de prévoir des droits d'audit et d'accès et de définir une stratégie de sortie. Il s'applique à VALMÉRIS. | Applicable depuis le 17/01/2025 |
| ISO/IEC 27001:2022 | Norme d'exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques ; 93 mesures en annexe A (dont le contrôle d'accès, la gestion des incidents, la sauvegarde, la continuité et la sécurité des relations avec les fournisseurs). | En vigueur |
| ISO/IEC 27005:2022 | Lignes directrices de gestion des risques liés à la sécurité de l'information : identification, analyse, évaluation et traitement des risques. | En vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI, 2024) | Méthode française d'appréciation et de traitement des risques numériques en cinq ateliers, compatible avec ISO/IEC 27005 ; elle intègre l'écosystème de l'organisation, dont ses prestataires. | Version 1.5 publiée en 2024 |
| ISO 22301:2019 | Norme d'exigences d'un système de management de la continuité d'activité : analyse d'impact sur l'activité, stratégies et plans de continuité, exercices et amélioration. | En vigueur |
| COBIT 2019 (ISACA) | Cadre de gouvernance et de management de l'information et des technologies : 40 objectifs de gouvernance et de management, dont la gestion des fournisseurs, des services et de la continuité. | Version 2019 |
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Le responsable du traitement ne fait appel qu'à des sous-traitants présentant des garanties suffisantes, liés par un contrat ; un sous-traitant ne recrute un autre sous-traitant qu'avec l'autorisation écrite préalable du responsable du traitement ; les transferts de données hors de l'Union européenne sont soumis à des garanties. | Applicable depuis le 25/05/2018 |
| Directive (UE) 2022/2464 (CSRD), modifiée par les directives (UE) 2025/794 et 2026/470, et normes européennes d'information en matière de durabilité (ESRS) | L'état de durabilité présente les impacts de l'entreprise sur les personnes et l'environnement et les effets des enjeux de durabilité sur sa situation (double matérialité) ; un groupe l'établit sur une base consolidée, en y intégrant ses filiales. Les ESRS comprennent des normes transversales et des normes thématiques (environnement, social, gouvernance). L'état de durabilité est vérifié par un auditeur de durabilité. Le groupe TERRANDÈLE y est soumis : cela n'est pas à déterminer. | Directive 2026/470 en vigueur depuis le 18/03/2026 ; ESRS révisées applicables aux exercices ouverts à compter du 01/01/2027, au choix pour 2026 |
| GHG Protocol (WRI et WBCSD) | Cadre de mesure et de déclaration des émissions de gaz à effet de serre en trois périmètres : émissions directes (scope 1), émissions liées à l'énergie achetée (scope 2), autres émissions indirectes de la chaîne de valeur (scope 3). | Édition révisée (2004) ; norme scope 3 (2011) |

Il n'est demandé aucune analyse juridique.

### Travail à faire

Un soir de neige, la panne de l'opérateur de téléphonie a privé les trois plateaux de tout appel pendant quatre heures ; le dispositif de gestion du risque lié aux TIC est loin de ce qu'attend le règlement DORA, et le groupe TERRANDÈLE a dû corriger deux fois les données de durabilité transmises par VALMÉRIS. M. MARVÉJOL vous demande de tirer les leçons de la panne, de proposer le cadre de gestion du risque lié aux TIC qui sera présenté au conseil d'administration du 24 juin 2027, de préparer avec l'auditrice interne l'audit de l'opérateur et de fiabiliser les données de durabilité destinées au groupe. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – L'analyse d'impact de la panne du 14 janvier 2027 (2,5 points)**

a) Après avoir présenté la typologie des risques liés aux systèmes d'information (cybermenaces, défaillances opérationnelles, risques réglementaires et métiers), classez dans cette typologie quatre causes ou facteurs d'aggravation de la panne relatés dans l'annexe 3.1, en couvrant les trois catégories.

b) Après avoir défini l'analyse d'impact sur l'activité, évaluez les effets de la panne sur les processus de VALMÉRIS, sur la continuité du service aux bénéficiaires, sur la relation avec les partenaires et sur les états financiers (postes exposés, en principe), puis tirez-en deux enseignements pour le plan de continuité d'activité. Aucune évaluation chiffrée ni aucun traitement comptable des pénalités ne sont attendus.

**3.2 – Le cadre de gestion du risque lié aux TIC (5 points)**

a) Après avoir situé la gestion du risque lié aux TIC parmi les cinq piliers du règlement DORA (annexe 3.5) et défini une politique de sécurité du système d'information fondée sur l'analyse des risques, proposez la démarche qui remplacera la politique de 2018 : l'appréciation des risques, en précisant la nature du référentiel de l'annexe 3.5 sur lequel vous vous appuyez, puis le contenu de la nouvelle politique.

b) Proposez la répartition des rôles et des responsabilités de la gestion du risque lié aux TIC entre le conseil d'administration, le directeur général, la direction des risques et de la conformité, le RSSI, la DSI et les prestataires, puis justifiez le positionnement que vous recommandez pour le RSSI.

c) Proposez quatre dispositifs de surveillance et de résilience répondant aux constats de l'annexe 3.2, portant respectivement sur la gestion des identités et des accès, sur le PCA et le PRA (avec un RTO et un RPO justifiés pour deux activités critiques), sur la classification et la remontée des incidents, et sur le programme de tests de résilience. Aucun délai de notification, aucun test technique de sécurité ni aucun paramétrage ne sont attendus.

d) Hiérarchisez quatre mesures à engager en 2027, en justifiant le rang de la première.

**3.3 – L'audit de l'opérateur de téléphonie (2 points)**

a) Présentez la démarche de l'audit de CALVÉNIS Télécom que préparera Mme VENDROUX : ses objectifs, la cartographie du service rendu, de l'appel du bénéficiaire à l'ouverture du dossier, et les principaux risques à couvrir.

b) Proposez quatre critères de performance et de conformité de cet audit, portant respectivement sur la disponibilité, la sécurité, la localisation et la confidentialité des données, et la réversibilité ; pour chacun, indiquez un contrôle à examiner et une preuve à demander à l'opérateur. Aucune analyse juridique du contrat n'est attendue.

**3.4 – Les données de durabilité destinées au groupe (3,5 points)**

a) Situez la demande du groupe TERRANDÈLE dans le cadre de la CSRD et des ESRS (annexe 3.5) : l'état de durabilité consolidé et la place qu'y tient VALMÉRIS, la double matérialité, illustrée par deux éléments de l'annexe 3.4, et la vérification par un auditeur de durabilité. Aucun calcul d'assujettissement n'est attendu, ni aucune démarche de l'auditeur.

b) Proposez le rôle du système d'information dans la collecte et la fiabilité des données de durabilité de VALMÉRIS, en quatre mesures portant respectivement sur les sources et la collecte automatisée, le référentiel des indicateurs, les contrôles et la piste d'audit, et la gouvernance des données ; reliez chacune à un constat de l'annexe 3.4.

c) Proposez deux indicateurs environnementaux, l'un mesurant l'empreinte des interventions, l'autre celle du système d'information de VALMÉRIS, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Aucun calcul d'empreinte n'est attendu.
