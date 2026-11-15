# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 19 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 architecture et urbanisation, F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle de données exécuté, indicateur, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

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
