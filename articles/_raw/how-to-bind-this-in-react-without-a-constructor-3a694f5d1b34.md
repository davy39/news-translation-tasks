---
title: How to bind this in React without a Constructor
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T21:19:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-bind-this-in-react-without-a-constructor-3a694f5d1b34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LyzgUAvHq6Z-q_fvqCA5pg.jpeg
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
seo_desc: 'By Tiffany White

  This post was originally published on my blog.

  this in React is a reference to the current component. Usually this in React is
  bound to its built-in methods. When you want to update state or use an event handler
  on a form, you could ...'
---

By Tiffany White

_This post was originally published on my [blog](https://tiffanywhite.tech/bind-this-without-constructor/)_.

`this` in React is a reference to the current component. Usually `this` in React is bound to its built-in methods. When you want to update state or use an event handler on a form, you could do something like this:

where `this.someInput` is passing state to whichever React component you are rendering.

Unfortunately, though, React doesn’t auto-bind `this` to custom methods. This means that if I wanted to manipulate the DOM by getting some input, which you can't do as you can with normal JavaScript, I would create a `ref` to do whatever DOM tinkering I wanted.

But because React doesn’t auto-bind `this`, the following code would output undefined when logged:

In order to avoid this, we could use the `constructor` function to render the component or get the state we want:

While this is a decent way to render a ref on a component, what if you wanted to bind several custom methods in one component? It would get pretty messy…

You get the idea.

Instead, we can bind `this` to custom React methods by declaring a method by assigning it to an arrow function:

which will allow us to bind the value of `this` to the `SomeComponent` component.

#### Hope This Helps!

ES6 gave us classes and constructors and React utilized them right away. You don’t _always_ need a constructor, and it helps to know when to use one and when not to.

#### While you’re here!

I write unobtrusive letters from time to time. They are dev letters that are a bit more intimate than regular newsletters. Sign up if you want. No worries.

