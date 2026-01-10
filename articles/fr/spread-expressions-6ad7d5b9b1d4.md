---
title: Comment simplifier votre code avec l'opérateur de décomposition
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T01:49:27.000Z'
originalURL: https://freecodecamp.org/news/spread-expressions-6ad7d5b9b1d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EsKDjaX82lNdGYXSWOst_w.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment simplifier votre code avec l'opérateur de décomposition
seo_desc: 'By Matt Granmoe

  Recently, a co-worker who is learning to love JavaScript came to me asking if there
  was a simple way to take a function like this:

  and return bar: parseBar(bar)when bar is passed. But somehow prevent returning bar
  as undefined when ba...'
---

Par Matt Granmoe

Récemment, un collègue qui apprend à aimer JavaScript est venu me demander s'il existait un moyen simple de prendre une fonction comme celle-ci :

et retourner `bar: parseBar(bar)` lorsque `bar` est passé. Mais d'une manière ou d'une autre, empêcher de retourner `bar` comme `undefined` lorsque `bar` n'est pas passé, puisque certaines utilisations de cela dans la base de code ne le passent pas. Il cherchait spécifiquement un moyen de faire cela qui ne nécessiterait aucune refactorisation (comme changer d'un retour implicite à un corps de fonction complet, utiliser des instructions if/else, créer une fonction séparée pour filtrer certaines valeurs, etc.).

Après quelques essais dans la console JavaScript, j'ai réalisé que ce qui suit est possible :

Voici un exemple condensé à essayer dans la console si vous le souhaitez :

Cela est possible grâce à deux choses. Premièrement, le fait que, bien que l'opérateur de décomposition ne puisse pas _apparaître_ n'importe où en tant que token, il peut être appliqué à littéralement _n'importe quel type de données dans tout le langage_.

Il est communément admis que `Object`, `Array`, `Set` et similaires sont itérables. Le fait que tous les types _primitifs_ soient également des opérandes valides de l'opérateur de décomposition nous permet de décomposer littéralement _n'importe quelle_ expression, puisque toutes les expressions évalueront à une certaine valeur après avoir été exécutées.

Si vous ne me croyez pas, essayez ce qui suit dans la console :

La deuxième chose qui nous aide est que la décomposition d'une valeur "vide" résulte en une opération sans effet.

Deux exemples rapides de la manière dont cette ruelle de JavaScript pourrait être utilisée :

* Expressions de garde (à la React's JSX, et aussi ce qui a été utilisé pour résoudre le problème original mentionné dans ce post) : `...(foo && parseFoo(foo))`
* Expressions "par défaut" : `...(someValue || someDefault)`

Une manière plus générique de se référer à toutes ces choses pourrait être "expressions de décomposition". Cependant, j'aimerais maintenant dire "expressions de décomposition" non pas comme un nom mais comme une suggestion. Allez de l'avant avec la connaissance que vous pouvez décomposer _toutes_ les expressions ! ?