---
title: Propriété Flex Basis dans Flexbox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T22:18:00.000Z'
originalURL: https://freecodecamp.org/news/flex-basis-property-in-flexbox
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e3c740569d1a4ca3c10.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
seo_title: Propriété Flex Basis dans Flexbox
seo_desc: 'Flex Basis

  The flex-basis property defines the size of the flex-item along the main axis of
  the flex container. The main axis is horizontal if flex-direction is set to row
  and it’ll be vertical if the flex-direction property is set to column.

  Syntax

  ...'
---

# **Flex Basis**

La propriété `flex-basis` définit la taille de l'élément `flex-item` le long de l'axe principal du conteneur flex. L'axe principal est horizontal si `flex-direction` est défini sur `row` et il sera vertical si la propriété `flex-direction` est définie sur `column`.

## **Syntaxe**

```css
flex-basis: auto | content | <width> | <height>;
```

## **flex-basis: auto**

`flex-basis: auto` recherche la taille principale de l'élément et définit la taille. Par exemple, dans un conteneur flex horizontal, `auto` recherchera `width` et `height` si l'axe du conteneur est vertical.

Si aucune taille n'est spécifiée, `auto` reviendra à `content`.

## **flex-basis: content**

`flex-basis: content` détermine la taille en fonction du contenu de l'élément, sauf si `width` ou `height` est défini via `box-sizing` normal.

Dans les deux cas où `flex-basis` est soit `auto` soit `content`, si la taille principale est spécifiée, cette taille aura la priorité.

## **flex-basis:**

Cela revient à spécifier `width` ou `height`, mais de manière plus flexible. `flex-basis: 20em;` définira la taille initiale de l'élément à `20em`. Sa taille finale sera basée sur l'espace disponible, le multiplicateur `flex-grow` et le multiplicateur `flex-shrink`.

La spécification suggère l'utilisation de la propriété raccourcie `flex`. Cela permet d'écrire `flex-basis` avec les propriétés `flex-grow` et `flex-shrink`.

## **Exemples**

Voici des lignes de conteneurs flex individuels et d'éléments flex individuels montrant comment `flex-basis` affecte le `box-sizing`.

![effet de flex-basis sur l'axe horizontal](https://vijayabharathib.github.io/fcc_guide_images/css/properties/flex-basis-horizontal.png)

Lorsque la `flex-direction` est `column`, le même `flex-basis` contrôlera la propriété `height`. Vous pouvez le voir dans l'exemple ci-dessous :

![exemple de flex-basis contrôlant la hauteur dans un conteneur vertical](https://vijayabharathib.github.io/fcc_guide_images/css/properties/flex-basis-vertical.png)

### Plus d'informations :

Vous pouvez trouver des références supplémentaires sur la propriété flex basis sur les pages suivantes :

* Spécification CSS [niveau 1](https://drafts.csswg.org/css-flexbox-1/)
* Page Mozilla Developer Network sur [flex-basis](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis#content)

## Plus d'informations sur Flexbox :

* [Conseils et astuces CSS Flexbox](https://guide.freecodecamp.org/css/tutorials/css-flexbox-tips-and-tricks/)
* [Flexbox - l'antisèche ultime](https://www.freecodecamp.org/news/flexbox-the-ultimate-css-flex-cheatsheet/)