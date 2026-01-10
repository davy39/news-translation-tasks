---
title: Learn the basics of object-oriented programming with JavaScript (and supercharge
  your coding…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-13T05:54:42.000Z'
originalURL: https://freecodecamp.org/news/intro-to-object-oriented-programming-oop-with-javascript-made-easy-a317b87d6943
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X6c_RNPQ7YOwfQemVNgBkw.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kris Baillargeon

  As a moderator of the freeCodeCamp chat rooms, I spend a lot of time with new developers.
  Boy, are they eager to learn. For a lot us, this can be quite a challenging quality.

  In the case of object-oriented programming (OOP), this ...'
---

By Kris Baillargeon

As a moderator of the [freeCodeCamp](https://www.freecodecamp.org/) chat rooms, I spend a lot of time with new developers. Boy, are they eager to learn. For a lot us, this can be quite a challenging quality.

In the case of object-oriented programming (OOP), this rings especially true. What the heck is a method and why is it so special? What’s the difference between a method and a property_?_ Why do we even use object-oriented programming, and why is it essential to me as a developer? These are some questions I asked myself while learning OOP, and because you’re here, it’s safe to assume that you have, too.

### Using Object-Oriented Programming with JavaScript

Almost everything in JavaScript is an object. Somewhere behind the scenes, every piece of code you write is either written or stored with OOP. That’s one of the reasons why it’s so important to understand it. If you don’t then you’ll most likely never be able to read other developers’ code. On top of that, your code will never reach its full potential!

A new object is made in JavaScript by assigning a variable to two curly brackets, like this:

```
var myObject = {};
```

```
// var myObject = new Object();  // Non recommended version, but it works
```

It’s that simple! You now have an object that can store any type of data you would store in a variable. There are many ways of inserting data into an object, but we’ll stick to the easiest methods right now.

### Quick Syntax Lesson

To end a line in JavaScript, when making a variable like this:

var a = 5;

the “line” ends at the semicolon. When you’re making an object, the “line” will end with a comma, like so:

```
myObject = { myProp: 5,  myOtherProp: 10,}
```

* Property/Key: The name of an object variable. An example would be `myProp` in the above code. || Left hand side of assignments
* Method : A function inside of an object, only available to that object. This is a type of property.
* Value: The value of an object variable. An example would be 10, which is the value of `myOtherProp.` This can be any valid JavaScript datatype.

Only the last property in an object _may_ not use a comma.

_Note: You may enclose your properties in single or double quotes. If there is a space in the property name, you must always use quotes. When using [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), using quotes is not optional._

### Referencing Object Properties

#### Dot notation

There are two ways of referencing an object, both having a name as reference. The most commonly used, dot notation_,_ is what is primarily used. It looks like this:

```
var myObject = {
```

```
otherObject: {            one: 1,        two: 2      },
```

```
addFunction: function(x,y){ return x+y }
```

```
}
```

```
var dot = myObject.otherObject;console.log(dot);//evaluates to otherObject: {..props:vals..}
```

The above code goes into `myObject` and adds another object to it, `otherObject` via dot notation. Any name that can be used as a variable is suitable for use in dot notation. Dot notation is best practice for referencing any property that doesn’t include spaces.

#### Bracket Notation

```
var myObject = {  "Other Obj": {          one: 1,      two: 2    }}
```

```
var bracket = myObject["Other Obj"];
```

```
bracket.newProperty = "This is a new property in myObject";
```

```
console.log(bracket.newProperty);
```

```
//evaluates to myObject["Other Obj"].newProperty
```

The other way to reference objects is via bracket notation. This is only recommended if the object’s property contains a space, such as the property `myObject[“Other Object”];` . In this case, using bracket notation is a must. When naming _methods,_ don’t use spaces — otherwise the function can’t be called. Additionally, you can use quotes to name any property.

### Using JavaScript IRL

Constructor Functions are worth mentioning, as we will be making our own form of constructor functions later on in this article. To do this, we must first learn two JavaScript keywords — **new** and **this**. You use the new keyword when referring to the constructor function.

For the this keyword, it’s basically a fancy keyword for the last called function parent object. If it has no parent object, window will be its parent object. You can bind a function to this keyword using Function.bind**().** Learn more [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)**.** But that’s a bit more advanced. Make any sense? Let’s look at some code:

```
var ConstructorForPerson = function(first, last, email) {  this.firstName = first;this.lastName = last;this.fullName = first + " " + last;this.eMail =  email;
```

```
}
```

```
var Bob = new ConstructorForPerson("bob", "brown", "bob122099@gmail.com");
```

```
console.log(Bob.eMail);
```

```
//evals "bob122099@gmail.com"
```

The above code will return a new object, `Bob.` That is the result of the constructor function, which will have the properties `Bob.firstName`, `Bob.lastName`, `Bob.fullName`, and `_Bob.eMail_`_**.**_

Note that inside of a constructor function, instead of ending a line with a comma, it ends with a semicolon like you would expect inside a function. Optionally, to keep things simple, you can make your own constructor functions without using **new** or **this**_._ That’s what we’ll be doing today so we can see all the moving pieces better.

### In Simple Terms

Object-oriented programming is a way of structuring your code for optimal readability, use, and maintenance. With this in mind, let’s try coding a representation of Google as a business, including some functions of a normal company.

* The Object — The Building/Management_._ This will contain all the information about any kind of employee, anything that can be done to an employee, including making a new one.
* The Properties — The Employees_._ This can be a manager or a desk clerk. This can be a list of employees. This can be your gross profit for this year. Pretty much anything.
* The Methods — What Can Google Do? What Can The Employees Do? This is how new employees are made, as well as how they will “perform tasks”.

### Let’s Code!

First, let’s look at our end result:

```
var google = { //create {google}
```

```
employees: {           management: {            },
```

```
developers: {                 },
```

```
maintenance: {            }   },      NewEmployee: function(name, role, phone, idNumber) {  //create NewExployee()            var newEmployeeData = {        name: name,        role: role,        phone: phone,        idNumber: idNumber,        working: false,        hours: [],       }     //make new object to append to google.employees[role]        google.employees[role][name] = newEmployeeData;    //assign object to google.employees[role][name]
```

```
return  google.employees[role][name];  //return the new object directly from google.employees[role][name]        } //end NewEmployee  } //end {google}
```

```
google.NewEmployee("james", "maintenance", "2035555555", "1234521"); //create {google:employees:maintenance["james"]} from NewEmployee()
```

```
google.employees["maintenance"]["james"].clockInOut = function() { //create clockInOut() - default false         if(this.working) {         this.hours[this.hours.length - 1].push(Date.now());         this.working = false;         return this.name + " clocked out at " + Date.now();        }       else{         this.hours.push([Date.now()]);         this.working = true;         return this.name + " clocked in at " + Date.now();        }
```

```
return "Error"     //if above doesn't work, "Error" }
```

```
google.employees["maintenance"]["james"].clockInOut(); //clock James in or out, returns a string w/ the time & state
```

Daunting?

Let’s break it down into smaller pieces. To start, we’ll make a global object called `Google`. It will contain another object for employees, which will contain more objects for each role and its individual employees.

So what will this look like in code? For the sake of keeping things easy, we’re going to make a constructor using a normal function. It will have 7 properties: `name`, _`role,`_ `phone`, _`idNumber`**,**_ `working`, and `hours`.

In addition, it will have 1 method: `clockInOut(),` which will look at the `_working_` property to update `hours.`

Let’s break it down.

First, we’re going to update our `Google` object with the `NewEmployee()` constructor function. Remember, instead of using the regular JavaScript constructor function, we’ll be using our own.

_Note: Pay attention to syntax as it will switch around a bit depending on what you’re doing_

_Also note: These examples will not run properly as they do not have the correct dependencies/properties/variables. Most if not all functionality from the final product will return an error. If you run the final product, however, everything should work fine._

```
var google = { //create {google}
```

```
employees: {           management: {
```

```
},           developers: {
```

```
},
```

```
maintenance: {
```

```
}         }, //<--this comma is unnecessary right now but when we add more object properties it will be necessary}
```

`employees` holds other objects which are various roles in the company: `management`, `developers`, and `maintenance`. We will be adding an employee via the employee’s role, in this case, maintenance.

```
var google = {  NewEmployee: function(name, role, phone, idNumber) {    var newEmployeeData = {      name: name,      role: role,      phone: phone,      idNumber: idNumber,      working: false,      hours: [],     }     //make new object to append to google.employees[role]        google.employees[role][name] = newEmployeeData;    //assign object to google.employees[role][name]
```

```
return  google.employees[role][name];  //return the new object directly from google.employees[role][name]  }}
```

Our “constructor” function”. Pretty straightforward, it takes a new object and appends it to the corresponding role.

```
google.employees["maintenance"]["james"].clockInOut = function() { //create clockInOut() - default false         if(this.working) {         this.hours[this.hours.length - 1].push(Date.now());         this.working = false;         return this.name + " clocked out at " + Date.now();        }       else{         this.hours.push([Date.now()]);         this.working = true;         return this.name + " clocked in at " + Date.now();        }
```

```
return "Error" //if above doesn't work, "Error" }
```

```
google.employees["maintenance"]["james"].clockInOut(); //call clockInOut()
```

This is where it might get confusing. Remember that the keyword this is just a funny way to say the calling function’s parent object? In the above, we add the method `clockInOut**_()_**` to our code. We invoke it simply by calling it. If working is false, it will create a new array with a Unix timestamp at index 0. If you’re already working, it will just append a Unix timestamp to the last created array, creating an array that looks kind of like this: [1518491647421, 1518491668453] with the first timestamp being when the employee “clocks in”, the second being when the employee “clocks out”.

Now we’ve seen how using OOP can be practical! Each individual employee can “clock in” and “clock out” with a simple function call, and all you have to know is their name and role!

This can, of course, be optimized to do something like look at an ID number instead of their role and name, but let’s not over-complicate things. Below we bring everything back into one program. Slightly less scary, right?

```
var google = { //create {google}
```

```
employees: {           management: {      },      developers: {      },
```

```
maintenance: {      }         },      NewEmployee: function(name, role, phone, idNumber) { //create NewExployee()            var newEmployeeData = {        name: name,        role: role,        phone: phone,        idNumber: idNumber,        working: false,        hours: [],       }     //make new object to append to google.employees[role]        google.employees[role][name] = newEmployeeData;    //assign object to google.employees[role][name]
```

```
return  google.employees[role][name];  //return the new object directly from google.employees[role][name]        }//end NewEmployee  } //end {google}
```

```
google.NewEmployee("james", "maintenance", "2035555555", "1234521"); //create {google:employees:maintenance["james"]} from NewEmployee()
```

```
google.employees["maintenance"]["james"].clockInOut = function() { //create clockInOut() - default false         if(this.working) {         this.hours[this.hours.length - 1].push(Date.now());         this.working = false;         return this.name + " clocked out at " + Date.now();        }       else{         this.hours.push([Date.now()]);         this.working = true;         return this.name + " clocked in at " + Date.now();        }
```

```
return "Error" //if above doesn't work, "Error" }
```

```
google.employees["maintenance"]["james"].clockInOut(); //call clockInOut()
```

Using Object Oriented Programming can not only make your code more powerful, but also much more readable to other developers. Feel free to contact me through [Github](https://github.com/krisb1220/) for projects, [Free Code Camp](http://www.freecodecamp.org/) info, Javascript/HTML/CSS help, to encourage me to write a tutorial on using JSON and APIS, or to talk about cats!

By the way, if you didn’t know, everything taught in this tutorial as well as ANYTHING you need to know about vanilla Javascript, HTML, CSS and more, you can count on [MDN](https://developer.mozilla.org/) to have an extensive amount of knowledge on it. It’s basically Google for web developers! It’s also 1220% free and open source.

Don’t forget to clap & follow if you enjoyed! More articles coming soon! :)

Keep up with me on Instagram [@krux.io](http://instagram.com/krux.io)

FURTHER LEARNING ON [MDN](https://developer.mozilla.org/):

[**OOP FOR BEGINNERS**](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)

[**GLOBAL OBJECTS**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/)

[**JSON TUTORIAL**](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

[**USING JSON IN JAVASCRIPT — GLOBAL JSON OBJECT**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

[**KEYWORD _THIS_**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)

[**CONSTRUCTOR FUNCTIONS**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/constructor)

