---
title: Trois façons de mettre en majuscule la première lettre de chaque mot dans une
  phrase en JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-04-07T14:08:35.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YPdTg5Gx1FX66jSc_uwwlQ.jpeg
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
seo_title: Trois façons de mettre en majuscule la première lettre de chaque mot dans
  une phrase en JavaScript
seo_desc: 'This article is based on Free Code Camp Basic Algorithm Scripting “Title
  Case a Sentence”.

  In this algorithm, we want to change a string of text so that it always has a capital
  letter at the start of every word.

  In this article, I’m going to explain ...'
---

_Cet article est basé sur Free Code Camp Basic Algorithm Scripting «_[Title Case a Sentence](https://www.freecodecamp.com/challenges/title-case-a-sentence)_»._

**Dans cet algorithme**, nous voulons modifier une chaîne de texte afin que chaque mot commence par une majuscule.

Dans cet article, je vais expliquer trois approches. D'abord avec une boucle FOR, ensuite en utilisant la méthode map(), et enfin en utilisant la méthode replace().

#### Défi de l'algorithme

> Retournez la chaîne fournie avec la première lettre de chaque mot en majuscule. Assurez-vous que le reste du mot est en minuscule.  
>   
> Pour cet exercice, vous devez également mettre en majuscule les mots de liaison comme «the» et «of».

#### Cas de test fournis

* **_titleCase("I'm a little tea pot")_** doit retourner une chaîne.
* **_titleCase("I'm a little tea pot")_** doit retourner "I'm A Little Tea Pot".
* **_titleCase("sHoRt AnD sToUt")_** doit retourner "Short And Stout".
* **_titleCase("HERE IS MY HANDLE HERE IS MY SPOUT")_** doit retourner "Here Is My Handle Here Is My Spout".

### 1. Mettre en majuscule la première lettre de chaque mot avec une boucle FOR

Pour cette solution, nous allons utiliser la méthode String.prototype.toLowerCase(), la méthode String.prototype.split(), la méthode String.prototype.charAt(), la méthode String.prototype.slice() et la méthode Array.prototype.join().

* La méthode **toLowerCase()** retourne la valeur de la chaîne appelante convertie en minuscules.
* La méthode **split()** divise un objet String en un tableau de chaînes en séparant la chaîne en sous-chaînes.
* La méthode **charAt()** retourne le caractère spécifié d'une chaîne.
* La méthode **slice()** extrait une section d'une chaîne et retourne une nouvelle chaîne.
* La méthode **join()** joint tous les éléments d'un tableau en une chaîne.

Nous devons ajouter un espace entre les parenthèses de la méthode **split()**,

```
var strSplit = "I'm a little tea pot".split(' ');
```

ce qui produira un tableau de mots séparés:

```
var strSplit = ["I'm", "a", "little", "tea", "pot"];
```

Si vous n'ajoutez pas l'espace dans les parenthèses, vous aurez ce résultat:

```
var strSplit = ["I", "'", "m", " ", "a", " ", "l", "i", "t", "t", "l", "e", " ", "t", "e", "a", " ", "p", "o", "t"];
```

Nous allons concaténer

```
str[i].charAt(0).toUpperCase()
```

— qui mettra en majuscule le caractère d'index 0 de la chaîne actuelle dans la boucle FOR —

et

```
str[i].slice(1)
```

— qui extraira de l'index 1 à la fin de la chaîne.

Nous allons mettre toute la chaîne en minuscules à des fins de normalisation.

#### Avec commentaires:

```js

function titleCase(str) {
  // Étape 1. Mettre la chaîne en minuscules
  str = str.toLowerCase();
  // str = "I'm a little tea pot".toLowerCase();
  // str = "i'm a little tea pot";
  
  // Étape 2. Diviser la chaîne en un tableau de chaînes
  str = str.split(' ');
  // str = "i'm a little tea pot".split(' ');
  // str = ["i'm", "a", "little", "tea", "pot"];
  
  // Étape 3. Créer la boucle FOR
  for (var i = 0; i < str.length; i++) {
    str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1); 
  /* Ici str.length = 5
    1ère itération: str[0] = str[0].charAt(0).toUpperCase() + str[0].slice(1);
                   str[0] = "i'm".charAt(0).toUpperCase()  + "i'm".slice(1);
                   str[0] = "I"                            + "'m";
                   str[0] = "I'm";
    2ème itération: str[1] = str[1].charAt(0).toUpperCase() + str[1].slice(1);
                   str[1] = "a".charAt(0).toUpperCase()    + "a".slice(1);
                   str[1] = "A"                            + "";
                   str[1] = "A";
    3ème itération: str[2] = str[2].charAt(0).toUpperCase()   + str[2].slice(1);
                   str[2] = "little".charAt(0).toUpperCase() + "little".slice(1);
                   str[2] = "L"                              + "ittle";
                   str[2] = "Little";
    4ème itération: str[3] = str[3].charAt(0).toUpperCase() + str[3].slice(1);
                   str[3] = "tea".charAt(0).toUpperCase()  + "tea".slice(1);
                   str[3] = "T"                            + "ea";
                   str[3] = "Tea";
    5ème itération: str[4] = str[4].charAt(0).toUpperCase() + str[4].slice(1);
                   str[4] = "pot".charAt(0).toUpperCase() + "pot".slice(1);
                   str[4] = "P"                           + "ot";
                   str[4] = "Pot";                                                         
    Fin de la boucle FOR*/
  }
  
  // Étape 4. Retourner le résultat
  return str.join(' '); // ["I'm", "A", "Little", "Tea", "Pot"].join(' ') => "I'm A Little Tea Pot"
}

titleCase("I'm a little tea pot");
```

#### Sans commentaires:

```js
function titleCase(str) {
  str = str.toLowerCase().split(' ');
  for (var i = 0; i < str.length; i++) {
    str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1); 
  }
  return str.join(' ');
}
titleCase("I'm a little tea pot");
```

### 2. Mettre en majuscule la première lettre de chaque mot avec la méthode map()

Pour cette solution, nous allons utiliser la méthode Array.prototype.map().

* La méthode **map()** crée un nouveau tableau avec les résultats de l'appel d'une fonction fournie sur chaque élément de ce tableau. L'utilisation de map appellera une fonction de rappel fournie une fois pour chaque élément d'un tableau, dans l'ordre, et construira un nouveau tableau à partir des résultats.

Nous allons mettre la chaîne en minuscules et la diviser comme vu dans l'exemple précédent avant d'appliquer la méthode map().

Au lieu d'utiliser une boucle FOR, nous allons appliquer la méthode map() comme condition sur la même concaténation que dans l'exemple précédent.

```
(word.charAt(0).toUpperCase() + word.slice(1));
```

#### Avec commentaires:

```js

function titleCase(str) {
  // Étape 1. Mettre la chaîne en minuscules
  str = str.toLowerCase() // str = "i'm a little tea pot";
  
  // Étape 2. Diviser la chaîne en un tableau de chaînes
           .split(' ') // str = ["i'm", "a", "little", "tea", "pot"];
         
  // Étape 3. Appliquer map sur le tableau
           .map(function(word) {
    return (word.charAt(0).toUpperCase() + word.slice(1));
    /* Processus de map
    1er mot: "i'm"    => (word.charAt(0).toUpperCase() + word.slice(1));
                          "i'm".charAt(0).toUpperCase() + "i'm".slice(1);
                                "I"                     +     "'m";
                          return "I'm";
    2ème mot: "a"      => (word.charAt(0).toUpperCase() + word.slice(1));
                          "a".charAt(0).toUpperCase()   + "".slice(1);
                                "A"                     +     "";
                          return "A";
    3ème mot: "little" => (word.charAt(0).toUpperCase()    + word.slice(1));
                          "little".charAt(0).toUpperCase() + "little".slice(1);
                                "L"                        +     "ittle";
                          return "Little";
    4ème mot: "tea"    => (word.charAt(0).toUpperCase() + word.slice(1));
                          "tea".charAt(0).toUpperCase() + "tea".slice(1);
                                "T"                     +     "ea";
                          return "Tea";
    5ème mot: "pot"    => (word.charAt(0).toUpperCase() + word.slice(1));
                          "pot".charAt(0).toUpperCase() + "pot".slice(1);
                                "P"                     +     "ot";
                          return "Pot";                                                        
    Fin de la méthode map() */
});

 // Étape 4. Retourner le résultat
 return str.join(' '); // ["I'm", "A", "Little", "Tea", "Pot"].join(' ') => "I'm A Little Tea Pot"
}

titleCase("I'm a little tea pot");
```

#### Sans commentaires:

```js
function titleCase(str) {
  return str.toLowerCase().split(' ').map(function(word) {
    return (word.charAt(0).toUpperCase() + word.slice(1));
  }).join(' ');
}
titleCase("I'm a little tea pot");
```

### 3. Mettre en majuscule la première lettre de chaque mot avec les méthodes map() et replace()

Pour cette solution, nous allons continuer à utiliser la méthode Array.prototype.map() et ajouter la méthode String.prototype.replace().

* La méthode **replace()** retourne une nouvelle chaîne avec certaines ou toutes les correspondances d'un motif remplacées par un remplacement.

Dans notre cas, le motif pour la méthode replace() sera une chaîne à remplacer par un nouveau remplacement et sera traitée comme une chaîne littérale. Nous pouvons également utiliser une **expression régulière** comme motif pour résoudre cet algorithme.

Nous allons mettre la chaîne en minuscules et la diviser comme vu dans le premier exemple avant d'appliquer la méthode map().

#### Avec commentaires:

```js

function titleCase(str) {
  // Étape 1. Mettre la chaîne en minuscules
  str = str.toLowerCase() // str = "i'm a little tea pot";
  
  // Étape 2. Diviser la chaîne en un tableau de chaînes
           .split(' ') // str = ["i'm", "a", "little", "tea", "pot"];
         
  // Étape 3. Appliquer map sur le tableau
           .map(function(word) {
    return word.replace(word[0], word[0].toUpperCase());
    /* Processus de map
    1er mot: "i'm" => word.replace(word[0], word[0].toUpperCase());
                       "i'm".replace("i", "I");
                       return word => "I'm"
    2ème mot: "a" => word.replace(word[0], word[0].toUpperCase());
                     "a".replace("a", "A");
                      return word => "A"
    3ème mot: "little" => word.replace(word[0], word[0].toUpperCase());
                          "little".replace("l", "L");
                          return word => "Little"
    4ème mot: "tea" => word.replace(word[0], word[0].toUpperCase());
                       "tea".replace("t", "T");
                       return word => "Tea"
    5ème mot: "pot" => word.replace(word[0], word[0].toUpperCase());
                       "pot".replace("p", "P");
                       return word => "Pot"                                                        
    Fin de la méthode map() */
});

 // Étape 4. Retourner le résultat
 return str.join(' '); // ["I'm", "A", "Little", "Tea", "Pot"].join(' ') => "I'm A Little Tea Pot"
}

titleCase("I'm a little tea pot");
```

#### Sans commentaires:

```js
function titleCase(str) {
  return str.toLowerCase().split(' ').map(function(word) {
    return word.replace(word[0], word[0].toUpperCase());
  }).join(' ');
}
titleCase("I'm a little tea pot");
```

J'espère que vous avez trouvé cela utile. Cela fait partie de ma série d'articles «How to Solve FCC Algorithms» sur les défis d'algorithmes de Free Code Camp, où je propose plusieurs solutions et explique étape par étape ce qui se passe sous le capot.

[**Trois façons de répéter une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi «Repeat a string repeat a string» de freeCodeCamp. Cela implique…_](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Deux façons de confirmer la fin d'une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi «Confirm the Ending» de freeCodeCamp._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Trois façons d'inverser une chaîne en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting «Reverse a String»_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Trois façons de factoriser un nombre en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting «Factorialize a Number»_](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Deux façons de vérifier les palindromes en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting «Check for Palindromes»._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Trois façons de trouver le mot le plus long dans une chaîne en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting «Find the Longest Word in a String»._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Trois façons de trouver le plus grand nombre dans un tableau en utilisant JavaScript**  
_Dans cet article, je vais expliquer comment résoudre le défi «Return Largest Numbers in Arrays» de Free Code Camp. Cela…_](https://www.freecodecamp.org/news/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1/)

Si vous avez votre propre solution ou des suggestions, partagez-les ci-dessous dans les commentaires.

Ou vous pouvez me suivre sur [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** et [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset)**.**


#RestezCurieux, 
#ContinuezÀCoder & 
#FaitesQueCelaArrive!

### Ressources

* [Méthode toLowerCase() — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
* [Méthode toUpperCase() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)
* [Méthode charAt() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)
* [Méthode slice() — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
* [Méthode split() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
* [Méthode join() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
* [for — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for)
* [Méthode map() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
* [Méthode replace() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)