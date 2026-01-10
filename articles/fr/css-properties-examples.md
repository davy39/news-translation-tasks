---
title: Propriétés CSS – Max-width, Min-width, Max-height et Min-height expliquées
  avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-20T17:09:20.000Z'
originalURL: https://freecodecamp.org/news/css-properties-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/pexels-scott-webb-1544944.jpg
tags:
- name: CSS
  slug: css
- name: css properties
  slug: css-properties
- name: Web Development
  slug: web-development
seo_title: Propriétés CSS – Max-width, Min-width, Max-height et Min-height expliquées
  avec des exemples
seo_desc: 'By Nelson Michael

  If you''re building a website, making it responsive is one of the most important
  things you''ll do.

  It can be difficult to create websites that look good across a variety of screen
  sizes. You''ll have to handle rendering an element''s w...'
---

Par Nelson Michael

Si vous construisez un site web, le rendre réactif est l'une des choses les plus importantes que vous ferez.

Il peut être difficile de créer des sites web qui ont une belle apparence sur une variété de tailles d'écran. Vous devrez gérer le rendu de la largeur ou de la hauteur d'un élément, et spécifier des largeurs variées en utilisant des requêtes média n'est pas facile.

Bien que les unités relatives telles que "pourcentage" puissent être utiles dans certains contextes, elles peuvent aussi être désastreuses dans d'autres.

Mais ne vous inquiétez pas – des caractéristiques comme max-width et min-width sont là pour aider. Ces propriétés nous permettent d'éviter d'utiliser des requêtes média pour résoudre certains défis réactifs.

À la fin de cet article, vous saurez ce que sont max-width, min-width, max-height et comment les utiliser.

## La propriété Max-width

La propriété max-width vous permet de spécifier la largeur maximale d'un élément. Cela signifie qu'un élément peut augmenter en largeur jusqu'à ce qu'il atteigne une unité [absolue ou relative](https://www.freecodecamp.org/news/css-unit-guide/), moment auquel il doit fixer sa largeur à cette unité.

Voici ce dont je parle :

Imaginez définir la largeur d'un élément à **80%** de la largeur de la fenêtre. Si la fenêtre a une largeur de **375px**, notre élément aura une largeur de **300px**, ce qui n'est pas trop mal.

(80/100) * 375 = 300px

Mais que se passe-t-il si nous avions une fenêtre plus large, disons **1300px**, dans quel cas notre élément aura une largeur de **1040px**.

(80/100) * 1300 = 1040px

C'est là que la propriété max-width est utile. Lorsque vous utilisez des unités relatives comme un pourcentage, définir une propriété max-width sur un élément lui permet de continuer à augmenter en largeur jusqu'à ce qu'il atteigne un point que nous désignons.

Voici un exemple :

%[https://codepen.io/D_kingnelson/pen/mdmeEOV]

Remarquez comment la taille de notre carte n'a jamais dépassé **350px** ? C'est ainsi que fonctionne max-width. Il permet à notre carte de grandir sur les petits écrans.

Si la largeur est inférieure à 350px, elle prend 80% de la taille actuelle de l'écran. Mais dès que la largeur atteint 350px, elle se fixe et ne dépasse pas cette largeur définie.

Voici à quoi ressemble le code :

```
// La carte ne peut pas devenir plus grande que 350px.

.card{
  margin:0 auto;
  padding:1.5em;
  width:80%;
  max-width:350px;
  height:50%;
  background: #FFFFFF;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
  border-radius:4px;
  overflow:hidden;
}
```

## La propriété Min-Width

Contrairement à la propriété max-width, la propriété min-width spécifie la largeur minimale. Elle indique la largeur minimale possible pour un élément.

Dans certains cas, vous pouvez vouloir que votre élément ait une largeur flexible, vous lui donnez donc une largeur dans une unité relative telle qu'un pourcentage. Mais à mesure que l'écran rétrécit, la largeur de l'élément rétrécit également.

C'est là que min-width intervient – vous pouvez définir une largeur minimale afin que la carte sache ne pas rétrécir en dessous de la largeur spécifiée.

%[https://codepen.io/D_kingnelson/pen/zYwdzxW]

```
// Ici, l'élément carte ne peut pas devenir plus petit que 250px
.card{
  margin:0 auto;
  padding:1.5em;
  width:80%;
  max-width:350px;
  // ici nous définissons la propriété min-width
  min-width : 250px;
  height:50%;
  background: #FFFFFF;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
  border-radius:4px;
  overflow:hidden;
}
```

## La propriété Max-Height

La propriété max-height fonctionne de manière similaire à la propriété max-width, mais elle affecte la hauteur au lieu de la largeur.

Voici un exemple :

%[https://codepen.io/D_kingnelson/pen/gOWxRrb]

```
// elle fixe la hauteur d'un élément à une unité spécifiée, l'empêchant effectivement d'augmenter en hauteur

.card{
  margin:0 auto;
  padding:1.5em;
  width:80%;
  max-width:350px;
  height:70%;
  // ici nous définissons la max-height pour la carte.
  max-height: 400px;
  background: #FFFFFF;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
  border-radius:4px;
  overflow:hidden;
}
```

## La propriété Min-Height

Contrairement à max-height, la propriété min-height fournit une hauteur minimale pour un élément.

Cela se produit lorsque la fenêtre rétrécit et que la hauteur de l'élément ne peut pas être réduite au-delà d'une unité de hauteur définie.

%[https://codepen.io/D_kingnelson/pen/yLboXVz]

```
.element{
    height:40vh;
    min-height:200px;
}
```

## Conclusion

La réactivité est un facteur important à considérer dans le développement web. Garder une trace de l'apparence des choses sur plusieurs tailles d'écran peut être difficile, mais les propriétés max-width, min-width, max-height et min-height aident à relever ces défis.

Ces propriétés vous permettent d'ajuster la taille des éléments sans avoir besoin d'utiliser des requêtes média.