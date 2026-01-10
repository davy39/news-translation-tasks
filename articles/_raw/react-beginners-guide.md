---
title: The React Beginner's Guide for 2022
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-01-10T21:15:23.000Z'
originalURL: https://freecodecamp.org/news/react-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-10-at-3.24.37-PM.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'So you''re ready to dive into learning React, but you still have some lingering
  questions, such as:


  How should I create my React projects?

  What tools should I add to my React app?

  Do I need to learn JavaScript first before learning React?

  Where shoul...'
---

So you're ready to dive into learning React, but you still have some lingering questions, such as:

* _How should I create my React projects?_
* _What tools should I add to my React app?_
* _Do I need to learn JavaScript first before learning React?_
* _Where should I deploy my projects?_

If you're looking for answers to any of these questions (and more), this simple, comprehensive guide was made for you.

It will give you everything you need to start learning and using React, without piecing together dozens of out-of-date beginner tutorials.

[Click here](https://www.reactbootcamp.com/cheatsheets) to download the cheatsheet in PDF format.

It includes all of the essential information in this article as a convenient PDF guide.

Let's get started!

## Table of Contents 

* [What do I need to install on my computer to use React?](#heading-what-do-i-need-to-install-on-my-computer)
* [How should I create my React projects?](#heading-how-should-i-create-my-react-projects)
* [What React concepts do I actually need to learn?](#heading-what-react-concepts-do-i-actually-need-to-learn)
* [Do I need to learn every React feature?](#heading-do-i-need-to-learn-every-single-react-feature-concept-hook)
* [Do I need to learn JavaScript before React?](#heading-do-i-need-to-learn-javascript-before-react)
* [What React libraries should I use?](#heading-what-react-libraries-should-i-use)
* [Where should I deploy my React projects?](#heading-where-should-i-deploy-my-react-projects)
* [Where should I learn React?](#heading-where-should-i-learn-react)

## What do I need to install on my computer?

To build full-scale React projects on your computer, there are a few essential tools every developer needs:

* [Node / NPM](https://nodejs.org) (I recommend installing the "LTS" version)
* A good code editor (I recommend [Visual Studio Code](https://code.visualstudio.com))
* Git (install it at [Git-SCM.com](https://git-scm.com/) and create a free account at [Github.com](https://github.com))

**Node** is defined as a JavaScript runtime. When combined with a package manager like **NPM** (which you get at the same time you install Node), it serves as a powerful tool to easily manage libraries within your React projects.

Without Node and NPM, if you wanted to add a new JavaScript library to your React project (like [day.js](https://day.js.org/), a library used for formatting dates), you would need to manually add a set of `<script>` tags and manage them yourself.

With Node and NPM (or another package manager like Yarn), we can simply run a command to install whatever JavaScript library we like. To install day.js, we would run:

```bash
npm install dayjs
```

And NPM will automatically grab that library's code and add it to our `node_modules` folder ✨

**Note**: Node / NPM is not required to create a React project. But it lets you use helpful tools like [Create React App](https://create-react-app.dev/) and [Next.js](https://nextjs.org) that make managing your React applications much easier.

A good code editor is also essential to be able to:

* Easily manage all files and folders in our React project
* Provide syntax highlighting to style our code to make it easier to read
* Run commands to develop, test, and build our project using an integrated terminal
* Install extensions to provide additional helpful functionality

**Visual Studio Code** (or [VSCode](https://code.visualstudio.com)) does all of these things and has great default settings for React development, in addition to being entirely free.

Finally, **Git** and **GitHub** are essential for saving changes that you make to your React projects. Git gives you "version control," a fancy name for a tool that enables you to save your code and restore past saves if necessary.

GitHub is essential as well because it allows us to save all of our code remotely, that is, on our GitHub account. You can save your code and the changes you've made to it with Git and then "push" all of those changes to your GitHub account. 

As a result, GitHub serves both as helpful backup for all the work we've done on our React projects and an essential way for others to see our code and make changes to it, too.

## How should I create my React projects?

If you are starting a new React project, you will never need to create your own files, folders, and package.json file (where you list all of your project's libraries).

There are three great tools that will help you immediately generate a new React project within a single command.

* Create React App
* Vite
* Next.js

Once you have Node / NPM installed (see beginning of article), you can use any of these tools to make a new React project with the following commands:

```bash
# for Create React App
npx create-react-app my-react-app

# for Vite
npm init vite@latest my-react-app --template react 

# for Next.js
npx create
```

**Create React App** is a well-established, reliable way to make a new React project and gives you essential tools and scripts to run, develop, and build your project for deployment.

Create React App uses Babel and Webpack to transpile and bundle your code (in short, to make it possible to run in the browser). 

Additionally, it provides great development tools like ESLint to "lint" your code, or to tell you about problems in the code you've written as you write it.

**Vite**, on the other hand, uses a different bundler than Create React App. Instead of using Webpack, it uses a bundler called ESBuild, which is orders of magnitude faster. 

In short, Vite (French for "fast" or "quickly"), is a newer, faster alternative to Create React App.

Be aware that one of these things is not like the others, namely **Next.js**. 

It's worth mentioning that Next.js is a React _framework_, which means that it is a "batteries-included" way to build React apps and includes a ton of features that are not a part of React itself.

The reason I have included Next.js is that it is arguably the fastest and easiest way to create a React application. Once you know the basics of React, you will see how Next's features allow you to build more complete React apps, faster.

But what if you want something smaller without having to create folders, files and install dependencies on your computer?

**Note**: node_modules folders can often contain literally 1000s of folders for your projects' dependencies and peer dependencies, which can collectively take up many gigabytes of space on your computer!

A great way to spin up a React project is by doing it in the browser, and there are a number of free services that allow you to do so instantly. ⚡️

Two sandbox services that can create React projects in the browser include:

* [CodeSandbox](https://codesandbox.io)
* [Stackblitz](https://stackblitz.com)

These are perfect to use when following a tutorial or if you want to test out a bit of code on the fly.

I've found the fastest way to create a new React project is to go to the address [react.new](https://react.new). That's right – you can create a brand new React project in a few seconds without running a single command!

## What React concepts do I actually need to learn?

React has a ton of new concepts that give us a new way to think about building applications on the web and in general.

If you don't have experience building React apps firsthand, how do you know which concepts and features of the library you will need?

The good thing is, you won't need all of them. In fact, as you start building React projects, you'll find that you use the same features for 90% of your work.

For someone working in React daily, these include:

* JSX
* Components (specifically function components)
* Props and state
* Lists, keys, and events
* Core React Hooks, primarily `useState`, `useEffect`
* React Context, including `useContext`
* How to write custom React hooks

It's also essential to know the basics of how React works and what problems it was created to fix. These concepts include:

* Rendering and re-rendering (especially knowing what can cause a re-render)
* Pure functions
* Side effects
* Immutability

Finally, I believe it is worth your while to at least be familiar with React class components. With hooks, we have largely switched to using function components. However, you will come across class components, especially if you are working on an older code base.

If you want a comprehensive list, I have summarized all the major React concepts that I believe every developer should know in a convenient cheatsheet. You can find it here:

[The React Cheatsheet (+ Real-World Examples)](https://www.freecodecamp.org/news/react-cheatsheet-with-real-world-examples/)

## Do I need to learn every single React feature / concept / hook?

No, you don't. Focus on the main concepts I mention in the question above.

In fact, many hooks and React features are rarely used even among the most expert developers. Just because it exists doesn't mean you're going to need it and you don't need to spend equal time learning every single React concept.

For example, I use React on a daily basis and I can count on one hand how many times I've needed the `useLayoutEffect` hook (a more obscure React hook).

## Do I need to learn JavaScript before React?

Since React is fundamentally a JavaScript library that prides itself on being "just JavaScript", if you're going to learn React, you will eventually need to become good at JavaScript as well.

I personally learned JavaScript before I attempted to learn React and I believe it helped me greatly. Although many others have claimed that it is possible to just "start" with React, you are ultimately thrown into a world full of JavaScript.

With that being said, the better you become at JavaScript, the better you will become at building things in React. You can learn both simultaneously and ultimately all React developers are still learning JavaScript, so to speak.

In short, you can start learning React without being the best at JavaScript, however, don't entertain the notion that you can entirely put off learning JavaScript. 

If you want to know exactly which JavaScript skills you will be using as a React developer, be sure to check out this article:

[The JavaScript Skills You Need For React](https://www.freecodecamp.org/news/javascript-skills-you-need-for-react-practical-examples/)

## What React libraries should I use?

There are thousands of React libraries that can be used within your React projects.

React is an unopinionated library, not a framework. Many of the tools that will be required to build your projects are simply not available in React.

React does not provide its own solution for writing styles, animating components, managing global app state, or creating routes or pages.

To build any significant React project, you will need to become acquainted with various libraries to give you functionality that you need.

I could write a series of articles on which React libraries I believe are the best and why, but this is my personal shortlist:

* For state management, use **Zustand** (Redux is still good with Redux Toolkit)
* For styling, use **TailwindCSS**
* For routing, use **React Router** (React Location is also promising)
* For data fetching, use **React Query**
* For forms, use **React Hook Form**

If you want a list of which libraries are worth using for most of your React projects, check out this article:

[5 React Libraries Every Project Needs](https://www.freecodecamp.org/news/5-react-libraries-every-project-needs/)

## Where should I deploy my React projects?

Fortunately, my answer to this question is much like the others – there are many great options for deploying your React project.

If you are deploying a React project that was created using the tool Create React App or with the build tool Vite, your built project will consist of simple HTML, CSS, and JavaScript files. 

This means your project can be deployed to any service that can host static assets like these, such as:

* [Surge](https://surge.sh/)
* [Github Pages](https://pages.github.com/)
* Even an AWS S3 bucket can host your React site

There are tons of options to choose from, but I would highly recommend you deploy your app to any one of these services:

* [Netlify](https://netlify.com)
* [Vercel](https://vercel.com) (best for Next.js)
* [Cloudflare Pages](https://pages.cloudflare.com)

I've used all of these services extensively to host my own React projects and each provide a great developer experience. 

The greatest convenience of all of these services is that you can instantly use projects stored on your GitHub account, and whenever you push a new change to them, your site is rebuilt and deployed with those changes.

It's worth noting that each of these three services come with a generous free tier, so you don't have to pay anything to get your React app on the web.

Their free tiers comes with a caveat, however. Both Netlify and Vercel impose a bandwidth limit of 100GB per month on their free plan. If your website has fewer than 100,000 visitors per months and doesn't consist of a lot of heavy assets such as large images and video, you shouldn't worry about hitting this limit.

Out of these three, Cloudflare has the most generous free plan available among static hosting providers with unlimited bandwidth.

If you're interested in deploying your React apps to Cloudflare pages, I've written an entire guide you can check out here:

[How to Auto-Deploy your React Apps with Cloudflare Pages](https://www.freecodecamp.org/news/how-to-auto-deploy-your-react-apps-with-cloudflare-pages/)

## Where should I learn React?

There are a ton of resources for learning React nowadays. So many that it is hard to figure out which are up-to-date and helpful.

The best thing you can do is find a helpful tutorial and follow it to completion, instead of attempting to take several at once.

> "The man who chases two rabbits catches neither."

If you're just getting started, look no further than **freeCodeCamp's React curriculum**. Be sure to take advantage of all of the links I have shared in each section as well. Both of these resources will take you a long way.

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

