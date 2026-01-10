---
title: Comment échapper à l'enfer async/await
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-07T03:41:16.000Z'
originalURL: https://freecodecamp.org/news/avoiding-the-async-await-hell-c77a0fb71c4c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_3nDjjPTWn4ohLt96IcwCA.png
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment échapper à l'enfer async/await
seo_desc: 'By Aditya Agarwal

  async/await freed us from callback hell, but people have started abusing it — leading
  to the birth of async/await hell.

  In this article, I will try to explain what async/await hell is, and I’ll also share
  some tips to escape it.

  Wha...'
---

Par Aditya Agarwal

async/await nous a libérés de l'enfer des callbacks, mais les gens ont commencé à en abuser — ce qui a conduit à la naissance de l'enfer async/await.

Dans cet article, je vais essayer d'expliquer ce qu'est l'enfer async/await, et je vais également partager quelques conseils pour y échapper.

### Qu'est-ce que l'enfer async/await

Lorsqu'on travaille avec JavaScript asynchrone, les gens écrivent souvent plusieurs instructions les unes après les autres et ajoutent un **await** avant un appel de fonction. Cela pose des problèmes de performance, car souvent une instruction ne dépend pas de la précédente — mais vous devez quand même attendre que la précédente soit terminée.

### Un exemple d'enfer async/await

Imaginez que vous écriviez un script pour commander une pizza et une boisson. Le script pourrait ressembler à ceci :

En surface, cela semble correct, et cela fonctionne. Mais ce n'est pas une bonne implémentation, car elle ne tire pas parti de la concurrency. Comprenons ce qu'il fait pour identifier le problème.

#### Explication

Nous avons enveloppé notre code dans une [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) asynchrone. Les étapes suivantes se produisent dans cet ordre exact :

1. Obtenir la liste des pizzas.
2. Obtenir la liste des boissons.
3. Choisir une pizza dans la liste.
4. Choisir une boisson dans la liste.
5. Ajouter la pizza choisie au panier.
6. Ajouter la boisson choisie au panier.
7. Commander les articles dans le panier.

#### Alors, qu'est-ce qui ne va pas ?

Comme je l'ai souligné plus tôt, toutes ces instructions s'exécutent les unes après les autres. Il n'y a pas de concurrency ici. Réfléchissez bien : pourquoi attendons-nous d'obtenir la liste des pizzas avant d'essayer d'obtenir la liste des boissons ? Nous devrions simplement essayer d'obtenir les deux listes ensemble. Cependant, lorsque nous devons choisir une pizza, nous avons besoin d'avoir la liste des pizzas au préalable. Il en va de même pour les boissons.

Nous pouvons donc conclure que le travail lié à la pizza et le travail lié à la boisson peuvent se faire en parallèle, mais les étapes individuelles impliquées dans le travail lié à la pizza doivent se faire séquentiellement (les unes après les autres).

#### Un autre exemple de mauvaise implémentation

Ce snippet JavaScript va récupérer les articles dans le panier et envoyer une demande pour les commander.

```js
async function orderItems() {
  const items = await getCartItems()    // appel asynchrone
  const noOfItems = items.length
  for(var i = 0; i < noOfItems; i++) {
    await sendRequest(items[i])    // appel asynchrone
  }
}
```

Dans ce cas, la boucle for doit attendre que la fonction `sendRequest()` soit terminée avant de continuer à l'itération suivante. Cependant, nous n'avons pas vraiment besoin d'attendre. Nous voulons envoyer toutes les requêtes aussi rapidement que possible, puis nous pouvons attendre qu'elles soient toutes terminées.

J'espère que maintenant vous vous rapprochez de la compréhension de ce qu'est l'enfer async/await et de la manière dont il affecte gravement les performances de votre programme. Maintenant, je veux vous poser une question.

### Que se passe-t-il si nous oublions le mot-clé await ?

Si vous oubliez d'utiliser **await** lors de l'appel d'une fonction asynchrone, la fonction commence à s'exécuter. Cela signifie que await n'est pas requis pour exécuter la fonction. La fonction asynchrone retournera une promesse, que vous pourrez utiliser plus tard.

```js
(async () => {
  const value = doSomeAsyncTask()
  console.log(value) // une promesse non résolue
})()
```

Une autre conséquence est que le compilateur ne saura pas que vous voulez attendre que la fonction s'exécute complètement. Ainsi, le compilateur quittera le programme sans terminer la tâche asynchrone. Nous avons donc besoin du mot-clé **await**.

```js
(async () => {
  const promise = doSomeAsyncTask()
  const value = await promise
  console.log(value) // la valeur réelle
})()
```

Une propriété intéressante des promesses est que vous pouvez obtenir une promesse dans une ligne et attendre qu'elle soit résolue dans une autre. C'est la clé pour échapper à l'enfer async/await.

Comme vous pouvez le voir, `doSomeAsyncTask()` retourne une promesse. À ce stade, `doSomeAsyncTask()` a commencé son exécution. Pour obtenir la valeur résolue de la promesse, nous utilisons le mot-clé await et cela indiquera à JavaScript de ne pas exécuter la ligne suivante immédiatement, mais d'attendre que la promesse soit résolue puis d'exécuter la ligne suivante.

### Comment sortir de l'enfer async/await ?

Vous devriez suivre ces étapes pour échapper à l'enfer async/await.

#### Trouver les instructions qui dépendent de l'exécution d'autres instructions

Dans notre premier exemple, nous choisissions une pizza et une boisson. Nous avons conclu que, avant de choisir une pizza, nous devons avoir la liste des pizzas. Et avant d'ajouter la pizza au panier, nous devons choisir une pizza. Nous pouvons donc dire que ces trois étapes dépendent les unes des autres. Nous ne pouvons pas faire une chose tant que nous n'avons pas terminé la précédente.

Mais si nous regardons cela plus largement, nous constatons que le choix d'une pizza ne dépend pas du choix d'une boisson, nous pouvons donc les choisir en parallèle. C'est une chose que les machines peuvent faire mieux que nous.

Ainsi, nous avons découvert certaines instructions qui dépendent de l'exécution d'autres instructions et d'autres qui n'en dépendent pas.

#### Regrouper les instructions dépendantes dans des fonctions asynchrones

Comme nous l'avons vu, la sélection d'une pizza implique des instructions dépendantes comme l'obtention de la liste des pizzas, le choix d'une pizza, puis l'ajout de la pizza choisie au panier. Nous devrions regrouper ces instructions dans une fonction asynchrone. De cette manière, nous obtenons deux fonctions asynchrones, `selectPizza()` et `selectDrink()`.

#### Exécuter ces fonctions asynchrones de manière concurrente

Nous tirons ensuite parti de la boucle d'événements pour exécuter ces fonctions asynchrones non bloquantes de manière concurrente. Deux modèles courants pour cela sont **le retour précoce des promesses** et la **méthode Promise.all**.

### Corrigons les exemples

En suivant les trois étapes, appliquons-les à nos exemples.

```js
async function selectPizza() {
  const pizzaData = await getPizzaData()    // appel asynchrone
  const chosenPizza = choosePizza()    // appel synchrone
  await addPizzaToCart(chosenPizza)    // appel asynchrone
}

async function selectDrink() {
  const drinkData = await getDrinkData()    // appel asynchrone
  const chosenDrink = chooseDrink()    // appel synchrone
  await addDrinkToCart(chosenDrink)    // appel asynchrone
}

(async () => {
  const pizzaPromise = selectPizza()
  const drinkPromise = selectDrink()
  await pizzaPromise
  await drinkPromise
  orderItems()    // appel asynchrone
})()

// Bien que je préfère cette méthode

Promise.all([selectPizza(), selectDrink()]).then(orderItems)   // appel asynchrone
```

Maintenant, nous avons regroupé les instructions en deux fonctions. À l'intérieur de la fonction, chaque instruction dépend de l'exécution de la précédente. Ensuite, nous exécutons de manière concurrente les deux fonctions `selectPizza()` et `selectDrink()`.

Dans le deuxième exemple, nous devons gérer un nombre inconnu de promesses. Gérer cette situation est très facile : nous créons simplement un tableau et y ajoutons les promesses. Ensuite, en utilisant `Promise.all()`, nous attendons de manière concurrente que toutes les promesses soient résolues.

```js
async function orderItems() {
  const items = await getCartItems()    // appel asynchrone
  const noOfItems = items.length
  const promises = []
  for(var i = 0; i < noOfItems; i++) {
    const orderPromise = sendRequest(items[i])    // appel asynchrone
    promises.push(orderPromise)    // appel synchrone
  }
  await Promise.all(promises)    // appel asynchrone
}

// Bien que je préfère cette méthode

async function orderItems() {
  const items = await getCartItems()    // appel asynchrone
  const promises = items.map((item) => sendRequest(item))
  await Promise.all(promises)    // appel asynchrone
}
```

J'espère que cet article vous a aidé à voir au-delà des bases de async/await, et vous a également aidé à améliorer les performances de votre application.

Si vous avez aimé l'article, n'hésitez pas à applaudir. Astuce — Vous pouvez applaudir 50 fois !

N'hésitez pas à partager sur Facebook et Twitter. Si vous souhaitez recevoir des mises à jour, suivez-moi sur [Twitter](https://twitter.com/dev__adi) et [Medium](https://medium.com/@adityaa803/) ou abonnez-vous à [ma newsletter](https://buttondown.email/itaditya) ! Si quelque chose n'est pas clair ou si vous voulez signaler quelque chose, veuillez commenter ci-dessous.