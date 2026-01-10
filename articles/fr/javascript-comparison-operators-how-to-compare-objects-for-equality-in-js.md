---
title: Opérateurs de comparaison JavaScript – Comment comparer des objets pour l'égalité
  en JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-01-25T18:47:40.000Z'
originalURL: https://freecodecamp.org/news/javascript-comparison-operators-how-to-compare-objects-for-equality-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-christina-morillo-1181675.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Opérateurs de comparaison JavaScript – Comment comparer des objets pour
  l'égalité en JS
seo_desc: 'While coding in JavaScript, there may be times when you need to compare
  objects for equality. The thing is, comparing objects in JavaScript is not that
  straightforward.

  In this article, you learn three ways to compare objects for equality in JavaScri...'
---

Lors de la programmation en JavaScript, il peut arriver que vous ayez besoin de comparer des objets pour vérifier leur égalité. Le problème est que la comparaison d'objets en JavaScript n'est pas aussi simple.

Dans cet article, vous apprendrez trois façons de comparer des objets pour vérifier leur égalité en JavaScript.

Commençons !

## Quelle est la différence entre la comparaison des types de données primitifs et non primitifs en JavaScript ?

Les types de données en JavaScript se divisent en deux catégories :

- Primitifs (comme Number, String, Boolean, Undefined, Null, Symbol)
- Non primitifs (comme Object)

Les types de données primitifs font référence à une seule valeur, et la comparaison des valeurs primitives est relativement simple – vous n'avez besoin que d'utiliser l'un des opérateurs de comparaison.

Dans l'exemple suivant, j'utilise l'opérateur d'égalité stricte, `===`, qui vérifie si les deux opérandes sont égaux et retourne un booléen comme résultat :

```javascript
let a = 1;
let b = 1;

console.log(a === b); // true
```

Vous pouvez également assigner la valeur de la variable `a` à une autre variable, `a1`, et les comparer :

```javascript
let a = 1;
let b = 1;

let a1 = a;

console.log(a === a1); // true
```

Dans l'exemple ci-dessus, les deux variables pointent vers la même valeur, donc le résultat est `true`.

En ce qui concerne les objets, cependant, leur comparaison n'est pas aussi simple.

```javascript
let a = { name: 'Dionysia', age: 29};
let b = {name: 'Dionysia', age:29};

console.log(a === b); // false
```

Même si les deux objets ont les mêmes paires clé-valeur, le résultat de la comparaison est `false`. Pourquoi cela ?

Est-ce parce que j'ai utilisé l'opérateur d'égalité stricte, `===` ? Que se passe-t-il si j'utilise l'opérateur d'égalité non stricte, `==` ?

```javascript
let a = { name: 'Dionysia', age: 29};
let b = {name: 'Dionysia', age:29};

console.log(a == b); // false
```

J'obtiens le même résultat !

`a` et `b` semblent identiques, mais les objets ne sont pas égaux lorsque j'utilise `===` ou `==`.

On pourrait penser que deux objets avec les mêmes propriétés et valeurs seraient considérés comme égaux.

La raison de ce résultat est liée à la manière dont JavaScript aborde les tests d'égalité lorsqu'il s'agit de comparer des types de données primitifs et non primitifs.

La différence entre les types de données primitifs et non primitifs est que :

- les types de données primitifs sont comparés par *valeur*.
- les types de données non primitifs sont comparés par *référence*.

Dans les sections suivantes, vous verrez quelques façons de comparer des objets pour vérifier leur égalité.

## Comment comparer des objets par référence en JavaScript

Comme vous l'avez vu dans l'exemple de la section précédente, l'utilisation de `==` et `===` retourne `false` lorsque vous essayez de comparer des objets par valeur :

```javascript
let a = { name: 'Dionysia', age: 29};
let b = {name: 'Dionysia', age:29};

console.log(a === b); // false
```

Les deux objets ont des clés et des valeurs identiques, mais le résultat était `false` parce qu'ils sont des instances différentes.

Pour comparer des objets par référence, vous devez tester si les deux pointent vers le même emplacement en mémoire.

Lorsque vous faites référence à un objet, vous faites référence à une adresse en mémoire.

Voyons un exemple :

```javascript
let a = { name: 'Dionysia', age: 29};

let b = a;


console.log(a === b); // true
```

Dans l'exemple ci-dessus, grâce à la ligne `let b = a;`, les deux variables ont la même référence et pointent vers la même instance d'objet, donc le résultat est `true`.

Lorsque j'assigne la variable `a` à `b`, l'adresse de `a` est copiée dans `b`. Cela entraîne que les deux ont la même adresse – et non la même valeur.

Cela dit, la plupart du temps, vous voudrez comparer des objets par valeur et non par instance.

Et comme vous l'avez vu, vous ne pouvez pas simplement utiliser `==` ou `===` pour comparer des objets par valeur – cela nécessite un peu plus de travail.

## Comment comparer des objets en utilisant la fonction `JSON.stringify()` en JavaScript

Une façon de comparer deux objets par valeur est d'utiliser la fonction `JSON.stringify`.

La fonction `JSON.stringify()` convertit les objets en chaînes JSON équivalentes. Vous pouvez ensuite utiliser l'un des opérateurs de comparaison pour comparer les chaînes.

```javascript
let a = { name: 'Dionysia', age: 29};
let b = { name: 'Dionysia', age: 29};

console.log(JSON.stringify(a) === JSON.stringify(b)); // true
```

La fonction `JSON.stringify()` a converti les deux objets en chaînes JSON, et puisque `a` et `b` ont les mêmes propriétés et valeurs, le résultat est `true`.

Mais `JSON.stringify()` n'est pas toujours la meilleure solution pour comparer des objets par valeur, car elle a des limitations.

Tout d'abord, lors de l'utilisation de `JSON.stringify()`, l'ordre des clés est important.

Regardez ce qui se passe lorsque les clés sont dans un ordre différent :

```javascript
let a = { age: 29, name: 'Dionysia'};
let b = { name: 'Dionysia', age: 29};

console.log(JSON.stringify(a) === JSON.stringify(b)); //false
```

Dans cet exemple, vous vous attendriez à ce que le résultat soit `true` puisque les valeurs sont les mêmes – seul l'ordre des clés a été inversé.

`JSON.stringify()` convertit l'objet tel quel, donc l'ordre des clés est important. Si elles ne sont pas dans le même ordre, le résultat sera `false`.

Ainsi, `JSON.stringify()` n'est pas le meilleur choix pour comparer des objets puisque vous ne pouvez pas toujours être certain de l'ordre des clés.

Il y a aussi une limitation supplémentaire : JSON ne représente pas tous les types.

Regardez ce qui se passe lorsque la valeur d'une clé est undefined :

```javascript
let a = { name: 'Dionysia'};
let b = { name: 'Dionysia', age: undefined};

console.log(JSON.stringify(a) === JSON.stringify(b)); //true
```

Dans l'exemple ci-dessus, le résultat est inattendu. Le résultat aurait dû être `false` mais a été retourné comme `true` parce que JSON ignore les clés dont les valeurs sont undefined.

## Comment comparer des objets en utilisant la méthode `_.isEqual()` de Lodash en JavaScript

Une solution élégante et sophistiquée pour comparer des objets par leur valeur est d'utiliser la bibliothèque JavaScript bien testée [Lodash](https://lodash.com/) et sa méthode `_.isEqual()`.

Prenons l'exemple de la section précédente, où les clés ont la même valeur mais sont dans un ordre différent, et utilisons la méthode `_.isEqual()` :

```javascript
let a = { age: 29, name: 'Dionysia'};
let b = { name: 'Dionysia', age: 29};

console.log(_.isEqual(a, b)); // true
```

Dans la section précédente, le résultat lors de l'utilisation de `JSON.stringify` était `false`.

La bibliothèque Lodash offre une variété de cas particuliers et effectue une comparaison profonde entre deux valeurs pour vérifier si les deux objets sont profondément égaux.

## Conclusion

Dans cet article, vous avez appris comment comparer des objets pour vérifier leur égalité en JavaScript.

Vous avez vu trois méthodes différentes et les avantages et inconvénients de chacune. En cas de doute, la manière la plus efficace de comparer des objets est d'utiliser la bibliothèque Lodash.

Merci d'avoir lu, et bon codage !