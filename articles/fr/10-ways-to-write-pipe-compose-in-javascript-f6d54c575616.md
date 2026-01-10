---
title: Mes façons préférées d'écrire pipe et compose en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-16T16:41:19.000Z'
originalURL: https://freecodecamp.org/news/10-ways-to-write-pipe-compose-in-javascript-f6d54c575616
coverImage: https://cdn-media-1.freecodecamp.org/images/1*I2oy7YWlgX6Ej9uGSOGD7Q.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Mes façons préférées d'écrire pipe et compose en JavaScript
seo_desc: 'By Yazeed Bzadough

  compose, and especially pipe, are easily among my favorite functions.

  This article’s just to have fun and explore different implementations of these two
  gems. I recommend you understand what they do before reading this; perhaps che...'
---

Par Yazeed Bzadough

`compose`, et surtout `pipe`, font facilement partie de mes fonctions préférées.

Cet article est juste pour s'amuser et explorer différentes implémentations de ces deux pépites. Je vous recommande de comprendre ce qu'elles font avant de lire ceci ; peut-être consulter [mon analyse approfondie ici](https://medium.com/front-end-hacking/pipe-and-compose-in-javascript-5b04004ac937).

```js
pipe = (...fns) => (x) => fns.reduce((v, f) => f(v), x);
```

Classique.

En commençant par la fonction la plus à gauche, réduisez un tableau de fonctions à une seule valeur en appelant la fonction suivante avec la sortie de la précédente.

```js
double = (x) => x * 2;
add1 = (x) => x + 1;

pipe(
  double,
  add1
)(100); // 201
```

J'ai découvert cette implémentation grâce à [Eric Elliott](https://medium.com/@_ericelliott), et j'ai écrit une analyse approfondie à ce sujet [ici](https://medium.com/front-end-hacking/pipe-and-compose-in-javascript-5b04004ac937).

Utilisez `reduceRight` pour implémenter `compose`. Maintenant, vos fonctions sont appelées de droite à gauche.

```js
compose = (...fns) => (x) => fns.reduceRight((v, f) => f(v), x);

compose(
  double,
  add1
)(100);
// 202
```

Vous pourriez aussi inverser `fns` et continuer à utiliser `reduce` (moins performant).

```js
compose = (...fns) => (x) => fns.reverse().reduce((v, f) => f(v), x);

compose(
  double,
  add1
)(100); // 202
```

`reverse` mute le tableau, donc vous pourriez d'abord le copier (encore moins performant).

```js
compose = (...fns) => (x) => [...fns].reverse().reduce((v, f) => f(v), x);

compose(
  double,
  add1
)(100); // 202
```

Utilisez `reduceRight` pour revenir à `pipe`.

```js
pipe = (...fns) => (x) => [...fns].reverse().reduceRight((v, f) => f(v), x);

pipe(
  double,
  add1
)(100); // 201
```

### Mais Elles Sont Toutes Unary

Tous les extraits ci-dessus, d'ailleurs, sont _unary_. Chaque fonction ne peut accepter qu'_un seul argument_.

Si votre pipeline's première fonction doit être _nAry_ (acceptant `n` arguments), essayez cette implémentation :

```js
multiply = (x, y) => x * y;
pipe = (...fns) => fns.reduce((f, g) => (...args) => g(f(...args)));

pipe(
  multiply,
  add1
)(10, 10); // 101
// Accepte plusieurs args maintenant
```

Cet extrait provient de [30secondsofcode.org](https://30secondsofcode.org/adapter#pipefunctions). Votre première fonction (la plus à gauche) peut accepter `n` arguments, toutes les autres doivent être unary.

Encore une fois, `reduceRight` nous donne `compose`. Maintenant, votre fonction la plus à droite peut accepter `n` arguments. Déplaçons `multiply` à la fin de la chaîne.

```js
compose = (...fns) => fns.reduceRight((f, g) => (...args) => g(f(...args)));

compose(
  add1,
  multiply
)(10, 10); // 101
// Accepte plusieurs args maintenant
// Mettre multiply en premier
```

Comme avant, vous pourriez inverser le tableau `fns` et continuer à utiliser `reduce` :

```js
compose = (...fns) =>
  [...fns].reverse().reduce((f, g) => (...args) => g(f(...args)));

compose(
  add1,
  multiply
)(10, 10); // 101
```

Si vous voulez garder `reduce` sans le léger impact sur les performances, échangez simplement `g` et `f` :

```js
compose = (...fns) => fns.reduce((f, g) => (...args) => f(g(...args)));

compose(
  add1,
  multiply
)(10, 10); // 101
```

Et utilisez `reduceRight` pour revenir à `pipe`.

```js
pipe = (...fns) => fns.reduceRight((f, g) => (...args) => f(g(...args)));

pipe(
  multiply,
  add1
)(10, 10); // 101
// mettre multiply en premier maintenant
```

### Conclusion

Ouf ! C'est beaucoup de façons de pipe et compose !

Cela prouve simplement que, peu importe quoi, vous _devez boucler sur un tableau de fonctions, appelant la suivante avec le résultat de la précédente_.

Peu importe si vous utilisez `reduce`, `reduceRight`, changez l'ordre d'invocation, ou autre chose.

> Si vous voulez `pipe()`, allez de gauche à droite. Vous voulez compose() ? Allez de droite à gauche.

Simple et clair. À la prochaine !