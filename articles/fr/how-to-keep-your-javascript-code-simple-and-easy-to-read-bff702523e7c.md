---
title: Comment garder votre code JavaScript simple et facile à lire
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T17:25:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-your-javascript-code-simple-and-easy-to-read-bff702523e7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ecVfURF6VRf5Yxf2yaRteg.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment garder votre code JavaScript simple et facile à lire
seo_desc: 'By Arthur Arakelyan

  There are many ways to solve the same problem, but some solutions are complex, and
  some are even ridiculous. In this article, I want to talk about bad and good solutions
  for the same problems.

  Let’s start with the problem that req...'
---

Par Arthur Arakelyan

Il existe de nombreuses façons de résoudre le même problème, mais certaines solutions sont complexes, et d'autres sont même ridicules. Dans cet article, je veux parler des mauvaises et des bonnes solutions pour les mêmes problèmes.

Commençons par le problème qui nous oblige à supprimer les valeurs en double d'un tableau.

#### **Complexe - Suppression des doublons en utilisant forEach**

Tout d'abord, nous créons un nouveau tableau vide, puis nous utilisons la méthode [**forEach()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) pour exécuter une fonction fournie une fois pour chaque élément du tableau. Finalement, nous vérifions si la valeur n'existe pas dans le nouveau tableau, et si ce n'est pas le cas, nous l'ajoutons.

```
function removeDuplicates(arr) {     const uniqueVals = [];      arr.forEach((value,index) => {            if(uniqueVals.indexOf(value) === -1) {           uniqueVals.push(value);       }     });  return uniqueVals;}
```

#### **Simple - Suppression des doublons en utilisant filter**

La méthode [**filter**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) crée un nouveau tableau avec tous les éléments qui passent le test implémenté par la fonction fournie. Basiquement, nous itérons sur le tableau et, pour chaque élément, nous vérifions si la première position de cet élément dans le tableau est égale à la position actuelle. Bien sûr, ces deux positions sont différentes pour les éléments en double.

```
function removeDuplicates(arr) {  return arr.filter((item, pos) => arr.indexOf(item) === pos)}
```

#### **Simple - Suppression des doublons en utilisant Set**

ES6 fournit l'objet [**Set**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set), qui simplifie grandement les choses. **Set** n'autorise que les valeurs uniques, donc lorsque vous passez un tableau, il supprime toutes les valeurs en double.

Cependant, si vous avez besoin d'un tableau avec des éléments uniques, pourquoi ne pas utiliser **Set** dès le début ?

```
function removeDuplicates(arr) {   return [...new Set(arr)];}
```

Passons à la résolution du deuxième problème qui nous oblige à écrire une fonction qui prend un tableau d'entiers non négatifs distincts, les rend consécutifs et retourne le nombre de nombres manquants.

Pour `const arr = [4, 2, 6, 8]`, le résultat devrait être  
`countMissingNumbers(arr) = 3`

Comme vous pouvez le voir, `3`, `5` et `7` sont manquants.

#### **Complexe - Résolution en utilisant sort et for loop**

Pour obtenir les plus petits et les plus grands nombres, nous devons les [**trier**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) par ordre croissant, et à cette fin, nous utilisons la méthode `sort`. Ensuite, nous bouclons du plus petit nombre au plus grand nombre. Chaque fois, nous vérifions si un nombre séquentiel existe dans le tableau ou non, et si ce n'est pas le cas, nous augmentons le compteur.

```
function countMissingNumbers(arr) {    arr.sort((a,b) => a-b);        let count = 0;        const min = arr[0];        const max = arr[arr.length-1];    for (i = min; i<max; i++) {      if (arr.indexOf(i) === -1) {          count++;               }          }            return count;}
```

#### **Simple - Résolution en utilisant Math.max et Math.min**

Cette solution a une explication simple : la fonction `[**Math.max()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max)` retourne le plus grand nombre dans le tableau et la fonction `[**Math.min()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min)` retourne le plus petit nombre dans le tableau.

Tout d'abord, nous déterminons combien de nombres il y aurait dans le tableau s'il n'y avait pas de nombres manquants. Pour cela, nous utilisons la formule suivante `maxNumber - minNuber + 1`, et la différence entre le résultat de celle-ci et la longueur du tableau nous donnera le nombre de nombres manquants.

```
function countMissingNumbers(arr) {      return Math.max(...arr) - Math.min(...arr) + 1 - arr.length;}
```

Le dernier problème que je veux aborder en exemple est de vérifier si la chaîne est un **palindrome** ou non.

_*Un **palindrome** est une chaîne qui se lit de la même manière de gauche à droite et de droite à gauche._

#### **Complexe - Vérification en utilisant for loop**

Dans cette option, nous bouclons sur la chaîne en commençant par le premier caractère jusqu'à la moitié de la longueur de la chaîne. L'index du dernier caractère dans une chaîne est string.length-1, l'avant-dernier caractère est string.length-2, et ainsi de suite. Ici, nous vérifions si le caractère à l'index spécifié depuis le début est égal au caractère à l'index spécifié à la fin. S'ils ne sont pas égaux, nous retournons false.

```
function checkPalindrome(inputString) {    let length = inputString.length   for (let i =0; i<length / 2; i++) {        if (inputString[i] !== inputString[length - 1 -i]) {             return false                }   }  return true}
```

#### **Simple - Vérification en utilisant reverse et join**

Je pense que cette solution simple ne nécessite pas d'explication, car elle parle d'elle-même. Nous créons simplement un tableau à partir de la chaîne en utilisant l'[**opérateur de décomposition**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax), puis nous [**inversons**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse) le tableau, puis nous le transformons à nouveau en une chaîne en utilisant la méthode [**join**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join) et nous le comparons avec la chaîne originale.

```
function checkPalindrome(string) {   return string === [...string].reverse().join('');}
```

#### Gardez cela simple !

Pourquoi compliquer quand il existe des moyens plus simples ? J'espère que vous avez trouvé cet article intéressant. Passez une bonne journée et essayez de ne pas compliquer les choses simples de la vie également :)

Merci pour vos applaudissements 👏