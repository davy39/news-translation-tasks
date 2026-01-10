---
title: Apprendre Reduce en 10 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-15T11:59:00.000Z'
originalURL: https://freecodecamp.org/news/learn-reduce-in-10-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/cover-image.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Redux
  slug: redux
- name: technology
  slug: technology
seo_title: Apprendre Reduce en 10 Minutes
seo_desc: 'By Yazeed Bzadough

  Hopefully this reduces the confusion.

  In my experience learning and teaching JavaScript, reduce is one of the toughest
  concepts to crack. In this article I''ll try to address one core question...


  What is reduce and why is it called...'
---

Par Yazeed Bzadough

Espérons que cela réduit la confusion.

Dans mon expérience d'apprentissage et d'enseignement de JavaScript, `reduce` est l'un des concepts les plus difficiles à maîtriser. Dans cet article, je vais essayer de répondre à une question centrale...

> Qu'est-ce que `reduce` et pourquoi est-il appelé ainsi ?

## Reduce a de nombreux noms
Certains d'entre eux, [selon Wikipedia](https://en.wikipedia.org/wiki/Fold_(higher-order_function)), sont

* Reduce
* Fold
* Accumulate
* Aggregate
* Compress

Ils suggèrent tous l'idée centrale. Il s'agit de **décomposer une structure en une seule valeur**.

> Reduce - Une fonction qui plie une liste en n'importe quel type de données.

C'est comme plier une boîte ! Avec `reduce`, vous pouvez transformer un tableau `[1,2,3,4,5]` en le nombre `15` en les additionnant tous.

<img src="https://www.freecodecamp.org/news/content/images/2019/10/folding-box.gif" alt="folding-box" />

### La méthode traditionnelle
Normalement, vous auriez besoin d'une boucle pour "plier" une liste en un nombre.

```js
const add = (x, y) => x + y;
const numbers = [1, 2, 3, 4, 5];
let total = 0;

for (let i = 0; i < numbers.length; i++) {
    total = add(total, numbers[i]);
}

console.log(total); // 15
```

### La méthode moderne
Mais avec `reduce`, vous pouvez brancher votre fonction `add` et la boucle est gérée pour vous !

```js
const add = (x, y) => x + y;
const numbers = [1, 2, 3, 4, 5];

numbers.reduce(add);
// 15
```

Vous pliez littéralement 1-5 pour obtenir 15.

<img src="https://www.freecodecamp.org/news/content/images/2019/10/folding-box.gif" alt="folding-box" />

## Les trois grands
Avant d'approfondir, je pense qu'il est important d'analyser `reduce` aux côtés de ses célèbres compagnons, `map` et `filter`. Ils éclipseront fortement `reduce`, le faisant paraître comme le bizarre du groupe.

![creepy-reduce](https://www.freecodecamp.org/news/content/images/2019/10/creepy-reduce.jpeg)

Malgré leurs popularités respectives, combiner ces trois titans vous permet de manipuler les listes comme vous le souhaitez !

![the-big-three](https://www.freecodecamp.org/news/content/images/2019/10/the-big-three.jpeg)

Pour un moment, faites-moi plaisir et imaginez que JavaScript ne peut pas utiliser de boucles, de récursions, ou de méthodes de tableau comme `forEach`, `some`, `find`, etc. Les trois seules méthodes restantes sont `map`, `filter` et `reduce`.

Notre travail en tant que programmeurs n'a pas changé, cependant. Nous avons toujours besoin de trois types de fonctionnalités dans nos applications.

1. Transformer des listes
2. Filtrer des listes
3. Transformer des listes en d'autres types de données (nombre, chaîne, booléen, objet, etc.).

Voyons comment nos seuls outils, `map`, `filter` et `reduce`, gèrent ce défi.

### ✅ Array.map transforme les listes
Transformer des listes en d'autres listes est le développement Front-End en un mot. Par conséquent, `map` couvre une grande partie de votre travail sur les listes. 

Supposons que notre application appelle une API pour la liste des utilisateurs, et nous avons besoin d'afficher le nom de chaque utilisateur à l'écran. Il suffit de créer une fonction qui retourne le nom d'_un_ utilisateur.

```js
const getUserName = (user) => user.name;
```

Et de la brancher dans `map` pour l'exécuter contre une liste entière d'utilisateurs.

```js
users.map(getUserName)
// ['Marie', 'Ken', 'Sara', 'Geoff', ...]
```

### ✅ Array.filter juge les listes
Et si vous voulez une nouvelle liste avec certains éléments supprimés, comme lorsque l'utilisateur recherche dans sa liste de contacts ? Il suffit de créer une fonction qui retourne `true` ou `false` en fonction de son entrée (un prédicat).

```js
const isEven = (x) => x % 2 === 0;
```

Et de la brancher dans `filter` pour l'appliquer contre une liste entière.

```js
const numbers = [1, 2, 3, 4, 5];
numbers.filter(isEven);
// [2, 4]
```

### ✅ Array.reduce fait tout cela, et plus encore
Lorsque `map` et `filter` ne suffisent pas, vous faites appel aux grands moyens. La méthode `reduce` peut faire ce que `map`/`filter` font, et tout ce qui implique de boucler sur un tableau.

![reduce-will-take-this](https://www.freecodecamp.org/news/content/images/2019/10/reduce-will-take-this.png)

Par exemple, comment calculeriez-vous l'âge total de vos utilisateurs ? Les âges de nos utilisateurs sont 25, 22, 29 et 30.

```js
const users = [
  { name: 'Marie', age: 25 },
  { name: 'Ken', age: 22 },
  { name: 'Sara', age: 29 },
  { name: 'Geoff', age: 30 },
];
```

`map` et `filter` ne peuvent retourner que des tableaux, mais nous avons besoin d'un `nombre` !

```js
users.map(?);
users.filter(?);

// Non ! J'ai besoin d'un nombre, pas de tableaux.
```

Si nous avions des boucles, nous passerions simplement par `users` et additionnerions leurs âges dans un compteur ! Eh bien, que diriez-vous si je vous disais que c'est encore plus facile avec `reduce` ?

```js
users.reduce((total, currentUser) => total + currentUser.age, 0);
// 106
```

![fallout-hold-up](https://www.freecodecamp.org/news/content/images/2019/10/fallout-hold-up-1.jpeg)

## Journalisez-le
Je pense que la manière la plus simple de comprendre cela est de `console.log` à chaque étape.

```js
const users = [
  { name: 'Marie', age: 25 },
  { name: 'Ken', age: 22 },
  { name: 'Sara', age: 29 },
  { name: 'Geoff', age: 30 },
];

const reducer = (total, currentUser) => {
    console.log('current total:', total);
    console.log('currentUser:', currentUser);
    
    // juste pour l'espacement
    console.log('\n');
    
    return total + currentUser.age;
}

users.reduce(reducer, 0);
```

Voici une capture d'écran de Chrome DevTools.

![reduce-screenshot-1](https://www.freecodecamp.org/news/content/images/2019/10/reduce-screenshot-1.png)

## Décomposez-le
Comme vous venez de le voir, `Array.reduce` prend deux paramètres.

1. Le reducer
2. Une valeur initiale (optionnelle)

Le reducer est la fonction qui fait tout le travail. Lorsque `reduce` boucle sur votre liste, il alimente deux paramètres à votre reducer.

1. Un accumulateur
2. La valeur actuelle

La valeur actuelle est auto-explicative, tout comme lorsque vous utilisez `array[i]` dans une boucle régulière. L'accumulateur, cependant, est un terme informatique qui semble effrayant mais qui est en réalité simple.

### L'accumulateur est la valeur de retour finale
Lorsque vous bouclez à travers les `users`, comment gardez-vous une trace de leur âge total ? Vous avez besoin d'une variable _compteur_ pour le contenir. **C'est l'accumulateur.** C'est la valeur finale que `reduce` retournera lorsqu'il aura terminé.

À chaque étape de la boucle, il alimente le dernier accumulateur et l'élément actuel à votre reducer. Ce que le reducer retourne devient le prochain accumulateur. Le cycle se termine lorsque la liste est terminée et que vous avez une seule valeur réduite.

![reduce-screenshot-1](https://www.freecodecamp.org/news/content/images/2019/10/reduce-screenshot-1.png)

### La valeur initiale est optionnelle
Le deuxième paramètre de `reduce` est la valeur initiale. Si vous ne la fournissez pas, `reduce` utilise par défaut le premier élément de la liste.

Cela convient si vous additionnez des nombres simples.

```js
[1, 2, 3].reduce((total, current) => total + current);
// 6
```

Mais cela ne fonctionne pas si vous utilisez un objet ou un tableau car vous ne devriez pas additionner ces choses.

```js
[{ age: 1 }, { age: 2 }, { age: 3 }]
    .reduce((total, obj) => total + obj.age);
    
// [object Object]23
// Résultat incorrect, utilisez une valeur initiale.
```

Dans ce cas, vous devriez donner la valeur initiale de `0`.

```js
[{ age: 1 }, { age: 2 }, { age: 3 }]
    .reduce((total, obj) => total + obj.age, 0);
    
// 6
// La valeur initiale corrige cela.
// 0 + 1 + 2 + 3 = 6
```

## Re-créons Reduce
> Ce que je ne peux pas créer, je ne le comprends pas - Richard Feynman
 
Espérons que je vous ai aidé jusqu'à présent. Il est maintenant temps d'écrire votre propre fonction `reduce` pour vraiment ancrer cela.

Ce sera une fonction qui prend trois paramètres.

1. Un reducer
2. Une valeur initiale
3. Un tableau sur lequel opérer

Pour cette démonstration, la valeur initiale n'est pas optionnelle.

```js
const reduce = (reducer, initialValue, array) => {
    let accumulator = initialValue;

    for (let i = 0; i < array.length; i++) {
        const currentItem = array[i];
        accumulator = reducer(accumulator, currentItem);
    }
    
    return accumulator;
}
```

Incroyable, seulement 10 lignes de code, 6 étapes clés. Je vais les passer en revue une par une.

1. Définir `reduce` et ses trois paramètres.
2. Initialiser l'`accumulator` en utilisant la `initialValue` fournie. Cette variable changera à chaque boucle.
3. Commencer à boucler sur le tableau.
4. Capturer l'`currentItem` du tableau pour ce cycle.
5. Appeler `reducer` avec l'`accumulator` et `currentItem`, en le sauvegardant comme un nouvel `accumulator`.
6. Lorsque la boucle est terminée et que l'`accumulator` a fini de changer, le retourner.


## Histoire diverse
Je voulais parler davantage de l'histoire de `reduce` et des reducers, mais je n'étais pas tout à fait sûr où le placer. Néanmoins, c'est très intéressant !

### Les reducers sont anciens
![redux-did-not-invent-reducers](https://www.freecodecamp.org/news/content/images/2019/10/redux-did-not-invent-reducers.jpeg)

[Redux](https://redux.js.org) a rendu les reducers populaires auprès des développeurs JavaScript, mais il ne les a pas inventés. Il n'est pas clair qui a inventé le terme, mais voici quelques références que j'ai déterrées.

### Théorie de la récursion (1952)
[Ce livre](https://www.amazon.com/Introduction-Metamathematics-Stephen-Cole-Kleene/dp/0923891579) de 1952 discute de `reduce` d'un point de vue métamathématique, en le désignant par `fold`.

### Manuel du programmeur Lisp (1960)
Le [Manuel du programmeur Lisp](https://kyber.io/rawvids/LISP_I_Programmers_Manual_LISP_I_Programmers_Manual.pdf) de 1960 contient une section sur la fonction `reduce`.

### Introduction à la programmation fonctionnelle (1988)
[Ce livre](https://usi-pl.github.io/lc/sp-2015/doc/Bird_Wadler.%20Introduction%20to%20Functional%20Programming.1ed.pdf) de 1988 parle de l'utilisation de `reduce` pour transformer des listes en d'autres valeurs.

En résumé, c'est un sujet ancien. Plus vous étudiez l'informatique, plus vous réalisez que nous réemballons principalement des concepts découverts il y a des décennies.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The more you study computer science the more you realize we&#39;re mostly re-wrapping concepts discovered decades ago.</p>&mdash; Yazeed Bzadough (@yazeedBee) <a href="https://twitter.com/yazeedBee/status/1183510524438437890?ref_src=twsrc%5Etfw">October 13, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Exercices pour vous
Pour des raisons de temps, nous terminons ici. Cependant, j'espère avoir au moins suggéré que `reduce` est incroyablement puissant et utile bien au-delà de la simple somme de nombres.

Si vous êtes intéressé, essayez ces exercices et [envoyez-moi un message à leur sujet plus tard](https://twitter.com/yazeedBee). Je pourrais écrire un article de suivi sur eux.

1. Réimplémentez la fonction [Array.map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) en utilisant `reduce`.
2. Réimplémentez la fonction [Array.filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) en utilisant `reduce`.
3. Réimplémentez la fonction [Array.some](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some) en utilisant `reduce`.
4. Réimplémentez la fonction [Array.every](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every) en utilisant `reduce`.
5. Réimplémentez la fonction [Array.find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find) en utilisant `reduce`.
6. Réimplémentez la fonction [Array.forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach) en utilisant `reduce`.
7. Transformez un tableau en un objet en utilisant `reduce`.
8. Transformez un tableau 2D en un tableau 1D (plat) en utilisant `reduce`.

## Vous voulez un coaching gratuit ?
Si vous souhaitez planifier un appel gratuit de 15 à 30 minutes pour discuter de questions de développement Front-End concernant le code, les entretiens, la carrière ou autre chose, [suivez-moi sur Twitter et envoyez-moi un message direct](https://twitter.com/yazeedBee).

Après cela, si vous appréciez notre première rencontre, nous pouvons discuter d'une relation de coaching continue qui vous aidera à atteindre vos objectifs de développement Front-End !

## Merci d'avoir lu
Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">https://yazeedb.com!</a>

À la prochaine !