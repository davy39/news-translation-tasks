---
title: Things I Wish I Knew Before Working with Electron.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T19:11:55.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-from-electronjs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9abd740569d1a4ca276a.jpg
tags:
- name: Electron
  slug: electron
- name: JavaScript
  slug: javascript
- name: lessons learned
  slug: lessons-learned
- name: projects
  slug: projects
seo_title: null
seo_desc: 'By Alain Perkaz

  In this article, I''ll share how you can avoid some of the mistakes I made when
  learning about Electron.js ?‍♂️. I hope it helps!

  Note: This wont be a coding tutorial, but rather a discussion about my personal
  takeaways.

  A couple of mo...'
---

By Alain Perkaz

In this article, I'll share how you can avoid some of the mistakes I made when learning about Electron.js ?‍♂️. I hope it helps!

**Note**: This wont be a coding tutorial, but rather a discussion about my personal takeaways.

A couple of months back, I decided to focus more on building my side product, [_taggr_](https://taggr.ai/). I was inspired to build it because of how many photos I have on my computer. 

For those of us that keep a backup of their pictures, those collections often get so big and complex that they become a full-time job to manage. A mix of folders and sub-folders may contain instant messaging picture backups, hi-resolution pictures from your trip to Bali, your uncle's wedding, or last-year's bachelor party.

Always keeping such collections tidy is **tedious** (believe me, I have tried for years). It's also hard to discover the shots that you love the most, hidden deep within the folders. 

So [_taggr_](https://taggr.ai/) is a desktop app that solves that problem. It lets users **rediscover** their memories while keeping their **privacy**.

I am building _[taggr](https://taggr.ai/)_ as a cross-platform desktop application. Here I'll share some of the things I've learned about cross-platform app development with [Electron.js](https://www.electronjs.org/) that I wish I knew from the beginning. Let's get started!

## Background 

Before presenting my takeaways on this ongoing journey with Electron, I would like to give a little more background about myself and the requirements of [_taggr_](https://taggr.ai/).

Every developer comes from a different background, and so do the requirements of the applications they develop. 

Contextualizing the choices I made for this project may help future developers select the right tools based on their needs and expertise (rather than what is hyped out there – GitHub ?, I am looking at you).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/train.gif)
_JavaScript development in a nutshell. Source: [giphy](https://giphy.com/gifs/train-hype-FY2ew2Zii9VOE" rel="noopener)._

As mentioned earlier, from the beginning I envisioned [_taggr_](https://taggr.ai/) as a cross-platform application. The app would perform all the required pre-processing and machine-learning computations client-side due to the focus on privacy. 

As a one-person show, I wanted to be able to write my app once and ship it to different systems without losing my sanity.

From my side, I am a front end engineer in love with the web and JavaScript. I previously worked with Java and C#, but I enjoy the flexibility that the web provides and its vibrant ecosystem. 

Having experienced first hand the pain of using tools like [Eclipse RCP](https://wiki.eclipse.org/Rich_Client_Platform) to build client-side apps before, I knew I didn’t want to work with that tech again.

In short, my stack requirements for taggr boiled down to something like the following:

* It should provide **cross-platform support,** ideally at the framework level. ?
* It should allow me to **write the code once**, and tweak for each platform if needed. ?️
* It should enable **access to machine-learning capabilities**, regardless of the host environment, without specific runtimes to be installed. It should be painless to set up. ?
* If feasible, it should **use web technologies**. It would be great to leverage my existing knowledge. ?

As you can see, the requirements do not read as: **I should use React with Redux, observables, and WebSockets**. Those are lower-level implementation details, and they should be decided upon _when and if_ the need arises. 

Pick the right tool for the job rather than picking a stack from the beginning, disregarding the problems at hand.

So, after furious googling, I decided to give Electron a try. I hadn’t used that framework before, but I knew that many companies were using it successfully in products such as [Atom](https://atom.io/), [VS Code](https://code.visualstudio.com/), [Discord](https://discord.com/), [Signal](https://signal.org/#signal), [Slack](https://slack.com/) and more.

Open-source and with out-of-the-box compatibility with both the the JS and Node ecosystems (Electron is build using Chromium and Node), Electron.js was an attractive tool for the work at hand. 

I won't go too much into detail regarding the rest of the stack, as I repeatedly changed core parts (persistence and view layers) when needed, and it falls out of the scope of this article. 

However, I would like to mention [Tensorflow.js](https://www.tensorflow.org/js), which enables running training and deploying ML models directly in the browser (with WebGL) and Node (with C bindings), without installing specific runtimes for ML in the host.

So back to Electron – thinking it was perfect, the fun began. ??

Enough talk about the background. Let’s dive into the takeaways.

## 1. Start small (and slow) ?

This is not a new concept, but it's worth bringing up periodically. Just because there are a ton of awesome [starter projects](https://github.com/sindresorhus/awesome-electron#boilerplates) with Electron available, it doesn’t mean that you should pick one right away.

**Wait. What?**

> Slow is smooth, and smooth is fast. — Navy saying

### With convenience comes complexity

While those starters include many useful integrations (Webpack, Babel, Vue, React, Angular, Express, Jest, Redux), they also have their issues. 

As an Electron newbie, I decided to go for a lean template that included the basics for ‘creating, publishing, and installing Electron apps’ without the extra bells and whistles. Not even Webpack in the beginning.

I recommend starting with something similar to [electron-forge](https://www.electronforge.io/) to get up and running quickly, You can set up your dependency graph and structure on top to learn the ropes of Electron. 

When the issues come (and they will), you will be better off if you build your custom starter project rather than picking [one](https://github.com/electron-react-boilerplate/electron-react-boilerplate/blob/master/package.json) with +30 npm scripts and +180 dependencies to begin with.

That said, once you feel comfortable with Electron’s basis, feel free to step up the game with Webpack/React/Redux/TheNextHotFramework. I did it **incrementally** and when needed. Don’t add a realtime database to your todo app just because you read a cool article about it somewhere.

## 2. Mindfully structure your app ?‍♂️

This one took a little longer to get right than I am happy to admit. ?

In the beginning, **it may be tempting to mix up the UI and Backend code** (file access, extended CPU operations), but things get complex quite fast. As my application grew in features, size, and complexity, maintaining one tangled UI+Backend codebase became more complicated and error-prone. Also, the coupling made it hard to test each part in isolation.

When building a desktop app that does more than an embedded webpage (DB access, file access, intensive CPU tasks…), I recommend **slicing the app into modules** and reducing the coupling. Unit testing becomes a breeze, and there is a clear path towards integration testing between the modules. For [_taggr_](https://taggr.ai/)_,_ I loosely followed the structure proposed [here](https://blog.axosoft.com/electron-things-to-know/).

On top of that, there is **performance**. The requirements and user expectations on this matter may vary wildly depending on the application that you are building. But blocking the main or render threads with expensive calls is never a good idea.

## 3. Design with the threading model in mind ?

I won’t go too much into detail here – I'm just mainly doubling down on what is awesomely explained in the [official docs](https://www.electronjs.org/docs/tutorial/performance).

In the specific case of [_taggr_](https://taggr.ai/), there are many long-running CPU, GPU, and IO intensive operations. When executing those operations in Electron’s main or renderer thread, the FPS count dips from 60, making the UI feel sluggish.

Electron offers several alternatives to **offload those operations from the main and renderer threads**, such as [WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Worker), [Node Worker Threads](https://nodejs.org/api/worker_threads.html), or [BrowserWindow](https://www.electronjs.org/docs/api/browser-window) instances. Each has its advantages and caveats, and the use case you face will determine which one is the best fit.

Regardless of which alternative you choose for offloading the operations out of the main and renderer threads (when needed), **consider how the communication interface will be**. It took me a while to come up with a interface I was satisfied with, as it heavily impacts how your application is structured and functions. I found helpfull to experiment with different approaches before picking one. 

For example, if you think WebWorkers message passing interface may not be the easiest to debug around, give [comlink](https://github.com/GoogleChromeLabs/comlink) a try.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/sponge.gif)
_Sponge Bob knows best. Source: [giphy](https://giphy.com/embed/jV4wbvtJxdjnMriYmY" rel="noopener)_

## 4. Test ❌, test ❌, and test ✔️

Old news, right? I wanted to add this as the last point, due to a couple of anecdotal ‘issues’ I recently faced. Strongly linked to the first and second points, building your custom starter project and making mistakes early on will save you precious debugging time further in the development.

If you followed my recommendations for splitting the app’s UI and Backend into modules with a clean interface between the two, setting up automated Unit and Integration tests should be easy. As the application matures, you may want to add support for [e2e testing](https://www.electronjs.org/spectron) too.

### GPS location extraction ?️

Two days ago, while implementing the GPS location extraction feature for [_taggr_](https://taggr.ai/)_,_ once the unit tests were green and the feature worked in development (with Webpack), I decided to try it in the production environment. 

While the feature worked well in development, it failed miserably in production. The EXIF information from the pictures was read as binary and processed by a third-party library. While the binary information was correctly loaded in both environments (checked with [diff](https://www.lifewire.com/compare-two-text-files-linux-3861434)), the third party library failed when parsing such data in the production build. Excuse me, ??

**Solution**: I found out that the encoding settings in the development and production environments set by Webpack were not the same. This caused the binary data to be parsed as UTF-8 in development but not in production. The issue was fixed by setting up the proper encoding headers in the HTML files loaded by Electron.

### Funky pictures ?

When manipulating and working with images, you may think that if a JPEG ‘just-works’ on your computer, it is a valid JPEG. **Wrong**.

While working with the Node image processing library [_sharp_](https://sharp.pixelplumbing.com/), resizing some JPEG images crashed the app. After looking closely, the cause was incorrect JPEG images generated by [Samsung firmware](https://github.com/lovell/sharp/issues/1578). ?‍♂️

**Solution**: setting up improved error boundaries in the app (ex. try-catch blocks), tweak the JPEG parsing module, and suspect of everything. ?️

## Summary

The Node and JavaScripts ecosystems are blooming, with many powerful tools being created and shared every day.

The amount of options makes it hard to choose a clear path to start building your new awesome Electron app. Regardless of your frameworks of choice, I would recommend focusing on the following:

1. **Start small** and add complexity incrementally.
2. **Mindfully structure your app**, keeping backend, and UI concerns modularized.
3. **Design with the threading model in mind**, even when building small apps.
4. **Test and test again**, to catch most of the errors early on and save headaches.

Thanks for sticking around until the end! ?

[_taggr_](https://taggr.ai/) is a cross-platform desktop application that enables users to **rediscover** their digital **memories** while keeping their **privacy**. Open-alpha is coming soon to Linux, Windows, and Mac OS. So keep an eye on [Twitter](https://twitter.com/TaggrOfficial) and [Instagram](https://www.instagram.com/taggrofficial/), where I post development updates, upcoming features, and news.

