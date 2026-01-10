---
title: Comparaison de dates en JavaScript – Comment comparer des dates en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-29T19:06:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-date-comparison-how-to-compare-dates-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--6-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comparaison de dates en JavaScript – Comment comparer des dates en JS
seo_desc: 'A date is one of the most common datatypes developers use when creating
  real-world applications.

  But often, devs struggle with this datatype and end up using date libraries like
  Moment.js for simple tasks that aren''t worth the large package size that...'
---

Une date est l'un des types de données les plus courants que les développeurs utilisent lors de la création d'applications réelles.

Mais souvent, les développeurs ont du mal avec ce type de données et finissent par utiliser des bibliothèques de dates comme Moment.js pour des tâches simples qui ne valent pas la taille importante du package qui accompagne l'installation d'un package entier.

Dans cet article, nous allons apprendre comment effectuer des comparaisons de dates en JavaScript. Si vous avez besoin du code rapidement, le voici :

```bash
const compareDates = (d1, d2) => {
  let date1 = new Date(d1).getTime();
  let date2 = new Date(d2).getTime();

  if (date1 < date2) {
    console.log(`${d1} est inférieur à ${d2}`);
  } else if (date1 > date2) {
    console.log(`${d1} est supérieur à ${d2}`);
  } else {
    console.log(`Les deux dates sont égales`);
  }
};

compareDates("06/21/2022", "07/28/2021");
compareDates("01/01/2001", "01/01/2001");
compareDates("11/01/2021", "02/01/2022");
```

Cela retournera :

```bash
"06/21/2022 est supérieur à 07/28/2021"
"Les deux dates sont égales"
"11/01/2021 est inférieur à 02/01/2022"
```

Lorsque nous pensons à la comparaison de dates en JavaScript, nous pensons à utiliser l'objet Date (`Date()`) et, bien sûr, cela fonctionne.

L'objet date nous permet d'effectuer des comparaisons en utilisant les opérateurs de comparaison `>`, `<`, `=`, ou `>=`, mais pas les opérateurs de comparaison d'égalité comme `==`, `!=`, `===`, et `!==` (sauf si nous attachons des méthodes de date à l'objet Date).

Commençons par apprendre comment effectuer des comparaisons en utilisant uniquement l'objet date, puis nous verrons comment effectuer des comparaisons d'égalité en utilisant l'objet date ainsi que les méthodes de date.

## Comment effectuer une comparaison de dates avec l'objet Date en JavaScript

Supposons que nous voulons comparer deux dates en JavaScript. Nous pouvons facilement utiliser l'objet Date (`Date()`) de cette manière :

```js
let date1 = new Date();
let date2 = new Date();

if (date1 > date2) {
  console.log("La date 1 est supérieure à la date 2");
} else if (date1 < date2) {
  console.log("La date 1 est inférieure à la date 2");
} else {
  console.log("Les deux dates sont identiques");
}
```

Le code ci-dessus retournera que les deux dates sont identiques parce que nous n'avons pas passé de dates différentes :

```bash
"Les deux dates sont identiques"
```

Passons maintenant des valeurs de dates différentes :

```js
let date1 = new Date();
let date2 = new Date("6/01/2022");

if (date1 > date2) {
  console.log("La date 1 est supérieure à la date 2");
} else if (date1 < date2) {
  console.log("La date 1 est inférieure à la date 2");
} else {
  console.log("Les deux dates sont identiques");
}
```

Cela retournera maintenant ce qui suit :

```bash
"La date 1 est supérieure à la date 2"
```

Heureusement, le code ci-dessus gère l'égalité comme dernière option lorsque les deux premières conditions échouent. Mais supposons que nous essayons de gérer l'égalité comme condition de cette manière :

```js
let date1 = new Date();
let date2 = new Date();

if (date1 === date2) {
  console.log("Les deux dates sont identiques");
} else {
  console.log("Pas les mêmes");
}
```

Cela retournera ce qui suit, ce qui est incorrect :

```bash
"Pas les mêmes"
```

## Comment effectuer une comparaison d'égalité avec JavaScript

Pour gérer la comparaison d'égalité, nous utilisons l'objet date ainsi que la méthode de date `getTime()` qui retourne le nombre de millisecondes. Mais si nous voulons comparer des informations spécifiques comme le jour, le mois, etc., nous pouvons utiliser d'autres méthodes de date comme `getDate()`, `getHours()`, `getDay()`, `getMonth()` et `getYear()`.

```bash
let date1 = new Date();
let date2 = new Date();

if (date1.getTime() === date2.getTime()) {
  console.log("Les deux sont égales");
} else {
  console.log("Pas égales");
}
```

Cela retournera :

```bash
"Les deux sont égales"
```

Nous pouvons passer différentes dates dans l'objet date afin de comparer :

```js
let date1 = new Date("12/01/2021");
let date2 = new Date("09/06/2022");

if (date1.getTime() === date2.getTime()) {
  console.log("Les deux sont égales");
} else {
  console.log("Pas égales");
}
```

Comme prévu, cela retournera :

```bash
"Pas égales"
```

Note : Avec la méthode `getTime()`, nous pouvons effectuer toutes les formes de comparaison de dates en utilisant tous les opérateurs de comparaison, qui sont `>`, `<`, `<=`, `>=`, `==`, `!=`, `===`, et `!==`.

## Comment effectuer des comparaisons de dates spécifiques

Supposons que nous voulons comparer des valeurs de dates spécifiques comme l'année. Alors nous pouvons utiliser la méthode de date `.getYear()` de cette manière :

```js
let date1 = new Date("06/21/2022").getYear();
let date2 = new Date("07/28/2021").getYear();

if (date1 < date2) {
  console.log("Date1 est inférieure à Date2 en termes d'année");
} else if (date1 > date2) {
  console.log("Date1 est supérieure à Date2 en termes d'année");
} else {
  console.log(`Les deux années sont égales`);
}
```

## Conclusion

Dans cet article, vous avez appris comment faire des comparaisons de dates en JavaScript en utilisant l'objet Date sans avoir à installer de bibliothèque.

Bon codage !

Embarquez pour un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.