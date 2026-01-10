---
title: Tableaux 2D JavaScript – Tableaux à deux dimensions en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2023-01-17T16:47:25.000Z'
originalURL: https://freecodecamp.org/news/javascript-2d-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/cover-template--9-.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Tableaux 2D JavaScript – Tableaux à deux dimensions en JS
seo_desc: 'In JavaScript programming, we are all used to creating and working with
  one-dimensional arrays. These are arrays that contain elements (elements of similar
  data types or multiple data types).

  But it’s also good to know that two-dimensional arrays (2D...'
---

En programmation JavaScript, nous sommes tous habitués à créer et à travailler avec des tableaux unidimensionnels. Ce sont des tableaux qui contiennent des éléments (des éléments de types de données similaires ou de plusieurs types de données).

Mais il est également bon de savoir que les tableaux à deux dimensions (2D) existent en JS.

Dans cet article, vous apprendrez ce que sont les tableaux à deux dimensions et comment ils fonctionnent en JavaScript. C'est assez différent des autres langages de programmation car, techniquement, il n'y a pas de tableau à deux dimensions en JavaScript.

## Qu'est-ce qu'un tableau à deux dimensions ?

Un tableau à deux dimensions, également connu sous le nom de tableau 2D, est une collection d'éléments de données disposés dans une structure de type grille avec des lignes et des colonnes. Chaque élément du tableau est appelé une cellule et peut être accessible par ses indices de ligne et de colonne.

```js
[ a1, a2, a3, ..., an,
  b1, b2, b3, ..., bn,
  c1, c2, c3, ..., cn,
  .
  .
  .
  z1, z2, z3, ..., zn ]
```

En JavaScript, il n'y a pas de syntaxe directe pour créer des tableaux 2D comme avec d'autres langages de programmation couramment utilisés comme C, C++ et Java.

Vous pouvez créer des tableaux à deux dimensions en JavaScript grâce à des tableaux irréguliers — un tableau de tableaux. Par exemple, voici à quoi ressemble un tableau irrégulier :

```js
let twoDimensionalArr = [ [ a1, a2, a3, ..., an ],
[ b1, b2, b3, ..., bn ],
[ c1, c2, c3, ..., cn ],
.
.
.
[ z1, z2, z3, ..., zn ] ];
```

Mais il y a une limitation. Il est important de noter que les tableaux à deux dimensions ont une taille fixe. Cela signifie qu'une fois créés, le nombre de lignes et de colonnes doit être fixe. De plus, chaque ligne doit avoir un nombre similaire d'éléments (colonnes).

Par exemple, le tableau ci-dessous a trois lignes et quatre éléments :

```js
let myArray = [
[0, 1, 2, 3], 
[4, 5, 6, 7],
[8, 9, 0, 0]
];
```

La limitation est qu'avec les tableaux irréguliers, vous ne pouvez pas spécifier une ligne et une colonne fixes. Cela signifie qu'un tableau irrégulier pourrait avoir m lignes, chacune ayant un nombre différent d'éléments.

```js
let myArray = [
[0, 1, 2, 3], 
[4, 5, 6, 7],
[8, 9]
];
```

## Pourquoi utiliser un tableau 2D en JavaScript ?

À ce stade, vous pouvez vous demander l'importance d'un tableau 2D, surtout si c'est la première fois que vous lisez à propos des tableaux 2D.

En JavaScript, nous utilisons des tableaux à deux dimensions, également connus sous le nom de matrices, pour stocker et manipuler des données de manière structurée et organisée.

* Ils permettent le stockage et la manipulation efficaces de grandes quantités de données, comme dans le traitement d'images ou de vidéos, les simulations scientifiques et les applications de tableur.

* Les tableaux à deux dimensions permettent également l'utilisation d'opérations matricielles, telles que la multiplication et la transposition de matrices, ce qui peut simplifier les calculs complexes et rendre le code plus lisible.

* Les tableaux à deux dimensions peuvent représenter des matrices mathématiques en algèbre linéaire et une large gamme de données, telles que des graphiques, des cartes et des tableaux.

* Les tableaux à deux dimensions sont couramment utilisés dans des applications qui impliquent des tableaux de données, le traitement d'images et le développement de jeux.

## Comment accéder aux éléments d'un tableau 2D JavaScript

Avant d'apprendre à créer des tableaux 2D en JavaScript, apprenons d'abord comment accéder aux éléments des tableaux 2D.

Vous pouvez accéder aux éléments d'un tableau à deux dimensions en utilisant deux indices, un pour la ligne et un pour la colonne. Supposons que vous ayez le tableau à deux dimensions suivant :

```js
let MathScore = [
    ['John Doe', 20, 60, 'A'],
    ['Jane Doe', 10, 52, 'B'],
    ['Petr Chess', 5, 24, 'F'],
    ['Ling Jess', 28, 43, 'A'],
    ['Ben Liard', 16, 51, 'B']
];
```

Le tableau ci-dessus est un tableau irrégulier dans lequel chaque élément contient le nom de l'étudiant, le score du test, le score de l'examen et la note. Vous pouvez accéder à des éléments spécifiques en utilisant l'index de ligne et de colonne comme vu dans la syntaxe ci-dessous :

```js
arrayName[rowIndex][columnIndex]
```

Pour mieux comprendre cela, convertissons le tableau à deux dimensions ci-dessus en un tableau en utilisant `console.table(arrayName)`.

> **Note :** assurez-vous de remplacer `arrayName` par le nom de votre tableau 2D. Dans mon cas, c'est `MathScore`.

Vous obtiendrez une sortie comme celle-ci, montrant l'index de ligne et de colonne. N'oubliez pas que les tableaux sont indexés à partir de zéro, ce qui signifie que les éléments sont référencés à partir de 0, et non de 1.

![](https://paper-attachments.dropboxusercontent.com/s_357699FE5D3810E96F0B6815928F66401CBB5DFE39FAA8BDA7338BEC543A022F_1673843651418_Untitled.drawio+3.png align="left")

Veuillez noter que la colonne et la ligne `(index)` sont pour l'illustration qui indique les indices des tableaux internes.

Vous utilisez deux crochets pour accéder à un élément du tableau à deux dimensions ou multidimensionnel. Le premier accède aux lignes, tandis que le second accède à l'élément dans la ligne spécifiée.

```js
console.log(MathScore[4][0]); // retourne 'Ben Liard'
console.log(MathScore[2][1]); // retourne 5
console.log(MathScore[1][3]); // retourne 'B'
console.log(MathScore[2][2]); // retourne 24
```

### Comment accéder aux premiers et derniers éléments d'un tableau 2D

Parfois, vous pourriez avoir besoin de trouver les premiers et derniers éléments d'un tableau à deux dimensions. Vous pouvez le faire en utilisant le premier et le dernier index des lignes et des colonnes.

Le premier élément aura toujours l'index de ligne et de colonne de 0, ce qui signifie que vous utiliserez `arrayName[0][0]`.

L'index du dernier élément peut être délicat, cependant. Par exemple, dans l'exemple ci-dessus, le premier élément est 'John Doe' tandis que le dernier est 'B' :

```js
console.log(MathScore[0][0]); // retourne 'John Doe'
console.log(MathScore[MathScore.length-1][(MathScore[MathScore.length -1]).length - 1]); // retourne 'B'
```

### Comment additionner tous les éléments d'un tableau 2D

Dans certaines situations, tous les éléments de votre tableau 2D peuvent être des nombres, donc vous pourriez avoir besoin de les additionner et d'arriver à un seul chiffre. Vous pouvez le faire en utilisant une boucle imbriquée. Vous allez d'abord parcourir les lignes, puis, pour chaque ligne, vous allez parcourir ses éléments.

```js
let numberArr = [
  [10, 20, 60],
  [8, 10, 52],
  [15, 5, 24],
  [26, 28, 43],
  [12, 16, 51]
];

var sum = 0;
numberArr.forEach((row) => {
  row.forEach((element) => {
    sum += element;
  });
});
console.log("La somme de tous les éléments du tableau est :" + sum); // retourne "La somme de tous les éléments du tableau est : 380"
```

## Comment manipuler les tableaux 2D en JavaScript

Vous pouvez manipuler les tableaux 2D comme les tableaux unidimensionnels en utilisant des méthodes de tableau générales comme pop, push, splice et bien plus encore.

Commençons par apprendre comment ajouter/insérer une nouvelle ligne et un nouvel élément au tableau 2D.

### Comment insérer un élément dans un tableau 2D

Vous pouvez ajouter un élément ou plusieurs éléments à un tableau 2D avec les méthodes push() et unshift().

La méthode push() ajoute des éléments à la fin du tableau 2D, tandis que la méthode unshift() ajoute des éléments au début du tableau 2D.

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.push(["Tom Right", 30, 32, "B"]);

MathScore.unshift(["Alice George", 28, 62, "A"]);
```

Lorsque vous utilisez `console.log()` ou `console.table()` sur le tableau, vous verrez que les nouvelles lignes ont été ajoutées :

```js
[
  ["Alice George", 28, 62, "A"],
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"],
  ["Tom Right", 30, 32, "B"]
]
```

Vous pouvez également ajouter des éléments au tableau interne, mais il est incorrect de pousser vers un seul tableau interne sans affecter tous les éléments du tableau. Cela est dû au fait que les tableaux à deux dimensions doivent avoir le même nombre d'éléments dans chaque tableau d'éléments.

```js
MathScore[0].push("B");
```

Au lieu d'affecter un seul élément de tableau, vous pouvez ajouter des éléments à tous les tableaux d'éléments à la fois :

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.forEach((score) => {
  let totalScore = score[1] + score[2];
  score.push(totalScore);
});

console.log(MathScore);
```

Cela retournera :

```js
[
  ["John Doe", 20, 60, "A", 80],
  ["Jane Doe", 10, 52, "B", 62],
  ["Petr Chess", 5, 24, "F", 29],
  ["Ling Jess", 28, 43, "A", 71],
  ["Ben Liard", 16, 51, "B", 67]
]
```

Vous pouvez également utiliser la méthode `unshift()` pour insérer l'élément au début et la méthode `splice()` pour insérer au milieu du tableau :

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.splice(2, 0, ["Alice George", 28, 62, "A"]);
```

Dans l'exemple ci-dessus, `1` est la position où vous souhaitez que le nouveau tableau soit inséré (n'oubliez pas qu'il est indexé à partir de zéro), `0` est utilisé pour ne supprimer aucun élément, et le troisième paramètre est le tableau à ajouter.

Cela donne le résultat suivant :

```js
[
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Alice George", 28, 62, "A"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
]
```

### Comment supprimer un élément d'un tableau 2D

Vous pouvez également supprimer un ou plusieurs éléments du début et de la fin d'un tableau 2D avec les méthodes `pop()` et `shift()`. Cela est similaire au fonctionnement des méthodes `push()` et `unshift()`, mais vous n'ajoutez aucun paramètre aux méthodes cette fois-ci.

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.pop();

MathScore.shift();
```

Lorsque vous utilisez `console.log()` ou `console.table()` sur le tableau, vous verrez que les premiers et derniers éléments du tableau ont été supprimés :

```js
[
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
]
```

Vous pouvez également supprimer des éléments de chaque élément de tableau :

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.forEach((score) => {
  score.pop();
});

console.log(MathScore);
```

Cela retournera :

```js
[
  ["John Doe", 20, 60],
  ["Jane Doe", 10, 52],
  ["Petr Chess", 5, 24],
  ["Ling Jess", 28, 43],
  ["Ben Liard", 16, 51]
]
```

Vous pouvez également utiliser la méthode `shift()` pour supprimer l'élément au début et la méthode `splice()` pour supprimer des éléments de tableau à des positions spécifiques :

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore.splice(2, 1);
```

Dans le code ci-dessus, vous supprimez un élément de la position d'index `2` du tableau 2D `MathScore`. Cela donnera le résultat suivant :

```js
[
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
]
```

**Note :** Toutes les méthodes de tableau JavaScript fonctionneront sur un tableau 2D car il s'agit d'un tableau de tableaux. Vous devez simplement être attentif lorsque vous ajustez des éléments individuels dans le tableau d'éléments. Vous apportez une modification similaire à tous les éléments en parcourant, même si les tableaux 2D en JavaScript ne sont pas stricts.

## Comment créer des tableaux 2D en JavaScript

Il existe deux options pour créer un tableau multidimensionnel. Vous pouvez créer le tableau manuellement avec la notation littérale de tableau, qui utilise des crochets `[]` pour envelopper une liste d'éléments séparés par des virgules. Vous pouvez également utiliser une boucle imbriquée.

### Comment créer un tableau 2D en utilisant un littéral de tableau

C'est comme les exemples que nous avons considérés en utilisant la syntaxe suivante :

```js
let arrayName = [
[ elements ],
[ elements ],
[ elements ], ... ];
```

Par exemple, voici un tableau 2D qui contient des informations sur le score de mathématiques et la note de chaque étudiant :

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];
```

### Comment créer un tableau 2D en utilisant une boucle for imbriquée

Il existe de nombreuses approches pour le faire. Mais généralement, vous créez une boucle imbriquée où la première boucle parcourt les lignes tandis que la deuxième boucle parcourt les éléments du tableau interne (colonnes) :

```js
let arr = [];
let rows = 4;
let columns = 3;

// création d'un tableau à deux dimensions
for (let i = 0; i < rows; i++) {
  arr[i] = [];
  for (let j = 0; j < columns; j++) {
    arr[i][j] = j;
  }
}

console.log(arr);
```

Dans le code ci-dessus, vous allez d'abord parcourir les lignes. Pour chaque ligne, il créera un tableau vide dans le tableau original déclaré et stocké dans la variable `arr`. Vous allez ensuite créer une boucle imbriquée pour parcourir les colonnes et ajouter des éléments individuels.

Dans cet exemple, l'index pour `j` est utilisé et donnera le résultat suivant :

```js
[
  [0, 1, 2],
  [0, 1, 2],
  [0, 1, 2],
  [0, 1, 2]
]
```

Vous pouvez décider de créer un nombre, l'initialiser à 0, puis l'augmenter lors de la boucle afin de ne pas avoir le même nombre pour tous les éléments :

```js
let arr = [];
let rows = 4;
let columns = 3;

let value = 0;
// création d'un tableau à deux dimensions
for (let i = 0; i < rows; i++) {
  arr[i] = [];
  for (let j = 0; j < columns; j++) {
    arr[i][j] = value++;
  }
}

console.log(arr);
```

Cela retournera :

```js
[
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [9, 10, 11]
]
```

Vous pouvez également décider de créer une fonction qui accepte ces valeurs comme arguments :

```js
const create2Darr = (rows, columns) => {
  let arr = [];
  let value = 0;

  // création d'un tableau à deux dimensions
  for (let i = 0; i < rows; i++) {
    arr[i] = [];
    for (let j = 0; j < columns; j++) {
      arr[i][j] = value++;
    }
  }
  console.log(arr);
};

let rows = 4;
let columns = 3;
create2Darr(rows, columns);
```

## Comment mettre à jour les éléments des tableaux 2D en JavaScript

Cela est très similaire à la façon dont vous le faites avec les tableaux unidimensionnels, où vous pouvez mettre à jour la valeur d'un tableau en utilisant l'index pour assigner une autre valeur.

```js
let array = [1, 2, 3];
array[1] = 5;

console.log(array); // retourne [1, 5, 3]
```

Vous pouvez utiliser la même approche pour changer une ligne entière ou même des éléments individuels :

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore[1] = ["Alice George", 28, 62, "A"];
console.log(MathScore);
```

Cela remplacera la valeur de l'index `1` par ce nouveau tableau :

```js
[
  ["John Doe", 20, 60, "A"],
  ["Alice George", 28, 62, "A"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
]
```

Vous pouvez mettre à jour des éléments individuels en suivant les indices de ligne et de colonne et en mettant à jour leurs valeurs :

```js
let MathScore = [
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Petr Chess", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
];

MathScore[2][0] = "Jack Jim";
console.log(MathScore);
```

Cela changera le nom sur la ligne avec l'index `2` en "Jack Jim", comme vu ci-dessous :

```js
[
  ["John Doe", 20, 60, "A"],
  ["Jane Doe", 10, 52, "B"],
  ["Jack Jim", 5, 24, "F"],
  ["Ling Jess", 28, 43, "A"],
  ["Ben Liard", 16, 51, "B"]
]
```

## Conclusion

Dans cet article, vous avez appris ce que sont les tableaux à deux dimensions et comment ils fonctionnent en JavaScript.

Il est important de savoir que les tableaux 2D en JavaScript fonctionnent encore beaucoup comme les tableaux unidimensionnels, alors n'hésitez pas à les ajuster et à les manipuler avec des [méthodes JavaScript](https://www.freecodecamp.org/news/the-javascript-array-handbook/).

Amusez-vous bien à coder !

Vous pouvez accéder à plus de 150 de mes articles en [visitant mon site web](https://joelolawanle.com/contents). Vous pouvez également utiliser le champ de recherche pour voir si j'ai écrit un article spécifique.