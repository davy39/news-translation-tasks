---
title: Oh Oui ! Async / Await
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-04T20:12:00.000Z'
originalURL: https://freecodecamp.org/news/oh-yes-async-await-f54e5a079fc1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Dp72fOGQa4WJy7M786c9ew.gif
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Oh Oui ! Async / Await
seo_desc: 'By Tiago Lopes Ferreira

  async/await is the new JavaScript syntax to declare an asynchronous function. It’s
  built on Promises, but is easier to use.

  A thorough explanation of Promises is beyond the scope of this article. If you are
  new to Promises in ...'
---

Par Tiago Lopes Ferreira

**async**/**await** est la nouvelle syntaxe JavaScript pour déclarer une fonction asynchrone. Elle est basée sur les Promesses, mais est plus facile à utiliser.

Une explication approfondie des Promesses dépasse le cadre de cet article. Si vous êtes nouveau dans l'utilisation des Promesses en JavaScript, veuillez consulter [Utiliser les promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) pour en savoir plus. Il n'est pas essentiel d'être un expert en promesses, mais une bonne introduction vous aidera à apprendre **async**/**await**.

Voici un rappel rapide de la façon d'écrire et d'utiliser une promesse.

### Promesses

Une Promesse représente une valeur qui sera disponible maintenant, dans le futur, ou (possiblement) jamais.

L'état d'une Promesse peut être l'un des suivants :

* **en attente** — la Promesse n'a été ni résolue ni rejetée. Elle représente l'état initial d'une Promesse.
* **résolue** — l'opération, enveloppée par la Promesse, s'est terminée avec succès.
* **rejetée** — l'opération a échoué.

`getRandomWithPromise()` définit une Promesse qui se résout avec une valeur de nombre aléatoire. `setTimeout()` simule un délai pour une tâche asynchrone telle qu'une requête HTTP.

Voici un exemple de la façon dont nous pouvons utiliser `getRandomWithPromise()`.

### async/await

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dp72fOGQa4WJy7M786c9ew.gif)

**async**/**await** est une paire mot-clé+opérateur qui simplifie le code asynchrone.

* **async** déclare que la fonction est asynchrone.
* **await** est l'opérateur utilisé pour attendre qu'une promesse soit remplie. Il ne peut être utilisé qu'à l'intérieur d'une fonction **async**.

Construisons un exemple, en utilisant la fonction `getRandomWithAsync()` et **async**/**await**.

La première chose à remarquer est que le mot-clé async déclare que la fonction est asynchrone.

L'opérateur **await** met en pause `getRandomWithPromise()` jusqu'à ce que la promesse soit remplie.

Lorsque la promesse est remplie, elle peut être :

**résolue** — ce qui signifie que **await** retournera la valeur résolue.

**rejetée** — ce qui signifie que **await** lèvera la valeur rejetée.

Parce qu'une promesse peut lever une erreur inattendue, il est important d'envelopper notre code à l'intérieur d'un bloc **try**/**catch**.

Notez que le corps de `getRandomWithAsync()` se lit comme s'il s'agissait d'une fonction synchrone. C'est l'un des avantages de **async**/**await**. Cela rend la logique du code facile à suivre, même si elle effectue un travail compliqué.

Il n'est plus nécessaire d'avoir une indentation comme avec une [chaîne de promesses](https://javascript.info/promise-chaining).

### await

Il est important de se souvenir que **await** ne peut être utilisé qu'à l'intérieur d'une fonction **async**. Sinon, vous obtiendrez une erreur de syntaxe.

Voici comment utiliser **await** avec une Expression de Fonction Invocable Immédiatement ([IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)).

### Classes

Nous pouvons également créer des fonctions **async** à l'intérieur des classes.

### Promesses Multiples

Que faire si nous avons plus d'une promesse à remplir avant de continuer ?

Nous pouvons le faire de deux manières — séquentiellement ou concurremment.

### Séquentiel

La promesse b n'est exécutée qu'après que la promesse a soit remplie. Ainsi, le temps d'exécution de la fonction est la somme du temps d'exécution des promesses a et b.

Cela peut être un problème de performance majeur. La bonne nouvelle est que nous pouvons exécuter les deux promesses concurremment pour gagner du temps.

### Concurrent

Nous pouvons exécuter les deux promesses en parallèle en modifiant le code. Si vous demandez les nombres aléatoires et sauvegardez les promesses, elles s'exécuteront concurremment. Nous attendons que les deux promesses se complètent en utilisant **await** dans des expressions séparées. Le résultat est affiché lorsqu'elles sont toutes les deux complètes.

Le temps d'exécution de la fonction est égal à celui de la promesse qui prend le plus de temps.

### Concurrent (avec Promise.all)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XmtzVJeT4cYJuwAXmZk5Lw.gif)

Nous pouvons également utiliser `Promise.all` pour la concurrence.

L'un des avantages est que `Promise.all` a un comportement de défaillance rapide. Si une promesse échoue, Promise.all n'attendra pas que les autres promesses soient remplies. Elle rejette immédiatement.

### await et thenable

L'utilisation de l'opérateur **await** n'est pas limitée aux promesses. **await** convertira toute valeur non-promise en une valeur de promesse. Il le fait en enveloppant la valeur dans `Promise.resolve`.

**await** peut être utilisé avec n'importe quel objet qui a une méthode `.then()`. Cet objet est également connu sous le nom de _thenable_.

### Conclusion

Nous avons maintenant la nouvelle syntaxe **async**/**await** de JavaScript pour écrire du code asynchrone.

**async** est le mot-clé qui spécifie qu'une fonction est asynchrone.

**await** est l'opérateur utilisé pour attendre qu'une promesse soit remplie.

La syntaxe **async**/**await** fait ressembler le code asynchrone à du code synchrone. Cela rend le code plus facile à lire et à comprendre.

N'oubliez pas que les promesses peuvent générer des erreurs inattendues. Il est important d'envelopper le code à l'intérieur d'un bloc **try**/**catch** pour les gérer.

Vous pouvez gérer plusieurs promesses de deux manières : séquentiellement ou concurremment. La concurrence a l'avantage car les promesses peuvent s'exécuter en parallèle.

Enfin, l'opérateur **await** n'est pas limité aux promesses. Nous pouvons l'utiliser avec n'importe quel objet ayant une méthode `.then()` (c'est-à-dire un thenable).

![Image](https://cdn-media-1.freecodecamp.org/images/1*g6-Vw7Ar5l1jNanUX_DGrA.gif)

### Remerciements à ?

* [Brian Terlson](https://twitter.com/bterlson) pour sa [Proposition de Fonctions Asynchrones](https://github.com/tc39/ecmascript-asyncawait)
* [Nicolás Bevacqua](https://twitter.com/nzgb) pour ce [PonyFoo — Comprendre l'async await de JavaScript](https://ponyfoo.com/articles/understanding-javascript-async-await)
* [MDN — fonction async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
* À tous les fans de [Adventure Time](https://www.youtube.com/watch?v=68dkSmglu4Y)

_N'oubliez pas de consulter mes articles sur ES6_

[**Démystifier les Itérables et Itérateurs ES6**](https://medium.freecodecamp.org/demystifying-es6-iterables-iterators-4bdd0b084082)
[_Démystifions la nouvelle façon de JavaScript d'interagir avec les structures de données._medium.freecodecamp.org](https://medium.freecodecamp.org/demystifying-es6-iterables-iterators-4bdd0b084082)
[**Explorons les Générateurs ES6**](https://medium.freecodecamp.org/lets-explore-es6-generators-5e58ed23b0f1)
[_Générateurs, alias, une implémentation des itérables._medium.freecodecamp.org](https://medium.freecodecamp.org/lets-explore-es6-generators-5e58ed23b0f1)