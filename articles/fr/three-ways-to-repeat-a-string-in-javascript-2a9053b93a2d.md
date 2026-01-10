---
title: Trois façons de répéter une chaîne en JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2017-02-13T19:45:18.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5xZaBnyrMAe9JkgajD3NbA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Trois façons de répéter une chaîne en JavaScript
seo_desc: 'In this article, I’ll explain how to solve freeCodeCamp’s “Repeat a string
  repeat a string” challenge. This involves repeating a string a certain number of
  times.

  There are the three approaches I’ll cover:


  using a while loop

  using recursion

  using ES...'
---

Dans cet article, je vais expliquer comment résoudre le défi "[Repeat a string repeat a string](https://www.freecodecamp.com/challenges/repeat-a-string-repeat-a-string)" de freeCodeCamp. Cela implique de répéter une chaîne un certain nombre de fois.

Voici les trois approches que je vais couvrir :

1. utiliser une boucle while
2. utiliser la récursivité
3. utiliser la méthode ES6 repeat()

### Description du défi algorithmique

> _Répéter une chaîne donnée (premier argument) `num` fois (deuxième argument). Retourner une chaîne vide si `num` n'est pas un nombre positif._

```js
function repeatStringNumTimes(str, num) {
  return str;
}
repeatStringNumTimes("abc", 3);
```

### Cas de test fournis

```js
repeatStringNumTimes("*", 3) devrait retourner "***".

repeatStringNumTimes("abc", 3) devrait retourner "abcabcabc".

repeatStringNumTimes("abc", 4) devrait retourner "abcabcabcabc".

repeatStringNumTimes("abc", 1) devrait retourner "abc".

repeatStringNumTimes("*", 8) devrait retourner "********".

repeatStringNumTimes("abc", -2) devrait retourner "".
```

### Approche #1 : Répéter une chaîne avec une boucle While

Une instruction while exécute son instruction tant qu'une condition spécifiée évalue à vrai.

Une instruction while ressemble à ceci :

```js
while (condition)
  instruction
```

avec une condition qui est évaluée avant chaque passage dans la boucle. Si la condition est vraie, l'instruction est exécutée. Si la condition est fausse, l'exécution continue avec toute instruction après la boucle while.

L'instruction est exécutée tant que la condition est vraie. Voici la solution :

```js

function repeatStringNumTimes(string, times) {
  // Étape 1. Créer une chaîne vide qui hébergera la chaîne répétée
  var repeatedString = "";

  // Étape 2. Définir la boucle While avec (times > 0) comme condition à vérifier
  while (times > 0) { // Tant que times est supérieur à 0, l'instruction est exécutée
    // L'instruction
    repeatedString += string; // Équivalent à repeatedString = repeatedString + string;
    times--; // Équivalent à times = times - 1;
  }
  /* Logique de la boucle While
                      Condition       V/F       repeatedString += string      repeatedString        times
    Première itération    (3 > 0)        true            "" + "abc"                  "abc"               2
    Deuxième itération   (2 > 0)        true           "abc" + "abc"               "abcabc"             1
    Troisième itération    (1 > 0)        true          "abcabc" + "abc"            "abcabcabc"           0
    Quatrième itération   (0 > 0)        false
    }
  */
  
  // Étape 3. Retourner la chaîne répétée
  return repeatedString; // "abcabcabc"
}

repeatStringNumTimes("abc", 3);
```

Et encore, sans commentaires :

```js
function repeatStringNumTimes(string, times) {
  var repeatedString = "";
  while (times > 0) {
    repeatedString += string;
    times--;
  }
  return repeatedString;
}
repeatStringNumTimes("abc", 3);
```

### Approche #2 : Répéter une chaîne en utilisant une condition et la récursivité

La récursivité est une technique pour itérer sur une opération en ayant une fonction qui s'appelle elle-même répétitivement jusqu'à ce qu'elle arrive à un résultat. Il y a quelques caractéristiques clés de la récursivité qui doivent être incluses pour qu'elle fonctionne correctement.

* La première est un **_cas de base_**: il s'agit d'une instruction, généralement dans une clause conditionnelle comme `if`, qui arrête la récursivité.
* La seconde est un **_cas récursif_**: il s'agit de l'instruction où la fonction récursive est appelée sur elle-même.

Voici la solution :

```js
function repeatStringNumTimes(string, times) {
  // Étape 1. Vérifier si times est négatif et retourner une chaîne vide si vrai
  if (times < 0) {
    return "";
  }
  
  // Étape 2. Vérifier si times est égal à 1 et retourner la chaîne elle-même si c'est le cas.
  if (times === 1) {
    return string;
  }
  
  // Étape 3. Utiliser la récursivité
  else {
    return string + repeatStringNumTimes(string, times - 1); // return "abcabcabc";
  }
  /* 
    Première partie de la méthode de récursivité
    Vous devez vous souvenir que vous n'aurez pas juste un appel, vous aurez plusieurs appels imbriqués
                     times       string + repeatStringNumTimes(string, times - 1)
      1er appel         3                 "abc" + ("abc", 3 - 1)
      2ème appel         2                 "abc" + ("abc", 2 - 1)
      3ème appel         1                 "abc" => if (times === 1) return string;
      4ème appel         0                  ""   => if (times <= 0) return "";
    Deuxième partie de la méthode de récursivité
      4ème appel retournera      ""
      3ème appel retournera     "abc"
      2ème appel retournera     "abc"
      1er appel retournera     "abc"
    L'appel final est une concaténation de toutes les chaînes
    return "abc" + "abc" + "abc"; // return "abcabcabc";
  */
}
repeatStringNumTimes("abc", 3);
```

Et encore, sans commentaires :

```js
function repeatStringNumTimes(string, times) {
  if(times < 0) 
    return "";
  if(times === 1) 
    return string;
  else 
    return string + repeatStringNumTimes(string, times - 1);
}
repeatStringNumTimes("abc", 3);
```

### Approche #3 : Répéter une chaîne en utilisant la méthode ES6 repeat()

Pour cette solution, vous allez utiliser la méthode String.prototype.repeat() :

* La méthode `**repeat()**` construit et retourne une nouvelle chaîne qui contient le nombre spécifié de copies de la chaîne sur laquelle elle a été appelée, concaténées ensemble.

Voici la solution :

```js

function repeatStringNumTimes(string, times) {
  //Étape 1. Si times est positif, retourner la chaîne répétée
  if (times > 0) { // (3 > 0) => true
    return string.repeat(times); // return "abc".repeat(3); => return "abcabcabc";
  }
  
  //Étape 2. Sinon si times est négatif, retourner une chaîne vide si vrai
  else {
    return "";
  }
}

repeatStringNumTimes("abc", 3);
```

Et encore, sans commentaires :

```js
function repeatStringNumTimes(string, times) {
  if (times > 0)
    return string.repeat(times);
  else
    return "";
}
repeatStringNumTimes("abc", 3);
```

Vous pouvez utiliser un **opérateur ternaire** comme raccourci pour l'instruction if/else, comme ceci :

```js
times > 0 ? string.repeat(times) : "";
```

Cela peut être lu comme :

```js
if (times > 0) {    
    return string.repeat(times);
} else {
    return "";
}
```

Vous pouvez ensuite retourner l'opérateur ternaire dans votre fonction :

J'espère que vous avez trouvé cela utile. Cela fait partie de ma série d'articles "How to Solve FCC Algorithms" sur les défis algorithmiques de freeCodeCamp, où je propose plusieurs solutions et explique étape par étape ce qui se passe sous le capot.

[**Deux façons de confirmer la fin d'une chaîne en JavaScript**](https://medium.freecodecamp.com/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac)  
_[Dans cet article, j'explique comment résoudre le défi "Confirm the Ending" de freeCodeCamp.](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)_

[**Trois façons d'inverser une chaîne en JavaScript**](https://medium.freecodecamp.com/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb)  
_[Cet article est basé sur le défi "Reverse a String" de Free Code Camp Basic Algorithm Scripting](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)_

[**Trois façons de factoriser un nombre en JavaScript**](https://medium.freecodecamp.com/how-to-factorialize-a-number-in-javascript-9263c89a4b38)  
_[Cet article est basé sur le défi "Factorialize a Number" de Free Code Camp Basic Algorithm Scripting](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)_

**[Deux façons de vérifier les palindromes en JavaScript](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)**  
_[Cet article est basé sur le défi "Check for Palindromes" de Free Code Camp Basic Algorithm Scripting.](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)_

**[Trois façons de trouver le mot le plus long dans une chaîne en JavaScript](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)**  
_[Cet article est basé sur le défi "Find the Longest Word in a String" de Free Code Camp Basic Algorithm Scripting.](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)_

**[Trois façons de mettre en majuscule la première lettre de chaque mot dans une phrase en JavaScript](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)**  
_[Cet article est basé sur le défi "Title Case a Sentence" de Free Code Camp Basic Algorithm Scripting.](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)_

Si vous avez votre propre solution ou des suggestions, partagez-les ci-dessous dans les commentaires.

Ou vous pouvez me suivre sur [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** et [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), juste après avoir cliqué sur le cœur vert ci-dessous ;-)


#RestezCurieux, 
#ContinuezÀCoder & 
#FaitesQueCelaArrive!

### Ressources supplémentaires

* [while loop — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
* [repeat() method — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/repeat)
* [recursion — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#Recursion)
* [Ternary Operator — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)