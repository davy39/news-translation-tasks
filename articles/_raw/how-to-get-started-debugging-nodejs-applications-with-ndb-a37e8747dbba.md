---
title: How to get started debugging NodeJS applications with ndb
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T22:09:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-debugging-nodejs-applications-with-ndb-a37e8747dbba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vd_jfkBVYHNek4GsfTShkQ.jpeg
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Geshan Manandhar

  NodeJs was released almost 9 years ago. The default debugging process of NodeJs
  (read Node.js) is quite clumsy. You are likely already aware of the need to add
  --inspect to the node script with node inspector. It is also dependent...'
---

By Geshan Manandhar

NodeJs was released almost 9 years ago. The default debugging process of NodeJs (read Node.js) is quite clumsy. You are likely already aware of the need to add `--inspect` to the node script with node inspector. It is also dependent on Chrome. Then you have to look at the proper web socket connection which is hard, and debug using Chrome’s node debugger. To be honest, it is a pain in the neck.

**Finally, Google chromelabs has released ndb**, which they say is “An improved debugging experience for Node.js, enabled by Chrome DevTools”. Ndb is a boon when debugging a Nodejs app.

I am going to show a step by step process of how to debug a nodejs application with [ndb](https://github.com/GoogleChromeLabs/ndb). Below you can see ndb in action. So now let’s roll up our sleeves and get started:

![Image](https://cdn-media-1.freecodecamp.org/images/poXxYHbteBuspVOlKzmD9bqdaHtmqqt7F9t6)

### Prerequisites

Below are some prerequisites before you get started:

1. You have nodejs installed on your system (a no-brainer but still worth a mention)
2. You have general knowledge of running node scripts and working with nodejs apps.
3. You have prior debugging experience with nodejs or any other language.

For debugging nodejs applications, in place of just another script I will use a full nodejs express application. It is an open source application I used for a demo on testing nodejs applications.

### Debugging nodejs express application as a demo

I am using my open source [currency API](https://github.com/geshan/currency-api) for this step-by-step guide to debugging a nodejs application. It is built using the ExpressJS framework. You can also check out the running app hosted on [Zeit Now](https://currency-api-nodejs.now.sh/api/convert/USD/AUD/2019-01-01) to see the USD to AUD rate of 2019–01–10 as an example.

The idea of the application is simple. If the conversion rate is available in the database, it will fetch it from the database. If not, it will fetch it from another API and send it back to the user, also saving the rate in the database at the same time (async) for later use.

You can clone the application from github and run `npm install` to get it ready for debugging. This is a very simple application with most of the logic in `exchangeRates.js` [file](https://github.com/geshan/currency-api/blob/master/src/exchangeRates.js). It has mocha [tests](https://github.com/geshan/currency-api/blob/master/test/exchnageRatesTest.js) too as it was a demo for testing a nodejs application.

### 1. Getting started, install ndb

Installing ndb is very easy. All you need to do to get started debugging your nodejs application is to install [ndb](https://github.com/GoogleChromeLabs/ndb#installation). I would suggest that you install it globally with:

```
# with npm
npm install -g ndb
# with yarn 
yarn global add ndb
```

You can also install and use it locally per app if you want. One thing I had to fix was to get the latest version of Chrome, as I saw some permission issues.

### 2. Run the app with ndb (not node or nodemon)

For debugging nodejs applications with ndb, you can directly run the nodejs app script with ndb rather than node. For example, if you were used to doing `node index.js` or `nodemon index.js` in development. To debug your app you can run:

```
ndb index.js
```

Notice that you don’t need to put any `-- inspect` so the experience is a lot smoother.

_You don’t need to remember a different port or go to chrome devtools and open up a different inspector window to debug. Such a relief!_

ndb opens up a screen like below when you do `ndb .` or `ndb index.js`:

![Image](https://cdn-media-1.freecodecamp.org/images/bf5fWVVRGMvWDXEc-J0xAAvyresEZ04xyw2f)

Please add a breakpoint on line 46. As you have run the application with ndb it will run in debug mode and stop at the breakpoint like below when you hit `http://localhost:8080/api/convert/USD/AUD/2019-01-01` on the browser. I have set the breakpoint on exchangeRates.js like 46 in the screenshot below:

![Image](https://cdn-media-1.freecodecamp.org/images/AfCAHbcURVEjAF8NNTUwN0jXozpjyvv0RO5u)

ndb allows you to run any script for debugging. For example, I can run `ndb npm start` and it will use the nodemon run. This means I can debug the application while changing the code which is great.

_As an example it can be run with `ndb npm start` to debug this nodejs express application._

You can also debug your test with a command like `ndb npm test`.

### 3. Let’s debug some code

As the debugger is working I can place more break points or run through the code at my speed and convenience.

_The essential shortcuts are `F10` to step over function call and `F11` to step into a function._

The usual debugging workflow I assume you are familiar with. Below I have advanced to line 52:

![Image](https://cdn-media-1.freecodecamp.org/images/wMByQMEy-UYehLe-SxXz-nGM9sDw5zwg-Srd)

### More debugging things

As with any other debugger, with ndb you can:

1. Add watches
2. Check the call stack trace
3. Check the process

_The console tab is also helpful if you want to some quick nodejs code in the context._

Read more about what you can do with ndb in the official [readme](https://github.com/GoogleChromeLabs/ndb#what-can-i-do). Below is a screenshot of the useful console:

![Image](https://cdn-media-1.freecodecamp.org/images/gICkxIsuYHbODz87IhtR979LkdhnHdh05R-z)

### Conclusion (TL;DR)

Debugging any nodejs application with ndb is a better developer experience. To debug the currency API nodejs express app with ndb, you run the following commands, given you have node > 8 installed:

1. npm install -g ndb
2. git clone [[email protected]](https://geshan.com.np/cdn-cgi/l/email-protection):geshan/currency-api.git
3. cd currency-api
4. npm install
5. ndb npm start
6. After the ndb debugger opens up, add a breakpoint at line 46 of src/exchangeRates.js
7. Then open `http://localhost:8080/api/convert/USD/AUD/2019-01-01` in the browser
8. Now as the app should pause at the breakpoint, enjoy! and continue debugging.

If it works for this app, you can debug any of your nodejs application with this approach.

_Welcome to the new way of debugging nodejs applications that is browser independent and a lot smoother than the default experience. Step up your debugging nodejs application game._

I hope this post has helped you debug your nodejs application better. If you have any other things to share about debugging nodejs apps or better usage of ndb please comment below!

Thanks for reading!

You can read more of my blog posts [geshan.com.np](https://geshan.com.np/blog/2019/01/getting-started-with-debugging-nodejs-applications-with-ndb/).

