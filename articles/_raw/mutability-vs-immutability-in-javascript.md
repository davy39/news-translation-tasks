---
title: Mutability vs Immutability in JavaScript – Explained with Code Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-05T18:20:10.000Z'
originalURL: https://freecodecamp.org/news/mutability-vs-immutability-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/purple-balls-1.jpg
tags:
- name: immutability
  slug: immutability
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Chukwunonso Nwankwo\nIn JavaScript, different data types have different\
  \ behaviors and locations in memory. So to reduce the chances of having bugs in\
  \ your code, you need to understand the concept of mutability and immutability in\
  \ JavaScript. \nMutab..."
---

By Chukwunonso Nwankwo

In JavaScript, different data types have different behaviors and locations in memory. So to reduce the chances of having bugs in your code, you need to understand the concept of mutability and immutability in JavaScript. 

Mutability refers to data types that can be accessed and changed after they've been created and stored in memory. Immutability, on the other hand, refers to data types that you can't change after creating them – but that you can still access in the memory.

This article will help you to fully grasp the concept of mutability and immutability of data in JavaScript. We'll begin with understanding the different data types and go from there. 

### Prerequisites

* Knowledge of how variables work in JavaScript
* Knowledge of how objects work in JavaScript

### Table of Contents

* [What are Primitve Data Types in JavaScript?](#heading-what-are-primitve-data-types-in-javascript)
* [What are Reference Data Types in JavaScript?](#heading-what-are-reference-data-types-in-javascript)
* [How to Clone Object Properties](#heading-how-to-clone-object-properties)
* [What is Immutability in JavaScript?](#heading-what-is-immutability-in-javascript)
* [How to Prevent Object Mutability](#heading-how-to-prevent-object-mutability)
* [const != Immutability](#heading-const-immutability)
* [Final Thoughts](#heading-final-thoughts)

# Data Types in JavaScript

Data types are categorized into `Primitive` and `Reference` types in JavaScript. Before explaining these categories, let's look at two important terms with regards to memory that you will need to know: the `Stack` and `Heap`.

### What is the Stack?

Stack is a data structure that obeys the `Last In First Out` (LIFO) principle. This implies that the last item to enter the `stack` goes out first. 

Imagine a pile of books stacked up on a shelf. The last book ends up being the first to be removed. Data stored inside the stack can still be accessed easily.

### What is the Heap?

Reference data are stored inside the `heap`. When reference data is created, the variable of the data is placed on the `stack` but the actual value is placed on the `heap`. 

## What are Primitve Data Types in JavaScript?

Primitive data types are immutable and are not objects because they lack properties and methods.

![data-types-1](https://www.freecodecamp.org/news/content/images/2023/04/data-types-1.png)

To determine the kind of data you are working with, use the `typeof` operator. The `typeof` operator works perfectly with all primitive data types except `null`. 

### Primitive Data Type Examples

Let's look at some examples of primitive data types now to get a better understanding of what they are and how they work
 
Here's an example of a number:

```js
let num = 23;

console.log(typeof num)
```

Here's an example of a string:

```js
let str = "Table"
```

Here's an example of an undefined variable. A variable is said to be undefined if there are no values attached to it.

```js
let figure;

 `null`
 
   let fig = null

   console.log(fig)

   console.log(fig === null)
```

Keep in mind that `null` is not same as `Null` or `NULL`.

Here's an example of a boolean. This primitive data type is either `true` or `false`.

```js
   let student = true;

   let married = false;
```

Booleans are not strings – notice that `true` or `false` are not in quotes.

Here's an example of a symbol. As a primitive data type, symbols are unique. The values that are returned are also guaranteed to be unique.

```js
   const mySymbol = Symbol();
   
   console.log(typeof mySymbol) //Symbol
```

Here's an example of BigInit. Use `BigInt` when the values you are working on are too big for the number data types.

```js
   const myBigInt = 12n;

   console.log(typeof myBigInt) //BigInt

   const check = BigInt(414242532)

   console.log(typeof check)
```


## What are Reference Data Types in JavaScript?

By default, reference data types are mutable. Reference data types consist of `Functions`, `Arrays`, and `Objects`.  

Let's look at some examples of reference data types to help you understand better:

Here's an example of a function:

```js
   function favorite(question) {
      console.log(`Hi dear, do you like ${question} programming language?`)
   }

   favorite('JavaScript')

```

Here's an example of an array:

```js
   const countriesVisited = ['Nigeria', 'Japan', 'Australia']

   console.log(countriesVisited)

```

Here's an example of an object:

```js

   const touristData = {
      firstname: 'Camila',
      lastname: 'Pedro',
      Nationality: 'Spanish'
   }
   console.log(touristData)

```

Just for clarity, the firstname is called the `key` while Camila is the `value`.

Reference data types place the variable on the `stack`. The variable serves as a pointer that points to the `object` located on the `heap.` 

The main distinction between these categories is that Primitives are `immutable` but References are `mutable`. Now, let's get to the meat of the matter.

# What is Mutability in JavaScript?

If a data type is mutable, that means that you can change it. Mutability allows you to modify existing values without creating new ones. 

For every `object`, a pointer is added to the `stack`, and this pointer points to the `object` on the `heap`.  

Take, for example, the following code: 

```js
    const staff = {
         name: "Strengthened",
         age: 43,
         Hobbies: ["reading", "Swimming"]
   }

```

On the stack you will find `staff` which is a pointer to the actual object on the `heap`.

```js
   const staff2 = staff;

   console.log(staff);
   
   console.log(staff2);
```

Another pointer is placed on the `stack` when `staff` was assigned to `staff2`. Now, these pointers point to a single object on the `heap`.

Reference data does not copy values, but rather pointers.

```js
   staff2.age = 53;

   console.log(staff)

   console.log(staff2)

```

Changing the `age` of `staff2` updates the `age` of the `staff` object. Now you know it is because both point to the same object. 

  ![reference2-1](https://www.freecodecamp.org/news/content/images/2023/04/reference2-1.png)


## How to Clone Object Properties

You can clone the properties of an object using the `Object. assign()` method and the `spread` operator. With these, you can change the properties of the cloned object without changing the properties of the object from which it was cloned.
 
### How the `Object.assign()` method Works

The `object.assign` method copies properties from an object (the source) into another object (the target) and returns the modified target object.

Here's the syntax:

```Object.assign(target, source)```

The method has two arguments, `target` and `source.` The `target` is the object that receives new properties, while the `source` is where the properties come from. The `target` can be an empty object `{}.` 

In a situation where the `source` and `target` share the same `key`, the `source` object overwrites the value of the `key` on the target.

```js
   const staff = {
      name: "Strengthened",
      age: 43,
      Hobbies: ["reading", "Swimming"]
   }

   const staff2 = Object.assign({}, staff);
```

The properties on the `staff` object were cloned into an empty `target`. 

`staff2` now has its own properties. You can prove this by changing the value of any of its properties. Making this change will not affect the values of the properties on the `staff` object.

```js
   staff2.age = 53;

   console.log(staff)

   console.log(staff2)
```

The value of `staff2.age` that was changed to `53` does not in any way affect the value of `staff.age` because they both have their own properties.

### How the `Spread` Operator Works

Here's the syntax of the spread operator:

```js
   const newObj = {...obj}

```

Using the `spread` operator is quite simple. You need to place three dots `...` before the name of the object whose properties you intend to clone:

```js
   const staff = {
    name: "Strengthened",
    age: 43,
    Hobbies: ["reading", "Swimming"]
   }

   const staff2 = {...staff};


   staff2.age = 53;

   console.log(staff)

   console.log(staff2)

```

![cloning](https://www.freecodecamp.org/news/content/images/2023/04/cloning.png)


## What is Immutability in JavaScript?

Immutability is the state where values are immutable (that is, not able to be changed). A value is immutable when altering it is impossible. Primitive data types are immutable, as we discussed above.

Let's look at an example:

```js
   const num = 46;
   const newNum = num;

```

Looking at the code above, `num` was reassigned to `newNum.` Now both `num` and `newNum` have a value of `46`. Changing the value on `newNum` will not alter the value on `num.

```js
      let student1 = "Halina";

      let student2 = student1;
```

In the code above, a variable called `student1` was created and assigned to `student2`.

```js
      student1 = "Brookes"

      console.log(student1);

      console.log(student2)
```

Changing `student1` to `Brookes` does not change the initial value on `student2`. This proves that in primitive data types, actual values are copied, so both have their own. On the stack memory, `student1` and `student2` are distinct. 

The stack obeys the `Last-In-First-Out` principle. The first item that enters the stack is the last item to go out and vice versa. Accessing items  stored in the stack is easy.

![primitive-1](https://www.freecodecamp.org/news/content/images/2023/04/primitive-1.png)

## How to Prevent Object Mutability 

So far you have learned that objects are mutable by default.

```js
   const studentNames = {
           student1: 'Halina',
           student2: "Brookes",
           student3:"Anthony"
   }


   Object.defineProperty(studentNames, "student4", {
      value: "Mirabel",
   })

   console.log(studentNames);
```

Now we've added `student4`.

To prevent object `mutability`, you can use the `Object.preventExtensions()`, `Object.seal()`, and `Object.freeze()` methods.

For all three methods, we will explore adding properties using dot notation and the `define` property, modifying properties using defineProperty, and deleting properties. 

This will give you a better understanding of the capabilities and limitations of each method, and ultimately help you in determining which method may be best suited for a particular use case. 

So, let's dive in and explore these methods in more detail.


### How to Use the `Object.preventExtensions` Method

Here's the syntax of this method:

`Object.preventExtensions(obj)`

Using `Object.preventExtensions` stops new properties from entering the object. The object does not increase in size and maintains its properties. By default, all objects in JavaScript are extensible. With this method, you can delete properties from your object.

#### How to add new properties


* using `dot notation`:


```js
   const makeNonExtensive = {
           firstname: "Charles",
           lastname: "Chandlier"
   }

   Object.preventExtensions(makeNonExtensive)

   makeNonExtensive.designation = "Software Engineer";
   
   console.log(makeNonExtensive)

```

Check the console – the `designation` property was not added and there's no error message.

```js
   const obj = {
           firstname: "Derek",
           designation: "Software Engineer"
   }
```   

* using the `defineProperty` method
   
Here's the syntax:
   
```js
   Object.defineProperty(obj, prop, descriptor)
```

Here's what's going on in that code:
   
- `obj`: The object you want to add properties to.
- `prop`: You define the name of the property you want to add or change. It should be either a string or symbol
- `Descriptor`: You include the value of the property.


```js
   const makeNonExtensive = {
           firstname: "Charles",
           lastname: "Chandlier"
   }

   Object.preventExtensions(makeNonExtensive)

   Object.defineProperty(makeNonExtensive, "age", {
      value: "twenty",
   })

   console.log(makeNonExtensive)
```

- Adding new properties using the define property throws this error message: `index.js:361 Uncaught TypeError: Cannot define property age, object is not extensible`.

![define-prop-cons](https://www.freecodecamp.org/news/content/images/2023/04/define-prop-cons.png)

#### How to modify an existing property using the `define Property`

```js
    const makeNonExtensive = {
            firstname: "Charles",
            lastname: "Chandlier"
    }

   Object.preventExtensions(makeNonExtensive)

   Object.defineProperty(makeNonExtensive, 'firstname', {
    value: 'Jason',
    })
    console.log(makeNonExtensive)
```

The value of the property of a non-extensible object can be changed as demonstrated with the above line of code.

![modify-pext-1](https://www.freecodecamp.org/news/content/images/2023/04/modify-pext-1.png)


#### How to delete a property

Here's the syntax:

```
   delete object.propertyname
```

```js
   const makeNonExtensive = {
           firstname: "Charles",
           lastname: "Chandlier"
   }

   Object.preventExtensions(makeNonExtensive)

   delete makeNonExtensive.lastname

   console.log(makeNonExtensive)

```

In spite of the object being non-extensible, the `lastname` property was deleted.

![pExtension-del-1](https://www.freecodecamp.org/news/content/images/2023/04/pExtension-del-1.png)


### How to Use `Object.seal()`

All objects in Javascript are extensible by default. Just as the name suggests, this method seals an object. You cannot add new properties to a sealed object or delete an existing property from a sealed object. But `object.seal` permits modifying existing properties.

Here's the syntax:

```
Object.seal()
```

#### How to add new properties

```js
   const studentNames = {
           student1: 'Halina',
           student2: "Brookes", 
           student3:"Alina"
   }

   Object.seal(studentNames)

   console.log(Object.isSealed(studentNames))
```

`Object.isSealed(studentNames)` is used to check if an object is sealed.

#### How to use `dot notation`

```js
   studentNames.student4 = "Barbara";

   console.log(studentNames)
```

Without producing an error, the dot notation fails when adding the new property `student4`. 
  
#### How to use the `defineProperty` method
  
  ```js
      const studentNames = {
              student1: 'Halina',
              student2: "Brookes",
              student3:"Alina"
      }

      Object.seal(studentNames)

      Object.defineProperty(studentNames, 'student4', {
         value: 'Barbara'
      })

      console.log(studentNames)

  ```

The error message "Uncaught TypeError: Cannot define property student4, the object is not extendable" is thrown when attempting to add the same property using the `define property` method.

![seal1-2](https://www.freecodecamp.org/news/content/images/2023/04/seal1-2.png)

#### How to modify an existing property using `define Property`
  
```js
   
      const studentNames = {
              student1: 'Halina',
              student2: "Brookes",
              student3:"Alina"
      }

         Object.seal(studentNames)

      Object.defineProperty(studentNames, 'student2', {
         value: "Water-Brookes",
      })

      console.log(studentNames)

```

Now `student2` has been changed from "Brookes" to "Water-Brookes".

![seal2](https://www.freecodecamp.org/news/content/images/2023/04/seal2.png)

#### How to delete a property

```js
   const studentNames = {
           student1: 'Halina',
           student2: "Brookes",
           Student3:"Alina"
   }

   Object.seal(studentNames)

   delete studentNames.student1

   console.log(studentNames)
 
```

Properties cannot be removed from sealed objects. In the console, student1 still remains.

![seal3-2](https://www.freecodecamp.org/news/content/images/2023/04/seal3-2.png)


### How to Use `Object.freeze()`

Here's the syntax:

```
   Object.freeze()
```

The `Object.freeze()` method freezes an object. Using this method guarantees high integrity by ensuring that pulling out, modifying existing properties, or adding new properties to the object will not be possible. 

To check if an object is frozen, use the syntax below:

```
   Object.isFrozen(obj);
```

Even when you apply the `object.freeze` to an object, you can add new property, modify an existing property, or delete properties from objects nested under it. 

Just as we have done for other methods, let's explore the object.freeze method in relation to adding new properties, modifying values, or deleting properties from an object.


#### How to add new properties

* Using `dot notation`

```js
   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance"
   }


   Object.freeze(teamplayers)

   teamplayers.player3 = "Finder";

   console.log(teamplayers)

```

![freeze-dot](https://www.freecodecamp.org/news/content/images/2023/04/freeze-dot.png)

Notice that `player3` was not added.

* Using the `defineProperty` method

```js
   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance"
   }


   Object.freeze(teamplayers)

   Object.defineProperty(teamplayers, 'player3', {
      value: 'Charis'
      })
      console.log(teamplayers)

   console.log(teamplayers)

```

Dot notation fails silently when trying to add a property, but `defineproperty` throws a TypeError instead.

![freeze1](https://www.freecodecamp.org/news/content/images/2023/04/freeze1.png)


#### How to modify an existing property


```js
   
   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance"
   }


   Object.freeze(teamplayers)


   teamplayers.player1 = "Christabel"

   console.log(teamplayers)
```

![freeze2](https://www.freecodecamp.org/news/content/images/2023/04/freeze2.png)

This will fail silently. But with the define property below a `typeError` is thrown.
 
```js
   
      const teamplayers = {
              player1: "Andrey",
              player2: "Abundance"
      }


      Object.freeze(teamplayers)


      Object.defineProperty(teamplayers, 'player1', {
         value: "Anne"
      })

      console.log(teamplayers)
```

 `Uncaught TypeError: Cannot redefine property: player1`


![freeze3](https://www.freecodecamp.org/news/content/images/2023/04/freeze3.png)

#### How to delete a property

```js

   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance"
   }


   Object.freeze(teamplayers)


   delete teamplayers.player2

   console.log(teamplayers)

```

Attempting to delete a property on a frozen object also fails silently.

![freeze4](https://www.freecodecamp.org/news/content/images/2023/04/freeze4.png)

#### How to use Deep Freeze

```js
  
   const teamplayers = {
           player1: "Andrey",
           player2: "Abundance",
                   substitutes: {
                   player3: "Jeremiah",
                   player4: "Jayden"
            }
   }

   const squad = teamplayers;

   Object.freeze(teamplayers)


   Object.defineProperty(teamplayers.substitutes, 'player5', {
      value: "Woodland"
   })

   console.log(teamplayers)


```

Player5 has been added to the nested `substitutes` even though the `object.freeze` method was applied to the parent `teamplayers`.

![deep1](https://www.freecodecamp.org/news/content/images/2023/04/deep1.png)

You can also modify the value of the properties in the nested object.

- How to delete a property

```js
   delete teamplayers.substitutes.player3

   console.log(teamplayers)
```

Player3 has been removed. Everything that the object.freeze prevents on the parent object is obtainable on the child object that is nested.

![deep2](https://www.freecodecamp.org/news/content/images/2023/04/deep2.png)

To prevent this, we employ the deep freeze technique as shown below:

```js
   const deepVal = obj => {
        Object.keys(obj).forEach(prop => {
        if (typeof obj[prop] === 'object') deepVal(obj[prop]);
        });
        return Object.freeze(obj);
    };

    const teamplayers = deepVal( {
            player1: "Andrey",
            player2: "Abundance",
                    substitutes: {
                        player3: "Jeremiah",
                        player4: "Jayden"
                    }
            }
    )
   const squad = teamplayers;

   Object.freeze(teamplayers)
   
   console.log(Object.isFrozen(teamplayers));
   
   console.log(Object.isFrozen(squad));


```

- How to add a new property to the child object.
  
```js
   
const deepVal = obj => {
        Object.keys(obj).forEach(prop => {
        if (typeof obj[prop] === 'object') deepVal(obj[prop]);
        });
        return Object.freeze(obj);
 };

    const teamplayers = deepVal( {
            player1: "Andrey",
            player2: "Abundance",
                    substitutes: {
                        player3: "Jeremiah",
                        player4: "Jayden"
                    }
            }
    )

   Object.freeze(teamplayers)

   Object.defineProperty(teamplayers.substitutes, 'player5', {
      value: "Alice"
   })

   console.log(teamplayers)

```

Now when you attempt adding a property, you will get this error `Uncaught TypeError: Cannot define property player5, object is not extensible`

![deep-addd-1](https://www.freecodecamp.org/news/content/images/2023/04/deep-addd-1.png)

Also deep freeze prevents you from changing and deleting properties of an object.

## const != Immutability

A variable declared using the `let` keyword can be reassigned using the assignment operator (`=`). Take a look at the code below to understand what I mean.

```js
   let num = 34;
   num = 50;

   console.log(num);
```

Here, after declaring variable `num` using the `let` keyword, the value was reassigned from 34 to 50.

However, you cannot achieve the same thing on the same variable declared using the `const` keyword. 

```js
 const num = 34;
 num = 50;

 console.log(num);

```

You will get this error `Uncaught TypeError: Assignment to constant variable`.

But that is not the case with objects. An object that you declared using `const` is still mutable, so you can still modify the properties of that particular object as you can see below:


```js
   const getObj = {
           color1: "Green",
           color2: "Blue",
           color3: "Yellow"
   }

   getObj.color1 = "Brown";
   
   console.log(getObj.color1) 

```

The value of `color1` was altered from `Green` to `Brown`, even when declared with `const`.


## Final Thoughts
You've now learned about the various data types and whether they are immutable or mutable by default. 

Objects can be changed by default. But using specific methods like the Object.seal, Object.freeze, and preventExtensions can prevent mutability. 

The level of immutability provided by these methods varies, so make sure you use the one that corresponds to the integrity level you want to accomplish. Until next time, keep exploring JavaScript.



