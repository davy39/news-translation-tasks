---
title: Comment fonctionnent les types dans TypeScript – Expliqué avec du code JavaScript
  + TypeScript
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-20T21:05:51.000Z'
originalURL: https://freecodecamp.org/news/basic-typescript-types
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Comment fonctionnent les types dans TypeScript – Expliqué avec du code
  JavaScript + TypeScript
seo_desc: 'TypeScript is a superset of JavaScript that introduces static typing to
  JavaScript. TypeScript''s enhanced type safety and code maintainability empower
  developers to write code more confidently.

  A fundamental aspect of TypeScript''s static typing syste...'
---

TypeScript est un sur-ensemble de JavaScript qui introduit la typage statique à JavaScript. La sécurité des types améliorée et la maintenabilité du code de TypeScript permettent aux développeurs d'écrire du code avec plus de confiance.

Un aspect fondamental du système de typage statique de TypeScript est son support pour les types de base. Ceux-ci fournissent une base pour définir la forme et le comportement des données au sein des applications TypeScript.

Dans ce guide complet, nous explorerons les types de base de TypeScript en les comparant avec leurs équivalents JavaScript. Je clarifierai également les différences et les avantages offerts par les fonctionnalités de typage statique de TypeScript.

Vous pouvez obtenir tout le code JavaScript et TypeScript à partir d'[ici](https://github.com/dotslashbit/fcc-article-resources/tree/main/ts-basic-types).

## Table des matières

* [Comprendre les annotations de type](#heading-comprendre-les-annotations-de-type)
* [Types de base JavaScript vs TypeScript](#heading-javascript-vs-typescript-types-de-base)
* [Conclusion](#heading-conclusion)

## Comprendre les annotations de type

L'annotation de type dans TypeScript implique de spécifier explicitement le type de données des variables, des paramètres de fonction et des valeurs de retour. Cette annotation améliore la clarté du code et permet à TypeScript de vérifier les types statiques pour détecter les erreurs lors de la compilation. Cela améliore la qualité et la maintenabilité du code.

Dans TypeScript, les annotations de type sont écrites en utilisant un deux-points (`:`) suivi du type souhaité. Explorons comment les annotations de type sont appliquées dans les types de base de TypeScript :

## Types de base JavaScript vs TypeScript

### Booléen

Voici comment vous écririez un booléen en JavaScript :

```javascript
let isDone = false;
console.log("isDone:", isDone); // Sortie : isDone: false
if (!isDone) {
    console.log("La tâche n'est pas encore terminée.");
}

```

En JavaScript, une variable booléenne `isDone` est déclarée et initialisée avec la valeur `false`. La condition `!isDone` vérifie si `isDone` est `false`, et si vrai, enregistre un message indiquant que la tâche n'est pas encore terminée.

Et voici comment vous déclareriez un booléen en TypeScript :

```typescript
let isDone: boolean = false;
console.log("isDone:", isDone); // Sortie : isDone: false
if (!isDone) {
    console.log("La tâche n'est pas encore terminée.");
}

```

En TypeScript, la même variable booléenne `isDone` est déclarée avec une annotation de type explicite `: boolean` indiquant qu'elle ne peut contenir que des valeurs booléennes. Le comportement et la sortie restent les mêmes qu'en JavaScript.

### Nombre

Voici comment vous déclarez un nombre en JavaScript :

```javascript
let count = 42;
let totalPrice = 24.99;
let quantity = 10;
console.log("count:", count); // Sortie : count: 42
console.log("totalPrice:", totalPrice); // Sortie : totalPrice: 24.99
console.log("quantity:", quantity); // Sortie : quantity: 10

```

En JavaScript, les variables numériques `count`, `totalPrice` et `quantity` sont déclarées et initialisées avec des valeurs numériques. Chaque valeur représente un type numérique différent (entier, virgule flottante, entier respectivement).

Et en TypeScript :

```typescript
let count: number = 42;
let totalPrice: number = 24.99;
let quantity: number = 10;
console.log("count:", count); // Sortie : count: 42
console.log("totalPrice:", totalPrice); // Sortie : totalPrice: 24.99
console.log("quantity:", quantity); // Sortie : quantity: 10

```

En TypeScript, des annotations de type `: number` sont ajoutées à chaque déclaration de variable, spécifiant explicitement qu'elles ne peuvent contenir que des valeurs numériques. Cela fournit une clarté et une sécurité de type similaires à JavaScript.

### Chaîne de caractères

Voici comment vous écrivez une chaîne de caractères en JavaScript :

```javascript
let message = "Bonjour, JavaScript !";
let firstName = "John";
let lastName = "Doe";
console.log("message:", message); // Sortie : message: Bonjour, JavaScript !
console.log("firstName:", firstName); // Sortie : firstName: John
console.log("lastName:", lastName); // Sortie : lastName: Doe

```

En JavaScript, les variables de chaîne de caractères `message`, `firstName` et `lastName` sont déclarées et initialisées avec des valeurs de chaîne de caractères.

Et voici comment vous le faites en TypeScript :

```typescript
let message: string = "Bonjour, TypeScript !";
let firstName: string = "John";
let lastName: string = "Doe";
console.log("message:", message); // Sortie : message: Bonjour, TypeScript !
console.log("firstName:", firstName); // Sortie : firstName: John
console.log("lastName:", lastName); // Sortie : lastName: Doe

```

En TypeScript, des annotations de type `: string` sont ajoutées à chaque déclaration de variable, spécifiant explicitement qu'elles ne peuvent contenir que des valeurs de chaîne de caractères. Cela améliore la lisibilité et la maintenabilité du code.

### Tableau

Voici comment vous pouvez déclarer un tableau en JavaScript :

```javascript
let numbers = [1, 2, 3, 4, 5];
let fruits = ["apple", "banana", "orange"];
console.log("numbers:", numbers); // Sortie : numbers: [1, 2, 3, 4, 5]
console.log("fruits:", fruits); // Sortie : fruits: ["apple", "banana", "orange"]

```

En JavaScript, les tableaux `numbers` et `fruits` sont déclarés et initialisés avec des valeurs numériques et des chaînes de caractères respectivement.

Voici comment vous le faites en TypeScript :

```typescript
let numbers: number[] = [1, 2, 3, 4, 5];
let fruits: string[] = ["apple", "banana", "orange"];
console.log("numbers:", numbers); // Sortie : numbers: [1, 2, 3, 4, 5]
console.log("fruits:", fruits); // Sortie : fruits: ["apple", "banana", "orange"]

```

En TypeScript, des annotations de type sont ajoutées pour déclarer des tableaux avec des types d'éléments spécifiques (`: number[]` et `: string[]`), garantissant que seules des valeurs numériques ou des chaînes de caractères peuvent être stockées dans les tableaux `numbers` et `fruits` respectivement.

### Tuple

Voici comment vous écririez un tuple en TypeScript :

```typescript
let person: [string, number] = ["John", 30];
console.log("person:", person); // Sortie : person: ["John", 30]

```

En TypeScript, un tuple `person` est déclaré avec une annotation de type explicite `[string, number]`, indiquant qu'il doit contenir une chaîne de caractères suivie d'un nombre. Il stocke le nom et l'âge d'une personne.

Et voici la simulation en JavaScript :

```javascript
// JavaScript ne dispose pas d'un support intégré pour les tuples, mais nous pouvons utiliser des tableaux.
let person = ["John", 30];
console.log("person:", person); // Sortie : person: ["John", 30]

```

En JavaScript, puisque les tuples ne sont pas supportés, les tableaux sont souvent utilisés comme solution de contournement pour simuler un comportement similaire aux tuples. Le tableau `person` stocke le nom et l'âge d'une personne, similaire à l'exemple TypeScript.

### Enum

Voici comment vous déclareriez une énumération en TypeScript :

```typescript
enum Direction {
    Up,
    Down,
    Left,
    Right
}
let direction: Direction = Direction.Up;
console.log("direction:", direction); // Sortie : direction: 0

```

En TypeScript, une énumération `Direction` est déclarée avec des constantes nommées `Up`, `Down`, `Left` et `Right`, qui sont assignées à des valeurs numériques commençant par 0 par défaut. La variable `direction` est assignée à la valeur `Direction.Up`.

Et voici la simulation en JavaScript :

```javascript
// JavaScript ne dispose pas d'un support intégré pour les énumérations, mais nous pouvons utiliser des objets ou des constantes.
const Direction = {
    Up: 0,
    Down: 1,
    Left: 2,
    Right: 3
};
let direction = Direction.Up;
console.log("direction:", direction); // Sortie : direction: 0

```

En JavaScript, les énumérations ne sont pas supportées nativement, donc des objets ou des constantes sont souvent utilisés pour simuler un comportement similaire aux énumérations. Ici, l'objet `Direction` contient des constantes nommées mappées à des valeurs numériques, et la variable `direction` est assignée à la valeur de `Direction.Up`, similaire à l'exemple TypeScript.

## Conclusion

Les types de base de TypeScript offrent des avantages significatifs par rapport à JavaScript traditionnel en termes de sécurité des types, de clarté et de maintenabilité.

En introduisant des annotations de type explicites et des constructions de type supplémentaires telles que les tuples et les énumérations, TypeScript permet aux développeurs d'écrire un code plus robuste et sans erreur.

Comprendre les différences entre les types de base JavaScript et TypeScript est essentiel pour exploiter tout le potentiel des capacités de typage statique de TypeScript dans le développement web moderne.

Si vous avez des commentaires, vous pouvez me contacter en message privé sur [Twitter](https://twitter.com/introvertedbot) ou [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/).