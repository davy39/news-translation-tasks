---
title: La dernière version de JavaScript n'a que 2 nouvelles fonctionnalités. Voici
  comment elles fonctionnent.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-13T06:42:34.000Z'
originalURL: https://freecodecamp.org/news/why-could-es7-be-called-es2-4c5f094ccef7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4KuLQRBf9qZkEGUsFKZnJg.png
tags:
- name: Exponential Operator
  slug: exponential-operator
- name: Array Prototype Includes
  slug: array-prototype-includes
- name: es7
  slug: es7
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: La dernière version de JavaScript n'a que 2 nouvelles fonctionnalités.
  Voici comment elles fonctionnent.
seo_desc: 'By Tiago Lopes Ferreira

  Let’s talk about the latest version of JavaScript: ECMAScript 2016 (more commonly
  known as ES7). ES7 brings two new features: Array.prototype.includes() and the new
  exponential operator: **.

  Array.prototype.includes()

  Gone are...'
---

Par Tiago Lopes Ferreira

Parlons de la dernière version de JavaScript : ECMAScript 2016 (plus communément connu sous le nom de ES7). ES7 apporte deux nouvelles fonctionnalités : `Array.prototype.includes()` et le nouvel opérateur exponentiel : `**`.

### Array.prototype.includes()

Les jours où nous utilisions `.indexOf()` pour savoir si un élément **existait** dans un tableau sont révolus.

Le mot clé est **"exister"**.

`.indexOf()` est bien si nous voulons savoir à quel index un élément donné apparaît.

Mais si notre objectif est de savoir si un élément donné **existe** dans un tableau, alors `.indexOf()` n'est pas la meilleure option. Et la raison est simple : Lorsque nous interrogeons l'existence de quelque chose, nous attendons une valeur booléenne, **pas un nombre**.

`Array.prototype.includes()` fait exactement cela. Il détermine si un élément donné existe dans un tableau, retournant `true` s'il existe, `false` sinon.

### Dans la Spécification

```
Array.prototype.includes ( searchElement [ , fromIndex ] )
```

* `searchElement` — l'élément à rechercher.
* `fromIndex` _(optionnel)_ — l'index à partir duquel commencer la recherche.

Plonger dans la [spécification](https://www.ecma-international.org/ecma-262/7.0/) donne l'impression de chercher du pouvoir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4KuLQRBf9qZkEGUsFKZnJg.png)

La spécification dit :

Allons étape par étape et essayons de comprendre la spécification avec des exemples.

1. La différence ici est la position de l'élément 4. Parce que notre premier exemple place 4 dans la dernière position, includes recherchera dans tout le tableau. Selon la spécification, `.includes()` retourne immédiatement après avoir trouvé le `searchElement`. Cela rend notre deuxième opération beaucoup plus rapide.
2. La grande différence avec l'algorithme [SameValueZero](https://www.ecma-international.org/ecma-262/7.0/#sec-samevaluezero) par rapport à la [Strict Equality Comparison](https://www.ecma-international.org/ecma-262/7.0/#sec-strict-equality-comparison) (utilisé par `.indexOf()`) est qu'il permet de détecter les éléments **NaN**.
3. Il retourne le booléen `true` lorsque l'élément est trouvé et `false` sinon. Plus d'index comme résultat ?
4. Contrairement à `.indexOf()`, `.includes()` ne saute pas les éléments manquants du tableau. Au lieu de cela, il les traite comme des valeurs **undefined**.

Commencez-vous à sentir le pouvoir ?

Nous n'avons même pas touché à `fromIndex`.

Vérifions la spécification :

> Le deuxième argument optionnel `fromIndex` est par défaut `0` (c'est-à-dire que tout le tableau est recherché). S'il est supérieur ou égal à la longueur du tableau, **false** est retourné, c'est-à-dire que le tableau ne sera pas recherché. S'il est négatif, il est utilisé comme **décalage** à partir de la fin du tableau pour calculer `fromIndex`. Si l'index calculé est inférieur à `0`, tout le tableau sera recherché.

1. Si aucun `fromIndex` n'est fourni, la valeur par défaut de `0` est prise et le tableau **entier** est recherché.
2. `.includes()` retourne immédiatement **false** lorsque la valeur de `fromIndex` est supérieure à la longueur du tableau.
3. Lorsque `fromIndex` est négatif, sa valeur est calculée comme `array.length — fromIndex`. Cela est particulièrement utile lors de la recherche sur les derniers éléments. Par exemple, `fromIndex = -5` est la même chose que de rechercher sur les 5 derniers éléments.
4. Pour éviter que `.includes()` ne se casse lorsque la valeur calculée de `fromIndex` est inférieure à 0, le tableau entier est recherché. Je préférerais qu'il se casse ?

OK — une dernière nouvelle fonctionnalité...

### L'Opérateur Exponentiel (`**`)

Nous attendions le jour où nous pourrions jouer avec les nombres exponentiels comme nous jouons avec l'addition, la soustraction, la multiplication, la division.

Eh bien, ce jour est arrivé.

L'opérateur `**` se comporte exactement de la même manière que `Math.pow()`. Il retourne le résultat de l'élévation du premier opérande à la puissance du second (par exemple, `x ** y`).

C'est tout !

Vous avez maintenant le pouvoir de **ES7** ! Utilisez-le bien !

![Image](https://cdn-media-1.freecodecamp.org/images/1*owhYyEq_wSRyPN_OuyQXPQ.gif)

### Remerciements à ?

* [2ality.com](http://2ality.com/2016/01/ecmascript-2016.html) par [Axel Rauschmayer](https://twitter.com/rauschma)
* [ECMAScript® 2016 Language Specification](https://www.ecma-international.org/ecma-262/7.0/)
* À tous les fans de [He-Man](https://www.youtube.com/watch?v=7yeA7a0uS3A)
* [freeCodeCamp](https://medium.freecodecamp.org/) pour la publication ❤️

Assurez-vous de consulter mes articles sur ES6 :

[**Explorons les Générateurs ES6**](https://medium.freecodecamp.org/lets-explore-es6-generators-5e58ed23b0f1)

[_Générateurs, aka, une implémentation des itérables._medium.freecodecamp.org](https://medium.freecodecamp.org/lets-explore-es6-generators-5e58ed23b0f1)

[**Oh Oui ! Async / Await**](https://medium.freecodecamp.org/oh-yes-async-await-f54e5a079fc1)

[_async / await est la nouvelle syntaxe JavaScript pour déclarer une fonction asynchrone._medium.freecodecamp.org](https://medium.freecodecamp.org/oh-yes-async-await-f54e5a079fc1)