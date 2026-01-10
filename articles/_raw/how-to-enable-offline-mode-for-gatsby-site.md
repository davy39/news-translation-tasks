---
title: How to Enable Offline Mode for Your Gatsby Site
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-09T15:15:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-enable-offline-mode-for-gatsby-site
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/gatsby-offline-article.jpg
tags:
- name: Gatsby
  slug: gatsby
- name: JAMstack
  slug: jamstack
seo_title: null
seo_desc: 'By Ondrej Polesny

  One of the reasons we create JAMstack sites is because of their great performance.
  Serving static files is easy and quick. But what if we upgrade the visitor''s experience
  and make the site available offline?

  Looking at both recent r...'
---

By Ondrej Polesny

One of the reasons we create JAMstack sites is because of their great performance. Serving static files is easy and quick. But what if we upgrade the visitor's experience and make the site available offline?

Looking at both recent reports on the State of the JAMstack in 2020 (you can check out [Kontent's report](https://tracker.kontent.ai/942894/the-state-of-jamstack-report-2020) and [Netlify's report](https://www.netlify.com/blog/2020/05/27/state-of-the-jamstack-survey-2020-first-results/)) it's clear that performance is the main reason we are building static sites. 

I call this fact a bit of a cheat. Performance benefit comes with the JAMstack by design, so it's like calling puppies cute. They're always cute because they're puppies.

If we're really serious about performance, though, even JAMstack sites can do better. But before we can dive into offline mode for Gatsby, we must understand how Gatsby serves pages:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/gatsby-site.png)

The visitor does not request every single HTML file from the server. Rather, Gatsby's JS client asks the server for the _page-data.json_ of the respective page. That's how the visitor transitions into the requested page without that classic page reload. But even for that we need the network.

## Why do websites even need an offline mode?

These days, everyone is online, right? An internet connection in mobile phones no longer seems like an option, but a requirement. We use apps like Whatsapp, Messenger, and others all the time. 

But what if we step inside an elevator? What if we're walking to a car parked in an underground garage or driving through a tunnel? What if we're inside a plane that's about to take off?

No reception. That's what all these places share. And the only thing people can do with their phones without reception is to watch downloaded Netflix movies. Until you enable offline mode for your website.

## How does it work?

In a nutshell, we save the visitor the round-trip to the server and download all the necessary data in advance. And we install a ServiceWorker which acts as a server instead of a real remote server. 

A ServiceWorker is a script that the visitor's browser runs in the background and enables features like push notifications and others. See [Google docs](https://developers.google.com/web/fundamentals/primers/service-workers) for more information.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/gatsby-service-worker.png)

With Gatsby, just like we're all used to, it's as simple as installing a plugin:

```
npm i gatsby-offline-plugin --save
```

And adding it to the `gatsby-config.js`:

``` javascript
plugins: [
    ...
    `gatsby-plugin-offline`,
    ...
]
```

But every website uses many different types of assets, so typically, we need to take one additional step and configure the service worker.

## Assets serving strategies

Every website contains many assets ranging from CSS files through images and icons to web fonts and actual page data. 

The service worker cannot really download all these assets during the first page load as that would go directly against the performance benefit. Visitors would also not be happy if their browsers started downloading 100MB of images the moment they decided to visit your photo gallery.

We can use regular expressions to target specific files and configure the service worker to treat them appropriately. Let's take a look at the available strategies:

### CacheFirst

Typical use: web fonts, stylesheets

The service worker checks the cache for the requested file. If the file's missing, it goes online to fetch it while storing it in the cache for future use.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/cache-first.png)
_Image credit: [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

### CacheOnly

Possible use: your own pre-caching logic

The service worker checks the cache for the requested file. If the file's missing, it returns an error.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/cache-only.png)
_Image credit: [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

### NetworkFirst

Typical use: non-critical API requests

The service worker goes online to fetch the requested file. If the network is down or server unresponsive, it falls back to the cache.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/network-first.png)
_Image credit: [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

### NetworkOnly

Typical use: critical API requests

The service worker goes online to fetch the requested file. If the network is down or server unresponsive, it returns an error.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/network-only.png)
_Image credit: [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

### StaleWhileRevalidate

Typical use: front-end assets, images

The service worker checks the cache for the requested file and provides it. Subsequently, it makes a network request to silently update the cache.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/stale-while-revalidate.png)
_Image credit: [https://developers.google.com/web/tools/workbox/modules/workbox-strategies](https://developers.google.com/web/tools/workbox/modules/workbox-strategies)_

## Configuring the Gatsby site

A simple configuration of a Gatsby site that should work offline looks like this:

``` javascript
{
    resolve: `gatsby-plugin-offline`,
    options: {
        precachePages: [`/blog/*`],
    },
}
```

This way I'm configuring the service worker to pre-cache all blog posts, which are all pages whose URL starts with `/blog/`. 

Once the visitor accesses the index page with links to blog posts, they will be able to click-through to any of them without an active internet connection. That is, if you use the `Link` element in the implementation. Standard anchor tags make a browser go around the service worker and fetch data from remote.

The service worker will treat all assets according to its default configuration:

* **CacheFirst**  
JS files, CSS files, everything inside folder "static/"
* **NetworkFirst**  
*/page-data/*/page-data.json files
* **StaleWhileRevalidate**  
images, web font files, etc.

So if you're worried that the service worker will fetch all assets of all blog posts, it will do so only after the visitor actually opens the blog post page. 

The reason is, cache space and the visitor's internet connection bandwidth are limited. On the first page load, the visitor downloads all the site-wide assets like stylesheets, web fonts, icons, and others, so these assets will be available in the cache on subsequent loads. Images and other resources of pre-cached pages will be resolved once the page is requested and this can be changed only via custom logic.

So in which cases would you want to change the config? There were actually not many cases I could come up with, but I did stumble upon a few:

* **Assets provided from URLs without matching filename suffix**  
Google serves CSS definitions of web fonts without the .css suffix and that is already covered by the default config. However, you may be serving images or other assets from URLs that don't have the appropriate suffix.
* **Gain more control over the cache**  
With some assets you want to be in charge of how long a certain item can reside in cache until it becomes expired.
* **Exotic assets**  
Alright, exotic may be a bit strong word :-) but web fonts in EOT format, pictures in HEIC format, short videos, songs, etc.

In these cases you need to adjust the default configuration and define it within the plugin options:

``` javascript
{
  resolve: `gatsby-plugin-offline`,
  options: {
    precachePages: [`/blog/*`],
    runtimeCaching: [
      // previous definitions from the default config
      (...),
      {
        urlPattern: /^https:\/\/fonts\.gstatic\.com/,
        handler: 'cacheFirst',
        options: {
          cacheableResponse: {
            statuses: [0, 200]
          },
          cacheName: 'google-fonts-webfonts',
          expiration: {
            maxAgeSeconds: 60 * 60,
            maxEntries: 30
          }
        }
      },
    ]
  },
},
```

This additional config item will ensure that at most 30 Google fonts served from gstatic.com will be cached for a maximum duration of one hour and will be handled using the CacheFirst strategy.

### Build the Site Before Testing

Once you are finished with the configuration, make sure to build and serve the site before testing the offline capabilities. They don't work in development mode.

```
gatsby build && gatsby serve
```

## JAMstack = performance, but...

In this article I showed you how to install and configure the offline plugin for Gatsby.

 All JAMstack sites come with the great benefit of amazing performance by design. By adding offline capabilities, you are taking the browsing experience of your visitors to the next level compared to other JAMstack sites. The service worker configuration allows you to further fine-tune how each asset will be handled and cached.

If you're interested, you can find more information about the plugin in the [Gatsby docs](https://www.gatsbyjs.org/packages/gatsby-plugin-offline/).

