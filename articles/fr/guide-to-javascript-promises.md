---
title: Comment fonctionnent les Promesses en JavaScript – Un Guide Complet pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-13T16:35:33.000Z'
originalURL: https://freecodecamp.org/news/guide-to-javascript-promises
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/promises.png
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: Comment fonctionnent les Promesses en JavaScript – Un Guide Complet pour
  Débutants
seo_desc: "By Amazing Enyichi Agu\nJavaScript has the ability to carry out asynchronous\
  \ (or async) instructions. These instructions run in the background until they have\
  \ finished processing. \nAsynchronous instructions do not stop the JavaScript engine\
  \ from activ..."
---

Par Amazing Enyichi Agu

JavaScript a la capacité d'exécuter des instructions asynchrones (ou async). Ces instructions s'exécutent en arrière-plan jusqu'à ce qu'elles aient terminé leur traitement.

Les instructions asynchrones n'empêchent pas le moteur JavaScript d'accepter et de traiter activement d'autres instructions. C'est pourquoi JavaScript est non bloquant par nature.

Il existe quelques fonctionnalités asynchrones en JavaScript, et l'une d'elles est les **Promesses**. Pour travailler avec les promesses, vous devez adopter une syntaxe spéciale qui rend l'écriture des instructions async beaucoup plus organisée. Travailler avec les promesses est une compétence très utile que tout développeur JavaScript devrait apprendre.

Cet article est un guide approfondi sur les promesses en JavaScript. Vous allez apprendre pourquoi JavaScript a des promesses, ce qu'est une promesse, et comment travailler avec elle. Vous allez également apprendre comment utiliser async/await—une fonctionnalité dérivée des promesses—et ce qu'est une file d'attente de tâches.

Voici les sujets que nous allons couvrir :

1. [Pourquoi devriez-vous vous soucier des promesses ?](#heading-pourquoi-devriez-vous-vous-soucier-des-promesses)
2. [Qu'est-ce qu'une promesse ?](#heading-quest-ce-quune-promesse)
3. [Comment créer une promesse en JavaScript](#heading-comment-creer-une-promesse-en-javascript)
4. [Comment attacher un callback à une promesse](#heading-comment-attacher-un-callback-a-une-promesse)
5. [Comment gérer les erreurs dans une promesse](#heading-comment-gerer-les-erreurs-dans-une-promesse)
6. [Comment gérer plusieurs promesses à la fois](#heading-comment-gerer-plusieurs-promesses-a-la-fois)
7. [Qu'est-ce que la syntaxe async/await ?](#heading-quest-ce-que-la-syntaxe-asyncawait)
8. [Comment créer une fonction async en JavaScript](#heading-comment-creer-une-fonction-async-en-javascript)
9. [Comment utiliser le mot-clé await](#heading-comment-utiliser-le-mot-cle-await)
10. [Comment gérer les erreurs dans async/await](#heading-comment-gerer-les-erreurs-dans-asyncawait)
11. [Qu'est-ce qu'une file d'attente de tâches ?](#heading-quest-ce-quune-file-dattente-de-taches)

Ce guide _promet_ d'être une lecture intéressante et instructive. :) Il est destiné à toute personne cherchant à mieux écrire des instructions async en JavaScript, utilisant ainsi pleinement ce que le langage a à offrir. Avec tout cela, commençons.

## Prérequis

Pour suivre le matériel et le comprendre, voici quelques choses que vous devriez avoir :

* [Connaissance de base de JavaScript](https://www.freecodecamp.org/news/the-complete-javascript-handbook-f26b2c71719c/)
* [Connaissance de la manière dont JavaScript traite les opérations async](https://www.freecodecamp.org/news/javascript-asynchronous-operations-in-the-browser/)

Connaître ces sujets vous aidera à comprendre correctement ce que vous êtes sur le point d'apprendre. Si vous ne possédez pas les prérequis, vous pouvez aller les apprendre et revenir. L'article utilisera certains concepts de ces sujets ici.

## Pourquoi devriez-vous vous soucier des promesses ?

Les promesses n'ont pas toujours fait partie de JavaScript. Les callbacks fonctionnaient avec les fonctions asynchrones pour produire les résultats souhaités dans le passé. Un callback est toute fonction qui est un paramètre d'une fonction async, que la fonction async invoque pour compléter son opération.

Pour appeler une fonction async, vous deviez passer un callback comme argument comme ceci :

```js
function callback(result) {
  // Utiliser le résultat de l'opération Async
}

randomAsyncOperation((response) => callback(response));

```

Mais les callbacks avaient un énorme problème. Démontrer le problème facilite sa compréhension.

Supposons que vous aviez une fonction asynchrone qui récupérait des données quelque part sur Internet. Cette fonction devrait accepter deux callbacks, `successCallback` et `failureCallback`.

Le `successCallback` s'exécuterait si l'opération était réussie et que le programme trouvait la ressource appropriée. Mais le `failureCallback` s'exécuterait si l'opération échouait et ne pouvait pas trouver la ressource.

```js
function SuccessCallback(result) {
  console.log("Ressource trouvée", result);
}

function failureCallback(error) {
  console.error("Oups. Quelque chose s'est mal passé", error);
}

```

Pour exécuter la fonction async, vous deviez passer les deux fonctions de callback comme arguments :

```js
fetchResource(url, successCallback, failureCallback)
```

Ici, `url` est une variable qui représente l'emplacement de la ressource.

Ce code s'exécutera sans problème pour l'instant. Vous avez pris en compte les deux scénarios possibles dans lesquels la fonction pourrait se retrouver. Vous avez un callback pour une opération réussie et un callback pour une opération échouée.

Maintenant, supposons que vous souhaitez effectuer de nombreuses autres opérations de récupération, mais chaque opération doit être réussie pour que la suivante s'exécute. Cela est utile si les données dont vous avez besoin doivent arriver dans un certain ordre et ne peuvent pas être dispersées.

Par exemple, vous pourriez rencontrer cette situation si le résultat de l'opération suivante dépend du résultat de la précédente.

Dans ce cas, vos callbacks de succès auraient leurs propres callbacks de succès, ce qui est important car vous devez utiliser les résultats s'ils arrivent.

```js
fetchResource(
  url,
  function (result) {
    // Faire quelque chose avec le résultat
    fetchResource(
      newUrl,
      function (result) {
        // Faire quelque chose avec le nouveau résultat
        fetchResource(
          anotherUrl,
          function (result) {
            // Faire quelque chose avec le nouveau résultat
          },
          failureCallback
        );
      },
      failureCallback
    );
  },
  failureCallback
);
```

À partir de l'exemple, vous pouvez remarquer une complication qui se développe. Vous devriez continuer à imbriquer vos callbacks de succès tout en répétant le `failureCallback` chaque fois que vous appelez la fonction async.

Ces callbacks imbriqués ont conduit à la [Pyramide de l'Enfer des Callbacks](https://medium.com/dsc-srm/javascript-callback-hell-or-pyramid-of-doom-4f786d14b997) ou callback hell, qui peut rapidement devenir un cauchemar. Y aurait-il une manière plus efficace de gérer des situations comme celle-ci ?

JavaScript a introduit les Promesses dans le cadre de [ES6 (ES2015)](https://262.ecma-international.org/6.0/#sec-promise-constructor) pour résoudre ce problème. Cela a simplifié le travail avec les callbacks et a permis une meilleure syntaxe comme vous le verrez bientôt. Les promesses sont désormais la base de la plupart des opérations asynchrones modernes que les développeurs utilisent en JavaScript aujourd'hui.

## Qu'est-ce qu'une promesse ?

![Une promesse animée entre deux personnes](https://www.freecodecamp.org/news/content/images/2023/06/A9vQ.gif)
_Crédit Image : [https://gifer.com](https://gifer.com/en/Pxwc)_

Une promesse est une assurance ou une garantie que quelque chose se produira dans le futur. Une personne peut promettre à une autre personne un résultat ou un résultat spécifique. Les promesses ne sont pas limitées aux individus, les gouvernements et les organisations peuvent également faire des promesses. Vous avez probablement fait une promesse auparavant.

Avec cette assurance (promesse) viennent deux résultats possibles—soit l'accomplissement, soit l'échec. Une promesse est liée à un résultat qui montrera qu'elle est accomplie. Si ce résultat ne se produit pas, alors la promesse a échoué. Une promesse doit avoir à la fin l'un de ces résultats.

En JavaScript, une Promesse est un [objet](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects) qui produira une seule valeur à un moment donné dans le futur. Si la promesse est réussie, elle produira une valeur résolue, mais si quelque chose ne va pas, elle produira une raison pour laquelle la promesse a échoué. Les résultats possibles ici sont similaires à ceux des promesses dans la vie réelle.

Les promesses JavaScript peuvent être dans l'un des trois états possibles. Ces états indiquent la progression de la promesse. Ils sont :

* _en attente_ : C'est l'état par défaut d'une promesse définie
* _accomplie_ : C'est l'état d'une promesse réussie
* _rejetée_ : C'est l'état d'une promesse échouée

Une promesse passe de _en attente_ à _accomplie_, ou de _en attente_ à _rejetée_—'accomplie' et 'rejetée' indiquent la fin d'une promesse.

Désormais, cet article se référera à une 'promesse' comme l'objet JavaScript.

## Comment créer une promesse en JavaScript

Pour créer une promesse, vous devez créer une instance d'objet en utilisant la fonction constructeur `Promise`. La fonction constructeur `Promise` prend un paramètre. Ce paramètre est une fonction qui définit quand résoudre la nouvelle promesse, et optionnellement quand la rejeter.

```js
const promise = new Promise((resolve, reject) => {
  // Condition pour résoudre ou rejeter la promesse
});

```

Par exemple, supposons que vous voulez qu'une promesse se résolve après un délai de deux secondes. Vous pouvez y parvenir en l'écrivant dans le paramètre de la fonction constructeur.

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("Terminé !"), 2000);
});
```

Dans les promesses, `resolve` est une fonction avec un paramètre optionnel représentant la valeur résolue. De plus, `reject` est une fonction avec un paramètre optionnel représentant la raison pour laquelle la promesse a échoué. Dans l'exemple ci-dessus, la valeur résolue de la promesse est la chaîne `'Terminé !'`.

Voici un autre exemple montrant comment vous pouvez résoudre ou rejeter une promesse en fonction des conditions que vous définissez. Dans cet exemple, le résultat de la promesse est basé sur un nombre aléatoire que le programme génère.

```js
const promise = new Promise((resolve, reject) => {
  const num = Math.random();
  if (num >= 0.5) {
    resolve("La promesse est accomplie !");
  } else {
    reject("La promesse a échoué !");
  }
});


```

À partir de ces exemples, vous pouvez voir que vous avez le contrôle sur le moment de résoudre ou de rejeter votre promesse et pouvez la lier à une certaine condition. Avec cela, vous avez appris comment créer une promesse en JavaScript.

## Comment attacher un callback à une promesse

Pour créer un callback pour une promesse, vous devez utiliser la méthode `.then()`. Cette méthode prend deux fonctions de callback. La première fonction s'exécute si la promesse est résolue, tandis que la deuxième fonction s'exécute si la promesse est rejetée.

```js
const promise = new Promise((resolve, reject) => {
  const num = Math.random();
  if (num >= 0.5) {
    resolve("La promesse est accomplie !");
  } else {
    reject("La promesse a échoué !");
  }
});

function handleResolve(value) {
  console.log(value);
}

function handleReject(reason) {
  console.error(reason);
}

promise.then(handleResolve, handleReject);
// La promesse est accomplie !
// ou
// La promesse a échoué !

```

C'est la manière de gérer les résultats possibles de votre promesse. Toute erreur non gérée dans votre promesse les maintiendra dans un état rejeté à la fin, mais les erreurs gérées font que l'opération retourne une promesse accomplie.

Il est possible de créer une promesse immédiatement résolue, puis d'attacher un callback avec la méthode `.then()`. Vous pouvez également créer une promesse immédiatement rejetée de la même manière.

```js
Promise.resolve("Succès").then((result) => console.log(result));
// Succès

Promise.reject("Pas de succès").then((result) => console.log(result));
// Erreur : Uncaught (in promise)

```

L'erreur dans la promesse rejetée est due au fait que vous devez définir un callback séparé pour gérer une promesse rejetée.

```js
Promise.reject("Pas de succès").then(
  () => {
    /* Callback vide si la promesse est accomplie */
  },
  (reason) => console.error(reason)
);
// Pas de succès

```

Maintenant, vous avez correctement géré un résultat rejeté.

Les promesses rendent incroyablement facile l'enchaînement des instructions asynchrones. Lorsque vous gérez une promesse avec la méthode **`.then()`**, l'opération retourne toujours une autre promesse. En employant cette approche, vous pouvez éliminer la précédemment mentionnée 'Pyramide de l'Enfer des Callbacks'.

Considérez le code qui causait précédemment la structure pyramidale :

```js
fetchResource(
  url,
  function (result) {
    // Faire quelque chose avec le résultat
    fetchResource(
      newUrl,
      function (result) {
        // Faire quelque chose avec le nouveau résultat
        fetchResource(
          anotherUrl,
          function (result) {
            // Faire quelque chose avec le nouveau résultat
          },
          failureCallback
        );
      },
      failureCallback
    );
  },
  failureCallback
);
```

Cependant, parce que `.then()` retourne une autre promesse, voici comment écrire les mêmes instructions ci-dessus avec des promesses :

```js
fetchResource(url)
  .then(handleResult, failureCallback)
  .then(handleNewResult, failureCallback)
  .then(handleAnotherResult, failureCallback);

```

Comme vous pouvez le voir, l'appel des promesses ne nécessite pas une syntaxe imbriquée. Vous pouvez même éliminer le `failureCallback` répété pour rendre le code beaucoup plus propre, ce que la section à venir de l'article explorera.

## Comment gérer les erreurs dans une promesse

Pour gérer les erreurs dans les promesses, utilisez la méthode `.catch()`. Si quelque chose ne va pas avec l'une de vos promesses, cette méthode peut attraper la raison de cette erreur.

```js
Promise.reject(new Error()).catch((reason) => console.error(reason));
// Erreur

```

Cette fois dans notre exemple, la sortie d'erreur n'est plus 'uncaught' grâce à `.catch()`.

Vous pouvez également utiliser la méthode `.catch()` dans une chaîne de promesses. Elle attrape la première erreur qu'elle rencontre dans la chaîne.

Par exemple, en refactorisant la chaîne de promesses suivant la fonction `fetchResource()` de l'exemple de la section précédente. Voici comment vous pouvez arrêter la répétition des callbacks d'erreur dans votre code.

```js
fetchResource(url)
  .then(handleResult)
  .then(handleNewResult)
  .then(handleAnotherResult)
  .catch(failureCallback);

```

Vous pouvez également utiliser `.catch()` pour vérifier les erreurs dans un groupe de promesses avant de procéder à d'autres opérations asynchrones.

```js
fetchResource(url)
  .then(handleResult)
  .then(handleNewResult)
  .catch(failureCallback)
  // Vérifier les erreurs dans le groupe de promesses ci-dessus avant de procéder
  .then(handleAnotherResult);

```

La méthode **`.catch()`** traite toute erreur dans une promesse sans nécessiter l'imbrication des fonctions de callback d'erreur.

Pour enchaîner une opération asynchrone à une promesse, indépendamment du fait que la promesse soit résolue ou non, utilisez la méthode `.finally()`. La méthode `.then()` est la manière dont vous gérez les résultats d'une promesse en écrivant des conditions individuelles pour les deux cas, résolu et rejeté. `.catch()` ne s'exécute que lorsqu'il y a une erreur. Mais parfois, vous pourriez vouloir qu'une opération s'exécute quoi qu'il arrive aux promesses précédentes.

L'utilisation de `finally()` aide à prévenir la répétition possible de code dans `.then()` et `.catch()`. Elle est destinée aux opérations que vous devez exécuter, qu'il y ait une erreur ou non.

```js
fetchResource(url)
  .then(handleResult)
  .then(handleNewResult)
  .finally(onFinallyHandle);

```

La méthode `finally()` a quelques cas d'utilisation dans les applications réelles. Elle est importante si vous souhaitez effectuer des opérations de nettoyage pour les activités initiées par la promesse. Un autre cas d'utilisation—dans les applications web Front-End—est la mise à jour de l'interface utilisateur, comme l'arrêt d'un indicateur de chargement.

## Comment gérer plusieurs promesses à la fois

Il est possible d'exécuter plus d'une promesse à la fois. Tous les exemples que vous avez vus jusqu'à présent concernent des promesses qui s'exécutent les unes après les autres.

Dans les exemples précédents, les promesses s'exécutent de manière similaire au code synchrone dans le sens où elles attendent que la précédente soit résolue ou rejetée. Mais vous pourriez avoir plusieurs promesses qui s'exécutent en parallèle.

Voici les méthodes disponibles qui peuvent nous aider à atteindre cet objectif :

* `Promise.all()`
* `Promise.race()`
* `Promise.any()`
* `Promise.allSettled()`

Dans cette section de l'article, nous allons passer en revue ces méthodes.

### La méthode `Promise.all()`

**`Promise.all()`** accepte un tableau de promesses comme argument mais retourne une seule promesse comme sortie. La promesse unique qu'elle retourne se résout avec un tableau de valeurs si toutes les promesses du tableau d'entrée sont accomplies. Le tableau que `Promise.all()` résout contiendra les valeurs résolues des promesses individuelles du tableau d'entrée.

```js
const promise1 = Promise.resolve(`Valeur de la première promesse`);
const promise2 = new Promise((resolve) =>
  setTimeout(resolve, 3000, `Valeur de la deuxième promesse`)
);
const promise3 = new Promise((resolve) =>
  setTimeout(resolve, 2000, `Valeur de la troisième promesse`)
);

Promise.all([promise1, promise2, promise3]);

// Sortie sur la console

// *Promise {<fulfilled>: Array(3)}*

Promise.all([promise1, promise2, promise3]).then((values) => {
  values.forEach((value) => console.log(value));
});

// Sortie sur la console

// Valeur de la première promesse
// Valeur de la deuxième promesse
// Valeur de la troisième promesse

```

Si au moins une promesse dans le tableau d'entrée ne se résout pas, `Promise.all()` retournera une promesse rejetée avec une raison. La raison du rejet sera la même que celle de la première promesse rejetée dans le tableau d'entrée.

```js
const promise1 = Promise.resolve(`Valeur de la première promesse`);
const promise2 = new Promise((resolve, reject) =>
  setTimeout(reject, 2000, `Première raison du rejet`)
);
const promise3 = new Promise((resolve, reject) =>
  setTimeout(reject, 3000, `Deuxième raison du rejet`)
);

Promise.all([promise1, promise2, promise3]);

// Sortie sur la console

// *Promise {<rejected>: "Première raison du rejet"}*
```

`Promise.all()` exécutera toutes les promesses d'entrée avant de retourner une valeur. Mais elle ne les exécute pas les unes après les autres—au lieu de cela, elle les exécute en même temps.

C'est pourquoi le temps total qu'il faudrait à `Promise.all()` pour retourner une valeur est environ le temps qu'il faudrait à la promesse la plus longue du tableau pour se terminer.

![Illustration montrant quand Promise.all() produira une valeur](https://www.freecodecamp.org/news/content/images/2023/06/quickpoll.png)

Malgré cela, elle doit terminer l'exécution de _toutes_ les promesses avant de retourner quoi que ce soit.

### La méthode `Promise.race()`

`Promise.race()` accepte un tableau de promesses comme argument et retourne une seule promesse comme sortie. La promesse unique qu'elle retourne est la promesse la plus rapide à terminer son exécution—résolue ou non. Cela signifie que `Promise.race()` retournera la promesse avec le temps d'exécution le plus court dans un tableau de promesses.

```js
const promise1 = new Promise((resolve) =>
  setTimeout(resolve, 3000, `Valeur de la première promesse`)
);
const promise2 = new Promise((resolve) =>
  setTimeout(resolve, 2000, `Valeur de la deuxième promesse`)
);
const promise3 = Promise.resolve(`Valeur de la troisième promesse`);

Promise.race([promise1, promise2, promise3]);

// Sortie sur la console

// *Promise {<fulfilled>: "Valeur de la troisième promesse"}*

```

Dans l'exemple ci-dessus, parce que `promise3` est une promesse qui se résout à sa création, `Promise.race()` la retourne comme la plus rapide. Tout comme les autres méthodes `Promise` que l'article discute dans cette section, elle exécute les promesses en parallèle et non les unes après les autres.

Si la promesse avec le temps d'exécution le plus court se trouve être rejetée avec une raison, `Promise.race()` retourne une promesse rejetée et la raison pour laquelle la promesse la plus rapide a été rejetée.

```js
const promise1 = Promise.reject(`Raison du rejet`);
const promise2 = new Promise((resolve) =>
  setTimeout(resolve, 3000, `Première promesse résolue`)
);
const promise3 = new Promise((resolve) =>
  setTimeout(resolve, 2000, `Deuxième promesse résolue`)
);

Promise.race([promise1, promise2, promise3]);

// Sortie sur la console

// *Promise {<rejected>: "Raison du rejet"}*

```

![Illustration montrant quand Promise.race() produira une valeur](https://www.freecodecamp.org/news/content/images/2023/06/quickpoll--3-.png)

`Promise.race()` est utile pour exécuter une liste d'opérations asynchrones mais en ayant besoin uniquement du résultat de l'opération exécutée le plus rapidement.

### La méthode `Promise.any()`

`Promise.any()` accepte un tableau de promesses comme argument mais retourne une seule promesse comme sortie. La promesse unique qu'elle retourne est la première promesse résolue dans le tableau d'entrée. Cette méthode attend que _n'importe quelle_ promesse dans le tableau soit résolue et la retournera immédiatement comme sortie.

```js
const promise1 = new Promise((resolve) =>
  setTimeout(resolve, 3000, `Valeur de la première promesse`)
);
const promise2 = new Promise((resolve) =>
  setTimeout(resolve, 2000, `Valeur de la deuxième promesse`)
);
const promise3 = Promise.reject(`Valeur de la troisième promesse`);

Promise.any([promise1, promise2, promise3]);

// Sortie sur la console

// *Promise {<fulfilled>: "Valeur de la deuxième promesse"}*

```

À partir de l'exemple ci-dessus, `promise1` se résoudra après 3 secondes, `promise2` se résoudra après 2 secondes, et `promise3` sera immédiatement rejetée. Parce que `Promise.any()` recherche la première promesse réussie, elle retourne `promise2`. `promise1` est un peu en retard et est donc laissée de côté.

Si aucune des promesses du tableau n'est résolue, **`Promise.any()`** retourne une promesse rejetée. Cette promesse rejetée contient un tableau JavaScript de raisons, où chaque raison correspond à celle d'une promesse du tableau d'entrée.

```js
const promise1 = new Promise((resolve, reject) =>
  setTimeout(reject, 3000, `Première raison de rejet`)
);
const promise2 = new Promise((resolve, reject) =>
  setTimeout(reject, 2000, `Deuxième raison de rejet`)
);
const promise3 = Promise.reject(`Troisième raison de rejet`);

Promise.any([promise1, promise2, promise3]);

// Sortie sur la console

// *Promise {<rejected>: Aggregate Error: All Promises were rejected}*

Promise.any([promise1, promise2, promise3]).catch(({ errors }) =>
  console.log(errors)
);

// Sortie sur la console

// *(3) ["Première raison de rejet", "Deuxième raison de rejet", "Troisième raison de rejet"]*

```

Cette méthode est utile pour les opérations asynchrones où la promesse réussie la plus rapide est tout ce dont vous avez besoin. `Promise.any()` et `Promise.race()` sont similaires, sauf que `Promise.any()` retournera la promesse la plus rapide à compléter et à être résolue, tandis que `Promise.race()` retournera la promesse la plus rapide à compléter et ne se soucie pas de savoir si elle est résolue ou non.

![Illustration montrant quand Promise.any() produira une valeur](https://www.freecodecamp.org/news/content/images/2023/06/quickpoll--1-.png)

### La méthode `Promise.allSettled()`

`Promise.allSettled()` est devenue une fonctionnalité des promesses JavaScript avec la sortie de [ES2020](https://262.ecma-international.org/11.0/). Elle gère les promesses en parallèle tout comme les autres méthodes de promesse que l'article discute dans cette section.

`Promise.allSettled()` aide à écrire un code asynchrone plus efficace car elle montre le résultat de toutes les promesses du tableau, quel que soit leur statut—résolu ou rejeté.

`Promise.allSettled()` accepte un tableau de promesses comme argument et retourne une seule promesse comme sortie.

La promesse unique qu'elle retourne se résoudra toujours ou entrera dans l'état 'accomplie' après que toutes les promesses d'entrée soient réglées. Elle ne se soucie pas si une promesse individuelle dans le tableau d'entrée est rejetée. Le tableau que `Promise.all()` résout contiendra les valeurs résolues ou les raisons de rejet des promesses du tableau d'entrée.

```js
const promise1 = new Promise((resolve) =>
  setTimeout(resolve, 3000, `Valeur de la première promesse`)
);
const promise2 = new Promise((resolve) =>
  setTimeout(resolve, 2000, `Valeur de la deuxième promesse`)
);
const promise3 = Promise.reject(`Valeur de la troisième promesse`);

Promise.allSettled([promise1, promise2, promise3]);

// Sortie sur la console

// *Promise {<fulfilled>: Array(3)}*

Promise.allSettled([promise1, promise2, promise3]).then(console.log);

// Sortie sur la console

/*
(3) [{}, {}, {}]
0: {status: 'fulfilled', value: "Valeur de la première promesse"}
1: {status: 'fulfilled', value: "Valeur de la deuxième promesse"}
2: {status: 'rejected', reason: "Valeur de la troisième promesse"}
*/

```

À partir de l'exemple ci-dessus, vous pouvez voir que même si `promise3` est rejetée à la création, `Promise.allSettled()` retourne toujours une promesse 'accomplie'. Elle le fait même si toutes les promesses du tableau d'entrée sont rejetées.

`Promise.allSettled()` est similaire à `Promise.all()` en ce sens que toutes leurs promesses d'entrée doivent être réglées avant que la promesse qu'elles retournent ait un état réglé—accomplie ou rejetée.

La différence est que `Promise.all()` ne peut être réussie que si toutes les promesses du tableau d'entrée sont résolues, tandis que `Promise.allSettled()` ne se soucie pas du statut des promesses d'entrée.

![Illustration montrant quand Promise.allSettled() produira une valeur](https://www.freecodecamp.org/news/content/images/2023/06/quickpoll--2-.png)

L'utilisation de cette méthode vous donnera un aperçu de la manière dont toutes vos promesses se sont comportées, celles qui ont été résolues et celles qui ont été rejetées. Elle donne des informations complètes sur toutes les promesses que vous lui passez et vous permet de les examiner indépendamment—le résultat de l'une n'affecte pas l'état de la promesse que la méthode retourne.

## Qu'est-ce que la syntaxe Async/Await ?

La syntaxe Async/Await est devenue une fonctionnalité de JavaScript avec la sortie de [ES8(ES2017)](https://262.ecma-international.org/8.0/). Elle est construite sur la base des promesses, et vous pouvez la voir comme une syntaxe alternative aux promesses.

`async/await` élimine l'enchaînement qui est courant avec la syntaxe des promesses, et finit par rendre le code asynchrone beaucoup plus synchrone.

Les promesses sont un excellent moyen d'éviter la précédemment discutée 'Pyramide de l'Enfer des Callbacks', mais async/await va plus loin avec le code asynchrone. Avec async/await, le code est plus facile à suivre et à maintenir. Cela est apparu comme un moyen d'améliorer la lisibilité du code pour les opérations asynchrones. C'est la manière moderne d'utiliser les promesses.

## Comment créer une fonction Async en JavaScript

`async` est un mot-clé JavaScript utilisé pour créer une fonction. La fonction que ce mot-clé aide à créer retournera toujours une promesse. Pour l'utiliser, placez `async` avant le mot-clé `function` lors de la déclaration de la fonction.

```js
async function example() {
	// Retourner une valeur
}

example()

// Sortie sur la console

// *Promise {<fulfilled>: undefined}*

```

À partir de l'exemple de code, vous pouvez voir que la fonction retourne une promesse avec une valeur `undefined`. Cela est dû au fait que tout ce que la fonction `async` retourne sera la valeur résolue de la promesse résultante. Dans ce cas, la fonction ne retourne rien, d'où `undefined`.

```js
async function example() {
  return "C'est bien d'être une fonction async";
}

example();

// Sortie sur la console

// *Promise {<fulfilled>: "C'est bien d'être une fonction async"}*

```

Dans l'exemple ci-dessus, la fonction retourne une chaîne, qui devient la valeur résolue de la promesse résultante. C'est la manière de créer une fonction `async`.

## Comment utiliser le mot-clé Await

Pour utiliser le mot-clé `await`, placez-le avant une promesse. C'est un indicateur pour la fonction `async` de mettre en pause l'exécution jusqu'à ce que cette promesse soit réglée.

C'est similaire à la méthode `.then()` qui s'assure qu'une promesse est 'accomplie' ou 'rejetée' avant de continuer. Notez que vous ne pouvez utiliser le mot-clé `await` qu'à l'intérieur d'une fonction `async`.

Au lieu d'enchaîner les promesses avec `.then()` comme l'article l'enseigne précédemment, vous pouvez répéter _await_ les opérations asynchrones, rendant votre code plus propre et plus facile à lire.

```js
const timerPromise = (message) =>
  new Promise((resolve) => setTimeout(resolve, 3000, message));

async function asyncFunc() {
  const result = await timerPromise("promesse terminée !");
  console.log(result);
}

// Sortie sur la console après 3 secondes

// promesse terminée !

```

L'utilisation du mot-clé `await` avant une promesse produira la valeur résolue de cette promesse. Cela est évident à partir de la ligne `const result = await promise('promesse terminée !')` où `result` devient une chaîne et non une nouvelle promesse. Cela est différent de `.then()` qui retourne toujours une nouvelle promesse.

Avec `await`, vous pouvez diviser toute chaîne de promesses, et obtenir leurs valeurs résolues. L'exemple suivant utilise la fonction `fetch()`—qui est une promesse—pour montrer l'élimination de l'enchaînement avec async/await.

```js
// Avec enchaînement
fetch("https://jsonplaceholder.typicode.com/users")
  .then((response) => response.json())
  .then((result) => console.log(result));

// Sortie sur la console

// Array(10) [...]

// Sans enchaînement
async function fetchResource(url) {
  const response = await fetch(url);
  const result = await response.json();
  console.log(result);
}
fetchResource("https://jsonplaceholder.typicode.com/users");

// Sortie sur la console

// Array(10) [...]

```

En fin de compte, cela revient à la préférence et au choix. Si vous préférez la syntaxe d'enchaînement, alors optez pour elle. Si vous préférez que votre code ressemble à du code synchrone et souhaitez utiliser async/await, alors c'est bien aussi.

Vous pouvez également utiliser les deux syntaxes ensemble, en enchaînant les promesses à l'intérieur d'une fonction async. Tout dépend de ce que vous voulez accomplir et du style que vous préférez.

## Comment gérer les erreurs dans Async/Await

Tout comme avec la syntaxe normale des promesses, vous pouvez attraper les erreurs correctement en utilisant async/await. Gérer correctement les erreurs dans les appels async est extrêmement important pour suivre les bugs. Utilisez des blocs try/catch pour cela.

`try` est un mot-clé JavaScript qui enveloppe un bloc de code. Alors que ce bloc de code s'exécute, `try` vérifie les erreurs. Aucune erreur ne peut échapper à un bloc try. Utilisez `try` à l'intérieur d'une fonction `async`.

La première erreur à l'intérieur du bloc `try` arrête les autres instructions de ce bloc de s'exécuter, `try` passe ensuite la valeur de l'erreur au bloc `catch`. Le bloc `catch` est similaire à `.catch()` dans les promesses. Tout comme la méthode de promesse, c'est une fonction d'une erreur.

```js
async function fetchResource(url) {
  try {
    const response = await fetch(url);
    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

```

Dans cet exemple, le mot-clé `catch` a une erreur, qui est enregistrée dans la console. Une promesse réglée avec une erreur non attrapée entraîne une promesse rejetée. Assurez-vous d'envelopper votre code dans des blocs try/catch pour avoir plus de contrôle sur les échecs et les défauts dans votre programme.

De plus, tout comme la méthode `.finally()` pour les promesses, vous pouvez utiliser un bloc `finally` à l'intérieur d'une fonction async. Les accolades qui suivent ce mot-clé enveloppent un bloc de code qui s'exécuterait indépendamment du fait qu'il y ait une erreur ou non.

```js
async function fetchResource(url) {
  try {
    const response = await fetch(url);
    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error(error);
  } finally {
    console.log("Opération terminée !");
  }
}
```

L'utilisation du bloc `finally` est similaire à l'utilisation de la méthode `.finally()`. Cela prouve simplement que l'utilisation d'une fonction async est une manière récente de travailler avec les promesses.

## Qu'est-ce qu'une file d'attente de tâches ?

La file d'attente de tâches—également connue sous le nom de file d'attente de micro-tâches—est un concept important à connaître en JavaScript. Elle ne faisait pas partie du runtime JavaScript à l'origine, mais le besoin s'en est fait sentir lorsque les promesses sont devenues une partie de JavaScript.

Considérez l'exemple de code suivant :

```js
Promise.resolve("Ceci est une valeur résolue").then(console.log);
setTimeout(console.log, 0, "Ceci est une valeur après le délai");
console.log("Ceci est un log normal");

```

Ici, la première ligne est une promesse qui se résout automatiquement, puis enregistre la valeur sur la console. La deuxième ligne est un délai défini à 0 millisecondes, ce qui signifie qu'il est censé être instantané. Le délai prend une fonction de callback qui enregistre une valeur sur la console. La troisième ligne est un log de console normal.

Lorsque vous exécutez le programme, pouvez-vous deviner l'ordre dans lequel ces logs apparaîtront ? Découvrons-le.

```js
// Sortie sur la console
/*
Ceci est un log normal
Ceci est une valeur résolue
--
undefined
--
Ceci est une valeur après le délai
*/

```

C'est une sortie intéressante. Le premier log provient de `console.log`. Ce n'est pas si déroutant car `console.log()` n'est pas une opération async. Le moteur JavaScript exécutera activement chaque instruction synchrone immédiatement après le démarrage du programme.

La deuxième ligne peut être un peu déroutante. Elle enregistre la valeur résolue de la promesse. Pourquoi la sortie de la promesse vient-elle ensuite ? Eh bien, la réponse simple est qu'une promesse est plus rapide que toute autre implémentation async en JavaScript. Mais ce n'est pas toute l'histoire.

Dans le runtime JavaScript, la boucle d'événements gère les opérations async. Elle ne peut appeler les fonctions de callback des instructions async que lorsque la pile d'appels est vide. Résoudre une promesse est une opération asynchrone, et il est compréhensible qu'elle vienne après un log normal. Mais pourquoi vient-elle avant l'instruction `setTimeout()` ?

Le runtime JavaScript a en fait ces deux files d'attente—la file d'attente de callbacks (ou Macrotask) et la file d'attente de tâches (ou Microtask). Peu avant que la boucle d'événements ne commence à appeler les fonctions dans la file d'attente de callbacks, elle appelle toutes les instructions de la file d'attente de tâches. Le callback d'une promesse reste dans la file d'attente de tâches, donc la boucle d'événements l'appelle en premier. C'est pourquoi les promesses retournent des valeurs plus rapidement que toute autre implémentation async.

La file d'attente de tâches est utile pour certaines autres instructions en plus des promesses. Cependant, cela dépasse le cadre de ce matériel. Si vous êtes curieux, vous pouvez [en lire plus sur la file d'attente de tâches ici](https://blog.greenroots.info/task-queue-and-job-queue-deep-dive-into-javascript-event-loop-model).

Un programme retourne immédiatement après avoir pris en charge la file d'attente de tâches. À partir de l'exemple de code ci-dessus, il retourne avec `undefined`. Après cela, la boucle d'événements passe à la file d'attente de callbacks et exécute les instructions qui s'y trouvent.

![Illustration représentant la file d'attente de micro-tâches et la file d'attente de callbacks (Macrotask)](https://www.freecodecamp.org/news/content/images/2023/06/event-loop.gif)
_Crédit Image : [Medium](https://medium.com/@saravanaeswari22/microtasks-and-macro-tasks-in-event-loop-7b408b2949e0">Saravanakumar</a> sur <a href="https://medium.com)_

Le callback dans `setTimeout()` se déplacera toujours vers la file d'attente de callbacks, peu importe la durée du minuteur. Dans l'exemple, il a été enregistré en dernier bien que le minuteur ait été défini à 0 millisecondes.

Avec cela, j'espère que vous comprenez pourquoi l'exemple de code a produit cette sortie, et la différence entre la file d'attente de callbacks et la file d'attente de micro-tâches.

## Conclusion

Cela a été une plongée profonde dans les promesses et les opérations async. Dans cet article, vous avez appris comment les promesses sont apparues en JavaScript, ce qu'elles sont, et comment les créer.

Vous avez également appris comment attacher des callbacks à une promesse, comment attraper les erreurs dans une promesse, et comment exécuter plusieurs promesses simultanément.

Nous avons également examiné la syntaxe async/await qui est construite sur la base des promesses. Vous avez appris quand elles sont devenues une fonctionnalité de JavaScript, comment créer une fonction async, et comment utiliser le mot-clé await.

Vous avez également appris comment gérer les erreurs en utilisant la syntaxe. Enfin, l'article a expliqué ce qu'est une file d'attente de tâches.

N'hésitez pas à revenir si vous n'avez pas tout compris du premier coup. Les promesses JavaScript peuvent prendre du temps à apprendre et à maîtriser, mais tout développeur JavaScript bénéficierait énormément de savoir comment fonctionnent les promesses. Cela vous donne plus de contrôle lors de l'écriture de code async professionnel pour vos applications.

Bonne chance pour la construction de votre prochain projet.

PS : Suivez-moi sur [Twitter](https://twitter.com/EnyichiA) et [LinkedIn](https://www.linkedin.com/in/enyichiaagu/).