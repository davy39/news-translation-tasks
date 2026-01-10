---
title: Que sont les fonctions d'ordre supérieur en JavaScript ? Explications avec
  des exemples
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-05-02T18:31:54.000Z'
originalURL: https://freecodecamp.org/news/higher-order-functions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Ivory-and-Blue-Lavender-Aesthetic-Photo-Collage-Presentation--7-.png
tags:
- name: functions
  slug: functions
- name: JavaScript
  slug: javascript
seo_title: Que sont les fonctions d'ordre supérieur en JavaScript ? Explications avec
  des exemples
seo_desc: JavaScript offers a powerful feature known as higher order functions (HOFs).
  These functions elevate your code by treating other functions as citizens of the
  language itself.  In simpler terms, HOFs can accept functions as arguments and even
  return f...
---

JavaScript offre une fonctionnalité puissante connue sous le nom de fonctions d'ordre supérieur (HOFs). Ces fonctions élèvent votre code en traitant d'autres fonctions comme des citoyens du langage lui-même. En termes plus simples, les HOFs peuvent accepter des fonctions comme arguments et même retourner des fonctions comme résultats. Cette capacité permet aux développeurs d'écrire un code propre, réutilisable et expressif.

Cet article traite de manière exhaustive des fonctions d'ordre supérieur en JavaScript. Nous commencerons par établir une compréhension claire des HOFs, de leurs concepts de base et des avantages qu'ils apportent à votre processus de développement. Nous explorerons ensuite certaines des HOFs les plus couramment utilisées en JavaScript, comme `map`, `filter` et `reduce`, en fournissant des explications détaillées, des analyses de syntaxe et des exemples pratiques pour consolider votre compréhension.

## Que sont les fonctions d'ordre supérieur ?

Les fonctions d'ordre supérieur (HOFs) en JavaScript sont des fonctions qui peuvent faire au moins l'une des choses suivantes :

* Accepter d'autres fonctions comme arguments.
* Retourner une fonction comme résultat.

## Concepts de base des fonctions d'ordre supérieur

### 1. Accepter des fonctions comme arguments

Les fonctions d'ordre supérieur peuvent accepter d'autres fonctions comme arguments. Cela permet un comportement dynamique, où le comportement de la fonction d'ordre supérieur peut être personnalisé en fonction de la fonction passée comme argument.

**Exemple :**

```javascript
// Fonction d'ordre supérieur qui accepte une fonction de rappel
function higherOrderFunction(callback) {
  // Effectuer certaines opérations
  console.log("Exécution de la fonction d'ordre supérieur...");
  
  // Appeler la fonction de rappel
  callback();
}

// Fonction de rappel à passer à la fonction d'ordre supérieur
function callbackFunction() {
  console.log("Exécution de la fonction de rappel...");
}

// Appeler la fonction d'ordre supérieur avec la fonction de rappel comme argument
higherOrderFunction(callbackFunction);

```

Dans cet exemple, `higherOrderFunction` est une fonction d'ordre supérieur qui accepte une autre fonction (`callback`) comme argument. Lorsque `higherOrderFunction` est appelée, elle exécute certaines opérations puis appelle la fonction `callback` qui lui est passée. Cela permet de personnaliser le comportement de `higherOrderFunction` en passant différentes fonctions de rappel.

### 2. Retourner des fonctions

Les fonctions d'ordre supérieur peuvent également retourner des fonctions. Cela permet la création de fonctions dynamiquement en fonction de certaines conditions ou paramètres.

**Exemple :**

```javascript
// Fonction d'ordre supérieur qui retourne une fonction
function createGreeter(greeting) {
  // Retourner une nouvelle fonction
  return function(name) {
    console.log(`${greeting}, ${name}!`);
  };
}

// Créer une fonction de salutation avec un message spécifique
const greetHello = createGreeter("Hello");
greetHello("John"); // Sortie : Hello, John!

// Créer une autre fonction de salutation avec un message différent
const greetGoodbye = createGreeter("Goodbye");
greetGoodbye("Alice"); // Sortie : Goodbye, Alice!

```

Dans cet exemple, `createGreeter` est une fonction d'ordre supérieur qui retourne une nouvelle fonction. La fonction retournée (`greetHello` et `greetGoodbye`) prend un paramètre `name` et affiche un message de salutation avec le message spécifié passé à `createGreeter`. Cela permet de créer différentes fonctions de salutation avec différents messages de manière dynamique.

### 3. Abstraction

Les fonctions d'ordre supérieur favorisent l'abstraction en encapsulant des motifs ou comportements communs dans des fonctions réutilisables. Cela conduit à un code plus propre et plus modulaire.

**Exemple :**

```javascript
// Fonction d'ordre supérieur pour effectuer une opération spécifiée sur chaque élément d'un tableau
function performOperationOnArray(array, operation) {
  return array.map(operation);
}

// Fonction de rappel pour doubler chaque élément d'un tableau
function double(number) {
  return number * 2;
}

const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = performOperationOnArray(numbers, double);
console.log(doubledNumbers); // Sortie : [2, 4, 6, 8, 10]

```

Dans cet exemple, `performOperationOnArray` est une fonction d'ordre supérieur qui accepte un tableau et une fonction `operation` comme arguments. Elle applique ensuite la fonction `operation` à chaque élément du tableau en utilisant la méthode `map` et retourne le résultat. Cela favorise la réutilisabilité du code et l'abstraction en permettant différentes opérations d'être effectuées sur des tableaux sans avoir à réécrire la logique pour itérer sur le tableau.

## Pourquoi utiliser les fonctions d'ordre supérieur ?

L'utilisation des HOFs en JavaScript offre plusieurs avantages qui peuvent améliorer la flexibilité, la réutilisabilité et la maintenabilité de votre base de code. Explorons ces bénéfices :

### Réutilisabilité du code

Les HOFs favorisent la réutilisabilité du code en permettant d'abstraire des motifs communs dans des fonctions réutilisables. Cela réduit la duplication de code et rend votre base de code plus maintenable.

```javascript
// Exemple : HOF pour filtrer des éléments basés sur une condition
function filterArray(array, condition) {
  return array.filter(condition);
}

const numbers = [1, 2, 3, 4, 5];

// Utilisation de filterArray pour filtrer les nombres pairs
const evenNumbers = filterArray(numbers, num => num % 2 === 0);
console.log(evenNumbers); // Sortie : [2, 4]

```

Au lieu d'écrire une logique de filtrage personnalisée à chaque fois, vous pouvez créer une fonction `filterArray` réutilisable qui accepte un tableau et une fonction de condition. Cela favorise la réutilisabilité du code car vous pouvez utiliser `filterArray` avec différentes conditions pour filtrer des tableaux basés sur divers critères.

### Modularité

Les HOFs aident à décomposer des tâches complexes en fonctions plus petites et plus gérables, favorisant une conception de code modulaire.

```javascript
// Exemple : HOF pour effectuer une série d'opérations sur un tableau
function processArray(array, operations) {
  return operations.reduce((acc, operation) => operation(acc), array);
}

const numbers = [1, 2, 3, 4, 5];

// Utilisation de processArray pour effectuer plusieurs opérations
const result = processArray(numbers, [
  arr => arr.map(num => num * 2),
  arr => arr.filter(num => num % 3 === 0)
]);
console.log(result); // Sortie : [6]

```

En encapsulant des opérations individuelles comme des fonctions et en les passant à une fonction d'ordre supérieur comme `processArray`, vous pouvez décomposer des tâches complexes en unités plus petites et plus gérables. Cela favorise une conception de code modulaire, rendant votre base de code plus facile à comprendre, maintenir et étendre.

### Flexibilité

Les HOFs permettent un comportement dynamique en acceptant des fonctions comme arguments ou en retournant des fonctions comme résultats. Cette flexibilité permet de personnaliser le comportement d'une fonction à l'exécution.

```javascript
// Exemple : HOF pour créer une fonction de multiplication
function createMultiplier(factor) {
  return function(number) {
    return number * factor;
  };
}

const double = createMultiplier(2);
console.log(double(5)); // Sortie : 10

```

En retournant une fonction de `createMultiplier`, vous pouvez générer dynamiquement une nouvelle fonction avec un facteur de multiplication spécifique. Cela offre de la flexibilité car vous pouvez créer plusieurs fonctions de multiplication avec différents facteurs sans avoir à redéfinir la logique à chaque fois.

## Fonctions d'ordre supérieur populaires en JavaScript

Explorons les fonctions d'ordre supérieur populaires en JavaScript ainsi que leurs descriptions, syntaxes et exemples d'utilisation pratiques :

### 1. Array.prototype.map()

La méthode `map()` crée un nouveau tableau en appelant une fonction fournie sur chaque élément du tableau appelant.

**Syntaxe :**

```javascript
const newArray = array.map(callback(currentValue, index, array));

```

**Utilisation :**

* Itérer sur des tableaux et transformer des éléments.

**Exemples :**

```javascript
// Exemple 1 : Doubler chaque nombre dans un tableau
const numbers = [1, 2, 3, 4, 5];
const doubledNumbers = numbers.map(num => num * 2);
console.log(doubledNumbers); // Sortie : [2, 4, 6, 8, 10]

// Exemple 2 : Convertir un tableau de chaînes en majuscules
const words = ["hello", "world", "javascript"];
const uppercaseWords = words.map(word => word.toUpperCase());
console.log(uppercaseWords); // Sortie : ["HELLO", "WORLD", "JAVASCRIPT"]

```

### 2. Array.prototype.filter()

La méthode `filter()` crée un nouveau tableau avec tous les éléments qui passent le test implémenté par la fonction fournie.

**Syntaxe :**

```javascript
const newArray = array.filter(callback(element, index, array));

```

**Utilisation :**

* Créer de nouveaux tableaux basés sur des conditions spécifiques.

**Exemples :**

```javascript
// Exemple 1 : Filtrer les nombres pairs d'un tableau
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // Sortie : [2, 4]

// Exemple 2 : Filtrer les mots de plus de 5 caractères
const words = ["apple", "banana", "grape", "kiwi", "orange"];
const longWords = words.filter(word => word.length > 5);
console.log(longWords); // Sortie : ["banana", "orange"]

```

### 3. Array.prototype.reduce()

La méthode `reduce()` applique une fonction contre un accumulateur et chaque élément du tableau pour le réduire à une seule valeur.

**Syntaxe :**

```javascript
const result = array.reduce(callback(accumulator, currentValue, index, array), initialValue);

```

**Utilisation :**

* Accumuler une seule valeur à partir d'un tableau.

**Exemples :**

```javascript
// Exemple 1 : Trouver la somme des nombres dans un tableau
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum); // Sortie : 15

// Exemple 2 : Trouver la moyenne des nombres dans un tableau
const numbers = [10, 20, 30, 40, 50];
const average = numbers.reduce((acc, num, index, array) => {
  acc += num;
  if (index === array.length - 1) {
    return acc / array.length;
  } else {
    return acc;
  }
}, 0);
console.log(average); // Sortie : 30

```

### 4. Array.prototype.forEach()

La méthode `forEach()` exécute une fonction fournie une fois pour chaque élément de tableau.

**Syntaxe :**

```javascript
array.forEach(callback(currentValue, index, array));

```

**Utilisation :**

* Itérer sur des tableaux et effectuer des effets de bord (par exemple, journalisation).

**Exemples :**

```javascript
// Exemple 1 : Journaliser chaque élément d'un tableau
const numbers = [1, 2, 3, 4, 5];
numbers.forEach(num => console.log(num));

// Exemple 2 : Mettre en majuscules et journaliser chaque mot d'un tableau
const words = ["hello", "world", "javascript"];
words.forEach(word => console.log(word.toUpperCase()));

```

### 5. Array.prototype.some()

La méthode `some()` teste si au moins un élément du tableau passe le test implémenté par la fonction fournie.

**Syntaxe :**

```javascript
const result = array.some(callback(element, index, array));

```

**Utilisation :**

* Vérifier si au moins un élément d'un tableau remplit une condition.

**Exemples :**

```javascript
// Exemple 1 : Vérifier si un nombre dans le tableau est supérieur à 10
const numbers = [5, 8, 12, 7, 3];
const isAnyNumberGreaterThan10 = numbers.some(num => num > 10);
console.log(isAnyNumberGreaterThan10); // Sortie : true

// Exemple 2 : Vérifier si un mot dans le tableau commence par "a"
const words = ["apple", "banana", "grape", "kiwi", "orange"];
const startsWithA = words.some(word => word.startsWith("a"));
console.log(startsWithA); // Sortie : true

```

### 6. Array.prototype.every()

La méthode `every()` teste si tous les éléments du tableau passent le test implémenté par la fonction fournie.

**Syntaxe :**

```javascript
const result = array.every(callback(element, index, array));

```

**Utilisation :**

* Vérifier si tous les éléments d'un tableau remplissent une condition.

**Exemples :**

```javascript
// Exemple 1 : Vérifier si tous les nombres dans le tableau sont positifs
const numbers = [5, 8, 12, 7, 3];
const areAllNumbersPositive = numbers.every(num => num > 0);
console.log(areAllNumbersPositive); // Sortie : true

// Exemple 2 : Vérifier si tous les mots dans le tableau ont une longueur supérieure à 3
const words = ["apple", "banana", "grape", "kiwi", "orange"];
const allWordsHaveLengthGreaterThan3 = words.every(word => word.length > 3);
console.log(allWordsHaveLengthGreaterThan3); // Sortie : true

```

Ces fonctions d'ordre supérieur populaires en JavaScript fournissent des outils puissants pour travailler avec des tableaux, permettant d'effectuer diverses opérations telles que le mappage, le filtrage, la réduction, l'itération et la vérification de conditions avec facilité et flexibilité.

## Techniques avancées avec les fonctions d'ordre supérieur

### 1. Composition de fonctions (Chaînage des HOFs)

La composition de fonctions implique le chaînage de plusieurs fonctions d'ordre supérieur pour créer des opérations ou transformations plus complexes.

**Exemple :**

```javascript
const numbers = [1, 2, 3, 4, 5];

// Chaînage de map() et filter() pour obtenir les carrés des nombres pairs
const result = numbers
  .filter(num => num % 2 === 0) // Filtrer les nombres pairs
  .map(num => num * num); // Élever au carré chaque nombre
console.log(result); // Sortie : [4, 16]

```

Dans cet exemple, nous avons chaîné les fonctions `filter()` et `map()`. Tout d'abord, `filter()` est utilisé pour filtrer les nombres pairs, puis `map()` élève au carré chacun des nombres filtrés. Cela crée un pipeline d'opérations, permettant d'effectuer des transformations complexes de manière concise et lisible.

### 2. Création de HOFs personnalisées

Vous pouvez créer des fonctions d'ordre supérieur personnalisées adaptées à vos besoins spécifiques, encapsulant des motifs ou comportements communs dans des fonctions réutilisables.

**Exemple :**

```javascript
// HOF personnalisée pour le filtrage basé sur plusieurs conditions
function customFilter(array, conditionFn) {
  return array.filter(conditionFn);
}

// Utilisation
const numbers = [1, 2, 3, 4, 5];
const evenGreaterThanTwo = customFilter(numbers, num => num % 2 === 0 && num > 2);
console.log(evenGreaterThanTwo); // Sortie : [4]

```

Dans cet exemple, `customFilter` est une fonction d'ordre supérieur personnalisée qui accepte un tableau et une fonction de condition. Elle filtre le tableau en fonction de la condition spécifiée dans `conditionFn`. Cela permet de créer une logique de filtrage personnalisée adaptée à des besoins spécifiques.

### 3. HOFs et paradigmes de programmation fonctionnelle

Les fonctions d'ordre supérieur sont fondamentales pour les paradigmes de programmation fonctionnelle, mettant l'accent sur l'utilisation de fonctions pures, l'immuabilité et le style de programmation déclaratif.

**Exemple :**

```javascript
// Paradigme de programmation fonctionnelle utilisant des HOFs
const numbers = [1, 2, 3, 4, 5];

// Utilisation de reduce() pour sommer les nombres
const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum); // Sortie : 15

// Utilisation de map() pour doubler les nombres
const doubled = numbers.map(num => num * 2);
console.log(doubled); // Sortie : [2, 4, 6, 8, 10]

```

Dans cet exemple, nous démontrons les paradigmes de programmation fonctionnelle en utilisant des fonctions d'ordre supérieur. La fonction `reduce()` est utilisée pour sommer les nombres, mettant l'accent sur l'immuabilité et l'accumulation, tandis que la fonction `map()` est utilisée pour doubler les nombres, promouvant un style déclaratif et fonctionnel pur.

## Avantages des HOFs dans l'écriture de code plus propre et plus déclaratif

Les fonctions d'ordre supérieur permettent d'écrire un code plus propre, plus déclaratif et plus expressif en promouvant la réutilisabilité du code, la modularité et les principes de programmation fonctionnelle.

**Exemple :**

```javascript
// Code déclaratif utilisant des HOFs
const numbers = [1, 2, 3, 4, 5];

// Utilisation de map() pour élever au carré chaque nombre
const squared = numbers.map(num => num * num);
console.log(squared); // Sortie : [1, 4, 9, 16, 25]

```

Dans cet exemple, la fonction `map()` est utilisée pour élever au carré chaque nombre dans le tableau. Cette approche est déclarative, exprimant clairement l'intention de l'opération sans détails impératifs de bas niveau, conduisant à un code plus propre et plus maintenable.

## Bonnes pratiques et considérations lors de l'utilisation de fonctions d'ordre supérieur

### 1. Choisir la bonne HOF pour la tâche

Sélectionner la fonction d'ordre supérieur appropriée en fonction de l'opération souhaitée est crucial pour écrire un code efficace et lisible. Prenez en compte des facteurs tels que la tâche spécifique à accomplir, la sortie attendue et toute exigence supplémentaire.

**Exemple :**

* Utilisez `map()` pour transformer des éléments dans un tableau.
* Utilisez `filter()` pour sélectionner des éléments basés sur une condition.
* Utilisez `reduce()` pour agréger des valeurs en un seul résultat.
* Utilisez `forEach()` pour effectuer des effets de bord sans retourner un nouveau tableau.

### 2. Éviter l'utilisation excessive de HOFs pour des raisons de lisibilité

Bien que les fonctions d'ordre supérieur puissent améliorer la lisibilité et la maintenabilité du code, leur utilisation excessive peut conduire à un code difficile à comprendre. Utilisez les HOFs de manière judicieuse, et privilégiez la lisibilité à l'abstraction excessive.

**Exemple :**

* Choisissez une simple boucle `for` plutôt que de chaîner plusieurs HOFs si cela améliore la clarté et la compréhension.

### 3. Comprendre les fonctions de rappel dans les HOFs

Les fonctions de rappel jouent un rôle vital au sein des fonctions d'ordre supérieur, car elles définissent le comportement ou la logique à exécuter par la HOF.

**Exemple :**

* Dans `map()`, la fonction de rappel définit la transformation appliquée à chaque élément.
* Dans `filter()`, la fonction de rappel spécifie la condition de sélection des éléments.
* Dans `reduce()`, la fonction de rappel détermine comment les valeurs sont agrégées dans le résultat final.

### 4. Écrire des fonctions de rappel efficaces et claires

Assurez-vous que les fonctions de rappel utilisées au sein des HOFs sont efficaces, claires et axées sur une seule responsabilité. Écrivez-les de manière à améliorer la lisibilité et à promouvoir la maintenabilité du code.

**Exemple :**

* Utilisez des noms de variables descriptifs au sein des fonctions de rappel pour améliorer la clarté du code.
* Décomposez les opérations complexes en fonctions plus petites et plus gérables si nécessaire.
* Envisagez d'utiliser des fonctions fléchées pour une syntaxe concise et lisible lors de la définition des fonctions de rappel.

### 5. Gestion des erreurs et cas limites avec les HOFs

Gérez les erreurs potentielles et les cas limites avec grâce lors de l'utilisation de fonctions d'ordre supérieur pour garantir la robustesse et la fiabilité de votre code.

**Exemple :**

* Validez les paramètres d'entrée avant d'appliquer des fonctions d'ordre supérieur pour prévenir les comportements inattendus.
* Implémentez des mécanismes de gestion des erreurs au sein des fonctions de rappel pour gérer les cas exceptionnels.
* Testez vos implémentations de HOF de manière approfondie pour couvrir les cas limites et garantir un comportement correct dans tous les scénarios.

### Conclusion

Tout au long de cet article, vous avez exploré les concepts de base des HOFs, discuté des fonctions populaires comme `map` et `reduce`, et découvert des techniques avancées comme la composition de fonctions et la création de HOFs personnalisées. Vous avez également acquis des informations précieuses sur les bonnes pratiques, vous assurant de tirer parti des HOFs de manière efficace et de traiter les pièges potentiels.

Alors que vous avancez, gardez ces outils puissants dans votre arsenal JavaScript. En maîtrisant les HOFs, vous écriverez un code plus propre, plus concis et plus expressif, propulsant vos compétences en développement à de nouveaux sommets. N'oubliez pas, le voyage ne s'arrête pas ici ! Explorez les concepts de programmation fonctionnelle qui s'intègrent parfaitement avec les HOFs. Il y a toujours plus à apprendre et à découvrir.

Connectez-vous avec moi sur [LinkedIn](https://ng.linkedin.com/in/joan-ayebola)