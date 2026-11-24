# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 51

**DOSSIER 3 – FIABILISER LA FACTURATION, MAÎTRISER LES ACCÈS, AUDITER LE CARREAU ET RÉPONDRE AUX DEMANDES DE DONNÉES DE DURABILITÉ (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 17, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en avril 2027. BRÉVALIM est une société d'économie mixte locale, société anonyme à conseil d'administration créée en 1994, qui exploite le marché de gros alimentaire de Brévaline, une métropole de l'ouest de la France. Sur un site de 60 hectares, 240 entreprises (grossistes en fruits et légumes, en produits de la mer, en viandes, en produits laitiers et en fleurs, transformateurs, logisticiens, services) louent à BRÉVALIM des cases dans des pavillons, des bureaux et des cellules d'un entrepôt frigorifique ; chaque nuit, des producteurs de la région vendent leurs récoltes sur le carreau des producteurs, et 2 000 véhicules d'acheteurs professionnels (restaurateurs, commerçants, marchés forains, restauration collective) passent le péage entre 3 heures et 11 heures. Brévaline Métropole détient 60 % du capital, le Département 6 %, la Banque VERDELIN 14 %, la chambre de commerce et d'industrie 8 % et l'Union des grossistes du marché de Brévaline 12 %. En 2026, BRÉVALIM a réalisé un chiffre d'affaires de 28 M€ ; elle emploie 210 salariés. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « Marché de Brévaline 2031 », adopté en janvier 2027 par le conseil d'administration, fixe cinq objectifs : porter de 30 % à 40 % la part des produits régionaux dans les volumes entrés sur le marché ; dématérialiser d'ici 2029 toute la relation avec les entreprises installées et les acheteurs ; valoriser 80 % des déchets du site en 2031, contre 60 % en 2026 ; fiabiliser la facturation et le pilotage, en rendant compte chaque trimestre aux actionnaires ; garantir la sûreté du site et la sécurité des données. Le système d'information s'est construit par morceaux : chaque direction a choisi ses outils, qui ne se parlent pas, et Brévaline Métropole demande désormais des données sur les flux alimentaires du marché.

Vous êtes directeur(rice) général(e) délégué(e) de BRÉVALIM depuis 2025, chargé(e) de l'exploitation du marché et du système d'information. La directrice générale, Mme Héloïse VAUCLERC, vous demande trois travaux : préparer la stratégie et l'organisation du système d'information (dossier 1) ; organiser et exploiter les données des acheteurs et des flux, et revoir le pilotage présenté au conseil d'administration (dossier 2) ; fiabiliser la facturation, maîtriser les accès au site et aux applications, auditer l'attribution du carreau et répondre aux demandes de données de durabilité (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de BRÉVALIM et chiffres clés

BRÉVALIM est une société d'économie mixte locale, société anonyme à conseil d'administration créée en 1994, dont le siège est sur le site du marché de gros de Brévaline, métropole de l'ouest de la France. Elle exploite le marché : elle loue des emplacements aux entreprises installées, organise chaque nuit la vente des producteurs sur le carreau, accueille les acheteurs professionnels au péage et fournit l'énergie, l'eau et le froid du site. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Le modèle, les actionnaires et la gouvernance**

| Donnée | Valeur |
|---|---|
| Entreprises installées | 240 entreprises, titulaires d'un contrat annuel d'emplacement : cases dans les pavillons, bureaux, cellules de l'entrepôt frigorifique |
| Carreau des producteurs | 300 emplacements, attribués chaque nuit par les placiers de BRÉVALIM aux producteurs de la région qui viennent vendre leurs récoltes |
| Acheteurs | acheteurs professionnels (restaurateurs, commerçants, marchés forains, restauration collective), titulaires d'une carte d'acheteur, qui entrent sur le site par le péage |
| Entrepôt frigorifique | 12 000 m² en 40 cellules louées aux entreprises installées ; BRÉVALIM produit le froid et le refacture |
| Actionnaires | Brévaline Métropole 60 % ; Département 6 % ; Banque VERDELIN 14 % ; chambre de commerce et d'industrie 8 % ; Union des grossistes du marché de Brévaline 12 %, présidée par Mme Évelyne GARBUSSAC, grossiste en fruits et légumes |
| Conseil d'administration | douze membres, dont huit représentants des collectivités ; président : M. Bastien FERRANDOU, vice-président de Brévaline Métropole |
| Direction | directrice générale : Mme Héloïse VAUCLERC ; directeur(rice) général(e) délégué(e) chargé(e) de l'exploitation et du système d'information : vous |

**L'activité en 2026**

| Donnée | Valeur |
|---|---|
| Site | 60 hectares |
| Entreprises installées | 240 : 150 grossistes, 50 transformateurs et logisticiens, 40 entreprises de services |
| Carreau des producteurs | 300 emplacements, occupés chaque nuit par 180 producteurs en moyenne l'été et 70 l'hiver |
| Acheteurs | 9 000 cartes d'acheteur actives ; 2 000 véhicules d'acheteurs par nuit, six nuits sur sept |
| Horaires | activité de 3 heures à 11 heures |
| Produits | 900 000 tonnes entrées sur le marché dans l'année, dont 30 % de produits régionaux |
| Déchets | 60 % des déchets du site valorisés |
| Chiffre d'affaires | 28 M€ : redevances d'emplacement et loyers 17 M€ ; droits d'entrée et cartes d'acheteur 4 M€ ; refacturation de l'énergie, de l'eau et du froid 5 M€ ; services 2 M€ |
| Dépenses du système d'information | environ 1,3 M€, dont 0,3 M€ d'infogérance |

**L'effectif au 31/12/2026**

| Direction ou service | Salariés |
|---|---|
| Direction de l'exploitation : placiers, agents de péage, agents de sûreté, agents de nuit | 95 |
| Direction technique : froid, maintenance, propreté, déchets | 60 |
| Service commercial et des relations avec les entreprises | 15 |
| Service des systèmes d'information | 7 |
| Fonctions support : finances, ressources humaines, juridique, achats | 25 |
| Direction générale et communication | 8 |
| **Total** | **210** |

**Le système d'information en quelques lignes**

- **Logiciel de gestion du marché**, installé en 2011, édité par un petit éditeur régional : contrats d'emplacement, facturation des redevances et des refacturations, attribution des emplacements du carreau, saisie par les placiers sur tablette. Il est installé sur des serveurs de la salle informatique du siège, dont l'exploitation (supervision, sauvegardes, astreinte) est confiée depuis 2024 à un infogérant.
- **Système de péage et de contrôle d'accès** (barrières, lecteurs de cartes, bornes de paiement), choisi en 2019 par la direction de l'exploitation chez un fournisseur spécialisé, avec son propre serveur.
- **Application des acheteurs** (carte d'acheteur sur téléphone, horaires, plan), développée en 2023 par une agence web.
- **Portail des entreprises installées** (factures, demandes techniques).
- **Supervision du froid** de l'entrepôt, choisie par la direction technique.
- **Badges** d'accès aux pavillons, à l'entrepôt et aux locaux techniques.
- Pont-bascule et suivi des déchets ; progiciel comptable et de paie ; bureautique en ligne.

**Organigramme simplifié (avril 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil d'administration | président : M. Bastien FERRANDOU |
| — | direction générale | directrice générale : Mme Héloïse VAUCLERC |
| Directeur(rice) général(e) délégué(e) chargé(e) de l'exploitation et du système d'information (vous) | direction de l'exploitation | Mme Armelle DUCHÉRAN |
| | direction technique | M. Loïc PERRAGUÈS |
| Directrice générale | service commercial et des relations avec les entreprises | Mme Nadège QUÉRINEL |
| | direction administrative et financière : fonctions support (finances, ressources humaines, juridique, achats) | M. Fabrice MORVÉLAN |
| | communication | — |
| Direction administrative et financière | service des systèmes d'information | M. Corentin LAVEYRAC, responsable des systèmes d'information |
| | déléguée à la protection des données, juriste | Mme Inès TALMONDIER |

### ANNEXE 3.1 – La facturation des contrats d'emplacement (note de M. Fabrice MORVÉLAN, directeur administratif et financier, mars 2027)

**A. La chaîne de facturation**

1. **Le contrat.** Le service commercial saisit dans le logiciel de gestion du marché le contrat annuel d'emplacement de chaque entreprise installée : cases, bureaux et cellules occupés, surfaces, tarifs, dates. Les changements en cours d'année (case supplémentaire, agrandissement, déménagement dans un autre pavillon) lui sont signalés par les placiers ou par l'entreprise, par téléphone ou par courriel.
2. **La facture.** Chaque mois, le logiciel émet une facture par entreprise installée, soit 240 factures : redevance d'emplacement et loyer du mois, refacturation de l'énergie, de l'eau et du froid du mois précédent. Les factures sont déposées en PDF sur le portail des entreprises installées ou envoyées sur papier.
3. **Le fichier des écritures.** Chaque mois, le logiciel produit un fichier des écritures des factures et des avoirs, d'environ 2 000 lignes, que la comptabilité charge dans le progiciel comptable.
4. **L'encaissement et les relances.** 200 entreprises paient par prélèvement, 40 par virement. La comptabilité rapproche les encaissements et prépare les relances dans un tableur, à partir d'une extraction du progiciel comptable.

**B. Les constats de 2026 et du début de 2027**

- En 2026, 60 changements d'emplacement ont été demandés. Un relevé de terrain mené en février 2027 par le service commercial a trouvé 15 cases ou cellules occupées par une entreprise dont le contrat n'avait pas été mis à jour. Le manque à facturer est estimé à 150 k€ par an.
- La révision annuelle des tarifs, au 1er janvier, est saisie à la main, contrat par contrat. En janvier 2027, 20 contrats ont été mal révisés : 12 entreprises ont été trop facturées, 8 n'ont pas été facturées au nouveau tarif. L'erreur a été découverte grâce aux réclamations transmises par l'Union des grossistes.
- Les 3 agents de la facturation créent les factures et les avoirs ; un avoir n'exige ni validation ni motif. En 2026, ils ont créé 300 avoirs, pour 400 k€.
- En 2026, 480 lignes du fichier mensuel des écritures, soit 2 %, ont été rejetées par le progiciel comptable (entreprise inconnue, compte absent, montant nul). La comptable les corrige ou les supprime directement dans le progiciel comptable ; rien n'est corrigé dans le logiciel de gestion du marché, et aucune liste des rejets n'est conservée.
- Pour 2026, le logiciel de gestion du marché donne 22 900 k€ de redevances, de loyers et de refacturations ; la comptabilité arrête les mêmes rubriques à 22 000 k€ (17 000 k€ de redevances et de loyers, 5 000 k€ de refacturations). Personne n'a encore expliqué l'écart. Le compte rendu trimestriel aux actionnaires prévu par le plan « Marché de Brévaline 2031 » reprendra ce chiffre d'affaires.
- Le logiciel ne conserve que la dernière version de chaque contrat : on ne sait ni qui a modifié une surface ou un tarif, ni quand. Les 15 personnes du service commercial et les 3 agents de la facturation ont tous les droits sur les contrats, les factures et les avoirs.
- En 2026, 25 entreprises ont été relancées pour des factures déjà payées ou annulées par un avoir.
- Pour 30 entreprises installées, l'identifiant de l'entreprise (numéro SIREN) enregistré dans le logiciel est absent ou ne correspond plus à l'entreprise, après un rachat ou un changement de nom.

**C. L'échéance de septembre 2027**

BRÉVALIM devra émettre ses factures sous forme électronique à compter du 1er septembre 2027 (annexe 3.5). L'éditeur du logiciel de gestion du marché livrera en juin 2027 une version qui transmet les factures à une plateforme agréée. Selon lui, « chaque facture partira avec ses données structurées : identifiant de l'entreprise, contrat, montants ; une facture fausse sera transmise telle quelle à l'entreprise et à la plateforme ».

**D. Les échelles retenues par la direction générale pour apprécier les risques**

| Niveau | Probabilité | Impact |
|---|---|---|
| faible | jamais constaté, peu plausible | moins de 50 k€ par an, sans réclamation |
| moyen | constaté quelques fois en 2026 | de 50 à 200 k€ par an, ou réclamations d'entreprises installées |
| fort | constaté chaque mois en 2026, ou facile à provoquer, ou quasi certain à l'échéance si rien ne change ; dans tous les cas, sa cause est toujours là | plus de 200 k€ par an, ou chiffre d'affaires présenté aux actionnaires inexact, ou factures électroniques erronées en série |

La direction générale traite en priorité les risques dont la probabilité et l'impact sont tous deux forts.

### ANNEXE 3.2 – Les badges et les comptes (relevé de M. Rodolphe MARCHEVIEL, responsable de la sûreté, et de M. Corentin LAVEYRAC, responsable des systèmes d'information, mars 2027)

**A. Les badges d'accès**

| Population | Badges actifs | Dont badges au nom de personnes parties (estimation de mars 2027) | Création du badge | Fin du badge |
|---|---|---|---|---|
| Salariés de BRÉVALIM | 230 | 20 | demande du service des ressources humaines, par courriel | aucune date de fin ; le badge est rendu au départ « quand on y pense » |
| Salariés des entreprises installées | 2 150 | environ 350 | formulaire papier rempli par l'entreprise | aucune date de fin ; aucune entreprise ne signale les départs de ses salariés |
| Saisonniers d'été recrutés par BRÉVALIM pour le carreau (renfort des placiers, propreté) | 80 | 80 | liste remise en mai par la direction de l'exploitation | contrats terminés fin septembre 2026 ; badges toujours actifs |
| Prestataires de nettoyage et de maintenance du froid | 140 | environ 50 | demande du prestataire | aucune date de fin ; 10 badges « prestataire », sans nom, circulent entre les intervenants |
| **Total** | **2 600** | **environ 500** | | |

- Tous les badges ouvrent, à toute heure et tous les jours, les pavillons, les quais et les couloirs de l'entrepôt frigorifique, les portes des 40 cellules et les locaux techniques (salle des machines du froid, locaux électriques). Les portes des cellules s'ouvrent ainsi au badge « pour que les agents de nuit et les techniciens du froid puissent intervenir ». Seuls la salle informatique du siège et le local de la caisse du péage ont un accès réservé.
- Les agents de sûreté constatent chaque semaine des badges prêtés : à un collègue qui a oublié le sien, à un chauffeur, à un salarié qui vient d'arriver et n'a pas encore de badge.
- Le système des badges enregistre chaque passage (badge, porte, heure) ; personne ne consulte ce journal, sauf après un incident.

**B. Les comptes des applications**

- Les 90 entreprises qui ont un compte sur le portail des entreprises installées en ont un seul chacune, créé par l'éditeur à la demande du service commercial. L'identifiant et le mot de passe sont partagés entre le dirigeant, le comptable et des salariés, et ne changent pas quand l'un d'eux quitte l'entreprise. Le compte donne accès à toutes les factures et à toutes les demandes techniques de l'entreprise.
- Les 12 placiers et les saisonniers d'été utilisent sur les tablettes deux comptes génériques du logiciel de gestion du marché, « placier 1 » et « placier 2 », dont le mot de passe n'a pas changé depuis 2019 et figure au dos des tablettes.
- Les comptes du logiciel de gestion du marché et du progiciel comptable sont nominatifs ; le service des systèmes d'information les crée sur demande par courriel, sans profil type.
- Personne n'est chargé de revoir les droits : M. MARCHEVIEL gère les badges, M. LAVEYRAC les comptes des applications, l'éditeur ceux du portail. La liste des personnes autorisées n'a jamais été comparée à celle des badges et des comptes actifs.

**C. Les incidents de 2026**

- 12 vols de marchandises dans des cellules de l'entrepôt, la nuit. Dans 5 cas, le journal des badges montre l'ouverture de la cellule avec le badge d'une personne partie : deux saisonniers de l'été, trois anciens salariés d'entreprises installées.
- En novembre 2026, un grossiste a découvert qu'un salarié d'un concurrent, qui avait travaillé chez lui jusqu'en juin, consultait encore ses factures sur le portail, avec l'identifiant et le mot de passe qu'il connaissait.
- Une nuit d'octobre, un saisonnier de l'été, dont le contrat avait pris fin en septembre, a été trouvé dans la salle des machines du froid.

**D. Deux points de vue**

**Mme Armelle DUCHÉRAN, directrice de l'exploitation** : « Si on limite les badges, mes agents de nuit ne pourront plus ouvrir une cellule en alarme à 4 heures du matin. »

**Mme Évelyne GARBUSSAC, présidente de l'Union des grossistes** : « Nos entreprises n'ont pas le temps de remplir un formulaire à chaque départ : un salarié sur trois change dans l'année. »

### ANNEXE 3.3 – L'attribution des emplacements du carreau des producteurs (note de Mme Josiane TRÉMOULAC, chef des placiers, extraits de plaintes et demande du conseil d'administration, mars 2027)

**A. Les règles écrites (règlement du carreau de 2018)**

- Les 300 emplacements sont attribués chaque nuit, à partir de minuit, par les placiers, qui saisissent chaque attribution sur tablette dans le logiciel de gestion du marché.
- Ordre de priorité : d'abord les abonnés de la saison, qui ont réservé un emplacement fixe pour toute la saison (100 emplacements en été) ; l'emplacement d'un abonné absent à 3 heures est remis en attribution. Ensuite, les autres producteurs, selon leur ancienneté sur le carreau. Enfin, à ancienneté égale, l'ordre d'arrivée constaté au péage.
- Après 3 heures, un placier peut modifier une attribution sans motif (échange d'emplacements, producteur arrivé en retard).
- Les 40 emplacements les plus proches de l'entrée des acheteurs sont les plus recherchés.

**B. Ce que l'on sait de l'été 2026 (180 producteurs par nuit en moyenne)**

- Le logiciel tient un journal des attributions et de leurs modifications : date, heure, compte utilisé, emplacement, producteur. Avec les deux comptes génériques des tablettes, il ne dit pas quel placier a fait la modification. Ce journal est conservé treize mois : les nuits de juin 2026 seront effacées à partir de juillet 2027.
- 40 % des modifications d'attribution ont été faites après 3 heures ; aucune ne porte de motif.
- Sur 10 nuits d'août 2026, Mme TRÉMOULAC a comparé les attributions enregistrées au relevé des emplacements fait à 5 heures par les agents de sûreté : sur 1 800 occupations relevées, 270, soit 15 %, ne correspondent pas à l'attribution enregistrée (autre producteur, emplacement occupé sans attribution, emplacement attribué mais vide).
- Sur les 40 emplacements proches de l'entrée, 30 ont été occupés plus de huit nuits sur dix par les mêmes 25 producteurs ; 10 de ces 25 producteurs ne sont ni abonnés, ni parmi les plus anciens du carreau.
- Six nuits, les tablettes n'ayant plus accès au logiciel, l'attribution s'est faite sur papier, puis a été ressaisie le lendemain ; une partie des feuilles n'a pas été conservée.
- Les 12 placiers travaillent de minuit à 8 heures ; le service des systèmes d'information n'est présent qu'en journée.

**C. Les plaintes (35 plaintes écrites de producteurs en 2026)**

- « Les places près de l'entrée sont toujours données aux mêmes, qui arrivent pourtant après nous. » (un producteur de légumes, juillet 2026)
- « Certains emplacements sont réservés aux habitués : on nous dit qu'ils sont pris, et ils restent vides jusqu'à 4 heures. » (une productrice de fruits, août 2026)
- Mme TRÉMOULAC : « Mes placiers appliquent les règles. Les échanges après 3 heures, c'est pour rendre service. Un audit, ils vont le prendre comme une accusation. »

**D. La demande du conseil d'administration (séance du 22/03/2027)**

« Avant la saison d'été 2027, qui commence le mardi 1er juin, le conseil veut savoir si les emplacements du carreau sont attribués selon les règles écrites et si les données enregistrées sont fiables. BRÉVALIM n'a pas d'audit interne : un auditeur des systèmes d'information externe conduira la mission pendant quatre semaines, du lundi 3 au vendredi 28 mai 2027 (jeudi 6 mai et lundi 17 mai fériés), et présentera ses conclusions au conseil du lundi 31 mai. Préparez-en le cadrage. »

### ANNEXE 3.4 – Les demandes de données de durabilité et le projet d'affichage dynamique (note de M. Loïc PERRAGUÈS, directeur technique, mars 2027)

**A. Les demandes de trois entreprises installées**

Trois entreprises installées, un logisticien qui loue 8 cellules de l'entrepôt frigorifique, un grossiste en produits de la mer et un grossiste en fruits et légumes, appartiennent à des groupes qui établissent leur état de durabilité conformément aux normes ESRS. Chaque année, en janvier, elles nous demandent, pour l'année écoulée et pour leurs cellules et leurs cases, l'électricité et l'eau consommées, le froid fourni et les déchets triés, par type de déchet.

| Donnée demandée | Où elle se trouve aujourd'hui | Comment elle est obtenue |
|---|---|---|
| Électricité et eau consommées | compteurs relevés chaque mois par les techniciens et saisis dans le logiciel de gestion du marché pour la refacturation | extraction du logiciel, puis tri à la main par entreprise |
| Froid fourni | supervision du froid, cellule par cellule | relevé à l'écran, cellule par cellule |
| Déchets triés par type | pont-bascule : une pesée par benne ; chaque benne sert à toutes les entreprises d'un pavillon | aucune donnée par entreprise : le poids du pavillon est réparti selon la surface occupée, sans que l'entreprise en soit informée |

- Une assistante de la direction technique rassemble ces données dans un tableur, qu'elle envoie par courriel : les trois demandes lui prennent 15 jours de travail par an. Rien n'est gardé de ce qui a été envoyé, ni de la façon dont les chiffres ont été obtenus.
- En 2026, un groupe a relevé que l'électricité envoyée pour 2025 comptait deux fois le mois de décembre ; un autre a reçu le froid d'une cellule voisine ; le troisième a demandé pourquoi ses déchets avaient augmenté de moitié, alors qu'il n'avait rien changé.
- Deux autres entreprises installées ont annoncé des demandes semblables pour 2028.
- M. PERRAGUÈS : « Ce n'est pas à BRÉVALIM de faire le reporting de ses clients. Mais si nous répondons mal, ils iront chercher ailleurs des cellules mieux suivies. »

**B. Le projet d'affichage dynamique (proposition du service de la communication, février 2027)**

- 60 écrans de grande taille, achetés neufs, dans les pavillons et au péage, pour afficher les cours du jour, les informations du marché (horaires, travaux, consignes) et des publicités des grossistes.
- Les écrans restent allumés jour et nuit, sept jours sur sept, alors que le marché est ouvert de 3 heures à 11 heures, six nuits sur sept.
- Des vidéos en haute définition passent en boucle ; un serveur rafraîchit tous les écrans toutes les minutes. Les cours du jour sont mis à jour deux fois par nuit par le service commercial.
- BRÉVALIM a déjà 20 écrans d'affichage, installés en 2022 au péage et dans deux pavillons, qui fonctionnent : le projet prévoit de les remplacer et de les mettre au rebut.
- Les horaires, le plan et les informations du marché figurent déjà dans l'application des acheteurs.
- Le service de la communication : « Les écrans rendront le marché plus moderne, et la publicité des grossistes les paiera. »

Aucune mesure de la consommation ni de l'empreinte du projet n'a été faite, et aucun calcul n'est demandé.

**C. La durabilité dans les décisions sur le système d'information**

Aucun comité ni aucune règle ne fait entrer la durabilité dans les décisions sur le système d'information. Le projet d'affichage n'a été examiné que par le service de la communication et par le fournisseur des écrans. Aucune demande d'achat d'équipement ou de logiciel ne comporte de critère environnemental ou social, et personne n'est chargé des demandes de données de durabilité.

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Facturation électronique | généralisation de la facturation électronique et du e-reporting, calendrier issu de l'article 91 de la loi de finances pour 2024 | depuis le 01/09/2026, toutes les entreprises assujetties à la TVA doivent pouvoir recevoir des factures électroniques ; BRÉVALIM devra émettre les siennes sous forme électronique à compter du 01/09/2027 ; les factures transitent par une plateforme agréée par l'administration, dans un format structuré (Factur-X, UBL ou CII) ; aucune règle de facturation n'est à connaître |
| Sécurité de l'information | ISO/IEC 27001:2022 ; ISO/IEC 27002:2022 | la norme ISO/IEC 27001 fixe les exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques ; son annexe A compte 93 mesures en quatre thèmes (organisationnelles, liées aux personnes, physiques, technologiques), dont la gestion des identités, le contrôle d'accès et la sécurité physique des locaux ; ISO/IEC 27002 est le guide de mise en œuvre de ces mesures |
| Données personnelles | règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | les données sont limitées à ce qui est nécessaire (minimisation), conservées pendant une durée limitée et protégées par des mesures de sécurité appropriées ; les badges, les comptes et les journaux de passage ou de modification se rapportent à des personnes identifiées ; BRÉVALIM a désigné une déléguée à la protection des données, Mme Inès TALMONDIER ; aucune analyse juridique n'est attendue |
| Information de durabilité | directive (UE) 2022/2464 (CSRD), modifiée en 2025 et en 2026 ; règlement délégué (UE) 2026/1563 du 3 juillet 2026 (ESRS révisées) ; règlement délégué (UE) 2026/1560 (norme volontaire VSME) | les entreprises dans le champ de la CSRD établissent un état de durabilité selon les normes ESRS, fondé sur la double matérialité (impacts de l'entreprise sur l'environnement et les personnes, effets des enjeux de durabilité sur l'entreprise) et couvrant sa chaîne de valeur ; les ESRS révisées s'appliquent aux exercices ouverts à compter du 01/01/2027 ; la norme volontaire VSME permet à une entreprise hors du champ de présenter des informations de durabilité ; les groupes des trois entreprises installées de l'annexe 3.4 établissent leur état de durabilité conformément aux normes ESRS ; BRÉVALIM n'établit pas d'état de durabilité, et aucun assujettissement n'est à déterminer |

### Travail à faire

La facturation des contrats d'emplacement, qui porte l'essentiel du chiffre d'affaires, accumule les erreurs à quelques mois de l'émission des factures électroniques. Près d'un badge sur cinq appartient à une personne partie, et des comptes sont partagés. Des producteurs contestent l'attribution des emplacements du carreau, et le conseil d'administration veut un audit avant la saison d'été. Enfin, trois entreprises installées demandent chaque année des données de durabilité que BRÉVALIM rassemble à la main, pendant que le service de la communication propose 60 écrans d'affichage dynamique. Mme VAUCLERC vous demande d'analyser les risques de la facturation et d'en organiser les contrôles, de proposer le dispositif de gestion des badges et des comptes, de cadrer l'audit de l'attribution du carreau et de faire entrer la durabilité dans les décisions sur le système d'information. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – Les risques et la fiabilisation de la facturation (3,5 points)**

a) Après avoir présenté une typologie des risques liés aux systèmes d'information, identifiez quatre risques de la chaîne de facturation de l'annexe 3.1, formulés comme des événements redoutés, et classez-les selon cette typologie.

b) Après avoir défini la fiabilisation d'un système d'information comptable et décisionnel, proposez la cartographie des contrôles de la chaîne de facturation, du contrat d'emplacement au chiffre d'affaires présenté aux actionnaires : pour cinq points de contrôle, précisez le risque traité, le contrôle, sa nature (préventif ou détectif, manuel ou automatisé) et son responsable. L'un de ces contrôles rapproche l'occupation constatée des emplacements et les contrats facturés. Aucune règle comptable ni fiscale de la facturation n'est attendue.

c) Appréciez la probabilité et l'impact de vos quatre risques selon les échelles de l'annexe 3.1 D, puis indiquez les deux actions à mener en priorité avant l'émission des factures électroniques, en les justifiant.

**3.2 – La gestion des badges et des comptes (3,5 points)**

a) Après avoir défini la gestion des identités et des accès, proposez, à partir de l'annexe 3.2, le dispositif de gestion des badges et des comptes de BRÉVALIM : le cycle de vie des identités (arrivée, changement, départ) pour chacune des quatre populations de badges ; l'application du principe du moindre privilège aux zones d'accès du site et aux comptes ; la revue périodique des droits ; la fin des comptes partagés et génériques. Répondez aux objections de Mme DUCHÉRAN et de Mme GARBUSSAC. Aucun paramétrage d'équipement ni aucun test technique n'est attendu.

b) Présentez, dans un tableau, les rôles et les responsabilités dans ce dispositif de la direction générale, du responsable de la sûreté, du responsable des systèmes d'information, des directions métiers, des entreprises installées et des prestataires.

**3.3 – L'audit de l'attribution des emplacements du carreau (2 points)**

a) Après avoir défini l'audit d'un processus du système d'information, cadrez l'audit de l'attribution des emplacements du carreau que conduira l'auditeur externe : ses trois objectifs, son périmètre, ses étapes sur les quatre semaines de la mission et quatre preuves à demander, dont les journaux des modifications faites sur les tablettes.

b) Proposez trois critères d'appréciation de l'attribution, l'équité, la traçabilité et la fiabilité des données, en précisant pour chacun ce qui est attendu et ce que l'annexe 3.3 laisse craindre. Indiquez enfin deux facteurs de succès et deux points de vigilance propres à cet audit. Aucune analyse juridique n'est attendue.

**3.4 – Les données de durabilité, l'affichage dynamique et la gouvernance responsable du système d'information (4 points)**

a) Après avoir rappelé ce qu'est un état de durabilité établi conformément aux normes ESRS, expliquez, à partir des annexes 3.4 et 3.5, pourquoi des entreprises installées demandent des données de durabilité à BRÉVALIM, qui n'établit pas d'état de durabilité, et quel rôle le système d'information doit jouer dans leur collecte, leur traçabilité et leur fiabilité. Proposez trois mesures. Aucun assujettissement n'est à déterminer.

b) Après avoir défini la sobriété numérique, appréciez le projet d'affichage dynamique de l'annexe 3.4 B au regard de ce principe, puis proposez trois mesures. Aucun calcul d'empreinte n'est attendu.

c) Proposez une gouvernance du système d'information orientée vers la responsabilité sociétale de BRÉVALIM : l'instance, sa composition et son rôle, trois critères de durabilité à faire entrer dans les décisions sur les projets, et un indicateur de suivi précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
