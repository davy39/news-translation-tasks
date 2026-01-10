---
title: How to develop your React superpowers with the HOC Pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-27T20:35:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-your-react-superpowers-with-the-hoc-pattern-61293651d59
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca70d740569d1a4ca7491.jpg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eduardo Vedes

  Hey everyone! ? I hope you had a Merry, Merry Christmas and a Happy New Year!

  2018 has reached its end and it makes sense for me to start the new year with an
  article about Higher-Order Components!

  I’ve promised you to write about it...'
---

By Eduardo Vedes

Hey everyone! ? I hope you had a Merry, Merry Christmas and a Happy New Year!

2018 has reached its end and it makes sense for me to start the new year with an article about Higher-Order Components!

I’ve promised you to write about it since we’ve approached the subject when we’ve talked about the render props and the container patterns so it makes sense to deep dive a little bit and pay attention to it!

Personally it’s not one of my favourite patterns, but it’s a powerful tool to know, master and hang on your tool belt.

Just keep in mind that you should not overuse it. Almost everything that you can encapsulate in a HOC you can certainly implement using the render props pattern — check my article about render props [here](https://medium.freecodecamp.org/how-to-develop-your-react-superpowers-with-the-render-props-pattern-b74e68c6d053) — and vice-versa.

### 01. What is a Higher-Order Component?

A higher-order component (HOC) is an advanced technique in React for reusing component logic. HOCs are not part of the React API. They are a pattern that stems from React’s nature that privileges composition over inheritance.

JavaScript is a well-suited language for functional programming as it can accept higher-order functions. A higher-order function is a function that can take another function as an argument and/or that returns a function as a result.

In the same way, a **higher-order component** is a function that **takes (wraps) a component and returns a new component**.

Higher-order functions allow us to abstract over actions, not just values.

HOCs are common in third-party React libs, such as Redux or React Router. I bet you’ve used some of them, maybe without being aware of it.

The main purpose of a higher-order component in React is to share common functionality between components without repeating code.

### 02. Types of Higher-Order Components

Basically there are two main types of HOC implementation: **Props Proxy** and **Inheritance Inversion**.

#### Props Proxy (ppHOC)

Props Proxy HOCs are elementarily expressed like this:

![Image](https://cdn-media-1.freecodecamp.org/images/mT3fcX7TeDvnJTfpgaBCFa-2cCYebKgfSHps)
_propsProxyHOC (standard implementation)_

It’s nothing more than a function, propsProxyHOC, that receives a Component as an argument (in this case we’ve called the argument WrappedComponent) and returns a new component with the WrappedComponent within.

Have in mind that when we return the WrappedComponent, we also pass thru the props that the HOC receives. This explains the name given to this type: **props proxy**.

When we return the Wrapped Component we have the possibility to manipulate props and to abstract state, even passing state as a prop into the Wrapped Component.

You can also wrap the Wrapped Component with other JSX elements changing its UI according to your app needs.

Props Proxy HOCs are useful to the following situations:

1. Manipulating props
2. Accessing the instance via Refs (be careful, [avoid using refs](https://reactjs.org/docs/refs-and-the-dom.html))
3. Abstracting State
4. Wrapping/Composing the WrappedComponent with other elements

#### Inheritance Inversion (iiHOC)

Inverted Inheritance HOCs are elementarily expressed like this:

![Image](https://cdn-media-1.freecodecamp.org/images/Wra7dgCf7jTWM51gKNERjEHIeyygj0wipllh)
_inheritanceInversionHOC (standard implementation)_

In this situation the returned class **extends** the WrappedComponent. It is called Inheritance Inversion, because instead of the WrappedComponent extending some Enhancer class, it is passively extended. In this way the relationship between them seems **inverse**.

Inheritance Inversion gives the HOC access to the WrappedComponent instance via _this_, which means you can use the state, props, component lifecycle and **even the render method**.

Inversion Inheritance HOCs are useful for the following situations:

1. Render Highjacking
2. Manipulating state

### 03. Getting our hands dirty

Okay everyone ?to illustrate a bit the concepts presented above, let’s do some code.

If you want to play later with the code we’re doing, you can pull it here from this [repo](https://github.com/evedes/higher-order-components) of mine ?.

Let’s try to implement a component that returns a welcome message according to the user which is logged into the system.

![Image](https://cdn-media-1.freecodecamp.org/images/YcaqLE7b82RUK5xZVvIKaSngnecv94UCeQ1G)
_main App.js component_

I’ve tweaked my App.js component to show some text and to render a component called Welcome to which I pass the prop user.

Ok, we can do that with a simple component like this:

![Image](https://cdn-media-1.freecodecamp.org/images/gJJJLEEcQg1UI93W-9JjxutVqpz6hZARjQIv)
_Welcome Component_

But…

What if I want the component to return Welcome Guest if no user is logged in?

Well… I can do that in the same Welcome component, with a simple if that checks if the user prop exists and if not it simply returns “Welcome Guest”.

But let’s suppose I want to encapsulate that logic to use with multiple / different Welcome Components.

So the way to go is to make a Props Proxy HOC:

![Image](https://cdn-media-1.freecodecamp.org/images/yyE5v1YvE9NmKyYI2jCqq8GQDZ09iUoV2kRP)
_propsProxy HOC_

What have we done here? We kept our Welcome component simple and we’ve created a JavaScript function called withUser which gets the Welcome component (WrappedComponent) as an argument and checks if the prop user exists. If it doesn’t it just returns a simple “Welcome Guest!” message.

This is very useful. Imagine you had 30 Welcome components in different languages (silly example but it makes the point of encapsulating the logic into a HOC).

Nice, so now we have a HOC to check if there’s a user logged in, otherwise it throws a Welcome Guest Message!

Let’s imagine now that the user info is coming from an external API (Auth0 for example) and is getting into our frontend application thru a Redux reducer which manages the App state.

So before checking if there’s a user we need to check if the data isLoaded into the system!

Wow! This way we could show a loading message while data is not loaded!

So… for this use case I guess we want to do some render highjacking and render another thing if data is not loaded.

For render highjacking we need to use a iiHOC. Wow! Such a coincidence! So let’s do it and compose the two HOCs together everyone ? This will hit hard on the head of the nail.

![Image](https://cdn-media-1.freecodecamp.org/images/AMxMlFa26czQe0fX2rqOira-XunoS2rDeGyE)
_propsProxy + inheritanceInversion HOCs composed_

Pay attention to what we’ve done:

We’ve created a withLoader iiHOC which extends the WrappedComponent. This way it can access its props and trigger different rendering.

In this situation we are getting the isLoaded prop and if it’s not loaded we simply return a loading message! Otherwise we let the WrappedComponent render by simply returning super.render().

In the export statement we are just composing two JavaScript functions such as f1(f2(f3))). Nothing more than that!

There are tools to compose functions in a prettier way, but that’s another story for another article!

### 04. Last but not least

I’ve tried to use simple examples for you to grasp the concepts in the most clean way possible.

My advice for you is that if you do not master this concepts please pull my repo [here](https://github.com/evedes/higher-order-components) and play with it a little bit.

Check the code and try to understand it line by line.

It takes some time to get used to and feel comfortable doing this kind of abstraction so don’t loose your motivation or your focus with HOCs.

Also as I said before, everything we’ve done here can be attained with render props or container pattern, so it’s not a must to choose a HOC or two to do clean code with this kind of encapsulation!

I hope you had as much fun reading this article as I had writing it! If you really enjoyed it please give me some claps (not less than 50 please) ? and always remember to “Be Strong and Code On!”

Also if you want more deep and complex explanations please feel free to read the links I’ve added to the Bibliography section below ?

### 05. Bibliography

1. [React Documentation](https://reactjs.org/docs/getting-started.html)

2. [Eloquent Javascrip](https://eloquentjavascript.net/)t

3. [React Higher Order Components in depth](https://medium.com/@franleplant/react-higher-order-components-in-depth-cf9032ee6c3e)

Thank you very much!

evedes, Dec 2018


