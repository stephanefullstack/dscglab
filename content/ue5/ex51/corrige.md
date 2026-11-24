# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 51 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 audit et fiabilisation, F12 sécurité et résilience, F14 numérique responsable, F15 RGPD opérationnel, fiche commune CSRD, ESRS et VSME, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les risques et la fiabilisation de la facturation | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels | 3,5 |
| 3.2 La gestion des badges et des comptes | `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 3,5 |
| 3.3 L'audit de l'attribution des emplacements du carreau | `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 2 |
| 3.4 Les données de durabilité, l'affichage dynamique et la gouvernance responsable du système d'information | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.b` Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) ; `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété | 4 |
| **Dossier 3 – Fiabiliser la facturation, maîtriser les accès, auditer le carreau et répondre aux demandes de données de durabilité** |  | **13** |

Répartition indicative : connaissances (typologie des risques, fiabilisation, gestion des identités et des accès, audit d'un processus, état de durabilité, sobriété numérique) environ 3 points (items 3.1 a-1, 3.1 b-1, 3.2 a-1, 3.3 a-1, 3.4 a-1 et 3.4 b-1, chacun en partie appliqué au cas) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – Les risques et la fiabilisation de la facturation (3,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels ». Limites : la conformité financière et comptable n'est pas traitée en UE 5 ; aucune règle de facturation, aucun traitement comptable des avoirs ni aucune incidence chiffrée sur les comptes n'est attendu.

**Annexes mobilisées** : annexe 3.1 (chaîne de facturation, constats, échéance de septembre 2027, échelles), annexe 3.5 (facturation électronique) et annexe 1.1 (240 entreprises installées, chiffre d'affaires de 28 M€ dont 17 M€ de redevances et de loyers et 5 M€ de refacturations, logiciel de gestion du marché, portail, progiciel comptable).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée (cybermenaces et malveillance, y compris interne ; défaillances opérationnelles ; risques réglementaires ; risques métiers), avec les critères touchés (intégrité, traçabilité, disponibilité, confidentialité) | 0,5 |
| a-2 | Quatre risques formulés comme des événements redoutés, tirés de l'annexe 3.1 avec leur cause et leurs chiffres, et classés de façon justifiée | 0,5 |
| b-1 | Fiabilisation définie (exhaustivité, exactitude, réalité, traçabilité des données comptables et décisionnelles ; contrôles applicatifs et généraux, séparation des tâches, piste d'audit, rapprochements) | 0,5 |
| b-2 | Cinq points de contrôle de la chaîne, du contrat au chiffre d'affaires, chacun avec le risque traité, le contrôle, sa nature et son responsable | 0,5 |
| b-3 | Parmi eux, le rapprochement de l'occupation constatée et des contrats facturés, et un contrôle de l'interface ou du chiffre d'affaires (rejets corrigés à la source, écart de 900 k€ expliqué) | 0,5 |
| c-1 | Quatre risques cotés selon les échelles de l'annexe 3.1 D, de façon justifiée | 0,5 |
| c-2 | Deux actions prioritaires avant le 01/09/2027, justifiées par la probabilité et l'impact et reliées aux risques forts | 0,5 |

**Réponse attendue**

*3.1 a) – La typologie et les quatre risques*

**Typologie** (a-1) : les risques liés aux systèmes d'information se classent en quatre familles (F12 § 0 et § 5) :
- les **cybermenaces et actes malveillants**, externes ou internes : hameçonnage, compromission de comptes, fraude interne ;
- les **défaillances opérationnelles**, non intentionnelles : erreur de saisie, interface défaillante, procédure absente, panne ;
- les **risques réglementaires** : manquement à une obligation, ici l'émission des factures sous forme électronique à compter du 01/09/2027 (annexe 3.5) ;
- les **risques métiers** : effets sur l'activité et la stratégie, ici le chiffre d'affaires, la relation avec les entreprises installées et la confiance des actionnaires.

Chaque risque porte atteinte à un ou plusieurs critères : intégrité (exactitude et exhaustivité des données), traçabilité, disponibilité, confidentialité. Pour une chaîne de facturation, l'**intégrité** et la **traçabilité** sont les critères dominants.

**Risques de la chaîne de facturation** (a-2 ; quatre sont attendus, six sont proposés) :

| Risque (événement redouté) et cause | Famille | Critère touché |
|---|---|---|
| R1 – Une entreprise occupe une case ou une cellule sans contrat à jour, et elle n'est pas facturée ou l'est mal : les changements arrivent par téléphone ou par courriel, sans procédure ni rapprochement (15 cases ou cellules en février 2027, sur 60 changements en 2026 ; 150 k€ par an) | défaillance opérationnelle (processus) ; effet métier : perte de revenus, inégalité entre entreprises | intégrité (exhaustivité) |
| R2 – Des tarifs erronés sont facturés après la révision annuelle : saisie à la main, contrat par contrat, sans contrôle (20 contrats en janvier 2027) | défaillance opérationnelle (erreur humaine) ; effet métier : réclamations de l'Union des grossistes | intégrité (exactitude) |
| R3 – Un avoir injustifié, par erreur ou par fraude, annule une facture sans que personne le voie : les mêmes agents créent factures et avoirs, sans validation ni motif ; 18 personnes ont tous les droits ; aucune trace des modifications (300 avoirs, 400 k€ en 2026) | acte malveillant interne rendu possible par une défaillance du contrôle interne (séparation des tâches) ; effet métier : perte | intégrité, traçabilité |
| R4 – Le chiffre d'affaires présenté aux actionnaires est inexact et impossible à justifier : les lignes rejetées sont corrigées ou supprimées dans le seul progiciel comptable, sans liste ; aucun rapprochement entre les deux applications (480 lignes, 2 % ; écart de 900 k€, environ 4 % de 22 000 k€) | défaillance opérationnelle (intégrité de l'interface) ; risque métier : confiance des actionnaires, compte rendu trimestriel du plan | intégrité, traçabilité |
| R5 – À partir du 01/09/2027, des factures électroniques erronées partent en série vers les entreprises et la plateforme agréée : identifiant absent ou faux pour 30 entreprises (12,5 %), contrats non à jour, tarifs erronés ; « une facture fausse sera transmise telle quelle » | risque réglementaire (obligation d'émission électronique) ; effet métier : réclamations, avoirs en chaîne | intégrité |
| R6 – Des entreprises sont relancées à tort et contestent : relances préparées sur une extraction, sans rapprochement des avoirs et des paiements (25 entreprises en 2026) | défaillance opérationnelle ; effet métier : relation avec les entreprises installées | intégrité |

*3.1 b) – La fiabilisation et la cartographie des contrôles*

**Définition** (b-1) : **fiabiliser un système d'information comptable et décisionnel**, c'est garantir que les données qui vont de l'événement de gestion (ici, l'occupation d'un emplacement) jusqu'au chiffre présenté aux décideurs sont **exhaustives, exactes, réelles et traçables**. Le dispositif combine les **contrôles applicatifs** (à la saisie, au traitement, aux interfaces, en sortie), les **contrôles généraux** (gestion des accès et des modifications, exploitation), la **séparation des tâches** incompatibles (saisir, valider, annuler) et une **piste d'audit** qui permet de reconstituer le chemin d'un chiffre jusqu'à sa source, avec des **rapprochements** réguliers entre applications (F10 § 2 et § 3). Chez BRÉVALIM, la chaîne va du contrat d'emplacement au chiffre d'affaires du compte rendu trimestriel aux actionnaires ; elle se rompt aujourd'hui à chaque maillon.

**Cartographie des contrôles** (b-2 et b-3 ; cinq points de contrôle sont attendus, sept sont proposés) :

| Point de contrôle | Risque traité | Contrôle | Nature | Responsable |
|---|---|---|---|---|
| 1. Création ou modification d'un contrat (changement de case) | R1, R3 | toute modification passe par une demande écrite, enregistrée, validée par la responsable commerciale avant saisie ; journal des modifications des contrats (auteur, date, valeur avant et après) demandé à l'éditeur ; droits de modification limités au service commercial | préventif, manuel et automatisé | service commercial (Mme QUÉRINEL) |
| 2. **Rapprochement de l'occupation constatée et des contrats facturés** | R1 | chaque trimestre, relevé des cases, bureaux et cellules effectivement occupés (placiers, agents de sûreté, direction technique pour les cellules), rapproché de la liste des contrats facturés ; chaque écart régularisé dans le mois | détectif, manuel | service commercial avec la direction de l'exploitation ; revue par le directeur administratif et financier |
| 3. Révision annuelle des tarifs | R2 | tarifs saisis une fois dans une grille, appliqués par le logiciel à tous les contrats ; à défaut, état « avant / après » de chaque contrat contrôlé par une seconde personne avant l'émission de janvier, avec un contrôle de vraisemblance (hausse égale au taux de révision) | préventif, automatisé ; détectif, manuel | facturation, validé par la direction administrative et financière |
| 4. Avoirs | R3, R6 | motif obligatoire ; validation par une personne distincte de l'émetteur (comptable, puis directeur administratif et financier au-delà d'un montant) ; état mensuel des avoirs par auteur et par entreprise revu par le directeur administratif et financier | préventif et détectif | M. MORVÉLAN |
| 5. Fichier mensuel des écritures vers le progiciel comptable | R4 | totaux de contrôle (nombre de lignes, montant) comparés avant et après chargement ; liste des rejets conservée ; correction **dans le logiciel de gestion du marché**, puis nouvel envoi ; aucune correction directe en comptabilité | détectif, automatisé et manuel | comptabilité |
| 6. Chiffre d'affaires présenté aux actionnaires | R4 | rapprochement mensuel, rubrique par rubrique, du chiffre d'affaires du logiciel et de celui de la comptabilité ; écart expliqué et documenté avant chaque compte rendu trimestriel ; source et date du chiffre indiquées | détectif, manuel | directeur administratif et financier |
| 7. Données des entreprises et relances | R5, R6 | identifiant de l'entreprise vérifié à la création et après tout rachat ou changement de nom ; relances préparées après rapprochement des paiements et des avoirs | préventif ; détectif | service commercial ; comptabilité |

Ces contrôles supposent des **droits séparés** dans le logiciel : le service commercial gère les contrats, la facturation émet, un tiers valide les avoirs, personne n'a tous les droits (lien avec la question 3.2).

*3.1 c) – La cotation et les deux actions prioritaires*

**Cotation selon les échelles de l'annexe 3.1 D** (c-1) :

| Risque | Probabilité | Impact | Priorité |
|---|---|---|---|
| R3 – Avoir injustifié | **forte** : 300 avoirs par an, chaque mois, sans validation ; facile à provoquer | **fort** : 400 k€ d'avoirs émis en 2026 sans validation ni motif ; la part injustifiée est inconnue, et une perte de plus de 200 k€ ne peut pas être exclue | **oui** |
| R4 – Chiffre d'affaires inexact | **forte** : des rejets chaque mois, cause toujours là | **fort** : écart de 900 k€ ; chiffre d'affaires présenté aux actionnaires inexact | **oui** |
| R5 – Factures électroniques erronées en série | **forte** : quasi certaine dès le 01/09/2027 si rien ne change : 30 identifiants faux ou absents aujourd'hui, contrats et tarifs non fiables | **fort** : factures électroniques erronées en série, chaque mois, aux 240 entreprises | **oui** |
| R1 – Occupation sans contrat à jour | forte : 15 occupations sans contrat à jour en février 2027, pour 60 changements demandés en 2026 ; aucune procédure | moyen : 150 k€ par an | non, mais il alimente R5 |
| R2 – Tarifs erronés | moyenne : une fois par an, 20 contrats | moyen : réclamations | non |
| R6 – Relances à tort | moyenne | moyen : réclamations | non |

**Deux actions à mener avant le 01/09/2027** (c-2) :
1. **Fiabiliser les données de base avant la première facture électronique** (R5, et R1 et R2 qui l'alimentent) : corriger les identifiants des 30 entreprises ; rapprocher les 240 contrats de l'occupation réelle, par un relevé contradictoire avec les placiers et les entreprises ; vérifier les tarifs 2027 ; mettre en place la procédure écrite des changements d'emplacement (points 1, 2 et 7). C'est la seule priorité qui a une **date** : à partir de septembre, chaque erreur de données partira chaque mois, telle quelle, vers les 240 entreprises et la plateforme. La plateforme transmet les données, elle ne les corrige pas.
2. **Mettre sous contrôle les avoirs et le passage vers la comptabilité** (R3 et R4, probabilité et impact forts) : validation des avoirs par une personne distincte, avec motif ; correction des rejets à la source ; rapprochement mensuel du chiffre d'affaires (points 4, 5 et 6). Puisqu'une facture fausse sera transmise telle quelle (annexe 3.1 C), chaque erreur devra être corrigée après coup : un circuit d'avoirs sans contrôle deviendrait la principale faiblesse de la chaîne.

Ces deux actions précèdent l'outil : la version du logiciel livrée en juin ne fiabilise rien si les données et les droits restent en l'état.

**Réponses tolérées**
- Autre typologie (risques internes et externes, accidentels et intentionnels, ou par critère d'intégrité, de traçabilité, de disponibilité), si les quatre familles du programme apparaissent dans le classement ; R3 classé en défaillance du contrôle interne plutôt qu'en malveillance, si la possibilité de fraude est signalée.
- R1 coté fort en impact, au titre de l'inégalité entre entreprises installées et de son effet sur R5, et retenu dans une action prioritaire, si c'est justifié.
- R3 coté moyen en impact, si le candidat relève que la part injustifiée des 400 k€ est inconnue ; les deux actions prioritaires portent alors sur R4 et R5, et la validation des avoirs peut figurer dans l'action sur le passage vers la comptabilité.
- Deuxième action différente si elle traite un risque fort : traçabilité des modifications des contrats et des tarifs exigée de l'éditeur dans la version de juin ; séparation des droits dans le logiciel.
- Contrôles regroupés autrement (par étape : contrat, facture, écritures, encaissement, chiffre présenté), si le rapprochement de l'occupation et des contrats y figure et si chaque contrôle porte sa nature et son responsable.

**Erreurs fréquentes**
- *Typologie récitée sans application, ou risques réduits aux constats* (`JUR-T01`, `JUR-T07`) — juste : des événements redoutés, avec leur cause et leurs chiffres, classés puis cotés selon les échelles de l'annexe.
- *Facturation électronique présentée comme la solution aux erreurs* (`JUR-T03`) — juste : elle transmet des données structurées ; des données fausses deviennent des factures électroniques fausses.
- *Contrôles sans responsable ni nature, ou limités à « contrôler les factures »* (`JUR-T11`) — juste : un contrôle par maillon de la chaîne, du contrat au chiffre d'affaires, avec la séparation des tâches.
- *Plateforme agréée appelée de son ancien nom, ou calendrier ancien de la réforme* (`JUR-N02`) — juste : plateforme agréée ; émission par BRÉVALIM à compter du 01/09/2027 (annexe 3.5).
- *Règles de facturation, mentions obligatoires, TVA, traitement comptable des avoirs, catégorie d'entreprise à déterminer* — non attendus (UE 1 et UE 4 ; date donnée par l'annexe).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI, critères | cybermenaces, défaillances, risques réglementaires et métiers | F12 § 0, § 1 et § 5 | notion de cours |
| Fiabilisation, contrôles applicatifs et généraux, séparation des tâches, piste d'audit | du contrat au chiffre d'affaires | F10 § 2 et § 3 | notion de cours |
| Généralisation de la facturation électronique | réception depuis le 01/09/2026 ; émission par BRÉVALIM à compter du 01/09/2027 ; formats structurés | `facturation_electronique_fr` ; F10 § 3.4 | en vigueur ; émission par BRÉVALIM à compter du 01/09/2027 (annexe 3.5) |
| Plateformes agréées | transmission des factures | `facturation_electronique_pa` ; F10 § 3.4 | en vigueur |

---

### 3.2 – La gestion des badges et des comptes (3,5 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique des solutions de cybersécurité n'est pas exigée ; la sécurité est envisagée de façon systémique (organisationnelle, humaine) ; les normes se mobilisent sans entrer dans leur démarche de conformité formelle.

**Annexes mobilisées** : annexe 3.2 (badges par population, zones, comptes, incidents, points de vue), annexe 3.5 (ISO/IEC 27001:2022 et 27002:2022, RGPD en principe) et annexe 1.1 (organigramme, effectif, entreprises installées, badges et portail).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gestion des identités et des accès définie (cycle de vie, une identité par personne, moindre privilège, revue, traçabilité), pour les accès physiques et logiques | 0,5 |
| a-2 | Cycle de vie (arrivée, changement, départ) des salariés de BRÉVALIM et des saisonniers, à partir d'une source qui fait foi, avec une date de fin | 0,5 |
| a-3 | Cycle de vie des salariés des entreprises installées et des prestataires (référent, déclaration simple, expiration), réponse à l'objection de Mme GARBUSSAC ; traitement immédiat des quelque 500 badges de personnes parties | 0,5 |
| a-4 | Moindre privilège appliqué aux zones (cellules, locaux techniques) et aux comptes ; réponse à l'objection de Mme DUCHÉRAN | 0,5 |
| a-5 | Revue périodique des droits (fréquence, acteurs) et fin des comptes partagés du portail et des comptes génériques des tablettes | 0,5 |
| b-1 | Rôles de la direction générale, du responsable de la sûreté, du responsable des systèmes d'information et des directions métiers, distingués | 0,5 |
| b-2 | Rôles des entreprises installées et des prestataires (référent, signalement des départs, revue, usage) | 0,5 |

**Réponse attendue**

*3.2 a) – Le dispositif de gestion des badges et des comptes*

**Définition** (a-1) : la **gestion des identités et des accès** (IAM) organise, pour chaque personne, la **création** de son identité et de ses droits à l'arrivée, leur **modification** quand elle change de fonction et leur **révocation** à son départ. Elle repose sur quelques principes : une identité par personne (badges et comptes **nominatifs**), le **moindre privilège** (droits limités au besoin de la fonction, par profils), la **séparation des tâches**, la **revue périodique** des droits et la **traçabilité** des accès (F12 § 3). Elle distingue l'identification (déclarer qui l'on est), l'authentification (le prouver) et l'autorisation (les droits accordés). Ses mesures figurent parmi celles de l'annexe A d'ISO/IEC 27001:2022 (gestion des identités, contrôle d'accès, sécurité physique des locaux), détaillées par ISO/IEC 27002:2022 (annexe 3.5). Chez BRÉVALIM, elle doit couvrir **ensemble** les accès physiques (badges) et logiques (comptes), car ce sont les mêmes personnes et les mêmes départs non signalés : environ 500 badges sur 2 600, près d'un sur cinq, appartiennent à des personnes parties.

**Le cycle de vie des identités, par population** (a-2 et a-3) :

| Population | Arrivée | Changement | Départ |
|---|---|---|---|
| Salariés de BRÉVALIM (230 badges, 20 de personnes parties) | l'entrée dans la paie, déclarée par les ressources humaines, déclenche le badge et les comptes du profil du poste, prêts le premier jour | le manager demande le nouveau profil ; les anciens droits sont retirés le jour du changement | la sortie déclarée par les ressources humaines désactive badge et comptes le dernier jour ; le badge est rendu |
| Saisonniers d'été (80 badges, tous de personnes parties) | liste de la direction de l'exploitation ; badge et compte nominatifs **datés** du premier au dernier jour du contrat | changement de mission validé par la chef des placiers | **expiration automatique** à la fin du contrat : plus aucun badge actif en octobre |
| Salariés des entreprises installées (2 150 badges, environ 350 de personnes parties) | demande du **référent des accès** désigné par chaque entreprise, sur le portail plutôt que sur papier ; badge lié à l'entreprise et à ses zones, valable un an au plus | le référent modifie les zones (nouvelle cellule, autre pavillon) | le référent déclare le départ sur le portail sous 48 heures ; à défaut, un badge non utilisé pendant deux mois est suspendu, et chaque badge expire s'il n'est pas reconfirmé lors de la revue |
| Prestataires de nettoyage et de maintenance du froid (140 badges, environ 50 de personnes parties) | liste nominative des intervenants transmise par le prestataire et validée par la direction qui a commandé la prestation ; badge limité aux zones et aux plages de l'intervention, jusqu'à la fin du contrat | toute nouvelle zone est validée par la direction technique | le prestataire signale chaque départ ; les **10 badges sans nom sont supprimés** |

**Réponse à Mme GARBUSSAC** : il ne s'agit pas d'un formulaire à chaque départ, mais d'une déclaration en quelques clics sur le portail par un référent, complétée par l'expiration automatique et la suspension des badges inutilisés : le dispositif tient même si une entreprise oublie de déclarer. La rotation d'un salarié sur trois rend ce dispositif plus nécessaire, non moins.

**Mesure immédiate** : désactiver les 80 badges des saisonniers et les 20 des anciens salariés de BRÉVALIM, puis demander à chaque entreprise et à chaque prestataire de confirmer sa liste dans le mois, faute de quoi les badges non confirmés sont suspendus. Cinq des 12 vols de 2026 ont été commis avec le badge d'une personne partie.

**Le moindre privilège** (a-4) : chaque personne n'accède qu'aux zones et aux applications dont sa fonction a besoin, aux heures où elle en a besoin.

| Zone ou application | Accès proposé |
|---|---|
| Pavillons | salariés des entreprises installées dans le pavillon, agents de BRÉVALIM et prestataires concernés, aux heures d'activité ; hors de ces heures, sûreté et agents de nuit |
| Entrepôt frigorifique (quais, couloirs) | entreprises locataires de cellules, agents de nuit, techniciens et prestataire de maintenance du froid |
| Chacune des 40 cellules | les seuls salariés de l'entreprise locataire ; droit d'intervention nominatif des agents de nuit et des techniciens du froid, tracé et revu |
| Locaux techniques (salle des machines du froid, locaux électriques) | direction technique, prestataire de maintenance pendant ses interventions, agents de sûreté |
| Portail des entreprises installées | un compte par personne, avec un profil : factures pour le dirigeant et le comptable, demandes techniques pour les salariés concernés |
| Logiciel de gestion du marché | profils séparés : contrats, facturation, validation des avoirs, attribution du carreau (lien avec la question 3.1) |

**Réponse à Mme DUCHÉRAN** : le moindre privilège n'empêche pas d'intervenir, il réserve l'intervention à ceux qui en ont la fonction. Les agents de nuit et les techniciens du froid gardent l'ouverture des cellules, avec leur badge nominatif. Chaque ouverture d'une cellule par une personne qui n'en est pas locataire est relue le matin par la sûreté, et un badge de secours reste sous la garde du poste de sûreté. Aujourd'hui, 2 600 badges ouvrent les 40 cellules ; demain, quelques dizaines, en plus des locataires. Le saisonnier trouvé dans la salle des machines n'y aurait pas eu accès.

**La revue périodique et la fin des comptes partagés et génériques** (a-5) :
- **Revue des droits** chaque semestre, avant l'été et à l'automne, pour les badges et les comptes : chaque direction métier, chaque référent d'entreprise et chaque prestataire reçoit la liste de ses personnes et de leurs droits, confirme ou retire, et ce qui n'est pas confirmé est suspendu. La revue est trimestrielle pour les droits étendus (validation des avoirs, administration des applications). Le rapprochement avec la liste de la paie est mensuel. La première revue a lieu avant la saison d'été 2027.
- **Fin des comptes partagés du portail** : un compte nominatif par personne, créé et retiré par le référent de l'entreprise, au lieu d'un identifiant commun connu même d'anciens salariés. L'incident de novembre 2026 (factures d'un grossiste consultées par un concurrent) en est la conséquence directe.
- **Fin des comptes génériques des tablettes** : un compte nominatif par placier et par saisonnier, avec une connexion rapide adaptée au travail de nuit (badge ou code personnel) ; le mot de passe écrit au dos des tablettes est changé tout de suite. Sans cela, aucune attribution du carreau n'est imputable à une personne (question 3.3).
- **Journaux** : relus par sondage chaque semaine et après chaque incident ; ce sont des données personnelles, à conserver pendant une durée limitée et à n'ouvrir qu'aux personnes habilitées, sur avis de la déléguée à la protection des données (annexe 3.5).

*3.2 b) – Les rôles et les responsabilités*

| Acteur | Rôle et responsabilités dans le dispositif |
|---|---|
| **Direction générale** (Mme VAUCLERC ; vous, directeur(rice) général(e) délégué(e)) | approuve la politique des accès (zones, populations, règles d'arrivée et de départ, revue) ; désigne les responsables ; arbitre les conflits entre sûreté et exploitation ; donne les moyens ; reçoit le bilan de chaque revue et rend compte de l'objectif de sûreté du plan |
| **Responsable de la sûreté** (M. MARCHEVIEL) | gère les badges : création, zones et horaires, désactivation ; contrôle sur le terrain (badges prêtés) ; relit les journaux de passage ; organise la revue des badges et en présente le bilan |
| **Responsable des systèmes d'information** (M. LAVEYRAC) | gère les comptes des applications, y compris l'administration des comptes du portail reprise à l'éditeur ; définit les profils types avec les métiers ; relie badges et comptes à une même source (ressources humaines, référentiel des entreprises) ; organise la revue des comptes ; n'accorde pas seul un droit qu'aucun métier n'a validé |
| **Directions métiers** (exploitation, technique, commercial, administrative et financière avec les ressources humaines) | propriétaires des droits de leur domaine : définissent les accès nécessaires à chaque fonction et valident demandes et revues ; les ressources humaines déclarent les arrivées et les départs ; l'exploitation, les placiers et les saisonniers ; la direction technique, les prestataires et les locaux techniques ; le service commercial, les référents des entreprises et le portail ; la direction administrative et financière, la séparation des tâches de la facturation |
| **Déléguée à la protection des données** (Mme TALMONDIER) | conseille sur la minimisation des données des badges et des journaux, leur durée de conservation et l'information des personnes |
| **Entreprises installées** | désignent un référent des accès ; demandent les badges et les comptes de leurs salariés ; déclarent chaque départ sous 48 heures ; répondent à la revue ; répondent de l'usage des badges par leurs salariés (aucun prêt), par un engagement écrit à la remise des badges |
| **Prestataires** | transmettent la liste nominative de leurs intervenants et signalent chaque départ ; n'utilisent que des badges nominatifs, dans les zones et aux heures de leur intervention ; répondent à la revue semestrielle de leur liste |

Chaque utilisateur, enfin, ne prête pas son badge et signale sa perte.

**Réponses tolérées**
- Cycle de vie présenté par étape (arrivée, changement, départ) plutôt que par population, si les quatre populations y figurent avec leur source et leur date de fin.
- Revue annuelle pour les badges des entreprises installées, alignée sur le contrat annuel d'emplacement, si elle est complétée par la suspension des badges inutilisés.
- Authentification à deux facteurs proposée pour les comptes du portail qui donnent accès aux factures, si elle ne remplace pas les comptes nominatifs.
- Désignation d'un référent sécurité ou rôle du comité de direction ajouté au tableau, s'il ne se substitue pas aux propriétaires métiers des droits.

**Erreurs fréquentes**
- *Réponse limitée aux badges ou aux comptes* (`JUR-S05`) — juste : un même dispositif pour les accès physiques et logiques, qui partagent les mêmes personnes et les mêmes départs non signalés.
- *Identification, authentification et autorisation confondues ; mot de passe complexe présenté comme une authentification forte* (`ET-28`) — juste : comptes nominatifs, preuve de l'identité, droits limités au besoin.
- *Moindre privilège appliqué au point d'empêcher l'exploitation, ou rejeté au nom de l'exploitation* (`JUR-T03`) — juste : droits nominatifs d'intervention, tracés et relus.
- *Responsable des systèmes d'information seul propriétaire des droits* (`JUR-T03`) — juste : les métiers décident des droits, la sûreté et les systèmes d'information les mettent en œuvre, la direction générale arbitre.
- *Réglage des équipements de contrôle d'accès, mesures techniques détaillées, analyse juridique des données des badges* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gestion des identités et des accès, moindre privilège, revue | cycle de vie, profils, traçabilité | F12 § 3 ; F10 § 3.1 | notion de cours |
| ISO/IEC 27001:2022 | norme d'exigences ; mesures de l'annexe A : gestion des identités, contrôle d'accès, sécurité physique | `iso_27001_2022` ; F12 § 2 | en vigueur |
| ISO/IEC 27002:2022 | guide de mise en œuvre des mesures | `iso_27002_2022` ; F12 § 2 | en vigueur |
| Rôles dans la sécurité | direction, métiers, prestataires, déléguée à la protection des données | F12 § 1 ; F15 § 1 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | minimisation, conservation limitée et sécurité des journaux, en principe | `rgpd` ; F15 § 2 | applicable depuis le 25/05/2018 |

---

### 3.3 – L'audit de l'attribution des emplacements du carreau (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : aucun test technique détaillé ; aucune analyse juridique, ni règle de non-discrimination ou de concurrence.

**Annexes mobilisées** : annexe 3.3 (règles écrites, journal, écarts de l'été 2026, plaintes, demande du conseil d'administration), annexe 3.2 (comptes génériques des tablettes, saisonniers), annexe 3.5 (RGPD en principe) et annexe 1.1 (300 emplacements, 180 producteurs par nuit l'été, placiers sur tablette, activité de nuit).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit d'un processus du SI défini ; objectifs et périmètre de la mission tirés de l'annexe 3.3 | 0,5 |
| a-2 | Étapes réparties sur les quatre semaines (fériés, conclusions au conseil du 31 mai) avec leurs livrables ; quatre preuves à demander, dont l'extraction du journal des modifications avant son effacement | 0,5 |
| b-1 | Trois critères (équité, traçabilité, fiabilité des données) : ce qui est attendu et ce que l'annexe laisse craindre, avec ses chiffres | 0,5 |
| b-2 | Deux facteurs de succès et deux points de vigilance propres à cet audit (nuit, placiers, données incomplètes, calendrier) | 0,5 |

**Réponse attendue**

*3.3 a) – Le cadrage de l'audit*

**Définition** (a-1) : l'**audit d'un processus du système d'information** est un examen indépendant et méthodique qui compare le fonctionnement réel d'un processus appuyé sur le système d'information (règles, pratiques, données, accès, traces) à un **référentiel** et à des **critères**, relève les écarts, en apprécie les risques et formule des recommandations hiérarchisées (F10 § 1.1 et § 1.2). Ici, c'est un **audit externe contractuel** demandé par le conseil d'administration. Son référentiel est le règlement du carreau de 2018, avec les règles internes d'accès aux tablettes. Ce n'est ni un audit légal des comptes, ni une enquête disciplinaire sur les placiers.

**Objectifs** (trois sont attendus, quatre sont proposés) :
- vérifier que les attributions de l'été 2026 respectent l'ordre de priorité écrit : abonnés, puis ancienneté, puis ordre d'arrivée ;
- apprécier la **fiabilité** des données enregistrées par rapport à l'occupation réelle ;
- apprécier la **traçabilité** des attributions et des modifications, et les contrôles existants ;
- recommander des règles et des contrôles applicables dès la saison d'été 2027, qui commence le 1er juin, et donner au conseil une réponse étayée aux 35 plaintes.

**Périmètre** :
- le processus d'attribution, de l'arrivée du producteur au péage à l'occupation constatée de l'emplacement ;
- la saison d'été 2026, de juin à septembre, et deux nuits observées en mai 2027 ;
- les données : journal des attributions et des modifications, liste des abonnés, ancienneté des producteurs, heures d'arrivée au péage, relevés des agents de sûreté, feuilles papier ;
- les acteurs : chef des placiers, 12 placiers, saisonniers, agents de sûreté, service commercial pour les abonnements, service des systèmes d'information.

Sont exclus : l'opportunité des règles elles-mêmes, que le conseil a fixées (l'audit peut toutefois signaler une règle ambiguë) ; la facturation des emplacements ; toute analyse juridique.

**Étapes, calendrier et livrables** (a-2 ; 18 jours ouvrés) :

| Semaine | Étape | Livrable |
|---|---|---|
| 1 (3-7 mai ; jeudi 6 mai férié) | **cadrage** : lettre de mission signée par la directrice générale sur mandat du conseil (objectifs, périmètre, référentiel, critères, accès garantis aux données et aux nuits du carreau, confidentialité, interlocuteurs) ; réunion de lancement avec Mme TRÉMOULAC et les placiers ; **extraction et conservation d'une copie du journal de l'été 2026** par le service des systèmes d'information | lettre de mission, liste des preuves demandées |
| 2 (10-14 mai) | **prise de connaissance** : entretiens avec la chef des placiers, plusieurs placiers, des agents de sûreté, le service commercial et le responsable des systèmes d'information ; **observation de deux nuits** sur le carreau, de minuit à 5 heures ; **cartographie du processus** d'attribution (étapes, données, contrôles) ; analyse des risques ; programme de travail | cartographie du processus, programme de travail |
| 3 (18-21 mai ; lundi 17 mai férié) | **examen** : reconstitution de l'ordre de priorité sur un échantillon de nuits ; analyse des modifications faites après 3 heures (emplacements, bénéficiaires, comptes) ; rapprochement des attributions et des relevés de 5 heures ; examen des feuilles papier et des ressaisies | dossier de travail |
| 4 (24-28 mai) | **constats** (constat, cause, risque, recommandation, priorité, responsable, échéance), **validation contradictoire** avec Mme TRÉMOULAC et la direction générale ; **rapport et note de synthèse**, avec les mesures applicables au 1er juin | rapport, note de synthèse, plan d'action |

Les conclusions sont présentées au conseil du lundi 31 mai ; le suivi du plan d'action revient à la direction de l'exploitation.

**Preuves à demander** (a-2 ; quatre sont attendues, huit sont proposées) :
- l'**extraction intégrale du journal des attributions et de leurs modifications** de l'été 2026 (date, heure, compte, emplacement, producteur), à faire dès la première semaine : les nuits de juin 2026 seront effacées à partir de juillet 2027 ;
- le règlement du carreau de 2018 et les consignes écrites ou orales données aux placiers ;
- la liste des abonnés de la saison 2026 et la liste d'ancienneté des producteurs ;
- les heures d'arrivée des producteurs au péage ;
- les relevés de 5 heures des agents de sûreté des 10 nuits d'août et la comparaison faite par Mme TRÉMOULAC (270 écarts) ;
- les feuilles papier conservées des six nuits sans tablettes et leurs ressaisies ;
- la liste des comptes des tablettes, de leurs utilisateurs et les plannings des placiers ;
- les 35 plaintes de 2026 et les réponses qui leur ont été faites.

*3.3 b) – Les trois critères, les facteurs de succès et les points de vigilance*

**Trois critères d'appréciation** (b-1) :

| Critère | Ce qui est attendu | Ce que l'annexe 3.3 laisse craindre |
|---|---|---|
| **Équité** | chaque emplacement est attribué selon l'ordre écrit, le même pour tous ; l'emplacement d'un abonné absent à 3 heures est réellement remis en attribution ; les dérogations sont rares, motivées et contrôlées | 30 des 40 emplacements de l'entrée occupés plus de huit nuits sur dix par les mêmes 25 producteurs, dont 10 ne sont ni abonnés ni parmi les plus anciens ; 40 % des modifications faites après 3 heures, sans motif ; emplacements « pris » qui restent vides jusqu'à 4 heures ; 35 plaintes |
| **Traçabilité** | chaque attribution et chaque modification est imputable à une personne, horodatée, motivée, et conservée assez longtemps pour être contrôlée | deux comptes génériques, utilisés aussi par les saisonniers, mot de passe au dos des tablettes : impossible de savoir qui a modifié ; aucun motif ; conservation de treize mois ; feuilles papier en partie perdues |
| **Fiabilité des données** | les données enregistrées reflètent l'occupation réelle : exactes, complètes, à jour | 270 occupations sur 1 800, soit 15 %, ne correspondent pas à l'attribution enregistrée ; six nuits ressaisies le lendemain ; toute statistique tirée du logiciel sur le carreau est donc douteuse |

**Deux facteurs de succès** (b-2 ; deux parmi les suivants) :
- un **mandat clair du conseil** et un **sponsor** à la direction générale, qui garantissent à l'auditeur l'accès aux données, aux personnes et au carreau la nuit, et l'**indépendance** de ses conclusions ;
- l'**adhésion des placiers** : l'audit porte sur le processus et ses contrôles, non sur les personnes ; Mme TRÉMOULAC est associée dès le lancement, les entretiens restent confidentiels et les constats sont validés contradictoirement ;
- des **compétences doubles** : l'exploitation d'un journal de données et la connaissance du fonctionnement réel du carreau ;
- la **conservation immédiate des preuves**, avant l'effacement du journal.

**Deux points de vigilance** (b-2 ; deux parmi les suivants) :
- le **travail de nuit** : les attributions se font de minuit à 5 heures, quand le service des systèmes d'information est absent ; l'auditeur doit planifier des nuits d'observation et disposer d'un interlocuteur de nuit ;
- les **données incomplètes** : avec des comptes génériques et des feuilles perdues, aucune modification ne peut être imputée à un placier ; l'audit doit le dire comme une limite et ne pas conclure à une faute individuelle ;
- la **relation avec les placiers**, qui vivront l'audit « comme une accusation », et la pression des producteurs : confidentialité, ton factuel, restitution d'abord aux audités ;
- le **calendrier** : 18 jours ouvrés, conclusions au conseil du 31 mai, saison le lendemain ; les recommandations doivent être hiérarchisées et applicables tout de suite ;
- les **données personnelles** des placiers et des producteurs dans le journal : accès limité aux besoins de la mission (annexe 3.5).

**Réponses tolérées**
- Démarche en cinq ou six étapes (cadrage, prise de connaissance, analyse des risques, examen, constats, restitution, suivi), si elle tient dans les quatre semaines et aboutit au conseil du 31 mai.
- Critère d'efficacité (temps d'attribution, attente des producteurs) ou de sécurité des accès aux tablettes en complément des trois critères, s'il est appliqué au cas.
- Facteurs de succès ou points de vigilance différents s'ils sont propres à cet audit (par exemple la neutralité de l'auditeur vis-à-vis des producteurs qui se plaignent).

**Erreurs fréquentes**
- *Méthodologie incomplète* (`JUR-A01`) — juste : objectifs, périmètre, référentiel, étapes, livrables, calendrier et preuves.
- *Audit du SI confondu avec l'audit légal ou avec une enquête disciplinaire* (`ET-34`) — juste : audit contractuel d'un processus, commandé par le conseil, qui conclut sur le processus et ses contrôles.
- *Facteurs de succès génériques* (`JUR-T01`, `JUR-T08`) — juste : nuit, placiers, données incomplètes, calendrier de la saison.
- *Conclusion sur des personnes à partir de comptes génériques* (`JUR-T03`) — juste : l'imputabilité manque ; c'est un constat en soi.
- *Analyse juridique de l'égalité d'accès ou de la concurrence entre producteurs ; tests techniques sur les tablettes* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Démarche d'audit du SI, livrables | cadrage, prise de connaissance, risques, examen, constats, restitution, suivi | F10 § 1.1 et § 1.2 | notion de cours |
| Critères d'audit, facteurs de succès | équité, traçabilité, fiabilité ; indépendance, adhésion, accès aux données | F10 § 0 et § 1 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | données personnelles du journal, accès limité, en principe | `rgpd` ; F15 § 2 | applicable depuis le 25/05/2018 |

---

### 3.4 – Les données de durabilité, l'affichage dynamique et la gouvernance responsable du système d'information (4 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.b` « Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) » ; `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété ». Limites : la durabilité est intégrée à la gouvernance globale du SI ; aucun calcul d'empreinte, aucun assujettissement à déterminer, aucune exigence détaillée des ESRS.

**Annexes mobilisées** : annexe 3.4 (demandes de trois entreprises installées, sources des données, erreurs, projet d'affichage, absence de règle), annexe 3.5 (CSRD, ESRS révisées, norme volontaire VSME) et annexe 1.1 (40 cellules, refacturation de l'énergie, de l'eau et du froid de 5 M€, supervision du froid, pont-bascule, portail, application des acheteurs, horaires du marché).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | État de durabilité selon les ESRS rappelé (double matérialité, chaîne de valeur, information fiable et justifiable) ; raisons des demandes : BRÉVALIM détient seule les mesures de consommations et de déchets des entreprises ; enjeu commercial pour BRÉVALIM | 0,5 |
| a-2 | Rôle du SI dans la collecte, la traçabilité et la fiabilité, appliqué aux trois sources (logiciel de gestion, supervision du froid, pont-bascule) et aux erreurs de 2026 | 0,5 |
| a-3 | Trois mesures justifiées | 0,5 |
| b-1 | Sobriété numérique définie et distinguée de l'efficacité (Green IT) et de l'économie d'énergie | 0,5 |
| b-2 | Projet apprécié : besoin, durée d'allumage (48 heures d'activité sur 168), définition des vidéos, rafraîchissement, réemploi des 20 écrans | 0,5 |
| b-3 | Trois mesures de sobriété justifiées | 0,5 |
| c-1 | Instance (composition, rôle) et trois critères de durabilité dans les décisions sur les projets | 0,5 |
| c-2 | Un indicateur complet (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.4 a) – Les demandes de données de durabilité et le rôle du système d'information*

**L'état de durabilité** (a-1) : une entreprise dans le champ de la CSRD publie un **état de durabilité** établi selon les normes ESRS (annexe 3.5 ; fiche commune). Il repose sur la **double matérialité** : les impacts de l'entreprise sur l'environnement et les personnes, et les effets des enjeux de durabilité sur l'entreprise. Il couvre ses propres activités et sa **chaîne de valeur**. Ses informations doivent être **fiables, traçables et justifiables** : ce n'est pas un simple rapport rédigé à partir d'estimations.

**Pourquoi les entreprises installées s'adressent à BRÉVALIM** :
- l'électricité, l'eau et le froid consommés dans leurs cellules et leurs cases, et les déchets qu'elles produisent sur le site, font partie de leurs propres consommations et de leurs impacts ; or **seule BRÉVALIM les mesure**, avec ses compteurs, la supervision du froid et le pont-bascule ;
- BRÉVALIM est dans leur **chaîne de valeur** : elle leur loue les emplacements, leur fournit l'énergie, l'eau et le froid, et collecte leurs déchets ;
- BRÉVALIM n'établit pas d'état de durabilité et n'a aucun assujettissement à déterminer : elle répond à une **demande de ses clients**. L'enjeu est commercial (M. PERRAGUÈS : « ils iront chercher ailleurs des cellules mieux suivies ») et de réputation. Il est aussi de coût, puisque les trois demandes prennent déjà 15 jours par an et que deux autres sont annoncées pour 2028.

**Le rôle du système d'information** (a-2) :
- **collecte** : les données existent déjà dans trois applications (logiciel de gestion du marché pour l'électricité et l'eau, supervision du froid, pont-bascule). Le système d'information doit les extraire automatiquement et les rattacher à chaque entreprise par un **référentiel des points de mesure** (compteur, cellule, benne) lié aux contrats d'emplacement, au lieu de relevés à l'écran et de tris à la main ;
- **traçabilité** : pour chaque donnée envoyée, il faut savoir d'où elle vient, sur quelle période, avec quelle unité et quelle méthode. Les déchets, mesurés par pavillon et répartis selon la surface, sont une **estimation** et doivent être présentés comme tels. Ce qui a été envoyé doit être conservé, avec ses corrections ; aujourd'hui, rien ne l'est ;
- **fiabilité** : des contrôles automatiques évitent les erreurs de 2026. Une période complète, sans mois compté deux fois, aurait évité le double mois de décembre ; un rattachement exact des cellules aux contrats, le froid de la cellule voisine ; une variation anormale expliquée, la hausse de moitié des déchets. Un rapprochement avec la **refacturation** donne la règle : un chiffre envoyé doit être le chiffre facturé.

**Trois mesures** (a-3) :
1. **Un référentiel unique des points de mesure**, tenu par la direction technique avec le service commercial : chaque compteur, chaque cellule de la supervision du froid et chaque benne ou pavillon est rattaché à une entreprise et à son contrat, et mis à jour à chaque changement d'emplacement (lien avec la question 3.1).
2. **Une extraction contrôlée et documentée**, produite chaque année avant la fin de janvier, puis chaque trimestre : contrôles de complétude, de doublon, de cohérence avec la refacturation et de variation ; une fiche de méthode par donnée ; les estimations signalées ; la mise à disposition **sur le portail**, dans l'espace de chaque entreprise, qui ne voit que ses propres données, avec l'historique des versions. Le tableur envoyé par courriel disparaît.
3. **Un responsable et un format communs** : le directeur technique est désigné propriétaire de ces données. Le même modèle de réponse sert à toutes les entreprises qui en font la demande (cinq en 2028), au besoin en s'appuyant sur la norme volontaire VSME pour structurer les informations (annexe 3.5). Pour les déchets, la mesure par entreprise est améliorée là où c'est possible ; ailleurs, la méthode d'estimation est indiquée avec le chiffre.

*3.4 b) – La sobriété numérique et le projet d'affichage dynamique*

**Définition** (b-1) : la **sobriété numérique** consiste à **interroger d'abord le besoin** (faut-il ce service, pour qui, à quelle échelle, avec quelle qualité ?) avant de chercher à le rendre plus efficace. Elle limite les équipements, les données et l'énergie au juste nécessaire. Elle se distingue du **Green IT**, qui réduit l'empreinte du système d'information à besoin donné, et ne se réduit pas à une économie d'énergie : pour des équipements électroniques, la **fabrication** pèse souvent davantage que la consommation (F14 § 1 et § 3).

**Appréciation du projet** (b-2) :
- **Le besoin** n'est pas démontré : les cours du jour ne changent que deux fois par nuit, et les horaires, le plan et les informations figurent déjà dans l'application des acheteurs. La publicité des grossistes est un objectif commercial, non un besoin d'information. Quelques écrans aux points de passage (péage, entrées des pavillons) peuvent suffire ; 60 écrans neufs ne se justifient pas.
- **La durée d'allumage** : jour et nuit, soit 168 heures par semaine, pour 48 heures d'activité (8 heures, six nuits sur sept) ; les écrans brillent sans public plus des deux tiers du temps.
- **La définition des vidéos** : de la haute définition en boucle pour des cours et des consignes qui sont du texte ; elle accroît les données transférées et stockées, la charge du serveur et la consommation des écrans.
- **La fréquence de rafraîchissement** : toutes les minutes, soit 1 440 fois par jour, pour deux mises à jour par nuit.
- **Le réemploi** : 20 écrans de 2022 qui fonctionnent seraient mis au rebut, et 60 écrans neufs fabriqués. C'est l'impact probablement le plus lourd du projet, et l'inverse de l'allongement de la durée de vie.

Le projet est donc **surdimensionné** au regard du besoin. Il ne faut pas forcément l'abandonner, mais le redimensionner. L'argument « la publicité les paiera » ne dit rien de son empreinte.

**Trois mesures de sobriété** (b-3 ; quatre sont proposées) :
1. **Réemployer** les 20 écrans existants et n'acheter que le complément justifié par des points de lecture réels, en privilégiant des écrans reconditionnés ou réparables, garantis longtemps, avec la reprise des équipements en fin de vie.
2. **N'allumer les écrans que pendant l'activité** (de l'arrivée des premiers acheteurs à la fin du marché, six jours sur sept), avec une extinction automatique ou une mise en veille le reste du temps.
3. **Des contenus sobres** : texte et images fixes pour les cours et les consignes, rafraîchis à chaque mise à jour des cours plutôt que toutes les minutes ; pas de vidéo en haute définition en boucle, au plus des séquences courtes et légères pour la publicité.
4. **Partir du besoin** : publier les cours du jour dans l'application des acheteurs, déjà installée, et réserver les écrans aux lieux où le téléphone ne suffit pas.

*3.4 c) – Une gouvernance du système d'information orientée vers la responsabilité sociétale*

**L'instance** (c-1) : un **comité du numérique responsable**, présidé par vous, directeur(rice) général(e) délégué(e) chargé(e) du système d'information. Il réunit :
- le responsable des systèmes d'information ;
- le directeur technique, pour l'énergie, les déchets et les données de durabilité ;
- le service de la communication et la direction administrative et financière, pour les achats ;
- la déléguée à la protection des données, pour l'éthique et les données personnelles ;
- un représentant de l'Union des grossistes, au nom des entreprises installées.

Il se réunit deux fois par an et **avant toute décision** sur un projet ou un achat d'équipement du système d'information. Il fixe les règles (durée de vie des équipements, critères d'achat), suit les demandes de données de durabilité et rend compte à la direction générale. La durabilité entre ainsi dans les décisions au lieu d'être examinée après coup : aujourd'hui, le projet d'affichage n'a été vu que par la communication et son fournisseur.

**Trois critères de durabilité dans les décisions sur les projets** (c-1) :
1. **Le besoin et le dimensionnement** : besoin démontré, alternatives avec l'existant (application, équipements en place), juste dimensionnement des équipements, des données et des durées de fonctionnement.
2. **Le cycle de vie des équipements** : réemploi de l'existant, durée de vie et réparabilité, reprise et fin de vie des équipements remplacés.
3. **La capacité à produire des données de durabilité fiables et l'éthique des données** : le projet mesure ce qu'il consomme et permet de répondre aux entreprises installées ; il limite les données personnelles et protège les données des entreprises.

**Un indicateur de suivi** (c-2) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Part des projets et des achats du système d'information examinés selon les critères de durabilité avant décision** | nombre de projets et d'achats d'équipements du SI examinés par le comité du numérique responsable avant la décision / nombre total de projets et d'achats d'équipements du SI décidés sur la période × 100 | registre des avis du comité ; bons de commande enregistrés dans le progiciel comptable | semestrielle | 100 % dès le second semestre 2027, contre 0 % aujourd'hui, aucune règle n'existant (annexe 3.4 C) | gouvernance |

**Réponses tolérées**
- Raison des demandes exprimée par les seules notions du cours (fournisseur de la chaîne de valeur, données d'activité nécessaires aux informations environnementales des groupes), si l'idée que BRÉVALIM détient seule les mesures est présente.
- Mesures différentes en a) si elles traitent la collecte, la traçabilité et la fiabilité : contrôle de cohérence avec la refacturation, archivage des envois, compteurs ou pesées par entreprise.
- Mesures de sobriété classées dans un autre ordre, ou quatrième mesure à la place de l'une des trois, si chacune répond à un défaut relevé.
- Instance intégrée à une instance de pilotage du système d'information existante ou à créer, si la durabilité y a un ordre du jour, des critères et un responsable.
- Autre indicateur complet et relié au cas : part des demandes de données de durabilité servies dans le délai sans correction (cible 100 % en 2028) ; heures d'allumage des écrans hors activité (cible zéro) ; part des équipements réemployés lors d'un renouvellement.

**Erreurs fréquentes**
- *Sobriété confondue avec l'économie d'énergie, ou réduite à la mise en veille* (`ET-12`) — juste : interroger le besoin et le nombre d'écrans d'abord, puis l'allumage et les contenus.
- *Empreinte du projet limitée à l'électricité* (`ET-38`) — juste : la fabrication de 60 écrans neufs et la mise au rebut de 20 écrans en état de marche pèsent au moins autant.
- *État de durabilité réduit à un rapport, ou rôle du SI ignoré* (`ET-17`) — juste : collecte automatisée, traçabilité des méthodes et des envois, contrôles de fiabilité.
- *Assujettissement de BRÉVALIM calculé, exigences détaillées des ESRS citées* — non attendus : BRÉVALIM répond à la demande de ses clients ; seule l'architecture des normes est mobilisée.
- *Indicateur incomplet ou générique, durabilité traitée comme un ajout marginal* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe ; critères appliqués avant la décision, dans la gouvernance du SI.
- *Calcul d'empreinte tenté* — non attendu.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Directive (UE) 2022/2464 (CSRD), modifiée en 2025 et en 2026 | état de durabilité, chaîne de valeur, en principe | `csrd` ; F14 § 2 ; fiche commune | en vigueur |
| Règlement délégué (UE) 2026/1563 (ESRS révisées) | double matérialité, architecture des normes | `esrs_2026` ; fiche commune | applicable aux exercices ouverts à compter du 01/01/2027 |
| Règlement délégué (UE) 2026/1560 (norme volontaire VSME) | réponse structurée d'une entreprise hors du champ | `vsme` ; fiche commune | en vigueur |
| Sobriété, Green IT, durée de vie, fabrication | définitions, leviers | F14 § 1 et § 3 | notion de cours |
| Gouvernance du SI orientée vers la responsabilité sociétale | comité du numérique responsable, critères, indicateur | F14 § 0 et § 8 | notion de cours |
