---
title: 'En savoir plus sur les promesses JavaScript : de zéro à héros en 25 tests'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T23:21:47.000Z'
originalURL: https://freecodecamp.org/news/learn-more-about-javascripts-promises-from-zero-to-hero-in-25-tests-ddaaf4d3c928
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JZlPOGIMUKYlwvBnmPomEg.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'En savoir plus sur les promesses JavaScript : de zéro à héros en 25 tests'
seo_desc: 'By Andrea Koutifaris

  A test is worth a thousand words… or was it a picture…?

  I think the best way to explain JavaScript promises is through examples. What is
  a good, self contained, and short way to write an example? A test!

  For those who have never ...'
---

Par Andrea Koutifaris

Un test vaut mille mots… ou était-ce une image… ?

Je pense que la meilleure façon d'expliquer les promesses JavaScript est à travers des exemples. Quelle est la meilleure façon d'écrire un exemple, autonome et court ? Un test !

Pour ceux qui n'ont jamais vu une suite de tests Jasmine, `it('...', (done) => {..`}) est un test et `done` est une fonction qui doit être exécutée lorsqu'un test asynchrone est terminé.

Les règles ici sont :

* **Chaque test commence par affirmer quelque chose en anglais**. Vous devez déduire pourquoi le code du test implique que l'affirmation du test est vraie.
* Certains tests ont des attentes. Si le test passe, les attentes sont vraies.
* D'autres tests dépendent du rappel `done()` pour être appelés. Si `done()` n'est pas appelé, le test échoue.

Chaque test se trouve dans [ce JSFiddle](https://jsfiddle.net/kouty79/e52qkkmu/), alors n'hésitez pas à jouer avec pendant la lecture. Surtout si vous avez des doutes sur l'un des tests, modifiez le code du test et étudiez ce qui se passe.

### Les tests

Commençons par les bases des promesses :

```
it('L\'exécuteur de promesse est exécuté DE MANIÈRE SYNCHRONE', () => {  let executorRun = false;  new Promise(function executor() {    executorRun = true;  });  expect(executorRun).toBe(true);});it('vous pouvez résoudre une promesse', (done) => {  new Promise((resolve) => setTimeout(resolve, 1))    .then(done);});it('... ou vous pouvez rejeter une promesse', (done) => {  new Promise((resolve, reject) => setTimeout(reject, 1))    .then(undefined, done);});it('Une erreur dans l\'exécuteur rejette la promesse', (done) => {  new Promise(function executor() {    throw 'Error';  }).catch(done);});
```

Il semble que lorsque vous appelez `resolve()`, le premier rappel `then(...)` est exécuté. Si vous appelez `reject()` ou si une erreur est levée, `catch()` ou le deuxième rappel de `then(...)` est exécuté.

De plus, **l'exécuteur de promesse est exécuté de manière synchrone**. Cela signifie que les promesses sont un moyen de gérer le code asynchrone, et non d'exécuter des tâches dans des threads asynchrones. Utilisez [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) si vous souhaitez exécuter du code JavaScript en dehors du thread principal.

Examinons plus en détail ce que sont ces fonctions `then(...)` et `catch()`, et ce que signifie "chaîner des promesses" :

```
// Chaînage des promesses
```

```
it('vous pouvez chaîner les promesses car .then(...) retourne une promesse', (done) => {  fetch('https://jsonplaceholder.typicode.com/posts/1')    .then(response => response.json())    .then(json => expect(json.userId).toBe(1))    .then(done);});it('vous pouvez utiliser le rappel d\'échec de .then(success, fail) pour gérer les promesses rejetées', (done) => {  Promise.reject()    .then(function success() {      throw 'Je ne dois pas être exécuté';    }, function fail() {      done();    });});it('... ou vous pouvez utiliser .catch() pour gérer les promesses rejetées', (done) => {  Promise.reject()    .then(function success() {      throw 'Je ne dois pas être exécuté';    })    .catch(done);});it('aussi .catch() retourne une promesse, permettant le chaînage des promesses', (done) => {  Promise.reject()    .catch(() => undefined)    .then(done);});it('vous devez retourner une promesse rejetée si vous voulez exécuter le prochain rappel d\'échec', (done) => {  function someApiCall() {    return Promise.reject('Error');  }  someApiCall()    .catch((err) => {      console.error(err);      // Sans la ligne ci-dessous, .catch n\'est pas appelé      return Promise.reject(err);    })    .catch(done);});it('... ou vous pouvez lever une erreur si vous voulez exécuter le prochain rappel d\'échec', (done) => {  function someApiCall() {    return Promise.reject('Error');  }  someApiCall()    .catch((err) => {      console.error(err);      throw err; // Sans cette ligne, .catch n\'est pas appelé    })    .catch(done);});it('les valeurs retournées dans les rappels .then()/.catch() sont fournies au prochain rappel', (done) => {  Promise.resolve(1)    .then(value => value + 1)    .then(value => expect(value).toBe(2));  Promise.reject(1)    .catch(value => value + 1)    .then(value => expect(value).toBe(2));  setTimeout(() => {    done();  }, 1);});
```

OK, mais qu'est-ce que `Promise.resolve()` et `Promise.reject()` ? Découvrons-le !

```
it('vous pouvez utiliser Promise.resolve() pour envelopper des valeurs ou des promesses', (done) => {  function iMayReturnAPromise() {    return Math.random() >= 0.5 ? Promise.resolve() : 5;  }
```

```
  Promise.resolve(iMayReturnAPromise()).then(done);});
```

```
it('vous pouvez utiliser Promise.resolve() pour exécuter quelque chose juste après', (done) => {  let arr = [];  Promise.resolve().then(() => arr.push(2));  arr.push(1);
```

```
  setTimeout(() => {    expect(arr).toEqual([1, 2]);    done();  }, 1);});
```

```
/** @seehttps://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules **/it('Promise.resolve() est normalement exécuté avant setTimeout(.., 0)', (done) => {  let arr = [];  setTimeout(() => arr.push('timeOut'), 0);  Promise.resolve().then(() => {    arr.push('resolve');  });
```

```
  setTimeout(() => {    expect(arr).toEqual(['resolve', 'timeOut']);    done();  }, 1);});
```

```
it('vous pouvez créer des promesses rejetées', (done) => {  Promise.reject('reason').catch(done);});
```

```
it('faites attention à "Uncaught (in promise) ..."', () => {  Promise.reject('The error');  // Affiche dans la console Uncaught (in promise) The error});
```

#### Chaînage des promesses vs. création de nouvelles

Bien que `new Promise(...)` soit un moyen de créer une promesse, vous devriez éviter de l'utiliser. La plupart du temps, les fonctions/bibliothèques retournent une promesse, donc vous devriez chaîner les promesses et non en créer de nouvelles :

```
it("Ne pas utiliser new Promise(...), préférer le chaînage", (done) => {  const url = 'https://jsonplaceholder.typicode.com/posts/1';  function badlyDesignedCustomFetch() {    return new Promise((resolve, reject) => {      fetch(url).then((response) => {        if (response.ok) {          resolve(response);        } else {          reject('Fetch failed');        }      });    });  }  function wellDesignedCustomFetch() {    return fetch(url).then((response) => {      if (!response.ok) {        return Promise.reject('Fetch failed');      }      return (response);    });  }  Promise.all([    badlyDesignedCustomFetch(),    wellDesignedCustomFetch()  ]).then(done);});
```

Mais, quand devriez-vous utiliser `new Promise(...)` ? Lorsque vous voulez passer d'une interface de rappel à une interface de promesse. Voir ci-dessous :

```
function imgOnLoad(img) {  return new Promise((resolve, reject) => {    img.onload = resolve;    img.onerror = reject;  });}
```

#### Exécution parallèle

Le chaînage des promesses est bien, mais qu'en est-il de l'exécution d'opérations asynchrones en parallèle ? Voici tout ce que vous devez savoir :

```
// Exécution parallèle des promesses
```

```
it('vous pouvez utiliser Promise.all([...]) pour exécuter des promesses en parallèle', (done) => {  const url = 'https://jsonplaceholder.typicode.com/posts';  const p1 = fetch(`${url}/1`);  const p2 = fetch(`${url}/2`);  Promise.all([p1, p2])    .then(([res1, res2]) => {      return Promise.all([res1.json(), res2.json()])    })    .then(([post1, post2]) => {      expect(post1.id).toBe(1);      expect(post2.id).toBe(2);    })    .then(done);});it('Promise.all([...]) échouera si l\'une des promesses échoue', (done) => {  const p1 = Promise.resolve(1);  const p2 = Promise.reject('Error');  Promise.all([p1, p2])    .then(() => {      fail('Je ne serai pas exécuté')    })    .catch(done);});it("si vous ne voulez pas que Promise.all() échoue, enveloppez les promesses dans une promesse qui ne échouera pas", (done) => {  function iMayFail(val) {    return Math.random() >= 0.5 ?      Promise.resolve(val) :      Promise.reject(val);  }  function promiseOr(p, value) {    return p.then(res => res, () => value);  }  const p1 = iMayFail(10);  const p2 = iMayFail(9);  Promise.all([promiseOr(p1, null), promiseOr(p2, null)])    .then(([val1, val2]) => {      expect(val1 === 10 || val1 === null).toBe(true);      expect(val2 === 9 || val2 === null).toBe(true);    })    .catch(() => {      fail('Je ne serai pas exécuté')    })    .then(done);});it('Promise.race([...]) se résoudra dès que l\'une des promesses se résoudra ou sera rejetée', (done) => {  const timeout =    new Promise((resolve, reject) => setTimeout(reject, 100));  const data =    fetch('https://jsonplaceholder.typicode.com/posts/1');  Promise.race([data, timeout])    .then(() => console.log('Fetch OK'))    .catch(() => console.log('Fetch timeout'))    .then(done);});
```

#### Syntaxe

La syntaxe des promesses est un peu complexe par rapport à la syntaxe typique du code synchrone. Il est vrai qu'en chaînant les promesses, le code conserve une bonne lisibilité, mais cela pourrait être mieux. La nouvelle **syntaxe await/async** rend l'utilisation des promesses aussi facile que l'écriture de code synchrone.

```
// Nouvelle syntaxe await/async
```

```
it('vous pouvez utiliser la nouvelle syntaxe await/async', async () => {  function timeout(ms) {    return new Promise((resolve) => setTimeout(resolve, ms));  }  const start = Date.now();  const delay = 200;  await timeout(delay + 2); // Juste une tolérance de quelques ms  expect(Date.now() - start).toBeGreaterThanOrEqual(delay);});it('une fonction async retourne une promesse', (done) => {  async function iAmAsync() {    return 1;  }  iAmAsync()    .then((val) => expect(val).toBe(1))    .then(done);});it('await attend simplement la résolution d\'une promesse', async (done) => {  await Promise.resolve();  done();});it('await lèvera une erreur si la promesse échoue', async(done) => {  try {    await Promise.reject();    fail('Je ne serai pas exécuté');  } catch (err) {    done();  }});
```

#### Fonctions synchrones

Dernière considération : lorsque vous concevez une fonction, vous devez décider si elle est synchrone ou non. Ne retournez pas une promesse juste parce que "on ne sait jamais". Utilisez des fonctions synchrones "normales" lorsque cela est possible.

Tous les tests sont [ici](https://jsfiddle.net/kouty79/e52qkkmu/), sur JSFiddle.

C'est tout ! J'espère que vous avez apprécié cet article.