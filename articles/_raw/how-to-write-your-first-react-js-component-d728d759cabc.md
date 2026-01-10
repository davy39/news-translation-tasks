---
title: How to write your first React.js component
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-24T02:25:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-your-first-react-js-component-d728d759cabc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N2KU7pOcwZwKeOi3B-YBLQ.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Samer Buna

  React’s function and class components, props, state, and event handlers



  Update: This article is now part of my book “React.js Beyond The Basics”.

  Read the updated version of this content and more about React at jscomplete.com/react-be...'
---

By Samer Buna

#### React’s function and class components, props, state, and event handlers

![Image](https://cdn-media-1.freecodecamp.org/images/1*QlwpBT5qXRN1F55aiPoxdw.png)

> **Update:** This article is now part of my book “React.js Beyond The Basics”.

> Read the updated version of this content and more about React at [**_jscomplete.com/react-beyond-basics_**](https://jscomplete.com/g/first-component)_._

The most important concept to understand in React.js is the component. A React component can be one of two types. It can be either a **function** component or a **class** component. Sometimes you will hear different terms to describe these two types, like **stateless** and **stateful**. Function components are also often associated with the **presentational** concept. I will refer to them in this article as function components and class components.

**A function component** is the simplest form of a React component. It is a simple function with a simple contract:

![Image](https://cdn-media-1.freecodecamp.org/images/1*XL5uu7lggaRZdKRpWhU3Gw.png)
_Screenshot captured from my Pluralsight course — [React.js: Getting Started](https://www.pluralsight.com/courses/react-js-getting-started" rel="noopener" target="_blank" title=")_

The function component receives an object of properties which is usually named **props.** It returns what looks like HTML, but is really a special JavaScript syntax called [JSX](https://facebook.github.io/react/docs/introducing-jsx.html).

A **class component** is a more featured way to define a React component. It also acts like a function that receives props, but that function also considers a private internal state as additional input that controls the returned JSX.

![Image](https://cdn-media-1.freecodecamp.org/images/1*N2KU7pOcwZwKeOi3B-YBLQ.png)
_Screenshot captured from my Pluralsight course — [React.js: Getting Started](https://www.pluralsight.com/courses/react-js-getting-started" rel="noopener" target="_blank" title=")_

This private internal state is what gives React its **reactive** nature. When the state of a class component changes, React will re-render that component in the browser.

The State and Props objects have one important difference. Inside a class component, the State object can be changed while the Props object represents fixed values. Class components can only change their internal state, not their properties. This is a core idea to understand in React and this article will have an example of that.

Let’s look at an actual example of a component. A very simple one, without any input and with a simple `h1` in a `div` output.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iEMbKsYd4nCFiZ_yoRJvoA.png)
_Screenshot captured from my Pluralsight course — [React.js: Getting Started](https://www.pluralsight.com/courses/react-js-getting-started" rel="noopener" target="_blank" title=")_

On the left side, the component is written in the special JSX syntax.

JSX allows us to describe our User Interfaces (UIs) in a syntax very close to the HTML that we are used to. It is, however, optional. React can be used without JSX, as you can see on the right side. In fact, React just compiles the JSX you see on the left to the pure JavaScript you see on the right. Then it works with compiled JavaScript in the browser.

The `React.createElement` call on the right side is a JavaScript representation of the Document Object Model ([DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)). React efficiently translates it into DOM operations that it performs in the browser.

### Let’s write a React component.

I will be using jsComplete’s [React Playground](https://jscomplete.com/react) for the examples in this article. It’s a tool where you can test your JavaScript and React code right in the browser. There is no need to install or configure anything.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RmSo6MSOYmz4DKn9q8iX1w.png)

The tool has a simple two-panels interface. The left panel is the editor where you write your JavaScript and React code. The latest version of both React and ReactDOM are already pre-loaded there. The editor also understands the JSX extension and all the modern features in JavaScript. This will allow us to focus on the React API itself rather than configuring and compiling a React application.

The right panel is the preview panel. You have a pre-defined `mountNode` element in the editor. When you execute your JavaScript code, anything you put in the `mountNode` element shows up in the preview panel. The preview panel will also show any errors you encounter when you execute your code. The playground is also a simple JavaScript _REPL_ (Run, Eval, Print, Loop) where you can test quick JavaScript functions and expressions. To execute the code at any time press `CTRL+Enter`.

Try the following in the REPL, for example:

```
mountNode.innerHTML = 'Hello!!';
```

Or the simple REPL mode

```
3 == '3'
```

To create a React component, define a new function. Let’s make that function return an HTML button element:

```
function Button() {  return (    <button>Go</button>  );}
```

What we returned here looks like HTML but remember that it is not. It is going to be compiled into JavaScript. The actual JavaScript that the browser sees when we use this button element in JSX is a call to the `React.createElement` function:

```
function Button() {  return (    React.createElement("button", null, "Go")  );}
```

While you can use React this way without JSX, it would be a lot harder to code and maintain. So, let’s stick with JSX.

The function above is a complete and very simple React component. Let’s use it!

We use a component by mounting it in the browser. The function designed to do that is `ReactDOM.render`, which takes in two arguments:

* The first is the component to render, in our case it is `Button`.
* The second argument is the element in which this component should be rendered. In the REPL’s environment we can use the special `mountNode` variable.

```
ReactDOM.render(<Button />, mountNode);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*L866_1BuscPjUtqExbP0tA.png)
_[https://jscomplete.com/repl?j=Skl5GngO-](https://jscomplete.com/repl?j=Skl5GngO-" rel="noopener" target="_blank" title=")_

All code examples in this article have a link in the screenshot caption where you can edit the example at jsComplete REPL.

A React function component receives as its first argument the `props` object. This argument allows us to make the component re-usable. For example, instead of hard-coding the “Go” label of the button above, we can pass the `Button` component a `label` attribute, like we do with regular HTML elements:

```
ReactDOM.render(<Button label="Save" />, mountNode);
```

Then we can access this attribute inside the component with a curly bracket for `props.label`.

```
function Button(props) {  return (    <button>{props.label}</button>  );}
```

The `props` argument is an object that holds all the values that were passed to the component when it was rendered.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HvOTyzJNb2I3bm7AKpVqVw.png)
_[https://jscomplete.com/repl?j=ByQm4nl_Z](https://jscomplete.com/repl?j=ByQm4nl_Z" rel="noopener" target="_blank" title=")_

### Making the component interactive

We have a button element and it is rendered through a React component.

Let’s now add some interactivity to this so-far boring example. Let’s make that button element increment a counter value on every click and display that value as the button label itself. So the label of this button is going to start with the number 1 and when the user clicks the button its label will change to 2, 3, 4 and so on.

Since this is something that needs to be reflected in the component rendered output, it belongs to the state of the component. We need the component to re-render itself every time the counter changes. We cannot use a property here because a component props cannot be changed. By using the special React state object, we will be utilizing React’s **reactive** nature and we will not need to worry about **how** to take the changes to the browser. React will do that for us.

But, our Button component is currently a function component. Function components cannot have state, so we need to upgrade this component to a class component first.

This is very simple. We first define a class that extends `React.Component`

```
class Button extends React.Component { }
```

In that class we define a `render` function, which returns the component’s JSX; the HTML button in our case.

```
render() {  return (    <button>1</button>  );}
```

This is a little bit more code, but we can now use a private state on the Button component!

![Image](https://cdn-media-1.freecodecamp.org/images/1*XQwiawVuQKD7VOqVcHXl8g.png)
_[https://jscomplete.com/repl?j=BJCWI2gd-](https://jscomplete.com/repl?j=BJCWI2gd-" rel="noopener" target="_blank" title=")_

To use a state object we first need to initialize it. The state object is a simple instance property, so we can initialize it inside the constructor function of the `Button` class. We just define the normal constructor function (which receives a `props` object in React) and call the `super` method to honor the inheritance of the component.

```
constructor(props) {  super(props);  this.state = { counter: 1 };}
```

After that, we initialize `this.state` to whatever we want. The keys of this state object are the various elements of the state. For our case, we need a `counter` state, which starts from 1.

Inside the render function, since we can write any JavaScript expression within curly brackets, we can read the value of the new `counter` state element that we initialized on the state using `this.state.counter`.

```
render() {  return (    <button>{this.state.counter}</button>  );}
```

The “`this`” keyword refers to the component instance we are handing off to `ReactDOM`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IgGVPxvwOdz_7AdlJj-new.png)
_[https://jscomplete.com/repl?j=SJfwu2xuZ](https://jscomplete.com/repl?j=SJfwu2xuZ" rel="noopener" target="_blank" title=")_

You can try and change that counter state to see how the button will render the values you put on the state.

There is another shorter syntax to define the initial state, which is to simply use a class property without a constructor call:

```
class Button extends React.Component {  state = { counter: 1 };    render() {    return (      <button>{this.state.counter}</button>    );  }}
```

This is not yet part of the official JavaScript language but it will be soon. The syntax works at the jsComplele REPL playground because that tool is using Babel to transpile it to the supported JavaScript that the browser will understand.

When you configure your own React application you’ll have to use something like Babel anyway to compile JSX into JavaScript. It is an easy win to also include and use the JavaScript features that are well on their way to becoming an official part of the language.

In the `Button` example so far, we have a state object and an HTML button element that displays a counter value that we initialized on the state. Now we need to change that value when we click the button. We need to define a click handler on that button.

React comes with normalized events that are easy to use. For this case, we need the `onClick` event, which we define on the HTML button element itself:

```
function F() {}
```

```
<button onClick={F} />
```

Unlike DOM event handlers, which use a string, React event handlers use an actual JavaScript function. This function can be a global one (like `F` above), or an inline function:

```
<button onClick={() => {}} />
```

However, the standard practice is to define a function on the class component itself. Let’s call it `handleClick` and we can define it on the component as an instance property:

```
class Button extends React.Component {  state = { counter: 1 };    handleClick = () => {    console.log('Button is clicked!!');  };    render() {    return (      <button onClick={this.handleClick}>        {this.state.counter}      </button>    );  }}
```

We are using the modern class field syntax, which allows us to use arrow functions that are bound to the component instance. `handleClick` will now act as a prototype function on this class. Inside `handleClick` the keyword “`this`” refers to the component instance that we are mounting in the DOM.

`handleClick` ’s job is easy: read the current counter value from the state object using `this.state.counter`. Then increment this value and update the component state with the new incremented value.

We can use React’s built-in `setState` method, which is available on every class component instance, to update a component state.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A61aPxQK-fx7Mw2nLbpPbg.png)
_[https://jscomplete.com/repl?j=Sy-u46l_Z](https://jscomplete.com/repl?j=Sy-u46l_Z" rel="noopener" target="_blank" title=")_

The button will now increment its label on every click.

This was simple and powerful! We defined an event handler for the `onClick` method. Every time the user clicks the button the `handleClick` function will be executed. The function reads the current state of the counter value, increments it, and then sets the state to the new incremented value. React takes care of all the rendering needed after these changes so you do not have to worry about that.

Note that we did not update the state object directly. We have to use React’s `setState` method when we want to update any element on the state. You can’t for example do this:

```
// WRONG:this.state.counter = this.state.counter + 1;
```

React’s `setState` method is an asynchronous one which schedules an update. Multiple `setState` calls might potentially be batched for performance. Since we are both reading and writing to the state object inside the `handleClick` function, we could hit a race condition. The general rule of thumb is whenever you need to update the state using a value from the current state, use the other contract of the `setState` method. This receives a function reference instead of an object as its first argument:

```
this.setState((prevState) => {});
```

This function receives a `prevState` object that we can confidently use without worrying about race conditions. The function returns the object that we want React to use to set the state. Our `counter` value example above becomes:

```
this.setState((prevState) => ({  counter: prevState.counter + 1 }));
```

You only need to use this second syntax of `setState` if your update depends on the current state. However, it may be a good idea to make a habit of always using the second function-argument syntax.

Here is the final code:

```
class Button extends React.Component {  state = { counter: 1 };    handleClick = () => {    this.setState((prevState) => ({      counter: prevState.counter + 1     }));  };    render() {    return (      <button onClick={this.handleClick}>        {this.state.counter}      </button>    );  }}
```

```
ReactDOM.render(<Button />, mountNode);
```

[Test it out](https://jscomplete.com/repl?j=rJgDsTgdb) and if you have any questions let me know in the comments below.

> This article is a write-up of part of my Pluralsight course — [React.js: Getting Started](https://www.pluralsight.com/courses/react-js-getting-started). I cover similar content in video format there.

Learning React or Node? Checkout my books:

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)

