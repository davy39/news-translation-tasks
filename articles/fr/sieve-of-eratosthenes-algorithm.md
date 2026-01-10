---
title: Comment utiliser l'algorithme du Crible d'Ératosthène
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-12T18:25:20.000Z'
originalURL: https://freecodecamp.org/news/sieve-of-eratosthenes-algorithm
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Sieve-of-Eratosthenes-min.png
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser l'algorithme du Crible d'Ératosthène
seo_desc: 'By Divine Orji

  One day, while learning algorithms in JavaScript, I found this challenge:


  Using a for loop, iterate from 0 to 100, and return an array of all prime numbers
  within that range.


  It seemed easy initially, but I couldn''t quite figure it o...'
---

Par Divine Orji

Un jour, en apprenant les algorithmes en JavaScript, j'ai trouvé ce défi :

> En utilisant une boucle `for`, itérer de 0 à 100, et retourner un tableau de tous les nombres premiers dans cette plage.

Cela semblait facile au début, mais je n'arrivais pas à le résoudre. J'ai donc fait une recherche Google et j'ai découvert un algorithme qui le fait parfaitement : le **Crible d'Ératosthène**.

## Qu'est-ce que ce _crible_ dont vous parlez ?

Le Crible d'Ératosthène est un ancien algorithme mathématique créé par [Ératosthène de Cyrène](https://en.wikipedia.org/wiki/Eratosthenes). Il trouve tous les nombres premiers entre 0 et une limite donnée.

## Intéressant ! Comment fonctionne le Crible d'Ératosthène ?

Décomposons-le :

* Notre entrée est un nombre positif représentant la limite.
* L'algorithme parcourt tous les nombres entre 0 et notre entrée.
* À chaque itération, si le nombre est un nombre premier, il marque tous les multiples de ce nombre comme non-premiers.

Cool, non ? Maintenant, résolvons notre défi initial :

```jsx
function getPrimes(input) {
  // Créer un tableau où chaque élément commence comme vrai
  const numsArr = Array.from({ length: input + 1 }, () => true);

  // Créer un tableau pour stocker les nombres premiers
  const primeNumbers = [];

  /*
  Parcourir numsArr en commençant par numsArr[2]
  car 0 et 1 ne sont définitivement pas des nombres premiers
  */
  for (let i = 2; i <= input; i++) {
    // Vérifier si numsArr[i] === true
    if (numsArr[i]) {
      // ajouter i au tableau primeNumbers
      primeNumbers.push(i);

      /* 
      convertir tous les éléments dans numsArr 
      dont les index sont des multiples de i 
      en false
      */
      for (let j = i + i; j <= input; j += i) {
        numsArr[j] = false;
      }
    }
  }

  return primeNumbers;
}

console.log(getPrimes(100));

```

Dans le code ci-dessus, nous avons fait ce qui suit :

* Créé un tableau d'éléments `true`. Les tableaux JavaScript sont indexés à partir de zéro, donc nous avons défini `length: input + 1` pour en tirer avantage.
* Créé `primeNumbers[]` pour stocker les nombres premiers.
* Utilisé une boucle `for` pour itérer sur chaque élément dans `numsArr[]`. Si l'élément actuel est `true`, ajoutez-le à `primeNumbers[]` et convertissez tous les éléments en multiples de son index en `false`.
* Retourné `primeNumbers[]`, qui contient maintenant tous les nombres premiers entre 0 et notre entrée.

Donc, cela fonctionne, mais il y a un léger problème (ou un problème majeur, selon la taille de l'entrée). À un moment donné pendant la boucle, tous les non-premiers possibles dans le tableau sont déjà `false`, mais atteindre un élément `true` déclenche toujours sa boucle imbriquée. C'est redondant !

Optimisons :

```jsx
// Algorithme du Crible d'Ératosthène

function getPrimes(input) {
  // Créer un tableau où chaque élément commence comme vrai
  const numsArr = Array.from({ length: input + 1 }, () => true);

  // Parcourir numsArr en commençant par numsArr[2]
  // continuer à exécuter la boucle jusqu'à ce que i soit supérieur à la racine carrée de l'entrée
  for (let i = 2; i <= Math.floor(Math.sqrt(input)); i++) {
    // Vérifier si numsArr[i] === true
    if (numsArr[i]) {
      /* 
      convertir tous les éléments dans numsArr 
      dont les index sont des multiples de i 
      en false
      */
      for (let j = i + i; j <= input; j += i) {
        numsArr[j] = false;
      }
    }
  }

  /*
  Utilisation de la méthode Array.prototype.reduce() :
    parcourir chaque élément dans numsArr[]
      si element === true, 
      ajouter l'index de cet élément à result[]
      retourner result
  */
  const primeNumbers = numsArr.reduce(
    (result, element, index) =>
      element ? (result.push(index), result) : result,
    []
  );

  // Retourner primeNumbers[]
  return primeNumbers;
}

console.log(getPrimes(100));

```

Que se passe-t-il dans le code ci-dessus ?

Mathématiquement, il est impossible d'obtenir de nouveaux multiples au-delà de la racine carrée d'une entrée donnée.

Pour le dire simplement, au moment où nous atteignons la racine carrée de `input`, tous les multiples possibles dans `numsArr[]` auraient déjà été convertis en `false`, donc il n'est pas nécessaire de continuer à vérifier les multiples.

Donc, voici ce que nous avons fait :

* Mis à jour la boucle `for` pour qu'elle se termine lorsque `i <= Math.floor(Math.sqrt(input))` est faux.
* Utilisé la méthode `reduce()` de JavaScript pour parcourir `numsArr[]` et retourner un tableau contenant l'`index` de tous les éléments `true`.

**Fait amusant :** Cette optimisation fonctionnera également si nous remplaçons la première boucle `for` par :

```jsx
// continuer à exécuter la boucle jusqu'à ce que input soit inférieur à i^2 (i au carré)
for (let i = 2; i * i <= input; i++) {
  // même code super-génial hihihi !
}

```

Essayez-le !

## Bien ! Y a-t-il des limitations au Crible d'Ératosthène ? 👀

Le Crible d'Ératosthène fonctionne efficacement avec de petites entrées - `n < 10 millions` (_est-ce que 10 millions est petit ???_). Cependant, des entrées plus grandes prennent beaucoup de temps et de mémoire. Le [crible segmenté](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#:~:text=usually%20the%20case.-,Segmented%20sieve,-%5Bedit%5D) est une solution proposée à ce problème.

## Quelques mots pour conclure

Il existe différentes versions de cet algorithme, chacune abordant certaines des limitations de l'original.

Apprendre cet algorithme a élargi mes connaissances sur les boucles imbriquées, les nombres premiers et la complexité temporelle. Pour explorer ces sujets en profondeur, consultez les ressources ci-dessous.