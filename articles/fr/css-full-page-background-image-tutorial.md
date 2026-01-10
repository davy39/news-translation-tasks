---
title: Tutoriel sur la taille des images d'arrière-plan CSS – Comment coder une image
  d'arrière-plan en plein écran
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-02T20:58:10.000Z'
originalURL: https://freecodecamp.org/news/css-full-page-background-image-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/CSS-BG-Img-Tutorial.jpg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: Tutoriel sur la taille des images d'arrière-plan CSS – Comment coder une
  image d'arrière-plan en plein écran
seo_desc: 'By Joe Liang

  This tutorial will show you a simple way to code a full page background image using
  CSS. And you''ll also learn how to make that image responsive to your users'' screen
  size.

  Making a background image fully stretch out to cover the entire ...'
---

Par Joe Liang

Ce tutoriel vous montrera une manière simple de coder une image d'arrière-plan en plein écran en utilisant CSS. Vous apprendrez également comment rendre cette image responsive selon la taille de l'écran de vos utilisateurs.

Faire en sorte qu'une image d'arrière-plan s'étire complètement pour couvrir l'intégralité de la fenêtre d'affichage (viewport) du navigateur est une tâche courante en conception web. Heureusement, cette tâche peut être accomplie avec quelques lignes de CSS.

## Couvrir la fenêtre d'affichage avec une image

Tout d'abord, nous voulons nous assurer que notre page couvre réellement l'intégralité de la fenêtre d'affichage :

```css
html {
   min-height: 100%;
}
```

À l'intérieur de `html`, nous utiliserons la propriété `background-image` pour définir l'image :

```css
background-image: url(image.jpg); /* remplacez image.jpg par le chemin vers votre image */
```

## La magie de la propriété 'background-size'

La magie opère avec la propriété `background-size` :

```css
background-size: cover;
```

`cover` indique au navigateur de s'assurer que l'image couvre toujours l'intégralité du conteneur, dans ce cas `html`. Le navigateur couvrira le conteneur même s'il doit étirer l'image ou en couper un peu les bords.

Comme le navigateur peut étirer l'image, vous devriez utiliser une image d'arrière-plan ayant une résolution suffisamment élevée. Sinon, l'image pourrait paraître pixelisée.

Si vous tenez à ce que toute l'image apparaisse en arrière-plan, vous devrez vous assurer que le ratio d'aspect de l'image est relativement proche de celui de la taille de l'écran.

## Comment ajuster la position d'une image et éviter la répétition

Le navigateur peut également choisir d'afficher votre image d'arrière-plan sous forme de mosaïque en fonction de sa taille. Pour éviter cela, utilisez `no-repeat` :

```css
background-repeat: no-repeat;
```

Pour que les choses restent esthétiques, nous garderons notre image toujours centrée :

```css
background-position: center center;
```

Cela centrera l'image horizontalement et verticalement à tout moment.

Nous avons maintenant produit une image entièrement responsive qui couvrira toujours tout l'arrière-plan :

```css
html {
   min-height: 100%;
   background-image: url(image.jpg);
   background-size: cover;
   background-repeat: no-repeat;
   background-position: center center;
}
```

## Comment fixer une image lors du défilement

Maintenant, au cas où vous voudriez ajouter du texte par-dessus l'image d'arrière-plan et que ce texte dépasse la fenêtre d'affichage actuelle, vous pourriez vouloir vous assurer que votre image reste en arrière-plan lorsque l'utilisateur fait défiler la page pour voir le reste du texte :

```css
background-attachment: fixed;
```

Vous pouvez inclure toutes les propriétés d'arrière-plan décrites ci-dessus en utilisant la notation abrégée :

```css
background: url(image.jpg) center center cover no-repeat fixed;
```

## Facultatif : Comment ajouter une Media Query pour mobile

Pour ajouter une cerise sur le gâteau, vous pourriez vouloir ajouter une media query pour les écrans plus petits :

```css
@media only screen and (max-width: 767px) {
  html {
     background-image: url(smaller-image.jpg);
  }
}
```

Vous pouvez utiliser Photoshop ou un autre logiciel d'édition d'images pour réduire la taille de votre image d'origine afin d'améliorer la vitesse de chargement de la page sur les connexions internet mobiles.

Maintenant que vous connaissez la magie de la création d'un arrière-plan d'image responsive en plein écran, il est temps de créer de magnifiques sites web !

## Vous voulez voir plus de conseils et de connaissances en développement web ?

* [S'abonner](https://1000mileworld.com/#post) à ma newsletter hebdomadaire
* Visitez mon blog sur [1000 Mile World](https://1000mileworld.com/)
* [Suivez-moi](https://twitter.com/1000mileworld) sur Twitter