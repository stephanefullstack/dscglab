# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 20 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique, F02 gouvernance et référentiels, F04 relations avec les ESN et contrats, F09 performance du SI, F11 blockchain et crypto-actifs, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

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
