---
title: 'Une introduction à la programmation orientée objet en JavaScript : objets,
  prototypes et classes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T16:31:35.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-object-oriented-programming-in-javascript-objects-prototypes-and-classes-5d135e7361b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zGuG4nFo8O4e0WMoNWVbMA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: object oriented
  slug: object-oriented
- name: General Programming
  slug: programming
- name: prototype
  slug: prototype
- name: 'tech '
  slug: tech
seo_title: 'Une introduction à la programmation orientée objet en JavaScript : objets,
  prototypes et classes'
seo_desc: 'By Andrea Koutifaris

  In many programming languages, classes are a well-defined concept. In JavaScript
  that is not the case. Or at least that wasn’t the case. If you search for O.O.P.
  and JavaScript you will run into many articles with a lot of differ...'
---

Par Andrea Koutifaris

Dans de nombreux langages de programmation, les classes sont un concept bien défini. En JavaScript, ce n'est pas le cas. Ou du moins, ce n'était pas le cas. Si vous recherchez P.O.O. et JavaScript, vous tomberez sur de nombreux articles avec différentes recettes sur la façon d'émuler une `class` en JavaScript.

Existe-t-il une manière simple, K.I.S.S., de définir une classe en JavaScript ? Et si oui, pourquoi tant de recettes différentes pour définir une classe ?

Avant de répondre à ces questions, comprenons mieux ce qu'est un `Object` JavaScript.

### **Objets en JavaScript**

Commençons par un exemple très simple :

```js
const a = {};
a.foo = 'bar';
```

Dans l'extrait de code ci-dessus, un objet est créé et enrichi avec une propriété `foo`. La possibilité d'ajouter des éléments à un objet existant est ce qui rend JavaScript différent des langages classiques comme Java.

Plus en détail, le fait qu'un objet puisse être enrichi permet de créer une instance d'une classe "implicite" sans avoir besoin de créer réellement la classe. Clarifions ce concept avec un exemple :

```js
function distance(p1, p2) {
  return Math.sqrt(
    (p1.x - p2.x) ** 2 + 
    (p1.y - p2.y) ** 2
  );
}

distance({x:1,y:1},{x:2,y:2});
```

Dans l'exemple ci-dessus, je n'ai pas eu besoin d'une classe Point pour créer un point, j'ai simplement étendu une instance de `Object` en ajoutant les propriétés `x` et `y`. La fonction distance ne se soucie pas de savoir si les arguments sont une instance de la classe `Point` ou non. Tant que vous appelez la fonction `distance` avec deux objets qui ont une propriété `x` et `y` de type `Number`, cela fonctionnera très bien. Ce concept est parfois appelé _duck typing_.

Jusqu'à présent, j'ai seulement utilisé un objet de données : un objet contenant uniquement des données et aucune fonction. Mais en JavaScript, il est possible d'ajouter des fonctions à un objet :

```js
const point1 = {
  x: 1,
  y: 1,
  toString() {
    return `(${this.x},${this.y})`;
  }
};

const point2 = {
  x: 2,
  y: 2,
  toString() {
    return `(${this.x},${this.y})`;
  }
};
```

Cette fois, les objets représentant un point 2D ont une méthode `toString()`. Dans l'exemple ci-dessus, le code `toString` a été dupliqué, et ce n'est pas bon.

Il existe de nombreuses façons d'éviter cette duplication, et en fait, dans différents articles sur les objets et les classes en JS, vous trouverez différentes solutions. Avez-vous déjà entendu parler du "Revealing module pattern" ? Il contient les mots "pattern" et "revealing", cela semble cool, et "module" est un must. Donc, cela doit être la bonne façon de créer des objets... sauf que ce n'est pas le cas. Le Revealing module pattern peut être le bon choix dans certains cas, mais ce n'est définitivement pas la manière par défaut de créer des objets avec des comportements.

Nous sommes maintenant prêts à introduire les classes.

### **Classes en JavaScript**

Qu'est-ce qu'une classe ? Selon un dictionnaire : une classe est "un ensemble ou une catégorie de choses ayant une propriété ou un attribut commun et différencié des autres par le genre, le type ou la qualité".

Dans les langages de programmation, nous disons souvent "Un objet est une instance d'une classe". Cela signifie que, en utilisant une classe, je peux créer de nombreux objets et ils partagent tous des méthodes et des propriétés.

Puisque les objets peuvent être enrichis, comme nous l'avons vu précédemment, il existe de nombreuses façons de créer des objets partageant des méthodes et des propriétés. Mais nous voulons la plus simple.

Heureusement, ECMAScript 6 fournit le mot-clé `class`, ce qui rend très facile la création d'une classe :

```js
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  toString() {
    return `(${this.x},${this.y})`;
  }
}
```

Donc, à mon avis, c'est la meilleure façon de déclarer des classes en JavaScript. Les classes sont souvent liées à l'héritage :

```js
class Point extends HasXY {
  constructor(x, y) {
    super(x, y);
  }

  toString() {
    return `(${this.x},${this.y})`;
  }
}
```

Comme vous pouvez le voir dans l'exemple ci-dessus, pour étendre une autre classe, il suffit d'utiliser le mot-clé `extends`.

Vous pouvez créer un objet à partir d'une classe en utilisant l'opérateur `new` :

```js
const p = new Point(1,1);
console.log(p instanceof Point); // affiche true
```

Une bonne manière orientée objet de définir des classes devrait fournir :

* une syntaxe simple pour déclarer une classe
* une manière simple d'accéder à l'instance actuelle, alias `this`
* une syntaxe simple pour étendre une classe
* une manière simple d'accéder à l'instance de la super classe, alias `super`
* éventuellement, une manière simple de dire si un objet est une instance d'une classe particulière. `obj instanceof AClass` devrait retourner `true` si cet objet est une instance de cette classe.

La nouvelle syntaxe `class` fournit tous les points ci-dessus.

Avant l'introduction du mot-clé `class`, quelle était la manière de définir une classe en JavaScript ?

De plus, qu'est-ce qu'une classe en JavaScript ? Pourquoi parlons-nous souvent de _prototypes_ ?

### **Classes en JavaScript 5**

De la [page Mozilla MDN sur les classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) :

> Les classes JavaScript, introduites dans ECMAScript 2015, sont principalement du sucre syntaxique sur l'héritage basé sur les **prototypes** existants de JavaScript. La syntaxe de classe n'introduit pas un nouveau modèle d'héritage orienté objet à JavaScript.

Le concept clé ici est l'**héritage basé sur les prototypes**. Puisqu'il y a beaucoup de malentendus sur ce qu'est ce type d'héritage, je vais procéder étape par étape, passant du mot-clé `class` au mot-clé `function`.

```js
class Shape {}
console.log(typeof Shape);
// affiche function
```

Il semble que `class` et `function` soient liés. Est-ce que `class` est juste un alias pour `function` ? Non, ce n'est pas le cas.

```js
Shape(2);
// Uncaught TypeError: Class constructor Shape cannot be invoked without 'new'
```

Donc, il semble que les personnes qui ont introduit le mot-clé `class` voulaient nous dire qu'une classe est une fonction qui doit être appelée en utilisant l'opérateur `new`.

```js
var Shape = function Shape() {} // Ou juste function Shape(){}
var aShape = new Shape();
console.log(aShape instanceof Shape);
// affiche true
```

L'exemple ci-dessus montre que nous pouvons utiliser `function` pour déclarer une classe. Nous ne pouvons cependant pas forcer l'utilisateur à appeler la fonction en utilisant l'opérateur `new`. Il est possible de lancer une exception si l'opérateur `new` n'a pas été utilisé pour appeler la fonction.

Quoi qu'il en soit, je vous suggère de ne pas mettre cette vérification dans chaque fonction qui agit comme une classe. Utilisez plutôt cette convention : toute fonction dont le nom commence par une majuscule est une classe et doit être appelée en utilisant l'opérateur `new`.

Continuons et découvrons ce qu'est un _prototype_ :

```js
class Shape {
  getName() {
    return 'Shape';
  }
}
console.log(Shape.prototype.getName);
// affiche function getName() ...
```

Chaque fois que vous déclarez une méthode à l'intérieur d'une classe, vous ajoutez en réalité cette méthode au prototype de la fonction correspondante. L'équivalent en JS 5 est :

```js
function Shape() {}
Shape.prototype.getName = function getName() {
  return 'Shape';
};
console.log(new Shape().getName()); // affiche Shape
```

Parfois, les fonctions de classe sont appelées _constructeurs_ car elles agissent comme des constructeurs dans une classe régulière.

Vous pouvez vous demander ce qui se passe si vous déclarez une méthode statique :

```js
class Point {
  static distance(p1, p2) {
    // ...
  }
}

console.log(Point.distance); // affiche function distance
console.log(Point.prototype.distance); // affiche undefined
```

Puisque les méthodes statiques sont en relation 1 à 1 avec les classes, la fonction statique est ajoutée à la fonction-constructeur, et non au prototype.

Récapitulons tous ces concepts dans un exemple simple :

```js
function Point(x, y) {
  this.x = x;
  this.y = y;
}

Point.prototype.toString = function toString() {
  return '(' + this.x + ',' + this.y + ')';
};
Point.distance = function distance() {
  // ...
}

console.log(new Point(1,2).toString()); // affiche (1,2)
console.log(new Point(1,2) instanceof Point); // affiche true
```

Jusqu'à présent, nous avons trouvé une manière simple de :

* déclarer une fonction qui agit comme une classe
* accéder à l'instance de la classe en utilisant le mot-clé `this`
* créer des objets qui sont réellement une instance de cette classe (`new Point(1,2) instanceof Point` retourne `true`)

Mais qu'en est-il de l'héritage ? Qu'en est-il de l'accès à la super classe ?

```js
class Hello {
  constructor(greeting) {
    this._greeting = greeting;
  }

  greeting() {
    return this._greeting;
  }
}

class World extends Hello {
  constructor() {
    super('hello');
  }

  worldGreeting() {
    return super.greeting() + ' world';
  }
}

console.log(new World().greeting()); // Affiche hello
console.log(new World().worldGreeting()); // Affiche hello world
```

Ci-dessus, un exemple simple d'héritage utilisant ECMAScript 6, ci-dessous le même exemple utilisant ce que l'on appelle l'**héritage par prototype** :

```js
function Hello(greeting) {
  this._greeting = greeting;
}

Hello.prototype.greeting = function () {
  return this._greeting;
};

function World() {
  Hello.call(this, 'hello');
}

// Copie le super prototype
World.prototype = Object.create(Hello.prototype);
// Fait en sorte que la propriété constructor référence la sous-classe
World.prototype.constructor = World;

World.prototype.worldGreeting = function () {
  const hello = Hello.prototype.greeting.call(this);
  return hello + ' world';
};

console.log(new World().greeting()); // Affiche hello
console.log(new World().worldGreeting()); // Affiche hello world
```

Cette manière de déclarer des classes est également suggérée dans l'exemple Mozilla MDN [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create#Examples).

En utilisant la syntaxe `class`, nous avons déduit que la création de classes implique de modifier le prototype d'une fonction. Mais pourquoi en est-il ainsi ? Pour répondre à cette question, nous devons comprendre ce que l'opérateur `new` fait réellement.

### Opérateur new en JavaScript

L'opérateur `new` est assez bien expliqué dans la page Mozilla MDN [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new). Mais je peux vous fournir un exemple relativement simple qui émule ce que fait l'opérateur `new` :

```js
function customNew(constructor, ...args) {
  const obj = Object.create(constructor.prototype);
  const result = constructor.call(obj, ...args);

  return result instanceof Object ? result : obj;
}

function Point() {}
console.log(customNew(Point) instanceof Point); // affiche true
```

Notez que l'algorithme réel `new` est plus complexe. Le but de l'exemple ci-dessus est juste d'expliquer ce qui se passe lorsque vous utilisez l'opérateur `new`.

Lorsque vous écrivez `new Point(1,2)`, ce qui se passe est :

* Le prototype `Point` est utilisé pour créer un objet.
* La fonction constructeur est appelée et l'objet nouvellement créé est passé comme contexte (alias `this`) avec les autres arguments.
* Si le constructeur retourne un Object, alors cet objet est le résultat du new, sinon l'objet créé à partir du prototype est le résultat.

Donc, que signifie **l'héritage par prototype** ? Cela signifie que vous pouvez créer des objets qui héritent de toutes les propriétés définies dans le prototype de la fonction qui a été appelée avec l'opérateur `new`.

Si vous y réfléchissez, dans un langage classique, le même processus se produit : lorsque vous créez une instance d'une classe, cette instance peut utiliser le mot-clé `this` pour accéder à toutes les fonctions et propriétés (publiques) définies dans la classe (et les ancêtres). À l'opposé des propriétés, toutes les instances d'une classe partageront probablement les mêmes références aux méthodes de la classe, car il n'est pas nécessaire de dupliquer le code binaire de la méthode.

### Programmation fonctionnelle

Parfois, les gens disent que JavaScript n'est pas bien adapté à la programmation orientée objet, et que vous devriez utiliser la programmation fonctionnelle à la place.

Bien que je ne sois pas d'accord avec le fait que JS ne soit pas adapté à la P.O.O., je pense que la programmation fonctionnelle est une très bonne façon de programmer. En JavaScript, les fonctions sont des [citoyens de première classe](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function) (par exemple, vous pouvez passer une fonction à une autre fonction) et il fournit des fonctionnalités comme `bind`, `call` ou `apply` qui sont des constructions de base utilisées en programmation fonctionnelle.

De plus, la programmation RX pourrait être considérée comme une évolution (ou une spécialisation) de la programmation fonctionnelle. Jetez un coup d'œil à [RxJs ici](https://rxjs-dev.firebaseapp.com/).

### Conclusion

Utilisez, lorsque cela est possible, la syntaxe `class` d'ECMAScript 6 :

```js
class Point {
  toString() {
    //...
  }
}
```

ou utilisez les prototypes de fonction pour définir des classes en ECMAScript 5 :

```js
function Point() {}
Point.prototype.toString = function toString() {
  // ...
}
```

J'espère que vous avez apprécié la lecture !