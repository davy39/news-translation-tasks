---
title: JavaScript setTimeout Tutorial – How to Use the JS Equivalent of sleep, wait,
  delay, and pause
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-03T02:08:26.000Z'
originalURL: https://freecodecamp.org/news/javascript-sleep-wait-delay
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b4c740569d1a4ca2aee.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Mehul Mohan\nJavaScript is the language of the web. And it hasn't been\
  \ the same since ES5 was released. More and more ideas and features are being ported\
  \ from different languages and being integrated in JavaScript. \nOne of those features\
  \ are Promis..."
---

By Mehul Mohan

JavaScript is the language of the web. And it hasn't been the same since ES5 was released. More and more ideas and features are being ported from different languages and being integrated in JavaScript. 

One of those features are Promises, which are probably the most widely used feature in JavaScript after ES5 was released.

But one of the things which JavaScript misses is a way to "pause" execution for a while and resume it later. In this post, I'll discuss how you can achieve that and what it really means to "pause" or "sleep" in JavaScript. 

_Spoiler: JavaScript never really "pauses"._

## TL;DR

Here's the copy-pasta code which does the job:

```js
/**
 * 
 * @param duration Enter duration in seconds
 */
function sleep(duration) {
	return new Promise(resolve => {
		setTimeout(() => {
			resolve()
		}, duration * 1000)
	})
}
```

But what is really happening here?

## setTimeout and fake Promises

Let's see a quick example using the above snippet (we'll discuss what's happening in it later):

```js
async function performBatchActions() {
	// perform an API call
	await performAPIRequest()

	// sleep for 5 seconds
	await sleep(5)

	// perform an API call again
	await performAPIRequest()
}
```

This function `performBatchActions`, when called, simply executes the `performAPIRequest` function, waits **about 5 seconds**, and then calls the same function again. Note how I wrote **about 5 seconds**, and not 5 seconds.

A strong note to put out there: the above code does not guarantee a perfect sleep. It means that if you specify duration to be, say, 1 second, JavaScript **does not guarantee** that it will start running the code after the sleep exactly after 1 second. 

Why not? you may ask. Unfortunately, it's because timers work in JavaScript, and in general, event loops. However, JavaScript absolutely guarantees that the piece of code after the sleep will never execute **before** the specified time. 

So we don't really have a full indeterminate situation, just a partial one. And in most cases it's within a margin of a few milliseconds only.

## JavaScript is single threaded

A single thread means that a JavaScript process cannot really go out of the way at all. It has to do all the things - from event listeners, to HTTP callbacks, on the same main thread. And when one thing is executing, another one cannot execute. 

Consider a webpage in which you have multiple buttons and you run the code above to simulate a sleep for, let's say, 10 seconds. What do you expect will happen?

Nothing at all. Your webpage will work just fine, your buttons will be responsive, and once the 10 second sleep is done, the code next to it will execute. So it's evident that JavaScript does not really block the whole main thread because if it did that, your webpage would have frozen and the buttons would have become non-clickable. 

So how did JavaScript actually pause a single thread, without ever really pausing it?

## Meet the Event Loop

Unlike other languages, JavaScript doesn't just keep on executing code in a linear fashion from top to bottom. It is an asynchronous event-driven language with tons of magic in the form of the event loop. 

An event loop splits your code in synchronous and certain events - like timers and HTTP requests. Precisely speaking, there are two queues - a task queue and microtask queue. 

Whenever you run JS, and there's an asynchronous thing (like a mouseclick event, or a promise), JavaScript throws it in the task queue (or microtask queue) and keeps executing. When it completes a "single tick", it checks if the task queues and microtask queue have some work for it. If yes, then it'll execute the callback/perform an action.

I would really recommend anyone interested in the detailed workings of event loops to watch this video:

%[https://www.youtube.com/watch?v=8aGhZQkoFbQ]

## Conclusion

You came here for a simple sleep instruction in JavaScript, and ended up learning about one of the core things in JavaScript - event loops! Amazing, isn't it? 

Well, if you liked the article, checkout [codedamn](https://codedamn.com) - a platform I've been building for developers and learners like you. Also, let's connect on social media - [twitter](https://twitter.com/mehulmpt) and [Instagram](https://instagram.com/mehulmpt). See you soon!

Peace

