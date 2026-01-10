---
title: La destructuration en JavaScript – Comment destructurer les tableaux et les
  objets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-20T18:27:28.000Z'
originalURL: https://freecodecamp.org/news/destructuring-patterns-javascript-arrays-and-objects
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/destructuring-arrays-and-objects-image.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: La destructuration en JavaScript – Comment destructurer les tableaux et
  les objets
seo_desc: 'By Alvin Okoro

  Working with JavaScript arrays and objects can be more fun if you destructure them.
  This helps when you''re fetching stored data.

  In this article, you will learn how you can take destructuring to the next level
  in JavaScript arrays and ...'
---

Par Alvin Okoro

Travailler avec des tableaux et des objets JavaScript peut être plus amusant si vous les destructurez. Cela aide lorsque vous récupérez des données stockées.

Dans cet article, vous apprendrez comment vous pouvez passer la destructuration au niveau supérieur dans les tableaux et objets JavaScript.

### Table des matières :

* Qu'est-ce qu'un tableau ?
* Qu'est-ce qu'un objet ?
* Ce que signifie destructurer en JavaScript
* La destructuration dans les tableaux
* La destructuration dans les objets

## Qu'est-ce qu'un tableau en JavaScript ?

En JavaScript, un tableau est une variable unique qui stocke plusieurs éléments. C'est une collection de données. Nous pouvons déclarer un tableau de deux manières différentes, qui sont :

```js
// Méthode 1
const firstArray = ["JavaScript", "Python", "Go"];

// Méthode 2
const secondArray = new Array(3);
secondArray[0] = "JavaScript";
secondArray[1] = "Python";
secondArray[2] = "Go";

```

Dans la méthode 1, vous pouvez initialiser lors de la déclaration de votre tableau. Dans la méthode 2, vous déclarez votre tableau avec le nombre d'éléments à stocker avant l'initialisation.

## Qu'est-ce qu'un objet en JavaScript ? 

En JavaScript, un objet est une collection de propriétés, et une propriété est une association entre un nom (ou _clé_) et une valeur. 

Écrire un objet en JavaScript ressemble quelque peu à un tableau, mais au lieu de cela, nous utilisons des accolades ou des moustaches pour les créer. Regardons le code ci-dessous montrant un objet voiture avec ses propriétés :

```js
const car = {
  name: "Toyota",
  color: "Black",
  year: 2022,
  engineType: "Automatic",
};

```

Remarquez que ce qui constitue un objet est une clé suivie de sa valeur.

Maintenant que vous connaissez les bases de ce à quoi ressemblent les tableaux et objets JavaScript, parlons davantage de la destructuration.

## Qu'est-ce que la destructuration en JavaScript ?

Imaginez que vous voulez choisir certaines chaussures dans votre collection, et que vous voulez vos préférées, les bleues. La toute première chose que vous devez faire est de chercher dans votre collection et de déballer ce que vous avez là.

Maintenant, la destructuration est exactement comme cette approche que vous avez prise lorsque vous cherchiez vos chaussures. La destructuration est l'acte de déballer des éléments dans un tableau ou un objet. 

La destructuration ne nous permet pas seulement de déballer des éléments, elle vous donne également le pouvoir de manipuler et d'échanger des éléments que vous avez déballés en fonction du type d'opération que vous souhaitez effectuer.

Voyons maintenant comment la destructuration fonctionne dans les tableaux et les objets.

## La destructuration dans les tableaux

Pour destructurer un tableau en JavaScript, nous utilisons les crochets [] pour stocker le nom de la variable qui sera assigné au nom du tableau stockant l'élément.

```js
const [var1, var2, ...] = arrayName;

```

Les points de suspension juste après le `var2` déclaré ci-dessus signifient simplement que nous pouvons créer plus de variables en fonction du nombre d'éléments que nous voulons retirer du tableau.

### Comment assigner des variables avec la destructuration

Maintenant, disons que nous avons un tableau de 6 couleurs mais que nous voulons obtenir seulement les 2 premières couleurs du tableau. Nous pouvons utiliser la destructuration pour obtenir ce que nous voulons.

Regardons cela maintenant :

```js
const colorArr = ["red", "yellow", "blue", "green", "white", "black"];

const [first, second] = colorArr;
console.log(first, second);

// red, yellow

```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/first.png)

Lorsque nous exécutons le code ci-dessus, nous devrions avoir red et yellow enregistrés dans la console. Génial !

### Comment échanger des variables avec la destructuration

Maintenant que vous savez comment assigner des variables avec la destructuration, regardons comment vous pouvez utiliser la destructuration pour échanger rapidement les valeurs des variables.

Supposons que nous avons un tableau de deux éléments, `"food"` et `"fruits"`, et que nous utilisons la destructuration pour assigner ces valeurs aux variables `positionOne` et `positionTwo` :

```js
const edibles = ["food", "fruits"];

let [positionOne, positionTwo] = edibles;
console.log(positionOne, positionTwo);

// food, fruits

```

Si nous voulons plus tard échanger les valeurs de `positionOne` et `positionTwo` sans destructuration, nous aurions besoin d'utiliser une autre variable pour temporairement contenir la valeur de l'une des variables actuelles, puis effectuer l'échange.

Par exemple :

```js
const edibles = ["food", "fruits"];

let [positionOne, positionTwo] = edibles;
const temp = positionOne;

positionOne = positionTwo;
positionTwo = temp;
console.log(positionOne, positionTwo);

// fruits, food

```

Mais avec la destructuration, nous pourrions échanger les valeurs de `positionOne` et `positionTwo` très facilement, sans avoir à utiliser une variable temporaire :

```js
const edibles = ["food", "fruits"];

let [positionOne, positionTwo] = edibles;
[positionOne, positionTwo] = [positionTwo, positionOne];
console.log(positionOne, positionTwo);

// fruits, food

```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/second.png)

Notez que cette méthode d'échange de variables ne mute pas le tableau original. Si vous enregistrez `edibles` dans la console, vous verrez que sa valeur est toujours `["food", "fruits"]`.

### Comment muter les tableaux avec la destructuration

Muter signifie changer la forme ou la valeur d'un élément. Une valeur est dite mutable si elle peut être changée. Avec l'aide de la destructuration dans les tableaux, nous pouvons muter les tableaux eux-mêmes.

Supposons que nous avons le même tableau `edibles`, et que nous voulons muter le tableau en échangeant l'ordre de `"food"` et `"fruits"`.

Nous pouvons faire cela avec la destructuration, de manière similaire à la façon dont nous avons échangé les valeurs de deux variables auparavant :

```js
const edibles = ["food", "fruits"];

[edibles[0], edibles[1]] = [edibles[1], edibles[0]];
console.log(edibles);

// ["fruits", "food"]

```

### La destructuration dans les objets

Lorsque nous destructurons des objets, nous utilisons des accolades avec le nom exact de ce que nous avons dans l'objet. Contrairement aux tableaux où nous pouvons utiliser n'importe quel nom de variable pour déballer l'élément, les objets permettent uniquement l'utilisation du nom des données stockées.

De manière intéressante, nous pouvons manipuler et assigner un nom de variable aux données que nous voulons obtenir de l'objet. Voyons tout cela maintenant dans le code.

```js
const freeCodeCamp = {
  frontend: "React",
  backend: "Node",
  database: "MongoDB",
};

const { frontend, backend } = freeCodeCamp;
console.log(frontend, backend);

// React, Node

```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/3-4.png)

Enregistrer ce que nous avons dans la console montre la valeur de frontend et backend. Voyons maintenant comment assigner un nom de variable à l'objet que nous voulons déballer.

```js
const freeCodeCamp = {
  frontend: "React",
  backend: "Node",
  database: "MongoDB",
};

const { frontend: courseOne, backend: courseTwo } = freeCodeCamp;
console.log(courseOne, courseTwo);

// React, Node

```

![Image](https://www.freecodecamp.org/news/content/images/2022/01/4-2.png)

Comme vous pouvez le voir, nous avons `courseOne` et `courseTwo` comme les noms des données que nous voulons déballer. 

Assigner un nom de variable nous aidera toujours à garder notre code propre, surtout lorsqu'il s'agit de travailler avec des données externes lorsque nous voulons les déballer et les réutiliser dans notre code.

## Conclusion

Vous avez maintenant appris comment travailler avec la destructuration dans les tableaux et les objets. Vous avez également appris comment échanger les positions des éléments dans les tableaux.

Alors, quoi de neuf ? Essayez de pratiquer et passez vos compétences en destructuration au niveau supérieur.