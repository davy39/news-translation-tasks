---
title: Conseils JavaScript pour vous aider à construire de meilleurs projets de développement
  web
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-08-15T14:17:37.000Z'
originalURL: https://freecodecamp.org/news/javascript-tips-for-better-web-dev-projects
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/start-graph--15-.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Conseils JavaScript pour vous aider à construire de meilleurs projets de
  développement web
seo_desc: 'JavaScript is a widely used web programming language. If you''re getting
  into software engineering or coding in particular and you want to focus on web development,
  learning JavaScript is probably the best thing to do.

  Learning JavaScript empowers you...'
---

JavaScript est un langage de programmation web largement utilisé. Si vous vous lancez dans le génie logiciel ou la programmation en particulier et que vous souhaitez vous concentrer sur le développement web, apprendre JavaScript est probablement la meilleure chose à faire.

Apprendre JavaScript vous permet de créer des expériences web dynamiques et interactives. Et cela vous permet de donner vie aux sites web et aux applications web en ajoutant des fonctionnalités, de l'interactivité et des mises à jour en temps réel pour une meilleure expérience utilisateur.

J'ai récemment relevé un défi **30 jours de conseils JavaScript** sur Twitter (maintenant, X) où j'ai partagé 30 conseils JavaScript différents avec mes abonnés quotidiennement pendant 30 jours. J'ai décidé de compiler ces conseils en un seul tutoriel géant pour les campeurs et tout le monde sur Internet. C'est pourquoi vous lisez ceci.

Que vous commeniez tout juste avec JavaScript ou que vous soyez déjà un développeur JavaScript expérimenté, vous tirerez quelque chose de cet article.


## Ce que nous allons couvrir
- [Conseil 1 : Utilisez `console.table()` pour afficher les tableaux et les objets dans la console](#heading-tip-1-use-consoletable-to-display-arrays-and-objects-in-the-console)
- [Conseil 2 : Utilisez l'interpolation de gabarit pour rendre les chaînes au lieu de l'opérateur d'affectation](#heading-tip-2-use-template-interpolation-to-render-strings-instead-of-the-assignment-operator)
- [Conseil 3 : Convertissez les chaînes en nombres avec le plus unaire et le constructeur Number](#heading-tip-3-convert-strings-to-numbers-with-unary-plus-and-number-constructor)
- [Conseil 4 : Vous n'avez pas besoin de déclarer chaque variable avec un mot-clé](#heading-tip-4-you-dont-need-to-declare-every-variable-with-a-keyword)
- [Conseil 5 : Utilisez `console.group()` avec plusieurs `console.log()` pour regrouper les éléments liés dans la console](#tip5useconsolegroupwithmultipleconsolelogtogrouprelateditemstotheconsole)
- [Conseil 6 : Stylez votre sortie de console avec le spécificateur `%c`](#heading-tip-6-style-your-console-output-with-the-c-specifier)
- [Conseil 7 : Comment `Math.floor(Math.random() * n1 + n2)` génère un nombre aléatoire entre `n1` et `n2`](#heading-tip-7-how-mathfloormathrandom-n1-n2-generates-a-random-number-between-n1-and-n2)
- [Conseil 8 : Méthodes de l'objet Math](#heading-tip-8-methods-of-the-math-object)
- [Conseil 9 : Mettez en majuscule la première lettre de n'importe quel mot](#heading-tip-9-capitalize-the-first-letter-of-any-word)
- [Conseil 10 : Déstructurez les tableaux avec des valeurs par défaut pour éviter d'obtenir `undefined`](#heading-tip-10-destructure-arrays-with-default-values-to-avoid-getting-undefined)
- [Conseil 11 : Utilisez l'opérateur de propagation pour copier et fusionner des tableaux](#heading-tip-11-use-the-spread-operator-to-copy-and-merge-arrays)
- [Conseil 12 : Utilisez la syntaxe de flèche pour écrire des fonctions plus courtes et plus élégantes](#heading-tip-12-use-arrow-syntax-to-write-shorter-and-more-elegant-functions)
- [Conseil 13 : Utilisez la déstructuration pour extraire les propriétés des objets](#heading-tip-13-use-destructuring-to-extract-properties-from-objects)
- [Conseil 14 : Utilisez les méthodes de chaîne `startsWith()` et `endsWith()` pour obtenir le début et la fin d'une chaîne](#heading-tip-14-use-the-startswith-and-endswith-string-methods-to-get-the-start-and-end-of-a-string)
- [Conseil 15 : Utilisez `trim()`, `trimStart()` et `trimEnd()` pour gérer les espaces blancs](#heading-tip-15-use-the-trim-trimstart-and-trimend-to-handle-white-spaces)
- [Conseil 16 : Utilisez `replace()` avec les méthodes `toUpperCase()` et `toLowerCase()` pour convertir entre les cas](#heading-tip-16-use-replace-with-the-touppercase-and-tolowercase-methods-to-convert-between-cases)
- [Conseil 17 : Utilisez la méthode `Array.from()` pour créer des tableaux à partir d'objets de type tableau ou d'itérables](#tip17usethearrayfrommethodtocreatearraysfromarray-likeobjectsoriterables)
- [Conseil 18 : Utilisez la méthode `map()` pour transformer tous les éléments d'un tableau](#heading-tip-18-use-the-map-method-to-transform-all-the-elements-of-an-array)
- [Conseil 19 : Utilisez la méthode `filter()` pour filtrer à travers les tableaux](#heading-tip-19-use-the-filter-method-to-filter-through-arrays)
- [Conseil 21 : Utilisez l'API Web Audio pour travailler avec des fichiers audio](#heading-tip-21-use-the-web-audio-api-to-work-with-audio-files)
- [Conseil 22 : Utilisez l'API Web Video pour travailler avec des fichiers vidéo](#heading-tip-22-use-the-web-video-api-to-work-with-video-files)
- [Conseil 23 : Préservez l'intégrité des objets en les scellant et en les gelant](#heading-tip-23-preserve-object-integrity-by-sealing-and-freezing-them)
- [Conseil 24 : Utilisez `async...await` pour les opérations asynchrones](#tip24use`asyncawait`forasynchronousoperations)
- [Conseil 25 : Clonez les objets avec l'opérateur de propagation, `Object.assign()` et `JSON.parse()`](#heading-tip-25-clone-objects-with-the-spread-operator-objectassign-and-jsonparse)
- [Conseil 26 : Supprimez les doublons d'un tableau avec Set et Map](#heading-tip-26-remove-duplicates-from-an-array-with-set-and-map)
- [Conseil 27 : Parcourez un tableau et aplatissez-le avec la méthode `flatMap()`](#heading-tip-27-map-through-and-array-and-flatten-it-with-the-flatmap-method)
- [Conseil 28 : Utilisez les méthodes `padStart()` et `padEnd()` pour remplir une chaîne avec un caractère](#ip28usethepadstartandpadendmethodstopadastringwithacharacter)
- [Conseil 29 : Utilisez la méthode `insertAdjacentHTML()` du DOM pour insérer une chaîne dans le DOM](#heading-tip-29-use-the-insertadjacenthtml-method-of-dom-to-insert-a-string-into-the-dom)
- [Conseil 30 : Utilisez la méthode `createTreeWalker()` du DOM pour parcourir le DOM](#heading-tip-30-use-the-createtreewalker-dom-method-to-traverse-the-dom)


## Conseil 1 : Utilisez `console.table()` pour afficher les tableaux et les objets dans la console
`console.log` affichera le tableau ou l'objet comme d'habitude, mais `console.table` le mettra sous forme de tableau pour vous.

Voici comment cela fonctionne avec les tableaux :

```js
const myArr = ['Kolade', 'Chelsea', 10, true];

console.log(myArr);
console.table(myArr);
```

Voici le résultat de `console.log()` et `console.table()` :

![ss1](https://www.freecodecamp.org/news/content/images/2023/08/ss1.png)

Vous pouvez voir qu'en plus de mettre le tableau sous forme de tableau pour vous, il l'affiche également de la manière dont un `console.log()` l'afficherait.

Cela fonctionne avec les objets de la même manière qu'avec les tableaux :

```js
const myObj = {
  name: 'Kolade',
  luckyNum: 10,
  lovesFootball: true,
};

console.log(myObj);
console.table(myObj);
```

![ss2](https://www.freecodecamp.org/news/content/images/2023/08/ss2.png)

## Conseil 2 : Utilisez l'interpolation de gabarit pour rendre les chaînes au lieu de l'opérateur d'affectation

La syntaxe d'interpolation de gabarit est plus propre et plus lisible que la concaténation régulière avec le plus (`+`). Avec l'interpolation de gabarit, vous pouvez facilement intégrer des variables dans des chaînes.

```js
const name = 'John Doe';
const age = 20;

const plusConcat =
  'Hi there \ud83d\udc4b\ud83c\udffd \nMy name is ' + name + ' and I am ' + age + ' years old.';

const templateLiteralConcat = `Hi there \ud83d\udc4b\ud83c\udffd \nMy name is, ${name} and I am ${age} years old.`;
```

## Conseil 3 : Convertissez les chaînes en nombres avec le plus unaire et le constructeur Number
L'opérateur plus unaire (`+`) et le constructeur de nombre (`Number()`) vous aident à convertir des chaînes en nombres.

Pour convertir la chaîne en nombre avec l'unaire, il vous suffit de préfixer la chaîne avec un signe plus. Et pour le faire avec le constructeur de nombre, enveloppez le nombre dans `Number()`

```js
const myNum = '5';

convertNum1 = +myNum;
convertNum2 = Number(myNum);

console.log(convertNum1, typeof convertNum1); // 5 'number'
console.log(convertNum2, typeof convertNum2); // 5 'number'
```


## Conseil 4 : Vous n'avez pas besoin de déclarer chaque variable avec un mot-clé

Saviez-vous que si vous avez plusieurs variables les unes à côté des autres, vous pouvez éviter d'utiliser `const`, `let` ou `var` pour déclarer chaque variable après la première ?

Le seul inconvénient est que si vous déclarez des variables sans mot-clé, vous devez les séparer par une virgule (`,`) au lieu d'un point-virgule.

C'est tout :

```js
// déclarez plusieurs variables à la fois.
let x, y, z;

x = 1;
y = 2;
z = 3;

console.log(x, y, z); // 1, 2, 3

// déclarez d'autres variables après la première sans le mot-clé.
const a = 'Hello',
  b = 'How are you today?',
  c = 'Are you coding today?';

console.log(a); // Hello
console.log(b); // How are you today?
console.log(c); // Are you coding today?
```

Ce qui précède est la même chose que :

```js
let x;
let y;
let z;

x = 1;
y = 2;
z = 3;

console.log(x, y, z); // 1, 2, 3

// déclarez d'autres variables après la première sans le mot-clé.
const a = 'Hello';
const b = 'How are you today?';
const c = 'Are you coding today?';

console.log(a); // Hello
console.log(b); // How are you today?
console.log(c); // Are you coding today?
```


## Conseil 5 : Utilisez `console.group()` avec plusieurs `console.log()` pour regrouper les éléments liés dans la console
Lorsque vous avez plusieurs éléments liés comme le nom d'utilisateur, la bio, etc., et que vous souhaitez les journaliser dans la console, vous devez utiliser `console.group()` et `console.groupEnd()` pour fermer le groupe.

Cela vous donnera une liste déroulante de tous les éléments :

```js
console.group('Bio:');

console.log('My name is Kolade');
console.warn("I don't like to be late");
console.error('You came late');

console.groupEnd();
```

![ss3](https://www.freecodecamp.org/news/content/images/2023/08/ss3.png)


## Conseil 6 : Stylez votre sortie de console avec le spécificateur `%c`

`%c` ne fait pas partie de JavaScript lui-même. Il s'agit d'un spécificateur de format fourni par les navigateurs modernes pour styliser la console. Lorsque vous souhaitez l'utiliser, il doit être le premier paramètre dans la méthode `console.log()`.

Vous pouvez définir le style que vous souhaitez appliquer à la console :

```js
const styles = `padding: 15px;
                background-color: #2ecc71;
                color: black`;

console.log('%c Hello, Everyone!', styles);
```

Ou vous pouvez le mettre directement :

```js
console.log(
  '%c Hello, Everyone!',
  'padding: 15px; background-color: #2ecc71; color: black'
);
```

![ss4](https://www.freecodecamp.org/news/content/images/2023/08/ss4.png)


## Conseil 7 : Comment `Math.floor(Math.random() * n1 + n2)` génère un nombre aléatoire entre `n1` et `n2`

Vous avez probablement vu comment `Math.floor(Math.random() * n1 + n2)` crée un nombre aléatoire entre 2 nombres. Vous avez même pu l'utiliser vous-même. Mais comment cela fonctionne-t-il ?

Par exemple, `Math.floor(Math.random() * 100 + 1)` générerait un nombre aléatoire entre `100` et `1`, après avoir suivi ces processus :

- `Math.random()` génère un nombre à virgule flottante aléatoire entre 0 et 1 – `0` inclus mais 1 exclus
- Avec `Math.random() * 100`, le nombre aléatoire est maintenant entre `0` et `99` mais a toujours de longues virgules flottantes
- `Math.floor(Math.random() * 100)` arrondit le nombre à virgule flottante à l'entier le plus proche entre `0` et `99`
- `Math.floor(Math.random() * 100 + 1)` ajoute `1` au résultat et décale la plage à `1 - 100`.

Cette infographie ci-dessous vous montre également comment cela fonctionne :

![generateRandomNum](https://www.freecodecamp.org/news/content/images/2023/08/generateRandomNum.png)


## Conseil 8 : Méthodes de l'objet Math

Voici plusieurs méthodes de l'objet `Math` et ce qu'elles font :

```js
let x;

// Obtenez la racine carrée d'un nombre
x = Math.sqrt(9);

// convertissez un nombre en valeur absolue
x = Math.abs(-5); // 5

// Arrondissez un nombre à l'entier le plus proche
x = Math.round(4.6);

// Arrondissez un nombre vers le haut
x = Math.ceil(4.2); // 5

// Arrondissez un nombre vers le bas
x = Math.floor(4.9); // 4

// Exponentielle d'un nombre
x = Math.pow(2, 3); // 8

// Obtenez le nombre minimum
x = Math.min(4, 5, 3); // 3

// Obtenez le nombre maximum
x = Math.max(4, 5, 3); // 5

// Obtenez un nombre/décimal aléatoire entre 0 et 1
x = Math.random();

// Obtenez un nombre aléatoire entre 1 et 200
x = Math.floor(Math.random() * 200 + 1); // n'importe quel nombre entre 1 et 200

console.log(x);
```


## Conseil 9 : Mettez en majuscule la première lettre de n'importe quel mot
Vous pouvez mettre en majuscule la première lettre de n'importe quel mot en combinant les méthodes `charAt()`, `toUpperCase()` et `slice()`.

Avec `charAt(0)`, vous pouvez obtenir la première lettre du mot et utiliser la méthode `toUpperCase()` avec celle-ci, puis concaténer le reste des lettres avec `slice(1)`.

```js
const str = 'john';
const capitalizedStr = (str) => str.charAt(0).toUpperCase() + str.slice(1);

console.log(capitalizedStr(str)); // John
console.log(capitalizedStr('doe')); // Doe
```


## Conseil 10 : Déstructurez les tableaux avec des valeurs par défaut pour éviter d'obtenir `undefined`
Si vous déstructurez avec une valeur par défaut, et que la valeur attendue n'est pas présente dans le tableau ou l'objet lors de la déstructuration, la valeur par défaut sera utilisée à la place. Cela permet d'éviter les erreurs et garantit que votre code gère élégamment les données manquantes.

Voici comment cela fonctionne avec les tableaux :

```js
// Déstructuration sans valeurs par défaut
const fruits = ['Apple', 'Banana'];
const [firstFruit, secondFruit, thirdFruit] = fruits;

console.log(firstFruit); // Apple
console.log(secondFruit); // Banana
console.log(thirdFruit); // undefined

// Déstructuration avec valeurs par défaut
const [fruit1, fruit2, fruit3 = 'Orange'] = fruits;

console.log(fruit1); // Apple
console.log(fruit2); // Banana
console.log(fruit3); // Orange
```

Et voici comment cela fonctionne avec les objets :

```js
// Sans valeurs par défaut
const person = { name: 'John Doe', age: 30 };
const { name, age, occupation } = person;
console.log(name); // John Doe
console.log(age); // 30
console.log(occupation); // undefined

// Avec valeurs par défaut
const { firstName = 'John', lastName = 'Doe', gender = 'Male' } = person;
console.log(firstName); // John
console.log(lastName); // Doe
console.log(gender); // Male
```


## Conseil 11 : Utilisez l'opérateur de propagation pour copier et fusionner des tableaux
Vous pouvez utiliser l'opérateur de propagation dans divers scénarios, tels que la copie de tableaux, la fusion de tableaux, le clonage d'objets et le passage de plusieurs arguments à des fonctions.

Voici comment l'utiliser pour copier et fusionner des tableaux :

```js
const originalArray = [1, 2, 3];
const copiedArray = [...originalArray];

console.log(copiedArray); // [1, 2, 3]

// fusionnez deux tableaux ou plus
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

const mergedArray = [...arr1, ...arr2];

console.log(mergedArray); // [1, 2, 3, 4, 5, 6
```

Voici comment vous pouvez cloner des objets avec celui-ci :

```js
const originalObj = { name: 'John', age: 30 };
const clonedObj = { ...originalObj };

console.log(clonedObj); // { name: 'John', age: 30 }
```

Et voici comment vous pouvez l'utiliser pour passer plusieurs arguments dans n'importe quelle fonction :

```js
function addNumbers(a, b, c) {
  return a + b + c;
}

const numbers = [10, 12, 8];
const sum = addNumbers(...numbers);

console.log(sum); // 30
```


## Conseil 12 : Utilisez la syntaxe de flèche pour écrire des fonctions plus courtes et plus élégantes
Les fonctions fléchées fournissent une syntaxe plus courte par rapport aux expressions de fonction traditionnelles et ont certaines caractéristiques uniques. Comprendre les fonctions fléchées est essentiel pour le développement JavaScript moderne.

```js
// Expression de fonction traditionnelle
function add1(a, b) {
  return a + b;
}

// Fonction fléchée
const add2 = (a, b) => a + b;

console.log(add1(1, 2)); // 3
console.log(add2(5, 8)); // 13

// Utilisation de l'expression de fonction traditionnelle
const numbers1 = [3, 4];
const numbers2 = [2, 8];

const squared1 = numbers1.map(function (num) {
  return num * num;
});

// Utilisation de la fonction fléchée
const squared2 = numbers2.map((num) => num * num);

console.log(squared1); // [ 9, 16 ]
console.log(squared2); // [ 4, 64 ]
```


## Conseil 13 : Utilisez la déstructuration pour extraire les propriétés des objets
La déstructuration d'objets est une fonctionnalité puissante en JavaScript. Elle vous permet d'extraire des propriétés d'objets et de les assigner à des variables de manière plus concise et lisible par rapport à la notation par points traditionnelle.

Voici comment extraire des propriétés avec la déstructuration :

```js
const person = {
  name: 'John Doe',
  age: 30,
  gender: 'male',
};

// Méthode traditionnelle
const name2 = person.name;
const age2 = person.age;
const gender2 = person.gender;

console.log(name, age, gender); // John Doe 30 male

// avec déstructuration
const { name, age, gender } = person;

console.log(name, age, gender);
// John Doe 30 male
```


## Conseil 14 : Utilisez les méthodes de chaîne `startsWith()` et `endsWith()` pour obtenir le début et la fin d'une chaîne
Les méthodes `startsWith()` et `endsWith()` vous aident à déterminer si une chaîne commence ou se termine par une sous-chaîne spécifique. Puisqu'elles retournent toutes les deux `true` ou `false`, elles sont pratiques pour diverses manipulations de chaînes et vérifications conditionnelles.

Voici leur utilisation de base :

```js
const message = 'Hello world';

console.log(message.startsWith('H')); // true
console.log(message.startsWith('h')); // false
console.log(message.endsWith('d')); // true
console.log(message.endsWith('D')); // false
```

Avec ces deux méthodes, vous pouvez extraire programmatiquement un certain texte ou nom de fichier, comme vous pouvez le voir ci-dessous :

```js
const files = [
  'text.txt',
  'document.txt',
  'image.jpg',
  'script.js',
  'docs.txt',
];

// Obtenez les fichiers .txt
const textFiles = files.filter((file) => file.endsWith('.txt'));
console.log(textFiles); [ 'text.txt', 'document.txt', 'docs.txt' ]
```

Les méthodes `startsWith()` et `endsWith()` prennent également en charge les positions de début et de fin facultatives pour limiter la plage de la chaîne où la vérification est effectuée :

```js
const text = 'Welcome to freeCodeCamp';

console.log(text.startsWith('W', 0)); // true
console.log(text.startsWith('freeCodeCamp', 11)); // true
console.log(text.endsWith('f', 11)); // false
```


## Conseil 15 : Utilisez `trim()`, `trimStart()` et `trimEnd()` pour gérer les espaces blancs

La méthode `trim()` supprime les espaces blancs aux deux extrémités de la chaîne. La méthode `trimStart()` supprime les espaces blancs au début de la chaîne. Et `trimEnd()` supprime les espaces blancs à la fin de la chaîne.

Ces trois méthodes sont utiles lorsque vous devez nettoyer les entrées des utilisateurs ou supprimer les espaces de début/fin des chaînes.

```js
const greet = '   Hello world!   ';
console.log(greet.trim());
// Hello world!

const greet2 = '   Hello world!   ';
console.log(greet2.trimStart());
// Sortie : 'Hello, world!   '

const text = '   Hello world!   ';
console.log(text.trimEnd());
// Sortie : '   Hello world!'

const input = '   ';
if (input.trim() === '') {
  console.log('The input is empty but has whitespace characters.');
} else {
  console.log('The input contains non-whitespace characters.');
}

// Sortie : The input is empty but has whitespace characters.
```


## Conseil 16 : Utilisez `replace()` avec les méthodes `toUpperCase()` et `toLowerCase()` pour convertir entre les cas

Les méthodes `toUpperCase()` et `toLowerCase()` convertissent une chaîne en majuscules et en minuscules, tandis que `replace()` prend une chaîne et la remplace par une chaîne spécifiée.

`replace()` peut également prendre des expressions régulières. Vous pouvez donc adapter cette regex pour une partie particulière de la chaîne, puis utiliser les méthodes `toLowerCase()` et `toUpperCase()` pour convertir entre les cas.

Dans l'extrait de code ci-dessous, j'ai utilisé la regex `(^|\s)\w/` pour rechercher le premier mot et chaque autre mot après un espace, puis les convertir en lettres majuscules :
```js
function toTitleCase(str) {
  return str.toLowerCase().replace(/(^|\s)\w/g, (match) => match.toUpperCase());
}

console.log(toTitleCase('welcome to twitter (now x)!'));
// Welcome To Twitter (now X)!
```

J'ai également pu convertir en **snake_case** en utilisant la regex `/\s+/g` pour rechercher chaque espace et les remplacer par un trait de soulignement (`_`)

```js
function toSnakeCase(str) {
  return str.toLowerCase().replace(/\s+/g, '_');
}

console.log(toSnakeCase('Convert this to snake case'));
// convert_this_to_snake_case
```

N'oubliez pas que vous pouvez convertir en cas sans `replace()` et regex :

```js
function toSentenceCase(str) {
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

console.log(toSentenceCase('hELLo TwEePs! HOW ARE YOU TODAY?'));
// Hello tweeps! how are you today?
```

Si vous souhaitez en savoir plus sur les expressions régulières, vous pouvez [lire mon livre sur elles ici gratuitement](https://www.freecodecamp.org/news/regular-expressions-for-javascript-developers/).


## Conseil 17 : Utilisez la méthode `Array.from()` pour créer des tableaux à partir d'objets de type tableau ou d'itérables

Les objets de type tableau ou itérables incluent les multiples arguments que vous passez à une fonction, et les éléments DOM que vous sélectionnez avec la méthode `querySelectorAll()`, par exemple, les éléments de liste.

Voici comment j'ai créé un tableau à partir d'un argument de fonction et utilisé la méthode de tableau `reduce()` sur eux :

```js
function sumArguments() {
  // L'objet "arguments" est de type tableau
  const argsArray = Array.from(arguments);
  return argsArray.reduce((acc, num) => acc + num, 0);
}

const result = sumArguments(1, 2, 3, 4, 5);
console.log(result); // Sortie : 15
```

Et voici comment j'ai créé un tableau à partir d'un ensemble d'éléments de liste sélectionnés avec `quersySelectorAll()` :

```html
<ul>
   <li>List item 1</li>
   <li>List item 2</li>
   <li>List item 3</li>
   <li>List item 4</li>
</ul>
```

```js
const listItems = document.querySelectorAll('li');
const itemsArray = Array.from(listItems);

itemsArray.forEach((item) => {
  console.log(item.textContent);
});
```

![ss5](https://www.freecodecamp.org/news/content/images/2023/08/ss5.png)


## Conseil 18 : Utilisez la méthode `map()` pour transformer tous les éléments d'un tableau

La méthode `map()` est une méthode de tableau d'ordre supérieur. Elle vous permet de transformer les éléments d'un tableau en nouvelles valeurs, créant un nouveau tableau de la même longueur que l'original mais avec des éléments modifiés.

```js
const numbers = [1, 4, 9, 16, 25];

const squareRoots = numbers.map((num) => Math.sqrt(num));
console.log(squareRoots); //[1, 2, 3, 4, 5]

const names = ['john', 'jane', 'smith'];

const capitalizedNames = names.map((name) => name.toUpperCase());
console.log(capitalizedNames); // ['JOHN', 'JANE', 'SMITH']
```

Il est très courant d'utiliser `map()` pour afficher les éléments provenant d'une API ou ceux que vous avez créés vous-même :

```html
<ul id="item-list"></ul>
```

```js
const items = ['Item 1', 'Item 2', 'Item 3'];

const itemList = document.querySelector('#item-list');

// Utilisez map() pour générer une liste d'éléments <li>
const liElements = items.map((item) => {
  const li = document.createElement('li');
  li.textContent = item;
  li.style.color = 'crimson';
  return li;
});

// Ajoutez les éléments <li> à la <ul>
liElements.forEach((li) => {
  itemList.appendChild(li);
});
```

![ss6](https://www.freecodecamp.org/news/content/images/2023/08/ss6.png)


## Conseil 19 : Utilisez la méthode `filter()` pour filtrer à travers les tableaux

La méthode `filter()` est une autre méthode de tableau qui vous permet de créer un nouveau tableau avec certains éléments qui passent un test spécifique.

Voici un exemple de base dans lequel j'ai obtenu tous les nombres pairs et impairs dans un tableau :

```js
const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

const oddNums = nums.filter((num) => num % 2 !== 0);
const evenNumbers = nums.filter((num) => num % 2 === 0);

console.log(evenNumbers); // [2, 4, 6, 8, 10, 12, 14]
console.log(oddNums); // [1,  3,  5,  7, 9, 11, 13, 15]
```

Et voici un exemple plus complexe où j'ai obtenu tous les produits à moins de 500 $ :

```js
const products = [
  { id: 1, name: 'Laptop', price: 1000 },
  { id: 2, name: 'Phone', price: 500 },
  { id: 3, name: 'Tablet', price: 300 },
  { id: 4, name: 'Headphones', price: 100 },
];

const cheapProducts = products.filter((product) => product.price < 500);

console.log(cheapProducts);
/*
[
  { id: 3, name: 'Tablet', price: 300 },
  { id: 4, name: 'Headphones', price: 100 }
]
*/
```


## Conseil 20 : Utilisez la méthode `forEach()` pour parcourir les tableaux

La méthode `forEach()` fournit un moyen plus propre et plus expressif de parcourir les tableaux par rapport aux boucles for traditionnelles.

```js
const fruits = ['apple', 'banana', 'orange'];

// avec la boucle for
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// avec forEach() – plus propre !
fruits.forEach((fruit) => {
  console.log(fruit);
});

/*
Sortie : 
apple
banana
orange
*/
```

## Conseil 21 : Utilisez l'API Web Audio pour travailler avec des fichiers audio

L'API Web Audio fournit des méthodes et des propriétés pour jouer, mettre en pause, contrôler le volume et effectuer d'autres tâches liées à l'audio.

Pour lire des fichiers audio ou créer un lecteur de musique avec l'API audio, vous devez l'utiliser en combinaison avec la balise audio (`<audio>`).

Voici comment je joue, mets en pause et contrôle le volume d'une chanson :

```html
<h1>Audio API</h1>

<audio id="my-audio" src="audio-file.mp3"></audio>
<div id="controls">
    <button id="play">Play</button>
    <button id="pause">Pause</button>
    <input type="range" id="volume" min="0" max="1" step="0.01" value="1" />
</div>
```

```js
const audioElement = document.querySelector('#my-audio');
const playBtn = document.querySelector('#play');
const pauseBtn = document.querySelector('#pause');
const volume = document.querySelector('#volume');

// jouer l'audio avec la méthode play()
playBtn.addEventListener('click', () => audioElement.play());

// mettre en pause l'audio avec la méthode pause()
pauseBtn.addEventListener('click', () => audioElement.pause());

// ajuster le volume avec la propriété volume
volume.addEventListener('change', () => (audioElement.volume = volume.value));
```

Lisez plus sur l'API audio web sur [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API).


## Conseil 22 : Utilisez l'API Web Video pour travailler avec des fichiers vidéo
L'API web vidéo vous permet de lire des fichiers vidéo avec les méthodes et propriétés intégrées. 

Tout comme l'API audio, vous pouvez jouer, mettre en pause, contrôler le volume d'une vidéo avec l'API vidéo. Vous devez également l'utiliser en combinaison avec la balise vidéo (`<video>`).

```html
<h1>Video API</h1>

<video id="my-video" src="video-file.mp4" poster="snail.jpg" width="500"
</video>

<div id="controls">
     <div id="current-time"></div>
     <button id="play">Play</button>
     <button id="pause">Pause</button>
</div>
```

```js
const videoElement = document.querySelector('#my-video');
const playBtn = document.querySelector('#play');
const pauseBtn = document.querySelector('#pause');
const videoTime = document.querySelector('#current-time');

// jouer la vidéo avec la méthode play()
playBtn.addEventListener('click', () => videoElement.play());

// mettre en pause la vidéo avec la méthode pause()
pauseBtn.addEventListener('click', () => videoElement.pause());

// afficher le temps de la vidéo avec la propriété currentTime
videoElement.addEventListener('timeupdate', () => {
  videoTime.innerText = videoElement.currentTime.toFixed(2);
});
```

Lisez plus sur l'API vidéo web sur [MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Video_and_audio_APIs).


## Conseil 23 : Préservez l'intégrité des objets en les scellant et en les gelant

Pour éviter de manipuler vos objets, vous pouvez les sceller avec `Object.seal` et les geler avec `Object.freeze()`.

Lorsque vous scellez un objet, vous ne pourrez plus ajouter et supprimer de propriétés :

```js
const person1 = {
  name: 'Kolade',
  luckyNum: 10,
  footballFan: true,
  club: 'Chelsea',
};

// scellez l'objet avec Object.seal()
Object.seal(person1);

console.log(person1.name); // Kolade

person1.favPet = 'Cat'; // Vous ne pouvez pas ajouter d'entrées à un objet scellé
console.log(person1.favPet); // undefined

delete person1.club; // Vous ne pouvez pas supprimer d'entrées d'un objet scellé
console.log(person1.club); // Chelsea

// Vous pouvez toujours modifier les valeurs des propriétés
person1.name = 'Kolade Chris';
console.log(person1.name); // Kolade Chris

// vérifiez si l'objet est scellé et gelé avec isSealed() et isFrozen()
console.log(Object.isSealed(person1)); // true
console.log(Object.isFrozen(person1)); // false
```

Lorsque vous gelez un objet, vous ne pouvez pas ajouter d'entrées, et l'objet est également scellé. Cela signifie que vous ne pouvez pas ajouter ou supprimer de celui-ci :

```js
const person2 = {
  name: 'Jane',
  luckyNum: 11,
  footballFan: true,
  club: 'Man United',
};

// gelez l'objet avec Object.freeze()
Object.freeze(person2);

console.log(person2.name); // Jane

person2.favPet = 'Cat'; // Vous ne pouvez pas ajouter d'entrées à un objet gelé
console.log(person2.favPet); // undefined

person2.name = 'Jane Doe';
console.log(person2.name); // Jane – rien ne change

delete person2.club; // Vous ne pouvez pas supprimer d'entrées d'un objet gelé
console.log(person2.club); // Man United

// vérifiez si l'objet est gelé et scellé avec isFrozen() et isSealed()
console.log(Object.isFrozen(person2)); // true
console.log(Object.isSealed(person2)); // true
// isSealed() retourne true car un objet gelé est également un objet scellé
```

La différence entre `Object.freeze()` et `Object.seal()` est que `Object.seal()` vous permet de modifier les entrées tandis que `Object.freeze()` ne le permet pas. Cela rend `Object.freeze()` plus fort.


## Conseil 24 : Utilisez `async...await` pour les opérations asynchrones

La syntaxe `async await` est plus simple et plus propre à utiliser. Donc, au lieu d'enchaîner plusieurs `.then()` tout en travaillant avec des données ou des opérations asynchrones qui retournent une `Promise`, vous devriez utiliser `async await`.

Voici à quoi ressemble l'enchaînement de plusieurs `.then()` :

```js
function fetchData1() {
  fetch('https://jsonplaceholder.typicode.com/users')
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(`There was an error: ${error}`));
}
```

Voici comment vous pouvez refactoriser le même code pour utiliser `async await` :

```js
async function fetchData2() {
  const response = await fetch('https://jsonplaceholder.typicode.com/users');
  const data = await response.json();
  console.log(data);
}
```

Vous ne pouvez pas utiliser `catch()` avec `async await`, donc vous devriez utiliser `try catch` pour gérer les erreurs :

```js
async function fetchData3() {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(`There was an error: ${error}`);
  }
}
```

Vous pouvez également utiliser des fonctions fléchées avec `async await` :

```js
const fetchData4 = async () => {
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(`There was an error: ${error}`);
  }
};
```

## Conseil 25 : Clonez les objets avec l'opérateur de propagation, `Object.assign()` et `JSON.parse()`

Il existe plusieurs façons et astuces pour cloner des objets, mais les méthodes les plus couramment utilisées sont l'utilisation de la syntaxe de propagation (`...`), `Object.assign()` et `JSON.parse()`.

```js
const originalObject = {
  name: 'Kolade',
  luckyNum: 10,
  isFootballFan: true,
  club: 'Chelsea',
};

// cloner avec l'opérateur de propagation
const clonedObject1 = { ...originalObject };

// cloner avec Object.assign()
const clonedObject2 = Object.assign({}, originalObject);

// clonage profond avec JSON.stringify() et JSON.parse()
const clonedObject3 = JSON.parse(JSON.stringify(originalObject));
console.table(clonedObject1);
console.table(clonedObject1);
console.table(clonedObject1);
```

Vous pouvez également créer un clone profond d'un objet avec `structuredClone()`. `structuredClone()` a été ajouté au langage JavaScript dans ECMAScript 2019.

```js
const clonedObject4 = structuredClone(originalObject);
console.table(clonedObject4);
```

Lisez plus sur la méthode `structuredClone()` sur [MDN](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone).


## Conseil 26 : Supprimez les doublons d'un tableau avec Set et Map

`Set` et `Map` sont des structures de données intégrées pour stocker des collections de valeurs, chacune avec ses propres caractéristiques et cas d'utilisation spécifiques.

Ni `Set` ni `Map` ne permettent les valeurs en double, vous pouvez donc les utiliser pour supprimer les doublons d'un tableau en les étalant dans ceux-ci :

```js
// créez des tableaux uniques avec Set()
const arrayWithDuplicates = [1, 2, 2, 3, 4, 4, 5];
const uniqueArray = [...new Set(arrayWithDuplicates)];

console.log(uniqueArray); // [1, 2, 3, 4, 5]

// créez des tableaux uniques avec Map()
const fruitsWithDuplicates2 = [
  'Mango',
  'Cashew',
  'Barley',
  'Mango',
  'Barley',
  'Berry',
  'Cashew',
];
const uniqueFruitsWithDuplicates2 = [
  ...new Map(fruitsWithDuplicates2.map((item) => [item, true])).keys(),
];

console.log(uniqueFruitsWithDuplicates2);
// [ 'Mango', 'Cashew', 'Barley', 'Berry' ]
```


## Conseil 27 : Parcourez un tableau et aplatissez-le avec la méthode `flatMap()`

Si vous souhaitez parcourir un tableau multidimensionnel et que vous souhaitez vous assurer que tous les éléments profondément imbriqués sont agrégés dans un seul tableau, vous pouvez utiliser la méthode `flatMap()`. Cela aplatira le tableau et le parcourra également.

Voici comment vous pouvez y parvenir en enchaînant `.flat()` à `.map()` :

```js
const numbers = [1, 2, 3, 4, 5];

const doubledAndSquared = numbers.map((num) => [num * 2, num * num]);
const flattenedArr = doubledAndSquared.flat();

console.log(doubledAndSquared); // [ [ 2, 1 ], [ 4, 4 ], [ 6, 9 ], [ 8, 16 ], [ 10, 25 ] ]
console.log(flattenedArr); //  [2, 1, 4, 4, 6, 9, 8, 16, 10, 25]
```

Et voici comment vous pouvez utiliser `flatMap()` pour faire la même chose :

```js
// combinez map et flat
const combinedMapAndFlat = numbers.flatMap((num) => [num * 2, num * num]);

console.log(combinedMapAndFlat); // Sortie : [2, 1, 4, 4, 6, 9, 8, 16, 10, 25];
```

N'est-ce pas génial ?


## Conseil 28 : Utilisez les méthodes `padStart()` et `padEnd()` pour remplir une chaîne avec un caractère

Les méthodes `padStart()` et `padEnd()` sont des méthodes de chaîne qui vous permettent de remplir une chaîne avec un caractère spécifié pour atteindre une longueur cible. Ces méthodes sont particulièrement pratiques pour formater des chaînes et aligner du texte en colonnes.

Voici l'utilisation de base :

```js
const originalString = 'Hello';
const paddedString = originalString.padStart(10, '*');
console.log(paddedString); // *****Hello

const originalString2 = 'World';
const paddedString2 = originalString2.padEnd(10, '-');
console.log(paddedString2); // World-----

// combinez padStart() et padEnd()
const text = 'Hello';
const paddedText = text.padStart(10, '-').padEnd(15, '+');
console.log(paddedText); // -----Hello+++++
```

Voici comment vous pouvez utiliser les deux méthodes pour aligner des éléments dans la console :

```js
const products = [
  { name: 'Apples', price: 1.5 },
  { name: 'Bananas', price: 0.75 },
  { name: 'Oranges', price: 2 },
];

console.log('Product      Price');
console.log('-------------------');

products.forEach(({ name, price }) => {
  const paddedName = name.padEnd(10, ' ');
  const formattedPrice = price.toFixed(2).padStart(8, ' ');
  console.log(`${paddedName}${formattedPrice}`);
});

/*
Sortie :

Product      Price
-------------------
Apples        1.50
Bananas       0.75
Oranges       2.00
*/
```

Et une meilleure utilisation est de formater le temps d'un lecteur de musique ou de vidéo dans le format `00:00` de `00:00` :

```js
function formatTime(currentTime, totalTime) {
  // Fonction auxiliaire pour remplir un nombre avec des zéros de tête
  const padWithZero = (num) => num.toString().padStart(2, '0');

  // Formatez le temps actuel en minutes:secondes
  const formattedCurrentTime = `${padWithZero(
    Math.floor(currentTime / 60)
  )}:${padWithZero(Math.floor(currentTime % 60))}`;

  // Formatez le temps total en minutes:secondes
  const formattedTotalTime = `${padWithZero(
    Math.floor(totalTime / 60)
  )}:${padWithZero(Math.floor(totalTime % 60))}`;

  // Combinez le temps actuel formaté et le temps total avec "of" entre les deux
  return `${formattedCurrentTime} of ${formattedTotalTime}`;
}

// Exemple de valeurs de temps
const currentTimeInSeconds = 125; // Exemple de temps actuel en secondes
const totalTimeInSeconds = 3600; // Exemple de temps total en secondes

// Formatez le temps et affichez le résultat
const formattedTime = formatTime(currentTimeInSeconds, totalTimeInSeconds);
console.log(formattedTime); // 02:05 of 60:00
```


## Conseil 29 : Utilisez la méthode `insertAdjacentHTML()` du DOM pour insérer une chaîne dans le DOM

La méthode `insertAdjacentHTML()` du DOM vous permet d'insérer une chaîne de HTML à une position spécifiée par rapport à un élément donné. Cette position pourrait être 'beforeend', 'afterend', 'beforebegin', ou 'afterbegin'.

Voici comment cela fonctionne :

```html
<div id="content">
   <p>This is an example.</p>
</div>

<button id="add-button">Add Paragraph</button>
```

```js
const addButton = document.getElementById('add-button');
const content = document.getElementById('content');

addButton.addEventListener('click', () => {
   const newParagraphHTML = '<p>This is a new paragraph.</p>';
   content.insertAdjacentHTML('afterend', newParagraphHTML);
});
```


## Conseil 30 : Utilisez la méthode `createTreeWalker()` du DOM pour parcourir le DOM

La méthode `createTreeWalker()` vous permet de parcourir les nœuds de l'arbre DOM et d'effectuer des actions sur eux en fonction de critères spécifiques.

Cette méthode peut être utile pour les structures de documents complexes ou les besoins de parcours spécialisés.

```html
<div id="content">
<p>This is a <span>paragraph</span> with some <em>emphasis</em>.</p>
<ul>
    <li>List item 1</li>
    <li>List item 2</li>
    <li>List item 3</li>
    <li>List item 4</li>
</ul>
</div>
```

Utilisez `createTreeWalker()` pour parcourir et afficher tous les nœuds de texte :

```js
const content = document.getElementById('content');
const treeWalker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT);

let node;
while ((node = treeWalker.nextNode())) {
  console.log(node.nodeValue.trim());
}
```

![ss7](https://www.freecodecamp.org/news/content/images/2023/08/ss7.png)

**N.B** : Les espaces blancs qualifient un nœud de texte – c'est pourquoi vous pouvez voir les espaces dans la sortie


## Conclusion
Chaque exemple de code dans cet article provient de mon défi 30 jours de JavaScript sur Twitter (maintenant, X). Vous pouvez consulter [mon profil Twitter](https://twitter.com/Ksound22).

J'espère que ces conseils vous aideront à comprendre certaines nuances de JavaScript et vous permettront de réaliser certaines choses dans vos projets web.