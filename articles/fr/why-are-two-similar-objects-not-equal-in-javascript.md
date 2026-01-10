---
title: Pourquoi deux objets similaires ne sont-ils pas égaux en JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-18T18:53:47.000Z'
originalURL: https://freecodecamp.org/news/why-are-two-similar-objects-not-equal-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/32-objects-not-equal-1.png
tags: []
seo_title: Pourquoi deux objets similaires ne sont-ils pas égaux en JavaScript ?
seo_desc: "By Dillion Megida\nIn JavaScript, two objects may not be equal even though\
  \ they appear to be similar. Why is that the case? \U0001F914 Let's understand why.\n\
  For example:\nconst obj1 = {\n  name: \"Dillion\"\n}\nconst obj2 = {\n  name: \"\
  Dillion\"\n}\n\nconsole.log(obj1 =..."
---

Par Dillion Megida

En JavaScript, deux objets peuvent ne pas être égaux même s'ils semblent similaires. Pourquoi est-ce le cas ? 🤔 Comprenons pourquoi.

Par exemple :

```js
const obj1 = {
  name: "Dillion"
}
const obj2 = {
  name: "Dillion"
}

console.log(obj1 === obj2)
// false
```

Comme vous pouvez le voir ici, `obj1` et `obj2` semblent similaires. Ils ont tous les deux la propriété `name` avec une valeur de "Dillion". Mais les comparer--`obj1 === obj2`--retourne `false`. 🤔

La même chose s'applique aux tableaux :

```js
let arr1 = [1, 2, 3]
let arr2 = [1, 2, 3]

console.log(arr1 === arr2)
// false
```

Pour comprendre pourquoi c'est le cas, vous devez comprendre ce que sont les valeurs **primitives** et **de référence** en JavaScript.

## Valeurs Primitives et de Référence

Pensez à une valeur primitive comme à **une seule valeur** (statique, fixe) et à une valeur de référence comme à **un groupe de valeurs multiples** ou à une valeur (dynamique).

Les valeurs primitives sont des types `string`, `number`, `boolean`, `null`, `undefined`, `symbol`, et `BigInt`. Ces valeurs sont fixes et stockées sur la **pile**, par exemple :

```js
let name = "Dillion"
let age = 60
let isRaining = true
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-71.png)

Les valeurs de référence sont des types `object` qui incluent les objets, les tableaux et les fonctions. Ces valeurs sont dynamiques (peuvent contenir plusieurs valeurs, propriétés, et peuvent être modifiées au fil du temps) et sont stockées sur le **tas**, avec une valeur de référence dans la pile, par exemple :

```js
let array = [1, 2, 3]
let obj = { name: "Dillion" }
function print() {
  console.log('hello')
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-72.png)

La valeur de référence est une adresse qui pointe vers l'emplacement des données en mémoire.

Voici un article où j'ai expliqué la différence en détail : [Primitive and Reference Values Simplified](https://deeecode.com/p/primitive-vs-reference-values/)

## Comparaison des Valeurs Primitives et de Référence

Lorsque vous comparez des valeurs primitives, vous comparez des valeurs **statiques**, qui ont une taille fixe sur la pile :

```js
let name = "Dillion"
let name2 = "Dillion"

console.log(name === name2)
// true
```

Ici, nous comparons `name` et `name2` pour voir s'ils sont égaux. Ce qui se passe ici, c'est que JavaScript vérifie les variables `name` et `name2` dans la pile, et voit qu'elles ont des valeurs égales, donc c'est vrai--elles sont égales.

Dans le cas des objets, vous comparez les **références** (les **adresses**) et non les valeurs exactes. Voici ce que je veux dire.

Si vous avez deux tableaux comme ceci :

```js
let array = [1, 2, 3]
let array2 = [1, 2, 3]
```

Voici à quoi cela ressemblerait sur la pile et le tas :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-73.png)

Comme vous pouvez le voir ici, pour `array`, `[1, 2, 3]` n'est pas stocké sur la pile. Il est stocké sur le tas, et l'emplacement mémoire de ces données est stocké sur la pile en tant que référence.

La même chose pour `array2` ; `[1, 2, 3]` n'est pas stocké sur la pile. Il est stocké sur le tas, dans un emplacement mémoire différent et la référence est stockée sur la pile.

Lorsque vous comparez les deux tableaux comme `array === array2`, vous ne comparez pas exactement `[1, 2, 3] === [1, 2, 3]` mais vous comparez en réalité `refForArray === refForArray2` (ref est l'abréviation de référence).

Comme nous l'avons vu dans l'illustration du tas, `array` et `array2` ont des emplacements mémoire différents, ce qui signifie qu'ils ont des références différentes, ce qui signifie alors que la variable `array` n'est pas égale à la variable `array2`.

La seule façon pour que `array` et `array2` soient égaux, c'est si vous avez quelque chose comme :

```js
let array = [1, 2, 3]
let array2 = array

console.log(array === array2)
// true
```

En assignant `array` à `array2`, vous assigner la référence que `array` détient dans la pile, à `array2` :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-74.png)

Par conséquent, `array` et `array2` ont maintenant la même valeur--la même **référence**.

## Comment comparer des objets

Nous avons vu que dans notre tentative de comparer deux valeurs d'objets, nous comparons en réalité la référence et non les données de l'objet. Alors, comment comparer correctement les données de l'objet ?

Il existe plusieurs façons de le faire, mais je vais en partager deux.

### Comparer des objets en utilisant `_.isEqual` de Lodash

Vous pouvez écrire une fonction qui effectue une vérification d'égalité entre deux objets, mais cela peut devenir compliqué lorsque vous devez comparer des objets profondément imbriqués qui peuvent avoir différentes valeurs, y compris des objets.

Une approche plus rapide consiste à utiliser la [méthode isEqual de Lodash](https://lodash.com/docs/4.17.15#isEqual) qui est une solution efficace qui gère la comparaison profonde entre deux valeurs :

```js
const _ = require('lodash'); 

const array = [1, 2, 3]
const object = { name: "Dillion" }

const array2 = [1, 2, 3]
const object2 = { name: "Dillion" }

console.log(_.isEqual(array, array2))
// true

console.log(_.isEqual(object, object2))
// true
```

### Comparer des objets en utilisant `JSON.stringify()`

Supposons que vous ne vouliez pas utiliser Lodash, vous pouvez utiliser `JSON.stringify` qui stringifie récursivement un objet ou un tableau en une chaîne :

```js
const array = [1, 2, 3]
const object = { name: "Dillion" }

const array2 = [1, 2, 3]
const object2 = { name: "Dillion" }

console.log(
  JSON.stringify(array)
  ===
  JSON.stringify(array2)
)
// true

console.log(
  JSON.stringify(object)
  ===
  JSON.stringify(object2)
)
// true
```

Puisque la version stringifiée est un type primitif (statique), les données des deux valeurs peuvent être comparées. Mais voici une limitation avec `JSON.stringify()`.

`JSON.stringify` peut retourner des résultats différents si l'ordre ou les propriétés d'un objet sont différents. Par exemple :

```js
const object = {
  name: "Dillion",
  age: 50
}

const object2 = {
  age: 50,
  name: "Dillion"
}

console.log(
  JSON.stringify(object)
  ===
  JSON.stringify(object2)
)
// false
```

Dans `object`, nous avons `name` avant `age`, mais dans `object2`, nous avons `age` avant `name`. Cela signifie que leurs représentations stringifiées seraient différentes et, par conséquent, leurs données ne sont pas égales.

## Conclusion

Les valeurs primitives et de référence sont des concepts fondamentaux à comprendre lorsque vous travaillez avec des données en JavaScript. Et comme nous l'avons vu dans cet article, comparer des valeurs primitives est plus facile, mais comparer des valeurs de référence peut être plus délicat car lorsque vous pensez comparer les **données**, vous ne réalisez peut-être pas que vous comparez en réalité la **référence**.

J'espère que cet article répond à la question de "Pourquoi deux objets similaires ne sont-ils pas égaux en JavaScript ?". Si c'est le cas, veuillez partager cet article 👍🏾