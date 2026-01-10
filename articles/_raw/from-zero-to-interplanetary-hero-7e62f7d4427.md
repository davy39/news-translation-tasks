---
title: From Zero to Interplanetary Hero
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-21T18:53:56.000Z'
originalURL: https://freecodecamp.org/news/from-zero-to-interplanetary-hero-7e62f7d4427
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GGQAuJS_S0gonQc3goq0Vw.png
tags:
- name: Blockchain
  slug: blockchain
- name: dapps
  slug: dapps
- name: ipfs
  slug: ipfs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: "By Carson Farmer\nA fun guide to getting started with browser-based ĐApps\
  \ on IPFS\n\n_[â€œIf you can read this, congratulationsâ€”the archive youâ€™re using\
  \ still knows about the mouseover textâ€\x9D!](https://xkcd.com/1683/\" rel=\"noopener\"\
  \ target=\"blank\" ..."
---

By Carson Farmer

#### A fun guide to getting started with browser-based ĐApps on IPFS

![Image](https://cdn-media-1.freecodecamp.org/images/1*GGQAuJS_S0gonQc3goq0Vw.png)
_[â€œIf you can read this, congratulationsâ€”the archive youâ€™re using still knows about the mouseover textâ€!](https://xkcd.com/1683/" rel="noopener" target="_blank" title=")_

[ĐApps](https://en.wikipedia.org/wiki/DAPP), or decentralized apps, are all the rage right now, particularly over on the [Etherium blockchain](https://www.ethereum.org/). But did you know that ĐApps can also run on the [Interplanatary File System (IPFS)](https://ipfs.io/)? You bet, and it’s a lot easier than you might think to get one up and going quickly.

In this post, we’re going to go through the steps required to get an IPFS-based ĐApp going quickly, and easily. We’re going to take advantage of some cool new [IPFS browser tools](https://blog.ipfs.io/35-ipfs-companion-2-2-0/#hn2), and my favorite online comic. In doing so, we’re going to help archive a precious resource ([xkcd](https://xkcd.com/)!) for future visitors. So this post has it all: intrigue, excitement, and a commitment to the future of the web!

### Archiving the gems of the web

The goal for this tutorial is to create a distributed web ‘clone’ of the [xkcd website](https://xkcd.com/). We’re going to use IPFS to fetch images from an archive of xkcd comics, and display them in a form familiar to fans of xkcd.

There are several reasons why we might want to do something like this. One, I like xkcd comics, and am always looking for an excuse to play around with them. Two, xkcd, along with several other archived resources, are available via [the IPFS archives](https://archives.ipfs.io/), which make them a handy example. Three, and this one is important, building content-based ĐApp on top of IPFS can help to archive the web!

What do I mean by that? Well, trends change, interests wain, and the Internet is a fickle place. Couple this with the increasing costs of maintaining servers, updating infrastructure, and keeping up with the latest trends, and you’ve got a recipe for dead links. IPFS and the distributed web is a great way to help combat [link rot](https://en.wikipedia.org/wiki/Link_rot).

Take our xkcd ĐApp for example. In a moment, we’re going to write some very simple JavaScript that will load a random xkcd comic each time our ĐApp is accessed. And so every time someone visits the ĐApp, the peer running in their browser fetches that comic, and temporarily caches that item, making it possible for others to retrieve it as well. In fact, the more we use the ĐApp, the better it is able to distribute and archive xkcd.

> The more we access and use things on the distributed web via IPFS, the more likely they are to stick around long-term — [tweet it](https://twitter.com/home?status=The%20more%20we%20access%20and%20use%20things%20on%20the%20distributed%20web%20via%20IPFS,%20the%20more%20likely%20they%20are%20to%20stick%20around%20long-term%20-%20%40carsonfarmer%20https%3A//medium.com/%40carsonfarmer/from-zero-to-interplanetary-hero-7e62f7d4427)

This is a really powerful idea: the more we access and use things on the distributed web via IPFS, the more likely they are to stick around long-term. And what about things that are important but less _popular_ (like historical documents)? This is where things like [Filecoin](https://filecoin.io/) will help to pick up the slack. In the [filecoin world](https://coincentral.com/filecoin-beginners-guide-largest-ever-ico/), rather than relying on popularity to preserve documents and files, you can pay the network to store these things for you. It’s a very cool idea.

### Getting started

For those of you who can’t wait, the full ĐApp is available from the [Textile GitHub repo](https://github.com/textileio/xkcd-dapp-demo). Feel free to clone that, and follow along with the code to make getting started easier. And since you’ve just saved yourself some time, why not [watch this great video](https://www.youtube.com/watch?v=HUVmypx9HGI) on the IPFS vision by Juan Benet before moving on. You can also check out a [‘live’ version here](https://ipfs.carsonfarmer.com/ipfs/QmYDEzjNKm6ZMCmQVVRAJqPnGL2H7c4EK81LBTK3GC4kCh/).

For those of you who want a step-by-step approach, here are a few setup steps to get you started.

First, clone our vanilla IPFS [Dapp Template](https://github.com/textileio/dapp-template), and change into the new directory:

```
git clone https://github.com/textileio/dapp-template.git xkcd-dappcd xkcd-dapp
```

This template is pretty simple, and has fairly minimal [dependencies](https://github.com/textileio/dapp-template/blob/carson/xkcd-demo/package.json). Most of the dev dependencies are just for transpiling JavaScript so that we can run our ĐApp in the browser. For details on all those packages, refer to their respective GitHub repos, or [get in touch](https://www.textile.io/) to ask a question or two.

So first things first, check out the `README.md` file from the repo. You’ll notice it says this app works best with `window.ipfs`, and that you can install the [IPFS Companion](https://github.com/ipfs-shipyard/ipfs-companion) web extension by clicking on one of the links.

The IPFS Companion is a browser extension that simplifies access to IPFS resources by running a [JavaScript IPFS peer](https://github.com/ipfs/js-ipfs) in your browser. Even better than this, it can expose an embedded IPFS node as `window.ipfs` on every webpage! This makes it possible for our ĐApp to detect if `window.ipfs` exists and opt-in to use it instead of creating our own one-off `js-ipfs` node. It is not _required_ for running ĐApps, but it does make them run better (faster), and I highly recommend installing it.

But, we can’t expect the users of our ĐApp to install a browser extension before being able to use our ĐApp. So there is a nice JavaScript module called `[window.ipfs-fallback](https://github.com/tableflip/window.ipfs-fallback)`, which will detect the presence of `window.ipfs` and automatically fall back to downloading the [latest version of IPFS](https://unpkg.com/ipfs/dist/index.min.js) from the CDN if it’s unavailable. So when building a ĐApp, it’s always a good idea to include this — and you get `window.ipfs` for free if available. Nice!

Ok, so just to make sure things are working nicely, let’s go ahead and install our required dependencies, and build and run our ĐApp locally. Enter the following into your terminal:

```
yarn installyarn buildyarn start
```

You should see a pretty minimal (blank page) ĐApp with a footer and not much else. Now go ahead and open your Javascript developer console (Chrome:Ctl+Shift+J(Command+Option+Jon Mac), Firefox: Ctrl+Shift+K(Command+Option+Kon Mac), Safari: Command+Option+I). You should see something like `running js-ipfs/0.29.2 with ID Qm{hash}` where `Qm{hash}` is a long alphanumeric hash that represents your peer id.

Congrats, you are successfully running a ĐApp on the decentralized web! Now let’s make it do something interesting…

### Fetching data on the distributed web

Ok, let’s add some functionality to our ĐApp. We’ll start by simply fetching a random xkcd comic and displaying it on a blank page. Simple enough right? First, rather than `yarn start`ing our app, let’s `yarn watch` it so that any changes we make to the JavaScript will automatically be reflected when we refresh our browser window.

Now, you can go ahead and modify the `setup` function in `src/main.js` with the following code:

There’s a lot to parse there, but basically what is happening is:

* Lines 3 & 5 are defining _which_ random comic to fetch ([from our archive](https://ipfs.io/ipfs/QmWEAXcqwq5zY2u8Z1mii5m3MXricctd7efFep7sSEWZQz))
* Lines 8 & 10 are initializing an IPFS peer node, and connecting to a peer known to be pinning the xkcd archive (this second step isn’t always required, but I added it here to help bootstrap the ĐApp)
* Line 14 is really the IPFS ‘magic’…it is fetching the files at the given CID and returning a promise, which we await and then do some work with in lines 15 to 27…
* Lines 15 & 16 simply loop through the binary objects returned from the previous step, and look for the actual png image
* Lines 18 & 20 convert the binary image data to a base64 encode string
* And finally, lines 22 through 27 create an image element and add it to the ‘main’ div for display.

Done!

### Cleaning things up

From here, any additional changes are simply to make the ĐApp look and feel more like the original xkcd comic webpage.

I won’t go into the details in this post, but you can take a look in the [xkcd-dapp-demo](https://github.com/textileio/xkcd-dapp-demo) repo for the full code example. There, I’ve added the nav buttons and styling from the xkcd website, along with some links to [proper attribution](https://ipfs.io/ipfs/QmWEAXcqwq5zY2u8Z1mii5m3MXricctd7efFep7sSEWZQz/about.html), [license information](https://ipfs.io/ipfs/QmWEAXcqwq5zY2u8Z1mii5m3MXricctd7efFep7sSEWZQz/license.html), and other goodies. We even have the fun hover comments! It’s almost all vanilla ES6 JavaScript, and I take good advantage of [async/await patterns](https://davidwalsh.name/async-await) to make the code nice and readable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2DSOGJ4sBp5Njb7hN3RF_Q.png)

So as you can see, it is relatively easy to get started making ĐApps on IPFS. Our xkcd ĐApp works best when run a) locally (via `yarn start` for example), and b) with the IPFS Companion browser extension enabled. If you want, you can actually fire up a local IPFS daemon, and run `ipfs add -r dist/`, to add the whole ĐApp to IPFS. Now, you can test it through your local IPFS gateway: `http://localhost:5001/ipfs/Qm{hash}/`(if your code isn’t identical to mine, your CID hash might differ, use the one output from the above `ipfs add` command).

### Wrapping up

We hope that [our template](https://github.com/textileio/dapp-template) will provide a quick and easy means to bootstrap additional ĐApps, and that the community of IPFS-based ĐApps will continue to grow. At [Textile](https://www.textile.io/), we’d really like to support a community of ĐApps around IPFS, so if you decide to use our template, let us know, and we’d be happy to add a link to [our template repo](https://github.com/textileio/dapp-template/blob/master/README.md). We’ll also keep an eye out for forks and try to promote them as best we can.

We hope you enjoyed our quick introduction to ĐApps on IPFS. If you enjoyed this, come [check us out](https://www.textile.photos/) and learn more about what we’re up to. While you’re at it, jump on the [Textile Photos waitlist](https://www.producthunt.com/upcoming/textile-photos) to request early access to a whole new way to control your photos, that also runs on IPFS and the permanent web.

