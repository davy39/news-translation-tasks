---
title: Inverser une chaîne de caractères en JavaScript – Inverser une chaîne avec
  la méthode JS .reverse()
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-07T17:01:57.000Z'
originalURL: https://freecodecamp.org/news/reversing-a-string-in-javascript-invert-a-string-with-the-js-reverse-method
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--8-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Inverser une chaîne de caractères en JavaScript – Inverser une chaîne avec
  la méthode JS .reverse()
seo_desc: 'Reversing strings in JavaScript is something you''ll need to do often on
  your web development journey. You might need to reverse a string during interviews,
  when solving algorithms, or when doing data manipulation.

  We will learn how to reverse a strin...'
---

Inverser des chaînes de caractères en JavaScript est quelque chose que vous devrez faire souvent lors de votre parcours en développement web. Vous pourriez avoir besoin d'inverser une chaîne lors d'entretiens, en résolvant des algorithmes, ou en manipulant des données.

Nous allons apprendre comment inverser une chaîne de caractères en JavaScript en utilisant des méthodes intégrées ainsi que la méthode `reverse()` de JavaScript dans cet article.

Pour ceux qui sont pressés, voici une ligne de code pour vous aider à inverser une chaîne en JavaScript :

```bash
let myReversedString = myString.split("").reverse().join("");
```

Ou vous pouvez utiliser ceci :

```bash
let myReversedString = [...myString].reverse().join("");
```

Discutons maintenant de ces méthodes et du rôle qu'elles jouent pour nous aider à inverser des chaînes en JavaScript.

## Comment inverser une chaîne avec les méthodes JavaScript

Utiliser les méthodes JavaScript pour inverser une chaîne est simple. Cela est dû au fait que nous allons utiliser seulement trois méthodes qui remplissent différentes fonctions et sont toutes utilisées ensemble pour atteindre cet objectif commun.

En général, nous divisons la chaîne particulière en un tableau en utilisant soit l'opérateur de décomposition soit la méthode `split()`. Ensuite, nous utilisons la méthode `reverse()`, qui ne peut être utilisée que pour inverser les éléments d'un tableau. Et enfin, nous joignons ce tableau ensemble en une chaîne en utilisant la méthode `join()`.

Essayons chacune de ces méthodes séparément.

### Comment diviser une chaîne en JavaScript

Il existe deux méthodes principales pour diviser une chaîne en JavaScript : utiliser l'opérateur de décomposition ou la méthode `split()`.

#### Comment diviser une chaîne avec la méthode split()

La méthode `split()` est une méthode très puissante que vous utilisez pour diviser une chaîne en une liste ordonnée de sous-chaînes basée sur un motif donné.

Par exemple, si nous avons une chaîne de mois séparés par des virgules que nous voulons diviser en un tableau de mois, nous pourrions avoir quelque chose comme ceci :

```bash
const months_string = 'Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec';

console.log(months_string.split(','))
```

Cela produira le tableau suivant :

```bash
["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
```

Dans notre cas, notre chaîne pourrait être une chaîne régulière sans rien séparant chaque caractère. Alors tout ce que nous avons à faire est de passer une chaîne vide sans espaces, comme vu ci-dessous :

```bash
let myString = "Hello World";

console.log(myString.split("")); // ["H","e","l","l","o"," ","W","o","r","l","d"]
console.log(myString.split(" ")); // ["Hello","World"]
```

#### Comment diviser une chaîne avec l'opérateur de décomposition

L'opérateur de décomposition est une addition ES6 qui facilite la division d'une chaîne en un tableau. Il fait bien plus que simplement diviser une chaîne :

```bash
let myString = "Hello World";

console.log([...myString]); // ["H","e","l","l","o"," ","W","o","r","l","d"]
```

### Comment inverser un tableau de chaînes avec la méthode `reverse()`

Jusqu'à présent, nous avons appris comment diviser une chaîne. Et la méthode `split()`, bien sûr, divise la chaîne en un tableau. Et maintenant vous pouvez appliquer la méthode d'inversion de tableau, comme montré ci-dessous :

```bash
let myString = "Hello World";

let splitString1 = myString.split("");
let splitString2 = myString.split(" ");

console.log(splitString1.reverse()); // ["d","l","r","o","W"," ","o","l","l","e","H"]
console.log(splitString2.reverse()); // ["World","Hello"]
```

Nous pouvons également appliquer cela à l'opérateur de décomposition de cette manière, mais nous ne pourrons plus définir comment nous voulons diviser notre chaîne :

```bash
let myString = "Hello World";

console.log([...myString].reverse()); // ["d","l","r","o","W"," ","o","l","l","e","H"]
```

### Comment joindre un tableau de chaînes ensemble avec la méthode `join()`

C'est une autre méthode puissante qui fonctionne dans le sens inverse de la méthode `split()`. Elle crée une nouvelle chaîne en concaténant tous les éléments d'un tableau qui sont séparés par des virgules ou toute autre chaîne spécifiée comme séparateur.

Par exemple, si nous avons un tableau de chaînes que nous voulons joindre en une seule chaîne séparée par un tiret (-), nous pouvons faire quelque chose comme ceci :

```js
let monthArray = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
console.log(monthArray.join("-"));
```

Et cela retournera ce qui suit :

```bash
"Jan-Feb-Mar-Apr-May-Jun-Jul-Aug-Sep-Oct-Nov-Dec"
```

Dans notre cas, nous avons déjà inversé la chaîne, et nous ne voulons rien entre les deux. Cela signifie que nous allons simplement passer une chaîne vide de cette manière :

```bash
let myString = "Hello World";

let splitString1 = myString.split("");
let splitString2 = myString.split(" ");

let reversedStringArray1 = splitString1.reverse();
let reversedStringArray2 = splitString2.reverse();

console.log(reversedStringArray1.join("")); // "dlroW olleH"
console.log(reversedStringArray2.join("")); // "WorldHello"
```

À la fin, nous pouvons effectuer toutes ces opérations avec une seule ligne de code en rassemblant toutes les méthodes dans le bon ordre :

```bash
let myString = "Hello World";

let myReversedString = myString.split("").reverse().join("");

console.log(myReversedString); // "dlroW olleH"
```

Et le même principe s'applique à l'opérateur de décomposition :

```js
let myString = "Hello World";

let myReversedString = [...myString].reverse().join("");

console.log(myReversedString); // "dlroW olleH"
```

## Conclusion

Dans ce tutoriel, nous avons appris comment inverser une chaîne en utilisant la méthode `reverse()`, ainsi que d'autres méthodes JavaScript. Nous avons également vu comment les méthodes fonctionnent avec des exemples.

Amusez-vous bien à coder !