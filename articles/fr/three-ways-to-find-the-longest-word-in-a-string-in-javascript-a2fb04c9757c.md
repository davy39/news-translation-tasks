---
title: Trois façons de trouver le mot le plus long dans une chaîne en JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-03-30T13:06:33.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*k2RZZ3j1e-_r9Av7SgzFDw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Trois façons de trouver le mot le plus long dans une chaîne en JavaScript
seo_desc: 'This article is based on Free Code Camp Basic Algorithm Scripting “Find
  the Longest Word in a String”.

  In this algorithm, we want to look at each individual word and count how many letters
  are in each. Then, compare the counts to determine which word...'
---

_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « [Find the Longest Word in a String](https://www.freecodecamp.com/challenges/find-the-longest-word-in-a-string) »._

**Dans cet algorithme**, nous voulons examiner chaque mot individuel et compter combien de lettres chacun contient. Ensuite, comparer les comptes pour déterminer quel mot a le plus de caractères et retourner la longueur du mot le plus long.

Dans cet article, je vais expliquer trois approches. D'abord avec une boucle FOR, ensuite en utilisant la méthode sort(), et enfin en utilisant la méthode reduce().

#### Défi de l'algorithme

> Retourner la longueur du mot le plus long dans la phrase fournie.  
>   
> Votre réponse doit être un nombre.

#### **Cas de test fournis**

* **_findLongestWord("The quick brown fox jumped over the lazy dog")_** devrait retourner un nombre
* **_findLongestWord("The quick brown fox jumped over the lazy dog")_** devrait retourner 6
* **_findLongestWord("May the force be with you")_** devrait retourner 5
* **_findLongestWord("Google do a barrel roll")_** devrait retourner 6
* **_findLongestWord("What is the average airspeed velocity of an unladen swallow")_** devrait retourner 8
* **_findLongestWord("What if we try a super-long word such as otorhinolaryngology")_** devrait retourner 19

```js
function findLongestWord(str) {
  return str.length;
}
findLongestWord("The quick brown fox jumped over the lazy dog");
```

### 1. Trouver le mot le plus long avec une boucle FOR

Pour cette solution, nous allons utiliser la méthode String.prototype.split()

* La méthode **split()** divise un objet String en un tableau de chaînes en séparant la chaîne en sous-chaînes.

Nous devons ajouter un espace vide entre les parenthèses de la méthode **split()**

```
var strSplit = "The quick brown fox jumped over the lazy dog".split(' ');
```

ce qui donnera un tableau de mots séparés :

```
var strSplit = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"];
```

Si vous n'ajoutez pas l'espace dans les parenthèses, vous aurez ce résultat :

```
var strSplit = 
["T", "h", "e", " ", "q", "u", "i", "c", "k", " ", "b", "r", "o", "w", "n", " ", "f", "o", "x", " ", "j", "u", "m", "p", "e", "d", " ", "o", "v", "e", "r", " ", "t", "h", "e", " ", "l", "a", "z", "y", " ", "d", "o", "g"];
```

```js
function findLongestWord(str) {
  // Étape 1. Diviser la chaîne en un tableau de chaînes
  var strSplit = str.split(' ');
  // var strSplit = "The quick brown fox jumped over the lazy dog".split(' ');
  // var strSplit = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"];
	
  // Étape 2. Initialiser une variable qui contiendra la longueur du mot le plus long
  var longestWord = 0;

  // Étape 3. Créer la boucle FOR
  for(var i = 0; i < strSplit.length; i++){
    if(strSplit[i].length > longestWord){ // Si strSplit[i].length est supérieur au mot avec lequel il est comparé...
	longestWord = strSplit[i].length; // ...alors longestWord prend cette nouvelle valeur
     }
  }
  /* Ici strSplit.length = 9
     Pour chaque itération : i = ?   i < strSplit.length?   i++  if(strSplit[i].length > longestWord)?   longestWord = strSplit[i].length
     1ère itération :        0             oui             1   if("The".length > 0)? => if(3 > 0)?     longestWord = 3
     2ème itération :        1             oui             2   if("quick".length > 3)? => if(5 > 3)?   longestWord = 5   
     3ème itération :        2             oui             3   if("brown".length > 5)? => if(5 > 5)?   longestWord = 5   
     4ème itération :        3             oui             4   if("fox".length > 5)? => if(3 > 5)?     longestWord = 5  
     5ème itération :        4             oui             5   if("jumped".length > 5)? => if(6 > 5)?  longestWord = 6 
     6ème itération :        5             oui             6   if("over".length > 6)? => if(4 > 6)?    longestWord = 6 
     7ème itération :        6             oui             7   if("the".length > 6)? => if(3 > 6)?     longestWord = 6
     8ème itération :        7             oui             8   if("lazy".length > 6)? => if(4 > 6)?    longestWord = 6 
     9ème itération :        8             oui             9   if("dog".length > 6)? => if(3 > 6)?     longestWord = 6 
     10ème itération :       9             non               
     Fin de la boucle FOR*/

  //Étape 4. Retourner le mot le plus long
  return longestWord; // 6
}

findLongestWord("The quick brown fox jumped over the lazy dog");
```

#### Sans commentaires :

```js
function findLongestWord(str) {
  var strSplit = str.split(' ');
  var longestWord = 0;
  for(var i = 0; i < strSplit.length; i++){
    if(strSplit[i].length > longestWord){
	longestWord = strSplit[i].length;
     }
  }
  return longestWord;
}
findLongestWord("The quick brown fox jumped over the lazy dog");
```

### 2. Trouver le mot le plus long avec la méthode sort()

Pour cette solution, nous allons utiliser la méthode Array.prototype.sort() pour trier le tableau selon un critère d'ordre, puis retourner la longueur du premier élément de ce tableau.

* La méthode **sort()** trie les éléments d'un tableau en place et retourne le tableau.

Dans notre cas, si nous trions simplement le tableau

```
var sortArray = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"].sort();
```

nous aurons ce résultat :

```
var sortArray = ["The", "brown", "dog", "fox", "jumped", "lazy", "over", "quick", "the"];
```

En Unicode, les nombres viennent avant les lettres majuscules, qui viennent avant les lettres minuscules.

Nous devons trier les éléments selon un critère d'ordre,

```
[].sort(function(firstElement, secondElement) {     return secondElement.length - firstElement.length; })
```

où la longueur du deuxième élément est comparée à la longueur du premier élément dans le tableau.

```js
function findLongestWord(str) {
  // Étape 1. Diviser la chaîne en un tableau de chaînes
  var strSplit = str.split(' ');
  // var strSplit = "The quick brown fox jumped over the lazy dog".split(' ');
  // var strSplit = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"];
  
  // Étape 2. Trier les éléments dans le tableau
  var longestWord = strSplit.sort(function(a, b) { 
    return b.length - a.length;
  });
  /* Processus de tri
    a           b            b.length     a.length     var longestWord
  "The"      "quick"            5            3         ["quick", "The"]
  "quick"    "brown"            5            5         ["quick", "brown", "The"]  
  "brown"    "fox"              3            5         ["quick", "brown", "The", "fox"]
  "fox"      "jumped"           6            3         ["jumped", quick", "brown", "The", "fox"]
  "jumped"   "over"             4            6         ["jumped", quick", "brown", "over", "The", "fox"]
  "over"     "the"              3            4         ["jumped", quick", "brown", "over", "The", "fox", "the"]
  "the"      "lazy"             4            3         ["jumped", quick", "brown", "over", "lazy", "The", "fox", "the"]
  "lazy"     "dog"              3            4         ["jumped", quick", "brown", "over", "lazy", "The", "fox", "the", "dog"]
  */
  
  // Étape 3. Retourner la longueur du premier élément du tableau
  return longestWord[0].length; // var longestWord = ["jumped", "quick", "brown", "over", "lazy", "The", "fox", "the", "dog"];
                                // longestWord[0]="jumped" => jumped".length => 6
}

findLongestWord("The quick brown fox jumped over the lazy dog");
```

#### Sans commentaires :

```js
function findLongestWord(str) {
  var longestWord = str.split(' ').sort(function(a, b) { return b.length - a.length; });
  return longestWord[0].length;
}
findLongestWord("The quick brown fox jumped over the lazy dog");
```

### 3. Trouver le mot le plus long avec la méthode reduce()

Pour cette solution, nous allons utiliser Array.prototype.reduce().

* La méthode **reduce()** applique une fonction contre un accumulateur et chaque valeur du tableau (de gauche à droite) pour le réduire à une seule valeur.

reduce() exécute une fonction de rappel une fois pour chaque élément présent dans le tableau.

Vous pouvez fournir une valeur initiale comme deuxième argument à reduce, ici nous allons ajouter une chaîne vide "".

```
[].reduce(function(previousValue, currentValue) {...}, "");
```

```js
function findLongestWord(str) {
  // Étape 1. Diviser la chaîne en un tableau de chaînes
  var strSplit = str.split(' ');
  // var strSplit = "The quick brown fox jumped over the lazy dog".split(' ');
  // var strSplit = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"];

  // Étape 2. Utiliser la méthode reduce
  var longestWord = strSplit.reduce(function(longest, currentWord) {
    if(currentWord.length > longest.length)
       return currentWord;
    else
       return longest;
  }, "");
  
  /* Processus de réduction
  currentWord      longest       currentWord.length     longest.length    if(currentWord.length > longest.length)?   var longestWord
  "The"             ""                  3                     0                              oui                          "The"
  "quick"           "The"               5                     3                              oui                         "quick"
  "brown"           "quick"             5                     5                              non                          "quick"
  "fox"             "quick"             3                     5                              non                          "quick"
  "jumped"          "quick"             6                     5                              oui                         "jumped"
  "over"            "jumped"            4                     6                              non                          "jumped"
  "the"             "jumped"            3                     6                              non                          "jumped"
  "lazy"            "jumped"            4                     6                              non                          "jumped"
  "dog"             "jumped"            3                     6                              non                          "jumped"
  */
  
  // Étape 3. Retourner la longueur du longestWord
  return longestWord.length; // var longestWord = "jumped" 
                             // longestWord.length => "jumped".length => 6
}

findLongestWord("The quick brown fox jumped over the lazy dog");
```

#### Sans commentaires :

```js
function findLongestWord(str) {
  var longestWord = str.split(' ').reduce(function(longest, currentWord) {
    return currentWord.length > longest.length ? currentWord : longest;
  }, "");
  return longestWord.length;
}
findLongestWord("The quick brown fox jumped over the lazy dog");
```

J'espère que vous avez trouvé cela utile. Cela fait partie de ma série d'articles « How to Solve FCC Algorithms » sur les défis d'algorithmes de Free Code Camp, où je propose plusieurs solutions et explique étape par étape ce qui se passe sous le capot.

[**Trois façons de répéter une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Repeat a string repeat a string » de freeCodeCamp. Cela implique..._](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Deux façons de confirmer la fin d'une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Confirm the Ending » de freeCodeCamp._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Trois façons d'inverser une chaîne en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Reverse a String »_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Trois façons de factoriser un nombre en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Factorialize a Number »_](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Deux façons de vérifier les palindromes en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Check for Palindromes »._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Trois façons de mettre en majuscule une phrase en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Title Case a Sentence »._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

[**Trois façons de trouver le plus grand nombre dans un tableau en utilisant JavaScript**  
_Dans cet article, je vais expliquer comment résoudre le défi « Return Largest Numbers in Arrays » de Free Code Camp. Cela..._](https://www.freecodecamp.org/news/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1/)

Si vous avez votre propre solution ou des suggestions, partagez-les ci-dessous dans les commentaires.

Ou vous pouvez me suivre sur [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** et [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), juste après avoir cliqué sur le cœur vert ci-dessous ;-)

#StayCurious, #KeepOnHacking & #MakeItHappen !

### Ressources

* [Méthode split() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
* [Méthode sort() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
* [reduce() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)
* [String.length — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
* [for — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for)