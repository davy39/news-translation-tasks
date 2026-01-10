---
title: What gets logged in the console when you’re mutating objects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T19:44:37.000Z'
originalURL: https://freecodecamp.org/news/mutating-objects-what-will-be-logged-in-the-console-ffb24e241e07
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PePMIr6hsZ70wtXX_mDCsw.png
tags:
- name: coding
  slug: coding
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Boris Sever

  A lot of developers are not using a debugger while developing. Instead they are
  relying on their old friend console.log().

  It is important to note that the console shows the object’s value which is evaluated
  at the time of the first ex...'
---

By Boris Sever

A lot of developers are not using a debugger while developing. Instead they are relying on their old friend `console.log()`.

It is important to note that the console shows the object’s value which is evaluated at the time of the **first expansion** in the console.

First, let me clarify what I mean by expansion. When we `console.log` an object (which covers arrays also), the object’s value is collapsed. For example:

`console.log( "users: ", [{name: "John"}]);`

The browser’s console will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*NOVGoKXu4ZAHsqA2Uvzx4g.png)

Then, when you click on the triangle, the object expands. At that exact time, the object’s value is evaluated and displayed.

Let's dive more into this and check out an example:

On line 1 we are initializing a new `users` variable, which is an array of objects.

On line 6 we are writing the value of the `users` variable to the console.

Next, we iterate through `users`, check if the user is valid, and depending on the return, we disable the user. For the sake of argument, let's assume the `validateUser()`returns `false` and code on line 10 is executed.

Even though `map` is creating a new array, changing the `user` object is also changing the `user` object in the `users` array. It changes because it has the same reference. (For a better explanation of what’s happening, check out [this article](https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0) ).

**The question is: what will be shown in the console which is called on line 6?**

When we open this example in Chrome and Firefox, the object is collapsed. Then upon expansion, we see the values:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zri_rWMD3yqBmrzCzw0UKQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*StVzIGl8SQnG1SBVNMBDMQ.png)

Enabled is set to `false`, even though the value was `true` at the time of the output. The reason behind this is that the object’s value is evaluated the first time when we click to expand the object (lazy read).

> _Note: Chrome will show an info icon which states: “Value below was evaluated just now.”_

Let’s now take a look at Safari:

![Image](https://cdn-media-1.freecodecamp.org/images/1*FsKGB4JmFTUCNXt6-HWckA.png)
_Safari ( version 11.0.3 )_

Hm, enabled is set to true. So we can see that there are some inconsistencies between browsers. Safari will try to expand the object automatically. If the object/array is too big, it will collapse and behave the same way as Chrome and Firefox.

One way to get around this is to use `JSON.stringify(),` e.g.   
`console.log("users", JSON.stringify(users, null, 2));`

which will produce the following output to the console:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vpDy5W8XC9d9egowdnlrxw.png)

Unfortunately, with this approach you cannot expand/collapse an object. The value won’t be mutated.

I’m a big fan of the functional programming paradigm and immutable variables. To modify the object, you create a clone which is then modified. In that case you would not experience this kind of a “problem”. So we could write something like this:

In map function, we now clone the user object which we modify and return.

In case you stick with object mutation, [Zoran Jambor](https://www.freecodecamp.org/news/mutating-objects-what-will-be-logged-in-the-console-ffb24e241e07/undefined) added another clever solution:  
`console.log("users", ...users);`  
So the users array is destructed and a list of objects is shown in the console:

![Image](https://cdn-media-1.freecodecamp.org/images/1*gwCP36E8dG742zoIvgm9TQ.png)

But here we also have to be careful. If the object’s value has been mutated, the console output will change on expansion:

![Image](https://cdn-media-1.freecodecamp.org/images/1*RRgBmR9HwBbFdrVCU5AOww.png)

In case you want to be absolutely sure that the object, which was logged, has the same value as it had during the console.log, you will need to make a deep clone of it. For example, we could use the following helper function instead of writing to the console directly:

On line 3 we are actually creating a deep clone of the object, which gives the following output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*YZ4sbglklsKS_AFcWIufRQ.png)

Now the object’s value is not changed on expansion.

If you use a debugger, adding a breakpoint to line 6 will pause the execution. You’ll see the current object’s value. If you prefer the console most of the time, be aware that the object/array is evaluated on the first expansion.

Check out [this great article](https://medium.com/datadriveninvestor/stopping-using-console-log-and-start-using-your-browsers-debugger-62bc893d93ff) on how to use your browser’s debugger.

Thank you for reading. Please share it with anyone who might find it useful and leave feedback. (This is my first story on Medium, and I would like to continue writing and get better at it).

