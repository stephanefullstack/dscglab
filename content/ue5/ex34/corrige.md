# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 34 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique et organisation de la DSI, F02 gouvernance et référentiels, F03 architecture et urbanisation, F04 relations avec les ESN et contrats, F05 projets et changement, F13 intelligence artificielle, F15 RGPD opérationnel, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 La place de marché, le rôle stratégique du système d'information et la veille technologique | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.d` Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques ; `1.3.d` Fonctionnement et usages des technologies émergentes : blockchain, registres distribués, IA, … | 3,5 |
| 1.2 La gouvernance des choix numériques et l'organisation de l'équipe numérique | `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ; `1.2.b` Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) | 3 |
| 1.3 L'architecture composable et ses impacts | `1.3.a` Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) ; `1.3.e` Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers | 2 |
| 1.4 Le choix et le pilotage de l'entreprise de services du numérique | `1.4.b` Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle ; `1.4.d` Méthodologie de négociation contractuelle et analyse des risques ; `1.4.e` Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) | 2,5 |
| 1.5 Le projet hybride, les exigences et la recette | `1.5.b` Méthodologies de gestion de projet (cycle en V, agile, hybride) ; `1.5.c` Élaboration d'un cahier des charges fonctionnel et technique ; `1.5.f` Mise en œuvre et contrôle du plan qualité | 3 |
| **Dossier 1 – Préparer la refonte du site et l'ouverture de la place de marché** |  | **14** |

Répartition indicative : connaissances (place de marché, veille, gouvernance du SI, équipes produit, urbanisation et architecture composable, négociation et gouvernance d'un contrat, démarche hybride et Scrum, exigence vérifiable, plan qualité et recette) environ 2,75 points (items 1.1 a-1, 1.1 b-1 pour moitié, 1.2 a-1, 1.2 b-1 pour moitié, 1.3 a-1, la moitié de 1.4 b-1, 1.5 a-2 pour moitié, la moitié de 1.5 c-1) ; analyse des annexes et recommandations environ 11,25 points, soit environ 80 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – La place de marché, le rôle stratégique du système d'information et la veille technologique (3,5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.d` « Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques » ; §1.3 : `1.3.d` « Fonctionnement et usages des technologies émergentes : blockchain, registres distribués, IA, … » (nature des deux technologies évaluées en b). Limites : « Ne pas confondre alignement stratégique et simple adéquation technique. » « Ne pas se limiter à une veille passive : intégrer l'analyse prospective dans l'évaluation des opportunités SI. »

**Annexes mobilisées** : annexes 1.2 (note de la présidente, repères 2026-2030, limites du site, deux technologies, essais, repères réglementaires) et 1.1 (modèle d'activité, canaux, ventes à l'étranger).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Place de marché caractérisée (plateforme d'intermédiation entre deux catégories d'utilisateurs, revenu par commission, effets de réseau, confiance) ; conclusion : le SI passe d'une fonction de soutien au cœur du modèle, ce qui impose de décider sa stratégie avec celle de l'entreprise | 0,5 |
| a-2 | Sources de valeur : de la marge et de la commission du dépôt-vente sur des articles traités par ORSALIE aux commissions sur des ventes entre particuliers et aux services ; la valeur tient à la confiance (authentification), au volume d'annonces et aux données | 0,5 |
| a-3 | Processus clés : processus internes et manuels remplacés par des processus pilotés par le vendeur et l'acheteur à travers le SI, qui orchestre plusieurs acteurs externes ; l'authentification reste le processus différenciant | 0,5 |
| a-4 | Dépendance au numérique appuyée sur les chiffres (85 % puis plus de 90 % des ventes en ligne ; × 4 vendeurs, 300 000 annonces ; incident de novembre 2026 et de mars 2027 ; places de marché A, B, C à la fois canaux et concurrents) | 0,5 |
| b-1 | Veille technologique définie (surveillance active et prospective) ; dispositif complet et appliqué au cas : objets reliés à « ORSALIE 2030 », sources, acteurs nommés, diffusion, décision et expérimentation | 0,5 |
| b-2 | Recherche par photo : apprentissage automatique ; apports (recherche d'articles uniques, international, préremplissage des annonces), limites (8 sur 10, 6 sur 10 pour les montres, n'authentifie pas), conditions et décision (expérimentation limitée, après la séparation du service de recherche) | 0,5 |
| b-3 | Assistant d'IA générative : apports (72 000 messages en langue étrangère, 30 heures de délai), risques (10 réponses erronées sur 200, dont un engagement de remboursement ; conversations conservées par l'outil gratuit ; information des clients, maîtrise de l'IA ; relation de luxe, inquiétude des conseillers), décision (assistant des conseillers avec validation humaine, puis extension prudente) | 0,5 |

**Réponse attendue**

*1.1 a) – Du revendeur à la place de marché : un nouveau rôle pour le système d'information*

Une **place de marché entre particuliers** est une plateforme d'intermédiation qui met en relation deux catégories d'utilisateurs, des vendeurs et des acheteurs, sans que l'opérateur soit propriétaire de ce qui est vendu ; elle se rémunère par une commission sur chaque transaction et par des services. Sa valeur croît avec le nombre d'utilisateurs de chaque côté (effets de réseau : plus d'annonces attirent plus d'acheteurs, qui attirent plus de vendeurs) et repose sur la confiance qu'elle organise entre inconnus. Chez ORSALIE, la confiance est apportée par l'authentification de l'atelier : c'est ce qui peut distinguer sa place de marché des places de marché A, B et C (0,5 pt avec la conclusion).

**Sources de valeur** (0,5 pt) : aujourd'hui, ORSALIE gagne une marge sur les articles rachetés (un tiers des articles reçus) et une commission sur le dépôt-vente, sur des articles qu'elle a elle-même reçus, photographiés, décrits et mis en vente ; sa capacité est bornée par l'atelier et le catalogue (110 000 articles reçus, 21 jours de délai). Demain, elle percevra une commission de 20 % sur des ventes entre particuliers et des revenus de services (estimation, garantie d'authenticité, revente facilitée), avec moins de 10 % d'articles en stock. La valeur ne vient plus du stock mais du **volume d'annonces** (300 000 par an), de la **conversion** des visiteurs en acheteurs et de la **confiance** ; les **données** (historique des prix et des ventes) deviennent elles-mêmes une source de valeur, puisque l'estimation proposée au vendeur en dépend. Le SI ne soutient plus la vente : il est le service vendu.

**Processus clés** (0,5 pt) : les processus actuels sont internes et largement manuels (réception, authentification, photographie, fiche, prix, stockage, expédition par le prestataire). Sur la place de marché, ils sont **déclenchés par les utilisateurs à travers le SI** : publication de l'annonce par le vendeur depuis son téléphone, estimation, vérification de l'annonce, paiement par l'acheteur, envoi par le vendeur à l'atelier, authentification, livraison, commission et reversement au vendeur, annulation et remboursement si l'article est refusé, échanges du service clients avec deux catégories de clients. Le SI doit **orchestrer** plusieurs acteurs externes (120 000 vendeurs, acheteurs de 40 pays, prestataire logistique, prestataire de paiement) et suivre chaque article unique d'un état à l'autre. L'authentification reste le processus différenciant, mais elle s'insère désormais dans un flux numérique de bout en bout.

**Dépendance au numérique** (0,5 pt) : 85 % des ventes sont déjà réalisées en ligne, plus de 90 % en 2030 ; la place de marché n'existe que par le site et l'application. Une indisponibilité arrête les ventes et entame la confiance : en novembre 2026, six heures de lenteur ont coûté 30 % des ventes du jour ; en mars 2027, les paiements en double et les fiches disparues ont fait baisser la note des avis de 4,6 à 4,1. Les volumes à absorber (quatre fois plus de vendeurs, près de trois fois plus d'articles proposés) sont hors de portée d'une application d'un seul tenant mise en ligne une fois par mois. Enfin, ORSALIE dépend aujourd'hui de places de marché qui deviendront ses concurrentes (15 % de ses ventes).

Conclusion : le SI passe d'une fonction de soutien à une **ressource stratégique au cœur du modèle d'affaires** ; sa stratégie ne peut plus être décidée au fil des demandes (annexe 1.2 C) ni réduite au choix d'un nouveau site : elle doit être alignée en permanence sur « ORSALIE 2030 » et dotée d'une gouvernance (question 1.2) et d'une architecture capables de suivre la croissance (question 1.3).

*1.1 b) – Le dispositif de veille et l'évaluation des deux technologies*

La **veille technologique** est la surveillance active et prospective des technologies et de leurs effets possibles sur le modèle économique de l'entreprise, organisée pour éclairer des décisions ; elle ne se limite pas à collecter des informations (0,5 pt avec le dispositif).

**Dispositif proposé pour ORSALIE** :
- **Objets**, reliés à « ORSALIE 2030 » : technologies de l'image et de l'IA (recherche, estimation, aide à la rédaction des annonces), paiements et confiance, architectures et services en ligne de place de marché, outils de relation client multilingue ; usages des concurrents (places de marché A, B et C, autres revendeurs) ; évolutions réglementaires du numérique (repères datés).
- **Sources** : éditeurs et fournisseurs actuels, salons et communautés professionnelles du commerce en ligne, études sectorielles, essais des services des concurrents, retours des clients et des vendeurs recueillis par le service clients et les boutiques.
- **Acteurs** : le responsable technique pour la veille technique ; les deux chefs de produit pour les usages et la concurrence ; l'analyste de données pour les usages de la donnée ; un relais par métier (atelier, catalogue, commerce, service clients) ; le (la) secrétaire général(e) consolide et porte les propositions.
- **Diffusion et décision** : une fiche d'évaluation courte par technologie (apport au modèle, maturité, ordre de grandeur des coûts, risques, conditions) ; une note trimestrielle ; décision au comité du numérique (question 1.2) : écarter, surveiller ou **expérimenter** sur un périmètre limité, avec des critères de réussite fixés à l'avance ; capitalisation des résultats des essais.

**Évaluation des deux technologies** (0,5 pt chacune) :

| | Recherche d'articles par photo | Assistant conversationnel d'IA générative |
|---|---|---|
| Nature | apprentissage automatique (reconnaissance d'images) : le modèle **classe** une image et propose des articles semblables | IA générative (grand modèle de langage) : le modèle **produit** un texte nouveau, plausible mais non garanti exact |
| Apports au modèle | trouver un article unique sans connaître son nom ; recherche indépendante de la langue, utile à 52 % de ventes à l'étranger ; préremplissage des annonces, qui facilite le dépôt pour 120 000 vendeurs et la qualité des annonces | réponse à toute heure et dans la langue du client : 72 000 messages par an (40 % de 180 000) rédigés dans une autre langue que le français, délai de 30 heures incompatible avec un client du luxe ; conseillers libérés des questions simples (suivi de commande) pour les demandes à forte valeur |
| Limites et risques | modèle exact reconnu 8 fois sur 10, 6 fois sur 10 pour les montres (25 % des ventes) ; confusion entre modèles proches, source de déception ; l'outil **n'authentifie pas** : il ne doit jamais être présenté comme une garantie ; dépendance à un fournisseur | 10 réponses erronées sur 200, dont un engagement de remboursement que l'entreprise devrait assumer ; l'outil gratuit conserve les conversations : données personnelles des clients exposées, sans contrat de sous-traitance ; information des clients qu'ils échangent avec une IA (depuis le 02/08/2026) et maîtrise de l'IA par les conseillers (depuis le 02/02/2025) ; image d'une marque de luxe, inquiétude des conseillers |
| Conditions | service de recherche séparé dans la nouvelle architecture ; essai sur la maroquinerie (55 % des ventes) avant les montres ; mesure de la conversion | outil sous contrat (sous-traitant au sens du RGPD), réponses fondées sur une base documentaire maîtrisée (conditions de vente, suivi des commandes), journalisation, transfert vers un conseiller ; formation et association des conseillers ; mention claire de l'IA |
| Décision recommandée | **expérimenter** après la séparation du service de recherche (lot 2), sur la maroquinerie, puis généraliser si la conversion progresse ; préremplissage des annonces à étudier pour le lot 1 | **expérimenter d'abord comme assistant des conseillers** : l'IA propose et traduit, le conseiller valide ; réponses automatiques limitées ensuite aux questions sans engagement (suivi de commande) ; arrêt immédiat de l'outil gratuit et du traducteur gratuit pour les messages des clients |

**Réponses tolérées**
- Place de marché présentée comme un « marché biface » ou une « plateforme multiface », si l'intermédiation, la commission et les effets de réseau sont expliqués.
- Axes de l'analyse illustrés par d'autres faits des annexes (fin des 21 jours de délai, internationalisation, données), s'ils restent rattachés aux trois axes demandés.
- Mention de la perspective de « potentiel concurrentiel » du modèle SAM (la technologie ouvre une stratégie nouvelle), si elle reste brève : aucun modèle d'alignement n'est demandé.
- Décisions inverses (assistant d'IA générative en premier, recherche par photo écartée) si elles sont justifiées par les annexes et assorties des conditions de maîtrise des risques.
- Outils de veille cités (alertes, agrégateurs, réseaux professionnels, cartographie des technologies), s'ils sont reliés aux objets et aux acteurs du cas.

**Erreurs fréquentes**
- *SI réduit à un outil ou à un nouveau site* (`ET-06` ; `JUR-G02` alignement réduit à un choix technique) — « il suffit de refaire le site » ; juste : le SI devient le cœur du modèle et sa stratégie se décide avec celle de l'entreprise.
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — « deux outils d'IA générative » ; juste : la recherche par photo classe, l'assistant produit du texte, avec des risques différents.
- *Opportunités sans risques* (`ET-19`) — assistant présenté comme une économie de conseillers ; juste : erreurs, données personnelles, transparence, relation de luxe.
- *Veille passive ou générique* (`JUR-T01` contextualiser chaque notion) — liste d'outils sans acteurs ni décision.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2024/1689 (AI Act), modifié par le règlement (UE) 2026/1744 | maîtrise de l'IA (depuis le 02/02/2025) ; information des personnes qui échangent avec une IA (depuis le 02/08/2026) | `ai_act` ; F13 § 5 | en vigueur, application échelonnée |
| Règlement (UE) 2016/679 (RGPD) | prestataire sous-traitant, contrat de sous-traitance | `rgpd` ; F15 | applicable depuis le 25/05/2018 |
| Veille technologique ; IA générative et apprentissage automatique | veille active et prospective ; typologie de l'IA | glossaire ; F01 § 0 ; F13 § 1 ; `erreurs_types.md` ET-09 | notion de cours |

---

### 1.2 – La gouvernance des choix numériques et l'organisation de l'équipe numérique (3 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité » ; `1.2.b` « Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) ».

**Annexes mobilisées** : annexes 1.2 C (décisions de la présidente seule, file de 400 demandes, temps des développeurs, rôle des chefs de produit), 1.1 (organigramme, composition de l'équipe numérique) et 1.3 (services de l'architecture envisagée).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance du SI définie (évaluer, orienter, surveiller ; distincte du management) ; deux instances du cas avec composition, fréquence et décisions | 0,5 |
| a-2 | Rôle de chaque acteur : présidente, responsables des métiers, chefs de produit, responsable technique, secrétaire général(e), équipe numérique ; point d'entrée unique des demandes | 0,5 |
| a-3 | Quatre critères d'arbitrage explicites et applicables au cas (contribution à « ORSALIE 2030 », valeur et urgence, effort au regard de la capacité, risques et dépendances avec l'architecture) | 0,5 |
| b-1 | Équipe produit définie ; comparaison argumentée avec l'organisation actuelle en file de demandes (priorités, responsabilité, relation avec les métiers, compétences) | 0,5 |
| b-2 | Répartition des dix personnes cohérente avec l'architecture et la place de marché (deux équipes produit, un socle, l'analyste en appui) | 0,5 |
| b-3 | Trois limites pour une équipe de dix personnes, chacune avec une parade | 0,5 |

**Réponse attendue**

*1.2 a) – La gouvernance des choix numériques*

La **gouvernance du système d'information** est le dispositif (instances, rôles, règles) par lequel la direction **évalue** les besoins et les options, **oriente** les choix et les priorités et **surveille** leur mise en œuvre et la performance du SI ; elle se distingue du **management**, qui planifie et exécute (0,5 pt avec les instances). Chez ORSALIE, ce dispositif n'existe pas : la présidente décide seule, au fil des demandes, et l'équipe numérique traite 900 demandes par an dans l'ordre d'arrivée.

**Deux instances** :

| Instance | Composition | Fréquence | Décisions |
|---|---|---|---|
| **Comité du numérique** | présidente (préside et arbitre en dernier ressort) ; secrétaire général(e) (prépare et anime) ; directeur commercial ; responsables de l'atelier, du catalogue et du service clients ; responsable technique ; les deux chefs de produit | mensuelle pendant la refonte, trimestrielle ensuite | orientations du numérique au service d'« ORSALIE 2030 » ; répartition de la capacité de l'équipe et des 2,4 M€ entre les produits ; lancement et arrêt des projets et des expérimentations issues de la veille ; principes d'architecture ; suivi de la refonte et des risques |
| **Revue de produit** (une par équipe produit) | chef de produit (propriétaire du produit) ; représentants des métiers concernés ; responsable technique ; développeurs | toutes les deux semaines, au rythme des itérations | ordre du carnet du produit, dans l'enveloppe fixée par le comité ; présentation de ce qui a été livré ; décisions sur les demandes nouvelles |

**Rôles** (0,5 pt) : la **présidente** fixe les orientations et arbitre les conflits entre métiers au comité, au lieu de décider demande par demande ; les **responsables des métiers** expriment leurs besoins dans le carnet, en sont responsables (valeur attendue, recette) et participent aux revues ; les **chefs de produit** deviennent propriétaires de produit : ils ordonnent le carnet selon les critères et en rendent compte ; le **responsable technique** garantit la faisabilité, l'architecture, la sécurité et la cohérence entre produits ; le (la) **secrétaire général(e)** anime la gouvernance, tient le portefeuille et les contrats, suit la dépense ; l'**équipe numérique** estime les demandes et s'engage sur ce qu'elle peut livrer. Règle commune : **toute demande passe par le carnet du produit concerné** ; plus de demande par messagerie ou dans le couloir, sauf incident.

**Quatre critères d'arbitrage** (0,5 pt) :
1. **Contribution à « ORSALIE 2030 »** : ouverture de la place de marché en 2028, ventes à l'étranger, délai de mise en vente de 7 jours, lutte contre la fraude, impact environnemental.
2. **Valeur et urgence** : effet sur les ventes, sur les clients et les vendeurs, risque d'incident ou de non-conformité (les paiements en double passent avant une amélioration de confort).
3. **Effort au regard de la capacité** : charge estimée par l'équipe, rapportée au temps disponible une fois les urgences traitées (aujourd'hui 30 % seulement du temps des développeurs va aux évolutions).
4. **Risques et dépendances** : une évolution de l'application actuelle, appelée à disparaître en 2028, n'est retenue que si elle est indispensable ; une demande qui en conditionne d'autres passe avant elles.

*1.2 b) – De la file de demandes aux équipes produit*

Une **équipe produit** est une équipe stable et pluridisciplinaire, responsable dans la durée d'un produit numérique (un ensemble cohérent de services rendus à des utilisateurs), avec un propriétaire du produit qui en ordonne le carnet selon la valeur ; elle conçoit, réalise, fait évoluer et maintient ce produit, et se mesure à ses résultats pour les utilisateurs plutôt qu'au nombre de demandes traitées (0,5 pt avec la comparaison).

| | Organisation actuelle : file de demandes | Organisation en équipes produit |
|---|---|---|
| Priorités | ordre d'arrivée ou insistance ; 400 demandes en attente, dont 150 depuis plus de six mois | carnet ordonné par le propriétaire du produit, selon les critères du comité |
| Responsabilité | personne n'est responsable d'un résultat ; les chefs de produit enregistrent et relancent | chaque équipe répond d'un produit et de ses indicateurs |
| Relation avec les métiers | client-fournisseur, par courriel ou de vive voix | métiers associés aux revues de produit et à la recette |
| Compétences | concentrées sur quelques personnes (deux développeurs connaissent le paiement) | partagées au sein de l'équipe, connaissance durable d'un domaine |
| Temps | 60 % en corrections et urgences | maintenance et évolutions du produit planifiées dans le même carnet |

**Répartition proposée** (0,5 pt), cohérente avec les services de l'annexe 1.3 :
- **Équipe « place de marché et vendeurs »** (3 personnes) : un chef de produit, propriétaire du produit, et deux développeurs ; annonces, estimation, commandes, commissions et paiements, relation avec les vendeurs ; renforcée par des développeurs de l'ESN pendant la refonte.
- **Équipe « acheteurs et catalogue »** (3 personnes) : l'autre chef de produit et deux développeurs ; catalogue, recherche, pages du site et de l'application, échanges avec l'atelier ; renforcée par l'ESN.
- **Socle** (3 personnes) : le responsable technique (architecture, cohérence entre produits, fournisseurs techniques) et les deux personnes de l'exploitation et du support (hébergement, surveillance, incidents, application actuelle jusqu'à son arrêt).
- **Appui transverse** : l'analyste de données, au service des deux équipes.

**Trois limites pour dix personnes, avec leurs parades** (0,5 pt) :
1. **Équipes trop petites et fragiles** : deux développeurs par équipe ; une absence ou un départ arrête un produit. Parade : binômes et documentation, polyvalence entre les deux équipes sur les services communs, renfort de l'ESN pendant la refonte et transfert de compétences (question 1.4).
2. **Le maintien de l'existant continue** : l'application actuelle tourne jusqu'en octobre 2028 et absorbe aujourd'hui 60 % du temps ; les urgences risquent de vider les itérations. Parade : le socle prend en charge l'application actuelle, un développeur « de garde » par itération selon un tour de rôle, une part de capacité réservée aux corrections dans chaque carnet.
3. **Cohérence entre équipes et cloisonnement** : paiements, données des clients et sécurité sont communs ; deux équipes peuvent faire des choix contraires. Parade : le responsable technique arbitre les choix d'architecture et fixe des règles communes (API, qualité, sécurité) ; une revue commune des deux carnets avant chaque comité.
Une quatrième limite peut être retenue à la place d'une des trois : la **disponibilité des métiers et des propriétaires de produit**, que la présidente ne peut pas assurer seule (deux heures par semaine) ; parade : mandat écrit des chefs de produit et temps des métiers réservé aux revues.

**Réponses tolérées**
- Instances nommées autrement (comité stratégique du numérique, comité d'arbitrage, comité d'architecture), si deux niveaux sont distingués (orientation et arbitrage d'une part, ordre du carnet d'autre part).
- Modèle cible présenté comme **bimodal** (socle stable de l'application actuelle et des logiciels de gestion, équipes produit pour la place de marché et le site), si la distinction des deux modes est expliquée et appliquée aux dix personnes.
- Référence à ISO/IEC 38500 (évaluer, diriger, surveiller) ou à COBIT 2019 (gouvernance distincte du management), si elle reste appliquée au cas.
- Répartition en deux équipes produit sans socle distinct (exploitation partagée), si le maintien de l'application actuelle et la cohérence technique sont confiés explicitement à quelqu'un.

**Erreurs fréquentes**
- *Gouvernance confondue avec le management ou réduite à un comité de projet* (`JUR-G06` vocabulaire précis) — juste : orientation, arbitrage et surveillance par la direction, avec les métiers.
- *Présidente maintenue comme seule décideuse* (`JUR-G05` analyser les déséquilibres organisationnels) — juste : elle arbitre au comité, les métiers et les propriétaires de produit décident de l'ordre du carnet.
- *Équipes produit sans limites, ou recopiées d'une grande entreprise* (`JUR-T01` contextualiser) — dix équipes de spécialistes ; juste : deux équipes de trois, un socle, des parades.
- *Critères génériques non appliqués* (`JUR-T03` analyser et argumenter) — juste : critères reliés à « ORSALIE 2030 » et aux incidents.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gouvernance des SI | évaluer, orienter, surveiller ; gouvernance et management ; comitologie | F02 § 2 et § 6 ; glossaire | notion de cours |
| ISO/IEC 38500:2024 | évaluer, diriger, surveiller (réponse tolérée) | `iso_38500_2024` ; F02 § 4 | en vigueur |
| COBIT 2019 (ISACA) | distinction gouvernance / management (réponse tolérée) | `cobit_2019` ; F02 § 3 | en vigueur |
| Organisation de la DSI | centralisée, décentralisée, fédérale, bimodale ; équipes produit | F01 § 4 | notion de cours |

---

### 1.3 – L'architecture composable et ses impacts (2 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des SI : `1.3.a` « Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) » ; `1.3.e` « Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers ». Limite : « Ne pas réduire l'urbanisation à une vision strictement technique : elle s'inscrit dans une stratégie globale. »

**Annexes mobilisées** : annexes 1.3 (principe, services envisagés, conséquences signalées) et 1.2 (limites du site actuel, objectifs 2030).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Urbanisation définie (démarche stratégique de découpage du SI en blocs faiblement couplés, reliés par des échanges maîtrisés, pour qu'il évolue avec la stratégie) ; architecture composable expliquée et opposée à l'application d'un seul tenant | 0,5 |
| a-2 | Trois apports appuyés sur les annexes (évolutions et mises en ligne séparées ; renfort ciblé lors des pics ; briques du marché et ouverture en 2028 ; migration progressive) et une limite | 0,5 |
| b-1 | Compétences et métiers de l'équipe numérique : impact et mesure | 0,5 |
| b-2 | Contrats, responsabilités en cas d'incident et répartition des données : impacts et mesures (dont ORSALIE reste responsable envers ses clients ; cohérence, données personnelles chez plusieurs sous-traitants, restitution) | 0,5 |

**Réponse attendue**

*1.3 a) – Ce qu'apporte l'architecture composable*

L'**urbanisation** du SI est une démarche stratégique qui organise le SI, par analogie avec l'urbanisme d'une ville, en blocs fonctionnels (zones, quartiers, îlots) faiblement couplés et reliés par des échanges maîtrisés, afin qu'il puisse évoluer au rythme de la stratégie sans être reconstruit en entier. L'**architecture composable** de l'annexe 1.3 en est une application : le site est découpé en services indépendants, chacun chargé d'un domaine métier (catalogue, annonces, paiements, recherche, relation client), qui échangent par des API documentées ; certains sont développés sur mesure, d'autres achetés en service en ligne, et chacun peut être modifié, mis en ligne, renforcé ou remplacé sans toucher aux autres. Elle s'oppose à l'application actuelle d'un seul tenant, où toute modification oblige à remettre en ligne l'ensemble (0,5 pt).

**Trois apports** (0,5 pt avec la limite) :
1. **Évoluer vite et sans risque global** : chaque service est mis en ligne séparément, aussi souvent que nécessaire ; une erreur sur les prix ne touche plus le paiement. Aujourd'hui, une mise en ligne par mois, et 4 incidents sur 12.
2. **Absorber les pics et la croissance de façon ciblée** : la recherche et le catalogue peuvent être renforcés pendant une opération commerciale, sans dimensionner tout le site (9 secondes d'affichage et 30 % de ventes perdues en novembre 2026 ; quatre fois plus de vendeurs et ventes à l'étranger à doubler d'ici 2030).
3. **Ouvrir la place de marché à temps en s'appuyant sur des briques du marché** : annonces, commandes et commissions reposent sur un logiciel de place de marché éprouvé ; l'équipe concentre ses développements sur ce qui distingue ORSALIE (catalogue des articles authentifiés, échanges avec l'atelier, pages en plusieurs langues).
Un quatrième apport peut remplacer l'un d'eux : la **migration progressive**, service par service, qui permet la mise en service par étapes et l'arrêt de l'application actuelle à la fin.

**Limite** : la complexité augmente (plus de pièces, d'échanges et de fournisseurs à surveiller et à payer) ; l'architecture n'est pas une fin en soi et ne vaut que si le découpage suit les processus métiers et si l'entreprise sait la gouverner.

*1.3 b) – Les impacts organisationnels et juridiques*

| Axe | Impact | Mesure |
|---|---|---|
| **Compétences et métiers de l'équipe numérique** (0,5 pt) | l'équipe ne connaît que la technologie de 2016 ; les développeurs passent d'un code unique à la conception d'API, à l'intégration de services d'éditeurs et à la surveillance d'échanges ; les chefs de produit deviennent propriétaires de produit ; le responsable technique devient architecte et pilote de fournisseurs ; les métiers (catalogue, service clients) changent d'outils | plan de montée en compétences relié à la refonte : binômes avec l'ESN, formations ciblées, responsable technique recentré sur l'architecture ; rôles et fiches de poste redéfinis |
| **Multiplication des contrats** (0,5 pt avec les deux axes suivants) | six fournisseurs techniques au lieu de trois ; abonnements révisables chaque année, mises à jour imposées, données restituées dans le format de l'éditeur ; le site n'est disponible que si chaque maillon l'est | inventaire des contrats tenu par le (la) secrétaire général(e) ; niveaux de service de chaque fournisseur cohérents avec l'objectif de disponibilité du site ; clauses de réversibilité avec restitution dans un format ouvert ; contrat de sous-traitance au sens du RGPD avec chaque prestataire qui traite des données personnelles ; revue annuelle des fournisseurs |
| **Responsabilités en cas d'incident** | une panne de paiement peut venir des pages, du logiciel de place de marché, du prestataire de paiement ou de l'hébergeur ; personne ne coordonne ; vis-à-vis du client, c'est ORSALIE qui reste responsable | un responsable de la gestion des incidents chez ORSALIE (socle), une procédure commune et une matrice de responsabilités par service et par fournisseur ; engagement contractuel de chaque fournisseur à coopérer et à fournir ses journaux ; surveillance de bout en bout du parcours d'achat |
| **Répartition des données** | un article, un vendeur ou un acheteur décrit dans plusieurs services : risque d'incohérence (article affiché disponible alors qu'il est vendu) ; données personnelles chez plusieurs sous-traitants ; restitution difficile en fin de contrat | règle selon laquelle, pour chaque donnée, un seul service fait foi et les autres s'y alimentent par API ; cartographie des données et des sous-traitants tenue à jour ; restitution des données prévue dans chaque contrat |

**Réponses tolérées**
- Architecture composable rapprochée d'une architecture orientée services ou de l'approche « meilleure solution par domaine » reliée par API, si l'indépendance des services et la remplaçabilité sont expliquées.
- Mesure de gestion des incidents formulée par référence à ITIL (gestion des incidents, accords de niveau de service), si elle désigne un responsable chez ORSALIE.
- Impact sur les métiers hors de l'équipe numérique (catalogue, service clients) développé à la place d'une partie de l'axe « compétences », s'il reste relié à l'architecture.
- Schéma simple des services et de leurs échanges à la place du texte de la sous-question a, s'il est légendé : aucun schéma détaillé n'est attendu.

**Erreurs fréquentes**
- *Urbanisation ou architecture réduite à la technique* (`ET-20` ; `JUR-G07` le pourquoi puis le comment) — description de serveurs et d'API ; juste : découpage au service des processus et de la stratégie.
- *Externalisation présentée comme un transfert de responsabilité* (F04 § 7) — « en cas d'incident, c'est l'éditeur qui répond » ; juste : ORSALIE reste responsable envers ses clients et, au sens du RGPD, responsable du traitement.
- *Impacts juridiques analysés en juriste* (limite du programme 1.4) — juste : contrats, responsabilités et sous-traitance au niveau des principes.
- *Compétences ignorées* (`JUR-D03` transformation des métiers et compétences) — juste : nouveaux savoir-faire de l'équipe et des métiers.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Urbanisation, API, spécifique et « meilleure solution par domaine » | zones, quartiers, îlots ; échanges par API ; remplaçabilité | F03 § 1, § 3 et § 4 ; `erreurs_types.md` ET-20 | notion de cours |
| Responsabilité partagée et réversibilité des services en ligne | le client reste responsable de ses données ; restitution | F03 § 5 ; F04 § 4 | notion de cours |
| ITIL (PeopleCert) | gestion des incidents, niveaux de service | `itil` ; F02 § 5 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | sous-traitants, contrats de sous-traitance | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 1.4 – Le choix et le pilotage de l'entreprise de services du numérique (2,5 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.b` « Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle » ; `1.4.d` « Méthodologie de négociation contractuelle et analyse des risques » ; `1.4.e` « Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) ». Limite : « L'analyse juridique approfondie relève du droit des contrats informatiques et est exclue du programme de l'UE. »

**Annexes mobilisées** : annexes 1.4 (objet, deux offres, risques, gouvernance à compléter, enveloppe), 1.5 (démarche hybride, carnet non stabilisé) et 1.3 (dépendance, compétences).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Comparaison des deux offres (forfait et équipe dédiée par itérations) au regard des risques relevés (périmètre, rotation, dépendance et propriété du code, transfert de compétences) et du calendrier de l'annexe 1.5 A ; calcul de tête : 1 650 k€ estimés, 250 k€ de marge sous le plafond | 0,5 |
| a-2 | Offre recommandée et justifiée par le cas | 0,5 |
| a-3 | Démarche de négociation : trois points à obtenir et deux concessions | 0,5 |
| b-1 | Instances de pilotage (stratégique, pilotage, opérationnel), clause d'audit et transfert de compétences précisés | 0,5 |
| b-2 | Deux indicateurs complets (formule, source, fréquence, cible, axe), reliés aux risques de la relation | 0,5 |

**Réponse attendue**

*1.4 a) – Comparaison, recommandation et négociation*

Calcul de tête : offre 2 = 150 + 25 × 60 = 150 + 1 500 = **1 650 k€** estimés, soit **250 k€** de marge sous le plafond de 1 900 k€ (environ quatre itérations) ; avec l'option des binômes (25 × 5 = 125 k€), **1 775 k€**, toujours sous le plafond et sous l'enveloppe de 2 000 k€. L'offre 1 affiche 1 800 k€, mais des avenants d'un tiers, comme pour la caisse en 2023, la porteraient vers 2 400 k€, au-delà de l'enveloppe (0,5 pt avec la comparaison).

| Risque relevé | Offre 1 – forfait sur périmètre figé (ESCARVÈNE Numérique) | Offre 2 – équipe dédiée par itérations, plafonnée (NORIVANE Conseil) |
|---|---|---|
| Dérive du périmètre | périmètre figé en août 2027 sur un carnet vague : chaque besoin découvert devient un avenant (800 € par jour) ; effet tunnel jusqu'aux livraisons de mai et novembre 2028 | le carnet est réordonné à chaque itération et le plafond borne la dépense ; mais aucun engagement sur ce qui sera achevé : le risque de contenu est porté par ORSALIE, qui doit piloter |
| Rotation des consultants | environ 15 % par an, équipe non nominative | environ 25 % par an, remplacement avec une semaine de préavis : perte de connaissance du code |
| Dépendance et propriété du code | code cédé, mais seulement au paiement final ; documentation à la fin | propriété du code spécifique non précisée ; composants de l'ESN sous licence : dépendance forte |
| Transfert de compétences | aucun ; équipe à Lyon | travail à Lille avec l'équipe numérique, binômes en option, arrêt possible toutes les cinq itérations |
| Calendrier | place de marché livrée en mai 2028, plus 15 jours de recette, alors que la présidente prévoit le lot 1 en avril 2028 ; reste du site en novembre 2028, après l'arrêt prévu de l'application actuelle en octobre 2028 : l'offre ne tient pas le calendrier de l'annexe 1.5 A | itérations de septembre 2027 à septembre 2028, compatibles avec les mises en service d'avril, de juin et d'octobre 2028 |

**Recommandation** : l'**offre 2**, parce qu'elle correspond à la démarche hybride décidée (cadrage au forfait, puis itérations), que les besoins de la place de marché ne sont pas stables et se préciseront avec les vendeurs invités, qu'elle permet de réordonner les priorités et de s'arrêter, qu'elle place l'ESN au contact de l'équipe numérique et qu'elle reste sous l'enveloppe. Elle exige qu'ORSALIE pilote (propriétaires de produit disponibles, question 1.5) et que ses faiblesses soient corrigées par la négociation (0,5 pt).

**Démarche de négociation** (0,5 pt) : préparer (objectifs, points non négociables, marges de concession, alternative : l'offre 1 ou une autre ESN consultée), puis négocier en échangeant des concessions contre des garanties.
- **Trois points à obtenir** : (1) la **cession à ORSALIE des droits sur le code spécifique au fur et à mesure des paiements**, le dépôt du code dans l'espace de code d'ORSALIE à chaque itération et une licence perpétuelle et transférable sur les composants de l'ESN ; (2) une **équipe nominative et stable** : remplacement seulement avec l'accord d'ORSALIE, recouvrement d'une itération aux frais de l'ESN ; (3) le **transfert de compétences inclus** (binômes et documentation intégrés à la définition de « terminé ») et un **engagement de qualité** : correction sans frais des anomalies des éléments livrés, clause d'audit.
- **Deux concessions possibles** : (1) un engagement ferme d'ORSALIE sur le premier lot (par exemple dix itérations), qui donne de la visibilité à l'ESN ; (2) le maintien du prix de 60 k€ par itération, sans remise, en échange de la stabilité de l'équipe et du transfert de compétences inclus. Autres concessions acceptées : servir de client de référence ; renoncer à des pénalités de retard, incompatibles avec un contenu d'itération fixé avec ORSALIE.

*1.4 b) – Le pilotage de la relation*

**Instances** (0,5 pt avec la clause d'audit et le transfert) :
- **Comité stratégique**, semestriel : présidente, secrétaire général(e), direction de l'ESN ; bilan de la relation, consommation du plafond, évolution du contrat, satisfaction.
- **Comité de pilotage**, mensuel : secrétaire général(e), responsable technique, propriétaires de produit, responsable d'équipe de l'ESN ; avancement par lot, indicateurs, risques, composition de l'équipe, décision de poursuivre à la fin de chaque série de cinq itérations.
- **Niveau opérationnel** : les événements des itérations (planification, revue avec acceptation par le propriétaire du produit, rétrospective), toutes les deux semaines.

**Deux indicateurs** (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux d'acceptation des éléments engagés par itération | nombre d'éléments du carnet engagés au début de l'itération et acceptés par le propriétaire du produit à la revue / nombre d'éléments engagés | outil de suivi du carnet, compte rendu de la revue | à chaque itération, consolidé chaque mois | au moins 80 % en moyenne sur les cinq dernières itérations | processus |
| Nombre d'anomalies bloquantes ou majeures découvertes après une mise en service | nombre d'anomalies bloquantes ou majeures constatées sur le site en service dans les 30 jours suivant la mise en service d'un lot, imputables aux développements livrés | outil de suivi des anomalies et des incidents d'ORSALIE | mensuelle et après chaque mise en service | aucune bloquante, au plus 3 majeures par lot | client |

Le premier compense l'absence d'engagement de l'ESN sur le contenu des itérations ; le second répond aux incidents de mars 2027.

**Clause d'audit** : droit pour ORSALIE, ou un tiers qu'elle mandate, d'auditer la prestation une fois par an et après tout incident majeur, avec un préavis court (quinze jours) : qualité et documentation du code, respect des exigences de sécurité et de la définition de « terminé », présence et qualification de l'équipe nominative, temps facturés, recours à des sous-traitants ; accès au code, aux résultats des tests et aux journaux ; plan d'actions suivi en comité de pilotage.

**Transfert de compétences** : binômes entre chaque développeur de l'ESN et un développeur d'ORSALIE ; documentation et tests exigés pour qu'un élément soit « terminé » ; part croissante des éléments réalisés par l'équipe d'ORSALIE (lot 3 conduit par elle, avec l'appui de l'ESN) ; transmission progressive du rôle de Scrum Master à une personne d'ORSALIE ; bilan des compétences acquises à chaque comité de pilotage.

**Réponses tolérées**
- Recommandation de l'offre 1 si elle est assortie d'un cahier des charges détaillé, d'un découpage en lots avec recettes intermédiaires et d'un transfert de compétences négocié, et si le risque d'avenants est traité.
- Formule mixte (forfait pour le cadrage et pour un lot bien défini, équipe dédiée pour la place de marché), si elle est justifiée par la stabilité des besoins de chaque lot.
- Autres indicateurs complets : stabilité de l'équipe, consommation du plafond rapportée à l'avancement, part des éléments réalisés en binôme.
- Pénalités ou bonus liés à la qualité (itération non facturée si la définition de « terminé » n'est pas respectée), proposés comme point de négociation.

**Erreurs fréquentes**
- *Régie, forfait et infogérance confondus* (`ET-31`) — « le forfait transfère tous les risques à l'ESN » ; juste : le forfait sur un besoin instable reporte le risque dans les avenants.
- *Indicateurs incomplets ou génériques* (`ET-18` ; `JUR-A02` justifier chaque indicateur) — juste : formule, source, fréquence, cible et axe, reliés aux risques de la relation.
- *Négociation réduite au prix* (`JUR-T03` analyser et argumenter) — juste : propriété du code, stabilité, transfert de compétences, audit.
- *Analyse juridique du contrat* (limite du programme 1.4) — juste : clauses et risques au niveau des principes.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des contrats et risques de la relation | forfait, régie ; dépendance, propriété, réversibilité | F04 § 1, § 4 et § 6 ; `erreurs_types.md` ET-31 | notion de cours |
| Gouvernance de la relation client-prestataire | comités à trois niveaux, indicateurs, clause d'audit | F04 § 5 | notion de cours |

---

### 1.5 – Le projet hybride, les exigences et la recette (3 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de SI : `1.5.b` « Méthodologies de gestion de projet (cycle en V, agile, hybride) » ; `1.5.c` « Élaboration d'un cahier des charges fonctionnel et technique » ; `1.5.f` « Mise en œuvre et contrôle du plan qualité ».

**Annexes mobilisées** : annexes 1.5 (démarche, rôles envisagés, carnet, incidents, pratiques), 1.4 (équipe de l'ESN, itérations) et 1.2 B (pic de 4 000 visiteurs).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Objet et livrables de chaque phase de la démarche hybride, avec les décisions de passage d'une phase à l'autre | 0,5 |
| a-2 | Trois responsabilités du Scrum Guide attribuées aux acteurs du cas, choix envisagés corrigés (présidente sponsor et non propriétaire du produit, responsable hiérarchique non Scrum Master) ; priorisation du carnet (but par lot, MoSCoW, valeur, risque et dépendances) | 0,5 |
| b-1 | Deux exigences vérifiables, dont une fonctionnelle, avec critère d'acceptation | 0,5 |
| b-2 | Troisième exigence ; au moins une exigence non fonctionnelle mesurable (performance) ; critères d'acceptation précis | 0,5 |
| c-1 | Plan qualité (organisation, définition de « terminé », environnement de recette, données d'essai, gestion des anomalies) ; niveaux de tests fonctionnels et responsabilités | 0,5 |
| c-2 | Quatre critères de mise en service d'un lot ; lien explicite avec les deux incidents du 7 mars 2027 | 0,5 |

**Réponse attendue**

*1.5 a) – L'organisation du projet hybride*

Une démarche **hybride** combine une partie planifiée, pour ce qui doit être stable (architecture, contrats, socle commun), et une réalisation **itérative et incrémentale**, pour ce qui se découvre en avançant (parcours des vendeurs et des acheteurs) ; elle convient à ORSALIE, qui a besoin d'une cible d'architecture et d'une date d'ouverture, mais dont les besoins de la place de marché sont encore flous (0,5 pt) :

| Phase | Objet | Livrables | Décision de passage |
|---|---|---|---|
| 1 – Cadrage et architecture (juin à août 2027) | fixer les objectifs, le périmètre, l'architecture cible et les choix des services en ligne | note de cadrage avec objectifs mesurables ; architecture cible et règles d'échange entre services ; contrats des éditeurs ; **plan qualité** ; premier carnet ordonné avec un but par lot ; définition de « terminé » ; environnement de recette | comité de pilotage de fin de cadrage (présidente) : lancement de la phase 2 |
| 2 – Itérations de deux semaines (septembre 2027 à septembre 2028) | réaliser les lots 1, 2 et 3 par incréments utilisables | à chaque itération, un incrément accepté par le propriétaire du produit ; recette de fin de lot | revue de fin de lot : lot prêt à la mise en service |
| 3 – Mise en service par étapes (avril, juin, octobre 2028) | ouvrir chaque lot à un public limité, puis à tous | procès-verbal de recette, décision de mise en service, retour d'expérience ; arrêt de l'application actuelle en octobre 2028 | décision de mise en service selon les critères de la question 1.5 c |

**Responsabilités du Scrum Guide** (0,5 pt avec la priorisation) :
- **Product Owner** (propriétaire du produit) : une seule personne par produit, disponible et mandatée, qui ordonne le carnet et accepte les éléments. Ce ne peut pas être la présidente, qui n'a que deux heures par semaine : elle reste **sponsor**, préside le comité de pilotage et participe aux revues de fin de lot. Les deux **chefs de produit**, mandatés par écrit, deviennent propriétaires des produits « place de marché et vendeurs » et « acheteurs et catalogue » (question 1.2).
- **Scrum Master** : garant du cadre, facilitateur, sans autorité hiérarchique sur l'équipe. M. LAMBRESCOT ne peut pas l'être tout en restant responsable hiérarchique des développeurs et seul décideur des mises en ligne. La **responsable d'équipe de l'ESN**, qui connaît le cadre, peut tenir ce rôle pendant la refonte, avec une transmission progressive à une personne d'ORSALIE ; M. LAMBRESCOT garde l'architecture et la cohérence technique.
- **Developers** : les développeurs d'ORSALIE et de l'ESN et la testeuse, répartis en deux équipes de dix personnes au plus, qui s'organisent eux-mêmes pour livrer l'incrément.

**Priorisation du carnet** : un **but du produit** par lot (lot 1 : « en avril 2028, 2 000 vendeurs invités vendent un article authentifié de bout en bout ») ; méthode **MoSCoW** (indispensable, important, souhaitable, exclu pour ce lot), complétée par la valeur pour « ORSALIE 2030 », le risque (paiement d'abord) et les dépendances (le service d'annonces avant l'estimation) ; besoins mélangés découpés en éléments distincts (B5 contient trois besoins de trois services différents) ; carnet réordonné à chaque revue.

*1.5 b) – Trois exigences vérifiables*

Une exigence est **vérifiable** lorsqu'elle est précise, mesurable et associée à un critère d'acceptation qui permet de dire, sans discussion, si elle est satisfaite (0,5 pt par paire d'exigences ; au moins une exigence non fonctionnelle) :

| Besoin | Exigence vérifiable | Type | Critère d'acceptation |
|---|---|---|---|
| B1 | Les pages d'article et les résultats de recherche s'affichent en moins de 2 secondes pour 95 % des consultations, avec 8 000 visiteurs simultanés (le double du pic de novembre 2026) | non fonctionnelle (performance) | mesure sur l'environnement de recette, en simulant le trafic de pointe avant chaque mise en service, puis suivi sur le site en service lors de la première opération commerciale |
| B2 | En tant que vendeur particulier, je publie une annonce depuis l'application de mon téléphone (au moins quatre photos, catégorie, marque, état, prix) ; l'annonce est enregistrée « en attente de vérification » et je reçois une confirmation | fonctionnelle (récit d'utilisateur) | étant donné un vendeur connecté, quand il valide une annonce complète, alors elle apparaît « en attente de vérification » et une confirmation lui est envoyée ; une annonce incomplète est refusée avec un message indiquant le champ manquant ; sur un panel de dix vendeurs particuliers associés à la recette, neuf y parviennent en moins de dix minutes |
| B7 | Une commande ne donne lieu qu'à un seul débit : une seconde demande de paiement pour la même commande est refusée, y compris en cas de double validation, de retour en arrière du navigateur ou de coupure de connexion | fonctionnelle (règle de gestion) | les trois situations jouées dans l'environnement d'essai du prestataire de paiement ne produisent aucun double débit ; le rapprochement quotidien entre commandes et débits ne fait apparaître aucun écart pendant le premier mois |

*1.5 c) – Le plan qualité et la stratégie de recette*

Le **plan qualité** (plan d'assurance qualité) fixe, dès le cadrage, l'organisation, les règles et les contrôles qui garantissent que le produit livré répond aux exigences : rôles, définition de « terminé », gestion des versions et des changements, plan de tests, critères d'acceptation, traitement des anomalies, revues. La **recette** vérifie, avant la mise en service, que ce qui est livré est conforme aux exigences (0,5 pt avec les niveaux de tests et les responsabilités) :
- **Organisation** : un environnement de recette semblable au site en service, alimenté par des **données fictives ou rendues anonymes** et relié aux environnements d'essai du prestataire de paiement et des éditeurs ; anomalies suivies dans un outil partagé et classées par gravité (bloquante, majeure, mineure) ; définition de « terminé » commune à ORSALIE et à l'ESN (critères d'acceptation vérifiés, tests passés, code relu, documentation à jour, élément installé sur l'environnement de recette) ; revue de fin d'itération et revue de fin de lot.
- **Niveaux de tests fonctionnels** : (1) vérification de chaque élément contre ses critères d'acceptation, à chaque itération ; (2) tests d'intégration entre services et avec les fournisseurs (prestataire de paiement, logiciel de place de marché, logiciel de l'atelier) ; (3) **tests de non-régression** sur les parcours critiques (paiement, commande, fiche d'article, publication d'une annonce), rejoués avant chaque mise en ligne ; (4) **recette fonctionnelle de bout en bout** par les utilisateurs clés sur des scénarios métier (achat depuis l'étranger, dépôt d'une annonce, authentification refusée et remboursement, mise à jour des prix) ; (5) **pilote** avec les 2 000 vendeurs invités, puis vérification après mise en service.
- **Responsabilités** : l'ESN et les développeurs réalisent les tests de leurs éléments et les tests d'intégration ; la testeuse de l'ESN prépare les cas de test avec les utilisateurs clés ; les **utilisateurs clés** (commerce, catalogue, atelier, service clients, finances pour les paiements) exécutent la recette ; le **propriétaire du produit** prononce l'acceptation ; le comité de pilotage, présidé par la présidente, décide la mise en service sur avis du responsable technique ; le (la) secrétaire général(e) veille à l'application du plan qualité.

**Quatre critères de mise en service d'un lot** (0,5 pt) :
1. Aucune anomalie bloquante ouverte, et aucune anomalie majeure sans solution de contournement acceptée par le propriétaire du produit.
2. Tous les scénarios critiques et les tests de non-régression passés, y compris avec l'environnement d'essai du prestataire de paiement ; exigence de performance vérifiée.
3. Procès-verbal de recette signé par le propriétaire du produit et par les utilisateurs clés concernés.
4. Procédure de retour à la version précédente écrite et essayée, assistance renforcée prévue les premiers jours, mise en ligne programmée hors d'une opération commerciale et annoncée au service clients.

**Lien avec les incidents** : les **paiements en double** auraient été évités par les tests d'intégration avec l'environnement d'essai du prestataire de paiement, par le test de non-régression du paiement et par l'exigence B7 ; les **fiches disparues** auraient été détectées par la recette de la mise à jour des prix par le catalogue, sur une copie des fiches, et par une vérification après mise en ligne ; le retour à la version précédente aurait pris quelques minutes au lieu de 6 heures avec une procédure essayée.

**Réponses tolérées**
- Exigence non fonctionnelle de sécurité (authentification renforcée des vendeurs, chiffrement des échanges), de langue (B6 : parcours d'achat complet disponible dans une liste de langues fixée) ou d'accessibilité, si elle est mesurable et assortie d'un critère d'acceptation ; exigence B3 réécrite (liste quotidienne des articles vendus à recevoir par l'atelier, avec leur date d'arrivée prévue).
- Critères d'acceptation rédigés en scénarios « étant donné, quand, alors » ou en liste de contrôles.
- Scrum Master interne désigné dès le début (chef de produit exclu), si l'absence de lien hiérarchique et la formation sont prévues.
- Recette présentée selon les niveaux du cycle en V (tests unitaires, intégration, recette, vérification de service régulier), si elle est intégrée aux itérations et aux lots.

**Erreurs fréquentes**
- *Agile présenté comme l'absence de méthode ou de cahier des charges* (`ET-32`) — « en agile, on n'écrit pas d'exigences » ; juste : carnet ordonné, critères d'acceptation, définition de « terminé ».
- *Rôles Scrum faux* (F05 § 9) — présidente propriétaire du produit sans disponibilité, Scrum Master responsable hiérarchique ; juste : un propriétaire disponible par produit, un Scrum Master facilitateur.
- *Exigences non vérifiables* (F05 § 3 : le jury attend des exigences vérifiables, avec leur critère de recette) — « le site doit être rapide » ; juste : seuil, condition de mesure, critère d'acceptation.
- *Recette laissée aux seuls développeurs ou réduite à un essai final* (`JUR-P03` diagnostiquer les erreurs de gestion de projet par étapes) — juste : niveaux de tests, utilisateurs clés, critères de mise en service tirés des incidents.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| The Scrum Guide (Schwaber et Sutherland), novembre 2020 | Product Owner, Scrum Master, Developers ; équipe de dix personnes au plus ; Product Goal, Definition of Done | `scrum_guide_2020` ; F05 § 2.2 | en vigueur |
| Démarche hybride, cahier des charges, MoSCoW | cadrage planifié et itérations ; exigences vérifiables | F05 § 2.3 et § 3 | notion de cours |
| Plan qualité, recette, mise en production | plan d'assurance qualité, recette fonctionnelle, procès-verbal, retour arrière | F05 § 6 | notion de cours |
