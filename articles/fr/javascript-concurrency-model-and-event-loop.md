---
title: Modèle de concurrence JavaScript et boucle d'événements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-13T21:46:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-concurrency-model-and-event-loop
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9de6740569d1a4ca3a44.jpg
tags:
- name: concurrency
  slug: concurrency
- name: JavaScript
  slug: javascript
seo_title: Modèle de concurrence JavaScript et boucle d'événements
seo_desc: Javascript runtime is single threaded which means that it can execute one
  piece of code at a time. In order to understand the concurrency model and the event
  loop in Javascript we have to first get to know some common terms that are associated
  with i...
---

L'environnement d'exécution JavaScript est monothread, ce qui signifie qu'il ne peut exécuter qu'un seul morceau de code à la fois. Pour comprendre le modèle de concurrence et la boucle d'événements en JavaScript, nous devons d'abord nous familiariser avec certains termes courants qui y sont associés. 

## La pile d'appels

Commençons par apprendre ce qu'est une pile d'appels.

Une pile d'appels est une structure de données simple qui enregistre où nous en sommes dans le code. Ainsi, si nous entrons dans une fonction, c'est-à-dire une invocation de fonction, elle est poussée dans la pile d'appels. Lorsque nous revenons d'une fonction, elle est retirée de la pile.

Examinons un exemple de code pour comprendre la pile d'appels :

```javascript
function multiply(x, y) {
   return x * y;
}

function squared(n) {
     return multiply(n, n)
  }

function printSquare(n) {
   return squared(n)
}

let numberSquared = printSquare(5);
console.log(numberSquared);
```

Tout d'abord, lorsque le code s'exécute, l'environnement d'exécution lira chaque définition de fonction. Mais lorsqu'il atteint la ligne où la première fonction **printSquare(5)** est invoquée, il poussera cette fonction dans la pile d'appels. 

Ensuite, cette fonction s'exécutera. Avant de retourner, elle rencontrera une autre fonction, **squared(n)**, donc elle suspendra son opération actuelle et poussera cette fonction au-dessus de la fonction existante. 

Elle exécute la fonction (dans ce cas, la fonction squared) et enfin elle rencontre une autre fonction **multiply(n, n)**. Ensuite, elle suspend ses exécutions actuelles et pousse cette fonction dans la pile d'appels. La fonction multiply s'exécute et retourne avec la valeur multipliée. 

Enfin, la fonction squared retourne et est retirée de la pile, puis il en va de même pour printSquare. La valeur finale au carré est allouée à la variable numberSquared. 

Nous rencontrons à nouveau une invocation de fonction (dans ce cas, il s'agit d'une instruction console.log()) donc l'environnement d'exécution pousse cela dans la pile. Cela l'exécute, imprimant ainsi le nombre au carré sur la console. 

Notez que la première fonction qui est poussée dans la pile avant que l'un des codes ci-dessus ne s'exécute est la fonction principale. Dans l'environnement d'exécution, cela est désigné comme une fonction 'anonyme'.

Donc, pour résumer : chaque fois qu'une fonction est invoquée, elle est poussée dans la pile d'appels où elle s'exécute. Enfin, lorsque la fonction a terminé son exécution et retourne soit implicitement soit explicitement, elle sera retirée de la pile. 

La pile d'appels enregistre simplement à quel moment quelle fonction était en cours d'exécution. Et elle garde une trace de la fonction qui est actuellement en cours d'exécution.

## Le navigateur

Maintenant, nous savons que JavaScript peut exécuter une chose à la fois, mais ce n'est pas le cas avec le navigateur. Le navigateur dispose de son propre ensemble d'API comme setTimeout et XMLHttpRequests qui ne sont pas spécifiées dans l'environnement d'exécution JavaScript. 

En fait, si vous parcourez le code source de V8, le populaire environnement d'exécution JavaScript qui alimente les navigateurs comme Google Chrome, vous ne trouverez aucune définition pour cela. C'est parce que ces API web spéciales existent dans l'environnement du navigateur et non à l'intérieur de l'environnement JavaScript. Donc, vous pouvez dire que ces API introduisent de la concurrence dans le mélange. 

Examinons un diagramme pour comprendre le tableau complet.

![Modèle de concurrence et boucle d'événements](https://i.imgur.com/rnQEY7o.png)

D'autres termes sont introduits ici, alors passons-les en revue :

**Heap** : C'est surtout l'endroit où les objets sont alloués.

**File d'attente de rappels** : C'est une structure de données qui stocke tous les rappels. Puisqu'il s'agit d'une file d'attente, les éléments sont traités selon le principe FIFO, c'est-à-dire premier entré, premier sorti.

**Boucle d'événements** : C'est là que toutes ces choses se rejoignent. La boucle d'événements vérifie simplement la pile d'appels, et si elle est vide (ce qui signifie qu'il n'y a pas de fonctions dans la pile), elle prend le rappel le plus ancien de la file d'attente de rappels et le pousse dans la pile d'appels, ce qui exécute finalement le rappel.

Comprenons cela avec un exemple de code :

```javascript
console.log('hi');

setTimeout(function() {
     console.log('freecodeCamp')
}, 5000);

console.log('JS')
```

Lorsque la première ligne s'exécute, il s'agit d'un console.log(). Il s'agit d'une invocation de fonction, ce qui signifie que cette fonction est poussée dans la pile d'appels où elle s'exécute en imprimant 'hi' sur la console. Enfin, elle est retournée et retirée de la pile. 

Ensuite, lorsque l'environnement d'exécution va exécuter setTimeout(), il sait qu'il s'agit d'une API web. Par conséquent, il la donne au navigateur pour gérer son exécution. Le navigateur démarre le minuteur, puis l'environnement d'exécution JavaScript retire setTimeout() de la pile. Il rencontre une autre invocation console.log() et la pousse donc dans la pile d'appels, le message 'JS' est enregistré dans la console, puis il est finalement retourné. Ensuite, le dernier console.log() est retiré de la pile. Maintenant, la pile d'appels est vide. 

Pendant ce temps, alors que tout cela se passait, le minuteur se termine. Lorsque 5 secondes se sont écoulées, le navigateur pousse la fonction de rappel dans la file d'attente de rappels. 

Ensuite, la boucle d'événements vérifie si la pile d'appels est libre ou non. Puisqu'elle est libre, elle prend la fonction de rappel et la pousse à nouveau dans la pile d'appels, ce qui exécute le code à l'intérieur. 

À nouveau, à l'intérieur du code, il y a une invocation console.log(), donc cette fonction va au sommet de la pile, s'exécute, ce qui enregistre 'freecodecamp' dans la console, et enfin elle retourne. Cela signifie qu'elle est retirée de la pile et enfin le rappel est retiré de la pile et nous avons terminé.

Pour mieux visualiser cela, essayez cet outil de Phillip Roberts : [Loupe Event Loop Visualizer](http://latentflip.com/loupe/?code=!!!PGJ1dHRvbj5DbGljayBtZSE8L2J1dHRvbj4%3D)