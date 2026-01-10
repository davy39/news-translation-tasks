---
title: Explorons les générateurs ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-21T17:22:27.000Z'
originalURL: https://freecodecamp.org/news/lets-explore-es6-generators-5e58ed23b0f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OiK88NOSMsbrlpWdDarvlg.gif
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
seo_title: Explorons les générateurs ES6
seo_desc: 'By Tiago Lopes Ferreira

  Generators are an implementation of iterables.

  The big deal about generators is that they are functions that can suspend its execution
  while maintaining the context.

  This behaviour is crucial when dealing with executions that ...'
---

Par Tiago Lopes Ferreira

Les générateurs sont [une implémentation des itérables](https://medium.freecodecamp.com/demystifying-es6-iterables-iterators-4bdd0b084082).

L'importance des générateurs réside dans le fait que **ce sont des fonctions qui peuvent suspendre leur exécution tout en maintenant le contexte**. 

Ce comportement est crucial lors de l'exécution de tâches qui doivent être mises en pause, mais dont le contexte doit être maintenu afin de pouvoir être récupéré ultérieurement.

**Le développement asynchrone vous semble-t-il familier ici ?**

### Syntaxe

La syntaxe des générateurs commence par la déclaration `function*` (veuillez noter l'_astérisque_) et le `yield` grâce auquel un générateur peut suspendre son exécution.

L'appel de notre fonction `generator` crée un nouveau générateur que nous pouvons utiliser pour contrôler le processus via la fonction `next`.

L'exécution de `next` exécutera le code de notre `generator` jusqu'à ce qu'une expression `yield` soit atteinte.

À ce stade, la valeur de `yield` est émise et l'exécution du `generator` est suspendue.

#### yield

`yield` est né avec les générateurs et nous permet d'émettre des valeurs. Cependant, nous ne pouvons le faire que si nous sommes à l'intérieur d'un générateur.

Si nous essayons d'utiliser `yield` pour une valeur dans un callback, par exemple, même si elle est déclarée à l'intérieur du générateur, nous obtiendrons une erreur.

#### yield*

`yield*` a été conçu pour permettre d'appeler un générateur à l'intérieur d'un autre générateur.

Notre itérateur `b`, produit par le générateur `bar`, ne fonctionne pas comme prévu lors de l'appel de `foo`.

C'est parce que, bien que l'exécution de `foo` produise un itérateur, nous n'itérons pas dessus.

C'est pourquoi ES6 a introduit l'opérateur `yield*`.

Cela fonctionne parfaitement avec les consommateurs de données.

En interne, `yield*` parcourt chaque élément du générateur et utilise `yield` pour chacun.

### Générateurs en tant qu'itérables

![Image](https://cdn-media-1.freecodecamp.org/images/1*p65T1aheR-c6JDSWRcUVhA.gif)

**Les générateurs sont des itérables simples**, ce qui signifie qu'ils suivent les protocoles `iterable` et `iterator` :

* Le protocole `iterable` stipule qu'un objet doit retourner une fonction itérateur dont la clé est `Symbol.iterator`.

* Le protocole `iterator` stipule que l'itérateur doit être un objet pointant vers l'élément suivant de l'itération. Cet objet doit contenir une fonction appelée `next`.

Parce que les générateurs sont des itérables, nous pouvons utiliser un consommateur de données, par exemple `for-of`, pour itérer sur les valeurs des générateurs.

#### Return

Nous pouvons ajouter une instruction `return` à notre générateur, cependant `return` se comportera différemment selon la manière dont les données du générateur sont itérées.

Lorsque nous effectuons l'itération manuellement, en utilisant `next`, nous obtenons notre valeur retournée (c'est-à-dire `done`) comme dernière `value` de notre objet itérateur et notre indicateur `done` comme vrai.

En revanche, lorsque nous utilisons un consommateur de données défini tel que `for-of` ou `destructuring`, la valeur retournée est ignorée.

#### **yield***

Nous avons vu que `yield*` nous permet d'appeler un générateur à l'intérieur d'un générateur.

Il nous permet également de stocker la valeur retournée par le générateur exécuté.

#### Throw

Nous pouvons utiliser `throw` à l'intérieur d'un générateur et `next` propagera notre exception.

Dès qu'une exception est levée, le flux de l'itérateur est rompu et son état est défini sur `done: true` indéfiniment.

### Générateurs en tant que consommateurs de données

Outre le fait que les générateurs produisent des données via `yield`, ils ont également la capacité de consommer des données en utilisant `next`.

Il y a quelques points intéressants à explorer ici.

#### Création du générateur (1)

À ce stade, nous créons notre générateur `g`.

Notre exécution s'arrête au point `A`.

#### Premier next (2)

La première exécution de `next` fait que notre générateur est exécuté jusqu'à la première instruction `yield`.

Lors de cette première exécution, toute valeur envoyée via `next` est ignorée. Cela est dû au fait qu'il n'y a pas d'instruction `yield` jusqu'à la première instruction `yield` ?

Notre exécution est suspendue à `B` en attendant qu'une valeur soit remplie pour `yield`.

#### Prochain next (3)

Lors des prochaines exécutions de `next`, notre générateur exécutera le code jusqu'au prochain `yield`.

Dans notre cas, il journalise la valeur obtenue via `yield` (c'est-à-dire `Got: foo`) et il est à nouveau suspendu sur `yield`.

### Cas d'utilisation

![Image](https://cdn-media-1.freecodecamp.org/images/1*OiK88NOSMsbrlpWdDarvlg.gif)

#### Implémenter des itérables

Parce que **les générateurs sont une implémentation des itérables**, lorsqu'ils sont créés, nous obtenons un objet itérable, où chaque `yield` représente la valeur à émettre à chaque itération. Cette description nous permet d'utiliser les générateurs pour créer des itérables.

L'exemple suivant représente un générateur en tant qu'itérable qui itère sur les nombres pairs jusqu'à ce que `max` soit atteint. Parce que notre générateur retourne un itérable, nous pouvons utiliser `for-of` pour itérer sur les valeurs.

Il est utile de se rappeler que `yield` met en pause l'exécution du générateur, et à chaque itération, le générateur reprend là où il avait été mis en pause.

#### Code asynchrone

Nous pouvons utiliser les générateurs pour mieux travailler avec du code asynchrone, comme les `promises`.

Ce cas d'utilisation est une bonne introduction au nouveau `async/await` dans ES8.

Voici un exemple de récupération d'un fichier JSON avec des `promises` comme nous le connaissons. Nous utiliserons l'exemple de [Jake Archibald](https://twitter.com/jaffathecake) sur [developers.google.com](https://developers.google.com/web/fundamentals/getting-started/primers/promises).

En utilisant la bibliothèque [co](https://github.com/tj/co) et un générateur, notre code ressemblera davantage à du code synchrone.

Quant au nouveau `async/await`, notre code ressemblera beaucoup à notre version précédente.

### Conclusion

Ce schéma, réalisé par [Axel Rauschmayer](https://twitter.com/rauschma) dans [Exploring ES6](http://exploringjs.com/es6/index.html), nous montre comment les générateurs sont liés aux itérateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XBMTOSxCUQ6MloksmDYdJw.png)

Les générateurs sont une implémentation des itérables et suivent les protocoles `iterable` et `iterator`. Par conséquent, ils peuvent être utilisés pour construire des itérables.

La chose la plus étonnante à propos des générateurs est leur capacité à suspendre leur exécution. Pour cela, ES6 introduit une nouvelle instruction appelée `yield`.

Cependant, appeler un générateur à l'intérieur d'un générateur n'est pas aussi simple que d'exécuter la fonction du générateur. Pour cela, ES6 a `yield*`.

> **Les générateurs sont la prochaine étape pour rapprocher le développement asynchrone du développement synchrone.**

### Remerciements à 🙏

* [Axel Rauschmayer](https://twitter.com/rauschma) pour son [Exploring ES6 — Generators](http://exploringjs.com/es6/ch_generators.html)
* [Nicolás Bevacqua](https://twitter.com/nzgb) pour son [PonyFoo — ES6 Generators in Depth](https://ponyfoo.com/articles/es6-generators-in-depth)
* [Jake Archibald](https://twitter.com/jaffathecake) pour son exemple de promises sur [developers.google.com](https://developers.google.com/web/fundamentals/getting-started/primers/promises)
* À tous les fans de [Regular Show](https://www.youtube.com/watch?v=n_OC-RAm7Qs)

_N'oubliez pas de consulter mes autres articles sur ES6_

[**Démystifier les itérables et itérateurs ES6**](https://medium.freecodecamp.com/demystifying-es6-iterables-iterators-4bdd0b084082)  
[_Démystifions la nouvelle façon de JavaScript d'interagir avec les structures de données._medium.freecodecamp.com](https://medium.freecodecamp.com/demystifying-es6-iterables-iterators-4bdd0b084082)