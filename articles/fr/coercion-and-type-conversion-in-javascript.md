---
title: Coercition et Conversion de Type en JavaScript – Expliqué avec des Exemples
  de Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-07T17:03:46.000Z'
originalURL: https://freecodecamp.org/news/coercion-and-type-conversion-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/4.-coercion.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Coercition et Conversion de Type en JavaScript – Expliqué avec des Exemples
  de Code
seo_desc: 'By Dillion Megida

  Coercion is an automatic type conversion that occurs in JavaScript when you want
  to perform certain operations. I''ll explain what coercion is in this article.

  What is Type Conversion?

  As the name implies, type conversion is the proc...'
---

Par Dillion Megida

La coercition est une conversion automatique de type qui se produit en JavaScript lorsque vous souhaitez effectuer certaines opérations. Je vais expliquer ce qu'est la coercition dans cet article.

## Qu'est-ce que la Conversion de Type ?

Comme son nom l'indique, la conversion de type est le processus de conversion d'une valeur d'un type à un autre.

Les valeurs en JavaScript peuvent être de différents types. Vous pouvez avoir un nombre, une chaîne de caractères, un objet, un booléen – vous l'appelez comme vous voulez. Parfois, vous pouvez vouloir convertir des données d'un type à un autre pour les adapter à une certaine opération.

La conversion de type peut être implicite (effectuée automatiquement pendant l'exécution du code) ou explicite (effectuée par vous, le développeur).

La Conversion de Type Implicite est également connue (et plus couramment appelée) sous le nom de **Coercition** tandis que la Conversion de Type Explicite est également connue sous le nom de **Casting de Type**. Examinons ces deux conversions en détail.

J'ai également une [version vidéo](https://youtu.be/00vjwv2BJqE) de ce tutoriel si vous préférez cela.

## Qu'est-ce que la Conversion de Type Implicite (Coercition) ?

Il existe certaines opérations que vous pourriez essayer d'exécuter en JavaScript qui sont littéralement impossibles. Par exemple, regardez le code suivant :

```js
const sum = 35 + "hello"
```

Ici, vous essayez d'additionner un nombre et une chaîne de caractères. Cela n'est, pratiquement parlant, pas possible. Vous ne pouvez additionner que des nombres (**sum**) ensemble ou additionner des chaînes de caractères (**concaténer**) ensemble.

Alors, que se passe-t-il si vous essayez d'exécuter le code ?

Eh bien, JavaScript est un langage faiblement typé. Au lieu de JavaScript de lever une erreur, il force le type d'une valeur à s'adapter au type de l'autre valeur afin que l'opération puisse être effectuée.

Dans ce cas, en utilisant le signe **+** avec un nombre et une chaîne de caractères, le nombre est forcé à une chaîne de caractères, puis le signe **+** est utilisé pour une opération de concaténation.

```js
const sum = 35 + "hello"

console.log(sum)
// 35hello

console.log(typeof sum)
// string
```

Ceci est un exemple de coercition où le type d'une valeur est forcé à s'adapter à l'autre afin que l'opération puisse continuer.

Avec le signe plus, il est plus idéal pour le nombre d'être converti en chaîne de caractères (au lieu de la chaîne de caractères convertie en nombre). Cela est dû au fait qu'un équivalent numérique d'une chaîne de caractères est `NaN` mais un équivalent de chaîne de caractères pour un nombre, disons `15`, est `"15"` – il est donc plus logique de **concaténer** deux chaînes de caractères que de **somme** un nombre et `NaN`.

Regardez un autre exemple ci-dessous :

```js
const times = 35 * "hello"

console.log(times)
// NaN
```

Ici, nous utilisons le signe de multiplication **\*** pour un nombre et une chaîne de caractères. Il n'y a pas d'opération avec les chaînes de caractères qui implique la multiplication, donc ici, la coercition idéale est de la chaîne de caractères vers le nombre (car les nombres ont des opérations compatibles avec la multiplication).

Mais puisque une chaîne de caractères (dans ce cas, `"hello"`) est convertie en nombre (qui est `NaN`) et que ce nombre est multiplié par `35`, le résultat final est `NaN`.

La coercition est généralement causée par différents opérateurs utilisés entre différents types de données :

```js
const string = ""
const number = 40
const boolean = true

console.log(!string)
// true - la chaîne est forcée en booléen `false`, puis l'opérateur NOT la nie

console.log(boolean + string)
// "true" - le booléen est forcé en chaîne "true", et concaténée avec la chaîne vide

console.log(40 + true)
// 41 - le booléen est forcé en nombre 1, et additionné avec 40
```

Un opérateur très courant qui cause la coercition est l'**opérateur d'égalité lâche** (**==**, ou double égal).

## Double Égalité et Coercition

En JavaScript, il existe à la fois l'opérateur de double égalité (**==** qui est appelé l'**opérateur d'égalité lâche**) et l'opérateur de triple égalité (**===** qui est appelé l'**opérateur d'égalité stricte**). Vous utilisez les deux opérateurs pour comparer l'égalité des valeurs.

### Comment fonctionne l'Opérateur d'Égalité Lâche

L'**opérateur d'égalité lâche** effectue une vérification lâche. Il vérifie si les valeurs sont égales. Les types ne sont pas un focus pour cet opérateur – seules les valeurs sont le facteur majeur.

Ce que je veux dire ici, c'est que **20**, une valeur de type `number`, et **"20"**, une valeur de type `string`, sont égales lorsque vous utilisez la double égalité :

```js
const variable1 = 20
const variable2 = "20"

console.log(variable1 == variable2)
// true
```

Bien que les types ne soient pas égaux, l'opérateur retourne `true` parce que les valeurs sont égales. Ce qui se passe ici est la **coercition**.

Lorsque vous utilisez l'**opérateur d'égalité lâche** avec des valeurs de types différents, ce qui se passe en premier est la coercition. Encore une fois, c'est là qu'une valeur est convertie au type qui convient à l'autre, avant que la comparaison ne se produise.

Dans ce cas, la **chaîne "20"** est convertie en type nombre (qui est `20`) puis comparée avec l'autre valeur, et elles sont toutes deux égales.

Un autre exemple :

```js
const variable1 = false
const variable2 = ""

console.log(variable1 == variable2)
// true
```

Ici, `variable1` est la valeur **false** (type booléen) et `variable2` est la valeur **""** (une chaîne vide, de type chaîne). Comparer les deux variables avec la double égalité retourne `true`. C'est parce que la chaîne vide est forcée en type booléen (qui est **false**).

### Comment fonctionne l'Opérateur d'Égalité Stricte

Cet opérateur effectue une vérification stricte – c'est-à-dire qu'il vérifie strictement les valeurs comparées, ainsi que les types. La coercition de type ne se produit pas ici, donc il n'y a pas de réponses inattendues. Voici les exemples ci-dessus :

```js
const variable1 = 20
const variable2 = "20"

console.log(variable1 === variable2)
// false

const variable3 = false
const variable4 = ""

console.log(variable3 === variable4)
// false
```

Dans le cas de `variable1` et `variable2`, elles ont les mêmes valeurs, mais les types ne sont pas les mêmes. Donc la triple égalité retourne `false`.

Dans le cas de `variable3` et `variable4`, elles ont les mêmes valeurs (si l'une est convertie au type de l'autre) mais les types ne sont pas les mêmes, donc la triple égalité retourne `false` cette fois aussi.

## Qu'est-ce que la Conversion de Type Explicite (Casting de Type) ?

Ici, vous convertissez explicitement une valeur d'un type à un autre. Cela peut également être pour que vous exécutiez une certaine opération avec succès.

Pour convertir explicitement les types, vous utilisez les `Constructeurs` de type. Par exemple, pour convertir un nombre en chaîne de caractères :

```js
const number = 30

const numberConvert = String(number)

console.log(numberConvert)
// "30"

console.log(typeof numberConvert)
// string
```

Un autre exemple est de convertir un nombre en booléen :

```js
const number = 30

const numberConvert = Boolean(number)

console.log(numberConvert)
// true

console.log(typeof numberConvert)
// boolean
```

Et un autre exemple, pour convertir un booléen en chaîne de caractères :

```js
const boolean = false

const booleanConvert = String(boolean)

console.log(booleanConvert)
// "false"

console.log(typeof booleanConvert)
// string
```

Dans ces exemples, nous convertissons explicitement une valeur d'un type à un autre. Quels sont les cas où vous devez faire cela ?

Cela est utile lorsque vous ne savez pas quel type vous attendez pour une valeur. Par exemple, des données provenant d'une API. Supposons qu'une API est configurée pour retourner une chaîne de caractères, peut-être "50" et que vous voulez la comparer à un nombre en utilisant l'égalité stricte comme ceci :

```js
const apiData = {
  rate: "50"
}

console.log(apiData.rate === 50)
// false
```

Dans un tel cas, vous voulez d'abord vous assurer que la valeur est explicitement de type nombre (au lieu de vous fier à la double égalité pour déclencher la coercition) avant de faire la vérification :

```js
const apiData = {
  rate: "50"
}

const rate = Number(apiData.rate)

console.log(rate === 50)
// true
```

## Conclusion

Parce que JavaScript est un langage faiblement typé, parfois vous pouvez avoir des conversions de type inattendues. Cela se produit implicitement lorsque vous essayez d'utiliser certains opérateurs entre des valeurs de types différents. Ensuite, au lieu d'obtenir une erreur, JavaScript essaie de "vous aider". JavaScript serait comme...

"Oh, je pense qu'ils voulaient taper une chaîne de caractères mais ils ont tapé un nombre à la place. Aidons-les à le convertir en chaîne de caractères avant d'effectuer l'opération. Ils apprécieraient cela 😇"

Eh bien, pas exactement comme cela 😂 mais j'espère que vous comprenez l'idée.

Dans cet article, nous avons vu comment fonctionne la conversion de type en JavaScript – à la fois implicitement et explicitement – avec des exemples.

Bien que la coercition puisse être utile parfois, elle peut causer des erreurs inattendues, surtout lorsque vous comparez des valeurs avec l'**opérateur d'égalité lâche**. C'est pourquoi il est recommandé d'utiliser toujours l'**opérateur d'égalité stricte** pour comparer des valeurs.

De plus, [utiliser TypeScript](https://www.freecodecamp.org/news/an-introduction-to-typescript/) peut vous aider à éviter les erreurs imprévisibles car vous pouvez vous assurer que les variables sont des types de données que vous souhaitez qu'elles soient.