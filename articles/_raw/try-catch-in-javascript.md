---
title: Try/Catch in JavaScript – How to Handle Errors in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-30T16:59:00.000Z'
originalURL: https://freecodecamp.org/news/try-catch-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/neo-urban-1734495_1920-1.jpg
tags:
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Fakorede Damilola\nBugs and errors are inevitable in programming. A\
  \ friend of mine calls them unknown features :). \nCall them whatever you want,\
  \ but I honestly believe that bugs are one of the things that make our work as programmers\
  \ interesting. \n..."
---

By Fakorede Damilola

Bugs and errors are inevitable in programming. A friend of mine calls them **unknown features** :). 

Call them whatever you want, but I honestly believe that bugs are one of the things that make our work as programmers interesting. 

I mean no matter how frustrated you might be trying to debug some code overnight, I am pretty sure you will have a good laugh when you find out that the problem was a simple comma you overlooked, or something like that. Although, an error reported by a client will bring about more of a frown than a smile. 

That said, errors can be annoying and a real pain in the behind. That is why in this article, I want to explain something called **try / catch** in JavaScript.

## What is a try/catch block in JavaScript?

A **try / catch** block is basically used to handle errors in JavaScript. You use this when you don't want an error in your script to break your code. 

While this might look like something you can easily do with an **if statement**, try/catch gives you a lot of benefits beyond what an if/else statement can do, some of which you will see below.

```
try{
//...
}catch(e){
//...
}
```

A try statement lets you test a block of code for errors.

A catch statement lets you handle that error. For example:

```
try{ 
getData() // getData is not defined 
}catch(e){
alert(e)
}
```

This is basically how a try/catch is constructed. You put your code in the **try block**, and immediately if there is an error, JavaScript gives the **catch** statement control and it just does whatever you say. In this case, it alerts you to the error. 

All JavaScript errors are actually objects that contain two properties: the name (for example, Error, syntaxError, and so on) and the actual error message. That is why when we alert **e**, we get something like **ReferenceError: getData is not defined**. 

Like every other object in JavaScript, you can decide to access the values differently, for example **e.name**(ReferenceError) and **e.message**(getData is not defined).

But honestly this is not really different from what JavaScript will do. Although JavaScript will respect you enough to log the error in the console and not show the alert for the whole world to see :). 

What, then, is the benefit of try/catch statements?

## How to use try/catch statements

### The `throw` Statement

One of the benefits of try/catch is its ability to display your own custom-created error. This is called **`(throw error)`**. 

In situations where you don't want this ugly thing that JavaScript displays, you can throw your error (an exception) with the use of the **throw statement**. This error can be a string, boolean, or object. And if there is an error, the catch statement will display the error you throw. 

```
let num =prompt("insert a number greater than 30 but less than 40")
try { 
if(isNaN(num)) throw "Not a number (☉｡☉)!" 
else if (num>40) throw "Did you even read the instructions ಠ︵ಠ, less than 40"
else if (num <= 30) throw "Greater than 30 (ب_ب)" 
}catch(e){
alert(e) 
}
```

This is nice, right? But we can take it a step further by actually throwing an error with the JavaScript constructor errors.

Basically JavaScript categorizes errors into six groups: 

* **EvalError** - An error occurred in the eval function.
* **RangeError** - A number out of range has occurred, for example `1.toPrecision(500)`. `toPrecision` basically gives numbers a decimal value, for example 1.000, and a number cannot have 500 of that.
* **ReferenceError** -  Using a variable that has not been declared
* **syntaxError** - When evaluating a code with a syntax error
* **TypeError** - If you use a value that is outside the range of expected types: for example `1.toUpperCase()`
* **URI (Uniform Resource Identifier) Error** - A URIError is thrown if you use illegal characters in a URI function.

So with all this, we could easily throw an error like `throw new Error("Hi there")`. In this case the name of the error will be **Error** and the message **Hi there**. You could even go ahead and create your own custom error constructor, for example:

```
function CustomError(message){ 
this.value ="customError";
this.message=message;
}
```

And you can easily use this anywhere with `throw new CustomError("data is not defined")`.

So far we have learnt about try/catch and how it prevents our script from dying, but that actually depends. Let's consider this example:

```
try{ 
console.log({{}}) 
}catch(e){ 
alert(e.message) 
} 
console.log("This should run after the logged details")
```

But when you try it out, even with the try statement, it still does not work. This is because there are two main types of errors in JavaScript (what I described above –syntaxError and so on – are not really types of errors. You can call them examples of errors): **parse-time errors** and **runtime errors or exceptions**. 

**Parse-time errors** are errors that occur inside the code, basically because the engine does not understand the code. 

For example, from above, JavaScript does not understand what you mean by **{{}}**, and because of that, your try / catch has no use here (it won't work). 

On the other hand, **runtime errors** are errors that occur in valid code, and these are the errors that try/catch will surely find.  

```
try{ 
y=x+7 
} catch(e){ 
alert("x is not defined")
} 
alert("No need to worry, try catch will handle this to prevent your code from breaking")
```

Believe it or not, the above is valid code and the try /catch will handle the error appropriately.

### The `Finally` statement

The **finally** statement acts like neutral ground, the base point or the final ground for your try/ catch block. With finally, you are basically saying **no matter what happens in the try/catch (error or no error), this code in the finally statement should run**. For example:

```
let data=prompt("name")
try{ 
if(data==="") throw new Error("data is empty") 
else alert(`Hi ${data} how do you do today`) 
} catch(e){ 
alert(e) 
} finally { 
alert("welcome to the try catch article")
}
```

### Nesting try blocks

You can also nest try blocks, but like every other nesting in JavaScript (for example if, for, and so on), it tends to get clumsy and unreadable, so I advise against it. But that is just me.

Nesting try blocks gives you the advantage of using just one catch statement for multiple try statements. Although you could also decide to write a catch statement for each try block, like this:

```
try { 
try { 
throw new Error('oops');
} catch(e){
console.log(e) 
} finally { 
console.log('finally'); 
} 
} catch (ex) { 
console.log('outer '+ex); 
}
```

In this case, there won't be any error from the outer try block because nothing is wrong with it. The error comes from the inner try block, and it is already taking care of itself (it has it own catch statement). Consider this below:

```
try { 
try { 
throw new Error('inner catch error'); 
} finally {
console.log('finally'); 
} 
} catch (ex) { 
console.log(ex);
}
```

This code above works a little bit differently: the error occurs in the inner try block with no catch statement but instead with a finally statement.

Note that **try/catch** can be written in three different ways: `try...catch`, `try...finally`, `try...catch...finally`), but the error is throw from this inner try. 

The finally statement for this inner try will definitely work, because like we said earlier, it works no matter what happens in try/catch. But even though the outer try does not have an error, control is still given to its catch to log an error. And even better, it uses the error we created in the inner try statement because the error is coming from there. 

If we were to create an error for the outer try, it would still display the inner error created, except the inner one catches its own error. 

You can play around with the code below by commenting out the inner catch.

```
try { 
try { 
throw new Error('inner catch error');
} catch(e){ //comment this catch out
console.log(e) 
} finally { 
console.log('finally'); 
} 
throw new Error("outer catch error") 
} catch (ex) { 
console.log(ex);
}
```

### The Rethrow Error

The catch statement actually catches all errors that come its way, and sometimes we might not want that. For example,

```
"use strict" 
let x=parseInt(prompt("input a number less than 5")) 
try{ 
y=x-10 
if(y>=5) throw new Error(" y is not less than 5") 
else alert(y) 
}catch(e){ 
alert(e) 
}
```

Let's assume for a second that the number inputted will be less than 5 (the purpose of **"use strict"** is to indicate that the code should be executed in "strict mode"). With **strict mode**, you can not, for example, use undeclared variables ([source](https://www.w3schools.com/)). 

I want the try statement to throw an error of **y is not...** when the value of y is greater than 5 which is close to impossible. The error above should be for **y is not less...** and not **y is undefined**. 

In situations like this, you can check for the name of the error, and if it is not what you want, **rethrow it**:

```
"use strict" 
let x = parseInt(prompt("input a number less than 5"))
try{
y=x-10 
if(y>=5) throw new Error(" y is not less than 5") 
else alert(y) 
}catch(e){ 
if(e instanceof ReferenceError){ 
throw e
}else alert(e) 
} 

```

This will simply **rethrow the error** for another try statement to catch or break the script here. This is useful when you want to only monitor a particular type of error and other errors that might occur as a result of negligence should break the code.

## Conclusion

In this article, I have tried to explain the following concepts relating to try/catch:

* What try /catch statements are and when they work
* How to throw custom errors
* What the finally statement is and how it works
* How Nesting try / catch statements work
* How to rethrow errors

Thank you for reading. Follow me on twitter [@fakoredeDami](https://twitter.com/fakoredeDami).

