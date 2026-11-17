# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 29 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 architecture, urbanisation et cloud, F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F10 audit et fiabilisation, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le dossier numérique du chantier et les échanges avec les partenaires | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) | 3 |
| 2.2 L'analyse des marges des chantiers | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 4,5 |
| 2.3 La fiabilité des données de gestion des chantiers | `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels | 2,5 |
| 2.4 La gouvernance stratégique des données et la base des logements | `2.3.a` Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques ; `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ; `2.3.f` Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques ; `2.3.d` Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique | 3 |
| **Dossier 2 – Organiser et exploiter les données des chantiers et des logements** |  | **13** |

Répartition indicative : connaissances (interopérabilité et ses plans, source unique et identifiant, chaîne de traitement des données, démarche décisionnelle, biais de lecture, typologie des contrôles, gouvernance des données, actif immatériel, souveraineté et réversibilité) environ 3 points (les items 2.1 b-1, 2.2 b-1 et 2.4 a-1, et la moitié des items 2.2 a-1, 2.3 b-1, 2.4 b-1 et 2.4 c-1) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le dossier numérique du chantier et les échanges avec les partenaires (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) ». L'approfondissement technique des échanges est exclu ; l'interopérabilité est traitée sur les plans technique et organisationnel.

**Annexes mobilisées** : annexes 1.1 (outils du système d'information, quarantaine d'entreprises partenaires, organigramme), 2.1 (tableau des étapes et des identifiants, contrôle de 100 dossiers, dossiers d'aides, échanges avec les partenaires et les négociants, projet et avis recueillis) et 2.4 (calendrier et formats de la facturation électronique).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Trois constats de l'annexe 2.1 et ce qu'ils coûtent : aides perdues et gestes commerciaux, temps de recherche, défauts des dossiers, achats non rattachés, confiance des clients | 0,5 |
| a-2 | Identifiant commun : numéro de projet attribué au premier contact (réponse à Mme FONTRIVAL) et numéro de chantier à la signature, uniques, non signifiants, stables, indépendants des versions du devis, portés par tous les outils et toutes les pièces | 0,5 |
| a-3 | Référentiel des clients et des logements, outil qui fait foi pour chaque catégorie de données, circulation sans ressaisie ; dossier numérique comme vue consolidée qui range les pièces par l'identifiant et en garde la version validée (réponse au conducteur de travaux et à la chargée des dossiers d'aides) | 0,5 |
| b-1 | Interopérabilité définie, avec ses plans technique (et syntaxique), sémantique et organisationnel | 0,5 |
| b-2 | Entreprises partenaires : dépôt des pièces dans le dossier numérique pour leur lot, formats ouverts, nommage par le numéro de chantier, factures électroniques structurées à compter du 01/09/2027 ; interface de programmation réservée aux trois partenaires équipés ; deux conditions organisationnelles | 0,5 |
| b-3 | Fournisseurs de matériaux : commandes passées depuis le logiciel de devis avec le numéro de chantier, interface de programmation avec les deux négociants qui la proposent, factures structurées déjà reçues rattachées automatiquement ; deux conditions organisationnelles | 0,5 |

**Réponse attendue**

*2.1 a) – Ce que coûte l'organisation actuelle et l'organisation cible des données*

**Trois constats et leur coût** (0,5 pt), parmi les suivants :
1. **Un même chantier sous des identifiants différents d'un outil à l'autre** (numéro de contact, numéro de visite, nom du fichier thermique, numéro de devis qui change à chaque version, nom du client dans le planning et le stockage, numéro de dossier de l'organisme) : aucun outil ne peut retrouver les données d'un autre ; retrouver les pièces d'un chantier, dans cinq outils, demande souvent plus d'une heure.
2. **Des dossiers incomplets ou incohérents** : 55 dossiers sur 100 présentent au moins un défaut (adresse écrite différemment dans 35, photos avant travaux introuvables dans 20, avenant non reporté dans 15, procès-verbal absent dans 12, calcul thermique décalé dans 10).
3. **Des aides perdues pour les clients** : 140 dossiers d'aides incomplets sur 700 (20 %) et 35 rejetés (5 %), soit environ 175 k€ d'aides perdues pour les clients et 70 k€ de gestes commerciaux consentis pour préserver la relation : une perte de marge et une atteinte à la **confiance des clients** que le plan « Cap 2029 » veut préserver.
4. **Des achats sans chantier** : une commande de matériaux sur deux ne porte pas le numéro de devis, et les factures des négociants, pourtant structurées, ne peuvent pas être rattachées à un chantier ; la marge de chaque chantier devient incalculable (lien avec l'annexe 2.2).

**L'identifiant commun** (0,5 pt) : deux niveaux, pour répondre à Mme FONTRIVAL sans créer de chantiers fictifs :
- un **numéro de projet** (ou de logement) attribué **au premier contact** par l'outil de gestion de la relation client, repris par la visite technique, le calcul thermique et le devis : il couvre les logements visités qui ne deviendront pas des chantiers ;
- un **numéro de chantier** attribué **à la signature** par le logiciel de devis et de facturation, rattaché au numéro de projet ; les versions du devis et les avenants sont numérotées **sous** ce numéro au lieu d'en changer.
Ces identifiants sont **uniques**, **non signifiants** (ni le nom du client ni la commune, qui s'écrivent de plusieurs façons et peuvent changer), **stables** et jamais réattribués. Ils sont **diffusés** partout : bons de commande, bons de livraison, planning, heures, photos, procès-verbal, factures des partenaires et des négociants, dossier d'aides (le numéro de l'organisme est conservé comme simple référence rattachée).

**Le référentiel, l'outil qui fait foi et la circulation** (0,5 pt) : chaque donnée a **une source maîtresse** où elle est saisie une seule fois, puis circule vers les outils qui l'utilisent, de préférence automatiquement, sans ressaisie :

| Catégorie de données | Outil qui fait foi | Outils alimentés |
|---|---|---|
| Client, adresse normalisée du logement, numéro de projet | gestion de la relation client (référentiel des clients et des logements) | visite, calcul thermique, devis, planning, dossier d'aides |
| Caractéristiques du logement, consommations déclarées, photos avant travaux | application de visite technique | calcul thermique, devis, dossier numérique |
| Résultat du calcul thermique (version liée au devis signé) | logiciel de calcul thermique | dossier numérique, dossier d'aides |
| Devis signé, avenants, lots, numéro de chantier, situations, factures | logiciel de devis et de facturation | planning, commandes, comptabilité, analyse des marges, dossier d'aides |
| Heures, photos de chantier, procès-verbal de réception | saisie sur la tablette de chantier, sous le numéro de chantier | paie, analyse des marges, dossier numérique |

Le **dossier numérique du chantier** n'est pas un dossier de fichiers de plus : c'est une **vue consolidée** des données et des pièces du chantier, retrouvées par l'identifiant. Il peut s'appuyer sur le module de suivi de chantier du logiciel de devis (environ 4 k€ par an), puisque ce logiciel attribue le numéro de chantier et dispose d'une interface de programmation. Il **classe automatiquement** les pièces prises sur la tablette sous le numéro de chantier (réponse au conducteur de travaux, qui ne classera rien à la main) et ne retient comme pièce de référence que la **version validée** (devis signé et avenants signés, calcul thermique correspondant, procès-verbal signé), les versions antérieures restant consultables (réponse à la chargée des dossiers d'aides). Une liste des pièces obligatoires par type de chantier signale à chaque étape celles qui manquent, avant la réception et avant le dépôt du dossier d'aides.

*2.1 b) – L'interopérabilité avec les entreprises partenaires et les fournisseurs*

L'**interopérabilité** est la capacité de systèmes hétérogènes, appartenant le cas échéant à des organisations différentes, à échanger des données et à les utiliser sans intervention manuelle (0,5 pt). Elle se joue sur plusieurs plans : **technique** (moyens d'échange : interface de programmation, plateforme), **syntaxique** (formats : PDF, fichier tableur, XML, formats structurés de facture), **sémantique** (même sens des données : numéro de chantier, adresse, désignation des articles) et **organisationnel** (qui transmet quoi, quand, sous quelle responsabilité) (F07 § 7). Le programme exige les plans technique et organisationnel : un format ouvert ne sert à rien si personne ne s'engage à l'utiliser. Les **formats ouverts** sont des formats dont la spécification est publique et que tout logiciel peut lire, ce qui évite la dépendance à un éditeur ; une **interface de programmation (API)** permet à un logiciel d'interroger ou d'alimenter un autre logiciel de manière automatisée.

**Avec les entreprises partenaires** (0,5 pt) : quarante PME et micro-entreprises, dont trois seulement ont un logiciel capable d'échanger des données ; une interface de programmation généralisée serait irréaliste.
- **Solution** : un **espace de dépôt** dans le dossier numérique, limité au lot de chaque partenaire, où il dépose ses pièces (planning, photos, attestation d'autocontrôle) dans des **formats ouverts** (PDF, photos datées), sous un nommage fondé sur le numéro de chantier : il n'a rien à ressaisir, ce qui répond au gérant de l'entreprise de chauffage. Ses **factures** suivent le calendrier de l'annexe 2.4 : à compter du 01/09/2027, les PME et micro-entreprises doivent les émettre sous forme électronique, par une plateforme agréée, dans l'un des formats Factur-X, UBL ou CII ; SOLVÉRANCE Habitat demande que le numéro de chantier y figure comme référence de la commande, ce qui permettra de les rattacher automatiquement. L'interface de programmation est réservée aux trois partenaires équipés, si le volume le justifie.
- **Deux conditions organisationnelles**, parmi : une **charte d'échange** (ou contrat d'interface) signée avec chaque partenaire, qui fixe les pièces attendues, leurs formats, leurs délais (par exemple photos et attestation dans les 48 heures, facture dans les quinze jours suivant la fin des travaux) et la mention obligatoire du numéro de chantier ; un **interlocuteur** désigné de part et d'autre (assistante d'exploitation, conducteur de travaux) et un accompagnement des partenaires qui n'ont qu'un tableur ; l'intégration de ces exigences dans la sélection et le suivi des partenaires (délai de paiement conditionné à la complétude du dossier) ; un calendrier aligné sur septembre 2027.

**Avec les fournisseurs de matériaux** (0,5 pt) : trois négociants, entreprises de taille intermédiaire, assurent 70 % des achats ; deux proposent une interface de programmation et tous émettent déjà des factures électroniques structurées (obligatoire pour eux depuis le 01/09/2026, annexe 2.4).
- **Solution** : passer les commandes **depuis le logiciel de devis**, à partir des quantités du devis signé, avec le numéro de chantier ; avec les deux négociants équipés, relier ce logiciel à leur interface de programmation pour transmettre la commande et recevoir la confirmation, l'avis de livraison et la facture ; avec le troisième, utiliser son site ou un fichier de commande dans un format ouvert, toujours avec le numéro de chantier. La facture structurée, qui porte alors ce numéro, est **rattachée automatiquement** au chantier et rapprochée de la commande et de la livraison (question 2.3).
- **Deux conditions organisationnelles**, parmi : **aucune commande sans numéro de chantier**, y compris au comptoir (les achats de dépannage sont imputés sur place au chantier, ou au stock du dépôt puis sortis par chantier) ; un **référentiel des articles** partagé avec les négociants (correspondance entre leurs références et les ouvrages de la bibliothèque de prix) ; une **responsable** des achats parmi les assistantes d'exploitation ; un accord avec chaque négociant sur les données échangées et le traitement des anomalies.

**Réponses tolérées**
- Un seul identifiant attribué dès le premier contact, s'il reste stable de la demande à la facture et si les logements sans chantier sont distingués par un statut.
- Dossier numérique tenu dans l'espace de stockage partagé, si l'identifiant commun, le classement automatique et la version de référence sont prévus ; ou dans un outil distinct, si son alimentation par les outils sources est décrite.
- Plateforme d'échange ou bus d'intégration cité, si le principe (source maîtresse, fin des ressaisies) reste au premier plan ; échanges de données informatisés (EDI) proposés avec les négociants à la place d'une interface de programmation.
- Plans de l'interopérabilité présentés en trois niveaux (le niveau syntaxique rattaché au plan technique).
- Mention de la facturation électronique de SOLVÉRANCE Habitat elle-même, si elle reste exacte (ventes aux particuliers hors du champ des factures entre entreprises).

**Erreurs fréquentes**
- *Interopérabilité seulement technique* (`ET-36`) — interface de programmation proposée aux quarante partenaires sans charte, ni délais, ni numéro de chantier obligatoire ; juste : technique, sémantique et organisationnelle ensemble.
- *Dossier numérique réduit à un répertoire de fichiers* (`JUR-T03`) — « créer un dossier partagé par chantier » sans identifiant commun ni source maîtresse : on ajoute un sixième endroit où chercher ; juste : une vue consolidée alimentée par les outils sources.
- *Identifiant signifiant* — numéro construit avec le nom du client ou la commune, ou numéro de devis qui change à chaque version ; juste : identifiant non signifiant et stable, versions numérotées sous lui.
- *Modèle des données ou détail technique hors attente* (`JUR-T06`, `JUR-T12`) — entités et cardinalités, description des formats balise par balise ou du fonctionnement des interfaces, que la question exclut.
- *Morceau de cours* (`JUR-T01`) — définition de l'interopérabilité sans application aux partenaires et aux négociants.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Généralisation de la facturation électronique (article 91 de la loi de finances pour 2024) : réception obligatoire depuis le 01/09/2026, émission par les PME et micro-entreprises à compter du 01/09/2027 ; formats Factur-X, UBL, CII | calendrier et formats, d'après les repères de l'annexe 2.4 | `facturation_electronique_fr` / F10 § 3.4 | en vigueur ; émission des PME au 01/09/2027 |
| Plateformes agréées de facturation électronique | réception des factures structurées des négociants | `facturation_electronique_pa` / F10 § 3.4 | en vigueur |
| Interopérabilité (plans technique, syntaxique, sémantique, organisationnel), formats ouverts, interfaces de programmation ; données de référence et identifiants | définitions et principes | F07 § 1 et 7 ; F03 § 3 | notion de cours |

---

### 2.2 – L'analyse des marges des chantiers (4,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.d` « Outils décisionnels : Excel avancé, Power BI, Tableau, etc. » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Aucune manipulation d'outil ni aucun calcul statistique ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexes 1.1 (plan « Cap 2029 », comité stratégique, organigramme), 2.1 (identifiants, commandes sans numéro) et 2.2 (tableaux 1 à 4, données et défauts, outil actuel et deux possibilités, demande de M. VORGNAC).

**Barème indicatif (4,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Collecte et nettoyage : sources (devis et facturation, comptabilité, heures, planning), traitement des données manquantes ou non rattachées, journal des rejets, chacun relié à un défaut de l'annexe 2.2 (B et C) | 0,5 |
| a-2 | Structuration, analyse et restitution : rapprochement par le numéro de chantier, règles de calcul documentées, analyse par chantier et par axe, restitution par profil et mise en action, chacune reliée à un défaut | 0,5 |
| b-1 | Démarche décisionnelle et non simple outil ; choix argumenté par trois critères tirés de l'annexe 2.2 C et du plan « Cap 2029 » | 0,5 |
| b-2 | Coût de tête de l'outil en ligne (25 + 3 × 6 = 43 k€ sur trois ans) rapproché d'un point de marge (250 k€ par an) ; conditions préalables (numéro de chantier commun, fiabilité des données) | 0,5 |
| c-1 | Premier constat argumenté, avec sa précaution de lecture et sa conséquence pour le plan | 0,5 |
| c-2 | Deuxième constat argumenté, avec sa précaution de lecture et sa conséquence pour le plan | 0,5 |
| c-3 | Troisième constat argumenté, avec sa précaution de lecture et sa conséquence pour le plan | 0,5 |
| d-1 | Représentation pour le comité stratégique : message, graphique, piège, indicateur complet | 0,5 |
| d-2 | Représentation pour les conducteurs de travaux : message, graphique, piège, indicateur complet | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de traitement des données de l'analyse mensuelle des marges*

La chaîne de traitement des données (chaîne de valeur de l'informatique décisionnelle) conduit des données brutes des logiciels de gestion à une information qui éclaire la décision : collecte, nettoyage, structuration, analyse, restitution (F08 § 1). Appliquée aux marges des chantiers (0,5 pt par groupe d'étapes, chaque étape reliée à un défaut de l'annexe 2.2 (B et C)) :

| Étape | Ce qu'elle traite chez SOLVÉRANCE Habitat | Défaut corrigé |
|---|---|---|
| Collecte | extraction automatique, chaque nuit ou à date fixe, des devis signés et avenants, des factures et situations (logiciel de devis et de facturation), des achats et factures des partenaires et des négociants (comptabilité), des heures par chantier (paie ou saisie sur tablette), du planning et de l'avancement | quatre extractions manuelles, trois jours par mois, rapprochées par le nom du client |
| Nettoyage | contrôle des données manquantes, invalides ou en double : heures « dépôt et divers », achats sans chantier, factures de partenaires attendues mais non reçues (signalées et estimées à partir de la commande), avenants non enregistrés ; **journal des rejets** renvoyé aux responsables pour correction **à la source** | 15 % des heures et 20 % des achats sans chantier ; 300 k€ de factures non reçues ; avenants absents |
| Structuration | rapprochement de toutes les données par le **numéro de chantier** (question 2.1), à partir du référentiel des chantiers (type de travaux, secteur, conducteur, réalisation par les équipes ou avec des partenaires) ; règles de calcul **documentées** dans un dictionnaire des indicateurs (marge prévue, marge constatée, coût horaire standard, règle explicite pour les achats non rattachés en attendant leur disparition) ; historisation des mois | rapprochement par le nom du client ; répartition des achats au prorata du chiffre d'affaires ; trois versions de l'analyse de juin |
| Analyse | analyse descriptive de la marge prévue et constatée par chantier, puis par type de travaux, secteur, réalisation, conducteur et période ; repérage des chantiers qui s'écartent de la prévision et recherche de leurs causes (analyse exploratoire) ; distinction des chantiers achevés et en cours | analyse limitée au total par type de travaux ; aucune lecture par chantier |
| Restitution et décision | tableaux de bord par profil : comité stratégique (trimestriel), direction et conducteurs de travaux (hebdomadaire ou mensuel, pour leurs chantiers) ; commentaire, plan d'action et suivi | analyse disponible le 20 du mois suivant ; conducteurs non destinataires ; demande de M. VORGNAC |

*2.2 b) – Le choix de l'outil décisionnel*

L'informatique décisionnelle est une **démarche** et non un outil (0,5 pt avec le choix) : l'outil n'est que la couche de restitution d'une chaîne qui suppose des données fiables et rapprochables, des définitions partagées (qu'est-ce qu'une marge constatée ?), des responsables, des compétences et une culture de la donnée chez les utilisateurs (F08 § 1 ; rapport du jury 2025). L'intégrateur le dit lui-même : « l'outil ne corrigera pas vos données ». Sans numéro de chantier commun, ni l'une ni l'autre possibilité ne fonctionne.

**Choix argumenté** : l'**outil décisionnel en ligne** (possibilité 2), au regard de trois critères, parmi :
1. **Les destinataires** : le comité stratégique, la direction et dix conducteurs de travaux, bientôt les équipes de deux agences ; le tableur reste sur le poste d'une personne et circule en PDF, alors que l'outil en ligne offre des droits par profil et une consultation sur tablette.
2. **La fraîcheur et la fiabilité** : préparation automatique chaque nuit, une seule version des chiffres, règles de calcul centralisées, contre une consolidation qui dépend encore d'une personne et d'imports manuels, avec le risque de versions concurrentes.
3. **L'adaptation au plan « Cap 2029 »** : un volume de chantiers qui doit doubler, des axes d'analyse plus nombreux (agences, secteurs) et la demande trimestrielle du fonds ; le tableur atteindrait vite ses limites (volumétrie, traçabilité, dépendance à la comptable).
4. **Le coût et les compétences** : le tableur est moins cher et plus rapide à mettre en place, mais ne libère qu'environ deux jours de travail par mois ; l'outil en ligne exige un intégrateur et une montée en compétence des utilisateurs.

**Coût et enjeu** (0,5 pt) : de tête, 25 + 3 × 6 = **43 k€ sur trois ans**, soit environ 14 k€ par an, à rapprocher d'**un point de marge**, qui représente 1 % de 25 000 k€, soit **250 k€ par an** (et le double si le chiffre d'affaires double) ; l'écart de 2026 entre marge prévue et constatée est de 1 100 k€. Le coût est donc faible au regard de l'enjeu, **à condition** que les prérequis soient tenus : numéro de chantier commun à tous les logiciels (question 2.1) et données fiabilisées à la source (question 2.3). Un passage par le tableur structuré pendant quelques mois, le temps de fiabiliser les données, est acceptable s'il prépare l'outil en ligne.

*2.2 c) – Trois constats argumentés sur les marges de 2026*

Trois constats parmi les suivants (0,5 pt chacun, constat, précaution et conséquence compris) :

1. **L'écart se concentre sur les rénovations globales** : marge constatée de 22 % contre 32 % prévus (10 points d'écart), contre 26 % pour 28 % prévus sur les travaux par lots (2 points) ; les rénovations globales, 30 % du chiffre d'affaires, portent 750 k€ des 1 100 k€ d'écart, soit environ 70 % ; 40 % d'entre elles (50 sur 125) sont en dépassement de plus de 5 points. *Précaution* : la moyenne masque une forte dispersion (dix chantiers expliquent environ 300 k€, soit 40 % de l'écart des rénovations globales) ; les coûts de chaque chantier sont imparfaitement mesurés (heures non imputées, achats répartis au prorata du chiffre d'affaires) ; il faut analyser chantier par chantier avant de généraliser. *Conséquence* : le plan veut développer les rénovations globales ; si leur marge n'est pas maîtrisée, la croissance détruira de la valeur : revoir leur chiffrage avec le bureau d'études et analyser les dix chantiers les plus en écart.
2. **La marge s'érode à mesure que l'activité croît** : 27 % au premier trimestre, 23 % au quatrième, alors que le chiffre d'affaires trimestriel passe de 5 500 à 7 000 k€. *Précaution* : **corrélation n'est pas causalité** : la baisse coïncide avec le recrutement de quinze compagnons au second semestre, peut-être avec une part plus forte de rénovations globales ou une saisonnalité ; quatre trimestres ne font pas une tendance ; et le quatrième trimestre est sans doute **surestimé**, puisque 300 k€ de factures de partenaires n'étaient pas reçues au 31 janvier : la baisse réelle est peut-être plus forte. *Conséquence* : doubler le chiffre d'affaires et ouvrir deux agences avec de nouvelles équipes risque d'amplifier l'érosion : mesurer la marge par équipe et par ancienneté et prévoir l'encadrement des nouveaux compagnons avant les ouvertures.
3. **Le nord de l'Isère a la marge la plus faible** : 21 % contre 24 à 26 % ailleurs. *Précaution* : **effet de structure** : la moitié de son chiffre d'affaires vient des rénovations globales, contre 24 à 30 % ailleurs, et ce type de travaux a la marge la plus faible ; l'effectif est réduit (100 chantiers, dont 25 rénovations globales) ; l'éloignement du dépôt n'explique donc au mieux qu'une partie de l'écart, et reste une hypothèse à vérifier (temps de trajet, approvisionnement). *Conséquence* : les agences de Grenoble et de Saint-Étienne seront elles aussi éloignées de Vénissieux : il faut mesurer la marge par secteur et par type de travaux pour calibrer leurs devis et leur approvisionnement.
4. **Les chantiers réalisés par les seules équipes perdent plus de marge que ceux confiés en partie à des partenaires** : 23 % contre 28 % prévus (5 points), contre 26 % pour 30 % (4 points). *Précaution* : comparaison fragile : 300 k€ de factures de partenaires manquent, soit environ 2 points sur 14 000 k€ de chiffre d'affaires, et la marge des chantiers confiés en partie aux partenaires serait plutôt de 24 % ; les heures non imputées et la répartition des achats faussent aussi la comparaison ; les deux groupes n'ont pas la même composition (toutes les rénovations globales sont dans le second). *Conséquence* : aucune décision de confier davantage de travaux aux partenaires ne peut être fondée sur ce tableau.

*2.2 d) – Deux représentations visuelles*

| Destinataire | Message | Graphique | Piège de lecture à éviter | Indicateur représenté |
|---|---|---|---|---|
| Comité stratégique (0,5 pt) | où et quand la marge se perd, et si elle se redresse | barres groupées « marge prévue / marge constatée » par type de travaux et par secteur, triées, avec le chiffre d'affaires de chaque barre ; courbe trimestrielle de l'écart de marge, avec une ligne de cible | **axe tronqué** qui amplifie les écarts ; moyennes sans le volume ni la part des rénovations globales (**effet de structure**) ; conclusion tirée d'un seul trimestre | écart de marge des chantiers achevés (fiche ci-dessous) |
| Conducteurs de travaux (0,5 pt) | quel chantier dérive cette semaine, pour agir avant la fin des travaux | liste de leurs chantiers en cours avec, pour chacun, une barre de progression (puce) qui compare la part des heures prévues déjà consommées à l'avancement contrôlé, en couleur selon le seuil d'alerte | lecture fondée sur un **avancement déclaré** non contrôlé ; comparaison entre conducteurs sans tenir compte du type de chantier ; trop d'indicateurs sur un petit écran | taux de consommation des heures prévues (fiche ci-dessous) |

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Écart de marge des chantiers achevés | (marge constatée − marge prévue au devis) / chiffre d'affaires facturé des chantiers achevés, en points | outil décisionnel alimenté par le logiciel de devis et de facturation, la comptabilité et les heures par chantier | mensuelle ; présentée chaque trimestre au comité stratégique | écart d'au plus 2 points en 2027 (4 points en 2026), puis d'au plus 1 point | financier |
| Taux de consommation des heures prévues | heures imputées au chantier / heures prévues au devis, comparé à l'avancement contrôlé | heures saisies sur la tablette de chantier ; devis signé ; avancement validé | hebdomadaire | taux au plus égal à l'avancement contrôlé plus 5 points ; alerte au-delà de 10 points | processus |

**Réponses tolérées**
- Candidat qui relève, de tête, que l'écart des seules rénovations globales (750 k€) dépasse celui de tout le groupe des chantiers confiés en partie à des partenaires (environ 550 k€, soit 4 220 − 3 670) : les lots confiés en partie aux partenaires semblent dépasser leur marge prévue, ce qui renvoie aux factures non reçues et à la répartition des achats.
- Constats différents s'ils sont tirés des tableaux, argumentés et assortis d'une précaution fondée (par exemple sur les avenants non enregistrés, qui faussent la marge prévue).
- Choix du tableur avancé structuré, s'il est justifié par l'urgence et le coût, présenté comme une étape et assorti des limites (diffusion, dépendance à une personne, versions).
- Chaîne présentée selon les termes extraction, transformation et chargement, ou avec un entrepôt de données, si les défauts de l'annexe 2.2 (B et C) sont traités ; une table de faits n'est pas attendue.
- Autres graphiques adaptés (jauge, carte des secteurs en taux, histogramme de la distribution des écarts par chantier), si le message et le piège sont précisés ; autres cibles si elles sont justifiées.

**Erreurs fréquentes**
- *Démarche décisionnelle réduite à un outil* (`ET-05`, `JUR-D02`) — « l'outil en ligne résoudra le problème » ; juste : sans numéro de chantier commun et sans données fiables, l'outil affichera plus vite des chiffres faux.
- *Chaîne de traitement incomplète* (`JUR-D01`) — collecte et restitution seules, sans nettoyage ni règles de rapprochement ; juste : les cinq étapes, chacune reliée à un défaut.
- *Corrélation prise pour une causalité* (`ET-26`, `JUR-D06`) — « la croissance fait baisser la marge », « l'éloignement explique la marge du nord de l'Isère » ; juste : facteurs communs, effet de structure, petit effectif, données incomplètes du quatrième trimestre.
- *Indicateurs génériques ou incomplets* (`ET-18`) — « taux de marge » sans source, cible ni axe, ou indicateur que les conducteurs ne peuvent pas actionner.
- *Calculs inutiles* (`JUR-T07`) — recalcul de moyennes pondérées ou de tous les taux, que la question exclut.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement des données, démarche décisionnelle, outils (en principe), choix du graphique, biais de lecture, effet de structure, corrélation et causalité, fiche d'indicateur à cinq champs | définitions et méthode | F08 § 1, 3, 5 et 6 | notion de cours |

---

### 2.3 – La fiabilité des données de gestion des chantiers (2,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels ». Aucune règle comptable de l'avancement ni des contrats à long terme ; aucun chiffrage de l'incidence sur les comptes.

**Annexes mobilisées** : annexes 1.1 (organigramme : directrice des opérations, conducteurs de travaux, assistantes d'exploitation, comptabilité, responsable informatique), 2.1 (feuilles d'heures papier, commandes sans numéro, avenants non reportés) et 2.2 B (heures, achats, factures des partenaires, avancement et situations, comptes de l'exercice 2026).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Heures et achats : des coûts mal mesurés et mal répartis faussent la marge de chaque chantier, les comparaisons et le chiffrage des devis futurs, sans changer le total | 0,5 |
| a-2 | Avancement, situations et factures des partenaires : risque de chiffre d'affaires et de marge de 2026 surestimés, charges incomplètes ; comptes présentés au comité et au fonds, piste d'audit | 0,5 |
| b-1 | Contrôle à la saisie et contrôle de rattachement, avec risque couvert, nature et responsable | 0,5 |
| b-2 | Rapprochement (avancement, heures et achats ; commande, livraison et facture ; factures attendues), avec risque couvert, nature et responsable | 0,5 |
| b-3 | Verrouillage (situations et factures, devis signés, périodes) et piste d'audit, avec risque couvert, nature et responsable ; séparation des tâches | 0,5 |

**Réponse attendue**

*2.3 a) – De la fiabilité des données à celle des marges et des comptes*

Un système d'information de gestion est **fiable** lorsque ses données sont exhaustives, exactes, rattachées à la bonne période et au bon objet, et traçables de la pièce d'origine jusqu'au résultat (F10 § 3). La marge d'un chantier et les comptes de l'entreprise reposent sur les mêmes données de base : leurs défauts n'ont pas tous le même effet.

**Des défauts qui faussent la marge de chaque chantier** (0,5 pt) :
- **Heures** : remplies de mémoire le vendredi, et 15 % sans chantier : le coût de main-d'œuvre de chaque chantier est approximatif et sous-estimé ; un chantier en dérive n'est pas repéré, et les comparaisons (équipes contre partenaires, secteurs, conducteurs) sont faussées.
- **Achats** : 20 % sans chantier, répartis au prorata du chiffre d'affaires : un chantier d'isolation gourmand en matériaux paraît plus rentable qu'il n'est, un chantier de chauffage confié à un partenaire moins rentable ; la répartition transfère la marge d'un chantier à l'autre.
- Ces défauts ne changent pas le résultat de l'entreprise (les heures sont payées, les achats enregistrés en comptabilité), mais ils privent la direction de la marge **par chantier**, que le plan « Cap 2029 » veut maîtriser, et faussent le **chiffrage des devis futurs**, fondé sur des coûts réels mal connus ; les heures sans chantier, absentes de toute marge, font même paraître le total des marges meilleur qu'il n'est.

**Des défauts qui faussent aussi les comptes** (0,5 pt) :
- **Avancement et situations** : déclaré sans contrôle, l'avancement réel des dix rénovations globales examinées était inférieur de 15 points à l'avancement déclaré ; les situations facturées (1,2 M€ pour 40 chantiers en cours) sont donc en avance sur les travaux. Si le chiffre d'affaires des chantiers en cours est constaté d'après les situations ou l'avancement déclaré, une surestimation de l'avancement fait apparaître en 2026 un chiffre d'affaires et une marge que les travaux n'ont pas encore produits ; dans tous les cas, des clients paient des travaux non réalisés (litiges, confiance). Le traitement comptable précis relève d'une autre UE et n'est pas attendu.
- **Factures des partenaires** reçues tardivement : 300 k€ de charges relatives à 2026 n'étaient pas connues au 31 janvier ; si elles ne sont pas identifiées à la clôture, le résultat de 2026 est surestimé.
- **Situations modifiables** et avenants non enregistrés : sans **piste d'audit**, on ne peut pas reconstituer le chemin d'une donnée de la pièce au résultat ni prouver ce qui a été facturé.
- Or **les comptes 2026 présentés au comité stratégique ont été arrêtés à partir des mêmes données** : le fonds fonde sur eux ses décisions (financement des agences, valeur de sa participation) ; une donnée de gestion non fiable devient une information financière non fiable.

*2.3 b) – Quatre contrôles intégrés au système d'information*

Un **contrôle applicatif** est intégré au traitement des données (à la saisie, au traitement, aux interfaces, en sortie) ; il est **préventif** s'il empêche l'erreur, **détectif** s'il la révèle après coup ; il est d'autant plus efficace qu'il est automatisé et qu'il respecte la **séparation des tâches** (F10 § 2 et 3 ; COSO 2013 en appui).

| Contrôle | Contenu chez SOLVÉRANCE Habitat | Risque couvert | Nature | Responsable |
|---|---|---|---|---|
| **À la saisie** (0,5 pt avec le suivant) | heures saisies chaque jour sur la tablette par le chef d'équipe, en choisissant le chantier dans la liste des chantiers ouverts au planning ; contrôles de vraisemblance (pas plus de 10 heures par jour et par compagnon, total égal aux heures de présence) ; « dépôt et divers » limité et motivé ; validation hebdomadaire par le conducteur de travaux | heures inexactes ou non imputées (15 %) | préventif | directrice des opérations, avec les conducteurs de travaux |
| **De rattachement** | numéro de chantier obligatoire pour toute commande (passée depuis le logiciel de devis), toute sortie du dépôt et toute facture de partenaire ou de négociant ; une facture sans numéro est mise en attente et n'est pas payée avant affectation | 20 % des achats et une facture de partenaire sur trois sans chantier | préventif | assistantes d'exploitation (achats) et comptabilité, sous l'autorité du directeur administratif et financier |
| **Rapprochement** (0,5 pt) | chaque mois, avant d'émettre une situation : avancement déclaré rapproché des heures et des achats consommés par rapport au devis, et validé par une autre personne que le conducteur (directrice des opérations ou bureau d'études pour les rénovations globales) ; rapprochement commande, livraison et facture ; liste des factures de partenaires attendues pour les chantiers terminés, examinée à chaque clôture ; écarts au-delà d'un seuil analysés et tracés | situations en avance sur les travaux (15 points) ; 300 k€ de factures non reçues ; achats facturés non livrés | détectif (préventif pour la validation de l'avancement avant l'émission de la situation) | directeur administratif et financier, avec la directrice des opérations |
| **Verrouillage** (0,5 pt) | situation ou facture émise non modifiable, corrigée seulement par un avoir, numérotation continue ; devis signé figé, tout avenant étant une nouvelle version signée par le client et liée au chantier ; clôture mensuelle des heures et des achats après validation ; journal des modifications (piste d'audit) ; droits de modification limités | situations modifiées après envoi ; avenants non tracés ; données modifiées après l'analyse | préventif | directeur administratif et financier ; paramétrage par le responsable informatique avec l'éditeur |

La validation de l'avancement par une personne distincte de celle qui le déclare applique la **séparation des tâches** ; la piste d'audit permet de reconstituer, pour tout chantier, le chemin du devis aux comptes.

**Réponses tolérées**
- Autres contrôles pertinents (pointage des heures sur la tablette à l'arrivée et au départ du chantier ; inventaire du stock du dépôt), s'ils relèvent bien de la catégorie demandée.
- Rapprochement de la marge par chantier avec la comptabilité (total des marges et résultat) proposé à la place du rapprochement commande, livraison et facture.
- Effet sur les comptes présenté en termes de résultat et de trésorerie, sans règle comptable.
- Effet de l'avancement présenté comme dépendant de la manière dont le chiffre d'affaires des chantiers en cours est constaté, sans règle comptable.
- Rapprochement qualifié de préventif lorsqu'il conditionne l'émission de la situation.

**Erreurs fréquentes**
- *Analyse comptable hors attente* (`ET-34`, `JUR-T07`) — exposé des règles de l'avancement, des contrats à long terme ou de l'audit légal ; juste : effets sur la fiabilité des données et des comptes, sans règle comptable.
- *Contrôles génériques* (`JUR-T01`) — « mettre en place un contrôle interne » sans contenu, risque, nature ni responsable ; juste : quatre contrôles précis, tirés des défauts de l'annexe 2.2 B.
- *Tout confié à l'informatique* (`JUR-T03`) — contrôle confié au seul responsable informatique ; juste : le contrôle appartient au métier (opérations, achats, comptabilité), l'informatique le paramètre.
- *Séparation des tâches oubliée* — le conducteur de travaux déclare l'avancement et émet seul la situation ; juste : validation par une autre personne.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| COSO — Internal Control — Integrated Framework (2013) | contrôle interne, cité en appui (contrôles généraux et applicatifs) | `coso_2013` / F10 § 2 | en vigueur |
| Contrôles applicatifs, séparation des tâches, piste d'audit, fiabilité des systèmes d'information décisionnels | typologie et principes | F10 § 2, 3.1, 3.2 et 3.5 | notion de cours |

---

### 2.4 – La gouvernance stratégique des données et la base des logements (3 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.a` « Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques » ; `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) » ; `2.3.f` « Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques » ; `2.3.d` « Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique ». Monétisation abordée de façon critique ; rôles illustratifs, non normatifs ; aucune analyse juridique.

**Annexes mobilisées** : annexes 1.1 (organigramme, absence de direction des systèmes d'information, un seul informaticien, fonds TALVÉRIS Croissance), 2.1 (identifiants, défauts des dossiers), 2.3 (base des logements, services en ligne et conditions de sortie, positions) et 2.4 (DAMA-DMBOK, RGPD, Data Act, SecNumCloud).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance des données définie (DAMA-DMBOK) ; cinq principes (qualité, conformité, sécurité, valorisation, cycle de vie), chacun appliqué à un constat des annexes | 0,5 |
| a-2 | Qui en répond : président, propriétaires métier des données, coordination par le directeur administratif et financier, intendance technique par le responsable informatique, référent pour la protection des données ; rôles proportionnés à une PME | 0,5 |
| b-1 | Actif immatériel défini ; deux sources de valeur et trois risques tirés de l'annexe 2.3 | 0,5 |
| b-2 | Réponse critique aux positions de M. VORGNAC (valeur conditionnelle, relance de tous les propriétaires depuis 2018) et de M. ROUSSERGUES (données personnelles, responsabilité plutôt que propriété) | 0,5 |
| c-1 | Souveraineté (localisation, droit applicable aux fournisseurs, dépendance) et réversibilité (conditions inégales de sortie, photos, bibliothèque de prix) analysées d'après les annexes 2.3 et 2.4 | 0,5 |
| c-2 | Trois mesures : inventaire et plan de réversibilité, exports réguliers en formats ouverts, conditions contractuelles de sortie et de localisation au renouvellement | 0,5 |

**Réponse attendue**

*2.4 a) – Les principes de la gouvernance des données*

La **gouvernance des données** est l'ensemble des décisions, des rôles, des règles et des processus qui garantissent que les données de l'organisation sont fiables, conformes, protégées et exploitées au service de sa stratégie, tout au long de leur cycle de vie ; le référentiel DAMA-DMBOK la place au centre de ses onze domaines de connaissance (annexe 2.4 ; F07 § 8). Ce n'est ni un outil ni une affaire d'informaticiens : à SOLVÉRANCE Habitat, les données des chantiers et des logements sont au cœur du métier et du plan « Cap 2029 ».

Cinq principes, appliqués aux annexes (0,5 pt) :
- **Qualité** : « une donnée, une source, un identifiant » ; saisie unique à la source, contrôles à la saisie (35 dossiers sur 100 avec une adresse écrite différemment, avenants non enregistrés, heures de mémoire).
- **Conformité** : registre des activités de traitement, finalités déterminées, données limitées au nécessaire (aucun registre ; base des logements, prospects compris, conservée sans finalité définie).
- **Sécurité** : accès selon le besoin d'en connaître, classification des données selon leur sensibilité (avis d'imposition ouverts à tous les salariés des services administratifs ; photos de l'intérieur des logements ; aucune liste des accès).
- **Valorisation** : exploiter d'abord les données pour le plan (marge par chantier, chiffrage, connaissance des logements des clients) ; n'envisager une valorisation externe qu'une fois la qualité et la conformité établies (demande du fonds).
- **Cycle de vie** : de la création à la suppression, une durée de conservation par catégorie de données (prospects sans devis signé, clients, justificatifs des ménages, fiches papier de 2018 à 2021), un archivage puis une suppression effective ; aujourd'hui « aucune donnée n'a jamais été supprimée ». Les durées sont fixées avec un conseil, au regard des obligations de conservation, sans analyse juridique ici.

**Qui en répond** (0,5 pt) : dans une PME sans direction des systèmes d'information, des rôles légers, inspirés du DAMA-DMBOK et proportionnés (le programme les tient pour illustratifs) :
- le **président** porte la politique des données et arbitre ; les données sont examinées en comité de direction ;
- des **propriétaires** métier, responsables des définitions, des règles de qualité et des droits d'accès de leur domaine : la directrice des opérations pour les données des chantiers, la responsable du bureau d'études pour les données techniques des logements, la responsable commerciale pour les clients et les prospects, le directeur administratif et financier pour les données financières et les dossiers d'aides ;
- le **directeur administratif et financier**, chargé du système d'information, **coordonne** la démarche (référent des données ; un responsable des données à plein temps n'est pas justifié à cette taille) ;
- le **responsable informatique**, **intendant** technique (droits d'accès, exports, sauvegardes, relation avec les éditeurs) ; des intendants métier (une assistante d'exploitation, une chargée des dossiers d'aides) corrigent les anomalies au quotidien ;
- un **référent pour la protection des données** personnelles (le cas échéant un délégué à la protection des données, mutualisé ou externe), qui tient le registre.

*2.4 b) – La base des logements, actif immatériel*

Un **actif immatériel** est une ressource sans substance physique, que l'entreprise maîtrise et dont elle attend des avantages futurs (il n'est pas question ici de son inscription dans les comptes) ; une base de données en est un lorsqu'elle est exploitable, fiable et utilisable légitimement. Sa valeur est une **valeur d'usage** (ce qu'elle apporte à l'activité) ou une **valeur d'échange** (ce qu'un tiers serait prêt à payer, ici à travers la valeur de l'entreprise) ; elle est contextuelle, périssable et grevée de risques (F07 § 8.6). Aucune valorisation chiffrée n'est attendue.

**Deux sources de valeur** (0,5 pt avec les risques), parmi :
- **chiffrer plus juste** : comparer les logements visités (année, parois, surfaces) aide le bureau d'études et les conseillers à estimer les quantités et les coûts, donc la marge des chantiers (Mme FONTRIVAL) ;
- **mieux servir les clients** : la connaissance des logements des clients permet de leur proposer les étapes suivantes d'une rénovation, dans le respect des finalités déclarées, et de préparer l'implantation des agences ;
- **valeur d'échange** : environ 9 000 logements décrits pièce par pièce, qui complètent le savoir-faire de chiffrage (bibliothèque de prix) : un patrimoine immatériel qu'un acquéreur examinera lors de la cession envisagée par le fonds, au même titre que les savoir-faire.

**Trois risques**, parmi :
- **Non-conformité** : données conservées sans durée, prospects visités depuis 2018 sans devis signé, aucun registre ; une mise en conformité imposerait de purger une grande partie de la base, et un acquéreur verrait un passif plutôt qu'un actif ;
- **Fuite ou perte** : 320 000 photos de l'intérieur des logements, des avis d'imposition ouverts à tous les salariés administratifs ; une fuite atteindrait l'intimité des ménages et la confiance des clients, que le plan veut préserver ;
- **Dépendance et perte d'accès** : l'application de visite ne permet de récupérer les photos qu'une à une et supprime les données 30 jours après la fin du contrat ; l'entreprise ne contrôle pas pleinement l'actif qu'elle croit détenir ;
- **Qualité et obsolescence** : consommations déclarées et non mesurées, logements transformés depuis la visite, identifiants multiples et adresses incohérentes, fiches papier numérisées non exploitables : la valeur annoncée serait surestimée.

**Réponse aux positions** (0,5 pt) :
- À **M. VORGNAC** : la base peut avoir de la valeur, mais **à condition** d'être conforme, documentée, fiable et récupérable ; en l'état, l'examen d'un acquéreur révélerait surtout des risques. Relancer **tous** les propriétaires visités depuis 2018 utiliserait des données collectées pour établir un devis, parfois il y a huit ans, à une autre fin et sans durée de conservation définie : ce serait contraire aux principes de finalité et de durée limitée rappelés à l'annexe 2.4, et risqué pour la réputation. Il faut d'abord fixer les finalités et les durées, purger, puis ne relancer que les personnes concernées dans ce cadre. La valorisation doit être abordée de façon critique : la valeur vient de l'usage interne plus que d'une exploitation commerciale des données personnelles.
- À **M. ROUSSERGUES** : des données qui se rapportent à des personnes identifiables (adresses, photos de l'intérieur, consommations, revenus) ne sont pas une marchandise dont l'entreprise disposerait librement : elle en est **responsable** (finalités, durées, sécurité) plus que propriétaire ; et une partie est détenue par des éditeurs dont les conditions de sortie ne garantissent pas la récupération. Les données non personnelles (bibliothèque de prix, statistiques anonymes) relèvent davantage de son savoir-faire.

*2.4 c) – Souveraineté et réversibilité des services en ligne*

La **souveraineté numérique** est la capacité de l'entreprise à garder la maîtrise de ses données : leur localisation, le droit applicable à ceux qui les hébergent, sa dépendance aux fournisseurs et les compétences pour en changer ; la **réversibilité** est la capacité de récupérer ses données et de poursuivre son activité, en interne ou chez un autre fournisseur, en fin de contrat (F03 § 5.3 ; F07 § 8.5).

**Analyse** (0,5 pt) :
- **Localisation et droit applicable** : l'application de visite héberge hors de l'Union européenne les données les plus sensibles (photos de l'intérieur, consommations, adresses) : ce transfert n'est possible que vers un pays reconnu comme assurant une protection adéquate ou avec des garanties appropriées (annexe 2.4), ce que rien dans l'annexe 2.3 ne garantit (conditions générales acceptées en ligne en 2022, aucun registre, personne de désigné). Deux fournisseurs, dont la messagerie qui stocke les justificatifs des ménages, ont leur siège hors de l'Union : même hébergées en Europe, leurs données peuvent être exposées à des demandes d'autorités étrangères (annexe 2.3). La localisation en Europe ne suffit pas à faire un hébergement souverain.
- **Dépendance** : six services en ligne souscrits au fil de la croissance (annexe 1.1), dont cinq portent les données des clients et des logements, chez plusieurs fournisseurs aux conditions de sortie différentes ; des conditions générales acceptées en ligne et modifiables ; un seul informaticien, qui « ne sait pas récupérer les photos ».
- **Réversibilité inégale** : bonne pour la gestion de la relation client et la messagerie (export complet), faible pour l'application de visite (photos une à une, suppression à 30 jours), pour le logiciel de devis (bibliothèque de prix construite depuis 2018 dans le seul format de l'éditeur, export complet « au cas par cas ») et pour le calcul thermique (fichiers lisibles par ce seul logiciel). Les deux actifs de données les plus précieux sont les moins récupérables.
- **Leviers** : le règlement sur les données (Data Act), applicable depuis le 12/09/2025, oblige les fournisseurs de services d'informatique en nuage à permettre le changement de fournisseur et la portabilité des données (annexe 2.4) : il donne un appui pour obtenir des conditions de sortie ; le RGPD impose que le contrat avec chaque éditeur, sous-traitant, prévoie le sort des données en fin de contrat, ce que des conditions générales acceptées en ligne ne garantissent pas. SecNumCloud est une référence pour juger la protection d'une offre contre les lois extra-européennes, sans être une obligation pour une PME.

**Trois mesures** (0,5 pt), parmi :
1. **Inventaire et plan de réversibilité** : pour chaque service, les données portées, leur sensibilité, leur localisation, le droit applicable au fournisseur et les conditions de sortie ; priorité aux photos et à la bibliothèque de prix ; scénario de sortie écrit pour les deux services les plus critiques.
2. **Exports réguliers et testés** des données critiques (formulaires et photos de visite par lots, bibliothèque de prix, calculs thermiques en format lisible) dans des **formats ouverts**, vers un espace maîtrisé par l'entreprise, avec un essai de relecture ; cela réduit la dépendance sans attendre la fin d'un contrat.
3. **Conditions contractuelles au renouvellement** : clauses de réversibilité (formats, délais, assistance, absence de suppression avant confirmation), contrat de sous-traitance conforme au RGPD, localisation dans l'Union pour les données sensibles, en s'appuyant sur le Data Act ; critère de souveraineté (siège, droit applicable, qualification SecNumCloud pour les données les plus sensibles) dans tout futur choix, sans que le choix d'un hébergement soit à faire ici.
4. **Minimisation** : supprimer les données devenues inutiles (prospects anciens, justificatifs des dossiers clos) réduit à la fois l'exposition hors de l'Union et le volume à récupérer.

**Réponses tolérées**
- Rôles différents s'ils sont justifiés et proportionnés (propriétaire unique des données des clients et des logements, par exemple la responsable commerciale) ; recours à un délégué à la protection des données externe présenté comme une option.
- Autres sources de valeur (connaissance du parc de logements par secteur pour les agences, appui aux dossiers d'aides) ; mention des caractéristiques du Big Data (volume et variété des photos) si elle reste reliée au cas.
- Mesures de sécurité (droits d'accès aux justificatifs, chiffrement) proposées en c), si elles sont reliées à la souveraineté ou à la réversibilité.

**Erreurs fréquentes**
- *Hébergement « souverain » réduit à la localisation* (`ET-37`) — « les données sont en Europe, il n'y a pas de problème » ; juste : le droit applicable au fournisseur compte autant que la localisation.
- *Monétisation sans regard critique* (`JUR-G10`, `JUR-N01`) — reprendre l'idée de relancer tous les propriétaires ou de « vendre la base » sans finalité, durée ni qualité ; juste : valeur conditionnelle, usages internes d'abord.
- *Données personnelles traitées comme une propriété* — « l'entreprise fait ce qu'elle veut de ses données » ; juste : responsabilité de l'entreprise, principes rappelés en annexe 2.4.
- *Analyse juridique ou statut affirmé sans date* (`ET-41`, `JUR-T07`) — développements sur les droits des personnes ou sur le régime des transferts ; juste : s'en tenir aux repères datés de l'annexe 2.4.
- *Gouvernance réduite à un organigramme* (`JUR-T01`) — création d'un responsable des données à plein temps, sans principes ni lien avec les constats ; juste : rôles légers, attachés aux métiers.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | gouvernance des données, rôles de propriétaire et d'intendant | `dama_dmbok2` / F07 § 8.1-8.2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | finalités, durée de conservation, sécurité, registre, sous-traitant, transferts hors de l'Union (repères de l'annexe 2.4) | `rgpd` / F15 § 2, 5 et 7 | en vigueur |
| Règlement (UE) 2023/2854 (Data Act), applicable depuis le 12/09/2025 | changement de fournisseur et portabilité des données (chapitre VI) | `data_act` / F07 § 8.5 | en vigueur |
| SecNumCloud 3.2 (ANSSI) | qualification d'offres de services d'informatique en nuage, protection contre les lois extra-européennes | `secnumcloud_3_2` / F03 § 5.3 | en vigueur |
| Actif immatériel, valeur d'usage et d'échange, souveraineté et réversibilité | définitions | F07 § 8.5-8.6 ; F03 § 5.3 | notion de cours |
