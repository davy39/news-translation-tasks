---
title: JavaScript’s apply, call, and bind explained by hosting a cookout
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-30T01:00:42.000Z'
originalURL: https://freecodecamp.org/news/javascripts-apply-call-and-bind-explained-by-hosting-a-cookout-84b85977ee11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FHLfdvXWAWi0HEBC83P8nw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever been in charge of operating the grill at a family event or party,
  then you can understand apply, call and bind in JavaScript.

  If you want to write clear code that you (or a teammate) can re-read at a later
  date, he...'
---

By Kevin Kononenko

**If you have ever been in charge of operating the grill at a family event or party, then you can understand apply, call and bind in JavaScript.**

If you want to write clear code that you (or a teammate) can re-read at a later date, here is one common rule: don’t repeat yourself!

If you create repetitive methods or functions, your code will be harder to maintain going forward. You will create bugs simply by failing to remember to update multiple versions of the same code.

If you have a firm understanding of the [concept of _this_ in JavaScript](https://blog.codeanalogies.com/2018/03/12/javascripts-this-explained-by-starting-a-high-school-band/), you know that this can be especially challenging as you try to track **execution context**. That is the relationship between the **function** and the **object** that it is being called upon.

In order to write cleaner code, you can use the **apply, call, and bind methods** to purposefully manipulate execution context. Different objects can share methods without rewriting them for each individual object.

Apply, call, and bind are sometimes called **function methods**, since they are called alongside a function.

If you are looking for a more technical explanation, I recommend the guide from [JavaScriptIsSexy](http://javascriptissexy.com/javascript-apply-call-and-bind-methods-are-essential-for-javascript-professionals/).

### How is this like cooking, exactly?

These three methods are kind of like applying cooking skills to prepare food for a cookout. Think of the different contexts that you might need to cook:

1. A general meal that you can cook pretty much any time and make everyone happy (pasta and sauce)
2. A cookout that might also be a party (burgers, hot dogs etc.)
3. A fancy dinner for just you and your partner (fish and wine)
4. Making dessert for a potluck event (cake)

Each one of these requires a different set of cooking techniques. Some are unique to an individual context, while others are more generalized. I will explain more in a minute.

In this case, each cooking context is kind of like an object. If you say that you are going to be cooking out on the grill, for example, that implies that you have a few skills… like operating a grill!

So, if we have an individual method for each of the cooking techniques you might use, there will be some unique methods to each object, and some cases where a method can be applied to multiple objects.

![Image](https://cdn-media-1.freecodecamp.org/images/0*7trEAvHGVHWAL1UH.)

In the code above, boiling water is a generalized skill that can probably be applied in any context.

Let’s use an example. The grill() **method** is within the context of the cookout **object**. That means that if you are holding a cookout, you expect that you will need to call up those grill skills.

But wait. You don’t forget how to use the grill when the cookout ends! Let’s say that you are your partner want to cook a steak for a fancy dinner, like the fancyDinner object. You still want to be able to borrow that grill() method from the cookout object. That is where apply, call, and bind come in.

This relationship between cooking skills (methods) and cooking contexts (objects) will be the main way that I show how to use apply, call, and bind().

In order to understand this tutorial, you are going to need to understand _this_ in JavaScript. Check out my [tutorial on JavaScript’s _this_](https://blog.codeanalogies.com/2018/03/12/javascripts-this-explained-by-starting-a-high-school-band/) if you need to review that.

### An Introduction to the Bind Method

Let’s imagine that you are holding a cookout for your son or daughter’s 10th birthday party. You want to cook three types of meat on the grill to satisfy everyone: chicken, burgers, and steak. They are apparently all meat eaters at this party.

However, you have no idea what each individual person wants! So you are going to need to ask each attendee when they arrive at the party. Each type of meat generally requires the same steps:

1. Add seasoning
2. Put it on the grill
3. Remove from grill after a certain amount of time

So there is no point in writing a separate method for each type of meat. The only thing that varies is the cooking time. Burgers take 15 minutes, chicken takes 20 minutes, and steak takes 10 minutes.

We want to use the same general process for all of these types of meat. The details will vary.

You may think, “Oh, this is a great time for a function!” But it is a little more complicated than that. As we said above, we are trying to use the concept of **execution context** to show our cooking skills. You wouldn’t want to cook burgers, chicken, and steak for the first time for an entire party. So, we must represent the skills you have gained over years of cooking, and how you will be applying them to this one particular scenario.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MKGALKHF_hr9Equr.)

In this case, our grill method just logs a sentence about when the individual person’s food will be ready. We are going to use bind() to store an **execution context**. To be clear, the execution context will have two important details.

1. A reference to the _cookout_ object to make sure we use the correct object
2. The number of minutes of cooking

This represents our existing knowledge about how to cook the different types of meat. In each case, we are storing the object and the number of minutes, so we can quickly handle the requests from all the party attendees.

Each variable — cookBurger, cookChicken, and cookSteak — is a new function that can be executed at any time with one more argument: the person’s name. So here are three people and their food requests:

1. Jack wants a burger
2. Jill wants steak
3. David wants chicken

By using our new functions, we can quickly take these requests without rewriting the grill method. Each of the examples below takes the final argument that is needed for the function to execute in the context of the cookout object.

![Image](https://cdn-media-1.freecodecamp.org/images/0*v7q9FTcaIthuVPqT.)

Imagine if you were not able to use the bind method here! It would be kind of like you were cooking burgers, chicken, and steak for the first time when the party started. You would be feeding in three arguments to a general grill() method, with no previous planning.

Instead, we use **partial function application** to show that we know how to cook each type of meat. We just need to hear what each individual guest wants to eat. This split represents your actual cooking experience.

### An Introduction To The Call Method

Here’s another scenario. Let’s say that when you and your partner cook a fancy dinner, you usually like to make some sort of fish and wine. As you can see from the first code snippet, you usually like to cook the fish in the oven.

But, you decide that one night, you would like to make steak instead. You are going to need to use the grill to make that steak, obviously.

![Image](https://cdn-media-1.freecodecamp.org/images/0*iXscRKRPeC-xTKBj.)

Here’s the issue: your grill() **method** is within the context of the cookout **object**! But now, you want to use those cooking skills within the fancyDinner object. Remember, **you don’t want to rewrite the grill method —** that will make your code harder to maintain.

Instead, you can use JavaScript’s call() method to call the grill method within the context of the _fancyDinner_ object. By using this new context, you will not need to rewrite it. Here is the full code before we get into the details.

![Image](https://cdn-media-1.freecodecamp.org/images/0*RF3pUlTfHzWhEA_X.)

So, our default drink for cookouts is soda, and the default drink for fancy dinners is wine. Now, we just need to add the unusual part as an **argument** in the call() method — “steak.” Here is the difference between using the method normally, and using call().

![Image](https://cdn-media-1.freecodecamp.org/images/0*oebh09RPKpZeIJB-.)

The first example should be pretty straightforward: it is all in the context of the cookout object. But in the second example, the first argument changed the context of _this_ to the _fancyDinner_ object!

When you get to the console.log statement within the grill() method, you can see that it references a single argument, _meal,_ as well as _this.drink._

When you use fancyDinner as the first argument of the call method, that sets the context to the fancyDinner object. Now, you are able to use those grilling skills in another context.

### An Introduction To the Apply Method

The apply() method is very similar to call(), except for one important difference. It can accept an array of arguments, instead of declaring individual parameters. That means that you can create a **variadic function** — that is, a function with any number of arguments. For that reason, it can only accept two parameters: the context, and an array of arguments.

Let’s return to our original birthday party example. You are holding a cookout for your son or daughter’s 10th birthday party. 12 kids replied and said they were going, but you do not know how many will actually show up. So, you need to be prepared to grill for an unknown number of people.

However, unlike bind(), functions that are called with apply() will be invoked immediately.

So, we need to create a function that can handle an array of an unknown number of meal orders, and return the full list of food that you will need to put on the grill. We can retain the organizational structure of the array, which helps give us the order that the requests came in.

There are a couple important things to note here. First of all, notice that the grill method does not have any parameters. This is different than in the past! To resolve this, we use the arguments object in line 4. The [arguments object in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) gives us an array-like object full of the arguments of the function.

To convert it to an actual array, we must use the slice() method from the array prototype. This is another handy application of the call() method, since the slice() method is not native to objects.

Finally, we must invoke the function using apply() in order to access the array in the mealOrders property. Here is how to do that.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5IRJN6HVTnIPtWYU.)

We still must use _cookout_ as the first argument, because just like call(), we must declare the execution context. Then, we can feed in the array from the mealOrders property.

This allows us to use an indefinite number of elements within the grill() method since we can pass in an array as the second argument.

### Get The Latest Tutorials

Did you enjoy this tutorial? Give it a clap so others can find it too. Or, sign up to get my latest visualized tutorials from the [CodeAnalogies blog](http://codeanalogies.com) here:

