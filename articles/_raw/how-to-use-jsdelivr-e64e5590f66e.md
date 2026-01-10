---
title: How to use JSDelivr
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-04-08T15:54:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-jsdelivr-e64e5590f66e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q1qvRLnBI5meBDrgpZW-BQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Easily download JavaScript libraries from npm and GitHub

  The most newbie-friendly way to add a library to a project is to:


  Search for the library

  Look for the source file

  Copy the source file

  Paste what you copied into the project.


  This works, but ...'
---

#### Easily download JavaScript libraries from npm and GitHub

The most newbie-friendly way to add a library to a project is to:

1. Search for the library
2. Look for the source file
3. Copy the source file
4. Paste what you copied into the project.

This works, but it’s a painful process. It’s easier if you use CDNs like JSDelivr.

### What is a CDN?

CDN stands for content delivery network. Its main purpose is to let users download files faster. Read [this article](https://www.fastly.com/blog/why-you-should-use-content-delivery-network) by Fastly if you’re wondering whether you should use a CDN.

CDNS let users download files faster by placing datacenters all over the world. When the browser sees a CDN link, they’ll serve up the library from the datacenter closest to the user. This is how CDNs work.

### What is JSDelivr?

JSDelivr is a special kind of CDN. It’s built to let users download JavaScript libraries that are hosted on npm and Github. (You can also load Wordpress plugins if they’re hosted on Wordpress.org).

If you use JSDelivr (or any other CDN that serves JavaScript libraries), you don’t need to copy-paste the source files into your project. You can use a link like this:

```
<script src="https://cdn.jsdelivr.net/npm/package-name"><;/script>
```

JSDelivr lets you specify the version of a library you want to download. If you want to specify a version, you add the version number after an `@`, like this:

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]"><;/script>
```

### How I use JSDelivr

**I use JSDelivr more like a package manager** since JSDelivr lets you specify the version of a library. I can upgrade or downgrade the library by changing a number. There’s no need to copy-paste the original source into my project.

However, **I rarely use JSDelivr nowadays** because I already have a build process that uses Webpack. Webpack lets you `require` libraries into frontend JavaScript. It lets you use npm as a package manager.

**I only use JSDelivr for projects that:**

1. Require a library
2. The library exists on JSDelivr (or other CDNs)
3. The project doesn’t have Webpack (or similar tools installed)

One example of such a project is the 20 components in [Learn JavaScript](https://learnjavascript.today/).

Here’s why.

Students who’re enrolled in Learn JavaScript are trying to learn JavaScript. I don’t want to distract them by making them learn Webpack.

Instead, I want to help them focus on what they’re here for — learning JavaScript. I do this by removing complexity from projects we build together. I strip everything down to plain old HTML, CSS, and JavaScript.

We’ve talked about what is JSDelivr, why use it, and when to use it. Let’s dive into the details of using it now.

For the rest of the article, we’ll use a library called [zl-fetch](https://github.com/zellwk/zl-fetch) as an example.

### Installing a library

To install a library, you need to add a `<scri`pt> tag that points to the library on JSDelivr. You can load the library from npm or Github, depending on your preferences.

I tend to load libraries from npm.

```
<script src="https://cdn.jsdelivr.net/npm/package-name"><;/script>
```

You need to change `package-name` to the name of the library you’re installing. In this case, it’s `zl-fetch`.

```
<script src="https://cdn.jsdelivr.net/npm/zl-fetch"><;/script>
```

If you’re unsure of the name of the library, you can search on [npm](https://www.npmjs.com/), or directly on [JSDelivr](https://www.jsdelivr.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/CndXOzCC03uVBwhf73T-AjP5qZxSjOLKzH4F)

### Specifying a version

By default, JSDelivr downloads the latest version of a library.

I don’t recommend you use the latest version because authors may update their library. If they update their library, your code may break.

**You always want to specify a version number.** You can add a version number by adding `@`, followed by the version number after the package name, like this:

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]"><;/script>
```

**Version numbers follow a [Semver](https://zellwk.com/blog/semantic-versioning/) format.** You can tell what versions are available by checking the available tags on Github.

![Image](https://cdn-media-1.freecodecamp.org/images/DvX7KL57jCAeQmDTJLSuhyMjtGTlyabzYuPv)

In our case, the current version of `zl-fetch` is `2.1.9`:

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]"><;/script>
```

### Loading a specific file

JSDelivr relies on authors to specify a default file for the above format to work. **If the default file is not specified, you need to point to the correct file.**

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]/path-to-file"><;/script>
```

There are two ways to know what files are available.

First, you can search for the package on JSDelivr. You’ll see a list of files and folders you can point to:

![Image](https://cdn-media-1.freecodecamp.org/images/mK4mbrhilqZjV1wau0pffsmFst5cQXWIug0n)

Second, if you know about npm, you can use npm to install the package somewhere on your computer. Then use your Finder (or Explorer) to browse through the files.

In this case, let’s say the default file is not specified, and we want the `dist/index.js` file. Here’s what you’ll write:

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]/dist/index.js"><;/script>
```

### Loading a minified version

Minified files are usually smaller in size. Users will be able to download the minified files faster than an unminified file.

JSDelivr minifies files automatically if you use the `.min.js` extension.

```
<script src="https://cdn.jsdelivr.net/npm/[email protected]/dist/index.min.js"><;/script>
```

### Wrapping up

I hope this article gives you a good overview of what JSDelivr can do.

Thanks for reading. Did this article help you out? If it did, I hope you consider [sharing it](https://twitter.com/share?text=How%20to%20use%20JSDelivr%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/jsdelivr/). You might help someone else out. Thanks so much!

This article was originally posted at [_my blog._](https://zellwk.com/blog/jsdelivr)  
Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.

