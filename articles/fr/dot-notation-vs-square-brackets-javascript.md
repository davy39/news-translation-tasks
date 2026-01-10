---
title: Notation par point vs notation par crochets pour les propriétés d'objet – Quelle
  est la différence ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-17T16:55:10.000Z'
originalURL: https://freecodecamp.org/news/dot-notation-vs-square-brackets-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/19.-dot-vs-bracket-notation.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Notation par point vs notation par crochets pour les propriétés d'objet
  – Quelle est la différence ?
seo_desc: "By Dillion Megida\nThere are multiple ways to access object properties\
  \ in JavaScript. But two common ones are dot notation and bracket notation. \nI'll\
  \ explain the difference between these two approaches in this article.\nWith dot\
  \ and bracket notation, ..."
---

Par Dillion Megida

Il existe plusieurs façons d'accéder aux propriétés d'un objet en JavaScript. Mais deux méthodes courantes sont la notation par point et la notation par crochets. 

Je vais expliquer la différence entre ces deux approches dans cet article.

Avec la notation par point et par crochets, vous pouvez :

* accéder à la valeur d'une propriété par sa clé
* modifier la valeur d'une propriété existante par sa clé et
* ajouter une nouvelle propriété à un objet

Mais ces deux méthodes accèdent aux propriétés différemment, et il existe différents scénarios où l'une est meilleure que l'autre.

## Accesseur de propriété par notation par point

L'approche par notation par point implique l'utilisation d'un point ou d'une période (`.`) et d'une clé pour accéder à une propriété. Voici la syntaxe :

```js
object.key
```

Vous avez le point puis la clé de la propriété à laquelle vous souhaitez accéder. Cette expression retournera la valeur de la propriété. Voyons un exemple :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const target = obj.name
// deeecode
```

En utilisant le point et la clé **name**, `.name`, nous obtenons "deeecode" qui est la valeur de la propriété name.

Vous pouvez également utiliser cette notation pour modifier une propriété existante :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

obj.age = 100

console.log(obj)
// {
//   name: "deeecode",
//   age: 100,
//   language: "javascript"
// }
```

Ici, nous modifions la propriété `age`.

De plus, vous pouvez ajouter une nouvelle propriété en utilisant cette approche :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

obj.location = "Mercury"

console.log(obj)
// {
//   name: "deeecode",
//   age: 80,
//   language: "javascript",
//   location: "Mercury"
// }
```

Ici, nous ajoutons la propriété `location`.

Mais cette approche a des limitations que nous examinerons bientôt. Ensuite, comprenons comment fonctionne l'approche par notation par crochets.

Voici une [version vidéo](https://youtu.be/AzVvBO65SMc) sur ce sujet si vous êtes intéressé.

## Accesseur de propriété par notation par crochets

L'approche par notation par crochets implique l'utilisation de crochets, dans lesquels vous avez une expression qui évalue une valeur. Cette valeur sert de clé pour accéder à la propriété. Voici la syntaxe :

```js
object[expression]
```

L'expression dans les crochets évalue une clé pour la propriété à laquelle vous souhaitez accéder, et cette expression retournera la valeur de la propriété. Voyons un exemple :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const target = obj["name"]
// deeecode
```

En utilisant des crochets et une expression de chaîne **"name"**, `["name"]`, nous obtenons "deeecode" qui est la valeur de la propriété name.

Vous pouvez également utiliser cette approche pour modifier une propriété existante :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

obj["age"] = 100

console.log(obj)
// {
//   name: "deeecode",
//   age: 100,
//   language: "javascript"
// }
```

Ici, nous modifions la propriété `age` en utilisant une expression de chaîne `"age"`.

Et, vous pouvez ajouter une nouvelle propriété en utilisant des crochets :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

obj["location"] = "Mercury"

console.log(obj)
// {
//   name: "deeecode",
//   age: 80,
//   language: "javascript",
//   location: "Mercury"
// }
```

Ici, nous ajoutons une nouvelle propriété `location` en utilisant une expression de chaîne `"location"`.

La notation par crochets a plus de capacités que la notation par point. Je vais expliquer.

## Différences entre la notation par point et la notation par crochets pour l'accès aux propriétés

La notation par point n'autorise que les clés statiques tandis que la notation par crochets accepte les clés dynamiques. Une clé statique signifie ici que la clé est tapée directement, tandis qu'une clé dynamique signifie ici que la clé est évaluée à partir d'une expression.

Regardons quelques exemples.

### Utilisation des deux approches pour accéder aux propriétés

Commençons par la notation par point :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "language"

const target = obj.myKey
// undefined
```

Ici, j'ai assigné la valeur "language" à une variable `myKey`. Ce que j'attendrais ici, c'est que lorsque j'utilise la notation par point, comme `obj.myKey`, "myKey" soit remplacé par "language". Donc cela se lirait comme `obj.language` et cela retournerait "javascript". 

Mais ce n'est pas ce qui se passe. Au lieu de cela, le résultat est `undefined`.

La raison en est que la notation par point n'accepte que les clés statiques. Donc lorsque vous faites `obj.myKey`, JavaScript cherche la propriété avec la clé `myKey` dans `obj`. Mais cette propriété n'existe pas, donc nous obtenons `undefined`.

La notation par crochets, en revanche, permet des clés dynamiques. Parce que cette notation accepte des expressions, vous pouvez utiliser n'importe quelle expression qui évalue une valeur. Cela pourrait être :

* `hello + Hi` qui évalue `helloHi` comme clé
* `returnKey()` qui évalue une valeur comme clé
* `isTrue ? "trueKey" : "falseKey"` qui évalue "trueKey" ou "falseKey" comme clé
* `variable` qui évalue la valeur de la variable comme clé

Par conséquent, en utilisant l'exemple précédent, nous pouvons avoir ceci :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "language"

const target = obj[myKey]
// javascript
```

L'expression que nous avons passée aux crochets est `myKey` qui est une variable. Cette expression évalue "language" qui est la valeur de la variable. En utilisant cette valeur, les crochets peuvent obtenir la valeur de la propriété, qui est "javascript".

Mais si vous passez une expression de chaîne comme `"myKey"`, vous obtenez `undefined` :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "language"

const target = obj["myKey"]
// undefined
```

Cela est dû au fait que l'expression de chaîne `"myKey"` évalue la valeur `"myKey"` qui sert de clé pour accéder à la propriété. Puisqu'il n'y a pas de clé `myKey` sur `obj`, la valeur retournée est `undefined`.

### Utilisation des deux approches pour modifier les propriétés

Commençons par la notation par point :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "age"

obj.myKey = 100

console.log(obj)
// {
//   name: "deeecode",
//   age: 80,
//   language: "javascript",
//   myKey: 100
// }
```

Ici, nous avons `myKey` avec la valeur "age". En tentant de faire `obj.myKey = 100` pour modifier la propriété `age`, cela ne fonctionnera pas. Cela est dû au fait que la notation par point accepte une clé statique. Donc `obj.myKey` prend `myKey` comme clé. Puisque `mykey` n'existe pas dans `obj`, cette instruction ajoute la clé. Ensuite, `obj` a une nouvelle clé, `myKey` avec la valeur `100`.

Le comportement est différent avec la notation par crochets :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "age"

obj[myKey] = 100

console.log(obj)
// {
//   name: "deeecode",
//   age: 100,
//   language: "javascript"
// }
```

Au lieu d'ajouter une nouvelle propriété `myKey` à `obj`, l'approche par crochets modifie la propriété `age`. La raison est que nous passons `myKey` comme une expression aux crochets. Cette expression, en tant que variable, évalue `"age"` qui est la valeur de la variable. En utilisant "age" comme clé, cette approche modifie la valeur de la propriété `age` à `100`.

Et si nous voulions ajouter une nouvelle propriété en utilisant des crochets, alors nous pouvons passer une expression qui retourne une nouvelle clé qui n'existe pas. Par exemple :

```js
const obj = {
  name: "deeecode",
  age: 80,
  language: "javascript",
}

const myKey = "location"

obj[myKey] = "Mercury"

console.log(obj)
// {
//   name: "deeecode",
//   age: 100,
//   language: "javascript",
//   location: "Mercury"
// }
```

Ici, la variable `myKey` contient une nouvelle valeur : `"location"`. En passant cela aux crochets, et en assignant une valeur de "Mercury", nous avons maintenant une nouvelle propriété avec une paire clé-valeur de `location` et "Mercury".

## Devriez-vous utiliser la notation par point ou par crochets ?

Jusqu'à présent, nous avons examiné comment chaque notation fonctionne, en utilisant différents exemples pour accéder/modifier des propriétés existantes et pour ajouter de nouvelles propriétés. Alors, laquelle devriez-vous utiliser lorsque vous écrivez du code JavaScript ?

Le principal facteur qui vous aidera à prendre votre décision est la clé de la propriété à laquelle vous souhaitez accéder. Si c'est une clé statique, utilisez la notation par point. Mais si c'est une clé dynamique (évaluée à partir d'une expression pendant l'exécution), utilisez la notation par crochets.

La notation par point est utile lorsque vous connaissez la propriété à l'avance. Vous faites simplement `object.key` pour lire/modifier une propriété existante ou pour ajouter une nouvelle propriété.

La notation par crochets est utile lorsque vous voulez [accéder dynamiquement à une propriété](https://freecodecamp.org/news/how-to-set-dynamic-object-properties-using-computed-property-names/). La clé de cette propriété pourrait provenir d'expressions comme `getKey()`, `"my" + "key"`, ou `keyVariable`.

J'espère que vous avez appris quelque chose de cet article. Veuillez partager si vous l'avez trouvé utile :)