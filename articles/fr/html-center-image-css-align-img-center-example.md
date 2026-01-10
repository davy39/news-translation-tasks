---
title: HTML Centrer une Image – Exemple d'Alignement CSS Img au Centre
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-01T21:16:57.000Z'
originalURL: https://freecodecamp.org/news/html-center-image-css-align-img-center-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/arrows-2889040_1920.jpg
tags:
- name: CSS
  slug: css
- name: css flex
  slug: css-flex
- name: CSS Grid
  slug: css-grid
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: HTML Centrer une Image – Exemple d'Alignement CSS Img au Centre
seo_desc: "If you're making websites with HTML and CSS, you will be working with images\
  \ a lot. \nDevelopers often struggle with image alignment in CSS, especially when\
  \ trying to figure out how to center an image.\nCentering anything in CSS is not\
  \ really a straigh..."
---

Si vous créez des sites web avec HTML et CSS, vous travaillerez beaucoup avec des images. 

Les développeurs ont souvent du mal avec l'alignement des images en CSS, surtout lorsqu'ils essaient de comprendre comment centrer une image.

Centrer quoi que ce soit en CSS n'est pas vraiment une chose simple - surtout pour les débutants. C'est pourquoi les gens se vantent d'être capables de centrer une div. :)

Puisque l'élément `img` est un élément en ligne, cela rend un peu plus difficile le centrage. Mais ne vous inquiétez pas, vous pouvez convertir l'image en un élément de bloc et ensuite la centrer.

Dans cet article, je vais vous montrer 4 façons différentes de centrer une image.

## Table des Matières
- [Comment Centrer une Image avec la Propriété Text Align](#heading-comment-centrer-une-image-avec-la-propriete-text-align)
- [Comment Centrer une Image avec Flexbox](#heading-comment-centrer-une-image-avec-flexbox)
- [Comment Centrer une Image avec CSS Grid](#heading-comment-centrer-une-image-avec-css-grid)
- [Comment Centrer une Image avec la Propriété Margin](#heading-comment-centrer-une-image-avec-la-propriete-margin)

## Comment Centrer une Image avec la Propriété Text Align

Vous pouvez centrer une image avec la propriété `text-align`. 

Une chose que vous devez savoir est que la balise pour insérer des images – `img` – est un élément en ligne. Le centrage avec la propriété `text-align` fonctionne uniquement pour les éléments de niveau bloc.

Alors, comment centrer une image avec la propriété text-align ? Vous enveloppez l'image dans un élément de niveau bloc comme un `div` et vous donnez au `div` un `text-align` de `center`.

```html
<div>
    <img src="fcc22.png" alt="freeCodeCamp" />
</div>
```

```css
div {
      text-align: center;
    }
```
![ss-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-1.png)

## Comment Centrer une Image avec Flexbox

L'introduction de CSS Flexbox a facilité le centrage de n'importe quoi.

Flexbox fonctionne en plaçant ce que vous voulez centrer dans un conteneur et en donnant au conteneur un `display` de `flex`. Ensuite, il définit `justify-content` sur `center` comme montré dans l'extrait de code ci-dessous :

```css
  div {
      display: flex;
      justify-content: center;
    }
```
![ss-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-1.png)

**P.S. :** Une propriété `justify-content` définie sur `center` centre une image horizontalement. Pour centrer l'image verticalement aussi, vous devez définir `align-items` sur `center`.

## Comment Centrer une Image avec CSS Grid

CSS Grid fonctionne comme Flexbox, avec l'avantage supplémentaire que Grid est multidimensionnel, contrairement à Flexbox qui est bidimensionnel.

Pour centrer une image avec CSS Grid, enveloppez l'image dans un élément div conteneur et donnez-lui un display de `grid`. Ensuite, définissez la propriété `place-items` sur center. 
```css
 div {
      display: grid;
      place-items: center;
    }
```
![ss-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-1.png)

**P.S. :**`place-items` avec une valeur de `center` centre n'importe quoi horizontalement et verticalement.

## Comment Centrer une Image avec la Propriété Margin

Vous pouvez également centrer une image en définissant une marge gauche et droite sur auto. Mais tout comme la propriété `text-align`, `margin` fonctionne uniquement pour les éléments de niveau bloc. 

Donc, ce que vous devez faire est de convertir l'image en un élément de niveau bloc d'abord en lui donnant un display de block.

```css
img {
      display: block;
      margin: 0 auto;
    }
```

Ces 2 propriétés pourraient suffire. Mais parfois, vous devez définir une largeur pour l'image, afin que les marges gauche et droite de auto aient des espaces à prendre.

```css
 img {
      display: block;
      margin: 0 auto;
      width: 40%;
    }
```

![ss-2](https://www.freecodecamp.org/news/content/images/2022/02/ss-2.png)

**P.S. :** Vous n'aurez peut-être pas à descendre aussi bas que 40% pour la largeur. L'image était déformée à un pourcentage de 60+, c'est pourquoi je suis descendu aussi bas que 40%.

J'espère que cet article vous aide à choisir la méthode qui fonctionne le mieux pour vous pour centrer une image.

Merci d'avoir lu.