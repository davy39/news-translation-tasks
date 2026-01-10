---
title: Comment écrire du code JavaScript plus simple
subtitle: ''
author: Temitope Oyedele
co_authors: []
series: null
date: '2023-03-10T18:57:42.000Z'
originalURL: https://freecodecamp.org/news/simplify-javascript-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/10-Ways-to-Simplify-Your-Javascript-Code--1-.png
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
seo_title: Comment écrire du code JavaScript plus simple
seo_desc: 'As developers, writing clean and maintainable code is the goal. But sometimes,
  this is hard to achieve when we have a large and bulky codebase that can become
  complex and difficult to manage.

  One way to avoid this is to simplify your code. This can h...'
---

En tant que développeurs, écrire du code propre et maintenable est l'objectif. Mais parfois, cela est difficile à atteindre lorsque nous avons une base de code volumineuse et encombrante qui peut devenir complexe et difficile à gérer.

Une façon d'éviter cela est de simplifier votre code. Cela peut aider à améliorer sa lisibilité, son efficacité et sa maintenabilité.

Cet article discutera de dix façons de simplifier votre code JavaScript, le rendant plus lisible et maintenable. Commençons tout de suite !

## Utiliser les fonctions fléchées

L'utilisation des fonctions fléchées est une manière abrégée de créer des fonctions en JavaScript. Elles simplifient votre code en réduisant le code standard nécessaire pour définir une fonction.

Par exemple, au lieu d'utiliser le mot-clé function pour définir une fonction comme ceci :

```javascript
function greeings(name){ 
console.log(Hello, ${name}!);
}
```

Vous pouvez utiliser une fonction fléchée comme ceci :

```javascript
const greeting = name => console.log(`Hello, ${name}!`);
```

En plus d'avoir une syntaxe plus courte, les fonctions fléchées peuvent rendre votre code plus concis, plus facile à lire et moins sujet aux erreurs. Cela en fait un meilleur choix que l'utilisation du mot-clé function.

## Utiliser des noms de variables descriptifs

L'utilisation de noms de variables descriptifs peut rendre votre code plus lisible et plus facile à comprendre. Cela est bien mieux que d'utiliser des noms de variables à une seule lettre ou des abréviations, car il peut ne pas être immédiatement clair pour quelqu'un d'autre lisant votre code ce que ces variables signifient.

Par exemple, au lieu d'utiliser :

```javascript
const x = 10;
```

Utilisez ceci :

```javascript
const numberOfItems = 10;
```

`numberOfItems` est beaucoup plus descriptif que `x` et vous aidera (ou d'autres développeurs regardant votre code) à comprendre ce qu'il fait.

## Utiliser la programmation fonctionnelle

La programmation fonctionnelle privilégie l'utilisation de fonctions pures et de structures de données immuables. L'utilisation de techniques de programmation fonctionnelle peut grandement simplifier votre code et réduire le risque de bugs et d'effets secondaires.

Par exemple, au lieu de modifier un tableau en place :

```
const numbers = [1, 2, 3];
numbers.push(4);
```

Vous pouvez utiliser l'opérateur de décomposition pour créer un nouveau tableau :

```
const numbers = [1, 2, 3];
const newNumbers = [...numbers, 4];
```

L'utilisation de l'opérateur de décomposition vous aide à prévenir les effets secondaires inattendus et rend votre code plus prévisible.

Lorsque vous modifiez la fonction en place, vous changez le tableau ou l'objet original. Si une autre partie de votre code dépend de ce tableau ou de cet objet, cela peut entraîner des bugs et des comportements inattendus.

D'autre part, l'utilisation de l'opérateur de décomposition crée un nouveau tableau ou objet, laissant l'original intact. Cela rend votre code plus prévisible et plus facile à comprendre.

## Éviter la imbrication de code

L'imbrication de code peut le rendre difficile à lire et à comprendre. Une meilleure façon est d'essayer d'aplatir votre code autant que possible. Vous pouvez le faire en utilisant des retours précoces, des opérateurs ternaires et la composition de fonctions.

Par exemple, au lieu d'imbriquer des instructions if :

```
if (condition1) {
  if (condition2) {
    // code
  }
}
```

Utilisez des retours précoces :

```
if (condition1) {
  return;
}
if (condition2) {
  return;
}
// code
```

L'utilisation de retours précoces ici rend notre code plus lisible et plus facile à comprendre car il décompose chaque condition en une instruction if séparée, et retourne tôt si une condition échoue.

Les retours précoces peuvent également augmenter l'efficacité de votre code en empêchant des calculs inutiles.

## Utiliser des paramètres par défaut

L'utilisation de paramètres par défaut vous permet de spécifier une valeur par défaut pour un paramètre de fonction. Cela peut simplifier votre code en réduisant le nombre d'instructions conditionnelles que vous devez écrire.

Par exemple, au lieu d'utiliser une logique conditionnelle pour définir une valeur par défaut :

```
function greet(name) {
  if (!name) {
    name = 'World';
  }
  console.log(`Hello, ${name}!`);
}
```

Vous pouvez utiliser un paramètre par défaut :

```
function greet(name = 'World') {
  console.log(`Hello, ${name}!`);
}
```

L'utilisation d'un paramètre par défaut vous fournit une manière simple de définir des valeurs par défaut. Mais pas seulement cela, cela rend votre code plus flexible, moins sujet aux erreurs, et également plus facile à comprendre.

## Utiliser la déstructuration

La déstructuration vous permet d'extraire des valeurs des tableaux et des objets et de les assigner à des variables. Faire cela peut rendre votre code plus concis et plus facile à lire.

Par exemple, au lieu d'accéder directement aux propriétés d'un objet comme ceci :

```
const person = { name: 'John', age: 30 };
const name = person.name;
const age = person.age;
```

Vous pouvez utiliser la déstructuration :

```javascript
const { name, age } = { name: 'John', age: 30 };
```

L'utilisation de la déstructuration serait bien meilleure que l'accès aux propriétés d'un objet car elle vous aide à comprendre rapidement le but du code, surtout lorsque vous travaillez avec des structures de données complexes. Elle aide également à réduire la quantité de code que vous devez écrire, offre de la flexibilité, résulte en un code plus propre et aide également à éviter les conflits de noms.

## Utiliser les Promesses

Les Promesses vous permettent d'écrire du code asynchrone de manière plus lisible et prévisible. Elles simplifient votre code en évitant le besoin de callbacks et en vous permettant d'enchaîner des opérations asynchrones ensemble.

Par exemple, au lieu d'imbriquer des callbacks :

```
function getUserData(userId, callback) {
  getUser(userId, function(user) {
    getPosts(user, function(posts) {
      getComments(posts, function(comments) {
        callback(comments);
      });
    });
  });
}
```

Vous pouvez utiliser des promesses comme ceci :

```
function getUserData(userId) {
  return getUser(userId)
    .then(user => getPosts(user))
    .then(posts => getComments(posts));
}
```

L'utilisation de promesses au lieu d'imbriquer des callbacks peut rendre le code plus concis et plus facile à lire, surtout lorsque vous travaillez avec des opérations asynchrones complexes.

## Utiliser les méthodes de tableau

JavaScript dispose de nombreuses méthodes intégrées pour manipuler les tableaux, telles que `map`, `filter`, `reduce` et `forEach`. L'utilisation de ces méthodes peut rendre votre code plus concis et plus facile à lire.

Par exemple, au lieu d'utiliser une boucle for pour itérer sur un tableau :

```
const numbers = [1, 2, 3];
for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
```

Vous pouvez utiliser la méthode `forEach` :

```
const numbers = [1, 2, 3];
numbers.forEach(number => console.log(number));
```

L'utilisation de méthodes de tableau plutôt que de boucles for traditionnelles peut rendre votre code plus concis, lisible et modulaire, tout en offrant une meilleure gestion des erreurs et en soutenant les techniques de programmation fonctionnelle.

## Utiliser les méthodes d'objet

Les objets JavaScript fournissent une variété de méthodes intégrées, telles que `Object.keys`, `Object.values` et `Object.entries`. Ces méthodes peuvent simplifier votre code en réduisant le besoin de boucles et de conditionnelles.

Par exemple, au lieu d'utiliser une boucle for pour itérer sur un objet :

```
const person = { name: 'John', age: 30 };
for (const key in person) {
  console.log(`${key}: ${person[key]}`);
}
```

Vous pouvez utiliser la méthode `Object.entries` :

```
const person = { name: 'John', age: 30 };
Object.entries(person).forEach(([key, value]) => console.log(`${key}: ${value}`));
```

Tout comme les méthodes de tableau, l'utilisation de méthodes d'objet peut rendre votre code plus concis, lisible et modulaire.

## Utiliser des bibliothèques et des frameworks

JavaScript dispose d'une grande variété de modules et de frameworks qui peuvent vous aider à créer un code plus simple avec moins de code standard.

Des exemples incluent React pour construire des interfaces utilisateur, Lodash pour la programmation fonctionnelle, et Moment.js pour travailler avec des dates et des heures.

Vous pourriez envisager d'utiliser un framework/bibliothèque lorsque :

* Lorsque vous souhaitez construire une application complexe avec des fonctionnalités qui peuvent être réalisées avec une bibliothèque ou un framework.
* Lorsque vous avez un délai serré et devez livrer votre projet rapidement.
* Lorsque vous souhaitez améliorer la qualité de votre code et réduire les coûts de maintenance au fil du temps.

D'autre part, vous pourriez également vouloir éviter d'utiliser un framework/bibliothèque lorsque :

* Lorsque les exigences de votre projet sont simples et ne nécessitent aucun outil externe.
* Lorsque vous souhaitez avoir le contrôle sur votre code et éviter les dépendances aux outils externes.

## Conclusion

Simplifier votre code peut le rendre plus lisible et maintenable. En suivant ces conseils, vous pouvez écrire un code qui est plus facile à comprendre et plus efficace.

Quels autres conseils suggéreriez-vous ? N'oubliez pas de partager si vous avez trouvé cela utile.