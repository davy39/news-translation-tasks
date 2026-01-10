---
title: Is React a Library or a Framework? Here's Why it Matters
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-04-12T21:29:45.000Z'
originalURL: https://freecodecamp.org/news/is-react-a-library-or-a-framework
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/is-react-a-library-or-framework.png
tags:
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: React
  slug: react
seo_title: null
seo_desc: 'Developers have spent a great deal of time talking about what React is.
  But they have left out why this topic matters so greatly for anyone who builds React
  applications.

  The answer to this question is essential for any React developer, regardless of...'
---

Developers have spent a great deal of time talking about what React is. But they have left out why this topic matters so greatly for anyone who builds React applications.

The answer to this question is essential for any React developer, regardless of their skill level. This is because it indicates what they must know and how they must work in developing any React application.

Whether you are a new or an advanced React developer, I hope this thoughtful analysis will improve your own development process as you build your next React project.

## Why is React a library and not a framework?

React was made to build full-fledged web applications. As a result, it's often compared with other tools that developers use to build apps, like Angular, Vue, and Svelte. 

React is written in JavaScript and is used to make better JavaScript applications. We refer to React specifically as a **library**. 

_But what makes React a library and not a framework?_ 

The reason becomes clear when we look at other similar tools that are used to create complete web applications.

Let's look at a project like Angular, which shares the same purpose as React (to create single-page web apps). What sets it apart is the fact that when you set up an Angular project, it is bootstrapped with nearly every single thing that you'll need to make a complete, large-scale app. 

> Many developers like to refer to frameworks or similar solutions as having "batteries included." 

Frameworks are a common choice for companies and anyone looking to make enterprise JavaScript applications, because they include resources that a large-scale application would likely need. This includes built-in tools for common tasks like creating forms, running automated tests, making network requests, and much more.

In short, everything that you need to make a complete application is included in your Angular project when it's generated. But that is not the case with React.

## React is fundamentally "unopinionated"

While popular tools have emerged like Create React App, which allow you to create a complete React project in a single command, React is often referred to as "unopinionated." 

_What does it mean for React to be unopinionated?_

The React and React DOM libraries give us the means of building a user interface with the JSX syntax, plus powerful state management tools via hooks, among other things.

However, React itself does not include many of the React-specific libraries you're going to need for most projects. Angular and Vue, by comparison, include many more tools all bundled within the core package itself.

Many developers consider this discussion of what is and isn't a library to be trivial. But it has real consequences for our development process. In other words, because React is a library and not a framework, **becoming a skilled React developer entails having a good knowledge of third-party React libraries**.

## Since React is a library, you must choose the tools on your own

That means, in order to build complete React applications, you will need to choose these packages and tools on your own. 

Here are a few examples of decisions that I often need to make when I'm building a React application myself: 

For a form library, I have to decide whether I want to use the package React Hook Form or Formik. These are both React-specific form libraries to add important features to our forms like validation.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/react-form-libraries.jpg)

For testing my React application, I might use either React Testing Library, Jest, or some combination of the two.

For making network requests, I might need to choose between the Fetch API and Axios. I might also need to decide if I want to add an additional library to make managing my server state easier, such as React Query or SWR.

## The tools you choose depend on your app and knowledge of them

This question of whether React is a library or framework is important because any React developer must know what their choices are and which choice to make given the type of React application they're building.

If you're building an app without many forms, you might not need a form library at all. If you're more confident with the Fetch API, you might use that over something like Axios. 

It really depends not only on what the demands of the app are, but also on what your preferences are as a developer. This is arguably an advantage that React has as a library and why I believe it's very popular among newer developers. It doesn't lock you into one choice or hold you to any specific libraries other than React itself. 

You're able to make your own decisions, and you're able to have more freedom overall, as a developer. 

That being said, even though React is not a framework this does not diminish its presence in the corporate realm. It's still used to build complex and impressive applications of all kinds. There are many lists of the large-scale React applications that businesses have made and which you likely use on a daily basis.

## You need to keep up with emerging libraries

If we were talking about which form library to choose two years ago, I would likely have included Redux Form. As for a data fetching library, I couldn't have mentioned React Query or SWR, because they weren't created (or hadn't gained much traction), until the last year or so.

Because React apps are often reliant upon third-party libraries, newer libraries come about that improve upon the old ones. Individual developers and teams transition to different tools to get the job done and the ecosystem changes as a whole.

Like it or not, React being a library and not a framework entails a large, shifting network of other libraries we must be aware of to build our projects. Some of which may fall out of favor and be replaced by others or may become deprecated and no longer supported as open-source projects. 

In short, React being a library may require us to pay more attention to what is going on _around_ React, as compared to if it was a framework.

## Wish React was a framework? There are many!

It's worth noting that there are frameworks out there that are based upon React. 

While React itself is just a library, many React-based frameworks have cropped up in recent years to provide developers with a more powerful set of built-in tools. These allow you to build projects faster without needing as many third-party libraries. 

Some of the most popular of these frameworks include Next.js, Gatsby, and Redwood.js, all of which are used to create full-scale dynamic and static React applications.

This is, in my opinion, the great advantage of frameworks – you do not have to make as many choices throughout the development process.

## Use React's flexibility to your advantage

Be aware that going forward, there is a robust ecosystem of React-focused libraries that you can add to your React project to achieve whatever you're looking for, from the most general tasks to the most specific. 

This is thanks to React's popularity and widespread usage. But also note, especially if you're coming from an opinionated framework like Angular or Vue, that there are many React-based frameworks that you can rely upon and learn about to build equally functional and featureful applications as well.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

