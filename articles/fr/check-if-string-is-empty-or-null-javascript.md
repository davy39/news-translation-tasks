---
title: Comment vérifier si une chaîne est vide ou nulle en JavaScript – Tutoriel JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-05-03T17:26:58.000Z'
originalURL: https://freecodecamp.org/news/check-if-string-is-empty-or-null-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/cover-template--13-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment vérifier si une chaîne est vide ou nulle en JavaScript – Tutoriel
  JS
seo_desc: 'In JavaScript, it''s important to check whether a string is empty or null
  before performing any operation. Trying to operate on an empty or null string can
  lead to errors, bugs, and unexpected results.

  In this tutorial, we''ll explore the different way...'
---

En JavaScript, il est important de vérifier si une chaîne est vide ou nulle avant d'effectuer une opération. Essayer d'opérer sur une chaîne vide ou nulle peut entraîner des erreurs, des bugs et des résultats inattendus.

Dans ce tutoriel, nous explorerons les différentes façons de vérifier si une chaîne est vide ou nulle en JavaScript et quelques bonnes pratiques à suivre pour le faire.

## Qu'est-ce qu'une chaîne vide ou nulle ?

Une chaîne vide est une chaîne qui n'a aucun caractère, tandis qu'une chaîne nulle est une chaîne qui n'a aucune valeur assignée. Il est important de différencier les deux, car elles ne sont pas identiques.

Par exemple, vous avez un formulaire où un utilisateur peut saisir son nom. Si l'utilisateur ne saisit rien, la valeur du champ d'entrée sera une chaîne vide. Cependant, la valeur sera nulle si le champ d'entrée n'est même pas créé.

## Comment vérifier si une chaîne est vide ou nulle

JavaScript offre plusieurs façons de vérifier si une chaîne est vide ou nulle. Explorons quelques-unes.

### Utilisation de l'instruction if et de l'opérateur typeof

Une façon de vérifier si une chaîne est vide ou nulle consiste à utiliser l'instruction `if` et l'opérateur `typeof`. Voici un exemple :

```js
let str = "";

if (typeof str === "string" && str.length === 0) {
  console.log("La chaîne est vide");
} else if (str === null) {
  console.log("La chaîne est nulle");
} else {
  console.log("La chaîne n'est ni vide ni nulle");
}
```

Dans cet exemple, nous vérifions si la variable `str` est une chaîne et si sa longueur est égale à zéro. Si c'est le cas, nous savons qu'il s'agit d'une chaîne vide. Si la variable `str` est `null`, nous savons qu'il s'agit d'une chaîne nulle. Sinon, nous savons que la chaîne n'est ni vide ni nulle.

### Utilisation de la propriété length

Une autre façon de vérifier si une chaîne est vide consiste à utiliser la propriété `length`. Voici un exemple :

```js
let str = "";

if (str.length === 0) {
  console.log("La chaîne est vide");
} else {
  console.log("La chaîne n'est pas vide");
}
```

Dans cet exemple, nous vérifions si la longueur de la variable `str` est égale à zéro. Si c'est le cas, nous savons qu'il s'agit d'une chaîne vide. Sinon, nous savons que la chaîne n'est pas vide.

### Utilisation de la méthode trim

Parfois, une chaîne peut contenir des caractères d'espace qui la font paraître non vide alors qu'elle l'est. Dans de tels cas, nous pouvons utiliser la méthode `trim` pour supprimer les caractères d'espace en début ou en fin de chaîne avant de vérifier si elle est vide. Voici un exemple :

```js
let str = "   ";

if (str.trim().length === 0) {
  console.log("La chaîne est vide");
} else {
  console.log("La chaîne n'est pas vide");
}
```

Dans cet exemple, nous utilisons d'abord la méthode `trim` pour supprimer les caractères d'espace en début ou en fin de la variable `str`, puis nous vérifions si la chaîne résultante a une longueur de zéro. Si c'est le cas, nous savons que la chaîne est vide. Sinon, nous savons que la chaîne n'est pas vide.

## Bonnes pratiques pour vérifier si une chaîne est vide ou nulle

Voici quelques bonnes pratiques à suivre lors de la vérification de chaînes vides ou nulles en JavaScript :

* Utilisez toujours l'égalité stricte (`===`) lors de la comparaison d'une chaîne avec `null`. Cela garantit que les types sont vérifiés et évite de comparer accidentellement une chaîne avec le nombre `0` ou `false`.

* Utilisez l'égalité stricte (`===`) lors de la vérification d'une chaîne vide. Cela garantit que vous ne comparez pas une chaîne vide avec une chaîne contenant uniquement des caractères d'espace.

* Utilisez la méthode `trim` pour supprimer les caractères d'espace en début et en fin de chaîne avant de vérifier si elle est vide. Cela garantit que les chaînes contenant uniquement des caractères d'espace sont également considérées comme vides.

* Utilisez des expressions régulières pour des vérifications plus complexes, telles que vérifier si une chaîne ne contient que des chiffres ou si elle correspond à un certain motif.

Par exemple :

```js
let str = "12345";
let digitRegExp = /^\d+$/;

if (digitRegExp.test(str)) {
  console.log("La chaîne ne contient que des chiffres");
} else {
  console.log("La chaîne ne contient pas uniquement des chiffres");
}
```

## Conclusion

Dans cet article, nous avons appris comment vérifier si une chaîne est vide ou nulle en JavaScript. Nous avons exploré différentes méthodes pour le faire, telles que l'utilisation de l'instruction `if` et de l'opérateur `typeof`, de la propriété `length` et de la méthode `trim`.

Si vous souhaitez en savoir plus sur JavaScript et le développement web, [parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents) écrits par moi, et consultez également [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant.

Amusez-vous bien à coder !