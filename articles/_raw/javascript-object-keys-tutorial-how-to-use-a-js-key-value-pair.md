---
title: JavaScript Object Keys Tutorial – How to Use a JS Key-Value Pair
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-11T18:35:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-object-keys-tutorial-how-to-use-a-js-key-value-pair
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/objects.jpg
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: null
seo_desc: "By Amy Haddad\nYou can group related data together into a single data structure\
  \ by using a JavaScript object, like this:\nconst desk = {\n   height: \"4 feet\"\
  ,\n   weight: \"30 pounds\",\n   color: \"brown\",\n   material: \"wood\",\n };\n\
  \nAn object contains proper..."
---

By Amy Haddad

You can group related data together into a single data structure by using a JavaScript object, like this:

```JavaScript
const desk = {
   height: "4 feet",
   weight: "30 pounds",
   color: "brown",
   material: "wood",
 };
```

An object contains properties, or key-value pairs. The `desk` object above has four properties. Each property has a name, which is also called a key, and a corresponding value. 

For instance, the key `height` has the value `"4 feet"`. Together, the key and value make up a single property. 

```JavaScript
height: "4 feet",
```

The `desk` object contains data about a desk. In fact, this is a reason why you’d use a JavaScript object: to store data. It’s also simple to retrieve the data that you store in an object. These aspects make objects very useful. 

This article will get you up and running with JavaScript objects:

* how to create an object 
* how to store data in an object
* and retrieve data from it.

Let’s start by creating an object.

# How to Create an Object in JavaScript

I'll create an object called `pizza` below, and add key-value pairs to it. 

```javaScript
const pizza = {
   topping: "cheese",
   sauce: "marinara",
   size: "small"
};
```

The keys are to the left of the colon `:` and the values are to the right of it. Each key-value pair is a `property`. There are three properties in this example:

* The key **topping** has a value **“cheese”**.
* The key **sauce** has a value **“marinara”**.
* The key **size** has a value **“small”**.

Each property is separated by a comma. All of the properties are wrapped in curly braces. 

This is the basic object syntax. But there are a few rules to keep in mind when creating JavaScript objects.

### Object Keys in JavaScript

Each key in your JavaScript object must be a string, symbol, or number.

Take a close look at the example below. The key names **`1`** and **`2`** are actually coerced into strings.

```javaScript 
const shoppingCart = {
   1: "apple",
   2: "oranges"
};
```

It’s a difference made clear when you print the object.

```javaScript 
console.log(shoppingCart);
//Result: { '1': 'apple', '2': 'oranges' }
```

There’s another rule to keep in mind about key names: if your key name contains spaces, you need to wrap it in quotes.

Take a look at the `programmer` object below. Notice the last key name, `"current project name"` . This key name contains spaces so, I wrapped it in quotes.

```javaScript
const programmer = {
   firstname: "Phil",
   age: 21,
   backendDeveloper: true,
   languages: ["Python", "JavaScript", "Java", "C++"],
   "current project name": "The Amazing App"
};
```

### Object Values in JavaScript

A value, on the other hand, can be any data type, including an array, number, or boolean. The values in the above example contain these types: string, integer, boolean, and an array.

You can even use a function as a value, in which case it’s known as a method. `sounds()`, in the object below, is an example. 

```javaScript 
const animal = {
   type: "cat",
   name: "kitty",
   sounds() { console.log("meow meow") }
};
```

Now say you want to add or delete a key-value pair. Or you simply want to retrieve an object’s value.

You can do these things by using dot or bracket notation, which we’ll tackle next.

# How Dot Notation and Bracket Notation Work in JavaScript

Dot notation and bracket notation are two ways to access and use an object’s properties. You’ll probably find yourself reaching for dot notation more often, so we'll start with that.

### How to Add a Key-Value Pair with Dot Notation in JavaScript

I'll create an empty `book` object below.

```JavaScript
const book = {};
```

To add a key-value pair using dot notation, use the syntax:

 `objectName.keyName = value`

This is the code to add the key (author) and value ("Jane Smith") to the `book` object: 

```JavaScript
book.author = "Jane Smith";
```

Here's a breakdown of the above code:

* `book` is the object's name
* `.` (dot)
* `author` is the key name 
* `=` (equals)
* `"Jane Smith"` is the value

When I print the book object, I’ll see the newly added key-value pair.

```javaScript 
console.log(book);
//Result: { author: 'Jane Smith' }
```

I’ll add another key-value pair to the `book` object.

```JavaScript
book.publicationYear = 2006;
```

The `book` object now has two properties.

```javaScript 
console.log(book);
//Result: { author: 'Jane Smith', publicationYear: 2006 }
```

### How to Access Data in a JavaScript Object Using Dot Notation

You can also use dot notation on a key to _access_ the related value. 

Consider this `basketballPlayer` object.

```javaScript
const basketballPlayer = {
   name: "James",
   averagePointsPerGame: 20,
   height: "6 feet, 2 inches",
   position: "shooting guard"
};
```

Say you want to retrieve the value “shooting guard.” This is the syntax to use: 

`objectName.keyName`

Let's put this syntax to use to get and print the "shooting guard" value.

```javaScript
console.log(basketballPlayer.position);
//Result: shooting guard
```

Here's a breakdown of the above code:

* `basketballPlayer` is the object's name
* `.` (dot)
* `position` is the key name

This is another example.

```javaScript
console.log(basketballPlayer.name);
//Result: James
```

### How to Delete a Key-Value Pair in JavaScript

To delete a key-value pair use the `delete` operator. This the syntax: 

`delete objectName.keyName`

So to delete the `height` key and its value from the `basketballPlayer` object, you’d write this code: 

```JavaScript
delete basketballPlayer.height;
````

As a result, the `basketballPlayer` object now has three key-value pairs.

```javaScript
console.log(basketballPlayer);
//Result: { name: 'James', averagePointsPerGame: 20, position: 'shooting guard' }
```

You’ll probably find yourself reaching for dot notation frequently, though there are certain requirements to be aware of.

When using dot notation, key names can’t contain spaces, hyphens, or start with a number.

For example, say I try to add a key that contains spaces using dot notation. I’ll get an error.

```javaScript
basketballPlayer.shooting percentage = "75%";
//Results in an error
```

So dot notation won’t work in every situation. That’s why there’s another option: bracket notation.

### How to Add a Key-Value Pair Using Bracket Notation in JavaScript

Just like dot notation, you can use bracket notation to add a key-value pair to an object. 

Bracket notation offers more flexibility than dot notation. That’s because key names _can_ include spaces and hyphens, and they can start with numbers.

I'll create an `employee` object below.

```JavaScript
const employee = {};
```

Now I want to add a key-value pair using bracket notation. This is the syntax: 

`objectName[“keyName”] = value`

So this is how I’d add the key (occupation) and value (sales) to the employee object: 

```JavaScript
employee["occupation"] = "sales";
```

Here's a breakdown of the above code:

* `employee` is the object's name
* `"occupation"` is the key name 
* `=` (equals)
* `"sales"` is the value

Below are several more examples that use bracket notation's flexibility to add a variety of key-value pairs.

```javaScript
//Add multi-word key name
employee["travels frequently"] = true;
 
//Add key name that starts with a number and includes a hyphen
employee["1st-territory"] = "Chicago";
 
//Add a key name that starts with a number
employee["25"] = "total customers";
```

When I print the `employee` object, it looks like this:

```javaScript
{
  '25': 'total customers',
  occupation: 'sales',
  'travels frequently': true,
  '1st-territory': 'Chicago'
}
```

With this information in mind, we can add the “shooting percentage” key to the `basketballPlayer` object from above.

```javaScript
const basketballPlayer = {
   name: "James",
   averagePointsPerGame: 20,
   height: "6 feet, 2 inches",
   position: "shooting guard"
};
```

You may remember that dot notation left us with an error when we tried to add a key that included spaces.

```JavaScript
basketballPlayer.shooting percentage = "75%";
//Results in an error
```

But bracket notation leaves us error-free, as you can see here:

```JavaScript
basketballPlayer["shooting percentage"] = "75%";
```

This is the result when I print the object:

```JavaScript 
{
  name: 'James',
  averagePointsPerGame: 20,
  height: '6 feet, 2 inches',
  position: 'shooting guard',
  'shooting percentage': '75%'
}
```

### How to Access Data in a JavaScript Object Using Bracket Notation

You can also use bracket notation on a key to _access_ the related value.

Recall the `animal` object from the start of the article.

```JavaScript
const animal = {
   type: "cat",
   name: "kitty",
   sounds() { console.log("meow meow") }
};
```

Let's get the value associated with the key, `name`. To do this, wrap the key name quotes and put it in brackets. This is the syntax: 

`objectName[“keyName”]`

Here's the code you'd write with bracket notation: `animal["name"];`.	

This is a breakdown of the above code:

* `animal` is the object's name
* `["name"]` is the key name enclosed in square brackets

Here’s another example.

```JavaScript
console.log(animal["sounds"]());

//Result: 
meow meow
undefined
```

Note that `sounds()` is a method, which is why I added the parentheses at the end to invoke it.

This is how you’d invoke a method using dot notation.

```JavaScript
console.log(animal.sounds());

//Result: 
meow meow
undefined
```

# JavaScript Object Methods

You know how to access specific properties. But what if you want _all_ of the keys or _all_ of the values from an object?

There are two methods that will give you the information you need.

```JavaScript
const runner = {
   name: "Jessica",
   age: 20,
   milesPerWeek: 40,
   race: "marathon"
};
```

Use the `Object.keys()` method to retrieve all of the key names from an object.

This is the syntax:

`Object.keys(objectName)`

We can use this method on the above `runner` object.

```JavaScript
Object.keys(runner);
```

If you print the result, you’ll get an array of the object’s keys.

```JavaScript
console.log(Object.keys(runner));
//Result: [ 'name', 'age', 'milesPerWeek', 'race' ]
```

Likewise, you can use the `Object.values()` method to get all of the values from an object. This is the syntax: 

`Object.values(objectName)`

Now we'll get all of the values from the `runner` object.

```JavaScript
console.log(Object.values(runner));
//Result: [ 'Jessica', 20, 40, 'marathon' ]
```

We’ve covered a lot of ground. Here’s a summary of the key ideas:

**Objects:**

* Use objects to store data as properties (key-value pairs).
* Key names must be strings, symbols, or numbers.
* Values can be any type.

**Access object properties:**

* Dot notation: `objectName.keyName`
* Bracket notation: `objectName[“keyName”]`

**Delete a property:**

* `delete objectName.keyName`  


There’s a lot you can do with objects. And now you’ve got some of the basics so you can take advantage of this powerful JavaScript data type.  


_I write about learning to program, and the best ways to go about it on [amymhaddad.com](http://amymhaddad.com/)._ I also _tweet about programming, learning, and productivity: [@amymhaddad](https://twitter.com/amymhaddad)_.

