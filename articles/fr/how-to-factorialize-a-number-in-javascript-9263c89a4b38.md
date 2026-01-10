---
title: Trois façons de factoriser un nombre en JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-03-16T11:51:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uKMWUxeIBoqzbgBNRHiyjQ.jpeg
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
seo_title: Trois façons de factoriser un nombre en JavaScript
seo_desc: 'This article is based on Free Code Camp Basic Algorithm Scripting “Factorialize
  a Number”

  In mathematics, the factorial of a non-negative integer n can be a tricky algorithm.
  In this article, I’m going to explain three approaches, first with the recu...'
---

_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « [Factorialize a Number](https://www.freecodecamp.com/challenges/factorialize-a-number) »_

**En mathématiques**, la factorielle d'un entier non négatif _n_ peut être un algorithme délicat. Dans cet article, je vais expliquer trois approches, d'abord avec la fonction récursive, ensuite en utilisant une boucle while et enfin avec une boucle for.

Nous avons déjà vu une approche récursive sur une chaîne de caractères dans l'article précédent, [**Comment inverser une chaîne de caractères en JavaScript de 3 manières différentes ?**](https://medium.com/@sonya.moisset/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb#.ekpftot4d) Cette fois, nous allons appliquer le même concept à un nombre.

#### Défi de l'algorithme

> Retournez la factorielle de l'entier fourni.  
>   
> Si l'entier est représenté par la lettre n, une factorielle est le produit de tous les entiers positifs inférieurs ou égaux à n.  
>   
> Les factorielles sont souvent représentées avec la notation abrégée **n!**  
>   
> Par exemple : **5! = 1 * 2 * 3 * 4 * 5 = 120**

```js

function factorialize(num) {
  return num;
}
factorialize(5);
```

#### _Cas de test fournis_

* **_factorialize(0)_** devrait retourner 1
* **_factorialize(5)_** devrait retourner 120
* **_factorialize(10)_** devrait retourner 3628800
* **_factorialize(20)_** devrait retourner 2432902008176640000

### Qu'est-ce que la factorisation d'un nombre ?

Lorsque vous factorisez un nombre, vous multipliez ce nombre par chaque nombre consécutif moins un.

Si votre nombre est 5, vous auriez :

```
5! = 5 * 4 * 3 * 2 * 1
```

Le schéma serait :

```
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2 * 1
4! = 4 * 3 * 2 * 1
5! = 5 * 4 * 3 * 2 * 1
```

### 1. Factoriser un nombre avec la récursion

```js
function factorialize(num) {
  // Si le nombre est inférieur à 0, rejetez-le.
  if (num < 0) 
        return -1;
    
  // Si le nombre est 0, sa factorielle est 1.
  else if (num == 0) 
      return 1;
    
  // Sinon, appelez à nouveau la procédure récursive
    else {
        return (num * factorialize(num - 1));
        /* 
        Première partie de la méthode de récursion
        Vous devez vous souvenir que vous n'aurez pas qu'un seul appel, vous aurez plusieurs appels imbriqués
        
        Chaque appel : num === "?"        	         num * factorialize(num - 1)
        1er appel – factorialize(5) retournera    5  * factorialize(5 - 1) // factorialize(4)
        2e appel – factorialize(4) retournera    4  * factorialize(4 - 1) // factorialize(3)
        3e appel – factorialize(3) retournera    3  * factorialize(3 - 1) // factorialize(2)
        4e appel – factorialize(2) retournera    2  * factorialize(2 - 1) // factorialize(1)
        5e appel – factorialize(1) retournera    1  * factorialize(1 - 1) // factorialize(0)
        
        Deuxième partie de la méthode de récursion
        La méthode atteint la condition si, elle retourne 1 que num multipliera par lui-même
        La fonction quittera avec la valeur totale
        
        5e appel retournera (5 * (5 - 1))     // num = 5 * 4
        4e appel retournera (20 * (4 - 1))    // num = 20 * 3
        3e appel retournera (60 * (3 - 1))    // num = 60 * 2
        2e appel retournera (120 * (2 - 1))   // num = 120 * 1
        1er appel retournera (120)             // num = 120
        
        Si nous résumons tous les appels en une ligne, nous avons
        (5 * (5 - 1) * (4 - 1) * (3 - 1) * (2 - 1)) = 5 * 4 * 3 * 2 * 1 = 120
        */
    }
}
factorialize(5);
```

#### Sans commentaires :

```js
function factorialize(num) {
  if (num < 0) 
        return -1;
  else if (num == 0) 
      return 1;
  else {
      return (num * factorialize(num - 1));
  }
}
factorialize(5);
```

### 2. Factoriser un nombre avec une boucle WHILE

```js
function factorialize(num) {
  // Étape 1. Créer une variable result pour stocker num
  var result = num;
   
  // Si num = 0 OU num = 1, la factorielle retournera 1
  if (num === 0 || num === 1) 
    return 1; 
 
  // Étape 2. Créer la boucle WHILE 
  while (num > 1) { 
    num--; // décrémentation de 1 à chaque itération
    result = result * num; // ou result *= num; 
    /* 
                    num           num--      var result      result *= num         
    1ère itération:   5             4            5             20 = 5 * 4      
    2e itération:   4             3           20             60 = 20 * 3
    3e itération:   3             2           60            120 = 60 * 2
    4e itération:   2             1          120            120 = 120 * 1
    5e itération:   1             0          120
    Fin de la boucle WHILE 
    */
  }
     
  // Étape 3. Retourner la factorielle de l'entier fourni
  return result; // 120
}
factorialize(5);
```

#### Sans commentaires :

```js
function factorialize(num) {
  var result = num;
  if (num === 0 || num === 1) 
    return 1; 
  while (num > 1) { 
    num--;
    result *= num;
  }
  return result;
}
factorialize(5);
```

### 3. Factoriser un nombre avec une boucle FOR

```js
function factorialize(num) {
  // Si num = 0 OU num = 1, la factorielle retournera 1
  if (num === 0 || num === 1)
    return 1;
  
  // Nous commençons la boucle FOR avec i = 4
  // Nous décrémentons i après chaque itération 
  for (var i = num - 1; i >= 1; i--) {
    // Nous stockons la valeur de num à chaque itération
    num = num * i; // ou num *= i;
    /* 
                    num      var i = num - 1       num *= i         i--       i >= 1?
    1ère itération:   5           4 = 5 - 1         20 = 5 * 4        3          yes   
    2e itération:  20           3 = 4 - 1         60 = 20 * 3       2          yes
    3e itération:  60           2 = 3 - 1        120 = 60 * 2       1          yes  
    4e itération: 120           1 = 2 - 1        120 = 120 * 1      0          no             
    5e itération: 120               0                120
    Fin de la boucle FOR 
    */
  }
  return num; //120
}
factorialize(5);
```

#### Sans commentaires :

```js
function factorialize(num) {
  if (num === 0 || num === 1)
    return 1;
  for (var i = num - 1; i >= 1; i--) {
    num *= i;
  }
  return num;
}
factorialize(5);
```

J'espère que vous avez trouvé cela utile. Cela fait partie de ma série d'articles « Comment résoudre les algorithmes FCC » sur les défis d'algorithmes de Free Code Camp, où je propose plusieurs solutions et explique étape par étape ce qui se passe sous le capot.

[**Trois façons de répéter une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Repeat a string repeat a string » de freeCodeCamp. Cela implique..._](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Deux façons de confirmer la fin d'une chaîne en JavaScript**  
_Dans cet article, j'explique comment résoudre le défi « Confirm the Ending » de freeCodeCamp._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Trois façons d'inverser une chaîne en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Reverse a String »_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Deux façons de vérifier les palindromes en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Check for Palindromes »._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Trois façons de trouver le mot le plus long dans une chaîne en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Find the Longest Word in a String »._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Trois façons de mettre en majuscule une phrase en JavaScript**  
_Cet article est basé sur Free Code Camp Basic Algorithm Scripting « Title Case a Sentence »._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

[**Trois façons de trouver le plus grand nombre dans un tableau en utilisant JavaScript**  
_Dans cet article, je vais expliquer comment résoudre le défi « Return Largest Numbers in Arrays » de Free Code Camp. Cela..._](https://medium.freecodecamp.com/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1)

Si vous avez votre propre solution ou des suggestions, partagez-les ci-dessous dans les commentaires.

Ou vous pouvez me suivre sur [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** et [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), juste après avoir cliqué sur le cœur vert ci-dessous ;-)


#RestezCurieux, 
#ContinuezÀCoder & 
#FaitesQueCelaArrive!