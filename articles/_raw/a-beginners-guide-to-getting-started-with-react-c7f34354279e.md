---
title: A beginner’s guide to getting started with React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T17:29:31.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-getting-started-with-react-c7f34354279e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h8d-4wYLN9wwiEsLAA_5yg.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ankita Masand

  In this tutorial, I’ll first help you understand why Facebook felt the need to build
  a library called React. I’ll cover all the basic concepts that you’d need to create
  your first React app. This tutorial aims to explain React by cle...'
---

By Ankita Masand

In this tutorial, I’ll first help you understand why Facebook felt the need to build a library called _React_. I’ll cover all the basic concepts that you’d need to create your first React app. This tutorial aims to explain React by clearly explaining its fundamentals like the _use of JSX and ES6, building stateful & stateless components, React Elements, virtual DOM and the diffing algorithm_.

![Image](https://cdn-media-1.freecodecamp.org/images/NsBhsN56E38anPtJhwdA44UQQg8RKAgKktfM)
_Credits: [https://matwrites.com](https://matwrites.com" rel="noopener" target="_blank" title=")_

The web has evolved from just being a bunch of static HTML pages to reliable, interactive and performant applications. With the advent of AJAX, we can asynchronously load the entire application in parts.

Whenever there is a change in any part of the application due to real-time updates or user input, that part only is loaded asynchronously to reflect the updated state. This means that only the respective Document Object Model ([DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)) container should be updated to reflect the changes to the client.

For example, consider the comments section on Facebook. The comments data fetched on initial load is appended to the DOM. Now, when you add a new comment, it makes an asynchronous request to the server to save this comment in the database, and update the DOM to reflect the current state.

Let’s get into the details of this example and understand how that would work. Let’s say that I have 20 comments in my comments array. The comments array is the source of truth, and it reflects the current state at any point in time. When the user adds a new comment, we need to modify this comments’ array once the new comment has been successfully added to the database. The comments array now holds 21 comments.

Oh yeah, we also need to write code to update the DOM to reflect the current state (Assume we’re using Vanilla JavaScript or jQuery here. Cool stuff coming up next!). This means that the comments DOM container is subscribed to the comments array. It should be modified when there is any change in the comments array. We can safely say that the comments array is the model here, and the comments container is the view.

Let’s add something more to this — hundreds of div elements are subscribed to this comments model, which means that we need to write code to update each of these `div` elements.

```
function updateCommentsSubscriber (response) {    commentsArr = [ ...response ] // commentsArr = ['Comment 1', 'Comment 2', ...]    var firstDiv = document.getElementById('first')    firstDiv.innerHTML = commentsArr.length    var secondDiv = document.getElementById('second')    secondDiv.innerHTML = commentsArr.toString()    ...}
```

Sigh! Imagine if this happened at the scale at which Facebook operates. Whenever we have a new element that is subscribed to that model, we’d have to write code to make changes to that element. This approach is not scalable.

Facebook dealt with the scalability and DOM slowness issue by building a library called **React**. React was first deployed on the _Newsfeed_ section of Facebook in 2011, and then on Instagram in 2012. It was open-sourced in 2013 and has been applauded by the community worldwide ever since.

In this tutorial, we’ll build on the fundamentals of React. By the end of this tutorial, you should be able to write your first React app.

### Table of Contents

1. Introducing React
2. JSX
3. ES6
4. React Elements
5. Components
6. State & Props
7. Stateless Components
8. Lifecycle methods
9. Virtual DOM
10. Building your first React app using create-react-app

While I suggest a deep dive into each of these topics, please feel free to skip any of these if you’re already confident about it.

### Introducing React

**React is a JavaScript library used for building user interfaces**. It solves the scalability issue mentioned earlier by efficiently updating the DOM.

One way to update the DOM is by manually putting in values in the respective DOM nodes, which is obviously slow and not scalable.

Angular solves this problem by using _data-binding_. It binds the variables used in the view with their respective counterparts in the model. It automatically updates all the instances of a variable in a view when its respective value in a model changes.

On the other hand, React provides a different approach to solving this problem. It uses a technique called _Reconciliation_ to evaluate the difference in the DOM representation at two points in time. It only updates the part that is changed. This will become clear once we get into the details of how React works. For now, let’s consider a simple example:

This goes into the HTML:

```
<div id='app'></div>
```

Put the below code in a JavaScript file:

```
class HelloReact extends React.Component {    render () {        return (            <div>Hello React!</div>        )    }}ReactDOM.render(<HelloReact>, document.getElementById('app'))
```

The above example will print `Hello React!` on the screen. `HelloReact` is called a _component_ in React. The `render` method inside this component returns the DOM representation.

It’s not a coincidence that I wrote HTML in JavaScript. `<div>Hello React!`</div`> i`nside render _method is_ a JSX syntax. It lets us write HTML in JavaScript.

The last statement does the work of rendering the `HelloReact` component inside our `app` container. In the following two sections, we'll dive deeper into JSX and ES6.

### JSX

If we didn’t have JSX, you’d have to write the above JSX code as:

```
React.createElement("div", null, "Hello React!")
```

This can complicate things if you need to deal with nested elements.

For example:

```
React.createElement("div", { className: "container" },    React.createElement("span", null, "Hello React!"),    React.createElement("span", null, "I'm inside HelloReact Component"))
```

And this is the JSX syntax for the above code:

```
<div className='container'>    <span>Hello React!</span>    <span>I'm inside HelloReact Component</span></div>
```

Writing JSX inside a React component gives a clear idea of what the component is going to render to the DOM. It looks clean and intuitive.

If you’re already convinced of using JSX with React, continue reading to learn more. If not, React does allow you to use it without JSX. You can learn more about it [here](https://reactjs.org/docs/react-without-jsx.html).

JSX is just a JavaScript extension that allows writing HTML-like code:

```
<div>Hello {name}!</div>
```

The expression inside the curly braces will be evaluated to the value of the variable `name`. You can even call functions inside JSX:

```
<div>Hello, {formatName('james.gosling')!}</div>
```

This would call the `formatName` function and pass `james.gosling` as the parameter to it. It'll render the value that is returned from the function `formatName`.

#### Conditional Statements

It is often the case that you need to render a DOM node only when a particular value has been set.

This can be achieved using JSX as:

```
greetUser (userName) {    if (isUserLoggedIn) {        return <div>Hello, {userName}!</div>    }    return <div>Hello, Guest!</div>}
```

The above example will greet a logged in user with his name and as _Guest_ when a user is not logged in.

Please note that this conditional rendering is not similar to the show/hide scenario. Based on the value of the variable `isUserLoggedIn`, only one of the two elements will be rendered to the DOM at a time.

#### Rendering Child Nodes using the map function

Let’s consider our comments example from above. Here, we have a comments array, and we need to render all of the comments in a DOM container.

`map` is a native JavaScript function used for iterating the elements in an array. You can pass a custom iterator function as one of its arguments. Each of the elements in the array would be serving as input to this iterator function. `map` will output an array based on the values returned during each iteration.

`map` comes handy when building React components. You can learn more about it [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map).

```
renderComments (commentsArr) {    /* commentsArr would look similar to this structure below    commentsArr = [{        id: 1,        text: "I'm a comment!"    }]    */    return (        <div class='comments-container'>            {                commentsArr.map (function (comment) {                   return <div key={comment.id}>{comment.text}</div>                })            }        </div>    )}
```

The above `renderComments` method would return the result of the `map` method. In this case, `map` returns an array of DOM nodes.

Notice the use of `key` with each `div` element. We'll get into the details of using `key` with DOM elements later. For now, it's just used as a way for uniquely identifying DOM elements.

#### Compiling JSX to JavaScript

The React library doesn’t understand JSX. It’s just used to make the developer’s job easier. So, what does React do when it comes across this weird _HTML-like_ syntax in JavaScript code?

JSX is transpiled to JavaScript statements by the [Babel plugin](https://babeljs.io/docs/en/babel-plugin-transform-react-jsx) before React encounters them. _Transpilation is the process of converting one source language to another_. So, all that React sees is simple JavaScript statements.

The simple JSX code from above

```
<div class='heading'>Hello React!</div>
```

gets transpiled to

```
React.createElement("div", { className: 'heading' }, "Hello React!")
```

`createElement` method is defined on React.

The first argument to the `createElement` method is the type of the DOM node that you'd like React to create for you. It can be `div`, `span`, `p`, and so on.

The second argument is used for specifying the attributes on the DOM node. In this case, we’re telling React that the `className` of the node is `heading`.

Notice the use of `className` instead of conventional `class` attribute. In React, `class` attribute is specified as `className` to avoid conflicts with the existing attributes.

The third argument carries information about the children of the DOM node. In this case, it is just plain text that will be added as `innerHTML` to the DOM node

The `createElement` method is analogous to the `document.createElement` method in JavaScript, but it outputs a React element. We'll get into the details of React Elements later.

### ES6

ES6 is the abbreviation for ECMAScript 6 or ECMAScript 2015. In this part, we’ll learn some common ES6 techniques that make developing React components an easier task.

#### `let` & `const`

`let` is used for declaring block-level variables, and `const` is used for declaring constants. JavaScript follows a **function-level scoping**.

A variable declared inside a function can be used in the entire function, but not outside of it.

Let’s consider an example that will help us understand function-level scoping:

```
function pokemon (id) { //id = 12    if (id === 12) {        var pokemonObj = {            id: 12,            name: 'butterfree',            height: 11,            weight: 22,            abilities: [                {                    name: 'tinted-lens'                }            ]        }    }    return pokemonObj    }
```

The above `pokemon` method takes `id` as the parameter, and returns `pokemonObj` if the `id` is equal to `12`. Go ahead and run this function in your browser console.

If you execute `pokemon(12)`, it prints the `pokemonObj` as expected. However, if you execute `pokemon(13)`, it doesn't display an error, and instead prints `undefined`.

Notice that `pokemonObj` gets defined in the `if` construct, which means if the `id` is not equal to 12, `pokemonObj` should not be available in the context of the `pokemon` function.

JavaScript follows function-level scoping, which means a variable declared in any statement inside a function is available throughout the function. So, `pokemonObj` is available even if it is declared inside `if` block.

The `let` construct solves this problem as it lets us limit the scope of variables to block level.

Use `let` for declaring the `pokemonObj` and check the results:

```
function pokemon (id) { //id = 12    if (id === 12) {        let pokemonObj = {            id: 12,            name: 'butterfree',            height: 11,            weight: 22,            abilities: [                {                    name: 'tinted-lens'                }            ]        }    }    return pokemonObj    }
```

You’ll get `pokemonObj is not defined`, and that justifies the block-level scoping of variables declared using the `let` construct.

A variable declared using `const` cannot be modified:

```
const POKEMON = 'butterfree' pokemon = 'pikachu'
```

The second statement above displays an error since it’s not allowed to modify constant variables.

#### Object Destructuring

Consider an object, `berries`, which are small fruit that can provide HP and status condition restoration, stat enhancement, and even damage negation when eaten by the Pokémon:

```
var berries = {    id: 1,    name: 'cheri',    growth_time: '3',    max_harvest: 5,    natural_gift_power: 60,    size: 20,    smoothness: 25,    soil_dryness: 15,    natural_gift_type: {        name: 'fire',        url: 'https://pokeapi.co/api/v2/type/10/'    }}
```

If I need to use some of the keys from the above object, the conventional approach is:

```
var id = berries.idvar name = berries.namevar growthTime = berries.growth_time
```

And with ES6:

```
let { id, name, growth_time, max_harvest, natural_gift_power, size } = berries
```

The above statement creates local variables as `id`, `name`, `growth_time`, `max_harvest`, `natural_gift_power`, and `size`, and each of them will have the value corresponding to that in the `berries` object. Isn't that cool?

Here, we’re destructuring the object to refer individual keys. If any of the keys wasn’t defined in the object, its value would be `undefined`.

#### String Templating

Here’s the old way of concatenating strings in JavaScript:

```
var cheriDescription = "One of the berries is " + name + ". Its growth time is " + growth_time + ". Its size is " + size + ". Its Max Harvest is " + max_harvest.
```

And here is the ES6 way:

```
let cheriDescription = `One of the berries is ${name}. Its growth time is ${growth_time}. Its size is ${size}. Its Max Harvest is ${max_harvest}.`
```

You can write the entire sentence in backticks without having to concatenate static text and variables in parts. Wrap the variables inside `'${}'`. This looks a lot cleaner.

#### Arrow Functions

This one’s my favorite. Below is the old way of writing functions in JavaScript:

```
function getBerrySize (berries) {    return berries.size}
```

And this is the ES6 way of writing functions:

```
const getBerrySize = (berries) => berries.size
```

Arrow functions follow this syntax:

`declaration` `functionName` = `(functionParams)` =&g`t; return res`ult

The above function `getBerrySize` returns the size of the berry. Notice that we didn't write the word `return` in the above arrow function. Use of `return` is optional if the body of the arrow function has just one statement and it returns that statement.

If a function body has more than one statement, wrap them in curly braces.

Arrow functions behave a little different compared to normal functions when used with the `this` construct. Learn more about `this` and how the arrow functions behave differently when used with `this` from my article [here](https://hackernoon.com/lets-get-this-this-once-and-for-all-f59d76438d34).

#### Classes

With ES6, we can wrap the relevant functions used for implementing a particular functionality inside a class.

Let’s build a class to evaluate berries:

```
class Berries {    constructor (berries) {        this.berries = berries    }    getSize () {        return this.berries.size    }    getGrowthTime () {        return this.berries.growth_time    }}const cherries = new Berries(berries)cherries.getSize() // 20cherries.getGrowthTime() // 3
```

We’ve wrapped the relevant berries methods inside the class `Berries`.

The statement `const cherries = new Berries(berries)` instantiates the Berries class and create an Object of type `Berries`.

The input passed to the Berries constructor is the `berries` object we've created earlier. We can use methods defined in the `Berries` class on this object.

Now that we’ve learned most of the common ES6 techniques, we can use them in the following sections.

### React Elements

React Elements are the smallest units that represent the state of the DOM at any point in time.

The browser doesn’t understand React. Like we saw earlier, JSX is converted to JavaScript statements for creating a DOM node.

With this statement:

```
React.createElement("div", { className: 'heading' }, "Hello React!")
```

The `div` DOM node isn't yet appended to the DOM. The above statement is converted to plain JavaScript object as:

```
{    type: 'div',    props: {        className: 'heading',        children: 'Hello React!'    }}
```

These objects are called **React Elements**.

They contain two important keys:

`type` specifies the type of the DOM node. It can be `div`, `span`, `p`, and so on.

`props` describes the properties of that element. In this case, we have `className` and `children`.

The nested elements can be specified as the value of the `children` key.

`ReactDOM` does the work of converting these React Elements to actual DOM nodes and also updates them accordingly.

React elements are immutable and are cheap to create. If there is any change in a React Element, its older instance is destroyed, and a newer one is created from scratch.

However, the corresponding DOM node is not always destroyed to make room for a newer one. DOM operations are expensive, and hence they should be avoided at all possible instances.

ReactDOM does a great job here. It creates new React elements because creating them is cheap, however, it efficiently updates only the part of the real DOM node that is modified.

React uses a _diffing_ algorithm to find out what needs to be updated to the DOM. We’ll learn more about it in the Virtual DOM section.

Let’s go through what we’ve learned so far:

* JSX is an _HTML-like_ syntax that is used in React components. It’s just a representation of the DOM node and doesn’t actually append elements to the DOM.
* The Babel plugin transpiles it to plain JavaScript statements as `React.createElement`.
* The `React.createElement` statements are further converted into JavaScript objects.
* ReactDOM efficiently updates the real DOM using the objects created above.

### Components

Components are reusable classes that define a particular functionality. React follows a _component-based_ structure. Each of the components that we define in React extends the basic functionalities of the native React Component.

Let’s create a simple React component for input text:

```
class Text extends React.Component {    state = {        value: ''    }    onChange = (e) => {        this.setState({ value: e.target.value })    }    render () {        return (            <input                type='text'                onChange={this.onChange}                value={this.state.value}            />        )    }}export default Text
```

Each of the React components has an implementation of the `render` method. This method returns the DOM representation for that component. In our case, it returns an `input` element. Remember, this `input` element is not actually a DOM node. It's just a DOM representation.

The attributes — `text`, `onChange` and `value` that are passed to the `input` element are called **props** in React. `onChange` is an event handler that gets called whenever the value of the text in input box changes. `props` in React are read-only.

React components maintain an internal state for handling the complexity based on various parameters. At the beginning of our component, we’ve initialized an object called `state`. This state variable handles the state of the Text Component. The state can be modified using the `setState` method, as shown in the `onChange` method defined above.

The `Text` component is an individual unit. It gets interesting when these components can be directly used in other complicated components. React follows a `Composition` based model, which means importing smaller components to implement complex functionality. It composites different smaller components into a bigger component to make up for a working feature.

Let’s create a forms component that would import the Text component from above:

```
import Text from './text'class Forms extends React.Component {    state = {}    render () {        return (            <div>                <p>Form for basic details</p>                <Text />            </div>        )    }}
```

First, we’re importing the Text component. Notice how the Text component is included in the `render` method of the Forms component.

When the Forms component is rendered, the `<Text` /> gets replaced by the return value o`f the` render method in the Text component.

### More on `state` and `props`

As mentioned earlier, React follows a Composition-based model. The bigger components can customize the components that are to be imported by sending in related props.

Let’s modify the `render` method of the above Forms component as

```
render () {    return (        <div>            <p>Form for basic details</p>            <Text                type='text'            />;        </div>    )}
```

Notice how we’re passing `type` props in the Text component.

We need to make changes to our Text component to accept these props.

Check out the changes in the `render` method:

```
render () {    let { type } = this.props    return (        <input            type={type}            onChange={this.onChange}            value={this.state.value}        />    )}
```

The `props` passed by the Forms component are available as an object in the Text Component. Notice how we're using the `type` property in the Text component that was passed by the forms component.

The state variable manages the internal state of a component. It can be changed based on Network changes, user’s input or any scheduled updates.

`state` is nothing but a JavaScript object. It can be changed using the `setState` method. The `setState` method takes an object as an input. Whenever any value changes in a state, we only pass that value in the `setState` method instead of passing the entire state object.

Let’s say that we have our Berries Component and that its internal state is the `berries` object that we defined above.

If there's a change in the `growth_time` property of the `berries` object, we can update it in the state as:

```
this.setState({ growth_time: new_growth_time })
```

We’re not passing the entire `berries` object to the `setState` method. We're only passing the value that needs to be updated.

The `setState` method operates as an asynchronous function. Multiple state update calls are batched and invoked together at later intervals to deal with performance issues.

### Stateless Components

The components defined above had their own state in place. However, we can also define Stateless components.

These components are pure functions. They don’t modify the input passed to them. These are just representational components.

Let’s see an example of a stateless component:

```
const getBerrySize = (props) => {    let { size } = props    return (        <p>{size}<;/p>    )}
```

The only job of this component is to return a DOM representation for displaying the size of the Berries.

### Component Lifecycle

A React Component follows a certain lifecycle pattern. It goes through four important phases:

1. Initialization
2. Mounting
3. Updating
4. Unmounting

Let’s look into some of the methods that are invoked during these phases

**Initialization**  
Initialize state and props.

**Mounting**  
`componentWillMount`— this method is invoked just before the mounting occurs. It is called before the `render` method. For setting the initial state & props, it’s recommended to use the `constructor` in place of this method.

`render` — this is the only required method in a class component. It returns the DOM representation at any point in time. It examines the value of `state` and `props`, and returns the updated DOM representation.

`componentDidMount` — this method gets invoked immediately after the component is mounted. This is a good place to instantiate network requests to the server. Once the data is loaded from the server, you can call `setState` method to invoke `render` for updating the DOM nodes.

**Updating**  
`componentWillReceiveProps` — if there is any change in `props`, this method is called to render the updated state. It’s not recommended to use this method from React version 16 on.

`shouldComponentUpdate` — if this method returns `true`, `render` method is called to make room for the updated `state` and `props`.

`componentWillUpdate` — this method gets called immediately before render begins doing its work.

`componentDidUpdate` — this method gets called once the updated state is rendered to the DOM.

**Unmounting**  
`componentWillUnmount` — this method is invoked just before the unmounting of a component. This is a good place to remove any subscriptions from the component.

This is a brief overview of the React Component Lifecycle. I’ll explain these methods in detail in my future articles.

### Virtual DOM

I mentioned the scalability problem earlier while introducing React. In this section, we’ll see how React efficiently solves this problem.

From what you’ve learned so far, it’s clear that React doesn’t directly update the real DOM. All React knows is that DOM is nothing but a JavaScript object. This giant JavaScript object is called **Virtual DOM**.

If there is any change in the output of the `render` method in any of the components, the Virtual DOM accommodates these changes by destroying its older instance, and creating a newer one.

As mentioned earlier, React uses a technique called _Reconciliation_ to evaluate the difference between the Real DOM and the Virtual DOM.

_Reconciliation is the action of making one view or belief compatible with another_. And that’s exactly what ReactDOM does. It makes changes to the real DOM to make it compatible with the current state of the virtual DOM. React uses a _diffing_ algorithm to evaluate the changes that are to be made to the real DOM.

It uses a heuristic algorithm that is based on two assumptions:

1. Two elements of different types will produce different trees
2. The Stable elements, or the elements that are not modified, are identified using a unique identifier called `key`.

#### Elements of different types

React first compares the type of the root element. If the type of root element is different in the real DOM and the virtual DOM, it destroys the real DOM and creates a new one.

For example, if the root type in real DOM was `div`, and the one in virtual DOM was `span`, the diffing algorithm would erase the entire `div` container from the real DOM.

#### DOM Elements of the same type

This case deals with elements that are of the same type, but that have some differences in their property values.

Consider this DOM node in real DOM:

```
<div class='heading'>React Diffing Algorithm</div>
```

Now, consider the updated DOM node which is the output of a `render` method of some Component:

```
<div className='sub-heading'>React Diffing Algorithm</div>
```

By comparing both of these nodes, React would know that only the className of the nodes is changed, and it would efficiently update just the value of the class in the real DOM.

#### Identifying the position of Children in the parent container

React recommends the use of the `key` prop if similar children are to be appended to a particular DOM node.

Let’s consider the example of a comments array:

```
commentsArr.map (comment => {    return <div key={comment.id}>{comment.text}</div>})
```

The use of `key` in the child nodes of the comments container helps React to uniquely identify different comment nodes. If there is a change in any of the comment nodes, React would know which one to update based on the value of the key.

### Getting Started with React using `create-react-app`

`create-react-app` is a React Command Line interface tool that is used for creating the initial boilerplate for any react application.

It does the tedious job of setting up a development server, handling the compilation of JSX down to JavaScript as discussed earlier, and it does a few more things.

```
npm i create-react-app -g
```

This installs the `create-react-app` node module globally on your system.

The command `create-react-app my-app` creates a react project inside the  
`my-app` directory. Play around with the files and try building a smaller React component.

I hope you now have an idea of what React is and how to use it.

### Let’s recap what we’ve learned so far

1. We saw that updating DOM nodes using raw JavaScript code is not scalable.
2. React is a JavaScript library for building user interfaces. It solves the scalability issue by efficiently updating the DOM.
3. React components output DOM representation in the form of JSX. JSX is just syntactic sugar that is used to ease the development work. It gets transpiled to JavaScript statements in the form of `React.createElement`.
4. We learned about most of the common ES6 techniques like the use of `let` and `const`, Object Destructuring, Classes, Arrow Functions, and String Templating. These are used while writing React components.
5. We learned about React Elements and how they are created.
6. We learned that React follows a component-based pattern and how it uses Composition to create complex components using simpler ones. The Component uses `state` and `props` for handling internal state.
7. We took a deep dive into how React creates Virtual DOM and also understood the underlying diffing algorithm that is used for efficiently updating the real DOM.

In the next series of articles on React, I’ll cover the following topics in more detail:

1. The lifecycle of React Components
2. Virtual DOM
3. Getting started with React using `create-react-app`

_Originally published at [hashnode.com](https://hashnode.com/post/a-reintroduction-to-react-cjsbli2an02b7dys2y3ypng2z)._

