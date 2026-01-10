---
title: Comment lier this dans React sans un Constructeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T21:19:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-bind-this-in-react-without-a-constructor-3a694f5d1b34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LyzgUAvHq6Z-q_fvqCA5pg.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment lier this dans React sans un Constructeur
seo_desc: 'By Tiffany White

  This post was originally published on my blog.

  this in React is a reference to the current component. Usually this in React is
  bound to its built-in methods. When you want to update state or use an event handler
  on a form, you could ...'
---

Par Tiffany White

_Cet article a été initialement publié sur mon [blog](https://tiffanywhite.tech/bind-this-without-constructor/)_.

`this` dans React est une référence au composant actuel. Habituellement, `this` dans React est lié à ses méthodes intégrées. Lorsque vous souhaitez mettre à jour l'état ou utiliser un gestionnaire d'événements sur un formulaire, vous pourriez faire quelque chose comme ceci :

où `this.someInput` transmet l'état au composant React que vous rendez.

Malheureusement, React ne lie pas automatiquement `this` aux méthodes personnalisées. Cela signifie que si je voulais manipuler le DOM en obtenant une entrée, ce que vous ne pouvez pas faire comme avec JavaScript normal, je créerais une `ref` pour effectuer les modifications du DOM que je souhaite.

Mais parce que React ne lie pas automatiquement `this`, le code suivant afficherait undefined lorsqu'il est journalisé :

Pour éviter cela, nous pourrions utiliser la fonction `constructor` pour rendre le composant ou obtenir l'état que nous voulons :

Bien que ce soit une manière décente de rendre une ref sur un composant, que se passe-t-il si vous souhaitez lier plusieurs méthodes personnalisées dans un seul composant ? Cela deviendrait assez désordonné...

Vous voyez l'idée.

Au lieu de cela, nous pouvons lier `this` aux méthodes personnalisées de React en déclarant une méthode en l'assignant à une fonction fléchée :

ce qui nous permettra de lier la valeur de `this` au composant `SomeComponent`.

#### J'espère que cela aide !

ES6 nous a donné des classes et des constructeurs, et React les a utilisés immédiatement. Vous n'avez pas _toujours_ besoin d'un constructeur, et il est utile de savoir quand l'utiliser et quand ne pas l'utiliser.

#### Pendant que vous êtes ici !

J'écris des lettres discrètes de temps en temps. Ce sont des lettres de développement qui sont un peu plus intimes que les newsletters régulières. Inscrivez-vous si vous le souhaitez. Pas de soucis.