---
title: Le guide complet de 'this' en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T07:45:00.000Z'
originalURL: https://freecodecamp.org/news/the-complete-guide-to-this-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc9740569d1a4ca39a1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: Web Development
  slug: web-development
seo_title: Le guide complet de 'this' en JavaScript
seo_desc: "In JavaScript, every function has a this reference automatically created\
  \ when you declare it. \nJavaScript's this is quite similar to a this reference\
  \ in other class-based languages such as Java or C# (JavaScript is a prototype-based\
  \ language and no “..."
---

En JavaScript, chaque fonction a une référence `this` créée automatiquement lorsque vous la déclarez. 

Le `this` de JavaScript est assez similaire à une référence `this` dans d'autres langages basés sur les classes comme Java ou C# (JavaScript est un langage basé sur les prototypes et n'a pas de concept de "classe") : *Il pointe vers l'objet qui appelle la fonction* (cet objet est parfois appelé *contexte*). En JavaScript, cependant, *la référence `this` à l'intérieur des fonctions peut être liée à différents objets selon l'endroit où la fonction est appelée*. 

Voici 5 règles de base pour la liaison de `this` en JavaScript :

### **Règle 1**

Lorsque une fonction est appelée dans le scope global, la référence `this` est par défaut liée à l'**objet global** (`window` dans le navigateur, ou `global` dans Node.js). Par exemple :

```javascript
function foo() {
  this.a = 2;
}

foo();
console.log(a); // 2
```

Note : Si vous déclarez la fonction `foo()` ci-dessus en mode strict, puis vous appelez cette fonction dans le scope global, `this` sera `undefined` et l'assignation `this.a = 2` lèvera une exception `Uncaught TypeError`.

### **Règle 2**

Examinons l'exemple ci-dessous :

```javascript
function foo() {
  this.a = 2;
}

const obj = {
  foo: foo
};

obj.foo();
console.log(obj.a); // 2
```

Clairement, dans l'extrait ci-dessus, la fonction `foo()` est appelée avec le *contexte* de l'objet `obj` et la référence `this` est maintenant liée à `obj`. Donc, lorsqu'une fonction est appelée avec un objet de contexte, la référence `this` sera liée à cet objet.

### **Règle 3**

`.call`, `.apply` et `.bind` peuvent tous être utilisés au site d'appel pour lier explicitement `this`. L'utilisation de `.bind(this)` est quelque chose que vous pouvez voir dans beaucoup de composants React.

```javascript
const foo = function() {
  console.log(this.bar)
}

foo.call({ bar: 1 }) // 1
```

Voici un exemple rapide de la façon dont chacun est utilisé pour lier `this` :

* `.call()` : `fn.call(thisObj, fnParam1, fnParam2)`
* `.apply()` : `fn.apply(thisObj, [fnParam1, fnParam2])`
* `.bind()` : `const newFn = fn.bind(thisObj, fnParam1, fnParam2)`

### **Règle 4**

```javascript
function Point2D(x, y) {
  this.x = x;
  this.y = y;
}

const p1 = new Point2D(1, 2);
console.log(p1.x); // 1
console.log(p1.y); // 2
```

La chose à laquelle vous devez prêter attention est que la fonction `Point2D` est appelée avec le mot-clé `new`, et la référence `this` est liée à l'objet `p1`. Donc, lorsqu'une fonction est appelée avec le mot-clé `new`, elle créera un nouvel objet et la référence `this` sera liée à cet objet.

Note : Lorsque vous appelez une fonction avec le mot-clé `new`, on l'appelle aussi *fonction constructeur*.

### **Règle 5**

JavaScript détermine la valeur de `this` à l'exécution, en fonction du contexte actuel. Donc `this` peut parfois pointer vers autre chose que ce à quoi vous vous attendez.

Considérons cet exemple d'une classe Cat avec une méthode appelée `makeSound()`, suivant le modèle de la Règle 4 (ci-dessus) avec une fonction constructeur et le mot-clé `new`.

```javascript
const Cat = function(name, sound) {
  this.name = name;
  this.sound = sound;
  this.makeSound = function() {
    console.log( this.name + ' dit : ' + this.sound );
  };
}

const kitty = new Cat('Fat Daddy', 'Mrrooowww');
kitty.makeSound(); // Fat Daddy dit : Mrrooowww
```

Maintenant, essayons de donner au chat un moyen de `annoy()` les gens en répétant son son 100 fois, une fois toutes les demi-secondes.

```javascript
const Cat = function(name, sound) {
  this.name = name;
  this.sound = sound;
  this.makeSound = function() {
    console.log( this.name + ' dit : ' + this.sound );
  };
  this.annoy = function() {
    let count = 0, max = 100;
    const t = setInterval(function() {
      this.makeSound(); // <-- cette ligne échoue avec `this.makeSound n'est pas une fonction` 
      count++;
      if (count === max) {
        clearTimeout(t);
      }
    }, 500);
  };
}

const kitty = new Cat('Fat Daddy', 'Mrrooowww');
kitty.annoy();
```

Cela ne fonctionne pas car à l'intérieur du callback `setInterval`, nous avons créé un nouveau contexte avec un scope global, donc `this` ne pointe plus vers notre instance de kitty. Dans un navigateur web, `this` pointera plutôt vers l'objet Window, qui n'a pas de méthode `makeSound()`.

Plusieurs façons de faire en sorte que cela fonctionne :

1. Avant de créer le nouveau contexte, assigner `this` à une variable locale nommée `me`, ou `self`, ou ce que vous voulez l'appeler, et utiliser cette variable à l'intérieur du callback.

```javascript
const Cat = function(name, sound) {
  this.name = name;
  this.sound = sound;
  this.makeSound = function() {
    console.log( this.name + ' dit : ' + this.sound );
  };
  this.annoy = function() {
    let count = 0, max = 100;
    const self = this;
    const t = setInterval(function() {
      self.makeSound();
      count++;
      if (count === max) {
        clearTimeout(t);
      }
    }, 500);
  };
}

const kitty = new Cat('Fat Daddy', 'Mrrooowww');
kitty.annoy();
```

1. Avec ES6, vous pouvez éviter d'assigner `this` à une variable locale en utilisant une fonction fléchée, qui lie `this` au contexte du code environnant où elle est définie.

```javascript
const Cat = function(name, sound) {
  this.name = name;
  this.sound = sound;
  this.makeSound = function() {
    console.log( this.name + ' dit : ' + this.sound );
  };
  this.annoy = function() {
    let count = 0, max = 100;
    const t = setInterval(() => {
      this.makeSound();
      count++;
      if (count === max) {
        clearTimeout(t);
      }
    }, 500);
  };
}

const kitty = new Cat('Fat Daddy', 'Mrrooowww');
kitty.annoy();
```