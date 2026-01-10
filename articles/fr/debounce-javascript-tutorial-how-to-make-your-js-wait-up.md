---
title: Debounce JavaScript – Comment faire attendre votre JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-03T19:01:55.000Z'
originalURL: https://freecodecamp.org/news/debounce-javascript-tutorial-how-to-make-your-js-wait-up
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c996c740569d1a4ca1fa3.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Debounce JavaScript – Comment faire attendre votre JS
seo_desc: 'By Adeel Imran

  Debounce methods do not execute when invoked. Instead, they wait for a predetermined
  time before executing. If the same method is called again, the previous is cancelled
  and the timer restarts.

  Here is a short video walk through in whi...'
---

Par Adeel Imran

Les méthodes Debounce ne s'exécutent pas lorsqu'elles sont invoquées. Au lieu de cela, elles attendent un temps prédéterminé avant de s'exécuter. Si la même méthode est appelée à nouveau, la précédente est annulée et le minuteur redémarre.

Voici une courte vidéo dans laquelle je crée une méthode debounce :

%[https://youtu.be/NfYIiKRZTaU]

Et voici le code source du tutoriel vidéo :

%[https://codepen.io/adeelibr/pen/LYNPYmb?editors=1011]

Examinons maintenant le code plus en détail.

Supposons que vous avez un bouton appelé comme ceci :

```html
<button id="myBtn">Cliquez-moi</button>
```

Et dans votre fichier JS, vous avez quelque chose comme ceci :

```js
document.getElementById('myBtn').addEventListener('click', () => {
  console.log('cliqué');
})
```

Chaque fois que vous cliquez sur votre bouton, vous verrez un message dans votre console disant `cliqué`.

Ajoutons une méthode debounce à notre écouteur d'événement `click` ici :

```js
document.getElementById('myBtn').addEventListener('click', debounce(() => {
  console.log('cliqué');
}, 2000))
```

La méthode debounce prend ici deux arguments, `callback` et `wait`. `callback` est la fonction que vous souhaitez exécuter, tandis que `wait` est le délai de période configurable après lequel vous souhaitez que votre `callback` soit exécuté.

Ici, notre méthode `callback` est simplement `console.log('cliqué');` et le `wait` est `2000 millisecondes`.

Alors, étant donné cette méthode debounce, qui prend deux paramètres `callback` et `wait`, définissons `debounce` :

```js
function debounce(callback, wait) {
  let timerId;
  return (...args) => {
    clearTimeout(timerId);
    timerId = setTimeout(() => {
      callback(...args);
    }, wait);
  };
}
```

La fonction `debounce` prend deux paramètres : le callback (qui est la fonction que nous voulons exécuter) et la période `wait` (après combien de délai nous voulons exécuter notre callback).

À l'intérieur de la fonction, nous retournons simplement une fonction, qui est la suivante :

```js
let timerId;
return (...args) => {
  clearTimeout(timerId);
  timerId = setTimeout(() => {
    callback(...args);
  }, wait);
};
```

Ce que fait cette fonction, c'est invoquer notre méthode `callback` après une certaine période de temps. Et si, pendant cette période, la même méthode est invoquée à nouveau, la fonction précédente est annulée et le minuteur est réinitialisé et redémarre.

Et c'est tout ! Tout ce que vous devez savoir sur ce qu'est le debounce.

Voici une autre vidéo bonus sur les fermetures (closures), car j'ai utilisé une `closure` à l'intérieur de ma fonction `debounce`.

%[https://youtu.be/-Q7oXxxw0-c]

Faites-moi savoir sur [twitter](https://twitter.com/adeelibr) si vous avez pu trouver l'utilisation de la fermeture à l'intérieur de la méthode debounce.

Bon codage à tous.