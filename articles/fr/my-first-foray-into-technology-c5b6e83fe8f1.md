---
title: Guide des débutants pour la notation Big O
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-10-12T21:30:43.000Z'
originalURL: https://freecodecamp.org/news/my-first-foray-into-technology-c5b6e83fe8f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HwLR-DKk0lYNEMpkH475kg.png
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Guide des débutants pour la notation Big O
seo_desc: 'By Festus K. Yangani

  Big O Notation is a way to represent how long an algorithm will take to execute.
  It enables a software Engineer to determine how efficient different approaches to
  solving a problem are.

  Here are some common types of time complexi...'
---

Par Festus K. Yangani

**La notation Big O est une manière de représenter combien de temps un algorithme mettra à s'exécuter.** Elle permet à un ingénieur logiciel de déterminer l'efficacité de différentes approches pour résoudre un problème.

Voici quelques types courants de complexités temporelles en notation Big O.

* O(1) - Complexité temporelle constante
* O(n) - Complexité temporelle linéaire
* O(log n) - Complexité temporelle logarithmique
* O(n^2) - Complexité temporelle quadratique

Espérons qu'à la fin de cet article, vous serez en mesure de comprendre les bases de la notation Big O.

#### O(1) — Temps constant

Les algorithmes à temps constant prendront toujours le même temps pour s'exécuter. Le temps d'exécution de ces algorithmes est indépendant de la taille de l'entrée. Un bon exemple de temps O(1) est l'accès à une valeur avec un index de tableau.

```
var arr = [ 1,2,3,4,5];
```

```
arr[2]; // => 3
```

D'autres exemples incluent : les opérations push() et pop() sur un tableau.

#### O(n) - Complexité temporelle linéaire

Un algorithme a une complexité temporelle linéaire si le temps nécessaire pour exécuter l'algorithme est directement proportionnel à la taille de l'entrée _n_. Par conséquent, le temps nécessaire pour exécuter l'algorithme augmentera proportionnellement à mesure que la taille de l'entrée _n_ augmente.

Un bon exemple est la recherche d'un CD dans une pile de CDs ou la lecture d'un livre, où n est le nombre de pages.

Exemples de O(n) en utilisant la recherche linéaire :

```
//si nous utilisons une boucle for pour imprimer les valeurs des tableaux
```

```
for (var i = 0; i < array.length; i++) {  console.log(array[i]);}
```

```
var arr1 = [orange, apple, banana, lemon]; //=> 4 étapes
```

```
var arr2 = [apple, htc,samsung, sony, motorola]; //=> 5 étapes
```

#### O(log n) - Complexité temporelle logarithmique

Un algorithme a une complexité temporelle logarithmique si le temps nécessaire pour exécuter l'algorithme est proportionnel au logarithme de la taille de l'entrée _n_. Un exemple est la recherche binaire, souvent utilisée pour rechercher des ensembles de données :

```
//Implémentation de la recherche binaire
var doSearch = function(array, targetValue) {    var minIndex = 0;    var maxIndex = array.length - 1;    var currentIndex;    var currentElement;        while (minIndex <= maxIndex) {        currentIndex = (minIndex + maxIndex) / 2 | 0;        currentElement = array[currentIndex];        if (currentElement < targetValue) {            minIndex = currentIndex + 1;        } else if (currentElement > targetValue) {            maxIndex = currentIndex - 1;        } else {            return currentIndex;        }    }    return -1;  //Si l'index de l'élément n'est pas trouvé.};
```

```
var numbers = [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33];
```

```
doSearch(numbers, 23) //=>; 6
```

D'autres exemples de complexité temporelle logarithmique incluent :

```
Exemple 1;
```

```
for (var i = 1; i < n; i = i * 2)  console.log(i);}
```

```
Exemple 2;
```

```
for (i = n; i >= 1; i = i/2) console.log(i);}
```

#### O(n^2) - Complexité temporelle quadratique

Un algorithme a une complexité temporelle quadratique si le temps nécessaire pour l'exécuter est proportionnel au carré de la taille de l'entrée. Un bon exemple est la vérification de la présence de doublons dans un jeu de cartes.

Vous rencontrerez une complexité temporelle quadratique dans les algorithmes impliquant des itérations imbriquées, telles que des boucles _for_ imbriquées. En fait, des boucles plus profondément imbriquées entraîneront des complexités _O(n^3), O(n^4), etc._

```
for(var i = 0; i < length; i++) {     //a une complexité temporelle O(n)    for(var j = 0; j < length; j++) { //a une complexité temporelle O(n^2)      // Plus de boucles ?    }}
```

D'autres exemples de complexité temporelle quadratique incluent le tri à bulles, le tri par sélection et le tri par insertion.

Cet article ne fait qu'effleurer la surface de la notation Big O. Si vous souhaitez en savoir plus sur la notation Big O, je vous recommande de consulter le [Big-O Cheat Sheet](http://bigocheatsheet.com/).