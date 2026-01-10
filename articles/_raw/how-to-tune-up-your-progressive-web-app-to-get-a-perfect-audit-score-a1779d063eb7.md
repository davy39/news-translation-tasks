---
title: How to tune up your Progressive Web App to get a perfect audit score
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T16:27:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-tune-up-your-progressive-web-app-to-get-a-perfect-audit-score-a1779d063eb7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Xfaf0E9NtFH7seZM.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: progressive web app
  slug: progressive-web-app
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ondrej Chrastina

  Progressive Web Apps (PWAs) quickly became the hottest development platform during
  the last year. Let’s take a look at what you need to do to adhere to the PWA standards.

  Articles about the PWA concept are all over the place. I wi...'
---

By Ondrej Chrastina

Progressive Web Apps (PWAs) quickly became the hottest development platform during the last year. Let’s take a look at what you need to do **to adhere to the PWA standards.**

Articles about the PWA concept are all over the place. I will focus on the actual steps that need to be done to have the PWA fully aligned to the specification. I will provide a GitHub link with the list of changes for each step I performed to allow you to easily try it yourself.

### Prerequisites

* [node.js](https://nodejs.org/en/download) v8+
* [Google Chrome](https://www.google.com/chrome/) browser v60+

I will start with that simple Angular application I used for showcasing the combination of Angular and PWA approach in my [previous article](http://bit.ly/pwa-in-angular-and-headless-cms). I have [upgraded](https://github.com/Kentico/cloud-sample-angular-pwa-app/pull/1) it to Angular v6 and [Kentico Cloud SDK v4](http://bit.ly/kc-js-cloud-sdk-v4).

![Image](https://cdn-media-1.freecodecamp.org/images/DgVUccQ9UixlgkMxLh7qbEg-AX40bYZiXcJJ)
_[Upgrade changes](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/443472555e627fc149e8b6d38d84cef228e0ac21" rel="noopener" target="_blank" title=")_

This application is a simple listing of interesting places stored in a headless CMS loaded by the SDK. The app already has these two perks that make it a PWA app:

* `manifest.json` with a set of icons used when the app is installed in the system.
* service worker implementation used for caching of the application skeleton (called the app shell) and the data from the headless CMS.

![Image](https://cdn-media-1.freecodecamp.org/images/hsRG5ts-kQ1s1k5uVWD1D1bMcC5RuUsvDA5P)

Although the app is ready to be installed and used, **it still needs a few touches to meet the PWA specification**.

### How to get through the PWA checklist

To verify whether the app meets all the criteria defined by the [Google checklist](https://developers.google.com/web/progressive-web-apps/checklist), one can use various tools these days. The most popular is called [Lighthouse](https://developers.google.com/web/tools/lighthouse).

![Image](https://cdn-media-1.freecodecamp.org/images/gL2OcEH88JhPypm7IMJKxpIJaafA5XW7wt1v)
_[Google checklist](https://developers.google.com/web/progressive-web-apps/checklist" rel="noopener" target="_blank" title=")_

Lighthouse is already embedded into the Google Chrome browser [developer tools](https://developers.google.com/web/tools/lighthouse/#devtools) on the [audit tab](https://developers.google.com/web/updates/2017/05/devtools-release-notes#lighthouse). To run it, I recommend that you publish the production variant of the app on the internet, and perform the audit from there.

To achieve this, just download the app in the “initial state” and then run the following commands.

For deployment, I am using [surge](https://surge.sh/).You just have to register and install the CLI tools. Then, you're able to deploy the folder into a *.source.sh sub-domain.

![Image](https://cdn-media-1.freecodecamp.org/images/SvXmPZVDOy8AbV4N1w6jMyeP2CtRAzDl4hD0)
_[Initial app state](http://bit.ly/git-repo-angular-pwa-before-audit" rel="noopener" target="_blank" title=")_

* `npm install`
* `npm run build` to build the application in production mode into the `/dist` folder
* `npm install -g surge` to install surge CLI globally
* `surge /dist your-own-subdomain.surge.sh` deploy “dist” folder to the specified URL. This requires you to either log in or [set the surge environment variables](https://docs.travis-ci.com/user/deployment/surge#Environment-variables) with the login and token.

Then, just navigate to the app in the Chrome browser. Go to “Developer Tools” > “Audits” > “Perform an audit” > select “Progressive Web App” > “Run audit”. You’ll see the following results.

![Image](https://cdn-media-1.freecodecamp.org/images/gk8m5IDRjuVsWu1lMwdkkjPBcSU9SmWCHz4o)

As you could see, eight checks already passed.

Now, let’s inspect the PWA checklist.

### PWA checklist

#### Fallback when no JavaScript is available

All you have to do to remove this message is to provide some message for non-JavaScript browsers. The `noscript` tag is an ideal way to do that. Just add the following HTML code to the body of `index.html`.

```
...<noscript>    This page requires you to have the Javascript enabled.</noscript>...
```

![Image](https://cdn-media-1.freecodecamp.org/images/hoYVfT5QWsbq8seVneFyXYi-6HimWlhEJnuw)
_[Add no-script content](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/65ae78f74713eb3d6719673e6d21ae0e8c8d5497" rel="noopener" target="_blank" title=")_

#### Address bar does not match brand colors

This warning tells you that you should specify the basic thematic color for the address bar. All you need is just an `HTML` meta tag in the head section of the page. I’ve chosen the same color that’s used for the top toolbar.

```
<html><head>...<meta name="theme-color" content="#1e88e5">...</head>...
```

![Image](https://cdn-media-1.freecodecamp.org/images/AebJUq6fV5ESn9rJemam9Xp2JvhONfNYROGM)
_[Add theme color meta tag](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/3293c5f93726674289186ccddedaeac99350bc0b" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/OJVdeXrUQlSZMNnFZFQaRbbuaruwuRj4tYzJ)

#### HTTP traffic is not automatically redirected to HTTPS

This is just about deployment configuration. To achieve [automatic https enforcement](https://surge.sh/help/using-https-by-default) just use “https://” before the domain you want to deploy the app to.

* `surge /dist [**https://**your-own-subdomain.surge.sh](https://url-where-you-want-to-deploy-you-app.surge.sh)`

Now you are ready to perform the audit again.

* `npm run build`
* `surge /dist [**https://**your-own-subdomain.surge.sh](https://url-where-you-want-to-deploy-you-app.surge.sh)`

![Image](https://cdn-media-1.freecodecamp.org/images/Wjq4nJ11MBLPuI-LTFTqQVwYSPhzanujT4oh)

**Yippee!**

You’ve passed all the automatic checks. Now, you might have noticed that there were manual steps outlined in the report:

* Site works cross-browser
* Page transitions don’t feel like they block on the network. Every time you tap a link/button, the app should be transitioning immediately or displaying a loading indicator while the app waits for a response from the network.
* Each page should have a URL — we should be able to create URLs for sharing. This is mainly meant to be applied for single-page-apps to ensure the client-side router is able to re-construct the app state from a given URL.

### Bonus - quicker first load in Angular

Do you plan on making your app really big? Do you want it to render its app shell immediately while having all Angular components loaded in the background? In fact, with bigger apps, you might get a warning in the report saying that the first load takes too much time.

To make things fast, just add a static `HTML` code into the root Angular component file. This HTML will be shown during initialization. In the commit link below, you can see that I’ve also thrown in a few static styles to make things render in one go.

```
..<app-root>    <header class="static" style="width: 100%;        height: 56px;        color: #fff;        background: #1e88e5;        position: fixed;        box-shadow: 0 4px 5px 0 rgba(0, 0, 0, .14), 0 2px 9px 1px rgba(0, 0, 0, .12), 0 4px 2px -2px rgba(0, 0, 0, .2);        padding-left: 16px;        margin: auto;        z-index: 10000;">        <h2 style="font-size: 20px;">Pack and Go</h2>    </header>    <main style="padding-top: 60px;        flex: 1;        overflow-x: hidden;        overflow-y: auto;"></main></app-root>...
```

Below you can see the result when tested with the “Slow 3G” connection setting in place.

![Image](https://cdn-media-1.freecodecamp.org/images/b0fN53QRtod8uKy6bSGLYhdzZldy2hLS8LsM)

![Image](https://cdn-media-1.freecodecamp.org/images/Q5OWTluieGNAAtF22wXF1mKgMeb90kWr5uOr)
_[Add static app shell](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/8521c612e273fc91670a408488dc981ad7023895" rel="noopener" target="_blank" title=")_

### Closing lines

All right, we’re done! If you strive for an ultra-modern PWA app built on top of a robust framework, now you have it.

The app runs on the latest version of Angular, and is backed by a fast and [headless Kentico Cloud CMS](http://bit.ly/kc-home). It meets **all** the requirements of the Lighthouse audit tool made by Google.

If you’re interested in seeing how to incorporate the Lighthouse checks into your continuous integration ecosystem, just reach out to me over [Twitter](http://bit.ly/twitter-freecodecamp)!

