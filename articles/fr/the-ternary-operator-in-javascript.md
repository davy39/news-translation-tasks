---
title: Opérateur ternaire JavaScript – Syntaxe et cas d'utilisation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-06T23:30:48.000Z'
originalURL: https://freecodecamp.org/news/the-ternary-operator-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/13.-ternary-operator.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Opérateur ternaire JavaScript – Syntaxe et cas d'utilisation
seo_desc: 'By Dillion Megida

  There are many operators in JavaScript, one of which is the ternary operator. In
  this article, I''ll explain what this operator is, and how it can be useful when
  building applications.

  I have a video version of this topic you can che...'
---

Par Dillion Megida

Il existe de nombreux opérateurs en JavaScript, dont l'opérateur ternaire. Dans cet article, je vais expliquer ce qu'est cet opérateur et comment il peut être utile lors de la création d'applications.

J'ai également une [version vidéo de ce sujet](https://youtu.be/MmwtZ0AwN9A) que vous pouvez consulter pour compléter votre apprentissage.

## Qu'est-ce que l'opérateur ternaire ?

L'opérateur ternaire est un opérateur conditionnel qui évalue l'une des deux expressions – une expression vraie et une expression fausse – en fonction d'une expression conditionnelle que vous fournissez.

Voici la syntaxe :

```js
condition ? trueExpression : falseExpression
```

Vous avez la **condition** qui retourne une valeur truthy ou falsy. Les valeurs truthy incluent ici `true` et les valeurs non falsy. Les valeurs falsy incluent ici `false`, `null`, `0`, etc.

Après la condition, vous avez le point d'interrogation (que vous pouvez considérer comme "interrogeant la condition"), suivi de **trueExpression**. Cette expression est exécutée si l'expression conditionnelle est évaluée à `true`.

Après l'expression vraie, vous avez un deux-points, suivi de **falseExpression**. Cette expression est exécutée si l'expression conditionnelle est évaluée à `false`.

L'opérateur ternaire retourne une valeur que vous pouvez assigner à une variable. Vous ne pouvez pas utiliser l'opérateur sans assigner la valeur retournée à une variable :

```js
const result = condition
  ? trueExpression
  : falseExpression
```

La valeur retournée dépend de l'évaluation de l'expression conditionnelle. Si la condition est `true`, la valeur retournée par **trueExpression** est assignée à la variable. Sinon, la valeur retournée par **falseExpression** sera assignée à la variable.

## Comment utiliser l'opérateur ternaire à la place des instructions `if`

L'opérateur ternaire peut être un bon remplacement pour les instructions `if` dans certains cas. Il vous permet d'écrire des lignes de code concises, plus propres et plus faciles à lire si utilisé correctement.

Voyons un exemple :

```js
const score = 80
let scoreRating

if (score > 70) {
  scoreRating = "Excellent"
} else {
  scoreRating = "Do better"
}

console.log(scoreRating)
// "Excellent"
```

Dans cet exemple, nous avons une variable `score` avec **80** et une variable `scoreRating`. Ensuite, nous avons une instruction `if` qui vérifie `score > 70`. Si cette condition est évaluée à `true`, la variable `scoreRating` est assignée à **"Excellent"**, sinon, elle est assignée à **"Do better"**.

Nous pouvons améliorer ce code avec l'opérateur ternaire. Voici comment.

Rappelons la syntaxe : vous avez la condition, un point d'interrogation, l'expression vraie, un deux-points, et enfin une expression fausse. Regardons cela en code :

```js
const score = 80

const scoreRating =
  score > 70 ? "Excellent" : "Do better"

console.log(scoreRating)
// Excellent
```

C'est ainsi que nous utilisons l'opérateur ternaire. Les expressions vraies et fausses ici sont des chaînes de caractères qui seront retournées à la variable `scoreRating` en fonction de notre condition `score > 70`.

Les expressions vraies et fausses peuvent être n'importe quel type d'expression, des exécutions de fonctions aux opérations arithmétiques, etc. Voici un exemple avec une exécution de fonction :

```js
function printPoor() {
  console.log("Poor result")
  return "poor"
}

function printSuccess() {
  console.log("Nice result")
  return "success"
}


const pass = false;

const result = pass ? printSuccess() : printPoor()
// Poor result (console.log executed)

console.log(result)
// poor
```

Ici, vous voyez que comme la condition retourne `false`, l'expression fausse, `printPoor()` est exécutée, ce qui affiche "Poor result" dans la console. Et comme l'expression fausse retourne "poor", vous pouvez voir que cette valeur est assignée à la variable `result`.

Pour le reste de cet article, j'utiliserai des expressions vraies et fausses de type chaîne de caractères pour simplifier.

## Comment utiliser les opérateurs ternaires imbriqués

Que faire si vous souhaitez réaliser une instruction `if...else if...else` avec un opérateur ternaire ? Vous pouvez alors utiliser des opérateurs ternaires imbriqués. Vous devez cependant être prudent dans leur utilisation, car cela peut rendre votre code plus difficile à lire.

Voyons un exemple :

```js
const score = 60
let scoreRating

if (score > 70) {
  scoreRating = "Excellent"
} else if (score > 50) {
  scoreRating = "Average"
} else {
  scoreRating = "Do better"
}

console.log(scoreRating)
// "Average"
```

Nous avons ici une instruction `if-else-if-else` où nous vérifions d'abord si `score > 70`. Si cela retourne `true`, nous assignons "Excellent" à la variable `scoreRating`. Si cela retourne `false`, nous vérifions si `score > 50`. Si cette deuxième condition retourne `true`, nous assignons "Average" à la variable, mais si cela retourne également false, nous assignons finalement (`else`) "Do better" à la variable.

Voyons comment faire cela avec l'opérateur ternaire :

```js
const score = 60

const scoreRating =
  score > 70
    ? "Excellent"
    : score > 50
    ? "Average"
    : "Do better"

console.log(scoreRating)
// "Average"
```

Ici, vous voyez que nous avons deux points d'interrogation et deux deux-points. Dans le premier opérateur ternaire, nous avons l'expression conditionnelle `score > 70`. Après le premier point d'interrogation, nous avons l'expression vraie qui est **"Excellent"**. Après le premier deux-points, l'expression suivante est censée être l'expression fausse. Pour l'expression fausse, nous déclarons une autre expression conditionnelle en utilisant l'opérateur ternaire.

La deuxième condition ici est `score > 70`. Après le deuxième point d'interrogation, nous avons l'expression vraie qui est **"Average"**. Après le deuxième deux-points, nous avons maintenant une autre expression fausse, qui est **"Do better"**.

Avec cela, si la première condition est vraie, "Excellent" est retourné à `scoreRating`. Si la première condition est fausse, alors nous avons une autre vérification de condition. Si cette deuxième condition est vraie, "Average" est retourné à la variable. Si cette deuxième condition est également fausse, alors nous avons l'expression fausse finale, "Do better", qui sera assignée à la variable.

## Plusieurs opérateurs ternaires peuvent rendre votre code illisible

Dans les exemples précédents, nous avons vu comment nous pouvons améliorer notre code tout en maintenant sa lisibilité. Mais vous devez être prudent lorsque vous utilisez plusieurs opérateurs ternaires.

Imaginez que nous avions un opérateur ternaire supplémentaire dans notre exemple précédent :

```js
const score = 45

const scoreRating =
  score > 70
    ? "Excellent"
    : score > 50
    ? "Average"
    : score > 40
    ? "Fair"
    : "Do better"

console.log(scoreRating)
// "Fair"
```

Ici, nous avons trois opérateurs ternaires, et vous pouvez voir que les choses deviennent plus difficiles à lire.

Dans des cas comme celui-ci où vous avez besoin de plusieurs conditions, l'utilisation d'une instruction `if` ou `switch`, bien que nécessitant des lignes de code plus longues, vous permet d'écrire un code plus lisible.

## Conclusion

L'opérateur ternaire vous permet d'évaluer des expressions conditionnelles et peut substituer les instructions `if` dans certains cas. Il vous permet d'écrire un code plus court et plus propre (même sur une seule ligne).

Dans cet article, je vous ai montré comment il fonctionne, en utilisant quelques exemples `if` et la version avec l'opérateur ternaire. J'ai également souligné que vous devez être prudent lorsque vous utilisez des opérateurs ternaires imbriqués, car cela peut rendre votre code illisible.

Si vous avez aimé cet article, merci de le partager !