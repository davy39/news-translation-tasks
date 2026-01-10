---
title: Nouvelles méthodes de tableaux JavaScript pour vous aider à écrire un code
  meilleur et plus propre
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2024-10-01T21:23:07.517Z'
originalURL: https://freecodecamp.org/news/new-javascript-array-methods-to-help-you-write-better-cleaner-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727789649013/c0c332b4-fc35-4b75-bea9-240dcd85ec88.png
tags:
- name: JavaScript
  slug: javascript
- name: array
  slug: array
- name: array methods
  slug: array-methods
seo_title: Nouvelles méthodes de tableaux JavaScript pour vous aider à écrire un code
  meilleur et plus propre
seo_desc: JavaScript is always improving, and every year, new features are added to
  make coding easier and more efficient. These updates help developers write cleaner
  code and work faster. If you want to stay ahead as a developer, it's important to
  learn about...
---

JavaScript s'améliore constamment et, chaque année, de nouvelles fonctionnalités sont ajoutées pour rendre le codage plus facile et plus efficace. Ces mises à jour aident les développeurs à écrire un code plus propre et à travailler plus rapidement. Si vous voulez rester à la pointe en tant que développeur, il est important d'apprendre les dernières fonctionnalités de JavaScript.

Dans cet article, nous allons parler de certains des nouveaux outils et méthodes disponibles en JavaScript, comme `findLast`, `toReversed`, `toSorted`, et plus encore. Ces fonctionnalités vous permettent de manipuler les tableaux et les données de manière plus intelligente sans modifier vos données d'origine. Nous examinerons comment chacune fonctionne et je vous montrerai des exemples, en expliquant comment elles peuvent améliorer votre code.

### Table des matières

1. [Méthodes de tableaux en JavaScript](#heading-methodes-de-tableaux-en-javascript)
    
2. [`findLast` : Localiser le dernier élément correspondant](#heading-findlast-localiser-le-dernier-element-correspondant)
    
3. [`findLastIndex` : Identifier l'index de la dernière correspondance](#heading-findlastindex-identifier-lindex-de-la-derniere-correspondance)
    
4. [`toReversed` : Inverser sans modifier les tableaux originaux](#heading-toreversed-inverser-sans-modifier-les-tableaux-originaux)
    
5. [`toSorted` : Tri immuable pour un code plus propre](#heading-tosorted-tri-immuable-pour-un-code-plus-propre)
    
6. [`toSpliced` : Créer de nouveaux tableaux par épissage sans mutation](#heading-tospliced-creer-de-nouveaux-tableaux-par-epissage-sans-mutation)
    
7. [`with` : Modifier les éléments d'un tableau par index](#heading-with-modifier-les-elements-dun-tableau-par-index)
    
8. [Combiner les nouvelles méthodes JavaScript pour une manipulation de données avancée](#heading-combiner-les-nouvelles-methodes-javascript-pour-une-manipulation-de-donnees-avancee)
    
9. [Rétrocompatibilité et polyfills](#heading-retrocompatibilite-et-polyfills)
    
10. [Conclusion](#heading-conclusion)
    

## Méthodes de tableaux en JavaScript

JavaScript dispose d'une variété de méthodes qui facilitent le travail avec les tableaux. Les tableaux sont des listes d'éléments, et vous aurez souvent besoin de rechercher, trier ou mettre à jour ces listes. Les anciennes méthodes comme `push()`, `pop()`, `map()` et `filter()` ont été utiles, mais elles peuvent parfois modifier les données d'origine, ce qui n'est pas toujours ce que vous souhaitez.

Les nouvelles méthodes JavaScript offrent de meilleures options pour gérer les tableaux, surtout lorsque vous avez besoin de conserver les données d'origine inchangées. Ces nouvelles méthodes rendent le codage plus fiable et plus propre.

Les dernières méthodes JavaScript offrent plus de façons de travailler avec les tableaux sans modifier la liste d'origine. Ces méthodes, comme `findLast`, `toSorted` et `toReversed`, créent un nouveau tableau ou vous donnent le résultat directement, laissant votre tableau d'origine intact.

## `findLast` : Localiser le dernier élément correspondant

Lorsque vous travaillez avec des tableaux, vous pourriez vouloir rechercher un élément qui correspond à certaines conditions. L'ancienne méthode `find()` vous aide à obtenir le premier élément correspondant, mais que faire si vous avez besoin de la dernière correspondance à la place ?

C'est là que `findLast()` intervient. Elle parcourt le tableau en partant de la fin et vous donne le dernier élément qui remplit votre condition, sans avoir à inverser manuellement le tableau.

### Syntaxe et paramètres de `findLast`

La méthode `findLast()` fonctionne presque comme `find()`, mais elle cherche la dernière correspondance. Voici la syntaxe de base :

```javascript
array.findLast(callback(element, index, array), thisArg);
```

* **callback** : Une fonction qui vérifie chaque élément du tableau.
    
* **element** : L'élément actuel en cours de vérification.
    
* **index** : L'index de l'élément actuel.
    
* **array** : Le tableau en cours de traitement.
    
* **thisArg** : Optionnel. Il peut être utilisé comme `this` à l'intérieur du callback.
    

### Exemples pratiques d'utilisation de `findLast`

Regardons un exemple simple. Imaginez que vous avez un tableau de nombres et que vous voulez trouver le dernier nombre supérieur à 5.

```javascript
const numbers = [2, 7, 4, 9, 3];

// Trouver le dernier nombre supérieur à 5
const lastNumberOver5 = numbers.findLast(num => num > 5);
console.log(lastNumberOver5); // Sortie : 9
```

Dans cet exemple, `findLast()` commence la recherche par la fin du tableau et renvoie le dernier nombre qui est supérieur à 5.

### Trouver la dernière occurrence dans les tableaux

Vous pouvez utiliser `findLast()` pour obtenir le dernier élément correspondant, ce qui peut être utile lorsqu'il y a plusieurs correspondances dans un tableau. Disons que vous voulez trouver le dernier nombre pair dans un tableau :

```javascript
const numbers = [1, 4, 6, 8, 3, 6];

// Trouver le dernier nombre pair
const lastEvenNumber = numbers.findLast(num => num % 2 === 0);
console.log(lastEvenNumber); // Sortie : 6
```

### Comparaison avec `find()`

La différence clé entre `find()` et `findLast()` est la direction dans laquelle elles cherchent. `find()` commence par le début du tableau et s'arrête à la première correspondance, tandis que `findLast()` commence par la fin et renvoie la dernière correspondance.

Voici une comparaison :

```javascript
const numbers = [3, 5, 7, 9, 5];

// Utilisation de find()
const first5 = numbers.find(num => num === 5);
console.log(first5); // Sortie : 5 (première correspondance)

// Utilisation de findLast()
const last5 = numbers.findLast(num => num === 5);
console.log(last5); // Sortie : 5 (dernière correspondance)
```

La méthode `findLast()` est particulièrement utile dans les scénarios où l'ordre des éléments compte, tels que :

1. **Récupérer le dernier message dans une application de chat** qui répond à une certaine condition.
    
2. **Trouver la dernière erreur** dans une liste de journaux système.
    
3. **Obtenir la dernière transaction** au-dessus d'un certain montant dans une application financière.
    

## `findLastIndex` : Identifier l'index de la dernière correspondance

Parfois, vous n'avez pas seulement besoin du dernier élément correspondant dans un tableau, mais vous voulez aussi sa position. C'est là que `findLastIndex()` aide. Elle fonctionne comme `findLast()`, mais au lieu de renvoyer la valeur, elle renvoie l'index du dernier élément qui remplit votre condition. Cela facilite le suivi de l'emplacement de cet élément dans le tableau.

### Syntaxe et paramètres clés

La syntaxe de `findLastIndex()` est simple et ressemble beaucoup à celle de `findLast()` :

```javascript
array.findLastIndex(callback(element, index, array), thisArg);
```

* **callback** : Une fonction qui s'exécute pour chaque élément du tableau.
    
* **element** : L'élément actuel en cours de vérification.
    
* **index** : La position de l'élément actuel dans le tableau.
    
* **array** : Le tableau en cours de traitement.
    
* **thisArg** : Optionnel. Utilisé comme `this` à l'intérieur du callback.
    

Si aucun élément ne remplit la condition, `findLastIndex()` renvoie `-1`.

### Exemples pratiques de `findLastIndex` en action

Regardons un exemple. Supposons que vous avez un tableau de nombres et que vous voulez trouver l'index du dernier nombre supérieur à 5.

```javascript
const numbers = [2, 7, 4, 9, 3];

// Trouver l'index du dernier nombre supérieur à 5
const lastIndexOver5 = numbers.findLastIndex(num => num > 5);
console.log(lastIndexOver5); // Sortie : 3 (index de 9)
```

Dans ce cas, `findLastIndex()` renvoie `3`, qui est la position de `9`, le dernier nombre supérieur à 5 dans le tableau.

### Récupérer le dernier index correspondant à une condition

Si vous avez besoin de localiser précisément la position du dernier élément qui correspond à une condition spécifique, `findLastIndex()` est l'outil approprié. Voici un autre exemple, trouver le dernier nombre pair dans un tableau :

```javascript
const numbers = [1, 4, 6, 8, 3, 6];

// Trouver l'index du dernier nombre pair
const lastEvenIndex = numbers.findLastIndex(num => num % 2 === 0);
console.log(lastEvenIndex); // Sortie : 5 (index du dernier 6)
```

Dans ce cas, l'index du dernier nombre pair est `5`.

### Contraste avec `findIndex`

La principale différence entre `findIndex()` et `findLastIndex()` est la direction de leur recherche. `findIndex()` commence par le début du tableau et s'arrête à la première correspondance. `findLastIndex()` travaille à l'inverse, en commençant par la fin et en renvoyant la dernière correspondance.

Voici une comparaison rapide :

```javascript
const numbers = [3, 5, 7, 9, 5];

// Utilisation de findIndex()
const first5Index = numbers.findIndex(num => num === 5);
console.log(first5Index); // Sortie : 1 (première correspondance)

// Utilisation de findLastIndex()
const last5Index = numbers.findLastIndex(num => num === 5);
console.log(last5Index); // Sortie : 4 (dernière correspondance)
```

### Considérations de performance pour les grands ensembles de données

Dans les petits tableaux, la différence de performance entre `findIndex()` et `findLastIndex()` peut ne pas être perceptible. Mais avec de grands ensembles de données, la différence peut avoir de l'importance. Puisque `findLastIndex()` commence par la fin du tableau, elle peut être plus efficace si vous vous attendez à ce que la correspondance soit proche de la fin. Cela peut faire gagner du temps par rapport à un balayage depuis le début avec `findIndex()`.

Par exemple, lors de l'utilisation d'un grand journal d'événements, l'utilisation de `findLastIndex()` pourrait trouver rapidement l'événement le plus récent qui remplit une condition :

```javascript
const events = new Array(100000).fill(0).map((_, i) => i + 1);

// Trouver l'index du dernier nombre divisible par 5000
const lastDivisibleBy5000 = events.findLastIndex(num => num % 5000 === 0);
console.log(lastDivisibleBy5000); // Sortie : 99999 (index de 100000)
```

Dans de grands ensembles de données comme celui-ci, l'utilisation de `findLastIndex()` aide à éviter les recherches inutiles lorsque vous n'êtes intéressé que par l'occurrence la plus récente ou la dernière.

## `toReversed` : Inverser sans modifier les tableaux originaux

En JavaScript, la méthode `reverse()` est utilisée pour inverser l'ordre des éléments dans un tableau. Mais elle modifie le tableau d'origine. Cela peut causer des problèmes si vous voulez conserver les données d'origine intactes. La méthode `toReversed()` corrige ce problème en vous permettant d'inverser un tableau sans affecter l'original.

### Syntaxe et utilisation de `toReversed`

La méthode `toReversed()` est simple à utiliser. Elle crée une version inversée du tableau sans modifier celui d'origine. Voici la syntaxe de base :

```javascript
const newArray = array.toReversed();
```

* **array** : Le tableau que vous souhaitez inverser.
    
* **newArray** : Un nouveau tableau avec les éléments inversés.
    

### Exemples pour inverser des tableaux en toute sécurité

Regardons un exemple où vous voulez inverser un tableau tout en ayant besoin de conserver la version originale :

```javascript
const numbers = [1, 2, 3, 4, 5];

// Inverser le tableau sans modifier l'original
const reversedNumbers = numbers.toReversed();

console.log(reversedNumbers); // Sortie : [5, 4, 3, 2, 1]
console.log(numbers);         // Sortie : [1, 2, 3, 4, 5]
```

Dans ce cas, le tableau `numbers` d'origine reste le même, et `toReversed()` renvoie un nouveau tableau avec les éléments inversés.

### Éviter les effets de bord avec `toReversed`

L'un des plus grands avantages de `toReversed()` est qu'elle évite les effets de bord. La méthode traditionnelle `reverse()` modifie directement le tableau d'origine, ce qui peut entraîner des bogues si les données d'origine sont nécessaires ailleurs. Avec `toReversed()`, le tableau d'origine reste inchangé, vous n'avez donc pas à vous soucier de modifications inattendues.

```javascript
const letters = ['a', 'b', 'c', 'd'];

// Utilisation de toReversed pour éviter les effets de bord
const reversedLetters = letters.toReversed();

console.log(reversedLetters); // Sortie : ['d', 'c', 'b', 'a']
console.log(letters);         // Sortie : ['a', 'b', 'c', 'd']
```

Comme vous pouvez le voir, le tableau `letters` d'origine est toujours dans sa forme initiale après l'appel à `toReversed()`.

### Comparaison avec la méthode `reverse`

La méthode `reverse()` modifie directement le tableau, tandis que `toReversed()` laisse l'original inchangé. Voici une comparaison rapide :

```javascript
const nums = [10, 20, 30, 40];

// Utilisation de reverse()
const reversedNums1 = nums.reverse();
console.log(reversedNums1);  // Sortie : [40, 30, 20, 10]
console.log(nums);           // Sortie : [40, 30, 20, 10] (Tableau d'origine modifié)

// Utilisation de toReversed()
const reversedNums2 = nums.toReversed();
console.log(reversedNums2);  // Sortie : [10, 20, 30, 40]
console.log(nums);           // Sortie : [40, 30, 20, 10] (L'original reste tel qu'il était après reverse)
```

Comme illustré, `reverse()` modifie le tableau lui-même, mais `toReversed()` ne touche pas au tableau d'origine.

### Comment `toReversed` améliore les pratiques de programmation fonctionnelle

En programmation fonctionnelle, l'idée est d'éviter de modifier les données directement. Au lieu de cela, de nouvelles valeurs sont renvoyées par les fonctions, laissant les données d'origine intactes.

`toReversed()` s'inscrit parfaitement dans ce concept, permettant aux tableaux d'être inversés sans altérer les données d'origine. Cela conduit à un code plus propre et plus sûr car vous réduisez le risque de modifier accidentellement quelque chose.

Par exemple, dans une configuration de programmation fonctionnelle, vous pourriez vouloir inverser un tableau de scores à des fins d'affichage sans modifier les scores réels :

```javascript
const scores = [95, 87, 75, 60];

// Inverser les scores pour l'affichage sans modifier l'original
const displayedScores = scores.toReversed();

console.log(displayedScores); // Sortie : [60, 75, 87, 95]
console.log(scores);          // Sortie : [95, 87, 75, 60] (Scores d'origine intacts)
```

## `toSorted` : Tri immuable pour un code plus propre

JavaScript dispose de la méthode `sort()` depuis longtemps, ce qui permet d'organiser les éléments d'un tableau. Le problème est que `sort()` modifie le tableau d'origine, ce qui peut entraîner des problèmes involontaires lorsque les données d'origine sont encore nécessaires ailleurs.

Pour corriger cela, JavaScript a introduit `toSorted()`. Cette méthode vous permet de trier des tableaux sans modifier l'original, rendant le code plus propre et plus fiable.

### Syntaxe et paramètres

La syntaxe de `toSorted()` est simple, similaire à `sort()`, mais elle ne modifie pas le tableau d'origine :

```javascript
const newArray = array.toSorted(compareFunction);
```

* **array** : Le tableau que vous souhaitez trier.
    
* **compareFunction** : Optionnel. Une fonction qui définit comment les éléments doivent être triés. Si elle n'est pas fournie, les éléments du tableau sont convertis en chaînes de caractères et triés par ordre croissant.
    

### Cas d'utilisation de `toSorted`

Supposons que vous ayez une liste d'étudiants et que vous vouliez les trier en fonction de leurs scores, mais que vous ayez besoin de la liste d'origine intacte :

```javascript
const students = [
  { name: 'Dave', score: 85 },
  { name: 'Alexa', score: 92 },
  { name: 'Katie', score: 78 }
];

// Trier les étudiants sans modifier le tableau d'origine
const sortedStudents = students.toSorted((a, b) => b.score - a.score);

console.log(sortedStudents);
// Sortie : [{name: 'Alexa', score: 92}, {name: 'Dave', score: 85}, {name: 'Katie', score: 78}]

console.log(students);
// Sortie (inchangée) : [{name: 'Dave', score: 85}, {name: 'Alexa', score: 92}, {name: 'Katie', score: 78}]
```

Cela vous permet de trier les étudiants en fonction de leurs scores sans affecter les données d'origine, ce qui pourrait être utile ailleurs dans le code.

### Trier des tableaux sans muter les données d'origine

`toSorted()` offre un moyen sûr de gérer le tri sans risquer de modifier accidentellement le tableau d'origine. C'est particulièrement utile lors du travail sur de grands projets où les données pourraient être utilisées dans différentes parties du code.

Voici un exemple où vous triez une simple liste de nombres :

```javascript
const numbers = [5, 2, 9, 1, 7];

// Trier les nombres sans modifier le tableau d'origine
const sortedNumbers = numbers.toSorted();

console.log(sortedNumbers); // Sortie : [1, 2, 5, 7, 9]
console.log(numbers);       // Sortie (inchangée) : [5, 2, 9, 1, 7]
```

### Comparaison avec la méthode traditionnelle `sort`

La méthode traditionnelle `sort()` trie un tableau mais modifie l'original, ce qui peut causer des problèmes si le tableau d'origine est nécessaire ailleurs.

```javascript
const numbers = [3, 1, 4, 2];

// Utilisation de sort()
const sortedNumbers1 = numbers.sort();
console.log(sortedNumbers1); // Sortie : [1, 2, 3, 4]
console.log(numbers);        // Sortie (tableau d'origine modifié) : [1, 2, 3, 4]

// Utilisation de toSorted()
const sortedNumbers2 = numbers.toSorted();
console.log(sortedNumbers2); // Sortie : [1, 2, 3, 4]
console.log(numbers);        // Sortie (inchangée) : [3, 1, 4, 2]
```

Comme vous pouvez le voir, `sort()` modifie le tableau d'origine, mais `toSorted()` le garde intact.

### Performance et bonnes pratiques

Pour les petits tableaux, la performance entre `sort()` et `toSorted()` sera presque la même. Mais pour les ensembles de données plus importants ou lorsque le tri est fréquent, `toSorted()` peut aider à éviter les effets de bord et rendre le code plus sûr.

L'utilisation de `toSorted()` signifie que vous pouvez passer en toute sécurité le tableau d'origine à d'autres parties du code sans vous soucier de changements inattendus.

Pour obtenir les meilleures performances, assurez-vous de toujours utiliser une fonction de comparaison appropriée, en particulier pour les tris complexes, comme le tri d'objets :

```javascript
const people = [
  { name: 'Rash', age: 30 },
  { name: 'Josh', age: 25 },
  { name: 'Sammy', age: 40 }
];

// Trier les personnes par âge sans muter le tableau d'origine
const sortedPeople = people.toSorted((a, b) => a.age - b.age);

console.log(sortedPeople);
// Sortie : [{name: 'Josh', age: 25}, {name: 'Rash', age: 30}, {name: 'Sammy', age: 40}]
```

L'utilisation de `toSorted()` améliore la lisibilité de votre code et aide à éviter les effets de bord involontaires, surtout lors de la manipulation de données importantes.

## `toSpliced` : Créer de nouveaux tableaux par épissage sans mutation

La méthode `splice()` en JavaScript a été utile pour ajouter, supprimer ou remplacer des éléments au sein d'un tableau. Mais elle modifie le tableau d'origine, ce qui peut entraîner des résultats inattendus si vous voulez conserver les données initiales.

Pour résoudre ce problème, `toSpliced()` a été introduite. Elle fonctionne comme `splice()`, mais sans modifier le tableau d'origine, permettant une approche plus sûre et plus propre.

### Syntaxe et utilisation pratique

Voici comment fonctionne la méthode `toSpliced()`. Elle crée un nouveau tableau après l'épissage, laissant celui d'origine inchangé.

```javascript
const newArray = array.toSpliced(start, deleteCount, item1, item2, ...);
```

* **start** : L'index à partir duquel commencer à modifier le tableau.
    
* **deleteCount** : Le nombre d'éléments à supprimer du tableau (optionnel).
    
* **item1, item2, ...** : Les éléments à ajouter à l'index de départ (optionnel).
    

### Exemples : Épisser des tableaux de manière immuable

Explorons un exemple pratique où vous voulez supprimer et remplacer des éléments d'un tableau mais conserver l'original intact :

```javascript
const fruits = ['apple', 'banana', 'cherry', 'date'];

// Créer un nouveau tableau en supprimant 'banana' et en ajoutant 'blueberry' sans modifier l'original
const newFruits = fruits.toSpliced(1, 1, 'blueberry');

console.log(newFruits); // Sortie : ['apple', 'blueberry', 'cherry', 'date']
console.log(fruits);    // Sortie : ['apple', 'banana', 'cherry', 'date']
```

Ici, `toSpliced()` supprime `'banana'` et ajoute `'blueberry'` à la même position, mais le tableau `fruits` d'origine reste inchangé.

### Comparaison avec la méthode traditionnelle `splice`

La différence clé entre `splice()` et `toSpliced()` est que `splice()` modifie le tableau d'origine, tandis que `toSpliced()` le laisse intact et renvoie un nouveau tableau.

```javascript
const numbers = [1, 2, 3, 4];

// Utilisation de splice()
const splicedNumbers = numbers.splice(1, 2, 10, 20);
console.log(splicedNumbers); // Sortie : [2, 3] (Éléments supprimés)
console.log(numbers);        // Sortie : [1, 10, 20, 4] (Tableau d'origine modifié)

// Utilisation de toSpliced()
const newNumbers = numbers.toSpliced(1, 2, 5, 6);
console.log(newNumbers);     // Sortie : [1, 5, 6, 4]
console.log(numbers);        // Sortie : [1, 10, 20, 4] (Tableau d'origine inchangé)
```

`splice()` modifie le tableau d'origine, mais `toSpliced()` ne le fait pas, vous donnant plus de contrôle et évitant les modifications de données non souhaitées.

### Cas d'utilisation pour la programmation fonctionnelle

`toSpliced()` s'intègre bien à la programmation fonctionnelle, qui privilégie l'évitement des modifications des données existantes. Par exemple, dans les applications où vous manipulez souvent des tableaux (comme des listes d'utilisateurs ou de produits), `toSpliced()` aide à conserver les données d'origine intactes.

```javascript
const users = ['Dave', 'Alexa', 'Katie'];

// Supprimer 'Alexa' et ajouter 'Dan' sans modifier le tableau d'origine
const updatedUsers = users.toSpliced(1, 1, 'Dan');

console.log(updatedUsers); // Sortie : ['Dave', 'Dan', 'Katie']
console.log(users);        // Sortie : ['Dave', 'Alexa', 'Katie']
```

Cette méthode facilite la gestion et le travail avec les tableaux dans les situations où les données d'origine doivent être préservées.

### Éviter les pièges avec `toSpliced`

Le principal avantage de `toSpliced()` est qu'elle évite les modifications involontaires du tableau d'origine. Elle réduit les risques de bogues causés par des données accidentellement modifiées.

Cependant, il est important de noter que la création d'un nouveau tableau avec `toSpliced()` signifie que l'ancien tableau n'est pas directement mis à jour. Vous devrez donc assigner le résultat à une nouvelle variable si vous souhaitez utiliser les données modifiées.

```javascript
const colors = ['red', 'green', 'blue'];

// Créer un nouveau tableau qui ajoute 'yellow' à l'index 1
const newColors = colors.toSpliced(1, 0, 'yellow');

console.log(newColors); // Sortie : ['red', 'yellow', 'green', 'blue']
console.log(colors);    // Sortie : ['red', 'green', 'blue'] (Original inchangé)
```

## `with` : Modifier les éléments d'un tableau par index

La méthode `with` est un nouvel outil puissant introduit en JavaScript pour aider à remplacer des éléments dans un tableau sans modifier le tableau d'origine.

Ceci est utile lorsque vous devez mettre à jour des éléments spécifiques sans affecter le reste des données, en gardant votre tableau d'origine intact. Elle favorise un code plus sûr et plus propre, en particulier lors de la manipulation de grands ensembles de données ou dans des styles de programmation fonctionnelle.

### Syntaxe et paramètres clés

La méthode `with` vous permet de créer un nouveau tableau où un élément à un index spécifique est remplacé.

```javascript
const newArray = array.with(index, newValue);
```

* **index** : La position de l'élément que vous souhaitez remplacer.
    
* **newValue** : La valeur à insérer à l'index donné.
    

### Exemples d'utilisation de `with` pour le remplacement d'éléments

Explorons un exemple simple où vous voulez remplacer un élément à une position spécifique :

```javascript
const fruits = ['apple', 'banana', 'cherry'];

// Remplacer 'banana' par 'blueberry' à l'index 1
const newFruits = fruits.with(1, 'blueberry');

console.log(newFruits); // Sortie : ['apple', 'blueberry', 'cherry']
console.log(fruits);    // Sortie : ['apple', 'banana', 'cherry']
```

Dans cet exemple, nous avons remplacé `'banana'` par `'blueberry'`, mais le tableau `fruits` d'origine reste le même, ce qui est très utile pour éviter les effets de bord dans votre code.

### Remplacer des éléments dans les tableaux tout en maintenant l'immuabilité

L'une des forces majeures de la méthode `with` est qu'elle ne modifie pas le tableau d'origine. Cela aide à maintenir l'immuabilité, qui est souvent nécessaire lors de la manipulation de données dans des applications de plus grande envergure. Vous pouvez remplacer des éléments en toute confiance sans vous soucier de modifications accidentelles des données d'origine.

```javascript
const numbers = [10, 20, 30, 40];

// Remplacer le nombre à l'index 2 (30) par 35
const updatedNumbers = numbers.with(2, 35);

console.log(updatedNumbers); // Sortie : [10, 20, 35, 40]
console.log(numbers);        // Sortie : [10, 20, 30, 40] (Original inchangé)
```

Cela fait de la méthode `with` un choix idéal lorsque vous devez mettre à jour des données mais que vous souhaitez toujours référencer le tableau d'origine ailleurs dans votre code.

### Applications de la méthode `with`

La méthode `with` peut être appliquée dans de nombreux scénarios, tels que la mise à jour des profils d'utilisateurs, la modification d'une liste d'articles ou le travail avec toute donnée nécessitant des mises à jour sélectives. Par exemple, lorsqu'il s'agit d'un tableau d'utilisateurs, vous pouvez remplacer les données d'un utilisateur spécifique sans affecter l'ensemble de l'ensemble de données.

```javascript
const users = ['Dave', 'Alexa', 'Katie'];

// Mettre à jour le nom à l'index 1 par 'Dan'
const updatedUsers = users.with(1, 'Dan');

console.log(updatedUsers); // Sortie : ['Dave', 'Dan', 'Katie']
console.log(users);        // Sortie : ['Dave', 'Alexa', 'Katie'] (Original inchangé)
```

Cette méthode aide à éviter la confusion qui peut découler de changements inattendus de données lors de la mise à jour d'éléments spécifiques dans un tableau.

### `with` vs méthodes traditionnelles pour le remplacement d'éléments

Avant l'introduction de `with`, le remplacement d'éléments dans les tableaux nécessitait des méthodes comme `splice()` ou des approches manuelles, les deux modifiant le tableau d'origine :

```javascript
const colors = ['red', 'green', 'blue'];

// Méthode traditionnelle (utilisant la mutation)
colors.splice(1, 1, 'yellow');
console.log(colors); // Sortie : ['red', 'yellow', 'blue'] (Tableau d'origine modifié)
```

Avec la nouvelle méthode `with`, vous pouvez éviter ce problème :

```javascript
const colors = ['red', 'green', 'blue'];

// Utilisation de la méthode `with`
const newColors = colors.with(1, 'yellow');
console.log(newColors); // Sortie : ['red', 'yellow', 'blue']
console.log(colors);    // Sortie : ['red', 'green', 'blue'] (Original inchangé)
```

The method `with` garantit que les données d'origine restent intactes, ce qui en fait une meilleure option pour les situations où l'immuabilité est importante.

## Combiner les nouvelles méthodes JavaScript pour une manipulation de données avancée

Les nouvelles méthodes JavaScript comme `findLast`, `toSorted` et `with` fournissent des outils puissants pour gérer et transformer les données. Utilisées ensemble, elles vous permettent de créer des opérations de données complexes de manière simple et lisible.

Voyons comment vous pouvez combiner ces méthodes pour gérer les données efficacement et écrire un code propre et efficace.

### Comment chaîner des méthodes comme `findLast`, `toSorted` et `with`

Le chaînage de méthodes en JavaScript vous permet d'appliquer plusieurs transformations à vos données dans un seul flux.

Par exemple, vous pourriez vouloir trier un tableau, trouver le dernier élément correspondant, puis le remplacer par une nouvelle valeur. Voici comment vous pouvez faire cela en utilisant `toSorted`, `findLastIndex` et `with` :

```javascript
const numbers = [20, 5, 15, 30, 10];

// Chaîner les méthodes pour trier, trouver le dernier élément supérieur à 10 et le remplacer
const result = numbers
  .toSorted((a, b) => a - b)   // Trier le tableau par ordre croissant
  .with(numbers.findLastIndex(num => num > 10), 100);  // Trouver et remplacer la dernière correspondance

console.log(result); // Sortie : [5, 10, 15, 20, 100]
```

Dans cet exemple :

* `toSorted()` organise le tableau par ordre croissant sans modifier le tableau d'origine.
    
* `findLastIndex()` trouve le dernier nombre supérieur à 10.
    
* `with()` remplace ce nombre (qui est 30) par 100, sans modifier le tableau d'origine.
    

Cette combinaison est utile lorsque vous travaillez avec des workflows de données complexes et garantit que les données d'origine restent inchangées.

### Créer des transformations de données complexes avec aisance

La véritable puissance de ces méthodes brille lorsque vous souhaitez effectuer plusieurs actions sur des tableaux de manière lisible et organisée. Voici un autre exemple où nous combinons le tri, la recherche et le remplacement de données, le tout dans un seul flux :

```javascript
const students = [
  { name: 'Dave', score: 85 },
  { name: 'Alexa', score: 75 },
  { name: 'Katie', score: 90 }
];

// Chaîner les méthodes pour trier, trouver le dernier étudiant avec un score supérieur à 80 et mettre à jour son score
const updatedStudents = students
  .toSorted((a, b) => b.score - a.score)   // Trier les étudiants par score (décroissant)
  .with(
    students.findLastIndex(student => student.score > 80), 
    { ...students.findLast(student => student.score > 80), score: 95 }
  );

console.log(updatedStudents);
```

Dans ce cas :

* `toSorted()` trie les étudiants en fonction de leurs scores du plus élevé au plus bas.
    
* `findLastIndex()` identifie le dernier étudiant ayant obtenu un score supérieur à 80.
    
* `with()` crée un nouveau tableau avec le score de cet étudiant mis à jour à 95.
    

La flexibilité de la combinaison de ces méthodes signifie que vous pouvez gérer facilement des structures de données même complexes sans compromettre la lisibilité ou modifier les données d'origine.

### Bonnes pratiques pour écrire un code propre et efficace avec ces méthodes

Pour écrire un code propre et efficace, tenez compte des conseils suivants lors de l'utilisation de ces nouvelles méthodes JavaScript :

1. **Éviter de muter les données d'origine** : Utilisez des méthodes comme `toSorted`, `toReversed` et `with` qui ne modifient pas le tableau d'origine. Cela garantit que vos données restent cohérentes tout au long de votre code.
    
2. **Utiliser le chaînage pour la lisibilité** : Chaînez les méthodes lorsque vous effectuez plusieurs transformations. Cela garde votre code concis et plus facile à suivre.
    
3. **Utiliser des fonctions fléchées** : Les fonctions fléchées courtes aident à réduire la complexité de votre code. Par exemple :
    
    ```javascript
    const sortedNumbers = numbers.toSorted((a, b) => a - b);
    ```
    
4. **Combiner les méthodes de manière réfléchie** : Assurez-vous que les méthodes que vous chaînez se succèdent logiquement. Par exemple, il est logique de trier les données d'abord avant de trouver le dernier élément correspondant à une condition.
    
5. **Manipuler les grands ensembles de données avec précaution** : Pour les tableaux très volumineux, tenez compte des implications en matière de performance. Des méthodes comme `findLast` et `toSorted` peuvent prendre du temps sur des ensembles de données plus importants, alors testez toujours les performances de votre code avec des tailles de données réalistes.
    

## Rétrocompatibilité et polyfills

À mesure que de nouvelles fonctionnalités JavaScript sont ajoutées, tous les navigateurs ne les prendront pas en charge immédiatement. Il est important de s'assurer que votre code fonctionne toujours sur les anciens navigateurs sans planter. Voyons comment vous pouvez gérer cela et introduisons les polyfills pour combler les lacunes lors de l'utilisation des dernières fonctionnalités.

### Comment assurer la rétrocompatibilité avec les anciens navigateurs

Pour vous assurer que votre code fonctionne correctement sur les anciens navigateurs qui ne prennent pas en charge les nouvelles méthodes JavaScript comme `findLast`, `toSorted` ou `with`, vous pouvez ajouter des vérifications pour voir si une fonctionnalité est disponible avant de l'utiliser. De cette façon, le code ne plante pas sur les navigateurs non pris en charge.

Voici un exemple :

```javascript
if (Array.prototype.findLast) {
  // Utiliser la méthode findLast
  const arr = [1, 2, 3, 4, 5];
  const lastOdd = arr.findLast(num => num % 2 !== 0);
  console.log(lastOdd); // Sortie : 5
} else {
  // Code de repli pour les anciens navigateurs
  console.log('findLast n\'est pas supporté');
}
```

Cet exemple vérifie si `findLast` existe. Si ce n'est pas le cas, vous pouvez exécuter un code de repli ou afficher un message. Cette approche aide à maintenir la rétrocompatibilité.

### Aperçu des polyfills pour les nouvelles fonctionnalités JavaScript

Un **polyfill** est un morceau de code qui ajoute la prise en charge de nouvelles fonctionnalités JavaScript sur les navigateurs qui ne les possèdent pas encore. Il fournit essentiellement une implémentation alternative de la fonctionnalité.

Par exemple, créons un polyfill pour `findLast` :

```javascript
if (!Array.prototype.findLast) {
  Array.prototype.findLast = function(callback) {
    for (let i = this.length - 1; i >= 0; i--) {
      if (callback(this[i], i, this)) {
        return this[i];
      }
    }
    return undefined;
  };
}
```

Ce polyfill ajoute la méthode `findLast` aux tableaux qui ne la prennent pas en charge. Désormais, même les anciens navigateurs peuvent exécuter le code qui utilise cette fonctionnalité.

Les polyfills pour les méthodes courantes sont disponibles sur des sites comme **MDN** ou via des bibliothèques comme **core-js** qui couvrent de nombreuses fonctionnalités JavaScript modernes.

### Outils et ressources pour tester le support des navigateurs

Avant d'utiliser de nouvelles fonctionnalités, il est utile de vérifier leur degré de prise en charge par les différents navigateurs. Voici quelques outils qui peuvent vous aider :

1. **Can I Use** : Un site Web populaire qui affiche la compatibilité des navigateurs pour les nouvelles fonctionnalités JavaScript. Vous pouvez rechercher des méthodes comme `toSorted` ou `findLast` pour voir quels navigateurs les prennent en charge.
    
    Exemple : [Can I Use: findLast](https://caniuse.com/?search=findLast)
    
2. **Babel** : Un compilateur JavaScript qui convertit le nouveau code JavaScript en versions plus anciennes qui fonctionnent sur les anciens navigateurs. Babel peut ajouter automatiquement des polyfills pour les fonctionnalités non prises en charge.
    
    Exemple d'utilisation avec Babel :
    
    ```bash
    npm install --save-dev @babel/preset-env
    ```
    
    Ensuite, configurez Babel pour utiliser le preset :
    
    ```json
    {
      "presets": ["@babel/preset-env"]
    }
    ```
    
3. [**Polyfill.io**](http://Polyfill.io) : Un service qui sert automatiquement les polyfills nécessaires en fonction du navigateur de l'utilisateur.
    
    Pour l'utiliser, ajoutez simplement ce script à votre HTML :
    
    ```html
    <script src="https://polyfill.io/v3/polyfill.min.js"></script>
    ```
    

Ce script ajoute automatiquement uniquement les polyfills nécessaires pour le navigateur chargeant la page, ce qui en fait un moyen facile de gérer la rétrocompatibilité.

## Conclusion

Nous avons exploré certaines des dernières fonctionnalités de JavaScript, notamment des méthodes comme `findLast`, `findLastIndex`, `toReversed`, `toSorted`, `toSpliced` et `with`.

Ces nouveaux ajouts apportent plus de flexibilité et d'efficacité au travail avec les tableaux. Ils aident à éviter les modifications involontaires des données d'origine et rendent le code plus propre et plus facile à suivre. Par exemple, `toSorted` permet le tri sans altérer le tableau d'origine, et `findLast` simplifie la localisation du dernier élément correspondant dans une liste.

Chacune de ces méthodes fait gagner du temps et réduit la complexité lors de la gestion et de la transformation des données.

Puisque JavaScript continue d'évoluer, il est important de commencer à utiliser ces méthodes dans vos futurs projets. Elles peuvent simplifier les tâches complexes de manipulation de données et rendre votre code plus facile à maintenir. Essayez d'ajouter ces méthodes à votre base de code actuelle et explorez comment elles peuvent améliorer la façon dont vous écrivez et gérez JavaScript.

La prochaine fois que vous travaillerez avec des tableaux, envisagez d'utiliser `toSorted` pour le tri, `findLast` pour la recherche ou `with` pour remplacer des éléments sans modifier les données d'origine. Ces petits ajustements peuvent avoir un impact important sur la qualité de votre code.

Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter sur [LinkedIn](https://ng.linkedin.com/in/joan-ayebola). Si vous avez apprécié ce contenu, envisagez de [m'offrir un café](https://www.buymeacoffee.com/joanayebola) pour soutenir la création de plus de contenus adaptés aux développeurs.