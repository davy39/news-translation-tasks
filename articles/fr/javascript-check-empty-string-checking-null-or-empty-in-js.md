---
title: JavaScript Vérifier une Chaîne Vide – Vérifier Null ou Vide en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-05T22:43:13.000Z'
originalURL: https://freecodecamp.org/news/javascript-check-empty-string-checking-null-or-empty-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--7-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Vérifier une Chaîne Vide – Vérifier Null ou Vide en JS
seo_desc: 'There are a number of reasons why you might need to check if a string is
  empty or not. One of the most important reasons is when you''re retrieving data
  from a database, API, or input field.

  In this article, you will learn how to check if a sting is e...'
---

Il existe de nombreuses raisons pour lesquelles vous pourriez avoir besoin de vérifier si une chaîne est vide ou non. L'une des raisons les plus importantes est lorsque vous récupérez des données depuis une base de données, une API ou un champ de saisie.

Dans cet article, vous apprendrez comment vérifier si une chaîne est vide ou null en JavaScript. Nous verrons de nombreux exemples et méthodes que vous pouvez utiliser afin de comprendre lesquelles utiliser et quand.

## Quelle est la Différence Entre Null et Vide ?

Avant de commencer, vous devez comprendre ce que signifient les termes Null et Vide, et savoir qu'ils ne sont pas synonymes.

Par exemple, si nous déclarons une variable et lui assignons une chaîne vide, puis déclarons une autre variable et lui assignons la valeur Null, nous pouvons les distinguer en regardant leur type de données :

```js
let myStr1 = "";
let myStr2 = null;

console.log(typeof myStr1); // "string"
console.log(typeof myStr2); // "object"
```

En regardant le code ci-dessus, nous pouvons voir que le compilateur/ordinateur interprète chaque valeur différemment. Donc, lorsqu'il est temps de vérifier, nous devons passer des conditions pour les deux types de valeurs car nous, en tant qu'humains, faisons fréquemment référence à `null` comme étant vide.

## Comment Vérifier si une Chaîne est Vide ou Null en JavaScript

Nous savons maintenant qu'une chaîne vide est une chaîne qui ne contient aucun caractère. Il est très simple de vérifier si une chaîne est vide. Nous pouvons utiliser deux méthodes principales qui sont quelque peu similaires car nous utiliserons l'opérateur d'égalité stricte (`==`).

### Comment Vérifier une Chaîne Vide en JavaScript avec la Propriété `length`

Dans cette première méthode, nous vérifierons la longueur de la chaîne en ajoutant la propriété length. Nous vérifierons si la longueur est égale à `0`. Si elle est égale à zéro, cela signifie que la chaîne est vide, comme nous pouvons le voir ci-dessous :

```bash
let myStr = "";

if (myStr.length === 0) {
  console.log("Ceci est une chaîne vide !");
}
```

Ce qui précède retournera ceci :

```bash
"Ceci est une chaîne vide !"
```

Mais cette approche pourrait malheureusement ne pas fonctionner dans toutes les situations. Par exemple, si nous avons une chaîne qui contient des espaces blancs comme vu ci-dessous :

```bash
let myStr = "  ";

if (myStr.length === 0) {
  console.log("Ceci est une chaîne vide !");
}else{
  console.log("Ceci n'est PAS une chaîne vide !");
}
```

Cela retournera :

```bash
"Ceci n'est PAS une chaîne vide !"
```

Nous pouvons facilement corriger cette erreur en supprimant d'abord les espaces blancs à l'aide de la méthode `trim()` avant de vérifier la longueur de la chaîne pour voir si elle est vide comme vu ci-dessous :

```bash
let myStr = "  ";

if (myStr.trim().length === 0) {
  console.log("Ceci est une chaîne vide !");
}else{
  console.log("Ceci n'est PAS une chaîne vide !");
}
```

Cela retournera maintenant ce qui suit :

```bash
"Ceci est une chaîne vide !"
```

Remarque : Si la valeur est null, cela générera une erreur car la propriété `length` ne fonctionne pas pour null.

Pour corriger cela, nous pouvons ajouter un argument qui vérifie si le type de la valeur est une chaîne et ignore cette vérification si ce n'est pas le cas :

```bash
let myStr = null;

if (typeof myStr === "string" && myStr.trim().length === 0) {
  console.log("Ceci est une chaîne vide !");
}
```

### Comment Vérifier une Chaîne Vide en JavaScript par Comparaison de Chaînes

Une autre façon de vérifier si une chaîne est vide est de comparer la chaîne à une chaîne vide.

Par exemple :

```bash
let myStr = "";

if (myStr === "") {
  console.log("Ceci est une chaîne vide !");
}
```

Comme avec la méthode précédente, si nous avons des espaces blancs, cela ne lira pas la chaîne comme vide. Nous devons donc d'abord utiliser la méthode `trim()` pour supprimer toutes les formes d'espaces blancs :

```bash
let myStr = "   ";

if (myStr.trim() === "") {
  console.log("Ceci est une chaîne vide !");
} else {
  console.log("Ceci n'est PAS une chaîne vide !");
}
```

Tout comme nous l'avons fait pour la méthode `length`, nous pouvons également vérifier le type de la valeur afin que cela ne s'exécute que lorsque la valeur est une chaîne :

```bash
let myStr = null;

if (typeof myStr === "string" && myStr.trim() === "") {
  console.log("Ceci est une chaîne vide !");
}
```

## Comment Vérifier Null en JavaScript

Jusqu'à présent, nous avons vu comment vérifier si une chaîne est vide en utilisant les méthodes de longueur et de comparaison.

Maintenant, voyons comment vérifier si elle est `null`, puis vérifier les deux. Pour vérifier `null`, nous comparons simplement cette variable à null lui-même comme suit :

```bash
let myStr = null;

if (myStr === null) {
  console.log("Ceci est une chaîne null !");
}
```

Cela retournera :

```bash
"Ceci est une chaîne null !"
```

## Comment Vérifier une Chaîne Null ou Vide en JavaScript

À ce stade, nous avons appris comment vérifier si une chaîne est vide et également si une variable est définie sur null. Vérifions maintenant les deux de cette manière :

```js
let myStr = null;

if (myStr === null || myStr.trim() === "") {
  console.log("Ceci est une chaîne vide !");
} else {
  console.log("Ceci n'est pas une chaîne vide !");
}
```

Cela retournera :

```bash
"Ceci est une chaîne vide !"
```

## Conclusion

Dans cet article, nous avons appris comment vérifier si une chaîne est vide ou null et pourquoi elles ne sont pas la même chose.

Amusez-vous bien à coder !