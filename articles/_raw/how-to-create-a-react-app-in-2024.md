---
title: How to Create a React App in 2024
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-01-26T13:44:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-react-app-in-2024
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/build-react-app-2024.png
tags:
- name: Developer Tools
  slug: developer-tools
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: null
seo_desc: 'In 2024, there are more ways than ever to get your React projects started.
  But which one should you choose?

  In this article, I''m going to break down all of the major ways you can use to create
  a React app and which one you should pick based off of yo...'
---

In 2024, there are more ways than ever to get your React projects started. But which one should you choose?

In this article, I'm going to break down all of the major ways you can use to create a React app and which one you should pick based off of your project's needs.

I'll also include a quick guide at the end to show you exactly how to choose between each according to the type of project you're building.

Let's get started!

## ❌ Why You Shouldn't Use Create React App

In 2023, the Create React App tool was deprecated, which means that it was no longer being maintained. Create React App has been the go-to way to make a new React project, but it's been dethroned by a number of different alternatives.

For that reason, Create React App is not an option I would recommend for creating a new React project in 2024.

## 💨 How to Create a React App with Vite

You may be asking, "What's a good replacement for Create React App?" That option is Vite.

Vite is ideal for making client-rendered React projects that run exclusively in the browser.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/vite.png)
_Vite docs home page_

To spin up a new React project with Vite, you just have to run a single command:

```bash
npm create vite@latest my-react-app -- --template react

```

The great thing about Vite is, as its name indicates, it's much faster than virtually every alternative. Where Vite really shines is how quickly it runs in development.

Vite is unopinionated, however, which means you will likely need to install a suite of third-party libraries for basic functionality, like routing and data fetching.

If your application doesn't have a server or you are using an external API and it doesn't need server-side rendering, Vite is a perfect choice.

Additionally, Vite comes with its own config file, **vite.config.js**, which might require reading the documentation in order to configure things such as environment variables, build options, and image options.

## 🥞 How to Create a React App with Next.js

If you're looking for a way to build a React app that gives you a single-page app (SPA) experience but with server-side rendering and server components, Next.js is your choice.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/nextjs.png)
_Next.js docs home page_

Next.js is the only option at the moment that comes with server components, which allows you to mark a component as `async` and `await` in some operation on the server.

```tsx
async function getData() {
  const res = await fetch('https://api.example.com/...');
  return res.json();
}
 
export default async function Page() {
  const data = await getData();
 
  return <main>{data}</main>;
}

```

The benefit of server components is that you don't have to show a loading spinner in your app before fetching data. Server components allow you to ship far less JavaScript to the client, which leads to faster load times for your users.

Server components do require that you have a server, however, this means that it can't be deployed as simply as a client-rendered React app made with Vite.

Next.js is powerful because it comes with a ton of built-in features, such as a dedicated file-based routing, image optimization, and font loading, to name a few.

Next.js also allows you to tap into server actions, which is a new React feature that allows you to run server code by calling a function.

```tsx
// Server Component
export default function Page() {
  // Server Action
  async function create() {
    'use server'
 
    // ...
  }
 
  return (
    // ...
  )
}

```

Next.js also has route handlers, which lets you to make HTTP requests to an API endpoint. This is something that client-rendered React apps can't do, because there's no server.

With all of Next.js' benefits, it comes with a steeper learning curve. There are a number of Next.js-specific concepts that may seem to go against some React concepts you've already learned.

For example, within server components, you can't use React Hooks. This means that you have to rely on patterns such as storing state in the URL.

Despite the learning curve, Next.js is the most popular React framework and is relied upon to build impressive React apps that power small startups to Fortune 500 companies.

If you want to make something impressive with React, you can certainly do it with Next.js.

## 💿 How to Create a React App with Remix

Remix, like Next.js, is a React-based framework that has a different focus on web standards to deliver a better user experience. Remix allows you to also write server and client React code.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/remix.png)
_Remix docs home page_

Remix prides itself on serving static and dynamic content faster than Next.js. This means it's equally good at building full-stack applications as well as static websites.

Instead of server components and server actions, Remix simply has actions. Actions allows you to handle data mutations on your server, which is anything that isn't a GET request. Actions are just simple functions with the name action.

To get data, you use simple functions called loaders. React Remix uses React Router under the hood. So if you're comfortable with React Router, you'll likely feel at home with Remix as well.

```tsx
export async function loader() {
  return json(await fakeGetTodos());
}

export default function Todos() {
  const data = useLoaderData<typeof loader>();
  return (
    <div>
      <TodoList todos={data} />
      <Form method="post">
        <input type="text" name="title" />
        <button type="submit">Create Todo</button>
      </Form>
    </div>
  );
}

```

Remix is a bit more stable than Next.js and has a less steep learning curve, still allowing you to build just as impressive applications, with the only downside being that it's not nearly as popular as Next.js. So it doesn't have the same community support and libraries around it.

But if you do want something with server-side rendering and client-side rendering, Remix still remains a great option to build your next React project.

## 🚀 How to Create a React App with Astro

The newest way to build a React project is definitely the most performant. React apps can also be built using a framework called Astro.  


![Image](https://www.freecodecamp.org/news/content/images/2024/01/astro.png)
_Astro docs home page_

Astro's goal is deliver content to users quickly through something called "island architecture".

In short, this means that JavaScript is loaded only when the user needs them, making for a much more optimal user experience. If you want the fastest website possible, I'd highly recommend looking at Astro.

Astro supports server-side rendering and is great for SEO-focused websites that are largely static. However, what's neat about Astro is that it can also run code on the server if you choose to. It's not as popular to build fully dynamic, full-stack applications with Astro, but it is possible to do so.

Astro is also very flexible as it's not even tied to React. You don't need to use React whatsoever to build an Astro app, and you can use React alongside other frameworks such as Vue and Svelte within the same app.

If you're building a website that has posts or content that uses markdown or MDX, Astro should be your top choice. It uses a feature called "collections" to describe all the data within your markdown files so that you know exactly what content is going to be rendered in your React components.

Astro is gaining rapidly in popularity, and it's probably the best choice out there if you are interested in making a static website that doesn't need a database or authentication, or a website that is largely static.

## 🤔 So What Should I Choose?

If you've read up to this point and you're still trying to figure out which framework would be best for you to build a React project in 2024, here's the rundown:

* If you're just starting out and learning the React basics but want to build a simple or medium-sized project, stick with Vite.
* If you want a full-stack framework with all the bells and whistles, like server components, and you don't mind spending time learning additional concepts, check out Next.js.
* If you've tried Next.js and find some of its concepts difficult to understand, but still want to build a full-stack React application, definitely look into Remix.
* Finally, if you have a static or content-driven website, and you don't really need a database or authentication, I would highly recommend using Astro.

## 🏆 Become a Professional React Developer

Looking for the ultimate resource to learn React from start to finish?

✨ **[Introducing: The React Bootcamp](https://www.thereactbootcamp.com)**

The bootcamp features every resource to help you succeed with React:

* 🎬 200+ in-depth videos
* 🕹️ 100+ hands-on React challenges
* 🛠️ 5+ impressive portfolio projects
* 📄 10+ essential React cheat sheets
* 🥾 A complete Next.js bootcamp
* 🖼️ A complete series of animated videos

Click below to try the React Bootcamp for yourself.

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)  
_Click to get started_

