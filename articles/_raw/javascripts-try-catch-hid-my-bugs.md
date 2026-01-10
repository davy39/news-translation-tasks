---
title: JavaScript's try-catch hid my bugs!
subtitle: ''
author: Zubin Pratap
co_authors: []
series: null
date: '2019-11-08T14:30:00.000Z'
originalURL: https://freecodecamp.org/news/javascripts-try-catch-hid-my-bugs
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/thomas-smith-doI0mceCxfk-unsplash.jpg
tags:
- name: Code Quality
  slug: code-quality
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'Let me start by making one thing clear - JavaScript is a great language,
  and not to blame. I was totally to blame - my mental model of error handling was
  incomplete, and that caused the trouble. Hence, this post.

  But first, let me give you some conte...'
---

Let me start by making one thing clear - JavaScript is a great language, and not to blame. I was totally to blame - my mental model of error handling was incomplete, and that caused the trouble. Hence, this post.

But first, let me give you some context. I was writing a bunch of code involving third party APIs ([Stripe's recurring billing and subscription APIs](https://stripe.com/docs/billing/quickstart), to be specific), and had written a wrapper class and some server route-handlers to respond to requests from the front-end web app. The entire application is React +TypeScript + Node, with a [Koa server](https://koajs.com/).

As part of this, I was trying to handle the following errors:

1. Errors thrown by Stripe's API
    
2. Errors thrown by my wrapper class, especially when fetching user data from the database
    
3. Errors in route-handlers that arise from a combination of the above.
    

During development, my most common errors were incomplete data in the server requests and incorrect data passed to Stripe.

To help you visualize the flow of data, let me give you some background on the server-side code. Typically this is what the function call chain looked like:

*Route-Handler -&gt; Stripe Wrapper -&gt; Stripe API*

The first function being called would be in the Route-Handler, then in the Stripe Wrapper class, inside which the Stripe API method would be called. So the call stack has Route-Handler at the bottom (first called function) and the Stripe API method on the top (last called function).

The problem was that I did not understand where to put my error handling. If I did not put an error handler in the server code, then node would crash (literally, exit execution!) and the front end would receive an error HTTP response (typically a HTTP [5xx err0r](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500)). So I put a few `try-catch` handlers inside the various methods being called, and added logging statements inside the `catch` block. That way I could debug the error by tracking the logs.

An example of the calling logic:

```javascript
 function stripeAPI(arg){
    console.log('this is the first function')
    if(!arg) throw new Error('no arg!')
    // else
    saveToDb()
}

function stripeWrapper(){
    console.log('this is the second function, about to call the first function')
    try{
        stripeAPI()
    } catch(err) {
//         console.log(' this error will not bubble up to the first function that triggered the function calls!')
    }
}

function routeHandler(){
    console.log('this is the third  function, about to call the second function')
    stripeWrapper()
}


function callAll(){
    try{
       routeHandler() 
       return 'done'
    } catch (err){
       console.log('error in callAll():', err)
       return ' not done '
    }
    
}


callAll()
```

The problems?

1. If I didn't log the error, I *lost* the error! In the above snippet, note that even though I've called `first()` without the required arguments, the error defined in the definition of `first` did not get thrown! Also, there is no `saveToDb()` method defined... and yet this was not caught! If you run this code above, you will see it returns 'done' - and you've got no idea that your database wasn't updated and something had gone wrong! ☠️☠️☠️
    
2. My console had way too many logs, repeating the same error. It also meant that in production, there was excessive logging... ?
    
3. The code looked ugly. Almost as ugly as my console.
    
4. Others who worked with code found it confusing and a debugging nightmare. ?
    

None of these are good outcomes, and all are avoidable.

## The concepts

So, let's get some basics out of the way. I'm sure you know them but some people may not, and let's not leave them behind!

Some basic terminology:

**Error** - also known as an 'exception', is when something goes wrong in the node code, and the program exits immediately. Errors, if not handled, will cause the program to come to a screeching halt, and ugly messages are spewed into the console, with a long and generally hideous error stack trace message.

**Throw** *\-* the `throw` operator is how the language handles an error. By using `throw` you generate an exception using the value you put after the operator. Note that the code after `throw` does not get executed - in that sense it is like a `return` statement.

**Error** - there is a JavaScript [object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) called `Error`. An error gets 'thrown' in order to help the programmer know something needs to be handled. Think of it as a little ticking bomb ? that gets thrown from one function to another inside a chain of function calls. Technically, you can throw any data, including JavaScript primitives as an error, but it's generally a good idea to throw an `Error` object.

You typically construct the `Error` object by passing in a message string like so: `new Error('This is an error')`. But simply creating a new `Error`? object is unhelpful as that's only half the job. You've got to `throw` it so it can be caught. That's how it becomes useful.

Languages generally come with a [standard set of errors,](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors) but you can create a custom error message with the `new Error('this is my error message')` constructor, and your error message should help you work out what's going on. More on [Node errors.](https://nodejs.org/api/errors.html)

**Catch** *\-* this is what you do when someone throws something at you, right? You'd probably do it reflexively even if someone threw you one of these... ?!

The `catch` statement in JavaScript lets you handle an error ? that gets thrown. If you don't catch the error, then the error 'bubbles up' (or down, depending on how you view the call stack) until it reaches the first called function and there it will crash the program.

In my example an error thrown by the Stripe API will bubble up all the way to my Route-Handler function, unless I catch it somewhere along the way and deal with it. If I don't handle the error, Node will throw an `uncaughtException` error and then terminate the program.

Let's return to my example:

**Call stack**

*Route-Handler -&gt; Stripe Wrapper -&gt; Stripe API*

**Error path**

*Stripe API (*? \_thrown here) -&gt; API Wrapper (*� �\_not caught) -&gt;* \_Route-Handler (\_� �still *not caught) -&gt; ccrraashh* ???

We want to avoid app crashes as it can cause your data to corrupt, your state to be inconsistent, and your user to think your app sucks. So handling errors thoughtfully requires many levels of analysis.

There are some detailed guides to error handling in JavaScript and one of my favourites is [here](http://javascript.info/try-catch), but I will summarize my key leanings for you here.

## Try-Catch statement

Use these to gracefully handle errors, but be careful about *where* and *when*. When errors are caught and not handled properly they are lost. That 'bubbling up' process happens only up until the error encounters a `catch` statement. If there is a `catch` statement in the call chain that intercepts the error then the error won't crash the app, but not handling the error will hide it! Then it gets passed as an argument to `catch` and it requires you to handle it there.

```javascript
try{
// code logic
} catch (error) {
// handle the error appropriately
}
```

So it's very important to catch *and* handle the error at a point where it makes the most logical sense for you when you have to debug it. It's tempting to think that you must catch it at the very first place it comes up (the last function called that sits right on the top of the call stack), but that isn't true!

*Route-Handler -&gt; Stripe Wrapper (don't catch here!) -&gt; Stripe API*

If I put my `try-catch` in the Stripe Wrapper which directly invokes Stripe's API, then I don't have information on *where* my Stripe Wrapper function was called. Maybe it was the handler, maybe it was another method inside my wrapper, maybe it was in another file altogether! In this simple example it's obviously called by Route-Handler, but in a real world app, it could be called in multiple places.

Instead, it makes sense for me to put the `try-catch` in the Route-Handler, which is the very first place where the function calls begin that resulted in the error. That way you can trace the call stack (also called unwinding the call stack) and drill down into the error. If I send bad data to Stripe it will throw an error, and that error will pass through my code until I catch it.

But when I catch it I need to handle it properly, or I could inadvertently conceal this error. Handling errors usually means deciding whether I need my front end user to know something has gone wrong (their payment didn't work, for example), or is it just an internal server error (for example, Stripe could not find the product ID I passed) that I need to handle gracefully without tripping up my front end users and crashing the Node code. If I added things to the database that are not correct, then I should clean up those false writes now.

When handling the error, it is a good idea to log it so I can monitor the app for bugs and failures in production and debug efficiently. So at the very, very least, handling would include logging the error in the `catch` statement. But...

```javascript
 function stripeAPI(arg){
    console.log('this is the first function')
    if(!arg) throw new Error('no arg!')
    // else
    saveToDb()
}

function stripeWrapper(){
    console.log('this is the second function, about to call the first function')
    try {
        stripeAPI()
    } catch(err) {
        console.log('Oops!  err will not bubble up to the first function that triggered the function calls!')
    }
}

function routeHandler(){
    console.log('this is the third  function, about to call the second function')
    stripeWrapper()
}


function callAll(){
    try {
       routeHandler() 
       return 'done'
    } catch (err){  
       console.log('error in callAll():', err)
       return ' not done '
    }
    
}


callAll()
```

...as you can see above, if I catch it and log it in the middle level (my Stripe Wrapper class), it won't reach `routeHandler` or `callAll`, and my app will not know something went wrong. `callAll` still returns `done` and the only evidence something went wrong was in the log statement: `'Oops! err will not bubble up to to first function that triggered the function calls!'`. Had we not put a log statement there the error would have vanished without a trace.

This is 'error hiding' and it makes debugging a pain. If I add a `try-catch` but don't do anything in the `catch` statement, I will prevent my program from crashing. But I also end up 'hiding' the problem! It usually leads to inconsistent state - parts of my server code thinks everything is OK, and tells my front end that. But another part of my server code had indicated something was wrong!

In this simple example, it's easy to unravel, but think of deeply nested called across your entire application - what a nightmare!

If you absolutely need to handle the error in the middle of your call stack, then be sure to re-throw the error appropriately. That means ending your `catch` statement with another `throw error` operation. That way the error will get thrown again and continue to 'bubble up' towards the first function (bottom of the call stack) that triggered the call chain where it can be properly handled again.

Here's what it looks like, adding just one small re-throw in the `stripeWrapper()` function. Run the code and see the difference in outcome because `callAll()` now gets passed the error!

```plaintext
function stripeWrapper(){
    console.log('this is the second function, about to call the first function')
    try{
        stripeAPI()
    } catch(err) {
        console.log('Oops!  err will not bubble up to to first function that triggered the function calls!')

        throw err  // add this to re-throw!

    }
}

function callAll(){
    try{
       routeHandler() 
       return 'done'
    } catch (err){  // catches the re-thrown error and prints it to console!
       console.log('error in callAll():', err)
       return ' not done '
    }
    
}
```

Since you threw the error in the middle stage, it went to the outer boundary, and got caught there. The code returns `not done` and you can investigate why the error says 'no arg'. You can also then see that it never executed `saveToDb()`, as the error threw before that code could be executed! That could be a good thing in cases where you're saving things to the database *assuming that there were no errors until that point*. Imagine saving things to the database that should never have been saved - that's dirty data in the database now! ???

So, don't do what I did in my early days of programming and simply log the error at *every* step in the call stack and re-throw it. It just means you will get multiple logs for each error as it passes through the call stack! Only intercept the error at a place where you can most efficiently and usefully handle it, ideally once in a given chain of calls.

In general, it really helps if you place your `try catch` statement at the outermost (first calling) function that lies at the bottom of the call stack. You can identify this as the place the error will bubble up to *just before* throwing an `uncaughtException` error. That's a good place to catch, log, and handle it.

To see the difference in handling when you don't use the `try-catch` simply modify `callAll()` to look like this:

```plaintext
function callAll(){
    routeHandler()  
    
    // this won't run!
    console.log('This function is not contained inside a try-catch, so will crash the node program.')
}

callAll()
```

You'll note that the `console.log` statement never runs here because the program crashes when `routeHandler()` finishes executing.

## Rules of Thumb ???

So let's summarize some quick rules that will cover 90+% of your needs:

1. Do not litter your code with `try-catch` statements
    
2. Try as much as possible to `catch` only once in a given chain of function calls
    
3. Try and place that `catch` at the outermost boundary - the first function that starts the chain of function calls (bottom of the call stack)
    
4. Do not leave your `catch` statement empty as a way to stop your program from crashing! If you don't handle it, chances are it will lead to inconsistent state between your front end and back end. This can be dangerous and lead to a horrible user experience ?!
    
5. Do not use a `catch` statement only in the middle of the call stack, and not at the outer boundary. This will cause the error to get 'hidden' in the middle of your code where it isn't going to help you debug or manage data properly. Others who work with your code will find where you live and cut off your internet connection.
    
6. Catch it where you need to know, and where you can meaningfully do all the things necessary to clean things up.
    

*Stripe API (*? *thrown here) -&gt; API Wrapper (*? *passing through) -&gt;* *Route-Handler (*? *caught, handled, logged) -&gt;* ???

Thanks for reading!

If you would like to learn more about my journey into code, check out [episode 53](http://podcast.freecodecamp.org/53-zubin-pratap-from-lawyer-to-developer) of the [freeCodeCamp podcast](http://podcast.freecodecamp.org/), where Quincy (founder of freeCodeCamp) and I share our experiences as career changers that may help you on your journey. You can also access the podcast on [iTunes](https://itunes.apple.com/au/podcast/ep-53-zubin-pratap-from-lawyer-to-developer/id1313660749?i=1000431046274&mt=2), [Stitcher](https://www.stitcher.com/podcast/freecodecamp-podcast/e/59201373?autoplay=true), and [Spotify](https://open.spotify.com/episode/4lG0RGpzriG5vXRMgza05C).

I will also hold a few AMAs and webinars in the coming months. If this is of interest to you please let me know by going [here](http://www.matchfitmastery.com/). And of course, you can also Tweet me at [@ZubinPratap](https://twitter.com/zubinpratap).

(Banner photo by [Thomas Smith](https://unsplash.com/@thomastasy?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/bugs?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText))
