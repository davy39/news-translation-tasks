---
title: Comment implémenter map, filter et reduce avec la récursivité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-30T16:20:44.000Z'
originalURL: https://freecodecamp.org/news/implement-array-map-with-recursion-35976d0325b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YMYCdveLRLC9SI3ZYg8dBA.jpeg
tags:
- name: ES6
  slug: es6
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment implémenter map, filter et reduce avec la récursivité
seo_desc: 'By Yazeed Bzadough

  Array.map

  We all probably know Array.map. It transforms an array of elements according to
  a given function.

  double = (x) => x * 2;

  map(double, [1, 2, 3]);

  // [2, 4, 6]


  I’ve always seen it implemented along these lines:

  map = (fn, ...'
---

Par Yazeed Bzadough

### Array.map

Nous connaissons tous probablement `Array.map`. Il transforme un tableau d'éléments selon une fonction donnée.

```js
double = (x) => x * 2;
map(double, [1, 2, 3]);
// [2, 4, 6]
```

J'ai toujours vu son implémentation selon ces lignes :

```js
map = (fn, arr) => {
  const mappedArr = [];

  for (let i = 0; i < arr.length; i++) {
    let mapped = fn(arr[i]);

    mappedArr.push(mapped);
  }

  return mappedArr;
};
```

[Cette vidéo](https://youtu.be/XcS-LdEBUkE?t=4m16s) m'a exposé à une implémentation alternative de `Array.map`. Elle date d'un JSConf de 2014, bien avant que je ne monte dans le wagon de la programmation fonctionnelle.

**Édition :** [David Cizek](https://medium.com/@dadc) et [Stephen Blackstone](https://medium.com/@steveb3210) ont gentiment souligné des cas limites et des performances sous-optimales concernant cette implémentation de `map`. Je ne conseillerais à personne de l'utiliser dans une vraie application. Mon intention est que nous apprécions et apprenions de cette approche récursive et provocante. ?

L'exemple original est en CoffeeScript, voici un équivalent en JavaScript.

```js
map = (fn, [head, ...tail]) =>
  head === undefined ? [] : [fn(head), ...map(fn, tail)];
```

Vous pourriez utiliser l'implémentation plus sûre de [David Cizek](https://medium.com/@dadc) à la place.

```js
map = (_fn_, [_head_, ..._tail_]) _=>_ (
  head === undefined && tail.length < 1
    ? []
    : [fn(head), ...map(fn, tail)]
);
```

En utilisant [l'affectation par décomposition de ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment), nous stockons le premier élément du tableau dans la variable `head`. Ensuite, nous stockons _tous les autres_ éléments du tableau dans `tail`.

Si `head` est `undefined`, cela signifie que nous avons un tableau vide, donc nous retournons simplement un tableau vide. Nous n'avons _mappé_ rien.

```js
map(double, []);
// []
```

Si `head` _n'est pas_ `undefined`, nous retournons un nouveau tableau avec `fn(head)` comme premier élément. Nous avons maintenant _mappé_ le premier élément du tableau. À côté se trouve `map(fn, tail)` qui appelle à nouveau `map`, cette fois avec un élément de moins.

Puisque `map` retourne un tableau, nous utilisons la [syntaxe de décomposition de ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) pour le concaténer avec `[head]`.

Suivons cela pas à pas dans le débogueur. Collez ceci dans la console JavaScript de votre navigateur.

```js
map = (fn, [head, ...tail]) => {
  if (head === undefined) {
    return [];
  }

  debugger;

  return [fn(head), ...map(fn, tail)];
};
```

Maintenant, faisons `map(double, [1, 2, 3])`.

![](https://cdn-media-1.freecodecamp.org/images/1*YB8D4_0XaIAGze7CKffX6A.png)

Nous voyons nos variables locales :

```
head: 1
tail: [2, 3]
fn: double
```

Nous savons que `fn(head)` est `2`. Cela devient le premier élément du nouveau tableau. Ensuite, nous appelons à nouveau `map` avec `fn` et le reste des éléments du tableau : `tail`.

Ainsi, avant même que l'appel initial de `map` ne retourne, nous continuerons à appeler `map` jusqu'à ce que le tableau soit vidé. Une fois le tableau vide, `head` sera `undefined`, permettant à notre cas de base de s'exécuter et de terminer tout le processus.

![](https://cdn-media-1.freecodecamp.org/images/1*dowa0N9An5o2V0quqD72nA.png)

Lors de l'exécution suivante, `head` est `2` et `tail` est `[3]`.

Puisque `tail` n'est pas encore vide, atteignez le prochain point d'arrêt pour appeler à nouveau `map`.

![](https://cdn-media-1.freecodecamp.org/images/1*IMm0-zX10Zs5GGqu9Yl1ow.png)

`head` est `3`, et `tail` est un tableau vide. La prochaine fois que cette fonction s'exécute, elle abandonnera à la ligne 3 et retournera enfin le tableau mappé.

Et voici notre résultat final :

![](https://cdn-media-1.freecodecamp.org/images/1*m9PXMrrg9x9v013-Rl-UkQ.png)

### Array.filter

`Array.filter` retourne un nouveau tableau basé sur les éléments qui satisfont une fonction prédicat donnée.

```js
isEven = (x) => x % 2 === 0;
filter(isEven, [1, 2, 3]);
// [2]
```

Considérez cette solution récursive :

```js
filter = (pred, [head, ...tail]) =>
  head === undefined
    ? []
    : pred(head)
    ? [head, ...filter(pred, tail)]
    : [...filter(pred, tail)];
```

Si `map` avait du sens, cela sera facile.

Nous capturons toujours le premier élément du tableau dans une variable appelée `head`, et le reste dans un tableau séparé appelé `tail`.

Et avec le même cas de base, si `head` est `undefined`, retourne un tableau vide et termine l'itération.

Mais nous avons une autre instruction conditionnelle : ne placez `head` dans le nouveau tableau que si `pred(head)` est `true`, car `filter` fonctionne en testant chaque élément contre une fonction prédicat. Ce n'est que lorsque le prédicat retourne `true` que nous ajoutons cet élément au nouveau tableau.

Si `pred(head)` ne retourne pas `true`, appelez simplement `filter(pred, tail)` sans `head`.

Développons rapidement et suivons cela dans la console Chrome.

```js
filter = (pred, [head, ...tail]) => {
  if (head === undefined) return [];

  if (pred(head)) {
    debugger;

    return [head, ...filter(pred, tail)];
  }

  debugger;

  return [...filter(pred, tail)];
};
```

Et cherchons des nombres ≤ 10 :

<pre name="2060" id="2060" class="graf graf--pre graf-after--p">filter(x => x <= 10, [1, 10, 20]);</pre>

![](https://cdn-media-1.freecodecamp.org/images/1*hGkyWV3T_hDb1Hnav_lmAg.png)

Puisque notre tableau est `[1, 10, 20]`, `head` est le premier élément, 1, et `tail` est un tableau du reste : `[10, 20]`.

Le prédicat teste si `x` ≤ 10, donc `pred(1)` retourne `true`. C'est pourquoi nous nous sommes arrêtés à l'instruction `debugger` de la ligne 4.

Puisque le `head` actuel a passé le test, il est autorisé à entrer dans notre tableau filtré. Mais nous n'avons pas terminé, donc nous appelons à nouveau `filter` avec le même prédicat, et maintenant `tail`.

Passez au prochain `debugger`.

![](https://cdn-media-1.freecodecamp.org/images/1*WESZIWb_dxhNNO-6-YJGuA.png)

Nous avons appelé `filter` avec `[10, 20]` donc `head` est maintenant 10, et `tail` est `[20]`. Alors, comment `tail` devient-il plus petit à chaque itération successive ?

Nous sommes à nouveau à l'instruction `debugger` de la ligne 4 parce que 10 ≤ 10. Passez au prochain point d'arrêt.

![](https://cdn-media-1.freecodecamp.org/images/1*1U9o0ejjyzTvfjeEypYIFA.png)

`head` est maintenant 20 et `tail` est vide.

Puisque 20 > 10, `pred(head)` retourne `false` et notre tableau filtré ne l'inclura pas. Nous appellerons `filter` une fois de plus sans `head`.

Cette prochaine fois, cependant, `filter` abandonnera à la ligne 2. [Décomposer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Array_destructuring) un tableau vide vous donne des variables `undefined`. Continuez au-delà de ce point d'arrêt pour obtenir votre valeur de retour.

![](https://cdn-media-1.freecodecamp.org/images/1*2BdKSxNZwaGJ9Sc1VAWjXA.png)

Cela me semble correct !

### Array.reduce

Dernier mais non des moindres, `Array.reduce` est idéal pour réduire un tableau à une seule valeur.

Voici mon implémentation naïve de `reduce` :

```js
reduce = (fn, acc, arr) => {
  for (let i = 0; i < arr.length; i++) {
    acc = fn(acc, arr[i]);
  }

  return acc;
};
```

Et nous pouvons l'utiliser comme ceci :

```js
add = (x, y) => x + y;
reduce(add, 0, [1, 2, 3]); // 6
```

Vous obtiendriez le même résultat avec cette implémentation récursive :

```js
reduce = (fn, acc, [head, ...tail]) =>
  head === undefined ? acc : reduce(fn, fn(acc, head), tail);
```

Je trouve celle-ci beaucoup plus facile à lire que les implémentations récursives de `map` et `filter`.

Suivons cela dans la console du navigateur. Voici une version développée avec des instructions `debugger` :

```js
reduce = (fn, acc, [head, ...tail]) => {
  if (head === undefined) {
    debugger;

    return acc;
  }

  debugger;

  return reduce(fn, fn(acc, head), tail);
};
```

Ensuite, nous appellerons cela dans la console :

```js
add = (x, y) => x + y;
reduce(add, 0, [1, 2, 3]);
```

![](https://cdn-media-1.freecodecamp.org/images/1*2oPtNloFlI-0OZ1B3IZENA.png)

#### Round 1

Nous voyons nos variables locales :

`acc` : notre valeur initiale de `0`

`fn` : notre fonction `add`

`head` : le premier élément du tableau, `1`

`tail` : les autres éléments du tableau regroupés dans un tableau _séparé_, `[2, 3]`

Puisque `head` n'est pas `undefined`, nous allons appeler récursivement `reduce`, **en passant ses paramètres requis** :

`fn` : Évidemment, la fonction `add` à nouveau ?

`acc` : Le résultat de l'appel de `fn(acc, head)`. Puisque `acc` est `0`, et `head` est `1`, `add(0, 1)` retourne `1`.

`tail` : Les éléments restants du tableau. En utilisant toujours tail, nous continuons à réduire le tableau jusqu'à ce qu'il ne reste plus rien !

Passez au prochain `debugger`.

#### Round 2

![](https://cdn-media-1.freecodecamp.org/images/1*jYaNr_L9nJYw7N2uMMFsbQ.png)

Variables locales :

`acc` : Maintenant, c'est `1`, parce que nous avons appelé `reduce` avec `fn(acc, head)`, qui était `add(0, 1)` à ce moment-là.

`fn` : Toujours `add` !

`head` : Vous souvenez-vous comment nous avons passé le `tail` précédent à `reduce` ? Maintenant, il a été décomposé, avec `head` représentant son premier élément, `2`.

`tail` : Il ne reste qu'un seul élément, donc `3` a été regroupé dans un tableau tout seul.

Nous savons que le prochain appel de `reduce` prendra une fonction, un accumulateur et un tableau. Nous pouvons évaluer le prochain ensemble de paramètres **en utilisant la console**.

![](https://cdn-media-1.freecodecamp.org/images/1*TVD3RgN7v4FW_j8mIogckQ.png)

Attendez-vous à ces valeurs au prochain point d'arrêt.

#### Round 3

![](https://cdn-media-1.freecodecamp.org/images/1*YjHE_30_rjv8s4__FNdy3g.png)

Nos variables locales sont comme prévu. `head` a un premier et seul élément qui est `3`.

Et notre tableau n'a plus qu'un seul élément, `tail` est vide ! Cela signifie que le prochain point d'arrêt sera le dernier.

Évaluons rapidement nos futures variables locales :

![](https://cdn-media-1.freecodecamp.org/images/1*agbXBbNDXSsqYRd6aYLD7w.png)

Passez au point d'arrêt final.

#### Round 4

![](https://cdn-media-1.freecodecamp.org/images/1*E0CAeH84AfH9JBdtposIBA.png)

Regardez, nous nous sommes arrêtés à la ligne 3 au lieu de la ligne 6 cette fois ! `head` est `undefined`, donc nous retournons le résultat final, `6` ! Il apparaîtra si vous passez au prochain point d'arrêt.

![](https://cdn-media-1.freecodecamp.org/images/1*VBzXT1FLhUP0_iRPJ_QTFQ.png)![](https://cdn-media-1.freecodecamp.org/images/1*ApR1Nzk791drSLLBzcq2Xw.png)

Cela me semble bon ! Merci beaucoup d'avoir lu cela.