---
title: How to build a PWA with Create-React-App and custom service workers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T16:29:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-pwa-with-create-react-app-and-custom-service-workers-376bd1fdc6d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZFhS3HkqFBOeau1Amj4uBQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: progressive web app
  slug: progressive-web-app
- name: React
  slug: react
- name: technology
  slug: technology
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Zaid Humayun

  Note: This is not a primer on create-react-app or what a service worker is. This
  post assumes prior knowledge of both.

  So, I recently had the opportunity to work on a React project which involved publishing
  the resulting web applicati...'
---

By Zaid Humayun

**Note: This is not a primer on create-react-app or what a service worker is. This post assumes prior knowledge of both.**

So, I recently had the opportunity to work on a React project which involved publishing the resulting web application as a Progressive Web Application (PWA).

I realised what a struggle it is to get a PWA with custom routes configured inside of a Create React App (CRA) build. Hopefully this helps out someone stuck in a similar position.

### **PWAs in Create-React-App**

How exactly do we get a PWA running inside our CRA shell?

Now, the CRA shell bundles a service worker by default. You should have noticed that in a basic CRA shell, inside of the `index.js` file, there is a call to `registerServiceWorker`:

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
```

You can create a new CRA app and look inside the `registerServiceWorker` file.

It looks quite complex, but it is really just checking to see if the environment variables are set for a production build and if a `serviceWorker` is supported in the current browser.

If you run a build with the command `yarn build`, you can open up the build folder and check inside to see that a `service-worker.js` file has been generated. This is the default service worker file CRA generates for you.

The formatting of the file is inline ES5 JavaScript, which makes it a little hard to read. But you can dump it into any prettifier, and you should see a more legible file.

Looking into the above file should show you that it is simply creating a static cache with the following cache name: `sw-precache-v3-sw-precache-webpack-plugin-+(selg.registration ? self.registration.scope)`. It then caches all of your static files like `index.html` and your `js` and `css` files inside of that cache.

You should also see a `fetch` event listener in there that catches a fetch event and checks to see if the app is requesting one of the previously cached static assets.

Now comes the million dollar question: what if you want to configure a dynamic cache for a specific route? In essence, a cache that will update itself with data sent from the server when the user visits a specified route. Note that this means the data will not be available at build time, and therefore cannot be cached by the default service worker generated.

### **Limitations of default PWAs in CRA**

Unfortunately, it’s not very easy to accomplish the above when using CRA. Unless you’re willing to `eject`, of course.

Take a look at these GitHub issues to see why the team at CRA won’t support customising the default service worker.

[**Custom ServiceWorker config · Issue #2237 · facebook/create-react-app**](https://github.com/facebook/create-react-app/issues/2237)  
[_1.0.0 added Progressive Web App support, is it possible to support custom config in near future? I really don't want to…_github.com](https://github.com/facebook/create-react-app/issues/2237)[**Import scripts in Service Worker by piotr-cz · Pull Request #2714 · facebook/create-react-app**](https://github.com/facebook/create-react-app/pull/2714)  
[_This PR adds an ability to use importScripts option of SWPrecacheWebpackPlugin. How-to: create a file called…_github.com](https://github.com/facebook/create-react-app/pull/2714)

So, given that we can’t seem to customise the default service-worker, how do we work our way around it?

### **Understanding How CRA Generates A Service Worker**

The first step to finding a work around for the build system is to actually understand how the build system works.

So, let’s start with the [library](https://github.com/GoogleChromeLabs/sw-precache) the build system uses to generate a service worker file.

`sw-precache` is a library that allows you to generate a service worker file based on a template. The template file is written using underscore’s templating engine.

[Here](https://github.com/GoogleChromeLabs/sw-precache/blob/master/service-worker.tmpl) is the link to the template file in the `sw-precache` source code.

Again, the template file looks complex, but it is quite straightforward once you manage to get your head around the templating language.

So, what happens when you run a build process in a CRA shell, in relation to generating a service worker, is:

1. The `sw-precache` library is executed internally
2. An options object is provided to `sw-precache` to allow generation of the service worker file from the template
3. The service worker file is generated in the `build` folder with the name `service-worker.js`

### **Overriding The Default Service Worker**

Now, how do we override the above process to allow our own custom service worker file to be generated?

The answer is based on Jeff Posnick’s (a maintainer of `sw-precache`) [stackoverflow answer](https://stackoverflow.com/questions/47636757/add-more-service-worker-functionality-with-create-react-app?rq=1).

First, we need to run the`sw-precache` CLI after the normal build process.

Install the `sw-precache` library by running the following command: `npm install --save-dev sw-precache`

Now, the `sw-precache` library runs on a config file, which is provided via an option on the CLI. This is the command: `sw-precache --config=sw-precache-config.js` , where `sw-precache-config.js` is the name of the config file.

Here is a sample config file.

```
module.exports = {
  staticFileGlobs: [
    'build/static/css/**.css',
    'build/static/js/**.js'
  ],
  swFilePath: './build/service-worker.js',
  templateFilePath: './service-worker.tmpl',
  stripPrefix: 'build/',
  handleFetch: false,
  runtimeCaching: [{
    urlPattern: /this\\.is\\.a\\.regex/,
    handler: 'networkFirst'
  }]
}
```

**Note:** It is important that you specify the swFilePath as `./build/service-worker.js` This is so that the service worker generated as a result of your custom build process overwrites the one created by CRA (they both share the same name, in this instance). Otherwise, you will end up with two service worker files in your build directory!

There is extensive documentation on the object properties and what valid values can be assigned to them on the [GitHub page](https://github.com/GoogleChromeLabs/sw-precache) for `sw-precache`.

Of special interest is the runtimeCaching option, because this is a very extensible solution to allow you to define custom rules for your service worker to respond to dynamic content.

The templateFilePath is an option for when you want the CLI to pick up your custom service worker template file. But you’re almost always going to be using the template file provided by the library itself.

Finally, we need to provide the script to signal to the CRA build system that we want our custom service worker to be generated. Go ahead and install the `sw-precache` library.

Next, update the package.json build script, with the following:

`build: react-scripts build && sw-precache --config=sw-precache-config.js`

Once you run the build process with `npm run build`, you can open up the build folder and see your generated service worker.

Run the build process with and without the custom service worker and notice the differences between the two.

### **Conclusion**

While this may seem like a very verbose approach to something as simple as customising a service worker, this approach has the benefit of keeping you firmly within the create-react-app shell.

There are other approaches to generating a custom service worker (using a combination of [react-app-rewire](https://github.com/timarney/react-app-rewired) and [workbox](https://github.com/GoogleChrome/workbox)). I’ll try and get that approach up in a post as well.

