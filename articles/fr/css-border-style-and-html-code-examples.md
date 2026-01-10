---
title: CSS Border – Style et exemples de code HTML
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-04T23:25:30.000Z'
originalURL: https://freecodecamp.org/news/css-border-style-and-html-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Css-border--1-.png
tags:
- name: CSS
  slug: css
- name: CSS Framework
  slug: css-framework
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: CSS Border – Style et exemples de code HTML
seo_desc: "In CSS, everything is a box. And each box – whether it's text, an image,\
  \ a div, a span, or any other element – has a border that separates its edges from\
  \ other boxes around it. \nThe CSS border property allows us to do several things\
  \ with the border o..."
---

En CSS, tout est une boîte. Et chaque boîte – qu'il s'agisse de texte, d'une image, d'une div, d'un span ou de tout autre élément – possède une bordure qui sépare ses bords des autres boîtes qui l'entourent. 

La propriété CSS border nous permet de faire plusieurs choses avec la bordure des boîtes individuelles. Se familiariser avec cette propriété peut vraiment vous aider à déboguer plus efficacement et à concevoir vos pages web de manière plus belle.

Dans ce tutoriel, nous examinerons en détail la propriété border de CSS. Cela vous aidera à vous familiariser avec elle et à commencer à l'utiliser dans votre prochain projet de codage. 

## Qu'est-ce que la propriété CSS `border` ?

`border` ne couvre pas tout ce que la propriété de bordure implique – bien qu'il soit important de noter qu'il s'agit d'une abréviation très utile, que nous aborderons plus tard dans ce tutoriel. 

Ainsi, en plus de cela, il existe les sous-propriétés `border-width`, `border-style`, `border-color` et `border-radius`. Examinons chacune d'elles une par une.

### Propriété CSS `border-width`

Vous utilisez la propriété `border-width` pour spécifier la largeur d'une bordure. La valeur est généralement exprimée en pixels (px), mais elle peut être exprimée en rem, em et en pourcentage (%). 

Et ce n'est pas tout – cette propriété accepte également `thin`, `medium` et `thick` comme valeurs. 

La propriété `border-width` est une abréviation pour `border-top-width`, `border-right-width`, `border-bottom-width` et `border-left-width`, dans le sens des aiguilles d'une montre. Ainsi, si vous le souhaitez, vous pouvez appliquer différentes valeurs de largeur à la bordure supérieure, droite, inférieure et gauche. 

### Propriété CSS `border-style`

Avec la propriété `border-style`, vous avez accès à différents styles que vous pouvez appliquer à la bordure d'une boîte. Elle accepte `none` (par défaut), `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset` et `outset`. 

Tout comme `border-width`, `border-style` est une abréviation pour `border-top-style`, `border-right-style`, `border-bottom-style` et `border-left-style`. Vous pouvez donc à nouveau spécifier différentes valeurs pour les propriétés si vous ne souhaitez pas utiliser l'abréviation. 

### Propriété CSS `border-color`

La propriété `border-color` vous permet de spécifier différentes couleurs pour votre bordure. Vous pouvez spécifier cette couleur avec des couleurs nommées, RGB et HSL – il n'y a pas de limites. 

Le noir est la couleur par défaut pour cette propriété. Donc, si vous ne spécifiez pas de valeur pour celle-ci, le noir est automatiquement défini tant que vous avez défini border-width et border-style avec certaines valeurs.

Comme pour `border-width` et `border-style`, vous pouvez également spécifier différentes couleurs sur tous les côtés de la bordure. Ainsi, `border-color` est une abréviation pour `border-top-color`, `border-right-color`, `border-bottom-color` et `border-left-color`. 

Ci-dessous se trouvent des extraits de code et leurs captures d'écran respectives montrant les trois sous-propriétés de `border` en action :

```html
<img src="freecodecamp.png" alt="freecodecamp-img" />
```

```css
img {
      display: block;
      margin: 0 auto;
      margin-top: 1rem;
    }

    img {
      border-top-width: 2px;
      border-right-width: 4px;
      border-bottom-width: 6px;
      border-left-width: 8px;
      border-top-style: solid;
      border-right-style: dotted;
      border-bottom-style: dashed;
      border-left-style: groove;
      border-top-color: #006100;
      border-right-color: #050116;
      border-bottom-color: #2ecc71;
      border-left-color: #3498db;
    }
```

![ss1](https://www.freecodecamp.org/news/content/images/2021/08/ss1.png)

```css
img {
      display: block;
      margin: 0 auto;
      margin-top: 1rem;
    }

img {
      border-width: 8px;
      border-style: solid;
      border-color: #006100;
    }
```

![ss2](https://www.freecodecamp.org/news/content/images/2021/08/ss2.png)

 ```css
 img {
      border-width: 10px;
      border-style: outset;
      border-color: #006100;
    }
```

![ss3](https://www.freecodecamp.org/news/content/images/2021/08/ss3.png)

Vous pouvez jouer avec les sous-propriétés pour mieux comprendre comment elles fonctionnent.

### L'abréviation `border` 

Nous avons appliqué les sous-propriétés `border` (`border-width`, `border-style` et `border-color`) une par une, mais elles peuvent être appliquées ensemble avec l'abréviation `border`. 

Cette abréviation est utile surtout lorsque vous voulez que les quatre côtés soient identiques comme je l'ai fait ci-dessous :

```css
img {
      border: 2px solid #006100;
    }
```

![ss4](https://www.freecodecamp.org/news/content/images/2021/08/ss4.png)

### Propriété CSS `border-radius`

Avec `border-radius`, vous pouvez supprimer les bords tranchants des bordures afin de les transformer en coins arrondis. Je pense que cela les rend également plus beaux. 

La valeur est spécifiée en pixels (px) et en pourcentage (%) également, selon vos préférences. 

```css
img {
      border: 2px solid #006100;
      border-radius: 10px;
    }
```
![ss5](https://www.freecodecamp.org/news/content/images/2021/08/ss5.png)

Si vous le souhaitez, vous pouvez également spécifier un rayon différent pour les bords supérieur, gauche, inférieur et droit de la bordure avec `border-top-right-radius`, `border-top-left-radius`, `border-bottom-right-radius` et `border-bottom-left-radius`. Cela est dû au fait que `border-radius` est également une abréviation pour ces quatre sous-propriétés.
 
Nous pouvons également appliquer certains rayons à nos bordures :  
 
```css
img {
      border: 2px solid #006100;
      border-top-right-radius: 10px;
      border-top-left-radius: 30px;
      border-bottom-right-radius: 50px;
      border-bottom-left-radius: 100px;
    }
```

![ss6](https://www.freecodecamp.org/news/content/images/2021/08/ss6.png)


## Un petit projet : Comment utiliser la propriété CSS `border` pour créer les anneaux olympiques

Nous pouvons utiliser ce que nous avons appris sur la propriété `border` et le combiner avec le positionnement CSS et Flexbox pour créer les anneaux olympiques.

```html
    <section class="container">
      <section class="top">
        <div class="red"></div>
        <div class="black"></div>
        <div class="blue"></div>
      </section>

      <section class="bottom">
        <div class="green"></div>
        <div class="yellow"></div>
      </section>
    </section>
```

```css
div {
      height: 12.5rem;
      width: 12.5rem;
      border: 12px solid;
      border-radius: 50%;
      margin: 1rem;
    }

    .blue {
      color: #3498db;
    }

    .black {
      color: black;
      position: relative;
      z-index: 1000;
    }

    .red {
      color: #ca2e2e;
    }

    .yellow {
      color: #ffa600;
    }

    .green {
      color: #19a019;
    }

    .container {
      display: flex;
      align-items: center;
      justify-content: center;
      transform: rotate(90deg);
    }

    .bottom {
      position: relative;
      right: 8.125rem;
    }

    @media screen and (max-width: 750px) {
      div {
        width: 130px;
        height: 130px;
      }

      .bottom {
        right: 7rem;
      }
    }
```

Alors, que se passe-t-il dans ce code ?

Les anneaux olympiques ont 5 cercles – 3 en haut et 2 en bas – avec les couleurs bleu, noir, rouge, jaune et vert, respectivement. 

Pour faire un cercle avec la propriété border-radius, nous définissons la largeur et la hauteur à 12.5rem chacune, puis le `border-radius` lui-même à 50%. C'est ainsi que vous faites un cercle avec CSS. 

Nous avons placé les anneaux supérieur et inférieur dans un conteneur parent, afin de pouvoir les placer l'un sur l'autre avec CSS Flexbox. Mais cela n'a pas terminé le travail, donc nous avons utilisé la propriété transform de l'animation CSS pour le terminer.

Enfin, nous avons apporté quelques petites modifications avec le positionnement CSS pour que les anneaux s'entrelacent. 

Au final, nous obtenons le résultat ci-dessous : 
![ss7](https://www.freecodecamp.org/news/content/images/2021/08/ss7.png)

## Conclusion 

J'espère que ce tutoriel vous aide à vous lancer avec la propriété CSS `border` afin que vous puissiez en faire un usage efficace dans vos projets. 

Merci beaucoup d'avoir lu et passez une bonne journée.