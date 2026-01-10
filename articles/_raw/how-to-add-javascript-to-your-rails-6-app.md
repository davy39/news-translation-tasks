---
title: How to Add JavaScript to Your Rails 6 App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-10T16:04:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-javascript-to-your-rails-6-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/carl-heyerdahl-KE0nC8-58MQ-unsplash--1-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Rails
  slug: rails
seo_title: null
seo_desc: "By Daniel Wesego\nAs a junior Full-Stack developer, my main focus was the\
  \ backend. I wanted to learn how to program my backend server to serve my web application.\
  \ \nBut after learning the basics of the the backend, I learned that the frontend\
  \ was just ..."
---

By Daniel Wesego

As a junior Full-Stack developer, my main focus was the backend. I wanted to learn how to program my backend server to serve my web application. 

But after learning the basics of the the backend, I learned that the frontend was just as important as the backend. And one way to increase the liveliness of your web application is by adding JavaScript.

JavaScript is essential to add interactivity to your web application. Of course, it has become far more than that now. It is a programming language that web browsers run. Many websites you have visited use some JavaScript code in their frontend. 

You may have started using Ruby on Rails to build your web application and wondered how to add JavaScript to your code. In this article, I'll show you how to add JavaScript code to your Rails app.

## Why JavaScript?

You may wonder why you even need JavaScript in your web application in the first place. In short, if you don't include any JS, then your web application's user experience will not be good.

Let's say you have a form that a user fills out and you want to do form validation. If the user submits the form without filling in the proper values, the page for the form has to reload again, hitting the server and coming up again for the user. That takes a lot of time and will probably annoy the user.

Of course you can sometimes get away with HTML form validation, but that's not always possible. Adding a simple script that checks the user inputs and notifies them that they should input the correct information is much better.

Of course this doesn't mean you can ignore server side validation, but that's for another article.

Another use case is loading files asynchronously, which you can do in JavaScript without reloading the whole page. You may have used some web apps that load more pictures and articles as you scroll down without having to refresh or change the page over and over again.

These and other use cases are great reasons to use JavaScript in your application. In fact, the demand for JavaScript has been increasing. You can even use it to write your backend. 

But we love Rails, so we are going to stick with it for a while. 

## What we'll cover here

At the time of writing, the latest version of the framework is Rails 6, and it has brought some changes to the way you interact with JavaScript. 

Prior to Rails 6, we had the asset pipeline to manage CSS and JavaScript files. But starting from Rails 6, Webpacker is the default compiler for JavaScript. CSS is still managed by the asset pipeline, but you can also use Webpack to compile CSS. 

You won't find your JavaScript folder in the same place as you did in Rails 5. The directory structure for JavaScript has changed to the **app/javascript/packs/** folder.

In that folder you will find the **application.js** file, which is just like the **application.css** file. It will be imported by default in the **application.html.erb** file when you create your new Rails app. 

The **application.html.erb** file will be used by all views. 

## Adding a script that will be used by all views

If you want your JavaScript to be available in all views or pages, you can just put it in the **application.js** file:

```js
require("@rails/ujs").start()
require("turbolinks").start()
require("@rails/activestorage").start()
require("channels")

console.log('Hello from application.js')
```

The first four lines are there by default. I have added a `console.log` statement to show you that the JavaScript will be available everywhere. 

You can test this by viewing any page in your application and opening the developer console. 

But you may not always want your JavaScript code to be loaded on every page. Instead, you can make the script available only when visiting a specific page.

## Adding a script that will be used by a specific file

If you want your JavaScript to be available for only a specific view, then you can use the **javascript_pack_tag** to import that specific file:

```html.erb
<h1 class='text-center'>I want my JS here only</h1>

<%= javascript_pack_tag 'my_js' %>

```

```js
console.log('Hello from My JS')
```

Remember that you need to add the file in the **packs** directory. The **javascript_pack_tag** should also refer to the name of the JavaScript file you created. 

Now the script will only run when the specific view that includes the **javascript_pack_tag** is loaded in the browser.

## Wrapping up

I hope this article helps clear up any confusion you might have when updating your app to Rails 6, or if you just got started with Rails. 

You can follow me on [Github](https://github.com/DanielMitiku) if you want to learn more.

