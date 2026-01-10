---
title: Tutoriel HTML Make It Blink – Comment utiliser la balise Blink, avec des exemples
  de code
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-07-27T23:21:14.000Z'
originalURL: https://freecodecamp.org/news/make-it-blink-html-tutorial-how-to-use-the-blink-tag-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/blink-1.jpg
tags:
- name: animations
  slug: animations
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Tutoriel HTML Make It Blink – Comment utiliser la balise Blink, avec des
  exemples de code
seo_desc: 'In the earlier days of the web, HTML elements like the blink tag were native
  ways to add some animation effects to liven up a webpage. How can we use those animations
  today to add flare to our websites and apps?


  What is the HTML tag blink?

  How do yo...'
---

Dans les premiers jours du web, les éléments HTML comme la balise blink étaient des moyens natifs d'ajouter des effets d'animation pour dynamiser une page web. Comment pouvons-nous utiliser ces animations aujourd'hui pour ajouter de l'éclat à nos sites web et applications ?

* [Qu'est-ce que la balise HTML blink ?](#heading-questce-que-la-balise-html-blink)
* [Comment utiliser la balise blink ?](#heading-comment-utiliser-la-balise-blink)
* [Pouvez-vous encore utiliser la balise blink ?](#heading-pouvez-vous-encore-utiliser-la-balise-blink)
* [Recréer la balise blink avec des animations CSS](#heading-recreer-la-balise-blink-avec-des-animations-css)

%[https://www.youtube.com/watch?v=-gU-gkfEA1Q]

## Qu'est-ce que la balise HTML blink ?

La balise [blink](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blink) (`<blink>`) est une balise HTML obsolète qui fait clignoter lentement le contenu de cette balise.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/google-search-blink.gif)
_Recherche Google de "blink tag"_

Cela, ainsi que d'autres balises obsolètes comme la balise [marquee](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/marquee) (`<marquee>`), étaient un moyen facile d'ajouter des effets d'animation simples à votre site.

## Comment utiliser la balise blink ?

Étant donné que la balise blink était un élément HTML simple, vous l'utilisiez directement en ligne avec votre contenu.

Par exemple, si vous vouliez que le mot "blink" dans blink-182 clignote, vous écriviez le HTML suivant :

```html
<p>
  <blink>blink</blink>-182
</p>
```

## Pouvez-vous encore utiliser la balise blink ?

Comme vous l'avez peut-être remarqué dans le gif ci-dessus, cette balise est obsolète.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/html-blink-browser-compatability.jpg)
_Compatibilité des navigateurs avec la balise blink_

Cela signifie que vous ne pouvez pas utiliser la balise HTML blink elle-même. Cependant, cela ne devrait pas nous empêcher de la recréer dans toute sa gloire clignotante.

_Note : la balise Blink a été dépréciée en raison de problèmes d'accessibilité. Veuillez [faire vos recherches](https://en.wikipedia.org/wiki/Blink_element#Usability_and_accessibility) avant d'essayer d'utiliser une solution qui fournit le même effet, car nous devrions tous faire un effort pour rendre nos projets aussi inclusifs que possible._

## Recréer la balise blink avec des animations CSS

Dans le monde du développement web d'aujourd'hui, les animations sont généralement gérées avec CSS ou JavaScript. En utilisant les animations CSS, nous pouvons recréer notre balise blink avec quelques lignes et être de retour en affaires.

Avec le CSS suivant :

```css
.blink {
  animation: blink 1s steps(1, end) infinite;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

```

Vous pouvez ajouter la classe `.blink` à n'importe quel élément HTML pour le faire clignoter.

```
<p>
  <span class="blink">blink</span>-182
</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/html-blink-effect.gif)
_Effet de clignotement HTML CSS_

## Moderniser la balise blink

Nous sommes en 2020, que se passerait-il si nous voulions quelque chose de plus fluide ?

Pour commencer, nous pouvons faire en sorte que l'animation s'estompe en supprimant les `steps` des définitions d'animation.

```css
.blink {
  animation: blink 1s infinite;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/css-blink-fade.gif)
_Effet de fondu clignotant_

Ou que se passerait-il si nous voulions le faire s'estomper comme un effet de science-fiction ?

```
.blink {
  animation: blink 3s infinite;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    color: blue;
  }
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/css-scfifi-fade.gif)
_Effet de fondu clignotant CSS sci-fi_

Ou même un bel effet de croissance et de fondu.

```css
.blink {
  animation: blink 3s infinite;
}

@keyframes blink {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
    transform: scale(2);
  }
  51% {
    opacity: 0;
    transform: scale(0);
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/css-grow-fade.gif)
_Effet de croissance et de fondu clignotant CSS_

## Prendre le contrôle des animations avec CSS

Bien que vous ne puissiez peut-être pas utiliser la balise blink, vous avez toujours beaucoup d'options. CSS offre une tonne d'options d'animation de manière native, donc que vous souhaitiez recréer votre passe-temps HTML préféré ou [recréer la séquence de titre d'Alien](https://codepen.io/colbyfayock/pen/aEqsL), les possibilités sont virtuellement illimitées.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e9f3fb Inscription à ma newsletter</a>
    </li>
  </ul>
</div>