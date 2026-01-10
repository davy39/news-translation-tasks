---
title: Comparaison de tableaux en JavaScript – Comment comparer 2 tableaux en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-16T00:15:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-compare-arrays-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comparaison de tableaux en JavaScript – Comment comparer 2 tableaux en
  JS
seo_desc: 'When handling logic with JavaScript, you might need to compare two arrays
  to see if they are equal or not.

  Really, this shouldn''t be difficult, as you''d think we could easily use either
  the loose equality (double equals - ==) or the strict equality (...'
---

Lorsque vous gérez la logique avec JavaScript, vous pourriez avoir besoin de comparer deux tableaux pour voir s'ils sont égaux ou non.

En réalité, cela ne devrait pas être difficile, car vous pourriez penser que nous pourrions facilement utiliser soit l'égalité lâche (double égal - `==`) soit l'égalité stricte (triple égal - `===`). Mais malheureusement, vous ne pouvez pas les utiliser dans ce cas.

```js
let array1 = [11, 22, 33];
let array2 = [11, 22, 33];

console.log(array1 == array2); //false
console.log(array1 === array2); //false
```

Cela se produit parce que les tableaux JavaScript ont un type d'Objet :

```js
let arrayType = typeof(array1);
console.log(arrayType); //"Object"
```

Les objets ne sont pas comparés en fonction de leurs valeurs mais en fonction des références des variables :

```js
console.log(array1[0] == array1[0]); //true
console.log(array1[1] === array1[1]); //true
```

Mais ce n'est pas ce que vous voulez. Au lieu de cela, vous voulez pouvoir comparer les deux tableaux directement et retourner une seule valeur booléenne sans avoir à vérifier chaque élément un par un.

Dans cet article, vous apprendrez les différentes façons de comparer deux tableaux en JavaScript pour voir s'ils sont similaires ou non.

## Comment comparer deux tableaux en les convertissant en chaînes de caractères

Une approche courante et assez simple que vous pouvez utiliser pour comparer deux tableaux consiste d'abord à convertir ces tableaux en forme de chaîne de caractères.

Il existe deux méthodes différentes que vous pouvez utiliser : vous pouvez décider de convertir votre tableau en texte JSON en utilisant la méthode `JSON.stringify()`, ou vous pouvez utiliser la méthode `.toString()` pour retourner votre tableau sous forme de chaîne de caractères.

**Note :** Les deux méthodes sont différentes, comme vous pouvez le voir ci-dessous :

```js
let array = [11, 22, 33];
console.log(JSON.stringify(array)); //"[11,22,33]"
console.log(array.toString()); //"11,22,33"
```

### Méthode 1 : Comment utiliser `JSON.stringify()`

Cette méthode vous permet de sérialiser chaque tableau en convertissant le tableau en une chaîne JSON. Vous pouvez ensuite comparer les deux chaînes JSON.

```js
let array1 = [11, 22, 33];
let array2 = [11, 22, 33];

console.log(JSON.stringify(array1) === JSON.stringify(array2)); //true
```

Nous pouvons également décider de créer une fonction réutilisable qui nous aide à comparer n'importe quels deux tableaux que nous lui passons :

```js
const compareArrays = (a, b) => {
  return JSON.stringify(a) === JSON.stringify(b);
};

let array1 = [11, 22, 33];
let array2 = [21, 22, 23];
let array3 = [11, 22, 33];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //true
```

### Méthode 2 : Comment utiliser `.toString()`

Similaire à `JSON.stringify()`, cette méthode convertit n'importe quel type de données en une chaîne de caractères et peut également convertir un objet en une chaîne de caractères.

```js
let array1 = [11, 22, 33];
let array2 = [11, 22, 33];

console.log(array1.toString() === array2.toString()); //true
```

Vous pouvez également décider de créer une fonction réutilisable qui vous aide à comparer n'importe quels deux tableaux que vous lui passez :

```js
const compareArrays = (a, b) => {
  return a.toString() === b.toString();
};

let array1 = [11, 22, 33];
let array2 = [21, 22, 23];
let array3 = [11, 22, 33];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //true
```

**Note :** Vous devriez utiliser la méthode `JSON.stringify()`, car elle ne sérialise que votre tableau JavaScript. Le tableau conserve la forme d'un tableau, mais il est simplement analysé pour devenir la version chaîne de caractères du tableau.

## Comment comparer deux tableaux en parcourant leurs valeurs

Les méthodes ci-dessus présentent des lacunes dans certains scénarios. Par exemple, lorsqu'un tableau a une valeur de `null` et un autre a une valeur de `undefined`, lorsque nous utilisons la comparaison stricte, nous obtenons `false` par défaut – ce qui est correct :

```js
console.log(null === undefined); //false
```

Mais lorsque nous utilisons les méthodes `JSON.Strigify()` ou `.toString()`, vous obtenez `true`, ce qui ne devrait pas être le cas :

```js
let array1 = [11, null, 33];
let array2 = [11, undefined, 33];

console.log(JSON.stringify(array1) === JSON.stringify(array2)); //true
console.log(array1.toString() === array2.toString()); //true
```

Une meilleure approche serait de comparer la longueur des tableaux puis de parcourir et comparer chaque élément du tableau.

### Méthode 1 : utiliser `every()`

La méthode `every()` vous aide à exécuter une fonction pour chaque élément de votre tableau. Cette fonction est appelée fonction de rappel. Elle a accès à certains paramètres de base comme l'élément, l'index, et bien plus, que nous pouvons utiliser dans la fonction :

```js
// Syntaxe
array.every((currentValue, index, arr)=> { ... })
```

Dans cette méthode, nous allons d'abord tester si les longueurs des deux tableaux sont comparables. Ensuite, nous allons parcourir un tableau et utiliser son index pour comparer ses éléments à ceux du deuxième tableau :

```js
const compareArrays = (a, b) =>
  a.length === b.length &&
  a.every((element, index) => element === b[index]);

let array1 = [11, 22, 33];
let array2 = [21, 22, 23];
let array3 = [11, 22, 33];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //true
```

Et lorsque nous avons null et undefined comme partie de nos éléments de tableau, il sera capable de détecter qu'ils ne sont pas les mêmes :

```js
const compareArrays = (a, b) =>
  a.length === b.length && a.every((element, index) => element === b[index]);

let array1 = [11, null, 33];
let array2 = [21, 22, 23];
let array3 = [11, undefined, 33];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //false
```

### Méthode 2 : utiliser une boucle for

La méthode every() a une meilleure syntaxe. Cependant, une autre façon dont nous pouvons implémenter la méthode est d'utiliser d'autres méthodes d'itération comme la boucle `for`, `forEach()` ou `map()` avec des instructions `if`. Cela peut être plus facile pour un débutant à comprendre.

```js
const compareArrays = (a, b) => {
  if (a.length !== b.length) return false;
  else {
    // Comparaison de chaque élément de votre tableau
    for (var i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        return false;
      }
    }
    return true;
  }
};

let array1 = [21, null, 33];
let array2 = [21, 22, 23];
let array3 = [21, undefined, 33];
let array4 = [21, 22, 23];

console.log(compareArrays(array1, array2)); //false
console.log(compareArrays(array1, array3)); //false
console.log(compareArrays(array2, array4)); //true
```

Dans les deux méthodes ci-dessus, vous allez d'abord vérifier la longueur, car si la longueur n'est pas égale, cela signifie automatiquement que les deux tableaux ne sont pas égaux et retourne `false`.

Si la longueur est égale, alors nous commençons à vérifier chaque élément. Il retourne `false` dès que deux éléments à la même position `index` dans les deux tableaux sont différents.

## Conclusion

Cet article vous a appris comment comparer deux tableaux en JavaScript en utilisant deux approches principales.

Ces approches consistent à convertir le tableau en une chaîne de caractères avant de les comparer, ou vous pouvez parcourir pour vérifier si leurs valeurs sont similaires les unes aux autres pour une comparaison plus détaillée.

**Note :** Le double égal vérifie si les deux valeurs sont égales, tandis que le triple égal vérifie si les deux valeurs et leurs types de données sont égaux. Vous pouvez lire plus sur [les deux types d'égalité ici](https://www.freecodecamp.org/news/javascript-triple-equals-sign-vs-double-equals-sign-comparison-operators-explained-with-examples/).

Amusez-vous bien en codant !

Embarquez pour un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.