---
title: Fonctions de rappel JavaScript – Qu'est-ce que les Callbacks en JS et comment
  les utiliser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-17T16:18:05.000Z'
originalURL: https://freecodecamp.org/news/javascript-callback-functions-what-are-callbacks-in-js-and-how-to-use-them
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/caspar-camille-rubin-7SDoly3FV_0-unsplash.jpg
tags:
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
seo_title: Fonctions de rappel JavaScript – Qu'est-ce que les Callbacks en JS et comment
  les utiliser
seo_desc: 'By Cem Eygi

  If you’re familiar with programming, you already know what functions do and how
  to use them. But what is a callback function? Callback functions are an important
  part of JavaScript and once you understand how callbacks work, you’ll become...'
---

Par Cem Eygi

Si vous êtes familier avec la programmation, vous savez déjà ce que font les fonctions et comment les utiliser. Mais qu'est-ce qu'une fonction de rappel ? Les fonctions de rappel sont une partie importante de JavaScript et une fois que vous comprendrez comment fonctionnent les callbacks, vous deviendrez beaucoup meilleur en JavaScript.

Donc dans cet article, j'aimerais vous aider à comprendre ce que sont les fonctions de rappel et comment les utiliser en JavaScript en passant par quelques exemples.

## Qu'est-ce qu'une fonction de rappel ?

En JavaScript, les fonctions sont des objets. Peut-on passer des objets à des fonctions en tant que paramètres ? Oui.

Ainsi, nous pouvons également passer des fonctions en tant que paramètres à d'autres fonctions et les appeler à l'intérieur des fonctions externes. Cela semble compliqué ? Laissez-moi vous montrer cela dans un exemple ci-dessous :

```javascript
function print(callback) {  
    callback();
}
```

La fonction print() prend une autre fonction en tant que paramètre et l'appelle à l'intérieur. Cela est valide en JavaScript et nous l'appelons un "callback". Donc une fonction qui est passée à une autre fonction en tant que paramètre est une fonction de rappel. Mais ce n'est pas tout.

**Vous pouvez également regarder la version vidéo des fonctions de rappel ci-dessous :**

%[https://youtu.be/qtfi4-8dj9c]

### Pourquoi avons-nous besoin des fonctions de rappel ?

JavaScript exécute le code séquentiellement dans l'ordre de haut en bas. Cependant, il y a des cas où le code s'exécute (ou doit s'exécuter) après qu'autre chose se produise et aussi de manière non séquentielle. Cela s'appelle la programmation asynchrone.

Les callbacks s'assurent qu'une fonction ne va pas s'exécuter avant qu'une tâche soit terminée, mais s'exécutera juste après que la tâche soit terminée. Cela nous aide à développer du code JavaScript asynchrone et nous protège des problèmes et des erreurs.

En JavaScript, la manière de créer une fonction de rappel est de la passer en tant que paramètre à une autre fonction, puis de l'appeler juste après qu'un événement s'est produit ou qu'une tâche est terminée. Voyons comment...

## Comment créer un Callback

Pour comprendre ce que j'ai expliqué ci-dessus, laissez-moi commencer par un exemple simple. Nous voulons enregistrer un message dans la console, mais il doit y être après 3 secondes.

```javascript
const message = function() {  
    console.log("Ce message est affiché après 3 secondes");
}
 
setTimeout(message, 3000);
```

Il existe une méthode intégrée en JavaScript appelée "setTimeout", qui appelle une fonction ou évalue une expression après une période de temps donnée (en millisecondes). Donc ici, la fonction "message" est appelée après que 3 secondes se soient écoulées. (1 seconde = 1000 millisecondes)

En d'autres termes, la fonction message est appelée après qu'un événement s'est produit (après que 3 secondes se soient écoulées pour cet exemple), mais pas avant. Donc la fonction message est un exemple de fonction de rappel.

### Qu'est-ce qu'une fonction anonyme ?

Alternativement, nous pouvons définir une fonction directement à l'intérieur d'une autre fonction, au lieu de l'appeler. Cela ressemblera à ceci :

```javascript
setTimeout(function() {  
    console.log("Ce message est affiché après 3 secondes");
}, 3000);
```

Comme nous pouvons le voir, la fonction de rappel ici n'a pas de nom et une définition de fonction sans nom en JavaScript est appelée une "fonction anonyme". Cela fait exactement la même tâche que l'exemple ci-dessus.

### Callback en tant que fonction fléchée

Si vous préférez, vous pouvez également écrire la même fonction de rappel en tant que fonction fléchée ES6, qui est un type de fonction plus récent en JavaScript :

```javascript
setTimeout(() => { 
    console.log("Ce message est affiché après 3 secondes");
}, 3000);
```

## Qu'en est-il des événements ?

JavaScript est un langage de programmation piloté par les événements. Nous utilisons également des fonctions de rappel pour les déclarations d'événements. Par exemple, supposons que nous voulons que les utilisateurs cliquent sur un bouton :

```html
<button id="callback-btn">Cliquez ici</button>
```

Cette fois, nous verrons un message dans la console uniquement lorsque l'utilisateur cliquera sur le bouton :

```javascript
document.querySelector("#callback-btn")
    .addEventListener("click", function() {    
      console.log("L'utilisateur a cliqué sur le bouton !");
});
```

Ici, nous sélectionnons d'abord le bouton avec son id, puis nous ajoutons un écouteur d'événement avec la méthode addEventListener. Elle prend 2 paramètres. Le premier est son type, "click", et le second paramètre est une fonction de rappel, qui enregistre le message lorsque le bouton est cliqué.

Comme vous pouvez le voir, les fonctions de rappel sont également utilisées pour les déclarations d'événements en JavaScript.

## Conclusion

Les callbacks sont souvent utilisés en JavaScript, et j'espère que cet article vous aide à comprendre ce qu'ils font réellement et comment travailler avec eux plus facilement. Ensuite, vous pouvez apprendre les [Promesses JavaScript](https://www.freecodecamp.org/news/javascript-es6-promises-for-beginners-resolve-reject-and-chaining-explained/), un sujet similaire que j'ai expliqué dans mon nouvel article.

**Si vous souhaitez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)** !**

Merci d'avoir lu !