---
title: Comment fonctionnent les conversions numériques dans les systèmes informatiques
  ? Explications avec des exemples
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2024-05-29T19:56:06.786Z'
originalURL: https://freecodecamp.org/news/how-do-numerical-conversions-work
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1715271341530/60608a00-2e63-434e-91e8-c766b171f6f7.png
tags:
- name: Computers
  slug: computers
- name: data
  slug: data
- name: MathJax
  slug: mathjax
seo_title: Comment fonctionnent les conversions numériques dans les systèmes informatiques
  ? Explications avec des exemples
seo_desc: 'Computers perform complex calculations when carrying out their assigned
  tasks. At the very core, the calculations boil down to operations like comparisons,
  assignments, and addition.

  Have you ever wondered how they are performed under the hood and wh...'
---

Les ordinateurs effectuent des calculs complexes lorsqu'ils exécutent leurs tâches assignées. Au cœur même, les calculs se réduisent à des opérations comme les comparaisons, les assignations et les additions.

Vous êtes-vous déjà demandé comment elles sont effectuées sous le capot et pourquoi elles sont importantes ? À un niveau fondamental, un ordinateur fonctionne en effectuant diverses conversions numériques.

Dans cet article, vous apprendrez les concepts suivants :

* L'importance des systèmes numériques dans les ordinateurs.

* Les types de systèmes numériques.

* Les techniques de conversion numérique.

* L'application de différents systèmes numériques.

* Des mini-exercices pour vous maintenir engagé tout au long.

## Types de systèmes numériques

La conversion numérique est le processus de conversion des nombres d'un système de numération à un autre. Dans les systèmes informatiques, les systèmes de numération courants incluent le décimal (base-10), le binaire (base-2), l'hexadécimal (base-16) et l'octal (base-8).

### Mais qu'est-ce qu'une base ?

En mathématiques et en informatique, le terme "base" fait référence au nombre de chiffres ou de symboles uniques utilisés dans un système de numération positionnel. La valeur de chaque chiffre est multipliée par la base élevée à la puissance de sa position dans le nombre, en commençant par le chiffre le plus à droite, qui représente la place des unités.

Voici une explication des systèmes de numération couramment rencontrés :

1. **Base-2 (Binaire)** :

   * La base-2, ou binaire, utilise seulement deux symboles : 0 et 1.

   * La valeur de chaque chiffre est une puissance de 2, avec des positions augmentant de droite à gauche.

2. **Base-10 (Décimal)** :

   * La base-10, ou décimal, utilise dix symboles de 0 à 9.

   * La valeur de chaque chiffre est une puissance de 10, avec des positions augmentant de droite à gauche.

3. **Base-8 (Octal)** :

   * La base-8, ou octal, utilise huit symboles : 0 à 7.

   * La valeur de chaque chiffre est une puissance de 8, avec des positions augmentant de droite à gauche.

4. **Base-16 (Hexadécimal)** :

   * La base-16, ou hexadécimal, utilise seize symboles : 0 à 9 et A à F (représentant 10 à 15).

   * La valeur de chaque chiffre est une puissance de 16, avec des positions augmentant de droite à gauche.

   * Ci-dessous se trouve un tableau montrant la correspondance des nombres hexadécimaux de 10 avec l'alphabet.

| Caractère | Hexadécimal |
| --- | --- |
| A | 10 |
| B | 11 |
| C | 12 |
| D | 13 |
| E | 14 |
| F | 15 |

Cette notation est couramment utilisée pour simplifier la représentation des valeurs codées en binaire.

## Importance de la compréhension des systèmes numériques dans les ordinateurs

Apprendre les conversions de numération en informatique est essentiel pour plusieurs raisons :

1. **Compréhension de la représentation des données** : Les ordinateurs stockent et manipulent les données en utilisant une représentation binaire (base-2). Savoir convertir entre les systèmes de numération aide à comprendre comment les données sont stockées et traitées au niveau fondamental.

2. **Adressage de la mémoire** : Les adresses mémoire dans les ordinateurs sont fréquemment représentées au format hexadécimal. Savoir convertir entre le décimal et l'hexadécimal est crucial pour comprendre la gestion de la mémoire et pour le débogage.

3. **Réseautage et communication** : En réseautage, les adresses IP et les adresses MAC sont souvent représentées au format hexadécimal. Comprendre la conversion hexadécimale est donc utile pour les professionnels du réseautage.

4. **Cryptographie** : En cryptographie, les nombres hexadécimaux sont fréquemment utilisés pour représenter les clés, les textes chiffrés et autres données cryptographiques. Comprendre les conversions de numération aide à comprendre les opérations cryptographiques.

## Techniques de conversion

Dans cette section, vous apprendrez des techniques pour convertir un système de numération en un autre.

### Décimal en binaire

**Processus de conversion étape par étape :**

1. **Divisez le nombre par 2** : La première étape consiste à diviser le nombre par 2 et à enregistrer le reste.

2. **Divisez le quotient par 2 de manière répétitive** : Divisez le quotient de l'étape 1 et enregistrez le reste. Continuez à diviser et à enregistrer le reste jusqu'à ce qu'il ne reste que 1 comme quotient.

3. **Trouvez la solution dans l'ordre inverse** : En commençant par le dernier quotient qui serait `1`, remontez pour obtenir la réponse finale.

**Exemple de conversion :**

Disons que vous voulez l'équivalent binaire de `17`, alors le processus serait comme suit :

| Opération | Résultat | Reste |
| --- | --- | --- |
| 17/2 | 8 | 1 ↴ |
| 8/2 | 4 | 0 ↴ |
| 4/2 | 2 | 0 ↴ |
| 2/2 | 1 ⤡ | 0 ↴ |

Pour trouver la réponse finale, suivez les flèches. Commencez par le bas où le résultat est `1` et remontez. Vous obtiendrez `10001`.

Donc,

$$17_{10} = 10001_{2}$$

Essayons un nombre plus grand `55`

| Opération | Résultat | Reste |
| --- | --- | --- |
| 55/2 | 27 | 1 ↴ |
| 27/2 | 13 | 1 ↴ |
| 13/2 | 6 | 1 ↴ |
| 6/2 | 3 | 0 ↴ |
| 3/2 | 1 ⤡ | 1 ↴ |

Donc,

$$55_{10} = 110111_{2}$$

#### Maintenant, à votre tour :

Quel est `67` en binaire ?

<details data-node-type="hn-details-summary"><summary>Afficher la réponse</summary><div data-type="detailsContent"><code>67</code> en binaire est <code>1000011</code>.</div></details>

### Binaire en décimal

**Processus de conversion étape par étape :**

1. **Écrivez le nombre binaire** : Séparez chaque bit pour plus de clarté.

2. **Associez chaque bit avec sa puissance correspondante de 2** : Commencez par `2^0` à droite et augmentez l'exposant de `1` à mesure que vous vous déplacez vers la gauche.

3. **Multipliez chaque bit par sa puissance correspondante de 2** : Si le bit est 1, multipliez-le par la puissance de 2 pour cette position. Si le bit est 0, le résultat est 0 pour cette position.

4. **Sommez tous les produits** : Additionnez tous les résultats de l'étape 3 pour obtenir l'équivalent décimal.

**Exemple de conversion :**

Pour `101`, la conversion serait comme suit :

$$\begin{align} &1\times2^2 + 0\times2^1 + 1\times2^0 \newline &= 4 + 0 + 1 \newline &= 5 \end{align}$$

Donc,

$$101_{2} = 5_{10}$$

Convertissons `1011001` en décimal :

$$\begin{align} &1\times2^6+0\times2^5+1\times2^4+1\times2^3+0\times2^2+0\times2^1+1\times2^0\newline &= 64+0+16+8+0+0+1 \newline &= 89 \end{align}$$

Donc,

$$1011001_{2} = 89_{10}$$

### Binaire en hexadécimal

**Processus de conversion étape par étape :**

1. **Faites des paires de 4** : Séparez le nombre binaire donné en 4 bits chacun, en commençant par le bit le plus à droite.

2. **Ajoutez des 0 à la paire la plus à gauche si les bits ne comptent pas jusqu'à 4** : Si la partie la plus à gauche ne fait pas 4 bits, ajoutez des zéros à gauche pour compléter le compte.

3. **Trouvez le nombre décimal équivalent comme expliqué précédemment** : Utilisez la conversion binaire en décimal.

**Exemple de conversion :**

Convertissons `10010010` en hexadécimal.

1. Divisez les bits en sections de 4 bits chacune, en commençant par le bit le plus à droite :

   * `10010010` = \[`1001][0010]`

   * Le remplissage n'était pas nécessaire ici car chaque section fait 4 bits de long.

2. Convertissez le binaire en décimal :

$$\begin{align} &[1001][0010]\newline &=[1\times2^3 + 0\times2^2 + 0\times2^1 + 1\times2^0] [0\times2^3 + 0\times2^2 + 1\times2^1 + 1\times2^0] \newline &=[8+0+0+1][0+0+1+1] = [9][2] \end{align}$$

Donc,

$$10010010_{2} = 92_{16}$$

Faisons un autre exemple. Mais d'abord,

Rappelons que les nombres 10 - 15 sont représentés comme suit en hexadécimal :

| Caractère | Hexadécimal |
| --- | --- |
| A | 10 |
| B | 11 |
| C | 12 |
| D | 13 |
| E | 14 |
| F | 15 |

Convertissons `11010011011` en hexadécimal.

1. Divisez les bits en groupes de 4, en commençant par la droite.

   * \[110\]\[1001\]\[1011\]

2. Ajoutez un remplissage de `0` à la section la plus à gauche.

   * \[0110\]\[1001\]\[1011\]

3. Convertissez les bits en décimal en utilisant la méthode binaire-décimal.

$$\begin{align} &[0110][1001][1011]\newline &=[0\times2^3+1\times2^2+1\times2^1+0\times2^0]\ [1\times2^3+0\times2^2+0\times2^1+1\times2^0]\ [1\times2^3+0\times2^2+1\times2^1+1\times2^0]\newline &=[6][9][11]\newline &=[6][9][B] \end{align}$$

4. Comme `11` correspond à `B` en hexadécimal, remplacez `11` par `B`.

   $$[6][9][11] =[6][9][B]$$

Donc,

$$11010011011_{2} = 69B_{16}$$

### Hexadécimal en binaire

**Processus de conversion étape par étape :**

**Exemple de conversion :**

1. **Identifiez chaque chiffre hexadécimal** : Décomposez le nombre hexadécimal en chiffres individuels.

2. **Convertissez chaque chiffre hexadécimal en binaire** : Chaque chiffre hexadécimal correspond à une séquence binaire unique de quatre bits.

### **Exemple de conversion :**

Convertissons le nombre hexadécimal `2F3` en binaire.

1. **Identifiez chaque chiffre hexadécimal** :

   * `2`

   * `F`

   * `3`

2. **Convertissez chaque chiffre hexadécimal en binaire** :

   * `2` en binaire : `0010`

   * `F` est `15` en décimal et en binaire : `1111`

   * `3` en binaire : `0011`

3. **Combinez les séquences binaires** :

   * `2F3` en binaire : `0010 1111 0011`

Donc, le nombre hexadécimal `2F3` se convertit en `001011110011` en binaire.

### Octal en binaire

**Processus de conversion étape par étape :**

**Exemple de conversion :**

Pour convertir un nombre octal en binaire, chaque chiffre octal (0-7) est converti en un nombre binaire de trois bits car le plus grand chiffre octal (7) peut être représenté en utilisant trois bits (111).

### **Processus de conversion étape par étape :**

1. **Identifiez chaque chiffre octal** : Décomposez le nombre octal en chiffres individuels.

2. **Convertissez chaque chiffre octal en binaire** : Utilisez la même méthode de conversion décimal-binaire.

3. **Combinez les séquences binaires** : Chaque séquence doit être de 3 bits, ajoutez des zéros à gauche si nécessaire. Concaténez les séquences binaires de trois bits pour former le nombre binaire final.

### **Exemple de conversion :**

Convertissons le nombre octal `157` en binaire.

1. **Identifiez chaque chiffre octal** :

   * `1`

   * `5`

   * `7`

2. **Convertissez chaque chiffre octal en binaire** :

   * `1` en binaire : `001`

   * `5` en binaire : `101`

   * `7` en binaire : `111`

3. **Combinez les séquences binaires** :

   * `157` en binaire : `001 101 111`

Donc, le nombre octal `157` se convertit en `001101111` en binaire.

### Binaire en octal

Pour convertir un nombre binaire en octal, regroupez les chiffres binaires en ensembles de trois, en commençant de droite à gauche. Vous pouvez compléter ce groupe avec des zéros de tête si le groupe le plus à gauche n'est pas de 3 chiffres.

### **Processus de conversion étape par étape :**

1. **Complétez le nombre binaire avec des zéros de tête** (si nécessaire) pour que le nombre de chiffres soit en groupes de trois :

   * Binaire : `11010011`

   * Binaire complété : `011 010 011`

2. **Regroupez les chiffres binaires en ensembles de trois** :

   * Groupes : `011 010 011`

3. **Convertissez chaque groupe de trois chiffres binaires en son équivalent octal** :

   * Utilisez la même méthode que binaire en décimal.

4. **Combinez les chiffres octaux** : Formez le nombre octal final en combinant les chiffres octaux.

### **Exemple de conversion :**

Convertissons le nombre binaire `11010011` en octal.

1. **Complétez le nombre binaire avec des zéros de tête** (si nécessaire) :

   * Binaire : `11010011`

   * Binaire complété : `011 010 011`

2. **Regroupez les chiffres binaires en ensembles de trois** :

   * Groupes : `011 010 011`

3. **Convertissez chaque groupe de trois chiffres binaires en son équivalent octal** :

   * `011` (binaire) = `3` (octal)

   * `010` (binaire) = `2` (octal)

   * `011` (binaire) = `3` (octal)

4. **Combinez les chiffres octaux** :

   * `11010011` en octal : `323`

Donc, le nombre binaire `11010011` se convertit en `323` en octal.

## Applications des conversions numériques

Dans cette section, vous apprendrez deux applications courantes des conversions numériques.

### Permissions de fichiers

La notation octale est couramment utilisée dans la gestion des permissions de fichiers dans les systèmes d'exploitation de type Unix. Dans les systèmes Unix, chaque fichier a des permissions associées qui déterminent qui peut lire, écrire ou exécuter le fichier. Ces permissions sont représentées par un nombre octal à 3 chiffres, où chaque chiffre correspond à un ensemble spécifique de permissions : `propriétaire`, `groupe` et `autres`.

Chaque chiffre dans la représentation octale est composé de trois bits, chaque bit représentant une permission spécifique :

* Le premier chiffre représente les permissions pour le propriétaire du fichier.

* Le deuxième chiffre représente les permissions pour le groupe associé au fichier.

* Le troisième chiffre représente les permissions pour les autres (utilisateurs ne faisant pas partie du groupe propriétaire).

La correspondance des permissions aux bits est la suivante :

* La permission de lecture correspond à la valeur `4`.

* La permission d'écriture correspond à la valeur `2`.

* La permission d'exécution correspond à la valeur `1`.

Pour calculer la représentation octale des permissions, vous additionnez les valeurs des permissions accordées. Par exemple :

* Si un fichier a des permissions de lecture et d'écriture pour le propriétaire, des permissions de lecture seule pour le groupe, et aucune permission pour les autres, la représentation octale serait `640`.

Voici la ventilation :

| Permission | Propriétaire | Groupe | Autres |
| --- | --- | --- | --- |
| Lecture = 4 | Oui | Oui | Non |
| Écriture = 2 | Oui | Non | Non |
| Exécution = 1 | Non | Non | Non |
|  | 4 +2 + 0 = 6 | 4 +0 + 0 = 4 | 0 |

* Le propriétaire a les permissions de lecture (4) + écriture (2), ce qui donne 6.

* Le groupe a uniquement les permissions de lecture (4).

* Les autres n'ont aucune permission, ce qui correspond à 0.

Donc, les permissions pour le fichier en représentation octale sont `640`.

**Quiz :**

<details data-node-type="hn-details-summary"><summary>Que montre la permission 777 ?</summary><div data-type="detailsContent">Lecture, écriture et exécution pour tous - utilisateurs, groupes et autres.</div></details>

Cette représentation octale des permissions fournit un moyen concis et efficace de gérer les permissions de fichiers dans les systèmes Unix, permettant une compréhension et une manipulation faciles des droits d'accès.

Pour en savoir plus sur les permissions de fichiers, vous pouvez lire mon autre article [ici](https://www.freecodecamp.org/news/linux-chmod-chown-change-file-permissions/).

### Codes de couleur

Vous avez peut-être remarqué que la notation `#ffffff`, `#c3c400` est répandue dans divers contextes numériques, tels que la conception web, les logiciels de retouche graphique et la programmation. Comme vous l'avez peut-être deviné, il s'agit d'une représentation hexadécimale. Par exemple, voyez cette palette de [Colorhunt](https://colorhunt.co/palette/ffff80ffaa80ff5580ff0080) :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1715250432475/ccab919f-3796-441a-89e7-60fc3a85e01c.png align="center")

Ici, nous avons une valeur hexadécimale de la couleur suivie de la valeur RVB équivalente.

Les codes de couleur hexadécimaux représentent les couleurs dans le modèle RVB en utilisant des paires de chiffres hexadécimaux pour chaque composante de couleur (rouge, vert et bleu). Chaque paire correspond à une valeur de 8 bits, allant de `00` à `FF`, où `00` représente l'intensité la plus faible (noir) et `FF` représente l'intensité la plus élevée (blanc).

Par exemple, `#FF0000` représente le rouge, `#00FF00` représente le vert et `#0000FF` représente le bleu.

**QUIZ :**

<details data-node-type="hn-details-summary"><summary>Si le rouge et le vert font du jaune dans le modèle RVB, quel serait l'équivalent hexadécimal ?</summary><div data-type="detailsContent">#ffff00</div></details>

## Conclusion

À la fin de cet article, vous devriez être à l'aise pour effectuer la plupart des conversions courantes. Dans cet article, vous avez :

* Exploré l'importance des conversions numériques dans les ordinateurs.

* Exploré les systèmes de numération comme le binaire, le décimal, l'hexadécimal et l'octal.

* Appris les techniques de conversion entre ces systèmes.

* Compris quelques applications pratiques des systèmes de numération en informatique.

## Prochaines étapes

Vous pouvez coder un convertisseur décimal-binaire en JavaScript en suivant [ce](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/learn-recursion-by-building-a-decimal-to-binary-converter/step-1) guide étape par étape.

J'espère que vous avez trouvé cet article utile. J'adorerais me connecter avec vous sur l'une de ces [plateformes](https://zaira_.bio.link/).

À bientôt dans le prochain tutoriel, bon codage 😁