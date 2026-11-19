# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 36 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 audit du SI, F11 blockchain et crypto-actifs, F12 sécurité et résilience, F13 intelligence artificielle, F14 numérique responsable, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 L'audit du processus de reversement aux vendeurs | `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. | 2 |
| 3.2 Le projet de séquestre programmable et de règlement en jetons | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT (ici, le contrat intelligent) ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ; `3.3.a` Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations ; `3.3.d` Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO | 2,5 |
| 3.3 La fraude et l'apport de l'intelligence artificielle | `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.f` Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques ; `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA | 3 |
| 3.4 L'architecture de confiance et la surveillance du site | `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) (ici, la gestion des identités et des accès, la journalisation, la supervision et les sauvegardes) | 3 |
| 3.5 La mesure et la réduction de l'impact environnemental du site | `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements | 2,5 |
| **Dossier 3 – Sécuriser les transactions et mesurer l'impact environnemental du numérique** |  | **13** |

Répartition indicative : connaissances (audit d'un processus, chaîne de blocs et contrat intelligent, typologie des risques, apprentissage automatique et IA générative, architecture de confiance, écoconception) 3 points (items 3.1 a-1, 3.2 a-1, 3.3 a-1 et b-1, 3.4 a-1, 3.5 b-1) ; analyse des annexes et recommandations 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – L'audit du processus de reversement aux vendeurs (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la conformité financière et comptable n'est pas traitée par l'UE 5.

**Annexes mobilisées** : annexe 3.1 (règles du dépôt-vente, processus actuel, constats de 2026, demande de la présidente) et annexe 1.1 (dépôt-vente, système d'information, organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit d'un processus du SI défini (examen indépendant et méthodique, au regard d'un référentiel, débouchant sur des recommandations) ; limite d'indépendance relevée ; étapes et livrables tenant d'avril à fin juillet 2027, équipe (vous et la responsable financière) | 0,5 |
| a-2 | Tableau de trois étapes du processus (acteur, application, risque, contrôle interne attendu ; trois étapes suffisent) ; deux tests documentaires, chacun relié à un constat chiffré | 0,5 |
| b-1 | Deux critères (par exemple fiabilité et sécurité) : ce qui est attendu et appréciation chiffrée de la situation | 0,5 |
| b-2 | Deux autres critères (par exemple conformité et efficacité ou efficience) : ce qui est attendu et appréciation chiffrée | 0,5 |

**Réponse attendue**

*3.1 a) – La démarche de l'audit*

L'**audit d'un processus du système d'information** est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel (ici le contrat de dépôt-vente et les règles internes d'ORSALIE, complétés par les principes du contrôle interne et par le RGPD pour les données des vendeurs), la manière dont un processus et les applications qui le supportent atteignent leurs objectifs de fiabilité, de sécurité, de conformité et d'efficacité ; il débouche sur des constats et des recommandations hiérarchisées (F10 § 1). L'audit **évalue** les contrôles internes, il ne s'y substitue pas.

| Élément | Contenu pour ORSALIE |
|---|---|
| Mandant et objectif | la présidente ; savoir si le processus de reversement est fiable et maîtrisé, et à quelles conditions il peut être repris pour la place de marché de 2028 |
| Périmètre | le processus de la livraison au virement (site, statut du prestataire logistique, logiciel des dépôts, tableur, portail bancaire, progiciel comptable), la gestion des coordonnées bancaires par le service clients, le signalement des retours ; année 2026 et premier trimestre 2027 ; hors périmètre : les rachats, la place de marché elle-même |
| Équipe et indépendance | vous-même et la responsable financière, à la demande de la présidente ; indépendance **limitée**, car vous supervisez les finances et la responsable financière valide les virements de plus de 20 000 € : le signaler dans la lettre de mission, faire mener les tests sur les virements qu'elle a validés par une personne extérieure au processus (par exemple une juriste des fonctions support) et présenter les conclusions directement à la présidente ; la comptable chargée du processus est auditée et fournit les extractions |
| Étapes | avril : cadrage (lettre de mission, référentiel, calendrier) ; avril-mai : prise de connaissance (entretiens avec la comptable, le service clients, M. LAMBRESCOT pour les applications) et cartographie du processus et de ses risques ; mai-juin : tests ; début juillet : constats partagés de façon contradictoire ; fin juillet : rapport et plan d'action présentés à la présidente ; puis suivi avant l'ouverture de la place de marché |
| Livrables | lettre de mission ; cartographie du processus et des risques ; programme de travail ; fiches de constats (constat, cause, risque, recommandation, priorité, responsable, échéance) ; rapport ; exigences pour le processus de la place de marché |

**Étapes du processus, risques et contrôles internes attendus** (a-2 ; le tableau couvre cinq étapes à titre de référence, trois suffisent) :

| Étape | Acteur et application | Risque | Contrôle interne attendu |
|---|---|---|---|
| 1. Livraison constatée | prestataire logistique → site | reverser un article non livré ou retourné | date de livraison et statut « retourné » transmis au logiciel des dépôts, et non signalés par courriel |
| 2. Calcul du montant dû | comptable, tableur alimenté par deux extractions | **erreur et doublon** (200 reversements en double, 70 k€) ; reversement avant la fin du délai (400 cas, 140 k€) | calcul dans le logiciel des dépôts ; un article ne peut être payé qu'une fois (statut « reversé ») ; versement bloqué tant que 30 jours ne sont pas écoulés ou si un retour est en cours |
| 3. Coordonnées bancaires | service clients, logiciel des dépôts | **détournement** : 6 reversements (15 k€) vers des fraudeurs | modification demandée depuis l'espace sécurisé du vendeur, confirmée par un second canal (contre-appel au numéro connu), tracée avec son auteur ; premier virement vers un nouveau compte validé par une seconde personne |
| 4. Virements | comptable, portail bancaire | virement non autorisé ou erroné, préparé et validé par la même personne | séparation des tâches : préparation par la comptable, validation par la responsable financière de chaque lot, quel que soit le montant |
| 5. Enregistrement | progiciel comptable (total mensuel) | dette envers les vendeurs fausse (écart de 150 k€) | transmission du détail par vendeur et rapprochement mensuel, justifié, entre le logiciel des dépôts et la comptabilité |

**Deux tests** (documentaires) :
1. **Rapprochement exhaustif** des virements de 2026 avec les ventes du logiciel des dépôts : recherche des articles payés deux fois et des virements antérieurs à la date de livraison plus 30 jours, puis comparaison avec les retours (constats : 200 doublons, 400 reversements anticipés).
2. **Sondage** sur un échantillon des 2 500 modifications de coordonnées bancaires : existence d'une demande écrite du vendeur, vérification de son identité, auteur de la saisie (constat : aucune vérifiée, 6 détournements). Autres tests admis : reconstitution de l'écart de 150 k€ au 31/12/2026 ; observation d'un cycle hebdomadaire de préparation ; revue des virements validés sans seconde signature.

*3.1 b) – Quatre critères de performance et de conformité*

| Critère | Ce qui est attendu | Appréciation de la situation (annexe 3.1) |
|---|---|---|
| **Fiabilité** (exactitude, exhaustivité) (b-1) | chaque vendeur reçoit une fois, au bon moment, le bon montant ; la dette envers les vendeurs est la même dans le logiciel des dépôts et en comptabilité | faible : 200 doublons, 400 reversements anticipés, écart non expliqué de 150 k€ ; tableur écrasé chaque semaine, donc aucune piste d'audit |
| **Sécurité** (intégrité, traçabilité) (b-1) | données bancaires modifiées seulement par une personne autorisée, après vérification, avec une trace ; validation indépendante des virements | insuffisante : 2 500 modifications sans contrôle ni trace de l'auteur, 6 détournements ; la même comptable prépare et valide les virements de moins de 20 000 € |
| **Conformité** (au contrat et au RGPD) (b-2) | respect du délai contractuel de 30 jours ; données personnelles des vendeurs (coordonnées bancaires) exactes et protégées | non respectée : 45 jours en moyenne, 2 000 réclamations ; coordonnées transmises par courriel ou par téléphone, exactitude et sécurité non assurées |
| **Efficacité et efficience** (b-2) | un processus rapide, peu coûteux et capable d'absorber le volume de la place de marché | faible : 1,5 équivalent temps plein pour 64 000 reversements, ressaisies, sommes non récupérées de 135 k€ (40 + 80 + 15) ; le processus manuel ne passera pas à des dizaines de milliers de vendeurs |

Conclusion attendue : le processus n'est pas en état d'être repris tel quel pour la place de marché ; il doit être automatisé dans le logiciel des dépôts (ou dans le futur système de la place de marché) avec des contrôles bloquants, avant 2028.

**Réponses tolérées**
- Démarche en cinq à sept étapes (cadrage, prise de connaissance, analyse des risques, programme, collecte, restitution, suivi) si l'objectif, le périmètre, les livrables et le calendrier sont présents ; échéancier en diagramme de Gantt.
- Processus présenté en schéma (couloirs par acteur, format libre) plutôt qu'en tableau, s'il fait apparaître acteur, application, risque et contrôle.
- Recours à un auditeur externe pour une partie des tests, au titre de l'indépendance.
- Référence au COSO 2013 (activités de contrôle) ou au principe de séparation des tâches pour fonder les contrôles attendus.
- Autres critères pertinents : disponibilité (portail bancaire, tableur), traçabilité présentée séparément, gouvernance (aucun responsable du processus entre finances et service clients).
- L'analyse des coordonnées bancaires sous l'angle de la fraude au changement de coordonnées, si elle reste reliée au processus audité.

**Erreurs fréquentes**
- *Audit confondu avec l'audit légal des comptes* (`ET-34`) — juste : un audit interne du processus et du SI qui le supporte, mandaté par la présidente ; l'écart de 150 k€ est un constat de fiabilité, pas une question de technique comptable.
- *Méthodologie incomplète* (`JUR-A01`) — juste : objectif, périmètre, étapes, livrables et échéancier jusqu'à fin juillet 2027.
- *Constats non exploités* (`JUR-T08`) — juste : chaque risque, test et critère est relié à un chiffre de l'annexe 3.1.
- *Tests techniques proposés comme diligences* (limite du programme 3.2) — juste : rapprochements, sondages, entretiens, observations.
- *Glissement vers l'audit des habilitations, la note de synthèse ou les facteurs de succès* (périmètre de la question) — juste : le processus, ses risques, ses contrôles et ses critères.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI, contrôle interne, démarche et livrables, séparation des tâches, piste d'audit | définitions, étapes, fiches de constats | F10 § 1 à 3 | notion de cours |
| COSO 2013 | contrôle interne (toléré) | `coso_2013` ; F10 § 2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | exactitude et sécurité des données des vendeurs | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.2 – Le projet de séquestre programmable et de règlement en jetons (2,5 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain » ; `3.3.a` « Évaluer les opportunités, les risques et le cadre réglementaire associés… » ; `3.3.d` « Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO ». Limites : l'approche n'exige aucune compétence de programmation des registres ou des contrats intelligents ; les effets environnementaux doivent être intégrés.

**Annexes mobilisées** : annexe 3.2 (proposition de SCELLIDE, précisions, règlement des négociants, comparaison, avis), annexe 3.5 (MiCA, ISO 22739:2024, RGPD) et annexe 1.1 (ventes à l'étranger, prestataire de paiement agréé).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de blocs définie (registre distribué, blocs chaînés, consensus, inaltérabilité pratique) et contrat intelligent défini (programme « si… alors » inscrit sur la chaîne, exécuté automatiquement) | 0,5 |
| a-2 | Fonctionnement appliqué au séquestre, du paiement au versement ; ce que la chaîne garantit (exécution des règles, intégrité de l'enregistrement) et ne garantit pas (vérité des données entrées : l'atelier est l'oracle ; authenticité des articles) | 0,5 |
| b-1 | Grille d'opportunité appliquée ; deux apports et quatre limites (dont 750 k€ contre 300 k€ sur trois ans, irréversibilité, oracle, données personnelles sur une chaîne publique, rigidité, compétences) | 0,5 |
| b-2 | Recommandation argumentée : solution classique pour les ventes entre particuliers ; au plus, essai limité du règlement en jetons pour les négociants volontaires, sous conditions | 0,5 |
| c | Deux éléments encadrés par MiCA et deux questions non encadrées, chacun avec sa conséquence pratique pour ORSALIE | 0,5 |

**Réponse attendue**

*3.2 a) – Chaîne de blocs, contrat intelligent et fonctionnement du séquestre*

Une **chaîne de blocs** est un registre distribué, répliqué entre de nombreux nœuds, dans lequel les transactions sont regroupées en blocs ; chaque bloc contient l'empreinte du précédent, et un mécanisme de **consensus** (ici la preuve d'enjeu, bien moins consommatrice d'énergie que la preuve de travail) décide des blocs ajoutés. Elle permet à des acteurs qui ne se font pas confiance de partager un registre horodaté, pratiquement inaltérable, sans administrateur central (F11 § 1 ; vocabulaire normalisé par l'ISO 22739:2024). Un **contrat intelligent** est un programme inscrit sur la chaîne qui exécute automatiquement des règles « si… alors » lorsque les conditions prévues sont enregistrées ; ce n'est pas, en lui-même, un contrat au sens juridique.

**Fonctionnement pour une vente entre particuliers** (a-2) : (1) l'acheteur paie par carte sur le site, avec l'authentification forte appliquée par le prestataire de paiement ; (2) SCELLIDE convertit le montant en jetons de monnaie électronique adossés à l'euro ; (3) les jetons sont bloqués dans le contrat intelligent ; (4) l'atelier d'ORSALIE envoie au contrat le résultat de l'authentification, et l'acheteur confirme la réception (ou sept jours s'écoulent sans réclamation) ; (5) le contrat libère simultanément la commission d'ORSALIE et la part du vendeur, convertie en euros par le prestataire de services sur crypto-actifs partenaire ; si l'atelier déclare l'article non authentique, l'acheteur est remboursé automatiquement.

**Ce que la chaîne garantit** : que les règles programmées seront exécutées telles qu'écrites, que l'enregistrement d'une étape ne sera pas modifié a posteriori, horodatage compris. **Ce qu'elle ne garantit pas** : la **vérité** des données qu'on lui fournit. Le contrat se fie entièrement au résultat que l'atelier lui transmet : l'atelier est l'**oracle**, et une erreur d'authentification (30 contrefaçons vendues en 2026, selon Mme VERCHAMP et l'annexe 3.3) sera exécutée sans recours. Contrairement à ce qu'affirme SCELLIDE, la chaîne ne « garantit » donc ni l'authenticité des articles, qui reste le travail des authentificateurs, ni l'absence de fraude en amont (fausse confirmation de réception, article échangé avant l'envoi).

*3.2 b) – Grille d'opportunité et recommandation*

| Question de la grille (F11 § 2.2) | Réponse pour le séquestre d'ORSALIE |
|---|---|
| Plusieurs acteurs écrivent-ils dans le même registre ? | non : seuls ORSALIE (atelier) et l'acheteur déclenchent les étapes, sur le site d'ORSALIE |
| Les acteurs se défient-ils, sans tiers de confiance accepté ? | non : ORSALIE est déjà le tiers de confiance de la place de marché, et un prestataire de paiement agréé sait tenir les fonds |
| Faut-il une inaltérabilité opposable ? | peu : les litiges exigent au contraire de pouvoir reprendre ou rembourser |
| Les données peuvent-elles être partagées ? | non : identifiants, prix et photographies de particuliers sur une chaîne publique, « consultables par tous » |
| Volume, délai, coût justifiés ? | 30 000 puis 150 000 ventes par an, absorbables par la solution classique, deux fois et demie moins chère |

**Deux apports** (b-1) : (1) exécution automatique et horodatée des règles de libération, qui rassure acheteurs et vendeurs et évite les erreurs manuelles du processus actuel (annexe 3.1) ; (2) versement au vendeur sous 48 heures, et image d'innovation recherchée par M. ROCHAMBEL auprès des acheteurs d'Asie.

**Quatre limites** (b-1) : (1) **coût** : 300 + 3 × 150 = **750 k€** sur trois ans, contre 60 + 3 × 80 = **300 k€** pour le séquestre du prestataire de paiement, soit 450 k€ de plus pour un service équivalent ; (2) **irréversibilité** : une fois libérés, les fonds ne peuvent plus être repris par le contrat ; le litige reste à la charge d'ORSALIE, ce qui annule une partie de l'apport ; (3) **oracle** : la sécurité de tout le dispositif repose sur l'envoi du résultat de l'authentification par l'équipe numérique, qui ne connaît pas la technologie (M. LAMBRESCOT) ; (4) **données personnelles** : leur inscription, inaltérable et publique, contredit la minimisation et l'effacement prévus par le RGPD ; s'y ajoutent la **rigidité** (trois semaines pour changer une règle, contre une journée), la **dépendance** à une jeune société qui n'est pas elle-même prestataire de services sur crypto-actifs et la conversion obligatoire en jetons, inutile pour des particuliers qui paient et sont payés en euros.

**Recommandation** (b-2) : la chaîne de blocs ne répond pas à un besoin réel d'ORSALIE, qui reste le tiers de confiance de sa place de marché : je recommande le **séquestre tenu par le prestataire de paiement agréé**, en reprenant de la proposition l'idée de règles de libération automatiques, programmées dans le système de la place de marché et tracées. Pour les **négociants**, l'économie (15 k€ de frais par an contre 40 k€) et la rapidité sont réelles mais modestes au regard des ventes ; un **essai limité** avec les douze négociants qui utilisent déjà des jetons peut être envisagé, si les conditions vues au c) sont remplies et si les jetons sont convertis en euros dès leur réception.

*3.2 c) – Ce que MiCA encadre et n'encadre pas dans le règlement des négociants*

| | Élément | Conséquence pratique pour ORSALIE |
|---|---|---|
| **Encadré** | l'**émission** des jetons de monnaie électronique : leur émetteur doit être agréé comme établissement de crédit ou de monnaie électronique | vérifier, avant tout essai, l'agrément de l'émetteur des jetons proposés par SCELLIDE |
| **Encadré** | les **prestataires de services sur crypto-actifs**, ici pour la conservation des jetons pour le compte d'ORSALIE et leur échange contre des euros : agrément obligatoire ; depuis le 02/07/2026, seuls les prestataires agréés selon MiCA peuvent exercer | exiger la preuve de l'agrément du partenaire de SCELLIDE (un ancien enregistrement français ne suffit plus) ; SCELLIDE, qui n'est pas prestataire, ne peut pas elle-même conserver ni échanger les jetons |
| **Non encadré** | la **comptabilité** des jetons reçus (repères de l'annexe 3.5) | à traiter avec l'expert-comptable d'ORSALIE avant tout essai ; MiCA ne la règle pas |
| **Non encadré** | la **fiscalité** des jetons reçus (repères de l'annexe 3.5) | à traiter avec le conseil d'ORSALIE avant tout essai ; MiCA ne la règle pas |

**Réponses tolérées**
- Définition de la chaîne de blocs par l'opposition à une base de données distribuée, administrée par un acteur qui peut la modifier.
- Recommandation de ne pas retenir non plus le règlement en jetons des négociants, si elle est argumentée (montant modeste, compétences absentes, questions non réglées par MiCA).
- Remarque que SCELLIDE annonce convertir elle-même les euros en jetons alors qu'elle n'est pas prestataire de services sur crypto-actifs : point à faire vérifier, sans analyse juridique.
- Autres éléments non encadrés, en complément : la protection des données personnelles inscrites sur la chaîne (relevant du RGPD, pour le séquestre entre particuliers) et la sécurité du SI d'ORSALIE ; la relation contractuelle entre ORSALIE et SCELLIDE, ou la valeur juridique du contrat intelligent.
- Évocation des effets environnementaux (preuve d'enjeu peu consommatrice, mais transactions et conversions supplémentaires) dans la grille.

**Erreurs fréquentes**
- *Chaîne de blocs confondue avec une base de données distribuée* (`ET-08`) ; *« inaltérable » sans nuance, oubli de l'oracle* (F11 § 6) — juste : la chaîne garantit l'enregistrement, pas la vérité de la donnée transmise par l'atelier.
- *Reprendre l'argument « la blockchain garantit l'authenticité »* (`JUR-T03`) — juste : l'authenticité est établie par l'atelier ; la proposition doit être lue de façon critique.
- *Opportunités sans limites, ou l'inverse* (`ET-19`) — juste : deux apports et quatre limites, puis une recommandation.
- *Coût réduit au prix de mise en place* (`ET-33`) — juste : coût sur trois ans, 750 k€ contre 300 k€.
- *Champ de MiCA étendu à des questions qu'il ne traite pas, ou NFT supposés couverts* (`ET-35`) ; *régime français antérieur présenté comme encore valable après le 01/07/2026* (F11 § 6) — juste : repères de l'annexe 3.5.
- *Développement du contrat intelligent ou description cryptographique* (limite du programme 3.3) — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de blocs, consensus, contrat intelligent, oracle, grille d'opportunité | définitions, limites | F11 § 1 et 2 | notion de cours |
| Règlement (UE) 2023/1114 (MiCA) | jetons de monnaie électronique, émetteur agréé, prestataires de services sur crypto-actifs, fin de la période transitoire le 01/07/2026 ; ni comptabilité ni fiscalité | `mica` ; F11 § 3 | applicable depuis le 30/12/2024 (jetons stables depuis le 30/06/2024) |
| ISO 22739:2024 | vocabulaire des chaînes de blocs | `iso_22739_2024` ; F11 § 3.4 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | minimisation, effacement | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.3 – La fraude et l'apport de l'intelligence artificielle (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.f` « Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques » ; `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ». Limite : le développement d'algorithmes d'apprentissage automatique n'est pas attendu.

**Annexes mobilisées** : annexe 3.3 (fraudes de 2026, règles actuelles, outil proposé, accès), annexe 3.5 (RGPD, règlement sur l'intelligence artificielle) et annexe 1.1 (ventes par zone, service clients, atelier).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie des risques SI présentée (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers, éventuellement fraude interne) | 0,5 |
| a-2 | Cinq fraudes classées et risque nouveau de la place de marché, avec le maillon exploité (compte, paiement, livraison, retour, dépôt ou annonce) | 0,5 |
| b-1 | Apprentissage automatique distingué de l'IA générative ; deux apports de l'outil par rapport aux règles (85 % de détection, scores des annonces et des photographies, moins de blocages) | 0,5 |
| b-2 | Quatre limites appliquées : faux positifs et biais (9 % contre 2 %), explicabilité, refus et suspensions automatiques face au droit à une intervention humaine, données étiquetées absentes ; conclusion conditionnelle | 0,5 |
| c-1 | Deux mesures de traitement, chacune reliée à une fraude et assortie de son responsable | 0,5 |
| c-2 | Troisième mesure (organisation de la lutte contre la fraude, décision humaine, registre structuré) ; mesures distinctes de l'architecture de confiance | 0,5 |

**Réponse attendue**

*3.3 a) – Typologie et classement des fraudes*

Les risques liés au SI se classent en **cybermenaces** (attaques délibérées contre les comptes, les données ou les applications), **défaillances opérationnelles** (erreurs, contrôles absents, pannes, dépendance à un prestataire), **risques réglementaires** (non-respect d'une obligation : protection des données, droit des consommateurs, contrefaçon) et **risques métiers** (atteinte à la marge, à l'image, à la relation client) ; une même fraude combine souvent plusieurs catégories, dont la catégorie dominante oriente le traitement (F12 § 5).

| Fraude (annexe 3.3 A) | Catégorie dominante | Maillon exploité | Enjeu 2026 |
|---|---|---|---|
| Paiements par carte contestés | cybermenace externe et risque métier (perte de la marchandise et du paiement) | paiement : carte volée utilisée sur un compte que rien ne relie à son titulaire | 400 cas, 200 k€ |
| Comptes de clients piratés | cybermenace (réutilisation d'identifiants dérobés ailleurs) | authentification des clients : mot de passe seul, essais illimités, aucune surveillance le week-end | 300 comptes, 60 k€ |
| Fausses réclamations « article non reçu » | fraude de clients, risque métier | livraison : preuve de remise insuffisante pour des articles de valeur | 250 cas, 125 k€ |
| Retours d'une contrefaçon à la place de l'original | fraude de clients et défaillance opérationnelle | retour : article remboursé sans être comparé à l'article expédié | 60 cas, 150 k€ |
| Contrefaçons présentées par des vendeurs | risque métier et réglementaire (vente de contrefaçons, image de la marque), défaillance de l'authentification | dépôt et, demain, annonce : 30 contrefaçons passées malgré l'atelier | 6 600 refusées, 30 vendues, 45 k€ |
| **Risque nouveau de la place de marché** (au choix) | cybermenace et fraude | compte vendeur piraté dont les coordonnées bancaires sont changées pour détourner les reversements (lien avec les 6 détournements de l'annexe 3.1), ou faux vendeurs publiant des annonces avec des photographies copiées | — |

Au total, environ **580 k€** de pertes en 2026, soit 1,2 % des ventes, sans compter l'atteinte à l'image. On note aussi une **fraude interne possible** (25 avoirs de 500 € accordés par un auteur inconnu).

*3.3 b) – L'outil de détection : apports et limites*

L'outil relève de l'**apprentissage automatique** : un modèle **apprend**, à partir de transactions passées dont on sait si elles étaient frauduleuses, à **classer** et à **attribuer un score** à de nouvelles transactions ; il ne produit pas de contenu. L'**IA générative**, elle, produit du texte ou des images à partir d'un modèle pré-entraîné (F13 § 1) : ce n'est pas l'outil proposé ici.

**Deux apports** (b-1) : (1) une **détection plus large et plus fine** que quinze règles fixes, qui n'ont arrêté qu'environ 55 % des fraudes au paiement (480 sur 880) : l'essai annonce 85 %, en tenant compte de nombreux signaux à la fois, et le score des **connexions** aurait pu signaler l'attaque de novembre ; (2) une **extension aux annonces** de la place de marché (score et analyse des photographies : 70 % des contrefaçons de l'essai signalées, photographies copiées repérées), qui permet de concentrer l'examen humain sur les cas à risque, et moins de commandes légitimes bloquées : environ 2 000 (3 % d'environ 65 000) contre 11 520 en 2026 (18 % des commandes bloquées), qui ont fait perdre 1 200 clients.

**Quatre limites ou risques** (b-2) :
1. **Faux positifs et biais** : 3 % des commandes légitimes bloquées, mais 9 % pour les clients du Moyen-Orient et d'Asie contre 2 % en Europe, soit 4,5 fois plus. Le modèle a appris sur des sites européens de mode : il pénalise les clients étrangers, alors que le plan « ORSALIE 2030 » veut doubler les ventes à l'étranger. Risque commercial et éthique de discrimination selon l'origine.
2. **Explicabilité** : l'éditeur ne donne pas les raisons d'un score ; un conseiller ne peut ni justifier un refus au client ni repérer une erreur du modèle.
3. **Place de la décision humaine** : le réglage proposé refuse des commandes et suspend des comptes de vendeurs **automatiquement**. D'après les repères, une personne a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé qui l'affecte de manière significative ; lorsqu'une telle décision est admise, elle peut obtenir une intervention humaine et la contester. ORSALIE doit donc prévoir l'examen humain des refus et des suspensions et un recours ; la notation à grande échelle des clients justifie en outre une analyse d'impact préalable. Le règlement sur l'intelligence artificielle impose déjà la **maîtrise de l'IA** par les conseillers qui utiliseront les scores ; aucun classement du système n'est demandé ici.
4. **Données nécessaires** : l'outil ne progresse que si les fraudes confirmées lui sont signalées ; or elles sont notées en texte libre dans un tableur et les retours de contrefaçons ne sont pas distingués. Sans données fiables et étiquetées, le modèle restera celui des autres clients de l'éditeur. L'analyse des photographies laisse passer 30 % des contrefaçons et n'examine pas l'article : elle **complète** l'atelier, elle ne le remplace pas.

Conclusion : l'outil est utile (abonnement de 90 k€ par an à rapprocher de 580 k€ de pertes), **à condition** d'en faire une aide à la décision : scores élevés examinés par un conseiller, seuils fixés par ORSALIE et réexaminés selon les zones, explication minimale exigée de l'éditeur, contrôle régulier des faux positifs par zone.

*3.3 c) – Trois mesures de traitement*

| Mesure | Fraude traitée | Responsable |
|---|---|---|
| (c-1) À l'expédition des articles de valeur, enregistrer les éléments d'identification de l'article (numéro de série, photographies de détail, scellé numéroté d'ORSALIE) ; au retour, l'atelier compare l'article reçu avant tout remboursement | retours de contrefaçons (60 cas, 150 k€) | Mme VERCHAMP (atelier), avec le service clients |
| (c-1) Exiger, au-delà d'un montant, une remise contre signature ou code communiqué à l'acheteur, et en tenir compte avant d'accepter une réclamation « non reçu » | fausses réclamations (250 cas, 125 k€) | M. ROCHAMBEL, avec le prestataire logistique |
| (c-2) Organiser la lutte contre la fraude : un référent fraude au service clients, un registre structuré des fraudes confirmées (catégorie, canal, zone, montant), qui alimente l'outil, une revue mensuelle des scores, des faux positifs et des seuils, et la décision humaine sur les refus et suspensions | toutes, notamment paiements contestés et contrefaçons des vendeurs | M. BELLASTRE, sous votre supervision |

**Réponses tolérées**
- Classement dans un tableau probabilité × impact, à partir des nombres de cas et des pertes de l'annexe 3.3, sans cotation chiffrée exigée.
- Distinction fraude externe / fraude interne / défaillance, si elle couvre les cinq fraudes.
- Autres risques nouveaux : collusion entre un acheteur et un vendeur, paiement proposé hors de la place de marché, usurpation de l'identité d'un vendeur connu.
- Autres mesures : vérification de l'identité des vendeurs de la place de marché avant leur première vente, plafond de vente pour les nouveaux vendeurs, examen renforcé par l'atelier des catégories les plus contrefaites (montres), clause de responsabilité et d'audit dans le contrat de l'éditeur de l'outil, transfert du risque par une assurance pour les fraudes résiduelles.
- Référence aux limites de l'IA défensive (faux positifs, biais, explicabilité) citées par le programme.

**Erreurs fréquentes**
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — juste : l'outil classe et note, il ne génère rien.
- *Outil présenté comme une solution sans limites, ou rejeté sans examen* (`ET-19`) — juste : apports chiffrés et limites appliquées, conclusion conditionnelle.
- *Morceau de cours sur les biais sans les chiffres de l'essai* (`JUR-T01`) — juste : 9 % contre 2 %, contradiction avec l'objectif de doubler les ventes à l'étranger.
- *Décision entièrement automatisée acceptée* (`JUR-D06` : le SI aide la décision humaine) — juste : examen humain des refus et des suspensions.
- *Fonctionnement interne du modèle développé* (limite du programme) — non attendu.
- *Mesures de la question 3.4 (MFA, journalisation) reprises ici* — elles ne sont pas valorisées deux fois.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques, menaces | cybermenaces, défaillances, risques réglementaires et métiers | F12 § 5 | notion de cours |
| Apprentissage automatique, IA générative, biais, IA défensive | distinction, limites | F13 § 1 à 3 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | décision fondée exclusivement sur un traitement automatisé, analyse d'impact | `rgpd` ; F15 | applicable depuis le 25/05/2018 |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle | maîtrise de l'IA depuis le 02/02/2025 | `ai_act` ; F13 § 5 | en vigueur, application échelonnée |
| Règlement (UE) 2026/1744 | systèmes à haut risque de l'annexe III au 02/12/2027 | `omnibus_numerique_ia` ; F13 § 5.2 | en vigueur |

---

### 3.4 – L'architecture de confiance et la surveillance du site (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ». Limites : la mise en œuvre technique n'est pas exigée ; la sécurité est envisagée de façon systémique.

**Annexes mobilisées** : annexe 3.3 D (accès au site et surveillance), annexe 3.3 A (fraudes), annexe 3.5 (ISO/IEC 27001:2022 et 27002:2022, guide d'hygiène de l'ANSSI, RGPD) et annexe 1.1 (équipe numérique, hébergeur en nuage, prestataire de paiement).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Architecture de confiance définie (aucune confiance implicite, chaque accès authentifié et autorisé selon le contexte, moindre privilège, cloisonnement) ; Zero Trust présenté comme un cadre et non comme un produit | 0,5 |
| a-2 | Authentification adaptée à chaque population : clients (renforcée selon le risque, limitation des essais), vendeurs (multifacteur, nouvelle vérification avant tout changement de coordonnées bancaires), administrateurs (multifacteur obligatoire, comptes nominatifs), reliée aux constats | 0,5 |
| a-3 | Chiffrement des données au repos (base des clients, pièces d'identité, coordonnées bancaires) ; cloisonnement de l'administration, des remboursements et du paiement par rapport aux pages publiques, administration non exposée directement | 0,5 |
| b-1 | Gestion des identités et des accès : comptes nominatifs, rôles, moindre privilège, fin des comptes partagés, comptes à privilèges, revue des 60 comptes | 0,5 |
| b-2 | Journalisation des connexions et des actions sensibles (avoirs, remboursements, coordonnées bancaires) et supervision hors heures ouvrées, reliées aux 25 avoirs et à l'attaque de novembre | 0,5 |
| b-3 | Sauvegardes séparées du compte de production, protégées, restauration essayée ; objectifs de reprise à fixer, sans détailler les plans | 0,5 |

**Réponse attendue**

*3.4 a) – L'architecture de confiance*

Une **architecture de confiance** organise le système d'information pour que chaque accès soit **authentifié** (l'identité est prouvée), **autorisé** (selon le juste besoin) et **tracé**, que les données sensibles soient **chiffrées** et que les fonctions soient **cloisonnées**, afin qu'une compromission reste limitée. Le modèle **Zero Trust** en est le cadre de référence : ne jamais accorder de confiance implicite (y compris à un administrateur connecté depuis Internet), vérifier chaque accès selon le contexte (identité, terminal, sensibilité de l'action), appliquer le moindre privilège ; c'est une démarche d'architecture progressive, **pas un produit** (F12 § 3).

| Principe | Proposition pour le site et la place de marché | Constat de l'annexe 3.3 traité |
|---|---|---|
| Authentification des **clients** (a-2) | limitation des essais et blocage temporaire, refus des mots de passe trop courts ou déjà dérobés ; authentification multifacteur proposée à tous, et exigée selon le risque : nouvel appareil, changement d'adresse de livraison, usage d'un avoir, commande élevée ; le paiement reste protégé par l'authentification forte du prestataire | 40 000 tentatives et 300 comptes piratés ; avoirs et adresse modifiables sans nouvelle vérification |
| Authentification des **vendeurs** (a-2) | authentification multifacteur obligatoire, car le compte donne accès à de l'argent ; nouvelle vérification et confirmation par un second canal avant tout changement de coordonnées bancaires | espace des vendeurs protégé par un mot de passe seul ; risque de détournement des reversements |
| Authentification des **administrateurs** (a-2) | authentification multifacteur obligatoire, comptes nominatifs distincts des comptes d'usage courant, accès réservé à des postes et à des personnes identifiés | administration accessible depuis Internet avec un mot de passe seul ; 3 comptes partagés par les développeurs |
| **Chiffrement** (a-3) | maintien du chiffrement des échanges ; chiffrement de la base des clients, des coordonnées bancaires et des copies de pièces d'identité, avec des clés gérées à part ; conservation des pièces limitée à la durée nécessaire | base des clients et pièces d'identité non chiffrées |
| **Cloisonnement** (a-3) | séparer les pages publiques, l'administration, la fonction de remboursement et d'avoirs et les données sensibles en zones distinctes, avec des droits propres : la compromission d'un compte client ou d'une page ne donne pas accès au reste ; administration non exposée directement à Internet ; environnement de développement séparé de l'exploitation ; aucune donnée de carte chez ORSALIE, le paiement restant chez le prestataire agréé ; double validation des remboursements et avoirs au-delà d'un seuil | une seule application, un même environnement pour tout ; développeurs avec tous les droits en exploitation ; 25 avoirs sans auteur connu |

La refonte du site est le moment de construire ce cloisonnement ; d'ici là, les mesures d'authentification et de comptes nominatifs sont prioritaires, car peu coûteuses.

*3.4 b) – Les dispositifs de surveillance et de résilience*

| Dispositif | Proposition | Ce qu'il change au regard de l'annexe 3.3 |
|---|---|---|
| **Gestion des identités et des accès** (b-1) | un annuaire unique des comptes internes ; rôles définis par métier (un conseiller accorde un avoir jusqu'à un plafond, un développeur n'accède pas aux données des clients en exploitation) ; suppression des 3 comptes partagés ; comptes à privilèges nominatifs, limités et surveillés ; création, modification et suppression des comptes liées aux arrivées et aux départs ; revue périodique des 60 comptes d'administration par leurs responsables | chaque action devient imputable ; les droits excessifs des développeurs et les comptes inutiles disparaissent |
| **Journalisation** (b-2) | conservation horodatée et protégée contre la modification des connexions (réussies et échouées) et des actions sensibles : avoirs, remboursements, changements de prix, de coordonnées bancaires et d'adresses, accès aux données des clients | on saurait qui a accordé les 25 avoirs de 500 € ; les traces permettent d'enquêter et alimentent la supervision et l'outil de détection |
| **Supervision** (b-2) | surveillance continue, y compris la nuit et le week-end, par une astreinte de l'équipe numérique ou un centre de supervision externe, avec des alertes automatiques (pic de connexions échouées, nombreux changements d'adresse, avoirs inhabituels) et une procédure de réaction (blocage des comptes visés, information des clients) | l'attaque du samedi soir de novembre aurait été repérée et arrêtée en quelques minutes, et non le lundi |
| **Sauvegardes** (b-3) | copies régulières de la base et des fichiers conservées hors du compte de production (autre compte ou autre fournisseur), dont une copie protégée contre la modification et la suppression, chiffrées ; restauration essayée régulièrement ; objectifs de perte de données et de durée d'interruption admissibles (RPO, RTO) fixés avec la présidente, base des plans de continuité et de reprise à formaliser ensuite | une compromission du compte de l'hébergeur ou une erreur ne détruirait plus à la fois les données et leurs copies ; la restauration ne serait plus un pari |

Ces mesures correspondent aux bonnes pratiques du guide d'hygiène informatique de l'ANSSI et aux mesures de l'annexe A de l'ISO/IEC 27001:2022 détaillées par l'ISO/IEC 27002:2022 (contrôle d'accès, authentification, journalisation, surveillance, sauvegarde, cryptographie), qui servent de **référentiels**, sans démarche de certification.

**Réponses tolérées**
- Présentation selon les fonctions du NIST CSF 2.0 (gouverner, identifier, protéger, détecter, répondre, rétablir), si les quatre dispositifs sont présents et reliés aux constats.
- Micro-segmentation évoquée pour limiter les mouvements latéraux, si elle est présentée comme un principe.
- Analyse comportementale des connexions et des actions des administrateurs par l'IA défensive, reliée à la question 3.3.
- Recours à un prestataire de supervision, si la responsabilité de la réaction reste définie chez ORSALIE.
- Mention de la séparation entre l'administration courante et les tâches d'administration technique.

**Erreurs fréquentes**
- *Zero Trust présenté comme un produit à acheter* (`ET-04`, `JUR-S03`) — juste : un cadre d'architecture et une démarche.
- *Authentification multifacteur confondue avec un mot de passe complexe* ; identification, authentification et autorisation confondues (`ET-28`).
- *Mesures sans lien avec les constats* (`JUR-S05`, `JUR-T08`) — juste : chaque proposition traite un constat de l'annexe 3.3 D.
- *Normes, référentiels et solutions confondus* (`JUR-S06`, `ET-01`) — juste : ISO/IEC 27001:2022 et le guide d'hygiène informatique de l'ANSSI comme référentiels, pas comme outils.
- *PCA et PRA développés ou confondus* (`ET-02`) — non attendus ici ; seuls les objectifs de reprise sont mentionnés.
- *Paramétrage technique ou tests techniques proposés* (`JUR-T12`) — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Architecture de confiance, Zero Trust, gestion des identités et des accès, authentification multifacteur, sauvegardes | principes | F12 § 3 et 4 | notion de cours |
| Modèle Zero Trust (ANSSI) | cadre d'architecture, pas un produit | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| ISO/IEC 27001:2022 et ISO/IEC 27002:2022 | mesures de l'annexe A (contrôle d'accès, journalisation, surveillance, sauvegarde, cryptographie) | `iso_27001_2022`, `iso_27002_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | 42 mesures : comptes nominatifs, administration, journalisation, sauvegarde | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | sécurité des données des clients et des vendeurs | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.5 – La mesure et la réduction de l'impact environnemental du site (2,5 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI » ; `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ». Limites : la durabilité est intégrée dans la gouvernance globale du SI, et non comme un ajout marginal.

**Annexes mobilisées** : annexe 3.4 (usage du site, premières mesures, projet du marketing, avis), annexe 3.5 (loi REEN, RGESN, EcoIndex) et annexe 1.1 (plan « ORSALIE 2030 », refonte du site, ventes en ligne).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Démarche : périmètre (pages, application, hébergement, réseaux, terminaux des clients), mesure de référence, limites des mesures disponibles (EcoIndex relatif, méthode de l'hébergeur inconnue), cibles, responsable, suivi intégré au pilotage du numérique | 0,5 |
| a-2 | Deux indicateurs complets (formule, source, fréquence, cible, axe) | 0,5 |
| b-1 | Écoconception définie (réduire l'impact dès la conception, sur le cycle de vie, en questionnant le besoin ; RGESN) ; deux mesures adaptées à l'annexe 3.4 | 0,5 |
| b-2 | Deux autres mesures, dont une réponse à l'objection de la responsable du catalogue | 0,5 |
| c | Conditions de l'affichage « site éco-conçu » : améliorations réalisées et mesurées, évaluation selon le RGESN et déclaration d'écoconception publiée, message précis et vérifiable, pas avant la refonte | 0,5 |

**Réponse attendue**

*3.5 a) – Démarche et indicateurs*

**Démarche** (a-1) :
1. **Périmètre** : les pages du site et l'application, l'hébergement et le stockage chez l'hébergeur en nuage, les réseaux, les **terminaux des clients** (60 % des pages vues sur smartphone) et, pour l'équipe, les équipements du catalogue et les postes. Les terminaux concentrent l'essentiel de l'empreinte du numérique, principalement du fait de leur fabrication (étude ADEME-Arcep) : un site lourd qui oblige à changer de smartphone pèse plus que les kilowattheures du serveur.
2. **Mesure de référence** (début 2027) : EcoIndex des dix pages types (moyenne F, accueil et fiche d'article en G), poids des pages (12 Mo et 160 éléments pour une fiche d'article), données transférées (1 500 To), stockage (80 To, doublé en trois ans), consommation et émissions déclarées par l'hébergeur (180 MWh, 30 tonnes équivalent CO2). Ces mesures ont des **limites** : l'EcoIndex est une note relative d'une page, pas une mesure de l'empreinte ; la méthode de l'hébergeur doit être demandée ; aucune mesure ne couvre les terminaux ni les réseaux. Une analyse du cycle de vie du service peut compléter ces mesures, en principe, plus tard.
3. **Cibles et responsable** : des cibles intégrées aux exigences de la refonte (critères du RGESN) ; un responsable désigné, puisque « personne n'en est chargé » (M. LAMBRESCOT) ; mesure à chaque mise en ligne.
4. **Suivi** : indicateurs dans le tableau de bord du numérique (axe environnement), revus avec la présidente, en cohérence avec l'objectif du plan « ORSALIE 2030 » de mesurer et réduire l'impact du numérique.

**Deux indicateurs** (a-2) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| EcoIndex moyen des dix pages types | somme des scores EcoIndex (sur 100) des dix pages types / 10, mesurés sur smartphone | mesures EcoIndex de l'équipe numérique, même protocole | mensuelle et avant chaque mise en ligne | note moyenne C au moins à la mise en service du nouveau site (2028), contre F en mars 2027, aucune page en F ou G | environnement |
| Poids moyen transféré par page vue | données transférées dans le mois / pages vues dans le mois | relevés de trafic de l'hébergeur et outil de mesure d'audience | mensuelle | moins de 2 Mo en 2028, contre environ 10 Mo en 2026 (1 500 To pour 150 millions de pages) et 12 Mo pour une fiche d'article | environnement |

*3.5 b) – Écoconception et quatre mesures*

L'**écoconception** d'un service numérique consiste à réduire ses impacts environnementaux **dès sa conception** et sur tout son **cycle de vie**, en interrogeant d'abord le **besoin** (sobriété : chaque fonctionnalité, chaque contenu est-il utile ?), puis l'efficacité des contenus, des pages, des serveurs et de l'hébergement ; le RGESN, version 2024, en fixe les critères (F14 § 2-3).

| Mesure | Application à ORSALIE |
|---|---|
| (b-1) **Photographies chargées à la demande** | afficher d'abord quelques photographies (vue d'ensemble, détails clés), les autres seulement quand le client les demande ; formats compressés et tailles adaptées à l'écran (smartphone) au lieu de la haute définition pour tous |
| (b-1) **Vidéo sans lecture automatique** | vidéo de 30 secondes lancée seulement par le client, dans une résolution adaptée au terminal |
| (b-2) **Conservation limitée des contenus** | après la vente, ne conserver qu'un jeu réduit de photographies utiles (preuve de l'état et de l'authentification), dans un seul format, et supprimer le reste selon une durée définie ; 80 To pour 700 000 articles, dont l'essentiel est vendu, doublés en trois ans |
| (b-2) **Compatibilité avec les terminaux anciens** | une application et des pages utilisables sur des smartphones de plus de quatre ans, comme le recommande le RGESN, pour ne pas pousser les clients à renouveler leur terminal (premier poste de l'empreinte, objectif de la loi REEN) |

**Réponse à l'objection de Mme DUVERNAIS** : il ne s'agit pas de supprimer les 40 photographies, mais de ne pas les charger toutes d'emblée : le client qui veut « voir chaque rayure » y accède, avec un zoom sur le détail ; un essai sur une catégorie permettra de vérifier que les retours pour « article différent de la fiche » ne progressent pas. La sobriété est ici conciliée avec la promesse d'un luxe circulaire et transparent.

*3.5 c) – Conditions d'un affichage « site éco-conçu »*

Le marketing ne pourrait afficher ce message qu'à plusieurs conditions : (1) **après** des améliorations réelles, donc pas en juin 2027, alors que l'accueil et la fiche d'article sont notés G ; (2) sur la base d'une **évaluation selon le RGESN** et de la **publication de la déclaration d'écoconception** prévue par ce référentiel, qui indique les critères respectés, ceux qui ne le sont pas et le plan de progrès ; (3) avec un message **précis et vérifiable** (par exemple « pages d'article allégées de 12 à 2 Mo, note EcoIndex moyenne C ») plutôt qu'une formule générale, et des données de l'hébergeur dont la méthode est connue ; (4) en **cohérence** avec le reste du site : on ne peut se dire éco-conçu en conservant indéfiniment des contenus inutiles. Faute de quoi, la marque, fondée sur la confiance et l'économie circulaire, s'exposerait à un reproche de communication trompeuse.

**Réponses tolérées**
- Autres indicateurs complets : volume stocké de photographies et de vidéos (To), part des pages notées A à C, consommation électrique par commande déclarée par l'hébergeur, part des clients dont le terminal a plus de quatre ans ; les indicateurs non chiffrés ou sans cible ne sont pas valorisés.
- Autres mesures : suppression des fonctionnalités et des éléments de suivi inutiles, allègement de la page d'accueil, mise en cache, allongement de la durée d'usage des ordinateurs portables et des équipements du catalogue (loi REEN), critères environnementaux dans le choix de l'hébergement après la refonte.
- Références aux trois composantes de l'EcoIndex (complexité de la page, poids, requêtes) pour justifier les mesures.
- Mention que l'affichage pourrait viser une partie seulement du site, déjà améliorée, avec la date de l'évaluation.

**Erreurs fréquentes**
- *Sobriété réduite à une économie d'énergie* (`ET-12`) — juste : questionner le besoin (photographies chargées, vidéo automatique, conservation).
- *Empreinte du numérique réduite à l'électricité de l'hébergement* (`ET-38`) — juste : les terminaux et leur fabrication dominent.
- *EcoIndex présenté comme une mesure complète de l'empreinte* (F14 § 4) — juste : note relative d'une page.
- *Indicateurs génériques, sans formule, source ou cible* (`ET-18`, `JUR-A02`) — juste : deux indicateurs complets, avec la valeur de départ.
- *Calcul d'empreinte ou de bilan carbone tenté* — non attendu.
- *Badge accepté en juin 2027 sans condition* (`JUR-T03`) — juste : des améliorations mesurées et une déclaration d'écoconception d'abord.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Écoconception, sobriété, Green IT, indicateurs | définitions, mesures, EcoIndex | F14 § 1 à 4 | notion de cours |
| Loi n° 2021-1485 du 15 novembre 2021 (REEN) | durée de vie des équipements, écoconception | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | critères d'écoconception, équipements anciens, déclaration d'écoconception | `rgesn_2024` ; F14 § 2 | version 2 publiée le 17/05/2024 |
| EcoIndex | note de A à G d'une page web | `ecoindex` ; F14 § 4 | outil en ligne |
| Étude ADEME-Arcep | part des terminaux dans l'empreinte (connaissance du candidat) | `etude_ademe_arcep_numerique` ; F14 § 1 | mise à jour du 17/01/2025 |
