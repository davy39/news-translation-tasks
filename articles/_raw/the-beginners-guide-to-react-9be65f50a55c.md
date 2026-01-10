---
title: The Beginner’s Guide to React
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-01-29T13:25:48.000Z'
originalURL: https://freecodecamp.org/news/the-beginners-guide-to-react-9be65f50a55c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uKVfsFREG2HMCL8hJdcZ5Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Interested in learning React? Get my React Handbook


  React is a JavaScript library that aims to simplify the development of visual interfaces.

  Developed at Facebook and released to the world in 2013, it drives some of the most
  widely used code in the...'
---

> Interested in learning React? Get my [React Handbook](https://flaviocopes.com/page/react-handbook/)

React is a JavaScript library that aims to simplify the development of visual interfaces.

Developed at Facebook and released to the world in 2013, it drives some of the most widely used code in the world. It powers Facebook and Instagram among many, many other software companies.

Its primary goal is to make it easy to reason about an interface and its state at any point in time by dividing the UI into a collection of components.

React is used to build single-page web applications, along with many other libraries and frameworks that were available before React came to life.

### Why is React so popular?

React has taken the frontend web development world by storm. Why?

#### Less complex than the alternatives

At the time when React was announced, Ember.js and Angular 1.x were the predominant choices for frameworks. Both of these imposed too many conventions on the code so that porting an existing app was not convenient at all.

React was created to be very easy to integrate into an existing project. That’s how they had to do it at Facebook in order to introduce it to the existing codebase. Also, those two frameworks brought too much to the table, while React only chose to implement the View layer instead of the full MVC stack.

#### Perfect timing

At that same time, Angular 2.x was announced by Google, along with the backwards incompatibility and major changes it was going to bring. Moving from Angular 1 to 2 was like moving to a different framework. And so this fact, along with the execution speed improvements that React promised, made React something developers were eager to try.

#### Backed by Facebook

Being backed by Facebook benefits a project if it turns out to be successful. But it’s not a guarantee, and there are many failed open source projects by both Facebook and Google (among others).

### Is React really that simple?

Even though I said that React is simpler than alternative frameworks, diving into React is still complex. This is mostly because of the corollary technologies that can be integrated with React, like Redux, Relay or GraphQL.

React in itself has a very small API.

There isn’t much more in React other than these concepts:

* Components
* JSX
* State
* Props

We’ll see each one of them in my next articles.

### JSX

Many developers, including myself, at first sight thought that JSX was horrible, and quickly dismissed React.

Even though they said JSX was not required, using React without JSX was painful.

It took me a couple years of occasionally looking at it to start digesting JSX, and now I largely prefer it over the alternative (that is, using templates).

The major benefit of using JSX is that you’re only interacting with JavaScript objects, not template strings.

JSX is not embedded HTML.

Many tutorials for React beginners like to postpone the introduction of JSX for later, because they assume the reader would be better off without it. Since I am now a JSX fan, however, I’ll immediately jump into it.

Here is how you define a h1 tag containing a string:

```jsx
const element = <h1>Hello, world!</h1>
```

It looks like a strange mix of JavaScript and HTML, but in reality it’s all JavaScript.

What looks like HTML is actually a sugar syntax for defining components and their positioning inside the markup.

Inside a JSX expression, attributes can be inserted very easily:

```jsx
const myId = 'test' 
const element = <h1 id={myId}>Hello, world!</h1>
```

You just need to pay attention to when an attribute has a dash (`-`), which is converted to camelCase syntax instead, as well as to these two special cases:

* `class` becomes `className`
* `for` becomes `htmlFor`

because they are reserved words in JavaScript.

Here’s a JSX snippet that wraps two components into a `div` tag:

```jsx
<div> 
  <BlogPostsList />
  <Sidebar /> 
</div>
```

A tag always needs to be closed, because this is more XML than HTML (if you remember the XHTML days, this will be familiar, but since then the HTML5 loose syntax won). In this case, a self-closing tag is used.

JSX, when introduced with React, is no longer a React-only technology.

### React Components

#### What is a React Component?

A component is one isolated piece of the interface. For example, in a typical blog homepage, you might find the Sidebar component and the Blog Posts List component. They are in turn composed by components themselves, so you could have a list of Blog post components, each for every blog post, and each with its own peculiar properties.

![Image](https://cdn-media-1.freecodecamp.org/images/Ok51aJciCr9ybh8lww0UL2Hl7g37lC2MJjne)

React makes it very simple: everything is a component.

Even plain HTML tags are components on their own, and they are added by default.

The next two lines are equivalent — they do the same thing. One with **JSX**, one without, by injecting `<h1>Hello World`!</h1> into an elem`ent` with id app.

```jsx
import React from 'react' 
import ReactDOM from 'react-dom' 

ReactDOM.render( 
  <h1>Hello World!</h1>, 
  document.getElementById('app') 
)

ReactDOM.render( 
  React.DOM.h1(null, "Hello World!"), 
  document.getElementById('app') 
)
```

See, `React.DOM` exposed for us an `h1` component. Which other HTML tags are available? All of them! You can inspect what `React.DOM` offers by typing it in the Browser Console:

![Image](https://cdn-media-1.freecodecamp.org/images/9DaF1EtL86DXgUhe2wvb92sjYFLx6S5nxcIr)

(the list goes on…)

The built-in components are nice, but you’ll quickly outgrow them. What React excels at is letting us compose a UI by composing custom components.

### Custom components

There are 2 ways to define a component in React:

A stateless component does not manage internal state, and is just a function:

```jsx
const BlogPostExcerpt = () => {
 return (
    <div>
      <h1>Title</h1>
      <p>Description</p>
    </div> 
  ) 
}
```

A stateful component is a class, which manages state in its own properties:

```jsx
import React, { Component } from 'react'

class BlogPostExcerpt extends Component { 
  render() { 
    return ( 
      <div>
        <h1>Title</h1> 
        <p>Description</p> 
      </div> 
    ) 
  } 
}
```

As they stand, they are equivalent because there is no state management yet (coming in the next couple articles).

There is a third syntax which uses the `ES5` / `ES2015` syntax without the classes:

```jsx
import React from 'react'

React.createClass({ 
  render() { 
    return ( 
      <div> 
        <h1>Title</h1>
        <p>Description</p> 
      </div> 
    ) 
  } 
})
```

You’ll rarely see this in modern `> ES6` codebases.

Props is how Components get their properties. Starting from the top component, every child component gets its props from the parent. In a stateless component, props is all that gets passed, and they are available by adding `props` as the function argument:

```jsx
const BlogPostExcerpt = (props) => { 
  return ( 
    <div> 
      <h1>{props.title}</h1> 
      <p>{props.description}</p> 
    </div> 
  ) 
}
```

In a stateful component, props are passed by default. There is no need to add anything special, and they are accessible as `this.props` in a Component instance.

```jsx
import React, { Component } from 'react'

class BlogPostExcerpt extends Component { 
  render() { 
    return ( 
      <div>
        <h1>{this.props.title}</h1>  
        <p>{this.props.description}</p> 
      </div> 
    ) 
  } 
}
```

### PropTypes

Since JavaScript is a dynamically typed language, we don’t really have a way to enforce the type of a variable at compile time. If we pass invalid types, they will fail at runtime or give weird results if the types are compatible but not what we expect.

Flow and TypeScript help a lot, but React has a way to directly help with props types. Even before running the code, our tools (editors, linters) can detect when we are passing the wrong values:

```jsx
import PropTypes from 'prop-types';
import React from 'react' 

class BlogPostExcerpt extends Component { 
  render() { 
    return ( 
      <div> 
        <h1>{this.props.title}</h1> 
        <p>{this.props.description}</p> 
      </div> 
    ) 
  } 
}

BlogPostExcerpt.propTypes = { 
  title: PropTypes.string, 
  description: PropTypes.string 
};

export default BlogPostExcerpt
```

### Which types can we use

These are the fundamental types we can accept:

* PropTypes.array
* PropTypes.bool
* PropTypes.func
* PropTypes.number
* PropTypes.object
* PropTypes.string
* PropTypes.symbol

We can accept one of two types:

```jsx
PropTypes.oneOfType([ PropTypes.string, PropTypes.number ]),
```

We can accept one of many values:

```jsx
PropTypes.oneOf(['Test1', 'Test2']),
```

We can accept an instance of a class:

```jsx
PropTypes.instanceOf(Something)
```

We can accept any React node:

```jsx
PropTypes.node
```

or even any type at all:

```jsx
PropTypes.any
```

Arrays have a special syntax that we can use to accept an array of a particular type:

```jsx
PropTypes.arrayOf(PropTypes.string)
```

We can compose an object property by using:

```jsx
PropTypes.shape({ 
  color: PropTypes.string, 
  fontSize: PropTypes.number 
})

```

### Requiring properties

Appending `isRequired` to any PropTypes option will cause React to return an error if that property is missing:

```jsx
PropTypes.arrayOf(PropTypes.string).isRequired, PropTypes.string.isRequired,
```

### Default values for props

If any value is not required, we need to specify a default value for it if it’s missing when the Component is initialized.

```jsx
BlogPostExcerpt.propTypes = { 
  title: PropTypes.string, 
  description: PropTypes.string 
}

BlogPostExcerpt.defaultProps = { 
  title: '', 
  description: '' 
}
```

Some tooling, like ESLint, has the ability to enforce defining the defaultProps for a Component with some propTypes not explicitly required.

### How props are passed

When initializing a component, pass the props in a way similar to HTML attributes:

```jsx
const desc = 'A description' 
//... 
<BlogPostExcerpt title="A blog post" description={desc} />

```

We passed the title as a plain string (something we can _only_ do with strings!), and the description as a variable.

### Children

A special prop is `children`. That contains the value of anything that is passed in the `body` of the component. For example:

```jsx
<BlogPostExcerpt title="A blog post" description={desc}> 
  Something 
</BlogPostExcerpt>

```

In this case, inside `BlogPostExcerpt` we could access “Something” by looking up `this.props.children`.

While Props allow a Component to receive properties from its parent (they could be “instructed” to print some data for example), state allows a component to take on a life of its own, and be independent from the surrounding environment.

Remember: only class-based Components can have a state. So if you need to manage state in a stateless (function-based) Component, you first need to “upgrade” it to a Class component:

```jsx
const BlogPostExcerpt = () => { 
  return ( 
    <div>
      <h1>Title</h1>
      <p>Description</p> 
    </div> 
  )
}

```

becomes:

```jsx
import React, { Component } from 'react'

class BlogPostExcerpt extends Component { 
  render() { 
    return (
      <div>  
        <h1>Title</h1> 
        <p>Description</p>
      </div>
    ) 
  } 
}

```

### Setting the default state

In the Component constructor, initialize `this.state`. For example, the BlogPostExcerpt component might have a `clicked` state:

```jsx
class BlogPostExcerpt extends Component {
  constructor(props) { 
    super(props) 
    this.state = { clicked: false } 
  }

  render() { 
    return (
      <div> 
        <h1>Title</h1>
        <p>Description</p> 
      </div> 
    ) 
  } 
}
```

### Accessing the state

The _clicked_ state can be accessed by referencing `this.state.clicked`:

```jsx
class BlogPostExcerpt extends Component {
  constructor(props) { 
    super(props)
    this.state = { clicked: false }
  }

  render() { 
    return (
      <div> 
        <h1>Title</h1> 
        <p>Description</p> 
        <p>Clicked: {this.state.clicked}</p> 
      </div> 
    ) 
  } 
}
```

### Mutating the state

A state should never be mutated by using

```jsx
this.state.clicked = true
```

Instead, you should always use `setState()` instead, passing it as an object:

```jsx
this.setState({ clicked: true })
```

The object can contain a subset, or a superset, of the state. Only the properties you pass will be mutated. The ones omitted will be left in their current state.

#### Why you should always use `setState()`

The reason is that using this method, React knows that the state has changed. It will then start the series of events that will lead to the Component being re-rendered, along with any DOM updates.

### State is encapsulated

A parent of a Component cannot tell if the child is stateful or stateless. The same goes for children of a Component.

Being stateful or stateless (functional or class-based) is entirely an implementation detail that other components don’t need to care about.

This leads us to Unidirectional Data Flow

### Unidirectional Data Flow

A state is always owned by one Component. Any data that’s affected by this state can only affect Components below it: its children.

Changing a state on a Component will never affect its parent, or its siblings, or any other Component in the application — just its children.

This is the reason that, many times, the state is moved up in the Components tree.

### Moving the State Up in the Tree

Because of the Unidirectional Data Flow rules, if two components need to share a state, the state needs to be moved up to a common ancestor.

Often, the closest ancestor is the best place to manage the state, but it’s not a mandatory rule.

The state is passed down to the components that need that value via props:

```jsx
class Converter extends React.Component { 
  constructor(props) { 
    super(props)
    this.state = { currency: '€' } 
  }

  render() { 
    return ( 
      <div> 
        <Display currency={this.state.currency} />
        <CurrencySwitcher currency={this.state.currency} />
      </div> 
    ) 
  } 
}

```

The state can be mutated by a child component by passing a mutating function down as a prop:

```jsx
class Converter extends React.Component { 
  constructor(props) { 
    super(props) 
    this.state = { currency: '€' } 
  }

  handleChangeCurrency = (event) => { 
    this.setState({ 
      currency: this.state.currency === '€' ? '$' : '€' 
    }) 
  }

  render() { 
    return ( 
      <div> 
        <Display currency={this.state.currency} /> 
        <CurrencySwitcher currency={this.state.currency} handleChangeCurrency={this.handleChangeCurrency} /> 
      </div> 
    ) 
  } 
}

const CurrencySwitcher = (props) => { 
  return ( 
    <button onClick={props.handleChangeCurrency}> 
      Current currency is {props.currency}. Change it! 
    </button> 
  ) 
}

const Display = (props) => { 
  return ( 
    <p>Current currency is {props.currency}.</p> 
  ) 
}

```

![Image](https://cdn-media-1.freecodecamp.org/images/W5hfnSrCoSOqkbTNbDn0b1bOocYiHkO70ZgB)

### Events

React provides an easy way to manage events. Prepare to say goodbye to `addEventListener` :)

In the previous article about the State you saw this example:

```jsx
const CurrencySwitcher = (props) => { 
  return ( 
    <button onClick={props.handleChangeCurrency}> 
      Current currency is {props.currency}. Change it! 
    </button> 
  ) 
}

```

If you’ve been using JavaScript for a while, this is just like plain old JavaScript event handlers. But this time you’re defining everything in JavaScript, not in your HTML, and you’re passing a function, not a string.

The actual event names are a little bit different, because in React you use camelCase for everything. So `onclick` becomes `onClick`, `onsubmit` becomes `onSubmit`.

For reference, this is old school HTML with JavaScript events mixed in:

```jsx
<button onclick="handleChangeCurrency()"> ... <;/button>
```

### Event handlers

It’s a convention to have event handlers defined as methods on the Component class:

```jsx
class Converter extends React.Component { handleChangeCurrency = (event) => { this.setState({ currency: this.state.currency === '€' ? '$' : '€' }) } }

```

All handlers receive an event object that adheres, cross-browser, to the [W3C UI Events spec](https://www.w3.org/TR/DOM-Level-3-Events/).

### Bind `this` in methods

Don’t forget to bind methods. The methods of ES6 classes by default are not bound. What this means is that `this` is not defined unless you define methods as

```jsx
class Converter extends React.Component { 
  handleClick = (e) => { /* ... */ } 
  //... 
}

```

when using the the property initializer syntax with Babel (enabled by default in `create-react-app`).

Otherwise you need to bind it manually in the constructor:

```jsx
class Converter extends React.Component { 
  constructor(props) { 
    super(props); 
    this.handleClick = this.handleClick.bind(this); 
  }

  handleClick(e) {} 
}

```

### The events reference

There are lots of events supported, so here’s a summary list.

#### Clipboard

* onCopy
* onCut
* onPaste

#### Composition

* onCompositionEnd
* onCompositionStart
* onCompositionUpdate

#### Keyboard

* onKeyDown
* onKeyPress
* onKeyUp

#### Focus

* onFocus
* onBlur

#### Form

* onChange
* onInput
* onSubmit

#### Mouse

* onClick
* onContextMenu
* onDoubleClick
* onDrag
* onDragEnd
* onDragEnter
* onDragExit
* onDragLeave
* onDragOver
* onDragStart
* onDrop
* onMouseDown
* onMouseEnter
* onMouseLeave
* onMouseMove
* onMouseOut
* onMouseOver
* onMouseUp

#### Selection

* onSelect

#### Touch

* onTouchCancel
* onTouchEnd
* onTouchMove
* onTouchStart

#### UI

* onScroll

#### Mouse Wheel

* onWheel

#### Media

* onAbort
* onCanPlay
* onCanPlayThrough
* onDurationChange
* onEmptied
* onEncrypted
* onEnded
* onError
* onLoadedData
* onLoadedMetadata
* onLoadStart
* onPause
* onPlay
* onPlaying
* onProgress
* onRateChange
* onSeeked
* onSeeking
* onStalled
* onSuspend
* onTimeUpdate
* onVolumeChange
* onWaiting

#### Image

* onLoad
* onError

#### Animation

* onAnimationStart
* onAnimationEnd
* onAnimationIteration

#### Transition

* onTransitionEnd

### React’s Declarative approach

You’ll run across articles describing React as a **declarative approach to building UIs**.

See [declarative programming](https://flaviocopes.com/functional-programming-js/declarative) to read more about declarative programming.

### React declarative approach

React made its “declarative approach” quite popular and upfront so it permeated the frontend world along with React.

It’s really not a new concept, but React made building UIs a lot more declarative than with HTML templates. You can build Web interfaces without even touching the DOM directly, and you can have an event system without having to interact with the actual DOM Events.

For example, looking up elements in the DOM using jQuery or DOM events is an iterative approach.

React’s declarative approach abstracts that for us. We just tell React we want a component to be rendered in a specific way, and we never have to interact with the DOM to reference it later.

### The Virtual DOM

Many existing frameworks, before React came on the scene, were directly manipulating the DOM on every change.

### The “real” DOM

What is the DOM, first of all? The DOM (_Document Object Model_) is a Tree representation of the page, starting from the `<ht`ml> tag, going down into each of the children, called nodes.

It’s kept in the browser memory, and directly linked to what you see in a page. The DOM has an API that you can use to traverse it, access every single node, filter them, and modify them.

The API is the familiar syntax you have likely seen many times, if you were not using the abstract API provided by jQuery and friends:

```jsx
document.getElementById(id) 
document.getElementsByTagName(name) 
document.createElement(name) 
parentNode.appendChild(node) 
element.innerHTML 
element.style.left 
element.setAttribute()
element.getAttribute() 
element.addEventListener() 
window.content 
window.onload 
window.dump()
window.scrollTo()
```

React keeps a copy of the DOM representation, because the Virtual DOM concerns the React rendering.

### The Virtual DOM

Every time the DOM changes, the browser has to do two intensive operations: repaint (visual or content changes to an element that do not affect the layout and positioning relative to other elements) and reflow (recalculate the layout of a portion of the page — or the whole page layout).

React uses a Virtual DOM to help the browser use fewer resources when changes need to be made on a page.

When you call `setState()` on a Component, specifying a state different than the previous one, React marks that Component as **dirty**. This is key: React only updates when a Component changes the state explicitly.

What happens next is:

* React updates the Virtual DOM relative to the components marked as dirty (with some additional checks, like triggering `shouldComponentUpdate()`)
* Runs the diffing algorithm to reconcile the changes
* Updates the real DOM

### Why is the Virtual DOM helpful: batching

The key thing is that React batches much of the changes and performs a unique update to the real DOM. It does this by changing all the elements that need to be changed at the same time, so the repaint and reflow the browser must perform to render the changes are executed just once.

> Interested in learning React? Get my [React Handbook](https://flaviocopes.com/page/react-handbook/)

