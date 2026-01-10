---
title: Quelles sont les valeurs Falsy en JavaScript ? Explications avec des exemples
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2024-01-30T15:27:25.000Z'
originalURL: https://freecodecamp.org/news/what-are-falsey-values-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-29-at-12.22.42-AM.png
tags:
- name: Conditionals
  slug: conditionals
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Quelles sont les valeurs Falsy en JavaScript ? Explications avec des exemples
seo_desc: 'In JavaScript, every value has a boolean equivalent. This means it can
  either be evaluated as true (truthy value) or false (falsy value) when used in a
  boolean context.

  But what is a boolean context? It''s a situation where a boolean value is expected...'
---

En JavaScript, chaque valeur a un équivalent booléen. Cela signifie qu'elle peut être évaluée comme vraie (valeur truthy) ou fausse (valeur falsy) lorsqu'elle est utilisée dans un contexte booléen.

Mais qu'est-ce qu'un contexte booléen ? C'est une situation où une valeur booléenne est attendue. Les exemples incluent les instructions if, les opérateurs logiques, et ainsi de suite. Lorsque vous utilisez une valeur non booléenne dans un contexte booléen, JavaScript convertira la valeur en son équivalent booléen.

Dans cet article, vous apprendrez les valeurs falsy en JavaScript et comment vérifier si une valeur est falsy. L'article couvre également certaines bonnes pratiques à considérer lors de la vérification de l'équivalent booléen d'une valeur.

Commençons !

## Table des matières

* [Les six valeurs Falsy en JavaScript](#les-six-valeurs-falsy-en-javascript)
  
* [Comment vérifier si une valeur est Falsy](#comment-verifier-si-une-valeur-est-falsy-en-javascript)
  
* [Valeurs Truthy qui peuvent apparaître comme des valeurs Falsy](#valeurs-truthy-qui-peuvent-apparaitre-comme-des-valeurs-falsy)
  
* [Bonnes pratiques lors de la vérification de l'équivalent booléen](#bonnes-pratiques-lors-de-la-verification-de-lequivalent-booleen)
  
* [Conclusion](#conclusion)
  

## Les six valeurs Falsy en JavaScript

Les valeurs falsy en JavaScript sont uniques car il n'y en a que six. À part ces six, toutes les autres valeurs sont des valeurs truthy.

Vous pouvez mémoriser ces valeurs falsy. Ainsi, lorsque vous rencontrerez une valeur qui n'est pas l'une des six, vous saurez qu'il s'agit d'une valeur `truthy`.

Voici les six valeurs falsy en JavaScript :

* `false` : La valeur booléenne `false`.
  
* `0` : Le nombre zéro.
  
* `""` ou `''` ou \`\`\`\` : Une chaîne de caractères vide.
  
* `null` : Le mot-clé null, représentant l'absence de toute valeur d'objet.
  
* `undefined` : Le mot-clé undefined, représentant une valeur non initialisée.
  
* `NaN` : Signifie "Not a Number". Il représente une valeur spéciale retournée par une opération qui devrait retourner une valeur numérique mais ne le fait pas.
  

Maintenant, voyons quelques exemples pratiques de ces valeurs falsy en JavaScript.

### Exemple 1 – La valeur booléenne `false`.

```javascript
let isOnline = false

function checkStatus(status) {
  return Boolean(status) ? "ONLINE" : "OFFLINE"
}

checkStatus(isOnline) // "OFFLINE"
```

Lorsque vous passez la variable `isOnline` à la fonction `checkStatus`, elle retourne la chaîne `"OFFLINE"`. Et cela est dû au fait que la valeur est `false` dans ce contexte. Ici, nous utilisons un opérateur ternaire basé sur la valeur booléenne de l'argument `status`.

### Exemple 2 – Le nombre zéro.

```javascript
let unreadMessages = 0
let hasUnreadMessages = Boolean(unreadMessages)
console.log(hasUnreadMessages) // false
```

Cet exemple vérifie si un utilisateur a des messages non lus ou non. Nous utilisons la fonction intégrée `Boolean` pour obtenir la valeur booléenne de la variable `unreadMessages`. Cela signifie que chaque fois que le nombre de `unreadMessages` est zéro, `hasUnreadMessages` sera `false`.

### Exemple 3 – Une chaîne de caractères vide.

```javascript
let userInput = "";
let defaultText = "No input provided";

let displayText = Boolean(userInput) || defaultText;

console.log(displayText); // No input provided
```

Cet exemple utilise l'opérateur logique OR `||` pour déterminer la valeur de `displayText`. Il assignera la valeur de `userInput` à `displayText` si elle est une valeur truthy. Ou il assignera le `defaultText` à `displayText` si `userInput` est une valeur falsy comme c'est le cas ici.

### Exemple 4 – `null`

```javascript
let user = null;

if (user && user.name) {
    console.log("Welcome, " + user.name + "!");
} else {
    console.log("Please log in to access the website.");
}
```

L'exemple suivant suppose que l'utilisateur n'est pas connecté et donc la valeur de l'objet `user` est `null`. Cela signifie que l'instruction `if` sera évaluée à `false`. Le comportement attendu sera alors que le code exécute le bloc `else`.

### Exemple 5 – `undefined`

```javascript
let age;
if (age === undefined) {
    console.log("The age is undefined.");
}
```

Lorsque une variable est déclarée mais non initialisée avec une valeur, JavaScript lui attribue la valeur `undefined` par défaut. Dans l'exemple de code ci-dessus, puisque la variable `age` est déclarée mais non assignée à une valeur, sa valeur est `undefined`. Cela signifie que le code dans l'instruction `if` sera exécuté.

### Exemple 6 – `NaN`

```javascript
let value1 = "Ten"
let value2 = 10

let result = value1 / value2

if (isNaN(result)) {
    console.log("The result is not a number.");
} else {
    console.log(result);
}
```

Cet exemple divise `value1` (une chaîne de caractères) par `value2` (un nombre). Cela résultera en une valeur `NaN` car vous ne pouvez pas diviser une chaîne de caractères par un nombre. Cela signifie que le code dans le bloc `if` sera exécuté. Et il enregistrera `The result is not a number` dans la console.

## Comment vérifier si une valeur est Falsy en JavaScript

Une manière sûre de vérifier si une valeur est falsy ou non est d'utiliser la fonction `Boolean`. La fonction `Boolean` retourne la valeur booléenne de la valeur de l'argument qui lui est passé.

Exemple :

```javascript
console.log(Boolean(false))
console.log(Boolean(0))
console.log(Boolean(""))
console.log(Boolean(null))
console.log(Boolean(undefined))
console.log(Boolean(NaN))
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-23-at-6.16.42-PM.png align="left")

*Résultats de log booléen pour toutes les six valeurs falsy.*

Ici, nous vérifions la valeur booléenne de toutes les six valeurs falsy. Et comme prévu, chacune retourne `false`.

Lorsque vous passez toute autre valeur qui n'est pas l'une de ces six valeurs falsy à la fonction Boolean, elle retournera `true`.

Exemple :

```javascript
console.log(Boolean('hello'))
console.log(Boolean(24))
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-23-at-6.24.35-PM.png align="left")

*Exemple de résultats de log booléen pour des valeurs truthy.*

## Valeurs Truthy qui peuvent apparaître comme des valeurs Falsy

Il y a certaines valeurs truthy qui, à première vue, peuvent apparaître comme des valeurs falsy mais qui ne le sont pas. Comme déjà mentionné, seules six valeurs en JavaScript sont des valeurs falsy. Tout le reste est une valeur truthy.

Voici quelques-unes de ces valeurs qui ne sont pas falsy mais qui peuvent apparaître comme telles.

```javascript
console.log(Boolean('false')) // Une chaîne avec le texte "false"
console.log(Boolean(' ')) // Une chaîne avec un espace
console.log(Boolean('0')) // Une chaîne avec zéro
console.log(Boolean([])) // Un tableau vide
console.log(Boolean({})) // Un objet vide
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-24-at-8.09.17-AM.png align="left")

*Résultats de log pour des valeurs truthy qui apparaissent comme falsy.*

Les trois premières chaînes contiennent du texte qui peut ressembler à des valeurs falsy. La première est la chaîne avec le texte `"false"`, une autre avec un espace, et la troisième avec zéro.

Rappelez-vous que la seule chaîne considérée comme une valeur falsy est une chaîne vide. Toutes les chaînes non vides en JavaScript sont des valeurs truthy, y compris les chaînes avec uniquement des espaces.

De plus, notez que contrairement aux chaînes, un tableau vide et un objet vide retournent `true` dans un contexte booléen.

## Bonnes pratiques lors de la vérification de l'équivalent booléen

Les conseils suivants vous aideront à rendre votre code plus lisible et plus facile à maintenir.

### 1. Utilisez la fonction Boolean

Il est toujours préférable d'utiliser la fonction intégrée `Boolean` lorsque vous voulez vérifier si une valeur est truthy ou falsy. La fonction fonctionne en forçant toute valeur à son booléen correspondant. Elle rend également votre intention claire pour quiconque lit le code.

Exemple :

```javascript
// Exemple sans la fonction Boolean
const value = ''; 

if (value) {
    console.log('It is a TRUTHY value');
} else {
    console.log('It is a FALSY value');
}

// Exemple avec la fonction Boolean
const value = ''

if (Boolean(value)) {
    console.log('It is a TRUTHY value');
} else {
    console.log('It is a FALSY value');
}
```

Les deux exemples font la même chose. Mais dans le deuxième exemple, il est explicite que vous vérifiez la représentation booléenne de la valeur donnée.

### 2. Utilisez l'égalité stricte `===` au lieu de l'égalité lâche `==`

Lorsque vous comparez des valeurs pour leur vérité ou leur fausseté, il est recommandé d'utiliser l'égalité stricte (`===`) plutôt que l'égalité lâche (`==`). L'égalité stricte compare à la fois la valeur et le type. L'égalité lâche effectue une coercition de type avant de comparer les valeurs, et cela peut conduire à des résultats inattendus.

Exemple :

```javascript
// Exemple d'égalité stricte

if (1 === [1]) {
  console.log('EQUAL')
} else {
  console.log('NOT EQUAL')
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-28-at-11.31.28-PM.png align="left")

*Résultat de log pour l'exemple d'égalité stricte.*

```javascript
// Exemple d'égalité lâche
if (1 == [1]) {
  console.log('EQUAL')
} else {
  console.log('NOT EQUAL')
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-28-at-11.32.20-PM.png align="left")

*Résultat de log pour l'exemple d'égalité lâche.*

Les deux exemples ci-dessus comparent les mêmes valeurs. Mais l'exemple d'égalité stricte log "NOT EQUAL". Cela est dû au fait que le nombre 1 n'est pas égal à un tableau contenant le nombre 1. Avec l'égalité lâche, il force le type des valeurs pour les rendre du même type. C'est pourquoi il log "EQUAL" dans la console.

### 3. Ajoutez des commentaires pour documenter votre code

Pour rendre votre code plus lisible et plus facile à maintenir, envisagez d'ajouter des commentaires lorsque cela est nécessaire pour expliquer votre logique lorsque vous traitez avec des valeurs truthy et falsy.

Documenter votre code est une bonne pratique pour aider les développeurs de votre équipe (ou votre futur vous-même) à comprendre le comportement attendu d'un morceau de code.

Exemple :

```javascript
let selectedUser = USER_OBJ

// Vérifie si aucun utilisateur n'est sélectionné
if (!selectedUser) {
    console.log("Please select a user.");
} else {
    console.log("User address: " + selectedUser.address);
}
```

Dans l'exemple ci-dessus, le commentaire ajouté avant l'instruction `if` clarifie que le code vérifie si aucun utilisateur n'a été sélectionné.

L'utilisation de l'opérateur logique NOT (`!`) peut donner l'impression que vous vérifiez si un utilisateur est sélectionné plutôt que de vérifier si aucun utilisateur n'est sélectionné. Donc un commentaire dans un cas comme celui-ci aide à fournir de la clarté.

## Conclusion

Dans cet article, vous avez appris les six valeurs falsy en JavaScript et comment elles diffèrent des valeurs truthy. Vous avez également appris certaines valeurs truthy qui peuvent apparaître comme falsy, mais qui ne le sont pas. Et vous avez également vu certaines bonnes pratiques à considérer lorsque vous travaillez avec des valeurs falsy.

Une bonne compréhension du concept des valeurs falsy et truthy et de la manière dont elles affectent les comparaisons et les instructions conditionnelles sera utile lors du débogage des applications JavaScript.

Merci d'avoir lu. Et bon codage ! Pour des tutoriels plus approfondis, n'hésitez pas à [vous abonner à ma chaîne YouTube](https://www.youtube.com/@DevAfterHours).