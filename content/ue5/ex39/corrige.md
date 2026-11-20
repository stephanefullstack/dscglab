# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 39 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F09 performance du SI (grille de maturité), F10 audit et fiabilisation, F12 sécurité et résilience, F14 numérique responsable, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 La note de synthèse de l'audit des piscines et ses suites | `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 2,5 |
| 3.2 La fiabilité de la chaîne « levée → facture » | `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels (ici, le système de facturation de la redevance) | 3 |
| 3.3 Les risques et la sécurité des équipements connectés et des systèmes techniques | `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 3,5 |
| 3.4 La stratégie numérique responsable de l'agglomération | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) (ici, la tension entre l'IA et la sobriété, la trajectoire et la grille de maturité numérique durable) ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI | 4 |
| **Dossier 3 – Fiabiliser, sécuriser et rendre plus sobre le système d'information** |  | **13** |

Répartition indicative : connaissances (note de synthèse et rapport d'audit, fiabilisation et familles de contrôles, typologie des risques, architecture de confiance, sobriété numérique, Green IT et IT for green) environ 2,5 points (items 3.1 a-1, 3.2-1, 3.3 a-1, la définition de l'item 3.3 b-1 et l'item 3.4 a-1) ; analyse des annexes et recommandations environ 10,5 points, soit environ 80 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – La note de synthèse de l'audit des piscines et ses suites (2,5 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la conformité financière et comptable n'est pas traitée par l'UE 5.

**Annexes mobilisées** : annexe 3.1 (cadre de la mission, constats, réactions, demande de la directrice générale des services), annexe 3.5 (guide d'hygiène de l'ANSSI, COSO 2013, RGPD) et annexe 1.1 (piscines, système d'information, organigramme, direction du numérique mutualisée portée par la ville).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Note de synthèse distinguée du rapport (destinataire décideur, brève, hiérarchisée, tournée vers la décision ; le rapport est détaillé, exhaustif et documenté) ; appréciation globale nette ; 20 lignes au maximum | 0,5 |
| a-2 | Deux constats de priorité 1, chacun complet : constat chiffré, risque, recommandation, responsable nommé, échéance datée | 0,5 |
| a-3 | Deux autres constats complets ; hiérarchie justifiée (gravité, récurrence, exposition) ; suivi du plan d'action annoncé | 0,5 |
| b-1 | Deux facteurs de succès reliés aux réactions de l'annexe 3.1 ou à la mutualisation | 0,5 |
| b-2 | Deux points de vigilance reliés au cas, dont l'indépendance de l'auditrice rattachée à la ville | 0,5 |

**Réponse attendue**

*3.1 a) – La note de synthèse*

Le **rapport d'audit** expose de façon complète le périmètre, la méthode, chaque constat avec ses éléments probants, ses causes et ses recommandations ; il s'adresse aux audités et documente la mission. La **note de synthèse** en extrait, pour un décideur qui n'a pas le temps de lire le rapport, l'appréciation globale et les constats qui appellent une décision, **hiérarchisés**, chacun assorti du risque, de la recommandation, du responsable, de la priorité et de l'échéance ; elle tient en une page et prépare une décision (F10 § 1.2 et § 5).

Hiérarchie attendue : les **comptes partagés et les annulations sans validation** (risque de fraude non détectable, relevé déjà en 2021 et en 2023) et le **réseau sans fil du public relié aux caisses**, aggravé par des logiciels sans mises à jour (porte d'entrée ouverte à n'importe quel visiteur, alors qu'une collectivité voisine vient de subir un rançongiciel) viennent en priorité 1 ; l'**écart de 18 k€**, d'un montant limité mais non expliqué, et la **conservation sans limite** des fiches d'anciens abonnés viennent en priorité 2. Le non-suivi des audits précédents ne forme pas un cinquième constat : il justifie le dispositif de suivi qui conclut la note.

Note modèle (environ 17 lignes) :

<!-- note -->
**À Mme VARSANGE – Audit des caisses et de la billetterie des piscines (2026) – Note de synthèse pour le comité de direction du 18/05/2027**
**Appréciation globale** : les encaissements et la sécurité des caisses sont mal maîtrisés ; les faiblesses de 2021 et 2023 persistent.
**1. Comptes partagés et annulations libres (priorité 1).** 45 agents sur 60 sur des comptes communs ; 6 000 tickets annulés (30 k€) sans motif ni validation. Risque : fraude impossible à détecter et à imputer. Recommandation : un identifiant par agent, annulation validée par un responsable, revue hebdomadaire. M. SALVÉRAC, 30/06/2027.
**2. Caisses exposées (priorité 1).** Wi-Fi du public sur le réseau des caisses ; logiciel et système sans mises à jour. Risque : intrusion, vol de données de paiement, caisses arrêtées. Recommandation : séparer les réseaux, corriger, remplacer les postes hors support. M. LANDOUSSE, 30/06/2027 ; postes fin 2027.
**3. Écarts non expliqués (priorité 2).** 18 k€ d'encaissements manquants. Risque : pertes, recettes non fiables. Recommandation : rapprochement quotidien, écart justifié au-delà d'un seuil, revue mensuelle des finances. M. SALVÉRAC et finances, 30/09/2027.
**4. Données conservées sans limite (priorité 2).** 32 000 fiches d'anciens abonnés, dont 25 000 de plus de trois ans. Risque : non-conformité au RGPD, fuite aggravée. Recommandation : durée fixée avec le DPO, purge. M. SALVÉRAC, 31/12/2027.
**Suivi** : plan d'action validé en comité de direction, point trimestriel, audit de suivi en janvier 2028.
<!-- /note -->

*3.1 b) – Facteurs de succès et points de vigilance*

**Deux facteurs de succès** (b-1) :
1. **Un portage par la direction générale et un suivi formalisé des recommandations.** Les plans de 2021 et de 2023 ont été acceptés puis oubliés, faute de suivi. Il faut que Mme VARSANGE fasse valider le plan d'action par le comité de direction, désigne un responsable et une échéance par recommandation, tienne un tableau de suivi présenté chaque trimestre et prévoie un audit de suivi en janvier 2028. C'est la composante « pilotage » du COSO 2013 (annexe 3.5).
2. **L'adhésion des audités, obtenue par des constats établis contradictoirement et des recommandations réalistes.** M. SALVÉRAC conteste : les constats chiffrés doivent lui être présentés comme des faiblesses du dispositif, et non comme un soupçon sur ses agents. Les comptes nominatifs **protègent les agents honnêtes**, puisqu'une annulation n'est plus imputable à toute l'équipe. La recommandation doit tenir compte de sa contrainte d'accueil : changement d'utilisateur rapide (code court ou badge plutôt qu'une nouvelle connexion), validation seulement au-delà d'un seuil.

**Deux points de vigilance** (b-2) :
1. **L'indépendance et la légitimité de l'auditrice.** Mme TRÉVAZIN est une agente de la ville, dont le directeur général arrête son programme et dirige aussi la direction du numérique mise en cause par deux constats (réseau, mises à jour). Elle risque d'être gênée pour critiquer sa propre collectivité, et d'être perçue par l'agglomération comme « l'audit de la ville ». Il faut une lettre de mission signée par la directrice générale de l'agglomération, une restitution directe à celle-ci, une charte d'audit commune aux deux collectivités, et la possibilité de faire revoir par un tiers les constats qui touchent la direction mutualisée.
2. **La dilution des responsabilités entre les directions et l'attentisme.** La direction du numérique renvoie au schéma directeur de 2028 ; la billetterie a été choisie sans elle ; chaque constat peut rebondir entre la direction des piscines, la direction mutualisée et l'éditeur. Il faut désigner **un seul responsable** par recommandation et décider tout de suite des mesures transitoires qui ne dépendent pas du schéma directeur : la séparation du réseau sans fil du public et l'installation des correctifs, demandées à la direction mutualisée par un arbitrage de la directrice générale.

**Réponses tolérées**
- Autre ordre de priorité justifié (par exemple l'écart de 18 k€ en priorité 1 avec les annulations, au titre du risque de détournement de fonds publics), si les quatre constats sont complets.
- Regroupement de la conservation des données et de l'accès tardif à l'extraction de l'éditeur dans un constat de « maîtrise de l'éditeur de billetterie ».
- Note présentée en tableau (constat, risque, recommandation, responsable, priorité, échéance) si elle reste dans les 20 lignes et comporte une appréciation globale.
- Autres facteurs de succès : accès aux données garanti par une clause des contrats des éditeurs (six semaines pour obtenir l'extraction) ; compétences en systèmes d'information de l'auditrice ou appui de la direction mutualisée ; information des élus. Autres points de vigilance : proportionnalité du coût des contrôles aux enjeux (18 k€), conduite du changement des 60 agents d'accueil, confidentialité des constats de sécurité.
- Responsables désignés par leur fonction (directeur des piscines, directeur du numérique mutualisé, responsable de la sécurité des systèmes d'information) plutôt que par leur nom.

**Erreurs fréquentes**
- *Démarche ou tests d'audit développés au lieu de la note* (`JUR-T07`) — juste : la note et ses suites ; la démarche n'est pas demandée.
- *Constats non hiérarchisés ou sans responsable ni échéance* (`JUR-T03`) — juste : une priorité, une personne et une date pour chaque recommandation.
- *Note qui dépasse 20 lignes ou qui recopie les notes brutes* (`JUR-T07`) — juste : une appréciation globale et quatre constats regroupés.
- *Audit du SI confondu avec l'audit légal des comptes* (`ET-34`) — juste : audit interne des caisses et de leur sécurité, sans opinion sur les comptes.
- *Facteurs de succès génériques* (`JUR-T01`) — juste : reliés aux deux audits sans suite, à la contestation de M. SALVÉRAC, à l'attentisme de la direction du numérique et au rattachement de l'auditrice à la ville.
- *Réactions des responsables ignorées* (`JUR-T08`) — juste : elles fondent les facteurs de succès et les points de vigilance.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Note de synthèse, diagnostic d'audit, facteurs de succès | constat, risque, recommandation, priorité, échéance ; indépendance, suivi | F10 § 1.2 et § 5 | notion de cours |
| COSO 2013 | pilotage du contrôle interne, suivi des faiblesses relevées | `coso_2013` ; F10 § 2 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | identification nominative, mises à jour, cloisonnement du réseau | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | durée de conservation limitée, sécurité | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.2 – La fiabilité de la chaîne « levée → facture » (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels » (contrôles applicatifs, séparation des tâches, piste d'audit, intégrité des interfaces, sauvegardes et restauration éprouvées). Limite : la conformité financière et comptable n'est pas traitée ; aucune règle de comptabilité publique ni de finances locales n'est mobilisée.

**Annexes mobilisées** : annexe 3.2 (déroulement, constats de 2026, échéance de juillet 2027), annexe 3.5 (ISO/IEC 27001:2022 et 27002:2022, COSO 2013) et annexe 1.1 (redevance incitative, logiciel de facturation hébergé par l'éditeur, camions).

**Barème indicatif (3 pts)**

| Item | Attendu | Points |
|---|---|---|
| 1 | Fiabilisation définie (données exactes, exhaustives, autorisées, traçables et disponibles) ; contrôles généraux informatiques et contrôles applicatifs distingués | 0,5 |
| 2 | Contrôle de l'interface camions → logiciel : constat, risque, nature, responsable | 0,5 |
| 3 | Contrôle des tarifs et du calcul, avec séparation des tâches : constat, risque, nature, responsable | 0,5 |
| 4 | Traçabilité des corrections (comptes nominatifs, journal) : constat, risque, nature, responsable | 0,5 |
| 5 | Sauvegarde et restauration éprouvée : constat, risque, nature, responsable | 0,5 |
| 6 | Contrôle à mettre en place en premier, justifié par l'échéance de juillet 2027 | 0,5 |

**Réponse attendue**

**Définitions** (item 1). **Fiabiliser** un système d'information de gestion, c'est organiser les traitements et les contrôles pour que les données qu'il produit, ici les levées et les factures, soient **exactes, exhaustives, autorisées, traçables** et **disponibles**, et qu'on puisse reconstituer le chemin de chaque facture jusqu'aux levées qui la justifient (piste d'audit). Les **contrôles généraux informatiques** portent sur l'environnement du système : gestion des accès, gestion des changements, exploitation (sauvegardes, supervision). Les **contrôles applicatifs** sont propres à un traitement : contrôles à la saisie, au traitement, aux interfaces et en sortie (F10 § 2 et § 3). La chaîne « levée → facture » en a besoin des deux.

**Quatre contrôles** (items 2 à 5) :

| Contrôle | Constat de l'annexe 3.2 | Risque traité | Nature | Qui le met en œuvre |
|---|---|---|---|---|
| **Intégrité de l'interface** : chaque fichier porte l'identifiant de la tournée et le nombre de levées ; l'ordinateur embarqué le conserve jusqu'à l'accusé de réception du serveur d'échange ; le logiciel refuse un fichier déjà importé ; chaque matin, un **rapprochement** automatique compare la liste des tournées réalisées, les fichiers reçus et les levées importées, et chaque écart ou rejet est traité et tracé | 120 tournées et environ 20 000 levées perdues ; 300 fichiers réimportés à la main, 5 000 levées facturées deux fois ; aucun rapprochement | facturation **incomplète** (levées perdues, usagers traités inégalement) ou **en double** (réclamations, perte de confiance) | préventive (accusé de réception, refus des doublons) et détective (rapprochement quotidien) | direction du numérique mutualisée (serveur d'échange), fabricant des équipements embarqués et éditeur (évolutions à demander) ; le rapprochement est revu chaque matin par le service de la facturation |
| **Tarifs et calcul des factures** : séparation des tâches entre l'agent qui saisit les tarifs et la responsable du service, qui les valide en les comparant aux tarifs votés avant tout lancement ; contrôles de vraisemblance bloquants (tarif hors d'une plage admise, facture qui dépasse un multiple de celle du semestre précédent) ; revue d'un échantillon de factures et des montants les plus élevés avant l'envoi | un même agent saisit les tarifs et lance la facturation ; tarif saisi à 25 € au lieu de 2,50 € ; 3 000 factures erronées, 900 réclamations | **facturation erronée de masse**, coût de traitement des réclamations, atteinte à l'acceptation de la redevance | préventive (double validation, contrôles bloquants) et détective (revue avant envoi) | Mme DARNÉZAN valide ; l'éditeur sépare les profils de saisie des tarifs et de lancement |
| **Traçabilité des corrections** : un compte nominatif par agent ; un journal des modifications (auteur, date, motif, valeur avant et après) que l'on ne peut pas modifier ; motif obligatoire, validation des corrections au-delà d'un montant ; revue mensuelle d'un échantillon | six agents sur le même compte « facturation » ; 4 000 factures modifiées sans trace | **fraude interne** (dette effacée), **erreurs non détectées**, impossibilité de justifier une facture devant l'usager | préventive (comptes nominatifs, validation) et détective (journal, revue) | l'éditeur (fonction de journalisation, à exiger), la direction du numérique (comptes), le service de la facturation (revue) |
| **Sauvegarde et restauration éprouvée** : sauvegarde du serveur d'échange hors de la salle du siège (par exemple dans la salle de l'hôtel de ville) et copie hors ligne ; alerte en cas d'échec d'une sauvegarde ; **test de restauration** au moins annuel, pour le serveur et pour la base de l'éditeur ; délai de restauration et perte de données admissible fixés avec l'éditeur | aucune restauration essayée ; sauvegarde dans la même salle ; sauvegarde arrêtée depuis l'été sans que personne le voie ; contrat muet | **perte définitive** des levées ou des factures d'un semestre, impossibilité de facturer ou de répondre aux réclamations | préventive (sauvegarde déportée), détective (alerte, test) | direction du numérique mutualisée (serveur d'échange), éditeur (base, preuve du test), service de la facturation (exigences de délai et de perte admissible) |

**Le contrôle à mettre en place en premier** (item 6) : le **contrôle des tarifs et du calcul**. Il se met en place **avant juillet 2027** sans évolution du logiciel : une organisation (double validation, comparaison aux tarifs votés) et une revue avant l'envoi suffisent ; l'erreur qu'il prévient touche des milliers de factures d'un coup (3 000 en juillet 2026). En attendant les évolutions de l'interface, qui dépendent du fabricant et de l'éditeur, un **rapprochement manuel** des tournées réalisées et des fichiers reçus peut compenser.

**Réponses tolérées**
- Le contrôle de l'interface placé en premier, si le candidat justifie par la perte continue de levées (1 % des tournées) et par les doublons, et prévoit un contrôle compensatoire des tarifs pour juillet 2027.
- Séparation des tâches présentée comme un cinquième contrôle, à condition que les quatre contrôles demandés soient traités.
- Référence au COSO 2013 (activités de contrôle) ou aux mesures de journalisation et de sauvegarde de l'ISO/IEC 27002:2022.
- Exigences envers l'éditeur exprimées comme des engagements de service (délai de restauration, perte admissible, preuve des tests), sans analyse juridique du contrat.
- Délai de restauration et perte de données admissible désignés par les sigles RTO et RPO, correctement définis.

**Erreurs fréquentes**
- *Contrôles génériques, sans lien avec les constats* (`JUR-T01`, `JUR-T08`) — juste : chaque contrôle répond à un chiffre de l'annexe 3.2.
- *Sauvegarde sans test de restauration* (`JUR-S02`) — juste : une sauvegarde qu'on n'a jamais restaurée ne prouve rien ; l'été 2026 le montre.
- *Dérive vers la comptabilité publique ou le recouvrement* (limite du programme) — juste : la transmission au comptable public n'est pas à étudier.
- *Confusion entre un contrôle et un outil* (« acheter un logiciel ») (`ET-01`) — juste : un contrôle est une règle, avec un responsable et une trace.
- *Nature préventive ou détective omise* — juste : elle est demandée pour chaque contrôle.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Fiabilisation, contrôles généraux et applicatifs, séparation des tâches, piste d'audit | définitions et contrôles | F10 § 2 et § 3 | notion de cours |
| COSO 2013 | activités de contrôle (toléré) | `coso_2013` ; F10 § 2 | en vigueur |
| ISO/IEC 27002:2022 | mesures de journalisation, de sauvegarde et de contrôle d'accès | `iso_27002_2022` ; F12 § 2 | en vigueur |

---

### 3.3 – Les risques et la sécurité des équipements connectés et des systèmes techniques (3,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information… ». Limite : l'analyse de sécurité technique détaillée n'est pas attendue.
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique et les démarches de certification ne sont pas attendues ; le Zero Trust est un cadre, pas un produit.

**Annexes mobilisées** : annexe 3.3 (inventaire, incidents, témoignages), annexe 3.5 (ISO/IEC 27001:2022, guide d'hygiène, Zero Trust, Cyber Resilience Act, RGPD) et annexe 1.1 (camions, déchèteries, piscines, direction du numérique mutualisée portée par la ville).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée : trois catégories définies ; risque = événement redouté apprécié par sa probabilité et son impact | 0,5 |
| a-2 | Cinq risques tirés de l'annexe 3.3, formulés comme des événements, couvrant les trois catégories | 0,5 |
| a-3 | Deux risques prioritaires justifiés par leur probabilité et leur impact | 0,5 |
| b-1 | Architecture de confiance définie ; principes de séparation des réseaux et d'accès à distance des mainteneurs, reliés aux constats | 0,5 |
| b-2 | Principes de chiffrement et de mises à jour (inventaire, mots de passe d'usine), reliés aux constats | 0,5 |
| c-1 | Rôles des quatre acteurs (agglomération, direction du numérique et RSSI, éditeurs et fabricants, mainteneurs) | 0,5 |
| c-2 | Formalisation (politique étendue, matrice des rôles, clauses de sécurité, instance) et positionnement du RSSI | 0,5 |

**Réponse attendue**

*3.3 a) – Typologie, cinq risques et deux priorités*

Un **risque** lié au système d'information est un événement redouté qui atteint la disponibilité, l'intégrité, la confidentialité ou la traçabilité de l'information et des traitements ; il s'apprécie par sa **probabilité** et son **impact**. On distingue : les **cybermenaces**, actes malveillants (rançongiciel, intrusion, usurpation d'un compte) ; les **défaillances opérationnelles**, pannes, erreurs ou défauts d'exploitation et de maintenance, y compris la dépendance à un prestataire ; les **risques réglementaires et métiers**, non-respect d'une obligation et atteinte à la mission elle-même, ici le service public (F12 § 0 et § 5).

| N° | Risque (événement redouté) | Catégorie | Faits de l'annexe 3.3 |
|---|---|---|---|
| R1 | Rançongiciel entré par l'accès à distance du mainteneur, qui chiffre la télégestion des piscines puis se propage aux réseaux de bureau de l'agglomération et de la ville | cybermenace | accès permanent, compte unique de 12 techniciens, mot de passe de 2019, messagerie sur le poste de supervision, réseaux non séparés ; scénario survenu chez la voisine en novembre 2026 |
| R2 | Prise de contrôle des ordinateurs embarqués des camions, qui fausse ou supprime les levées et sert de porte d'entrée | cybermenace | même mot de passe d'usine sur 40 ordinateurs, faille publiée en 2026 non corrigée, accès au réseau mobile |
| R3 | Arrêt des six déchèteries par la panne du serveur unique du contrôle d'accès | défaillance opérationnelle | un samedi bloqué en septembre 2026, 2 000 usagers refoulés ou admis sans contrôle ; aucun inventaire de la direction du numérique |
| R4 | Panne ou dysfonctionnement durable d'un équipement non maintenu (camions, contrôle d'accès, télégestion), faute d'un responsable de ses mises à jour, les contrats ne traitant pas de la sécurité | défaillance opérationnelle (dépendance aux prestataires) | « c'est au client de les installer » ; « notre contrat ne porte pas sur l'informatique » |
| R5 | Mise en cause de l'agglomération pour la conservation sans limite des images de plaques d'immatriculation des véhicules des professionnels, qui permettent d'identifier des personnes (RGPD : conservation limitée, sécurité adaptée, annexe 3.5) | risque réglementaire | images des plaques conservées sans limite de durée ; caméras sur le réseau de bureau |
| R6 | Fermeture des piscines ou mauvais traitement de l'eau, mettant en jeu la santé des baigneurs et la continuité du service public | risque métier | télégestion non pilotable chez la voisine ; objectif « continuité et sécurité des services publics, numériques et techniques » de « Castelrive 2032 » |

Cinq risques suffisent, dont au moins un par catégorie.

**Deux risques prioritaires** (a-3) :
- **R1** : **probabilité élevée**. L'accès est ouvert en permanence, avec un compte partagé et un mot de passe inchangé depuis 2019, et le scénario vient de se réaliser chez une voisine. **Impact très fort** : fermeture des quatre piscines pendant des semaines, risque sanitaire, propagation à toute l'agglomération et à la ville par des réseaux non séparés.
- **R2** : **probabilité élevée**, avec un mot de passe d'usine identique sur 40 ordinateurs et une faille connue non corrigée. **Impact fort** : la collecte et la facturation de 84 000 redevables reposent sur ces levées.
On peut aussi retenir R6, conséquence métier de R1, si le choix est justifié.

*3.3 b) – Quatre principes d'architecture de confiance*

Une **architecture de confiance** organise les systèmes pour que la confiance accordée à un utilisateur, à un équipement ou à une connexion soit **vérifiée à chaque accès et limitée au nécessaire** : authentification, autorisation au moindre privilège, chiffrement, cloisonnement, traçabilité. Le modèle **Zero Trust** en est le cadre de référence : aucune confiance implicite liée à la place dans le réseau. C'est un modèle d'architecture que l'on adopte progressivement, en complément de la défense en profondeur, et non un produit (annexe 3.5 ; F12 § 3).

| Principe | Application aux équipements de l'agglomération | Constat de l'annexe 3.3 |
|---|---|---|
| (b-1) **Séparation des réseaux techniques et du réseau de bureau** | placer la télégestion, le contrôle d'accès et le serveur d'échange des camions dans des zones distinctes du réseau de bureau et du réseau de la ville, avec des échanges limités au strict nécessaire et contrôlés ; un poste de supervision dédié, sans messagerie ni navigation | équipements sur le même réseau que les bureaux, lui-même relié à la ville ; caméras sur le réseau de bureau ; messagerie sur le poste de supervision |
| (b-1) **Authentification et traçabilité des accès à distance** | un compte nominatif par technicien du mainteneur, une authentification à plusieurs facteurs, un accès ouvert à la demande pour une intervention et refermé ensuite, par un point d'entrée unique contrôlé par l'agglomération plutôt qu'un logiciel de prise de main installé sur le poste ; sessions journalisées et revues | compte unique de 12 techniciens, mot de passe de 2019, accès à tout moment |
| (b-2) **Chiffrement** | chiffrer les échanges entre les capteurs et la plateforme, entre les camions et le serveur d'échange, et les données sensibles stockées (images des plaques) ; en faire une exigence envers les fabricants | mesures des capteurs transmises sans chiffrement ; levées transmises par le réseau mobile |
| (b-2) **Mises à jour et durcissement** | inventaire de tous les équipements connectés et techniques ; mots de passe d'usine changés et distincts pour chaque équipement ; politique de mise à jour avec calendrier et responsable ; à l'achat, exiger une durée de support et des mises à jour de sécurité, que le Cyber Resilience Act imposera aux fabricants à partir du 11/12/2027 | ordinateurs jamais mis à jour, faille non corrigée, mot de passe d'usine identique sur 40 ordinateurs, aucun équipement dans l'inventaire |

*3.3 c) – Rôles, responsabilités et formalisation*

Ces équipements sont des **systèmes critiques** du service public : la collecte, la facturation, les déchèteries et la sécurité des baigneurs en dépendent. Leur sécurité ne peut être laissée « au technique ».

| Acteur | Rôles et responsabilités |
|---|---|
| **Directrice générale des services de l'agglomération** | approuve l'extension de la politique de sécurité aux systèmes techniques, fixe le niveau de risque accepté, arbitre les moyens avec la ville au sein de l'instance commune, rend compte aux élus |
| **Directions utilisatrices** (collecte, piscines) | propriétaires de leurs systèmes et des risques métier : déclarent leurs équipements à l'inventaire, autorisent les accès de leurs mainteneurs, prévoient le mode dégradé (conduite manuelle des chaufferies, ouverture manuelle des barrières), font inscrire les exigences de sécurité dans leurs contrats |
| **Direction du numérique mutualisée** | exploite la séparation des réseaux, le point d'entrée des accès à distance, les sauvegardes et la supervision ; installe les mises à jour ou en contrôle l'installation |
| **RSSI mutualisé** | définit les règles, conduit l'analyse des risques, conseille les directions, revoit les accès, pilote le traitement des incidents, rend compte de l'état de sécurité |
| **Éditeurs et fabricants** | fournissent des produits sûrs, publient et signalent les correctifs de sécurité, informent l'agglomération des vulnérabilités et des incidents (obligations du Cyber Resilience Act, échelonnées de 2026 à 2027), respectent les exigences de chiffrement et de comptes |
| **Mainteneurs** | n'accèdent qu'avec des comptes nominatifs et sur demande, tracent leurs interventions, sécurisent leurs propres postes et signalent sans délai tout incident |

**Formalisation et suivi** (c-2) : (1) la **politique de sécurité de 2023 étendue** aux équipements connectés et aux systèmes techniques ; (2) une **matrice des responsabilités** (réalise, approuve, consulté, informé) pour l'inventaire, les accès à distance, les mises à jour et les incidents ; (3) des **clauses de sécurité** ajoutées aux contrats de maintenance et aux contrats des éditeurs (mises à jour, accès, signalement des incidents, droit d'audit) ; (4) un **comité de sécurité commun** à la ville et à l'agglomération, qui se réunit chaque trimestre et suit les risques et le plan d'action.

**Positionnement du RSSI** : rattaché au directeur du numérique, il contrôle ce que sa propre hiérarchie exploite, et il n'a aucune autorité sur l'agglomération. Il devrait relever **fonctionnellement des deux directions générales**, ou de leur comité de sécurité commun, avec une mission écrite qui couvre les systèmes techniques des deux collectivités, un droit d'alerte direct auprès de Mme VARSANGE et des **correspondants sécurité** dans les directions de la collecte et des piscines.

**Réponses tolérées**
- Transmission sans chiffrement des mesures des capteurs présentée comme un risque d'intégrité (mesures faussées, tournées mal calculées), en cybermenace ou en défaillance ; elle ne relève pas du RGPD, ces mesures ne se rapportant à aucune personne.
- Autres risques pertinents : usurpation du compte partagé de la plateforme des capteurs ; dépendance à un mainteneur unique pour la nuit ; fraude à l'accès aux déchèteries ; risque d'image auprès des usagers et des élus.
- Cotation qualitative (faible, moyen, fort) ou matrice probabilité × impact, sans calcul.
- Référence aux mesures du guide d'hygiène de l'ANSSI (identification nominative, changement des éléments d'authentification par défaut, cloisonnement, mises à jour, maîtrise des risques liés aux prestataires) ou à l'annexe A de l'ISO/IEC 27001:2022.
- Matrice des responsabilités présentée en tableau croisé (activités × acteurs).
- Mention de NIS 2 comme cadre de gouvernance possible, si elle est datée correctement (directive non transposée en France au 31/12/2026) et si le candidat ne cherche pas à qualifier l'agglomération au regard de ce texte.

**Erreurs fréquentes**
- *Zero Trust présenté comme un produit à acheter* (`ET-04`, `JUR-S03`) — juste : un cadre d'architecture, progressif.
- *Mesures techniques détaillées ou paramétrages* (limite du programme 4.2) — juste : des principes, reliés aux constats.
- *Risques non classés ou catégorie manquante* (`JUR-T03`) — juste : cinq risques, trois catégories.
- *Sécurité des systèmes techniques laissée aux mainteneurs ou à la seule direction du numérique* (`JUR-T11`) — juste : responsabilités partagées, propriétaires métier dans les directions.
- *RSSI présenté comme un technicien ou maintenu sous le seul directeur du numérique* (`ET-15`) — juste : une autorité fonctionnelle sur les deux collectivités.
- *Référentiels, normes et solutions confondus* (`ET-01`, `JUR-S06`) — juste : ISO/IEC 27001 (norme), guide d'hygiène (guide), Zero Trust (modèle), Cyber Resilience Act (règlement).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques, architecture de confiance, rôles | définitions, principes | F12 § 0, § 1, § 3 et § 5 | notion de cours |
| ISO/IEC 27001:2022 et ISO/IEC 27002:2022 | mesures de l'annexe A (accès, vulnérabilités, séparation des réseaux, fournisseurs) | `iso_27001_2022`, `iso_27002_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | identification nominative, authentification par défaut, cloisonnement, mises à jour, prestataires | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Modèle Zero Trust (avis de l'ANSSI, 2021) | cadre d'architecture | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| Règlement (UE) 2024/2847 (Cyber Resilience Act) | obligations des fabricants : sécurité dès la conception, mises à jour, signalement | `cra` ; F12 § 7 | signalement depuis le 11/09/2026 ; application générale le 11/12/2027 |
| Règlement (UE) 2016/679 (RGPD) | conservation limitée, sécurité | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.4 – La stratégie numérique responsable de l'agglomération (4 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable… » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI ». Limites : la durabilité doit être intégrée à la gouvernance globale du SI et non traitée comme un ajout marginal ; les résultats d'empreinte sont donnés, jamais calculés.

**Annexes mobilisées** : annexe 3.4 (obligation non remplie, état des lieux, premières mesures, projet de tournées optimisées), annexe 3.5 (loi REEN, RGESN, étude ADEME-Arcep) et annexe 1.1 (projet « Castelrive 2032 », direction du numérique mutualisée, dépenses du numérique).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Sobriété numérique définie (interroger le besoin d'abord) ; Green IT et IT for green distingués ; pour au moins trois dimensions, niveau actuel décrit de façon observable et justifié par l'annexe 3.4, et niveau visé en 2030, sur l'échelle à quatre niveaux donnée par la question | 0,5 |
| a-2 | Deux premiers axes, reliés chacun à un constat chiffré | 0,5 |
| a-3 | Deux autres axes, et ordre de priorité justifié (part de la fabrication, gains rapides) | 0,5 |
| a-4 | Gouvernance (adoption, portage, instance commune avec la ville, intégration au futur schéma directeur) et trajectoire datée jusqu'en 2030 | 0,5 |
| b-1 | Deux arguments en faveur du projet et deux limites tirées de l'annexe 3.4 D | 0,5 |
| b-2 | Conditions de la recommandation (expérimentation, mesure du bilan net, sobriété du dispositif) | 0,5 |
| c-1 | Premier indicateur complet (formule, source, fréquence, cible, axe) | 0,5 |
| c-2 | Second indicateur complet | 0,5 |

**Réponse attendue**

*3.4 a) – Définitions, grille de maturité et stratégie*

La **sobriété numérique** consiste à interroger d'abord le **besoin** (cet équipement, ce service, ce calcul, cette impression sont-ils utiles ?) avant de chercher l'efficacité ; elle ne se réduit pas à une économie d'énergie. Le **Green IT** réduit l'empreinte du système d'information lui-même (équipements, salles informatiques, logiciels, usages). L'**IT for green** mobilise le numérique pour réduire l'empreinte d'une autre activité de l'organisation : le projet de tournées optimisées en relève (F14 § 3).

**Grille de maturité du numérique responsable** (F09 § 5 ; F14). Les quatre niveaux sont donnés par la question ; la grille complète figure ici à titre de référence, et le candidat n'a qu'à décrire, pour chaque dimension, le niveau actuel et le niveau visé :

| Dimension | 1 – Initial | 2 – Engagé | 3 – Structuré | 4 – Piloté | Agglomération en 2027 → cible 2030 |
|---|---|---|---|---|---|
| Équipements et achats | renouvellement à date fixe, achat au prix | actions ponctuelles (réemploi occasionnel) | durée de vie allongée, critères environnementaux dans les achats | durée de vie et achats suivis par des indicateurs, revus chaque année | **1** (postes tous les quatre ans par lots, téléphones tous les deux ans, prix seul, 30 % des tablettes inutilisées) → **3** |
| Infrastructures | aucune mesure | consommation connue | serveurs inutiles retirés, consolidation, PUE suivi | PUE et consommation pilotés selon une cible | **1 à 2** (PUE 2,2 et 2,0, 40 serveurs inutiles, utilisation de 15 %, 900 MWh connus) → **3** |
| Usages et services | aucune règle | « écogestes » affichés | règles d'impression et de stockage, sensibilisation, écoconception des nouveaux services | évaluation environnementale de chaque projet avant décision | **2** (écogestes de 2023, 4 millions de pages) → **3** |
| Gouvernance et mesure | ni responsable ni mesure | première mesure isolée | stratégie adoptée, responsable désigné, bilan annuel | objectifs intégrés au schéma directeur et au projet de territoire, rendus aux élus | **2** (bilan de fin 2026, mais aucune stratégie, aucun responsable, rien présenté aux élus) → **4** |

**Quatre axes priorisés** :

| Rang | Axe | Constat de l'annexe 3.4 | Contenu |
|---|---|---|---|
| 1 (a-2) | **Allonger la durée de vie des équipements et acheter de façon responsable** | la fabrication pèse environ 70 % de l'empreinte ; postes tous les quatre ans, téléphones tous les deux ans, achat au prix ; 400 postes et 900 téléphones stockés | passer à six ans pour les postes (un tiers d'achats en moins) et à quatre ans pour les téléphones (moitié moins), renouveler au cas par cas ; critères de garantie, de réparabilité, de reconditionnement et de reprise ; réaffecter les tablettes inutilisées ; réemploi des équipements stockés avant leur enlèvement |
| 2 (a-2) | **Rationaliser les salles informatiques, avec la ville** | 120 serveurs utilisés à 15 %, 40 sans application ; PUE de 2,2 et 2,0 ; environ 20 % de l'empreinte | retirer les serveurs inutiles, virtualiser et consolider, moderniser la climatisation, puis regrouper l'hébergement dans la salle la plus efficace, avec un PUE cible |
| 3 (a-3) | **Évaluer et écoconcevoir les projets et les services numériques** | projet de tournées sans estimation d'empreinte ; services des éditeurs sans aucune donnée | évaluer chaque projet (besoin, empreinte de ses équipements et de ses calculs) avant décision, appliquer les critères du RGESN et exiger des éditeurs leurs données de consommation, pour compléter le bilan : selon l'étude ADEME-Arcep, les centres de données, y compris ceux situés à l'étranger, pèsent près de la moitié de l'empreinte du numérique en France, alors que le bilan de l'agglomération exclut les services hébergés |
| 4 (a-3) | **Rendre les usages plus sobres et former** | 4 millions de pages, 150 imprimantes individuelles ; écogestes sans suite | retirer les imprimantes individuelles au profit des copieurs, impression recto verso par défaut, dématérialisation pertinente ; former les agents et les élus au numérique responsable, comme le prévoit la loi REEN |

**Ordre de priorité** (a-3) : la fabrication domine l'empreinte, ici environ 70 % ; les terminaux restent, selon l'étude ADEME-Arcep, la première source de l'empreinte du numérique, surtout par leur fabrication. L'allongement de la durée de vie passe donc en premier : il est aussi le moins coûteux. Les salles viennent ensuite, car le retrait des serveurs inutiles est un gain rapide ; l'évaluation des projets doit précéder la décision sur les tournées ; la sobriété des usages accompagne le tout.

**Gouvernance et trajectoire** (a-4) : la stratégie est **adoptée par le conseil communautaire** et portée par un(e) vice-président(e). Elle est construite **avec la ville**, elle aussi tenue d'en avoir une et qui partage la direction du numérique et les salles informatiques. Elle est pilotée par un **comité du numérique responsable commun** aux deux collectivités, qui réunit chaque semestre la direction générale, la direction du numérique, Mme PRÉVILLAN, les achats, les directions utilisatrices et des représentants des agents, autour d'un référent désigné à la direction du numérique. Elle est **intégrée au futur schéma directeur** et à l'objectif « réduire l'empreinte environnementale du numérique » de « Castelrive 2032 », et non ajoutée à côté. Trajectoire :
- **2027** : adoption avant la fin de l'année ; retrait des serveurs inutiles ; téléphones conservés quatre ans ; réemploi du stock ; bilan complété des services hébergés ;
- **2028** : critères d'achat et évaluation environnementale des projets inscrits au schéma directeur ;
- **2029** : consolidation des salles informatiques ;
- **2030** : postes conservés six ans et empreinte réduite d'environ 30 % (environ 210 tCO2e contre 300), mesurée chaque année avec la même méthode.

*3.4 b) – Le projet de tournées optimisées et la sobriété*

**Deux arguments en sa faveur** (b-1) : (1) c'est de l'**IT for green** à fort enjeu : 150 tCO2e de gazole évitées chaque année, ordre de grandeur plausible pour 120 000 km de camions, soit la moitié de l'empreinte du numérique ; s'y ajoutent moins de bruit et d'usure des camions ; (2) il **cible un besoin réel** : le remplissage des bacs collectifs des immeubles et des professionnels varie, et les tournées fixes passent devant des bacs à moitié vides.

**Deux limites** (b-1) : (1) l'**empreinte du dispositif n'est pas mesurée**. Il faudrait 2 000 capteurs à pile, près de sept fois le parc actuel de 300 ; leur renouvellement tous les cinq ans produirait environ 400 capteurs et leurs piles à traiter chaque année. S'y ajoutent de nouvelles tablettes, alors que 30 % des tablettes existantes dorment, et un calcul chaque nuit dans le cloud, sans aucune donnée : le bilan net est inconnu, et le gain annoncé vient du vendeur lui-même ; (2) le **besoin n'est pas uniforme** : dans les communes rurales, les tournées changent peu, donc l'optimisation y apporterait peu. À cela s'ajoutent un risque d'effet rebond, 2 000 objets connectés de plus à sécuriser (question 3.3) et la dépendance à une jeune entreprise et à son cloud.

**Recommandation et conditions** (b-2) : recommander le projet **à titre d'expérimentation**, pas les 2 000 capteurs dès 2027 :
- un essai d'un an sur les secteurs à bacs collectifs de la ville-centre, avec une mesure des kilomètres avant et après ;
- un **bilan net** établi avec la même méthode que celui du bureau d'études (fabrication des capteurs et des tablettes, calcul, gazole évité), exigé de la jeune entreprise ;
- la sobriété du dispositif : capteurs seulement là où le remplissage varie ; tournées transmises aux ordinateurs embarqués ou aux tablettes existantes ; calcul hebdomadaire plutôt que quotidien si les gains sont proches ; modèle adapté à la tâche, comme le recommande le thème « algorithmie et intelligence artificielle » du RGESN ;
- des exigences de sécurité et de durée de vie dans le contrat ;
- une généralisation décidée par le comité du numérique responsable au vu du bilan net.

*3.4 c) – Deux indicateurs de suivi*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| (c-1) **Durée de vie moyenne des postes de travail au retrait** | somme des âges des postes retirés dans l'année / nombre de postes retirés | inventaire du parc de la direction du numérique mutualisée (dates d'achat et de retrait) | annuelle | 6 ans en 2030, contre 4 ans en 2026 | environnement |
| (c-2) **Empreinte carbone annuelle du numérique de l'agglomération** | somme des émissions estimées de la fabrication, de l'électricité, des impressions et des autres usages, puis des services hébergés quand les éditeurs fournissent leurs données (tCO2e) | bilan annuel tenu par la chargée de mission avec le bureau d'études (inventaire, relevés d'électricité, données des éditeurs) | annuelle, avec une méthode constante | 210 tCO2e au plus en 2030, contre environ 300 en 2026 (− 30 %), à périmètre comparable | environnement |

**Réponses tolérées**
- Grille de quatre ou cinq niveaux inspirée de CMMI, ou d'autres dimensions (données, compétences, inclusion), si chaque niveau est décrit de façon observable et si l'agglomération y est située à partir des annexes.
- Autres axes pertinents : sobriété des données (stockage, purge), réemploi et dons d'équipements, critères environnementaux dans le choix des éditeurs et des hébergeurs ; ordre différent s'il est justifié.
- Gouvernance portée par le comité de direction ou par l'élu(e) chargé(e) du numérique ; trajectoire découpée autrement.
- Projet rejeté si la justification tient au bilan net inconnu et au besoin non démontré, ou accepté sans expérimentation si la mesure du bilan net est exigée avant la généralisation.
- Autres indicateurs complets : PUE des salles informatiques (énergie totale consommée par la salle / énergie consommée par les équipements informatiques ; cible 1,6 au plus en 2029) ; nombre de pages imprimées par agent ; part des achats de matériels assortis de critères environnementaux ; part des serveurs utilisés ; part des agents formés au numérique responsable (axe social) ; bilan net de l'expérimentation des tournées (gazole évité − empreinte du dispositif).

**Erreurs fréquentes**
- *Sobriété réduite à une économie d'énergie* (`ET-12`) — juste : interroger le besoin (renouvellements, serveurs inutiles, capteurs, impressions).
- *Empreinte réduite à l'électricité ou au PUE* (`ET-38`) — juste : la fabrication représente environ 70 % ; le PUE ne mesure ni la fabrication ni l'origine de l'électricité.
- *Tension entre l'IA et la sobriété ignorée*, ou projet accepté sur la seule foi du gain annoncé (F14 § 8) — juste : bilan net et expérimentation.
- *Calcul d'empreinte tenté* — non attendu : les résultats sont donnés.
- *Grille de maturité « plate »* (F09 § 5) — juste : des niveaux distincts et observables.
- *Durabilité traitée en ajout marginal* (limite du programme) — juste : intégrée au schéma directeur, au projet de territoire et à une gouvernance commune.
- *Indicateurs génériques, sans cible ni source* (`ET-18`, `JUR-A02`) — juste : deux indicateurs complets, avec leur valeur de départ.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Sobriété, Green IT et IT for green, indicateurs, grille de maturité | définitions, PUE, durée de vie, part de la fabrication | F14 § 1 à 4 ; F09 § 5 | notion de cours |
| Loi n° 2021-1485 du 15 novembre 2021 (REEN) | stratégie numérique responsable des collectivités de plus de 50 000 habitants au 01/01/2025, durée de vie, sensibilisation | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | écoconception, interrogation du besoin, thème de l'algorithmie et de l'IA | `rgesn_2024` ; F14 § 2 | version 2 publiée le 17/05/2024 |
| Étude ADEME-Arcep | poids du numérique (4,4 %), part des terminaux (environ la moitié, surtout par leur fabrication) et des centres de données (environ 46 %) dans l'empreinte | `etude_ademe_arcep_numerique` ; F14 § 1 | mise à jour du 17/01/2025 |
| CMMI (toléré pour les niveaux de la grille) | niveaux de maturité | `cmmi_v3` ; F09 § 5 | en vigueur |
