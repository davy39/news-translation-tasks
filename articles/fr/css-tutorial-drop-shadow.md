---
title: Tutoriel CSS Box Shadow – Comment ajouter une ombre portée à n'importe quel
  élément HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-18T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-tutorial-drop-shadow
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/feature.jpg
tags:
- name: '#box-shadow'
  slug: box-shadow
- name: CSS
  slug: css
- name: css properties
  slug: css-properties
- name: CSS3
  slug: css3
- name: Pure CSS
  slug: pure-css
seo_title: Tutoriel CSS Box Shadow – Comment ajouter une ombre portée à n'importe
  quel élément HTML
seo_desc: 'By Joe Liang

  We can add a drop shadow to any HTML element using the CSS property box-shadow.
  Here''s how.

  ##Adding a Basic Drop Shadow

  Let''s first set up some basic HTML elements to add our drop shadows to:

  ```html

  Box1

  Box2

  Box3


  Then add some basic ...'
---

Par Joe Liang

Nous pouvons ajouter une ombre portée à n'importe quel élément HTML en utilisant la propriété CSS `box-shadow`. Voici comment.

## Ajout d'une ombre portée de base

Commençons par configurer quelques éléments HTML de base pour ajouter nos ombres portées :

```html
<div id="box1" class="box">Box1</div>
<div id="box2" class="box">Box2</div>
<div id="box3" class="box">Box3</div>
```

Ensuite, ajoutons un peu de CSS de base :

```css
p {
    padding: 10px;
}
.box {
    padding: 20px;
    width: 50%;
    margin: 30px auto;
    background: #000;
    color: #fff;
}
```

Le résultat est simplement trois boîtes noires qui nous permettront d'ajouter facilement des ombres portées en appelant leurs identifiants uniques :

![Configuration des éléments HTML](https://www.freecodecamp.org/news/content/images/2020/05/html-elements-1.png)
_Configuration des éléments HTML_

Pour ajouter une ombre portée de base, utilisons la propriété `box-shadow` sur la Boîte 1 :

```css
/* décalage-x | décalage-y | couleur */
#box1 {
    box-shadow: 6px 12px yellow;
}
```

![Ajout d'une ombre portée de base à la Boîte 1](https://www.freecodecamp.org/news/content/images/2020/05/box1.png)
_Ajout d'une ombre portée de base à la Boîte 1_

Nous avons 3 paramètres ici. Les deux premiers sont, respectivement, le décalage-x et le décalage-y. Ils définissent l'emplacement de l'ombre portée.

Le décalage est relatif à l'origine, qui en HTML est toujours le coin supérieur gauche d'un élément. Un décalage-x positif déplacera l'ombre vers la droite, et un décalage-y positif déplacera l'ombre vers le bas.

Le troisième paramètre est la couleur de votre ombre portée.

Gardez à l'esprit que bien que nous ayons utilisé des éléments `<div>` ici, la propriété `box-shadow` peut également être appliquée à tout autre élément HTML.

## Ajout d'un rayon de flou

Si nous voulons que l'ombre ait l'air un peu plus réaliste, nous voudrons expérimenter avec le paramètre `blur-radius`.

Ce paramètre contrôle la quantité de flou à appliquer à l'ombre, ce qui la rend plus grande et plus claire. Appliquons-le à la Boîte 2 :

```css
/* décalage-x | décalage-y | rayon-de-flou | couleur */
#box2 {
	box-shadow: 6px 12px 4px red;
}
```

![Ajout d'un rayon de flou à la Boîte 2](https://www.freecodecamp.org/news/content/images/2020/05/box2-blur.png)
_Ajout d'un rayon de flou à la Boîte 2_

La valeur de 4px définit le rayon du flou à appliquer à notre ombre portée.

## Ajout d'un rayon de propagation

Si nous voulons contrôler la taille de l'ombre, nous pouvons utiliser le paramètre `spread-radius` qui contrôle la croissance ou la réduction d'une ombre.

Ajoutons un rayon de propagation de 8px à la Boîte 2 :

```css
/* décalage-x | décalage-y | rayon-de-flou | rayon-de-propagation | couleur */
#box2 {
    box-shadow: 6px 12px 4px 8px red;
}
```

![Ajout d'un rayon de propagation en plus d'un flou à la Boîte 2](https://www.freecodecamp.org/news/content/images/2020/05/box2-blur-and-spread.png)
_Ajout d'un rayon de propagation en plus d'un flou à la Boîte 2_

Rappelez-vous l'ordre de ces paramètres !

## Combinaison de plusieurs ombres dans une seule propriété

Si nous voulons être sophistiqués, nous pouvons ajouter plusieurs ombres portées à un élément en utilisant une seule propriété `box-shadow`.

Faisons cela avec la Boîte 3 en ajoutant simultanément une ombre portée bleue et verte :

```css
/* N'importe quel nombre d'ombres, séparées par des virgules */
#box3 {
    box-shadow: 6px 12px 2px 2px blue, -6px -12px 2px 2px green;
}
```

![Combinaison de plusieurs ombres portées](https://www.freecodecamp.org/news/content/images/2020/05/box3.png)
_Ajout de plusieurs ombres portées à la Boîte 3_

## Bonus : Créer une ombre intérieure

Bien que cela ne crée pas une ombre portée, le paramètre `inset` peut également être utilisé avec la propriété `box-shadow`.

Comme le suggère le nom, ce paramètre crée une ombre intérieure (c'est-à-dire une ombre à l'intérieur d'une boîte).

Le paramètre `inset` peut être placé soit au début, soit à la fin de la propriété `box-shadow`. Ici, nous démontrons son utilisation avec un élément `blockquote`.

HTML :

```html
<blockquote>
  <q>The key to success is to start before you're ready.</q>
  <p>&mdash; Marie Forleo</p>
</blockquote>
```

CSS :

```css
blockquote {
  width: 50%;
  margin: 50px auto;
  padding: 20px;
  font-size: 24px;
  box-shadow: inset 10px 5px black;
}
```

![Créer une ombre intérieure](https://www.freecodecamp.org/news/content/images/2020/05/blockquote.png)
_Créer une ombre intérieure_

Bien sûr, vous pouvez ajouter un peu de flou et de propagation pour améliorer l'ombre, ou même plusieurs ombres :

```css
 box-shadow: inset 10px 5px 25px 5px black, 5px 5px 12px 2px black;
```

![Ombre intérieure combinée avec une ombre portée](https://www.freecodecamp.org/news/content/images/2020/05/blockquote-enhanced.png)
_Ombre intérieure combinée avec une ombre portée_

Avec la propriété `box-shadow`, nous pouvons facilement faire ressortir les éléments d'une page web pour créer un bel effet d'éclairage 3D.

Si vous voulez faire quelques expériences vous-même, voici un [code pen](https://codepen.io/1000mileworld/pen/dyYeggy) que j'ai créé avec les exemples utilisés dans ce tutoriel.

Amusez-vous et voyez ce que vous pouvez créer !

## Vous voulez voir plus de conseils et de connaissances en développement web ?

* [Abonnez-vous](https://1000mileworld.com/#post) à ma newsletter hebdomadaire
* Visitez mon blog à [1000 Mile World](https://1000mileworld.com/)
* [Suivez-moi](https://twitter.com/1000mileworld) sur Twitter