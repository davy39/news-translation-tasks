---
title: Démystifier les itérables et les itérateurs ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-21T17:20:07.000Z'
originalURL: https://freecodecamp.org/news/demystifying-es6-iterables-iterators-4bdd0b084082
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PZBEg-i1BCHKA-sPsVoMJg.gif
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Démystifier les itérables et les itérateurs ES6
seo_desc: 'By Tiago Lopes Ferreira

  ES6 introduces a new way to interact with JavaScript data structures — iteration.
  Let’s demystify it.

  There are 2 core concepts:


  Iterable — described by a data structure that provides a way to expose its data
  to the public. T...'
---

Par Tiago Lopes Ferreira

ES6 introduit une nouvelle façon d'interagir avec les structures de données JavaScript — **l'itération**. Démystifions cela.

Il y a 2 concepts clés :

* **Itérable** — décrit par une structure de données qui fournit un moyen d'exposer ses données au public. Cela se fait en implémentant une méthode dont la clé est `Symbol.iterator`. `Symbol.iterator` est une usine d'itérateurs.
* **Itérateur** — décrit par une structure qui contient un pointeur vers l'élément suivant dans l'itération.

### Protocole

Les itérables et les itérateurs suivent un protocole qui permet aux objets d'être itérables :

* Un **itérable** doit être un objet avec une fonction itératrice dont la clé est `Symbol.iterator`.
* Un **itérateur** doit être un objet avec une fonction nommée `next` qui retourne un objet avec les clés : `value` — l'élément actuel dans l'itération ; et `done` — _true_ si l'itération est terminée, _false_ sinon.

#### Itérabilité

L'itérabilité suit l'idée des _sources de données_ et des _consommateurs de données_ :

* **sources de données** — sont l'endroit d'où les consommateurs de données obtiennent leurs données. Par exemple, un `Array` tel que `[1,2,3]` est une structure de source de données qui contient les données à travers lesquelles un consommateur de données va itérer (par exemple, `1, 2, et 3`). D'autres exemples sont `String`, `Maps` et `Sets`.
* **consommateurs de données** — sont ce qui consomme les données des sources de données. Par exemple, la boucle `for-of` est un consommateur de données capable d'itérer sur une source de données `Array`. D'autres exemples sont l'_opérateur de propagation_ et `Array.from`.

Pour qu'une structure soit une _source de données_, elle doit permettre et dire comment ses données doivent être consommées. Cela se fait par le biais des **itérateurs**. Par conséquent, une _source de données_ doit suivre le protocole d'itérateur décrit ci-dessus.

Cependant, il n'est pas pratique pour chaque _consommateur de données_ de supporter toutes les _sources de données_, surtout puisque JavaScript nous permet de construire nos propres sources de données. Ainsi, ES6 introduit l'interface **Iterable**.

Les _consommateurs de données_ consomment les données des _sources de données_ par le biais des **itérables**.

#### En pratique

Voyons comment cela fonctionne sur une source de données définie — `Array`.

### Sources de données itérables

![Image](https://cdn-media-1.freecodecamp.org/images/1*tqsRBISIOIoXcCAYp7V1Lw.gif)

Nous allons utiliser `for-of` pour explorer certaines des sources de données qui implémentent le **protocole itérable**.

#### Objets simples

À ce stade, nous devons dire que les objets simples ne sont pas itérables. [Axel Rauschmayer](http://(https://twitter.com/rauschma) fait un excellent travail en expliquant pourquoi dans [Exploring ES6](http://exploringjs.com/es6/).

Une brève explication est que nous pouvons itérer sur les objets JavaScript à deux niveaux différents :

* **niveau programme** — ce qui signifie itérer sur les propriétés d'un objet qui représentent sa structure. Par exemple, `Array.prototype.length`, où `length` est lié à la structure de l'objet et non à ses données.
* **niveau données** — ce qui signifie itérer sur une structure de données et en extraire ses données. Par exemple, pour notre exemple `Array`, cela signifierait itérer sur les données du tableau. Si `array = [1,2,3,4]`, itérer sur les valeurs `1, 2, 3 et 4`.

> **Cependant, introduire le concept d'itération dans les objets simples signifie mélanger les structures de programme et de données** — [Axel](http://(https://twitter.com/rauschma)

Le problème avec les objets simples est la capacité de chacun à créer ses propres objets.

_Dans notre exemple de Hugo, comment JavaScript distinguerait-il entre le niveau données, c'est-à-dire `Hugo.fullName`, et le niveau programme, c'est-à-dire `Hugo.toString()` ?_

Bien qu'il soit possible de distinguer entre les deux niveaux d'itération sur des structures bien définies, telles que les `Arrays`, il est impossible de le faire pour n'importe quel objet.

C'est pourquoi nous obtenons l'itération gratuitement sur `Array` (également sur `String`, `Map`, et `Set`) mais pas sur les objets simples.

> **Nous pouvons, cependant, implémenter nos propres itérables.**

### Implémenter des itérables

![Image](https://cdn-media-1.freecodecamp.org/images/1*PZBEg-i1BCHKA-sPsVoMJg.gif)

Nous pouvons construire nos propres itérables, bien que nous utilisions généralement des générateurs pour cela.

Pour construire notre propre itérable, nous devons suivre le protocole d'itération, qui dit :

* Un objet devient un **itérable** s'il implémente une fonction dont la clé est `Symbol.iterator` et retourne un `iterator`.
* L'`iterator` lui-même est un objet avec une fonction appelée `next` à l'intérieur. `next` doit retourner un objet avec deux clés `value` et `done`. `value` contient l'élément suivant de l'itération et `done` un drapeau indiquant si l'itération est terminée.

#### Exemple

Notre implémentation d'itérable est très simple. Nous avons suivi le **protocole itérable** et à chaque itération, la boucle `for-of` demandera à l'itérateur l'élément `next`.

Notre itérateur retournera sur `next` un objet contenant ce qui suit par itération :

Veuillez noter que nous changeons l'ordre de nos propriétés `next` et `done` pour plus de commodité. Ayant `next` en premier, cela briserait l'implémentation puisque nous allons d'abord extraire un élément puis compter les éléments.

Il est utile de savoir que `done` est `false` par défaut, ce qui signifie que nous pouvons l'ignorer lorsque c'est le cas. Il en va de même pour `value` lorsque `done` est `true`.

Nous verrons cela dans une minute.

#### Itérateur en tant qu'itérable

Nous pourrions construire notre itérateur en tant qu'itérable.

Veuillez noter que c'est le modèle suivi par les itérateurs intégrés d'ES6.

**Pourquoi est-ce utile ?**

Bien que `for-of` ne fonctionne qu'avec les itérables, et non avec les itérateurs, être le même signifie que nous pouvons suspendre l'exécution de `for-of` et continuer après.

#### Retour et Lancer

Il y a deux méthodes d'itérateur optionnelles que nous n'avons pas encore explorées :

**Retour**

`return` donne à l'itérateur l'opportunité de **nettoyer** la maison lorsqu'il se brise de manière inattendue. Lorsque nous appelons `return` sur un itérateur, nous spécifions que nous ne prévoyons plus d'appeler `next`.

**Lancer**

`throw` n'est appliqué qu'aux générateurs. Nous verrons cela lorsque nous jouerons avec les générateurs.

### Conclusion

ES6 apporte l'itération comme une nouvelle façon d'itérer sur les structures de données JavaScript.

> Pour que l'itération soit possible, il y a des _producteurs de données_, qui contiennent les données, et des _consommateurs de données_, qui prennent ces données.

Pour que cette combinaison fonctionne en douceur, l'itération est définie par un protocole, qui dit :

* Un `itérable` est un objet qui implémente une fonction dont la clé est `Symbol.iterator` et retourne un `iterator`.
* Un `iterator` est un objet avec une fonction appelée `next` à l'intérieur. `next` est un objet avec deux clés `value` et `done`. `value` contient l'élément suivant de l'itération et `done` un drapeau indiquant si l'itération est terminée.

Les objets simples ne sont pas `itérables` puisque il n'y a pas de moyen facile de distinguer entre l'itération au niveau programme et au niveau données.

C'est pourquoi ES6 offre un moyen de construire nos propres itérateurs en suivant le protocole `iterator`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IwfjCQMFHLP5iswRC7dLyg.gif)

### Remerciements à :

* [Axel Rauschmayer](https://twitter.com/rauschma) pour son [Exploring ES6 — Iteration](http://exploringjs.com/es6/ch_iteration.html)
* [Nicolás Bevacqua](https://twitter.com/nzgb) pour son [PonyFoo — ES6 Iterators in Depth](https://ponyfoo.com/articles/es6-iterators-in-depth)
* À tous les fans de [The Simpsons](https://www.youtube.com/watch?v=SR8WWFzrZAg)