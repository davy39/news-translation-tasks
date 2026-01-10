---
title: Deep dive into Scope Chains and Closures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:18:03.000Z'
originalURL: https://freecodecamp.org/news/deep-dive-into-scope-chains-and-closures-21ee18b71dd9
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tFNnwdoFlSJ7QmF_
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Turney

  How Scope chain and closures work under the hood with examples.


  _Photo by [Unsplash](https://unsplash.com/@anuragvh?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Anurag Harishchandrakar on <a href="ht...'
---

By Kevin Turney

#### How Scope chain and closures work under the hood with examples.

![Image](https://cdn-media-1.freecodecamp.org/images/JC6Wko1HdOI-OS-znRe4GntOJVoHvbHE-8zc)
_Photo by [Unsplash](https://unsplash.com/@anuragvh?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Anurag Harishchandrakar</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Understanding Scope and Closures in JavaScript

To dig deep and get the information you need, think like a journalist. Ask the six main questions: who, what, why, where, when, and how. If you can answer all these on a particular subject, then you have garnered the essence of what you need to know.

Before we get to closures, we have to have an understanding of scope.

First, if you know what [[scope]] (double bracket scope) is, then this article isn’t for you. You have more advanced knowledge and can move on.

### The what…

What is **scope** and why does it matter?

> **_Scope is the context environment (also known as lexical environment) created when a function is written. This context defines what other data it has access to._**

Put another way, scope is about access. Does the function have the ability to look up a variable for execution or manipulation, which variables are visible?

There are two types of scope: local and global. Scope resolution, or finding what variables belong where, starts at the innermost context and proceeds outward until the identifier is found. Let’s start small…

```
var firstNum = 1;
```

```
function number() {  var secondNum = 2;  return firstNum + secondNum;}
```

```
number();
```

### The when, why and how… execution context

![Image](https://cdn-media-1.freecodecamp.org/images/UxvNw5GMNCWBibNq99xSI1iWoGnY-39EZipV)

When function is invoked, it forms a new execution context. What is an execution context? Well, just as we have two types of scope, we have two types of execution context. They are a global execution context and a function execution context.

The global context is always running. In the case of a browser environment, it only stops when the browser is closed. When we call a function, we place that function’s execution context on top of the global execution context. Hence the terminology we **stack** them.

JavaScript is a single threaded language, which means it can do only one thing at a time. When we call a function, the previous execution context is paused. The called function is on the top and it is then executed. When that finishes, it is popped off the stack and then the older execution context is resumed. This ‘stack’ of execution is what keeps track of the position of execution in our application. It also is important in looking up identifiers.

So now we have an execution context formed, what’s next?

#### **Each execution context has an associated variable object**

![Image](https://cdn-media-1.freecodecamp.org/images/fUmuSkkuMeZsJVFFqOMP6ViyoAyZxzcPhIbl)

First, an **Activation Object** (not accessible by code, yet operates in the background) is formed. It is associated with this execution context. This object holds all **declared variables**, **functions**, and **parameters** passed within that context (its scope or accessibility range).

Parameters to a function are implicitly defined. They are “local” to that function’s scope. These declared variables are “hoisted”, taken to the top of the scope that they belong to.

Before I go further, to avoid confusion — in the global execution context, a **Variable Object** is created, and if it is a function, it is an **Activation Object**. They are pretty much identical.

![Image](https://cdn-media-1.freecodecamp.org/images/lPIm2hQe6Qz9ZTByQxWx9S8-qj93KbtRQ66G)

Now when this function is invoked, a “scope chain” of these objects is created. Why? The scope chain is a way to link or provide a systematic access to all variables and other functions that the current execution context (function in this case) has access to. [[Scope]] is the hidden mechanism that links these variable objects for identifier lookup. This hidden [[Scope]] is a property of the function, created at declaration, not invocation.

At the head of the scope chain train, if it is a function, is the **Activation Object**. This activation object has it’s own declared variables, arguments, and this.

Next, on the scope chain, is the next object from the containing context. If it is a global variable it is a **Variable Object.** If it is a function, it is an **Activation Object**. This happens until we reach the global context. That is why you can see we start from the innermost context to the outermost, think Russian nesting dolls.

What is the difference between a variable that is declared and one that is undeclared? If the identifier is preceded by a var, let, or const, it is declared explicitly and memory space is allocated for that variable’s use. If the identifier is not explicitly declared, then it is implicitly declared in the global scope which we will explore shortly. For purposes of this article, I’m sticking with var, no particular reason.

I know, the above was a little technical, and to be honest as I wrote this, I only learned of the Variable and Activation objects myself. Now that you had the deep dive explanation, here’s a high angle description…

The scope chain is similar to the prototype chain. If a variable or property is not found, it continues up the chain until it is either found or a error is thrown. The function creates a hidden [[scope]] property. This property links innermost scopes to outermost scopes. In this case, number’s scope chain is linked to the global window object (the containing context that holds function number). This is what allows the engine to look outside of function number to find firstNum and secondNum.

For example, let’s take the same function number and change one thing:

```
// global scope  - includes firstNum, secondNum, and the// function number
```

```
var firstNum = 1;
```

```
function number() {    // local scope for number - only thirdNum is local to number()    // because it was explicitly declared. secondNum is implicitly declared in the    // the global scope.
```

```
secondNum = 2;    var thirdNum = 3;    return firstNum + secondNum;  }// what do we have access to in the global scope?number(); // 3firstNum; // 1secondNum; // 2thirdNum; // Reference Error: thirdNum is not defined
```

![Image](https://cdn-media-1.freecodecamp.org/images/mZ88I9Xu0AfpjMKHwLSdNTEOUMdwg6DYfFgy)

When speaking of global scope, variable declarations, non-nested function declarations, and function expressions (still considered a variable definition) are considered in the scope of the global window object in the browser. So as we see above, the window object has a properties firstNum, secondNum, and number added to it. If we proceed along the scope chain looking for it, we keep looking until we reach the global context’s variable object. If it’s not in there, then we get the Reference Error.

```
In a new tab, type "about:blank" in the search bar. A blank page will open and hit cmd-option-i to open dev tools.
```

```
Type the code above and remember, shift-enter for a new line!
```

```
Now type "window" and explore all the properties on the window object.
```

```
Look closely and you will see the properties firstNum, secondNum, and number are all available on the window object.
```

When we try to access thirdNum outside of where it was declared, we get a Reference Error. The engine that compiles the code failed to find an identifier in the window global scope object.

ThirdNum is only available inside of the function where it was declared. It is encapsulated or private to function number

The question you may have is “Does the global scope has access to everything inside of number?” Again, scope only works from the inside out, the innermost context, local, to the outermost context, global.

Starting with local scope, we can say that data and variables that are wrapped in a function are only accessible to members of that function. The scope chain is what links firstNum to number().

When number() is invoked, the non-technical conversation goes like this…

> **_Engine:_** _“Number, I’m giving you a new execution context. Let me find what you need to run”_

> **_Engine_**_: “Ok, I see that thirdNum is explicitly declared. I’m setting space aside for you, go to the top of number’s function block and wait till I call you…_

> **_Engine_**_: “Number, I see secondNum, does he belong to you?”_

> **_Number_**_: “Nope.”_

> **_Engine_**_: “Ok, I see you’re linked to the global window object, let me look outside of you.”_

> **_Engine_**_: “Window, I have an identifier named secondNum, does he belong to you?”_

> **_Window_**_: “He didn’t declare himself explicitly in Number with a var, let, or_  
> _const, so I’ll take him and set space aside.”_

> **_Engine_**_: “Cool. Number, I see firstNum in your function block, does he belong to you?”_

> **_Number_**_: “Nope.”_

> **_Engine_**_: “Window, I see firstNum being used inside of Number, he needs him, does he belong to you?”_

> **_Window_**_: “Yes, he was declared.”_

> **_Engine_**_: “Everyone is accounted for, Now I’m assigning values to variables.”_

> **_Engine_**_: Number, I’m executing you, ready, go!”_

That’s pretty much it for understanding scope, The key takeaways are:

1. Identifier lookup works from the inside out and stops at the first match.
2. There are two types of scope, global and local
3. The scope chain is created at function invocation and is based on where variables and/or blocks of code are written (lexical environment). Are variables or functions nested?
4. In JavaScript, if an identifier is not proceeded with a var, let, or const, it is implicitly declared in the global scope.
5. Scope does not go 1 for 1 with a function, it goes 1 to 1 with function invocation. Execute a function 3 times, get 3 different scopes. Why? Because if the execution of a function is finished, it is popped off the execution stack and with it, its access to other variables via its scope chain. Thus, a new scope is created each time a function is executed. Closures work a little differently!

Let’s finish up with a more complex example before we move on to closures.

```
a = 1;var b = 2;
```

```
function outer(z) {  b = 3;  c = 4;  var d = 5;  e = 6;
```

```
function inner() {    var e = 0;    d = 2 * d;    return d;  }  return inner();  var e;}outer(1);
```

1. Before we run anything, hoisting is started at the outside, global level. Therefore we start with a declaration for a **variable** **b**, and a function declaration for **function object outer**. At this point nothing is assigned, we only have these two keys set up in the global scope variable object.
2. Next, we start at **a = 1.** This is an assignment, or a “write to” statement, yet there is no formal declaration for it. So what happens in the global scope, and if not in “strict mode”, is that **a** will be implicitly declared as belonging to the global scope variable object.
3. We move to the next line and look up identifier **b**, through hoisting it was accounted for and now we can assign a value, 2, to it.

So far we have…

#### Global Scope

![Image](https://cdn-media-1.freecodecamp.org/images/WS9msWmNLLYx50YR5DCjUfXfKMs-GIrr424a)

4. Since we built the **function object outer**, at hoisting time, we then jump to execution, outer(1);

5. Remember that upon function invocation, an execution context is first created. With that we create an Activation Object. It contains data and variables local to that context. We also form the scope chain.

6. The parameter **z** is implicitly declared for this function and is assigned 1.

A quick side note: at this time, the function’s execution context creates its “**this**” binding. It also creates an **arguments array**, which is an array of parameters passed, in this case, z. **This** is beyond the scope of this article, so allow me to glance over it.

7. Now we look for explicit variable declarations in **function outer**. We have **d**, and **var e** is declared after the **function inner**.

8. Here’s some hidden magic, **at this time a hidden [[scope]] property for function outer links its scope chain of variable objects. In this case, it works like a Linked List with a parent type property connecting the function outer Activation Object to the global execution context’s Variable Object.** You can see here that scope extends from the inside out to form this “linking”. This is the reference that allows us to proceed up the scope chain for lookups.

#### Scope for Function outer

![Image](https://cdn-media-1.freecodecamp.org/images/cv8nLf3vH0T-8NFBDzxDArKSAL7n5gnLIn7w)

9. We step inside of **outer** and start at **b** = 3. Is **b** declared? Nope. So JavaScript uses the hidden **[[scope]]** property attached to function **outer** to move up the scope chain to find a “**b**”. It finds it in the global scope object and, since we are in the body of function **outer**, we assign **b** the value 3.

#### Global Scope again

![Image](https://cdn-media-1.freecodecamp.org/images/qpQb0nuu7Y1WbN3MJwp9ermPDVShi8R9u9Sj)

10. Next line, **c** = 4. Since this is a write to identifier **c**, was **c** explicitly declared in function **outer**? No, and therefore it is not found by lookup in outer’s Activation Object. So it moves up the scope chain and looks in the global scope Variable Object. It is not there. Because this is a write to/ assignment operation, the global scope will handle it and place it on its Variable Object.

#### Global Scope Variable Object

![Image](https://cdn-media-1.freecodecamp.org/images/kLw4Ge1eryBuP1xrBetBMr8EX9KtPsCmmjBk)

11. **d** = 5. Yes, it is here so we assign it 5.

#### Scope for function outer

![Image](https://cdn-media-1.freecodecamp.org/images/rCC-QbTSWgdHODOvdaCuvVt39-kqwO2qCnpF)

12. **e** = 6. Remember that straggler, var **e**? It was still declared in the body of **outer** and so we already had a place for it — so we assign it 6. If it wasn’t declared like **c**, we would move up the scope chain for a lookup. Since it is a write and not a read operation and not in ‘strict mode’, it would have been placed in the global’s scope.

13. We get to invoking function **inner**. We start all over like we did with function **outer:** hoisting, set up an Activation Object, and create a hidden **[[scope]]** property. In this case, the containing context is function **outer**, and **outer** “points” to the global scope.

#### Scope for function inner

![Image](https://cdn-media-1.freecodecamp.org/images/uM9gVd9l86C9w6eMypi55J1Xxi0f0CaThFSv)

14. Now with **e** and in general, variables that are given the same name work like this. Since identifier lookup starts from the innermost scope to the outermost scope, lookup stops at the first finding of that identifier. In the body of **inner,** we see var **e**= 0, done, stop, go no further. The **e** in the body of function **outer** is “inaccessible”. The term that is commonly used is “shadowing” **e** in function **inner** “shadows” or obscures the **e** in function **outer**.

15. Next line is **d** = 2 * **d**. Before we assign a value to **d** on the left, we have to evaluate the expression on the right, 2 * **d**. Since **d** is not local in scope to **inner**, we move up the scope chain to find a variable for **d** and whether it has a value associated with it. We find it in the **outer** scope in function **outer** and it is there that the value is changed.

#### Scope for function outer

![Image](https://cdn-media-1.freecodecamp.org/images/UfIUjuTpQ3t3JGOHDPpY0rxS6ZvpCHz0Eleo)

The important thing here is that **inner is manipulating data in its outer scope!**

16. Function **inner** returns a value **d**, 10.

17. Function **outer** returns the value of function **inner**.

18. Result is 10.

19. Once function **outer** has completely finished executing, **garbage collection** takes place. Garbage collection is the freeing up of resources that are longer needed. It starts at the global scope and works as far as it has “reachability”.

The global scope in this example has no handle to function **outer** or function **inner**, so whoosh, gone. This is important when we get to closures, because there, we need data and some variables to stick around even after a function has finished running.

### Finally, let’s get some Closure!

#### How shall we define a closure?

Let’s start with a few definitions, all correct, some more in depth, but that get to the same point.

```
1. Closures are functions that have access to variables from another function's scope. This is accomplished by creating a function inside another function.
```

```
2. A Closure is a function that returns another function.
```

```
3. A Closure is an implicit, permanent link between a function and its scope chain.
```

#### Why Closures?

Without being able to leverage scope chain rules, async operations would be impossible. Because there is no guarantee that data will still be around to use later. JavaScript only has function scope as its encapsulation mechanism.

Closures are the best form of privacy for functions and variables. This is evident in the use of many module patterns. A module pattern returns an object to expose a public API. It also keeps other methods and variables private. Closures are used in event handling and callbacks.

An example of a module …

```
var Toaster = (function(){    var setting = 0;    var temperature;    var low = 100;    var med = 200;    var high = 300;    // public    var turnOn = function(){        return heatSetting();    };    var adjustSetting = function(setting){        if(setting <= 3){            temperature = low;        }if (setting >3  && setting <= 6){            temperature = med;        }if (setting > 6 && setting <= 10){            temperature = high;
```

```
}return temperature;    };    // private    var heatSetting = function(adjustSetting){        var thermostat = adjustSetting;        return thermostat;        };    return{            turnOn:turnOn,            adjustSetting:adjustSetting        };})();
```

```
Toaster.adjustSetting(5);Toaster.adjustSetting(8);
```

The module Toaster has private locals and a public interface and is written as an Immediately Invoked Function Expression (IIFE). We create a function, immediately invoke it, and grab the return value.

Another small example:

```
function firstName(first){    function fullName(last){        console.log(first + " " + last);    }    return fullName;}var name = firstName("Mister");name("Smith") // Mister Smithname("Jones"); //Mister Jones
```

The inner function fullName( ) is accessing the variable, first, in its outer scope, firstName( ). **Even after the inner function, fullName, has returned, it still has access to that variable**. How is this possible? The inner function’s scope chain includes the scope of its outer scope.

When a function is called, an execution context and a scope chain are created. Also the function get’s a hidden [[Scope]] property. The Activation Object for the function is initialized and placed in the chain. Then the outer function’s activation object is placed in the chain. In this case, finally the global **Variable Object**.

In this example, fullName is defined. A [[Scope]] property is created. The containing function’s activation object is added to fullName’s scope chain. It is also added to the global variable object. This reference to an outer function’s activation object enables access to all of the containing scopes variables. It does not get garbage collected.

**This is most important. The activation object of the outer function, firstName(), cannot be destroyed once it is finished executing, because the reference still exists in fullName’s scope chain. After firstName( )**  
**execution completes, its scope chain for that execution context is destroyed. But the activation object will remain in memory until fullName( ) is destroyed.** We can do that by setting its reference to null.

The keen observer will note that we return a reference to fullName, not the return value of fullName( )!

This is what we mean by an implicit, permanent link between and function and it’s scope chain.

A closure always gets the last value from the containing function because the reference to the variable object is stored.

For instance …

```
var myFunctions= [];function createMyFunction(i) {    return function() {           console.log("My value: " + i);            };        }for (var i = 0; i < 10; i++) {myFunctions[i] = createMyFunction(i);myFunctions[i]();}
```

```
My value: 0 My value: 1 My value: 2 My value: 3 My value: 4 My value: 5 My value: 6 My value: 7 My value: 8 My value: 9
```

If we go back to our original scope example and change one thing:

```
a = 1;var b = 2;
```

```
function outer(z) {  b = 3;  c = 4;  var d = 5;  e = 6;
```

```
function inner() {    var e = 0;    d = 2 * d;    return d;  }  return inner; // we remove the call operator, now we are returning a reference to function inner.  var e;}myG = outer(1); // store a reference to function inner in the global scope (the return value of outer)myG(); // when we execute myG, inner's [[Scope]] property is copied to recreate the scope chain,    //  and that gives it access to the scopes that contain function inner, outter then global. We got inner and inner's got outter.
```

Here are a few more examples:

```
function make_calculator() {    var n = 0;  // this calculator stores a single number n    return {      add: function(a) { n += a; return n; },      multiply: function(a) { n *= a; return n; }    };}
```

```
first_calculator = make_calculator();second_calculator = make_calculator();
```

```
first_calculator.add(3);                   // returns 3second_calculator.add(400);                // returns 400
```

```
first_calculator.multiply(11);             // returns 33second_calculator.multiply(10);            // returns 4000
```

Suppose we wanted to execute an array of functions:

```
function buildList(list) {    var result = [];    for (var i = 0; i < list.length; i++) {        result.push(function number(i) {          var item = 'item' + list[i];          console.log(item + ' ' + list[i])} );    }    return result;}buildList([1,2,3,4,5]);
```

```
function testList() {     var fnlist = buildList([1,2,3,4,5]);     for (var i = 0; i < fnlist.length; i++) {       fnlist[i](i); // another IIFE with i passed as a parameter!!     } } testList();
```

I hope that this explanation of scope and closures helps. Play around with the patterns you see here, experiment. Actually writing this article was difficult — I gained a far deeper understanding than I had when I started.

### Resources

[YDKJS](https://github.com/getify/You-Dont-Know-JS/tree/master/scope%20%26%20closures)

[Dmitry Soshnikov, Javascript:Core](http://dmitrysoshnikov.com/ecmascript/javascript-the-core/#variable-object)

[ECMA 262.3](http://dmitrysoshnikov.com/ecmascript/chapter-2-variable-object/)

[StackOverflow](https://stackoverflow.com/questions/111102/how-do-javascript-closures-work)

[Nick Zakas](https://www.amazon.com/Professional-JavaScript-Developers-Nicholas-Zakas/dp/1118026691)

