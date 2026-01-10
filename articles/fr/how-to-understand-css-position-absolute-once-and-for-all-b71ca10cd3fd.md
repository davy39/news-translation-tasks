---
title: Comment comprendre CSS Position Absolute une fois pour toutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:30:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-css-position-absolute-once-and-for-all-b71ca10cd3fd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3ydATM3NxrGI8Bz0T6NWXQ.gif
tags:
- name: code
  slug: code
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment comprendre CSS Position Absolute une fois pour toutes
seo_desc: 'By Marina Ferreira

  Stop losing your elements on the screen by understanding how an object figures where
  it is supposed to sit


  Positioning an element absolutely is more about the element''s container position
  than its own. To be able to position itsel...'
---

Par Marina Ferreira

#### Arrêtez de perdre vos éléments à l'écran en comprenant comment un objet détermine où il doit se situer

![Image](https://cdn-media-1.freecodecamp.org/images/UiuGXOBbEzwyUMEnynyr4s8mfhpGIds2RQCo)

Positionner un élément de manière absolue concerne davantage la position du conteneur de l'élément que celle de l'élément lui-même. Pour pouvoir se positionner, il doit savoir quel div parent il va prendre comme référence.

Le code ci-dessous montre quatre divs imbriquées. `.box-1` à `.box-3` sont centrées uniquement par `display: flex` et `margin: auto`. `.box-4` n'a pas de `margin` définie et se situe à sa position par défaut dans le flux du document.

```
<body>  <div class="box-1">    <div class="box-2">      <div class="box-3">        <div class="box-4"></div>      </div>    </div>  </div></body>
```

La propriété `position` n'est pas définie pour tous les éléments.

```
body {  display: flex;}
```

```
.box-1,.box-2,.box-3 {  display: flex;  margin: auto;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/u9GyvXp81914z3hJb5bSL3rcjE62v4ZKOnIn)
_.box-4 position par défaut_

Pour pouvoir se positionner, un élément doit connaître deux choses :

* les coordonnées pour sa position `x` et `y` définies par `top`, `right`, `bottom`, `left`
* quel parent il va prendre comme référence

En appliquant `position: absolute` à `.box-4`, l'élément est retiré du `[flux normal du document](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Normal_Flow)`. Comme ses coordonnées ne sont pas définies, il reste simplement à la position par défaut qui est le coin supérieur gauche de son div parent.

![Image](https://cdn-media-1.freecodecamp.org/images/fGJYLQ7rKPWPOZj3qzsp-nxyBUvTRbiSfMYe)
_.box-4 position absolue sans décalage._

En définissant `top: 0` et `left: 0`, l'élément doit alors savoir quel parent il va considérer comme point de référence. Pour être une référence, l'élément doit être positionné à l'écran avec `position: relative`. `.box-4` demande alors à ses divs parents s'ils sont positionnés. Tout d'abord, il demande à `.box-3` et obtient `Non, je ne suis pas positionné.` comme réponse. Il en va de même pour `.box-2` puis `.box-1`, puisque tous ont `position: unset`.

Comme `.box-4` n'a pas pu trouver de parent positionné, il se positionne par rapport au `body`. Cet élément est toujours positionné à l'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/tjeIL8YkyGBlzTpwCapPcQTfOptpdBXzWc2U)
_.box-4 position absolue. Les divs parents ne sont pas positionnés._

Si nous définissons `position: relative` pour `.box-1`, lorsque `.box-4` lui demande : `Es-tu positionné ?`, il obtient `Oui, je le suis.` comme réponse. Et alors `.box-4` sera positionné par rapport à `.box-1` :

![Image](https://cdn-media-1.freecodecamp.org/images/OgWq2g7Wm468076IPANHhE7HIYODqUQkUpAv)
_.box-4 position absolue, .box-1 position relative._

Il en va de même pour `.box-2` et `.box-3`.

**L'élément positionné de manière absolue se positionnera par rapport à l'ancêtre positionné le plus proche.**

Dès qu'il trouve un ancêtre positionné, la position des éléments au-dessus de celui-ci n'est plus pertinente. Les images ci-dessous montrent la disposition lors de la définition de `position: relative` pour `.box-2` et `.box-3`, respectivement :

![Image](https://cdn-media-1.freecodecamp.org/images/rBN0SYpLuSJUUnxJMPu4N0TguV3gNYBQ30Vr)

![Image](https://cdn-media-1.freecodecamp.org/images/eYzaYiMTTqnqSqZHYIs3g6q6uVbOmO0GX6IN)
_.box-4 position absolue, .box-2 et .box-3 position relative, respectivement._

Vous pouvez également trouver une explication vidéo sur [Code Sketch Channel](https://youtu.be/VFt_n4M9Vyk) ?.

Merci d'avoir lu ! F44BF3FB

_Publié à l'origine sur [marina-ferreira.github.io](https://marina-ferreira.github.io/tutorials/css/position-absolute/)._

![Image](https://cdn-media-1.freecodecamp.org/images/qKShNDloz66ZcWplME6mkPXlYDLYUhs6bxsC)