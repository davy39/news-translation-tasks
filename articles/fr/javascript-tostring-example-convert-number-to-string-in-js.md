---
title: Exemple JavaScript toString – Comment convertir un nombre en chaîne de caractères
  en JS et plus
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-19T21:09:06.000Z'
originalURL: https://freecodecamp.org/news/javascript-tostring-example-convert-number-to-string-in-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c982c740569d1a4ca1892.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Exemple JavaScript toString – Comment convertir un nombre en chaîne de
  caractères en JS et plus
seo_desc: "By Dillion Megida\nSometimes you want to convert one data type into another\
  \ data type without changing the values manually.\nFor instance, you might want\
  \ to convert a number to a string. JavaScript sometimes does this implicitly. \n\
  Like when you use the..."
---

Par Dillion Megida

Parfois, vous souhaitez convertir un type de données en un autre sans changer les valeurs manuellement.

Par exemple, vous pourriez vouloir convertir un nombre en chaîne de caractères. JavaScript le fait parfois implicitement.

Comme lorsque vous utilisez l'opérateur double égal (`==`), ou lorsque vous essayez de faire quelque chose sur une valeur avec un type de données incompatible avec l'opération. Cela s'appelle [Type Coercion](https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/).

Cela dit, vous pouvez également convertir les types de données explicitement. Et je vais vous montrer comment faire cela dans cet article.

Le type de données chaîne de caractères est un type de données très courant en JavaScript. Pour presque tous les autres types de données, vous devez avoir une représentation sous forme de chaîne.

Comme vous avez dû voir quelque chose de similaire à `"[object Object]"` lorsque vous utilisez un objet à la place d'une chaîne de caractères réelle.

Dans cet article, nous allons apprendre ce qu'est la méthode `toString`, et comment convertir un nombre (et quelques autres types de données) en chaîne de caractères en utilisant cette méthode.


## La méthode `toString`

Comme son nom l'indique, cette méthode est utilisée pour changer les données en chaîne de caractères. Les tableaux, les nombres et les booléens ont chacun cette méthode qui convertit leurs données de diverses manières. Examinons-les individuellement maintenant.

### Comment convertir un nombre en chaîne de caractères

La méthode `toString` existe sur chaque littéral de nombre. Elle convertit les nombres en leurs représentations sous forme de chaîne. Voici comment elle est utilisée :


```js
const num = 54;
console.log(num.toString())
// "54"
```

Mais il y a plus à cela. La méthode `toString` pour les nombres accepte également un argument `base`. Cet argument vous permet de convertir un nombre dans une autre base.

La valeur retournée est la représentation sous forme de chaîne du nouveau nombre. Voici comment elle est utilisée :

```js
const num = 54;
const num2 = num.toString(2);
console.log(num2);
// "110110"
```

`parseInt` est une autre méthode JavaScript qui, au contraire, convertit les chaînes de caractères en leurs représentations numériques respectives. Voici comment elle fonctionne :

```js
const numInStr = "54";
const str = "Hello";
console.log(parseInt(numInStr));
// 54
console.log(parseInt(str));
// NaN
```

Pour une variable qui ne ressemble pas à un nombre, `parseInt` retourne `Nan` comme on peut le voir ci-dessus.


## Comment convertir un tableau en chaîne de caractères en JavaScript

Les tableaux ont également la méthode `toString`. La valeur retournée par cette méthode est une concaténation de toutes les valeurs du tableau (et des tableaux profondément imbriqués) séparées par des virgules. Voici comment elle est utilisée :

```js
const arr = ["javascript", "toString", [1, "deep1", [3, 4, "array"]]];
console.log(arr.toString());
// "javascript,toString,1,deep1,3,4,array"
```

## Comment convertir un objet en chaîne de caractères en JavaScript

La valeur de retour de `toString` sur un objet est - comme vous avez souvent pu le constater - `"[object Object]"`. Par exemple :

```js
const obj = {name: 'Object'};
const obj2 = {type: 'data', number: 100};
console.log(obj.toString());
// [object Object]
console.log(obj2.toString());
// [object Object]
```

La conversion par défaut des objets en chaîne est `[object Object]`. Remarquez qu'il y a deux `object` là, et pas seulement un ? Et l'autre est en majuscule ?

Il existe d'autres représentations pour les objets comme ce qui suit :

```js
function print() {};
const arr = [];
const obj = {};
console.log(
  Object.prototype.toString.call(print),
  Object.prototype.toString.call(arr),
  Object.prototype.toString.call(obj)
)
// [object Function] [object Array] [object Object]
```

Les fonctions, les tableaux, les objets, et même les dates et les expressions régulières sont tous des objets. Et chacun d'eux a la méthode `toString`.

Lorsque `toString` est appelé sur eux, il récupère la classe d'objet de la valeur, puis l'imprime comme vous le voyez ci-dessus ("Function, Array, Object).

Nous utilisons `call(variable)` parce que `toString` obtient la classe de l'objet via la propriété `this`.


## Conclusion

La méthode `.toString` retourne une conversion en chaîne de caractères des données sur lesquelles elle est utilisée. Cela est très utile pour certains cas, surtout pour les `number`s.

Dans cet article, nous avons appris comment la méthode JavaScript `toString` fonctionne avec les `number`s, les `array`s et les `object`s, et nous avons également jeté un coup d'œil à `parseInt`.