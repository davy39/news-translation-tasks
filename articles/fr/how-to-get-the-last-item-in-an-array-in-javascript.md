---
title: Comment obtenir le dernier élément d'un tableau en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-17T21:21:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-last-item-in-an-array-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/web-design-g911869a8e_1920.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment obtenir le dernier élément d'un tableau en JavaScript
seo_desc: 'By Madison Kanna

  When you’re programming in JavaScript, you might need to get the last item in an
  array. In this tutorial, we’ll go over two different ways to do this.

  How to Get the Last Item in a JavaScript Array

  Method 1: Use index positioning

  Use...'
---

Par Madison Kanna

Lorsque vous programmez en JavaScript, vous pourriez avoir besoin d'obtenir le dernier élément d'un tableau. Dans ce tutoriel, nous allons passer en revue deux méthodes différentes pour y parvenir.

## Comment obtenir le dernier élément d'un tableau JavaScript

### Méthode 1 : Utiliser le positionnement par index

Utilisez le positionnement par index si vous connaissez la longueur du tableau.

Créons un tableau :

```js
const animals = ['cat', 'dog', 'horse']
```

Ici, nous pouvons voir que le dernier élément de ce tableau est `horse`.

Pour obtenir le dernier élément, nous pouvons accéder à celui-ci en fonction de son index :

`const finalElement = animals[2]`;

Les tableaux JavaScript sont indexés à partir de zéro. C'est pourquoi nous pouvons accéder à l'élément `horse` avec `animals[2]`. Si vous n'êtes pas sûr de ce que signifie "indexé à partir de zéro", nous l'expliquerons plus tard dans ce tutoriel.

Cette méthode pour obtenir le dernier élément du tableau fonctionne si vous connaissez la longueur du tableau.

Mais que faire si vous ne connaissez pas la longueur du tableau ? Ce tableau, `animals`, est très petit. Mais vous pourriez avoir un autre tableau contenant des dizaines d'éléments, et vous ne connaissez peut-être pas sa longueur.

### Méthode 2 : Lorsque vous ne connaissez pas la longueur du tableau

Pour obtenir le dernier élément d'un tableau lorsque vous ne connaissez pas sa longueur :

`const lastItem = animals[animals.length - 1]`;

La variable `lastItem` contient maintenant la valeur `horse`.

Analysons ce qui se passe dans la ligne ci-dessus. Tout d'abord, affichons simplement `animals.length` dans la console :

`console.log(animals.length);`

Si vous n'êtes pas familier avec la propriété `length`, elle retourne la longueur de ce tableau. Cela affiche `3`, car il y a `3` éléments dans le tableau.

Nous avons appris précédemment que les tableaux JavaScript sont indexés à partir de zéro. Cela signifie simplement que dans les tableaux JavaScript, vous commencez à compter à partir de zéro au lieu de un. Nous pouvons le voir en regardant notre tableau `animals`. `cat` est à l'index `0`, `dog` est à l'index `1`, et `horse` est à l'index `2`.

Vous pourriez encore être confus. Nous venons d'apprendre que `animals.length` nous indique combien d'éléments il y a dans un tableau. Nous avons également appris qu'avec les tableaux JavaScript, nous commençons à compter à partir de zéro au lieu de un. Mais comment cela aide-t-il à expliquer pourquoi nous pouvons obtenir le dernier élément de ce tableau en utilisant `animals[animals.length - 1]` ?

Imaginons un instant que les tableaux JS n'étaient *pas* indexés à partir de zéro, et que nous commencions à compter à partir de 1, ce qui est la façon dont nous comptons normalement les choses dans le monde réel.

Avec le tableau `animals`, nous pourrions rapidement commencer à compter et dire que `cat`, le premier élément, a un index de 1, `dog` a un index de `2`, et `horse` a un index de `3`. L'idée clé ici est que, dans l'indexation à base un, *l'index du dernier élément est la longueur du tableau*. Si le tableau a une longueur de 3, vous savez que le dernier élément du tableau a un index de `3`. Ainsi, `animals[3]` évaluerait à `horse`.

Pourtant, les tableaux JavaScript commencent à partir de `0`. Donc, si nous voulons déterminer l'index du dernier élément d'un tableau JavaScript, nous pouvons soustraire 1 de la longueur du tableau :

`animals[animals.length - 1]`;

À l'intérieur des crochets, `animals.length - 1` évalue à `2`. Nous avons maintenant le dernier élément du tableau.

Dans cet article, nous avons appris deux méthodes pour obtenir le dernier élément d'un tableau JavaScript.

Merci d'avoir lu !

**Si vous avez aimé cet article, rejoignez mon [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), où nous relevons des défis de codage ensemble chaque dimanche et nous soutenons mutuellement tout en apprenant de nouvelles technologies.**

**Si vous avez des commentaires ou des questions sur cet article, ou retrouvez-moi sur Twitter [@madisonkanna](https://twitter.com/Madisonkanna).**