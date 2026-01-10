---
title: Comment utiliser Async/Await en JavaScript – Expliqué avec des exemples de
  code
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-12-15T15:33:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-async-await
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/js-async-await.png
tags:
- name: async/await
  slug: asyncawait
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser Async/Await en JavaScript – Expliqué avec des exemples
  de code
seo_desc: 'Hello friends! In this article, I''m going to show you how to use the “async/await”
  special syntax when handling JavaScript Promises.

  If you don''t know or need a refresher on JavaScript promises, you can read my previous
  article: How JavaScript Promis...'
---

Bonjour les amis ! Dans cet article, je vais vous montrer comment utiliser la syntaxe spéciale « async/await » lors de la gestion des promesses JavaScript.

Si vous ne connaissez pas ou avez besoin d'un rappel sur les promesses JavaScript, vous pouvez lire mon article précédent : [Comment fonctionnent les promesses JavaScript – Tutoriel pour débutants](https://www.freecodecamp.org/news/javascript-promise-object-explained/).

Vous devrez bien comprendre les promesses JavaScript avant d'apprendre la syntaxe async/await.

## Comment fonctionne async/await

La syntaxe async/await est une syntaxe spéciale créée pour vous aider à travailler avec les objets de promesse. Elle rend votre code plus propre et plus clair.

Lors de la gestion d'une `Promise`, vous devez enchaîner l'appel à la fonction ou à la variable qui retourne une `Promise` en utilisant les méthodes `then/catch`.

Lorsque vous avez plusieurs promesses, vous aurez également besoin de nombreuses chaînes de méthodes `then`. Par exemple, voici comment vous pourriez récupérer des données en utilisant la fonction `fetch()` :

```js
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => console.log(json))
  .catch(error => console.log(error));
```

Dans le code ci-dessus, la fonction `fetch()` retourne une `Promise`, que nous gérons en utilisant la méthode `then()`. À l'intérieur de la première méthode `then()`, nous acceptons la `response` de la requête et la convertissons en un objet en utilisant la méthode `json()`.

Dans la deuxième méthode `then()`, nous recevons les données `json` retournées par l'appel à la méthode `json()`, puis nous enregistrons ces données dans la console.

Nous ajoutons également la méthode `catch()` pour gérer toute erreur qui pourrait survenir lors de l'exécution de la requête.

Le code n'est vraiment pas difficile à comprendre, mais nous pouvons le rendre encore plus joli en supprimant les chaînes `.then()` et `.catch()`, ce qui supprime également les fonctions de rappel.

### Le mot-clé Await

Le mot-clé `await` fait essentiellement attendre JavaScript jusqu'à ce que l'objet `Promise` soit résolu ou rejeté. Au lieu d'avoir à utiliser le modèle de rappel à l'intérieur de la méthode `then()`, vous pouvez assigner la promesse remplie à une variable comme ceci :

```js
const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
const json = await response.json();
console.log(json)

```

Le mot-clé `await` est placé avant l'appel à une fonction ou à une variable qui retourne une promesse. Il fait attendre JavaScript que l'objet de promesse soit réglé avant d'exécuter le code à la ligne suivante.

Maintenant, si vous exécutez le code ci-dessus, vous pourriez obtenir une erreur comme celle-ci :

```txt
SyntaxError: await is only valid in async functions and the top level bodies of modules

```

Cette erreur se produit parce que le mot-clé `await` doit être utilisé à l'intérieur d'une fonction asynchrone ou d'un module.

### Le mot-clé Async

Pour créer une fonction asynchrone, vous devez ajouter le mot-clé `async` avant le nom de votre fonction. Regardez la ligne 1 dans l'exemple ci-dessous :

```js
async function runProcess() {
  const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  const json = await response.json();
  console.log(json)
}

runProcess();

```

Ici, nous avons créé une fonction asynchrone appelée `runProcess()` et nous y avons placé le code qui utilise le mot-clé `await`. Nous pouvons ensuite exécuter la fonction asynchrone en l'appelant, comme une fonction régulière.

## Comment gérer les erreurs dans Async/Await

Pour gérer une erreur qui pourrait survenir avec la syntaxe async/await, vous pouvez utiliser le bloc try/catch pour attraper tout rejet de votre promesse.

Voir l'exemple ci-dessous :

```js
async function runProcess() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
}

runProcess();

```

Le bloc try/catch, placé à l'intérieur de la fonction `runProcess()`, gérera le rejet qui provient des objets de promesse.

Maintenant, nous avons une version complète async/await du code standard de Promise que nous avons créé précédemment. Voici une comparaison entre les deux :

![Image](https://www.freecodecamp.org/news/content/images/2023/12/PROMISE---ASYNC.png)
_Comparaison du code Promise vs Async/Await_

Dans la version async/await, le résultat de la promesse est directement assigné à une variable. Dans la version standard de la promesse, le résultat de la promesse est passé en tant qu'argument à la méthode `.then()`.

La plupart des développeurs préfèrent la version async/await car elle semble plus directe.

## Comment utiliser Async/Await dans les fonctions IIFE et fléchées

Une expression de fonction invoquée immédiatement (IIFE) est une technique utilisée pour exécuter une fonction immédiatement dès que vous la définissez.

Contrairement aux fonctions et variables régulières, les IIFE seront supprimées du processus en cours une fois qu'elles sont exécutées.

Outre la fonction standard, vous pouvez également créer une IIFE asynchrone. Cela est utile lorsque vous devez exécuter la fonction asynchrone une seule fois :

```js
(async function () {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
})();

```

Vous pouvez également utiliser la syntaxe fléchée lors de la création d'une fonction asynchrone comme suit :

```js
const runProcess = async () => {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
};

runProcess();

```

N'hésitez pas à utiliser la syntaxe que vous souhaitez dans votre code.

## Pourquoi utiliser la syntaxe async/await ?

La syntaxe async/await vous permet de gérer les promesses sans utiliser l'enchaînement des méthodes `.then()` et `.catch()`, ce qui supprime également le besoin de rappels imbriqués.

Cet avantage est significatif lorsque vous avez un processus complexe après que la promesse soit réglée.

Revenons à notre exemple précédent, supposons que vous avez une instruction conditionnelle à l'intérieur de la méthode `.then()` comme suit :

```js
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => {
    if (json.userId == 1) {
      json.completed == false;
    } else {
      json.completed == true;
    }
  })
  .catch(error => console.log(error));
```

Ici, vous pouvez voir que la fonction de rappel qui accepte les données `json` a un bloc if/else à l'intérieur.

Ce code est difficile à comprendre et à modifier par rapport à la version async/await comme suit :

```js
(async function () {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
    const json = await response.json();
    if (json.userId == 1) {
      json.completed == false;
    } else {
      json.completed == true;
    }
    console.log(json);
  } catch (error) {
    console.log(error);
  }
})();
```

En utilisant la syntaxe async/await, vous réduisez le besoin d'enchaînement de méthodes et de rappels imbriqués. Cela impacte la lisibilité de votre code, surtout lorsque vous avez du code imbriqué comme des blocs if/else et des boucles for.

## Conclusion

Maintenant, vous avez appris comment fonctionne la syntaxe async/await. La syntaxe facilite grandement le travail avec les promesses en supprimant le besoin d'enchaînement des méthodes `.then()` et `.catch()`, ce qui supprime également le besoin de rappels imbriqués.

Même si le mot-clé `await` ne peut être utilisé qu'à l'intérieur d'une fonction `async`, vous pouvez utiliser une IIFE pour invoquer la fonction asynchrone une seule fois.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !