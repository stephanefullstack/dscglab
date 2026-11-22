# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 21

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 22/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex58_consolidation_ifrs_change_latent_goodwill_complet` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.7 | `exercices/ex59_apport_partiel_endroit_valeur_reelle_soulte` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.11 | `exercices/ex60_audit_ventes_filiale_groupe_etranger_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 a IFRS obligatoires dès 2025 ; référentiel en cas de retour sur Euronext Growth | `2.1.b` Contexte réglementaire et légal de la consolidation | 2 |
| 1.1 b Lecture des comptes : quatre traitements comparés (IFRS / ANC) | `2.1.d` Méthodes et information financière | 2 |
| 1.2 Caractéristiques qualitatives auxiliaires ; réponse au fonds | `2.1.a` Cadre conceptuel | 2,5 |
| 1.3 Périmètre ; NAUTILÈNE ; date d'entrée de PALMÉOR | `2.1.c` Périmètre de consolidation | 2,5 |
| 1.4 a Frais d'acquisition du bâtiment : traitement, montants, tableau d'incidence | `2.2.c` Homogénéisation (frais d'acquisition, droits de mutation) | 2 |
| 1.4 b Frais d'acquisition du bâtiment : écritures | `2.2.c` Homogénéisation (frais d'acquisition, droits de mutation) | 2 |
| 1.5 a Change : vérification des comptes individuels, traitement IFRS | `2.2.d` Retraitements propres aux IFRS (change latent) | 2 |
| 1.5 b Change : tableau d'incidence, impôt différé | `2.2.d` Retraitements propres aux IFRS (change latent) | 2 |
| 1.5 c Change : écritures | `2.2.d` Retraitements propres aux IFRS (change latent) | 2 |
| 1.5 d Change : incidence sur le résultat et volatilité | `2.2.d` Retraitements propres aux IFRS (change latent) | 1 |
| 1.6 a Marge interne descendante | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.6 b Soldes réciproques, ventes internes, dividende | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.7 a Frais d'acquisition des titres PALMÉOR | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.7 b Actif net identifiable, goodwill complet, part des PNC | `2.2.g` Écarts d'évaluation et goodwill | 2,5 |
| 1.7 c Écarts d'évaluation : écritures, résultat retraité | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.7 d Perte de valeur du goodwill : écritures et répartition | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.8 a Tableaux de partage | `2.2.h` Partage des capitaux propres | 3 |
| 1.8 b Élimination des titres, partage, PNC à la clôture | `2.2.h` Partage des capitaux propres | 3 |
| 1.9 Phases du processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.10 a État du résultat net consolidé de 2026 | `2.3.a` Documents de synthèse consolidés | 5 |
| 1.10 b Deux informations sur l'acquisition de PALMÉOR | `2.3.a` Documents de synthèse consolidés | 1 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = participations ne donnant pas le contrôle (PNC) ; `CAP_ELIM` = capital de la filiale éliminé ; `EA` = goodwill ; `AMO_EA` = pertes de valeur cumulées du goodwill ; `DOT_EA` = perte de valeur du goodwill de l'exercice (ligne de l'état du résultat net) ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat de l'écriture de bilan. Un suffixe désigne la société concernée (`RST.SCAPHELIA`, `261.SCAPHELIA` : titres détenus par SCAPHÉLIA SE).

---

### 1.1 Référentiel et lecture des comptes (4 pts)

#### a. IFRS obligatoires dès 2025 ; retour éventuel sur Euronext Growth (2 pts)

**Règle (0,5 pt).** Les sociétés dont les titres sont admis aux négociations sur un **marché réglementé** d'un État membre **à la date de clôture** établissent leurs comptes consolidés, pour chaque exercice, selon les normes comptables internationales **adoptées par l'Union européenne** [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2, § 15]. Les autres sociétés établissent leurs comptes consolidés selon le règlement ANC n° 2020-01 **ou**, sur option, selon ces normes [V C. com. L. 233-24 ; F03 § 1.2].

**Application à 2025 (0,75 pt).** Euronext Growth est un système multilatéral de négociation, pas un marché réglementé : tant que les actions n'y étaient négociées, SCAPHÉLIA SE relevait du règlement ANC (comptes de 2024 et des exercices antérieurs). Ses actions sont admises sur Euronext Paris, marché réglementé, depuis le 12/06/2025 et le sont encore au **31/12/2025, date de clôture** : les comptes consolidés de **tout l'exercice 2025** devaient donc être établis en IFRS adoptées. Le critère est la situation à la clôture, non la date ni la durée de la cotation pendant l'exercice : l'admission en juin suffisait. Le règlement ANC ne lui était plus ouvert, puisqu'il ne vaut que pour les sociétés qui ne relèvent pas de l'obligation (annexe 1.2).

**Retour sur Euronext Growth (0,75 pt).** Si, à la clôture d'un exercice (par exemple le 31/12/2027), les actions n'étaient plus admises sur un marché réglementé, l'obligation ne jouerait plus pour cet exercice : SCAPHÉLIA SE rejoindrait les « autres » sociétés et pourrait **choisir** entre le règlement ANC n° 2020-01 et les IFRS adoptées, sur option [V L. 233-24 ; F03 § 1.2]. Un retour aux règles françaises serait donc possible, mais pas imposé ; conserver les IFRS préserverait la comparabilité des comptes d'un exercice à l'autre et avec les groupes cotés (question 1.2). Si le transfert intervenait après la clôture de 2027, les comptes de 2027 resteraient soumis aux IFRS. Dans tous les cas, les comptes individuels restent établis selon le PCG.

**Réponses tolérées** : référence au « règlement IAS » ou au « règlement européen de 2002 » sans numéro ; mention que le retour aux règles ANC constituerait un changement de référentiel qui devrait être expliqué aux lecteurs (non exigée).

**Erreurs fréquentes** : IFRS présentées comme obligatoires seulement à partir de 2026, premier exercice entier de cotation ; IFRS présentées comme applicables aux comptes individuels ; retour aux règles françaises présenté comme impossible, ou au contraire comme obligatoire ; examen des seuils de l'obligation de consolider, qui ne sont pas en cause (`JUR-F07`).

#### b. Ce que le référentiel change dans la lecture des comptes (2 pts)

Quatre traitements du dossier, 0,5 pt chacun (comparaison IFRS / ANC et conséquence pour le lecteur) [V F05 § 5 ; F04 R4, R12] :

| Traitement | IFRS (comptes de 2026) | Règlement ANC n° 2020-01 | Ce que voit le lecteur |
|---|---|---|---|
| Écarts de change latents (1.5) | Gain latent de 75 000 € et perte latente de 30 000 € en résultat financier (IAS 21 § 23, 28) | Retraitement propre aux IFRS (F04 R12) : traitement des comptes individuels conservé, perte latente provisionnée, gain latent non comptabilisé en résultat | Le résultat IFRS intègre des gains non réalisés (+ 75 000 € ici) et varie avec les cours de clôture |
| Goodwill de PALMÉOR (1.7) | Le goodwill n'est pas amorti ; une perte de valeur (400 000 € en 2026) est comptabilisée quand il perd de la valeur, et n'est jamais reprise | Écart d'acquisition amorti si sa durée d'utilisation est limitée (à défaut, sur dix ans), sinon non amorti et suivi ; dépréciation non reprise (art. 231-11) | En IFRS, pas de charge annuelle régulière, mais des pertes ponctuelles, parfois importantes, qui signalent une acquisition moins rentable que prévu |
| Frais d'acquisition des titres PALMÉOR (1.7 a) | Charges de 2026 (180 000 €) : le résultat de l'année de l'acquisition est réduit (IFRS 3 § 53) | Inclus dans le coût d'acquisition, nets d'impôt (135 000 €), donc dans l'écart d'acquisition (art. 231-2) | Le coût d'une acquisition pèse en IFRS sur le résultat de l'exercice où elle a lieu |
| Participations ne donnant pas le contrôle de PALMÉOR (1.7 b, 1.8) | Évaluées, sur option, à la juste valeur (2 300 000 €) : goodwill complet de 3 550 000 €, dont 630 000 € pour les PNC ; PNC présentées dans le total des capitaux propres | Intérêts minoritaires limités à leur quote-part de l'actif net réévalué (1 670 000 €), écart d'acquisition « partiel » (art. 232-1), rubrique distincte des capitaux propres du groupe (F14) | En IFRS, actif (goodwill) et capitaux propres plus élevés ; les minoritaires font partie des capitaux propres de l'ensemble |

**Réponses tolérées** : présentation de l'état du résultat net (pas de résultat exceptionnel en IFRS, IAS 1 § 87 : F14) à la place de l'un des quatre traitements.

**Erreurs fréquentes** : citer les frais d'acquisition du bâtiment comme une différence entre les deux référentiels : en consolidation selon le règlement ANC aussi, leur inscription à l'actif est obligatoire [V art. 272-6 ; F04 R4] ; citer l'élimination des marges internes ou des dividendes, identique dans les deux référentiels ; affirmer que l'écart d'acquisition n'est jamais amorti en ANC ; réponse générale sans chiffre du dossier (`JUR-F07`).

**Références normatives (1.1)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règlement (CE) n° 1606/2002, art. 4 ; C. com. L. 233-24 | IFRS adoptées obligatoires pour les sociétés cotées sur un marché réglementé à la clôture ; option pour les autres | [V] | F03 § 1.2, § 15 |
| IAS 21 § 23, 28 ; PCG art. 420-5 | Écarts de change latents | [V] | F04 R12 |
| IFRS 3 § 19, 32, 53 ; ANC 2020-01 art. 231-2, 231-11, 232-1, 272-6 | Goodwill, PNC, frais d'acquisition ; comparaison ANC | [V] | F05 § 1, § 2, § 5 ; F04 R4 |

---

### 1.2 Caractéristiques qualitatives auxiliaires (2,5 pts)

**Présentation (1 pt).** Pour être utile, l'information financière doit d'abord être **pertinente** et donner une **image fidèle** de ce qu'elle représente : ce sont les caractéristiques fondamentales [V Project Summary du cadre conceptuel de 2018, p. 6 ; F03 § 7.2, § 17]. Quatre caractéristiques **auxiliaires** en **améliorent l'utilité**, sans pouvoir rendre utile une information qui ne l'est pas [V p. 6] (0,25 pt) :
- la **comparabilité** : elle permet d'identifier et de comprendre les similitudes et les différences entre des éléments, d'une période à l'autre ou d'une entité à l'autre ; la permanence des méthodes y contribue, sans se confondre avec elle [S F03 § 17] (0,25 pt) ;
- la **vérifiabilité** : des observateurs différents, compétents et indépendants pourraient s'accorder, même sans accord complet, sur le fait qu'une information donne une image fidèle ; la vérification est directe (observation) ou indirecte (contrôle des données d'entrée d'un calcul et recalcul) [S F03 § 17] (0,25 pt) ;
- la **rapidité** (information disponible à temps pour influer sur les décisions) et la **compréhensibilité** (classement, description et présentation claires et concises, pour des utilisateurs qui ont une connaissance raisonnable des affaires et qui examinent l'information avec diligence) [S F03 § 17] (0,25 pt).

**Première inquiétude : la comparaison des comptes (0,75 pt).**
- Les comptes consolidés de 2026 présentent obligatoirement les montants de 2025, établis selon les **mêmes normes** et les mêmes méthodes [V IAS 1 § 38, 38A ; IAS 8 § 15 ; F03 § 17] : le fonds peut suivre l'évolution du groupe d'un exercice à l'autre à partir de 2025, sur des bases homogènes.
- Les comptes sont aussi comparables à ceux des **autres groupes cotés de l'Union**, qui appliquent les mêmes normes adoptées : c'est un gain pour un investisseur qui compare SCAPHÉLIA à ses concurrents.
- En revanche, la série antérieure, établie selon le règlement ANC, n'est pas directement comparable : les méthodes diffèrent (question 1.1 b : change latent, goodwill, frais d'acquisition, participations ne donnant pas le contrôle). La comparabilité est une qualité auxiliaire : elle ne justifierait pas de conserver un référentiel que la loi n'autorise plus, et c'est la pertinence de l'information qui prime.

**Seconde inquiétude : la juste valeur des 20 % de PALMÉOR (0,75 pt).**
- La juste valeur de 2 300 000 € n'est pas un prix payé : elle n'est pas vérifiable directement, mais elle l'est **indirectement** : la méthode (prix de cessions récentes d'actions de fabricants comparables non cotés), les données (cessions retenues) et la décote (absence de contrôle, faible liquidité) sont décrites dans le rapport de l'évaluateur et peuvent être contrôlées et recalculées par un autre spécialiste (annexe 1.7).
- Le groupe doit indiquer dans les notes la base d'évaluation de ces participations, les **techniques de valorisation et les données importantes** retenues [V IFRS 3 B64 o) ; F05 § 13] : le fonds disposera des éléments pour apprécier le chiffre.
- L'incertitude d'évaluation n'empêche pas l'information d'être utile [V Project Summary, p. 6 ; F03 § 17] ; l'enjeu est mesurable : la juste valeur augmente le goodwill et les PNC de 630 000 € par rapport à une évaluation à la quote-part de l'actif net (1 670 000 €).

**Réponses tolérées** : rapidité et compréhensibilité mobilisées pour la réponse au fonds (publication des comptes, clarté des notes) ; mention que les comptes de 2025 comportaient déjà des comparatifs de 2024 établis selon les mêmes normes (non exigée ; le passage aux IFRS n'est pas l'objet du dossier) ; mention du rôle du commissaire aux comptes du groupe dans la vérification (non exigée).

**Erreurs fréquentes** : caractéristiques fondamentales présentées comme auxiliaires ; idée qu'une information comparable mais non pertinente serait utile ; vérifiabilité confondue avec l'existence d'un prix payé ; réponse sans application aux deux inquiétudes (`JUR-F07`).

**Références normatives (1.2)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS Foundation, *Conceptual Framework — Project Summary*, mars 2018, p. 6 | Caractéristiques fondamentales et auxiliaires ; rôle des auxiliaires ; incertitude d'évaluation | [V] | F03 § 7.2, § 17 |
| Cadre conceptuel de 2018, chapitre 2 (texte intégral non lu) | Contenu de chaque caractéristique auxiliaire | [S] | F03 § 17 |
| IAS 1 § 38, 38A ; IAS 8 § 15 | Informations comparatives ; permanence des méthodes | [V] | F03 § 17 |
| IFRS 3 B64 o) | Informations sur les PNC évaluées à la juste valeur | [V] | F05 § 13 |

---

### 1.3 Périmètre (2,5 pts)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % des PNC |
|---|---:|---|---|---:|---:|
| PALMÉOR | 80 % | Exclusif | Intégration globale | 80 % | 20 % |
| SCAPHÉLIA Italia | 90 % | Exclusif | Intégration globale | 90 % | 10 % |
| NAUTILÈNE Plongée | 12 % | Aucun (ni contrôle, ni influence notable) | Hors périmètre | – | – |

(1,5 pt pour le tableau : 0,5 pt par ligne.)

Toutes les participations sont directes : pourcentages de contrôle et d'intérêt sont égaux [V F03 § 4.1]. SCAPHÉLIA SE détient la majorité des droits de vote de PALMÉOR et de SCAPHÉLIA Italia et nomme le président de PALMÉOR ; aucun pacte ne confère de droit particulier aux associés minoritaires [V IFRS 10 § 7 ; F03 § 2].

**NAUTILÈNE (0,5 pt).** Avec 12 % des droits de vote, l'investisseur est présumé ne pas exercer d'influence notable, sauf à la démontrer clairement [V IAS 28 § 5 ; F03 § 2] : SCAPHÉLIA SE n'est représentée dans aucun organe et ses ventes à NAUTILÈNE, aux conditions du marché, sont négligeables ; les essais réalisés par le centre ne constituent pas la fourniture, par SCAPHÉLIA SE, d'informations techniques essentielles à NAUTILÈNE : aucun des indices d'influence notable n'est réuni [V IAS 28 § 6]. La participation reste hors du périmètre ; elle figure parmi les actifs financiers (traitement non demandé).

**Date d'entrée de PALMÉOR (0,5 pt).** Le groupe en a obtenu le contrôle le 01/01/2026 : ses produits et ses charges entrent dans les comptes consolidés à compter de cette date, sur la base des justes valeurs de ses actifs et de ses passifs à la date d'acquisition [V IFRS 10 B88 ; F05 § 13]. Tout le résultat de 2026 est donc consolidé ; aucun résultat antérieur n'est intégré : les réserves de PALMÉOR au 01/01/2026 (4 400 000 €) font partie de l'actif net acquis et sont éliminées avec les titres (question 1.8).

**Erreurs fréquentes** : NAUTILÈNE mise en équivalence ; résultat de PALMÉOR consolidé au prorata ou à partir de 2027 ; réserves d'acquisition de PALMÉOR comptées dans les réserves consolidées.

**Références normatives (1.3)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 7 ; IAS 28 § 5 | Contrôle ; présomption d'influence notable | [V] | F03 § 2 |
| IFRS 10 B88 | Produits et charges consolidés à compter de la prise de contrôle | [V] | F05 § 13 |

---

### 1.4 Frais d'acquisition du bâtiment de stockage (4 pts)

#### a. Traitement, montants et tableau d'incidence (2 pts)

**Traitement (0,5 pt).** Selon les normes IFRS, le coût d'une immobilisation corporelle comprend son prix d'achat, y compris les **taxes non remboursables** (droits de mutation), et les coûts directement attribuables, dont les **honoraires de professionnels** et les frais d'actes [V IAS 16 § 16 a), b), 17 f) ; F04 R4, § 13] ; le manuel le confirme (annexe 1.4, point 2). SCAPHÉLIA SE a usé de l'option du PCG de les passer en charges [V PCG art. 213-8 ; F04 R4] : les comptes consolidés les réintègrent au coût et les amortissent avec la construction. Les frais déduits en 2026 font naître une différence temporelle imposable.

**Répartition et amortissement (1 pt).**
- Frais : 192 000 + 48 000 + 16 000 = **256 000 €**, répartis au prorata des prix (annexe 1.4, point 2) : terrain 256 000 × 640 000 / 3 200 000 = **51 200 €** ; construction 256 000 × 2 560 000 / 3 200 000 = **204 800 €** (0,5 pt).
- Le terrain n'est pas amorti. Amortissement complémentaire de la construction, du 01/07 au 31/12/2026 : 204 800 / 20 × 6 / 12 = **5 120 €** (0,5 pt).

**Tableau d'incidence au 31/12/2026 (0,5 pt)**

| | Comptes individuels | Comptes consolidés | Écart |
|---|---:|---:|---:|
| Terrain | 640 000 | 691 200 | + 51 200 |
| Construction (valeur brute) | 2 560 000 | 2 764 800 | + 204 800 |
| Amortissements de la construction | – 64 000 | – 69 120 | – 5 120 |
| **Valeur nette du bien** | **3 136 000** | **3 386 880** | **+ 250 880** |
| Charges de 2026 (frais et dotation) | 320 000 | 69 120 | **+ 250 880** sur le résultat avant impôt |
| Impôt différé passif (250 880 × 25 %) | | | – 62 720 |
| **Résultat net** | | | **+ 188 160** |

Base fiscale du bien : sa valeur dans les comptes individuels, 3 136 000 € (annexe 1.5) ; valeur consolidée supérieure : différence imposable, passif d'impôt différé de 62 720 €. Le bien ayant été acquis en 2026, aucune incidence ne touche les réserves.

**Réponses tolérées** : tableau limité aux écarts ; calcul de l'impôt différé sur les seuls frais affectés à la construction (204 800 – 5 120) avec un impôt différé distinct sur le terrain (51 200 × 25 %), même total.

**Erreurs fréquentes** : terrain amorti, ou frais du terrain amortis ; amortissement sur douze mois ; oubli de l'impôt différé ou impôt différé actif ; frais laissés en charges au motif que le PCG les autorise (`JUR-G06`) ; absence de tableau « comptes individuels → comptes consolidés » (`JUR-F05`).

#### b. Écritures (2 pts)

**C1 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2111 Terrains nus | 51 200 | |
| 2131 Bâtiments | 204 800 | |
| 2813 Amortissements des constructions | | 5 120 |
| IDP Impôt différé passif | | 62 720 |
| RST.SCAPHELIA Résultat SCAPHÉLIA SE | | 188 160 |
| **Total** | **256 000** | **256 000** |
| | *Libellé : frais d'acquisition du bâtiment de stockage incorporés au coût* | | |

**C1R (compte de résultat, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles | 5 120 | |
| CH_ID Charge d'impôt différé | 62 720 | |
| RES_CR Résultat | 188 160 | |
| 63541 Droits de mutation | | 192 000 |
| 6226 Honoraires | | 48 000 |
| 6227 Frais d'actes et de contentieux | | 16 000 |
| **Total** | **256 000** | **256 000** |

**Erreurs fréquentes** : écriture de bilan sans contrepartie en résultat de SCAPHÉLIA SE ; écriture de compte de résultat déséquilibrée (`JUR-F04`) ; amortissement porté au crédit du compte du bâtiment.

**Références normatives (1.4)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 16 § 16 a), b), 17 f) | Taxes non remboursables, coûts directement attribuables, honoraires | [V] | F04 R4, § 13 |
| PCG art. 213-8 ; ANC 2020-01 art. 272-6 | Option des comptes individuels ; activation obligatoire en consolidation ANC | [V] | F04 R4 |
| IAS 12 § 15 | Différence temporelle imposable | [V] | F04 § 1 |

---

### 1.5 Créance en dollars et dette en yens (7 pts)

#### a. Comptes individuels et traitement IFRS (2 pts)

**Vérification des montants (1 pt)**

| Élément | Cours du jour | Cours de clôture | Écart |
|---|---:|---:|---:|
| Créance : 1 980 000 USD | 1 980 000 / 1,1000 = 1 800 000 | 1 980 000 / 1,0560 = 1 875 000 | gain latent **75 000** (477) |
| Dette : 72 000 000 JPY | 72 000 000 / 160 = 450 000 | 72 000 000 / 150 = 480 000 | perte latente **30 000** (476 et provision 1515) |

Les montants inscrits par SCAPHÉLIA SE sont exacts (0,25 pt par montant vérifié, 0,25 pt pour le sens : l'euro a baissé face au dollar, la créance vaut plus ; il a baissé face au yen, la dette coûte plus).

**Comptes individuels (0,5 pt).** Les créances et les dettes en devises sont converties au dernier cours à la clôture ; les écarts sont inscrits en comptes transitoires, 476 pour une perte latente et 477 pour un gain latent ; seule la perte latente affecte le résultat, par une provision pour perte de change [V PCG art. 420-5 ; F04 R12]. Le gain latent sur le dollar n'est pas constaté en résultat et ne réduit pas la provision sur le yen.

**Comptes consolidés (0,5 pt).** Selon IAS 21, l'opération est enregistrée au cours du jour ; à la clôture, les éléments monétaires (créances, dettes) sont convertis au cours de clôture et les écarts, gains comme pertes, sont comptabilisés en résultat [V IAS 21 § 21, 23 a), 28 ; F04 R12, § 11 ; manuel, annexe 1.4, point 3]. Les comptes 476 et 477 et la provision n'ont plus d'objet : la créance et la dette restent à leur valeur au cours de clôture, le gain de 75 000 € et la perte de 30 000 € vont en résultat financier.

#### b. Tableau d'incidence et impôt différé (2 pts)

**Tableau d'incidence (1 pt)**

| | Comptes individuels | Comptes consolidés | Écart |
|---|---:|---:|---:|
| Créance en dollars | 1 875 000 | 1 875 000 | 0 |
| Dette en yens | 480 000 | 480 000 | 0 |
| 477 Différences de conversion – Passif | 75 000 | – | – 75 000 |
| 476 Différence de conversion – Actif | 30 000 | – | – 30 000 |
| 1515 Provision pour perte de change | 30 000 | – | – 30 000 |
| Gain de change (766) | – | + 75 000 | + 75 000 |
| Perte de change (666) | – | – 30 000 | – 30 000 |
| Dotation à la provision (6865) | – 30 000 | – | + 30 000 |
| **Résultat avant impôt** | | | **+ 75 000** |
| Impôt différé | | | **0** |
| **Résultat net** | | | **+ 75 000** |

**Impôt différé (1 pt).** Une différence temporelle n'existe que si la base fiscale d'un actif ou d'un passif diffère de sa valeur consolidée [V IAS 12 § 5, 15, 24 ; F04 R12] (0,25 pt). Selon l'hypothèse de l'annexe 1.6, les écarts de conversion sont compris dans le résultat imposable de 2026 : la base fiscale de la créance est 1 875 000 € et celle de la dette 480 000 €, égales à leurs valeurs IFRS ; aucune différence temporelle (0,25 pt). Le gain latent a déjà été imposé, et la perte latente déduite, dans l'impôt exigible de SCAPHÉLIA SE : la charge d'impôt consolidée correspond désormais au gain et à la perte portés en résultat (0,25 pt). La provision, non déductible, n'avait pas réduit l'impôt de SCAPHÉLIA SE : son annulation est sans conséquence fiscale. **Aucun impôt différé** (0,25 pt).

**Réponses tolérées** : raisonnement par le résultat (résultat imposable de 2026 = résultat IFRS pour ces opérations) au lieu des bases fiscales.

**Erreurs fréquentes** : impôt différé passif de 18 750 € sur le gain et impôt différé actif de 7 500 € sur la perte, calculés sans examiner l'hypothèse fiscale (`JUR-F07`) ; créance et dette « reconverties » une seconde fois ; provision maintenue à côté de la perte de change (perte comptée deux fois).

#### c. Écritures (2 pts)

**C2 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 477 Différences de conversion – Passif | 75 000 | |
| 1515 Provisions pour pertes de change | 30 000 | |
| 476 Différence de conversion – Actif | | 30 000 |
| RST.SCAPHELIA Résultat SCAPHÉLIA SE | | 75 000 |
| **Total** | **105 000** | **105 000** |
| | *Libellé : écarts de change latents portés en résultat, provision annulée* | | |

**C2R (compte de résultat, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 666 Pertes de change financières | 30 000 | |
| RES_CR Résultat | 75 000 | |
| 766 Gains de change financiers | | 75 000 |
| 6865 Dotations aux provisions financières | | 30 000 |
| **Total** | **105 000** | **105 000** |

#### d. Incidence et volatilité (1 pt)

**Incidence (0,5 pt).** Le résultat net consolidé est supérieur de **75 000 €** à ce que donneraient les comptes individuels : le gain latent entre en résultat, la perte latente y figure désormais comme une perte de change au lieu d'une dotation (effet nul) ; sans impôt différé.

**Volatilité (0,5 pt).** En IFRS, chaque clôture fait entrer en résultat les écarts non réalisés, gains comme pertes : le résultat dépend des cours du 31 décembre et l'écart de 2026 peut s'inverser en 2027 si les cours évoluent d'ici au règlement (février et mars 2027). Les comptes individuels, eux, n'enregistrent que les pertes probables et attendent le règlement pour les gains : leur résultat est plus prudent et moins sensible aux cours. Le groupe n'ayant conclu aucun contrat pour se protéger de l'évolution des cours, rien ne compense ces variations dans son résultat.

**Références normatives (1.5)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 420-5 ; comptes 476, 477, 1515 | Conversion à la clôture, comptes transitoires, provision | [V] | F04 R12 |
| IAS 21 § 21, 23 a), 28 | Cours du jour, cours de clôture, écarts en résultat | [V] | F04 R12, § 11 |
| IAS 12 § 5, 15, 24 | Différences temporelles imposables et déductibles | [V] | F04 § 1, R12 |

---

### 1.6 Opérations internes (4 pts)

#### a. Marge interne descendante (2 pts)

**Calcul (0,75 pt).** Le taux de 30 % est exprimé sur le coût de production : la marge comprise dans un prix d'achat de 130 vaut 30, soit **30 / 130** du stock.
- Marge au 01/01/2026 : 520 000 × 30 / 130 = **120 000 €** (impôt différé actif d'ouverture 30 000 €, incidence nette 90 000 € sur les réserves) ;
- Marge au 31/12/2026 : 780 000 × 30 / 130 = **180 000 €** (impôt différé actif 45 000 €) ;
- Incidence de 2026 : 180 000 – 120 000 = **60 000 €** avant impôt, soit **45 000 €** nets (0,25 pt pour chacun des deux stocks, 0,25 pt pour la variation et l'impôt).

**Écritures (0,75 pt)**

**C3 (bilan)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RSV.SCAPHELIA Réserves SCAPHÉLIA SE (120 000 × 75 %) | 90 000 | |
| RST.SCAPHELIA Résultat SCAPHÉLIA SE (60 000 × 75 %) | 45 000 | |
| IDA Impôt différé actif (180 000 × 25 %) | 45 000 | |
| 37 Stocks de marchandises (SCAPHÉLIA Italia) | | 180 000 |
| **Total** | **180 000** | **180 000** |
| | *Libellé : marge de SCAPHÉLIA SE comprise dans les stocks de SCAPHÉLIA Italia* | | |

**C3R (compte de résultat)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6037 Variation des stocks de marchandises (180 000 – 120 000) | 60 000 | |
| CH_ID Produit d'impôt différé (60 000 × 25 %) | | 15 000 |
| RES_CR Résultat | | 45 000 |
| **Total** | **60 000** | **60 000** |

**Pourquoi les minoritaires de SCAPHÉLIA Italia n'en supportent rien (0,5 pt).** Les résultats internes compris dans des actifs sont éliminés en totalité et imputés à la société qui les a **réalisés** [V manuel, annexe 1.4, point 6 ; ANC art. 251-2 ; F04 R14] ; l'élimination totale résulte aussi d'IFRS 10 B86 c). La vente est **descendante** : la marge a été dégagée par SCAPHÉLIA SE, société mère, dont le résultat revient entièrement aux propriétaires du groupe. SCAPHÉLIA Italia a payé ses achats au prix convenu : son résultat, et donc la part des minoritaires (10 % × 900 000 = 90 000 €), est inchangé.

**Erreurs fréquentes** : marge calculée à 30 % du stock (234 000 €) ; élimination de la seule marge de clôture en résultat, sans reprise de la marge d'ouverture par les réserves ; marge imputée à SCAPHÉLIA Italia et partagée 90 / 10.

#### b. Soldes réciproques, ventes internes et dividende (2 pts)

**C4 (bilan, 0,5 pt)** : débit 401 Fournisseurs (SCAPHÉLIA Italia) 940 000 ; crédit 411 Clients (SCAPHÉLIA SE) 940 000. *Libellé : élimination des soldes réciproques ; montants concordants, aucune mise en concordance.*

**C4R (compte de résultat, 0,5 pt)** : débit 701 Ventes de produits finis (SCAPHÉLIA SE) 6 400 000 ; crédit 607 Achats de marchandises (SCAPHÉLIA Italia) 6 400 000. *Libellé : élimination des ventes internes.* Écriture sans incidence sur le résultat [V ANC art. 251-1 ; IFRS 10 B86 c) ; F04 R14].

**Dividende (1 pt).** SCAPHÉLIA SE a reçu 90 % × 500 000 = **450 000 €** ; ce montant est éliminé du résultat de la mère et reclassé en réserves, puisqu'il provient de résultats déjà consolidés [V manuel, annexe 1.4, point 6 ; F04 R14] (0,25 pt).

**C5 (bilan)** : débit RST.SCAPHELIA Résultat SCAPHÉLIA SE 450 000 ; crédit RSV.SCAPHELIA Réserves SCAPHÉLIA SE 450 000 (0,25 pt).

**C5R (compte de résultat)** : débit 7611 Revenus des titres de participation 450 000 ; crédit RES_CR Résultat 450 000 (0,25 pt).

Les **50 000 €** versés au distributeur italien ne sont pas éliminés : ils sont sortis du groupe au profit d'un tiers ; ils ont réduit les réserves de SCAPHÉLIA Italia, donc la part des minoritaires dans ces réserves (0,25 pt).

**Erreurs fréquentes** : élimination de 500 000 € ; dividende éliminé dans les réserves de la filiale ; ventes éliminées pour 6 400 000 × 30 / 130.

**Références normatives (1.6)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 B86 c) ; ANC 2020-01 art. 251-1, 251-2 | Élimination des opérations internes, imputation au vendeur, dividendes internes | [V] | F04 R14 |

---

### 1.7 Acquisition de PALMÉOR (7 pts)

#### a. Frais d'acquisition des titres (1,5 pt)

**Traitement (0,5 pt).** Les frais connexes à l'acquisition (honoraires d'avocats, de banque d'affaires, d'audit) sont des **charges** de la période : ils rémunèrent des services, ils ne font pas partie de la contrepartie transférée et n'entrent pas dans le goodwill [V IFRS 3 § 53 ; F05 § 2 ; manuel, annexe 1.4, point 4]. SCAPHÉLIA SE les a incorporés au coût des titres (9 780 000 €) : le retraitement ramène les titres à 9 600 000 € et constate la charge ; aucun impôt différé (hypothèse de l'annexe 1.7).

**C6 (bilan, 0,5 pt)** : débit RST.SCAPHELIA Résultat SCAPHÉLIA SE 180 000 ; crédit 261.SCAPHELIA Titres de participation PALMÉOR 180 000. *Libellé : frais d'acquisition des titres PALMÉOR passés en charges.*

**C6R (compte de résultat, 0,5 pt)** : débit 6226 Honoraires 180 000 ; crédit RES_CR Résultat 180 000.

**Erreurs fréquentes** : frais maintenus dans le coût des titres, ou dans le coût net d'impôt comme en ANC (`JUR-G02`, transposé à tort) ; impôt différé constaté contre l'hypothèse.

#### b. Actif net identifiable et goodwill complet (2,5 pts)

**Actif net identifiable à la juste valeur au 01/01/2026 (1 pt)**

| | Montant |
|---|---:|
| Capitaux propres de PALMÉOR | 6 400 000 |
| Marque « Abyssale » (2 400 000 – 0) | + 2 400 000 |
| Stock de produits finis (1 400 000 – 1 200 000) | + 200 000 |
| Impôt différé passif sur les écarts (2 600 000 × 25 %) | – 650 000 |
| **Actif net identifiable** | **8 350 000** |

**Goodwill complet (1 pt).** Les participations ne donnant pas le contrôle sont évaluées à leur juste valeur, option retenue pour ce regroupement [V IFRS 3 § 19 ; manuel, annexe 1.4, point 4] :

Goodwill = contrepartie transférée + PNC à la juste valeur – actif net identifiable [V IFRS 3 § 32 ; F05 § 2.1]
= 9 600 000 + 2 300 000 – 8 350 000 = **3 550 000 €**.

La contrepartie transférée est le prix payé, 160 000 × 60 = 9 600 000 €, hors frais (question 1.7 a). Aucun impôt différé n'est constaté sur le goodwill [V IAS 12 § 15 a) ; F05 § 2].

**Part des PNC dans le goodwill (0,5 pt)** : juste valeur des PNC – leur quote-part de l'actif net = 2 300 000 – 20 % × 8 350 000 = 2 300 000 – 1 670 000 = **630 000 €** [V F05 § 2.1] ; part du groupe : 9 600 000 – 80 % × 8 350 000 = **2 920 000 €** (contrôle : 2 920 000 + 630 000 = 3 550 000).

**Réponses tolérées** : calcul de la part du groupe seule, puis de la part des PNC par différence.

**Erreurs fréquentes** : frais de 180 000 € ajoutés au prix ; écarts d'évaluation retenus bruts d'impôt différé ; goodwill calculé sur 80 % de l'actif net (goodwill partiel, 2 920 000 €) alors que le manuel retient la juste valeur des PNC ; impôt différé sur le goodwill.

#### c. Écarts d'évaluation (1,5 pt)

**C7 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Concessions et droits similaires, brevets, licences, marques – marque Abyssale | 2 400 000 | |
| 355 Produits finis | 200 000 | |
| IDP Impôt différé passif (2 600 000 × 25 %) | | 650 000 |
| RSV.PALMEOR Réserves PALMÉOR – écarts d'évaluation nets | | 1 950 000 |
| **Total** | **2 600 000** | **2 600 000** |
| | *Libellé : écarts d'évaluation de PALMÉOR au 01/01/2026* | | |

**Incidence de 2026 (0,5 pt).** La marque, à durée d'utilité indéterminée, n'est pas amortie [V IAS 38 § 107 ; F05 § 11] : aucune écriture en 2026. Le stock a été vendu : son coût consolidé est sa juste valeur à la date d'acquisition [V IFRS 10 B88 ; F05 § 13], l'écart de 200 000 € est repris en résultat avec son impôt différé.

**C8 (bilan)** : débit RST.PALMEOR Résultat PALMÉOR 150 000 ; débit IDP Impôt différé passif 50 000 ; crédit 355 Produits finis 200 000.

**C8R (compte de résultat)** : débit 7135 Variation des stocks de produits 200 000 ; crédit CH_ID Produit d'impôt différé 50 000 ; crédit RES_CR Résultat 150 000.

**Résultat retraité de PALMÉOR (0,5 pt)** : 1 305 000 – 200 000 × 75 % = **1 155 000 €**.

#### d. Perte de valeur du goodwill (1,5 pt)

**Répartition (0,5 pt).** Le goodwill complet comprend la part des participations ne donnant pas le contrôle ; le manuel répartit la perte de valeur du goodwill d'une filiale dont les PNC sont évaluées à la juste valeur **selon la même clé que son résultat** [V annexe 1.4, point 5 ; règle vérifiée sur le texte de la norme : F05 § 13] : groupe 80 % × 400 000 = **320 000 €** ; PNC 20 % × 400 000 = **80 000 €**. La clé est celle du résultat, et non la part des PNC dans le goodwill (630 / 3 550, soit 17,75 %).

**C10 (bilan, 0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST_G Résultat consolidé – part du groupe | 320 000 | |
| RST_M Participations ne donnant pas le contrôle – résultat | 80 000 | |
| AMO_EA Pertes de valeur cumulées du goodwill de PALMÉOR | | 400 000 |
| **Total** | **400 000** | **400 000** |
| | *Libellé : perte de valeur du goodwill de PALMÉOR au 31/12/2026* | | |

**C10R (compte de résultat, 0,25 pt)** : débit DOT_EA Perte de valeur du goodwill 400 000 ; crédit RES_CR Résultat 400 000. La charge figure sur sa ligne de l'état du résultat net, dans le résultat opérationnel (annexe 1.4, points 1 et 5).

**Sort ultérieur (0,5 pt).** La perte de valeur du goodwill n'est **jamais reprise**, même si la valeur de PALMÉOR se redresse [V F05 § 2 ; manuel, annexe 1.4, point 5] ; le goodwill net est de 3 550 000 – 400 000 = **3 150 000 €**. Dans les exercices suivants, la perte est reprise dans les réserves consolidées (part du groupe) et dans les réserves des PNC. Elle n'est pas déductible et ne donne lieu à aucun impôt différé (hypothèse du manuel ; IAS 12 § 15 a)).

**Réponses tolérées** : perte de valeur imputée par les postes du partage (C9 et C10 fusionnées) si la répartition 320 000 / 80 000 est juste.

**Erreurs fréquentes** : perte imputée au seul groupe, comme pour un goodwill partiel ; répartition selon la part des PNC dans le goodwill ; impôt différé actif de 100 000 € ; perte calculée ou recalculée alors qu'elle est fournie (`JUR-F07`).

**Références normatives (1.7)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 19, 32, 53 | Option de la juste valeur des PNC, goodwill, frais connexes en charges | [V] | F05 § 2, § 2.1 |
| IAS 12 § 15 a) | Pas d'impôt différé sur le goodwill | [V] | F05 § 2 |
| IAS 38 § 107 ; IFRS 10 B88 | Marque non amortie ; charges établies sur les justes valeurs d'acquisition | [V] | F05 § 11, § 13 |
| Règle de répartition de la perte de valeur du goodwill entre le groupe et les PNC, perte non reprise | Lue sur le texte de la norme ; donnée par le manuel | [V] | F05 § 2, § 13 |

---

### 1.8 Partage des capitaux propres (6 pts)

#### a. Tableaux de partage (3 pts)

**PALMÉOR au 01/01/2026 (1 pt)**

| | Total | Groupe (80 %) | PNC (20 %) |
|---|---:|---:|---:|
| Capital | 2 000 000 | 1 600 000 | 400 000 |
| Réserves | 4 400 000 | 3 520 000 | 880 000 |
| Écarts d'évaluation nets d'impôt | 1 950 000 | 1 560 000 | 390 000 |
| **Actif net identifiable** | **8 350 000** | **6 680 000** | **1 670 000** |
| Goodwill complet | 3 550 000 | 2 920 000 | 630 000 |
| **Total** | **11 900 000** | **9 600 000** | **2 300 000** |
| Titres éliminés | – 9 600 000 | – 9 600 000 | – |
| **Solde** | **2 300 000** | **0** | **2 300 000** |

La part du groupe égale le coût des titres et celle des PNC leur juste valeur : rien n'entre dans les réserves consolidées à l'acquisition.

**PALMÉOR au 31/12/2026 (1,25 pt)**

| | Total | Groupe (80 %) | PNC (20 %) |
|---|---:|---:|---:|
| Capitaux propres retraités hors résultat | 8 350 000 | 6 680 000 | 1 670 000 |
| Résultat retraité de 2026 | 1 155 000 | 924 000 | 231 000 |
| Goodwill complet | 3 550 000 | 2 920 000 | 630 000 |
| Perte de valeur du goodwill | – 400 000 | – 320 000 | – 80 000 |
| **Total** | **12 655 000** | **10 204 000** | **2 451 000** |
| Titres éliminés | – 9 600 000 | – 9 600 000 | – |
| **Part revenant à chacun** | | **604 000** (réserves 0, résultat 604 000) | **2 451 000** (dont résultat 151 000) |

**SCAPHÉLIA Italia au 31/12/2026 (0,75 pt)**

| | Total | Groupe (90 %) | PNC (10 %) |
|---|---:|---:|---:|
| Capital | 500 000 | 450 000 | 50 000 |
| Réserves (après distribution) | 1 200 000 | 1 080 000 | 120 000 |
| Résultat de 2026 | 900 000 | 810 000 | 90 000 |
| **Total** | **2 600 000** | **2 340 000** | **260 000** |
| Titres éliminés | – 450 000 | – 450 000 | – |
| **Part revenant à chacun** | | **1 890 000** (réserves 1 080 000, résultat 810 000) | **260 000** |

Le résultat de SCAPHÉLIA Italia n'est pas retraité : la marge interne et le dividende sont imputés à SCAPHÉLIA SE (question 1.6).

**Erreurs fréquentes** : partage des capitaux propres individuels, sans les écarts d'évaluation (`JUR-G04`) ; part des PNC limitée à 20 % de l'actif net (goodwill partiel) ; perte de valeur oubliée dans la part des PNC ; marge interne retranchée du résultat de SCAPHÉLIA Italia.

#### b. Écritures et PNC à la clôture (3 pts)

**C9 (bilan, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.PALMEOR Capital PALMÉOR | 2 000 000 | |
| RSV.PALMEOR Réserves PALMÉOR (4 400 000 + 1 950 000) | 6 350 000 | |
| RST.PALMEOR Résultat PALMÉOR retraité | 1 155 000 | |
| EA Goodwill complet | 3 550 000 | |
| 261.SCAPHELIA Titres PALMÉOR (9 780 000 – 180 000) | | 9 600 000 |
| RST_G Résultat consolidé – part du groupe (80 % × 1 155 000) | | 924 000 |
| RSV_M PNC – juste valeur à l'acquisition (1 670 000 + 630 000) | | 2 300 000 |
| RST_M PNC – résultat (20 % × 1 155 000) | | 231 000 |
| **Total** | **13 055 000** | **13 055 000** |
| | *Libellé : élimination des titres PALMÉOR, goodwill complet et partage (80 / 20)* | | |

La perte de valeur du goodwill est enregistrée par l'écriture C10 (question 1.7 d). Les réserves consolidées part du groupe issues de PALMÉOR sont nulles.

**C11 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.ITALIA Capital SCAPHÉLIA Italia | 500 000 | |
| RSV.ITALIA Réserves SCAPHÉLIA Italia | 1 200 000 | |
| RST.ITALIA Résultat SCAPHÉLIA Italia | 900 000 | |
| 261.SCAPHELIA Titres SCAPHÉLIA Italia | | 450 000 |
| RSV_G Réserves consolidées – part du groupe (90 % × 1 700 000 – 450 000) | | 1 080 000 |
| RST_G Résultat consolidé – part du groupe (90 % × 900 000) | | 810 000 |
| RSV_M PNC – réserves (10 % × 1 700 000) | | 170 000 |
| RST_M PNC – résultat (10 % × 900 000) | | 90 000 |
| **Total** | **2 600 000** | **2 600 000** |

**Participations ne donnant pas le contrôle au 31/12/2026 (1 pt)**

| | Réserves | Résultat | Total |
|---|---:|---:|---:|
| PALMÉOR : juste valeur à l'acquisition, résultat, perte de valeur | 2 300 000 | 231 000 – 80 000 = 151 000 | 2 451 000 |
| SCAPHÉLIA Italia | 170 000 | 90 000 | 260 000 |
| **Total** | **2 470 000** | **241 000** | **2 711 000** |

Les PNC sont présentées au sein des capitaux propres consolidés, distinctement des capitaux propres attribuables aux propriétaires de SCAPHÉLIA SE [V IFRS 10 § 22 ; F14 § 2.2].

**Erreurs fréquentes** : titres éliminés pour 9 780 000 € (goodwill majoré des frais) ; goodwill porté pour sa seule part du groupe avec des PNC à la juste valeur (écriture déséquilibrée, `JUR-F04`) ; PNC de PALMÉOR à 1 901 000 € (20 % des capitaux propres retraités, sans goodwill) ; PNC présentées hors des capitaux propres.

**Références normatives (1.8)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 B86 b) ; IFRS 3 § 19, 32 | Élimination des titres ; goodwill complet | [V] | F05 § 2, § 3 |
| IFRS 10 § 22 | PNC au sein des capitaux propres | [V] | F14 § 2.2 |

---

### 1.9 Phases du processus de consolidation (2 pts)

**Rattachement (1,5 pt : 0,25 pt par traitement correctement rattaché : bâtiment, change, frais des titres, opérations internes, écarts d'évaluation et goodwill, partage)**

| Phase | Traitements du dossier |
|---|---|
| 1. Retraitements d'homogénéisation des comptes individuels | Frais d'acquisition du bâtiment (1.4) et écarts de change latents (1.5), chez SCAPHÉLIA SE ; frais d'acquisition des titres PALMÉOR inscrits au coût des titres par SCAPHÉLIA SE (1.7 a) |
| 2. Éliminations des opérations internes | Marge interne sur les stocks de SCAPHÉLIA Italia (1.6 a) ; soldes réciproques, ventes internes, dividende (1.6 b) |
| 3. Regroupement d'entreprises : écarts d'évaluation et goodwill | Actif net identifiable de PALMÉOR, écarts d'évaluation et leur incidence de 2026, goodwill complet (1.7 b et c) ; perte de valeur du goodwill (1.7 d) |
| 4. Élimination des titres et partage des capitaux propres | Tableaux de partage, écritures C9 et C11, PNC à la clôture (1.8) |

**Réponses tolérées** : frais d'acquisition des titres classés en phase 3, avec le regroupement, s'ils sont justifiés (retraitement des comptes de la mère qui modifie le coût des titres à éliminer) ; perte de valeur du goodwill classée en phase 4.

**Ordre (0,5 pt).** Le partage répartit des capitaux propres et des résultats **déjà retraités** et élimine les titres pour leur coût **retraité**. Les retraitements de SCAPHÉLIA SE modifient son résultat (+ 188 160 + 75 000 – 180 000 – 45 000 – 450 000 €) et ses réserves (– 90 000 + 450 000 €), qui reviennent au groupe, et le coût des titres PALMÉOR à éliminer (9 600 000 € au lieu de 9 780 000 €) : faire le partage avant aurait surévalué le goodwill de 180 000 € et faussé le résultat du groupe.

**Erreurs fréquentes** : partage présenté comme une première étape ; confusion entre retraitements d'homogénéisation et éliminations ; marge interne classée parmi les retraitements d'homogénéisation.

---

### 1.10 État du résultat net consolidé (6 pts)

#### a. État du résultat net consolidé de 2026 (5 pts)

Présentation par nature (annexe 1.4, point 1 ; IAS 1 § 82, 99, 102 ; F14 § 2.3). Charges en négatif.

| Poste | SCAPHÉLIA SE | PALMÉOR | SCAPHÉLIA Italia | Retraitements et éliminations | **Consolidé** |
|---|---:|---:|---:|---:|---:|
| Produits des activités ordinaires | 112 400 000 | 22 000 000 | 20 000 000 | – 6 400 000 (C4R) | **148 000 000** |
| Achats consommés et variation des stocks | – 58 600 000 | – 10 100 000 | – 14 300 000 | + 6 400 000 (C4R) – 60 000 (C3R) – 200 000 (C8R) | **– 76 860 000** |
| Charges de personnel | – 27 800 000 | – 6 100 000 | – 2 500 000 | | **– 36 400 000** |
| Charges externes | – 13 100 000 | – 3 080 000 | – 1 600 000 | + 64 000 (C1R) – 180 000 (C6R) | **– 17 896 000** |
| Impôts et taxes | – 1 950 000 | – 390 000 | – 120 000 | + 192 000 (C1R) | **– 2 268 000** |
| Dotations aux amortissements et aux provisions | – 4 450 000 | – 560 000 | – 260 000 | – 5 120 (C1R) | **– 5 275 120** |
| Perte de valeur du goodwill | | | | – 400 000 (C10R) | **– 400 000** |
| **Résultat opérationnel** | 6 500 000 | 1 770 000 | 1 220 000 | – 589 120 | **8 900 880** |
| Résultat financier | 140 000 | – 30 000 | – 20 000 | + 75 000 (C2R) – 450 000 (C5R) | **– 285 000** |
| **Résultat avant impôt** | 6 640 000 | 1 740 000 | 1 200 000 | – 964 120 | **8 615 880** |
| Impôt sur le résultat | – 1 572 000 | – 435 000 | – 300 000 | – 62 720 + 15 000 + 50 000 = + 2 280 | **– 2 304 720** |
| **Résultat net de l'ensemble consolidé** | 5 068 000 | 1 305 000 | 900 000 | – 961 840 | **6 311 160** |
| Attribuable aux participations ne donnant pas le contrôle | | | | | **241 000** |
| **Attribuable aux propriétaires de SCAPHÉLIA SE** | | | | | **6 070 160** |

L'impôt sur le résultat comprend l'impôt exigible (– 2 307 000 €) et un produit net d'impôt différé (+ 2 280 €). Le chiffre d'affaires consolidé est bien celui annoncé (148 M€).

**Contrôles.**
- Par les résultats : 5 068 000 + 1 305 000 + 900 000 = 7 273 000 ; retraitements : + 188 160 (bâtiment) + 75 000 (change) – 45 000 (marge) – 450 000 (dividende) – 180 000 (frais des titres) – 150 000 (stock de PALMÉOR) – 400 000 (perte de valeur) = – 961 840 ; résultat de l'ensemble **6 311 160 €**.
- PNC : PALMÉOR 20 % × (1 155 000 – 400 000) = 151 000 ; SCAPHÉLIA Italia 10 % × 900 000 = 90 000 ; total **241 000 €**.
- Propriétaires : SCAPHÉLIA SE 5 068 000 + 188 160 + 75 000 – 45 000 – 450 000 – 180 000 = 4 656 160 ; PALMÉOR 924 000 – 320 000 = 604 000 ; SCAPHÉLIA Italia 810 000 ; total **6 070 160 €**.

**Barème** : 0,25 pt par ligne juste de produits et de charges (sept lignes, perte de valeur du goodwill comprise : 1,75 pt) ; 0,5 pt pour le résultat financier (dividende éliminé, écarts de change) ; 0,5 pt pour l'impôt (exigible et différé) ; 0,25 pt pour chacun des trois sous-totaux (résultat opérationnel, résultat avant impôt, résultat net : 0,75 pt) ; 0,5 pt pour la part des PNC et 0,5 pt pour celle des propriétaires ; 0,5 pt pour la présentation (par nature, IAS 1, aucun élément « extraordinaire », aucun autre élément du résultat global en 2026, état du résultat global réduit au résultat net).

**Réponses tolérées** : présentation sans les colonnes des sociétés si les retraitements sont justifiés ; perte de valeur du goodwill présentée juste avant le résultat opérationnel ou parmi les dotations, si elle est identifiée.

**Erreurs fréquentes** : dividende interne laissé en résultat financier ; ventes internes non éliminées (chiffre d'affaires de 154 400 000 €) ; perte de valeur imputée au seul groupe dans la répartition ; résultat présenté en part du groupe seulement ; « dotation à l'amortissement du goodwill » ou résultat exceptionnel en IFRS (`JUR-G01`).

#### b. Deux informations sur l'acquisition de PALMÉOR (1 pt)

Deux informations, 0,5 pt chacune [V IFRS 3 B64 ; F05 § 13] :
- **Participations ne donnant pas le contrôle** : montant à la date d'acquisition, **2 300 000 €**, évaluées à la juste valeur ; technique de valorisation et données importantes : prix de cessions récentes d'actions de fabricants comparables non cotés, décote pour absence de contrôle et faible liquidité [V B64 o)] ;
- **Coûts connexes à l'acquisition** : **180 000 €**, comptabilisés en charges externes de 2026 [V B64 m)].

**Réponses tolérées** (B64 a) à f), i)) : nom, description de PALMÉOR, date d'acquisition (01/01/2026) et pourcentage des droits de vote acquis (80 %) ; contrepartie transférée de 9 600 000 €, en trésorerie ; montants comptabilisés pour les principales catégories d'actifs et de passifs (marque 2 400 000 €, stock 1 400 000 €, impôt différé passif 650 000 €) ; goodwill de 3 550 000 € et description qualitative de ses composantes (synergies attendues avec la gamme de SCAPHÉLIA, savoir-faire). Toute information non chiffrée vaut 0,25 pt au plus.

**Références normatives (1.10)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 1 § 81A, 81B, 82, 87, 99, 102 ; IFRS 18 C1 | Postes, attribution, présentation par nature ; IFRS 18 non appliquée en 2026 | [V] | F14 § 0, § 2.3 |
| IFRS 3 B64 a) à o) | Informations à fournir sur un regroupement | [V] | F05 § 10, § 13 |

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, branche complète, référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2 |
| 2.2 Régime de faveur : conditions, plus-value d'apport, engagements, titres reçus, cas de l'agrément | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 2 |
| 2.3 a) Nombre d'actions et augmentation de capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1 |
| 2.3 b) Soulte, équité, limite légale, condition fiscale | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 2 |
| 2.3 c) Variante à la centaine inférieure : conseil | `1.2.b` Déterminer une soulte simple et vérifier sa légalité ; `1.1.b` | 1 |
| 2.3 d) Répartition du capital d'AGRÉSIA après l'opération | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1 |
| 2.4 Mode d'évaluation des apports | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 2 |
| 2.5 a) Valeurs réelles, provision pour impôts, fonds commercial, composition | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 5 |
| 2.5 b) Prime d'apport | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1 |
| 2.6 a) VENTOUREL : apport, titres et soulte reçus, traitement fiscal de la plus-value | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) ; `1.1.b` | 2,5 |
| 2.6 b) AGRÉSIA : augmentation de capital, soulte, réalisation des apports | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 2 |
| 2.6 c) AGRÉSIA : frais de l'opération, dette et créance réciproques | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 1,5 |
| 2.7 Note à M. LAUZERANDE | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Qualification, branche complète et référentiel (2 pts)

- *Qualification (0,5 pt).* L'opération est un **apport partiel d'actif** : VENTOUREL apporte à AGRÉSIA, société qui existe déjà, un ensemble d'actifs et de passifs qui forme une **branche autonome**, et reçoit **elle-même** en échange des actions nouvelles d'AGRÉSIA (et une soulte d'arrondi) ; elle n'est **pas dissoute** et garde son activité de mobilier urbain [V PCG art. 710-2, F01 § 1]. Son actif change de nature : la branche est remplacée par une participation dans AGRÉSIA.
- *Différence avec une fusion et une scission (0,5 pt).* Dans une **fusion**, la société qui transmet son patrimoine le transmet **en totalité**, est **dissoute sans liquidation**, et ce sont **ses associés** qui reçoivent les titres de l'absorbante [V C. com. L. 236-1 et L. 236-3 I, F01 § 1]. Dans une **scission**, la société transmet aussi la totalité de son patrimoine, mais à **plusieurs** sociétés, et disparaît [V C. com. L. 236-18, F01 § 1]. Ici, seule une partie du patrimoine est transmise, à une seule société, VENTOUREL subsiste et c'est elle qui reçoit les titres. Les deux sociétés ont choisi de soumettre l'apport au régime juridique des scissions (annexe 2.4), ce que permet le Code de commerce [V C. com. L. 236-27, F01 § 4] ; l'opération reste un apport partiel d'actif.
- *Branche complète d'activité (0,75 pt).* Une branche complète est l'ensemble des éléments d'actif et de passif d'une division qui forment, du point de vue de l'organisation, une **exploitation autonome**, capable de fonctionner par ses propres moyens ; elle s'apprécie dans l'organisation de l'apporteuse [V BOI-IS-FUS-20-20 § 10 à 90, F02 § 1]. La branche « aires de jeux » réunit :
  - des **installations propres** : l'atelier de Mazan, son terrain et ses machines, distincts de l'usine de mobilier urbain de Carpentras ;
  - un **personnel propre**, 38 salariés affectés à la seule branche (bureau d'études, fabrication, pose, vente, suivi des contrats), qui passe chez AGRÉSIA ;
  - une **clientèle** et des **contrats** propres : 260 clients actifs, 46 marchés et commandes en cours, la marque BALANDRIN ;
  - tous les éléments liés à l'exploitation : stocks, créances, dettes fournisseurs et sociales, emprunt qui a financé la cabine, provision pour les garanties données, sans patrimoine étranger à l'exploitation.
  Les services administratifs communs (comptabilité, paie, trésorerie, informatique) peuvent rester chez VENTOUREL sans être répartis [V BOI-IS-FUS-20-20 § 120]. Il ne s'agit pas d'éléments isolés (un atelier ou une marque seuls) : la branche est **complète**.
- *Référentiel (0,25 pt).* L'opération est enregistrée dans les **comptes individuels** des deux sociétés selon le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui vise les apports partiels d'actif rémunérés par des titres et retracés dans un traité d'apport, et fixe le mode d'évaluation des apports et leur inscription chez la bénéficiaire pour les valeurs du traité [V PCG art. 710-1, 720-1, F01 § 1].

---

### 2.2 Régime fiscal de faveur (2 pts)

- *Conditions (0,5 pt).*
  - Les deux sociétés sont des personnes morales **soumises à l'impôt sur les sociétés** [V CGI art. 210 C-1, F02 § 1].
  - L'opération est un apport partiel d'actif au sens fiscal : apport, sans dissolution, d'une **branche complète d'activité**, contre des titres représentatifs du capital de la bénéficiaire [V CGI art. 210-0 A, I, 4°, F02 § 1]. Le régime de l'art. 210 A s'applique alors **de plein droit**, **sans agrément** et, depuis le 01/01/2018, **sans engagement de conservation** des titres reçus [V CGI art. 210 B-1, BOI-IS-FUS-20-40, F02 § 1].
  - **Motifs économiques valables** [V CGI art. 210-0 A, III, F02 § 1] : recentrage de VENTOUREL sur le mobilier urbain, gamme complète d'AGRÉSIA pour les appels d'offres des communes.
  - La soulte, inférieure à la valeur d'une action AGRÉSIA, ne fait pas obstacle au régime (2.3 b).
- *Conséquences pour VENTOUREL (0,5 pt).*
  - La **plus-value d'apport** (1 493 000 €, 2.6 a) **n'est pas soumise à l'IS** [V CGI art. 210 A-1 et 210 B-1, F02 § 1 et § 2] : elle est en **sursis d'imposition**. Les résultats de la branche ne sont pas imposés immédiatement, et la provision pour garanties n'est imposée chez l'apporteuse que si elle est devenue sans objet [V BOI-IS-FUS-20-40-30 § 100 et 110, F02 § 1].
  - **Contrepartie** : la plus-value de cession future des **17 555 actions AGRÉSIA** sera calculée par référence à la **valeur fiscale des biens apportés** dans les écritures de VENTOUREL, soit **1 667 000 €** (valeurs fiscales égales aux valeurs nettes comptables, marque à 0), et non d'après leur valeur d'inscription de 3 159 900 € [V CGI art. 210 B-2, F02 § 1]. L'imposition de la plus-value est donc reportée, non effacée.
- *Engagements et obligations d'AGRÉSIA (0,5 pt)* [V CGI art. 210 A-3, F02 § 2 et § 4] :
  - reprendre à son passif la **provision pour garanties** de 48 000 €, dont l'imposition est différée (a) ;
  - **réintégrer** dans ses bénéfices imposables les plus-values sur les **biens amortissables** : l'atelier (construction) par parts égales sur **15 ans** (360 000 / 15 = **24 000 €** par an), les machines sur **5 ans** (180 000 / 5 = **36 000 €** par an) (d). La plus-value sur la construction représente 360 000 / 540 000 = 66,67 % de la plus-value nette sur les biens amortissables, moins de 90 % : la règle de la durée moyenne pondérée ne joue pas. En contrepartie, AGRÉSIA amortit ces biens sur leur valeur d'apport ;
  - calculer la plus-value de cession future des **biens non amortissables**, le **terrain** et la **marque**, d'après leur valeur fiscale chez VENTOUREL, soit 120 000 € et 0 € (c) ;
  - inscrire les **stocks** à leur valeur fiscale chez VENTOUREL (e) : leur valeur d'apport lui est égale, aucun écart.
- *Si la branche n'était pas complète (0,5 pt).* Le régime de faveur ne s'appliquerait que sur **agrément** de l'administration, délivré si l'opération est justifiée par un motif économique, se traduisant notamment par une activité autonome chez la bénéficiaire, et par un rapprochement durable entre les parties, formalisé par un **engagement de conservation des titres pendant trois ans**, si l'art. 210-0 A est respecté et si les modalités de l'opération assurent l'imposition future des plus-values en sursis [V CGI art. 210 B-3, F02 § 1]. À défaut d'agrément, le **droit commun** s'appliquerait : l'apport serait une cession partielle d'entreprise, VENTOUREL serait imposée immédiatement sur la plus-value (1 493 000 × 25 % = 373 250 €) et AGRÉSIA n'aurait aucune plus-value à réintégrer, donc aucune provision pour impôts à intégrer à l'apport [V BOI-IS-FUS-30-20 § 10, F02 § 2 et § 6].

---

### 2.3 Rémunération, soulte et répartition du capital (5 pts)

**a) Nombre d'actions et augmentation de capital (1 pt)**
- *Nombre exact (0,5 pt).* Dans un apport partiel d'actif, le nombre d'actions se déduit directement de la valeur d'échange des apports [V F01 § 4] : 3 160 000 / 180 = **17 555,56 actions**, nombre qui n'est pas entier. La valeur de la branche est celle du traité, quel que soit le mode d'évaluation des apports [V PCG art. 740-1, F01 § 1].
- *Projet de traité (0,5 pt).* Arrondi à l'unité inférieure : **17 555 actions** de 20 €, soit une **augmentation de capital de 351 100 €**.

**b) Soulte du projet de traité (2 pts)**
- *Soulte (0,5 pt).* 3 160 000 – 17 555 × 180 = 3 160 000 – 3 159 900 = **100 €**, versés par AGRÉSIA à VENTOUREL : c'est la valeur des 0,56 action qui ne peut être remise.
- *Équité (0,5 pt).* VENTOUREL reçoit 3 159 900 + 100 = **3 160 000 €**, exactement la valeur de la branche qu'elle apporte ; les associés d'AGRÉSIA ne cèdent pas plus de valeur qu'ils n'en reçoivent. Aucun transfert de valeur n'est organisé entre les sociétés [V BOI-IS-FUS-30-20 § 20 et 30, F02 § 1].
- *Limite légale (0,5 pt).* L'apport étant soumis au régime juridique des scissions (annexe 2.4), la soulte ne peut dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-27 et L. 236-18, al. 3, F01 § 4] : 10 % × 17 555 × 20 = **35 110 €**. La soulte de 100 € est **légale**.
- *Condition fiscale (0,5 pt).* Le régime de faveur des apports partiels d'actif est réservé aux apports qui ne procurent aucune liquidité à l'apporteuse ; il n'est pas refusé lorsque la soulte est **inférieure à la valeur d'une action** de la bénéficiaire (annexe 2.5) [V BOI-IS-FUS-20-20 § 130, F02 § 1]. 100 € < 180 € : la soulte **ne remet pas en cause le régime de faveur**.

**c) Variante à la centaine inférieure : conseil (1 pt)**
- *Calcul et limite légale (0,25 pt).* 17 500 actions (capital 350 000 €) et une soulte de 3 160 000 – 17 500 × 180 = **10 000 €**, au plafond légal de 10 % × 17 500 × 20 = 35 000 € : la variante resterait **légale** et l'échange équitable.
- *Effet fiscal (0,5 pt).* La soulte dépasserait largement la valeur d'une action (10 000 € pour 180 €) : VENTOUREL recevrait une liquidité que la tolérance n'admet pas, et l'apport risquerait de **perdre le régime de faveur** [V BOI-IS-FUS-20-20 § 130, F02 § 1]. La plus-value d'apport serait alors imposée immédiatement : 1 493 000 × 25 % = **373 250 €** d'IS en 2027, pour 10 000 € encaissés.
- *Conseil (0,25 pt).* Garder l'arrondi **à l'unité inférieure** du projet de traité (soulte de 100 €) : un « compte rond » ne justifie pas ce risque. Le respect du plafond légal ne suffit pas : la condition fiscale est ici plus stricte.

**d) Répartition du capital d'AGRÉSIA après l'opération (1 pt)**

| Associé | Actions | % du capital et des droits de vote |
|---|---:|---:|
| SAS BRAMEFAN Participations | 34 560 | 52,72 % |
| Cadres et salariés d'AGRÉSIA | 13 440 | 20,50 % |
| SAS VENTOUREL Équipements | 17 555 | 26,78 % |
| **Total** | **65 555** | **100 %** |

Tableau (0,5) ; commentaire (0,5) : BRAMEFAN Participations passe de 72 % à 52,72 % : elle est diluée mais **garde la majorité** des droits de vote et la désignation des dirigeants. VENTOUREL devient le deuxième associé avec **26,78 %**, sans pacte ni dirigeant désigné : elle est **minoritaire**. Le capital d'AGRÉSIA passe à 65 555 × 20 = 1 311 100 €.

---

### 2.4 Mode d'évaluation des apports (2 pts)

- *Situation de contrôle (0,75 pt).* Avant l'opération, aucune des deux sociétés ne détient d'actions de l'autre, et elles ne sont pas sous le contrôle d'une même entité : AGRÉSIA est contrôlée par la personne morale BRAMEFAN Participations (72 %), VENTOUREL par la famille LAUZERANDE, qui ne détient rien dans AGRÉSIA ni dans BRAMEFAN Participations (annexe 2.1). L'opération est réalisée **sous contrôle distinct** [V PCG art. 741-1 et 741-2, F01 § 2.1].
- *Sens de l'opération (0,5 pt).* VENTOUREL **perd le contrôle** de la branche, qui passe dans le patrimoine d'AGRÉSIA, et **ne prend pas le contrôle** de la bénéficiaire (26,78 %, 2.3 d), dont BRAMEFAN Participations garde la majorité (52,72 %) : l'apport est réalisé **à l'endroit** [V art. 742-1, F01 § 2.2]. La branche est la cible, AGRÉSIA l'initiatrice.
- *Mode d'évaluation (0,25 pt).* Apport **à l'endroit sous contrôle distinct** : **valeur réelle** [V art. 743-1, F01 § 2.3]. AGRÉSIA prend le contrôle d'une activité : l'opération est traitée comme une acquisition.
- *Si VENTOUREL recevait la majorité (0,5 pt).* VENTOUREL **prendrait le contrôle** d'AGRÉSIA : l'apport serait réalisé **à l'envers** [V art. 742-2, F01 § 2.2]. La cible serait alors AGRÉSIA, dont les actifs ne figurent pas au traité, et VENTOUREL garderait, à travers sa participation majoritaire, le contrôle de la branche qu'elle apporte : il n'y aurait pas lieu de réévaluer celle-ci, et les apports seraient inscrits à la **valeur comptable** [V art. 743-1, cas 3, F01 § 2.3]. Ici, il faudrait pour cela que la branche vaille plus qu'AGRÉSIA avant l'opération (48 000 × 180 = 8 640 000 €), soit près de trois fois sa valeur.

---

### 2.5 Valeur des apports et prime d'apport (6 pts)

**a) Éléments identifiés, provision pour impôts, fonds commercial et composition de l'apport (5 pts)**
- *Plus-values sur les éléments identifiés (1 pt).*

| Élément (en €) | Valeur nette comptable | Valeur réelle | Plus-value |
|---|---:|---:|---:|
| Terrain | 120 000 | 210 000 | 90 000 |
| Atelier de Mazan | 640 000 | 1 000 000 | 360 000 |
| Machines | 600 000 | 780 000 | 180 000 |
| Marque BALANDRIN (absente du bilan) | – | 300 000 | 300 000 |
| **Total** | | | **930 000** |

  La marque est un élément identifié inscrit à sa valeur réelle bien qu'elle ne figure pas au bilan de VENTOUREL [V PCG art. 744-1, F01 § 3.1]. Les autres éléments ont une valeur réelle égale à leur valeur au bilan.
- *Provision pour impôts (1,5 pt).*
  - **Atelier et machines** (1) : biens **amortissables** ; leurs plus-values, en sursis chez VENTOUREL, seront réintégrées dans le résultat imposable d'AGRÉSIA (2.2) : l'apport comprend un **passif d'impôt différé** de (360 000 + 180 000) × 25 % = 90 000 + 45 000 = **135 000 €**, inscrit en **provision pour impôts** [V art. 744-1, F01 § 3.3, F02 § 6].
  - **Terrain et marque** (0,5) : biens **non amortissables** ; leur plus-value ne sera imposée qu'en cas de cession, d'après leur valeur fiscale chez VENTOUREL, et AGRÉSIA n'envisage pas de les céder : selon la convention de l'énoncé (annexe 2.5), **aucun impôt différé** n'est calculé [F01 § 3.3]. La provision pour garanties, déjà déduite et reprise pour le même montant, n'en appelle pas non plus. Le fonds commercial, écart résiduel, ne donne lieu à aucun impôt différé [F01 § 3.3].
- *Actif net réel identifié (0,5 pt).* Actif net comptable de la branche : 2 340 000 – 673 000 = 1 667 000 € ; actif net réel identifié = 1 667 000 + 930 000 – 135 000 = **2 462 000 €**.
- *Fonds commercial (1 pt).* La valeur globale de la branche retenue par le traité (3 160 000 €) dépasse la somme algébrique des valeurs réelles des éléments identifiés : l'écart, 3 160 000 – 2 462 000 = **698 000 €**, est inscrit en **fonds commercial** (compte 207) [V art. 744-1, F01 § 3.1]. Il représente la clientèle, les marchés en cours et le savoir-faire de l'équipe, qui ne sont pas identifiables séparément.
- *Composition de l'apport (1 pt).*

| Élément (en €) | Valeur d'apport |
|---|---:|
| Marque BALANDRIN | 300 000 |
| Fonds commercial | 698 000 |
| Terrain | 210 000 |
| Atelier de Mazan | 1 000 000 |
| Machines | 780 000 |
| Matières premières | 260 000 |
| Produits finis | 180 000 |
| Clients | 540 000 |
| **Total des actifs** | **3 968 000** |
| Provision pour garanties | – 48 000 |
| Provision pour impôts | – 135 000 |
| Emprunt | – 320 000 |
| Fournisseurs | – 210 000 |
| Dettes provisionnées pour congés à payer | – 95 000 |
| **Valeur des apports** | **3 160 000** |

**b) Prime d'apport (1 pt)**

| Élément | Calcul | Montant (€) |
|---|---|---:|
| Valeur des apports | composition ci-dessus | 3 160 000 |
| Augmentation de capital | 17 555 × 20 | 351 100 |
| Soulte versée par AGRÉSIA | 2.3 b | 100 |
| **Prime d'apport** | 3 160 000 – 351 100 – 100 | **2 808 800** |

Contrôle : 17 555 × (180 – 20) = 2 808 800 €. La soulte, payée en espèces par AGRÉSIA, ne rémunère pas une part du capital : elle diminue la prime [V F01 § 4 et § 9].

---

### 2.6 Écritures au 31 mars 2027 (6 pts)

Toutes les écritures ci-dessous sont équilibrées.

**a) VENTOUREL (2,5 pts)**

**A1 — Apport de la branche (1,5 pt).** Sortie des actifs pour leur valeur brute et de leurs amortissements (0,5) ; sortie des passifs (0,25) ; créance sur AGRÉSIA pour la valeur d'apport (0,25) ; **plus-value d'apport** de 3 160 000 – 1 667 000 = 1 493 000 €, présentée en résultat exceptionnel (annexe 2.6) (0,5) [V PCG art. 1212-26, art. 513-5, F01 § 9]. La marque, absente du bilan, n'a pas à être sortie.

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – AGRÉSIA, compte d'apport | 3 160 000 | |
| 2813 Amortissements des constructions | 760 000 | |
| 2815 Amortissements des installations, matériel et outillage industriels | 1 050 000 | |
| 1512 Provisions pour garanties données aux clients | 48 000 | |
| 164 Emprunts auprès des établissements de crédit | 320 000 | |
| 401 Fournisseurs | 210 000 | |
| 4282 Dettes provisionnées pour congés à payer | 95 000 | |
| 211 Terrains | | 120 000 |
| 2131 Bâtiments | | 1 400 000 |
| 2154 Matériels industriels | | 1 650 000 |
| 31 Matières premières et fournitures | | 260 000 |
| 355 Produits finis | | 180 000 |
| 411 Clients | | 540 000 |
| 778 Autres produits exceptionnels (plus-value d'apport) | | 1 493 000 |
| **Total** | **5 643 000** | **5 643 000** |

**A2 — Réception des actions et de la soulte (0,5 pt).** Les titres reçus sont inscrits en titres de participation pour leur **valeur d'apport** [V PCG art. 1212-26, F01 § 9] : 17 555 × 180 = 3 159 900 € ; la soulte est encaissée.

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation (17 555 actions AGRÉSIA) | 3 159 900 | |
| 512 Banques (soulte) | 100 | |
| 467 Divers comptes débiteurs – AGRÉSIA, compte d'apport | | 3 160 000 |

**Traitement fiscal de la plus-value (0,5 pt).** Le **sursis d'imposition** ne se traduit pas en comptabilité : la plus-value de 1 493 000 € figure dans le résultat comptable de 2027, puis est **déduite de manière extra-comptable** pour le calcul du résultat imposable [V CGI art. 210 A-1, F02 § 1 ; déduction : conséquence directe, comme pour le boni exonéré, F02 § 2 bis]. VENTOUREL suit hors comptabilité la valeur fiscale des actions AGRÉSIA (1 667 000 €), qui servira au calcul de la plus-value de leur cession [V CGI art. 210 B-2, F02 § 1]. Aucune provision pour impôts n'est constatée chez VENTOUREL, qui ne comptabilise pas d'impôts différés.

**b) AGRÉSIA : augmentation de capital et réalisation des apports (2 pts)**

**A3 — Augmentation de capital et soulte (0,75 pt).** Capital et prime (0,5) ; soulte et compte d'apport (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (VENTOUREL) | 3 160 000 | |
| 101 Capital (17 555 × 20) | | 351 100 |
| 1043 Primes d'apport | | 2 808 800 |
| 512 Banques (soulte versée à VENTOUREL) | | 100 |

**A4 — Réalisation des apports à la valeur réelle (1,25 pt).** Actifs inscrits pour leur **valeur réelle**, qui devient leur valeur brute chez AGRÉSIA, sans reprise des amortissements de VENTOUREL, marque inscrite bien qu'absente du bilan de l'apporteuse (0,5) ; fonds commercial (0,25) ; provisions, dont la provision pour impôts, et dettes (0,25) ; compte d'apport crédité de la valeur des apports (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Concessions et droits similaires, brevets, licences, marques (marque BALANDRIN) | 300 000 | |
| 207 Fonds commercial | 698 000 | |
| 211 Terrains | 210 000 | |
| 2131 Bâtiments (atelier de Mazan) | 1 000 000 | |
| 2154 Matériels industriels | 780 000 | |
| 31 Matières premières et fournitures | 260 000 | |
| 355 Produits finis | 180 000 | |
| 411 Clients (dont créance sur AGRÉSIA 36 000) | 540 000 | |
| 1512 Provisions pour garanties données aux clients | | 48 000 |
| 1523 Provisions pour impôts | | 135 000 |
| 164 Emprunts auprès des établissements de crédit | | 320 000 |
| 401 Fournisseurs | | 210 000 |
| 4282 Dettes provisionnées pour congés à payer | | 95 000 |
| 4561 Associés – Comptes d'apport en société (VENTOUREL) | | 3 160 000 |
| **Total** | **3 968 000** | **3 968 000** |

**c) AGRÉSIA : écritures complémentaires (1,5 pt)**

**A5 — Frais de l'opération (0,75 pt).** Les frais d'augmentation de capital peuvent être imputés sur la prime [V PCG art. 212-9, F01 § 7], pour leur montant **net d'impôt**, comme le prévoit l'annexe 2.6 [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 40 000 × 75 % = **30 000 €** sur la prime, économie d'impôt de 10 000 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 1043 Primes d'apport | 30 000 | |
| 444 État – Impôts sur les bénéfices | 10 000 | |
| 512 Banques | | 40 000 |

Prime d'apport après l'opération : 2 808 800 – 30 000 = **2 778 800 €**.

**A6 — Dette d'AGRÉSIA envers VENTOUREL (0,75 pt).** Avec la branche, AGRÉSIA reçoit la créance de 36 000 € que la branche détenait **sur AGRÉSIA elle-même** : réunissant les qualités de créancier et de débiteur de la même obligation, elle l'**éteint par confusion** [V C. civ. art. 1349, F01 § 8]. La dette d'AGRÉSIA est annulée en même temps que la créance reçue ; chez VENTOUREL, la créance est sortie avec les autres clients de la branche (A1), sans autre écriture.

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette envers VENTOUREL) | 36 000 | |
| 411 Clients (créance de la branche reçue avec l'apport) | | 36 000 |

---

### 2.7 Note à M. LAUZERANDE, président de VENTOUREL (2 pts)

*Objet : effets de l'apport de la branche « aires de jeux » sur les comptes de VENTOUREL.*

| Poste (en €) | Avant | Apport | Après |
|---|---:|---:|---:|
| Immobilisations corporelles nettes | 4 150 000 | – 1 360 000 | 2 790 000 |
| Titres de participation (AGRÉSIA) | – | + 3 159 900 | 3 159 900 |
| Stocks | 1 020 000 | – 440 000 | 580 000 |
| Clients | 1 480 000 | – 540 000 | 940 000 |
| Disponibilités | 650 000 | + 100 | 650 100 |
| **Total de l'actif** | **7 300 000** | **+ 820 000** | **8 120 000** |
| Capitaux propres | 3 900 000 | + 1 493 000 | 5 393 000 |
| Provisions pour risques | 110 000 | – 48 000 | 62 000 |
| Emprunts | 1 840 000 | – 320 000 | 1 520 000 |
| Fournisseurs | 860 000 | – 210 000 | 650 000 |
| Dettes fiscales et sociales | 590 000 | – 95 000 | 495 000 |

- *Actif (0,5 pt).* La branche (2 340 000 € d'actifs nets d'amortissements, 673 000 € de passifs) est remplacée par **17 555 actions AGRÉSIA** inscrites pour **3 159 900 €**, qui deviennent le premier poste de l'actif (38,92 %). Ce placement n'est pas coté et ne produit de trésorerie que par les dividendes d'AGRÉSIA ou sa cession.
- *Résultat de 2027 (0,5 pt).* Il comprend un **produit exceptionnel de 1 493 000 €**, la plus-value d'apport. Ce produit n'entraîne aucune entrée de trésorerie (100 € de soulte), ne se renouvellera pas et n'est pas imposé en 2027 (sursis) : l'impôt est reporté sur la cession future des titres, dont la valeur fiscale reste de 1 667 000 €. Il faudra l'isoler pour apprécier la rentabilité du mobilier urbain, qui sera désormais la seule activité de VENTOUREL ; et le distribuer réduirait la trésorerie alors qu'il n'a rien encaissé.
- *Capitaux propres (0,25 pt).* Ils passent de 3 900 000 € à **5 393 000 €** (+ 38,28 %), plus-value d'apport comprise dans le résultat de la période, sans entrée de trésorerie.
- *Position au capital d'AGRÉSIA (0,25 pt).* Avec **26,78 %**, VENTOUREL est le deuxième associé d'AGRÉSIA mais reste **minoritaire** : BRAMEFAN Participations garde 52,72 % et désigne seule les dirigeants. VENTOUREL ne décide ni de la gestion de son ancienne branche ni des dividendes ; elle peut négocier une place dans les organes d'AGRÉSIA ou un pacte, qui ne sont pas prévus.
- *Banque (0,25 pt).* L'emprunt de la cabine (320 000 €) sort du bilan : les emprunts passent de 1 840 000 € à 1 520 000 €, et leur rapport aux capitaux propres de 0,47 à 0,28. Mais une partie de l'actif productif et des créances clients est remplacée par une participation minoritaire non cotée, moins facile à mobiliser en garantie, et le chiffre d'affaires de VENTOUREL diminue : la banque appréciera la capacité de remboursement sur la seule activité de mobilier urbain.
- *Personnel de la branche (0,25 pt).* Les **38 salariés** de la branche passent chez AGRÉSIA avec l'atelier et les contrats en cours ; les congés acquis (95 000 €) sont repris par AGRÉSIA. Ils rejoignent une entreprise plus grande sur un marché proche ; VENTOUREL conserve 66 salariés.

---

### Réponses tolérées
- **2.1** : branche complète démontrée avec les seuls critères de l'autonomie (installations, personnel, clientèle), si les éléments du cas sont cités.
- **2.2** : sursis présenté comme une « exonération sous condition » si la contrepartie (valeur fiscale des titres, 210 B-2) est indiquée ; réintégrations présentées en total (60 000 € par an pendant cinq ans, puis 24 000 € par an).
- **2.3 a** : nombre exact arrondi à 17 556 si le candidat relève que le traité arrondit à l'unité inférieure et retient 17 555.
- **2.3 b** : plafond légal vérifié avec la règle de la fusion (C. com. L. 236-1), même limite de 10 % du nominal des titres attribués.
- **2.3 c** : conseil fondé sur le seul risque fiscal, si le respect du plafond légal est vérifié.
- **2.4** : contrôle distinct justifié par l'absence de lien entre les familles BRAMEFAN et LAUZERANDE, si le contrôle de BRAMEFAN Participations sur AGRÉSIA est relevé.
- **2.5 a** : impôt différé calculé sur le total des plus-values amortissables ; marque inscrite dans un sous-compte du 205.
- **2.6 a** : A1 et A2 réunies, ou titres inscrits pour 3 160 000 € si la soulte est portée en déduction ; plus-value inscrite dans un sous-compte du 778 ; écriture de l'apporteuse sans compte d'apport (titres et banque débités directement).
- **2.6 b** : soulte inscrite d'abord au crédit d'un compte 467, puis réglée par le 512 ; dettes provisionnées pour congés à payer ventilées entre 4282 et 4382 ; A3 et A4 réunies.
- **2.6 c** : créance de 36 000 € retirée dès la réalisation des apports (clients repris pour 504 000 €, dette fournisseurs d'AGRÉSIA diminuée directement), sans écriture A6 distincte, si la confusion est expliquée.
- **2.7** : capitaux propres présentés sans la plus-value, si le candidat le signale et chiffre son effet à part.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime d'apport calculée sans déduire la soulte (2 808 900 €), sur l'actif net comptable (1 667 000 – 351 100 = 1 315 900 €) ou sur l'actif net réel identifié sans le fonds commercial ; frais imputés pour leur montant brut (40 000 €).
- `JUR-R05` Difficulté à s'adapter à l'apport partiel d'actif : actions attribuées aux associés de VENTOUREL au lieu de VENTOUREL elle-même ; parité calculée entre deux valeurs unitaires alors que le nombre d'actions se déduit de la valeur de la branche ; plafond de la soulte jugé suffisant pour conclure sur le régime fiscal (2.3 c) ; sens de l'opération apprécié sur le pourcentage de la famille LAUZERANDE dans VENTOUREL.
- `JUR-F07` Annexes mal exploitées : marque oubliée parce qu'elle ne figure pas au bilan de VENTOUREL ; impôt différé calculé sur le terrain et la marque malgré la convention de l'annexe 2.5, ou sur le fonds commercial ; provision pour impôts omise ; créance réciproque de 36 000 € non éliminée.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1 et A4.
- Erreurs propres à ce cas : amortissements de VENTOUREL repris chez AGRÉSIA alors que les apports sont à la valeur réelle ; plus-value d'apport non constatée chez VENTOUREL, ou titres inscrits à la valeur nette comptable de la branche ; plus-value présentée comme définitivement exonérée, sans la contrepartie de l'art. 210 B-2 ; engagement de conservation des titres de trois ans imposé alors que la branche est complète ; provision pour impôts constatée chez VENTOUREL.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 710-1, 710-2, 720-1, 740-1 | Champ du titre VII, définition de l'apport partiel d'actif, inscription des apports pour les valeurs du traité, rémunération sur les valeurs d'échange | [V] p. 81-82 | F01 § 1 |
| C. com. L. 236-1, L. 236-3 I, L. 236-18 | Fusion, dissolution sans liquidation, scission ; soulte limitée à 10 % de la valeur nominale des titres attribués | [V] Légifrance | F01 § 1 et § 4 |
| C. com. L. 236-27 | Apport partiel d'actif soumis, d'un commun accord, au régime des scissions (section 2) | [V] `DSC-200/ccom.xml`, lu le 22/11/2026 | F01 § 4 |
| PCG art. 741-1, 741-2, 742-1, 742-2, 743-1 | Contrôle distinct, apport à l'endroit et à l'envers, valeur réelle ou comptable | [V] p. 82-84 | F01 § 2 |
| PCG art. 744-1 | Valeur réelle des éléments identifiés, figurant ou non au bilan (marque, impôts différés), fonds commercial | [V] p. 85 | F01 § 3.1 et § 3.3 |
| Convention de l'énoncé (annexe 2.5) | Aucun impôt différé sur la plus-value d'un bien non amortissable dont la cession n'est pas envisagée | Convention du corrigé du sujet zéro, à poser en hypothèse | F01 § 3.3 |
| PCG art. 1212-26, 513-5 ; compte 778 | Titres reçus à la valeur d'apport ; résultat d'apport présenté en résultat exceptionnel (convention de l'énoncé) | [V] p. 160, p. 42-43 | F01 § 9 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion de la dette réciproque | [V] | F01 § 8 |
| CGI art. 210-0 A (I, 4° ; III), 210 A-1, 210 A-3, 210 B-1, 210 B-2, 210 B-3, 210 C-1 ; BOI-IS-FUS-20-40 | Définition fiscale de l'apport partiel, motif économique, sursis d'imposition, engagements de la bénéficiaire et réintégration sur 15 et 5 ans, plein droit sans engagement de conservation, valeur fiscale des titres reçus, agrément | [V] | F02 § 1, § 2 et § 4 |
| BOI-IS-FUS-20-20 § 10 à 130 ; BOI-IS-FUS-20-40-30 § 100 et 110 | Branche complète d'activité, services communs, soulte inférieure à la valeur d'une action ; résultats et provisions de la branche | [V] jeu `bofip-vigueur` | F02 § 1 |
| BOI-IS-FUS-30-20 § 10, 20 et 30 | Imposition en droit commun, rémunération sur les valeurs réelles, transferts de valeur | [V] | F02 § 1 et § 6 |
| Comptes 467 et 778 (apporteuse) | Compte d'apport, plus-value d'apport | Convention de rédaction (le PCG ne donne pas d'écriture pour l'apporteuse) | F01 § 9 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Conditions d'exercice, instances et assurance de l'expert-comptable ; responsabilités civile et disciplinaire du cabinet RIVOLANE, distinguées de la responsabilité pénale | `3.1.a` Cadres d'exercice professionnel ; `3.1.e` Mise en cause de la responsabilité | 4 |
| 3.2 Fin normale du mandat, choix du successeur, récusation et ses motifs | `3.1.b` Nomination et cessation | 2 |
| 3.3 Documentation des prix de transfert et représentation devant l'administration : impartialité, autorévision | `3.1.c` Principes déontologiques | 1,5 |
| 3.4 Certification des comptes annuels de la filiale et intervention pour l'auditeur du groupe | `3.2.a` Notion d'audit | 1,5 |
| 3.5 Risques et assertions du cycle des ventes et des créances ; procédures ; procédure analytique de substance et extraits de normes | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit ; `3.1.d` Référentiel normatif (NEP) | 5,5 |
| 3.6 Investigations auprès de la société mère et d'une autre filiale ; suite d'un refus | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.7 Anomalies, écritures, caractère significatif, opinion selon la correction, parties du rapport | `3.2.e` Portée des opinions | 2 |
| 3.8 Emplacement de l'état de durabilité, renvois, informations spécifiques à l'entité | `3.3.a` Contexte et normes de durabilité | 3 |
| 3.9 Impacts, risques et opportunités ; matérialité d'impact et matérialité financière ; connectivité avec les comptes | `3.3.b` Principes de construction du reporting | 3 |
| 3.10 Objectifs, axes et assurance limitée ; étapes ; procédures sur deux données | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4 |
| 3.11 Avis en cas de limitation ou de correction ; différences avec l'opinion sur les comptes | `3.4.c` Portée des avis | 2 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 L'expert-comptable : cadre d'exercice et responsabilités (4 pts)

**a. Qui encadre la profession d'expert-comptable (2 pts)**

*Conditions d'exercice (0,75 pt)*
- Nul ne peut porter le titre d'expert-comptable ni exercer la profession s'il n'est **inscrit au tableau de l'ordre** [V ord. 45-2138 art. 3 I]. L'inscription suppose la jouissance des droits civils, l'absence de condamnation entachant l'honorabilité, le **diplôme d'expertise comptable** (ou l'une des voies dérogatoires prévues) et des garanties de moralité [V ord. art. 3 II].
- Un cabinet comme RIVOLANE Expertise exerce sous la forme d'une **société d'expertise comptable**, inscrite au tableau, dont plus des deux tiers des droits de vote sont détenus par des experts-comptables et dont les représentants légaux sont des professionnels [V ord. art. 7 I-II].
- L'activité est incompatible avec toute occupation de nature à porter atteinte à l'indépendance, avec un emploi salarié hors de la profession et avec une activité commerciale autre qu'accessoire [V ord. art. 22]. L'expert-comptable exerce avec compétence, conscience professionnelle et indépendance d'esprit [V décret 2012-432 art. 142, 145] ; il passe avec son client un contrat écrit, la lettre de mission [V décret art. 151].

*Instances de l'ordre (0,75 pt)*
- Les **conseils régionaux** de l'ordre, élus, tiennent le tableau et statuent sur les inscriptions ; ils ont seuls qualité pour **surveiller l'exercice de la profession** dans leur circonscription ; ils concilient les différends professionnels [V ord. art. 28, 31, 40].
- Le **conseil national**, à la tête de l'ordre, réunit les présidents des conseils régionaux et des membres élus ; il assure la défense de l'honneur et de l'indépendance de la profession et peut exercer les droits de la partie civile pour les faits qui portent atteinte à l'intérêt collectif de la profession [V ord. art. 1, 33, 37].
- Réponse à la présidente : l'expert-comptable relève de l'**ordre des experts-comptables**, et non de la Haute autorité de l'audit, compétente pour les commissaires aux comptes ; la NOUGATERIE peut porter les faits à la connaissance du conseil régional dont relève le cabinet de Valence, chargé de surveiller l'exercice de la profession [S, application].

*Assurance (0,5 pt)*
- Les experts-comptables sont tenus de souscrire un **contrat d'assurance** garantissant leur responsabilité civile [V ord. art. 17 al. 1] ; garantie minimale de **500 000 € par sinistre** et de **1 000 000 € par année d'assurance** et par assuré ; les franchises ne sont pas opposables aux tiers ; un contrat souscrit par le conseil national joue à titre subsidiaire [V décret 2012-432 art. 134, 138 ; ord. art. 17 al. 2].
- Le préjudice de la NOUGATERIE (au plus 22 500 €, ci-dessous) est très inférieur à la garantie : son indemnisation est assurée si la responsabilité du cabinet est établie [S].

**b. Ce que la NOUGATERIE peut reprocher au cabinet RIVOLANE et en obtenir (2 pts)**

*Responsabilité civile (1,25 pt : fondement 0,25 ; faute 0,25 ; préjudice 0,5 ; lien de causalité et conclusion 0,25)*
- **Fondement** : les professionnels de l'expertise comptable assument la responsabilité de leurs travaux ; la responsabilité de la société d'expertise comptable laisse subsister celle de l'expert-comptable qui a exécuté les travaux [V ord. art. 12 al. 3]. Envers sa cliente, la responsabilité est **contractuelle** : réparation du dommage causé par l'inexécution de la lettre de mission [V C. civ. 1231-1 ; S, application à l'expert-comptable]. Elle tend à des **dommages-intérêts**.
- **Faute** : l'expert-comptable est en principe tenu d'une obligation de moyens [S, qualification doctrinale] ; mais le dépôt dans le délai d'une déclaration que la lettre de mission lui confie, à partir de pièces reçues à temps, est une prestation précise, et l'absence de remplacement de la collaboratrice est un défaut d'organisation du cabinet : la faute est caractérisée [S]. Le cabinet n'a pas non plus alerté sa cliente du risque, alors qu'il lui doit information et conseil [V décret art. 155 ; S, application].
- **Préjudice** : la **taxe de 214 000 €** était due en tout état de cause (annexe 3.2) : son paiement n'est pas un dommage. Le préjudice réparable est la **majoration de 21 400 €** et, au plus, les **intérêts de retard de 1 100 €**, discutés puisque la société a conservé la trésorerie pendant le retard : **22 500 € au plus**, et non 236 500 € [S].
- **Lien de causalité** : les pièces ont été transmises le 06/10/2026, dans le délai prévu ; le retard est imputable au seul cabinet [S]. **Conclusion** : la NOUGATERIE peut demander au cabinet, et à travers lui à son assureur, la réparation de 21 400 € à 22 500 €, de préférence à l'amiable ; l'action se prescrit par cinq ans à compter du jour où elle a connu les faits [V C. civ. 2224 ; S, défaut de texte spécial].

*Responsabilité disciplinaire et responsabilité pénale (0,75 pt : disciplinaire 0,5 ; pénale 0,25)*
- **Disciplinaire** : elle sanctionne le manquement de l'expert-comptable à ses devoirs professionnels (compétence, conscience professionnelle) [V décret art. 142, 145 ; S, qualification] ; les peines sont la réprimande, le blâme, la suspension (avec ou sans sursis) et la radiation du tableau [V ord. art. 53]. Elle relève de l'ordre et **ne répare pas** le dommage de la cliente : aucune somme ne peut en être obtenue. Une radiation pour un retard isolé, dû à une absence non remplacée, serait disproportionnée [S].
- **Pénale** : elle suppose une **infraction** prévue par un texte, punie d'une amende ou d'une peine d'emprisonnement ; pour l'expert-comptable, les textes visent notamment l'exercice illégal de la profession et l'usage abusif du titre, et la violation du secret professionnel [V ord. art. 20, 21]. Une négligence dans le dépôt d'une déclaration n'est pas une infraction : la demande de « punition pénale » est sans fondement [S].

**Réponses tolérées**
- Un préjudice limité à la seule majoration (21 400 €), ou comprenant les intérêts de retard (22 500 €), si la taxe de 214 000 € est écartée : points complets.
- L'omission des montants de garantie de l'assurance, si son caractère obligatoire est indiqué : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Confondre les instances de l'expert-comptable et celles du commissaire aux comptes (H2A, CNCC), ou présenter les instances sans répondre à la présidente (`JUR-A05`).
- Inclure la taxe due dans le préjudice, ou attendre une indemnisation de la sanction disciplinaire (`JUR-A06`).
- Mélanger responsabilité civile, disciplinaire et pénale (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 1, 3, 7, 12, 17, 20-22, 28, 31, 33, 37, 40, 53 ; décret 2012-432 art. 134, 138, 142, 145, 151, 155 | Conditions d'exercice ; instances ; assurance ; responsabilités ; sanctions | [V] | F09 § 2, § 7, § 17 ; F10 § 2.2, § 4.3 |
| C. civ. 1231-1, 2224 | Responsabilité contractuelle ; prescription | [V] ; application à l'expert-comptable et obligation de moyens : [S] | F09 § 7.1 |

### 3.2 Fin du mandat, successeur et récusation (2 pts)

**Terme du mandat et choix du successeur (1 pt)**
- **Terme (0,5 pt)** : désigné en 2021 pour six exercices, le cabinet voit ses fonctions expirer **après la décision des associés qui statue sur les comptes de 2026**, prévue le 17/06/2027 [V L. 821-44 al. 1]. La NOUGATERIE reste tenue d'avoir un commissaire aux comptes : elle dépasse les trois seuils (total du bilan de 29,85 M€, chiffre d'affaires de près de 35 M€, 165 salariés en moyenne), alors que deux suffisent [V L. 227-9-1 al. 2 ; D. 221-5]. S'il est proposé de ne pas le renouveler, le cabinet est **entendu**, s'il le demande, par les associés [V L. 821-51].
- **Choix du successeur (0,5 pt)** : dans une SAS, la nomination des commissaires aux comptes est une décision **collective des associés**, prise dans les conditions des statuts [V L. 227-9 al. 2 ; L. 821-40 I] : ici à la majorité des voix, donc par BRUXOLIA (85 %), qui peut proposer SABLONIÈRE Audit France ; la famille, avec 15 %, ne peut s'y opposer. Avant d'accepter, le successeur vérifie et consigne son indépendance et ses moyens, **analyse les services rendus par lui ou son réseau** à la NOUGATERIE ou à la société qui la contrôle, notamment les risques d'autorévision, et en informe les associés [V L. 821-4 II ; code de déontologie art. 21, 22 I] ; il s'assure auprès du cabinet MÉJANEL que le non-renouvellement ne vise pas à contourner les obligations légales [V code de déontologie art. 26 I], et MÉJANEL lui donne accès aux informations et documents pertinents [V L. 821-44 al. 3].

**Récusation (1 pt : titulaires et moment 0,25 ; argument 2 : 0,25 ; argument 1 : 0,5)**
- **Titulaires et moment** : la récusation est demandée **en justice**, pour **juste motif**, par des associés représentant au moins **5 % du capital** (la famille, avec 15 %, le peut), le comité d'entreprise ou le ministère public [V L. 821-49 al. 1]. Elle vise un commissaire aux comptes **désigné** : la famille ne peut agir « dès maintenant » ; elle le pourra après la décision des associés, dans le délai fixé par décret, de trente jours à compter de la désignation [V L. 821-49 al. 1 ; R. 821-176]. Si la demande aboutit, un commissaire aux comptes est désigné en justice jusqu'à une nouvelle désignation par les associés [V L. 821-49 al. 4].
- **Argument 2** (contestation d'une méthode de comptabilisation chez une autre filiale) : une divergence d'appréciation sur un traitement comptable **ne peut constituer un motif fondé** de récusation [V L. 821-49 al. 3]. Elle témoigne plutôt de l'esprit critique attendu d'un commissaire aux comptes [S].
- **Argument 1** (réseau de l'auditeur du groupe) : l'appartenance à ce réseau n'est pas en soi un juste motif. Le commissaire aux comptes est indépendant de l'entité et des entités qui la contrôlent, en réalité et en apparence ; il exerce une mission d'intérêt général et ne « travaille » ni pour la mère ni pour les minoritaires [V code de déontologie art. 1er I, 5 ; S, application]. En revanche, SABLONIÈRE Conseil, membre du même réseau, a conçu la **politique de prix de transfert** que la NOUGATERIE applique à ses achats et à sa redevance de marque : le successeur aurait à apprécier, dans les comptes, des charges qui résultent des travaux de son réseau. C'est un **risque d'autorévision** qu'il doit analyser avant d'accepter ; sans sauvegarde appropriée, il ne peut accepter la mission [V code de déontologie art. 19 I 2°, 22 I ; L. 821-28 IV]. Ce fait précis, et non l'appartenance au réseau, est l'argument que le juge pourrait retenir comme juste motif, s'il est établi que le risque n'a pas été traité [S].

**Réponses tolérées**
- La mention du délai de trente jours sans autre détail, ou de la seule « demande en justice après la désignation » : points complets.
- L'idée que la famille peut demander à être informée des services rendus par le réseau du successeur : sans points supplémentaires.

**Erreurs fréquentes**
- Confondre la récusation avec le relèvement de fonctions, ou décrire la procédure devant le tribunal (`JUR-A01`).
- Croire que des minoritaires peuvent empêcher la désignation, ou qu'une récusation peut viser un candidat non encore désigné (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 227-9, L. 227-9-1, D. 221-5, L. 821-40 I, L. 821-44, L. 821-49, L. 821-51, R. 821-176 | Désignation dans une SAS ; terme ; récusation ; audition | [V] | F09 § 3.3, § 3.7, § 21 |
| Code de déontologie art. 1er, 5, 19, 21, 22, 26 ; L. 821-4 II, L. 821-28 IV | Indépendance ; autorévision ; acceptation ; prédécesseur | [V] ; juste motif : [S] | F09 § 12, § 21 ; F10 § 3, § 17 |

### 3.3 Documentation des prix de transfert et représentation de la NOUGATERIE (1,5 pt)

**Cadre (0,5 pt)**
- Le code de déontologie s'applique au commissaire aux comptes **quelle que soit la nature des missions ou des prestations** qu'il fournit [V code de déontologie art. 1er II 1°] : le fait que MÉJANEL soit aussi une société d'expertise comptable ne change rien. La NOUGATERIE n'étant pas une entité d'intérêt public, il n'existe pas de liste fermée de services interdits ; le cabinet ne peut accepter une prestation qui crée un **risque d'autorévision** ou compromet son **indépendance** sans mesure de sauvegarde appropriée [V L. 821-28 IV ; A. 821-55 § 22-30].
- L'indépendance et l'**impartialité** s'apprécient en réalité et **en apparence**, aux yeux d'un tiers objectif, raisonnable et informé ; le commissaire aux comptes évite toute situation qui pourrait laisser penser qu'il cherche à satisfaire un intérêt particulier [V code de déontologie art. 4, 5 I-II ; A. 821-54 § 16].

**Demande 1 : documentation des prix de transfert (0,5 pt)**
- La documentation justifierait les prix des amandes et du miel facturés par la centrale du groupe et le taux de la redevance de marque (2 % des ventes, soit environ 718 000 € sur les ventes avant remises de 2026 [S, calcul]) : ce sont des **charges des comptes** que le cabinet certifie, et la documentation fonde aussi l'appréciation du risque fiscal attaché à ces prix. Le cabinet se prononcerait sur des éléments résultant de sa propre prestation : **autorévision** [V code de déontologie art. 5 II, 19 I 2°].
- Aucune sauvegarde ne paraît suffisante au sein du même cabinet (une équipe distincte n'efface pas l'apparence d'autorévision aux yeux du tiers) : **refus** [S, application de A. 821-55 § 28-30].

**Demande 2 : représentation devant l'administration fiscale (0,5 pt)**
- Défendre les positions de l'entité dans un contrôle ferait du cabinet le **défenseur de ses intérêts** dans un différend dont il devrait ensuite apprécier l'issue dans les comptes (risque fiscal, provision éventuelle) : atteinte à l'impartialité, **conflit d'intérêts** perçu par le tiers et nouveau risque d'autorévision [V code de déontologie art. 4, 5, 19 I 2° ; S, application]. La demande vient en outre du groupe (« nos positions ») : l'intérêt de la société mère peut diverger de celui de la NOUGATERIE et de ses associés minoritaires [S].
- **Réponse** : refus écrit des deux prestations, motivé et documenté [V A. 821-55 § 24, § 30, § 41-43] ; le groupe peut confier la documentation et la défense à un autre professionnel ; le cabinet examinera la documentation comme un élément probant, avec esprit critique [S].

**Réponses tolérées**
- Le refus de la seule demande 2, si la demande 1 est acceptée à condition d'être limitée à une revue de cohérence sans établissement des analyses : 0,25 pt sur 0,5 pour la demande 1.

**Erreurs fréquentes**
- Réciter les principes du code sans les appliquer aux deux demandes, ou appliquer la liste des services interdits aux entités d'intérêt public (`JUR-A05`).
- Confondre l'indépendance d'esprit de l'expert-comptable, compatible avec le conseil, et l'indépendance du commissaire aux comptes (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 1er II, 4, 5, 19 ; A. 821-54 § 16-19 ; A. 821-55 § 22-30, § 41-43 ; L. 821-28 IV | Impartialité ; indépendance ; autorévision ; démarche risques et sauvegardes ; documentation | [V] ; application : [S] | F10 § 3, § 12, § 17 |

### 3.4 Certification des comptes annuels et intervention pour l'auditeur du groupe (1,5 pt)

**Certification des comptes annuels de la NOUGATERIE (0,5 pt)**
- **Mission légale** confiée par les associés : le cabinet certifie, en justifiant de ses appréciations, que les comptes annuels sont réguliers et sincères et donnent une image fidèle du résultat, de la situation financière et du patrimoine [V L. 821-53 al. 1] ; référentiel : le **plan comptable général** ; normes : les **NEP** ; seuil de signification fixé par le cabinet (250 000 €) ; **assurance raisonnable** que les comptes pris dans leur ensemble ne comportent pas d'anomalies significatives ; **opinion** dans un rapport destiné aux associés, sous la seule responsabilité du cabinet [V NEP principes § 01, 08 ; NEP rapport § 08 ; R. 821-180].

**Intervention demandée par SABLONIÈRE Réviseurs (0,75 pt)**
- **Objet** : la liasse de consolidation, établie selon les principes du groupe (IFRS), et non les comptes annuels ; **seuil** fixé par l'auditeur du groupe (400 000 €) ; **destinataire** : l'auditeur du groupe, qui l'utilise comme un élément de sa propre certification des comptes consolidés de BRUXOLIA et en conserve seul la responsabilité [S, principe ; en droit français, la certification des comptes consolidés est délivrée notamment après examen des travaux des commissaires aux comptes des entités consolidées : V L. 821-53 al. 2-3].
- Pour MÉJANEL, ce n'est pas une mission confiée par la loi française, mais une **prestation** : elle suppose l'accord de la NOUGATERIE, une **lettre de mission** préalable précisant les engagements et les honoraires, et l'analyse de son incidence sur l'indépendance [V L. 821-2 IV ; R. 821-195 ; A. 821-55 § 15 ; S, qualification].

**Articulation (0,25 pt)** : les deux interventions portent sur les mêmes opérations, mais leurs référentiels, leurs seuils, leurs destinataires et leurs calendriers diffèrent : une conclusion transmise le 05/02/2027 ne préjuge pas de l'opinion sur les comptes annuels, rendue le 14/04/2027 [S]. Point d'attention : la levée du secret professionnel prévue entre commissaires aux comptes de la société consolidante et des sociétés consolidées ne vise, à la lettre, que des commissaires aux comptes ; pour un auditeur étranger, le cadre de la transmission est à sécuriser avant de répondre [V L. 821-35 al. 3 ; application à un auditeur étranger : ?].

**Réponses tolérées**
- La présentation de l'intervention comme un audit contractuel de la liasse : points complets, si son caractère de prestation et la lettre de mission sont indiqués.

**Erreurs fréquentes**
- Décrire la démarche de l'auditeur du groupe sur des comptes consolidés (non demandée), ou confondre les deux référentiels (`JUR-A01`).
- Répondre directement à l'auditeur du groupe sans l'accord de la NOUGATERIE ni lettre de mission (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-2 IV, L. 821-35, L. 821-53, R. 821-180, R. 821-195 ; NEP principes § 01, 08 ; NEP rapport § 08 ; A. 821-55 § 15 | Certification ; prestation ; lettre de mission ; secret | [V] ; qualification de l'intervention : [S] | F11 § 1, § 26.3 ; F09 § 21 |

### 3.5 Cycle des ventes et des créances clients (5,5 pts)

**a. Risques d'anomalies significatives et assertions (2 pts ; 0,25 pt par risque correctement relié à ses assertions, dans la limite de 2 pts)**

Faute de revue du calcul des remises par la direction (annexe 3.5 § 8), le cabinet ne s'appuie pas sur les procédures de l'entité : son évaluation du risque au niveau des assertions correspond au risque inhérent [V NEP risques § 41].

| Risque | Origine dans l'annexe 3.5 | Assertions |
|---|---|---|
| Remises de fin d'année sous-estimées | Taux par tranche appliqué à la totalité du chiffre d'affaires ; calcul fondé sur des prévisions d'octobre, alors que 58 % des ventes se font au quatrième trimestre ; aucune revue ; barèmes de trois centrales connus par un simple tableau | Exhaustivité et mesure des remises (709) ; exhaustivité et évaluation des avoirs à établir (4198) |
| Ventes de fin décembre enregistrées sans livraison effective dans l'exercice | Livraisons du 28 au 31/12 (1 840 000 €), bons de livraison parfois signés le lendemain | Réalité et séparation des exercices des ventes ; existence des créances |
| Retours d'invendus sous-estimés | Avoir à établir estimé (96 000 €) sur des retours passés, plafond contractuel de 3 % | Mesure des ventes ; évaluation et exhaustivité de l'avoir à établir |
| Ventes en ligne payées avant leur expédition, enregistrées dans le mauvais exercice | Paiement à la commande ; 138 000 € de commandes payées en décembre, expédiées en janvier | Séparation des exercices ; classification des sommes reçues (avances des clients) |
| Créance sur LAGARDEL Distribution insuffisamment dépréciée | Aucun règlement depuis le 15/11/2026 ; dépréciation forfaitaire de 10 % | Évaluation des créances ; présentation (compte 416) |
| Créances anciennes | 370 000 € échus depuis plus de 60 jours | Existence ; évaluation |
| Forte saisonnalité et volume de fin d'année | 58 % des ventes d'octobre à décembre | Risque inhérent élevé sur la séparation des exercices et les estimations de clôture |
| Présentation | Chiffre d'affaires net des remises ; information sur les engagements et sur les créances douteuses | Présentation et intelligibilité ; exhaustivité de l'annexe |

**b. Procédures en réponse (2 pts ; 0,25 pt par procédure reliée à son objectif, dans la limite de 2 pts)**
- **Accords** : obtenir les cinq accords **signés** (et non le seul tableau des taux), rapprocher les barèmes et la définition de la base (hors coffrets) — *mesure et exhaustivité des remises*.
- **Recalcul des remises** centrale par centrale sur la base contractuelle définitive, avec le taux de la tranche atteinte ; rapprochement avec les demandes d'avoir reçues en mars 2027 — *mesure, évaluation du 4198 ; dénouement postérieur* [V NEP estimations § 17].
- **Procédure analytique de substance** sur les remises (c. ci-dessous) — *exhaustivité*.
- **Séparation des exercices** : sur les livraisons des derniers jours de décembre et des premiers jours de janvier, rapprochement des bons de livraison signés (date, quantités) avec les factures et leur date de comptabilisation ; examen des avoirs émis en janvier — *réalité, séparation, existence*.
- **Retours** : comparaison de l'estimation avec les retours effectifs jusqu'au 31/01/2027 et avec le plafond de 3 % — *mesure de l'avoir à établir*.
- **Ventes en ligne** : rapprochement des encaissements de la plateforme avec les expéditions ; vérification que les 138 000 € payés et non expédiés ne sont pas en chiffre d'affaires — *séparation, classification*.
- **Créances** : analyse de l'antériorité de la balance âgée et revue des encaissements postérieurs à la clôture ; demandes de confirmation aux centrales sur un échantillon — *existence, évaluation* [V NEP éléments probants § 10].
- **LAGARDEL** : lecture du jugement et de la lettre de l'administrateur, appréciation de la dépréciation au regard de ces événements postérieurs — *évaluation* [V NEP estimations § 17 ; NEP événements postérieurs § 06].

**c. Procédure analytique de substance sur les remises de fin d'année (1,5 pt)**

*Calcul et conclusion (0,75 pt : attente 0,5 ; écart, rapport et conclusion 0,25)*

| Centrale | Chiffre d'affaires 2026 | Tranche atteinte | Taux | Montant attendu |
|---|---:|---|---:|---:|
| MARVÉLINE | 8 360 000 | 8 000 000 et plus | 5 % | 418 000 |
| TROVALIS | 6 540 000 | de 4 000 000 à moins de 7 000 000 | 3,5 % | 228 900 |
| BERGALLE | 6 120 000 | 6 000 000 et plus | 4 % | 244 800 |
| QUINCÉA | 4 380 000 | de 3 000 000 à moins de 6 000 000 | 3 % | 131 400 |
| DOLMANE | 2 460 000 | moins de 3 000 000 | 2 % | 49 200 |
| **Total** | | | | **1 072 300** |

- Montant comptabilisé : 921 820 € ; **écart : 921 820 − 1 072 300 = − 150 480 €**, soit **− 14,0 %** de l'attente : le montant comptabilisé est **inférieur** à l'attente.
- |− 150 480| / 30 000 = **5,02** fois l'écart acceptable : la procédure **ne corrobore pas** le montant comptabilisé ; l'écart est **à expliquer**.

*Conditions de fiabilité de l'attente (0,5 pt)*
- Une procédure analytique de substance détermine un **montant attendu** et un **écart acceptable** [V NEP procédures analytiques § 05] ; elle peut servir de procédure de substance sur un poste significatif, seule ou avec des tests de détail [V § 07].
- Les données produites par l'entité ne fondent une attente que si le cabinet a collecté des éléments sur leur **exactitude** et leur **exhaustivité** [V NEP éléments probants § 6] : le chiffre d'affaires de l'outil statistique a été rapproché de la comptabilité (0,1 %) ; les barèmes de MARVÉLINE et de TROVALIS sont lus sur les accords signés ; ceux des trois autres centrales proviennent d'un tableau transmis par courriel, copie non étayée par les accords : l'attente n'est fiable pour ces centrales qu'après obtention des accords signés, plus probants [V NEP éléments probants § 6 ; S, application].
- **Précision** : l'attente inclut les coffrets, exclus de la base contractuelle (moins de 1 % des ventes de chaque centrale) ; elle est donc légèrement supérieure aux remises exactes, d'environ 11 000 € au plus [S, calcul : 1 % × 1 072 300 = 10 723 €] : cette imprécision, couverte par l'écart acceptable de 30 000 €, n'explique pas un écart de 150 480 €.

*Suite à donner (0,25 pt)* : l'écart n'est pas en soi une anomalie ; le cabinet détermine les procédures qui permettent de l'**élucider** [V § 09] : tests de détail par centrale (base contractuelle, tranche atteinte, taux retenu), qui révèlent l'usage des prévisions d'octobre (annexe 3.8) ; ce mode de calcul est un risque non identifié jusqu'alors, qui conduit à examiner les autres estimations de clôture fondées sur des prévisions [V § 10].

**Réponses tolérées**
- En a. et b., d'autres risques ou procédures tirés de l'annexe, correctement reliés à des assertions ou à des objectifs.
- En c., un écart présenté en valeur absolue (150 480 €), si le sens (sous-estimation des remises) est indiqué.

**Erreurs fréquentes**
- Confondre réalité (flux) et existence (soldes), ou citer des assertions sans les relier à un risque (`JUR-A01`).
- Appliquer les taux par tranche de façon marginale, alors que l'annexe écarte expressément cette lecture (`JUR-F07`).
- Conclure à une anomalie de 150 480 € sans tests de détail (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP risques § 41 ; NEP éléments probants § 6, § 9-10 | Risque inhérent ; assertions ; techniques ; fiabilité des informations de l'entité | [V] | F11 § 4.1, § 4.3, § 6, § 26.2 |
| NEP procédures analytiques § 03-05, § 07, § 09-10 ; NEP estimations § 17 ; NEP événements postérieurs § 06 | Procédure analytique de substance ; élucidation ; dénouement | [V] ; application : [S] | F11 § 12.1, § 17.1, § 18.1, § 26.1 |

### 3.6 Investigations dans le groupe (1,5 pt)

**Principe : les pièces de la NOUGATERIE (0,5 pt)**
- À toute époque, le commissaire aux comptes opère les vérifications qu'il juge opportunes et se fait communiquer **sur place** toutes les pièces utiles, **notamment tous contrats** [V L. 821-60] ; le secret professionnel ne lui est pas opposable, sauf par les auxiliaires de justice [V L. 821-61 al. 3].
- Les accords avec BERGALLE, QUINCÉA et DOLMANE sont signés **au nom de la NOUGATERIE** : ce sont ses contrats, quel que soit le lieu où ils sont conservés. La direction doit les obtenir de son mandataire et les communiquer ; le tableau des taux ne les remplace pas (question 3.5 c.) [S, application]. La position de la directrice financière est donc erronée sur ce point.

**BRUXOLIA Confiseries SA et BRUXOLIA France SAS (0,75 pt : société mère 0,5 ; autre filiale 0,25)**
- **Société mère** : les investigations peuvent être faites auprès des personnes ou entités qui **contrôlent** l'entité au sens de L. 233-3 [V L. 821-61 al. 1] ; BRUXOLIA Confiseries SA, qui détient 85 % des droits de vote, contrôle la NOUGATERIE [V L. 233-3 I 1°]. Le texte ne distingue pas selon la nationalité de la personne qui contrôle [V, lecture]. **Question ouverte** : la mise en œuvre de ce droit auprès d'une société établie en Belgique, soumise à son propre droit, n'est pas établie par les textes lus [?]. Réponse prudente : demander les contrats-cadres par l'intermédiaire de la présidente, nommée par le groupe, en précisant qu'ils ne sont utiles que dans la mesure où ils déterminent les remises [S].
- **Autre filiale** : BRUXOLIA France SAS ne contrôle pas la NOUGATERIE et n'est pas contrôlée par elle : elle n'entre pas dans l'al. 1 [V L. 821-61 al. 1, lecture]. Elle accomplit des opérations **pour le compte** de la NOUGATERIE : le cabinet peut lui demander toutes **informations** utiles, mais non la communication de ses pièces sans **décision de justice** [V L. 821-61 al. 2 ; D. 821-175].

**Refus persistant (0,25 pt)**
- Le refus des dirigeants de la NOUGATERIE de communiquer des pièces utiles peut constituer le **délit d'obstacle** [V L. 821-6 3°] ; son application aux dirigeants de la société mère étrangère n'est pas établie [?].
- Le cabinet informe la présidente de la difficulté [V L. 821-63 I ; S, application] ; si les éléments ne peuvent être obtenus, c'est une **limitation** : réserve pour limitation si ses incidences sont circonscrites (les remises de trois centrales), impossibilité de certifier sinon [V NEP rapport § 11, § 14]. Ici, les accords ont été obtenus le 24/02/2027 (annexe 3.8).

**Réponses tolérées**
- Une analyse qui retient que la société mère étrangère est visée par l'al. 1, en signalant la difficulté pratique d'exercer ce droit en Belgique : points complets.

**Erreurs fréquentes**
- Étendre le droit d'investigation à toutes les sociétés du groupe, ou confondre investigation et demande de confirmation des tiers (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-60, L. 821-61, L. 233-3, D. 821-175, L. 821-6 3°, L. 821-63 I | Investigations ; contrôle ; tiers ; obstacle ; communication | [V] ; société mère étrangère : [?] | F09 § 5, § 21 ; F11 § 2, § 23.2 |
| NEP rapport § 11, § 14 | Limitation | [V] | F11 § 8.1 |

### 3.7 Anomalies, écritures et opinion (2 pts)

**Calcul des anomalies (0,5 pt ; 0,25 pt par anomalie)**
- **Remises de fin d'année** : l'administration des ventes a appliqué le taux de la tranche prévue en octobre ; pour MARVÉLINE (base 8 312 000 €, tranche de 8 000 000 € et plus) et BERGALLE (base 6 080 000 €, tranche de 6 000 000 € et plus), la tranche atteinte est supérieure. Complément : 8 312 000 × (5 % − 4 %) = 83 120 € ; 6 080 000 × (4 % − 3 %) = 60 800 € ; **anomalie de 143 920 €** (remises exactes 1 065 740 €, comptabilisées 921 820 €). Les autres centrales restent dans la tranche prévue. Après correction, l'écart avec l'attente n'est plus que de 1 065 740 − 1 072 300 = − 6 560 €, inférieur à l'écart acceptable et expliqué par les coffrets : la procédure analytique est élucidée.
- **LAGARDEL Distribution** : la cessation des paiements, fixée au 15/12/2026, est une situation **existant à la clôture** ; le jugement du 11/02/2027 et la lettre du 10/03/2027, connus avant l'arrêté des comptes du 19/03/2027, l'éclairent et doivent être pris en compte [V NEP événements postérieurs § 02, § 08 ; C. com. L. 123-20 al. 1-2 ; S, qualification]. La valeur actuelle de la créance est la répartition attendue : la dépréciation est de 504 000 × (1 − 30 %) = 352 800 €, au lieu de 50 400 € : **anomalie de 302 400 €** ; la créance est virée au compte des clients douteux [V PCG art. 214-25, 1214-41 ; convention de l'annexe 3.8].

**Écritures de correction au 31/12/2026 (0,5 pt)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 709 | Rabais, remises et ristournes accordés | 143 920 | |
| | 4198 | Rabais, remises, ristournes à accorder et autres avoirs à établir | | 143 920 |

Libellé : complément des remises de fin d'année de MARVÉLINE et de BERGALLE (écriture X1, équilibrée à 143 920 €).

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 416 | Clients douteux ou litigieux | 604 800 | |
| | 411 | Clients | | 604 800 |

Libellé : virement de la créance sur LAGARDEL Distribution au compte des clients douteux, toutes taxes comprises (écriture X2, équilibrée à 604 800 €).

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 68174 | Dotations pour dépréciations des actifs circulants - Créances | 302 400 | |
| | 491 | Dépréciations des comptes de clients | | 302 400 |

Libellé : complément de dépréciation de la créance sur LAGARDEL Distribution, 504 000 × 70 % − 50 400 (écriture X3, équilibrée à 302 400 €). Après corrections, le résultat avant impôt est de 3 680 000 − 143 920 − 302 400 = **3 233 680 €**.

**Caractère significatif (0,25 pt)** : 143 920 / 250 000 = **0,58** fois le seuil, non significative à elle seule ; 302 400 / 250 000 = **1,21** fois, significative à elle seule ; ensemble, avec les 41 000 € des autres cycles, 487 320 € (**1,95** fois). Les anomalies s'apprécient individuellement et en cumul, par leur montant, leur nature et les circonstances [V NEP anomalies § 14] ; toutes surévaluent le résultat.

**Opinion selon la décision de la direction (0,5 pt)**
- **Les deux anomalies sont corrigées** : il reste 41 000 € (**0,16** fois le seuil) : **certification sans réserve** ; le cabinet communique les anomalies non corrigées et obtient une déclaration écrite à laquelle en est joint l'état [V NEP anomalies § 15-17 ; NEP déclarations § 6 ; NEP rapport § 08].
- **Seules les remises sont corrigées** : il reste 302 400 + 41 000 = 343 400 € (**1,37** fois le seuil) : désaccord significatif, circonscrit à une créance et chiffré : **certification avec réserve pour désaccord** ; un refus de certifier ne se justifie pas, la réserve chiffrée suffisant au lecteur [V NEP rapport § 09-10, § 12].
- **Seule la créance sur LAGARDEL est corrigée** : il reste 143 920 + 41 000 = 184 920 € (**0,74** fois le seuil) : les anomalies non corrigées ne sont pas significatives par leur montant ; **certification sans réserve**, les anomalies non corrigées figurant à l'état joint à la déclaration écrite et étant communiquées à la présidente [V NEP anomalies § 14-17 ; S, qualification]. Le cabinet apprécie aussi leur nature : une erreur de calcul isolée et chiffrée ne le conduit pas à une réserve [S].

**Parties du rapport, cas de la réserve (0,25 pt)** : la partie « **Opinion avec réserve** » indique que, sous cette réserve, les comptes sont réguliers et sincères et donnent une image fidèle ; la partie « **Fondement de l'opinion avec réserve** » expose le motif et son incidence (créances et résultat surévalués de 302 400 €). Les motifs sont communiqués au préalable à la présidente ; le rapport est destiné aux associés [V NEP rapport § 06, § 18 ; L. 821-63 I ; R. 821-180].

**Réponses tolérées**
- Une créance sur LAGARDEL maintenue au compte 411, si la dépréciation est juste : 0,25 pt sur 0,5 en écritures.
- Une réserve dans le cas où seule la créance est corrigée, si elle est motivée par la nature de l'anomalie (refus d'appliquer les accords signés) : 0,25 pt sur 0,5 en opinion.

**Erreurs fréquentes**
- Traiter la procédure collective comme un événement postérieur sans lien avec la clôture, ou déprécier le montant toutes taxes comprises (`JUR-A01`, `JUR-F07`).
- Écriture sans libellé ou sans numéro de compte (`JUR-F03`).
- Conclure à une certification sans réserve lorsque la seule anomalie significative n'est pas corrigée (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 214-25, 1214-41, 1214-49 ; liste des comptes ; C. com. L. 123-20 al. 1-2 | Dépréciation ; clients douteux ; comptes 709, 4198, 411, 416, 491, 68174 | [V] | F11 § 12.5, § 17.2, § 26.4 |
| NEP événements postérieurs § 02, § 08 ; NEP anomalies § 14-17 ; NEP déclarations § 6 ; NEP rapport § 06, § 08-10, § 12, § 18 ; R. 821-180 ; L. 821-63 I | Événements postérieurs ; anomalies ; opinions ; parties du rapport | [V] ; qualification : [S] | F11 § 8, § 12.1, § 12.3, § 14.1 |

---

### Partie B – Durabilité (12 points)

### 3.8 Emplacement, renvois et informations spécifiques à l'entité (3 pts)

**Emplacement des informations (0,75 pt)**
- Toutes les informations requises par les ESRS figurent dans une **section spécifique du rapport de gestion**, identifiée comme l'**état de durabilité**, qui comprend aussi les informations incorporées par renvoi [V ESRS 1 (2026) § 103] ; elles sont présentées de manière à être **clairement distinguées** des autres informations du rapport de gestion [V § 104 a)].
- **Application** : le chapitre 4 mêle l'histoire, les recettes et les médailles (texte commercial) et les informations publiées selon les ESRS. La NOUGATERIE doit identifier l'état de durabilité comme tel et en sortir la partie 4.1, ou la signaler comme étrangère à l'état. L'ordre des parties (générales, environnement, social, gouvernance) est conforme [V § 105].

**Renvois (1 pt)**
- Une information ne peut être **incorporée par renvoi** qu'à une autre section du rapport de gestion, aux **états financiers**, à la déclaration sur la gouvernance d'entreprise, au rapport sur la rémunération, au document d'enregistrement universel ou aux publications prudentielles [V ESRS 1 (2026) § 117], et à cinq conditions : élément distinct et clairement identifié dans le document source ; publication avant ou en même temps que le rapport de gestion ; **même langue** ; **au moins le même niveau d'assurance** ; mêmes exigences de numérisation [V § 118].
- **Application** : la **page du site internet** et la **Charte d'achat** du groupe ne figurent pas dans cette liste ; la Charte est en outre rédigée en anglais et n'est pas vérifiée par le cabinet. Les informations sur les emballages et sur l'approvisionnement en amandes et en miel, sujets matériels selon l'analyse de la société, doivent être **reprises dans l'état** [S, application]. Le renvoi à la **note 18 de l'annexe des comptes annuels** est admis (états financiers), si la note identifie clairement les informations reprises : elle est publiée avec les comptes, en français, et couverte par la certification, d'un niveau d'assurance supérieur [S, application de § 117 b) et § 118] ; c'est aussi une connexion directe avec les états financiers [V § 114].

**Informations spécifiques à l'entité (1,25 pt)**
- Lorsqu'un sujet lié à des impacts, risques et opportunités matériels n'est pas couvert, ou pas de façon suffisamment détaillée, par les ESRS, l'entreprise publie des **informations spécifiques à l'entité** [V ESRS 1 (2026) § 11], en tenant compte de leur **comparabilité** dans le temps et avec les entreprises du secteur [V § 12]. Un indicateur spécifique doit être **pertinent**, donner une **représentation fidèle**, fondée sur des hypothèses raisonnables et **vérifiables**, et s'accompagner d'**informations contextuelles** suffisantes [V AR 3-4].
- **Application** :
  - les trois données répondent à des sujets matériels et peuvent être publiées comme informations spécifiques ;
  - leurs définitions manquent ou sont renvoyées à la Charte, renvoi inadmissible : la NOUGATERIE doit préciser dans l'état, pour chaque donnée, l'unité (poids ou valeur), le périmètre (amandes utilisées ou achetées), la période, les sources et la méthode de calcul ;
  - pour les saisonniers, deux lectures sont possibles (saisonniers de 2026 déjà présents en 2025, ou saisonniers de 2025 revenus en 2026) : le choix doit être écrit, et appliqué de la même façon chaque année pour la comparabilité [S, application].

**Réponses tolérées**
- La mention que les informations non matérielles demandées par une centrale peuvent figurer dans l'état si elles sont signalées comme ne résultant pas de l'évaluation de la matérialité [V ESRS 1 (2026) § 108-109] : sans points supplémentaires.

**Erreurs fréquentes**
- Admettre tout renvoi vers un document public de l'entreprise, ou ignorer les conditions de langue et d'assurance (`JUR-A05`).
- Présenter les trois données sans exiger de définition, ou détailler des normes thématiques (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 103-105, § 108-109, § 114, § 117-118 | Section spécifique ; distinction ; renvois et conditions ; connexion directe | [V] ; application : [S] | F12 § 9, § 17, § 22 |
| ESRS 1 (2026) § 11-12, AR 3-4 | Informations spécifiques à l'entité | [V] | F12 § 3.3, § 20 |

### 3.9 Impacts, risques et opportunités ; connectivité (3 pts)

**Notions (0,5 pt)** : un **impact** est un effet positif ou négatif, réel ou potentiel, de l'entreprise sur les personnes ou l'environnement, lié à ses activités propres ou à sa chaîne de valeur, y compris en amont (matérialité d'impact) ; un **risque** ou une **opportunité** est un effet financier, actuel ou attendu, sur la situation, les performances, les flux de trésorerie, l'accès au financement ou le coût du capital (matérialité financière) ; il peut découler d'un impact, d'une **dépendance** à l'égard de ressources naturelles ou humaines, ou d'autres facteurs [V ESRS 1 (2026) § 39-41, § 47-48].

**Application au contexte (1,75 pt ; 0,25 pt par élément correctement qualifié, dans la limite de 1,75 pt)**

| Élément du contexte | Matérialité d'impact | Matérialité financière |
|---|---|---|
| Amandes importées | Impact négatif dans la chaîne de valeur amont : prélèvements d'eau d'irrigation dans des régions en stress hydrique | Dépendance : risque de hausse des prix (+ 22 % après la sécheresse de 2025) et de rupture d'approvisionnement |
| Contrat avec AMANDÈNE Provence | Impact positif : soutien à la replantation d'amandiers et à une filière locale | Opportunité : origine française attendue par les centrales ; risque : prix ferme supérieur au prix des amandes importées |
| Miel et pollinisateurs | Impact positif par les achats aux apiculteurs locaux | Dépendance à la pollinisation : risque de récoltes réduites et de prix plus élevés (+ 18 %) |
| Cuisson au gaz | Impact négatif : émissions liées à 5 800 MWh de gaz | Risque de coût de l'énergie et de transition ; investissement de 2 600 000 € dans une ligne électrique |
| Emballages | Impact négatif : déchets de boîtes métalliques et de films plastiques | Risque de déréférencement par deux centrales à partir de 2028 ; opportunité d'emballages recyclables |
| Saisonniers | Impact négatif réel : chaleur près des fours, six jours sur sept, trois accidents avec arrêt | Risque de difficultés de recrutement ; opportunité : fidéliser les saisonniers, formés plus vite |
| Exigences des centrales | — | Risque commercial lié à la notation des fournisseurs, sur 77,6 % des ventes réalisées avec les centrales à accord |

Un même sujet peut être matériel des deux points de vue, et un impact positif ne compense pas un impact négatif [V ESRS 1 (2026) § 35-36, § 44].

**Connectivité avec les comptes (0,75 pt)**
- L'état de durabilité fournit des informations permettant de comprendre les **connexions** avec les états financiers [V ESRS 1 (2026) § 112] ; un montant présent dans les deux renvoie aux états financiers (**connexion directe**) ; les données et hypothèses concordent, ou les différences sont expliquées [V § 114, § 116].
- **Contrat de Provence** : l'état décrit le contrat et les quantités (300 tonnes par an) ; l'annexe des comptes mentionne l'engagement d'achat de 8 280 000 € (300 tonnes × 9,20 € × 3 ans) : l'état renvoie à cette note, avec les mêmes quantités et le même prix.
- **Ligne de cuisson n° 2** : l'état annonce son remplacement au début de 2028 ; les comptes ont révisé sa durée d'utilisation (valeur nette de 640 000 € amortie jusqu'au 31/12/2027) : la date retenue est la même dans les deux documents ; l'investissement prévu de 2 600 000 €, futur, n'est pas dans les comptes de 2026 et l'état l'explique [S, application].

**Réponses tolérées**
- D'autres éléments tirés du contexte (sucre de betterave, transport des produits), s'ils sont correctement qualifiés.
- Le classement du contrat de Provence parmi les impacts de la chaîne de valeur plutôt que parmi les opportunités, si l'effet financier est aussi décrit.

**Erreurs fréquentes**
- Ne retenir que des risques financiers, ou conduire l'analyse de double matérialité (notation, seuils), qui n'est pas demandée (`JUR-A06`).
- Confondre la connectivité avec la simple répétition de montants (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 35-36, § 39-41, § 44, § 47-48 | Impacts ; risques et opportunités ; dépendances | [V] ; application : [S] | F12 § 6, § 15 |
| ESRS 1 (2026) § 112, § 114, § 116 | Connectivité ; connexion directe ; cohérence des hypothèses | [V] ; application : [S] | F12 § 9 |

### 3.10 Mission, assurance, démarche et procédures (4 pts)

**a. Objectifs, axes et assurance (2 pts)**
- **Objectifs (0,5 pt)** : un **avis** sur la conformité aux ESRS du **processus** mis en œuvre pour déterminer les informations publiées (analyse de double matérialité) et sur la conformité des **informations** publiées, dans un rapport destiné aux associés [V L. 821-54 II, par analogie ; LD 2026 § 2]. La NOUGATERIE publie volontairement : la mission est conduite dans les conditions de la certification légale par hypothèse, les textes s'appliquant par analogie [S]. Elle ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].
- **Axes (0,5 pt)** : axe 1 (processus) et axe 2 (informations) ; l'axe des informations de la taxonomie est sans objet, la NOUGATERIE n'y étant pas tenue, et celui du balisage aussi, faute de règles applicables ; la consultation du comité social et économique est hors de la lettre de mission [V LD 2026 § 2, § 10 ; F12 § 11 (b)].
- **Assurance limitée (0,5 pt)** : vérifications moindres, en **nature**, en **étendue** et en **durée**, que pour une assurance raisonnable ; conclusion exprimée sous une **forme négative** : le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes [V LD 2026, « Niveau d'assurance »].
- **Différence avec la certification des comptes (0,5 pt)** : pour les comptes, l'assurance est **raisonnable**, élevée mais non absolue, et l'opinion s'exprime sous une **forme positive** (« nous certifions que les comptes sont réguliers et sincères… ») ; la certification est conduite selon les NEP homologuées, la mission sur la durabilité selon les lignes directrices de la H2A, dans l'attente d'une norme d'assurance européenne [V NEP principes § 08 ; NEP rapport § 08 ; LD 2026, propos liminaires ; F13 § 2.4].

**b. Étapes et procédures (2 pts)**
- **Étapes (0,75 pt)** : lettre de mission ; **prise de connaissance** de l'entité (approvisionnements, saisonniers, relations avec le groupe) et des processus qui produisent les données (sorties de stock, données de la centrale, tableau des contrats saisonniers) ; **planification**, avec la sélection des informations **vérifiées spécifiquement**, celles qui présentent un risque important de non-conformité ou de fortes attentes des utilisateurs (ici les données attendues par les centrales) ; **contrôle du processus** (axe 1, achevé sans anomalie) ; **contrôle des informations** (axe 2), dont la présentation et les renvois (question 3.8) ; lecture d'ensemble et cohérence avec les comptes, en lien avec l'équipe qui certifie les comptes ; communication avec la direction, déclarations écrites ; **rapport** d'assurance limitée par axe [V LD 2026 § 3-8, § 11-14, § 17 ; F13 § 3].
- **Procédures (1,25 pt ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 0,75 pt par donnée)** :
  - *Part des amandes d'origine française* : obtention de la **définition** (poids, amandes utilisées, année civile) ; **rapprochement du dénominateur** (1 250 tonnes) avec les sorties de stock et les achats consommés des comptes (exactitude, connectivité) ; **rapprochement** des 300 tonnes de Provence avec les bons de livraison, les factures et le contrat d'AMANDÈNE Provence (réalité, exactitude) ; **demande des données d'achats par origine** et des documents d'origine des fournisseurs de la centrale pour les 125 tonnes (réalité) ; **recalcul** : 425 / 1 250 = 34,0 % [V LD 2026 § 8, § 12 ; S, procédures].
  - *Part des saisonniers réembauchés* : obtention de la **définition** retenue ; **rapprochement** du tableau des contrats avec le registre du personnel et la paie des saisons 2025 et 2026 (exhaustivité des 90 et des 84 saisonniers) ; **test sur un échantillon** des 65 saisonniers déclarés présents les deux années (réalité) ; **recalcul** : 65 / 90 = 72,2 %, publié à 72 % ; cohérence avec les effectifs de la note 18 de l'annexe des comptes [V LD 2026 § 8 ; S, procédures].

**Réponses tolérées**
- En b., les étapes dans l'ordre du programme (prise de connaissance, planification, contrôle de la conformité des informations et du processus, contrôle du balisage, contrôle des exigences de publication, rapport) : points complets.

**Erreurs fréquentes**
- Retenir les axes de la taxonomie et du balisage pour une entité qui n'y est pas tenue, ou présenter l'assurance limitée comme une garantie (`JUR-A05`, `JUR-A01`).
- Proposer des procédures sans lien avec les deux données ni objectif (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; NEP principes § 08 ; NEP rapport § 08 | Objet de l'avis ; absence de garantie ; assurance raisonnable | [V] ; application à une mission volontaire : [S] | F13 § 2 ; F11 § 1.1 ; F12 § 11 |
| LD 2026 § 2-8, § 10-14, § 17, « Niveau d'assurance » | Axes ; assurance limitée ; étapes ; informations vérifiées spécifiquement | [V] ; procédures : [S] | F13 § 2-3, § 7 |

### 3.11 Avis sur les informations et comparaison avec l'opinion sur les comptes (2 pts)

- **La direction maintient la part de 34 % (0,75 pt)** : l'origine de 125 tonnes (10 % des amandes utilisées, 29,4 % des 425 tonnes déclarées françaises) ne peut être vérifiée ; la confirmation du groupe, simple déclaration interne non étayée par des documents, ne constitue pas un élément suffisant et approprié [V LD 2026 § 12 ; S, application]. C'est une **limitation** : le cabinet n'a pu mettre en œuvre toutes les vérifications nécessaires. Elle porte sur une donnée identifiée et chiffrable (125 tonnes sur 1 250) : incidences **clairement circonscrites**, réserve suffisante si elle les décrit : **avis de conformité assorti d'une réserve motivée** sur l'axe 2 ; l'avis sur le processus (axe 1) reste un avis de conformité [V LD 2026 § 17 ; F13 § 4.3 ; S, qualification]. Ni impossibilité d'émettre un avis, la limitation ne privant pas de sens l'ensemble des informations, ni non-conformité, aucune erreur n'étant établie.
- **La direction retient l'information proposée (0,5 pt)** : la donnée publiée est vérifiable et sa limite est indiquée ; aucune limitation ne subsiste : **avis de conformité** sur les deux axes ; le cabinet peut formuler une **observation** renvoyant à l'information sur les achats de la centrale non ventilés par origine [V LD 2026 § 17 ; F13 § 4.4].
- **Différences avec l'opinion sur les comptes (0,75 pt ; 0,25 pt par différence, dans la limite de 0,75 pt ; le niveau d'assurance, noté en 3.10 a., n'est pas noté de nouveau)** :
  - **objet et référentiel** : conformité aux ESRS d'un processus et d'informations en grande partie qualitatives, contre la régularité, la sincérité et l'image fidèle des comptes au regard du plan comptable général [V L. 821-53 ; L. 821-54 II] ;
  - **structure** : un avis par axe, avec d'éventuelles observations et des éléments ayant fait l'objet d'une attention particulière, contre une opinion unique sur les comptes pris dans leur ensemble, avec la justification des appréciations [V LD 2026 § 17 ; NEP rapport § 18] ;
  - **vocabulaire** : avis de conformité, avec réserve, de non-conformité, impossibilité d'émettre un avis, contre certification sans réserve, avec réserve, refus et impossibilité de certifier [V LD 2026 § 17 ; R. 821-180] ;
  - **indépendance des conclusions** : la limitation sur l'origine des amandes ne porte que sur une information de durabilité ; elle n'affecte pas l'opinion sur les comptes, dont les achats sont justifiés par les factures de la centrale, sans incidence comptable de leur origine [S].

**Réponses tolérées**
- Une impossibilité d'émettre un avis sur l'axe 2, si le candidat motive l'absence de circonscription par l'importance de cette donnée pour les centrales : 0,25 pt sur 0,75.

**Erreurs fréquentes**
- Qualifier la situation d'erreur (non-conformité) alors qu'il s'agit d'une limitation, ou remplacer la réserve par une observation (`JUR-A02`).
- Appliquer à l'avis le vocabulaire de la certification des comptes (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 12, § 17 | Éléments suffisants et appropriés ; avis, réserve pour limitation, observations, structure par axe | [V] ; qualification : [S] | F13 § 3, § 4.1-4.4 |
| C. com. L. 821-53, L. 821-54 II ; NEP rapport § 18 ; R. 821-180 | Certification des comptes ; structure du rapport ; opinions | [V] | F11 § 1.1, § 8 |
