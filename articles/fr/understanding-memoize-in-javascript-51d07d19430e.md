---
title: Comment utiliser Memoize pour mettre en cache les résultats de fonction JavaScript
  et accélérer votre code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-29T05:53:11.000Z'
originalURL: https://freecodecamp.org/news/understanding-memoize-in-javascript-51d07d19430e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UPyVG04cujAGglMNgF1bTA.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment utiliser Memoize pour mettre en cache les résultats de fonction
  JavaScript et accélérer votre code
seo_desc: 'By Divyanshu Maithani

  Functions are an integral part of programming. They help add modularity and reusability
  to our code.

  It’s quite common to divide our program into chunks using functions which we can
  call later to perform some useful action.

  Some...'
---

Par Divyanshu Maithani

Les fonctions sont une partie intégrante de la programmation. Elles aident à ajouter de la **modularité** et de la **réutilisabilité** à notre code.

Il est assez courant de diviser notre programme en morceaux en utilisant des fonctions que nous pouvons appeler plus tard pour effectuer une action utile.

Parfois, une fonction peut devenir coûteuse à appeler plusieurs fois (par exemple, une fonction pour calculer la [factorial](https://en.wikipedia.org/wiki/Factorial) d'un nombre). Mais il existe un moyen d'optimiser de telles fonctions et de les faire s'exécuter beaucoup plus rapidement : la **mise en cache**.

Par exemple, supposons que nous avons une `fonction` pour retourner la factorielle d'un nombre :

```js
function factorial(n) {
    // Calculs : n * (n-1) * (n-2) * ... (2) * (1)
    return factorial
}
```

Super, maintenant trouvons `factorial(50)`. L'ordinateur effectuera les calculs et nous retournera la réponse finale, génial !

Lorsque cela est fait, trouvons `factorial(51)`. L'ordinateur effectue à nouveau un certain nombre de calculs et nous obtient le résultat, mais vous avez peut-être remarqué que nous répétons déjà un certain nombre d'étapes qui auraient pu être évitées. Une manière optimisée serait :

```
factorial(51) = factorial(50) * 51
```

Mais notre `fonction` effectue les calculs à partir de zéro à chaque fois qu'elle est appelée :

```
factorial(51) = 51 * 50 * 49 * ... * 2 * 1
```

Ne serait-ce pas cool si d'une manière ou d'une autre notre fonction `factorial` pouvait se souvenir des valeurs de ses calculs précédents et les utiliser pour accélérer l'exécution ?

Voici la **mémoïsation**, une manière pour notre `fonction` de se souvenir (mettre en cache) des résultats. Maintenant que vous avez une compréhension de base de ce que nous essayons d'atteindre, voici une définition formelle :

> [**Memoization**](https://en.wikipedia.org/wiki/Memoization) est une technique d'optimisation utilisée principalement pour accélérer les programmes informatiques en **stockant les résultats d'appels de fonctions coûteux** et en retournant le résultat mis en cache lorsque les mêmes entrées se produisent à nouveau

**Mémoïser** en termes simples signifie **mémoriser** ou stocker en mémoire. Une fonction mémoïsée est généralement plus rapide car si la fonction est appelée ultérieurement avec la ou les valeurs précédentes, alors au lieu d'exécuter la fonction, nous récupérerons le résultat du cache.

Voici à quoi pourrait ressembler une simple fonction mémoïsée _(et voici un [CodePen](https://codepen.io/divyanshu013/pen/xdQPvp?editors=0011) au cas où vous voudriez interagir avec)_ :

```js
// une simple fonction pour ajouter quelque chose
const add = (n) => (n + 10);
add(9);
// une simple fonction mémoïsée pour ajouter quelque chose
const memoizedAdd = () => {
  let cache = {};
  return (n) => {
    if (n in cache) {
      console.log('Récupération depuis le cache');
      return cache[n];
    }
    else {
      console.log('Calcul du résultat');
      let result = n + 10;
      cache[n] = result;
      return result;
    }
  }
}
// fonction retournée depuis memoizedAdd
const newAdd = memoizedAdd();
console.log(newAdd(9)); // calculé
console.log(newAdd(9)); // mis en cache
```

### Points clés de la mémoïsation

Quelques points clés du code ci-dessus sont :

* `memoizedAdd` retourne une `fonction` qui est invoquée plus tard. Cela est possible car en JavaScript, les fonctions sont des objets de première classe, ce qui nous permet de les utiliser comme des [fonctions d'ordre supérieur](http://eloquentjavascript.net/05_higher_order.html#h_xxCc98lOBK) et de retourner une autre fonction.
* `cache` peut se souvenir de ses _valeurs_ puisque la fonction retournée a une [fermeture](https://developer.mozilla.org/en/docs/Web/JavaScript/Closures) sur elle.
* Il est essentiel que la fonction mémoïsée soit [pure](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976). Une fonction pure retournera la même sortie pour une entrée particulière, peu importe le nombre de fois où elle est appelée, ce qui fait que le `cache` fonctionne comme prévu.

### Écrire votre propre fonction `memoize`

Le code précédent fonctionne bien, mais que faire si nous voulions transformer n'importe quelle fonction en une fonction mémoïsée ?

Voici comment écrire votre propre fonction memoize ([codepen](https://codepen.io/divyanshu013/pen/zwMPdK?editors=0011#code-area)) :

```
// une simple fonction pure pour obtenir une valeur en ajoutant 10
const add = (n) => (n + 10);
console.log('Appel simple', add(3));
// une simple fonction memoize qui prend une fonction
// et retourne une fonction mémoïsée
const memoize = (fn) => {
  let cache = {};
  return (...args) => {
    let n = args[0];  // prenant juste un argument ici
    if (n in cache) {
      console.log('Récupération depuis le cache');
      return cache[n];
    }
    else {
      console.log('Calcul du résultat');
      let result = fn(n);
      cache[n] = result;
      return result;
    }
  }
}
// création d'une fonction mémoïsée pour la fonction pure 'add'
const memoizedAdd = memoize(add);
console.log(memoizedAdd(3));  // calculé
console.log(memoizedAdd(3));  // mis en cache
console.log(memoizedAdd(4));  // calculé
console.log(memoizedAdd(4));  // mis en cache
```

Maintenant, c'est génial ! Cette simple fonction `memoize` enveloppera n'importe quelle fonction simple en une équivalente mémoïsée. Le code fonctionne bien pour les fonctions simples et il peut être facilement ajusté pour gérer n'importe quel nombre d'`arguments` selon vos besoins. Une autre alternative est d'utiliser certaines bibliothèques de facto telles que :

* `_.memoize(func, [resolver])` de [Lodash](https://lodash.com/docs/4.17.4#memoize)
* Décorateurs ES7 `@memoize` de [decko](https://github.com/developit/decko#memoize)

### Mémoïsation des fonctions récursives

Si vous essayez de passer une fonction récursive à la fonction `memoize` ci-dessus ou `_.memoize` de Lodash, les résultats ne seront pas ceux attendus puisque la fonction récursive, lors de ses appels ultérieurs, finira par s'appeler elle-même au lieu de la fonction mémoïsée, ne faisant ainsi aucun usage du `cache`.

Assurez-vous simplement que votre fonction récursive appelle la fonction mémoïsée. Voici comment vous pouvez ajuster un exemple de manuel de [factorial](https://en.wikipedia.org/wiki/Factorial) ([codepen](https://codepen.io/divyanshu013/pen/JNevOm)) :

```
// même fonction memoize que précédemment
const memoize = (fn) => {
  let cache = {};
  return (...args) => {
    let n = args[0];
    if (n in cache) {
      console.log('Récupération depuis le cache', n);
      return cache[n];
    }
    else {
      console.log('Calcul du résultat', n);
      let result = fn(n);
      cache[n] = result;
      return result;
    }
  }
}
const factorial = memoize(
  (x) => {
    if (x === 0) {
      return 1;
    }
    else {
      return x * factorial(x - 1);
    }
  }
);
console.log(factorial(5)); // calculé
console.log(factorial(6)); // calculé pour 6 et mis en cache pour 5
```

Quelques points à noter à partir de ce code :

* La fonction `factorial` appelle de manière récursive une version mémoïsée d'elle-même.
* La fonction mémoïsée met en cache les valeurs des factoriels précédents, ce qui améliore significativement les calculs puisqu'ils peuvent être réutilisés `factorial(6) = 6 * factorial(5)`

### La mémoïsation est-elle la même que la mise en cache ?

Oui, en quelque sorte. La mémoïsation est en fait un type spécifique de mise en cache. Alors que la mise en cache peut se référer en général à toute technique de stockage (comme la [mise en cache HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching)) pour une utilisation future, la mémoïsation implique spécifiquement la _mise en cache_ des valeurs de retour d'une `fonction`.

### Quand mémoïser vos fonctions

Bien qu'il puisse sembler que la mémoïsation puisse être utilisée avec toutes les fonctions, elle a en réalité des cas d'utilisation limités :

* Pour mémoïser une fonction, elle doit être pure afin que les valeurs de retour soient les mêmes pour les mêmes entrées à chaque fois
* La mémoïsation est un compromis entre l'espace ajouté et la vitesse ajoutée et n'est donc significative que pour les fonctions ayant une plage d'entrée limitée afin que les valeurs mises en cache puissent être utilisées plus fréquemment
* Il peut sembler que vous devriez mémoïser vos appels d'API, mais ce n'est pas nécessaire car le navigateur les met automatiquement en cache pour vous. Voir [HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) pour plus de détails
* Le meilleur cas d'utilisation que j'ai trouvé pour les fonctions mémoïsées est **pour les fonctions de calcul intensif** qui peuvent améliorer significativement les performances (factorial et fibonacci ne sont pas vraiment de bons exemples du monde réel)
* Si vous êtes dans React/Redux, vous pouvez consulter [reselect](https://github.com/reactjs/reselect#creating-a-memoized-selector) qui utilise un _sélecteur mémoïsé_ pour s'assurer que les calculs ne se produisent que lorsqu'un changement se produit dans une partie liée de l'arbre d'état.

#### Lectures complémentaires

Les liens suivants peuvent être utiles si vous souhaitez en savoir plus sur certains des sujets de cet article en détail :

* [Fonctions d'ordre supérieur](http://eloquentjavascript.net/05_higher_order.html#h_xxCc98lOBK) en JavaScript
* [Fermetures](https://developer.mozilla.org/en/docs/Web/JavaScript/Closures) en JavaScript
* [Fonctions pures](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976)
* Documentation de `_.memoize` de Lodash [docs](https://lodash.com/docs/4.17.4#memoize) et [code source](https://github.com/lodash/lodash/blob/4.17.4/lodash.js#L10554-L10572)
* Plus d'exemples de mémoïsation [ici](https://www.sitepoint.com/implementing-memoization-in-javascript/) et [ici](http://inlehmansterms.net/2015/03/01/javascript-memoization/)
* [reactjs/reselect](https://github.com/reactjs/reselect)

J'espère que cet article vous a été utile et que vous avez une meilleure compréhension de la mémoïsation en JavaScript :)

---

Vous pouvez me suivre sur [twitter](https://twitter.com/divyanshu013) pour les dernières mises à jour. J'ai également commencé à publier des articles plus récents sur mon blog personnel [blog](https://divyanshu013.dev/).