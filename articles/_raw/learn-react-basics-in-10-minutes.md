---
title: Learn React Basics in 10 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-18T01:26:43.000Z'
originalURL: https://freecodecamp.org/news/learn-react-basics-in-10-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/intro-to-react.jpg
tags:
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: 'State Management '
  slug: state-management
seo_title: null
seo_desc: 'By Joe Liang

  If you want to learn the basics of React in the time it takes you to drink a cup
  of coffee, this post is for you.

  This article aims to provide a beginner-friendly introduction to React, what it
  is, and why we need it. It assumes you have...'
---

By Joe Liang

If you want to learn the basics of React in the time it takes you to drink a cup of coffee, this post is for you.

This article aims to provide a beginner-friendly introduction to React, what it is, and why we need it. It assumes you have some understanding of [basic JavaScript](https://1000mileworld.com/learn-javascript-6-golden-knowledge-nuggets-for-beginners/).

We will discuss some of its basic concepts and go over what you can build with React.

We will also discuss some code, but the overall goal is to gain an intuitive understanding of what React is all about so that you get comfortable with the basics.

<h2>What is React?</h2>

Developed by Facebook in 2011, React has quickly become one of the most widely used JavaScript libraries. According to [HackerRank](https://research.hackerrank.com/developer-skills/2018/), 30% of employers look for developers who know React but only about half of the applicants actually have the required knowledge.

Clearly, React is in high demand in the job market.

So what exactly is React?

React is an efficient and flexible JavaScript library for building user interfaces (and React itself is written using JavaScript). It breaks down complex UIs into small, isolated code called “components”. By using these components, React only concerns itself with what you see on the front page of a website.

![React components](https://www.freecodecamp.org/news/content/images/2020/03/React-components.png)
_A calculator app that can be split into React components._

Components are independent and reusable. They can either be JavaScript functions or classes. Either way, they both return a piece of code that represents part of a web page.

Here’s an example of a function component that renders a `<h2>` element onto the page:

```js
function Name() {
  return <h2>Hi, my name is Joe!</h2>;
}

And here is a class component doing the same rendering:

```js
class Person extends React.Component {
  render() {
    return <h2>Hi again from Joe!</h2>;
  }
}

Using a class component takes slightly more effort in that you have to extend React.Component (part of the React library) while a function component is mostly plain JavaScript. However, class components provide certain critical functionalities that function components lack (see [Functional vs Class-Components in React](https://medium.com/@Zwenza/functional-vs-class-components-in-react-231e3fbd7108)).

You may have noticed that there is a strange mixture of HTML and JavaScript inside each component. React actually uses a language called JSX that allows HTML to be mixed with JavaScript.

Not only can you use JSX to return pre-defined HTML elements, you can also create your own. For example, instead of rendering `<h2>` elements directly in the class component, you can render the functional component which returns the same thing:

```js
class Person extends React.Component {
  render() {
    return <Name />;
  }
}

Note the self-closing ‘/>’ of the component.

The power of React starts to become more evident as you can imagine rendering many simple components to form a more complex one.

To build a page, we can call these components in a certain order, use the results they return, and display them to the user.

<h2>Why Choose React Over Vanilla JavaScript?</h2>

Being able to break down complex UIs through the use of components gives React an edge over vanilla JavaScript (plain JS without any external libraries or frameworks). But what else can React do that places it in such high demand among employers?

Let’s take a look at the differences between how React and vanilla JS handle things.

In the previous section, we discussed how React uses components to render UIs. We did not delve into what was happening on the HTML side of things. It may be surprising to learn that the HTML code that pairs with React is really simple:

```html
<div id="root"></div>

It is usually just a `<div>` element with an id that serves as a container for a React app. When React renders its components, it will look for this id to render to. The page is empty before this rendering.

Vanilla JS, on the other hand, defines the initial UI right in the HTML.

In addition, vanilla JS takes care of functionality while HTML takes care of displaying content (markup).

In the earlier days of the web, the separation of functionality and markup sounded logical as apps were simpler. However, as complexity grew so did the headaches of maintaining large pieces of JS code.

JS code that updates a piece of HTML can be spread across several files, and developers may have a hard time keeping track of where the code came from. They have to keep things straight in their heads of all the interactions between the code that resides in different files.

React sorts the code into components, where each component maintains all the code needed to both display and update the UI.

Updating the UI requires updating the DOM, or document object model (see [DOM Manipulation Using JavaScript](https://1000mileworld.com/dom-manipulation-using-javascript/)). This is where React truly shines.

If you want to access the DOM in vanilla JS, you have to first find it before it can be used. React stores the data in regular JS variables and maintains its own _virtual_ DOM.

If you want to then update the DOM in vanilla JS, you have to locate the appropriate node and then manually append or remove elements. React automatically updates the UI based on the application state, which we will discuss in more detail in the next section.

So the primary reason why we may want to use React over vanilla JS can be summarized in one word: simplicity.

With vanilla JS, it’s easy to get lost in a maze of DOM searches and updates. React forces you to break down your app into components which produces more maintainable code.

Thus, for complex apps you will definitely want to learn React.

<h2>Basic React Concepts</h2>

We have already discussed how React uses components to break down complex UIs and JSX to render those components.

In this section we will talk about some more fundamental concepts of React.

<h3>State</h3>

As mentioned previously, React updates the UI based on the application state. This state is actually stored as a property of a React class component:

```js
class Counter extends React.Component {
  state = {
    value: 0
  };
}

Suppose we have a counter and 2 buttons that either increment or decrement. The value of the counter is rendered onto the page through JSX.

The display counter value is based on the state and we change the state by clicking one of the buttons. Vanilla JS treats a button click as an event and so does React. When such an event occurs, we will call functions that either increment or decrement the counter based on the button clicked. These functions have the code that changes the component state.

Here’s an example of such a counter:

```js
class Counter extends React.Component {
  state = {
    value: 0
  };
handleIncrement= () => {
  this.setState(state => {
     value: state.value + 1 
  });
};
handleDecrement= () => {
  this.setState(state => {
     value: state.value - 1 
  });
};
render() {
    return (
      <div>
        <h2>{this.state.value}</h2>
        <button onClick={this.handleDecrement}>Decrement</button>
        <button onClick={this.handleIncrement}>Increment</button>
      </div>
    );
}
};


We updated the state by calling `setState` in each of the functions handling a button click. The counter displayed on the page will update in real time. Thus, React gets its name because it _reacts_ to state changes.

In short, React automatically monitors every component state for changes and updates the DOM appropriately.

<h3>Props</h3>

We can use props (short for "properties") to allow components to talk to each other.

Suppose the counter in our previous example represents the quantity of a product a customer wishes to purchase. The store wants to place a limit of 2 products purchased per customer. At checkout, we want to display an appropriate message if the customer tries to purchase more than 2.

Here’s how we may do it with props:

```js
const Display = (props) => {
   let message;
   if(props.number>2){
	message = ‘You’re limited to purchasing 2 max!’;
   }else{
	message = ‘All’s good.’;
   }
   return(
	<p>message</p>
   );
};

class Timer extends React.Component {
   state = {
	quantity: 0
   }
   //...code for handling button clicking, updating state, etc.
    render(){
        return(
          <Display number = {this.state.quantity} />
          //...code for other components
       );
    }
};

  
We create a functional component called `Display` and pass props as a parameter. When we render this component, we pass to it number as an attribute set to the quantity of the product a customer wants to purchase. This is similar to setting an attribute of an HTML tag. We call this value with `props.number` in `Display` to determine what message to return.

<h3>Component Lifecycle</h3>

As React updates the DOM based on component states, special methods called lifecycle methods exist to provide opportunities to perform actions at specific points in the lifecycle of a component.

They allow you to catch components at a certain point in time to call appropriate functions. These points of time can be before components are rendered, after they are updated, etc. You may want to explore a [component’s lifecycle methods](https://www.freecodecamp.org/news/how-to-understand-a-components-lifecycle-methods-in-reactjs-e1a609840630/).

To see lifecycle methods in action, you can check out this [Pomodoro Clock](https://codepen.io/1000mileworld/full/qBEwRvK) I made.

The clock timer is initially set to the session length. When the session timer counts down to zero, the timer needs to switch to the break length and start counting down from there.

Since the timer is a component, I used the lifecycle method `componentDidUpdate` within my main class component to handle any changes with `handleChange()`:

```js
componentDidUpdate() {
    this.handleChange();
}

You can think of lifecycle methods as adding event listeners in vanilla JS to a React component.

<h2>What Can You Build with React?</h2>

So now you have a basic understanding of React, what can you build with it?

We already mentioned in the beginning of this post that Facebook developed React in 2011, so naturally the Facebook platform is based on React. Other famous apps that either completely or partially use React include Instagram, Netflix, and Whatsapp.

But as beginners of React, we are not looking to immediately build the next Facebook so here’s a list of [10 React Starter Project Ideas to Get You Coding](https://medium.com/@dtkatz/10-react-starter-project-ideas-to-get-you-coding-5b35782e1831).

If you want to learn more about web development and check out some examples of beginner-friendly React projects, visit my blog at [1000 Mile World](https://www.1000mileworld.com/).

Thanks for reading and happy coding!

