---
title: Callbacks et Promesses coexistant en harmonie avec l'API
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-19T23:38:01.000Z'
originalURL: https://freecodecamp.org/news/callbacks-and-promises-living-together-in-api-harmony-7ed26204538b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Xc0Degaa5ZyZGmnVAI5_eQ.png
tags:
- name: api
  slug: api
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Callbacks et Promesses coexistant en harmonie avec l'API
seo_desc: 'By Ethan Arrowood

  In this article, we''ll learn how to update a callback-based API to support Promises
  as well.

  First, what is an API, or application programming interface? It''s sometimes referred
  to as a module. It is a collection of methods and vari...'
---

Par Ethan Arrowood

Dans cet article, nous allons apprendre comment mettre à jour une API basée sur des callbacks pour supporter également les Promesses.

Tout d'abord, qu'est-ce qu'une API, ou interface de programmation d'application ? Elle est parfois appelée un _module_. Il s'agit d'une collection de méthodes et de variables que les développeurs peuvent utiliser dans leur propre application.

Regardez l'épisode accompagnant Real Coding [ici](https://youtu.be/6DphXwRbPlo).

### Fonctions de Callback

De nombreuses API et modules JavaScript fournissent un paramètre final dans leurs méthodes pour ce qu'on appelle une méthode de callback. La plupart du temps, vous verrez cela défini comme `done`, `next`, `callback`, ou `cb` (abréviation pour callback). Les fonctions de callback sont incroyablement utiles car elles permettent aux autres développeurs de tirer plus de votre fonction, comme la gestion des erreurs et les requêtes asynchrones.

Par exemple, une méthode d'API peut produire une variété d'erreurs et ces erreurs, si elles ne sont pas correctement gérées, peuvent faire planter une application entière. Une API utilisant des méthodes de callback **devrait** retourner tous les objets `Error` comme premier paramètre dans le callback. Il est supposé que le premier paramètre dans une fonction de callback est toujours une instance d'erreur.

La fonction ci-dessous est un exemple simple. Son but est de doubler le paramètre `x` et de le retourner via la fonction `callback` spécifiée. `error` commence comme `null`. Si l'une des vérifications conditionnelles échoue, une instance `Error` est assignée à `error`. Ensuite, si `error` existe (il n'est pas null ou undefined), alors nous ne doublons pas `x` et nous définissons la variable `double` comme `null`; sinon, `x` est doublé et assigné à la variable `double`. Après tout cela, la fonction `doublePositiveOnly` retournera la méthode de callback avec le premier paramètre référençant la variable `error` et le second paramètre référençant la variable `double`.

```js
function doublePositiveOnly(x, callback) {
  let error
  if ( !x )
    error = new Error('x doit être défini')
  if ( typeof x !== 'number' )
    error = new Error('x doit être un nombre')
  if ( x < 0 )
    error = new Error('x doit être positif')
    
  const double = error ? null : x * 2
  
  return callback(error, double)
}
```

Comment utiliseriez-vous cette fonction ?

```js
doublePositiveOnly(16, function (err, result) {
  if (err) console.error(err.message)
  console.log(result)
})
```

### Fonctions de Promesse

Les fonctions de promesse en production sont faciles à reconnaître car elles utilisent les méthodes `.then` et `.catch` pour retourner des informations à l'utilisateur. Presque toutes les fonctions de callback peuvent être remplacées par des promesses, alors reconstruisons notre méthode `doublePositiveOnly` en utilisant des promesses.

```js
function doublePositiveOnly( x ) {
  return new Promise(function (resolve, reject) {
    let error
    if ( !x )
      error = new Error('x doit être défini')
    if ( typeof x !== 'number' )
      error = new Error('x doit être un nombre')
    if ( x < 0 )
      error = new Error('x doit être positif')
      
    error ? reject(error) : resolve(x * 2)
  })
}
```

La fonction ci-dessus sert exactement le même but que l'implémentation de callback. Cependant, cette version ne prend plus une méthode de callback comme paramètre. Au lieu de cela, elle `reject` une erreur ou `resolve` le résultat. Vous pouvez utiliser cette méthode comme suit :

```js
doublePositiveOnly(16).then(function (result) {
  // faire des trucs cool avec le résultat
  console.log(result)
}).catch(function (err) {
  // oh non une erreur ! Gérez-la comme vous le souhaitez
  console.error(err.message) 
})
```

La lisibilité d'une fonction de Promesse est beaucoup plus claire que celle d'une fonction de callback, car vous pouvez facilement gérer le résultat ainsi que les erreurs potentielles. Il y a beaucoup plus à dire sur les fonctions de Promesse que je n'ai pas couvert ici, et je vous encourage à [apprendre](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) autant que possible à leur sujet.

### Callbacks et Promesses Ensemble

Nous avons des callbacks et nous avons des promesses. Elles sont interchangeables et satisfont toutes deux des besoins similaires. Maintenant, considérons le scénario où nous avons une API qui ne supporte que les méthodes de callback. Cette API est téléchargée 1000 fois et fonctionne maintenant en production sur d'innombrables applications. Mais maintenant, le mainteneur veut supporter les Promesses également. Peut-il le faire tout en maintenant le support des callbacks ? **OUI !**

Regardons à nouveau l'implémentation de callback de `doublePositiveOnly`, mais maintenant également avec le support des promesses :

```js
function doublePositiveOnly(x, callback) {
  const func = this.doublePositiveOnly
  
  if ( callback === undefined ) {
    return new Promise(function (resolve, reject) {
      func(x, function (err, result) {
        err ? reject(err) : resolve(result)
      })
    })
  }
  
  let error
  if ( !x )
    error = new Error('x doit être défini')
  if ( typeof x !== 'number' )
    error = new Error('x doit être un nombre')
  if ( x < 0 )
    error = new Error('x doit être positif')
  
  const double = error ? null : x * 2
  
  return callback(error, double)
}
```

Et voilà, la méthode `doublePositiveOnly` supporte maintenant également les promesses. Cela fonctionne parce que d'abord, elle stocke la référence à la fonction dans la variable `func`. Ensuite, elle vérifie si un callback a été passé à la fonction. Si ce n'est pas le cas, elle retourne une promesse qui passe le paramètre `x` à un autre appel de `doublePositiveOnly`, et elle inclut une fonction de callback. Cette fonction de callback `reject` ou `resolve` la promesse, tout comme l'implémentation basée uniquement sur les promesses.

Ce qui est génial avec cette solution, c'est que vous pouvez l'utiliser presque partout et vous n'avez pas à modifier les parties originales de la fonction ! Vous pouvez la voir en action dans un module auquel j'ai récemment contribué appelé [fastify-jwt](https://github.com/fastify/fastify-jwt/). Les méthodes `[requestVerify](https://github.com/fastify/fastify-jwt/blob/master/jwt.js#L108-L114)` et `[replySign](https://github.com/fastify/fastify-jwt/blob/master/jwt.js#L79-L85)` supportent à la fois les callbacks et les promesses.

Si vous avez des questions, n'hésitez pas à demander !

Vous pouvez me suivre sur [Github](https://github.com/Ethan-Arrowood) et [Twitter](https://twitter.com/ArrowoodTech) ou consulter mon [site web](https://ethanarrowood.com).

Continuez le bon travail.

~Ethan Arrowood