---
title: Comment insérer dans un tableau JavaScript à un index spécifique – JS Push
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-04-25T18:14:43.000Z'
originalURL: https://freecodecamp.org/news/insert-into-javascript-array-at-specific-index
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-template--11-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment insérer dans un tableau JavaScript à un index spécifique – JS Push
seo_desc: 'JavaScript arrays are an important part of the language. They allow you
  to store and manipulate collections of data.

  Sometimes, you may need to insert a new element into an array at a specific index.
  To accomplish this task, you can use the push() me...'
---

Les tableaux JavaScript sont une partie importante du langage. Ils permettent de stocker et de manipuler des collections de données.

Parfois, vous pouvez avoir besoin d'insérer un nouvel élément dans un tableau à un index spécifique. Pour accomplir cette tâche, vous pouvez utiliser la méthode `push()` ou la méthode `splice()`.

Dans cet article, vous apprendrez à utiliser ces deux techniques en détail.

## Comment fonctionnent les tableaux JavaScript

Avant de plonger dans les méthodes d'insertion, examinons brièvement les tableaux en JavaScript.

Un tableau est une collection de valeurs de données de n'importe quel type. Vous pouvez créer des tableaux en utilisant soit le constructeur de tableau, soit la notation littérale.

Voici un exemple de tableau créé en utilisant le constructeur de tableau :

```js
const arrayConstructor = new Array(1, 2, 3);
console.log(arrayConstructor); // Sortie : [1, 2, 3]
```

Et voici un exemple de tableau créé en utilisant la notation littérale :

```js
const literalArray = [1, 2, 3];
console.log(literalArray); // Sortie : [1, 2, 3]
```

Dans les deux cas, vous avez un tableau avec trois éléments : `1`, `2` et `3`.

## Comment insérer dans un tableau JavaScript à un index spécifique avec la méthode `push()`

La méthode [`push()`](https://www.freecodecamp.org/news/how-to-insert-an-element-into-an-array-in-javascript/) dans les tableaux JavaScript est utilisée pour ajouter un ou plusieurs éléments à la fin d'un tableau.

Examinons la syntaxe de la méthode `push()` :

```js
array.push(element1, element2, ..., elementN);
```

Ici, `array` est le tableau auquel vous souhaitez ajouter des éléments, et `element1`, `element2`, etc., sont les éléments que vous souhaitez ajouter à la fin du tableau.

Par exemple, supposons que vous avez un tableau de fruits et que vous souhaitez ajouter un élément à la fin :

```js
const fruits = ['apple', 'banana', 'cherry'];
fruits.push('date');
console.log(fruits); // Sortie : ['apple', 'banana', 'cherry', 'date']
```

Dans ce code, `'date'` est ajouté à la fin du tableau `fruits` en utilisant la méthode `push()`.

Il peut arriver que vous ayez besoin d'insérer un élément à un index spécifique dans un tableau. Dans un tel scénario, vous pouvez utiliser la méthode `push()` en combinaison avec le découpage de tableau.

Voici les étapes pour insérer un élément à un index spécifique dans un tableau :

1. Créez un nouveau tableau vide.

2. Copiez les éléments avant l'index spécifique du tableau original vers le nouveau tableau.

3. Ajoutez le nouvel élément au nouveau tableau.

4. Copiez les éléments après l'index spécifique du tableau original vers le nouveau tableau.

Illustrons ces étapes avec un exemple. Supposons que vous avez un tableau de nombres :

```js
const numbers = [1, 2, 4, 5];
```

Et vous souhaitez insérer le nombre `3` à l'index `2` (rappelons que JavaScript utilise un indexage basé sur zéro). Voici comment vous pouvez accomplir cela :

```js
const index = 2;
const newNumbers = [
    ...numbers.slice(0, index),
    3,
    ...numbers.slice(index)
];
console.log(newNumbers); // Sortie : [1, 2, 3, 4, 5]
```

Dans cet exemple, un nouveau tableau `newNumbers` est créé en copiant les éléments avant l'index `2` en utilisant la méthode `slice()`. Cela est suivi par le nouvel élément `3`, et enfin vous copiez les éléments restants après l'index `2` en utilisant à nouveau la méthode `slice()`. Le résultat est le nouveau tableau `[1, 2, 3, 4, 5]`.

L'opérateur de décomposition (`...`) dans l'exemple ci-dessus est utilisé pour concaténer les tableaux.

Mais ce n'est pas la meilleure approche car vous utilisez une autre méthode (`slice`), rendant le code difficile à comprendre pour un débutant. Explorons comment utiliser la méthode splice qui est plus directe.

## Comment utiliser la méthode `splice()` pour insérer dans un tableau JavaScript à un index spécifique

La méthode `splice()` dans les tableaux JavaScript est utilisée pour ajouter ou supprimer des éléments d'un tableau. Vous pouvez utiliser la méthode `splice()` pour insérer des éléments à un index spécifique dans un tableau.

Voici la syntaxe de [la méthode `splice()`](https://joelolawanle.com/posts/slice-vs-splice-javascript-understanding-differences-use) :

```js
array.splice(start, deleteCount, item1, item2, ..., itemN);
```

* `array` est le tableau que vous souhaitez modifier.

* `start` est l'index où vous souhaitez commencer à modifier le tableau.

* `deleteCount` est le nombre d'éléments que vous souhaitez supprimer du tableau, en commençant à l'index `start`.

* `item1`, `item2`, etc., sont les éléments que vous souhaitez ajouter au tableau à l'index `start`.

Par exemple, supposons que vous avez un tableau de nombres :

```js
const numbers = [1, 2, 4, 5];
```

Et vous souhaitez insérer le nombre `3` à l'index `2`. Voici comment vous pouvez accomplir cela en utilisant la méthode `splice()` :

```js
numbers.splice(2, 0, 3);
console.log(numbers); // Sortie : [1, 2, 3, 4, 5]
```

Dans ce code, la méthode `splice()` est appelée sur le tableau `numbers`, en commençant à l'index `2`, avec un `deleteCount` de `0`. Vous ajoutez ensuite le nouvel élément `3` au tableau à l'index `start`. Le résultat est le tableau modifié `[1, 2, 3, 4, 5]`.

## Conclusion

Dans cet article, vous avez appris les deux techniques principales pour insérer des éléments dans un tableau JavaScript à un index spécifique.

La méthode `splice()` devrait être votre option préférée car elle a une meilleure syntaxe et est plus directe. Connaître ces techniques vous permettra de manipuler les tableaux JavaScript plus efficacement.

Embarquez dans un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.

Amusez-vous bien à coder !