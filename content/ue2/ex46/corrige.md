# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 46 — Dossier 1 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F04 diagnostic financier consolidé, F07 risques de taux et de change, F08 gouvernance et ESG, F10 auteurs et théories, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (équilibre des bilans, des capitaux employés, des comptes de résultat, de la variation des capitaux propres, des tableaux des flux de trésorerie, du chiffre d'affaires par zone, des stocks, de la pyramide des âges et des poids de la grille RSE ; marges, ROCE, ROE, durées en jours, DFN / EBITDA avec et sans dettes locatives, taux de fréquence et intensité des émissions ; note RSE sur la grille fournie ; cours à terme, points de terme et montants des couvertures à terme ; prime, valeur intrinsèque, valeur temps et dénouement de l'option ; barème, liste noire, hors-programme ; croissance à taux de change constants, positions de change, effet d'une variation de 5 %, termaillage, garantie de change et résultats si l'appel d'offres est perdu vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un cours à terme à 12 mois erroné à la question 1.6, repris dans la vente à terme de la question 1.7).

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Activité, rentabilité, BFR et flux de trésorerie | `1.a` Réaliser une analyse financière des comptes consolidés ; `1.c` Apprécier la performance opérationnelle et financière d'un groupe | 3 |
| 1.2 Lecture des comptes en IFRS : écarts de conversion et dettes locatives | `1.b` Interpréter les états financiers des groupes en normes comptables internationales (IFRS) | 1,5 |
| 1.3 Éléments extra-financiers et relation avec le groupe ; forces, faiblesses et risques | `2.1.a` Identifier les éléments extra-financiers pour le diagnostic, dans la lignée du modèle d'affaires de l'entreprise ; `1.a` ; `1.c` | 2,5 |
| 1.4 Note RSE de fournisseur, éligibilité, limites et actions | `2.1.c` Utiliser les outils de notation financière et extra-financière | 2,5 |
| 1.5 Position de change et sensibilité | `6.3.a` Caractériser la position de change courte ou longue, ouverte ou fermée | 1,5 |
| 1.6 Cours à terme, couverture à terme et termaillage | `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) ; `6.3.d` Maîtriser les contrats à terme et optionnels (change) ; `6.3.c` Maîtriser les techniques internes et les garanties externes | 2,5 |
| 1.7 Risque conditionnel de l'appel d'offres : terme, option, garantie de change, indexation | `6.3.d` ; `6.3.c` | 2,5 |
| **Total** | | **16** |

Part du calcul : environ 8 points (1.1-01 à 1.1-04, 1.2-01 et 1.2-02 pour partie, 1.4-01, 1.5-01 et 1.5-03, 1.6-01 à 1.6-03, 1.7-02 et 1.7-03). Part de l'analyse : environ 8 points. Les questions 1.3 et 1.4 se traitent sans les calculs de la question 1.1, et la question 1.7 sans ceux de la question 1.6 (un cours à terme cohérent suffit) : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 1.1 Activité, rentabilité, BFR et flux de trésorerie (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Croissance publiée + 7,57 % ; chiffre d'affaires américain de 2026 au cours de 2025 : 24,84 / 1,08 = 23,00 M€ ; croissance à taux de change constants + 10,36 % (effet de change − 1,40 M€) ; États-Unis + 8,00 % en euros, + 15,00 % en dollars ; poids des États-Unis 39,84 % et 40,00 % | 0,75 |
| 1.1-02 | Marges d'EBITDA 19,52 % et 18,33 % ; marges opérationnelles 13,75 % et 12,59 % ; capitaux employés 33,40 et 36,30 M€ ; ROCE 15,49 % et 14,05 % ; ROE 21,11 % et 19,23 % | 0,75 |
| 1.1-03 | Durée de stockage 101,83 et 108,00 jours ; BFR 14,60 et 16,70 M€, soit 104,70 et 111,33 jours de chiffre d'affaires | 0,5 |
| 1.1-04 | CAF 7,46 et 7,60 M€ ; flux de trésorerie disponible 3,06 et 1,30 M€ ; dividendes de 2026 (2,40 M€) supérieurs au flux disponible, financés par la hausse du compte courant de la holding (+ 1,50 M€) et par la trésorerie (− 0,90 M€) | 0,5 |
| 1.1-05 | Commentaire relié au panel : croissance supérieure mais freinée par le dollar, rentabilité au-dessus du panel mais en érosion, stocks qui absorbent la trésorerie, dépendance financière envers la holding | 0,5 |

**Activité (0,75 pt).**

| M€ | 2025 | 2026 | Évolution |
|---|---:|---:|---:|
| États-Unis (en M$ : 21,60 ; 24,84) | 20,00 | 21,60 | + 8,00 % (+ 15,00 % en dollars) |
| France | 18,00 | 18,36 | + 2,00 % |
| Autres pays d'Europe | 12,20 | 14,04 | + 15,08 % |
| **Chiffre d'affaires publié** | **50,20** | **54,00** | **+ 7,57 %** (panel : + 5,00 %) |
| États-Unis au cours moyen de 2025 : 24,84 / 1,0800 | | 23,00 | |
| **Chiffre d'affaires à taux de change constants** | 50,20 | 54,00 − 21,60 + 23,00 = **55,40** | **+ 10,36 %** |
| **Poids des États-Unis** | 20,00 / 50,20 = **39,84 %** | 21,60 / 54,00 = **40,00 %** | |

Le périmètre étant constant, toute la croissance est organique. La baisse du dollar (cours moyen de 1,0800 à 1,1500, soit − 6,09 % pour la valeur en euros du dollar) a coûté **1,40 M€** de chiffre d'affaires : l'activité américaine progresse de 15 % en volume et en prix, mais de 8 % seulement en euros. Les États-Unis sont la zone la plus dynamique avec le reste de l'Europe ; la France, marché mûr, stagne (+ 2,00 %).

**Rentabilité (0,75 pt).**

| | 2025 | 2026 | Panel |
|---|---:|---:|---:|
| Marge d'EBITDA | 9,80 / 50,20 = **19,52 %** | 9,90 / 54,00 = **18,33 %** | 17,00 % |
| Marge opérationnelle | 6,90 / 50,20 = **13,75 %** | 6,80 / 54,00 = **12,59 %** | 11,00 % |
| Immobilisations + droits d'utilisation | 18,80 | 19,60 | |
| BFR | 14,20 + 8,40 + 0,80 − 5,20 − 3,60 = 14,60 | 16,20 + 9,00 + 0,90 − 5,60 − 3,80 = 16,70 | |
| **Capitaux employés** | **33,40** | **36,30** | |
| Contrôle : capitaux propres + DFN (9,00 + 3,00 + 2,40 − 2,60 ; 8,00 + 4,50 + 2,10 − 1,70) | 21,60 + 11,80 = 33,40 | 23,40 + 12,90 = 36,30 | |
| **ROCE après impôt** = RO × 0,75 / capitaux employés | 5,175 / 33,40 = **15,49 %** | 5,10 / 36,30 = **14,05 %** | 12,00 % |
| **ROE** = résultat net / capitaux propres | 4,56 / 21,60 = **21,11 %** | 4,50 / 23,40 = **19,23 %** | |

Décomposition (information) : rotation des capitaux employés 1,50 puis 1,49 ; coût net de la dette 0,80 × 0,75 / 12,90 = 4,65 % ; effet de levier (14,05 % − 4,65 %) × 12,90 / 23,40 = 5,18 points, d'où ROE = 14,05 % + 5,18 % = 19,23 %. Le chiffre d'affaires progresse de 7,57 % mais l'EBITDA de 1,02 % seulement, et le résultat opérationnel recule (− 1,45 %) : les achats consommés passent de 30,60 % à 31,67 % du chiffre d'affaires (hausse des prix et du franc suisse pour les composants de Bienne), et la baisse du dollar réduit la marge des ventes américaines, dont une grande partie des coûts est en euros et en francs suisses.

**BFR et stocks (0,5 pt).**

| | 2025 | 2026 | Panel |
|---|---:|---:|---:|
| Durée de stockage = stocks / CA × 360 | 14,20 / 50,20 × 360 = **101,83 j** | 16,20 / 54,00 × 360 = **108,00 j** | 95 j |
| Délai clients (information) | 60,24 j | 60,00 j | |
| **BFR en jours de CA** | 14,60 / 50,20 × 360 = **104,70 j** | 16,70 / 54,00 × 360 = **111,33 j** | 90 j |

Les stocks augmentent de 14,08 %, presque deux fois plus vite que le chiffre d'affaires. La hausse vient des montures finies : celles de la filiale américaine (+ 0,80 M€, pour livrer en 48 heures) et surtout les collections de plus de deux ans (1,20 → 2,10 M€), qui exposent à des démarques ou à des dépréciations. Le BFR dépasse le panel de plus de 21 jours, soit 16,70 − 54,00 × 90 / 360 = 3,20 M€ de capitaux immobilisés en plus (calcul facultatif).

**Flux de trésorerie (0,5 pt).**

| M€ | 2025 | 2026 |
|---|---:|---:|
| **CAF** = résultat net + dotations | 4,56 + 2,90 = **7,46** | 4,50 + 3,10 = **7,60** |
| Variation du BFR (hors écarts de conversion) | − 1,20 | − 2,40 |
| Flux net lié à l'activité | 6,26 | 5,20 |
| Investissements | − 3,20 | − 3,90 |
| **Flux de trésorerie disponible** | **3,06** (6,10 % du CA) | **1,30** (2,41 % du CA ; panel 5,00 %) |
| Dividendes versés à la holding | − 2,40 | − 2,40 |
| Emprunts bancaires remboursés | − 1,00 | − 1,00 |
| Compte courant de la holding | — | **+ 1,50** |
| Dettes locatives remboursées | − 0,30 | − 0,30 |
| Variation de la trésorerie | − 0,64 | − 0,90 |

**Financement des dividendes de 2026** : le flux disponible (1,30 M€) ne couvre que 54,17 % du dividende (2,40 M€, soit 184,62 % du flux disponible). Le dividende, les remboursements d'emprunt et de dettes locatives (3,70 M€ au total) ont été payés par le flux disponible (1,30), par **l'augmentation du compte courant de la holding (1,50)** et par **la baisse de la trésorerie (0,90)**. Autrement dit, la holding a prêté d'une main ce qu'elle a reçu de l'autre.

**Commentaire (0,5 pt).**
- **Une croissance réelle, masquée en partie par le dollar** : + 10,36 % à taux de change constants, deux fois le panel ; les États-Unis (40 % du chiffre d'affaires) en sont le moteur, mais aussi la principale source de volatilité.
- **Une rentabilité au-dessus du panel mais en érosion** : ROCE de 14,05 % contre 12,00 %, marges supérieures de 1 à 1,6 point ; mais la marge opérationnelle perd 1,15 point en un an (13,745 % − 12,593 %) sous l'effet combiné du dollar faible et du franc suisse fort. La rentabilité est donc sensible au change des deux côtés : ventes en dollars, achats en francs suisses (questions 1.5 à 1.7).
- **Des stocks qui absorbent la trésorerie** : le BFR (111 jours contre 90) et les collections anciennes expliquent la chute du flux disponible (− 57,52 %), alors que la CAF progresse.
- **Une structure financière saine en apparence, dépendante en réalité** : DFN / EBITDA de 1,30 (panel 1,50 ; engagement bancaire à 2,00) ; mais 34,88 % de la DFN est un compte courant remboursable à la demande de la holding, qui a financé un dividende supérieur au flux disponible.

**Réponses tolérées** : croissance à taux constants calculée sur la seule filiale (+ 15,00 %) si le total est aussi donné ; capitaux employés obtenus par les ressources (capitaux propres + DFN) ; BFR en jours calculé sur 365 jours si la convention est annoncée ; flux disponible présenté après remboursement des dettes locatives (2,76 et 1,00 M€), si le choix est annoncé.

**Erreurs fréquentes**
- Calculer la croissance à taux constants en convertissant le chiffre d'affaires de 2025 au cours de 2026, ou en appliquant le cours de clôture : la convention fixe le cours moyen de 2025.
- Oublier le compte courant de la holding dans la DFN (DFN de 8,40 M€ au lieu de 12,90 M€) : c'est une dette financière, rémunérée et remboursable à la demande.
- Lire la variation du BFR sur les bilans (+ 2,10) pour reconstituer le tableau des flux : l'écart (0,30) correspond aux écarts de conversion, sans effet sur la trésorerie.
- `JUR-E01` — confondre CAF et flux de trésorerie disponible ; `JUR-T13` — ratios calculés sans comparaison au panel ; `JUR-T07` — ratios présentés en texte plutôt qu'en tableau.

Références : F04 § 2, § 3 et § 5 (bilan économique, ROCE, ROE, effet de levier, tableau des flux) [V guide p. 57-58] ; programme l. 468-473 (périmètre constant, analyse par les flux) [V].

---

### 1.2 Lecture des comptes en IFRS : écarts de conversion et dettes locatives (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | Écarts de conversion : perte de valeur en euros de l'actif net de la filiale, inscrite dans les capitaux propres et non dans le résultat ; ROE de 19,23 % contre une rentabilité globale de 17,95 % (21,11 % et 19,26 % en 2025) ; risque de conversion distinct du risque de transaction ; écarts cumulés de − 0,95 M€ | 0,75 |
| 1.2-02 | Dettes locatives : EBITDA relevé des loyers (0,42 M€, 4,24 % de l'EBITDA) ; DFN / EBITDA de 1,30 avec dettes locatives, 1,14 sans (1,20 et 1,00 en 2025) ; comparaisons à mener dans la même lecture ; marge sous l'engagement bancaire | 0,75 |

**Écarts de conversion (0,75 pt).** Les comptes de la filiale américaine sont tenus en dollars ; pour les consolider, son bilan est converti au cours de clôture et son résultat au cours moyen. Le dollar ayant baissé (clôture 1,0400 → 1,1200 → 1,1600), l'actif net de la filiale vaut moins en euros : − 0,40 M€ en 2025 et − 0,30 M€ en 2026. Ce que le lecteur doit en retenir (les montants sont fournis) :
- **Une perte latente, hors résultat** : elle ne résulte d'aucune opération réalisée, ne touche pas la trésorerie et ne serait constatée en résultat qu'en cas de cession de la filiale. Elle est inscrite directement dans les capitaux propres, qui ne progressent que de 1,80 M€ au lieu de 2,10 M€ (4,50 − 2,40).
- **Une rentabilité des capitaux propres flattée** : le ROE publié (19,23 %) ignore cette perte. La rentabilité globale, (4,50 − 0,30) / 23,40 = **17,95 %**, est inférieure de 1,28 point ; en 2025, **19,26 %** contre 21,11 %. Pour l'actionnaire, c'est la richesse réellement créée, écarts de conversion compris, qui compte ; la holding, qui raisonne en francs suisses, supporte en outre un risque de conversion sur l'euro.
- **Deux risques de change distincts** : le **risque de conversion** (valeur en euros de l'actif net d'une filiale étrangère, ici 0,95 M€ cumulés au 31/12/2026) et le **risque de transaction** (flux de l'année en dollars et en francs suisses, déjà visible dans les marges et traité aux questions 1.5 à 1.7). Le premier ne se couvre pas par les mêmes instruments ; il se réduit en finançant la filiale en dollars (ses dettes locatives en dollars le font déjà en partie).

**Dettes locatives (0,75 pt).** Le sous-groupe inscrit l'entrepôt et les bureaux américains à l'actif (droit d'utilisation) et au passif (dette locative de 2,10 M€). Effets sur la lecture :

| 2026 | Avec la norme (publié) | Sans la norme | 2025 avec / sans |
|---|---:|---:|---:|
| EBITDA (M€) | 9,90 | 9,90 − 0,42 = 9,48 | 9,80 / 9,38 |
| DFN (M€) | 12,90 | 12,90 − 2,10 = 10,80 | 11,80 / 9,40 |
| **DFN / EBITDA** | **1,30** | **1,14** | **1,20 / 1,00** |

- **L'EBITDA est relevé** de la totalité des loyers (0,42 M€, soit 4,24 % de l'EBITDA) : ils deviennent amortissement (0,30) et intérêts (0,12) ; la partie remboursement est classée en financement, ce qui améliore aussi le flux d'activité.
- **L'endettement est alourdi** : la DFN intègre l'engagement de loyers, et le ratio DFN / EBITDA monte de 1,14 à 1,30 malgré la hausse de l'EBITDA. Il reste loin de l'engagement bancaire (2,00, soit une marge de 6,90 M€ de DFN supplémentaire) ; les comparaisons avec le panel et avec l'engagement doivent se faire dans la même lecture.
- **Une incitation à surveiller** (lien avec la question 1.3, non exigé ici) : la part variable du président dépend en totalité de l'EBITDA (annexe 1.3). Un indicateur relevé par la présentation des loyers, et insensible aux stocks qui gonflent, peut récompenser une croissance qui consomme de la trésorerie (question 1.3).

**Réponses tolérées** : toute formulation qui interprète l'effet sur la performance et l'endettement sans justification technique ; mention de la primauté de la substance sur la forme ; rentabilité globale appelée « ROE résultat global », si elle est définie.

**Erreurs fréquentes**
- Recalculer les écarts de conversion à partir des cours de clôture : ils sont fournis et n'ont pas à être recalculés.
- Déduire les écarts de conversion du résultat net ou du flux de trésorerie : ils ne passent ni par l'un ni par l'autre.
- Confondre risque de conversion et risque de transaction, ou proposer de couvrir l'écart de conversion par une vente à terme des encaissements de l'année.
- Citer des numéros de normes ou décrire la technique de conversion : hors du champ de l'épreuve (UE 4) ; `JUR-T13` — exposé général sans les montants du sous-groupe.

Références : F04 § 0, § 4 et § 6 (spécificités IFRS, interpréter sans justifier ; endettement avec et sans dettes locatives) [V guide p. 58] ; F07 § 3.1 (nature du risque de change) ; programme l. 468 et 472 [V].

---

### 1.3 Éléments extra-financiers et relation avec le groupe ; forces, faiblesses et risques (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | Savoir-faire : 35,42 % des lunetiers et polisseurs ont 55 ans ou plus (panel 25 %), 30 départs d'ici 2031, trois ans pour former un polisseur, apprentis formés et retenus en baisse (4 et 2), formation en recul (14 h) ; actif immatériel absent du bilan | 0,5 |
| 1.3-02 | Dépendance envers le groupe : fournisseur unique à Bienne (31,58 % des achats), prix fixés par la holding en francs suisses (+ 3 %, puis + 4 %), compte courant remboursable à la demande (34,88 % de la DFN), dividende fixé par la holding | 0,5 |
| 1.3-03 | Gouvernance et relation d'agence (Jensen et Meckling, 1976) : holding principal, président agent révocable ; pouvoirs encadrés ; asymétrie d'information et mécanismes de contrôle ; incitation sur l'EBITDA ; intérêts du groupe et de la filiale qui peuvent diverger | 0,5 |
| 1.3-04 | Synthèse hiérarchisée des forces, des faiblesses et des risques, chiffrée, avec des recommandations | 1 |

**Savoir-faire des lunetiers et des polisseurs (0,5 pt).** Le modèle d'affaires de VERMONDAZ repose sur un savoir-faire de fabrication (usinage de l'acétate, assemblage, polissage) qui justifie un positionnement de qualité et des marges supérieures au panel. Cet actif n'apparaît pas au bilan. Il est menacé :
- **pyramide des âges** : 34 des 96 lunetiers et polisseurs, soit **35,42 %**, ont 55 ans ou plus (25 % dans le panel) ; 30 partiront d'ici 2031, près d'un tiers de l'effectif de ces métiers ;
- **transmission insuffisante** : il faut trois ans pour former un polisseur, or l'entreprise forme moins d'apprentis (6 → 4) et en garde moins (4 → 2) ; les heures de formation baissent (18 → 14 h par salarié) ;
- **conditions de travail** : le taux de fréquence des accidents passe de 21,62 à **30,00** par million d'heures (12 accidents pour 400 000 heures), signe possible d'une production poussée par la croissance des volumes avec des équipes vieillissantes.
Le rythme des départs dépasse celui de la relève : sans plan de transmission, la capacité de production et la qualité qui fondent les marges sont en jeu, au moment où l'appel d'offres demanderait des volumes supplémentaires.

**Dépendance envers le groupe (0,5 pt).**
- **Approvisionnements** : l'usine de Bienne est le seul fournisseur des charnières en titane et des verres solaires, soit 5,40 M€ et **31,58 %** des achats consommés en 2026 (29,95 % en 2025). Une rupture à Bienne arrêterait l'assemblage.
- **Prix** : ils sont fixés par la holding, sans mise en concurrence, en francs suisses : + 3 % en 2026, + 4 % annoncés pour 2027, auxquels s'ajoute la hausse du franc (cours moyen 0,9400 → 0,9200, environ 0,11 M€ de surcoût en 2026). Les achats à Bienne augmentent de 17,39 % en euros pour 14,89 % en francs suisses. La marge se répartit entre Bienne et Oyonnax selon une décision du groupe : la rentabilité de VERMONDAZ n'est donc pas entièrement le fruit de sa propre gestion.
- **Financement et distribution** : le compte courant (4,50 M€, **34,88 %** de la DFN) est remboursable à la demande de la holding, et le dividende (2,40 M€, 52,63 % du résultat de 2025) est fixé par elle, même quand le flux disponible ne le couvre pas.

**Gouvernance et relation d'agence (0,5 pt).** Au sens de Jensen et Meckling (1976), la holding (principal) délègue la gestion de VERMONDAZ à M. CHAVEROT (agent). Les intérêts peuvent diverger et l'information est asymétrique : le président connaît mieux le marché américain, les stocks et les ateliers que la holding.
- **Mécanismes de contrôle** : nomination pour trois ans et révocation à tout moment, budget approuvé, reporting mensuel, accord préalable pour les investissements, les emprunts, les couvertures de plus de douze mois ou optionnelles et les appels d'offres de plus de 5 M$ : l'appel d'offres de CORRINDALE et le choix de sa couverture (question 1.7) relèvent de la holding. Il n'y a ni conseil ni administrateur indépendant au niveau de la filiale : le contrôle passe tout entier par l'associé unique.
- **Mécanisme d'incitation imparfait** : une part variable assise à 100 % sur l'EBITDA encourage la croissance des volumes, mais ne tient compte ni des stocks (BFR de 111 jours), ni du flux disponible, ni des indicateurs sociaux. Un critère de flux de trésorerie ou de BFR, et un critère extra-financier (transmission, sécurité), aligneraient mieux le président sur la création de valeur durable.
- **Conflit entre le groupe et la filiale** : la holding arbitre les prix de Bienne, le dividende et le compte courant au mieux du groupe ; la direction de VERMONDAZ, jugée sur l'EBITDA de la filiale, supporte des hausses de prix qu'elle ne décide pas. Les parties prenantes de la filiale (salariés d'Oyonnax, banques, client américain) ont intérêt à une filiale autonome financièrement, dans une lecture partenariale (Freeman, 1984).

**Synthèse hiérarchisée (1 pt).**

| | Constats |
|---|---|
| **Forces** | croissance de 10,36 % à taux de change constants, deux fois le panel, portée par les États-Unis et l'Europe ; rentabilité supérieure au panel (ROCE 14,05 % contre 12,00 %, marge opérationnelle 12,59 % contre 11,00 %) ; savoir-faire de fabrication reconnu ; endettement modéré (DFN / EBITDA 1,30, sous l'engagement de 2,00) ; appartenance à un groupe qui fournit composants et financement |
| **Faiblesses** | marges en érosion (− 1,15 point de marge opérationnelle) ; stocks et BFR excessifs (108 et 111 jours contre 95 et 90), collections anciennes ; flux disponible faible (2,41 % du chiffre d'affaires) et dividende financé par le compte courant ; trésorerie de 1,70 M€ ; incitation du président assise sur le seul EBITDA |
| **Risques** | change de transaction des deux côtés (dollar à la baisse, franc suisse à la hausse : questions 1.5 à 1.7) et de conversion ; perte du savoir-faire (35 % de 55 ans et plus) ; dépendance envers Bienne et envers les décisions de la holding (prix, dividende, remboursement du compte courant) ; accidents du travail en hausse ; éligibilité RSE à l'appel d'offres (question 1.4) |

Recommandations attendues, en lien avec le cas (deux suffisent) : un plan de transmission (apprentis, tutorat par les seniors, fidélisation des jeunes formés) ; une réduction des stocks (collections anciennes, stock américain dimensionné sur les ventes) ; une politique de couverture du change (questions 1.5 à 1.7) ; une révision de la part variable du président (flux disponible, BFR, sécurité) ; une discussion avec la holding sur un dividende aligné sur le flux disponible et sur la monnaie de facturation de Bienne.

**Réponses tolérées** : analyse en forces, faiblesses, opportunités et menaces ; mention de la double matérialité pour le savoir-faire et la sécurité (impact sur les salariés, effet sur la capacité de production) ; agence présentée entre la famille ALDENWYL et les dirigeants du groupe, si elle est reliée à la filiale.

**Erreurs fréquentes**
- Analyser les prix de Bienne sous l'angle fiscal ou juridique : ils ne sont qu'un fait de dépendance et de partage de la marge au sein du groupe.
- Attribuer la théorie des parties prenantes à Jensen et Meckling, ou citer Jensen et Meckling sans en tirer de conséquence pour le cas (`JUR-D02`, `JUR-M01`).
- Lister les indicateurs sociaux sans les relier à la capacité de production, aux marges et à l'appel d'offres (`JUR-T05`) ; `JUR-D01` — confusion entre RSE et critères ESG ; `JUR-T13` — synthèse sans chiffres.

Références : programme 2.1 l. 476-485 et guide p. 59 (éléments extra-financiers reliés au modèle d'affaires et aux risques ; gouvernance, théorie de l'agence, valeur actionnariale et partenariale) [V] ; F08 § 1.1 et § 2 ; F10 § 3 ; F04 § 0 (synthèse hiérarchisée) [V guide p. 57].

---

### 1.4 Note RSE de fournisseur, éligibilité, limites et actions (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Indicateurs : recyclage 23,4 / 60,0 = 39,00 % ; taux de fréquence 30,00 ; formation 14 h ; intensité 1 026 / 54,00 = 19,00 t par M€ ; achats 80 % ; éthique 3 points. Points 2, 2, 2, 5, 4, 3 ; note 3,00 | 1 |
| 1.4-02 | Catégorie C, non éligible : il manque 0,50 point ; l'offre n'est recevable que si la catégorie B est atteinte en septembre 2027 sur données vérifiées | 0,25 |
| 1.4-03 | Portée et limites : données déclaratives, vérification et coût, divergence entre évaluateurs (64/100 « confirmé » ailleurs), pondérations propres au client, effets de seuil, périmètre de mesure (émissions d'Oyonnax rapportées au chiffre d'affaires consolidé), critères non matériels ou absents (savoir-faire), notation qui reste une opinion | 0,75 |
| 1.4-04 | Actions prioritaires, rattachées à la règle de réévaluation : recyclage d'au moins 55 % des chutes sur les trois mois précédant la décision (+ 0,50) et audit social externe (+ 0,10), note 3,60, catégorie B ; avec un dispositif d'alerte, 3,70 ; sécurité et formation, mesurées sur 2026, relèvent d'actions de fond ; coût et calendrier | 0,5 |

**Calcul de la note (1 pt).**

| Critère | Valeur de VERMONDAZ (2026) | Points | Poids | Poids × points |
|---|---:|---:|---:|---:|
| Chutes recyclées | 23,4 / 60,0 = 39,00 % (< 40 %) | 2 | 25 % | 0,50 |
| Taux de fréquence | 12 × 1 000 000 / 400 000 = 30,00 (≤ 34) | 2 | 20 % | 0,40 |
| Formation | 14 h (≥ 12) | 2 | 10 % | 0,20 |
| Intensité des émissions | 1 026 / 54,00 = 19,00 t CO2e par M€ (≤ 20) | 5 | 20 % | 1,00 |
| Achats auprès de signataires d'une charte | 80 % (≥ 75 %) | 4 | 15 % | 0,60 |
| Éthique des affaires | code signé, sans audit externe | 3 | 10 % | 0,30 |
| **Note** | | | **100 %** | **3,00** |

**Éligibilité (0,25 pt).** Avec 3,00, VERMONDAZ est en **catégorie C, non éligible** (seuil de B : 3,50). Il lui manque 0,50 point. Son offre ne sera recevable que si elle atteint la catégorie B **en septembre 2027**, sur des données vérifiées par l'auditeur de la chaîne. Le risque de l'appel d'offres est donc double : être retenue sur le prix, et l'être sur la note RSE.

**Portée et limites d'une notation extra-financière de fournisseur (0,75 pt).**
- **Portée** : la note devient une condition d'accès au marché, au même titre que le prix ; elle traduit la gestion des risques ESG de la chaîne sur sa chaîne d'approvisionnement (sécurité, environnement, éthique) et peut ouvrir un contrat de trois ans. Elle oblige VERMONDAZ à mesurer et à piloter des indicateurs qu'elle publie déjà.
- **Données déclaratives** : les indicateurs sont fournis par le fournisseur lui-même ; la chaîne exige donc une vérification par un auditeur qu'elle choisit, payée par le fournisseur (14 000 €). Sans vérification, la note n'aurait qu'une fiabilité limitée.
- **Divergence entre évaluateurs** : la plateforme du distributeur allemand classe VERMONDAZ au niveau « confirmé » (64/100) sur un simple questionnaire, alors que la grille de CORRINDALE la juge non éligible. Les méthodes diffèrent (critères, poids, sources, vérification) : une note n'a de sens que rapportée à sa méthode, et le fournisseur doit gérer plusieurs évaluations aux exigences différentes.
- **Coût** : audit de vérification (14 000 €), audit social (9 000 €), abonnement aux plateformes (4 000 € par an), temps interne ; il pèse davantage sur une entreprise de 290 salariés que sur un grand groupe.
- **Effets de seuil et de pondération** : à 39,00 % de chutes recyclées, VERMONDAZ manque d'un point le palier de 40 % ; la note agrège des critères compensables (l'excellente intensité des émissions compense en partie un mauvais taux de fréquence). Ce critère est d'ailleurs flatté par le périmètre : les émissions du seul site d'Oyonnax sont rapportées au chiffre d'affaires consolidé, dont 40 % est réalisé par une filiale dont les émissions (entrepôt, logistique) ne sont pas comptées. Les poids sont ceux du client, pas forcément les enjeux les plus matériels pour VERMONDAZ : la grille ignore la transmission des savoir-faire, enjeu majeur relevé à la question 1.3.
- Depuis le 2 juillet 2026, les notations ESG publiées par des fournisseurs de notation exerçant dans l'Union relèvent du règlement (UE) 2024/3005 ; une grille d'évaluation interne d'un client, comme celle de CORRINDALE, reste une évaluation privée (mention valorisée, non exigée).

**Actions prioritaires (0,5 pt).** Selon la règle de réévaluation de l'annexe 1.4, seuls deux critères peuvent changer avant la décision : le recyclage, mesuré sur les trois mois qui la précèdent si une nouvelle filière est en place (juin à août 2027, avec le régénérateur), et l'éthique des affaires, appréciée à la date de la décision. Les autres indicateurs restent ceux de 2026 :

| Action | Effet sur la note | Note obtenue | Délai et coût |
|---|---:|---:|---|
| Contrat avec le régénérateur d'acétate pour 55 % au moins des chutes (il propose jusqu'à 60 %) | 2 → 4 points : + 0,50 | 3,50 : catégorie B, sans aucune marge | dès juin 2027 ; coût logistique faible |
| Audit social externe | 3 → 4 points : + 0,10 | **3,60 : catégorie B** | deux mois ; 9 000 € |
| Audit social externe et dispositif d'alerte | 3 → 5 points : + 0,20 | 3,70 : catégorie B | quelques semaines de plus |
| Recyclage limité à 40 % | 2 → 3 points : + 0,25 | 3,25 (3,35 avec l'audit) : catégorie C | insuffisant |

La combinaison du recyclage d'au moins 55 % des chutes et de l'audit social donne **3,60**, en catégorie B, avec une marge de 0,10 point qui protège d'une correction des données par l'auditeur ; le dispositif d'alerte, mis en place en même temps que l'audit, porte la note à 3,70 et accroît cette marge. Les actions sur la sécurité et la formation restent nécessaires au-delà de l'appel d'offres, mais elles ne jouent pas en septembre, la grille retenant pour elles les indicateurs de 2026 : plan de prévention des accidents (un taux de fréquence de 26 ou moins rapporterait 0,20 point lors des évaluations suivantes), reprise de la formation et de l'apprentissage (question 1.3).

**Réponses tolérées** : actions prioritaires limitées au recyclage, à l'audit et au dispositif d'alerte dans n'importe quelle combinaison qui atteint 3,50, si le seuil sans marge est signalé ; note exprimée sur 100 (60/100) si l'échelle est convertie de façon cohérente ; recyclage rapporté à l'acétate consommé (29,25 %), si le candidat signale que la grille vise les chutes : la conclusion (2 points) est inchangée.

**Erreurs fréquentes**
- Arrondir 39,00 % à 40 % pour obtenir 3 points : seule une valeur égale à une borne donne le palier le plus favorable. Ou calculer une moyenne simple des points : elle donne ici aussi 3,00, par coïncidence, mais la méthode n'est pas celle de la grille et ne permet pas de mesurer l'effet des actions (un point de recyclage vaut 0,25, un point d'éthique 0,10).
- Proposer des actions dont l'effet ne peut pas être mesuré avant septembre 2027 comme seules réponses.
- Présenter la note comme une mesure objective de la performance RSE, sans discuter la méthode (`JUR-D01`) ; `JUR-T13` — limites générales de la notation sans les chiffres du cas.

Références : programme 2.1 l. 490 (mesures ESG et scoring) et guide p. 60-61 (calculer un score à partir d'une grille fournie) [V] ; F08 § 3.1 à 3.3 (marché de la notation ESG, divergences, règlement (UE) 2024/3005, méthode de calcul) [V Cellar pour le règlement].

---

### 1.5 Position de change et sensibilité (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | Positions par trimestre : USD + 4,20 ; + 3,80 ; + 4,80 ; + 4,20 M$ (+ 17,00 M$ sur douze mois, 14 655 172 €) ; CHF − 1,30 ; − 1,20 ; − 1,40 ; − 1,30 M CHF (− 5,20 M CHF, 5 591 398 €) | 0,5 |
| 1.5-02 | Qualification : position longue ouverte en dollars (risque de baisse du dollar, hausse du cours EUR/USD) ; position courte ouverte en francs suisses (risque de hausse du franc, baisse du cours EUR/CHF) ; risques qui se cumulent | 0,5 |
| 1.5-03 | Variation de 5 % : − 732 759 € sur le dollar, − 279 570 € sur le franc suisse, − 1 012 329 € au total (14,89 % du résultat opérationnel de 2026) | 0,5 |

**Position par trimestre et sur douze mois (0,5 pt).** La position de change d'une devise est la différence entre ce que le sous-groupe recevra et ce qu'il paiera dans cette devise ; les décaissements en dollars de la filiale se compensent avec ses encaissements dans la même devise.

| Millions de devises | T2 2027 | T3 2027 | T4 2027 | T1 2028 | 12 mois | Contre-valeur au 1er avril (€) |
|---|---:|---:|---:|---:|---:|---:|
| Encaissements USD | 6,40 | 6,00 | 7,20 | 6,40 | 26,00 | |
| Décaissements USD | − 2,20 | − 2,20 | − 2,40 | − 2,20 | − 9,00 | |
| **Position USD** | **+ 4,20** | **+ 3,80** | **+ 4,80** | **+ 4,20** | **+ 17,00** | 17 000 000 / 1,16 = **14 655 172** |
| Contre-valeur (€) | 3 620 690 | 3 275 862 | 4 137 931 | 3 620 690 | | |
| **Position CHF** | **− 1,30** | **− 1,20** | **− 1,40** | **− 1,30** | **− 5,20** | 5 200 000 / 0,93 = **5 591 398** |
| Contre-valeur (€) | 1 397 849 | 1 290 323 | 1 505 376 | 1 397 849 | | |

Aux dates de conversion et de règlement : + 8,00 M$ et − 2,50 M CHF le 30 septembre 2027 ; + 9,00 M$ et − 2,70 M CHF le 31 mars 2028.

**Qualification (0,5 pt).**
- **Dollar : position longue et ouverte** (chaque trimestre et sur l'année) : le sous-groupe détiendra des dollars non couverts ; il craint la **baisse du dollar**, c'est-à-dire une **hausse** du cours EUR/USD au certain. C'est ce qui s'est produit en 2025 et en 2026 (question 1.1).
- **Franc suisse : position courte et ouverte** : VERMONDAZ devra acheter des francs suisses ; elle craint la **hausse du franc**, c'est-à-dire une **baisse** du cours EUR/CHF.
- Les deux risques **ne se compensent pas** : dans un scénario de dollar faible et de franc fort, comme en 2026, ils se cumulent. Il n'y a aucune compensation naturelle entre deux devises différentes ; seule la compensation au sein du dollar (dépenses de la filiale) réduit déjà l'exposition de 26,00 à 17,00 M$.

**Effet d'une variation défavorable de 5 % (0,5 pt).** Par convention, la contre-valeur en euros d'une unité de devise varie de 5 %.

| | Contre-valeur au comptant | Variation défavorable | Effet sur les flux en euros |
|---|---:|---|---:|
| Dollar | 14 655 172 € | baisse de 5 % (cours 1,1600 / 0,95 = 1,2211) | **− 732 759 €** |
| Franc suisse | 5 591 398 € | hausse de 5 % (cours 0,9300 / 1,05 = 0,8857) | **− 279 570 €** |
| **Cumul** | | | **− 1 012 329 €** |

Une variation de 5 %, ordinaire sur une année, coûterait environ 1,01 M€, soit **14,89 %** du résultat opérationnel de 2026 (6,80 M€) et plus de 40 % du dividende. Le risque de change est donc significatif pour la filiale ; il justifie une politique de couverture, d'autant que le flux disponible est faible et la trésorerie réduite.

**Réponses tolérées** : variation appliquée au cours au certain (1,1600 × 1,05 = 1,2180 et 0,9300 × 0,95 = 0,8835), soit − 697 865 € et − 294 284 €, si la convention retenue est annoncée ; position présentée par semestre seulement, si le détail par trimestre est donné en annexe de la réponse.

**Erreurs fréquentes**
- Qualifier de courte la position en dollars d'un exportateur, ou indiquer qu'une hausse du cours EUR/USD est favorable à VERMONDAZ (`JUR-T12`).
- Retenir les encaissements bruts (26,00 M$) au lieu de la position nette des décaissements de la filiale.
- Additionner dollars et francs suisses en devises, sans les convertir en euros.
- `JUR-T07` — position présentée sans tableau.

Références : programme 6.3 l. 625-627 (position de change) et guide p. 78-79 [V] ; F07 § 3.1 (position longue, courte, ouverte, fermée ; sens du risque au certain).

---

### 1.6 Cours à terme, couverture à terme et termaillage (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.6-01 | Cours à terme : USD 1,1669 (6 mois, + 69 points) et 1,1715 (12 mois, + 115 points), l'euro est en report par rapport au dollar ; CHF 0,9196 (6 mois, − 104 points) et 0,9089 (12 mois, − 211 points), l'euro est en déport par rapport au franc suisse ; explication par l'écart de taux | 1 |
| 1.6-02 | Ventes à terme de dollars : 6 855 772 € et 7 682 458 € ; achats à terme de francs suisses : 2 718 573 € et 2 970 624 € ; écart avec le comptant (− 40 780 et − 76 163 € ; + 30 401 et + 67 398 €) : coût du différentiel de taux, pas une perte | 0,5 |
| 1.6-03 | Règlement anticipé : 2 661 290 € payés le 1er avril, soit 2 728 562 € au 30 septembre avec le compte courant à 5,00 %, contre 2 718 573 € à terme : surcoût de 9 989 € ; équilibre à un taux de 4,26 % ou à un escompte de 1,36 % | 0,5 |
| 1.6-04 | Intérêt et limites du termaillage : technique interne sans prime, mais besoin de trésorerie, accord du groupe, transfert de liquidité à l'intérieur du groupe ; retarder n'a d'intérêt que si la devise est attendue en baisse ; monnaie de facturation | 0,5 |

**Cours à terme (1 pt).** Par la parité des taux d'intérêt, une banque qui vend à terme une devise l'achète au comptant et place les fonds jusqu'à l'échéance : le cours à terme intègre l'écart de taux entre les deux devises.

| | Calcul | Cours à terme | Points de terme | Lecture |
|---|---|---:|---:|---|
| USD 6 mois (182 j) | 1,1600 × (1 + 3,70 % × 182 / 360) / (1 + 2,50 % × 182 / 360) = 1,1600 × 1,018706 / 1,012639 | **1,1669** | **+ 69** | euro en **report** |
| USD 12 mois (365 j) | 1,1600 × (1 + 3,60 % × 365 / 360) / (1 + 2,60 % × 365 / 360) = 1,1600 × 1,036500 / 1,026361 | **1,1715** | **+ 115** | euro en **report** |
| CHF 6 mois | 0,9300 × (1 + 0,25 % × 182 / 360) / (1 + 2,50 % × 182 / 360) = 0,9300 × 1,001264 / 1,012639 | **0,9196** | **− 104** | euro en **déport** |
| CHF 12 mois | 0,9300 × (1 + 0,30 % × 365 / 360) / (1 + 2,60 % × 365 / 360) = 0,9300 × 1,003042 / 1,026361 | **0,9089** | **− 211** | euro en **déport** |

Le dollar rapporte plus que l'euro : à terme, un euro vaut plus de dollars qu'au comptant (report de l'euro, déport du dollar). Le franc suisse rapporte moins que l'euro : à terme, un euro vaut moins de francs suisses (déport de l'euro, report du franc). Le cours à terme n'est pas une prévision du cours futur : il traduit seulement l'écart de taux.

**Couvertures à terme des deux échéances (0,5 pt).**

| Échéance | Opération | Montant en euros à terme | Au comptant du 1er avril | Écart |
|---|---|---:|---:|---:|
| 30/09/2027 | vente à terme de 8 000 000 $ à 1,1669 | **6 855 772** | 6 896 552 | − 40 780 |
| 31/03/2028 | vente à terme de 9 000 000 $ à 1,1715 | **7 682 458** | 7 758 621 | − 76 163 |
| 30/09/2027 | achat à terme de 2 500 000 CHF à 0,9196 | **2 718 573** | 2 688 172 | + 30 401 |
| 31/03/2028 | achat à terme de 2 700 000 CHF à 0,9089 | **2 970 624** | 2 903 226 | + 67 398 |

Les ventes à terme fixent 14 538 230 € de recettes et les achats à terme 5 689 197 € de dépenses : le solde de 8 849 033 € est connu dès le 1er avril et les positions sont **fermées**. Les écarts avec le comptant du jour ne sont pas une perte de change : ils mesurent le différentiel de taux (le dollar, mieux rémunéré, se vend « moins cher » à terme ; le franc suisse, moins rémunéré, s'achète « plus cher »). En contrepartie, VERMONDAZ renonce à tout gain si le dollar monte ou si le franc baisse. La couverture de flux certains par contrat à terme ferme convient ici : les flux viennent du carnet de commandes et des contrats ; les douze mois restent dans les pouvoirs du président (couverture de douze mois au plus, sans instrument optionnel).

**Termaillage : règlement anticipé à Bienne (0,5 pt).**

| | Calcul | Coût en euros au 30/09/2027 |
|---|---|---:|
| Règlement anticipé le 1er avril, escompte de 1,00 % | 2 500 000 × 0,99 / 0,9300 = 2 661 290 € payés le 1er avril, financés par le compte courant : 2 661 290 × (1 + 5,00 % × 182 / 360) | **2 728 562** |
| Achat à terme à 6 mois | 2 500 000 / 0,9196 | **2 718 573** |
| **Écart** | | **9 989 € en faveur de l'achat à terme** |

Le règlement anticipé supprime le risque de change dès aujourd'hui, comme le terme, et procure un escompte de 25 000 CHF. Mais il doit être financé au taux du compte courant (5,00 %), bien supérieur au taux de l'euro à 6 mois (2,50 %) qui fonde le cours à terme. Il ne deviendrait intéressant qu'avec un financement à moins de **4,26 %**, ou un escompte d'au moins **1,36 %** (au taux de 5,00 %). Si VERMONDAZ disposait d'une trésorerie placée au taux de l'euro à 6 mois, le règlement anticipé coûterait 2 694 926 € et serait meilleur que le terme (− 23 647 €) : c'est la source du financement qui décide.

**Intérêt et limites du termaillage (0,5 pt).**
- **Intérêt** : technique interne, sans prime ni contrepartie bancaire ; elle consiste à avancer un paiement dans une devise dont on craint la hausse (le franc suisse) et à retarder un encaissement dans une devise dont on attend la hausse, ou à faire l'inverse si l'on anticipe une baisse. Ici, retarder un règlement à Bienne n'aurait d'intérêt que si le franc était attendu en baisse au-delà de ce que dit le cours à terme ; or le franc est en report et le retard coûterait 5,00 % d'intérêts.
- **Limites** : il faut de la trésorerie (1,70 M€ seulement) ou un financement ; le gain dépend de l'escompte et du taux, fixés par le groupe ; à l'échelle du groupe, il ne fait que déplacer de la liquidité entre la holding, Bienne et VERMONDAZ, et l'escompte réduit la marge de Bienne. Il ne couvre que les flux intragroupe : les dollars, reçus de clients tiers, restent à couvrir.
- **Autre technique interne** : demander à la holding de facturer les composants de Bienne en euros. Le risque de change passerait au groupe, qui raisonne en francs suisses ; pour VERMONDAZ, la position courte en francs suisses disparaîtrait.

**Réponses tolérées** : cours à terme non arrondis ou montants calculés avec quatre décimales différentes (écarts de quelques euros) ; cours à terme du dollar à 6 mois de 1,1670 (+ 70 points ; 6 855 184 €), dû à un arrondi intermédiaire du rapport des facteurs, la valeur exacte 1,166950 étant à la limite de l'arrondi ; comparaison du termaillage menée en valeur au 1er avril (2 718 573 / 1,025278 = 2 651 548 € à comparer à 2 661 290 €), si la méthode est cohérente ; report et déport exprimés du point de vue de la devise (dollar en déport, franc en report), s'ils sont exacts.

**Erreurs fréquentes**
- Inverser la formule au certain (taux de l'euro au numérateur) : cours à terme du dollar inférieur au comptant.
- Présenter l'écart entre terme et comptant comme une perte de change ou comme une commission.
- Comparer le règlement anticipé et le terme à des dates différentes, sans capitaliser le décaissement du 1er avril.
- Proposer une compensation multilatérale ou une centralisation de trésorerie, qui ne répondent pas à la question posée ; `JUR-T13` — techniques internes énumérées sans chiffrage.

Références : programme 6.3 l. 626-631 (marché au comptant et à terme ; termaillage, indexation ; forward de devises) et guide p. 78-79 [V] ; F07 § 3.2 et § 3.3 (parité des taux, report et déport, techniques internes).

---

### 1.7 Risque conditionnel de l'appel d'offres : terme, option, garantie de change, indexation (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.7-01 | Risque conditionnel : prix ferme en dollars remis en mai, recette incertaine jusqu'en septembre (une chance sur deux) ; une couverture ferme deviendrait une position ouverte si l'offre est perdue | 0,25 |
| 1.7-02 | Prime : 3,60 % × 6 000 000 = 216 000 $, soit 186 207 € ; valeur intrinsèque 6 000 000 / 1,15 − 6 000 000 / 1,16 = 44 978 € ; valeur temps 141 229 € | 0,5 |
| 1.7-03 | Tableau des résultats : gagné (terme 5 121 639 € ; option 5 369 349 / 5 031 184 / 5 031 184 € ; garantie 5 301 880 / 5 110 309 / 5 069 890 €) ; perdu (terme − 433 917 / − 50 775 / + 359 734 € ; option − 186 207 / − 141 229 / + 269 280 € ; garantie − 15 000 €) | 1 |
| 1.7-04 | Clause d'indexation : tunnel de ± 5 % gardé par VERMONDAZ, partage de moitié au-delà (à 1,2600 : écart de 8,62 %, prix relevé de 1,81 %) ; protection partielle et symétrique des années 2 et 3 | 0,25 |
| 1.7-05 | Recommandation argumentée, compatible avec les pouvoirs délégués par la holding | 0,5 |

**Un risque conditionnel (0,25 pt).** En remettant en mai un prix ferme en dollars, VERMONDAZ s'expose à une baisse du dollar avant l'encaissement du 31 mars 2028. Mais la recette n'existera que si l'offre est retenue en septembre (une chance sur deux selon VERMONDAZ, sous réserve de la note RSE : question 1.4). Le risque est donc **conditionnel** : couvrir par un contrat ferme, c'est risquer, si l'offre est perdue, de devoir livrer des dollars que l'entreprise n'aura pas. La couverture adaptée doit protéger si l'offre est gagnée et coûter peu, et de façon limitée, si elle est perdue.

**Prime de l'option (0,5 pt).** Option de vente de dollars (achat d'euros), prix d'exercice 1,1500 :
- prime = 3,60 % × 6 000 000 $ = 216 000 $, soit 216 000 / 1,1600 = **186 207 €** ;
- **valeur intrinsèque** = max (0 ; 6 000 000 / 1,15 − 6 000 000 / 1,16) = 5 217 391 − 5 172 414 = **44 978 €** : l'option est dans la monnaie, car elle permet de vendre les dollars à 1,1500, mieux que le comptant du jour (1,1600) ;
- **valeur temps** = 186 207 − 44 978 = **141 229 €** : c'est le prix de la possibilité de gain d'ici un an (76 % de la prime), que l'acheteur perd si le cours n'évolue pas.
La prime est donnée par la banque : aucun modèle d'évaluation n'est à mobiliser.

**Résultats selon le cours et l'issue de l'appel d'offres (1 pt).** Montants en euros au 31 mars 2028 (primes non capitalisées).

*Appel d'offres gagné : euros obtenus pour 6 000 000 $*

| Cours au 31/03/2028 | Sans couverture | Vente à terme à 1,1715 | Option (prime déduite) | Garantie de change (primes déduites) |
|---|---:|---:|---:|---:|
| 1,0800 (dollar en hausse) | 5 555 556 | 5 121 639 | abandon : 5 555 556 − 186 207 = **5 369 349** | gain de 427 350 par rapport au cours garanti, 213 675 reversés : 5 341 880 − 40 000 = **5 301 880** |
| 1,1600 (stabilité) | 5 172 414 | 5 121 639 | exercice : 5 217 391 − 186 207 = **5 031 184** | gain de 44 209, 22 104 reversés : 5 150 309 − 40 000 = **5 110 309** |
| 1,2600 (dollar en baisse) | 4 761 905 | 5 121 639 | exercice : **5 031 184** | perte de 366 300 par rapport à 5 128 205, indemnité de 95 % = 347 985 : 5 109 890 − 40 000 = **5 069 890** |

*Appel d'offres perdu : résultat net en euros*

| Cours au 31/03/2028 | Vente à terme (dollars achetés au comptant pour livrer) | Option (exercée seulement si elle rapporte) | Garantie de change |
|---|---:|---:|---:|
| 1,0800 | 5 121 639 − 5 555 556 = **− 433 917** | abandon : **− 186 207** | **− 15 000** |
| 1,1600 | 5 121 639 − 5 172 414 = **− 50 775** | 44 978 − 186 207 = **− 141 229** | **− 15 000** |
| 1,2600 | 5 121 639 − 4 761 905 = **+ 359 734** | 455 487 − 186 207 = **+ 269 280** | **− 15 000** |

Lecture :
- **Vente à terme** : la meilleure solution si l'offre est gagnée et le dollar faible ou stable, et la plus simple ; mais si l'offre est perdue, elle devient une **position spéculative** (perte de 433 917 € si le dollar monte). Elle ne convient qu'une fois le contrat obtenu.
- **Option** : la seule qui garde tout le gain si le dollar monte (5 369 349 €) ; elle est meilleure que le terme si le cours final est inférieur à 6 000 000 / (5 121 639 + 186 207) = **1,1304**. Si l'offre est perdue, la perte est **plafonnée à la prime** (186 207 €). Mais la prime est élevée (3,60 % du nominal), et l'instrument optionnel exige l'accord préalable de la holding. Si l'offre est perdue en septembre, l'option pourrait être revendue pour sa valeur temps restante (non chiffrée), ce qui réduirait la perte.
- **Garantie de change publique** : conçue pour la période de négociation. Si l'offre est perdue, elle ne coûte que **15 000 €**, quel que soit le cours. Si elle est gagnée, elle protège presque comme le terme (5 069 890 € au pire, contre 5 121 639 €), tout en laissant à VERMONDAZ la moitié du gain si le dollar monte. Ses limites : quotité de 95 % (5 % de la perte reste à la charge de l'entreprise), partage des gains, primes, démarches et délais de l'assureur.

**Clause d'indexation (0,25 pt).** Pour les années 2 et 3, la clause partage le risque avec le client : VERMONDAZ garde les variations jusqu'à ± 5 % autour de 1,1600, puis la moitié de l'écart au-delà. Exemple : à un cours moyen de 1,2600, l'écart est de 1,26 / 1,16 − 1 = 8,62 % ; le prix en dollars serait relevé de (8,62 % − 5 %) / 2 = **1,81 %**, ce qui ne compense qu'une partie de la baisse du dollar. La clause est symétrique (le prix baisse si le dollar monte), révisée une fois par an et sur la moyenne de l'année écoulée : elle réduit le risque à long terme sans le supprimer. Elle est à accepter, en négociant si possible une franchise plus étroite ou un partage plus favorable, et elle ne dispense pas de couvrir chaque tranche annuelle.

**Recommandation (0,5 pt).** Exemple de recommandation (toute recommandation cohérente et argumentée est acceptée) :
- **flux certains des douze mois** : vendre à terme les dollars et acheter à terme les francs suisses des deux échéances, en totalité pour le 30 septembre 2027 et pour une part importante (par exemple 75 %) du 31 mars 2028, les prévisions de la fin de l'exercice étant moins sûres ; ne pas anticiper le règlement à Bienne aux conditions proposées (surcoût de 9 989 €), mais demander à la holding une facturation en euros ou un escompte plus élevé ;
- **appel d'offres** : souscrire la **garantie de change** de l'assureur-crédit public pendant la négociation (15 000 € de coût maximal si l'offre est rejetée), plutôt que l'option, trop chère pour une recette incertaine, et plutôt que le terme, spéculatif si l'offre est perdue ; si VERMONDAZ gagne, la garantie se poursuit jusqu'à l'encaissement de la première tranche ;
- **années 2 et 3** : accepter la clause d'indexation, couvrir chaque tranche à terme dès qu'elle est commandée ;
- **gouvernance** : soumettre la réponse à l'appel d'offres (plus de 5 M$) et la politique de couverture à la holding, en même temps que le plan d'actions RSE (question 1.4), sans lequel l'offre ne serait pas recevable.

Un candidat qui retient l'option, au motif qu'elle garde le gain si le dollar monte et plafonne la perte, obtient les points s'il en chiffre le coût, signale l'accord nécessaire de la holding et compare la perte maximale avec celle de la garantie.

**Réponses tolérées** : résultats des instruments exprimés par rapport à la situation sans couverture ; primes capitalisées au taux de l'euro, si l'hypothèse est annoncée ; vente à terme prise en septembre seulement, une fois le contrat obtenu, au cours à terme de ce jour (non chiffrable), présentée comme stratégie combinée avec la garantie.

**Erreurs fréquentes**
- Couvrir par une vente à terme ferme une recette qui n'existe pas encore, sans envisager l'échec de l'offre.
- Exercer l'option quand le cours final est inférieur au prix d'exercice (dollar fort), ou oublier la prime dans le résultat net.
- Calculer la valeur intrinsèque avec le cours à terme ou avec le cours final : la convention retient le cours comptant du jour.
- Décrire le régime juridique de la garantie publique ou nommer un produit réel : seules comptent les conditions de l'annexe ; `JUR-T13` — recommandation générale, sans lien avec les pouvoirs de la holding ni avec la note RSE.

Références : programme 6.3 l. 626-631 (garanties publiques, indexation, options de change, forward) et guide p. 79 (stratégie de couverture comparée selon le coût, la souplesse, la simplicité et le risque résiduel ; valeur intrinsèque et valeur spéculative de l'option, prime donnée) [V] ; F07 § 3.2 et § 3.3 (garantie de change avec intéressement, option de change, grille de choix).

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 57-58 ; programme l. 466-473 | démarche du diagnostic consolidé ; ROCE, ROE, effet de levier ; flux de trésorerie ; lecture d'une norme IFRS sans technique comptable | [V] | F04 § 0 à 6 |
| Guide pédagogique DSCG, juillet 2026, p. 59-61 ; programme l. 476-490 | éléments extra-financiers reliés au modèle d'affaires ; gouvernance et agence ; score ESG calculé sur une grille fournie | [V] | F08 § 1.1, § 2 et § 3 |
| Règlement (UE) 2024/3005 sur les activités de notation ESG, applicable depuis le 2 juillet 2026 | notations ESG publiées par des fournisseurs exerçant dans l'Union (mention facultative) | [V Cellar] | F08 § 3.2 |
| Guide pédagogique DSCG, juillet 2026, p. 78-79 ; programme l. 625-631 | position de change, marché au comptant et à terme, parité des taux, techniques internes, garanties publiques, options de change (prime donnée, valeur intrinsèque et valeur temps) | [V] | F07 § 3 |
| Jensen et Meckling (1976) | théorie de l'agence, mécanismes de contrôle et d'incitation | [V programme 2.1] | F10 § 3 ; F08 § 1.1 |
| Freeman (1984) | approche partenariale | [V programme 2.1] | F10 § 3 |
| Comptes, panel, indicateurs extra-financiers, grille de CORRINDALE, flux en devises, cours et taux, conditions de l'option, de la garantie et de la clause d'indexation | hypothèses d'énoncé, fictives, à utiliser telles quelles | — | annexes 1.1 à 1.7 |
