---
title: What the heck is JSX and why you should use it to build your React apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T17:29:36.000Z'
originalURL: https://freecodecamp.org/news/what-the-heck-is-jsx-and-why-you-should-use-it-to-build-your-react-apps-1195cbd9dbc6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*o7WmwGkLVR0dVQUYqfSBeg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ryan Harris

  As developers, we use a variety of tools and open source packages to make our jobs
  easier. Some of them are so widely used throughout the community that they seem
  native to JavaScript. But, they’re not, and they can fundamentally chang...'
---

By Ryan Harris

As developers, we use a variety of tools and open source packages to make our jobs easier. Some of them are so widely used throughout the community that they seem native to JavaScript. But, they’re not, and they can **fundamentally change how you write code** on a daily basis.

One of these technologies that you are probably using already is JSX - **a XML like syntax extension for JavaScript**. Created by the team at Facebook, it is intended to simplify the developer experience. As the spec says, the rationale for creating JSX was:

> “…to define a concise and familiar syntax for defining tree structures with attributes.” ~ [JSX Spec](https://facebook.github.io/jsx/)

Now, you’re probably saying to yourself, “Hey, Ryan, this sounds great, but **get to the code already**”, so here’s our first example.

```
const helloWorld = <h1>Hello, World!</h1>;
```

And that’s it!

The code snippet above looks familiar, but have you ever stopped to think about its power? JSX makes it so we can **pass around tree structures composed of HTML or React elements** as if they were standard JavaScript values.

While you don’t have to use JSX when writing React ([or use React in order to try JSX](https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-jsx)), there’s no denying it is an important part of the React ecosystem, so let’s dive in and see what’s going on under the hood.

#### Getting started with JSX

The first thing to note when using JSX syntax is that React must be in scope. This is due to how it gets compiled. Take this component for example:

```
function Hello() {  return <h1>Hello, World!</h1>}
```

Behind the scenes, each element rendered by the `Hello` component is transpiled into to a `React.createElement` call.

In this case:

```
function Hello() {  return React.createElement("h1", {}, "Hello, World!")}
```

![Image](https://cdn-media-1.freecodecamp.org/images/i45KojKuegRdDklO7hgQUgFvqxOIUvvI-hZv)
_Image source [rawpixel](https://unsplash.com/@rawpixel" rel="noopener" target="_blank" title=")_

The same is true for nested elements. The two examples below would ultimately render the same markup.

```
// Example 1: Using JSX syntaxfunction Nav() {  return (    <ul>      <li>Home</li>      <li>About</li>      <li>Portfolio</li>      <li>Contact</li>    </ul>  );}
```

```
// Example 2: Not using JSX syntaxfunction Nav() {  return (    React.createElement(      "ul",      {},      React.createElement("li", null, "Home"),      React.createElement("li", null, "About"),      React.createElement("li", null, "Portfolio"),      React.createElement("li", null, "Contact")    )  );}
```

#### React.createElement

When React creates elements, it calls this method, which takes three arguments.

1. The element name
2. An object representing the element’s props
3. An array of the element’s children

One thing to note here is that React interprets lowercase elements as HTML and Pascal case (ex. ThisIsPascalCase) elements as custom components. Because of this, the following examples would be interpreted differently.

```
// 1. HTML elementReact.createElement("div", null, "Some content text here")
```

```
// 2. React elementReact.createElement(Div, null, "Some content text here")
```

The first example would generate a `<d`iv> with the s`tring "Some content text` here" as its child. However, the second version would throw an error (unless, of course, a custom comp`onent &`lt;Div /> was in sco`pe) bec`ause <Div /> is undefined.

#### Props in JSX

When working in React, your components often render children and need to pass them data in order for the children to render properly. These are called props.

I like to think of React components as a group of friends. And what do friends do? They [give each other props](https://www.urbandictionary.com/define.php?term=props). Thankfully, JSX offers us a number of ways to do that.

```
// 1. Props defaulted to true<User loggedIn />
```

```
// 2. String literals<User name="Jon Johnson" />
```

```
// 3. JavaScript expressions<User balance={5 + 5 + 10} />
```

```
// 4. Spread attributes<User preferences={...this.state} />
```

But beware! You cannot pass if statements or for loops as props because they are [statements, not expressions](https://dev.to/promhize/javascript-in-depth-all-you-need-to-know-about-expressions-statements-and-expression-statements-5k2).

![Image](https://cdn-media-1.freecodecamp.org/images/540ZKVGYlZkyJmuY6dpHkUwAozpqC2Xf4l5w)
_Image source [Kevin Ku](https://unsplash.com/@ikukevk" rel="noopener" target="_blank" title=")_

#### Children in JSX

As you are building your app, you eventually start having components render children. And then those components sometimes have to render children. And so on and so forth.

Since JSX is meant to make it easy for us to reason about tree-like structures of elements, it makes all of this very easy. Basically, whatever elements a component returns become its children.

There are four ways to render child elements using JSX:

#### Strings

This is the simplest example of JSX children. In the case below, React creates a `<`h1> HTML element with one child. The child, however, is not another HTML element, just a simple string.

```
function AlertBanner() {  return (    <h1>Your bill is due in 2 days</h1>  )}
```

#### **JSX Elements**

This is probably the use case that new React developers would be most familiar with. In the component below, we’re returning an HTML child (the `<head`er>), which has two children of it`s own &`lt;Na`v /> and &l`t;ProfilePic /> both of which are custom defined JSX elements.

```
function Header(props) {  return (    <header>      <Nav />      <ProfilePic />    </header>  )}
```

#### **Expressions**

Expressions allow us to easily render elements in our UI that are the result of a JavaScript computation. A simple example of this would be basic addition.

Say we have a component called `<BillFooter` /> that renders information about a bill or receipt. Let’s assume it takes one prop c`alled` total that represents the pre-tax cost and another `prop t`axRate, which represents the applicable tax rate.

Using expressions, we can easily render out some useful information for our users!

```
function BillFooter(props) {  return (    <div>      <h5>Tax: {props.total * props.taxRate}</h5>      <h5>Total: {props.total + props.total * props.taxRate}</h5>    </div>  );}
```

#### **Functions**

With functions, we can programmatically create elements and structures, which React will then render for us. This makes it easy to create multiple instances of a component or render repeated UI elements.

As an example, let’s use JavaScript’s `.map()` function to create a navigation bar.

```
// Array of page informationconst pages = [  {    id: 1,    text: "Home",    link: "/"  },  {    id: 2,    text: "Portfolio",    link: "/portfolio"  },  {    id: 3,    text: "Contact",    link: "/contact"  }];// Renders a <ul> with programmatically created <li> childrenfunction Nav() {  return (    <ul>      {pages.map(page => {        return (          <li key={page.id}>            <a href={page.link}>{page.text}</a>          </li>        );      })}    </ul>  );}
```

Now, if we want to add a new page to our site, all we need to do is add a new object to the `pages` array and React will take care of the rest!

**Take note of the** `key` **prop**. Our function returns an array of sibling elements, in this case `<`li>s, and React needs a way to keep track of which mounts, unmounts or updates. To do that, it relies on this unique identifier for each element.

#### Use the tools!

![Image](https://cdn-media-1.freecodecamp.org/images/ry5AANkjQySL0wIL0UlvdjlsG8ZHH720HGtf)
_Image source [Barn Images](https://unsplash.com/@barnimages" rel="noopener" target="_blank" title=")_

Sure, you can write React applications without JSX, but I’m not really sure why you’d want to.

The ability JSX gives us to pass around elements in JavaScript like they were first-class citizen lends itself well to working with the rest of the React ecosystem. So well, in fact, you may have been writing it every day and not even known it.

Bottom line: just use JSX. You’ll be happy you did.

