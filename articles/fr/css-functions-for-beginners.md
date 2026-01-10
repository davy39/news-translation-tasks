---
title: Fonctions CSS – Comment utiliser calc(), max(), min() et clamp()
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-05-18T15:11:08.000Z'
originalURL: https://freecodecamp.org/news/css-functions-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-katerina-holmes-5905965.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: CSS
  slug: css
seo_title: Fonctions CSS – Comment utiliser calc(), max(), min() et clamp()
seo_desc: "In CSS there are a lot of different units of measurement. You have px and\
  \ percentages, vh, vw, em, rem, and others. \nThere will come a time when you want\
  \ to get a value by combining two or more different units. CSS has a function that\
  \ you can use to ..."
---

En CSS, il existe de nombreuses unités de mesure différentes. Vous avez les px et les pourcentages, vh, vw, em, rem, et d'autres.

Il arrivera un moment où vous voudrez obtenir une valeur en combinant deux unités différentes ou plus. CSS dispose d'une fonction que vous pouvez utiliser pour effectuer de tels calculs – `calc()`. Et dans ce tutoriel, vous apprendrez comment elle fonctionne.

Il existe d'autres fonctions que vous pouvez utiliser avec ces unités relatives – comme `max`, `min` et `clamp` – qui, confrontées à différentes valeurs, utilisent celle qui est appropriée. Ces fonctions sont vraiment utiles dans les mises en page responsives et peuvent être une alternative à l'utilisation des media queries.

Si vous apprenez à les utiliser de manière appropriée, vous pouvez éviter le changement saccadé de mise en page qui peut se produire lors du redimensionnement d'une fenêtre si vous utilisiez des media queries, et avec moins de code !

## Comment utiliser la fonction CSS `calc()`

La fonction calc prend un seul paramètre. Ce paramètre peut être une expression combinant n'importe quelle unité de longueur et les quatre opérateurs mathématiques `+`, `-`, `/`, `*`.

Vous pouvez également utiliser des parenthèses pour indiquer un ordre d'évaluation différent des règles de priorité standard.

Dans l'expression à l'intérieur de la fonction `calc()`, vous pouvez utiliser des variables CSS, des valeurs obtenues avec `[attr()](https://developer.mozilla.org/en-US/docs/Web/CSS/attr)`, et des valeurs des fonctions `max()`, `min()` et `clamp()`.

`calc()` vous permet de calculer une valeur à partir de paramètres complexes.

```css
div {
    width: calc(100% - 2em);
}
```

**Note** : laissez toujours un espace de chaque côté des opérateurs mathématiques.

## Comment utiliser la fonction CSS `max()`

La fonction `max` accepte une liste de valeurs séparées par des virgules et retourne la plus grande. Chaque valeur peut également être une expression (tout ce que vous pouvez utiliser comme argument pour la fonction `calc()` peut être l'un des arguments de cette fonction également).

La fonction max peut être considérée comme un moyen de déterminer une _valeur minimale_ pour une certaine chose.

Un cas d'utilisation pour cette fonction est de rendre un texte responsive, tout en donnant une valeur minimale à la dimension.

Par exemple :

```css
h1 {
    font-size: max(1rem, 10vh);
}
```

De cette manière, le texte sera un dixième de la hauteur de la fenêtre, sauf si la hauteur de la fenêtre devient trop petite. Le texte aura toujours une `font-size` d'au moins `1rem` pour assurer la lisibilité.

## Comment utiliser la fonction CSS `min()`

De la même manière que la fonction max, `min` peut prendre n'importe quel nombre d'arguments, y compris d'autres fonctions `max`, `min` ou `clamp`, et retourner la plus petite valeur parmi elles.

La fonction min peut être considérée comme déterminant une _valeur maximale_.

Par exemple, supposons que vous créez un formulaire et que vous souhaitez qu'il soit responsive lorsque la largeur de l'écran change. Vous voudrez lui donner une largeur maximale pour éviter cet étirement horizontal qui peut se produire sur les plus grands écrans.

Vous pourriez écrire quelque chose comme ceci :

```css
.form {
    width: min(600px, 90vw);
}
```

Votre page aura une largeur égale à 90 % de la largeur de la fenêtre, ou 600 px de large, selon la plus petite des deux. Ainsi, si la largeur de la fenêtre est supérieure à ~670 px, le formulaire ne s'étirera pas horizontalement.

## Exemple pour `min()` et `max()` :

Vous pouvez voir les extraits de code en action dans ce pen. Essayez de redimensionner le pen horizontalement et verticalement et voyez la largeur du formulaire et la taille de la police changer de manière responsive.

%[https://codepen.io/nethleen/pen/XWZMGVd]

## Comment utiliser la fonction CSS `clamp()`

La fonction clamp limite une valeur entre une limite supérieure et une limite inférieure. Elle sélectionne une valeur dans une plage avec des limites définies.

`clamp` prend trois valeurs. La première sera la valeur minimale, la deuxième la valeur préférée, et la troisième la valeur maximale.

La fonction clamp retournera la valeur préférée, sauf si elle est plus petite que la valeur minimale (auquel cas elle retournera la valeur minimale) ou si elle est plus grande que la valeur maximale, auquel cas elle retournera la valeur maximale.

Vous pouvez utiliser `clamp` pour redimensionner de manière responsive les éléments de mise en page dans une plage.

```css
h1 {
    font-size: clamp(1rem, 10vw, 2rem);
}

div {
    padding: clamp(10px, 6vw, 50px);
    width: clamp(140px, 90vw, 600px);
}
```

## Exemple de la fonction `clamp` :

Voir cela en action dans ce pen ! Redimensionnez le pen horizontalement et voyez comment les différents éléments changent de dimensions.

%[https://codepen.io/nethleen/pen/ExQWJZo]

Le MDN propose plus d'informations détaillées sur toutes ces fonctions :

* [calc](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)
* [max](https://developer.mozilla.org/en-US/docs/Web/CSS/max)
* [min](https://developer.mozilla.org/en-US/docs/Web/CSS/min)
* [clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)

Et avec cela, vous avez vu un aperçu de ces quatre fonctions merveilleuses. Vous en savez assez pour commencer à les utiliser, alors allez-y et amusez-vous !