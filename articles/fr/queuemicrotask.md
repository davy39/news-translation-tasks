---
title: Une introduction à queueMicrotask de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-08T18:11:45.000Z'
originalURL: https://freecodecamp.org/news/queuemicrotask
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca077740569d1a4ca48d3.jpg
tags:
- name: api
  slug: api
- name: asynchronous programming
  slug: asynchronous-programming
- name: Browsers
  slug: browsers
- name: JavaScript
  slug: javascript
seo_title: Une introduction à queueMicrotask de JavaScript
seo_desc: "By Ujjwal Gupta\nIntroduction\nqueueMicrotask is a new browser API which\
  \ can be used to convert your synchronous code into async:\nqueueMicrotask(() =>\
  \ {\n    console.log('hey i am executed asychronously by queueMicrotask');\n});\n\
  \nIt's similar to what we ..."
---

Par Ujjwal Gupta

## Introduction

**queueMicrotask** est une nouvelle API de navigateur qui peut être utilisée pour convertir votre code synchrone en asynchrone :

```javascript
queueMicrotask(() => {
    console.log('hey i am executed asychronously by queueMicrotask');
});
```

C'est similaire à ce que nous faisions avec setTimeout :

```javascript
setTimeout(() => {
    console.log('hey i am executed asychronously by setTimeout');
}, 0);
```

Alors, à quoi sert **queueMicrotask** alors que nous avons déjà **setTimeout** ?

> **queueMicrotask** ajoute la fonction (tâche) dans une file d'attente et chaque fonction est exécutée une par une (FIFO) après que la tâche actuelle a terminé son travail et qu'il n'y a pas d'autre code en attente d'être exécuté avant que le contrôle du contexte d'exécution ne soit rendu à la boucle d'événements du navigateur.

En gros, les tâches de **queueMicrotask** sont exécutées juste après que la pile d'appels actuelle est vide, avant de passer l'exécution à la boucle d'événements.

> Dans le cas de **setTimeout**, chaque tâche est exécutée à partir de la file d'événements, après que le contrôle a été donné à la boucle d'événements.

Alors, si nous exécutons **setTimeout** en premier et ensuite **queueMicrotask**, lequel sera appelé en premier ? Exécutez le code ci-dessous et vérifiez par vous-même :

```javascript
setTimeout(() => {
    console.log('hey i am executed asychronously by setTimeout');
},0);

queueMicrotask(() => {
    console.log('hey i am executed asychronously by queueMicrotask');
}); 
```

Node.js fait la même chose avec "process.nextTick".

## Quand l'utiliser

Il n'y a pas de règle pour savoir quand utiliser **queueMicrotask**, mais il peut être utilisé intelligemment pour exécuter un morceau de code sans arrêter l'exécution actuelle.

Par exemple, supposons que nous avons un tableau où nous maintenons une liste de valeurs. Après chaque insertion de valeur, nous trions le tableau pour que la recherche de valeurs soit plus rapide.

```
var arr=[];

function add(value){
  arr.push(value);
  arr.sort();
}
```

Cependant, la recherche d'un élément est effectuée chaque fois que quelqu'un utilise une boîte de recherche. Cela signifie que le gestionnaire d'événements sera appelé après que le contrôle a été transféré à la boucle d'événements, donc le tri des données bloque l'exécution d'autres codes synchrones importants.

Voici comment nous pouvons utiliser **queueMicrotask** pour améliorer notre code :

```javascript
var arr = [];

function add(value) {
  arr.push(value);
  queueMicrotask(() => {
    arr.sort();
  })
}
```

## Références

* [https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/queueMicrotask)