---
title: Tutoriel sur les méthodes de tableau JavaScript – Les méthodes les plus utiles
  expliquées avec des exemples
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-02-17T21:04:00.000Z'
originalURL: https://freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods
coverImage: https://cdn-media-2.freecodecamp.org/w1280/602b49ef0a2838549dcc6285.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Tutoriel sur les méthodes de tableau JavaScript – Les méthodes les plus
  utiles expliquées avec des exemples
seo_desc: 'If you''re a JavaScript developer and want to improve your coding, then
  you should be familiar with the most commonly used ES5 and ES6+ array methods.

  These methods make coding a lot easier and also make your code look clean and easy
  to understand.

  So...'
---

Si vous êtes un développeur JavaScript et que vous souhaitez améliorer votre codage, alors vous devriez être familier avec les méthodes de tableau ES5 et ES6+ les plus couramment utilisées.

Ces méthodes rendent le codage beaucoup plus facile et rendent également votre code propre et facile à comprendre.

Dans cet article, nous allons explorer certaines des méthodes de tableau les plus populaires et largement utilisées. Alors, commençons.

## La méthode Array.forEach

La méthode `Array.forEach` a la syntaxe suivante :

```js
Array.forEach(callback(currentValue [, index [, array]])[, thisArg]);
```

La méthode `forEach` exécute une fonction fournie une fois pour chaque élément du tableau.

Jetez un œil au code ci-dessous :

```js
const months = ['January', 'February', 'March', 'April'];

months.forEach(function(month) {
  console.log(month);
});

/* output

January
February
March
April

*/

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/bGBqzOw?editors=0012).

Ici, à l'intérieur de la fonction de rappel de la boucle `forEach`, chaque élément du tableau est automatiquement passé comme premier paramètre de la fonction.

Le code équivalent de la boucle for pour l'exemple ci-dessus ressemble à ceci :

```js
const months = ['January', 'February', 'March', 'April'];

for(let i = 0; i < months.length; i++) {
  console.log(months[i]);
}

/* output

January
February
March
April

*/

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/abBJXMR?editors=0012).

La chose à garder à l'esprit est que la méthode `forEach` ne retourne aucune valeur.

Jetez un œil au code ci-dessous :

```js
const months = ['January', 'February', 'March', 'April'];
const returnedValue = months.forEach(function (month) {
  return month;
});

console.log('returnedValue: ', returnedValue); // undefined

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/PobpxGb?editors=0012).

> _Notez que_ `_forEach_` _est uniquement utilisé pour parcourir le tableau et effectuer un traitement ou une journalisation. Il ne retourne aucune valeur, même si vous retournez explicitement une valeur depuis la fonction de rappel (cela signifie que la valeur retournée est_ `undefined` _dans l'exemple ci-dessus)._

Dans tous les exemples ci-dessus, nous avons utilisé uniquement le premier paramètre de la fonction de rappel. Mais la fonction de rappel reçoit également deux paramètres supplémentaires, qui sont :

* index - l'index de l'élément qui est actuellement en cours d'itération
* array - tableau original que nous parcourons

```js
const months = ['January', 'February', 'March', 'April'];

months.forEach(function(month, index, array) {
  console.log(month, index, array);
});

/* output

January 0 ["January", "February", "March", "April"]
February 1 ["January", "February", "March", "April"]
March 2 ["January", "February", "March", "April"]
April 3 ["January", "February", "March", "April"]

*/

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/OJbpqJR?editors=0012).

Selon les besoins, vous pouvez trouver utile d'utiliser les paramètres `index` et `array`.

### Avantages de l'utilisation de forEach au lieu d'une boucle for

* L'utilisation d'une boucle `forEach` rend votre code plus court et plus facile à comprendre
* Lorsque vous utilisez une boucle `forEach`, nous n'avons pas besoin de suivre le nombre d'éléments disponibles dans le tableau. Cela évite donc la création d'une variable de compteur supplémentaire.
* L'utilisation d'une boucle `forEach` facilite le débogage du code car il n'y a pas de variables supplémentaires pour parcourir le tableau
* La boucle `forEach` s'arrête automatiquement lorsque tous les éléments du tableau ont fini d'être itérés.

### Support des navigateurs

* Tous les navigateurs modernes et Internet Explorer (IE) version 9 et supérieures
* Microsoft Edge version 12 et supérieures

## La méthode Array.map

La méthode Array map est la méthode de tableau la plus utile et la plus largement utilisée parmi toutes les autres méthodes.

La méthode `Array.map` a la syntaxe suivante :

```js
Array.map(function callback(currentValue[, index[, array]]) {
    // Retourne l'élément pour new_array
}[, thisArg])
```

La méthode `map` exécute une fonction fournie une fois pour chaque élément du tableau et elle **retourne un nouveau tableau transformé.**

Jetez un œil au code ci-dessous :

```js
const months = ['January', 'February', 'March', 'April'];
const transformedArray = months.map(function (month) {
  return month.toUpperCase();
});

console.log(transformedArray); // ["JANUARY", "FEBRUARY", "MARCH", "APRIL"]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/ExNWOyr?editors=0012).

Dans le code ci-dessus, à l'intérieur de la fonction de rappel, nous convertissons chaque élément en majuscules et le retournons.

Le code équivalent de la boucle for pour l'exemple ci-dessus ressemble à ceci :

```js
const months = ['January', 'February', 'March', 'April'];
const converted = [];

for(let i = 0; i < months.length; i++) {
 converted.push(months[i].toUpperCase());
};

console.log(converted); // ["JANUARY", "FEBRUARY", "MARCH", "APRIL"]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/gOLmyQQ?editors=0012).

L'utilisation de `map` permet d'éviter de créer un tableau `converted` séparé au préalable pour stocker les éléments convertis. Cela permet donc d'économiser de l'espace mémoire et le code semble également beaucoup plus propre en utilisant `map`, comme ceci :

```js
const months = ['January', 'February', 'March', 'April'];

console.log(months.map(function (month) {
  return month.toUpperCase();
})); // ["JANUARY", "FEBRUARY", "MARCH", "APRIL"]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/oNYZVoX?editors=0012).

Notez que la méthode `map` retourne un nouveau tableau qui est de la même longueur exacte que le tableau original.

La différence entre les méthodes `forEach` et `map` est que `forEach` est uniquement utilisé pour la boucle et ne retourne rien. En revanche, la méthode `map` retourne un nouveau tableau qui est de la même longueur exacte que le tableau original.

De plus, notez que `map` ne modifie pas le tableau original mais retourne un nouveau tableau.

Jetez un œil au code ci-dessous :

```js
const users = [
  {
    first_name: 'Mike',
    last_name: 'Sheridan'
  },
  {
    first_name: 'Tim',
    last_name: 'Lee'
  },
  {
    first_name: 'John',
    last_name: 'Carte'
  }
];

const usersList = users.map(function (user) {
  return user.first_name + ' ' + user.last_name;
});

console.log(usersList); // ["Mike Sheridan", "Tim Lee", "John Carte"]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/LYbWaxP?editors=0012).

Ici, en utilisant le tableau d'objets et les méthodes `map`, nous générons facilement un seul tableau avec le prénom et le nom de famille concaténés.

Dans le code ci-dessus, nous utilisons l'opérateur `+` pour concaténer deux valeurs. Mais il est beaucoup plus courant d'utiliser la syntaxe des littéraux de gabarit ES6 comme montré ci-dessous :

```js
const users = [
  {
    first_name: 'Mike',
    last_name: 'Sheridan'
  },
  {
    first_name: 'Tim',
    last_name: 'Lee'
  },
  {
    first_name: 'John',
    last_name: 'Carte'
  }
];

const usersList = users.map(function (user) {
  return `${user.first_name} ${user.last_name}`;
});

console.log(usersList); // ["Mike Sheridan", "Tim Lee", "John Carte"]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/abBJMqe?editors=0012).

La méthode `map` de tableau est également utile si vous souhaitez extraire uniquement des données spécifiques du tableau comme ceci :

```js
const users = [
  {
    first_name: 'Mike',
    last_name: 'Sheridan',
    age: 30
  },
  {
    first_name: 'Tim',
    last_name: 'Lee',
    age: 45
  },
  {
    first_name: 'John',
    last_name: 'Carte',
    age: 25
  }
];

const surnames = users.map(function (user) {
  return user.last_name;
});

console.log(surnames); // ["Sheridan", "Lee", "Carte"]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/rNWyRdR?editors=0012).

Dans le code ci-dessus, nous extrayons uniquement les noms de famille de chaque utilisateur et les stockons dans un tableau.

Nous pouvons même utiliser `map` pour générer un tableau avec un contenu dynamique comme montré ci-dessous :

```js
const users = [
  {
    first_name: 'Mike',
    location: 'London'
  },
  {
    first_name: 'Tim',
    location: 'US'
  },
  {
    first_name: 'John',
    location: 'Australia'
  }
];

const usersList = users.map(function (user) {
  return `${user.first_name} lives in ${user.location}`;
});

console.log(usersList); // ["Mike lives in London", "Tim lives in US", "John lives in Australia"]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/ExNWMOY?editors=0012).

Notez que dans le code ci-dessus, nous ne modifions pas le tableau `users` original. Nous créons un nouveau tableau avec un contenu dynamique car `map` retourne toujours un nouveau tableau.

### Avantages de l'utilisation de la méthode map

* Elle permet de générer rapidement un nouveau tableau sans modifier le tableau original
* Elle permet de générer un tableau avec un contenu dynamique basé sur chaque élément
* Elle nous permet d'extraire rapidement n'importe quel élément du tableau
* Elle génère un tableau de la même longueur exacte que le tableau original

**Support des navigateurs :**

* Tous les navigateurs modernes et Internet Explorer (IE) version 9 et supérieures
* Microsoft Edge version 12 et supérieures

## La méthode Array.find

La méthode `Array.find` a la syntaxe suivante :

```js
Array.find(callback(element[, index[, array]])[, thisArg])
```

> _La méthode_ `_find_` _retourne la_ `_valeur_` _du_ `_premier élément_` _du tableau qui satisfait la condition de test fournie._

La méthode `find` prend une fonction de rappel comme premier argument et exécute la fonction de rappel pour chaque élément du tableau. Chaque valeur d'élément de tableau est passée comme premier paramètre à la fonction de rappel.

Supposons que nous avons une liste d'employés comme ceci :

```js
const employees = [
 { name: "David Carlson", age: 30 },
 { name: "John Cena", age: 34 },
 { name: "Mike Sheridan", age: 25 },
 { name: "John Carte", age: 50 }
];
```

et nous voulons obtenir l'enregistrement de l'employé dont le nom est `John`. Dans ce cas, nous pouvons utiliser la méthode `find` comme montré ci-dessous :

```js
const employee = employees.find(function (employee) {
  return employee.name.indexOf('John') > -1;
});

console.log(employee); // { name: "John Cena", age: 34 }

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/VwmpVmL?editors=0011).

Même s'il y a `"John Carte"` dans la liste, la méthode `find` s'arrêtera lorsqu'elle trouvera la première correspondance. Elle ne retournera donc pas l'objet avec le nom `"John Carte".`

Le code équivalent de la boucle for pour l'exemple ci-dessus ressemble à ceci :

```js
const employees = [
 { name: "David Carlson", age: 30 },
 { name: "John Cena", age: 34 },
 { name: "Mike Sheridan", age: 25 },
 { name: "John Carte", age: 50 }
];

let user;

for(let i = 0; i < employees.length; i++) {
  if(employees[i].name.indexOf('John') > -1) {
    user = employees[i];
    break;
  }
}

console.log(user); // { name: "John Cena", age: 34 }

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/BaQWbeY?editors=0012).

Comme vous pouvez le voir, l'utilisation d'une boucle for normale rend le code beaucoup plus long et plus difficile à comprendre. Mais en utilisant la méthode `find`, nous pouvons écrire le même code de manière facile à comprendre.

### Avantages de l'utilisation de la méthode find

* Elle nous permet de trouver rapidement n'importe quel élément sans écrire beaucoup de code
* Elle arrête la boucle dès qu'elle trouve une correspondance, donc il n'y a pas besoin d'une instruction break supplémentaire

**Support des navigateurs :**

* Tous les navigateurs modernes sauf Internet Explorer (IE)
* Microsoft Edge version 12 et supérieures

## La méthode Array.findIndex

La méthode `Array.findIndex` a la syntaxe suivante :

```js
Array.findIndex(callback(element[, index[, array]])[, thisArg])
```

La méthode `findIndex` retourne l'**index** du premier élément du tableau **qui satisfait la condition de test fournie**. Sinon, elle retourne `-1`, indiquant qu'aucun élément n'a passé le test.

```js
const employees = [
  { name: 'David Carlson', age: 30 },
  { name: 'John Cena', age: 34 },
  { name: 'Mike Sheridan', age: 25 },
  { name: 'John Carte', age: 50 }
];

const index = employees.findIndex(function (employee) {
  return employee.name.indexOf('John') > -1;
});

console.log(index); // 1
```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/JjbWebQ?editors=0012).

Ici, nous obtenons le résultat **1** qui est l'index du premier objet avec le nom `John`. Notez que l'index commence à zéro.

Le code équivalent de la boucle for pour l'exemple ci-dessus ressemble à ceci :

```js
const employees = [
  { name: 'David Carlson', age: 30 },
  { name: 'John Cena', age: 34 },
  { name: 'Mike Sheridan', age: 25 },
  { name: 'John Carte', age: 50 }
];

let index = -1;

for(let i = 0; i < employees.length; i++) {
  if(employees[i].name.indexOf('John') > -1) {
    index = i;
    break;
  }
}

console.log(index); // 1

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/oNYZOgY?editors=0012).

### Avantages de l'utilisation de la méthode findIndex

* Elle nous permet de trouver rapidement l'index d'un élément sans écrire beaucoup de code
* Elle arrête la boucle dès qu'elle trouve une correspondance, donc il n'y a pas besoin d'une instruction break supplémentaire
* Nous pouvons trouver l'index en utilisant la méthode `find` du tableau également, mais l'utilisation de `findIndex` le rend facile et évite de créer des variables supplémentaires pour stocker l'index

**Support des navigateurs :**

* Tous les navigateurs modernes sauf Internet Explorer (IE)
* Microsoft Edge version 12 et supérieures

## La méthode Array.filter

La méthode `Array.filter` a la syntaxe suivante :

```js
Array.filter(callback(element[, index[, array]])[, thisArg])
```

La méthode `filter` retourne `un nouveau tableau` avec tous les éléments qui satisfont la condition de test fournie.

La méthode `filter` prend une fonction de rappel comme premier argument et exécute la fonction de rappel pour chaque élément du tableau. Chaque valeur d'élément de tableau est passée comme premier paramètre à la fonction de rappel.

```js
const employees = [
  { name: 'David Carlson', age: 30 },
  { name: 'John Cena', age: 34 },
  { name: 'Mike Sheridan', age: 25 },
  { name: 'John Carte', age: 50 }
];

const employee = employees.filter(function (employee) {
  return employee.name.indexOf('John') > -1;
});

console.log(employee); // [ { name: "John Cena", age: 34 }, { name: "John Carte", age: 50 }]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/yLVMQgE?editors=0011).

Comme on peut le voir dans le code ci-dessus, l'utilisation de `filter` permet de trouver tous les éléments du tableau qui correspondent à la condition de test spécifiée.

Ainsi, l'utilisation de `filter` ne s'arrête pas lorsqu'elle trouve une correspondance particulière, mais continue à vérifier les autres éléments du tableau qui correspondent à la condition. Ensuite, elle retourne tous les éléments correspondants du tableau.

> La principale différence entre `find` et `filter` est que `find` ne retourne que le premier élément correspondant du tableau, mais l'utilisation de `filter` retourne tous les éléments correspondants du tableau.

Notez que la méthode `filter` retourne toujours un tableau. Si aucun élément ne passe la condition de test, un tableau vide sera retourné.

Le code équivalent de la boucle for pour l'exemple ci-dessus ressemble à ceci :

```js
const employees = [
  { name: 'David Carlson', age: 30 },
  { name: 'John Cena', age: 34 },
  { name: 'Mike Sheridan', age: 25 },
  { name: 'John Carte', age: 50 }
];

let filtered = [];

for(let i = 0; i < employees.length; i++) {
 if(employees[i].name.indexOf('John') > -1) {
   filtered.push(employees[i]);
 }
}

console.log(filtered); // [ { name: "John Cena", age: 34 }, { name: "John Carte", age: 50 }]

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/qBqrwaq?editors=0011).

### Avantages de l'utilisation de la méthode filter

* Elle nous permet de trouver rapidement tous les éléments correspondants du tableau
* Elle retourne toujours un tableau même s'il n'y a pas de correspondance, donc elle évite d'écrire des conditions `if` supplémentaires
* Elle évite le besoin de créer une variable supplémentaire pour stocker les éléments filtrés

**Support des navigateurs :**

* Tous les navigateurs modernes et Internet Explorer (IE) version 9 et supérieures
* Microsoft Edge version 12 et supérieures

## La méthode Array.every

La méthode `Array.every` a la syntaxe suivante :

```js
Array.every(callback(element[, index[, array]])[, thisArg])
```

La méthode `every` teste si tous les éléments du tableau passent les conditions de test fournies et retourne une valeur booléenne `true` ou `false`.

Supposons que nous avons un tableau de nombres et que nous voulons vérifier si chaque élément du tableau est un nombre positif. Nous pouvons utiliser la méthode `every` pour y parvenir.

```js
let numbers = [10, -30, 20, 50];

let allPositive = numbers.every(function (number) {
  return number > 0;
});
console.log(allPositive); // false 

numbers = [10, 30, 20, 50];

allPositive = numbers.every(function (number) {
  return number > 0;
});
console.log(allPositive); // true

```

Imaginez que vous avez un formulaire d'inscription et que vous voulez vérifier si tous les champs obligatoires sont remplis ou non avant de soumettre le formulaire. Vous pouvez utiliser la méthode `every` pour vérifier facilement chaque valeur de champ.

```js
window.onload = function () {
  const form = document.getElementById('registration_form');
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const fields = ['first_name', 'last_name', 'email', 'city'];
    const allFieldsEntered = fields.every(function (fieldId) {
      return document.getElementById(fieldId).value.trim() !== '';
    });

    if (allFieldsEntered) {
      console.log('Tous les champs sont remplis');
      // Toutes les valeurs des champs sont saisies, soumettre le formulaire
    } else {
      alert('Veuillez remplir toutes les valeurs des champs.');
    }
  });
};

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/rNWyQwo?editors=0011).

Ici, à l'intérieur de la fonction de rappel de la méthode `every`, nous vérifions si chaque valeur de champ n'est pas vide et retournons une valeur booléenne.

Dans le code ci-dessus, la méthode `every` retourne `true` si, pour tous les éléments du tableau `fields`, la fonction de rappel retourne une valeur `true`.

Si la fonction de rappel retourne une valeur `false` pour l'un des éléments du tableau `fields`, alors la méthode `every` retournera `false` comme résultat.

### Avantages de l'utilisation de la méthode every

* Elle nous permet de vérifier rapidement si tous les éléments correspondent à certains critères sans écrire beaucoup de code

### Support des navigateurs :

* Tous les navigateurs modernes et Internet Explorer (IE) version 9 et supérieures
* Microsoft Edge version 12 et supérieures

## La méthode Array.some

La méthode `Array.some` a la syntaxe suivante :

```js
 Array.some(callback(element[, index[, array]])[, thisArg]
```

La méthode `some` teste si au moins un élément du tableau passe la condition de test donnée par la fonction fournie et retourne une valeur booléenne `true` ou `false`.

Elle retourne `true` dès qu'elle trouve la première correspondance et retourne `false` s'il n'y a pas de correspondance.

Supposons que nous avons un tableau de nombres et que nous voulons vérifier si le tableau contient au moins un élément positif. Nous pouvons utiliser la méthode `some` pour y parvenir.

```js
let numbers = [-30, 40, 20, 50];

let containsPositive = numbers.some(function (number) {
  return number > 0;
});
console.log(containsPositive); // true 

numbers = [-10, -30, -20, -50];

containsPositive = numbers.every(function (number) {
  return number > 0;
});
console.log(containsPositive); // false

```

Il existe certains scénarios utiles pour utiliser la méthode `some`.

### Exemple 1 de la méthode `Some` :

Supposons que nous avons une liste d'employés et que nous voulons vérifier si un employé particulier est présent dans ce tableau ou non. Nous voulons également obtenir la position d'index de cet employé si l'employé est trouvé.

Ainsi, au lieu d'utiliser les méthodes `find` et `findIndex` séparément, nous pouvons utiliser la méthode `some` pour faire les deux.

```js
const employees = [
  { name: 'David Carlson', age: 30 },
  { name: 'John Cena', age: 34 },
  { name: 'Mike Sheridon', age: 25 },
  { name: 'John Carte', age: 50 }
];

let indexValue = -1;
const employee = employees.some(function (employee, index) {
  const isFound = employee.name.indexOf('John') > -1;
  if (isFound) {
    indexValue = index;
  }
  return isFound;
});

console.log(employee, indexValue); // true 1

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/ExNWOvz?editors=0011).

### Exemple 2 de la méthode `Some` :

Les méthodes de tableau `forEach`, `map` et `filter` s'exécutent du début à la fin jusqu'à ce que tous les éléments du tableau soient traités. Il n'y a aucun moyen de s'arrêter ou de sortir de la boucle une fois qu'un élément particulier est trouvé.

Dans de tels cas, nous pouvons utiliser la méthode `some` du tableau. Les méthodes `map`, `forEach` et `some` prennent les mêmes paramètres dans la fonction de rappel :

* Le premier paramètre est la valeur réelle
* Le deuxième paramètre est l'index
* Le troisième paramètre est le tableau original

La méthode `some` arrête de parcourir le tableau dès qu'elle trouve une correspondance particulière comme on peut le voir dans l'exemple 1 ci-dessus.

### Avantages de l'utilisation de la méthode some

* Elle nous permet de vérifier rapidement si certains des éléments correspondent à certains critères sans écrire beaucoup de code
* Elle nous permet de sortir rapidement de la boucle, ce qui n'était pas possible avec les autres méthodes de boucle vues ci-dessus

### Support des navigateurs :

* Tous les navigateurs modernes et Internet Explorer (IE) version 9 et supérieures
* Microsoft Edge version 12 et supérieures

## La méthode Array.reduce

La méthode `Array.reduce` a la syntaxe suivante :

```js
Array.reduce(callback(accumulator, currentValue[, index[, array]])[, initialValue])
```

La méthode `reduce` exécute une fonction **réductrice** (que vous fournissez) sur chaque élément du tableau, résultant en une seule valeur de sortie.

> Notez que la sortie de la méthode `reduce` est toujours une seule valeur. Il peut s'agir d'un objet, d'un nombre, d'une chaîne, d'un tableau, etc. Cela dépend de ce que vous voulez que la sortie de la méthode `reduce` génère, mais c'est toujours une seule valeur.

Supposons que vous voulez trouver la somme de tous les nombres dans le tableau. Vous pouvez utiliser la méthode `reduce` pour cela.

```js
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce(function(accumulator, number) {
  return accumulator + number; 
}, 0);

console.log(sum); // 15
```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/ExNWzmo?editors=0012).

La méthode `reduce` accepte une fonction de rappel qui reçoit `accumulator`, `number`, `index` et `array` comme valeurs. Dans le code ci-dessus, nous utilisons uniquement `accumulator` et `number`.

L'`accumulator` contiendra la `initialValue` à utiliser pour le tableau. La `initialValue` détermine le type de retour des données retournées par la méthode `reduce`.

Le `number` est le deuxième paramètre de la fonction de rappel qui contiendra l'élément du tableau lors de chaque itération de la boucle.

Dans le code ci-dessus, nous avons fourni `0` comme `initialValue` pour l'`accumulator`. Ainsi, la première fois que la fonction de rappel s'exécute, `accumulator + number` sera `0 + 1 = 1` et nous retournons la valeur `1`.

La fois suivante où la fonction de rappel s'exécute, `accumulator + number` sera `1 + 2 = 3` (`1` ici est la valeur précédente retournée lors de la dernière itération et `2` est l'élément suivant du tableau).

Ensuite, la fois suivante où la fonction de rappel s'exécute, `accumulator + number` sera `3 + 3 = 6` (le premier `3` ici est la valeur précédente retournée lors de la dernière itération et le `3` suivant est l'élément suivant du tableau) et cela continuera ainsi jusqu'à ce que tous les éléments du tableau `numbers` soient itérés.

Ainsi, l'`accumulator` conservera la valeur de la dernière opération comme une variable statique.

Dans le code ci-dessus, `initialValue` de `0` n'est pas requis car tous les éléments du tableau sont des entiers.

Ainsi, le code ci-dessous fonctionnera également :

```js
const numbers = [1, 2, 3, 4, 5];

const sum = numbers.reduce(function (accumulator, number) {
  return accumulator + number;
});

console.log(sum); // 15

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/ExNWObz?editors=0012).

Ici, l'`accumulator` contiendra le premier élément du tableau et `number` contiendra l'élément suivant du tableau (`1 + 2 = 3` lors de la première itération puis `3 + 3 = 6` lors de l'itération suivante, et ainsi de suite).

Mais il est toujours bon de spécifier la `initialValue` de l'`accumulator` car cela facilite la compréhension du type de retour de la méthode `reduce` et l'obtention du type de données correct.

Jetez un œil au code ci-dessous :

```js
const numbers = [1, 2, 3, 4, 5];

const doublesSum = numbers.reduce(function (accumulator, number) {
  return accumulator + number * 2;
}, 10);

console.log(doublesSum); // 40

```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/jOVBQYx?editors=0012).

Ici, nous multiplions chaque élément du tableau par 2. Nous avons fourni une `initialValue` de 10 à l'`accumulator` donc 10 sera ajouté au résultat final de la somme comme ceci :

```js
[1 * 2, 2 * 2, 3 * 2, 4 * 2, 5 * 2] = [2, 4, 6, 8, 10] = 30 + 10 = 40
```

Supposons que vous avez un tableau d'objets avec des coordonnées x et y et que vous voulez obtenir la somme des coordonnées x. Vous pouvez utiliser la méthode `reduce` pour cela.

```js
const coordinates = [
  { x: 1, y: 2 }, 
  { x: 2, y: 3 }, 
  { x: 3, y: 4 }
];

const sum = coordinates.reduce(function (accumulator, currentValue) {
    return accumulator + currentValue.x;
}, 0);

console.log(sum); // 6
```

Voici une [Démonstration Code Pen](https://codepen.io/myogeshchavan97/pen/OJbpaOg?editors=0012).

### Avantages de l'utilisation de la méthode reduce

* L'utilisation de `reduce` nous permet de générer tout type de données simples ou complexes basées sur le tableau
* Elle se souvient des données précédemment retournées par la boucle, ce qui nous aide à éviter de créer une variable globale pour stocker la valeur précédente

**Support des navigateurs :**

* Tous les navigateurs modernes et Internet Explorer (IE) version 9 et supérieures
* Microsoft Edge version 12 et supérieures

### Merci d'avoir lu !

Vous voulez apprendre toutes les fonctionnalités ES6+ en détail, y compris `let` et `const`, les promesses, diverses méthodes de promesses, la déstructuration de tableaux et d'objets, les fonctions fléchées, async/await, import et export, et bien plus encore ?

Consultez mon livre [Maîtriser le JavaScript Moderne](https://yogeshchavan1.podia.com/mastering-modern-javascript?coupon=LA1HR55). Ce livre couvre tous les prérequis pour apprendre React et vous aide à devenir meilleur en JavaScript et React.

De plus, consultez mon cours gratuit [Introduction à React Router](https://yogeshchavan1.podia.com/react-router-introduction) pour apprendre React Router à partir de zéro.

**Vous voulez rester à jour avec du contenu régulier concernant JavaScript, React, Node.js ? [Suivez-moi sur LinkedIn](https://www.linkedin.com/in/yogesh-chavan97/).**