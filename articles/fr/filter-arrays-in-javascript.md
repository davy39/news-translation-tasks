---
title: Comment filtrer un tableau en JavaScript – Filtrer des tableaux et des objets
  en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-17T01:13:56.000Z'
originalURL: https://freecodecamp.org/news/filter-arrays-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template--2-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment filtrer un tableau en JavaScript – Filtrer des tableaux et des
  objets en JS
seo_desc: 'When building a dynamic and interactive program, you may need to add some
  interactive features. For example, where a user clicks a button to filter through
  a long list of items.

  You may also need to manipulate a large array of data to return only ite...'
---

Lors de la création d'un programme dynamique et interactif, vous devrez peut-être ajouter des fonctionnalités interactives. Par exemple, lorsqu'un utilisateur clique sur un bouton pour filtrer une longue liste d'éléments.

Vous devrez peut-être également manipuler un grand tableau de données pour ne retourner que les éléments qui correspondent à vos conditions spécifiées.

Dans cet article, vous apprendrez comment filtrer un tableau en JavaScript en utilisant deux approches majeures. Vous apprendrez également comment filtrer un tableau d'objets et retourner un nouveau tableau d'éléments filtrés.

## Comment filtrer un tableau avec une boucle `for`

Avant l'introduction d'ES6 en 2015, de nombreux développeurs s'appuyaient sur la méthode de boucle for pour gérer presque toutes les manipulations de tableaux. Mais le code peut devenir assez long et difficile à comprendre, ce qui a conduit à la publication de nombreuses méthodes JavaScript individuelles comme la méthode `filter()` (que vous apprendrez bientôt).

Mais d'abord, pour être complet, nous verrons comment le faire en utilisant des boucles for.

Supposons que vous avez un tableau d'objets qui contient les détails des utilisateurs comme le nom, l'âge et la profession. Vous pouvez décider de filtrer les utilisateurs dont l'âge correspond à une condition spécifique.

```js
let users = [
    { name: 'John', age: 25, occupation: 'gardener' },
    { name: 'Lenny', age: 51, occupation: 'programmer' },
    { name: 'Andrew', age: 43, occupation: 'teacher' },
    { name: 'Peter', age: 81, occupation: 'teacher' },
    { name: 'Anna', age: 47, occupation: 'programmer' },
    { name: 'Albert', age: 76, occupation: 'programmer' },
]
```

Vous pouvez maintenant filtrer le tableau d'objets en utilisant l'âge pour retourner un nouveau tableau dont l'`age` est supérieur à `40` et dont la `profession` est égale à `programmer` :

```js
let filteredUsers = [];
for (let i= 0; i<users.length; i++) {
    if (users[i].age > 40 && users[i].occupation === 'programmer' ) {
        filteredUsers = [...filteredUsers, users[i]];
    }
}
console.log(filteredUsers);
```

Cela retournera un tableau de trois utilisateurs qui répondent à la condition spécifiée.

![](https://paper-attachments.dropboxusercontent.com/s_A2A56A7C05733A13745945CF4C6950EBC758CD93042A33CBFFD44710AB9E7883_1676527392206_image.png align="left")

Maintenant, cela fonctionne bien. Mais une meilleure façon de filtrer un tableau est d'utiliser la méthode filter() d'ES6.

## Comment filtrer un tableau avec la méthode `filter()`

La méthode `filter()` est une méthode ES6 qui fournit une syntaxe plus propre pour filtrer un tableau. Elle retourne de nouveaux éléments dans un nouveau tableau sans altérer le tableau original.

```js
// Syntaxe
myArray.filter(callbackFn)
```

Dans la fonction de rappel, vous avez accès à chaque élément, à l'`index` et au tableau original lui-même :

```js
myArray.filter((element, index, array) => { /* ... */ })
```

Effectuons maintenant le même exemple en filtrant l'utilisateur par son `age` et sa `profession` :

```js
let filteredUsers = users.filter((user) => {
    return user.age > 40 && user.occupation === 'programmer';
});

console.log(filteredUsers);
```

Cela retournera la même sortie, mais vous remarquerez que votre code est assez propre. Il est également important de savoir que vous pouvez réécrire le code ci-dessus en une seule ligne et supprimer l'instruction `return` :

```js
let filteredUsers = users.filter(user => user.age > 40 && user.occupation === 'programmer');
console.log(filteredUsers);
```

Les deux blocs de code retourneront les utilisateurs filtrés :

![](https://paper-attachments.dropboxusercontent.com/s_A2A56A7C05733A13745945CF4C6950EBC758CD93042A33CBFFD44710AB9E7883_1676527392206_image.png align="left")

La méthode filter facilite l'exécution de plus d'opérations directement sans créer autant de variables car elle est excellente pour l'enchaînement avec d'autres méthodes fonctionnelles.

Par exemple, vous pouvez trier le tableau filtré et retourner un tableau contenant uniquement leurs noms :

```js
let filteredUserNames = users.filter(user => user.age > 40 && user.occupation === 'programmer')
    .sort((a, b) => a.age - b.age)
    .map(user => user.name);

console.log(filteredUserNames); // ['Anna', 'Lenny', 'Albert']
```

Il y a plus à filtrer les tableaux en JavaScript avec la méthode filter() de JavaScript. Vous pouvez en savoir plus sur la méthode filter de JavaScript dans ce [Tutoriel JavaScript Array.filter()](https://www.freecodecamp.org/news/javascript-array-filter-tutorial-how-to-iterate-through-elements-in-an-array/), et vous pouvez également apprendre la [différence entre les méthodes find() et filter() de JavaScript ici](https://www.freecodecamp.org/news/find-vs-filter-javascript/).

## Comment filtrer un objet en JavaScript

Les objets JavaScript ne sont pas itérables comme les tableaux ou les chaînes de caractères (vous ne pouvez pas les parcourir en boucle). Cela signifie que vous ne pouvez pas utiliser `filter()`, la méthode de boucle for ou toute méthode d'itération directement sur un objet. Alors, comment filtrer un objet en JavaScript ?

Vous pouvez le faire en convertissant l'objet en tableau en utilisant l'une des méthodes statiques d'objet telles que `Object.keys()`, `Object.values()` ou `Object.entries()`. Vous pouvez ensuite utiliser la méthode filter() pour filtrer le tableau et retourner un nouveau tableau d'éléments filtrés.

Supposons que vous avez un objet qui contient les détails des utilisateurs comme le nom, l'âge et la profession. Ces méthodes statiques d'objet peuvent retourner les clés, les valeurs ou chaque paire clé-valeur sous forme de tableau.

```js
const userDetails = {
    firstName: "Jane",
    lastName: "Daniels",
    userName: "jane.daniels",
    email: "jane.daniels@example.com",
    comapny: "Example Inc.",
    address: "1234 Example Street",
    age : 25,
    hobby: "Singing"
};

let keysArray = Object.keys(userDetails);

console.log(keysArray);
```

Cela retournera un tableau des clés de l'objet :

```js
['firstName', 'lastName', 'userName', 'email', 'comapny', 'address', 'age', 'hobby']
```

Vous pouvez maintenant utiliser la méthode filter() pour filtrer le tableau et retourner un nouveau tableau d'éléments filtrés :

```js
let filteredKeys = keysArray.filter(key => key.length > 5);

console.log(filteredKeys);
```

Cela retournera un tableau de clés dont la longueur est supérieure à 5 :

```js
['firstName', 'lastName', 'userName', 'comapny', 'address', 'hobby']
```

Mais définitivement, vous voudrez effectuer une opération de filtrage plus utile. Par exemple, vous pouvez filtrer les paires clé-valeur de notre objet qui incluent un nom à partir d'un grand objet. Ensuite, vous pouvez d'abord obtenir les clés, les filtrer et utiliser la méthode `reduce()` pour `réduire` les clés filtrées en un objet avec les clés filtrées et leurs valeurs :

```js
const userDetails = {
    firstName: "Jane",
    lastName: "Daniels",
    userName: "jane.daniels",
    email: "jane.daniels@example.com",
    comapny: "Example Inc.",
    address: "1234 Example Street",
    age : 25,
    hobby: "Singing"
};

const userNames = Object.keys(userDetails)
    .filter((key) => key.includes("Name"))
    .reduce((object, key) => {
        return Object.assign(object, {
          [key]: userDetails[key]
        });
  }, {});

console.log(userNames);
```

Cela retournera un objet avec les clés filtrées et leurs valeurs :

```js
{
    firstName: "Jane",
    lastName: "Daniels",
    userName: "jane.daniels"
}
```

## Conclusion

Dans cet article, vous avez appris comment filtrer un tableau en JavaScript en utilisant la boucle `for` et la méthode `filter()`. La méthode `filter()` offre une meilleure syntaxe pour filtrer les tableaux en JavaScript.

Vous avez également appris comment filtrer un objet en JavaScript en le convertissant en tableau et en utilisant la méthode filter().

Merci d'avoir lu, et amusez-vous bien à coder !

Vous pouvez accéder à plus de 188 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.