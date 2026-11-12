# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 5

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Rendre le système d'information sobre et durable et en piloter les résultats | 14 | 1.1 à 1.5 | `exercices/ex13_sobriete_si_logistique_froid` |
| 2 – Préparer l'intégration du système d'information d'un transporteur acquis | 13 | 2.1 à 2.5 | `exercices/ex14_integration_si_acquisition` |
| 3 – Éclairer la décision d'adhérer au socle SI du groupe | 13 | 3.1 à 3.5 | `exercices/ex15_socle_si_groupe_filiale` |
| **Total** | **40** | | |

---

## DOSSIER 1 – RENDRE LE SYSTÈME D'INFORMATION SOBRE ET DURABLE ET EN PILOTER LES RÉSULTATS (14 points)

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

---

## DOSSIER 2 – PRÉPARER L'INTÉGRATION DU SYSTÈME D'INFORMATION D'UN TRANSPORTEUR ACQUIS (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Urbanisation et cible de convergence | `1.3.a` Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) ; `1.3.c` Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle | 3 |
| 2.2 Référentiels communs | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) | 3 |
| 2.3 Échanges avec les chargeurs | `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 2 |
| 2.4 Impacts sur les métiers de Transports CAUVERLIN | `1.3.e` Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers | 2 |
| 2.5 Valeur, reprise et gouvernance des données | `2.3.f` Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.3.a` Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques | 3 |
| **Dossier 2 – Préparer l'intégration du système d'information d'un transporteur acquis** |  | **13** |

Répartition indicative : connaissances (principes de l'urbanisation, données de référence, caractérisation des trois architectures orientées données, interopérabilité, transformation des métiers, donnée comme actif immatériel) 3 points (items 2.1 a-1, 2.2 a-1, 2.2 b-1 pour moitié, 2.3-1, 2.4-1, 2.5 a-1) ; analyse des annexes et recommandations 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Urbanisation et cible de convergence (3 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.a` « Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) » ; `1.3.c` « Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle ».

**Annexes mobilisées** : annexes 1.1 (activité, plan « ORMESTAL 2030 », organigramme), 2.1 (les deux systèmes d'information, calendrier et contraintes) et 2.3 (témoignages des exploitants, de la responsable du transport et du chargeur).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Urbanisation définie comme démarche stratégique (analogie de la ville, zones, quartiers, îlots) et deux de ses règles (une fonction implantée une seule fois, référentiels uniques, échanges par une zone d'échange) | 0,5 |
| a-2 | Diagnostic tiré de l'annexe 2.1 : deux recouvrements, deux ruptures de flux, deux fonctions sans application, chacun appuyé sur un fait ; 1 pt pour six éléments justes ; 0,5 pour trois à cinq ; 0 en deçà | 1 |
| b-1 | Cible organisée par zones (relation et échanges avec les clients, opérations, gestion et comptabilité, référentiels, pilotage, échanges), schéma ou tableau lisible | 0,5 |
| b-2 | Sort de chaque application ou outil (repris, remplacé, abandonné) justifié par les annexes : fin de maintenance au 30 septembre 2027, départ du fondateur, mutualisation des tournées, doubles saisies ; 0,5 si les décisions sont justes mais non justifiées | 1 |

**Réponse attendue**

*2.1 a) – Principes de l'urbanisation et diagnostic*

**Urbaniser** le système d'information, c'est l'organiser, par analogie avec l'urbanisme d'une ville, en blocs fonctionnels faiblement couplés pour qu'il évolue au rythme de la stratégie sans être reconstruit à chaque changement. Le SI est découpé en **zones** (grands domaines : relation avec les clients, opérations, gestion, référentiels, pilotage, échanges), en **quartiers** (sous-domaines : entreposage, transport, facturation) et en **îlots** (ensembles cohérents de fonctions portés par une application : planification des tournées, suivi de l'exécution). Ses règles : une fonction n'est implantée qu'une fois, une donnée de référence a un seul propriétaire, les applications échangent par une zone d'échange plutôt que par des liaisons et des ressaisies au cas par cas. C'est une démarche stratégique, au service des processus et du plan « ORMESTAL 2030 » (intégrer en moins d'un an), et non un inventaire de logiciels (F03 § 1) (0,5 pt).

Diagnostic des deux SI (1 pt pour six éléments justes ; 0,5 pour trois à cinq ; 0 en deçà) :

| Constat | Fait de l'annexe 2.1 | Conséquence |
|---|---|---|
| **Recouvrement 1** : deux îlots de planification des tournées | logiciel de gestion du transport d'ORMESTAL France, qui propose les tournées ; chez Transports CAUVERLIN, tableur de planification et ancien logiciel de transport | deux façons de planifier dans le même quartier transport ; aucune mutualisation possible des camions qui « se croisent chez les mêmes clients » dans l'Ain (Mme VALDRESSE) |
| **Recouvrement 2** : plusieurs fichiers pour les mêmes clients, sites et camions | fichier des clients en deux exemplaires chez ORMESTAL France, rapprochés à la main chaque semaine ; fichier du fondateur chez Transports CAUVERLIN ; 30 chargeurs communs et environ 1 000 sites connus sous deux identifiants ; camions identifiés par numéro de parc d'un côté, par immatriculation de l'autre | les mêmes clients et sites n'ont pas le même identifiant, et les camions relèvent de deux règles d'identification (numéro de parc, immatriculation) : aucun rapprochement automatique, tarifs divergents pour 12 chargeurs communs |
| **Rupture 1** : la commande de transport est saisie trois fois | courriel ou téléphone → tableur de planification → ancien logiciel → ressaisie des exports par le cabinet d'expertise comptable | deux heures de saisie par jour et par exploitante (Mme ESTARDEL), erreurs de recopie, facturation tardive |
| **Rupture 2** : les relevés de température ne circulent pas | enregistreurs lus au retour du camion, relevé envoyé à la demande du chargeur | relevé obtenu « parfois une semaine plus tard » contre 48 heures exigées par les enseignes (Mme SORVIGNAC) |
| **Rupture 3** (variante acceptée) : les tarifs passent par courriel | tableur du fondateur envoyé chaque mois au cabinet | tarifs appliqués à la main, 5 % de factures donnant lieu à un avoir |
| **Fonction sans application 1** : suivi en temps réel des tournées | aucun camion de Transports CAUVERLIN n'est équipé de télématique : suivi par téléphone | ni heure d'arrivée, ni preuve de livraison, ni alerte de température |
| **Fonction sans application 2** : gestion des tarifs et des données de référence | tarifs et clients dans le tableur personnel du fondateur ; contraintes des sites dans les onglets des exploitants | aucune règle, aucun contrôle, savoir détenu par des personnes |
| **Fonction sans application 3** (variante acceptée) : mise à disposition des documents aux chargeurs | aucun portail chez Transports CAUVERLIN | chargeurs servis à la demande, sans délai garanti |

*2.1 b) – Cible de convergence zone par zone*

| Zone (quartiers) | Cible | Sort des applications et outils, et justification |
|---|---|---|
| **Relation et échanges avec les clients** (prise de commande, documents de livraison) | portail des clients et échanges normalisés d'ORMESTAL France, ouverts aux 120 chargeurs de Transports CAUVERLIN (question 2.3) | portail **repris et étendu** ; courriels, appels et espace partagé **remplacés** par le portail ou par l'échange automatisé : fin de la première saisie et délai de 48 heures tenu |
| **Opérations** – quartier transport (planification, exécution, preuves de livraison) | un seul logiciel de gestion du transport pour les 345 camions (260 + 85), télématique sur tous les camions | logiciel de gestion du transport d'ORMESTAL France **repris** et étendu aux deux exploitants : seul outil maintenu, il permet la mutualisation des tournées ; ancien logiciel de transport **remplacé** avant le 30 septembre 2027, date de fin de sa maintenance, après reprise de son historique ; tableur de planification **abandonné**, les contraintes des sites qu'il contient étant reprises dans le référentiel des sites ; télématique **reprise** et installée sur les 85 camions : suivi, preuve de livraison et relevés transmis en continu |
| **Opérations** – quartier entreposage | logiciel de gestion des entrepôts inchangé | **repris** sans changement : Transports CAUVERLIN n'a pas d'entrepôt ; la cible relie seulement les expéditions au logiciel de transport unique |
| **Gestion** (tarifs, facturation, comptabilité) | logiciel de gestion comptable et commerciale d'ORMESTAL France, tenu pour Transports CAUVERLIN comme société distincte | logiciel **repris** : grilles de tarifs datées, facturation calculée à partir des tournées réalisées ; tableur des tarifs du fondateur **abandonné** après reprise des grilles datées ; ressaisie par le cabinet d'expertise comptable **abandonnée** (le maintien d'une mission du cabinet relève de la directrice administrative et financière) |
| **Référentiels** (clients, sites de livraison, véhicules, tarifs) | référentiels uniques et gouvernés (question 2.2) | fichiers du fondateur et fichiers en double d'ORMESTAL France **remplacés** par les référentiels : fin du rapprochement hebdomadaire à la main |
| **Pilotage** | tableaux de bord communs du transport (ponctualité, remplissage des camions, chiffre d'affaires par chargeur) alimentés par le logiciel unique | à construire après la bascule ; aucun outil de Transports CAUVERLIN à reprendre |
| **Échanges** (zone transverse) | échanges entre applications et avec les chargeurs par des interfaces normalisées, sans ressaisie | remplace les exports manuels et les courriels |

Ce qui est repris de Transports CAUVERLIN n'est donc pas un logiciel mais un **patrimoine** : l'historique des tournées, les contraintes des sites, les tarifs négociés et le savoir-faire des exploitants (question 2.5). Le candidat peut représenter la cible par un schéma en blocs emboîtés (zones contenant les quartiers et les îlots, flèches vers la zone d'échange), légendé et commenté en trois ou quatre phrases.

**Réponses tolérées**
- Découpage des zones différent (par exemple une zone « exécution du transport » distincte de la planification, ou les référentiels rangés dans une zone « données ») s'il respecte la logique zones, quartiers, îlots et s'applique aux deux SI.
- Fonctions sans application autres que celles du tableau (optimisation des tournées faite à la main, absence d'outil de gestion des sauvegardes), si elles sont tirées des annexes.
- Maintien provisoire de l'ancien logiciel en consultation seule pour l'historique, jusqu'à la fin de la reprise, si la date du 30 septembre 2027 est prise en compte.
- Cartographie présentée en tableau plutôt qu'en schéma (format libre).
- Mention, pour la zone gestion, de l'adoption ultérieure du socle SI commun du groupe annoncée par la présentation, sans développement ; elle ne remet pas en cause la reprise du logiciel d'ORMESTAL France en 2027.

**Erreurs fréquentes**
- *Urbanisation réduite à un inventaire technique* (`ET-20`, `JUR-G07` le pourquoi puis le comment de l'urbanisation) — lister des serveurs ou des postes ; juste : zones, quartiers, îlots au service des processus de transport et de facturation.
- *Garder les deux SI côte à côte sans décision argumentée* (`JUR-G09` mise en cohérence de SI inter-organisationnels : décision argumentée et accompagnement du changement) — alors que l'ancien logiciel n'est plus maintenu après le 30 septembre 2027 et que le plan impose l'intégration en moins d'un an.
- *Diagnostic sans faits de l'annexe* (`JUR-T01` morceau de cours) — « il y a des doublons » sans dire lesquels ; juste : 30 chargeurs communs, triple saisie, relevés envoyés en une semaine.
- *Schéma illisible ou non légendé* (`JUR-T10`).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Urbanisation du SI (zones, quartiers, îlots ; règles d'urbanisme) | définition, découpage, démarche | F03 § 1 et § 6 | notion de cours [S] |
| Cartographies fonctionnelle et applicative | repérage des recouvrements et des ruptures | F03 § 2 | notion de cours |

---

### 2.2 – Référentiels communs (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) ».

**Annexes mobilisées** : annexes 1.1 (organigramme : propriétaires possibles), 2.1 (identifiants actuels, calendrier), 2.2 (volumes, constats de qualité, options) et 2.3 (témoignages).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Données de référence définies (données partagées, stables, utilisées par plusieurs processus et applications, gérées une seule fois) et gestion d'un référentiel de données maîtres | 0,5 |
| a-2 | Trois référentiels organisés : identifiant unique, règle de rapprochement, propriétaire métier, appliqués aux constats de l'annexe 2.2 ; 0,5 pour deux référentiels complets | 1 |
| b-1 | Trois options caractérisées et comparées selon trois critères appliqués au cas (réponse au besoin des opérations, qualité des données à la source, coût sur trois ans et délai) | 1 |
| b-2 | Recommandation justifiée (référentiel de données maîtres, entrepôt ultérieur pour le pilotage, lac écarté) et compatible avec le calendrier | 0,5 |

**Réponse attendue**

*2.2 a) – Données de référence et organisation des trois référentiels*

Les **données de référence** (*master data*) sont les données partagées et relativement stables qui décrivent les objets de l'activité (clients, sites, véhicules, tarifs) et que plusieurs processus et applications utilisent ; elles doivent exister **une seule fois**, sous un identifiant unique, avec un propriétaire. La gestion des données maîtres (*Master Data Management*, à écrire en toutes lettres pour ne pas la confondre avec la gestion des terminaux mobiles) est la discipline et l'outil qui les créent, les contrôlent et les diffusent aux applications (F07 § 1 et § 6.2) (0,5 pt).

| Référentiel | Identifiant unique | Règle de rapprochement des fiches des deux sociétés | Propriétaire (et intendant) |
|---|---|---|---|
| **Clients** (400 + 120, dont 30 communs, soit 490) | code client unique de l'ensemble, attribué par le référentiel ; les 30 chargeurs communs conservent leur code à cinq chiffres d'ORMESTAL France | numéro SIREN d'abord (à compléter pour la moitié des fiches de Transports CAUVERLIN qui ne l'ont pas), puis raison sociale normalisée et adresse ; les 140 fiches ramenées à 120 chargeurs ; une fiche par chargeur, ses établissements rattachés | Mme MERCOIRAN, directrice administrative et financière, car le client porte la facturation et les tarifs ; intendant : un collaborateur de la facturation |
| **Sites de livraison** (6 000 + 2 500, dont environ 1 000 communs, soit environ 7 500) | code site attribué par le référentiel, et non l'adresse, qui varie selon la saisie | adresse normalisée (code postal, voie, commune) et enseigne, complétées par le code du magasin chez l'enseigne quand il existe ; environ 1 000 sites communs fusionnés ; horaires de réception, quai et contraintes d'accès deviennent des informations de la fiche ; création réservée aux intendants, ce qui corrige aussi le défaut d'ORMESTAL France | Mme VALDRESSE, responsable du transport ; intendants : les deux exploitants de Transports CAUVERLIN pour les sites de l'Ain, qui en connaissent les contraintes |
| **Véhicules** (260 + 85) | numéro de parc unique, étendu aux 85 camions, y compris les 12 camions loués | immatriculation (et numéro d'identification du véhicule) conservée comme attribut daté, et non comme identifiant, puisqu'elle change à chaque renouvellement d'une location | Mme VALDRESSE, responsable du transport (ou M. DRAVIGNOL, directeur des opérations) ; intendant : le gestionnaire du parc |

Les tarifs sont rattachés au client du référentiel et portent obligatoirement une date d'effet. Le responsable des systèmes d'information administre l'outil ; il n'est propriétaire d'aucun référentiel (1 pt ; 0,5 pour deux référentiels complets).

*2.2 b) – Comparaison des options et recommandation*

Un **référentiel de données maîtres** gère à la source les données partagées et les diffuse aux applications ; un **entrepôt de données** rassemble, après coup, des données intégrées, historisées et non volatiles pour l'analyse ; un **lac de données** stocke des données brutes, hétérogènes, dont la structure n'est définie qu'à la lecture (F07 § 6) (0,5 pt sur l'item b-1).

| Critère | Option 1 – Référentiel de données maîtres | Option 2 – Entrepôt de données commun | Option 3 – Lac de données |
|---|---|---|---|
| Réponse au besoin des opérations (identifiants communs dans le logiciel de transport, le portail, la facturation) | oui : les applications utilisent le même client, le même site, le même camion ; condition de la mutualisation des tournées | non : chaque application garde ses fichiers ; les doubles saisies demeurent ; utile au pilotage seulement | non : aucun rapprochement ; les fichiers restent dans leur état |
| Qualité et cohérence des données | contrôlées à la création (SIREN, adresse complète, date d'effet), avec un propriétaire par référentiel | rapprochement chaque nuit, a posteriori : les erreurs sont constatées, non évitées | risque de « marécage de données » : 20 doublons, 500 adresses incomplètes et 100 grilles non datées déposés tels quels |
| Coût sur trois ans et délai | 150 + 3 × 30 = 240 k€ ; 5 mois | 100 + 3 × 20 = 160 k€ ; 4 mois | 80 + 3 × 40 = 200 k€ ; 3 mois |

(0,5 pt sur l'item b-1 pour la comparaison selon trois critères appliqués.)

**Recommandation** : l'**option 1**. C'est la plus chère (80 k€ de plus que l'entrepôt sur trois ans), mais c'est la seule qui supprime la cause des difficultés, à savoir des objets identifiés différemment et créés sans règle : elle met fin aux doubles saisies (deux heures par jour et par exploitante), aux avoirs sur les tarifs (5 % des factures) et permet la mutualisation des tournées. Elle doit être lancée dès avril pour être prête en cinq mois, avant la seconde vague de septembre ; les référentiels des clients et des sites passent en premier, celui des véhicules suit avec la pose de la télématique. L'entrepôt (option 2) pourra venir ensuite, alimenté par des données déjà rapprochées, pour les tableaux de bord communs. Le lac (option 3) est écarté : il ne crée aucun identifiant commun et coûte le plus cher en fonctionnement (40 k€ par an) (0,5 pt).

**Réponses tolérées**
- Autres propriétaires, s'ils sont des responsables métier justifiés : directeur des opérations pour les sites et les véhicules, responsable du transport pour les clients si l'on retient le point de vue de l'exploitation.
- Code client des deux sociétés conservé avec une table de correspondance gérée par le référentiel, si l'identifiant de l'ensemble est unique.
- Recommandation combinant les options 1 et 2 dès le départ, si le candidat montre que l'entrepôt ne remplace pas le référentiel et que le calendrier le permet.
- Autres critères de comparaison (organisation requise, adéquation au calendrier du 30 septembre 2027, risque de dépendance à des spécialistes rares), s'ils sont appliqués aux options.

**Erreurs fréquentes**
- *Sigle MDM sans précision* (`ET-13`) — confusion avec la gestion des terminaux mobiles ; juste : gestion des données maîtres, écrite en toutes lettres.
- *Entrepôt et lac confondus, ou lac présenté comme un entrepôt moderne* (`ET-24`) — juste : l'entrepôt intègre et structure pour l'analyse, le lac stocke du brut ; ni l'un ni l'autre ne fournit d'identifiants aux applications.
- *Propriétaire du référentiel = responsable des systèmes d'information* — juste : un responsable métier décide des règles et de la qualité ; la fonction SI administre l'outil (F07 § 8.1).
- *Immatriculation ou adresse retenue comme identifiant* — elles changent (12 camions loués, adresses incomplètes) ; juste : un identifiant attribué par le référentiel.
- *Modèle conceptuel ou logique des données dessiné* (`ET-23`) — non demandé : l'énoncé exclut tout modèle de données.
- *Choix fondé sur le seul coût* (`JUR-T03` analyser et argumenter) — retenir l'option la moins chère sans examiner si elle répond au besoin.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK (2e édition, 2017, révision 2024) | domaine « données de référence et données maîtres », rôles de propriétaire et d'intendant | `dama_dmbok2` / F07 § 8.2 | en vigueur (référentiel, non norme) |
| Données de référence, entrepôt, lac, référentiel de données maîtres | définitions et choix | F07 § 1 et § 6.2 | notion de cours |
| Rôles de propriétaire et d'intendant des données | gouvernance des référentiels | F07 § 8.1 | notion de cours (illustratif) |

---

### 2.3 – Échanges avec les chargeurs (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) » ; `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ».

**Annexes mobilisées** : annexes 2.1 (échanges d'ORMESTAL France et de Transports CAUVERLIN, calendrier et contraintes), 2.2 (chargeurs communs) et 2.3 (témoignage de Mme SORVIGNAC).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Interopérabilité définie, avec ses dimensions technique (formats, interfaces), sémantique (mêmes identifiants, même sens) et organisationnelle (processus, responsabilités) | 0,5 |
| 2 | Deux choix techniques adaptés aux chargeurs (échange automatisé au format normalisé ou par API pour les chargeurs équipés ; portail pour les autres ; preuves et relevés transmis par la télématique et mis à disposition sous 48 heures) | 0,5 |
| 3 | Trois dispositions organisationnelles : accord d'échange, responsabilités, calendrier de bascule en vagues hors période de pointe ; 0,5 pour deux | 1 |

**Réponse attendue**

L'**interopérabilité** est la capacité de systèmes différents, ici ceux d'ORMESTAL France et des chargeurs, à échanger des données et à les utiliser sans intervention manuelle. Elle a une dimension **technique** (formats normalisés ou ouverts comme XML ou JSON, interfaces de programmation), une dimension **sémantique** (une commande désigne le même client, le même site et la même date pour les deux parties, grâce aux identifiants des référentiels de la question 2.2) et une dimension **organisationnelle** (processus, engagements, responsabilités) ; le programme exige les deux plans, technique et organisationnel (F07 § 7) (0,5 pt).

**Deux choix techniques** (0,5 pt) :
1. **Commandes** : les chargeurs qui transmettent déjà leurs commandes à ORMESTAL France par échange automatisé (70 % de ses clients), comme la Fromagerie BRÉMACIER parmi les 30 chargeurs communs, utilisent le même échange, au format normalisé, pour les livraisons de l'ancien périmètre de Transports CAUVERLIN, ou l'interface de programmation du logiciel de gestion du transport ; les autres chargeurs, qui commandent aujourd'hui par courriel, par téléphone ou par l'espace partagé, saisissent leurs commandes sur le portail des clients. La commande entre ainsi une seule fois, directement dans le logiciel de transport.
2. **Preuves de livraison et relevés de température** : produits par la télématique installée sur les 85 camions (signature sur la tablette, températures du caisson), ils sont mis à disposition automatiquement sur le portail et, pour les chargeurs qui le demandent, par l'interface de programmation, dans un format ouvert ; le délai de 48 heures exigé par les enseignes est tenu sans demande du chargeur.

**Trois dispositions organisationnelles** (1 pt ; 0,5 pour deux) :
1. **Accord d'échange** avec chaque chargeur raccordé : contenu de la commande et identifiants utilisés (code client et code site du référentiel), heure limite de transmission pour une livraison le lendemain, délai de mise à disposition des preuves et des relevés, confidentialité, traitement des messages rejetés. Pour les chargeurs qui passent au portail, des conditions d'utilisation et une formation courte.
2. **Responsabilités** : un interlocuteur unique chez ORMESTAL France pour chaque chargeur (attente de Mme SORVIGNAC) ; un correspondant chez le chargeur ; le propriétaire du flux (responsable du transport) répond de sa disponibilité ; une procédure écrite dit qui détecte un échange en échec, qui prévient l'autre partie et comment la commande est passée en secours (portail ou téléphone, avec saisie unique par l'exploitant).
3. **Calendrier de bascule** par vagues, compatible avec les dates de l'annexe 2.1 C : en juin 2027, en pilote, les 30 chargeurs communs, déjà raccordés à ORMESTAL France et dont les codes clients existent déjà dans ses applications ; en septembre, les 90 autres chargeurs, avant l'arrêt de la maintenance de l'ancien logiciel le 30 septembre 2027 ; période de fonctionnement en parallèle de deux à trois semaines pour chaque vague ; aucune bascule de la mi-novembre à la fin de décembre ; chaque chargeur est informé de sa date au moins un mois à l'avance. Le pilote s'appuie sur les codes clients et sites déjà présents dans les applications d'ORMESTAL France pour ces chargeurs (la plupart de leurs sites figurent parmi les quelque 1 000 sites déjà connus) ; les camions de Transports CAUVERLIN affectés au pilote sont équipés de la télématique en priorité ; le référentiel de données maîtres, livré fin août, reprend ces fiches avant la seconde vague.

**Réponses tolérées**
- Échange de données informatisé cité comme exemple de format normalisé, sans détail de sa syntaxe.
- Calendrier différent (par exemple trois vagues, ou les chargeurs par téléphone basculés en dernier) s'il respecte le 30 septembre 2027, la période de pointe et l'objectif de moins d'un an.
- Pilote placé après la livraison du référentiel (début septembre), si la seconde vague reste achevée avant le 30 septembre 2027 ou si le maintien de l'ancien logiciel en consultation seule est justifié.
- Maintien, pour quelques petits chargeurs, d'une commande par téléphone saisie une seule fois par l'exploitant dans le logiciel de transport, si le choix est justifié.

**Erreurs fréquentes**
- *Interopérabilité traitée sous le seul angle technique* (`ET-36`) — juste : formats et interfaces, mais aussi mêmes identifiants, accord d'échange, responsabilités et calendrier.
- *Description détaillée des normes d'échange ou des messages* — hors programme (le programme exclut l'approfondissement technique des échanges) ; une mention des formats suffit.
- *Facturation électronique traitée à la place des commandes et des preuves de livraison* — hors du sujet de la question.
- *Témoignage de la Fromagerie BRÉMACIER ignoré* (`JUR-T08`) — un seul interlocuteur, un seul format, pas de bascule pendant les fêtes, procédure en cas d'échec.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Interopérabilité : niveaux technique, syntaxique, sémantique, organisationnel | définition et dimensions | F07 § 7 ; F03 § 3 | notion de cours [S] |
| Référentiel général d'interopérabilité (RGI), version 2.0 | exemple de cadre de recommandations sur les normes et standards, propre aux administrations (réponse tolérée, non attendue) | `rgi_v2` / F07 § 7 | en vigueur |

---

### 2.4 – Impacts sur les métiers de Transports CAUVERLIN (2 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.e` « Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers ».

**Annexes mobilisées** : annexes 1.1 (organigramme), 2.1 (outils actuels, calendrier) et 2.3 (témoignages de M. CAUVERLIN, de Mme ESTARDEL, de M. MORLANDIER, de Mme VALDRESSE et de Mme MERCOIRAN).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Transformation des métiers caractérisée : la nouvelle architecture déplace le travail de la production (saisie, construction) vers la supervision, le contrôle et la relation, et modifie compétences, responsabilités et contrôles | 0,5 |
| 2 | Impact organisationnel sur le métier d'exploitant, appuyé sur les témoignages, et une mesure d'accompagnement | 0,5 |
| 3 | Impact juridique sur la responsabilité en cas d'erreur de planification, et une mesure (validation humaine tracée, motifs des modifications) | 0,5 |
| 4 | Impact comptable sur la piste d'audit et l'arrêté des comptes, et une mesure (facturation à partir des tournées réalisées, tarifs datés, rapprochement mensuel) | 0,5 |

**Réponse attendue**

Une nouvelle architecture ne change pas seulement les outils : en automatisant la saisie et en centralisant les données, elle **transforme les métiers**, qui passent de la production (saisir, construire, recopier) à la **supervision** (vérifier, arbitrer, traiter les exceptions) et à la relation avec les clients. Elle modifie les compétences attendues, la répartition des responsabilités et les contrôles, qui s'appuient désormais sur des traces informatiques (programme 1.3.e ; guide p. 349 : évolution des métiers vers la supervision et le conseil, responsabilité en cas d'erreur, piste d'audit) (0,5 pt).

| Impact | Analyse à partir de l'annexe 2.3 | Mesure d'accompagnement |
|---|---|---|
| **Organisationnel** : le métier d'exploitant (0,5 pt) | les exploitants ne construiront plus les tournées sur le tableur ni ne ressaisiront les commandes (deux heures par jour libérées) : ils vérifieront les propositions du logiciel, traiteront les imprévus et parleront aux clients, comme chez ORMESTAL France (Mme VALDRESSE) ; crainte de devenir « une presse-bouton » (Mme ESTARDEL) ; risque de perdre la connaissance fine des sites qui fait la fidélité des clients (M. CAUVERLIN) | associer les deux exploitants à la reprise des contraintes des sites et en faire les intendants du référentiel des sites de l'Ain ; formation au logiciel en binôme avec des exploitants d'ORMESTAL France ; démarche de conduite du changement qui valorise le rôle d'arbitre et de conseil |
| **Juridique** : la responsabilité en cas d'erreur de planification (0,5 pt) | le logiciel propose, l'exploitant valide : envers le chargeur, la société reste responsable de la prestation ; en interne, il faut pouvoir établir qui a décidé quoi, si la proposition ignorait une contrainte (« le mardi matin ») ou si une modification a causé l'erreur (M. MORLANDIER) ; les preuves de livraison et les relevés horodatés deviennent les éléments de preuve en cas de litige sur une marchandise perdue | validation humaine obligatoire de chaque tournée ; journal des propositions, des validations et des modifications avec leur motif et leur auteur ; contraintes des sites saisies dans le référentiel pour que le logiciel les respecte ; règles de délégation de validation écrites ; les données personnelles des conducteurs recueillies par la télématique sont inscrites au registre des traitements (mention, sans analyse juridique) |
| **Comptable** : la piste d'audit et l'arrêté des comptes (0,5 pt) | aujourd'hui, on ne peut pas remonter d'une facture à la tournée et à la commande ; 5 % des 1 400 factures annuelles donnent lieu à un avoir faute de tarif daté ; les tournées réalisées non facturées au 31 décembre ont été estimées à la main ; dix semaines pour arrêter les comptes de 2026 (Mme MERCOIRAN) ; avec un identifiant commun, chaque montant facturé se rattache à une tournée réalisée, à une preuve de livraison et à une commande | facturation calculée par le logiciel de gestion comptable et commerciale à partir des tournées réalisées dès le 1er octobre 2027, avec des tarifs datés ; rapprochement mensuel des tournées réalisées et des tournées facturées ; liste des prestations réalisées non facturées produite par le logiciel au 31 décembre 2027 ; objectif d'arrêté en quatre semaines |

**Réponses tolérées**
- Impact organisationnel portant sur le fondateur (passage de la négociation au cas par cas à des grilles tarifaires gouvernées) ou sur le cabinet d'expertise comptable, si le métier d'exploitant est aussi traité.
- Reprise de la comptabilité de Transports CAUVERLIN dans le logiciel d'ORMESTAL France à l'ouverture de l'exercice 2028 plutôt qu'en cours d'exercice, si la facturation bascule plus tôt et si le choix est justifié.
- Mesures de conduite du changement formulées selon un modèle connu (ADKAR, huit étapes de Kotter : F05 § 7), si elles sont appliquées aux exploitants.

**Erreurs fréquentes**
- *« Le logiciel est responsable de l'erreur »* — un logiciel n'est pas responsable : la société répond envers le chargeur et la décision validée par l'exploitant doit être tracée.
- *Développement de droit du travail (fiche de poste, temps de travail) ou de droit des transports (lettre de voiture, responsabilité du voiturier)* — exclu par l'énoncé ; juste : responsabilité, preuve et traçabilité dans le SI.
- *Transformation des métiers présentée comme une simple suppression de postes ou de tâches* (`JUR-D03` transformation des métiers et compétences) — juste : déplacement vers la supervision, le contrôle et la relation, compétences nouvelles.
- *Témoignages non exploités* (`JUR-T08`).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Effets métiers des nouvelles architectures (production → supervision, responsabilité en cas d'erreur, piste d'audit) | transformation des métiers | programme 1.3.e ; guide p. 349 | notion de cours |
| Conduite du changement : résistances, leviers | accompagnement des exploitants | F05 § 7 | notion de cours |
| ADKAR (Prosci ; Hiatt, 2003) ; huit étapes de Kotter (1995-1996) | modèles de conduite du changement (réponse tolérée) | `adkar`, `kotter_8_etapes` / F05 § 7 | publiés |
| Piste d'audit dans le SI | traçabilité de la facture à la commande | F10 § 3.2 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | registre des traitements (simple mention) | `rgpd` / F15 § 2 | en vigueur depuis le 25/05/2018 |

---

### 2.5 – Valeur, reprise et gouvernance des données (3 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.f` « Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques » ; `2.3.a` « Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques ».
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ».

**Annexes mobilisées** : annexes 2.1 (outils, calendrier), 2.2 (volumes, constats de qualité, sauvegarde et diffusion) et 2.3 (témoignages de M. CAUVERLIN, des exploitants et de Mme MERCOIRAN).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Donnée présentée comme actif immatériel (ressource maîtrisée, source de valeur d'usage, voire d'échange) et appliquée aux données de Transports CAUVERLIN | 0,5 |
| a-2 | Trois risques (perte, fuite, dépendance à une personne), chacun illustré par un fait des annexes | 0,5 |
| b | Démarche de reprise en quatre étapes (inventaire et profilage, nettoyage, structuration et chargement, contrôle après reprise), appliquée aux chiffres de l'annexe 2.2 ; 0,5 pour deux ou trois étapes justes | 1 |
| c-1 | Trois règles de gouvernance portant sur trois enjeux différents, avec un responsable, appliquées au cas | 0,5 |
| c-2 | Indicateur de qualité complet (formule, source, fréquence, cible, axe), relié à un constat | 0,5 |

**Réponse attendue**

*2.5 a) – Les données, actif immatériel, et leurs risques*

Une donnée est un **actif immatériel** quand l'entreprise la maîtrise et qu'elle en tire une valeur durable : une **valeur d'usage** (mieux décider, mieux servir, gagner du temps) et, parfois, une **valeur d'échange** ; c'est un patrimoine qu'il faut inventorier, protéger et entretenir (F07 § 8.6) (0,5 pt). Les données de Transports CAUVERLIN en sont un : l'historique d'environ 200 000 tournées de 2016 à 2026 renseigne sur les volumes, les délais et les incidents de chaque liaison et servira au calcul des tournées mutualisées ; les contraintes des 2 500 sites sont le savoir-faire qui fidélise les clients ; les 300 grilles de tarifs traduisent la relation commerciale avec 120 chargeurs. Ces données font partie de ce qu'ORMESTAL France a acquis le 4 janvier 2027 ; leur valeur se perd si elles ne sont pas reprises.

Trois risques (0,5 pt) :
- **Perte** : l'ancien logiciel n'est plus maintenu après le 30 septembre 2027 ; sa sauvegarde est faite sur un disque externe rangé dans le bureau du fondateur et n'a jamais été relue ; une partie de l'historique (horaires réels, incidents) n'existe que dans les tableurs des exploitants.
- **Fuite** : les tarifs, qui sont des données confidentielles, sont tenus sur l'ordinateur portable du fondateur et envoyés chaque mois par courriel ; le fichier a déjà été envoyé par erreur à un chargeur en 2025.
- **Dépendance à une personne** : certains tarifs ne sont écrits que « dans la tête » de M. CAUVERLIN, qui part le 31 décembre 2027 ; les contraintes des sites sont connues des deux seuls exploitants.

*2.5 b) – Démarche de reprise en quatre étapes* (1 pt)

1. **Inventaire et profilage des sources** (collecte) : recenser l'ancien logiciel, les tableurs de planification, le fichier des clients et des tarifs, les fichiers de relevés ; mesurer la qualité de chacune (20 doublons sur 140 fiches, SIREN dans la moitié des fiches, 500 adresses incomplètes sur 2 500, 100 grilles sur 300 sans date d'effet) ; décider de ce qui est repris (par exemple les trois dernières années de tournées dans le logiciel de transport, le reste archivé en consultation seule).
2. **Nettoyage** : fusionner les 20 doublons et rattacher les 30 chargeurs communs à leur code d'ORMESTAL France par le SIREN ; compléter les 500 adresses avec les exploitants et les codes des magasins des enseignes ; dater les 100 grilles avec M. CAUVERLIN avant son départ, puis les faire confirmer par les chargeurs ; faire arbitrer par la direction le tarif retenu pour les 12 chargeurs communs qui ont deux tarifs pour une même liaison.
3. **Structuration et chargement** : attribuer à chaque objet l'identifiant du référentiel (client, site, véhicule), convertir les données aux formats du logiciel de gestion du transport et du logiciel de gestion comptable et commerciale, charger d'abord dans un environnement d'essai.
4. **Contrôle après reprise** : comptages (140 fiches devenues 120 clients ; environ 1 000 sites fusionnés et environ 1 500 sites nouveaux ; 85 camions), contrôle par échantillon des fiches et des tarifs, recette signée par chaque propriétaire de référentiel, fonctionnement en parallèle pendant la première vague ; l'ancien logiciel n'est arrêté qu'après cette validation et l'archivage de son historique.

*2.5 c) – Trois règles de gouvernance des données de l'ensemble intégré* (0,5 pt pour les règles, 0,5 pt pour l'indicateur)

| Enjeu | Règle | Responsable |
|---|---|---|
| **Qualité** | tout client, site ou véhicule est créé uniquement dans le référentiel, par un intendant, avec des champs obligatoires (SIREN pour un client, adresse complète, horaires et quai pour un site, date d'effet pour un tarif) ; contrôle mensuel de la qualité | propriétaire de chaque référentiel (Mme MERCOIRAN, Mme VALDRESSE) |
| **Sécurité** | les tarifs et les données des clients sont classés confidentiels et ne sont conservés que dans les applications de l'entreprise, avec des droits d'accès par fonction ; aucun fichier de données sur un poste personnel ni envoyé par courriel ; sauvegardes hors des bureaux, relues au moins une fois par trimestre | responsable des systèmes d'information, M. BRÉVANNE, sur décision des propriétaires |
| **Cycle de vie** (ou **conformité**) | durée de conservation fixée pour chaque catégorie (historique des tournées accessible pendant trois ans puis archivé, archives de l'ancien logiciel conservées en consultation seule puis supprimées au terme de la durée de conservation légale ou contractuelle fixée pour chaque catégorie, les tournées réalisées justifiant la facturation : F07 § 8.4) ; ou, pour la conformité, inscription au registre des traitements des données personnelles reprises (contacts chez les chargeurs, conducteurs) | propriétaires des données, avec le responsable des systèmes d'information |

**Indicateur associé à la règle de qualité** :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de fiches complètes des référentiels clients et sites | fiches comportant tous les champs obligatoires de leur type (client : SIREN et adresse ; site : adresse complète, horaires de réception et quai) / fiches actives | référentiel de données maîtres (contrôle automatique des champs obligatoires) | mensuelle | 100 % des fiches créées après la reprise ; au moins 98 % de l'ensemble fin 2027 (aujourd'hui, la moitié des clients de Transports CAUVERLIN sans SIREN et 500 sites incomplets sur 2 500) | processus |

**Réponses tolérées**
- Autres risques (obsolescence de l'ancien logiciel, erreur de reprise), s'ils s'ajoutent aux trois demandés.
- Démarche présentée selon les cinq étapes de la chaîne de traitement (collecte, nettoyage, structuration, analyse, restitution), si le contrôle après reprise y figure.
- Indicateur de qualité différent mais complet : taux de doublons du référentiel clients (doublons détectés / fiches actives, cible 0 %) ou part des grilles de tarifs datées (grilles avec date d'effet / grilles actives, cible 100 %, un tiers sans date aujourd'hui).
- Mention du délégué à la protection des données, s'il est désigné, pour la règle de conformité, sans analyse juridique.

**Erreurs fréquentes**
- *Valeur comptable des données calculée ou inscription au bilan proposée* — exclu par l'énoncé ; juste : valeur d'usage et risques, sans évaluation comptable (F07 § 8.6).
- *Reprise réduite à une copie des fichiers* — les doublons, les adresses incomplètes et les tarifs non datés seraient transférés tels quels ; juste : nettoyer avant de charger, contrôler après.
- *Règles de gouvernance génériques ou sans responsable* (`JUR-T07` répondre à la seule question posée ; `JUR-T01`) — juste : trois règles appliquées aux constats de l'annexe 2.2, chacune avec un propriétaire.
- *Indicateur sans formule ni cible* (`ET-18`).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Donnée comme actif immatériel, risques de perte, de fuite, d'obsolescence | valeur d'usage et risques, sans évaluation comptable | F07 § 8.6 | notion de cours |
| Chaîne de traitement des données (collecte, nettoyage, structuration) | démarche de reprise | F08 § 0, § 1 et § 4 ; F07 § 8.3 | notion de cours |
| ISO/IEC 25012 (modèle de qualité des données) | dimensions complétude, unicité, exactitude | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| DAMA-DMBOK (2e édition, 2017, révision 2024) | gouvernance, qualité, sécurité, cycle de vie | `dama_dmbok2` / F07 § 8.2 | en vigueur (référentiel) |
| Règlement (UE) 2016/679 (RGPD) | registre des traitements (règle de conformité, simple mention) | `rgpd` / F15 § 2 | en vigueur depuis le 25/05/2018 |

---

## DOSSIER 3 – ÉCLAIRER LA DÉCISION D'ADHÉRER AU SOCLE SI DU GROUPE (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Le SI dans la chaîne de valeur de la filiale | `1.1.b` Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 3 |
| 3.2 Choix d'un scénario et feuille de route | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.c` Méthodologies de planification stratégique du SI | 2,5 |
| 3.3 Organisation de la fonction SI entre le groupe et la filiale | `1.2.b` Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 2 |
| 3.4 Risques de l'adhésion au socle | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers | 3,5 |
| 3.5 Coût complet de l'adhésion et refacturation | `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI ; `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI | 2 |
| **Dossier 3 – Éclairer la décision d'adhérer au socle SI du groupe** |  | **13** |

Répartition indicative : connaissances (alignement stratégique, chaîne de valeur, modèles d'organisation de la DSI, typologie des risques, rôle du contrôle de gestion du SI) 2,75 points (items 3.1 a-1, 3.3 a-2, 3.4 a-1, 3.5 a-1, la moitié de 3.1 a-2 et de 3.2 b-2) ; analyse des annexes et recommandations 10,25 points, soit environ 79 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Le SI dans la chaîne de valeur de la filiale (3 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.b` « Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 3.2 (activités et applications, équipe, ce que les clients reconnaissent), 3.1 (périmètre du socle), 3.3 (positions de Mme DUCHASTEL et de M. DRAVIGNOL) et 1.1 (activité, plan « ORMESTAL 2030 »).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Alignement stratégique du SI défini (mise en cohérence permanente de la stratégie SI et de la stratégie de l'organisation, au-delà de l'adéquation technique) | 0,5 |
| a-2 | Chaîne de valeur de la filiale : activités principales et de soutien distinguées, chaque application de l'annexe 3.2 B placée, apport du SI précisé ; 0,5 si l'une des deux familles manque ou si l'apport n'est pas précisé | 1 |
| b-1 | Activités où un socle commun est pertinent (activités de soutien), avec la justification | 0,5 |
| b-2 | Activités où le SI propre porte un avantage concurrentiel (réservation des quais, traçabilité des températures, portail), justifiées par l'annexe 3.2 E | 0,5 |
| b-3 | Deux conditions pour que l'adhésion reste alignée sur la stratégie de la filiale | 0,5 |

**Réponse attendue**

*3.1 a) – Alignement stratégique et chaîne de valeur*

L'**alignement stratégique du système d'information** est la mise en cohérence permanente entre la stratégie de l'organisation et la stratégie de son SI : le SI doit servir les choix qui fondent l'avantage concurrentiel et les objectifs de l'organisation, et ses évolutions se décident à partir d'eux, non à partir des seules considérations techniques. Il est dynamique (à refaire à chaque changement de stratégie) et organisationnel autant que technique (F01 § 1) (0,5 pt). Pour une filiale, il se joue à deux niveaux : avec la stratégie de la filiale (différenciation par la réactivité et la traçabilité, annexe 3.2 E) et avec celle du groupe (plan « ORMESTAL 2030 »).

La **chaîne de valeur** (Porter, 1985) décompose l'activité en activités principales, qui créent directement la valeur perçue par le client, et en activités de soutien, qui les rendent possibles ; le SI y automatise, informe ou transforme chaque maillon (F01 § 2). Appliquée à ORMESTAL France (1 pt) :

| Famille | Activité de la filiale | Application(s) (annexe 3.2 B) | Apport du SI |
|---|---|---|---|
| Principale – logistique interne et opérations | réception, stockage, préparation des commandes, expédition dans les 14 entrepôts | logiciel de gestion des entrepôts ; module de réservation des créneaux de quai | automatise les flux, optimise l'occupation des quais ; **transforme** le service : créneau confirmé en moins de 15 minutes |
| Principale – logistique externe | transport et livraison (260 camions) | logiciel de gestion du transport ; télématique des camions | planifie les tournées ; suit la position et la température des caissons, collecte la preuve de livraison |
| Principale – commercialisation et services | relation avec les clients, service après livraison | portail des clients (suivi, alertes, certificats, preuves, réservation) | **transforme** la relation : alerte de température en temps réel, certificat dès la livraison ; premier motif de satisfaction |
| Soutien – infrastructure de l'entreprise | comptabilité, facturation, trésorerie | logiciel de gestion comptable et commerciale | automatise la facturation à partir des tournées et des prestations ; informe la direction |
| Soutien – approvisionnements | achats (pièces des installations frigorifiques, emballages, carburant, sous-traitance) | logiciel de gestion comptable et commerciale | automatise les commandes et leur validation |
| Soutien – gestion des ressources humaines | paie et gestion administrative de 650 salariés | logiciel de paie | automatise un traitement réglementé |
| Soutien – infrastructure de l'entreprise | communication interne, travail collaboratif | messagerie, agenda, partage de fichiers | coordonne les équipes de Mâcon et des entrepôts |
| Soutien – développement technologique | développement du portail et de la réservation des quais, adaptation des progiciels métiers | équipe SI de la filiale (7 personnes sur les applications métiers) | nourrit l'avantage des activités principales |

*3.1 b) – Socle commun ou SI propre, et conditions d'un alignement préservé*

**Un socle commun est pertinent pour les activités de soutien** (0,5 pt) : comptabilité, facturation et trésorerie, paie, messagerie et outils collaboratifs, et, sous réserve, achats. Ces activités ne différencient pas la filiale aux yeux des clients ; leurs besoins sont proches d'une filiale à l'autre et standardisables ; leur mise en commun apporte des économies d'échelle, un pilotage homogène du groupe (cinq filiales tiennent encore leur propre paie et leur propre comptabilité, M. DORMAELS ; clôture ramenée de dix à cinq jours dans les filiales qui ont adhéré, annexe 3.1 B), évite la montée de version de 2028 (annexe 3.2 C) et répond au plan, qui ne vise que les fonctions support. Les achats appellent une réserve : la commande d'une pièce d'une installation frigorifique en panne un samedi « dans l'heure » (M. DRAVIGNOL) touche la continuité des activités principales.

**Le SI propre de la filiale porte un avantage concurrentiel dans les activités principales** (0,5 pt) : la réservation des quais (créneau confirmé en moins de 15 minutes contre deux heures chez les autres prestataires), la traçabilité des températures transmise en temps réel (condition de deux appels d'offres d'enseignes en 2026) et le portail des clients (utilisé chaque semaine par neuf clients sur dix, premier motif de satisfaction, avant le prix) ; selon le directeur des opérations, ces services ont fait gagner trois appels d'offres face à des concurrents moins chers. Ils reposent sur des applications adaptées ou développées par l'équipe de la filiale et sur sa capacité à les faire évoluer vite : les soumettre à un cycle annuel d'évolutions décidé à Rotterdam affaiblirait la différenciation que la directrice générale veut préserver (« je ne veux pas que nos clients paient la standardisation »).

**Deux conditions pour que l'adhésion reste alignée** (0,5 pt, deux conditions précises et reliées au cas) :
1. **Préserver les échanges entre le socle et les activités principales** : la facturation dépend des tournées et des prestations transmises par les logiciels de gestion du transport et des entrepôts ; la refonte de ces échanges (200 k€, annexe 3.2 D) doit être prévue, testée avant la bascule et maintenue par un standard d'échange dont le groupe garantit la stabilité.
2. **Garder la maîtrise et la capacité d'évolution des applications métiers** : les applications qui portent l'avantage restent hors du socle, et l'équipe métier est renforcée par les deux personnes libérées (annexe 3.2 D) ; une procédure rapide permet de traiter hors cycle annuel les besoins métiers urgents qui touchent le socle (achat d'urgence d'une pièce, évolution de la facturation exigée par un client).

D'autres conditions sont admises : un niveau de service du socle adapté au rythme de l'activité (paie, facturation de fin de mois) ; la représentation de la filiale dans les décisions sur le socle.

**Réponses tolérées**
- Référence complémentaire au modèle d'alignement stratégique de Henderson et Venkatraman (1993), valorisée si elle éclaire l'analyse (stratégie de la filiale fondée sur la technologie, perspective de potentiel concurrentiel), sans être attendue.
- Chaîne de valeur présentée sous forme de schéma, ou découpage des activités principales en trois maillons (entrepôts, transport, relation client) au lieu de quatre.
- Facturation classée parmi les activités principales (service rendu au client) si le lien avec les tournées et les prestations est expliqué.
- Achats rangés dans le socle sans réserve, si la condition d'une procédure d'achat urgente apparaît dans b-3, ou rangés hors du socle avec une justification tirée du témoignage de M. DRAVIGNOL.

**Erreurs fréquentes**
- *Alignement réduit à l'adoption d'un logiciel commun* (`JUR-G02` ; `ET-06`) — « adhérer au socle, c'est s'aligner sur le groupe » ; juste : l'alignement porte sur la stratégie de la filiale autant que sur celle du groupe et peut justifier de garder des applications propres.
- *Chaîne de valeur récitée* (`JUR-T01` ; `ET-39`) — liste générique des activités de Porter sans les applications ni les chiffres de l'annexe 3.2.
- *Tout le SI dans le socle, ou rien* — refuser l'adhésion contredit le plan du groupe ; tout y mettre ignore l'avantage reconnu par les clients.
- *Avantage concurrentiel affirmé sans preuve* (`JUR-T08`) — juste : délai de 15 minutes contre deux heures, deux appels d'offres d'enseignes, neuf clients sur dix, trois appels d'offres gagnés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Alignement stratégique : définition | mise en cohérence permanente | F01 § 1 | notion de cours |
| Chaîne de valeur (Porter, 1985) | activités principales et de soutien ; apport du SI | `porter_chaine_valeur_1985` / F01 § 2 | modèle théorique |
| Strategic Alignment Model (Henderson et Venkatraman, 1993) | réponse tolérée | `henderson_venkatraman_1993` / F01 § 1 | modèle théorique |

---

### 3.2 – Choix d'un scénario et feuille de route (2,5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.c` « Méthodologies de planification stratégique du SI ».

**Annexes mobilisées** : annexes 3.1 (scénarios, calendrier, règles de gouvernance), 3.2 (coûts, équipe, avantage reconnu), 3.3 (positions des acteurs) et 1.1 (plan « ORMESTAL 2030 »).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Comparaison des deux scénarios selon les quatre critères, appuyée sur les annexes ; 0,5 pour deux ou trois critères | 1 |
| a-2 | Recommandation argumentée, qui répond aussi à la demande du groupe (client présent dans plusieurs pays) | 0,5 |
| b-1 | Feuille de route en trois étapes jusqu'à fin 2028 : contenu, échéance, responsable de chaque étape | 0,5 |
| b-2 | Indicateur de suivi complet (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.2 a) – Comparaison et recommandation*

| Critère | Scénario 1 – Adhésion complète | Scénario 2 – Adhésion limitée aux fonctions support |
|---|---|---|
| **Alignement sur la stratégie de la filiale** | défavorable : les applications qui fondent l'avantage reconnu par les clients (quais confirmés en 15 minutes, alertes de température, portail) sont retirées d'ici fin 2029 au profit des applications du groupe ; la différenciation qui a fait gagner trois appels d'offres est menacée | favorable : la filiale standardise ce qui ne la différencie pas et garde ce qui la différencie |
| **Respect du plan « ORMESTAL 2030 »** | au-delà du plan, qui ne vise que les fonctions support ; répond au souhait de M. DORMAELS et du client présent dans quatre pays | conforme au plan : fonctions support sur le socle d'ici fin 2028, calendrier tenable (projet d'environ douze mois) |
| **Coûts** | partie logistique non chiffrée et trois ans de projet, qui s'ajoutent au coût du socle ; économies d'échelle possibles mais inconnues | coût complet connu : proche du maintien sur trois ans (2 800 contre 2 700 k€), puis 150 k€ par an réaffectés aux applications métiers (deux personnes redéployées, question 3.5) |
| **Agilité des métiers** | toute évolution des quais, de la traçabilité ou du portail attend le comité d'architecture annuel, où la filiale ne siège pas : perte de réactivité (M. DRAVIGNOL) | agilité conservée sur les métiers ; la contrainte annuelle ne touche que les fonctions support, à aménager pour les achats urgents |

(1 pt.)

**Recommandation : le scénario 2** (0,5 pt). Il respecte le plan du groupe, préserve l'avantage concurrentiel de la filiale et repose sur un coût connu. Il répond à la demande du groupe d'une autre manière : les données de suivi des livraisons et de température de la filiale peuvent alimenter la plateforme de données du groupe, pour offrir au client présent dans plusieurs pays une vue commune sans retirer le portail de la filiale. La convergence des applications métiers pourra être réexaminée après 2028, quand les applications logistiques du groupe auront été chiffrées et comparées au service rendu aujourd'hui. L'adhésion est assortie de conditions négociées avant la signature (questions 3.3 à 3.5).

*3.2 b) – Feuille de route jusqu'à fin 2028 et indicateur de suivi*

| Étape | Contenu | Échéance | Responsable |
|---|---|---|---|
| 1. Cadrage et conditions d'adhésion | décision de la directrice générale présentée à M. DORMAELS ; convention d'adhésion avec la DSI du groupe (niveau de service, réversibilité, clé de refacturation, représentation de la filiale, procédure d'évolution urgente) ; inventaire des échanges entre les applications métiers et le PGI ; demandes d'évolution déposées avant le 30 septembre (circuit d'achat urgent) ; désignation des deux correspondants | avril à septembre 2027 | Mme DUCHASTEL (décision) ; M. BRÉVANNE (pilotage) ; Mme MERCOIRAN (conditions financières) |
| 2. Bascule de la messagerie, de la finance et des achats | messagerie et outils collaboratifs au quatrième trimestre 2027 ; refonte et essais des échanges avec la facturation ; formation ; bascule de la comptabilité, de la facturation, de la trésorerie et des achats au 1er janvier 2028 ; double fonctionnement jusqu'à l'arrêté des comptes de 2027 | octobre 2027 à juin 2028 | M. BRÉVANNE ; Mme MERCOIRAN, propriétaire des processus de gestion |
| 3. Bascule de la paie et bilan | paie au 1er juillet 2028 (début de trimestre, dans les six mois de double fonctionnement chiffrés à l'annexe 3.2 D) ; envoi des données de gestion à la plateforme de données du groupe ; retrait de l'ancien logiciel de gestion comptable et commerciale et du logiciel de paie ; bilan de l'adhésion (coût complet réel, niveau de service obtenu) présenté au comité de direction et à M. DORMAELS | juillet à décembre 2028 | M. BRÉVANNE ; Mme MERCOIRAN ; Mme DUCHASTEL (bilan) |

(0,5 pt.)

Indicateur de suivi de la feuille de route (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Taux de bascule des fonctions support dans les délais** | nombre de fonctions support basculées sur le socle à la date prévue, sans retour à l'ancienne application / 4 fonctions prévues (messagerie, finance et facturation, achats, paie) | comité de pilotage de l'adhésion (jalons validés conjointement par la filiale et la DSI du groupe) | mensuelle | 75 % au 31 mars 2028, 100 % au 31 décembre 2028 | processus |

**Réponses tolérées**
- Recommandation du scénario 1 si elle est argumentée et assortie de conditions fortes (maintien des services différenciants jusqu'à ce que les applications du groupe offrent le même délai de confirmation des quais et les mêmes alertes, représentation de la filiale dans le choix des évolutions) : la démarche est valorisée et l'item a-2 est accordé si les conditions sont précises.
- Critères formulés autrement (valeur pour les clients, faisabilité du calendrier), s'ils couvrent les quatre critères demandés.
- Calendrier différent (finance au 1er janvier 2029 avec dérogation au plan, paie au 1er janvier 2028), s'il respecte les règles de bascule de l'annexe 3.1 B et s'il est justifié ; une bascule de la finance au 1er janvier 2029 oblige à imputer la montée de version au scénario d'adhésion (annexe 3.2 C).
- Autre indicateur complet : coût complet annuel des fonctions support (refacturation et correspondants), cible 650 k€ au plus en 2029 et 2030, axe financier ; délai de clôture mensuelle, cible cinq jours ouvrés, axe processus ; taux de satisfaction des utilisateurs du socle, axe client.

**Erreurs fréquentes**
- *Feuille de route confondue avec un schéma directeur complet* (par analogie avec `ET-07`, schéma directeur confondu avec un plan de projet) — diagnostic, vision cible et portefeuille de tout le SI ; juste : la feuille de route d'un scénario, en trois étapes datées.
- *Recommandation sans tenir compte du plan du groupe* — refuser toute adhésion ; le plan s'impose à la filiale pour les fonctions support : la marge de décision porte sur le périmètre et les conditions.
- *Indicateur incomplet ou sans lien avec la feuille de route* (`JUR-A02` ; `ET-18`) — « respect du planning » sans formule ni cible.
- *Bascule de la finance ou des achats en cours d'exercice* — contraire aux règles de l'annexe 3.1 B.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Planification stratégique du SI : schéma directeur et feuille de route | étapes, échéances, responsables | F01 § 3 | notion de cours |
| Portefeuille applicatif (conserver, faire évoluer, remplacer, retirer) | scénarios | F01 § 3.2 | notion de cours |
| Fiche d'indicateur à cinq champs | indicateur de suivi | F09 § 4 | notion de cours |

---

### 3.3 – Organisation de la fonction SI entre le groupe et la filiale (2 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.b` « Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers » (règles de gouvernance, représentation et arbitrage de la question b).

**Annexes mobilisées** : annexes 3.2 A (équipe et rattachement), 3.1 D (règles de gouvernance du socle), 3.3 (positions de Mme DUCHASTEL, de M. KAMPERVELD et de M. BRÉVANNE) et 1.1 (organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Modèle actuel caractérisé (décentralisé), avec les faits de l'annexe 3.2 A et ses effets | 0,5 |
| a-2 | Modèles fédéral et centralisé présentés, avec un avantage et une limite de chacun pour ORMESTAL France | 0,5 |
| b-1 | Positionnement recommandé du responsable des SI : double rattachement explicite, rôle de chaque lien | 0,5 |
| b-2 | Deux règles de gouvernance précises entre la filiale et le groupe | 0,5 |

**Réponse attendue**

*3.3 a) – Modèle actuel, modèles fédéral et centralisé*

**Modèle actuel : décentralisé** (0,5 pt). La filiale dispose de sa propre équipe SI de 20 personnes, choisit seule ses logiciels, ses prestataires et son hébergement et ne soumet pas ses projets au groupe ; la DSI du groupe se limite à animer une réunion mensuelle et à transmettre des règles de sécurité ; le responsable des SI rend compte à la directrice générale, sans lien écrit avec le DSI du groupe (annexe 3.2 A). Effets : réactivité et proximité des métiers, qui ont produit le portail et la réservation des quais ; mais hétérogénéité des SI du groupe (cinq filiales ont encore leur propre paie et leur propre comptabilité, M. DORMAELS), absence de règles sur qui décide de quoi (M. BRÉVANNE, Mme DUCHASTEL).

**Deux modèles cibles** (0,5 pt) :

| Modèle | Principe | Avantage pour ORMESTAL France | Limite pour ORMESTAL France |
|---|---|---|---|
| **Centralisé** | une DSI unique, celle du groupe, décide et opère pour toutes les filiales ; les filiales ne gardent que des correspondants | cohérence et économies d'échelle ; pilotage homogène du groupe ; sécurité homogène | éloignement des métiers de la logistique du froid française ; évolutions décidées une fois par an à Rotterdam ; perte de la réactivité qui fonde l'avantage reconnu par les clients ; dépendance complète au groupe |
| **Fédéral** | la DSI du groupe porte la gouvernance, l'architecture, le socle commun et les règles de sécurité ; chaque filiale garde une équipe SI pour ses métiers, dans le respect de ces règles | équilibre entre un socle commun pour les fonctions support et l'agilité des applications métiers ; cohérent avec le scénario 2 | coordination plus exigeante ; rôles et arbitrages à écrire ; risque de doublons si la frontière entre socle et métiers n'est pas tenue |

*3.3 b) – Positionnement du responsable des SI et règles de gouvernance*

**Positionnement recommandé : un double rattachement explicite, dans un modèle fédéral** (0,5 pt). M. BRÉVANNE reste rattaché **hiérarchiquement à la directrice générale** et membre du comité de direction : il porte l'alignement du SI sur la stratégie de la filiale et le budget des applications métiers. Il est rattaché **fonctionnellement au DSI du groupe** : il applique les règles d'architecture et de sécurité, est le correspondant du socle dans la filiale (avec les deux correspondants) et représente la filiale dans les instances du socle. Ce double lien est écrit dans une fiche de fonction validée par Mme DUCHASTEL et M. KAMPERVELD, qui précise ce qui relève de chacun, et met fin à la situation décrite par M. BRÉVANNE (« sans règle écrite »).

**Deux règles de gouvernance** (0,5 pt, deux règles précises et applicables) :
1. **Répartition écrite des décisions** : le socle relève du groupe, qui décide après avis des filiales ; les applications métiers relèvent de la filiale, qui décide dans le respect des règles d'architecture, de sécurité et des échanges standard définis par le groupe ; chaque filiale reste propriétaire de ses données. Cette répartition prend la forme d'une matrice des responsabilités (décide, est consulté, est informé) annexée à la convention d'adhésion.
2. **Représentation et arbitrage** : la filiale siège au comité d'architecture du groupe, ou à un comité des filiales adhérentes qui le précède, pour les évolutions du socle ; une procédure d'évolution urgente hors cycle annuel est prévue (obligation réglementaire, besoin métier critique comme un achat urgent), avec un délai de réponse fixé ; un désaccord persistant est arbitré par Mme DUCHASTEL et M. DORMAELS.

Règles également admises : convention de service interne entre la DSI du groupe et la filiale (disponibilité, délais d'information et de rétablissement) ; refacturation transparente, arrêtée chaque année avec les filiales (question 3.5) ; revue annuelle du socle par les filiales.

**Réponses tolérées**
- Modèle actuel qualifié de « décentralisé de fait » ou d'« autonomie de la filiale », si les faits de l'annexe 3.2 A sont cités.
- Recommandation d'un modèle bimodal (mode stable pour le socle, mode exploratoire pour les services aux clients), si les règles de coordination entre le groupe et la filiale sont précisées.
- Rattachement hiérarchique au DSI du groupe et fonctionnel à la directrice générale, si le candidat montre comment l'alignement sur la stratégie de la filiale reste garanti (participation au comité de direction, budget des applications métiers arrêté par la directrice générale).

**Erreurs fréquentes**
- *Modèle fédéral confondu avec le modèle décentralisé* (F01 § 8) — juste : le modèle fédéral suppose une gouvernance et un socle communs, absents aujourd'hui.
- *Recommandation irréaliste* (`JUR-G05` déséquilibres organisationnels et recommandations réalistes) — supprimer l'équipe SI de la filiale, ou ignorer le plan du groupe.
- *Gouvernance réduite à un outil ou au seul socle technique* (`JUR-G06` vocabulaire précis de la gouvernance) — juste : rôles, instances, règles de décision et d'arbitrage.
- *Modèles présentés sans application au cas* (`JUR-T01`) — définitions sans avantage ni limite pour ORMESTAL France.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèles d'organisation de la DSI (centralisé, décentralisé, fédéral, bimodal, externalisé) ; rôle et rattachement du DSI | modèle actuel, modèles cibles, positionnement | F01 § 4 | notion de cours |
| Comitologie SI (comité d'architecture, comité d'arbitrage) | règles de gouvernance | F02 § 6 | notion de cours |

---

### 3.4 – Risques de l'adhésion au socle (3,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ». Limite : « Une veille réglementaire est indispensable pour maintenir la conformité des pratiques. »

**Annexes mobilisées** : annexes 3.1 (hébergement, règles de gouvernance et de service, sortie, repères au 31/12/2026), 3.3 (positions des acteurs, incident de décembre 2026, échelle de cotation) et 3.2 (équipe, correspondants).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie des risques SI présentée (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers) | 0,5 |
| a-2 | Quatre risques identifiés, formulés comme des événements et rattachés chacun à une catégorie ; 0 en deçà de trois risques | 0,5 |
| b-1 | Cotation de chaque risque avec l'échelle de l'annexe 3.3 C, justifiée par les annexes | 0,5 |
| b-2 | Cartographie probabilité × impact et ordre de priorité | 0,5 |
| c | Option et mesure de traitement précises pour chaque risque ; 1 pour trois risques, 0,5 pour deux | 1,5 |

**Réponse attendue**

*3.4 a) – Typologie et identification*

Un **risque lié au SI** est un événement possible qui, s'il survient, porte atteinte à la disponibilité, à l'intégrité, à la confidentialité ou à la traçabilité de l'information, à la continuité des activités, à la conformité ou à la stratégie de l'organisation ; il s'apprécie par sa probabilité et son impact (F12 § 0). La typologie du programme distingue les **cybermenaces** (rançongiciel, hameçonnage, attaque par un fournisseur), les **défaillances opérationnelles** (panne, erreur, indisponibilité d'un service ou d'un prestataire), les **risques réglementaires** (non-conformité au RGPD, aux obligations sectorielles) et les **risques métiers** ou stratégiques (dépendance, perte d'avantage concurrentiel, inadaptation du SI aux besoins) (0,5 pt).

Quatre risques de l'adhésion (0,5 pt) :

| N° | Risque, formulé comme un événement | Catégorie | Faits des annexes |
|---|---|---|---|
| R1 | **Dépendance à la DSI du groupe et au fournisseur unique** : le groupe ou son fournisseur de cloud impose un tarif, un changement ou une migration que la filiale ne peut ni refuser ni quitter, faute de procédure de sortie et de compétences internes | risque métier (stratégique) : dépendance à un fournisseur | aucune procédure de sortie, tarif fixé chaque année sans détail des coûts, fournisseur unique (annexe 3.1 D) ; deux correspondants seulement ; « personne chez nous ne saura plus faire fonctionner ces applications » (M. BRÉVANNE) |
| R2 | **Souveraineté et localisation des données** : des données de paie et des contrats de clients sont rendus accessibles à une autorité d'un pays tiers, ou leur hébergement n'est pas conforme aux exigences du RGPD | risque réglementaire (conformité, confidentialité) | fournisseur dont le siège est hors de l'Union européenne, données stockées dans l'Union (annexe 3.1 A) ; transferts hors de l'Union soumis à des conditions particulières (annexe 3.1 E) ; « je voudrais savoir ce que le groupe a prévu » (Mme MERCOIRAN) |
| R3 | **Perte d'agilité des métiers** : un besoin urgent touchant le socle (achat d'une pièce un samedi, nouvelle règle de facturation exigée par un client) ne peut être satisfait à temps | risque métier | évolutions décidées une fois par an, demandes avant le 30 septembre, comité sans les filiales, assistance en anglais et en néerlandais de 8 à 18 heures en semaine (annexe 3.1 D) ; M. DRAVIGNOL |
| R4 | **Indisponibilité de la plateforme du groupe** : le socle est indisponible plusieurs jours ; la paie, la facturation et les achats sont bloqués | défaillance opérationnelle (la cause peut être une cybermenace, inconnue ici) | incident des 14 et 15 décembre 2026 dans la filiale belge, information au bout de six heures, cause non communiquée, aucune procédure de secours (annexe 3.3 B) ; disponibilité visée de 99,5 % sans engagement écrit ni compensation ; un seul fournisseur (annexe 3.1) |

*3.4 b) – Évaluation et cartographie*

| Risque | Probabilité | Impact | Criticité | Justification |
|---|---|---|---|---|
| R1 Dépendance | 3 (probable) | 3 (grave) | **9 – élevée** | tarif révisé chaque année et aucune sortie prévue : la situation de dépendance est acquise dès l'adhésion ; perte de maîtrise des données de paie et de facturation |
| R2 Souveraineté | 2 (possible) | 3 (grave) | **6 – moyenne** | données stockées dans l'Union, mais aucune garantie connue sur l'accès depuis un pays tiers ; un manquement porterait sur des données personnelles et sur la confiance des clients |
| R3 Agilité | 3 (probable) | 2 (significatif) | **6 – moyenne** | le cycle annuel est certain, mais le scénario 2 limite le risque aux fonctions support : retards internes, sauf pour les achats urgents |
| R4 Indisponibilité | 3 (probable) | 3 (grave) | **9 – élevée** | l'incident s'est déjà produit en 2026 sur l'une des trois filiales adhérentes ; paie, facturation et achats perturbés deux jours |

(0,5 pt.)

Cartographie (0,5 pt) :

| Impact \ Probabilité | 1 improbable | 2 possible | 3 probable | 4 quasi certain |
|---|---|---|---|---|
| 4 critique | | | | |
| 3 grave | | R2 (6) | **R1 (9), R4 (9)** | |
| 2 significatif | | | R3 (6) | |
| 1 mineur | | | | |

Ordre de priorité : R4 et R1, de criticité élevée, sont traités avant la bascule, R4 d'abord parce qu'il menace la facturation et les achats dès le 1er janvier 2028, la paie à partir de sa bascule, R1 dans la convention d'adhésion avant la signature ; R2 et R3, de criticité moyenne, sont traités dans le plan d'adhésion de l'étape 1.

*3.4 c) – Traitement des quatre risques*

| Risque | Option | Mesure |
|---|---|---|
| R1 Dépendance | réduire | **réversibilité** inscrite dans la convention d'adhésion : export complet et régulier des données de la filiale (paie, comptabilité, facturation, achats) dans un format ouvert et documenté, essai annuel de restitution, délai, assistance et coût de sortie, préavis et plafond des hausses de tarif ; maintien de deux correspondants formés et d'une documentation ; demande au groupe de faire jouer auprès de son fournisseur les droits de changement de fournisseur prévus par le Data Act (annexe 3.1 E) |
| R2 Souveraineté | réduire | garanties écrites demandées au groupe : contrat de sous-traitance avec le fournisseur couvrant les données de la filiale, localisation dans l'Union inscrite au contrat, chiffrement des données avec des clés maîtrisées par le groupe, information de la filiale en cas de demande d'accès d'une autorité ; inscription des traitements au registre ; critère d'un cloud de confiance (référentiel du Cigref, qualification SecNumCloud de l'ANSSI) pour le prochain choix d'hébergeur du groupe |
| R3 Agilité | réduire (et éviter pour les métiers) | **comité d'arbitrage** groupe-filiales et procédure d'évolution urgente hors cycle annuel, avec un délai de réponse fixé ; circuit d'achat d'urgence prévu dans le paramétrage commun (seuil, validation a posteriori) ; le maintien des applications métiers hors du socle (scénario 2) évite le risque là où il serait critique |
| R4 Indisponibilité | réduire | **clauses de niveau de service internes** dans une convention de service avec la DSI du groupe : disponibilité de 99,5 % mesurée et communiquée chaque mois, information de la filiale en moins d'une heure, délai de rétablissement, priorité pendant les périodes de paie et de clôture, minoration de la refacturation en cas de manquement ; **mode dégradé** documenté et exercé une fois par an : virement de la paie sur la base du mois précédent avec régularisation, factures émises dès le rétablissement, bons d'achat d'urgence hors PGI régularisés ensuite |

(1,5 pt pour les quatre risques traités avec une option et une mesure précise ; 1 pour trois, 0,5 pour deux.) Après traitement, la criticité résiduelle est revue en comité de direction ; un risque résiduel faible peut être accepté.

**Réponses tolérées**
- Cotations différentes d'un niveau, si elles sont justifiées par les annexes (R3 à impact 3 en raison des achats urgents ; R2 à probabilité 1 parce que les données sont stockées dans l'Union ; R1 à probabilité 4).
- Autres risques pertinents, à la place de l'un des quatre : échec de la bascule au 1er janvier 2028 (risque de projet), perte des compétences internes, cybermenace visant une plateforme partagée par huit filiales.
- Option « transférer » pour une part de R4 (minoration de la refacturation, assurance du groupe) ou « éviter » pour R2 (données de paie conservées hors du socle), si elle est expliquée.
- Référence à ISO 31000:2018 ou à ISO/IEC 27005:2022 pour les options de traitement, valorisée sans être attendue.

**Erreurs fréquentes**
- *Hébergement « souverain » assimilé à un hébergement dans l'Union européenne* (`ET-37`) — juste : la localisation ne règle pas le droit applicable à un fournisseur dont le siège est hors de l'Union.
- *Plan de continuité ou de reprise développé* (`JUR-S02`) — non demandé ; juste : un mode dégradé et des engagements de service.
- *Risques non formulés comme des événements, ou confondus avec leurs mesures* (`JUR-T03`) — « absence de réversibilité » est une cause ; le risque est l'impossibilité de sortir ou de récupérer ses données.
- *Cotations sans justification ni cartographie* (`JUR-T08`) — juste : chaque note s'appuie sur un fait (incident de décembre, absence de sortie, cycle annuel).
- *Analyse juridique du transfert ou de l'assujettissement à un texte de cybersécurité* — non attendue ; une mention suffit (annexe 3.1 E).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI ; cartographie probabilité × impact | identification, cotation | F12 § 0 ; F10 § 1.2 (cartographie probabilité × impact) | notion de cours |
| ISO 31000:2018 ; ISO/IEC 27005:2022 | options de traitement (réponse tolérée) | `iso_31000_2018`, `iso_27005_2022` / F12 § 2 | en vigueur |
| Réversibilité, portabilité, souveraineté | R1, R2 | F03 § 5.3 ; F04 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | sous-traitant, transferts hors de l'Union (annexe 3.1 E) | `rgpd` / F15 | applicable depuis le 25/05/2018 |
| Règlement (UE) 2023/2854 (Data Act) | changement de fournisseur de cloud | `data_act` / F03 § 5.3 | applicable depuis le 12/09/2025 |
| Proposition « omnibus numérique » (19/11/2025) | non applicable (annexe 3.1 E) | `omnibus_numerique_donnees` | projet |
| Référentiel du cloud de confiance du Cigref ; SecNumCloud 3.2 (ANSSI) | critères d'un cloud de confiance | `cigref_cloud_confiance`, `secnumcloud_3_2` / F03 § 5.3 | publiés |
| Niveaux de service (ITIL) | clauses de niveau de service internes | `itil` / F02 § 5 | en vigueur |

---

### 3.5 – Coût complet de l'adhésion et refacturation (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI » ; `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ». Limite : « Le pilotage stratégique par les indicateurs suppose une capacité de recul critique. »

**Annexes mobilisées** : annexes 3.2 C et D (coûts actuels, coûts annoncés et coûts relevés), 3.1 D (refacturation) et 3.3 (position de Mme MERCOIRAN).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Rôle du contrôle de gestion appliqué au SI dans la décision | 0,5 |
| a-2 | Coûts sur trois ans selon les chiffres du groupe : maintien 2 700 k€, adhésion 1 800 k€, économie annoncée de 900 k€ | 0,5 |
| a-3 | Coûts cachés intégrés (1 000 k€, adhésion à 2 800 k€) et conclusion nuancée (régime de croisière sans économie de trésorerie, autres justifications de la décision) | 0,5 |
| b | Deux critiques précises de la refacturation par compte et une clé plus adaptée | 0,5 |

**Réponse attendue**

*3.5 a) – Rôle du contrôle de gestion et coût complet*

Le **contrôle de gestion appliqué au SI** mesure le coût complet des services numériques (coûts directs, indirects et cachés), les impute aux activités qui les consomment par des inducteurs (refacturation interne), rapproche ces coûts de la valeur produite (qualité de service, gains, risques évités) et éclaire les décisions par des comparaisons de scénarios sur un horizon commun, avant d'en suivre la réalisation (F09 § 2). Ici, il doit vérifier l'économie annoncée par le groupe, faire apparaître ce que le chiffrage omet et apprécier la clé de refacturation (0,5 pt).

Coût sur trois ans, de 2028 à 2030, en k€ (0,5 pt) :
- **Maintien de la situation actuelle** : 3 × 800 + 300 (montée de version) = **2 700 k€** ;
- **Adhésion selon les chiffres du groupe** : 3 × 500 (refacturation) + 300 (migration) = **1 800 k€**, soit l'économie annoncée de **900 k€**.

Avec les coûts cachés relevés à l'annexe 3.2 D (0,5 pt) : double fonctionnement 250 + correspondants 3 × 150 = 450 + formation 100 + refonte des échanges 200 = **1 000 k€**, soit un coût complet de l'adhésion de 1 800 + 1 000 = **2 800 k€**, supérieur de **100 k€** à celui du maintien. La baisse de productivité des premiers mois, non chiffrée, accroît encore cet écart.

**Conclusion** : sur trois ans, l'adhésion n'apporte pas d'économie ; l'économie annoncée par le groupe vient de l'oubli des coûts cachés. En régime de croisière, après la bascule, le coût des fonctions support passe de 800 à 500 + 150 = 650 k€ par an. Ces 150 k€ ne sont pas une économie de trésorerie : ils correspondent aux deux personnes redéployées vers le portail et la réservation des quais, que la filiale continue de payer. L'adhésion libère donc une capacité de 150 k€ par an au profit des activités qui la différencient, à dépense constante. La décision ne se justifie donc pas par les coûts sur trois ans, mais par le plan du groupe, le pilotage homogène des filiales, la montée de version évitée et le redéploiement de deux personnes vers les applications qui différencient la filiale ; elle est conditionnée à la révision de la clé de refacturation (b), dont dépend l'essentiel de l'écart.

*3.5 b) – Critique de la refacturation par compte*

Deux critiques attendues parmi les trois suivantes (0,5 pt avec la clé proposée) :
1. **Un inducteur qui ne reflète pas la consommation** : un tarif unique de 1 000 € s'applique à un comptable qui utilise le PGI toute la journée comme à un chef d'équipe qui ne lit que ses courriels. Les 350 comptes de la seule messagerie (70 % des comptes) coûteraient 350 k€ par an, alors que la messagerie revient aujourd'hui à environ 100 € par compte, soit 35 k€ : la filiale, qui compte beaucoup d'utilisateurs de terrain, finance une part du PGI des autres.
2. **Une incitation contraire aux objectifs** : pour réduire la facture, la filiale pourrait limiter le nombre de comptes (comptes partagés, qui nuisent à la sécurité et à la traçabilité) ou garder la messagerie hors du socle, au détriment de la mise en commun recherchée.
3. **Un tarif opaque et sans lien avec le service rendu** : il est fixé chaque année par le groupe, sans détail de ses coûts ni lien avec le niveau de service (aucune minoration après l'incident de décembre 2026) ; la filiale ne peut ni contrôler ce qu'elle paie ni inciter la DSI du groupe à l'efficience.

**Clé plus adaptée** : une refacturation par service, sur la base d'un catalogue de services du socle : le PGI selon des unités d'œuvre représentatives (utilisateurs actifs du PGI, ou nombre de bulletins de paie, de factures et de commandes d'achat), la messagerie et les outils collaboratifs par compte à leur coût propre, la plateforme de données par un forfait par filiale ; des prix standard fixés pour l'exercice et connus à l'avance, une base de coûts communiquée aux filiales, et une minoration en cas de niveau de service non tenu.

**Réponses tolérées**
- Calcul présenté par année ou par poste, s'il aboutit aux mêmes totaux ; comparaison faite en coût annuel moyen sur la période, si le raisonnement est juste.
- Deux personnes redéployées maintenues dans le coût de l'adhésion (2 800 + 3 × 150 = 3 250 k€, soit 550 k€ de plus que le maintien), si le candidat raisonne au niveau de la dépense totale de la filiale et l'écrit.
- Correspondants comptés pour la seule durée de 2029 et 2030 ou montée de version exclue du maintien, si l'hypothèse est écrite et la conclusion reste nuancée.
- Clé fondée sur la seule distinction entre comptes du PGI et comptes de messagerie, avec deux tarifs, si elle est justifiée par l'annexe 3.2 D.
- Mention qualitative du retour sur investissement (gains non financiers : clôture plus rapide, pilotage du groupe), sans calcul.

**Erreurs fréquentes**
- *Coût complet réduit à la refacturation* (`ET-33` ; `JUR-A03` indicateurs de coûts dans une logique ouverte) — oubli du double fonctionnement, des correspondants, de la formation et des échanges.
- *Montée de version imputée au scénario d'adhésion*, alors qu'elle est évitée par la bascule de la finance au 1er janvier 2028, date retenue par le groupe (annexe 3.2 C).
- *Les 150 k€ par an du régime de croisière présentés comme une économie de trésorerie de la filiale* — ils correspondent aux deux personnes redéployées, dont le coût quitte le périmètre des fonctions support mais reste supporté par la filiale, au service des activités principales.
- *Calcul d'actualisation ou analyse fiscale des flux entre le groupe et la filiale* — hors du programme de l'UE 5 et non demandés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Contrôle de gestion appliqué au SI : coût complet, inducteurs, refacturation interne | rôle, critique de la clé | F09 § 2 | notion de cours |
| Coût total de possession, coûts cachés, CAPEX et OPEX | comparaison sur trois ans | F09 § 3 | notion de cours |
