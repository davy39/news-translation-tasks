---
title: Comment changer conditionnellement des valeurs avec when() en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-21T20:16:45.000Z'
originalURL: https://freecodecamp.org/news/30-seconds-of-code-conditionally-change-values-with-when-732b09e46334
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ye9GrpJqOsiaZPbMeZkpGQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment changer conditionnellement des valeurs avec when() en JavaScript
seo_desc: 'By Yazeed Bzadough

  30 Seconds of Code is a brilliant collection of JavaScript snippets, digestible
  in ≤ 30 seconds. Anyone looking to master JavaScript should go through the entire
  thing.

  Inspired by Ramda, I contributed when() to 30secondsofcode’s o...'
---

Par Yazeed Bzadough

30 Seconds of Code est une collection brillante de snippets JavaScript, digestibles en ≤ 30 secondes. **Toute personne cherchant à maîtriser JavaScript devrait parcourir l'ensemble.**

Inspiré par [Ramda](http://ramdajs.com/docs/#when), j'ai contribué `when()` au [dépôt GitHub officiel](https://github.com/Chalarangelo/30-seconds-of-code/pull/652) de 30secondsofcode. C'est l'une de mes fonctions préférées.

`when()` prend 3 paramètres :

1.  `pred` : Une fonction prédicat (doit retourner `true` ou `false`)
2.  `whenTrue` : Une fonction à exécuter si `pred` retourne `true`.
3.  Une valeur : `x`.

Voici l'implémentation la plus basique :

```js
when = (pred, whenTrue, x) => {
  if (pred(x)) {
    return whenTrue(x);
  } else {
    return x;
  }
};
```

Que vous pouvez raccourcir en :

```js
when = (pred, whenTrue, x) => (pred(x) ? whenTrue(x) : x);
```

Disons que nous voulons tripler les nombres pairs

```js
when((x) => x % 2 === 0, (x) => x * 3, 2);
// 6
```

Nous avons obtenu `6` parce que `2` est un nombre pair. Que se passe-t-il si nous passons `11` ?

```js
when((x) => x % 2 === 0, (x) => x * 3, 11);
// 11
```

### Un pas plus loin

`when` a actuellement besoin des 3 paramètres à la fois—que se passe-t-il si nous pouvons fournir seulement les deux premiers, et donner `x` plus tard ?

```js
when = (pred, whenTrue) => (x) => (pred(x) ? whenTrue(x) : x);
```

Cette version est celle que j'ai soumise à [30secondsofcode.org](https://30secondsofcode.org/function#when). Maintenant notre code est plus flexible.

```js
tripleEvenNums = when((x) => x % 2 === 0, (x) => x * 3);

tripleEvenNums(20); // 60
tripleEvenNums(21); // 21
tripleEvenNums(22); // 66
```

### Encore plus loin

Nous pouvons passer `x` plus tard parce que `when(pred, whenTrue)` retourne une fonction attendant `x`. Que se passe-t-il si nous curryons `when()` ?

Si vous êtes nouveau dans le currying, voir [mon article](https://medium.com/front-end-hacking/how-does-javascripts-curry-actually-work-8d5a6f891499) à ce sujet.

Une fonction curryfiée n'a pas besoin de tous ses paramètres à la fois. Vous pouvez en fournir certains et obtenir une fonction qui prend le reste, permettant des motifs puissants.

#### Un exemple idiot

Imaginons que nous avons deux listes de personnes, toutes deux contiennent un gars nommé `Bobo`.

`Bobo` veut un surnom pour chaque liste.

- Si nous trouvons `Bobo` dans la liste 1, changeons son nom en `B Money`.
- Si nous trouvons `Bobo` dans la liste 2, changeons son nom en `Bo-bob`.

Curryfier `when` nous permet d'écrire facilement une fonction pour chaque préoccupation.

Si vous suivez, voici une fonction `curry` de [30secondsofcode.org](https://30secondsofcode.org/function#curry).

```js
curry = (fn, arity = fn.length, ...args) =>
  arity <= args.length ? fn(...args) : curry.bind(null, fn, arity, ...args);
```

Nous aurons besoin d'un prédicat pour trouver `Bobo`.

```js
isBobo = (person) => person.name === 'Bobo';
```

Pour garder nos fonctions pures, nous aurons besoin d'un moyen de changer _immutablement_ le nom d'une personne.

```js
changeName = (newName, obj) => ({
  ...obj,
  name: newName
});
```

Curryfions-le également pour que nous puissions fournir seulement `newName`.

```js
changeName = curry((newName, obj) => ({
  ...obj,
  name: newName
}));
```

Voici nos listes.

```js
list1 = [
  {
    name: 'Bobo',
    id: 1,
    iq: 9001
  },
  {
    name: 'Jaime',
    id: 2,
    iq: 9000
  },
  {
    name: 'Derek',
    id: 3,
    iq: 8999
  }
];

list2 = [
  {
    name: 'Sam',
    id: 1,
    iq: 600
  },
  {
    name: 'Bobo',
    id: 2,
    iq: 9001
  },
  {
    name: 'Peter',
    id: 3,
    iq: 8
  }
];
```

Mappons sur `list1`.

```js
doIfBobo = when(isBobo);
renameToBMoney = changeName('B Money');

list1.map(doIfBobo(renameToBMoney));
```

Notre résultat :

```js
[
  {
    name: 'B Money',
    id: 1,
    iq: 9001
  },
  {
    name: 'Jaime',
    id: 2,
    iq: 9000
  },
  {
    name: 'Derek',
    id: 3,
    iq: 8999
  }
];
```

Grâce à `when`, nous n'avons changé que `Bobo` et ignoré tout le monde !

Maintenant, mappons sur `list2`.

```js
renameToBoBob = changeName('Bo-bob');

list2.map(doIfBobo(renameToBoBob));
```

```js
Notre résultat :

[{
  "name": "Sam",
  "id": 1,
  "iq": 600
},
 {
 "name": "Bo-bob",
   "id": 2,
   "iq": 9001
 },
 {
   "name": "Peter",
   "id": 3,
   "iq": 8
 }
];
```

Cela me semble bien ! Nous avons donné à `Bobo` ses surnoms sans affecter personne d'autre.

Si vous êtes intéressé, considérez ces liens :

- [Collection de 30secondsofcode.org](https://30secondsofcode.org/array)
- [Mon article sur le currying](https://medium.com/front-end-hacking/how-does-javascripts-curry-actually-work-8d5a6f891499)
- [Ramda](http://ramdajs.com/docs/)