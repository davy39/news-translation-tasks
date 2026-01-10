---
title: Comment fonctionne la récursion ? Simplifié en JavaScript avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-07T17:51:43.000Z'
originalURL: https://freecodecamp.org/news/recursion-in-javascript-simplified
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/recursion-js.png
tags:
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
seo_title: Comment fonctionne la récursion ? Simplifié en JavaScript avec des exemples
seo_desc: "By Dillion Megida\nRecursion works similarly to how loops do in JavaScript.\
  \ Loops allow you to execute a set of code multiple times as long as a condition\
  \ is true. \nIn this article, I will explain what Recursion is and how it works\
  \ in JavaScript.\nIn l..."
---

Par Dillion Megida

La récursion fonctionne de manière similaire aux boucles en JavaScript. Les boucles vous permettent d'exécuter un ensemble de code plusieurs fois tant qu'une condition est vraie.

Dans cet article, j'expliquerai ce qu'est la récursion et comment elle fonctionne en JavaScript.

Dans les boucles, lorsque la condition devient fausse, l'exécution s'arrête. Si la condition d'exécution reste toujours vraie, vous obtenez une **boucle infinie** qui peut faire planter votre application.

C'est la même chose avec la récursion – tant que la condition de récursion reste vraie, la récursion continue jusqu'à ce qu'une condition l'arrête, sinon, vous obtenez une **récursion infinie**.

Voici une version vidéo de ce tutoriel si vous préférez : [La récursion en JavaScript, simplifiée](https://www.youtube.com/watch?v=wCPU8iYiTbE)

Alors, plongeons dans le vif du sujet...

## Qu'est-ce que la récursion ?

La récursion est un concept où une fonction s'appelle elle-même, et continue de s'appeler jusqu'à ce qu'on lui dise de s'arrêter.

Regardons un exemple :

```js
function printHello() {
  console.log("hello")
}

printHello()
```

Ici, nous déclarons une fonction `printHello` qui affiche "hello" dans la console. Ensuite, nous appelons la fonction après sa définition.

Dans le cas de la récursion, nous pouvons également appeler la fonction `printHello` depuis l'intérieur de la fonction `printHello` elle-même, comme ceci :

```js
function printHello() {
  console.log("hello")

  printHello()
}

printHello()

// hello - premier appel de fonction
// hello - deuxième appel de fonction
// hello - troisième appel de fonction
// et cela continue à l'infini
```

C'est cela la récursion. Ainsi, lorsque JavaScript exécute `printHello()`, "hello" est affiché dans la console, puis `printHello()` est rappelé. Voici comment la récursion se produit :

- `printHello()` est exécuté la **PREMIÈRE** fois, "hello" est affiché dans la console, et juste là dans la fonction, `printHello()` est rappelé
- `printHello()` est exécuté la **DEUXIÈME** fois, `console.log("hello")` s'exécute à nouveau, et `printHello()` est rappelé
- `printHello()` est exécuté la **TROISIÈME** fois, `console.log("hello")` s'exécute à nouveau, et `printHello()` est rappelé
- et cela continue encore et encore jusqu'à ce que la pile d'appels atteigne son maximum et que l'application plante :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/call-stack-error.png)
_Erreur : Taille maximale de la pile d'appels dépassée_

Comprenons la signification de cette erreur.

## Qu'est-ce que la pile d'appels ?

La pile d'appels (call stack) est un mécanisme que JavaScript utilise pour suivre la fonction qui est en cours d'exécution.

Lorsqu'une fonction est appelée, elle est ajoutée à la pile d'appels. Par exemple, cette fonction ci-dessus :

```js
function printHello() {
  console.log("hello")
}

printHello()
```

Lorsque cette fonction doit être exécutée, elle est ajoutée à la pile d'appels :

```js
// printHello()
// ----
// pile d'appels
```

Après l'exécution (lorsque tout le code a été exécuté ou lorsqu'une instruction `return` est rencontrée), la fonction est retirée de la pile :

```js
// ----
// pile d'appels
```

Si la fonction `printHello`, par exemple, appelle une autre fonction comme ceci :

```js
function printHi() {
  console.log("hi")
}

function printHello() {
  console.log("hello")

  printHi()
}

printHello()
```

Dans ce cas, la pile d'appels ressemblera à ceci lorsque `printHello` est appelée :

```js
// printHello()
// ----
// pile d'appels
```

Après l'exécution de la ligne `console.log("hello")`, la ligne suivante est `printHi()`, et cet appel est ajouté au sommet de la pile :

```js
// printHi()
// printHello()
// ----
// pile d'appels
```

Une fois que l'appel `printHi()` a terminé son exécution, il est retiré de la pile :

```js
// printHello()
// ----
// pile d'appels
```

Une fois que `printHello()` a terminé son exécution, elle est également retirée de la pile :

```js
// ----
// pile d'appels
```

Alors, comment la récursion fonctionne-t-elle avec la pile d'appels ?

## La récursion et la pile d'appels

Revenons à notre code de récursion ci-dessus :

```js
function printHello() {
  console.log("hello")

  printHello()
}

printHello()
```

Ce qui se passe ici, c'est que lorsque `printHello()` est exécuté, il est ajouté à la pile d'appels :

```js
// printHello()
// ----
// pile d'appels
```

Le `console.log("hello")` est exécuté, puis `printHello()` est de nouveau exécuté et ajouté au sommet de la pile d'appels :

```js
// printHello()
// printHello() -- "hello"
// ----
// pile d'appels
```

Maintenant, nous avons deux fonctions actuellement dans la pile d'appels : la première `printHello` et la seconde `printHello` qui a été appelée par la première.

Pendant l'exécution de la deuxième `printHello`, `console.log("hello")` est exécuté, et `printHello` est de nouveau appelé. Maintenant, la pile ressemble à ceci :

```js
// printHello()
// printHello() -- "hello"
// printHello() -- "hello"
// ----
// pile d'appels
```

En l'état, nous n'avons aucune condition qui arrête la récursion, donc `printHello` continue de s'appeler et de remplir la pile :

```js
// ...
// printHello() -- "hello"
// printHello() -- "hello"
// printHello() -- "hello"
// printHello() -- "hello"
// printHello() -- "hello"
// printHello() -- "hello"
// ----
// pile d'appels
```

Et ensuite, nous obtenons l'erreur de taille de la pile d'appels :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/call-stack-error-1.png)
_Erreur : Taille maximale de la pile d'appels dépassée_

Pour éviter cette récursion infinie qui sature la pile d'appels, nous avons besoin d'une condition qui arrête la récursion.

## Cas général et cas de base dans la récursion

Un cas général (également appelé cas récursif) en récursion est le cas qui fait que la fonction continue de se récurser (de s'appeler elle-même).

Un cas de base en récursion est le point d'arrêt de la fonction récursive. C'est la condition que vous spécifiez pour arrêter la récursion (tout comme l'arrêt d'une boucle).

Voici un exemple :

```js
let counter = 0

function printHello() {
  console.log("hello")
  counter++
  console.log(counter)

  if (counter > 3) {
    return;
  }

  printHello()
}

printHello()
```

Ici, notre cas général n'est pas énoncé explicitement, mais implicitement : **si la variable counter N'EST PAS SUPÉRIEURE à 3, la fonction doit continuer à s'appeler**.

Tandis que le cas de base, explicitement énoncé, est : **si la variable counter EST SUPÉRIEURE à 3, la fonction doit terminer son exécution**. Ce cas entraînera le retrait de toutes les fonctions récursives de la pile d'appels, puisque la récursion est terminée.

Voici à quoi ressemblerait la pile d'appels lorsque `printHello()` est appelée pour la première fois :

```js
// printHello()
// ----
// pile d'appels
```

Ensuite, "hello" est affiché, la variable `counter` est incrémentée de 1 (ce qui la fait passer à **1**), et la variable `counter` est également affichée. Le cas de base est vérifié. "`counter` n'est pas supérieur à **3**", donc la condition n'est pas encore remplie.

La ligne suivante de la fonction est `printHello()` et dans la pile d'appels :

```js
// printHello()
// printHello() -- "hello" -- 1
// ----
// pile d'appels
```

"hello" est de nouveau affiché, et la variable `counter` est incrémentée et également affichée. Le cas de base n'est pas rempli car "`counter` n'est toujours pas supérieur à **3**". Ensuite, le `printHello()` de la deuxième fonction est appelé et la pile d'appels ressemble à ceci :

```js
// printHello()
// printHello() -- "hello" -- 2
// printHello() -- "hello" -- 1
// ----
// pile d'appels
```

Le même cycle se produit, et `printHello()` est de nouveau appelé :

```js
// printHello()
// printHello() -- "hello" -- 3
// printHello() -- "hello" -- 2
// printHello() -- "hello" -- 1
// ----
// pile d'appels
```

Après que "hello" a été affiché dans la console, `counter` est incrémenté de 1 (ce qui fait **4**). "4 est supérieur à 3", ce qui correspond à notre cas de base, donc l'instruction `return` est exécutée.

Peu importe ce que nous retournons, mais `return` arrête l'exécution d'une fonction. Cela signifie que le quatrième `printHello()` dans notre pile d'appels ne pourra pas appeler `printHello()` à nouveau car cette ligne n'est pas atteinte.

Ce qui se passe ensuite, c'est que le quatrième `printHello()` est retiré de la pile d'appels car il a terminé son exécution :

```js
// printHello() -- "hello" -- 3
// printHello() -- "hello" -- 2
// printHello() -- "hello" -- 1
// ----
// pile d'appels
```

Pour le troisième `printHello()`, après la ligne où il s'appelle lui-même, il ne reste plus rien à exécuter dans la fonction. Cela signifie donc que le troisième `printHello()` a également terminé son exécution et sera retiré de la pile d'appels :

```js
// printHello() -- "hello" -- 2
// printHello() -- "hello" -- 1
// ----
// pile d'appels
```

Même chose pour le deuxième et le premier `printHello()`, rendant ainsi la pile d'appels vide :

```js
// ----
// pile d'appels
```

Vous voyez donc comment nous avons évité une récursion infinie en fournissant un cas de base. Une fonction récursive doit avoir **AU MOINS UN CAS DE BASE** (vous pouvez en avoir autant que vous le souhaitez) pour garantir que la récursion ne s'exécute pas indéfiniment.

Il existe différentes manières d'écrire des cas de base. En voici une où le cas général est explicite, tandis que le cas de base est implicite :

```js
let counter = 0

function printHello() {
  console.log("hello")
  counter++
  console.log(counter)

  if (counter < 4) {
      printHello()
  }

  return;
}

printHello()
```

Ici, nous avons le cas général qui dit à la fonction de continuer la récursion. Le cas ici est **si counter EST INFÉRIEUR à 4**. Donc, si ce cas est rempli, la récursion continue de se produire.

Mais le cas de base, qui n'est pas aussi explicite que dans l'exemple précédent, est **si counter N'EST PLUS INFÉRIEUR à 4**, passer à la ligne suivante. Cela exécute `return` et la fonction se termine. Ensuite, tout ce qui se trouve sur la pile d'appels commence à être retiré car l'exécution est terminée.

## Conclusion

La récursion n'est pas exactement un remplacement des boucles. Mais dans certains cas, la récursion peut être plus efficace et plus facile à lire avec moins de lignes de code.

Dans cet article, vous avez appris le concept de récursion, qui se produit lorsqu'une fonction s'appelle elle-même tant qu'un cas général est rempli jusqu'à ce qu'un cas de base l'arrête. Vous avez également vu comment elle se compare aux boucles et comment elle fonctionne avec la pile d'appels.

Comme exemple concret, consultez mon article ici où j'explique [Comment trouver la factorielle d'un nombre en utilisant la récursion en JavaScript](https://dillionmegida.com/p/factorial-with-recursion-in-js)