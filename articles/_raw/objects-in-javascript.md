---
title: What are Objects in JavaScript?
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2023-02-08T19:23:29.000Z'
originalURL: https://freecodecamp.org/news/objects-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Your-paragraph-text.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Objects are important data structures in JavaScript. This is partly because
  arrays are objects in JavaScript, and you''ll use them all the time.

  Objects are super important for grouping data and functionalities, so you can do
  a lot with an object in J...'
---

Objects are important data structures in JavaScript. This is partly because arrays are objects in JavaScript, and you'll use them all the time.

Objects are super important for grouping data and functionalities, so you can do a lot with an object in JavaScript. The DOM node, and any DOM node created with `createElement` are examples of an object in JavaScript. 

In this article, we will cover all the following about objects:

* [What is a JavaScript Object?](#heading-what-is-a-javascript-object)
* [How to Create an Object in JavaScript](#heading-how-to-create-an-object-in-javascript)
* [How to Add Properties in an Object](#heading-how-to-add-properties-in-an-object)
* [Why `let` Keyword Over dot Notation?](#heading-why-let-keyword-over-dot-notation)
* [How to Modify Properties in an Object](#heading-how-to-modify-properties-in-an-object)
* [How to Delete Properties in an Object](#heading-how-to-delete-properties-in-an-object)
* [How to Use Special Keys in Objects](#heading-how-to-use-special-keys-in-objects)
* [How to Access Properties with Square Brackets](#heading-how-to-access-properties-with-square-brackets)
* [How to Dynamically Set Properties](#heading-how-to-dynamically-set-properties)
* [Method Shorthand Syntax](#heading-method-shorthand-syntax)
* [Advantages of Using Object Short Methods over Regular Methods.](#heading-advantages-of-using-object-short-methods-over-regular-methods)
* [Object Spread Operator](#heading-object-spread-operator)
* [Object Destructuring](#heading-object-destructuring)
* [How to Use the `this` Keyword in JavaScript](https://www.freecodecamp.org/news/p/f8c8e52f-7c90-4e0c-b2ac-0bb498e15fb3/How%20to%20Use%20the%20this%20Keyword%20in%20JavaScript)
* [Conclusion](#heading-conclusion)

## What is a JavaScript Object?

Objects in everyday life have properties and “method” actions. Take, for instance, a fan. It's an object with properties such as make, color, or model, and actions it can perform such as cooling rooms and controlling humidity.

As explained above, objects in JavaScript are core data structures that comprise properties and methods. While methods are functions/actions an object can perform (such as driving and cooling rooms with real life objects like cars and fans), properties are characteristics of an object such as its name and value. 

Objects let you group related data together and split code into logical pieces. In JavaScript, we have primitive values and reference values. Number, Boolean, Null, Undefined, String, and Symbol are primitive values, while objects like DOM nodes, Arrays, and so on are reference values.

In both real life and JavaScript, you can use objects in different ways depending on their properties and methods. We'll learn more about JavaScript objects now.

## How to Create an Object in JavaScript

We'll use the code below as an example:

```javascript
const person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
```

In the above code, we have a `person` object that we created with curly braces. The object has key-value pairs. You can store key-value pairs in a JavaScript object, associating each key with a unique value. 

These key-value pairs allow you to retrieve values using the associated keys. For instance, the above object represents a person with properties like "name", "age"," friends", and a function "greet". Each property becomes a key-value pair with the property name as the key and the property value as the value. Both properties and methods are created inside the object.

To create a key in an object, you don't need a let or const keyword. Because objects are dynamic, you can add or change properties without declaring a variable. Rather, you start with your preferred name, a colon, and then your value. 

We created an array of `friends` inside the object to show we can have an object inside of an object. We created a method (which is a function) inside of an object with `greet` as the key.

### How to Add Properties in an Object

There are two major approaches to adding properties to an object in JavaScript. The first is to create a brand-new object.

```javascript
let person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
 person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  },
  isAdmin:true
}
```

With the above code, we created the first person object using the `let` keyword, allowing us to reassign it to a new value. We then added the "isAdmin" property to the person object. If you run `console.log(person)`, you will see that "isAdmin" is now part of the object's properties.

The second approach is to add properties using dot notation.

```javascript
const person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
person.isAdmin = true;
```

With dot notation, you can access properties that an object has not added before. For example, if the person object doesn't have an "isAdmin" property, accessing it will return "undefined". 

You can add the "isAdmin" property to the person object using dot notation, and you can also overwrite any property by assigning a new value to it. This approach is shorter and simpler compared to other methods.

### Why `let` Keyword Over dot Notation?

The choice between using the `let` keyword and dot notation depends on whether you need to create a new object reference or modify an existing one.

You would use the `let` keyword to create a new object when you need to create a new reference to an object, separate from any existing references to similar objects. 

On the other hand, you would use dot notation to add or modify properties on an existing object reference. This is useful when you want to make changes to an object without creating a new reference. 

### How to Modify Properties in an Object

You can also use dot notation to modify properties in an object. The below code shows that the property `name` with the pair value `kamal` will be changed to `lawal` when modified using dot notation.

```javascript
const person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
person.isAdmin = true;
person.name = 'lawal';
console.log(person);
```

### How to Delete Properties in an Object

It is very simple to delete a property in an object. JavaScript has a special keyword called "**delete**" that allows you to discard any properties you wish.

```javascript
const person = {
  name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
person.isAdmin = true;
delete person.friends;
console.log(person);
```

The property `friends` will be deleted from the object with the above code.

### How to Use Special Keys in Objects

You can use anything as a key name that you can use as a variable name. But not every key name can serve as a variable name because keys are more flexible than variables.

```javascript
let person = {
 name:'kamal',
 age:37,
}
```

Suppose you want to use "last name" as a key instead of "name". JavaScript syntax does not allow two separate words in this naming convention. 

But you can overcome this by using a special key in an object. JavaScript automatically converts any key you enter into a string, even the key "age". As a result, objects in JavaScript are a dictionary of string keys and values of any type.

```javascript
let person = {
  last name:'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
```

To use "last name" as a key in the above code, you need to inform JavaScript that it is a key by enclosing it in quotes, either single or double quotes will work. Using a name that can also be used as a variable is recommended instead of this exception method of setting a key.

```javascript
let person = {
  'last name':'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
  greet:function(){
    alert('Hello World')
  }
}
```

Using single quotes to surround "last name" and using it as a key name is valid JavaScript code and will work properly.

### How to Access Properties with Square Brackets

To add and modify properties in an object, you can use the object notation method. However, there is another method in JavaScript for accessing object properties, known as square bracket notation, which enables you to access a property created by a **special key** in JavaScript.

```javascript
let person = {
  'last name':'kamal',
  age:30,
  friends:[
     'Shola','Ade','Ibraheem'
  ],
}
// console.log(person.last name); is not valid in JavaScript
```

You cannot access the key name 'last name' using the dot notation method, but you can use the square bracket notation, which is available for any object. 

```javascript
console.log(person['last name']);
```

The above code will display the value of the last name key which is `kamal`. However, it is crucial to enclose your key within single or double quotes.

### How to Dynamically Set Properties

You can enable another dynamic feature with square brackets and objects in JavaScript. This works when you need to define a new property, especially when you don't know the property name. 

For example, you won't know specific user input ahead of time. But, you'll need to add the property with that name to the object.

```javascript
const userName ='level';

let person = {
 'first name':'kamal',
  age:30,
  [userName]: 'see',
}
console.log(person);
```

By not wrapping the **userName** in a square bracket, the property with the name userName will be added instead of the value stored inside it. Adding a square bracket to the **userName** will search and take the value stored in the variable as a key name and add it to a person object.

### Method Shorthand Syntax

There is an alternative syntax you can use to define a method in a more efficient way. Traditionally, to create a method in an object, you need a key and a value, where you create the value as a method using the function keyword.

```javascript
let person = {
  name:'jamaldeen',
  age:30,
  hobbies:[
     'reading','playing','sleeping'
  ],
  speek:function(){
    return this.hobbies
  }
}
console.log(person.speak());
```

In the above code, the method is created with a function keyword after a colon. Alternatively, you could do this:

```javascript
let person = {
  name:'jamaldeen',
  age:30,
  hobbies:[
     'reading','playing','sleeping'
  ],
  speek(){
    return this.hobbies
  }
}
console.log(person.speak());
```

In JavaScript, creating a method with object short methods is a shorthand notation. Omitting the "function" keyword and the colon(:) before the function body is allowed using the short methods. 

This is because with the short method syntax, the property is automatically defined as method, which renders the "function" keyword useless. 

The code remains functional because the JavaScript engine recognizes the shorthand syntax and interprets it as a regular function definition. 

### Advantages of Using Object Short Methods over Regular Methods.

Some of the advantages of using object short methods over regular methods are as follows

1. Conciseness: Unlike regular methods, object short methods allow you to write more compact and readable code.
2. Improved performance: Although, the performance of both object short methods and regular are similar, but the shorter syntax makes it easier to write and maintain your code.
3. Reusability: You can easily reuse object short methods in other objects.
4. Better organization: With object short methods, you can easily group related methods within an object and keep your code organized.

While using object short methods is good, using regular methods may still be more appropriate. It's important to choose the right approach based on your particular requirements.

### Object Spread Operator

The object spread operator is a popular and powerful syntax in JavaScript. The spread operator takes all the key-value pairs of an object and copies the key name and value into a new object. 

An object is a reference value, and if you want a copy of the object without pointing to the same property in memory, the spread operator is the answer.

```javascript
let person = {
  name:'kamal',
  age:30,
  hobbies:[
     'reading','playing','sleeping'
  ]
}
console.log(person);
const person2 ={...person};
console.log(person2.age);
```

The syntax for object spread operator goes between the opening and closing brackets. Then there should be three dots and the object you want to spread into this object.

### Object Destructuring

Object destructuring is an important feature in JavaScript that allows you to pull out values from an object and assign them to individual variables. 

To perform object destructuring, you use a destructuring pattern on the left-hand side of an assignment statement, and the object that you want to extract values from on the right-hand side. For example:

```javascript
const person = { name: 'lawal', age: 39 };
const { person, age } = person;
console.log(name); // 'lawal'
console.log(age); // 39

```

The `const` statement uses object destructuring to extract the `name` and `age` properties from the `person` object and assign them to two separate variables. This is a concise and efficient way to extract values from an object, especially when dealing with complex objects.

Object destructuring also enables you to provide default values, in case the property you want to extract does not exist in the object. You can also rename the variables being extracted using an alias, giving you greater control over the structure and naming of the extracted values.

## How to Use the `this` Keyword in JavaScript

What is the `this` keyword? `this` is a specific keyword in JavaScript which is most important when used inside of a function in an object. But you can use it anywhere in your code aside from the function body of an object. 

`this` is a powerful keyword used in referencing the current object in which it's used. 

```javascript
let person = {
  name:'kamal',
  age:30,
  greet:function(){
    return `My name is ${this.name}, and my age is ${this.age} years old`;
  },
}
console.log(person.greet());
// My name is kamal, and my age is 30 years old.
```

The code above demonstrates that the "this" keyword refers to the object containing the function, in this case the "person" object, and the result displays the output of the "greet" function. 

Regardless of its location within an object, the `this` keyword always refers to the entity that executed the function in the code. Using `this` in different contexts within the code can produce distinct results. For instance:

```javascript
let person = {
  name:'kamal',
  age:30,
  greet:function(){
    return `My name is ${this.name}, and my age is ${this.age} years old`;
  },
}
console.log(this);
```

The output of the code shows that the `this` keyword when console.logged will print a window object.

## Conclusion

In this tutorial, we learned about the JavaScript object, how to create an object, and how modify/delete properties in an object.

We briefly talked about how important the spread operator and object destructuring are in JavaScript object as well as the popular `this` keyword and how to use it in JavaScript objects.

