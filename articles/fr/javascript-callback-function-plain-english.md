---
title: Fonction de Rappel JavaScript – Expliquée en Anglais Simple
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-10-05T17:17:28.000Z'
originalURL: https://freecodecamp.org/news/javascript-callback-function-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/freeCodeCamp-Cover-4.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
seo_title: Fonction de Rappel JavaScript – Expliquée en Anglais Simple
seo_desc: "Every JavaScript beginner will face this question at least once: \"What\
  \ is a callback function?\" \nWell, we can find the answer in the word callback\
  \ itself. It's all about notifying the caller after the successful completion or\
  \ failure of a task. \nIn t..."
---

Chaque débutant en JavaScript sera confronté à cette question au moins une fois : "Qu'est-ce qu'une fonction de rappel ?"

Eh bien, nous pouvons trouver la réponse dans le mot **rappel** lui-même. Il s'agit de notifier l'appelant après l'achèvement réussi ou l'échec d'une tâche.

Dans cet article, je me concentrerai moins sur les aspects techniques des rappels et essayerai d'expliquer comment ils fonctionnent en langage naturel. Cela devrait vous aider à comprendre ce qu'est une `fonction de rappel` et pourquoi elle existe.

Si vous êtes un débutant en JavaScript, alors cet article est définitivement pour vous.

Si vous aimez aussi apprendre à partir de contenu vidéo, cet article est également disponible sous forme de tutoriel vidéo ici : 👈

%[https://www.youtube.com/watch?v=AUCavCH7FTw]

# D'abord, qu'est-ce qu'une fonction ?

Une fonction en JavaScript est un ensemble d'instructions qui effectue une tâche. Cet ensemble d'instructions peut exister sans une fonction, mais les avoir dans une fonction nous aide à réutiliser la tâche à plusieurs endroits.

Voici un exemple de fonction qui double une valeur si la valeur est un nombre pair. Nous passons un nombre comme argument à la fonction. Les instructions à l'intérieur de la fonction vérifient si l'argument est un nombre pair. Si c'est le cas, il le double et retourne le résultat. Sinon, il retourne le nombre original.

```js
function doubleEven(n) {
    if (n % 2 === 0) {
    	return n * 2;
    }
    return n;
}

```

Maintenant, vous pouvez utiliser cette fonction dans autant d'endroits que vous en avez besoin :

```js
doubleEven(10); // Résultat, 20
doubleEven(5); // Résultat, 5
```

## Vous pouvez passer une fonction comme argument à une autre fonction

Dans l'exemple ci-dessus, nous avons vu que vous pouvez passer un nombre comme argument à une fonction. De même, vous pouvez passer une fonction comme argument aussi. Vérifiez ceci :

```js
/** 
Créons une fonction foo qui prend une
fonction comme argument. Ici, nous invoquons 
la fonction bar passée à l'intérieur du corps de foo.
*/
function foo(bar) {
    bar();
}


```

D'accord, alors comment invoquons-nous foo maintenant ?

```js
/**
Invoquez foo en passant une fonction comme argument.
*/
foo(function() {
    console.log('bar');
}); // Résultat, bar
```

Remarquez que nous avons passé la définition entière de la fonction comme argument à `foo`. La fonction passée n'a pas de nom. Elle est appelée une `fonction anonyme`.

# Qu'est-ce qu'une Fonction de Rappel ?

La capacité d'une fonction JavaScript à accepter une autre fonction comme argument est un aspect puissant du langage.

Un appelant de la fonction peut passer une autre fonction comme argument à exécuter en fonction de n'importe quel déclencheur. Comprenons-le avec l'histoire de `Robin et PizzaHub`.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/pizza.png)
_Robin et l'Histoire de PizzaHub_

Robin, un petit garçon du Pays des Merveilles, adore manger de la pizza. Un matin, il prend le téléphone de sa mère et commande une pizza en utilisant l'application PizzaHub. Robin sélectionne sa pizza barbecue au fromage préférée et appuie sur le bouton de commande.

L'application PizzaHub enregistre la commande et informe Robin qu'elle le `notifiera` lorsque la pizza sera prête et en route. Robin, le garçon heureux, attend un moment et reçoit enfin une `notification` confirmant que la pizza est en route !

Donc, si nous décomposons l'histoire, la séquence des événements se déroule comme suit :

* Robin `commande` la pizza
* L'application `note` la commande
* PizzaHub `prépare` la pizza, et elle est prête après un moment.
* L'application `notifie` Robin, confirmant que la pizza est en route.

Le mécanisme de notification de Robin concernant la pizza fonctionne en utilisant la fonction de `rappel`.

## Écrivons l'histoire avec un langage de programmation

Oui, faisons-le. La séquence d'événements ci-dessus est un ensemble d'instructions que nous pouvons mettre logiquement dans des fonctions.

D'abord, Robin commande la pizza. L'application enregistre la commande en invoquant une fonction, comme ceci :

```js
orderPizza('Veg', 'Cheese Barbeque');
```

Maintenant, la fonction `orderPizza()` vivant quelque part sur le serveur PizzaHub peut effectuer certaines de ces actions (elle peut en fait faire beaucoup plus que cela, mais gardons cela simple) :

```js
function orderPizza(type, name) {
    console.log('Pizza commandée...');
    console.log('Pizza est pour la préparation');
    setTimeout(function () {
        let msg = `Votre pizza ${type} ${name} est prête ! La facture totale est de 13 $`;
        console.log(`Sur le serveur Pizzahub ${msg}`);
    }, 3000);
}
```

La fonction `setTimeout` démontre que la préparation de la pizza prend un certain temps. Nous enregistrons un message dans la console après que la pizza soit prête. Cependant, il y a un problème !

Le message est enregistré du côté `PizzaHub` et le pauvre Robin n'a aucune idée à ce sujet. Nous devons le `notifier` en lui disant que la pizza est prête.

## Introduction d'une fonction de rappel

Nous devons maintenant introduire une fonction de rappel pour informer Robin de l'état de la pizza. Changeons la fonction `orderPizza` pour passer une fonction de rappel comme argument. Remarquez également que nous appelons la fonction `callback` avec le message lorsque la pizza est prête :

```js
function orderPizza(type, name, callback) {
    console.log('Pizza commandée...');
    console.log('Pizza est pour la préparation');
    setTimeout(function () {
        let msg = `Votre pizza ${type} ${name} est prête ! La facture totale est de 13 $`;
        callback(msg);
    }, 3000);
}
```

Maintenant, apportons des modifications à l'invocation de la fonction `orderPizza` :

```js
orderPizza('Veg', 'Cheese Barbeque', function(message){
	console.log(message);
});
```

Ainsi, l'appelant sera maintenant notifié en utilisant la fonction de rappel une fois que la pizza sera prête. N'est-ce pas si utile ?

# En Résumé

Pour résumer :

* Une fonction JavaScript peut accepter une autre fonction comme argument.
* Passer la fonction comme argument est un concept de programmation puissant qui peut être utilisé pour notifier un appelant qu'un événement s'est produit. Il est également connu sous le nom de fonction de rappel.
* Vous pouvez utiliser des fonctions de rappel pour notifier l'appelant en fonction d'un cas d'utilisation. Les rappels sont également utilisés pour effectuer certaines tâches en fonction de l'état (réussite, échec) d'autres tâches.
* Mais soyez prudent – imbriquer trop de fonctions de rappel peut ne pas être une bonne idée et peut créer un `Enfer de Rappels`. Nous en apprendrons plus à ce sujet dans un prochain article.

Merci d'avoir lu ! Vous pouvez en apprendre plus à partir de ce dépôt open source sur la programmation asynchrone. N'oubliez pas d'essayer les quiz.

%[https://github.com/atapas/promise-interview-ready]

# Avant de Terminer...

C'est tout pour l'instant. J'espère que vous avez trouvé cet article perspicace et informatif.

Restons en contact. Vous pouvez me suivre sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary), sur ma [chaîne YouTube](https://youtube.com/c/TapasAdhikary?sub_confirmation=1), et [GitHub (atapas)](https://github.com/atapas).

Êtes-vous intéressé à en apprendre plus sur les concepts asynchrones de JavaScript ? Voici quelques liens pour vous aider :

* [JavaScript Synchrone vs Asynchrone – Pile d'Appels, Promesses, et Plus](https://www.freecodecamp.org/news/synchronous-vs-asynchronous-in-javascript/)
* [Une série d'articles sur les Promesses JavaScript & Async/Await](https://blog.greenroots.info/series/javascript-promises)
* [Une série vidéo sur la programmation asynchrone en JavaScript](https://www.youtube.com/watch?v=pIjfzjsoVw4&list=PLIJrr73KDmRyCanrlIS8PEOF0kPKgI8jN)