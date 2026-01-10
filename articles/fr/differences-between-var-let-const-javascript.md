---
title: "var, let et const en JavaScript \x13 les diff\x1Erences entre ces mots-cl\x1E\
  s expliqu\x1Ees"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-11T22:48:17.000Z'
originalURL: https://freecodecamp.org/news/differences-between-var-let-const-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/15.-var-let-const.png
tags:
- name: JavaScript
  slug: javascript
- name: variables
  slug: variables
seo_title: "var, let et const en JavaScript \x13 les diff\x1Erences entre ces mots-cl\x1E\
  s expliqu\x1Ees"
seo_desc: 'By Dillion Megida

  In JavaScript, you can declare variables with the var, let, and const keywords.
  But what are the differences between them? That''s what I''ll explain in this tutorial.

  I have a video version of this topic you can check out as well. 😇...'
---

Par Dillion Megida

En JavaScript, vous pouvez dclarer des variables avec les mots-cls `var`, `let` et `const`. Mais quelles sont les diffrences entre eux ? C'est ce que je vais expliquer dans ce tutoriel.

J'ai une [version vido de ce sujet](https://youtu.be/Gd_JG3e1g4A) que vous pouvez galement consulter. 607

Si vous commencez  tout juste  utiliser JavaScript, voici quelques points que vous pourriez entendre  propos de ces mots-cls :

- `var` et `let` crent des variables qui peuvent tre rassignes  une autre valeur.
- `const` cre des variables "constantes" qui ne peuvent pas tre rassignes  une autre valeur.
- les dveloppeurs ne devraient plus utiliser `var`. Ils devraient utiliser `let` ou `const`  la place.
- si vous n'allez pas changer la valeur d'une variable, il est bon de pratiquer l'utilisation de `const`.

Les deux premiers points sont probablement assez explicites. Mais qu'en est-il de la raison pour laquelle nous ne devrions pas utiliser var, ou quand utiliser let vs const ? En parcourant ce tutoriel, esprons que tout cela aura du sens pour vous.

## `var` vs `let` vs `const`  Quelles sont les diffrences ?

Pour analyser les diffrences entre ces mots-cls, j'utiliserai trois facteurs :

- Porte des variables
- Redclaration et rassignment
- Hoisting

J'ecris galement des tutoriels spars sur la porte des variables, le hoisting des variables, et la redclaration et le rassignment des variables  vous pouvez donc en apprendre davantage  leur sujet galement. Ils seront bientt disponibles. :)

Commenons par examiner comment ces facteurs s'appliquent aux variables dclares avec `var`.

## Comment dclarer des variables avec `var` en JavaScript

### La porte des variables dclares avec `var`

Les variables dclares avec `var` peuvent avoir une porte **globale** ou **locale**. La porte globale est pour les variables dclares en dehors des fonctions, tandis que la porte locale est pour les variables dclares  l'intieur des fonctions.

Voyons quelques exemples, en commenant par la porte globale :

```js
var number = 50

function print() {
  var square = number * number
  console.log(square)
}

console.log(number) // 50

print() // 2500
```

La variable `number` a une porte globale  elle est dclare en dehors des fonctions dans l'espace global  donc vous pouvez y accder partout ( l'intieur et  l'extieur des fonctions).

Voyons un exemple de porte locale :

```js
function print() {
  var number = 50
  var square = number * number
  console.log(square)
}

print() // 2500

console.log(number)
// ReferenceError: number is not defined
```

Ici, nous avons dclar la variable `number` dans la fonction `print`, donc elle a une porte locale. Cela signifie que la variable ne peut tre accessible qu' l'intieur de cette fonction. Toute tentative d'accder  la variable en dehors de la fonction o elle a  t dclare entranera une erreur de rfrence **variable is not defined**.

### Comment redclarer et rassigner des variables dclares avec `var`

Les variables dclares avec `var` peuvent tre redclares et rassignes. Je vais expliquer ce que je veux dire avec des exemples.

Voici comment dclarer une variable avec `var` :

```js
var number = 50
```

Vous avez le mot-cl `var`, le nom de la variable `number`, et une valeur initiale **50**. Si une valeur initiale n'est pas fournie, la valeur par dfaut sera **undefined** :

```js
var number

console.log(number)
// undefined
```

Le mot-cl `var` permet la redclaration. Voici un exemple :

```js
var number = 50
console.log(number) // 50

var number = 100
console.log(number) // 100
```

Comme vous pouvez le voir, nous avons redclar la variable `number` en utilisant le mot-cl `var` et une valeur initiale de **100**.

Le mot-cl `var` permet galement le rassignment. Dans le code `var number = 50`, nous avons assign la valeur **50**  `number`. Nous pouvons rassigner une autre valeur n'importe o dans le code puisque elle a  t dclare avec `var`. Voici ce que je veux dire :

```js
var number = 50
console.log(number) // 50

number = 100
console.log(number) // 100

number = 200
console.log(number) // 200
```

Ici, nous ne redclarons pas  plutt, nous rassignons. Aprs avoir dclar la premire fois avec une valeur initiale de **50**, nous rassignons une nouvelle valeur de **100** et plus tard avec une nouvelle valeur de **200**.

### Comment hoister des variables dclares avec `var`

Les variables dclares avec `var` sont hoistes en haut de leur porte globale ou locale, ce qui les rend accessibles avant la ligne o elles sont dclares. Voici un exemple :

```js
console.log(number) // undefined

var number = 50

console.log(number) // 50
```

La variable `number` ici a une porte globale. Puisqu'elle est dclare avec `var`, la variable est hoiste. Cela signifie que nous pouvons accder  la variable avant la ligne o elle est dclare sans erreurs. 

Mais la variable est hoiste avec une valeur par dfaut de **undefined**. Donc c'est la valeur retourne par la variable (jusqu' la ligne o la variable est dclare avec une valeur initiale soit ex cute).

Voyons un exemple de porte locale :

```js
function print() {
  var square1 = number * number
  console.log(square1)

  var number = 50

  var square2 = number * number
  console.log(square2)
}

print()
// NaN
// 2500
```

Dans la fonction `print`, `number` a une porte locale. Grce au hoisting, nous pouvons accder  la variable `number` avant la ligne de dclaration. 

Comme nous le voyons dans `square1`, nous assignons **number \* number**. Puisque `number` est hoist avec une valeur par dfaut de **undefined**, `square1` sera **undefined \* undefined** ce qui donne **NaN**.

Aprs l'ex cution de la ligne de dclaration avec une valeur initiale, `number` aura une valeur de **50**. Donc dans `square2`, **number \* number** sera **50 \* 50** ce qui donne **2500**.

Il y a quelques problmes avec `var`, que nous discuterons  la fin. Sachez simplement qu'il est gnralement dconseill de l'utiliser dans vos projets JavaScript modernes. 

## Comment dclarer des variables avec `let` en JavaScript

### La porte des variables dclares avec `let`

Les variables dclares avec `let` peuvent avoir une porte **globale**, **locale** ou **de bloc**. La porte de bloc est pour les variables dclares dans un bloc. Un bloc en JavaScript implique des accolades ouvrantes et fermantes :

```js
{
  // un bloc
}
```

Vous pouvez trouver des blocs dans `if`, `loop`, `switch`, et quelques autres instructions. Toute variable dclare dans de tels blocs avec le mot-cl `let` aura une porte de bloc. galement, vous ne pouvez pas accder  ces variables en dehors du bloc. Voici un exemple montrant une porte globale, locale et de bloc :

```js
let number = 50

function print() {
  let square = number * number

  if (number < 60) {
    var largerNumber = 80
    let anotherLargerNumber = 100

    console.log(square)
  }

  console.log(largerNumber)
  console.log(anotherLargerNumber)
}

print()
// 2500
// 80
// ReferenceError: anotherLargerNumber is not defined
```

Dans cet exemple, nous avons une variable de porte globale `number` et une variable de porte locale `square`. Il y a galement une variable de porte de bloc `anotherLargerNumber` parce qu'elle est dclare avec `let` dans un bloc. 

`largerNumber`, en revanche  bien que dclar dans un bloc  n'a pas de porte de bloc parce qu'elle est dclare avec `var`. Donc `largerNumber` a une porte locale puisqu'elle est dclare dans la fonction `print`.

Nous pouvons accder  `number` partout. Nous pouvons seulement accder  `square` et `largerNumber` dans la fonction parce qu'elles ont une porte locale. Mais accder  `anotherLargerNumber` en dehors du bloc lance une erreur **anotherLargerNumber is not defined**.

### Comment redclarer et rassigner des variables dclares avec `let`

Tout comme `var`, les variables dclares avec `let` peuvent tre rassignes  d'autres valeurs, mais elles ne peuvent pas tre redclares. Voyons un exemple de rassignment :

```js
let number = 50
console.log(number) // 50

number = 100
console.log(number) // 100
```

Ici, nous avons rassign une autre valeur **100** aprs la dclaration initiale de **50**.

Mais redclarer une variable avec `let` lancera une erreur :

```js
let number = 50

let number = 100
// SyntaxError: Identifier 'number' has already been declared
```

Vous voyez que nous obtenons une erreur de syntaxe : **Identifier 'number' has already been declared**.

### Comment hoister des variables dclares avec `let`

Les variables dclares avec `let` sont hoistes en haut de leur porte globale, locale ou de bloc, mais leur hoisting est un peu diffrent de celui avec `var`.

Les variables `var` sont hoistes avec une valeur par dfaut de **undefined**, ce qui les rend accessibles avant leur ligne de dclaration (comme nous l'avons vu ci-dessus).

Mais, les variables `let` sont hoistes sans initialisation par dfaut. Donc lorsque vous essayez d'accder  de telles variables, au lieu d'obtenir **undefined**, ou une erreur **variable is not defined**, vous obtenez **cannot access variable before initialization**. Voyons un exemple :

```js
console.log(number)
// ReferenceError: Cannot access 'number' before initialization

let number = 50
```

Ici, nous avons une variable globale, `number` dclare avec `let`. En essayant d'accder  cette variable avant la ligne de dclaration, nous obtenons **ReferenceError: Cannot access 'number' before initialization**.

Voici un autre exemple avec une variable de porte locale :

```js
function print() {
  let square = number * number

  let number = 50
}

print()
// ReferenceError: Cannot access 'number' before initialization
```

Ici, nous avons une variable de porte locale, `number`, dclare avec `let`. En y accdant avant la ligne de dclaration  nouveau, nous obtenons l'erreur de rfrence **cannot access 'number' before initialization**

## Comment dclarer des variables avec `const` en JavaScript

### La porte des variables dclares avec `const`

Les variables dclares avec `const` sont similaires  `let` en ce qui concerne la **porte**. De telles variables peuvent avoir une porte **globale**, **locale** ou **de bloc**.

Voici un exemple :

```js
const number = 50

function print() {
  const square = number * number

  if (number < 60) {
    var largerNumber = 80
    const anotherLargerNumber = 100

    console.log(square)
  }

  console.log(largerNumber)
  console.log(anotherLargerNumber)
}

print()
// 2500
// 80
// ReferenceError: anotherLargerNumber is not defined
```

Cet exemple est tir de notre exemple prcdent, mais j'ai remplac `let` par `const`. Comme vous pouvez le voir ici, la variable `number` a une porte globale, `square` a une porte locale (dclare dans la fonction `print`), et `anotherLargeNumber` a une porte de bloc (dclare avec `const`).

Il y a galement `largeNumber`, dclare dans un bloc. Mais parce qu'elle est avec `var`, la variable n'a qu'une porte locale. Par consquent, elle peut tre accessible en dehors du bloc.

Parce que `anotherLargeNumber` a une porte de bloc, y accder en dehors du bloc lance une erreur **anotherLargerNumber is not defined**.

### Comment redclarer et rassigner des variables dclares avec `const`

 cet  gard, `const` est diffrent de `var` et `let`. `const` est utilis pour dclarer des variables **constantes**  c'est--dire des variables avec des valeurs qui ne peuvent pas tre changes. Donc de telles variables ne peuvent pas tre redclares, et elles ne peuvent pas non plus tre rassignes  d'autres valeurs. Tenter de le faire lancera une erreur.

Voyons un exemple avec la redclaration :

```js
const number = 50

const number = 100

// SyntaxError: Identifier 'number' has already been declared
```

Ici, vous pouvez voir l'erreur de syntaxe **Identifier has already been declared**.

Maintenant, voyons un exemple avec le rassignment :

```js
const number = 50

number = 100

// TypeError: Assignment to constant variable
```

Ici, vous pouvez voir l'erreur de type **Assignment to constant variable**.

### Comment hoister des variables dclares avec `const`

Les variables dclares avec `const`, tout comme `let`, sont hoistes en haut de leur porte globale, locale ou de bloc  mais sans initialisation par dfaut.

Les variables `var`, comme vous l'avez vu pr cdemment, sont hoistes avec une valeur par dfaut de **undefined** donc elles peuvent tre accessibles avant la dclaration sans erreurs. Accder  une variable dclare avec `const` avant la ligne de dclaration lancera une erreur **cannot access variable before initialization**.

Voyons un exemple :

```js
console.log(number)
// ReferenceError: Cannot access 'number' before initialization

const number = 50
```

Ici, `number` est une variable de porte globale dclare avec `const`. En essayant d'accder  cette variable avant la ligne de dclaration, nous obtenons **ReferenceError: Cannot access 'number' before initialization**. La mme chose se produira si c' tait une variable de porte locale.

Voici un article pour en apprendre davantage sur [Hoisting in JavaScript with let and const  and How it Differs from var](https://www.freecodecamp.org/news/javascript-let-and-const-hoisting/).

## Conclusion

Voici un tableau r sum montrant les diffrences entre ces mots-cls :

| Mot-cl | Porte               | Redclaration et Rassignment | Hoisting                   |
| ------- | -------------------- | ---------------------------- | -------------------------- |
| `var`   | Globale, Locale      | oui et oui                   | oui, avec valeur par dfaut    |
| `let`   | Globale, Locale, Bloc | non et oui                   | oui, sans valeur par dfaut |
| `const` | Globale, Locale, Bloc | non et non                   | oui, sans valeur par dfaut |

Ces facteurs que j'ai expliqus jouent un role dans la dtermination de la faon dont vous dclarez des variables en JavaScript. 

Si vous ne voulez jamais qu'une variable change, `const` est le mot-cl  utiliser.

Si vous voulez rassigner des valeurs :

- et vous voulez le comportement de hoisting, `var` est le mot-cl  utiliser
- si vous ne le voulez pas, `let` est le mot-cl pour vous

Le comportement de hoisting peut causer des bugs inattendus dans votre application. C'est pourquoi les dveloppeurs sont gnralement conseills d'viter `var` et de s'en tenir  `let` et `const`.

J'espre que vous avez appris quelque chose de cet article.