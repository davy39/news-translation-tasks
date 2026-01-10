---
title: Une introduction rapide aux fonctions d'ordre supérieur en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-11T21:44:21.000Z'
originalURL: https://freecodecamp.org/news/a-quick-intro-to-higher-order-functions-in-javascript-1a014f89c6b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JyhQls2zLuu22yrnsk6mcA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction rapide aux fonctions d'ordre supérieur en JavaScript
seo_desc: 'By Yazeed Bzadough

  Higher-Order Functions

  A function that accepts and/or returns another function is called a higher-order
  function.

  It’s higher-order because instead of strings, numbers, or booleans, it goes higher
  to operate on functions. Pretty me...'
---

Par Yazeed Bzadough

### Fonctions d'ordre supérieur

Une fonction qui accepte et/ou retourne une autre fonction est appelée une **fonction d'ordre supérieur**.

Elle est _d'ordre supérieur_ car au lieu de manipuler des chaînes de caractères, des nombres ou des booléens, elle va _plus haut_ pour opérer sur des fonctions. Assez méta.

Avec les fonctions en JavaScript, vous pouvez

- Les stocker comme variables
- Les utiliser dans des tableaux
- Les assigner comme propriétés d'objets (méthodes)
- Les passer comme arguments
- Les retourner depuis d'autres fonctions

_Comme n'importe quelle autre donnée_. C'est la clé ici.

### Les fonctions opèrent sur les données

#### Les chaînes de caractères sont des données

```js
sayHi = (name) => `Bonjour, ${name}!`;
result = sayHi('Utilisateur');

console.log(result); // 'Bonjour, Utilisateur!'
```

#### Les nombres sont des données

```js
double = (x) => x * 2;
result = double(4);

console.log(result); // 8
```

#### Les booléens sont des données

```js
getClearance = (allowed) => (allowed ? 'Accès accordé' : 'Accès refusé');

result1 = getClearance(true);
result2 = getClearance(false);

console.log(result1); // 'Accès accordé'
console.log(result2); // 'Accès refusé'
```

#### Les objets sont des données

```js
getFirstName = (obj) => obj.firstName;

result = getFirstName({
  firstName: 'Yazeed'
});

console.log(result); // 'Yazeed'
```

#### Les tableaux sont des données

```js
len = (array) => array.length;
result = len([1, 2, 3]);

console.log(result); // 3
```

Ces 5 types sont des [citoyens de première classe](https://en.wikipedia.org/wiki/First-class_citizen) dans chaque langage grand public.

Qu'est-ce qui les rend de première classe ? Vous pouvez les passer, les stocker dans des variables et des tableaux, les utiliser comme entrées pour des calculs. Vous pouvez les utiliser comme _n'importe quelle donnée_.

### Les fonctions peuvent aussi être des données

![](https://cdn-media-1.freecodecamp.org/images/0*wy_bAnMM-coF9cep.png)

#### Fonctions comme arguments

```js
isEven = (num) => num % 2 === 0;
result = [1, 2, 3, 4].filter(isEven);

console.log(result); // [2, 4]
```

Voyez comment `filter` utilise `isEven` pour décider quels nombres garder ? `isEven`, _une fonction_, était un paramètre _pour une autre fonction_.

Elle est appelée par `filter` pour chaque nombre, et utilise la valeur retournée `true` ou `false` pour déterminer si un nombre doit être gardé ou rejeté.

#### Retourner des fonctions

```js
add = (x) => (y) => x + y;
```

`add` nécessite deux paramètres, mais pas tous en même temps. C'est une fonction demandant seulement `x`, qui retourne une fonction demandant seulement `y`.

Encore une fois, cela n'est possible que parce que JavaScript permet aux fonctions d'être une valeur de retour — tout comme les chaînes de caractères, les nombres, les booléens, etc.

Vous pouvez toujours fournir `x` et `y` immédiatement, si vous le souhaitez, avec une double invocation

```js
result = add(10)(20);
```

```js
console.log(result); // 30
```

Ou `x` maintenant et `y` plus tard :

```js
add10 = add(10);
result = add10(20);

console.log(result); // 30
```

Revenons à cet exemple. `add10` est le résultat de l'appel de `add` avec un paramètre. Essayez de le logger dans la console.

![](https://cdn-media-1.freecodecamp.org/images/1*BaPwZXD00kXBtTy7QV_tzA.png)

`add10` est une fonction qui prend un `y` et retourne `x + y`. Après avoir fourni `y`, elle se dépêche de calculer et de retourner votre résultat final.

![](https://cdn-media-1.freecodecamp.org/images/1*kg9Sv6gQExV_llaE3GUI-g.png)

### Une meilleure réutilisabilité

Probablement le plus grand avantage des fonctions d'ordre supérieur est une meilleure réutilisabilité. Sans elles, les méthodes principales de tableaux de JavaScript — `map`, `filter`, et `reduce` — n'existeraient pas !

Voici une liste d'utilisateurs. Nous allons faire quelques calculs avec leurs informations.

```js
users = [
  {
    name: 'Yazeed',
    age: 25
  },
  {
    name: 'Sam',
    age: 30
  },
  {
    name: 'Bill',
    age: 20
  }
];
```

#### Map

Sans fonctions d'ordre supérieur, nous aurions toujours besoin de boucles pour imiter la fonctionnalité de `map`.

```js
getName = (user) => user.name;
usernames = [];

for (let i = 0; i < users.length; i++) {
  const name = getName(users[i]);

  usernames.push(name);
}

console.log(usernames);
// ["Yazeed", "Sam", "Bill"]
```

Ou nous pourrions faire ceci !

```js
usernames = users.map(getName);

console.log(usernames);
// ["Yazeed", "Sam", "Bill"]
```

#### Filter

Dans un monde sans fonctions d'ordre supérieur, nous aurions encore besoin de boucles pour recréer la fonctionnalité de `filter` aussi.

```js
startsWithB = (string) => string.toLowerCase().startsWith('b');

namesStartingWithB = [];

for (let i = 0; i < users.length; i++) {
  if (startsWithB(users[i].name)) {
    namesStartingWithB.push(users[i]);
  }
}

console.log(namesStartingWithB);
// [{ "name": "Bill", "age": 20 }]
```

Ou nous pourrions faire ceci !

```js
namesStartingWithB = users.filter((user) => startsWithB(user.name));

console.log(namesStartingWithB);
// [{ "name": "Bill", "age": 20 }]
```

#### Reduce

Oui, reduce aussi… On ne peut pas faire grand-chose de cool sans fonctions d'ordre supérieur !! ?

```js
total = 0;

for (let i = 0; i < users.length; i++) {
  total += users[i].age;
}

console.log(total);
// 75
```

Comment ça ?

```js
totalAge = users.reduce((total, user) => user.age + total, 0);

console.log(totalAge);
// 75
```

### Résumé

- Les chaînes de caractères, les nombres, les booléens, les tableaux et les objets peuvent être stockés comme variables, tableaux, et propriétés ou méthodes.
- JavaScript traite les fonctions de la même manière.
- Cela permet des fonctions qui opèrent sur d'autres fonctions : **fonctions d'ordre supérieur**.
- Map, filter et reduce sont des exemples parfaits — et rendent les motifs courants comme la transformation, la recherche et la somme de listes beaucoup plus faciles !

[Je suis sur Twitter](https://twitter.com/yazeedBee) si vous souhaitez discuter. À la prochaine !

Prenez soin de vous, <br />
Yazeed Bzadough <br />
[yazeedb.com](http://yazeedb.com/)