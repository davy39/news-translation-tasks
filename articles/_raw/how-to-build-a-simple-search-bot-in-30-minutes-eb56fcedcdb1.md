---
title: How to Build A Simple Search Bot in 30 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-03T20:01:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-search-bot-in-30-minutes-eb56fcedcdb1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pMm3_L9RmFcb0KLJT1SirQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By Quinn Langille

  Apartment hunting sucks, especially in Montreal. This guide will show you how to
  build a bot that stays on top of the hunt for you. This way, you’ll never have to
  endlessly refresh your searches again.

  Context

  Unlike other cities, m...'
---

By Quinn Langille

Apartment hunting sucks, especially in Montreal. This guide will show you how to build a bot that stays on top of the hunt for you. This way, you’ll never have to endlessly refresh your searches again.

### Context

Unlike other cities, most people who rent apartments in Montreal are on the same lease term. New leases start in July, last 12 months, and end on June 30th. While one could argue that this simplifies a lot of things — such as availability and expectations — it also means that competition is steep.

Every day I would wake up, refresh my 10 open [Kijiji](https://www.kijiji.ca/) pages, and send emails inquiring about all the new ads. I would do this again at lunch, dinner, and before bed. My reply rate was low — well below 10%. When someone did reply, their answer was usually grim.

My next step was to up the ante and actually pick up the phone. Calling made my chances a little better. Landlords were more responsive, and this time there were usually less than 10 people ahead of me. But definitely still more than 5. Back to the drawing board.

One day, while complaining to a coworker that all my time was getting eaten by this apartment hunt — it dawned on me. I could I solve this problem with my computer.

When I got home I wrote a small program that watches Kijiji searches for changes. When it sees them, it sends a Short Message Service (SMS) text to my phone with the relevant information. The rest of this article will explain how I did that.

**Note:** for those who don’t care about the tutorial, I’ve put the Kijiji scraper up as an open source repo [here](https://github.com/quinnlangille/pad-patrol): ?

### Building Pad-Patrol

When I arrived home from work, I got my laptop out and fired up my terminal. I knew the program should be lightweight, as I’ll be running it 24/7 — or at least until I find an apartment. I decided to just build a simple node script that I could execute from my terminal.

#### Setup

Assuming that you have `node` and `npm` installed, the first step — of any node project — is to initialize npm inside the project directory.

Next, let’s create an `src` directory where our code will live.

Inside the`src` directory, make an `index.js` file where our script will go.

You can do that like so:

```
$ npm init // this will ask a few questions$ mkdir src$ cd src && touch index.js
```

#### Writing the script

When making a solo project I tend to freestyle — breaking stuff and then fixing it (arguably the best way to learn). I’m going to try to mimic my initial thought process with the following instructions, but let me know if they seem all over the place.

The very first thing we have to do is make a successful request to Kijiji. To ensure that we’re able to get a proper response, let’s make a very basic fetch.

To do that, we’ll need to install a request library:

```
$ npm install request-promise
```

and then add the following to `index.js`:

Once that’s saved, we can run `$ node src/index.js` and we should see some HTML markup in our console. Step one complete — Easy!

Because we only care when content changes, lets make a simple hash of the response. That way, we can compare the response and compare the hashes. In the event we need to log our results, this will be much less cumbersome than the raw markup.

To do this, we can use a hashing tool called `checksum`:

```
$ yarn add checksum
```

and then:

Ok cool, this worked! Our 1500 lines of HTML has been cut down to 32 digits. Now, let’s wrap it in a reusable function:

The above code will create a hash from the fetched value. Then on the following fetch, it will compare the original and new hashes.

If they’re different, it will return `true`. This worked great…like, a little too great. As you’ll see, it returns `true` every time ?

After further inspection of the response from the fetch, we can see that Kijiji has a timestamp in the header. This means that the hash will be different on every fetch. It’s important to note that this would have also happened due to rotating ads and a bunch of other dynamic content.

The takeaway from the above oversight is to always carefully inspect your response when dealing with an API you didn’t write.

This mean’s we’ll need to access granular bits of the markup, so let’s install a third party package to help parse the response. [Cheerio](https://cheerio.js.org/) is a library that can ingest HTML markup and turn it into an accessible JavaScript API. It’s intended purpose was to help `jQuery` developers not use `jQuery`, but intentions are overrated.

For us, it’s going to be a fake set of Chrome Developer Tools!

As a pre-requisite to using Cheerio in this way, we need to know what to look for in our markup. So let’s bust open Chrome and inspect our URL.

If we inspect at the ads, we can see all search responses have the classes `.search-item` and `.regular-ad`. Perfect!

We can select those with Cheerio like so:

Just like we had planned, this spits out an array of neatly organized objects. According to Cheerio’s documentation, all attributes of an element are nested in a key called `attribs`. If we go back to the Chrome Developer Tools, we can see that each ad has a unique data-attribute called ID. Let’s target that — replace the code inside your `checkURL` function with the following:

```
rp(siteToCheck).then(response => {  const $ = co.load(HTMLresponse);  let apartmentString = "";
```

```
  // use cheerio to parse HTML response and find all search results  $(".search-item.regular-ad").each((i, element) => {    console.log(element.attribs["data-ad-id"]);  });});
```

Ok great, we’re getting a list of unique ID numbers. These ID’s are the only information we care about on the page.

So let’s go back to our original plan of comparing hashes, except we’ll only hash the unique IDs:

Perfect! It’s working exactly as intended. When someone posts a new ad (or removes an old ad, a caveat of watching the order of IDs) we print `true` in our console. All that’s left to do it set up our SMS tool.

#### Sending SMS from the Terminal

This is actually much easier than it seems. To do this we’ll use a third party software called [Twilio](https://www.twilio.com/). It does a lot, but one of it’s core features is to send SMS. As a bonus, it also has great JavaScript API! To finish the tutorial, you’ll need one of their [account](https://www.twilio.com/try-twilio)s — a free trial will be more than enough to play around — and maybe even get a new apartment.

Ok, so to start we need to run:

```
$ yarn add twilio
```

from there, in `index.js` lets add Twilio and define a new function called `SMS`:

```
const twilio = require(twilio);
```

```
// you'll need to get your own credentials for this oneconst client = new Twilio("accountID", "authKey");
```

```
function SMS({ body, to, from }) {  client.messages    .create({      body,      to,      from    })    .then(() => {      console.log(`? Success! Message has been sent to ${to}`);    })    .catch(err => {      console.log(err);    });} 
```

This simple function takes two phone numbers (`to` and `from`) and a message (`body`). Instead of console logging the result of our `checkURL` function, we can call `SMS` with whatever message we want:

There you have it! Every time our script sees a change between the site hashes, it will send a text message with the URL right to your phone ?.

### Happy Hunting!

The actual script that I’ve built is a little more complicated than the above example — I’ve put it up as an open source repo on [GitHub](https://github.com/quinnlangille/pad-patrol).

Eventually, I’d like to make some additions to it — the first of which will be making it more generic and not just a Kijiji scraper. It’s pretty basic, so it will be a great first-time project for new contributors.

Feel free to contribute in any way you see fit ?

Also, in case anyone was wondering, I just signed a lease last Sunday. The apartment I ended up renting was from the very first update pad-patrol sent me — it was destiny ✨

I’m currently working as a software developer at luxury fashion company in Montreal. I’ve been doing that for about a year, after finishing a [web dev bootcamp](https://www.decodemtl.com) last summer. I spend my free time learning hot new tech and, up until a few days ago, hunting for apartments.

