---
title: Debounce Expliqué – Comment Faire Attendre JavaScript Que Votre Utilisateur
  Ait Fini de Taper
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-07T20:31:24.000Z'
originalURL: https://freecodecamp.org/news/debounce-explained-how-to-make-your-javascript-wait-for-your-user-to-finish-typing-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/pexels-photo.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Debounce Expliqué – Comment Faire Attendre JavaScript Que Votre Utilisateur
  Ait Fini de Taper
seo_desc: 'By Cristian Vega

  Debounce functions in JavaScript are higher-order functions that limit the rate
  at which another function gets called.


  A higher-order function is a function that either takes a function as an argument
  or returns a function as part o...'
---

Par Cristian Vega

Les fonctions Debounce en JavaScript sont des fonctions d'ordre supérieur qui limitent le taux auquel une autre fonction est appelée.

> Une fonction d'ordre supérieur est une fonction qui prend une fonction comme argument ou retourne une fonction dans le cadre de son instruction de retour. Notre fonction debounce fait les deux.

Le cas d'utilisation le plus courant pour un debounce est de le passer comme argument à un écouteur d'événement attaché à un élément HTML. Pour mieux comprendre à quoi cela ressemble et pourquoi c'est utile, examinons un exemple.

Supposons que vous avez une fonction nommée `myFunc` qui est appelée chaque fois que vous tapez quelque chose dans un champ de saisie. Après avoir passé en revue les exigences de votre projet, vous décidez que vous voulez changer l'expérience.

Au lieu de cela, vous voulez que `myFunc` s'exécute lorsque au moins 2 secondes se sont écoulées depuis la dernière fois que vous avez tapé quelque chose.

C'est là qu'un debounce entre en jeu. Au lieu de passer `myFunc` à l'écouteur d'événement, vous passeriez le debounce. Le debounce lui-même prendrait alors `myFunc` comme argument, ainsi que le nombre 2000.

Maintenant, chaque fois que vous cliquez sur le bouton, `myFunc` ne s'exécutera que si au moins 2 secondes se sont écoulées avant la dernière fois que `myFunc` a été appelée.

## Comment implémenter une fonction debounce

De début à fin, il ne faut que 7 lignes de code pour implémenter une fonction debounce. Le reste de cette section se concentre sur ces 7 lignes de code afin que nous puissions voir comment notre fonction debounce fonctionne en interne.

```javascript
function debounce( callback, delay ) {
    let timeout;
    return function() {
        clearTimeout( timeout );
        timeout = setTimeout( callback, delay );
    }
}
```

En commençant par la ligne 1, nous avons déclaré une nouvelle fonction nommée `debounce`. Cette nouvelle fonction a deux paramètres, `callback` et `delay`.

```javascript
function debounce( callback, delay ) {

}

```

`callback` est toute fonction qui doit limiter le nombre de fois qu'elle s'exécute.

`delay` est le temps (en millisecondes) qui doit s'écouler avant que `callback` puisse s'exécuter à nouveau.

```javascript
function debounce( callback, delay ) {
    let timeout;
}
```

À la ligne 2, nous déclarons une variable non initialisée nommée `timeout`.
Cette nouvelle variable contient le `timeoutID` retourné lorsque nous appelons `setTimeout` plus tard dans notre fonction `debounce`.

```javascript
function debounce( callback, delay ) {
    let timeout;
    return function() {
    }
}
```

À la ligne 3, nous retournons une fonction anonyme. Cette fonction anonyme fermera la variable `timeout` afin que nous puissions y accéder même après que l'appel initial à `debounce` ait fini de s'exécuter.

> Une fermeture en JavaScript se produit chaque fois qu'une fonction interne conserve l'accès à la portée lexicale de sa fonction externe, même si la fonction externe a fini de s'exécuter. Si vous voulez en savoir plus sur les fermetures, vous pouvez lire [le chapitre 7 de « You Don’t Know JS »](https://github.com/getify/You-Dont-Know-JS/blob/2nd-ed/scope-closures/ch7.md) par Kyle Simpson

```javascript
function debounce( callback, delay ) {
    let timeout;
    return function() {
        clearTimeout( timeout );
    }
}
```

À la ligne 4, nous appelons la méthode `clearTimeout` du mixin `WindowOrWorkerGlobalScope`. Cela garantira que chaque fois que nous appelons notre fonction `debounce`, `timeout` est réinitialisé et le compteur peut redémarrer.

Le mixin `WindowOrWorkerGlobalScope` de JavaScript nous donne accès à quelques méthodes bien connues, comme `setTimeout`, `clearTimeout`, `setInterval`, `clearInterval` et `fetch`.

Vous pouvez en savoir plus à ce sujet en [lisant cet article](https://www.freecodecamp.org/news/an-introduction-to-scope-in-javascript-cbd957022652/).

```javascript
function debounce( callback, delay ) {
    let timeout;
    return function() {
        clearTimeout( timeout );
        timeout = setTimeout( callback, delay );
    }
}
```

À la ligne 5, nous avons atteint la fin de notre implémentation de la fonction `debounce`.

Cette ligne de code fait quelques choses. La première action consiste à attribuer une valeur à la variable `timeout` que nous avons déclarée à la ligne 2. La valeur est un `timeoutID` qui est retourné lorsque nous appelons `setTimeout`. Cela nous permettra de référencer le timeout créé par l'appel à `setTimeout` afin que nous puissions le réinitialiser chaque fois que notre fonction `debounce` est utilisée.

La deuxième action effectuée est l'appel à `setTimeout`. Cela créera un timeout qui exécutera `callback` (l'argument de fonction passé à notre fonction `debounce`) une fois que `delay` (l'argument numérique passé à notre fonction `debounce`) s'est écoulé.

Puisque nous utilisons un timeout, `callback` ne s'exécutera que si nous permettons au timeout d'atteindre 0. C'est là que réside le cœur de notre fonction `debounce`, car nous réinitialisons le timeout chaque fois que `debounce` est appelé. C'est ce qui nous permet de limiter le taux d'exécution de `myFunc`.

Les lignes 5 et 6 ne contiennent que des accolades, nous ne les passerons donc pas en revue.

C'est tout. C'est ainsi que notre fonction `debounce` fonctionne en interne. Maintenant, ajoutons à notre exemple précédent du début. Nous allons créer un champ de saisie et y attacher un écouteur d'événement avec notre fonction `debounce` comme l'un de ses arguments.

## Exemple concret

Tout d'abord, nous devons créer un champ de saisie.

```html
<label for="myInput">Tapez quelque chose !</label>
<input id="myInput" type="text">
```

Ensuite, nous devons créer une fonction que nous voulons exécuter chaque fois que nous tapons quelque chose dans notre champ de saisie.

```javascript
function helloWorld() {
    console.log("Hello World!")
}
```

Enfin, nous devons sélectionner le champ de saisie que nous avons créé ci-dessus et y attacher un écouteur d'événement `keyup`.

```javascript
const myInput = document.getElementById("myInput");

myInput.addEventListener(
    "keyup",
    debounce( helloWorld, 2000 )
);
```

Cela conclut notre exemple concret ! Chaque fois que nous tapons quelque chose dans notre champ de saisie, `helloWorld` s'exécutera si au moins 2 secondes se sont écoulées depuis la dernière fois que nous avons tapé quelque chose.

> Un remerciement spécial à l'utilisateur Reddit **stratoscope** pour avoir aidé à corriger une partie du code initial de cet article. [Voici une démonstration fonctionnelle](https://repl.it/@geary/JsDebounce#script.js) qu'il a créée de cette fonction `debounce` sur Repl.it.

## Notes de clôture

Les fonctions Debounce sont simples, mais puissantes, et peuvent avoir un impact notable sur la plupart des applications JavaScript.

Bien que notre exemple ait été amusant et simple, de nombreuses grandes organisations utilisent des fonctions debounce pour augmenter les performances de leurs applications.

Si vous voulez en savoir plus sur JavaScript, consultez mon site web ! Je travaille sur des choses intéressantes à [https://juanmvega.com](https://juanmvega.com).