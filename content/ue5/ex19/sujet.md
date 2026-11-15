# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 19

**DOSSIER 1 – ORGANISER ET VALORISER LES DONNÉES DES SUPPORTERS (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 7, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en juin 2027. MONTALBRET XV est le club de rugby professionnel de l'agglomération de Montalbret, ville fictive du Sud-Ouest de 180 000 habitants. Il est exploité par une société anonyme sportive professionnelle détenue à 80 % par la holding familiale de son président, M. Damien ROQUESSOL, et à 20 % par l'association MONTALBRET XV, qui gère la formation et les équipes amateurs. Le club dispute la deuxième division professionnelle et vise l'accession à l'élite d'ici 2030. Il emploie 150 salariés permanents, dont 48 joueurs et entraîneurs, et fait appel les jours de match à environ 400 intervenants extérieurs (accueil, sécurité, restauration). Il joue dans un stade de 16 000 places appartenant à la communauté d'agglomération et compte 7 000 abonnés. Son chiffre d'affaires de la saison 2025-2026 s'élève à 28 millions d'euros ; 0,9 million d'euros est consacré au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « MONTALBRET 2030 », adopté par le conseil d'administration en janvier 2027, fixe trois priorités : mieux connaître les supporters et les partenaires pour développer les recettes hors droits sportifs ; structurer la gouvernance du numérique du club et étudier de nouvelles formes de relation avec les supporters ; fiabiliser l'organisation des jours de match dans un stade modernisé et réduire son empreinte environnementale. La directrice générale, Mme Inès LAFERRADE, en rend compte chaque trimestre au conseil d'administration.

Vous êtes responsable administratif et financier de MONTALBRET XV depuis 2025. Mme LAFERRADE vous a aussi confié la responsabilité du système d'information du club, et elle vous demande trois travaux : organiser et valoriser les données des supporters (dossier 1) ; gouverner le numérique du club et évaluer le projet de jetons de supporters (dossier 2) ; maîtriser les risques des jours de match et l'empreinte du stade connecté (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de MONTALBRET XV et chiffres clés

MONTALBRET XV est une société anonyme sportive professionnelle qui exploite le club de rugby professionnel de l'agglomération de Montalbret, ville fictive du Sud-Ouest de 180 000 habitants. Elle est détenue à 80 % par la holding familiale de son président et à 20 % par l'association MONTALBRET XV, qui gère la formation et les équipes amateurs. La saison sportive court de juillet à juin : la saison 2025-2026 est la dernière saison close, la saison 2026-2027 est en cours de clôture. Le club dispute la deuxième division professionnelle et vise l'accession à l'élite d'ici 2030.

**Chiffres clés de la saison 2025-2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires | 28 M€ : partenariats et publicité 11 M€ ; billetterie et abonnements 6 M€ ; droits audiovisuels et dotations 5 M€ ; hospitalités (loges, salons) 4 M€ ; boutique et licences 2 M€ |
| Matchs à domicile | 15 par saison, environ 12 000 spectateurs en moyenne |
| Effectif | 150 salariés permanents, dont 48 joueurs et entraîneurs ; environ 400 intervenants extérieurs les jours de match (accueil, sécurité, restauration), fournis par des prestataires |
| Stade | 16 000 places, propriété de la communauté d'agglomération, mis à la disposition du club ; modernisation en cours (écran géant, éclairage, réseau sans fil pour le public, contrôle d'accès par billet dématérialisé) |
| Supporters et clients | 7 000 abonnés ; environ 120 000 contacts dans les fichiers du club (billetterie, boutique en ligne, application mobile, lettre d'information) ; 250 entreprises partenaires |
| Budget du système d'information | 0,9 M€ (environ 3 % du chiffre d'affaires) |
| Plan « MONTALBRET 2030 » (adopté en janvier 2027) | mieux connaître les supporters et les partenaires pour développer les recettes hors droits sportifs ; structurer la gouvernance du numérique du club et étudier de nouvelles formes de relation avec les supporters ; fiabiliser l'organisation des jours de match dans un stade modernisé et réduire son empreinte environnementale |

**Organigramme simplifié (juin 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil d'administration | représentants de la holding familiale et de l'association MONTALBRET XV ; se réunit chaque trimestre | — |
| Présidence | président du conseil d'administration | M. Damien ROQUESSOL |
| Direction générale | directrice générale, qui porte le plan « MONTALBRET 2030 » | Mme Inès LAFERRADE |
| Rattaché à la directrice générale | directeur sportif (équipe professionnelle, staff technique et médical, lien avec le centre de formation de l'association) | M. Xavier TOURNEBIAU |
| Rattaché à la directrice générale | directeur commercial et des partenariats (partenaires, hospitalités, loges et salons) | M. Cédric BARRALOU |
| Rattachée à la directrice générale | responsable du pôle marketing et numérique (communication, lettre d'information, réseaux sociaux, application mobile, boutique en ligne) | Mme Léa SOUBIRAC |
| Rattachée à la directrice générale | responsable de la billetterie (abonnements, billets, accueil du public au guichet) | Mme Nathalie ARRIBEUX |
| Rattaché(e) à la directrice générale | responsable administratif et financier (comptabilité, contrôle de gestion, ressources humaines, achats, juridique, système d'information) | vous |
| Rattaché au responsable administratif et financier | responsable informatique | M. Bastien PEYRASTRE |
| Rattaché à la directrice générale | responsable du stade et de la sécurité (exploitation du stade, organisation des jours de match, relations avec les prestataires d'accueil et de sécurité) | M. Franck DOUMERGAT |

### ANNEXE 1.2 – Les applications qui gèrent les supporters (note de M. Bastien PEYRASTRE, responsable informatique, avril 2027)

**A. Les applications**

| Application | Utilisateur principal | Données sur les supporters | Identifiant de la personne |
|---|---|---|---|
| Logiciel de billetterie et d'abonnements, en mode SaaS | billetterie | identité, coordonnées, date de naissance, abonnements (saison, formule, tribune, place), billets achetés (match, tribune, prix, canal de vente) | numéro de client attribué par le logiciel |
| Boutique en ligne | pôle marketing et numérique | identité, adresse de livraison, commandes, montants | adresse électronique |
| Application mobile du club, développée et hébergée par une agence de communication | pôle marketing et numérique | compte (pseudonyme, adresse électronique), articles lus, vidéos vues, participation aux jeux-concours | identifiant de compte de l'application |
| Outil d'envoi de la lettre d'information | pôle marketing et numérique | adresse électronique, prénom, ouvertures et clics | adresse électronique |
| Fichier des partenaires et des loges, tenu sur un tableur | direction commerciale et des partenariats | 250 entreprises partenaires, 1 500 contacts dans ces entreprises, invités de chaque loge et de chaque salon, match par match | raison sociale de l'entreprise, nom de l'invité |
| Contrôle d'accès du stade, exploité par un prestataire | responsable du stade et de la sécurité | aucune fiche de personne : liste des billets et des cartes d'abonnement valides pour un match, heure de passage de chaque billet ou carte à l'entrée | numéro de billet ou de carte d'abonnement |

**B. Les échanges entre applications**
- Le seul échange automatisé est une interface de programmation (API) qui transmet, avant chaque match, la liste des billets et des cartes d'abonnement valides du logiciel de billetterie au contrôle d'accès. Les passages enregistrés à l'entrée sont exportés par le prestataire, le lendemain du match, dans un fichier que la billetterie copie dans un tableur.
- Chaque mois, le pôle marketing exporte de la billetterie un fichier des acheteurs et l'importe dans l'outil de la lettre d'information ; il fait de même chaque trimestre pour les clients de la boutique en ligne.
- Dans l'application mobile, l'achat et l'affichage d'un billet ouvrent les pages du site de la billetterie, où le supporter saisit son numéro de client ; l'application ne conserve ni ce numéro ni les achats, et aucune donnée n'est échangée entre les deux applications. Les données d'usage de l'application restent chez l'agence de communication, qui facture chaque extraction.
- Avant chaque match, les invitations des loges et des salons (environ 900 invités par match) sont ressaisies à la main dans la billetterie à partir des listes que les partenaires envoient par courriel.
- Le prestataire de restauration du stade remet en fin de saison un relevé des paiements effectués avec la carte d'abonnement rechargeable, utilisée par environ un abonné sur trois.

**C. Constats sur les données (profilage réalisé en mars 2027)**

| Application | Fiches de personnes (milliers) | Adresse électronique absente ou invalide | Fiches incomplètes (code postal ou date de naissance manquants) | Consentement à recevoir les offres des partenaires du club |
|---|---|---|---|---|
| Billetterie et abonnements | 50 | 10 % | 20 % | jamais demandé |
| Boutique en ligne | 25 | 5 % | 30 % | case à cocher depuis 2024 ; texte et date conservés pour 8 000 fiches |
| Application mobile | 20 | 15 % | 60 % | jamais demandé |
| Lettre d'information | 25 | 20 % | 70 % | case unique « offres du club et de ses partenaires », sans date, pour 15 000 fiches ; 10 000 fiches importées en 2022 d'un ancien fichier, d'origine inconnue |
| **Ensemble** | **120** | | | |

Autres constats :
- le rapprochement des quatre fichiers sur un échantillon (nom, prénom, date de naissance, adresse électronique) conduit à estimer à 72 000 le nombre de personnes distinctes derrière les 120 000 fiches : environ 40 % des fiches font double emploi ; un abonné figure en moyenne dans trois applications, sous des orthographes et des adresses différentes ;
- la « catégorie de supporter » de la billetterie est un champ libre : on y trouve « VIP », « partenaire », « invité », « famille », « ancien joueur » ou rien ; l'adresse postale est saisie dans un seul champ ;
- aucune application ne supprime les fiches : la billetterie conserve toutes celles qui ont été créées depuis 2012, y compris celles de personnes qui n'ont rien acheté depuis dix ans ;
- le registre des traitements, établi en 2019, n'a pas été mis à jour depuis ; il ne mentionne ni l'application mobile ni la boutique en ligne. Le club n'a pas désigné de délégué à la protection des données.

**D. Témoignage de M. PEYRASTRE**

« Chaque application a sa propre fiche du supporter, et personne n'est chargé de dire laquelle est la bonne. Quand un abonné change d'adresse électronique, il doit le faire quatre fois. L'éditeur de la billetterie propose une API pour la plupart de ses données ; nous n'utilisons que celle du contrôle d'accès. »

### ANNEXE 1.3 – Règles de gestion de la billetterie et des abonnements (extrait du cahier des charges du futur référentiel « supporters », mai 2027)

Le futur référentiel « supporters » conservera, pour chaque personne, une fiche unique, à laquelle seront rattachés ses abonnements, ses billets et ses présences au stade. Règles de gestion validées par la billetterie et par le pôle marketing et numérique :
- RG1 – Un supporter est identifié par un numéro de supporter attribué par le référentiel (ex. S0041207) ; on conserve son nom, son prénom, sa date de naissance, son adresse électronique, son téléphone, son code postal, la date de son consentement à recevoir les offres du club et la date de son consentement à recevoir les offres des partenaires (vides en l'absence de consentement).
- RG2 – Une saison est identifiée par un code (ex. 2027-2028) ; on conserve sa date de début et sa date de fin.
- RG3 – Une tribune est identifiée par un code (OUEST, EST, NORD, SUD) ; on conserve son libellé et son nombre de places.
- RG4 – Un abonnement est identifié par un numéro ; on conserve la formule (plein tarif, tarif réduit, jeune, famille), le prix payé et la date de souscription. Un abonnement est nominatif : il est souscrit par un et un seul supporter, pour une et une seule saison, dans une et une seule tribune. Un supporter peut avoir souscrit plusieurs abonnements au fil des saisons, ou aucun ; une saison et une tribune peuvent n'avoir encore aucun abonnement.
- RG5 – Un match est identifié par un numéro ; on conserve sa date, son heure de coup d'envoi et le nom de l'adversaire. Un match appartient à une et une seule saison ; le calendrier est enregistré à l'ouverture de la campagne d'abonnement, si bien que toute saison comporte au moins un match.
- RG6 – Un billet est identifié par un numéro ; on conserve le tarif appliqué, le prix payé, la date d'achat et le canal de vente (guichet, site internet, application mobile). Un billet est nominatif : il est acheté par un et un seul supporter, pour un et un seul match, dans une et une seule tribune. Un supporter peut n'avoir acheté aucun billet ; un match ou une tribune peut n'avoir donné lieu à aucun billet vendu.
- RG7 – Pour chaque abonnement et chaque match, le référentiel enregistre la présence de l'abonné au stade et son heure de passage à l'entrée, transmises par le contrôle d'accès. Un abonnement peut n'avoir donné lieu à aucune présence ; un match peut n'avoir enregistré aucune présence d'abonné (match à huis clos).
- RG8 – Une fiche de supporter sans abonnement, sans achat de billet ni de produit de la boutique et sans ouverture de la lettre d'information pendant trois saisons consécutives est supprimée ou rendue anonyme à la fin de la troisième saison.

Le détail des places (rang, siège) et les invitations des loges ne sont pas à modéliser.

### ANNEXE 1.4 – Réabonnements et fréquentation, et avis recueillis (juin 2027)

**A. Ensemble des abonnés (source : logiciel de billetterie ; relevé du prestataire de restauration)**

| Indicateur | 2024-2025 | 2025-2026 | 2026-2027 (provisoire) |
|---|---|---|---|
| Nombre d'abonnés | 7 000 | 7 000 | 7 000 |
| Taux de réabonnement (part des abonnés de la saison précédente qui se sont réabonnés) | 90 % | 85 % | 80 % |
| Part des abonnés dans leur première saison d'abonnement | 10 % | 15 % | 20 % |
| Taux de présence des abonnés aux 15 matchs à domicile | 84 % | 82 % | 72 % |
| Mode de mesure de la présence | entrées comptées par tribune, dont on retranche les billets vendus (estimation) | entrées comptées par tribune, dont on retranche les billets vendus (estimation) | lecture de chaque carte d'abonnement au contrôle d'accès par billet dématérialisé |
| Dépense moyenne à la boutique (stade et en ligne) par abonné et par saison | 70 € | 75 € | 80 € |
| Dépense moyenne à la restauration par abonné présent et par match (abonnés payant avec la carte rechargeable) | 7 € | 7 € | 7 € |

**B. Par tribune (le nombre d'abonnés de chaque tribune est le même en 2025-2026 et en 2026-2027)**

| Tribune | Places | Abonnés | Taux de réabonnement pour 2026-2027 | Taux de présence 2025-2026 (estimation) | Taux de présence 2026-2027 (contrôle d'accès) | Dépense moyenne à la boutique par abonné, 2026-2027 |
|---|---|---|---|---|---|---|
| Ouest (tribune d'honneur, salons) | 5 000 | 2 500 | 92 % | 90 % | 88 % | 120 € |
| Est | 5 000 | 2 000 | 80 % | 84 % | 70 % | 70 € |
| Nord (espace familles) | 3 000 | 1 500 | 70 % | 78 % | 64 % | 60 € |
| Sud (jeunes et étudiants) | 3 000 | 1 000 | 65 % | 64 % | 48 % | 30 € |
| **Ensemble** | **16 000** | **7 000** | **80 %** | **82 %** | **72 %** | **80 €** |

En 2026-2027, six des quinze matchs à domicile ont été joués le vendredi à 21 heures, contre deux en 2025-2026. La campagne « premier abonnement à moitié prix », lancée au printemps 2025 et reconduite en 2026, visait surtout les tribunes Nord et Sud.

**C. Avis recueillis**

**Mme Léa SOUBIRAC, responsable du pôle marketing et numérique** : « Le nombre d'abonnés tient, c'est l'essentiel. Mais je veux savoir qui va partir avant qu'il parte : l'agence de l'application nous propose un outil d'intelligence artificielle qui prédit les désabonnements. Il suffit de lui envoyer tous nos fichiers dès la rentrée. »

**Mme Nathalie ARRIBEUX, responsable de la billetterie** : « Attention aux chiffres de présence : jusqu'en 2025-2026, on comptait les entrées par tribune et on retranchait les billets vendus, sans compter les invités ni les enfants ; on surestimait sûrement la présence des abonnés. Depuis cette saison, chaque carte est lue à l'entrée. Ce qui m'inquiète, ce sont les familles de la tribune Nord : beaucoup m'ont dit au guichet que le vendredi soir, avec les enfants, ce n'est pas possible. »

**M. Olivier CARBESSE, directeur général de VIRANDEL Automobiles, concessionnaire automobile de l'agglomération et partenaire du club depuis 2019 (300 000 € par saison)** : « Vos supporters sont nos clients. Je vous propose, au choix : d'acheter votre fichier, à 1 € par fiche pour les 50 000 fiches d'adultes qui ont une adresse électronique, nom, adresse électronique, code postal, âge et tribune compris, que nous réutiliserons librement ; ou un accès permanent, pour 30 000 € par saison, à un espace en ligne où mes équipes choisiraient elles-mêmes les supporters à contacter ; ou, à défaut, de cofinancer une campagne : vous adressez vous-mêmes notre offre d'essai de véhicule aux supporters de votre choix, nous payons 10 000 € par campagne et vous ne nous transmettez que les résultats d'ensemble et les coordonnées des personnes qui demandent un essai sur notre formulaire. »

**M. Cédric BARRALOU, directeur commercial et des partenariats** : « 50 000 €, c'est le prix d'une loge pour la saison, et si VIRANDEL l'obtient, d'autres partenaires demanderont la même chose. »

**Le président de la plus ancienne association de supporters du club** (courriel du 12 mai 2027) : « Si le club vend nos adresses à ses partenaires, beaucoup d'entre nous rendront leur carte. »

### ANNEXE 1.5 – Repères sur la protection des données (au 31/12/2026)

| Texte | Repères utiles | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 (RGPD) | Une donnée à caractère personnel est toute information se rapportant à une personne physique identifiée ou identifiable, directement ou indirectement. Les données sont collectées pour des finalités déterminées, explicites et légitimes et ne sont pas traitées ultérieurement d'une manière incompatible avec ces finalités ; elles sont limitées à ce qui est nécessaire et conservées pendant une durée qui n'excède pas celle qui est nécessaire à ces finalités. Le responsable du traitement détermine les finalités et les moyens du traitement ; le sous-traitant traite les données pour son compte, sur ses instructions documentées, dans le cadre d'un contrat écrit. Chaque responsable du traitement tient un registre des activités de traitement : finalités, catégories de personnes et de données, catégories de destinataires, délais prévus pour l'effacement, description générale des mesures de sécurité. La désignation d'un délégué à la protection des données est obligatoire, notamment, lorsque les activités de base du responsable du traitement consistent en des opérations qui exigent un suivi régulier et systématique à grande échelle des personnes ; le délégué informe et conseille le responsable du traitement et les salariés, contrôle le respect du règlement et coopère avec l'autorité de contrôle. | Applicable depuis le 25/05/2018 |
| Directive 2002/58/CE « vie privée et communications électroniques », modifiée en 2009 | La prospection directe par courrier électronique auprès de personnes physiques suppose leur consentement préalable, sauf lorsqu'une entreprise s'adresse à ses propres clients pour des produits ou services analogues à ceux qu'elle leur a fournis, à condition qu'ils puissent s'y opposer simplement et gratuitement. | En vigueur depuis 2002, modifiée en 2009 |

### Travail à faire

Mme LAFERRADE veut que la connaissance des supporters devienne un levier du plan « MONTALBRET 2030 » : fidéliser les abonnés, développer les recettes de la boutique et des partenariats, sans entamer la confiance qui lie le club à ses supporters. Elle vous demande de remettre de l'ordre dans les données des supporters, d'en tirer un premier diagnostic et de lui proposer une position sur la demande de VIRANDEL Automobiles. Vous mobiliserez pour cela les annexes 1.1 à 1.5 ainsi que vos connaissances professionnelles.

**1.1 – Cartographie et urbanisation (2 points)**

a) À partir de l'annexe 1.2, schématisez, en format libre, la cartographie applicative des données des supporters : applications, données échangées et mode d'échange de chaque flux.

b) Après avoir défini l'urbanisation du système d'information, déduisez de votre cartographie trois défauts d'urbanisation, puis précisez la place d'un référentiel unique des supporters dans l'architecture cible.

**1.2 – Modélisation des données de la billetterie et des abonnements (3,5 points)**

a) À partir des règles de gestion de l'annexe 1.3, construisez le modèle conceptuel des données du référentiel (entités, identifiants, attributs, associations et cardinalités), en justifiant chaque cardinalité par une règle de gestion.

b) Déduisez-en le modèle logique des données (schéma relationnel), après avoir énoncé les règles de passage utilisées.

**1.3 – Qualité, cohérence et circulation des données (3,5 points)**

a) Proposez l'identifiant unique du supporter et trois règles de dédoublonnage des fiches existantes, puis un indicateur permettant d'en suivre l'efficacité, dont vous préciserez la formule, la source, la fréquence, la cible et l'axe du tableau de bord.

b) Après avoir défini le dictionnaire de données, rédigez son entrée pour trois données : l'adresse électronique, la date de naissance et le consentement à recevoir les offres des partenaires. Chaque entrée précisera quatre rubriques que vous choisirez et justifierez.

c) Désignez trois responsables des données des supporters en précisant le rôle et le titulaire de chacun, puis proposez, sans entrer dans le détail technique, le mode de circulation des données entre le référentiel et les applications qui remplacera les exports et les ressaisies.

**1.4 – Analyse des données de fidélité (2,5 points)**

a) Décrivez la chaîne de traitement qui permettrait d'exploiter les données de l'annexe 1.4 de façon fiable, en illustrant chacune de ses cinq étapes (collecte, nettoyage, structuration, analyse, restitution) par le cas.

b) Formulez un diagnostic argumenté de la fidélité des abonnés : deux constats tirés de l'annexe 1.4, une hypothèse explicative pour chacun, et deux précautions de lecture.

c) Recommandez, en la justifiant, la méthode d'analyse la plus adaptée à la prochaine étape, puis expliquez, par deux arguments tirés des annexes, pourquoi la proposition de prédiction des désabonnements est prématurée.

**1.5 – Valeur des données des supporters et demande du partenaire (2,5 points)**

a) Montrez en quoi les données des supporters constituent un patrimoine immatériel pour MONTALBRET XV, puis identifiez trois risques qui pèsent sur cet actif.

b) Distinguez les trois formules proposées par VIRANDEL Automobiles (vente des données, mise à disposition, campagne réalisée par le club pour le compte du partenaire), évaluez chacune au regard des repères de l'annexe 1.5, des enjeux économiques et de la confiance des supporters, puis recommandez une position assortie de deux conditions.
