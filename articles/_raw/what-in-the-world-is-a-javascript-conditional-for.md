---
title: What in the world is a JavaScript conditional?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-14T12:25:00.000Z'
originalURL: https://freecodecamp.org/news/what-in-the-world-is-a-javascript-conditional-for
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/scott-webb-GQD3Av_9A88-unsplash.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: Conditionals
  slug: conditionals
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Syk Houdeib

  This article is a beginner''s introduction to JavaScript conditionals. It covers
  why we need them, and how they fit into the front-end context. And why you will
  end up using them regularly.

  Introduction

  I came into development from a no...'
---

By Syk Houdeib

This article is a beginner's introduction to JavaScript conditionals. It covers why we need them, and how they fit into the front-end context. And why you will end up using them regularly.

## Introduction

I came into development from a non-traditional path. One thing was always particularly hard – to be able to go beyond the syntax of a new concept and place it in a context that made sense.

Conditionals are a little more intuitive than other concepts, but I want to show you the big picture. In this article, I'll explain why we need conditionals and how we can use them as front-end developers.

With the help of a beginner-friendly practical example, you'll see how you can use conditionals to process data in different ways and why they're a fundamental tool in development. Feel free to follow along while reading through this article.

The only prerequisite is a basic understanding of arrays and loops. I've covered those in two previous articles: 

**Arrays**: [https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-array/)

**Loops**: [https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for/) 

### The setup

Let’s imagine that we are working on an online platform that allows us to do our grocery shopping from a website. That's a real-world application of the things we want to talk about here.

Take a look at [Lola Market](https://lolamarket.com/tienda), which is where I work, for an example of what this would look like.

In the example we set up in the previous articles, we took a bunch of products (mushrooms, steak, fish, aubergines, and lentils) and organised them inside an array. We then stored that array as a variable and used a `forEach` loop to iterate over the list.

We are assuming that this list of products is now displayed on our website. Our task is to add a "(v)" next to vegetarian items on this list. This is just the kind of thing we regularly do on the front end.

## Conditionals

Conditionals are essential building blocks of programming. They are a way to do something only **if** certain **conditions** are met. The simplest and most common conditional in JavaScript is the `if` statement. Take a look at an example:



```js
if (product === 'steak') {
    // do stuff
}
```

Let’s start by translating this to English: “If the variable called `product` is exactly the string of characters 'steak' then execute the code within.”

Here’s a closer look

* `if`: This is the conditional.
* `(product === ‘steak’)`: This is our condition. There are a lot of ways you can construct conditions. We don’t need to worry about this yet. For now, bear in mind that whatever we put here will always be evaluated to either `true` or `false`.
* `// do stuff`: The statement. This is where the code we want to run goes. It will be executed **only** if the result of the evaluation of the condition is `true`. Otherwise, it will be ignored.

This bit of code will work on its own just fine, but we can have much more detailed control by using its friends  `else if` and `else`. `else if` adds another condition to check and executes another separate block of code, while `else` becomes the default action to take if none of the conditions are met.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-214.png)
_Photo by [Unsplash](https://unsplash.com/@jckbck?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Jakub Dziubak</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### Vegetarian Friendly

Let’s focus back on our original objective, which is to log a “(v)” next to the name of vegetarian items. This is a prime example of when we need to use a conditional. We want code that, **if** the `product` in the array **is** vegetarian, to print its name and add to it the “(v)”. And if it’s not vegetarian, to only print the name of the `product`.

First, we need to identify vegetarian items. Normally this information will be included with the data we requested from our database. But since we are using a simplified example, we will do it manually. We know that steak and fish are not vegetarian.

Notice, the condition I’m testing is if a product **is not** vegetarian. This is only because there are more vegetarian products on this list and I want the condition to be simple and the conditional to do the least amount of work. I could have just as easily tested for vegetarian items instead.

There are often many conditions that can be used to achieve the same goal. Writing good conditions that are efficient and readable is a useful skill that comes with practice.

So let’s write the condition that separates vegetarian from non-vegetarian.

```js
if (product === 'steak' || product === 'fish') {
    console.log(product)
} else {
    console.log(product + '(v)')
}
```

Following on from the example in my previous articles (linked above) we want to place the conditional inside the loop. The loop gives us each product in the list to process individually. This conditional block is the code that we are executing for each product in our array of products now.

Refresh the browser to start with a fresh console, then enter the following:

* The variable `product` storing our array of products.
* The `forEach` loop iterating over the array.
* And our conditional block inside.

![The dev tools console with our full code now using the conditional inside of the loop](https://www.freecodecamp.org/news/content/images/2019/09/conditional.PNG)
_The conditional block running inside of a loop_

### Execution

If we read the conditional code in **plain English** it says: “**If** the currently selected `product` **is** exactly ‘steak’ **or** ‘fish’ then log `product` to the console. Otherwise, in all other cases log `product` to the console but also add a string “(v)” to the end of it.”

Quick note, the `===` operator checks that the left and right expressions are **exactly** the same. and the `||` operator means **or.** We have two conditions to check here (steak or fish)**.** If **either** of the two conditions is true it will execute the code within.

Hit enter to run the code and see the results.

![The result of executing the code in the console. It prints the vegetarian items with a (v) at the end](https://www.freecodecamp.org/news/content/images/2019/09/conditional-result.PNG)
_The result of the loop with the conditionals_

And there it is. Every time the loop runs, it checks the currently selected element `product` and goes through the conditionals.

* Is `product` exactly the string ‘steak’?
* No. Check the following condition.
* Is `product` exactly the string ‘fish’?
* No. This condition is not met, the code inside will not execute. Go to the default code specified in the `else` block.
* Print `product` and add `(v)` to it.
* This iteration is finished. Start the next iteration.

If it finds ‘steak’ or ‘fish’ it will execute the code within that condition logging the `product` name without the "(v)". Then the loop finishes that iteration and starts the next, and so on. This process repeats for each element in the array until it’s all completed and the loop has logged the correct message for each one.

## Conclusion

To recap, a **conditional statement** sets certain **conditions.** When met (which means when the condition evaluates to `true`) the code specified inside the conditional block **executes**. Otherwise, it is ignored and not executed.

In our example, we have only logged messages to the console. But we can use the same idea to manipulate the DOM to display and modify content on a website.

Here are a few things you will need to further expand your knowledge and understand these concepts more in-depth:

* **Conditionals:** The `if` statement is one of the most commonly-used conditionals. But you will need to learn about others like the `while` statement, the `switch` statement, or the very useful **ternary operator**.
* **Conditions:** Understand how to create conditions and how they are evaluated. For that, you need to become familiar with the concepts of “**truthy**” and “**falsy**”. This is when values that are not explicitly `true` or `false` are evaluated as such.  For example, a string like `'mushrooms'` is considered true whereas an empty string `''` is always considered false.
* **Logical operators and comparison operators:** We saw those in our conditions. Logical operators like “_and”_ and “_or”_, written `&&` and `||`. Comparison operators like _“equals”_ and _“greater than”_, written `===` and `>`. These are simple concepts that are the bread and butter of writing code.

### Closure

Thanks for reading. I hope you found this useful. And if you enjoyed it, sharing it around would be greatly appreciated. If you have any questions or comments I’m on [Twitter](https://twitter.com/Syknapse) [@Syknapse](https://twitter.com/Syknapse) and I would love to hear from you.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-157.png)
_Photo by [Claudia](https://twitter.com/__Santaella)_

My name is Syk and I’m a front-end developer at [Lola Market](https://twitter.com/Tech_LolaMarket) in Madrid. I career-changed into web dev from an unrelated field, so I try to create content for those on a similar journey. My DMs are always open for aspiring web developers in need of some support. You can also read about my transformation in [this article](https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/).

  

