---
title: "Hoisting en JavaScript avec let et const \x13 et comment cela diffère de var"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-18T23:33:20.000Z'
originalURL: https://freecodecamp.org/news/javascript-let-and-const-hoisting
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/5.-let-const-hoisting.png
tags:
- name: JavaScript
  slug: javascript
seo_title: "Hoisting en JavaScript avec let et const \x13 et comment cela diffère\
  \ de var"
seo_desc: "By Dillion Megida\nI used to think that hoisting only happened to variables\
  \ declared with var. But recently, I learned that it also happens to variables declared\
  \ with let and const. \nI'll explain what I mean in this article.\nI also have a\
  \ video versio..."
---

Par Dillion Megida

Je pensais autrefois que le hoisting ne se produisait qu'avec les variables déclarées avec `var`. Mais récemment, j'ai appris que cela se produit également avec les variables déclarées avec `let` et `const`. 

Je vais expliquer ce que je veux dire dans cet article.

J'ai également une [version vidéo de cet article](https://www.youtube.com/watch?v=VbHaL_J8Ex0) que vous pouvez consulter si vous êtes intéressé.

## Comment le Hoisting fonctionne avec `var` en JavaScript

Voici comment le hoisting fonctionne sur les variables déclarées avec `var`:

```js
console.log(number)
// undefined

var number = 10

console.log(number)
// 10
```

La variable `number` est remontée en haut de la portée globale. Cela permet d'accéder à la variable avant la ligne où elle est déclarée, sans erreur.

Mais ce que vous remarquerez ici, c'est que seule la déclaration de la variable (`var number`) est remontée  l'initialisation (`= 10`) ne l'est pas. Donc, lorsque vous essayez d'accéder à `number` avant qu'elle ne soit déclarée, vous obtenez **l'initialisation par défaut qui se produit avec var**, qui est `undefined`.

Ensuite, la ligne de déclaration et d'initialisation est exécutée, donc l'accès à `number` après cela retourne la valeur initialisée, **10**.

## Comment le Hoisting fonctionne avec let/const en JavaScript

Si vous essayez de faire la même chose que ci-dessus avec `let` ou `const`, voici ce qui se passe:

```js
console.log(number)

let number = 10
// ou const number = 10

console.log(number)
```

Vous obtenez une erreur qui dit: **ReferenceError: Cannot access 'number' before initialization**.

Ainsi, vous pouvez accéder à une variable déclarée avec var avant sa déclaration sans erreur, mais vous ne pouvez pas faire de même avec `let` ou `const`. 

C'est pourquoi j'avais toujours pensé que le hoisting ne se produisait qu'avec var, et non avec let ou const. 

Mais comme je l'ai dit, j'ai récemment appris que les variables déclarées avec `let` ou `const` sont également remontées. Laissez-moi expliquer.

Regardez cet exemple:

```js
console.log(number2)

let number = 10
```

Je journalise une variable appelée `number2` dans la console, et je déclare et initialise une variable appelée `number`.

L'exécution de ce code produit cette erreur: **ReferenceError: number2 is not defined**

Quelle est la différence entre l'erreur précédente et cette erreur? L'erreur précédente dit **ReferenceError: Cannot access 'number' before initialization** tandis que cette nouvelle erreur dit **ReferenceError: number2 is not defined**.

Voici la différence. La première dit "cannot access before initialization" tandis que la seconde dit "is not defined".

Ce que la seconde signifie, c'est que JavaScript n'a aucune idée de ce qu'est la variable `number2` parce qu'elle n'est pas définie  et en effet, nous ne l'avons pas définie. Nous avons seulement défini `number`.

Mais la première ne dit pas "is not defined", au lieu de cela, elle dit "cannot access before initialization". Voici le code à nouveau:

```js
console.log(number)
// ReferenceError: Cannot access 'number' before initialization

let number = 10

console.log(number)
```

Cela signifie que JavaScript "connaît" la variable `number`. Comment le sait-il? Parce que `number` est remontée en haut de la portée globale. 

Mais pourquoi une erreur se produit-elle? Eh bien, cela clarifie la différence entre le comportement de hoisting avec `var` et `let`/`const`.

Les variables déclarées avec `let` ou `const` sont **remontées SANS initialisation par défaut**. Donc, y accéder avant la ligne où elles sont déclarées lance **ReferenceError: Cannot access 'variable' before initialization**.

Mais les variables déclarées avec `var` sont **remontées AVEC une initialisation par défaut à undefined**. Donc, y accéder avant la ligne où elles sont déclarées retourne `undefined`.

## Zone morte temporelle

Il y a un nom pour la période pendant l'exécution où les variables `let`/`const` sont remontées mais pas accessibles: on l'appelle la **Zone Morte Temporelle**.

Encore une fois, le code ci-dessus:

```js
console.log(number)

let number = 10

console.log(number)
```

La variable `number` est dans une zone morte temporelle où JavaScript connaît son existence (parce que sa déclaration est remontée) mais elle n'est pas accessible (car elle n'a pas d'initialisation).

## Conclusion

Si vous étiez comme moi, et que vous pensiez que le hoisting ne s'appliquait qu'avec `var` et non avec `let`/`const`, j'espère que cet article clarifie cette fausse supposition.

Comme je l'ai expliqué dans cet article, les variables `let` et `const` sont remontées, mais elles sont remontées sans initialisation par défaut. Cela les rend inaccessibles (car ces variables sont dans une zone morte temporelle).

Les variables déclarées avec `var`, en revanche, sont remontées avec une initialisation par défaut à `undefined`.

J'espère que vous avez appris quelque chose de cet article :)