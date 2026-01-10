---
title: Qu'est-ce que la récursivité en JavaScript ?
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2022-11-14T18:44:18.000Z'
originalURL: https://freecodecamp.org/news/recursion-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/benjamin-semah-freecodecamp-recursion.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Recursion
  slug: recursion
seo_title: Qu'est-ce que la récursivité en JavaScript ?
seo_desc: 'Recursion is a problem-solving technique in programming. In this article,
  you will learn how to use recursive functions in JavaScript.

  What is a Recursive Function?

  A recursive function is a function that calls itself somewhere within the body of
  the...'
---

La récursivité est une technique de résolution de problèmes en programmation. Dans cet article, vous apprendrez à utiliser les fonctions récursives en JavaScript.

## Qu'est-ce qu'une fonction récursive ?

Une fonction récursive est une fonction qui s'appelle elle-même quelque part dans le corps de la fonction. Voici un exemple de base d'une fonction récursive.

```javascript
function recursiveFunc() {
  // du code ici... 
  recursiveFunc()
}
```

Comme vous pouvez le voir, la fonction `recursiveFunc` s'appelle elle-même dans le corps de la fonction. Elle continuera à s'appeler elle-même jusqu'à ce que le résultat souhaité soit atteint.

Alors, comment indiquer à la fonction quand arrêter de s'appeler elle-même ? Vous le faites en utilisant une **condition de base**.

## Les trois parties d'une fonction récursive

Chaque fois que vous écrivez une fonction récursive, trois éléments doivent être présents. Ce sont :

* La définition de la fonction.
  
* La condition de base.
  
* L'appel récursif.
  

Lorsque ces trois éléments sont manquants, votre fonction récursive ne fonctionnera pas comme vous l'attendez. Examinons chacun d'eux de plus près.

### Comment définir une fonction récursive

Vous définissez une fonction récursive de la même manière que vous définissez des fonctions JavaScript régulières.

```javascript
function recursiveFunc() {
  // du code ici...
}
```

Ce qui différencie les fonctions récursives des fonctions JavaScript régulières sont la condition de base et l'appel récursif.

### Qu'est-ce qu'une condition de base ?

Lorsque vous utilisez une fonction récursive, la condition de base est ce qui permet à la fonction de savoir quand arrêter de s'appeler elle-même. Une fois la condition de base remplie, la récursivité s'arrête.

```javascript
function recursiveFunc() {
  if(condition de base) {
    // arrête la récursivité si la condition est remplie
  }
  // sinon la récursivité continue
  recurse();
}
```

### Pourquoi avez-vous besoin d'une condition de base ?

Sans la condition de base, vous rencontrerez une récursivité infinie. Une situation où votre fonction continue à s'appeler elle-même sans s'arrêter, comme ceci :

```javascript
function doSomething(action) {
  console.log(`Je suis ${action}.`)
  doSomething(action)
}

doSomething("en cours d'exécution")
```

De plus, sans condition de base, votre fonction dépasse la taille maximale de la pile d'appels. Vous rencontrerez l'erreur montrée ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/benjamin-semah-max-callstack.PNG align="left")

*Dépassement de la taille maximale de la pile d'appels lorsqu'il n'y a pas de condition de base*

La pile d'appels garde une trace des fonctions actuellement en cours d'exécution et des fonctions qui sont à l'intérieur d'elles.

La pile d'appels a une limite. Et puisque une fonction récursive sans condition de base s'exécutera indéfiniment, elle dépasse la limite de la pile d'appels.

La condition de base fournit un moyen de sortir lorsque la fonction obtient le résultat souhaité.

### Exemple de fonction récursive

Voyons un exemple simple de fonction récursive.

```javascript
function doSomething(n) {
  if(n === 0) {
    console.log("TÂCHE TERMINÉE !")
    return
  }
  console.log("Je fais quelque chose.")
  doSomething(n - 1)
}
doSomething(3)
```

Voici le résultat lorsque vous passez le nombre `3` à la fonction `doSomething`.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/benjamin-semah-task-completed.PNG align="left")

La condition de base pour la fonction `doSomething` est `n === 0`. Chaque fois que la fonction est appelée, elle vérifie d'abord si la condition de base est remplie.

Si oui, elle imprime `TÂCHE TERMINÉE !`. Si non, elle continue avec le reste du code dans la fonction. Dans ce cas, elle imprimera `Je fais quelque chose.` puis appellera à nouveau la fonction.

### L'appel récursif

L'appel récursif est ce qui gère l'appel de la fonction elle-même à nouveau. Dans la fonction `doSomething`, l'appel récursif est la ligne ci-dessous.

```javascript
doSomething(n-1)
```

Remarquez ce qui se passe lorsque la fonction s'appelle elle-même. Un nouveau paramètre `n - 1` est passé à la fonction. À chaque itération d'un appel récursif, le paramètre sera différent de celui de l'appel précédent.

La fonction continuera à s'appeler elle-même jusqu'à ce que le nouveau paramètre satisfasse la condition de base.

## Récursivité vs Boucles

La récursivité et les boucles fonctionnent de manière similaire. Chaque fonction récursive que vous écrivez a une solution alternative avec une boucle.

Par exemple, vous pouvez créer une fonction pour trouver la factorielle d'un nombre donné en utilisant à la fois la récursivité et les boucles.

### Comment trouver la factorielle avec une boucle :

```javascript
function findFactorial(num) {
  let factorial = 1
  for (let i = num; i > 0; i--) {
    factorial *= i
  }
  return factorial
}

findFactorial(5) // 120
```

Pour trouver la factorielle en utilisant une boucle, vous initialisez d'abord une variable `factorial` avec une valeur de `1`.

Ensuite, vous initiez la boucle avec le nombre donné `num`. La boucle continuera à s'exécuter jusqu'à ce que `i > 0`.

Pour chaque itération, vous multipliez la valeur actuelle de `factorial` par `i`. Et vous diminuez la valeur de `i` de 1 jusqu'à ce que `i` ne soit plus supérieur à zéro.

Enfin, vous retournez la valeur de la factorielle lorsque la boucle a fini de s'exécuter.

### Comment trouver la factorielle avec la récursivité :

Vous pouvez créer la même solution avec une fonction récursive.

```javascript
function findFactorial(num) {
  if (num === 0) return 1
  let factorial = num * findFactorial(num - 1)
  return factorial;
}

findFactorial(5) // 120
```

Tout d'abord, vous avez besoin d'une condition de base `num === 0`.

Vous avez également besoin de l'appel récursif `findFactorial(num - 1)` pour vous assurer que le nombre continue de diminuer à chaque appel lorsque vous passez un nouveau paramètre de `n-1`.

Ensuite, vous multipliez le résultat avec le nombre précédent `num * findFactorial(num - 1)` jusqu'à ce que la condition de base soit remplie.

### Alors, lequel est le meilleur – la récursivité ou les boucles ?

Alors, lequel est le meilleur ? Il n'y a pas de bonne ou de mauvaise réponse à cela. C'est à vous de décider. Selon le problème que vous résolvez, vous pouvez choisir l'un plutôt que l'autre.

Optimisez pour la lisibilité de votre code. Parfois, comme dans l'exemple de la factorielle, la récursivité conduit à un code plus court et plus lisible.

Mais les fonctions récursives ne sont pas toujours intuitives. Si c'est le cas, vous devriez rester avec les boucles.

## Conclusion

Dans cet article, vous avez appris ce qu'est la récursivité et comment créer des fonctions récursives en JavaScript.

Lire et écrire des fonctions récursives peut être déroutant au début. Mais rappelez-vous, ce qui rend les fonctions récursives différentes des fonctions régulières sont la **condition de base** et l'**appel récursif**.

Merci d'avoir lu. Et bon codage !