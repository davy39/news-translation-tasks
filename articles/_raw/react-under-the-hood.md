---
title: How React works under the hood
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-05T00:55:10.000Z'
originalURL: https://freecodecamp.org/news/react-under-the-hood
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/New-Project--24-.jpg
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
seo_title: null
seo_desc: "By Mehul Mohan\nReact is a very popular JavaScript library. With over 5.5\
  \ million weekly downloads, React is enjoying great popularity. But not a lot of\
  \ React developers know how React works under the hood. \nIn this post, I'll try\
  \ to uncover some inte..."
---

By Mehul Mohan

React is a very popular JavaScript library. With over 5.5 million weekly downloads, React is enjoying great popularity. But not a lot of React developers know how React works under the hood. 

In this post, I'll try to uncover some interesting things about React which you, as a React developer, might find fascinating. Let's start at the beginning.

But before we start, if you're a React developer, I have some exciting news for you! Once you complete this article, you'll get to develop something cool with React and win prizes on the way :)

## What does React do?

At its very core, React basically maintains a tree for you. This tree is able to do efficient diff computations on the nodes. 

Think of your HTML code as a tree. In fact, that is exactly how the browser treats your DOM (your rendered HTML on the browser). React allows you to effectively re-construct your DOM in JavaScript and push only those changes to the DOM which have actually occurred.

## JSX is syntactic sugar

There's nothing like JSX - neither to JavaScript, nor to the browser. JSX is simply syntactic sugar for creating very specific JavaScript objects.

When you write something like:

```
const tag = <h1>Hello</h1>
```

what you're essentially doing is this:

```
const tag = React.createElement("h1", {}, "Hello")
```

You see, when you start writing nested stuff, not only is this difficult to code, but it also becomes very inconvenient to maintain such a codebase. JSX thus helps you bring the cleanliness of HTML to the power of JavaScript.

But what does React.createElement do itself? It creates a plain old JavaScript object. In fact, you can manually call it and see for yourself!

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-05-at-5.19.08-am.png)

You see, we've an object like this:

```js
{
    $$typeof: Symbol(react.element),
    key: null,
    props: {children: "Hello"},
    ref: null,
    type: "div"
}
```

And if we start nesting elements like this:

```js
React.createElement('div', { }, 
React.createElement('p', {}, 'A p inside a div')
)

```

We would start getting nested objects:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-05-at-5.22.49-am.png)

So now you know, once all the JSX is parsed and all the React.createElement calls have been resolved, we land with one giant nested object like above.

## React Renderer

Now, if you go back to the point where we start our app, you'll see that in your index.js file, you would find the following line:

```jsx
// .. prev code

ReactDOM.render(<App />, container)
```

From above, we know that when `<App />` has been done parsing, this is just a huge object of React elements. Then how is React able to construct actual divs and p tags out of it? Meet ReactDOM.

ReactDOM in turn, recursively creates nodes depending on their 'type' property and appends them finally to the DOM.

It should be clear at this point that why decoupling React from the renderers is actually a great move! What React does is, simply construct a tree of UI which could be used not only on web, but on environments like mobile too, given that a renderer is available which is able to communicate with the host OS. Here, React Native comes to play. You see, React Native uses React library, but not ReactDOM as the render. Instead, the package react-native itself is a renderer.

We do this in a react native application to start the app:

```js
const { AppRegistry } = require('react-native')
AppRegistry.registerComponent('app', () => MainComponent)
```

Look! No ReactDOM. Why not? Because we don't have methods like appendChild, neither do we have a DOM like environment. Instead, for mobiles, we need support for UI directly from OS. But the React library doesn't need to know that, the renderer (React Native) takes care of that.

## React Reconciliation

When we say that React maintains a copy of DOM using virtual DOM in JavaScript, and it uses to diff it to any changes and apply it to real DOM, we don't want React to brute-force its way. React, in fact does very lazy reconciliation. React would make the least amount of changes possible, i.e. it would try to re-use elements, attributes, and even styles if possible!

Consider this example:

```jsx
<img className="class-1" alt="stuff" />
```

Let's say you change this JSX expression to the below one using some condition or some state:

```jsx
<img className="class-1" alt="something else" />
```

Now while diffing, React would see that well, the img tag makes use of the same className both in old and new trees, so why modify it. And it would just modify your alt attribute and move on.

However, there's a catch. Because we don't want React to do a lot of computation on diffing part, React would assume that if a parent has changed, its containing subtree has definitely changed. For example:

```jsx
<div className="class-1">
	<p>I did not change</p>
</div>
```

If you change this JSX to the below using condition/state:

```jsx
<p className="class-1">
	<p>I did not change</p>
</p>
```

Although you could see that we don't need to re-create the inner p tag, but React has no way of knowing that while traversing the tree from top (unless, of course you perform heavy tree diffing, which are much expensive algorithms than the heuristic O(n) react follows for diffing). So, React decides to destroy all children (i.e. calling their cleanup functions in useEffect, or componentWillUnmount in class based components) and re-create the children from scratch. 

## React Keys

When adding/removing elements in a node, React would simply loop over the children in old tree and children in the new tree of the node and mark the places where it needs to perform any addition/removal. But this has a disadvantage without additional help from developer. Consider this example:

```jsx
<ul>
    <li>A</li>
    <li>B</li>
</ul>
```

Consider this is changed to the below by condition/state:

```jsx
<ul>
    <li>Z</li>
    <li>A</li>
    <li>B</li>
<ul>
```

Now, when React would start comparing the two lists for difference, it would find the difference at child node 1, would mutate the old A to new Z, then again at child node 2, would mutate it from the old B to new A, and then finally append the new B node.

However, a better way would've been to preserve the existing A and B nodes and just prepend the Z node. But how would React know about that? React keys would help.

Keys just provide a nice way to React to know which elements have changed or not changed while diffing. Now, instead of comparing the whole element, React would compare the keys of the children to see which element needs to be added/removed. The below way is an efficient way of performing the same thing:

```jsx
<ul>
    <li key="A">A</li>
    <li key="B">B</li>
</ul>
```

Now, if this gets changed to:

```jsx
<ul>
    <li key="Z">Z</li>
    <li key="A">A</li>
    <li key="B">B</li>
</ul>
```

React would now know that keys 'A' and 'B' already exists, so we just need to add the new element with key 'Z'.

_Are you a React developer? Show off your **React skills** by developing a 3 minute interactive game in React and **win hoodies, shirts and coffee mugs**! Take part in **codecomp** by joining codedamn's discord server **[here](http://bit.ly/codedamn-discord)**_

So these were some important concepts I believe would be really helpful for you as a React developers to start understanding the core of React and how it actually works. Feel free to pass down any suggestions or questions you have about the same. 

You can [follow me on twitter](https://twitter.com/mehulmpt) for more JS/coding tweets and things. Peace!

