---
title: Une brève introduction à la déstructuration des tableaux en ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-01T01:39:22.000Z'
originalURL: https://freecodecamp.org/news/array-destructuring-in-es6-30e398f21d10
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5TN-55RU-eTfNlcDL2RR1g.png
tags:
- name: arrays
  slug: arrays
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Une brève introduction à la déstructuration des tableaux en ES6
seo_desc: 'By Kevwe Ochuko

  Destructuring in JavaScript is a simplified method of extracting multiple properties
  from an array by taking the structure and deconstructing it down into its own constituent
  parts through assignments by using a syntax that looks simi...'
---

Par Kevwe Ochuko

La **déstructuration** en JavaScript est une méthode simplifiée pour extraire plusieurs propriétés d'un tableau en prenant la structure et en la décomposant en ses propres parties constituantes par le biais d'affectations en utilisant une syntaxe qui ressemble aux littéraux de tableau.

Elle crée un motif qui décrit le type de valeur que vous attendez et effectue l'affectation. La déstructuration des tableaux utilise la position.

Voir l'extrait de code ci-dessous.

```js
const [first, second, third] = ["Laide", "Gabriel", "Jets"];

```

_La syntaxe avec déstructuration._

```js
const first = "Laide",
      second = "Gabriel",
      third = "Jets";

```

_La syntaxe sans déstructuration._

> _Vous ne pouvez pas utiliser de nombres pour la déstructuration. Les nombres généreront une erreur car les nombres ne peuvent pas être des noms de variables._

```js
const [1, 2, 3] = ["Laide", "Gabriel", "Jets"];

```

_Cette syntaxe génère une erreur._

La **déstructuration** a rendu l'extraction de données d'un tableau très simple et lisible. Imaginez essayer d'extraire des données d'un tableau imbriqué avec 5 ou 6 niveaux. Cela serait très fastidieux. Vous utilisez un littéral de tableau du côté gauche de l'affectation.

```js
const householdItems = ["Table", "Chair", "Fan"];
const [a, b, c] = householdItems;

```

Il prend chaque variable du littéral de tableau du côté gauche et la mappe à l'élément correspondant au même index dans le tableau.

```js
console.log(a); // Sortie: Table
console.log(b); // Sortie: Chair
console.log(c); // Sortie: Fan

```

La déclaration et l'affectation peuvent être faites séparément dans la déstructuration.

```js
let first, second;
[first, second] = ["Male", "Female"];

```

Si le nombre de variables passées aux littéraux de tableau de déstructuration est supérieur au nombre d'éléments dans le tableau, alors les variables qui ne sont pas mappées à un élément du tableau retournent `undefined`_._

```js
const householdItems = ["Table", "Chair", "Fan", "Rug"];
const [a, b, c, d, e] = householdItems;

console.log(c); // Sortie: Fan
console.log(d); // Sortie: Rug
console.log(e); // Sortie: undefined

```

Si le nombre de variables passées aux littéraux de tableau de déstructuration est inférieur au nombre d'éléments dans le tableau, les éléments sans variables à mapper sont simplement laissés. Il n'y a aucune erreur.

```js
const householdItems = ["Table", "Chair", "Fan", "Rug"];
const [a, b, c] = householdItems;
console.log(c); // Sortie: Fan
```

### **Déstructuration des tableaux retournés**

La déstructuration facilite le travail avec une fonction qui retourne un tableau comme valeur de manière plus précise. Elle fonctionne pour tous les itérables.

```js
function runners() {
  return ["Sandra", "Ola", "Chi"];
}

const [a, b, c] = runners();

console.log(a); // Sortie: Sandra
console.log(b); // Sortie: Ola
console.log(c); // Sortie: Chi

```

### **Valeur par défaut**

La déstructuration permet d'assigner une valeur par défaut à une variable si aucune valeur ou `_undefined_` est passée. C'est comme fournir une solution de repli lorsque rien n'est trouvé.

```js
let a, b;
[a = 40, b = 4] = [];
console.log(a); // Sortie: 40
console.log(b); // Sortie: 4

[a = 40, b = 4] = [1, 23];
console.log(a); // Sortie: 1
console.log(b); // Sortie: 23
```

Les valeurs par défaut peuvent également faire référence à d'autres variables, y compris celles du même littéral de tableau.

```js
const [first = "Cotlin", second = first] = [];
console.log(first); // Sortie: Cotlin
console.log(second); // Sortie: Cotlin

```

```js
const [first = "Cotlin", second = first] = ["Koku"];
console.log(first); // Sortie: Koku
console.log(second); // Sortie: Koku

```

```js
const [first = "Cotlin", second = first] = ["Koku", "Lydia"];
console.log(first); // Sortie: Koku
console.log(second); // Sortie: Lydia

```

### Ignorer certaines valeurs

La déstructuration vous permet de mapper une variable aux éléments qui vous intéressent. Vous pouvez ignorer ou sauter les autres éléments du tableau en utilisant des virgules de fin.

```js
let a, b;
[a, , b] = ["Lordy", "Crown", "Roses"];

console.log(a); // Sortie: Lordy
console.log(b); // Sortie: Roses

```

### **Le paramètre Rest et la syntaxe de propagation**

Le nouvel **opérateur** _()_ qui a été ajouté dans ES6 peut être utilisé dans la déstructuration. Si l'**opérateur** _()_ apparaît du côté gauche dans la déstructuration, alors c'est un [**PARAMÈTRE REST**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)**.** Un paramètre Rest est utilisé pour mapper tous les éléments restants du tableau qui n'ont pas été mappés à la variable rest elle-même. C'est comme rassembler ce qui reste. La variable Rest doit toujours être la dernière, sinon une erreur `SyntaxError` est générée.

```js
const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
const [first, , third, ...others] = planets;

console.log(first); // Sortie: Mercury
console.log(third); // Sortie: Earth
console.log(others); // Sortie: ["Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

```

Si l'opérateur () apparaît du côté droit dans la déstructuration, alors c'est une [**SYNTAXE DE PROPAGATION**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)**.** Il prend tous les autres éléments du tableau qui n'ont pas de variable mappée et les mappe à la variable rest.

```js
const otherPlanets = ["Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
const [first, second, ...rest] = ["Mercury", "Venus", ...otherPlanets];

console.log(first); // Sortie: Mercury
console.log(second); // Sortie: Venus
console.log(rest); // Sortie: ["Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
```

Lorsque vous avez plus de variables du côté gauche, il mappe les éléments individuels du tableau de manière égale aux variables.

```js
const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

const [first, second, ...rest] = ["Sun", ...planets];

console.log(first); // Sortie: Sun
console.log(second); // Sortie: Mercury
console.log(rest); // Sortie: ["Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

```

### **Échanger ou permuter des variables**

Une expression de déstructuration peut être utilisée pour permuter les valeurs de deux variables.

```js
let a, b;
[a, b] = ["Male", "Female"];
[a, b] = [b, a];

console.log(a); // Sortie: Female
console.log(b); // Sortie: Male

```

### **Déstructuration de tableau imbriqué**

Vous pouvez également faire de la déstructuration imbriquée avec des tableaux. L'élément correspondant doit être un tableau afin d'utiliser un littéral de tableau de déstructuration imbriqué pour assigner des éléments à des variables locales.

```js
const numbers = [8, [1, 2, 3], 10, 12];
const [a, [d, e, f]] = numbers;

console.log(a); // Sortie: 8
console.log(d); // Sortie: 1
console.log(e); // Sortie: 2

```

### Déstructuration multiple de tableau

Vous pouvez déstructurer un tableau plus d'une fois dans le même extrait de code.

```js
const places = ["first", "second", "third", "fourth"];
const [a, b, , d] = [f, ...rest] = places;

console.log(a); // Sortie: first
console.log(d); // Sortie: fourth
console.log(f); // Sortie: first
console.log(rest); // Sortie: ["second", "third", "fourth"]

```

### **Conclusion**

Vous pouvez copier et coller le code sur [le site de Babel](https://babeljs.io/en/repl.html#?babili=false&browsers=&build=&builtIns=false&spec=false&loose=false&code_lz=Q&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=es2015%2Ces2016%2Creact%2Cstage-2&prettier=false&targets=&version=6.26.0&envVersion=) pour voir à quoi ressemblerait le code si la déstructuration n'existait pas. Vous auriez écrit plus de lignes de code, mais la déstructuration simplifie tout.