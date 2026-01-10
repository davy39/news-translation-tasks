---
title: CSS Vertical Align – Comment Centrer une Div, du Texte ou une Image [Exemple
  de Code]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-04T15:02:39.000Z'
originalURL: https://freecodecamp.org/news/css-vertical-align-how-to-center-a-div-text-or-an-image-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/center.png
tags:
- name: CSS
  slug: css
- name: CSS Grid
  slug: css-grid
- name: flexbox
  slug: flexbox
- name: Web Design
  slug: web-design
seo_title: CSS Vertical Align – Comment Centrer une Div, du Texte ou une Image [Exemple
  de Code]
seo_desc: "Even with helpful tools like CSS Grid and Flexbox, centering elements in\
  \ CSS remains notoriously challenging. \nIt's been the subject of many jokes and\
  \ memes, and when you successfully center something, you'll want to brag about it.\n\
  Why is Centering C..."
---

Même avec des outils utiles comme CSS Grid et Flexbox, centrer des éléments en CSS reste notoirement difficile. 

Cela a été le sujet de nombreuses blagues et mémes, et lorsque vous réussissez à centrer quelque chose, vous aurez envie de vous en vanter.

## Pourquoi Centrer des Éléments CSS est-il si Difficile ?

CSS peut être délicat à utiliser. Par exemple, si vous essayez d'aligner quelque chose horizontalement OU verticalement, ce n'est pas si difficile.

Vous pouvez simplement définir text-align sur center pour un élément en ligne, et `margin: 0 auto` le ferait pour un élément de niveau bloc.

Mais des problèmes surviennent sur plusieurs fronts si vous essayez de combiner les alignements vertical et horizontal.   

Dans ce tutoriel, je vais vous présenter trois méthodes différentes pour centrer correctement une div, du texte ou une image en CSS.

## Comment Centrer un Élément avec la Propriété CSS Position 

La propriété CSS position prend les valeurs relative, absolute, fixed et static (par défaut). Une fois définie, vous pourrez appliquer les propriétés top, right, bottom et left à l'élément. 

La combinaison des valeurs relative et absolute peut accomplir beaucoup de choses, et vous pouvez donc l'utiliser pour centrer n'importe quoi. 

Jetez un œil aux extraits ci-dessous pour voir quelques exemples.

### Comment centrer du texte avec le positionnement CSS

```html
<div class="container">
    <div class="centered-element">
      <p>Je suis un Camper, et je suis centré verticalement</p>
    </div>
</div>
``` 

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
} 

.container {
  position: relative;
  height: 400px;
  border: 2px solid #006100;
}

.centered-element {
  margin: 0;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```

![ss1b](https://www.freecodecamp.org/news/content/images/2021/08/ss1b.png)

### Comment centrer une image avec le positionnement CSS

```html
<div class="container">
    <div class="centered-element">
      <img src="freecodecamp.png" alt="centered" />
    </div>
</div>
```

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  position: relative;
  height: 400px;
  border: 2px solid #006100;
}

.centered-element {
  margin: 0;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```

![ss2b](https://www.freecodecamp.org/news/content/images/2021/08/ss2b.png)

Le code ci-dessus a centré le texte et l'image verticalement. Pour prendre en charge à la fois le centrage vertical et horizontal, nous devons apporter une petite modification au CSS. Nous allons définir la propriété top à 50 %, et nous allons ajouter une transformation sur les axes X et Y.

```
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  position: relative;
  height: 400px;
  border: 2px solid #006100;
}

.centered-element {
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

```

Le texte ressemble maintenant à ceci :
![ss4b](https://www.freecodecamp.org/news/content/images/2021/08/ss4b.png)

Et l'image à ceci : 
![ss3b](https://www.freecodecamp.org/news/content/images/2021/08/ss3b.png)

Notez que j'ai appliqué la propriété transform car l'enfant (avec la classe centered-element) était légèrement décentré. `translateY()` le pousse vers le centre verticalement et translate sur les axes X et Y (`translate()`) le pousse vers le centre verticalement et horizontalement. 

## Comment Centrer un Élément avec Flexbox en CSS

CSS Flexbox gère les mises en page dans une dimension (ligne ou colonne). Avec Flexbox, il est assez facile de centrer une div, du texte ou une image en seulement trois lignes de code. 

Vérifiez les extraits ci-dessous pour des exemples. 

### Comment centrer du texte avec Flexbox

```html
<div class="container">
    <div class="centered-element">
      <p>Je suis un Camper, et je suis centré verticalement</p>
    </div>
</div>
```

```css
.container {
    display: flex;
    align-items: center;
    height: 600px;
    border: 2px solid #006100; 
}
```
![ss5b-1](https://www.freecodecamp.org/news/content/images/2021/08/ss5b-1.png)

### Comment centrer une image avec Flexbox

```html
<div class="container">
    <div class="centered-element">
      <img src="freecodecamp.png" alt="centered" />
    </div>
</div>
```

```css
.container {
    display: flex;
    align-items: center;
    height: 600px;
    border: 2px solid #006100; 
}
```
![ss6b](https://www.freecodecamp.org/news/content/images/2021/08/ss6b.png)

Nous avons pris en charge l'alignement vertical en seulement deux lignes de code. Pour centrer horizontalement l'image et le texte, ajoutez justify-content: center.

```html
<div class="container">
    <div class="centered-element">
      <p>Je suis un Camper, je suis maintenant centré verticalement et horizontalement</p>
    </div>
</div>
```

```html
<div class="container">
    <div class="centered-element">
      <img src="freecodecamp.png" alt="centered" />
    </div>
</div>
```

```css
.container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 600px;
    border: 2px solid #006100;
}
```

Le texte ressemble maintenant à ceci :
![ss7bb](https://www.freecodecamp.org/news/content/images/2021/08/ss7bb.png)

Et l'image à ceci : ![ss11bb](https://www.freecodecamp.org/news/content/images/2021/08/ss11bb.png)

## Comment Centrer un Élément avec CSS Grid 

Avec Flexbox, il est assez facile de centrer n'importe quoi, n'est-ce pas ? Mais avec CSS Grid, il est vraiment facile de centrer n'importe quoi, car deux lignes de code suffisent pour le faire. 

### Comment centrer du texte avec CSS Grid 

```html
<div class="container">
    <div class="centered-element">
      <p>Je suis un Camper, et je suis centré verticalement</p>
    </div>
</div>
```

```css
.container {
    display: grid;
    align-items: center;
    height: 600px;
    border: 2px solid #006100;
}
```

![ss8bb](https://www.freecodecamp.org/news/content/images/2021/08/ss8bb.png)

### Comment centrer une Image avec CSS Grid

```html
<div class="container">
    <div class="centered-element">
      <img src="freecodecamp.png" alt="centered" />
    </div>
</div>
```

```css
.container {
    display: grid;
    align-items: center;
    height: 600px;
    border: 2px solid #006100;
}
```

Les exemples ci-dessus prennent en charge le centrage vertical pour vous. Pour obtenir le texte et l'image centrés horizontalement également, remplacez les align items par `place items` – une combinaison de `align-items` et `justify-content` :

```css
.container {
    display: grid;
    place-items: center;
    height: 600px;
    border: 2px solid #006100;
}

```

Le texte ressemble maintenant à ceci :

![ss7bb-1](https://www.freecodecamp.org/news/content/images/2021/08/ss7bb-1.png)

Et l'image à ceci :
![ss11bb-1](https://www.freecodecamp.org/news/content/images/2021/08/ss11bb-1.png)

## Comment Centrer une Div, du Texte ou une Image Autonome en CSS

Les trois méthodes ci-dessus vous permettent de centrer une div, du texte ou une image dans un conteneur. Vous pouvez également centrer une div, du texte ou une image autonome. 

Voyons comment faire cela maintenant.
 
### Comment centrer une div autonome en CSS

```html
<div class="container"></div>
```

```css
div.container {
    height: 300px;
    width: 300px;
    border: 2px solid #006100;
    margin: 0 auto;
  }
```

![ss12bb](https://www.freecodecamp.org/news/content/images/2021/08/ss12bb.png)

### Comment centrer du texte autonome en CSS 

```html
<p>Je suis un Camper, et je suis centré</p>
```
 
```css
     p {
         text-align: center;
     }
```

![ss13bb](https://www.freecodecamp.org/news/content/images/2021/08/ss13bb.png)

### Comment centrer une image autonome en CSS

```html
<img src="freecodecamp.png" alt="centered" />
```

```css
img {
      display: block;
      margin: 0 auto;
 }
 /* Applique un display de block, une marge de 0 en haut et en bas, 
 et auto à gauche et à droite */
```

![ss14bb](https://www.freecodecamp.org/news/content/images/2021/08/ss14bb.png)

## Conclusion

J'espère que ce tutoriel vous donne suffisamment de connaissances sur l'alignement vertical et comment centrer des éléments en CSS pour que ce soit moins fastidieux pour vous dans votre prochain projet. 

Merci d'avoir lu, et continuez à coder.