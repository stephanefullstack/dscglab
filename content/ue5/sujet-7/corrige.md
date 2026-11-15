# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 7

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Organiser et valoriser les données des supporters | 14 | 1.1 à 1.5 | `exercices/ex19_donnees_supporters_billetterie` |
| 2 – Gouverner le numérique du club et évaluer le projet de jetons de supporters | 13 | 2.1 à 2.5 | `exercices/ex20_gouvernance_numerique_jetons` |
| 3 – Maîtriser les risques des jours de match et l'empreinte du stade connecté | 13 | 3.1 à 3.4 | `exercices/ex21_jours_match_stade_connecte` |
| **Total** | **40** | | |

---

## DOSSIER 1 – ORGANISER ET VALORISER LES DONNÉES DES SUPPORTERS (14 points)

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Cartographie et urbanisation | `1.3.b` Cartographie applicative et fonctionnelle des SI ; `1.3.c` Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle | 2 |
| 1.2 Modélisation des données de la billetterie et des abonnements | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) | 3,5 |
| 1.3 Qualité, cohérence et circulation des données | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.3.a` Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques ; `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) | 3,5 |
| 1.4 Analyse des données de fidélité | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model | 2,5 |
| 1.5 Valeur des données des supporters et demande du partenaire | `2.3.f` Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques ; `2.3.e` Aspects réglementaires (RGPD, archivage légal) et monétisation des données | 2,5 |
| **Dossier 1 – Organiser et valoriser les données des supporters** |  | **14** |

Répartition indicative : connaissances (définitions, règles de passage, étapes de la chaîne de traitement) 3,25 points (items 1.1 b-1 pour moitié, 1.2 b-1, 1.3 b-1 pour moitié, 1.3 c-1 pour moitié, 1.4 a-1 et a-2 pour moitié, 1.4 c pour moitié, 1.5 a-1 pour moitié, et la moitié des items 1.2 a-1 à a-4 consacrée au formalisme) ; analyse des annexes et recommandations 10,75 points, soit environ 77 %. Durée conseillée : 14 points × 4,5 minutes ≈ 1 h 03.

---

### 1.1 – Cartographie et urbanisation (2 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.b` « Cartographie applicative et fonctionnelle des SI » ; `1.3.c` « Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle ».

**Annexes mobilisées** : annexes 1.1 (organigramme : utilisateurs des applications) et 1.2 (applications, échanges, constats, témoignage de M. PEYRASTRE).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Six applications (et le prestataire de restauration comme source externe) représentées avec leurs données principales | 0,5 |
| a-2 | Flux orientés et légendés : données échangées et mode (API, export manuel, ressaisie, courriel, absence de flux) ; le seul flux automatisé identifié | 0,5 |
| b-1 | Urbanisation définie (démarche stratégique, zones, quartiers, îlots, échanges maîtrisés) et trois défauts tirés de la cartographie | 0,5 |
| b-2 | Place du référentiel unique : zone des référentiels, alimentant les applications par une zone d'échange ; le référentiel ne remplace pas les applications métier | 0,5 |

**Réponse indicative**

*1.1 a) – Cartographie applicative des données des supporters*

```
 [Partenaires] ──courriel (listes d'invités)──> [Fichier des partenaires et des loges : tableur]
                                                        │ ressaisie manuelle avant chaque match (≈ 900 invités)
                                                        v
 [Boutique en ligne] ──export trimestriel──┐   [Billetterie et abonnements, SaaS] ══API══> [Contrôle d'accès]
  id : adresse électronique               │    id : n° de client                   <──fichier── (passages,
                                          v         │                                  copiés dans un tableur)
                          [Lettre d'information] <──┘ export mensuel (acheteurs)
                           id : adresse électronique

 [Application mobile, agence] ··· pages de la billetterie ouvertes dans l'application, aucun échange de données
  id : identifiant de compte   ··· données d'usage gardées par l'agence, extraction facturée (aucun flux)
 [Prestataire de restauration] ──relevé annuel (paiements par carte rechargeable)──> club (tableur)

Légende : ══ échange automatisé (API) ; ── export, fichier ou ressaisie manuels ; ··· absence de flux maîtrisé.
Aucun identifiant commun : n° de client, adresse électronique, identifiant de compte, raison sociale.
```

Sont valorisés : le sens des flux ; la distinction entre le seul échange automatisé (API billetterie → contrôle d'accès) et les exports manuels, ressaisies et courriels ; l'identifiant propre à chaque application (numéro de client, adresse électronique, identifiant de compte, raison sociale) ; l'absence de flux depuis l'application mobile.

*1.1 b) – Défauts d'urbanisation et place du référentiel*

L'urbanisation du SI est la démarche, stratégique et non seulement technique, qui organise le système d'information par analogie avec l'urbanisme d'une ville : découpage en zones, quartiers et îlots faiblement couplés, une seule source pour chaque donnée de référence et des échanges qui passent par une zone d'échange maîtrisée, afin que le SI évolue avec la stratégie sans tout reconstruire (F03 § 1).

Trois défauts (0,5 pt avec la définition) :
1. **Une donnée de référence sans source unique ni propriétaire** : la personne du supporter est décrite dans quatre applications et un tableur, avec quatre types d'identifiant ; 120 000 fiches pour environ 72 000 personnes ; « personne n'est chargé de dire laquelle est la bonne » (M. PEYRASTRE).
2. **Des échanges point à point, manuels et tardifs** : exports mensuels et trimestriels, fichier du contrôle d'accès copié dans un tableur, environ 900 invitations ressaisies avant chaque match (13 500 par saison) ; un seul flux automatisé, alors que l'éditeur de la billetterie offre des API. Les données circulent mal, avec retard et risque d'erreur.
3. **Des îlots isolés ou captifs** : les données d'usage de l'application mobile restent chez l'agence (extraction facturée), le fichier des partenaires vit sur un tableur hors des applications gérées, le relevé de restauration arrive une fois par an. Le club ne maîtrise pas une partie de ses propres données.

Place du référentiel unique des supporters (0,5 pt) : il se situe dans la **zone des référentiels** (données de référence) de l'architecture cible, à côté du référentiel des partenaires, et non dans l'une des applications métier. Il détient la fiche unique de chaque personne (identifiant, identité, coordonnées, consentements) et les liens vers ses abonnements, billets et présences (annexe 1.3) ; il **alimente** les applications des quartiers billetterie, commerce (boutique), relation numérique (application, lettre d'information) et partenariats, et reçoit leurs mises à jour, par une **zone d'échange** (API) plutôt que par des fichiers. Les applications continuent d'exercer leurs fonctions ; elles cessent de créer chacune leur propre supporter. Il alimente aussi les analyses (question 1.4).

**Réponses tolérées**
- Cartographie présentée en tableau des flux (source, destination, données, mode, fréquence) au lieu d'un dessin, si elle fait apparaître les mêmes éléments (format libre, JUR-T10).
- Défauts formulés en d'autres termes (redondance, couplage fort, absence de zone d'échange, SI non aligné sur l'objectif de connaissance des supporters), s'ils sont tirés de l'annexe 1.2.
- Référentiel placé dans la billetterie, devenue application maîtresse de la fiche du supporter, si le candidat justifie ce choix (seule application qui porte l'identité et les abonnements, API disponibles) et en signale la limite (dépendance à l'éditeur du SaaS).
- Vocabulaire des couches (métier, fonctionnelle, applicative, technique) employé à la place des zones et quartiers.

**Erreurs types**
- *Urbanisation réduite à une vision technique* (`ET-20`, `JUR-G07`) — inventaire des logiciels et des serveurs, sans dire pourquoi urbaniser ni quels principes appliquer ; juste : les défauts portent sur les données de référence, les échanges et la maîtrise des îlots.
- *Schéma illisible ou sans flux* (`JUR-T10`) — liste d'applications sans sens des échanges ni mode ; juste : flux orientés et légendés.
- *Définition sans application au cas* (`JUR-T01`) — définition de l'urbanisation récitée sans les 120 000 fiches, les ressaisies ni l'application mobile captive ; juste : chaque défaut s'appuie sur un fait de l'annexe 1.2.
- *Architecture technique détaillée* (`JUR-T12`) — description de serveurs, de bases ou de bus d'intégration, que la question n'appelle pas ; juste : la place fonctionnelle du référentiel et le principe des échanges.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Urbanisation : zones, quartiers, îlots ; une donnée de référence, un seul propriétaire ; zone d'échange | définition, règles d'urbanisme | F03 § 1 et 3 | notion de cours |
| Cartographie applicative | applications, flux, ruptures | F03 § 2 | notion de cours |

---

### 1.2 – Modélisation des données de la billetterie et des abonnements (3,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) ».

**Annexes mobilisées** : annexe 1.3 (règles de gestion RG1 à RG8).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Six entités avec identifiant souligné et attributs élémentaires correctement placés (Supporter, Saison, Tribune, Abonnement, Match, Billet), sans clé étrangère | 0,5 |
| a-2 | Associations de l'abonnement (souscrire, concerner, situer) et du match (programmer) avec cardinalités justifiées par RG4 et RG5 | 0,5 |
| a-3 | Associations du billet (acheter, donner accès, placer) avec cardinalités justifiées par RG6 | 0,5 |
| a-4 | Association n:m *assister* entre Abonnement et Match, porteuse de l'heure de passage, cardinalités 0,n / 0,n justifiées par RG7 | 0,5 |
| b-1 | Règles de passage énoncées (entité → table ; cardinalité maximale 1 → clé étrangère ; association n:m → table à clé composée portant ses attributs) | 0,5 |
| b-2 | Tables Abonnement, Match et Billet avec leurs clés étrangères | 0,5 |
| b-3 | Table Presence à clé composée (#num_abonnement, #num_match) portant heure_passage | 0,5 |

**Réponse indicative**

*1.2 a) – Modèle conceptuel des données*

Le MCD représente les objets de gestion (entités), leurs propriétés (attributs) et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique (F07 § 1).

Entités (identifiant en premier, souligné sur la copie) (0,5 pt) :
- SUPPORTER (<u>num_supporter</u>, nom, prenom, date_naissance, courriel, telephone, code_postal, date_consentement_club, date_consentement_partenaires) – RG1 ;
- SAISON (<u>code_saison</u>, date_debut, date_fin) – RG2 ;
- TRIBUNE (<u>code_tribune</u>, libelle_tribune, nb_places) – RG3 ;
- ABONNEMENT (<u>num_abonnement</u>, formule, prix_abonnement, date_souscription) – RG4 ;
- MATCH (<u>num_match</u>, date_match, heure_coup_envoi, adversaire) – RG5 ;
- BILLET (<u>num_billet</u>, tarif, prix_billet, date_achat, canal_vente) – RG6.

Associations et cardinalités :

```
SUPPORTER  (0,n) ──── souscrire ──── (1,1) ABONNEMENT
ABONNEMENT (1,1) ──── concerner ──── (0,n) SAISON
ABONNEMENT (1,1) ──── situer ─────── (0,n) TRIBUNE
MATCH      (1,1) ──── programmer ─── (1,n) SAISON
SUPPORTER  (0,n) ──── acheter ────── (1,1) BILLET
BILLET     (1,1) ──── donner_acces ─ (0,n) MATCH
BILLET     (1,1) ──── placer ─────── (0,n) TRIBUNE
ABONNEMENT (0,n) ──── assister [heure_passage] ──── (0,n) MATCH
```

Sur la copie, chaque entité n'est dessinée qu'une fois : ABONNEMENT au centre, relié à SUPPORTER, SAISON, TRIBUNE et MATCH ; BILLET relié à SUPPORTER, MATCH et TRIBUNE ; MATCH relié à SAISON.

- *souscrire*, *concerner*, *situer* : un abonnement est souscrit par un seul supporter, pour une seule saison, dans une seule tribune (1,1 côté Abonnement) ; un supporter peut n'avoir aucun abonnement ou en avoir plusieurs au fil des saisons, une saison ou une tribune peut n'en avoir encore aucun (0,n) – RG4 ;
- *programmer* : un match appartient à une seule saison (1,1) ; toute saison comporte au moins un match, puisque le calendrier est enregistré à l'ouverture de la campagne (1,n) – RG5 (0,5 pt pour ces quatre associations) ;
- *acheter*, *donner_acces*, *placer* : un billet est acheté par un seul supporter, pour un seul match, dans une seule tribune (1,1) ; un supporter, un match ou une tribune peut n'avoir donné lieu à aucun billet (0,n) – RG6 (0,5 pt) ;
- *assister*, association n:m porteuse de l'attribut heure_passage : l'heure de passage ne dépend ni de l'abonnement seul ni du match seul, mais du couple ; un abonnement peut n'avoir aucune présence, un match à huis clos n'en enregistre aucune (0,n de part et d'autre) – RG7 (0,5 pt).

La règle RG8 est une règle de cycle de vie (suppression ou anonymisation) : elle ne crée ni entité ni association. Une contrainte n'est pas représentable par les cardinalités et peut être signalée : la présence ne vaut que pour un match de la saison de l'abonnement.

*1.2 b) – Modèle logique des données*

Règles de passage (0,5 pt) : chaque entité devient une table dont l'identifiant est la clé primaire ; pour une association binaire dont une patte a une cardinalité maximale de 1, l'identifiant de l'entité de l'autre patte migre comme clé étrangère dans la table de l'entité côté 1,1 (non nulle, puisque la cardinalité minimale est 1) ; une association n:m devient une table dont la clé primaire est la concaténation des identifiants des entités reliées, chacun clé étrangère, et qui porte les attributs de l'association.

- Supporter (<u>num_supporter</u>, nom, prenom, date_naissance, courriel, telephone, code_postal, date_consentement_club, date_consentement_partenaires)
- Saison (<u>code_saison</u>, date_debut, date_fin)
- Tribune (<u>code_tribune</u>, libelle_tribune, nb_places)
- Abonnement (<u>num_abonnement</u>, formule, prix_abonnement, date_souscription, #num_supporter, #code_saison, #code_tribune)
- Match (<u>num_match</u>, date_match, heure_coup_envoi, adversaire, #code_saison) (0,5 pt avec Abonnement et Billet)
- Billet (<u>num_billet</u>, tarif, prix_billet, date_achat, canal_vente, #num_supporter, #num_match, #code_tribune)
- Presence (<u>#num_abonnement, #num_match</u>, heure_passage) (0,5 pt)

Exemple d'enregistrements cohérents : l'abonnement A2027-00815 (formule famille, tribune NORD, saison 2027-2028) du supporter S0041207 donne lieu à une ligne de Presence pour le match M2027-02 avec l'heure de passage 14:22. Le modèle physique (types, index, contraintes) se déduit du MLD lors de l'implantation dans le référentiel ; il n'est pas demandé.

**Réponses tolérées**
- Noms d'entités, d'associations ou d'attributs différents s'ils restent explicites (« Abonné », « Rencontre », « Passage ») ; notation « pattes de corbeau » ou UML lisible (format libre, JUR-T10).
- Présence modélisée comme une entité PASSAGE à identifiant propre, reliée par deux associations 1,1 à Abonnement et à Match, si le candidat signale l'unicité du couple abonnement × match : barème de a-4 et b-3 maintenu.
- Consentements modélisés par une entité CONSENTEMENT (type, date, texte présenté) reliée au supporter : valorisé s'il est justifié (traçabilité du texte, constat de l'annexe 1.2), sans pénaliser la solution par attributs qui suit RG1.
- Billet relié à une association ternaire supporter × match × tribune avec identifiant propre : accepté si les cardinalités restent justes.

**Erreurs types**
- *MCD et MLD confondus* (`ET-23`, `JUR-T06`) — clés étrangères dessinées dans le MCD, ou MLD sans table issue de l'association *assister* ; juste : le MCD ne comporte ni clé étrangère ni table ; le MLD dérive de règles de passage énoncées.
- *Attribut d'association mal placé* — heure de passage portée par Abonnement ou par Match ; juste : elle dépend du couple et figure dans la table Presence.
- *Cardinalités non justifiées* (`JUR-T01`) — liste d'entités sans associations ni renvoi aux règles ; juste : chaque cardinalité est rattachée à une règle de gestion.
- *Hors sujet technique* — écriture de requêtes ou de scripts de création de tables, que la question exclut ; juste : schéma relationnel seulement.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Formalisme Merise (MCD, MLD, règles de passage) | entités, associations, cardinalités, association porteuse | F07 § 2 à 5 | manuels |

---

### 1.3 – Qualité, cohérence et circulation des données (3,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) ».
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.a` « Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques » ; `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ».

**Annexes mobilisées** : annexes 1.1 (organigramme), 1.2 (identifiants, constats du profilage, échanges, témoignage de M. PEYRASTRE) et 1.3 (RG1, RG8).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Identifiant unique du supporter : attribué par le référentiel, non signifiant, stable, porté par toutes les applications (table de correspondance avec les anciens identifiants) | 0,5 |
| a-2 | Trois règles de dédoublonnage appliquées aux fiches (rapprochement certain, rapprochement probable soumis à validation, règle de fusion et de conservation) | 0,5 |
| a-3 | Indicateur à cinq champs (formule, source, fréquence, cible, axe) | 0,5 |
| b-1 | Dictionnaire de données défini et quatre rubriques choisies et justifiées | 0,5 |
| b-2 | Entrées des trois données (adresse électronique, date de naissance, consentement aux offres des partenaires) cohérentes avec les constats | 0,5 |
| c-1 | Trois responsables désignés, avec leur titulaire, et rôles distingués parmi propriétaire, intendant, responsable informatique, délégué à la protection des données | 0,5 |
| c-2 | Circulation par API du référentiel et formats ouverts, en remplacement des exports et des ressaisies, appliquée aux flux de l'annexe 1.2 | 0,5 |

**Réponse indicative**

*1.3 a) – Identifiant unique, dédoublonnage et indicateur*

**Identifiant unique** (0,5 pt) : le numéro de supporter (ex. S0041207, RG1), attribué par le référentiel à la création de la fiche, **non signifiant** (il ne contient ni le nom, ni la tribune, ni l'adresse électronique, qui changent), **stable** pendant toute la vie de la fiche, jamais réattribué. Chaque application le reçoit et le conserve à côté de son propre identifiant (numéro de client de la billetterie, identifiant de compte de l'application, adresse électronique de la boutique et de la lettre), dans une table de correspondance tenue par le référentiel. L'adresse électronique ne peut pas servir d'identifiant : elle change, manque ou est invalide pour 5 % à 20 % des fiches selon l'application, et une famille en partage parfois une seule.

**Trois règles de dédoublonnage** (0,5 pt) :
1. **Rapprochement certain, fusion automatique** : même adresse électronique normalisée (minuscules, espaces supprimés) et même nom et prénom normalisés (accents, tirets) ; ou même numéro de client cité dans le compte de l'application.
2. **Rapprochement probable, validation humaine** : même nom, prénom et date de naissance, mais adresses différentes ; ou même adresse électronique et prénoms différents (famille) : la fusion est proposée à l'intendant de la donnée, qui tranche ; aucune fusion sur le seul nom.
3. **Règle de fusion (« survie » des valeurs)** : la billetterie fait foi pour l'identité et les abonnements, la valeur la plus récemment confirmée pour les coordonnées, et pour les consentements la valeur **la plus restrictive** (un refus ou une absence l'emporte sur un consentement non daté) ; l'historique des fiches fusionnées est conservé. En amont, une recherche de l'existant est imposée avant toute création de fiche.

**Indicateur** (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de fiches en double | fiches du référentiel en double non fusionnées (doublons probables détectés par le rapprochement mensuel) / fiches actives du référentiel | référentiel « supporters » (rapport mensuel de rapprochement) | mensuelle | moins de 2 % à la fin de la saison 2027-2028 (point de départ : environ 40 % des fiches des quatre applications en mars 2027, avant reprise) | processus |

*1.3 b) – Dictionnaire de données*

Le dictionnaire de données est le référentiel qui décrit chaque donnée de façon unique et partagée : nom, définition, format, règles de validité, source de référence, propriétaire, sensibilité, durée de conservation ; il fixe le sens commun des données (dimension sémantique) et il se distingue du MCD, qui décrit les relations entre les données (F07 § 1). Pour le club, il met fin aux champs libres (« catégorie de supporter ») et aux définitions différentes d'une application à l'autre.

Quatre rubriques suffisent (0,5 pt avec la définition) ; le tableau en propose six, parmi lesquelles le candidat en retient quatre : **définition** (sens partagé), **format et règle de validité** (contrôle à la saisie), **caractère obligatoire**, **source de référence** (application ou référentiel qui fait foi), **propriétaire**, **sensibilité et durée de conservation** (conformité, cycle de vie RG8).

| Rubrique | Adresse électronique | Date de naissance | Consentement à recevoir les offres des partenaires |
|---|---|---|---|
| Définition | adresse de messagerie personnelle du supporter, utilisée pour les billets, les confirmations et, s'il y consent, la prospection | date de naissance du supporter, qui détermine l'âge et le droit aux tarifs jeune et réduit | date à laquelle le supporter a accepté de recevoir les offres des partenaires du club, avec le texte qui lui a été présenté et le canal de recueil (texte et canal : à ajouter au modèle, par exemple par l'entité CONSENTEMENT tolérée au 1.2) |
| Format et validité | forme « nom@domaine », vérifiée à la saisie et confirmée par un message de validation ; une seule adresse par fiche | JJ/MM/AAAA ; date passée, âge compris entre 0 et 110 ans | date JJ/MM/AAAA, vide en l'absence de consentement ; jamais présumée ; distinct du consentement aux offres du club |
| Obligatoire | oui pour l'achat en ligne et l'application ; facultative au guichet | oui pour un abonnement et un tarif réduit | non : vide par défaut |
| Source de référence | référentiel « supporters », mis à jour par toute application où le supporter la modifie | référentiel, à partir de la billetterie | référentiel, à partir du formulaire commun de préférences (boutique, billetterie, application) |
| Propriétaire | responsable du pôle marketing et numérique | responsable de la billetterie | responsable du pôle marketing et numérique, sur avis du délégué à la protection des données |
| Sensibilité et conservation | donnée personnelle ; supprimée avec la fiche selon RG8 | donnée personnelle ; supprimée avec la fiche selon RG8 | donnée personnelle ; conservée avec sa preuve tant que la fiche existe, effacée en cas de retrait |

(0,5 pt pour les trois entrées.) Sont valorisées : la séparation des deux consentements (RG1) et la conservation du texte présenté, qui répond aux constats de l'annexe 1.2 (case unique non datée de la lettre, 10 000 fiches d'origine inconnue).

*1.3 c) – Responsables et circulation des données*

**Responsables** (0,5 pt pour trois responsables avec leur titulaire, parmi les rôles suivants), rôles illustratifs et non normatifs (F07 § 8.1) :
- **propriétaire de la donnée**, responsable métier d'un domaine qui en fixe les définitions, les règles et la qualité attendue : la responsable de la billetterie pour l'identité, les abonnements, les billets et les présences ; la responsable du pôle marketing et numérique pour les coordonnées et les consentements ; le directeur commercial pour les partenaires ;
- **intendant de la donnée**, qui applique au quotidien les contrôles, valide les fusions probables, corrige à la source et tient le dictionnaire : un gestionnaire de la billetterie, formé à cette mission ;
- **responsable informatique**, qui met en œuvre le référentiel, les API, les droits d'accès et la sécurité, sans décider du contenu des données ;
- **délégué à la protection des données**, à désigner (le club n'en a pas : annexe 1.2) : il conseille sur les consentements, les durées de conservation (RG8) et les nouveaux usages, et fait mettre à jour le registre (application mobile et boutique absentes) ;
- vous-même, comme responsable du SI, arbitrez les conflits entre propriétaires et rendez compte à la directrice générale.

**Circulation des données** (0,5 pt) : le référentiel expose des **API**, c'est-à-dire des interfaces documentées et sécurisées par lesquelles chaque application crée ou recherche un supporter, lit sa fiche et transmet ses mises à jour (changement d'adresse, consentement, achat) au fil de l'eau, au lieu des exports mensuels et trimestriels : une adresse modifiée une fois l'est partout. L'éditeur de la billetterie propose déjà des API (annexe 1.2) ; le contrôle d'accès renvoie les passages par la même voie, sans tableur. Les échanges qui restent par fichier (relevé de restauration, listes d'invités des partenaires) utilisent des **formats ouverts** et structurés (CSV ou JSON décrits par le dictionnaire) et un formulaire en ligne pour les invités, ce qui supprime les ressaisies. Le contrat avec l'agence de l'application mobile prévoit la restitution des données d'usage, sans frais, dans un format ouvert. Le détail technique des échanges n'est pas attendu.

**Réponses tolérées**
- Règles de dédoublonnage fondées sur d'autres combinaisons de critères (téléphone, code postal) dès lors qu'elles distinguent rapprochement certain et rapprochement probable soumis à validation.
- Autre indicateur de qualité complet : taux d'adresses électroniques valides (adresses validées / fiches actives ; cible au moins 95 %), taux de fiches complètes, part des consentements datés.
- Rubriques différentes du dictionnaire (type, domaine de valeurs, règle de calcul, exemple) si elles sont justifiées.
- Propriétaire unique pour toutes les données des supporters (la responsable de la billetterie ou du pôle marketing), si le candidat le justifie ; rôle d'administrateur des données (CDO) proposé à titre illustratif.
- Bus d'intégration ou plateforme d'échange cités, si le principe (zone d'échange, fin des fichiers manuels) reste au premier plan.

**Erreurs types**
- *Qualité laissée à l'informatique* (`JUR-D03`) — « la DSI corrigera les doublons » ; juste : le propriétaire métier fixe les règles, l'intendant les applique, l'informatique outille.
- *Dictionnaire confondu avec le MCD* — le dictionnaire présenté comme un schéma des entités ; juste : le dictionnaire décrit chaque donnée, le MCD leurs relations (F07 § 1).
- *MDM non explicité* (`ET-13`) — sigle employé seul, confondu avec la gestion des terminaux mobiles ; juste : écrire « gestion des données de référence ».
- *Interopérabilité seulement technique* (`ET-36`) — API proposées sans dictionnaire commun ni responsabilités ; juste : technique, sémantique et organisationnelle ensemble.
- *DPO confondu avec le responsable informatique* (`ET-29`) — le délégué tient les outils ou décide des moyens ; juste : il informe, conseille et contrôle, sans conflit d'intérêts.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 25012 (2008) — Modèle de qualité des données | dimensions (exactitude, complétude, unicité, cohérence, actualité), à titre d'exemple | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines données de référence, qualité, métadonnées ; rôles de propriétaire et d'intendant | `dama_dmbok2` / F07 § 8.1-8.2 | en vigueur |
| Dictionnaire de données, données de référence, API et formats ouverts | définitions, principes | F07 § 1 et 7 ; F03 § 3 | notion de cours |

---

### 1.4 – Analyse des données de fidélité (2,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ».

**Annexes mobilisées** : annexes 1.2 (sources, relevé de restauration, doublons) et 1.4 (tableaux A et B, calendrier, campagne de premier abonnement, avis de Mme SOUBIRAC et de Mme ARRIBEUX).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Collecte, nettoyage et structuration illustrés par le cas | 0,5 |
| a-2 | Analyse et restitution illustrées par le cas | 0,5 |
| b-1 | Deux constats chiffrés de l'annexe 1.4, chacun assorti d'une hypothèse explicative | 0,5 |
| b-2 | Deux précautions de lecture tirées des annexes (rupture de série, échantillon de la restauration, données provisoires, corrélation et causalité) | 0,5 |
| c | Méthode exploratoire (segmentation des abonnés) recommandée et justifiée ; prédiction prématurée pour deux raisons tirées des annexes | 0,5 |

**Réponse indicative**

*1.4 a) – Chaîne de traitement* (1 pt : 0,5 pour les étapes 1 à 3, 0,5 pour les étapes 4 et 5)

1. **Collecte** : abonnements et billets de la billetterie, passages du contrôle d'accès (par carte, depuis 2026-2027), commandes de la boutique, relevé de restauration, ouvertures de la lettre et usage de l'application, récupérés par les API plutôt que par des exports ; finalité de l'analyse inscrite au registre.
2. **Nettoyage** : dédoublonnage des fiches (40 % de doublons), rapprochement des commandes et des abonnements par le numéro de supporter, traitement des valeurs manquantes (dates de naissance, codes postaux), repérage des valeurs aberrantes (carte lue deux fois au même match, abonné compté présent à plus de quinze matchs), harmonisation des champs libres.
3. **Structuration** : chargement dans une base d'analyse organisée selon le modèle de la question 1.2 (présences par abonnement et par match, abonnements par saison et par tribune), avec des définitions communes (taux de réabonnement, taux de présence) et des séries rendues comparables ou explicitement séparées avant et après 2026-2027.
4. **Analyse** : comparaisons par saison, par tribune, par ancienneté et par formule ; croisements entre présence, dépenses et réabonnement, au niveau de chaque abonné.
5. **Restitution** : tableau de bord de la fidélité pour la directrice générale et la billetterie (taux de réabonnement par tribune et par ancienneté, présence, dépense), commenté, avec les précautions de lecture, et mis à jour à chaque match et à chaque campagne d'abonnement.

*1.4 b) – Diagnostic argumenté de la fidélité*

**Deux constats et deux hypothèses** (0,5 pt) :
1. **L'attrition des abonnés s'accroît, masquée par le recrutement** : le taux de réabonnement passe de 90 % à 85 % puis 80 % en trois saisons, alors que le nombre d'abonnés reste de 7 000 ; il faut donc remplacer 1 400 abonnés pour 2026-2027, contre 700 deux saisons plus tôt (20 % des abonnés sont dans leur première saison). L'érosion se concentre dans les tribunes Sud (65 %) et Nord (70 %), contre 92 % en Ouest. *Hypothèse* : les abonnés recrutés par la campagne « premier abonnement à moitié prix », ciblée sur Nord et Sud, se réabonnent moins une fois revenus au plein tarif ; la fidélité serait achetée pour une saison.
2. **La présence des abonnés recule, surtout hors de la tribune d'honneur** : de 82 % à 72 % entre 2025-2026 et 2026-2027 ; de 2 points en Ouest (90 % à 88 %) mais de 14 à 16 points en Est, Nord et Sud (Sud : 64 % à 48 %). Les tribunes les moins présentes en 2025-2026 sont aussi celles qui se sont le moins réabonnées. *Hypothèse* : la programmation de six matchs le vendredi à 21 heures (deux auparavant) éloigne les familles et les jeunes (témoignage de Mme ARRIBEUX sur la tribune Nord) ; une moindre présence pourrait annoncer un non-réabonnement, à vérifier abonné par abonné.

**Deux précautions de lecture** (0,5 pt) :
- **Rupture de série** : jusqu'en 2025-2026, la présence est une estimation (entrées par tribune moins billets vendus, sans les invités ni les enfants), sans doute surestimée ; depuis 2026-2027, chaque carte est lue. Une partie de la baisse de 10 points peut tenir au changement de mesure ; seule la comparaison entre tribunes au sein d'une même saison est sûre, et la série 2026-2027 sert de nouvelle base.
- **Données partielles, agrégées et provisoires** : la dépense de restauration ne porte que sur l'abonné sur trois qui paie avec la carte rechargeable (échantillon non représentatif) ; les chiffres de 2026-2027 sont provisoires ; trois saisons ne font pas une tendance ; des moyennes par tribune ne disent rien des comportements individuels, et la concomitance entre présence et réabonnement est une corrélation, non une causalité (d'autres facteurs : résultats sportifs, prix, calendrier).

*1.4 c) – Méthode recommandée* (0,5 pt)

L'analyse **descriptive** (ce qui s'est passé) est déjà faite par l'annexe 1.4 ; la prochaine étape est une analyse **exploratoire** : une **segmentation des abonnés**, c'est-à-dire leur regroupement en profils homogènes selon l'ancienneté, la formule, la tribune, la présence, la dépense et la réaction aux matchs du vendredi, pour repérer les profils qui ne se réabonnent pas et tester les hypothèses du b) (par exemple : « jeunes recrutés à moitié prix, présents moins d'un match sur deux »). Elle répond à la question de la directrice générale (qui fidéliser, par quelle offre) et reste compréhensible par la billetterie.

Une approche **prédictive** (score de désabonnement par abonné, proposée à Mme SOUBIRAC) est prématurée ; deux arguments sont attendus, parmi les suivants : (1) elle apprend sur un historique individuel fiable, or le club ne relie pas encore les présences, les achats et les réabonnements d'une même personne (pas d'identifiant commun, 40 % de doublons) ; (2) la présence individuelle n'existe que depuis une saison et la série est rompue, ce qui ne laisse ni historique ni exemples suffisants ; (3) envoyer « tous nos fichiers » à l'agence, sans finalité définie ni mise à jour du registre, contredit les repères de l'annexe 1.5 (finalités déterminées, minimisation, contrat avec un sous-traitant) ; (4) un score que personne n'explique ne dirait pas quelle offre proposer. La prédiction pourra être envisagée après une ou deux saisons de données propres, sur les seules données nécessaires.

**Réponses tolérées**
- Autres constats tirés de l'annexe 1.4 (dépense à la boutique quatre fois plus élevée en Ouest qu'en Sud, dépense en hausse de 70 € à 80 € par abonné, stabilité de la dépense de restauration), s'ils sont assortis d'une hypothèse.
- Chaîne présentée selon la chaîne décisionnelle (collecte, extraction, transformation et chargement, entrepôt, restitution), si les cinq étapes de la question y sont reconnaissables.
- Analyse de cohortes (suivi des abonnés recrutés une même saison) proposée à la place ou en complément de la segmentation : acceptée, c'est une démarche exploratoire.
- Visualisation proposée pour la restitution (courbes par tribune, histogrammes par ancienneté), si elle sert le diagnostic.

**Erreurs types**
- *Corrélation = causalité* (`ET-26`) — « les abonnés qui viennent moins se désabonnent : les matchs du vendredi font partir les abonnés » ; juste : hypothèse à vérifier abonné par abonné.
- *Extrapolation sans précaution* (`JUR-D06`) — comparer les présences de 2025-2026 et de 2026-2027 sans voir le changement de mesure ; juste : rupture de série signalée.
- *Science des données = BI* (`ET-25`) — confondre le tableau de bord descriptif et la prédiction ; juste : descriptif, exploratoire et prédictif ont des finalités et des exigences de données différentes.
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — l'outil de l'agence présenté comme un assistant conversationnel ; juste : la prédiction des désabonnements relève de l'apprentissage automatique sur données historiques.
- *Calculs inutiles* (`JUR-T07`) — recalcul des moyennes pondérées ; juste : interpréter les écarts lus dans les tableaux.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne décisionnelle ; nettoyage décrit, non exécuté | étapes, points de vigilance | F08 § 1 | notion de cours |
| Analyses descriptive, exploratoire, prédictive | finalités, prérequis, limites | F08 § 2 | notion de cours |

---

### 1.5 – Valeur des données des supporters et demande du partenaire (2,5 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.f` « Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques » ; `2.3.e` « Aspects réglementaires (RGPD, archivage légal) et monétisation des données ».

**Annexes mobilisées** : annexes 1.1 (recettes, plan « MONTALBRET 2030 »), 1.2 (consentements, registre, absence de délégué, application captive), 1.4 (dépenses, propositions de VIRANDEL Automobiles, avis de M. BARRALOU et de l'association de supporters) et 1.5 (repères du RGPD et de la directive ePrivacy).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Patrimoine immatériel montré par la valeur d'usage et la valeur d'échange des données, appliquées au cas | 0,5 |
| a-2 | Trois risques sur cet actif tirés des annexes (perte de confiance, non-conformité, obsolescence et mauvaise qualité, perte de maîtrise ou dépendance, fuite) | 0,5 |
| b-1 | Trois formules distinguées et évaluées : vente (transfert et libre réutilisation), mise à disposition (accès des équipes du partenaire), campagne réalisée par le club (aucune donnée transmise) | 1 |
| b-2 | Position recommandée (campagne pour le compte du partenaire, sur les seuls supporters qui ont consenti aux offres des partenaires) et deux conditions | 0,5 |

**Réponse indicative**

*1.5 a) – Un patrimoine immatériel et ses risques*

Un patrimoine immatériel est un ensemble de ressources non physiques que l'organisation contrôle et dont elle attend des avantages futurs ; les données des supporters en font partie, même si elles ne figurent pas au bilan (0,5 pt avec l'application) :
- **valeur d'usage** : elles servent à fidéliser 7 000 abonnés (6 M€ de billetterie et d'abonnements), à cibler les offres de la boutique (les abonnés y dépensent 80 € par saison en 2026-2027, soit environ 560 k€, plus du quart des 2 M€ de boutique et licences de 2025-2026 ; le constat tient avec 75 € en 2025-2026) et à prouver aux partenaires la qualité de l'audience du club (11 M€ de partenariats, première recette) : elles sont au cœur de la priorité du plan « MONTALBRET 2030 » sur les recettes hors droits sportifs ;
- **valeur d'échange** : un partenaire est prêt à payer pour y accéder (annexe 1.4) ; cette valeur dépend de leur qualité (72 000 personnes réelles, non 120 000 fiches), de leur exclusivité et de la confiance des supporters.

Trois risques (0,5 pt) :
1. **Perte de confiance** : une communication jugée abusive ferait fuir les supporters (« beaucoup d'entre nous rendront leur carte ») ; l'actif se détruit en même temps que la relation.
2. **Non-conformité et inexploitabilité** : consentements aux offres des partenaires tracés pour 8 000 fiches seulement, 10 000 fiches d'origine inconnue, registre non tenu à jour depuis 2019, aucun délégué désigné, fiches conservées depuis 2012 ; une grande partie du fichier ne peut pas être utilisée pour la prospection.
3. **Dépréciation et perte de maîtrise** : doublons, adresses invalides et fiches incomplètes diminuent la valeur ; les données d'usage de l'application restent chez l'agence ; une fuite (fichier copié chez un partenaire, tableur des loges) exposerait le club.

*1.5 b) – Les trois formules de VIRANDEL Automobiles et la position recommandée*

Évaluation (1 pt) :

| Formule | Nature | Repères de l'annexe 1.5 | Enjeux économiques | Confiance des supporters | Appréciation |
|---|---|---|---|---|---|
| Achat du fichier (50 000 fiches, 1 € par fiche, réutilisation libre) | **vente** : transfert définitif d'une copie ; le partenaire devient responsable de ses propres traitements | finalité nouvelle (prospection d'un tiers) étrangère à celle de la collecte (billetterie) ; prospection par courriel sans consentement préalable des personnes aux offres des partenaires, recueilli pour 8 000 fiches seulement ; registre et destinataires à revoir | 50 000 € : moins de 0,5 % des 11 M€ de partenariats, environ 17 % du contrat de VIRANDEL ; recette unique, exclusivité perdue, demandes des autres partenaires (M. BARRALOU) | rupture : vente des adresses perçue comme une trahison (association de supporters) | à refuser |
| Accès permanent à un espace de sélection (30 000 € par saison) | **mise à disposition** : les équipes du partenaire consultent et choisissent elles-mêmes les supporters | mêmes limites que la vente ; le club ne maîtrise plus qui accède à quoi ; minimisation impossible ; sécurité et journalisation des accès à prévoir | recette récurrente modeste ; coût et risque d'un accès externe au référentiel | profilage des supporters par un concessionnaire : perte de contrôle visible | à refuser |
| Campagne cofinancée (10 000 € par campagne) | **campagne réalisée par le club pour le compte du partenaire** : le club sélectionne et adresse l'offre ; seuls des résultats d'ensemble et les coordonnées des volontaires qui remplissent le formulaire du partenaire lui parviennent | aucune donnée transmise par le club ; le club reste responsable de son traitement ; prospection limitée aux supporters qui ont consenti aux offres des partenaires ; registre complété | recette répétable (par exemple trois campagnes : 30 000 € par saison), offre reproductible pour d'autres partenaires sans céder l'actif | acceptable si elle respecte les choix exprimés et reste rare | à retenir |

Les montants se lisent de tête ; la vente rapporte peu au regard du risque qu'elle fait peser sur les 6 M€ de billetterie et sur la relation avec 250 partenaires qui viennent chercher une audience fidèle.

**Position recommandée** (0,5 pt) : refuser la vente et la mise à disposition ; accepter la campagne réalisée par le club pour le compte de VIRANDEL Automobiles, et en faire une offre type pour les partenaires, à deux conditions :
1. **ne viser que les supporters qui ont consenti aux offres des partenaires**, avec une preuve datée (8 000 fiches aujourd'hui), après dédoublonnage ; lancer un recueil des préférences clair et séparé (offres du club, offres des partenaires) dans toutes les applications avant d'élargir la cible ;
2. **encadrer le dispositif** : mettre à jour le registre des traitements (finalité, catégories de destinataires) et désigner un délégué à la protection des données, qui donne son avis ; contrat avec le partenaire interdisant toute transmission de données autres que celles des volontaires, limitant le nombre de campagnes par saison et prévoyant un bilan anonyme ; lien de désinscription dans chaque message.

**Réponses tolérées**
- Cible élargie aux 15 000 fiches de la lettre d'information après une campagne de reconfirmation qui recueille un consentement daté : acceptée, la condition restant le consentement daté.
- Recommandation d'un refus total pour la saison 2027-2028, le temps de fiabiliser les consentements, si elle est argumentée (8 000 fiches seulement, registre non tenu) : acceptée.
- Mise à disposition de données **agrégées et anonymes** (profil de l'audience par âge et par commune, sans aucune donnée individuelle) proposée en complément au partenaire : valorisée.
- Désignation du délégué présentée comme vraisemblablement obligatoire au regard du suivi des supporters (repère de l'annexe 1.5) : acceptée si elle reste prudente et ne développe pas d'analyse juridique.
- Autres risques pertinents (concentration sur un seul partenaire, dépendance à l'éditeur du SaaS) s'ils sont tirés des annexes.

**Erreurs types**
- *Monétisation présentée sans regard critique* (`JUR-N01`) — « 50 000 € de recettes nouvelles sans coût » ; juste : modèle économique, conformité et éthique mis en balance.
- *Analyse juridique hors programme* (`JUR-T07`) — développement sur les bases légales, les droits des personnes ou les sanctions de l'autorité de contrôle ; juste : s'en tenir aux repères fournis et à leur application.
- *Rôle du délégué méconnu* (`JUR-D05`, `ET-29`) — délégué présenté comme responsable du traitement ou comme technicien ; juste : il informe, conseille et contrôle ; la décision et la responsabilité restent au club.
- *Définition sans application au cas* (`JUR-T01`) — patrimoine immatériel défini sans les recettes du club, les 72 000 personnes ni la menace de l'association de supporters.
- *Données comptabilisées* — valeur des données chiffrée comme un actif au bilan ; juste : valeur d'usage et d'échange appréciées, sans traitement comptable (UE 4).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | finalités, minimisation, durée de conservation, responsable et sous-traitant, registre, délégué à la protection des données (repères de l'annexe 1.5) | `rgpd` / F15 § 1, 2 et 5 | en vigueur |
| Directive 2002/58/CE « vie privée et communications électroniques », modifiée en 2009 | consentement préalable à la prospection par courrier électronique (repère de l'annexe 1.5) | `eprivacy` | en vigueur |
| Monétisation et valeur des données (approche critique) | modèles, limites économiques et éthiques, donnée comme actif | F07 § 8.6 | notion de cours |

---

## DOSSIER 2 – GOUVERNER LE NUMÉRIQUE DU CLUB ET ÉVALUER LE PROJET DE JETONS DE SUPPORTERS (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Gouvernance et organisation du numérique du club | `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ; `1.2.b` Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 3 |
| 2.2 Maturité numérique et tableau de bord du SI | `1.2.d` Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) ; `1.2.e` Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) | 2 |
| 2.3 Chaîne de valeur et planification stratégique du SI | `1.1.b` Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) ; `1.1.c` Méthodologies de planification stratégique du SI ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 2,5 |
| 2.4 Le projet de jetons de supporters | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ; `3.3.d` Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO ; `3.3.a` Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations | 3,5 |
| 2.5 Coût du projet et projet de contrat | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `1.4.b` Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) ; `1.4.c` Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD ; `1.4.a` Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques | 2 |
| **Dossier 2 – Gouverner le numérique du club et évaluer le projet de jetons de supporters** |  | **13** |

Répartition indicative : connaissances (gouvernance du SI, modèles et référentiels de maturité, chaîne de valeur, fonctionnement d'une blockchain, coût total de possession) 2,5 points (items 2.1 a-1, 2.2 a-1, 2.3 a-1, 2.4 a-1, 2.5 a-1) ; analyse des annexes et recommandations 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Gouvernance et organisation du numérique du club (3 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité » ; `1.2.b` « Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ».

**Annexes mobilisées** : annexes 2.1 (organisation, dépenses, décisions, témoignages) et 1.1 (organigramme : informatique rattachée au responsable administratif et financier, directions rattachées à la directrice générale).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance du SI définie (la direction évalue, oriente et surveille l'usage du SI au service de la stratégie ; distincte du management ; parties prenantes) | 0,5 |
| a-2 | Modèle de fait caractérisé (décentralisé de fait autour d'un socle centralisé minimal, SI parallèle des directions) et trois effets appuyés sur les chiffres de l'annexe 2.1 | 0,5 |
| a-3 | Enjeux relationnels analysés entre la directrice générale, l'informatique et les directions métiers (positions, causes, conséquences), appuyés sur les témoignages | 0,5 |
| b-1 | Modèle cible recommandé et justifié par la taille du club, ses ressources et ses besoins d'agilité | 0,5 |
| b-2 | Deux instances de gouvernance avec composition, fréquence et décisions | 0,5 |
| b-3 | Trois règles d'achat et d'usage des services en ligne, opérationnelles et reliées aux constats | 0,5 |

**Réponse attendue**

*2.1 a) – Définition, modèle de fait et enjeux relationnels*

La **gouvernance du système d'information** est l'ensemble des structures, des processus et des règles par lesquels la direction **évalue** les besoins et les options, **oriente** les choix (priorités, arbitrages, moyens) et **surveille** la performance, les risques et la conformité du SI au service de la stratégie (modèle « évaluer, diriger, surveiller » d'ISO/IEC 38500:2024 et de COBIT 2019). Elle se distingue du **management** du SI, qui planifie, construit et exploite selon ces orientations. Elle associe les parties prenantes : conseil d'administration, directrice générale, directions métiers, informatique, prestataires (0,5 pt). Au club, cette gouvernance n'existe pas : personne n'arbitre ni ne surveille, et le conseil d'administration n'a jamais traité du numérique.

**Modèle organisationnel de fait** : un **socle centralisé minimal** (deux personnes et un infogérant, rattachés au responsable administratif et financier, qui gèrent les postes, la messagerie, le réseau et les logiciels de gestion) et, autour, une organisation **décentralisée de fait** : chaque direction choisit, achète et administre ses propres outils, hors de tout cadre. Ce n'est pas un modèle choisi (fédéral ou bimodal), mais une juxtaposition : un **SI parallèle** (« shadow IT ») qui s'est développé faute de réponse de l'informatique.

Trois effets (0,5 pt pour le modèle et trois effets chiffrés) :
1. **Des dépenses non pilotées** : 400 k€ de dépenses numériques échappent au budget du SI, soit près d'un tiers des 1,3 M€ dépensés par le club ; la directrice générale « découvre les projets quand la facture arrive » et ne peut pas comparer les demandes.
2. **Des risques non maîtrisés** : 23 services en ligne souscrits par carte bancaire ou note de frais, aux conditions générales des fournisseurs, dont l'informatique n'administre que 11 ; accès des salariés partis restés ouverts ; données physiques des joueurs stockées on ne sait où ; tablettes personnelles du staff.
3. **Des projets décidés au fil des opportunités et une informatique cantonnée au dépannage** : application mobile, analyse vidéo, jetons proposés par des fournisseurs et découverts tard par l'informatique ; 80 % de son temps au support, quatre mois de réponse aux demandes ; aucun plan pluriannuel ne relie ces projets au plan « MONTALBRET 2030 ».

**Enjeux relationnels** (0,5 pt) :
- **Directrice générale et informatique** : l'informatique, rattachée au responsable administratif et financier, est perçue comme une fonction de support technique, non comme un partenaire de la stratégie ; la directrice générale porte le plan devant le conseil sans instrument pour piloter son deuxième axe.
- **Informatique et directions métiers** : une relation de **fournisseur débordé** à clients impatients. Le marketing contourne un « guichet qui dit non » (Mme SOUBIRAC) ; l'informatique subit les conséquences (« on nous appelle quand ça ne marche plus », M. PEYRASTRE) sans avoir été consultée ; la direction sportive revendique l'autonomie de ses outils au nom de l'avantage sportif (M. TOURNEBIAU).
- **Entre directions** : aucune instance ne permet de confronter les priorités ; les arbitrages se font en tête à tête avec la directrice générale, au profit de la direction qui la sollicite au bon moment (le projet de jetons est même porté directement au président).
- **Points d'appui** : chacun reconnaît le besoin d'un cadre (M. PEYRASTRE veut « au moins savoir ce qui existe », Mme SOUBIRAC accepte « des règles », M. TOURNEBIAU admet ne pas savoir où sont les données) ; la nouvelle responsabilité du SI confiée au responsable administratif et financier en est l'occasion.

*2.1 b) – Modèle cible, instances et règles d'achat*

**Modèle recommandé** (0,5 pt) : une **organisation centralisée légère**, adaptée à un club de 150 salariés dont les dépenses numériques atteignent 1,3 M€ : l'informatique (responsable informatique, technicien, infogérant) devient le point unique de cohérence pour le socle, la sécurité, les contrats, les accès et le catalogue des services, sous la responsabilité du responsable administratif et financier, qui rend compte à la directrice générale ; elle s'appuie sur un **correspondant numérique** dans chaque direction (marketing et numérique, sportive, commerciale, billetterie). Les directions gardent l'initiative de leurs besoins et peuvent **expérimenter** des outils en ligne dans un cadre défini (durée, coût, données), ce qui répond à l'agilité demandée par le marketing sans recréer un SI parallèle. Une organisation décentralisée assumée ou fédérale, avec des équipes informatiques par direction, n'est pas à la portée d'un club de cette taille ; une organisation bimodale au sens strict (deux équipes, l'une pour la stabilité, l'autre pour l'innovation) supposerait des effectifs qu'il n'a pas, mais son principe est retenu sous forme d'un « couloir d'expérimentation ».

**Deux instances de gouvernance** (0,5 pt) :

| Instance | Composition | Fréquence | Décisions |
|---|---|---|---|
| **Comité du numérique** (instance stratégique) | directrice générale (présidente), responsable administratif et financier chargé du SI (animateur), directeur sportif, directeur commercial et des partenariats, responsables du pôle marketing et numérique, de la billetterie, du stade et de la sécurité ; responsable informatique ; prestataires invités selon l'ordre du jour | trimestrielle, avant chaque conseil d'administration | valide le plan du SI et ses révisions, arbitre le portefeuille de projets selon des critères communs (question 2.3 b), fixe les règles d'achat des services en ligne, suit le tableau de bord (question 2.2 b) ; décide des projets innovants (jetons) ; prépare le point « numérique » présenté au conseil d'administration, où siège l'association |
| **Revue mensuelle des demandes et des services** (instance de pilotage) | responsable administratif et financier, responsable informatique, correspondants numériques des directions | mensuelle (et à la demande pendant la saison) | instruit les demandes (besoin, coût complet, données, risques) et rend un avis en moins d'un mois ; tient le catalogue des services ; lance les expérimentations dans le cadre fixé ; suit les contrats et les incidents |

**Trois règles d'achat et d'usage des services en ligne** (0,5 pt) :
1. **Déclaration préalable et catalogue** : aucun service en ligne n'est souscrit sans être inscrit au catalogue tenu par l'informatique ; les 23 services existants y sont recensés d'ici la fin de 2027 et ceux qui font double emploi sont arrêtés ; plus de paiement par carte bancaire ou note de frais hors catalogue.
2. **Avis de l'informatique et contrat négocié selon le risque** : tout service qui traite des données de personnes (supporters, joueurs, partenaires) ou qui dépasse un seuil annuel fixé par le comité passe par l'avis de l'informatique (sécurité, localisation des données, réversibilité, coût complet) dans un délai d'un mois au plus, et le contrat est signé par le club ; en deçà, la direction souscrit seule dans le cadre d'une expérimentation limitée (durée de six mois, sans données sensibles, bilan à la revue mensuelle).
3. **Accès et cycle de vie** : comptes nominatifs, accès d'administration détenus par l'informatique en plus de la direction, retrait des accès au départ d'un salarié, outils professionnels sur des équipements du club (fin des tablettes personnelles pour les données des joueurs), données exportables à la fin de chaque contrat.

**Réponses tolérées**
- Gouvernance définie à partir des six principes d'ISO/IEC 38500:2024 ou des domaines de COBIT 2019 (EDM pour la gouvernance), si la distinction avec le management apparaît.
- Modèle de fait qualifié d'« éclaté », de « SI fantôme » ou de « décentralisation subie », si le socle centralisé minimal et l'autonomie non encadrée des directions sont décrits.
- Modèle cible fédéral « léger » (correspondants dans les directions, cadre commun fixé par le centre) ou bimodal adapté (socle stable et expérimentations encadrées), s'il est justifié par la taille et les ressources du club ; rattachement de l'informatique à la directrice générale proposé et justifié.
- Instances nommées autrement (comité stratégique du SI, comité de portefeuille, comité des projets), ou conseil d'administration retenu comme l'une des deux instances avec un point numérique annuel, si composition, fréquence et décisions sont précisées.
- Règle de seuil chiffré différente, ou règle de revue annuelle des contrats, si elle répond à un constat de l'annexe 2.1.

**Erreurs fréquentes**
- *Modèles récités sans le cas* (`JUR-T01` contextualiser chaque notion) — tableau des cinq modèles sans dire lequel existe de fait au club ; juste : caractériser l'existant à partir des chiffres de l'annexe 2.1.
- *Solution démesurée* (`JUR-G05` analyser les déséquilibres organisationnels et recommander de façon réaliste) — créer une direction des systèmes d'information de dix personnes, des comités hebdomadaires ; juste : deux personnes et un infogérant, des correspondants et deux instances.
- *Interdire le SI parallèle sans alternative* (`JUR-G05` analyser les déséquilibres organisationnels et recommander de façon réaliste) — « tout outil non validé est supprimé » ; juste : catalogue, avis rapide et couloir d'expérimentation qui répondent au besoin d'agilité.
- *Gouvernance réduite à la technique ou à la sécurité* (`JUR-G06` vocabulaire précis de la gouvernance) — liste de mesures techniques ; juste : décisions, rôles, arbitrages et suivi par la direction.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 38500:2024 — gouvernance des technologies de l'information | évaluer, diriger, surveiller ; gouvernance et management | `iso_38500_2024` / F02 § 4 | en vigueur |
| COBIT 2019 (ISACA) | distinction gouvernance / management, domaine EDM | `cobit_2019` / F02 § 3 | en vigueur |
| Modèles organisationnels de la fonction informatique | centralisé, décentralisé, fédéral, bimodal | F01 § 4 | notion de cours |
| Comitologie du SI | comité stratégique, comité de portefeuille | F02 § 6 | notion de cours |
| SI parallèle (« shadow IT ») | services souscrits hors de l'informatique | F04 § 6 | notion de cours |

---

### 2.2 – Maturité numérique et tableau de bord du SI (2 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.d` « Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) » ; `1.2.e` « Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) ». Limite : « Le pilotage ESG est à comprendre dans une logique d'indicateurs intégrés, non isolés. »

**Annexes mobilisées** : annexes 2.2 (autodiagnostic), 2.1 (dépenses, services en ligne, délai des demandes, formation) et 1.1 (effectif).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Intérêt et deux limites d'une évaluation de la maturité, avec un modèle ou un référentiel cité correctement (CMMI, COBIT 2019, MAGNum 2026) | 0,5 |
| a-2 | Deux forces, deux faiblesses et deux biais tirés de la grille de l'annexe 2.2 | 0,5 |
| b | Quatre indicateurs complets (formule, source, fréquence, cible, axe), dont au moins un ESG, reliés aux constats ; 0,5 pour deux indicateurs complets | 1 |

**Réponse attendue**

*2.2 a) – Évaluation de la maturité et lecture de la grille*

Une **évaluation de la maturité numérique** positionne l'organisation, domaine par domaine, sur une échelle de niveaux décrits par des pratiques observables, puis fixe une cible et un plan de progression. Le **CMMI** (ISACA) propose cinq niveaux de maturité (initial, géré, défini, géré quantitativement, en optimisation), dont s'inspire l'échelle de l'annexe 2.2 ; **COBIT 2019** évalue la capacité des processus de 0 à 5 ; **MAGNum 2026** (ISACA, CIGREF, IFACI) est un modèle de maturité et d'audit de la gouvernance du numérique.
- **Intérêt** : un langage commun entre directions, un diagnostic partagé et comparable dans le temps, la priorisation des efforts sur les domaines les plus faibles, un point de départ pour la planification (question 2.3) et pour le tableau de bord.
- **Limites** : une note ne vaut que par ses preuves (une autoévaluation est subjective) ; une moyenne masque les écarts ; la grille mesure des pratiques, pas la valeur créée ; viser le niveau 5 partout n'a pas de sens pour un club de cette taille, la cible doit être choisie domaine par domaine ; un modèle de maturité n'est pas une certification (0,5 pt pour l'intérêt et deux limites, avec un référentiel cité).

**Lecture de la grille** (0,5 pt) :
- **Deux forces** : *applications et outils* (moyenne 3) et *compétences et usages* (moyenne 3) : les directions disposent d'outils récents et les équipes du marketing et du staff sportif s'en servent (4 sur les compétences). Mais la force des outils est fragile : elle repose sur les notes de 5 du marketing et de la direction sportive, alors que l'informatique note 2 et la direction commerciale 1 ; ce sont des outils nombreux et modernes, non un ensemble cohérent.
- **Deux faiblesses** : *gouvernance et arbitrage des projets* (1,5) et *pilotage et mesure* (1,5), notées faibles par toutes les directions (aucune note au-dessus de 2, écart de 1 seulement) : le constat est **partagé**, ce qui fonde la priorité de la question 2.1 et du tableau de bord. La *stratégie numérique* (2) suit.
- **Deux biais de l'autodiagnostic** : (1) **biais d'autoévaluation et de position** : chaque direction se note sur ce qu'elle voit et surestime son propre domaine (5 pour ses outils au marketing, 4 pour les données à la direction sportive, « nos données de performance sont suivies »), tandis que l'informatique note « ce qu'elle voit remonter au support », au plus bas sur la stratégie et la gouvernance ; (2) **absence de preuves et d'interprétation commune de l'échelle** : chaque directeur a noté seul, sans justificatif, et le niveau 5 du marketing (« amélioration continue à partir des mesures ») est incompatible avec un pilotage noté 2 par ce même pôle ; un écart de 4 points sur les applications montre que les directeurs n'évaluent pas la même chose. La moyenne de 3 sur les applications est donc trompeuse ; il faut une revue contradictoire des notes, avec des preuves, avant de fixer les cibles.

*2.2 b) – Tableau de bord trimestriel du SI*

Le tableau de bord présenté chaque trimestre à la directrice générale (et repris pour le conseil d'administration) suit les quatre axes de l'IT Balanced Scorecard de Van Grembergen (contribution financière, orientation utilisateurs, excellence opérationnelle, orientation future), les dimensions de gouvernance et sociale de l'ESG y étant **intégrées** ; les indicateurs répondent aux faiblesses de l'annexe 2.2.

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des dépenses numériques engagées hors du budget du SI | dépenses numériques payées sur les budgets propres des directions / dépenses numériques totales du club | comptabilité analytique (factures et notes de frais imputées sur une rubrique « numérique ») | trimestrielle, cumul de la saison | 10 % au plus en 2028-2029 (31 % en 2025-2026 : 400 k€ sur 1 300 k€) | contribution financière |
| Part des services en ligne inscrits au catalogue et administrés par le club | services en ligne inscrits au catalogue, avec contrat validé et accès d'administration détenus par l'informatique / services en ligne utilisés par les directions | catalogue des services tenu par l'informatique, rapproché des factures | trimestrielle | 100 % à la fin de la saison 2027-2028 (aucun catalogue ; accès d'administration pour 11 services sur 23) | excellence opérationnelle (G de l'ESG) |
| Délai moyen de décision sur les demandes des directions | somme des jours entre le dépôt de chaque demande et la décision / nombre de demandes décidées dans le trimestre | registre des demandes de la revue mensuelle | trimestrielle | 30 jours au plus dès 2027-2028 (environ quatre mois aujourd'hui) | orientation utilisateurs |
| Part des salariés formés aux usages numériques | salariés permanents, hors joueurs et entraîneurs, ayant suivi dans la saison au moins une formation aux outils numériques du club et à leurs bons usages / salariés permanents hors joueurs et entraîneurs | plan de formation et fichier du personnel | semestrielle | 60 % en 2028-2029 (10 sur 102 en 2026, environ 10 %) | orientation future (S de l'ESG) |

(0,5 pt pour deux indicateurs complets et reliés aux constats ; 1 pt pour quatre, dont au moins un ESG.)

Ces quatre indicateurs sont **équilibrés** : un par axe de l'IT Balanced Scorecard, soit les coûts (contribution financière), la qualité de la réponse aux directions (orientation utilisateurs), la maîtrise des services et des contrats (excellence opérationnelle, qui porte la dimension de gouvernance de l'ESG) et la capacité des équipes (orientation future, qui porte la dimension sociale de l'ESG). Chacun est suivi avec une cible datée et un responsable (responsable administratif et financier pour les deux premiers, revue mensuelle pour le troisième, ressources humaines pour le quatrième).

**Réponses tolérées**
- Autre modèle cité correctement (niveaux de capacité de COBIT 2019, MAGNum 2026), ou CMMI cité sans numéro de version ; vocabulaire des niveaux traduit librement s'ils sont différenciés.
- Forces ou faiblesses choisies autrement (données à 2,5 comme faiblesse, stratégie à 2), si elles sont lues dans la grille et nuancées par les écarts.
- Biais formulés comme « biais de complaisance », « effet de halo », « hétérogénéité de compréhension », « absence de preuves », « moyenne trompeuse », si deux biais distincts sont illustrés par l'annexe.
- Indicateurs de remplacement, s'ils sont complets et reliés à un constat : satisfaction des directions à l'égard de l'informatique (orientation utilisateurs), part du budget du SI consacrée aux projets (orientation future ; 100 k€ sur 900 k€ en 2025-2026), part des projets décidés par le comité du numérique (excellence opérationnelle, G de l'ESG), progression du niveau de maturité revu contradictoirement sur la gouvernance (orientation future), part des comptes des salariés partis désactivés dans la semaine (excellence opérationnelle, G de l'ESG) ; axes du tableau de bord prospectif classique (financier, clients, processus internes, apprentissage) acceptés s'ils sont appliqués au SI.
- Indicateur environnemental (durée de vie moyenne des équipements du club, part des services en ligne arrêtés faute d'usage), s'il est complet et que sa cible est justifiée.

**Erreurs fréquentes**
- *Grille récitée ou plate* (`JUR-T01` contextualiser chaque notion ; corrigé du sujet zéro : « grille sans niveaux différenciés ») — niveaux du CMMI énumérés sans lecture des notes ; juste : forces, faiblesses et biais tirés des chiffres de l'annexe 2.2.
- *Autodiagnostic pris pour une mesure* (`JUR-D06` prudence d'interprétation) — « le club est au niveau 3 sur ses outils » ; juste : notes subjectives, écart de 4 points, revue contradictoire nécessaire.
- *CMMI ou COBIT présentés comme une norme certifiable* (`ET-01` norme, référentiel, solution) ; juste : un modèle de maturité et un référentiel de gouvernance, adaptables.
- *Indicateurs génériques ou incomplets* (`ET-18` indicateurs génériques ; `JUR-A02` justifier chaque indicateur) — « taux de disponibilité » sans source ni cible ; indicateur ESG isolé sans lien avec le SI ; juste : cinq champs et un constat de l'annexe 2.1 derrière chaque indicateur.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| CMMI (ISACA, CMMI Institute) | cinq niveaux de maturité | `cmmi_v3` / F01 § 5, F09 § 5 | en vigueur |
| COBIT 2019 (ISACA) | niveaux de capacité des processus de 0 à 5 | `cobit_2019` / F02 § 3 | en vigueur |
| MAGNum 2026 (ISACA, CIGREF, IFACI) | maturité et audit de la gouvernance du numérique | `magnum_2026` / F01 § 5 | en vigueur |
| IT Balanced Scorecard (Van Grembergen) | axes du tableau de bord du SI | `van_grembergen_it_bsc` / F09 § 4 | modèle théorique |

---

### 2.3 – Chaîne de valeur et planification stratégique du SI (2,5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.b` « Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) » ; `1.1.c` « Méthodologies de planification stratégique du SI » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 1.1 (recettes, plan « MONTALBRET 2030 », organigramme) et 2.1 (dépenses par direction, décisions au fil des opportunités).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de valeur présentée (Porter, 1985 : activités principales et de soutien ; le SI automatise, informe, transforme) et son intérêt pour l'alignement | 0,5 |
| a-2 | Chaîne de valeur du club et trois activités prioritaires, chacune justifiée par les recettes de l'annexe 1.1 et un axe du plan | 0,5 |
| a-3 | Écart entre ces priorités et la répartition actuelle des dépenses numériques (annexe 2.1), et conclusion sur l'alignement | 0,5 |
| b-1 | Démarche de planification en étapes, avec horizon et acteurs | 0,5 |
| b-2 | Trois critères d'arbitrage des projets, appliqués à un exemple du cas | 0,5 |

**Réponse attendue**

*2.3 a) – Chaîne de valeur et activités prioritaires*

La **chaîne de valeur** (Porter, 1985) décompose l'organisation en **activités principales**, qui créent directement la valeur pour le client, et en **activités de soutien**, qui les rendent possibles ; l'avantage concurrentiel naît de la façon dont chaque activité est conduite et dont les activités sont reliées. Pour chaque maillon, le SI peut **automatiser** (productivité), **informer** (pilotage) ou **transformer** (nouveau service, nouvelle relation). Appliquée au SI, elle sert l'**alignement**, mise en cohérence permanente de la stratégie du SI avec celle de l'organisation : elle montre où le SI crée un avantage (y investir) et où il est une commodité (mutualiser, externaliser) (0,5 pt).

**Chaîne de valeur de MONTALBRET XV** : activités principales : formation et performance sportive de l'équipe professionnelle ; organisation des matchs et accueil du public ; commercialisation auprès des supporters (billetterie et abonnements, boutique et licences) ; partenariats et hospitalités ; relation et communication avec les supporters. Activités de soutien : administration et finance, ressources humaines, achats, gestion du stade avec la communauté d'agglomération, système d'information.

Trois activités à soutenir en priorité (0,5 pt) :
1. **Partenariats et hospitalités** : 11 M€ de partenariats et 4 M€ d'hospitalités, soit plus de la moitié des 28 M€ de recettes, auprès de 250 entreprises ; c'est le premier levier des « recettes hors droits sportifs » (axe 1). Le SI doit **informer** (connaissance des partenaires, suivi des contrats, des loges et des invités) et **automatiser** les invitations.
2. **Relation et commercialisation auprès des supporters** : billetterie et abonnements 6 M€, boutique et licences 2 M€, 7 000 abonnés et 120 000 contacts ; axes 1 et 2 (« nouvelles formes de relation avec les supporters »). Le SI peut **transformer** la relation (application, boutique, programme de fidélité) : c'est là que se situe le projet de jetons.
3. **Performance sportive** : l'accession à l'élite d'ici 2030 conditionne l'ensemble des recettes (droits audiovisuels et dotations 5 M€, affluence, attrait pour les partenaires) ; l'analyse des performances et le suivi physique des joueurs sont une source d'avantage concurrentiel, à condition que leurs données soient maîtrisées.

**Alignement actuel** (0,5 pt) : la dépense numérique ne suit pas ces priorités. Le budget du SI va pour près de la moitié (400 k€ sur 900 k€) au socle administratif, activité de soutien, qu'il faut maîtriser et mutualiser ; les partenariats, première recette du club, n'ont que 80 k€ de dépenses numériques (50 + 30) et un tableur (note de 1 de la direction commerciale) ; le pôle marketing et numérique et la direction sportive consomment 520 k€ (350 au pôle marketing et numérique, 170 à la direction sportive), dont 370 k€ hors du budget du SI et de toute stratégie. Le SI est **aligné par accident**, au gré des initiatives des directions, et non par décision : la planification doit réorienter les moyens vers les partenariats et la relation avec les supporters, sans fragiliser le socle.

*2.3 b) – Démarche de planification stratégique du SI*

Une démarche de **schéma directeur** à l'échelle du club (0,5 pt pour les étapes, l'horizon et les acteurs) :
1. **Cadrage** (été 2027) : mandat de la directrice générale, comité du numérique (question 2.1) comme instance de pilotage, responsable administratif et financier comme chef de la démarche, avec le responsable informatique.
2. **Diagnostic** (septembre-octobre 2027) : inventaire des 23 services en ligne et des contrats, dépenses numériques complètes (1,3 M€), revue contradictoire de l'autodiagnostic de l'annexe 2.2, besoins de chaque direction et de l'association.
3. **Orientations** : traduction des trois axes du plan « MONTALBRET 2030 » en objectifs pour le SI, à partir de la chaîne de valeur (a).
4. **Portefeuille de projets et feuille de route** : projets priorisés selon des critères communs, jalons par saison, coûts en ordre de grandeur, ressources (informatique, infogérant, prestataires).
5. **Validation et suivi** : validation par le conseil d'administration, suivi trimestriel par le tableau de bord (question 2.2 b), **révision annuelle à l'intersaison**.

**Horizon** : trois saisons, 2027-2028 à 2029-2030, calé sur l'échéance du plan « MONTALBRET 2030 » et l'objectif d'accession ; révision chaque année et à tout changement de division. **Acteurs** : directrice générale (commanditaire), responsable administratif et financier et responsable informatique (pilotes), directeurs et correspondants numériques (besoins, priorités), infogérant et éditeurs (faisabilité), conseil d'administration, où siège l'association (validation).

**Trois critères d'arbitrage des projets** (0,5 pt) :
1. **Contribution au plan « MONTALBRET 2030 »** : axe servi, recettes ou gains attendus, avec des hypothèses vérifiables ;
2. **Coût complet et capacité à faire** : coût total de possession sur trois saisons, y compris les coûts cachés, rapporté au budget du SI, et charge pour une équipe de deux personnes ;
3. **Risques** : données de personnes (supporters, joueurs), dépendance à un fournisseur, réversibilité, image du club auprès des supporters et de l'association.
Les obligations réglementaires passent en priorité. Appliqué au projet de jetons, qui n'aurait plus été présenté directement au président : contribution à l'axe 2 incertaine, coût de 500 à 700 k€ sur trois saisons, risques élevés (question 2.4) : il serait au mieux classé en expérimentation, après les chantiers des partenariats et des données des supporters.

**Réponses tolérées**
- Chaîne de valeur du club découpée autrement (billetterie et boutique séparées, « jours de match » comme activité principale), si activités principales et de soutien sont distinguées.
- Organisation des jours de match retenue parmi les trois priorités (axe 3 du plan), si le choix est justifié par les annexes, à la place de la performance sportive ou de la relation avec les supporters.
- Recours au modèle SAM de Henderson et Venkatraman (1993) en complément, sans développement.
- Démarche en quatre ou six étapes, horizon de trois à cinq ans, si diagnostic, orientations, portefeuille et suivi y figurent ; critères exprimés comme une grille valeur / risque / coût.

**Erreurs fréquentes**
- *Alignement réduit à un choix technique* (`JUR-G02` alignement réduit à un choix technique ou à une standardisation logicielle ; `ET-06`) — « il faut un logiciel unique de gestion des supporters » ; juste : relier les activités créatrices de valeur aux moyens du SI.
- *Chaîne de valeur récitée sans le club* (`JUR-T01`) — activités génériques d'une entreprise industrielle (logistique d'approvisionnement, production) ; juste : les recettes de l'annexe 1.1 pour hiérarchiser.
- *Schéma directeur confondu avec un plan de projet* (`ET-07` schéma directeur et plan de projet confondus) — calendrier des tâches d'un projet, horizon d'une saison ; juste : diagnostic, orientations, portefeuille, horizon de trois saisons et révision annuelle.
- *Arbitrage sans critère* (`JUR-T03` analyser et argumenter) — liste de projets sans règle de priorité ; juste : trois critères annoncés et appliqués.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de valeur (Porter, 1985) | activités principales et de soutien ; automatiser, informer, transformer | `porter_chaine_valeur_1985` / F01 § 2 | modèle théorique |
| Schéma directeur et portefeuille de projets | étapes, horizon, critères d'arbitrage | F01 § 3 | notion de cours |

---

### 2.4 – Le projet de jetons de supporters (3,5 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain » ; `3.3.d` « Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO » ; `3.3.a` « Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations ». Limite : « Les effets environnementaux et énergétiques doivent être intégrés dans l'analyse ».

**Annexes mobilisées** : annexes 2.3 (proposition, coûts, sondage, avis, contrat), 2.4 (repères) et 1.1 (abonnés, plan « MONTALBRET 2030 », contrôle d'accès par billet dématérialisé).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fonctionnement d'une blockchain (registre distribué, blocs chaînés, consensus, clés publique et privée, publique ou permissionnée) et distinction avec une base de données centralisée | 0,5 |
| a-2 | Volet 1 rattaché aux jetons fongibles (crypto-actifs donnant accès à des avantages) ; volet 2 aux jetons uniques non fongibles (NFT) au service de la certification et de la traçabilité des billets | 0,5 |
| b-1 | Grille d'opportunité de cinq critères, énoncée et justifiée | 0,5 |
| b-2 | Volet 1 apprécié critère par critère (valeur ajoutée, limites : énergie, gouvernance, données personnelles, image), avec les faits de l'annexe 2.3 | 0,5 |
| b-3 | Volet 2 apprécié (alternative centralisée existante, oracle au contrôle d'accès, données personnelles, coût) | 0,5 |
| c-1 | Deux éléments encadrés par MiCA (offre au public des jetons fongibles, services de conservation et d'échange réservés aux PSCA agréés) et un élément non encadré (billets uniques non fongibles, ou aspects comptables et fiscaux), d'après l'annexe 2.4 | 0,5 |
| c-2 | Recommandation argumentée et conditionnée à Mme LAFERRADE | 0,5 |

**Réponse attendue**

*2.4 a) – Fonctionnement et typologie*

Une **blockchain** est un **registre distribué** : la même liste de transactions est répliquée entre de nombreux **nœuds**, sans administrateur unique. Les transactions sont regroupées en **blocs** chaînés : chaque bloc contient l'empreinte (hachage) du précédent, si bien qu'une modification d'un bloc passé se voit et invalide la suite : le registre est pratiquement inaltérable. Les nœuds s'accordent sur l'état du registre par un **mécanisme de consensus** : preuve de travail (calcul coûteux, très énergivore), preuve d'enjeu (validateurs choisis selon les jetons qu'ils immobilisent, consommation bien plus faible), ou validation par des participants identifiés. Chaque utilisateur signe ses opérations avec sa **clé privée** et est reconnu par sa **clé publique** (adresse du portefeuille) : perdre la clé privée, c'est perdre ses jetons, d'où les services de conservation. Une blockchain **publique** est ouverte à tous en lecture et en validation ; une blockchain **permissionnée** (privée ou de consortium) réserve la validation à des participants identifiés. Une **base de données centralisée** est tenue par un administrateur unique, qui écrit, corrige et efface, et en qui les utilisateurs ont confiance ; elle est plus rapide, moins chère et plus sobre. La blockchain n'a d'intérêt que pour organiser la confiance entre des acteurs qui écrivent dans un même registre sans tiers de confiance accepté (0,5 pt).

**Typologie** (0,5 pt) :
- **Volet 1** : émission de **jetons fongibles**, tous identiques et interchangeables, achetés en euros et revendables sur des plateformes d'échange : ce sont des **crypto-actifs** qui donnent accès à des avantages (votes, tirages au sort, priorité d'achat) ; ils relèvent de la **tokenisation** de droits d'accès à des avantages ; ce n'est pas de la finance décentralisée, puisque leur conservation et leur échange contre des euros passent par un prestataire intermédiaire agréé. Ce ne sont pas des NFT.
- **Volet 2** : chaque billet est un **jeton unique et non fongible (NFT)** ; l'usage visé est la **certification** de l'authenticité du billet et la **traçabilité** de ses reventes.

*2.4 b) – Grille d'opportunité et appréciation des deux volets*

**Grille d'opportunité** (0,5 pt) : (1) plusieurs acteurs doivent-ils écrire dans le même registre sans tiers de confiance accepté ? (2) faut-il un enregistrement inaltérable et horodaté, et la donnée inscrite est-elle fiable (oracle) ? (3) les données peuvent-elles être inscrites sur un registre partagé et inaltérable (données personnelles) ? (4) le coût et l'empreinte énergétique sont-ils justifiés ? (5) la gouvernance du registre et l'effet sur l'image du club sont-ils acceptables ? Si la réponse aux deux premières questions est négative, une base de données centralisée tenue par le club suffit.

| Critère | Volet 1 – jetons de supporters | Volet 2 – billets sur le registre distribué |
|---|---|---|
| 1. Plusieurs écrivains sans tiers de confiance | **non** : le club seul émet les jetons, définit les avantages et organise des votes consultatifs ; les supporters font déjà confiance au club | **non** : le club est le seul émetteur des billets ; sa billetterie fait foi, et sa bourse de revente à prix plafonné existe déjà (1 500 reventes) |
| 2. Inaltérabilité utile et donnée fiable | faible : un vote consultatif sur la mascotte n'exige pas un registre inaltérable ; le résultat n'engage pas le club | **oracle** : la blockchain prouve qui détient le jeton, pas qui se présente au contrôle d'accès (Mme ARRIBEUX) ; les 300 reventes sur les réseaux sociaux se règlent par le billet nominatif et la bourse existante |
| 3. Données personnelles | adresses de portefeuille et votes inscrits « pour la transparence » sur une blockchain publique : inaltérables, ils contrarient la minimisation et l'effacement des données prévus par le RGPD (annexe 2.4) | numéro de client et pseudonyme inscrits sur un registre public : effacement impossible, données réidentifiables ; à proscrire |
| 4. Coût et énergie | 500 k€ sur trois saisons (question 2.5) ; mécanisme de consensus non précisé : une preuve de travail serait contraire à l'axe 3 du plan (empreinte environnementale) et à l'image d'un club engagé | 200 k€ de plus, sans compter l'adaptation de la billetterie et du contrôle d'accès, non chiffrée, pour une recette de quelques milliers d'euros |
| 5. Gouvernance et image | blockchain publique dont le club ne maîtrise pas les règles ; dépendance à TOKAVÉRA ; **une voix par jeton** : le plus riche pèse le plus, contraire à l'esprit de l'association (M. BORDAVIEILLE) ; jetons à prix libre : un effondrement ferait perdre de l'argent à des familles « sous les couleurs du club » ; priorité de billetterie qui passe devant les abonnés fidèles (Mme ESTRABOUL) ; 70 % des abonnés sans portefeuille, 1 € par mois de frais | dépendance à la même blockchain et à l'application de TOKAVÉRA pour revendre ; complexité pour les supporters au guichet |

**Volet 1** (0,5 pt) : la **valeur ajoutée** espérée est réelle sur le fond : engager des supporters plus jeunes, créer un lien nouveau (axe 2 du plan), une recette nouvelle. Mais **rien dans ce besoin n'exige une blockchain** : des votes, des tirages au sort et des avantages peuvent être offerts dans l'application du club, par un programme de fidélité tenu dans une base centralisée, gratuit ou lié à l'abonnement (60 % des répondants veulent donner leur avis « sans avoir à payer »). La blockchain apporte surtout des risques : spéculation et perte possible pour les supporters, ploutocratie des votes, données personnelles inaltérables, empreinte inconnue, image du club, dépendance.

**Volet 2** (0,5 pt) : la valeur ajoutée est **nulle ou presque** : la revente encadrée existe déjà dans la billetterie, et le contrôle d'accès par billet dématérialisé règle l'authenticité au stade ; le registre n'apporte rien sur la personne présente au contrôle (oracle), inscrit des données personnelles sur un registre public, impose une adaptation coûteuse des outils du stade, et ses recettes (5 € par revente) ne couvriraient pas ses coûts même dans l'hypothèse de TOKAVÉRA.

*2.4 c) – Ce que MiCA encadre et n'encadre pas ; recommandation*

**Ce que MiCA encadre dans ce projet** (annexe 2.4 ; 0,5 pt pour deux éléments encadrés et un non encadré) :
1. **L'offre au public des jetons fongibles** du volet 1 : ce sont des crypto-actifs au sens du règlement (représentation numérique d'un droit, transférable et stockée au moyen d'un registre distribué) ; leur offre au public suppose l'information des acheteurs par un **livre blanc** établi par une personne morale, sous réserve des exemptions prévues par le règlement, que le conseil du club appréciera. Le projet de contrat (article 8) laisse au club, « en sa qualité d'émetteur », toutes ces obligations : il doit le savoir avant de s'engager, et en faire vérifier la portée par son conseil, sans qu'il soit demandé ici de l'analyser.
2. **La conservation des jetons et leur échange contre des euros**, assurés par le partenaire de TOKAVÉRA : ce sont des services sur crypto-actifs réservés aux **PSCA agréés au titre de MiCA** ; la période transitoire des anciens PSAN ayant pris fin le 01/07/2026, nul ne peut exercer sans cet agrément depuis le 02/07/2026. L'affirmation « agréé depuis mars 2026 » doit être vérifiée auprès de l'autorité compétente avant tout engagement ; TOKAVÉRA, qui n'est pas PSCA, ne peut pas fournir elle-même ces services.

**Ce que MiCA n'encadre pas** : les **billets du volet 2**, jetons **uniques et non fongibles**, sont exclus de son champ s'ils sont réellement uniques ; leur revente relève des règles de la billetterie du club. MiCA ne fixe en outre ni traitement comptable ni régime fiscal pour ces jetons, et ne règle pas la question des données personnelles (RGPD). ISO 22739:2024 n'est qu'une norme de vocabulaire, qui ne garantit rien de la conformité du projet.

**Recommandation à Mme LAFERRADE** (0,5 pt) : **ne pas signer** avant la campagne d'abonnement de juillet. **Renoncer à l'option billets**, sans valeur ajoutée face à la bourse de revente existante et au contrôle d'accès, et coûteuse. Pour le volet 1, ne pas lancer de jetons spéculatifs sous les couleurs du club : répondre d'abord à l'axe 2 du plan par une **expérimentation centralisée** dans l'application du club (votes consultatifs gratuits ou réservés aux abonnés, une voix par supporter, avantages de fidélité), dont on mesurera l'adhésion pendant une saison. Le projet de jetons ne pourrait être réexaminé par le comité du numérique, puis par le conseil d'administration où siège l'association, qu'à cinq conditions : consensus économe en énergie, aucune donnée personnelle inscrite sur la blockchain, votes non pondérés par le nombre de jetons et aucune priorité de billetterie au détriment des abonnés, prestataire de conservation dont l'agrément est vérifié et avis juridique du club sur l'offre au public, contrat renégocié (question 2.5).

**Réponses tolérées**
- Volet 1 rattaché aux « jetons utilitaires » ou à la « tokenisation de droits d'accès », ou rapproché des programmes de fidélité sur blockchain, si le caractère fongible et l'échange sur des plateformes sont relevés ; volet 2 rattaché à la seule certification ou à la seule traçabilité.
- Grille d'opportunité formulée en six questions (volume et délai ajoutés), ou sous forme d'arbre de décision, si les critères « plusieurs acteurs sans tiers de confiance » et « alternative centralisée » y figurent.
- Recommandation d'un pilote de jetons limité (petit nombre de jetons, sans revente libre, sur une blockchain à preuve d'enjeu, sans donnée personnelle inscrite), si elle est conditionnée et cohérente avec les coûts de la question 2.5.
- Mention de l'existence d'exemptions de livre blanc ou de la notion de jeton utilitaire, sans analyse, avec renvoi au conseil juridique du club.
- Remarque selon laquelle l'activité de vente des jetons par TOKAVÉRA pourrait elle-même relever d'un service sur crypto-actifs, avec renvoi au conseil du club et sans analyse.

**Erreurs fréquentes**
- *Volet 1 présenté comme de la finance décentralisée* (typologie de F11 § 2.1) — « les jetons relèvent de la DeFi » ; juste : la finance décentralisée suppose un échange sans intermédiaire, alors que la conservation et l'échange passent ici par un PSCA agréé : il s'agit d'une tokenisation de droits d'accès.
- *Blockchain confondue avec une base de données distribuée* (`ET-08`) — « une blockchain est une base de données partagée sur plusieurs serveurs » ; juste : registre répliqué, consensus entre acteurs qui ne se font pas confiance, inaltérabilité.
- *Opportunités sans risques* (`ET-19` opportunités sans risques pour une technologie émergente) — « innovation, image moderne, 1,5 M€ » sans critique des hypothèses ni des risques pour les supporters ; juste : grille d'opportunité et alternative centralisée.
- *Oubli de l'énergie ou de l'oracle* (limite du programme ; F11 § 6) — énergie absente de l'analyse, ou « la blockchain garantit que le bon supporter entre au stade » ; juste : le registre garantit l'enregistrement, pas la réalité qu'il décrit.
- *MiCA présenté comme cadre comptable et fiscal, ou NFT soumis à MiCA* (`ET-35`) ; juste : offre au public, PSCA, jetons stables ; NFT uniques exclus ; ni traitement comptable ni régime fiscal.
- *Statut d'un prestataire non daté* (`ET-41` statut réglementaire affirmé sans date) — ancien PSAN présenté comme suffisant ; juste : agrément PSCA exigé depuis le 02/07/2026.
- *Analyse juridique du statut des jetons ou développement d'un contrat intelligent* — qualification détaillée, régime de responsabilité, algorithme ; juste : repères de l'annexe 2.4 et renvoi au conseil du club.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2023/1114 (MiCA) | offre au public de crypto-actifs, PSCA, exclusion des crypto-actifs uniques et non fongibles ; fin de la transition des anciens PSAN le 01/07/2026 | `mica` / F11 § 3 ; annexe 2.4 | applicable depuis le 30/12/2024 |
| Règlement (UE) 2016/679 (RGPD) | minimisation, conservation limitée, effacement | `rgpd` / F11 § 2.3 ; annexe 2.4 | applicable depuis le 25/05/2018 |
| ISO 22739:2024 | vocabulaire des chaînes de blocs et des registres distribués | `iso_22739_2024` / F11 § 3.4 ; annexe 2.4 | en vigueur |
| Fonctionnement, typologie, grille d'opportunité et limites d'une blockchain | consensus, clés, publique ou permissionnée, oracles, énergie | F11 § 1 et 2 | notion de cours |

---

### 2.5 – Coût du projet et projet de contrat (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ».
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.a` « Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques » ; `1.4.b` « Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) » ; `1.4.c` « Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD ». Limite : « L'analyse juridique approfondie relève du droit des contrats informatiques et est exclue du programme de l'UE. »

**Annexes mobilisées** : annexes 2.3 (coûts et recettes, sondage, avis, extrait du contrat), 2.1 (budget du SI) et 1.1 (abonnés).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Coût total de possession défini et estimé de tête : 500 k€ pour le volet 1 (300 de coûts directs, 200 de coûts cachés), 700 k€ avec l'option, hors commissions | 0,5 |
| a-2 | Comparaison aux recettes : hypothèse de TOKAVÉRA (1 600 k€ nets, retour sur investissement de 220 %) et ordre de grandeur tiré du sondage (environ 50 k€ auprès des abonnés la première saison ; projet non rentable) ; option non couverte dans tous les cas | 0,5 |
| b | Type de contrat caractérisé (abonnement à un service en ligne, SaaS, et forfait de mise en place) et trois clauses à négocier (niveau de service, propriété et restitution des données, réversibilité), justifiées et formulées ; 0,5 pour le type et une clause | 1 |

**Réponse attendue**

*2.5 a) – Coût total de possession et comparaison aux recettes*

Le **coût total de possession** est le coût complet d'une solution sur sa durée d'usage : acquisition et mise en place, abonnements et exploitation, support, formation et communication, conformité, sortie ; il inclut les **coûts cachés**, que la proposition du fournisseur ne montre pas, et ne s'actualise pas (sommes rondes sur trois saisons, en milliers d'euros, annexe 2.3).

| Poste (trois saisons) | Volet 1 | Option billets |
|---|---|---|
| Forfait de mise en place | 150 | 80 |
| Abonnements (3 × 50 ; 3 × 40) | 150 | 120 |
| **Coûts directs** | **300** | **200** |
| Support aux supporters à la billetterie (mi-temps, 3 × 30, Mme ARRIBEUX) | 90 | — |
| Campagne de communication (3 × 30, Mme SOUBIRAC) | 90 | — |
| Premier avis juridique sur la conformité (article 8 du contrat) | 20 | — |
| **Coûts cachés chiffrés** | **200** | non chiffrés (adaptation de la billetterie et du contrôle d'accès) |
| **Coût total sur trois saisons** | **500** | **200**, soit **700** avec le volet 1 |

S'y ajoutent la **commission de 20 %** sur les ventes de jetons, des coûts non chiffrés (adaptation des outils du stade, temps de l'équipe informatique de deux personnes, suivi réglementaire) et des coûts supportés par les supporters (1 € par mois de tenue de portefeuille). Le volet 1 représente environ 170 k€ par saison, près d'un cinquième du budget du SI (0,5 pt).

**Comparaison aux recettes** (0,5 pt) :
- **Selon TOKAVÉRA** : 1 500 + 250 + 250 = 2 000 k€ de ventes, moins 400 k€ de commission, soit **1 600 k€ nets** ; retour sur investissement = (1 600 − 500) / 500 = **220 %**. Mais l'hypothèse suppose **15 000 acheteurs** la première saison, plus de deux fois le nombre d'abonnés, dépensant 100 € chacun.
- **Selon le sondage** : 15 % des répondants se disent prêts à acheter, pour 50 € ; extrapolé aux 7 000 abonnés, cela fait environ 1 000 acheteurs (15 % × 7 000 = 1 050) et environ **50 k€** la première saison, trente fois moins que l'hypothèse de TOKAVÉRA ; le chiffre est même probablement surestimé, car les répondants au questionnaire sont les abonnés les plus engagés. Même en doublant ce montant pour les supporters non abonnés (100 k€) puis en retenant 50 k€ par saison, les ventes atteindraient 200 k€, soit 160 k€ nets de commission, pour 500 k€ de coûts : une **perte d'environ 340 k€**, retour sur investissement d'environ − 70 %. En outre, chaque jeton vendu engage le club à fournir des avantages pendant la durée du projet, et les reventes entre supporters ne lui rapportent rien.
- **Option billets** : 90 k€ de commissions sur trois saisons dans l'hypothèse de TOKAVÉRA (6 000 reventes par saison, quatre fois les 1 500 de la bourse actuelle) pour 200 k€ de coûts ; environ 7,5 k€ par saison au rythme actuel. Elle n'est rentable dans aucune hypothèse.

*2.5 b) – Type de contrat et clauses à négocier*

**Type de contrat** : un **abonnement à un service en ligne (SaaS)** pour la plateforme, l'application des supporters et le tableau de bord (article 1), assorti d'une prestation de **mise en place au forfait** (prix fixe de 150 k€, plus 80 k€ pour l'option) et d'une **rémunération variable** (commission de 20 % des ventes). Ce n'est ni une régie ni une infogérance : TOKAVÉRA fournit un service standard, ne s'engage qu'à ses « meilleurs efforts », sans niveau mesurable, et reste maîtresse de l'outil ; le club, qui assume seul les obligations réglementaires (article 8) et dont la sortie est verrouillée par la reconduction tacite (article 2), porte l'essentiel du risque.

**Trois clauses à négocier avant tout engagement** (0,5 pt pour le type et une clause ; 1 pt pour le type et trois clauses justifiées et formulées) :

| Clause | Pourquoi | Formulation de principe |
|---|---|---|
| **Niveau de service** (article 4) | « meilleurs efforts » et interruption « à tout moment » : aucune disponibilité garantie, alors que les ventes se concentrent sur l'ouverture des campagnes et les jours de match ; aucun recours en cas de panne | « TOKAVÉRA garantit une disponibilité de la plateforme d'au moins 99,5 % par mois, portée à 99,9 % les jours de match et d'ouverture des ventes, mesurée et communiquée chaque mois au club ; les maintenances sont planifiées, annoncées et exclues des jours de match ; tout manquement donne lieu à des pénalités sur l'abonnement, et la récurrence ouvre au club un droit de résiliation. » |
| **Propriété et protection des données** (article 5) | les données des supporters seraient la propriété de TOKAVÉRA, réutilisables pour ses offres et celles de ses partenaires : le club perdrait la maîtrise de son actif et la confiance de ses supporters ; le club reste responsable des traitements, TOKAVÉRA doit agir comme sous-traitant | « Les données des supporters appartiennent au club, responsable du traitement ; TOKAVÉRA les traite uniquement pour l'exécution du contrat, sur ses instructions écrites, sans réutilisation pour son compte ni pour des tiers ; aucune donnée personnelle n'est inscrite sur la blockchain ; le lieu d'hébergement, les mesures de sécurité et les sous-traitants ultérieurs sont précisés et soumis à l'accord du club. » |
| **Réversibilité** (article 6, avec la durée de l'article 2) | à la fin du contrat, le club perd l'accès à ses données, alors que les jetons et les engagements envers leurs détenteurs demeurent ; la reconduction tacite par trois saisons et le préavis de douze mois l'enferment | « En fin de contrat, quelle qu'en soit la cause, TOKAVÉRA restitue au club, dans un format ouvert et documenté et dans un délai convenu, l'ensemble des données des supporters et des transactions, puis les efface ; elle assiste le club pendant une période de transition pour assurer la continuité des avantages promis aux détenteurs de jetons ; le contrat est conclu pour une saison renouvelable expressément. » |

Les autres articles méritent attention sans analyse juridique : plafond de responsabilité limité à une saison d'abonnement (article 7), alors que les risques pour le club et ses supporters dépassent largement ce montant ; transfert au club de toutes les obligations réglementaires (article 8).

**Réponses tolérées**
- Coût total arrondi présenté avec la commission estimée (par exemple 500 k€ + 20 % des ventes), ou avec une provision pour l'adaptation des outils du stade, si l'hypothèse est écrite.
- Recettes du sondage estimées autrement (abonnés seuls, extrapolation aux 120 000 contacts écartée faute de base), si l'ordre de grandeur reste de quelques dizaines de milliers d'euros par saison et si la fragilité de l'hypothèse de TOKAVÉRA est relevée ; estimation limitée aux 150 répondants intéressés (environ 7,5 k€), si l'hypothèse est écrite : la conclusion est la même.
- Retour sur investissement exprimé en gain net (1 100 k€ selon TOKAVÉRA, perte d'environ 340 k€ selon le sondage) plutôt qu'en pourcentage.
- Contrat qualifié de « contrat de service en ligne », de « licence d'usage par abonnement » ou de « contrat mixte » (forfait et abonnement), si le caractère standard du service et l'absence d'engagement mesurable sont relevés.
- Troisième clause choisie parmi la durée et la reconduction tacite, la responsabilité ou les obligations réglementaires, si elle est justifiée par le cas et formulée, à condition que le niveau de service et les données figurent parmi les trois.

**Erreurs fréquentes**
- *TCO réduit au prix affiché* (`ET-33` TCO = prix d'achat) — 300 k€ sans le support, la communication ni la conformité ; juste : 500 k€ pour le volet 1, 700 k€ avec l'option.
- *Hypothèses du fournisseur reprises sans critique* (`JUR-D06` prudence d'interprétation) — « 1,5 M€ dès la première saison » ; juste : 15 000 acheteurs pour 7 000 abonnés, sondage à environ 50 k€.
- *Calcul actualisé ou précision inutile* — le coût total ne s'actualise pas ; sommes rondes de tête.
- *Régie, forfait et infogérance confondus* (`ET-31`) — « contrat d'infogérance de la billetterie » ; juste : abonnement SaaS et forfait de mise en place.
- *Données laissées au prestataire* (`JUR-A05` externalisation : contractualisation et conformité) — accepter que TOKAVÉRA soit propriétaire des données ; juste : données au club, sous-traitance encadrée, restitution.
- *Analyse juridique approfondie du contrat* — régime de la responsabilité, validité des clauses ; juste : principes et formulations de gestion.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Coût total de possession, coûts cachés, retour sur investissement en principe | postes, horizon de trois saisons, sans actualisation | F09 § 3 | notion de cours |
| Typologie des contrats, niveaux de service, clauses de données et de réversibilité | SaaS, forfait, SLA, pénalités, restitution | F04 § 1, 3 et 4 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | responsable du traitement et sous-traitant, minimisation | `rgpd` / F04 § 4 | applicable depuis le 25/05/2018 |

---

## DOSSIER 3 – MAÎTRISER LES RISQUES DES JOURS DE MATCH ET L'EMPREINTE DU STADE CONNECTÉ (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Risques des jours de match | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. | 3 |
| 3.2 Gouvernance et résilience des systèmes du stade | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 2,5 |
| 3.3 Diagnostic d'audit | `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ; `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance | 2,5 |
| 3.4 Empreinte du stade connecté et demande du partenaire | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.b` Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) ; `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI | 5 |
| **Dossier 3 – Maîtriser les risques des jours de match et l'empreinte du stade connecté** |  | **13** |

Répartition indicative : connaissances (typologie des risques, analyse d'impact sur l'activité, système critique, articulation avec le plan de continuité, audit et contrôle, Green IT et sobriété, outils de mesure, norme volontaire) 2,25 points environ (items 3.1 a pour moitié, b-1 pour moitié, 3.2 a-1 pour moitié, c-1 pour un quart, 3.3 b pour moitié, 3.4 a-1, a-3 pour moitié, c-2 pour un quart) ; analyse des annexes et recommandations 10,75 points, soit environ 83 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Risques des jours de match (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers » ; `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; la quantification des incidences sur les comptes relève de l'UE 4.

**Annexes mobilisées** : annexes 3.1 (déroulé, acteurs, réseaux), 3.2 (incidents A et B, repère RGPD) et 1.1 (chiffres clés) ; l'annexe 3.3 peut être utilisée en appui.

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cybermenaces et défaillances opérationnelles brièvement définies, deux risques précis par catégorie tirés des annexes | 0,5 |
| a-2 | Risques réglementaires et risques métiers brièvement définis, deux risques précis tirés des annexes | 0,5 |
| b-1 | Analyse d'impact sur l'activité définie ; impacts de l'incident A sur au moins trois processus du jour de match | 0,5 |
| b-2 | Continuité du service aux spectateurs (absence de mode dégradé, dépendance au prestataire) et postes des états financiers exposés, sans chiffrage au-delà des montants de l'annexe | 0,5 |
| c-1 | Trois risques prioritaires retenus et justifiés par leur probabilité et leur impact | 0,5 |
| c-2 | Pour chacun, une option de traitement, une mesure précise et un référentiel ou une méthode adaptés ; 0,5 dès deux risques complets | 0,5 |

**Réponse attendue**

*3.1 a) – Typologie et six risques d'un jour de match*

Les risques liés au SI se répartissent en trois catégories (F12 § 0) : les **cybermenaces** (actions malveillantes visant la confidentialité, l'intégrité ou la disponibilité de l'information), les **défaillances opérationnelles** (pannes, erreurs, dépendances, absence de procédure, sans intention de nuire) et les **risques réglementaires et métiers** (manquement à une obligation légale ou contractuelle ; atteinte aux activités, aux recettes et à l'image de l'organisation).

| Catégorie | Risques d'un jour de match (annexes 3.1 et 3.2) |
|---|---|
| Cybermenaces | (1) **fraude aux billets dématérialisés** : copie et revente de billets diffusés hors de tout contrôle (incident B : 400 billets copiés, 1 100 présentations, 550 acheteurs refoulés, annonce reprenant le logo du club) ; (2) **intrusion par une interconnexion** : depuis le réseau du public vers les terminaux de paiement de la tribune Est, par l'accès à distance permanent de PORTALVÈNE Accès (attaque par un prestataire) ou par le poste de supervision relié au réseau administratif et au réseau des systèmes du stade |
| Défaillances opérationnelles | (3) **panne du contrôle d'accès** à l'ouverture des portes, provoquée par une mise à jour non maîtrisée du prestataire (incident A : 35 minutes, 80 lecteurs arrêtés) ; (4) **absence de mode dégradé et dépendance au prestataire** : aucune consigne écrite, liste des billets sur le seul serveur local, astreinte fermée pendant les matchs ; variante : défaillance de l'écran géant ou de la sonorisation qui portent les consignes de sécurité, ou de la messagerie grand public qui relie les 400 intervenants |
| Risques réglementaires et métiers | (5) **réglementaire** : violation de données personnelles (noms et adresses électroniques de 400 invités accessibles en ligne) sans décision de notification, alors que le délai de 72 heures, qui courait depuis la découverte du 16 janvier 2027, est dépassé depuis près de cinq mois (repère de l'annexe 3.2) ; (6) **métier** : atteinte à la sécurité et à l'accueil du public (2 000 spectateurs entrés sans contrôle, nombre d'entrées par tribune inconnu), perte de recettes et de confiance des spectateurs et des partenaires (avoirs, 1 200 réclamations, 200 invités de loge en retard, renouvellement des partenariats) |

(0,5 pt pour les deux premières catégories, 0,5 pt pour la troisième.)

*3.1 b) – Analyse d'impact de l'incident A*

L'**analyse d'impact sur l'activité** (*business impact analysis*) recense les processus critiques, mesure les effets d'une interruption dans le temps (sécurité des personnes, recettes, image, obligations), identifie leurs dépendances (systèmes, données, prestataires, personnes) et en déduit la durée d'interruption tolérable, qui fonde les dispositifs de continuité (F12 § 4). Un jour de match, la tolérance se compte en minutes : les spectateurs arrivent en deux heures et le coup d'envoi est fixé (0,5 pt avec les processus).

Impacts sur les processus :
- **entrée du public** : arrêt total des 80 lecteurs pendant 35 minutes, files de 45 minutes, 3 000 spectateurs, près d'un sur cinq, entrés après le coup d'envoi ;
- **sécurité et comptage du public** : 2 000 entrées sans lecture, jauge par tribune inconnue pour ce match, décision prise oralement, sans règle préétablie ;
- **hospitalités et partenariats** : 200 invités de loge en retard, gestes attendus par les partenaires (11 M€ de partenariats et 4 M€ d'hospitalités en jeu à terme) ;
- **restauration** : ventes d'avant-match perdues ;
- **billetterie et relation avec les supporters** : 1 200 réclamations en trois semaines, 2 000 messages critiques ;
- **information de gestion** : passages non enregistrés, statistiques de fréquentation du match faussées.

Continuité et états financiers (0,5 pt) :
- **Continuité** : le service a été rétabli par chance (un ingénieur joint sur son téléphone personnel) ; il n'existait ni procédure dégradée, ni copie de la liste des billets hors du serveur, ni engagement de délai de rétablissement : le club dépend entièrement d'un prestataire indisponible aux heures des matchs.
- **États financiers**, postes exposés : chiffre d'affaires de la billetterie, diminué des avoirs (45 000 €), et dette envers les spectateurs tant que ces avoirs ne sont pas utilisés ; autres produits (redevance des buvettes, − 10 000 €) ; charges externes (heures supplémentaires des prestataires, 5 000 €) ; aucun recours chiffrable contre PORTALVÈNE Accès faute de pénalité au contrat ; risque de réclamations des partenaires sur leurs contrats. Les 60 000 € représentent 1 % des recettes annuelles de billetterie et d'abonnements (6 M€ en 2025-2026) et environ 0,2 % du chiffre d'affaires, mais l'impact d'image et la répétition du risque pèsent davantage ; l'évaluation des incidences sur les comptes relève de l'UE 4.

*3.1 c) – Trois risques prioritaires et leur traitement*

Échelle retenue (hypothèse à écrire) : probabilité faible, moyenne ou forte ; impact limité, important ou critique.

| Risque prioritaire | Probabilité et impact | Option de traitement | Mesure | Référentiel ou méthode |
|---|---|---|---|---|
| R3-R4 – Panne du contrôle d'accès sans mode dégradé | **forte** (déjà survenue ; mises à jour à distance sans prévenir ; astreinte fermée) × **critique** (16 000 spectateurs, sécurité, recettes, image) | **réduire** le risque et en **partager** une part avec le prestataire | avenant au contrat : gel des mises à jour dans les 48 heures qui précèdent un match, technicien présent ou astreinte joignable chaque jour de match, délai de rétablissement de 15 minutes assorti de pénalités ; procédure dégradée avec liste des billets exportée sur des lecteurs autonomes | analyse d'impact et continuité selon ISO 22301:2019 ; relations avec les fournisseurs parmi les mesures de l'annexe A d'ISO/IEC 27001:2022 |
| R1 – Fraude aux billets dématérialisés | **forte** (fichiers envoyés à chaque match ; incident déjà survenu) × **important** (700 refus, invités refoulés, image, données d'invités diffusées) | **réduire** | billets d'invitation nominatifs, délivrés dans l'espace en ligne de la billetterie plutôt qu'en fichier ; alerte en cas de double présentation ; consignes de diffusion données aux partenaires ; procédure de traitement des violations de données (décision de notification sous 72 heures) | EBIOS Risk Manager (version 1.5), dont les scénarios stratégiques intègrent l'écosystème (partenaires, prestataires) ; RGPD pour la notification |
| R2 – Intrusion par une interconnexion entre réseaux | **moyenne** (aucune attaque constatée, mais trois interconnexions non maîtrisées) × **critique** (systèmes de sécurité du stade, données de paiement, propagation au réseau administratif) | **réduire** ; **éviter** le raccordement des terminaux au réseau du public | séparation des trois réseaux (question 3.2 b) ; accès à distance des prestataires ouvert sur demande, nominatif et tracé ; comptes partagés remplacés par des comptes nominatifs | appréciation des risques selon ISO/IEC 27005:2022 ; mesures de l'annexe A d'ISO/IEC 27001:2022 |

(0,5 pt pour trois risques justifiés par la probabilité et l'impact ; 0,5 pt pour les traitements, dès deux complets.)

Le risque réglementaire R5 appelle une décision immédiate, indépendante de la cotation : examen de la violation avec le partenaire, décision de notifier ou non, consignée.

**Réponses tolérées**
- Autres risques pertinents : défaillance du réseau sans fil ou de la plateforme de paiement (buvettes à l'arrêt), hameçonnage des supporters par de faux sites de billetterie, consignes de sécurité diffusées à 120 anciens intervenants, comptes partagés du logiciel de contrôle d'accès (annexe 3.3).
- Classement d'un même fait dans deux catégories (la fuite de la liste est à la fois une cybermenace et un risque réglementaire), s'il est justifié.
- Cotation numérique (1 à 4) ou matrice de criticité, si l'échelle est annoncée.
- Option « transférer » par une cyberassurance pour le risque résiduel, présentée comme complément et non comme substitut aux mesures.
- Méthode MEHARI ou NIST CSF 2.0 citée à la place d'EBIOS RM ou d'ISO/IEC 27005, si elle est située (méthode d'analyse, cadre).

**Erreurs fréquentes**
- *Typologie récitée sans faits du cas* (`JUR-T01`, `ET-39`) — liste générique de menaces ; juste : chaque risque est formulé comme un événement du jour de match, chiffré par les annexes.
- *Impact réduit au coût de l'incident, ou dérive vers le traitement comptable* (périmètre 4.1, F10 § 0) — juste : processus, continuité, postes exposés, sans écriture ni provision.
- *Norme, méthode et solution confondues* (`ET-01`, `JUR-S06`) — « installer ISO 27001 », « acheter EBIOS » ; juste : ISO/IEC 27001:2022 est une norme d'exigences, EBIOS RM une méthode d'appréciation des risques, ISO/IEC 27005:2022 des lignes directrices.
- *Mesures techniques détaillées* (`JUR-T12`) — réglages des lecteurs ou des équipements de réseau ; juste : mesures organisationnelles et contractuelles, principes d'architecture.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI ; analyse d'impact sur l'activité | catégories de risques ; BIA | F12 § 0, 4 et 5 | notion de cours |
| ISO/IEC 27001:2022 ; ISO/IEC 27005:2022 | norme d'exigences et mesures de l'annexe A ; gestion des risques | `iso_27001_2022`, `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager (ANSSI, version 1.5) | méthode d'appréciation des risques, écosystème | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| ISO 22301:2019 | management de la continuité d'activité | `iso_22301_2019` ; F12 § 4 | en vigueur |
| RGPD | notification d'une violation dans les 72 heures | `rgpd` ; F12 § 5 | applicable depuis le 25/05/2018 |

---

### 3.2 – Gouvernance et résilience des systèmes du stade (2,5 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) » (ici le seul positionnement dans le plan de continuité ; IAM non traitée) ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique des solutions n'est pas exigée ; le lien avec les normes peut être fait sans entrer dans les certifications.

**Annexes mobilisées** : annexes 3.1 (acteurs, réseaux, interconnexions), 3.3 (constats) et 1.1 (organigramme).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Système critique défini et appliqué (systèmes du stade concernés) ; rôles et responsabilités des cinq acteurs | 0,5 |
| a-2 | Document et instance qui formalisent ces responsabilités, avec leur contenu et leur fréquence | 0,5 |
| b | Trois principes de séparation des réseaux, reliés aux constats, sans détail technique ; 0,5 dès trois principes reliés | 0,5 |
| c-1 | Procédure dégradée d'entrée du public (déclenchement, décideur, moyens, retour à la normale), située dans le plan de continuité et distinguée de la reprise | 0,5 |
| c-2 | Exercice de crise : scénario, participants, fréquence, retour d'expérience | 0,5 |

**Réponse attendue**

*3.2 a) – Système critique et responsabilités*

Un **système critique** est un système dont l'indisponibilité, l'altération ou la compromission met en cause la sécurité des personnes ou la poursuite d'une activité essentielle, et dont la gouvernance doit donc désigner sans ambiguïté qui décide, qui exploite et qui contrôle. Au stade, sont critiques le **contrôle d'accès** (entrée et comptage du public), la **sonorisation** et l'**écran géant** (consignes de sécurité), l'**éclairage** et, à un degré moindre, le **paiement des buvettes** (0,5 pt avec les rôles).

| Acteur | Responsabilités |
|---|---|
| Direction générale du club (Mme LAFERRADE) | responsable en dernier ressort : fixe le niveau de risque accepté, approuve la politique de sécurité des systèmes du stade et l'avenant à la convention, arbitre les moyens, préside le comité ; rend compte au conseil d'administration (priorité du plan « MONTALBRET 2030 ») |
| Responsable du stade et de la sécurité (M. DOUMERGAT) | propriétaire des processus du jour de match : exprime les besoins de continuité, pilote les prestataires, déclenche la procédure dégradée, dirige la cellule de crise le jour du match |
| Informatique du club (M. PEYRASTRE, sous l'autorité du responsable administratif et financier) | référent de la sécurité des systèmes : tient l'inventaire, valide toute interconnexion et tout accès d'un prestataire, revoit les comptes, suit les incidents ; à terme, appui d'un responsable de la sécurité à temps partagé, indépendant de l'exploitation |
| Communauté d'agglomération (M. CASTÉRADE) | propriétaire des infrastructures installées en 2026 (réseaux, écran géant, éclairage, bornes) : en assure la maintenance et la sécurité, informe le club de toute intervention, met un agent joignable à disposition chaque jour de match |
| Prestataires (PORTALVÈNE Accès, SOLDÉRIS Paiement, GARDALEINE Sécurité, prestataire d'accueil) | obligations contractuelles : délai de rétablissement et astreinte les jours de match, mises à jour soumises à l'accord du club, comptes nominatifs, notification des incidents, participation aux exercices ; tenue à jour des listes d'intervenants |

Formalisation (0,5 pt) : un **avenant à la convention de mise à disposition** et une **annexe sécurité** commune aux contrats des prestataires, appuyés sur une **politique de sécurité des systèmes du stade** (périmètre, rôles, règles d'accès et de mise à jour, gestion des incidents, continuité), approuvée par la direction générale ; un **comité de sécurité des systèmes du stade** (direction générale, responsable du stade, informatique, agglomération, prestataires selon l'ordre du jour), réuni avant chaque saison puis chaque trimestre, qui suit les incidents, les exercices et le plan d'action de l'audit ; une **cellule de crise** désignée pour chaque jour de match.

*3.2 b) – Trois principes de séparation des réseaux*

1. **Cloisonnement en trois zones de confiance** : le réseau du public, ouvert à des milliers de terminaux inconnus, ne donne accès à aucun système du club ni du stade ; les terminaux de paiement de la tribune Est sont rattachés au réseau des systèmes du stade (constat 5).
2. **Flux limités au nécessaire, autorisés et tracés** : seuls les échanges indispensables sont permis entre zones (transmission de la liste des billets vers le contrôle d'accès, par exemple), sur décision documentée de l'informatique et du propriétaire ; le poste de supervision n'est plus relié aux deux réseaux à la fois (constat 6) ; cette segmentation limite la propagation d'une attaque.
3. **Aucune confiance accordée par défaut** : chaque accès, notamment celui des prestataires à distance, est authentifié (authentification multifacteur), nominatif, limité dans le temps et tracé (constats 1 et 4) ; c'est le principe du cadre Zero Trust, qui est une démarche d'architecture et non un produit.

(0,5 pt pour trois principes reliés aux constats.)

*3.2 c) – Résilience des jours de match*

**Procédure dégradée d'entrée du public** (0,5 pt avec son positionnement) : déclenchement par le responsable du stade dès qu'une entrée ne fonctionne plus pendant plus de cinq minutes ; moyens prêts avant chaque match (liste des billets valides exportée à 17 h, à la fin de la transmission, sur des lecteurs portatifs autonomes, contrôle visuel encadré, ordre d'ouverture des entrées) ; rôle de chaque superviseur et de chaque agent ; message au public par la sonorisation, l'écran et l'application ; enregistrement a posteriori des passages ; fin de la procédure décidée par le responsable du stade. Elle relève du **plan de continuité d'activité**, qui maintient l'activité critique en mode dégradé pendant l'incident ; le rétablissement du logiciel par PORTALVÈNE Accès relève de la **reprise**, distincte. Ces deux dispositifs sont des éléments du plan de continuité, pas un plan complet.

**Exercice de crise** (0,5 pt) : scénario réaliste tiré des incidents (panne du contrôle d'accès à l'ouverture des portes d'un match complet, prestataire injoignable ; ou diffusion de faux billets la veille d'un match) ; participants : direction générale, responsable du stade et de la sécurité, informatique, billetterie, communication, agent de l'agglomération, PORTALVÈNE Accès, GARDALEINE Sécurité et prestataire d'accueil ; fréquence : un exercice complet avant le premier match à domicile de chaque saison (août 2027), puis un exercice partiel à mi-saison, par exemple lors d'un événement sans enjeu ; retour d'expérience écrit et mise à jour de la procédure et de la liste de la cellule de crise.

**Réponses tolérées**
- Instance unique « comité des jours de match » qui traite la sécurité des systèmes avec la sécurité du public, si les systèmes y ont une place explicite.
- Fonction de responsable de la sécurité externalisée ou mutualisée avec la communauté d'agglomération, si elle reste indépendante de l'exploitation.
- Principes formulés autrement (défense en profondeur, moindre privilège), s'ils restent au niveau des principes et sont reliés aux constats.
- Exercice sur table plutôt qu'en situation réelle, s'il associe les prestataires.

**Erreurs fréquentes**
- *PCA et PRA confondus* (`ET-02`, `JUR-S02`) — présenter la procédure dégradée comme la remise en service du logiciel ; juste : la procédure dégradée maintient l'entrée du public, la reprise rétablit le système.
- *Zero Trust présenté comme un produit* (`ET-04`, `JUR-S03`) — Zero Trust décrit comme un équipement que l'on achète ; juste : cadre d'architecture qui vérifie chaque accès.
- *Gouvernance réduite à l'informatique* (`JUR-T11`) — oublier l'agglomération propriétaire et les prestataires ; juste : responsabilités partagées et formalisées.
- *Détail technique* (`JUR-T12`) — réglages des équipements de réseau ; juste : principes de séparation et de contrôle des flux.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Rôles et gouvernance des systèmes critiques ; politique de sécurité | acteurs, comité, politique | F12 § 1 | notion de cours |
| Le modèle Zero Trust (avis de l'ANSSI) | cadre d'architecture | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| ISO 22301:2019 | continuité, exercices | `iso_22301_2019` ; F12 § 4 | en vigueur |

---

### 3.3 – Diagnostic d'audit (2,5 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse » ; `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ». Limite : l'exécution de tests techniques détaillés n'est pas attendue.

**Annexes mobilisées** : annexes 3.3 (périmètre, méthode, onze constats), 3.2 (incidents) et 3.1 (acteurs).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Forme : destinataire, objet, 20 lignes au maximum, structure visible, vocabulaire accessible | 0,5 |
| a-2 | Constats regroupés en trois ou quatre thèmes et hiérarchisés, chacun relié à son risque | 1 |
| a-3 | Recommandations priorisées, datées et confiées à un responsable | 0,5 |
| b | Audit distingué du contrôle (indépendance, référentiel, appréciation d'ensemble, recommandations) ; suites : plan d'action et suivi | 0,5 |

**Réponse attendue**

*3.3 a) – Note de synthèse*

Note modèle (18 lignes) :

<!-- note -->
**À l'attention de Mme LAFERRADE — Objet : audit des systèmes du jour de match, diagnostic et priorités (juin 2027)**

L'audit confirme que l'entrée du public dépend de systèmes que personne ne pilote.

1. Continuité non assurée (constats 2, 3, 4, 7) : ni procédure dégradée, ni exercice de crise, prestataire injoignable les soirs de match et libre de ses mises à jour. Risque : nouvelle panne d'un match complet.
2. Accès et réseaux mal cloisonnés (1, 5, 6, 9) : comptes partagés, paiement sur le réseau du public, poste relié à deux réseaux. Risque : intrusion jusqu'aux systèmes du stade.
3. Responsabilités floues (8, 11) : convention muette, aucun inventaire. Risque : aucune décision possible en cas d'incident.
4. Billets des partenaires non sécurisés (10). Risque : nouvelle fraude.

Priorités : avant le premier match de 2027-2028, avenant avec PORTALVÈNE Accès (gel des mises à jour, astreinte, délai), procédure dégradée testée en exercice, comptes nominatifs, terminaux retirés du réseau du public (M. DOUMERGAT, M. PEYRASTRE) ; d'ici décembre 2027, avenant à la convention et inventaire avec l'agglomération, billets nominatifs.

Je propose un comité trimestriel pour suivre ce plan.
<!-- /note -->

Éléments d'appréciation :
- **regroupement et hiérarchie** (1 pt) : la continuité vient en premier (incident déjà survenu, impact critique), puis l'exposition des systèmes, puis la gouvernance, qui conditionne la durée des mesures ; un classement différent est accepté s'il est justifié ; 0,5 pt si les constats sont repris un à un sans regroupement ni risque ;
- **recommandations** (0,5 pt) : réalistes pour une informatique de deux personnes, datées par rapport au premier match à domicile de septembre 2027, confiées à un responsable.

*3.3 b) – Audit et contrôle, suites de la mission*

Le **contrôle** vérifie, de façon ponctuelle et souvent par les acteurs eux-mêmes, qu'une opération respecte une règle (un agent vérifie un billet, le responsable compte les entrées). L'**audit** est un examen indépendant (cabinet extérieur au club et aux prestataires), méthodique (entretiens, revue des contrats, observation d'un match) et fondé sur un référentiel (ISO/IEC 27001:2022), qui apprécie la conception et l'efficacité de l'ensemble du dispositif et de sa gouvernance, puis conclut par des recommandations hiérarchisées (F10 § 1.1). Suites : **plan d'action** validé par la directrice générale (mesure, responsable, échéance, indicateur), **suivi** par le comité à chaque trimestre et compte rendu au conseil d'administration, **audit de suivi** après les premiers matchs de la saison 2027-2028 (0,5 pt).

**Réponses tolérées**
- Note en tirets ou avec un court tableau des priorités, dans la limite des 20 lignes.
- Trois thèmes au lieu de quatre (billets rattachés à la continuité ou aux accès), si tous les constats majeurs sont couverts.
- Recommandations datées par rapport au calendrier sportif (« avant le premier match à domicile ») plutôt qu'à une date.

**Erreurs fréquentes**
- *Note trop longue ou non hiérarchisée* (`JUR-S07`, `JUR-T07`) — reprise des onze constats dans l'ordre de l'annexe ; juste : thèmes, risques et priorités.
- *Paraphrase des constats sans risque* (`JUR-T03`) — juste : chaque thème est relié à la conséquence qu'il expose.
- *Audit du SI confondu avec l'audit des comptes* (`ET-34`) — juste : l'audit porte sur la sécurité, la continuité et la gouvernance des systèmes du jour de match.
- *Démarche complète de mission à la place de la note* (`JUR-T07`) — juste : la mission est faite, il s'agit d'en restituer le diagnostic.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI, diagnostic, note de synthèse | constat, risque, recommandation, priorité, suivi | F10 § 1.1 et 1.2 | notion de cours |
| ISO/IEC 27001:2022 | référentiel de l'audit | `iso_27001_2022` ; F12 § 2 | en vigueur |

---

### 3.4 – Empreinte du stade connecté et demande du partenaire (5 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.b` « Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) » ; `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI ». Limites : le champ de la CSRD est donné par l'énoncé, jamais déterminé ; aucun calcul d'empreinte ; la durabilité est intégrée à la gouvernance du SI.

**Annexes mobilisées** : annexes 3.4 (équipements, consommations, estimation des émissions, contenus, demande d'ÉNERVALDE, repères au 31/12/2026), 3.1 (acteurs) et 1.1 (chiffres clés).

**Barème indicatif (5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Green IT et sobriété numérique définis et distingués | 0,5 |
| a-2 | Analyse sous les trois angles (fabrication, usage, durée de vie), étayée par les chiffres de l'annexe 3.4, compensation du gain de l'éclairage par le numérique relevée | 0,5 |
| a-3 | Deux outils ou indicateurs de mesure adaptés au cas, chacun avec sa limite | 0,5 |
| b-1 | Quatre mesures sur quatre domaines distincts, chacune avec principe, effet attendu et porteur ; 1 pour trois, 0,5 pour deux | 1 |
| b-2 | Priorisation justifiée (poids de la fabrication, rapidité, coût, dépendance envers l'agglomération) | 0,5 |
| c-1 | Raison de la demande : ÉNERVALDE, dans le champ de la CSRD, rend compte de sa chaîne de valeur, dont le club fait partie ; enjeu du renouvellement | 0,5 |
| c-2 | Réponse du club : norme volontaire (modules, plafond de la chaîne de valeur), données disponibles et réponse commune aux partenaires ; rôle du SI (collecte, traçabilité, fiabilité) | 0,5 |
| d | Deux indicateurs complets (formule, source, fréquence, cible, axe) ; 0,5 par indicateur | 1 |

**Réponse attendue**

*3.4 a) – Analyse de l'empreinte*

Le **Green IT** vise à réduire l'empreinte environnementale du SI lui-même (fabrication, usage et fin de vie des équipements, centres de données, logiciels), notamment par l'efficacité ; la **sobriété numérique** interroge d'abord le besoin : renoncer à un équipement, à une fonction ou à un contenu, ou les dimensionner au juste usage, plutôt que seulement les rendre moins consommateurs (F14 § 3). L'IT for green, distinct, mobilise le numérique pour réduire l'empreinte de l'organisation, comme le pilotage de l'éclairage (0,5 pt).

Analyse (0,5 pt) :
- **Fabrication** : elle représente 75 % des 40 tonnes d'équivalent CO2 émises chaque année par les équipements numériques du stade, soit environ 30 tonnes : 200 écrans de loges au lieu de 60, deux écrans géants, 120 bornes, 80 lecteurs, 60 terminaux. Ce constat rejoint le repère de l'ADEME et de l'Arcep : l'empreinte du numérique tient d'abord à la fabrication des équipements ; selon le volet de 2022 de cette étude, les terminaux, dont ceux des 40 000 utilisateurs de l'application, en concentraient l'essentiel.
- **Usage** : la consommation totale baisse de 25 % (320 à 240 MWh) grâce à l'éclairage à diodes (− 60 %), mais celle des écrans, réseaux et systèmes est multipliée par six (20 à 120 MWh) et représente la moitié du total : le gain de l'éclairage masque la croissance du numérique, due à l'ajout d'équipements ; l'éclairage pilotable, plus efficace, ouvre en outre un usage nouveau, les spectacles lumineux (effet rebond). Les 120 bornes et les 200 écrans des loges restent allumés en permanence pour un stade utilisé 55 jours par an. Les contenus ajoutent un usage non mesuré : 40 To de vidéos dont 70 % ne sont plus regardées après un mois, lecture automatique en très haute définition, application de 180 Mo, page d'accueil notée F, diffusions en très haute définition pour 300 spectateurs.
- **Durée de vie** : 60 écrans jetés à cinq ans, lecteurs remplacés tous les trois ans, à chaque renouvellement du contrat, quelle que soit leur usure ; sans inventaire, le club ne connaît ni l'âge ni l'état de ses équipements.

Outils et indicateurs (0,5 pt, deux attendus) :
- **sous-comptage de l'électricité** par usage (MWh, relevés mensuels de l'agglomération) : mesure fiable de l'usage, mais ignore la fabrication, qui domine, et l'origine de l'électricité ;
- **bilan des émissions de gaz à effet de serre** du numérique par catégories d'émissions (GHG Protocol, méthode Bilan Carbone), qui intègre la fabrication : complet, mais fondé sur des estimations et des facteurs d'émission, avec une incertitude forte (l'estimation de l'annexe est celle d'un bureau d'études) ;
- **EcoIndex** de la page d'accueil du site et des écrans de l'application : indicateur simple et parlant pour le pôle marketing, mais relatif, limité à une page et qui n'est pas une analyse de cycle de vie ;
- **durée de vie moyenne des équipements** tirée d'un inventaire : directement liée à la fabrication, mais suppose un inventaire qui n'existe pas encore.

*3.4 b) – Quatre mesures priorisées*

| Priorité | Domaine | Principe | Effet attendu (annexe 3.4) | Porteur |
|---|---|---|---|---|
| 1 | Durée de vie des équipements | inventaire des équipements numériques du stade ; aucun remplacement d'un équipement en état de fonctionner ; écrans conservés au moins dix ans ; avenant avec PORTALVÈNE Accès pour renouveler les lecteurs selon leur état et non à chaque renouvellement du contrat, tous les trois ans ; réemploi ou reconditionnement, critères de durabilité et de réparabilité dans les achats | agit sur la fabrication, 75 % des émissions ; évite de nouveaux rebuts comme les 60 écrans de 2021 | responsable administratif et financier (achats, informatique) et responsable du stade, avec l'agglomération |
| 1 | Pilotage des écrans, de l'éclairage et du réseau sans fil | mise en veille programmée des 200 écrans des loges ; bornes et écrans allumés seulement pendant les 55 jours d'utilisation ; spectacles lumineux limités aux grands matchs ; programmation horaire de l'écran géant | réduit l'essentiel des 120 MWh d'usage du numérique, rapidement et sans investissement | responsable du stade et de la sécurité, avec l'agglomération propriétaire |
| 2 | Contenus et application | écoconception selon le RGESN : suppression de la lecture automatique, résolution adaptée à l'usage, application allégée, durée de conservation des vidéos et suppression des 70 % qui ne sont plus regardées, diffusions en direct en définition adaptée | réduit le stockage (40 To), les échanges de données et la sollicitation des téléphones des supporters ; amélioration de la note F | responsable du pôle marketing et numérique, avec l'agence de l'application |
| 3 | Mutualisation | avec la stratégie numérique responsable de l'agglomération (2025) : inventaire, sous-comptage et achats communs ; usage partagé des écrans et des bornes avec les autres événements ; une seule collecte des données environnementales du stade pour le club et pour l'agglomération | évite les doublons d'équipements et de collectes ; donne au club les données qu'il n'a pas | directrice générale et M. CASTÉRADE |

(1 pt pour quatre mesures complètes ; 0,5 pt pour la priorisation.)

Priorisation : la durée de vie vient en premier parce que la fabrication domine l'empreinte ; le pilotage est au même rang parce qu'il est immédiat et gratuit ; l'écoconception demande un travail avec l'agence et un changement de pratiques du pôle marketing ; la mutualisation dépend d'un accord avec l'agglomération, à négocier dans l'avenant à la convention (question 3.2).

*3.4 c) – La demande d'ÉNERVALDE*

**Pourquoi** (0,5 pt) : ÉNERVALDE entre dans le champ de la CSRD modifiée par la directive Omnibus I (donnée de l'annexe) ; son état de durabilité, établi selon les normes européennes (ESRS), couvre sa **chaîne de valeur** : ses achats, dont le partenariat de 900 000 € par saison, et les impacts liés à sa marque (écran géant, vidéos) entrent dans les informations qu'elle publie, notamment ses émissions indirectes. Le club doit donc lui fournir des données fiables ; à défaut, ÉNERVALDE recourra à des estimations défavorables, et la durabilité devient un critère du renouvellement de 2028.

**Ce que le club peut fournir** (0,5 pt) : le club n'entre pas dans le champ de la CSRD (donnée) et compte moins de 1 000 salariés : depuis les exercices ouverts au 01/01/2027, ÉNERVALDE ne peut exiger de lui que les informations de la liste prévue pour la chaîne de valeur par le règlement délégué (UE) 2026/1560, qui fixe aussi la **norme volontaire pour les PME** (VSME). Le club peut donc établir volontairement un rapport selon le **module de base** de cette norme, puis le cas échéant son module complet, et le remettre à **tous** ses partenaires au lieu de remplir un questionnaire par partenaire (inquiétude de M. BARRALOU) ; il y joint ses consommations d'énergie (sous-compteurs), l'estimation des émissions du bureau d'études avec ses hypothèses, et sa politique de numérique responsable (mesures de la question b). Le **système d'information** en est la condition : il identifie la source et le responsable de chaque donnée (agglomération pour l'électricité, inventaire pour les équipements, plateforme de vidéos pour le stockage), collecte les données de tiers, conserve la méthode et les hypothèses (traçabilité) et contrôle leur cohérence d'une saison à l'autre (fiabilité).

*3.4 d) – Deux indicateurs*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Consommation d'électricité des équipements numériques du stade | somme des relevés des sous-compteurs « écrans » et « réseaux et systèmes » sur la saison, en MWh | sous-compteurs de la communauté d'agglomération | relevé mensuel, cumul par saison | 80 MWh au plus en 2028-2029, contre 120 en 2026-2027, soit un tiers de moins | environnement |
| Durée de vie moyenne des équipements numériques du stade à leur retrait | somme des âges des équipements retirés du service / nombre d'équipements retirés, par famille (écrans, lecteurs, bornes, terminaux) | inventaire des équipements numériques du stade, tenu par l'informatique du club avec l'agglomération | annuelle | au moins dix ans pour les écrans, six ans pour les lecteurs ; aucun équipement en état de fonctionner jeté | environnement |

(0,5 pt par indicateur complet.)

**Réponses tolérées**
- Définition de la sobriété accompagnée de l'IT for green, ou distinction Green IT / IT for green, si la sobriété est définie.
- Autres outils : analyse de cycle de vie citée en principe, indicateur d'efficacité énergétique d'un centre de données si le candidat évoque l'hébergement des vidéos.
- Ordre de priorité différent (pilotage en premier, pour sa rapidité), s'il est justifié.
- Autres indicateurs complets : note EcoIndex de la page d'accueil (cible C au moins en 2028), volume de vidéos stockées, part des heures d'allumage des écrans hors événements, part des achats d'équipements comportant des critères de durabilité.
- « Effet rebond » employé au sens large pour la croissance du numérique, s'il est expliqué.
- Mention de la double matérialité pour expliquer la demande d'ÉNERVALDE (impacts de sa chaîne de valeur et risque de réputation), sans détail des normes thématiques.

**Erreurs fréquentes**
- *Sobriété confondue avec l'économie d'énergie* (`ET-12`) — juste : la sobriété questionne le besoin (bornes allumées toute l'année, vidéos jamais regardées).
- *Empreinte réduite à l'électricité* (`ET-38`) — se féliciter de la baisse de 25 % ; juste : la fabrication représente 75 % des émissions et la consommation du numérique a été multipliée par six.
- *Assujettissement discuté ou seuils périmés* (`ET-41`, `ET-17`) — calculer si le club ou ÉNERVALDE entre dans le champ ; juste : le champ est donné par l'annexe ; la CSRD est une obligation d'information sur la chaîne de valeur, pas un simple rapport.
- *Indicateurs génériques ou incomplets* (`ET-18`, `JUR-A02`) — « réduire l'empreinte » sans formule ni cible ; juste : formule, source, fréquence, cible et axe.
- *Calcul d'empreinte* (périmètre 4.3.e) — recalculer des émissions ; juste : lecture des données fournies.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Green IT, sobriété, IT for green ; indicateurs | définitions, mesures, indicateurs | F14 § 1, 3 et 4 | notion de cours |
| Directive (UE) 2022/2464 (CSRD), modifiée par la directive (UE) 2026/470 « Omnibus I » | champ donné, chaîne de valeur | `csrd`, `csrd_omnibus` ; fiche commune | en vigueur ; Omnibus I non transposée en France |
| ESRS révisées, règlement délégué (UE) 2026/1563 | normes de l'état de durabilité d'ÉNERVALDE | `esrs_2026` ; fiche commune | applicable aux exercices ouverts à compter du 01/01/2027 |
| Norme volontaire VSME, règlement délégué (UE) 2026/1560 | modules, plafond de la chaîne de valeur | `vsme` ; fiche commune ; `ue4/fiches/F12` § 4 | en vigueur |
| Loi REEN n° 2021-1485 | axes, stratégie des intercommunalités | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | écoconception des contenus et de l'application | `rgesn_2024` ; F14 § 2 | en vigueur |
| Étude ADEME-Arcep | poids de la fabrication et des terminaux | `etude_ademe_arcep_numerique` ; F14 § 1 | publiée |
| EcoIndex ; GHG Protocol ; méthode Bilan Carbone | outils de mesure | `ecoindex`, `ghg_protocol`, `methode_bilan_carbone` ; F14 § 4 | en vigueur |
