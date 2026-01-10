---
title: Qu'est-ce qu'une Promesse ? Les Promesses JavaScript pour Débutants
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-16T22:56:20.000Z'
originalURL: https://freecodecamp.org/news/what-is-promise-in-javascript-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/JS-Promises-Expl.png
tags:
- name: JavaScript
  slug: javascript
- name: promises
  slug: promises
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce qu'une Promesse ? Les Promesses JavaScript pour Débutants
seo_desc: 'If you''re a JavaScript beginner, you might be struggling to understand
  what a promise really is.

  I recently published this as a thread on Twitter and was blown away by the responses.
  So I decided to expand this into an introductory tutorial on JavaSc...'
---

Si vous êtes un débutant en JavaScript, vous avez peut-être du mal à comprendre ce qu'est vraiment une promesse.

J'ai récemment publié cela sous forme de fil sur Twitter et j'ai été impressionné par les réponses. J'ai donc décidé d'en faire un tutoriel d'introduction sur les promesses JavaScript.

J'ai lu beaucoup d'articles sur les promesses et le problème est que beaucoup de ces guides ne les expliquent pas de manière compréhensible. Les gens ne comprennent pas ce qu'est une promesse en JavaScript parce qu'ils ne savent pas vraiment de quoi il s'agit et comment elle se comporte en termes simples et compréhensibles.

Alors dans cet article, je vais vous raconter une courte histoire qui explique ce que sont les promesses et comment elles fonctionnent exactement. Je vais également vous montrer comment utiliser les promesses dans votre JavaScript avec quelques exemples.

## Qu'est-ce qu'une Promesse en JavaScript ?

Imaginez que vous interviewez des candidats pour un poste dans votre entreprise.

Un jeune homme arrive en hâte pour un entretien. Alors que sa session d'entretien est sur le point de commencer, il réalise qu'il a oublié son CV.

Dommage, n'est-ce pas ?

Il n'est pas découragé, cependant. Heureusement pour lui, il a un colocataire qui était encore à la maison à ce moment-là.

Il appelle rapidement son colocataire au téléphone et lui demande de l'aide. Il supplie son colocataire de l'aider à trouver son CV. Son colocataire PROMET de lui envoyer un message dès qu'il a quelque chose à signaler.

En supposant que le CV soit finalement trouvé, il peut envoyer un message :

> « Succès, j'ai trouvé votre CV ! »

Mais s'il ne le trouve pas, il est censé envoyer un message d'échec avec la raison pour laquelle il n'a pas pu trouver le CV. Par exemple, il peut envoyer ce message à son ami qui est en entretien :

> « Désolé, je n'ai pas pu trouver votre CV parce que la clé de votre coffre-fort est manquante. »

En attendant, l'entretien se poursuit comme prévu, et l'intervieweur s'accroche à la promesse de trouver le CV, et non au CV lui-même. À ce moment-là, l'intervieweur définit le statut de la livraison du CV comme EN ATTENTE.

Le candidat répond à toutes les questions qui lui sont posées. Mais en fin de compte, son embauche dépend toujours du STATUT FINAL de son CV.

Son colocataire envoie enfin un message. Comme nous l'avons discuté précédemment, s'il n'a pas trouvé le CV, il partagera cet échec avec vous ainsi que la raison pour laquelle il ne l'a pas trouvé.

Lorsque cela se produit, l'entretien se terminera et le candidat sera rejeté.

D'un autre côté, si le colocataire trouve le CV, il annoncera joyeusement à son ami qu'il a réussi, et il ira de l'avant et RÉALISERA ses espoirs d'obtenir un emploi.

## Comment cela se traduit-il en code JS ?

La promesse du colocataire de trouver le CV et d'envoyer un message est synonyme de la manière dont nous définissons une promesse en JavaScript. Le code ne retourne pas directement ou immédiatement une valeur. Au lieu de cela, il retourne une promesse qu'il fournira éventuellement la valeur à un moment ultérieur.

Une promesse en JavaScript est asynchrone, ce qui signifie qu'elle prend du temps à se résoudre ou à se terminer. Tout comme la recherche du CV du candidat prend du temps à se compléter.

Pour cette raison, l'intervieweur décide de ne pas rester assis à ne rien faire, alors ils commencent à interviewer le candidat sur la base de la promesse de livraison d'un CV. Nous utilisons la promesse de retourner un CV à la place d'un CV réel.

Le moteur JS n'attend pas non plus en ne faisant rien – il commence à exécuter d'autres parties du code, en attendant la valeur retournée de la promesse.

Le message texte contient le message d'état de la recherche du CV. Avec une promesse JavaScript, cela s'appelle également la valeur de retour.

Si le message est un « succès », nous procéderons à l'embauche du candidat et lui accorderons le poste. Si cela échoue, nous procéderons au rejet de sa candidature.

Avec les promesses JavaScript, nous faisons cela en [utilisant une fonction de rappel](https://www.freecodecamp.org/news/javascript-callback-functions-what-are-callbacks-in-js-and-how-to-use-them/) (gestionnaires de promesse). Ces fonctions sont définies dans une méthode `then()` imbriquée.

Pour spécifier quels rappels appeler, vous utilisez les deux fonctions suivantes :

* `resolve(value)` : Cela indique que la tâche asynchrone a réussi. Cela appellera le rappel de réalisation dans le gestionnaire `then()`.

* `reject(error)` : Cela indique une erreur lors de l'exécution de la tâche asynchrone. Cela appellera le rappel de rejet dans le gestionnaire `then()`.

Si la promesse est réussie, le rappel de réalisation sera appelé. Si la promesse est rejetée, le rappel de rejet sera appelé à la place.

Une promesse est simplement un espace réservé pour une tâche asynchrone qui n'est pas encore terminée. Lorsque vous définissez un objet de promesse dans votre script, au lieu de retourner une valeur immédiatement, il retourne une promesse.

## Comment écrire une promesse en JavaScript

Vous pouvez définir une promesse dans votre JavaScript en appelant la classe `Promise` et en construisant un objet comme ceci :

```js
const myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('this is the eventual value the promise will return');
  }, 300);
});

console.log(myPromise);
```

L'exécution de ceci dans la console retournera un objet `Promise` :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/promise-console-1.png align="left")

Construire un objet n'est pas la seule façon de définir une promesse, cependant. Vous pouvez également utiliser l'API intégrée `Promise` pour atteindre le même objectif :

```js
const anotherPromise = Promise.resolve("this is the eventual value the promise will return")

console.log(anotherPromise);
```

Alors que la promesse dans le premier exemple de code attendra 3 secondes avant de réaliser la promesse avec le message `this is the eventual...`, la promesse dans le deuxième exemple de code la réalisera immédiatement avec le même message.

## Promesses rejetées en JavaScript

Une promesse peut également être rejetée. La plupart du temps, les rejets se produisent parce que JS a rencontré une sorte d'erreur lors de l'exécution du code asynchrone. Dans un tel scénario, il appelle la fonction `reject()` à la place.

Voici un exemple simple et artificiel de la manière dont une promesse peut être rejetée :

```js
const myPromise = new Promise((resolve, reject) => {
  let a = false;
  setTimeout(() => {
    return (a) ? resolve('a is found!'): reject('sorry, no a');
  }, 300);
});
```

Pouvez-vous penser à la raison pour laquelle cette promesse est rejetée ? Si vous avez dit "parce que `a` n'est pas faux", félicitations !

La promesse dans le troisième exemple de code se résoudra en un rejet après un délai de trois secondes, parce que l'instruction `(a)?` se résout à faux, ce qui déclenchera `reject`.

## Comment enchaîner les promesses avec `then()`

Lorsque la promesse retourne enfin une valeur, vous voudrez généralement faire quelque chose avec cette valeur de retour.

Par exemple, si vous faisiez une requête réseau, vous pourriez vouloir accéder à la valeur et l'afficher sur la page pour l'utilisateur.

Vous pouvez définir deux fonctions de rappel que vous souhaitez appeler lorsqu'une promesse est soit réalisée soit rejetée. Ces fonctions sont définies à l'intérieur d'une méthode `then()` imbriquée :

```js
const anotherPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('this is the eventual value the promise will return');
  }, 300);
});

// CONTINUATION
anotherPromise
.then(value => { console.log(value) })
```

L'exécution de ce code affichera le message de réalisation après trois secondes dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/EVENTAL-RETURN.png align="left")

Notez que vous pouvez imbriquer autant de promesses que vous le souhaitez. Chaque étape s'exécutera après l'étape précédente, en prenant la valeur de retour de cette étape précédente :

```js
const anotherPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('this is the eventual value the promise will return');
  }, 300);
});

anotherPromise
.then(fulfillFn, rejectFn)
.then(fulfilFn, rejectFn)
.then(value => { console.log(value) })
```

Mais nous avons manqué quelque chose d'important.

Gardez toujours à l'esprit qu'une méthode `then()` doit prendre à la fois le gestionnaire de réalisation et un gestionnaire de rejet. Ainsi, le premier est appelé si la promesse est réalisée et le second est appelé si la promesse est rejetée avec une erreur.

Les promesses dans les exemples de code quatre et cinq n'incluent pas de second gestionnaire. Donc, en supposant qu'une erreur est rencontrée, il n'y aurait pas de gestionnaire de rejet pour gérer l'erreur.

Si vous allez définir une seule fonction de rappel (aka un gestionnaire de réalisation) dans `then()`, alors vous devrez imbriquer une méthode `catch()` en bas de la chaîne de promesses pour attraper toute erreur possible.

### Comment utiliser la méthode `catch()` en JS

La méthode `catch()` sera toujours appelée chaque fois qu'une erreur est rencontrée à un moment donné le long de la chaîne de promesses :

```js
const myPromise = new Promise((resolve, reject) => {
  let a = false;
  setTimeout(() => {
    return (a) ? resolve('a is found!'): reject('sorry, no a');
  }, 300);
}); 

myPromise
.then(value => { console.log(value) })
.catch(err => { console.log(err) });
```

Puisque `myPromise` se résoudra finalement en un rejet, la fonction définie dans le `then()` imbriqué sera ignorée. Au lieu de cela, le gestionnaire d'erreur dans `catch()` s'exécutera, ce qui devrait journaliser le message d'erreur suivant dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Catch.png align="left")

## Conclusion

Les promesses JavaScript sont une fonctionnalité très puissante qui vous aide à exécuter du code asynchrone en JavaScript. Dans la plupart, sinon tous, les entretiens pour des rôles utilisant JavaScript, votre intervieweur vous posera probablement une question sur les promesses.

Dans cet article, j'ai expliqué ce qu'est une promesse en termes simples, et j'ai montré son utilisation pratique de base avec quelques exemples de code.

J'espère que vous avez tiré quelque chose d'utile de cet article. Si vous aimez les tutoriels liés à la programmation comme celui-ci, vous devriez [consulter mon blog](https://ubahthebuilder.tech/user-authentication-vs-user-authorization-what-do-they-mean-in-back-end-web-development). J'y publie régulièrement des articles sur le développement logiciel.

Merci d'avoir lu et à bientôt.

**P/S** : Si vous apprenez JavaScript, j'ai créé un eBook qui enseigne 50 sujets en JavaScript avec des notes numériques dessinées à la main. [Découvrez-le ici](https://ubahthebuilder.gumroad.com/l/js-50).