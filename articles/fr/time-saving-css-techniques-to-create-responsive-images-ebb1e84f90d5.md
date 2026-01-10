---
title: Techniques CSS pour gagner du temps et créer des images responsives
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T19:18:06.000Z'
originalURL: https://freecodecamp.org/news/time-saving-css-techniques-to-create-responsive-images-ebb1e84f90d5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aVzJTznRRfP1lM7AXe9yLw.jpeg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: responsive design
  slug: responsive-design
- name: 'tech '
  slug: tech
seo_title: Techniques CSS pour gagner du temps et créer des images responsives
seo_desc: 'By Adrien Zaganelli

  As a web developer, there is a high probability that you have encountered the two
  enemies of this article: images and deadlines. Sometimes, for some reasons, your
  images won’t fit the layout and you don’t want to wrap your head ar...'
---

Par Adrien Zaganelli

En tant que développeur web, il est très probable que vous ayez déjà rencontré les deux ennemis de cet article : les **images** et les **délais**. Parfois, pour une raison ou une autre, vos images ne s'adaptent pas à la mise en page et vous ne voulez pas passer des heures à essayer de résoudre ce problème.

Cette situation m'est arrivée de nombreuses fois et j'ai appris de mes erreurs. Plus de hacks de magie noire — voici mes cinq techniques préférées pour gérer le redimensionnement des images.

### La méthode "OMG J'EN AI BESOIN TOUT DE SUITE"

Il est 17h un vendredi, vous devez finir cette page, mais les images ne s'adaptent pas à la mise en page. Il est temps d'utiliser votre tour de magie !

```css
.myImg {
  background-image: url("my-image.png");
  background-size: cover;
}
```

Ça vous dit quelque chose ? Nous l'avons tous fait au moins une fois, n'est-ce pas ? Cela ne vous donne pas l'impression de tricher ?

Utiliser les propriétés `background` est très utile, elles fonctionnent simplement. Pourtant, rappelez-vous que vous devriez les utiliser uniquement pour les images non contenues ou comme remplacement de texte et dans [certains cas particuliers](https://stackoverflow.com/a/1469139).

### La méthode du futur

Et si je vous disais que ce genre de magie existe aussi pour les éléments `<img>` ? Dites "hi" à la propriété `object-fit` — qui fonctionne aussi pour les vidéos, soit dit en passant !

```css
.myImg {
  object-fit: cover;
  width: 320px;
  height: 180px;
}
```

C'est tout, les amis ! Voyez comment, lorsque nous récupérons la valeur conviviale `cover`, nous pouvons aussi utiliser `contain`.

#### **Okay, quel est le piège ?**

Malheureusement, `object-fit` ne fonctionne pas sur IE et les anciennes versions de Safari, mais il existe un [polyfill](https://github.com/bfred-it/object-fit-images/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*d0wZwFpXGiAYH9_NrJCroA.png)
_source : [https://css-tricks.com/almanac/properties/o/object-fit/#article-header-id-4](https://css-tricks.com/almanac/properties/o/object-fit/#article-header-id-4" rel="noopener" target="_blank" title=")_

%[https://codepen.io/adri_zag/pen/VBQJYg]

### La méthode "Netflix"

Vous pourriez penser "beau truc, mec, encore une méthode qui ne fonctionne pas dans les anciens navigateurs comme IE ?". Ne vous inquiétez pas, celle-ci fonctionne partout et c'est ma préférée ! Vous devrez envelopper votre image avec un parent rembourré en relatif.

Nous allons conserver le ratio de l'image avec un pourcentage sur la propriété `padding`. Votre image sera un enfant absolu en pleine taille.

Le code ressemble à ceci :

```css
.wrapper {
  position: relative;
  padding-top: 56.25%; /* Ratio 16:9 */
}
img {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: auto;
}
```

"Hey mec, ça a l'air compliqué."

Une fois que vous avez compris le concept, la technique est simple et [largement utilisée](https://www.w3schools.com/howto/howto_css_aspect_ratio.asp). Netflix l'utilise !

![Image](https://cdn-media-1.freecodecamp.org/images/1*rTrhAIVolZR2oQh2ou1jXg.png)
_Regardez les noms des classes !_

Une petite démonstration :

%[https://codepen.io/adri_zag/pen/BPrejO]

### La méthode simple

Vous connaissez peut-être déjà celle-ci :

```css
img {
  height: auto;
  width: 100%;
/* encore plus de contrôle avec max-width */
  max-width: 720px;
}
```

Si votre mise en page n'est pas trop compliquée, cela fonctionne dans la plupart des cas.

%[https://codepen.io/adri_zag/pen/LBQvwy]

### La méthode performance (Avancé)

Par performance, j'entends les temps de chargement. Une grande image héro peut tout gâcher et rendre votre page lente, surtout sur mobile.

Saviez-vous que dans les [navigateurs modernes](https://caniuse.com/#feat=srcset), vous pouvez changer la source d'une image en fonction de la largeur de votre page ? C'est pour cela que `srcset` a été créé !

Vous pouvez les combiner avec la balise HTML 5 `[<picture>](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)`, qui se dégrade élégamment avec une `<img>`.

```css
<picture>
  <source media="(max-width: 799px)" srcset="elva-480w.jpg">
  <source media="(min-width: 800px)" srcset="elva-800w.jpg">
  <img src="elva-800w.jpg">
</picture>
```

%[https://codepen.io/adri_zag/pen/pZLBpx]

### Pour résumer

1. Utilisez `background-image` si votre image ne fait pas partie du contenu de la page.
2. Utilisez `object-fit` si vous ne vous souciez pas d'IE.
3. La technique du conteneur rembourré, utilisée par Netflix, fonctionne partout.
4. Dans la plupart des cas, ajoutez simplement `height: auto;` dans votre CSS.
5. Si vous avez besoin de temps de chargement rapides, utilisez `srcset` pour charger des images plus petites sur mobile.