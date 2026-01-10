---
title: Async et Await en JavaScript Expliqués en Faisant une Pizza
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-30T20:20:59.000Z'
originalURL: https://freecodecamp.org/news/async-await-javascript-tutorial-explained-by-making-pizza
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/carissa-gan-_0JpjeqtSyg-unsplash.jpg
tags:
- name: async/await
  slug: asyncawait
- name: asynchronous
  slug: asynchronous
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Async et Await en JavaScript Expliqués en Faisant une Pizza
seo_desc: 'By Dave Gray

  Async and await might sound complicated...but they''re as easy as pizza pie once
  you dive in.

  We all use async and await in our daily routines.

  What is an async task?

  An async task lets you complete other tasks while the async task is sti...'
---

Par Dave Gray

Async et await peuvent sembler compliqués... mais ils sont aussi simples qu'une pizza une fois que vous vous y plongez.

Nous utilisons tous async et await dans nos routines quotidiennes.

## Qu'est-ce qu'une tâche asynchrone ?

Une tâche asynchrone vous permet de compléter d'autres tâches pendant que la tâche asynchrone est encore en cours d'exécution.

### Voici quelques exemples de tâches asynchrones du quotidien

#### Exemple 1 :

Vous commandez de la nourriture dans un drive-in, ce qui lance votre demande de nourriture (une tâche asynchrone).

Vous avancez dans la file du drive-in (la tâche suivante), pendant que votre nourriture est préparée.

Vous n'avez pas eu à attendre que votre nourriture soit prête avant de pouvoir avancer.

Vous attendez votre nourriture et votre demande est satisfaite à la fenêtre de retrait.

#### Exemple 2 :

Vous lavez le sol de votre cuisine.

Pendant que vous attendez que le sol de votre cuisine sèche, vous passez l'aspirateur sur le tapis de votre chambre.

La tâche initiale était de nettoyer le sol de votre cuisine, et la tâche est terminée lorsque le sol est sec.

Rester là à attendre que le sol sèche n'est pas très productif, alors vous avez passé l'aspirateur dans la chambre pendant que le sol de la cuisine séchait.

*C'est ainsi que JavaScript gère les fonctions asynchrones, aussi.*

### Exemple d'Async/Await – Cuire une Pizza Surgelée

Vous décidez de cuire une pizza dans votre four, et votre première étape est de préchauffer le four.

Vous réglez donc la température souhaitée et commencez à préchauffer le four.

Pendant que le four préchauffe, vous sortez la pizza surgelée du congélateur, ouvrez la boîte et la placez sur une plaque à pizza.

Il vous reste du temps !

Peut-être prendre une boisson et regarder la télévision en attendant que le four bippe pour signaler qu'il est prêt.

Voici un exemple de code pour simuler cela :

```js
// Cette fonction asynchrone simule la réponse du four
const ovenReady = async () => {
  return new Promise(resolve => setTimeout(() => {
    resolve('Bip ! Four préchauffé !')
  }, 3000));
}

// Définir la fonction asynchrone preheatOven
const preheatOven = async () => {
  console.log('Préchauffage du four.');
  const response = await ovenReady();
  console.log(response);
}

// Définir les autres fonctions
const getFrozenPizza = () => console.log('Prendre la pizza.');
const openFrozenPizza = () => console.log('Ouvrir la pizza.');
const getPizzaPan = () => console.log('Prendre la plaque.');
const placeFrozenPizzaOnPan = () => console.log('Mettre la pizza sur la plaque.');
const grabABeverage = () => console.log('Prendre une boisson.');
const watchTV = () => console.log('Regarder la télévision.');

// Maintenant, appeler les fonctions
preheatOven();
getFrozenPizza();
openFrozenPizza();
getPizzaPan();
placeFrozenPizzaOnPan();
grabABeverage();
watchTV();

// Séquence de sortie dans la console :
Préchauffage du four.
Prendre la pizza.
Ouvrir la pizza.
Prendre la plaque.
Mettre la pizza sur la plaque.
Prendre une boisson.
Regarder la télévision.
Bip ! Four préchauffé !

Le processus ci-dessus est exactement ce que font async et await.

Pendant que nous `await` pour que la fonction asynchrone `preheatOven` se termine, nous pouvons effectuer des tâches synchrones comme `getFrozenPizza`, `openFrozenPizza`, `getPizzaPan`, `placeFrozenPizzaOnPan`, `grabABeverage` et même `watchTV`.

### Nous effectuons des tâches asynchrones comme cela tout le temps

Et c'est ainsi que fonctionne le JavaScript `async`, aussi.

Remarquez que lorsque nous `await` une réponse d'une fonction `async`, elle doit être appelée dans une autre fonction `async`. C'est ce que nous voyons ci-dessus lorsque `ovenReady` est appelée à l'intérieur de `preheatOven`.

### Deux points clés à retenir :

1. JavaScript ne va PAS attendre qu'une fonction `async` comme `preheatOven` se termine avant de passer aux tâches suivantes comme `getFrozenPizza` et `openFrozenPizza`.
2. JavaScript va `await` qu'une fonction `async` comme `ovenReady` se termine et retourne des données avant de passer à la tâche suivante dans une fonction asynchrone parente. Nous le voyons lorsque l'instruction `console.log(response)` ne s'exécute pas tant que `ovenReady` n'a pas retourné une réponse.

## Si l'exemple de la pizza ne vous suffit pas...

Je sais que les exemples du quotidien aident certains d'entre nous, mais d'autres préfèrent peut-être du vrai code.

Par conséquent, je vais fournir un exemple moins abstrait d'async et await en JavaScript ci-dessous qui demande des données avec l'API Fetch :

## Exemple de Code d'Async/Await en JavaScript

```js
const getTheData = async () => {
    try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!response.ok) throw Error();
    const data = await response.json();
    // faire quelque chose avec ces données... sauvegarder dans la db, mettre à jour le DOM, etc.
    console.log(data);
    console.log('Vous verrez ceci en dernier.')
    } catch (err) {
        console.error(err);
    }
} 

getTheData();
console.log('Vous verrez ceci en premier.');
```




# Conclusion

J'espère vous avoir aidé à comprendre async et await en JavaScript.

Je sais que cela peut prendre un certain temps pour bien comprendre.

Commencez à préchauffer votre four pour la pizza que vous désirez et regardez d'autres exemples d'async et await pendant que vous attendez le bip !

Je vous laisse avec un tutoriel de ma chaîne YouTube. La vidéo donne une explication plus approfondie et plus d'exemples de code, y compris une discussion sur les callbacks, les promesses, les thenables et l'API Fetch ainsi qu'async & await :

%[https://youtu.be/VmQ6dHvnKIM]