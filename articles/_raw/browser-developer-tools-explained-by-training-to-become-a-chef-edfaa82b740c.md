---
title: Browser Developer Tools Explained By Training To Become a Chef
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-21T04:11:43.000Z'
originalURL: https://freecodecamp.org/news/browser-developer-tools-explained-by-training-to-become-a-chef-edfaa82b740c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zdQasZBj8_S3hYF4CAgbHw.jpeg
tags:
- name: JavaScript
  slug: javascript
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

  If you have ever visited a restaurant, this guide will help you understand how dev
  tools like Chrome Dev Tools and text editors like Sublime Text work.

  When you are building your first website with HTML and CSS, you can easily get ...'
---

By Kevin Kononenko

If you have ever visited a restaurant, this guide will help you understand how dev tools like Chrome Dev Tools and text editors like Sublime Text work.

When you are building your first website with HTML and CSS, you can easily get overwhelmed with all the new technologies that are needed to deploy even a basic site.

Hosting services?

Text editors?

[File directories](https://blog.codeanalogies.com/2018/06/24/file-directories-explained-by-getting-dressed-in-the-morning/)?

All of these technologies go way beyond the tutorials that you may have tried on sites like [freeCodeCamp](http://freecodecamp.com/) and [Codecademy](http://codecademy.com/)!

So, I figured a quick tutorial on using text editors and dev tools would remove one confusing part of the process.

In fact, all of this closely resembles the way that a restaurant chef might create new meals to serve to customers. Think of the concept of a recipe. A recipe is a specific set of instructions and ingredients that will produce the exact same meal over and over. As you are about to see, the process of developing a new recipe is kind of like building a website with HTML and CSS.

![Image](https://cdn-media-1.freecodecamp.org/images/0*F-EL1qZ_NXoH7-Cd)

In order to understand this tutorial, you just need to know HTML and CSS basics. Let’s jump into it.

#### Comparing A Recipe and Front-End Code

Let’s think about the fundamental goal of being a chef. Your goal is to translate recipes into delicious food for customers. Of course, it becomes difficult when you consider all the factors that you need to juggle at once: incoming orders, different timing, etc. But let’s forget about that for a moment.

Here is what a restaurant system might look like.

![Image](https://cdn-media-1.freecodecamp.org/images/0*B0f0CXgRdEfzZUBO)

1. A chef develops a recipe that will be used every single night at the restaurant. It can be replicated over and over again by the kitchen staff, and turned into the same meal every night.
2. The kitchen staff follows instructions on the recipe
3. The final product is the meal (looks like pasta and meatballs in this case, what kind of chef is this?)

Similarly, when you are building a website, you must write code that can be interpreted by a browser so that the exact same website can be served to visitors across the world.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5FogkHgSQE8DdXMW)

1. You write code using HTML, CSS and JavaScript that will produce a full webpage
2. A browser interprets that code and transforms it into a GUI (graphical user interface)
3. A website visitor experiences the site (For example, Google.com)

Each time that you visit a particular website is called a “**session**“. Every time that you open up a page on a new **domain** (like Google.com or Facebook.com), a new session begins and lasts until you leave the domain. So, one person can visit multiple pages within a session. The session is kind of like the visit to a restaurant.

#### What are dev tools, then?

Dev tools allow you to inspect the underlying code of a website and play around with it. If you use the Chrome Web Browser, then you can use [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools/), for example. Just right-click anywhere on the page, and select “Inspect”, the last option on the menu.

Dev tools allow you to manipulate the styling, structure, and JavaScript on the page within an individual session. But, these changes will not last if you refresh the page and begin a new session.

![Image](https://cdn-media-1.freecodecamp.org/images/0*55kT4xY-Ei77yv8s)

In this case, I changed the background color of the **input** element to blue. Pretty boring stuff. You can go to any other website and do the same thing. Of course, the changes will never last beyond your individual session.

This is kind of like being that person in the restaurant that takes a delicious meal… and puts hot sauce on it. Because you’re that type of person that loves hot sauce on everything. ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*AC9vkIwvCUgtmLoY)

Your love for hot sauce will have no impact on the recipe itself. It will have no impact on the other similar meals that will be served that night. And, if you go to another restaurant, you will have to ask for hot sauce all over again.

![Image](https://cdn-media-1.freecodecamp.org/images/0*UhPaUxJpiboe_T27)

In the same way, you can use developer tools to play with the code on another domain, but it will not have any impact beyond that particular session on that domain.

#### Using Dev Tools While Building Your First Website

As the chef, it’s your job to come up with recipes that will lead to food that customers love. But, you **probably** don’t want to figure this out by inventing a recipe, giving it to the kitchen staff, and learning later whether the customers liked it or not.

Instead, you probably want to test out a bunch of recipes in your own kitchen, and then release the one that seems to taste best.

This removes all the complexity of working with a kitchen staff and producing a high volume of food. You are acting as both the chef and the customer at once.

![Image](https://cdn-media-1.freecodecamp.org/images/0*BglqPJucNuE0AOzL)

Notice that in this case, you have control of both the recipe and the final product. So, instead of pushing one meal out to customers, you can make part of a recipe, then combine ingredients in different ways. Then, you can adjust the recipe as you go to reflect the combinations that are working.

When you are building your first website, you should also use the original code alongside developer tools to adjust your website on your laptop or desktop.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8CxZHcH6Lljbk4KV)

The text editor (like Sublime Text, Vim, or Emacs) is the tool that allows you to change the original recipe — the HTML, CSS, and JavaScript files.

However, as you are adjusting your browser in real-time, you probably will not want to change the “recipe”, save the file, and reload the page every single time. It’s exhausting!

Instead, you can shorten this feedback cycle by making changes using developer tools, and then adjusting the “recipe” after you create something worth saving in the browser itself.

Remember, if you build something valuable using developer tools, but then refresh the page, your changes will be gone. Even if the file is hosted locally on your computer.

#### Developer Tools Only Work for the Front-End

Of course, a restaurant has many processes going on at once that support the chef. There is the person that greets you at the door, the servers, the cleanup crew, the bartender, and so on.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vcuFkRYKEKX3vyhy)

These are the people that are not involved in the translation of recipes into food, but still help run the restaurant’s operations.

This is kind of like server-side code, or the **back-end**. Although you write server-side code with a text editor as well, you cannot make any changes via developer tools.

Why is this? Well, can you imagine if individual customers were allowed to change the rules of the restaurant like they can change their food? It would be madness! Customers can’t change the way the restaurant operates, no matter how badly they want to.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7jJULiF0FDXjRoZ8)

Developer tools only allow you to adjust HTML, CSS, and JavaScript. They do not reveal server-side code, since that would allow anyone to identify any security vulnerabilities presence within the web application. But, server-side code is also written in a text editor.

If you’d like to learn more about setting up server-side code for the first time, check out my [guide to the concept of a localhost](https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/).

#### Get The Latest Tutorials

Did you enjoy this tutorial? Give it a “clap” ? or sign up here to get the latest visual tutorial on web development topics.

