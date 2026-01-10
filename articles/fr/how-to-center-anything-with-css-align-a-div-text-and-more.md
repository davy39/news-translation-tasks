---
title: Comment centrer n'importe quoi avec CSS - Aligner une Div, du texte, et plus
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-05-15T04:24:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-anything-with-css-align-a-div-text-and-more
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/5f9c9b00740569d1a4ca291b.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: responsive design
  slug: responsive-design
seo_title: Comment centrer n'importe quoi avec CSS - Aligner une Div, du texte, et
  plus
seo_desc: "Centering things is one of the most difficult aspects of CSS. \nThe methods\
  \ themselves usually aren't difficult to understand. Instead, it's more due to the\
  \ fact that there are so many ways to center things. \nThe method you use can vary\
  \ depending on t..."
---

Centrer des éléments est l'un des aspects les plus difficiles de CSS. 

Les méthodes elles-mêmes ne sont généralement pas difficiles à comprendre. Au contraire, c'est plutôt dû au fait qu'il existe de nombreuses façons de centrer les choses. 

La méthode que vous utilisez peut varier en fonction de l'élément HTML que vous essayez de centrer, ou si vous le centrez horizontalement ou verticalement.

Dans ce tutoriel, nous allons voir comment centrer différents éléments horizontalement, verticalement, et à la fois verticalement et horizontalement.

### Voici un Scrim Interactif Montrant Comment Centrer N'importe Quoi avec CSS

<iframe src="https://scrimba.com/scrim/co4db41c6a8d6458e2d84500b?embed=freecodecamp,mini-header" width="100%" height="420"></iframe>

## Comment Centrer Horizontalement

Centrer des éléments horizontalement est généralement plus facile que de les centrer verticalement. Voici quelques éléments courants que vous pourriez vouloir centrer horizontalement et différentes façons de le faire.

### Comment Centrer du Texte avec la Propriété CSS Text-Align Center

Pour centrer du texte ou des liens horizontalement, utilisez simplement la propriété `text-align` avec la valeur `center` :

```html
<div class="container">
  <p>Bonjour, (centré) Monde !</p>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
}

p {
  /* Centrer horizontalement*/
  text-align: center;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-15.png)

### Comment Centrer une Div avec la Marge Auto CSS

Utilisez la propriété raccourcie `margin` avec la valeur `0 auto` pour centrer des éléments de niveau bloc comme une `div` horizontalement :

```html
<div class="container">
  <div class="child"></div>
</div>
```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Centrer horizontalement*/
  margin: 0 auto;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-horizontally.jpg)

### Comment Centrer une Div Horizontalement avec Flexbox

Flexbox est la manière la plus moderne de centrer les éléments sur la page, et rend la conception de mises en page responsives beaucoup plus facile qu'avant. Cependant, il n'est pas entièrement supporté dans certains navigateurs obsolètes comme Internet Explorer.

Pour centrer un élément horizontalement avec Flexbox, appliquez simplement `display: flex` et `justify-content: center` à l'élément parent :

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Centrer l'enfant horizontalement*/
  display: flex;
  justify-content: center;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-horizontally-1.jpg)

## Comment Centrer Verticalement

Centrer des éléments verticalement sans méthodes modernes comme Flexbox peut être une vraie corvée. Ici, nous allons passer en revue certaines des anciennes méthodes pour centrer les choses verticalement d'abord, puis vous montrer comment le faire avec Flexbox.

### Comment Centrer une Div Verticalement avec le Positionnement Absolu CSS et les Marges Négatives

Pendant longtemps, c'était la méthode de prédilection pour centrer les choses verticalement. Pour cette méthode, vous devez connaître la hauteur de l'élément que vous souhaitez centrer.

Tout d'abord, définissez la propriété `position` de l'élément parent sur `relative`. 

Ensuite, pour l'élément enfant, définissez la propriété `position` sur `absolute` et `top` sur `50%` :

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Installation */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Centrer verticalement */
  position: absolute;
  top: 50%;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-1.jpg)

Mais cela centre vraiment seulement le bord supérieur de l'élément enfant.

Pour vraiment centrer l'élément enfant, définissez la propriété `margin-top` sur `-(la moitié de la hauteur de l'élément enfant)` :

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Installation */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Centrer verticalement */
  position: absolute;
  top: 50%;
  margin-top: -25px; /* La moitié de la hauteur de cet élément */
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-final.jpg)

### Comment Centrer une Div Verticalement avec Transform et Translate

Si vous ne connaissez pas la hauteur de l'élément que vous souhaitez centrer (ou même si vous la connaissez), cette méthode est un truc astucieux.

Cette méthode est très similaire à la méthode des marges négatives ci-dessus. Définissez la propriété `position` de l'élément parent sur `relative`. 

Pour l'élément enfant, définissez la propriété `position` sur `absolute` et définissez `top` sur `50%`. Maintenant, au lieu d'utiliser une marge négative pour vraiment centrer l'élément enfant, utilisez simplement `transform: translate(0, -50%)` :

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Installation */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Centrer verticalement */
  position: absolute;
  top: 50%;
  transform: translate(0, -50%);
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-final-1.jpg)

Notez que `translate(0, -50%)` est une abréviation pour `translateX(0)` et `translateY(-50%)`. Vous pourriez également écrire `transform: translateY(-50%)` pour centrer l'élément enfant verticalement.

### Comment Centrer une Div Verticalement avec Flexbox

Comme pour centrer les choses horizontalement, Flexbox rend super facile le centrage des choses verticalement.

Pour centrer un élément verticalement, appliquez `display: flex` et `align-items: center` à l'élément parent :

```html
<div class="container">
  <div class="child"></div>
</div>
```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Centrer verticalement */
  display: flex;
  align-items: center;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-final-2.jpg)

## Comment Centrer à la fois Verticalement et Horizontalement

### Comment Centrer une Div Verticalement et Horizontalement avec le Positionnement Absolu CSS et les Marges Négatives

Cela est très similaire à la méthode ci-dessus pour centrer un élément verticalement. Comme la dernière fois, vous devez connaître la largeur et la hauteur de l'élément que vous souhaitez centrer.

Définissez la propriété `position` de l'élément parent sur `relative`.

Ensuite, définissez la propriété `position` de l'enfant sur `absolute`, `top` sur `50%`, et `left` sur `50%`. Cela centre simplement le coin supérieur gauche de l'élément enfant verticalement et horizontalement.

Pour vraiment centrer l'élément enfant, appliquez une marge supérieure négative définie à la moitié de la hauteur de l'élément enfant, et une marge gauche négative définie à la moitié de la largeur de l'élément enfant :

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Installation */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Centrer verticalement et horizontalement */
  position: absolute;
  top: 50%;
  left: 50%;
  margin: -25px 0 0 -25px; /* Appliquer des marges supérieures et gauches négatives pour vraiment centrer l'élément */
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-and-horizontally.jpg)

### Comment Centrer une Div Verticalement et Horizontalement avec Transform et Translate

Utilisez cette méthode pour centrer un élément verticalement et horizontalement si vous ne connaissez pas ses dimensions exactes et ne pouvez pas utiliser Flexbox.

Tout d'abord, définissez la propriété `position` de l'élément parent sur `relative`. 

Ensuite, définissez la propriété `position` de l'élément enfant sur `absolute`, `top` sur `50%`, et `left` sur `50%`. 

Enfin, utilisez `transform: translate(-50%, -50%)` pour vraiment centrer l'élément enfant :

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Installation */
  position: relative;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
  /* Centrer verticalement et horizontalement */
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-and-horizontally-1.jpg)

### Comment Centrer une Div Verticalement et Horizontalement avec Flexbox

Flexbox est le moyen le plus facile de centrer un élément à la fois verticalement et horizontalement.

Cela est vraiment juste une combinaison des deux méthodes Flexbox précédentes. Pour centrer le ou les éléments enfants horizontalement et verticalement, appliquez `justify-content: center` et `align-items: center` à l'élément parent :

```html
<div class="container">
  <div class="child"></div>
</div>

```

```css
.container {
  font-family: arial;
  font-size: 24px;
  margin: 25px;
  width: 350px;
  height: 200px;
  outline: dashed 1px black;
  /* Centrer verticalement et horizontalement */
  display: flex;
  justify-content: center;
  align-items: center;
}

.child {
  width: 50px;
  height: 50px;
  background-color: red;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/11/box-centered-vertically-and-horizontally-2.jpg)

C'est tout ce que vous devez savoir pour centrer avec les meilleurs. Maintenant, allez de l'avant et centrez toutes les choses.