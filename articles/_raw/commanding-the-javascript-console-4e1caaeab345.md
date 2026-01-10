---
title: Commanding the Javascript console
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-20T21:02:13.000Z'
originalURL: https://freecodecamp.org/news/commanding-the-javascript-console-4e1caaeab345
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wUSjXYVzyV0nerQIIe8GCA.png
tags:
- name: debugging
  slug: debugging
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kyle Gill

  Useful tricks for debugging, formatting, and efficiency

  The console is one of the first tools developers learn about. The console is the
  tool developers use when debugging their own applications. The law of the instrument
  states that it’...'
---

By Kyle Gill

#### Useful tricks for debugging, formatting, and efficiency

The console is one of the first tools developers learn about. The console is the tool developers use when debugging their own applications. The [law of the instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument) states that it’s easy to develop overconfidence in a familiar tool.

> “I suppose it is tempting, if the only tool you have is a hammer, to treat everything as if it were a nail.” -Maslow

The same idea can be applied to the console. In an ecosystem where tools, keyboard shortcuts, and API’s flow like milk and honey in the promised land, it’s hard to justify picking up a new hammer when your old one works just fine. Trust me on this one though, those prong thingies on the back of your hammer [aren’t just for ripping out nails](https://www.familyhandyman.com/tools/hammers-aren-t-just-for-nails-101-ways-to-use-a-rip-hammer/view-all/).

What follows are some of the simplest tricks I’ve found for debugging in the console.

#### #1: Wrapping Arguments

If you wrap the argument passed into `console.log` in {}’s you’ll output the data you’re logging in object form. The object will have a nice name to tell you what it was that you were trying to output.

Rather than seeing a whole bunch of objects with similar fields like id and name in your console like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*FvyeehvzCpelNj-pKSHPcg.png)

You’ll get the name of the variable in front of the data being printed like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*HZ7WTogIsT071Ag1uK_6ag.gif)
_Down with ambiguity!_

#### #2: Copying Data to the Clipboard

You can copy data logged in the console to your computer’s clipboard. I find this useful when you want to manipulate an object in a REPL or pull out data you’re debugging.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yxRiSSUeqr7Z-HSK2iU_-Q.gif)

Right click next to the data you want to copy and select “Store as a global variable”. This will save the data as a variable in the console with a temporary name. (If it’s the first time you’re doing it in a console window it will be `temp1`.) Then you can use the `copy()` command putting in the name `temp1` as the argument. This copies the data stored to your clipboard which you can paste like you would anything else you copy.

It’s especially helpful when a database query won’t return data in a format that matches how your data is being manipulated on the frontend. You can show you how data is being mutated or transformed.

#### #3: Short Circuiting expressions

If you short circuit an expression with a `||` you can make refactoring code or adding in a debug statement a lot faster. This is particularly useful with one line fat arrow functions where you want to see what data you’re receiving as an argument.

```
// THISsomeFunction = data => (  <div>    <Component data={data} />  </div>)
```

```
// BECOMES...someFunction = data =&gt; console.log(data) || (  <div>    <Component data={data} />  </div>)
```

```
// RATHER THAN...someFunction = data =&gt; {  console.log(data)    return (    <div>      <Component data={data} />    </div>  )}
```

You skip out on wrapping the whole function in curly braces and adding a return. This feels like it’s not that big a deal until you’re optimizing performance and do it a thousand times trying to figure out what egregious React sin you’ve committed.

#### #4: Log, Error, Warn

In addition to `console.log()`, the console has several other functions to print data into the console in different predefined formats. Among these are:

* `console.log()`

![Image](https://cdn-media-1.freecodecamp.org/images/1*uWQAooSF_gUIYa1SDaRVgQ.png)

* `console.warn()`

![Image](https://cdn-media-1.freecodecamp.org/images/1*XNH6EhI8d-V0-Le7dP7gAA.png)

* `console.error()`

![Image](https://cdn-media-1.freecodecamp.org/images/1*jPEvpMtNVWWIu_EvyegIiw.png)

#### #5: Custom formatting for console output

You can do more than just implement the built-in formatting with `console.log`, `warn`, and `error`. You can play the role of artist where the console is your canvas!

Perhaps try printing a nice pill around output you want to emphasize:

![Image](https://cdn-media-1.freecodecamp.org/images/1*DOCtgY_O8f_1mAq3UzLtIQ.png)
_Required skills: HTML, CSS, and Quantum Computing Experience_

Here’s that snippet:

You can also store CSS to use as styles in a variable to apply to output. You can punk your coworkers with a splash of rainbow to trail everything you output. If you want humungous rainbows following everything, try this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*dDcJa9FRxivPU_-aP_3l5Q.png)
_Effective when venting frustration_

#### #6: Printing JSON as a Table

Unbeknownst to many, the console has a built-in method for printing tabular data in table format. This can be great for quickly perusing JSON data.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iX3XXABKkojWkFk-UbuF1g.gif)

#### #7: Easy Counting

The `console.count()` method can make keeping track of how many times you’ve hit a point in your code really simple. You no longer need to pepper your code in incrementing variables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9303rNoYjFIpTUS42OnWwQ.gif)

> Pro tip: you can replace “number” with a label from a variable and it will count how many times the count method with that label has been hit.

I’ve found this to be useful when trying to debug race conditions or unnecessary re-rendering in a React app.

#### #8: Using DOM Elements

You can select a DOM element in the Elements tab and then access it with `$0`. The browser will actually keep a history where `$0` represents the current selection. `$1` represents the previous selection. `$2` the second last selection and so on up to 5 elements.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q3EbqExsRdUy2y3VuJDGNg.gif)
_With a typing speed of approximately 15 words per minute_

You may ask yourself: when would I ever want to change the innerHTML of my app from the console? And the answer would be probably only when you want a really simple example GIF for a blog post. But this too has its use cases.

#### #9: The Debugger Statement

If you’ve ever added a console.log, gone into the browser tools and added a breakpoint, to see what’s happening when it gets to that code, free yourself with the `debugger` statement.

If you add `debugger` on a line in your Javascript the browser will stop and open up the debugging tools and pause execution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hv31lQMyiy6kVJ9teHQdnA.gif)
_Shortcut!_

Although it’s not a console feature, it’s a great thing to know. Logging information to the console isn’t as effective or efficient as the debugging tools built into browsers (like Chrome’s Sources tab or Firefox’s Debugger tab). To further improve your debugging, look into resources that dive into those tools.

However, the console remains a really quick and effective way to see application flow in apps where lots of different lifecycle methods and re-renders are firing and improving how you use them too will make you a better developer.

### Thanks for Reading!

If you have your own tips, please share! I’d love to hear from you here in the comments, on Twitter, or via email.

If you found what you read interesting or helpful, feel welcome to leave a clap or two, subscribe for future updates, or retweet/share this tweet: ?

