---
title: La vraie différence entre catch et onRejected
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T22:08:33.000Z'
originalURL: https://freecodecamp.org/news/the-real-difference-between-catch-vs-onrejected-15cab8978e92
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JLtSGRqnw1wIR-o3LPziwA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: promises
  slug: promises
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La vraie différence entre catch et onRejected
seo_desc: 'By Max Belsky

  Most popular articles describe the difference between catch and onRejected in a
  code snippet like this:

  const getPromise = () => new Promise((resolve, reject) => {  Math.round(Math.random())
  ?     resolve(''resolve #1'') :     reject(''rej...'
---

Par Max Belsky

La plupart des articles populaires décrivent la différence entre catch et onRejected dans un extrait de code comme ceci :

```
const getPromise = () => new Promise((resolve, reject) => {  Math.round(Math.random()) ?     resolve('resolve #1') :     reject('reject #1')})
```

```
getPromise().then(result => {  throw new Error('reject #2')}, error => {  // Gère uniquement 'reject #1'})
```

```
getPromise().then(result => {  throw new Error('reject #2')})  .catch(error => {    // Gère à la fois 'reject #1',     // et 'reject #2'  }))
```

onRejected ne gère jamais les promesses rejetées du même callback `.then(onFulfilled)` et `.catch` prend les deux. Cependant, outre la différence de comportement, il y a une autre nuance. Il s'agit de la manière dont ces méthodes seront traduites en [microtâches](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/) et de la manière dont elles seront mises en file d'attente.  
Examinons un exemple de la différence.

#### Promise.race

Il y a une tâche — écrire un polyfill pour `Promise.race`. Nous utilisons un modèle commun dans les deux fonctions pour gérer les promesses `resolved` et différents outils pour gérer les promesses `rejected`.

```
const promiseRaceOnRejected = (promises = []) => {  return new Promise((resolve, reject) => {    promises.forEach(promise => {      promise.then(        result => resolve(result),        error => reject(error)      )    })  })}
```

```
const promiseRaceCatch = (promises = []) => {  return new Promise((resolve, reject) => {    promises.forEach(promise => {      promise.then(result => resolve(result))        .catch(error => reject(error))    })  })}
```

Essayez quelques tests pour être sûr que les deux solutions fonctionnent bien :

```
// Une fonction auxiliaire pour créer une promesse retardée
const getPromise = (resolveMs, rejectMs) => {  return new Promise((resolve, reject) => {    if ('number' === typeof rejectMs) {      setTimeout(() => reject(rejectMs), rejectMs)    }
```

```
    if ('number' === typeof resolveMs) {      setTimeout(() => resolve(resolveMs), resolveMs)    }  })}
```

```
const testRaces = async () => {  const r1 = await promiseRaceOnRejected([    getPromise(0),     getPromise(5)  ])  // 0
```

```
const r2 = await promiseRaceCatch([    getPromise(0),     getPromise(5)  ])  // 0
```

```
const r3 = await promiseRaceOnRejected([    getPromise(5),     getPromise(null, 2)  ])    .catch(e => e)  // 2
```

```
const r4 = await promiseRaceCatch([    getPromise(5),     getPromise(null, 2)  ])    .catch(e => e)  // 2}
```

```
testRaces()
```

Comme vous pouvez le voir, les deux polyfills fonctionnent comme prévu. L'ordre des arguments et la variation du gestionnaire de promesses `rejected` n'ont pas d'importance. Jusqu'à ce que nous essayions avec le prochain ensemble de tests :

```
const r5 = await promiseRaceOnRejected([    Promise.resolve('Resolve'),     Promise.reject('Reject')  ])  // Resolve
```

```
const r6 = await promiseRaceCatch([    Promise.resolve('Resolve'),     Promise.reject('Reject')  ])  // Resolve
```

```
const r7 = await promiseRaceOnRejected([    Promise.reject('Reject'),     Promise.resolve('Resolve')  ])    .catch(e => e)  // Reject
```

```
const r8 = await promiseRaceCatch([    Promise.reject('Reject'),     Promise.resolve('Resolve')  ])    .catch(e => e)  // ???
```

Les cinquième, sixième et septième courses retournent les valeurs attendues. Et pour la huitième ? Au lieu de `Reject`, elle retourne `Resolve` et ce n'est pas un bug.

#### File d'attente des microtâches

Selon le résultat du travail, une promesse en attente change son état en `resolved` ou `rejected`. L'environnement JS place cette promesse dans une file d'attente de microtâches. Comme décrit dans la spécification ECMA 2015 [specification](http://www.ecma-international.org/ecma-262/6.0/#sec-jobs-and-job-queues), cette file d'attente fonctionne selon le principe [FIFO](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)) — premier entré, premier sorti. Basé sur cela, examinons le cas de la huitième course.

![Image](https://cdn-media-1.freecodecamp.org/images/uFX52cgzB6WwzZeyDMGbhZwt40hV6C8k-uWa)
_Premier tick de la file d'attente_

Au début de la course, nous avons déjà deux promesses en file d'attente, et la rejetée est la première. `.then` sans second argument ne peut pas gérer une promesse rejetée, donc il remet la promesse dans la file d'attente. Et au lieu de gérer cette promesse avec `.catch`, l'environnement JS passe à `p2` parce qu'elle a une priorité plus élevée dans la file d'attente.

![Image](https://cdn-media-1.freecodecamp.org/images/-ZAASKNuYIOZwBQBwd7XpBdvYecTiE2n0ZWF)
_Deuxième tick de la file d'attente_

Au prochain tick, `.then` gère `p2` et la course se termine avec le résultat `Resolve`.

La prochaine fois que vous choisirez entre les gestionnaires catch et onRejected, souvenez-vous non seulement des promesses rejetées qu'ils attrapent, mais aussi de la différence de mise en file d'attente !