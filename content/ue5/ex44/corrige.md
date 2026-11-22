# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 44 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 architecture, urbanisation et cloud, F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F13 intelligence artificielle, F15 RGPD opérationnel, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle des données exécuté, indicateurs, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le modèle des données du réseau, des sessions et des tarifs | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 3 |
| 2.2 Les échanges de données avec les plateformes d'itinérance, le logiciel des interventions et les sites hôtes | `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `1.3.c` Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle | 2 |
| 2.3 L'utilisation et la disponibilité des points | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 4 |
| 2.4 La valeur des données et leur hébergement | `2.3.f` Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques ; `2.3.e` Aspects réglementaires (RGPD, archivage légal) et monétisation des données ; `2.3.d` Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique | 4 |
| **Dossier 2 – Organiser, exploiter et valoriser les données de recharge** |  | **13** |

Répartition indicative : connaissances (modèles conceptuel et logique, cardinalités et règles de passage, interopérabilité, chaîne de traitement, analyses descriptive et prédictive, informatique décisionnelle comme démarche, patrimoine informationnel, principes du RGPD, piliers du cloud de confiance, indicateur à cinq champs) environ 2,5 points (la moitié des items 2.1 b-1, 2.1 b-4, 2.2 a-1, 2.2 b-2, 2.3 a-1, 2.3 c-1, 2.3 d-1, 2.4 a-1, 2.4 b-1 et 2.4 c-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le modèle des données du réseau, des sessions et des tarifs (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) » ; `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ». Modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites ; modèle physique seulement nommé ; aucune requête.

**Annexes mobilisées** : annexe 2.1 (règles de gestion, extrait du modèle logique actuel, précisions du responsable des données, constats de 2026) ; annexe 1.1 (bornes d'un à quatre points, quatre constructeurs, paiement des sessions).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux défauts du modèle actuel, chacun rapporté à une règle de gestion et au constat de l'annexe 2.1 C qu'il explique | 0,5 |
| a-2 | Troisième défaut, rapporté à une règle et à un constat ; conclusion : les anomalies viennent de la structure des données | 0,5 |
| b-1 | Modèle conceptuel et modèle logique distingués ; sept entités avec identifiant et attributs élémentaires (site, borne, point, connecteur, session, tarif, opérateur de mobilité) | 0,5 |
| b-2 | Associations hiérarchiques et cardinalités justifiées par les règles : site, borne, point, connecteur, session | 0,5 |
| b-3 | Historique des tarifs : un tarif par point, tranche et période de validité, jamais écrasé, et session facturée selon un tarif (1,1) ; opérateur de mobilité rattaché à la session (0,1) | 0,5 |
| b-4 | Modèle logique de sept tables déduit par les règles de passage énoncées (clé étrangère côté 1,1 ou 0,1, obligatoire ou facultative ; table à clé composée pour une association n:m, absente ici) | 0,5 |

**Réponse attendue**

*2.1 a) – Trois défauts du modèle logique actuel*

Trois défauts parmi les suivants (0,5 pt pour deux défauts, 0,5 pt pour le troisième et la conclusion), chacun rapporté à une règle de gestion et au constat qu'il explique :

1. **Une borne n'a qu'un point.** La table BORNE confond la borne physique et le point de recharge : une borne à quatre points est enregistrée quatre fois (1234-A à 1234-D), avec le même numéro de série. Or RG2 identifie la borne par son numéro de série et RG3 lui donne d'un à quatre points, chacun identifié par un identifiant unique. D'où **8 000 « bornes » pour environ 3 600 bornes physiques** : le logiciel de gestion des interventions, qui suit les bornes physiques, ne se rapproche de CIRCÉA que par une table tenue à la main (annexe 2.2), et une demande d'intervention sur vingt-cinq vise un mauvais point.
2. **Le tarif est un texte dans la session.** Le champ « tarif » de SESSION est un libellé recopié ou saisi, et non une clé étrangère vers un tarif, alors que RG9 facture chaque session selon un tarif déterminé, décrit par RG8. D'où **environ 60 libellés différents** et **3 % de sessions sans tarif** : on ne sait ni analyser les sessions selon leur tarif, ni relier une session au prix en vigueur.
3. **L'historique des tarifs n'est pas conservé.** TARIF n'a qu'une ligne par « borne », écrasée à chaque changement, avec deux prix fixes (jour et nuit), alors que RG8 prévoit un tarif par point et par tranche horaire, et un nouveau tarif à chaque changement de prix, les tarifs passés étant conservés. Sur les **600 points du pilote**, dont les prix changent jusqu'à six fois par jour, personne ne peut dire quel tarif s'appliquait un jour donné. La généralisation de la tarification variable en 2027 étendra le problème à tout le réseau.
4. **L'opérateur de mobilité n'est pas relié à la session.** Le moyen de paiement n'est qu'un mot (« itinérance »), sans lien avec l'opérateur, alors que RG6 et RG7 rattachent la session payée par badge à l'opérateur qui l'a émis. Pour les **1,6 million de sessions d'itinérance** (40 % des 4 millions), l'équipe données rapproche chaque mois à la main les relevés des deux plateformes pour quelque 200 opérateurs ; la direction du développement du réseau ne sait pas ce que lui apporte chaque opérateur.
5. **Les connecteurs sont des colonnes répétées et la session ne désigne pas son connecteur.** BORNE porte deux colonnes « type_connecteur », alors que RG4 fait du connecteur un objet identifié et RG5 déroule la session sur un connecteur : les pannes d'un connecteur ne peuvent pas être reliées aux sessions échouées.

**Conclusion** : ces anomalies ne sont pas d'abord des erreurs de saisie ; elles viennent de la **structure des données**, qui ne traduit pas les règles de gestion. Le modèle corrigé est la condition de la cohérence des échanges (question 2.2) et des analyses (question 2.3).

*2.1 b) – Le modèle conceptuel et le modèle logique des données*

**Modèle conceptuel et modèle logique** (0,5 pt avec les entités) : le **modèle conceptuel des données** représente les objets de gestion (entités, avec leur identifiant et leurs attributs), leurs liens (associations) et les **cardinalités** minimale et maximale de chaque patte, qui traduisent les règles de gestion, indépendamment de toute technique ; il ne comporte aucune clé étrangère. Le **modèle logique** le traduit en tables, avec clés primaires et clés étrangères, selon les règles de passage ; le modèle physique l'implante ensuite dans un système de gestion de base de données (F07 § 1 à 4).

**Les entités** (identifiant souligné dans la copie, ici en premier) :
- **Site** (num_site, nom_site, adresse, commune, type_site, code_proprietaire) : le code du propriétaire est un simple attribut, la liste des propriétaires n'étant pas à modéliser (RG1) ;
- **Borne** (num_serie, ref_modele, constructeur, date_mise_service) : le modèle et le constructeur sont des attributs (RG2) ;
- **Point** (id_point, categorie, puissance_kw) : l'identifiant unique du point, qui servira aux échanges (question 2.2) ;
- **Connecteur** (num_connecteur, type_connecteur) ;
- **Session** (num_session, date_heure_debut, duree_min, energie_kwh, type_moyen, ref_moyen) : le moyen de paiement est décrit par son type et sa référence ; pour la carte bancaire, la référence est le jeton remis par la banque, jamais le numéro de la carte (RG6), ce qui limite les données conservées au nécessaire ;
- **Tarif** (id_tarif, heure_debut, heure_fin, prix_kwh, prix_minute, date_debut_validite, date_fin_validite) ;
- **OperateurMobilite** (code_operateur, raison_sociale, plateforme_itinerance).

**Les associations et leurs cardinalités** (0,5 pt pour les associations hiérarchiques, 0,5 pt pour le tarif et l'opérateur) :

| Association | Entités et cardinalités | Règle de gestion |
|---|---|---|
| *etre_installee* | Borne (1,1) — Site (1,n) | RG1 et RG2 : une borne est installée sur un seul site ; un site porte une ou plusieurs bornes |
| *porter* | Point (1,1) — Borne (1,n) | RG3 : un point appartient à une seule borne ; une borne porte au moins un point (au plus quatre : contrôle du logiciel, une cardinalité ne dit que 1 ou n) |
| *equiper* | Connecteur (1,1) — Point (1,n) | RG4 : un connecteur appartient à un seul point ; un point a un ou deux connecteurs |
| *se_derouler* | Session (1,1) — Connecteur (0,n) | RG5 : une session se déroule sur un seul connecteur ; un connecteur peut n'avoir servi à aucune session |
| *s_appliquer* | Tarif (1,1) — Point (0,n) | RG8 : un tarif s'applique à un seul point ; un point porte plusieurs tarifs (un par tranche et par période), aucun s'il n'est pas ouvert à la vente |
| *etre_facturee_selon* | Session (1,1) — Tarif (0,n) | RG9 : une session est facturée selon un seul tarif ; un tarif peut n'avoir servi à aucune session |
| *etre_apportee_par* | Session (0,1) — OperateurMobilite (0,n) | RG6 et RG7 : une session payée par badge est rattachée à un seul opérateur, les autres à aucun ; un opérateur nouvellement relié peut n'avoir apporté aucune session |

**L'historique des tarifs** : un tarif n'est plus une ligne par point que l'on écrase, mais une occurrence de l'entité Tarif pour un point, une tranche horaire et une **période de validité** (dates de début et de fin). Chaque changement de prix ferme le tarif en cours (date de fin renseignée) et crée un nouveau tarif ; le tarif en vigueur est celui dont la date de fin est vide. Comme chaque session est reliée au tarif appliqué (*etre_facturee_selon*), on peut dire quel prix s'appliquait à un point un jour donné et analyser les sessions par tarif, y compris sous la tarification variable. L'association *etre_apportee_par* (0,1) donne enfin, sans rapprochement manuel, les sessions apportées par chaque opérateur et par chaque plateforme.

Deux contrôles relèvent du logiciel, et non du modèle : le tarif d'une session doit s'appliquer au point dont relève son connecteur, et à l'heure de son début ; une session n'est rattachée à un opérateur que si son moyen de paiement est un badge.

**Le modèle logique** (0,5 pt), obtenu par les règles de passage :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire ;
2. pour une association dont l'une des pattes a pour cardinalité maximale 1 (ici, les sept associations), la clé primaire de l'entité du côté « n » migre comme clé étrangère dans la table de l'entité du côté 1 ; elle est obligatoire si la cardinalité minimale est 1, facultative si elle est 0 (l'opérateur de la session) ;
3. une association dont les deux cardinalités maximales sont n deviendrait une table dont la clé primaire est composée des clés des deux entités ; le modèle n'en comporte pas.

- Site (<u>num_site</u>, nom_site, adresse, commune, type_site, code_proprietaire)
- Borne (<u>num_serie</u>, ref_modele, constructeur, date_mise_service, #num_site)
- Point (<u>id_point</u>, categorie, puissance_kw, #num_serie)
- Connecteur (<u>num_connecteur</u>, type_connecteur, #id_point)
- Tarif (<u>id_tarif</u>, heure_debut, heure_fin, prix_kwh, prix_minute, date_debut_validite, date_fin_validite, #id_point)
- Session (<u>num_session</u>, date_heure_debut, duree_min, energie_kwh, type_moyen, ref_moyen, #num_connecteur, #id_tarif, #code_operateur)
- OperateurMobilite (<u>code_operateur</u>, raison_sociale, plateforme_itinerance)

Le code de l'opérateur est vide pour une session payée par l'application ou par carte bancaire. La table Point remplace les « bornes » 1234-A à 1234-D : la borne physique 1234 n'existe plus qu'une fois.

**Réponses tolérées**
- Formalisme différent (notation « pattes de corbeau », schéma relationnel dessiné), s'il est lisible et cohérent (`JUR-T10`).
- Moyen de paiement modélisé comme une entité (compte, badge, carte), reliée à la session (1,1) et, pour le badge, à l'opérateur (0,1), si les données conservées restent limitées (jeton pour la carte).
- Grille de tarifs commune à plusieurs points, reliée aux points par une association n:m porteuse des dates de validité, si le candidat montre comment la session reste reliée au tarif appliqué.
- Entités Propriétaire, Modèle de borne, Constructeur ou Plateforme ajoutées, si elles sont justifiées, malgré RG1 et RG2.
- Tranche horaire modélisée à part, si l'historique reste porté par les dates de validité.

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dessinées dans le modèle conceptuel, ou modèle logique qui ne découle pas du modèle conceptuel.
- *Défaut reproduit* — une seule entité Borne qui reçoit la puissance et les connecteurs, ou un attribut « tarif » dans la session : c'est le modèle de l'annexe 2.1 B.
- *Historique perdu* — tarif sans dates de validité, ou tarif mis à jour au lieu d'être fermé et remplacé ; session sans lien avec le tarif appliqué.
- *Opérateur obligatoire* — cardinalité 1,1 entre la session et l'opérateur, alors que 60 % des sessions sont payées par l'application ou par carte.
- *Morceau de cours ou requête hors attente* (`JUR-T01`, `JUR-T07`) — règles de passage récitées sans les appliquer, ou requêtes écrites alors que la question n'en demande pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, modèle logique, modèle physique ; cardinalités ; règles de passage | définitions et méthode | F07 § 1 à 4 | notion de cours |

---

### 2.2 – Les échanges de données avec les plateformes d'itinérance, le logiciel des interventions et les sites hôtes (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) », sans détail des échanges techniques.
- §1.3 – Urbanisation et architecture : `1.3.c` « Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle ». L'interopérabilité est traitée sur le plan technique et sur le plan organisationnel, comme le demande le programme.

**Annexes mobilisées** : annexes 1.1 (deux plateformes d'itinérance, 40 % des sessions, logiciel de gestion des interventions, services aux sites hôtes), 2.1 (borne confondue avec le point) et 2.2 (échanges, mots sans définition commune, courriel de l'opérateur de mobilité).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Interopérabilité définie, sur les plans technique et organisationnel, entre organisations ; premier problème, chiffré, avec ses conséquences pour les acteurs | 0,5 |
| a-2 | Deux autres problèmes, chiffrés, avec leurs conséquences pour les conducteurs, les opérateurs de mobilité ou les sites hôtes | 0,5 |
| b-1 | Identifiant unique du point attribué par CIRCÉA et repris partout ; statuts et tarifs normalisés par un dictionnaire des données appliqué aux mots de l'annexe 2.2 B | 0,5 |
| b-2 | Interfaces de programmation et formats ouverts par échange ; règles de cohérence (source de référence, concordance, contrat d'interface) ; un indicateur à cinq champs | 0,5 |

**Réponse attendue**

*2.2 a) – Trois problèmes d'échange et leurs conséquences*

**Définition** (0,5 pt avec le premier problème) : l'**interopérabilité** est la capacité de systèmes et d'organisations hétérogènes à échanger des données et à les utiliser sans intervention manuelle. Elle a un versant **technique** (canaux, interfaces de programmation, formats) et un versant **organisationnel** (définitions communes, processus, responsabilités, engagements entre partenaires) (F07 § 7). Pour AMPÉRANE, elle est **inter-organisationnelle** : CIRCÉA n'est qu'un maillon d'une chaîne qui relie deux plateformes d'itinérance, quelque 200 opérateurs de mobilité et leurs applications, les sept entreprises de maintenance qui partagent le logiciel des interventions, et 1 200 sites hôtes. La cohérence de cet ensemble ne dépend pas d'un seul système (F03 § 3).

Trois problèmes parmi les suivants (0,5 pt pour le premier avec la définition, 0,5 pt pour les deux autres) :

| Problème (annexe 2.2) | Cause | Conséquences |
|---|---|---|
| **Des statuts publiés en retard et traduits différemment** : environ **un statut affiché sur dix** périmé ou faux en janvier 2027 | envoi groupé toutes les quinze minutes ; neuf états dans CIRCÉA, quatre et trois chez les plateformes ; « en maintenance » transmis comme « disponible » à la plateforme B ; « disponible » sans définition commune | **conducteurs** : déplacement vers un point en panne ou occupé, parfois avec une batterie presque vide ; **opérateurs de mobilité** : clients mécontents, qui s'en prennent à eux ; l'opérateur qui apporte 8 % des sessions d'itinérance menace de ne plus mettre le réseau en avant ; **AMPÉRANE** : sessions perdues et disponibilité perçue bien inférieure à l'objectif de 98 % |
| **Des tarifs affichés différents des tarifs facturés** : environ **une session d'itinérance sur quatre** sur les points du pilote, une sur cinquante ailleurs ; un tiers des réclamations sur l'itinérance portent sur le prix | un fichier par semaine, un seul prix par point : ni les tranches horaires ni les changements en cours de semaine ne sont transmis | **conducteurs** : prix non annoncé, perte de confiance ; **opérateurs** : écart entre ce qu'ils ont affiché et ce qu'AMPÉRANE leur facture, contestations ; **AMPÉRANE** : la généralisation de la tarification variable en 2027 étendra ces écarts du pilote à tout le réseau si l'échange ne change pas |
| **Des identifiants de points différents dans chaque système** : environ **5 %** des points mal rapprochés, **une demande d'intervention sur vingt-cinq** sur un mauvais point | CIRCÉA désigne une « borne » virtuelle, le logiciel des interventions une position sur une borne physique, chaque plateforme son propre identifiant ; table de correspondance tenue à la main (défaut du modèle, question 2.1) | **conducteurs** : statut publié sur le mauvais point ; **entreprises de maintenance et techniciens** : déplacement pour rien, panne prolongée ; **AMPÉRANE** : deux personnes occupées à tenir la table, disponibilité réelle dégradée |
| **Une intervention close qui ne remet pas le point en service** : en moyenne **une demi-journée** de plus « hors service » | clôture non transmise du logiciel des interventions à CIRCÉA ; remise en service à la main | **conducteurs** : un point réparé affiché indisponible ; **AMPÉRANE** : disponibilité perdue sans panne réelle, à chaque intervention |
| **Des rapports mensuels aux sites hôtes en tableur, aux colonnes variables** | tableur envoyé vers le 10 du mois suivant, préparé à la main | **sites hôtes** : données tardives, impossibles à intégrer ; l'enseigne propriétaire de 300 sites demande des données quotidiennes en format ouvert ; **AMPÉRANE** : risque sur les services aux sites hôtes (10 M€ de chiffre d'affaires) |

*2.2 b) – L'organisation cible des échanges en quatre mesures*

1. **Un identifiant unique du point** (0,5 pt avec la deuxième mesure). Chaque point reçoit, à sa déclaration dans CIRCÉA, un identifiant unique (entité Point de la question 2.1), qui ne change plus. Le logiciel des interventions le reprend (borne physique par son numéro de série, point par son identifiant) et les plateformes l'affichent au lieu de composer le leur : la table de correspondance disparaît. Le **référentiel des points** devient une donnée de référence partagée, dont CIRCÉA est la seule source, avec un propriétaire (direction de l'exploitation et de la maintenance) et un intendant à l'équipe données : dans une logique d'urbanisation, ce référentiel est un bloc commun aux applications, et non une copie par application (F03 § 1 ; DAMA-DMBOK, données de référence).
2. **Des statuts et des tarifs normalisés.** Un **dictionnaire des données**, commun à CIRCÉA, au logiciel des interventions, au service clients et aux plateformes, définit chaque donnée échangée (nom, définition, format, valeurs admises, source, propriétaire). Il tranche les mots de l'annexe 2.2 B :
   - *session* : un branchement qui a délivré de l'énergie ; une tentative de moins de deux minutes sans énergie est une tentative échouée, et non une session ;
   - *disponible* : un conducteur peut y démarrer une recharge maintenant ;
   - *point* : l'emplacement de recharge identifié par son identifiant unique.
   Il fixe aussi une **liste commune de statuts** (par exemple disponible, occupé, hors service, en maintenance), à laquelle chacun des neuf états de CIRCÉA est rattaché, « en maintenance » ne valant jamais « disponible », et la **structure du tarif** publié : tranche horaire, prix par kilowattheure et par minute, dates de validité, comme dans le modèle de la question 2.1.
3. **Des interfaces de programmation et des formats ouverts** (0,5 pt avec la quatrième mesure). Une **interface de programmation** est un point d'accès documenté par lequel un système met des données à disposition d'un autre ou en reçoit, selon un contrat d'interface ; un **format ouvert** a une spécification publique, indépendante d'un éditeur (F07 § 7). Appliqués aux échanges :
   - statuts : publiés par interface de programmation à chaque changement d'état, et non par lot toutes les quinze minutes ;
   - tarifs : publiés à chaque changement, avant leur entrée en vigueur, avec leurs tranches et leurs dates ;
   - interventions : demande créée à partir de l'alerte de CIRCÉA et clôture renvoyée à CIRCÉA, qui remet le point en service sans ressaisie ;
   - sites hôtes : données quotidiennes mises à disposition dans un format ouvert, ou par interface de programmation pour l'enseigne qui les intègre à son outil, à la place du tableur mensuel.
4. **Des règles de cohérence entre CIRCÉA, le logiciel des interventions et les plateformes** :
   - CIRCÉA est la **source de référence** du statut et du tarif de chaque point ; les autres systèmes ne les modifient pas ;
   - un point qui fait l'objet d'une intervention ouverte ne peut être publié « disponible » ;
   - le tarif affiché par l'opérateur et le tarif facturé portent le même identifiant de tarif et la même période de validité ;
   - une comparaison automatique quotidienne des trois systèmes signale tout écart à l'intendant ;
   - un **contrat d'interface** avec chaque plateforme fixe les données, les définitions, le délai de publication, le traitement des écarts et les responsables. C'est le versant organisationnel, sans lequel les interfaces ne suffisent pas.

**Indicateur de suivi** :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des statuts affichés conformes à l'état du point | contrôles où le statut affiché par la plateforme correspond à l'état du point dans CIRCÉA et dans le logiciel des interventions / contrôles réalisés × 100 | comparaison automatique de CIRCÉA, du logiciel des interventions et des statuts publiés par les deux plateformes | quotidienne, présentée chaque mois par plateforme | au moins 99 % fin 2027 (environ 90 % en janvier 2027) | client |

**Réponses tolérées**
- Analyse des problèmes rattachée aux niveaux d'interopérabilité (technique, syntaxique, sémantique, organisationnel), si les conséquences pour les acteurs sont précisées.
- Autres problèmes tirés de l'annexe 2.2 (absence de dictionnaire, intervention close non transmise, rapports aux sites hôtes), s'ils sont chiffrés ou datés.
- Plateforme d'échange ou bus d'intégration présentés comme point de passage unique des échanges, sans détail technique.
- Référentiel des points confié à la direction technique, si un propriétaire métier est nommé.
- Autre indicateur à cinq champs : part des sessions d'itinérance dont le prix affiché correspond au tarif facturé ; délai de publication d'un changement de statut ; part des points rapprochés par leur identifiant unique.

**Erreurs fréquentes**
- *Interopérabilité réduite à la technique* (`ET-36`) — « mettre des interfaces de programmation » sans identifiant commun, sans dictionnaire, sans règles ni responsabilités.
- *Détail technique hors attente* (`JUR-T07`) — description des messages, des schémas ou des mécanismes d'authentification, que la question exclut.
- *Conséquences non contextualisées* (`JUR-T01`) — problèmes énoncés sans les chiffres de l'annexe (un sur dix, un sur quatre, 5 %, un sur vingt-cinq) ni leurs effets pour les conducteurs, les opérateurs et les sites hôtes.
- *Correction en aval seulement* — table de correspondance mieux tenue, au lieu de l'identifiant unique attribué à la source.
- *Indicateur incomplet* (`ET-18`) — indicateur sans formule, source, fréquence, cible ou axe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | intégration et interopérabilité, données de référence, métadonnées | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Interopérabilité, interface de programmation, format ouvert, dictionnaire des données, données de référence, urbanisation, cohérence inter-organisationnelle | définitions et méthode | F03 § 1 et 3 ; F07 § 1, 7 et 8.1 | notion de cours |

---

### 2.3 – L'utilisation et la disponibilité des points (4 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.d` « Outils décisionnels : Excel avancé, Power BI, Tableau, etc. » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Limites : aucun calcul statistique, aucune manipulation d'outil, aucun développement d'algorithme ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexe 2.3 (indicateurs par type de site et par puissance, affirmation de la directrice du développement du réseau, limites, modèle de prévision, modes de restitution) ; annexes 2.1 et 2.2 (définitions de la session et de la disponibilité) ; « AMPÉRANE 2030 » (présentation).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Étapes de la chaîne présentées ; collecte et nettoyage de l'indicateur de disponibilité, chacun avec son biais tiré de l'annexe | 0,5 |
| a-2 | Structuration, analyse et restitution, chacune avec son biais ; conclusion : disponibilité déclarée, non constatée | 0,5 |
| b-1 | Deux constats argumentés et chiffrés, avec leur portée pour « AMPÉRANE 2030 » | 0,5 |
| b-2 | Troisième constat argumenté et chiffré | 0,5 |
| b-3 | Affirmation appréciée (effet de structure, sessions courtes et échouées, disponibilité déclarée et constatée, critère retenu) ; conclusion nuancée sur la proposition | 0,5 |
| c-1 | Analyses descriptive et prédictive distinguées ; usage du modèle justifié par le cas | 0,5 |
| c-2 | Deux limites, dont celle des données d'apprentissage ; façon d'en tenir compte dans la décision | 0,5 |
| d-1 | Choix du mode de restitution par deux critères explicités, informatique décisionnelle traitée comme une démarche ; représentation pour les sites hôtes justifiée par son message | 0,5 |

**Réponse attendue**

*2.3 a) – La chaîne de traitement de l'indicateur de disponibilité et ses biais*

**La chaîne de traitement** (0,5 pt avec les deux premières étapes) transforme des données brutes en information utile à la décision : **collecte** des données à leur source, **nettoyage** (doublons, valeurs manquantes, aberrantes ou invalides), **structuration** (règles de gestion et de calcul, rapprochements, stockage historisé, par exemple dans un entrepôt de données), **analyse**, puis **restitution** aux décideurs (F08 § 1). Chaque étape peut introduire un biais que la suivante ne corrige pas. Pour l'indicateur de disponibilité présenté chaque mois au comité de direction :

| Étape | Ce qui se passe aujourd'hui | Biais tiré de l'annexe 2.3 |
|---|---|---|
| **Collecte** | CIRCÉA enregistre l'état que chaque borne lui déclare | **mesure déclarative** : une borne qui répond mais ne charge pas reste « disponible » ; les signalements des conducteurs, collectés par le service clients, ne sont rattachés qu'au site |
| **Nettoyage** | aucun contrôle des états manquants ni de cohérence | quand la liaison est perdue, CIRCÉA garde le dernier état connu : une valeur manquante est remplacée sans le dire, le plus souvent par « disponible » ; aucun contrôle de cohérence avec les signalements (rapprochés à la main, une fois par an) ni avec les sessions échouées ou de moins de deux minutes, comptées comme réussies (7 % du réseau, 15 % des aires de services) ; les « bornes » virtuelles compliquent le rapprochement avec le point (annexe 2.1) |
| **Structuration** | règle de calcul : temps en état de fonctionner / temps de référence | les heures de maintenance programmée sont retirées du temps de référence, deux fois plus pour les bornes rapides : la disponibilité des points rapides, donc des aires de services, est flattée ; la règle n'est écrite dans aucun dictionnaire (annexe 2.2 B) |
| **Analyse** | moyenne de tous les points | la moyenne masque la dispersion, alors que l'objectif d'« AMPÉRANE 2030 » vise 98 % **par point** ; elle mêle les points ouverts dans l'année et les plus anciens |
| **Restitution** | un seul chiffre par mois au comité de direction | sans distribution, sans écart à la cible par point, sans comparaison avec les signalements : le comité lit 97 % et ne voit pas que 35 % des signalements de panne portent sur des points déclarés disponibles |

**Conclusion** (0,5 pt avec les trois dernières étapes) : l'indicateur publié mesure une **disponibilité déclarée par les bornes**, flatteuse, et non la **disponibilité constatée par les conducteurs**. Piloter l'objectif de 98 % par point suppose de rapprocher, point par point, les états de CIRCÉA, les sessions échouées ou très courtes, les signalements et les interventions, avec une définition écrite.

*2.3 b) – Trois constats et l'affirmation de Mme ESCARDINE*

**Trois constats** parmi les suivants (0,5 pt pour deux constats, 0,5 pt pour le troisième : le fait chiffré, son interprétation et sa portée pour « AMPÉRANE 2030 ») :

1. **Les sessions par point dépendent d'abord de la puissance.** Un point rapide fait environ 3,0 sessions par jour, un point normal 0,8. Or 83 % des points des aires de services sont rapides (1 000 sur 1 200), contre 29 % dans les supermarchés (1 200 sur 4 200) et 10 % au plus ailleurs. À puissance égale, les aires de services font à peine mieux que les supermarchés pour les points rapides (3,2 contre 3,0) et moins bien pour les points normaux (0,6 contre 0,8) : l'écart de 2,8 contre 1,4 est un **effet de structure**.
2. **La baisse des supermarchés vient des ouvertures.** Les supermarchés passent de 1,5 à 1,4 session par point et par jour, mais ils ont reçu 700 des 900 points ouverts en 2026, qui mettent environ un an à atteindre leur utilisation normale : à parc constant, rien n'indique une dégradation. La croissance vers 20 000 points reproduira cet effet chaque année.
3. **La disponibilité progresse sur le papier, pas pour les conducteurs.** La disponibilité mesurée passe de 96 % à 97 %, mais la part des signalements de panne reçus alors que CIRCÉA indiquait le point disponible monte de 30 % à 35 %, et de 40 % à 50 % aux aires de services, qui affichent pourtant la meilleure disponibilité (98 %). Les aires ont aussi le plus de sessions échouées (7 % puis 9 %) et de sessions de moins de deux minutes (15 %, contre 5 % dans les supermarchés).
4. **Le « meilleur » site dépend du critère.** Les hôtels et restaurants (24 %) et les parkings de collectivités et d'entreprises (20 %) ont les taux d'occupation les plus élevés, les aires de services et les supermarchés les plus faibles (6 % et 5 %) : des recharges longues, la nuit ou pendant la journée de travail, contre des recharges courtes sur la route. Le nombre de sessions ne dit ni l'énergie vendue, ni les recettes, ni le service rendu aux conducteurs qui ne peuvent pas recharger chez eux.

**L'affirmation de Mme ESCARDINE** (0,5 pt) : « les aires de services sont nos meilleurs sites » n'est pas démontré :
- l'avantage en sessions par point est un **effet de structure** : il tient à la part des points rapides, non à la qualité des sites ; à puissance égale, l'écart disparaît presque ;
- ce chiffre est **gonflé par les sessions courtes** : 15 % des sessions des aires durent moins de deux minutes, souvent des démarrages relancés, comptés comme des sessions réussies ; hors sessions courtes, les points rapides des aires feraient à peu près autant, voire un peu moins, que ceux des supermarchés, dont une partie vient d'ouvrir ;
- la « meilleure disponibilité » est la plus **déclarative** : maintenance programmée retirée du calcul, deux fois plus pour les bornes rapides, et la moitié des signalements de panne des aires portent sur des points que CIRCÉA disait disponibles ;
- le **critère** est contestable : ni l'énergie, ni les recettes, ni l'occupation ne sont considérées. Retenir le seul chiffre qui conforte une conviction relève du **biais de confirmation** (F08 § 5).

Conclusion : les aires de services sont de bons emplacements pour la recharge rapide, mais l'annexe ne permet pas de les dire « meilleures ». Leur réserver l'essentiel des ouvertures de 2027 serait prématuré : il faut comparer les sites à puissance égale, hors sessions courtes, sur la disponibilité constatée et sur l'énergie ou les recettes, puis décider site par site (question c). Les ouvertures doivent aussi servir l'objectif de recharge « accessible à tous ».

*2.3 c) – Le modèle de prévision des sites candidats*

**Les deux analyses** (0,5 pt avec la justification) : l'**analyse descriptive** résume ce qui s'est passé (niveaux, évolutions, répartitions, écarts à une cible : c'est celle des tableaux A et B) ; l'**analyse prédictive** estime ce qui se passera, à partir des régularités observées dans des données passées, par exemple au moyen d'un modèle d'apprentissage automatique, qui apprend des données pour prévoir ou classer, à distinguer de l'IA générative (F08 § 2 ; F13). À l'examen, on en interprète les résultats et on en discute la fiabilité ; on ne la construit pas.

**Pourquoi l'utiliser ici** : pour passer de 8 000 à 20 000 points en 2030, AMPÉRANE doit trier de nombreux sites candidats (300 aujourd'hui) avant d'engager des études de terrain et des travaux coûteux. Le modèle combine de façon homogène plusieurs variables qu'aucun analyste ne pondère de tête (trafic, véhicules électriques de la commune, durée de stationnement, commerces, type de site, puissance), donne à chaque site une prévision comparable et objective le premier tri ; vérifié sur 200 sites mis de côté, il prévoit à moins de 20 % près pour sept sites sur dix.

**Deux limites** parmi (0,5 pt avec la façon d'en tenir compte) :
- **les données d'apprentissage se limitent aux sites existants** : le modèle a appris sur des sites qu'AMPÉRANE a elle-même choisis et qui ont été ouverts (biais de sélection). Il est sans repère pour les 80 parkings de gares et de centres de loisirs, types qu'AMPÉRANE n'exploite pas : leur prévision est une extrapolation hors du domaine appris ;
- **la variable prévue reproduit les biais de la mesure** : les sessions par point comptent les sessions de moins de deux minutes et mêlent points rapides et normaux. Le modèle apprend donc l'effet de structure et le gonflement des aires de services, ce que montre son résultat : 45 des 60 sites de priorité 1 sont des aires de services, soit 45 des 50 aires candidates ;
- **le passé ne dit pas l'avenir** : tarification variable généralisée en 2027, croissance du parc de véhicules électriques, ouverture de bornes concurrentes à proximité, variable absente du modèle ;
- **la fiabilité et l'explication sont limitées** : la prévision s'écarte de plus de 20 % pour trois sites sur dix, et le modèle « ne dit pas pourquoi un site est classé premier ».

**En tenir compte dans la décision** : le modèle sert à **classer pour étudier**, non à décider ; la direction du développement du réseau garde la décision, après une étude de terrain des sites de tête. L'équipe données corrige la variable prévue (sessions de plus de deux minutes, ou énergie délivrée, ou recettes, par puissance), traite à part les types de sites absents des données d'apprentissage (étude de terrain, voire site pilote), indique les principales variables qui expliquent chaque classement et compare, un an après l'ouverture, la prévision à la réalité pour corriger le modèle.

*2.3 d) – Le mode de restitution et une représentation pour les sites hôtes*

**Le choix** (0,5 pt avec la représentation), par deux critères parmi :
- **la fiabilité et la cohérence des chiffres** : aujourd'hui chaque direction retravaille les tableaux dans ses tableurs, avec ses définitions ; un libre-service sans définitions communes produirait « dix disponibilités différentes » ;
- **la réactivité et l'autonomie des utilisateurs** : 60 demandes en attente, rapports des sites hôtes reçus vers le 10 du mois suivant, alors que les sites hôtes veulent leurs chiffres quand ils le veulent et que l'enseigne de 300 sites veut des données quotidiennes ;
- **la confidentialité** : chaque site hôte ne doit voir que ses propres sites ; les droits par profil sont une condition d'ouverture de l'outil aux sites hôtes ;
- **le coût et les compétences** : 60 k€ par an et trois mois de mise en place, contre le temps de huit personnes absorbé par la production de tableaux.

**Recommandation** : l'**outil décisionnel en libre-service**, mais **gouverné**. L'informatique décisionnelle est une démarche, pas un outil (F08 § 6) : l'équipe données publie des indicateurs certifiés, définis dans le dictionnaire (disponibilité constatée, sessions de plus de deux minutes) et calculés sur le modèle corrigé (question 2.1) ; les droits sont fixés par profil, le portail des sites hôtes ne montrant que leurs sites ; les utilisateurs sont formés. L'équipe données passe de la production de tableaux à la gouvernance des indicateurs et aux analyses, dont le modèle de prévision. Le portail répond aussi à l'attente des sites hôtes relevée à la question 2.2.

**Une représentation pour les sites hôtes**, parmi :
- **barres mensuelles des sessions et de l'énergie délivrée sur le site**, comparées au même mois de l'année précédente, avec, pour chaque point, sa disponibilité constatée face à la ligne de la cible de 98 %. *Message* : l'activité du site progresse-t-elle, et AMPÉRANE tient-elle son engagement de disponibilité sur ses points ?
- **carte de chaleur des sessions par jour de la semaine et par heure**. *Message* : les heures d'affluence des conducteurs sur le parking, à rapprocher des heures d'ouverture ; elle recoupe le rapport de fréquentation payant envisagé (question 2.4), qui en serait la version détaillée.

Pièges à éviter : comparer des sites de tailles différentes en valeurs absolues plutôt qu'en sessions par point, tronquer l'axe, juxtaposer des disponibilités calculées selon des règles différentes.

**Réponses tolérées**
- Chaîne présentée selon les étapes de l'informatique décisionnelle (collecte, extraction-transformation-chargement, entrepôt, restitution), si un biais est rattaché à chaque étape.
- Analyse exploratoire mobilisée pour les constats (croisements par type de site et par puissance), à côté de l'analyse descriptive.
- Autres constats tirés des annexes 2.3 A et B (hausse des sessions échouées aux aires, stabilité de l'ensemble à 1,5), s'ils sont chiffrés et interprétés.
- Effet des sessions courtes établi par la lecture des pourcentages, sans le calcul d'environ 2,7 sessions par point rapide aux aires, qui n'est pas attendu.
- Analyse prescriptive évoquée en ouverture (choisir le nombre de points par site), sans développement.
- Tableaux préparés par l'équipe données retenus à titre transitoire, le temps d'écrire le dictionnaire, si le candidat prévoit ensuite le libre-service gouverné.
- Autres représentations (carte des sites, jauge ou puce de la disponibilité par point), si le message est précisé.
- Biais de la chaîne rattachés à d'autres étapes, si chacun est tiré de l'annexe et justifié.
- En 2.3 d, choix justifié par un seul critère bien appliqué : item complet si la représentation est justifiée par son message.

**Erreurs fréquentes**
- *Corrélation présentée comme une causalité* (`ET-26`) — sessions par point attribuées à la qualité des aires de services, sans examiner la puissance, les sessions courtes et la mesure de la disponibilité.
- *Prudence d'interprétation oubliée* (`JUR-D06`) — hausse de la disponibilité de 96 % à 97 % lue comme un progrès, malgré la hausse des signalements ; baisse des supermarchés lue comme une dégradation, malgré les ouvertures.
- *Prévision prise pour une décision* — classement du modèle appliqué tel quel, ou modèle décrit dans sa construction (algorithme, variables à régler) alors que la question demande son usage et ses limites ; confusion entre IA générative et apprentissage automatique (`ET-09`).
- *Informatique décisionnelle réduite à un outil* (`ET-05`, `JUR-D02`) — libre-service recommandé sans définitions communes, sans droits ni formation.
- *Calcul hors attente* (`JUR-T07`) — moyennes pondérées recalculées en détail ou tests statistiques, alors que la question demande des constats argumentés en chiffres ronds.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement, analyses descriptive et prédictive, outils décisionnels en libre-service, choix des graphiques, biais de sélection et de confirmation | définitions et méthode | F08 § 1, 2, 5 et 6 | notion de cours |
| Effet de structure | méthode de lecture | — | notion de cours |
| Apprentissage automatique et IA générative distingués | définitions | F13 ; F08 § 2 | notion de cours |
| Dictionnaire des données, indicateurs certifiés | structuration | F07 § 1 et 8 | notion de cours |

---

### 2.4 – La valeur des données et leur hébergement (4 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.f` « Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques » ; `2.3.e` « Aspects réglementaires (RGPD, archivage légal) et monétisation des données » ; `2.3.d` « Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique ». Limites : la monétisation est abordée de façon critique ; aucune valorisation chiffrée des données ; aucune analyse juridique ; aucune démarche de qualification d'un hébergeur ; le droit des données personnelles au-delà des principes donnés en annexe relève de l'UE 1.

**Annexes mobilisées** : annexes 1.1 (650 000 conducteurs, 120 000 utilisateurs actifs de l'application, services aux sites hôtes, hébergement hors de l'Union européenne), 2.1 à 2.3 (qualité des données), 2.4 (données, propositions, demande des fonds, appel à partenaires, options d'hébergement) et 2.5 (repères).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Patrimoine informationnel défini (actif immatériel, valeur d'usage et d'échange) ; deux sources de valeur appliquées au cas | 0,5 |
| a-2 | Deux risques qui menacent cette valeur, tirés des annexes | 0,5 |
| b-1 | Principes du RGPD appliqués : propositions (a) et (b) appréciées, avec la demande de liste de l'enseigne | 0,5 |
| b-2 | Proposition (c) appréciée ; recommandation : propositions retenues et conditions | 0,5 |
| b-3 | Réponse critique à M. TREVÉLOC : la valeur tient à la qualité, à la conformité et à la confiance, non au volume | 0,5 |
| c-1 | Les trois piliers du cloud de confiance définis et appliqués à l'option 1 | 0,5 |
| c-2 | Les trois piliers appliqués à l'option 2, avec les coûts et les délais | 0,5 |
| c-3 | Recommandation motivée au regard de l'appel de LOIRAVEL Agglomération et des conditions de mise en œuvre | 0,5 |

**Réponse attendue**

*2.4 a) – Le patrimoine informationnel, ses sources de valeur et ses risques*

**Définition** (0,5 pt avec les sources de valeur) : le **patrimoine informationnel** est l'ensemble des données et des informations qu'une organisation produit, détient et exploite, considéré comme un **actif immatériel** : il a une **valeur d'usage** (mieux décider, mieux opérer) et une **valeur d'échange** (services ou données proposés à des tiers). Comme tout actif, il s'inventorie, se classe, a un propriétaire, se protège, et sa valeur dépend de sa qualité et du droit de l'utiliser (F07 § 8.6).

**Deux sources de valeur** parmi :
- **la valeur d'usage pour piloter le réseau** : choisir les sites candidats (prévision de l'annexe 2.3 E, pour 20 000 points en 2030), piloter la disponibilité de 98 % par point, négocier avec les opérateurs de mobilité sur la base des sessions que chacun apporte, et mieux diagnostiquer les pannes à partir des codes d'erreur. Les journaux détaillés de deux constructeurs, aujourd'hui réservés à leurs services, enrichiraient ce patrimoine : le règlement sur les données ouvre en principe à l'utilisateur d'un produit connecté l'accès aux données que génère son utilisation (annexe 2.5) ;
- **la valeur d'échange, par de nouveaux services** : rapports de fréquentation pour les sites hôtes, données agrégées pour les collectivités, en ligne avec l'objectif de « nouvelles recettes tirées des données et des services aux sites hôtes » (10 M€ en 2026) ;
- **la valeur dans les relations avec les partenaires** : des données de sessions fiables et bien hébergées sont une condition pour répondre à l'appel de LOIRAVEL Agglomération et à ceux de trois autres agglomérations.

**Deux risques** parmi (0,5 pt) :
- **la qualité** : 60 libellés de tarifs, 3 % de sessions sans tarif, un statut publié sur dix faux, 5 % de points mal rapprochés, une disponibilité déclarée flatteuse. Des données fausses valent peu et conduisent à de mauvaises décisions (questions 2.1 à 2.3) ;
- **la conformité et la confiance** : les sessions reliées à un compte, à une immatriculation ou à un badge sont des données personnelles, avec des lieux et des heures qui révèlent des habitudes de vie. Un usage non annoncé exposerait AMPÉRANE et ruinerait la confiance de quelque 650 000 conducteurs et des opérateurs de mobilité ;
- **la dépendance et la souveraineté** : des données hébergées chez un fournisseur soumis à un droit extra-européen, avec des services gérés qui rendent le départ difficile ; des journaux de bornes détenus par les constructeurs ; un appel à partenaires qui peut être perdu ;
- **la perte, la fuite ou l'obsolescence** : une fuite des comptes de l'application, ou des données anciennes sur des bornes retirées qui ne disent plus rien de l'avenir.

*2.4 b) – Les trois propositions au regard du RGPD et la demande des fonds*

Les principes à appliquer sont ceux de l'annexe 2.5 : **finalités déterminées**, sans usage ultérieur incompatible ; **minimisation** ; **information** des personnes sur les finalités et les destinataires. Les conducteurs ont été informés d'un usage pour la facturation, le service clients et l'amélioration du réseau, « rien d'autre » (annexe 2.4 A). Une donnée agrégée qui ne permet plus d'isoler un conducteur n'est plus une donnée personnelle ; une donnée rattachée à un compte, à une immatriculation ou à un badge l'est.

**Proposition (a) – rapports de fréquentation pour les supermarchés** (0,5 pt avec la proposition b) :
- le rapport lui-même porte sur des données **agrégées** par site, par jour et par heure : il ne livre aucune donnée personnelle s'il est assez agrégé pour qu'aucun conducteur ne puisse être isolé, ce qui suppose de regrouper les heures creuses des petits sites. C'est une valorisation acceptable, proche du service rendu aux sites hôtes ;
- la **liste des conducteurs** qui rechargent plus d'une heure, avec leur adresse électronique, est à refuser : elle transmettrait des données personnelles à un tiers pour sa prospection commerciale, une finalité étrangère à celles annoncées et dont les conducteurs n'ont pas été informés, au-delà du nécessaire ;
- les contrats avec les sites hôtes ne disent rien de l'usage des données produites sur leurs parkings : la règle doit être écrite avec eux avant toute vente.

**Proposition (b) – données agrégées pour les collectivités** : utile à la planification publique ; une fois agrégées, les données ne permettent plus d'isoler un conducteur, et leur production reste proche de la finalité d'amélioration du réseau annoncée aux conducteurs. La proposition est acceptable à condition :
- d'une agrégation suffisante (commune et heure, en regroupant les petites communes) ;
- que la part des conducteurs venus d'un autre département soit retirée de l'offre : AMPÉRANE n'enregistre pas le domicile des conducteurs (annexe 2.4 A), et la produire supposerait de collecter une donnée nouvelle, au-delà du nécessaire et pour une finalité dont les conducteurs n'ont pas été informés ;
- d'un contrat qui interdit de recouper les données ou de les revendre ;
- d'une mise en garde sur leur qualité (disponibilité déclarée).

**Proposition (c) – historiques de recharge par véhicule pour SELVAREN Automobiles** (0,5 pt avec la recommandation) : à refuser dans cette forme. L'immatriculation rattache chaque historique à son propriétaire : ce sont des données personnelles, avec des **données de localisation** (lieux et heures de recharge) qui révèlent les déplacements et les habitudes. La finalité est nouvelle (étude des batteries et surtout offres commerciales du constructeur) et incompatible avec celles annoncées ; les conducteurs n'en ont pas été informés ; l'historique « complet » excède ce qu'exige l'étude de l'usure des batteries. Seule une version **agrégée par modèle de véhicule**, sans immatriculation (énergie délivrée, puissance acceptée, durées), serait envisageable, et elle ne permettrait pas le démarchage visé.

**Recommandation** : retenir (a) sans la liste de conducteurs et (b), à leurs conditions d'agrégation et de contrat ; refuser (c). Avant toute mise en œuvre :
- la déléguée à la protection des données est consultée ;
- le registre des traitements est mis à jour ;
- l'information des conducteurs est complétée si un nouvel usage est retenu ;
- les données agrégées sont produites à partir du modèle corrigé (question 2.1), faute de quoi la qualité vendue ne serait pas au rendez-vous.

**La réponse à M. TREVÉLOC** (0,5 pt) : douze millions de sessions ne valent pas par leur volume. Leur valeur tient à leur **qualité**, aujourd'hui insuffisante (60 libellés de tarifs, disponibilité flatteuse), à leur **droit d'usage**, borné par les finalités annoncées aux conducteurs et par les contrats avec les sites hôtes, et à la **confiance** des conducteurs, des opérateurs et des collectivités. « Vendre tout ce qui peut l'être » serait illicite pour les données personnelles et risqué pour la réputation, au moment même où les fonds demandent un système d'information sûr. Ce que des investisseurs examineront en 2028, c'est un patrimoine **documenté et gouverné** : inventaire des données, propriétaires, dictionnaire, indicateurs de qualité, conformité, hébergement maîtrisé, et des services récurrents fondés sur des données agrégées. La monétisation est donc sélective et prudente, et la première valeur des données reste leur usage pour atteindre 20 000 points à 98 % de disponibilité.

*2.4 c) – Les deux options d'hébergement selon le cloud de confiance*

**Les trois piliers** (0,5 pt avec l'option 1) : le référentiel du cloud de confiance du Cigref évalue une offre d'informatique en nuage selon trois piliers (annexe 2.5) :
- la **sécurité** des données et des services ;
- l'**immunité aux lois extra-européennes**, c'est-à-dire l'absence d'accès possible aux données par une autorité d'un État tiers en vertu de son droit ;
- la **maîtrise de la dépendance** : réversibilité, portabilité, absence d'enfermement chez un fournisseur.

Toute exigence opérationnelle doit aussi être exigible par contrat ; ce n'est ni un label, ni une certification. La souveraineté ne se réduit pas à la localisation des centres de données : elle tient au **droit applicable au prestataire** (F03 § 5.3 ; F07 § 8.5).

| Pilier | Option 1 – Rester, avec protections renforcées | Option 2 – Hébergeur européen qualifié SecNumCloud |
|---|---|---|
| Sécurité | niveau élevé d'un grand fournisseur, chiffrement de toutes les données ; mais les clés sont gérées dans un service du fournisseur, qui exploite l'environnement où elles servent | exigences de sécurité de SecNumCloud vérifiées lors de la qualification de l'offre par l'ANSSI ; risque propre à la migration (douze mois de transition, reprise des données, remplacement de deux outils d'analyse), à maîtriser par un plan de bascule et des essais |
| Immunité aux lois extra-européennes | **non assurée** : le fournisseur « reste soumis au droit du pays de son siège » ; la localisation en France ne change pas le droit qui s'applique à lui, et un engagement contractuel d'informer et de contester ne peut pas l'emporter sur une loi ; l'option ne répond pas à l'exigence de LOIRAVEL Agglomération | **assurée en principe** : siège dans l'Union, capital européen, critères de protection contre les lois extra-européennes de SecNumCloud ; l'option répond à l'exigence de LOIRAVEL Agglomération |
| Maîtrise de la dépendance | **faible** : services gérés propres au fournisseur (base de données, file de messages, outils d'analyse), qui rendent tout départ « long et coûteux » ; la dépendance croîtra avec le réseau. Le règlement sur les données facilite en principe le changement de fournisseur, sans supprimer ces adhérences | **meilleure sur le droit et les formats** : export en formats ouverts, CIRCÉA adaptée à des services plus standards, donc plus portable ; mais nouvelle dépendance envers un hébergeur dix fois plus petit, au catalogue restreint, dont la capacité à suivre un réseau multiplié par deux et demi doit être vérifiée et inscrite au contrat |
| Coût et délai | 150 k€ par an ; trois mois | 1 200 k€ de migration au total, répartis sur 2027 et 2028, puis environ 360 k€ de plus par an (15 % des 2 400 k€ de 2026, qui couvrent CIRCÉA, l'application des conducteurs et les outils d'analyse) ; douze mois |

(0,5 pt pour l'option 2 avec les coûts et les délais.)

**Recommandation** (0,5 pt) : retenir l'**option 2**, décidée dès le printemps 2027 :
- **l'enjeu** : seule l'option 2 permet de répondre à LOIRAVEL Agglomération (600 points, soit 7,5 % du réseau de 2026 et 3 % de l'objectif de 2030) et aux trois agglomérations qui préparent des appels semblables, sur un segment qui pèse 15 % des sites ; elle réduit aussi la dépendance envers un fournisseur soumis à un droit extra-européen, que les fonds relèveront avant la levée de 2028 ;
- **le coût** : un surcoût de l'ordre de 0,5 M€ par an en moyenne sur quatre ans, à rapprocher de cet enjeu et des 118 M€ de chiffre d'affaires ;
- **le calendrier** : réponse à l'appel avant le 30 juin 2027, avec un engagement daté ; migration en priorité des données des sessions et des comptes des conducteurs, puis du reste de CIRCÉA, pour une mise en service du partenariat début 2028. Pendant la transition, le chiffrement de l'option 1 protège les données encore chez le fournisseur actuel ;
- **le contrat** : contrat de sous-traitance offrant des garanties suffisantes (RGPD, annexe 2.5), engagements de service, capacité de croissance, réversibilité et export en formats ouverts, chaque exigence opérationnelle étant exigible par contrat (Cigref) ;
- **l'organisation** : remplacement des deux outils d'analyse de l'équipe données, et suivi de la migration par la direction technique.

**Réponses tolérées**
- Option 1 recommandée pour son coût et son délai, si le candidat reconnaît qu'elle ne répond pas à l'exigence de LOIRAVEL Agglomération et en tire la conséquence (renoncer à l'appel, ou héberger à part les seules données de ses parkings).
- Solution mixte : données des collectivités et données personnelles des conducteurs chez l'hébergeur qualifié, le reste chez le fournisseur actuel, si la complexité d'exploitation de deux hébergeurs est discutée.
- Comparaison de tête du coût sur 2027-2030 (environ 600 k€ contre 2 640 k€ au volume de 2026), qui n'est pas attendue.
- Patrimoine informationnel défini comme l'ensemble des actifs informationnels, ou valeur des données présentée selon d'autres catégories (stratégique, opérationnelle, commerciale), si elles sont appliquées au cas.
- Proposition (b) refusée faute de garanties suffisantes sur la qualité ou sur l'agrégation, si le refus est argumenté.
- Part des conducteurs d'un autre département acceptée si le candidat précise d'où vient la donnée et la limite à un calcul agrégé interne.

**Erreurs fréquentes**
- *Hébergement « souverain » réduit à la localisation en France* (`ET-37`) — l'option 1 jugée suffisante parce que les centres de données sont en France, sans examiner le droit applicable au fournisseur.
- *Monétisation sans regard critique* (`JUR-N01`, `JUR-D04`) — ventes acceptées telles quelles, données collectées au-delà du nécessaire, ou données personnelles présentées comme une marchandise dont l'entreprise serait propriétaire.
- *Dérive juridique* (`JUR-T07`) — analyse des contrats, recherche d'un fondement juridique du traitement ou des prérogatives des conducteurs sur leurs données (UE 1), alors que la question demande d'appliquer les principes donnés en annexe.
- *SecNumCloud mal présenté* (`ET-01`) — qualification de l'ANSSI présentée comme une norme ISO ou comme une certification de l'entreprise.
- *Morceau de cours* (`JUR-T01`) — piliers du cloud de confiance ou principes du RGPD récités sans application aux propositions et aux options de l'annexe 2.4.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | donnée personnelle, données de localisation, finalité, minimisation, information, sous-traitant (annexe 2.5) | `rgpd` / F15 § 5 | en vigueur |
| Règlement (UE) 2023/2854 sur les données (Data Act), applicable depuis le 12/09/2025 | accès de l'utilisateur aux données d'un produit connecté, changement de fournisseur de cloud (annexe 2.5) | `data_act` / F07 § 8.5 | en vigueur |
| SecNumCloud, version 3.2 (ANSSI, 08/03/2022) | qualification d'offres d'informatique en nuage, sécurité et protection contre les lois extra-européennes | `secnumcloud_3_2` / F03 § 5.3 | en vigueur |
| Référentiel du cloud de confiance du Cigref, V1 du 27/05/2021, V2 disponible | trois piliers, exigences exigibles par contrat | `cigref_cloud_confiance` / F03 § 5.3, F07 § 8.5 | publié |
| Patrimoine informationnel, valeur d'usage et d'échange, monétisation critique, souveraineté, réversibilité | définitions et méthode | F07 § 8.5 et 8.6 ; F03 § 5.3 | notion de cours |
