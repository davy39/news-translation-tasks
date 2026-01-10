---
title: 'Prototype en JavaScript : c''est particulier, mais voici comment ça fonctionne'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-31T11:11:28.000Z'
originalURL: https://freecodecamp.org/news/prototype-in-js-busted-5547ec68872
coverImage: https://cdn-media-1.freecodecamp.org/images/1*prjnL1V1OgyVtYrhssOUSQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Prototype en JavaScript : c''est particulier, mais voici comment ça fonctionne'
seo_desc: 'By Pranav Jindal

  The following four lines are enough to confuse most JavaScript developers:

  Object instanceof Function//true

  Object instanceof Object//true

  Function instanceof Object//true

  Function instanceof Function//true

  Prototype in JavaScript is...'
---

Par Pranav Jindal

Les quatre lignes suivantes suffisent à confondre la plupart des développeurs JavaScript :

```
Object instanceof Function//true
```

```
Object instanceof Object//true
```

```
Function instanceof Object//true
```

```
Function instanceof Function//true
```

Le prototype en JavaScript est l'un des concepts les plus déroutants, mais vous ne pouvez pas l'éviter. Peu importe à quel point vous l'ignorez, vous rencontrerez l'énigme du prototype au cours de votre vie avec JavaScript.

Alors, affrontons-le de front.

En commençant par les bases, il existe les types de données suivants en JavaScript :

1. undefined
2. null
3. number
4. string
5. boolean
6. object

Les cinq premiers sont des types de données primitifs. Ceux-ci stockent une valeur de leur type, comme un booléen, et peuvent être vrai ou faux.

Le dernier « object » est un type de référence que nous pouvons décrire comme une collection de paires clé-valeur (mais c'est bien plus).

En JavaScript, de nouveaux objets sont créés en utilisant la **fonction constructeur Object** (ou la notation littérale d'objet `{}`) qui fournit des méthodes génériques comme `toString()` et `valueOf()`.

Les fonctions en JavaScript sont des objets spéciaux qui peuvent être « **appelées** ». Nous les créons en utilisant la **fonction constructeur Function** (ou la notation littérale de fonction). Le fait que ces **constructeurs** soient à la fois des objets et des fonctions m'a toujours confus, un peu comme l'énigme de la poule et de l'œuf confond tout le monde.

Avant de commencer avec les prototypes, je veux clarifier qu'il existe deux prototypes en JavaScript :

1. **prototype** : Il s'agit d'un objet spécial qui est assigné comme propriété de toute fonction que vous créez en JavaScript. Soyons clairs ici, il est déjà présent pour toute fonction que vous créez, mais pas obligatoire pour les fonctions internes fournies par JavaScript (et la fonction retournée par `bind`). Ce `prototype` est le même objet que celui pointé par le `[[Prototype]]` (voir ci-dessous) du nouvel objet créé à partir de cette fonction (en utilisant le mot-clé `new`).
2. **[[Prototype]]** : Il s'agit d'une propriété quelque peu cachée sur chaque objet à laquelle le contexte d'exécution accède si une propriété qui est lue sur l'objet n'est pas disponible. Cette propriété est simplement une référence au `prototype` de la fonction à partir de laquelle l'objet a été créé. Elle peut être accessible dans le script en utilisant un **getter-setter** spécial (sujet pour un autre jour) appelé `__proto__`. Il existe d'autres nouvelles façons d'accéder à ce prototype, mais pour des raisons de brièveté, je ferai référence à `**[[Prototype]]**` en utilisant `__proto__`.

```
var obj = {}var obj1 = new Object()
```

Les deux instructions ci-dessus sont des instructions équivalentes lorsqu'elles sont utilisées pour créer un nouvel objet, mais beaucoup de choses se passent lorsque nous exécutons l'une de ces instructions.

Lorsque je crée un nouvel objet, il est vide. En fait, il n'est pas vide car il est une instance du constructeur `Object`, et il obtient intrinsèquement une référence au `prototype` de `Object`, qui est pointé par le `__proto__` du nouvel objet créé.

![Image](https://cdn-media-1.freecodecamp.org/images/h04OjQTCA9CyQ5yXzbwg2-HYnz8RbCTUvtc6)

Si nous regardons le `prototype` de la fonction constructeur `Object`, il semble identique au `__proto__` de `obj`. En fait, ce sont deux pointeurs qui référencent le même objet.

![Image](https://cdn-media-1.freecodecamp.org/images/2hy0s7jdEw-W66w8dWxo-8Ck2nBIBMWixr9t)

```
obj.__proto__ === Object.prototype//true
```

Chaque `prototype` d'une fonction a une propriété intrinsèque appelée `constructor` qui est un pointeur vers la fonction elle-même. Dans le cas de la fonction `Object`, le `prototype` a un `constructor` qui pointe vers `Object`.

```
Object.prototype.constructor === Object//true
```

![Image](https://cdn-media-1.freecodecamp.org/images/rnUjw1hZdqdTpcSW2y3ZX8ptZ3OUcCzuaKbO)

Dans l'image ci-dessus, le côté gauche est la vue développée du constructeur `Object`. Vous devez vous demander ce que sont toutes ces autres fonctions au-dessus. Eh bien, les fonctions sont des **objets**, donc elles peuvent avoir des propriétés comme les autres objets.

Si vous regardez de près, `Object` (à gauche) lui-même a un `__proto__` ce qui signifie que `Object` doit avoir été créé à partir d'un autre constructeur qui a un `prototype`. Comme `Object` est un objet fonction, il doit avoir été créé en utilisant le constructeur `Function`.

![Image](https://cdn-media-1.freecodecamp.org/images/we607uLIJLuCdG4P0metYMcjf9PpNHvh22tm)

Le `__proto__` de `Object` semble identique au `prototype` de `Function`. Lorsque je vérifie l'égalité des deux, ils s'avèrent être les mêmes objets.

```
Object.__proto__ === Function.prototype//true
```

Si vous regardez de près, vous verrez que `Function` lui-même a un `__proto__` ce qui signifie que la fonction constructeur `Function` doit avoir été créée à partir d'une fonction constructeur qui a un `prototype`. Comme `Function` est lui-même une **fonction**, il doit avoir été créé en utilisant le constructeur `Function`, c'est-à-dire lui-même. Je sais que cela semble bizarre, mais lorsque vous le vérifiez, cela s'avère être vrai.

![Image](https://cdn-media-1.freecodecamp.org/images/gHONmm8YNyMAgQQYD3MQ88WsYsathI0Nr-cp8)

Le `__proto__` de `Function` et le `prototype` de `Function` sont en fait deux pointeurs qui référencent le même objet.

```
Function.prototype === Function.__proto__\\true
```

Comme mentionné précédemment, le `constructor` de tout `prototype` doit pointer vers la fonction qui possède ce `prototype`. Le `constructor` du `prototype` de `Function` pointe vers `Function` lui-même.

```
Function.prototype.constructor === Function\\true
```

![Image](https://cdn-media-1.freecodecamp.org/images/ftvp4bDag11U4kaWjV3nG7UfkqQKjSQPA4i0)

Encore une fois, le `**prototype**` de `**Function**` a un `__proto__`. Eh bien, ce n'est pas une surprise... `prototype` est un objet, il peut en avoir un. Mais remarquez également qu'il pointe vers le `prototype` de `Object`.

```
Function.prototype.__proto__ == Object.prototype\\true
```

Nous pouvons donc avoir une carte principale ici :

![Image](https://cdn-media-1.freecodecamp.org/images/F86Ee6hanmaQuvSRBZ8S1rG6Cq1R-LVhA4Kl)

```
Opérateur instanceofa instanceof b
```

L'opérateur `instanceof` recherche l'objet `b` pointé par l'un des `constructor`(s) de la chaîne `__proto__` sur `a`. Relisez cela ! S'il trouve une telle référence, il retourne `true`, sinon `false`.

Nous revenons maintenant à nos quatre premières instructions `instanceof`. J'ai écrit les instructions correspondantes qui font que `instanceof` retourne `true` pour les suivantes :

```
Object instanceof FunctionObject.__proto__.constructor === Function
```

```
Object instanceof ObjectObject.__proto__.__proto__.constructor === Object
```

```
Function instanceof FunctionFunction.__proto__.constructor === Function
```

```
Function instanceof ObjectFunction.__proto__.__proto__.constructor === Object
```

Ouf !! Même les spaghettis sont moins emmêlés, mais j'espère que les choses sont plus claires maintenant.

Ici, j'ai quelque chose que je n'ai pas mentionné plus tôt : le `prototype` de `Object` n'a pas de `__proto__`.

En fait, il a un `__proto__` mais celui-ci est égal à `**null**`. La chaîne devait se terminer quelque part et elle se termine ici.

```
Object.prototype.__proto__\\null
```

Notre `Object`, `Function`, `Object.prototype` et `Function.prototype` ont également des propriétés qui sont des fonctions, comme `Object.assign`, `Object.prototype.hasOwnProperty` et `Function.prototype.call`. Ce sont des fonctions internes qui n'ont pas de `prototype` et sont également des instances de `Function` et ont un `__proto__` qui est un pointeur vers `Function.prototype`.

![Image](https://cdn-media-1.freecodecamp.org/images/fs6Q6b4ewNiWTuSehUQAY1Cf2OJTV0WyzHAB)

```
Object.create.__proto__ === Function.prototype\\true
```

Vous pouvez explorer d'autres fonctions constructeurs comme `Array` et `Date`, ou prendre leurs objets et rechercher le `prototype` et `__proto__`. Je suis sûr que vous serez en mesure de comprendre comment tout est connecté.

#### Questions supplémentaires :

Il y a une autre question qui m'a tracassé pendant un moment : Pourquoi le `prototype` de `Object` est-il un **objet** et le `prototype` de `Function` est-il un **objet fonction** ?

[**Ici**](https://stackoverflow.com/a/32929083/1934798) se trouve une bonne explication si vous pensiez la même chose.

Une autre question qui pourrait être un mystère pour vous jusqu'à présent est : Comment les types de données primitifs obtiennent-ils des fonctions comme `toString()`, `substr()` et `toFixed()` ? Cela est bien expliqué [**ici**](https://javascript.info/native-prototypes#primitives).

En utilisant `prototype`, nous pouvons faire fonctionner l'héritage avec nos objets personnalisés en JavaScript. Mais c'est un sujet pour un autre jour.

Merci d'avoir lu !