---
title: Comment définir des propriétés d'objet dynamiques en utilisant les noms de
  propriétés calculés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-17T16:53:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-dynamic-object-properties-using-computed-property-names
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/20.-dynamic-object-properties-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment définir des propriétés d'objet dynamiques en utilisant les noms
  de propriétés calculés
seo_desc: "By Dillion Megida\nWhen declaring objects before ES6, you had to use static\
  \ keys for properties. But since the release of ES6, you can use dynamic keys. \n\
  I'll show you how they work in this article.\nWhat are Static and Dynamic Keys?\n\
  What do I mean by ..."
---

Par Dillion Megida

Avant ES6, lors de la déclaration d'objets, vous deviez utiliser des clés statiques pour les propriétés. Mais depuis la sortie d'ES6, vous pouvez utiliser des clés dynamiques. 

Je vais vous montrer comment elles fonctionnent dans cet article.

## Qu sont les clés statiques et dynamiques ?

Que veux-je dire par clés statiques ? Jetez un coup d'œil à cet objet :

```js
const obj = {
  name: "dillion",
  age: 1000,
}
```

Vous pouvez voir que `name` et `age` sont des clés statiques. Elles ne proviennent de nulle part – elles ne sont pas calculées. Ces clés sont directement ajoutées à l'objet.

Et si vous vouliez ajouter une clé dynamique ? Une clé dynamique fait ici référence au résultat d'une expression. Par exemple, une clé dynamique peut être une variable ou une valeur calculée.

Je vais vous montrer comment faire cela dans cet article.

J'ai une [version vidéo](https://youtu.be/iP02oY4rt6A) de ce sujet que vous pouvez également consulter.

## La fonctionnalité des noms de propriétés calculés

La fonctionnalité des noms de propriétés calculés dans ES6 vous permet de définir des noms de propriétés de manière dynamique – c'est-à-dire que les noms de propriétés seront des expressions qui évaluent à une valeur.

Cette fonctionnalité est utile pour les noms de propriétés que vous ne connaissez pas à l'avance. Pour un nom de propriété comme "name", vous le connaissez déjà, donc vous pouvez créer votre objet comme ceci :

```js
const object = {
  name: value
}  
```

Mais qu'en est-il d'un nom de propriété qui provient d'une expression exécutée pendant l'exécution ? Une telle expression peut être une concaténation, un appel de fonction, ou une expression conditionnelle, pour n'en nommer que quelques-unes. 

Dans de tels cas, vous ne connaissez pas le nom de la propriété à l'avance. Et c'est là que vous utilisez la fonctionnalité des noms de propriétés calculés.

Pour utiliser des valeurs calculées pour les noms de propriétés, vous utilisez des crochets et passez l'expression.

Voici la syntaxe :

```js
const object = {
  [expression]: value
}
```

### Comment définir des variables comme noms de propriétés

Regardons un exemple de variable :

```js
const key1 = "language"
const key2 = "isStudent"

const obj = {
  name: "dillion",
  age: 1000,
  [key1]: "javascript",
  [key2]: true
}

console.log(obj)
// {
//   name: "dillion",
//   age: 1000,
//   language: "javascript",
//   isStudent: true
// }
```

Comme vous pouvez le voir dans cet exemple, `name` et `age` sont ajoutés directement, en tant que clés statiques. Mais, `language` et `isStudent` ne sont pas ajoutés en tant que clés statiques. Ils sont ajoutés dynamiquement, en tant qu'expressions de variables : `[key1]` et `[key2]`. Les valeurs retournées par les expressions représentent alors les clés qui seront ajoutées à l'objet.

Ce n'est qu'un exemple montrant une expression de variable. Comme je l'ai dit, vous pouvez utiliser différentes formes d'expressions qui retournent une valeur.

Regardons un autre exemple d'expression.

### Comment définir des expressions conditionnelles comme noms de propriétés

Les expressions conditionnelles, créées avec l'[opérateur conditionnel](https://www.freecodecamp.org/news/the-ternary-operator-in-javascript/), vous permettent de définir des conditions. Une certaine valeur sera retournée si la condition est vraie, et une autre valeur sera retournée si elle est fausse.

Regardons un exemple utilisant une expression conditionnelle comme nom de propriété :

```js
const age = 10

const key1 = "ageIsMoreThan5"
const key2 = "ageIsMoreThan10"

const obj = {
  name: "dillion",
  [age > 10 ? key2 : key1]: true
}

console.log(obj)
// {
//   name: "dillion",
//   ageIsMoreThan5: true
// }
```

Ici, nous avons une variable `age` qui contient une valeur numérique de **10**. 

Dans l'objet `obj`, nous avons une expression conditionnelle : `age > 10 ? key2 : key1`. Cette expression indique que si la valeur de la variable `age` est supérieure à 10, `key2` est retourné, sinon `key1` est retourné. 

Parce que **10** (valeur de `age`) n'est pas supérieur à 10, `key2` est retourné. La valeur de la variable `key2` est `ageIsMoreThan5`.

Et si `age` est **20**, une clé de propriété différente est ajoutée à `obj` :

```js
const age = 20

const key1 = "ageIsMoreThan5"
const key2 = "ageIsMoreThan10"

const obj = {
  name: "dillion",
  [age > 10 ? key2 : key1]: true
}

console.log(obj)
// {
//   name: "dillion",
//   ageIsMoreThan10: true
// }
```

Comme vous pouvez le voir ici, l'expression conditionnelle est évaluée à `key2` car `age > 10` retourne `true`. La valeur de `key2` est "ageIsMoreThan10", donc c'est la propriété ajoutée à l'objet.

## Conclusion

Dans cet article, je vous ai montré comment la prise en charge des noms de propriétés calculés en JavaScript fonctionne pour ajouter des clés dynamiques lors de la déclaration d'objets.

Vous pouvez penser à n'importe quelle expression qui retourne une valeur. De telles expressions peuvent être utilisées entre crochets, pour servir de clé de propriété dans un objet.

Vous pouvez également utiliser cette fonctionnalité pour accéder/modifier une propriété existante ou ajouter une nouvelle propriété. Vous pouvez en apprendre plus sur cela dans mon article sur la [Notation par point et notation par crochets pour les propriétés d'objet](https://freecodecamp.org/news/dot-notation-vs-square-brackets-javascript/).

Si vous avez trouvé cet article utile, n'hésitez pas à le partager 🤟🏾