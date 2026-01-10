---
title: JavaScript Wait – Comment faire une pause de N secondes en JS avec .setTimeout()
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-04-26T19:14:41.000Z'
originalURL: https://freecodecamp.org/news/javascript-wait-how-to-sleep-n-seconds-in-js-with-settimeout
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/nikita-kachanovsky-OVbeSXRk_9E-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript Wait – Comment faire une pause de N secondes en JS avec .setTimeout()
seo_desc: "Sometimes you might want to delay the execution of your code. \nYou may\
  \ need certain lines of code to execute at a point in the future, when you explicitly\
  \ specify, rather than all the code executing synchronously.\nSomething like that\
  \ is possible with..."
---

Parfois, vous pouvez vouloir retarder l'exécution de votre code.

Vous pouvez avoir besoin que certaines lignes de code s'exécutent à un moment précis dans le futur, lorsque vous le spécifiez explicitement, plutôt que tout le code s'exécute de manière synchrone.

Cela est possible avec JavaScript.

Dans cet article, vous apprendrez la méthode `setTimeout()` – ce qu'elle est et comment vous pouvez l'utiliser dans vos programmes.

Voici ce que nous allons couvrir dans ce guide rapide :

1. [Qu'est-ce que `setTimeout()` en JavaScript](#introduction)
2. [Syntaxe de `setTimeout()` en JavaScript](#syntaxe)
3. [Comment attendre N secondes en JavaScript](#attendre)
    1. [Comment utiliser la méthode `clearTimeout()`](#effacer)
5. [`setTimeout` vs `setInterval` - Quelle est la différence ?](#difference)

## Qu'est-ce que `setTimeout()` en JavaScript ? <a name="introduction"></a>

Le rôle de `setTimeout()`, une méthode asynchrone de l'objet window, est de définir un minuteur qui exécutera une action. Ce minuteur indique un moment spécifique où il y aura un déclencheur pour cette action particulière.

Puisque `setTimeout()` fait partie de l'objet window, il peut également s'écrire `window.setTimeout()`. Cela dit, le préfixe `window` est implicite et donc généralement omis et non spécifié.

## La méthode `setTimeout()` - Aperçu de la syntaxe <a name="syntaxe"></a>

La syntaxe générale de la méthode `setTimeout()` ressemble à ceci :

```js
setTimeout(function_name, time);
```

Décomposons cela :

- `setTimeout()` est une méthode utilisée pour créer des événements temporisés.
- Elle accepte deux paramètres **requis**. 
- `function_name` est le premier paramètre requis. C'est le nom d'une fonction de rappel qui contient le code que vous souhaitez exécuter. Le nom de la fonction sert de référence et de pointeur vers la définition de la fonction qui contient le bloc de code réel.
- `time` est le deuxième paramètre requis, et il est défini en **millisecondes** (pour référence, `1 seconde = 1000 millisecondes`). Il représente la quantité de temps spécifiée que le programme doit attendre pour que la fonction soit exécutée.

Dans l'ensemble, cela signifie que `setTimeout()` exécutera le code contenu dans une fonction donnée *une fois*, et seulement après une quantité de temps spécifiée.

À ce stade, il est utile de mentionner qu'au lieu de passer un nom de fonction, vous pouvez passer une fonction *anonyme* à `setTimeout()`.

Cela est pratique lorsque la fonction ne contient pas beaucoup de lignes de code.

Une fonction *anonyme* signifie que vous intégrez le code directement en tant que premier paramètre dans `setTimeout()`, et ne référencez pas le nom de la fonction comme vous l'avez vu ci-dessus.

```js
setTimeout(function() {
    // le code de la fonction va ici
}, time);
```

Une autre chose à noter est que `setTimeout()` retourne un `timeoutID` – un entier positif qui identifie le minuteur créé par `setTimeout()`.

Plus tard, vous verrez comment la valeur de `timeoutID` est utilisée avec la méthode `clearTimeout()`.

## Comment attendre N secondes en JavaScript <a name="attendre"></a>

Regardons un exemple de la façon dont `setTimeout()` est appliqué :

```js
// ce code est exécuté en premier

console.log("Où puis-je apprendre à coder gratuitement et obtenir un emploi de développeur ?");

// cette ligne indique que la définition de la fonction sera exécutée une fois que 3ms se seront écoulées

setTimeout(codingCourse, 3000);


// définition de la fonction

function codingCourse() {
  console.log("freeCodeCamp");
}
```

![js2](https://www.freecodecamp.org/news/content/images/2022/04/js2.gif)

Le code JavaScript est exécuté de haut en bas.

La première ligne de code, `console.log("Où puis-je apprendre à coder gratuitement et obtenir un emploi de développeur ?");`, est exécutée immédiatement une fois que j'appuie sur exécuter.

La deuxième ligne de code indique qu'il doit y avoir un délai planifié de 3000ms (ou 3 secondes) avant que le code dans la fonction `codingCourse()` ne soit exécuté.

Une fois que les 3000ms se sont écoulées, vous voyez que le code à l'intérieur de la fonction (`console.log("freeCodeCamp")`) s'exécute avec succès.

Regardons un autre exemple :

```js
console.log("Bonjour !");

setTimeout(function() {
  console.log("Bonne nuit !");
}, 1000);

console.log("Bon après-midi !");
```

![js4-1](https://www.freecodecamp.org/news/content/images/2022/04/js4-1.gif)

Dans l'exemple ci-dessus, la première ligne de code, `console.log("Bonjour !");`, s'exécute immédiatement.

Il en va de même pour la ligne `console.log("Bon après-midi !");`, même si c'est la dernière ligne de code dans le fichier.

Le code dans `setTimeout()` indique qu'il doit y avoir un délai d'une seconde avant qu'il ne s'exécute.

Cependant, pendant ce temps, l'exécution du reste du code dans le fichier n'est pas mise en attente.

Au lieu de cela, cette ligne est sautée pour le moment, et la ligne `console.log("Bon après-midi !");` est exécutée.

Une fois que cette seconde s'est écoulée, le code dans `setTimeout()` s'exécute.

Vous pouvez également passer des paramètres *optionnels* supplémentaires à `setTimeout()`.

Dans l'exemple ci-dessous, la fonction `greeting` accepte deux arguments, `phrase` et `name`.

```js
function greeting(phrase,name) {
  console.log(`${phrase}, mon nom est ${name}` );
}

setTimeout(greeting, 3000,"Bonjour le monde","John Doe");
```

Ceux-ci sont ensuite passés à la méthode `setTimeout()`, et il y aura un délai de 3 secondes une fois la fonction appelée :

![js6](https://www.freecodecamp.org/news/content/images/2022/04/js6.gif)


### Comment utiliser la méthode `clearTimeout()` en JavaScript  <a name="effacer"></a>

Que faire si vous souhaitez annuler l'événement temporisé que vous avez déjà créé ?

Vous pouvez empêcher le code dans `setTimeout()` de s'exécuter en utilisant la méthode `clearTimeout()`. C'est ici que le `timeoutID` mentionné précédemment est utile.

La syntaxe générale de `clearTimeout()` est la suivante :

```js
clearTimeout(timeoutID)
```

La façon dont cela fonctionne est que vous devez enregistrer le `timeoutID`, qui est retourné avec chaque appel de `setTimeout()`, dans une variable.

Ensuite, `timeoutID` est utilisé comme paramètre pour `clearTimeout()`, comme vu ci-dessous :

```js
let timeoutID = setTimeout(function(){
    console.log("Bonne nuit");
}, 2000);

clearTimeout(timeoutID);

console.log("Bonjour !");
```

![js5](https://www.freecodecamp.org/news/content/images/2022/04/js5.gif)

Maintenant, le code dans `setTimeout()` ne s'exécutera pas.

## Quelle est la différence entre `setTimeout` et `setInterval` ? <a name="difference"></a>

`setTimeout()` et `setInterval()` ont une syntaxe très similaire.

Voici la syntaxe pour `setInterval()` :

```js
setInterval(function_name, time);
```

Cependant, ce n'est pas une bonne idée de les utiliser de manière interchangeable car ils fonctionnent différemment.

`setTimeout()` déclenche une action **une fois**, tandis que `setInterval()` déclenche une action **de manière répétée**. 

Dans l'exemple ci-dessous, la fonction `codingCourse` est appelée toutes les trois secondes :

```js
console.log("Où puis-je apprendre à coder gratuitement et obtenir un emploi de développeur ?");


setInterval(codingCourse, 3000);


// définition de la fonction
function codingCourse() {
  console.log("freeCodeCamp");
}
```

![js3](https://www.freecodecamp.org/news/content/images/2022/04/js3.gif)

`setInterval()` est un bon choix lorsque vous souhaitez répéter quelque chose régulièrement.

## Conclusion

Et voilà ! Vous connaissez maintenant les bases de `setTimeout()` et comment créer des événements temporisés en JavaScript.

Pour en savoir plus sur JavaScript, rendez-vous sur la [Certification Algorithmes et Structures de Données JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de freeCodeCamp.

C'est un programme gratuit, bien pensé et structuré où vous apprendrez de manière interactive. À la fin, vous construirez également 5 projets pour obtenir votre certification et consolider vos connaissances en mettant vos nouvelles compétences en pratique.

Merci d'avoir lu !