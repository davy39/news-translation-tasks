---
title: Trois façons de trouver le plus grand nombre dans un tableau en utilisant JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-10-17T18:00:48.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LSH8HhFM40_2KWWOzhqPhg.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Trois façons de trouver le plus grand nombre dans un tableau en utilisant
  JavaScript
seo_desc: 'In this article, I’m going to explain how to solve Free Code Camp’s “Return
  Largest Numbers in Arrays” challenge. This involves returning an array with the
  largest numbers from each of the sub arrays.

  There are the three approaches I’ll cover:


  with ...'
---

Dans cet article, je vais expliquer comment résoudre le défi de Free Code Camp « [Return Largest Numbers in Arrays](https://www.freecodecamp.com/challenges/return-largest-numbers-in-arrays) ». Cela implique de retourner un tableau avec les plus grands nombres de chacun des sous-tableaux.

Voici les trois approches que je vais couvrir :

1. avec une boucle FOR
2. en utilisant la méthode reduce()
3. en utilisant Math.max()

#### Description du défi algorithmique

> Retournez un tableau composé du plus grand nombre de chaque sous-tableau fourni. Pour simplifier, le tableau fourni contiendra exactement 4 sous-tableaux.  
>   
> N'oubliez pas que vous pouvez parcourir un tableau avec une simple boucle for et accéder à chaque élément avec la syntaxe de tableau arr[i].

```js
function largestOfFour(arr) {
  return arr;
}
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);

```

#### Cas de test fournis

```
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]) devrait retourner un tableau.

largestOfFour([[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]) devrait retourner [27,5,39,1001].

largestOfFour([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]) devrait retourner [9, 35, 97, 1000000].
```

### **Approche #1 : Retourner les plus grands nombres dans un tableau avec une boucle For**

Voici ma solution, avec des commentaires intégrés pour vous aider à la comprendre :

```js

function largestOfFour(arr) {
   // Étape 1. Créer un tableau qui hébergera le résultat des 4 sous-tableaux
   var largestNumber = [0,0,0,0];
 
   // Étape 2. Créer la première boucle FOR qui parcourra les tableaux
   for(var arrayIndex = 0; arrayIndex < arr.length; arrayIndex++) {
   /* Le point de départ, index 0, correspond au premier tableau */
 
    // Étape 3. Créer la deuxième boucle FOR qui parcourra les sous-tableaux
    for(var subArrayIndex = 0; subArrayIndex < arr[arrayIndex].length; subArrayIndex++) {
    /* Le point de départ, index 0, correspond au premier sous-tableau */
       
       if(arr[arrayIndex][subArrayIndex] > largestNumber[arrayIndex]) {
          
          largestNumber[arrayIndex] = arr[arrayIndex][subArrayIndex];
          
       /* Cycles de la boucle FOR
          arrayIndex => i
          subArrayIndex => j
          
       Itération dans le premier tableau
          Pour chaque itération : arr[i][j]           largestNumber[i]          si arr[i][j] > largestNumber[i]?     alors largestNumber[i] = arr[i][j]
          Première itération :    arr[0][0] => 4      largestNumber[0] => 0     4 > 0? => VRAI                       alors largestNumber[0] = 4
          Deuxième itération :   arr[0][1] => 5      largestNumber[0] => 4     5 > 4? => VRAI                       alors largestNumber[0] = 5
          Troisième itération :    arr[0][2] => 1      largestNumber[0] => 5     1 > 5? => FAUX                      alors largestNumber[0] = 5
          Quatrième itération :   arr[0][3] => 3      largestNumber[0] => 5     3 > 5? => FAUX                      alors largestNumber[0] = 5
          Cinquième itération :    arr[0][4] => FAUX  largestNumber[0] => 5                                          largestNumber = [5,0,0,0]
       Sortir du premier tableau et continuer sur le deuxième
       Itération dans le deuxième tableau
          Pour chaque itération : arr[i][j]            largestNumber[i]           si arr[i][j] > largestNumber[i]?     alors largestNumber[i] = arr[i][j]
          Première itération :    arr[1][0] => 13      largestNumber[1] => 0      13 > 0? => VRAI                      alors largestNumber[1] = 13
          Deuxième itération :   arr[1][1] => 27      largestNumber[1] => 13     27 > 13? => VRAI                     alors largestNumber[1] = 27
          Troisième itération :    arr[1][2] => 18      largestNumber[1] => 27     18 > 27? => FAUX                    alors largestNumber[1] = 27
          Quatrième itération :   arr[1][3] => 26      largestNumber[1] => 27     26 > 27? => FAUX                    alors largestNumber[1] = 27
          Cinquième itération :    arr[1][4] => FAUX   largestNumber[1] => 27                                          largestNumber = [5,27,0,0]
       Sortir du premier tableau et continuer sur le troisième
       Itération dans le troisième tableau
          Pour chaque itération : arr[i][j]            largestNumber[i]           si arr[i][j] > largestNumber[i]?     alors largestNumber[i] = arr[i][j]
          Première itération :    arr[2][0] => 32      largestNumber[2] => 0      32 > 0? => VRAI                      alors largestNumber[2] = 32
          Deuxième itération :   arr[2][1] => 35      largestNumber[2] => 32     35 > 32? => VRAI                     alors largestNumber[2] = 35
          Troisième itération :    arr[2][2] => 37      largestNumber[2] => 35     37 > 35? => VRAI                     alors largestNumber[2] = 37
          Quatrième itération :   arr[2][3] => 39      largestNumber[2] => 37     39 > 37? => VRAI                     alors largestNumber[2] = 39
          Cinquième itération :    arr[2][4] => FAUX   largestNumber[2] => 39                                          largestNumber = [5,27,39,0]
       Sortir du premier tableau et continuer sur le quatrième
       Itération dans le quatrième tableau
          Pour chaque itération : arr[i][j]            largestNumber[i]           si arr[i][j] > largestNumber[i]?     alors largestNumber[i] = arr[i][j]
          Première itération :    arr[3][0] => 1000    largestNumber[3] => 0      1000 > 0? => VRAI                    alors largestNumber[3] = 1000
          Deuxième itération :   arr[3][1] => 1001    largestNumber[3] => 1000   1001 > 1000? => VRAI                 alors largestNumber[3] = 1001
          Troisième itération :    arr[3][2] => 857     largestNumber[3] => 1001   857 > 1001? => FAUX                 alors largestNumber[3] = 1001
          Quatrième itération :   arr[3][3] => 1       largestNumber[3] => 1001   1 > 1001? => FAUX                   alors largestNumber[3] = 1001
          Cinquième itération :    arr[3][4] => FAUX   largestNumber[3] => 1001                                        largestNumber = [5,27,39,1001]
       Sortir de la boucle FOR */
        }
    }
 }
 // Étape 4. Retourner les plus grands nombres de chaque sous-tableau
 return largestNumber; // largestNumber = [5,27,39,1001];
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

Et voici la version sans mes commentaires :

```js

function largestOfFour(arr) {
   var largestNumber = [0,0,0,0];
   for(var arrayIndex = 0; arrayIndex < arr.length; arrayIndex++) {
    for(var subArrayIndex = 0; subArrayIndex < arr[arrayIndex].length; subArrayIndex++) {
       if(arr[arrayIndex][subArrayIndex] > largestNumber[arrayIndex]) {         
          largestNumber[arrayIndex] = arr[arrayIndex][subArrayIndex];
        }
    }
 }
 return largestNumber;
}
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

### Approche #2 : Retourner les plus grands nombres dans un tableau avec des fonctions intégrées — avec map() et reduce()

Pour cette solution, vous utiliserez deux méthodes : la méthode Array.prototype.map() et la méthode Array.prototype.reduce().

* La méthode **map()** crée un nouveau tableau avec les résultats de l'appel d'une fonction fournie sur chaque élément de ce tableau. L'utilisation de map appellera une fonction de rappel fournie une fois pour chaque élément dans un tableau, dans l'ordre, et construira un nouveau tableau à partir des résultats.
* La méthode **reduce()** applique une fonction contre un accumulateur et chaque valeur du tableau pour le réduire à une seule valeur.

L'**opérateur ternaire** est le seul opérateur JavaScript qui prend trois opérandes. Cet opérateur est utilisé comme raccourci pour l'instruction if.

```
(currentLargestNumber > previousLargestNumber) ? currentLargestNumber : previousLargestNumber;
```

Cela peut aussi se lire comme :

```
if (currentLargestNumber > previousLargestNumber == true) {
    return currentLargestNumber;
} else {
    return previousLargestNumber;
}
```

Voici ma solution, avec des commentaires intégrés :

```js

function largestOfFour(mainArray) {
  // Étape 1. Map sur les tableaux principaux
  return mainArray.map(function (subArray){ // Étape 3. Retourner les plus grands nombres de chaque sous-tableau => retourne [5,27,39,1001]

    // Étape 2. Prendre les plus grands nombres pour chaque sous-tableau avec la méthode reduce()
    return subArray.reduce(function (previousLargestNumber, currentLargestNumber) {

      return (currentLargestNumber > previousLargestNumber) ? currentLargestNumber : previousLargestNumber;

      /* Processus de map et cycles de la méthode Reduce
      currentLargestNumber => cLN
      previousLargestNumber => pLN
      Itération dans le premier tableau
          Pour chaque itération :     cLN         pLN       si (cLN > pLN) ?        alors cLN        sinon pLN
          Première itération :         4           0        4 > 0? => VRAI              4             /
          Deuxième itération :        5           4        5 > 4? => VRAI              5             /
          Troisième itération :         1           5        1 > 5? => FAUX             /             5
          Quatrième itération :        3           5        3 > 5? => FAUX             /             5
          Cinquième itération :         /           5                                               retourne 5
       Sortir du premier tableau et continuer sur le deuxième
      Itération dans le deuxième tableau
        Pour chaque itération :     cLN         pLN       si (cLN > pLN) ?        alors cLN        sinon pLN
        Première itération :        13           0        13 > 0? => VRAI            13              /
        Deuxième itération :       27          13        27 > 13? => VRAI           27              /
        Troisième itération :        18          27        18 > 27? => FAUX           /             27
        Quatrième itération :       26          27        26 > 27? => FAUX           /             27
        Cinquième itération :         /          27                                                retourne 27
      Sortir du premier tableau et continuer sur le troisième
      Itération dans le troisième tableau
        Pour chaque itération :     cLN         pLN       si (cLN > pLN) ?        alors cLN        sinon pLN
        Première itération :        32           0        32 > 0? => VRAI            32              /
        Deuxième itération :       35          32        35 > 32? => VRAI           35              /
        Troisième itération :        37          35        37 > 35? => VRAI           37              /
        Quatrième itération :       39          37        39 > 37? => VRAI           39              /
        Cinquième itération :         /          39                                                retourne 39
      Sortir du premier tableau et continuer sur le quatrième
      Itération dans le quatrième tableau
        Pour chaque itération :     cLN         pLN       si (cLN > pLN) ?        alors cLN        sinon pLN
        Première itération :        1000         0        1000 > 0? => VRAI         1000             /
        Deuxième itération :       1001       1000       1001 > 1000? => VRAI      1001             /
        Troisième itération :        857        1001       857 > 1001 => FAUX        /             1001
        Quatrième itération :        1         1001       1 > 1001? => FAUX         /             1001
        Cinquième itération :         /         1001                                              retourne 1001
      Sortir du premier tableau et continuer sur le quatrième */
    }, 0); // 0 sert de contexte pour le premier pLN dans chaque sous-tableau
  });
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

Et voici la version sans commentaires :

```js

function largestOfFour(mainArray) {
  return mainArray.map(function (subArray){
    return subArray.reduce(function (previousLargestNumber, currentLargestNumber) {
      return (currentLargestNumber > previousLargestNumber) ? currentLargestNumber : previousLargestNumber;
    }, 0);
  });
}
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

### Approche #3 : Retourner les plus grands nombres dans un tableau avec des fonctions intégrées — avec map() et apply()

Pour cette solution, vous utiliserez deux méthodes : la méthode Array.prototype.map() et la méthode Function.prototype.apply().

* La méthode **apply()** appelle une fonction avec une valeur this donnée et des arguments fournis sous forme de tableau (ou d'un objet de type tableau).

Vous pouvez passer un tableau d'arguments à une fonction en utilisant la méthode **apply()** et la fonction exécutera les éléments du tableau.

De telles fonctions sont connues sous le nom de **fonctions variadiques**, et elles peuvent accepter n'importe quel nombre d'arguments au lieu d'un nombre fixe.

La fonction **Math.max()** retourne le plus grand de zéro ou plusieurs nombres, et nous pouvons passer n'importe quel nombre d'arguments.

```
console.log(Math.max(4,5,1,3)); // affiche 5
```

Mais vous ne pouvez pas passer un tableau de nombres à la méthode comme ceci :

```
var num = [4,5,1,3];
console.log(Math.max(num)); // affiche NaN
```

C'est là que la méthode **apply()** se révèle utile :

```
var num = [4,5,1,3];
console.log(Math.max.apply(null, num)); // affiche 5
```

Notez que le premier argument de **apply()** définit la valeur de **this**, non utilisé dans cette méthode, donc vous passez **null**.

Maintenant que vous avez une méthode pour retourner le plus grand nombre dans un tableau, vous pouvez parcourir chaque sous-tableau avec la méthode **map()** et retourner tous les plus grands nombres.

Voici ma solution, avec des commentaires intégrés :

```js

function largestOfFour(mainArray) {
  // Étape 1. Map sur les tableaux principaux
  return mainArray.map(function(subArray) { // Étape 3. Retourner les plus grands nombres de chaque sous-tableau => retourne [5,27,39,1001]
    
    // Étape 2. Retourner les plus grands nombres pour chaque sous-tableau avec la méthode Math.max()
    return Math.max.apply(null, subArray);
  });
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

Et sans commentaires :

```js

function largestOfFour(mainArray) {
  return mainArray.map(function(subArray) {
    return Math.max.apply(null, subArray);
  });
}
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

J'espère que vous avez trouvé cela utile. Cela fait partie de ma série d'articles « Comment résoudre les algorithmes FCC » sur les défis algorithmiques de Free Code Camp, où je propose plusieurs solutions et explique étape par étape ce qui se passe sous le capot.

[**Trois façons de répéter une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Repeat a string repeat a string » de freeCodeCamp. Cela implique..._](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Deux façons de confirmer la fin d'une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Confirm the Ending » de freeCodeCamp._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Trois façons d'inverser une chaîne en JavaScript**  
_Cet article est basé sur le défi « Reverse a String » de Free Code Camp Basic Algorithm Scripting._](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Trois façons de factoriser un nombre en JavaScript**  
_Cet article est basé sur le défi « Factorialize a Number » de Free Code Camp Basic Algorithm Scripting._](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Deux façons de vérifier les palindromes en JavaScript**  
_Cet article est basé sur le défi « Check for Palindromes » de Free Code Camp Basic Algorithm Scripting._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Trois façons de trouver le mot le plus long dans une chaîne en JavaScript**  
_Cet article est basé sur le défi « Find the Longest Word in a String » de Free Code Camp Basic Algorithm Scripting._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Trois façons de mettre en majuscule une phrase en JavaScript**  
_Cet article est basé sur le défi « Title Case a Sentence » de Free Code Camp Basic Algorithm Scripting._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

Si vous avez votre propre solution ou des suggestions, partagez-les ci-dessous dans les commentaires.

Ou vous pouvez me suivre sur [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** et [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), juste après avoir cliqué sur le cœur vert ci-dessous ;-)


#RestezCurieux, 
#ContinuezÀCoder & 
#FaitesQueCelaArrive!

### Ressources supplémentaires

* [for — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for)
* [array.length — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length)
* [méthode map() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
* [méthode reduce() — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)
* [Opérateur ternaire — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)
* [méthode apply() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)
* [Math.max() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max)
* [this — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/this)