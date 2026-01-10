---
title: Les Événements du Navigateur Expliqués en Français Simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-29T21:14:43.000Z'
originalURL: https://freecodecamp.org/news/javascript-events-explained-in-simple-english
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/events.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: events
  slug: events
- name: JavaScript
  slug: javascript
seo_title: Les Événements du Navigateur Expliqués en Français Simple
seo_desc: 'What are browser events?

  An event refers to an action or occurrence that happens in the system you are programming.
  The system then notifies you about the event so that you can respond to it in some
  way if necessary.

  In this article, I will focus on ...'
---

## Qu'est-ce que les événements du navigateur ?

Un [événement](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events) fait référence à une action ou à un événement qui se produit dans le système que vous programmez. Le système vous notifie ensuite de l'événement afin que vous puissiez y répondre de manière appropriée si nécessaire.

Dans cet article, je me concentrerai sur les événements dans le contexte des navigateurs web. Essentiellement, un événement est un indicateur qui montre qu'une certaine action a eu lieu afin que vous puissiez faire une réponse appropriée.

Pour illustrer ce dont je parle, imaginons que vous êtes debout à un passage piéton, attendant que les feux de circulation changent afin que vous puissiez traverser la route en toute sécurité. L'événement est le changement de feu de circulation qui vous fait ensuite prendre une action – qui, dans ce cas, est de traverser la route.

De même, en développement web, nous pouvons prendre une action chaque fois qu'un événement qui nous intéresse se produit.

Certains des événements courants que vous avez peut-être rencontrés en développement web incluent :

1. Événements de la souris

* `click`

* `dblclick`

* `mousemove`

* `mouseover`

* `mousewheel`

* `mouseout`

* `contextmenu`

* `mousedown`

* `mouseup`

2. Événements tactiles

* `touchstart`

* `touchmove`

* `touchend`

* `touchcancel`

3. Événements du clavier

* `keydown`

* `keypress`

* `keyup`

4. Événements de formulaire

* `focus`

* `blur`

* `change`

* `submit`

5. Événements de la fenêtre

* `scroll`

* `resize`

* `hashchange`

* `load`

* `unload`

Pour une liste complète des événements et des différentes catégories dans lesquelles ils tombent, vous pouvez consulter la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/Events). Certains des événements listés sont des événements standard dans les spécifications officielles, tandis que d'autres sont des événements utilisés en interne par des navigateurs spécifiques.

## Qu'est-ce que les gestionnaires d'événements ?

Comme mentionné ci-dessus, nous surveillons les événements afin que, chaque fois que nous recevons une notification que l'événement s'est produit, le programme puisse prendre l'action appropriée.

Cette action est souvent prise dans des fonctions appelées **gestionnaires d'événements** qui sont également appelés **écouteurs d'événements**. Si un événement se produit et que le gestionnaire d'événements est invoqué, nous disons qu'un événement a été enregistré. Cela est illustré dans le code ci-dessous.

Si le bouton avec l'`id` `btn` est cliqué, le gestionnaire d'événements est invoqué et une alerte avec le texte "Le bouton a été cliqué" est affichée. La propriété `onclick` a été assignée à une fonction qui est le gestionnaire d'événements. C'est l'une des trois façons d'ajouter un gestionnaire d'événements à un élément DOM.

```js
const button = document.getElementById("btn");
button.onclick = function(){
   alert("Le bouton a été cliqué");
}
```

Il est important de noter que les **gestionnaires d'événements** sont principalement déclarés comme des fonctions, mais ils peuvent aussi être des objets.

## Comment assigner des gestionnaires d'événements

Il existe plusieurs façons d'attacher des gestionnaires d'événements aux éléments HTML. Nous allons discuter de ces méthodes, ainsi que de leurs avantages et inconvénients, ci-dessous.

### Assignation d'un gestionnaire d'événements avec un attribut HTML

C'est la façon la plus simple d'attacher un gestionnaire d'événements aux éléments HTML, bien que ce soit la moins recommandée. Cela implique l'utilisation d'un attribut d'événement HTML en ligne nommé `on<event>` dont la valeur est le gestionnaire d'événements. Par exemple `onclick`, `onchange`, `onsubmit` et ainsi de suite.

Notez qu'il n'est pas rare de trouver des attributs d'événement HTML nommés `onClick`, `onChange` ou `onSubmit` car les attributs HTML ne sont pas sensibles à la casse. Essentiellement, il est syntaxiquement correct d'utiliser `onclick`, `onClick` ou `ONCLICK`. Mais il est courant de le laisser en minuscules.

```html
<button onclick = "alert('Bonjour le monde !')"> Cliquez-moi </button>
<button onclick = "(() => alert('Bonjour le monde !'))()"> Cliquez-moi aussi </button>
<button onclick = "(function(){alert('Bonjour le monde !')})()"> Et moi </button>
```

Dans l'exemple ci-dessus, le code JavaScript a été littéralement assigné à l'attribut d'événement HTML.

Notez le format de l'expression de fonction immédiatement invoquée (IIFE) dans les deux derniers éléments `button`. Bien que cela semble facile et direct, l'assignation d'un attribut d'événement HTML en ligne est inefficace et difficile à maintenir.

Imaginez que vous avez plus de 20 boutons de ce type dans votre balisage. Il serait répétitif d'écrire le même code JavaScript pour chaque bouton. Il est toujours préférable d'écrire JavaScript dans son propre fichier afin que vous puissiez facilement utiliser le même code pour plusieurs fichiers HTML.

De plus, vous ne pouvez pas avoir plusieurs lignes de code JavaScript en ligne. Le code JavaScript en ligne est considéré comme un anti-modèle pour les raisons mentionnées ci-dessus. Essayez donc de l'éviter sauf si vous essayez quelque chose de rapide.

### Déclaration d'un gestionnaire d'événements dans une balise `script`

Au lieu de faire ce qui précède, vous pouvez également déclarer le gestionnaire d'événements dans une balise `script` et l'invoquer en ligne comme montré ci-dessous.

```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="./index.css" type="text/css" />
    <script>
      function onClickHandler(){
         alert("Bonjour le monde !");
       }
    </script> 
  </head>
  <body>
    <div class="wrapper">
       <button onclick = "onClickHandler()"> Cliquez-moi </button>
    </div>
  </body>
</html>
```

Remarquez, cependant, que simplement assigner le nom de la fonction comme valeur de l'attribut d'événement HTML comme `onclick = "onClickHandler"` ne fonctionnera pas. Vous devez l'invoquer comme montré ci-dessus, en enfermant l'invocation entre guillemets comme la valeur de n'importe quel attribut HTML.

### Assignation d'un gestionnaire d'événements en utilisant la propriété DOM

Au lieu d'utiliser l'attribut d'événement HTML en ligne illustré ci-dessus, vous pouvez également assigner le gestionnaire d'événements comme valeur d'une propriété d'événement sur l'élément DOM. Cela n'est possible qu'à l'intérieur d'une balise `script` ou dans un fichier JavaScript.

Une limitation de cette approche est que vous ne pouvez pas avoir plusieurs gestionnaires d'événements pour le même événement. Si vous avez plusieurs gestionnaires pour le même événement, comme illustré ci-dessous, seul le dernier sera appliqué. Les autres seront écrasés.

```js
const button = document.getElementById("btn");
button.onclick = function(){
   alert("Le bouton a été cliqué");
}
// Seul celui-ci est appliqué
button.onclick = function(){
   console.log("Le bouton a été cliqué");
}
```

Si vous souhaitez supprimer l'écouteur d'événement de l'événement `onclick`, vous pouvez simplement réassigner `button.onclick` à `null`.

```js
button.onclick = null
```

### Comment améliorer la méthode DOM d'ajout d'écouteurs d'événements

La méthode ci-dessus d'ajout d'écouteurs d'événements est préférable à l'utilisation de JavaScript en ligne. Cependant, elle a une limitation qui restreint un élément à n'avoir qu'un seul gestionnaire d'événements pour chaque événement.

Par exemple, vous ne pouvez pas appliquer plusieurs gestionnaires d'événements pour un événement de clic sur un élément.

Pour remédier à cette limitation, `addEventListener` et `removeEventListener` ont été introduits. Cela vous permet d'ajouter plusieurs gestionnaires d'événements pour le même événement sur le même élément.

```js
const button = document.getElementById('btn');
button.addEventListener('click', () => {
  alert('Bonjour le monde');
})
button.addEventListener('click', () => {
  console.log('Bonjour le monde');
})
```

Dans le code ci-dessus, un élément avec l'`id` `btn` est sélectionné puis surveillé pour un événement `click` en attachant deux gestionnaires d'événements. Le premier gestionnaire d'événements sera invoqué et un message d'alerte `Bonjour le monde` apparaîtra. Ensuite, `Bonjour le monde` sera également enregistré dans la console.

Comme vous l'avez peut-être remarqué dans les exemples ci-dessus, la signature de la fonction `element.addEventListener` est :

```js
element.addEventListener(event, eventHandler, [paramètre optionnel])
```

#### Paramètres de la méthode `addEventListener`

1. **event**

Le premier paramètre, `event` (qui est un paramètre requis) est une chaîne qui spécifie le nom de l'événement. Par exemple `"click"`, `"mouseover"`, `"mouseout"` et ainsi de suite.

2. **eventHandler**

Le deuxième paramètre, qui comme le premier est également requis, est une fonction qui est invoquée lorsque l'événement se produit. Un objet événement est passé comme premier paramètre. L'objet événement dépend du type d'événement. Par exemple, un objet `MouseEvent` est passé pour un événement de clic.

3. **Paramètre optionnel**

Le troisième paramètre, qui est un paramètre optionnel, est un objet avec les propriétés :

* `once` : Sa valeur est un booléen. Si `true`, l'écouteur est supprimé après son déclenchement.

* `capture` : Sa valeur est également un booléen. Il définit la phase où il doit gérer l'événement, qui peut être soit dans la phase de bulle, soit dans la phase de capture. La valeur par défaut est `false`, donc l'événement est capturé dans la phase de bulle. Vous pouvez en lire plus à ce sujet [ici](https://javascript.info/bubbling-and-capturing). Pour des raisons historiques, les options peuvent également être `true` ou `false`.

* `passive` : Sa valeur est également un booléen. Si elle est `true`, alors le gestionnaire n'appellera pas `preventDefault()`. `preventDefault()` est une méthode de l'objet événement.

De même, si vous souhaitez arrêter de surveiller l'événement `click`, vous pouvez utiliser `element.removeEventListener`. Mais cela ne fonctionne que si l'écouteur d'événement a été enregistré en utilisant `element.addEventListener`. La signature de la fonction est similaire à celle de `element.addEventListener`.

```js
element.removeEventListener(event, eventHandler, [options])
```

Pour que nous puissions utiliser `element.removeEventListener` pour supprimer un `event`, la fonction passée comme deuxième argument à `element.addEventListener` doit être une fonction nommée lors de l'ajout de l'écouteur d'événement. Cela garantit que la même fonction peut être passée à `element.removeEventListener` si nous voulons la supprimer.

Il est également important de mentionner ici que, si vous avez passé les arguments optionnels au gestionnaire d'événements, alors vous devez également passer les mêmes arguments optionnels à `removeEventListener`.

```js
const button = document.getElementById('btn');
button.removeEventListener('click', clickHandler)
```

## Qu'est-ce que les objets événement ?

Un gestionnaire d'événements a un paramètre appelé **objet événement** qui contient des informations supplémentaires sur l'événement.

Les informations stockées dans l'**objet événement** dépendent du type d'événement. Par exemple, l'**objet événement** passé à un gestionnaire d'événements `click` a une propriété appelée `target` qui référence l'élément à partir duquel l'événement de clic a été déclenché.

Dans l'exemple ci-dessous, si vous cliquez sur l'élément avec l'`id` `btn`, `event.target` le référencera. Tous les gestionnaires d'événements de clic reçoivent un **objet événement** avec la propriété `target`. Comme déjà mentionné, différents événements ont des paramètres **objet événement** qui stockent différentes informations.

```js
const button = document.getElementById("btn");
button.addEventListener("click", event => {
  console.log(event.target);
})
```

## La valeur de `this`

Dans un gestionnaire d'événements, la valeur de `this` est l'élément sur lequel le gestionnaire d'événements est enregistré. Notez que l'élément sur lequel le gestionnaire d'événements est enregistré n'est pas nécessairement le même que l'élément sur lequel l'événement s'est produit.

Par exemple, dans le code ci-dessous, le gestionnaire d'événements est enregistré sur le wrapper. Normalement, la valeur de `this` est la même que `event.currentTarget`. Si vous cliquez sur le `button`, la valeur de `this` à l'intérieur de `onClickHandler` est le `div` et non le `button` car c'est le `div` sur lequel le gestionnaire d'événements est enregistré, bien que le clic provienne du bouton.

Cela s'appelle la `propagation d'événement`. C'est un concept très important que vous pouvez lire [ici](https://www.sitepoint.com/event-bubbling-javascript/) si vous êtes intéressé.

```html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="./index.css" type="text/css" />
    <script>
      function onClickHandler(){
         console.log(this)
         alert("Bonjour le monde !");
       }
       const wrapper = document.querySelector(".wrapper");
       wrapper.addEventListener("click", onClickHandler);
    </script> 
  </head>
  <body>
    <div class="wrapper">
       <button> Cliquez-moi </button>
    </div>
  </body>
</html>
```

## Conclusion

Dans cet article, nous avons examiné :

* Les événements du navigateur et ce qu'ils sont

* Différentes façons d'ajouter des gestionnaires d'événements aux éléments DOM

* Les paramètres d'objet événement pour les gestionnaires d'événements

* La valeur de `this` dans un gestionnaire d'événements