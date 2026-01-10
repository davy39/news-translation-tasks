---
title: Impossible de passer une valeur d'entrée dans une variable JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:16:00.000Z'
originalURL: https://freecodecamp.org/news/cant-pass-an-input-value-into-a-javascript-variable
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa4740569d1a4ca26d3.jpg
tags:
- name: error
  slug: error
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
- name: variables
  slug: variables
seo_title: Impossible de passer une valeur d'entrée dans une variable JavaScript
seo_desc: 'Imagine the following scenario – you have a simple input and a button.
  When a user types into the input and presses the button, the text from the input
  should be logged to the console.

  Here''s what you have so far:

  <input id="search" placeholder="Sear...'
---

Imaginez le scénario suivant – vous avez une entrée simple et un bouton. Lorsque l'utilisateur tape dans l'entrée et appuie sur le bouton, le texte de l'entrée doit être enregistré dans la console.

Voici ce que vous avez jusqu'à présent :

```html
<input id="search" placeholder="Rechercher..."></input>
<button value='send' id="submit" onclick="myFunction()">Rechercher</button>

<div id="alpha"></div>
```

```js
function myFunction() {
  const test = document.getElementById("search").value;
}

console.log(test);
```

Mais lorsque vous chargez la page, vous voyez `Uncaught ReferenceError: test is not defined` dans la console.

Que se passe-t-il ici, et pourquoi ne pouvez-vous pas accéder à la variable `test` en dehors de `myFunction` ?

## Portée en JavaScript

La raison pour laquelle vous ne pouvez pas accéder à `test` en dehors de `myFunction` est due à la [portée](https://developer.mozilla.org/en-US/docs/Glossary/Scope). Une autre façon de décrire la portée est le contexte.

Parce que `test` a été défini ou créé dans `myFunction`, il n'est disponible que dans le contexte ou la portée de `myFunction` lui-même. Essayer d'enregistrer `test` en dehors de `myFunction` provoquera une erreur.

Une autre façon de le dire est que la variable `test` est limitée à la fonction et ne peut être enregistrée que depuis `myFunction`.

Une façon simple de corriger cela est d'enregistrer `test` depuis `myFunction`. Ensuite, chaque fois que le bouton est pressé, la valeur actuelle de l'entrée sera enregistrée dans la console :

```js
function myFunction() {
  const test = document.getElementById("search").value;
  console.log(test);
}
```

Vous pouvez en savoir plus sur la portée en JavaScript ici : [Une introduction à la portée en JavaScript](https://www.freecodecamp.org/news/an-introduction-to-scope-in-javascript-cbd957022652/)

## Comment accéder à une variable en dehors d'une fonction

Bien qu'il ne soit pas possible d'accéder directement à une variable limitée à une fonction depuis l'extérieur de la fonction dans laquelle elle a été définie, il existe des moyens d'utiliser la valeur de `test` dans le reste du programme.

### Stocker la valeur de `test` en tant que variable globale

La portée globale est le niveau le plus élevé de votre programme, en dehors de toutes les autres fonctions. Les variables dans la portée globale sont disponibles dans le reste de votre programme.

Ainsi, une façon simple de rendre `test` disponible partout est de l'enregistrer en tant que variable globale. Par exemple :

```js
let test = '';

function myFunction() {
  test = document.getElementById("search").value;
}

function myOtherFunction() {
  console.log(test);
}
```

Ensuite, vous pourriez accéder à la valeur de `test` lorsque `myOtherFunction` est appelée. Mais cela suppose que l'entrée contient déjà du texte et que `myFunction`, qui définit la valeur de `test`, est appelée avant `myOtherFunction`.

C'est là qu'une bonne compréhension de JavaScript asynchrone est utile. Lisez-en plus dans cet article : [L'évolution de JavaScript asynchrone : des callbacks, aux promesses, à Async/Await](https://www.freecodecamp.org/news/the-evolution-of-async-javascript-from-callbacks-to-promises-to-async-await-e73b047f2f40/)

### Retourner test depuis la fonction

Une autre façon d'accéder à `test` depuis l'extérieur de la fonction d'origine dans laquelle il est défini est de simplement le retourner depuis cette fonction. Ensuite, lorsque vous l'appelez depuis une autre fonction, vous aurez accès à `test`.

Ensuite, vous pouvez créer un autre bouton pour ajouter la valeur de `test` à la page et attacher `myOtherFunction` à ce bouton.

Par exemple :

```html
<input id="search" placeholder="Rechercher..."></input>
<button value='send' id="submit" onclick="myFunction()">Rechercher</button>
<button value='append' id="append" onclick="myOtherFunction()">Ajouter</button>

<div id="alpha"></div>
```

```js
function myFunction() {
  const test = document.getElementById("search").value;
  return test;
}

function myOtherFunction() {
  const myDiv = document.getElementById("alpha");
  myDiv.innerText = myFunction();
}
```

Et voici le résultat en action :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Peek-2020-06-10-20-46.gif)