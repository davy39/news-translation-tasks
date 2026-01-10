---
title: Comment fonctionnent les fonctions en JavaScript – Exemples de code de fonction
  JS
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-01-20T17:52:37.000Z'
originalURL: https://freecodecamp.org/news/understanding-functions-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/kevin-ku-w7ZyuGYNpRQ-unsplash-1.jpg
tags:
- name: functions
  slug: functions
- name: JavaScript
  slug: javascript
seo_title: Comment fonctionnent les fonctions en JavaScript – Exemples de code de
  fonction JS
seo_desc: 'JavaScript is a widely-used programming language that is essential for
  web development. Its ability to run on both client-side and server-side makes it
  a versatile tool that has become an essential tool for web developers.

  JavaScript is a high-level,...'
---

JavaScript est un langage de programmation largement utilisé qui est essentiel pour le développement web. Sa capacité à s'exécuter à la fois côté client et côté serveur en fait un outil polyvalent qui est devenu un outil essentiel pour les développeurs web.

JavaScript est un langage de haut niveau, interprété, utilisé côté client, ce qui signifie qu'il s'exécute dans le navigateur web de l'utilisateur. Vous pouvez l'utiliser pour créer des applications web et mobiles, des extensions de navigateur et d'autres logiciels.

Il est supporté par tous les principaux navigateurs web, et c'est une technologie essentielle pour le développement web front-end.

Les **fonctions** sont l'un des éléments de base de la programmation JavaScript pour la création d'applications web.

Vous pouvez considérer les fonctions comme un moyen de regrouper un ensemble d'instructions et de les exécuter en tant qu'unité unique.

Dans cet article, nous allons explorer les bases des fonctions en JavaScript et comment vous pouvez les utiliser efficacement dans votre code.

## Syntaxe des fonctions

Une fonction est un bloc de code qui effectue une tâche spécifique. Les fonctions JavaScript sont principalement utilisées pour encapsuler la logique, rendant ce code plus réutilisable et plus facile à comprendre.

La syntaxe pour créer une fonction en JavaScript est assez simple. Les fonctions peuvent prendre des entrées sous forme de paramètres et peuvent retourner une valeur ou une sortie.

Les fonctions vous aident à organiser et structurer votre code. Elles permettent également la réutilisation du code et facilitent la compréhension et la maintenance de grandes bases de code.

### Comment écrire une fonction en JavaScript

Vous commencez par utiliser le mot-clé "**function**", suivi du nom de la fonction et d'une paire de parenthèses.

À l'intérieur des parenthèses, vous pouvez spécifier les paramètres d'entrée que la fonction prendra, également connus sous le nom d'arguments. Les arguments sont généralement optionnels.

Ensuite, vous incluez un bloc de code à l'intérieur des accolades qui définit les instructions que la fonction exécutera lorsqu'elle sera appelée.

Voici un exemple de fonction de base qui prend deux nombres et retourne leur somme :

```.js
//index.js

function addNumbers(a, b) {
  return a + b;
}

```

La fonction ci-dessus, nommée "**addNumbers**", prend deux paramètres, **a** et **b**. Le code à l'intérieur du corps de la fonction additionne simplement ces deux paramètres et retourne le résultat.

## Comment déclarer une fonction en JavaScript

En plus de la manière régulière de déclarer une fonction comme vu ci-dessus, vous pouvez également définir des fonctions en utilisant des **expressions de fonction** ou des **fonctions fléchées**.

La syntaxe des fonctions fléchées est une version abrégée de la syntaxe des fonctions régulières. Voici la même fonction que ci-dessus, mais écrite avec une fonction fléchée :

```js
//index.js
const addNumbers = (a, b) => a + b;
```

Dans l'exemple ci-dessus, la fonction est assignée à la variable **addNumbers**. La flèche **=>** est utilisée pour définir la fonction, et le code à l'intérieur des accolades est le corps de la fonction.

Les expressions de fonction en JavaScript sont similaires aux déclarations de fonction régulières. La différence entre elles est que l'expression de fonction est toujours assignée à une variable. Voici un exemple d'expression de fonction :

```js
//index.js
let multiplyNumbers = function(a, b) {
    return a * b;
}

```

Dans cet exemple, la fonction est assignée à la variable **multiplyNumbers**. Cette variable peut être utilisée pour appeler la fonction, comme une fonction régulière.

## Comment utiliser les fonctions de rappel

Les fonctions peuvent également être passées en tant qu'arguments à d'autres fonctions, connues sous le nom de **fonctions de rappel**. Voici un exemple d'une fonction de rappel utilisée pour journaliser le résultat d'une opération de multiplication :

```js
//index.js

function multiplyByTwo(n, callback) {
  var result = n * 2;
  callback(result);
}

function logResult(result) {
  console.log(result);
}

multiplyByTwo(5, logResult); // journalise 10
```

Dans cet exemple, la fonction **multiplyByTwo** prend deux arguments : un nombre et une fonction de rappel. La fonction multiplie le nombre par 2 puis invoque la fonction de rappel, passant le résultat en tant qu'argument. La fonction **logResult** est ensuite exécutée, ce qui journalise le résultat dans la console.

## Comment utiliser les paramètres par défaut

Les fonctions JavaScript ont également une fonctionnalité appelée paramètres par défaut. Ils vous permettent de définir des valeurs par défaut pour les paramètres au cas où ils ne seraient pas passés lorsque la fonction est appelée.

Cela est utile dans les situations où vous souhaitez fournir une valeur par défaut pour un paramètre au cas où il ne serait pas passé. Voici un exemple :

```js
//index.js

function greet(name = "John Doe") {
    console.log(`Hello, ${name}!`);
}

greet(); // Hello, John Doe!
greet("Jane Smith"); // Hello, Jane Smith
```

Dans cet exemple, la fonction `greet` prend un seul paramètre `name`, qui est défini par défaut sur "John Doe". Si la fonction est appelée sans passer d'arguments, elle utilisera la valeur par défaut "John Doe". Mais si un argument est passé, elle utilisera cette valeur à la place.

## Comment utiliser la fonction constructeur

JavaScript a un type spécial de fonction appelé fonction constructeur, qui est utilisé pour créer des objets.

Vous définissez une fonction constructeur en utilisant le mot-clé "function" suivi d'un nom qui commence par une lettre majuscule (appelé en utilisant le mot-clé "new").

Par exemple, le code suivant définit une fonction constructeur nommée "Person" qui crée un objet avec une propriété name et age :

```js
//index.js

function Person(name, age) {
  this.name = name;
  this.age = age;
}

let person = new Person("John Smith", 30);
console.log(person.name); // Sortie : "John Smith"
console.log(person.age); 
```

## Comment utiliser les fermetures

Une **fermeture** est une fonction qui a accès à des variables dans son scope parent, même après que la fonction parent a retourné. Cela permet de préserver les variables entre les appels de fonction, et c'est une fonctionnalité puissante qui permet des motifs de programmation plus avancés tels que la programmation orientée objet.

Voici un exemple de fonction de fermeture qui crée un compteur :

```js
//index.js

function createCounter() {
  let count = 0;
  return function() {
    return count++;
  }
}
const myCounter = createCounter();
console.log(myCounter()); // Sortie : 0
console.log(myCounter()); // Sortie : 1
```

## Comment utiliser les fonctions d'ordre supérieur

Les fonctions peuvent également être passées en tant qu'arguments à d'autres fonctions, ce qui est connu sous le nom de fonction "d'ordre supérieur". Par exemple :

```js
//index.js

function performOperation(a, b, operation) {
    return operation(a, b);
}

let result = performOperation(5, 10, addNumbers);
console.log(result);  // 15
```

Dans cet exemple, la fonction **performOperation** prend trois arguments : **a**, **b** et **operation**.

L'argument **operation** est une fonction qui prend deux arguments et retourne un résultat. Dans ce cas, nous passons la fonction **addNumbers** en tant qu'argument operation, donc le résultat de la fonction **performOperation** sera le résultat de l'appel de la fonction **addNumbers** avec les arguments **a** et **b**.

## Conclusion

Dans cet article, nous avons couvert les bases des fonctions en JavaScript, y compris comment les définir, les appeler et les utiliser dans nos codes.

Avec une compréhension solide des fonctions, vous pouvez écrire un code plus efficace et plus maintenable en JavaScript.

Vous pouvez consulter la [documentation MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions) pour en savoir plus sur les fonctions en JavaScript. Si vous souhaitez commencer à apprendre les fondamentaux de JavaScript, freeCodeCamp propose un cours gratuit [Certification JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) pour vous.

Bon codage !