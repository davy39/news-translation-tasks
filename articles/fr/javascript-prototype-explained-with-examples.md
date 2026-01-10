---
title: Explication du Prototype JavaScript avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T23:01:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-prototype-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d53740569d1a4ca3726.jpg
tags:
- name: JavaScript
  slug: javascript
- name: prototype
  slug: prototype
- name: toothbrush
  slug: toothbrush
seo_title: Explication du Prototype JavaScript avec des Exemples
seo_desc: 'Prototypes

  JavaScript is a prototype-based language, therefore understanding the prototype
  object is one of the most important concepts which JavaScript practitioners need
  to know. This article will give you a short overview of the Prototype object t...'
---

## **Prototypes**

JavaScript est un langage basé sur les prototypes, donc comprendre l'objet prototype est l'un des concepts les plus importants que les praticiens de JavaScript doivent connaître. Cet article vous donnera un bref aperçu de l'objet Prototype à travers divers exemples. Avant de lire cet article, vous devrez avoir une compréhension de base de la [référence `this` en JavaScript](https://guide.freecodecamp.org/src/pages/javascript/this-reference/index.md).

### **Objet Prototype**

Pour plus de clarté, examinons l'exemple suivant :

```javascript
function Point2D(x, y) {
  this.x = x;
  this.y = y;
}
```

Lorsque la fonction `Point2D` est déclarée, une propriété par défaut nommée `prototype` sera créée pour elle (notez que, en JavaScript, une fonction est aussi un objet). La propriété `prototype` est un objet qui contient une propriété `constructor` et sa valeur est la fonction `Point2D` : `Point2D.prototype.constructor = Point2D`. Et lorsque vous appelez `Point2D` avec le mot-clé `new`, les objets nouvellement créés hériteront de toutes les propriétés de `Point2D.prototype`. Pour vérifier cela, vous pouvez ajouter une méthode nommée `move` dans `Point2D.prototype` comme suit :

```javascript
Point2D.prototype.move = function(dx, dy) {
  this.x += dx;
  this.y += dy;
}

var p1 = new Point2D(1, 2);
p1.move(3, 4);
console.log(p1.x); // 4
console.log(p1.y); // 6
```

Le `Point2D.prototype` est appelé **objet prototype** ou **prototype** de l'objet `p1` et pour tout autre objet créé avec la syntaxe `new Point2D(...)`. Vous pouvez ajouter plus de propriétés à l'objet `Point2D.prototype` comme vous le souhaitez. Le modèle courant est de déclarer des méthodes à `Point2D.prototype` et les autres propriétés seront déclarées dans la fonction constructeur.

Les objets intégrés en JavaScript sont construits de manière similaire. Par exemple :

* Le prototype des objets créés avec `new Object()` ou la syntaxe `{}` est `Object.prototype`.
* Le prototype des tableaux créés avec `new Array()` ou la syntaxe `[]` est `Array.prototype`.
* Et ainsi de suite avec d'autres objets intégrés tels que `Date` et `RegExp`.

`Object.prototype` est hérité par tous les objets et il n'a pas de prototype (son prototype est `null`).

### **Chaîne de prototypes**

Le mécanisme de la chaîne de prototypes est simple : lorsque vous accédez à une propriété `p` sur l'objet `obj`, le moteur JavaScript recherchera cette propriété à l'intérieur de l'objet `obj`. Si le moteur ne parvient pas à trouver la propriété, il continue la recherche dans le prototype de l'objet `obj` et ainsi de suite jusqu'à atteindre `Object.prototype`. Si, après la recherche, rien n'a été trouvé, le résultat sera `undefined`. Par exemple :

```javascript
var obj1 = {
  a: 1,
  b: 2
};

var obj2 = Object.create(obj1);
obj2.a = 2;

console.log(obj2.a); // 2
console.log(obj2.b); // 2
console.log(obj2.c); // undefined
```

Dans l'extrait ci-dessus, l'instruction `var obj2 = Object.create(obj1)` créera l'objet `obj2` avec le prototype `obj1`. En d'autres termes, `obj1` devient le prototype de `obj2` au lieu de `Object.prototype` par défaut. Comme vous pouvez le voir, `b` n'est pas une propriété de `obj2`, mais vous pouvez toujours y accéder via la chaîne de prototypes. Pour la propriété `c`, cependant, vous obtenez la valeur `undefined` car elle ne peut pas être trouvée dans `obj1` et `Object.prototype`.

### **Classes**

En ES2016, nous pouvons maintenant utiliser le mot-clé `Class` ainsi que les méthodes mentionnées ci-dessus pour manipuler le `prototype`. La `Class` JavaScript plaît aux développeurs issus de l'OOP, mais elle fait essentiellement la même chose que ci-dessus.

```javascript
class Rectangle {
  constructor(height, width) {
    this.height = height
    this.width = width
  }

  get area() {
    return this.calcArea()
  }

  calcArea() {
    return this.height * this.width
  }
}

const square = new Rectangle(10, 10)

console.log(square.area) // 100
```

Cela revient essentiellement à :

```javascript
function Rectangle(height, width) {
  this.height = height
  this.width = width
}

Rectangle.prototype.calcArea = function calcArea() {
  return this.height * this.width
}
```

Les méthodes `getter` et `setter` dans les classes lient une propriété d'objet à une fonction qui sera appelée lorsque cette propriété est recherchée. Ce n'est que du sucre syntaxique pour faciliter la recherche ou la définition de propriétés.

## Plus d'informations sur les prototypes JS :

* [Tout ce que vous devez savoir pour comprendre le prototype de JavaScript](https://www.freecodecamp.org/news/all-you-need-to-know-to-understand-javascripts-prototype-a2bff2d28f03/)