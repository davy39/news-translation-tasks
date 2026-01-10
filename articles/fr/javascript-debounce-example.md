---
title: Debounce – Comment retarder une fonction en JavaScript (Exemple JS ES6)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-18T18:16:53.000Z'
originalURL: https://freecodecamp.org/news/javascript-debounce-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/teaser.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Debounce – Comment retarder une fonction en JavaScript (Exemple JS ES6)
seo_desc: "By Ondrej Polesny\nIn JavaScript, a debounce function makes sure that your\
  \ code is only triggered once per user input. Search box suggestions, text-field\
  \ auto-saves, and eliminating double-button clicks are all use cases for debounce.\
  \ \nIn this tutoria..."
---

Par Ondrej Polesny

En JavaScript, une fonction debounce garantit que votre code n'est déclenché qu'une seule fois par entrée utilisateur. Les suggestions de boîte de recherche, les sauvegardes automatiques des champs de texte et l'élimination des doubles clics sur les boutons sont autant de cas d'utilisation pour debounce. 

Dans ce tutoriel, nous allons apprendre à créer une fonction debounce en JavaScript.

## Qu'est-ce que debounce ?

Le terme **debounce** vient de l'électronique. Lorsque vous appuyez sur un bouton, disons sur votre télécommande de télévision, le signal voyage vers la micropuce de la télécommande si rapidement que avant que vous n'ayez le temps de relâcher le bouton, il rebondit, et la micropuce enregistre votre "clic" plusieurs fois.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/debounce-button.png)

Pour atténuer cela, une fois qu'un signal du bouton est reçu, la micropuce cesse de traiter les signaux du bouton pendant quelques microsecondes, le temps qu'il est physiquement impossible pour vous d'appuyer à nouveau dessus.

## Debounce en JavaScript

En JavaScript, le cas d'utilisation est similaire. Nous voulons déclencher une fonction, mais seulement une fois par cas d'utilisation. 

Disons que nous voulons afficher des suggestions pour une requête de recherche, mais seulement après qu'un visiteur ait fini de la taper. 

Ou nous voulons sauvegarder les modifications d'un formulaire, mais seulement lorsque l'utilisateur ne travaille pas activement sur ces modifications, car chaque "sauvegarde" nous coûte un voyage vers la base de données. 

Et mon préféré—certaines personnes se sont vraiment habituées à Windows 95 et double-cliquent maintenant sur tout 😁.

Voici une implémentation simple de la fonction _debounce_ ([CodePen ici](https://codepen.io/ondrabus/pen/WNGaVZN)) :

```js
function debounce(func, timeout = 300){
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => { func.apply(this, args); }, timeout);
  };
}
function saveInput(){
  console.log('Sauvegarde des données');
}
const processChange = debounce(() => saveInput());
```

Elle peut être utilisée sur un champ de saisie :

```html
<input type="text" onkeyup="processChange()" />
```


Ou un bouton :

```html
<button onclick="processChange()">Cliquez-moi</button>
```

Ou un événement de fenêtre :

```js
window.addEventListener("scroll", processChange);
```

Et sur d'autres éléments comme une simple fonction JS.

Alors, que se passe-t-il ici ? La fonction `debounce` est une fonction spéciale qui gère deux tâches :

* Allouer une portée pour la variable _timer_
* Planifier votre fonction pour qu'elle soit déclenchée à un moment spécifique

Expliquons comment cela fonctionne dans le premier cas d'utilisation avec une saisie de texte. 

Lorsque le visiteur écrit la première lettre et relâche la touche, `debounce` réinitialise d'abord le timer avec `clearTimeout(timer)`. À ce stade, l'étape n'est pas nécessaire car il n'y a encore rien de planifié. Ensuite, il planifie la fonction fournie—`saveInput()`—pour qu'elle soit invoquée dans 300 ms. 

Mais supposons que le visiteur continue d'écrire, donc chaque relâchement de touche déclenche à nouveau `debounce`. Chaque invocation doit réinitialiser le timer, ou, en d'autres termes, annuler les plans précédents avec `saveInput()`, et le reprogrammer pour un nouveau moment—300 ms dans le futur. Cela continue tant que le visiteur continue de frapper les touches en moins de 300 ms. 

La dernière planification ne sera pas annulée, donc `saveInput()` sera finalement appelée.

## L'autre approche—comment ignorer les événements suivants

C'est bien pour déclencher la sauvegarde automatique ou afficher des suggestions. Mais qu'en est-il du cas d'utilisation avec plusieurs clics sur un seul bouton ? Nous ne voulons pas attendre le dernier clic, mais plutôt enregistrer le premier et ignorer les autres ([CodePen ici](https://codepen.io/ondrabus/pen/bGwmXjN)).

```js
function debounce_leading(func, timeout = 300){
  let timer;
  return (...args) => {
    if (!timer) {
      func.apply(this, args);
    }
    clearTimeout(timer);
    timer = setTimeout(() => {
      timer = undefined;
    }, timeout);
  };
}
```

Ici, nous déclenchons la fonction `saveInput()` lors du premier appel à `debounce_leading` causé par le premier clic sur le bouton. Nous planifions la destruction du timer pour dans 300 ms. Chaque clic de bouton ultérieur dans ce laps de temps aura déjà le timer défini et ne fera que repousser la destruction de 300 ms dans le futur.

## Implémentations de Debounce dans les bibliothèques

Dans cet article, je vous ai montré comment implémenter une fonction debounce en JavaScript et l'utiliser pour, eh bien, debouncer les événements déclenchés par les éléments d'un site web. 

Cependant, vous n'avez pas besoin d'utiliser votre propre implémentation de _debounce_ dans vos projets si vous ne le souhaitez pas. Les bibliothèques JS largement utilisées contiennent déjà son implémentation. Voici quelques exemples :

<table style="border-spacing: 0; border-collapse: collapse;"><tbody><tr><td style="padding: 4px; border: 1px solid black;"><em><strong>Bibliothèque</strong></em></td><td style="padding: 4px; border: 1px solid black;"><em><strong>Exemple</strong></em></td></tr><tr><td style="padding: 4px; border: 1px solid black;"><a href="http://benalman.com/projects/jquery-throttle-debounce-plugin/">jQuery (via bibliothèque)</a></td><td style="padding: 4px; border: 1px solid black;"><code>$.debounce(300, saveInput);</code></td></tr><tr><td style="padding: 4px; border: 1px solid black;"><a href="https://lodash.com/docs/4.17.15#debounce">Lodash</a></td><td style="padding: 4px; border: 1px solid black;"><code>_.debounce(saveInput, 300);</code></td></tr><tr><td style="padding: 4px; border: 1px solid black;"><a href="https://underscorejs.org/#debounce">Underscore</a></td><td style="padding: 4px; border: 1px solid black;"><code>_.debounce(saveInput, 300);</code></td></tr></tbody></table>