---
title: How to Write Better React Components
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2021-01-20T19:07:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-better-react-components
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/modern_way-1.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'Many features were added to JavaScript in ES6. And these changes help developers
  write code that is short and easy to understand and maintain.

  When you use create-react-app to create a React App, you already have support for
  these changes. This is be...'
---

Many features were added to JavaScript in ES6. And these changes help developers write code that is short and easy to understand and maintain.

When you use [create-react-app](https://github.com/facebook/create-react-app) to create a React App, you already have support for these changes. This is because it uses Babel.js to convert the ES6+ code to ES5 code which all browsers understand.

In this article, we'll explore various ways we can write shorter, simpler and easier to understand React code. So let's get started.

Take a look at the below Code Sandbox demo:

%[https://codesandbox.io/s/quirky-chebyshev-zff8p]

Here, we have two input text boxes that take input from users, and two buttons that calculate the addition and subtraction of the numbers provided as input.

## Avoid manually binding event handlers

As you know in React, when we attach any `onClick` or `onChange` or any other event handler like this:

```js
<input
  ...
  onChange={this.onFirstInputChange}
/>

```

then, the handler function (onFirstInputChange) does not retain the binding of `this`.

This is not an issue with React, but that's how JavaScript event handlers work.

So we have to use the `.bind` method to correctly bind `this` like this:

```js
constructor(props) {
  // some code
  this.onFirstInputChange = this.onFirstInputChange.bind(this);
  this.onSecondInputChange = this.onSecondInputChange.bind(this);
  this.handleAdd = this.handleAdd.bind(this);
  this.handleSubtract = this.handleSubtract.bind(this);
}

```

The above lines of code will maintain `this`'s binding of the class correctly inside the handler functions.

But adding a new binding code for every new event handler is tedious. Luckily we can fix it using the class properties syntax.

Using class properties allows us to define properties directly inside the class.

Create-react-app internally uses the `@babel/babel-plugin-transform-class-properties` plugin for Babel version >= 7 and `babel/plugin-proposal-class-properties` plugin for Babel version <7  so you don't have to manually configure it.

To use it, we need to convert the event handler functions to arrow function syntax.

```js
onFirstInputChange(event) {
  const value = event.target.value;
  this.setState({
    number1: value
  });
}

```

The above code can be written as follows:

```js
onFirstInputChange = (event) => {
  const value = event.target.value;
  this.setState({
    number1: value
  });
}

```

In a similar way, we can convert the other three functions:

```js
onSecondInputChange = (event) => {
 // your code
}

handleAdd = (event) => {
 // your code
}

handleSubtract = (event) => {
 // your code
}

```

Also, there is no need to bind the event handlers in the constructor. So we can remove that code. Now the constructor will look like this:

```js
constructor(props) {
  super(props);

  this.state = {
    number1: "",
    number2: "",
    result: "",
    errorMsg: ""
  };
}

```

We can simplify it even further. The class properties syntax allows us to declare any variable directly inside the class so we can completely remove the constructor and declare the state as a part of the class, as shown below:

```js
export default class App extends React.Component {
  state = {
    number1: "",
    number2: "",
    result: "",
    errorMsg: ""
  };

  render() { }
}

```

Here's a Code Sandbox demo: [https://codesandbox.io/s/trusting-dust-ukvx2](https://codesandbox.io/s/trusting-dust-ukvx2)

If you check out the above Code Sandbox demo, you will see that the functionality is still working as before.

But using class properties makes the code much simpler and easy to understand.

Nowadays, you will find React code written like this.

## Use a single event handler method

If you inspect the above code, you will see that for each input field we have a separate event handler function, `onFirstInputChange` and `onSecondInputChange`.

If the number of input fields increases, the number of event handler functions also increases, which is not good. 

For example, if you're creating a registration page, then there will be many input fields. So creating a separate handler function for each input field is not feasible.

Let's change that.

To create a single event handler that will handle all input fields, we need to give a unique name to each input field that matches exactly with the corresponding state variable names.

We already have this setup. The names `number1` and `number2` which we've given to the input fields are also defined in the state. So let's change the handler method of both of the input fields to `onInputChange` like this:

```js
<input
  type="text"
  name="number1"
  placeholder="Enter a number"
  onChange={this.onInputChange}
/>

<input
  type="text"
  name="number2"
  placeholder="Enter a number"
  onChange={this.onInputChange}
/>

```

and add a new `onInputChange` event handler like this:

```js
onInputChange = (event) => {
  const name = event.target.name;
  const value = event.target.value;
  this.setState({
    [name]: value
  });
};

```

Here, while setting the state, we're setting the dynamic state name with the dynamic value. So when we're changing the `number1` input field value, `event.target.name` will be `number1` and `event.target.value` will be the user-entered value.

And when we're changing the `number2` input field value, `event.target.name` will be `number2` and `event.taget.value` will be the user-entered value.

So here we're using the ES6 dynamic key syntax to update the corresponding value of the state.

Now you can delete the `onFirstInputChange` and `onSecondInputChange` event handler methods. We no longer need them.

Here's a Code Sandbox demo: [https://codesandbox.io/s/withered-feather-8gsyc](https://codesandbox.io/s/withered-feather-8gsyc)

## Use a single calculation method

Now, let's refactor the `handleAdd` and `handleSubtract` methods.

We're using two separate methods that have almost the same code which creates code duplication. We can fix this by creating a single method and passing a parameter to the function identifying the addition or subtraction operation.

```js
// change the below code:
<button type="button" className="btn" onClick={this.handleAdd}>
  Add
</button>

<button type="button" className="btn" onClick={this.handleSubtract}>
  Subtract
</button>

// to this code:
<button type="button" className="btn" onClick={() => this.handleOperation('add')}>
  Add
</button>

<button type="button" className="btn" onClick={() => this.handleOperation('subtract')}>
  Subtract
</button>

```

Here, we've added a new inline method for the `onClick` handler where we're manually calling a new `handleOperation` method by passing the operation name.

Now, add a new `handleOperation` method like this:

```js
handleOperation = (operation) => {
  const number1 = parseInt(this.state.number1, 10);
  const number2 = parseInt(this.state.number2, 10);

  let result;
  if (operation === "add") {
    result = number1 + number2;
  } else if (operation === "subtract") {
    result = number1 - number2;
  }

  if (isNaN(result)) {
    this.setState({
      errorMsg: "Please enter valid numbers."
    });
  } else {
    this.setState({
      errorMsg: "",
      result: result
    });
  }
};

```

and remove the previously added `handleAdd` and `handleSubtract` methods.

Here's a Code Sandbox demo: [https://codesandbox.io/s/hardcore-brattain-zv09d](https://codesandbox.io/s/hardcore-brattain-zv09d)

## Use ES6 destructuring syntax

Inside the `onInputChange` method, we have code like this:

```js
const name = event.target.name;
const value = event.target.value;

```

We can use ES6 destructuring syntax to simplify it like this:

```js
const { name, value } = event.target;

```

Here, we're extracting the `name` and `value` properties from the `event.target` object and creating local `name` and `value` variables to store those values.

Now, inside the `handleOperation` method, instead of referring to state every time we use  `this.state.number1` and `this.state.number2`, we can separate out those variables beforehand.

```js
// change the below code:

const number1 = parseInt(this.state.number1, 10);
const number2 = parseInt(this.state.number2, 10);

// to this code:

let { number1, number2 } = this.state;
number1 = parseInt(number1, 10);
number2 = parseInt(number2, 10);

```

Here's a Code Sandbox demo: [https://codesandbox.io/s/exciting-austin-ldncl](https://codesandbox.io/s/exciting-austin-ldncl)

## Use enhanced object literal syntax

If you check the `setState` function call inside the `handleOperation` function, it looks like this:

```js
this.setState({
  errorMsg: "",
  result: result
});

```

We can use the enhanced object literal syntax to simplify this code.

If the property name exactly matches with the variable name like `result: result` then we can skip mentioning the part after the colon. So the above `setState` function call can be simplified like this:

```js
this.setState({
  errorMsg: "",
  result
});

```

Here's a Code Sandbox demo: [https://codesandbox.io/s/affectionate-johnson-j50ks](https://codesandbox.io/s/affectionate-johnson-j50ks)

## Convert class components to React Hooks

Starting with React version 16.8.0, React has added a way to use state and lifecycle methods inside the functional components using React Hooks.

Using React Hooks allows us to write a code that is a lot shorter and easy to maintain and understand. So let's convert the above code to use React Hooks syntax.

If you're new to React Hooks, check out my [introduction to react hooks](https://levelup.gitconnected.com/an-introduction-to-react-hooks-50281fd961fe?source=friends_link&sk=89baff89ec8bc637e7c13b7554904e54) article.

Let's first declare an App component as a functional component:

```js
const App = () => {

};

export default App;

```

To declare the state we need to use the `useState` hook, so import it at the top of the file. Then create 3 `useState` calls, one for storing the numbers together as an object. We can update them together using a single handler function and two other `useState` calls for storing the result and error message.

```js
import React, { useState } from "react";

const App = () => {
  const [state, setState] = useState({
    number1: "",
    number2: ""
  });
  const [result, setResult] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
};

export default App;

```

Change the `onInputChange` handler method to this:

```js
const onInputChange = () => {
  const { name, value } = event.target;

  setState((prevState) => {
    return {
      ...prevState,
      [name]: value
    };
  });
};

```

Here, we're using the updater syntax for setting the state because, when working with React Hooks, the state is not merged automatically when updating an object.

So we're first spreading out all the properties of the state and then adding the new state value.

Change the `handleOperation` method to this:

```js
const handleOperation = (operation) => {
  let { number1, number2 } = state;
  number1 = parseInt(number1, 10);
  number2 = parseInt(number2, 10);

  let result;
  if (operation === "add") {
    result = number1 + number2;
  } else if (operation === "subtract") {
    result = number1 - number2;
  }

  if (isNaN(result)) {
    setErrorMsg("Please enter valid numbers.");
  } else {
    setErrorMsg("");
    setResult(result);
  }
};

```

Now, return the same JSX returned from the render method of the class component but remove all the references of `this` and `this.state` from the JSX.

Here's a Code Sandbox demo: [https://codesandbox.io/s/musing-breeze-ec7px?file=/src/App.js](https://codesandbox.io/s/musing-breeze-ec7px?file=/src/App.js)

## Implicitly return objects

Now, we have optimized our code to use modern ES6 features and avoided code duplications. There is one more thing we can do is to simplify the `setState` function call.

If you check the current `setState` function call inside the `onInputChange` handler, it looks like this:

```js
setState((prevState) => {
  return {
    ...prevState,
    [name]: value
  };
});

```

In an arrow function, if we have code like this:

```js
const add = (a, b) => {
 return a + b;
}

```

Then we can simplify it as shown below:

```js
const add = (a, b) => a + b;

```

This works because If there is a single statement in the arrow function body, then we can skip the curly brackets and the return keyword. This is known as an implicit return.

So if we're returning an object from arrow function like this:

```js
const getUser = () => {
 return {
  name: 'David,
  age: 35
 }
}

```

Then we **can't** simplify it like this:

```js
const getUser = () => {
  name: 'David,
  age: 35
}

```

This is because opening curly brackets indicates the beginning of the function, so the above code is invalid. To make it work we can wrap the object in round brackets like this:

```js
const getUser = () => ({
  name: 'David,
  age: 35
})

```

The above code is the same as the below code:

```js
const getUser = () => {
 return {
  name: 'David,
  age: 35
 }
}

```

So we can use the same technique to simplify our `setState` function call.

```js
setState((prevState) => {
  return {
    ...prevState,
    [name]: value
  };
});

// the above code can be simplified as:

setState((prevState) => ({
  ...prevState,
  [name]: value
}));

```

Here's a Code Sandbox demo: [https://codesandbox.io/s/sharp-dream-l90gf?file=/src/App.js](https://codesandbox.io/s/sharp-dream-l90gf?file=/src/App.js)

This technique of wrapping code in round brackets is used a lot in React:

* To define a functional component:

```js
const User = () => (
   <div>
    <h1>Welcome, User</h1>
    <p>You're logged in successfully.</p>
   </div>
);

```

* Inside mapStateToProps function in react-redux:

```js
const mapStateToProps = (state, props) => ({ 
   users: state.users,
   details: state.details
});

```

* Redux action creator functions:

```js
const addUser = (user) => ({
  type: 'ADD_USER',
  user
});

```

and many other places.

## An Extra Tip to Help You Write Better React Components

If we have a component like this:

```js
const User = (props) => (
   <div>
    <h1>Welcome, User</h1>
    <p>You're logged in successfully.</p>
   </div>
);

```

and later want to log the props to the console just for testing or debugging, then instead of converting the code to the below code:

```js
const User = (props) => {
 console.log(props);
 return (
   <div>
    <h1>Welcome, User</h1>
    <p>You're logged in successfully.</p>
   </div>
 );
}

```

you can use the logical OR operator (`||`) like this:

```js
const User = (props) => console.log(props) || (
   <div>
    <h1>Welcome, User</h1>
    <p>You're logged in successfully.</p>
   </div>
);

```

How does it work?

The `console.log` function just prints the value passed to it, but it does not return anything – so it will be evaluated as undefined `||` (...).

And because the `||` operator returns the first truthy value, the code after `||` will also be executed.

### Thanks for reading!

You can learn all about ES6+ features in detail in my [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/) book.

Also you can check out my free [Introduction to React Router](https://yogeshchavan.podia.com/react-router-introduction) course.

**Subscribe to my [weekly newsletter](https://yogeshchavan.dev/) to join 1000+ other subscribers to get amazing tips, tricks, articles and discount deals directly in your inbox.**

