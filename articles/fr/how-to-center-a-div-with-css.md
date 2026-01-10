---
title: Comment centrer une div avec CSS
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-27T19:58:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-a-div-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-pixabay-161043-1.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: Web Development
  slug: web-development
seo_title: Comment centrer une div avec CSS
seo_desc: 'There are a few common coding problems you might encounter when you start
  practicing what you''ve learned by building projects.

  One common problem you''ll face as a web developer is how to place an element at
  the center of a page or within an element a...'
---

Il y a quelques problèmes de codage courants que vous pourriez rencontrer lorsque vous commencez à pratiquer ce que vous avez appris en construisant des projets.

Un problème courant auquel vous serez confronté en tant que développeur web est de savoir comment placer un élément au centre d'une page ou dans un élément agissant comme son conteneur. C'est le problème omniprésent "Comment centrer une div ?".

Dans cet article, nous verrons comment nous pouvons centrer des éléments en utilisant diverses propriétés CSS. Nous verrons des exemples de code dans chaque section et une représentation visuelle des éléments dans tous les exemples.

## Comment centrer une div en utilisant la propriété CSS Flexbox

Dans cette section, nous verrons comment utiliser la propriété CSS Flexbox pour centrer un élément horizontalement, verticalement et au centre d'une page/conteneur.

Vous pouvez utiliser une image si vous préférez, mais nous allons simplement utiliser un cercle simple dessiné avec CSS. Voici le code :

```html
<div class="container">

      <div class="circle">

      </div>

</div>
```

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--276-.png)

Le positionnement avec Flexbox nécessite que nous écrivions le code dans la classe de l'élément parent ou conteneur.

### Comment centrer une div horizontalement en utilisant Flexbox

Maintenant, nous allons écrire le code pour centrer l'élément `div` horizontalement. Nous utilisons toujours le cercle que nous avons créé ci-dessus.

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
  display: flex;
  justify-content: center;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

Nous avons ajouté deux lignes de code pour centrer le cercle horizontalement. Voici les lignes que nous avons ajoutées :

```css
display: flex;
justify-content: center;
```

`display: flex;` nous permet d'utiliser Flexbox et ses propriétés, tandis que `justify-content: center;` aligne le cercle au centre horizontalement.

Voici la position de notre cercle :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--278-.png)

### Comment centrer une div verticalement en utilisant Flexbox

Ce que nous allons faire dans cette section est similaire à la précédente, à l'exception d'une ligne de code.

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
  display: flex;
  align-items: center;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

Dans cet exemple, nous avons utilisé `align-items: center;` pour centrer le cercle verticalement. Rappelez-vous que nous devons écrire `display: flex;` d'abord avant de spécifier la direction.

Voici la position de notre cercle :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--280-.png)

### Comment positionner une div au centre en utilisant Flexbox

Dans cette section, nous allons positionner le cercle au centre de la page en utilisant à la fois les propriétés d'alignement horizontal et vertical de CSS Flexbox. Voici comment :

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
  display: flex;
  justify-content: center;
  align-items: center;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

Voici les trois lignes de code que nous avons ajoutées à la classe du conteneur ci-dessus :

```css
display: flex;
justify-content: center;
align-items: center;
```

Comme prévu, nous commençons par `display: flex;` qui nous permet d'utiliser Flexbox en CSS. Nous avons ensuite utilisé les propriétés `justify-content` (alignement horizontal) et `align-items` (alignement vertical) pour positionner le cercle au centre de la page.

Voici la position de notre cercle :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--282-.png)

## Comment centrer une div horizontalement en utilisant la propriété CSS `margin`

Dans cette section, nous allons utiliser la propriété `margin` pour centrer notre cercle horizontalement.

Recréons notre cercle.

```html
<div class="container">

      <div class="circle">

      </div>

</div>
```

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--276-.png)

Cette fois, nous allons écrire le code dans la classe `circle`. Voici comment :

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: black;
  margin: 0 auto;
}
```

Tout ce que nous avons ajouté est la ligne de code `margin: 0 auto;` à la classe `circle`.

Regardons la position du cercle :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--278--1.png)

## Comment centrer du texte horizontalement en utilisant la propriété CSS `text-align`

Dans cette section, nous verrons comment centrer du texte horizontalement.

Cette méthode ne fonctionne que lorsque nous travaillons avec du texte écrit dans un élément.

Voici un exemple :

```html
<div class="container">

    <h1>Bonjour le monde !</h1>
      
</div>
```

Dans l'exemple ci-dessus, nous avons créé une `div` avec une classe de conteneur et un élément `h1` avec du texte. Voici à quoi cela ressemble pour le moment :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--272-.png)

Écrivons le code CSS.

```css
.container {
  width: 500px;
  height: 250px;
  margin: 50px;
  outline: solid 1px black;
}

h1 {
  text-align: center;
}
```

Pour aligner le texte dans l'élément `h1` au centre de la page, nous avons dû utiliser la propriété `text-align`, en lui donnant une valeur de `center`. Voici à quoi cela ressemble maintenant dans le navigateur :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--274-.png)

## Conclusion

Dans cet article, nous avons vu comment centrer des éléments horizontalement, verticalement et au centre de la page en utilisant Flexbox et les propriétés de marge et d'alignement de texte en CSS.

Dans chaque section, nous avons vu à la fois un exemple de code et une représentation visuelle de ce que fait le code.

Bon codage !