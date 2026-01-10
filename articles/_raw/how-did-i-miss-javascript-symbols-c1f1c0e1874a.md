---
title: A quick overview of JavaScript symbols
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-13T08:35:24.000Z'
originalURL: https://freecodecamp.org/news/how-did-i-miss-javascript-symbols-c1f1c0e1874a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3AzH-G1JpbL4UhzH5TXS5w.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Vali Shah

  Symbols

  Symbols are new primitive type introduced in ES6. Symbols are completely unique
  identifiers. Just like their primitive counterparts (Number, String, Boolean), they
  can be created using the factory function Symbol() which returns ...'
---

By Vali Shah

#### Symbols

Symbols are new [**primitive**](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) type introduced in ES6. Symbols are completely unique identifiers. Just like their primitive counterparts (**Number**, **String**, **Boolean**), they can be created using the factory function `Symbol()` which returns a Symbol.

```js
const symbol = Symbol('description')
```

Every time you call the factory function, a new and unique symbol is created. The optional string-valued parameter is a descriptive string that is shown when printing the symbol.

```js
> symbol
Symbol(description)
```

Every symbol returned by `Symbol()` is unique, so every symbol has its own identity:

```js
> Symbol() === Symbol()
false
```

You can see that symbols are primitive if you apply the `typeof` operator to one of them — it will return a new symbol-specific result:

```js
> typeof symbol
'symbol'
```

#### **Use Case: Symbols as keys of non-public properties**

Whenever there are inheritance hierarchies in JavaScript, you have two kinds of properties (e.g. created via classes, a purely prototypal approach):

* **Public** properties are seen by clients of the code
* **Private** properties are used internally within the pieces that make up the inheritance hierarchy (e.g. classes, objects).

For usability's sake, public properties usually have string keys. But for private properties with string keys, accidental name clashes can become a problem. Therefore, symbols are a good choice.

For example, in the following code, symbols are used for private properties `_counter` and `_action`:

```js
const _counter = Symbol('counter');
const _action  = Symbol('action');
class Countdown {
    constructor(counter, action) {
        this[_counter] = counter;
        this[_action] = action;
    }
    dec() {
        let counter = this[_counter];
        if (counter < 1) return;
        counter--;
        this[_counter] = counter;
        if (counter === 0) {
            this[_action]();
        }
    }
}
```

Note that symbols only protect you from name clashes, not from unauthorized access. You can find out all an object’s property keys — including symbols — via the following:

```js
const obj = {
  [Symbol('my_key')]  : 1, 
   enum               : 2, 
   nonEnum            : 3
};

Object.defineProperty(obj, 'nonEnum', { enumerable: false }); // Making 'nonEnum' as not enumerable.

// Ignores symbol-valued property keys:
> Object.getOwnPropertyNames(obj)
['enum', 'nonEnum']

// Ignores string-valued property keys:
> Object.getOwnPropertySymbols(obj)
[Symbol(my_key)]

// Considers all kinds of keys:
> Reflect.ownKeys(obj)
[Symbol(my_key),'enum', 'nonEnum']

// Only considers enumerable property keys that are strings:
> Object.keys(obj)
['enum']
```

#### Do we really need symbols?

Use symbols when your requirement is one of these:

* **Enum:** To allow you to define constants with semantic names and unique values.

```js
const directions = {
  UP   : Symbol( ‘UP’ ),
  DOWN : Symbol( ‘DOWN’ ),
  LEFT : Symbol( ‘LEFT’ ),
  RIGHT: Symbol( ‘RIGHT’ )
};
```

* **Name Clashes:** when you wanted to prevent collisions with keys in objects
* **Privacy:** when you don’t want your object properties to be enumerable
* **Protocols:** To define how an object can be iterated.   
 Imagine, for instance, a library like `dragula` defining a protocol through `Symbol.for(dragula.moves)` . You can add a method on that `Symbol` to any DOM element. If a DOM element follows the protocol, then `dragula` could call the `el[Symbol.for('dragula.moves')]()` user-defined method to assert whether the element can be moved.
* **Well-known Symbols:** In addition to user-defined symbols, JavaScript has some built-in symbols. These represent internal language behaviors which were not exposed to developers in < ES5. More information [**here**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#Well-known_symbols)**.**

#### **Conclusion**

`Symbols` in JavaScript can provide access level uniqueness to objects. It's worthwhile for all developer to have a basic understanding of them and their various use-cases.

`code = **co**ffee + **de**veloper`

