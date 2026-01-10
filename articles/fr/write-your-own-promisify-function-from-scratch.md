---
title: Comment écrire votre propre fonction Promisify à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-22T06:39:48.000Z'
originalURL: https://freecodecamp.org/news/write-your-own-promisify-function-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/write.jpg
tags:
- name: callbacks
  slug: callbacks
- name: interview questions
  slug: interview-questions
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: promises
  slug: promises
seo_title: Comment écrire votre propre fonction Promisify à partir de zéro
seo_desc: 'By Shailesh Shekhawat

  Introduction

  In this article, you will learn how to write your own promisify function from scratch.

  Promisification helps in dealing with callback-based APIs while keeping code consistent
  with promises.

  We could just wrap any fu...'
---

Par Shailesh Shekhawat

### Introduction

Dans cet article, vous apprendrez à écrire votre propre fonction promisify à partir de zéro.

La promisification aide à gérer les API basées sur les callbacks tout en gardant le code cohérent avec les promesses.

Nous pourrions simplement envelopper n'importe quelle fonction avec `new Promise()` et ne plus nous en soucier. Mais faire cela lorsque nous avons de nombreuses fonctions serait redondant.

Si vous comprenez les promesses et les callbacks, alors apprendre à écrire des fonctions promisify devrait être facile. Alors commençons.

### Mais vous êtes-vous déjà demandé comment promisify fonctionne ?

> L'important est de ne pas cesser de questionner. La curiosité a sa propre raison d'exister.
> 
> — Albert Einstein

Les promesses ont été introduites dans la [Norme ECMA-262, 6ème Édition](http://www.ecma-international.org/ecma-262/6.0/) (ES6) publiée en juin 2015.

C'était une amélioration significative par rapport aux callbacks, comme nous savons tous à quel point le "callback hell" peut être illisible :)

![Image](https://www.freecodecamp.org/news/content/images/2019/12/callback-1.gif)

En tant que développeur Node.js, vous devriez savoir [ce qu'est une promesse](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-promise-27fc71e77261) et [comment elle fonctionne en interne](https://101node.io/blog/how-promises-actually-work-inside-out/), ce qui vous aidera également lors des entretiens JS. N'hésitez pas à les réviser rapidement avant de continuer.

### Pourquoi devons-nous convertir les callbacks en promesses ?

1. Avec les callbacks, si vous voulez faire quelque chose de manière séquentielle, vous devrez spécifier un argument `err` dans chaque callback, ce qui est redondant. Dans les promesses ou async-await, vous pouvez simplement ajouter une méthode ou un bloc `.catch` qui attrapera toutes les erreurs survenues dans la chaîne de promesses.
2. Avec les callbacks, vous n'avez aucun contrôle sur quand il est appelé, dans quel contexte, ou combien de fois il est appelé, ce qui peut entraîner des fuites de mémoire.
3. En utilisant les promesses, nous contrôlons ces facteurs (surtout la gestion des erreurs) donc le code est plus lisible et maintenable.

## Comment faire en sorte que les fonctions basées sur les callbacks retournent une promesse

Il y a deux façons de le faire :

1. Envelopper la fonction dans une autre fonction qui retourne une promesse. Elle résout ou rejette ensuite en fonction des arguments du callback.
2. Promisification — Nous créons une fonction utilitaire/aide `promisify` qui transformera toutes les API basées sur les callbacks avec erreur en premier.

Exemple : il y a une API basée sur les callbacks qui fournit la somme de deux nombres. Nous voulons la promisifier pour qu'elle retourne une promesse `thenable`.

```js
const getSumAsync = (num1, num2, callback) => {
 
  if (!num1 || !num2) {
    return callback(new Error("Arguments manquants"), null);
  }
  return callback(null, num1 + num2);
}
getSumAsync(1, 1, (err, result) => {
  if (err){
    doSomethingWithError(err)
  }else {
    console.log(result) // 2
  }
})
```

### Envelopper dans une promesse

Comme vous pouvez le voir, `getSumPromise` délègue tout le travail à la fonction originale `getSumAsync`, fournissant son propre callback qui se traduit par une promesse `resolve/reject`.

### Promisify

Lorsque nous devons promisifier de nombreuses fonctions, nous pouvons créer une fonction auxiliaire `promisify`.

### Qu'est-ce que la Promisification ?

La promisification signifie transformation. C'est une conversion d'une fonction qui accepte un callback en une fonction retournant une promesse.

En utilisant `util.promisify()` de Node.js :

```
const { promisify } = require('util')
const getSumPromise = promisify(getSumAsync) // étape 1
getSumPromise(1, 1) // étape 2
.then(result => {
  console.log(result)
})
.catch(err =>{
  doSomethingWithError(err);
})
```

Ainsi, cela ressemble à une fonction magique qui transforme `getSumAsync` en `getSumPromise` qui a les méthodes `.then` et `.catch`.

### Écrivons notre propre fonction promisify :

Si vous regardez l'**étape 1** dans le code ci-dessus, la fonction `promisify` accepte une fonction comme argument, donc la première chose que nous devons faire est d'écrire une fonction qui peut faire la même chose :

```
const getSumPromise = myPromisify(getSumAsync)
const myPromisify = (fn) => {}
```

Après cela, `getSumPromise(1, 1)` est un appel de fonction. Cela signifie que notre promisify devrait retourner une autre fonction qui peut être appelée avec les mêmes arguments que la fonction originale :

```
const myPromisify = (fn) => {
 return (...args) => {
 }
}
```

Dans le code ci-dessus, vous pouvez voir que nous étalons les arguments car nous ne savons pas combien d'arguments la fonction originale a. `args` sera un tableau contenant tous les arguments.

Lorsque vous appelez `getSumPromise(1, 1)`, vous appelez en réalité `(...args)=> {}`. Dans l'implémentation ci-dessus, elle retourne une promesse. C'est pourquoi vous pouvez utiliser `getSumPromise(1, 1).then(..).catch(..)`.

J'espère que vous avez compris l'indice que la fonction wrapper `(...args) => {}` devrait retourner une promesse.

### Retourner une promesse

```
const myPromisify = (fn) => {
  return (...args) => {
    return new Promise((resolve, reject) => {
      
    })
  }
}
```

Maintenant, la partie délicate est de décider quand `résoudre ou rejeter` une promesse.
En fait, cela sera décidé par l'implémentation de la fonction originale `getSumAsync` — elle appellera la fonction de callback originale et nous devons simplement la définir. Ensuite, en fonction de `err` et `result`, nous `rejetterons` ou `résoudrons` la promesse.

```
const myPromisify = (fn) => {
  return (...args) => {
    return new Promise((resolve, reject) => {
      function customCallback(err, result) {
       if (err) {
         reject(err)
       }else {
         resolve(result);
        }
      }
   })
  }
}
```

Notre `args[]` ne contient que les arguments passés par `getSumPromise(1, 1)` à l'exception de la fonction de callback. Vous devez donc ajouter `customCallback(err, result)` à `args[]` que la fonction originale `getSumAsync` appellera en conséquence car nous suivons le résultat dans `customCallback`.

### Ajouter customCallback à args[]

```
const myPromisify = (fn) => {
   return (...args) => {
     return new Promise((resolve, reject) => {
       function customCallback(err, result) {
         if (err) {
           reject(err)
         }else {
          resolve(result);
         }
        }
        args.push(customCallback)
        fn.call(this, ...args)
      })
  }
}
```

Comme vous pouvez le voir, nous avons ajouté `fn.call(this, args)`, qui appellera la fonction originale dans le même contexte avec les arguments `getSumAsync(1, 1, customCallback)`. Ensuite, notre fonction promisify devrait être en mesure de `résoudre/rejeter` en conséquence.

L'implémentation ci-dessus fonctionnera lorsque la fonction originale attend un callback avec deux arguments, `(err, result)`. C'est ce que nous rencontrons le plus souvent. Ensuite, notre callback personnalisé est dans le bon format et `promisify` fonctionne parfaitement pour un tel cas.

**Mais que se passe-t-il si la fonction originale** `**fn**` **attend un callback avec plus d'arguments** comme `**callback(err, result1, result2, ...)**`**?**

Pour la rendre compatible avec cela, nous devons modifier notre fonction `myPromisify` qui sera une version avancée.

```
const myPromisify = (fn) => {
   return (...args) => {
     return new Promise((resolve, reject) => {
       function customCallback(err, ...results) {
         if (err) {
           return reject(err)
         }
         return resolve(results.length === 1 ? results[0] : results) 
        }
        args.push(customCallback)
        fn.call(this, ...args)
      })
   }
}
```

Exemple :

```
const getSumAsync = (num1, num2, callback) => {
 
  if (!num1 || !num2) {
    return callback(new Error("Dépendances manquantes"), null);
  }
  
  const sum = num1 + num2;
  const message = `La somme est ${sum}`
  return callback(null, sum, message);
}
const getSumPromise = myPromisify(getSumAsync)
getSumPromise(2, 3).then(arrayOfResults) // [6, 'La somme est 6']
```

C'est tout ! Merci d'être arrivé jusqu'ici !

J'espère que vous êtes en mesure de saisir le concept. Essayez de le relire. C'est un peu de code à comprendre, mais pas trop complexe. Faites-moi savoir si cela a été utile ?

N'oubliez pas de le partager avec vos amis qui commencent avec Node.js ou qui ont besoin de monter en compétences avec Node.js.

Références :

[https://nodejs.org/dist/latest-v8.x/docs/api/util.html#util_util_promisify_original](https://nodejs.org/dist/latest-v8.x/docs/api/util.html#util_util_promisify_original)

[https://github.com/digitaldesignlabs/es6-promisify](https://github.com/digitaldesignlabs/es6-promisify)

_Vous pouvez lire d'autres articles comme celui-ci sur [101node.io](https://101node.io/blog/write-your-own-promisify-function-from-scratch/)._