---
title: 'Progressive Web Apps 102: Building a Progressive Web App from scratch'
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2018-09-13T00:19:37.000Z'
originalURL: https://freecodecamp.org/news/progressive-web-apps-102-building-a-progressive-web-app-from-scratch-397b72168040
coverImage: https://cdn-media-1.freecodecamp.org/images/0*q57QiIkbThi9Mqvl
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'We learnt about what is a Progressive Web App (PWA) in part 1. In this
  part, we are going to build a progressive web app using no frameworks but just DOM
  manipulation.

  Let’s do a quick recap of what we have learnt so far. For an app to be progressive...'
---

We learnt about [what is a Progressive Web App (PWA)](https://medium.freecodecamp.org/progressive-web-apps-101-the-what-why-and-how-4aa5e9065ac2) in part 1. In this part, we are going to build a progressive web app using no frameworks but just DOM manipulation.

Let’s do a quick recap of what we have learnt so far. For an app to be progressive, it needs to have the following requirements:

1. a manifest file — `manifest.json`
2. service worker with at least a fetch event — `serviceworker.js`
3. icon — `icon.jpeg`
4. served over HTTPS — `https://www.myawesomesite.com`

In this tutorial, I will be talking about requirements 1 and 2 — creating a manifest file and registering a service worker.

### Objective

For this example, we are going to create a simple progressive web app. The complexity is kept intentionally simple so that we can focus on the concepts of a progressive web app. You should be able to take these concepts and apply them in your own Angular, React, Vue or vanilla JavaScript app.

We are going to create a meme engine. We will pull the latest trending memes from `giphy.com` and display them in our app. A user should be able to view the images even if the connection is down. Hence, we are providing a seamless offline experience.

Great! So now let's get to the important stuff.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6EJH5wIYnR3sHy6yI4bm7w.gif)

### Step 0: Build the app

Let’s start with a skeleton index.html:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>All the memes!</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
<header>
    <h1 class="center">Top trending memes today</h1>
</header>
<main>
    <div class="container"></div>
</main>
<script src="app.js"></script>

</body>
</html>
```

As you can see, it is a simple `index.html` that only prints out the text `Top trending memes today`. Nothing fancy.

Next, let’s add an ability to fetch trending memes from `giphy.com`. Here is what the fetch function looks like:

```js
async function fetchTrending() {
    const res = await fetch(`https://api.giphy.com/v1/gifs/trending?api_key=${apiKey}&limit=25`);
    const json = await res.json();

    main.innerHTML = json.data.map(createMeme).join('\n');
}
```

### Let’s make it progressive

#### Step 1: Manifest file

As you may recall from part 1, the manifest file is a `json` file. It has meta information about the app like icon name, background color, the name of the app, etc. Here is a `manifest.json` file with these parameters:

```json
{
  "name": "Meme",
  "short_name": "Meme",
  "icons": [{
    "src": "images/icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png"
    }, {
      "src": "images/icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png"
    }, {
      "src": "images/icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png"
    }, {
      "src": "images/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    }, {
      "src": "images/icons/icon-256x256.png",
      "sizes": "256x256",
      "type": "image/png"
    }],
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#3E4EB8",
  "theme_color": "#2F3BA2"
}
```

You can also use a tool to generate this. [Here is a tool](https://app-manifest.firebaseapp.com/) that I found useful:

![Image](https://cdn-media-1.freecodecamp.org/images/1*EeVAMTLF9yowvPPJuOHpqw.png)
_Web App manifest generator_

Adding it to our app is simple. Add the following line to `index.html` :

```html
<link rel="manifest" href="/manifest.json">
```

#### **Step 2: Service Worker**

Let’s create the file `serviceworker.js` . First, we are going to register the service worker on install. Then we will cache some static assets such as `styles.css` and `app.js.` Next, we need to provide offline capability using `fetch` . Here is what the `serviceWorker.js` looks like:

```js
const staticAssets = [
    './',
    './styles.css',
    './app.js'
];

self.addEventListener('install', async event => {
    const cache = await caches.open('static-meme');
    cache.addAll(staticAssets);
});

self.addEventListener('fetch', event => {
    const {request} = event;
    const url = new URL(request.url);
    if(url.origin === location.origin) {
        event.respondWith(cacheData(request));
    } else {
        event.respondWith(networkFirst(request));
    }

});

async function cacheData(request) {
    const cachedResponse = await caches.match(request);
    return cachedResponse || fetch(request);
}

async function networkFirst(request) {
    const cache = await caches.open('dynamic-meme');

    try {
        const response = await fetch(request);
        cache.put(request, response.clone());
        return response;
    } catch (error){
        return await cache.match(request);

    }

}
```

Let’s break this down. A service worker will help us cache data and fetch resources. If we have data in our cache, we return the data from cache or else fetch it from the network. For your own app, think of what functionality you will need to provide for offline access. Then, cache resources accordingly. For my case, I want to show previously cached images when the network is down.

We will need to add this to our index.html. To add it, we will register the service worker by leveraging the browser’s navigator library:

```js
window.addEventListener('load', async e => {
    await fetchTrending();

    if ('serviceWorker' in navigator) {
        try {
            navigator.serviceWorker.register('serviceWorker.js');
            console.log('SW registered');

        } catch (error) {
            console.log('SW failed');

        }
    }
});
```

Let’s verify that it actually has been registered. Click on the network tab in the browser and go to application settings. This tab is really helpful when developing a progressive web app. Reload the page, and you will be able to see a service worker in this tab.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ayDNoz8Aw59BlVTfhrSU-w.png)
_Service Worker has been registered_

Now let’s refresh the browser. In the first load, data will be cached by the service worker. Try turning the connection off. We will still be able to view images.

Our app is now available even offline! If you have enabled HTTPS and uploaded an icon, congratulations you now have a Progressive Web App!

### Next Steps

If you are interested in developing your own progressive web app, I would highly recommend checking out this [codelabs](https://codelabs.developers.google.com/codelabs/your-first-pwapp/) by Google Developers.

Did you learn something new? Have comments? Know a DevJoke? [Tweet me @shrutikapoor08](https://twitter.com/shrutikapoor08)

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">// When I wrote this, only God and I understood what I was doing<br>// Now, only God knows<a href="https://twitter.com/hashtag/devjoke?src=hash&amp;ref_src=twsrc%5Etfw">#devjoke</a> <a href="https://twitter.com/hashtag/notajoke?src=hash&amp;ref_src=twsrc%5Etfw">#notajoke</a> <a href="https://twitter.com/hashtag/development?src=hash&amp;ref_src=twsrc%5Etfw">#development</a> <a href="https://twitter.com/hashtag/javascript?src=hash&amp;ref_src=twsrc%5Etfw">#javascript</a> <a href="https://t.co/4V6lMUdhdb">pic.twitter.com/4V6lMUdhdb</a></p>&mdash; Shruti Kapoor (@shrutikapoor08) <a href="https://twitter.com/shrutikapoor08/status/1027666190447955968?ref_src=twsrc%5Etfw">August 9, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



