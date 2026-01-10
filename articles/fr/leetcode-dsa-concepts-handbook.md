---
title: 'Méditations LeetCode : Un Guide Visuel des Concepts de Structures de Données
  et d''Algorithmes'
subtitle: ''
author: Eda Eren
co_authors: []
series: null
date: '2025-05-29T19:52:13.635Z'
originalURL: https://freecodecamp.org/news/leetcode-dsa-concepts-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748548297673/2ea8ee5a-e873-4401-b024-86412bf00f8a.png
tags:
- name: Computer Science
  slug: computer-science
- name: MathJax
  slug: mathjax
- name: leetcode
  slug: leetcode
- name: DSA
  slug: dsa
seo_title: 'Méditations LeetCode : Un Guide Visuel des Concepts de Structures de Données
  et d''Algorithmes'
seo_desc: 'It may seem like an oxymoron when the words "LeetCode" and "meditation"
  are used together – after all, one thing that almost everyone can agree is that
  LeetCode is challenging. It''s called grinding LeetCode for a reason.

  It doesn''t have anything to d...'
---

Il peut sembler un oxymore lorsque les mots "LeetCode" et "méditation" sont utilisés ensemble – après tout, une chose sur laquelle presque tout le monde peut s'accorder est que [LeetCode](https://leetcode.com/) est difficile. C'est appelé *grinding* LeetCode pour une raison.

Cela n'a rien à voir avec la plateforme, bien sûr, mais plutôt avec ce qu'elle représente : résoudre des problèmes pendant des heures, généralement pour trouver une solution qui est encore plus difficile à comprendre.

Mais ce qui est plus difficile, c'est de trouver une feuille de route pour résoudre ces problèmes avec très peu de connaissances sur les structures de données et les algorithmes. Ce guide est plus ou moins basé sur la [liste Blind 75](https://neetcode.io/practice?tab=blind75) qui est incluse dans les problèmes de pratique de [neetcode.io](http://neetcode.io). C'est une ressource incroyable qui offre une feuille de route d'étude organisée pour résoudre les problèmes de LeetCode.

En fait, pourquoi ne pas adopter une approche plus structurée et *plus calme* ? Nous pouvons traiter l'apprentissage des sujets de la liste comme une brève promenade dans la nature – une sorte de méditation, si vous voulez.

Cela dit, ce guide ne traite pas de problèmes spécifiques. Plutôt, il s'agit de comprendre les concepts derrière eux de manière informelle. Il est également indépendant du langage – parfois vous verrez du TypeScript, parfois du Python, et parfois du JavaScript.

Ce guide nécessite également que vous soyez patient, que vous vous détendiez, que vous fassiez un pas en arrière et que vous fassiez attention. Les GIFs de qualité moyenne utilisés dans le guide (peut-être ironiquement !) visent à encourager cela. Ils ne sont pas des vidéos, donc vous pouvez attendre qu'ils arrivent à un moment que vous n'avez pas compris ou manqué au lieu de les rembobiner hâtivement ou de vous précipiter à un certain point dans le futur.

Résoudre des centaines de problèmes LeetCode peut être la porte à franchir pour obtenir un entretien dans les grandes entreprises technologiques… mais apprendre les sujets dont traitent les problèmes n'est pas sous le monopole de quiconque.

Cela dit, commençons le premier chapitre.

## Table des Matières

1. [Prérequis](#heading-prerequisites)
    
2. [Chapitre Un : Tableaux & Hachage](#heading-chapter-one-arrays-amp-hashing)
    
    * [Tableaux Dynamiques](#heading-dynamic-arrays)
        
    * [Tables de Hachage](#heading-hash-tables)
        
    * [Sommes Préfées](#heading-prefix-sums)
        
3. [Chapitre Deux : Deux Pointeurs](#heading-chapter-two-two-pointers)
    
    * [Exemple de Palindrome](#heading-palindrome-example)
        
    * [Exemple des Carrés d'un Tableau Trié](#heading-squares-of-a-sorted-array-example)
        
4. [Chapitre Trois : Fenêtre Glissante](#heading-chapter-three-sliding-window)
    
    * [Taille de Fenêtre Fixe](#heading-fixed-window-size)
        
    * [Taille de Fenêtre Dynamique](#heading-dynamic-window-size)
        
5. [Chapitre Quatre : Pile](#heading-chapter-four-stack)
    
6. [Chapitre Cinq : Recherche Binaire](#heading-chapter-five-binary-search)
    
7. [Chapitre Six : Listes Chaînées](#heading-chapter-six-linked-lists)
    
    * [Listes Chaînées Simples](#heading-singly-linked-lists)
        
    * [Listes Chaînées Doubles](#heading-doubly-linked-lists)
        
    * [Listes Chaînées Circulaires](#heading-circular-linked-lists)
        
8. [Interlude : Pointeurs Rapides & Lents](#heading-interlude-fast-amp-slow-pointers)
    
    * [Trouver le Nœud du Milieu d'une Liste Chaînée](#heading-finding-the-middle-node-of-a-linked-list)
        
9. [Chapitre Sept : Arbres](#heading-chapter-seven-trees)
    
    * [Arbres Binaires, Arbres de Recherche Binaire (BSTs)](#heading-binary-trees-binary-search-trees-bsts)
        
        * [Insertion dans un Arbre de Recherche Binaire](#heading-inserting-into-a-binary-search-tree)
            
            * [Solution Récursive](#heading-recursive-solution)
                
            * [Solution Itérative](#heading-iterative-solution)
                
        * [Suppression d'un Arbre de Recherche Binaire](#heading-deleting-from-a-binary-search-tree)
            
        * [Parcours](#heading-traversals)
            
            * [Recherche en Profondeur (DFS)](#heading-depth-first-search-dfs)
                
                * [Parcours Préfixe](#heading-preorder-traversal)
                    
                * [Parcours Infixe](#heading-inorder-traversal)
                    
                * [Parcours Postfixe](#heading-postorder-traversal)
                    
            * [Recherche en Largeur (BFS)](#heading-breadth-first-search-bfs)
                
10. [Chapitre Huit : Tas / File de Priorité](#heading-chapter-eight-heap-priority-queue)
    
    * [Propriétés des Tas](#heading-heap-properties)
        
    * [Tas avec Tableaux](#heading-heaps-with-arrays)
        
    * [Insertion/Suppression d'Éléments](#heading-insertingremoving-elements)
        
    * [Tri par Tas](#heading-heapsort)
        
11. [Chapitre Neuf : Retour sur Trace](#heading-chapter-nine-backtracking)
    
    * [Sous-ensembles](#heading-subsets)
        
12. [Chapitre Dix : Tries](#heading-chapter-ten-tries)
    
13. [Chapitre Onze : Graphes](#heading-chapter-eleven-graphs)
    
    * [Représentation des Graphes](#heading-representing-graphs)
        
        * [Liste d'Arêtes](#heading-edge-list)
            
        * [Matrice d'Adjacence](#heading-adjacency-matrix)
            
        * [Liste d'Adjacence](#heading-adjacency-list)
            
    * [Parcours](#heading-traversals-1)
        
        * [Recherche en Largeur](#heading-breadth-first-search)
            
        * [Recherche en Profondeur](#heading-depth-first-search)
            
14. [Chapitre Douze : Programmation Dynamique](#heading-chapter-twelve-dynamic-programming)
    
15. [Chapitre Treize : Intervalles](#heading-chapter-thirteen-intervals)
    
16. [Chapitre Quatorze : Manipulation de Bits](#heading-chapter-fourteen-bit-manipulation)
    
    * [Opérateurs Bit à Bit](#heading-bitwise-operators)
        
        * [ET (`&`)](#heading-and-amp)
            
        * [OU (`|`)](#heading-or)
            
        * [XOR (`^`)](#heading-xor)
            
        * [NON (`~`)](#heading-not)
            
        * [Déplacement à Gauche (remplissage zéro) (`<<`)](#heading-left-shift-zero-fill-ltlt)
            
        * [Déplacement à Droite (conservation du signe) (`>>`)](#heading-right-shift-sign-preserving-gtgt)
            
        * [Déplacement à Droite (non signé) (`>>>`)](#heading-right-shift-unsigned-gtgtgt)
            
    * [Obtenir un Bit](#heading-getting-a-bit)
        
    * [Définir un Bit](#heading-setting-a-bit)
        
17. [Conclusion](#heading-conclusion)
    
18. [Ressources & Crédits](#heading-resources-amp-credits)
    

## Prérequis

Avant de plonger, une certaine familiarité avec TypeScript/JavaScript et Python peut être utile, car ce sont les langages que j'utilise pour les exemples. De plus, une compréhension de base de la notation Big O est utile lorsque nous abordons les complexités temporelles et spatiales.

Même si nous ne passons pas par les mathématiques derrière les concepts, certaines connaissances mathématiques de base peuvent également aider. Cela dit, ce n'est définitivement pas nécessaire pour profiter ou apprendre quelque chose d'utile de ce guide.

## Chapitre Un : Tableaux & Hachage

Faisons très brièvement connaissance avec nos sujets pour ce chapitre : tableaux dynamiques, tables de hachage et sommes préfées.

### Tableaux Dynamiques

Les tableaux dynamiques sont, eh bien, dynamiques. Ils sont flexibles et peuvent changer leur taille pendant l'exécution.

Le type `list` de Python est un tableau dynamique. Nous pouvons créer une liste `items`, par exemple :

```python
items = [3, 5]
```

La **longueur** de `items` est 2, comme vous pouvez le voir, mais sa **capacité** est supérieure ou égale à sa longueur. En fait, la capacité fait référence à la taille totale, tandis que la longueur est la taille réelle.

Puisque les tableaux dynamiques sont toujours des tableaux, ils ont besoin d'un bloc de mémoire contigu.

Nous pouvons facilement ajouter un élément à `items` :

```python
items.append(7)
```

Et en ajouter quelques autres :

```python
items.append(9)
items.append(11)
items.append(13)
```

Tout au long, la longueur et la capacité de `items` continuent de croître dynamiquement.

![Visualisation animée de quatre cases pour un tableau "items" qui contient les valeurs 3 et 5 à l'initialisation, l'ajout de 7 au tableau ajoute quatre cases supplémentaires.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747912308935/960ff442-e095-4781-8ab5-9b84e0ecb804.gif align="center")

#### Complexité temporelle et spatiale

L'accès à un élément est \\(O(1)\\) car nous avons un [accès aléatoire](https://en.wikipedia.org/wiki/Random_access).

L'insertion d'un nouvel élément ou la suppression d'un élément est \\(O(n)\\) (pensez à devoir décaler tous les éléments avant l'insertion ou après la suppression d'un élément). Mais, afin de ne pas être trop pessimiste, nous pouvons regarder [l'analyse amortie](https://en.wikipedia.org/wiki/Amortized_analysis) – dans ce cas, l'insertion/suppression à la fin du tableau devient \\(O(1)\\).

La complexité spatiale est \\(O(n)\\), car le besoin d'espace augmentera proportionnellement à l'augmentation de l'entrée.

Si vous avez besoin de plus d'informations sur la complexité temporelle et spatiale, vous pouvez [vous référer à ce guide](https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/).

### Tables de Hachage

Une table de hachage mappe les clés aux valeurs, implémentant un *tableau associatif*.

Le `dict` de Python en est un exemple :

```python
number_of_petals = {
    'Euphorbia': 2, 
    'Trillium': 3, 
    'Columbine': 5,
}
```

Ainsi que les "objets" de JavaScript :

```javascript
let numberOfMoons = {
  'Earth': 1,
  'Mars': 2,
  'Jupiter': 95,
  'Saturn': 146,
  'Uranus': 27,
  'Neptune': 14,
};
```

Il y a deux ingrédients importants pour une table de hachage :

* un tableau de "buckets" pour stocker les données
    
* une fonction de hachage pour mapper les données à un index spécifique dans le tableau
    

Les hachages sont généralement de grands entiers, donc pour trouver un index, nous pouvons prendre le résultat du hachage modulo la longueur du tableau.

![Visualisation animée d'un tableau avec 5 buckets, la fonction de hachage trouvant un bucket pour chaque valeur dans le dictionnaire number_of_petals.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747913143164/2a8371ba-133c-4d5a-a270-b44f935fc91b.gif align="center")

**Note :** La **fonction de hachage** qui mappe les éléments aux buckets **n'est pas** le `hash()` utilisé dans la visualisation (c'est juste une [fonction Python](https://docs.python.org/3/library/functions.html#hash) pour calculer la valeur de hachage d'un objet). La fonction de hachage dans ce cas est l'opération modulo ( `%` ).

Ici, avec la valeur de hachage de la clé de chaque élément, nous calculons le reste lorsqu'elle est divisée par la longueur du tableau pour trouver dans quel "bucket" elle doit aller.

Le rapport du nombre d'éléments au nombre de buckets est appelé le **facteur de charge**, et plus il est élevé, plus il y a de **collisions** (lorsque des éléments doivent être insérés au même endroit dans le tableau).

Il existe certaines tactiques de résolution de collision comme le **sondage linéaire** (sondage à travers le tableau jusqu'à trouver un bucket vide) et le **chaînage** (chaînage de plusieurs éléments comme des listes chaînées), mais nous n'aborderons pas celles-ci pour l'instant.

#### Complexité temporelle et spatiale

Le cas moyen pour les opérations de recherche, d'insertion et de suppression est \\(O(1)\\) car nous utilisons des clés pour rechercher les valeurs.

La complexité spatiale est \\(O(n)\\) car elle croît linéairement avec le nombre d'éléments.

### Sommes Préfées

Une somme préfixée est la séquence de nombres que nous obtenons après avoir ajouté les sommes des totaux cumulés d'une autre séquence. Elle est également appelée **somme cumulative**.

Le premier élément du tableau résultant est le premier élément du tableau d'entrée. C'est bien. Nous commençons au deuxième élément, et ajoutons les nombres précédents à chaque fois que nous avançons. C'est-à-dire :

$$result[i] = \begin{cases} nums[0] & \text{si } i \text{ est zéro} \\ result[i - 1] + nums[i] & \text{si } i \geq 1 \end{cases}$$

En code, nous pouvons l'implémenter facilement :

```python
def runningSum(nums):
    result = [nums[0]]
    
    for i in range(1, len(nums)):
        result.append(result[i - 1] + nums[i])

    return result
```

![Visualisation animée de runningSum du tableau [1, 2, 3, 4, 5].](https://cdn.hashnode.com/res/hashnode/image/upload/v1747913501237/e9c95eef-6310-457c-b94e-da5a61fc890a.gif align="center")

#### Complexité temporelle et spatiale

La complexité temporelle pour une somme préfixée est \\(O(n)\\) car nous itérons sur chacun des éléments du tableau.

La complexité spatiale est également \\(O(n)\\) car le besoin d'espace externe croît à mesure que la longueur du tableau original augmente.

## Chapitre Deux : Deux Pointeurs

L'une des techniques d'itération à travers un tableau est la **technique des deux pointeurs**, et elle est aussi simple qu'elle en a l'air : nous gardons simplement deux pointeurs, l'un commençant par la gauche, et l'autre par la droite, se rapprochant progressivement l'un de l'autre.

![Visualisation animée de la technique des deux pointeurs](https://cdn.hashnode.com/res/hashnode/image/upload/v1747913831967/b8e251a9-2e9e-41be-84ed-46f2559b1515.gif align="center")

### Exemple de Palindrome

Un exemple très basique peut être celui où nous vérifions si une chaîne est un palindrome ou non. Un palindrome est une chaîne qui se lit de la même manière dans les deux sens.

Dans un monde imaginaire où toutes les entrées consistent toujours en des lettres anglaises minuscules, nous pouvons le faire comme ceci :

```typescript
// s consiste en des lettres anglaises minuscules
function isPalindrome(s: string) {
  let left = 0;
  let right = s.length - 1;

  while (left <= right) {
    if (s[left++] !== s[right--]) {
      return false;
    }
  }

  return true;
}
```

Nous initialisons deux pointeurs : `left` et `right`. `left` pointe vers le début du tableau, tandis que `right` pointe vers le dernier élément. Lorsque nous bouclons tant que `left` est inférieur à `right`, nous vérifions s'ils sont égaux. Si ce n'est pas le cas, nous retournons `false` immédiatement. Sinon, notre pointeur `left` est augmenté – c'est-à-dire qu'il est déplacé d'un pas vers la *droite*, et notre pointeur `right` est diminué, ce qui signifie qu'il est déplacé d'un pas vers la *gauche*. Lorsqu'ils se chevauchent finalement, la boucle se termine, et nous retournons `true`.

Disons que notre chaîne est `'racecar'`, qui est un palindrome. Cela se passera comme suit :

![Visualisation animée de isPalindrome, avec l'exemple 'racecar' résultant en true.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747913932303/e60727a0-4e45-4452-8648-d35d1ae680c9.gif align="center")

### Exemple des Carrés d'un Tableau Trié

Un autre exemple où nous pouvons utiliser la technique des deux pointeurs est le problème [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array).

La description dit :

> Étant donné un tableau d'entiers `nums` trié dans l'ordre **non décroissant**, retourner *un tableau de* ***les carrés de chaque nombre*** *trié dans l'ordre non décroissant*.

Par exemple, si l'entrée est `[-4, -1, 0, 3, 10]`, la sortie doit être `[0, 1, 9, 16, 100]`.

Maintenant, évidemment, nous pouvons simplement élever chaque nombre au carré, puis trier le tableau avec une méthode de tri intégrée, et en avoir fini avec cela. Mais une opération de tri n'est jamais meilleure que \\(O(n \ log \ n)\\) en temps d'exécution, donc nous pouvons le faire en utilisant deux pointeurs en seulement \\(O(n)\\) temps :

```typescript
function sortedSquares(nums: number[]): number[] {
  let left = 0;
  let right = nums.length - 1;
  let result = [];

  while (left <= right) {
    if (Math.abs(nums[left]) > Math.abs(nums[right])) {
      result.push(nums[left++] ** 2);
    } else {
      result.push(nums[right--] ** 2);
    }
  }

  return result.reverse();
}
```

Nous comparons la valeur absolue des éléments auxquels `left` et `right` pointent, et poussons le carré du plus grand dans notre tableau `result`. Et nous retournons la version inversée de celui-ci.

**Note :** La raison pour laquelle nous retournons le résultat inversé est que le tableau est initialement déjà trié, et nous obtenons la plus grande valeur absolue en premier. La raison pour laquelle cela fonctionne est liée à la manière dont les *deux pointeurs* fonctionnent : lorsque nous commençons par les deux extrémités, nous commençons initialement par les plus petites et plus grandes valeurs du tableau.

Parce que nous ne faisons qu'un seul passage à travers le tableau tout en comparant, puis en inversant plus tard, cela se termine par être \\(O(n)\\), un meilleur temps d'exécution que \\(O(n \ log \ n)\\).

## Chapitre Trois : Fenêtre Glissante

Maintenant que nous sommes familiers avec la technique des Deux Pointeurs, nous pouvons ajouter une autre à notre boîte à outils : la Fenêtre Glissante. Elle est généralement utilisée pour les opérations effectuées sur les sous-ensembles d'une donnée donnée. Elle se présente également en deux versions : **taille de fenêtre fixe** et **taille de fenêtre dynamique**.

### Taille de Fenêtre Fixe

Si nous avons une contrainte de taille dans un problème donné – disons, nous devons vérifier un sous-tableau de taille \\(k\\) – la fenêtre glissante est une technique appropriée à utiliser.

Par exemple, obtenir la somme maximale de sous-tableau (de taille \\(k\\)) d'un tableau donné peut être fait comme ceci :

![Visualisation animée de la technique de fenêtre glissante à taille fixe, tableau [1, 5, 4, 2, 9] avec k = 3, ayant la somme maximale de 15.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747914357907/ecd51e70-e649-4856-a563-47621b950526.gif align="center")

Notez que la taille de la fenêtre est \\(k\\), et elle ne change pas tout au long de l'opération – d'où, **taille fixe**.

Une chose très cool à remarquer ici est que avec chaque **glissement**, ce qui arrive à notre somme est que nous *ajoutons* l'élément de droite, et *diminuons* l'élément de gauche.

Regardons un exemple pour obtenir la somme maximale de sous-tableau avec une taille donnée `k` :

```typescript
function maxSubarray(numbers: number[], k: number) {
  if (numbers.length < k) {
    return 0;
  }

  let currentSum = 0;

  // Somme initiale de la première fenêtre 
  for (let i = 0; i < k; i++) {
    currentSum += numbers[i];
  }

  let maxSum = currentSum;

  let left = 0;
  let right = k;

  while (right < numbers.length) {
    currentSum = currentSum - numbers[left++] + numbers[right++];
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
}
```

**Note :** La mise à jour des pointeurs peut également être faite en dehors des crochets, comme ceci :

```typescript
while (right < numbers.length) {
  currentSum = currentSum - numbers[left] + numbers[right];
  maxSum = Math.max(maxSum, currentSum);
  left++;
  right++;
}
```

Puisque l'opérateur postfixé retourne la valeur en premier, ils peuvent être utilisés à l'intérieur des crochets pour être légèrement plus concis.

Ici, nous obtenons d'abord la somme initiale de notre fenêtre en utilisant la boucle `for`, et nous la définissons comme la somme maximale.

Ensuite, nous initialisons deux pointeurs : `left` qui pointe vers l'extrémité gauche de la fenêtre, et `right` qui pointe vers l'extrémité droite de la fenêtre. Lorsque nous bouclons, nous mettons à jour notre `currentSum`, en diminuant la valeur `left`, et en ajoutant la valeur `right`. Lorsque notre somme actuelle est supérieure à la somme maximale, la variable `maxSum` est également mise à jour.

### Taille de Fenêtre Dynamique

Contrairement à la version à taille de fenêtre fixe, la taille de la fenêtre change dynamiquement cette fois.

Par exemple, prenons un bref aperçu du problème [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock). Nous devons choisir un jour pour acheter une action, et la vendre dans le *futur*. Les nombres dans le tableau sont des prix, et nous devons acheter l'action au prix le plus bas possible, et la vendre au prix le plus haut possible.

Nous pouvons initialiser les pointeurs `left` et `right` à nouveau, mais cette fois, nous les mettrons à jour en fonction d'une condition. Lorsque l'élément de gauche est inférieur à celui de droite, cela signifie que c'est bon – nous pouvons acheter et vendre à ces prix, donc nous obtenons leur différence et mettons à jour notre variable `maxDiff` qui contient la différence maximale entre les deux.

Si, cependant, celui de gauche est supérieur à celui de droite, nous mettons à jour notre pointeur `left` pour qu'il soit là où se trouve `right`. Dans les deux cas, nous continuerons à mettre à jour `right` jusqu'à ce que nous atteignions la fin du tableau.

Avec la flèche bleue indiquant le pointeur de gauche, et la rouge celui de droite, le processus ressemble à ceci :

![Visualisation animée de la technique de fenêtre glissante à taille dynamique, tableau [7, 1, 5, 3, 6] ayant la différence maximale de 5.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747914550588/222996a0-d2a6-414e-86cf-fe60deb908d8.gif align="center")

La solution ressemble à ceci :

```typescript
function maxProfit(prices: number[]): number {
  let left = 0;
  let right = left + 1;
  let maxDiff = 0;

  while (right < prices.length) {
    if (prices[left] < prices[right]) {
      let diff = prices[right] - prices[left];
      maxDiff = Math.max(maxDiff, diff);
    } else {
      left = right;
    }

    right++;
  }

  return maxDiff;
}
```

**Note :** Celui-ci est également appelé **version rapide/rattrapage** de la fenêtre glissante dynamique, car le pointeur `left` saute pour rattraper le pointeur `right` dans le bloc `else`.

#### Complexité temporelle et spatiale

Les deux exemples ont la même complexité temporelle et spatiale : La complexité temporelle est \\(O(n)\\) car dans le pire des cas, nous itérons à travers tous les éléments du tableau. La complexité spatiale est \\(O(1)\\) car nous n'avons pas besoin d'espace supplémentaire.

## Chapitre Quatre : Pile

Un type de données de pile est peut-être l'un des plus connus. Une pile de livres pourrait être un bon exemple à visualiser, mais l'insertion et la suppression ne peuvent se faire que par une seule extrémité. Une pile fonctionne selon le principe dernier entré, premier sorti (LIFO) : le dernier élément à entrer est le premier à sortir.

Généralement, nous aurons des méthodes pour *pousser* un élément sur la pile, et *extraire* un élément de la pile.

Par exemple, disons que nous cherchons des parenthèses valides dans une chaîne donnée, et l'opération que nous allons faire se déroule comme suit.

Lorsque nous itérons sur les caractères de la chaîne, nous *poussons* le caractère sur la pile. Si nous avons poussé une parenthèse fermante (l'une de `)`, `}`, ou `]`), alors, si l'élément poussé précédemment est sa paire ouvrante, nous *extraire* cette paire de la pile.

Si, à la fin, la pile est vide, la chaîne est composée de parenthèses valides.

![Visualisation animée de l'ajout et de la suppression d'une pile de parenthèses.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747914829489/e86baf72-22f6-41fe-9de9-f4da136a8777.gif align="center")

Une pile peut être implémentée comme un tableau ou une liste chaînée. Mais l'utilisation de listes chaînées est plus courante car avec les tableaux, nous avons un potentiel *débordement de pile* lorsque nous prédéfinissons une taille de pile maximale. D'un autre côté, les listes chaînées ne sont pas statiques en ce qui concerne la mémoire, donc elles sont un bon candidat pour implémenter des piles.

Les listes chaînées sont également efficaces car nous utilisons une extrémité de la pile pour l'insertion et la suppression, et ces opérations sont des opérations en temps constant.

Regardons une implémentation simple de pile en Python.

Maintenant, nous pouvons utiliser une `list`, mais [une liste en Python est implémentée comme un tableau dynamique en dessous](https://docs.python.org/3/faq/design.html#how-are-lists-implemented-in-cpython), donc à un moment donné, pousser un élément peut être une opération \\(O(n)\\) si la liste doit être copiée dans un autre emplacement mémoire. Pour cette raison, nous utiliserons un [`deque`](https://docs.python.org/3/library/collections.html#collections.deque), qui est implémenté comme une liste doublement chaînée, afin que nous sachions que les opérations de poussée et d'extraction seront \\(O(1)\\).

```python
from collections import deque

class Stack:
    def __init__(self):
        self._stack = deque()

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        return self._stack[-1]

    def is_empty(self):
        return not bool(len(self._stack))

    def size(self):
        return len(self._stack)
```

En plus de `push` et `pop`, nous aurons également généralement des fonctions comme `peek` pour obtenir l'élément le plus haut de la pile, `is_empty` pour vérifier si la pile est vide, et `size` pour obtenir la taille de la pile.

Nous pouvons également le faire en utilisant JavaScript. Maintenant, nous pouvons le faire en utilisant un tableau, mais nous voulons utiliser une liste chaînée à la place. Puisque nous n'avons pas une bibliothèque intégrée robuste comme Python cette fois, nous implémenterons une version très simple nous-mêmes. Même si nous n'avons pas encore vu les listes chaînées, l'idée de base est que nous avons des nœuds, chacun ayant une valeur `data`, et un pointeur `next` pointant vers le nœud suivant.

Créons d'abord un nœud simple :

```javascript
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}
```

Nous pouvons écrire notre pile maintenant :

```javascript
class Stack {
  constructor() {
    this.top = null;
    this.length = 0;
  }

  push(item) {
    const node = new Node(item);
    node.next = this.top;
    this.top = node;
    this.length++;
  }

  pop() {
    if (this.isEmpty()) { return null; }

    const data = this.top.data;
    this.top = this.top.next;
    this.length--;

    return data;
  }

  peek() {
    if (this.isEmpty()) { return null; }

    return this.top.data;
  }

  isEmpty() {
    return this.size() === 0;
  }

  size() {
    return this.length;
  }
}
```

Maintenant, utilisons-le :

```javascript
let myStack = new Stack();

myStack.push(5);
myStack.push(17);
myStack.push(55345);
myStack.push(0);
myStack.push(103)

console.log(myStack.size()) // 5
console.log(myStack.peek()) // 103

myStack.pop()

console.log(myStack.size()) // 4
console.log(myStack.peek()) // 0
```

#### Complexité temporelle et spatiale

Chaque méthode que nous avons définie pour notre pile a une complexité temporelle de \\(O(1)\\), et il en serait de même si nous devions utiliser un tableau. Cependant, comme mentionné ci-dessus, les tableaux ont des limitations en ce sens que l'allocation d'une taille de pile prédéfinie peut entraîner un débordement de pile. Et si nous devions utiliser un tableau dynamique, l'ensemble du tableau pourrait devoir être copié pour aller dans un autre emplacement mémoire après qu'une certaine taille soit atteinte, entraînant un temps \\(O(n)\\). Donc, les listes chaînées sont idéales pour implémenter un type de données de pile.

Si la complexité spatiale est linéaire – \\(O(n)\\) – la pile croîtra linéairement avec le nombre d'éléments qu'elle contient.

## Chapitre Cinq : Recherche Binaire

La recherche binaire est l'un des algorithmes les plus connus. C'est aussi un [algorithme de type diviser pour régner](https://brilliant.org/wiki/divide-and-conquer/), où nous divisons le problème en composants plus petits.

Le point crucial de la recherche binaire est de trouver un élément cible dans un tableau trié donné. Nous avons deux pointeurs : `high` pour pointer vers le plus grand élément, et `low` pour pointer vers le plus petit élément. Nous les initialisons d'abord pour le tableau lui-même, avec `high` étant le dernier index et `low` étant le premier index.

Ensuite, nous calculons le point médian. Si la cible est plus grande que le point médian, alors nous ajustons notre pointeur `low` pour pointer vers `mid + 1`, sinon si la cible est plus petite que le point médian, nous ajustons `high` pour être `mid - 1`. À chaque itération, nous éliminons la moitié du tableau jusqu'à ce que le point médian soit égal à la cible ou que le pointeur `low` dépasse `high`.

Si nous trouvons l'index de la cible, nous pouvons le retourner dès que nous le trouvons. Sinon, nous pouvons simplement retourner `-1` pour indiquer que la cible n'existe pas dans le tableau.

Par exemple, si nous avons un tableau `nums` `[-1, 0, 3, 5, 9, 12]` et notre `target` est `9`, l'opération ressemble à ceci :

![Visualisation animée de la recherche binaire, tableau [-1, 0, 3, 5, 9, 12] avec target = 9, le résultat étant l'index 4.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747915126875/c27134cb-ae7c-4f09-88d8-13fc64900319.gif align="center")

Nous pouvons l'écrire en TypeScript comme ceci :

```typescript
function search(nums: number[], target: number): number {
  let high = nums.length - 1;
  let low = 0;

  while (high >= low) {
    let mid = Math.floor((high + low) / 2);

    if (target > nums[mid]) {
      low = mid + 1;
    } else if (target < nums[mid]) {
      high = mid - 1;
    } else {
      return mid;
    }
  }

  return -1;
}
```

#### Complexité temporelle et spatiale

La complexité temporelle d'un algorithme de recherche binaire est \\(O(log \ n)\\) dans le pire des cas. (Par exemple, si la cible n'est pas dans le tableau, nous allons diviser le tableau par deux jusqu'à ce qu'il ne reste qu'un élément.) La complexité spatiale est \\(O(1)\\) car nous n'avons pas besoin d'espace supplémentaire.

## Chapitre Six : Listes Chaînées

Une liste chaînée est une structure de données linéaire que vous connaissez probablement. C'est aussi une structure de données qui peut croître et décroître dynamiquement – donc contrairement aux tableaux, il n'est pas nécessaire d'allouer de la mémoire au préalable.

Une partie importante d'une liste chaînée est le **pointeur de tête** qui pointe vers le début de la liste. Il peut y avoir ou non un **pointeur de queue** qui pointe également vers la fin de la liste.

L'ingrédient principal d'une liste chaînée est un nœud simple, qui se compose de deux parties : les données et le pointeur suivant. Donc, c'est une idée importante à retenir : *un nœud ne connaît que ses données et son voisin.*

Le tout dernier nœud de la liste chaînée pointe vers `null` pour indiquer qu'il s'agit de la fin de la liste.

Mais il existe différents types de listes chaînées qui diffèrent légèrement les unes des autres, alors prenons brièvement un aperçu de celles-ci.

### Listes Chaînées Simples

L'idée principale avec les listes chaînées simples est que chaque nœud, avec les données qu'il possède, a un pointeur qui pointe *uniquement* vers le nœud suivant :

```javascript
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}
```

Et voici un exemple où nous avons trois nœuds, contenant les valeurs `1`, `2`, et `3` consécutivement :

![Visualisation animée d'une liste chaînée simple, avec des nœuds ayant les valeurs 1, 2, et 3.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747915365474/8604a69f-f24f-4dc5-b4a0-2eba452a4305.gif align="center")

Voici une implémentation simple d'une liste chaînée simple en JavaScript :

```javascript
class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  // Ajouter une valeur à la fin de la liste
  append(value) {
    let node = new Node(value);
    // Si la liste est vide
    if (this.head === null) {
      this.head = node;
      this.tail = this.head;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    
    this.length++;
    return this;
  }

  // Ajouter une valeur au début de la liste
  prepend(value) {
    let node = new Node(value);
    // Si la liste est vide
    if (this.head === null) {
      this.head = node;
      this.tail = this.head;
    } else {
      node.next = this.head;
      this.head = node;
    }
    
    this.length++;
    return this;
  }

  remove(value) {
    // Si la liste est vide, retourner null
    if (this.head === null) { 
      return null; 
    }

    // Si c'est le premier élément
    if (this.head.data === value) {
      this.head = this.head.next;
      this.length--;
      // Si c'est le seul élément 
      // (nous n'avons rien après l'avoir supprimé)
      if (this.head === null) {
        this.tail = null;
      } 
      return;
    }

    let currentNode = this.head;
    
    while (currentNode.next) {
      if (currentNode.next.data === value) {
        currentNode.next = currentNode.next.next;
        // Si c'est le dernier élément, mettre à jour la queue
        if (currentNode.next === null) {
          this.tail = currentNode;
        } 
        this.length--;
        return;
      }
      currentNode = currentNode.next;
    }
  }

  search(value) {
    let currentNode = this.head;

    while (currentNode) {
      if (currentNode.data === value) {
        return currentNode;
      }
      currentNode = currentNode.next;
    }

    // Si la valeur n'existe pas, retourner null
    return null;
  }

  printList() {
    let values = [];
    let currentNode = this.head;
    while (currentNode) {
      values.push(currentNode.data);
      currentNode = currentNode.next;
    }
    
    console.log(values);
  }
}
```

**Note :** Nous garderons un pointeur de queue dans tous ces exemples pour plus de commodité. Cela [ne fait pas de mal](https://softwareengineering.stackexchange.com/a/301863) d'avoir un pointeur de queue.

Nous pouvons maintenant l'utiliser :

```javascript
const mySinglyLinkedList = new SinglyLinkedList();

mySinglyLinkedList.prepend(3);
mySinglyLinkedList.prepend(143);
mySinglyLinkedList.prepend(5);

mySinglyLinkedList.printList(); // [ 5, 143, 3 ]

mySinglyLinkedList.append(21);
mySinglyLinkedList.printList(); // [ 5, 143, 3, 21 ]

console.log(mySinglyLinkedList.search(143));
// Node {
//   data: 143,
//   next: Node { data: 3, next: Node { data: 21, next: null } }
// }

mySinglyLinkedList.remove(143);
mySinglyLinkedList.printList(); // [ 5, 3, 21 ]

console.log(mySinglyLinkedList.search(143)); // null
```

### Listes Chaînées Doubles

Les listes chaînées doubles diffèrent des listes "simples" en ce sens que chaque nœud a également un autre pointeur qui pointe vers l'élément précédent.

Ainsi, cette fois, un seul nœud aura une apparence différente :

```javascript
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.previous = null;
  }
}
```

Voici le même exemple que ci-dessus, mais sous forme de liste chaînée double :

![Visualisation animée d'une liste chaînée double, avec des nœuds ayant les valeurs 1, 2 et 3.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747915463580/605d3541-a702-4bef-9777-28c47800b7aa.gif align="center")

Une implémentation simple pourrait ressembler à ceci :

```javascript
class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  // Ajouter une valeur à la fin de la liste
  append(value) {
    let node = new Node(value);
    // Si la liste est vide
    if (this.head === null) {
      this.head = node;
      this.tail = this.head;
    } else {
      node.previous = this.tail;
      this.tail.next = node;
      this.tail = node;
    }
    
    this.length++;
    return this;
  }

  // Ajouter une valeur au début de la liste
  prepend(value) {
    let node = new Node(value);
    // Si la liste est vide
    if (this.head === null) {
      this.head = node;
      this.tail = this.head;
    } else {
      this.head.previous = node;
      node.next = this.head;
      this.head = node;
    }
    
    this.length++;
    return this;
  }

  remove(value) {
    // Si la liste est vide, retourner null
    if (this.head === null) { 
      return null;
    }

    let currentNode = this.head;

    // Si c'est le premier élément
    if (currentNode.data === value) {
      this.head = currentNode.next;
      // Si l'élément supprimé n'est pas le seul,
      // rendre le pointeur précédent du nouveau head null
      if (this.head) {
        this.head.previous = null;
      // Si l'élément supprimé était le seul élément,
      // pointer la queue vers null également
      } else {
        this.tail = null;
      }
      this.length--;
      return;
    }

    while (currentNode) {
      if (currentNode.data === value) {
        if (currentNode.previous) {
          currentNode.previous.next = currentNode.next;
        }
        if (currentNode.next) {
          currentNode.next.previous = currentNode.previous;
        // Si c'est le dernier élément de la liste, mettre à jour la queue
        // pour pointer vers le nœud précédent
        } else {
          this.tail = currentNode.previous;
        }
        
        this.length--;
        return;
      }
    
      currentNode = currentNode.next;
    }
  }

  search(value) {
    let currentNode = this.head;
    while (currentNode) {
      if (currentNode.data === value) {
        return currentNode;
      }
      currentNode = currentNode.next;
    }

    // Si la valeur n'existe pas, retourner null
    return null;
  }

  printList() {
    let values = [];
    let currentNode = this.head;
    
    while (currentNode) {
      values.push(currentNode.data);
      currentNode = currentNode.next;
    }
    
    console.log(values);
  }
}
```

### Listes Chaînées Circulaires

Avec les listes chaînées circulaires, nous avons le dernier nœud pointant également vers le premier élément, créant ainsi une circularité.

Nous ne regarderons que la liste chaînée circulaire simple pour des raisons de simplicité, donc notre nœud aura la même apparence que dans le premier exemple :

```javascript
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}
```

Le même exemple, sous forme de liste chaînée circulaire :

![Visualisation animée d'une liste chaînée circulaire, les nœuds ayant les valeurs 1, 2 et 3.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747915538225/ea4341cb-2a39-4728-b833-362455a51cdd.gif align="center")

Voici une implémentation simple :

```javascript
class CircularLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  // Ajouter une valeur à la "fin" de la liste
  append(value) {
    let node = new Node(value);
    // Si la liste est vide
    if (this.head === null) {
      this.head = node;
      this.tail = node;
      // En tant que seul nœud de la liste, il doit pointer vers lui-même
      node.next = node;
    } else {
      // En tant que "dernier" nœud, il doit pointer vers la tête (this.tail.next)
      node.next = this.tail.next;
      this.tail.next = node;
      this.tail = node;
    }

    this.length++;
    return this;
  }

  // Ajouter une valeur au début de la liste
  prepend(value) {
    let node = new Node(value);
    node.next = this.head;
    // Mettre à jour le pointeur next du dernier nœud pour pointer vers le nouveau nœud
    this.tail.next = node;
    this.head = node;
    this.length++;
    return this;
  }  

  remove(value) {
    // Si la liste est vide, retourner null
    if (this.head === null) { 
      return null; 
    }

    // Si c'est le premier élément
    if (this.head.data === value) {
      // Si c'est le seul élément
      if (this.head.next === this.head) {
        this.head = null;
        this.tail = null;
        return;
      }
      this.head = this.head.next;
      this.tail.next = this.head;
      this.length--;
      return;
    }

    let currentNode = this.head;
    let prevNode = null;

    // Itérer jusqu'à trouver la valeur ou
    // ne pas la trouver après avoir parcouru toute la liste
    while (currentNode.data !== value || prevNode === null) {
      if (currentNode.next === this.head) { 
        break; 
      }
      prevNode = currentNode;
      currentNode = currentNode.next;
    }

    if (currentNode.data === value) {
      // Si un nœud précédent existe avant l'élément à supprimer,
      // mettre à jour le pointeur next du nœud précédent pour pointer vers
      // celui après l'élément à supprimer
      // (le désassocier)
      if (prevNode) {
        prevNode.next = currentNode.next;
        // Si l'élément à supprimer est le dernier,
        // mettre à jour la queue pour être le nœud précédent
        if (this.tail === currentNode) {
          this.tail = prevNode;
        }
      // Si l'élément à supprimer est le premier de la liste
      } else {
        // Si c'est le seul dans la liste
        if (this.head.next === this.head) {
          this.head = null;
          this.tail = null;
        } else {
          this.head = this.head.next;
          this.tail.next = this.head;
        }
      }
    }
  }

  printList() {
    let nodes = [];
    let currentNode = this.head;
    if (this.head === null) { 
      console.log(nodes); 
      return;
    }

    // Parcourir la liste une fois pour ajouter les valeurs,
    // ne pas tourner en rond
    do {
      nodes.push(currentNode.data);
      currentNode = currentNode.next;
    } while (currentNode !== this.head);

    console.log(nodes);
  }
}
```

#### Complexité temporelle et spatiale

Avec les listes chaînées, la complexité temporelle pour accéder à un élément est dans le pire des cas \\(O(n)\\). *Préfixer* et *suffixer* un élément dépend de savoir si nous avons un pointeur de queue. Si nous en avons un, alors les deux opérations sont \\(O(1)\\), car nous devons seulement arranger les pointeurs. Mais si nous n'avons pas de pointeur de queue, *suffixer* un élément nécessite de parcourir toute la liste, donc c'est une opération \\(O(n)\\). Supprimer un élément est similaire – dans le pire des cas, c'est \\(O(n)\\).

Si la complexité spatiale est linéaire – \\(O(n)\\) – alors la quantité de données à stocker croît linéairement avec le nombre de nœuds dans la liste.

## Interlude : Pointeurs Rapides & Lents

Prenons un rapide aperçu d'une technique qui s'avère utile lorsqu'il s'agit de travailler avec des listes chaînées.

Nous pouvons garder deux pointeurs lors du parcours d'une liste chaînée : rapide et lent. Alors que le rapide augmente de deux étapes, le pointeur lent n'augmentera que d'une seule étape.

### Trouver le nœud du milieu d'une liste chaînée

Lorsque le pointeur rapide atteint la fin de la liste, le pointeur lent sera au nœud "du milieu".

Voyons comment cela pourrait fonctionner :

```javascript
let slow = head;
let fast = head;

while (fast !== null && fast.next !== null) {
  slow = slow.next;
  fast = fast.next.next;
}
```

Nous pouvons penser à une liste comme `[1, 2, 3, 4, 5]` (où chaque valeur est un nœud dans la liste chaînée).

Les deux `fast` et `slow` commencent par pointer vers la tête, c'est-à-dire `1`.

Ensuite, nous mettons à jour le pointeur lent d'une étape, qui sera `2`. Et, `fast` sera à `3`.

Lorsque nous mettons à jour `slow` à nouveau, il sera à `3`. Lorsque le pointeur rapide augmente, il sera deux étapes plus loin, et son pointeur `next` pointera vers la valeur `null`, moment auquel notre boucle cessera d'itérer.

`slow` finira par pointer vers le nœud avec la valeur `3`, qui est le nœud du milieu.

![Visualisation animée de la technique des pointeurs rapides et lents sur une liste chaînée de 5 nœuds.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747915833404/d3c562e8-36e3-459f-a29c-860e0d4869f0.gif align="center")

Avec un nombre pair de nœuds, il y a deux candidats pour le nœud du milieu. Par exemple, avec une liste comme `[1, 2, 3, 4]`, notre implémentation actuelle trouvera le milieu comme `3`. Cette technique est également utile pour détecter les cycles dans une liste chaînée.

## Chapitre Sept : Arbres

Examinons une structure de données non linéaire qui est assez familière à de nombreux développeurs : les arbres.

Que la familiarité engendre le mépris ou non est discutable, alors commençons par le composant le plus simple d'un arbre : un nœud.

Les arbres, comme les listes chaînées, sont constitués de nœuds. La version la plus simple d'un arbre est simplement le **nœud racine** qui n'a pas d'arêtes (liens) pointant vers lui ; c'est-à-dire qu'il n'a pas de **nœuds parents**. C'est le point de départ, en quelque sorte.

Un arbre ne peut avoir qu'un seul nœud racine, et lorsque vous y réfléchissez, *s'il y a* \\(n\\) *nœuds dans un arbre, cela signifie qu'il y a* \\(n - 1\\) *arêtes (liens)* car il n'y a pas d'arête (lien) pointant vers le nœud racine.

Si vous avez regardé un arbre suffisamment longtemps, vous avez peut-être eu un moment d'épiphanie : un arbre a des arbres plus petits en son sein. Une branche peut tout aussi bien être un tronc, ayant d'autres branches pour le petit arbre qu'elle constitue.

La structure de données de l'arbre est ainsi, elle est récursive : *un nœud enfant peut être la racine d'un sous-arbre*.

Deux termes qui sont importants lorsqu'il s'agit d'un nœud d'arbre sont **profondeur** et **hauteur**.

La **profondeur** d'un nœud est la distance à laquelle il se trouve du nœud racine (combien d'arêtes (liens) faut-il parcourir pour aller du nœud racine à celui-ci), et la **hauteur** d'un nœud est la distance à laquelle il se trouve de son **nœud feuille** le plus éloigné (qui est un nœud qui n'a pas d'enfants).

**Note :** La hauteur du nœud racine est la même que la hauteur de l'arbre entier.

Un **arbre équilibré** est celui où *les hauteurs des sous-arbres gauche et droit de chaque nœud diffèrent d'au plus 1*.

### Arbres binaires, arbres de recherche binaire (BSTs)

Un **arbre binaire** est un arbre où chaque nœud a au plus deux enfants. C'est-à-dire qu'un nœud peut avoir un nœud enfant gauche et un nœud enfant droit, et pas plus.

Le nombre maximum de nœuds dans un arbre binaire est \\(2^h - 1\\) où \\(h\\) est la hauteur de l'arbre. C'est là que le *binaire* de l'arbre binaire prend tout son sens : à chaque niveau, le nombre de nœuds croît proportionnellement aux exposants de \\(2\\).

Par exemple, le nombre de nœuds au premier niveau (le niveau 0) est \\(2^0 = 1\\), qui est simplement le nœud racine. Le deuxième niveau a au plus 2 nœuds : \\(2^1 = 2\\) (rappelons que nous comptons à partir de \\(0\\), donc le deuxième niveau est \\(1\\)).

Un **arbre de recherche binaire** est un arbre binaire où les valeurs plus petites que le nœud vont à sa gauche et celles plus grandes que lui vont à sa droite :

$$\text{enfants de gauche } \lt \text{ nœud } \lt \text{ enfants de droite}$$

Voici un exemple :

![Visualisation animée d'un arbre de recherche binaire avec 8 comme nœud racine, 3 comme son enfant gauche, 10 comme son enfant droit. 3 a 1 comme enfant gauche, 6 comme son enfant droit. 6 a 4 comme son enfant gauche, 7 comme son enfant droit. 10 a 14 comme son enfant droit. 14 a 13 comme son enfant gauche. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1747916761231/c0b5301c-6832-43a9-8abd-30f578ac2a29.gif align="center")

Nous pouvons définir un nœud d'arbre comme ceci :

```typescript
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;

  constructor(val: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val;
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
  }
}
```

#### Insertion dans un arbre de recherche binaire

Si nous voulons insérer un nouveau nœud dans un arbre de recherche binaire, nous devons l'insérer à sa place appropriée pour conserver les propriétés d'un BST intactes.

##### Solution récursive :

```typescript
function insertIntoBST(root: TreeNode | null, val: number) {
  if (root === null) {
    return new TreeNode(val);
  }

  if (val < root.val) {
    root.left = insertIntoBST(root.left, val);
  } else {
    root.right = insertIntoBST(root.right, val);
  }

  return root;
}
```

Ici, nous parcourons l'arbre jusqu'à ce que nous trouvions un espace (une position `null`) pour notre valeur qui attend de devenir un `TreeNode`. Nous commençons par le nœud racine. Si la valeur du nœud à insérer est inférieure à la valeur du nœud racine, nous allons à gauche (en passant `root.left` comme argument `root` à la fonction). Sinon, nous allons à droite (en passant `root.right` comme argument `root`).

#### Complexité temporelle et spatiale

La complexité temporelle est \\(O(h)\\) où \\(h\\) est la hauteur de l'arbre. À chaque niveau de l'arbre, nous allons soit à gauche soit à droite, donc nous ne visitons pas nécessairement chaque nœud. La complexité spatiale est également \\(O(h)\\) car nous utilisons la récursivité, créant un nouveau cadre de pile pour chaque appel de fonction.

*Notez que si l'arbre est déséquilibré, la complexité temporelle et spatiale peut être dite être* \\(O(n)\\)*.*

##### Solution itérative :

Nous pouvons également le faire de manière itérative, en utilisant uniquement des pointeurs :

```typescript
function insertIntoBST(root: TreeNode | null, val: number) {
  if (root === null) {
    return new TreeNode(val);
  }

  let prevNode: TreeNode | null = null;
  let currentNode: TreeNode | null = root;

  while (currentNode !== null) {
    prevNode = currentNode;
    if (val < currentNode.val) {
      currentNode = currentNode.left;
    } else {
      currentNode = currentNode.right;
    }
  }

  if (prevNode) {
    if (val < prevNode.val) {
      prevNode.left = new TreeNode(val);
    } else {
      prevNode.right = new TreeNode(val);
    }
  }

  return root;
}
```

Ici, nous faisons la même chose : itérer jusqu'à ce que nous trouvions la place correcte, mais aussi en gardant une trace du nœud parent. Ensuite, nous insérons le nœud comme enfant gauche ou droit du parent, selon sa valeur.

#### Complexité temporelle et spatiale

La complexité temporelle est à nouveau \\(O(h)\\) (*ou si l'arbre est déséquilibré,* \\(O(n)\\)) pour la même raison que dans la solution récursive. Mais la complexité spatiale est constante – \\(O(1)\\) – car nous n'utilisons que des pointeurs.

#### Suppression d'un arbre de recherche binaire

La chose difficile lors de la suppression d'un nœud d'un BST est de maintenir le BST en tant que BST. Toutes les valeurs plus petites doivent toujours aller dans le sous-arbre gauche du nœud racine, et toutes celles qui sont plus grandes doivent aller dans le sous-arbre droit du nœud racine.

Prenons un exemple de la manière dont nous pourrions le faire en JavaScript :

```javascript
function deleteNode(root: TreeNode | null, key: number) {
  if (root === null) {
    return root;
  }

  if (key < root.val) {
    root.left = deleteNode(root.left, key);
  } else if (key > root.val) {
    root.right = deleteNode(root.right, key);
  } else {
    // Le nœud à supprimer n'a pas d'enfants
    if (root.left === null && root.right === null) {
      return null;
    } 

    // Si l'un des enfants gauche ou droit existe,
    // retourner celui qui existe comme le nouvel enfant 
    // du nœud parent (du nœud à supprimer)
    if (root.left === null || root.right === null) {
      return root.left ? root.left : root.right;
    }

    // Si les deux enfants existent, parcourir le sous-arbre gauche, obtenir sa valeur maximale...
    let currentNode = root.left;

    while (currentNode.right !== null) {
      currentNode = currentNode.right;
    }

    // ...le remplacer par le nœud à supprimer
    root.val = currentNode.val;
    // ...puis appliquer la récursion au sous-arbre gauche pour se débarrasser de la valeur dupliquée
    root.left = deleteNode(root.left, root.val);
  }

  return root;
}
```

Nous parcourons l'arbre jusqu'à ce que nous trouvions le nœud à supprimer. Une fois que nous l'avons trouvé, il y a plusieurs choses à faire.

Dans le cas où il n'a pas d'enfants, nous pouvons retourner `null` et en avoir fini avec lui.

S'il a un enfant, nous pouvons retourner celui qui existe en utilisant l'opération ternaire (`return root.left ? root.left : root.right`).

**Note :** *Dans ce cas, nous faisons essentiellement du nœud racine du sous-arbre l'enfant du nœud parent.*

Par exemple, dans l'image, si le nœud à supprimer est 10 (il n'a qu'un seul enfant droit avec la valeur 14), nous faisons de 14 l'enfant droit de 8. Cela ne brise pas notre BST, car ceux qui sont plus grands que 8 continuent d'être dans le sous-arbre droit de 8 :

![Un arbre binaire qui a la valeur 8 comme nœud racine. Il a un enfant gauche avec la valeur 3 et un enfant droit avec la valeur 10. L'enfant gauche a un nœud enfant gauche avec la valeur 1 et un nœud enfant droit avec la valeur 6, qui a un nœud enfant gauche avec la valeur 4 et un nœud enfant droit avec la valeur 7. L'enfant droit du nœud racine avec la valeur 10 a un nœud enfant droit avec la valeur 14, qui a un nœud enfant gauche avec la valeur 13.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747918477656/7a66ad05-3c93-4482-987e-399f65e9dc57.png align="center")

Sinon, si les enfants gauche et droit du nœud à supprimer existent tous les deux, nous devons faire quelque chose de différent.

Dans ce cas, nous remplacerons le nœud à supprimer par la plus grande valeur du sous-arbre gauche.

Mais, après le remplacement, nous aurons deux nœuds de la même valeur aux deux endroits, donc nous devons appliquer `deleteNode` lui-même au sous-arbre dont nous avons pris notre nœud de remplacement.

Tout cela est fait pour maintenir le BST en tant que BST. Cela peut être un peu difficile à comprendre au début, mais [NeetCode a une explication détaillée de ce problème](https://www.youtube.com/watch?v=LFzAoJJt92M).

**Notez** que nous pouvons également utiliser la plus petite valeur du sous-arbre droit. Dans ce cas, notre code ressemblerait à ceci :

```javascript
let currentNode = root.right;

while (currentNode.left !== null) {
  currentNode = currentNode.left;
}

root.val = currentNode.val;
root.right = deleteNode(root.right, root.val);
```

#### Complexité temporelle et spatiale

Similaire à l'insertion dans un BST, à la fois la complexité temporelle et spatiale de la suppression d'un BST sera \\(O(h)\\) où \\(h\\) est la hauteur de l'arbre.

#### Parcours

Nous allons jeter un bref coup d'œil à deux des méthodes les plus célèbres pour parcourir un arbre où l'ordre dans lequel nous visitons les nœuds compte : la recherche en profondeur et la recherche en largeur.

##### 1. Recherche en Profondeur (DFS)

Dans une recherche en profondeur, nous parcourons une branche jusqu'à ce que nous arrivions à un nœud feuille. Ensuite, nous revenons en arrière et faisons la même chose avec une autre branche.

Il y a trois façons courantes de faire une recherche en profondeur :

* parcours préfixe
    
* parcours infixe
    
* parcours postfixe
    

###### Parcours Préfixe :

Cela se passe comme suit : Nous visitons d'abord le nœud, puis passons à son sous-arbre gauche, puis au sous-arbre droit.

**nœud ➜ sous-arbre gauche ➜ sous-arbre droit**

![Visualisation animée du même arbre de recherche binaire affichant le parcours préfixe, avec les nœuds mis en évidence dans cet ordre : 8, 3, 1, 6, 4, 7, 10, 14, 13.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747918872908/dedfc341-d32e-4558-abd6-00ff8d67b46f.gif align="center")

Nous pouvons faire un parcours préfixe de manière récursive :

```javascript
function preorderWalk(node) {
  if (node === null) {
    return;
  }

  console.log(node.val);
  preorderWalk(node.left);
  preorderWalk(node.right);
}
```

###### Parcours Infixe :

Cela se passe comme suit : nous visitons d'abord le sous-arbre gauche, puis le nœud, puis le sous-arbre droit.

**sous-arbre gauche ➜ nœud ➜ sous-arbre droit**

![Visualisation animée du même arbre de recherche binaire affichant le parcours infixe, avec les nœuds mis en évidence dans cet ordre : 1, 3, 4, 6, 7, 8, 10, 13, 14.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747918945108/a1ff3284-8aa0-4815-928c-99cdbd8ac956.gif align="center")

**Note :** Le parcours infixe nous donne les valeurs triées.

Nous pouvons également faire un parcours infixe de manière récursive :

```javascript
function inorderWalk(node) {
  if (node === null) {
    return;
  }

  inorderWalk(node.left);
  console.log(node.val);
  inorderWalk(node.right);
}
```

###### Parcours Postfixe :

Cela se passe comme suit : nous visitons d'abord le sous-arbre gauche, puis le sous-arbre droit, et enfin le nœud.

**sous-arbre gauche ➜ sous-arbre droit ➜ nœud**

![Visualisation animée du même arbre de recherche binaire affichant le parcours postfixe, avec les nœuds mis en évidence dans cet ordre : 1, 4, 7, 6, 3, 13, 14, 10, 8.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747919023258/e3c7f4a3-3ec8-47d3-aa49-e8f4b0f8d30a.gif align="center")

Nous pouvons faire un parcours postfixe de manière récursive :

```javascript
function postorderWalk(node) {
  if (node === null) {
    return;
  }

  postorderWalk(node.left);
  postorderWalk(node.right);
  console.log(node.val);
}
```

##### 2. Recherche en Largeur (BFS)

Dans la recherche en largeur, nous visitons les nœuds niveau par niveau, c'est-à-dire en visitant chaque enfant d'un nœud avant de passer au suivant.

Une file d'attente est utilisée lors de l'implémentation d'une BFS. Puisque nous n'avons pas d'arêtes reliant tous les enfants d'un même niveau ensemble, il est logique de les garder dans une file d'attente et de visiter chacun lorsqu'il est temps. Lorsqu'un nœud est ajouté à la file d'attente et n'a pas encore été visité, il est appelé un **nœud découvert**.

Une opération BFS simple ressemble à ceci (qui est répétée jusqu'à ce que la file d'attente soit vide) :

* visiter le nœud
    
* mettre en file d'attente l'enfant gauche
    
* mettre en file d'attente l'enfant droit
    

Notez que la recherche en largeur est également connue sous le nom de *parcours par niveau*.

![Visualisation animée du même arbre de recherche binaire affichant le parcours par niveau, avec les nœuds mis en évidence dans cet ordre : 8, 3, 10, 1, 6, 14, 4, 7, 13.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747919081789/17beb70f-7302-4f32-9a9a-72d69e190ac9.gif align="center")

Un exemple simple de parcours par niveau en JavaScript pourrait ressembler à ceci :

```javascript
function levelOrderWalk(root) {
  if (root === null) {
    return;
  }

  let queue = [];
  queue.push(root);

  while (queue.length > 0) {
    let currentNode = queue[0];

    console.log(currentNode.val);

    if (currentNode.left !== null) {
      queue.push(currentNode.left);
    }

    if (currentNode.right !== null) {
      queue.push(currentNode.right);
    }

    // Retirer le nœud actuel
    queue.shift();
  }
}
```

Cet exemple est basé sur le [Gist GitHub](https://gist.github.com/vaidehijoshi/27f9fa6b6b68f70360019805b5ca3692#file-level_order_search-js) de Vaidehi Joshi.

## Chapitre Huit : Tas / File de Priorité

Il est maintenant temps de jeter un coup d'œil à une structure de données appelée *tas*, qui est un excellent moyen d'implémenter un [type de données abstrait](https://en.wikipedia.org/wiki/Abstract_data_type) appelé **file de priorité**. Ils sont si interdépendants que les files de priorité sont parfois appelées tas – car les tas sont un moyen très efficace de créer une file de priorité.

### Propriétés des Tas

Le type de tas qui nous intéresse est également appelé **tas binaire** car il s'agit simplement d'un arbre binaire qui possède des propriétés spécifiques.

L'une d'entre elles est qu'il doit être un **arbre binaire complet**, ce qui signifie que tous les niveaux doivent être remplis, et *tous les nœuds du dernier niveau doivent être aussi à gauche que possible*.

Par exemple, en ce qui concerne la forme, ceci est un arbre binaire complet :

![Visualisation animée d'un arbre avec un nœud racine ayant deux enfants, les enfants gauche et droit ayant chacun deux enfants. L'enfant gauche de l'enfant gauche n'a qu'un enfant gauche.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747919274226/cdc2f987-3327-4220-8584-ad3999ea7f39.gif align="center")

Mais les tas doivent également être soit un **tas max** soit un **tas min** – tous les nœuds parents doivent être soit supérieurs ou égaux aux valeurs de leurs enfants (s'il s'agit d'un tas max) soit inférieurs ou égaux aux valeurs de leurs enfants (s'il s'agit d'un tas min).

Un tas max pourrait ressembler à ceci :

![Visualisation animée d'un tas max, ayant 42 en haut, 19 à sa gauche, 36 à sa droite. 19 a 17 à sa gauche, 3 à sa droite. 36 a 25 à sa gauche, 1 à sa droite. 17 a 2 à sa gauche.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747919301787/6a3b30cd-a686-4112-80a9-0249c7597751.gif align="center")

**Note :** Un enfant gauche n'a pas besoin d'être inférieur à l'enfant droit, comme dans un arbre de recherche binaire. De plus, nous pouvons toujours avoir des valeurs dupliquées dans un tas.

Un tas min, en revanche, a les valeurs des nœuds parents inférieures à celles de leurs enfants :

![Visualisation animée d'un tas min, ayant 1 en haut, 2 à sa gauche, 3 à sa droite. 2 a 17 à sa gauche, 19 à sa droite. 3 a 36 à sa gauche, 7 à sa droite. 17 a 42 à sa gauche.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747919335031/b5b82848-ac1f-405d-9124-725a9c26af55.gif align="center")

**Note :** Lorsque nous avons un tas max, le nœud racine aura la valeur maximale. Et, si nous avons un tas min à la place, le nœud racine aura la valeur minimale.

### Tas avec Tableaux

Nous pouvons créer un tas en utilisant un tableau. Puisque le nœud racine est l'élément le plus intéressant avec soit une valeur maximale soit minimale, il sera le premier élément de notre tableau, résidant à l'index 0.

Ce qui est bien avec l'utilisation d'un tableau, c'est que, étant donné l'index \\(i\\) d'un nœud parent, son enfant gauche sera à l'index \\(2i + 1\\), et son enfant droit sera à l'index \\(2i + 2\\).

![Visualisation animée du tas max ci-dessus implémenté comme un tableau. L'index d'un enfant gauche correspond à 2i+1, l'index d'un enfant droit correspond à 2i+2.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747919415922/b98a55a9-f9cc-4e11-8d53-f5a8a411d861.gif align="center")

Étant donné cela, tout nœud enfant aura son parent à l'index \\(\lfloor{\frac{(n - 1)}{2}}\rfloor\\).

**Note :** \\(\lfloor\\) et \\(\rfloor\\) indiquent la [fonction plancher](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions).

Une question que nous pourrions nous poser à ce moment est de savoir pourquoi nous devrions utiliser un tableau du tout ?

La réponse réside dans le mot **file d'attente** d'une **file de priorité**. Puisqu'une file d'attente est principalement préoccupée par le premier élément (suivant le [principe FIFO](https://en.wikipedia.org/wiki/FIFO_\(computing_and_electronics\))), un tableau peut être un choix idéal. Dans une file de priorité, chaque élément a une priorité, et la valeur avec la priorité la plus élevée est désenfilée en premier.

### Insertion/Suppression d'Éléments

Prenons un aperçu de la manière dont nous pouvons ajouter un élément à un tas.

Nous savons que nous devons ajouter le nouvel élément à l'endroit le plus bas à gauche, mais une fois que nous faisons cela, cela pourrait violer la propriété de tas max ou min. Alors, comment pouvons-nous éviter de violer la **propriété d'ordre de tas** ?

Nous allons **heapifier**, bien sûr !

Disons que nous voulons ajouter un nœud avec la valeur `20` :

![Visualisation animée du tas max ci-dessus. Un nouvel élément 20 est d'abord inséré à l'endroit le plus à gauche possible. Ensuite, il échange de place avec 17 puis avec 19, arrivant à gauche de 42.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747919523941/eb0959dd-fcf8-4fb7-9ebf-938fde24ba10.gif align="center")

Ainsi, heapify est l'échange de nœuds jusqu'à ce que nous sachions que la propriété d'ordre de tas est maintenue.

Une chose similaire se produit lorsque nous devons supprimer un élément. Mais puisque nous nous préoccupons principalement de l'élément maximum ou minimum, nous devons simplement supprimer le nœud racine. Alors, comment allons-nous faire cela ?

Nous commençons par échanger le dernier élément (celui en bas à gauche) avec la racine. Maintenant, nous pouvons facilement supprimer la "racine", qui réside en tant que nœud feuille. Mais nous devons toujours maintenir la propriété d'ordre de tas, donc nous devons **heapifier** à nouveau.

![Visualisation animée du tas max ci-dessus. 2 échange de place avec 42, 42 disparaissant. 2 échange ensuite de place avec 36 et 25, maintenant 36 arrive en haut.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747919564248/0e7b9a38-6b23-4448-a804-cf095d16f30e.gif align="center")

### Tri par Tas

Mieux encore, si nous avons un tas, et que nous le heapifions continuellement, nous pouvons trier un tableau.

Commençons par construire un tas max :

```typescript
function buildMaxHeap(arr: number[]) {
  /*
  Index du dernier nœud interne 
  (c'est-à-dire, le parent du dernier nœud feuille, 
   ou, le dernier nœud non feuille).
  Le dernier nœud feuille résidera à l'index arr.length - 1,
  donc, nous obtenons son parent en utilisant la formule mentionnée ci-dessus.
  */
  let i = Math.floor((arr.length - 1) / 2);
    
  while (i >= 0) {
    heapify(arr, i, arr.length);
    i--;
  }
    
  return arr;
}
```

Ensuite, la fonction `heapify` :

```typescript
function heapify(arr: number[], i: number, maxLength: number) {
  while (i < maxLength) {
    let index = i;
    let leftChildIdx = 2 * i + 1;
    let rightChildIdx = leftChildIdx + 1;

    if (leftChildIdx < maxLength && arr[leftChildIdx] > arr[index]) {
      index = leftChildIdx;
    }

    if (rightChildIdx < maxLength && arr[rightChildIdx] > arr[index]) {
      index = rightChildIdx;
    }
        
    if (index === i) { return; }
        
    // Échanger
    [arr[i], arr[index]] = [arr[index], arr[i]];

    i = index;
  }
}
```

Avec un index donné `i`, nous obtenons ses index d'enfants gauche et droit, et si les index sont dans les limites, nous vérifions s'ils sont désordonnés. Dans ce cas, nous faisons de `index` l'index de l'enfant, et nous échangeons les deux nœuds. Ensuite, nous continuons avec ce nouvel index, en l'assignant à `i`.

Maintenant, `heapify` est bien et tout, mais comment pouvons-nous l'utiliser pour le tri ?

```typescript
function heapSort(arr: number[]) {
  buildMaxHeap(arr);

  let lastElementIdx = arr.length - 1;

  while (lastElementIdx > 0) {
    [arr[0], arr[lastElementIdx]] = [arr[lastElementIdx], arr[0]];

    heapify(arr, 0, lastElementIdx);
    lastElementIdx--;
  }

  return arr;
}
```

**Notez** que notre tas max `[42, 19, 36, 17, 3, 25, 1, 2]` ne changera pas lorsqu'il est utilisé dans la fonction `buildMaxHeap`, car c'est déjà un tas max ! Mais s'il devait avoir `17` comme enfant droit de `42`, alors `17` aurait `25` comme enfant, ce qui brise la propriété d'ordre du tas. Donc, utiliser `buildMaxHeap` avec cette version cassée échangera correctement `17` et `25`, en faisant un tas max :

```typescript
buildMaxHeap([42, 36, 17, 19, 3, 25, 1, 2]);

// -> [42, 36, 25, 19, 3, 17, 1, 2]
```

Dans `heapSort`, avec notre nouveau tas max, nous commencerons par échanger les premiers et derniers nœuds. Ensuite, nous continuerons à heapifier jusqu'à ce que tous les éléments soient à leur place. Si nous l'utilisons avec notre propre tas max, nous pouvons voir qu'il retourne le tableau trié :

```typescript
heapSort([42, 19, 36, 17, 3, 25, 1, 2]);
// -> [1, 2, 3, 17, 19, 25, 36, 42]
```

Les exemples sont adaptés de [l'article de Vaidehi Joshi](https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82).

#### Complexité temporelle et spatiale

Le tri par tas, en tant que bel algorithme de tri qu'il est, s'exécute en temps \\(O(n \ log \ n)\\).

Dans cet exemple, la construction du tas max commence à partir du dernier nœud non feuille et remonte jusqu'au nœud racine, appelant `heapify` à chaque fois. La fonction `heapify` a une complexité temporelle de \\(O(log \ n)\\) car nous travaillons avec un arbre binaire, et dans le pire des cas, nous devons le faire pour tous les niveaux. Puisque nous le faisons \\(n / 2\\) fois, globalement, `buildMaxHeap` a une complexité temporelle de \\(O(n \ log \ n)\\).

Nous échangeons les premiers et derniers éléments, et nous heapifions en parcourant chaque élément, donc cela est également globalement une opération \\(O(n \ log \ n)\\) – ce qui rend la complexité temporelle de `heapSort` \\(O(n \ log \ n)\\)*.*

**Note :** La construction du tas max [peut être améliorée pour avoir](https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity) \\(O(n)\\) [temps d'exécution](https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity).

Puisqu'il n'y a pas d'utilisation d'espace auxiliaire, la complexité spatiale est constante, \\(O(1)\\).

## Chapitre Neuf : Retour sur Trace

Commençons par admettre ce fait : le retour sur trace est difficile. Ou plutôt, *le comprendre la première fois* est difficile. Ou, c'est l'un de ces concepts que vous pensez avoir saisi, pour réaliser plus tard que vous ne l'aviez en fait pas.

Nous allons nous concentrer sur un problème de trouver les sous-ensembles d'un tableau, mais avant cela, imaginons que nous marchons le long d'un chemin.

Ensuite, nous atteignons une fourche. Nous choisissons l'un des chemins, et nous marchons.

Ensuite, nous atteignons une autre fourche dans le chemin. Nous choisissons à nouveau l'un des chemins, et nous continuons à marcher, puis nous atteignons une impasse. Donc, nous *revenons en arrière* jusqu'au dernier point où nous avions une fourche, puis nous empruntons l'autre chemin que nous n'avions pas choisi la première fois.

Ensuite, nous atteignons une autre impasse. Donc, nous *revenons en arrière* une fois de plus et nous réalisons qu'il n'y a plus d'autres chemins que nous pouvons emprunter à partir de là. Donc, nous *revenons en arrière* à nouveau, et nous explorons l'autre chemin que nous n'avions pas choisi la première fois que nous sommes arrivés à ce point.

Nous atteignons encore une autre impasse, donc nous *revenons en arrière*. Nous voyons qu'il n'y a plus de chemins à explorer, donc nous *revenons en arrière* une fois de plus.

Maintenant, nous sommes à notre point de départ. Il n'y a plus de chemins à explorer, donc nous pouvons arrêter de marcher.

C'était une agréable mais fatigante promenade, et cela s'est passé comme ceci :

![Visualisation animée du concept de retour sur trace.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747920157477/3151155c-d40c-408d-bff6-5d326ad0a0f3.gif align="center")

Maintenant, jetons un coup d'œil à un problème LeetCode.

### Sous-ensembles

La description pour [Subsets](https://leetcode.com/problems/subsets) dit :

> Étant donné un tableau d'entiers `nums` d'éléments **uniques**, retourner *tous les sous-ensembles possibles (l'ensemble des parties)*.
> 
> L'ensemble des solutions **ne doit pas** contenir de sous-ensembles dupliqués. Retourner la solution dans **n'importe quel ordre**.

Par exemple :

```plaintext
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

Ou :

```plaintext
Input: nums = [0]
Output: [[], [0]]
```

Avant de plonger dans le code de la solution, jetons un coup d'œil à la manière dont le retour sur trace fonctionnera dans ce cas. Appelons le tableau `nums` `items` à la place :

![Visualisation animée du retour sur trace pour un tableau [1, 2, 3], explorant chaque choix possible.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747920218696/a85bf516-9bc1-4231-ab39-4a31ce1a8e6d.gif align="center")

Pour chaque élément dans `items`, nous avons initialement deux choix : inclure l'élément, ou ne pas l'inclure.

Pour chaque niveau \\(n\\) dans cet *arbre de décision*, nous avons l'option d'inclure l'élément suivant dans `items`. Nous avons \\(2^n\\) sous-ensembles possibles au total.

Simplifions un peu l'exemple, et disons que `items` est maintenant `['a', 'b']` (**Nous ignorerons les spécificités du problème pour l'instant**).

![Visualisation animée du retour sur trace pour un tableau ['a', 'b'], explorant chaque choix possible.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747920275978/ab435765-7b05-4939-bd72-55dcfae7a6d4.gif align="center")

Dans ce cas, nous pouvons utiliser le retour sur trace comme ceci :

```typescript
function subsets(items: string[]) {
  let result: string[][] = [];
  let currentSubset: string[] = [];

  function backtrack(idx: number) {
    if (idx >= items.length) {
      result.push([...currentSubset]);
      return;
    }

    currentSubset.push(items[idx]);
    backtrack(idx + 1);

    currentSubset.pop();
    backtrack(idx + 1);
  }

  backtrack(0);

  return result;
}

console.log(subsets(['a', 'b']));
// -> [['a', 'b'], ['a'], ['b'], []]
```

Eh bien, cela semble simple à première vue, mais que se passe-t-il ?

Une chose à remarquer est que nous `pop` de `currentSubset`, puis nous appelons `backtrack`. Dans notre exemple de marche, c'est la partie où nous revenons à notre point précédent, et continuons notre marche.

Dans la première animation, nous avons indiqué une impasse avec une marque de croix, et dans ce cas, une impasse est le **cas de base** que nous atteignons.

Cela peut encore être difficile à comprendre, alors ajoutons quelques `console.log` utiles, et voyons la sortie :

```typescript
function subsets(items: string[]) {
  let result: string[][] = [];
  let currentSubset: string[] = [];

  function backtrack(idx: number) {
    console.log(`======= this is backtrack(${arguments[0]}) =======`)
    if (idx >= items.length) {
      console.log(`idx is ${idx}, currentSubset is [${currentSubset}], adding it to result...`);
      result.push([...currentSubset]);
      console.log(`backtrack(${arguments[0]}) is returning...\n`)
      return;
    }

    currentSubset.push(items[idx]);
    console.log(`added ${items[idx]} to currentSubset, inside backtrack(${arguments[0]})`);
    console.log(`calling backtrack(${idx + 1})...`)
    backtrack(idx + 1);

    let item = currentSubset.pop();
    console.log(`popped ${item} from currentSubset, inside backtrack(${arguments[0]})`);
    console.log(`calling backtrack(${idx + 1})...`)
    backtrack(idx + 1);

    console.log(`******* done with backtrack(${arguments[0]}) *******\n`);
  }

  backtrack(0);

  return result;
}

console.log(subsets(['a', 'b']));
```

La sortie ressemble à ceci :

```plaintext
======= this is backtrack(0) =======
added a to currentSubset, inside backtrack(0)
calling backtrack(1)...
======= this is backtrack(1) =======
added b to currentSubset, inside backtrack(1)
calling backtrack(2)...
======= this is backtrack(2) =======
idx is 2, currentSubset is [a,b], adding it to result...
backtrack(2) is returning...

popped b from currentSubset, inside backtrack(1)
calling backtrack(2)...
======= this is backtrack(2) =======
idx is 2, currentSubset is [a], adding it to result...
backtrack(2) is returning...

******* done with backtrack(1) *******

popped a from currentSubset, inside backtrack(0)
calling backtrack(1)...
======= this is backtrack(1) =======
added b to currentSubset, inside backtrack(1)
calling backtrack(2)...
======= this is backtrack(2) =======
idx is 2, currentSubset is [b], adding it to result...
backtrack(2) is returning...

popped b from currentSubset, inside backtrack(1)
calling backtrack(2)...
======= this is backtrack(2) =======
idx is 2, currentSubset is [], adding it to result...
backtrack(2) is returning...

******* done with backtrack(1) *******

******* done with backtrack(0) *******

[ [ 'a', 'b' ], [ 'a' ], [ 'b' ], [] ]
```

Si vous avez remarqué, *Ajouter* `'a'`? et *Continuer*? les flèches au premier niveau sont des appels à `backtrack(0)`.

*Ajouter* `'b'`? et *Continuer*? les flèches au deuxième niveau sont des appels à `backtrack(1)`.

Les appels `backtrack(2)` sont lorsque nous atteignons les "impasses". Dans ces cas, nous ajoutons `currentSubset` à `result`. Nous atteignons toujours le cas de base dans un appel `backtrack(2)` car c'est seulement lorsque `idx` est égal à `items.length`.

![Visualisation animée de la fonction backtrack pour le tableau ['a', 'b'].](https://cdn.hashnode.com/res/hashnode/image/upload/v1747920409397/0c18c7a6-1776-415b-8918-a6cafe6ba70c.gif align="center")

**Note :** Nous avons modifié la fonction dans les exemples ci-dessus pour qu'elle fonctionne avec des chaînes, mais dans la solution réelle, nous ne traiterons que des nombres, donc en TypeScript, `result` et `currentSubset` ressembleront à ceci :

```typescript
let result: number[][] = [];
let currentSubset: number[] = [];
```

De plus, les types de paramètres et de retour de la fonction sont différents :

```typescript
function subsets(nums: number[]): number[][] { ... }
```

Sinon, tout reste le même.

#### Complexité temporelle et spatiale

Un sous-ensemble est, dans le pire des cas, de longueur \\(n\\) qui est la longueur de notre entrée. Nous aurons \\(2^n\\) sous-ensembles et puisque nous utilisons également un [opérateur de propagation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) dans notre exemple pour copier `currentSubset`, la complexité temporelle sera \\(O(n \cdot 2^n)\\). La complexité spatiale est – *je pense* – \\(O(n \cdot 2^n)\\) également en raison de la pile d'appels récursifs (qui est de profondeur `n`), et de l'espace nécessaire pour `result` (qui est dans le pire des cas \\(2^n\\)).

## Chapitre Dix : Tries

La structure de données trie [tire son nom du mot *re****trie****val*](https://en.wikipedia.org/wiki/Trie#History,_etymology,_and_pronunciation) – et elle est généralement prononcée comme "try", afin que nous ne soyons pas confus avec une autre structure de données familière et amicale, "tree".

Mais un trie est toujours une structure de données en forme d'arbre (ou similaire à un arbre) dont les nœuds stockent généralement des lettres individuelles. Ainsi, en parcourant les nœuds d'un trie, nous pouvons récupérer des chaînes.

Les tries sont utiles pour des applications telles que l'autocomplétion et la vérification orthographique – et plus notre trie est grand, moins nous avons de travail à faire pour insérer une nouvelle valeur.

**Note :** L'utilisation de tableaux n'est pas très efficace en mémoire, mais pour l'instant, nous allons nous en tenir à l'implémentation de tableau.

Tout d'abord, voyons à quoi ressemble un trie :

![Visualisation animée d'un trie ayant les valeurs "sea" et "see"](https://cdn.hashnode.com/res/hashnode/image/upload/v1747920685051/e152eedd-75c6-478b-8291-5510b8f1421c.gif align="center")

Dans ce trie, nous pouvons récupérer les chaînes "sea" et "see" – mais pas "sew", par exemple.

Il y a beaucoup de choses qui se passent, mais nous pouvons essayer de le comprendre pièce par pièce.

Regardons un nœud de trie.

Nous allons créer une classe `TrieNode` qui a `children`, qui est un tableau de longueur 26 (afin que chaque index corresponde à une lettre de l'alphabet anglais), et une variable de drapeau `isEndOfWord` pour indiquer si ce nœud représente le dernier caractère d'un mot :

```typescript
class TrieNode {
  children: (TrieNode | null)[];
  isEndOfWord: boolean;

  constructor() {
    this.children = Array.from({ length: 26 }, () => null);
    this.isEndOfWord = false;
  }
}
```

Nous initialisons `children` avec des valeurs `null`. À mesure que nous ajoutons un caractère à notre trie, l'index correspondant à ce caractère sera rempli.

**Note :** Nous ne stockons pas le caractère lui-même dans cette implémentation – il est implicite dans l'utilisation des index.

Dans un trie, nous commençons avec un nœud racine vide.

```typescript
class Trie {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }
  // ...
}
```

Pour insérer un mot, nous allons boucler à travers chaque caractère, et initialiser un nouveau `TrieNode` à l'index correspondant.

```typescript
insert(word: string) {
  let currentNode = this.root;
  for (const char of word) {
    let idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
    if (currentNode.children[idx] === null) {
      currentNode.children[idx] = new TrieNode();
    }
    currentNode = currentNode.children[idx];
  }

  currentNode.isEndOfWord = true;
}
```

Une fois que nous atteignons le nœud qui indique le dernier caractère du mot que nous avons inséré, nous marquons également la variable `isEndOfWord` comme `true`.

**Note :** `word` sera en minuscules dans ces exemples – sinon, nous devons le convertir, par exemple :

```typescript
word = word.toLowerCase();
```

Pour rechercher l'existence d'un mot dans le trie, nous ferons une chose similaire. Nous regarderons les nœuds pour chaque caractère, et si nous atteignons le dernier qui a `isEndOfWord` marqué comme `true`. Cela signifie que nous avons trouvé le mot :

```typescript
search(word: string) {
  let currentNode = this.root;
  for (const char of word) {
    let idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
    if (currentNode.children[idx] === null) {
      return false;
    }      
    currentNode = currentNode.children[idx];
  }

  return currentNode.isEndOfWord;
}
```

**Note :** Si nous trouvons le mot que nous cherchons, alors c'est ce qu'on appelle un **hit de recherche**. Sinon, nous avons un **miss de recherche** et le mot n'existe pas dans notre trie.

Supprimer un mot est un peu plus difficile. Disons que nous voulons supprimer le mot "see." Mais, il y a aussi un autre mot "sea," avec le même préfixe ('s' et 'e'). Donc, nous devons supprimer uniquement les nœuds que nous sommes autorisés à supprimer.

Pour cette raison, nous allons définir une fonction récursive. Une fois que nous atteignons le dernier caractère du mot que nous voulons supprimer, nous allons revenir en arrière et supprimer les caractères que nous pouvons supprimer :

```typescript
const removeRecursively = (node: TrieNode | null, word: string, depth: number) => {
  if (node === null) {
    return null;
  }

  if (depth === word.length) {
    if (node.isEndOfWord) {
      node.isEndOfWord = false;
    }
    if (node.children.every(child => child === null)) {
      node = null;
    }

    return node;
  }

  let idx = word[depth].charCodeAt(0) - 'a'.charCodeAt(0);
  node.children[idx] = removeRecursively(node.children[idx], word, depth + 1);

  if (node.children.every(child => child === null) && !node.isEndOfWord) {
    node = null;
  }

  return node;
}
```

`depth` indique l'index du mot, ou *la profondeur du trie que nous atteignons*.

Une fois que `depth` est égal à la longueur du mot (un de plus que le dernier caractère), nous vérifions s'il s'agit de la fin du mot. Si c'est le cas, nous allons le marquer comme `false` maintenant, car ce mot n'existera plus à partir de maintenant. Ensuite, nous ne pouvons marquer le nœud comme `null` que s'il n'a pas d'enfants (en d'autres termes, si tous sont `null`). Nous allons appliquer cette logique à chaque nœud enfant de manière récursive jusqu'à ce que le mot soit supprimé aussi loin qu'il peut l'être.

Voici l'exemple final d'implémentation d'un trie :

```typescript
class TrieNode {
  children: (TrieNode | null)[];
  isEndOfWord: boolean;

  constructor() {
    this.children = Array.from({ length: 26 }, () => null);
    this.isEndOfWord = false;
  }
}

class Trie {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode();
  }

  insert(word: string) {
    let currentNode = this.root;
    for (const char of word) {
      let idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
      if (currentNode.children[idx] === null) {
        currentNode.children[idx] = new TrieNode();
      }
      currentNode = currentNode.children[idx];
    }

    currentNode.isEndOfWord = true;
  }

  search(word: string) {
    let currentNode = this.root;
    for (const char of word) {
      let idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
      if (currentNode.children[idx] === null) {
        return false;
      }      
      currentNode = currentNode.children[idx];
    }

    return currentNode.isEndOfWord;
  }

  remove(word: string) {
    const removeRecursively = (node: TrieNode | null, word: string, depth: number) => {
      if (node === null) {
        return null;
      }

      if (depth === word.length) {
        if (node.isEndOfWord) {
          node.isEndOfWord = false;
        }
        if (node.children.every(child => child === null)) {
          node = null;
        }

        return node;
      }

      let idx = word[depth].charCodeAt(0) - 'a'.charCodeAt(0);
      node.children[idx] = removeRecursively(node.children[idx], word, depth + 1);

      if (node.children.every(child => child === null) && !node.isEndOfWord) {
        node = null;
      }

      return node;
    }

    removeRecursively(this.root, word, 0);
  }
}

let t = new Trie();

t.insert('sea');
t.insert('see');

console.log(t.search('sea')); // true
console.log(t.search('see')); // true

console.log(t.search('hey')); // false
console.log(t.search('sew')); // false

t.remove('see');

console.log(t.search('see')); // false 
console.log(t.search('sea')); // true
```

#### Complexité temporelle et spatiale

La complexité temporelle de la création d'un trie sera \\(O(m * n)\\) où \\(m\\) est le mot le plus long et \\(n\\) est le nombre total de mots. L'insertion, la recherche et la suppression d'un mot est \\(O(a * n)\\) où \\(a\\) est la longueur du mot et \\(n\\) est le nombre total de mots.

En ce qui concerne la complexité spatiale, dans le pire des cas, chaque nœud peut avoir des enfants pour tous les caractères de l'alphabet que nous représentons. Mais, la taille de l'alphabet est constante, donc le besoin de stockage croîtra proportionnellement au nombre de nœuds que nous avons, ce qui est \\(O(n)\\) où \\(n\\) est le nombre de nœuds.

## Chapitre Onze : Graphes

Un graphe est probablement *la* structure de données que tout le monde connaît, quelle que soit sa profession ou ses intérêts.

La [théorie des graphes](https://en.wikipedia.org/wiki/Graph_theory#Representation) est un sujet très vaste, mais nous allons simplement examiner certains des principaux ingrédients qui constituent un graphe et comment le représenter, ainsi que les parcours de base de graphes.

Dans un graphe, il y a deux composants principaux : les sommets (ou nœuds) et les arêtes qui relient ces sommets.

**Note :** Ici, nous allons utiliser "sommet" et "nœud" de manière interchangeable. Les termes "sommets adjacents" et "voisins" sont également utilisés de manière interchangeable.

Un graphe peut être **orienté** ou **non orienté**. Avec une arête orientée, nous avons un sommet d'origine et un sommet de destination. D'un autre côté, une arête non orientée est bidirectionnelle, l'origine et la destination ne sont pas fixes.

**Note :** Il peut également y avoir des [graphes mixtes](https://en.wikipedia.org/wiki/Graph_\(discrete_mathematics\)#Mixed_graph) qui ont à la fois des arêtes orientées et non orientées.

Un graphe peut également être pondéré ou non pondéré, chaque arête peut avoir des poids différents, représentant généralement le coût d'aller d'un sommet à l'autre.

Nous pouvons définir un graphe comme ceci :

$$G = (V, \ E)$$

\\(V\\) est un ensemble de sommets, et \\(E\\) est un ensemble d'arêtes.

Par exemple, si nous avons un graphe orienté comme ceci :

![Visualisation animée d'un graphe avec des nœuds A, B, C, D. A a des arêtes orientées vers B et C, C en a une vers B et D. D en a une vers C. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1747921387268/fe3d0ef9-a271-4c87-9143-84e80e41af5f.gif align="center")

Alors, nous avons les sommets :

$$V = \{A, \ B, \ C, \ D\}$$

Et, les arêtes sont :

$$E = \{(A, \ B), \ (A, \ C), \ (C, \ B), \ (C, \ D)\, \ (D, \ C)\}$$

Si nous avons un graphe non orienté tel que celui-ci :

![Visualisation animée du même graphe ci-dessus avec des arêtes non orientées.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747921458245/d2920859-81c0-4082-a49d-e41b08b81124.gif align="center")

Nous avons les mêmes sommets :

$$V = \{A, \ B, \ C, \ D\}$$

Mais nos arêtes peuvent ressembler à ceci :

$$E = \{\{B, \ A\}, \{A, \ C\}, \{C, \ B\}, \{D, \ C\}\}$$

**Note :** Nous utilisons des parenthèses lorsqu'il s'agit d'arêtes orientées, mais des accolades pour les arêtes non orientées car il n'y a pas de direction d'un sommet à l'autre.

Lorsque deux sommets partagent une arête, ils sont **adjacents** l'un à l'autre. Le **degré** d'un sommet est le nombre de sommets adjacents à celui-ci. Nous pouvons également définir le degré comme le nombre d'arêtes sortant du sommet. Par exemple, dans l'image ci-dessus, le sommet A a un degré de 2.

Un **chemin simple** est celui où nous ne répétons aucun sommet lors du parcours du graphe.

Un exemple pourrait ressembler à ceci :

![Visualisation animée du même graphe ci-dessus avec les nœuds mis en évidence dans cet ordre : A, B, C, D.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747921569022/50f556e7-f954-4203-8c4b-493b2be5a353.gif align="center")

Un **cycle** est un chemin simple, sauf que nous finissons par revenir au sommet de départ :

![Visualisation animée du même graphe ci-dessus avec les nœuds mis en évidence dans cet ordre : A, B, C (avec toutes les arêtes également mises en évidence).](https://cdn.hashnode.com/res/hashnode/image/upload/v1747921594728/717408ba-f9fb-4cef-9b52-70f487e9162d.gif align="center")

### Représentation des Graphes

En ce qui concerne la représentation des graphes, il existe plusieurs façons de le faire, et nous allons en examiner trois : une liste d'arêtes, une matrice d'adjacence et une liste d'adjacence.

#### Liste d'Arêtes

Nous pouvons simplement mettre toutes les arêtes dans un tableau :

```plaintext
[ [A, B], [A, C], [B, C], [C, D] ]
```

Mais pour trouver une arête dans une liste d'arêtes, nous devrons itérer à travers elles, donc cela aura une complexité temporelle de \\(O(E)\\), où dans le pire des cas, nous rechercherons toute la liste pour trouver une arête. De même, elle nécessite \\(O(E)\\) d'espace pour représenter toutes les arêtes.

#### Matrice d'Adjacence

La matrice d'adjacence pour notre exemple pourrait ressembler à ceci :

$$\left\lceil\begin{matrix}& A & B & C & D \\A & 0 & 1 & 1 & 0 \\B & 1 & 0 & 1 & 0 \\C & 1 & 1 & 0 & 1 \\D & 0 & 0 & 1 & 0\end{matrix}\right\rceil$$

Chaque ligne est pour un sommet, et la colonne correspondante montre la relation entre ces sommets. Par exemple, le sommet A n'a pas d'arête pointant vers D, donc la cellule qui correspond à A et D est 0. D'un autre côté, A est connecté à B et C, donc ces cellules ont la valeur 1.

**Note :** Si le graphe est pondéré, nous pouvons simplement mettre le poids au lieu de `1`, et lorsqu'il n'y a pas d'arête, la valeur peut rester `0`.

*Une matrice d'adjacence aura des 0s dans la "diagonale principale", montrant qu'il n'y a pas de boucles.*

Essayons de l'implémenter en TypeScript.

Nous commencerons par un sommet de graphe minimal :

```typescript
class GraphVertex {
  value: string | number;

  constructor(value: string | number) {
    this.value = value;
  }
}
```

Maintenant, nous pouvons définir notre graphe. Nous allons le rendre très simple avec trois propriétés à maintenir : `matrix` pour représenter le graphe sous forme de matrice d'adjacence, `vertices` pour maintenir les sommets, et `isDirected` pour indiquer si notre graphe est orienté :

```typescript
class Graph {
  matrix: number[][];
  vertices: GraphVertex[];
  isDirected: boolean;

  constructor(vertices: GraphVertex[], isDirected = true) {
    this.vertices = vertices;
    this.isDirected = isDirected;
    // ...
  }

  // ...
}
```

L'initialisation de notre matrice d'adjacence pourrait ressembler à ceci :

```typescript
this.matrix = Array.from({ length: vertices.length }, () => {
  return Array.from({ length: vertices.length }, () => 0)
});
```

Nous aurons un tableau de la longueur des sommets. Chaque élément du tableau est un tableau de la longueur des sommets également, mais rempli de zéros.

Dans notre exemple avec quatre sommets, la matrice d'adjacence initiale ressemble à ceci :

```typescript
[ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
```

Ensuite, ajouter une arête consiste simplement à marquer la valeur correspondante comme `1`, afin que nous puissions représenter une connexion entre deux sommets :

```typescript
this.matrix[this.vertices.indexOf(v1)][this.vertices.indexOf(v2)] = 1;
```

**Note :** Cette implémentation suppose que tous les sommets sont distincts.

Si nous avons un graphe non orienté, nous pouvons le faire dans les deux sens :

```typescript
if (!this.isDirected) {
  this.matrix[this.vertices.indexOf(v2)][this.vertices.indexOf(v1)] = 1;
}
```

Supprimer une arête, dans ce cas, consistera simplement à réinitialiser la valeur à `0` :

```typescript
this.matrix[this.vertices.indexOf(v1)][this.vertices.indexOf(v2)] = 0;
```

Et, vérifier l'existence d'une arête consiste simplement à vérifier si la valeur correspondante est `0` ou non :

```typescript
this.matrix[this.vertices.indexOf(v1)][this.vertices.indexOf(v2)] !== 0;
```

Et, voici l'exemple complet avec des méthodes supplémentaires pour ajouter et supprimer une arête, vérifier s'il y a une arête entre deux sommets, et vérifier si un sommet spécifique est dans le graphe :

```typescript
class Graph {
  matrix: number[][];
  vertices: GraphVertex[];
  isDirected: boolean;

  constructor(vertices: GraphVertex[], isDirected = true) {
    this.vertices = vertices;
    this.matrix = Array.from({ length: vertices.length }, () => {
      return Array.from({ length: vertices.length }, () => 0)
    });
    this.isDirected = isDirected;
  }

  addEdge(v1: GraphVertex, v2: GraphVertex) {
    this._checkVertexIsInGraph(v1);
    this._checkVertexIsInGraph(v2);

    this.matrix[this.vertices.indexOf(v1)][this.vertices.indexOf(v2)] = 1;

    if (!this.isDirected) {
      this.matrix[this.vertices.indexOf(v2)][this.vertices.indexOf(v1)] = 1;
    }
  }

  /* 
  Pour un graphe pondéré :

  addEdge(v1: GraphVertex, v2: GraphVertex, weight: number) {
    this._checkVertexIsInGraph(v1);
    this._checkVertexIsInGraph(v2);

    this.matrix[this.vertices.indexOf(v1)][this.vertices.indexOf(v2)] = weight;
    if (!this.isDirected) {
      this.matrix[this.vertices.indexOf(v2)][this.vertices.indexOf(v1)] = weight;
    }
  }
  */

  removeEdge(v1: GraphVertex, v2: GraphVertex) {
    this._checkVertexIsInGraph(v1);
    this._checkVertexIsInGraph(v2);

    this.matrix[this.vertices.indexOf(v1)][this.vertices.indexOf(v2)] = 0;

    if (!this.isDirected) {
      this.matrix[this.vertices.indexOf(v2)][this.vertices.indexOf(v1)] = 0;
    }
  }

  hasEdge(v1: GraphVertex, v2: GraphVertex) {
    this._checkVertexIsInGraph(v1);
    this._checkVertexIsInGraph(v2);

    return this.matrix[this.vertices.indexOf(v1)][this.vertices.indexOf(v2)] !== 0;
  }

  getAdjacencyMatrix() {
    return this.matrix;
  }

  _checkVertexIsInGraph(v: GraphVertex) {
    if (!this.vertices.includes(v)) {
      throw new Error('Vertex doesn\'t exist');
    }
  }
}


let a = new GraphVertex('A');
let b = new GraphVertex('B');
let c = new GraphVertex('C');
let d = new GraphVertex('D');

let graph = new Graph([a, b, c, d], false);

graph.addEdge(a, b);
graph.addEdge(a, c);
graph.addEdge(b, c);
graph.addEdge(c, d);

console.log(graph.getAdjacencyMatrix());
// -> [ [0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0] ]
```

Les opérations sur une matrice d'adjacence ont une complexité temporelle de \\(O(1)\\). Mais nos besoins de stockage seront de \\(O(V^2)\\) où \\(V\\) est le nombre de sommets.

#### Liste d'Adjacence

Dans une liste d'adjacence, généralement une table de hachage **ou** un tableau de listes chaînées est utilisé. Par exemple :

```typescript
let graph = {
  'A': ['B', 'C'],
  'B': ['A', 'C'],
  'C': ['A', 'B', 'D'],
  'D': ['C']
}
```

Voyons comment nous pouvons modifier notre code ci-dessus pour utiliser une liste d'adjacence à la place.

Au lieu d'avoir une `matrix` qui est un tableau de tableaux, nous pouvons avoir une [`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) qui mappe les sommets à un tableau de leurs voisins.

Nous pouvons l'initialiser comme une map qui a les sommets comme clés, chacune ayant une valeur de tableau vide pour l'instant :

```typescript
this.list = new Map<GraphVertex, GraphVertex[]>();
for (const v of vertices) {
  this.list.set(v, []);
}
```

Ajouter une arête sera simplement pousser dans le tableau du sommet correspondant :

```typescript
this.list.get(v1)!.push(v2);
```

Si notre graphe est non orienté, nous pouvons le faire dans les deux sens ici aussi :

```typescript
if (!this.isDirected) {
  this.list.get(v2)!.push(v1);
}
```

Supprimer une arête sera supprimer ce sommet du tableau :

```typescript
this.list.set(v1, this.list.get(v1)!.filter(v => v !== v2));
```

Vérifier si une arête existe est simplement vérifier l'existence de ce sommet dans le tableau :

```typescript
this.list.get(v1)!.includes(v2);
```

**Note :** Nous utilisons un [opérateur d'affirmation non-null](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-assertion-operator) car nous utilisons TypeScript dans ces exemples. Comme nous le verrons ci-dessous, nous vérifions d'abord si le sommet est dans le graphe. Et puisque nous ajoutons tous les sommets du graphe comme clés à `this.list`, nous sommes sûrs que l'obtention de ce sommet à partir de la liste n'est pas `undefined`. Mais TypeScript nous avertira car si une clé n'est pas trouvée dans un objet `Map`, elle pourrait [potentiellement retourner `undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/get#return_value).

Voici notre graphe :

```typescript
class Graph {
  list: Map<GraphVertex, GraphVertex[]>;
  vertices: GraphVertex[];
  isDirected: boolean;

  constructor(vertices: GraphVertex[], isDirected = true) {
    this.vertices = vertices;
    this.list = new Map();
    for (const v of vertices) {
      this.list.set(v, []);
    }
    this.isDirected = isDirected;
  }

  addEdge(v1: GraphVertex, v2: GraphVertex) {
    this._checkVertexIsInGraph(v1);
    this._checkVertexIsInGraph(v2);

    this.list.get(v1)!.push(v2);
    
    if (!this.isDirected) {
      this.list.get(v2)!.push(v1);
    }
  }

  removeEdge(v1: GraphVertex, v2: GraphVertex) {
    this._checkVertexIsInGraph(v1);
    this._checkVertexIsInGraph(v2);

    this.list.set(v1, this.list.get(v1)!.filter(v => v !== v2));

    if (!this.isDirected) {
      this.list.set(v2, this.list.get(v2)!.filter(v => v !== v1));
    }
  }

  hasEdge(v1: GraphVertex, v2: GraphVertex) {
    this._checkVertexIsInGraph(v1);
    this._checkVertexIsInGraph(v2);

    return this.list.get(v1)!.includes(v2);
  }

  getAdjacencyList() {
    return this.list;
  }

  _checkVertexIsInGraph(v: GraphVertex) {
    if (!this.vertices.includes(v)) {
      throw new Error('Vertex doesn\'t exist');
    }
  }
}


let a = new GraphVertex('A');
let b = new GraphVertex('B');
let c = new GraphVertex('C');
let d = new GraphVertex('D');

let graph = new Graph([a, b, c, d], false);

graph.addEdge(a, b);
graph.addEdge(a, c);
graph.addEdge(b, c);
graph.addEdge(c, d);

console.log(graph.getAdjacencyList());

/* Output:

Map (4) {
  GraphVertex: { "value": "A" } => [
    GraphVertex: { "value": "B" }, 
    GraphVertex: { "value": "C" }
  ], 
  GraphVertex: { "value": "B" } => [
    GraphVertex: { "value": "A" }, 
    GraphVertex: { "value": "C" }
  ], 
  GraphVertex: { "value": "C" } => [
    GraphVertex: { "value": "A" }, 
    GraphVertex: { "value": "B" }, 
    GraphVertex: { "value": "D" }
  ], 
  GraphVertex: { "value": "D" } => [
    GraphVertex: { "value": "C" }
  ]
} 

*/
```

Obtenir les voisins d'un sommet est \\(O(1)\\) car nous cherchons simplement une clé dans une map. Mais trouver une arête particulière peut être \\(O(d)\\) où \\(d\\) est le nombre de degrés du sommet, car nous pourrions avoir besoin de parcourir tous les voisins pour la trouver. Et, cela pourrait être \\(V - 1\\) où \\(V\\) est le nombre de sommets dans le graphe. C'est le cas lorsque ce sommet a tous les autres sommets comme voisins.

La complexité spatiale peut être \\(O(V + E)\\) où \\(V\\) est le nombre de sommets et \\(E\\) est le nombre d'arêtes.

### Parcours

En continuant avec la représentation de la liste d'adjacence, examinons maintenant deux (très familières) façons de parcourir un graphe : la recherche en largeur d'abord et la recherche en profondeur d'abord.

Mais d'abord, nous allons modifier un peu notre graphe. Nous allons ajouter un nouveau sommet `'E'` et mettre à jour certaines arêtes :

```typescript
let a = new GraphVertex('A');
let b = new GraphVertex('B');
let c = new GraphVertex('C');
let d = new GraphVertex('D');
let e = new GraphVertex('E');


let graph = new Graph([a, b, c, d, e], false);

graph.addEdge(a, b);
graph.addEdge(a, c);
graph.addEdge(b, d);
graph.addEdge(c, e);
```

L'idée importante à retenir est qu'il n'y a pas de hiérarchie de sommets, donc nous n'avons pas de nœud racine.

Pour une recherche en largeur ou en profondeur, nous pouvons utiliser un nœud arbitraire comme point de départ.

#### Recherche en Largeur d'Abord

Avec notre nouveau graphe, un parcours de recherche en largeur d'abord ressemble à ceci :

![Visualisation animée pour une recherche en largeur d'abord d'un graphe avec les nœuds A, B, C, D, E avec les nœuds mis en évidence dans cet ordre : A, B, C, D, E.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747922399341/f4b9f63b-5188-48a2-83ec-51524721c2b1.gif align="center")

En ce qui concerne la recherche en largeur d'abord, une file d'attente est généralement utilisée, et l'idée est simple : étant donné un nœud actuel, nous ajouterons d'abord les nœuds adjacents, en les marquant comme visités au fur et à mesure.

À l'intérieur de la classe `Graph`, nous pouvons implémenter une méthode `bfs` qui fait exactement cela :

```typescript
bfs(startNode: GraphVertex) {
  const visited = new Set();
  const queue = [startNode];
  visited.add(startNode);

  while (queue.length > 0) {
    const currentNode = queue.shift();
    // console.log(currentNode);
    this.list.get(currentNode as GraphVertex)!.forEach((node) => {
      if (!visited.has(node)) {
        visited.add(node);
        queue.push(node);
      }
    });
  }
}
```

Si nous appelons la méthode `bfs` avec `a` comme sommet de départ (`graph.bfs(a)`), et que nous enregistrons `currentNode` dans la console à chaque fois que nous y allons, c'est comme nous l'attendions :

```plaintext
GraphVertex { value: 'A' }
GraphVertex { value: 'B' }
GraphVertex { value: 'C' }
GraphVertex { value: 'D' }
GraphVertex { value: 'E' }
```

Avec la liste d'adjacence, l'utilisation d'une BFS a une complexité temporelle de \\(O(V + E)\\) (somme des sommets et des arêtes) car nous parcourons tout le graphe.

#### Recherche en Profondeur d'Abord

Avec le même graphe modifié, une recherche en profondeur d'abord ressemble à ceci :

![Visualisation animée pour une recherche en profondeur d'abord d'un graphe avec les nœuds A, B, C, D, E avec les nœuds mis en évidence dans cet ordre : A, B, D, C, E.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747922463260/72e852c1-642f-4ce0-829d-e658a8a7b880.gif align="center")

Avec la recherche en profondeur d'abord, il y a généralement de la récursion impliquée car nous parcourons un chemin jusqu'à ce que nous ayons visité tous les nœuds de ce chemin. Une fois que nous atteignons une impasse, nous allons **revenir en arrière** et continuer à explorer jusqu'à ce que nous ayons visité tous les sommets du graphe.

Encore une fois, à l'intérieur de la classe `Graph`, nous pouvons ajouter une méthode `dfs` :

```typescript
dfs(startNode: GraphVertex, visited = new Set()) {
  visited.add(startNode);
  // console.log(startNode);
  this.list.get(startNode)!.forEach((node) => {
    if (!visited.has(node)) {
      this.dfs(node, visited);
    }
  });
}
```

En commençant par un nœud, nous vérifions jusqu'où nous pouvons aller à partir de là. Une fois que nous atteignons une impasse (lorsque le `dfs` à l'intérieur de `forEach` retourne), nous continuons à vérifier les autres voisins (avec `forEach`) jusqu'à ce qu'il n'en reste plus. Nous faisons essentiellement la même chose jusqu'à ce que tous les sommets soient visités.

L'enregistrement de la sortie correspond à notre attente :

```plaintext
GraphVertex { value: 'A' }
GraphVertex { value: 'B' }
GraphVertex { value: 'D' }
GraphVertex { value: 'C' }
GraphVertex { value: 'E' }
```

La complexité temporelle pour un parcours de recherche en profondeur d'un graphe est similaire à celle de la BFS, \\(O(V + E)\\).

## Chapitre Douze : Programmation Dynamique

La programmation dynamique (DP) est l'un de ces concepts qui peut sembler un peu intimidant lorsque vous l'entendez pour la première fois. Mais le point crucial est simplement de décomposer les problèmes en parties plus petites et de les résoudre. C'est aussi une question de stocker ces solutions afin de ne pas avoir à les calculer à nouveau.

Décomposer les problèmes en sous-problèmes n'est pas nouveau – c'est à peu près ce que la résolution de problèmes est tout entière. Ce que la programmation dynamique traite également spécifiquement, ce sont les **sous-problèmes qui se chevauchent** qui se répètent – nous voulons calculer les solutions à ces sous-problèmes afin de ne pas avoir à les calculer à nouveau chaque fois. En d'autres termes, *nous voulons nous souvenir du passé afin de ne pas être condamnés à le répéter*.

Par exemple, calculer 1 + 1 + 1 + 1 + 1 est très facile si nous avons déjà calculé 1 + 1 + 1 + 1. Nous pouvons simplement nous souvenir de la solution précédente, et l'utiliser :

![Visualisation animée du résultat de 1 + 1 + 1 + 1 constituant un sous-problème de 1 + 1 + 1 + 1 + 1 .](https://cdn.hashnode.com/res/hashnode/image/upload/v1747922611072/bcb33cae-aed3-41bd-8823-4e10a0e13fbf.gif align="center")

Le calcul de la suite de Fibonacci est l'un des exemples les plus connus lorsqu'il s'agit de programmation dynamique. Parce que nous devons calculer les mêmes fonctions chaque fois pour un nouveau nombre, cela se prête très bien à la DP.

Par exemple, pour calculer `fib(4)` nous devons calculer `fib(3)` et `fib(2)`. Mais calculer `fib(3)` implique également de calculer `fib(2)`, donc nous allons faire le même calcul, *encore*.

Une fonction Fibonacci classique, vieille et récursive pourrait ressembler à ceci :

```typescript
function fib(n: number): number {
  if (n === 0 || n === 1) {
    return n;
  }

  return fib(n - 1) + fib(n - 2);
}
```

Bien que le problème que nous avons mentionné subsiste : nous allons continuer à calculer les mêmes valeurs :

![Visualisation animée affichant des appels Fibonacci répétés.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747922659848/577aef57-17b5-40ad-a926-74387b0e3731.gif align="center")

Mais, nous voulons faire mieux.

La **mémoïsation** consiste à se souvenir des problèmes que nous avons déjà résolus afin de ne pas avoir à les résoudre à nouveau et de perdre notre temps. Nous pouvons *réutiliser* la solution au sous-problème que nous avons déjà mémoïsé. Donc, nous pouvons garder un *cache* pour stocker ces solutions et les utiliser :

```typescript
function fib(n: number, cache: Map<number, number>): number {
  if (cache.has(n)) {
    return cache.get(n)!;
  }

  if (n === 0 || n === 1) {
    return n;
  }

  const result = fib(n - 1, cache) + fib(n - 2, cache);
  cache.set(n, result);

  return result;
}
```

Par exemple, nous pouvons initialement passer une `Map` vide comme argument pour `cache`, et imprimer les 15 premiers nombres de Fibonacci :

```typescript
let m = new Map<number, number>();

for (let i = 0; i < 15; i++) {
  console.log(fib(i, m));
}

/*
  0
  1
  1
  2
  3
  5
  8
  13
  21
  34
  55 
  89
  144
  233
  377 
 */
```

Il existe deux approches différentes en programmation dynamique : **top-down** et **bottom-up**.

Le top-down est comme ce à quoi il ressemble : commencer par un grand problème, le décomposer en composants plus petits, les mémoriser. C'est ce que nous venons de faire avec l'exemple `fib`.

Le bottom-up est également comme ce à quoi il ressemble : commencer par le plus petit sous-problème, trouver une solution, et travailler notre chemin jusqu'au problème plus grand lui-même. Il a également un avantage : avec l'approche bottom-up, nous n'avons pas besoin de stocker chaque valeur précédente – nous pouvons seulement garder les deux éléments en bas afin de pouvoir les utiliser pour construire jusqu'à notre cible.

Avec l'approche bottom-up, notre fonction `fib` peut ressembler à ceci :

```typescript
function fib(n: number) {
  let dp = [0, 1];
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}
```

Notez simplement que nous conservons un tableau dont la taille croîtra linéairement à mesure que l'entrée augmente. Donc, nous pouvons faire mieux avec une complexité spatiale constante, sans utiliser de tableau du tout :

```typescript
function fib(n: number) {
  if (n === 0 || n === 1) {
    return n;
  }

  let a = 0;
  let b = 1;

  for (let i = 2; i <= n; i++) {
    let tmp = a + b;
    a = b;
    b = tmp;
  }

  return b;
}
```

#### Complexité temporelle et spatiale

Les complexités temporelles pour les approches top-down et bottom-up dans l'exemple de Fibonacci sont toutes deux \\(O(n)\\) car nous résolvons chaque sous-problème, chacun d'entre eux étant de temps constant.

**Note :** La complexité temporelle de la fonction récursive de Fibonacci qui n'utilise pas la DP est exponentielle (en fait, \\(O(\phi^{n})\\) – oui [le nombre d'or](https://en.wikipedia.org/wiki/Golden_ratio) comme base).

Mais en ce qui concerne la complexité spatiale, l'approche bottom-up (la deuxième version) est \\(O(1)\\).

**Note :** La première version que nous avons utilisée pour l'approche bottom-up a une complexité temporelle de \\(O(n)\\) car nous stockons les valeurs dans un tableau.

L'approche top-down a une complexité spatiale de \\(O(n)\\) car nous stockons une `Map` dont la taille croîtra linéairement à mesure que `n` augmente.

## Chapitre Treize : Intervalles

Un intervalle a simplement un début et une fin. La manière la plus facile de penser aux intervalles est comme des cadres temporels.

Avec les intervalles, la préoccupation habituelle est de savoir s'ils se chevauchent ou non.

Par exemple, si nous avons un intervalle `[1, 3]` et un autre `[2, 5]`, ils se chevauchent clairement, donc ils peuvent être fusionnés pour créer un nouvel intervalle `[1, 5]` :

![Visualisation animée avec l'intervalle [1, 3] fusionnant avec [2, 5], devenant [1, 5].](https://cdn.hashnode.com/res/hashnode/image/upload/v1747923034510/05767713-f24f-4467-82f5-89e025631be9.gif align="center")

Pour que deux intervalles **ne se chevauchent pas** :

* le *début* de l'un doit être *strictement plus grand* que la *fin* de l'autre
    

```plaintext
newInterval[0] > interval[1]
```

Ou :

* la *fin* de l'un doit être *strictement plus petite* que le *début* de l'autre
    

```plaintext
newInterval[1] < interval[0]
```

Si les deux sont faux, ils se chevauchent.

S'ils se chevauchent, le nouvel (fusionné) intervalle aura la valeur minimale des deux intervalles comme début, et la valeur maximale comme fin :

```plaintext
[
  min(newInterval[0], interval[0]),
  max(newInterval[1], interval[1])
]
```

## Chapitre Quatorze : Manipulation de Bits

[Une opération bit à bit](https://en.wikipedia.org/wiki/Bitwise_operation) opère sur une chaîne de bits, un tableau de bits, ou un nombre binaire (considéré comme une chaîne de bits) au niveau de ses bits individuels.

Représentons d'abord un nombre en binaire (base 2). Nous pouvons utiliser la méthode `toString` sur un [nombre](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number), et spécifier la **base** :

```javascript
const n = 17;

console.log(n.toString(2)); // 10001
```

Nous pouvons également analyser un entier en lui donnant une base :

```javascript
console.log(parseInt(10001, 2)); // 17
```

**Note :** Nous pouvons également représenter un nombre binaire avec le préfixe `0b` :

```javascript
console.log(0b10001); // 17
console.log(0b101); // 5
```

Par exemple, ce sont les mêmes nombres :

```javascript
0b1 === 0b00000001 // true
```

Toutes les opérations bit à bit sont effectuées sur des nombres binaires de 32 bits en JavaScript. C'est-à-dire, *avant qu'une opération bit à bit ne soit effectuée, JavaScript convertit les nombres en entiers signés de 32 bits*.

Ainsi, par exemple, `17` ne sera pas simplement `10001` mais `00000000 00000000 00000000 00010001`.

*Après que l'opération bit à bit soit effectuée, le résultat est reconverti en nombres JavaScript de 64 bits.*

### Opérateurs Bit à Bit

#### ET (`&`)

Si deux bits sont `1`, le résultat est `1`, sinon `0`.

Les GIFs ci-dessous montrent les nombres comme des chaînes de 8 bits, mais lors de l'exécution d'opérations bit à bit, rappelez-vous qu'ils sont convertis en nombres de 32 bits.

![Visualisation animée d'une opération ET. 00010001 & 00000101 = 00000001.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747923324409/4415a01f-6129-4dcf-a1ce-b8e898bdba9a.gif align="center")

```javascript
const x1 = 0b10001;
const x2 = 0b101;

const result = x1 & x2; // 1 (0b1)
```

#### OU (`|`)

Si l'un des bits est `1`, le résultat est `1`, sinon `0`.

![Visualisation animée d'une opération OU. 00010001 | 00000101 = 00010101.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747923365941/22e562c4-e195-4567-b8ef-4b94cb4a394f.gif align="center")

```javascript
const x1 = 0b10001;
const x2 = 0b101;

const result = x1 | x2; // 21 (0b10101)
```

#### XOR (`^`)

Si les bits sont différents (l'un est `1` et l'autre est `0`), le résultat est `1`, sinon `0`.

![Visualisation animée d'une opération XOR. 00010001 ^ 00000101 = 00010100.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747923403151/52090e1a-98ee-4303-a433-6318ec6f18d2.gif align="center")

```javascript
const x1 = 0b10001;
const x2 = 0b101;

const result = x1 ^ x2; // 20 (0b10100)
```

#### NON (`~`)

Inverse les bits (`1` devient `0`, `0` devient `1`).

![Visualisation animée d'une opération NON. ~00010001 = 11101110.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747923458432/2807b821-8069-45e6-a37b-d8167ec722e7.gif align="center")

```javascript
const n = 17;

const result = ~n; // -18
```

**Note :** Le NON bit à bit de n'importe quel entier 32 bits `x` donne `-(x + 1)`.

Si nous utilisons [une fonction d'aide](https://stackoverflow.com/a/33758875) pour voir les représentations binaires, c'est comme nous l'attendions :

```javascript
console.log(createBinaryString(n));
// -> 00000000 00000000 00000000 00010001

console.log(createBinaryString(result));
// -> 11111111 11111111 11111111 11101110
```

Le bit le plus à gauche indique le signe – si le nombre est négatif ou positif.

Rappelons que nous avons dit que JavaScript utilise des entiers **signés** de 32 bits pour les opérations bit à bit. **Le bit le plus à gauche est** `1` pour les nombres négatifs et `0` pour les nombres positifs. De plus, l'opérateur fonctionne sur les représentations binaires des opérandes en [complément à deux](https://en.wikipedia.org/wiki/Two's_complement). L'opérateur est appliqué à chaque bit, et le résultat est construit bit par bit.

**Note :** Le complément à deux nous permet d'obtenir un nombre avec un signe inverse. Une façon de le faire est d'inverser les bits du nombre dans la représentation positive et d'ajouter 1 :

```javascript
function twosComplement(n) {
  return ~n + 0b1;
}
```

#### Déplacement à Gauche (remplissage zéro) (`<<`)

Décale le nombre donné de bits vers la gauche, en ajoutant des bits zéro décalés depuis la droite.

```javascript
const n = 17;
const result = n << 1; // 34


console.log(createBinaryString(17));
// -> 00000000 00000000 00000000 00010001

console.log(createBinaryString(34));
// -> 00000000 00000000 00000000 00100010
```

**Notez** que le 32ème bit (le plus à gauche) est abandonné.

#### Déplacement à Droite (conservation du signe) (`>>`)

Décale le nombre donné de bits vers la droite, en conservant le signe lors de l'ajout de bits depuis la gauche.

```javascript
const n = 17;
const result = n >> 1; // 8


console.log(createBinaryString(17));
// -> 00000000 00000000 00000000 00010001

console.log(createBinaryString(8));
// -> 00000000 00000000 00000000 00001000
```

```javascript
const n = -17;
const result = n >> 1; // -9

console.log(createBinaryString(-17));
// -> 11111111 11111111 11111111 11101111

console.log(createBinaryString(-9));
// -> 11111111 11111111 11111111 11110111
```

#### Déplacement à Droite (non signé) (`>>>`)

Décale le nombre donné de bits vers la droite, en ajoutant des `0` lors de l'ajout de bits depuis la gauche, peu importe le signe.

```javascript
const n = 17;
const result = n >>> 1; // 8


console.log(createBinaryString(17));
// -> 00000000 00000000 00000000 00010001

console.log(createBinaryString(8));
// -> 00000000 00000000 00000000 00001000
```

```javascript
const n = -17;
const result = n >>> 1; // 2147483639

console.log(createBinaryString(-17));
// -> 11111111 11111111 11111111 11101111

console.log(createBinaryString(2147483639));
// -> 01111111 11111111 11111111 11110111
```

### Obtenir un Bit

Pour obtenir un bit spécifique, nous devons d'abord créer un **masque de bits**. Nous pouvons le faire en décalant `1` vers la gauche par l'index du bit que nous voulons obtenir. Le résultat est le **ET** du nombre binaire et du masque de bits.

Mais en utilisant JavaScript, nous pouvons également faire un décalage à droite non signé par l'index pour mettre le bit à la première place (afin que nous n'obtenions pas la valeur réelle qui se trouve à cette position, mais si elle est un `1` ou un `0`) :

```javascript
function getBit(number, idx) {
  const bitMask = 1 << idx;
  const result = number & bitMask;

  return result >>> idx;
}
```

Par exemple, essayons `13`, qui est `1101` en binaire :

```javascript
const binaryNumber = 0b1101;

console.log('Bit at position 0:', getBit(binaryNumber, 0));
console.log('Bit at position 1:', getBit(binaryNumber, 1));
console.log('Bit at position 2:', getBit(binaryNumber, 2));
console.log('Bit at position 3:', getBit(binaryNumber, 3));

/*
Output:

Bit at position 0: 1
Bit at position 1: 0
Bit at position 2: 1
Bit at position 3: 1
*/
```

### Définir un Bit

Si nous voulons mettre un bit à `1` (en d'autres termes, pour "*définir un bit*"), nous pouvons faire une chose similaire.

Tout d'abord, nous pouvons créer un masque de bits à nouveau en décalant `1` vers la gauche par l'index du bit que nous voulons mettre à `1`. Le résultat est le **OU** du nombre et du masque de bits :

```javascript
function setBit(number, idx) {
  const bitMask = 1 << idx;
  return number | bitMask;    
}
```

Rappelons que dans notre exemple `13` était `1101` en binaire, disons que nous voulons mettre le `0` à l'index 1 :

```javascript
const binaryNumber = 0b1101;
const newBinaryNumber = setBit(binaryNumber, 1);

console.log(createBinaryString(newBinaryNumber));
// -> 00000000 00000000 00000000 00001111

console.log('Bit at position 1:', getBit(newBinaryNumber, 1));
// -> Bit at position 1: 1
```

## Conclusion

Avec quelques détours ici et là, nous avons examiné quatorze (ou quinze, si vous comptez notre *interlude*) concepts différents, des tableaux et du hachage à la manipulation de bits.

Bien que je doive dire qu'avec le temps, il est facile d'oublier tout ce que nous avons appris. Mais, ce n'est pas un problème en soi, car comme vous l'avez peut-être réalisé, s'il y a une idée qui devrait rester avec vous avec ce guide, c'est que les problèmes sont mieux résolus lorsqu'ils sont décomposés en parties plus petites. Et, comme pour tout le reste, écrire ou parler à soi-même (voir [le débogage du canard](https://www.freecodecamp.org/news/rubber-duck-debugging/)) fait des miracles.

Maintenant, il est temps de prendre une profonde inspiration.

C'était une aventure délicieuse d'explorer les structures de données et les algorithmes, et espérons que vous y avez trouvé une certaine valeur.

Ayez un beau voyage devant vous, et jusqu'à alors, bon codage.

### Ressources & Crédits

Ce guide a été principalement inspiré par la série incroyable [BaseCS](https://medium.com/basecs) de Vaidehi Joshi, qui est une ressource incroyable pour apprendre les concepts de base de l'informatique.

L'idée de visualisation a été inspirée par la série [JavaScript Visualized](https://dev.to/lydiahallie/series/3341) de Lydia Hallie.

Bien sûr, vous pouvez également consulter les [cours de NeetCode](https://neetcode.io/courses) qui peuvent être incroyablement utiles pour une étude sérieuse.

Il existe de nombreuses autres ressources à consulter si vous souhaitez aller plus loin, en voici quelques-unes que j'ai utilisées dans notre exploration :

* [brilliant.org](http://brilliant.org)
    
* [leetcodethehardway.com](http://leetcodethehardway.com)
    
* [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
    
* [baeldung.com/cs](http://baeldung.com/cs)
    
* [*The Absolute Essentials for Bit Manipulation in JavaScript* par Lucas F. Costa](https://lucasfcosta.com/2018/12/25/bitwise-operations.html)
    
* [Heap & HeapSort - Noriko Tomuro](https://condor.depaul.edu/ntomuro/courses/402/notes/heap.html)
    
* [Heaps - Professor Reva Freedman](https://faculty.cs.niu.edu/~freedman/340/340notes/340heap.htm)
    
* ["Using `collections.deque` to Create a Python Stack" - Jim Anderson](https://realpython.com/how-to-implement-python-stack/#using-collectionsdeque-to-create-a-python-stack)