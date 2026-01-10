---
title: How Gatsby is so blazing fast
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-01T17:49:37.000Z'
originalURL: https://freecodecamp.org/news/how-gatsby-is-so-blazing-fast-c99a6f2d405e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rcK0xeuBYK_yTArHwNJh5Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Luan Orlandi

  Performance greatly affects the user experience. Gatsby builds fast websites out-of-the-box.

  When creating the tool, they noticed that slow websites are slow in different ways,
  but fast websites are fast in similar ways. So baking opt...'
---

By Luan Orlandi

Performance greatly affects the user experience. Gatsby builds fast websites out-of-the-box.

When creating the tool, they noticed that slow websites are slow in different ways, but fast websites are fast in similar ways. So baking optimization approaches in a framework resulted in Gatsby.

From my experience, Gatsby set up [webpack](https://webpack.js.org/) to build the most optimal performance. Webpack is a module bundler for JavaScript used by many front-end projects.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bMLE3-PipX9X0N7eCHIGow.png)
_A big community develops Gatsby on GitHub, also contributing to the [logo design](https://github.com/gatsbyjs/gatsby/issues/408#issuecomment-245861049" rel="noopener" target="_blank" title=")._

### Blending static websites with dynamic apps

Gatsby is a static website generator that uses React. It creates HTML files for each page your website has.

So when building your website, Node.js will mount the React application to create HTML files with the rendered content for each route. This is the core of Gatsby.

> “ Instead of waiting to generate pages when requested, Gatsby pre-build pages” — [gatsbyjs.org](https://www.gatsbyjs.org/)

Let’s go back in the basics to see why this is important for performance.

When the user accesses a page through an HTML file, the browser renders the content. Without any cache or JavaScript, using an anchor tag will load another HTML file when clicked. As a result, the user might have to wait or worse, see a blank page while rendering the content.

This is the most traditional way that the Web was designed until Single Page Applications (SPA) came up.

SPA renders the page by updating the content with JavaScript. It’s much faster to update than downloading static files. Because they load a single HTML file and dynamically update that page as the user interacts.

React is a library to handle the view layer for SPA. Such frameworks and libraries like React doesn’t know what to render unless some JavaScript code starts running. So building them as SPAs will drastically affect the [Critical Rendering Path](https://calendar.perfplanet.com/2012/deciphering-the-critical-rendering-path/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*aAoiF2OcphAPg8DoYwXqpA.png)
_Critical Rendering Path stalls the render while loading and executing JavaScript._

Gatsby has a webpack configuration to provide enough content for the first render:

* **HTML** tags
* **JavaScript** code set as [async](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#Attributes), necessary for user interaction but not for the first render
* **CSS** as inline, so no need to download them

### Code split and cache

When building a page, Gatsby can see which components the page needs and let webpack do code splitting automatically. This is applied by setting up [Dynamic Imports](https://webpack.js.org/guides/code-splitting/#dynamic-imports).

Through this way, the browser will only request files required for the page, not the entire website, speeding up the time to interact with the page.

As a result, links to other pages will download their files only when the user interacts with the link, slowing navigation.

To avoid this problem, the webpack configuration of Gatsby applies a technique called [Link prefetching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Link_prefetching_FAQ).

After the browser is finished loading the page, it silently looks for links with prefetch attributes to download them. Then, when a user clicks on a link, the files requested for the page will have high chances to be already in cache.

### Every page is a React app

Navigating through pages in a static website still requires a load of HTML files, but not for Gatsby — they are React apps.

> “Gatsby generates your site’s HTML pages, but also creates a JavaScript runtime that takes over in the browser once the initial HTML has loaded” — gatsbyjs.org

Each anchor tag for another page will become a route by [Reach Router](https://reach.tech/router) (a tool for building routes on React with accessibility). It looks like it’s changing from one HTML file to another when in fact, it’s a SPA updating the content on the page.

### Image optimization

[HTTP Archive](https://httparchive.org/) tracks a lot of popular websites, most of the data types requested by pages are images.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ymIv-FahsytuypmNU560UQ.png)
_[transfer size](https://httparchive.org/reports/page-weight#bytesTotal" rel="noopener" target="_blank" title="">Total Kilobytes</a> — The sum of <a href="https://www.w3.org/TR/resource-timing-2/#dom-performanceresourcetiming-transfersize" rel="noopener" target="_blank" title=") of all resources requested by the page is around 1285.5 KB for mobile._

![Image](https://cdn-media-1.freecodecamp.org/images/1*AyrHOyvvLoTQAoBzRyBP-A.png)
_[Image Byte](https://httparchive.org/reports/page-weight#bytesImg" rel="noopener" target="_blank" title=")s — The sum of transfer size of all external images requested by the page is 491.0 KB for mobile._

Optimizing images can be one of the best performance improvements on a website.

Fewer bytes to download means less bandwidth required, so the browser can download and render content faster. These are some of the optimizations we can do:

* Resize to the same amount of space it needs
* Generate [responsive images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images#How_do_you_create_responsive_images) with different resolutions for desktop and phones
* Remove metadata and apply compression
* Apply lazy loading to speed up the initial page load
* Display a placeholder while the image is loading

This can take a lot of effort and Gatsby has a solution: this whole process can be automated.

Like many tools in Gatsby, [gatsbyjs-image](https://www.gatsbyjs.org/packages/gatsby-image/) is powered by GraphQL. This plugin sets up the images with different resolutions for download. It creates some thumbnails and applys compression. All this on the building step.

When the image is loading, a “blur-up” technique displays a preview in a very low-quality image that is already in the HTML file (or just the background). All the work is reduced in coding GraphQL queries to create the automated optimization. Check out this demo:

![Image](https://cdn-media-1.freecodecamp.org/images/1*NtTh_CL3BXESFTWvMfzR9w.gif)
_[Demo from Gatsby](https://using-gatsby-image.gatsbyjs.org/" rel="noopener" target="_blank" title=") for optimized performance with images. The “blur-up” technique is also used by Medium._

### Minification and unique filenames

These techniques are already widely used by popular frameworks and libraries, and in Gatsby there is not much difference.

[All files are minified](https://webpack.js.org/guides/production/#minification) by default when building with webpack. Because browsers don’t care about beautiful code, so why not write everything in one line?

The files are unique when built by assigning a hash on the filename. If something changes, a new name is given for the file.

The reason behind this is to allow the server that hosts these files to give a long duration for browser caching.

So when the user comes back for the website, they already have the files. Updates in your files will give a new filename when built. So the browser downloads the file because there will be no match with the one from the cache.

### More resources and beyond

Gatsby cares about performance optimization so that you don’t need to.

If you are more curious about how Gatsby works under the hood, check out the [documentation](https://www.gatsbyjs.org/docs/behind-the-scenes/).

I also recommend this webinar from the Gatsby team, [Behind the Scenes: What makes Gatsby Great](https://www.gatsbyjs.com/behind-the-scenes/).

I am teaching [Gatsby on Udemy](https://www.udemy.com/gatsby-crie-seu-site-pessoal/) and worked in the development of a [company’s website](http://upx.com) with Gatsby, as well my [personal website](http://luanorlandi.github.io).

**I am teaching and spreading how awesome Gatsby is. [Follow me on twitter](https://twitter.com/luanorlandi) to read more topics about tech and Gatsby.**

