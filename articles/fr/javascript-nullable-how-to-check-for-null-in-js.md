---
title: JavaScript Nullable – Comment vérifier Null en JS
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2022-07-07T00:07:35.000Z'
originalURL: https://freecodecamp.org/news/javascript-nullable-how-to-check-for-null-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/javascript-null.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Nullable – Comment vérifier Null en JS
seo_desc: "Sometimes you've gotta check to make sure that nothing isn't actually...nothing.\
  \ \U0001F632❗❓ \nIn JavaScript, null is a primitive type intentionally containing\
  \ the value of null. Undefined is a primitive type and represents a variable you\
  \ declare without ini..."
---

Parfois, il faut vérifier que rien n'est en fait... rien. 😲⁉️❓

En JavaScript, **null** est un type primitif contenant intentionnellement la valeur null. **Undefined** est un type primitif et représente une variable que vous déclarez sans initialiser de valeur.

Donc, null est rien et undefined manque simplement quelque chose. 🤔

![Image](https://www.freecodecamp.org/news/content/images/2022/07/nothing.gif)
_null est rien ; undefined n'est pas quelque chose_

Pas super utile, je sais. Approfondissons.

## Comment définir les valeurs Null et Undefined

Un exemple aidera. Ci-dessous, nous déclarons deux variables. Gardons cela simple et utilisons `null` et `undefined` pour comparer les résultats, car ils sont parfois confondus en raison de leurs similitudes.

```javascript
let leviticus = null;
// leviticus est null

let dune;
// dune est undefined
```

`leviticus` est _intentionnellement_ sans valeur d'objet (**null**). Alors que `dune` est déclaré, mais il _manque involontairement_ une valeur (**undefined**).

## Comment vérifier Null avec `typeof()`

Vous pouvez vérifier null avec l'opérateur `typeof()` en JavaScript.

```javascript
console.log(typeof(leviticus))
// object

console.log(typeof(dune))
// undefined
```

Curieusement, si vous vérifiez avec `typeof()`, une variable null retournera `object`. Cela est dû à un [bug historique](https://www.turbinelabs.com/blog/the-odd-history-of-javascripts-null) dans JavaScript.

## Comment vérifier Null avec les opérateurs d'égalité

Une autre curiosité est que lorsque vous vérifiez l'égalité de manière lâche en utilisant [double equals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness) `==`, `null` et `undefined` retourneront `true`.

```javascript
console.log(leviticus == dune)
// true

console.log(leviticus === dune)
// false

console.log(leviticus == null)
// true (mais ce n'est pas une bonne habitude à utiliser, contrairement à l'égalité stricte montrée dans l'exemple suivant)
```

Mais lorsque vous vérifiez strictement l'égalité en utilisant [triple equals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness) `===`, null et undefined retourneront `false`.

Cela est dû au fait que null et undefined sont tous deux [falsy](https://developer.mozilla.org/en-US/docs/Glossary/Falsy) en JavaScript. Falsy signifie qu'une valeur est considérée comme `false` lorsqu'elle est rencontrée dans un contexte booléen (`true` ou `false`).

JavaScript utilise la coercition pour convertir des valeurs d'un type à un autre afin de pouvoir les utiliser dans un contexte booléen.

Mais en vérifiant strictement l'égalité, vous pouvez voir qu'ils ne sont en fait pas égaux.

## Comment vérifier Null avec l'égalité stricte

La meilleure façon de vérifier null est d'utiliser une égalité stricte et explicite :

```javascript
console.log(leviticus === null)
// true

console.log(dune === null)
// false
```

## Comment vérifier Null avec la méthode `Object.is()`

Une autre méthode infaillible pour vérifier null est d'utiliser la méthode intégrée `Object.is()` :

```javascript
console.log(Object.is(leviticus, null))
// true

console.log(Object.is(dune, null))
// false
```

## Résumé

* `null` est un type primitif de variable qui évalue à falsy, a un `typeof()` de object, et est typiquement déclaré intentionnellement comme `null`.
* `undefined` est un type primitif de variable qui évalue à falsy, a un `typeof()` de undefined, et représente une variable qui est déclarée mais manque d'une valeur initiale.
* `null == undefined` évalue à true car ils sont _lâchement_ égaux.
* `null === undefined` évalue à false car ils ne sont pas, _en fait_, égaux.
* `<variable_null> === null` est la **meilleure façon** de vérifier strictement null.
* `Object.is(<variable_null>, null)` est une **méthode tout aussi fiable** pour vérifier null.

Prenez courage ! Comme vous l'avez probablement compris, il y a une pléthore de casse-têtes dans l'écosystème JavaScript comme celui-ci. Mais lorsque vous le décomposez, vous pouvez les comprendre avec confiance.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/denzel.gif)
_Vous pouvez le faire !_

## Merci d'avoir lu !

J'espère que cela a été une explication utile pour vous. Continuez à coder, et continuez à avancer !

Venez me dire bonjour sur Twitter : [https://twitter.com/EamonnCottrell](https://twitter.com/EamonnCottrell)

Bonne journée 👋.