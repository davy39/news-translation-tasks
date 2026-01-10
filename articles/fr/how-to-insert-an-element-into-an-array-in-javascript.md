---
title: Insérer dans un tableau en JavaScript – Comment insérer un élément dans un
  tableau en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-18T14:09:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-insert-an-element-into-an-array-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--1-.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Insérer dans un tableau en JavaScript – Comment insérer un élément dans
  un tableau en JS
seo_desc: 'The array datatype is one of the most commonly used datatypes when you''re
  working with an ordered list of values.

  Each value is referred to as an element with a unique id. It stores elements of
  various datatypes that you can access through a single v...'
---

Le type de données tableau est l'un des types de données les plus couramment utilisés lorsque vous travaillez avec une liste ordonnée de valeurs.

Chaque valeur est appelée un élément avec un `id` unique. Il stocke des éléments de divers types de données auxquels vous pouvez accéder via une seule variable.

En pratique, un tableau pourrait contenir une liste d'utilisateurs, et nous pourrions avoir besoin d'ajouter un ou des éléments au tableau après le dernier élément, avant le premier élément, ou à un point spécifié dans notre tableau.

Cet article vous montrera comment insérer un élément dans un tableau en utilisant JavaScript. Au cas où vous seriez pressé, voici les méthodes que nous allons discuter en profondeur dans cet article :

```bash
// Ajouter au début d'un tableau
Array.unshift(element);

// Ajouter à la fin d'un tableau
Array.push(element);

// Ajouter à un emplacement spécifié
Array.splice(position_de_depart, 0, nouvel_element...);

// Ajouter avec la méthode concat sans modifier le tableau original
let newArray = [].concat(Array, element);
```

* Lorsque vous souhaitez ajouter un élément à la fin de votre tableau, utilisez `push()`.
  
* Si vous devez ajouter un élément au début de votre tableau, utilisez `unshift()`.
  
* Si vous souhaitez ajouter un élément à un emplacement particulier de votre tableau, utilisez `splice()`.
  
* Et enfin, lorsque vous souhaitez conserver votre tableau original, vous pouvez utiliser la méthode `concat()`.
  

## Comment ajouter au début d'un tableau avec la méthode `unshift()`

En JavaScript, vous utilisez la méthode `unshift()` pour ajouter un ou plusieurs éléments au début d'un tableau et elle retourne la longueur du tableau après que les nouveaux éléments ont été ajoutés.

Si nous avons un tableau de pays et que nous voulons ajouter un pays avant "Nigeria", qui est actuellement à l'index `0`, nous pouvons le faire avec la méthode `unshift()`, comme montré ci-dessous :

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

countries.unshift("Kenya");

console.log(countries); // ["Kenya","Nigeria","Ghana","Rwanda"]
```

Comme nous l'avons dit, nous pouvons également ajouter plus d'un élément en utilisant la méthode `unshift()` :

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

countries.unshift("South Africa", "Mali", "Kenya");

console.log(countries); // ["South Africa","Mali","Kenya","Nigeria","Ghana","Rwanda"]
```

Dans notre explication de la méthode `unshift()`, nous avons également indiqué qu'elle retourne la longueur du nouveau tableau, ce qui est vrai :

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

let countriesLength = countries.unshift("South Africa", "Mali", "Kenya");

console.log(countriesLength); // 6
```

## Comment ajouter à la fin d'un tableau avec la méthode `push()`

La méthode `push()` est similaire à la méthode `unshift()` car elle ajoute un élément à la fin d'un tableau plutôt qu'au début. Elle retourne la longueur du nouveau tableau et, comme la méthode `unshift()`, peut être utilisée pour ajouter plus d'un élément.

Essayons le même exemple à nouveau, mais cette fois ajoutons-les à la fin du tableau en utilisant la méthode `push()` :

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

countries.push("Kenya");

console.log(countries); // ["Nigeria","Ghana","Rwanda","Kenya"]

countries.push("South Africa", "Mali");

console.log(countries); // ["Nigeria","Ghana","Rwanda","Kenya","South Africa","Mali"]
```

Et comme nous l'avons dit, nous pouvons l'utiliser pour obtenir la longueur du nouveau tableau :

```bash
const countries = ["Nigeria", "Ghana", "Rwanda"];

let countriesLength = countries.push("Kenya");

console.log(countriesLength); // 4
```

## Comment ajouter à un emplacement spécifié dans un tableau avec la méthode `splice()`

Jusqu'à présent, nous avons seulement vu comment ajouter un élément au début ou à la fin d'un tableau. Mais vous pourriez vous demander comment ajouter un élément à un emplacement spécifique dans un tableau. Eh bien, vous pouvez le faire avec la méthode `splice()`.

La méthode `splice()` est une méthode polyvalente pour modifier le contenu d'un tableau en supprimant, remplaçant ou ajoutant des éléments à des positions spécifiées du tableau. Cette section couvrira comment utiliser cette méthode pour ajouter un élément à un emplacement spécifique.

Par exemple, considérons le tableau suivant de pays, qui contient trois éléments (pays) disposés par ordre alphabétique :

```bash
const countries = ["Ghana", "Nigeria", "Rwanda"];
```

Supposons que nous voulons ajouter "Kenya", qui, selon l'ordre alphabétique, devrait être placé en deuxième position, à l'index `1` (après Ghana et avant Nigeria). Dans ce cas, nous utiliserons la méthode `splice()` avec la syntaxe suivante :

```bash
Array.splice(position_de_depart, 0, nouvel_element...);
```

* Le `position_de_depart` spécifie l'index où nous voulons que les nouveaux éléments soient insérés dans le tableau. S'il y a plusieurs éléments, il spécifie où les éléments insérés commenceront.
  
* Si nous voulons ajouter au tableau, nous définissons le deuxième argument à zéro (`0`), indiquant à la méthode `splice()` de ne supprimer aucun élément du tableau.
  
* Le ou les paramètres suivants ou éléments peuvent être plus d'un, car ce sont les éléments que nous voulons ajouter au tableau à la position spécifiée.
  

Par exemple, plaçons "Kenya" après "Ghana" dans notre tableau de pays :

```bash
const countries = ["Ghana", "Nigeria", "Rwanda"];

countries.splice(1, 0, 'Kenya');

console.log(countries); // ["Ghana","Kenya","Nigeria","Rwanda"]
```

![](https://paper-attachments.dropbox.com/s_8F843EE332F48B356BFA84EB69212DF653EB2859C5739E7748DB9362133DCFB7_1658069550677_illustration.jpg align="left")

Tout comme nous l'avons fait pour les autres méthodes, nous pouvons également ajouter plus d'un élément :

```bash
const countries = ["Ghana", "Nigeria", "Rwanda"];

countries.splice(1, 0, 'Kenya', 'Mali');

console.log(countries); // ["Ghana","Kenya","Mali","Nigeria","Rwanda"]
```

Notez que les méthodes précédentes retournent la longueur du nouveau tableau, mais la méthode splice modifie le tableau original. Elle ne supprime aucun élément, donc elle retourne un tableau vide.

Vous pouvez en lire plus sur [Slice vs. Splice en JavaScript et quand les utiliser dans cet article détaillé](https://joelolawanle.com/posts/slice-vs-splice-javascript-understanding-differences-use).

## Comment ajouter des éléments dans un tableau avec la méthode `concat()`

Nous pouvons utiliser la méthode `concat()` pour ajouter des éléments à un tableau sans modifier ou altérer le tableau original. Au lieu de cela, en créer un nouveau est une meilleure méthode si nous ne voulons pas que le tableau original soit affecté.

Nous pouvons utiliser cette méthode pour ajouter des éléments à la fois au début et à la fin du tableau en fonction de l'endroit où nous plaçons les éléments :

```bash
const countries = ["Ghana", "Nigeria", "Rwanda"];

let newCountries = [].concat("Mali", countries, "Kenya");

console.log(newCountries); // ["Mali","Ghana","Nigeria","Rwanda","Kenya"]
```

La méthode `concat()` nous permet également de joindre deux (ou plus) tableaux en un seul nouveau tableau :

```bash
const africanCountries = ["Ghana", "Nigeria", "Rwanda"];
const europeanCountries = ["Germany", "France", "spain"];

let countries = [].concat(africanCountries, europeanCountries);

console.log(countries); // ["Ghana","Nigeria","Rwanda","Germany","France","spain"]
```

## Conclusion

Dans cet article, nous avons appris diverses façons d'ajouter des éléments dans un tableau au début, à la fin, ou à n'importe quelle position en utilisant la méthode `splice()`.

Nous avons également appris que la méthode `concat()` nous permet d'ajouter des éléments sans altérer le tableau original.

Utilisez n'importe quelle méthode qui répond à vos besoins.

Bon codage !

Embarquez pour un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents) écrits par moi. Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.