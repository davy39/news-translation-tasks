---
title: JavaScript TypeOf – Comment vérifier le type d'une variable ou d'un objet en
  JS
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2020-11-09T22:07:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-typeof-how-to-check-the-type-of-a-variable-or-object-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/cover.png
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
seo_title: JavaScript TypeOf – Comment vérifier le type d'une variable ou d'un objet
  en JS
seo_desc: 'Data types and type checking are fundamental aspects of any programming
  language.

  Many programming languages like Java have strict type checking. This means that
  if a variable is defined with a specific type it can contain a value of only that
  type.

  ...'
---

Les types de données et la vérification de type sont des aspects fondamentaux de tout langage de programmation.

De nombreux langages de programmation comme Java ont une vérification de type stricte. Cela signifie que si une variable est définie avec un type spécifique, elle ne peut contenir qu'une valeur de ce type.

JavaScript, cependant, est un langage à typage faible (ou à typage dynamique). Cela signifie qu'une variable peut contenir une valeur de n'importe quel type. Le code JavaScript peut s'exécuter comme ceci :

```js
let one = 1;
one = 'one';
one = true;
one = Boolean(true);
one = String('It is possible');

```

Avec cela à l'esprit, il est crucial de connaître le type d'une variable à tout moment.

Le type d'une variable est déterminé par le type de la valeur qui lui est assignée. JavaScript a un opérateur spécial appelé `typeof` qui vous permet d'obtenir le type de n'importe quelle valeur.

Dans cet article, nous allons apprendre comment `typeof` est utilisé, ainsi que quelques pièges à surveiller.

# **Types de données JavaScript**

Jetons un rapide coup d'œil aux types de données JavaScript avant de nous pencher sur l'opérateur `typeof`.

En JavaScript, il existe sept types primitifs. Un primitif est tout ce qui n'est pas un objet. Ils sont :

1. String
2. Number
3. BigInt
4. Symbol
5. Boolean
6. undefined
7. null

Tout le reste est un `object` – y compris `array` et `function`. Un objet est une collection de paires clé-valeur.

# **L'opérateur JavaScript typeof**

L'opérateur `typeof` ne prend qu'un seul opérande (un opérateur unaire). Il évalue le type de l'opérande et retourne le résultat sous forme de chaîne. Voici comment l'utiliser lorsque vous évaluez le type d'un nombre, 007.

```js
typeof 007;  // retourne 'number'

```

Il existe une syntaxe alternative pour l'opérateur `typeof` où vous pouvez l'utiliser comme une `function` :

```js
typeof(operand)

```

Cette syntaxe est utile lorsque vous voulez évaluer une expression plutôt qu'une seule valeur. Voici un exemple de cela :

```js
typeof(typeof 007); // retourne 'string'

```

Dans l'exemple ci-dessus, l'expression `typeof 007` évalue le type number et retourne la chaîne 'number'. `typeof('number')` donne alors `'string'`.

Regardons un autre exemple pour comprendre l'importance des parenthèses avec l'opérateur `typeof`.

```js
typeof(999-3223); // retourne, "number"
```

Si vous omettez les parenthèses, cela retournera, `NaN` (Not a Number) :

```js
typeof 999-3223; // retourne, NaN
```

C'est parce que, d'abord `typeof 999` donnera une chaîne, "number". L'expression `"number" - 32223` donne NaN comme cela arrive lorsque vous effectuez une opération de soustraction entre une chaîne et un nombre.

### **Exemples de JavaScript typeof**

Le fragment de code suivant montre le résultat de la vérification de type de diverses valeurs en utilisant l'opérateur `typeof`.

```js
typeof 0;  //'number'
typeof +0;  //'number'
typeof -0;  //'number'
typeof Math.sqrt(2);  //'number'
typeof Infinity;  //'number'
typeof NaN;  //'number', même si ce n'est pas un nombre
typeof Number('100');  //'number', Après une conversion réussie en nombre
typeof Number('freeCodeCamp');  //'number', malgré le fait qu'il ne peut pas être converti en nombre

typeof true;  //'boolean'
typeof false;  //'boolean'
typeof Boolean(0);  //'boolean'

typeof 12n;  //'bigint'

typeof '';  //'string'
typeof 'freeCodeCamp';  //'string'
typeof `freeCodeCamp is awesome`;  //'string'
typeof '100';  //'string'
typeof String(100); //'string'

typeof Symbol();  //'symbol'
typeof Symbol('freeCodeCamp');  //'symbol'

typeof {blog: 'freeCodeCamp', author: 'Tapas A'};  //'object';
typeof ['This', 'is', 101]; //'object'
typeof new Date();  //'object'
typeof Array(4);  //'object'

typeof new Boolean(true);  //'object'; 
typeof new Number(101);  //'object'; 
typeof new String('freeCodeCamp');  //'object';
typeof new Object;  //'object'

typeof alert;  //'function'
typeof function () {}; //'function'
typeof (() => {});  //'function' - une fonction fléchée donc, les parenthèses sont requises
typeof Math.sqrt;  //'function'

let a;
typeof a;  //'undefined'
typeof b;  //'undefined'
typeof undefined;  //'undefined'

typeof null;  //'object'

```

Le tableau ci-dessous montre les valeurs de vérification de type de `typeof` :

<table style="box-sizing: inherit; margin: 0.5em 0px 2.5em; padding: 0px; border: 0px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-variant-numeric: inherit; font-variant-east-asian: inherit; font-weight: 400; font-stretch: inherit; line-height: inherit; font-family: -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 1.6rem; vertical-align: top; border-spacing: 0px; border-collapse: collapse; display: inline-block; overflow-x: auto; max-width: 100%; width: auto; white-space: nowrap; background: radial-gradient(at left center, rgba(0, 0, 0, 0.2) 0px, transparent 75%) 0px center / 10px 100% no-repeat scroll, radial-gradient(at right center, rgba(0, 0, 0, 0.2) 0px, transparent 75%) 100% center / 10px 100% scroll rgb(255, 255, 255); color: rgb(10, 10, 35); letter-spacing: normal; orphans: 2; text-align: start; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><thead style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><th style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: 700; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 1.2rem; vertical-align: baseline; color: var(--gray85); letter-spacing: 0.2px; text-align: left; text-transform: uppercase; background-color: var(--gray10);"><strong style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 12px; vertical-align: baseline; color: var(--gray85);">TYPE</strong></th><th style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: 700; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 1.2rem; vertical-align: baseline; color: var(--gray85); letter-spacing: 0.2px; text-align: center; text-transform: uppercase; background-color: var(--gray10);"><strong style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: bold; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 12px; vertical-align: baseline; color: var(--gray85);">VALEUR DE RETOUR DE TYPEOF</strong></th></tr></thead><tbody style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">String</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'string'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Number</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'number'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">BigInt</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'bigint'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Symbol</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'symbol'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Boolean</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'boolean'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">undefined</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'undefined'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Function object</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'function'</code></td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">null</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'object'</code>(voir ci-dessous!)</td></tr><tr style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline;"><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(90deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-size: 20px 100%; background-repeat: no-repeat;">Any other objects</td><td style="box-sizing: inherit; margin: 0px; padding: 6px 12px; border: 1px solid var(--gray10); font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 16px; vertical-align: baseline; background-image: linear-gradient(270deg, rgb(255, 255, 255) 50%, rgba(255, 255, 255, 0)); background-position: 100% 0px; background-size: 20px 100%; background-repeat: no-repeat; text-align: center;"><code style="box-sizing: inherit; margin: 0px; padding: 0px 5px 2px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: 400 !important; font-stretch: inherit; line-height: 1em; font-family: &quot;Roboto Mono&quot;, monospace; font-size: 0.8em; vertical-align: baseline; background: var(--gray15);">'object'</code></td></tr></tbody></table>

# **Pièges courants avec `typeof`**

Il existe des cas où l'opérateur `typeof` peut ne pas retourner les types auxquels vous vous attendez. Cela peut causer de la confusion et des erreurs. Voici quelques cas.

### **Le type de NaN est un nombre**

```js
typeof NaN;  //'number', même si ce n'est pas un nombre
```

Le `typeof NaN` est `'number'`. C'est étrange, car nous ne devrions pas détecter un `NaN` en utilisant `typeof`. Il existe de meilleures façons de le gérer. Nous les verrons dans un instant.

### **Le type de `null` est l'objet**

```js
  typeof null;  //'object'

```

En JavaScript, `typeof null` est un objet ce qui donne une fausse impression que, `null` est un objet alors qu'il s'agit d'une valeur primitive.

Ce résultat de `typeof null` est en fait un bug dans le langage. Une tentative a été faite pour le corriger dans le passé mais elle a été rejetée en raison du problème de compatibilité ascendante.

### **Le type d'une variable non déclarée est undefined**

Avant ES6, une vérification de type sur une variable non déclarée résultait en `'undefined'`. Mais ce n'est pas une manière sûre de gérer cela.

Avec ES6, nous pouvons déclarer des variables à portée de bloc avec les mots-clés `let` ou `const`. Si vous les utilisez avec l'opérateur `typeof` avant qu'elles ne soient initialisées, elles lanceront une `ReferenceError`.

```js
 typeof cat; // ReferenceError
 let cat = 'brownie'; 
```

### **Le type d'une fonction constructeur est un objet**

Toutes les fonctions constructeur, à l'exception du constructeur `Function`, seront toujours de type 'object'.

```js
typeof new String('freeCodeCamp'); //'object'
```

Cela peut prêter à confusion, car nous nous attendons à ce que ce soit le type réel (dans l'exemple ci-dessus, un type `string`).

### **Le type d'un Array est un objet**

Bien que techniquement correct, cela pourrait être le plus décevant. Nous voulons différencier un Array et un Object même si un Array est techniquement un Object en JavaScript.

```js
typeof Array(4);  //'object'
```

Heureusement, il existe des moyens de détecter correctement un Array. Nous verrons cela bientôt.

# **Au-delà de `typeof` – Meilleure vérification de type**

Maintenant que nous avons vu certaines des limitations de l'opérateur `typeof`, voyons comment les corriger et faire une meilleure vérification de type.

### **Comment détecter NaN**

En JavaScript, NaN est une valeur spéciale. La valeur NaN représente le résultat d'une expression arithmétique qui ne peut pas être représentée. Par exemple,

```js
let result = 0/0;
console.log(result);  // retourne, NaN

```

De plus, si nous effectuons des opérations arithmétiques avec `NaN`, cela donnera toujours un `NaN`.

```js
console.log(NaN + 3); // retourne, NaN

```

La vérification de type sur NaN en utilisant l'opérateur `typeof` n'aide pas beaucoup car il retourne le type comme un `'number'`. JavaScript a une fonction globale appelée `isNaN()` pour détecter si un résultat est NaN.

```js
isNaN(0/0); // retourne, true

```

Mais il y a un problème ici aussi.

```js
isNaN(undefined); // retourne true pour 'undefined'

```

Dans ES6, la méthode `isNaN()` est ajoutée à l'objet global `Number`. Cette méthode est beaucoup plus fiable et donc c'est celle qui est préférée.

```js
Number.isNaN(0/0); // retourne, true
Number.isNaN(undefined); // retourne, false

```

Un autre aspect intéressant de `NaN` est qu'il est la seule valeur JavaScript qui n'est jamais égale à aucune autre valeur y compris elle-même. Donc voici une autre façon de détecter NaN pour les environnements où ES6 n'est pas supporté :

```js
function isNaN (input) {
  return input !== input;
}

```

### **Comment détecter null en JavaScript**

Nous avons vu que la détection de null en utilisant l'opérateur `typeof` est confuse. La manière préférée de vérifier si quelque chose est null est d'utiliser l'opérateur d'égalité stricte (`===`).

```js
function isNull(input) {
 return input === null;
}

```

Assurez-vous de ne pas utiliser `==` par erreur. Utiliser `==` à la place de `===` entraînera une détection de type trompeuse.

### **Comment détecter un Array en JavaScript**

À partir de ES6, nous pouvons détecter un array en utilisant la méthode `Array.isArray` :

```js
Array.isArray([]); // retourne true
Array.isArray({}); // retourne false

```

Avant ES6, nous pouvions utiliser l'opérateur `instanceof` pour déterminer un Array :

```js
function isArray(input) {
  return input instanceof Array;
}

```

# **Une solution générique pour la vérification de type en JavaScript**

Il existe un moyen de créer une solution générique pour la vérification de type. Jetez un œil à la méthode, `Object.prototype.toString`. Celle-ci est très puissante et extrêmement utile pour écrire une méthode utilitaire pour la vérification de type.

Lorsque `Object.prototype.toString` est invoqué en utilisant `call()` ou `apply()`, il retourne le type d'objet au format : `[object Type]`. La partie `Type` dans la valeur de retour est le type réel.

Voyons comment cela fonctionne avec quelques exemples :

```js
// retourne '[object Array]'
Object.prototype.toString.call([]); 

// retourne '[object Date]'
Object.prototype.toString.call(new Date()); 

// retourne '[object String]'
Object.prototype.toString.call(new String('freeCodeCamp'));

// retourne '[object Boolean]'
Object.prototype.toString.call(new Boolean(true));

// retourne '[object Null]'
Object.prototype.toString.call(null);

```

Donc, cela signifie que si nous prenons simplement la chaîne de retour et extrayons la partie `Type`, nous aurons le type réel. Voici une tentative de le faire :

```js
function typeCheck(value) {
  const return_value = Object.prototype.toString.call(value);
  // nous pouvons aussi utiliser regex pour faire cela...
  const type = return_value.substring(
           return_value.indexOf(" ") + 1, 
           return_value.indexOf("]"));

  return type.toLowerCase();
}

```

Maintenant, nous pouvons utiliser la fonction `typeCheck` pour détecter les types :

```js
typeCheck([]); // 'array'
typeCheck(new Date()); // 'date'
typeCheck(new String('freeCodeCamp')); // 'string'
typeCheck(new Boolean(true)); // 'boolean'
typeCheck(null); // 'null'

```

# **En résumé**

Pour résumer ce que nous avons appris dans cet article :

* La vérification de type JavaScript n'est pas aussi stricte que dans d'autres langages de programmation.
* Utilisez l'opérateur `typeof` pour détecter les types.
* Il existe deux variantes de la syntaxe de l'opérateur `typeof` : `typeof` et `typeof(expression)`.
* Le résultat d'un opérateur `typeof` peut être trompeur à certains moments. Nous devons nous fier à d'autres méthodes disponibles (`Number.isNaN`, `Array.isArry`, etc.) dans ces cas.
* Nous pouvons utiliser `Object.prototype.toString` pour créer une méthode de détection de type générique.

# **Avant de terminer...**

Merci d'avoir lu jusqu'ici ! Restons en contact. Vous pouvez me mentionner sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary) avec des commentaires.

Vous pourriez aussi aimer ces autres articles :

* [JavaScript undefined et null : Parlons-en une dernière fois !](https://blog.greenroots.info/javascript-undefined-and-null-lets-talk-about-it-one-last-time-ckh64kmz807v848s15kdkg3dd)
* [JavaScript : Comparaison d'égalité avec ==, === et Object.is](https://blog.greenroots.info/javascript-equality-comparison-with-and-objectis-ckdpt2ryk01vel9s186ft8cwl)
* [Le mot-clé `this` de JavaScript + 5 règles de liaison clés expliquées pour les débutants en JS](https://www.freecodecamp.org/news/javascript-this-keyword-binding-rules/)

C'est tout pour l'instant. À bientôt avec mon prochain article. En attendant, prenez bien soin de vous.