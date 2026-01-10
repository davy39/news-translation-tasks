---
title: 'La récursivité n''est pas difficile : un guide étape par étape de cette technique
  de programmation utile'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:18:29.000Z'
originalURL: https://freecodecamp.org/news/recursion-is-not-hard-858a48830d83
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VtrFuLn-4TnmFVDD8G3pxQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 'La récursivité n''est pas difficile : un guide étape par étape de cette
  technique de programmation utile'
seo_desc: 'By Kevin Turney

  I’m going to say this right off the bat. Do you know the events that happen upon
  function invocation? No? Then that’s where we will start.

  Function invocation

  When we call a function, an execution context gets placed on the execution ...'
---

Par Kevin Turney

Je vais le dire tout de suite. Connaissez-vous les événements qui se produisent lors de l'invocation d'une fonction ? Non ? Alors c'est par là que nous allons commencer.

#### Invocation de fonction

Lorsque nous appelons une fonction, un contexte d'exécution est placé sur la pile d'exécution. Décomposons cela un peu plus.

Tout d'abord, qu'est-ce qu'une pile ?

Une pile est une structure de données qui fonctionne sur une base "Dernier entré, premier sorti". Un élément est "poussé" sur une pile pour l'ajouter, et un élément est "retiré" de la pile pour le supprimer.

Utiliser une pile est une méthode d'ordonnancement de certaines opérations pour l'exécution.

Maintenant, revenons à ce qu'est un contexte d'exécution ? Un contexte d'exécution se forme lors de l'invocation d'une fonction. Ce contexte se place sur une pile d'exécution, un ordre d'opérations. L'élément qui est toujours le premier dans cette pile est le contexte d'exécution global. Ensuite viennent les contextes créés par les fonctions.

Ces contextes d'exécution ont des propriétés, un objet d'activation et une liaison "this". La liaison "this" est une référence à ce contexte d'exécution. L'objet d'activation comprend : les paramètres passés, les variables déclarées et les déclarations de fonctions.

Ainsi, chaque fois que nous plaçons un nouveau contexte sur la pile, nous avons généralement tout ce dont nous avons besoin pour exécuter le code.

Pourquoi dis-je _généralement_ ?

Avec la récursivité, nous attendons des valeurs de retour provenant d'autres contextes d'exécution. Ces autres contextes sont plus haut dans la pile. Lorsque le dernier élément de la pile termine son exécution, ce contexte génère une valeur de retour. Cette valeur de retour est transmise comme valeur de retour du cas récursif à l'élément suivant. Ce contexte d'exécution est ensuite retiré de la pile.

#### Récursivité

Alors, qu'est-ce que la récursivité ?

Une fonction récursive est une fonction qui s'appelle elle-même jusqu'à ce qu'une "condition de base" soit vraie, et l'exécution s'arrête.

Tant que la condition est fausse, nous continuerons à placer des contextes d'exécution au sommet de la pile. Cela peut se produire jusqu'à ce que nous ayons un "débordement de pile". Un débordement de pile se produit lorsque nous n'avons plus de mémoire pour contenir les éléments dans la pile.

![Image](https://cdn-media-1.freecodecamp.org/images/yEbQk71bUba6KLDWGXuamXQlntQU4mkFaoO4)

En général, une fonction récursive a au moins deux parties : une condition de base et au moins un cas récursif.

Regardons un exemple classique.

#### Factorielle

```
const factorial = function(num) {  debugger;  if (num === 0 || num === 1) {    return 1  } else {    return num * factorial(num - 1)  }}
```

```
factorial(5)
```

Ici, nous essayons de trouver 5! (cinq factorielle). La [fonction factorielle](http://mathworld.wolfram.com/Factorial.html) est définie comme le produit de tous les entiers positifs inférieurs ou égaux à son argument.

La première condition stipule : "si le paramètre passé est égal à 0 ou 1, nous allons sortir et retourner 1".

Ensuite, le cas récursif stipule :

"Si le paramètre n'est pas 0 ou 1, alors nous allons passer la valeur de `num` fois la valeur de retour de l'appel de cette fonction à nouveau avec `num-1` comme argument".

Ainsi, si nous appelons `factorial(0)`, la fonction retourne 1 et n'atteint jamais le cas récursif.

Il en va de même pour `factorial(1)`.

Nous pouvons voir ce qui se passe si nous insérons une instruction de débogage dans le code et utilisons les outils de développement pour parcourir et observer la pile d'appels.

1. La pile d'exécution place `factorial()` avec 5 comme argument passé. Le cas de base est faux, donc entrez dans la condition récursive.
2. La pile d'exécution place `factorial()` une deuxième fois avec `num-1` = 4 comme argument. Le cas de base est faux, entrez dans la condition récursive.
3. La pile d'exécution place `factorial()` une troisième fois avec `num-1` (4-1) = 3 comme argument. Le cas de base est faux, entrez dans la condition récursive.
4. La pile d'exécution place `factorial()` une quatrième fois avec `num-1`(3-1) = 2 comme argument. Le cas de base est faux, entrez dans la condition récursive.
5. La pile d'exécution place `factorial()` une cinquième fois avec `num-1` (2-1) = 1 comme argument. Maintenant, le cas de base est vrai, donc retourne 1.

À ce stade, nous avons diminué l'argument de un à chaque appel de fonction jusqu'à ce que nous atteignions une condition pour retourner 1.

6. À partir de là, le dernier contexte d'exécution se termine, `num === 1`, donc cette fonction retourne 1.

7. Ensuite, `num === 2`, donc la valeur de retour est 2. (1×2).

8. Ensuite, `num === 3`, donc la valeur de retour est 6, (2×3).

Jusqu'à présent, nous avons 1×2×3.

9. Ensuite, `num === 4`, (4×6). 24 est la valeur de retour au contexte suivant.

10. Enfin, `num === 5`, (5×24) et nous avons 120 comme valeur finale.

![Image](https://cdn-media-1.freecodecamp.org/images/KioR-yl8aB2lxriDCulsNMTivQ1J5xlmEyrg)

La récursivité est assez géniale, n'est-ce pas ?

Nous aurions pu faire la même chose avec une boucle for ou while. Mais utiliser la récursivité donne une solution élégante qui est plus lisible.

C'est pourquoi nous utilisons des solutions récursives.

De nombreuses fois, un problème décomposé en parties plus petites est plus efficace. Diviser un problème en parties plus petites aide à le résoudre. Ainsi, la récursivité est une approche de type "diviser pour régner" pour résoudre les problèmes.

* Les sous-problèmes sont plus faciles à résoudre que le problème original
* Les solutions aux sous-problèmes sont combinées pour résoudre le problème original

Le "diviser pour régner" est le plus souvent utilisé pour parcourir ou rechercher des structures de données telles que les arbres de recherche binaire, les graphes et les tas. Il fonctionne également pour de nombreux algorithmes de tri, comme [quicksort](https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort) et [heapsort](https://www.geeksforgeeks.org/heap-sort/).

Travaillons à travers les exemples suivants. Utilisez les outils de développement pour obtenir une compréhension conceptuelle de ce qui se passe où et quand. N'oubliez pas d'utiliser des instructions de débogage et de parcourir chaque processus.

#### Fibonacci

```
const fibonacci = function(num) {  if (num <= 1) {    return num  } else {    return fibonacci(num - 1) + fibonacci(num - 2)  }}fibonacci(5);
```

#### Tableaux récursifs

```
function flatten(arr) {  var result = []  arr.forEach(function(element) {    if (!Array.isArray(element)) {      result.push(element)    } else {      result = result.concat(flatten(element))    }  })  return result}
```

```
flatten([1, [2], [3, [[4]]]]);
```

#### Inverser une chaîne

```
function reverse(str) {  if (str.length === 0) return ''  return str[str.length - 1] + reverse(str.substr(0, str.length - 1))}
```

```
reverse('abcdefg');
```

#### Quicksort

```
function quickSort(arr, lo, hi) {  if (lo === undefined) lo = 0  if (hi === undefined) hi = arr.length - 1
```

```
  if (lo < hi) {    // partitionner le tableau    var p = partition(arr, lo, hi)    console.log('partition de, ' + lo + ' à ' + hi + '=> partition: ' + p)    // trier les sous-tableaux    quickSort(arr, lo, p - 1)    quickSort(arr, p + 1, hi)  }  // pour l'appel initial, retourner un tableau trié  if (hi - lo === arr.length - 1) return arr}
```

```
function partition(arr, lo, hi) {  // choisir le dernier élément comme pivot  var pivot = arr[hi]  // garder une trace de l'index pour placer le pivot  var pivotLocation = lo  // parcourir le sous-tableau et si l'élément <= pivot, placer l'élément avant le pivot  for (var i = lo; i < hi; i++) {    if (arr[i] <= pivot) {      swap(arr, pivotLocation, i)      pivotLocation++    }  }  swap(arr, pivotLocation, hi)  return pivotLocation}
```

```
function swap(arr, index1, index2) {  if (index1 === index2) return  var temp = arr[index1]  arr[index1] = arr[index2]  arr[index2] = temp  console.log('échangé' + arr[index1], arr[index2], +' dans ', arr)  return arr}
```

```
quickSort([1, 4, 3, 56, 9, 8, 7, 5])
```

Pratiquer les techniques récursives est important. Pour les structures de données imbriquées comme les arbres, les graphes et les tas, la récursivité est inestimable.

Dans un futur article, je discuterai de l'optimisation de l'appel terminal et des techniques de mémoisation en relation avec la récursivité. Merci pour la lecture !

#### Ressources supplémentaires

[Wikipedia](https://en.wikipedia.org/wiki/Recursion)

[Software Engineering](https://softwareengineering.stackexchange.com/questions/25052/in-plain-english-what-is-recursion)

[Un autre bon article](https://www.topcoder.com/community/data-science/data-science-tutorials/an-introduction-to-recursion-part-2/)

[M.I.T. open courseware](http://web.mit.edu/6.005/www/fa15/classes/10-recursion/)