---
title: JavaScript Console.log() Example – How to Print to the Console in JS
subtitle: ''
author: Jesse Hall
co_authors: []
series: null
date: '2020-09-09T21:01:11.000Z'
originalURL: https://freecodecamp.org/news/javascript-console-log-example-how-to-print-to-the-console-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/fCC_-Console.log.png
tags:
- name: console
  slug: console
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Logging messages to the console is a very basic way to diagnose and troubleshoot
  minor issues in your code.

  But, did you know that there is more to console than just log? In this article,
  I''ll show you how to print to the console in JS, as well as al...'
---

Logging messages to the console is a very basic way to diagnose and troubleshoot minor issues in your code.

But, did you know that there is more to `console` than just `log`? In this article, I'll show you how to print to the console in JS, as well as all of the things you didn't know `console` could do.

## Firefox Multi-line Editor Console

If you've never used the multi-line editor mode in Firefox, you should give it a try right now!

Just open the console, `Ctrl+Shift+K` or `F12`, and in the top right you will see a button that says "Switch to multi-line editor mode". Alternatively, you can press `Ctrl+B`.

This gives you a multi-line code editor right inside Firefox.

## console.log

Let's start with a very basic log example.

```js
let x = 1
console.log(x)
```

Type that into the Firefox console and run the code. You can click the "Run" button or press `Ctrl+Enter`.

In this example, we should see "1" in the console. Pretty straightforward, right?

## Multiple Values

Did you know that you can include multiple values? Add a string to the beginning to easily identify what it is you are logging.

```js
let x = 1
console.log("x:", x)
```

But what if we have multiple values that we want to log?

```js
let x = 1
let y = 2
let z = 3
```

Instead of typing `console.log()` three times we can include them all. And we can add a string before each of them if we wanted, too.

```js
let x = 1
let y = 2
let z = 3
console.log("x:", x, "y:", y, "z:", z)
```

But that's too much work. Just wrap them with curly braces! Now you get an object with the named values.

```js
let x = 1
let y = 2
let z = 3
console.log( {x, y, z} )
```

![Console Output](https://www.freecodecamp.org/news/content/images/2020/09/image-34.png align="left")

*Console Output*

You can do the same thing with an object.

```js
let user = {
  name: 'Jesse',
  contact: {
    email: 'codestackr@gmail.com'
  }
}
console.log(user)
console.log({user})
```

The first log will print the properties within the user object. The second will identify the object as "user" and print the properties within it.

If you are logging many things to the console, this can help you to identify each log.

## Variables within the log

Did you know that you can use portions of your log as variables?

```js
console.log("%s is %d years old.", "John", 29)
```

In this example, `%s` refers to a string option included after the initial value. This would refer to "John".

The `%d` refers to a digit option included after the initial value. This would refer to 29.

The output of this statement would be: "John is 29 years old.".

## Variations of logs

There are a few variations of logs. There is the most widely used `console.log()`. But there is also:

```js
console.log('Console Log')
console.info('Console Info')
console.debug('Console Debug')
console.warn('Console Warn')
console.error('Console Error')
```

These variations add styling to our logs in the console. For instance, the `warn` will be colored yellow, and the `error` will be colored red.

Note: The styles vary from browser to browser.

## Optional Logs

We can print messages to the console conditionally with `console.assert()`.

```js
let isItWorking = false
console.assert(isItWorking, "this is the reason why")
```

If the first argument is false, then the message will be logged.

If we were to change `isItWorking` to `true`, then the message will not be logged.

## Counting

Did you know that you can count with console?

```js
for(i=0; i<10; i++){
  console.count()
}
```

Each iteration of this loop will print a count to the console. You will see "default: 1, default: 2", and so on until it reaches 10.

If you run this same loop again you will see that the count picks up where it left off; 11 - 20.

To reset the counter we can use `console.countReset()`.

And, if you want to name the counter to something other than "default", you can!

```js
for(i=0; i<10; i++){
  console.count('Counter 1')
}
console.countReset('Counter 1')
```

Now that we have added a label, you will see "Counter 1, Counter 2", and so on.

And to reset this counter, we have to pass the name into `countReset`. This way you can have several counters running at the same time and only reset specific ones.

## Track Time

Besides counting, you can also time something like a stopwatch.

To start a timer we can use `console.time()`. This will not do anything by itself. So, in this example, we will use `setTimeout()` to emulate code running. Then, within the timeout, we will stop our timer using `console.timeEnd()`.

```js
console.time()
setTimeout(() => {
  console.timeEnd()
}, 5000)
```

As you would expect, after 5 seconds, we will have a timer end log of 5 seconds.

We can also log the current time of our timer while it's running, without stopping it. We do this by using `console.timeLog()`.

```js
console.time()

setTimeout(() => {
  console.timeEnd()
}, 5000)

setTimeout(() => {
  console.timeLog()
}, 2000)
```

In this example, we will get our 2 second `timeLog` first, then our 5 second `timeEnd`.

Just the same as the counter, we can label timers and have multiple running at the same time.

## Groups

Another thing that you can do with `log` is group them. ?

We start a group by using `console.group()`. And we end a group with `console.groupEnd()`.

```js
console.log('I am not in a group')

console.group()
console.log('I am in a group')
console.log('I am also in a group')
console.groupEnd()

console.log('I am not in a group')
```

This group of logs will be collapsible. This makes it easy to identify sets of logs.

By default, the group is not collapsed. You can set it to collapsed by using `console.groupCollapsed()` in place of `console.group()`.

Labels can also be passed into the `group()` to better identify them.

## Stack Trace

You can also do a stack trace with `console`. Just add it into a function.

```js
function one() {
  two()
}
function two() {
  three()
}
function three() {
  console.trace()
}
one()
```

In this example, we have very simple functions that just call each other. Then, in the last function, we call `console.trace()`.

![Console Output](https://www.freecodecamp.org/news/content/images/2020/09/image-35.png align="left")

*Console Output*

## Tables

Here's one of the most mind-blowing uses for console: `console.table()`.

So let's set up some data to log:

```js
let devices = [
  {
    name: 'iPhone',
    brand: 'Apple'
  },
  {
    name: 'Galaxy',
    brand: 'Samsung'
  }
]
```

Now we'll log this data using `console.table(devices)`.

![Console Output](https://www.freecodecamp.org/news/content/images/2020/09/image-36.png align="left")

*Console Output*

But wait – it gets better!

If we only want the brands, just `console.table(devices, ['brand'])`!

![Console Output](https://www.freecodecamp.org/news/content/images/2020/09/image-37.png align="left")

*Console Output*

How about a more complex example? In this example, we'll use jsonplaceholder.

```js
async function getUsers() {
  let response = await fetch('https://jsonplaceholder.typicode.com/users')
  let data = await response.json()
 
  console.table(data, ['name', 'email'])
}

getUsers()
```

Here we are just printing the "name" and "email". If you `console.log` all of the data, you will see that there are many more properties for each user.

## Style ?

Did you know that you can use CSS properties to style your logs?

To do this, we use `%c` to specify that we have styles to add. The styles get passed into the second argument of the `log`.

```js
console.log("%c This is yellow text on a blue background.", "color:yellow; background-color:blue")
```

You can use this to make your logs stand out.

## Clear

If you are trying to troubleshoot an issue using logs, you may be refreshing a lot and your console may get cluttered.

Just add `console.clear()` to the top of your code and you'll have a fresh console every time you refresh. ?

Just don't add it to the bottom of your code, lol.

## Thanks for Reading!

If you want to revisit the concepts in this article via video, you can check out this [video-version I made here](https://youtu.be/_-bHhEGcDiQ).

%[https://youtu.be/_-bHhEGcDiQ] 

![Jesse Hall (codeSTACKr)](https://www.freecodecamp.org/news/content/images/2020/06/footer-banner-1.png align="left")

I'm Jesse from Texas. Check out my other content and let me know how I can help you on your journey to becoming a web developer.

* [Subscribe To My YouTube](https://youtube.com/codeSTACKr)
    
* Say Hello! [Instagram](https://instagram.com/codeSTACKr) | [Twitter](https://twitter.com/codeSTACKr)
    
* [Sign Up For My Newsletter](https://codestackr.com/)
