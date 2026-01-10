---
title: Qu'est-ce que l'opérateur de coalescence des nuls en JavaScript et à quoi sert-il
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-05T06:55:34.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-nullish-coalescing-operator-in-javascript-and-how-is-it-useful
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/28-nullish-coalescing-operator.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que l'opérateur de coalescence des nuls en JavaScript et à quoi
  sert-il
seo_desc: 'By Dillion Megida

  The Nullish Coalescing Operator is a new logical operator in JavaScript introduced
  in ES 2020. In this article, we''ll understand how this operator works.

  There are over four logical operators in JavaScript: the AND &&, OR ||, NOT !,...'
---

Par Dillion Megida

L'opérateur de coalescence des nuls est un nouvel opérateur logique en JavaScript introduit dans ES 2020. Dans cet article, nous allons comprendre comment cet opérateur fonctionne.

Il existe plus de quatre opérateurs logiques en JavaScript : le ET `&&`, le OU `||`, le NON `!`, et l'opérateur de coalescence des nuls `??`.

Parfois appelé **opérateur nul**, cet opérateur est utilisé entre deux opérandes :

```js
operand1 ?? operand2
```

Pour comprendre cet opérateur, nous devons comprendre ce que signifient "nullish", "coalescing" et **short-circuiting**.

J'ai une [vidéo sur ce sujet](https://youtu.be/CX3VWymirxw) que vous pouvez également consulter.

## Que sont les valeurs "nullish" ?

Les valeurs nullish en JavaScript sont `null` et `undefined`. Ces valeurs font partie des **valeurs falsy** mais sont plus spécifiquement appelées **valeurs nulles**. Toutes les valeurs nullish sont falsy, mais toutes les valeurs falsy (par exemple, `0`) ne sont pas nullish.

Ainsi, l'opérateur nul est lié aux valeurs `null` et `undefined` tandis que les autres opérateurs logiques sont liés aux valeurs `truthy` et `falsy` en général.

## Que signifie "coalescing" ?

Coalescing, selon le dictionnaire, signifie "se réunir pour former un tout". Comment cela s'applique-t-il à la programmation ? Cela signifie que vous rassemblez plusieurs valeurs pour en faire une seule.

En programmation, coalescing ne signifie pas spécifiquement "joindre les valeurs ensemble", mais plutôt "décider quelle valeur est faite à partir des valeurs fournies".

Nous verrons comment cela fonctionne avec des exemples plus tard dans cet article.

## Short-Circuiting

Le concept de short-circuiting s'applique à de nombreux langages de programmation. Il se produit lorsque les interpréteurs exécutent une expression liée à un booléen et sautent la partie non pertinente de l'expression.

Par exemple, une expression booléenne comme "J'ai 40 ans et je suis dans la tech". Cette expression ne serait `true` que si j'ai 40 ans, et pas seulement cela, je suis dans la tech.

Après que l'interpréteur ait exécuté "J'ai 40 ans", il ne peut pas encore conclure que l'expression entière est vraie, car dans le cas où "je ne suis **PAS** dans la tech", l'expression sera fausse. La deuxième partie de l'expression est pertinente car elle peut changer le résultat.

Mais, dans le cas où "je n'ai **PAS** 40 ans", le short-circuiting se produira. Puisque la première partie de l'expression retourne `false`, l'interpréteur sait qu'il est inutile d'évaluer la deuxième expression. La deuxième partie est non pertinente, car la valeur de cette expression ne change pas le résultat. Ainsi, l'interpréteur saute la deuxième partie (économisant ainsi des ressources--temps, puissance).

Cela s'applique également à l'opérateur nul.

Vous pouvez en apprendre davantage sur le short-circuiting [dans cet article](https://dillionmegida.com/p/short-circuit-in-programming-simplified/)

## L'opérateur de coalescence des nuls

Maintenant que nous avons examiné les fondamentaux de cet opérateur, comprenons ce que fait cet opérateur.

Lorsqu'il est utilisé dans une expression, l'opérateur nul vérifie le premier opérande (à gauche) pour voir si sa valeur est `null` ou `undefined`. Si ce n'est pas le cas, l'opérateur le retourne de l'expression. Mais si le premier opérande est l'une de ces valeurs, l'opérateur retourne le deuxième opérande de l'expression.

Voyons un exemple rapide :

```js
function expression1() {
  return null
}

const expression2 = 4 * 5

const result = expression1() ?? expression2

console.log(result)
// 20
```

Ici, nous avons une fonction appelée `expression1` qui, lorsqu'elle est appelée, retourne `null`. Et nous avons également `expression2` qui contient la valeur de l'expression **4 * 5**.

Pour la variable `result`, nous utilisons l'opérateur nul et passons `expression1()` et `expression2` comme opérandes.

Le premier opérande (l'appel de fonction expression) retourne `null`. L'opérateur confirme que le premier opérande est `null`, donc il retourne la valeur du deuxième expression : `expression2`.

Voyons un autre exemple :

```js
function expression1() {
  console.log("expression1")
  return false
}

function expression2() {
  console.log("expression2")
  return "Dillion"
}

const result = expression1() ?? expression2()

console.log(result)
// expression1
// false
```

Ici, nous avons `expression1`, une fonction qui, lorsqu'elle est appelée, exécute `console.log("expression1")`, puis retourne `false`. Et nous avons `expression2`, qui est une fonction qui, lorsqu'elle est appelée, exécute `console.log("expression2")`, et retourne "Dillion".

En utilisant l'opérateur nul, nous avons le premier opérande comme `expression1()`, et le deuxième opérande comme `expression2()` et assignons la valeur de l'expression à `result`.

Lorsque nous exécutons ce code, vous voyez que nous avons "expression1" enregistré, ce qui provient de l'exécution de `expression1`. Et vous voyez que `result` est enregistré comme `false`. Cela signifie que `expression1()` est l'expression retournée par l'opérateur nul.

L'opérateur vérifie si la première expression retourne `null` ou `undefined`, auquel cas il retournerait la deuxième expression. Mais dans ce cas, la première expression retourne `false`, donc l'opérateur retournerait la première expression.

Une autre chose que vous remarquez est que "expression2" n'est pas enregistré. Cela signifie que `expression2()` n'est pas exécuté du tout. **Short-circuiting** se produit ici.

Puisque l'opérateur a déjà confirmé que le premier opérande n'est PAS `null` ou `undefined`, il ne se soucie pas de la deuxième expression, car la valeur de la deuxième expression ne change pas ce que l'opérateur retournerait.

## Nullish vs OR Operator

Les opérateurs Nullish et OR ont quelques similitudes, mais ils fonctionnent un peu différemment.

L'opérateur OR **vérifie si le premier opérande est une valeur truthy**. Si le premier opérande en est une, il la retourne, sinon, il retourne le deuxième opérande.

Mais, l'opérateur Nullish **vérifie si le premier opérande est une valeur nullish**. Si le premier opérande n'en est pas une, il le retourne, sinon, il retourne le deuxième opérande.

Voici un exemple avec OR :

```js
const expression1 = ""
const expression2 = "Dillion"

const result = expression1 || expression2

console.log(result)
// "Dillion"
```

Puisque le premier opérande, `expression1`, est une valeur falsy (chaîne vide), l'opérateur retourne le deuxième opérande. Si `expression1` était 20, par exemple (ce qui est une valeur truthy), il aurait été retourné, et le short-circuiting se serait produit.

Voici un exemple avec Nullish :

```js
const expression1 = undefined
const expression2 = "Dillion"

const result = expression1 ?? expression2

console.log(result)
// "Dillion"
```

En utilisant l'opérateur nul ici, le premier opérande est `undefined`, une valeur nullish, donc l'opérateur retourne le deuxième opérande. Si `expression1` était `false`, 20, ou une autre valeur non-nullish, il aurait été retourné, et le short-circuiting se serait produit.

## Utilisation de l'opérateur nul directement avec AND/OR

Vous pouvez directement mélanger les opérateurs AND et OR dans des expressions mais vous ne pouvez pas faire cela pour l'opérateur nul. Voici ce que je veux dire :

```js
exp1 && exp2 || exp3 && exp4
```

Ici, nous combinons AND et OR. L'ordre dans cette expression est :
1. "exp1 ET exp2"
2. "le résultat de cela OU exp3"
3. "le résultat de cela ET exp4"

> N'oubliez pas que, en raison du short-circuiting, l'étape 2 ou l'étape 3 peut ne jamais être atteinte.

Mais vous ne pouvez pas faire ces combinaisons directement avec l'opérateur nul. Par exemple :

```js
exp1 && exp2 ?? exp3 || exp4
```

Nous mélangeons AND, Nullish et OR ici : cela générera une erreur de syntaxe. Voyons un exemple concret :

```js
function expression1() {
  return null
}

const expression2 = 20 < 10

const expression3 = "Dillion"

const result = expression1() ?? expression2 || expression3
// SyntaxError: Unexpected token '||'
```

Nous avons `expression1`, une fonction qui, lorsqu'elle est appelée, retourne `null`, `expression2` qui contient la valeur retournée par **20 < 10**, et `expression3` qui contient la valeur de chaîne "Dillion".

Utilisez les opérateurs nul et OR avec ces trois expressions, ce que je m'attendrais est que :

1. `expression1()` retourne `null`, donc l'opérateur nul retourne le côté droit de l'expression qui est `expression2 || expression3`
2. du côté droit, l'opérateur OR est utilisé, qui vérifie si le côté gauche, `expression2` est truthy ; puisque c'est une valeur falsy, l'opérateur retourne le côté droit

Mais, en exécutant cela, nous obtenons une erreur : **SyntaxError: Unexpected token '||'**. Cela signifie que vous ne pouvez pas utiliser ces opérateurs directement. La seule façon de les combiner est d'ajouter des parenthèses comme ceci :

```js
const result = (expression1() ?? expression2) || expression3

console.log(result)
// Dillion
```

En entourant **expression1() ?? expression2** de parenthèses, nous pouvons ensuite utiliser le résultat retourné comme premier opérande pour l'opérateur OR, et ajouter `expression3` comme deuxième opérande.

## Conclusion

L'opérateur nul est très utile pour déclarer des valeurs par défaut pour les valeurs potentielles `null` ou `undefined`. Supposons que vous attendiez un objet d'une API. Si cet objet ne contient pas une propriété attendue, cette propriété peut soit contenir `null`, soit être `undefined` comme ceci :

```js
const obj = {}

console.log(obj.type)
// undefined
```

En utilisant l'opérateur nul, nous pouvons fournir une valeur par défaut :

```js
const obj = {}

console.log(obj.type ?? "default")
// "default"
```

Il existe de nombreuses autres façons d'utiliser cet opérateur pour les valeurs par défaut ou les vérifications sécurisées.

Si vous avez aimé cet article, merci de le partager :)