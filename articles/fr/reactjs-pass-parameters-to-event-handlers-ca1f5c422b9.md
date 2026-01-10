---
title: ReactJS - Gestionnaires d'événements paramétrés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-11T16:16:58.000Z'
originalURL: https://freecodecamp.org/news/reactjs-pass-parameters-to-event-handlers-ca1f5c422b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Rxzsy_E2MgxPP5oVmh1Q_g.jpeg
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
seo_title: ReactJS - Gestionnaires d'événements paramétrés
seo_desc: 'By Sanket Meghani

  It is quite frequent requirement to pass parameters to event handlers of custom
  React components. There are several ways to achieve this with ES6 depending on whether
  we need reference to the event or not.

  Using the bind function

  We...'
---

Par Sanket Meghani

Il est assez fréquent de devoir passer des paramètres aux gestionnaires d'événements des composants React personnalisés. Il existe plusieurs façons d'y parvenir avec ES6, selon que nous ayons besoin d'une référence à l'événement ou non.

### Utilisation de la fonction bind

Nous pouvons définir le gestionnaire d'événements et le lier à `this` en utilisant la fonction `Function.prototype.bind()` de JavaScript.

Si nous devons passer des paramètres personnalisés, nous pouvons simplement passer les paramètres à l'appel de bind. Le SyntheticEvent sera passé en tant que second paramètre au gestionnaire.

Un appel de fonction `bind` dans une prop JSX comme ci-dessus créera une toute nouvelle fonction à chaque rendu. Cela est mauvais pour les performances, car cela entraînera l'invocation du garbage collector bien plus que nécessaire. Cela peut également provoquer des re-rendus inutiles si une toute nouvelle fonction est passée en tant que prop à un composant qui utilise une vérification d'égalité de référence sur la prop pour déterminer s'il doit se mettre à jour.

Pour éviter de créer une toute nouvelle fonction à chaque rendu, nous pouvons lier la fonction dans le constructeur.

Maintenant, nous n'avons pas besoin de lier la fonction lors de la spécification du gestionnaire d'événements à la ligne 13. Cependant, l'inconvénient ici est que nous ne pouvons pas passer de valeur dynamique pour le paramètre.

### Utilisation de la fonction fléchée ES6

Appeler `bind` à chaque fois est ennuyeux. Pour éviter d'appeler `bind`, nous pouvons utiliser la fonction fléchée ES6 qui lie la fonction avec `this` automatiquement.

Nous pouvons également passer des paramètres supplémentaires aux gestionnaires d'événements.

Le problème avec les deux syntaxes ci-dessus est qu'une instance de callback différente est créée chaque fois que le composant est rendu, comme avec la fonction `bind`.

Pour éviter de créer une toute nouvelle instance de callback à chaque rendu, nous pouvons utiliser la syntaxe d'initialisation de propriété pour lier correctement les callbacks.

Pour passer des paramètres aux gestionnaires d'événements tout en utilisant la syntaxe d'initialisation de propriété, nous devons utiliser le currying.

Veuillez noter que le currying entraîne la création d'une nouvelle instance à chaque invocation.

### Conclusion

Étant donné toutes les différentes approches ci-dessus, l'utilisation de la fonction fléchée avec le currying semble être la manière la plus propre et la plus concise (mais pas la plus efficace) de définir des gestionnaires d'événements qui acceptent des paramètres définis par l'utilisateur.

J'aimerais entendre vos commentaires, suggestions ou questions sur les approches ci-dessus.