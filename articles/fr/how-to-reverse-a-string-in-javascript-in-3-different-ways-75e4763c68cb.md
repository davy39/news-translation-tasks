---
title: Trois façons d'inverser une chaîne de caractères en JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-03-14T13:20:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aFrHLdCeSRv4z-hsfCA6hw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
seo_title: Trois façons d'inverser une chaîne de caractères en JavaScript
seo_desc: Reversing a string is one of the most frequently asked JavaScript question
  in the technical round of interview. Interviewers may ask you to write different
  ways to reverse a string, or they may ask you to reverse a string without using
  in-built metho...
---

**Inverser une chaîne de caractères** est l'une des questions JavaScript les plus fréquemment posées lors des entretiens techniques. Les recruteurs peuvent vous demander d'écrire différentes façons d'inverser une chaîne, ou de le faire sans utiliser de méthodes intégrées, ou même d'inverser une chaîne en utilisant la récursivité.

Il existe potentiellement des dizaines de façons différentes de le faire, à l'exclusion de la fonction intégrée **reverse**, car JavaScript n'en possède pas.

Voici mes trois façons les plus intéressantes de résoudre le problème d'inversion d'une chaîne de caractères en JavaScript. Notez que cet article est basé sur le défi d'algorithme de base de freeCodeCamp « [Inverser une chaîne](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-algorithm-scripting/reverse-a-string) ».

### Voici un Scrim interactif montrant comment inverser une chaîne de caractères en JavaScript

<iframe src="https://scrimba.com/scrim/cV6mkPUg?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

#### Défi d'algorithme

> Inversez la chaîne de caractères fournie.  
> _Vous devrez peut-être transformer la chaîne en tableau avant de pouvoir l'inverser._  
> _Votre résultat doit être une chaîne de caractères._

```js
function reverseString(str) {
    return str;
}
reverseString("hello");
```

#### Cas de test fournis

* **_reverseString("hello")_** devrait devenir "olleh"
* **_reverseString("Howdy")_** devrait devenir "ydwoH"
* **_reverseString("Greetings from Earth")_** devrait retourner "htraE morf sgniteerG"

### 1. Inverser une chaîne de caractères avec des fonctions intégrées

Pour cette solution, nous utiliserons trois méthodes : la méthode String.prototype.split(), la méthode Array.prototype.reverse() et la méthode Array.prototype.join().

* La méthode split() divise un objet String en un tableau de chaînes en séparant la chaîne en sous-chaînes.
* La méthode reverse() inverse un tableau en place. Le premier élément du tableau devient le dernier et le dernier devient le premier.
* La méthode join() joint tous les éléments d'un tableau en une chaîne.

```js
function reverseString(str) {
    // Étape 1. Utiliser la méthode split() pour retourner un nouveau tableau
    var splitString = str.split(""); // var splitString = "hello".split("");
    // ["h", "e", "l", "l", "o"]
 
    // Étape 2. Utiliser la méthode reverse() pour inverser le nouveau tableau créé
    var reverseArray = splitString.reverse(); // var reverseArray = ["h", "e", "l", "l", "o"].reverse();
    // ["o", "l", "l", "e", "h"]
 
    // Étape 3. Utiliser la méthode join() pour joindre tous les éléments du tableau en une chaîne
    var joinArray = reverseArray.join(""); // var joinArray = ["o", "l", "l", "e", "h"].join("");
    // "olleh"
    
    // Étape 4. Retourner la chaîne inversée
    return joinArray; // "olleh"
}
 
reverseString("hello");
```

#### Enchaînement des trois méthodes ensemble :

```
function reverseString(str) {
    return str.split("").reverse().join("");
}
reverseString("hello");
```

### 2. Inverser une chaîne de caractères avec une boucle For décroissante

```js
function reverseString(str) {
    // Étape 1. Créer une chaîne vide qui hébergera la nouvelle chaîne créée
    var newString = "";
 
    // Étape 2. Créer la boucle FOR
    /* Le point de départ de la boucle sera (str.length - 1) qui correspond au 
       dernier caractère de la chaîne, "o"
       Tant que i est supérieur ou égal à 0, la boucle continuera
       Nous décrémentons i après chaque itération */
    for (var i = str.length - 1; i >= 0; i--) { 
        newString += str[i]; // ou newString = newString + str[i];
    }
    /* Ici, la longueur de hello est égale à 5
        Pour chaque itération : i = str.length - 1 et newString = newString + str[i]
        Première itération :    i = 5 - 1 = 4,         newString = "" + "o" = "o"
        Deuxième itération :   i = 4 - 1 = 3,         newString = "o" + "l" = "ol"
        Troisième itération :    i = 3 - 1 = 2,         newString = "ol" + "l" = "oll"
        Quatrième itération :   i = 2 - 1 = 1,         newString = "oll" + "e" = "olle"
        Cinquième itération :    i = 1 - 1 = 0,         newString = "olle" + "h" = "olleh"
    Fin de la boucle FOR*/
 
    // Étape 3. Retourner la chaîne inversée
    return newString; // "olleh"
}
 
reverseString('hello');
```

#### Sans commentaires :

```js
function reverseString(str) {
    var newString = "";
    for (var i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }
    return newString;
}
reverseString('hello');
```

### 3. Inverser une chaîne de caractères avec la récursivité

Pour cette solution, nous utiliserons deux méthodes : la méthode String.prototype.substr() et la méthode String.prototype.charAt().

* La méthode substr() retourne les caractères d'une chaîne en commençant à l'emplacement spécifié jusqu'au nombre de caractères spécifié.

```
"hello".substr(1); // "ello"
```

* La méthode charAt() retourne le caractère spécifié d'une chaîne.

```
"hello".charAt(0); // "h"
```

La profondeur de la récursivité est égale à la longueur de la chaîne. Cette solution n'est pas la meilleure et sera très lente si la chaîne est très longue et que la taille de la pile est une préoccupation majeure.

```js
function reverseString(str) {
  if (str === "") // C'est le cas terminal qui mettra fin à la récursivité
    return "";
  
  else
    return reverseString(str.substr(1)) + str.charAt(0);
/* 
Première partie de la méthode de récursivité
Vous devez vous rappeler que vous n'aurez pas juste un appel, vous aurez plusieurs appels imbriqués

Chaque appel : str === "?"        	                  reverseString(str.subst(1))     + str.charAt(0)
1er appel – reverseString("Hello")   retournera   reverseString("ello")           + "h"
2e appel – reverseString("ello")    retournera   reverseString("llo")            + "e"
3e appel – reverseString("llo")     retournera   reverseString("lo")             + "l"
4e appel – reverseString("lo")      retournera   reverseString("o")              + "l"
5e appel – reverseString("o")       retournera   reverseString("")               + "o"

Deuxième partie de la méthode de récursivité
La méthode atteint la condition if et l'appel le plus imbriqué retourne immédiatement

5e appel retournera reverseString("") + "o" = "o"
4e appel retournera reverseString("o") + "l" = "o" + "l"
3e appel retournera reverseString("lo") + "l" = "o" + "l" + "l"
2e appel retournera reverserString("llo") + "e" = "o" + "l" + "l" + "e"
1er appel retournera reverserString("ello") + "h" = "o" + "l" + "l" + "e" + "h" 
*/
}
reverseString("hello");
```

#### Sans commentaires :

```
function reverseString(str) {
  if (str === "")
    return "";
  else
    return reverseString(str.substr(1)) + str.charAt(0);
}
reverseString("hello");
```

#### Opérateur conditionnel (ternaire) :

```js
function reverseString(str) {
  return (str === '') ? '' : reverseString(str.substr(1)) + str.charAt(0);
}
reverseString("hello");
```

**Inverser une chaîne de caractères en JavaScript** est un petit et simple algorithme qui peut être demandé lors d'un entretien technique téléphonique ou en personne. Vous pourriez prendre le chemin le plus court pour résoudre ce problème, ou adopter une approche en le résolvant avec la récursivité ou même des solutions plus complexes.

J'espère que vous avez trouvé cela utile. Cela fait partie de ma série d'articles « Comment résoudre les algorithmes FCC » sur les défis d'algorithmes de Free Code Camp, où je propose plusieurs solutions et explique étape par étape ce qui se passe sous le capot.

[**Trois façons de répéter une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Répéter une chaîne » de freeCodeCamp. Cela implique..._](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Deux façons de confirmer la fin d'une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Confirmer la fin » de freeCodeCamp._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Trois façons de factoriser un nombre en JavaScript**  
_Cet article est basé sur le défi d'algorithme de base de Free Code Camp « Factoriser un nombre »_](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Deux façons de vérifier les palindromes en JavaScript**  
_Cet article est basé sur le défi d'algorithme de base de Free Code Camp « Vérifier les palindromes »._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Trois façons de trouver le mot le plus long dans une chaîne en JavaScript**  
_Cet article est basé sur le défi d'algorithme de base de Free Code Camp « Trouver le mot le plus long dans une chaîne »._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Trois façons de mettre en majuscule la première lettre de chaque mot dans une phrase en JavaScript**  
_Cet article est basé sur le défi d'algorithme de base de Free Code Camp « Mettre en majuscule la première lettre de chaque mot dans une phrase »._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

Si vous avez votre propre solution ou des suggestions, partagez-les ci-dessous dans les commentaires.

Ou vous pouvez me suivre sur [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** et [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), juste après avoir cliqué sur le cœur vert ci-dessous ;-)


#RestezCurieux, 
#ContinuezÀCoder & 
#FaitesQueÇaArrive !

### Ressources

* [Méthode split() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
* [Méthode reverse() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
* [Méthode join() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
* [String.length — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
* [Méthode substr() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substr)
* [Méthode charAt() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)