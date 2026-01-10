---
title: JavaScript Vérifier si Indéfini – Comment Tester l'Indéfini en JS
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-07-11T17:13:42.000Z'
originalURL: https://freecodecamp.org/news/javascript-check-if-undefined-how-to-test-for-undefined-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/cover-template--9-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Vérifier si Indéfini – Comment Tester l'Indéfini en JS
seo_desc: 'An undefined variable or anything without a value will always return "undefined"
  in JavaScript. This is not the same as null, despite the fact that both imply an
  empty state.

  You''ll typically assign a value to a variable after you declare it, but thi...'
---

Une variable indéfinie ou tout ce qui n'a pas de valeur retournera toujours "undefined" en JavaScript. Ce n'est pas la même chose que null, malgré le fait que les deux impliquent un état vide.

Vous attribuerez généralement une valeur à une variable après l'avoir déclarée, mais ce n'est pas toujours le cas.

Lorsque qu'une variable est déclarée ou initialisée mais qu'aucune valeur ne lui est attribuée, JavaScript affiche automatiquement "undefined". Cela ressemble à ceci :

```bash
let myStr;

console.log(myStr); // undefined
```

De plus, lorsque vous essayez d'accéder à des valeurs dans, par exemple, un tableau ou un objet qui n'existe pas, cela retournera `undefined`.

```bash
let user = {
    name: "John Doe",
    age: 14
};

console.log(user.hobby); // undefined
```

Voici un autre exemple :

```bash
let myArr = [12, 33, 44];

console.log(myArr[7]); // undefined
```

Dans cet article, vous apprendrez les différentes méthodes et approches que vous pouvez utiliser pour savoir si une variable est `undefined` en JavaScript. Cela est nécessaire si vous souhaitez éviter que votre code ne génère des erreurs lors de l'exécution d'une opération avec une variable indéfinie.

Au cas où vous seriez pressé, voici les trois méthodes standard qui peuvent vous aider à vérifier si une variable est `undefined` en JavaScript :

```bash
if(myStr === undefined){}
if(typeof myArr[7] === "undefined"){}
if(user.hobby === void 0){}
```

Expliquons maintenant chacune de ces méthodes plus en détail.

## Comment Vérifier si une Variable est Indéfinie en JavaScript avec une Comparaison Directe

L'une des premières méthodes qui vient à l'esprit est la comparaison directe. Il s'agit de comparer la sortie pour voir si elle retourne `undefined`. Vous pouvez facilement le faire de la manière suivante :

```bash
let user = {
    name: "John Doe",
    age: 14
};

if (user.hobby === undefined) {
    console.log("Ceci est indéfini");
}
```

Cela fonctionne également pour les tableaux comme vous pouvez le voir ci-dessous :

```bash
let scores = [12, 34, 66, 78];

if (scores[10] === undefined) {
    console.log("Ceci est indéfini");
}
```

Et cela fonctionne définitivement aussi pour d'autres variables :

```bash
let name;

if (name === undefined) {
    console.log("Ceci est indéfini");
}
```

## Comment Vérifier si une Variable est Indéfinie en JavaScript avec `typeof`

Nous pouvons également utiliser le type de la variable pour vérifier si elle est `undefined`. Heureusement pour nous, undefined est un type de données pour une valeur indéfinie comme vous pouvez le voir ci-dessous :

```bash
let name;

console.log(typeof name); // "undefined"
```

Avec cela, nous pouvons maintenant utiliser le type de données pour vérifier l'indéfini pour tous les types de données comme nous l'avons vu ci-dessus. Voici à quoi ressemblera la vérification pour les trois scénarios que nous avons considérés :

```bash
if(typeof user.hobby === "undefined"){}
if(typeof scores[10] === "undefined"){}
if(typeof name === "undefined"){}
```

## Comment Vérifier si une Variable est Indéfinie en JavaScript avec l'Opérateur `Void`

L'opérateur `void` est souvent utilisé pour obtenir la valeur primitive `undefined`. Vous pouvez le faire en utilisant "`void(0)`" qui est similaire à "`void 0`" comme vous pouvez le voir ci-dessous :

```bash
console.log(void 0); // undefined
console.log(void(0)); // undefined
```

En réalité, cela fonctionne comme une comparaison directe (que nous avons vue précédemment). Mais nous remplacerions undefined par `void(0)` ou `void 0` comme vu ci-dessous :

```bash
if(typeof user.hobby === void 0){}
if(typeof scores[10] === void 0){}
if(typeof name === void 0){}
```

Ou comme ceci :

```js
if(typeof user.hobby === void(0)){}
if(typeof scores[10] === void(0)){}
if(typeof name === void(0)){}
```

## Conclusion

Dans cet article, nous avons appris comment vérifier si une variable est indéfinie et ce qui provoque qu'une variable soit indéfinie.

Nous avons également appris trois méthodes que nous pouvons utiliser pour vérifier si une variable est indéfinie. Toutes les méthodes fonctionnent parfaitement. Le choix de votre méthode préférée vous appartient entièrement.

Amusez-vous bien à coder !