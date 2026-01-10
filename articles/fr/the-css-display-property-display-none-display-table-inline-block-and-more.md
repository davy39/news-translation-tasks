---
title: La propriété CSS Display – Display None, Display Table, Inline Block et plus
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-19T20:47:14.000Z'
originalURL: https://freecodecamp.org/news/the-css-display-property-display-none-display-table-inline-block-and-more
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/css-display-property.png
tags:
- name: CSS
  slug: css
- name: css flex
  slug: css-flex
- name: CSS Grid
  slug: css-grid
- name: Web Design
  slug: web-design
seo_title: La propriété CSS Display – Display None, Display Table, Inline Block et
  plus
seo_desc: 'In CSS, the display property determines how an element looks. It is also
  a crucial part of the presentation of your HTML code as it has a significant impact
  on layouts.

  In fact, to use the modern Flexbox and Grid models, you need to use the display
  p...'
---

En CSS, la propriété display détermine l'apparence d'un élément. Elle constitue également une partie cruciale de la présentation de votre code HTML, car elle a un impact significatif sur les mises en page.

En fait, pour utiliser les modèles modernes Flexbox et Grid, vous devez utiliser la propriété display avant d'avoir accès à leurs diverses propriétés et valeurs. C'est l'une des raisons pour lesquelles la propriété display est si importante en CSS.

Plongeons-nous dans l'apprentissage de l'utilisation de la propriété `display` et de toutes ses différentes valeurs.

## Syntaxe de base de la propriété `display`

```html
élement {
        display: valeur;
     }
```

## Valeurs de la propriété Display en CSS

Il existe des éléments en ligne et de niveau bloc en CSS. La différence entre les deux est que les éléments en ligne n'occupent pas tout l'espace – c'est-à-dire qu'ils ne commencent pas sur une nouvelle ligne – mais les éléments de bloc le font.

La propriété display prend de nombreuses valeurs différentes telles que `inline`, `inline-block`, `block`, `table`, et plus encore, qui influencent toutes la mise en page et la présentation d'un élément sur la page web. De plus, pour implémenter les mises en page flex et grid, vous devez utiliser la propriété display.

Vous pouvez utiliser cette propriété display pour changer un élément `inline` en `block`, un élément `block` en `inline`, des éléments `block` et `inline` en `inline-block`, et bien plus encore.

![display-property-values](https://www.freecodecamp.org/news/content/images/2021/08/display-property-values.png align="left")

### `display: inline`

Un élément avec une propriété display définie sur `inline` ne commencera pas sur une nouvelle ligne et occupera la largeur d'écran restante/disponible. Il occupe simplement l'espace qu'un tel élément occuperait normalement.

Pour cette raison, vous ne pouvez pas définir la `width` et la `height` d'un élément qui a un display `inline`, car il n'occupe pas toute la largeur de l'écran.

Certains éléments sont en ligne par défaut, comme `<span>`, `<a>`, `<i>`, et `<img>`.

```html
<div>
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
      <span>Ceci est un élément en ligne</span> Modi eaque debitis eos quod labore
      maiores delectus asperiores voluptatem voluptas soluta!
</div>
```

```css
 body {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        font-size: 2rem;
      }
div {
        max-width: 600px;
      }
span {
        background-color: #006100;
      }
```

![inline-display](https://www.freecodecamp.org/news/content/images/2021/08/inline-display.png align="left")

### `display: block`

Un élément qui a la propriété display définie sur `block` commence sur une nouvelle ligne et occupe la largeur d'écran disponible.

Vous pouvez spécifier les propriétés `width` et `height` pour de tels éléments. Des exemples d'éléments qui sont de niveau bloc par défaut sont `<div>`, `<section>`, `<p>`, et bien d'autres.

Vous pouvez définir le `span` du code HTML précédent sur `block` display et il se comportera comme un élément de niveau bloc.

```css
span {
        display: block;
        background-color: #006100;
      }
```

![block-display](https://www.freecodecamp.org/news/content/images/2021/08/block-display.png align="left")

Vous pouvez voir que le `<span>` occupe toute la largeur. C'est parce qu'il a une propriété display définie sur block.

### `display: inline-block`

En plus des affichages block et inline, il y a aussi inline-block.

Un élément auquel vous attribuez un display `inline-block` est en ligne par présentation. Mais il a l'avantage supplémentaire de pouvoir appliquer `width` et `height`, ce que vous ne pouvez pas faire lorsque l'élément est attribué à un display `inline`.

Ainsi, vous pouvez considérer le display `inline-block` comme un élément en ligne et un élément de bloc en un seul package.

```css
 span {
        display: inline-block;
        background-color: #006100;
        width: 140px;
        height: 140px;
      }
```

![inline-block-display](https://www.freecodecamp.org/news/content/images/2021/08/inline-block-display.png align="left")

### `display: none`

Lorsque vous définissez la propriété display d'un élément sur `none`, l'élément est complètement retiré de la page et n'a aucun effet sur la mise en page.

Cela signifie également que les appareils comme les lecteurs d'écran, qui rendent les sites web accessibles aux personnes aveugles, n'auront pas accès à l'élément.

Ne confondez pas `display: none` avec `visibility: hidden`. Ce dernier cache également l'élément, mais laisse l'espace qu'il occuperait normalement ouvert ou vide.

```css
span {
        display: none;
        background-color: #006100;
        width: 140px;
        height: 140px;
      }
```

![display-none](https://www.freecodecamp.org/news/content/images/2021/08/display-none.png align="left")

Visibility hidden laisse l'espace occupé par l'élément span ouvert, comme vous pouvez le voir ci-dessous:

```css
 span {
        visibility: hidden;
        background-color: #006100;
        width: 140px;
        height: 140px;
      }
```

![visibility-hidden](https://www.freecodecamp.org/news/content/images/2021/08/visibility-hidden.png align="left")

### `display: table`

Vous utiliserez rarement une valeur de display `table` de nos jours, mais il est toujours important de la connaître. Elle était plus utile dans le passé car vous l'utilisiez pour les mises en page avant l'avènement des floats, Flex et Grid.

Définir display sur `table` fait en sorte que l'élément se comporte comme un tableau. Vous pouvez donc faire une réplique d'un tableau HTML sans utiliser l'élément table et les éléments correspondants tels que `tr` et `td`.

Par exemple, en HTML, vous pouvez faire un tableau avec l'élément `<table>` et aussi un `<div>`, ou tout autre conteneur de votre choix.

Vous faites un tableau avec l'élément HTML `<table>` comme ceci:

```html
<table>
      <tr>
        <td>Fruits</td>
        <td>Lémuriens</td>
        <td>Animaux de compagnie</td>
      </tr>
      <tr>
        <td>Noix de cajou</td>
        <td>Hua hua</td>
        <td>Chien</td>
      </tr>
      <tr>
        <td>Pomme</td>
        <td>Sifaka à diadème</td>
        <td>Chat</td>
      </tr>
      <tr>
        <td>Mangue</td>
        <td>À queue annelée</td>
        <td>Poulet</td>
      </tr>
</table>
```

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-size: 2rem;
}

div {
    max-width: 600px;
}

span {
    display: inline-block;
    background-color: #006100;
    width: 140px;
    height: 140px;
}

tr,
td {
    padding: 10px;
}
```

Le résultat des extraits de code HTML et CSS ci-dessus ressemble à ceci:

![table-with-table-element](https://www.freecodecamp.org/news/content/images/2021/08/table-with-table-element.png align="left")

Mais vous pouvez faire le même tableau avec l'élément `<div>` en définissant les displays respectifs sur `table`, `table-row` et `table-cell`. Vous obtiendrez le même résultat comme vous pouvez le voir ci-dessous:

```html
 <div class="table">
      <div class="row">
        <div class="cell">Fruits</div>
        <div class="cell">Lémuriens</div>
        <div class="cell">Animaux de compagnie</div>
      </div>
      <div class="row">
        <div class="cell">Noix de cajou</div>
        <div class="cell">Hua hua</div>
        <div class="cell">Chien</div>
      </div>
      <div class="row">
        <div class="cell">Pomme</div>
        <div class="cell">Sifaka à diadème</div>
        <div class="cell">Chat</div>
      </div>
      <div class="row">
        <div class="cell">Mangue</div>
        <div class="cell">À queue annelée</div>
        <div class="cell">Poulet</div>
      </div>
</div>
```

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-size: 2rem;
}

div {
    max-width: 600px;
}

span {
    display: inline-block;
    background-color: #006100;
    width: 140px;
    height: 140px;
}

.table {
   display: table;
}

.row {
   display: table-row;
}

.cell {
   display: table-cell;
}

.row,
.cell {
  padding: 10px;
}
```

Vous obtenez toujours votre tableau:

![table-with-div](https://www.freecodecamp.org/news/content/images/2021/08/table-with-div.png align="left")

## Autres valeurs de la propriété Display

En plus de `inline`, `block`, `none` et `table`, qui sont vraiment importantes car elles influencent considérablement l'apparence des pages web, il existe d'autres valeurs de la propriété `display` qui méritent votre attention.

Certaines d'entre elles, vous les utiliserez tout le temps sans vraiment réaliser qu'elles font également partie de la propriété display. Et d'autres que vous n'utiliserez presque jamais.

Examinons-en quelques-unes maintenant.

### `display: flex`

Un display `flex` vous donne accès au système de mise en page Flex, qui simplifie la façon dont nous concevons et mettons en page nos pages web.

```html
<div class="container">
      <div class="child">
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
        <span>Ceci est un élément en ligne</span> Modi eaque debitis eos quod
        labore maiores delectus asperiores voluptatem voluptas soluta!
      </div>
      <div class="child">
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
        <span>Ceci est un élément en ligne</span> Modi eaque debitis eos quod
        labore maiores delectus asperiores voluptatem voluptas soluta!
      </div>
</div>
```

```css
.container {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        font-size: 2rem;
}
    
span {
       visibility: hidden;
       background-color: #006100;
       width: 140px;
       height: 140px;
}

.child {
       border: 2px solid crimson;
       margin: 4px;
}
```

![display-flex](https://www.freecodecamp.org/news/content/images/2021/08/display-flex.png align="left")

### `display: grid`

Un display défini sur `grid` vous permet de construire des mises en page avec le système de grille, qui est une forme avancée de flex.

```html
<div class="container">
      <div class="child">
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
        <span>Ceci est un élément en ligne</span> Modi eaque debitis eos quod
        labore maiores delectus asperiores voluptatem voluptas soluta!
      </div>
      <div class="child">
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
        <span>Ceci est un élément en ligne</span> Modi eaque debitis eos quod
        labore maiores delectus asperiores voluptatem voluptas soluta!
      </div>
</div>
```

```css
.container {
        display: grid;
        place-items: center;
        height: 100vh;
        font-size: 2rem;
      }
   
span {
       visibility: hidden;
       background-color: #006100;
       width: 140px;
        height: 140px;
}

.child {
       border: 2px solid crimson;
       margin: 4px;
}
```

![display-grid](https://www.freecodecamp.org/news/content/images/2021/08/display-grid.png align="left")

### `display: inherit`

Cela fait en sorte que l'élément hérite de la propriété display de son parent. Ainsi, si vous avez une balise `<span>` à l'intérieur d'une div et que vous donnez à la balise span un display `inherit`, elle la transforme d'un élément en ligne en un élément de bloc.

```html
<div>
      Lorem ipsum dolor sit amet consectetur
      <span>Élément en ligne</span> adipisicing elit. Cumque cupiditate harum
      consectetur a exercitationem laboriosam nobis eos pariatur expedita iure.
</div>
```

```css
body {
     display: flex;
     align-items: center;
     justify-content: center;
     height: 100vh;
     font-size: 2rem;
}

span {
     display: inherit;
     background-color: crimson;
}
```

![display-inherit](https://www.freecodecamp.org/news/content/images/2021/08/display-inherit.png align="left")

### `display: initial`

Cela définit la propriété display d'un élément à sa valeur par défaut. Ainsi, si vous définissez la propriété display d'un span sur initial, il reste en ligne, et si vous définissez la même valeur pour une div, il reste en bloc.

```html
<div>
      Lorem ipsum dolor sit amet consectetur
      <span>Élément en ligne</span> adipisicing elit. Cumque cupiditate harum
      consectetur a exercitationem laboriosam nobis eos pariatur expedita iure.
</div>
```

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-size: 2rem;
}

span {
    display: initial;
    background-color: crimson;
}
```

![display-initial](https://www.freecodecamp.org/news/content/images/2021/08/display-initial.png align="left")

## Conclusion

Avoir une bonne compréhension de la propriété display aidera vos mises en page à avoir une belle apparence. Cela vous donne également beaucoup plus de contrôle sur la manière dont vous présentez vos éléments tout en travaillant avec CSS.

Vous pouvez continuer à revenir à cet article pour référence, car la propriété display est toujours déroutante au début jusqu'à ce que vous l'utilisiez suffisamment pour la comprendre pleinement.

J'espère que cet article vous a donné les connaissances de base dont vous avez besoin pour utiliser la propriété display à bon escient.

Merci d'avoir lu, et continuez à coder.