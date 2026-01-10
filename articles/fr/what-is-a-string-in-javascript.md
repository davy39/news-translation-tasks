---
title: Qu'est-ce qu'une chaîne de caractères en JS ? La variable String JavaScript
  expliquée
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-02-03T19:26:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-string-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-template--1-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce qu'une chaîne de caractères en JS ? La variable String JavaScript
  expliquée
seo_desc: 'When learning JavaScript or any programming language, you''ll encounter
  the keyword or term string.

  A string represents textual data, which is a fundamental part of many applications.
  You can also use strings to interact with users through prompts, al...'
---

Lorsque vous apprenez JavaScript ou tout autre langage de programmation, vous rencontrerez le mot-clé ou le terme string.

Une chaîne de caractères représente des données textuelles, qui constituent une partie fondamentale de nombreuses applications. Vous pouvez également utiliser des chaînes de caractères pour interagir avec les utilisateurs via des invites, des alertes et d'autres formes d'entrée et de sortie utilisateur.

Dans cet article, vous apprendrez ce qu'est une chaîne de caractères, comment elle fonctionne en JavaScript, comment créer une chaîne de caractères et comment échapper les guillemets et les apostrophes dans les chaînes de caractères.

## Qu'est-ce qu'une chaîne de caractères en JavaScript ?

En JavaScript, une chaîne de caractères est un type de données représentant une séquence de caractères qui peut consister en des lettres, des nombres, des symboles, des mots ou des phrases.

Nous utilisons des chaînes de caractères pour représenter des données basées sur du texte et nous les définissons en utilisant soit des guillemets simples (`'`), des guillemets doubles (`"`), ou des backticks (\`\`):

```js
let name1 = 'John Doe';
let name2 = "John Doe";
let name3 = `John Doe`;
```

Dans l'exemple ci-dessus, vous avez trois chaînes de caractères assignées à différentes variables. Pour être sûr qu'elles sont toutes des chaînes de caractères, vous pouvez vérifier le type de la variable :

```js
console.log(typeof(name1)); // string
console.log(typeof(name2)); // string
console.log(typeof(name3)); // string
```

Il est important de savoir qu'en JavaScript, les chaînes de caractères sont immuables. Cela signifie qu'une fois une chaîne de caractères créée, son contenu ne peut pas être modifié.

Au lieu de cela, vous devez créer une nouvelle chaîne de caractères représentant la version modifiée lorsque vous souhaitez modifier une chaîne de caractères.

Par exemple, si vous avez une chaîne de caractères assignée à une variable, vous ne pouvez pas la modifier. Au lieu de cela, vous créerez une nouvelle chaîne de caractères et assignerez la nouvelle chaîne à la même variable comme ceci :

```js
let name = "John Doe";
name = "Jane Doe";
```

Cela signifie que la chaîne de caractères originale `"John Doe"` existe toujours en mémoire, mais la variable `name` fait maintenant référence à la nouvelle chaîne de caractères `"Jane Doe"`.

Les chaînes de caractères en JavaScript peuvent être transformées et traitées de diverses manières, telles que les convertir en majuscules ou en minuscules, extraire des sous-chaînes, rechercher des caractères ou des séquences spécifiques, et comparer des chaînes de caractères pour déterminer si elles sont égales.

Ces capacités font des chaînes de caractères un outil polyvalent et puissant pour les développeurs. Elles disposent d'un certain nombre de méthodes et de propriétés intégrées qui permettent aux développeurs de manipuler et de travailler avec des chaînes de caractères. Explorons-en quelques-unes.

## Concatenation de chaînes de caractères en JavaScript

En JavaScript, la concaténation de chaînes de caractères combine deux ou plusieurs chaînes de caractères en une seule chaîne avec leurs variables. Vous pouvez le faire en utilisant l'opérateur `+`, comme le montre l'exemple ci-dessous :

```js
let firstName = "John";
let lastName = "Doe";
let fullName = firstName + " " + lastName;
console.log(fullName); // John Doe
```

Dans cet exemple, vous ajoutez une chaîne de caractères vide (`" "`) entre les deux pour créer un espace entre les deux chaînes de caractères. Une autre façon de concaténer des chaînes de caractères en JavaScript est d'utiliser la méthode `concat()`, qui est disponible sur chaque objet chaîne de caractères. Par exemple :

```js
let firstName = "John";
let lastName = "Doe";
let fullName = firstName.concat(" ", lastName);
console.log(fullName); // John Doe
```

## Concatenation de chaînes de caractères en JavaScript avec les littéraux de gabarit

En JavaScript, vous pouvez également utiliser des littéraux de gabarit pour la concaténation de chaînes de caractères. Un littéral de gabarit est un type spécial de chaîne de caractères que vous définissez en utilisant des backticks (\`\`\`) au lieu de guillemets (`'` ou `"`).

Les littéraux de gabarit peuvent contenir des expressions évaluées (telles que des variables) et concaténées avec le texte environnant, comme le montre l'exemple ci-dessous :

```js
let firstName = "John";
let lastName = "Doe";
let fullName = `${firstName} ${lastName}`;
console.log(fullName); // John Doe
```

Les littéraux de gabarit fournissent un moyen concis et lisible de concaténer des chaînes de caractères et d'insérer des expressions dans des chaînes de caractères. Ils prennent également en charge les sauts de ligne et d'autres caractères spéciaux, ce qui en fait un outil flexible pour la manipulation de chaînes de caractères en JavaScript.

## Comment échapper les guillemets et les apostrophes dans les chaînes de caractères

En JavaScript, si vous devez inclure un guillemet ou une apostrophe dans une chaîne de caractères, vous devez l'échapper en utilisant une barre oblique inverse (`\`) car le fait de ne pas le faire générera une erreur, comme le montre l'exemple ci-dessous :

```js
let quote = "He said, "I learned from freeCodeCamp!"";
```

Cela générera l'erreur suivante :

```js
Uncaught SyntaxError: Unexpected identifier 'I'
```

Pour corriger cela, vous pouvez utiliser le type de guillemet opposé. Par exemple, si votre guillemet contient un guillemet double, enveloppez votre chaîne de caractères avec un guillemet simple et vice versa :

```js
let quote = 'He said, "I love JavaScript!"';
let apostrophe = "It's a beautiful day";
```

Vous pouvez en apprendre davantage sur [comment échapper les chaînes de caractères en JavaScript dans cet article](https://www.freecodecamp.org/news/how-to-escape-strings-in-javascript/).

## Comment convertir une chaîne de caractères en majuscules ou en minuscules avec JavaScript

En JavaScript, vous pouvez convertir une chaîne de caractères en majuscules ou en minuscules en utilisant les méthodes `toUpperCase()` et `toLowerCase()`, respectivement. Ces méthodes retournent une nouvelle chaîne de caractères avec tous les caractères en majuscules ou en minuscules, comme le montre l'exemple ci-dessous :

```js
let myString = "Welcome to freeCodeCamp!";
let upperCaseString = myString.toUpperCase();
let lowerCaseString = myString.toLowerCase();

console.log(upperCaseString); // "WELCOME TO FREECODECAMP!"
console.log(lowerCaseString); // "welcome to freecodecamp!"
```

Notez que ces méthodes ne modifient pas la chaîne de caractères originale mais retournent une nouvelle chaîne de caractères avec la casse souhaitée. La chaîne de caractères originale reste inchangée puisque les chaînes de caractères sont immuables.

## Conclusion

Il est important pour vous de savoir qu'il y a plus à savoir sur les chaînes de caractères en JavaScript, mais cet article est une introduction de base aux chaînes de caractères, à leur fonctionnement et à leur utilisation pour des opérations simples.

Vous pouvez explorer [les méthodes de chaînes de caractères](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Useful_string_methods) pour savoir comment manipuler les chaînes de caractères.

Vous pouvez accéder à plus de 180 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.