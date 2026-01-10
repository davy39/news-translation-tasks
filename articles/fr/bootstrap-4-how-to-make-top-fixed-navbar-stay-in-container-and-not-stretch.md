---
title: 'Bootstrap 4 : Comment faire en sorte que la navbar fixe reste dans le conteneur
  et ne s''étire pas ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:17:00.000Z'
originalURL: https://freecodecamp.org/news/bootstrap-4-how-to-make-top-fixed-navbar-stay-in-container-and-not-stretch
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a9e740569d1a4ca26b6.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: bootstrap 4
  slug: bootstrap-4
- name: toothbrush
  slug: toothbrush
seo_title: 'Bootstrap 4 : Comment faire en sorte que la navbar fixe reste dans le
  conteneur et ne s''étire pas ?'
seo_desc: "There are many ways to make a fixed navbar stay inside a parent's div container.\
  \ We'll go over the most straightforward one here.\nImagine you have the following\
  \ code, modified slightly from the Bootstrap docs:\n<div class=\"container\">\n\
  \  <nav class=\"na..."
---

Il existe de nombreuses façons de faire en sorte qu'une navbar fixe reste à l'intérieur d'un conteneur parent `div`. Nous allons passer en revue la méthode la plus simple ici.

Imaginez que vous avez le code suivant, légèrement modifié à partir de la [documentation Bootstrap](https://v4-alpha.getbootstrap.com/components/navbar/#collapsible-content) :

```html
<div class="container">
  <nav class="navbar navbar-fixed-top navbar-inverse bg-inverse">
    <button class="navbar-toggler hidden-lg-up" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Basculer la navigation">
    </button>
    <div class="collapse navbar-toggleable-md" id="navbarResponsive">
      <a class="navbar-brand" href="#">
        <img src="" width="30" height="30" class="d-inline-block align-top" alt="">Navbar
      </a>
      <ul class="nav navbar-nav float-md-right">
        <li class="nav-item active">
          <a class="nav-link" href="#">Accueil
            <span class="sr-only">(actuel)</span>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Lien</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Lien</a>
        </li>
      </ul>
    </div>
  </nav>
  <div class="next"></div>
  bonjour
</div>
```

```css
div.next {
  background-color: lightblue;
  width: 100%;
  height: 60rem;
}
```

Et votre page ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1.png)

## Solutions

Bien que la documentation indique "Les navbars et leur contenu sont fluides par défaut. Utilisez des conteneurs optionnels pour limiter leur largeur horizontale", la solution la plus simple est d'utiliser CSS pour définir directement la largeur de la navbar :

```css
div.next {
  background-color: lightblue;
  width: 100%;
  height: 60rem;
}

.container {
  padding: 0px;
}

nav.navbar {
  width: inherit;
  top: 0%;
  left: 50%;
  transform: translateX(-50%);
}
```

En ajoutant des règles ciblant `.container` et `nav.navbar`, votre navbar a maintenant la même largeur que le conteneur parent :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-46.png)