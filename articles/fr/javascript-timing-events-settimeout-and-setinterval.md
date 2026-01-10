---
title: 'Événements de temporisation JavaScript : setTimeout et setInterval'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-timing-events-settimeout-and-setinterval
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ce8740569d1a4ca34d2.jpg
tags:
- name: events
  slug: events
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: 'Événements de temporisation JavaScript : setTimeout et setInterval'
seo_desc: 'Programmers use timing events to delay the execution of certain code, or
  to repeat code at a specific interval.

  There are two native functions in the JavaScript library used to accomplish these
  tasks: setTimeout() and setInterval().

  setTimeout

  setTim...'
---

Les programmeurs utilisent les événements de temporisation pour retarder l'exécution de certains codes, ou pour répéter du code à des intervalles spécifiques.

Il existe deux fonctions natives dans la bibliothèque JavaScript utilisées pour accomplir ces tâches : `setTimeout()` et `setInterval()`.

### setTimeout

`setTimeout()` est utilisé pour retarder l'exécution de la fonction passée d'une quantité de temps spécifiée.

Il y a deux paramètres que vous passez à `setTimeout()` : la fonction que vous souhaitez appeler, et la quantité de temps en millisecondes pour retarder l'exécution de la fonction.

Rappelez-vous qu'il y a 1000 millisecondes (ms) dans une seconde, donc 5000 ms est égal à 5 secondes.

`setTimeout()` exécutera la fonction du premier argument une fois après que le temps spécifié se soit écoulé.

**Exemple :**

```javascript
let timeoutID;

function delayTimer() {
  timeoutID = setTimeout(delayedFunction, 3000);
}

function delayedFunction() {
  alert("Three seconds have elapsed.");
}
```

Lorsque la fonction `delayTimer` est appelée, elle exécutera `setTimeout`. Après 3 secondes (3000 ms), elle exécutera `delayedFunction` qui enverra une alerte.

**setInterval**

Utilisez `setInterval()` pour spécifier une fonction à répéter avec un délai entre les exécutions.

Encore une fois, deux paramètres sont passés à `setInterval()` : la fonction que vous souhaitez appeler, et la quantité de temps en millisecondes pour retarder chaque appel de la fonction.

`setInterval()` continuera à s'exécuter jusqu'à ce qu'il soit effacé.

**Exemple :**

```javascript
let intervalID;

function repeatEverySecond() {
  intervalID = setInterval(sendMessage, 1000);
}

function sendMessage() {
  console.log("One second elapsed.");
}
```

Lorsque votre code appelle la fonction `repeatEverySecond`, elle exécutera `setInterval`. `setInterval` exécutera la fonction `sendMessage` chaque seconde (1000 ms).

### clearTimeout et clearInterval

Il existe également des fonctions natives correspondantes pour arrêter les événements de temporisation : `clearTimeout()` et `clearInterval()`.

Vous avez peut-être remarqué que chaque fonction de temporisation ci-dessus est enregistrée dans une variable. Lorsque la fonction `setTimeout` ou `setInterval` s'exécute, un numéro lui est attribué et enregistré dans cette variable. Notez que JavaScript fait tout cela en arrière-plan.

Ce numéro généré est unique pour chaque instance de temporisateurs. Ce numéro attribué est également la manière dont les temporisateurs sont identifiés lorsque vous souhaitez les arrêter. Pour cette raison, vous devez toujours définir votre temporisateur dans une variable.

Pour la clarté de votre code, vous devez toujours associer `clearTimeout()` à `setTimeout()` et `clearInterval()` à `setInterval()`.

Pour arrêter un temporisateur, appelez la fonction clear correspondante et passez-lui la variable d'ID du temporisateur qui correspond au temporisateur que vous souhaitez arrêter. La syntaxe pour `clearInterval()` et `clearTimeout()` est la même.

**Exemple :**

```javascript
let timeoutID;

function delayTimer() {
  timeoutID = setTimeout(delayedFunction, 3000);
}

function delayedFunction() {
  alert("Three seconds have elapsed.");
}

function clearAlert() {
  clearTimeout(timeoutID);
}
```