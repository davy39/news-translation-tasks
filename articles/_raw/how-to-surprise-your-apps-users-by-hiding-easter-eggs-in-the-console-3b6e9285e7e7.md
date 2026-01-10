---
title: How to surprise your app’s users by hiding Easter eggs in the console
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T00:23:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-surprise-your-apps-users-by-hiding-easter-eggs-in-the-console-3b6e9285e7e7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0B1CuHTa6jjPvRZLDBtUBw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ethan Ryan

  I love console.logging(“stuff”).

  I do it throughout my apps, for debugging purposes and feature building purposes,
  and just for the sheer hell of it. It’s fun to log stuff to the console.

  I even use console.warn() and console.error(), a...'
---

By Ethan Ryan

I love console.logging(“stuff”).

I do it throughout my apps, for debugging purposes and feature building purposes, and just for the sheer hell of it. It’s fun to log stuff to the console.

I even use `console.warn()` and `console.error()`, and `console.table()` if I’m feeling frisky.

I like all the pretty colors they make in my console, and sometimes you want some messages to stand out more than others.

But I realized while looking at [my story generator app WordNerds](https://wordnerds.co/) yesterday than I was logging to the console in production mode.

Uh-oh spaghetti-ohs.

That’s a no-no. It could slow down the code unnecessarily, and more importantly, it could compromise my users’ email addresses! I was logging all my users’ usernames and email addresses. Not cool! Their passwords are encrypted of course but still, no bueno. I wouldn’t want any bad guys getting a a bunch of my users’ email addresses and spamming them crapola.

### Getting Rid of Console Logs In Production Mode

Fixing it turned out to be easy. Sure, I could have gone through the codebase and commented out all my console.logs(), but that would be a pain, and some of them are serving important purposes in development mode.

Luckily there’s an easier, better way.

First I consulted [some of the solutions](https://stackoverflow.com/questions/8002116/should-i-be-removing-console-log-from-production-code) to this problem [listed on StackFlow](https://stackoverflow.com/questions/7500811/how-do-i-disable-console-log-when-i-am-not-debugging), and then ultimately went with the first solution listed on [this blog post](https://www.codebyamir.com/blog/suppressing-console-log-messages-in-production).

![Image](https://cdn-media-1.freecodecamp.org/images/jc4ODxkMp1KtvfhpstgQLe-aVYqusFrOAuK8)
_Solution via [www.codebyamir.com](http://www.codebyamir.com" rel="noopener" target="_blank" title=")_

As some of the comments mentioned when someone listed this as a solution to the problem: “That’s a hack. Your [sic] wasting computation in production”

![Image](https://cdn-media-1.freecodecamp.org/images/-s1srDkkrRoKPbhbzIx-WFfUHZrAf-Q60tE0)
_“That’s a hack.”_

Good debate! I wasn’t too worried about calling an empty function several times and wasting some computation in production, so I went with this solution, because it’s easy to implement and solves my problem.

Here’s how I did it, in the src/index.js file:

![Image](https://cdn-media-1.freecodecamp.org/images/DSciz3L5MRihw5jjT7o7rCeWNMz9kQI-mjGf)
_src/index.js file_

Of course I could do this in any file, like the App component, or my StoryContainer component. Anywhere as long as it was before any console logs or warns or errors were being rendered. But it made sense to me to do it at the root.

I tested it in development by replacing ‘production’ with ‘development’, and it worked! No more messages in the console.

#### Adding Messages Back Into the Console

But then I felt sad :(

No more messages in the console? Seemed so sparse.

May as well have SOME messages for those curious, intrepid word nerds daring enough to open up the console.

So I added one back in, like a hidden [Easter egg](https://en.wikipedia.org/wiki/Easter_egg_(media)):

![Image](https://cdn-media-1.freecodecamp.org/images/acJJhS1TezClILOJ2V4Uzb0okV6it-dXBUcw)
_hello everybody!_

How’d I do this? Easy: since all my app’s calls to `console.log()`, `console.warn()`, and `console.error()` where being overwritten by empty functions, I simply added in a `console.info()`! It’s basically the same as a `console.log()`. Some of the differences are listed, and disputed, [here](https://stackoverflow.com/questions/25532778/node-js-console-log-vs-console-info).

`hello everybody!` was a little boring though. I already had my app’s logged-in user’s name stored in state, so why not personalize my message?

And if I’m gonna personalize my message, why not personalized a bunch of messages, and randomly return one every time a logged-in user inspects the console? Everyone likes finding Easter eggs!

That’s what I decided to do, and here’s how I did it:

![Image](https://cdn-media-1.freecodecamp.org/images/H5wxFxT9YHiehoaeFUKSOIL70eiW-gbACi3e)
_Greeting component_

I’m rendering my Greeting component in my StoryContainer, so that whenever a logged-in user chooses to check out the console, they’ll see one of those friendly messages!

```js
function getFriendlyMessage(nameString) {
  let messages = [
    `Hello ${nameString}, it's good to see you!`,
    `sup ${nameString}`,
    `hi there ${nameString}, you look awesome today!`,
    `hi there ${nameString}, you spectacular human being you!`,
    `you look awesome today ${nameString}!`,
    `hellllooooooo ${nameString}!`,
    `Hey ${nameString}, how's life?`,
    `Can you keep a secret, ${nameString}? You're my favorite!`,
    `Nothing to see here, ${nameString}.`,
    `Congratulations, ${nameString}! You've discovered the console ;)`,
    `have i told you lately that i love you, ${nameString}?`,
    `i knew you'd find this Easter egg eventually, ${nameString}...`,
  ]
  var randomMessage = messages[Math.floor(Math.random() * messages.length)];
  return randomMessage
}
```

Coding is fun.

Thanks for reading, word nerds!

