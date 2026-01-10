---
title: How to build a custom PWA with Workbox in create-react-app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T19:23:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-custom-pwa-with-workbox-in-create-react-app-be580686cf73
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Sp2Kk29yH_3VsOeB4i1dpg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Zaid Humayun

  Note: This is the third in a series of posts about PWAs inside of React. For a quick
  primer, see the previous two posts here and here.

  In this follow up post, I’m going to take you through how to build a custom Progressive
  Web App (PW...'
---

By Zaid Humayun

**Note:** This is the third in a series of posts about PWAs inside of React. For a quick primer, see the previous two posts [here](https://medium.freecodecamp.org/how-to-build-a-pwa-with-create-react-app-and-custom-service-workers-376bd1fdc6d3) and [here](https://medium.freecodecamp.org/how-to-customize-service-workers-with-create-react-app-4424dda6210c).

In this follow up post, I’m going to take you through how to build a custom Progressive Web App (PWA) using [Google’s Workbox library](https://developers.google.com/web/tools/workbox/) without ejecting from the create-react-app (CRA) shell.

Workbox is a collection of libraries that make it easier to build offline functionality. Workbox is also considered the successor to the `sw-precache` library, which CRA uses to generate a default SW.

There has been some talk about CRA migrating from `sw-precache` to Workbox (reference [this issue](https://github.com/facebook/create-react-app/issues/2340) for details). Unfortunately, nothing seems to have come of it quite yet.

### **Goals**

1. Configure the CRA build to use [react-app-rewired](https://github.com/timarney/react-app-rewired). (react-app-rewired is a library to configure the default CRA build without ejecting)
2. Use react-app-rewired to customize the build to use Workbox to generate a service worker
3. Build a very simple todo app
4. Implement offline functionality for the todo app using Workbox.   
The offline functionality we will be targeting:  
a) Cache retrieved assets so they can be served offline  
b) Allow POSTing of data offline

### **Introducing Workbox into CRA**

First, create a fresh CRA repository with the following command:

```
npx create-react-app react-app-rewire-workbox
```

This should set up a new folder with the relevant name. Once you have this folder set up, cd into the folder and create a service worker file in the public folder. I’ll call mine `custom-service-worker.js`.

Once, you’ve done this, go ahead and remove the check for `NODE_ENV` being set to PRODUCTION inside of `registerServiceWorker.js`

Finally, inside of the `custom-service-worker.js` file, paste the following code:

This code snippet is something I’ve picked up straight from the [Workbox website](https://developers.google.com/web/tools/workbox/guides/get-started). You use the `importScripts` line to inject a global variable named `workbox` into your file. The script your are importing is served via a CDN. You then have a simple check to see if the variable was loaded correctly by the script or not.

So, we now have Workbox working for us in a dev environment. Next, let’s figure out how to implement `react-app-rewired` into CRA.

### **Implementing react-app-rewired In CRA**

Add the `react-app-rewired` package to your project folder by using the following command:

```
npm install --save-dev react-app-rewired
```

Now, if you read [the docs](https://github.com/timarney/react-app-rewired), they mention that you need to set up a `config-overrides.js` file in the root directory of your project. Let’s figure out what this does first.

I’ll set up a barebones file and explain to you what it means. There is a very detailed explanation of this in [the docs](https://github.com/timarney/react-app-rewired#extended-configuration-options), if you wish to read that instead.

You can export an object from this file with three keys: webpack, jest, devServer. The respective functions allow you to configure the webpack production server configuration, the jest configuration, and finally the webpack development server configuration.

If you look at the `devServer` key in the `config-overrides.js` file, you will notice that we are logging `configFunction.toString()` instead of just `configFunction` . This is because if you try the latter, Node will just print `[Function]` to the console.

Open up your `package.json` file and replace the scripts command for start with `react-app-rewired start` .

### **Building The Todo App**

So far, we have managed to introduce Workbox into our dev environment, and have also introduced `react-app-rewired` into our CRA shell. Let’s leave things as they are and build a sample todo app, and get it running in the dev environment.

The todo app is going to need a couple of moving pieces, just so we can actually make use of service workers.

It’s going to involve:

1. A basic UI layer (I’m going to completely ignore styling for this.)
2. A `json-server` we can request data from

I’m not going into too much detail about setting this up, because its all fairly straightforward. I’ll include a link to a git repo with a working version of this app at the end of this article, so you can have a look at that.

Here is the Todo component I have written.

The component makes a fetch request to a `json-server` I have set up, and gets a response consisting of an array of todos. The component then renders these todos. Like I said, extremely simple.

To set up the `json-server` run the following command:

```
npm install --save json-server
```

Create a file called `db.json` with the following structure

Finally, run the following command in the terminal:

```
json-server --watch db.json --port 8000
```

This runs a local server on port 8000, and watches the `db.json` file for any changes. In case anything changes, the server restarts itself. Its a very simple way to mock a server for testing your app.

Finally, update your `App.js` file to reflect your new Todo component, and remove the default JSX from that file.

Fire up the app (inside of an incognito window) and take a look at what it looks like now. You should see a list of todos and an input box below them with a button to submit. Like I said, very simple UI.

Once you’ve got all that set up, let’s figure out a way to make this stuff work offline using Workbox.

**Note:** While testing service worker functionality in a dev environment, always make sure you do so within a new incognito window each time. It makes testing and debugging much less of a headache because your data is not stored across sessions.

### **Implementing Caching With Workbox**

Now, if you go ahead and open up the Chrome toolbar, you should see something that looks like the following under the Application tab.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6M7SSHyjM_1Yf2GV8Dvk9A.png)
_Google Chrome Developer Toolbar_

Check the offline checkbox and then try to reload your webpage. It will probably fail with an error saying there was no network connection detected. If you look at the network tab, you will see a bunch of failed network requests.

The most obvious one that will fail is the request to our `json-server` to fetch the list of todos. Let’s fix that one first. Open up the `custom-service-worker.js` file and add in the following code

```
workbox.routing.registerRoute(  'http://localhost:8000/todos',  workbox.strategies.networkFirst())
```

This is setting up a caching strategy of `networkFirst` for any requests made to the`http://localhost:8000/todos` endpoint. The image below gives you a clear explanation of what the `networkFirst` strategy implies. You always check the network first, and only in case of the network failing do you go to the cache to fetch the resource. This is a typical strategy you might use when querying an API that is likely to provide fresh data.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xTrAJtPw5Cdb-SErJgBSYg.png)
_Network First strategy_

Now, the app is still not going to load because we are still missing two important pieces. Namely, we are still not caching

1. The JS bundle that is being served by our local dev server.
2. The `index.html` file

Add the following code to `custom-service-worker.js`

```
workbox.routing.registerRoute(
```

```
  /\.(?:js|css|html)$/,
```

```
  workbox.strategies.networkFirst(),
```

```
)
```

```
workbox.routing.registerRoute(
```

```
  ‘http://localhost:3000',
```

```
  workbox.strategies.networkFirst()
```

```
)
```

If you notice, the first route in the above code snippet is a `RegEx` object. This is a clean and simple way to target multiple routes with the same strategy. However, if you are targeting a resource that doesn’t follow the same origin policy, make sure to specify the entire route.

This is, of course, not the ideal way to do things. Ideally, we want static assets like JS bundles, stylesheets and HTML files pre-cached as part of the Webpack build process. We will get to that, but its important to understand that there is no black magic going on. This is all just simple caching.

Go ahead and fire up the page again and open up your console. You should see a bunch of logs by Workbox about routing. Go into offline mode, and refresh the page. You should see everything load just like normal. If you open up the workbox logs in the console, you will see Workbox printing out whether the network request failed or succeeded, and workbox’s response to that failure (see screenshot below):

![Image](https://cdn-media-1.freecodecamp.org/images/1*deKoAAdcLbj8PjqykZNvsQ.png)
_Workbox log in Chrome Dev Tools Window_

### **Implementing Deferred POSTing Of Data With Workbox**

Alright, next up: how do we POST data back to the server without a network connection?

First, let’s set up a way to POST data back online, and make sure it works. Update your `addTodo` function inside of your Todo component so it looks like the following:

All we’ve done is added a callback handler to `setState` so we can be notified when the state has updated. At this point, we’ve made a POST request to the `json-server` to update `db.json` with the new todo.

Try submitting a new todo, open up `db.json` and you should see the new todo added to your array of objects.

Now, try doing the exact same thing offline, and you should get a network error for obvious reasons. You will probably get a log statement that says: Failed to fetch.

To solve this, we’re going to make use of something called backgroundSync, the spec for which you can read up on [here](https://wicg.github.io/BackgroundSync/spec/). The way its supposed to work is that whenever you make a request to a server for a specific resource (in our case a POST request), if no network is detected, Workbox will store this request in indexedDB and keep polling the request for a set period of time. When a network connection is detected, the request will be replayed. If no network connection is established within the pre-defined period of time, the request is discarded.

The backgroundSync API uses something called SyncManager under the hood. You can read about it in the MDN docs [here](https://developer.mozilla.org/en-US/docs/Web/API/SyncManager). Unfortunately, as you can see, SyncManager is not on the standards track and Chrome is the only browser that has a fully implemented spec. What this means is that Chrome is the only browser where this is guaranteed to work reliably.

We need to add some code to `custom-service-worker.js` to get the backgroundSync stuff working for us. Add the following code to the file:

We are making use of a background sync plugin that Workbox provides us with. The first parameter you provide to the constructor is the name of the queue you want Workbox to create when storing failed requests. The second parameter is an options object, where we are defining the maximum amount of time to attempt to replay requests within.

Finally, we register a new route with the POST method, and set up the strategy we want to use for caching. This is very similar to what we have already done with the exception of defining the type of request being made, and also having a plugin defined for our strategy.

Now, try running through the same scenario of submitting a todo without any network connection and observe what happens in the log. You will get a log that looks like the following screenshot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fga8x8OIE4dT8b4DMvBRIw.png)
_Workbox adds the failed request to a queue_

You can look at the request that has been added by looking for indexedDB under the application tab in the Chrome DevTools window. Open up the listed subdirectories under the indexedDB dropdown menu, and you should see the request stored, waiting to be replayed.

Switch off the offline option in the DevTools window, and you should see a new Workbox log popup almost immediately. It will look like the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*C46elEi-gXvBXEwpy1INqw.png)
_Workbox log detailing that the failed request has been replayed and submitted_

The image above involves Workbox replaying the failed request the moment it receives a sync request, and giving you the confirmation that your request has been successful. If you look at `db.json` now, you will notice that the new todo has been added to the file.

Well, there we go. We have a way to replay failed requests through a service worker now.

What we need to do next is to integrate a Webpack plugin so Workbox can cache static assets as part of the build process. This will get rid of the need to explicitly have a route to cache static assets inside of our Service Worker file.

### **Precaching Static Assets**

This is going to be the final step. In this section, we are going to make the changes to CRA’s build process to force it to generate the Service Worker file using Workbox instead of `sw-precache`.

First up, install the following packages: `workbox-webpack-plugin` and `path`.

Open up the `package.json` file and edit the build script to run with `react-app-rewired` instead of `react-scripts` the same way we did for the start script.

Finally, open up the `config-overrides.js` file and edit it to look like the following:

There’s a couple of things we’re doing in this file.

First, we check to see if it’s a production build. If it is, we create a Workbox config object and provide it with the path of our custom SW, and also the path of the output SW we want.

We also provide an option called `importWorkboxFrom` and set it to `disabled`.

This is an option specifying that we don’t want Workbox imported from anywhere, since we’re directly requesting it from a CDN in our SW script.

Finally, we have a function that is called `removeSWPrecachePlugin` . All this does is loop over the plugins listed in the Webpack config, find the correct one, and return the index so we can remove it.

Now, go ahead and run the build for the app, and open up the SW file generated in the build folder. In my case, this SW file has the name `custom-service-worker.js`

You will notice a new `importScripts` call at the top of the file, which seems to be requesting a precache manifest file. This file is stored in the build folder, and if you open it up, you should see the list of all static assets being cached by Workbox.

### **Conclusion**

So, we’ve accomplished the following goals:

1. Configure the CRA build to use [react-app-rewired](https://github.com/timarney/react-app-rewired)
2. Use react-app-rewired to customise the build to use Workbox to generate a Service Worker — We accomplished this using `workbox-webpack-plugin.` The build process will now automatically cache all static assets.
3. Build a very simple todo app
4. Implement offline functionality for the todo app using Workbox.   
The offline functionality we will be targeting:  
a) Cache retrieved assets so they can be served offline  
b) Allow POSTing of data offline

Here is the [link](https://github.com/redixhumayun/react-app-rewired-workbox) to the repo which has a working version of the app. You can clone that and have a play with it.

> Follow me on twitter [here](https://twitter.com/zz_humayun). Follow me on GitHub [here](https://github.com/redixhumayun)

