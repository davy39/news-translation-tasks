---
title: React Libraries to Use in Your Projects in 2024
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-02-02T18:42:15.000Z'
originalURL: https://freecodecamp.org/news/react-libraries-to-use-in-your-projects
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/react-libraries-2024.png
tags:
- name: Libraries
  slug: libraries
- name: React
  slug: react
seo_title: null
seo_desc: 'If you''re building applications with React, you should learn how to use
  some helpful libraries that''ll make it easier to add the features you need.

  For example, to add features like authentication or styling, you''ll need to find
  a good third-party li...'
---

If you're building applications with React, you should learn how to use some helpful libraries that'll make it easier to add the features you need.

For example, to add features like authentication or styling, you'll need to find a good third-party library to handle it.

In this comprehensive guide, I'm going to show you all of the libraries that I would recommend you use in 2024 to build fast, reliable React apps with ease.

## Table of Contents

* [React Framework](#heading-react-framework)
* [Package Manager](#heading-package-manager)
* [CSS & UI Libraries](#heading-css-amp-ui-libraries)
* [State Management](#heading-state-management)
* [Data Fetching](#heading-data-fetching)
* [Routing](#heading-routing)
* [Authentication](#heading-authentication)
* [Database & ORM](#heading-database-amp-orm)
* [Dates & Times](#heading-dates-amp-times)
* [Forms](#heading-forms)
* [Drag & Drop](#heading-drag-amp-drop)
* [Mobile Apps](#heading-mobile-apps)
* [Deployment](#heading-deployment)
* [TypeScript](#heading-the-1-library-to-know)
* [Become a Pro React Developer](#heading-become-a-professional-react-developer)

## 🛠️ React Framework

First of all, how do we even create our React app in 2024?

If you want a client-rendered React project, [your best choice is **Vite**](https://www.freecodecamp.org/news/how-to-create-a-react-app-in-2024/), which has displaced the deprecated Create React App tool.

If you're interested in building a server-rendered or full-stack React project, **Next.js** is the most complete and popular full-stack React framework. 

Next.js version 13 introduced the app router, which gave us features like server components and server actions. These allow us to fetch data and render our React components on the server.

If some of Next.js's features are too complex or you don't understand how to use them, a great full-stack alternative for making dynamic and static sites is **[Remix](https://remix.run/)**.

If you're making an application that you want to load quickly and largely serve static content, another great pick is **[Astro](https://www.freecodecamp.org/news/learn-the-astro-web-framework/)**. Astro allows you to use React alongside other frameworks like Vue and Svelte (meaning it is “framework agnostic”) and is designed to ship the smallest amount of JavaScript necessary to the client, which results in very fast load times.

## 📦 Package Manager

To install all of these libraries listed in this guide, you're going to need something called a package manager.

If you have Node.js installed, which is necessary to run a React project locally on your computer, you can simply use **NPM**, which is still a great choice in 2024. There are other alternatives to NPM, including Yarn and PNPM.

The newest alternative, which is quickly becoming very popular in the JavaScript world, is **[Bun](https://www.freecodecamp.org/news/learn-bun-a-faster-node-js-alternative/)**. Bun is both a JavaScript runtime like Node as well as a package manager and is marketed as a faster alternative to Node and NPM.

## 🎨 CSS & UI Libraries

Now that you've got your project set up and your libraries installed, how are you going to style your React projects?

All of the frameworks I've mentioned above include basic CSS support. It's perfectly fine in 2024 if you want to stick to just styling your React projects with **plain CSS**.

You can use CSS style sheets or CSS modules, but perhaps the most popular choice at the moment in terms of pure styling is to use **[Tailwind CSS](https://www.freecodecamp.org/news/learn-tailwind-css/)**. Tailwind CSS does come with a few setup steps, but it allows you to chain pre-made classes together to quickly add styles directly within your component files.

**[ShadCN](https://ui.shadcn.com/)** is a very popular UI library for 2024 that combines Tailwind CSS with a component library called Radix UI. Component libraries like Radix allow you to easily add components without coding them yourself. 

ShadCN has become popular due to the greater control it provides over how your components look with the help of Tailwind CSS.

There are a bunch of other very popular functional component libraries as well. **Material UI** still remains popular, as well as others like **Mantine** and **Chakra UI**. Which one you pick really depends on how you want your final app to look. I'd recommend trying out a bunch of these UI libraries and see which one you like best.

## 💽 State Management

React has built-in tools such as [useState](https://www.freecodecamp.org/news/learn-react-usestate-hook-in-10-minutes/) and [useReducer](https://www.freecodecamp.org/news/usereducer-hook-react/) to manage your app state in basic applications. If you're using Next.js, [state management has been moved to the URL](https://www.freecodecamp.org/news/how-to-use-urls-for-state-management-in-react/) when working with server components. Despite these options, you may need a way to manage state in a more precise way.

You might have lots of pieces of state and want greater control over how state updates render your components. If so, you can reach for a dedicated state management library.

Libraries such as **Zustand**, **Recoil**, and **Jotai**, which are all very similar, allow you to manage state simply by declaring properties and methods on an object. This ultimately is the simplest way to handle state management across your app's components.

If I had to pick one state management library for all of my React projects in 2024, I would choose **[Zustand](https://www.npmjs.com/package/zustand)**. It takes almost no time to learn how to use it. It also doesn't require you to add a provider component to your application, which makes it very convenient to use in any component you like.

## 🐕 Data Fetching

State management and data fetching often go hand in hand. If you're building a client-rendered React app, you're likely going to need a data fetching library.

The best way to fetch data from a server in a React app in 2024 remains React Query or **Tanstack Query** as it's now called. TanStack Query gives you fine-grained control over not only fetching data, when to fetch and refetch it, caching, all through convenient custom hooks, as well as very easily change or mutate data.

Another solid alternative is **SWR**, which also offers a custom hook to handle queries and mutations, but it's far simpler in terms of what it offers. You can't go wrong with picking either one and fetching data and performing your HTTP requests with the fetch API.

[Here's an article](https://www.freecodecamp.org/news/how-to-fetch-api-data-in-react/) that walks you through some of the most popular methods of data fetching in React (including Tanstack Query and SWR).

## 🧭 Routing

If you're using a framework like Next.js, Remix, or Astro, your routing is already taken care of. All of them come with built-in ways to create routes or pages in your project.

With a client-rendered React app such as one made with Vite or Create React App, you're going to need to pick a routing library. **[React Router](https://www.freecodecamp.org/news/learn-react-router-6-full-course/)** still remains the most popular choice. It takes care of every routing need you might have. It’s also very advanced due to its data loading features with the `loader` prop. The `loader` prop allows you to fetch data for a given route without using an external library like React Query.

An up-and-coming library that appears to have equally good features is **[Tanstack Router](https://tanstack.com/router/latest)**. The Tanstack Router was made to be fully type-safe and offer great defaults for data fetching just like React Router version 6 provides.

While Tanstack Router is a bit newer, you really can't go wrong with either choice, and it's a perfect pairing if you're already using Tanstack Query or SWR in your applications.

## 🔒 Authentication

While authentication is something that's handled by the server side of our projects, it's worth knowing what libraries integrate best with React projects, both on the client and the server.

In 2024, [**Supabase** has emerged](https://www.freecodecamp.org/news/learn-supabase-open-source-firebase-alternative/) as a very robust authentication solution and offers easy integration with React apps, both on the server, say, in a Next.js project, and on the client. In past years, Firebase was chosen for similar reasons, but it's harder to integrate on the server side of things.

If you're using Next.js, you have a ton of options available to you such as **NextAuth**, **Clerk**, and the newcomer **Lucia**. It's unfortunate that there isn't currently a built-in auth library for Next.js, but perhaps in the future there'll be one.

In the meantime, I'll personally be using Supabase and would highly recommend you check them out as well via their documentation.

## 🥞 Database & ORM

Much like authentication, your database is something that will and should speak largely to your server-side code.

Databases like Supabase and Firebase don't require that you have a server. You can get and change data directly in the client, and you can add security rules within your dashboard to make sure certain types of requests are allowed or not allowed according to users' authentication status and role.

Outside of these two options, if you're using a traditional server or a full-stack framework, there are countless options. In 2024, the general preference is clearly for SQL databases like MySQL or PostgreSQL over NoSQL databases like MongoDB or Firebase.

With your database, to talk to your database, you'll either use plain SQL or an ORM that allows you to use a custom query language. Popular options for ORMs include **Prisma** or **Drizzle**. Both of them allow you to generate type-safe code so that you know what data will be returned and both integrate very well with SQL or NoSQL databases of your choosing.

## 🕰️ Dates & Times

When you're working with JavaScript, it's always recommended to have a date library. JavaScript's date constructor is unpredictable and virtually impossible to work reliably with things like time zones.

There are a bunch of options, but I tend to gravitate to **date-fns** or **day.js**. Both are very small but extensive libraries that allow you to manipulate JavaScript dates either in the browser or on the back end. You can't go wrong with either one.

## 📋 Forms

You may not need a form library in most cases if you're just building an app with a simple sign-up form, using the `required` prop on your inputs is usually all you need.

If you're building something more complex and have a lot of forms, **[React Hook Form](https://www.freecodecamp.org/news/how-to-create-forms-in-react-using-react-hook-form/)** is a fully featured form library that allows you to validate form input and display errors with very minimal code.

Other form libraries, such as Formik and React Final Form, will give you the same functionality, but React Hook Form is a bit better because it has a more modern API based on hooks and usually requires less code.

## ☔️ Drag & Drop

When it comes to adding drag and drop to your application, you almost certainly need a third-party library. The most popular choice in the past has been React Beautiful DnD. As of 2024, it is no longer receiving regular updates.

Going forward, a solid replacement for drag and drop is to use **[DnD Kit](https://dndkit.com/)**. It's lightweight, very flexible, and the documentation includes a bunch of super helpful examples covering every use case you might have when implementing drag and drop.

## 📱 Mobile Apps

If you want to build a mobile app, the library to do so for React developers has always been [React Native](https://www.freecodecamp.org/news/react-native-full-course-android-ios-development/). There are some exciting libraries pushing the boundaries of React Native to extend to the web.

[**Expo** is a tool similar to Vite](https://expo.dev/), but for making mobile React apps. It has great features like fast refresh, and with Expo Go, you can easily run your project on your own device as you develop it. Expo is making it easier to take your mobile code base and also deploy it to the web.

This is the end goal of other projects such as **[Tamagui](https://tamagui.dev/)**, which you should also check out if you want to make a real native app that runs on Android, iOS, and the web.

If you have a React app that you've already written to run in the browser, the fastest way to have it run as a native app and launch it on the Apple App Store or Google Play Store is to use **[Capacitor.js](https://capacitorjs.com/)**.

## 🚀 Deployment

There are more ways than ever to deploy your React app. [Vercel is probably the easiest platform](https://www.freecodecamp.org/news/deploy-react-app/) to deploy your React app with, whether it's client-rendered or server-rendered. They support just about every framework you can think of, including non-JavaScript languages. They have a generous hobby plan, and competitors in the same space include Netlify and Cloudflare Pages.

Cloudflare Pages might be a little bit trickier to set up, especially if you have a full-stack React project, but it is the most generous in terms of price out of all of these options. If you don't mind paying for a server, you can use something like Railway or Render, which is great to deploy to if you have a server that is separate from your React app.

## ✨ The #1 Library To Know

Finally, the number one essential library you should know if you're a React developer in 2024 is [TypeScript](https://www.freecodecamp.org/news/learn-typescript-beginners-guide/). All of the frameworks I've mentioned include options to build a React app with TypeScript.

TypeScript is a tool that allows you to detect type errors in your JavaScript code to help you prevent runtime errors. You can build all of your React projects with just JavaScript, but at some point, you're going to either see the benefits of using TypeScript yourself or be looking at a codebase that has TypeScript in it.

I'd highly recommend you set aside some time to learn TypeScript. It's the most essential, the most in-demand tool to know as a React developer and can greatly improve your overall code quality.

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

