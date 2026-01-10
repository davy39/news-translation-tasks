---
title: AJAX Basics Explained By Working At A Fast Food Restaurant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-15T04:22:43.000Z'
originalURL: https://freecodecamp.org/news/ajax-basics-explained-by-working-at-a-fast-food-restaurant-88d95f5fcb7a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5NmA_RD2IAd7_htOB7RKNA.jpeg
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kevin Kononenko

  AJAX (Asynchronous JavaScript And XML) can be pretty confusing if you do not have
  a firm understanding of server-side code.

  When I started with web development, I first learned HTML, CSS, JavaScript, and
  jQuery before I ventured in...'
---

By Kevin Kononenko

**AJAX (Asynchronous JavaScript And XML) can be pretty confusing if you do not have a firm understanding of server-side code.**

When I started with web development, I first learned HTML, CSS, JavaScript, and jQuery before I ventured into Node.js and Ruby on Rails.

But, of course, I wanted to understand how to build dynamic web applications, so I needed to learn how to use AJAX to communicate with a server. I didn’t want to just build static pages that were straight out of 2005.

The front-end is a completely different challenge than back-end. I struggled to understand the different parts of a GET or POST request.

So, I came up with the analogy of a fast-food restaurant to explain it. If you have been to a McDonald’s, Burger King or Wendy’s, then you can write your own GET and POST requests.

In order to understand this post, you will need to have a beginner’s understanding of jQuery.

### What does AJAX look like?

Have you ever noticed that you can comment on a post on Facebook without reloading the entire page? That is AJAX at work. **AJAX** allows users to interact with your web application without completely reloading the page.

Imagine if every time you “liked” a post on Facebook or added a comment, the page reloaded? That would be terrible! Instead, Facebook quickly adds your ‘comment’ or ‘like’ to the post and allows you to keep reading. They add that interaction to their database without interrupting your experience!

### Why do we need AJAX?

Okay, those are anecdotal examples, so let’s look at the entire system.

Think of your whole web application as a fast-food restaurant. You are the cashier, the person on the front-lines. You handle **requests** from customers.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PBD--x73I4_zG0Kh.)

If you look at this diagram, I can see three separate jobs that need to be done.

1. The cashier must handle user requests at a fast pace.
2. You need cooks to throw the burgers on the grill and cook all the food.
3. You need a meal prep team to package the food up and put it in a bag or on a tray.

However, if you did not have AJAX, you would only be allowed to process one order at a time from start to finish! You would need to take the order… then charge the customer… then sit there doing nothing while people in the kitchen cook the food…. then continue waiting while the meal prep team packages it up. You could only take the next order after all that.

![Image](https://cdn-media-1.freecodecamp.org/images/0*89PNzvIka550TPv2.)

Now THAT is a bad user experience! You would not be able to call it “fast food” anymore. Instead, you would need to call it “mediocre food”… or something.

AJAX allows for an **asynchronous processing model**. That means you can request data or send data without loading the entire page. This is just like the way a normal fast food restaurant operates. As the cashier, you take the customer’s order, send it over to the kitchen team, and get ready to take the next customer’s order.

Customers can continue to make orders, and you do not need to sit there while the employees in the kitchen work and make everybody wait.

This certainly introduces some complexity. You now have multiple specializations within the restaurant. Additionally orders are being handled at different paces. But, it creates a much better user experience.

![Image](https://cdn-media-1.freecodecamp.org/images/0*716D3LoopXh8ILWC.)

You have probably seen this in action at a restaurant yourself. One person is working the fries machine. One person is managing the grill. When an order comes in, the cashier can instantly communicate with both and get back to taking orders.

### How To Create A POST Request

Let’s put these concepts to work. As the cashier, you need to send incoming customer requests to the kitchen so that the rest of your team can prepare the meal. You can do that with POST request.

In your actual code, a POST request sends data to your server. That means that you are sending order data to the back-end, in this case.

It has three major parts:

1. **A URL**: this is the route that the request will follow. More in a minute.
2. **Data**: any extra parameters that you need to send to the server.
3. [**Callback**](https://blog.codeanalogies.com/2016/04/11/javascript-callbacks-explained-using-minions/): What happens after you have sent the request

What are some common things that people order in a fast-food restaurant? Let’s look at 2 examples.

1. Fries
2. A combo meal composed of a burger, fries and a drink

These two require different processes. A fries request might only need one person to scoop some fries into a sleeve. But a combo meal order will require work from multiple team members. So, these two need different URLs.

```
$.post('/comboMeal')
```

```
$.post('/fries')
```

The URL allows us to use the same logic on the back-end for certain types of requests. That part is outside of the scope of this tutorial, so you can dig into that a little more when you look at the back-end.

Next is the **data**. This is an [object](https://blog.codeanalogies.com/2017/04/29/javascript-arrays-and-objects-are-just-like-books-and-newspapers/) that tells us a little bit more about the request. For the combo meal URL, we probably need to know:

1. The type of main meal
2. They type of drink
3. The price
4. Any special requests

For the fries, we might only need to know:

1. The size of the fries
2. The price

![Image](https://cdn-media-1.freecodecamp.org/images/0*6W8k6X4azQU9Jb3b.)

Let’s look at an example of a combo meal: a cheeseburger with a Pepsi that costs $6.00. Here is what that looks like in JavaScript.

```
let order = {  mainMeal: 'cheeseburger',  drink: 'Pepsi',  price: 6,   exceptions: '' };
```

```
$.post('/comboMeal', order);
```

The _order_ variable holds the contents of the order. And then we include it in the POST request so that our kitchen staff knows what the heck to put in the combo meal!

But, we can’t have all of this code run at a random time! We need a trigger event that will set off the request. In this case, a customer order at a fast food restaurant is kind of like a person that clicks an ‘order’ button on your website. We can use jQuery’s [click() event](https://api.jquery.com/click/) to run the POST when the user clicks a button.

```
$('button').click(function(){   let order = {     mainMeal: 'cheeseburger',    drink: 'Pepsi',     price: 6,     exceptions: ''   };   $.post('/comboMeal', order); });
```

Last part. We need to tell the customer something after their order has been sent. Cashiers usually say “Next customer please!” since this is a fast food restaurant, so we can use that within the callback to show that the order has been submitted.

```
$('button').click(function(){    let order = {     mainMeal: 'cheeseburger',     drink: 'Pepsi',     price: 6,     exceptions: ''    };
```

```
$.post('/comboMeal', order, function(){     alert('Next customer please!');   }); })
```

### How To Create A GET Request

So far, we have the ability to submit an order. Now, we need a way to deliver that order to our customer.

This is where GET requests come in. GET allows us to request data from the server (or kitchen, this analogy). Please note: right now, our database is full of orders, not the food itself. This is an important distinction because **GET requests do not change our database**. They only deliver that information to the front-end. POST requests change the information in the database.

Here are some typical questions you might get asked before receiving your food.

1. Would you like to eat here or get the food to go?
2. Do you need any condiments (like ketchup or mustard)?
3. What is your number on the receipt (to verify it is your food)?

So, let’s say you ordered three combo meals for your family. You want to eat the food in the restaurant. You need ketchup. And the number on your receipt is 191.

We can create a GET request with a URL of ‘/comboMeal’, which corresponds to the POST request along with the same URL. However, this time we need different data. It is a totally different type of request. The same URL name just allows us to better organize our code.

```
let meal = {  location: 'here',  condiments: 'ketchup',  receiptID: 191 };
```

```
$.get('/comboMeal', meal);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*v3wuuGaPDFsYr-pgR7a6bg.png)

We also need a trigger for this one. This request is triggered by customers answering your questions as the cashier before you deliver the food to them. There is no convenient way to represent questions and answers with JavaScript. So I will just create another click event for the button with class ‘answer’.

```
$('.answer').click(function(){  let meal = {     location: 'here',     condiments: 'ketchup',     idNumber: 191,   };
```

```
$.get('/comboMeal', meal); });
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*dbcZP0FyqCa19uYK.)

This one also needs a callback function, because we are going to receive whatever was contained in the three combo meals in order 191. We can receive that data through a _data_ parameter in our callback.

This will return whatever the back-end stipulates for order 191. I am going to use a function named _eat_ to signify that you eventually get to eat the food, but keep in mind that there is no eat function in JavaScript!

```
$('.answer').click(function(){   let meal = {     location: 'here',     condiments: 'ketchup',     idNumber: 191,    };   //data contains the data from the server   $.get('/comboMeal', meal, function(data){      //eat is a made-up function but you get the point      eat(data);   }); });
```

The final product, _data_, would contain the contents of the three combo meals, theoretically. It depends on how it is written on the back-end!

![Image](https://cdn-media-1.freecodecamp.org/images/0*CmjCchSTgQN7L6Bg.)

### Try Other Visual Explanations

Did you enjoy this tutorial? Give it a clap so others can see it! Or, **sign up for the newsletter** to hear about the latest releases of CSS and JavaScript tutorials.

