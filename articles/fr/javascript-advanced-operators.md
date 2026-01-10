---
title: Opérateurs JavaScript avancés – Fusion nulle, Chaînage optionnel et Affectation
  par décomposition
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2024-01-04T15:22:39.000Z'
originalURL: https://freecodecamp.org/news/javascript-advanced-operators
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/js-advanced-operators.png
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
- name: Web Development
  slug: web-development
seo_title: Opérateurs JavaScript avancés – Fusion nulle, Chaînage optionnel et Affectation
  par décomposition
seo_desc: 'Hi Everyone! In this article, I''m going to teach you how to use three
  advanced JavaScript operators: the Nullish Coalescing, Optional Chaining, and Destructuring
  Assignment operators.

  These three operators will help you write clearer and less error-p...'
---

Bonjour à tous ! Dans cet article, je vais vous apprendre à utiliser trois opérateurs JavaScript avancés : les opérateurs de fusion nulle, de chaînage optionnel et d'affectation par décomposition.

Ces trois opérateurs vous aideront à écrire un code plus clair et moins sujet aux erreurs.

## L'opérateur de fusion nulle

Lorsque vous inspectez du code JavaScript, vous pouvez trouver une expression utilisant un double point d'interrogation (`??`), comme dans le code ci-dessous :

```js
console.log(username ?? "Guest");
```

Le double point d'interrogation est un opérateur logique qui retourne l'expression du côté droit de la marque lorsque l'expression du côté gauche est `null` ou `undefined`.

Cet opérateur est également connu sous le nom d'opérateur de fusion nulle. Il s'agit d'une nouvelle fonctionnalité introduite dans JavaScript ES2020 qui vous permet de vérifier les valeurs `null` ou `undefined` de manière plus concise.

### Syntaxe de l'opérateur de fusion nulle

La syntaxe de l'opérateur de fusion nulle est très simple. Il se compose de deux points d'interrogation `??` placés entre deux opérandes.

Voici un exemple :

```js
let firstName = null;
let username = firstName ?? "Guest";
console.log(username); // "Guest"
```

Le code ci-dessus attribue la valeur de la variable `firstName` comme valeur de la variable `username`.

Lorsque la valeur de `firstName` est `null` ou `undefined`, alors la valeur `Guest` sera attribuée à la variable `username` à la place :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/nullish-coalescing-output.png)
_Résultat de l'utilisation de l'opérateur de fusion nulle_

Vous pouvez également l'écrire de cette manière :

```js
let username = undefined ?? "Guest";
console.log(username); // "Guest"
```

Comme vous pouvez le voir, vous n'avez pas besoin d'une instruction `if-else` pour vérifier les valeurs `null` ou `undefined`.

### Pourquoi JavaScript a besoin de cet opérateur

L'opérateur de fusion nulle a été créé comme une alternative améliorée à l'opérateur OR `||`.

L'opérateur OR a été initialement créé pour fournir une valeur par défaut ou de repli lorsque l'expression du côté gauche est fausse, ou évalue à `false`.

Mais après quelques utilisations dans le monde réel, il est clair qu'il y a des moments où les développeurs veulent retourner des valeurs qui sont considérées comme fausses, comme `0` et une chaîne vide (`""`).

L'utilisation de l'opérateur OR vous empêchera de retourner des valeurs fausses. Considérez l'exemple suivant :

```js
// une chaîne vide évalue à false en JavaScript :
let firstName = "";
let username = firstName ?? "Guest";
console.log(username); // ""

// Lorsque vous utilisez l'opérateur OR :
username = firstName || "Guest";
console.log(username); // "Guest"
```

En utilisant l'opérateur de fusion nulle, vous ne remplacerez que les valeurs **exactement** `null` et `undefined` par la valeur du côté droit.

L'opérateur de fusion nulle peut être utilisé avec n'importe quel type de valeur, y compris les nombres, les chaînes et les objets.

### Cas d'utilisation de l'opérateur de fusion nulle

L'opérateur de fusion nulle est utile dans diverses situations où vous devez vérifier les valeurs `null` ou `undefined` et fournir une valeur par défaut.

Voici plusieurs exemples de cas d'utilisation courants :

#### Gestion des arguments de fonction manquants

Lorsque qu'une fonction est appelée, il est possible que certains des arguments soient omis.

L'opérateur de fusion nulle peut être utilisé pour fournir des valeurs par défaut pour un argument manquant comme suit :

```js
function greet(name) {
  console.log(`Hello, ${name ?? "Guest"}!`);
}

greet(); // 'Hello, Guest!'
greet("John"); // 'Hello, John!'
```

#### Accès aux propriétés d'un objet

Lorsque vous travaillez avec des objets, il est possible qu'une propriété n'existe pas ou soit `undefined`.

L'opérateur de fusion nulle peut être utilisé pour accéder en toute sécurité aux propriétés d'un objet et fournir une valeur par défaut lorsque la propriété est manquante :

```js
let user = { name: "John Doe" };
let email = user.email ?? "N/A";
console.log(email); // 'N/A'
```

#### Choix entre une variable et une constante

Vous pouvez vouloir sélectionner une valeur à partir d'une variable ou d'une constante si la variable est `null` ou `undefined` :

```js
let value = null;
const DEFAULT_VALUE = 'Default';

let result = value ?? DEFAULT_VALUE;

console.log(result); // 'Default'
```

Comme vous pouvez le voir, l'opérateur de fusion nulle est une excellente fonctionnalité qui peut rendre votre code plus concis et fiable.

### Utilisation de `??` avec les opérateurs `||` et `&&`

Pour des raisons de sécurité, le double point d'interrogation ne peut pas être utilisé avec les opérateurs OR (`||`) et AND (`&&`) de JavaScript sans parenthèses `()` séparant les opérateurs.

Par exemple, le code suivant essaie de voir si l'une des variables `firstName` ou `lastName` peut être utilisée comme valeur de `username` avant d'utiliser `"Guest"` comme valeur :

```js
let firstName = "John";
let lastName = "Stone";
let username = firstName || lastName ?? "Guest";
// Erreur : Unexpected token '??'

console.log(username);
```

Cela est dû au fait que JavaScript ne pourra pas déterminer quel opérateur il doit évaluer en premier. Vous devez utiliser des parenthèses pour indiquer clairement la priorité des évaluations.

Le code suivant évaluera d'abord les expressions à l'intérieur des parenthèses :

```js
let firstName = null;
let lastName = undefined;
let username = (firstName || lastName) ?? "Guest";

console.log(username); // "Guest"
```

Et c'est ainsi que vous combinez l'opérateur de fusion nulle avec l'opérateur AND ou OR.

## L'opérateur de chaînage optionnel

Comme l'opérateur de fusion nulle, l'opérateur de chaînage optionnel est un ajout moderne à JavaScript qui offre une meilleure façon de faire les choses.

L'opérateur de chaînage optionnel `?.` vous donne un moyen sûr d'accéder aux propriétés et méthodes d'un objet, en évitant une erreur dans le processus.

L'un des problèmes les plus courants en JavaScript est que vous pouvez obtenir une erreur lorsque vous accédez à une propriété d'une valeur `undefined`.

Par exemple, supposons que vous avez un objet `car` comme suit :

```js
const car = {};

console.log(car.manufacturer); // undefined
console.log(car.manufacturer.address); // ❌ TypeError!
```

Dans l'exemple ci-dessus, l'accès à la propriété `manufacturer` retourne `undefined`, mais lorsque vous essayez d'accéder à la propriété `address` de la propriété `manufacturer`, JavaScript retourne une erreur.

Bien que ce soit ainsi que JavaScript fonctionne, une meilleure façon de gérer la propriété inexistante serait de simplement retourner un `undefined`, comme lorsque nous essayons d'accéder à la propriété `manufacturer`.

C'est pourquoi l'opérateur de chaînage optionnel a été créé. L'opérateur retourne soit la valeur de la propriété, soit `undefined` lorsque la propriété est `null` ou `undefined`.

Pour utiliser l'opérateur, il suffit d'ajouter un point d'interrogation devant la notation par point `.` :

```js
const car = {};

console.log(car.manufacturer?.address); // undefined
```

L'opérateur de chaînage optionnel peut être ajouté chaque fois que vous utilisez la notation par point pour accéder à une propriété ou à une méthode.

Cet opérateur vous permet d'éviter le TypeError qui se produit lorsque vous accédez à une propriété ou appelez une méthode à partir d'une propriété inexistante :

```js
const car = {};

console.log(car.manufacturer?.address); // undefined
console.log(car.manufacturer?.drive()); // undefined
```

Notez que l'opérateur de chaînage optionnel ne vérifie que la valeur qui le précède. Si la variable `car` peut être `null`, alors vous devez ajouter l'opérateur après lorsque vous accédez à l'objet `car` également.

Voir l'exemple suivant :

```js
const car = null;

console.log(car?.manufacturer?.address); // undefined
console.log(car.manufacturer?.address); // TypeError: Cannot read properties of null
```

Et c'est ainsi que fonctionne l'opérateur de chaînage optionnel. Il est vraiment utile lorsque vous travaillez avec des objets dans votre projet.

Ensuite, apprenons l'affectation par décomposition.

## Opérateur d'affectation par décomposition

L'affectation par décomposition est un opérateur spécial qui vous permet de "déballer" ou "extraire" les valeurs des tableaux et objets JavaScript. Il est devenu l'une des fonctionnalités les plus utiles du langage JavaScript pour deux raisons :

* Il vous aide à éviter la répétition de code.
* Il garde votre code propre et facile à comprendre.

Voyons comment vous pouvez décomposer un tableau et un objet ensuite.

### Décomposition des tableaux

Voici comment vous attribuez normalement les valeurs d'un tableau à des variables :

```js
const sampleArray = ['Jane', 'John'];

const firstIndex = sampleArray[0];
const secondIndex = sampleArray[1];
```

Le code ci-dessus fonctionne, mais vous avez besoin de deux lignes de code pour obtenir deux éléments d'un tableau. En utilisant l'affectation par décomposition, vous pouvez attribuer les éléments du tableau à des variables en une seule ligne :

```js
const sampleArray = ['Jane', 'John'];

const [firstIndex, secondIndex] = sampleArray;
```

Le code ci-dessus retournera la même valeur pour les variables `firstIndex` et `secondIndex`. Peu importe le nombre d'éléments que vous avez, la décomposition commencera à partir de l'index zéro.

Pour créer une affectation par décomposition, vous devez ajouter des crochets `[]` après le mot-clé `let`/ `const`. Lorsque vous ajoutez des crochets après l'opérateur d'affectation (`=`), c'est un tableau. Si vous les ajoutez avant l'opérateur d'affectation, c'est une affectation par décomposition.

Vous pouvez également utiliser l'opérateur de repos `…` pour copier le reste des valeurs après votre affectation. Regardez l'exemple suivant :

```js
const sampleArray = ['Jane', 'John', 'Jack', 'Aston'];

const [one, two, ...rest] = sampleArray;
```

La variable `rest` contiendra un tableau avec les valeurs `['Jack','Aston']`.

Vous pouvez également mettre des valeurs par défaut pour ces variables lorsque la valeur extraite est undefined :

```js
const [a = 'Martin', b = 10] = [true];

// a retournera true
// b retournera 10
```

Vous pouvez également attribuer immédiatement le retour d'une fonction à des affectations. Cela est fréquemment utilisé dans des bibliothèques comme React :

```jsx
const [a, b] = myFunction();

function myFunction() {
  return ['John', 'Jack'];
}
```

La variable `a` retournera "John" et `b` retournera "Jack".

Enfin, vous pouvez également ignorer certaines variables en sautant l'affectation pour cet index :

```js
const [a, , b] = [1, 2, 3];

// a retournera 1
// b retournera 3
```

L'affectation par décomposition rend le déballage des valeurs de tableau plus facile et plus court, avec moins de répétition.

### Décomposition des objets

Tout comme les tableaux, vous pouvez décomposer les objets de la même manière, mais au lieu d'utiliser les crochets (`[]`), vous devez utiliser les accolades (`{}`) :

```js
const user = {
  firstName: 'Jack',
  lastName: 'Smith',
};

const { firstName, lastName } = user;
```

Vous pouvez utiliser le délimiteur deux-points (`:`) pour attribuer la propriété à un nom différent. L'exemple ci-dessous attribue la valeur de `firstName` à `name` :

```js
const user = {
  firstName: 'Jack',
  lastName: 'Smith',
};

const { firstName: name, lastName } = user;
```

Notez que vous ne créez toujours que deux variables : `name` et `lastName`. La propriété `firstName` est attribuée à `name`, donc elle ne créera pas de variable séparée.

Tout comme les tableaux, vous pouvez décomposer un objet retourné par une fonction immédiatement :

```js
function myFunction() {
  return { firstName: 'Jack', lastName: 'Austin' };
}

const { firstName, lastName } = myFunction();

```

De plus, vous pouvez décomposer un objet à partir des paramètres de fonction, exactement lorsque vous définissez la fonction :

```js
function myFunction({ firstName, lastName }) {
  return firstName + ' ' + lastName;
}

const user = {
  firstName: 'Jack',
  lastName: 'Austin',
};

const name = myFunction(user);
```

L'affectation par décomposition est un ajout utile à JavaScript qui facilite le déballage des valeurs des objets et des tableaux. Vous allez l'utiliser fréquemment lorsque vous codez en utilisant une bibliothèque comme React.

## Conclusion

JavaScript s'améliore constamment chaque année, et les trois opérateurs expliqués dans cet article sont un excellent ajout qui peut vous aider à produire un code plus concis et lisible.

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine fois !