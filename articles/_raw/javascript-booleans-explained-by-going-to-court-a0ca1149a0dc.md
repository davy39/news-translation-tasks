---
title: JavaScript booleans explained by going to court
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T04:04:31.000Z'
originalURL: https://freecodecamp.org/news/javascript-booleans-explained-by-going-to-court-a0ca1149a0dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-ZzuerbatF4F0uu9qCvHaA.png
tags:
- name: Boolean
  slug: boolean
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever watched a TV show about court (or been to court), then you can
  understand booleans in JavaScript.

  You might think that booleans are the most straightforward topic that you could
  ask for in JavaScript.

  After all, si...'
---

By Kevin Kononenko

If you have ever watched a TV show about court (or been to court), then you can understand booleans in JavaScript.

You might think that booleans are the most straightforward topic that you could ask for in JavaScript.

After all, since a variable can be any of the following:

* number
* string
* array
* object
* boolean

…boolean seems to be the easiest.

```
let bool = true;
```

```
let bool= false;
```

The only two options for a boolean are `true` or `false`. And they are used in `if()` statements to decide which statement should be executed.

```
if(true){
```

```
}
```

```
else{
```

```
// if value is false, this block runs
```

```
}
```

But here’s the thing. Within `if()` statements, other variable values can **evaluate** to true or false. In other words, once the value is used in the `if()` statement, JavaScript will evaluate whether it is `true` or `false`.

For example, do you know if the value 0 is `true` or `false`?

This is not a philosophy question. JavaScript has an answer.

Anyways, this happens because JavaScript is a **weakly typed** language. This means that in the context of an `if()` statement, it will convert other variable values to `true` or `false` in order to run the code. This is known as determining the “truthiness” of a value.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JYzIah834O2zHY4K)

Many other languages are **strongly typed**, so they will not convert values into true or false.

This may seem a little crazy, but it is actually pretty similar to the way that a judge in the United States determines whether an accused person is innocent or guilty. So, I can explain the way that “truthiness” and `true`/`false` works in JavaScript through legal rules that you have seen in “Law and Order” or any other court-based procedural dramas on TV.

For the purposes of this tutorial, imagine that you are a district attorney that is trying to prosecute a person who is accused of stealing a car.

And, you will need to understand the [basics of variables in JavaScript](https://blog.codeanalogies.com/2017/12/20/a-visual-guide-to-understanding-the-sign-in-javascript/) to use this tutorial. Let’s get into it!

### What is “truthiness” in JavaScript?

In the United States, the criminal law system states that an accused person is “innocent until proven guilty”. That means that the burden lies on the prosecutor (you, in this case) to provide enough evidence to disprove the default assumption that the accused person is innocent.

In fact, the standard of evidence is “[beyond a reasonable doubt.](https://en.wikipedia.org/wiki/Reasonable_doubt)” This is consistent across many countries in the world.

When we use `if()` statements, we are not always going to be able to plug in a variable with a value of `true` or `false`. Many times, we must plug in a statement that will be evaluated by JavaScript **as** `true` or `false`.

This is similar to the legal system! Although it is **possible** that there will be one piece of evidence that makes the “guilty” or “not guilty” verdict obvious, it is also likely that a judge or jury will need to evaluate multiple pieces of evidence and make a decision.

Let’s start with the basics. A `true` statement is evidence that will lead to the conviction of the accused. A `false` statement is evidence that will let them walk free. Let’s create a variable called `evidence` and set it to `true`.

```
let evidence = true;
```

```
if (evidence){
```

```
  convict();
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

`convict()` and `release()` are made-up functions. In this case, since evidence is set to `true`, the judge would convict the car thief. Here’s an interactive diagram of this scenario.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hQ4EcsTZPmWWNOXLvxRThQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zNtmdN3AjQ4Tpcl_Xa_oKA.jpeg)

The robber kinda looks like Edward Norton from “The Italian Job”, eh?

![Image](https://cdn-media-1.freecodecamp.org/images/0*FRlRPnEU3_Pu7fYK)

Anyways, in real life, it is never this straightforward. Let’s say that you have a killer piece of evidence — fingerprints from the car door. You present that to the judge.

```
let evidence = "fingerprints";
```

```
if (evidence){
```

```
  convict();
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

Aha! We only changed the first line, where we declared the variable evidence. And it is now a string rather than a boolean. But guess what? Due to **type coercion**, JavaScript will evaluate the string as `true`. Since there is no condition within the `if()` statement, all strings are `true`. We would run the `convict()` function!

![Image](https://cdn-media-1.freecodecamp.org/images/0*3f8jEtYDOMaiVPeX)

### Examples of truthiness

Let’s imagine that instead, the evidence variable is set to `0`. We run the same `if()` statement again.

```
let evidence = 0;
```

```
if (evidence){
```

```
  convict();
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

In this case, the statement would actually evaluate to `false`, and our accused car thief would be released.

![Image](https://cdn-media-1.freecodecamp.org/images/0*x6feidPaPL5Uga82)

This is why it is called “truthiness” — because JavaScript is evaluating whether the condition is `true` or `false`.

Since the variable is set to `0`, it’s kind of like if you were asked to present evidence against the thief, and you said… nothing.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vDx4QLx1Hfwa6e07)

Obviously the judge is going to determine you don’t have enough evidence, and set the person free! The same would happen if evidence was set to an empty string ````. You still aren’t offering anything, so your statement is evaluated as `false`_._

```
let evidence = '';
```

Here’s one more test to see if you understand `true` versus `false`. What if the variable has not yet been initialized to a value?

```
let evidence;
```

```
if (evidence){
```

```
  convict();
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

This is a pretty common one, because web developers will have another statement in their script that gives a value to the `evidence` variable. And, just like the two examples above, JavaScript will evaluate this variable as `false` if it does not have any value.

This is a great example of “innocent until proven guilty”. The variable has not yet been assigned a value, so there is no way JavaScript could call it `true`.

### Using DOM Elements in if() statements

So we have covered values of variables that are “falsy”. But what about elements from the DOM?

**Note**: if you need a refresher, check out my [guide to DOM elements here](https://blog.codeanalogies.com/2018/01/06/traversing-the-dom-visual-explanation/).

In other words, what happens when we use a DOM element to determine which branch of an `if/else` statement to run? If you use jQuery or React (or Angular, and so forth), you probably manipulate the DOM in order to create a more dynamic interface.

In our courtroom example, let’s say that you swear that the lockpick the thief used is located in a trashcan near the crime scene. In HTML terms, you are saying that there is a div with ID `lockpick` somewhere in the DOM. How might the judge validate your claim?

```
if(document.getElementById('lockpick')){
```

```
  convict()
```

```
}
```

```
else{
```

```
  release()
```

```
}
```

Here’s an interactive image of that scenario.

![Image](https://cdn-media-1.freecodecamp.org/images/1*p37rdMZPQYElpR9ZZCITcQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*jcorLVV6rRXqiHk_XnBKdQ.jpeg)

“Truthiness” here means that JavaScript will inspect the DOM, and only return `true` if it finds an element with ID `lockpick`. It’s kind of like a judge determining if the evidence that you present is real and authentic. In this case, it is, so the first block of code will run, and the person will be convicted.

This is super useful! We have now extended the concept of `true` so that it includes whether an element exists or not. This logic also applies to objects and arrays. You can check whether an element with a specific class exists, whether a certain element has children, you get the idea.

### More variations of if() statements

When you bring an accused person to court, they may still be convicted of a lesser crime. If you don’t have enough evidence for the main charge, they can still be convicted of a lower charges.

In the example of car theft, there is a breaking and entering crime, and then theft is possible if the accused person has already broken into the car.

We can combine `if()`, `else if()`, and `else()` to model these options. Let’s say the accused person **did** break into the car, but did not take anything. We could model the options like this:

```
let breaking = true;
```

```
let theft = false;
```

```
if (breaking && theft){
```

```
  convict('felony');
```

```
}
```

```
else if(breaking){
```

```
  convict ('misdemeanor');
```

```
}
```

```
else{
```

```
  release();
```

```
}
```

There are now three scenarios. If the first condition is satisfied, that code block will run. That means that the thief would be convicted of a felony. But, if only the value of the variable `breaking` can be evaluated as `true`, the person will still be convicted of a misdemeanor.

The judge is saying, “You need to show me evidence of both breaking and entering **and** theft if I am going to convict this person of a felony.”

![Image](https://cdn-media-1.freecodecamp.org/images/0*09AccMKv051RIVLG)

The first `if()` statement will evaluate `true && false`, which will be reduced to `false` since `false` takes precedence over `true` (remember, innocent until proven guilty).

This would still work if we used values that were “truthy” or “falsy”. Each one would be evaluated to `true` or `false` within the `if()` statement, and then JavaScript would decide which block to execute.

### Get more visual tutorials

Did you enjoy this guide? Give it a “clap”, or sign up below to get my latest tutorials on web development topics.

