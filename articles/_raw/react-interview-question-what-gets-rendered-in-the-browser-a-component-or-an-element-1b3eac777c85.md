---
title: 'React Interview Question: What gets rendered in the browser, a component or
  an element?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-13T22:44:15.000Z'
originalURL: https://freecodecamp.org/news/react-interview-question-what-gets-rendered-in-the-browser-a-component-or-an-element-1b3eac777c85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mXjNHOx9bbQ5D4sSUAX2Lg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Samer Buna\n Trick Question \nYou might not like the answer because,\
  \ unfortunately, it is a bit complicated.\n\nIsn’t the word element synonymous to\
  \ the word component anyway??\n\n\nForm reactjs.org\n\nUpdate: This article is now\
  \ part of my book “React.js ..."
---

By Samer Buna

#### ** Trick Question **

You might not like the answer because, unfortunately, it is a bit complicated.

> Isn’t the word **element** synonymous to the word **component** anyway??

![Image](https://cdn-media-1.freecodecamp.org/images/1*mXjNHOx9bbQ5D4sSUAX2Lg.png)
_Form reactjs.org_

> **Update:** This article is now part of my book “React.js Beyond The Basics”.

> Read the updated version of this content and more about React at [**_jscomplete.com/react-beyond-basics_**](https://jscomplete.com/g/component-or-element)_._

Technically speaking, ReactDOM does not render a React component or a React element in the DOM. It renders **DOM elements backed by instances of their components**. This is true for class components. For function components, ReactDOM renders just DOM elements. Function components don’t have instances (that can be accessed with `this`) so when using a function component, ReactDOM renders a DOM element generated from the function’s returned element.

What you need to understand here is that a React element is different from a DOM element. A React element is just a **description** of an HTML element, a React component, or a mix of these.

Okay, a better interview question might be: **When you use something like `<MyComponent` /> in JSX, is that a component, an element, or an ins**tance?

It’s an **element** but not a DOM element. It’s a React element. The clue here is that any JSX tag gets translated to a `React.createElement` call. Keep that in mind. CREATE. **ELEMENT**.

However, for React to continue working with this React element, it will have to either invoke a function or create an instance from a class.

You might find the words **component**, **element**, and **instance** mixed up in the React guides and tutorials out there. I am guilty of mixing these words myself, but I think a beginner React learner needs to understand the important distinctions. The React blog has a [post about this topic](https://reactjs.org/blog/2015/12/18/react-components-elements-and-instances.html) but that I think it is a bit too technical for a beginner.

Here is how I would provide simple definitions of these word to beginners:

* A React **Component** is a template. A blueprint. A global definition. This can be either a **function** or a **class** (with a render function).
* A React **Element** is what gets **returned** from components. It’s an object that virtually describes the DOM nodes that a component represents. With a function component, this element is the object that the function returns. With a class component, the element is the object that the component’s render function returns. React elements are not what we see in the browser. They are just objects in memory and we can’t change anything about them.
* React internally creates, updates, and destroys **instances** to figure out the DOM elements tree that needs to be rendered to the browser. When working with class components, it’s common to refer to their browser-rendered DOM elements as component instances. You can render many instances of the same component. The instance is the “`this`” keyword that you use inside class-based components. You would not need to create an instance from a class manually. You just need to remember that it’s there somewhere in React’s memory.
* Function-based React elements do not have instances. A function component can still be rendered multiple times but React just does not associate a local instance with each render. It just uses the invocation of the function to determine what DOM element to render for the function.

The bottom line is that ReactDOM does not render components in the browser, and it does not render elements either (in the sense of keeping the term element to represent the result of `React.createElement`). It also does not render instances. **It renders DOM elements.**

Unfortunately, it seems to be a common practice out there to use the term component to mean both the template and any instances or invocations used though the template. I don’t blame anyone for being confused here. This is a bit painful.

#### What’s the story here?

Every React App starts with a `render` call that uses a **React element**. Let’s use the `HelloMessage` example from [reactjs.org](https://reactjs.org/) slightly modified to have a function component as well:

```
const Today = () => (  <div>Today is {new Date().toDateString()}</div>);
```

```
class HelloMessage extends React.Component {  render() {    return (      <React.Fragment>        <div>Hello {this.props.name}</div>        <Today />      </React.Fragment>    );  }}
```

```
ReactDOM.render(  <HelloMessage name="Taylor" />,  mountNode);
```

The first React element is the one we start with in the `ReactDOM.render` call:

```
<HelloMessage name="Taylor" /> // This is a React element
```

This React element describes that the DOM tree to be rendered should start with the `HelloMessage` component and a `name` prop value that’s equal to `Taylor`.

**React now needs to answer the question: What is `HelloMessage`?**

Every time a React element describes a React component (like the React element we have above), React uses the component to replace that description with what the component returns. It creates an instance for class-based components at this point and keeps a reference of that in memory. It does not create anything for function-based components; it just invokes them.

What gets returned from the `HelloMessage` component is a React element that describes a `React.Fragment` component.

**React now needs to answer the question: What is `React.Fragment`?**

React will keep reducing these unknown descriptions of components until it has only valid DOM nodes. The description of `React.Fragment` gets translated into 2 React elements, one describing a `div` and another describing a `Today` component.

**React now needs to answer the question: What is `Today`?**

It calls the `Today` function to figure this last question out. The `Today` function returns a React element that describes a `div`.

At this point, the virtual tree is complete with all React elements that describe DOM nodes. React uses its reconciliation algorithm to figure out what to update in the browser. The nodes that were translated with a component instance retain the power of modifying that instance.

**Did this clear things up a bit or did I confuse the terms a bit more? Let me know in the responses below.**

Thanks for reading.

Learning React or Node? Checkout my books:

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)

