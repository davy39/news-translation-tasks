---
title: Différence entre les opérateurs logiques AND et OR
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-27T08:15:17.000Z'
originalURL: https://freecodecamp.org/news/difference-between-logical-operators-and-and-or
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/31-and-or.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: Différence entre les opérateurs logiques AND et OR
seo_desc: 'By Dillion Megida

  AND && and OR || are logical operators in JavaScript which you can use for performing
  different logical expressions. In this article, I''ll explain the difference between
  them.

  The goal of this article is for you to understand how th...'
---

Par Dillion Megida

AND `&&` et OR `||` sont des opérateurs logiques en JavaScript que vous pouvez utiliser pour effectuer différentes expressions logiques. Dans cet article, je vais expliquer la différence entre eux.

Le but de cet article est que vous compreniez comment ces opérateurs fonctionnent et en quoi ils sont différents.

Pour comprendre ces opérateurs, il est important de comprendre le concept des valeurs **truthy** et **falsy** en JavaScript.

## Valeurs Truthy et Falsy

En JavaScript, de nombreuses valeurs peuvent être représentées par leurs équivalents booléens. Une valeur représentée par `false` est une valeur falsy et une valeur représentée par `true` est une valeur truthy. Voici quelques exemples :

```js
0
false
undefined
null
"" // chaîne vide
```

Les valeurs `0`, `false`, `undefined`, `null` et la chaîne vide `""` sont des valeurs falsy car leurs représentations booléennes sont `false`.

En ce qui concerne les valeurs truthy, toute valeur qui n'est pas `falsy` est `truthy`. Cela signifie que les valeurs truthy incluent `true`, `1`, `[3, 4]`, `{}`, `"hello"`.

Maintenant que nous avons clarifié cela, voyons comment cela se rapporte aux opérateurs `AND` et `OR`.

J'ai une [version vidéo de ce sujet](https://youtu.be/HZ-X6JVqfhQ) si cela vous intéresse.

## L'opérateur `AND`

L'opérateur logique `AND` est utilisé entre deux opérandes dans une expression comme ceci :

```js
operand1 && operand2
```

L'opérateur retourne le deuxième opérande **si le premier opérande est une valeur truthy**. Si le premier opérande est une valeur falsy, l'opérateur retournera le premier opérande à la place. Comme nous l'avons vu, une valeur truthy est une valeur qui évalue à `true`.

Voyons un exemple :

```js
const exp1 = 5
const exp2 = "Dillion"

const result = exp1 && exp2

console.log(result)
// "Dillion"
```

Dans cet exemple, nous avons `exp1` avec une valeur de **5** et `exp2` avec une valeur de **"Dillion"**. Ensuite, nous avons la variable `result` qui contient la valeur retournée par l'utilisation de l'opérateur `&&` entre `exp1` et `exp2`.

Ce qui se passe ici, c'est que l'opérateur, de gauche à droite, vérifie si `exp1` est une **valeur truthy**. **5** est une valeur truthy, donc l'opérateur retourne la valeur de droite. C'est pourquoi `result` contient la valeur de **"Dillion"**.

Voyons un autre exemple où nous utilisons l'opérateur `AND` plusieurs fois :

```js
function returnFalsy() {
  return ""
}

const exp1 = [1, 2]
const exp2 = returnFalsy()
const exp3 = { name: "Dillion" }

const result = exp1 && exp2 && exp3

console.log(result)
// ""
```

Comme nous pouvons le voir dans cet exemple, nous avons :

- `exp1` avec un tableau
- `exp2` avec la valeur retournée par l'appel de `returnFalsy()` (qui est une chaîne vide--une **valeur falsy**)
- `exp3` avec un objet

Enfin, nous avons la variable `result` qui contient la valeur retournée par l'utilisation de l'opérateur `&&` entre `exp1` et `exp2` et entre `exp2` et `exp3`.

Ce que nous avons ici, c'est `exp1 && exp2` comme opérande 1 et opérande 2. Ensuite, le résultat de cette expression deviendra l'opérande 1 pour l'expression suivante : `result && exp3`. `exp3` ici est le deuxième opérande dans la deuxième expression.

Ce qui se passe ici, c'est que l'opérateur, de gauche à droite, vérifie si `exp1` est une **valeur truthy**. Dans ce cas, nous avons un tableau, qui est une valeur truthy, ce qui signifie que le deuxième opérande `exp2` sera retourné. `exp2` devient le premier opérande, et `exp3` devient le deuxième opérande pour la deuxième expression.

Le deuxième opérateur `&&` vérifie si `exp2` est une valeur truthy. Dans ce cas, la chaîne vide **""** est une valeur falsy, donc l'opérateur retourne `exp2`. Il ne se donne pas la peine de vérifier `exp3` car le fait que `exp2` soit falsy signifie que l'opérateur arrêtera de vérifier de gauche à droite.

Ce qui se passe ici est le **short-circuiting** que vous pouvez apprendre davantage dans mon [article sur les opérateurs de court-circuit](https://dillionmegida.com/p/short-circuit-in-programming-simplified/)

## L'opérateur `OR`

L'opérateur logique `OR` est utilisé entre deux opérandes dans une expression comme ceci :

```js
operand1 || operand2
```

L'opérateur retourne le premier opérande **si le premier opérande est une valeur truthy**. Si le premier opérande est une valeur falsy, l'opérateur retournera le deuxième opérande à la place.

Voyons un exemple :

```js
const exp1 = 5
const exp2 = "Dillion"

const result = exp1 || exp2

console.log(result)
// 5
```

Dans cet exemple, nous avons `exp1` avec une valeur de **5** et `exp2` avec une valeur de **"Dillion"**. Ensuite, nous avons la variable `result` qui contient la valeur retournée par l'utilisation de l'opérateur `||` entre `exp1` et `exp2`.

Ce qui se passe ici, c'est que l'opérateur, de gauche à droite, vérifie si `exp1` est une **valeur truthy**. **5** est une valeur truthy, donc l'opérateur la retourne. C'est pourquoi `result` contient la valeur de **5**.

L'opérateur `OR` ne se donne pas la peine de vérifier `exp2` car il a déjà trouvé une valeur truthy. C'est l'inverse de l'opérateur `AND`. `AND` continue de gauche à droite tant que c'est `true`. Mais `OR` s'arrête (encore une fois, [short-circuiting](https://dillionmegida.com/p/short-circuit-in-programming-simplified/)) dès qu'il voit un `true`--il ne continue de gauche à droite que tant que c'est `false`.

Voyons un autre exemple où nous utilisons l'opérateur `OR` plusieurs fois :

```js
function returnFalsy() {
  return ""
}

const exp1 = null
const exp2 = returnFalsy()
const exp3 = { name: "Dillion" }

const result = exp1 || exp2 || exp3

console.log(result)
// { name: "Dillion" }
```

Comme nous pouvons le voir dans cet exemple, nous avons :

- `exp1` avec une valeur de `null` (une **valeur falsy**)
- `exp2` avec la valeur retournée par l'appel de `returnFalsy()` (qui est une chaîne vide--une **valeur falsy**)
- `exp3` avec un objet

Enfin, nous avons la variable `result` qui contient la valeur retournée par l'utilisation de l'opérateur `||` entre `exp1` et `exp2` et entre `exp2` et `exp3`.

Ce que nous avons ici, c'est `exp1 || exp2` comme opérande 1 et opérande 2. Ensuite, le résultat de cette expression deviendra l'opérande 1 pour l'expression suivante : `result || exp3`. `exp3` ici est le deuxième opérande dans la deuxième expression.

Ce qui se passe ici, c'est que l'opérateur, de gauche à droite, vérifie si `exp1` est une **valeur truthy**. Dans ce cas, nous avons `null`, qui est une valeur falsy, ce qui signifie que le deuxième opérande `exp2` sera retourné. `exp2` devient le premier opérande, et `exp3` devient le deuxième opérande pour la deuxième expression.

Le deuxième opérateur `||` vérifie si `exp2` est une valeur truthy. Dans ce cas, la chaîne vide **""** est une valeur falsy, donc l'opérateur retourne `exp3`. Comme vous le remarquez ici, l'opérateur `OR` continue tant qu'il rencontre des valeurs fausses. Il ne s'arrête que lorsqu'il trouve une valeur truthy ou lorsqu'il arrive à la fin des expressions.

## Utilisation de `AND` et `OR` dans les instructions `if`

Les instructions `if` vous permettent de créer des instructions conditionnelles où vous déterminez ce qui sera exécuté en fonction d'une condition.

<!-- Vous pouvez en apprendre davantage sur [les instructions if dans cet article](). -->

Voyons un exemple où nous utilisons `AND` dans une instruction `if` :

```js
const isLoggedIn = true
const cart = []

if (isLoggedIn && cart.length) {
  console.log("Cart not empty")
} else {
  console.log("Cart is empty")
}
```

Pouvez-vous deviner le résultat de l'exécution de ce code ? Le résultat est :

```js
// Cart is empty
```

Voici pourquoi. La condition pour l'instruction `if` est `isLoggedIn && cart.length`. L'opérande de gauche est `isLoggedIn` qui évalue à `true`. Rappelez-vous que l'opérateur `&&` retourne l'opérande de droite si l'opérande de gauche est `true`. Il ne retourne l'opérande de gauche que si l'opérande de gauche est `false`. Dans ce cas, l'opérateur retournerait `cart.length`, qui évalue à 0 puisque le tableau `cart` est vide.

Ce qui signifie que le bloc `if` est exécuté comme `if(0)`.

L'instruction `if` forcerait `0` à une valeur booléenne. Comme nous l'avons vu précédemment, `0` est une **valeur falsy**. Donc l'instruction `if`, voyant que l'expression de condition `0` est `false`, exécuterait le bloc `else` : `console.log("Cart is empty")`. Vous pouvez en apprendre davantage sur [la coercition de type dans cet article](https://www.freecodecamp.org/news/coercion-and-type-conversion-in-javascript/).

Supposons que `OR` ait été utilisé à la place :

```js
const isLoggedIn = true
const cart = []

if (isLoggedIn || cart.length) {
  console.log("Cart not empty")
} else {
  console.log("Cart is empty")
}
```

Pouvez-vous deviner le résultat de cela ? Le voici :

```js
// Cart not empty
```

Voici pourquoi. La condition pour l'instruction `if` ici est `isLoggedIn || cart.length`. L'opérande de gauche est `isLoggedIn` qui évalue à `true`. Rappelez-vous que l'opérateur `||` retourne l'opérande de gauche s'il est `true`. Il ne retourne l'opérande de droite que si l'opérande de gauche est `false`. Dans ce cas, l'opérateur retournerait `isLoggedIn` qui évalue à `true`.

Ce qui signifie que le bloc `if` est exécuté comme `if(true)`.

Dans ce cas, la coercition ne se produit pas car `true` est déjà une valeur booléenne. Donc l'instruction `if`, voyant que l'expression de condition `true` est `true`, exécuterait le bloc `if` : `console.log("Cart not empty")`.

## Conclusion

Voici un résumé de la différence entre `AND` et `OR` :

- `AND` retourne l'expression de droite si l'expression de gauche est `true`
- `AND` retourne l'expression de gauche si l'expression de gauche est `false`
- `OR` retourne l'expression de droite si l'expression de gauche est `false`
- `OR` retourne l'expression de gauche si l'expression de gauche est `true`

Vous remarquez que `OR` est l'inverse de `AND` ? Alors que `AND` continue vers la droite tant que la gauche est `true`, `OR` continue vers la droite tant que la gauche est `false`.

Si vous avez aimé cet article, veuillez le partager avec d'autres.