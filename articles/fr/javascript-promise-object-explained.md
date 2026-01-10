---
title: Comment fonctionnent les Promesses JavaScript – Tutoriel pour débutants
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-11-29T15:55:31.000Z'
originalURL: https://freecodecamp.org/news/javascript-promise-object-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/js-promise.png
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: Comment fonctionnent les Promesses JavaScript – Tutoriel pour débutants
seo_desc: 'Hi everyone! In this article, I’m going to teach you one of the most confusing
  JavaScript topics, which is the Promise object. Promises may seem difficult at first,
  but they''re actually quite simple once you understand how they work.

  Here''s what we''l...'
---

Bonjour à tous ! Dans cet article, je vais vous enseigner l'un des sujets JavaScript les plus déroutants, à savoir l'objet Promise. Les promesses peuvent sembler difficiles au premier abord, mais elles sont en réalité assez simples une fois que vous comprenez comment elles fonctionnent.

Voici ce que nous allons couvrir :

1. [Comment fonctionne une Promesse](#heading-comment-fonctionne-une-promesse)
2. [Callbacks vs Promesses](#heading-callbacks-vs-promesses)
3. [Quand utiliser les Promesses au lieu des Callbacks](#heading-quand-utiliser-les-promesses-au-lieu-des-callbacks)
4. [Promesses et l'API Fetch](#heading-promesses-et-lapi-fetch)
5. [La méthode `Promise.all()`](#heading-la-methode-promiseall)
6. [La méthode `Promise.allSettled()`](#heading-la-methode-promiseallsettled)
7. [La méthode `Promise.any()`](#heading-la-methode-promiseany)
8. [La méthode `Promise.race()`](#heading-la-methode-promiserace)
9. [Conclusion](#heading-conclusion)

## Comment fonctionne une Promesse

En gros, un objet `Promise` représente un "état en attente" au sens le plus courant : la promesse sera finalement remplie à une date ultérieure.

Pour vous donner une illustration, supposons que vous souhaitez acheter un nouveau téléphone pour remplacer votre ancien téléphone, vous ouvrez donc une application de messagerie pour contacter un magasin de téléphones. Cela ressemble à la manière dont vous accédez à une variable ou à une fonction qui retourne une promesse :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/access-a-promise.png)
*Illustration 1 : Envoyer un message à un magasin est similaire à la manière dont vous accédez à un objet Promise en JavaScript*

Après avoir envoyé un message expliquant ce que vous voulez, vous recevez un message automatisé indiquant qu'un représentant répondra à votre message sous peu. Cela ressemble à la réception d'un objet Promise :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/promise-pending-state.png)
*Illustration 2 : Un message automatisé du magasin que vous avez contacté auparavant. C'est l'objet Promise que vous recevez en JavaScript*

Une minute plus tard, vous recevez un nouveau message d'un représentant humain, indiquant que le modèle de téléphone que vous souhaitez acheter est disponible à l'achat. C'est lorsque la Promise est résolue :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/promise-resolved.png)
*Illustration 3 : Un représentant du magasin a répondu à votre message. C'est comme lorsque une Promise est résolue*

Ou, dans un scénario complètement différent, le représentant vous dit que le magasin ne vend pas de téléphones, car le magasin est une épicerie et non un magasin de téléphones. Cela signifie que la Promise a été rejetée :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/promise-rejected.png)
*Illustration 4 : Le représentant a répondu que le magasin ne vend pas de téléphones. C'est comme lorsque une Promise est rejetée*

Cette illustration montre comment l'objet `Promise` en JavaScript fonctionne :

* Une Promise est comme le message automatisé que nous avons vu précédemment. Elle représente un état en attente qui doit être rempli à un moment ultérieur.
* Le représentant humain disant que le modèle de téléphone est disponible est similaire à la méthode `resolve()`, qui montre que la Promise est remplie.
* Le représentant vous disant que vous contactez le mauvais magasin est comme la méthode `reject()`, qui est la méthode utilisée pour montrer que la Promise ne peut pas être remplie en raison d'une erreur.

Une implémentation typique de promesse ressemble à ceci :

```js
let p = new Promise((resolve, reject) => {
  let isTrue = true;
  if (isTrue) {
    resolve('Promise résolue');
  } else {
    reject('Promise rejetée');
  }
});

```

Lors de la création d'un nouvel objet Promise, nous devons passer une fonction de rappel qui sera appelée immédiatement avec deux arguments : les fonctions `resolve()` et `reject()`.

Selon le résultat de la `Promise`, soit la fonction `resolve()`, soit la fonction `reject()` sera appelée pour mettre fin à l'état en attente.

Pour gérer l'objet `Promise`, vous devez enchaîner l'appel de fonction avec les fonctions `then()` et `catch()` comme montré ci-dessous :

```js
let p = new Promise((resolve, reject) => {
  let isTrue = true;
  if (isTrue) {
    resolve('Succès');
  } else {
    reject('Erreur');
  }
});

p
.then(message => console.log(`Promise résolue : ${message}`))
.catch(message => console.log(`Promise rejetée : ${message}`));

```

La fonction `resolve()` correspond à la fonction `then()`, tandis que `reject()` correspond à la fonction `catch()`. Vous pouvez changer la valeur `isTrue` en `false` pour tester cela.

Voici une illustration du processus de promesse :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/promise-object--1-.png)
*Le processus se déroulant à l'intérieur d'une Promise. Selon le code exécuté à l'intérieur de la Promise, elle se résoudra ou sera rejetée.*

En utilisant le modèle de promesse, vous pouvez appeler vos fonctions séquentiellement en plaçant le processus suivant à l'intérieur des méthodes `then()` ou `catch()`.

## Callbacks vs Promesses

Le modèle de promesse a été créé pour remplacer l'utilisation des callbacks dans certaines situations. En utilisant les promesses, le code que nous écrivons est plus intuitif et maintenable.

En revenant à l'illustration de messagerie, créons un exemple d'utilisation de callbacks pour gérer la situation.

Tout d'abord, nous déclarons les deux variables requises pour cette situation, appelées `isPhoneStore` et `isPhoneAvailable` :

```js
const isPhoneStore = true;
const isPhoneAvailable = true;

```

Ensuite, nous écrivons une fonction qui traitera les messages entrants. Cette fonction imitera le modèle de promesse, et elle se résoudra uniquement lorsque `isPhoneStore` et `isPhoneAvailable` seront `true` :

```js
function processMessage(resolveCallback, rejectCallback) {
  if (!isPhoneStore) {
    rejectCallback({
      name: 'Mauvais magasin',
      message: 'Désolé, ceci est une épicerie !',
    });
  } else if (!isPhoneAvailable) {
    rejectCallback({
      name: 'En rupture de stock',
      message: 'Désolé, le téléphone X est en rupture de stock !',
    });
  } else {
    resolveCallback({
      name: 'OK',
      message: 'Le téléphone X est disponible ! Combien souhaitez-vous en acheter ?',
    });
  }
}

```

Ici, vous pouvez voir que la fonction `processMessage` accepte deux fonctions de rappel : `resolveCallback` et `rejectCallback`.

Lorsque nous appelons la fonction, nous devons fournir les fonctions de rappel, de manière similaire à la façon dont nous devons enchaîner les méthodes `then()` et `catch()` lors de l'accès à une promesse :

```js
processMessage(
  value => console.log(value),
  reason => console.log(reason)
);

```

Dans l'appel à `processMessage` ci-dessus, le premier argument est la fonction `resolveCallback()`, et le second argument est la fonction `rejectCallback()`.

Si vous exécutez le code ci-dessus, alors la fonction `resolveCallback()` sera appelée. Vous pouvez changer l'une des deux variables en `false` pour déclencher la fonction `rejectCallback()`.

Maintenant que nous avons un exemple de callback fonctionnel, réécrivons le code en utilisant une promesse comme suit :

```js
const isPhoneStore = true;
const isPhoneAvailable = true;

function processMessage() {
  return new Promise((resolve, reject) => {
    if (!isPhoneStore) {
      reject({
        name: 'Mauvais magasin',
        message: 'Désolé, ceci est une épicerie !',
      });
    } else if (!isPhoneAvailable) {
      reject({
        name: 'En rupture de stock',
        message: 'Désolé, le téléphone X est en rupture de stock !',
      });
    } else {
      resolve({
        name: 'OK',
        message: 'Le téléphone X est disponible ! Combien souhaitez-vous en acheter ?',
      });
    }
  });
}

processMessage()
  .then(response => console.log(response))
  .catch(error => console.log(error));

```

Ici, vous pouvez voir que la fonction `processMessage()` retourne un objet `Promise` qui est résolu uniquement lorsque `isPhoneStore` et `isPhoneAvailable` sont `true`.

Lorsque l'une des deux variables est `false`, alors l'objet `Promise` sera rejeté.

Ici, vous pouvez voir que vous n'avez pas besoin d'ajouter deux paramètres supplémentaires à la fonction `processMessage()` juste pour les callbacks. De plus, lors de l'appel de la fonction, vous utilisez les méthodes `then()` et `catch()` pour gérer le résultat de la promesse.

L'utilisation d'une promesse rend le code plus facile à comprendre. Voici la comparaison des deux côte à côte :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/callback-vs-promise.png)
*Comparaison du code entre Callbacks et Promesses*

Je ne sais pas pour vous, mais je préfère certainement écrire et lire le modèle de promesse plutôt que le modèle de callback. 😉

### Quand utiliser les Promesses au lieu des Callbacks

Comme je l'ai mentionné précédemment, l'objet promesse a été créé pour remplacer les fonctions de rappel dans certaines situations.

Et si vous examinez attentivement le code de l'objet promesse ci-dessus, vous verrez que même les promesses utilisent des callbacks à l'intérieur des méthodes `then()` et `catch()`. Cela signifie que les Promesses n'éliminent pas le besoin de callbacks.

Les Promesses sont utilisées lorsque vous devez attendre qu'une certaine tâche se termine avant d'exécuter le processus suivant.

Par exemple, supposons que vous avez trois fonctions qui doivent s'exécuter séquentiellement de un à trois.

Chaque fonction s'exécute pendant quelques secondes. Nous simulons cela en utilisant la méthode `setTimeout()` :

```js
function stepOne(value){
  setTimeout(() => {
    console.log(value);
  }, 3000);
}

function stepTwo(value){
  setTimeout(() => {
    console.log(value);
  }, 2000);
}

function stepThree(value){
  setTimeout(() => {
    console.log(value);
  }, 1000);
}
```

En utilisant des callbacks, vous pouvez définir des paramètres sur les fonctions `stepOne()` et `stepTwo()`, puis appeler ces fonctions séquentiellement comme ceci :

```js
function stepOne(value, callback) {
  setTimeout(() => {
    console.log(value);
    callback();
  }, 3000);
}

function stepTwo(value, callback) {
  setTimeout(() => {
    console.log(value);
    callback();
  }, 2000);
}

function stepThree(value, callback) {
  setTimeout(() => {
    console.log(value);
    callback();
  }, 1000);
}

// Exécuter les fonctions séquentiellement avec des callbacks
stepOne(1, () => {
  stepTwo(2, () => {
    stepThree(3, () => {
      console.log("Toutes les étapes sont terminées.");
    });
  });
});
```

Les callbacks imbriqués où vous passez la fonction suivante à l'intérieur de la fonction précédente sont familièrement connus sous le nom de "callback hell". Ce modèle de code est difficile à lire et il est désordonné.

Avec les promesses, vous pouvez réécrire le code ci-dessus comme suit :

```js
function stepOne(value) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(value);
      resolve();
    }, 3000);
  });
}

function stepTwo(value) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(value);
      resolve();
    }, 2000);
  });
}

function stepThree(value) {
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(value);
      resolve();
    }, 1000);
  });
}

// Exécuter les fonctions séquentiellement avec des Promesses
stepOne(1)
  .then(() => stepTwo(2))
  .then(() => stepThree(3))
  .then(() => {
    console.log("Toutes les étapes sont terminées.");
  });
```

Ici, vous pouvez voir que chaque fonction retourne une promesse qui se résout lorsque le délai d'attente est terminé. Les appels de fonction utilisant les méthodes `then()` maintiennent un ordre clair des étapes.

Dans un projet réel où vous avez de nombreuses lignes de code à l'intérieur des fonctions de rappel, l'utilisation des Promesses offre un gain massif dans votre capacité à lire, étendre et maintenir le code.

Mais si vous exécutez du code qui n'a pas besoin d'attendre certains processus, alors vous pouvez utiliser des callbacks sans problème.

Par exemple, les méthodes de tableau comme `forEach()` utilisent des callbacks, donc il n'y a pas besoin de promesses ici :

```js
const myArray = [1, 2, 3, 4];

myArray.forEach(value => console.log(value + 5));

```

Une autre utilisation des promesses est lorsque vous utilisez l'API Fetch, qui est utilisée pour exécuter des requêtes réseau. Voyons comment cela fonctionne maintenant.

## Promesses et l'API Fetch

L'API Fetch retourne toujours un objet `Promise`, vous devez donc le gérer en utilisant les méthodes `then()` et `catch()` comme montré ci-dessous :

```js
fetch('<Votre URL API>')
  .then(response => console.log(response))
  .catch(error => console.log(error));

```

Si vous exécutez une fonction `fetch()` et attribuez le résultat à une variable, la variable contiendra un objet `Promise` :

```js
const response = fetch('<Votre URL API>');
console.log(response); // Promise {<pending>}

```

Comme vous pouvez le voir, l'objet `Promise` est attribué à la variable `response` dans un état en attente. Si vous attendez un moment et que vous enregistrez à nouveau l'objet, le résultat sera rempli :

```txt
Promise {<fulfilled>: Response}

```

L'API Fetch retournera un objet `Response` lorsque la promesse est remplie. C'est aussi pourquoi je nomme généralement le paramètre à l'intérieur de la méthode `then()` comme `response`. N'hésitez pas à nommer la réponse comme `message`, `value`, ou tout autre nom sur lequel votre équipe s'est mise d'accord.

Maintenant que vous avez appris comment fonctionne l'objet `Promise`, il est temps d'apprendre quelques méthodes supplémentaires liées à cet objet.

### La méthode `Promise.all()`

Plus que simplement remplacer le modèle de callback, JavaScript fournit également quelques méthodes que vous pouvez utiliser pour travailler avec des objets `Promise`. Par exemple, supposons que vous traitez trois promesses différentes dans votre projet comme ceci :

```js
const p1 = Promise.resolve('Succès');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Terminé');

```

Maintenant, supposons que vous avez besoin que les trois promesses se résolvent avant de passer à l'étape suivante. Sachant ce que nous savons sur les promesses, nous pouvons enchaîner les promesses en utilisant la méthode `then()` comme ceci :

```js
p1.then(message1 => {
  return p2.then(message2 => {
    return p3.then(message3 => {
      return [message1, message2, message3];
    });
  });
}).then(messages => {
  console.log(messages);
});

```

Dans cet exemple, chaque méthode `then()` retourne une autre promesse, créant des callbacks imbriqués. Lorsque la promesse `p3` est résolue, les messages sont retournés sous forme de tableau unique.

La dernière méthode `then()` enregistrerait alors le tableau `messages` retourné par les promesses. Cette approche fonctionne, mais c'est exactement le type de code que nous voulons éviter lorsque nous utilisons des promesses.

Au lieu d'utiliser des callbacks imbriqués, nous pouvons utiliser la méthode `Promise.all()` à la place. Voici l'exemple ci-dessous :

```js
const p1 = Promise.reject('Erreur de la Promesse Un');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Terminé');

Promise.all([p1, p2, p3])
  .then(messages => console.log(messages))
  .catch(error => console.log(error));

```

La méthode `Promise.all()` accepte un tableau de promesses, et lorsque toutes les promesses sont résolues, la méthode transmettra les `messages` retournés par les promesses sous forme de tableau et les transmettra à la méthode `then()`.

Si l'une des promesses est rejetée, alors la méthode retourne le premier rejet qu'elle rencontre et arrête tout processus ultérieur.

Cette méthode vous permet de travailler avec de nombreuses promesses sans avoir à créer des callbacks imbriqués. Vous devriez utiliser cette méthode lorsque vous avez besoin que toutes les promesses se résolvent.

### La méthode `Promise.allSettled()`

La méthode `Promise.allSettled()` est similaire à la méthode `Promise.all()`, mais au lieu de passer à `catch()` lorsqu'une des promesses est rejetée, la méthode stockera le résultat du rejet et continuera à traiter les autres promesses.

Lorsque toutes les promesses sont réglées, la méthode retournera un tableau d'objets contenant les détails de chaque promesse. Par exemple, supposons que vous exécutez le code suivant :

```js
const p1 = Promise.reject('Erreur de la Promesse Un');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Terminé');

Promise.allSettled([p1, p2, p3]).then(response => {
  console.log(response);
});

```

Alors le résultat serait :

```txt
[
  { status: 'rejected', reason: 'Erreur de la Promesse Un' },
  { status: 'fulfilled', value: 200 },
  { status: 'fulfilled', value: 'Terminé' }
]

```

Comme vous pouvez le voir, la variable `response` est un tableau d'objets montrant le statut et la valeur ou la raison de ce statut. Lorsque vous appelez cette méthode, vous n'avez pas besoin d'enchaîner la méthode `catch()`.

Vous devriez utiliser cette méthode lorsque vous avez toujours besoin de connaître le résultat de chaque promesse.

### La méthode `Promise.any()`

La méthode `Promise.any()` est similaire à la méthode `Promise.all()`, sauf qu'elle retourne uniquement une seule valeur de n'importe quelle promesse qui appelle la fonction `resolve()` en premier. Si vous essayez la méthode comme suit :

```js
const p1 = Promise.reject('Erreur de la Promesse Un');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Terminé');

Promise.any([p1, p2, p3]).then(response => {
  console.log(response);
});

```

La sortie sera :

```txt
200

```

C'est parce que la première promesse est rejetée, et une fois que la deuxième promesse est résolue, la méthode `any()` arrête toute exécution ultérieure des promesses et retourne la valeur résolue.

Cette méthode retourne une erreur uniquement lorsque toutes les promesses sont rejetées. Vous devriez utiliser cette méthode uniquement lorsque vous avez besoin d'obtenir une seule promesse résolue parmi de nombreuses promesses.

### La méthode `Promise.race()`

La méthode `Promise.race()` est comme la méthode `Promise.any()`, avec une différence : la promesse est réglée lorsque n'importe quelle promesse est résolue ou rejetée :

```js
const p1 = Promise.reject('Erreur de la Promesse Un');
const p2 = Promise.resolve(200);
const p3 = Promise.resolve('Terminé');

Promise.race([p1, p2, p3])
  .then(response => console.log(response))
  .catch(reason => console.log(reason));

```

Puisque `p1` retourne un rejet, alors la méthode `Promise.race()` retourne le rejet au lieu de continuer le processus :

```txt
Erreur de la Promesse Un

```

Vous devriez utiliser cette méthode uniquement lorsque vous avez besoin d'obtenir une seule promesse réglée, peu importe si le résultat est résolu ou rejeté.

Comme vous pouvez le voir, ces quatre méthodes de l'objet `Promise` vous fournissent un outil de composition puissant qui vous aide à décider comment gérer plusieurs promesses dans votre projet.

## Conclusion

Et maintenant vous avez appris comment fonctionne l'objet `Promise` en JavaScript. Une promesse est facile à comprendre lorsque vous saisissez les trois états qui peuvent être générés par la promesse : en attente, résolue et rejetée.

Vous avez également appris comment les promesses peuvent être utilisées pour remplacer les callbacks, quand utiliser les promesses au lieu des callbacks, et comment utiliser les méthodes de promesse lorsque vous devez gérer de nombreuses promesses dans votre projet.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine fois !