---
title: Tutoriel sur les tableaux d'objets JavaScript – Comment créer, mettre à jour
  et parcourir des objets en utilisant les méthodes de tableau JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-14T11:48:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-of-objects-tutorial-how-to-create-update-and-loop-through-objects-using-js-array-methods
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/js-tutorial-cover.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: loop
  slug: loop
- name: object
  slug: object
seo_title: Tutoriel sur les tableaux d'objets JavaScript – Comment créer, mettre à
  jour et parcourir des objets en utilisant les méthodes de tableau JS
seo_desc: 'By Ondrej Polesny

  On average I work with JSON data 18 times a week. And I still need to google for
  specific ways to manipulate them almost every time. What if there was an ultimate
  guide that could always give you the answer?

  In this article, I''ll sh...'
---

Par Ondrej Polesny

En moyenne, je travaille avec des données JSON 18 fois par semaine. Et je dois encore chercher sur Google des moyens spécifiques de les manipuler presque à chaque fois. Et si il existait un guide ultime qui pourrait toujours vous donner la réponse ?

Dans cet article, je vais vous montrer les bases du travail avec les tableaux d'objets en JavaScript.

Si vous avez déjà travaillé avec une structure JSON, vous avez travaillé avec des objets JavaScript. Tout simplement. JSON signifie JavaScript Object Notation. 

Créer un objet est aussi simple que ceci :

```js
{
  "color": "purple",
  "type": "minivan",
  "registration": new Date('2012-02-03'),
  "capacity": 7
}
```

Cet objet représente une voiture. Il peut y avoir de nombreux types et couleurs de voitures, chaque objet représente alors une voiture spécifique.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/purple.png)

Maintenant, la plupart du temps, vous obtenez des données comme celles-ci à partir d'un service externe. Mais parfois, vous devez créer des objets et leurs tableaux manuellement. Comme je l'ai fait lorsque je créais cette boutique en ligne :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/categories.jpg)

Considérant que chaque élément de la liste de catégories ressemble à ceci en HTML :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/code.jpg)

Je ne voulais pas avoir ce code répété 12 fois, ce qui le rendrait difficile à maintenir.

## Créer un tableau d'objets

Mais revenons aux voitures. Jetons un coup d'œil à cet ensemble de voitures :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/cars.jpg)

Nous pouvons le représenter comme un tableau de cette manière :

```js
let cars = [
  {
    "color": "purple",
    "type": "minivan",
    "registration": new Date('2017-01-03'),
    "capacity": 7
  },
  {
    "color": "red",
    "type": "station wagon",
    "registration": new Date('2018-03-03'),
    "capacity": 5
  },
  {
    ...
  },
  ...
]
```

Les tableaux d'objets ne restent pas les mêmes tout le temps. Nous devons presque toujours les manipuler. Alors, jetons un coup d'œil à la façon dont nous pouvons ajouter des objets à un tableau déjà existant.

### Ajouter un nouvel objet au début - Array.unshift

![Image](https://www.freecodecamp.org/news/content/images/2020/05/beginning.jpg)

Pour ajouter un objet à la première position, utilisez `Array.unshift`.

```js
let car = {
  "color": "red",
  "type": "cabrio",
  "registration": new Date('2016-05-02'),
  "capacity": 2
}
cars.unshift(car);
```

### Ajouter un nouvel objet à la fin - Array.push

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ending.jpg)

Pour ajouter un objet à la dernière position, utilisez `Array.push`.

```js
let car = {
  "color": "red",
  "type": "cabrio",
  "registration": new Date('2016-05-02'),
  "capacity": 2
}
cars.push(car);
```

### Ajouter un nouvel objet au milieu - Array.splice

![Image](https://www.freecodecamp.org/news/content/images/2020/05/middle.jpg)

Pour ajouter un objet au milieu, utilisez `Array.splice`. Cette fonction est très pratique car elle peut également supprimer des éléments. Faites attention à ses paramètres :

```js
Array.splice(
  {index où commencer},
  {nombre d'éléments à supprimer},
  {éléments à ajouter}
);
```

Donc, si nous voulons ajouter la Volkswagen Cabrio rouge à la cinquième position, nous utiliserions :

```js
let car = {
  "color": "red",
  "type": "cabrio",
  "registration": new Date('2016-05-02'),
  "capacity": 2
}
cars.splice(4, 0, car);
```

## Parcourir un tableau d'objets

Permettez-moi de vous poser une question ici : Pourquoi voulez-vous parcourir un tableau d'objets ? La raison pour laquelle je pose cette question est que le parcours n'est presque jamais la cause principale de ce que nous voulons accomplir. 

JavaScript fournit de nombreuses fonctions qui peuvent résoudre votre problème sans avoir à implémenter la logique dans un cycle général. Jetons un coup d'œil.

### Trouver un objet dans un tableau par ses valeurs - Array.find

Supposons que nous voulons trouver une voiture qui est rouge. Nous pouvons utiliser la fonction `Array.find`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/cars-colorred.jpg)

```js
let car = cars.find(car => car.color === "red");
```

Cette fonction retourne le premier élément correspondant :

```js
console.log(car);
// sortie :
// {
//   color: 'red',
//   type: 'station wagon',
//   registration: 'Sat Mar 03 2018 01:00:00 GMT+0100 (GMT+01:00)',
//   capacity: 5
// }
```

Il est également possible de rechercher plusieurs valeurs :

`let car = cars.find(car => car.color === "red" && car.type === "cabrio");`

Dans ce cas, nous obtiendrons la dernière voiture de la liste.

### Obtenir plusieurs éléments d'un tableau qui correspondent à une condition - Array.filter

La fonction `Array.find` retourne uniquement un objet. Si nous voulons obtenir toutes les voitures rouges, nous devons utiliser `Array.filter`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/cars-colorred2.jpg)

```js
let redCars = cars.filter(car => car.color === "red");
console.log(redCars);
// sortie :
// [
//   {
//     color: 'red',
//     type: 'station wagon',
//     registration: 'Sat Mar 03 2018 01:00:00 GMT+0100 (GMT+01:00)',
//     capacity: 5
//   },
//   {
//     color: 'red',
//     type: 'cabrio',
//     registration: 'Sat Mar 03 2012 01:00:00 GMT+0100 (GMT+01:00)',
//     capacity: 2
//   }
// ]
```

### Transformer les objets d'un tableau - Array.map

C'est quelque chose dont nous avons très souvent besoin. Transformer un tableau d'objets en un tableau d'objets différents. C'est un travail pour `Array.map`. Supposons que nous voulons classer nos voitures en trois groupes en fonction de leur taille.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/cars-sizes.jpg)

```js
let sizes = cars.map(car => {
  if (car.capacity <= 3){
    return "small";
  }
  if (car.capacity <= 5){
    return "medium";
  }
  return "large";
});
console.log(sizes);
// sortie :
// ['large','medium','medium', ..., 'small']
```

Il est également possible de créer un nouvel objet si nous avons besoin de plus de valeurs :

```js
let carsProperties = cars.map(car => {
 let properties = {
   "capacity": car.capacity,
   "size": "large"
 };
 if (car.capacity <= 5){
   properties['size'] = "medium";
 }
 if (car.capacity <= 3){
   properties['size'] = "small";
 }
 return properties;
});
console.log(carsProperties);
// sortie :
// [
//   { capacity: 7, size: 'large' },
//   { capacity: 5, size: 'medium' },
//   { capacity: 5, size: 'medium' },
//   { capacity: 2, size: 'small' },
//   ...
// ]
```

### Ajouter une propriété à chaque objet d'un tableau - Array.forEach

Mais que faire si nous voulons également la taille de la voiture ? Dans ce cas, nous pouvons enrichir l'objet avec une nouvelle propriété `size`. C'est un bon cas d'utilisation pour la fonction `Array.forEach`.

```js
cars.forEach(car => {
 car['size'] = "large";
 if (car.capacity <= 5){
   car['size'] = "medium";
 }
 if (car.capacity <= 3){
   car['size'] = "small";
 }
});
```

### Trier un tableau par une propriété - Array.sort

Lorsque nous avons terminé la transformation des objets, nous devons généralement les trier d'une manière ou d'une autre. 

Typiquement, le tri est basé sur une valeur de propriété que chaque objet possède. Nous pouvons utiliser la fonction `Array.sort`, mais nous devons fournir une fonction qui définit le mécanisme de tri. 

Supposons que nous voulons trier les voitures en fonction de leur capacité par ordre décroissant.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/cars-sort.jpg)

```js
let sortedCars = cars.sort((c1, c2) => (c1.capacity < c2.capacity) ? 1 : (c1.capacity > c2.capacity) ? -1 : 0);
console.log(sortedCars);
// sortie :
// [
//   {
//     color: 'purple',
//     type: 'minivan',
//     registration: 'Wed Feb 01 2017 00:00:00 GMT+0100 (GMT+01:00)',
//     capacity: 7
//   },
//   {
//     color: 'red',
//     type: 'station wagon',
//     registration: 'Sat Mar 03 2018 01:00:00 GMT+0100 (GMT+01:00)',
//     capacity: 5
//   },
//   ...
// ]
```

La fonction `Array.sort` compare deux objets et place le premier objet à la deuxième place si le résultat de la fonction de tri est positif. Vous pouvez donc considérer la fonction de tri comme si c'était une question : Le premier objet doit-il être placé à la deuxième place ?

![Image](https://www.freecodecamp.org/news/content/images/2020/05/sort.png)

Assurez-vous de toujours ajouter le cas pour zéro lorsque la valeur comparée des deux objets est la même afin d'éviter des échanges inutiles.

### Vérifier si les objets d'un tableau remplissent une condition - Array.every, Array.includes

`Array.every` et `Array.some` sont pratiques lorsque nous devons simplement vérifier chaque objet pour une condition spécifique. 

Avons-nous une cabrio rouge dans la liste des voitures ? Toutes les voitures sont-elles capables de transporter au moins 4 personnes ? Ou plus centré sur le web : Y a-t-il un produit spécifique dans le panier d'achat ?

```js
cars.some(car => car.color === "red" && car.type === "cabrio");
// sortie : true

cars.every(car => car.capacity >= 4);
// sortie : false
```

Vous vous souvenez peut-être de la fonction `Array.includes` qui est similaire à `Array.some`, mais qui fonctionne uniquement pour les types primitifs.

## Résumé

Dans cet article, nous avons passé en revue les fonctions de base qui vous aident à créer, manipuler, transformer et parcourir des tableaux d'objets. Elles devraient couvrir la plupart des cas auxquels vous serez confronté.

Si vous avez un cas d'utilisation qui nécessite des fonctionnalités plus avancées, consultez [ce guide détaillé sur les tableaux](https://www.freecodecamp.org/news/data-structures-101-arrays-a-visual-introduction-for-beginners-7f013bcc355a/) ou visitez la [référence W3 schools](https://www.w3schools.com/Jsref/jsref_obj_array.asp).

Ou [contactez-moi](https://twitter.com/ondrabus) et je préparerai un autre article :-)