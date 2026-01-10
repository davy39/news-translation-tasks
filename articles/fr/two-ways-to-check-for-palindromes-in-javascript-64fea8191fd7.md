---
title: Deux façons de vérifier les palindromes en JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-03-22T11:23:37.000Z'
originalURL: https://freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gaAkSMf6J7cMTJCgQVX2Kg.jpeg
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
seo_title: Deux façons de vérifier les palindromes en JavaScript
seo_desc: 'This article is based on Free Code Camp Basic Algorithm Scripting “Check
  for Palindromes”.

  A palindrome is a word, phrase, number, or other sequence of characters which reads
  the same backward or forward. The word “palindrome” was first coined by the...'
---

_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « [Check for Palindromes](https://www.freecodecamp.com/challenges/check-for-palindromes) »._

**Un palindrome** est un mot, une phrase, un nombre ou une autre séquence de caractères qui se lit de la même manière à l'envers ou à l'endroit. Le mot « palindrome » a été inventé pour la première fois par le dramaturge anglais [Ben Jonson](https://en.wikipedia.org/wiki/Ben_Jonson) au 17ème siècle, à partir des racines grecques _palin_ (« encore ») et _dromos_ (« chemin, direction »). — _src. Wikipedia_

Dans cet article, je vais expliquer deux approches, d'abord avec des fonctions intégrées et ensuite en utilisant une boucle for.

#### Défi de l'algorithme

> Retourne true si la chaîne donnée est un palindrome. Sinon, retourne false.  
>   
> Un palindrome est un mot ou une phrase qui s'épelle de la même manière à l'endroit et à l'envers, en ignorant la ponctuation, la casse et les espaces.  
>   
> **Note.** Vous devrez supprimer **tous les caractères non alphanumériques** (ponctuation, espaces et symboles) et tout mettre en minuscules pour vérifier les palindromes.  
>   
> Nous passerons des chaînes avec des formats variés, tels que « racecar », « RaceCar » et « race CAR » parmi d'autres.

```js
function palindrome(str) {
  return true;
}
palindrome("eye");
```

#### _Cas de test fournis_

* **_palindrome("race car")_** devrait retourner true
* **_palindrome("not a palindrome")_** devrait retourner false
* **_palindrome("A man, a plan, a canal. Panama")_** devrait retourner true
* **_palindrome("never odd or even")_** devrait retourner true
* **_palindrome("nope")_** devrait retourner false
* **_palindrome("almostomla")_** devrait retourner false
* **_palindrome("My age is 0, 0 si ega ym.")_** devrait retourner true
* **_palindrome("1 eye for of 1 eye.")_** devrait retourner false
* **_palindrome("0_0 (: /-\ :) 0–0")_** devrait retourner true

### Quelle **expression régulière** devons-nous utiliser pour passer le dernier cas de test ?

Les expressions régulières sont des motifs utilisés pour faire correspondre des combinaisons de caractères dans des chaînes.

Lorsque la recherche d'une correspondance nécessite quelque chose de plus qu'une correspondance directe, le motif inclut des caractères spéciaux.

```
Pour passer le dernier cas de test, nous pouvons utiliser deux expressions régulières :

/[^A-Za-z0–9]/g  ou

/[\W_]/g
```

**\W** supprime **tous les caractères non alphanumériques** :

* **\W** correspond à tout caractère non alphanumérique
* **\W** est équivalent à [^A-Za-z0–9_]
* **\W** correspond à tout ce qui n'est pas inclus dans les crochets

Que signifie cela ?

```
[^A-Z] correspond à tout ce qui n'est pas inclus entre A et Z

[^a-z] correspond à tout ce qui n'est pas inclus entre a et z

[^0-9] correspond à tout ce qui n'est pas inclus entre 0 et 9

[^_] correspond à tout ce qui n'inclut pas _
```

Mais dans notre cas de test, nous avons besoin que palindrome("**0_0 (: /-\ :) 0–0**") retourne **true**, ce qui signifie que "**_(: /-\ :)**" doit être correspondre.

Nous devrons ajouter "**_**" pour passer ce cas de test spécifique.

```
Nous avons maintenant "\W_"
```

Nous devrons également ajouter le drapeau **g** pour une recherche globale.

```
Nous avons finalement "/[\W_]/g"
```

> **_/[\W_]/g_** _a été utilisé à des fins purement démonstratives pour montrer comment fonctionne RegExp. **/[^A-Za-z0–9]/g** est l'expression régulière la plus facile à choisir._

### 1. Vérifier les palindromes avec des fonctions intégrées

Pour cette solution, nous allons utiliser plusieurs méthodes :

* La méthode **toLowerCase()** pour retourner la valeur de la chaîne appelante convertie en minuscules.
* La méthode **replace()** pour retourner une nouvelle chaîne avec certaines ou toutes les correspondances d'un motif remplacées par un remplacement. Nous utiliserons l'une des RegExp que nous venons de créer précédemment.
* La méthode **split()** divise un objet String en un tableau de chaînes en séparant la chaîne en sous-chaînes.
* La méthode **reverse()** inverse un tableau en place. Le premier élément du tableau devient le dernier et le dernier devient le premier.
* La méthode **join()** joint tous les éléments d'un tableau en une chaîne.

```js
function palindrome(str) {
  // Étape 1. Mettre la chaîne en minuscules et utiliser la RegExp pour supprimer les caractères indésirables
  var re = /[\W_]/g; // ou var re = /[^A-Za-z0-9]/g;
  
  var lowRegStr = str.toLowerCase().replace(re, '');
  // str.toLowerCase() = "A man, a plan, a canal. Panama".toLowerCase() = "a man, a plan, a canal. panama"
  // str.replace(/[\W_]/g, '') = "a man, a plan, a canal. panama".replace(/[\W_]/g, '') = "amanaplanacanalpanama"
  // var lowRegStr = "amanaplanacanalpanama";
     
  // Étape 2. Utiliser les mêmes méthodes de chaînage avec des fonctions intégrées de l'article précédent 'Three Ways to Reverse a String in JavaScript'
  var reverseStr = lowRegStr.split('').reverse().join(''); 
  // lowRegStr.split('') = "amanaplanacanalpanama".split('') = ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"]
  // ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"].reverse() = ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"]
  // ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"].join('') = "amanaplanacanalpanama"
  // Donc, "amanaplanacanalpanama".split('').reverse().join('') = "amanaplanacanalpanama";
  // Et, var reverseStr = "amanaplanacanalpanama";
   
  // Étape 3. Vérifier si reverseStr est strictement égal à lowRegStr et retourner un booléen
  return reverseStr === lowRegStr; // "amanaplanacanalpanama" === "amanaplanacanalpanama"? => true
}
 
palindrome("A man, a plan, a canal. Panama");
```

#### Sans commentaires :

```js
function palindrome(str) {
  var re = /[\W_]/g;
  var lowRegStr = str.toLowerCase().replace(re, '');
  var reverseStr = lowRegStr.split('').reverse().join(''); 
  return reverseStr === lowRegStr;
}
palindrome("A man, a plan, a canal. Panama");
```

### 2. Vérifier les palindromes avec une boucle FOR

L'indexation à moitié (len/2) a des avantages lors du traitement de grandes chaînes. Nous vérifions la fin de chaque partie et divisons le nombre d'itérations à l'intérieur de la boucle FOR par deux.

```js
function palindrome(str) {
 // Étape 1. La première partie est la même que précédemment
 var re = /[^A-Za-z0-9]/g; // ou var re = /[\W_]/g;
 str = str.toLowerCase().replace(re, '');

 // Étape 2. Créer la boucle FOR
 var len = str.length; // var len = "A man, a plan, a canal. Panama".length = 30
 
 for (var i = 0; i < len/2; i++) {
   if (str[i] !== str[len - 1 - i]) { // Tant que les caractères de chaque partie correspondent, la boucle FOR continue
       return false; // Lorsque les caractères ne correspondent plus, false est retourné et nous sortons de la boucle FOR
   }
   /* Ici len/2 = 15
      Pour chaque itération : i = ?    i < len/2    i++    if(str[i] !== str[len - 1 - i])?
      1ère itération :        0        oui         1     if(str[0] !== str[15 - 1 - 0])? => if("a"  !==  "a")? // false
      2ème itération :        1        oui         2     if(str[1] !== str[15 - 1 - 1])? => if("m"  !==  "m")? // false      
      3ème itération :        2        oui         3     if(str[2] !== str[15 - 1 - 2])? => if("a"  !==  "a")? // false  
      4ème itération :        3        oui         4     if(str[3] !== str[15 - 1 - 3])? => if("n"  !==  "n")? // false  
      5ème itération :        4        oui         5     if(str[4] !== str[15 - 1 - 4])? => if("a"  !==  "a")? // false
      6ème itération :        5        oui         6     if(str[5] !== str[15 - 1 - 5])? => if("p"  !==  "p")? // false
      7ème itération :        6        oui         7     if(str[6] !== str[15 - 1 - 6])? => if("l"  !==  "l")? // false
      8ème itération :        7        oui         8     if(str[7] !== str[15 - 1 - 7])? => if("a"  !==  "a")? // false
      9ème itération :        8        oui         9     if(str[8] !== str[15 - 1 - 8])? => if("n"  !==  "n")? // false
     10ème itération :        9        oui        10     if(str[9] !== str[15 - 1 - 9])? => if("a"  !==  "a")? // false
     11ème itération :       10        oui        11    if(str[10] !== str[15 - 1 - 10])? => if("c" !==  "c")? // false
     12ème itération :       11        oui        12    if(str[11] !== str[15 - 1 - 11])? => if("a" !==  "a")? // false
     13ème itération :       12        oui        13    if(str[12] !== str[15 - 1 - 12])? => if("n" !==  "n")? // false
     14ème itération :       13        oui        14    if(str[13] !== str[15 - 1 - 13])? => if("a" !==  "a")? // false
     15ème itération :       14        oui        15    if(str[14] !== str[15 - 1 - 14])? => if("l" !==  "l")? // false
     16ème itération :       15        non               
    Fin de la boucle FOR*/
 }
 return true; // Les deux parties sont strictement égales, cela retourne true => La chaîne est un palindrome
}

palindrome("A man, a plan, a canal. Panama");
```

#### Sans commentaires :

```js
function palindrome(str) {
 var re = /[^A-Za-z0-9]/g;
 str = str.toLowerCase().replace(re, '');
 var len = str.length;
 for (var i = 0; i < len/2; i++) {
   if (str[i] !== str[len - 1 - i]) {
       return false;
   }
 }
 return true;
}
palindrome("A man, a plan, a canal. Panama");
```

J'espère que vous avez trouvé cela utile. Cela fait partie de ma série d'articles « How to Solve FCC Algorithms » sur les défis d'algorithmes de Free Code Camp, où je propose plusieurs solutions et explique étape par étape ce qui se passe sous le capot.

[**Deux façons de confirmer la fin d'une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Confirm the Ending » de freeCodeCamp._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Trois façons d'inverser une chaîne en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Reverse a String »_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Trois façons de factoriser un nombre en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Factorialize a Number »_](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Trois façons de trouver le mot le plus long dans une chaîne en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Find the Longest Word in a String »._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Trois façons de mettre en majuscule une phrase en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Title Case a Sentence »._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

[**Trois façons de trouver le plus grand nombre dans un tableau en utilisant JavaScript**  
_Dans cet article, je vais expliquer comment résoudre le défi « Return Largest Numbers in Arrays » de Free Code Camp. Cela…_](https://www.freecodecamp.org/news/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1/)

Si vous avez votre propre solution ou des suggestions, partagez-les ci-dessous dans les commentaires.

Ou vous pouvez me suivre sur [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** et [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), juste après avoir cliqué sur le cœur vert ci-dessous ;-)


#RestezCurieux, 
#ContinuezÀCoder & 
#FaitesQueCelaArrive !

### Ressources

* [Expressions régulières — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Regular_Expressions)
* [Méthode toLowerCase() — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
* [replace() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
* [Méthode split() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
* [Méthode reverse() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
* [Méthode join() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
* [String.length — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
* [for — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for)