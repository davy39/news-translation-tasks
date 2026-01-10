---
title: Comment construire une fenêtre modale avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-03T23:49:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-modal-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/How-to-build-a-modal-with-JavaScript.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: user experience
  slug: user-experience
- name: Web Development
  slug: web-development
seo_title: Comment construire une fenêtre modale avec JavaScript
seo_desc: "By Victor Eke\nIt's probably happened to you before: you unintentionally\
  \ attempted to perform an action on a webpage, but luckily got a pop-up window asking\
  \ you to confirm your decision. \nThis pop-up window is called a modal. It's a web\
  \ page element t..."
---

Par Victor Eke

Cela vous est probablement déjà arrivé : vous avez involontairement tenté d'effectuer une action sur une page Web, mais vous avez heureusement reçu une fenêtre contextuelle vous demandant de confirmer votre décision.

Cette fenêtre contextuelle est appelée une modale. C'est un élément de page Web qui s'affiche au premier plan, devant le reste du contenu de la page.

Vous pouvez utiliser les modales pour diverses raisons, comme stocker des informations que vous ne souhaitez pas voir immédiatement sur une page Web, créer des menus de navigation, ajouter des éléments d'appel à l'action (CTA), et bien plus encore.

Un excellent exemple est la modale qui apparaît sur Twitter lorsque vous tentez de fermer le menu de composition d'un tweet.

![Fenêtre modale d'avertissement Twitter](https://www.freecodecamp.org/news/content/images/2022/10/twitter_warning_message_modal.png)

Vous pouvez également utiliser les modales pour d'autres choses comme la création d'éléments d'appel à l'action, de menus de navigation, de widgets de newsletter, etc.

En tant que développeur Web, savoir comment construire une modale peut être une compétence très pratique. Dans ce tutoriel, je vais vous guider à travers le processus de création d'une modale simple en utilisant HTML, CSS et JavaScript.

Voici une capture d'écran de ce que nous allons construire :

![Une modale construite avec html, css et javascript](https://www.freecodecamp.org/news/content/images/2022/10/modal.png)

Les étapes sont très faciles à suivre, vous pourrez donc personnaliser la modale ou construire la vôtre à partir de zéro – c'est entièrement à vous de décider. À la fin de cet article, je fournirai le fichier CodePen afin que vous puissiez l'expérimenter.

## Étape 1 – Ajouter le balisage

Très bien, commençons par le HTML.

Tout d'abord, vous allez ajouter un élément `section` et lui donner deux classes, `modal` et `hidden`. Sous cet élément, vous aurez également un élément `<div>` avec les classes `overlay` et `hidden`. Enfin, vous ajouterez un élément `<button>` avec les classes `btn` et `btn-open`.

Voici à quoi cela ressemble :

```html
<section class="modal hidden"></section>
<div class="overlay hidden"></div>
<button class="btn btn-open">Open Modal</button>
```

- L'élément section avec la classe `modal` servira de conteneur pour votre modale.
- La div avec la classe `overlay` servira d'élément de superposition. C'est l'arrière-plan sombre et flou que vous voyez lorsque la modale est ouverte.
- Le bouton avec les classes `btn` et `btn-open` servira de bouton d'ouverture pour déclencher notre modale lorsque vous cliquez dessus.

Maintenant, à l'intérieur de votre modale, ajoutez le balisage, ainsi que le bouton `X` pour fermer la modale. Ce bouton se verra attribuer une classe `btn-close`.

Voici donc à quoi ressemblera votre balisage complet à la fin :

```html
<section class="modal hidden">
  <div class="flex">
    <img src="user.png" width="50px" height="50px" alt="user" />
    <button class="btn-close">✖</button>
  </div>
  <div>
    <h3>Restez en contact</h3>
    <p>
      Ceci est un faux formulaire de newsletter, ne prenez donc pas la peine de le tester. Pas
      que je m'attende à ce que vous le fassiez, de toute façon. :)
    </p>
  </div>

  <input type="email" id="email" placeholder="brendaneich@js.com" />
  <button class="btn">Envoyer</button>
</section>

<div class="overlay hidden"></div>
<button class="btn btn-open">Ouvrir la modale</button>
```

**Important** ⚠️ Notez bien la classe `hidden` ajoutée à la modale et à l'élément overlay. C'est très important car vous ciblerez ces classes pour masquer votre modale et l'overlay en utilisant CSS.

Voici le résultat :

![balisage-complet](https://www.freecodecamp.org/news/content/images/2022/10/complete-markup.png)

## Étape 2 – Styliser la modale

Commençons par réinitialiser la marge et le rembourrage (padding) par défaut de chaque élément de la page, puis centrons la modale et le bouton d'ouverture.

Passez maintenant à votre CSS et ajoutez les styles suivants :

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Inter", sans-serif;
}

body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #222;
  position: relative;
  min-height: 100vh;
}
```

L'étape suivante consiste à styliser le conteneur de la modale lui-même et les éléments à l'intérieur. Ce processus est un peu long, je vais donc simplement copier et coller le style ici, puis l'expliquer brièvement après :

```css
.modal {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.4rem;
  width: 450px;
  padding: 1.3rem;
  min-height: 250px;
  position: absolute;
  top: 20%;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 15px;
}

.modal .flex {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal input {
  padding: 0.7rem 1rem;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 0.9em;
}

.modal p {
  font-size: 0.9rem;
  color: #777;
  margin: 0.4rem 0 0.2rem;
}

button {
  cursor: pointer;
  border: none;
  font-weight: 600;
}

.btn {
  display: inline-block;
  padding: 0.8rem 1.4rem;
  font-weight: 700;
  background-color: black;
  color: white;
  border-radius: 5px;
  text-align: center;
  font-size: 1em;
}

.btn-open {
  position: absolute;
  bottom: 150px;
}

.btn-close {
  transform: translate(10px, -20px);
  padding: 0.5rem 0.7rem;
  background: #eee;
  border-radius: 50%;
}
```

Et voici le résultat :

![style-modale-complet](https://www.freecodecamp.org/news/content/images/2022/10/complete-modal-style.png)

Ce que vous avez fait, c'est styliser l'élément modal puis le positionner en utilisant la propriété `absolute`. Cela fonctionne parce que vous avez ajouté une propriété `position: relative` à l'élément `body` précédemment.

Vous avez également stylisé les éléments à l'intérieur de la modale, mais je n'entrerai pas dans les détails car ce n'est pas l'aspect le plus crucial ici.

## Étape 3 – Ajouter l'overlay

Pour l'overlay, vous voulez le positionner sur toute la page avec un arrière-plan sombre subtil et un flou.

Puisque vous avez la position relative sur l'élément `body`, vous pouvez utiliser la propriété `position: fixed` pour ajouter l'overlay par-dessus. Vous allez le superposer sur 100 % de la largeur et de la hauteur de la fenêtre d'affichage (viewport).

```css
.overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(3px);
  z-index: 1;
}
```

Voici le résultat :

![overlay](https://www.freecodecamp.org/news/content/images/2022/10/overlay.png)

L'overlay fonctionne, mais vous voulez qu'il n'affecte que l'élément body et non la modale. Pour corriger cela, ajoutez une propriété `z-index` plus élevée au conteneur de la modale.

```css
.modal {
  z-index: 2;
}
```

Maintenant, la modale devrait être sur l'overlay et non derrière.

![modal](https://www.freecodecamp.org/news/content/images/2022/10/modal-1.png)

Vous avez réussi à créer la modale et à ajouter un overlay derrière elle ! Mais vous ne voulez pas afficher la modale, du moins pas avant que le bouton `btn-open` ne soit cliqué.

Pour la masquer, vous devez cibler la classe `.hidden` que vous avez ajoutée précédemment à la modale et à l'élément overlay dans votre CSS. Vous lui donnerez également un `display: none`.

```css
.hidden {
  display: none;
}
```

Maintenant, seul le bouton s'affiche sur la page. Vous pouvez maintenant travailler sur la fonctionnalité de la modale en utilisant JavaScript.

## Étape 4 – Ajouter la fonctionnalité de la modale

Avant de continuer, je pense qu'il est préférable d'expliquer comment la modale fonctionne. Vous vous souvenez comment vous avez utilisé la classe `hidden` pour masquer la modale et l'overlay ? Pour ajouter ou supprimer cette classe des éléments, vous utiliserez la propriété `classList` du DOM.

Mais d'abord, vous devez sélectionner vos classes en utilisant la méthode `querySelector` du DOM et les stocker dans des variables afin qu'elles soient réutilisables.

```js
const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const openModalBtn = document.querySelector(".btn-open");
const closeModalBtn = document.querySelector(".btn-close");
```

## Comment ouvrir la modale

Afin d'afficher la modale, créez une fonction appelée `openModal`. À l'intérieur de cette fonction, vous utiliserez la propriété `classList` du DOM qui accepte différentes méthodes comme `.remove()` et `.add()` pour supprimer la classe `hidden` de `modal` et `overlay`.

```js
const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};
```

Ensuite, vous pouvez utiliser un `eventListener` pour lier cette fonction au bouton d'ouverture de la modale `openModalBtn`. De cette façon, chaque fois que ce bouton est cliqué, la fonction est exécutée, ce qui affiche la modale.

```js
openModalBtn.addEventListener("click", openModal);
```

Maintenant, lorsque vous cliquez sur le bouton "Ouvrir la modale", cela supprimera la classe `hidden` de l'élément modal et vous pourrez voir votre modale.

Voici le résultat :

![Ouvrir la modale](https://www.freecodecamp.org/news/content/images/2022/10/open-modal.gif)

## Comment fermer la modale

Pour fermer la modale, vous allez également créer une fonction appelée `closeModal`. À l'intérieur de la fonction, utilisez la méthode `.add()` pour rajouter la classe `hidden` que vous aviez supprimée.

La propriété `classList` possède également une méthode `add()` que vous utiliserez pour rajouter la classe hidden lorsque vous cliquez sur le bouton `closeModal`. Tout comme vous avez ajouté un `eventListener` au bouton pour ouvrir la modale, vous ferez de même pour le bouton `x` – mais cette fois, vous rajouterez la classe `hidden`.

```js
const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};
```

Pour fermer la modale, ajoutez un `eventListener` au bouton de fermeture pour exécuter la fonction que vous venez d'écrire.

```js
closeModalBtn.addEventListener("click", closeModal);
```

Maintenant, lorsque vous cliquez sur le bouton de fermeture, la fonction rajoutera la classe hidden aux composants modal et overlay, fermant ainsi la modale.

Voici le résultat :

![fermer la modale](https://www.freecodecamp.org/news/content/images/2022/10/close_modal.gif)

Habituellement, les modales sont également fermées lorsque vous cliquez à l'extérieur du conteneur de la modale ou sur le corps de la page Web. Pour ce faire, ajoutez un `eventListener` pour fermer la modale lorsque vous cliquez sur l'overlay.

```js
overlay.addEventListener("click", closeModal);
```

![fermer_modale_quand_overlay_est_clique](https://www.freecodecamp.org/news/content/images/2022/10/close_modal_when_overlay_is_clicked.gif)

## Comment fermer la modale en appuyant sur une touche

En plus de fermer la modale lorsque vous cliquez sur le bouton de fermeture ou sur l'overlay, vous pouvez également attacher un écouteur d'événement pour surveiller les événements du clavier.

Dans ce cas, vous voulez que la modale se ferme lorsque vous appuyez sur la touche `Escape`, tout comme dans l'exemple de la modale de composition de Twitter.

```js
document.addEventListener("keydown");
```

Mais cette fois, le type d'événement que vous voulez n'est pas l'événement `"click"` – vous voulez utiliser l'événement `"keydown"` pour exécuter votre fonction.

Ensuite, vous écrirez une condition qui vérifie si la touche actuellement pressée est la touche `Escape` et si la modale ne contient pas la classe `hidden`. Si elle est ouverte, vous voulez exécuter la fonction `closeModal` (en substance, fermer la modale).

```js
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});
```

Maintenant, quand la modale est ouverte et que vous appuyez sur la touche `<kbd>Esc</kbd>`, elle se fermera.

Et avec cela, vous avez réussi à créer un composant modal avec HTML, CSS et JavaScript et il fonctionne exactement comme prévu. 🥳

Voici le fichier CodePen pour tester cette modale en action :

<iframe height="400" style="width: 100%;" scrolling="no" title="Modal with overlay and blur" src="https://codepen.io/evavic44/embed/zYjjzoV?default-tab=html%2Cresult&theme-id=light" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Consultez le Pen <a href="https://codepen.io/evavic44/pen/zYjjzoV">
  Modal with overlay and blur</a> par Eke (<a href="https://codepen.io/evavic44">@evavic44</a>)
  sur <a href="https://codepen.io">CodePen</a>.
</iframe>

## Conclusion

J'espère sincèrement que vous avez trouvé cet article intéressant ou utile. Si c'est le cas, n'hésitez pas à le partager avec vos amis ou à vous abonner à mon blog pour ne manquer aucune publication future. Merci de m'avoir lu.

[GitHub](https://github.com/evavic44) | [Twitter](https://twitter.com/victorekea) | [Blog](https://eke.hashnode.dev) | [Portfolio](https://victoreke.com)