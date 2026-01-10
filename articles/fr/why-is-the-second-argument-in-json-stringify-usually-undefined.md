---
title: Pourquoi le deuxième argument de JSON.stringify() est-il généralement null
  ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-29T17:43:00.000Z'
originalURL: https://freecodecamp.org/news/why-is-the-second-argument-in-json-stringify-usually-undefined
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/24.-json-stringify-null.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Pourquoi le deuxième argument de JSON.stringify() est-il généralement null
  ?
seo_desc: "By Dillion Megida\nUsually, when developers use the JSON.stringify() method,\
  \ the second argument is usually skipped, or with a value null. But this argument\
  \ has its relevance.\nHere's a common example usage of JSON.stringify():\nconst\
  \ obj = {\n  name: \"D..."
---

Par Dillion Megida

Généralement, lorsque les développeurs utilisent la méthode `JSON.stringify()`, le deuxième argument est généralement omis ou possède la valeur `null`. Cependant, cet argument a son importance.

Voici un exemple courant d'utilisation de `JSON.stringify()` :

```js
const obj = {
  name: "Dillion",
  language: "JavaScript",
  age: 100,
  isEngineer: true
}

const stringifiedObj = JSON.stringify(obj, null, 2)

console.log(stringifiedObj)
// {
//   "name": "Dillion",
//   "language": "JavaScript",
//   "age": 100,
//   "isEngineer": true
// }
```

Comme vous le voyez ici, nous avons passé trois arguments à `stringify` : l'objet, `null` et 2.

Dans des cas comme celui-ci, le deuxième argument n'est pas nécessaire, c'est pourquoi nous avons `null`. Mais il existe des cas où le deuxième argument peut être utile. Je vais vous montrer l'utilité du deuxième argument dans cet article.

J'ai une [vidéo d'une minute sur ce sujet](https://youtu.be/y3P17LC8rJQ) que vous pouvez également consulter.

## La méthode JSON.stringify

La méthode `stringify` de l'objet `JSON` est utilisée pour, comme son nom l'indique, transformer une valeur en chaîne de caractères (stringify) en JavaScript. Généralement, cette méthode est utilisée pour convertir un objet en une chaîne JSON, qui est un format recommandé pour des éléments tels que les réponses d'API, les fichiers de configuration, etc.

Voici la syntaxe de la méthode :

```js
stringify(value, replacer, space)
```

La `value` est l'objet que vous voulez transformer. Le `replacer` spécifie les valeurs des propriétés à remplacer lors de la transformation. Et `space` spécifie les espaces blancs pour le résultat final (ce qui aide à la lisibilité).

Le `replacer` est généralement `null` parce qu'il n'y a rien à remplacer, mais dans les cas où vous souhaitez remplacer certaines propriétés lors de la transformation en chaîne, c'est l'endroit idéal pour le faire.

## L'argument replacer de JSON.stringify

L'argument `replacer` peut être soit une fonction appelée sur chaque propriété de l'objet, soit un tableau contenant les clés qui doivent exister dans le résultat final.

### Fonction de rappel (callback) replacer

En utilisant une fonction de rappel comme replacer dans `JSON.stringify`, vous pouvez parcourir les propriétés et les modifier pour le résultat final. Voici un exemple :

```js
function replacer(key, value) {
  if (key === "age") {
    return 500
  }

  if (key === "name") {
    return `Mr. ${value}`
  }

  if (key === "isEngineer") {
    return undefined
  }

  return value
}
```

Ici, nous avons une fonction `replacer` qui prend chaque propriété (la clé et la valeur) comme arguments. Cette fonction vérifie si la clé est "age", auquel cas elle renvoie **500** comme valeur. Elle vérifie également si la clé est "name", auquel cas elle renvoie "Mr." concaténé avec la valeur de `name`. Enfin, elle vérifie si la clé est "isEngineer" et, si c'est le cas, elle renvoie `undefined`.

Si les conditions précédentes ne sont pas remplies, elle renvoie la `value`.

Appliquons cela à la méthode `stringify` :

```js
const obj = {
  name: "Dillion",
  language: "JavaScript",
  age: 100,
  isEngineer: true,
}

const stringifiedObj = JSON.stringify(
  obj,
  replacer,
  2
)

console.log(stringifiedObj)

// {
//   "name": "Mr. Dillion",
//   "language": "JavaScript",
//   "age": 500
// }
```

En appliquant la fonction `replacer` comme second argument, que remarquez-vous dans le résultat final ?

Pour chaque propriété, la clé (`key`) et la valeur (`value`) sont passées à la fonction replacer. La valeur renvoyée par cette fonction devient la valeur de la propriété. Mais la clé ne change pas.

Pour `name`, nous renvoyons "Mr." concaténé avec la valeur existante qui était "Dillion", nous obtenons donc "Mr. Dillion".

Pour `language`, nous ne faisons rien. Nous renvoyons simplement la `value`.

Pour `age`, nous avons renvoyé 500 depuis la fonction replacer, donc 500 remplace la valeur précédente qui était 100.

Pour `isEngineer`, nous avons renvoyé `undefined` depuis la fonction replacer. `undefined` n'est pas une valeur valide dans les chaînes JSON, cette propriété est donc exclue du résultat final.

Comme vous l'avez vu ici, nous avons utilisé l'argument replacer (dans ce cas, une fonction) pour "remplacer" (modifier) les propriétés de l'objet avant de le transformer en chaîne.

### Tableau replacer

Un replacer peut être soit une fonction, soit un tableau. En utilisant un tableau comme replacer, vous ne pouvez pas modifier les propriétés, mais vous pouvez spécifier les propriétés qui doivent figurer dans le résultat final. Voici un exemple :

```js
const replacer = ["name", "isEngineer"]
```

Ici, nous avons un tableau de deux chaînes : "name" et "isEngineer". Utilisons-le maintenant avec `stringify` :

```js
const obj = {
  name: "Dillion",
  language: "JavaScript",
  age: 100,
  isEngineer: true,
}

const stringifiedObj = JSON.stringify(
  obj,
  replacer,
  2
)

console.log(stringifiedObj)

// {
//   "name": "Dillion",
//   "isEngineer": true
// }
```

Comme vous pouvez le voir ici, les seules propriétés de la chaîne JSON finale sont `name` et `isEngineer`, car ce sont les clés que nous avons spécifiées dans le tableau replacer.

## Alors pourquoi le deuxième argument de JSON.stringify() est-il généralement null ?

Vous utilisez `null` parce que vous ne voulez rien remplacer. Lorsque vous passez `null` comme argument replacer, cela signifie "pas de remplacements", ainsi chaque propriété de l'objet est transformée en chaîne.

Mais peu de développeurs connaissent cette particularité. En tant que développeur moi-même, j'ai appris à toujours utiliser `null` lors de la transformation d'objets en JSON. Je n'avais jamais compris pourquoi.

J'espère donc que cet article vous en aura appris davantage sur `JSON.stringify()`.

Comme prochaine étape, vous pouvez consulter mon article sur la [Référence circulaire](https://www.freecodecamp.org/news/circular-reference-in-javascript-explained/). Dans cet article, je montre comment la méthode `stringify` peut être utilisée pour résoudre les erreurs de référence circulaire.