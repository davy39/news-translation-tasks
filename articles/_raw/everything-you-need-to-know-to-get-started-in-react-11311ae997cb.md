---
title: Everything you need to know to get started in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-08T19:36:49.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-to-get-started-in-react-11311ae997cb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8ErnbNtq1QtnahH2VSCohQ.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Abdul Moiz Ansari


  “The hardest thing about getting started, is getting started” - Guy Kawasaki


  React is the most popular Front End Library in use today. But getting started on
  React can be hard at times. There is Component Hierarchy, states, pro...'
---

By Abdul Moiz Ansari

> “The hardest thing about getting started, is getting started” - Guy Kawasaki

React is the most popular Front End Library in use today. But getting started on React can be hard at times. There is Component Hierarchy, states, props and functional programming involved. This article tries to solve this problem, by giving you a nice and easy way of getting started in React. So without wasting any time, let’s jump in.

### Environment

We will use a simple HTML file in this article. Just make sure to include the following script tags in the head section of your HTML file.

```html
<script src="https://unpkg.com/react@16/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.js"></script>
```

So our working file should look like this.

```html
<!DOCTYPE html>
<html>
<head>    
    <title>My React App</title>

    <script src="https://unpkg.com/react@16/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.26.0/babel.js"></script>    
</head>
<body>
    
    <div id="root"></div>

    <script type="text/babel" >   
    
       //React code should go here
    </script>
</body>
</html>
</script></body></html>
```

We are good to go now.

![Image](https://cdn-media-1.freecodecamp.org/images/Dgrr7QYoN3uYtpLisYwkUzzXyuj-oQhyZdNH)
_credits : [https://www.pexels.com](https://www.pexels.com/photo/flight-sky-earth-space-2166/" rel="noopener" target="_blank" title=")_

### Components

Components are the meat and potatoes of a React application.

They are independent and reusable blocks of code that build a React application.

Let’s look at our first component.

```js
class App extends React.Component{
 render(){
  return <h3>Hello React World.</h3>
 }
}
ReactDOM.render(            
 <App />,
 document.getElementById('root')
);
```

Our App component is an ES6 class which extends the Component class of React. It has a single method for now called `render`, which returns an **h3** element returning the text ‘Hello React World’. The browser will only render elements returned by the `render()` method.

#### **But wait a minute, is that render method necessary?**

Yes, a class component must include a render method. All the other methods are optional.

`ReactDOM.render()` is rendering the App component in a div element with the id ‘root’. It takes the component as the first parameter and parent div as the second parameter.

#### JavaScript Syntax Extension (JSX)

The h3 element we declared in the App component is not HTML, it’s JavaScript Syntax Extension (JSX). JSX is a syntax extension in JavaScript. It enables us to write HTML like JavaScript Objects(JSX) in JavaScript.

```js
class App extends React.Component{
 render(){
  const element = <h3>Hello React World</h3>;
  return <div>{element}</div>;
 }
}
```

JSX gives us the power of JavaScript while writing HTML. Those curly braces `{}` in the example above tell the React compiler that **element** is a JavaScript variable. Let’s see another more practical example.

```js
render() {
 const users = [‘Abdul Moiz’,’Linda Lee’,’John Frank’];
 const listItems = users.map(user => <li>{user}</li>);
 return <ul>{listItems}</ul>; 
}
```

In the example above, we have a list of users in an array that we’ve mapped on the list and made an array of `li` elements. We’ll use this in our `ul` element later.

JSX is the recommended way and the industry de facto standard to declare your UI in React.

### Props

Props are the properties passed by the parent component to child components.

It is a common pattern in React to abstract away the common UI logic in child components. In those cases, it is common for the parent component to pass some data as properties in child components.

```js
class App extends React.Component {
 render() {
  return <Greet greeting="Hello" />;  
 }
}
class Greet extends React.Component{
 render(){
  return <h3>{this.props.greeting} World</h3>;
 }
}
```

In the example above, we have passed a greeting prop to the Greet component and used it in our App component. We can access all the props from the _this.props_ object of our class. In this case, we are accessing _greeting_ as _this.props.greeting_.

#### **OK, but what type of data can I pass in props?**

Pretty much every default data structure in JavaScript: string literals, numbers, array, objects, and even functions. Yes we can pass functions, but we won’t be getting into that right now.

### State

State, like props, also holds data, but some different types of data.

Props hold the data sent by the parent component. State holds the private, dynamic data of the component. State holds the data which changes between multiple renderings of the component.

> Props get passed to the component (like function parameters), whereas state is managed within the component (like variables declared within a function) - React Docs

Complex? Don’t worry, it will all make sense in a moment.

```js
class App extends React.Component {
 constructor(){
  super();
  this.state = {name :"Abdul Moiz"};
 }
 changeName(){
  this.setState({name : "John Doe"});
 }
 
 render(){
  return (
   <div>
     <h3>Hello {this.state.name}</h3>
     <button type='button' onClick=this.changeName.bind(this)}>
      Change
     </button>
   </div>
  );
 }
}
```

As we can see, we have to initialize the state in a constructor and then we can use it in the render method. Like props, we are accessing state with the ‘this.state’ object. And on the click event of our _Change_ button, we are changing the value of name in state to ‘John Doe’.

#### **setState()**

We are using the _setState()_ method to change our state. _setState()_ is available by default in React Component and is the only way to change state. We are passing an object as the parameter to _setState()_. React will look at the passed object and will change only the provided keys of the state with the provided values.

**But wait a minute, if _setState()_ is the only way to change the state, does this mean that I cannot change the state straight away?**

Yes, we cannot change the state straight away like this:

```
this.state.name = “John Doe”;
```

Because when we call _setState()_, it tells React that data has been changed and we need to re-render the component with the updated data. Updating the state straight away will have no effect on UI.

### Event Handlers

Event handlers in React are not very different from event handlers in the DOM. But they have some small yet important differences.

In the DOM, event handlers are lowercase, but in React, event handlers are camelCase. Secondly, in the DOM, event handlers take value as a string, but in React, event handlers take function reference as value.

The following is an example of how we handle an event in the DOM:

```
<button type=”submit” onclick=”doSomething()”></button>
```

And here’s how it’s done in React:

```
<button type=”submit” onClick=doSomething></button>
```

If you notice, in the DOM, we’re handling the click event using the `onclick` (lowercase) DOM property. While in React, we are using the `onClick` (camelCase) event handler from React. Also, we are passing a string value `doSomething()` in the DOM. But in React, we are passing the reference of the function `doSomething` as the value.

If you want to read about the full list of events provided by React (as usual, there are tons of them), consider reading [this article](https://reactjs.org/docs/events.html#supported-events) from the official docs.

Tired? Me too, but we are almost there — keep up the learning!

### Life Cycle Methods (Life Cycle Hooks)

React gives us some special methods called Life Cycle Hooks. These life cycle hooks run at particular times in a the life cycle of a component. Luckily, we can put our own functionality in those life cycle hooks, by overriding them in our component. Let’s look at some of the commonly used life cycle hooks.

#### componentDidMount()

Mounting is the time when the component gets rendered for the first time in the browser. `componentDidMount()` runs after the component gets mounted. It is a good place to fetch any data or initiate anything.

#### componentDidUpdate()

As its name suggests, `componentDidUpdate()` runs after the component gets updated. It is the place to handle data changes. Maybe you want to handle some network requests, or perform calculations based on the changed data. `componentDidUpdate()` is the place to do all of that.

Let’s see that in action:

```js
class App extends React.Component {
 constructor(){
  super(); 
  this.state = {
   person : {name : "" , city : ""}
  };
 }
 componentDidMount(){
  //make any ajax request
  this.setState({
   person : {name : "Abdul Moiz",city : "Karachi"}
  });
 }
 componentDidUpdate(){
  //because I could'nt come up with a simpler example of //componentDidUpdate
  console.log('component has been updated',this.state);
 }
 render(){
  return (
   <div>
    <p>Name : {this.state.person.name}</p>
    <p>City : {this.state.person.city}</p>
   </div>
  );
 }
}
```

Our initial state has two properties, name and city, and both have an empty string as value. In `componentDidMount()` we set the state and change name to ‘Abdul Moiz’ and city to ‘Karachi’. Because we changed the state, the component updated as a result of executing `componentDidUpdate()`.

### Conclusion

React is here to stay. Learning React can be difficult, but you will love it once you surpass the initial learning curve. This article was meant to make that learning process a little bit easier for you.

And don’t forget to follow me on [Twitter](http://twitter.com/@aamoizansari).

#### Resources

* [https://reactjs.org/docs](https://reactjs.org/docs/faq-state.html)
* [http://lucybain.com/blog](http://lucybain.com/blog/2016/react-state-vs-pros/)
* [https://thinkster.io](https://thinkster.io)

