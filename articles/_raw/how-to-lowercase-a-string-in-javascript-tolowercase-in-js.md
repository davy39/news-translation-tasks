---
title: How to Lowercase a String in JavaScript – toLowerCase() in JS
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-10-17T15:51:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-lowercase-a-string-in-javascript-tolowercase-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-magda-ehlers-1337382.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Strings are a fundamental part of working with JavaScript. And the toLowerCase()
  method is one of the many integrated methods that you can use to work with strings.

  In this article, we''ll see how to make strings lowercase with the toLowerCase()
  metho...'
---

Strings are a fundamental part of working with JavaScript. And the `toLowerCase()` method is one of the many integrated methods that you can use to work with strings.

In this article, we'll see how to make strings lowercase with the `toLowerCase()` method in Python.

## **What is a** S**tring?**

A string is a data type that can contain many different characters. A string is written as a series of characters between single or double quotes.

```javascript
const exampleString = 'I am a String!'
console.log(exampleString); // I am a String!
```

## **What is a** M**ethod?**

A method is a function that you can use on a specific data type. Methods can either take or not take arguments.

## **How** D**oes the** `toLowerCase()` M**ethod** W**ork?**

The `toLowerCase()` method is a string method that returns a new string that's completely lowercase. If the original string has uppercase letters, in the new string these will be lowercase. Any lowercase letter, or any character that is not a letter, is not affected.

```javascript
console.log(exampleString.toLowerCase()); // i am a string!

console.log('FREECODECAMP'.toLowerCase()); // freecodecamp

```

## **What to** K**eep in** M**ind** W**hen** U**sing the** toLowerCase M**ethod**

The `toLowerCase()` method does a pretty straightforward thing: it creates a new string where all the uppercase letters are now lowercase. But there are a few things to keep in mind when using it. Let's take a look at them.

### **Strings are immutable**

Strings are an immutable data type, which means they can't be changed. The original string will stay unchanged after you use the `toLowerCase()` method.

In the examples above, the `toLowerCase()` method has acted on the `exampleString` but never changed it. Checking the value of `exampleString` still shows the original value:

```javascript
console.log(exampleString); // I am a string!

console.log(exampleString.toLowerCase()); // i am a string!

console.log(exampleString); // I am a string!

```

### **The** `toLowerCase()` **method returns a new string**

This means that the `toLowerCase()`  method returns a new string. You'll need to save it in a variable if you want to use it again in your code.

```javascript
const newString = exampleString.toLowerCase()

console.log(newString); // i am a string!
```

### **Strings are case sensitive**

Strings are case sensitive, so a lowercase string is different than an uppercase string.

```javascript
console.log('freecodecamp' === 'FREECODECAMP'); // false

```

This is useful when thinking about what the `toLowerCase()` method could be useful for. In the example you will see how this feature makes the `toLowerCase()` method useful and necessary when building a script or program that deals with strings.

## **`toLowerCase()`** M**ethod** E**xample** – H**ow to** C**heck if the** U**ser** I**nput** M**atches**

Let's write a small app that asks the user a question, gets the input, and gives feedback about the user's answer.

There are various ways to do that: you could use this in a web app, getting the value from an `input` element with `type="text"`. To keep it simple, in the example you will see the usage of the `prompt` JavaScript function.

The `prompt` function will display a browser message popup with an input field in which the user can write an answer:

```javascript
const answer = prompt("What color is the sun?")
if (answer === "yellow") {
  alert("Correct!")
} else {
  alert("That is not the correct color!")
}
```

This code asks the user a question, "What color is the sun?", and waits for an answer. Then it checks if the answer is "yellow", and if it is it prints "Correct!" If it isn't, it prints "That is not the correct color!".

But there is an issue with this code.

Running this code, you will have this question asked in the popup:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-69.png)

If you answer "Yellow", it says "That is not the correct color!"

Why does this happen?

Remember that strings are case sensitive. The script is checking if the user input the string `yellow` – `Yellow`, with a capital "Y", is a different string.

You can easily fix this by using the `toLowerCase()` method, and doing this small change to the code:

```javascript
const answer = prompt("What color is the sun?")
if (answer.toLowerCase() === "yellow") {
  alert("Correct!")
} else {
  alert("That is not the correct color!")
}
```

And now, if you try again...

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-70.png)

What changed? Writing `answer.toLowerCase()` you make sure that the checked string is completely lowercase before comparing it with the correct answer string "yellow". In this way it doesn't matter if the user writes "YELLOW" or "yELLOW" or "yellow" – it is all converted to lowercase.

Thanks for reading! Now you know how to use the `toLowerCase()` method in JavaScript.

