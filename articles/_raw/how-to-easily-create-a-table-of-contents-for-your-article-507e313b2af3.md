---
title: How To Easily Create a Table Of Contents For Your Article
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T00:24:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-create-a-table-of-contents-for-your-article-507e313b2af3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Bg43TmnKj37GvTiX8vHZCg.png
tags:
- name: medium
  slug: medium
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
- name: writing tips
  slug: writing-tips
seo_title: null
seo_desc: 'By Adam Kelly

  In this article, I’ll discuss how you can create a table of contents for your Medium
  post, and I’ll show you how I built the feature.

  Table of Contents


  Get The URL

  Generate Your Table Of Contents

  Design

  Development

  Get the source


  Many...'
---

By Adam Kelly

In this article, I’ll discuss how you can create a table of contents for your Medium post, and I’ll show you how I built the feature.

#### Table of Contents

* [Get The URL](https://medium.com/p/507e313b2af3#e2d0)
* [Generate Your Table Of Contents](https://medium.com/p/507e313b2af3#b4b8)
* [Design](https://medium.com/p/507e313b2af3#d9a8)
* [Development](https://medium.com/p/507e313b2af3#dca5)
* [Get the source](https://medium.com/p/507e313b2af3#696e)

Many of you have probably seen [this post](https://medium.freecodecamp.org/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549) about how to link to parts of your Medium article. You may have also seen [this chrome extension](https://medium.com/@castroalves/medium-anchor-a-must-have-chrome-extension-for-bloggers-c45dfdc6b91e), which makes the process simpler.

Well, you can do one better. This is how to create a table of contents for your Medium article, automatically.

### 1. Get The URL

First, you need the URL of your Medium article. If it has been published, just grab the link from your address bar

![Image](https://cdn-media-1.freecodecamp.org/images/FbUV0O6cwmoi23LHvzz2NrKX2MuiSju8xMVQ)

If you are still writing, click the “share” button in the top right corner, and copy the link from there

![Image](https://cdn-media-1.freecodecamp.org/images/VaWdhwfh2lPCB8GLINgsV4G4dgYpvVl9akgK)

### 2. Generate Your Table Of Contents

Now the easy bit. Go to [www.mediumtoc.com](https://www.mediumtoc.com) and paste your URL in the input bar, and click “go.”

![Image](https://cdn-media-1.freecodecamp.org/images/SeFydbL76uBcTWxPJBlP0hmWot5mc6li8H2f)

Then it should give you your contents, which you can copy and paste into your medium article!

![Image](https://cdn-media-1.freecodecamp.org/images/eEoCmfNhuAvDpM1-72E5vu6ZJ42NpZAPsU1w)

You can see this in action at the top of this post.

### How I Built This

#### Design:

I first designed the website in [Sketch](https://www.sketchapp.com/). I chose to take some design cues from the Medium website, with a serif font for the heading, and I also used the same button design.

I chose to use a [https://material.io/guidelines/components/text-fields.html](https://material.io/guidelines/components/text-fields.html) input bar, as the design is functional and minimalistic, the style I was going for.

#### Development:

The architecture of this app is largely based on the [JAM stack](https://jamstack.org/). This is based on the idea of having client side Javascript, reusable API’s, and prebuilt markup. It allows sites to go on CDNs.

The sites architecture is:

**Front End:** [React](https://reactjs.org/) and [Preact](https://preactjs.com/) (a lightweight virtual DOM implementation) in production

**Back End:** Express running on [Now](https://zeit.co/now), although I plan to migrate to AWS Lambda, as there is only 1 API endpoint. The back end scrapes the headings from the Medium article and returns their links.

**Front End Hosting / CDN:** The site runs on [Netlify](https://www.netlify.com/), which has free SSL integration, and automatically deploys from the master branch on GitHub.

If anyone is interested in any of these topics, leave a comment and I will write more about them!

The website was designed and developed over the course of two days. The first day was focused on the back end of the site, and the design. The second day was the development. There are only 4 react components, and I chose not to use redux, as there is not very much changing in the state.

#### Get the source!

This is open source, so you can get all the code on [github.com/adamisntdead/medium-toc](https://github.com/adamisntdead/medium-toc). ✨

Big thanks to the freeCodeCamp community for their wonderful [publication](http://medium.freecodecamp,com)!

### If you liked this article, please leave an applause! ? Want more articles like this? F[ollow me.](http://medium.com/@adamisntdead/)

