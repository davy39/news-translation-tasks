---
title: Web APIs explained by selling goods from your farm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-27T04:46:11.000Z'
originalURL: https://freecodecamp.org/news/web-apis-explained-by-selling-goods-from-your-farm-84aaf99cfc78
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iYNkAqKLBM9qw2j1TdO6SA.jpeg
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have been to a farmer’s market or farm stand, then you can understand the
  concept of an application programming interface (API).

  If you are new to web development, you probably hear the term “API” a lot.

  “I can’t wait until ...'
---

By Kevin Kononenko

**If you have been to a farmer’s market or farm stand, then you can understand the concept of an application programming interface (API).**

If you are new to web development, you probably hear the term “API” a lot.

_“I can’t wait until that company releases their public API!”_

_“That company’s API is a confusing mess.”_

_“Do they have an endpoint for that data in their API?”_

Understanding the concept of an application programming interface (API) can be pretty difficult if you are not familiar with concepts like SOAP, HTTP, and XML.

So, I wanted to find a way to explain the way that web APIs work as a whole, so that when you get into the nitty-gritty technical details, you will understand how it all fits together.

In this tutorial, you are the owner of a farm that sells five products: chicken, pork, eggs, tomatoes, and corn.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JS5g1_gRC72cQhQA.)

In order to understand this tutorial, you just need to understand the difference between server-side code (back-end) and client-side code (front-end). You can read the beginning of my [guide to GET/POST](https://blog.codeanalogies.com/2018/01/15/ajax-basics-explained-by-working-at-a-fast-food-restaurant/) if you are not already familiar with server vs. client.

### The Difference Between A GUI and an API

Let’s start with a familiar way to use the web. The web browser, like Chrome, is an example of a graphical user interface (GUI). As the user, you can interact with a user-friendly tool in order to accomplish tasks, like booking flights or searching Google.

The GUI allows website visitors to interact with code on the server in a controlled and structured fashion.

As a farm owner, this is kind of like the farm stand that you set up on your property or your stall at the farmer’s market.

![Image](https://cdn-media-1.freecodecamp.org/images/0*uI8OpnP5gTeq9XLB.)

You can’t just stack your goods inside your barn, allow visitors to come in, and then expect to make money. Instead, you need to set up a booth so visitors can quickly understand your available goods and pricing.

This is the way that customers “interact” with your hard work. They don’t need to understand the planting process, or the equipment you use, or the processing. They just see the final product.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1CKu4-YZRsxGAB09.)

Notice how every customer experiences a one-to-one interaction. When they arrive at your stall, they are only looking at products from your farm.

### Then What Is An API?

There are other ways to sell your products besides direct to consumer. You can also sell to distributors and local restaurants, so that your products can be included in different dishes or sold in a grocery store.

This is a new way for consumers to “experience” your product. Sure, they might not know whose eggs are in their omelette when they order breakfast at the local diner, but they are still “using” your product.

But, from your perspective as a farm owner, you have a completely different sales process and supply chain. Now, you don’t need to carefully arrange a booth for consumers. Instead, you probably need to add a shipping bay to your barn so that distributors and restaurants can pull up their trucks and load up. You also need to package your goods for larger sales.

![Image](https://cdn-media-1.freecodecamp.org/images/0*9KQ-8Us5U8PvR90e.)

This is similar to the concept of an API. When you build an API, you make it possible for other developers to access your data and use it in their applications.

Just like restaurant customers can “experience” your chickens’ eggs by eating an omelette, website users can “experience” your product on somebody else’s website through a widget on the website or code on the other company’s servers.

Now, we have a new level of interaction. Your distributors and restaurant customers might interact with you one-on-one by visiting the farm, but they then expose thousands of customers to your products when they sell them later.

As the farm owner, you still must set up processes so that you can successfully serve these distributors. Similarly, an API is a structured way that others can utilize your server-side code. As the developer, you still have full control.

I used a search widget as an example in the image above, but really, just about anything could be used to access an API. That is just one example of a common way that website users experience APIs from 3rd parties. Other common ones include:

* Mapping tools
* Payment processing
* Weather data

### What Can Be Accessed Through An API?

Let’s say that you want to start selling eggs from your farm to distributors and restaurants. You would need to set up a series of processes on your farm to support this:

1. Mass storage of eggs
2. Accounting for monthly billing to customers
3. A shipping area to load up eggs onto trucks.

Before you set up all these processes, you need to decide whether you are ready to accept mass orders of eggs in the first place. Do you have enough hens to produce the right number of eggs on a weekly basis? If you don’t, you may put too much strain on your system and disappoint your customers when you run out of eggs.

API developers set up **endpoints** that allow other developers to access specific data from their database. The example above would be an “eggs” endpoint. If you do not create one in the first place, then customers cannot buy eggs from you.

You can set up specific endpoints for each product from your farm- chickens, pork, eggs, tomatoes and corn. Some may only be accessible through the farmer’s market (GUI) because you are not sure if you are ready to ramp up production to meet the needs of distributors.

![Image](https://cdn-media-1.freecodecamp.org/images/0*gtKR8rDGBgGewhIr.)

That is one difference between an API and an open-source database. In an open-source database, everything can be queried and accessed. When you set up an API for your back-end, you create endpoints that reveal only specific data.

Just like distributors are the ones that can now interact with your farm, developers from other companies are the ones that interact with your API. Once they write code that accesses data from your server, their website visitors can have new experiences based on your data.

### Tracking an Individual API Call

Let’s say that you decided to set up an **endpoint** for eggs at your farm. A local restaurant wants to buy 1000 eggs to satisfy the 1000 omelette orders it receives each week.

![Image](https://cdn-media-1.freecodecamp.org/images/0*c2DAEyegIUTrwM_W.)

Notice how our **API call** actually starts with a user request? That may feel a little counter-intuitive based on the description.

An individual **API call** occurs when some trigger happens, and code written by another developer sends a **request** to your API at a specific **endpoint**. Your API must deliver a response based on your server-side code.

In this case, the trigger is the order of 1000 eggs. The restaurant manager has already created a relationship with a farm — your farm. And, your farm has already set up the processes to deliver 1000 eggs at a time.

So, the 1000 egg order comes in, and your farm delivers the response: 1000 eggs.

Keep in mind, there might be 100 other restaurants that have created a relationship with your farm, and 10 of them may send a **request** at the same time! That is where scalability comes into play. You need to decide if your server is ready to handle that demand. But that is a topic for another tutorial!

![Image](https://cdn-media-1.freecodecamp.org/images/0*4QZDXA5t95N7vboE.)

Here is the technical version of the sequence above, if you had a mapping application that could be used on other websites like Google Maps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*SkAzRcrC2zXcNLy9.)

1. Some user on another site uses your mapping application, and takes an action that requires data from your server.
2. The developer on that other site has already written the code that will create a **request** to your API based on the action from that user
3. The **API call** comes in, and your server delivers a **response.**

Of course, there are probably 1000 other web apps that are using your mapping widget, so you need to be prepared for all those API calls!

![Image](https://cdn-media-1.freecodecamp.org/images/0*0wWqB2oCcd7-WNuO.)

### Examples of GET and POST

Here is a [quick refresher on GET and POST](https://blog.codeanalogies.com/2018/01/15/ajax-basics-explained-by-working-at-a-fast-food-restaurant/) if you need to read up.

So far, in our farm examples, the requests in our little scenario have resembled GET requests. Due to requests triggered by the restaurant’s customers, the restaurant must send a truck to your farm to pick up eggs.

But what about POST requests? In a real world example, the Facebook API allows users of other apps to create posts, and then that app can send those posts directly to Facebook to go live immediately.

In some cases, like social media APIs, it may make sense to allow the end-user to post directly to a social platform from a third party app.

But here is another example. The Amazon API allows online store owners to programmatically post their products to Amazon’s Marketplace. In that situation, the developer on the team of the independent online store owner can also create a presence on Amazon. So, the API does not involve any sort of end user or website visitor.

In our farm example, this is kind of like the way you might handle monthly billing. After restaurants and distributors visit your farm all month to buy products, you send them a bill at the end of the month that details the payment they must send.

Just like the restaurant must build their own processes to make sure they collect eggs at the right time, they must also have a process for paying you on time. This probably involves their accountant. Let’s say that the accountant knows that they must pay you on the first of the month.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2OLXd7qM5P3DMsaI.)

Now, how might the user/customer trigger a POST request? Well, imagine that the restaurant immediately sent you a payment each time someone ordered food that came from your farm. If a person ordered a $5 omelette, and $2 of the cost came from the eggs from your farm, the restaurant would immediately send the $2 to your bank account. If this was a web app, that level of communication might work, but since this is a farming example, that would be a little impractical.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6KCimIOx44uBhIYm.)

### The Difference Between a Farm and a Web App

As you can start to see in the last example, there is one major difference between our little farm supply chain and an API call. Timing.

Simply due to the logistics of the real world… we cannot hope to match the instantaneous nature of most API calls, even if the steps are generally the same.

Let’s look at the example GET request from earlier in the tutorial.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Ln76YuGduAcDlTqg.)

Here is what that means in web development terms.

1. User takes an action that triggers a request
2. Code on the server-side makes an API call to an endpoint
3. API delivers specific information

But if we draw the analogy to a real-world farm:

1. User orders an omelette
2. Restaurant sends a truck to pick up eggs at your farm.
3. Eggs are delivered to the restaurant and served in the omelette

It would be incredibly impractical to send a truck to a farm to make the freshest omelette known to humankind. But, the steps are still the same. So I just wanted to mention this difference in timing.

But, when a user triggers a request when they use a web application, they usually get a nearly instant response.

### What Does It Mean To “Open Your API”?

So let’s return to our original question: What does it mean when a company “opens their API”?

It means that they have valuable data available on their server that they can now reveal via specific **endpoints**. The company gets to determine how developers from other companies can access their data, but at the same time, they are making it widely available in a structured way.

In our farm analogy, this is the point when your farm decides to sell your products to distributors and restaurants, and sets up the internal systems to handle mass orders.

### Enjoy this tutorial?

If you enjoyed this tutorial, you will probably like the rest of my visualized guides to web development topics. Read further on the [CodeAnalogies blog](https://codeanalogies.com/), or sign up hear to get the latest tutorials:

