---
title: Comment vérifier si un tableau JavaScript est vide ou non avec .length
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-05T23:08:04.000Z'
originalURL: https://freecodecamp.org/news/check-if-javascript-array-is-empty-or-not-with-length
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/road-690087_1920.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment vérifier si un tableau JavaScript est vide ou non avec .length
seo_desc: 'By Madison Kanna

  When you''re programming in JavaScript, you might need to know how to check whether
  an array is empty or not.

  To check if an array is empty or not, you can use the .length property.

  The length property sets or returns the number of el...'
---

Par Madison Kanna

Lorsque vous programmez en JavaScript, vous pourriez avoir besoin de savoir comment vérifier si un tableau est vide ou non.

Pour vérifier si un tableau est vide ou non, vous pouvez utiliser la propriété .length.

La propriété length définit ou retourne le nombre d'éléments dans un tableau. En connaissant le nombre d'éléments dans le tableau, vous pouvez dire s'il est vide ou non. Un tableau vide aura `0` éléments à l'intérieur.

Passons en revue quelques exemples.

### Voici un Scrim interactif montrant comment vérifier si un tableau JavaScript est vide ou non avec .length :

<iframe src="https://scrimba.com/scrim/cpJWbLud?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## Syntaxe d'exemple de .length

```javascript
const myArray = ['Horses', 'Dogs', 'Cats'];
```

Ici, nous créons une variable pointant vers un tableau.

En utilisant la propriété length, nous pouvons vérifier la longueur du tableau :

```javascript
myArray.length
```

Cela retournera 3, car il y a 3 éléments dans le tableau.

Pour vérifier si le tableau est vide ou non avec .length, nous pouvons le faire de trois manières.

### Exemple .length un

Tout d'abord, créons un nouveau tableau sans éléments.

```javascript
const arr = []
```

Maintenant, nous pouvons vérifier si le tableau est vide en utilisant `.length`.

```javascript
arr.length
```

Cela retournera 0, car il y a 0 éléments dans le tableau.

### Exemple .length deux

Nous pouvons également vérifier explicitement si le tableau est vide ou non.

`if (arr.length === 0) { console.log("Le tableau est vide !") }`

Si notre tableau est vide, le message ci-dessus sera enregistré. Si le tableau contient des éléments, le code dans le bloc `if` ne s'exécutera pas.

Voici la troisième façon de vérifier si un tableau est vide ou non en utilisant .length.

### Exemple .length trois

En combinant l'utilisation de la propriété length et de l'opérateur logique "not" en JavaScript, le symbole "!", nous pouvons vérifier si un tableau est vide ou non.

L'opérateur `!` nie une expression. C'est-à-dire que nous pouvons l'utiliser pour retourner `true` si un tableau est vide.

Pour cet exemple, ouvrons notre console JavaScript. Pour ouvrir votre console dans Chrome, vous pouvez cliquer sur Inspecter -> Console.

Tout d'abord, créez un tableau sans éléments.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image.png)

Ensuite, utilisons l'opérateur logique "not", ainsi que notre propriété .length, pour tester si le tableau est vide ou non.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screen-Shot-2020-09-30-at-5.29.35-PM.png)

Si nous n'avions pas utilisé l'opérateur "not", `arr.length` aurait retourné `0`. Avec l'opérateur ajouté, il retournera `true` si son opérande est `false`. Parce que arr.length est `0`, ou false, il retourne `true`.

Utilisons cela avec une instruction `if`, et affichons un message si notre tableau est vide.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-2.png)

Lors de la vérification si un tableau est vide ou non, il est souvent préférable de vérifier également si le tableau est bien un tableau.

Pourquoi ?

Parce qu'il pourrait y avoir un cas où vous vous attendiez à vérifier la longueur d'un tableau, mais au lieu de cela, vous recevez un autre type de données, par exemple, une chaîne de caractères :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-7.png)

Parce que la `propriété length` peut être utilisée sur d'autres types de données, il est bon de vérifier également que votre tableau est bien un tableau comme vous vous y attendiez.

Je vous suggère également d'utiliser la méthode `Array.isArray()` pour confirmer que votre tableau est un tableau. Cette méthode détermine si ce qui a été passé en paramètre est un tableau ou non. Si ce qui a été passé en paramètre était un tableau, cette méthode retournera `true`.

Ajoutons cette méthode à notre exemple.

### Comment utiliser la méthode Array.isArray()

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-3.png)

## Conclusion

Dans cet article, nous avons appris que vous pouvez utiliser la propriété `length` en JavaScript de diverses manières pour vérifier si un tableau est vide ou non. La propriété `length` retourne le nombre d'éléments dans un tableau.

Nous avons également appris qu'il est préférable d'utiliser également la méthode `Array.isArray` lors de l'utilisation de la propriété `.length`, pour vérifier si la valeur passée est un tableau comme vous vous y attendez.