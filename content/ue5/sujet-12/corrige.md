# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 12

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Préparer la refonte du site et l'ouverture de la place de marché | 14 | 1.1 à 1.5 | `exercices/ex34_place_marche_refonte_agile` |
| 2 – Organiser et exploiter les données des articles et des ventes | 13 | 2.1 à 2.4 | `exercices/ex35_donnees_articles_delais_vente` |
| 3 – Sécuriser les transactions et mesurer l'impact environnemental du numérique | 13 | 3.1 à 3.5 | `exercices/ex36_sequestre_fraude_impact_site` |
| **Total** | **40** | | |

---

## DOSSIER 1 – PRÉPARER LA REFONTE DU SITE ET L'OUVERTURE DE LA PLACE DE MARCHÉ (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES ARTICLES ET DES VENTES (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le référentiel des articles et les échanges avec les places de marché | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) | 4 |
| 2.2 Les délais de vente, les retours et les outils d'analyse | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 4,5 |
| 2.3 La gouvernance des données | `2.3.a` Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques ; `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) | 2 |
| 2.4 Le projet de studio de mise en ligne | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI | 2,5 |
| **Dossier 2 – Organiser et exploiter les données des articles et des ventes** |  | **13** |

Répartition indicative : connaissances (données de référence, dictionnaire de données, interopérabilité, chaîne de traitement, analyses descriptive et exploratoire, gouvernance des données et ses rôles, DAMA-DMBOK, retour sur investissement et délai de récupération) environ 3,5 points (item 2.1 b-1 et la moitié des items 2.1 a-1, 2.1 c-1, 2.2 a-1, 2.2 a-2, 2.3-1, 2.3-4 et 2.4 a-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 9,5 points, soit environ 73 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le référentiel des articles et les échanges avec les places de marché (4 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) ». L'approfondissement technique des échanges est exclu ; l'interopérabilité est traitée sur les plans technique et organisationnel. Aucun modèle des données n'est demandé.

**Annexes mobilisées** : annexes 1.1 (modèle d'activité, canaux de vente, système d'information, organigramme), 2.1 (trois descriptions de l'article, constats de mars 2027, témoignages), 2.2 (ventes annulées par canal) et 2.5 (principes du RGPD, DAMA-DMBOK).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Données de référence définies ; référentiel des articles, seule source qui fait foi pour la description de chaque article, alimentant le site, l'application, les boutiques et les places de marché ; justifié par deux constats chiffrés de l'annexe 2.1 (trois descriptions, 2 300 libellés pour 400 marques, 100 fiches sur 500 à l'état trop favorable, 900 ventes en double) | 0,5 |
| a-2 | Identifiant de l'article attribué une seule fois, non signifiant, stable même après un retour, jamais réattribué, avec les autres numéros rattachés ; trois attributs normalisés (marque et modèle, état, et un autre attribut à liste de valeurs) avec leur règle | 0,5 |
| a-3 | Résultat de l'authentification enregistré dans le référentiel et rattaché à l'article (statut, auteur, date, observations, photographies de contrôle) ; étapes du cycle de l'article sous forme de statuts, avec le cycle de la future place de marché (annonce, vente, authentification, livraison) | 0,5 |
| b-1 | Dictionnaire de données défini (description partagée de chaque donnée : nom, définition, format, domaine de valeurs, règle, source, propriétaire, règle de qualité) et distingué d'un modèle des données | 0,5 |
| b-2 | « État de l'article » et « article disponible » : définition commune, règle, propriétaire, règle de qualité | 0,5 |
| b-3 | « Date de mise en vente » : définition commune, règle, propriétaire, règle de qualité ; cohérence d'ensemble des trois fiches | 0,5 |
| c-1 | Interopérabilité définie, avec ses plans ; API et format ouvert définis ; interface de programmation avec A et C, fichier en format ouvert toutes les heures avec B, disponibilité tenue par le référentiel et transmise à chaque réservation ou vente | 0,5 |
| c-2 | Deux conditions organisationnelles (correspondance des catégories et des échelles d'état, convention d'échange et suivi des rejets, données des vendeurs limitées au nécessaire, règle de retrait des articles de valeur) | 0,5 |

**Réponse attendue**

*2.1 a) – Le référentiel des articles, l'identifiant, les attributs, l'authentification et le cycle de l'article*

**Le constat** : un article unique est décrit trois fois, par trois équipes, sous trois numéros (annexe 2.1 A). La ressaisie produit des écarts : 2 300 libellés de marque pour environ 400 marques réelles, un même modèle de sac sous 17 libellés, une fiche sur cinq (100 sur 500) qui affiche un état plus favorable que celui noté par l'atelier. Le résultat de l'authentification, cœur du métier, vit dans un tableur déjà écrasé une fois. La disponibilité est transmise une fois par nuit, d'où 900 articles vendus deux fois en 2026.

**Le référentiel des articles** (0,5 pt) : les **données de référence** sont les données partagées et stables dont plusieurs processus ont besoin ; elles sont gérées dans un **référentiel unique**, qui fait foi (F07 § 1). Pour ORSALIE :
- un **référentiel des articles** devient la **seule source** de la description de chaque article. Il est créé à la réception, enrichi par l'atelier puis par le catalogue, et il **alimente** sans ressaisie le site et l'application, le logiciel de caisse et les annonces des places de marché ;
- une donnée est saisie **une fois, là où elle naît** : la marque et le modèle à la réception, l'état et l'authentification à l'atelier, la description, les photographies et le prix au catalogue ; une correction faite dans le référentiel se propage à tous les canaux ;
- le référentiel peut être porté par le logiciel des dépôts, à faire évoluer, ou par le futur catalogue du site refondu : l'essentiel est qu'il n'y en ait **qu'un**, et que les autres logiciels le consultent au lieu de garder leur propre copie modifiable.

**L'identifiant et trois attributs normalisés** (0,5 pt) :
- l'**identifiant de l'article** est attribué **une seule fois**, à la première réception (ou, demain, à la publication de l'annonce par le vendeur). Il est **unique**, **non signifiant** (ni marque, ni date, ni code de boutique) et **stable** : un article retourné par un client garde son identifiant, ses photographies et son historique, au lieu de recevoir un nouveau numéro de réception (annexe 2.1 B). Il n'est **jamais réattribué**. Le numéro de réception de chaque arrivée, la référence du site et les références des places de marché A, B et C sont conservés comme **références rattachées** ;
- trois **attributs normalisés**, parmi :
  1. **marque et modèle**, choisis dans une **liste de référence** des marques et des modèles tenue par le catalogue avec l'atelier, au lieu du texte libre : une nouvelle marque est créée après vérification, et les 2 300 libellés sont ramenés aux 400 marques réelles ;
  2. **état**, noté sur **une seule échelle** commune à l'atelier et au catalogue, avec une table de correspondance vers les échelles des places de marché (question b) ;
  3. **catégorie, matière et couleur**, choisies dans des listes de valeurs, et **dimensions** dans un format fixé (unité, ordre longueur × hauteur × profondeur), pour réduire les retours pour fiche inexacte.

**L'authentification et le cycle de l'article** (0,5 pt) :
- le **résultat de l'authentification** est enregistré **dans le référentiel**, rattaché à l'identifiant : statut (authentique, refusé, second avis), authentificateur, date, observations et photographies de contrôle. Le tableur disparaît ; la mention « authentifié par ORSALIE » n'est affichée que si le statut le permet, et le service clients retrouve la preuve en un clic (M. BELLASTRE). Ce résultat est une donnée **sensible** : il n'est modifiable que par l'atelier, et chaque modification est tracée ;
- le **cycle de l'article** est décrit par des **statuts** successifs : reçu (ou annoncé) ; en attente d'authentification ; authentifié ou refusé (rendu au vendeur) ; en remise en état ; en attente de photographie ; en vente ; réservé (dans un panier, en boutique ou sur une place de marché) ; vendu ; retourné, puis remis en vente sous le même identifiant ou rendu au vendeur. Chaque changement de statut est **daté** : on mesure ainsi le délai de chaque étape (annexe 2.2 D) et la disponibilité réelle ;
- **demain**, sur la place de marché, le cycle s'inverse : annonce publiée par le vendeur, vente, envoi à l'atelier, authentification, livraison à l'acheteur, ou annulation si l'article n'est pas authentique ou non conforme. Le référentiel doit accepter les deux cycles, avec le même identifiant et les mêmes listes de marques et d'états.

*2.1 b) – Un extrait de dictionnaire de données*

Un **dictionnaire de données** décrit chaque donnée de manière partagée : nom, définition, format et domaine de valeurs, règle d'enregistrement ou de calcul, source, propriétaire, sensibilité et règles de qualité (0,5 pt). Il fixe le **sens** des données, et non leur structure : ce n'est pas un modèle conceptuel (F07 § 1 et 8.3). Il met fin, ici, aux trois sens de chaque mot relevés dans les témoignages de l'annexe 2.1 C, qui rendent les chiffres incomparables d'un canal à l'autre.

| Notion | Définition commune | Règle d'enregistrement ou de calcul | Propriétaire | Règle de qualité |
|---|---|---|---|---|
| **État de l'article** (0,5 pt avec la suivante) | appréciation de l'usure et des défauts de l'article, sur une échelle unique (par exemple cinq niveaux, du « neuf » à « état correct »), chaque niveau étant décrit par des critères observables (rayures, coins, fonctionnement) | noté par l'authentificateur à l'issue de l'authentification, puis mis à jour après la remise en état ; le catalogue le reprend sans le modifier ; une table de correspondance traduit l'échelle unique dans celle de chaque place de marché | responsable de l'atelier | aucun article en vente sans état noté ; état affiché identique à l'état enregistré par l'atelier, contrôlé chaque mois sur un échantillon (100 fiches sur 500 en écart en mars 2027) |
| **Article disponible** | article authentifié, en vente, ni réservé ni vendu, qui peut être acheté immédiatement sur tous les canaux | statut « en vente » dans le référentiel ; il passe à « réservé » dès la mise au panier, la vente en boutique ou la commande sur une place de marché, et cette information est transmise à tous les canaux ; un article en attente d'authentification ou de photographie est « en préparation », non disponible | directeur commercial | aucun article vendu deux fois : les ventes annulées faute de stock sont suivies chaque semaine (900 en 2026) ; écart entre le nombre d'articles disponibles du référentiel et celui de chaque canal contrôlé chaque jour |
| **Date de mise en vente** (0,5 pt) | date à laquelle l'article devient disponible pour la première fois, sur le site et l'application | horodatage automatique du passage au statut « en vente » dans le référentiel, et non saisie manuelle ; la date de publication sur chaque place de marché est enregistrée à part, comme une donnée distincte | responsable du catalogue | date toujours postérieure à la date de réception et à la date d'authentification ; écart entre la mise en vente et la publication sur chaque place de marché suivi (de un à dix jours en 2026) |

Les **propriétaires** sont des responsables métiers, et non l'équipe numérique : ils arbitrent la définition et la qualité attendue. Des **intendants** (un rédacteur référent du catalogue, un authentificateur référent) corrigent les anomalies au quotidien (F07 § 8.1). La date de mise en vente fixe aussi le point de départ commun du délai de mise en vente (depuis la réception) et du délai de vente (jusqu'à la vente), utilisés dans l'annexe 2.2.

*2.1 c) – Les échanges avec les places de marché*

L'**interopérabilité** est la capacité de systèmes hétérogènes, appartenant le cas échéant à des organisations différentes, à échanger des données et à les utiliser sans ressaisie. Elle a un plan **technique** (moyen d'échange : interface de programmation, dépôt de fichiers), un plan **syntaxique** (format), un plan **sémantique** (même sens des données : catégories, échelles d'état) et un plan **organisationnel** (qui transmet quoi, quand, sous quelle responsabilité). Une **interface de programmation (API)** permet à un logiciel d'interroger ou de mettre à jour un autre logiciel automatiquement, à chaque événement. Un **format ouvert** est un format dont la spécification est publique et que tout logiciel peut lire (F07 § 7).

**Les solutions d'échange** (0,5 pt, avec la définition) :
- avec les **places de marché A et C** : l'**interface de programmation** qu'elles proposent, et qu'ORSALIE n'utilise pas (annexe 2.1 B). L'annonce est publiée dès la mise en vente, à partir du référentiel, et la **disponibilité est mise à jour à chaque événement** : dès qu'un article est réservé ou vendu sur un canal, il est retiré des autres en quelques secondes. Les commandes reçues des places de marché réservent l'article dans le référentiel de la même façon ;
- avec la **place de marché B**, qui n'accepte que des fichiers : un **fichier en format ouvert** produit automatiquement par le référentiel et déposé **toutes les heures**, au lieu d'une fois par nuit ; comme un délai d'une heure laisse subsister un risque, les articles de forte valeur ou très demandés peuvent n'être proposés sur B qu'après un délai, ou retirés dès leur mise au panier sur un autre canal ;
- les **boutiques** enregistrent la vente dans le logiciel de caisse relié au référentiel, et non plus par messagerie ;
- dans tous les cas, le **référentiel** est la seule source de la disponibilité ; les connecteurs ne font que la transmettre.

**Deux conditions organisationnelles** (0,5 pt), parmi :
- une **table de correspondance** des catégories et des échelles d'état de chaque place de marché, tenue par le catalogue (plan sémantique) : c'est elle qui supprime les compléments saisis à la main ;
- une **convention d'échange** avec chaque place de marché (données transmises, fréquence, délais de prise en compte, interlocuteurs) et un **suivi des échanges** : alerte en cas d'échec d'un envoi, rejets traités le jour même par un intendant désigné, ventes annulées suivies chaque semaine (600 sur les places de marché en 2026, et une suspension de huit jours de la place de marché B) ;
- des **données limitées au nécessaire** : le nom et la commune du vendeur particulier ne sont plus transmis à la place de marché B, qui ne les utilise pas (principe de minimisation du RGPD, annexe 2.5), et les données transmises sont encadrées par les conditions conclues avec chaque place de marché ;
- une **règle de priorité** des canaux, décidée par le directeur commercial (articles réservés au site et aux boutiques, délai avant publication sur B).

**Réponses tolérées**
- Référentiel présenté comme une démarche de gestion des données de référence, si le terme est écrit en toutes lettres et si une seule source de description est retenue.
- Autres attributs normalisés justifiés par l'annexe 2.1 (photographies rattachées à l'identifiant, prix, dimensions), si chacun porte une règle.
- Autres définitions des trois notions, si elles sont uniques pour toute l'entreprise, mesurables, et accompagnées d'une règle et d'un propriétaire ; propriétaire unique (la responsable du catalogue) pour les trois notions, s'il est justifié.
- Fichier structuré en XML ou à séparateurs cité pour la place de marché B ; synchronisation par API proposée aussi pour B à terme, si la place de marché l'ouvre.
- Plans de l'interopérabilité présentés en deux ou trois niveaux (le plan syntaxique rattaché au plan technique).

**Erreurs fréquentes**
- *Modèle des données hors attente* (`JUR-T06`, `ET-23`) — entités, associations et cardinalités dessinées au lieu de règles d'organisation, alors que la question les exclut.
- *Identifiant signifiant ou instable* — numéro de réception, marque ou date retenus comme identifiant : l'article retourné change encore de numéro et perd son historique.
- *Sigle ambigu* (`ET-13`) — « mettre en place un MDM » sans préciser qu'il s'agit de la gestion des données de référence.
- *Interopérabilité seulement technique* (`ET-36`) — interface de programmation proposée partout, sans correspondance des catégories et des états, sans suivi ni responsable.
- *Détail technique hors attente* (`JUR-T07`) — description des formats d'API, des méthodes d'appel ou de l'authentification des échanges.
- *Morceau de cours* (`JUR-T01`) — définitions du référentiel, du dictionnaire ou de l'interopérabilité sans les articles, les trois notions et les trois places de marché.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines données de référence, métadonnées, qualité, intégration et interopérabilité | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | principe de minimisation appliqué aux données des vendeurs transmises (annexe 2.5) | `rgpd` / F15 § 0 | en vigueur |
| Données de référence, identifiant, dictionnaire de données, dimensions de la qualité, propriétaire et intendant, plans de l'interopérabilité, API et formats ouverts | définitions et principes | F07 § 1, 7, 8.1 et 8.3 | notion de cours |

---

### 2.2 – Les délais de vente, les retours et les outils d'analyse (4,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.d` « Outils décisionnels : Excel avancé, Power BI, Tableau, etc. » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Aucun calcul statistique ni aucune manipulation d'outil ; lecture critique des biais, reliée à la stratégie.

**Annexes mobilisées** : annexes 1.1 (canaux, catégories, délai de 21 jours, effectif de l'équipe numérique, dépenses du numérique), 2.1 (définitions divergentes, ventes en double), 2.2 (tableaux par catégorie et par canal, motifs de retour, décomposition du délai, question de la présidente) et 2.3 (rapport mensuel, attentes, deux options).

**Barème indicatif (4,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de traitement appliquée aux sources d'ORSALIE : collecte, nettoyage, structuration autour de l'identifiant et des définitions communes, analyse, restitution ; rôles | 0,5 |
| a-2 | Analyses descriptive et exploratoire définies et distinguées, prédictive écartée ; combinaison justifiée par l'annexe 2.2 (décrire où passent le temps et l'argent, puis explorer les causes) | 0,5 |
| b-1 | Premier constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-2 | Deuxième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-3 | Troisième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| c-1 | Réponse à la présidente, de tête : 11 jours d'attente sur 21, montres ; retours pour fiche inexacte (3 000 × 40 € = 120 k€, sur 360 k€ de retours), 900 ventes en double dont 600 sur les places de marché, montres invendues ; conséquence pour l'objectif de 7 jours | 0,5 |
| c-2 | Deux représentations adaptées, chacune justifiée par son message et assortie d'un piège évité | 0,5 |
| d-1 | Comparaison des deux options selon quatre critères, avec le coût de tête sur trois ans (150 k€ et 60 k€) | 0,5 |
| d-2 | Recommandation argumentée (option 1) et deux conditions de réussite ; informatique décisionnelle présentée comme une démarche et non comme un outil | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de traitement et la méthode d'analyse*

**La chaîne de traitement** (0,5 pt) transforme des données brutes en décisions (F08 § 1) :
- **collecte** : extraction automatique, chaque nuit, des données du référentiel des articles (ou, en attendant, du logiciel des dépôts et du tableur de l'atelier), du site, du logiciel de caisse, des places de marché A, B et C et de l'outil de gestion de la relation client (motifs de retour) ;
- **nettoyage** : rapprochement des numéros de réception d'un même article, correction des dates de réception saisies en retard, classement des motifs de retour saisis en texte libre, repérage des mois manquants (place de marché C avant avril, boutique de Paris en août), des doublons et des valeurs aberrantes, consignés dans un journal des rejets et corrigés à la source ;
- **structuration** : chargement dans une base d'analyse commune, organisée par article, date, catégorie, canal et pays, selon les définitions du dictionnaire (question 2.1 b) : une seule définition de la date de mise en vente, du retour ou du montant des ventes, au lieu des trois montants de mars 2027 (3,8, 4,0 et 4,2 M€) ;
- **analyse**, puis **restitution** dans des tableaux de bord adaptés à chaque destinataire (présidente, commerce, catalogue, atelier), avec des alertes, et **décision** suivie d'actions.

L'analyste de données conçoit et documente la chaîne ; les propriétaires des données valident les définitions et la qualité ; les règles de préparation, aujourd'hui connues d'elle seule, sont écrites.

**La méthode** (0,5 pt) : l'**analyse descriptive** résume ce qui s'est passé (volumes, délais moyens, répartitions, écarts à une cible) ; l'**analyse exploratoire** recherche, sans hypothèse arrêtée à l'avance, des croisements, des profils et des valeurs atypiques qui orientent vers des explications ; l'**analyse prédictive** estime ce qui va se passer (F08 § 2). ORSALIE combinera :
- une **analyse descriptive d'abord**, parce que la question de la présidente est descriptive (où, combien) et que les chiffres doivent d'abord être fiabilisés : délai par étape, retours par motif, ventes annulées par canal ;
- puis une **analyse exploratoire** pour comprendre les causes : croiser les délais des montres avec la charge de l'horloger, les retours pour fiche inexacte avec les écarts d'état relevés par le contrôle de mars 2027, les ventes annulées avec l'heure de la vente et le canal ;
- une analyse **prédictive** (prévoir les ventes d'un article) serait prématurée : l'historique est court, et les définitions changent selon les canaux.

*2.2 b) – Trois constats argumentés et leurs précautions de lecture*

Trois constats parmi les suivants (0,5 pt chacun : le fait chiffré, son interprétation au regard du plan « ORSALIE 2030 », la précaution de lecture) :

1. **Plus de la moitié du délai de mise en vente est de l'attente.** Sur 21 jours, 11 sont passés à attendre : 6 avant l'authentification, 5 avant la photographie (annexe 2.2 D). Le travail lui-même (authentification, photographie, fiche, prix) prend 4 jours. Le délai tient donc d'abord à la capacité et à l'organisation des files d'attente de l'atelier et du catalogue. L'objectif de 7 jours ne sera pas atteint en accélérant seulement le travail. *Précaution* : l'échantillon porte sur 1 000 articles reçus en février 2027, un seul mois, qui n'est pas forcément représentatif (saisonnalité des dépôts). De plus, la date de réception est parfois saisie plusieurs jours après l'arrivée du colis : le délai réel est plutôt sous-estimé.
2. **Les montres sont la catégorie la plus lente à chaque étape.** Il leur faut 35 jours pour être mises en vente (contre 17 pour la maroquinerie) et 60 jours pour être vendues, et 25 % sont encore invendues 90 jours après leur mise en vente. Un seul horloger les authentifie et contrôle leur fonctionnement (Mme VERCHAMP) ; le défaut de fonctionnement est leur premier motif de retour. *Précaution* : un goulet d'étranglement chez l'horloger est une explication plausible, non démontrée ; le prix plus élevé des montres ou leur clientèle peuvent aussi expliquer une vente plus lente (corrélation n'est pas causalité). La part des invendus ne porte que sur les articles mis en vente avant le 1er octobre 2026.
3. **Un tiers des retours vient d'une fiche inexacte.** 3 000 retours sur 9 000 ont pour motif un article différent de la fiche ; c'est le premier motif de la maroquinerie, qui a le taux de retour le plus élevé (13 %). Le contrôle de mars 2027 va dans le même sens : une fiche sur cinq affiche un état plus favorable que celui noté par l'atelier (annexe 2.1 B). La qualité des données coûte donc directement de l'argent et la confiance des clients. *Précaution* : jusqu'en juin 2026, les motifs étaient saisis en texte libre, puis classés à la main par l'analyste ; le total de 9 000 mêle des retours effectifs et les réclamations comptées comme retours par les places de marché.
4. **Les places de marché concentrent les ventes en double.** Elles représentent un sixième des articles vendus (16 000 sur 96 000), mais deux tiers des ventes annulées (600 sur 900), parce que leur disponibilité n'est mise à jour qu'une fois par nuit ; la suspension de huit jours par la place de marché B en est la conséquence. *Précaution* : leur taux de retour (15 %) et leur délai de vente (20 jours) ne sont pas comparables à ceux du site, car ils ne sont pas définis de la même façon (réclamations comptées comme retours, délai compté à partir de la publication de l'annonce), et la place de marché C n'a transmis que neuf mois de données.
5. **Les données des boutiques ne permettent aucune conclusion.** Les échanges ne sont pas enregistrés, et les ventes de la boutique de Paris manquent pour août 2026. *Précaution* : on ne compare pas le délai de vente des boutiques (50 jours) à celui des autres canaux tant que les données sont incomplètes.

*2.2 c) – La réponse à la présidente et deux représentations*

**La réponse à Mme VELDRANE** (0,5 pt), de tête :
- **le temps** se perd dans les **files d'attente** : 11 jours sur 21, avant l'authentification et avant la photographie. Les **montres** cumulent 35 jours avant la mise en vente et 60 jours avant la vente, soit plus de trois mois de la réception à la vente. Pour atteindre 7 jours, il faut supprimer l'essentiel de ces 11 jours d'attente : la capacité de l'atelier, celle de l'horlogerie et celle du catalogue sont les leviers ;
- **l'argent** se perd :
  - dans les **retours** : 9 000 retours à environ 40 € coûtent environ 360 k€ par an ; ceux qui sont dus à une **fiche inexacte** (3 000) coûtent environ 120 k€, sans compter les ventes perdues, et ils sont évitables par la qualité des données ;
  - dans les **ventes en double** : 900 ventes annulées, dont 600 sur les places de marché, avec des pénalités, une mauvaise note et huit jours de suspension de la place de marché B ;
  - dans les **montres invendues** : un quart des montres reste invendu après 90 jours, soit près de 4 000 articles à l'échelle de l'année, dont une partie a été rachetée par ORSALIE et immobilise sa trésorerie.

Réponse : « Nous perdons surtout du temps dans les files d'attente de l'atelier et du catalogue, et sur les montres ; nous perdons de l'argent sur les retours dus à des fiches inexactes, sur les ventes en double des places de marché et sur les montres qui ne se vendent pas. Ces trois pertes viennent en grande partie de la qualité et de la circulation des données. »

**Deux représentations** (0,5 pt), parmi :
- **Barre horizontale empilée des 21 jours par étape**, en distinguant les attentes (en couleur vive) du travail (en gris), avec une ligne repère à 7 jours. *Message* : 11 jours sur 21 sont de l'attente. *Piège évité* : on indique la source et le mois de l'échantillon, pour ne pas présenter février 2027 comme une moyenne annuelle.
- **Barres triées des motifs de retour**, du plus fréquent au moins fréquent, avec en regard le coût estimé à 40 € par retour. *Message* : la fiche inexacte arrive en tête et coûte environ 120 k€. *Piège évité* : on signale que la moitié de l'année a été classée à la main, et que les réclamations des places de marché sont comptées comme des retours.
- **Barres empilées par catégorie** du délai de mise en vente et du délai de vente, sur une même échelle qui part de zéro. *Message* : il faut près de 95 jours pour une montre, contre moins de 50 pour la maroquinerie. *Piège évité* : des moyennes qui cachent la dispersion ; on indique aussi le nombre d'articles de chaque catégorie.
- **Barres par canal** des ventes et des ventes annulées. *Message* : les places de marché font un sixième des ventes et deux tiers des annulations. *Piège évité* : on compare des parts, et non des valeurs absolues de tailles différentes.

Un graphique en secteurs des quatre catégories, ou des taux de retour des canaux comparés sans mention de leur définition, sont de mauvais choix.

*2.2 d) – Les deux options d'outils d'analyse*

**Comparaison** (0,5 pt), selon quatre critères parmi :

| Critère | Option 1 : outil décisionnel en libre-service | Option 2 : tableaux de bord des logiciels existants |
|---|---|---|
| Réponse aux attentes de l'annexe 2.3 B | vue croisée des canaux, des pays et des étapes ; chaque responsable compose ses analyses, la présidente a « les mêmes chiffres pour tout le monde » | chaque logiciel ne voit que ses propres données : ni les ventes par canal et par pays en un seul écran, ni le délai par étape |
| Fiabilité et cohérence | jeux de données certifiés, selon des définitions communes, si le dictionnaire existe | chaque logiciel garde ses définitions : les trois montants des ventes de mars 2027 subsisteront |
| Coût (de tête, sur trois ans) | 90 + 3 × 20 = 150 k€, soit 50 k€ par an, environ 2 % des 2,4 M€ de dépenses du numérique | 30 + 3 × 10 = 60 k€ |
| Délai et dépendance | quatre mois ; peu de charge pour l'équipe numérique | trois mois, mais seulement quand l'équipe numérique, prise par la refonte, sera disponible |
| Pérennité | indépendante des logiciels sources : elle survit à la refonte du site | les écrans du site seront à refaire après la refonte |
| Risques | multiplication d'indicateurs concurrents si personne ne certifie les données ; données « pas plus justes » que les sources | morcellement durable ; l'analyste continue de répondre à la main aux 150 demandes d'extraction |

**Recommandation : l'option 1** (0,5 pt). C'est la seule qui croise les sources et donne à chacun les mêmes chiffres, ce que demandent la présidente et les responsables. Son surcoût, d'environ 90 k€ sur trois ans, est à rapprocher des 48 jours par an que l'analyste consacre au rapport mensuel, des 150 demandes d'extraction traitées à la main et des pertes chiffrées à la question c. L'option 2 coûte moins cher, mais elle prolonge le problème : des définitions différentes selon les logiciels, et des écrans à refaire après la refonte. Deux conditions de réussite, parmi :
- **les données avant l'outil** : référentiel des articles et dictionnaire de données d'abord (question 2.1), car l'outil « ne rendra pas les données plus justes » ; la préparation des données (60 k€) est le poste essentiel de l'option ;
- **des jeux de données et des indicateurs certifiés** par leurs propriétaires et validés par l'instance de gouvernance (question 2.3) ; les analyses personnelles restent possibles, mais seuls les indicateurs certifiés circulent ;
- **un rôle nouveau pour l'analyste** : elle documente la chaîne, certifie les jeux de données et accompagne les utilisateurs, au lieu d'extraire ;
- **la formation et la culture de la donnée** des 25 utilisateurs, et un démarrage par trois tableaux de bord : celui de la présidente (hebdomadaire), celui du catalogue et de l'atelier (articles en attente par étape), celui du commerce (ventes de la veille) ;
- des **droits d'accès** limités : les responsables n'ont pas besoin des données personnelles des vendeurs et des clients pour leurs analyses.

**Réponses tolérées**
- Analyse exploratoire placée en premier, si le candidat montre qu'elle sert d'abord à repérer les incohérences (dates, motifs, mois manquants) avant toute description.
- Autres constats tirés de l'annexe 2.2 (bijoux : 20 % d'invendus et 25 jours de mise en vente ; taux de retour élevé de la maroquinerie), s'ils portent une précaution.
- Coût des retours présenté pour les seuls retours évitables (120 k€) ou pour l'ensemble des retours (360 k€), si le calcul est juste.
- Option 2 retenue à titre transitoire jusqu'à la refonte, si le candidat en montre les limites et prévoit l'option 1 ensuite.
- Un outil décisionnel du marché cité à titre d'exemple, si la démarche (données, gouvernance, compétences) est développée.

**Erreurs fréquentes**
- *Informatique décisionnelle réduite à un outil* (`JUR-D02`, `ET-05`) — recommander l'outil en libre-service sans préparation des données, sans définitions communes ni rôle de l'analyste.
- *Corrélation présentée comme une causalité* (`ET-26`) — « l'horloger est la cause des invendus de montres » sans réserve.
- *Prudence d'interprétation absente* (`JUR-D06`) — comparer le taux de retour ou le délai des places de marché à ceux du site sans relever que leurs définitions diffèrent, ou généraliser l'échantillon de février 2027.
- *Calcul ou manipulation hors attente* (`JUR-T07`) — moyennes pondérées, écarts-types, prévisions, ou description de la manipulation d'un outil décisionnel.
- *Constat sans conséquence* (`JUR-T03`) — chiffres recopiés sans lien avec l'objectif de 7 jours ni avec la question de la présidente.
- *Lecture partielle des annexes* (`JUR-T08`) — ignorer la décomposition du délai (annexe 2.2 D) ou les témoignages qui l'expliquent.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement des données, analyses descriptive, exploratoire et prédictive | définitions et choix de la méthode | F08 § 1 et 2 | notion de cours |
| Choix d'une représentation, biais de lecture, corrélation et causalité | représentations et précautions | F08 § 5 | notion de cours |
| Outils décisionnels, libre-service et gouvernance centrale | comparaison des options | F08 § 6 | notion de cours |

---

### 2.3 – La gouvernance des données (2 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.a` « Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques » ; `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ». Le rôle du *Chief Data Officer* et la structuration de la gouvernance sont illustratifs, non normatifs ; aucune expertise des infrastructures.

**Annexes mobilisées** : annexes 1.1 (organigramme, plan « ORSALIE 2030 »), 2.1 (constats, données des vendeurs, absence de responsable, future place de marché), 2.3 (montants des ventes divergents, analyste seule à connaître les règles) et 2.5 (RGPD, DAMA-DMBOK, ISO/IEC 25012).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Gouvernance des données définie ; trois enjeux appliqués au cas (qualité, conformité, usage des données pour la future place de marché) | 0,5 |
| 2 | Instance de gouvernance : composition, fréquence, décisions, rattachement à la présidente | 0,5 |
| 3 | Propriétaire et intendant de trois domaines de données, rôle de l'équipe numérique | 0,5 |
| 4 | DAMA-DMBOK présenté comme un référentiel de bonnes pratiques et non comme une norme ; domaines prioritaires pour ORSALIE et usage concret | 0,5 |

**Réponse attendue**

La **gouvernance des données** est l'ensemble des rôles, des instances, des règles et des processus qui garantissent que les données sont définies, fiables, conformes, protégées et utilisées au service de la stratégie de l'organisation (F07 § 8). Elle relève des métiers et de la direction, et non de la seule équipe numérique.

**Trois enjeux pour ORSALIE** (0,5 pt) :
- **qualité** : les données des articles sont le produit lui-même, puisque le client achète sur une fiche. Les 2 300 libellés de marque, l'état trop favorable d'une fiche sur cinq, les 3 000 retours pour fiche inexacte et les 900 ventes en double montrent que la qualité se paie en retours, en pénalités et en confiance ;
- **conformité** : les données des vendeurs particuliers sont des données personnelles. Leur transmission inutile à la place de marché B est contraire au principe de minimisation, et ORSALIE doit pouvoir démontrer le respect des principes du RGPD (annexe 2.5). Le résultat de l'authentification est la **preuve** de la promesse faite au client ; il doit être exact, traçable et protégé, ce qui exclut un tableur partagé qui a déjà été écrasé ;
- **usage des données pour la future place de marché** : à partir de 2028, des particuliers publieront eux-mêmes leurs annonces. La liste de référence des marques et des modèles, l'échelle d'état et l'historique des articles vendus et de leurs prix fonderont l'estimation du prix proposée aux vendeurs et la garantie d'authenticité. Sans gouvernance, les erreurs actuelles seraient multipliées par le nombre d'annonces.

**L'instance** (0,5 pt) : un **comité des données**, par exemple :
- **composition** : le (la) secrétaire général(e), qui l'anime et qui supervise l'équipe numérique ; les propriétaires des données (responsable du catalogue, responsable de l'atelier, directeur commercial, responsable du service clients) ; le responsable technique ; l'analyste de données, qui en assure le secrétariat ; le service juridique, ainsi que le délégué à la protection des données si ORSALIE en a désigné un ;
- **fréquence** : mensuelle pendant la première année (mise en place du référentiel et du dictionnaire), puis trimestrielle ;
- **décisions** : valider les définitions du dictionnaire et leurs propriétaires ; fixer les règles de qualité, les cibles et les priorités de correction ; arbitrer les conflits de définition (le montant des ventes de mars 2027) ; décider des données transmises aux places de marché et des droits d'accès ; certifier les indicateurs de l'outil décisionnel ;
- **rattachement** : un compte rendu à la présidente, qui arbitre en dernier ressort et inscrit la qualité des données parmi les conditions du plan « ORSALIE 2030 ». Pour une entreprise de 130 salariés, aucun poste de directeur des données n'est indispensable : la structure est illustrative.

**Les rôles** (0,5 pt) : le **propriétaire** est le responsable métier d'un domaine de données (définitions, règles, qualité attendue, droits d'accès) ; l'**intendant** met en œuvre au quotidien (dictionnaire, contrôles, corrections) (F07 § 8.1).

| Domaine de données | Propriétaire | Intendant |
|---|---|---|
| Description des articles (marque, modèle, attributs, photographies, fiches) | Mme Clémence DUVERNAIS, responsable du catalogue | un rédacteur référent du catalogue |
| Authentification et état des articles | Mme Sabine VERCHAMP, responsable de l'atelier | un authentificateur référent |
| Ventes, disponibilités et retours | M. Damien ROCHAMBEL, directeur commercial, avec M. Karim BELLASTRE pour les retours | Mme Léa CORVENNAT, analyste de données |

L'**équipe numérique** est dépositaire technique des données : elle exploite et protège les logiciels et les échanges, mais elle ne décide pas du sens des données. Les données personnelles des vendeurs relèvent du service juridique pour leur conformité, sans être pour autant gérées par l'équipe numérique.

**Le DAMA-DMBOK** (0,5 pt) : c'est un **référentiel** de bonnes pratiques de gestion des données, et non une norme certifiable ni un logiciel ; il organise la gestion des données en onze domaines autour de la gouvernance (annexe 2.5 ; F07 § 8.2). ORSALIE s'en sert pour :
- **choisir ses priorités** : les données de référence (référentiel des articles), la qualité des données, les métadonnées (dictionnaire), l'intégration et l'interopérabilité (places de marché), puis l'entreposage et l'informatique décisionnelle (outil de la question 2.2 d) ;
- **évaluer sa situation** domaine par domaine, et suivre ses progrès d'une année sur l'autre ;
- **nommer les rôles** et structurer le plan d'action du comité, sans tout mettre en œuvre d'un coup.

La norme ISO/IEC 25012 (annexe 2.5) complète le dispositif : ses caractéristiques (exactitude, complétude, cohérence, actualité) servent à formuler les règles de qualité du dictionnaire.

**Réponses tolérées**
- Instance présidée par la présidente, ou comité intégré au comité de direction, si sa composition associe les métiers et si ses décisions sont précisées.
- Autres domaines de données (prix, photographies, données des vendeurs), si chacun a un propriétaire métier et un intendant.
- Mention d'un responsable des données (*Chief Data Officer*) à terme, présentée comme une option et non comme une obligation.
- Enjeu de sécurité des données (accès au résultat de l'authentification, tableur partagé) traité à la place de la conformité, s'il est appliqué au cas.

**Erreurs fréquentes**
- *Gouvernance confiée à l'équipe numérique* — le responsable technique « propriétaire » de toutes les données ; les métiers absents du comité.
- *Norme, référentiel et solution confondus* (`ET-01`, `JUR-S06`) — DAMA-DMBOK présenté comme une norme à certifier ou comme un logiciel.
- *Organisation imposée* — création d'une direction des données avec plusieurs postes pour une entreprise de 130 salariés, alors que le programme présente cette structuration comme illustrative.
- *Hors du sujet* — développement sur la vente des données ou sur leur valeur comptable, que la question ne demande pas.
- *Morceau de cours* (`JUR-T01`) — rôles définis sans les personnes et les domaines d'ORSALIE.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | onze domaines, priorités d'ORSALIE | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| ISO/IEC 25012 (2008), modèle de qualité des données | caractéristiques de la qualité citées dans les règles | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | minimisation, exactitude, intégrité et confidentialité, responsabilité (annexe 2.5) | `rgpd` / F15 § 0 | en vigueur |
| Proposition « omnibus numérique » du 19/11/2025 | non applicable (annexe 2.5) | `omnibus_numerique_donnees` | projet |
| Gouvernance des données, propriétaire, intendant, rôles illustratifs | définitions | F07 § 8.1 | notion de cours |

---

### 2.4 – Le projet de studio de mise en ligne (2,5 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI » ; `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI ». Les calculs se font de tête, sur des sommes rondes, sans prise en compte du coût du capital ; les méthodes financières qui en tiennent compte relèvent de l'UE 2.

**Annexes mobilisées** : annexes 1.1 (effectif du catalogue, délai de 21 jours, plan « ORSALIE 2030 »), 2.2 (motifs et coût des retours, décomposition du délai) et 2.4 (temps, coûts, gains, essai de mars 2027).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Retour sur investissement et délai de récupération définis ; coût d'une fiche : 8 € aujourd'hui, 5 € avec le studio (4 € de temps, 0,50 € de coûts annuels, 0,50 € d'investissement réparti) | 0,5 |
| a-2 | Gains en trésorerie : 60 k€ de retours évités et 90 k€ de marge, soit 150 k€, nets des coûts annuels 100 k€ ; délai de récupération 2,5 ans ; retour sur investissement sur cinq ans 100 % | 0,5 |
| a-3 | Temps libéré (10 000 h, environ six postes, 400 k€) écarté du calcul : gain de capacité et non de trésorerie, sauf recrutements évités ; conclusion nuancée (hypothèses, délai ramené à 15 jours seulement) | 0,5 |
| b | Trois coûts indirects ou cachés tirés de l'annexe 2.4 | 0,5 |
| c | Un indicateur de suivi complet : formule, source, fréquence, cible justifiée, axe | 0,5 |

**Réponse attendue**

*2.4 a) – Le coût d'une fiche, le délai de récupération et le retour sur investissement*

Le **retour sur investissement** (ROI) rapporte le gain net cumulé d'un projet sur une durée à son coût : (gains cumulés − investissement) / investissement. Le **délai de récupération** est le temps nécessaire pour que les gains nets annuels remboursent l'investissement : investissement / gain net annuel. Ce sont des indicateurs simples, qui ignorent le coût du capital ; ils ne retiennent que les gains mesurables et se complètent d'une appréciation des gains non financiers (F09 § 3.3).

**Le coût d'une fiche** (0,5 pt avec les définitions), en raisonnant en coût complet par article publié (l'article est l'inducteur des coûts du catalogue) :
- **aujourd'hui** : 12 minutes, soit un cinquième d'heure, à 40 € de l'heure : **8 €** par fiche ;
- **avec le studio** :
  - 6 minutes de temps, soit **4 €** ;
  - les coûts annuels, 30 + 20 = 50 k€ pour 100 000 fiches, soit **0,50 €** ;
  - l'investissement, 250 k€ réparti sur cinq ans, soit 50 k€ par an pour 100 000 fiches, ou **0,50 €** ;
  - au total, **5 €** par fiche, soit une baisse de 3 € (près de 40 %).

**Le délai de récupération et le retour sur investissement** (0,5 pt), en ne retenant que les gains qui se traduisent en trésorerie :
- **retours évités** : les 3 000 retours pour fiche inexacte (annexe 2.2 C) divisés par deux, soit 1 500 retours à 40 € de dépenses : **60 k€** par an (le temps interne de traitement des retours, que l'annexe 2.2 C exclut des 40 €, n'est pas compté, comme le temps libéré) ;
- **marge supplémentaire** estimée : **90 k€** par an ;
- **gains en trésorerie** : 60 + 90 = **150 k€** par an ; nets des coûts annuels du studio : 150 − 50 = **100 k€** par an ;
- **délai de récupération** : 250 / 100 = **2,5 ans**, inférieur à la durée d'utilisation prévue de cinq ans ;
- **retour sur investissement sur cinq ans** : (5 × 100 − 250) / 250 = **100 %**. Le studio rapporte, sur sa durée d'utilisation, deux fois ce qu'il a coûté.

**Le traitement du temps libéré** (0,5 pt) : le studio libère 6 minutes sur 100 000 articles, soit **10 000 h** par an, environ six postes à 1 600 heures sur les 20 du catalogue, d'une valeur de **400 k€** au coût horaire. Ce n'est pas un gain de trésorerie : Mme DUVERNAIS ne prévoit aucun départ. Le compter conduirait à un gain net de 500 k€ par an et à un délai de récupération de six mois, ce qui serait trompeur. C'est un **gain de capacité**. Il ne devient un gain financier que s'il évite des recrutements : la croissance des ventes à l'étranger et les annonces de la place de marché en exigeraient, et c'est l'hypothèse qu'il faut écrire et suivre.

**Conclusion** : le studio est rentable sans compter le temps libéré, mais sa rentabilité repose sur deux estimations, la marge supplémentaire et la division par deux des retours. Or cette dernière dépend de la qualité des données saisies par l'atelier, puisque l'outil rédige à partir d'elles : sans le référentiel de la question 2.1, une erreur d'état sera recopiée dans cinq langues. Le studio ramène le délai de mise en vente de 21 à 15 jours seulement ; l'objectif de 7 jours exige aussi de réduire les 6 jours d'attente avant l'authentification (annexe 2.2 D). Recommandation : lancer le studio après la mise en place du référentiel, ou en même temps, en commençant par la maroquinerie, qui fait plus de la moitié des articles mis en vente et dont le premier motif de retour est la fiche inexacte.

*2.4 b) – Trois coûts indirects ou cachés*

Trois coûts parmi les suivants (0,5 pt), tirés de l'annexe 2.4 :
- **la relecture** : à l'essai, une fiche sur dix (20 sur 200) contenait une erreur ; 3 minutes de relecture peuvent ne pas suffire, et une erreur qui passe crée un retour. Il s'agit d'une IA générative, qui produit un texte plausible et non une vérité, à distinguer du détourage, qui relève de la reconnaissance d'images par apprentissage automatique (F13 § 1) ;
- **les reprises de photographies** : une photographie de bijou brillant sur dix est à reprendre à la main, soit du temps de photographe qui n'est pas compté pour les bijoux (20 000 articles par an) ;
- **le stockage et l'affichage** de photographies trois fois plus lourdes : un hébergement en nuage plus coûteux et des pages plus lentes ;
- **l'abonnement au-delà de 120 000 fiches** : si la rédaction assistée est offerte aux vendeurs de la place de marché (environ 300 000 annonces en 2030), il faudrait payer au moins 180 000 fiches au-delà du forfait, soit au moins 54 k€ de plus par an, et environ 84 k€ si les 100 000 fiches d'ORSALIE relèvent du même abonnement ((300 000 + 100 000 − 120 000) × 0,30 €) ;
- **le raccordement** au site, à refaire après la refonte, par une équipe numérique déjà mobilisée ; et la dépendance à l'éditeur de l'outil de rédaction (prix révisables, récupération des fiches en fin de contrat) ;
- **la conduite du changement** des sept photographes, dont le métier change (formation, reconversion, risque de départ), au-delà des 40 k€ prévus, et la perte de productivité des premiers mois.

*2.4 c) – Un indicateur de suivi du projet*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Coût complet d'une fiche publiée** | (heures de catalogue consacrées aux fiches × coût horaire + coûts annuels du studio + investissement réparti sur cinq ans) / nombre de fiches publiées | référentiel des articles (horodatage des étapes et fiches publiées) et contrôle de gestion (coûts) | mensuelle | au plus 5 € fin 2028 (8 € en 2026) | financier |

L'indicateur relie le projet à son objectif économique ; il est utilement complété par un indicateur de qualité (taux de retour pour fiche inexacte) et par le délai de mise en vente (réponses tolérées), pour équilibrer coût, qualité et délai.

**Réponses tolérées**
- Coût d'une fiche avec le studio limité au temps (4 €), si le candidat ajoute ensuite les coûts annuels et l'investissement de façon explicite.
- Retour sur investissement exprimé en gain net cumulé sur cinq ans (5 × 100 − 250 = 250 k€), si le ratio est aussi donné ou si la confusion entre montant et ratio n'est pas faite.
- Surcoût de l'abonnement chiffré à 54 k€ (annonces des vendeurs seules) ou à 84 k€ (annonces et fiches d'ORSALIE), si l'hypothèse est écrite.
- Temps libéré valorisé partiellement, si l'hypothèse de recrutements évités est écrite et chiffrée de façon cohérente (par exemple deux ou trois postes évités).
- Autres indicateurs complets, par exemple : délai moyen entre la réception et la mise en vente (somme des jours entre réception et mise en vente / articles mis en vente ; référentiel des articles ; mensuelle ; 15 jours fin 2028 puis 7 jours en 2030, 21 jours en 2026 ; axe processus) ; taux de retour pour fiche inexacte (retours pour fiche inexacte / ventes en ligne ; outil de gestion de la relation client ; mensuelle ; au plus 2 % fin 2028, près de 4 % en 2026 ; axe client) ; part des fiches corrigées à la relecture (fiches corrigées / fiches rédigées par l'outil ; référentiel des articles ; mensuelle ; au plus 5 % fin 2028, 10 % à l'essai ; axe processus).

**Erreurs fréquentes**
- *Temps libéré compté comme une économie de trésorerie* — délai de récupération de six mois annoncé sans hypothèse de redéploiement ni de recrutements évités (F09 § 3.3).
- *Retour sur investissement et coût total confondus* (`ET-33`) — ROI présenté comme un montant, ou coûts annuels oubliés dans le calcul.
- *Calcul financier hors attente* (`JUR-T07`) — calculs qui tiennent compte du coût du capital, alors que l'énoncé demande un calcul de tête simple.
- *IA générative et apprentissage automatique confondus* (`ET-09`) — la rédaction assistée présentée comme un modèle qui « apprend » l'état des articles, ou comme infaillible.
- *Indicateur incomplet ou générique* (`ET-18`, `JUR-A02`) — « suivre la rentabilité » sans formule, source, fréquence, cible ni axe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Retour sur investissement et délai de récupération, coûts cachés, gain de productivité et trésorerie | définitions et calcul de tête | F09 § 2 et 3.3 | notion de cours |
| Coût complet et inducteur de coûts appliqués au système d'information | coût d'une fiche par article publié | F09 § 2 | notion de cours |
| IA générative et apprentissage automatique | limites de la rédaction assistée | F13 § 1 | notion de cours |
| Indicateur à cinq champs, axes du tableau de bord prospectif | indicateur de suivi du projet | F08 § 3 ; F09 § 4.1 | notion de cours |

---

## DOSSIER 3 – SÉCURISER LES TRANSACTIONS ET MESURER L'IMPACT ENVIRONNEMENTAL DU NUMÉRIQUE (13 points)

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
