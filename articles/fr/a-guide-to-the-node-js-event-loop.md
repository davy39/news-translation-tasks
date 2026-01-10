---
title: Un guide sur la boucle d'événements de Node.js
subtitle: ''
author: Musab Habeeb
co_authors: []
series: null
date: '2024-05-28T07:00:35.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-the-node-js-event-loop
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Node.js-event-loop.jpg
tags:
- name: node js
  slug: node-js
seo_title: Un guide sur la boucle d'événements de Node.js
seo_desc: 'Node.js is an open-source JavaScript runtime environment that allows you
  to run JavaScript outside the browser. Although Node.js is single-threaded, it has
  an event loop that makes it multi-threaded.

  The Node.js event loop is a crucial mechanism in N...'
---

Node.js est un environnement d'exécution JavaScript open-source qui permet d'exécuter JavaScript en dehors du navigateur. Bien que Node.js soit mono-thread, il possède une boucle d'événements qui le rend multi-thread.

La boucle d'événements de Node.js est un mécanisme crucial dans Node.js qui permet aux programmes Node.js de s'exécuter de manière concurrente et asynchrone. Maîtriser la boucle d'événements de Node.js aide un développeur Node.js à comprendre comment les programmes Node.js s'exécutent sous le capot.

Dans cet article, vous apprendrez les bases de la boucle d'événements, en commençant par les threads et les processus, puis comment fonctionne la boucle d'événements JavaScript, et enfin, comment fonctionne la boucle d'événements Node.js.

## Qu'est-ce que les Threads et les Processus ?

Pour maîtriser la boucle d'événements de Node.js, vous devez comprendre les processus et les threads.

Un programmeur peut écrire des programmes qui effectuent différentes tâches avec différents langages de programmation. Alors que certains langages de programmation ne peuvent exécuter qu'une seule tâche à la fois, d'autres langages de programmation peuvent exécuter plusieurs tâches simultanément.

Un processus implique plusieurs tâches qui s'exécutent dans un programme du début à la fin, tandis qu'un thread est l'exécution d'une tâche individuelle.

Un processus se compose de toutes les étapes qu'un programme prend pour s'exécuter jusqu'à son achèvement. C'est un programme en cours d'exécution. Un programme peut avoir un ou plusieurs processus indépendants, chacun ayant son propre espace mémoire ou adresse. Un processus peut avoir un ou plusieurs threads.

Un thread est une unité d'exécution unique qui fait partie d'un processus, comme une tâche dans un programme. Un thread a un identifiant de thread, un ensemble de registres et une pile. Un thread partage également sa section de code, sa section de données, les ressources du système d'exploitation et l'espace mémoire avec d'autres threads dans un processus.

Le code ci-dessous contient une fonction `isNumberEven` qui vérifie si un nombre est pair et une fonction `isNumberOdd` qui vérifie si un nombre est impair. Un processus implique l'exécution de ce code du début à la fin, tandis qu'un thread implique l'exécution de fonctions individuelles.

```javascript
function isNumberEven(number) {
  if (number % 2 === 0) {
    return true;
  } else {
    return false;
  }
}

function isNumberOdd(number) {
  if (number % 2 !== 0) {
    return true;
  } else {
    return false;
  }
}

isNumberEven(6);
isNumberOdd(1);
```

### Qu'est-ce que les Single-threads et les Multi-threads ?

Tous les langages de programmation ont un moteur d'exécution qui exécute leur code. Certains moteurs d'exécution sont mono-thread (ce qui signifie qu'ils ne peuvent exécuter qu'un seul thread à la fois), tandis que d'autres sont multi-thread (ce qui signifie qu'ils peuvent exécuter plus d'un thread à la fois).

Le diagramme ci-dessous montre un processus mono-thread et un processus multi-thread :

![Single threads et Multi threads](https://hackmd.io/_uploads/SJkCXfQTa.jpg align="left")

*Processus Single-thread et Multi-thread*

Un langage de programmation mono-thread a un moteur d'exécution mono-thread qui exécute les tâches dans un programme de manière séquentielle. Un langage de programmation multi-thread a un moteur d'exécution multi-thread qui exécute les tâches dans un programme simultanément. Un moteur d'exécution multi-thread est plus performant qu'un moteur d'exécution mono-thread.

Les langages de programmation comme Java, C#, etc., sont multi-thread, tandis que les langages comme JavaScript, Python, etc., sont mono-thread.

Les langages de programmation mono-thread sont synchrones, ce qui signifie qu'ils exécutent les tâches dans leurs programmes de manière séquentielle. JavaScript est synchrone, mais sa boucle d'événements le rend asynchrone.

Dans les sections à venir, vous apprendrez comment fonctionne la boucle d'événements JavaScript, puis vous maîtriserez la boucle d'événements Node.js.

## Comment fonctionne la boucle d'événements JavaScript

Vous devez comprendre comment le moteur d'exécution JavaScript exécute le code JavaScript pour comprendre la boucle d'événements JavaScript.

Le moteur d'exécution JavaScript se compose principalement de :

* Tas de mémoire et

* Pile d'appels

Le tas de mémoire est l'endroit où les variables déclarées dans le programme se voient allouer un espace mémoire, et la pile d'appels est l'endroit où le moteur d'exécution stocke les fonctions dans le programme pour exécution.

Le moteur d'exécution JavaScript exécute le code ci-dessous de manière synchrone et dans ce processus étape par étape :

* Il alloue un espace mémoire pour toutes les variables dans le code.

* Il exécute la fonction `exponentiation` après l'avoir poussée sur la pile d'appels.

* Il exécute la fonction `validatePassword` après l'avoir poussée sur la pile d'appels.

```javascript
function exponentiation(base, exponent) {
  let result = 1;
  for (let i = 0; i < exponent; i++) {
    result *= base;
  }
  return result;
}

function validatePassword(password) {
  const hasUppercase = /[A-Z]/.test(password);
  const hasLowercase = /[a-z]/.test(password);
  const hasNumber = /[0-9]/.test(password);
  const isValidLength = password.length >= 8;

  if (hasUppercase && hasLowercase && hasNumber && isValidLength) {
    return "password is valid";
  } else {
    return "password is invalid";
  }
}

exponentiation(5, 3);
validatePassword("Ab01234");
```

Si votre code contient une fonction bloquante, qui est une fonction qui prend beaucoup de temps à s'exécuter, la fonction bloquera les autres fonctions jusqu'à ce qu'elle se termine. Les utilisateurs ne peuvent pas interagir avec un site web qui a une fonction bloquante dans son code pendant que la fonction s'exécute.

Le code ci-dessous contient la fonction `fibonacci`, qui prend du temps à s'exécuter. Le moteur d'exécution commence par exécuter la fonction `factorial`, puis la fonction `fibonacci`, pendant laquelle la fonction `findMin` ne peut pas s'exécuter.

```javascript
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

function fibonacci(num) {
  if (num <= 1) {
    return num;
  }
  return fibonacci(num - 1) + fibonacci(num - 2);
}

function findMin(numbers) {
  if (!numbers || numbers.length === 0) {
    throw new Error("Empty array provided");
  }

  let min = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < min) {
      min = numbers[i];
    }
  }
  return min;
}

let numbers = [4, 2, 8, 1, 6];

factorial(5);

fibonacci(45);

findMin(numbers);
```

Pour faire en sorte que le programme de l'exemple ci-dessus s'exécute de manière asynchrone, vous devriez rendre la fonction `fibonacci` non bloquante avec les API web JavaScript.

Les API web JavaScript ne s'exécutent pas sur le thread principal mais créent plutôt leurs propres threads, ce qui leur permet de s'exécuter de manière concurrente et de ne pas bloquer l'exécution d'autres fonctions dans votre code.

Vous pouvez utiliser ces API web JavaScript pour rendre vos fonctions non bloquantes :

* [setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)

* [AJAX](https://developer.mozilla.org/en-US/docs/Glossary/AJAX) et

* [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

Donc, si vous ajoutez un `setTimeout` à votre code comme ceci :

```javascript
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

function fibonacci(num) {
  if (num <= 1) {
    return num;
  }
  return fibonacci(num - 1) + fibonacci(num - 2);
}

function findMin(numbers) {
  if (!numbers || numbers.length === 0) {
    throw new Error("Empty array provided");
  }

  let min = numbers[0];
  for (let i = 1; i < numbers.length; i++) {
    if (numbers[i] < min) {
      min = numbers[i];
    }
  }
  return min;
}

let numbers = [4, 2, 8, 1, 6];

factorial(5);

setTimeout(fibonacci(45), 3000);

findMin(numbers);
```

Les fonctions `factorial` et `findMin` s'exécuteront sur le thread principal, tandis que la fonction `fibonacci` s'exécute de manière concurrente sur un thread séparé.

Pour bien comprendre comment le programme ci-dessus s'exécute, vous devez comprendre comment fonctionne la boucle d'événements JavaScript. La boucle d'événements JavaScript est un mécanisme par lequel les tâches dans un programme JavaScript s'exécutent de manière asynchrone.

La boucle d'événements JavaScript a une file d'attente de rappels qui stocke les fonctions qui prennent du temps à s'exécuter.

La boucle d'événements envoie les fonctions qui s'exécutent immédiatement à la file d'attente de rappels pour exécution et envoie les fonctions bloquantes aux threads de l'API web pour exécution.

Ensuite, la boucle d'événements renvoie la fonction bloquante à la file d'attente de rappels lorsque le temps défini s'écoule. La boucle d'événements vérifie ensuite si la pile d'appels est vide avant de pousser la fonction dans la file d'attente de rappels vers la pile d'appels pour exécution.

Le diagramme ci-dessous explique comment fonctionne la boucle d'événements en JavaScript :

![Boucle d'événements JavaScript](https://hackmd.io/_uploads/B1AMVMQpa.jpg align="left")

*La boucle d'événements JavaScript*

Le code ci-dessus qui contient les fonctions `factorial`, `fibonacci` et `findMin` est exécuté comme ceci après avoir ajouté une fonction `setTimeout`.

La boucle d'événements pousse la fonction `factorial` sur la pile d'appels pour exécution. Ensuite, la boucle d'événements pousse la fonction `fibonacci` sur la pile d'appels, mais la fonction `fibonacci` a une fonction `setTimeout` qui l'empêche de s'exécuter immédiatement. Donc, la boucle d'événements pousse la fonction `fibonacci` vers un thread séparé pour que les API web s'exécutent de manière concurrente.

Ensuite, la boucle d'événements pousse la fonction `findMin` sur la pile d'appels pour exécution. Lorsque le temps défini dans le `setTimeout` s'écoule, la boucle d'événements pousse la fonction `fibonacci` sur la pile d'appels pour exécution.

## Comment fonctionne la boucle d'événements Node.js

Node.js est un environnement d'exécution JavaScript qui permet à JavaScript de s'exécuter en dehors du navigateur, comme sur l'interface de ligne de commande, les serveurs et le matériel.

Node.js a une boucle d'événements qui est similaire à la boucle d'événements JavaScript. La boucle d'événements Node.js et la boucle d'événements JavaScript ont une pile d'appels et une file d'attente de rappels. La boucle d'événements Node.js est implémentée et gérée par une bibliothèque nommée [libuv](https://libuv.org/) écrite en C.

La boucle d'événements Node.js a six phases, qui sont :

* Phase de temporisation

* Phase de rappels en attente

* Phase inactive

* Phase de sondage

* Phase de vérification

* Phase de rappels de fermeture

Le diagramme ci-dessous montre comment fonctionne la boucle d'événements Node.js :

![Boucle d'événements Node.js](https://hackmd.io/_uploads/SkiVEMXTp.jpg align="left")

*La boucle d'événements Node.js*

Il existe une file d'attente de micro-tâches qui existe en dehors de la boucle d'événements Node.js. La file d'attente de micro-tâches se compose de la `file d'attente nextTick` et de la `file d'attente Promise`. La `file d'attente nextTick` exécute la fonction `process.nextTick`, tandis que la `file d'attente Promise` exécute `.then`, `.catch` et autres promesses.

Dans les sections à venir, vous apprendrez chaque phase de la boucle d'événements Node.js.

### Phase de temporisation

Il y a trois temporisateurs dans Node.js : `setTimeout`, `setInterval` et `setImmediate`. `setTimeout` et `setInterval` s'exécutent dans la phase de temporisation. L'exemple de code ci-dessous s'exécute pendant la phase de temporisation :

```javascript
setTimeout(() => {
  console.log("Rappel setTimeout exécuté");
}, 1000);

setInterval(() => {
  console.log("Rappel setInterval exécuté");
}, 2000);
```

### Phase de rappels en attente

Les opérations d'E/S s'exécutent dans la phase de sondage de la boucle d'événements. Pendant la phase de sondage, certains rappels de opérations d'E/S spécifiques sont reportés à la phase en attente de l'itération suivante de la boucle d'événements. Les rappels de opérations d'E/S reportés de l'itération précédente s'exécutent dans la phase de rappels en attente.

L'exemple de code ci-dessous s'exécute pendant la phase de "rappels en attente" :

```javascript
const fs = require("fs");

fs.readFile(__filename, (err, data) => {
  if (err) throw err;
  console.log("Données du fichier :", data);
});
```

### Phase inactive

La phase inactive n'est pas une phase normale de la boucle d'événements Node.js. C'est une période pendant laquelle la boucle d'événements n'a rien à faire mais effectue des tâches en arrière-plan comme la vérification des résultats de faible priorité ou l'exécution du garbage collection.

Pour ignorer la phase inactive et ne pas effectuer de tâches en arrière-plan, vous pouvez appeler la méthode `idle.ignore()` du package [idle-gc](https://www.npmjs.com/package/idle-gc) dans votre code.

```javascript
const { idle } = require("idle-gc");

idle.ignore();
```

La méthode `idle.ignore()` garantit que le code continue de s'exécuter sans période inactive jusqu'à son achèvement. Cependant, en raison des problèmes de performance qu'elle cause, la méthode `idle.ignore()` doit être utilisée avec parcimonie.

### Phase de sondage

La phase de sondage est l'endroit où les opérations d'E/S s'exécutent. Les opérations d'E/S transfèrent des données vers ou depuis un ordinateur. La boucle d'événements vérifie les nouvelles opérations d'E/S et les exécute dans la file d'attente de sondage.

L'exemple de code ci-dessous s'exécute pendant la phase de sondage :

```javascript
const http = require("http");

http.get("http://jsonplaceholder.typicode.com/posts/1", (res) => {
  console.log("Réponse de la requête HTTP reçue");
  res.on("data", (chunk) => {
    // Faire quelque chose avec les données
  });
});
```

### Phase de vérification

La phase de vérification est l'endroit où le temporisateur `setImmediate` s'exécute. La boucle d'événements Node.js passe à la phase de vérification lorsqu'il y a un `setImmediate` dans le programme, et que la phase de sondage devient inactive ou lorsque la phase de sondage se termine.

L'exemple de code ci-dessous s'exécute pendant la phase de vérification :

```javascript
setImmediate(() => {
  console.log("Rappel setImmediate exécuté");
});
```

### Phase de rappels de fermeture

La phase de rappels de fermeture est la dernière phase de la boucle d'événements Node.js. La phase de rappels de fermeture est l'endroit où les rappels de l'événement de fermeture d'une socket et de la fermeture d'un serveur `HTTP` s'exécutent.

L'exemple de code ci-dessous s'exécute pendant la phase de vérification :

```javascript
const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello World\n');
});

server.listen(3000, () => {
  console.log('Serveur à l'écoute sur le port 3000');
  server.close(() => {
    console.log('Serveur fermé');
  });
});
```

## Conclusion

La boucle d'événements Node.js est le mécanisme qui permet la programmation asynchrone dans Node.js.

En tant que développeur Node.js, vous pouvez comprendre comment votre code Node.js s'exécute sous le capot si vous maîtrisez la boucle d'événements Node.js.

Cet article a expliqué les processus et les threads, la boucle d'événements JavaScript et la boucle d'événements Node.js.