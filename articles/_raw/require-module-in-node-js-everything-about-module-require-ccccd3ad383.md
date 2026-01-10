---
title: Everything you should know about ‘module’ & ‘require’ in Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T06:56:00.000Z'
originalURL: https://freecodecamp.org/news/require-module-in-node-js-everything-about-module-require-ccccd3ad383
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tZaoIiIYEv0bc0bLO-CYVg.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Srishti Gupta

  Modules


  Node.js treats each JavaScript file as a separate module.


  For instance, if you have a file containing some code and this file is named xyz.js,
  then this file is treated as a module in Node, and you can say that you’ve creat...'
---

By Srishti Gupta

### Modules

> Node.js treats each JavaScript file as a separate module.

For instance, if you have a file containing some code and this file is named `xyz.js`, then this file is treated as a _module_ in Node, and you can say that you’ve created a module named `xyz`.

![Image](https://cdn-media-1.freecodecamp.org/images/I7AE0rZ1lpEU9AhiKUgm1TjeJl3JUeWY-CsF)
_JavaScript file in Node.js corresponding to a ‘module’_

Let’s take an example to understand this better.

You have a file named `circle.js` which consists of the logic for calculating the area & the circumference of a circle of a given radius, as given below:

_circle.js_

You can call `circle.js` file a module named `circle`.

You might be wondering why is there a need to have multiple modules? You could have just written all the code in a single module. Well, it is very important to write modular code. By modular, I mean to say that your code should be independent and should be loosely coupled. Imagine that there’s a large application and you have all your code written in just one place, just one file. Too messy, right?

### How does the code written inside a module run?

Before executing the code written inside a module, Node takes the entire code and encloses it within a function wrapper. The syntax of this function wrapper is:

![Image](https://cdn-media-1.freecodecamp.org/images/jrHUpyWccEG3RTJQg54GR78bbJw6FxN6cWtf)
_All code you write in a module resides in the function wrapper!_

The function wrapper for the `circle` module will look like the one given below:

You can see that there is a function wrapper at the root level encompassing all the code written inside the `circle` module.

> The entire code written inside a module is private to the module, unless explicitly stated (exported) otherwise.

This is the most significant advantage of having modules in Node.js. Even if you define a global variable in a module using `var`, `let` or `const` keywords, the variables are scoped locally to the module rather than being scoped globally. This happens because each module has a function wrapper of its own and the code written inside one function is local to that function and cannot be accessed outside this function.

![Image](https://cdn-media-1.freecodecamp.org/images/ppIlxCPf-ko2PaAXyhiOqckmoNtcyHKeYCs1)
_Code written inside a module is private to it!_

Imagine that there are two modules — _A_ and _B_. The code written inside the _module A_ is enclosed within the function wrapper corresponding to the _module A_. Similar thing happens with the code written inside the _module B_. Because the code pertaining to both the modules is enclosed within different functions, these functions will not be able to access the code of each other. (Remember each function in JavaScript has its own local scope?) This is the reason why _module A_ cannot access the code written inside _module B_ and vice-versa.

The five parameters — `exports`, `require`, `module`, `__filename`, `__dirname` are available inside each module in Node. Though these parameters are global to the code within a module yet they are local to the module (because of the function wrapper as explained above). These parameters provide valuable information related to a module.

Let’s revisit the `circle` module, which you looked at earlier. There are three constructs defined in this module — a constant variable `PI`, a function named `calculateArea` and another function named `calculateCircumference`. An important point to keep in mind is that all these constructs are private to the `circle` module by default. It means that you cannot use these constructs in any other module unless explicitly specified.

So, the question that arises now is how do you specify something in a module that can be used by some other module? This is when the `module` & `require` parameters of the function wrapper are helpful. Let’s discuss these two parameters in this article.

### `**module**`

The `module` parameter (rather a keyword in a module in Node) refers to the object representing the _current module_. `exports` is a key of the `module` object, the corresponding value of which is an object. The default value of `module.exports` object is `{}` (empty object). You can check this by logging the value of `module` keyword inside any module. Let’s check what is the value of `module` parameter inside the `circle` module.

_circle.js_

Notice that there is a `console.log(module);` statement at the end of the code in the file given above. When you see the output, it will log the `module` object, which has a key named `exports` and the value corresponding to this key is `{}` (an empty object).

Now, what does the `module.exports` object do? Well, it is used for defining stuff that can be exported by a module. Whatever is exported from a module can, in turn, be made available to other modules. Exporting something is quite easy. You just need to add it to the `module.exports` object. There are three ways to add something to the `module.exports` object to be exported. Let’s discuss these methods one by one.

**Method 1:**  
**(Defining constructs and then using multiple `module.exports` statements to add properties)**

In the first method, you define the constructs first and then use multiple _module.exports_ statements where each statement is used to export something from a module. Let’s look at this method in action and see how you can export the two functions defined in the `circle` module.

_circle.js_

As I told you earlier, `module` is an object having the key named `exports` and this key (`module.exports`), in turn, consists of another object. Now, if you notice the code given above, all you are doing is adding new properties (key-value pairs) to the `module.exports` object.

The first property has the key `calculateArea` (defined on line 19) and the value written on the right side of the assignment operator is the function defined with the name `calculateArea` (on line 9).

The second property (defined on line 20) has the key `calculateCircumference` and the value is the function defined with the name `calculateCircumference` (on line 16).

Thus, you have assigned two properties (key-value pairs) to the `module.exports` object.

Also, let’s not forget that you have used the dot notation here. You can alternatively use the bracket notation for assigning the properties to the `module.exports` object and add the functions — `calculateArea` and `calculateCircumference` by specifying the keys following the bracket notation. Thus, you can write the following two lines to add properties to the `module.exports` object using bracket notation while replacing the last two lines (using dot notation) in the code given above:

```
// exporting stuff by adding to module.exports object using the bracket notation
```

```
module.exports['calculateArea'] = calculateArea;module.exports['calculateCircumference'] = calculateCircumference; 
```

Let’s now try to log the value of the `module.exports` object after adding the properties. Notice that the following statement is added at the end of the code in the file given below:

```
// logging the contents of module.exports object after adding properties to it
```

```
console.log(module.exports);
```

_circle.js_

Let’s check the output of this code and see if everything is working fine. To do this, save your code and run the following command in your _Terminal_:

```
node circle
```

Output:

```
{    calculateArea: [Function: calculateArea],   calculateCircumference: [Function: calculateCircumference] }
```

The constructs — `calculateArea` and `calculateCircumference`, added to the `module.exports`, object are logged. Thus, you successfully added the two properties in the `module.exports` object so that the functions — `calculateArea` and `calculateCircumference` can be exported from the `circle` module to some other module.

In this method, you first defined all the constructs and then used multiple _module.exports_ statements where each statement is used to add a property to the `module.exports` object.

**Method 2:**  
**(Defining constructs and then using a single `module.exports` statement to add properties)**

Another way is to define all the constructs first (as you did in the earlier method) but use a single `module.exports` statement to export them all. This method is similar to the syntax of object literal notation where you add all the properties to an object at once.

Here, you used the object literal notation and added both the functions — `calculateArea` and `calculateCircumference` (all at once) to the `module.exports` object by writing a single _module.exports_ statement.

If you check the output of this code, you will get the same result as you got earlier when using method 1.

**Method 3:**  
**(Adding properties to the `module.exports` object while defining constructs)**

In this method, you can add the constructs to the `module.exports` object while defining them. Let’s see how this method can be adopted in our `circle` module.

In the code given above, you can see that the functions in the module are added to the `module.exports` object when they are being defined. Let’s look at how this is working. You are adding a key `calculateArea` to the `module.exports` object and the value corresponding to this key is the function definition.

Note that the function no longer has any name and is an anonymous function which is just treated as a value to a key of an object. Thus, this function cannot be referenced to in the `circle` module and you cannot invoke this function inside this module by writing the following statement:

```
calculateArea(8);
```

If you try to execute the above statement, you will get a `ReferenceError` stating `calculateArea is not defined`.

Now that you have learned how you can specify what needs to be exported from a module, how do you think the other module will be able to use the exported stuff? You need to import the module to some other module so as to be able to use the exported stuff from the former in the latter. This is when we need to discuss another parameter named `require`.

### **require**

`require` keyword refers to a function which is used to import all the constructs exported using the `module.exports` object from another module. If you have a module _x_ in which you are exporting some constructs using the `module.exports` object and you want to import these exported constructs in module _y_, you then need to require the module _x_ in the module _y_ using the `require` function. The value returned by the `require` function in module _y_ is equal to the `module.exports` object in the module _x_.

![Image](https://cdn-media-1.freecodecamp.org/images/N6RvqZ73VV1jBVwXFGq4btuHNztUnTRTcVEf)
_**require** function returns **module.exports** object_

Let’s understand this using the example which we discussed earlier. You already have the `circle` module from which you are exporting the functions `calculateArea` and `calculateCircumference`. Now, let’s see how you can use the `require` function to import the exported stuff in another module.

Let’s first create a new file wherein you will be using the exported code from the `circle` module. Let’s name this file `app.js` and you can call it the `app` module.

The objective is to import into the `app` module all the code exported from the `circle` module. So, how can you include your code written in one module inside another module?

Consider the syntax of the `require` function given below:

```
const variableToHoldExportedStuff = require('idOrPathOfModule');
```

The `require` function takes in an argument which can be an ID or a path. The ID refers to the id (or name) of the module needed. You should provide ID as an argument when you are using the third-party modules or core modules provided by the Node Package Manager. On the other hand, when you have custom modules defined by you, you should provide the path of the module as the argument. You can read more about the require function from [this](https://nodejs.org/api/modules.html#modules_require_id) link.

Because you’ve already defined a custom module named `circle`, you’ll provide the path as an argument to the `require` function.

_app.js_

If you notice clearly, the dot at the start of the path means that it is a relative path and that the modules `app` and `circle` are stored at the same path.

Let’s log on to the console the `circle` variable, which contains the result returned by the `require` function. Let’s see what is contained inside this variable.

_app.js_

Check the output by saving all your code and running the following command in your Terminal (latter isn’t required if you have `nodemon` package installed):

```
node app
```

Output:

```
{ calculateArea: [Function: calculateArea],calculateCircumference: [Function: calculateCircumference] }
```

As you can see, the `require` function returns an object, the keys of which are the names of the variables/functions that have been exported from the required module (`circle`). In short, the `require` function returns the `module.exports` object.

Let’s now access the functions imported from the `circle` module.

_app.js_

Output:

```
Area = 200.96, Circumference = 50.24
```

What do you think will happen if I try to access the variable named `PI` defined in the `circle` module inside the `app` module?

_app.js_

Output:

```
Area = 200.96, Circumference = 50.24pi = undefined
```

Can you figure out why `pi` is `undefined`? Well, this is because the variable `PI` is not exported from the `circle` module. Remember the point where I told you that you cannot access the code written inside a module in another module for all the code written inside a module is private to it unless exported? Here, you are trying to access something which has not been exported from the `circle` module and is private to it.

So, you may be wondering why you didn’t get a `ReferenceError`. This is because you are trying to access a key named `PI` inside the `module.exports` object returned by the `require` function. You also know that the key named `PI` does not exist in the `module.exports` object.

Note that when you try to access a non-existent key in an object, you get the result as `undefined`. This is the reason why you get `PI` as `undefined` instead of getting a `ReferenceError`.

Now, let’s export the variable `PI` from the `circle` module and see if the answer changes.

_circle.js_

Notice that here, you are not using the name of the variable `PI` as the key of the property added to the `module.exports` object. You are, instead, using another name, which is `lifeOfPi`.

This is an interesting thing to note. When you are exporting some coding construct, you can give any name to the key when adding a property added to the `module.exports` object. It is not mandatory to use the same name as the name you used while defining the construct. This is because you can use any valid identifier as the key in a JavaScript object. Thus, on the left side of the assignment operator, you can use any valid identifier, but on the right side of the assignment operator, you need to provide a value which is defined as a construct in the scope of the current module (as you’ve defined the variables and functions in the ‘circle’ module).

An important point to be noted is that while importing something from another module in the current module, you need to use the same key which you used while exporting it.

_app.js_

Because you used the key `lifeOfPi`, you need to use the same key to access the variable `PI` defined in the `circle` module, as is done in the code given above.

Output:

```
Area = 200.96, Circumference = 50.24pi = 3.14
```

What do you think will happen if you use the name of the variable instead of using the key which was used while exporting? In short, let’s try to access `PI` (name of the variable) instead of `lifeOfPi` (key used while exporting `PI`).

_app.js_

Output:

```
Area = 200.96, Circumference = 50.24pi = undefined
```

This happens because the `module.exports` object does not know the variable `PI` anymore. It just knows about the keys added to it. Because the key used for exporting the variable `PI` is `lifeOfPi`, the latter can only be used to access the former.

### TL;DR

* Each file in Node.js is referred to as a _module_.
* Before executing the code written in a module, Node.js takes the entire code written inside the module and converts it into a function wrapper, which has the following syntax:

```
(function(exports, require, module, __filename, __dirname) { // entire module code lives in here});
```

* The function wrapper ensures that all the code written inside a module is private to it unless explicitly stated otherwise (exported). The parameters `exports`, `require`, `module`, `__filename`, and `__dirname` act as the variables global to the entire code in a module. Since each module has a function wrapper of its own, the code written inside one function wrapper becomes local to that function wrapper (read module) and is not accessible inside another function wrapper (read module).
* `module` keyword refers to the object representing the current module. The `module` object has a key named `exports`. `module.exports` is another object which is used for defining what can be exported by a module and can be made available to other modules. In short, if a module wants to export something, it should be added to the `module.exports` object.
* The default value of `module.exports` object is `{}`.
* There are three methods in which you can export something from a module, or add something to the `module.exports` object:  
1. Define all the constructs first and then use multiple `module.exports` statements where each statement is used to export a construct.  
2. Define all the constructs first and then use a single `module.exports` statement to exports all constructs at once following object literal notation.  
3. Add constructs to the `module.exports` object while defining them.
* `require` keyword refers to a function which is used to import all the variables and functions exported using the `module.exports` object from another module. In short, if a file wants to import something it has to declare it using the following syntax:

```
require('idOrPathOfModule');
```

* While exporting something from a module, you can use any valid identifier. It is not mandatory that you need to give the exact name of the variable/function as the key of the property added to `module.exports` object. Just make sure that you use the same key for accessing something which you used while exporting it.

