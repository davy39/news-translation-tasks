---
title: How to develop your React superpowers with the Container Pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-28T17:19:21.000Z'
originalURL: https://freecodecamp.org/news/react-superpowers-container-pattern-20d664bdae65
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OmLZDzZ_WRGIaLdv
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

  Hello everyone! ?

  This time I’m going to tell you about this very useful pattern in React called the
  container pattern or container component pattern.

  This is one of the first patterns I learned. It helped me a lot to separate proble...'
---

By Eduardo Vedes

Hello everyone! ?

This time I’m going to tell you about this very useful pattern in React called the **container pattern** or **container component pattern**.

This is one of the first patterns I learned. It helped me a lot to separate problems in smaller ones and solve them one at a time.

Also, it definitely helped make my code much more reusable and self-contained at once.

It might seem a paradox! How you get your code to be reusable and self-contained at the same time?

Well, reusable because you learn to do small dummy (presentational) components that you can re-use a lot.

Self-contained because the container, view, or whatever you are using to keep all your logic can easily be detached from one place and attached to any other one without big changes/refactoring in your main app.

#### **So this is a win-win and a secret superpower you need to acquire as soon as you can!**

The truth is when you want to do a feature you always start simple and clean.

Days pass by and you get to add one more small feature here, one more feature there. You’re making a patch here, a patch there, and your whole code becomes messy and unmanageable.

Trust me, I’ve been there. **And I’m still there nowadays!** We all are, at a certain point, because programming is a craft. But we can minimize that a lot with practice and with this amazing design pattern.

But, what is a design pattern?

### 01. What is a Software Design Pattern?

A [design pattern](https://en.wikipedia.org/wiki/Software_design_pattern) is nothing more than a general, reusable solution to a commonly occurring problem within a given context in software design. It’s not a finished design that can be transformed directly into source or machine code. It’s a description or template for how to solve a problem that can be used in many different situations.

**Design patterns are formalized best practices that the programmer can use to solve common problems when designing an application or system.**

You know the [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) software design pattern?

### 02. What is the MVC Design Pattern?

Well, MVC stands for [Model-View-Controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). It is an architectural pattern used for developing user interfaces. It divides the application into three interconnected parts.

Traditionally it was used for desktop GUI (graphical user interfaces). This architecture has become popular for designing web applications and even mobile ones.

Imagine you have a triangle with three vertices: **View**, **Controller,** and **Model**.

The View is what user sees on screen (client side).

The User seeing the view can produce changes, can press a button, fulfill a form, press play to see a video, trigger a panoply of stuff together.

The Controller handles the changes the user promoted and all the logic behind. (It works as a relayer, it does requests and handles everything between the View and the Model.)

The Model is the manager. It contains what’s called the business logic, the data. The model receives information from the controller and proceeds to the changes needed. It gives the updates back to the Controller and the View.

React is “a JavaScript library to build user interfaces” (by definition ?). Most of the time you mix and handle the V and part of the C.

And that’s this V and this C that we want to separate distinctly from the container pattern.

### 03. What is the Container Pattern?

The Container Pattern is a solution to separate quite well the V from the C. Instead of doing only one **<Component** /> with the logic and the view, you separate it in **two: <ComponentCon**taine**r /> and &**lt;Component />. The former will do all the logical operations needed and promote communication with the business while the latter will be a dummy presentational component that will render whatever his parent Container demands.

Presentational components are concerned with **how things look_._** While Container components are concerned with **how things work**.

### 04. Let’s get our hands dirty

Imagine we want to do a Superhero List component that shows some data about them. We’ll fetch the data from an API and we want to display it on screen.

Okay, to simulate our Model (database) I’ve created a fake data object. This object contains the info of the super heroes. It also has a fetchFarAwayAPI() function that will return that object.

![Image](https://cdn-media-1.freecodecamp.org/images/6oM0C4bT-PSw0dDWZvxBgoAszEDh3g7DjuUe)
_backend, database simulation_

Then I’ve created a stateful component to fetch the API, save the answer in the state of our component, and render the data in a bootstrap table on the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/PQ0-Zo7UZQZ9XBxF71WiYRLKe6kQMGKWqGUH)
_SuperHeroList component definition_

![Image](https://cdn-media-1.freecodecamp.org/images/V4TdLd9nlB-u3RAzkREv54vySgm-ajYZNJbf)
_SuperHeroList render method_

Okay, we’ve totally separated the Controller from the view. This ?is the main idea you should keep in mind about the container pattern.

If you take a thoughtful look we’ve made one component where we fetch data, save it into state, and render it on screen. We’ve mixed the C and the V. Agree?

Okay, how do we solve this? Yup! **Container Pattern!**

Follow me!

The first step is to create a Presentational Component, to render the view. This component will receive props and render it. It’s completely dummy. Take a look:

![Image](https://cdn-media-1.freecodecamp.org/images/NjvKR1zu5hRBiM36hBidB5HkiB-6ZZJxJIhy)
_SuperHeroList Presentational Component_

To handle the Controller (logic) stuff I’ve refactored our old SuperHeroList renaming it to SuperHeroListContainer.

![Image](https://cdn-media-1.freecodecamp.org/images/iIyrhzvGMjr2RzRAgwAQ-A6Ks3MffQCkExVw)
_SuperHeroListContainer Component_

Okay, we’ve totally separated the Controller from the view and this ?is the main idea you should keep in mind about what’s the container pattern.

But…

We can go further and take the row complexity out of the new SuperHeroList Component. How do we do it? Let’s create a new SuperHeroRow Component:

![Image](https://cdn-media-1.freecodecamp.org/images/ycgvvXOcy1cByqk23d15vT9mShVn-YYo9I9J)
_SuperHeroRow Component_

![Image](https://cdn-media-1.freecodecamp.org/images/OpesZFFBU08yhgqUi9cxtnncjNzLcUXyIPH7)
_SuperHeroList Component_

What have we done here? We’ve decoupled the row rendering complexity outside of the SuperHeroList Component. We let the former only render the table and invoking the SuperHeroRow to render each one of the rows alone.

We’ve extracted row complexity to another component. Always remember, the container pattern is there (inside SuperHeroListContainer). We’ve just spread the rendering into two parent/child components that are completely dummy and presentational using React preferred way of working: composition!

You have the freedom to extract responsibilities/complexities into smaller components. That’s how you should work with React! You need to adjust it to what’s best for the app, for the team, for the context you’re in.

![Image](https://cdn-media-1.freecodecamp.org/images/rlgOQMQjvzfepYufQD0khYiQe6R6pqZ76tmD)
_Super Hero List Browser View_

Sometimes we can abstract the thing a little bit! I think by now we’re fine but… let’s go a little bit further…

Let’s create a second SuperHeroList this time using a HOC (Higher Order Component).

A higher-order component (HOC) is an advanced technique in React for reusing component logic. HOCs are not part of the React API, per se. They are a pattern that emerges from React’s compositional nature.

Concretely, **a higher-order component is a function that takes a component and returns a new component.**

The thing here is to refactor our SuperHeroListContainer into a vanilla JavaScript function. This function takes a component (commonly called the WrappedComponent) and returns a new component.

Just check how I’ve done it below:

![Image](https://cdn-media-1.freecodecamp.org/images/kDPOzrmiYp88pMEFwVIiMZ9MiRMPgCoJCCAL)
_withContainer HOC_

We’ve refactored the <SuperHeroListContainer /> into this function called withContainer. It receives any Component you want to pass thru it and returns a class Component with all the logic inside!

In this case, the abstraction allows us to export multiple kinds of tables or reuse all the logic that we had in the container to invoke multiple/different presentational/dummy components.

That’s how we get self-containment and reusability together ?

![Image](https://cdn-media-1.freecodecamp.org/images/Ur3mNoy-cQ7ff6-6DspQgf2aIGXdabRygkiE)
_SuperHeroList 1 and 2 rendered on screen_

### Last But Not Least

Don’t worry if, at the beginning, you had difficulty determining how to apply the container pattern. It’s an iterative process. With practice, you’ll get there without thinking a lot. It will be intuitive and it will seem at first sight the best approach to almost (90%) anything you do in React.

React has a powerful composition model. [They recommend](https://reactjs.org/docs/composition-vs-inheritance.html) using composition instead of inheritance to reuse code between components.

NOTE: For this article I’ve used Create React App 2.0 with Bootstrap. You can always pull my repo [here](https://github.com/evedes/container-pattern) and do some experimentations later on. You’ll find the two SuperHeroLists and the two examples we’ve done along the article.

Keep reading my articles and don’t forget: always **Be Strong and Code On**!

### Bibliography

1. [React Documentation](https://reactjs.org/docs/getting-started.html)
2. [Container Components](https://medium.com/@learnreact/container-components-c0e67432e005) from _Learn React with chantastic_;
3. [Software design pattern](https://en.wikipedia.org/wiki/Software_design_pattern), from wikipedia, the free encyclopedia;
4. [Model-view-controller](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), from wikipedia, the free encyclopedia;
5. [Presentational and Container Patterns](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0), by Dan Abramov;

Thank you very much!

evedes, Oct 2018

