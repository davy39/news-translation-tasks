---
title: The React Roadmap for 2024 – How to Learn React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-01-09T18:57:12.000Z'
originalURL: https://freecodecamp.org/news/the-react-roadmap-learn-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/react-roadmap-2024.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In this guide, I''ll break down a complete roadmap that will cover all
  the concepts, libraries, and tools to help you become a React developer in 2024.

  My goal is to show you the happy path in React, navigating you away from pitfalls
  so you can spend ...'
---

In this guide, I'll break down a complete roadmap that will cover all the concepts, libraries, and tools to help you become a React developer in 2024.

My goal is to show you the happy path in React, navigating you away from pitfalls so you can spend your time on what really matters in React to help you reach your goals.

Here's the roadmap I would choose for any React developer, whether you're a total beginner or a more advanced one, to help you build amazing apps, get a job, and enjoy using React.

If you're interested in a step-by-step guide on how to learn React in 2024, [check out this article](https://www.freecodecamp.org/news/how-to-learn-react-step-by-step/) that I've written. I recommend reading the two together.

## Here's an Outline:

1. [Learn Core React Concepts](#heading-learn-core-react-concepts)
2. [Learn Core Hooks](#heading-learn-core-hooks)
3. [Intermediate React Concepts](#heading-intermediate-react-concepts)
4. [Create React Apps with Vite](#heading-create-react-apps-with-vite)
5. [Fetch Data with TanStack Query](#heading-fetch-data-with-tanstack-query)
6. [Manage State with Zustand](#heading-manage-state-with-zustand)
7. [Style with TailwindCSS and Radix](#heading-style-with-tailwindcss-and-radix)
8. [Add Routing with TanStack Router](#heading-add-routing-with-tanstack-router)
9. [Build Forms with React Hook Form](#heading-build-forms-with-react-hook-form)
10. [Full-Stack React Apps with Next.js](#heading-full-stack-react-apps-with-nextjs)

## 🧱 Learn Core React Concepts

There are a number of core React concepts that are necessary to build just about any React application, no matter how simple or complex.

The biggest concept in React is arguably **components**. In 2024, almost every component you make will be a **function component**.

These components are composed of React **elements** and **JSX**. Understanding the behavior of JSX is essential, as well as passing data to components using props and knowing the difference between **props and state.** Finally, knowing how to conditionally render parts of the user interface with **conditional rendering** is also key.

⏳ Spend less time on:

* Class components, which are almost exclusively seen in older projects. Class components are no longer the default component type due to React Hooks, which are used only in function components.
* Older patterns like render props and higher-order components aren't necessary to learn because they were used largely before React Hooks arrived in 2018.
* Simple concepts such as list, keys, and events, which are not as difficult to grasp.

## 🎣 Learn Core Hooks

After the core concepts of React, you have the built-in React Hooks. The most important and frequently used of which are **useState**, **useEffect**, **useRef**, and **useContext**.

To use these hooks, you're going to need to understand the basics of React state, how to perform a side effect with useEffect, and avoid the potential pitfalls of useEffect, such as infinite loops.

You'll need to also understand refs for the useRef hook. And the context API for useContext.

Again, these are what you're going to use probably 90% of the time. The other 10% or so might be custom hooks that you make in order to add unique functionality to your application.

⏳ Spend less time on:

* Hooks like useReducer, which won't be used that frequently in comparison to useContext.
* Optimization hooks like useCallback and useMemo. These can be important at times, but you'll use them far less frequently.

## 🧠 Intermediate React Concepts

To really master React, you need to have a solid grasp of some intermediate concepts.

Some of these intermediate concepts include:

* Understand what causes React to render
* How to move business logic into reusable hooks
* Basic patterns like "lifting state up"
* How to use composition to avoid prop drilling and overusing context

While the core concepts I mentioned are usually best understood by actively coding and making React projects, intermediate concepts require understanding how React works.

Fortunately, you can get all of that understanding through reading the all-new [React documentation](https://react.dev). There are a number of very helpful guides covering these intermediate and sometimes advanced concepts.

## 🛠️ Create React Apps with Vite

What is both a positive and a negative of React is how unopinionated it is. React helps us to make single-page applications, but we often need to resort to third-party libraries to add essential functionality.

To create a new React app in 2024, I'd highly recommend using the CLI/build tool, **Vite**.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.42.58-PM.png)
_Create React apps with Vite_

You can use a package manager like NPM and a single command to create a React application from scratch with all the tools that you need to run it in development and build it for production.

```bash
npm create vite@latest my-react-app -- --template react

```

Create React App is no longer recommended. It's not being as actively maintained and is far slower than Vite.

## 🐕 Fetch Data with TanStack Query

Data fetching out of the box in React applications is hard. Without a dedicated library, you need to resort to performing HTTP requests in the useEffect hook.

However, this requires adding a lot of additional boilerplate code to manage loading and error state, and it doesn't handle a lot of logic to prevent making unnecessary requests.

The go-to library I'd recommend for any React or Next.js application would be **TanStack Query** (previously known as React Query).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.43.53-PM.png)
_Fetch data with TanStack Query_

It provides simple hooks to not only request but also to "mutate" (update) data from an API endpoint.

It covers just about everything you could want out of a data-fetching library, including caching, deduping multiple requests, knowing when data is out of date. And can be customized exactly the way you'd like.

If you're looking for a good alternative, you can try SWR. It does not have as many features as TanStack Query but is another good lightweight option that makes data fetching with React much easier.

## 🤹‍♂️ Manage State with Zustand

State management libraries are a must in React applications when you get to a certain size project. The default state management library for React applications for a long time has been Redux, and has been improved with Redux Toolkit.

There are still thousands of companies using Redux even in 2024. However, the ecosystem has shifted towards easier state management solutions.

That allows you to describe your state as an object and write functions to update properties on that state object. The go-to state management library for the past couple of years for me has been **Zustand**.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.44.32-PM.png)
_Manage state with Zustand_

It's a great small library that's very helpful – not just at managing state across any component using simple hooks, but it also provides very convenient features such as preventing unnecessary rerenders.

There are many good alternatives to Zustand such as Recoil and Jotai, both of which share a similar API to Zustand.

## ✨ Style with TailwindCSS and Radix

There are tons of styling options for React in the form of component libraries. These are premade sets of components, which not only offer a nice consistent design, but built-in functionality as well.

In past years, I would have recommended something like Material UI, but these component libraries can often be inflexible, hard to customize, and increase your bundle size greatly.

A better alternative for 2024 that many developers and businesses are moving towards is using a solution like **Tailwind CSS**. It just allows you to style your components with chainable, premade classes, in combination with a minimal component library, such as **Radix**.

Radix provides what are known as primitives. They allow you to make very functional components that your application needs such as dialogs, buttons, selects, tooltips, and just about anything you can think of, which can be styled any way you like.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.45.07-PM.png)
_Style your apps with ShadCN UI_

**ShadCN UI** is a set of components that uses both TailwindCSS and Radix components and provides a good starting place for any application. You can also customize it more than a traditional component library.

I'd highly recommend using something like ShadCN UI for React projects that you use in 2024.

If you would like to use a component library instead, some good choices are Mantine, Chakra UI, and Material UI.

## 🪧 Add Routing with TanStack Router

**React Router** still remains the go-to router for most React applications you will build.

React Router has been around since virtually the beginning of React and continues to get significant updates with React Router 6. It covers just about any use case you can imagine, as you can see in their thorough documentation.

One important alternative, however, is **TanStack Router**. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.45.50-PM.png)
_Add routing with TanStack Router_

It's a brand new router for 2024 with a plethora of great features. It has type-safe navigation, built-in TypeScript support, nested routing, automatic route prefetching, and is designed for use with client-side data fetching libraries like TanStack Query and SWR.

If you're using TanStack Query, I'd highly recommend checking out TanStack Router for future React projects.

## 📑 Build Forms with React Hook Form

Form libraries are not always necessary when building React apps. But if you need form validation, a highly customizable and straightforward choice is **React Hook Form**.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.46.53-PM.png)
_Form Validation with React Hook Form_

With the built-in `useForm` hook, it makes it very easy to customize the input validation and the error messages.

What's great about React Hook Form is that there's very little code to add to your components. Most of it is abstracted in the useForm hook itself.

Some other reliable alternatives that might include a bit more code to setup are Formik and Final Form.

## 🥞 Full-Stack React Apps with Next.js

Perhaps the most important choice here when choosing a way to build a React project is the full-stack React framework.

These frameworks allow you to build not only the React client that users interact with, but also the server-side, where you can create APIs, add authentication, and so on.

The most popular React framework is **Next.js** and for good reason. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-09-at-12.47.25-PM.png)
_Build full-stack apps with Next.js_

Next.js 13 gave us server components, which allow us to run our React code on the server. This reduces the amount of JavaScript sent to our client, making for an overall better and faster user experience.

This also allows us to fetch data on the server, and include that data in our React component on its initial render. That means that we can avoid a lot of loading spinners, but still give our applications a single-page app-like experience.

The downside of Next.js is that it does come with a lot of patterns that might seem to conflict with the core concepts of React. But it's done with the intention of making your life easier as a React developer and building faster.

A good alternative to Next.js is **Remix**, which will soon be adopting server components.

## 🏆 Become a Professional React Developer

Looking for the ultimate resource to learn React from start to finish?

✨ **[Introducing: The React Bootcamp](https://www.thereactbootcamp.com)**

The bootcamp features every resource to help you succeed with React:

* 🎬 200+ in-depth videos
* 🕹️ 100+ hands-on React challenges
* 🛠️ 5+ impressive portfolio projects
* 📄 10+ essential React cheatsheets
* 🥾 A complete Next.js bootcamp
* 🖼️ A complete series of animated videos

Click below to try the React Bootcamp for yourself.

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)  
_Click to get started_

