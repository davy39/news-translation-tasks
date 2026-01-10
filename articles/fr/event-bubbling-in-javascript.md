---
title: Le bouillonnement d'événements en JavaScript – Comment fonctionne la propagation
  d'événements avec des exemples
date: '2022-10-31T21:04:17.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/event-bubbling-in-javascript
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/1.-event-bubbling-js.png
tags:
- name: Document Object Model
  slug: document-object-model
- name: DOM
  slug: dom
- name: JavaScript
  slug: javascript
seo_desc: "By Dillion Megida\nHTML elements receive different types of events, from\
  \ click, to blur, to scroll, and so on. \nOne behavior these events have in common\
  \ is Event Bubbling. I'll explain what this behavior means in this article.\nI also\
  \ made a video vers..."
---


Par Dillion Megida

<!-- more -->

Les éléments HTML reçoivent différents types d'événements, du `click` au `blur`, en passant par le `scroll`, et bien d'autres.

Un comportement que ces événements ont en commun est le bouillonnement d'événements (*Event Bubbling*). J'expliquerai ce que signifie ce comportement dans cet article.

J'ai également réalisé une version vidéo de cet article que [vous pouvez regarder ici][1].

## Qu'est-ce que le bouillonnement d'événements ?

Le bouillonnement d'événements est un concept du DOM (Document Object Model). Il se produit lorsqu'un élément reçoit un événement, et que cet événement remonte (on peut aussi dire qu'il est transmis ou propagé) vers ses éléments parents et ancêtres dans l'arborescence du DOM jusqu'à atteindre l'élément racine.

Il s'agit du comportement par défaut des événements sur les éléments, à moins que vous n'arrêtiez la propagation, [ce que j'expliquerai à la fin de cet article][2].

Regardons un exemple pour mieux expliquer le fonctionnement du bouillonnement d'événements.

Le HTML :

```
<body>
  <div>
    <span>
      <button>Click Me!</button>
    </span>
  </div>
</body>
```

Le CSS :

```
body {
  padding: 20px;
  background-color: pink;
}

div {
  padding: 20px;
  background-color: green;
  width: max-content;
}

span {
  display: block;
  padding: 20px;
  background-color: blue;
}
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-256.png)

Le **button** est un enfant du **span**, qui est lui-même un enfant du **div**, et le div est un enfant du **body**. L'arborescence DOM ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-263.png) _Arborescence DOM pour cette interaction_

Lorsque vous cliquez sur le **button**, vous pouvez considérer que vous cliquez également sur le **span** (le fond bleu). C'est parce que le bouton est un enfant du span.

C'est la même chose pour le **div** et le **body**. Lorsque vous cliquez sur le bouton, c'est comme si vous cliquiez également sur le span, le div et le body, car ils sont les ancêtres du bouton. C'est l'idée du bouillonnement d'événements.

Un événement ne s'arrête pas à l'élément direct qui le reçoit. L'événement remonte vers ses ancêtres, jusqu'à ce qu'il atteigne l'élément racine.

Ainsi, si le bouton reçoit un événement **click**, par exemple, le `span`, le `div` et le `body` (jusqu'à **html**, l'élément racine) reçoivent respectivement cet événement :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-264.png) _Illustration montrant le fonctionnement du bouillonnement d'événements_

De plus, si vous cliquez sur la boîte bleue (span), le bouton ne reçoit pas l'événement de clic car il n'est pas un parent ou un ancêtre du span. En revanche, le div, le body et le HTML recevraient l'événement.

La même chose se produit si vous cliquez sur le div – l'événement est propagé aux éléments body et html.

## Comment gérer les événements qui bouillonnent

Le comportement de "bouillonnement d'événements" vous permet de gérer un événement dans un élément parent au lieu de l'élément réel qui a reçu l'événement.

Ce modèle de gestion d'un événement sur un élément ancêtre est appelé la délégation d'événements (*Event Delegation*). Vous pouvez [en savoir plus ici][3].

Créons quelques écouteurs et gestionnaires d'événements :

```
const body = document.getElementsByTagName("body")[0]
const div = document.getElementsByTagName("div")[0]
const span = document.getElementsByTagName("span")[0]
const button = document.getElementsByTagName("button")[0]

body.addEventListener('click', () => {
  console.log("body was clicked")
})

div.addEventListener('click', () => {
  console.log("div was clicked")
})

span.addEventListener('click', () => {
  console.log("span was clicked")
})

button.addEventListener('click', () => {
  console.log("button was clicked")
})
```

Ici, nous avons sélectionné les éléments `body`, `div`, `span` et `button` du DOM. Ensuite, nous avons ajouté des écouteurs d'événements `click` à chacun d'eux avec une fonction de gestion qui affiche respectivement "body was clicked", "div was clicked", "span was clicked" et "button was clicked".

Ce qui s'affiche dans la console lorsque vous cliquez sur le fond rose (qui est le body) est :

```
body was clicked
```

Lorsque vous cliquez sur le fond vert (qui est le div), la console affiche :

```
div was clicked
body was clicked
```

L'événement "click" sur l'élément body est déclenché même si l'élément div était l'élément cible cliqué, car l'événement "click" a bouillonné du div vers le body.

Lorsque vous cliquez sur le fond bleu (qui est le span), la console affiche :

```
span was clicked
div was clicked
body was clicked
```

Et enfin, lorsque vous cliquez sur le bouton, la console affiche :

```
button was clicked
span was clicked
div was clicked
body was clicked
```

## Comment arrêter le bouillonnement d'événements

Le bouillonnement d'événements est un comportement par défaut. Mais dans certains cas, vous pourriez vouloir l'empêcher.

Supposons, par exemple, à partir de notre code HTML, que vous vouliez que le div ouvre une modale lorsqu'il est cliqué. Pour le bouton, en revanche, vous voulez qu'il effectue une requête API lorsqu'il est cliqué.

Dans ce cas, vous ne voudrez peut-être pas que la modale s'ouvre lorsque vous cliquez sur le bouton. Vous voudrez peut-être que la modale ne s'ouvre que lorsque vous cliquez réellement sur le div (et non lorsque vous cliquez sur l'un de ses enfants). C'est là qu'intervient l'arrêt de la propagation de l'événement.

Pour empêcher le bouillonnement d'un événement, vous utilisez la méthode `stopPropagation` de l'objet `event`.

Lors de la gestion des événements, un objet `event` est passé à la fonction de gestion :

```
button.addEventListener("click", (event) => {
  // faire n'importe quoi avec l'objet event
}
```

L'objet `event` contient des propriétés qui fournissent des informations sur l'événement déclenché et l'élément sur lequel il a été déclenché. Cet objet contient également des méthodes – l'une d'entre elles étant `stopPropagation()`.

La méthode `stopPropagation` d'un événement empêche l'événement de se propager aux parents et ancêtres de l'élément sur lequel l'événement a été déclenché.

Nous pouvons utiliser cela dans le code JavaScript ci-dessus :

```
body.addEventListener('click', () => {
  console.log("body was clicked")
})

div.addEventListener('click', () => {
  console.log("div was clicked")
})

span.addEventListener('click', () => {
  console.log("span was clicked")
})

button.addEventListener('click', (event) => {
  event.stopPropagation()
  console.log("button was clicked")
})
```

Avec cela, lorsque vous cliquez sur le bouton, tout ce que vous obtenez dans la console est :

```
button was clicked
```

Les parents et ancêtres du bouton ne reçoivent pas l'événement de clic car il ne remonte pas à partir du bouton.

Vous pouvez également arrêter le bouillonnement à partir d'un élément différent comme ceci :

```
body.addEventListener('click', () => {
  console.log("body was clicked")
})

div.addEventListener('click', () => {
  console.log("div was clicked")
})

span.addEventListener('click', (event) => {
  event.stopPropagation()
  console.log("span was clicked")
})

button.addEventListener('click', () => {
  console.log("button was clicked")
})
```

Avec `stopPropagation()` appelé sur l'écouteur d'événement du span, et le bouton cliqué, vous obtenez sur la console :

```
button was clicked
span was clicked
```

L'événement bouillonne du bouton vers le span mais s'arrête là car la propagation est interrompue à ce stade.

## Conclusion

Lorsque les éléments reçoivent des événements, ces événements se propagent vers leurs parents et ancêtres vers le haut dans l'arborescence DOM. C'est le concept de **bouillonnement d'événements** (*Event Bubbling*), et cela permet aux éléments parents de gérer les événements qui se produisent sur les éléments de leurs enfants.

Les objets d'événement possèdent également la méthode `stopPropagation` que vous pouvez utiliser pour arrêter le bouillonnement d'un événement. Cela est utile dans les cas où vous voulez qu'un élément reçoive un événement de clic uniquement lorsqu'il est cliqué, et non lorsque l'un de ses éléments enfants est cliqué.

`stopPropagation` et `preventDefault` sont des méthodes de l'objet `event` pour arrêter les comportements par défaut. Voici un article sur [la différence entre ces méthodes][4].

[1]: https://www.youtube.com/watch?v=KaHZdW02Tg0
[2]: #heading-comment-arreter-le-bouillonnement-d-evenements
[3]: https://www.freecodecamp.org/news/event-delegation-javascript/
[4]: https://www.freecodecamp.org/news/manage-default-behavior-in-browser/