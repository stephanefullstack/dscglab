# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 41 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F09 performance du SI, F11 blockchain et registres distribués, F15 RGPD opérationnel, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle des données exécuté, indicateurs, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le modèle des données des dossiers et des missions | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) | 3 |
| 2.2 Les échanges de données avec les distributeurs, les constructeurs et les prestataires | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données | 2,5 |
| 2.3 Les délais d'arrivée des prestataires | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 3,5 |
| 2.4 Le registre commun des missions | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain | 2 |
| 2.5 Le coût du système d'information des dossiers et son pilotage | `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) | 2 |
| **Dossier 2 – Organiser et exploiter les données des dossiers et du réseau de prestataires** |  | **13** |

Répartition indicative : connaissances (cardinalités, modèles conceptuel et logique et règles de passage, interopérabilité et ses niveaux, dimensions de la qualité, analyses descriptive et exploratoire, chaîne de traitement, fonctionnement d'un registre distribué, inducteur de coût, indicateur à cinq champs) environ 2,5 points (la moitié des items 2.1 b-1, 2.1 b-4, 2.2 a-1, 2.2 b-2, 2.3 a-1, 2.3 b-2, 2.4 a-1, 2.4 a-2, 2.5 a-1 et 2.5 b-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le modèle des données des dossiers et des missions (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) ». Modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites ; modèle physique seulement nommé ; aucune requête.

**Annexes mobilisées** : annexe 2.1 (règles de gestion, extrait du modèle logique actuel, précisions du directeur des plateaux, constats de 2026).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux défauts du modèle actuel, chacun rapporté à une règle de gestion et relié à un constat de l'annexe 2.1 C | 0,5 |
| a-2 | Troisième défaut, rapporté à une règle et à un constat ; conclusion : les anomalies viennent de la structure des données | 0,5 |
| b-1 | Cardinalités définies ; sept entités avec identifiant et attributs élémentaires (bénéficiaire, contrat, garantie, dossier, mission, prestataire, spécialité) | 0,5 |
| b-2 | Associations hiérarchiques et leurs cardinalités, justifiées par les règles : contrat du bénéficiaire, garantie du contrat, dossier ouvert au titre d'une garantie, missions du dossier, spécialité de la mission, prestataire qui réalise (0,1) | 0,5 |
| b-3 | Historique des propositions : association n:m entre mission et prestataire, porteuse de la date, de la réponse et du motif du refus, distincte de la réalisation ; habilitations n:m | 0,5 |
| b-4 | Modèle logique de neuf tables déduit par les règles de passage énoncées (clé étrangère côté 0,1 ou 1,1 ; table à clé composée pour chaque association n:m) | 0,5 |

**Réponse attendue**

*2.1 a) – Trois défauts du modèle logique actuel*

Trois défauts parmi les suivants (0,5 pt pour deux défauts, 0,5 pt pour le troisième et la conclusion), chacun rapporté à une règle de gestion et à un constat :

1. **Le prestataire est un texte libre dans le dossier.** La colonne « prestataire » de DOSSIER n'est pas une clé étrangère vers PRESTATAIRE, alors que RG6 confie chaque mission à un prestataire agréé, identifié par son numéro d'agrément (RG7). Rien ne garantit que le nom saisi désigne un prestataire connu : les 3 400 prestataires apparaissent sous **environ 5 000 noms** différents, et l'on ne sait pas dire combien de missions chacun a reçues. Le réseau de prestataires ne peut ni mesurer la charge ni la qualité d'un prestataire, ni rapprocher sûrement ses factures.
2. **Une seule mission par dossier.** Les heures de demande et d'arrivée et le prestataire sont des colonnes du dossier : le modèle confond le dossier et la mission, alors que RG5 prévoit une ou plusieurs missions par dossier. Les missions suivantes sont décrites dans le champ « commentaire » : **180 000 missions** sur 700 000 (700 000 payées pour 520 000 dossiers) échappent au logiciel des dossiers, à la mesure des délais et au contrôle des factures.
3. **Les refus ne sont pas conservés.** Le chargé efface le nom du prestataire qui refuse (RG6 demande d'enregistrer chaque proposition, sa réponse et le motif du refus). Une mission sur cinq a pourtant été refusée au moins une fois : on ne sait ni quels prestataires refusent, ni pourquoi (dépanneuse occupée, zone trop lointaine, heure de nuit), ni le temps perdu avant l'acceptation, qui pèse sur le délai d'arrivée.
4. **La garantie n'est pas reliée au contrat.** GARANTIE est la liste de toutes les garanties de VALMÉRIS, sans lien avec un contrat, et le contrat n'est qu'un groupe de colonnes du bénéficiaire (code du distributeur, référence, date de fin). RG3 rattache chaque garantie à un contrat, et RG4 ouvre le dossier au titre d'une garantie de l'un des contrats du bénéficiaire : rien n'empêche aujourd'hui de choisir une garantie que le contrat ne comporte pas. D'où **environ 5 000 dossiers** (à peu près 1 %) organisés et payés sans être dus.
5. **Un seul contrat par bénéficiaire.** Le contrat étant stocké dans la ligne du bénéficiaire, un bénéficiaire couvert par deux contrats (RG1) est enregistré deux fois : le modèle fabrique des doublons, qui s'ajoutent à ceux des fichiers des distributeurs (annexe 2.2).

Défauts secondaires, acceptés s'ils sont reliés à une règle ; faute de constat dans l'annexe 2.1 C, ils valent au plus 0,5 pt sur les deux items : une seule spécialité par prestataire (RG7) ; zone d'intervention réduite à la commune du dépôt, sans rayon (RG7) ; origine de l'heure d'arrivée absente (RG5).

**Conclusion** : ces anomalies ne sont pas d'abord des erreurs de saisie ; elles viennent de la **structure des données**, qui ne traduit pas les règles de gestion. Le futur logiciel du projet PASSERELLE doit reposer sur un modèle corrigé, faute de quoi la reprise des données reconduira les défauts.

*2.1 b) – Le modèle conceptuel et le modèle logique des données des dossiers et des missions*

**Les cardinalités** (0,5 pt avec les entités) : dans un modèle conceptuel des données, chaque patte d'une association porte une cardinalité minimale et une cardinalité maximale, qui disent combien de fois, au moins et au plus, une occurrence de l'entité participe à l'association (0,1 ; 1,1 ; 0,n ; 1,n). Elles traduisent les règles de gestion : « une mission porte sur une seule spécialité » donne 1,1 du côté de la mission. Le modèle conceptuel est indépendant de toute technique et ne comporte aucune clé étrangère ; le modèle logique le traduit en tables (F07 § 1 à 3).

**Les entités** (identifiant souligné dans la copie, ici en premier) :
- **Beneficiaire** (num_beneficiaire, nom, prenom, telephone) ;
- **Contrat** (num_contrat, ref_distributeur, code_distributeur, date_effet, date_fin) : le code du distributeur est un simple attribut, la liste des distributeurs n'étant pas à modéliser (RG2) ;
- **Garantie** (num_garantie, code_garantie, libelle_garantie, plafond_eur) : la garantie d'un contrat ; son code renvoie à la liste des garanties de VALMÉRIS, qui devient la codification commune (question 2.2) ;
- **Dossier** (num_dossier, date_heure_ouverture, plateau, type_evenement, date_heure_evenement, lieu_evenement) ;
- **Mission** (num_mission, date_heure_creation, date_heure_arrivee, origine_heure_arrivee) : le délai d'arrivée n'est pas stocké, il se calcule à partir des heures enregistrées ;
- **Prestataire** (num_agrement, raison_sociale, telephone, commune_depot, rayon_km) ;
- **Specialite** (code_specialite, libelle_specialite).

**Les associations et leurs cardinalités** (0,5 pt pour les associations hiérarchiques, 0,5 pt pour l'historique des propositions) :

| Association | Entités et cardinalités | Règle de gestion |
|---|---|---|
| *couvrir* | Contrat (1,1) — Beneficiaire (1,n) | RG1 et RG2 : un contrat couvre un seul bénéficiaire ; un bénéficiaire est couvert par un ou plusieurs contrats |
| *comprendre* | Garantie (1,1) — Contrat (1,n) | RG3 : une garantie appartient à un seul contrat ; un contrat en comprend au moins une |
| *etre_ouvert_au_titre_de* | Dossier (1,1) — Garantie (0,n) | RG4 : un dossier est ouvert au titre d'une seule garantie ; une garantie peut n'avoir donné lieu à aucun dossier |
| *donner_lieu* | Mission (1,1) — Dossier (1,n) | RG5 : un dossier donne lieu à au moins une mission ; une mission relève d'un seul dossier |
| *porter_sur* | Mission (1,1) — Specialite (0,n) | RG5 et RG8 : une mission porte sur une seule spécialité |
| *etre_propose* (date_heure_proposition, reponse, date_heure_reponse, motif_refus) | Mission (1,n) — Prestataire (0,n) | RG6 : une mission est proposée à un ou plusieurs prestataires, une fois chacun ; un prestataire nouvellement agréé peut n'avoir reçu aucune proposition ; les dates et heures d'envoi et de réponse, la réponse et le motif dépendent du couple mission-prestataire : ce sont des attributs de l'association |
| *realiser* | Mission (0,1) — Prestataire (0,n) | RG6 : la mission est réalisée par le prestataire qui l'a acceptée, et par aucun tant qu'elle n'est pas acceptée |
| *etre_habilite* | Prestataire (1,n) — Specialite (0,n) | RG7 et RG8 : un prestataire est habilité pour une ou plusieurs spécialités ; une spécialité nouvelle peut n'être exercée par personne |

**L'historique des refus** : chaque proposition, acceptée ou refusée, est une occurrence de l'association *etre_propose*, avec la date et l'heure de son envoi, la réponse, la date et l'heure de cette réponse et le motif : rien n'est plus effacé. On peut alors compter les refus par prestataire, par motif et par zone, et mesurer le temps écoulé entre la création de la mission et son acceptation (heure de la réponse de la proposition acceptée). La réalisation est une association distincte (0,1), car le prestataire qui réalise la mission est le seul qui l'a acceptée.

Le dossier n'est pas relié directement au bénéficiaire : on le retrouve par la garantie, puis le contrat, qui couvre un seul bénéficiaire (RG2). Une association directe serait redondante et permettrait d'ouvrir un dossier pour un bénéficiaire au titre de la garantie d'un autre. Le modèle rend aussi impossible le défaut 4 : un dossier ne peut plus être ouvert qu'au titre d'une garantie qui appartient à un contrat.

**Le modèle logique** (0,5 pt), obtenu par les règles de passage :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire ;
2. pour une association dont l'une des pattes a pour cardinalité maximale 1 (*couvrir*, *comprendre*, *etre_ouvert_au_titre_de*, *donner_lieu*, *porter_sur*, *realiser*), la clé primaire de l'entité du côté « n » migre comme clé étrangère dans la table de l'entité du côté 1 ; elle est obligatoire si la cardinalité minimale est 1, facultative si elle est 0 (le prestataire de la mission, *realiser*) ;
3. une association dont les deux cardinalités maximales sont n (*etre_propose*, *etre_habilite*) devient une table dont la clé primaire est composée des clés des deux entités, chacune clé étrangère, et qui porte les attributs de l'association.

- Beneficiaire (<u>num_beneficiaire</u>, nom, prenom, telephone)
- Contrat (<u>num_contrat</u>, ref_distributeur, code_distributeur, date_effet, date_fin, #num_beneficiaire)
- Garantie (<u>num_garantie</u>, code_garantie, libelle_garantie, plafond_eur, #num_contrat)
- Dossier (<u>num_dossier</u>, date_heure_ouverture, plateau, type_evenement, date_heure_evenement, lieu_evenement, #num_garantie)
- Mission (<u>num_mission</u>, date_heure_creation, date_heure_arrivee, origine_heure_arrivee, #num_dossier, #code_specialite, #num_agrement)
- Prestataire (<u>num_agrement</u>, raison_sociale, telephone, commune_depot, rayon_km)
- Specialite (<u>code_specialite</u>, libelle_specialite)
- Proposition (<u>#num_mission, #num_agrement</u>, date_heure_proposition, reponse, date_heure_reponse, motif_refus)
- Habilitation (<u>#num_agrement, #code_specialite</u>)

La clé composée de Proposition traduit la règle « un même prestataire ne reçoit qu'une proposition pour une mission donnée ». Le numéro d'agrément de Mission est vide tant que la mission n'est pas acceptée. Deux contrôles relèvent du modèle physique ou du logiciel, et non du modèle logique : le prestataire qui réalise la mission doit être celui qui l'a acceptée, et il doit être habilité pour la spécialité de la mission.

**Réponses tolérées**
- Formalisme différent (notation « pattes de corbeau », schéma relationnel dessiné), s'il est lisible et cohérent (`JUR-T10`).
- Garantie modélisée comme une liste commune de garanties, reliée au contrat par une association n:m porteuse du plafond, si le candidat montre comment le dossier reste rattaché à une garantie du contrat (association vers le couple contrat-garantie, ou contrôle explicite).
- Contrat couvrant plusieurs bénéficiaires (association n:m) et association directe entre le dossier et le bénéficiaire, si l'hypothèse est écrite et la redondance discutée.
- Prestataire retenu déduit de la proposition acceptée, sans association *realiser*, si le candidat énonce la contrainte d'une seule acceptation par mission.
- Entité Partenaire ou Distributeur ajoutée, ou zone d'intervention modélisée à part, si le candidat la justifie, malgré RG2.

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dessinées dans le modèle conceptuel, ou modèle logique qui ne découle pas du modèle conceptuel.
- *Mission et dossier confondus* — une seule entité Dossier qui reçoit le prestataire et les heures : c'est le défaut de l'annexe 2.1 B reproduit.
- *Refus perdus* — association mission-prestataire 1:n (le seul prestataire retenu), sans les propositions refusées ni leurs attributs ; ou attributs de la proposition placés dans la table Mission.
- *Garantie flottante* — garantie sans lien avec le contrat, qui laisse possible l'ouverture d'un dossier au titre d'une garantie non souscrite.
- *Morceau de cours ou requête hors attente* (`JUR-T01`, `JUR-T07`) — règles de passage récitées sans les appliquer, ou requêtes écrites alors que la question n'en demande pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, modèle logique, modèle physique ; cardinalités ; règles de passage | définitions et méthode | F07 § 1 à 4 | notion de cours |

---

### 2.2 – Les échanges de données avec les distributeurs, les constructeurs et les prestataires (2,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) », sans détail des échanges techniques ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ». L'interopérabilité est traitée sur le plan technique et sur le plan organisationnel, comme le demande le programme.

**Annexes mobilisées** : annexes 1.1 (quinze distributeurs, deux constructeurs, application des prestataires, progiciel de règlement, organigramme), 2.1 (doublons créés par le modèle), 2.2 (flux, anomalies, définitions, responsabilités) et 2.6 (RGPD : exactitude des données ; DAMA-DMBOK).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Interopérabilité et qualité des données définies ; premier problème rattaché à un niveau d'interopérabilité et à une dimension de la qualité, avec sa conséquence chiffrée | 0,5 |
| a-2 | Deux autres problèmes, chacun rattaché à un niveau et à une dimension, avec sa conséquence | 0,5 |
| b-1 | Formats ouverts et interfaces de programmation : canal cible pour chaque flux, en temps réel quand le service l'exige | 0,5 |
| b-2 | Codification commune des garanties et dictionnaire des données défini et appliqué aux trois notions de l'annexe 2.2 C | 0,5 |
| b-3 | Contrôles à l'entrée (format, code, doublon, rejet tracé) et responsabilités : propriétaire et intendant des données des partenaires, engagements de qualité dans les conventions de distribution | 0,5 |

**Réponse attendue**

*2.2 a) – Trois problèmes d'interopérabilité et de qualité*

**Définitions** (0,5 pt avec le premier problème) : l'**interopérabilité** est la capacité de systèmes et d'organisations hétérogènes à échanger des données et à les utiliser sans intervention manuelle. Elle se joue à quatre niveaux : **technique** (canaux, interfaces de programmation), **syntaxique** (formats : XML, JSON, fichiers à séparateurs), **sémantique** (même sens des données : dictionnaire, codifications communes) et **organisationnel** (processus, responsabilités, engagements entre partenaires) (F07 § 7). La **qualité des données** est leur aptitude à servir l'usage prévu ; elle se mesure selon des dimensions : exactitude, complétude, unicité, cohérence, actualité (fraîcheur) (F07 § 8.3).

Trois problèmes parmi les suivants (0,5 pt pour le premier avec les définitions, 0,5 pt pour les deux autres) :

| Problème (annexe 2.2) | Niveau d'interopérabilité | Dimension de la qualité | Conséquence |
|---|---|---|---|
| **Codes de garanties propres à chaque distributeur et dates sous trois formes** : 1 200 codes pour 40 garanties, traduits à la main ; 3 % de codes inconnus ou mal traduits ; 15 000 dates de fin erronées | sémantique (même garantie, codes différents) et syntaxique (formats de date et de fichier) | exactitude, cohérence | une garantie refusée à un bénéficiaire couvert, ou accordée à tort (les 5 000 dossiers hors contrat de l'annexe 2.1 en sont en partie la suite) ; deux informaticiens mobilisés pour tenir la table de correspondance |
| **Bénéficiaires en double et introuvables** : 300 000 doublons (un sur vingt), 26 000 dossiers ouverts « sous réserve » (5 %) ; « bénéficiaire » n'a pas le même sens pour tous les distributeurs | sémantique (définition du bénéficiaire) et organisationnel (fichier en retard ou rejeté, sans engagement du distributeur) | unicité, actualité, complétude | pour le bénéficiaire en détresse, cinq minutes d'appel en plus et un doute sur sa prise en charge ; pour les plateaux, plus de 2 000 heures d'appel perdues (26 000 × 5 minutes) ; des statistiques par bénéficiaire faussées |
| **Ruptures de la chaîne et ressaisies** : environ 30 000 alertes des constructeurs reçues par interface de programmation mais transmises par courriel et ressaisies ; acceptations et heures d'arrivée renvoyées une fois par nuit, refus restés dans l'application ; 700 000 factures en PDF ou sur papier ressaisies par 25 agents, dont 4 % avec une erreur | technique (le logiciel des dossiers ne sait pas lire les alertes ni recevoir les événements en temps réel) et syntaxique (factures non structurées) | actualité, exactitude | impossible d'informer le bénéficiaire en temps réel ni de déclencher l'assistance sans appel, deux objectifs d'« Assister 2030 » ; erreurs de règlement et réclamations des prestataires ; temps des agents absorbé par la saisie |
| **Absence de dictionnaire et de responsable** : « délai d'arrivée » et « dossier clos » définis autrement selon les plateaux ou les directions ; aucune direction responsable des données reçues ; conventions de distribution sans clause de qualité | sémantique et organisationnel | cohérence | des indicateurs incomparables entre plateaux (question 2.3) ; la DSI corrige chaque nuit les fichiers des autres, sans que la cause soit traitée à la source |

*2.2 b) – L'organisation cible des échanges en quatre mesures*

1. **Des formats ouverts et des interfaces de programmation** (0,5 pt). Une **interface de programmation** (API) est un point d'accès normalisé et documenté par lequel un système met à disposition ou reçoit des données d'un autre, selon un contrat d'interface (données échangées, versions, sécurité) ; un **format ouvert** est un format dont la spécification est publique et qui ne dépend d'aucun éditeur. Appliqué aux flux de VALMÉRIS :
   - contrats et bénéficiaires : un **format d'échange unique**, ouvert et publié par VALMÉRIS (par exemple un fichier XML ou JSON décrit par un schéma), imposé aux quinze distributeurs à la place des neuf formes actuelles ; une interface de programmation pour les distributeurs qui le peuvent, afin qu'un contrat souscrit dans la journée soit connu le jour même ;
   - alertes des véhicules connectés : intégration directe dans le futur logiciel des dossiers (projet PASSERELLE), qui ouvre le dossier sans ressaisie ; un format d'alerte commun, proposé aux deux constructeurs puis aux autres partenaires ;
   - application des prestataires : échange des acceptations, des refus et des positions **en temps réel** par interface de programmation, et non plus par un fichier de nuit, condition de l'information du bénéficiaire en temps réel ;
   - factures : facture structurée déposée dans l'application et rattachée à la mission, au lieu du PDF et du papier ressaisis.
2. **Une codification commune des garanties et un dictionnaire des données** (0,5 pt). La liste des 40 garanties de VALMÉRIS devient la **codification de référence** : chaque distributeur transmet ce code, et non plus le sien, ce qui supprime la table de correspondance de 1 200 codes. Le **dictionnaire des données** décrit chaque donnée échangée : nom, définition, format, valeurs admises, règle de calcul, source, propriétaire. Il tranche les trois notions de l'annexe 2.2 C :
   - *bénéficiaire* : la personne couverte, nommément désignée dans le contrat ;
   - *délai d'arrivée* : durée entre l'ouverture du dossier et l'arrivée géolocalisée du prestataire, la même sur les trois plateaux ;
   - *dossier clos* : fin de la dernière mission, la date de paiement de la dernière facture étant une autre donnée.
   Le DAMA-DMBOK range ces travaux dans les domaines de l'intégration et de l'interopérabilité, des métadonnées et des données de référence (annexe 2.6).
3. **Des contrôles à l'entrée des données** (0,5 pt avec la quatrième mesure). Chaque fichier ou message reçu est contrôlé avant chargement :
   - format des dates et des champs obligatoires ;
   - code de garantie existant dans la codification ;
   - cohérence des dates d'effet et de fin ;
   - rapprochement des bénéficiaires déjà connus selon une règle d'identité écrite (nom, prénom, téléphone, contrat), pour ne pas créer de doublon.
   Les enregistrements rejetés sont renvoyés au distributeur, avec le motif et un délai de correction, et inscrits dans un journal des rejets ; un taux de rejet est suivi par distributeur. L'exactitude des données est d'ailleurs un principe que rappelle le RGPD (annexe 2.6).
4. **Des responsabilités sur les données reçues des partenaires.** Un **propriétaire** métier des données des contrats et des bénéficiaires est désigné, par exemple le service des relations avec les partenaires, qui négocie les conventions de distribution ; un **intendant** (responsable des données des partenaires) tient le dictionnaire et la codification, suit la qualité par distributeur et anime la correction à la source avec les distributeurs et la DSI. Les conventions de distribution comprennent un **engagement de qualité** : format, fréquence, délai de transmission, taux d'erreur maximal et circuit de correction. La DSI exploite les échanges mais ne corrige plus seule les fichiers des autres.

**Réponses tolérées**
- Autres problèmes tirés de l'annexe 2.2 (neuf formes de fichiers, partenaires sans alertes), s'ils sont rattachés à un niveau et à une dimension.
- Niveau d'interopérabilité rattaché autrement, s'il est justifié (dates : syntaxique ou sémantique).
- Plateforme d'échange ou bus d'échange proposés comme canal unique entre les distributeurs et le logiciel des dossiers, sans détail technique.
- Données de référence des garanties présentées comme un petit référentiel, si le rôle des distributeurs est précisé.
- Responsable des données des partenaires rattaché à la DSI, si le propriétaire métier est distinct.

**Erreurs fréquentes**
- *Interopérabilité réduite à la technique* (`ET-36`) — « mettre des API » sans codification commune, sans dictionnaire ni responsabilités.
- *Détail technique hors attente* (`JUR-T07`) — description des échanges techniques, des schémas ou des mécanismes d'authentification, que la question exclut.
- *Qualité sans mesure* — problèmes énoncés sans les chiffres de l'annexe (un sur vingt, 5 %, 3 %, 4 %) ni leur conséquence pour le bénéficiaire.
- *Correction en aval seulement* — nettoyage nocturne renforcé, au lieu de la correction à la source et des engagements des distributeurs.
- *Morceau de cours* (`JUR-T01`) — niveaux d'interopérabilité et dimensions de la qualité récités sans application aux flux de VALMÉRIS.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines intégration et interopérabilité, métadonnées, données de référence, qualité | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | exactitude des données (annexe 2.6) | `rgpd` / F15 | en vigueur |
| Interopérabilité et ses quatre niveaux, interface de programmation, format ouvert, dictionnaire des données, dimensions de la qualité, propriétaire et intendant | définitions et méthode | F07 § 1, 7, 8.1 et 8.3 | notion de cours |

---

### 2.3 – Les délais d'arrivée des prestataires (3,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Aucun calcul statistique ni aucune manipulation d'outil ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexes 2.3 (indicateurs par plateau, missions par zone, affirmation du directeur des plateaux, limites) et 2.2 C (définition du délai propre à Valence) ; « Assister 2030 » (présentation).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Analyses descriptive et exploratoire définies et distinguées ; démarche justifiée par l'annexe 2.3 (descriptive d'abord, exploratoire ensuite) | 0,5 |
| a-2 | Premier constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| a-3 | Deuxième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| a-4 | Troisième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-1 | Affirmation appréciée : structure des zones, définition du délai, heures saisies à la main, satisfaction, objectif mal lu ; conclusion nuancée | 0,5 |
| b-2 | Effets pervers de la prime ; deux évolutions de la chaîne de traitement (collecte, nettoyage, structuration) qui rendent la comparaison juste | 0,5 |
| c-1 | Deux représentations adaptées au comité de direction, chacune justifiée par son message et par le piège évité | 0,5 |

**Réponse attendue**

*2.3 a) – La démarche et trois constats*

**La démarche** (0,5 pt) : l'**analyse descriptive** résume ce qui s'est passé (niveaux, évolutions, répartitions, écarts à un objectif) ; l'**analyse exploratoire** croise les données, sans hypothèse arrêtée, pour repérer des profils, des valeurs atypiques et des pistes d'explication ; elle prépare les explications sans les démontrer (F08 § 2). On retient :
- l'**analyse descriptive d'abord** : le comité de direction veut savoir où en sont les délais en 2026 par rapport à 2025 et à l'objectif de − 20 % d'ici 2029 ;
- puis l'**analyse exploratoire**, parce que l'annexe signale des facteurs qui brouillent la comparaison (météo, zones, mode de saisie, définition du délai) : il faut croiser les délais avec la saison, le type de zone, l'origine de l'heure d'arrivée et les refus avant d'en tirer un jugement sur les plateaux.

**Trois constats** parmi les suivants (0,5 pt chacun : le fait chiffré, son interprétation au regard d'« Assister 2030 », la précaution de lecture) :

1. **La légère baisse du délai moyen en 2026 tient à l'hiver doux.** Le délai moyen de l'ensemble passe de 50 à 48 minutes ; mais pendant les trois mois d'hiver, il tombe de 60 à 52 minutes, et de mars à novembre il reste à 47 minutes les deux années. Aucun progrès durable n'est donc acquis ; l'objectif de − 20 % (environ 38 minutes en 2029 si l'on part de 48) reste entier, et un hiver rigoureux le ferait remonter. *Précaution* : deux années seulement, et une base de 2026 favorable : l'année de référence de l'objectif doit être fixée et corrigée de la météo.
2. **La moyenne cache une queue de délais longs, surtout à Metz.** Sur chaque plateau, la moyenne dépasse la médiane (Limoges 47 contre 38, Metz 56 contre 42, Valence 38 contre 30) : quelques attentes très longues, en zone rurale (74 minutes en moyenne, contre 32 en ville), tirent la moyenne vers le haut. Près d'un quart des arrivées (23 %) dépassent encore 60 minutes, 30 % à Metz : ce sont elles qui exposent le bénéficiaire immobilisé au bord d'une route et qui font les réclamations. *Précaution* : on ne peut pas combiner les médianes des plateaux pour obtenir celle de l'ensemble ; il faudrait la distribution des délais par classes.
3. **La dégradation de Metz est d'abord un effet de structure.** Metz passe de 50 à 56 minutes, de 24 % à 30 % d'arrivées au-delà d'une heure et de 82 % à 74 % de satisfaits, alors que sa part de missions rurales passe de 25 % à 40 % avec les quatre départements reçus de Limoges. À zone égale, ses délais (34, 50 et 76 minutes) ne dépassent ceux de Limoges que de 2 à 4 minutes ; avec sa répartition de 2025, son délai moyen tournerait autour de 50 minutes, comme en 2025. En revanche, ses refus bondissent (20 % à 28 %) : le réseau de prestataires y est trop peu dense. *Précaution* : les délais par zone de 2025 ne sont pas donnés ; c'est une hypothèse à vérifier, qui oriente l'action vers le réseau, non vers les chargés de Metz.
4. **Les délais de Valence sont les moins fiables.** Valence affiche les délais les plus courts (38 minutes), mais 70 % de ses heures d'arrivée sont saisies à la main par le prestataire (30 % à 35 % ailleurs), son délai est compté depuis l'acceptation de la mission, une dizaine de minutes après l'ouverture du dossier (annexe 2.2 C), et ses bénéficiaires ne sont pas plus satisfaits du délai (79 % contre 83 % à Limoges). *Précaution* : la satisfaction repose sur 15 % de répondants, qui ne sont pas forcément représentatifs ; l'écart de satisfaction est un signal, pas une preuve.
5. **Les refus augmentent** (18 % à 20 % pour l'ensemble) : chaque refus retarde l'arrivée. Le délai d'acceptation, non mesuré aujourd'hui, est une piste d'amélioration du délai total. *Précaution* : les refus sont lus dans l'application des prestataires, sans motif (annexe 2.1 C).

*2.3 b) – L'affirmation et la proposition du directeur des plateaux*

**L'affirmation de M. CORTHELAY** (0,5 pt) : « Valence est notre meilleur plateau » n'est pas démontré, pour quatre raisons :
- **un effet de structure** : 70 % des missions de Valence sont urbaines, contre 40 % à Limoges et 30 % à Metz. À zone égale et selon sa propre mesure, Valence n'a d'avance qu'en ville (30 minutes contre 32 et 34), et cette avance de 2 à 4 minutes est inférieure à la dizaine de minutes que lui retire sa définition du délai ; il est moins rapide que Limoges en zone périurbaine (48 contre 46) et rurale (74 contre 72). Avec la répartition de Limoges, son délai serait d'environ 47 minutes, comme celui de Limoges : la comparaison des moyennes globales est trompeuse (paradoxe de Simpson) ;
- **une définition différente** : compté depuis l'acceptation, et non depuis l'ouverture du dossier, le délai de Valence est raccourci d'une dizaine de minutes ; à définition commune, il serait de l'ordre de 48 minutes ;
- **une mesure déclarative** : 70 % des heures de Valence sont saisies par le prestataire lui-même, sans contrôle, et la satisfaction de ses bénéficiaires n'est pas meilleure qu'ailleurs ;
- **une lecture erronée de l'objectif** : la cible d'environ 38 minutes vaut pour l'ensemble de VALMÉRIS, à partir de sa base de 2026 ; un plateau urbain qui affiche 38 minutes selon sa propre mesure ne l'« atteint » pas. Retenir le seul chiffre qui conforte sa conviction relève du **biais de confirmation**.

Conclusion : à mesure commune, rien n'indique que Valence soit le plus rapide, même en ville ; il serait plutôt le plus lent. On ne peut ni le classer premier, ni en faire le modèle des autres plateaux, tant que la définition et la mesure ne sont pas communes.

**La prime et la chaîne de traitement** (0,5 pt) : une prime liée au délai moyen, calculé sur des heures saisies à la main et selon des règles propres à chaque plateau, inciterait à **embellir la mesure** plutôt qu'à réduire le délai réel. Elle pénaliserait Metz, qui a reçu des zones rurales, et pousserait à délaisser les missions lointaines. Une prime éventuelle ne se conçoit qu'après la fiabilisation de la mesure, sur un indicateur comparé à zone égale.

Deux évolutions de la chaîne de traitement, parmi :
- **collecte** : heure d'arrivée relevée par la géolocalisation de l'application, la saisie manuelle devenant l'exception justifiée ; heure d'ouverture du dossier, heure de création de la mission et heures d'envoi et de réponse de chaque proposition, donc heure d'acceptation, enregistrées pour chaque mission (modèle de la question 2.1) ; type de zone rattaché à chaque mission ;
- **nettoyage** : marquage de l'origine de chaque heure (géolocalisée ou déclarée) ; repérage des valeurs impossibles (arrivée avant la création de la mission, délai nul) et des valeurs aberrantes, vérifiées plutôt que supprimées ; dédoublonnage des missions ;
- **structuration** : une seule définition du délai d'arrivée, écrite dans le dictionnaire (de l'ouverture du dossier à l'arrivée géolocalisée), et des dimensions communes (plateau, type de zone, mois et saison, spécialité, origine de l'heure), pour comparer les plateaux **à zone et à saison égales**, avec la médiane et la part au-delà de 60 minutes à côté de la moyenne.

*2.3 c) – Deux représentations pour le comité de direction*

Deux représentations parmi (0,5 pt) :
- **Barres groupées du délai médian et de la part des arrivées au-delà de 60 minutes, par plateau et par type de zone.** *Message* : à zone égale, les plateaux sont proches ; les écarts tiennent surtout à la part des zones rurales. *Piège évité* : la moyenne globale par plateau, qui mêle des structures de zones différentes (effet de structure).
- **Courbe mensuelle du délai d'arrivée sur 2025 et 2026**, les mois d'hiver signalés, avec la trajectoire de l'objectif de 2029 tracée depuis l'année de référence. *Message* : la baisse de 2026 vient de l'hiver ; hors hiver, rien n'a changé. *Piège évité* : l'extrapolation d'une année douce et la comparaison de deux chiffres annuels.
- **Histogramme de la distribution des délais**, par classes de 15 minutes, par plateau. *Message* : la queue des attentes longues, que la moyenne et la médiane ne montrent pas. *Piège évité* : la moyenne seule, qui masque la dispersion.
- **Barres empilées à 100 % de l'origine des heures d'arrivée** (géolocalisée ou déclarée), par plateau, à côté des délais. *Message* : la fiabilité de la mesure diffère d'un plateau à l'autre. *Piège évité* : comparer des mesures de fiabilité inégale comme si elles se valaient.

Un classement des trois plateaux sur leur seul délai moyen, ou un histogramme à l'axe tronqué qui grossit l'écart entre Valence et Metz, sont de mauvais choix.

**Réponses tolérées**
- Analyse diagnostique présentée comme une variante de l'analyse exploratoire ; analyse prédictive écartée faute d'historique suffisant.
- Autres constats tirés de l'annexe 2.3 (satisfaction stable pour l'ensemble, hausse des refus à Metz), s'ils sont chiffrés et assortis d'une précaution.
- Effet de structure démontré par la lecture du tableau B sans le calcul de « 47 minutes », qui n'est pas attendu.
- Effets de la zone et de la définition croisés (environ 40 minutes en ville, à définition commune), sans calcul détaillé.
- Évolutions de la chaîne de traitement portant sur l'analyse ou la restitution, si elles rendent la comparaison juste.
- Autres représentations (carte des délais médians par département, petits multiples par plateau, jauge de l'objectif), si le message et le piège évité sont précisés.

**Erreurs fréquentes**
- *Corrélation présentée comme une causalité* (`ET-26`) — délais de Valence attribués à son organisation, sans examiner les zones, la définition du délai et la saisie à la main.
- *Prudence d'interprétation oubliée* (`JUR-D06`) — amélioration de 2026 lue comme un progrès durable, malgré l'hiver doux ; objectif jugé atteint par un plateau.
- *Calcul hors attente* (`JUR-T07`) — moyennes pondérées recalculées en détail ou tests statistiques, alors que la question demande des constats argumentés en chiffres ronds.
- *Moyenne et médiane confondues* — médianes des plateaux additionnées ou moyennées pour obtenir celle de l'ensemble.
- *Morceau de cours* (`JUR-T01`) — définitions des méthodes d'analyse sans application aux plateaux et aux années de l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Analyses descriptive et exploratoire, chaîne de traitement, choix des graphiques, biais de confirmation, effet de structure et paradoxe de Simpson, corrélation et causalité | définitions et méthode | F08 § 1, 2 et 5 | notion de cours |
| Dictionnaire des données, dimensions d'analyse | structuration | F07 § 1 et 6 | notion de cours |

---

### 2.4 – Le registre commun des missions (2 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ». Le fonctionnement est expliqué en principe, sans développement du registre ni du contrat automatisé ; aucun cryptoactif ni jeton, aucune analyse juridique.

**Annexes mobilisées** : annexes 1.1 (3 400 prestataires, progiciel de règlement, application des prestataires), 2.3 (heures d'arrivée saisies à la main), 2.4 (proposition du consortium, coûts, contestations, objections de la DSI, plateforme centralisée) et 2.6 (RGPD, ISO 22739:2024).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Registre partagé répliqué entre les cinq nœuds, blocs chaînés par des empreintes (inaltérabilité pratique), consensus entre membres identifiés | 0,5 |
| a-2 | Clés privée et publique, signature de chaque inscription ; contrat automatisé (« si … alors », règlement en euros) ; différence avec une base de données centralisée | 0,5 |
| b-1 | Valeur ajoutée appliquée (preuve partagée, contestations, paiement rapide) et coûts sur trois ans : 1 000 k€ contre 450 k€ | 0,5 |
| b-2 | Trois limites tirées des annexes (oracle, données personnelles, gouvernance, périmètre, intégration) ; avis motivé et conditions | 0,5 |

**Réponse attendue**

*2.4 a) – Le fonctionnement du registre proposé*

Un **registre distribué** est un registre d'opérations dont chaque participant détient une copie, mise à jour selon une règle de consensus, sans administrateur central unique ; une **chaîne de blocs** est un registre distribué où les opérations sont regroupées en blocs chaînés (F11 § 1 ; vocabulaire de l'ISO 22739:2024, annexe 2.6). Appliqué au projet :
- **un registre partagé** (0,5 pt avec les blocs et le consensus) : les cinq membres (trois assisteurs, deux fédérations) exploitent chacun un nœud qui détient une copie complète du registre ; chacun peut vérifier ce que les autres ont inscrit ;
- **des blocs chaînés par des empreintes** : chaque bloc contient l'empreinte (le résultat du hachage) du bloc précédent. Modifier une mission ou une facture déjà inscrite changerait l'empreinte de son bloc et romprait la chaîne, ce que les autres nœuds verraient aussitôt : le registre est **pratiquement inaltérable** et horodaté, sans l'être absolument (trois membres sur cinq qui s'entendraient pourraient réécrire la chaîne) ;
- **un consensus entre membres identifiés** : un bloc n'est ajouté qu'avec l'accord d'au moins trois des cinq nœuds. C'est une chaîne **privée et permissionnée**, dite de consortium : seuls des membres admis valident, sans minage ; la consommation d'énergie est donc faible, contrairement aux chaînes publiques à preuve de travail ;
- **des clés et des signatures** (0,5 pt avec le contrat automatisé et la distinction) : chaque membre et chaque dépanneur détient une **clé privée**, secrète, avec laquelle il signe ses inscriptions, et une **clé publique**, connue de tous, qui permet de vérifier la signature. On sait ainsi qui a inscrit quoi, et l'auteur ne peut pas le nier : l'assisteur sa mission, le dépanneur son arrivée et sa facture ;
- **un contrat automatisé** (contrat intelligent) : un programme inscrit dans le registre exécute une règle « si … alors » : si la fin de l'intervention est inscrite et si la facture respecte le barème, alors l'ordre de virement est émis. Le règlement se fait **en euros**, par le circuit bancaire habituel de l'assisteur, sans jeton ni cryptoactif.

**La différence avec une base de données centralisée** : une base centralisée, même répartie sur plusieurs serveurs, est tenue par un seul administrateur, qui peut corriger ou supprimer une donnée ; ceux qui la consultent doivent lui faire confiance. Le registre distribué organise la confiance entre des acteurs qui ne se font pas confiance, ici des assisteurs concurrents et des dépanneurs, par la réplication, le consensus et l'inaltérabilité, au prix de la performance, du coût et de la souplesse.

*2.4 b) – Valeur ajoutée, coûts, limites et avis*

**La valeur ajoutée et les coûts** (0,5 pt) :
- *valeur ajoutée* : une **version unique des faits**, horodatée et signée, partagée entre l'assisteur et le dépanneur, qui peut réduire les contestations (15 000 factures en 2026, soit 5 %, qui occupent dix agents, environ 500 k€ par an) ; un **paiement en 48 heures**, argument fort pour attirer et garder les meilleurs dépanneurs ; un seul outil pour les dépanneurs qui travaillent avec plusieurs assisteurs ;
- *coûts sur trois ans, de tête* : registre : 300 (construction) + 250 (raccordement) + 3 × 150 (fonctionnement) = **1 000 k€** ; plateforme centralisée : 300 + 3 × 50 = **450 k€**, soit **550 k€ d'écart**. Or la plateforme apporte l'essentiel du même gain : facture rattachée à la mission, contrôlée par rapport au barème et aux heures géolocalisées, payée sous dix jours, pour tous les prestataires et non pour les seuls dépanneurs.

**Les limites et l'avis** (0,5 pt), en trois limites parmi :
- **le problème de l'oracle** : le registre garantit que l'inscription n'a pas changé, pas qu'elle est vraie. Les contestations portent sur l'heure d'arrivée, la distance et la majoration de nuit ; si l'heure est saisie à la main (38 % des heures en 2026, 70 % à Valence), elle sera inscrite à la main « pour toujours ». C'est la fiabilité de la donnée à la source (géolocalisation) qui réduit les litiges ;
- **les données personnelles** : nom, téléphone, immatriculation, lieu et photos des véhicules seraient copiés chez deux concurrents et ne pourraient plus être effacés, ce qui heurte la minimisation et la limitation de la durée de conservation (annexe 2.6). Il faudrait n'inscrire qu'une **empreinte** des missions et garder les données elles-mêmes hors du registre. S'y ajoute la confidentialité des barèmes face aux concurrents ;
- **la gouvernance du consortium** : décisions à la majorité de cinq membres, dont deux fédérations de dépanneurs, qui pourraient imposer des barèmes à VALMÉRIS ; rien n'est prévu en cas de désaccord, de sortie d'un membre ou d'erreur du contrat automatisé ;
- **le périmètre** : environ 600 des 1 400 dépanneurs du réseau, soit moins de la moitié, et aucune autre spécialité (serruriers, plombiers, aide à domicile) : VALMÉRIS devrait de toute façon tenir un second circuit ;
- **l'intégration** : le raccordement à l'ancien logiciel serait à refaire avec la solution du projet PASSERELLE ;
- **l'automatisme** : un contrat automatisé qui paie une facture inexacte, parce que la donnée inscrite est fausse, rend l'erreur plus difficile à reprendre ; ses règles évoluent lentement, à la majorité des membres.

**Avis motivé** : ne pas adhérer au consortium en 2027. Le problème de VALMÉRIS n'est pas un manque de confiance entre acteurs qu'aucun tiers ne pourrait arbitrer : VALMÉRIS commande et paie ses missions, et peut être lui-même le tiers de confiance de ses échanges. Le problème est la qualité des données à la source. La plateforme centralisée y répond pour 450 k€ sur trois ans, pour tous les prestataires. VALMÉRIS peut rester observateur du consortium et réexaminer le projet après la bascule de PASSERELLE, à des conditions écrites :
- seules des empreintes des missions sont inscrites, les données personnelles restant hors du registre ;
- une charte de gouvernance fixe le vote, les barèmes propres à chaque assisteur, la sortie et le traitement des erreurs ;
- les heures inscrites sont géolocalisées ;
- les coûts sont partagés selon l'usage.

**Réponses tolérées**
- Adhésion conditionnelle au consortium, si les conditions (empreintes seulement, gouvernance, géolocalisation, intégration après PASSERELLE) sont posées et si le coût est comparé à celui de la plateforme.
- Coût sur trois ans qui ajoute aux deux solutions une part de temps interne, si l'hypothèse est écrite.
- Grille d'opportunité (plusieurs acteurs écrivent-ils ? se font-ils confiance ? faut-il une preuve inaltérable ? les données sont-elles partageables ?) appliquée au cas à la place de la liste des limites.
- Consensus décrit comme un vote entre membres ou comme une validation par autorité, sans nom d'algorithme.

**Erreurs fréquentes**
- *Blockchain confondue avec une base de données distribuée* (`ET-08`) — registre présenté comme une simple base partagée, ou inaltérabilité présentée comme absolue.
- *Opportunités sans limites* (`ET-19`) — confiance et fin des litiges reprises du consortium sans examiner l'oracle, les données personnelles et la gouvernance.
- *Cryptoactifs hors sujet* — jetons, règlement sur les marchés de cryptoactifs ou monnaie numérique invoqués, alors que le projet règle en euros, sans jeton.
- *Développement hors attente* (`JUR-T07`) — algorithme de hachage, code du contrat automatisé ou choix d'une technologie détaillés.
- *Avis sans comparaison* — recommandation qui ne confronte pas les 1 000 k€ du registre aux 450 k€ de la plateforme centralisée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO 22739:2024, vocabulaire des chaînes de blocs et des registres distribués (2e édition) | termes : registre distribué, bloc, nœud, consensus, contrat intelligent ; norme de vocabulaire, non d'exigences | `iso_22739_2024` / F11 § 3.4 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | minimisation et limitation de la conservation face à l'inaltérabilité du registre (annexe 2.6) | `rgpd` / F11 § 2.3 ; F15 | en vigueur |
| Registre distribué, typologie (publique, privée, de consortium), consensus, clés, oracle, grille d'opportunité, limites | fonctionnement et appréciation | F11 § 1 et 2 | notion de cours |

---

### 2.5 – Le coût du système d'information des dossiers et son pilotage (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI » (coût complet, inducteurs, imputation aux activités) ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ». Total de tête en sommes rondes ; aucun calcul actualisé, aucune répartition chiffrée exigée.

**Annexes mobilisées** : annexes 1.1 (520 000 dossiers et leur répartition, 22 M€ de dépenses du SI), 2.3 (part des arrivées au-delà de 60 minutes, heures géolocalisées) et 2.5 (coûts de 2026, dossiers par type, tableau de bord actuel).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Inducteur de coût défini ; 10 400 k€ / 520 000 dossiers = 20 € par dossier et par an | 0,5 |
| a-2 | Deux arguments tirés de l'annexe 2.5 qui montrent la limite du coût moyen unique (appels, missions, durée de suivi, appels sans dossier) | 0,5 |
| b-1 | Indicateur de coût complet, avec ses cinq champs et le risque surveillé | 0,5 |
| b-2 | Indicateur de qualité du service complet, avec ses cinq champs et le risque surveillé ; équilibre avec les appels reçus | 0,5 |

**Réponse attendue**

*2.5 a) – Le coût par dossier et ses limites*

**L'inducteur de coût** (0,5 pt avec le calcul) : un **inducteur** est une grandeur mesurable dont la variation explique celle du coût d'une ressource ou d'une activité, et qui sert à imputer ce coût aux produits ou aux services qui la consomment : nombre d'appels, de missions, de dossiers, durée de suivi (F09 § 2).

**Le calcul, de tête** : 2 400 + 3 200 + 700 + 1 100 + 400 + 2 600 = **10 400 k€** par an, soit près de la moitié des 22 M€ de dépenses du SI ; pour 520 000 dossiers : 10 400 000 € / 520 000 = **20 € par dossier et par an**.

**La limite d'un coût moyen unique** (0,5 pt), en deux arguments parmi :
- **la téléphonie, premier poste (3 200 k€, près d'un tiers du total), est facturée selon le nombre d'appels**, qui varie de 4 par dossier d'habitation à 9 par dossier d'aide aux personnes : un dossier d'aide aux personnes consomme plus de deux fois plus de téléphonie qu'un dossier d'habitation ;
- **l'application des prestataires est facturée selon le nombre de missions**, de 1 par dossier d'habitation à 1,5 par dossier automobile ;
- **la durée de suivi** va d'un jour pour un dossier automobile à quinze jours pour un dossier d'aide aux personnes, qui sollicite davantage le logiciel, le support et les chargés ;
- **environ 100 000 appels ne donnent lieu à aucun dossier** : leur coût est réparti sur les dossiers, alors qu'il relève de l'information des assurés ;
- la **part des autres coûts de la DSI** (2 600 k€) est une répartition, et non une consommation mesurée.

Le coût moyen de 20 € mélange donc des dossiers qui ne consomment pas les mêmes ressources. Il ne permet ni de connaître le coût d'une garantie proposée à un distributeur, ni de mesurer l'économie d'un dossier ouvert sans appel par une alerte de véhicule connecté. Il faut **imputer chaque poste par son inducteur** (appels, missions, dossiers et durée de suivi), selon la logique de la méthode à base d'activités, en principe. À titre d'illustration, non attendue : à 1 € par appel et 1 € par mission, le reste valant 12,5 € par dossier, on obtiendrait environ 20 € pour un dossier automobile, 17,5 € pour un dossier d'habitation et 23 € pour un dossier d'aide aux personnes, avant même de tenir compte de la durée de suivi.

*2.5 b) – Deux indicateurs pour le comité de direction*

Le tableau de bord actuel ne mesure que l'**activité** (appels reçus). Les deux indicateurs proposés y ajoutent le **coût** et la **qualité du service**, chacun associé à un **risque**, pour équilibrer le pilotage comme le demande M. MARVÉJOL (0,5 pt par indicateur complet) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Coût du système d'information des dossiers par dossier, par type de dossier** | coûts annuels du SI des dossiers répartis selon leurs inducteurs (appels pour la téléphonie, missions pour l'application, dossiers et durée de suivi pour le reste) / nombre de dossiers de chaque type | comptabilité analytique (direction administrative et financière), téléphonie en ligne (appels), logiciel des dossiers (dossiers, missions, durée de suivi) | trimestrielle, sur douze mois glissants | coût moyen au plus 20 € par dossier jusqu'à la bascule de PASSERELLE (niveau de 2026), écart entre types expliqué par les inducteurs | financier |
| **Part des arrivées au-delà de 60 minutes, mesurées par géolocalisation** | missions dont l'arrivée géolocalisée intervient plus de 60 minutes après l'ouverture du dossier / missions dont l'heure d'arrivée est géolocalisée × 100 | application des prestataires (heure géolocalisée) et logiciel des dossiers (heure d'ouverture, plateau, zone) | mensuelle, par plateau et par type de zone | au plus 15 % en 2029 (23 % en 2026 selon les relevés actuels), avec au moins 90 % d'heures géolocalisées | client |

**Les risques surveillés** : le premier suit la **dérive des coûts** du SI des dossiers, notamment de la téléphonie, et montre si les dossiers ouverts sans appel ou en ligne réduisent effectivement le coût. Le second mesure le **risque pour le bénéficiaire** : une attente longue, parfois de nuit au bord d'une route, est la première source de réclamations et menace la relation avec les distributeurs. Il repose sur une mesure fiable et commune aux plateaux, ce qui évite les biais relevés à la question 2.3. Il est lu par plateau et par type de zone, pour ne pas pénaliser Metz. Présentés à côté des appels reçus, avec leur tendance et leur cible, ils relient l'activité, le coût et le service rendu.

**Réponses tolérées**
- Coût moyen de 20 € retenu comme indicateur, si le candidat annonce sa décomposition par type.
- Autres arguments tirés de l'annexe 2.5 (part des autres coûts de la DSI imputée par convention, appels sans dossier), s'ils sont expliqués.
- À la place de l'indicateur de qualité du service : délai médian d'arrivée géolocalisé (médiane des durées entre l'ouverture du dossier et l'arrivée géolocalisée ; application et logiciel des dossiers ; mensuelle, par plateau et par zone ; baisse de 20 % entre 2026 et 2029 à définition constante ; axe client). Comme indicateur de risque supplémentaire : taux de dossiers ouverts sous réserve (dossiers ouverts pour un bénéficiaire introuvable / dossiers ouverts × 100 ; logiciel des dossiers ; mensuelle, par distributeur ; au plus 1 % fin 2028, 5 % en 2026 ; axe processus), ou part des missions refusées au moins une fois (missions refusées au moins une fois / missions × 100 ; table des propositions ; mensuelle, par plateau et par zone ; au plus 15 % fin 2028, 20 % en 2026 ; axe processus).

**Erreurs fréquentes**
- *Coût complet réduit à un poste* (`ET-33`) — seul le logiciel interne (2 400 k€) retenu, en oubliant la téléphonie, qui pèse davantage.
- *Calcul hors attente* (`JUR-T07`) — répartition détaillée par type ou calcul actualisé, alors que la question demande un coût par dossier de tête et des arguments.
- *Indicateur incomplet ou générique* (`ET-18`, `JUR-A02`) — « suivre la satisfaction » sans formule, source, fréquence, cible ni axe, ou indicateur de délai moyen calculé sur des heures déclaratives.
- *Indicateurs qui doublent le tableau actuel* — nombre d'appels par chargé ou taux de décroché, qui mesurent encore l'activité sans le coût ni le service rendu.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Contrôle de gestion du SI : coût complet, inducteurs, imputation aux activités (méthode à base d'activités en principe) | définition et calcul de tête | F09 § 2 et 3.1 | notion de cours |
| Indicateur à cinq champs, équilibre performance, risque et coût, axes du tableau de bord prospectif | deux indicateurs du comité de direction | F08 § 3 ; F09 § 4 | notion de cours |
