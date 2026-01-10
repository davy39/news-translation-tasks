---
title: JavaScript Convertir une Chaîne en Nombre – Exemple JS de Chaîne en Entier
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-29T00:04:12.000Z'
originalURL: https://freecodecamp.org/news/javascript-convert-string-to-number-js-string-to-int-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--5-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Convertir une Chaîne en Nombre – Exemple JS de Chaîne en Entier
seo_desc: 'When you''re working with data from various sources, some of these data
  may arrive in the incorrect format. And you''ll need to correct those formats before
  performing certain actions on the data.

  This is just one of the many reasons you might want to ...'
---

Lorsque vous travaillez avec des données provenant de diverses sources, certaines de ces données peuvent arriver dans un format incorrect. Et vous devrez corriger ces formats avant d'effectuer certaines actions sur les données.

Ceci n'est qu'une des nombreuses raisons pour lesquelles vous pourriez vouloir apprendre à convertir une chaîne en nombre en JavaScript.

Dans cet article, nous allons apprendre à convertir une chaîne en nombre en passant en revue les différentes méthodes et en fournissant des exemples pour chacune.

Avant de commencer, une façon courante de distinguer une valeur de chaîne est qu'elle est toujours enfermée dans des guillemets simples ou doubles, tandis qu'un nombre ne l'est pas :

```js
"John Doe" -> Chaîne
'John Doe' -> Chaîne
"12" -> Chaîne
12 -> Nombre
```

Supposons que nous avons notre chaîne stockée dans une variable. Une bonne façon de vérifier si une variable est une chaîne est d'utiliser l'opérateur `typeof` :

```js
let name = "John Doe";

console.log(typeof name) // "string"
```

Apprenons maintenant à convertir une chaîne en nombre.

## Comment Convertir une Chaîne en Nombre en Utilisant la Fonction `Number()`

La fonction Number est une méthode puissante que vous pouvez utiliser pour convertir des chaînes ou d'autres valeurs en type Number. Cette méthode retournera également `NaN` si la valeur ne peut pas être convertie :

```js
console.log(Number('212'))  // 212
console.log(Number("2124"))  // 2124
console.log(Number('0.0314E+2')); // 3.14

console.log(Number("Hello World"))  // NaN
console.log(Number(undefined))  // NaN
```

Cela fonctionne également avec des variables :

```js
let age = "12";
let password = "John12";

console.log(Number(age)) // 12
console.log(Number(password)) // NaN
```

C'est l'une des méthodes les plus faciles à utiliser car elle fonctionne également avec des valeurs décimales et retourne les valeurs sans les manipuler :

```js
let answer = "12.0";
let answer = "12.0267";

console.log(Number(answer)) // 12.0
console.log(Number(answer)) // 12.0267
```

## Comment Convertir une Chaîne en Nombre en Utilisant les Fonctions `parseInt()` et `parseFloat()`

Les fonctions `parseInt()` et `parseFloat()` prennent une chaîne comme paramètre, puis convertissent cette chaîne en entier/nombre.

Vous pouvez également utiliser `parseInt()` pour convertir un nombre non entier en entier, tandis que `parseFloat()` est la méthode la plus puissante car elle peut maintenir les flottants et certaines logiques mathématiques :

```js
console.log(parseInt('12')) // 12
console.log(parseInt('12.092')) // 12.092
console.log(parseInt('  3.14  ')) // 3
console.log(parseInt('0.0314E+2')) // 0
console.log(parseInt('John Doe')) // NaN

console.log(parseFloat('12')) // 12
console.log(parseFloat('12.092')) // 12.092
console.log(parseFloat('  3.14  ')) // 3.14
console.log(parseFloat('0.0314E+2')) // 3.14
console.log(parseFloat('John Doe')) // NaN
```

Comme d'habitude, cela fonctionne également avec des variables :

```js
let age = "12";

console.log(parseInt(age)) // 12
console.log(parseFloat(age)) // 12
```

Note : La fonction `parseFloat()` retournera toujours NaN lorsque le caractère de la chaîne ne peut pas être converti en nombre :

```js
console.log(parseFloat('N0.0314E+2')) // NaN
```

## Comment Convertir une Chaîne en Nombre en Utilisant l'Opérateur Unaire Plus (`+`)

C'est l'une des façons les plus rapides et les plus faciles de convertir quelque chose en nombre. J'ai dit « quelque chose » car il convertit bien plus que les représentations de chaînes de nombres et de flottants – il fonctionne également sur les valeurs non chaînées `true`, `false`, et `null` ou une chaîne vide.

Un avantage (ou aussi un inconvénient) de cette méthode est qu'elle ne effectue aucune autre opération sur le nombre comme l'arrondi ou la conversion en entier.

Examinons quelques exemples :

```js
console.log(+'100'); // 100
console.log(+'100.0373'); // 100.0373
console.log(+''); // 0
console.log(+null); // 0
console.log(+true); // 1
console.log(+false); // 0
console.log(+'John Doe'); // NaN
console.log(+'0.0314E+2'); // 3.14
```

Comme prévu, cela fonctionne également avec des variables :

```js
let age = "74";

console.log(+age); // 74
```

Si vous comparez `ParseInt()` et l'opérateur unaire plus, vous pourriez finir par utiliser l'opérateur unaire plus plutôt que la méthode `parseInt()` dans certaines situations.

Par exemple, supposons que vous obtenez des valeurs aléatoires – disons une valeur UUID qui à un moment donné peut commencer par des nombres et à d'autres moments peut commencer par des lettres. Cela signifie que l'utilisation de la fonction `parseInt()` peut parfois retourner `NaN` et d'autres fois retourner les premiers caractères qui sont des nombres :

```js
console.log(parseInt("cb34d-234ks-2343f-00xj")); // NaN
console.log(parseInt("997da-00xj-2343f-234ks")); // 997


console.log(+"cb34d-234ks-2343f-00xj"); // NaN
console.log(+"997da-00xj-2343f-234ks"); // NaN
```

## Comment Convertir une Chaîne en Nombre en Utilisant les Méthodes Mathématiques JavaScript

Une autre façon de convertir des chaînes en nombre est d'utiliser certaines méthodes mathématiques JavaScript.

Vous pouvez utiliser la méthode `floor()`, qui arrondira la valeur passée à l'entier le plus proche. La méthode `ceil()`, qui est l'inverse de `floor()`, arrondit à l'entier supérieur le plus proche. Enfin, la méthode `round()`, qui est entre les deux, arrondit simplement le nombre à l'entier le plus proche (soit vers le haut ou vers le bas selon la proximité).

### Comment Convertir une Chaîne en Nombre en Utilisant la Méthode `Math.floor()` JavaScript

Comme je l'ai expliqué ci-dessus, cela retournera toujours un entier. Supposons que nous passons une valeur flottante – elle arrondira la valeur à l'entier le plus proche. Cela retournera `NaN` si nous passons des lettres comme une chaîne ou tout autre caractère non entier :

```js
console.log(Math.floor("14.5")); // 14
console.log(Math.floor("654.508")); // 654
console.log(Math.floor("0.0314E+2")); // 3
console.log(Math.floor("34d-234ks")); // NaN
console.log(Math.floor("cb34d-234ks-2343f-00xj")); // NaN
```

### Comment Convertir une Chaîne en Nombre en Utilisant la Méthode `Math.ceil()` JavaScript

Cela est assez similaire et arrondira uniquement nos valeurs flottantes pour toujours retourner un nombre entier :

```js
console.log(Math.ceil("14.5")); // 15
console.log(Math.ceil("654.508")); // 655
console.log(Math.ceil("0.0314E+2")); // 3
console.log(Math.ceil("34d-234ks")); // NaN
```

### Comment Convertir une Chaîne en Nombre en Utilisant la Méthode `Math.round()` JavaScript

Cela fonctionne comme les deux méthodes mais retourne simplement le nombre entier après l'avoir arrondi à l'entier le plus proche :

```js
console.log(Math.round("14.5")); // 15
console.log(Math.round("654.508")); // 655
console.log(Math.round("0.0314E+2")); // 3
console.log(Math.round("34d-234ks")); // NaN
```

Toutes les méthodes Math ci-dessus fonctionnent également avec des variables :

```js
let age = "14.5";

console.log(Math.floor(age)); // 14
console.log(Math.ceil(age)); // 15
console.log(Math.round(age)); // 15
```

## Comment Convertir une Chaîne en Nombre en Utilisant certaines Opérations Mathématiques

Ce n'est pas vraiment une méthode, mais cela vaut la peine de le savoir. Jusqu'à présent, nous avons discuté des méthodes directes pour réaliser cette conversion – mais dans certains cas, vous pourriez simplement vouloir effectuer ces opérations mathématiques pour aider à la conversion.

Cela inclut la multiplication par `1`, la division par `1` et également la soustraction par `0`. Lorsque nous effectuons l'une de ces opérations sur une chaîne, elles seront converties en entiers :

```js
console.log("14.5" / 1); // 14.5
console.log("0.0314E+2" / 1); // 3.14

console.log("14.5" * 1); // 14.5
console.log("0.0314E+2" * 1); // 3.14

console.log("14.5" - 0); // 14.5
console.log("0.0314E+2" - 0); // 3.14
```

Comme d'habitude, cela fonctionne également avec des variables :

```js
let age = "14.5";

console.log(age / 1); // 14.5
console.log(age * 1); // 14.5
console.log(age - 0); // 14.5
```

## Conclusion

Dans cet article, nous avons examiné diverses méthodes et approches pour convertir des chaînes en entiers en JavaScript.

Il est préférable d'être conscient que de nombreuses méthodes existent afin que vous puissiez choisir ce qui fonctionne le mieux pour vous et l'appliquer dans n'importe quelle situation.