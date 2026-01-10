---
title: 7 React Projects to Build in 2024
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-01-16T12:07:51.000Z'
originalURL: https://freecodecamp.org/news/react-projects-to-build-in-2024
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/mugshotbot.com_customize_color-orange-mode-light-pattern-bubbles-theme-two_up-url-https___gifcoins.io--1-.png
tags:
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: null
seo_desc: 'To be confident with using React, you need to build real-world projects.
  But what projects are worth building in 2024?

  I have put together a list of seven projects that I think are ideal for becoming
  a confident React developer, from simple to comple...'
---

To be confident with using React, you need to build real-world projects. But what projects are worth building in 2024?

I have put together a list of seven projects that I think are ideal for becoming a confident React developer, from simple to complex applications. This will give you some inspiration for what apps to build.

I'll also walk you through the entire tech stack I would use to build each project, as well as a summary of how to build each one step by step.

Let's get started!

## 🤖 ChatGPT AI App

As ChatGPT becomes more powerful, you can build impressive applications using the ChatGPT API.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/chatgpt.png)
_ChatGPT AI app: Draw-a-UI_

This is a great starter app because, for most applications, all you need to do is send text or an image to the ChatGPT API, give it some instructions, and it'll send a response back to you.

You could use the ChatGPT API to build a text summarizer, a translation app, an app that explains what a code snippet does. The possibilities are really endless.

One simple ChatGPT-powered AI app that I've built is "Draw a UI", where you can draw a quick mockup of a user interface, send it to ChatGPT, and it'll actually send you back the HTML that was generated according to your screenshot!

I would build this application using Next.js as well as the `tldraw` npm package, which allows you to draw pictures in your React app.

Next, send that screenshot to a Next.js route handler on the back end that uses the **openai** npm package to talk with ChatGPT, and then sends you back the HTML code.

## 👨‍💻 Personal Website

If you're not ready to build something very complex yet, a personal website is a great starting point. You can use it as a way to get comfortable working with JSX and CSS in React.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/portfolio.png)
_A personal website made with Next.js and TailwindCSS_

Learn how to create basic components, add images, links to your social media profiles, and so on. When you start building more projects, you can show them off on your website.

The great thing about a personal website is that you can extend it as much as you want. You can add your own integrated blog, or you can talk about things that you've learned or what you're working on at the moment.

In order to build your personal website, I would recommend using Next.js because it makes it so easy to build individual pages that are statically rendered, which is good for SEO.

For the images, you can use the integrated `next/image` library. And for making a blog, I'd highly recommend using the ContentLayer package , which you can use to write all of your blog posts as markdown or MDX.

ContentLayer is great because it makes your markdown content type safe so you know what data each blog post includes. This is also a great way to get started with TypeScript in React, although it may seem intimidating at first.

## 💬 Chat App

A truly dynamic web application would be a chat app, something that you likely use every day. It's good to build applications that you're familiar with because it gives you a good idea of what parts it's composed of.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/chat.png)
_Chat App made with React, similar to WhatsApp_

A chat app is simple in terms of its components. You only need a messages area, an input to type new messages, and a list of people to chat with.

It's a great project because it can be as simple or as complex as you like. To build something like this, I would use Vite to create the React project and power the backend with Supabase.

You don't need any server-side code here with Supabase, and it also gives you real-time chat functionality, entirely free. You can add authentication to identify users (using Supabase Auth), and put all the created users in a sidebar to chat with.

Then you can create a table for messages and send them off to Supabase whenever someone types in some text. To extend it further, you could make it possible for them to add images and video with Supabase Storage.

Finally, you can display messages in real-time using subscriptions depending on to the user you're chatting with.

## 💳 E-Commerce App

The next type of app we'll talk about is an e-commerce app. 

An e-commerce app can be used for selling physical or digital products with a one-time purchase feature.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/ecommerce.png)
_An E-Commerce app with physical goods, made with Next.js_

After the purchase, you need to deliver it to the customer. The e-commerce app could be very complex, but it doesn't have to be at the start. You just need to make a basic storefront with your products.

Give them an associated image with a description, as well as a buy button. You don't even need to add authentication. To build this, I would use Next.js integrated with Stripe to handle purchases.

The inventory system doesn't have to be very complex if you're selling a physical product. It could be as simple as having a number in a database that can be updated whenever stock is added and decreased whenever someone makes a purchase.

## 🛒 Online Marketplace 

The online marketplace is an extension of the e-commerce app. It's a bit more complex because you're adding more products. 

You might also consider adding extra features such as reviews, which are essential to online shopping.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/marketplace.png)
_Next.js store with an integrated shopping cart and reviews_

The challenge in this case is adding a shopping cart. To make for a good user experience on a website with many products, you want to allow customers to add multiple products to their cart.

To add a shopping cart, I would use the same stack as before, Next.js and Stripe, to handle managing and purchasing the products. Fortunately, there's a great package called use-shopping-cart, which integrates perfectly with Stripe checkout. 

You can use it to make a complete shopping cart with the ability to add and remove items, as well as clear the cart right out of the box.

For reviews, you could add a database layer like Supabase, or you could outsource reviews to a third-party service that allows you to integrate reviews, like Trustpilot, for example.

## 🚚 SaaS App (Software as a Service)

The final evolution in doing sales online with React is a SaaS application.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/saas.png)
_Gumroad inspired SaaS app made with Next.js_

In this app, you provide customers access to a certain software service that you've made, usually for a monthly or yearly subscription fee.

You can create a SaaS application as a paid version of an app that you've already built, such as the AI app or the chat app.

In short, if you can build an application that users would pay for, either to be more productive, for entertainment, or to educate them, then all you need to do to make a SaaS app is to charge those customers a fee for using it.

A SaaS app could charge users based on usage or over a set period of time, such as a month or a year. 

This can be done with the help of Stripe or a merchant of records such as Paddle, which makes taxes easier. Both of them can handle subscriptions.

I would recommend using Stripe Checkout to allow customers to manage their subscription and cancel it if necessary.

## 📱Real-World App Clone

Finally, the most ambitious project would be to build a clone of an app that you really like or that you use every day.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/clone.png)
_A clone of the YouTube web app with React_

An app clone is very difficult because you're usually cloning something that a big company is based off of. However, doing so is a great approach to leveling up your skills as a React developer because you have to think through about how a service is made.

If you were to clone something like YouTube, for example, you're not only going to build out the user interface and have it look like YouTube's, but you'll also need the functionalities that YouTube has, such as menus and drawers and notifications, and the ability to add and view videos, comments, likes, and so on.

If I were to build a YouTube clone, I would use either Supabase or a MySQL database like PlanetScale, along with Next.js, and authentication with Supabase or NextAuth.

I would build the user interface with TailwindCSS and Radix UI. Radix is a library that provides simple (primitive) components that can be easily styled, but are fully functional, which saves you a bunch of time.

To upload videos and media, I would use a platform dedicated to streaming videos such as Mux, which provides a great developer API.

For storing images and all other media and attachments, I would use Supabase Storage.

How far you take it really depends on your ambition and whether you want it to be a business of your own or a great portfolio project to show off to potential employers.

## 🛠️ Want to Build All the Projects?

You can learn exactly how to build each project within this list inside the all-new React Bootcamp:

✨ **[Introducing: The React Bootcamp](https://www.thereactbootcamp.com)**

You'll learn how to build every project in this list through hours of step-by-step videos, plus the complete source code to make them your own.

The bootcamp features every resource to help you succeed with React:

* 🎬 200+ in-depth videos
* 🕹️ 100+ hands-on React challenges
* 🛠️ 5+ impressive portfolio projects
* 📄 10+ essential React cheat sheets
* 🥾 A complete Next.js bootcamp
* 🖼️ A complete series of animated videos

Click below to try the React Bootcamp for yourself.

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)  

