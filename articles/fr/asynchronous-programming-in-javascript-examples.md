---
title: Programmation asynchrone en JavaScript – Callbacks, Promesses & Exemples Async/Await
subtitle: ''
author: Musab Habeeb
co_authors: []
series: null
date: '2024-02-02T16:04:52.000Z'
originalURL: https://freecodecamp.org/news/asynchronous-programming-in-javascript-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Await-2.png
tags:
- name: async/await
  slug: asyncawait
- name: asynchronous programming
  slug: asynchronous-programming
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: Programmation asynchrone en JavaScript – Callbacks, Promesses & Exemples
  Async/Await
seo_desc: 'All programming languages have runtime engines that execute their code.
  In JavaScript, the runtime engine is single-threaded, which means that it runs code
  line by line or sequentially.

  The JavaScript runtime engine makes it a synchronous programming...'
---

Tous les langages de programmation disposent de moteurs d'exécution qui exécutent leur code. En JavaScript, le moteur d'exécution est monothread, ce qui signifie qu'il exécute le code ligne par ligne ou séquentiellement.

Le moteur d'exécution JavaScript en fait un langage de programmation synchrone où les programmes s'exécutent séquentiellement. Les langages de programmation qui ne sont pas synchrones sont appelés langages de programmation asynchrones, qui sont des langages de programmation où les programmes s'exécutent concurrentiel.

Bien que JavaScript soit synchrone, vous pouvez effectuer de la programmation asynchrone avec lui. Dans cet article, vous apprendrez la programmation asynchrone en JavaScript et comment l'utiliser.

## Qu'est-ce que la programmation asynchrone ?

La programmation asynchrone est une technique qui permet à votre programme d'exécuter ses tâches concurrentiel. Vous pouvez comparer la programmation asynchrone à un chef avec plusieurs cuisinières, casseroles et ustensiles de cuisine. Ce chef pourra cuisiner divers plats à la fois.

La programmation asynchrone rend vos programmes JavaScript plus rapides, et vous pouvez effectuer de la programmation asynchrone avec l'une de ces méthodes :

* Callbacks

* Promesses

* Async/Await

Dans les sections à venir, vous apprendrez ces techniques et comment les utiliser.

## Callbacks

Un callback est une fonction utilisée comme argument dans une autre fonction. Les callbacks vous permettent de créer des programmes asynchrones en JavaScript en passant le résultat d'une fonction dans une autre fonction.

```javascript
function greet(name) {
    console.log(`Hi ${name}, how do you do?`);
}

function displayGreeting(callback) {
    let name = prompt("Please enter your name");
    callback(name);
};

displayGreeting(greet);
```

Dans le code ci-dessus, la fonction `greet` est utilisée pour logger un message de salutation dans la console, et elle a besoin du nom de la personne à saluer.

La fonction `displayGreeting` obtient le nom de la personne et a un callback qui passe le nom comme argument à la fonction `greet` tout en l'appelant. Ensuite, la fonction `displayGreeting` est appelée avec la fonction greet passée en argument.

### L'enfer des callbacks

Bien que les callbacks facilitent le contrôle et rendent votre programme asynchrone, vous finirez par rencontrer un problème appelé l'enfer des callbacks en les utilisant.

Ce problème survient lorsque vous effectuez plusieurs tâches asynchrones avec des callbacks, ce qui peut entraîner l'imbrication de callbacks dans des callbacks.

Voici un exemple :

```javascript
function greet(callback) {
    setTimeout(function() {
        console.log("Hi Musab");
        callback();
    }, 1000);
}

function introduce(callback) {
    setTimeout(function() {
        console.log("I am your academic advisor");
        callback();
    }, 1000);
}

function question(callback) {
    setTimeout(function() {
        console.log("Are you currently facing any challenge in your academics");;
        callback();
    }, 1000);
}

// enfer des callbacks
greet(function() {
    introduce(function() {
        question(function() {
            console.log("Done");
        });
    });
});
```

Dans le code ci-dessus, les fonctions `greet`, `introduce` et `question` sont imbriquées pour créer un enfer des callbacks, ce qui rend la gestion des erreurs difficile. Vous devriez changer votre technique de programmation asynchrone des callbacks à `Promise` pour éviter l'enfer des callbacks.

## Promesse

La plupart des programmes consistent en un code producteur qui effectue une tâche chronophage et un code consommateur qui a besoin du résultat du code producteur.

Une `Promise` relie le code producteur et le code consommateur ensemble. Dans l'exemple ci-dessous, la fonction `displayGreeting` est le code producteur tandis que la fonction `greet` est le code consommateur.

```javascript
let name;

// code producteur
function displayGreeting(callback) {
    name = prompt("Please enter your name");
}

// code consommateur
function greet(name) {
    console.log(`Hi ${name}, how do you do?`);
}
```

Dans l'exemple ci-dessous, la syntaxe `new Promise` crée une nouvelle `Promise`, qui prend une fonction qui exécute le code producteur. La fonction résout ou rejette sa tâche et attribue la `Promise` à une variable nommée `promise`.

Si le code producteur se résout, son résultat sera passé au code consommateur via le gestionnaire `.then`.

```javascript
let name;

function displayGreeting() {
    name = prompt("Please enter your name");
}

let promise = new Promise(function(resolve, reject) {
    // le code producteur
    displayGreeting();
    resolve(name)
});

function greet(result) {
    console.log(`Hi ${result}, how do you do?`);
}

promise.then(
    // le code consommateur
    result => greet(result),
    error => alert(error)
);
```

Vous pouvez convertir l'exemple précédent de l'enfer des callbacks en une promesse en retournant une promesse de chaque fonction et en enchaînant les appels de fonction ensemble avec le gestionnaire `.then`.

Vous pouvez également utiliser le gestionnaire `.catch` pour attraper toute erreur lancée pendant l'exécution de la fonction.

```javascript
function greet() {
    return new Promise(resolve => {
        setTimeout(function() {
            console.log("Hi Musab");
            resolve();
        }, 1000);
    });  
}

function introduce() {
    return new Promise(resolve => {
        setTimeout(function() {
            console.log("I am your academic advisor");
            resolve();
        }, 1000);
    });
}

function question() {
    return new Promise(resolve => {
        setTimeout(function() {
            console.log("Are you currently facing any challenge in your academics");;
            resolve();
        }, 1000);
    });
}

greet()
    .then(() => introduce())
    .then(() => question())
    .then(() => console.log("Done"))
    .catch(error => console.error("An error occured: ", error));
```

### Quels sont les états d'une promesse en JavaScript ?

Une promesse peut être dans l'un de ces trois états :

* En attente : C'est l'état initial de la promesse et son état tant qu'elle est encore en cours d'exécution.

* Remplie : C'est l'état de la promesse lorsqu'elle se résout avec succès.

* Rejetée : C'est l'état de la promesse lorsque des erreurs l'empêchent d'être résolue.

## Async/Await

`async`/`await` est un sucre syntaxique pour créer une `Promise` — il facilite la création de promesses.

Pour rendre une fonction asynchrone en utilisant `async`/`await`, vous devez écrire le mot-clé `async` avant la déclaration de la fonction. Ensuite, vous pouvez écrire le mot-clé `await` avant l'appel d'exécution du code producteur.

Voici un exemple :

```javascript
let name;

function displayGreeting() {
    name = prompt("Please enter your name");
    return name;
}

function greet(result) {
    console.log(`Hi ${result}, how do you do?`);
}

async function greeting() {
    // le code producteur
    let result = await displayGreeting();
    // le code consommateur
    greet(result);
};

greeting();
```

Dans l'exemple ci-dessus, le code producteur est la fonction `displayGreeting`, et le code consommateur est la fonction `greet`. La fonction `greeting` est la `Promise` qui connecte le code producteur et le code consommateur. Elle attend le résultat retourné par la fonction `displayGreeting` et passe ce résultat à la fonction greet.

### Gestion des erreurs dans Async/Await

Vous pouvez facilement gérer les erreurs qui surviennent lorsque vous effectuez des opérations asynchrones avec `async`/`await` en utilisant l'instruction `try...catch`. L'opération asynchrone s'exécute dans le bloc `try`, et vous pouvez gérer les erreurs dans le bloc `catch`.

C'est-à-dire :

```javascript
async function greeting() {
    try {
        let result = await displayGreeting();
        greet(result);
    } catch(err) {
        console.error(err)
    }
};
```

## Conclusion

La programmation asynchrone en JavaScript est utilisée pour faire en sorte que les tâches d'un programme s'exécutent concurrentiel et utilise des techniques telles que les callbacks, `Promise` ou `async`/`await`.

Cet article explique comment utiliser ces techniques de programmation asynchrone et comment gérer les erreurs avec elles.

Vous pouvez consulter la [section sur les promesses et async/await du site JavaScript.info](https://javascript.info/async) pour en apprendre davantage sur la programmation asynchrone en JavaScript.