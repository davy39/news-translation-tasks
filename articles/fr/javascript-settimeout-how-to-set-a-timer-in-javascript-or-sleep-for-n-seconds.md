---
title: JavaScript setTimeout() – Comment définir un minuteur en JavaScript ou mettre
  en pause pendant N secondes
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-04-27T17:45:49.000Z'
originalURL: https://freecodecamp.org/news/javascript-settimeout-how-to-set-a-timer-in-javascript-or-sleep-for-n-seconds
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/set-timeout.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript setTimeout() – Comment définir un minuteur en JavaScript ou
  mettre en pause pendant N secondes
seo_desc: 'This tutorial will help you to understand how the built-in JavaScript method  setTimeout()
  works with intuitive code examples.

  How to Use setTimeout() in JavaScript

  The setTimeout() method allows you to execute a piece of code after a certain amount
  ...'
---

Ce tutoriel vous aidera à comprendre comment fonctionne la méthode intégrée de JavaScript `setTimeout()` avec des exemples de code intuitifs.

## Comment utiliser setTimeout() en JavaScript

La méthode `setTimeout()` vous permet d'exécuter un morceau de code après qu'un certain laps de temps s'est écoulé. Vous pouvez considérer cette méthode comme un moyen de régler un minuteur pour exécuter du code JavaScript à un moment précis.

Par exemple, le code ci-dessous affichera "Hello World" dans la console JavaScript après 2 secondes :

```js
setTimeout(function(){
    console.log("Hello World");
}, 2000);

console.log("setTimeout() example...");
```

Le code ci-dessus affichera d'abord "setTimeout() example..." dans la console, puis affichera "Hello World" une fois que deux secondes se seront écoulées depuis l'exécution du code par JavaScript.

La syntaxe de la méthode `setTimeout()` est la suivante :

```js
setTimeout(function, milliseconds, parameter1, parameter2, ...);
```

Le premier paramètre de la méthode `setTimeout()` est une `function` JavaScript que vous souhaitez exécuter. Vous pouvez écrire la `function` directement lors de son passage, ou vous pouvez également faire référence à une fonction nommée comme indiqué ci-dessous :

```js
function greeting(){
  console.log("Hello World");
}

setTimeout(greeting);
```

Ensuite, vous pouvez passer le paramètre `milliseconds`, qui sera la durée pendant laquelle JavaScript attendra avant d'exécuter le code. 

Une seconde est égale à mille millisecondes, donc si vous voulez attendre 3 secondes, vous devez passer `3000` comme deuxième argument :

```js
function greeting(){
  console.log("Hello World");
}

setTimeout(greeting, 3000);
```

Si vous omettez le deuxième paramètre, alors `setTimeout()` exécutera immédiatement la `function` transmise sans attendre du tout.

Enfin, vous pouvez également passer des paramètres supplémentaires à la méthode `setTimeout()` que vous pouvez utiliser à l'intérieur de la `function` comme suit :

```js
function greeting(name, role){
  console.log(`Hello, my name is ${name}`);
  console.log(`I'm a ${role}`);
}

setTimeout(greeting, 3000, "Nathan", "Software developer");
```

Maintenant, vous vous demandez peut-être : "pourquoi ne pas simplement passer les paramètres directement à la fonction ?"

C'est parce que si vous passez les paramètres directement comme ceci :

```js
setTimeout(greeting("Nathan", "Software developer"), 3000);
```

Alors JavaScript exécutera immédiatement la `function` sans attendre, car vous passez un _appel de fonction_ (function call) et non une _référence de fonction_ (function reference) comme premier paramètre. 

C'est pourquoi si vous devez passer des paramètres à la fonction, vous devez les passer via la méthode `setTimeout()`.

Mais honnêtement, je n'ai jamais eu besoin de passer des paramètres supplémentaires à la méthode `setTimeout()` dans mon rôle de développeur logiciel, alors ne vous en faites pas 😉

## Comment annuler la méthode setTimeout

Vous pouvez également empêcher la méthode `setTimeout()` d'exécuter la `function` en utilisant la méthode `clearTimeout()`.

La méthode `clearTimeout()` nécessite l' `id` renvoyé par `setTimeout()` pour savoir quelle méthode `setTimeout()` annuler :

```js
clearTimeout(id);
```

Voici un exemple de la méthode `clearTimeout()` en action :

```js
const timeoutId = setTimeout(function(){
    console.log("Hello World");
}, 2000);

clearTimeout(timeoutId);
console.log(`Timeout ID ${timeoutId} has been cleared`);
```

Si vous avez plusieurs méthodes `setTimeout()`, vous devez alors enregistrer les ID renvoyés par chaque appel de méthode, puis appeler la méthode `clearTimeout()` autant de fois que nécessaire pour les effacer tous.

## Conclusion

La méthode JavaScript `setTimeout()` est une méthode intégrée qui vous permet de planifier l'exécution d'une certaine `function`. Vous devez passer la durée d'attente en `milliseconds`, ce qui signifie que pour attendre une seconde, vous devez passer mille `milliseconds`.

Pour annuler l'exécution d'une méthode `setTimeout()`, vous devez utiliser la méthode `clearTimeout()`, en passant la valeur de l'ID renvoyée lors de l'appel de la méthode `setTimeout()`.

## **Merci d'avoir lu ce tutoriel**

Si vous avez apprécié cet article et que vous souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre le JavaScript. Il propose un guide étape par étape qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous aurez vraiment l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !

##