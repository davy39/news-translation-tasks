---
title: Objects in JavaScript – A Beginner's Guide
subtitle: ''
author: Damilola Oladele
co_authors: []
series: null
date: '2022-07-20T17:50:17.000Z'
originalURL: https://freecodecamp.org/news/objects-in-javascript-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/shelf4.jpg
tags:
- name: JavaScript
  slug: javascript
- name: object
  slug: object
seo_title: null
seo_desc: 'If you declare multiple variables to hold different values, this can make
  your program messy and clunky.

  For instance, if you need to store three characteristics each for 10 individuals,
  having 30 variables individually declared can make your program...'
---

If you declare multiple variables to hold different values, this can make your program messy and clunky.

For instance, if you need to store three characteristics each for 10 individuals, having 30 variables individually declared can make your program appear less organized.

So you need a way to group values with similar characteristics together to make your code more readable. And in JavaScript, objects work well for this purpose.

Unlike other data types, objects are capable of storing complex values. Because of this, JavaScript relies heavily on them. So it's important that you become familiar with what an object is, how to create one, and how you can use it before going in-depth into learning JavaScript.

This article will introduce you to the basics of objects, object syntax, the different methods of creating objects, how to copy objects and how to iterate over an object.

In order to get the most out of this article, you need to have at least a basic understanding of JavaScript, particularly variables, functions, and data types.

## What Are Objects in JavaScript?

An object is a data type that can take in collections of key-value pairs.

A major difference between an object and other data types such as strings and numbers in JavaScript is that an objects can store different types of data as its values. On the other hand, primitive data types such as numbers and strings can store only numbers and strings, respectively, as their values.

The key, also known as the property name, is usually a string. If any other data type is used as a property name other than strings, it would be converted into a string.

You can visualize an object as a multi-purpose shelf containing space for your gadgets and ornaments as well as a storage space for books, and files.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/shelf1-2.jpg align="left")

*A shelf with several items in it*

The most recognizable feature of an object is the brackets which contain the key-value pair.

```javascript
const emptyObject = {};
console.log(typeof emptyObject); //'object'
```

The contents of an object can consist of variables, functions, or both. Variables found in objects are properties, while functions are methods. Methods allow the objects to use the properties within them to perform some kind of action.

For example, in the sample code below, **object1.user**, **object1.nationality** and **object1.profession** are all properties of **object1** while **object1.myBio()** is a method:

```javascript
const object1 = {
    user: "alex",
    nationality: "Nigeria",
    profession: "Software Enginneer",
    myBio() {
        console.log(`My name is ${this.user}. I'm a               ${this.profession} from ${this.nationality}`)
    }
}
console.log(object1.user); //Alex 
console.log(object1.nationality); //Nigeria 
console.log(object1.profession); //Software Engineer 
console.log(object1.myBio()); //My name is alex. I'm a Software Engineer from Nigeria
```

The keys in the sample code above are **user**, **nationality** and **profession** while their values are the string values that come after the colons. Also, notice the use of the **this** keyword. The **this** keyword simply refers to the object itself.

As mentioned earlier in this article, the value of a property can be any data type. In the following sample code, the values are both arrays and objects:

```javascript
 const object2 = { 
        users: ["Alex", "James", "Mohammed"], 
        professions: { 
            alex: "software engineer", 
            james: "lawyer", 
            mohammed: "technical writer" 
        } 
    }; 
    console.log(object2.users); //['Alex', 'James', 'Mohammed'] 
    console.log(object2.professions); //{alex: 'software engineer', james: 'lawyer', mohammed: 'technical writer'}
```

## How to Access Objects and Create New Object Properties or Methods in JavaScript

There are two ways to access objects: dot notation and bracket notation. In the previous sample code, we used dot notation to access the properties and methods in **object1** and **object2**.

Also, to create new properties and methods after the declaration of an object, you can use either dot notation or bracket notation. You just have to state the new property and give it a value.

For instance, we can add new properties to **object2** like this:

```javascript
object2.ages = [30, 32, 40];
object2["summary"] = `Object2 has ${object2.users.length} users`;
console.log(object2);
/*
{
    "users": [
        "Alex",
        "James",
        "Mohammed"
    ],
    "professions": {
        "alex": "software engineer",
        "james": "lawyer",
        "mohammed": "technical writer"
    },
    "ages": [
        30,
        32,
        40
    ],
    "summary": "Object2 has 3 users"
}
*/
```

Similarly, you can use either notation to change the value of an object:

```javascript
object2.users = ["jane", "Williams", "John"];
object2["age"] = [20, 25, 29]
console.log(object2.users); //['jane', 'Williams', 'John']
console.log(object2.ages) //[20, 25, 29
```

Although dot notation is the most commonly used to access an object's properties and methods, it has some limitations. Let's look at them now.

### You Can't Use Values as Property Names with Dot Notation

If you want to use the value of a variable as a property name in your object, you have to use bracket notation and not dot notation. Whether the variable value is defined at runtime or not is irrelevant.

Runtime is a phase of a computer program in which the program is run or executed on a computer system.

For example:

```javascript
const object3 = {};
const gadget = prompt("enter a gadget type"); 
object3[gadget] = ["jbl", "sony"]; 
console.log(object3) //(respose entered in prompt): ["jbl","sony"] notice that the property name is the value you enter in the reply to the prompt message
```

If you define the variable value in your code, and you use dot notation to set that value as a property name of your object, dot notation will create a new property with the variable name instead of with the variable value.

```javascript
const computer = "brands"
object3.computer = ["hp", "dell", "apple"]
console.log(object3.brands); //undefined
console.log(object3.computer)//['hp', 'dell', 'apple']

object3[computer] = ["hp", "dell", "apple"]
console.log(object3.brands) //['hp', 'dell', 'apple']
```

Notice the omission of quotes within the square brackets. This is because the brackets took in a variable.

### You Can't Use Multi-Word Properties with Dot Notation

Where the property name is a multi-word string then dot notation is insufficient. For instance:

```javascript
object3.users height = [5.6, 5.4, 6.0];
Console.log(object3.users height); //SyntaxError
```

A syntax error occurs because JavaScript reads the command as `object3.users`, but the string height is not recognized so it returns a syntax error.

When using dot notation to access objects, the usual rules of declaring a variable apply. This means that if you want to use dot notation to access an object or create a property, the property name must not start with a number, must not include any spaces, and can only include the special characters *$* and \_*.*

To avoid this kind of error, you have to use bracket notation. For instance, you can correct the above sample code like this:

```javascript
object3["users height"] = [5.6, 5.4, 6.0];  
console.log(object3["users height"]); //[5.6, 5.4, 6]
```

## How to Create Objects with the Object Constructor in JavaScript

There are two methods by which you can create an object: an object literal and the object constructor. The objects used so far as samples in this article are object literals. Object literals work well if you want to create a single object.

But if you want to create more than one object, it is always better to use the object constructor. This allows you to avoid unnecessary repetition in your code and also makes it easier to change the properties of your object.

Basically, constructors are functions whose names are usually capitalized. The capitalization of a constructor name does not have any effect on the object. It is only a means of identification.

You can use a constructor to create a new object by calling the constructor with the **new** keyword. The **new** keyword will create an instance of an object and bind the **this** keyword to the new object.

As earlier mentioned in this article, the **this** keyword is a reference to the object itself.

An example of an object constructor is:

```javascript
function Profile(name, age, nationality) { 
    this.name = name; 
    this.age = age; 
    this.nationality = nationality; 
    this.bio = function () { 
        console.log(`My name is ${this.name}. I'm ${this.age} years old. I'm from ${this.nationality}`) 
    } 
};

const oladele = new Profile("Oladele", 50, "Nigeria" );
console.log(oladele.bio()); //My name is Oladele. I'm 50 years old. I'm from Nigeria
```

## How to Create Object Copies in JavaScript

Unlike primitive data types such as strings and numbers, assigning an existing object to another variable will not produce a copy of the original but rather a reference in memory.

What this means is that both the original object and subsequent objects created by assigning the original object as a value are referencing the same item in memory.

This means that a change in the value of any of the objects will also cause a change in the others. For example:

```javascript
let x = 10;
let y = x;
x = 20;
console.log(x); //20
console.log(y); //10

let object4 = { 
    name: "Alex", 
    age: 40 
}; 
let object5 = object4; 
console.log(object5); //{name: 'Alex', age: 40} 
object4.name = "Jane"; 
console.log(object5); //{name: 'Jane', age: 40}
console.log(object4 === object5); //true
```

To create a copy of an object, you can use the spread operator.

### What is the Spread Operator?

The spread operator is represented by three dots `...` . You can use the spread operator to copy the values of any iterable including objects.

An iterable is an object which can be looped over or iterated over with the help of a for...loop. Examples of iterables include objects, arrays, sets, strings, and so on.

To use the spread operator, you will have to prefix it to the object you want to copy from. For instance:

```javascript
let object6 = {...object5}; 
object5.name = "Willaims"; 
console.log(object5); //{name: 'Willaims', age: 40}
console.log(object6); //{name: 'Jane', age: 40}
console.log(object5 === object6); //false
```

As you can see, unlike in the previous code sample, where a change in the **object4** caused a change in **object5**, the change in **object6** did not result in a change in **object5**.

### How to Use the Object.assign() Method

The **Object.assign()** method copies all enumerable properties of one object into another and then returns the modified object.

The method takes in two parameters. The first parameter is the target object which takes in the properties copied. The second parameter is the source object which has the properties you want to copy. For instance :

```javascript
let object7  = Object.assign({}, object6); 
console.log(object7); //{name: 'Jane', age: 40}
console.log(object7); //{name: 'Jane', age: 40}

console.log(object6 === object7); //false
object6.age = 60
console.log(object6); //{name: 'Jane', age: 60}
console.log(object7); //{name: 'Jane', age: 40
```

You can see from the above sample code that a change in the value of the **age** property of **object6** did not cause a change in the vale of the **age** property of **object7**.

Note that both the spread operator and the **Object.assign()** method can only make a shallow copy of an object.

This means that if you have deeply nested objects or arrays in your source object, only the references to such objects are copied into the target object. So a change in the value of any of the deeply nested objects would cause a change in the value of the deeply nested object of the other. For example:

```javascript
let objectX = {
    name: 'Mary', 
    age: 40,
    gadgets: { 
        brand: ["apple", "sony"]
    }
};

let objectY = {...objectX};
objectY.name = "Bianca";
objectY.gadgets.brand[0] = "hp";
console.log(objectX);
/*
{
    "name": "Mary",
    "age": 40,
    "gadgets": {
        "brand": [
            "hp",
            "sony"
        ]
    }
}
*/ 

console.log(objectY);
/*
{
    "name": "Bianca",
    "age": 40,
    "gadgets": {
        "brand": [
            "hp",
            "sony"
        ]
    }
}
*/
```

The above sample code performed the following actions:

1. Created an object named **objectX**.
    
2. Gave three properties to **objectX**: name, age and gadgets.
    
3. Gave the **gadgets** property of **objectX** an object as its value.
    
4. Gave the object value of the **gadget** property a **brand** property.
    
5. Gave the **brand** property an array as its value.
    
6. Copied the properties in **objectX** into **objectY** with the use of the spread operator.
    
7. Changed the value of the **name** property of **objectY** to **Mary**.
    
8. Changed the the first item in the array value of the **brand** property from **apple** to **hp**.
    

In the sample code, the array value is a deeply nested object. Notice that a change in the value of the **name** property of **objectY** did not cause a change in the value of the **name** property of **objectX**. But a change in the deeply nested object of **objectY** caused a similar change in the deeply nested object of **objectX** .

## How to Iterate Over Objects in JavaScript

Use a **for...in** loop to iterate over an object and to select its properties. The **for..in** loop syntax is as follows:

```javascript
for(let key in object) {
    //perform action(s) for each key
}
```

The **key** keyword in the syntax above is a parameter for the properties. So you can replace it with any word of your choice. Replace the object keyword with the name of the object you want to iterate over. For example:

```javascript
let objectZ = {
    name: "Ade",
    Pronuon: "he",
    age: 60
};
for(let property in objectZ) {
    console.log(`${property}: ${objectZ[property]}`)
}
/* 
name: Ade
Pronuon: he
age: 60
*/
```

Notice the use of bracket notation in the loop to get the values of the property. Using dot notation instead of bracket notation would return undefined.

## Conclusion

In JavaScript, objects are probably the most important data type. Programming concepts like Object-Oriented programming work on the principle of leveraging the flexibility of objects to store complex values and their distinct capability of interacting with properties and methods within the object.

This article lays a solid foundation for understanding such advanced concepts by explaining the basics of objects.
