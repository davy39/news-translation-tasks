---
title: How to use destructuring in JavaScript (ES6) to its full potential
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-15T20:01:40.000Z'
originalURL: https://freecodecamp.org/news/destructuring-in-javascript-es6-ee963292623a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0e6fFQQRvkZ1LkeAHAMx7w.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Joanna Gaudyn

  Destructuring was a new addition to ES6. It took inspiration from languages like
  Python and allows you to extract data from arrays and objects into distinct variables.
  It might sound like something you’ve done in the earlier versions...'
---

By Joanna Gaudyn

Destructuring was a new addition to ES6. It took inspiration from languages like Python and allows you to extract data from arrays and objects into distinct variables. It might sound like something you’ve done in the earlier versions of JavaScript already, right? Have a look at two examples.

The first one extracts data from an object:

```
const meal = {  name: 'pizza',  type: 'marinara',  price: 6.25};
```

```
const name = meal.name;const type = meal.type;const price = meal.price;
```

```
console.log(name, type, price);
```

Prints:

> pizza marinara 6.25

And the second one from an array:

```
const iceCreamFlavors = ['hazelnut', 'pistachio', 'tiramisu'];const flavor1 = iceCreamFlavors[0];const flavor2 = iceCreamFlavors[1];const flavor3 = iceCreamFlavors[2];console.log(flavor1, flavor2, flavor3);
```

Prints:

> hazelnut pistachio tiramisu

The thing is, though, that neither of these examples actually uses destructuring.

#### What is destructuring?

Destructuring lets you specify the elements you want to extract from an array or object _on the left side of an assignment_. This means much less code and exactly the same result as above, without losing readability. Even if it sounds odd at first.

Let’s redo our examples.

#### Destructuring objects

Here’s how we destructure values from an object:

```
const meal = {  name: 'pizza',  type: 'marinara',  price: 6.25};
```

```
const {name, type, price} = meal;
```

```
console.log(name, type, price);
```

Prints:

> pizza marinara 6.25

The curly braces `{ }` stand for the object which is being destructured and `name`, `type`, and `price` represent the variables to which you want to assign the values. We can skip the property from where to extract the values, as long as the names of our variables correspond with the names of the object’s properties.

Another great feature of object destructuring is that you can choose which values you want to save in variables:

`_const {type} = meal;_` will only select the `_type_` property from the `_meal_` object.

![Image](https://cdn-media-1.freecodecamp.org/images/kWOMzaEg2A62-CFxEphqLSsopdq6r9ohdxDV)
_[source](https://unsplash.com/photos/22Vt7JIf7ZI" rel="noopener" target="_blank" title=")_

#### Destructuring arrays

Here’s how our original example would be handled:

```
const iceCreamFlavors = ['hazelnut', 'pistachio', 'tiramisu'];
```

```
const [flavor1, flavor2, flavor3] = iceCreamFlavors;
```

```
console.log(flavor1, flavor2, flavor3);
```

Prints:

> hazelnut pistachio tiramisu

The brackets `[ ]` stand for the array which is being destructured and `flavor1`, `flavor2` and `flavor3` represent the variables to which you want to assign the values. Using destructuring we can skip the indexes at which the values live in our array. Convenient, isn’t it?

Similarly as with an object, you can skip some values when destructuring an array:

`const [flavor1, , flavor3] = iceCreamFlavors;` will simply ignore `flavor2`.

![Image](https://cdn-media-1.freecodecamp.org/images/ZaoWWywMgfyk2d4UgeIhJzLwIYD2O46xHzpV)
_[source](https://unsplash.com/photos/qg_faAXDawA" rel="noopener" target="_blank" title=")_

Long live laziness as a potent motivator for the invention of new shortcuts!

Did you like this article? Maybe you’ll find these interesting too:

[**What does yoga have to do with programming?**](https://medium.freecodecamp.org/what-does-yoga-have-to-do-with-programming-b17094e3fb3a)  
[_You might be surprised._medium.freecodecamp.org](https://medium.freecodecamp.org/what-does-yoga-have-to-do-with-programming-b17094e3fb3a)[**Spread operator and rest parameter in JavaScript (ES6)**](https://medium.com/@aska.gaudyn/spread-operator-and-rest-parameter-in-javascript-es6-4416a9f47e5e)  
[_Both the spread operator and the rest parameter are written as three consecutive dots (…). Do they have anything else…_medium.com](https://medium.com/@aska.gaudyn/spread-operator-and-rest-parameter-in-javascript-es6-4416a9f47e5e)[**An overview of JavaScript iterators**](https://medium.freecodecamp.org/javascript-iterators-17ab32c3cae7)  
[_The difference between for, for…in and for…of loops_medium.freecodecamp.org](https://medium.freecodecamp.org/javascript-iterators-17ab32c3cae7)

