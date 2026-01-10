---
title: JavaScript Create Object  –  How to Define Objects in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T15:06:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-create-object-how-to-define-objects-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/IMG_7192.JPG
tags:
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: 'By Cristian Salcescu

  Objects are the main unit of encapsulation in Object-Oriented Programming. In this
  article, I will describe several ways to build objects in JavaScript. They are:


  Object literal

  Object.create()

  Classes

  Factory functions


  Object ...'
---

By Cristian Salcescu

Objects are the main unit of encapsulation in Object-Oriented Programming. In this article, I will describe several ways to build objects in JavaScript. They are:

* Object literal
* Object.create()
* Classes
* Factory functions

## Object Literal

First, we need to make a distinction between data structures and object-oriented objects. Data structures have public data and no behavior. That means they have no methods.

We can easily create such objects using the object literal syntax. It looks like this:

```
const product = {
  name: 'apple',
  category: 'fruits',
  price: 1.99
}
  
console.log(product);
```

Objects in JavaScript are dynamic collections of key-value pairs. The key is always a string and has to be unique in the collection. The value can a primitive, an object, or even a function.

We can access a property using the dot or the square notation.

```
console.log(product.name);
//"apple"

console.log(product["name"]);
//"apple"
```

Here is an example where the value is another object.

```
const product = {
  name: 'apple',
  category: 'fruits',
  price: 1.99,
  nutrients : {
   carbs: 0.95,
   fats: 0.3,
   protein: 0.2
 }
}
```

The value of the `carbs` property is a new object. Here is how we can access the `carbs` property.

```
console.log(product.nutrients.carbs);
//0.95
```

### Shorthand Property Names

Consider the case where we have the values of our properties stored in variables.

```
const name = 'apple';
const category = 'fruits';
const price = 1.99;
const product = {
  name: name,
  category: category,
  price: price
}
```

JavaScript supports what is called the shorthand property names. It allows us to create an object using just the name of the variable. It will create a property with the same name. The next object literal is equivalent to the previous one.

```
const name = 'apple';
const category = 'fruits';
const price = 1.99;
const product = {
  name,
  category,
  price
}
```

## Object.create

Next, let's look at how to implement objects with behavior, object-oriented objects.

JavaScript has what is called the prototype system that allows sharing behavior between objects. The main idea is to create an object called the prototype with a common behavior and then use it when creating new objects.

The prototype system allows us to create objects that inherit behavior from other objects.

Let’s create a prototype object that allows us to add products and get the total price from a shopping cart.

```
const cartPrototype = {
  addProduct: function(product){
    if(!this.products){
     this.products = [product]
    } else {
     this.products.push(product);
    }
  },
  getTotalPrice: function(){
    return this.products.reduce((total, p) => total + p.price, 0);
  }
}
```

Notice that this time the value of the property  `addProduct` is a function. We can also write the previous object using a shorter form called the shorthand method syntax.

```
const cartPrototype = {
  addProduct(product){/*code*/},
  getTotalPrice(){/*code*/}
}
```

The `cartPrototype` is the prototype object that keeps the common behavior represented by two methods, `addProduct` and `getTotalPrice`. It can be used to build other objects inheriting this behavior.

```
const cart = Object.create(cartPrototype);
cart.addProduct({name: 'orange', price: 1.25});
cart.addProduct({name: 'lemon', price: 1.75});

console.log(cart.getTotalPrice());
//3
```

The `cart` object has `cartPrototype` as its prototype. It inherits the behavior from it. `cart` has a hidden property that points to the prototype object.

When we use a method on an object, that method is first searched on the object itself rather than on its prototype.

### this

Note that we are using a special keyword called `this` to access and modify the data on the object.

Remember that functions are independent units of behavior in JavaScript. They are not necessarily part of an object. When they are, we need to have a reference that allows the function to access other members on the same object. `this` is the function context. It gives access to other properties.

### Data

You may wonder why we haven’t defined and initialized the `products` property on the prototype object itself.

We shouldn't do that. Prototypes should be used to share behavior, not data. Sharing data will lead to having the same products on several cart objects. Consider the code below:

```
const cartPrototype = {
  products:[],
  addProduct: function(product){
      this.products.push(product);
  },
  getTotalPrice: function(){}
}

const cart1 = Object.create(cartPrototype);
cart1.addProduct({name: 'orange', price: 1.25});
cart1.addProduct({name: 'lemon', price: 1.75});
console.log(cart1.getTotalPrice());
//3

const cart2 = Object.create(cartPrototype);
console.log(cart2.getTotalPrice());
//3
```

Both the `cart1` and `cart2` objects inheriting the common behavior from the `cartPrototype` also share the same data. We don’t want that. Prototypes should be used to share behavior, not data.

## Class

The prototype system is not a common way of building objects. Developers are more familiar with building objects out of classes.

The class syntax allows a more familiar way of creating objects sharing a common behavior. It still creates the same prototype behind the scene but the syntax is clearer and we also avoid the previous data-related issue. The class offers a specific place to define the data distinct for each object.

Here is the same object created using the class sugar syntax:

```
class Cart{
  constructor(){
    this.products = [];
  }
  
  addProduct(product){
      this.products.push(product);
  }
  
  getTotalPrice(){
    return this.products.reduce((total, p) => total + p.price, 0);
  }
}

const cart = new Cart();
cart.addProduct({name: 'orange', price: 1.25});
cart.addProduct({name: 'lemon', price: 1.75});
console.log(cart.getTotalPrice());
//3

const cart2 = new Cart();
console.log(cart2.getTotalPrice());
//0
```

Notice that the class has a constructor method that initialized that data distinct for each new object. The data in the constructor is not shared between instances. In order to create a new instance, we use the `new` keyword.

I think the class syntax is more clear and familiar to most developers. Nevertheless, it does a similar thing, it creates a prototype with all the methods and uses it to define new objects. The prototype can be accessed with `Cart.prototype`.

It turns out that the prototype system is flexible enough to allow the class syntax. So the class system can be simulated using the prototype system.

### Private Properties

The only thing is that the `products` property on the new object is public by default.

```
console.log(cart.products);
//[{name: "orange", price: 1.25}
// {name: "lemon", price: 1.75}]
```

We can make it private using the hash `#` prefix.

Private properties are declared with `#name` syntax. `#` is a part of the property name itself and should be used for declaring and accessing the property. Here is an example of declaring `products` as a private property:

```
class Cart{
  #products
  constructor(){
    this.#products = [];
  }
  
  addProduct(product){
    this.#products.push(product);
  }
  
  getTotalPrice(){
    return this.#products.reduce((total, p) => total + p.price, 0);
  }
}

console.log(cart.#products);
//Uncaught SyntaxError: Private field '#products' must be declared in an enclosing class
```

### Factory Functions

Another option is to create objects as collections of closures.

Closure is the ability of a function to access variables and parameters from the other function even after the outer function has executed. Take a look at the `cart` object built with what is called a factory function.

```
function Cart() {
  const products = [];
  
  function addProduct(product){
    products.push(product);
  }
  
  function getTotalPrice(){
    return products.reduce((total, p) => total + p.price, 0);
  }
  
  return {
   addProduct,
   getTotalPrice
  }
}

const cart = Cart();
cart.addProduct({name: 'orange', price: 1.25});
cart.addProduct({name: 'lemon', price: 1.75});
console.log(cart.getTotalPrice());
//3
```

`addProduct` and `getTotalPrice` are two inner functions accessing the variable `products` from their parent. They have access to the `products` variable event after the parent `Cart` has executed. `addProduct` and `getTotalPrice` are two closures sharing the same private variable.

`Cart` is a factory function.

The new object `cart` created with the factory function has the `products` variable private. It cannot be accessed from the outside.

```
console.log(cart.products);
//undefined
```

Factory functions don’t need the `new` keyword but you can use it if you want. It will return the same object no matter if you use it or not.

## Recap

Usually, we work with two types of objects, data structures that have public data and no behavior and object-oriented objects that have private data and public behavior.

Data structures can be easily built using the object literal syntax.

JavaScript offers two innovative ways of creating object-oriented objects. The first is using a prototype object to share the common behavior. Objects inherit from other objects. Classes offer a nice sugar syntax to create such objects.

The other option is to define objects are collections of closures.

**For more on closures and function programming techniques check out my book series [Functional Programming with JavaScript and React](https://www.amazon.com/gp/product/B08BW8BY1H).**

**The** [**Functional Programming in JavaScript**](https://www.amazon.com/dp/B08CZZ4FQQ) **book is coming out.**

