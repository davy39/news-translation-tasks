---
title: Comment utiliser la déstructuration en JavaScript (ES6) à son plein potentiel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T20:01:40.000Z'
originalURL: https://freecodecamp.org/news/destructuring-in-javascript-es6-ee963292623a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0e6fFQQRvkZ1LkeAHAMx7w.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment utiliser la déstructuration en JavaScript (ES6) à son plein potentiel
seo_desc: 'By Joanna Gaudyn

  Destructuring was a new addition to ES6. It took inspiration from languages like
  Python and allows you to extract data from arrays and objects into distinct variables.
  It might sound like something you’ve done in the earlier versions...'
---

Par Joanna Gaudyn

La déstructuration était une nouvelle fonctionnalité ajoutée à ES6. Elle s'est inspirée de langages comme Python et permet d'extraire des données de tableaux et d'objets dans des variables distinctes. Cela peut sembler être quelque chose que vous avez déjà fait dans les versions précédentes de JavaScript, n'est-ce pas ? Regardez ces deux exemples.

Le premier extrait des données d'un objet :

```
const meal = {  name: 'pizza',  type: 'marinara',  price: 6.25};
```

```
const name = meal.name;const type = meal.type;const price = meal.price;
```

```
console.log(name, type, price);
```

Affiche :

> pizza marinara 6.25

Et le second extrait des données d'un tableau :

```
const iceCreamFlavors = ['hazelnut', 'pistachio', 'tiramisu'];const flavor1 = iceCreamFlavors[0];const flavor2 = iceCreamFlavors[1];const flavor3 = iceCreamFlavors[2];console.log(flavor1, flavor2, flavor3);
```

Affiche :

> hazelnut pistachio tiramisu

Le problème, c'est que ni l'un ni l'autre de ces exemples n'utilise réellement la déstructuration.

#### Qu'est-ce que la déstructuration ?

La déstructuration vous permet de spécifier les éléments que vous souhaitez extraire d'un tableau ou d'un objet _du côté gauche d'une affectation_. Cela signifie beaucoup moins de code et exactement le même résultat qu'auparavant, sans perdre en lisibilité. Même si cela peut sembler étrange au premier abord.

Refaisons nos exemples.

#### Déstructuration d'objets

Voici comment nous déstructurons les valeurs d'un objet :

```
const meal = {  name: 'pizza',  type: 'marinara',  price: 6.25};
```

```
const {name, type, price} = meal;
```

```
console.log(name, type, price);
```

Affiche :

> pizza marinara 6.25

Les accolades `{ }` représentent l'objet qui est déstructuré et `name`, `type` et `price` représentent les variables auxquelles vous souhaitez assigner les valeurs. Nous pouvons omettre la propriété d'où extraire les valeurs, tant que les noms de nos variables correspondent aux noms des propriétés de l'objet.

Une autre grande fonctionnalité de la déstructuration d'objets est que vous pouvez choisir quelles valeurs vous souhaitez enregistrer dans des variables :

`_const {type} = meal;_` ne sélectionnera que la propriété `_type_` de l'objet `_meal_`.

![Image](https://cdn-media-1.freecodecamp.org/images/kWOMzaEg2A62-CFxEphqLSsopdq6r9ohdxDV)
_[source](https://unsplash.com/photos/22Vt7JIf7ZI" rel="noopener" target="_blank" title=")_

#### Déstructuration de tableaux

Voici comment notre exemple original serait traité :

```
const iceCreamFlavors = ['hazelnut', 'pistachio', 'tiramisu'];
```

```
const [flavor1, flavor2, flavor3] = iceCreamFlavors;
```

```
console.log(flavor1, flavor2, flavor3);
```

Affiche :

> hazelnut pistachio tiramisu

Les crochets `[ ]` représentent le tableau qui est déstructuré et `flavor1`, `flavor2` et `flavor3` représentent les variables auxquelles vous souhaitez assigner les valeurs. En utilisant la déstructuration, nous pouvons omettre les index où se trouvent les valeurs dans notre tableau. Pratique, n'est-ce pas ?

De manière similaire à un objet, vous pouvez ignorer certaines valeurs lors de la déstructuration d'un tableau :

`const [flavor1, , flavor3] = iceCreamFlavors;` ignorera simplement `flavor2`.

![Image](https://cdn-media-1.freecodecamp.org/images/ZaoWWywMgfyk2d4UgeIhJzLwIYD2O46xHzpV)
_[source](https://unsplash.com/photos/qg_faAXDawA" rel="noopener" target="_blank" title=")_

Vive la paresse comme puissant moteur pour l'invention de nouveaux raccourcis !

Avez-vous aimé cet article ? Peut-être que vous trouverez ceux-ci intéressants aussi :

[**Qu'a le yoga à voir avec la programmation ?**](https://medium.freecodecamp.org/what-does-yoga-have-to-do-with-programming-b17094e3fb3a)  
[_Vous pourriez être surpris._medium.freecodecamp.org](https://medium.freecodecamp.org/what-does-yoga-have-to-do-with-programming-b17094e3fb3a)[**Opérateur de propagation et paramètre de repos en JavaScript (ES6)**](https://medium.com/@aska.gaudyn/spread-operator-and-rest-parameter-in-javascript-es6-4416a9f47e5e)  
[_L'opérateur de propagation et le paramètre de repos sont écrits comme trois points consécutifs (…). Ont-ils autre chose en commun…_medium.com](https://medium.com/@aska.gaudyn/spread-operator-and-rest-parameter-in-javascript-es6-4416a9f47e5e)[**Un aperçu des itérateurs JavaScript**](https://medium.freecodecamp.org/javascript-iterators-17ab32c3cae7)  
[_La différence entre les boucles for, for…in et for…of_medium.freecodecamp.org](https://medium.freecodecamp.org/javascript-iterators-17ab32c3cae7)