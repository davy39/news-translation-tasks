---
title: Promises and Pokemon — how I learned to think in async
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T23:38:59.000Z'
originalURL: https://freecodecamp.org/news/promises-and-pokemon-how-i-learned-to-think-in-async-2ec098c2c90d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*J1GQbpmhZFXJ2AxGHLC1Og.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kalalau Cantrell

  If you’ve been learning JavaScript, you may have heard about promises and how awesome
  they are.

  So, you decided to research the basics. Perhaps you came across the MDN docs on
  promises or great articles like this one by Eric Ellio...'
---

By Kalalau Cantrell

If you’ve been learning JavaScript, you may have heard about promises and how awesome they are.

So, you decided to research the basics. Perhaps you came across the [MDN docs on promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) or great articles like [this one](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-promise-27fc71e77261) by Eric Elliott or [this one](https://codeburst.io/javascript-learn-promises-f1eaa00c5461) by Brandon Morelli. If you’ve read all of these and more, you’ve probably seen the go-to example of promises in action.

Once you’ve seen enough of these types of examples, however, you begin to wonder if you’re actually grasping promises. At this point, if you’re like me, you understand conceptually what makes them awesome — they allow you to write asynchronous code in a synchronous pattern — but you’re itching to see an example of what they can do other than sequence a series of `console.log` that fire at different times.

So, what did I do? I built a simple Pokemon game, featuring a turn-based battle against an [Electabuzz](https://bulbapedia.bulbagarden.net/wiki/Electabuzz_(Pok%C3%A9mon)).

**This article assumes you understand the promises example referenced above. Please check out the resources linked in the intro paragraph if you need a refresher.**

### Basic functionality

The Electabuzz and the player each start off with a certain amount of hit points (HP). The first thing that happens is Electabuzz attacks and the player loses some HP. Then, the game **waits** until the player chooses an attack to use against Electabuzz.

Yep, the game just waits…and waits…this is the part where I really started appreciating the value of using promises. Once the player chooses an attack, Electabuzz loses some HP and then it attacks again. This loop continues until either Electabuzz’s HP or the player’s HP reaches zero.

### The Pseudo-Code

Pretty simple so far. Now, let’s tweak this a bit so that Electabuzz attacks with a more natural timing. I wanted it to seem like he was “thinking” about his move before making it.

While we’re at it, let’s sprinkle in a little bit of promise action so that we can chain on functions that will fire once Electabuzz is done attacking and not a millisecond earlier. This is a turn-based game after all.

Great, this setup will later allow us to do this.

Now, on to the code for the player.

How do we write a function that when called will wait for user input before finishing its execution? We know it needs to involve an **event listener** somehow for the user input part. We also know that we should be able to use **promises** somehow for the asynchronous part…but how to put the two together?

What I found is that if you 1) create a promise, and 2) within that promise add an event listener to, in our case, the click event of a button, and 3) if the function that gets called by the event listener resolves the promise, you can achieve this waiting effect.

Voila! Now we’re able to do this.

Note that each call to `playerTurn()` in the code above will just wait…and wait…until the player chooses to attack. Only then will the execution continue to Electabuzz’s turn and then back.

But why write it like that when the same code can be written in its equivalent async/await form, which looks so much nicer? If you’ve been able to follow what we’ve done with promises up to this point, it’s not too much of a leap to see how async/await works. Compare the below code with the above and you’ll see that they are equivalent but the below code is easier to reason around.

Take a deeper dive into async/await by checking out [this article](https://medium.freecodecamp.org/oh-yes-async-await-f54e5a079fc1) by Tiago Lopes Ferreira or [these slides](https://wesbos.github.io/Async-Await-Talk/#1) by Wes Bos.

So, now our code is able to fire off a few rounds of turn-based combat with Electabuzz. But we need a way for the game to end.

Finally, we’d like the game to continue to run on its own until the game-ending conditions are met. Instead of manually repeating the `cpuTurn()` and `playerTurn()` logic like we’ve been doing, we can recursively call our `gameLoop()` function.

Now, the `gameLoop` will run and continue to call itself and continue running until either Electabuzz takes our HP to zero or we take his to zero. If you want want to learn more about recursion, watch [this YouTube video](https://youtu.be/k7-N8R0-KY4) by MPJ. While you’re at it, check out the other videos on MPJ’s Fun Fun Function channel. He is great at explaining complex topics in a fun way.

Let’s take a look at the pseudo-code in full:

### The Code

Now that we’re through the pseudo-code, here is a Pen showing how I implemented this logic with actual JavaScript:

### Conclusion

Thanks for reading. This little experiment with promises showed me that there’s a lot that promises simplify when it comes to composing asynchronous code. Although the typical promises example with console.logs and setTimeouts illustrated the concept, it just didn’t excite me so I decided to create this simple game to get me pumped about promises. I hope you picked up some of that excitement. If there are any async experts out there reading this, it’d be great to hear from you on better ways to achieve the same functionality (with generators, for instance). If anything was unclear to anyone, let me know and I’ll try to clarify.

**Please feel free to say hello on [Twitter](https://www.twitter.com/kalalaucantrell).**

