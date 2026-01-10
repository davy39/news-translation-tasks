---
title: La délégation d'événements en JavaScript – Expliquée avec un exemple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-01T17:58:39.000Z'
originalURL: https://freecodecamp.org/news/event-delegation-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/2.-event-delegation-js.png
tags:
- name: JavaScript
  slug: javascript
seo_title: La délégation d'événements en JavaScript – Expliquée avec un exemple
seo_desc: 'By Dillion Megida

  Event Delegation is a pattern based upon the concept of Event Bubbling. It is an
  event-handling pattern that allows you to handle events at a higher level in the
  DOM tree other than the level where the event was first received.

  Ther...'
---

Par Dillion Megida

La délégation d'événements est un modèle basé sur le concept de [remontée d'événements](https://www.freecodecamp.org/news/event-bubbling-in-javascript/). Il s'agit d'un modèle de gestion d'événements qui permet de gérer les événements à un niveau plus élevé dans l'arborescence DOM plutôt qu'au niveau où l'événement a été reçu initialement.

Il existe une [version vidéo de ce sujet](https://www.youtube.com/watch?v=aZ3JWv0ofuA) si vous préférez cela.

## Une brève introduction à la propagation d'événements

Par défaut, les événements déclenchés sur un élément se propagent vers le haut de l'arborescence DOM jusqu'à l'élément parent, ses ancêtres, et ainsi de suite jusqu'à l'élément racine (`html`).

Regardez cet exemple :

```html
<div>
  <span>
    <button>Cliquez-moi !</button>
  </span>
</div>
```

Ici, nous avons une `div` qui est le parent d'un `span`, qui à son tour est le parent de l'élément `button`.

En raison de la remontée d'événements, lorsque le bouton reçoit un événement, par exemple un **clic**, cet événement remonte dans l'arborescence, de sorte que `span` et `div` recevront également l'événement.

Si vous souhaitez en savoir plus sur la remontée d'événements, vous pouvez [lire mon article à ce sujet ici](https://www.freecodecamp.org/news/event-bubbling-in-javascript/).

## Comment fonctionne la délégation d'événements ?

Avec la délégation d'événements, au lieu de gérer l'événement de clic sur le `button`, vous pouvez le gérer sur la `div`.

L'idée est que vous "**déléguez**" la gestion d'un événement à un autre élément (dans ce cas, la div, qui est un élément parent) au lieu de l'élément réel (le bouton) qui a reçu l'événement.

Voici ce que je veux dire par là en code :

```js
const div = document.getElementsByTagName("div")[0]

div.addEventListener("click", (event) => {
  if(event.target.tagName === 'BUTTON') {
    console.log("le bouton a été cliqué")
  }
})
```

L'objet `event` possède une propriété `target` qui contient des informations sur l'élément qui a réellement reçu l'événement. Avec `target.tagName`, nous obtenons le nom de la balise de l'élément, et nous vérifions s'il s'agit de **BUTTON**.

Avec ce code, lorsque vous cliquez sur le `button`, l'événement remonte jusqu'à la `div` qui gère l'événement.

## Avantages de la délégation d'événements

La délégation d'événements est un modèle utile qui permet d'écrire un code plus propre et de créer moins d'écouteurs d'événements avec une logique similaire.

Que veux-je dire par là ? Regardez ce code :

```html
<div>
  <button>Bouton 1</button>
  <button>Bouton 2</button>
  <button>Bouton 3</button>
</div>
```

Ici, nous avons 3 boutons. Supposons que nous voulions gérer un événement de clic sur chaque bouton, de sorte que lorsque l'un d'eux est cliqué, le texte du bouton soit enregistré dans la console. Nous pouvons l'implémenter comme ceci :

```js
const buttons = document.querySelectorAll('button')

buttons.forEach(button => {
  button.addEventListener("click", (event) => {
    console.log(event.target.innerText)
  })
})
```

J'utilise ici `querySelectorAll` car il retourne une `NodeList` sur laquelle je peux utiliser la méthode `forEach`. `getElementsByTagName` retourne une `HTMLCollection` qui ne possède pas la méthode `forEach`.

Lorsque vous cliquez sur le premier bouton, "Bouton 1" est enregistré dans la console. Pour le deuxième bouton, "Bouton 2" est enregistré, et pour le troisième bouton, "Bouton 3" est enregistré.

Bien que cela fonctionne comme nous le voulons, nous avons créé trois écouteurs d'événements pour les trois boutons.

Étant donné que l'événement de clic sur ces boutons se propage vers le haut dans l'arborescence DOM, nous pouvons utiliser un parent ou un ancêtre commun qu'ils partagent pour gérer l'événement. Dans ce cas, nous déléguons à un parent commun qu'ils partagent pour gérer la logique que nous voulons.

Voici comment :

```js
const div = document.querySelector('div')

div.addEventListener("click", (event) => {
  if(event.target.tagName === 'BUTTON') {
    console.log(event.target.innerText)
  }
})
```

Maintenant, nous n'avons qu'un seul écouteur d'événement, mais la même logique : lorsque vous cliquez sur le premier bouton, "Bouton 1" est enregistré dans la console, et ainsi de suite pour les autres boutons.

Même si nous ajoutons un bouton supplémentaire comme ceci :

```html
<div>
  <button>Bouton 1</button>
  <button>Bouton 2</button>
  <button>Bouton 3</button>
  <button>Bouton 4</button>
</div>
```

Nous n'aurons pas à modifier le code JavaScript car ce nouveau bouton partage également le parent `div` (auquel nous avons délégué la gestion de l'événement) avec les autres boutons.

## Conclusion

Avec la délégation d'événements, vous créez moins d'écouteurs d'événements et effectuez une logique similaire basée sur les événements en un seul endroit. Cela facilite l'ajout et la suppression d'éléments sans avoir à ajouter de nouveaux écouteurs d'événements ou à supprimer ceux existants.

La délégation d'événements est possible grâce à la propagation d'événements dans le DOM, où l'événement qu'un élément enfant reçoit est également transmis au parent et aux ancêtres de l'enfant. Encore une fois, vous pouvez [en savoir plus sur la remontée d'événements ici](https://www.freecodecamp.org/news/event-bubbling-in-javascript/).

Merci d'avoir lu, et bon codage !