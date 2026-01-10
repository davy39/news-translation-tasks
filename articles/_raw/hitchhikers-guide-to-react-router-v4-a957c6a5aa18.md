---
title: 'The Hitchhiker’s Guide To React Router v4: Grok React Router in 20 minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-25T23:59:06.000Z'
originalURL: https://freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18
coverImage: https://cdn-media-1.freecodecamp.org/images/0*GQM3tb92nE_1yMTX
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Eduardo Vedes

  Hi fellow React Hitchhiker! Want a ride into React Router? Jump in. Let’s go!

  To understand the philosophy behind React Router, we need to know what a Single-Page
  Application (SPA) is.

  What Is A Single-Page Application?

  Basically it’...'
---

By Eduardo Vedes

Hi fellow React Hitchhiker! Want a ride into React Router? Jump in. Let’s go!

To understand the philosophy behind React Router, we need to know what a Single-Page Application (SPA) is.

### **What Is A Single-Page Application?**



Basically it’s a web application or web site that interacts with the user by dynamically rewriting the current page rather than loading entire new pages from a server.



### Why is this so good?!



**1.** avoids interruption of the user experience between successive pages

**2.** makes the application behave more like a desktop application

**3.** all the code resources are dynamically loaded and added to the page as necessary, usually in response to user actions

**4.** because it’s kewl and kewl and extra-ultra-wide-4K-level-of-kewl. ?

SPAs are an industry standard now, and lots of companies are in a quest to find programmers to develop their projects.



### **What is React Router?**



React Router is a tool that allows you to handle routes.

Since you’re dealing with an SPA, you need a way to trigger the contents that are loaded on the screen. React Router introduces a concept called “Dynamic Routing”, which is quite different from the “Static Routing” we are used to.

When you’re dealing with “Static Routing” you declare your routes as part of your app’s initialisation before any rendering takes place (Rails, Express, Ember, Angular, and so on).

“Dynamic Routing” means that routing takes place as your app is rendering, not in a configuration or convention outside of a running app.

React Router v4 advocates and implements a component-based approach to routing.

It provides different Routing Components according to the needs of the application and platform.

In this specific case we’re going to explore  **<BrowserRouter>** because we want to use “dynamic routing” in a “web app” context and leave the other ones for other circumstances.



### **Who Created React Router?**

These two amazing human beings, [Michael Jackson](https://twitter.com/mjackson) and [Ryan Florence](https://twitter.com/ryanflorence). And they deserve loads, tons of claps! Together they started [React Training](https://twitter.com/reacttraining).

Nowadays, correct me if I’m wrong, they followed separate paths:

Michael Jackson continues to develop [React Training](https://reacttraining.com/).

Ryan Florence created [Reach.Tech](https://reach.tech/).



### **Has React Router Anything To Do With Redux?**

No. Although they typically appear together.

Are you sure? Yes ? I am sure ?

They’re both great and indispensable tools and as they are Higher Order Components (basically JavaScript functions that take a Component and return a new one), so it’s common to find them “composed” together.

### **Setup, Let’s Get Our Hands Dirty**

![Image](https://cdn-media-1.freecodecamp.org/images/Ga6dcRb1gmEed2ge937FwIv9aR1AwIkAvGvJ)
_Photo by [Unsplash](https://unsplash.com/@rosiet07?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Rose Elena</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

To guide you through this process we’ll use Create React App (CRA).

In the end you’ll have a clean boilerplate to build simple websites.

If by any chance [React](https://reactjs.org/docs/hello-world.html) or [Create React App](https://github.com/facebook/create-react-app) are beyond your grasp, I recommend you to first get into those and then come back with a cup of coffee.

Okay, to those who stood with me: after installing CRA, you need to install the react-router package.

If you use npm just open your terminal, go to your CRA folder and type:

_`npm i -S react-router-dom`_

or

_`yarn add react-router-dom`_ — if you use yarn as your package manager.

Just to check your _**package.json**_ and make sure everything is okay, here’s mine:

![Image](https://cdn-media-1.freecodecamp.org/images/k1OxWlNSx7lJ3wBTUrYsyrJpcgFTK00hNvH7)

As you can see ?at this point we have **react-router-dom** as a dependency.

Done, npm or yarn start and…

**Bang! We’re riding Ma!** 

### **The App We Are Building**

Let’s do a simple personal website with a navigation bar that allows the user to switch between content. Our website will have three main sections called **Home**, **About** and **Topics**.

The **NavBar** will be an omnipresent component while the **Home**, **About** and **Topics** will be rendered below according to the routes selected.

Are you seeing the browser URL: _**localhost:3000/home**_ in the screenshot below?

It means that the **Home** route is triggered and the **Home** view is rendered.

This will be our final result:

![Image](https://cdn-media-1.freecodecamp.org/images/Igwuii40jvc5gCBOQuuVWbEexaNZgVxbdJcP)

And this… ?, this is a website?

? Yes, It is!

A naked one! Just try not to feel bias towards other complexities like styling and so on! I don’t want you to be distracted with anything other than grokking **how simple** it is to implement **React Router v4**.

So, after you’ve recovered from the shock, ?, let’s take the next step and see my /src/index.js file.

#### /src/index.js

_index.js_ is the first file to be loaded by CRA, the initialisation point of everything in your App.

Let’s take a look at what I’ve done:

![Image](https://cdn-media-1.freecodecamp.org/images/scJ4TP9j27Ph1S425FUiTbB4e-b9iC-0v-gf)

So what are we doing here?

* We are importing the **<BrowserRouter/>** component from the dependency we’ve installed and stating that we’re going to call it **<Router/>** from this point on:

_`import { BrowserRouter as Router } from ‘react-router-dom’;`_

* We are importing a **<Routes/>** component, created by me, with the routes we’re going to use in our web site — don’t worry right now with this Component:

_`import { Routes } from ‘./routes’;`_

The **<Routes/>** component is taking the place of the default CRA  _**<App/>**_ component. It’s basically the same — I just called it **<Routes/>** because I feel it makes sense to turn the code more meaningful and readable.

You are not loading an unique App anymore but a **Routes** component that will handle the routes and will trigger the mounting and rendering of the components which shall load within each route.

* We are embracing **<Routes/>** with the **<Router/>** component.

As a matter of fact, **<Router/>** works as a [Higher Order Component](https://reactjs.org/docs/higher-order-components.html) that only knows its children in the future and interacts with them in a more wide scope, independently of who and how many they are.

You do not have to worry about how it works to use it. This is a much deeper and advanced matter.

Just make sure you understand that **React.DOM** is not anymore **loading a simple App**. It’s loading the App embraced by a Component called `Router` that in a higher instance or scope can interact with it and with the browser `DOM`.

#### **<Routes /> Com**ponent

![Image](https://cdn-media-1.freecodecamp.org/images/hFLFpV5UPMby62nxbB2rzQUQmAzPLbJRRUaz)



#### So basically what does _routes.js_ do?



It starts by importing React and a few components we’ll take a look later. Just think of them as simple stateless components: **Home**, **About**, **TopicList**, **TopicDetail**, **NavBar** and **NoMatch**.

It also imports three components from the **react-router-dom** package which we’ll need to invoke: **<Route/>**, **<Switch/>**and **<Redirect/>**.

After the imports, we export the stateless component Routes which invokes the `NavBar` (which will be always in the screen) and a **<Switch/>** component.

#### What does this <Switch/> guy do?



This component basically renders the first child **<Route>** or **<Redirect>** that matches the browser location.

It starts to test stuff like this: “is the browser URL in this **<Route/>** path? No? Okay.” Next Route. “Is the browser URL in this other route path? No.”

Next Route. “Oh, I got it! It’s in this one, let’s trigger the Component render and finish the checking by now (I don’t care with the other routes below…)”

If by any chance this happens:

![Image](https://cdn-media-1.freecodecamp.org/images/pCLNszAHXi5Tl-gq0toLitQyc1cRQeKIBcxm)

the second route will never be triggered because Switch will jump off before reaching it. He just goes to have a coffee… (and me too!!! ? Back!)

Inside **<Switch/>** we define each **<Route/>**.

Each **<Route/>** tells this to the browser:  
“Hey browser DOM! If **<Switch/>** chooses me because your location is (exactly) this one, please render the following Component”.

![Image](https://cdn-media-1.freecodecamp.org/images/IAEvLJjBJE6kKk-8RAsqXskmBYFYLHgM0Hck)

Or in other cases such as the one below, it says:  
“Hey, browser, if by any instance your **<Switch/>** chose me because location is /Topics/”something” render Component Topic Detail. Certainly it’ll find out who is **this :topicId** (variable) thing that the user is asking us to match and route it accordingly”.

![Image](https://cdn-media-1.freecodecamp.org/images/4xy5vihwiXuuj1xpsrhmWu7kjnmvlCn8GMJn)

Okay everyone. Because **<Switch/>** has this default behavior of checking each route, we need to provide a fallback in case it doesn’t match anything:

![Image](https://cdn-media-1.freecodecamp.org/images/-Bw2qOlJNvs9k2GOwX3lYgeozuPGkCjApbav)

This last Route simply renders a default page stating that no route was matched, kind of an [HTTP 404](https://en.wikipedia.org/wiki/HTTP_404) error.

Remember that here we’re dealing with an SPA and with “Dynamic Routing” so this is a simulation as if we were demanding routes to a server ?. Actually we’re not!

We just do not know what to render if the user, for instance, inserts something not mismatched into the URL like this: _**http://localhost:3000/HelloWorld**_.

As this route was not defined, we provide a **NoMatch** component to inform them about the non-existence of the route.

**<Redirect/>** is there because if the user tries to load the URL without any route **http://localhost:3000/**, it would get a **NoMatch** because there’s no route defined for it. So the best way to handle this is make use of  **<Redirect/>** and push the user to the route of **/Home** which is by default our first screen of the app.

#### Why is this necessary?

Again, because usually the user would start the Application by typing it’s general URL and without the **<Redirect/>** the first rendered component would  be **<NoMatch/>**. We don’t want that, we want the user to be redirected to  the **<Home/>** component.



### **Views And / Or Components**

At this point in our guide, I’d like to stop a little bit to differentiate a View from a Component. This is not the essence of this guide, but will make sense after I show you the folder structure of my _CRA_.

When we are “[Thinking in React](https://reactjs.org/docs/thinking-in-react.html)” and we start making an App, and it starts to grow, sometimes we stop because we feel things are not in the right place.

This means that we need to give names to those things and keep them separated in different “drawers” or ”folders”.

Views and Components are things that are painted on screen. So what differentiates one thing from the other?

And are views not components? And components are not views?

Well, in terms of coding language, a View and a Component are certainly functions or classes — stateless components or stateful components as we call it in React lingo.

So what does differentiate them?

Well, a View has a route. Inside this View you can render a lot of components.

A component usually is an abstraction that can be invoked a lot of times in different views. It can be a button, a form, a chart. It can even be a more complex thing, while a view is unique and has a route.

This is a very simple concept that must be understood at the beginning, as soon as we start doing an app so small as a personal homepage.

Let’s take a look at my CRA folder structure:

![Image](https://cdn-media-1.freecodecamp.org/images/hkA3J3XhCQmBMSaZQiKxrMHciTyAglBaveTJ)
_CRA folder structure_

So, as you can see I — and 99% of the world — like to keep oranges and pears in different baskets. And so do you! I have faith in you! I trust you!

There are a lot of patterns on how to organize this stuff and a lot of discussion starts when we introduce more packages like Redux that transform a little bit the architecture of the app, or when we want to paint on the screen Dashboards, Widgets, Cycling Pigs or more weird stuff…

But, to differentiate concepts, take a careful look at Views and Components.

**Home**, **About**, **TopicList** and **NoMatch** are views. They have their own proper routes that trigger them.

**NavBar** is an omnipresent component that’s always invoked. It doesn’t have a route.

**TopicDetails** is a component that will display Topic info when the **TopicList/:topicId** route is triggered. It’s a reusable component that can be imported into other places and refactored or extended. It doesn’t have a specific route.

### **The Home / About Views**



Inside the Home folder, I have an _index.js_ and a _Home.js_ file.

Having an _index.js_ to export the other files is a good practice. Just trust me or bring some wine because this will be a long talk ?

… oh, let’s just drink the wine and we will talk later! ?

![Image](https://cdn-media-1.freecodecamp.org/images/JhqPLcyHbEQyDQJDGPmkFAJ-mR9-pgdCMzsL)
_**index.js that exports Home view**_

![Image](https://cdn-media-1.freecodecamp.org/images/B2JGUGC4cflc25P0fLBAXlxnnsioeIJFpNqV)
_**Home.js view stateless component**_

This is a simple view that only exports its title. The **About** view is equal to this one.

Now let’s take a look at the **TopicList View** because it’s a little bit different.

### **TopicList and TopicDetail Views**

![Image](https://cdn-media-1.freecodecamp.org/images/GbOKrOTh4Y4daFnJqRjMwikEiFxzmcg6fjHV)
_TopicList View Code_

So **TopicList View** has this detail of handling different routes. Remember that **/Topic/:topicId** route that **<Route/>** told **<Switch/>** to let **TopicDetail** handle? 

Here we are with that.

**TopicList** receives **{ match }** as a prop. Don’t let the destructuring feature scare you. We could simply receive props and call _props.match_. This is simply how all the cool kids nowadays destructure props to improve readability and React flow. I also like it a lot! This is kind of like picking up a box with your mobile inside or picking up the mobile directly. As a matter of fact it was kept inside the box but at this moment you only need to check your e-mail ? so let the box stay where it is! Don’t bring it with you to work!

Anyways, let’s keep focused on code.

In this file, we import a Component from React Router called **{ Link }** because we want to create Links ?

We receive a match from the Route we’ve chosen when we’ve clicked **Topics** and we are rendering an unordered list with 3 options: **Topic1**, **Topic2** and **Topic3**.

Basically if the User chooses **Topic1 Link** in the screen, the **<Link/>** will push the browser URL to that path **/Topics/Topic1**.

What happens next? **<Router/>** and **<Switch />** detect that the URL changed and take a look into their info to check what route needs to be fired. So they discover that now the route triggered is `the one for **/Topics/:topicId** and triggers **TopicDetail** rendering. **TopicDetail** will render **Topic1** details.

![Image](https://cdn-media-1.freecodecamp.org/images/1s20EOEWOhQoRsqZdn5SnOwixBEDUV7VOP65)
_TopicDetail Component_

**TopicDetail** receives **match** from the Router and renders the **topicId** located at **match.params.topicId**.

### **The NavBar Component**



The **NavBar** component has a special role here because it’s omnipresent.

Its function is to allow the user to navigate the website and to show the sections (routes) available.

As you’ve seen in the beginning, it’s inside **<Router/>** but outside **<Switch/>** so any view will always be composed with **NavBar** on top.

![Image](https://cdn-media-1.freecodecamp.org/images/RRwqmKgTbtRjQNW28kK0neRfS6idxrjYhjOT)
_NavBar Component Code_

As you can see, its role is basic. It only supplies **<Link/>** and tells **<Router/>** to ask **<Switch/>** to trigger the chosen **<Route/>** and render it on screen.



### **Last but not least**

I think that by this time you probably have a basic understanding of how React Router works and can be used to do a simple website.

If you want to check the code or test it you can pull my repo, available on [GitHub](https://github.com/evedes/React-Boilerplate-01).

### **Bibliography**

To make this article, I’ve used the React Router documentation that you can find [here](https://github.com/evedes/React-Boilerplate-01).

All the other sites I’ve used are linked along the document to add info or provide context to what I’ve tried to explain to you.

This article is part 1 of a series called “Hitchhiker’s Guide to React Router v4.” Parts 2–4 coming to freeCodeCamp throughout this week!

* **[Part II: [match, location, history] — your best friends!](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-4b12e369d10/)**
* **[Part III: recursive paths, to the infinity and beyond!](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-21c99a878bf8/)**
* **[Part IV: route config, the hidden value of defining a route configuration array](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-c98c39892399/)**

Thank you very much!

