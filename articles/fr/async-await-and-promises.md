---
title: Async/Await et les Promesses expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/async-await-and-promises
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ceb740569d1a4ca34e7.jpg
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
- name: toothbrush
  slug: toothbrush
seo_title: Async/Await et les Promesses expliqués
seo_desc: 'The async / await operators make it easier to implement many async Promises.
  They also allow engineers to write clearer, more succinct, testable code.

  To understand this subject, you should have a solid understanding of how Promises
  work.

  Basic Synta...'
---

Les opérateurs `async` / `await` [opérateurs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators) facilitent la mise en œuvre de nombreuses Promesses asynchrones. Ils permettent également aux ingénieurs d'écrire un code plus clair, plus concis et plus testable.

Pour comprendre ce sujet, vous devez avoir une solide compréhension du fonctionnement des [Promesses](https://guide.freecodecamp.org/javascript/promises).

## **Syntaxe de base**

```javascript
function slowlyResolvedPromiseFunc(string) { 
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(string);
    }, 5000);
  });
}

async function doIt() {
  const myPromise = await slowlyResolvedPromiseFunc("foo");
  console.log(myPromise); // "foo"
}

doIt();
```

Il y a quelques points à noter :

* La fonction qui englobe la déclaration `await` doit inclure l'opérateur `async`. Cela indique à l'interpréteur JS qu'il doit attendre jusqu'à ce que la Promesse soit résolue ou rejetée.
* L'opérateur `await` doit être en ligne, lors de la déclaration const.
* Cela fonctionne pour `reject` ainsi que pour `resolve`.

---

## **Promesses imbriquées vs. `Async` / `Await`**

La mise en œuvre d'une seule Promesse est assez simple. En revanche, les Promesses enchaînées ou la création d'un motif de dépendance peuvent produire du "code spaghetti".

Les exemples suivants supposent que la bibliothèque [`request-promise`](https://github.com/request/request-promise) est disponible sous le nom `rp`.

### **Promesses enchaînées/imbriquées**

```javascript
// Première Promesse
const fooPromise = rp("http://domain.com/foo");

fooPromise.then(resultFoo => {
    // Doit attendre que "foo" soit résolu
    console.log(resultFoo);

    const barPromise = rp("http://domain.com/bar");
    const bazPromise = rp("http://domain.com/baz");

    return Promise.all([barPromise, bazPromise]);
}).then(resultArr => {
    // Gérer les résolutions de "bar" et "baz" ici
    console.log(resultArr[0]);
    console.log(resultArr[1]);
});
```

### **Promesses `async` et `await`**

```javascript
// Envelopper tout dans une fonction asynchrone
async function doItAll() {
    // Récupérer les données de l'endpoint "foo", mais attendre la résolution
    console.log(await rp("http://domain.com/foo"));

    // Lancer simultanément les deux prochains appels asynchrones,
    // ne pas attendre que "bar" soit lancé pour lancer "baz"
    const barPromise = rp("http://domain.com/bar");
    const bazPromise = rp("http://domain.com/baz");

    // Après avoir lancé les deux simultanément, attendre les deux
    const barResponse = await barPromise;
    const bazResponse = await bazPromise;

    console.log(barResponse);
    console.log(bazResponse);
}

// Enfin, invoquer la fonction asynchrone
doItAll().then(() => console.log('Terminé !'));
```

Les avantages de l'utilisation de `async` et `await` devraient être clairs. Ce code est plus lisible, modulaire et testable.

Il est juste de noter que même s'il y a un sentiment ajouté de concurrency, le processus de calcul sous-jacent est le même que dans l'exemple précédent.

---

## **Gestion des erreurs / Rejet**

Un bloc try-catch de base gère une Promesse rejetée.

```javascript
async function errorExample() {
  try {
    const rejectedPromise = await Promise.reject("Oh-oh !");
  } catch (error) {
    console.log(error); // "Oh-oh !"
  }
}

errorExample();
```