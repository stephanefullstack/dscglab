# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 33

**DOSSIER 3 – SÉCURISER L'ACCÈS AUX DONNÉES, PRÉPARER UNE CRISE CYBER, RENDRE LE NUMÉRIQUE PLUS RESPONSABLE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 3.1 – Les habilitations aux dossiers des personnes accompagnées (note de Mme Agnès PELLEGRAIN, déléguée à la protection des données, et constats d'avril 2027)

**A. Les comptes des trois logiciels de dossier**

J'ai rapproché, le 31 mars 2027, la liste des comptes des trois logiciels de la liste des salariés présents dans le progiciel de paie.

| Logiciel de l'ancienne association | Établissements et services équipés | Comptes actifs | dont comptes nominatifs de salariés présents | dont comptes partagés par une unité | dont comptes de salariés qui ont quitté la Fondation | dont comptes d'éditeur ou d'administration | Dernière revue des droits |
|---|---|---|---|---|---|---|---|
| GERVELLE | 18 | 900 | 760 | 40 | 90 | 10 | 2018 |
| MIRANDELLE | 9 | 450 | 375 | 20 | 50 | 5 | jamais |
| LUMERANDE | 5 | 250 | 215 | 10 | 20 | 5 | 2017 |
| **Total** | **32** | **1 600** | **1 350** | **70** | **160** | **20** | — |

- **Comptes partagés** : les 70 comptes d'unité (par exemple « nuit-foyer-3 ») servent sur les postes des salles de transmissions, surtout la nuit et le week-end. Dans 10 des 20 unités que j'ai visitées, le mot de passe était affiché près du poste.
- **Remplaçants et intérimaires** : environ 150 remplaçants et intérimaires différents travaillent chaque mois dans les établissements. L'ouverture d'un compte demande en moyenne 10 jours (courriel du directeur d'établissement à la DSI, sans formulaire). Pour quelques jours de remplacement, le cadre de l'unité remet au remplaçant l'identifiant et le mot de passe d'un titulaire absent, ou le fait travailler sur le compte de l'unité.
- **Salariés partis** : sur les 160 comptes de salariés qui ont quitté la Fondation, 30 ont été utilisés après la date de départ, le plus souvent dans l'unité où le salarié travaillait. La direction des ressources humaines enregistre environ 250 départs et 300 arrivées par an dans le progiciel de paie ; elle n'en informe pas la DSI. La fermeture d'un compte dépend de la demande du directeur d'établissement.
- **Mobilités** : environ 100 salariés changent d'établissement chaque année. Un nouveau compte leur est ouvert, l'ancien n'est pas fermé : 60 salariés ont ainsi accès aux dossiers de deux établissements ou plus.
- **Droits par établissement** : dans les trois logiciels, un compte ouvert dans un établissement voit tous les dossiers de cet établissement, y compris les comptes rendus des médecins et des psychologues. Dans plusieurs foyers, les agents de cuisine et d'entretien ont un compte pour consulter les régimes alimentaires : ils voient l'ensemble du dossier. Seul le logiciel de l'ancienne association GERVELLE distingue un profil « soignant ».
- **Comptes d'éditeur et d'administration** : chaque éditeur dispose d'un accès permanent à distance pour la maintenance ; les mots de passe de ces comptes n'ont pas changé depuis l'installation des logiciels.
- **Traces** : seul le logiciel de l'ancienne association GERVELLE enregistre les consultations des dossiers (journal conservé trois mois, que personne ne consulte) ; les deux autres n'enregistrent que les modifications.
- **Registre** : le registre des activités de traitement de la Fondation, établi en 2020, ne précise pas quelles catégories de professionnels accèdent à quelles données.
- En janvier 2027, une famille s'est plainte qu'un ancien éducateur, parti en 2025 dans une autre organisation, connaissait des éléments récents du dossier de sa fille. Rien n'a pu être établi, faute de traces.

**B. Les droits prévus dans le dossier unique**

- Le dossier unique doit être utilisé par environ 1 600 professionnels. Il permet de définir des profils de droits par métier et par établissement, d'activer l'authentification à deux facteurs et d'enregistrer toutes les consultations ; aucun profil n'est encore défini. Pour gagner du temps, l'équipe projet propose de « reprendre les droits actuels des trois logiciels ».
- Environ 1 500 familles et représentants légaux pourront consulter une partie du dossier de leur proche, selon des droits définis pour chaque personne. Personne n'a encore décidé qui fixe ces droits, ni comment ils sont modifiés quand la situation de la personne ou de sa famille change, ou quand un adulte accompagné ne souhaite pas que sa famille lise certains écrits.

**C. La demande du conseil d'administration et les témoignages**

- **M. Henri LABASTROU, président du conseil d'administration** : « Avant d'ouvrir le dossier unique à 1 600 professionnels et à 1 500 familles, le conseil veut savoir qui voit quoi, et pourquoi. Je demande un audit des habilitations, avec des conclusions présentées au conseil de septembre 2027, avant la mise en service du dossier unique prévue à partir de la fin de l'année. »
- **Mme Nathalie BRÉCHEVAL, directrice générale**, vous confie cet audit, à mener en juin et juillet 2027. Vous disposerez de l'appui de la déléguée à la protection des données ; un administrateur de la DSI fournira les extractions des comptes et des traces.
- **Mme Sandrine QUILLEVÈRE, directrice d'une maison d'accueil spécialisée** : « La nuit, un professionnel remplaçant ne peut pas attendre dix jours un compte. Si on lui ferme l'accès, il travaillera sans les consignes d'accompagnement des résidents. »
- **M. Laurent TRÉVENEC, directeur des systèmes d'information** : « Je ferme les comptes quand on me prévient ; personne ne me prévient. »
- **Mme Valérie OSMONDE, directrice des ressources humaines** : « La paie sait qui part. Mais ce n'est pas à mon service de gérer les comptes informatiques. »

### ANNEXE 3.2 – Une attaque dans une association voisine et la situation de la Fondation (note de M. Laurent TRÉVENEC, directeur des systèmes d'information, avril 2027)

**A. Ce qui est arrivé à l'association TERNAVIELLE**

L'association TERNAVIELLE gère 15 établissements et services pour des personnes en situation de handicap dans un département voisin. Son directeur général nous a présenté son retour d'expérience en mars 2027.

| Moment | Faits |
|---|---|
| Mi-janvier 2027 | Un salarié répond à un faux courriel aux couleurs de la messagerie et y saisit son identifiant et son mot de passe. |
| Samedi 6 février 2027, 2 h | Un rançongiciel chiffre les serveurs de l'association, dont celui du logiciel de dossier des personnes accompagnées, ainsi que les disques de sauvegarde, reliés en permanence au réseau. Un message de rançon s'affiche. |
| Nuit du samedi au dimanche | Dans quatre foyers, les professionnels de nuit ne peuvent plus consulter les consignes d'accompagnement (régimes, allergies, traitements à donner). Le directeur d'astreinte ne sait pas qui appeler : le prestataire informatique est fermé le week-end, aucune liste de contacts n'existe. |
| Lundi 8 février | Le directeur général est informé à 9 h. Une cellule de crise est improvisée ; personne ne sait qui doit décider de couper les liaisons avec les établissements ni de répondre à la demande de rançon. |
| Vendredi 12 février | La plainte est déposée, six jours après la découverte de l'attaque. La violation de données est notifiée à l'autorité de contrôle le cinquième jour. |
| Mi-février | Les attaquants publient sur un site environ 2 000 dossiers (identité, diagnostics, comptes rendus). Plusieurs familles l'apprennent par la presse locale, avant tout courrier de l'association. |
| Février et mars | Les dossiers restent indisponibles trois semaines. Les équipes reviennent au papier : consignes reconstituées de mémoire et à partir d'anciennes impressions, transmissions écrites à la main puis ressaisies. |

L'association avait souscrit une assurance contre les risques cyber ; l'assureur a refusé d'indemniser les pertes et les frais engagés, la plainte ayant été déposée hors délai ; seule l'assistance prévue au contrat a été fournie. Le coût de l'attaque est estimé à 600 k€ (prestataire spécialisé dans la réponse aux incidents, matériels, heures supplémentaires), sans compter la perte de confiance des familles.

**B. La situation de la Fondation VERLANDRE**

- **Sauvegardes** : les serveurs de la salle du siège sont sauvegardés chaque nuit sur des disques installés dans la même salle et reliés en permanence au réseau ; une copie mensuelle est emportée au domicile d'un administrateur. Aucune restauration complète n'a jamais été essayée.
- **Crise** : il n'existe aucune procédure de crise écrite ni aucune liste à jour des contacts (éditeurs, prestataires, assureur). Un samedi soir de novembre 2026, une panne de la salle de serveurs a privé pendant 6 heures les unités de nuit de l'accès aux dossiers ; personne n'a su qui prévenir.
- **Astreinte** : chaque nuit et chaque week-end, un directeur d'établissement par pôle est d'astreinte pour les événements graves (accident, fugue, incendie). La procédure d'astreinte ne prévoit rien pour une panne ou une attaque informatique. La DSI n'assure aucune permanence la nuit ni le week-end.
- **Rôles** : la sécurité est assurée, en plus de leurs autres tâches, par les trois administrateurs des infrastructures et du réseau. Il n'existe ni politique de sécurité écrite ni charte informatique commune ; la charte de l'ancienne association GERVELLE date de 2015. Personne n'est désigné pour décider en cas d'attaque.
- **Hameçonnage** : en février 2027, un faux courriel aux couleurs de la messagerie a recueilli les identifiants de 25 salariés ; la DSI l'a appris par hasard. L'authentification à deux facteurs n'est activée que pour les comptes de la DSI.
- **Assurance** : la Fondation négocie un contrat d'assurance cyber (plafond de 2 000 k€, franchise de 50 k€). Avant de signer, l'assureur demande l'authentification à deux facteurs des accès à distance, des sauvegardes déconnectées du réseau dont la restauration a été essayée, et une procédure écrite de gestion de crise.
- **Familles** : les familles sont informées par courrier et par téléphone ; aucun message n'est prévu en cas d'incident touchant les données.

**C. Témoignages**

- **Mme Nathalie BRÉCHEVAL, directrice générale** : « Je ne veux pas découvrir un samedi soir que personne ne sait qui décide. »
- **M. Thierry BOURDAILLE, surveillant de nuit dans un foyer d'hébergement** : « La nuit, je suis seul avec douze résidents. Si l'ordinateur ne marche plus, je dois savoir où trouver les consignes et qui appeler. »
- **Mme Odile LANGEVELLE, représentante des familles au conseil d'administration** : « Si un jour les dossiers de nos enfants sont publiés, je veux l'apprendre par la Fondation, pas par le journal. »

### ANNEXE 3.3 – Le numérique de la Fondation et les personnes accompagnées (notes de M. Laurent TRÉVENEC et de M. Rémi CAZENOVE, directeur du pôle Travail, et témoignages, avril 2027)

**A. Le portail des familles et l'application des personnes accompagnées**

- Le dossier unique ouvrira un portail des familles et une application pour smartphone et tablette : consultation du planning, des rendez-vous et du projet personnalisé, messages avec l'équipe. Le cahier des charges ne contient aucune exigence d'accessibilité ; les écrans ont été conçus par l'éditeur, sans les personnes concernées.
- Beaucoup de personnes accompagnées lisent peu ou pas ; certaines ont des troubles de la vue, de la motricité fine ou de la compréhension. Les établissements rédigent déjà certains documents (règlement de fonctionnement, menus, projet personnalisé) en phrases courtes, illustrées de pictogrammes.
- Selon une enquête menée auprès des familles en mars 2027, environ 30 % d'entre elles n'utilisent pas internet ou ont besoin d'aide pour le faire.
- En avril 2027, une première version du portail et de l'application a été présentée à 20 personnes accompagnées et à 20 familles. Seules 6 personnes et 12 familles ont réussi, sans aide, à trouver le prochain rendez-vous.
- **Mme Odile LANGEVELLE, représentante des familles** : « Je voudrais que mon fils puisse lire lui-même son planning, et que les parents qui n'ont pas d'ordinateur ne soient pas oubliés. »

**B. Le projet d'outil de rédaction automatique des transmissions**

- La société SCRIBALEN propose un outil d'intelligence artificielle générative : en fin de service, le professionnel dicte ses observations sur son smartphone ; l'outil les transcrit et rédige une transmission structurée, enregistrée dans le dossier de la personne. L'éditeur annonce un gain de 20 minutes par professionnel et par jour. L'outil utilise un modèle d'un fournisseur tiers, hébergé dans l'Union européenne ; l'éditeur indique que son offre satisfait aux exigences légales applicables à l'hébergement des données de santé, ce point n'est pas à analyser.
- Les enregistrements vocaux et les textes sont conservés 12 mois par l'éditeur « pour améliorer le service ». L'outil peut aussi produire une synthèse mensuelle du comportement de chaque personne accompagnée et signaler à l'encadrement les professionnels dont les écrits sont jugés incomplets.
- Lors d'un essai de deux semaines dans un foyer, sur 200 transmissions rédigées par l'outil, 20 contenaient une information inexacte (un fait qui n'avait pas été dicté, une confusion de prénoms). Les professionnels dictaient parfois dans la chambre ou devant la personne.
- **M. Thierry BOURDAILLE, surveillant de nuit** : « Je ne suis pas à l'aise avec l'écrit : dicter m'aiderait beaucoup. »
- **Une éducatrice spécialisée** : « Une transmission, c'est un regard professionnel sur une personne, pas un résumé fait par une machine. »
- **Mme Odile LANGEVELLE** : « Je veux savoir si c'est une machine qui écrit sur mon fils. »

**C. La salle de serveurs du siège**

- La salle compte 25 serveurs physiques, dont 10 sont utilisés à moins de 10 % de leur capacité ; la climatisation date de 2012. Elle héberge les trois logiciels de dossier, la paie, le planning, la comptabilité et 8 To de fichiers partagés, dont la moitié n'a pas été ouverte depuis trois ans.
- Le DSI souhaite fermer la salle d'ici 2029 et passer à des services en ligne pour les applications qui y restent. Le fournisseur pressenti pour héberger ces applications ne communique ni la localisation de ses centres de données ni leurs consommations d'énergie.

**D. Les équipements et l'établissement d'aide par le travail**

- Le parc compte environ 1 400 ordinateurs et 600 tablettes et smartphones. Il n'existe pas de politique des équipements : chaque établissement commande sur son budget ; les ordinateurs sont remplacés en moyenne tous les quatre ans. Environ 300 ordinateurs et 150 smartphones retirés sont stockés dans des armoires du siège ; d'autres sont jetés avec les déchets ordinaires. Aucun équipement n'a été réemployé en 2026.
- La DSI prévoit de renouveler environ 400 ordinateurs des unités. Selon elle, environ 150 d'entre eux pourraient servir deux ans de plus avec de la mémoire et un disque neuf (environ 100 € par poste) ; les 250 autres sont trop anciens.
- **M. Rémi CAZENOVE, directeur du pôle Travail** : « L'atelier de conditionnement trie, nettoie et étiquette depuis 2025 des téléphones reconditionnés pour une entreprise de la région ; 12 travailleurs y sont formés. Nous pourrions reconditionner les équipements de la Fondation : c'est un travail valorisant pour les travailleurs. »
- **M. Laurent TRÉVENEC** : « Je veux bien, à condition qu'aucune donnée des personnes accompagnées ne reste sur un disque qui sort de nos murs. »

### ANNEXE 3.4 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Le responsable du traitement met en œuvre des mesures de sécurité adaptées au risque, pour garantir la confidentialité, l'intégrité, la disponibilité et la résilience des systèmes, ainsi que la capacité à rétablir l'accès aux données en cas d'incident, et en vérifie régulièrement l'efficacité. Les données relatives à la santé font l'objet d'une protection renforcée. Un traitement susceptible d'engendrer un risque élevé pour les personnes est précédé d'une analyse d'impact relative à la protection des données. Une violation de données est notifiée à l'autorité de contrôle dans les 72 heures et, en cas de risque élevé, les personnes concernées en sont informées. Le délégué à la protection des données informe, conseille et contrôle le respect du règlement. | Applicable depuis le 25/05/2018. Une proposition européenne de simplification (« omnibus numérique », 19/11/2025) modifiant ce règlement est en discussion et n'est pas applicable. |
| Guide de la sécurité des données personnelles (autorité de contrôle), édition 2024 | Fiches de recommandations, dont la gestion des habilitations (profils définis selon les besoins des métiers, retrait des droits au départ ou au changement de poste, revue régulière des droits), la traçabilité des accès, la sauvegarde et la gestion des incidents. | En vigueur |
| ISO/IEC 27001:2022 | Norme internationale qui spécifie les exigences d'un système de management de la sécurité de l'information, fondé sur l'appréciation et le traitement des risques ; son annexe A énumère 93 mesures de sécurité, dont le contrôle d'accès, la gestion des incidents et la sauvegarde. | En vigueur |
| ISO/IEC 27005:2022 | Lignes directrices pour la gestion des risques liés à la sécurité de l'information : identifier, analyser, évaluer et traiter les risques (réduire, conserver, éviter ou partager le risque, par exemple par une assurance). | En vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI) | Méthode d'appréciation et de traitement des risques numériques, en cinq ateliers, qui intègre les parties prenantes de l'écosystème (éditeurs, prestataires) ; compatible avec l'ISO/IEC 27005:2022. | En vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | 42 mesures de bonnes pratiques, dont la sensibilisation des utilisateurs, l'identification nominative de chaque personne qui accède au système d'information, l'encadrement des arrivées et des départs des utilisateurs et la sauvegarde des données. | En vigueur |
| Directive (UE) 2022/2555 (« NIS 2 ») | Cybersécurité d'entités dites essentielles ou importantes, selon leur secteur et leur taille. Les organes de direction approuvent les mesures de gestion des risques, en supervisent la mise en œuvre, peuvent être tenus pour responsables et suivent une formation. Les mesures couvrent notamment l'analyse des risques, la gestion des incidents, la continuité des activités et la gestion des crises, le contrôle d'accès, la formation et l'authentification multifacteur. | Délai de transposition expiré le 17/10/2024. En France, le projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité, adopté par le Sénat le 12/03/2025, n'est ni adopté par l'Assemblée nationale ni promulgué. |
| Loi n° 2023-22 du 24 janvier 2023 (LOPMI), article L. 12-10-1 du code des assurances | L'indemnisation par un assureur des pertes et dommages causés par une atteinte à un système d'information, y compris le remboursement d'une rançon, est subordonnée au dépôt d'une plainte au plus tard 72 heures après la connaissance de l'atteinte. | En vigueur |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | Obligations de transparence : les personnes sont informées qu'elles interagissent avec un système d'intelligence artificielle ; les contenus produits par une intelligence artificielle générative sont marqués comme tels. | Obligations de transparence applicables depuis le 02/08/2026 |
| Loi n° 2021-1485 du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique en France (REEN) | Sensibilisation au numérique responsable, allongement de la durée de vie des équipements et réemploi, écoconception des services numériques, centres de données et réseaux moins énergivores. | En vigueur |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | Critères d'écoconception des services numériques (stratégie, expérience utilisateur, contenus, hébergement, etc.), dont l'usage du service sur des équipements anciens. | En vigueur |
| Étude de l'ADEME et de l'Arcep sur l'empreinte environnementale du numérique en France | Les terminaux représentent de 65 % à 92 % de l'empreinte environnementale du numérique selon l'indicateur considéré, principalement du fait de leur fabrication. | Volets de 2022 et de 2023 ; mise à jour du 17/01/2025 |

Le conseil d'administration considère, sans que ce point soit à discuter, que la Fondation n'est pas à ce jour identifiée comme entité essentielle ou importante au sens de la directive NIS 2 ; il a décidé de s'inspirer de ses mesures. Il n'est demandé aucune analyse juridique.

### Travail à faire

La Fondation VERLANDRE s'apprête à ouvrir le dossier unique à 1 600 professionnels et à 1 500 familles, alors que personne ne sait qui voit quoi dans les logiciels actuels, qu'une association voisine vient de subir une attaque qui a paralysé ses établissements et que le projet « Horizon 2030 » demande un numérique responsable, accessible et éthique. Mme BRÉCHEVAL vous demande d'auditer les habilitations, d'analyser les risques qui pèsent sur les données des personnes accompagnées, de préparer la Fondation à une crise cyber et de proposer une stratégie de numérique responsable. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.4 ainsi que vos connaissances professionnelles.

**3.1 – L'audit des habilitations aux dossiers des personnes accompagnées (3 points)**

a) Après avoir défini l'audit du système d'information et précisé ce qui le distingue du contrôle interne, présentez la démarche de l'audit demandé par le conseil d'administration : objectifs, périmètre, étapes et livrables, en tenant compte du calendrier fixé dans l'annexe 3.1.

b) Représentez, sous la forme d'un tableau, le processus « arrivée, mobilité, départ » des utilisateurs des logiciels de dossier tel qu'il fonctionne aujourd'hui : pour chacune des trois étapes, l'acteur, le risque et le contrôle interne attendu. Indiquez ensuite trois tests de contrôle que vous mènerez pendant l'audit, chacun relié à un constat de l'annexe 3.1. Les diligences attendues sont des rapprochements, des sondages, des entretiens et des observations.

c) Proposez quatre critères de performance et de conformité au regard desquels l'audit appréciera les habilitations (par exemple la fiabilité, l'efficacité, la sécurité, la conformité au RGPD) ; pour chacun, précisez ce qui est attendu et appréciez la situation actuelle à partir de l'annexe 3.1.

**3.2 – Les risques pesant sur les données des personnes accompagnées (3 points)**

a) Après avoir présenté la typologie des risques liés aux systèmes d'information (cybermenaces, défaillances opérationnelles, risques réglementaires et métiers), identifiez quatre risques pesant sur les données des personnes accompagnées, révélés par les annexes 3.1 et 3.2, en couvrant les trois catégories. Pour chacun, précisez sa catégorie et ses conséquences pour les personnes accompagnées et pour la Fondation.

b) Choisissez l'un des référentiels de l'annexe 3.4 qui permettent d'apprécier les risques, en précisant sa nature (norme, lignes directrices, méthode ou guide), puis indiquez, en principe, comment la démarche qu'il propose permettrait d'évaluer ces quatre risques et de décider de leur traitement. Appliquez les options de traitement à deux des quatre risques, dont l'un au moins fera intervenir le contrat d'assurance cyber en cours de négociation. Ni le détail des ateliers ni une cotation chiffrée ne sont attendus.

**3.3 – La politique de cybersécurité et la gestion d'une crise cyber (3,5 points)**

a) Après avoir défini la politique de sécurité du système d'information et rappelé ses objectifs, proposez les quatre principes sur lesquels vous fonderiez celle de la Fondation, chacun relié à un risque de la question 3.2 et décliné en une mesure prioritaire. Aucun paramétrage n'est attendu.

b) Proposez l'organisation de la gestion d'une crise cyber à la Fondation : le déclenchement et la composition de la cellule de crise ; les rôles du conseil d'administration, de la directrice générale, de la direction des systèmes d'information, des directeurs d'établissement d'astreinte, de la déléguée à la protection des données, de l'assureur et des prestataires ; la communication auprès des professionnels, des familles et des personnes accompagnées. Vous tiendrez compte des établissements ouverts jour et nuit et des enseignements de l'annexe 3.2. Le contenu détaillé des plans de continuité et de reprise n'est pas attendu.

**3.4 – Une stratégie de numérique responsable, accessible et éthique (3,5 points)**

a) Après avoir précisé ce qu'est une gouvernance du système d'information orientée vers la responsabilité sociétale (inclusion, éthique, sobriété), proposez trois mesures pour rendre le portail des familles et l'application accessibles aux personnes accompagnées et aux familles, puis quatre règles éthiques d'usage de l'outil de rédaction automatique des transmissions, en vous appuyant sur les annexes 3.3 et 3.4.

b) Indiquez trois conditions d'une transition responsable de la salle de serveurs du siège vers des services en ligne, puis proposez la place de l'établissement d'aide par le travail dans le réemploi des équipements, avec deux conditions de réussite. Aucun calcul d'empreinte n'est attendu.

c) Proposez deux indicateurs de suivi de cette stratégie, l'un pour l'accessibilité, l'autre pour le réemploi des équipements, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
