# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 13 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F14 numérique responsable, F07 données et gouvernance, F09 performance du SI, F02 gouvernance, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Le projet « Froid intelligent » et la stratégie SI responsable | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 3 |
| 1.2 Sobriété et cycle de vie des données | `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements | 3 |
| 1.3 Diagnostic des équipements et plan d'action | `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 3 |
| 1.4 Gouvernance du numérique responsable | `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété ; `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité | 2 |
| 1.5 Tableau de bord SI intégrant la durabilité | `1.2.e` Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI | 3 |
| **Dossier 1 – Rendre le système d'information sobre et durable et en piloter les résultats** |  | **14** |

Répartition indicative : connaissances (Green IT et IT for green, cycle de vie des données et sobriété, cycle de vie d'un équipement, gouvernance du SI orientée RSE, tableau de bord équilibré) 2,5 points (items 1.1 a-1, 1.2 a-1, 1.3 b-1, 1.4 a-1, 1.5 a-1) ; analyse des annexes et recommandations 11,5 points, soit environ 82 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – Le projet « Froid intelligent » et la stratégie SI responsable (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : « La transformation numérique responsable nécessite une approche transversale et non cloisonnée » ; « La durabilité doit être intégrée dans la gouvernance globale du SI, et non comme ajout marginal ».

**Annexes mobilisées** : annexes 1.1 (plan « ORMESTAL 2030 »), 1.2 (consommation et volume de référence, cibles 2030) et 1.3 (projet, options A et B, avis).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Green IT et IT for green distingués, chacun illustré par un exemple tiré des annexes (empreinte du SI lui-même ; SI au service de la durabilité de l'activité) | 0,5 |
| a-2 | Projet situé : IT for green par sa finalité, qui entre aussi dans le champ du Green IT par ses effets sur le SI ; les deux bilans sont à évaluer ensemble | 0,5 |
| b-1 | Gain attendu chiffré et relativisé (3 000 MWh, 10 % de la consommation, moitié de l'effort de 6 000 MWh ; mesure de l'éditeur, trois mois d'hiver, entrepôt neuf) | 0,5 |
| b-2 | Effets sur l'empreinte du SI chiffrés (300 ou 100 MWh face à 600 MWh et à la cible de 480 ; 120 ou 20 To par an face à 400 To et à la cible de 250 ; 1 500 capteurs à fabriquer) | 0,5 |
| b-3 | Conditions d'un bilan favorable (pilote mesuré, sobriété des données et du modèle, hébergement transparent, maîtrise humaine) et option recommandée avec justification | 0,5 |
| c | Deux principes de stratégie SI responsable, déduits du cas et applicables à d'autres projets | 0,5 |

**Réponse attendue**

*1.1 a) – Green IT, IT for green et place du projet*

Le **Green IT** (ou numérique responsable appliqué au SI) vise à réduire l'empreinte environnementale du système d'information lui-même : fabrication et fin de vie des équipements, énergie des salles et des services hébergés, volume des données, conception des logiciels et usages. L'**IT for green** mobilise le système d'information au service de la stratégie environnementale de l'organisation : capteurs, optimisation des flux, pilotage de l'énergie, collecte des données de durabilité (F14 § 3). Exemples tirés des annexes : relever de trois à cinq ans la durée de vie des 1 200 équipements, ou réduire la conservation des vidéos des quais, relève du Green IT ; l'éco-conduite fondée sur les boîtiers télématiques relève de l'IT for green (0,5 pt).

Le projet « Froid intelligent » relève de l'**IT for green** par sa finalité : réduire la consommation électrique des 14 entrepôts, premier enjeu énergétique du plan « ORMESTAL 2030 ». Mais il entre aussi dans le champ du **Green IT** par ses moyens : 1 500 capteurs supplémentaires, des données plus fréquentes, un stockage et un calcul hébergés qui alourdissent l'empreinte du SI, alors que le même plan demande de la réduire de 20 %. La filiale doit donc évaluer ensemble les deux bilans, celui de l'activité et celui du SI, et non le seul gain annoncé (0,5 pt).

*1.1 b) – Analyse du projet et recommandation*

**Gain attendu** (0,5 pt). L'éditeur annonce 3 000 MWh par an (option A) ou 2 700 MWh (option B), soit environ 10 % des 30 000 MWh consommés par les entrepôts en 2026 et la moitié de l'effort de 6 000 MWh qu'exige la cible de 24 000 MWh : c'est un levier important, comme le souligne Mme PRUNEYRAC. Ce chiffre reste une promesse : il a été mesuré par l'éditeur lui-même, pendant trois mois d'hiver, dans un entrepôt neuf aux Pays-Bas, alors que les entrepôts de la filiale ne sont pas neufs et que l'été, où le froid coûte le plus, n'a pas été observé. M. TALBREUX demande à juste titre une mesure chez nous, sur une année.

**Effets sur l'empreinte du SI** (0,5 pt).
- **Énergie** : l'option A ajoute 300 MWh par an, soit la moitié de la consommation actuelle du SI (600 MWh), qui passerait à 900 MWh quand la cible 2030 est de 480 MWh ; l'option B ajoute 100 MWh (700 MWh au total). L'origine de l'électricité et l'efficacité énergétique des centres de l'option A ne sont pas connues : l'estimation de 300 MWh est invérifiable.
- **Données** : l'option A ajoute 120 To par an ; le stockage passerait de 400 à 520 To dès la première année, pour une cible de 250 To ; l'option B ajoute 20 To par an grâce aux données résumées à la minute et conservées deux ans.
- **Équipements** : 1 500 capteurs à fabriquer, à installer puis à recycler, quelle que soit l'option ; leur fabrication pèse dans l'empreinte, qui en 2026 tient déjà pour 65 % aux équipements.
- **Effet rebond** : des envois toutes les 10 secondes et un modèle réentraîné chaque semaine sur toutes les données brutes créent un besoin de stockage et de calcul sans limite.

**Conditions et recommandation** (0,5 pt). En énergie, le bilan d'ensemble reste nettement favorable : environ 2 700 MWh nets pour l'option A, 2 600 pour l'option B, le gain étant dix fois (A) à vingt-sept fois (B) supérieur à la consommation ajoutée. Mais le plan fixe aussi un objectif propre au SI, que l'option A rend inatteignable. L'**option B** est recommandée : modèle spécialisé de taille plus réduite, réentraîné chaque mois (sobriété du modèle) ; données résumées dans l'entrepôt et conservées deux ans (sobriété des données) ; hébergement en France avec un rapport des consommations attribuées (transparence, maîtrise de la localisation des données). Son surcoût de 40 k€ par an (240 contre 200 k€) rémunère la maîtrise des données et le respect de l'objectif propre au SI, pour un gain net d'énergie presque égal (2 600 contre 2 700 MWh). Conditions : un **pilote mesuré** dans deux entrepôts de la filiale (l'un en froid positif, l'autre en froid négatif) pendant une année, avant toute généralisation, avec une consommation de référence relevée avant le démarrage ; la consommation ajoutée au SI compensée par les actions de sobriété des questions 1.2 et 1.3 ; la possibilité pour les chefs d'équipe de reprendre la main sur une chambre froide à tout moment.

*1.1 c) – Deux principes d'une stratégie SI responsable* (0,5 pt pour deux principes justifiés)

1. **Évaluer chaque projet numérique sur son bilan complet et mesuré** : gain pour l'activité et coût pour le SI (énergie, données, équipements), sur la base de mesures réalisées dans la filiale et non de chiffres annoncés ; c'est ce qui permet de tenir ensemble les deux objectifs du plan « ORMESTAL 2030 ».
2. **Dimensionner au juste besoin (sobriété dès la conception)** : collecter, conserver et calculer ce qui sert la décision, au rythme utile ; choisir l'hébergement selon des critères environnementaux et de maîtrise (localisation, électricité, transparence des consommations, conservation des données), et pas seulement selon le coût.

**Réponses tolérées**
- Option A retenue si le candidat la conditionne explicitement à une limitation des données envoyées, à une transparence des consommations et à une compensation chiffrée dans le SI ; recommandation d'un pilote sans choix immédiat d'option, si elle est argumentée.
- Principes formulés autrement s'ils découlent du cas : intégrer la durabilité au portefeuille de projets et au tableau de bord SI ; préférer les solutions frugales ; associer les métiers et la RSE à la décision.
- Mention de la souveraineté des données pour l'option A, sans analyse juridique du transfert.

**Erreurs fréquentes**
- *Projet présenté comme seulement vertueux* (`ET-19` opportunités sans risques) — « l'IA économise de l'énergie, il faut la déployer » ; juste : gain annoncé à vérifier, empreinte du SI ajoutée, conditions.
- *Green IT et IT for green confondus* (`ET-12`) — juste : le projet sert l'activité (IT for green) mais alourdit le SI (Green IT).
- *Empreinte réduite à l'électricité* (`ET-38`) — oubli des 1 500 capteurs et du stockage ; juste : fabrication, énergie, données.
- *Fonctionnement interne du modèle d'IA* — description de l'apprentissage ou de l'architecture du modèle ; juste : taille, fréquence de réentraînement et volume de données comme leviers de sobriété.
- *Morceau de cours* (`JUR-T01` contextualiser chaque notion) — définitions sans les chiffres de l'annexe 1.3.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Green IT, IT for green, sobriété numérique, effet rebond | définitions, analyse du projet | F14 § 1 et 3 | notion de cours |
| Cloud et centres de données, tension IA et sobriété, modèles frugaux | options d'hébergement | F14 § 5 ; F13 | notion de cours |
| Loi n° 2021-1485 du 15 novembre 2021 (REEN) | centres de données moins énergivores (annexe 1.4 C) | `loi_reen` / F14 § 2 | en vigueur |

---

### 1.2 – Sobriété et cycle de vie des données (3 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ». Limite : « L'expertise technique des infrastructures (serveurs, réseaux) n'est pas attendue ».
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ».

**Annexes mobilisées** : annexes 1.2 (données, volumes, exigences des clients, cibles 2030) et 1.4 (RGESN, EcoIndex).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cinq étapes du cycle de vie et sobriété des données définies | 0,5 |
| a-2 | Relevés de température : règles compatibles avec les exigences des clients (cinq minutes, alerte immédiate, un, deux ou cinq ans, 48 heures) | 0,5 |
| a-3 | Vidéos des quais : durée réduite justifiée par l'usage constaté, extraits utiles conservés, suppression automatique | 0,5 |
| a-4 | Fichiers dupliqués : stockage unique de référence, suppression des copies, purge des sauvegardes | 0,5 |
| a-5 | Mise en œuvre (propriétaire, automatisation, contrôle de la restitution) et effet attendu au regard de la cible de 250 To | 0,5 |
| b | Bonne pratique d'écoconception justifiée et illustrée par un service de l'annexe 1.2 (page de suivi des températures du portail) | 0,5 |

**Réponse attendue**

*1.2 a) – Cycle de vie et règles par catégorie*

Le **cycle de vie des données** décrit les étapes qu'elles traversent : création ou collecte, stockage, usage, archivage, suppression ; à chaque étape correspondent une règle, un responsable et une durée (F07 § 8.4). La **sobriété numérique appliquée aux données** consiste à interroger le besoin avant d'optimiser la technique : ne collecter que ce qui sert, au rythme utile, ne conserver qu'une seule copie de référence, pour la durée requise, puis archiver ou supprimer (F14 § 3) (0,5 pt).

| Étape | Relevés de température (40 To) | Vidéos des quais (200 To) | Fichiers dupliqués (environ 60 To de copies) |
|---|---|---|---|
| **Collecte** | un relevé toutes les cinq minutes, fréquence exigée par les contrats, au lieu de 30 secondes (dix fois moins de relevés) ; envoi immédiat d'une alerte et passage à un relevé plus fréquent dès qu'une température sort de la plage ; dans les entrepôts qui pilotent leurs groupes froid avec le projet « Froid intelligent », une mesure plus fine reste utile au pilotage local, mais seuls les résumés à la minute de l'option B sont envoyés, et seul le relevé à cinq minutes est archivé pour les clients | enregistrement des quais conservé, mais limité aux heures d'activité ou déclenché par le mouvement, si l'exploitation le permet | aucune nouvelle copie : les documents sont partagés par un lien vers l'espace de référence, et non joints aux courriels |
| **Stockage** | une seule base de référence (l'outil de supervision) ; le cloud du groupe et l'outil de reporting la consultent au lieu de la copier | stockage local de courte durée | un seul espace de référence par type de document (lettres de voiture, bons de livraison, fichiers de chaque service) ; dédoublonnage des 120 To existants |
| **Archivage** | après la livraison, les relevés du lot sont archivés dans un format compressé, indexés par client et par lot, et restituables en 48 heures | extraits liés à une réclamation archivés jusqu'à sa clôture | documents archivés selon des durées fixées avec la direction administrative et financière |
| **Suppression** | automatique au terme de la durée fixée par le contrat du client : un an (enseignes), deux ans (industriels), cinq ans (deux industriels des surgelés) ; purge des relevés accumulés depuis 2015 au-delà de ces durées | automatique au bout d'un mois, au lieu de trois : les 140 extraits consultés en 2026 avaient tous moins de 20 jours | suppression des copies ; sauvegardes purgées selon un calendrier de rotation |

(0,5 pt par catégorie dont les règles couvrent les quatre étapes et respectent les exigences des clients.)

**Mise en œuvre et effet** (0,5 pt) : chaque catégorie a un propriétaire (le responsable des entrepôts et la responsable du transport pour les relevés, le responsable des entrepôts pour les vidéos, chaque directeur pour ses documents), qui valide les durées ; le responsable des systèmes d'information automatise les purges et en garde la trace. Un contrôle trimestriel vérifie que les relevés d'un lot pris au hasard sont restitués en moins de 48 heures : la sobriété ne doit jamais faire manquer une exigence contractuelle. En ordre de grandeur, ramener les vidéos à un mois (environ 70 To au lieu de 200), supprimer les 60 To de copies et purger les relevés anciens ramènerait le stockage vers 190 To, sous la cible de 250 To, et compenserait les 20 To par an de l'option B de l'annexe 1.3.

*1.2 b) – Une bonne pratique d'écoconception* (0,5 pt)

**Justifier le besoin et dimensionner chaque nouveau traitement au juste nécessaire, dès sa conception** (thèmes « stratégie » et « spécifications » du RGESN, annexe 1.4 C) : avant toute mise en service, une revue d'écoconception vérifie la fréquence de mise à jour, le poids des pages et des données, la durée de conservation et la compatibilité avec des équipements anciens. Illustration : la page de suivi des températures du portail des clients se rafraîchit toutes les 30 secondes, pèse 8 Mo et obtient la note F à l'EcoIndex, alors que neuf connexions sur dix servent à télécharger un certificat. Il faut placer le certificat en accès direct, rafraîchir la page à la demande ou toutes les cinq minutes (le rythme des relevés exigés), alléger les contenus, et fixer une note EcoIndex cible pour les pages les plus consultées.

**Réponses tolérées**
- Six ou sept étapes du cycle de vie (collecte, traitement, partage, archivage, destruction), si les cinq étapes du programme y figurent.
- Durée de conservation des vidéos de 30 jours ou d'un mois et demi, si elle est justifiée par l'usage constaté (extraits de moins de 20 jours) et par le délai des réclamations ; enregistrement continu maintenu.
- Collecte des relevés à une fréquence plus fine que cinq minutes, si elle reste justifiée par un usage (alerte, pilotage du projet « Froid intelligent ») et limitée dans le temps.
- Autre bonne pratique d'écoconception (compatibilité avec les terminaux anciens, conservation par défaut limitée, mesure de l'EcoIndex avant mise en production), illustrée par le cas.

**Erreurs fréquentes**
- *Sobriété réduite à l'économie d'énergie* (`ET-12`) — « supprimer des données pour économiser l'électricité » ; juste : questionner le besoin de collecter, de copier et de conserver.
- *Règles contraires aux contrats* — suppression des relevés avant un an, ou relevés espacés au-delà de cinq minutes ; juste : durées et fréquence de l'annexe 1.2 C comme plancher.
- *Analyse juridique des durées de conservation* — renvoi à une réglementation sanitaire ou au droit des données personnelles ; juste : les durées sont celles des contrats, fournies par l'annexe.
- *Solution technique détaillée* (`JUR-T12` moins de technique, plus de management) — choix d'un format de compression ou d'une architecture de stockage ; juste : règles, responsables, contrôle.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cycle de vie des données : création, stockage, usage, archivage, suppression ; durées de conservation | règles par catégorie | F07 § 8.4 | notion de cours |
| Référentiel général d'écoconception de services numériques (RGESN), version 2 (2024) | bonne pratique d'écoconception | `rgesn_2024` / F14 § 2 | en vigueur |
| EcoIndex | note de la page de suivi des températures | `ecoindex` / F14 § 4 | outil en ligne |

---

### 1.3 – Diagnostic des équipements et plan d'action (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI » ; `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ».
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Limite : « L'usage des outils ne dispense pas d'une lecture critique des corrélations et biais ».

**Annexes mobilisées** : annexes 1.2 (équipements, mesures de référence et cibles, estimation des émissions) et 1.4 (étude ADEME-Arcep, loi REEN, RGESN).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux écarts entre la référence et la cible (durée de vie de 3 à 5 ans, reconditionné de 0 à 30 %, parc de 1 200 à 1 100) et poids des équipements (65 % de l'estimation, contre 30 % pour la salle serveurs et les services hébergés), rapproché de l'étude ADEME-Arcep | 0,5 |
| a-2 | Deux précautions de lecture de l'estimation (incertitude de 30 % supérieure à la baisse visée de 20 %, méthode fondée sur des valeurs moyennes et sur des montants de factures, première estimation sans point de comparaison), en quinze lignes au maximum | 0,5 |
| b-1 | Cycle de vie d'un équipement présenté (fabrication, distribution, usage, fin de vie), fabrication prépondérante | 0,5 |
| b-2 | Comparaison argumentée des deux politiques (400 contre 240 achats par an, coûts de tête, empreinte, conditions et limites : froid négatif, boîtiers, compatibilité des applications) | 0,5 |
| c | Trois actions prioritaires sur au moins deux domaines, chacune reliée à un constat de l'annexe 1.2 ; 0,5 pour deux actions | 1 |

**Réponse attendue**

*1.3 a) – Diagnostic argumenté (note modèle)*

<!-- note -->
L'empreinte du SI tient d'abord à ses équipements : la fabrication et la fin de vie des 1 200 équipements pèsent 65 % des 300 t éqCO2 estimées en 2026, contre 30 % pour la salle serveurs et les services hébergés. C'est l'ordre de grandeur de l'étude ADEME-Arcep (65 à 92 % pour les terminaux) : même une baisse de 20 % de la consommation électrique ne suffirait pas à atteindre la cible de 240 t. Les écarts à combler portent donc sur la durée de vie, de 3 à 5 ans, et sur la part reconditionnée des achats, de 0 à 30 %, ainsi que sur le parc, de 1 200 à 1 100 équipements. Or la politique du groupe, qui renouvelle tout tous les trois ans, contredit sa propre cible, et huit équipements retirés sur dix fonctionnaient encore. Deux précautions s'imposent. L'estimation est incertaine à plus ou moins 30 %, davantage que la baisse visée de 20 % : elle ne prouvera pas seule l'atteinte de la cible. Elle applique des valeurs moyennes au nombre d'équipements et estime les services hébergés par leurs factures : allonger la durée de vie ne la réduira que si la méthode en tient compte, et une baisse de prix ferait baisser l'empreinte affichée sans effet réel. C'est une première estimation : il faut garder la même méthode et suivre des indicateurs physiques (durée de vie, achats, MWh, To).
<!-- /note -->

(0,5 pt pour les écarts et le poids des équipements ; 0,5 pt pour deux précautions.)

*1.3 b) – Cycle de vie d'un équipement et comparaison des deux politiques*

Le **cycle de vie d'un équipement numérique** comprend la fabrication (extraction des matières, composants, assemblage), la distribution, l'usage (électricité, maintenance) et la fin de vie (réemploi, reconditionnement, recyclage des déchets électroniques). Pour un terminal, la fabrication domine l'empreinte : chaque année d'usage gagnée évite une part de fabrication, ce que vise l'axe « limiter le renouvellement des terminaux » de la loi REEN (annexe 1.4 C) (0,5 pt).

| Critère | Renouvellement tous les trois ans (politique du groupe) | Durée de vie portée à cinq ans, avec reconditionnement |
|---|---|---|
| Achats annuels | environ 400 équipements neufs | environ 240 équipements (40 % de moins), dont une part reconditionnée |
| Coût annuel (calcul de tête) | 0,4 M€ (400 × 1 000 €) | environ 0,26 M€ s'ils sont achetés neufs (240 × 1 000 € + 240 révisions à 100 €), soit environ 0,14 M€ d'économie par an, davantage avec des équipements reconditionnés à 600 € ; ces montants valent en régime de croisière, une fois la transition achevée |
| Empreinte | fabrication de 400 équipements par an ; équipements encore utilisables envoyés au recyclage | fabrication réduite d'environ 40 % ; réemploi des équipements retirés par un reconditionneur |
| Conditions et limites | simplicité, homogénéité du parc, performance garantie | révision à mi-vie (batterie, nettoyage) ; durée différenciée pour les terminaux du froid négatif, qui s'usent plus vite ; boîtiers télématiques conservés aussi longtemps que le camion ; applications compatibles avec les équipements anciens (RGESN) ; suivi des pannes |

(0,5 pt pour une comparaison argumentée sur plusieurs critères, conclue.)

Conclusion : la politique du groupe est contraire au plan « ORMESTAL 2030 » ; la filiale doit proposer au groupe une politique différenciée par type d'équipement, fondée sur l'état réel des équipements plutôt que sur leur âge.

*1.3 c) – Trois actions prioritaires* (1 pt pour trois actions reliées aux constats ; 0,5 pt pour deux)

1. **Équipements — allonger la durée de vie et recourir au reconditionnement** (priorité 1, premier poste de l'empreinte) : durée de vie portée à cinq ans pour les postes et les tablettes, à quatre ans pour les terminaux du froid négatif, avec révision à mi-vie ; 30 % d'équipements reconditionnés dans les achats dès 2028 ; équipements retirés confiés à un reconditionneur pour réemploi plutôt qu'au collecteur de déchets électroniques ; boîtiers télématiques séparés des tablettes et gardés jusqu'à leur panne ou jusqu'au remplacement du camion.
2. **Usages — rationaliser le parc** (priorité 2, cible de 1 100 équipements) : un seul équipement par salarié (40 salariés disposent d'un poste fixe et d'un portable) ; postes partagés entre les équipes de jour et de nuit dans les bureaux des entrepôts, généralisés et comptés une fois ; attribution des équipements selon le besoin du poste.
3. **Services hébergés — appliquer les règles de sobriété des données** (priorité 3, cibles de 250 To et de 480 MWh) : règles de la question 1.2 (relevés archivés à cinq minutes, vidéos à un mois, copies supprimées), choix de l'option B du projet « Froid intelligent », allègement de la page de suivi des températures du portail.

**Réponses tolérées**
- Diagnostic structuré autrement (forces, faiblesses, priorités), s'il comporte les écarts, le poids des équipements et deux précautions.
- Autres précautions : périmètre de l'estimation (le projet « Froid intelligent » n'y figure pas) ; valeurs moyennes qui ne distinguent pas un équipement reconditionné d'un équipement neuf.
- Coût comparé sans tenir compte des révisions, ou durée de vie de quatre ans pour l'ensemble du parc, si le raisonnement est cohérent.
- Actions sur les usages formulées en sensibilisation des salariés (gestes de stockage, extinction des postes), si au moins une action porte sur les équipements.

**Erreurs fréquentes**
- *Empreinte limitée à l'électricité* (`ET-38`) — plan centré sur la salle serveurs, qui ne pèse que 10 % ; juste : fabrication prépondérante, durée de vie et reconditionnement d'abord.
- *Estimation lue comme une mesure exacte* (`JUR-D06` prudence d'interprétation) — « nous avons émis 300 t » ; juste : estimation incertaine, méthode à stabiliser, indicateurs physiques en complément.
- *Calcul d'émissions* — recalcul des tonnes par équipement ou par MWh ; juste : lecture des parts et des écarts donnés par l'annexe.
- *Allongement de la durée de vie sans condition* — juste : révision, durée différenciée, compatibilité des applications.
- *Diagnostic descriptif* (`JUR-T03` analyser et argumenter) — chiffres recopiés sans hiérarchie ni conclusion.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Étude ADEME-Arcep sur l'empreinte environnementale du numérique (volet du 19/01/2022 ; mise à jour du 17/01/2025) | poids des terminaux et de leur fabrication | `etude_ademe_arcep_numerique` / F14 § 1 | publiée |
| Loi n° 2021-1485 du 15 novembre 2021 (REEN) | limiter le renouvellement des terminaux, réemploi, reconditionnement | `loi_reen` / F14 § 2 | en vigueur |
| RGESN, version 2 (2024) | services utilisables sur des équipements anciens | `rgesn_2024` / F14 § 2 | en vigueur |
| Indicateurs d'empreinte : durée de vie, part reconditionnée, consommation, lecture d'une référence et d'une cible | diagnostic | F14 § 4 | notion de cours |

---

### 1.4 – Gouvernance du numérique responsable (2 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété ».
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ».

**Annexes mobilisées** : annexes 1.1 (organigramme, rapport au groupe), 1.3 (avis sur le projet « Froid intelligent », projet d'éco-conduite) et 1.4 (attentes du groupe et de la directrice générale).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance du SI orientée RSE définie (inclusion, éthique, sobriété intégrées aux structures, processus et règles par lesquels la direction oriente et surveille le SI) | 0,5 |
| a-2 | Instance précisée : composition associant les parties prenantes clés du cas (dont représentants du personnel et utilisateurs), fréquence, décisions | 0,5 |
| b | Trois conditions de poursuite du score d'éco-conduite, respectivement éthique, transparence et inclusion, tirées de l'annexe 1.3 C ; 0,5 pour deux | 1 |

**Réponse attendue**

*1.4 a) – Définition et instance*

La **gouvernance du SI** désigne l'ensemble des structures, processus et règles par lesquels la direction évalue, oriente et surveille l'usage du SI au service de la stratégie (F02). **Orientée RSE**, elle intègre la sobriété, l'éthique et l'inclusion dans ces décisions mêmes : choix des projets, politique d'équipement, règles sur les données, indicateurs, et non dans un document à part (limite du programme : la durabilité n'est pas un « ajout marginal ») (0,5 pt).

**Instance proposée : un comité du numérique responsable** (0,5 pt)
- **Composition** : présidé par Mme DUCHASTEL ; M. BRÉVANNE (responsable des systèmes d'information) en assure le secrétariat ; Mme PRUNEYRAC (responsable RSE) ; M. DRAVIGNOL (directeur des opérations), M. TALBREUX (entrepôts) et Mme VALDRESSE (transport) pour les métiers ; Mme MERCOIRAN (directrice administrative et financière) pour les coûts ; deux utilisateurs (un chef d'équipe d'entrepôt, un conducteur) et un représentant du personnel pour les projets qui touchent le travail des salariés ; la direction des systèmes d'information du groupe invitée quand une politique du groupe est en cause.
- **Fréquence** : trimestrielle, avant le compte rendu à M. DORMAELS ; séance supplémentaire pour tout nouveau projet numérique important.
- **Décisions** : valider la stratégie et la charte du numérique responsable de la filiale ; donner un avis sur tout nouveau projet numérique au regard de son bilan complet (activité et SI), avant engagement (« Froid intelligent », éco-conduite) ; arrêter les règles de conservation des données et la politique d'équipement, et porter auprès du groupe la demande de dérogation à la règle des trois ans ; fixer les cibles annuelles et examiner le tableau de bord SI (question 1.5) ; arbitrer entre gain d'activité et empreinte du SI.

*1.4 b) – Application au score d'éco-conduite* (1 pt pour trois conditions ; 0,5 pt pour deux)

Le comité ne rejette pas l'objectif (5 % de carburant en moins, enjeu d'IT for green) ; il conditionne le projet à trois exigences, après un pilote avec des conducteurs volontaires.
1. **Éthique** : un outil d'aide et de progrès, non de surveillance ni de sanction. Pas de classement nominatif affiché ; chaque conducteur voit son propre score et les résultats ne sont publiés que par équipe ; le score est corrigé selon le type de tournée (urbaine avec trente arrêts ou longue distance) pour ne pas pénaliser structurellement certains conducteurs ; l'entretien avec les moins bien notés devient une proposition de formation à l'éco-conduite ; aucune décision automatique sur la seule base du score.
2. **Transparence** : critères et poids du calcul expliqués aux conducteurs avant le lancement ; durée de conservation des données fixée et annoncée ; accès du conducteur à ses propres données et possibilité de contester un résultat ; projet présenté au comité avec les représentants du personnel, puis bilan du pilote publié.
3. **Inclusion** : tablette avec pictogrammes, messages vocaux et choix de la langue pour la trentaine de conducteurs qui lisent difficilement le français ; formation en petits groupes ; interface conçue avec des conducteurs, dont certains de ceux qui rencontrent ces difficultés.

**Réponses tolérées**
- Instance nommée autrement (comité RSE et SI, comité de gouvernance numérique) ou intégrée au comité de direction élargi, si la composition, la fréquence et les décisions sont précises.
- Fréquence semestrielle, si le suivi trimestriel du tableau de bord est assuré par ailleurs.
- Recommandation d'abandonner le classement individuel au profit d'un objectif collectif par entrepôt, si elle est argumentée par les trois exigences.

**Erreurs fréquentes**
- *Gouvernance réduite à un comité sans pouvoir* (`JUR-G06` vocabulaire précis de la gouvernance) — « créer un comité vert » sans membres ni décisions ; juste : composition, fréquence, décisions et lien avec le tableau de bord.
- *Durabilité cloisonnée* — instance limitée à la RSE et au SI, sans les métiers ni les utilisateurs ; juste : parties prenantes clés associées.
- *Analyse juridique* — consultation obligatoire des représentants du personnel, régime du traitement des données des conducteurs ; juste : conditions de gouvernance (éthique, transparence, inclusion), hors analyse juridique.
- *Éthique réduite à une déclaration* (`JUR-T03` analyser et argumenter) — « le projet doit être éthique et transparent » ; juste : règles concrètes qui changent la conception du score.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gouvernance du SI, comitologie, parties prenantes | définition et instance | F02 § 2 et 6 | notion de cours |
| Gouvernance SI orientée RSE : comité numérique responsable, inclusion, éthique, charte | instance et conditions | F14 § 0 ; perimetre 4.3.c | notion de cours |

---

### 1.5 – Tableau de bord SI intégrant la durabilité (3 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.e` « Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) ». Limite : « Le pilotage ESG est à comprendre dans une logique d'indicateurs intégrés, non isolés. »
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI ».

**Annexes mobilisées** : annexes 1.2 (mesures de référence et cibles 2030, exigences des clients, coûts des équipements) et 1.4 (reporting actuel, attentes).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Principe du tableau de bord équilibré appliqué au SI (Balanced Scorecard, IT Balanced Scorecard) et structure en quatre axes, dont un axe de durabilité relié aux trois autres | 0,5 |
| a-2 | Quatre indicateurs complets (formule, source, fréquence, cible, axe), dont au moins deux reliés aux cibles 2030 de l'annexe 1.2 D ; 1 pour trois, 0,5 pour deux | 1,5 |
| b | Trois arguments tirés de l'annexe 1.4 (intégration au lieu d'un fichier séparé, cibles et trajectoire, sources et méthode stables, responsabilités et incitations) ; 0,5 pour deux | 1 |

**Réponse attendue**

*1.5 a) – Principe, structure et indicateurs*

Le **tableau de bord équilibré** (Balanced Scorecard, Kaplan et Norton) traduit une stratégie en un nombre restreint d'indicateurs répartis sur plusieurs axes, pour ne pas piloter sur les seuls résultats financiers ; appliqué au SI (IT Balanced Scorecard, Van Grembergen), il retient la contribution financière, l'orientation vers les utilisateurs et les clients, l'excellence opérationnelle et l'orientation vers l'avenir. Le programme demande d'y intégrer les dimensions ESG, et non de les isoler (F09 § 4) (0,5 pt avec la structure ci-dessous).

**Structure proposée** : quatre axes — (1) contribution financière, (2) clients et métiers, (3) excellence opérationnelle, (4) durabilité (environnement et social). L'axe de durabilité est relié aux trois autres : chaque axe porte un indicateur dont le levier est aussi environnemental (le coût des achats baisse quand la durée de vie s'allonge ; le volume stocké mesure l'hygiène des données ; le service aux clients garantit que la sobriété ne dégrade pas les exigences contractuelles). Les indicateurs actuels de budget et de disponibilité sont conservés dans leurs axes.

| Axe | Indicateur | Formule | Source | Fréquence | Cible | Justification au regard du cas |
|---|---|---|---|---|---|---|
| Contribution financière | Coût annuel des achats d'équipements numériques | nombre d'équipements achetés × prix unitaire payé (neufs et reconditionnés) + coût des révisions à mi-vie | comptabilité fournisseurs (direction administrative et financière), inventaire du parc | trimestrielle, cumul annuel | 0,25 M€ au plus par an à partir de 2029 (0,4 M€ en 2026) | relie l'allongement de la durée de vie à l'économie qu'il procure (environ 0,14 M€ par an) |
| Clients et métiers | Taux de demandes de relevés de température satisfaites dans le délai contractuel | demandes de relevés satisfaites en 48 heures au plus / demandes reçues | portail des clients, outil de suivi des réclamations | mensuelle | 100 % (alerte en dessous de 98 %) | vérifie que la sobriété des données (relevés à cinq minutes, archivage, purge) respecte les contrats |
| Excellence opérationnelle | Volume de données stocké, toutes copies comprises | somme des volumes stockés dans la salle serveurs de Mâcon et chez les hébergeurs | outils de supervision du stockage, rapports des hébergeurs | mensuelle | 250 To au plus en 2030 (400 To en 2026), jalon de 300 To fin 2028 | cible 2030 de l'annexe 1.2 D ; mesure l'application des règles de cycle de vie |
| Durabilité | Durée de vie moyenne des équipements retirés | somme des durées d'usage des équipements retirés sur la période / nombre d'équipements retirés | inventaire du parc tenu par le responsable des systèmes d'information | semestrielle | 5 ans en 2030 (3 ans en 2026) | cible 2030 de l'annexe 1.2 D ; premier levier de l'empreinte (65 %) |

(1,5 pt pour quatre indicateurs complets dont deux reliés aux cibles 2030 ; 1 pt pour trois ; 0,5 pt pour deux.)

Chaque indicateur a un responsable (Mme MERCOIRAN, M. TALBREUX, M. BRÉVANNE) et une fiche qui fixe sa définition et sa méthode, inchangées d'un trimestre à l'autre. L'estimation des émissions (300 t éqCO2, cible 240 t) reste suivie chaque année, avec la même méthode, mais n'est pas un indicateur trimestriel : son incertitude dépasse les variations à piloter.

*1.5 b) – En quoi ce tableau de bord corrige le reporting actuel* (1 pt pour trois arguments ; 0,5 pt pour deux)

1. **Une durabilité intégrée, et non isolée** : aujourd'hui, les chiffres environnementaux sont envoyés une fois par an dans un fichier séparé, que le comité de direction ne voit pas, tandis que le tableau de bord trimestriel ne mesure que les coûts et la disponibilité ; le nouveau tableau de bord place la durabilité dans le même document, chaque trimestre, à côté des coûts et du service, comme le demande Mme DUCHASTEL.
2. **Des cibles, une trajectoire et des sources** : « Électricité : 600 MWh — Stockage : 400 To — CO2 : 300 t » ne dit ni d'où viennent les chiffres, ni comment ils sont calculés, ni où il faut aller ; chaque indicateur porte désormais une cible 2030 et des jalons, une source et une méthode stable, ce qu'exige M. DORMAELS à partir du deuxième trimestre 2027 ; des indicateurs physiques suivis par la filiale remplacent un chiffre de CO2 incertain à 30 %.
3. **Des responsables et des incitations** : les équipes de M. BRÉVANNE sont évaluées sur la disponibilité et le budget, rien ne les pousse à garder un terminal ou à supprimer des données ; avec des indicateurs de durée de vie et de volume stocké, examinés par le comité du numérique responsable (question 1.4) et repris dans les objectifs des équipes, la sobriété devient un résultat attendu.
4. **Un équilibre vérifié** (argument accepté à la place de l'un des trois précédents) : l'indicateur de délai de restitution des relevés empêche qu'un gain environnemental se fasse au détriment des clients.

**Réponses tolérées**
- Quatre axes classiques du Balanced Scorecard, avec des indicateurs ESG répartis dans chaque axe, si la durabilité est intégrée et non isolée.
- Indicateurs différents, s'ils sont complets et tirés des annexes : par exemple ceux de la liste ci-dessous.

| Axe | Indicateur | Formule | Source | Fréquence | Cible |
|---|---|---|---|---|---|
| Durabilité (environnement) | Consommation électrique du SI | consommation de la salle serveurs de Mâcon + consommation attribuée par les hébergeurs | compteur de la salle serveurs, rapports des hébergeurs | trimestrielle | 480 MWh au plus en 2030 (600 MWh en 2026) |
| Durabilité (environnement) | Part des équipements achetés reconditionnés | équipements reconditionnés achetés / équipements achetés dans l'année | inventaire du parc, commandes | semestrielle | 30 % en 2030 (0 % en 2026) |
| Clients et métiers | Note EcoIndex moyenne des cinq pages du portail des clients les plus consultées | moyenne des notes EcoIndex des cinq pages les plus consultées | mesure EcoIndex trimestrielle, statistiques du portail | trimestrielle | note C au moins fin 2028 (F pour la page de suivi des températures en 2026) |

**Erreurs fréquentes**
- *Indicateurs ESG isolés* (exclusion du programme 1.2 ; `ET-18`) — un cinquième onglet « environnement » sans lien avec les autres axes ; juste : axes reliés, leviers communs.
- *Indicateurs incomplets ou génériques* (`JUR-A02` distinguer et justifier les indicateurs ; `ET-18`) — « réduire le CO2 » sans formule, source, fréquence ni cible.
- *Pilotage sur la seule estimation des émissions* (`ET-38` ; `JUR-D06` prudence d'interprétation) — juste : indicateurs physiques, estimation annuelle à méthode constante.
- *Arguments sans lien avec l'annexe 1.4* (`JUR-T08` exploiter toutes les annexes) — critique générale d'un tableau de bord ; juste : fichier séparé, absence de cible et de source, incitations des équipes.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Balanced Scorecard (Kaplan et Norton, 1992) | principe du tableau de bord équilibré | F09 § 4 | notion de cours |
| IT Balanced Scorecard (Van Grembergen) | axes appliqués au SI | `van_grembergen_it_bsc` / F09 § 4 | publié |
| Indicateurs d'impact environnemental du SI (durée de vie, consommation, EcoIndex) | indicateurs de durabilité | F14 § 4 | notion de cours |
| EcoIndex | indicateur toléré | `ecoindex` / F14 § 4 | outil en ligne |
