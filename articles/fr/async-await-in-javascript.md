---
title: Comment utiliser Async/Await en JavaScript avec un exemple de code JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-02T18:11:00.000Z'
originalURL: https://freecodecamp.org/news/async-await-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--12-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser Async/Await en JavaScript avec un exemple de code JS
seo_desc: 'By Nishant Kumar

  In this tutorial, we are going to learn how to use Async/Await in JavaScript.

  But before we get there, we should understand a few topics like:


  Event loops

  Callbacks

  Promises


  What are Event Loops in JavaScript?

  Event loops are one o...'
---

Par Nishant Kumar

Dans ce tutoriel, nous allons apprendre comment utiliser Async/Await en JavaScript.

Mais avant d'y arriver, nous devons comprendre quelques sujets comme :

1. Boucles d'événements
2. Fonctions de rappel (Callbacks)
3. Promesses (Promises)

## Qu'est-ce que les boucles d'événements en JavaScript ?

Les boucles d'événements sont l'un des aspects les plus importants de JavaScript.

JavaScript est un langage de programmation mono-thread, ce qui signifie qu'une seule tâche peut s'exécuter à la fois. Il possède une pile d'appels et tout le code est exécuté à l'intérieur de cette pile d'appels. Comprenons avec un exemple.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--8-.png)

Dans l'exemple ci-dessus, nous pouvons voir que nous enregistrons deux valeurs dans la console.

Lorsque `First()` termine son exécution, il sera retiré de la pile d'appels et la boucle d'événements passera à la ligne suivante. La ligne suivante sera stockée dans la pile d'appels et sera marquée pour exécution.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--9-.png)

Notre console affichera le résultat suivant :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--18-.png)

Pour mieux comprendre les choses, prenons un autre exemple.

```javascript
console.log('First!');

setTimeout(function second(){
    console.log('Timed Out!')
}, 0000)

console.log('Final!');
```

Comme d'habitude, notre code sera déplacé dans la pile d'appels et la boucle d'événements parcourra ligne par ligne.

Nous obtiendrons « First! » dans la console et il sera retiré de la pile d'appels.

Maintenant, la boucle d'événements passera à la deuxième ligne et la poussera dans la pile d'appels. Elle rencontrera la fonction `setTimeout`, qui est une macro-tâche, et elle sera exécutée dans la prochaine boucle d'événements.

Et maintenant, vous vous demandez peut-être ce qu'est une macro-tâche. Eh bien, c'est une tâche qui s'exécute après toutes les tâches dans la boucle d'événements, ou vous pourriez dire, dans l'autre boucle d'événements. Les fonctions `SetTimeout` et `SetInterval` peuvent être des exemples de macro-tâches qui s'exécutent après que toutes les autres tâches sont terminées.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--19-.png)

Enfin, la dernière ligne de code sera exécutée. Nous obtiendrons First dans notre console, puis Final, et enfin Timed Out.

## Comment fonctionnent les fonctions de rappel (Callbacks) en JavaScript ?

Les fonctions de rappel sont celles qui ont été passées à une autre fonction en tant qu'argument.

Prenons un exemple.

```javascript
const movies = [
{ title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
{ title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

getMovies();
```

Nous avons un tableau qui contient la liste des films Star Wars et une fonction `getMovies()` pour récupérer la liste.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--20-.png)

Créons une autre fonction appelée `createMovie()`. Elle sera utilisée pour ajouter un nouveau film.

```javascript
const movies = [
        { title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
        { title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }
    ]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

function createMovies(movie){
    setTimeout(() => {
        movies.push(movie)
    }, 2000);
}

getMovies();


createMovies({ title: `Return of the Jedi`, body:`Luke Skywalker attempts to bring his father back to the light side of the Force. At the same time, the rebels hatch a plan to destroy the second Death Star.` });
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--20--1.png)

Mais le problème ici est que nous n'obtenons pas le troisième film sur la console. C'est parce que `createMovie()` prend plus de temps que `getMovies()`. La fonction `createMovie()` a pris deux secondes mais `getMovies()` n'en a pris qu'une seule.

En d'autres termes, `getMovies()` s'exécute avant `createMovies()` et la liste des films est déjà affichée.

Pour résoudre cela, nous pouvons utiliser des fonctions de rappel (Callbacks).

Dans `createPost()`, passez une fonction de rappel et appelez la fonction juste après que le nouveau film est ajouté (au lieu d'attendre deux secondes).

```javascript
const movies = [
        { title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
        { title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }
    ]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

function createMovies(movie, callback){
    setTimeout(() => {
        movies.push(movie);
        callback();
    }, 2000);
}


createMovies({ title: `Return of the Jedi`, 
                body:`Luke Skywalker attempts to bring his father back to the light side of the Force. 
                At the same time, the rebels hatch a plan to destroy the second Death Star.` }, getMovies);
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--21--2.png)

Maintenant, nous obtenons la liste mise à jour des films.

## Comment fonctionnent les promesses (Promises) en JavaScript ?

Une promesse est une valeur qui peut produire une valeur dans le futur. Cette valeur peut être résolue ou non résolue (dans certains cas d'erreur, comme une défaillance réseau). Cela fonctionne comme une promesse dans la vie réelle.

Elle a trois états : remplie, rejetée ou en attente.

* **Remplie :** `onFulfilled()` sera appelée (par exemple, `resolve()` a été appelée).
* **Rejetée :** `onRejected()` sera appelée (par exemple, `reject()` a été appelée).
* **En attente :** pas encore remplie ou rejetée.

Prenons un exemple.

La promesse prend deux paramètres, resolve et reject. Lorsque quelque chose ne va pas, reject est appelée, sinon resolve est appelée.

```javascript
const movies = [
        { title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
        { title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }
    ]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

function createMovies(movie){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            movies.push(movie);

            const error = false;

            if(!error){
                resolve();
            }
            else{
                reject('Error: Something went wrong!')
            }
        }, 2000);
    })
}

createMovies({ title: `Return of the Jedi`, body:`Luke Skywalker attempts to bring his father back to the light side of the Force. At the same time, the rebels hatch a plan to destroy the second Death Star.`})
.then(getMovies);
```

Si nous obtenons une erreur, ce sera quelque chose comme « Error: Something went wrong! », et si ce n'est pas le cas, la promesse sera résolue.

Une fois la promesse résolue, elle appelle le mot-clé `.then()` et `getMovies()`.

## Enfin, comment fonctionne Async/Await en JavaScript ?

Async signifie asynchrone. Il permet à un programme d'exécuter une fonction sans geler l'ensemble du programme. Cela est fait en utilisant les mots-clés Async/Await.

Async/Await facilite l'écriture des promesses. Le mot-clé 'async' avant une fonction fait que la fonction retourne une promesse, toujours. Et le mot-clé await est utilisé à l'intérieur des fonctions async, ce qui fait attendre le programme jusqu'à ce que la promesse soit résolue.

```javascript
async function example() {

  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("done!"), 2000)
  });

  let result = await promise; // attend jusqu'à ce que la promesse soit résolue (*)

  alert(result); // "done!"
}

example();
```

L'exécution de la fonction « pause » à la ligne (*) et reprend lorsque la promesse est remplie, avec `result` devenant son résultat. Ainsi, le code ci-dessus affiche « done! » en deux secondes.

Prenons un exemple pratique.

```javascript
const movies = [
        { title: `A New Hope`, body:`After Princess Leia, the leader of the Rebel Alliance, is held hostage by Darth Vader, Luke and Han Solo must free her and destroy the powerful weapon created by the Galactic Empire.`},
        { title: `The Empire Strikes Back`, body: `Darth Vader is adamant about turning Luke Skywalker to the dark side. Master Yoda trains Luke to become a Jedi Knight while his friends try to fend off the Imperial fleet.` }
    ]

function getMovies(){
    setTimeout(() => {
        movies.forEach((movie, index) => {
            console.log(movie.title)
        })
    }, 1000);
}

function createMovies(movie){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            movies.push(movie);

            const error = false;

            if(!error){
                resolve();
            }
            else{
                reject('Error: Something went wrong!')
            }
        }, 2000);
    })
}

async function init(){
    await createMovies({ title: `Return of the Jedi`, body:`Luke Skywalker attempts to bring his father back to the light side of the Force. At the same time, the rebels hatch a plan to destroy the second Death Star.`});
    
    getMovies(); (*)
}

init();
```

Dans l'exemple ci-dessus, `getMovies()` à la ligne (*) attend que `createMovies()` soit exécuté dans la fonction async.

En d'autres termes, `createMovies()` est asynchrone, donc `getMovies()` ne s'exécutera qu'après que `createMovies()` soit terminé.

Maintenant, vous connaissez toutes les bases des boucles d'événements, des fonctions de rappel, des promesses et d'Async/Await. Ces fonctionnalités ont été introduites dans ECMAScript 2017, et elles ont rendu la lecture et l'écriture de code JS beaucoup plus faciles et plus efficaces.

> _C'est tout pour aujourd'hui ! Bon apprentissage et bonnes expériences,_