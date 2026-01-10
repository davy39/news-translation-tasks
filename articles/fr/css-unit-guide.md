---
title: 'Guide des unités CSS : CSS em, rem, vh, vw, et plus, expliqués'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-03T00:16:00.000Z'
originalURL: https://freecodecamp.org/news/css-unit-guide
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cd8740569d1a4ca347f.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: 'Guide des unités CSS : CSS em, rem, vh, vw, et plus, expliqués'
seo_desc: 'Many CSS properties like width, margin, padding,  and font-size take a
  length, and CSS has many different ways to express length.

  In CSS, length is a number an a unit with no whitespace. For example, 5px, 0.9em,
  and so on.

  There are two general kinds...'
---

De nombreuses propriétés CSS comme `width`, `margin`, `padding`, et `font-size` prennent une longueur, et CSS a de nombreuses façons différentes d'exprimer la longueur.

En CSS, la longueur est un nombre et une unité sans espace. Par exemple, `5px`, `0.9em`, et ainsi de suite.

Il existe deux types généraux d'unités utilisées pour la longueur et la taille en CSS : absolues et relatives.

## Unités de longueur absolues

Les unités de longueur absolues sont basées sur une unité physique réelle et sont généralement considérées comme étant de la même taille sur tous les appareils. Cependant, selon la taille et la qualité de votre écran, ou les paramètres de votre navigateur ou de votre système d'exploitation, il peut y avoir quelques exceptions.

Voici quelques unités de longueur absolues courantes en CSS :

### `px`

Les pixels, ou `px`, sont l'une des unités de longueur les plus courantes en CSS.

En CSS, 1 pixel est [formellement défini](https://drafts.csswg.org/css-values/#reference-pixel) comme 1/96 de pouce. Toutes les autres unités de longueur absolues sont basées sur cette définition d'un pixel.

Mais lorsque cette norme a été initialement formulée, la plupart des moniteurs avaient une résolution de 1024 x 768 et un DPI (points par pouce) de 96.

Les écrans des appareils modernes ont des résolutions et des DPI beaucoup plus élevés, donc une ligne de 96 pixels de long peut ne pas mesurer exactement 1 pouce, selon l'appareil.

Même si la taille en pixels peut varier selon les appareils, il est généralement considéré comme préférable d'utiliser les pixels pour les écrans.

Si vous savez que votre page sera imprimée sur une imprimante de haute qualité, vous pouvez alors envisager d'utiliser une autre unité comme `cm` ou `mm`.

Vous pouvez en savoir plus sur l'histoire de l'unité pixel et pourquoi un pouce CSS ne correspond pas toujours à un pouce physique [dans cet article](https://www.smashingmagazine.com/2021/07/css-absolute-units/).

### `cm`

Centimètres.

En CSS, `1cm` est environ 37,8 pixels, ou environ 25,2/64 de pouce.

### `mm`

Millimètres.

En CSS, `1mm` est environ 3,78 pixels, ou 1/10ème de centimètre.

### `in`

Pouces.

En CSS, `1in` est environ 96 pixels, ou environ 2,54 cm.

### `pt`

Points.

En CSS, `1pt` est environ 1,3333 pixel, ou 1/72ème de pouce.

### `pc`

Picas.

En CSS, `1pc` est environ 16 pixels, ou 1/6 de pouce.

## Unités de longueur relatives

Les unités de longueur relatives sont relatives à la taille ou aux paramètres d'un autre élément. Par exemple, la taille de police relative d'un élément peut être calculée en utilisant la taille de police de l'élément parent.

Voici quelques unités de longueur relatives courantes :

### `em`

L'unité CSS `em` tire son nom d'une unité typographique. En typographie, le terme em "[était à l'origine une référence à la largeur de la lettre majuscule M dans la police et la taille utilisées](https://en.wikipedia.org/wiki/Em_(typography))_".

Lorsqu'elle est utilisée avec la propriété `font-size`, `em` hérite de la `font-size` de son élément parent :

```css
.container {
  font-size: 16px;
}

.container p {
  font-size: 1em;
}

.container h2 {
  font-size: 3em;
}

.container h3 {
  font-size: 2em;
}
```

Dans cet exemple, la `font-size` de `p` est `16px` (16 * 1). Pendant ce temps, la `font-size` de `h2` est `48px` (16 * 3), et `32px` pour le `h3` (16 * 2).

Si `em` est utilisé avec une autre propriété comme `width`, `em` est calculé en utilisant la taille de l'élément ciblé.

### `rem`

Root `em`. Cette unité relative n'est pas affectée par la taille ou le paramètre d'un élément parent, et est basée sur la racine du document. Pour les sites web, la racine du document est l'élément `html`.

```css
p {
  font-size: 1.25rem;
}
```

Dans la plupart des navigateurs, la taille de police par défaut est 16, donc la `font-size` des éléments `html` est `16px`. Donc dans ce cas, `p` est `20px` (16 * 1,25).

Mais si un utilisateur change la taille de police par défaut de son navigateur, alors la `font-size` de `p` sera mise à l'échelle vers le haut ou vers le bas en conséquence.

### `%`

Pourcentages, ou la taille en pourcentage relative à la taille du parent :

```css
div {
  width: 400px;
}

div p {
  width: 75%;
}
```

Puisque la largeur du parent est `400px`, la largeur du paragraphe intérieur est de `300px` (400 * 0,75).

### `vw`

Largeur de la vue. `1vw` est 1 % de la largeur de la fenêtre d'affichage.

Par exemple :

```css
body {
  width: 100vw;
}
```

Puisque l'élément `body` est défini à `100vw`, ou 100 % de la largeur de la fenêtre d'affichage, il occupera toute la largeur disponible. Donc si vous redimensionnez votre navigateur à 690 pixels de large, alors le `body` occupera toute la largeur de 690 pixels.

### `vh`

Hauteur de la vue. `1vh` est 1 % de la hauteur de la fenêtre d'affichage.

Par exemple :

```css
div {
  height: 50vh;
}
```

Le `div` remplira 50 % de la hauteur de la fenêtre d'affichage. Donc si la fenêtre du navigateur est haute de 900 pixels, la `height` du `div` sera de 450 pixels.

### `ex`

L'unité CSS `ex` tire son nom de la hauteur de la lettre x en typographie, ou "[la hauteur de la lettre _x_ dans la police](https://en.wikipedia.org/wiki/X-height)". Dans de nombreuses polices, le caractère x minuscule est généralement environ la moitié de la hauteur du plus grand caractère.

![Une image montrant la hauteur de la lettre x du mot Sphinx.](https://www.freecodecamp.org/news/content/images/2022/02/660px-Typography_Line_Terms.svg.png)
_[Source](https://en.wikipedia.org/wiki/X-height)_

En CSS, `1ex` est la hauteur de la lettre x de la police, ou la moitié de `1em`.

Mais puisque la taille du caractère x minuscule peut varier considérablement en fonction de la police, l'unité CSS `ex` est rarement utilisée.

### `ch`

Unité de caractère. L'unité CSS `ch` est définie comme la largeur du caractère 0 (zéro, ou U+0030) de la police.

Bien que l'unité `ch` fonctionne comme une mesure exacte pour les polices à chasse fixe comme Courier, elle peut être imprévisible avec les polices proportionnelles comme Arial.

Par exemple, si votre police est Courier et que vous définissez la largeur d'un élément à `60ch`, cet élément sera exactement de 60 caractères de large.

Mais si votre police est Arial et que vous définissez la largeur d'un élément à `60ch`, il est impossible de savoir à quel point l'élément sera large - les caractères peuvent déborder du conteneur ou être trop courts.

![Une image montrant 20ch comme une mesure exacte dans Courier, mais inexacte dans les polices Helvetica et Georgia.](https://www.freecodecamp.org/news/content/images/2022/02/ch-unit-monospaced-and-proportional-fonts.png)
_[Source](https://meyerweb.com/eric/thoughts/2018/06/28/what-is-the-css-ch-unit/)_

Consultez [cet article](https://meyerweb.com/eric/thoughts/2018/06/28/what-is-the-css-ch-unit/) pour une explication approfondie de l'unité `ch` et pour voir quelques exemples.

### `vmin` et `vmax`

Les unités de minimum de la fenêtre d'affichage (`vmin`) et de maximum de la fenêtre d'affichage (`vmax`) sont basées sur les valeurs de `vw` et `vh`.

`1vmin` est 1 % de la plus petite dimension de la fenêtre d'affichage, et `1vmax` est 1 % de la plus grande dimension de la fenêtre d'affichage.

Par exemple, imaginez une fenêtre de navigateur qui est large de 1200 pixels et haute de 600 pixels. Dans ce cas, `1vmin` est `6px` (1 % de `vh`, qui est plus petit à 600 pixels). Pendant ce temps, `1vmax` est `12px` (1 % de `vh`, qui est la valeur la plus grande à 1200 pixels).