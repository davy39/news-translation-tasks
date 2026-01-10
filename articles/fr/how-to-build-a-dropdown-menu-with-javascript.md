---
title: Comment créer un menu déroulant avec JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-09T18:27:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-dropdown-menu-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/how-to-build-a-dropdown-menu-with-javascript.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment créer un menu déroulant avec JavaScript
seo_desc: 'By Victor Eke

  If you use the internet, you''ve likely used a dropdown menu before. They primarily
  serve two purposes: collecting user input in web forms, and implementing action/navigation
  menus in web applications.

  Dropdowns are one of the best ways ...'
---

Par Victor Eke

Si vous utilisez Internet, vous avez probablement déjà utilisé un menu déroulant. Ils servent principalement deux objectifs : collecter les entrées utilisateur dans les formulaires web et implémenter des menus d'action/navigation dans les applications web.

Les menus déroulants sont l'un des meilleurs moyens d'offrir de nombreuses options pour une collection similaire d'éléments sans avoir à compromettre le flux de mise en page général d'une application. En dehors des applications web, ils sont également utilisés dans les logiciels autonomes, les systèmes d'exploitation, et ainsi de suite.

Dans ce guide, vous apprendrez à créer un menu de navigation déroulant en utilisant HTML, CSS et JavaScript.

Voici une capture d'écran de ce que vous allez construire. À la fin de ce guide, j'inclurai le fichier codepen afin que vous puissiez jouer avec.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/dropdown-menu-with-css.png)
_Résultat final du menu déroulant_

Maintenant que nous avons couvert les bases du menu déroulant, discutons des étapes pour en construire un.

## Étape 1 – Ajouter le balisage pour le menu déroulant

Puisque nous utiliserons des icônes dans ce guide, nous devons d'abord les importer. Pour simplifier, nous utiliserons une bibliothèque gratuite appelée [Boxicons](https://boxicons.com/). N'hésitez pas à choisir d'autres alternatives que vous préférez.

Il existe plusieurs façons de [configurer](https://boxicons.com/usage) Boxicons sur votre site. Mais la manière la plus simple est de définir la balise de script dans le `head` de votre fichier HTML, comme ceci :

```html
<head>
   <link 
     href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" 
     rel="stylesheet"
    />
 </head>
```

Après avoir importé les icônes, créez un élément `div` avec une classe `container`. Cet élément contiendra le `button` et le menu déroulant.

À l'intérieur du conteneur, créez un élément bouton et donnez-lui une classe et un id `btn`. Pour le bouton, passez le texte du bouton et l'icône de flèche.

Voici le balisage pour le bouton.

```html
<button class="btn" id="btn">
  Dropdown
  <i class="bx bx-chevron-down" id="arrow"></i>
</button>
```

Ensuite, nous ajouterons le balisage pour le menu déroulant lui-même. Sous la balise bouton, créez un élément `div` et donnez-lui une classe et un id `dropdown`. À l'intérieur de l'élément div, créez une balise `a` pour chaque élément individuel du menu déroulant et passez leurs icônes et textes respectifs.

Voici à quoi ressemble le balisage :

```html
<div class="dropdown" id="dropdown">
  <a href="#create">
    <i class="bx bx-plus-circle"></i>
    Créer Nouveau
  </a>
  <a href="#draft">
    <i class="bx bx-book"></i>
    Tous les brouillons
  </a>
  <a href="#move">
    <i class="bx bx-folder"></i>
    Déplacer vers
  </a>
  <a href="#profile">
    <i class="bx bx-user"></i>
    Paramètres du profil
  </a>
  <a href="#notification">
    <i class="bx bx-bell"></i>
    Notification
  </a>
  <a href="#settings">
    <i class="bx bx-cog"></i>
    Paramètres
  </a>
</div>
```

Voici le résultat.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/dropdown-menu-markup.png)
_Aperçu du balisage du menu déroulant_

Ce n'est pas encore très beau – alors commençons à styliser le menu.

## Étape 2 – Styliser le menu déroulant

Tout d'abord, nous allons réinitialiser la marge et le remplissage par défaut de chaque élément sur la page et stocker certaines valeurs dans des variables afin de pouvoir les réutiliser dans notre fichier CSS. Ensuite, nous donnerons à l'élément body un style global.

```css
@import url(https://fonts.googleapis.com/css?family=Inter:100,200,300,regular,500,600,700,800,900);

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Inter", sans-serif;
  --shadow: rgba(0, 0, 0, 0.05) 0px 6px 10px 0px,
    rgba(0, 0, 0, 0.1) 0px 0px 0px 1px;
  --color: #166e67;
  --gap: 0.5rem;
  --radius: 5px;
}

body {
  margin: 2rem;
  background-color: #b3e6f4;
  font-size: 0.9rem;
  color: black;
}
```

L'étape suivante consiste à styliser le bouton et le conteneur du menu déroulant lui-même. Pour accélérer les choses, je vais expliquer seulement les parties importantes du style.

Copiez le balisage ci-dessous et collez-le dans votre fichier CSS.

```css
.btn {
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  column-gap: var(--gap);
  padding: 0.6rem;
  cursor: pointer;
  border-radius: var(--radius);
  border: none;
  box-shadow: var(--shadow);
  position: relative;
}

.bx {
  font-size: 1.1rem;
}

.dropdown {
  position: absolute;
  width: 250px;
  box-shadow: var(--shadow);
  border-radius: var(--radius);
  margin-top: 0.3rem;
  background: white;
}

.dropdown a {
  display: flex;
  align-items: center;
  column-gap: var(--gap);
  padding: 0.8rem 1rem;
  text-decoration: none;
  color: black;
}

.dropdown a:hover {
  background-color: var(--color);
  color: white;
}
```

Puisque les menus déroulants sont généralement placés au-dessus des éléments, le bouton a été positionné de manière relative et le menu déroulant, de manière absolue. Cela garantit que les deux éléments seront proches l'un de l'autre et que le menu déroulant sera placé au-dessus des éléments. De cette manière, lorsqu'il est basculé, il n'affectera pas le flux de la page.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/dropdown-menu-with-css.png)
_Stylisation du menu déroulant_

Maintenant que le menu déroulant a été stylisé, nous voulons qu'il apparaisse uniquement lorsque le bouton a été cliqué plutôt qu'immédiatement. Pour le masquer, nous utiliserons CSS.

Dans un article précédent que j'ai écrit sur [Comment créer une modale avec JavaScript](https://freecodecamp.org/news/how-to-build-a-modal-with-javascript), nous avons utilisé `display: none` pour masquer l'élément modal initialement de la fenêtre d'affichage. Mais l'inconvénient de l'utilisation de cette propriété était qu'elle n'était pas animable, selon [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animated_properties).

Donc dans ce guide, nous allons suivre une approche différente pour masquer le menu déroulant. Cela implique de combiner les propriétés `visibility` et `opacity` ensemble pour obtenir le résultat souhaité. Cette méthode est celle que [GitHub](https://github.com) utilise pour implémenter son menu déroulant.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/github-dropdown-menu.png)
_Menu déroulant sur GitHub_

À l'intérieur de la classe dropdown que nous avons créée précédemment, ajoutez une propriété de visibilité et donnez-lui une valeur de hidden et définissez l'opacité sur `0`. Cela masquera le menu déroulant de la page.

Pour afficher le modal, nous allons créer une classe séparée appelée `show`. Cette classe contiendra la propriété de visibilité avec une valeur de `visible` et une opacité de `1`. Et nous pouvons injecter cette classe dans le modal en utilisant JavaScript dans un instant.

Voici le code :

```css
.dropdown {
  position: absolute;
  width: 250px;
  box-shadow: var(--shadow);
  border-radius: var(--radius);
  margin-top: 0.3rem;
  background: white;
  transition: all 0.1s cubic-bezier(0.16, 1, 0.5, 1);
    
  transform: translateY(0.5rem);
  visibility: hidden;
  opacity: 0;
}

.show {
  transform: translateY(0rem);
  visibility: visible;
  opacity: 1;
}

.arrow {
  transform: rotate(180deg);
  transition: 0.2s ease;
}
```

En plus du style pour masquer l'élément modal, nous avons ajouté une autre classe pour faire tourner l'icône de flèche lorsque le bouton du menu déroulant est cliqué.

## Étape 3 – Ajouter la fonctionnalité du menu déroulant

Pour commencer, stockons nos éléments respectifs dans des variables afin qu'ils soient réutilisables.

```js
const dropdownBtn = document.getElementById("btn");
const dropdownMenu = document.getElementById("dropdown");
const toggleArrow = document.getElementById("arrow");
```

L'étape suivante consiste à créer une fonction pour basculer la classe `show` sur l'élément du menu déroulant et pour faire tourner la flèche du menu déroulant lorsque le bouton est cliqué. Nous nommerons cette fonction `toggleDropdown`.

```js
const toggleDropdown = function () {
  dropdownMenu.classList.toggle("show");
  toggleArrow.classList.toggle("arrow");
};
```

Ensuite, nous pouvons appeler cette fonction sur le bouton du menu déroulant en utilisant la méthode `addEventListener`. Ainsi, chaque fois que le bouton est cliqué, il déclenchera la fonction qui contrôle l'affichage et le masquage du menu déroulant.

```js
dropdownBtn.addEventListener("click", function (e) {
  e.stopPropagation();
  toggleDropdown();
});
```

Si vous avez remarqué, nous avons ajouté une méthode `stopPropagation()` à l'intérieur de la fonction du menu déroulant. Cela empêche la fonction de l'élément bouton d'être transmise à l'élément parent, empêchant ainsi la fonction de s'exécuter deux fois. Vous comprendrez mieux cela dans la section suivante.

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/toggle-dropdown-menu-.gif)
_basculer le menu déroulant_

## Comment fermer le menu déroulant lorsqu'un élément DOM est cliqué

Les menus déroulants sont généralement fermés de quatre manières différentes :

* En cliquant sur le bouton qui l'active
* En cliquant sur l'un de ses éléments enfants
* En cliquant à l'extérieur du menu (sur le body)
* En appuyant sur les touches Échap ou flèche vers le bas

Mais pour ce guide, concentrons-nous sur les trois premières.

Tout d'abord, nous sélectionnerons l'élément racine `<html>` en utilisant `document.documentElement`. Et comme avant, nous passerons la fonction `toggleDropdown()` à l'intérieur.

Mais cette fois, nous voulons définir une condition qui vérifie si le menu déroulant contient la classe `show` ou non. Ce n'est que lorsqu'il la contient que nous voulons déclencher la fonction de fermeture.

```js
document.documentElement.addEventListener("click", function () {
  if (dropdownMenu.classList.contains("show")) {
    toggleDropdown();
  }
});
```

Voici le résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/close-dropdown-when-dom-element-is-clicked.gif)
_Fermer le menu déroulant lorsqu'un élément DOM est cliqué_

Et c'est ainsi que vous créez un menu déroulant avec JavaScript. Ci-dessous se trouve le fichier codepen pour tester ce menu déroulant en action.

<iframe height="400" style="width: 100%;" scrolling="no" title="Dropdown menu" src="https://codepen.io/evavic44/embed/eYKQJjJ?default-tab=html%2Cresult&theme-id=light" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/evavic44/pen/eYKQJjJ">
  Dropdown menu</a> by Eke (<a href="https://codepen.io/evavic44">@evavic44</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

## Conclusion

J'espère sincèrement que vous avez trouvé cet article intéressant ou utile. Si c'est le cas, partagez-le avec vos amis ou abonnez-vous à mon blog pour ne manquer aucune future publication. Merci d'avoir lu.

[GitHub](https://github.com/evavic44) | [Twitter](https://twitter.com/victorekea) | [Blog](https://eke.hashnode.dev) | [Portfolio](https://victoreke.com)