---
title: 'How to Learn React in 2021: The 7 Skills You Need To Know'
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-01-06T16:01:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-react-skills-you-need-to-know
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/how-to-learn-react-2021-1.png
tags:
- name: React
  slug: react
- name: React context
  slug: react-context
- name: react hooks
  slug: react-hooks
- name: react router
  slug: react-router
seo_title: null
seo_desc: 'You want to learn React_—_the most in-demand JavaScript library in the
  world. But what steps do you need to take to get there? Let''s walk through the
  seven skills you should learn to become a professional React developer.

  As you''re piecing together y...'
---

You want to learn React_—_the most in-demand JavaScript library in the world. But what steps do you need to take to get there? Let's walk through the seven skills you should learn to become a professional React developer.

As you're piecing together your React learning path, it's easy to feel overwhelmed and say, _"It's impossible to learn it all. There are too many things I need to learn!"_

**To be successful with React, don't attempt to learn everything. Focus on learning the right things.** 

Let's break down the seven key skills that you need to focus on to build impressive applications and become an in-demand React developer.

## Step 1: Become confident with the core fundamentals of HTML, CSS, and JavaScript

The first step in learning React is actually somewhat of a step backwards.

The building blocks of the web and every single webpage are HTML, CSS, and JavaScript. Any good React developer should know how to use them. React builds upon them to help you create apps that run on the web.

If you’ve built something with HTML, CSS and JavaScript already, you’re in a good place. For example, if you’ve built a complete landing page or a small website.

Out of the three technologies, **React is most connected with JavaScript**. React _is_ JavaScript, with some added features. For that reason, you’ll need to have solid JavaScript skills.

### What JavaScript concepts should you know for React?

* Basic data structures: variables, objects, and arrays
* Array methods and working with array data: `.map()`, `.filter()`, and `.reduce()`
* Be very familiar with functions and a little bit with classes
* Asynchronous JavaScript: promises, making HTTP requests with Fetch API, async/await syntax can help
* The DOM: learn to create, select and modify HTML elements as well as their attributes
* Object and array destructuring are helpful for working with data

Many developers claim that you should know "ES6/ES7/ES8/ESNext JavaScript" (in other words, the latest JavaScript features) to better learn React. Knowing more JavaScript can help, but new features can also serve as a distraction for new learners. 

First, become confident with the JavaScript concepts I've listed above by building some small projects that require JavaScript. After that, you can take a look at some newer features of the language.

## Step 2: Learn React fundamentals and React hooks

Once you’re confident with JavaScript, you’re ready to learn React and its core concepts. 

These fundamentals are all React-specific and they exist to help us build applications with React, using patterns that JavaScript itself does not have.

### What React fundamentals do you need to know?

* How to structure JSX elements (and how it differs from plain HTML)
* How to render (show) JSX elements and how to show or hide elements based on certain conditions
* How to split JSX into components and how to reuse and organize those components to make our app interface.
* How to pass data (+ JSX elements and components) to components using props and when to do so
* How to store and update data within components using state and how to "lift state up" to other components
* How to use event data in React and handle events from `onClick`, `onChange`, and `onSubmit` events (i.e. events from buttons, inputs, and forms)

As a 7-year old library, React’s features have changed over time. A question I’m often asked is **what should you learn first: the old or the new syntax?** At the end of 2018, React received a large update that included features called React Hooks.

Hooks were a great improvement. They made React apps simpler, more powerful, and allow us to write less code. What’s important for you to know is the five core React hooks.

### What five React Hooks do you need to know most of all? 

* `useState`: to store and manage data within individual components
* `useEffect`: to perform actions like HTTP requests or working with a browser API
* `useRef`: to reference JSX elements
* `useContext`: to access data from React Context to share data among components more easily [rather than passing props]
* `useReducer`: to store and manage data across multiple components

There are more hooks than these 5, but the others are not needed as often. So yes, you should learn the latest React features. Jump into using hooks right away. They will be the basis of every React app you make.

## Step 3: Learn to fetch data from both REST and GraphQL APIs

A React app is the frontend of a complete application. In every application, you will likely have both a React frontend, which the user interacts with as well as a backend that our React code interacts with. The backend is where we get our data from and do other things like authenticate our users.

There are two ways of working with data from a backend. The standard way of getting data is from what’s called a REST API. **REST APIs** are the most common form of API. And the newer way is from what’s called a **GraphQL API**. 

You’ll encounter both types of API in your work, so become familiar with using React to interact with both.

## Step 4: Learn to style your React apps with a component library or utility class library

Every React app needs styling for its appearance. One choice is to use plain CSS. You can write your own styles and put them in a separate style sheet.

But besides CSS, many React developers use what’s known as a component library for easier styling. **A component library** gives us reusable components that have their own pre-made styles. The most popular component library for React is **Material UI**. But there are many others you can choose from.

Developers also use tools that provide pre-made class names called utility class libraries. Unlike a component library, **a utility class library** comes with pre-made classes to style your elements. 

You can style your app by applying classnames to each element. This removes the need to write any styles yourself. The most popular utility class library is **Tailwind CSS**.

You’ll encounter both of these as a developer, so become familiar with both a component library and a utility class library.

## Step 5: Manage state in React with React context

**What is state management?** It’s the process of deciding where to locate data and how to work with it across our app. To manage state across your app’s components, use React Context. 

**React Context** is a tool that’s built into the core React library and allows us to pass data across our app's components without using props. It helps us solve the problem of prop-drilling which involves passing props (data) down to components that are deeply nested into one another. 

With React Context, we place a value on the context we create and then access it using the `useContext()` React hook.

**What about Redux?** Redux is a popular library for managing state in React apps. It is a far more complex tool than you need for most apps you’ll build. While Redux is still relied upon for very large applications, React Context will be enough for any app you make.

Plus you can get many of the benefits of Redux by combining React Hooks and React Context. This is a great advantage compared to learning an extra library.

## Step 6: Learn a React router. In particular, react-router-dom

**What is a router?** Any website we visit has many pages we can browse by going forward or backward in our browser’s history. To create these different pages or routes in React, we need to use what’s called a router.

React itself does not come with its own router, so we’re going to need to use a third party library, one called react-router-dom. 

**react-router-dom** is necessary for creating pages in our app, as well as navigating the user around each page. It lets us create links to different pages of our app and navigate to them or redirect them to other pages if we need.

### What features of react-router-dom do you need to know?

* How to create app routes using the `<Route />`, `<Switch />`, and `<BrowserRouter />` components
* How to navigate users to different pages using the `<Link />` component and programmatically using the `useHistory()` hook
* How to create dynamic routes using the path prop (i.e. `<Route path="/posts/:post-slug" component={Post} />`) and get the path's value using the `useParams()` hook
* How to redirect users from protected content using the `<Redirect />` component (see number 7)

## Step 7: Learn patterns for authentication in React

Authenticated users are people who have signed in to use our app. And we want to give those users access to different things. For that reason, authentication goes hand in hand with routing. This is because authenticated users should be able to see certain pages that unauthenticated users cannot.

### What do you need to know about authentication as a React developer?

There is one main thing. You should learn how to show certain content to authenticated users and hide that content from unauthenticated ones.

In review, these are all the core skills you need to have as a React developer, capable of building complete applications and working as a hired frontend developer.

Beyond these 7 skills, note that there are many that can deepen your understanding as a developer. For example, learning more about browsers, HTTP, and APIs, to name a few. But if you follow all these steps, you’ll have a solid understanding of React and be able to build applications of any scale.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

