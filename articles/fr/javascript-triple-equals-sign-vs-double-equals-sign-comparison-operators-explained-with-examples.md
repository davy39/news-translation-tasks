---
title: 'JavaScript : Triple signe égal VS Double signe égal – Opérateurs de comparaison
  expliqués avec des exemples'
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-03-12T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-triple-equals-sign-vs-double-equals-sign-comparison-operators-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c2d740569d1a4ca306d.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: 'JavaScript : Triple signe égal VS Double signe égal – Opérateurs de comparaison
  expliqués avec des exemples'
seo_desc: 'You may have seen double and triple equals signs in JavaScript. But what
  do they mean?

  Well in short: == inherently converts type and === does not convert type.

  Double Equals (==) checks for value equality only. It inherently does type coercion.
  This...'
---

Vous avez peut-être vu des doubles et triples signes égal en JavaScript. Mais que signifient-ils ?

En bref : `==` convertit implicitement le type et `===` ne convertit pas le type.

Le Double Égal (`==`) vérifie uniquement l'égalité des valeurs. Il effectue une coercition de type implicite. Cela signifie qu'avant de vérifier les valeurs, il convertit les types des variables pour qu'ils correspondent.

En revanche, le Triple Égal (`===`) ne effectue pas de coercition de type. Il vérifiera si les variables comparées ont à la fois la même valeur **ET** le même type.

D'accord - alors, comprenons mieux la différence à travers quelques exemples. Pour chacun d'eux, réfléchissez à ce que sera la sortie de ces instructions.

### Exemple 1 :

```js
const foo = "test"
const bar = "test"

console.log(foo == bar) //true
console.log(foo === bar) //true                            
```

La valeur et le type de `foo` et `bar` sont identiques. Par conséquent, le résultat est `true` pour les deux.

### Exemple 2 :

```js
const number = 1234
const stringNumber = '1234'

console.log(number == stringNumber) //true
console.log(number === stringNumber)  //false                                   

```

La valeur de `number` et `stringNumber` semble similaire ici. Cependant, le type de `number` est `Number` et le type de `stringNumber` est `string`. Même si les valeurs sont identiques, le type ne l'est pas. Par conséquent, une vérification `==` retourne `true`, mais lorsqu'on vérifie la valeur **et** le type, la valeur est `false`.

### Exemple 3 :

```js
console.log(0 == false) //true
console.log(0 === false) //false                  
```

Raison : même valeur, type différent. Coercition de type

C'est un cas intéressant. La valeur de `0` lorsqu'elle est vérifiée avec `false` est la même. C'est parce que `0` et `false` ont la même valeur pour JavaScript, mais lorsqu'on vérifie le type **et** la valeur, la valeur est false car `0` est un `number` et `false` est un `boolean`.

### Exemple 4 :

```
const str = ""

console.log(str == false) //true
console.log(str === false) //false
```

La valeur d'une chaîne vide et `false` est la même en JavaScript. Par conséquent, `==` retourne true. Cependant, le type est différent et donc `===` retourne false.

## Quand utiliser `==` et quand utiliser `===` ?

En cas de doute, utilisez `===`. Cela vous évitera un tas de bugs potentiels.

Si vous prenez en charge un cas d'utilisation où vous pouvez être un peu indulgent quant au type des données entrantes, alors utilisez `==`. Par exemple, si une API accepte à la fois `"true"` et `true` du client, utilisez `==`. En bref, n'utilisez pas `==` sauf si vous avez un cas d'utilisation solide pour cela.

Voici un tableau pratique de vérité JavaScript pour votre référence, et pour vous montrer à quel point l'égalité est compliquée en JavaScript :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-6.png)
_Source : [https://dorey.github.io/JavaScript-Equality-Table/](https://dorey.github.io/JavaScript-Equality-Table/)_

Si vous avez aimé cet article, n'oubliez pas de me suivre sur Twitter pour les mises à jour.

%[https://twitter.com/shrutikapoor08/status/1180173695643348992?s=20]