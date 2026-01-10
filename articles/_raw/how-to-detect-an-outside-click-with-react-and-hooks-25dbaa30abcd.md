---
title: How to detect an outside click with React and Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T17:17:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-detect-an-outside-click-with-react-and-hooks-25dbaa30abcd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xJYzPKhZBDlYsR2nwkbvPQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Andrei Cacio

  What does “Outside Click” mean?

  You can think of it as the “anti-button”. An outside click is a way to know if the
  user clicks everything BUT a specific component. You may have seen this behavior
  when opening a dropdown menu or a drop...'
---

By Andrei Cacio

### What does “Outside Click” mean?

You can think of it as the “anti-button”. An outside click is a way to know if the user clicks everything BUT a specific component. You may have seen this behavior when opening a dropdown menu or a dropdown list and clicking outside of it to close it.

There are all sorts of other use cases for such a feature:

* when closing dropdown lists
* when closing modal windows
* when transitioning in and out of edit mode for editable elements
* closing
* and many more…

Now let’s see how we can a write a generic and reusable React component which will incorporate this behavior.

### How it will look like

A happy flow should look like this:

### Component structure

For this component to work we will need to attach a click event handler on the document itself. This will help us detect when we are clicking anywhere on the page. Then we will need to check if our clicked target differs from our wrapped element. So a basic structure will look like this:

_For the first example, we will start coding using the React Class style and then refactor it with the new Hooks API._

We implemented two lifecycle functions:

* **componentDidMount()**: will attach the event listener
* **componentWillUnmount()**: will clean up the click handler before the component will get destroyed

and then we render whatever that components wrap over. For our first example above it will render the <span>.

### The “ClickOutside” condition

Now we need to check if the user clicks outside of the wrapped child. One _naive_ solution is to compare the target element (the element that we click) with our child’s node. But, this will work only if we have a simple (single level) node as a child. If our wrapped child has more sub-nodes, then this solution will fail.

Luckily there is a method called [**.contains()**](https://developer.mozilla.org/en/docs/Web/API/Node/contains) which tells us if a node is a child of a given node. The next step will be to gain access to our child’s node. To achieve this we will use [React Refs](https://reactjs.org/docs/refs-and-the-dom.html).

Refs are React’s way of giving us access to the raw node object. We will also use Reacts API for handling the **this.props.children** components. We need this API because we will inject our created ref to our wrapped child. Having this in mind our component will look like so:

Perfect, this should work as expected. At least for our happy flow (one wrapped child). If we intend to wrap more than one node, we need to make some adjustments:

* we need to have an array of refs (as many as our wrapped children)
* we need to use **React.Children.map** to clone each child and inject the associated ref from our private array of refs

This should do just fine. Now let’s refactor this using Hooks!

### Hooks

React 16.8 introduced a new API called [Hooks](https://reactjs.org/docs/hooks-intro.html). With Hooks we can write less code and get a smaller footprint on our codebase. Also, Hooks take advantage of functions which are first class citizens in JavaScript. If you are familiar with [stateless functional components](https://hackernoon.com/react-stateless-functional-components-nine-wins-you-might-have-overlooked-997b0d933dbc) in React you are halfway there. Our initial refactor will look like so:

Up until now, we are still using the “old” React API to declare a simple stateless functional component. However, we still need those lifecycle functions to attach our handler on the **document** node.

Here is where [**Effect hook**](https://reactjs.org/docs/hooks-effect.html) comes in. The Effect hook will replace our “**componentDidMount**” and “**componentWillUnmount**” methods. The Effect Hook will be called right after the components renders so it will help us attach our desired handler on time. Also for the cleanup part, if the Effect hook returns a function that function will be called right before the component will be unmounted. So it is just the right time to do some cleanup. In the next refactor, things will become a bit clearer.

This is the final form of our functional component using the Effect Hook. If you want to see both examples in action you can run them below. (_You can default export either the Class component or the functional component and the app will behave the same._)

### Conclusion

Even though the click outside behavior is a widely used feature, it may not be so straightforward to implement in React. With this example, I took the liberty to experiment a bit with React Hooks and build the solution in two ways to compare the two approaches. I am a big fan of functional components, and now with the help of Hooks, we can take them to the next level.

