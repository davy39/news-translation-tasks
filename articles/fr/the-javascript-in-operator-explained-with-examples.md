---
title: L'opérateur JavaScript `in` expliqué avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-13T07:34:34.000Z'
originalURL: https://freecodecamp.org/news/the-javascript-in-operator-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/javascript-in-operator.png
tags:
- name: JavaScript
  slug: javascript
seo_title: L'opérateur JavaScript `in` expliqué avec des exemples
seo_desc: "By Linda Ikechukwu\nOne of the first topics you’ll come across when learning\
  \ JavaScript (or any other programming language) are operators. \nThe most common\
  \ operators are the arithmetic, logical, and comparison operators. But did you know\
  \ that JavaScri..."
---

Par Linda Ikechukwu

L'un des premiers sujets que vous rencontrerez lors de l'apprentissage de JavaScript (ou de tout autre langage de programmation) sont les opérateurs. 

Les opérateurs les plus courants sont les opérateurs arithmétiques, logiques et de comparaison. Mais saviez-vous que JavaScript dispose d'un opérateur `in` ?

Si ce n'est pas le cas, ne vous inquiétez pas. Je viens de le découvrir récemment en cherchant une solution à un problème sur Google. 

Dans cet article, vous apprendrez exactement ce que fait l'opérateur JavaScript `in`, quand l'utiliser et comment l'utiliser.

## Qu'est-ce que l'opérateur JavaScript in ?

L'opérateur JavaScript `in` est utilisé pour vérifier si une propriété spécifiée existe dans un objet ou dans ses propriétés héritées (en d'autres termes, sa chaîne de prototypes). L'opérateur `in` retourne `true` si la propriété spécifiée existe.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/const-linda-----name_--Linda---job_--frontend-developer---.png)
_Anatomie d'un objet JavaScript simple._

La chaîne de prototypes JavaScript est la manière dont les objets ou les instances d'objets ont accès à des propriétés et méthodes qui ne leur appartenaient pas à l'origine. Ces objets héritent des propriétés et méthodes définies dans leurs constructeurs ou prototypes, auxquels on peut accéder via leur propriété `__proto__`.

Cet article suppose que vous avez une compréhension de base de ce que sont les objets, comment les créer, à quoi ils servent et comment fonctionne l'héritage en JavaScript. Si ce n'est pas le cas, [cet article sur MDN](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes#:~:text=Jump%20to%20section,add%20methods%20to%20existing%20constructors.) devrait vous aider.

## Quand utiliser l'opérateur JavaScript in

### Pour vérifier si une propriété existe sur un objet

```js
const car = {
  make: 'Toyota',
  model:'Camry',
  year: '2018',
  start: function() {
    console.log(`Starting ${this.make} ${this.model}, ${this.year}`);
  }
}

'make' in car // Retourne true.
'start' in car // Retourne true.
'Toyota' in car // Retourne false. 'Toyota' n'est pas un nom de propriété, mais une valeur.
```

### Pour vérifier si une propriété est héritée par un objet.

Utilisons la syntaxe de classe ES6 pour créer un constructeur d'objet. Cela s'applique également aux constructeurs de fonctions :

```js
class Car {
  constructor(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }
  start() {
    console.log(`Starting ${this.make} ${this.model}, ${this.year}`);
  }
}

const toyota = new Car('Toyota', 'Camry', '2018');

'start' in toyota;
/* Retourne true car toyota est une instance du constructeur d'objet Car. L'objet toyota hérite donc de toutes les propriétés du constructeur Car. */

'toString' in toyota;
/* Retourne true. toString est une méthode propriété du type Object, dont le constructeur Car est une instance. */
```

### Pour vérifier si un index/clé existe dans un tableau.

Vous vous demandez peut-être, puisque nous avons établi que l'opérateur JavaScript `in` peut être utilisé avec des objets, pourquoi pouvons-nous également l'utiliser avec des tableaux ?

Eh bien, un tableau est en fait un prototype (instance) du type `Object`. En fait, tout en JavaScript est une instance du type `Object`.

Cela peut sembler fou, mais exécutons un simple programme dans la console du navigateur pour confirmer.

Tout d'abord, définissez un tableau et confirmez s'il s'agit d'une instance du type `Object` en utilisant l'opérateur `instanceof` :

```js
const number = [2, 3, 4, 5];

number instanceof Object // Retourne true

```

Toujours sceptique ? Tapez `number` dans la console et appuyez sur entrée, puis ouvrez le résultat. 

Vous remarquerez une liste de propriétés, dont `__proto__` qui pointe vers `Array`. En ouvrant cela également et en descendant dans la liste, nous arrivons à une autre propriété `__proto__` avec une valeur de `Object`.

Cela montre que le tableau `number` est une instance du type `Array` qui est une instance du type `Object`.

Maintenant, revenons à l'utilisation de l'opérateur `in` :

```js
const number = [2, 3, 4, 5];

3 in number // Retourne true.
2 in number // Retourne true.

5 in number // Retourne false car 5 n'est pas un index existant dans le tableau mais une valeur ;

'filter' in number
/* Retourne true car filter est une méthode propriété sur le type Array dont le tableau number est une instance. Le tableau number hérite de la propriété filter.*/
```

### Pour vérifier si une propriété existe sur un élément Html

Dans l'article de Kirupa, [Check If You Are On a Touch Enabled Device](https://www.kirupa.com/html5/check_if_you_are_on_a_touch_enabled_device.htm), il met en évidence cette fonction :

```js
function isTouchSupported() {
  var msTouchEnabled = window.navigator.msMaxTouchPoints;
  var generalTouchEnabled = "ontouchstart" in document.createElement("div");

  if (msTouchEnabled || generalTouchEnabled) {
    return true;
  }
  return false;
}

```

Cette fonction retourne `true` si vous êtes sur un appareil qui supporte le tactile et retourne `false` si vous êtes sur un appareil qui ne supporte pas le tactile en vérifiant si les propriétés `window.navigator.msMaxTouchPoints` et `ontouchstart` sont présentes. Ces propriétés n'existent que sur les appareils qui sont tactiles. 

Assez simple ! 

Concentrons-nous sur la ligne mise en évidence. Rappelez-vous comment nous avons établi que l'opérateur `in` retourne `true` si la propriété spécifiée existe dans un objet ? Les éléments HTML utilisés en JavaScript deviennent en fait des instances du type `Object`, d'où le nom "Document Object Model" ou DOM.

Bien sûr, vous ne me croyez peut-être pas sans une sorte de preuve. Comme avant, tapons quelques commandes dans la console.

Créez un élément `div` et listez ses propriétés en utilisant `console.dir()` :

```js
const element = document.createElement('div');

console.dir(element);

```

Vous verrez alors l'élément `div` avec ses propriétés listées dans la console.

Ouvrez le menu déroulant et vous remarquerez qu'il a une propriété `__proto__` de `HtmlDivElement`. Ouvrez cela et vous trouverez une autre propriété `__proto__` de `HtmlElement`, puis `Element`, `Node`, `Eventtarget`, et enfin `Object`.

Exécutez également :

```js
element instanceof Object
```

Cela retournera `true`, montrant que l'élément `div` est une instance du type `Object`, ce qui explique pourquoi l'opérateur `in` peut être utilisé sur lui.

## Conclusion

Vous avez appris à connaître l'opérateur JavaScript `in`, peu populaire, qui est utilisé pour vérifier la présence de propriétés sur un objet ou des instances de type `Object`. Cela devrait être utile lors de l'écriture de logiques de vérification.

Si vous avez aimé cet article, vous aimerez définitivement d'autres articles sur mon blog [codewithlinda.com](https://www.codewithlinda.com/blog). J'y publie des articles adaptés aux débutants sur le développement frontend sans jargon technique (autant que possible) ?.