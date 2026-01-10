---
title: Comment utiliser Promise.allSettled() en JavaScript
subtitle: ''
author: Rahul
co_authors: []
series: null
date: '2023-06-27T17:03:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-promise-allsettled-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/andrew-petrov-hopnkQoC0dg-unsplash.jpg
tags:
- name: asynchronous
  slug: asynchronous
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
seo_title: Comment utiliser Promise.allSettled() en JavaScript
seo_desc: "Have you ever worked with promises in JavaScript and gotten frustrated\
  \ when one rejects and ruins everything? \nYou write some promise-based code, everything\
  \ is chugging along nicely, and then boom – one little promise rejects and the whole\
  \ chain come..."
---

Avez-vous déjà travaillé avec des promesses en JavaScript et été frustré lorsqu'une seule est rejetée et ruine tout ?

Vous écrivez du code basé sur des promesses, tout se déroule bien, et puis boum – une petite promesse est rejetée et toute la chaîne s'écroule.

Votre code s'arrête net et vous vous demandez pourquoi JavaScript ne pouvait pas simplement ignorer ce petit contretemps et continuer son bonhomme de chemin. Eh bien, mon ami, j'ai une bonne nouvelle pour vous.

Rencontrez `Promise.allSettled()`, votre nouveau meilleur ami et la promesse dont vous ne saviez pas que vous aviez besoin. `Promise.allSettled()` est un changement de jeu, vous permettant d'attendre que toutes vos promesses se règlent – soit qu'elles se résolvent, soit qu'elles soient rejetées – et ensuite d'agir en fonction des résultats.

Plus de chaînes de promesses ruinées ou de rejets non gérés. Juste du pur bonheur de promesse sans altération. Rejoignez-moi alors que nous plongeons dans cette méthode de promesse peu connue mais incroyablement utile et voyons à quel point elle peut simplifier votre code [asynchrone JavaScript](https://www.freecodecamp.org/news/asynchronous-javascript/).

## Qu'est-ce que Promise.allSettled() ?

Vous voulez utiliser la méthode Promise.allSettled() de JavaScript, mais vous n'êtes pas tout à fait sûr de son fonctionnement ou de la raison pour laquelle vous voudriez l'utiliser ? Pas de souci, je vous couvre.

`Promise.allSettled()` attend que toutes les promesses que vous lui donnez se règlent, ce qui signifie soit qu'elles se résolvent, soit qu'elles soient rejetées. Elle retourne ensuite un tableau d'objets avec le statut et la valeur ou la raison de chaque promesse.

Cela est utile lorsque vous avez plusieurs tâches asynchrones que vous voulez vous assurer d'avoir complétées, mais que vous ne vous souciez pas nécessairement si certaines échouent.

Par exemple, disons que vous avez trois appels API qui retournent des promesses, et que vous voulez obtenir toutes les données des appels réussis, même si l'un échoue. Vous pourriez faire :

```js
Promise.allSettled([apiCall1(), apiCall2(), apiCall3()]).then((results) => {});

```

Cela exécutera les trois appels API, et la fonction de rappel `.then()` sera appelée une fois qu'ils seront tous réglés. Le tableau des résultats contiendra trois objets : un pour chaque promesse, avec soit un statut 'fulfilled' et les données, soit 'rejected' et l'erreur.

Nous pouvons filtrer pour obtenir uniquement les appels réussis, et continuer en utilisant ces données.

Les points clés à retenir sont :

* `Promise.allSettled()` attend que toutes les promesses d'entrée se règlent et retourne leurs résultats.
* Réglé signifie soit résolu (fulfilled), soit rejeté.
* Il retourne un tableau d'objets avec le statut et la valeur/raison pour chaque promesse d'entrée.
* Il permet de gérer les promesses réussies même lorsque certaines sont rejetées.

## Le problème avec `Promise.all()` et la solution avec `Promise.allSettled()`

`Promise.all()` est génial lorsque vous voulez attendre que plusieurs promesses se complètent et obtenir un tableau de toutes les valeurs résolues. Mais il a un inconvénient majeur : si l'une des promesses est rejetée, l'ensemble du `Promise.all()` est rejeté immédiatement.

Cela peut être problématique dans certains cas. Par exemple, disons que vous faites des requêtes à trois services backend différents, et que vous ne vous souciez pas vraiment si l'un échoue tant que les deux autres réussissent. Avec `Promise.all()`, une seule promesse rejetée rejetterait l'ensemble du groupe, et vous manqueriez les réponses réussies des autres promesses.

Heureusement, il existe une solution simple : `Promise.allSettled()`. Cela fonctionne de manière similaire à `Promise.all()` mais au lieu de rejeter immédiatement si une promesse est rejetée, il attend que toutes les promesses se règlent (soit qu'elles se résolvent, soit qu'elles soient rejetées) et retourne ensuite un tableau d'objets avec le statut et la valeur/raison de chaque promesse.

Par exemple :

```js
Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("2")),
  Promise.resolve(3),
]).then((results) => {
  // results est un tableau de :
  // {status: "fulfilled", value: 1}
  // {status: "rejected", reason: Error}
  // {status: "fulfilled", value: 3}
});

```

Comme vous pouvez le voir, même si la deuxième promesse a été rejetée, nous obtenons toujours les valeurs résolues des autres promesses. Cela vous permet de gérer les rejets avec grâce sans manquer de réponses réussies.

`Promise.allSettled()` offre plus de flexibilité dans ces types de situations. Vous obtenez une image complète de toutes vos promesses, indépendamment du fait que certaines soient rejetées, afin que vous ayez l'opportunité de toujours utiliser les valeurs résolues et de gérer les rejets de manière appropriée.

Alors, la prochaine fois que vous devrez attendre plusieurs promesses mais que vous ne pourrez pas vous permettre de manquer des valeurs résolues en raison d'un rejet, assurez-vous d'utiliser `Promise.allSettled()` ! C'est un ajout très utile à l'[API Promise](https://www.freecodecamp.org/news/tag/promises/).

## Questions courantes sur `Promise.allSettled()`

### Est-ce que `Promise.allSettled()` ralentira mon code ?

Pas vraiment. `Promise.allSettled()` attend simplement que toutes les promesses que vous lui passez se règlent, soit en se remplissant, soit en étant rejetées. Il ne fait rien d'autre qui pourrait impacter les performances.

### Puis-je toujours attraper les erreurs avec `Promise.allSettled()` ?

Oui, absolument ! `Promise.allSettled()` vous donnera le résultat de chaque promesse, qu'elle ait été remplie ou rejetée.

Pour toute promesse rejetée, vous obtiendrez la raison pour laquelle elle a été rejetée, généralement une erreur. Vous pouvez attraper ces erreurs dans le gestionnaire `.catch()` de l'appel `Promise.allSettled()`.

### Quand devrais-je utiliser `Promise.allSettled()` par rapport à `Promise.all()` ?

Utilisez `Promise.allSettled()` lorsque vous voulez exécuter plusieurs promesses en parallèle, mais que vous ne voulez pas qu'une seule promesse rejetée cause le rejet de l'ensemble du groupe.

Par exemple, si vous récupérez des données à partir de plusieurs API tierces, une promesse rejetée d'une API ne devrait pas vous empêcher d'obtenir des données des autres API.

Utilisez `Promise.all()` lorsque vous voulez exécuter des promesses en parallèle mais que vous avez besoin qu'elles se complètent toutes avec succès pour que votre code continue.

Par exemple, si vous devez récupérer des données de deux API pour les afficher sur une page, vous voudriez que les deux promesses se remplissent avant de rendre les données.

### Puis-je obtenir les résultats des promesses réglées ?

Oui ! `Promise.allSettled()` retourne un tableau d'objets avec le statut et la valeur/raison de chaque promesse. Par exemple :

```js
Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("2")),
  Promise.resolve(3),
]).then((results) => {
  console.log(results);
  /*
    [
      { status: "fulfilled", value: 1 },
      { status: "rejected", reason: Error: 2 },
      { status: "fulfilled", value: 3 }
    ]
    */
});

```

Vous obtiendrez des informations sur toutes les promesses, qu'elles aient été remplies ou rejetées, afin que vous ayez une image complète des opérations parallèles.

## Conclusion

Voilà donc. `Promise.allSettled()` est une méthode pratique dont vous ne saviez pas que vous aviez besoin.

Vous n'avez plus besoin d'envelopper `Promise.all()` dans un try/catch juste pour gérer les rejets potentiels. Vous pouvez laisser `Promise.allSettled()` gérer tout cela pour vous et vous concentrer uniquement sur les valeurs résolues. Votre code asynchrone sera plus propre et plus facile à lire.

Merci d'avoir lu. Je suis [Rahul](https://rahul.biz), j'ai 19 ans et je suis rédacteur technique. Voici ma [preuve de travail](https://fueler.io/rahoool).