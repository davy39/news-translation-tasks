---
title: Opérateurs unaires, binaires et ternaires en JavaScript – Expliqués avec des
  exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-17T16:58:24.000Z'
originalURL: https://freecodecamp.org/news/unary-binary-ternary-operators-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/16.-unary-binary-ternary.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Opérateurs unaires, binaires et ternaires en JavaScript – Expliqués avec
  des exemples
seo_desc: "By Dillion Megida\nThere are many operators in JavaScript that let you\
  \ carry out different operations. \nThese operators can be categorized based on\
  \ the number of operands they require, and I'll be using examples to explain these\
  \ categories in this tut..."
---

Par Dillion Megida

Il existe de nombreux opérateurs en JavaScript qui vous permettent d'effectuer différentes opérations.

Ces opérateurs peuvent être catégorisés en fonction du nombre d'opérandes qu'ils nécessitent, et j'utiliserai des exemples pour expliquer ces catégories dans ce tutoriel.

Les trois catégories d'opérateurs basées sur le nombre d'opérandes qu'ils nécessitent sont :

* Opérateurs unaires : qui nécessitent un opérande (Un)
* Opérateurs binaires : qui nécessitent deux opérandes (Bi)
* Opérateurs ternaires : qui nécessitent trois opérandes (Ter)

Notez que ces catégories ne s'appliquent pas uniquement à JavaScript. Elles s'appliquent à la programmation en général.

Dans le reste de cet article, je partagerai quelques exemples d'opérateurs qui appartiennent à chaque catégorie.

J'ai une [version vidéo de ce sujet](https://youtu.be/dwP0WuzbFA0) que vous pouvez regarder si vous êtes intéressé.

## Qu'est-ce qu'un opérande ?

Tout d'abord, comprenons ce qu'est un opérande. Dans une opération, un **opérande** est la donnée qui est **opérée**. L'opérande combiné avec l'opérateur forme une opération.

Regardez cet exemple :

```js
20 + 30
```

Ici, nous avons une opération de somme (que nous apprendrons plus tard). Cette opération implique l'opérateur plus `+`, et il y a deux opérandes ici : `20` et `30`.

Maintenant que nous comprenons les opérandes, voyons des exemples d'opérateurs et les catégories auxquelles ils appartiennent.

## Qu'est-ce qu'un opérateur unaire ?

Ces opérateurs nécessitent un opérande pour fonctionner. Fournir deux ou plus peut entraîner une erreur de syntaxe. Voici quelques exemples d'opérateurs qui appartiennent à cette catégorie.

### L'opérateur `typeof`

L'opérateur `typeof` retourne le type de données d'une valeur. Il nécessite un seul opérande. Voici un exemple :

```js
typeof "hello"
// string
```

Si vous lui passez deux opérandes, vous obtiendrez une erreur :

```js
typeof "hello" 50
// Uncaught SyntaxError: Unexpected number
```

### L'opérateur `delete`

Vous pouvez utiliser l'opérateur `delete` pour supprimer un élément dans un tableau ou supprimer une propriété dans un objet. C'est un opérateur unaire qui nécessite un seul opérande. Voici un exemple avec un tableau :

```js
const array = [2,3,4]
delete array[2]

console.log(array)
// [ 2, 3, <empty> ]
```

Notez que supprimer des éléments d'un tableau avec l'opérateur `delete` n'est pas la bonne façon de faire. J'ai expliqué pourquoi [dans cet article ici](https://dillionmegida.com/p/deleting-items-from-array-with-delete-keyword/)

Et voici un exemple avec un objet :

```js
const object = {
  name: "deeecode",
  age: 50
}
delete object.age

console.log(object)
// { name: 'deeecode' }
```

### L'opérateur unaire plus `+`

Cet opérateur ne doit pas être confondu avec l'opérateur plus arithmétique que j'expliquerai plus tard dans cet article. L'opérateur unaire plus tente de convertir une valeur non numérique en nombre. Il retourne `NaN` lorsque c'est impossible. Voici un exemple :

```js
+"200"
// 20 - number

+false
// 0 - number representation

+"hello"
// NaN
```

Comme vous pouvez le voir ici encore, un seul opérande est requis, qui vient après l'opérateur.

Je m'arrêterai avec ces trois exemples. Mais sachez qu'il existe d'autres opérateurs unaires tels que les opérateurs d'incrément `++`, de décrément `++`, et NOT logique `!`, pour n'en nommer que quelques-uns.

## Qu'est-ce qu'un opérateur binaire ?

Ces opérateurs nécessitent deux opérandes pour fonctionner. Si un ou plus de deux opérandes sont fournis, ces opérateurs entraînent une erreur de syntaxe.

Regardons quelques opérateurs qui appartiennent à cette catégorie.

### Opérateurs arithmétiques

Tous les opérateurs arithmétiques sont des opérateurs binaires. Vous avez le premier opérande à gauche de l'opérateur, et le second opérande à droite de l'opérateur. Voici quelques exemples :

```js
10 + 20
// 30

20 - 5
// 15

30 / 6
// 5
```

Si vous ne fournissez pas deux opérandes, vous obtiendrez une erreur de syntaxe. Par exemple :

```js
10 +
// SyntaxError: Unexpected end of input
```

### Opérateurs de comparaison

Tous les opérateurs de comparaison nécessitent également deux opérandes. Voici quelques exemples :

```js
80 < 20
// false

10 < 40
// true

2 >= 2
// true
```

### Opérateur d'affectation `=`

L'opérateur d'affectation est également un opérateur binaire car il nécessite deux opérandes. Par exemple :

```js
const number = 20
```

À gauche, vous avez le premier opérande, la variable (`const number`), et à droite, vous avez le second opérande, la valeur (`20`).

Vous vous demandez probablement : "n'est-ce pas que `const number` est deux opérandes ?". Eh bien, `const` et `number` forment un seul opérande. La raison en est que `const` définit le comportement de `number`. L'opérateur d'affectation `=` n'a pas besoin de `const`. Vous pouvez donc utiliser l'opérateur comme ceci :

```js
number = 20
```

Mais il est bon de toujours utiliser un mot-clé de variable.

Donc, comme je l'ai dit, pensez à `const number` comme un seul opérande, et la valeur à droite comme le second opérande.

## Qu'est-ce qu'un opérateur ternaire ?

Ces opérateurs nécessitent trois opérandes. En JavaScript, il y a **un opérateur** qui appartient à cette catégorie – l'opérateur conditionnel. Dans d'autres langages, peut-être, il pourrait y avoir plus d'exemples.

### L'opérateur conditionnel `? ... :`

L'opérateur conditionnel nécessite trois opérandes :
* l'**expression conditionnelle**
* l'**expression truthy** qui est évaluée si la condition est `true`
* l'**expression falsy** qui est évaluée si la condition est `false`.

Vous pouvez en apprendre plus sur [l'opérateur conditionnel ici](https://www.freecodecamp.org/news/the-ternary-operator-in-javascript/)

Voici un exemple de son fonctionnement :

```js
const score = 80
const scoreRating = score > 50 ? "Good" : "Poor"

// "Good"
```

Le premier opérande – l'expression conditionnelle – est `score > 50`.

Le deuxième opérande – l'expression truthy – est "Good", qui sera retourné à la variable `scoreRating` si la condition est `true`.

Le troisième opérande – l'expression falsy – est "Poor", qui sera retourné à la variable `scoreRating` si la condition est `false`.

J'ai écrit un article lié à cet opérateur que vous pouvez consulter [ici](https://www.freecodecamp.org/news/why-a-ternary-operator-is-not-a-conditional-operator-in-js/). Il explique pourquoi un opérateur ternaire n'est pas un opérateur conditionnel en JavaScript.

## Conclusion

Les opérations en JavaScript impliquent un ou plusieurs opérandes et un opérateur. Et les opérateurs peuvent être catégorisés en fonction du nombre d'opérandes qu'ils nécessitent.

Dans cet article, nous avons examiné les trois catégories d'opérateurs : **unaires**, **binaires** et **ternaires**. Nous avons également vu des exemples d'opérateurs en JavaScript qui appartiennent à chaque catégorie.

Veuillez partager cet article si vous le trouvez utile.