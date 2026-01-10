---
title: Comment les promesses JavaScript fonctionnent réellement de l'intérieur vers
  l'extérieur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-18T16:56:00.000Z'
originalURL: https://freecodecamp.org/news/how-javascript-promises-actually-work-from-the-inside-out-76698bb7210b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IXaKMoKxyvrZs1prvukJvw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment les promesses JavaScript fonctionnent réellement de l'intérieur
  vers l'extérieur
seo_desc: 'By Shailesh Shekhawat

  One of the most important questions I faced in interviews was how promises are implemented.
  Since async/await is becoming more popular, you need to understand promises.

  What is a Promise?

  A promise is an object which represents ...'
---

Par Shailesh Shekhawat

L'une des questions les plus importantes auxquelles j'ai été confronté lors d'entretiens était de savoir comment les promesses sont implémentées. Puisque async/await devient de plus en plus populaire, vous devez comprendre les promesses.

### Qu'est-ce qu'une promesse ?

Une promesse est un objet qui représente le résultat d'une opération asynchrone qui est soit résolue, soit rejetée (avec une raison).

Il existe 3 états :

* **Remplie :** `onFulfilled()` sera appelée (par exemple, `resolve()` a été appelée)
* **Rejetée :** `onRejected()` sera appelée (par exemple, `reject()` a été appelée)
* **En attente :** pas encore remplie ou rejetée

Alors voyons comment cela est implémenté :

[https://github.com/then/promise/blob/master/src/core.js](https://github.com/then/promise/blob/master/src/core.js)

Selon la définition sur [Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise#Parameters) : elle prend une fonction _executor_ comme argument.

```js
function noop() {} 

function Promise(executor) {
  if (typeof this !== 'object') {
    throw new TypeError('Les promesses doivent être construites via new');
  }
 if (typeof executor !== 'function') {
   throw new TypeError("L'argument du constructeur de la promesse n'est pas une fonction");
 }
  this._deferredState = 0;
  this._state = 0;
  this._value = null;
  this._deferreds = null;
  if (executor === noop) return;
  doResolve(executor, this);
}
```

Cela ressemble à une fonction simple avec certaines propriétés initialisées à `0` ou `null`. Voici quelques points à noter :

La propriété `**this._state**` peut avoir trois valeurs possibles comme décrit ci-dessus :

```
0 - en attente

1 - remplie avec _value

2 - rejetée avec _value

3 - a adopté l'état d'une autre promesse, _value
```

Sa valeur est `0` (**_en attente)_** lorsque vous créez une nouvelle **_promesse._**

Plus tard, `doResolve(executor, this)` est invoqué avec l'objet `executor` et `promise`.

Passons à la définition de `doResolve` et voyons comment elle est implémentée.

```js
/**
* Prenez une fonction de résolution potentiellement défectueuse et assurez-vous
* que onFulfilled et onRejected ne sont appelées qu'une seule fois.
*
* Ne fait aucune garantie concernant l'asynchronisme.
*/

function doResolve(fn, promise) {
  var done = false;
  var resolveCallback = function(value) {
      if (done) return;
      done = true;
      resolve(promise, value);
 };
 var rejectCallback = function(reason) {
   if (done) return;
   done = true;
   reject(promise, reason);
};
    
var res = tryCallTwo(fn, resolveCallback, rejectCallback);
  if (!done && res === IS_ERROR) {
    done = true;
    reject(promise, LAST_ERROR);
 }
}
```

Ici, elle appelle à nouveau la fonction `tryCallTwo` avec l'executor et 2 callbacks. Les callbacks appellent à leur tour `resolve` et `reject`.

La variable `done` est utilisée ici pour s'assurer que la promesse est résolue ou rejetée une seule fois. Donc, si vous essayez de rejeter ou de résoudre une promesse plus d'une fois, elle retournera car `done = true`.

```js
function tryCallTwo(fn, a, b) {
   try {
    fn(a, b);
   } catch (ex) {
     LAST_ERROR = ex;
     return IS_ERROR;
  }
}
```

Cette fonction appelle indirectement la fonction de rappel principale `executor` avec 2 arguments. Ces arguments contiennent la logique sur la manière dont `resolve` ou `reject` doit être appelée. Vous pouvez vérifier _resolveCallback_ et _rejectCallback_ dans la fonction `doResolve` ci-dessus.

S'il y a une erreur pendant l'exécution, elle stockera l'erreur dans `LAST_ERROR` et retournera l'erreur.

Avant de passer à la définition de la fonction `resolve`, examinons d'abord la fonction `.then` :

```js
Promise.prototype.then = function(onFulfilled, onRejected) {
   if (this.constructor !== Promise) {
     return safeThen(this, onFulfilled, onRejected);
   }
   var res = new Promise(noop);
   handle(this, new Handler(onFulfilled, onRejected, res));
   return res;
};

function Handler(onFulfilled, onRejected, promise) {
   this.onFulfilled = typeof onFulfilled === "function" ? onFulfilled  : null;
   this.onRejected = typeof onRejected === "function" ? onRejected :  null;
   this.promise = promise;
}
```

Dans la fonction ci-dessus, `then` crée une nouvelle `promise` et l'assigne comme propriété à une nouvelle fonction appelée `Handler`. La fonction `Handler` a pour arguments _onFulfilled_ et _onRejected_. Plus tard, elle utilisera cette promesse pour la résoudre ou la rejeter avec une valeur/raison.

Comme vous pouvez le voir, la fonction `.then` appelle à nouveau une autre fonction :

```js
handle(this, new Handler(onFulfilled, onRejected, res));
```

#### Implémentation :

```js
function handle(self, deferred) {
  while (self._state === 3) {
    self = self._value;
  }
  if (Promise._onHandle) {
    Promise._onHandle(self);
  }
  if (self._state === 0) {
     if (self._deferredState === 0) {
         self._deferredState = 1;
         self._deferreds = deferred;
         return;
    }
    if (self._deferredState === 1) {
       self._deferredState = 2;
       self._deferreds = [self._deferreds, deferred];
       return;
    }
    self._deferreds.push(deferred);
    return;
 }
   handleResolved(self, deferred);
}
```

* Il y a une boucle while qui continuera à assigner l'objet de promesse résolue à la promesse actuelle qui est également une promesse pour `_state === 3`
* Si `_state = 0(en attente)` et que l'état de la promesse a été différé jusqu'à ce qu'une autre promesse imbriquée soit résolue, son callback est stocké dans `self._deferreds`

```js
function handleResolved(self, deferred) {
   asap(function() { // asap est une bibliothèque externe utilisée pour exécuter cb immédiatement
   var cb = self._state === 1 ? deferred.onFulfilled :     deferred.onRejected;
   if (cb === null) {
       if (self._state === 1) {
           resolve(deferred.promise, self._value);
       } else {
         reject(deferred.promise, self._value);
       }
      return;
  }
  var ret = tryCallOne(cb, self._value);
    if (ret === IS_ERROR) {
       reject(deferred.promise, LAST_ERROR);
    } else {
      resolve(deferred.promise, ret);
    }
  });
}
```

Ce qui se passe :

* Si l'état est 1`(remplie)` alors appelez _resolve_ sinon _reject_
* Si `onFulfilled` ou `onRejected` est `null` ou si nous avons utilisé un `.then()` vide, _resolved_ ou _reject_ sera appelé respectivement
* Si `cb` n'est pas vide, alors il appelle une autre fonction `tryCallOne(cb, self._value)`

```js
function tryCallOne(fn, a) {
   try {
     return fn(a);
   } catch (ex) {
      LAST_ERROR = ex;
     return IS_ERROR;
   }
} a) {
```

`**tryCallOne**` **:** Cette fonction appelle uniquement le callback qui est passé dans l'argument `self._value`. S'il n'y a pas d'erreur, elle résoudra la promesse, sinon elle la rejettera.

Chaque promesse doit fournir une méthode `.then()` avec la signature suivante :

```js
promise.then(
  onFulfilled?: Function,
  onRejected?: Function
) => Promise
```

* `onFulfilled()` et `onRejected()` sont tous deux optionnels.
* Si les arguments fournis ne sont pas des fonctions, ils doivent être ignorés.
* `onFulfilled()` sera appelée après que la promesse soit remplie, avec la valeur de la promesse comme premier argument.
* `onRejected()` sera appelée après que la promesse soit rejetée, avec la raison du rejet comme premier argument.
* Ni `onFulfilled()` ni `onRejected()` ne peuvent être appelées plus d'une fois.
* `.then()` peut être appelée plusieurs fois sur la même promesse. En d'autres termes, une promesse peut être utilisée pour agréger des callbacks.
* `.then()` doit retourner une nouvelle promesse.

### Chaînage des promesses

`.then` doit retourner une promesse. C'est pourquoi nous pouvons créer une chaîne de promesses comme ceci :

```js
Promise
.then(() => 
  Promise.then(() => 
   Promise.then(result => result) 
)).catch(err)
```

#### Résolution d'une promesse

Voyons la définition de la fonction `resolve` que nous avons laissée plus tôt avant de passer à `.then()` :

```js
function resolve(self, newValue) {
// Procédure de résolution de promesse : https://github.com/promises-aplus/promises-spec#the-promise-resolution-procedure
   if (newValue === self) {
      return reject(
        self,
        new TypeError("Une promesse ne peut pas être résolue avec elle-même.")
     );
   }
   if (
      newValue &&
     (typeof newValue === "object" || typeof newValue === "function")
   ) {
    var then = getThen(newValue);
    if (then === IS_ERROR) {
      return reject(self, LAST_ERROR);
   }
   if (then === self.then && newValue instanceof Promise) {
      self._state = 3;
     self._value = newValue;
     finale(self);
      return;
   } else if (typeof then === "function") {
      doResolve(then.bind(newValue), self);
      return;
   }
}
   self._state = 1;
   self._value = newValue;
   finale(self);
}
```

* Nous vérifions si le résultat est une promesse ou non. Si c'est une fonction, alors appelez cette fonction avec la valeur en utilisant `doResolve()`.
* Si le résultat est une promesse, elle sera poussée dans le tableau `deferreds`. Vous pouvez trouver cette logique dans la fonction `finale`.

#### Rejeter une promesse :

```js
Promise.prototype['catch'] = function (onRejected) {
   return this.then(null, onRejected);
};
```

La fonction ci-dessus peut être trouvée dans `./es6-extensions.js`.

Chaque fois que nous rejetons une promesse, le callback `.catch` est appelé, ce qui est une syntaxe simplifiée pour `then(null, onRejected)`.

Voici un diagramme de base que j'ai créé qui donne un aperçu de ce qui se passe à l'intérieur :

![Image](https://cdn-media-1.freecodecamp.org/images/r2vWWMWfHAR70Vx6s3URd8HIb9aA-ngZJcqt)

Voyons une fois de plus comment tout fonctionne :

Par exemple, nous avons cette promesse :

```js
new Promise((resolve, reject) => {
   setTimeout(() => {
    resolve("Le temps est écoulé");
  }, 3000)
})
.then(console.log.bind(null, 'La promesse est remplie'))
.catch(console.error.bind(null, 'Quelque chose de mauvais est arrivé : '))
```

1. Le constructeur de la promesse est appelé et une instance est créée avec `new Promise`
2. La fonction `executor` est passée à `doResolve(executor, this)` et le callback où nous avons défini `setTimeout` sera appelé par `tryCallTwo(executor, resolveCallback, rejectCallback)` donc cela prendra 3 secondes pour se terminer
3. Nous appelons `.then()` sur l'instance de la promesse donc avant que notre `timeout` ne soit terminé ou qu'une API asynchrone ne retourne, `Promise.prototype.then` sera appelé comme `.then(cb, null)`
4. `.then` crée une nouvelle `promise` et la passe comme argument à `new Handler(onFulfilled, onRejected, promise)`
5. La fonction `handle` est appelée avec l'instance `promise` originale et l'instance `handler` que nous avons créée au point 4.
6. À l'intérieur de la fonction `handle`, l'état actuel `self._state = 0` et `self._deferredState = 0` donc `self_deferredState` deviendra `1` et l'instance `handler` sera assignée à `self.deferreds` après quoi le contrôle retournera de là
7. Après `.then()` nous appelons `.catch()` qui appellera interne `.then(null, errorCallback)` — les mêmes étapes sont répétées à partir du **point 4 au point 6 et saute le point 7** puisque nous avons appelé `.catch` une fois
8. L'état actuel de la `promise` est **en attente** et elle attendra jusqu'à ce qu'elle soit résolue ou rejetée. Donc dans cet exemple, après 3 secondes, le callback `setTimeout` est appelé et nous résolvons cela explicitement ce qui appellera `resolve(value)`.
9. `resolveCallback` sera appelé avec la valeur `Le temps est écoulé` :) et il appellera la fonction principale `resolve` qui vérifiera si `value !== null && value == 'object' && value === 'function'`
10. Cela échouera dans notre cas puisque nous avons passé une `string` et `self._state` deviendra `1` avec `self._value = 'Le temps est écoulé'` et plus tard `finale(self)` est appelé.
11. `finale` appellera `handle(self, self.deferreds)` une fois car `self._deferredState = 1`, et pour la chaîne de promesses, il appellera `handle()` pour chaque fonction `deferred`.
12. Dans la fonction `handle`, puisque la `promise` est déjà résolue, elle appellera `handleResolved(self, deferred)`
13. La fonction `handleResolved` vérifiera si `_state === 1` et assignera `cb = deferred.onFulfilled` qui est notre callback `then`. Plus tard, `tryCallOne(cb, self._value)` appellera ce callback et nous obtenons le résultat final. Pendant ce processus, si une erreur se produit, la `promise` sera rejetée.

#### Lorsque une promesse est rejetée

Dans ce cas, toutes les étapes resteront les mêmes — mais au **point 8**, nous appelons `reject(reason)`. Cela appellera indirectement `rejectCallback` défini dans `doResolve()` et `self._state` deviendra `2`. Dans la fonction `finale`, `cb` sera égal à `deferred.onRejected` qui sera appelé plus tard par `tryCallOne`. C'est ainsi que le callback `.catch` sera appelé.

C'est tout pour l'instant ! J'espère que vous avez apprécié l'article et qu'il vous aidera lors de votre prochain entretien JavaScript.

Si vous rencontrez un problème, n'hésitez pas à [me contacter](https://twitter.com/thatshailesh) ou à commenter ci-dessous. Je serais heureux de vous aider 😊

_N'hésitez pas à applaudir si vous avez trouvé cela digne d'être lu !_

_Publié à l'origine sur [101node.io](https://101node.io/blog/how-promises-actually-work-inside-out) le 5 février 2019._