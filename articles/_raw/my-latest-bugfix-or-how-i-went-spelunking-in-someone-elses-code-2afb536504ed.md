---
title: 'My latest bugfix: or, how I went spelunking in someone else’s code'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-11T00:45:51.000Z'
originalURL: https://freecodecamp.org/news/my-latest-bugfix-or-how-i-went-spelunking-in-someone-elses-code-2afb536504ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NSN1a2xVtV1exzcD8fpzhA.jpeg
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Tiffany White

  I love CodeSandbox. It has pretty much replaced CodePen for me unless I am fiddling
  around with CSS or freeCodeCamp front-end projects.

  I like going through the sandboxes and picking out different ones to look at, take
  apart, and fig...'
---

By Tiffany White

I love [CodeSandbox](https://codesandbox.io/). It has pretty much replaced CodePen for me unless I am fiddling around with CSS or freeCodeCamp front-end projects.

I like going through the sandboxes and picking out different ones to look at, take apart, and figure out how they work.

While going through [React Tutorial for Beginners](https://egghead.io/courses/the-beginner-s-guide-to-react) by [Kent C. Dodds](https://kentcdodds.com/) on [Egghead.io](https://egghead.io), I decided I would look for sandboxes that correlated with the course, as I was using Codesandbox to build out the stopwatch we were building in that course.

I found a [sandbox](https://codesandbox.io/s/v1vqomk697) which I forked and found to be buggy.

Why didn’t the stopwatch work? Glancing at the code for a few seconds, I saw some obvious problems right away.

Here is an example of the stopwatch being broken:

![Image](https://cdn-media-1.freecodecamp.org/images/0*eaNKf6gfrCEUwhR8.gif)

#### Bugfix 1

The first thing I noticed was on line 7:

`Date.now()` needs parentheses. `Date` is an an object constructor with `.now()` being a method. When we click on the start button, React doesn’t know what to do here; we aren’t setting the state of `lapse` to be a number, which we expect. By adding the parentheses, we get the start button to work. No more `NaNms`.

But now we have another problem: _the timer won’t stop_.

![Image](https://cdn-media-1.freecodecamp.org/images/0*NH4ULkrZWEeopk1_.gif)

I also removed the `console.log(Math.random());` because I felt it was unnecessary.

#### Bugfix 2: Getting the Stopwatch to Stop and Clear

Each time the button is clicked, we set the state to either `running` or `lapse`. The timer runs when we click `start` but clicking `stop` or `clear` doesn’t seem to work. How can we fix this?

We can create a timer update function that accepts the current state. We can accomplish this by using native DOM APIs such as `setInterval()` and `clearInterval()`. We can run conditional logic to see if the timer is running:

and use `Date.now()` to get the timestamp in ms, and assign it a `startTime` variable to compare the current time to the amount of time that has passed. When we click the start button, it sets the `startTime` to the current timestamp. We also need to return a new state as state is _not_ mutable.

Okay so this _partially_ works. But as you can see below, if I click `clear` while the stopwatch timer is running, it _doesn’t_ clear the timer, and it also doesn’t allow me to _stop_ the timer, either.

![Image](https://cdn-media-1.freecodecamp.org/images/0*LLjNKMeXojOisrdD.gif)

How do we fix this particular bug?

If we look back at the previous code, we can see we are using `clearInterval()` to reset the stopwatch timer. In our current iteration, our `handleOnClear` method is just _setting_ the state without _clearing_ the previous state.

We can fix this by adding `clearInterval()` and passing in the timer function to the `handleOnClear` method to clear the state.

This will give us the results we want.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wtb7CitBJj9OtyLf.gif)

#### Potential Problem?

There is a memory leak in this particular iteration. The timer will run until it is _explicitly_ stopped in the DOM. We can use a [React lifecycle method](https://reactjs.org/docs/state-and-lifecycle.html#adding-lifecycle-methods-to-a-class) to stop all processes in the DOM when this component is mounted or unmounted.

For this we can use `componentWillUnmount` to tell React to unmount the component once it is done rendering.

#### Thoughts and Conclusions

I find it much more enjoyable fixing _other people’s_ bugs than my own. This was a fun exercise and I plan on doing it more regularly and blogging about it.

This stopwatch is a stupid simple component but if you are just scratching the surface of React like I am, I am sure digging into something like this stopwatch and figuring out how it works is an excellent exercise and use of one’s time.

#### Sign Up for the Newsletter. No spam. I hate that, too.

