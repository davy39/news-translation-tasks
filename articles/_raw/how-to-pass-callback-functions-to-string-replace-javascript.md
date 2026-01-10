---
title: How to Pass Callback Functions to String.replace() in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-01T20:14:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-pass-callback-functions-to-string-replace-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-pawe--l-1121782.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Dillion Megida\nDid you know that the string .replace() method accepts\
  \ a callback function? I just discovered it today and thought I'd share. \nWhat\
  \ do you need this function for? Why does it exist? I'll answer all these questions\
  \ as you go through ..."
---

By Dillion Megida

Did you know that the string `.replace()` method accepts a callback function? I just discovered it today and thought I'd share. 

What do you need this function for? Why does it exist? I'll answer all these questions as you go through this article.

## The `replace()` Method

The `replace()` string method replaces text characters in a string. It takes two arguments: the string to be replaced, and the value it should be replaced with.

With this method, you can replace string characters (like "hello") or [characters that match a RegEx pattern](https://www.freecodecamp.org/news/javascript-string-replace-example-with-regex/) (like `/hi/`).

Here's the syntax of this method:

```js
String.replace(string/pattern, replacer)
```

Here are some examples showing how to use this method:

```js
const sentence = "Hi my name is Dillion"

const replaced1 = sentence.replace("Dillion", "JavaScript")
console.log(replaced1)
// "Hi my name is JavaScript"

const replaced2 = sentence.replace(/\s/g, "-")
console.log(replaced2)
// "Hi-my-name-is-Dillion"
```

But, the `replacer` argument can also be a function.

## Why would you need to use a function as the replacer method?

The reason is that sometimes, you want to do something with those characters that match the specified pattern.

Here's the syntax:

```js
String.replace(/pattern/, function(matched){
    // do something with matched and return
    // the replace value
})
```

If you're using a literal string pattern like "Dillion", you do not need the callback function because you already know that it's only "Dillion" you're matching through the sentence.

But with RegEx patterns, it can match multiple things. Here's an example:

```js
const sentence = "I am a good guy and you too"
const replaced = sentence.replace(/g\S*/g, "😂")

console.log(replaced)
// I am a 😂 😂 and you too
```

The regex pattern matches all words that start with "g" and two words match; "good" and "guy". In this case, if we want to do something with the matched value, we would need the callback.

Here's another example:

```js
const sentence = "I am a good guy and you too"
const replaced = sentence.replace(/g\S*/g, function(matched){
    console.log("matched", matched)
    return "😂"
})

console.log(replaced)
// matched good
// matched guy
// I am a 😂 😂 and you too
```

What are the examples of things we can do with matched values? There are so many scenarios, but I'll use the one use case that led me to discover this.

## How to find and replace URLs in a text with RegEx

On platforms like WhatsApp and Twitter, you'll discover that when you make a post or message with a link, the link is colored differently from other text and behaves like a link. Then when it's clicked, it navigates the user to a separate page.

How do they achieve this? The idea is to replace the links in the text with an element that has some styles to it and also works as a link.

Here's how I did this with JavaScript:

```js
const text = "My website is https://dillionmegida.com and I write on http://freecodecamp.org/"

const regex = /https?:\/\/\S*/gi

const modifiedText = text.replace(regex, (url) => {
    return `<a class="text--link" href="${url}">${url}</a>`
})

console.log(modifiedText)
// My website is <a class="text--link" href="https://dillionmegida.com">https://dillionmegida.com</a> and I write on <a class="text--link" href="http://freecodecamp.org/">http://freecodecamp.org/</a>
```

The regex matches patterns with "https://..." (with the s optional). Using the callback, I can get the `url` that matches the regex and use it to create an anchor tag string with a "text--link" class.

With this returned string, I can inject it into the DOM. In my case, I was using React, so I used [dangerouslySetInnerHTML](https://reactjs.org/docs/dom-elements.html#dangerouslysetinnerhtml) to inject it into a paragraph. I can specify a color for the "text--link" class in my stylesheet.

## Conclusion

We learn new things every day, and I hope you've learned something in JavaScript today – the callback function in `String.replace()`. 

Also, in this article, I showed a good use case for taking advantage of this function.

Kindly share this if you find it helpful.


