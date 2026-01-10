---
title: '30 Seconds of Code : Comment renommer plusieurs clés d''objet en JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-13T11:55:29.000Z'
originalURL: https://freecodecamp.org/news/30-seconds-of-code-rename-many-object-keys-in-javascript-268f279c7bfa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qlRItHMmEVJGSEDRYJbGLA.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: immutability
  slug: immutability
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: '30 Seconds of Code : Comment renommer plusieurs clés d''objet en JavaScript'
seo_desc: 'By Yazeed Bzadough

  30 Seconds of Code is a brilliant collection of JavaScript snippets, digestible
  in ≤ 30 seconds. Anyone looking to master JavaScript should go through the entire
  thing.

  The list didn’t contain a function to rename multiple object k...'
---

Par Yazeed Bzadough

30 Seconds of Code est une collection brillante de snippets JavaScript, digestibles en ≤ 30 secondes. **Toute personne cherchant à maîtriser JavaScript devrait parcourir l'ensemble.**

La liste ne contenait pas de fonction pour renommer plusieurs clés d'objet, cependant, j'ai donc créé une [pull request](https://github.com/Chalarangelo/30-seconds-of-code/pull/646) qui a été fusionnée avec succès !

Voici l'entrée officielle : [https://30secondsofcode.org/object#renamekeys](https://30secondsofcode.org/object#renamekeys)

J'ai précédemment écrit sur le [renommage des clés d'objet](https://medium.com/front-end-hacking/immutably-rename-object-keys-in-javascript-5f6353c7b6dd), mais nous ne changions qu'une clé à la fois.

Ensuite, [Adam Rowe](https://medium.com/@adaminsley) a gentiment commenté, demandant comment nous pourrions renommer _plusieurs_ clés d'objet. J'ai répondu avec cet exemple de code après quelques réflexions et recherches.

```js
renameKeys = (keysMap, obj) =>
  Object.keys(obj).reduce(
    (acc, key) => ({
      ...acc,
      ...{ [keysMap[key] || key]: obj[key] }
    }),
    {}
  );
```

Cela a été inspiré par la fonction `renameKeys` de [Ramda Adjunct](https://char0n.github.io/ramda-adjunct/2.6.0/RA.html#.renameKeys).

- `keysMap` contient des paires clé/valeur de vos anciennes/nouvelles clés d'objet.
- `obj` est l'objet à modifier.

Vous pourriez l'utiliser comme ceci :

```js
keysMap = {
  name: 'firstName',
  job: 'passion'
};

obj = {
  name: 'Bobo',
  job: 'Front-End Master'
};

renameKeys(keysMap, obj);
// { firstName: 'Bobo', passion: 'Front-End Master' }
```

Décortiquons cela ! Nous pouvons écrire une version étendue, conviviale pour le `debugger`, de cette fonction :

```js
renameKeys = (keysMap, obj) => {
  debugger;

  return Object.keys(obj).reduce((acc, key) => {
    debugger;

    const renamedObject = {
      [keysMap[key] || key]: obj[key]
    };

    debugger;

    return {
      ...acc,
      ...renamedObject
    };
  }, {});
};
```

Et nous l'utiliserons comme ceci :

```js
renameKeys(
  {
    name: 'firstName',
    job: 'passion'
  },
  {
    name: 'Bobo',
    job: 'Front-End Master'
  }
);
```

![](https://cdn-media-1.freecodecamp.org/images/1*C9BI6jfACst-UcchX6wyyA.png)

En pause à la ligne 2, nous voyons que `keysMap` et `obj` ont été correctement assignés.

C'est ici que le plaisir commence. Passez au `debugger` suivant.

![](https://cdn-media-1.freecodecamp.org/images/1*3HKJjlIj8tChHNlre9WV9Q.png)

Inspectez nos variables locales à la ligne 7 :

- `acc: {}` car c'est la valeur initiale de `Array.reduce()` (ligne 19).
- `key: "name"` car c'est la première clé de `Object.keys(obj)`.
- `renamedObject: undefined`

Remarquez également que nous pouvons accéder à `keysMap` et `obj` depuis la portée de la fonction parente.

Devinez ce que sera `renamedObject`. Comme dans mon [article mentionné précédemment](https://medium.com/front-end-hacking/immutably-rename-object-keys-in-javascript-5f6353c7b6dd), nous utilisons les [_computed property names_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer) pour assigner dynamiquement la clé de `renamedObject`.

Si `keysMap[key]` existe, utilisez-le. Sinon, utilisez la clé d'objet originale. Dans ce cas, `keysMap[key]` est "firstName".

![](https://cdn-media-1.freecodecamp.org/images/1*aYI7ss4IOWIipNsC40r9rg.png)

C'est la clé de `renamedObject`, qu'en est-il de sa valeur correspondante ?

![](https://cdn-media-1.freecodecamp.org/images/1*GEBIVtNMWIuosMVq4FLMQw.png)

C'est `obj[key]` : "Bobo". Atteignez le `debugger` suivant et vérifiez-le.

![](https://cdn-media-1.freecodecamp.org/images/1*XMGM2FxuNscmq_imZf8Nmw.png)

`renamedObject` est maintenant `{ firstName: "Bobo" }`.

![](https://cdn-media-1.freecodecamp.org/images/1*z8HEVhgr8-e5HFrtAK5lzg.png)

Maintenant, en utilisant l'opérateur _spread_, nous allons fusionner `acc` et `renamedObject`. Rappelez-vous que `acc` est actuellement la valeur initiale de `.reduce` : un objet vide.

Ainsi, la fusion de `acc` et `renamedObject` donne simplement un clone de `renamedObject`.

![](https://cdn-media-1.freecodecamp.org/images/1*Fw0QyV7VsU2UH-GtD-74WQ.png)

Puisque nous retournons cet objet, cependant, il devient `acc` dans l'itération suivante de `.reduce`. Passez au `debugger` suivant pour voir cela.

![](https://cdn-media-1.freecodecamp.org/images/1*h0Lxhtw1trErPruUBKamfA.png)

Nous sommes à nouveau dans `.reduce`, car il y a une autre `key` à traiter. Nous voyons que `acc` est maintenant `{ firstName: "Bobo" }`.

Le même processus s'exécute à nouveau, et `renamedObject` est correctement créé.

![](https://cdn-media-1.freecodecamp.org/images/1*OfKamMrGJLBIvY2WgQrlaA.png)

Cette fois, la fusion de `acc` et `renamedObject` fait réellement une différence.

![](https://cdn-media-1.freecodecamp.org/images/1*uMdN7mSsIhgvzJCceftUOw.png)

Passez ce `debugger` pour retourner cet objet, et vous avez terminé !

Voici le résultat final :

![](https://cdn-media-1.freecodecamp.org/images/1*TpcJHEG6MUxazCkNnCg6AQ.png)

Amusez-vous à renommer **toutes les clés**, jusqu'à la prochaine fois !