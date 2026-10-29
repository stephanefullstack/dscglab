# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 2 — Dossier 2 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F04 relations avec les ESN et contrats, F05 projets et changement, F06 gestion des connaissances, F12 sécurité et résilience, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). L'analyse juridique approfondie des contrats est hors programme (programme 1.4) : seuls les principes de gestion de la relation avec l'ESN sont attendus. La répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Choix des formes de contrat | `1.4.b` Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle ; `1.4.d` Méthodologie de négociation contractuelle et analyse des risques | 4 |
| 2.2 Niveaux de service, pénalités et réversibilité | `1.4.c` Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD ; `1.4.e` Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) | 4 |
| 2.3 Planification de la transition | `1.5.d` Planification des ressources, délais, coûts et qualité ; `1.5.e` Identification et gestion des risques (maintenance, évolutivité, sécurité) | 3 |
| 2.4 Transfert des connaissances | `1.6.b` Architecture fonctionnelle des systèmes de knowledge management ; `1.6.c` Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) | 3 |
| **Dossier 2 – Infogérance, transition et transfert des connaissances** |  | **14** |

Répartition indicative : connaissances (définitions de la régie, du forfait, de l'infogérance, du SLA, de l'OLA, du modèle SECI : items 2.1 a, 2.2 a, 2.4 a) 3,5 points, la définition du chemin critique étant notée avec son identification (2.3 b-1) ; analyse du contrat et des niveaux de service, Gantt, dispositif de transfert 10,5 points. Durée conseillée : 14 points × 4,5 minutes ≈ 1 h 05.

---

### 2.1 – Choix des formes de contrat (4 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.b` « Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle » ; `1.4.d` « Méthodologie de négociation contractuelle et analyse des risques ».

**Annexes mobilisées** : annexes 1.4 (témoignages de M. LEMOINE et de Mme VASSEUR) et 2.1 (architecture, niveaux de service de 2026, offre de Nexalis, plan de transition).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Régie : mise à disposition de compétences au temps passé, sous la direction du client, qui porte le risque | 0,5 |
| a-2 | Forfait : livrable défini, prix et délai fixés, risque de dépassement porté par le prestataire | 0,5 |
| a-3 | Infogérance : prise en charge durable de tout ou partie du SI avec engagements de niveaux de service | 0,5 |
| b-1 | Limites de la régie actuelle tirées de l'annexe 2.1 et des témoignages (0,5 par limite, dans la limite de 1) | 1 |
| b-2 | Migration : forfait justifié (périmètre défini, recette, délai impératif) | 0,5 |
| b-3 | Exploitation : infogérance avec SLA justifiée (continuité 7 jours sur 7, fin de la dépendance à une personne) | 0,5 |
| b-4 | Conditions : compétence de pilotage conservée à la DSI, coût complet à comparer, dépendance maîtrisée | 0,5 |

**Réponse indicative**

*2.1 a) – Régie, forfait, infogérance*

- **Régie** (assistance technique) : l'ESN met à disposition des compétences facturées au temps passé (ici 90 jours à 650 € HT, soit 58 500 € HT en 2026) ; elle s'engage sur les moyens fournis, et le client, qui dirige les travaux, porte le risque de délai et de résultat (0,5 pt).
- **Forfait** : l'ESN s'engage à livrer un résultat défini par un cahier des charges, à un prix et dans un délai fixés ; elle porte le risque de dépassement, sauf avenant si le besoin change (0,5 pt).
- **Infogérance** : le client confie durablement à l'ESN tout ou partie de son SI (hébergement, exploitation, supervision, support) ; l'ESN s'engage sur des niveaux de service mesurables, assortis de pénalités ; le client reste responsable de son SI et de ses données et doit piloter la prestation (0,5 pt).

*2.1 b) – Limites de la régie actuelle et recommandations*

Limites de la régie pour Comptoirs Ligériens (1 pt pour deux limites étayées) :
- aucun engagement de niveau de service : disponibilité de 98,6 % sur la plage 6 h – 22 h, 14 incidents bloquants dont 9 un week-end, alors que les commandes du week-end préparent les livraisons du lundi, et 7 heures en moyenne pour rétablir le service, sans levier contractuel ;
- la régie suppose un client capable de diriger les intervenants ; or le pilotage repose sur M. LEMOINE seul, qui part le 30 juin 2027, et les ingénieurs d'Altinéa « changent tous les six mois » : aucune capitalisation ;
- des risques non maîtrisés : aucune restauration de sauvegarde testée, 22 nuits d'interface en échec ou corrigées à la main.

Recommandations :
- **Migration de l'ERP et du portail : forfait** (offre de 36 000 € HT, environnement recetté livré). Le besoin est ponctuel, son périmètre est connu (inventaire de la tâche B), le délai est impératif (30 juin 2027) : le forfait transfère le risque de dépassement à Nexalis, à condition de définir les livrables et les critères de recette (tâche D) et de lier le paiement à la recette (0,5 pt).
- **Exploitation durable : infogérance** avec des niveaux de service adaptés au rythme des magasins (7 jours sur 7, 6 h – 22 h). Elle répond au souhait de Mme VASSEUR d'une DSI qui « pilote » au lieu de « surveiller des serveurs la nuit » et met fin à la dépendance envers une personne (0,5 pt).
- **Conditions** : la DSI garde un responsable du contrat capable de contrôler les niveaux de service (sinon la dépendance envers M. LEMOINE devient une dépendance envers Nexalis, ce que redoute Mme VASSEUR) ; le surcoût apparent (168 000 € HT par an contre 58 500 € HT de régie en 2026) s'apprécie en coût complet, en ajoutant au coût actuel le remplacement de M. LEMOINE, le renouvellement de la salle informatique, une astreinte de week-end et le coût des incidents ; une réversibilité négociée dès la signature limite le risque d'enfermement (0,5 pt).

**Réponses tolérées**
- Forfait de migration confié à un autre prestataire que l'infogérant, ou régie maintenue quelques mois en assistance à la transition, si la cohérence avec le délai et le pilotage est démontrée.
- Mention d'un hébergement en mode SaaS de l'ERP ou d'une tierce maintenance applicative pour l'interface, si elle est justifiée.
- Ordre de grandeur du coût complet, sans chiffrage poste par poste (non attendu).

**Erreurs types**
- *Régie, forfait et infogérance confondus* — confondre régie et forfait ou affirmer que la régie transfère le risque au prestataire ; juste : en régie, le client dirige et porte le risque ; au forfait, le prestataire s'engage sur le livrable.
- `JUR-A05` / `JUR-G11` — présenter l'infogérance comme un transfert de responsabilité ; juste : le client reste responsable de son SI, de ses données et du pilotage de la prestation.
- Recommander un seul contrat pour deux besoins de nature différente (projet ponctuel et service récurrent).
- `JUR-T01` — définitions sans exploitation des chiffres de l'annexe 2.1.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des contrats de prestation informatique | régie, forfait, infogérance | F04 § 1 | guide p. 255 |

---

### 2.2 – Niveaux de service, pénalités et réversibilité (4 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.c` « Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD » ; `1.4.e` « Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) ».

**Annexes mobilisées** : annexes 2.1 (niveaux de service de 2026, articles du projet de contrat, observation de la DSI) et 3.3 (RGPD, NIS 2, Data Act).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | SLA défini : engagement contractuel sur des niveaux mesurables, avec mesure, reporting et conséquences | 0,5 |
| a-2 | OLA distingué : accord interne entre équipes qui soutient le SLA | 0,5 |
| b-1 | Trois faiblesses des articles 6, 7 et 9 confrontées aux chiffres de 2026 (0,5 par faiblesse) | 1,5 |
| b-2 | Rédactions ou indicateurs de remplacement mesurables | 0,5 |
| c-1 | Clause de réversibilité : contenu adapté au cas | 0,5 |
| c-2 | Deux autres clauses justifiées (sous-traitance des données personnelles, audit, sécurité et notification) | 0,5 |

**Réponse indicative**

*2.2 a) – SLA et OLA*

La convention de niveau de service (*Service Level Agreement*) est l'engagement contractuel du prestataire envers son client sur des niveaux de service mesurables (disponibilité, délais de prise en charge et de rétablissement, sauvegardes), avec la méthode et la période de mesure, le reporting et les conséquences d'un manquement, dont les pénalités (0,5 pt). L'accord de niveau opérationnel (*Operational Level Agreement*) est un accord interne entre équipes d'une même organisation (par exemple, chez Nexalis, entre l'hébergement et le support) qui permet de tenir le SLA ; il n'engage pas le prestataire envers le client. Ces notions sont décrites par le référentiel ITIL (0,5 pt).

*2.2 b) – Trois faiblesses du projet de contrat*

| Article | Faiblesse au regard de 2026 | Rédaction ou indicateur proposé |
|---|---|---|
| 6 – plage de mesure | disponibilité mesurée du lundi au vendredi, de 8 h à 18 h : 9 des 14 incidents bloquants de 2026 sont survenus un week-end, et les commandes du week-end préparent les livraisons du lundi ; un taux de 99,5 % ainsi mesuré peut coexister avec des week-ends sans service | disponibilité mesurée de 6 h à 22 h, 7 jours sur 7, soit environ 480 heures par mois : 99,5 % tolère environ 2,4 heures d'indisponibilité par mois ; mesure par la supervision du client ou un outil partagé |
| 6 – prise en charge | prise en charge d'un incident bloquant en 4 heures « ouvrées » : un incident survenu le samedi matin peut n'être pris en charge que le lundi, alors que 9 des 14 incidents bloquants de 2026 sont survenus un week-end | prise en charge en 30 minutes à 1 heure, 7 jours sur 7, sur la plage 6 h – 22 h (astreinte) |
| 6 – rétablissement | « meilleurs efforts » : aucun engagement, alors que le rétablissement moyen a été de 7 heures en 2026 | garantie de temps de rétablissement d'un incident bloquant de 4 heures, y compris le week-end ; indicateur : part des incidents bloquants rétablis en moins de 4 heures, cible 95 % |
| 7 – pénalités | plafond de 5 % de la redevance mensuelle, soit 700 € HT au plus par mois ; déclenchement subordonné à une réclamation écrite dans les 15 jours d'un rapport trimestriel établi par le prestataire lui-même : peu dissuasif et facile à perdre | pénalités automatiques, calculées sur un reporting mensuel contradictoire, plafond porté par exemple à 10 à 15 % de la redevance, et droit de résiliation en cas de manquements répétés |
| 9 – sauvegardes | conservation de sept jours, aucun test de restauration, alors qu'aucune restauration n'a été testée en 2026 : une corruption découverte après une semaine serait irrécupérable | perte de données maximale admissible (RPO) de 24 heures, rétention de 30 jours et archive mensuelle sur un an, copie dans un second site ; test de restauration chaque semestre avec procès-verbal ; indicateur : tests de restauration réussis / tests prévus, cible 100 % |

(Trois faiblesses attendues parmi les cinq, 0,5 pt chacune ; 0,5 pt pour des propositions mesurables.)

*2.2 c) – Réversibilité et autres clauses*

Clause de réversibilité (0,5 pt) : elle organise dès la signature la sortie du contrat, à son terme ou en cas de résiliation, sans interruption de service : restitution de toutes les données (ERP, portail, sauvegardes, historiques) dans un format ouvert et documenté, avec la documentation d'exploitation, en particulier celle de l'interface caisses-ERP ; assistance du prestataire sortant et transfert de compétences vers le repreneur ou la DSI ; maintien du service pendant une période de transition (par exemple six mois) ; prix et délais fixés au contrat, et non « à convenir » ; plan de réversibilité tenu à jour et testé. Pour un service d'informatique en nuage, le Data Act, applicable depuis le 12/09/2025, organise aussi le changement de fournisseur (portabilité des données, assistance à la sortie) (annexe 3.3) ; depuis le 12/01/2027, aucun frais de changement de fournisseur ne peut être facturé (article 29 § 1), à condition que l'hébergement de Nexalis soit un « service de traitement de données » au sens du règlement et non un service conçu en majorité sur mesure pour la coopérative (article 31). Le référentiel du cloud de confiance du Cigref rappelle que toute exigence opérationnelle doit être contractuellement exigible.

Deux autres clauses, parmi (0,5 pt) :
- **Données personnelles** : l'infogérant traite pour le compte de la coopérative des données personnelles (comptes des utilisateurs du portail, coordonnées des producteurs exploitants individuels) ; il est sous-traitant au sens de l'article 28 du RGPD, qui impose un contrat écrit (traitement sur instruction, confidentialité, sécurité, assistance, sort des données en fin de contrat) et interdit le recours à un autre sous-traitant sans autorisation écrite préalable, spécifique ou générale, du responsable du traitement (en cas d'autorisation générale, information préalable et droit d'objection) : l'article 14 doit être modifié en conséquence.
- **Audit** : droit pour la coopérative, ou un tiers qu'elle mandate, d'auditer la prestation, la sécurité et le respect des niveaux de service, avec accès aux preuves et rapports d'audit indépendants.
- **Sécurité et notification des incidents** : engagements de sécurité (authentification multifacteur des administrateurs, localisation des données dans l'Union européenne, chiffrement des sauvegardes) et notification sans délai de tout incident de sécurité. NIS 2 fait de la sécurité de la chaîne d'approvisionnement une mesure de gestion des risques ; sa transposition française n'est pas promulguée au 31/12/2026 (annexe 3.3), mais l'anticiper par contrat est une bonne pratique. La coopérative, centrale d'achat et grossiste alimentaire de plus de 50 salariés, entrerait elle-même dans le champ de NIS 2 comme entité importante dès l'entrée en vigueur de la loi de transposition (annexe II, point 4), et Nexalis, fournisseur de services gérés, également : la sécurité de la chaîne d'approvisionnement deviendrait alors une obligation, que le contrat doit anticiper dès 2027.

**Réponses tolérées**
- Autres valeurs cibles cohérentes avec le contexte (99,7 % sur 6 h – 22 h, rétablissement en 2 ou 6 heures, RPO de 12 heures) si elles sont justifiées par les commandes du week-end.
- Faiblesse relevée sur le reporting trimestriel produit par le seul prestataire, ou sur l'exclusion des « maintenances programmées » sans encadrement, en remplacement de l'une des trois attendues.
- Qualification de la coopérative comme future entité importante au sens de NIS 2 (grossiste alimentaire de plus de 50 salariés) et de Nexalis comme fournisseur de services gérés, présentée comme dépendante de la transposition française.
- Clause de durée et de sortie anticipée, ou clause d'évolution des prix, si elle est justifiée par le risque de dépendance.

**Erreurs types**
- *SLA et OLA confondus* — confondre SLA et OLA ; juste : le SLA engage le prestataire envers le client, l'OLA organise les équipes qui le tiennent.
- *Indicateurs génériques* — proposer des niveaux de service sans plage ni méthode de mesure ; juste : un engagement vaut par sa mesure, sa période et sa conséquence.
- *RTO et RPO inversés* — confondre perte de données admissible (RPO) et durée d'interruption admissible (RTO) dans l'article 9.
- *NIS 2 confondue avec le RGPD ; Statut réglementaire affirmé sans date* — présenter NIS 2 comme applicable en droit français ou la confondre avec le RGPD ; juste : statut de l'annexe 3.3, et deux textes distincts (cybersécurité / données personnelles).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ITIL (PeopleCert) | SLA, OLA, catalogue de services | `itil` / F04 § 3 | en vigueur |
| RGPD, règlement (UE) 2016/679, art. 28 | sous-traitant, contrat écrit | `rgpd` / F15 § 5 | en vigueur |
| Data Act, règlement (UE) 2023/2854 | changement de fournisseur de services en nuage | `data_act` / F07 § 8.5 | applicable depuis le 12/09/2025 |
| Directive (UE) 2022/2555 (NIS 2) et sa transposition française | chaîne d'approvisionnement ; projet de loi non promulgué | `nis2`, `nis2_transposition_fr` / F12 § 6 | non promulguée au 31/12/2026 |
| Référentiel du cloud de confiance (Cigref) | exigences contractuellement exigibles, réversibilité | `cigref_cloud_confiance` / F04 § 4 | publié |

---

### 2.3 – Planification de la transition (3 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.d` « Planification des ressources, délais, coûts et qualité » ; `1.5.e` « Identification et gestion des risques (maintenance, évolutivité, sécurité) ».

**Annexes mobilisées** : annexes 2.1 (plan de transition, contrainte sur M. LEMOINE, échéance du 30 juin 2027) et 1.4 (témoignage de M. LEMOINE).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Barres placées au plus tôt, antériorités respectées | 1 |
| a-2 | Jalons (signature, environnement prêt, recette, décision de bascule, bascule, fin de la régie) | 0,5 |
| a-3 | Contrainte de ressource de M. LEMOINE vérifiée (B, E et F jamais simultanées) | 0,5 |
| b-1 | Chemin critique défini (suite des tâches sans marge, qui fixe la durée minimale du projet) et identifié : A-C-D-F-G-H ; fin en semaine 15 | 0,5 |
| b-2 | Échéance tenue avec une marge d'environ deux semaines et demie ; tâche A (puis D) à surveiller ; marges de B et E | 0,5 |

**Réponse indicative**

*2.3 a) – Diagramme de Gantt (semaine 1 = semaine du 1er mars 2027)*

```
Tâche                          S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15
A Contrats (3)                 ██ ██ ██                                          ◆ J1 fin S3 : contrats signés
B Inventaire, documentation (4)██ ██ ██ ██ ·· ··                                 (marge 2 semaines)
C Environnement (3)                     ██ ██ ██                                 ◆ J2 fin S6 : environnement prêt
D Migration à blanc, recette (4)                  ██ ██ ██ ██                    ◆ J3 fin S10 : recette validée
E Transfert de compétences (3)             ██ ██ ██ ·· ·· ··                     (marge 3 semaines, voir b)
F Restauration, répétition (2)                                ██  ██             ◆ J4 fin S12 : décision de bascule
G Bascule, accompagnement (2)                                         ██  ██     ◆ J5 bascule le week-end des 29 et 30 mai
H Fin de la régie, bilan (1)                                                  ██ ◆ J6 fin S15 : projet clos
```

Dates au plus tôt : A semaines 1 à 3 ; B semaines 1 à 4 ; C semaines 4 à 6 ; D semaines 7 à 10 (après B et C) ; E semaines 5 à 7 (après B) ; F semaines 11 et 12 ; G semaines 13 et 14 (après E et F) ; H semaine 15 (1 pt).

Jalons : contrats signés (fin de la semaine 3, 21 mars), environnement prêt (fin de la semaine 6), recette validée (fin de la semaine 10), décision de bascule après la répétition générale (fin de la semaine 12, 23 mai), bascule (week-end du 29 et 30 mai, semaine 13), fin de la régie et bilan (semaine 15, du 7 au 13 juin) (0,5 pt).

Ressource : M. LEMOINE intervient sur B (semaines 1 à 4), E (semaines 5 à 7) et F (semaines 11 et 12) : aucune semaine commune, le plan au plus tôt respecte la contrainte (0,5 pt).

*2.3 b) – Chemin critique, échéance et points de vigilance*

Le chemin critique est la suite des tâches dont la marge est nulle : tout retard sur l'une d'elles retarde d'autant la fin du projet, dont il fixe la durée minimale. Ici, c'est A-C-D-F-G-H : 3 + 3 + 4 + 2 + 2 + 1 = 15 semaines. Le projet s'achève à la fin de la semaine 15 (13 juin 2027) et la bascule a lieu fin mai : l'échéance du mercredi 30 juin (semaine 18) est tenue, avec une marge d'environ deux semaines et demie (0,5 pt).

Vigilance (0,5 pt) :
- la tâche A est critique et c'est la plus exposée : la négociation des clauses de la question 2.2 peut l'allonger ; si elle dure 5 semaines au lieu de 3, le projet finit en semaine 17 (27 juin), sans plus aucune marge. Il faut donc lancer la négociation des niveaux de service et de la réversibilité dès la semaine 1, en priorité ;
- la tâche D (recette) dépend de la disponibilité des acheteurs et des magasins ;
- B a 2 semaines de marge ; E a 5 semaines de marge au regard des seules antériorités, mais seulement 3 si l'on tient compte de M. LEMOINE, qui doit aussi participer à F en semaines 11 et 12 : E ne doit pas glisser au-delà de la semaine 10.

**Réponses tolérées**
- Gantt dessiné à la main dans un autre format lisible (format libre, JUR-T10), jalons représentés autrement ; numérotation des semaines par dates.
- Bascule placée en fin de semaine 12 ou au début de la semaine 13, si le candidat le justifie.
- Mention d'un réseau PERT en complément, sans calcul développé.

**Erreurs types**
- `JUR-P01` — Gantt illisible, sans jalons, ou noyé de commentaires non demandés.
- Antériorités non respectées (D lancée avant la fin de B ; G avant la fin de E) ou contrainte de ressource ignorée (B, E et F en parallèle pour M. LEMOINE).
- Chemin critique confondu avec la liste des tâches les plus longues ; juste : la suite des tâches sans marge.
- *Schéma directeur confondu avec un plan de projet* — confondre le plan de projet avec un schéma directeur.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Diagramme de Gantt, chemin critique, jalons | planification à partir d'un texte | F05 § 4 | guide p. 285 |

---

### 2.4 – Transfert des connaissances (3 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.b` « Architecture fonctionnelle des systèmes de knowledge management » ; `1.6.c` « Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) ».

**Annexes mobilisées** : annexes 1.4 (témoignage de M. LEMOINE) et 2.1 (interface, nuits corrigées à la main, tâches B, E et F du plan).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Connaissances tacites et explicites distinguées | 0,5 |
| a-2 | Modèle SECI : quatre modes de conversion en spirale | 0,5 |
| b-1 | Trois modes au moins appliqués au cas, chacun avec une action concrète (0,5 par mode) | 1,5 |
| b-2 | Calendrier intégré au plan (B, E, F) et indicateur d'efficacité à cinq champs | 0,5 |

**Réponse indicative**

*2.4 a) – Connaissances tacites et explicites ; modèle SECI*

La connaissance explicite est formalisée et transmissible par un support (procédure, documentation, base de connaissances) ; la connaissance tacite est incorporée à la personne (savoir-faire, intuition, « je sais quels magasins posent problème ») et difficile à formuler (0,5 pt). Le modèle SECI (Nonaka et Takeuchi, 1995) décrit la création de connaissances par quatre conversions successives, en spirale : socialisation (tacite vers tacite, par l'observation et la pratique partagée), externalisation (tacite vers explicite, par la formalisation), combinaison (explicite vers explicite, par l'assemblage et la diffusion) et internalisation (explicite vers tacite, par la mise en pratique) (0,5 pt).

*2.4 b) – Dispositif de transfert des savoirs de M. LEMOINE*

Le savoir critique de M. LEMOINE (corrections nocturnes de l'interface, clôture mensuelle des stocks) est presque entièrement tacite : « ce n'est écrit nulle part ». Dispositif :
- **Externalisation (tâche B, semaines 1 à 4)** : entretiens d'explicitation menés par la DSI ; rédaction, avec M. LEMOINE, des procédures de l'interface et de la clôture, de la liste des magasins dont les fichiers posent problème et des corrections types ; chaque correction manuelle est décrite comme une anomalie à traiter à la source (contrôle de complétude du fichier de caisse) (0,5 pt).
- **Socialisation (tâche E, semaines 5 à 7)** : binôme entre M. LEMOINE et l'ingénieur de Nexalis et le technicien de la DSI qui reprendront l'exploitation ; observation des chargements de 6 heures et de la clôture de mars, puis travail à deux sur les corrections réelles (0,5 pt).
- **Combinaison (tâches E et F)** : intégration des procédures dans la base de connaissances de la DSI et dans la documentation d'exploitation de Nexalis, rapprochement avec la documentation livrée par Altinéa en 2019, et inscription de ces documents dans le plan de réversibilité (question 2.2) (0,5 pt).
- **Internalisation (tâche F, semaines 11 et 12, et clôture de mai)** : les repreneurs exécutent seuls les procédures pendant la répétition générale de la bascule et la clôture de mai, M. LEMOINE n'intervenant qu'en observateur ; les écarts enrichissent la documentation (0,5 pt, si trois modes ne sont pas déjà notés).

Indicateur et pilotage (0,5 pt) : taux de procédures critiques exécutées sans aide par un repreneur = procédures critiques exécutées seules avec succès / procédures critiques recensées en tâche B ; source : registre de la répétition générale et des clôtures ; fréquence : hebdomadaire jusqu'à la bascule ; cible : 100 % à la décision de bascule (fin de la semaine 12) ; axe : apprentissage. Un référent de la DSI est responsable de la base de connaissances après le départ de M. LEMOINE.

**Réponses tolérées**
- Indicateur différent s'il mesure l'appropriation et non la seule production de documents (nombre de nuits d'anomalie traitées sans M. LEMOINE, cible : toutes à partir de mai).
- Proposition de solliciter M. LEMOINE pour un appui ponctuel après son départ, présentée comme une mesure de secours et non comme la solution.
- Mobilisation d'outils (wiki, base de connaissances, vidéos de démonstration), valorisée si elle est rattachée à un mode du modèle.

**Erreurs types**
- *Gestion des connaissances réduite à la GED* — réduire la gestion des connaissances à la rédaction de documents ou à une GED ; juste : dispositif systémique (outils, processus, culture) qui organise aussi la pratique partagée.
- Inverser les modes du modèle (l'externalisation va du tacite vers l'explicite) ; dater ou attribuer le modèle à tort (Polanyi a introduit la connaissance tacite, il n'est pas l'auteur du modèle SECI).
- Dispositif hors calendrier, qui commence après le départ de M. LEMOINE ou ignore sa contrainte de disponibilité.
- Confondre transfert des connaissances et gestion prévisionnelle des emplois (relève des ressources humaines, hors de la question).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Nonaka et Takeuchi, *The Knowledge-Creating Company* (1995) | modèle SECI | `nonaka_takeuchi_seci` / F06 § 1 | publié |
