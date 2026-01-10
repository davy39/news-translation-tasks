---
title: Erreur de Référence Circulaire en JavaScript – Signification et Comment la
  Corriger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-07T21:52:14.000Z'
originalURL: https://freecodecamp.org/news/circular-reference-in-javascript-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/22.-circular-reference-error.png
tags:
- name: error
  slug: error
- name: JavaScript
  slug: javascript
seo_title: Erreur de Référence Circulaire en JavaScript – Signification et Comment
  la Corriger
seo_desc: "By Dillion Megida\nHave you ever encountered a \"circular reference\" error\
  \ when working with JSON? \nIn this tutorial, I'll explain what this error means\
  \ as well as how to fix it.\nThis error, in my experience, occurs when you try to\
  \ convert an object wi..."
---

Par Dillion Megida

Avez-vous déjà rencontré une erreur de "référence circulaire" en travaillant avec JSON ?

Dans ce tutoriel, je vais expliquer ce que signifie cette erreur ainsi que comment la corriger.

Cette erreur, selon mon expérience, se produit lorsque vous essayez de convertir un objet avec des références circulaires en JSON. Vous avez peut-être rencontré cette erreur en faisant cela ou autre chose.

Tout d'abord, comprenons ce qu'est une référence circulaire en JavaScript.

## Qu'est-ce qu'une Référence Circulaire en JS ?

Un objet en JavaScript peut avoir différents types de données pour les propriétés. Voici un exemple d'objet :

```js
const obj = {
  name: "Dillion",
  isDev: true,
  hobbies: ["singing", "writing"],
  age: 100,
}
```

Cet objet a des propriétés contenant des valeurs de type chaîne de caractères, booléen, tableau et nombre.

Dans les objets, vous pouvez également avoir un objet imbriqué. Voici ce que je veux dire :

```js
obj.languages = {
  first: "javascript",
  second: "java",
}

console.log(obj)
// {
//   name: "Dillion",
//   isDev: true,
//   hobbies: ["singing", "writing"],
//   age: 100,
//   languages: {
//     first: "javascript",
//     second: "java"
//   }
// }
```

Ici, nous ajoutons une propriété `languages`, qui contient une valeur d'objet avec les propriétés `first` et `second`.

Pour accéder aux propriétés de l'objet imbriqué, vous pouvez utiliser la notation par points (ou [notation par crochets](https://www.freecodecamp.org/news/dot-notation-vs-square-brackets-javascript/)) comme ceci :

```js
obj.languages.first
obj.languages.second
```

J'ai une [version vidéo de ce sujet](https://youtu.be/EaHC3QfU1NY) que vous pouvez également consulter.

Maintenant, que se passe-t-il si nous avons un objet imbriqué qui pointe vers l'objet original ? Regardez cet exemple :

```js
obj.itself = obj
```

Ici, nous ajoutons une propriété `itself`, et nous lui assignons une référence d'objet, qui est `obj`. Cela crée une **référence circulaire**. Je vais vous montrer pourquoi cela s'appelle une référence circulaire.

Essayons d'afficher `obj` dans la console :

```js
// {
//   name: "Dillion",
//   isDev: true,
//   hobbies: ["singing", "writing"],
//   age: 100,
//   languages: {
//     first: "javascript",
//     second: "java"
//   },
//   itself: [Circular *1]
// }
```

Dans la console, la valeur de la propriété `itself` affiche **[Circular \*1]**. Il s'agit d'une notation indiquant que la propriété pointe vers l'objet, et essayer d'afficher la valeur de cette propriété entraînera un objet imbriqué sans fin.

Cela signifie que la propriété `itself` ressemblera à ceci :

```js
{
  name: "Dillion",
  isDev: true,
  hobbies: ["singing", "writing"],
  age: 100,
  languages: {
    first: "javascript",
    second: "java"
  },
  itself: {
    name: "Dillion",
    isDev: true,
    hobbies: ["singing", "writing"],
    age: 100,
    languages: {
      first: "javascript",
      second: "java"
    },
    itself: {
      name: "Dillion",
      // ...
    }
  }
}
```

Voici une illustration graphique de cela :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-54.png)
*Illustration graphique d'une référence cyclique*

Comme vous pouvez le voir dans cet objet, la propriété `itself` contient toutes les propriétés de l'objet, y compris `itself`, qui contient à nouveau toutes les propriétés de l'objet, y compris `itself`, et cela continue sans fin.

Avec cette référence circulaire de la propriété à l'objet, nous pouvons accéder à la propriété `first` comme ceci :

```js
obj.itself.itself.itself.itself.itself.itself.first
```

Ces nombreux `itself` fonctionnent toujours grâce à la référence circulaire.

Nous pouvons également accéder à la propriété `name` dans `obj` comme ceci :

```js
obj.itself.itself.itself.itself.name
```

Puisque `itself` a une référence à `obj`, nous pouvons accéder à la propriété `name` à partir de n'importe quel `itself` imbriqué.

Maintenant, voyons comment ce schéma de référence circulaire s'applique à JSON.

## Le Problème de JSON avec les Références Circulaires

Regardons à nouveau notre objet initial :

```js
const obj = {
  name: "Dillion",
  isDev: true,
  hobbies: ["singing", "writing"],
  age: 100,
}
```

Lorsque vous convertissez cet objet en chaîne pour qu'il corresponde à la structure JSON, voici le résultat :

```js
const stringified = JSON.stringify(obj)

console.log(stringified)
// {
//   "name":"Dillion",
//   "isDev":true,
//   "hobbies":["singing","writing"],"age":100
// }
```

JSON stringify parcourt les propriétés de la première étant "name" à la dernière étant "hobbies".

Et si nous avions notre objet `languages` imbriqué converti en chaîne ?

```js
obj.languages = {
  first: "javascript",
  second: "java",
}

const stringified = JSON.stringify(obj)

console.log(stringified)
// {
//   "name":"Dillion",
//   "isDev":true,
//   "hobbies":["singing","writing"],"age":100,
//   "languages":{
//     "first":"javascript",
//     "second":"java"
//   }
// }
```

Comme vous le voyez ici, la méthode stringify parcourt les propriétés de la première étant "name" à la dernière étant "languages". Lorsqu'elle arrive à languages, elle parcourt les propriétés de l'objet qui sont `first` et `second`.

Maintenant, introduisons une référence circulaire et voyons ce qui se passe :

```js
obj.itself = obj

const stringified = JSON.stringify(obj)

console.log(stringified)
// TypeError: Converting circular structure to JSON
```

Maintenant, nous obtenons une erreur : **TypeError: Converting circular structure to JSON**.

Quel est le problème ici ?

En convertissant un objet avec une référence circulaire, cela entraîne un processus de conversion en chaîne infini.

Supposons que JSON stringify essaie de parcourir cet objet, voici ce qui se passe : la méthode stringify va de la première propriété dans `obj` qui est `name` à la dernière propriété `itself`. Lorsqu'elle arrive à `itself`, elle convertit les propriétés de cet objet. La valeur de l'objet `itself` est l'objet `obj`, donc stringify parcourt à nouveau de `name` à `itself`. En rencontrant `itself`, elle doit parcourir à nouveau.

Voici une illustration expliquant ce qui se passe :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-55.png)

Comme vous le voyez ici, cela entraîne une boucle infinie car `stringify` ne sait pas quand s'arrêter. Chaque fois qu'elle rencontre `itself`, elle doit parcourir cet objet qui contient `itself`. Elle continuera à convertir en chaîne pour toujours.

Cela est fondamentalement impossible. Donc, lorsque la méthode stringify rencontre une référence circulaire dans un objet, elle génère immédiatement une erreur. Il n'y a pas besoin de perdre son temps 😅

Alors, si vous rencontrez cette erreur lors de la création d'applications, comment la résoudre ?

## Comment Résoudre l'Erreur de Référence Circulaire

Il existe plusieurs façons de résoudre ce problème. Vous pouvez utiliser des bibliothèques ou implémenter une solution vous-même.

Une méthode majeure pour résoudre cela est d'utiliser la **sérialisation**. Ce processus implique de sérialiser l'objet pour supprimer certaines propriétés d'un objet avant de le convertir en JSON.

Dans ce processus, vous pouvez supprimer les propriétés qui ne vous intéressent pas, ou dans notre cas, les propriétés qui peuvent causer des erreurs.

Voici une solution simple :

```js
obj.itself = obj

function replacer(key, value) {
  if(key === 'itself') {
    return null
  }

  return value
}

const stringified = JSON.stringify(obj, replacer)

console.log(stringified)
// {
//   "name":"Dillion",
//   "isDev":true,
//   "hobbies":["singing","writing"],"age":100,
//   "languages":{
//     "first":"javascript",
//     "second":"java"
//   },
//   "itself":null
// }
```

Ce que nous avons fait ici, c'est utiliser l'[argument replacer de JSON.stringify](https://dillionmegida.com/p/second-argument-in-json-stringify/) pour modifier la propriété `itself`.

Dans la fonction replacer, nous vérifions la clé `itself`, et retournons la valeur `null` pour cette clé. De cette façon, `JSON.stringify` remplace la valeur de référence circulaire par `null` lors de la conversion en chaîne, évitant ainsi une conversion infinie.

## Conclusion

Si vous construisez des applications avec JavaScript, vous avez peut-être rencontré cette erreur de référence cyclique d'une manière ou d'une autre.

Dans cet article, j'ai expliqué ce qu'est cette erreur et pourquoi elle existe lors de la conversion d'un objet en JSON.

Si vous avez aimé cet article, veuillez le partager avec d'autres 👏🏾