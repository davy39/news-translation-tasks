---
title: How to Debug Errors in Your Source Code
subtitle: ''
author: Mabel Obadoni
co_authors: []
series: null
date: '2023-02-24T23:37:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-errors-in-your-source-code
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Errors.png
tags:
- name: debugging
  slug: debugging
- name: error handling
  slug: error-handling
seo_title: null
seo_desc: "The process of handling errors is known as debugging. It involves identifying\
  \ and removing errors from your program. \nIf you want to be an efficient programmer,\
  \ you'll want to cultivate your ability to debug code. It's one of the main skills\
  \ you'll n..."
---

The process of handling errors is known as debugging. It involves identifying and removing errors from your program. 

If you want to be an efficient programmer, you'll want to cultivate your ability to debug code. It's one of the main skills you'll need as a software developer or programmer. This means you need to learn all about errors, too. 🤷

Errors can come in many forms – from as little as an omission of a semicolon to as huge as a crashed database. They're all part of the bittersweet experience of programming.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-126.png)

Regardless of your stage in programming, you most likely will come across at least one type of error while coding. The error could come up during writing code, running it, or even testing it. And there's usually a specific remedy to each error. This implies that not all errors are handled or solved the same way.

Errors in programming are also referred to as bugs. These bugs prevent your program from doing what it's instructed. Once you have a grasp of common errors, you'll be able to figure out the right treatment for the error you're experiencing. 

To debug errors in your source code, you'll need to understand:

* The sources of the errors in your code – What exactly is the cause of the errors displaying?
* The types of errors –Now that I have an error, what type is it? What should I do to clear these red lines off my screen?

This article will focus on how to answer these questions.

## **Where Do Errors Come From in Coding?**

The first step in finding a solution is knowing exactly the source of the problem. This will guide you in suggesting or building a solution. When writing your code in whatever programming language you use, errors can occur due to different factors.

The main sources of error include:

### Human Errors

Even though Artificial Intelligence plays a larger and larger role in many operations, the fact remains that humans still write source code. 

Errors caused by omission, knowledge gaps, or the lack of proper structure come from the developer. 

When a developer lacks the technical knowledge of the syntax of a particular language, there's bound to be errors in the source code. Or if they mean one thing and write another in code, the conflict in logic will always result in an error.

So, before you venture into coding in any language, make sure you understand the structure behind it and the rules that govern its programs. This will help you write fewer errors into your code that you then have to debug.

### Machine Errors 

For issues such as low memory, little storage space, and slow CPU processing speed, the machine also plays a role in causing errors. In fact a machine with a slow memory can cause runtime errors (errors due to slow code execution).

When getting a computer, if you're able, make sure to get one that matches up to the tasks you'll send its way. You should also use cloud storage and other cloud operations to reduce the risks of errors caused by your machine.

### Procedural Errors

Solving a problem requires following certain methods. Programming has its underlying methodology which you should follow whenever possible. 

This is why standard bodies exist, such as the World Wide Web consortium. It ensures that certain standards are followed when developing programs. 

Errors can occur when you ignore the standard methods entirely and try to maneuver your own way. Such code may not go beyond your machine as it may not be production worthy.

Study the procedures for building and operating the solution you are coding and try to follow them.

## **Types of Coding Errors**

Errors can occur regardless of your skill in programming. Your coding prowess is displayed when you can confidently decipher the error message and figure out what type of error occurred. 

Many programming languages have similar structures, especially Object Oriented Programming languages (such as Python and JavaScript). These similarities in structure means that they also have similar error patterns. 

In programming, the most common errors are:

### Syntax Errors

The word "syntax" simply means arrangement. In programming, syntax is the arrangement of the code following a set of rules or patterns. 

Just like in the English language where the letters are arranged from A - Z, programming languages also have their syntax you'll need to follow so the program runs seamlessly. 

When you're writing in English, for example, if you don't follow the grammar and syntax rules of the language, your words won't make a lot of sense. The same is true in programming: if you don't adhere to the syntax rules of the programming language, you'll get a **Syntax Error.**

Therefore, a syntax error is that error caused by disobeying the rules guiding a particular language. And the error message that pops up prevents your program from running.

Syntax Errors can be caused by various factors such as incorrect spelling, omitted punctuation, wrong use of quotes (" "), incorrect declaration of variables and values, and more.

As small as these errors may seem, they can break your source code if not properly solved. When any of these syntax errors occur, your compiler responds in two ways:

* **It highlights the code line where the error has occurred:** This will help you know the exact spot to check for your mistake.
* **It gives at least** a **one sentence explanation of the error type**.

In most cases, the compiler will indicate that it is a "Syntax Error" and sometimes point to what was omitted, included, or misplaced. Here's an example:

```reactjs
// importing the required dependencies and components
import { BrowserRouter as Router, Route, Switch,Redirect } from 'react-router-dom';
import './App.css';
import Home from './components/Home';
import About from './components/About';
import Projects from './components/Projects';
import Contact from './components/Contact';
import Nav from './components/Nav';


function App() {
  return (
    <div className='App'>
      <Router>
        {/* <Nav /> */}
        <Switch>
          <Route exact path='/'  component={Home}/>
          <Route  path='/About'  component={About} />
          <Route path='/Projects' component={Projects} />
          <Route path='/Contact'  component={Contact} />
          <Redirect to ="/" />
        
        </Switch>
      </Router>  
    </div>
```

The above snippet is from a React.js project. According to React syntax, if you declare a component you must use it, otherwise it'll throw a syntax error as seen in the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/SC4.PNG)
_Syntax error_

In the example, the Nav component was declared in the set of import statements but it wasn't called in the routing statement. Because of this, it displays an error message in the terminal.

Beginners in programming often encounter syntax errors as they're learning – especially if you're juggling between two different languages at the same time. With consistent practice, you can get better at writing your source code that complies with the syntax rules of the language you're using. 

### Logic or Semantic Errors

Another word for logic is reasoning. Writing source code for any program requires a lot of reasoning. Remember that coding is a means of providing solutions to problems. So your solution must follow the logic that guides it.

Also referred to as a semantic error, a logic error is an error that occurs when a program outputs something different from what was intended. Whenever your program behaves in a way that's different from what you outlined it to do, you have encountered a logical error.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/SC21-1.png)

```python
import pandas as pd
import numpy as np
a = 5
b ="10"
print(c=a+b)

```

In the above example, it is clear that the compiler couldn't add a string and a number because the number in the string was not implicitly converted to the **int** datatype. 

You can also see that there is a syntax error in this program as well when you look at the **print()** statement. You can debug the logic error by converting the string to an integer datatype as show below:

```python
import pandas as pd
import numpy as np
a = 5
b = Int("10")
print(c=a+b)
```

Unlike a syntax error, a logic error may not prevent your program from running. Instead, it will run but display an incorrect output.

### What Causes Logic Errors?

**Wrong Declaration of Data Type:** Using the example above, the second variable is a string because of the quotes surrounding it. So, the compiler assumes that you want to place both variables side by side. So always make sure you're meticulous with your data type declaration and conversion.

**Incorrect sequence**: Say you were to write, "Code love I to". Well, this sentence makes no logical sense because the words are not placed in the proper order. 

The same goes for programming languages. When the code is not sequential, the compiler again assumes a meaning for your code and then gives you an output different from your expectations. 

For instance, a function (in JavaScript) that is declared locally will be available globally due to the semantics of JavaScript function scope. So, if you'd need that particular function all through your source code, it is better to declare it in a global scope.

Scope in JS simply means the location of a declared variable and how it can be accessed. A variable has a global scope if it can be accessed anywhere along the entire source code. A local variable is one limited to only the block within which it is declared. The difference between a global variable and a local variable is the accessibility.

```javascript
var age =prompt("Enter your age")

 if (age<18){
 console.log("you are a minor")
 }
 else{
 console.log("You are" + age + "years old")
 }
 
 
```

In the above code snippet, the variable "age" is globally declared that is why it can be called anywhere in the entire source code.

Incorrect Sequence is a logical error because variables must be rightly declared if they are to be used repeatedly. 

**Misplaced Conditional Statement, Boolean or Logical Expressions:** Logical expressions such as if-else, do-while, and the rest are the major causes of logical errors. When they're not properly placed, there's every tendency to get an incorrect output. Most programs rely a lot on logical expressions, so you need to know how to use them.

Logical errors can happen to anyone, regardless of skill level – just like all errors. So spend some time getting your logic right before you start coding. Some programmers go as far as drawing a schematic diagram to emphasize the logic they want for their program.

### Runtime Error

Every program has a certain amount of time it takes to execute. As a programmer, it is your duty to ensure that your program loads in the shortest possible time. 

Remember, a slow program won't do well in the marketplace. Nobody wants an application that "wastes" their time, right?

Runtime, in simple terms, is the time taken for a program to execute or run. You can have your code syntax well written following a specified logic and still encounter errors as or when your program executes. This problem is caused by a runtime error.

![APC Screen showing error alert](https://www.freecodecamp.org/news/content/images/2023/02/image-125.png)
_A PC Screen showing error alert_

As seen in the above picture, Runtime errors can occur while your program is being executed – the time between interpreting your codes and showing the required output.

These errors can be caused by a non-declared variable, a slow internet connection or many other reasons during the course of code execution.

```javascript
const country = "Nigeria"
let indp = 1960
	function Election(){
    if ( country == "Nigeria"){
    console.log ( country + "had her "+ "independence in " + indp)
    }
    }
election()

```

The above code will throw a runtime error because the function being called is different from the one declared.

#### How to solve runtime errors

The best way to resolve runtime errors is to address them based on their cause. For a non-declared variable, ensure that the variable is properly declared using the right syntax and that the declared variable is the same as that which is called, as illustrated in the code block below:

```javascript
let name = "Ayomide"
console.log (name + " " +" was my colleague")
```

In the case of low memory, clear your cache and refresh your browser or restart your computer. 

For poor internet connection, switch your internet service provider or close some opened tabs on your browser.

In severe cases, back up your source code and solve the hardware problem that your computer may be experiencing.

## **Conclusion**

Errors can occur in any program, no matter the skill of the programmer. What sets you apart is your ability to find and debug these errors.

The more errors you debug, the better you become at writing clean and performant code. Look out for the next error line and swing into action!  
  

