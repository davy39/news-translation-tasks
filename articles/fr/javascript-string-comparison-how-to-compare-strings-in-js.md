---
title: Comparaison de chaînes JavaScript – Comment comparer des chaînes en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-01T22:07:46.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-comparison-how-to-compare-strings-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/string-comparison.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comparaison de chaînes JavaScript – Comment comparer des chaînes en JS
seo_desc: 'By Dillion Megida

  You may want to compare two strings to know which is higher or lower alphabetically
  or to see if they are equal.

  You can do this in many ways. I''ll show you two of them in this article.

  1. How to Compare Strings Using localeCompare

  ...'
---

Par Dillion Megida

Vous pouvez vouloir comparer deux chaînes pour savoir laquelle est plus haute ou plus basse alphabétiquement ou pour voir si elles sont égales.

Vous pouvez le faire de plusieurs manières. Je vais vous en montrer deux dans cet article.

## 1. Comment comparer des chaînes en utilisant localeCompare

Vous pouvez utiliser la méthode `localeCompare` pour comparer deux chaînes dans la locale actuelle. Voici la syntaxe :

```js
string1.localeCompare(string2)
```

`localeCompare` retourne :

* 1 si `string1` est plus grande (plus haute dans l'ordre alphabétique) que `string2`
* -1 si `string1` est plus petite (plus basse dans l'ordre alphabétique) que `string2`
* 0 si `string1` et `string2` sont égales dans l'ordre alphabétique

Voici quelques exemples comparant deux chaînes :

```js
const string1 = "hello"
const string2 = "world"

const compareValue = string1.localeCompare(string2)
// -1
```

Cela donne `-1` parce que, dans la locale anglaise, **h** dans hello vient avant **w** dans world (w est plus bas dans l'ordre alphabétique que h).

Un autre exemple :

```js
const string1 = "banana"
const string2 = "back"

const compareValue = string1.localeCompare(string2)
// 1
```

La comparaison ci-dessus donne `1` parce que, dans la locale anglaise, ba**n** dans banana vient après ba**c** dans back.

Un exemple de plus :

```js
const string1 = "fcc"
const string2 = "fcc"
const string3 = "Fcc"

const compareValue1 = string1.localeCompare(string2)
// 0

const compareValue2 = string1.localeCompare(string3)
// -1
```

Comparer "fcc" et "fcc" donne `0` parce qu'elles sont égales dans l'ordre. "fcc" et "Fcc" donne `-1` parce que la majuscule "F" est plus grande que le petit "f".

Dans certains navigateurs, au lieu de **-1**, cela peut retourner **-2** ou une autre valeur négative. Donc, ne dépendez pas de **-1** ou **1**, mais plutôt des valeurs négatives (inférieures à 0) ou positives (supérieures à 0).

## 2. Comment comparer des chaînes en utilisant des opérateurs mathématiques

Vous pouvez également utiliser des opérateurs mathématiques comme supérieur à (**>**), inférieur à (**<**), et égal à lors de la comparaison de chaînes.

Les opérateurs mathématiques fonctionnent de manière similaire à `localeCompare` – en retournant des résultats basés sur l'ordre des caractères dans la chaîne.

En utilisant les exemples précédents :

```js
const string1 = "hello"
const string2 = "world"

console.log(string1 > string2)
// false
```

`string1` n'est pas plus grande que `string2`, parce que **h** vient avant **w**, donc elle est plus petite.

Pour l'autre exemple :

```js
const string1 = "banana"
const string2 = "back"

console.log(string1 > string2)
// true
```

`string1` est plus grande que `string2` parce que ba**n** vient après ba**c**k.

Et pour le dernier exemple :

```js
const string1 = "fcc"
const string2 = "fcc"
const string3 = "Fcc"

console.log(string1 === string2)
// true

console.log(string1 < string3)
// false
```

`string1` est égale à (`===`) `string2`, mais `string1` n'est pas plus petite que `string3`, ce qui contraste avec `localeCompare`.

Avec les opérateurs mathématiques, "fcc" est plus grande que "Fcc", mais avec `localeCompare`, `"fcc".localeCompare("Fcc")` retourne `-1` pour montrer que "fcc" est plus petite que "Fcc".

Ce comportement est une raison pour laquelle je ne recommande pas d'utiliser les opérateurs mathématiques pour comparer des chaînes, même s'ils ont le potentiel de le faire.

Une autre raison pour laquelle je ne recommande pas d'utiliser les opérateurs mathématiques est que `"fcc" > "fcc"` et `"fcc" < "fcc"` est `false`. "fcc" est égale à "fcc". Donc, si vous dépendez des opérateurs mathématiques, obtenir `false` peut être pour des raisons différentes de celles que vous croyez.

Donc, pour comparer des chaînes, parmi les nombreuses méthodes qui peuvent exister, utiliser `localeCompare` est une approche efficace car elle peut être utilisée pour différentes langues.

Maintenant, vous connaissez une manière facile de comparer des chaînes. Bon codage !