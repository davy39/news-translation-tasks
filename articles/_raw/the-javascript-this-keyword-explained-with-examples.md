---
title: The JavaScript this Keyword Explained with Examples
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2024-06-05T14:58:48.000Z'
originalURL: https://freecodecamp.org/news/the-javascript-this-keyword-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Python-Data-Types--3-.png
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'All leading web browsers support JavaScript, a popular and versatile programming
  language. The this keyword is a very important concept to know in JavaScript.

  The this keyword is a reference to an object, but the object varies based on where
  and how ...'
---

All leading web browsers support JavaScript, a popular and versatile programming language. The `this` keyword is a very important concept to know in JavaScript.

The `this` keyword is a reference to an object, but the object varies based on where and how it is called.

In this article, you'll learn how to implicitly (based on context) and explicitly (using the `call()`,  `apply()`, and `bind()` methods) determine the value of the `this` keyword. 

Here are the topics we will be covering:

* [What are the Rules that Guide the Behavior of the `this` keyword](#heading-what-are-the-rules-that-guide-the-behavior-of-the-this-keyword)?
* [What is the `call()` Method in JavaScript](#heading-what-is-the-call-method-in-javascript)?
* [What is the `apply()` Method in JavaScript](#heading-what-is-the-apply-method-in-javascript)?
* [What is the `bind()` Method in JavaScript](#heading-what-is-the-bind-method-in-javascript)?
* [Why were the `call()`, `apply()`, and `bind()` Methods Introduced to JavaScript?](#heading-why-were-the-call-apply-and-bind-methods-introduced-to-javascript)
* [What are the Differences Between the `call()`, `apply()`, and `bind()` Methods?](#heading-what-are-the-differences-between-the-call-apply-and-bind-methods)
* [Why Use the `call()`, `apply()`, and `bind()` Methods in Javascript?](#heading-why-use-the-call-apply-and-bind-methods-in-javascript)

## What are the Rules that Guide the Behavior of the `this` keyword?

Some rules guide the behavior of  the `this`  keyword in JavaScript. They are the global scope, function context, object method, constructor, and event handlers.

### Global Scope

Whenever the `this` keyword is used outside of any function, it refers to the global object. 

While the global object is `global` in the Node.js environment, it's a `window` in the context of a web browser:

```javascript
console.log(this);

```

![bind 1](https://hackmd.io/_uploads/Hy3UshesT.png)
_Global Scope Result_

The result from the code above shows that `this` returns the `window`, which is the global object for the web browser.

### Function Context

The method of invocation determines the value of the `this` keyword in a standard regular function:

```javascript
function saySomething() {
  console.log(this)
}

saySomething()  // {window: Window, self: Window, document: document, name: '', location: Location, …}

```

![bind 1](https://hackmd.io/_uploads/H1oponlia.png)
_Function context result_

The above code result is the global object for the web browser.

### Object Method

Methods are function-holder properties of an object. In JavaScript, they allow an object to manipulate its properties using `this` keyword:

```javascript
const club = {
  name: "Arsenal",
  yearFounded: "1989",
  details() {
    return `Hey, ${this.name} ${this.yearFounded}`;
  },
};

console.log(club.details()); // Arsenal , 1989

```

In the context of the above code, `this` refers to the `club`. As you can see from the output, it says `Arsenal 1989`.

But we would have a different result if we created a new variable for the details method, as shown below:

```javascript
const club = {
  name: "Arsenal",
  yearFounded: "1989",
  details() {
    return `Hey, ${this.name} ${this.yearFounded}`;
  },
};

const full = club.details;
console.log(full()); // Hey,  undefined

```

Although the `details()` method was defined inside the `club` object, it's not expressly bound to it. We call the `details()` as a method on the object.

In JavaScript, a method gets the value of `this` when it looks at the function that comes before the dot.

### Constructor Function

It's not news that the function constructor was the default initializer for user-defined objects before the introduction of the ECMAScript 2015 update.

The `new` keyword creates an instance of a constructor function:

```javascript
function Country(name) {
  this.name = name;
  this.age = 1960;

  this.info = function () {
    console.log(`${this.name} was founded ${this.age} years ago`);
  };
}

const country = new Country("Nigeria");
console.log(country.name);
console.log(country.info());

```

![nigeria](https://hackmd.io/_uploads/Skn8R3eip.png)
_Constructor function result_

The `this` refers to the newly created object, in this case, the instance of the country.

### Event Handlers

In an `addEventListener` event handler,  `this` refers to the element before the dot. This is the element that the event listener was added to trigger the event:

```javascript
const button = document.querySelector("button");

button.addEventListener("click", function () {
  console.log(this);
});

// OUTPUT  <button>click</button>

```

Once the above code runs, a button with an `innerText` value of `click` will be logged to the console.

In all the above rules that guide the behavior of the popular `this` keyword, one thing is clear: the context determines the value of the `this` keyword.

Aside from implicitly determining the value of `this`, function methods like `call()`, `apply()`, and `bind()` can be used to explicitly determine what `this` should refer to.

## What is the `call()` Method in JavaScript?

The `call()` method is one of the most popular ways to explicitly define what `this` refers to.  In JavaScript, the `call()` method is mostly used to borrow a method from an isolated object and use it on another with a specific context.

The `call()` method requires its arguments to be passed one by one:

```javascript
const game = {
  title: "PrisonBreak",
  year: 1979,
};

function detail() {
  console.log(`${this.title}, was released in ${this.year}`);
}
detail();

// RESULT undefined was released in undefined

```

The above prints the result because there's no connection between the `game` and the `detail` method. Hence, calling the `detail` method by itself will only print `undefined`.

```javascript
const game = {
  fullDetail: function () {
    return this.title + " " + this.year;
  },
};

const newGame = {
  title: "Merlin",
  year: 1994,
};

const fullDetail = game.fullDetail.call(newGame);
console.log(fullDetail); // Output: Merlin 1994

```

In the code above, there are `game` and  `newGame` objects. The `game` has a `fullDetail` method, while the `newGame` has title and year has properties.

As we know from the definition above, the `call()` method used the context of `newGame` to invoke the `fullDetail` method of the `game` object.

This means that, we have access to the `newGame` properties because the `this` inside of `fullDetail` refers to `newGame` object.

We now have a connection between the `game` and the `newGame` with the help of the `call()` method.

Aside from passing `this` as an argument, there's provision for passing additional arguments individually:

```javascript
const game = {
  fullDetail: function (category) {
    return `${this.title} was released ${this.year}, and the film is a ${category} film`;
    return this.title + " " + this.year + " " + "category";
  },
};

const newGame = {
  title: "Merlin",
  year: 1994,
};

const fullDetail = game.fullDetail.call(newGame, "seasonal");

console.log(fullDetail); // Merlin was released 1994, and the film is a seasonal film


```

The above code shows the possibility of passing another argument aside `this` keyword.

### How to Use the call() Method in a Real World Application

<iframe height="300" style="width: 100%;" scrolling="no" title="call and apply javascript" src="https://codepen.io/kamal90/embed/gOygyaO?default-tab=js" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/kamal90/pen/gOygyaO">
  call and apply javascript</a> by kamaldeeen (<a href="https://codepen.io/kamal90">@kamal90</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

The following code was extracted from the code above:

```javascript
const newMovie = {
    info: {
      title,
      [extraName]: extraValue,
    },
    id: Math.random(),
    formatted() {
      return this.info.title.toUpperCase();
    }
  };

```

The above code is an object named `newMovie`. In the `newMovie` object, an `info` object with `title` and  `extraName` was created.

The `title` is the name of the movie, while the `[extraName]` line uses bracket notation to dynamically access the user input, using the value of the variable as the key name. While the `extraValue` is the value associated with the key.

The `id` is the unique identifier that generates a random number using the `Math.random()` function.

The `formatted()` method returns the uppercase format of the title. By using the `this.info.title`, where the `newMovie` object is the same as `this`, and the `info`is an object inside the `newMovie` that contains information like the title, and the rest.

```javascript

filteredMovies.forEach((movie) => {
    const newMovieEl = document.createElement('li');
    const {info} = movie;
    const {formatted} = movie
    let text = formatted.call(movie) + '-';
    for (const key in info) {
      if (key !== 'title') {
        text = text + `${key}: ${info[key]}`
      }
    }
    newMovieEl.textContent = text;
    movieList.append(newMovieEl)

  })
}

```

The above code shows the uses of the `call()` method in a real world application.

Let's explain what's happening in the code.

The line `const newMovieEl = document.createElement('li');` creates a new `<li>` element using `document.createElement('li')`, with the new element stored in the constant `newMovieEl`.

The line `const {info} = movie;` uses destructuring assignment to extract the `info` property from the movie object.

The line `const {formatted} = movie` uses destructuring assignment to extract the `formatted` method from the movie object.

The line `let text = formatted.call(movie) + '-';` shows how to use the `call()` method in an application.

Invoking the `formatted` function directly will not give the required result, as the function of `this` in that context is the window object.

By using the `call` method on the `formatted` function, the `call()` method allows the context of the `this` to change from the window object to the`movie` object.

As said above, in JavaScript, the `call()` method is used to borrow a method from an isolated object and use it on another with a specific context.

The `call()` method requires its arguments to be passed one by one, and executes the function instantly.

The line `for (const key in info) {if (key !== 'title') {text = text +` ${key}: ${info[key]}`}` iterates over each key in the info object and checks if the current key is not equal to `title`. It then appends the key-value pair to the text string.

The line `newMovieEl.textContent = text movieList.append(newMovieEl)` sets the text content of the newly created list item element to the generated text, and appends the newly created list item element to the parent element with the id `movieList`.

## What is the `apply()` Method in JavaScript?

The `apply()` method is similar to the `call()` method, with the only difference being that the `apply()` method takes arguments as an array (or array-like object), while arguments get passed individually to the `call()` method.

To get started with the `apply()` method, let's check its syntax:

```javascript
nameOfFunction.apply(thisArg, [argsArray])

```

The `nameOfFunction` is the function to be called, `thisArg` is the `this` value provided for the function, and the array or array-like object is the `argsArray` to be passed to the function.

```javascript
const game = {
  fullDetail: function () {
    return this.title + " " + this.year;
  },
};

const newGame = {
  title: "Merlin",
  year: 1994,
};

const fullDetail = game.fullDetail.apply(newGame);
console.log(fullDetail); // Output: Merlin 1994

```

Just as in the `call()` method, there are `game` , and `newGame` objects. The `game` has a `fullDetail` method, while the `newGame` has a title and year has properties.

As we know from the definition above, the `apply()` method used the context of `newGame` to invoke the `fullDetail` method of the `game` object.

This means that, we have access to the `newGame` properties because the `this` inside of `fullDetail` refers to the `newGame` object.

We now have a connection between the `game` and the `newGame` with the help of the `apply()` method.

The `apply()` method can also be used to pass an array or  array-like collection as an argument.

```javascript
const game = {
  fullDetail: function (greet) {
    return `${greet} ${this.title} ${this.year}`;
  },
};

const newGame = {
  title: "Merlin",
  year: 1994,
};

const fullDetail = game.fullDetail.apply(newGame, ["Welcome"]);
console.log(fullDetail); // Output: Welcome Merlin 1994

```

The above code shows that the `fullDetail` function inside the `game` object expects a `greet` parameter. The `apply()` method is used to invoke the `fullDetail` with the `newGame` object and the array `['Welcome']` as an argument passed to the function.

### How to Use the apply() Method in a Real World Application

<iframe height="300" style="width: 100%;" scrolling="no" title="Apply" src="https://codepen.io/kamal90/embed/GRLWYoN?default-tab=js" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/kamal90/pen/GRLWYoN">
  Apply</a> by kamaldeeen (<a href="https://codepen.io/kamal90">@kamal90</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

The following code was extracted from the code above:

```javascript
const newMovie = {
    info: {
      title,
      [extraName]: extraValue,
    },
    id: Math.random(),
    formatted() {
      return this.info.title.toUpperCase();
    }
  };

```

The above code is an object named `newMovie`. In the `newMovie` object, an `info` object with `title`,`extraName` was created.

The `title` is the name of the movie, while the `[extraName]` line uses bracket notation to dynamically access the user input, using the value of the variable as the key name. While the `extraValue` is the value associated with the key.

The `id` is the unique identifier that generates a random number using the `Math.random()` function.

The `formatted()` method returns the uppercase format of the title. By using the `this.info.title`, where the `newMovie` object is the same as `this`, and the `info`is an object inside the `newMovie` that contains information like the title, and the rest.

```javascript

filteredMovies.forEach((movie) => {
    const newMovieEl = document.createElement('li');
    const {info} = movie;
    const {formatted} = movie
    let text = formatted.apply(movie) + '-';
    for (const key in info) {
      if (key !== 'title') {
        text = text + `${key}: ${info[key]}`
      }
    }
    newMovieEl.textContent = text;
    movieList.append(newMovieEl)

  })
}

```

The above code shows the uses of the `apply()` method in a real world application.

Now, let's explain the code.

The line `const newMovieEl = document.createElement('li');` creates a new `<li>` element using `document.createElement('li')`, with the new element stored in the constant `newMovieEl`.

The line `const {info} = movie;`uses destructuring assignment to extract the `info` property from the movie object.

The line `const {formatted} = movie`uses destructuring assignment to extract the `formatted` method from the movie object.

The line `let text = formatted.apply(movie) + '-';`shows how to use the `apply()` method in an application.

Invoking the `formatted` function directly will not give the required result, as the function of `this` in that context is the window object.

By using the `apply` method on the `formatted` function, the `apply()` method allows the context of  `this` to change from the window object to `movie` object.

As said above, in JavaScript, the `apply()` method takes arguments as an array (or array-like object), and executes the function instantly.

The line `for (const key in info) {if (key !== 'title') {text = text +` ${key}: ${info[key]}`}`iterates over each key in the info object and checks if the current key is not equal to `title`.

It then appends the key-value pair to the text string.

The line `newMovieEl.textContent = text movieList.append(newMovieEl)` sets the text content of the newly created list item element to the generated text, and appends the newly created list item element to the parent element with the id `movieList`.

## What is the `bind()` Method in JavaScript?

The `bind()` method creates a new function that has its `this` keyword set to the provided value and does not immediately call the function.

It is available on all JavaScript functions and is used to permanently set the `this` context for a function.

The difference between the `call()`, `apply()`, and `bind()` methods is that, the `bind()` method creates a new function with a bound `this`,  while both `call()` and `apply()` are one time-time-use methods that don't create a new function.

The `bind()` method doesn't immediately call the function, but both `call()` and `apply()` call the function instantly.

Let's look at the syntax for the `bind()` method:

```javascript
functionName.bind(thisArg[, arg1[, arg2[, ...]]])

```

The `thisArg` represents the value to be passed as `this` value whenever the function gets executed, and the `arg1, arg2, ...` are the arguments bound to the function when it gets invoked.

```javascript

const player = {
  name: "Rooney",
  jerseyNumber: 10,
  introduction: function () {
    console.log(this.name + "wears Jersey number " + this.jerseyNumber + ".");
  },
};
const player2 = {
  name: "Jimmy ",
  jerseyNumber: 18,
};

let result = player.introduction.bind(player2);

result(); // Jimmy wears Jersey number 18.

```

In the above code, when you call `result()`, it prints `Jimmy wears Jersey number 18`. This is possible because the `this` keyword inside the introduction method is bound to the `player2` object.

It is also possible to use the `bind()` method with more than one argument.

```javascript
const player = {
  name: "Rooney",
  jerseyNumber: 10,
  introduction: function (goals, country) {
    console.log(
      `${this.name} wears Jersey number ${this.jerseyNumber}, he plays for ${country}, and he has scored ${goals} goals`,
    );
  },
};
const player2 = {
  name: "Jimmy ",
  jerseyNumber: 18,
};

let result = player.introduction.bind(player2, 87, "Nigeria");

result(); // Jimmy  wears Jersey number 18, he plays for Nigeria, and he has scored 87 goals

```

In the above example, two parameter were passed: `thisArg` and `arg1`. Then the `player2` object is bound to the `introduction` method which has two parameters: `goals` and `country`.

### How to Use the bind() Method in a Real World Application

For a proper understanding of how to use the `bind()` method in a real-world application, there's a need to show the application without the `bind()` method.

The unconventional calculator is the name of the application we will be building for this exercise.

<iframe height="300" style="width: 100%;" scrolling="no" title="Untitled" src="https://codepen.io/kamal90/embed/qBwRWwX?default-tab=js" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/kamal90/pen/qBwRWwX">
  Untitled</a> by kamaldeeen (<a href="https://codepen.io/kamal90">@kamal90</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Let's break down the code.

The above code creates a simple unconventional calculator with the aim of performing basic aritmhemetic operations (addition, subtraction, division, and multiplication).

It takes the user's input, updates the displayed result, and logs calculations.

* The `outputResult(answer, text)` function updates the result and the calculation text.
* The `getUserInput()` function retrieves the user's input from the input field.
* The task of the `writeToLog(operationidentifier, older, olderTwo, newResult)` is to format the calculation string for an output.
* The `createLog(operationidentifier, older, olderTwo, newResult)` function creates a log object for the calculation, and stores it in an array.
* The `createOutput(conditional)` performs the core calculation logic based on the provided operation. Operations like `add()`, `subtract()`, `divide()`, and `multiply()` trigger calculations for their respective operations.

Here is the code with the `bind()` function**:**

<iframe height="300" style="width: 100%;" scrolling="no" title="Unconventional Calculator" src="https://codepen.io/kamal90/embed/MWRjXWg?default-tab=js" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/kamal90/pen/MWRjXWg">
  Unconventional Calculator</a> by kamaldeeen (<a href="https://codepen.io/kamal90">@kamal90</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

The above code creates simple calculator functionality in JavaScript.

The code takes an input from the user, performs calculations based on button clicks, updates the UI with the results, and maintains a log of past calculations.

Let's break down the JavaScript code in the following sections.

#### Select all the HTML elements

The code selects all the HTML elements using their IDs.

The `addButton` , `subtractButton`, `divideButton`, and `multiplyButton`  are elements to display the calculation history.

The `result` is the element to display the current result and the `inputNumber`  is an input field for user input.

#### Create functions for output and user input

The `outputResult (answer, text)` function displays the provided answer in the `result` element and the text in the `calculation` element.

`getUserInput()` function gets the value entered in the `inputNumber` field and converts it to an integer.

#### Create variables for calculation and logging

`defaultResult` is a constant set to `0`, used as the initial result.

`currentResult` is a variable for storing the current result of calculations.

`logEntries` is an array that stores log entries for calculation history.

For logging functions, the `writeToLog(prevResult, operand, original)` function updates the UI with the calculation description and calls the `outputResult` function.

The `createLog (operationidentifier, older, olderTwo, newResult)` function creates a log entry object and pushes it to the `logEntries` array.

#### Create calculation function

The `calculate (operation)` takes an operation string as input ( `ADD` , `SUBTRACT`, `DIVIDE`, or `MULTIPLY`). It performs calculations based on the following operations:

It adds for `ADD`, subtracts for `SUBTRACT`, divides for `DIVIDE`, multiplies for `MULTIPLY`.

The `writeToLog` and `createLog` functions are called to log the calculation.

#### Create event listeners for buttons

The `addButton.addEventListener('click',calculate.bind(this, 'ADD')` assigns an event listener to the `addButton`.

Similar event listeners are assigned to the `subtractButton`, `divideButton`, and `multiplyButton` for their respective operations.

The code snippet indicates that the `calculate` function will be executed whenever a button is clicked. The function is bound with the `bind()` method, and arguments such as `ADD`, `SUBTRACT`, `MULTIPLY`, and `DIVIDE` are passed to the `calculate` function.

## Why were the `call()`, `apply()`, and `bind()` Methods Introduced to JavaScript?

With these methods, JavaScript applications are more dynamic and adaptable. It affords the programmer more control over how the function is executed.

It is generally hard to have a full grasp of the `this` keyword in JavaScript. Hence, the introduction of the `call()`, `apply()`, and `bind()` methods gives programmers more control over this quirky subject.

Say you are a versatile footballer who can comfortably play in different positions on the field. In a regular football match, your coach assigns a specific wing for you (the function) and you play according to the coach's instructions (the function's code), and the other footballers you are on the pitch with (the arguments).

With the `call()` method, your coach can temporarily put you in a different position on the pitch (set the `this` value) for a specific match. This lets you use your footballing skills even on the wing you wouldn't normally play.

With the `apply()` method, it is like having a whole football tactics (arguments) full of different technical fouls, delay tactics, and many more. The coach can throw the entire tactics at you, and you can use them all (function execution with a specific context) for the match.

With the `bind()` method, imagine your coach creating a special understudy role ( `bound()` function) just for you. This understudy role always has a specific wing on the pitch (predefined `this`) ready, so you can seamlessly step in and deliver the instructions (function execution) whenever needed.

## What are the Differences Between the `call()`, `apply()`, and `bind()` Methods?

When it comes to handling arguments:

* The `call()` method accepts arguments individually as a comma separated list.
* With the `apply()` method, the arguments are accepted as an array-like or an array object.
* The `bind()` method can pass in additional arguments when the new function is invoked.

When it comes to invocation and execution:

*  The `call()` method invokes the function immediately with the specific individual arguments and the specified `this` value, and it accepts argument one by one.
* The `apply()` method just like the `call()` method invokes the function instantly, but with difference being that it accepts arguments as an array or array like object.
* The `bind()` method creates a new function with an optional arguments and a specified `this` value. It doesn'timmediatley invoke the function, as it bound the functuion for a later execution.

## Why Use the `call()`, `apply()`, and `bind()` Methods in Javascript?

The `call()`, `apply()`, and `bind()` methods deal extensively with how to control the context of a function ( `this` keyword) and arguments when it's called.

There are several benefits attached to using these methods in JavaScript:

* **Change the value of the `this` keyword**: The `this` keyword refers to the object that calls a certain function. With the help of these methods, you can explicitly set the value of `this` keyword to something else.
* **Event Handling**: Both the `call()` and `apply()` methods can ensure that the handler is executed with the correct context and arguments, even if its definition space is different from the invocation space.
* **Flexible arguments**: These methods take arguments in a different way. The `call()` method takes an individual argument, the `apply()` method takes an argument as an array, and the `bind()` method allows for pre-setting some arguments for later use.
* **Partial function**: The `bind()` method creates a new function made up of a preset context and optional initial arguments. This is very useful for partial applications, where certain arguments are fixed ahead of time, with others to be provided at a later stage.
* **Borrowing Functions**: These methods use a function from a new object to another set of object entirely.

In a nutshell, they give you enough breathing space over how functions are executed in JavaScript.

## Conclusion

In this tutorial, you learned about how to implicitly (based on context) and explicitly (by using the `call()`, `apply()`, and `bind()` methods) determine the value of `this` keyword.


