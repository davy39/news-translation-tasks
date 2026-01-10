---
title: Parcourir un objet en JavaScript – Comment itérer sur un objet en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-20T15:55:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-iterate-over-objects-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--2-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: Parcourir un objet en JavaScript – Comment itérer sur un objet en JS
seo_desc: 'In JavaScript, when you hear the term "loop", you probably think of using
  the various loop methods like for loops, forEach(), map() and others.

  But in the case of objects, unfortunately, these methods don''t work because objects
  are not iterable.

  This...'
---

En JavaScript, lorsque vous entendez le terme « boucle », vous pensez probablement à utiliser les différentes méthodes de boucle comme les boucles [`for`](https://www.freecodecamp.org/news/javascript-for-loops/), [`forEach()`](https://www.freecodecamp.org/news/javascript-foreach-js-array-for-each-example/), `map()` et autres.

Mais dans le cas des objets, malheureusement, ces méthodes ne fonctionnent pas car les objets ne sont pas itérables.

Cela ne signifie pas que nous ne pouvons pas parcourir un objet – mais cela signifie que nous ne pouvons pas parcourir un objet directement de la même manière que nous le faisons pour un tableau :

```js
let arr = [24, 33, 77];
arr.forEach((val) => console.log(val)); // ✅✅✅

for (val of arr) {
  console.log(val); // ✅✅✅
}

let obj = { age: 12, name: "John Doe" };
obj.forEach((val) => console.log(val)); // ❌❌❌

for (val of obj) {
  console.log(val); // ❌❌❌
}
```

Dans cet article, vous apprendrez comment parcourir un objet en JavaScript. Il existe deux méthodes que vous pouvez utiliser – et l'une d'entre elles précède l'introduction d'ES6.

## Comment parcourir un objet en JavaScript avec une boucle `for...in`

Avant ES6, nous nous appuyions sur la méthode `for...in` chaque fois que nous voulions parcourir un objet.

La boucle `for...in` itère à travers les propriétés de la chaîne de prototypes. Cela signifie que nous devons vérifier si la propriété appartient à l'objet en utilisant `hasOwnProperty` chaque fois que nous parcourons un objet avec la boucle `for...in` :

```js
const population = {
  male: 4,
  female: 93,
  others: 10
};

// Parcourir l'objet
for (const key in population) {
  if (population.hasOwnProperty(key)) {
    console.log(`${key}: ${population[key]}`);
  }
}
```

Pour éviter le stress et la difficulté de la boucle et pour utiliser la méthode `hasOwnProperty`, ES6 et ES8 ont introduit des méthodes statiques d'objet. Celles-ci convertissent les propriétés d'objet en tableaux, nous permettant d'utiliser directement les méthodes de tableau.

## Comment parcourir un objet en JavaScript avec des méthodes statiques d'objet

Un objet est composé de propriétés qui ont des paires clé-valeur, c'est-à-dire que chaque propriété a toujours une valeur correspondante.

Les méthodes statiques d'objet nous permettent d'extraire soit les `keys()`, soit les `values()`, ou les deux clés et valeurs sous forme d'`entries()` dans un tableau, nous permettant d'avoir autant de flexibilité sur eux que nous le faisons avec des tableaux réels.

Nous avons trois méthodes statiques d'objet, qui sont :

* `Object.keys()`

* `Object.values()`

* `Object.entries()`

### Comment parcourir un objet en JavaScript avec la méthode `Object.keys()`

La méthode `Object.keys()` a été introduite dans ES6. Elle prend l'objet que nous voulons parcourir comme argument et retourne un tableau contenant tous les noms de propriétés (également appelés clés).

```js
const population = {
  male: 4,
  female: 93,
  others: 10
};

let genders = Object.keys(population);

console.log(genders); // ["male","female","others"]
```

Cela nous donne maintenant l'avantage d'appliquer n'importe quelle méthode de boucle de tableau pour itérer à travers le tableau et récupérer la valeur de chaque propriété :

```js
let genders = Object.keys(population);

genders.forEach((gender) => console.log(gender));
```

Cela retournera :

```bash
"male"
"female"
"others"
```

Nous pouvons également utiliser la clé pour obtenir la valeur en utilisant la notation entre crochets telle que `population[gender]` comme vu ci-dessous :

```js
genders.forEach((gender) => {
  console.log(`There are ${population[gender]} ${gender}`);
})
```

Cela retournera :

```bash
"There are 4 male"
"There are 93 female"
"There are 10 others"
```

Avant de continuer, utilisons cette méthode pour additionner toute la population en parcourant afin que nous connaissions la population totale :

```js
const population = {
  male: 4,
  female: 93,
  others: 10
};

let totalPopulation = 0;
let genders = Object.keys(population);

genders.forEach((gender) => {
  totalPopulation += population[gender];
});

console.log(totalPopulation); // 107
```

### Comment parcourir un objet en JavaScript avec la méthode `Object.values()`

La méthode `Object.values()` est très similaire à la méthode `Object.keys()` et a été introduite dans ES8. Cette méthode prend l'objet que nous voulons parcourir comme argument et retourne un tableau contenant toutes les valeurs des clés.

```js
const population = {
  male: 4,
  female: 93,
  others: 10
};

let numbers = Object.values(population);

console.log(numbers); // [4,93,10]
```

Cela nous donne maintenant l'avantage d'appliquer n'importe quelle méthode de boucle de tableau pour itérer à travers le tableau et récupérer la `value` de chaque propriété :

```js
let numbers = Object.values(population);

numbers.forEach((number) => console.log(number));
```

Cela retournera :

```bash
4
93
10
```

Nous pouvons effectuer efficacement le calcul total puisque nous pouvons parcourir directement :

```js
let totalPopulation = 0;
let numbers = Object.values(population);

numbers.forEach((number) => {
  totalPopulation += number;
});

console.log(totalPopulation); // 107
```

### Comment parcourir un objet en JavaScript avec la méthode Object.entries()

La méthode `Object.entries()` a également été introduite avec ES8. En termes basiques, ce qu'elle fait est qu'elle produit un tableau de tableaux, où chaque tableau interne a deux éléments qui sont la propriété et la valeur.

```js
const population = {
  male: 4,
  female: 93,
  others: 10
};

let populationArr = Object.entries(population);

console.log(populationArr);
```

Cela produit :

```bash
[
  ['male', 4]
  ['female', 93]
  ['others', 10]
]
```

Cela retourne un tableau de tableaux, chaque tableau interne ayant la `[key, value]`. Vous pouvez utiliser n'importe quelle méthode de tableau pour parcourir :

```js
for (array of populationArr){
  console.log(array);
}

// Output:
// ['male', 4]
// ['female', 93]
// ['others', 10]
```

Nous pourrions décider de [destructurer le tableau](https://www.freecodecamp.org/news/destructuring-patterns-javascript-arrays-and-objects/), afin d'obtenir la `key` et la valeur :

```js
for ([key, value] of populationArr){
  console.log(key);
}
```

Vous pouvez en apprendre davantage sur la façon de [parcourir des tableaux dans cet article](https://www.freecodecamp.org/news/how-to-loop-through-an-array-in-javascript-js-iterate-tutorial/).

## Conclusion

Dans ce tutoriel, vous avez appris que la meilleure façon de parcourir un objet est d'utiliser n'importe quelle méthode statique d'objet en fonction de vos besoins pour d'abord convertir en tableau avant de parcourir.

Amusez-vous bien à coder !

Embarquez pour un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.