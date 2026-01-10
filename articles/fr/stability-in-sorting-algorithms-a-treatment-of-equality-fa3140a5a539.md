---
title: Stabilité dans les algorithmes de tri — Un traitement de l'égalité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-28T23:16:19.000Z'
originalURL: https://freecodecamp.org/news/stability-in-sorting-algorithms-a-treatment-of-equality-fa3140a5a539
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ghZAH4YaFgcBXL84TuMLXw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Stabilité dans les algorithmes de tri — Un traitement de l'égalité
seo_desc: 'By Onel Harrison

  Algorithms are at the heart of computer science. Algorithms used for sorting are
  some of the most fundamental, useful, and consequently, ubiquitous.


  Algorithm — a finite set of unambiguous steps for solving a specific problem.


  We c...'
---

Par Onel Harrison

Les algorithmes sont au cœur de l'informatique. Les algorithmes utilisés pour le tri sont parmi les plus fondamentaux, utiles et, par conséquent, omniprésents.

> Algorithme — un ensemble fini d'étapes non ambiguës pour résoudre un problème spécifique.

Nous trions constamment et souvent inconsciemment, et nous nous appuyons sur l'ordre des objets groupés. Par exemple, nous classons les tâches d'une liste selon leur priorité. Nous empilons les livres sur des étagères par leur hauteur. Nous trions les lignes dans une feuille de calcul ou une base de données, ou nous nous appuyons sur l'ordre alphabétique des mots dans un dictionnaire. Parfois, nous percevons même une certaine forme de beauté dans les arrangements ordonnés.

![Image](https://cdn-media-1.freecodecamp.org/images/bi4NZvtpx6kQ5I1PXNoNLOsusrYSVCQDbVhP)
_Photo par [Unsplash](https://unsplash.com/photos/6GjHwABuci4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Mikael Kristenson</a> sur <a href="https://unsplash.com/search/photos/order-placement?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

En tant que programmeurs, savoir **comment** nous trions est important car cela affecte ce à quoi un arrangement trié pourrait ressembler. Tous les tris ne classent pas les objets de la même manière ! Pour cette raison, les résultats des opérations de tri diffèrent en fonction des algorithmes utilisés. Si cela n'est pas reconnu, nous pourrions nous surprendre nous-mêmes ou les personnes qui utilisent notre logiciel.

La stabilité des algorithmes de tri est l'une des propriétés distinctives parmi eux. Elle traite de la manière dont l'algorithme gère les éléments comparables avec des clés de tri égales.

> Clé de tri — Une clé utilisée pour déterminer l'ordre des éléments dans une collection, par exemple l'âge, la taille, la position dans l'alphabet, etc.

**Un algorithme de tri stable** maintient l'ordre relatif des éléments avec des clés de tri égales. Un algorithme de tri instable ne le fait pas. En d'autres termes, lorsqu'une collection est triée avec un algorithme de tri stable, les éléments avec les mêmes clés de tri conservent leur ordre après le tri de la collection.

### Un exemple, du code et une démonstration

![Image](https://cdn-media-1.freecodecamp.org/images/cLIBZqqktMgD1zb37j0Ic-RpIXSLOBQtNYdx)
_Image montrant l'effet du tri stable_

L'image ci-dessus illustre l'effet d'un tri stable. À gauche, les données ont été triées alphabétiquement par Nom. Après avoir trié les données par Note, vous pouvez voir que l'ordre alphabétique des noms a été maintenu pour chaque ligne avec la même Note.

![Image](https://cdn-media-1.freecodecamp.org/images/qFs0bAIY74R0sBaXe-PmAjqOA00fbhU5tR4p)
_Image montrant l'effet du tri instable_

Avec un tri instable, il n'y a aucune garantie que l'ordre alphabétique soit maintenu comme le montre l'image ci-dessus.

#### Vous n'avez pas toujours besoin d'un tri stable

Savoir si le tri que vous utilisez est stable ou non est particulièrement important. Surtout dans les situations où vos données ont déjà un certain ordre que vous souhaitez maintenir lorsque vous les triez par une autre clé de tri. Par exemple, vous avez des lignes dans une feuille de calcul contenant des données d'étudiants qui, par défaut, sont triées par nom. Vous souhaitez également les trier par notes tout en maintenant l'ordre trié des noms.

D'un autre côté, la stabilité du tri n'a pas d'importance lorsque les clés de tri des objets dans une collection sont les objets eux-mêmes — un tableau d'entiers ou de chaînes, par exemple — car nous ne pouvons pas faire la différence parmi les clés dupliquées.

```
// JavaScript
```

```
// 5 $ si vous pouvez dire correctement quel 4 dans le tableau trié
// était le premier 4 lorsque le tableau n'était pas trié.
```

```
var numbers = [5, 4, 3, 4, 9];numbers.sort(); // [3, 4, 4, 5, 9]
```

```
// Un voyage d'une seconde autour du monde, offert par Flash, à
// celui qui me dit correctement quel 'harry' dans le tableau trié était
// le deuxième 'harry' dans le tableau non trié.
```

```
var names = ['harry', 'barry', 'harry', 'cisco'];names.sort(); // ['barry', 'cisco', 'harry', 'harry']
```

#### Les tris sont partout — connaissez vos tris

Il est assez facile de savoir si le tri par défaut dans votre langage de programmation ou votre bibliothèque est stable. La documentation devrait inclure cette information. Par exemple, [le tri par défaut est stable en Python](https://wiki.python.org/moin/HowTo/Sorting), [instable en Ruby](https://ruby-doc.org/core-2.0.0/Enumerable.html#method-i-sort), et [non défini](http://www.ecma-international.org/ecma-262/7.0/index.html#sec-array.prototype.sort) en [JavaScript](http://www.ecma-international.org/ecma-262/7.0/index.html#sec-array.prototype.sort) (cela dépend de l'implémentation du navigateur).

Voici quelques algorithmes de tri courants et leur stabilité :

* Tri par insertion — Stable
* Tri par sélection — Instable
* Tri à bulles — Stable
* Tri fusion — Stable
* Tri de Shell — Instable
* Timsort — Stable

Voir [Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability) pour une liste plus exhaustive.

#### C'est l'heure de la démonstration ??

[Cette démonstration](https://onelharrison.com/sort-stability-demo/) montre l'effet de l'utilisation d'un algorithme de tri stable (tri par insertion) et instable (tri par sélection) pour trier un petit tableau de données. Je me suis un peu amusé et j'ai pratiquement reverse engineered React en construisant cela. Jetez un coup d'œil à la [source](https://github.com/onelharrison/sort-stability-demo).

### Qu'est-ce qui suit ?

Si vous avez soif de plus de connaissances sur la stabilité d'autres algorithmes de tri, [Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability) a un bon tableau comparatif et des informations supplémentaires sur les algorithmes de tri bien connus.

Jusqu'à la prochaine fois, paix.

#### Vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article ? Applaudissez, partagez-le pour que d'autres puissent le lire aussi, et suivez pour plus. N'hésitez pas à laisser un commentaire aussi.