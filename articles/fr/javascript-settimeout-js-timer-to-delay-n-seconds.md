---
title: JavaScript setTimeout() – Minuterie JS pour retarder de N secondes
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-26T23:57:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-settimeout-js-timer-to-delay-n-seconds
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/erik-mclean-7lyRKyKIdJY-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript setTimeout() – Minuterie JS pour retarder de N secondes
seo_desc: "Have you ever wondered if there is a method to delay your JavaScript code\
  \ by a few seconds? \nIn this article, I will explain what the setTimeout() method\
  \ is with code examples and how it differs from setInterval(). \nWhat is setTimeout()\
  \ in JavaScript..."
---

Vous êtes-vous déjà demandé s'il existait une méthode pour retarder votre code JavaScript de quelques secondes ?

Dans cet article, je vais expliquer ce qu'est la méthode `setTimeout()` avec des exemples de code et comment elle diffère de `setInterval()`.

## Qu'est-ce que `setTimeout()` en JavaScript ?

`setTimeout()` est une méthode qui exécutera un morceau de code après que le minuteur ait fini de s'exécuter.

Voici la syntaxe pour la méthode `setTimeout()`.

```js
let timeoutID = setTimeout(function, delay in milliseconds, argument1, argument2,...);
```

Décomposons la syntaxe.

### Fonction

`setTimeout()` définira un minuteur et une fois que le minuteur sera écoulé, la fonction s'exécutera.

### Délai en millisecondes

À l'intérieur de cette méthode, vous pouvez spécifier combien de millisecondes vous souhaitez retarder la fonction. 1 000 millisecondes équivalent à 1 seconde.

Dans cet exemple, le message apparaîtra à l'écran après un délai de 3 secondes (3 000 millisecondes).

%[https://codepen.io/jessica-wilkins/pen/NWgqKKa?editors=0011]

```js
const para = document.getElementById("para");

function myMessage() {
  para.innerHTML = "Je viens d'apparaître";
  console.log("message apparu");
}
setTimeout(myMessage, 3000);
```

Si le délai n'est pas présent dans la méthode `setTimeout()`, il est alors défini à zéro et le message apparaîtra immédiatement.

%[https://codepen.io/jessica-wilkins/pen/eYRNOgX?editors=1111]

```js
const para = document.getElementById("para");

function myMessage() {
  para.innerHTML = "Aucun délai pour ce message";
  console.log("message apparu immédiatement");
}
setTimeout(myMessage);
```

### Arguments

Vous pouvez également avoir des arguments optionnels qui sont passés dans la fonction.

Dans cet exemple de conversation, Britney posera une question et la réponse d'Ashley sera retardée de 3 secondes. Elle inclura les deux arguments optionnels de la fonction `lunchMenu`.

%[https://codepen.io/jessica-wilkins/pen/YzQXzZa?editors=1010]

```js
const ashley = document.getElementById("ashley");

function lunchMenu(food1, food2) {
  ashley.innerHTML = `<strong>Ashley : </strong>J'ai mangé ${food1} et ${food2}.`;
}

setTimeout(lunchMenu, 3000, "pizza", "salade");
```

### timeoutID

`setTimeout()` retournera le `timeoutID` qui est un entier positif et un identifiant unique pour le minuteur.

### clearTimeout()

Cette méthode est utilisée pour annuler un `setTimeout()`. À l'intérieur de la méthode, vous devez référencer le `timeoutID`.

Voici la syntaxe de base.

```js
clearTimeout(timeoutID)
```

Dans cet exemple, le message apparaîtra après un délai de 10 secondes (10 000 millisecondes). Mais si l'utilisateur clique sur le bouton `Arrêter le minuteur`, alors le `setTimeout()` sera annulé.

%[https://codepen.io/jessica-wilkins/pen/JjJdoWm]

```js
const timerMsg = document.getElementById("message1");
const stopBtn = document.getElementById("stop");

function timerMessage() {
  timerMsg.innerHTML = "Merci d'avoir attendu !";
}

let timeoutID = setTimeout(timerMessage, 10000);

stopBtn.addEventListener("click", () => {
  clearTimeout(timeoutID);
  timerMsg.innerHTML = "Le minuteur a été arrêté";
});
```

## Devriez-vous passer une chaîne de caractères au lieu d'une fonction pour setTimeout() ?

Il est considéré comme une mauvaise pratique et un risque pour la sécurité de passer une chaîne de caractères au lieu d'une fonction.

Évitez d'écrire `setTimeout()` comme ceci :

```js
setTimeout("console.log('Ne faites pas cela');", 1000);


```

Certains éditeurs de code vous avertiront et vous suggéreront d'utiliser une fonction à la place.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-26-at-3.32.04-AM.png)

Utilisez toujours une fonction au lieu d'une chaîne de caractères dans ce cas.

```js
setTimeout(function () {
  console.log("Faites cela à la place");
}, 1000);
```

Si vous souhaitez en savoir plus sur les risques de sécurité pour un eval implicite, veuillez lire à ce sujet dans la section des docs MDN sur [Never Use Eval](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval#never_use_eval!).

## Comment `setInterval()` diffère-t-il de `setTimeout()` ?

Contrairement à `setTimeout()` qui exécute une fonction une seule fois après un délai, `setInterval()` répétera une fonction toutes les X secondes. Si vous souhaitez arrêter `setInterval()`, alors vous utilisez `clearInterval()`.

La syntaxe pour `setInterval()` est la même que pour `setTimeout()`.

```js
let intervalID = setInterval(function, delay in milliseconds, argument1, argument2,...);
```

Dans cet exemple, nous avons un message de vente qui est imprimé à l'écran chaque seconde.

%[https://codepen.io/jessica-wilkins/pen/wveaaYX]

```js
let intervalID = setInterval(() => {
  salesMsg.innerHTML += "<p>La vente se termine bientôt. ACHETEZ MAINTENANT !</p>";
}, 1000);
```

À l'intérieur de la méthode `setTimeout()`, nous utilisons `clearInterval()` pour arrêter d'imprimer le message après 10 secondes.

```js
setTimeout(() => {
  clearInterval(intervalID);
}, 10000);
```

Tout comme avec `setTimeout()`, vous devez utiliser l'identifiant unique pour le minuteur à l'intérieur de la méthode `clearInterval()`.

## Exemples de projets réels

Maintenant que nous comprenons comment `setTimeout()` et `setInterval()` fonctionnent, examinons un exemple de la façon dont cela peut s'appliquer à une fonctionnalité réelle sur un site web.

%[https://codepen.io/jessica-wilkins/pen/yLXNojz?editors=0011]

Dans cet exemple, nous avons une barre de progression qui démarrera 2 secondes après le chargement de la page. À l'intérieur du `setTimeout()`, nous avons un `setInterval()` qui exécutera la fonction `animate()` tant que la largeur de la barre n'est pas de 100 %.

```js
setTimeout(() => {
  let intervalID = setInterval(() => {
    if (barWidth === 100) {
      clearInterval(intervalID);
    } else {
      animate();
    }
  }, 100);//cela définit la vitesse de l'animation
}, 2000);
```

À l'intérieur de la fonction `animate()`, nous avons un autre `setTimeout()` qui affichera 100 % Complété lorsque la barre de progression sera pleine.

```js
const animate = () => {
  barWidth++;
  progressBar.style.width = `${barWidth}%`;
  setTimeout(() => {
    loadingMsg.innerHTML = `${barWidth}% Complété`;
  }, 10100);
};
```

Une barre de progression n'est qu'une des nombreuses animations que vous pouvez créer avec `setTimeout()` et `setInterval()`. Vous pouvez également utiliser ces méthodes lors de la création de jeux en ligne.

Dans [How to Build A Simon Game](https://www.youtube.com/watch?v=n_ec3eowFLQ) de Beau Carnes, vous pouvez voir comment `setTimeout()` et `setInterval()` sont utilisés dans la logique du jeu.

## Conclusion

`setTimeout()` est une méthode qui exécutera un morceau de code après que le minuteur ait fini de s'exécuter.

```js
let timeoutID = setTimeout(function, delay in milliseconds, argument1, argument2,...);
```

Le délai est défini en millisecondes et 1 000 millisecondes équivalent à 1 seconde.

Si le délai est omis dans la méthode `setTimeout()`, alors le délai est défini à 0 et la fonction s'exécutera.

Vous pouvez également avoir des arguments optionnels qui sont passés dans la fonction.

`setTimeout()` retournera le `timeoutID` qui est un entier positif et un identifiant unique pour le minuteur.

Il est important de ne pas utiliser une chaîne de caractères à la place de la fonction pour des raisons de sécurité.

```js
setTimeout("console.log('Ne faites pas cela');", 1000);
```

Si vous souhaitez annuler `setTimeout()`, vous devez utiliser `clearTimeout()`

```js
clearTimeout(timeoutID)
```

Si vous souhaitez exécuter un morceau de code de manière répétée pendant un certain nombre de secondes, vous utiliseriez alors `setInterval()`.

```js
let intervalID = setInterval(() => {
 // ce code s'exécute chaque seconde
}, 1000);
```

`setTimeout()` peut être utilisé pour créer des animations JavaScript basiques et des jeux en ligne.

J'espère que vous avez apprécié cet article sur `setTimeout()`.