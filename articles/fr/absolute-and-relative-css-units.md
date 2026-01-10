---
title: Que sont les unités absolues et relatives en CSS ? Explications avec exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-30T21:19:17.000Z'
originalURL: https://freecodecamp.org/news/absolute-and-relative-css-units
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/absolute-relative-units-1.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Que sont les unités absolues et relatives en CSS ? Explications avec exemples
seo_desc: 'By Dillion Megida

  In CSS, we categorize measurement units as either absolute or relative units. In
  this article, I''ll explain what these categories are with examples of units that
  fall under each of them.

  CSS Measurement Units

  You can use different m...'
---

Par Dillion Megida

En CSS, nous classons les unités de mesure comme étant soit des unités absolues, soit des unités relatives. Dans cet article, j'expliquerai ce que sont ces catégories avec des exemples d'unités pour chacune d'elles.

## Unités de mesure CSS

Vous pouvez utiliser différentes unités de mesure en CSS. Vous utilisez ces unités avec des valeurs de longueur ou de taille et elles peuvent être associées à des propriétés comme `font-size`, `width`, `border-width`, `padding`, et bien d'autres encore.

Lorsque vous utilisez `font-size`, vous spécifiez une valeur pour la taille de la police.

Vous spécifiez également une longueur pour la `width` d'un élément.

Et avec le padding, vous spécifiez une longueur.

Ces valeurs ont des unités qui aident CSS à comprendre quelle longueur ou taille leurs éléments doivent avoir à l'écran. Et comme je l'ai mentionné au début de l'article, nous pouvons classer ces valeurs en unités **absolues** et **relatives**.

## Que sont les unités absolues ?

Les unités absolues spécifient une valeur de longueur fixe. Peu importe si la largeur ou la hauteur de l'écran change, la valeur restera fixe.

Les unités qui entrent dans cette catégorie comprennent :

`mm` (millimètres)
`cm` (centimètres) : 10mm font 1cm
`in` (pouces) : 2,54cm font 1in
`pt` (points) : 1/72in fait 1pt
`pc` (picas) – 12pt font 1pc
`px` (pixel) – 0,75pt fait 1px

Pour les supports haute résolution comme les documents imprimés, il est recommandé d'utiliser `cm`, `mm` ou `pt`. Pour les pages web, `px` est l'unité recommandée.

Voici un exemple :

```html
<div>Hello</div>
```

Et le CSS :

```css
div {
  border: 2px solid black;
  width: 300px;
}
```

Sur un plein écran, voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-475.png)

Lorsque l'écran devient plus petit, la `div` conserve toujours une largeur de `300px` car il s'agit d'une valeur fixe :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-476.png)

La largeur du bloc n'est relative à rien, donc quels que soient les autres changements de taille, le DOM va toujours essayer de maintenir cette largeur de `300px` autant que possible.

## Que sont les unités relatives ?

Contrairement aux unités absolues, les unités relatives ne sont pas fixes. Leurs valeurs sont « relatives » à une autre valeur. Cela signifie que lorsque cette autre valeur change, la valeur de l'unité relative change également.

Les unités qui entrent dans cette catégorie comprennent :
`%` (pourcentage) : relatif à la taille de l'élément parent
`em` (font size) : relatif à la taille de la police
`rem` (root `em`) : relatif à la taille de la police de l'élément racine
`vw` (viewport width) : relatif à la largeur du viewport
`vh` (viewport height) : relatif à la hauteur du viewport

Vous pouvez voir comment les valeurs avec ces unités sont relatives à une autre valeur. Voici un exemple :

```html
<div class='container'>
    <div class='card'>
        Hello
    </div>
</div>
```

Et le CSS :

```css
.container {
  width: 300px;
  border: 2px solid black;
  padding: 20px;
}

.card {
  width: 60%;
  border: 2px solid green;
  padding: 10px;
}
```

Le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-478.png)

D'après ce qui précède, vous voyez que la div `.container` fait `300px` (fixe). Mais la div `.card` a une largeur de `60%`, ce qui signifie `60%` de la largeur de son élément parent. Vous avez donc **60% de 300px**, et cela donne à la div `.card` une largeur de `180px`.

Si la largeur de la div `.container` change, la div `.card` changera également.

Voici un autre exemple utilisant `vw` :

```css
.container {
  width: 100vw;
  background-color: blue;
  padding: 10px;
}

.card {
  width: 80vw;
  height: 100vh;
  background-color: red;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-479.png)

Ici, vous pouvez voir que la div `.container` a une largeur de `100vw`, ce qui signifie 100% de la largeur du viewport. La div `.card` a une largeur de `80vw` et une hauteur de `90vh`, ce qui signifie 80% de la largeur du viewport et 90% de la hauteur du viewport.

Lorsque vous réduisez la taille du viewport, ces valeurs relatives s'ajustent :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-481.png)

Ici, j'ai réduit la largeur et la hauteur du viewport, et ainsi les valeurs relatives appliquées sur `.container` et `.card` sont également ajustées.

L'unité `em` peut signifier deux choses : dans le contexte de la typographie, elle signifie « **relatif à la taille de police de l'élément parent** » et dans le contexte des propriétés de taille comme les largeurs et les hauteurs, elle signifie « **relatif à la taille de police de l'élément actuel** ».

Voyons un exemple :

```html
<div class='container'>
    <p class='text'>I am a text</p>
</div>
```

Et le CSS :

```css
.container {
  font-size: 16px;
}

.text {
  font-size: 2em;
  width: 3em;
  border: 1px solid red;
  padding: 10px;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-482.png)

Je vais expliquer ce qui s'est passé dans le résultat ci-dessus.

La div `.container` a une `font-size` de `16px`.

Le p `.text` a une `font-size` de `2em`. Puisqu'il s'agit de typographie, cela signifie « **la taille de la police est 2 fois la taille de police du parent** », elle est donc de `32px`.

La balise p a également une `width` de `3em`. Comme cette propriété ne relève pas de la typographie, cela signifie « **la largeur est 3 fois la taille de la police de l'élément lui-même** ». La `font-size` est de `32px`, donc la `width` sera de `96px`.

`rem` d'un autre côté, dans les deux contextes, signifie « **relatif à la taille de police de l'élément racine** ». Voici un exemple :

```html
<div class='container'>
    <p class='text'>I am a text</p>
</div>
```

Et le CSS :

```css
html {
  font-size: 20px;
}

.container {
  width: 5rem;
  border: 1px solid green;
}

.text {
  font-size: 0.5rem;
  width: 2rem;
  padding: 1rem;
  border: 1px solid red;
}
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-484.png)

L'élément racine a une `font-size` de `20px`. Voici les calculs pour les unités relatives dans le CSS :

* La div `.container` a une `width` de `5rem` ce qui correspond à **5 fois 20px**, soit **100px**
* Le p `.text` a :
    * une `font-size` de `0.5rem` ce qui correspond à **1/2 de 20px**, soit **10px**
    * une `width` de `2rem` ce qui correspond à **2 fois 20px**, soit **40px**
    * un `padding` de `1rem` ce qui correspond à **1 fois 20px**, soit **20px**


## Conclusion

Les unités sont une valeur de mesure en CSS, ce qui aide CSS à déterminer quelles valeurs de longueur/taille seront appliquées aux propriétés basées sur la taille.

Dans cet article, nous avons examiné les deux catégories d'unités que sont les unités **absolues** et **relatives**.

En résumé, les unités **absolues** sont utilisées pour des valeurs fixes. Ces valeurs ne changent pas, quels que soient les changements de taille des éléments environnants ou du viewport.

Les unités **relatives**, quant à elles, sont utilisées pour des valeurs qui sont relatives à — ou dépendent de — valeurs d'autres éléments (généralement le parent, le viewport ou l'élément racine).

Merci de m'avoir lu !