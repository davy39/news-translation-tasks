---
title: JavaScript Modulo, Division, Reste et Autres Opérateurs Mathématiques Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T18:43:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-arithmetic-math-operators-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d3b740569d1a4ca369f.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: toothbrush
  slug: toothbrush
seo_title: JavaScript Modulo, Division, Reste et Autres Opérateurs Mathématiques Expliqués
seo_desc: 'JavaScript provides the user with five arithmetic operators: +, -, *, /
  and %. The operators are for addition, subtraction, multiplication, division and
  remainder (or modulo), respectively.

  Addition

  Syntax

  a + b

  Usage

  2 + 3          // returns 5

  true...'
---

JavaScript fournit à l'utilisateur cinq opérateurs arithmétiques : `+`, `-`, `*`, `/` et `%`. Les opérateurs sont respectivement pour l'addition, la soustraction, la multiplication, la division et le reste (ou modulo).

## **Addition**

**Syntaxe**

`a + b`

**Utilisation**

```text
2 + 3          // retourne 5
true + 2       // interprète true comme 1 et retourne 3
false + 5      // interprète false comme 0 et retourne 5
true + "bar"   // concatène la valeur booléenne et retourne "truebar"
5 + "foo"      // concatène la chaîne et le nombre et retourne "5foo"
"foo" + "bar"  // concatène les chaînes et retourne "foobar"
```

*Conseil :* Il existe un opérateur d'[incrément](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Increment_()) pratique qui est un excellent raccourci lorsque vous ajoutez des nombres par 1.

## **Soustraction**

**Syntaxe**

`a - b`

**Utilisation**

```text
2 - 3      // retourne -1
3 - 2      // retourne 1
false - 5  // interprète false comme 0 et retourne -5
true + 3   // interprète true comme 1 et retourne 4
5 + "foo"  // retourne NaN (Not a Number)
```

*Conseil :* Il existe un opérateur de [décrément](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators#Decrement_(--)) pratique qui est un excellent raccourci lorsque vous soustrayez des nombres par 1.

## **Multiplication**

**Syntaxe**

`a * b`

**Utilisation**

```text
2 * 3                // retourne 6
3 * -2               // retourne -6
false * 5            // interprète false comme 0 et retourne 0
true * 3             // interprète true comme 1 et retourne 3
5 * "foo"            // retourne NaN (Not a Number)
Infinity * 0         // retourne NaN
Infinity * Infinity  // retourne Infinity
```

## **Division**

**Syntaxe**

`a / b`

**Utilisation**

```text
3 / 2                // retourne 1.5
3.0 / 2/0            // retourne 1.5
3 / 0                // retourne Infinity
3.0 / 0.0            // retourne Infinity
-3 / 0               // retourne -Infinity
false / 5            // interprète false comme 0 et retourne 0
true / 2             // interprète true comme 1 et retourne 0.5
5 + "foo"            // retourne NaN (Not a Number)
Infinity / Infinity  // retourne NaN
```

## **Reste**

**Syntaxe**

`a % b`

**Utilisation**

```text
3 % 2          // retourne 1
true % 5       // interprète true comme 1 et retourne 1
false % 4      // interprète false comme 0 et retourne 0
3 % "bar"      // retourne NaN
```

## **Incrément**

**Syntaxe**

`a++ ou ++a`

**Utilisation**  
// Postfix x = 3; // déclare une variable y = x++; // y = 4, x = 3  
// Préfix var a = 2; b = ++a; // a = 3, b = 3

## **Décrément**

**Syntaxe**

`a-- ou --a`

**Utilisation**  
// Postfix x = 3; // déclare une variable y = x--; // y = 3, x = 3  
// Préfix var a = 2; b = --a; // a = 1, b = 1 _!Important!_ Comme vous pouvez le voir, vous **ne pouvez pas** effectuer d'opérations sur `Infinity`.

## Plus sur les maths en JavaScript :

* [Fonctions mathématiques de JavaScript expliquées](https://www.freecodecamp.org/news/math-in-javascript/)
* [La méthode math.random() de JavaScript expliquée](https://www.freecodecamp.org/news/p/b988fbe9-a282-435b-8df0-71eb9193ad5c/)