---
title: Style de police HTML – Comment changer la couleur et la taille du texte avec
  une balise HTML
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-19T23:23:07.000Z'
originalURL: https://freecodecamp.org/news/html-font-style-how-to-change-text-color-and-size-with-an-html-tag
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/fontstyle.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Style de police HTML – Comment changer la couleur et la taille du texte
  avec une balise HTML
seo_desc: 'When you code in HTML and add some text, you don’t want to leave it like
  that. You want to make that text look good.

  And to do that, you need to change their appearance through the color and font-size
  properties of CSS.

  In this tutorial, I will show ...'
---

Lorsque vous codez en HTML et que vous ajoutez du texte, vous ne voulez pas le laisser tel quel. Vous voulez que ce texte ait une belle apparence.

Et pour cela, vous devez modifier leur apparence via les propriétés `color` et `font-size` de CSS.

Dans ce tutoriel, je vais vous montrer deux façons différentes de rendre vos textes HTML plus attrayants.

## Syntaxe de base de `font-size`

```html
selector {
     font-size: value;
     color: value;
}
```

## Comment changer la taille et la couleur du texte dans la balise HTML

Vous pouvez changer la couleur et la taille de votre texte directement dans sa balise avec les propriétés color et font-size. Cela s'appelle le CSS en ligne. Vous le faites avec l'attribut style en HTML.

Dans le code HTML ci-dessous, nous allons changer la couleur et la taille du texte freeCodeCamp.

```html
<h1>freeCodeCamp</h1>
```

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}
```

Voici à quoi cela ressemble dans le navigateur :
![unstyled-font](https://www.freecodecamp.org/news/content/images/2021/08/unstyled-font.png)

Pour changer la taille du texte, vous utiliserez l'attribut style, puis vous définirez une valeur avec la propriété `font-size` comme ceci :

```html
<h1 style="font-size: 4rem">freeCodeCamp</h1>
```

Le texte ressemble maintenant à ceci dans le navigateur : 
![text-size](https://www.freecodecamp.org/news/content/images/2021/08/text-size.png)

Si vous vous demandez ce que signifie 4rem, c'est une unité de mesure. C'est la même chose que 64 pixels, car 16px font 1rem sauf si vous changez la taille de police racine (`html`) à une autre valeur.

Pour changer la couleur du texte, vous pouvez utiliser l'attribut style, puis définir une valeur avec la propriété color :

```html
<h1 style="color: #2ecc71">freeCodeCamp</h1>
```

Voici ce que nous avons maintenant dans le navigateur :
![text-color](https://www.freecodecamp.org/news/content/images/2021/08/text-color.png)

En combinant les propriétés `font-size` et `color`, nous obtenons ceci dans le navigateur :

![inline-text-size-and-color](https://www.freecodecamp.org/news/content/images/2021/08/inline-text-size-and-color.png)

Avec le code : 

```html
<h1 style="font-size: 4rem; color: #2ecc71">freeCodeCamp</h1>
```

## Comment changer la taille et la couleur du texte dans un fichier CSS externe

Vous pouvez également changer la couleur et la taille du texte dans une feuille de style externe. Plus important encore, vous devez lier le CSS externe dans la section head de votre HTML.

La syntaxe de base pour le faire ressemble à ceci :

```html
<link rel="stylesheet" href="path-to-css-file">
```

Maintenant, pour changer la taille et la couleur du texte freeCodeCamp, vous devez le sélectionner dans la feuille de style et appliquer les propriétés et valeurs appropriées.

Rappelons que voici notre simple code HTML :

```html
<h1>freeCodeCamp</h1>
```

Vous pouvez changer la couleur et la taille du texte en sélectionnant l'élément (h1) et en attribuant des valeurs aux propriétés color et font-size :

```css
 h1 {
    color: #2ecc71;
    font-size: 4rem;
}
```

Nous obtenons le même résultat dans le navigateur :
![external-text-size-and-color](https://www.freecodecamp.org/news/content/images/2021/08/external-text-size-and-color.png)

## Conclusion

J'espère que ce tutoriel vous donne les connaissances nécessaires pour pouvoir changer la taille et la couleur de votre texte HTML afin de les rendre plus attrayants.

Merci d'avoir lu, et continuez à coder.