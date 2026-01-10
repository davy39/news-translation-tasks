---
title: Sélecteur CSS Hover Expliqué (avec Exemple)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-29T17:26:00.000Z'
originalURL: https://freecodecamp.org/news/hover-selector
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e6a740569d1a4ca3cf6.jpg
tags:
- name: CSS
  slug: css
seo_title: Sélecteur CSS Hover Expliqué (avec Exemple)
seo_desc: 'The CSS :hover selector is one of many pseudo-classes that are used to
  style elements. :hover is used to select elements that users hover their cursor
  or mouse over. It can be used on all elements, not only on links.

  When used to style links, :hover ...'
---

Le sélecteur CSS `:hover` est l'une des nombreuses pseudo-classes utilisées pour styliser des éléments. `:hover` est utilisé pour sélectionner les éléments sur lesquels les utilisateurs passent leur curseur ou leur souris. Il peut être utilisé sur tous les éléments, pas seulement sur les liens.

Lorsqu'il est utilisé pour styliser des liens, `:hover` est souvent associé aux sélecteurs `:link`, `:visited` et `:active` qui stylisent respectivement les liens non visités, visités et actifs.

Si les règles `:link` et `:visited` sont dans la définition CSS, `:hover` doit venir après elles. Sinon, les styles de la règle `:hover` ne seront pas appliqués à l'élément sélectionné.

**Syntaxe :**

```css
a:hover {
  /* Déclarations CSS */
}
```

Le sélecteur hover n'applique les styles fournis dans la règle que lorsqu'un élément entre dans l'état de survol. Cela se produit généralement lorsque l'utilisateur passe sa souris sur l'élément.

```css
button {
  color: white;
  background-color: green;
}

button:hover {
  background-color: white;
  border: 2px solid green;
  color: green;
}
```

Dans l'exemple ci-dessus, le style normal du bouton est un texte blanc sur un bouton vert. Lorsque l'utilisateur passe sa souris sur le bouton, la règle avec le sélecteur `:hover` devient active et le style du bouton change.

Notez que `:hover` peut poser problème sur les écrans tactiles – différentes implémentations matérielles et de navigateurs mobiles peuvent déclencher la pseudo-classe dans certains cas et pas dans d'autres. Assurez-vous de tester minutieusement les éléments avec `:hover` dans autant de navigateurs mobiles et d'appareils différents que possible.