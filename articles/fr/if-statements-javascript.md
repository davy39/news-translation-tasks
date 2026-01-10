---
title: Comment utiliser les instructions If en JavaScript – un guide pour débutants
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2023-11-20T21:45:44.000Z'
originalURL: https://freecodecamp.org/news/if-statements-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Pink-Elegant-Group-Project-Education-Presentation.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les instructions If en JavaScript – un guide pour débutants
seo_desc: "JavaScript is a powerful and versatile programming language that is widely\
  \ used for creating dynamic and interactive web pages. \nOne of the fundamental\
  \ building blocks of JavaScript programming is the if statement. if statements allow\
  \ developers to c..."
---

JavaScript est un langage de programmation puissant et polyvalent largement utilisé pour créer des pages web dynamiques et interactives.

L'une des briques fondamentales de la programmation JavaScript est l'instruction `if`. Les instructions `if` permettent aux développeurs de contrôler le flux de leurs programmes en prenant des décisions basées sur certaines conditions.

Dans cet article, nous allons explorer les bases des instructions `if` en JavaScript, comprendre leur syntaxe et voir comment elles peuvent être utilisées pour créer un code plus réactif et intelligent.

## Qu'est-ce qu'une instruction `if` ?

Une instruction `if` est une instruction conditionnelle qui vous permet d'exécuter un bloc de code uniquement si une condition spécifiée est vraie. En d'autres termes, elle fournit un moyen de prendre des décisions dans votre code.

Par exemple, vous pouvez vouloir afficher un message à l'utilisateur s'il a saisi le bon mot de passe, ou vous pouvez vouloir effectuer une certaine action uniquement si une variable a une valeur spécifique.

Voici un exemple simple pour illustrer la structure de base d'une instruction `if` :

```javascript
let temperature = 25;

if (temperature > 20) {
  console.log("Il fait chaud aujourd'hui !");
}
```

Dans cet exemple, l'instruction `if` vérifie si la valeur de la variable `temperature` est supérieure à 20. Si la condition est vraie, le code à l'intérieur des accolades (`{}`) est exécuté, et le message "Il fait chaud aujourd'hui !" est enregistré dans la console.

## Syntaxe des instructions `if`

La syntaxe d'une instruction `if` en JavaScript est simple. Elle se compose du mot-clé `if` suivi d'une paire de parenthèses contenant une condition. Si la condition est évaluée à `true`, le code à l'intérieur des accolades est exécuté. Voici la syntaxe de base :

```javascript
if (condition) {
  // Code à exécuter si la condition est vraie
}
```

Décomposons les composants de l'instruction `if` :

* **Mot-clé `if` :** C'est le mot-clé qui commence l'instruction `if` et est suivi d'une paire de parenthèses.
* **Condition :** À l'intérieur des parenthèses, vous fournissez la condition que vous souhaitez évaluer. Cette condition doit aboutir à une valeur booléenne (`true` ou `false`).
* **Bloc de code :** Le bloc de code est enfermé dans des accolades `{}`. Si la condition est vraie, le code à l'intérieur du bloc est exécuté.

Il est important de noter que les accolades sont essentielles, même si le bloc ne contient qu'une seule instruction. Inclure les accolades rend votre code plus lisible et aide à prévenir les bugs qui peuvent survenir lors de l'ajout de plus d'instructions au bloc plus tard.

## Instructions `if` simples

Plongeons plus profondément dans les instructions `if` simples en explorant quelques exemples. Les instructions `if` simples se composent d'une seule condition et d'un bloc de code qui s'exécute lorsque la condition est vraie.

### Exemple 1 : Vérification d'un nombre

```javascript
let number = 7;

if (number > 0) {
  console.log("Le nombre est positif.");
}
```

Dans cet exemple, l'instruction `if` vérifie si la valeur de la variable `number` est supérieure à 0. Si la condition est vraie, le message "Le nombre est positif." est enregistré dans la console.

### Exemple 2 : Vérification de l'entrée utilisateur

```javascript
let userInput = prompt("Entrez votre âge :");

if (userInput >= 18) {
  console.log("Vous êtes éligible pour voter.");
}
```

Cet exemple utilise la fonction `prompt` pour obtenir l'âge de l'utilisateur comme entrée. L'instruction `if` vérifie ensuite si l'âge saisi est supérieur ou égal à 18. Si vrai, le message "Vous êtes éligible pour voter." est enregistré dans la console.

### Exemple 3 : Vérification de l'égalité

```javascript
let password = "secure123";

if (password === "secure123") {
  console.log("Accès autorisé.");
}
```

Dans cet exemple, l'instruction `if` vérifie si la valeur de la variable `password` est exactement égale à la chaîne "secure123". Si la condition est vraie, le message "Accès autorisé." est enregistré dans la console.

## Instructions If-Else

Bien que les instructions `if` simples soient utiles, souvent vous voudrez fournir une action alternative lorsque la condition est fausse. C'est là que l'instruction `if-else` est utile. Le bloc `else` contient le code qui s'exécute lorsque la condition `if` est fausse.

### Exemple : Instruction If-Else

```javascript
let hour = 14;

if (hour < 12) {
  console.log("Bonjour !");
} else {
  console.log("Bon après-midi !");
}
```

Dans cet exemple, l'instruction `if` vérifie si la valeur de la variable `hour` est inférieure à 12. Si vrai, elle enregistre "Bonjour !" dans la console. Sinon, elle enregistre "Bon après-midi !".

## Instructions If-Else If

Parfois, vous pouvez avoir plusieurs conditions à vérifier. Dans de tels cas, vous pouvez utiliser des instructions `else if` pour ajouter des conditions supplémentaires. Le code à l'intérieur du premier bloc de condition vraie rencontrée sera exécuté, et les conditions suivantes seront ignorées.

### Exemple : Instruction If-Else If

```javascript
let grade = 85;

if (grade >= 90) {
  console.log("A");
} else if (grade >= 80) {
  console.log("B");
} else if (grade >= 70) {
  console.log("C");
} else {
  console.log("D");
}
```

Dans cet exemple, le code détermine la note d'un élève en fonction de son score. Il vérifie d'abord si la note est supérieure ou égale à 90, et si vrai, il enregistre "A". Si non, il passe à la condition suivante et vérifie si la note est supérieure ou égale à 80, et ainsi de suite. Si aucune des conditions n'est vraie, il enregistre "D".

## Instructions `if` imbriquées

Vous pouvez également imbriquer des instructions `if` à l'intérieur d'autres instructions `if` pour créer des structures de décision plus complexes. Chaque instruction `if` dans la structure imbriquée ajoute une couche supplémentaire de conditions.

### Exemple : Instruction `if` imbriquée

```javascript
let temperature = 25;
let isSummer = true;

if (isSummer) {
  if (temperature > 30) {
    console.log("C'est une journée d'été chaude !");
  } else {
    console.log("C'est une journée d'été chaude.");
  }
} else {
  console.log("Ce n'est pas l'été.");
}
```

Dans cet exemple, l'instruction `if` extérieure vérifie si c'est l'été. Si vrai, elle entre dans la structure imbriquée et vérifie la température. Selon la température, elle enregistre différents messages. Si ce n'est pas l'été, elle enregistre "Ce n'est pas l'été."

## Opérateurs logiques dans les instructions `if`

JavaScript fournit des opérateurs logiques (`&&`, `||`, `!`) qui vous permettent de combiner plusieurs conditions dans une seule instruction `if`.

### Exemple : Opérateurs logiques

```javascript
let age = 25;
let hasLicense = true;

if (age >= 18 && hasLicense) {
  console.log("Vous êtes éligible pour conduire.");
} else {
  console.log("Vous n'êtes pas éligible pour conduire.");
}
```

Dans cet exemple, l'opérateur `&&` (ET logique) combine deux conditions : l'âge de la personne étant 18 ans ou plus et ayant un permis valide. Si les deux conditions sont vraies, il enregistre "Vous êtes éligible pour conduire." Sinon, il enregistre "Vous n'êtes pas éligible pour conduire."

## Instructions Switch

Dans les situations où vous avez plusieurs conditions possibles à vérifier contre une seule valeur, une instruction `switch` peut être plus concise qu'une série d'instructions `if-else if`.

### Exemple : Instruction Switch

```javascript
let dayOfWeek = "Wednesday";

switch (dayOfWeek) {
  case "Monday":
    console.log("C'est le début de la semaine.");
    break;
  case "Wednesday":
    console.log("C'est le milieu de la semaine.");
    break;
  case "Friday":
    console.log("C'est presque le week-end.");
    break;
  default:
    console.log("C'est un jour ordinaire.");
}
```

Dans cet exemple, l'instruction `switch` vérifie la valeur de `dayOfWeek` et exécute le bloc de code correspondant. Si aucun des cas ne correspond, le bloc `default` est exécuté.

## Erreurs courantes avec les instructions `if`

Lors de l'utilisation des instructions `if`, les débutants commettent souvent quelques erreurs courantes. Abordons quelques-unes d'entre elles :

### Erreur 1 : Oublier l'opérateur d'égalité

```javascript
let x = 5;

// Incorrect
if (x = 10) {
  console.log("x est 10.");
}
```

Le code ci-dessus est incorrect car il utilise l'opérateur d'affectation `=` au lieu de l'opérateur d'égalité `===` à l'intérieur de la condition `if`. Le code correct devrait être `if (x === 10)`.

### Erreur 2 : Mal placer les accolades

```javascript
let y = 15;

// Incorrect
if (y > 10)
  console.log("y est supérieur à 10");
  console.log("Cette instruction n'est pas dans le bloc if");
```

Dans cet exemple, seule la première instruction `console.log` fait partie du bloc `if` car les accolades sont manquantes. Pour inclure les deux instructions dans le bloc `if`, utilisez des accolades :

```javascript
if (y > 10) {
  console.log("y est supérieur à 10");
  console.log("Cette instruction est dans le bloc if");
}
```

### Erreur 3 : Confondre `=` et `==`

```javascript
let z = "5";

// Incorrect
if (z = 5) {
  console.log("z est 5.");
}
```

Le code ci-dessus est incorrect car il utilise l'opérateur d'affectation `=` au lieu de l'opérateur d'égalité `==` à l'intérieur de la condition `if`. Le code correct devrait être `if (z == 5)`.

## Conclusion

Comprendre et maîtriser les instructions `if` est essentiel pour tout développeur JavaScript. Ces instructions conditionnelles fournissent la logique qui permet à vos programmes de prendre des décisions et de répondre dynamiquement à différentes situations.

Que vous validiez l'entrée de l'utilisateur, contrôliez le flux de votre application ou gériez différents cas, les instructions `if` sont un outil fondamental dans votre arsenal de programmation.

Alors que vous continuez votre voyage dans le développement JavaScript, pratiquez l'utilisation des instructions `if` dans divers scénarios. Expérimentez avec différentes conditions, structures imbriquées et opérateurs logiques pour devenir à l'aise et compétent dans l'utilisation de ces outils puissants.

Avec une compréhension solide des instructions `if`, vous serez bien équipé pour construire des applications web plus dynamiques et réactives.