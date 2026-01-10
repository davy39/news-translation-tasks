---
title: Que signifie l'erreur "Maximum call stack exceeded" ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-30T07:56:07.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-maximum-call-stack-stack-exceeded-error-mean
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/29-maximum-call-stack-exceeded.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: Que signifie l'erreur "Maximum call stack exceeded" ?
seo_desc: 'By Dillion Megida

  Have you ever gotten an error similar to this? This error occurs because the call
  stack has exceeded its limit. But what does this mean?

  First, let''s understand what the call stack is.

  The Call Stack

  The call stack is a data structu...'
---

Par Dillion Megida

Avez-vous déjà obtenu une erreur similaire à celle-ci ? Cette erreur se produit parce que la pile d'appels a dépassé sa limite. Mais que signifie cela ?

Tout d'abord, comprenons ce qu'est la pile d'appels.

## La pile d'appels

La pile d'appels est une structure de données en JavaScript qui contient la ou les fonctions en cours d'exécution. Cette structure est au format dernier entré, premier sorti. Voici un exemple :

```js
function printName() {
  console.log("Dillion")
}

printName()
// Dillion
```

Au début, la pile d'appels est vide. Lorsque `printName` est déclarée, la pile d'appels est toujours vide. Lorsque `printName()` doit être exécutée, elle est ajoutée à la pile d'appels :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-47.png)

Lorsque la fonction est terminée, elle est retirée de la pile d'appels. La fin de la fonction se produit lorsque :

* toutes les lignes de la fonction ont été exécutées OU
* une instruction `return` est rencontrée dans la fonction

De cette manière, la pile d'appels peut suivre quelle fonction est actuellement en cours d'exécution, et depuis quel contexte.

Voici un autre exemple :

```js
function printName() {
  function printFirstName() {
    console.log("Dillion")
  }
  
  function printLastName() {
    console.log("Megida")
  }
  
  printFirstName()
  printLastName()
  
  console.log("Dillion Megida")
  
}

printName()
// "Dillion"
// "Megida"
// "Dillion Megida"
```

Dans cet exemple, nous avons déclaré une fonction appelée `printName`. Dans cette fonction, nous déclarons deux autres fonctions : `printFirstName` et `printLastName`. Les deux fonctions sont appelées, puis l'instruction `console.log("Dillion Megida")`.

Lorsque `printName()` doit être exécutée, elle est ajoutée à la pile d'appels :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-49.png)

Dans `printName()`, lorsque `printFirstName()` doit être exécutée, elle est également ajoutée à la pile d'appels (au-dessus de `printName()` car elle n'a pas encore terminé son exécution) :


![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-53.png)

Après que `printFirstName()` a terminé son exécution (qui enregistre "Dillion" dans la console), elle est retirée de la pile d'appels. `printLastName()` doit maintenant être exécutée, donc elle est ajoutée à la pile d'appels :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-51.png)

Après l'exécution de `printLastName()` (qui enregistre "Megida" dans la console), elle est retirée de la pile d'appels :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-52.png)

`printName()` continue son exécution qui exécute maintenant `console.log("Dillion Megida")`. Vous pouvez voir "Dillion Megida" dans la console. `printName()` est maintenant terminée, et retirée de la pile d'appels :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-54.png)

C'est ainsi que la pile d'appels fonctionne pour suivre la ou les fonctions actuelles en cours d'exécution. Mais la pile d'appels a une taille maximale. Lorsque vous avez plus de fonctions que ce qui est autorisé dans la pile d'appels, vous obtenez l'erreur **maximum call stack size exceeded**.

Un cas populaire dans lequel vous pouvez dépasser la taille maximale de la pile d'appels est la **récursivité**

J'ai une [vidéo expliquant cela](https://youtu.be/D71LzJBdaKw) que vous pouvez également consulter.

## Récursivité et la pile d'appels

Regardez cet exemple :

```js
function printNames() {
  console.log("Dillion")
  
  printNames()
  
  console.log("Megida")
}

printNames()
// "Dillion" - premier appel
// "Dillion" - deuxième appel
// "Dillion" - troisième appel
// "Dillion" - quatrième appel
// "Dillion" - cinquième appel
// et ainsi de suite, jusqu'au maximum
```

Dans cet exemple, nous avons déclaré `printNames`. Dans cette fonction, nous avons d'abord `console.log("Dillion")`, puis nous avons `printNames()`.

Voyons ce qui se passe lorsque nous appelons `printNames()` après la déclaration de la fonction.

`printNames()`--celui-ci est ajouté à la pile d'appels :


![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-55.png)

`console.log("Dillion")` est exécuté. "Dillion" est enregistré dans la console. Ensuite, `printNames()` est exécuté à nouveau, qui est ajouté à la pile d'appels en tant que fonction active :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-56.png)

Nous avons maintenant deux fonctions dans la pile d'appels. Le premier appel de `printNames` et le deuxième appel de `printNames` qui est appelé depuis le premier.

Dans ce deuxième appel de la fonction, `console.log("Dillion")` est exécuté ce qui enregistre "Dillion" dans la console. Ensuite, la ligne `printNames()` est exécutée à nouveau. Un troisième appel, qui est ajouté à la pile d'appels en tant que fonction active :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-57.png)

Maintenant, nous avons trois fonctions dans la pile d'appels. Comme rien n'arrête ces appels de fonction, cela va se produire indéfiniment jusqu'à ce que "la pile d'appels ne puisse plus le supporter" 😂:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-58.png)

La pile d'appels a une taille maximale de fonctions qu'elle peut contenir en même temps. Cette taille peut être différente dans différents navigateurs. Lorsque cette taille est dépassée, vous obtenez l'erreur **maximum call stack size exceeded**.

Cela rendrait également votre application JavaScript non réactive. Et vous ne voulez définitivement pas cela pour vos utilisateurs.

Lorsque vous créez des récursivités dans vos programmes JavaScript, vous devez également avoir un **cas de base**, qui termine les récursivités après quelques appels. Cela est important afin de ne pas dépasser la taille de la pile d'appels et faire planter votre application.

Voici un exemple de cas de base :

```js
let counter = 0;

function printNames() {
  console.log("Dillion")
  counter++
  
  if (counter < 5) {
    printNames()
  }
  
  console.log("Megida")
}

printNames()

// Dillion
// Dillion
// Dillion
// Dillion
// Dillion
// Megida
// Megida
// Megida
// Megida
// Megida
```

J'ai mis à jour le code pour inclure un cas de base. Le cas de base ici est que "si la variable counter n'est plus inférieure à 5, arrêter la récursivité". Donc lorsque la fonction est appelée, `printNames()` est ajoutée à la pile d'appels. Nous avons `counter` à 0, puis nous enregistrons "Dillion" dans la console. Après cela, nous augmentons `counter` de 1. Nous avons ensuite la condition "si counter est inférieur à 5". Comme `counter` est inférieur à 5, nous exécutons `printNames()`.

Maintenant, la pile d'appels contient les premier et deuxième appels de `printNames()`.

Au cinquième appel de `printNames`, la pile d'appels contiendra 5 appels de `printNames()` :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-59.png)

Rappelez-vous que les quatre premiers appels de fonction ne sont pas terminés. Avant qu'ils ne se terminent, ils ont appelé une autre fonction qui a été ajoutée à la pile d'appels.

À ce cinquième appel, "Dillion" est enregistré dans la console pour la cinquième fois. `counter`, à 4, est incrémenté de 1 à 5. Ensuite, la condition "si counter est inférieur à 5" est vérifiée. `counter` (à 5) n'est pas inférieur à 5, donc c'est le cas de base qui **dit à la récursivité de s'arrêter**.

Comme la fonction ne s'appelle pas elle-même à nouveau, elle passe à la ligne suivante.

Ensuite, la ligne suivante dans la fonction est exécutée, qui est `console.log("Megida")`. Après cette ligne, la cinquième fonction dans la pile d'appels termine son exécution et quitte maintenant la pile d'appels.

Maintenant que la cinquième fonction a terminé son exécution, la quatrième fonction peut continuer là où elle s'est arrêtée. La ligne suivante dans la quatrième fonction est `console.log("Megida")` qui enregistre "Megida" dans la console lorsqu'elle est exécutée. Ensuite, la quatrième fonction quitte la pile :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-60.png)

Et les fonctions restantes dans la pile termineront leur exécution jusqu'à ce que la pile devienne vide :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-61.png)

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-62.png)

## Conclusion

Lorsque vous rencontrez l'erreur "Maximum call stack exceeded", la signification simple est que "la pile d'appels contient maintenant plus de fonctions actives qu'elle ne peut en contenir".

La pile d'appels stocke la ou les fonctions actuellement en cours d'exécution. Lorsque trop de fonctions sont exécutées, la pile d'appels peut dépasser sa taille et générer une erreur. Cela se produit généralement dans les cas de récursivités qui n'ont pas de cas de base.

Si vous avez aimé cet article, partagez-le avec d'autres :)