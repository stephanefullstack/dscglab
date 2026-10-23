# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Exercice d'entraînement n° 2 — Dossier 2 (25 points)

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 restructurations, PCG titre VII (à jour au 23/10/2026) ; F02 fiscalité des restructurations (à jour au 22/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (titres émis, augmentation de capital, prime, mode de valorisation, écritures, barème).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification | `1.1.a` Définir les opérations de restructuration | 2 |
| 2.2 Titres émis | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 3 |
| 2.3 Mode de valorisation | `1.2.c` Déterminer le mode de valorisation des apports | 4 |
| 2.4 Valeur des apports, prime | `1.2.d` Calculer et composer les apports | 3 |
| 2.5 Écritures BORÉE | `1.3.a` Écritures chez la bénéficiaire et l'apporteuse | 4 |
| 2.6 Écritures ATLAS | `1.3.a` Écritures chez la bénéficiaire et l'apporteuse | 3 |
| 2.7 Régime fiscal | `1.1.b` Régime fiscal de droit commun et régime de faveur | 3 |
| 2.8 Capitaux propres et analyse | `1.4.a` Restituer au dirigeant les impacts de l'opération | 3 |
| **Total** | | **25** |

---

### 2.1 Qualification de l'opération (2 pts)

Il s'agit d'un **apport partiel d'actif** : ATLAS apporte un ensemble d'actifs et de passifs constituant une branche autonome, et reçoit en échange des titres de la bénéficiaire, BORÉE [V PCG art. 710-2] (1 pt).

Différences (1 pt) :
- avec une **fusion** : ATLAS ne disparaît pas. Elle continue d'exploiter ses deux autres divisions, et ce sont ATLAS elle-même, et non ses associés, qui reçoit les titres BORÉE ;
- avec une **cession** : la contrepartie n'est pas du numéraire mais des titres de la bénéficiaire. ATLAS reste ainsi indirectement exposée à l'activité apportée.

---

### 2.2 Titres émis et répartition du capital (3 pts)

**Valeur réelle d'une action BORÉE (0,5 pt)** : 2 400 000 / 40 000 = **60 €**.

**Actions à émettre (1 pt)** : la rémunération est calculée sur la **valeur réelle** de la branche, qui exprime le rapport de valeurs entre les parties : 3 600 000 / 60 = **60 000 actions**.

**Augmentation de capital (0,5 pt)** : 60 000 × 10 = **600 000 €**.

**Répartition du capital après l'opération (1 pt)** — 100 000 actions :

| Actionnaire | Avant | Après | % après |
|---|---:|---:|---:|
| ATLAS | 0 | 60 000 | **60 %** |
| Famille DUVAL | 28 000 | 28 000 | 28 % |
| Autres actionnaires | 12 000 | 12 000 | 12 % |
| **Total** | **40 000** | **100 000** | **100 %** |

---

### 2.3 Mode de valorisation des apports (4 pts)

**Situation de contrôle (1 pt).** Avant l'opération, ATLAS et BORÉE n'ont aucun lien en capital et ne sont pas contrôlées par une même entité : l'opération est réalisée **sous contrôle distinct** [V PCG art. 741-1].

**Sens de l'opération (1,5 pt).** Un apport est **à l'envers** lorsque l'apporteuse prend le contrôle de la bénéficiaire [V PCG art. 742-2]. Avec 60 % du capital après l'opération, ATLAS prend le contrôle de BORÉE, tandis que la famille DUVAL, qui détenait 70 %, n'en a plus que 28 %. L'apport est donc **à l'envers**. Économiquement, l'initiatrice est ATLAS et la cible est BORÉE [V art. 730-1].

**Conclusion (1,5 pt).** Pour une opération sous contrôle distinct à l'envers, les apports sont évalués à la **valeur comptable** [V PCG art. 743-1, cas 3]. La cible étant BORÉE, ce sont ses actifs qui changent de contrôle. Or ils ne figurent pas dans le traité : seuls y figurent les éléments apportés par l'initiatrice, qu'il n'y a pas lieu de réévaluer.

---

### 2.4 Valeur des apports et prime d'apport (3 pts)

**Valeur comptable des apports (1 pt)**

| Élément | Montant |
|---|---:|
| Entrepôts (VNC) | 1 200 000 |
| Camions (VNC) | 400 000 |
| Emballages | 100 000 |
| Créances clients | 300 000 |
| – Provision pour litige | – 20 000 |
| – Dettes fournisseurs | – 180 000 |
| **Actif net comptable apporté** | **1 800 000** |

**Prime d'apport (1 pt)** : 1 800 000 – 600 000 = **1 200 000 €**.

**Libération du capital (1 pt).** L'actif net comptable apporté (1 800 000 €) couvre l'augmentation de capital (600 000 €). La dérogation de l'art. 743-3, qui imposerait les valeurs réelles en cas d'insuffisance, ne joue pas [V PCG art. 743-3].

Le nombre de titres est calculé sur la valeur réelle (3 600 000), mais l'apport est comptabilisé à la valeur comptable (1 800 000). Les deux ne se contredisent pas : la valeur réelle sert à fixer le rapport d'échange, la valeur comptable à enregistrer les apports.

---

### 2.5 Écritures chez BORÉE au 01/01/2027 (4 pts)

Écritures complètes dans `corrige.yaml` (B1, B2), toutes équilibrées. Schéma type : `gabarits/ecritures_types/05_apport_partiel_actif.yaml`.

**B1 — Augmentation de capital (1,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 1 800 000 | |
| 101 Capital | | 600 000 |
| 1043 Primes d'apport | | 1 200 000 |

**B2 — Réalisation de l'apport (2,5 pts).** En valeur comptable, la bénéficiaire reprend les **valeurs brutes et les amortissements** de l'apporteuse [V BOI-IS-FUS-10-20-40-20 § 170-180, voir F01 § 3.2].

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments | 2 000 000 | |
| 2182 Matériel de transport | 1 000 000 | |
| 326 Emballages | 100 000 | |
| 411 Clients | 300 000 | |
| 28131 Amortissements des bâtiments | | 800 000 |
| 28182 Amortissements du matériel de transport | | 600 000 |
| 1511 Provisions pour litiges | | 20 000 |
| 401 Fournisseurs | | 180 000 |
| 4561 Associés – Comptes d'apport en société | | 1 800 000 |

---

### 2.6 Écritures chez ATLAS au 01/01/2027 (3 pts)

**A1 — Sortie de la branche et réception des titres (2 pts).** ATLAS inscrit les titres BORÉE reçus pour la valeur de l'apport retenue au traité, soit la valeur comptable [F01 § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation (60 000 titres BORÉE) | 1 800 000 | |
| 28131 Amortissements des bâtiments | 800 000 | |
| 28182 Amortissements du matériel de transport | 600 000 | |
| 1511 Provisions pour litiges | 20 000 | |
| 401 Fournisseurs | 180 000 | |
| 2131 Bâtiments | | 2 000 000 |
| 2182 Matériel de transport | | 1 000 000 |
| 326 Emballages | | 100 000 |
| 411 Clients | | 300 000 |

**Résultat de l'opération (1 pt).** Aucun résultat n'est dégagé : les titres sont inscrits pour la valeur nette des éléments apportés (1 800 000 €). Les éléments de la division sont simplement remplacés à l'actif d'ATLAS par une participation de même montant.

*Variante admise :* passage par un compte de créance sur la bénéficiaire (compte 46), soldé à la réception des titres. Les comptes 675 et 775 sont à proscrire : ils ont été supprimés du PCG en 2026 [F99].

---

### 2.7 Régime fiscal (3 pts)

**Condition (1 pt).** L'apport bénéficie de plein droit du régime de faveur des fusions (art. 210 A) s'il porte sur une ou plusieurs **branches complètes d'activité** [V CGI art. 210 B-1]. La branche complète est « l'ensemble des éléments d'actif et de passif d'une division d'une société qui constituent, du point de vue de l'organisation, une exploitation autonome, c'est-à-dire un ensemble capable de fonctionner par ses propres moyens » [V BOI-IS-FUS-20-20 § 10]. Son autonomie s'apprécie selon l'organisation de l'apporteuse, à la date de réalisation de l'apport [V même BOI § 20 et 90]. Depuis le 01/01/2018, aucun engagement de conservation des titres n'est exigé [V BOI-IS-FUS-20-40, remarque]. À défaut de branche complète, le régime de faveur n'est possible que sur agrément [V CGI art. 210 B-3].

**Appréciation (0,5 pt).** La condition est remplie [V BOI-IS-FUS-20-20 § 50 à 90] :
- **activité réellement exercée** et organisation distincte des autres divisions (centre de profit autonome) ;
- **installations, clientèle et personnel propres**, le personnel étant transféré avec l'activité ;
- l'apport ne porte pas sur des **éléments isolés** : les entrepôts et les camions sont apportés avec l'exploitation qui les utilise ;
- le recours temporaire aux **services administratifs communs** d'ATLAS ne fait pas obstacle à l'autonomie : ces services sont rattachés aux branches pour leur quote-part.

**Conséquences (1,5 pt)**
- **ATLAS** : la plus-value réalisée lors d'une cession ultérieure des titres BORÉE sera calculée par référence à la **valeur fiscale qu'avaient les biens apportés** dans ses écritures [V CGI art. 210 B-2]. Ici, cette valeur est égale à la valeur comptable des titres (1 800 000 €) : la plus-value latente de 1 800 000 € (3 600 000 – 1 800 000) sera imposée lors de la cession des titres.
- **Provision pour litige** : chez ATLAS, elle n'est pas imposée du fait de l'apport ; elle ne le serait que si elle était devenue sans objet [V BOI-IS-FUS-20-40-30 § 110]. Chez BORÉE, la bénéficiaire reprend les provisions de l'apporteuse afférentes aux éléments apportés [V CGI art. 210 A-3-a, applicable aux APA par renvoi du 210 B-1]. Les 20 000 €, déduits par ATLAS, seront compris dans le résultat imposable de BORÉE lors de leur reprise, si la provision devient sans objet.

---

### 2.8 Capitaux propres de BORÉE et analyse (3 pts)

**Capitaux propres (1 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital | 400 000 | + 600 000 | 1 000 000 |
| Primes d'apport | 0 | + 1 200 000 | 1 200 000 |
| Réserves | 1 100 000 | | 1 100 000 |
| **Total** | **1 500 000** | **+ 1 800 000** | **3 300 000** |

**Explication pour la famille DUVAL (grille de niveaux, 2 pts)**

| Niveau | 0 | 1 | 1,5 | 2 |
|---|---|---|---|---|
| Attendu | Absence ou explication erronée | Rappel de la règle (contrôle distinct, envers, valeur comptable) | Règle et justification économique | Règle, justification et chiffrage de l'alternative |

Idées attendues :
- **Pourquoi la valeur comptable** : économiquement, ce n'est pas BORÉE qui acquiert la division, c'est ATLAS qui prend le contrôle de BORÉE. Les actifs qui changent de contrôle sont ceux de BORÉE ; ceux de la division restent sous le contrôle d'ATLAS et ne sont pas réévalués. Comptabiliser la division à sa valeur réelle reviendrait à constater chez BORÉE une plus-value sur des actifs dont le contrôle ne change pas.
- **Ce qu'aurait changé la valeur réelle** :
  - chez BORÉE, actifs réévalués (entrepôts + 500 000, camions + 100 000) et fonds commercial de 1 200 000 € (3 600 000 – 2 400 000 d'actif net réel identifié), soit des amortissements futurs plus élevés ;
  - prime d'apport de 3 000 000 € au lieu de 1 200 000 € ;
  - chez ATLAS, titres inscrits pour 3 600 000 € et plus-value d'apport de 1 800 000 €.
- **Pour la famille DUVAL** : elle perd le contrôle de BORÉE (de 70 % à 28 %), bien que les capitaux propres comptables passent de 1 500 000 € à 3 300 000 €. C'est la conséquence de la valeur relative des apports, la division valant 1,5 fois BORÉE.

---

### Réponses tolérées
- **2.2** : calcul du nombre de titres par un rapport de valeurs (3 600 000 / 2 400 000 = 1,5 titre émis pour 1 titre existant, soit 40 000 × 1,5 = 60 000).
- **2.6** : passage par un compte de créance (46) sur la bénéficiaire, soldé à la réception des titres.
- **2.7** : tout raisonnement correct sur le sort de la provision, même sans la référence au 210 A-3-a.

### Erreurs fréquentes
- Retenir la **valeur réelle** au motif que les sociétés sont sous contrôle distinct, sans analyser le **sens** de l'opération. C'est le piège principal du sujet (cas 3 du tableau de l'art. 743-1).
- Calculer le nombre de titres sur la valeur comptable (1 800 000 / 60 = 30 000) : la parité se fixe sur les valeurs réelles.
- Calculer la prime sur la valeur réelle alors que l'apport est comptabilisé à la valeur comptable (`JUR-R01`).
- Inscrire les éléments apportés pour leur valeur nette, sans reprendre les valeurs brutes et les amortissements.
- Constater un résultat de cession chez ATLAS, ou utiliser les anciens comptes 675 et 775.
