---
title: Hauteur de ligne Bootstrap
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:18:00.000Z'
originalURL: https://freecodecamp.org/news/bootstrap-row-height
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a99740569d1a4ca2690.jpg
tags:
- name: Bootstrap
  slug: bootstrap
- name: bootstrap 4
  slug: bootstrap-4
seo_title: Hauteur de ligne Bootstrap
seo_desc: 'Bootstrap is one of the fastest ways to, well, bootstrap a project. The
  library includes a lot of helpful CSS utility classes to get a responsive, mobile
  first layout up and running quickly.

  But what if you start adding your own CSS rules to the mix,...'
---

Bootstrap est l'un des moyens les plus rapides pour, bien, démarrer un projet. La bibliothèque inclut de nombreuses classes utilitaires CSS pour obtenir rapidement une mise en page responsive, mobile first.

Mais que se passe-t-il si vous commencez à ajouter vos propres règles CSS, mais qu'elles ne semblent avoir aucun effet sur la mise en page ? Est-ce que Bootstrap écrase vos styles ? Ou autre chose ?

Par exemple, disons que vous voulez augmenter la hauteur d'une ligne et redimensionner une image.

Voici votre HTML :

```html
<div class="container">
  <div id="divheight">
    <div class="row bg-info text-white">
      <div class="col-sm-2 align-middle">
        <img src="https://static-cdn.jtvnw.net/jtv_user_pictures/freecodecamp-profile_image-d9514f2df0962329-300x300.png" </img>
      </div>
      <div class="col-sm-3 align-middle">
        <label>freecodecamp</label>
      </div>
      <div class="col-sm-7 align-middle">
        <label>Greg working on Electron-Vue boilerplate w/ Akira #programming #vuejs #electron</label>
      </div>
    </div>
  </div>
</div>
```

Et le CSS :

```css
#divheight {
  heights: 120px;
}

img {
  width: 50px;
  height: 50px;
}

```

Le problème est que, pour une raison quelconque, la hauteur de la ligne est de 50px comme l'image, et non de 120px :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-47.png)

## Solution

Il y a quelques raisons à cela. Tout d'abord, avez-vous remarqué la faute de frappe ci-dessus ?

Corrigez cela et votre CSS ressemblera à ceci :

```css
#divheight {
  height: 120px;
}

img {
  width: 50px;
  height: 50px;
}
```

Mais votre ligne n'est toujours pas de 120px. Si vous inspectez `#divheight`, vous verrez qu'elle est juste en dessous de 120px :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-48.png)

Au lieu de cibler `#divheight`, descendez à l'élément `div` suivant et ciblez la classe `row` :

```css
.row {
  height: 120px;
}

img {
  width: 50px;
  height: 50px;
}
```

Ensuite, la ligne sera de 120px comme vous vous y attendez :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image-49.png)