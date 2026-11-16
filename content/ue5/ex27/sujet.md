# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 27

**DOSSIER 3 – ASSURER LA CONTINUITÉ DU SYSTÈME D'INFORMATION PENDANT LES VENDANGES, FIABILISER LES APPORTS ET CHOISIR UN HÉBERGEMENT RESPONSABLE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 9, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. Les Vignerons de ROCALDÈNE sont une union de coopératives agricoles dont le siège est à Pézenas, dans l'Hérault. Fondée en 1987, l'union regroupe neuf caves coopératives de l'Hérault et de l'Aude, auxquelles environ 1 400 viticulteurs apportent la vendange de quelque 6 500 hectares de vignes. Chaque cave reçoit et vinifie la vendange de ses adhérents ; l'union assemble et élève les vins, les conditionne sur son site de Pézenas et les commercialise en vrac auprès de négociants, en bouteilles auprès de la grande distribution et à l'export. L'union est administrée par un conseil composé des présidents des neuf caves, que préside M. Gilles ESCOURBIAC, viticulteur ; sa directrice générale, Mme Hélène MAZERANDE, dirige les services de l'union. L'union et ses caves emploient 260 salariés permanents, rejoints par environ 180 saisonniers pendant les vendanges. Le chiffre d'affaires de l'union s'est élevé à 145 millions d'euros en 2026 ; 2,2 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « ROCALDÈNE 2030 », adopté par le conseil de l'union en décembre 2026, fixe trois priorités : adapter le vignoble et l'offre au changement climatique et conquérir de nouveaux marchés, notamment à l'export et dans la vente en ligne ; mieux connaître la qualité des apports, de la parcelle à la bouteille, pour mieux la valoriser ; garantir la continuité du système d'information pendant les campagnes et en réduire l'empreinte environnementale. Mme MAZERANDE en rend compte au conseil à chaque réunion.

Vous êtes responsable administratif et financier adjoint de l'union depuis 2025, rattaché à la directrice générale et chargé du projet de refonte du système d'information. Mme MAZERANDE vous demande trois travaux : éclairer la stratégie du système d'information et préparer sa refonte (dossier 1) ; organiser et exploiter les données des parcelles et des apports, et apprécier un projet d'authentification des bouteilles (dossier 2) ; assurer la continuité du système d'information pendant les vendanges, fiabiliser les apports et choisir un hébergement responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation des Vignerons de ROCALDÈNE et chiffres clés

Les Vignerons de ROCALDÈNE sont une union de coopératives agricoles fondée en 1987, dont le siège et le site de conditionnement sont à Pézenas (Hérault). Neuf caves coopératives de l'Hérault et de l'Aude en sont membres. Les viticulteurs sont adhérents de leur cave : chaque cave reçoit la vendange de ses adhérents pendant les vendanges, de fin août à mi-octobre, la vinifie et conserve les vins dans ses cuves. L'union assemble et élève les vins des neuf caves, les conditionne et les commercialise. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires de l'union | 145 M€ : vrac auprès de négociants 35 % (environ 51 M€), bouteilles vendues à la grande distribution en France 40 % (58 M€), export 25 % (environ 36 M€ ; Europe du Nord, Amérique du Nord, Asie) ; vente en ligne aux particuliers à l'étude |
| Vendange 2026 | environ 380 000 hectolitres, soit 380 milliers d'hectolitres |
| Vignoble | environ 6 500 hectares, exploités par environ 1 400 viticulteurs adhérents des caves |
| Effectif permanent | 260 salariés : environ 150 à l'union (conditionnement et logistique 75, commercial et service clients 25, production, qualité et laboratoire 20, services administratifs et financiers et direction 24, équipe informatique 6) et 110 dans les caves ; environ 180 saisonniers dans les caves pendant les vendanges ; aucune cave n'a d'informaticien |
| Système d'information | à l'union : un progiciel de gestion (gestion commerciale, stocks, comptabilité), dont le support par l'éditeur s'arrête fin 2028 ; le laboratoire d'analyses de l'union ; un portail des adhérents aux fonctions limitées ; une salle informatique au siège de Pézenas. Dans chaque cave : un logiciel de cave (réception et pesée des apports, suivi des cuves) ; les neuf caves utilisent les logiciels de quatre éditeurs différents |
| Budget du système d'information | 2,2 M€ (environ 1,5 % du chiffre d'affaires) |
| Plan « ROCALDÈNE 2030 » (adopté en décembre 2026) | adapter le vignoble et l'offre au changement climatique et conquérir de nouveaux marchés (export, vente en ligne) ; mieux connaître la qualité des apports, de la parcelle à la bouteille, pour mieux la valoriser ; garantir la continuité du système d'information pendant les campagnes et en réduire l'empreinte environnementale |

**Les neuf caves coopératives**

| Cave | Département | Adhérents | Vignes (hectares) | Salariés permanents |
|---|---|---|---|---|
| Cave de CAUSSELAC | Hérault | 230 | 1 100 | 18 |
| Cave de ROQUEVERNE | Hérault | 200 | 950 | 16 |
| Cave de LAURADEL | Aude | 180 | 850 | 14 |
| Cave de SAINT-BRÉZIAN | Hérault | 170 | 800 | 13 |
| Cave de CABRISSAC | Aude | 150 | 700 | 12 |
| Cave de GRAUSSELLE | Hérault | 140 | 650 | 11 |
| Cave de PECHAUROUX | Aude | 130 | 550 | 10 |
| Cave de TERRAGOUSSE | Hérault | 110 | 500 | 9 |
| Cave de VALCROZIÈRES | Aude | 90 | 400 | 7 |
| **Total** | | **1 400** | **6 500** | **110** |

Chaque cave est dirigée par un directeur salarié, sous l'autorité de son propre conseil, que préside un viticulteur élu ; le président de chaque cave siège au conseil de l'union.

**Organigramme simplifié (mars 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil de l'union | président du conseil, composé des présidents des neuf caves | M. Gilles ESCOURBIAC, viticulteur |
| Direction générale | directrice générale, qui porte le plan « ROCALDÈNE 2030 » | Mme Hélène MAZERANDE |
| Rattaché à la directrice générale | directeur commercial (vrac, grande distribution, export, service clients, projet de vente en ligne) | M. Damien SALVERNAC |
| Rattachée à la directrice générale | directrice de la production et de la qualité (assemblage et élevage des vins, laboratoire d'analyses, conditionnement et logistique) | Mme Claire BOUSQUIÉRAN |
| Rattaché à la directrice générale | directeur administratif et financier (comptabilité, contrôle de gestion, paie et ressources humaines, achats) | M. Philippe VERDAGNOL |
| Direction administrative et financière | responsable administratif et financier adjoint, rattaché à la directrice générale pour le projet de refonte du système d'information | vous |
| Rattaché au directeur administratif et financier | responsable du système d'information (équipe informatique de 6 personnes) | M. Sébastien CAUSSINEL |
| Caves | neuf caves coopératives, chacune avec son président et son directeur | — |

Le comité de direction de l'union réunit chaque mois la directrice générale et les trois directeurs qui lui sont rattachés. La directrice générale réunit chaque trimestre les neuf directeurs de cave.

### ANNEXE 3.1 – Le système d'information pendant la campagne et l'incident de septembre 2026 (note de M. Sébastien CAUSSINEL, responsable du système d'information, février 2027)

**A. Les applications utilisées pendant la campagne de vendanges**

| Application | Où elle fonctionne | Ce qu'elle permet pendant les vendanges | Volumes de la vendange 2026 |
|---|---|---|---|
| Logiciel de cave : réception et pesée des apports | sur un serveur installé dans le local de chaque cave ; quatre éditeurs différents (MOUSTERAL Logiciels équipe les caves de GRAUSSELLE, CABRISSAC et TERRAGOUSSE) | pesée de chaque remorque sur le pont-bascule, mesure du degré, impression du bon d'apport remis au viticulteur ; le bon décide, dans les minutes qui suivent, de la cuve dans laquelle la vendange est versée ; une fois versée, la vendange ne peut plus être pesée de nouveau | environ 20 000 apports de fin août à mi-octobre, sur 45 jours d'ouverture des quais de réception, de 7 h à 21 h ; jusqu'à 900 apports par jour pour les neuf caves, dont 120 pour la seule cave de CAUSSELAC |
| Logiciel de cave : suivi des cuves | même serveur que la réception | remplissage des cuves, températures de fermentation relevées deux fois par jour par le maître de chai | — |
| Logiciel du laboratoire de l'union | salle informatique de l'union, à Pézenas | analyse d'un prélèvement de moût de chaque apport, apporté par une navette deux fois par jour ; les résultats doivent être connus le lendemain à 8 h, quand les œnologues décident de la conduite des cuves ; les échantillons sont conservés 48 heures au froid et peuvent être analysés de nouveau | environ 22 000 analyses, jusqu'à 1 000 par jour de pointe |
| Progiciel de gestion de l'union | salle informatique de l'union ; sauvegarde chaque nuit | commandes, conditionnement, expéditions et facturation, qui continuent pendant les vendanges ; les enseignes de la grande distribution appliquent des pénalités en cas de livraison en retard | environ 40 commandes par jour en septembre et octobre, environ 80 commandes par jour en novembre et décembre, pic des ventes de fin d'année |
| Messagerie en ligne | service d'un fournisseur extérieur | échanges entre les caves, l'union et les adhérents | — |

En dehors des vendanges, les quais de réception sont fermés et les logiciels de cave ne servent qu'au suivi des cuves et aux relevés adressés aux adhérents.

**B. L'incident de la cave de GRAUSSELLE (septembre 2026)**

Les vendanges ont commencé le lundi 31 août 2026. Le mardi 1er septembre, à 6 h 30, l'agent de réception de la cave de GRAUSSELLE a trouvé l'écran du serveur bloqué par un message de rançon : un rançongiciel avait chiffré le serveur. Le disque de sauvegarde, branché en permanence sur ce serveur, avait été chiffré lui aussi ; la dernière copie conservée ailleurs, chez le prestataire, datait du 15 juin 2026.

- M. Fabien CASTANIÉRAC, directeur de la cave, a appelé TRAMONTEL Informatique, le prestataire informatique local qui entretient le serveur, arrivé à 11 h, puis MOUSTERAL Logiciels, dont l'assistance téléphonique n'ouvre qu'à 9 h. L'équipe informatique de l'union n'a été prévenue qu'à 10 h. Le président de la cave voulait payer la rançon, l'union s'y opposait : personne ne savait qui devait décider, et la question n'a été tranchée que le lendemain.
- Les 85 apports du lundi 31 août ont été perdus ; ils ont été reconstitués à partir des doubles des bons conservés par les viticulteurs.
- Du 1er au 3 septembre, pendant trois jours, les pesées et les degrés ont été notés à la main sur des feuilles volantes, sans numérotation : environ 300 apports. L'attente des remorques, habituellement de 20 minutes, a atteint 3 heures ; des remorques de raisin sont restées au soleil, et des adhérents sont repartis pour revenir le soir. « On a perdu la confiance de nos adhérents en trois jours », résume M. CASTANIÉRAC.
- Le logiciel a été remis en service le vendredi 4 septembre à midi, sur un nouveau serveur. Deux salariés de la cave ont ressaisi les 385 bons en deux jours ; les adhérents ont relevé 25 erreurs sur leurs relevés d'apports (numéro d'adhérent, poids, degré). La reprise de l'incident (ressaisie des bons, rapprochement avec les doubles, reprise des fiches, réponses aux adhérents) a coûté environ 250 heures de travail à la cave.
- Les fiches des adhérents et des parcelles modifiées entre le 15 juin et le 31 août ont dû être reprises une à une.
- Dans trois autres caves, le disque de sauvegarde est lui aussi branché en permanence sur le serveur. Aucune cave n'a jamais essayé de restaurer ses données à partir d'une sauvegarde. Aucune cave ne dispose d'une procédure écrite de réception sans le logiciel.

**C. Qui intervient sur le système d'information des caves**

| Acteur | Rôle actuel |
|---|---|
| Équipe informatique de l'union (6 personnes) | progiciel de l'union, laboratoire, messagerie ; aide les caves à leur demande, par téléphone, sans organisation particulière pendant les vendanges ; ne connaît pas l'état des sauvegardes des caves |
| Directeurs des neuf caves | ont choisi leur logiciel et leur prestataire ; responsables du serveur de leur cave ; recrutent et forment les saisonniers de la réception |
| TRAMONTEL Informatique | entretient les serveurs et les postes de cinq caves, à la demande, sans délai d'intervention garanti ; les quatre autres caves ont chacune leur propre prestataire |
| Éditeurs des logiciels de cave (quatre) | maintiennent leur logiciel ; assistance téléphonique les jours ouvrés, de 9 h à 18 h, y compris pendant les vendanges |

**D. Le pilotage de la campagne**

Il n'existe aucun tableau de bord du système d'information pendant la campagne. L'équipe informatique de l'union a reçu 14 incidents signalés par téléphone, dont 4 ont interrompu la réception informatisée d'une cave plus d'une heure (panne de l'imprimante des bons, perte du lien avec le pont-bascule, coupure du réseau, rançongiciel) ; aucun registre n'en est tenu. L'attente des remorques n'est mesurée dans aucune cave. Le soutien informatique de la campagne 2026 a coûté 95 k€ : 45 k€ de prestataires des caves (dont 25 k€ d'intervention et 10 k€ de serveur pour l'incident de GRAUSSELLE), 20 k€ d'interventions des éditeurs et 30 k€ d'heures supplémentaires de l'équipe informatique de l'union, soit environ 250 € par millier d'hectolitres reçus. Mme MAZERANDE souhaite, pour la campagne 2027, « un point quotidien, chiffré, sur une page ».

### ANNEXE 3.2 – La fiabilité des apports (constats de Mme Claire BOUSQUIÉRAN, directrice de la production et de la qualité, janvier 2027, et demande de la directrice générale)

**A. Constats établis à partir des extractions des neuf logiciels de cave (vendange 2026)**

1. *Degrés modifiés après la pesée* : les logiciels de trois éditeurs sur quatre permettent de modifier le degré d'un bon après son impression, sans demander de motif ; ils conservent la date de la dernière modification, mais pas la valeur d'origine. Environ 600 bons (3 % des apports), dans sept caves, ont été modifiés après leur impression. Le rapprochement des bons papier présentés par les adhérents qui se sont plaints montre des écarts de degré de plus de 0,5 % vol., à la hausse comme à la baisse. Un adhérent s'est plaint : « mon bon papier indique 13,2, mon relevé 12,6 ; personne ne m'a prévenu ». Le degré entre dans la rémunération des adhérents par leur cave.
2. *Comptes partagés au poste de pesée* : dans six caves, les agents de réception, saisonniers compris, se connectent avec un compte unique « PESÉE », dont le mot de passe est affiché près du poste.
3. *Cumul des fonctions* : dans la plupart des caves, le chef de quai peut créer un adhérent ou une parcelle, enregistrer une pesée et modifier un bon ; dans trois caves, le directeur dispose des droits d'administration et modifie lui-même les paramètres, dont le poids à vide des remorques déduit de chaque pesée.
4. *Absence de journal des modifications* : seul l'éditeur qui équipe SAINT-BRÉZIAN et VALCROZIÈRES tient un journal des modifications, désactivé à VALCROZIÈRES. Ailleurs, la seule trace d'origine est le bon papier remis au viticulteur.
5. *Aucun contrôle a posteriori* : personne ne rapproche les bons imprimés des relevés adressés aux adhérents ; les directeurs signent chaque mois un état récapitulatif des apports.

**B. La proposition de MOUSTERAL Logiciels : un module de détection des apports anormaux (extraits de la plaquette commerciale et du test)**

- « Fondé sur l'apprentissage automatique, le module apprend, à partir des apports passés, ce qu'est un apport normal (poids, degré, heure, parcelle, cépage, adhérent) et signale en temps réel les apports qui s'en écartent. Il détecte 9 apports anormaux sur 10. »
- Le module a appris sur les apports des vendanges 2023 à 2025 des trois caves équipées par MOUSTERAL Logiciels ; pour les six autres caves, il faudrait extraire les données de trois autres logiciels.
- Option proposée : le blocage automatique de tout bon signalé, jusqu'à sa validation.
- Coût : 20 k€ de mise en place, puis 15 k€ par an pour les neuf caves.
- Test conduit par l'éditeur sur les environ 2 000 apports de la vendange 2026 de GRAUSSELLE : le module a signalé 300 apports (15 %), dont 20 seulement ont été confirmés comme des erreurs ou des anomalies après examen par Mme BOUSQUIÉRAN ; les 280 autres s'expliquaient par les pluies de la mi-septembre, qui ont fait baisser les degrés, par la première récolte d'un cépage planté en 2023 et par les apports ressaisis après l'incident de septembre. Six bons modifiés à la main après la pesée n'ont pas été signalés, le module ne voyant que la valeur finale du degré.

**C. La demande de Mme Hélène MAZERANDE, directrice générale (février 2027)**

« Les adhérents doivent pouvoir faire confiance à leur bon, et le conseil aux chiffres des apports. Avant la campagne 2027, je veux un audit du module des apports des logiciels de cave, dans les neuf caves : de la pesée au relevé adressé à l'adhérent, qui peut faire quoi, ce qui est tracé, ce qui est contrôlé. Je veux les conclusions en juin 2027, avant de décider du module de MOUSTERAL Logiciels. »

### ANNEXE 3.3 – La salle informatique de l'union et les options d'hébergement (note de M. Sébastien CAUSSINEL, février 2027)

**A. La salle informatique de Pézenas**

- Aménagée en 2008 dans le bâtiment administratif, elle accueille 20 serveurs : progiciel de l'union, laboratoire, fichiers partagés, portail des adhérents, sauvegardes de l'union. Les serveurs des caves n'y sont pas. 12 serveurs ont plus de sept ans ; les 8 autres ont moins de quatre ans. La plupart sont utilisés à moins de 20 % de leurs capacités.
- Les deux climatiseurs datent de 2008. En juillet 2025, pendant la canicule (42 °C à Pézenas), l'un d'eux est tombé en panne : la température a dépassé le seuil d'alerte et le progiciel de l'union a été arrêté 6 heures. Les batteries des onduleurs, de 2016, ne tiennent plus que 8 minutes en cas de coupure de courant, contre 30 minutes à l'origine ; la salle n'a pas de groupe électrogène.
- Les sauvegardes de l'union sont copiées chaque nuit sur un disque installé dans la même salle.
- Consommation d'électricité de 2026 : 130 MWh pour l'ensemble de la salle, dont 65 MWh pour les équipements informatiques ; l'indicateur d'efficacité énergétique (PUE : énergie totale consommée / énergie consommée par les équipements informatiques) est donc d'environ 2,0.

**B. Trois options étudiées**

Dans les options A et B, les 8 serveurs récents seraient conservés et les 12 plus anciens retirés : les applications de l'union seraient regroupées sur ces 8 serveurs, dont les équipements informatiques consommeraient environ 30 MWh par an. Dans l'option C, les serveurs seraient retirés au fur et à mesure du transfert des applications ; ceux du progiciel de l'union resteraient dans la salle de Pézenas jusqu'au remplacement du progiciel.

| | Option A – Rénover la salle de Pézenas | Option B – Héberger les serveurs dans le centre de données régional LIMBRÈZE Data | Option C – Passer à un cloud public |
|---|---|---|---|
| Description | nouveaux climatiseurs et onduleurs, regroupement des applications | serveurs de l'union installés dans un centre de données situé dans l'agglomération de Montpellier, à 40 km ; deux liaisons réseau indépendantes avec Pézenas | applications de l'union hébergées par un fournisseur mondial de cloud public, dans un centre situé dans un autre pays de l'Union européenne ; le progiciel de l'union, en fin de support, ne peut pas y être transféré tel quel et resterait à Pézenas jusqu'à son remplacement |
| Coût de mise en œuvre | 300 k€ | 150 k€ | 250 k€ |
| Coût annuel | 60 k€ (électricité, maintenance) | 80 k€ (hébergement, liaisons) | environ 100 k€, variable selon les capacités consommées |
| Indicateur d'efficacité énergétique (PUE) | 1,5, estimé par le bureau d'études après travaux | 1,3, mesuré en 2026 et publié chaque année par le centre | 1,2, moyenne annoncée pour l'ensemble des centres du fournisseur dans le monde ; aucune valeur pour le centre qui hébergerait les données |
| Consommation d'électricité estimée | environ 45 MWh par an | environ 39 MWh par an | non communiquée : capacités partagées entre clients |
| Origine de l'électricité | contrat actuel du site de Pézenas, électricité du réseau national | contrat d'électricité d'origine renouvelable produite dans la région, attestée par des garanties d'origine | « neutralité carbone » annoncée pour l'ensemble du groupe, obtenue par l'achat de certificats et de crédits de compensation ; selon le fournisseur, l'électricité du pays d'implantation est plus carbonée que celle de la France |
| Réutilisation de la chaleur | aucune | chaleur récupérée pour chauffer une piscine intercommunale voisine | non communiquée |
| Autres éléments | la salle reste dans le bâtiment administratif, exposée aux canicules | un second site, distinct de Pézenas, pourrait recevoir les copies des sauvegardes de l'union et des neuf caves ; personnel présent jour et nuit ; visites possibles | capacités ajoutées en quelques minutes ; facturation à l'usage ; données environnementales fournies par le groupe dans un rapport mondial annuel |

**C. Positions**

- M. Philippe VERDAGNOL, directeur administratif et financier : « Le cloud, c'est moderne, et on ne paie que ce qu'on consomme. »
- M. Sébastien CAUSSINEL : « La salle ne passera pas un nouvel été de canicule, et nos sauvegardes dorment à trois mètres des serveurs. »
- Mme Hélène MAZERANDE : « Le plan veut réduire l'empreinte environnementale du système d'information : je dois pouvoir montrer au conseil des progrès mesurés, pas des promesses. »

### ANNEXE 3.4 – Repères sur la continuité, la sécurité et le numérique responsable (au 31/12/2026)

| Texte ou référentiel | Repères utiles | Situation au 31/12/2026 |
|---|---|---|
| ISO 22301:2019 | Norme internationale qui spécifie les exigences d'un système de management de la continuité d'activité : analyse des impacts sur l'activité, stratégies et plans de continuité, exercices et tests, amélioration continue. | En vigueur |
| ISO/IEC 27001:2022 | Norme internationale qui spécifie les exigences d'un système de management de la sécurité de l'information, fondé sur l'appréciation et le traitement des risques ; son annexe A énumère 93 mesures de sécurité, dont la journalisation, la gestion des droits d'accès, la séparation des tâches et la sauvegarde. | En vigueur |
| ISO/IEC 27002:2022 | Guide de mise en œuvre des mesures de sécurité de l'information (mesures organisationnelles, liées aux personnes, physiques et technologiques). | En vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI) | Méthode d'appréciation et de traitement des risques numériques, en cinq ateliers, qui intègre les parties prenantes de l'écosystème (prestataires, éditeurs). | En vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | 42 mesures de bonnes pratiques, dont des comptes nominatifs, des sauvegardes régulières dont une copie est conservée hors ligne, et des restaurations testées. | En vigueur |
| Loi n° 2021-1485 du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique en France (REEN) | Sensibilisation au numérique responsable, allongement de la durée de vie des équipements, écoconception des services numériques, centres de données et réseaux moins énergivores. | En vigueur |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | Critères d'écoconception des services numériques, dont une famille consacrée à l'hébergement. | En vigueur |

Les Vignerons de ROCALDÈNE n'entrent ni dans le champ de la directive (UE) 2022/2555 dite NIS 2, ni dans celui de la directive CSRD sur la publication d'informations en matière de durabilité : ces deux points sont des données de l'énoncé, qui ne sont pas à discuter. Aucune analyse juridique n'est attendue.

### Travail à faire

La vendange 2026 a montré qu'une panne du système d'information d'une cave peut arrêter la réception des apports en pleine campagne, et que les chiffres des apports ne sont pas toujours fiables. Mme MAZERANDE veut traiter la troisième priorité du plan « ROCALDÈNE 2030 » : garantir la continuité du système d'information pendant les campagnes et en réduire l'empreinte environnementale. Elle vous demande de préparer la campagne 2027, de l'éclairer sur la fiabilité des apports et sur le module proposé par MOUSTERAL Logiciels, et de recommander un hébergement pour les serveurs de l'union. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.4 ainsi que vos connaissances professionnelles.

**3.1 – Analyse d'impact de la campagne de vendanges (2 points)**

Après avoir défini l'analyse d'impact sur l'activité, conduisez-la, à partir de l'annexe 3.1, pour trois applications utilisées pendant la campagne : le logiciel de réception et de pesée des caves, le logiciel du laboratoire et le progiciel de gestion de l'union. Pour chacune, indiquez les processus de l'union ou des caves touchés par son indisponibilité, sa criticité pendant la campagne, la durée maximale d'interruption admissible et la perte de données maximale admissible, en les justifiant. Montrez enfin en quoi la criticité de ces applications varie selon la période de l'année. L'impact sur les états financiers n'est pas à traiter.

**3.2 – Le dispositif de continuité et de reprise de la campagne 2027 (3 points)**

a) Après avoir distingué le plan de continuité d'activité et le plan de reprise d'activité, proposez le dispositif de continuité et de reprise de la réception des apports pour la campagne 2027 : le mode dégradé de la réception, les règles de sauvegarde et de test des restaurations, et l'exercice à conduire avant les vendanges, chacun relié à un enseignement de l'incident de septembre 2026.

b) Répartissez les rôles et les responsabilités de ce dispositif entre l'union, les caves, le prestataire informatique local et l'éditeur du logiciel de cave, puis précisez comment la direction de l'union pilote le dispositif (instance, décisions, compte rendu au conseil). Aucun paramétrage technique n'est attendu.

**3.3 – Le module de détection des apports anormaux (1,5 point)**

Après avoir situé le module proposé par MOUSTERAL Logiciels parmi les familles de l'intelligence artificielle, présentez deux apports et trois limites de ce module pour la détection et la prévention des erreurs et des fraudes sur les apports, ces trois limites portant respectivement sur les données d'apprentissage, les faux positifs et le contrôle humain, en vous appuyant sur l'annexe 3.2. Indiquez enfin si l'union doit l'adopter pour la campagne 2027, et à quelles conditions. Le fonctionnement interne du modèle n'est pas à décrire.

**3.4 – L'audit du module des apports (2 points)**

a) Après avoir défini l'audit du système d'information, présentez en quatre étapes la démarche de l'audit du module des apports demandé par Mme MAZERANDE, du cadrage de la mission à la restitution, en passant par la cartographie du processus de réception, en précisant l'objet de chaque étape dans le cas.

b) Pour trois risques du processus de réception révélés par l'annexe 3.2, précisez le contrôle attendu (accès nominatifs, séparation des tâches, journalisation des modifications) et la manière dont l'auditeur vérifiera qu'il fonctionne.

c) Indiquez trois critères de performance et de conformité que l'audit retiendra, en illustrant chacun par un point de contrôle propre au module des apports.

**3.5 – Le tableau de bord du système d'information de la campagne (1,5 point)**

Après avoir présenté le principe d'un tableau de bord du système d'information qui équilibre la performance, les risques et les coûts, proposez le tableau de bord de la campagne de vendanges 2027 : ses destinataires et sa fréquence, puis trois indicateurs, un de performance, un de risque et un de coût, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe, et justifié par l'annexe 3.1.

**3.6 – Le choix d'un hébergement responsable (3 points)**

a) Après avoir défini la sobriété numérique et précisé ce qu'est une stratégie responsable du système d'information, présentez quatre critères de comparaison des options d'hébergement au regard de leur impact environnemental, chacun assorti d'un indicateur de mesure et de sa limite.

b) Comparez les trois options de l'annexe 3.3 au regard de ces critères, de leur coût sur trois ans et de la continuité du système d'information, puis recommandez une option en précisant deux conditions de sa réussite. Aucun calcul d'empreinte n'est attendu.

c) Proposez deux indicateurs de suivi de l'option recommandée, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
