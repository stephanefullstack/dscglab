# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 32

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES PARCOURS (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 11, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mai 2027. La Fondation VERLANDRE est une fondation reconnue d'utilité publique, dont le siège est à Tours. Elle est née en 2019 de la réunion de trois associations de parents créées dans les années 1960 et 1970 en Indre-et-Loire et dans le Loir-et-Cher. Elle accompagne environ 2 400 enfants et adultes en situation de handicap dans 40 établissements et services répartis sur 28 sites : instituts médico-éducatifs et services d'éducation spéciale pour les enfants, foyers d'hébergement et maisons d'accueil spécialisées ouverts jour et nuit, services d'accompagnement à domicile et cinq établissements et services d'aide par le travail (blanchisserie, espaces verts, restauration, conditionnement). La Fondation emploie 1 800 salariés (éducateurs, accompagnants, soignants, moniteurs d'atelier, services généraux et siège). Ses produits ont atteint 125 millions d'euros en 2026, financés pour l'essentiel par l'agence régionale de santé et par les deux départements ; les établissements d'aide par le travail réalisent en outre 12 millions d'euros de chiffre d'affaires. Les organisations, les personnes et les données de ce cas sont fictives.

Le projet stratégique « Horizon 2030 », adopté par le conseil d'administration en janvier 2027, fixe quatre orientations : passer d'une logique de places à une logique de parcours, en coordonnant autour de chaque personne les professionnels, la famille et les partenaires ; garantir la qualité et la sécurité de l'accompagnement ; rendre les métiers plus attractifs en redonnant du temps auprès des personnes ; développer un numérique responsable, accessible et éthique. Le projet de « dossier unique de la personne accompagnée », qui doit remplacer les trois logiciels hérités des associations et les dossiers papier, en est le chantier numérique principal.

Vous êtes responsable du contrôle interne et de la performance de la Fondation VERLANDRE depuis 2025, rattaché à la directrice générale, Mme Nathalie BRÉCHEVAL. Elle vous demande trois travaux : éclairer la stratégie du système d'information et préparer le projet de dossier unique (dossier 1) ; organiser et exploiter les données des parcours (dossier 2) ; sécuriser l'accès aux données, préparer la Fondation à une crise cyber et rendre son numérique plus responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de la Fondation VERLANDRE et chiffres clés

La Fondation VERLANDRE est une fondation reconnue d'utilité publique dont le siège est à Tours. Elle est née en 2019 de la réunion de trois associations de parents : l'association GERVELLE, créée en 1962 à Tours, l'association MIRANDELLE, créée en 1968 dans le Loir-et-Cher, et l'association LUMERANDE, créée en 1974 dans le sud de l'Indre-et-Loire. Son conseil d'administration, présidé par M. Henri LABASTROU, réunit un collège des familles et des personnalités qualifiées. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Les établissements et services en 2026**

| Pôle | Établissements et services | Nombre | Personnes accompagnées |
|---|---|---|---|
| Enfance | instituts médico-éducatifs, services d'éducation spéciale | 12 | 700 enfants et adolescents |
| Hébergement | foyers d'hébergement, maisons d'accueil spécialisées, ouverts jour et nuit | 14 | 600 adultes hébergés |
| Domicile | services d'accompagnement à domicile | 9 | 550 adultes accompagnés à domicile |
| Travail | établissements et services d'aide par le travail (blanchisserie, espaces verts, restauration, conditionnement) | 5 | 550 travailleurs handicapés |
| **Total** | 28 sites, en Indre-et-Loire et dans le Loir-et-Cher | **40** | **2 400** |

Environ 900 personnes sont inscrites sur les listes d'attente des établissements et services.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Produits | 125 M€ : environ 110 M€ de financements publics (agence régionale de santé et deux départements), 12 M€ de chiffre d'affaires des établissements d'aide par le travail, 3 M€ de dons, legs et autres produits |
| Effectif | 1 800 salariés : environ 1 100 professionnels de l'accompagnement éducatif et social (dont l'encadrement et les secrétariats des établissements), beaucoup en horaires alternés, de jour, de nuit et le week-end ; 250 soignants et paramédicaux ; 150 moniteurs et encadrants d'atelier ; 200 salariés des services généraux (cuisine, entretien, transport) ; 100 salariés au siège, dont une direction des systèmes d'information de 14 personnes |
| Dépenses du système d'information | environ 3 M€ (2,4 % des produits) |
| Projet stratégique « Horizon 2030 » (janvier 2027) | logique de parcours coordonnés autour de chaque personne ; qualité et sécurité de l'accompagnement ; attractivité des métiers et temps redonné auprès des personnes ; numérique responsable, accessible et éthique ; chantier numérique principal : le dossier unique de la personne accompagnée |

**Le système d'information en quelques lignes**

Chaque association a apporté son logiciel de dossier de la personne accompagnée, d'éditeurs et de versions différents : celui de l'association GERVELLE est utilisé par 18 de ses 20 établissements et services, celui de l'association MIRANDELLE par 9 de ses 13 établissements et services, celui de l'association LUMERANDE par 5 de ses 7 établissements et services ; les huit autres établissements et services tiennent des dossiers papier. La Fondation utilise en outre un progiciel de gestion de la production et de la facturation des établissements d'aide par le travail, un progiciel de paie et de gestion des ressources humaines, un logiciel de planning des équipes, un progiciel comptable, ainsi qu'une messagerie et une suite bureautique en ligne. Les serveurs sont installés dans une salle du siège ; un réseau relie les sites. Le parc compte environ 1 400 ordinateurs, dont beaucoup sont partagés dans les unités, et 600 tablettes et smartphones.

**Organigramme simplifié (mai 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil d'administration | président | M. Henri LABASTROU |
| Direction générale | directrice générale | Mme Nathalie BRÉCHEVAL |
| Siège, rattaché à la directrice générale | directeur administratif et financier | M. Pascal DURANTEL |
| Siège, rattaché au directeur administratif et financier | directeur des systèmes d'information (direction de 14 personnes) | M. Laurent TRÉVENEC |
| Siège, rattachée à la directrice générale | directrice des ressources humaines | Mme Valérie OSMONDE |
| Siège, rattaché à la directrice générale | responsable du contrôle interne et de la performance | vous |
| Siège, rattachée à la directrice générale | déléguée à la protection des données | Mme Agnès PELLEGRAIN |
| Pôles, rattachés à la directrice générale | directrice du pôle Enfance | Mme Corinne LÉVRAUD |
| | directeur du pôle Hébergement | M. Stéphane MARCILHAC |
| | directrice du pôle Domicile | Mme Élodie FARGEAS |
| | directeur du pôle Travail | M. Rémi CAZENOVE |
| Établissements, rattachés au directeur de leur pôle | directeurs d'établissement | — |

Le comité de direction réunit chaque mois la directrice générale, le directeur administratif et financier, la directrice des ressources humaines et les quatre directeurs de pôle.

### ANNEXE 2.1 – Les données des personnes accompagnées aujourd'hui (note de Mme Hélène QUÉRANDEAU, responsable de l'admission et des parcours au siège, et témoignages recueillis en avril 2027)

**A. Une même personne, plusieurs dossiers**

Chacun des trois logiciels hérités des associations attribue son propre numéro à la personne accompagnée :

| Logiciel de l'ancienne association | Établissements et services équipés | Numéro attribué à la personne | Dossiers « actifs » en 2026 (personne accompagnée dans l'année ou dossier jamais clôturé) |
|---|---|---|---|
| GERVELLE | 18 | numéro chronologique attribué à la création du dossier | 1 300 |
| MIRANDELLE | 9 | trois premières lettres du nom suivies de la date de naissance | 600 |
| LUMERANDE | 5 | code de l'établissement suivi d'un numéro d'ordre : il change quand la personne change d'établissement | 400 |
| **Total** | **32** | | **2 300** |

Les 32 établissements et services équipés ont accompagné environ 2 000 personnes en 2026 ; les 8 autres, qui tiennent des dossiers papier, en ont accompagné environ 400. Les 2 300 dossiers « actifs » comprennent donc environ 300 dossiers en trop : environ 200 personnes ont deux dossiers actifs, ouverts sous deux numéros lors d'un changement d'établissement, sous un nom d'usage et un nom de naissance, ou avec une faute de frappe ; environ 100 dossiers de personnes parties avant 2026 n'ont jamais été clôturés. La plupart des personnes ont un numéro de dossier attribué par la maison départementale des personnes handicapées qui a décidé leur orientation ; il n'est saisi que dans le logiciel de l'ancienne association GERVELLE, et il change quand la personne déménage dans l'autre département.

**B. Des mots qui n'ont pas le même sens**

| Notion | Ancienne association GERVELLE | Ancienne association MIRANDELLE | Ancienne association LUMERANDE |
|---|---|---|---|
| « Place occupée » | une place est occupée dès qu'une personne y est admise, même absente (hospitalisation, retour en famille, vacances) | une place est occupée les seuls jours où la personne est présente | une place est occupée si la personne est présente ou absente depuis moins de quinze jours |
| « Personne en attente » | toute personne dont la famille a déposé une demande, même sans décision d'orientation | toute personne reçue en entretien de préadmission | toute personne qui a une décision d'orientation vers l'établissement |
| « Sortie » | départ de la personne de la Fondation | tout départ d'un établissement, y compris vers un autre établissement de la Fondation | tout départ d'un établissement, y compris vers un autre établissement de la Fondation |

Aucune personne n'est retirée d'une liste d'attente quand elle est admise ailleurs, sauf si sa famille le signale.

**C. Les demandes d'admission et les états d'activité**

- Les décisions d'orientation et les demandes d'admission arrivent des deux maisons départementales des personnes handicapées et des familles par courrier, par courriel et sous forme de tableurs, dans des présentations différentes. Chaque établissement tient sa propre liste d'attente dans un tableur ou dans un cahier ; personne ne voit l'ensemble des listes.
- La maison départementale d'Indre-et-Loire propose depuis 2026 un service en ligne de suivi des orientations, doté d'une interface de programmation (API) documentée ; celle du Loir-et-Cher accepte le dépôt de fichiers dans un format ouvert sur un espace d'échange sécurisé. Toutes deux appliquent le référentiel général d'interopérabilité (annexe 2.5) et souhaitent savoir, chaque mois, quelles personnes orientées ont été admises.
- Les deux départements et l'agence régionale de santé demandent des états d'activité (journées, personnes accompagnées, admissions, sorties), chacun selon son propre modèle de tableur. Les secrétariats des établissements les remplissent à la main à partir des logiciels et des dossiers papier ; le siège les relit et les corrige avant l'envoi.

**D. Témoignages**

- **Mme Hélène QUÉRANDEAU, responsable de l'admission et des parcours** : « Pour répondre à une famille qui demande où en est sa demande, j'appelle cinq établissements. En mars, j'ai rapproché à la main toutes les listes d'attente : trois semaines de travail (annexe 2.2). Le dossier unique doit devenir la référence, mais si l'on y reprend les doublons, on les aura pour vingt ans. »
- **M. Fabrice ROSPARIN, directeur d'un institut médico-éducatif** : « Un jeune qui part dans un foyer de l'ancienne association MIRANDELLE compte comme une sortie chez nous et comme une admission chez eux ; au siège, il disparaît des statistiques de la Fondation. Et personne ne sait me dire ce qu'est une place occupée. »
- **Mme Gaëlle TRÉMOLIÈRE, secrétaire d'un foyer d'hébergement** : « Chaque mois, je remplis deux tableurs différents pour les deux départements, avec les mêmes chiffres présentés autrement. Je passe deux jours à recopier ce qui est déjà dans le logiciel. »
- **Mme Agnès PELLEGRAIN, déléguée à la protection des données** : « Les listes d'attente circulent par courriel dans des tableurs qui contiennent les diagnostics des enfants. Et personne ne supprime jamais rien. »

### ANNEXE 2.2 – Les listes d'attente et l'occupation en 2026 (relevé établi par Mme Hélène QUÉRANDEAU, mars 2027)

**A. Occupation et listes d'attente par pôle (sources : logiciels et listes des établissements)**

| Pôle | Places | Personnes accompagnées dans l'année | Taux d'occupation | Inscriptions en liste d'attente au 31/12/2026 | Délai moyen d'attente des personnes admises en 2026 | Admissions en 2026 | Délai moyen entre une sortie et l'admission suivante |
|---|---|---|---|---|---|---|---|
| Enfance | 650 | 700 | 96 % | 350 | 2 ans | 90 | 45 jours |
| Hébergement | 580 | 600 | 95 % | 300 | 3 ans | 40 | 60 jours |
| Domicile | 500 | 550 | 90 % | 150 | 8 mois | 120 | 30 jours |
| Travail | 520 | 550 | 97 % | 100 | 18 mois | 60 | 20 jours |
| **Total** | **2 250** | **2 400** | — | **900** | — | **310** | — |

Le nombre de personnes accompagnées dans l'année dépasse le nombre de places, parce qu'une place libérée en cours d'année est attribuée à une autre personne. Les taux d'occupation sont calculés par chaque établissement selon la définition de son ancienne association (annexe 2.1 B), puis consolidés par le siège. Les admissions comprennent les changements d'établissement à l'intérieur de la Fondation. Les délais d'attente ne portent que sur les personnes admises en 2026.

**B. Le rapprochement des listes d'attente (mars 2027)**

Mme QUÉRANDEAU a rapproché à la main les 900 inscriptions, à partir du nom, du prénom et de la date de naissance :

| Constat | Nombre |
|---|---|
| Personnes inscrites sur une seule liste | 400 |
| Personnes inscrites sur deux listes | 150 |
| Personnes inscrites sur quatre listes | 50 |
| **Personnes distinctes** | **600** |
| dont personnes déjà accompagnées par la Fondation, qui attendent une autre solution | 150 |
| dont, parmi elles, jeunes adultes de plus de 20 ans maintenus dans un institut médico-éducatif faute de place en foyer ou en établissement d'aide par le travail | 100 |
| dont personnes non accompagnées par la Fondation qui n'ont pas confirmé leur demande depuis plus de douze mois | 100 |

Sur dix familles de ce dernier groupe jointes par téléphone, six ont indiqué que leur enfant ou leur proche avait été admis ailleurs ou avait déménagé. Certaines personnes n'ont pas pu être rapprochées avec certitude (orthographe du nom, date de naissance manquante).

**C. Des valeurs qui diffèrent selon la source**

| Donnée de 2026 | Source | Valeur | Autre source | Valeur |
|---|---|---|---|---|
| Taux d'occupation du pôle Hébergement | tableau de bord mensuel du siège | 95 % | état d'activité transmis au département, en journées de présence | 91 % |
| Personnes en attente d'une place dans le pôle Enfance | listes des établissements | 350 | relevés des deux maisons départementales (orientations vers la Fondation non suivies d'admission) | 280 |
| Sorties | total des trois logiciels et des dossiers papier | 280 | direction générale (personnes qui ont quitté la Fondation) | 220 |

Dans le pôle Hébergement, les absences des personnes (hospitalisations, retours en famille, vacances) représentent environ 4 % des journées.

**D. La demande du conseil d'administration**

M. Henri LABASTROU, président : « Le rapport annuel annonce 900 personnes en attente. Les familles du conseil n'y croient pas, et l'agence régionale de santé nous demande des chiffres sûrs. Je veux savoir combien de personnes attendent vraiment une place, et depuis combien de temps. »

### ANNEXE 2.3 – Le tableau de bord actuel (extrait et attentes recueillies en avril 2027)

**A. Le tableau de bord mensuel**

Depuis 2020, Mme Sophie VALDRIAC, contrôleuse de gestion rattachée au directeur administratif et financier, établit chaque mois un tableau de bord de 30 indicateurs : 12 d'activité, 10 de ressources humaines et 8 de finances. Elle y consacre cinq jours par mois, à partir d'extractions des trois logiciels, des tableurs envoyés par les huit établissements à dossiers papier, du progiciel de paie et du progiciel comptable. Le tableau, un fichier de six pages, est envoyé vers le 25 du mois suivant, sous la même forme, à la directrice générale, aux quatre directeurs de pôle et aux 40 directeurs d'établissement. Une enquête d'avril 2027 indique que 10 des 44 directeurs le lisent régulièrement. Le conseil d'administration n'en reçoit aucun extrait.

Extrait du tableau de mars 2027 (ensemble de la Fondation) :

| Indicateur | Mars 2027 | Février 2027 |
|---|---|---|
| Journées réalisées | 54 000 | 49 000 |
| Taux d'occupation | 95 % | 94 % |
| Personnes en liste d'attente | 910 | 900 |
| Repas servis | 98 000 | 90 000 |
| Taux d'absentéisme des salariés | 9 % | 10 % |
| Heures d'intérim | 6 000 | 5 500 |
| Litres de carburant des véhicules | 15 000 | 14 000 |
| Charges de personnel cumulées depuis janvier (k€) | 21 000 | 14 000 |

Aucun indicateur n'a de cible ; aucun commentaire n'accompagne les chiffres. Les définitions sont celles de chaque ancienne association.

**B. Les attentes**

- **Mme Nathalie BRÉCHEVAL, directrice générale** : « "Horizon 2030" nous demande de passer des places aux parcours. Ce tableau compte des repas et du carburant ; il ne me dit pas si les parcours s'améliorent. »
- **M. Stéphane MARCILHAC, directeur du pôle Hébergement** : « Je veux comparer mes quatorze établissements, voir tout de suite où une place se libère et quelles situations s'enlisent. Quatre ou cinq chiffres, avec une alerte, me suffisent. »
- **Mme Corinne LÉVRAUD, directrice du pôle Enfance** : « Cent jeunes adultes restent chez nous faute de place ailleurs, et aucun tableau ne le montre. Seule une enquête de mars 2027 m'a appris qu'environ 70 % des projets personnalisés avaient été révisés depuis moins d'un an. »
- **Mme Valérie OSMONDE, directrice des ressources humaines** : « Le tableau montre l'absentéisme et l'intérim, mais pas les postes vacants, qui atteignaient 7 % des postes d'accompagnement fin mars. C'est pourtant ce qui fragilise l'accompagnement. »
- **M. Henri LABASTROU, président du conseil d'administration** : « Le conseil voudrait, chaque trimestre, quelques chiffres sûrs et compris de tous. »

### ANNEXE 2.4 – Les anciens logiciels et leurs données (note de M. Laurent TRÉVENEC, directeur des systèmes d'information, avril 2027)

**A. Ce que contiennent les anciens logiciels**

| Logiciel de l'ancienne association | Dossiers actifs | Dossiers de personnes sorties | dont dernière sortie de la Fondation il y a plus de 20 ans | Coût actuel (k€ par mois) |
|---|---|---|---|---|
| GERVELLE | 1 300 | 5 000 | 1 000 | 8 |
| MIRANDELLE | 600 | 2 000 | 500 | 7 |
| LUMERANDE | 400 | 1 000 | — | 5 |
| **Total** | **2 300** | **8 000** | **1 500** | **20** |

- Les logiciels contiennent en outre environ 150 000 pièces numérisées (comptes rendus, bilans, décisions d'orientation, courriers), dans des formats propres à chaque éditeur, et environ 2 500 demandes d'admission qui n'ont pas abouti, dont 2 000 sans aucun contact avec la famille depuis plus de deux ans.
- Les extractions sont fournies par les éditeurs sous forme de fichiers de tableur ; les pièces numérisées sont livrées en vrac, classées sous le numéro attribué par chaque logiciel.
- Les huit établissements à dossiers papier conservent environ 400 dossiers actifs et 3 000 dossiers de personnes sorties, dont 1 000 dont la dernière sortie remonte à plus de 20 ans, dans des armoires.
- Les trois contrats sont conclus par année civile ; chacun se renouvelle tacitement, sauf résiliation trois mois avant son échéance.

Les données du dossier unique seront hébergées dans l'Union européenne. L'offre de l'éditeur retenu pour le dossier unique, ORLINÈVE, satisfait aux exigences légales applicables à l'hébergement des données de santé ; ce point n'est pas à analyser.

**B. Trois options pour les données des anciens logiciels**

| | Option 1 : tout reprendre | Option 2 : reprendre les dossiers actifs, archiver les autres | Option 3 : garder les anciens logiciels en consultation |
|---|---|---|---|
| Contenu | reprise dans le dossier unique de tous les dossiers, actifs et sortis, et de toutes les pièces numérisées | reprise des seuls dossiers actifs, après dédoublonnage ; export des dossiers des personnes sorties et de leurs pièces dans des formats ouverts, versés dans un service d'archivage électronique distinct du dossier unique | reprise des seuls dossiers actifs ; logiciels des anciennes associations GERVELLE et MIRANDELLE conservés en lecture seule ; l'éditeur du logiciel de l'ancienne association LUMERANDE refuse ce mode et cessera de maintenir sa version fin 2028 |
| Coût | 150 k€ de reprise supplémentaire, une seule fois | 60 k€ de mise en place, puis 12 k€ par an | 4 k€ par mois pour le logiciel de l'ancienne association GERVELLE et 3 k€ par mois pour celui de l'ancienne association MIRANDELLE, sans limite de durée |
| Accès | tous les utilisateurs du dossier unique, selon leurs droits habituels | consultation sur demande motivée par l'équipe de l'admission et des parcours, chaque accès étant enregistré | comptes actuels des anciens logiciels |
| Avis recueilli | équipe projet : « Les doublons et les dossiers anciens alourdiront le contrôle de la reprise. » | déléguée à la protection des données : « C'est l'occasion de supprimer ce qui doit l'être. » | directeurs d'établissement : « C'est la solution la plus simple ; on garde nos habitudes. » |

La directrice générale demande de comparer les coûts sur cinq ans.

### ANNEXE 2.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Les données sont collectées pour des finalités déterminées et ne sont pas traitées ultérieurement de manière incompatible avec elles ; elles sont adéquates, pertinentes et limitées à ce qui est nécessaire (minimisation) ; elles sont exactes et tenues à jour ; elles sont conservées sous une forme permettant l'identification des personnes pendant une durée n'excédant pas celle nécessaire aux finalités (limitation de la conservation) ; elles sont protégées contre l'accès non autorisé, la perte et la destruction (intégrité et confidentialité). Le responsable du traitement doit pouvoir démontrer le respect de ces principes. Une personne peut demander communication des données qui la concernent. Les données relatives à la santé font l'objet d'une protection renforcée. | Applicable depuis le 25/05/2018. Une proposition européenne de simplification (« omnibus numérique », 19/11/2025) modifiant ce règlement est en discussion et n'est pas applicable. |
| Loi n° 78-17 du 6 janvier 1978 relative à l'informatique, aux fichiers et aux libertés | Complète le RGPD en droit français. | En vigueur, modifiée en 2018 |
| Référentiel général d'interopérabilité (RGI), version 2.0 (DINUM) | Cadre de recommandations qui référence les normes et standards, dont des formats ouverts, à appliquer par les administrations, dont les départements, pour rendre leurs systèmes d'information interopérables. | En vigueur depuis l'arrêté du 20/04/2016 |
| DAMA-DMBOK (DAMA International), 2e édition | Référentiel de bonnes pratiques de gestion des données, organisé en onze domaines autour de la gouvernance des données, dont les données de référence, la qualité des données, les métadonnées, l'intégration et l'interopérabilité. | 2e édition (2017), révisée en 2024 |

Durées de conservation retenues par la Fondation, sur proposition de la déléguée à la protection des données (hypothèses de l'énoncé, à appliquer sans analyse juridique) :
- dossier de la personne accompagnée : pendant tout l'accompagnement, puis 20 ans après la dernière sortie de la Fondation ; il est ensuite détruit ;
- demande d'admission qui n'a pas abouti : 2 ans après le dernier contact avec la famille ; elle est ensuite détruite.

Il n'est demandé aucune analyse juridique.

### Travail à faire

Le dossier unique de la personne accompagnée doit remplacer les trois logiciels hérités des associations et les dossiers papier. Mme BRÉCHEVAL vous demande d'en faire la source de référence des données des personnes, d'organiser leurs échanges avec les maisons départementales et les financeurs, d'exploiter les données des listes d'attente pour répondre au conseil d'administration, de refondre le tableau de bord pour piloter les parcours et de décider du sort des données des anciens logiciels. Vous mobiliserez pour cela les annexes 1.1 à 2.5 ainsi que vos connaissances professionnelles.

**2.1 – Le référentiel des personnes accompagnées et les échanges avec les partenaires (5 points)**

a) Proposez, en vous appuyant sur l'annexe 2.1, l'organisation des données qui fera du dossier unique la source de référence des données des personnes accompagnées : le référentiel des personnes, l'identifiant de la personne et trois règles de dédoublonnage. Aucun modèle des données (entités, associations, cardinalités) n'est attendu.

b) Après avoir défini un dictionnaire de données, rédigez-en un extrait pour les trois notions de l'annexe 2.1 B (« place occupée », « personne en attente », « sortie ») : pour chacune, sa définition commune, sa règle de calcul ou d'enregistrement, son propriétaire et une règle de qualité.

c) Après avoir défini l'interopérabilité, proposez les solutions d'échange de la Fondation avec les deux maisons départementales des personnes handicapées, d'une part, et avec les départements et l'agence régionale de santé, d'autre part, en précisant pour chacun l'outil d'échange retenu (interface de programmation, formats ouverts, fichiers structurés) et deux conditions organisationnelles. Le détail technique des échanges n'est pas attendu.

**2.2 – Les listes d'attente et l'occupation (3,5 points)**

a) Distinguez l'analyse descriptive et l'analyse exploratoire des données, puis justifiez la méthode, ou la combinaison de méthodes, que vous retiendrez pour exploiter les données de l'annexe 2.2.

b) Formulez trois constats argumentés tirés de l'annexe 2.2, en précisant pour chacun une précaution de lecture (doublons, définitions, sources ou population mesurée).

c) Répondez à la question du président du conseil d'administration, de tête et en chiffres ronds, puis proposez deux représentations visuelles adaptées pour présenter ces résultats au conseil d'administration, en justifiant chacune. Aucun calcul statistique n'est attendu.

**2.3 – Le tableau de bord des parcours (2,5 points)**

a) Critiquez le tableau de bord actuel décrit dans l'annexe 2.3 A, en quatre arguments.

b) Proposez le tableau de bord des parcours destiné aux directeurs de pôle : ses destinataires, sa fréquence et quatre indicateurs, respectivement d'activité, de qualité de l'accompagnement, de ressources et de risque, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

c) Indiquez comment ce tableau de bord sera revu et amélioré dans le temps.

**2.4 – Le cycle de vie des données des anciens logiciels (2 points)**

a) Présentez les étapes du cycle de vie des données des personnes accompagnées, en les appliquant au cas de la Fondation et aux durées de conservation de l'annexe 2.5.

b) Comparez les trois options de l'annexe 2.4 B au regard des principes du RGPD rappelés dans l'annexe 2.5, du coût et des risques, puis recommandez l'une d'elles en la justifiant. Le choix de l'hébergement n'est pas à traiter.
