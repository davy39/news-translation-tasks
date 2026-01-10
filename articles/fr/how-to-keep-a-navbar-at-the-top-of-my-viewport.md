---
title: Comment garder une barre de navigation en haut de la vue ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:12:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-a-navbar-at-the-top-of-my-viewport
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aab740569d1a4ca2701.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
- name: UI
  slug: ui
seo_title: Comment garder une barre de navigation en haut de la vue ?
seo_desc: 'If you''re working on the Product Landing Page project and are having trouble
  with some of the user stories, you''re not alone.

  User story #13 gives a lot of people trouble. It reads:


  The navbar should always be at the top of the viewport.


  Non-fixed,...'
---

Si vous travaillez sur le projet [Page de destination de produit](https://www.freecodecamp.org/learn/responsive-web-design/responsive-web-design-projects/build-a-product-landing-page) et que vous avez des difficultés avec certaines des histoires utilisateur, vous n'êtes pas seul.

L'histoire utilisateur #13 pose problème à beaucoup de gens. Elle dit :

> La barre de navigation doit toujours être en haut de la vue.

### Barre de navigation normale, non fixe

Imaginez que vous avez le HTML suivant :

```html
...
<header id="header">
  <img src="https://static1.squarespace.com/static/54d3e88ce4b0be204d0da36a/t/566f5b70bfe873371e44c7b0/1525197822184/" alt="logo" id="header-img">
  <nav id="nav-bar">
    <ul> 
      <li><a href="#about-us" class="nav-link">À propos</a></li>
      <li><a href="#videos" class="nav-link">Démo</a></li>
      <li><a href="#photos" class="nav-link">Galerie photo</a></li>
      <li><a href="#contact-us" class="nav-link">Contact</a></li>
  </nav>
</header>
...
```

Mais lorsque vous faites défiler la page vers le bas, la barre de navigation finit par quitter la vue :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Peek-2020-05-25-17-46.gif)

### Comment créer une barre de navigation fixe

Pour créer une barre de navigation fixe, ou une barre de navigation qui reste toujours en haut de la vue même lorsque vous faites défiler la page vers le bas, il y a quelques choses que vous devez faire.

Tout d'abord, ciblez l'en-tête et fixez-le à la page avec la règle suivante :

```css
header {
  position: fixed; /* Position fixe */
}
```

Vous remarquerez que la barre de navigation se contracte à sa largeur par défaut, alors définissez sa largeur à la largeur totale de la page :

```css
header {
  position: fixed;
  width: 100%;
}
```

Selon les propriétés `display` des autres éléments, vous devrez peut-être définir manuellement les positions `top` et `left` de la barre de navigation :

```css
header {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
}
```

Ensuite, il vous suffit d'appliquer un peu de style supplémentaire pour que tout ait une belle apparence :

```css
header {
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  background-color: #cc0000;
  color: white;
  font-family: 'Exo 2', sans-serif;
  padding: 1em;
}
```

### Barre de navigation fixe — le résultat

Après cela, votre barre de navigation devrait rester visible même lorsque vous faites défiler la page vers le bas :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Peek-2020-05-25-17-45.gif)