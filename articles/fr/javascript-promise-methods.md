---
title: Les promesses JavaScript – Les méthodes promise.then, promise.catch et promise.finally
  expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-16T18:30:06.000Z'
originalURL: https://freecodecamp.org/news/javascript-promise-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-pixabay-532414.jpg
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: Les promesses JavaScript – Les méthodes promise.then, promise.catch et
  promise.finally expliquées
seo_desc: 'By Dillion Megida

  A promise is an object in JavaScript that will produce a value sometime in the future.
  This usually applies to asynchronous operations.

  In applications, asynchronous operations happen a lot. This can be API requests,
  delayed data pr...'
---

Par Dillion Megida

Une promesse est un objet en JavaScript qui produira une valeur à un moment donné dans le futur. Cela s'applique généralement aux opérations asynchrones.

Dans les applications, les opérations asynchrones se produisent souvent. Cela peut être des requêtes API, un traitement de données différé, et bien plus encore. 

Au lieu de bloquer l'exécution du code jusqu'à ce que les données se chargent, vous pouvez les définir comme des promesses, afin que l'exécution du code se poursuive avec d'autres parties du code. Et lorsque les promesses sont complétées, vous pouvez utiliser les données qu'elles contiennent.

Vous pouvez en apprendre davantage sur [les promesses dans cet article simplifié](https://dillionmegida.com/p/javascript-promises/).

Dans certains cas, une promesse réussit, et dans d'autres cas, elle échoue. Comment gérez-vous le résultat de chaque issue ?

Pour le reste de cet article, nous allons comprendre les méthodes `then`, `catch` et `finally` des promesses.

## Les états des promesses en JavaScript

Une promesse a trois états :
* **en attente** : la promesse est encore en cours
* **tenue** : la promesse se résout avec succès et retourne une valeur
* **rejetée** : la promesse échoue avec une erreur

Les états **tenue** et **rejetée** ont un point commun : qu'une promesse soit tenue ou rejetée, la promesse est **résolue**. Ainsi, un état résolu peut être soit une promesse tenue, soit une promesse rejetée.

## Quand une promesse est tenue

Quand une promesse est tenue, vous pouvez accéder aux données résolues dans la méthode `then` de la promesse :

```js
promise.then(value => {
 // utiliser la valeur pour quelque chose
})
```

Pensez à la méthode `then` comme "cela fonctionne et **ensuite** faites ceci avec les données retournées par la promesse". S'il n'y a pas de données, vous pouvez ignorer la méthode `then`.

Il est également possible que la méthode `then` puisse retourner une autre promesse, donc vous pouvez enchaîner une autre méthode `then` comme ceci :

```js
promise
  .then(value => {
    return value.anotherPromise()
  })
  .then(anotherValue => {
    // utiliser cette valeur
  })
```

## Quand une promesse est rejetée

Quand une promesse est rejetée (c'est-à-dire que la promesse échoue), vous pouvez accéder aux informations d'erreur retournées dans la méthode `catch` de la promesse :

```js
promise.catch(error => {
  // interpréter l'erreur et peut-être afficher quelque chose sur l'UI
})
```

Les promesses peuvent échouer pour différentes raisons. Pour les requêtes API, cela peut être une connexion réseau échouée, ou une erreur retournée par le serveur. De telles promesses seront rejetées si elles rencontrent des erreurs.

Pensez à la méthode `catch` comme "cela ne fonctionne pas donc je **capture** l'erreur pour qu'elle ne casse pas l'application". Si vous ne capturez pas l'erreur, cela peut casser votre application dans certains cas.

## Quand une promesse est résolue

Il y a une dernière étape de la promesse. Que la promesse soit tenue ou rejetée, la promesse a été complétée (a été **résolue**). À ce stade complété, vous pouvez **finalement** faire quelque chose.

La méthode `finally` des promesses est utile lorsque vous voulez faire quelque chose après que la promesse a été résolue. Cela peut être un nettoyage ou du code que vous pourriez vouloir dupliquer dans les méthodes `then` et `catch`.

Par exemple, au lieu de faire :

```js
let dataIsLoading = true;

promise
  .then(data => {
    // faire quelque chose avec les données
    dataIsLoading = false;
  })
  .catch(error => {
   // faire quelque chose avec l'erreur
   dataIsLoading = false;
  })
```

Vous pouvez utiliser la méthode `finally` comme ceci :

```js
let dataIsLoading = true;

promise
  .then(data => {
    // faire quelque chose avec les données
  })
  .catch(error => {
   // faire quelque chose avec l'erreur
  })
  .finally(() => {
    dataIsLoading = false;
  })
```

La méthode `finally` est appelée indépendamment du résultat (tenue ou rejetée) de la promesse.

## Conclusion

Les promesses ont les méthodes `then`, `catch` et `finally` pour faire différentes choses en fonction du résultat d'une promesse. En résumé :

* `then` : quand une promesse réussit, vous pouvez **ensuite** utiliser les données résolues
* `catch` : quand une promesse échoue, vous **capturez** l'erreur, et faites quelque chose avec les informations d'erreur
* `finally` : quand une promesse est résolue (échoue ou réussit), vous pouvez **finalement** faire quelque chose