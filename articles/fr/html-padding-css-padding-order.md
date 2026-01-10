---
title: HTML Padding – Ordre de la marge intérieure CSS
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-04T21:33:13.000Z'
originalURL: https://freecodecamp.org/news/html-padding-css-padding-order
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/kobu-agency-ipARHaxETRk-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: HTML Padding – Ordre de la marge intérieure CSS
seo_desc: "In this article, we are going to learn about CSS padding properties, the\
  \ shorthand property, and how padding differs from margin. \nWhat is padding in\
  \ CSS?\nCSS padding creates space around the element's content. This space is within\
  \ the element's bord..."
---

Dans cet article, nous allons apprendre les propriétés de marge intérieure CSS, la propriété raccourcie et comment la marge intérieure diffère de la marge. 

## Qu'est-ce que la marge intérieure en CSS ?

La marge intérieure CSS crée de l'espace autour du contenu de l'élément. Cet espace se trouve à l'intérieur de la bordure et de la marge de l'élément. 

Examinons le modèle de boîte CSS pour mieux comprendre comment fonctionne la marge intérieure. Chaque élément HTML a une boîte autour de lui et est composé de quatre parties : contenu, marge intérieure, bordure et marge. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-03-at-1.38.36-AM.png)

La section bleue est le contenu de l'élément tandis que la section verte représente la marge intérieure. Remarquez comment la marge intérieure se trouve à l'intérieur des propriétés de bordure et de marge. 

Examinons les propriétés de marge intérieure de CSS plus en détail.

### Propriété padding-top

Il s'agit d'une propriété CSS qui ajoute de l'espace en haut d'un élément. 

```css
  padding-top: 20px;
```

%[https://codepen.io/jessica-wilkins/pen/poPOjjw]

### Propriété padding-right

Il s'agit d'une propriété CSS qui ajoute de l'espace à droite d'un élément. 

```css
  padding-right: 40px;

```

%[https://codepen.io/jessica-wilkins/pen/ExmeVKp]

### Propriété padding-bottom

Il s'agit d'une propriété CSS qui ajoute de l'espace en bas d'un élément. 

```css
  padding-bottom: 20px;

```

%[https://codepen.io/jessica-wilkins/pen/QWvVjKv]

### Propriété padding-left

Il s'agit d'une propriété CSS qui ajoute de l'espace à gauche d'un élément. 

```css
  padding-left: 40px;

```

%[https://codepen.io/jessica-wilkins/pen/GRmXprJ]

## Différence entre la marge intérieure et la marge en CSS

La marge crée de l'espace autour de l'élément et à l'extérieur de sa bordure. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-03-at-1.38.36-AM.png)

Cet exemple ajoute 50px de marge inférieure à l'élément `h1`. Cela crée un espace supplémentaire entre les éléments `h1` et `p`. 

```css
margin-bottom: 50px;
```

%[https://codepen.io/jessica-wilkins/pen/XWRBVRJ?editors=1100]

## Propriété raccourcie de la marge intérieure

La propriété raccourcie de la marge intérieure nous permet de définir la marge intérieure sur les quatre côtés à la fois au lieu d'écrire `padding-top`, `padding-right`, `padding-bottom`, `padding-left`. 

Lorsque vous utilisez une seule valeur, des quantités égales de marge intérieure seront appliquées sur tous les côtés. 

```css
 padding: 10px;
```

Voici le code sans la propriété raccourcie :

```css
  padding-top: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  padding-left: 10px;
```

Voici à quoi ressemblerait le résultat dans le navigateur.

%[https://codepen.io/jessica-wilkins/pen/YzVjrBb?editors=1100]

Lorsque vous utilisez deux valeurs, la première valeur ajoute de la marge intérieure en haut et en bas tandis que la deuxième valeur ajoute de la marge intérieure à gauche et à droite.

```css
  padding: 10px 30px;

```

Voici le code sans la propriété raccourcie :

```css
  padding-top: 10px;
  padding-right: 30px;
  padding-bottom: 10px;
  padding-left: 30px;
```

%[https://codepen.io/jessica-wilkins/pen/xxdJPgB]

Lorsque vous utilisez trois valeurs, la première valeur ajoute de la marge intérieure en haut, la deuxième valeur ajoute de la marge intérieure à droite et à gauche, et la troisième valeur ajoute de la marge intérieure en bas. 

```css
  padding: 10px 30px 50px;

```

Voici le code sans la propriété raccourcie :

```css
  padding-top: 10px;
  padding-right: 30px;
  padding-bottom: 50px;
  padding-left: 30px;
```

%[https://codepen.io/jessica-wilkins/pen/vYmaWjG]

Et lorsque vous utilisez quatre valeurs, la première valeur ajoute de la marge intérieure en haut, la deuxième valeur ajoute de la marge intérieure à droite, la troisième valeur ajoute de la marge intérieure en bas et la quatrième valeur ajoute de la marge intérieure à gauche.

Le meilleur moyen de se souvenir de l'ordre pour les quatre valeurs est de penser dans le sens des aiguilles d'une montre (haut, droite, bas, gauche).

```css
  padding: 10px 20px 30px 40px;
```

Voici le code sans la propriété raccourcie :

```css
  padding-top: 10px;
  padding-right: 20px;
  padding-bottom: 30px;
  padding-left: 40px;
```

%[https://codepen.io/jessica-wilkins/pen/jOmpaRp]

Vous pouvez choisir d'utiliser des pixels, em, rem ou des pourcentages pour les valeurs. Mais vous n'êtes pas autorisé à utiliser des valeurs négatives.

## Conclusion

Lorsque vous souhaitez ajouter de l'espace autour du contenu d'un élément HTML, vous utiliserez les propriétés de marge intérieure. 

La propriété raccourcie de la marge intérieure nous permet de définir la marge intérieure sur les quatre côtés à la fois au lieu d'écrire `padding-top`, `padding-right`, `padding-bottom`, `padding-left`. 

Si vous souhaitez créer de l'espace entre les éléments, vous utiliserez les propriétés de marge. Avec la marge, vous pouvez utiliser des valeurs négatives, alors qu'avec la marge intérieure, cela n'est pas autorisé.