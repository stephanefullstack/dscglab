# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 8 — Dossier 2 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 architecture et urbanisation, F04 ESN et contrats, F10 audit et fiabilisation, F11 blockchain et crypto-actifs, F13 intelligence artificielle, la fiche commune `commun/fiches/sapin2_lcbft_mica.md` § 3, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Ne sont pas attendus, car hors programme : les écritures et le traitement comptable des opérations, des avoirs ou des jetons, la fiscalité, le détail des formats de facture au-delà de leur nom, la conception d'un modèle d'apprentissage automatique, le développement d'une blockchain ou d'un contrat intelligent, l'analyse juridique approfondie du contrat, ainsi que la qualification du module de détection au regard du règlement sur l'intelligence artificielle. Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Fiabilité des données comptables et décisionnelles | `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers | 3 |
| 2.2 Facturation électronique et architecture du SI financier | `1.3.a` Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) ; `1.3.e` Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers ; `1.3.b` Cartographie applicative et fonctionnelle des SI ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) | 3 |
| 2.3 Intelligence artificielle et prévention des fraudes | `4.1.f` Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques ; `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA | 2 |
| 2.4 Sécurisation du contrat avec l'ESN | `1.4.a` Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques ; `1.4.b` Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle ; `1.4.c` Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD ; `1.4.d` Méthodologie de négociation contractuelle et analyse des risques ; `1.4.e` Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) | 3 |
| 2.5 Blockchain et crypto-actifs : trois propositions | `3.3.a` Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations ; `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.d` Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain | 3 |
| **Dossier 2 – Fiabiliser le système d'information financier et évaluer l'apport des nouvelles technologies** |  | **14** |

Répartition indicative : connaissances (définitions de la fiabilité d'un SI comptable et décisionnel, du principe de la détection d'anomalies par apprentissage automatique, du contrat au forfait et de la blockchain : items 2.1 a-1, 2.3-1, 2.4 a-1 et 2.5 a-1) 2 points ; analyse des annexes et recommandations 12 points. Durée conseillée : 14 points × 4,5 minutes ≈ 1 h 03.

---

### 2.1 – Fiabilité des données comptables et décisionnelles (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ».

**Annexes mobilisées** : annexes 1.1 (organisation, plan « ALTIVERNE 2030 ») et 2.1 (note du directeur administratif et financier, incidents, remarques des auditeurs externes).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fiabilité d'un SI comptable et décisionnel définie (exhaustivité, exactitude, réalité et autorisation, rattachement à la bonne période, cohérence, traçabilité, disponibilité à temps) | 0,5 |
| a-2 | Quatre risques distincts, chacun étayé par un fait chiffré de l'annexe 2.1 (0,5 par paire de risques) | 1 |
| b-1 | Quatre mesures, une par famille imposée, chacune reliée explicitement à un risque identifié (0,5 par paire de mesures) | 1 |
| b-2 | Un indicateur complet (formule, source, fréquence, cible, axe) attaché à l'une des mesures | 0,5 |

**Réponse indicative**

*2.1 a) – Définition et risques*

Un système d'information comptable et décisionnel est fiable lorsque les données qu'il produit sont **exhaustives** (toutes les opérations sont enregistrées, une seule fois), **exactes** (montants, tiers, comptes), **réelles et autorisées** (elles correspondent à des opérations validées par une personne habilitée), **rattachées à la bonne période**, **cohérentes** d'une application à l'autre et **traçables** : une piste d'audit permet de remonter de la pièce justificative au solde et au tableau de bord, et inversement. Pour un groupe qui veut des « processus financiers fiabilisés » (plan « ALTIVERNE 2030 »), la fiabilité tient autant aux contrôles intégrés au SI qu'à l'organisation des tâches (0,5 pt).

Quatre risques parmi les suivants, chacun étayé (1 pt, 0,5 par paire) :

| Risque | Faits de l'annexe 2.1 |
|---|---|
| R1 – Paiements frauduleux ou non autorisés | une même comptable modifie les coordonnées bancaires des fournisseurs et prépare les campagnes de virements ; validation globale de campagnes d'environ 1 200 virements sans liste des coordonnées modifiées ; aucun contre-appel ; 350 000 € virés vers le compte frauduleux, 100 000 € récupérés, soit 250 000 € perdus ; 14 personnes ayant des droits d'administration du PGI et 30 comptes d'anciens salariés actifs |
| R2 – Chiffre d'affaires de maintenance incomplet ou inexact | avenants transmis par courriel une fois par mois ; 600 contrats facturés après leur résiliation (0,9 M€ d'avoirs) et 400 appareils jamais facturés (0,6 M€ par an) ; ressaisie des interventions hors contrat : 1 500 avoirs de correction ; environ 3 000 factures encore établies sur papier en agence |
| R3 – Dettes fournisseurs et charges inexactes (doublons) | réception par trois canaux (plateforme, courriel, courrier) et ressaisie de la plupart des 90 000 factures ; 220 factures payées deux fois (0,4 M€) ; aucun rapprochement de la facture avec la commande et la réception |
| R4 – Intégrité des interfaces et du paramétrage, piste d'audit rompue | fichier d'interface des bons d'intervention modifiable avant intégration, sans nombre de lignes ni total de contrôle, contrôlé à l'œil ; modifications du paramétrage (conditions de paiement, taux de TVA) faites en production par le prestataire, sans trace ni validation : une erreur de paramétrage se répercute sur toutes les factures |
| R5 – Information décisionnelle peu fiable et tardive | reporting du chiffre d'affaires de maintenance établi sur tableur, avec un écart inexpliqué d'environ 2 % avec la comptabilité ; comptes des filiales remontés par tableur ; clôture mensuelle à J+12 pour une cible de J+5 ; comptes 2026 arrêtés avec quatre semaines de retard |

*2.1 b) – Quatre mesures de fiabilisation et un indicateur*

| Famille | Mesure proposée à ALTIVERNE | Risque traité |
|---|---|---|
| Contrôles applicatifs | contrôles bloquants à la saisie et avant paiement : unicité du couple fournisseur / numéro de facture / montant ; rapprochement automatique de la facture avec la commande et la réception des pièces avant mise en paiement ; blocage de tout paiement vers des coordonnées bancaires modifiées depuis moins de trente jours tant qu'elles n'ont pas été confirmées | R3, R1 |
| Séparation des tâches | matrice des rôles : la création et la modification des fiches fournisseurs et des coordonnées bancaires sont confiées à une cellule « référentiel des tiers » distincte des comptables qui préparent les virements ; contre-appel du fournisseur à un numéro déjà connu, et non à celui du courriel ; liste des coordonnées modifiées jointe à chaque campagne soumise au directeur administratif et financier ; retrait des 14 droits d'administration, désactivation des 30 comptes d'anciens salariés, revue semestrielle des habilitations | R1 |
| Traçabilité | journalisation des modifications des fiches tiers et du paramétrage (auteur, date, ancienne et nouvelle valeur) ; gestion des changements : demande écrite, essai dans un environnement de recette, validation par la direction financière, mise en production par une autre personne que l'auteur ; piste d'audit fiable de la facture au paiement | R4 |
| Interfaces automatisées et rapprochements | interface automatisée entre le logiciel des interventions et le PGI, avec nombre de bons et total de contrôle, rejets tracés et traités sous 24 heures, suppression des ressaisies et des carnets papier ; saisie des avenants en agence dans un circuit de validation du PGI ; rapprochement mensuel automatique des contrats actifs, des appareils et des factures ; rapprochement bancaire automatique ; reporting alimenté par le PGI, seule source du chiffre d'affaires | R2, R5 |

Indicateur (0,5 pt), un parmi :

| Axe | Indicateur | Formule | Source | Fréquence | Cible |
|---|---|---|---|---|---|
| Processus | Changements de coordonnées bancaires vérifiés | changements de coordonnées bancaires confirmés par contre-appel et validés par une seconde personne avant tout paiement / changements de coordonnées bancaires enregistrés | journal des modifications des fiches fournisseurs du PGI | mensuelle | 100 % dès juin 2027 |
| Processus | Intégration automatique des factures fournisseurs | factures fournisseurs intégrées dans le PGI sans ressaisie / factures fournisseurs reçues | PGI et plateforme agréée | mensuelle | au moins 90 % fin 2027 (aucune aujourd'hui : depuis septembre 2026, 30 % des factures arrivent par la plateforme, toutes ressaisies) |
| Financier | Écarts entre contrats actifs et facturation | nombre d'écarts constatés au rapprochement (contrats résiliés encore facturés + appareils ajoutés par avenant non facturés) | rapprochement mensuel du PGI (contrats et factures) | trimestrielle | 0 écart fin 2027 (1 000 écarts en novembre 2026 : 600 contrats résiliés encore facturés et 400 appareils non facturés) |

Priorité : la séparation des tâches sur les coordonnées bancaires et la mise en paiement, qui ne coûte presque rien et traite le risque qui a déjà coûté 250 000 €, puis les contrôles applicatifs et l'interface, à livrer avant le 1er septembre 2027.

**Réponses tolérées**
- Risques formulés selon les assertions de l'audit (exhaustivité, réalité, exactitude, séparation des exercices) ou selon la typologie des risques du SI (défaillances opérationnelles, risque de fraude, risque réglementaire), dès lors qu'ils sont étayés par l'annexe 2.1.
- Mesures réparties autrement entre les quatre familles (par exemple le contrôle de doublon classé en rapprochement), si chacune des familles imposées est couverte et reliée à un risque.
- Référence au COSO 2013 (activités de contrôle, contrôles généraux informatiques) ou à COBIT 2019 en appui, sans développement.
- Tout autre indicateur complet et contextualisé (délai de clôture mensuelle, cible J+5 ; nombre de factures payées en double, cible 0).

**Erreurs fréquentes**
- *Risques énumérés sans lien avec le cas* (`JUR-T01`, `ET-39`) — liste générique (« risque de fraude, risque d'erreur ») ; juste : chaque risque appuyé sur un fait et un chiffre de l'annexe 2.1.
- *Fiabilisation réduite à l'outil* (`JUR-T12`) — « changer de PGI » ; juste : contrôles applicatifs, organisation des tâches, habilitations et traçabilité, dans le PGI existant.
- *Dérive vers l'audit des comptes* (`ET-34`) — écritures de correction, provisions, appréciation des comptes 2026 ; juste : l'UE 5 traite les processus et les contrôles du SI qui produisent les données.
- *Indicateur incomplet* (`JUR-A02`, `ET-18`) — « taux de fraude » sans formule, source ni cible ; juste : cinq champs renseignés et reliés à la mesure.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Fiabilisation des SI comptables et décisionnels | séparation des tâches, piste d'audit, contrôles applicatifs, interfaces, SI décisionnel | F10 § 2 et 3 | guide p. 266-267 et 307 |
| Contrôles généraux informatiques (accès, changements, exploitation) | remarques des auditeurs externes | `nep_315` ; F10 § 1.3 | en vigueur (arrêté du 13/11/2024) |

---

### 2.2 – Facturation électronique et architecture du SI financier (3 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.a` « Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) » ; `1.3.e` « Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers » ; `1.3.b` « Cartographie applicative et fonctionnelle des SI ».
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) » (rôle de la plateforme agréée et des formats Factur-X, UBL et CII, seulement nommés).

**Annexes mobilisées** : annexes 1.1 (filiales), 2.1 (outils, volumes, facturation électronique et ses repères datés) et 2.2 (périmètre du projet, module de détection).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Impacts organisationnels, distingués entre comptabilité fournisseurs et facturation des clients | 0,5 |
| a-2 | Impacts juridiques, appuyés sur le calendrier de l'annexe 2.1 (ETI émettrice depuis le 01/09/2026 ; fournisseurs PME au 01/09/2027) | 0,5 |
| a-3 | Impacts comptables (processus et qualité de l'information, sans écriture) | 0,5 |
| b-1 | Schéma lisible : composants demandés, zones de la cartographie, flux structurés et contrôles | 1 |
| b-2 | Deux règles d'urbanisation justifiées par le cas | 0,5 |

**Réponse indicative**

*2.2 a) – Impacts du passage à la facturation électronique*

| Impact | Comptabilité fournisseurs | Facturation des clients |
|---|---|---|
| Organisationnel (0,5 pt) | les 18 comptables passent de la ressaisie (environ 5 000 factures chacune par an) au contrôle des anomalies, au traitement des rejets et des litiges et à la relation avec les fournisseurs ; un circuit d'approbation (« bon à payer ») associe les acheteurs, l'usine et les agences qui ont reçu les pièces ; les statuts de traitement renvoyés par la plateforme (reçue, refusée, approuvée, payée) sont attribués à des responsables ; pic de charge à partir du 1er septembre 2027, quand les 4 800 PME et micro-entreprises fournisseurs, 80 % des fournisseurs, émettront à leur tour ; formation et conduite du changement, que le contrat de LUMIGRÈS exclut | fin des carnets de factures en agence : les interventions hors contrat sont facturées depuis le PGI ou le logiciel des interventions ; les assistantes d'agence cessent la ressaisie ; l'annuaire impose de tenir à jour l'identification et l'adresse de facturation électronique de chaque client (bailleurs, syndics, établissements) ; le service de facturation suit les factures refusées par les clients |
| Juridique (0,5 pt) | la réception électronique est obligatoire pour toutes les entreprises depuis le 01/09/2026 : la société mère la respecte techniquement, mais télécharge en PDF puis ressaisit les factures, ce qui fait perdre l'intérêt et la traçabilité du flux électronique ; à partir du 01/09/2027, la quasi-totalité des factures arrivera par la plateforme ; la plateforme agréée, souscrite dans l'urgence, est un prestataire critique : contrat à revoir (niveaux de service, sécurité, réversibilité) | entreprise de taille intermédiaire, la société mère doit **émettre** ses factures électroniques par une plateforme agréée depuis le 01/09/2026 : parmi les quelque 3 000 factures papier des agences, celles adressées à des clients assujettis ne sont pas conformes ; pour les clients non assujettis (syndicats de copropriétaires, par exemple), les données de l'opération relèvent du e-reporting, que les carnets papier ne permettent pas davantage ; les opérations internationales (clients étrangers) relèvent du e-reporting par la plateforme ; les filiales relèvent de leur propre droit (annexe 2.1) |
| Comptable (0,5 pt) | factures reçues en données structurées : intégration automatique, pré-imputation, rapprochement avec la commande et la réception, canal unique qui supprime les doublons nés de la réception par courriel et par courrier (220 doublons en 2026) ; piste d'audit de bout en bout, horodatée ; dettes fournisseurs plus fiables et clôture accélérée (cible J+5) | factures émises en données structurées et suivies par statut : chiffre d'affaires et créances plus fiables, relances fondées sur des statuts, rapprochement des encaissements facilité ; facture électronique conservée comme original |

*2.2 b) – Architecture cible et cartographie urbanisée*

Schéma attendu (1 pt), format libre ; exemple :

```
ZONE PILOTAGE        Reporting et tableaux de bord de la direction financière  <—  PGI (source unique)
                     Consolidation : comptes des filiales belge et suisse remontés dans un plan de comptes commun
                     Module de détection des anomalies (lecture seule) —> alertes —> cellule de contrôle (décision humaine)
                                    ^ lit fiches tiers, factures, paiements
ZONE RÉFÉRENTIELS    Référentiel des tiers (clients, fournisseurs, coordonnées bancaires), contrats et appareils, plan de comptes
                     un seul propriétaire par référentiel ; modifications par circuit de validation
ZONE GESTION         PGI : achats, comptabilité fournisseurs et clients, facturation, trésorerie
ZONE OPÉRATIONS      Logiciel des interventions (bons des techniciens)  —> bons valorisés —>  PGI
ZONE ÉCHANGES        Couche d'intégration : interfaces automatisées avec totaux de contrôle et rejets tracés
                     <—> Plateforme agréée (Factur-X, UBL ou CII) <—> fournisseurs et clients ; statuts de traitement —> PGI
                         Plateforme agréée —> administration (e-reporting ; annuaire et concentration des données par le portail public)
                     <—> Banque : fichiers de virements validés —> ; <— relevés pour le rapprochement automatique
                     <—  Logiciels comptables des filiales (remontée normalisée)
```

Deux règles d'urbanisation, justifiées (0,5 pt) parmi :
- **un référentiel unique par donnée, avec un propriétaire** : les fiches fournisseurs et leurs coordonnées bancaires n'existent qu'à un endroit, modifiées par une seule cellule selon un circuit de validation ; c'est la réponse architecturale à la fraude d'octobre 2026 et la condition d'une détection fiable ;
- **des échanges par une zone d'échange maîtrisée**, et non par des fichiers modifiables d'application à application : interfaces automatisées avec contrôle de complétude, statuts et rejets tracés ; cela supprime les ressaisies et les fichiers sans total de contrôle relevés par les auditeurs ;
- **le découplage des blocs** : le module d'IA lit les données du PGI sans les modifier et peut être remplacé sans toucher à la comptabilité, ce qui limite la dépendance à LUMIGRÈS ;
- **une fonction implantée une seule fois** : toute la facturation passe par le PGI et la plateforme, plus de carnets d'agence ni de reporting parallèle sur tableur.

Cette cartographie relève de l'urbanisation, démarche stratégique qui organise le SI en blocs cohérents au service des processus financiers du plan « ALTIVERNE 2030 », et non d'un inventaire des logiciels.

**Réponses tolérées**
- Schéma en couches (métier, fonctionnelle, applicative, technique) ou en blocs, avec ou sans le vocabulaire zones, quartiers et îlots, s'il fait apparaître les flux et les contrôles.
- Module d'IA placé dans une zone « contrôle et conformité » ou dans la zone de gestion, s'il est présenté en lecture seule et relié à une décision humaine.
- Proposition d'étendre à terme le PGI ou un plan de comptes commun aux filiales, présentée comme une étape ultérieure.
- Impacts présentés en texte plutôt qu'en tableau, si les deux processus et les trois natures d'impact sont couverts.
- Distinction entre clients assujettis (facturation électronique) et non assujettis (e-reporting), si la conclusion sur les carnets papier est tirée.

**Erreurs fréquentes**
- *Urbanisation réduite à un inventaire technique* (`ET-20`, `JUR-G07`) — liste de serveurs et de logiciels ; juste : zones fonctionnelles, référentiels, flux et règles d'urbanisme au service des processus.
- *Calendrier faux ou vocabulaire périmé* (`ET-41`, `JUR-N02`) — écrire que l'émission ne concerne le groupe qu'en 2027, employer l'ancienne appellation des plateformes ou faire du portail public la plateforme d'échange ; juste : ETI émettrice depuis le 01/09/2026, plateformes agréées, portail public limité à l'annuaire et à la concentration des données.
- *Impacts comptables traités comme une question de régularité des comptes* (`ET-34`) — écritures, TVA détaillée ; juste : processus comptables (intégration, rapprochement, piste d'audit, délais de clôture).
- *Format de facture détaillé* (`JUR-T07`) — description de la structure d'un fichier ; juste : les formats sont seulement nommés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Généralisation de la facturation électronique (art. 91 de la loi de finances pour 2024) | calendrier 01/09/2026 et 01/09/2027, formats, e-reporting | `facturation_electronique_fr` ; F10 § 3.4 | en vigueur ; émission des PME et micro-entreprises applicable le 01/09/2027 [S] |
| Plateformes agréées ; portail public de facturation | plateforme d'échange, annuaire, concentrateur | `facturation_electronique_pa` ; F10 § 3.4 | en vigueur [S] |
| Urbanisation, cartographies, règles d'urbanisme | zones, référentiels uniques, zone d'échange, découplage | F03 § 1 et 2 | — |

---

### 2.3 – Intelligence artificielle et prévention des fraudes (2 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.f` « Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques » ; `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ».

**Annexes mobilisées** : annexes 2.1 (incidents, volumes, effectif de la comptabilité fournisseurs) et 2.2 (module et démonstration, clauses 3 et 7).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Principe présenté : apprentissage à partir de l'historique, score d'écart au comportement habituel, alerte au-delà d'un seuil ; distinction avec des règles fixes | 0,5 |
| 2 | Deux apports appliqués aux anomalies de l'annexe 2.1 | 0,5 |
| 3 | Trois limites appuyées sur la démonstration (faux positifs, explicabilité, qualité des données d'apprentissage ; faux négatifs ou dépendance acceptés) | 0,5 |
| 4 | Conditions de la supervision humaine (qui décide, seuils, traçabilité, revue des performances) | 0,5 |

**Réponse indicative**

La détection d'anomalies par apprentissage automatique consiste à faire apprendre à un modèle, à partir de l'historique (ici les factures, les fiches fournisseurs et les paiements de 2024 à 2026), ce qu'est une opération habituelle, puis à attribuer à chaque opération nouvelle un **score** qui mesure son écart à ce comportement ; au-delà d'un **seuil**, une alerte est émise. L'apprentissage peut être non supervisé (repérer ce qui s'écarte de la norme) ou supervisé (apprendre à partir de cas déjà qualifiés de fraude ou de doublon). À la différence d'un contrôle par règles fixes (« bloquer deux factures de même numéro »), le modèle repère des combinaisons inhabituelles qu'aucune règle n'a prévues ; il produit une probabilité, non une décision (0,5 pt).

Deux apports parmi (0,5 pt) :
- **l'exhaustivité** : le module examine toutes les opérations, environ 90 000 factures et près de 29 000 virements par an, quand le directeur administratif et financier valide des campagnes de 1 200 virements sans les détailler ;
- **la prévention avant le paiement** : lors de la démonstration, le module a signalé le changement de coordonnées bancaires frauduleux d'octobre, qui a coûté 250 000 €, et 150 des 220 doublons ; utilisé avant chaque campagne, il aurait permis de suspendre ces paiements ;
- **la détection de schémas combinés** : coordonnées modifiées récemment, montant inhabituel, demande pressante, bénéficiaire nouveau, que des règles simples ne croisent pas ;
- **la libération de temps** : les comptables concentrent leurs contrôles sur les opérations les plus risquées.

Trois limites parmi (0,5 pt) :
- **les faux positifs** : 6 000 alertes sur l'année, soit 500 par mois et près de 28 par comptable fournisseurs, pour 151 anomalies réelles (le changement de coordonnées frauduleux et 150 doublons), soit à peine 2,5 % des alertes, les 5 849 autres s'étant révélées sans fondement ; au-delà, la lassitude conduit à ignorer les alertes, y compris les vraies ;
- **l'explicabilité** : le module « ne fournit pas de justification détaillée de chaque score » ; or il faudra justifier la suspension d'un paiement auprès d'un fournisseur et documenter les contrôles auprès des auditeurs externes ;
- **la qualité des données d'apprentissage** : l'historique n'a pas été nettoyé ; les doublons non corrigés et les fournisseurs créés deux fois risquent d'être appris comme « normaux » (biais), ce que confirme la détection de 150 doublons seulement sur 220 ;
- **les faux négatifs** : 70 doublons non signalés ; le module ne remplace pas les contrôles bloquants d'unicité ni la séparation des tâches de la question 2.1 ;
- **la dépendance** : seuils réglés par LUMIGRÈS et règles apprises sur les données d'ALTIVERNE restant sa propriété (clauses 3 et 7).

Conditions de la supervision humaine (0,5 pt) :
- l'IA alerte, une personne décide : toute suspension ou libération d'un paiement signalé est décidée par une cellule de contrôle distincte des comptables qui préparent les virements, jamais automatiquement ;
- les seuils sont fixés et révisés par la direction financière d'ALTIVERNE, non par l'ESN, pour ramener les alertes à un volume traitable ;
- chaque alerte et la décision prise sont journalisées ; les alertes qualifiées (vraie anomalie ou fausse alerte) sont réinjectées pour améliorer le modèle ;
- une revue trimestrielle des performances (alertes confirmées, anomalies découvertes après coup) est présentée au directeur administratif et financier ; les utilisateurs sont formés à l'interprétation des scores.

Indicateur possible de cette supervision (valorisé, non exigé) : précision des alertes = alertes confirmées comme anomalies / alertes examinées ; source : journal des alertes et des décisions ; fréquence mensuelle ; cible : au moins 20 % à fin 2027, contre environ 2,5 % lors de la démonstration ; axe processus.

**Réponses tolérées**
- Présentation du module comme apprentissage supervisé ou non supervisé, si le principe du score et du seuil est exact.
- Apports formulés en termes de rapidité de détection ou de couverture des trois familles d'anomalies, s'ils sont appliqués au cas.
- Mention des biais ou de la protection des données personnelles des fournisseurs entrepreneurs individuels comme limite, si elle est reliée au cas.

**Erreurs fréquentes**
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — le module « rédige » ou « converse » ; juste : modèle qui classe et attribue un score à partir de données structurées.
- *Apports sans limites* (`ET-19`) — l'IA « supprime la fraude » ; juste : gains réels, mais faux positifs, explicabilité, qualité des données et supervision humaine.
- *IA décrite comme un outil technique* (`JUR-T12`) — architecture interne du modèle, choix d'un algorithme ; juste : effets sur le métier de la comptabilité fournisseurs et sur le contrôle interne.
- *Hors sujet réglementaire* (`JUR-T07`) — qualification du module au regard du règlement sur l'intelligence artificielle : non demandée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Apprentissage automatique et IA générative ; détection de fraude ; risques (biais, explicabilité, dépendance) ; gouvernance et supervision humaine | principe, apports et limites | F13 § 1 à 4 | guide p. 336 et 354-355 |

---

### 2.4 – Sécurisation du contrat avec l'ESN (3 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.a` « Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques » ; `1.4.b` « Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle » ; `1.4.c` « Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD » ; `1.4.d` « Méthodologie de négociation contractuelle et analyse des risques » ; `1.4.e` « Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) ».

**Annexes mobilisées** : annexes 2.1 (échéance du 01/09/2027, données financières) et 2.2 (offre, module, clauses, témoignage de la DSI).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Contrat au forfait caractérisé (livrables définis, prix et délai fixés, engagement de résultat, risque porté par le prestataire), et contradiction relevée avec les clauses 2 à 5 | 0,5 |
| a-2 | Trois clauses à renégocier ou à ajouter, chacune justifiée par le cas et assortie d'une formulation de principe (0,5 par clause) | 1,5 |
| b-1 | Instance de pilotage adaptée (composition, fréquence, objet) | 0,5 |
| b-2 | Indicateur de suivi complet (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse indicative**

*2.4 a) – Caractérisation du contrat et clauses à renégocier*

Le contrat proposé est un **contrat d'intégration au forfait** : l'ESN s'engage à livrer des résultats définis (raccordement à la plateforme, interface, module) pour un prix (900 000 €) et une date fixés à l'avance ; c'est en principe un engagement de résultat, et le risque de dépassement pèse sur le prestataire. Il s'y ajoute un abonnement au module (100 000 € par an) et une maintenance corrective (60 000 € par an), soit environ 1,38 M€ sur trois ans. Or les clauses 2 à 5 vident le forfait de sa substance : simples « meilleurs efforts » sur la date, aucun résultat garanti pour le module, recette tacite et pénalités symboliques ; le risque revient à ALTIVERNE (0,5 pt).

Trois clauses parmi les suivantes (1,5 pt, 0,5 par clause justifiée et reformulée) :

| Clause | Pourquoi la renégocier ou l'ajouter | Formulation de principe |
|---|---|---|
| 2 et 5 – Délais et pénalités | le 1er septembre 2027 est une échéance réglementaire et opérationnelle : les 4 800 PME fournisseurs émettront par la plateforme et les 18 comptables ne pourront plus ressaisir ; « meilleurs efforts » et une pénalité plafonnée à 9 000 €, soit 1 % du prix ou six semaines de retard, ne protègent pas | date ferme de mise en service, avec jalons intermédiaires (réception automatique, émission, interface) et essais de bout en bout avant l'été ; obligations d'ALTIVERNE (disponibilités, données) listées précisément ; pénalités proportionnées au préjudice et plafond relevé, par exemple 10 % du prix |
| 4 – Recette | une recette réputée acquise en dix jours et une mise en production qui « vaut recette » interdisent de vérifier l'interface sur des données réelles, alors que les fichiers d'interface actuels sont déjà une source d'erreurs | cahier de recette validé par ALTIVERNE, essais sur des données réelles d'un mois complet, procès-verbal signé par la direction financière et la DSI, réserves bloquantes et non bloquantes, période de vérification de bon fonctionnement couvrant une clôture mensuelle |
| 3 – Résultats du module d'IA | sans objectif mesurable ni maîtrise des seuils, ALTIVERNE paie 250 000 € et 100 000 € par an pour 500 alertes par mois sans garantie | objectifs mesurés à l'issue d'une période d'apprentissage sur un jeu d'essai (part des doublons et des changements de coordonnées frauduleux détectés, nombre maximal d'alertes par mois), seuils fixés par ALTIVERNE, motifs principaux de chaque alerte restitués, nettoyage préalable de l'historique inclus au périmètre |
| 7 – Propriété des développements et des paramétrages | les interfaces sont spécifiques à ALTIVERNE et les règles apprises le sont sur ses propres données : laissées à LUMIGRÈS, elles empêchent de changer de prestataire | développements spécifiques cédés à ALTIVERNE (ou licence permanente), paramétrages, seuils et documentation appartenant à ALTIVERNE, code source accessible (dépôt chez un tiers) |
| 8 – Accès aux données (et clause de sécurité à ajouter) | factures, coordonnées bancaires et paiements sont des données confidentielles, dont certaines à caractère personnel (fournisseurs entrepreneurs individuels) ; réutilisation pour d'autres clients et hébergement de localisation inconnue | interdiction de toute réutilisation ; accord de sous-traitance des données personnelles (instructions, sécurité, sous-traitants ultérieurs autorisés, sort des données en fin de contrat) ; hébergement dans l'Union européenne ; engagements de sécurité et notification des incidents ; clause d'audit |
| 10 – Durée et sortie (réversibilité à ajouter) | tacite reconduction, prix révisable par la seule ESN et restitution dans un format propriétaire, sans assistance : dépendance totale | plan de réversibilité : restitution des données, des paramétrages et de l'historique des alertes dans un format ouvert et documenté, assistance au transfert vers un autre prestataire, délais et coût fixés ; révision de prix encadrée ; préavis de non-reconduction |
| 1 – Périmètre (formation à ajouter) | la formation des comptables et des agences est exclue alors que le métier change (question 2.2) ; la reprise des données antérieures à 2024 n'est pas prévue | formation et accompagnement inclus ; option chiffrée pour les filiales ; procédure de demande de changement avec chiffrage préalable |

Les clauses 6 (maintenance corrective) et 9 (comité mensuel) sont acceptables, la seconde à compléter (question b).

*2.4 b) – Pilotage de la relation*

Instance (0,5 pt) : un **comité de pilotage** mensuel, hebdomadaire jusqu'au 1er septembre 2027, réunissant le chef de projet de LUMIGRÈS, la DSI et la direction financière (M. MARSANGE ou Mme FRESSINAUD), car les résultats attendus sont d'abord métier : avancement des jalons, recette, anomalies, alertes du module, risques ; complété par un **comité stratégique** trimestriel (directeur général, direction de LUMIGRÈS) qui arbitre les avenants et la reconduction. Côté ALTIVERNE, un responsable du contrat contrôle le reporting de l'ESN avec ses propres outils.

Indicateur (0,5 pt), un parmi :

| Axe | Indicateur | Formule | Source | Fréquence | Cible |
|---|---|---|---|---|---|
| Processus | Respect des jalons | jalons livrés et recettés à la date prévue / jalons prévus à cette date | planning contractuel et procès-verbaux de recette | mensuelle | 100 % des jalons nécessaires au 1er septembre 2027 |
| Processus | Délai de correction des anomalies bloquantes | anomalies bloquantes corrigées en deux jours ouvrés au plus / anomalies bloquantes signalées | outil de suivi des anomalies d'ALTIVERNE | mensuelle | 100 % (engagement de la clause 6) |

**Réponses tolérées**
- Choix d'autres clauses de l'annexe 2.2 ou de clauses absentes (audit, sécurité, sous-traitance des données personnelles, réversibilité), dès lors qu'elles sont justifiées par le cas et reformulées.
- Qualification de l'abonnement au module comme un service en ligne (SaaS) distinct du forfait.
- Proposition d'un lotissement du contrat ou d'une consultation d'un second intégrateur, si elle tient compte du délai rappelé par la DSI.

**Erreurs fréquentes**
- *Forfait et régie confondus* (`ET-31`) — « le forfait est payé au temps passé » ; juste : prix et livrables fixés, engagement de résultat ; la régie met à disposition des compétences pilotées par le client.
- *Analyse juridique approfondie* (programme 1.4, exclusions) — qualification du contrat, régime de la responsabilité, décisions de justice ; juste : enjeux opérationnels et principes de sécurisation.
- *Données laissées au prestataire, réversibilité oubliée* (F04, piège 4 ; `JUR-A05`) ; juste : données, paramétrages et règles apprises propriété du client, restitution en format ouvert.
- *Pénalités sans mesure* (F04, piège 3) — pénalités sans niveaux mesurables ; juste : jalons et niveaux mesurés, pénalités proportionnées.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des contrats, clauses critiques, gouvernance de la relation | forfait, recette, pénalités, propriété, réversibilité, comités | F04 § 1, 3 à 6 | guide p. 235-236, 255-256 |
| RGPD, règlement (UE) 2016/679 | sous-traitance des données personnelles (art. 28) | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 2.5 – Blockchain et crypto-actifs : trois propositions (3 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.a` « Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations » ; `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.d` « Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ».

**Annexes mobilisées** : annexes 1.1 (chiffre d'affaires, clients) et 2.3 (propositions et repères au 31/12/2026).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Blockchain définie (registre distribué, blocs chaînés par empreintes, consensus, horodatage, inaltérabilité pratique, confiance entre acteurs) | 0,5 |
| a-2 | Rattachement des trois propositions à la typologie | 0,5 |
| b-1 | Proposition (a) : opportunités, risques, cadre | 0,5 |
| b-2 | Proposition (b) : opportunités, risques, cadre (prestataire non agréé, MiCA) | 0,5 |
| b-3 | Proposition (c) : opportunités, risques, cadre (NFT et champ de MiCA) | 0,5 |
| b-4 | Recommandations justifiées et hiérarchisées pour les trois propositions | 0,5 |

**Réponse indicative**

*2.5 a) – Définition et typologie*

La blockchain est un registre distribué, partagé et synchronisé entre plusieurs nœuds, dont les transactions sont regroupées en blocs chaînés par des empreintes cryptographiques et validées par un mécanisme de consensus ; elle permet à des acteurs qui ne se font pas mutuellement confiance de partager une information horodatée et pratiquement inaltérable, sans administrateur central. Elle se distingue d'une base de données distribuée, que son administrateur peut modifier. Les blockchains publiques sont ouvertes à tous ; les blockchains permissionnées réservent la validation à des participants identifiés (0,5 pt).

Rattachement (0,5 pt) :
- (a) rapports de visite : **certification** (preuve d'existence et d'intégrité d'un document à une date, par ancrage de son empreinte) ;
- (b) paiements en jeton de monnaie électronique : applications **financières** des crypto-actifs, de la famille de la **finance décentralisée**, ici avec un intermédiaire qui conserve et convertit les jetons ;
- (c) certificat d'appareil et fidélité : **NFT**, avec une dimension de **traçabilité** de l'historique de l'appareil.

*2.5 b) – Évaluation et recommandations*

| Proposition | Opportunités | Risques et limites | Cadre (annexe 2.3) |
|---|---|---|---|
| (a) Rapports de visite certifiés (0,5 pt) | preuve que le rapport n'a pas été modifié depuis sa date, vérifiable par le client sans faire confiance au groupe : répond directement aux deux contestations de 2026 ; coût modeste (40 000 € par an, de l'ordre de 0,1 € par rapport pour environ 400 000 rapports) ; argument commercial auprès des bailleurs | l'ancrage prouve l'intégrité du document, pas la réalité de la visite ni l'exactitude de son contenu (problème de l'« oracle ») : la saisie du rapport doit rester contrôlée ; le rapport cite le technicien : seule l'empreinte, et jamais le rapport, doit être inscrite dans un registre inaltérable ; dépendance au prestataire d'ancrage ; consommation d'énergie selon le mécanisme de consensus de la blockchain choisie | aucun crypto-actif émis ni offert : MiCA ne s'applique pas ; risque RGPD (minimisation, effacement) fortement réduit si seule l'empreinte, jamais le rapport, est inscrite ; alternative de l'horodatage électronique d'un service de confiance (eIDAS 2) ; ISO 22739:2024 fixe seulement le vocabulaire |
| (b) Paiements en jeton stable (0,5 pt) | faible : un seul client, 1,2 M€ de chiffre d'affaires, 0,2 % du chiffre d'affaires du groupe ; règlement international plus rapide | le prestataire, ancien PSAN dont l'agrément MiCA est en cours d'instruction, ne peut plus fournir en France de services sur crypto-actifs depuis le 02/07/2026 : recourir à lui exposerait ALTIVERNE à un prestataire en situation irrégulière ; risque de perte ou de vol des jetons conservés (clés), risque de contrepartie, vigilance sur l'origine des fonds d'un client établi hors de l'Union ; commission de 1 % (environ 12 000 € par an) ; rapprochements bancaires plus complexes, à rebours de la fiabilisation | ALTIVERNE n'émettrait pas de jeton et ne fournirait pas de service sur crypto-actifs : elle n'a pas à être agréée ; en revanche, la conservation pour son compte et l'échange contre des euros sont des services sur crypto-actifs réservés aux PSCA agréés ; le jeton de monnaie électronique doit être émis par un établissement de crédit ou de monnaie électronique ; la facture reste établie en euros ; l'opération, internationale, relève du e-reporting par la plateforme (annexe 2.1) |
| (c) Certificat et fidélité en NFT (0,5 pt) | différenciation des appareils modernisés ; certificat unique et transférable au nouveau propriétaire ou syndic | les clients n'ont pas de portefeuille de crypto-actifs : usage improbable ; ALTIVERNE serait seule à écrire l'historique, qui doit être mis à jour à chaque intervention : une blockchain n'apporte rien qu'une base centralisée tenue par le groupe n'assure déjà ; image d'objets spéculatifs auprès de bailleurs sociaux et d'établissements de santé ; coût de 60 000 € la première année ; énergie | les NFT réellement uniques sont exclus du champ de MiCA ; des NFT « de collection » émis en série et échangeables risquent de ne pas être regardés comme uniques et de relever alors de MiCA (offre au public de crypto-actifs) |

Recommandations hiérarchisées (0,5 pt) :
1. **Proposition (a) : expérimenter**, sur le parc des deux bailleurs qui ont contesté des rapports, l'ancrage de la seule empreinte des rapports, en le comparant à un horodatage électronique fourni par un service de confiance au sens d'eIDAS 2 ; décision de généralisation sur la base du coût, de l'usage par les clients et de la valeur de preuve.
2. **Proposition (c) : abandonner** les NFT de collection ; remplacer le certificat NFT par un certificat numérique de l'appareil remis dans l'espace client, dont l'empreinte peut être ancrée comme en (a).
3. **Proposition (b) : refuser** en l'état ; proposer au client un virement international en euros ; ne réexaminer qu'avec un PSCA agréé et une conversion immédiate en euros, si la demande devient significative.

Lorsqu'un registre distribué entre dans un processus financier, les auditeurs légaux en prennent connaissance comme de tout système d'information (NEP), sans norme propre à la blockchain : le projet (a), qui ne touche pas les comptes, n'en relève pas.

**Réponses tolérées**
- Proposition (a) rattachée à la traçabilité, ou (c) à la certification, si l'usage est justifié.
- Proposition (b) rattachée aux crypto-actifs et aux jetons stables plutôt qu'à la finance décentralisée, avec la remarque qu'un intermédiaire agréé est requis.
- Recommandation de lancer (a) directement ou de lui préférer l'horodatage d'un service de confiance, si le choix est argumenté par la preuve, le coût et la protection des données.
- Évaluation des trois propositions présentée dans un tableau compact (opportunités, risques, cadre), si chaque case s'appuie sur l'annexe 2.3.
- Grille d'opportunité (plusieurs acteurs qui écrivent, absence de tiers de confiance, besoin d'inaltérabilité, données partageables, volume, coût et énergie) appliquée aux trois propositions.

**Erreurs fréquentes**
- *Blockchain confondue avec une base de données distribuée* (`ET-08`) ; juste : registre partagé entre acteurs sans confiance mutuelle, synchronisé par consensus.
- *MiCA invoqué pour la tenue des comptes ou l'impôt, NFT soumis sans réserve à MiCA* (`ET-35`) ; juste : MiCA encadre l'offre au public, les jetons stables et les prestataires ; les NFT réellement uniques en sont exclus.
- *Régime français antérieur à MiCA présenté comme en vigueur* (F11, piège 2) ; juste : depuis le 02/07/2026, seuls les PSCA agréés au titre de MiCA peuvent exercer.
- *Inaltérabilité confondue avec la vérité de la donnée* (F11, piège 3) ; juste : le registre garantit l'intégrité de ce qui y est inscrit, pas son exactitude.
- *Opportunités sans risques ni énergie* (`ET-19`) ; juste : apports, limites, coûts et consommation d'énergie mis en regard.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2023/1114 (MiCA) | offre au public, jetons stables, PSCA, exclusion des NFT uniques, fin de la période transitoire des anciens PSAN le 01/07/2026 | `mica` ; F11 § 3 ; fiche commune § 3 | applicable depuis le 30/12/2024 (jetons stables depuis le 30/06/2024) |
| Règlement (UE) 2024/1183 (eIDAS 2) | services de confiance : horodatage | `eidas2` ; F11 § 3.4 | en vigueur |
| RGPD, règlement (UE) 2016/679 | minimisation, effacement face à l'inaltérabilité | `rgpd` ; F11 § 2.3 | applicable depuis le 25/05/2018 |
| ISO 22739:2024 | vocabulaire des registres distribués | `iso_22739_2024` ; F11 § 3.4 | en vigueur [S] |
| NEP | aucune norme propre à la blockchain | `nep_315` ; F11 § 3.4 | en vigueur |
| Usages, grille d'opportunité, limites | certification, NFT, oracle, énergie | F11 § 1 et 2 | guide p. 268-269 |
