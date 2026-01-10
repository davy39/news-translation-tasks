---
title: A Quick Look at Bun 1.0 – The Node.js Alternative
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-09-15T07:58:01.000Z'
originalURL: https://freecodecamp.org/news/a-quick-look-at-bun-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/But-why-is-that-relevant--2-.png
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: null
seo_desc: 'By Nishant Kumar

  A wise man once told me, "When you start eating Bun, Node.js will feel bland".

  But why is that relevant? JavaScript got way faster with a new JavaScript runtime
  called Bun, which is now production-ready with its version 1.0 release.

  ...'
---

By Nishant Kumar

A wise man once told me, "When you start eating Bun, Node.js will feel bland".

But why is that relevant? JavaScript got way faster with a new JavaScript runtime called Bun, which is now production-ready with its version 1.0 release.

But how and why is it faster than Node.js? A lot of questions come to mind.

I'll answer some of those questions in this article. And I'll do that quickly as I am now faster just like my pal, JavaScript, cooking in the oven with Bun 1.0.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/But-why-is-that-relevant--3-.gif)

Bun is a fast, all-in-one toolkit for running, building, testing, and debugging JavaScript and TypeScript, from a single file to a full-stack application.

Here are some things we can do with Bun.

## Run your Code Faster with Bun

Now, we don’t need tools like `npm`, `pnpm`, or `yarn` because Bun is 17 times faster. Take a look at the data below:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/266451126-23cbde35-b859-41b5-9480-98b88bf40c44.png)

Bun takes only 0.36 seconds to compile your code, whereas it takes about 6.44 seconds in the case of pnpm, 10.58 seconds with npm, and 12.08 seconds with yarn.

## Bun Supports Hot Reloading

Bun supports hot reloading out of the box so you don’t need tools like Nodemon. It will automatically refresh the server when running JavaScript or TypeScript Code.

You can replace `npm run` with `bun run` to save over 150ms milliseconds every time you run a command.

Here is the full chart:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-2023-09-14-at-7.17.45-PM-1.png)

From the chart above, using `npm` takes about 176ms to run, `yarn` takes about 131ms. In the case of `pnpm`, it takes 259ms. However, it takes about 7ms in the case of `Bun`. That's fast, isn't it?

## Bun as a JavaScript Bundler

Bun is also a JavaScript bundler with best-in-class performance and an ESBuild-compatible plugin API, so we don’t need things like:

* ESBuild
* Webpack
* Parcel, .parcelrc
* Rollup, rollup.config.js

![Image](https://www.freecodecamp.org/news/content/images/2023/09/But-why-is-that-relevant--2-.gif)

Bun now supports Next.js, Remix, Nuxt, Astro, SvelteKit, Nest, SolidStart, and Vite.

### Bun has both ESM and CommonJS Compatibility

Another great feature about Bun is that we can use ES Modules and CommonJs together in the same file, which was not possible in Node.js.

You can use `import` and `require()` in the same file:

```javascript
import lodash from "lodash";
const _ = require("underscore");
```

Apart from that, Bun has built-in support for the Web standard APIs that are available in browsers, such as `fetch`, along with extra Bun APIs like `Bun.file()` to lazy read a file and `Bun.Write()` to write a file to the local file system which is a lot simpler than Node.js.

#### `Bun.file()` Example

```javascript
const file = Bun.file("package.json");
const contents = await file.text();
```

The code above will read the contents of a `package.json` file and transfer its content to a new variable called `contents`. 

#### `Bun.write()` Example

```javascript
await Bun.write("index.html", "<html/>");
await Bun.write("index.html", Buffer.from("<html/>"));
await Bun.write("index.html", Bun.file("home.html"));
await Bun.write("index.html", 
await fetch("https://example.com/"));
```

In the code above, `Bun.write()` will write the string `"<html/>"`, or copy the contents of `home.html` file into the `index.html` file. If we have to fetch data, it will fetch the results from an external web API and write the contents to a `index.html` file.

## Why is Bun so fast?

Bun is fast because it uses the JavaScriptCore engine, while Node.js uses the JavaScript V8 engine. The former has been optimized for faster startup time.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/But-why-is-that-relevant.png)

If you want to get things done faster, you should consider replacing Node.js with Bun.

## How to Get Started With Bun

You cam install Bun on MacOS and Linux systems using npm:

```javascript
npm install -g bun
```

Now you are all set. To install a npm package, do this:

```javascrpt
bun install <package-name>
```

To start a Next.js app, do this:

```javascript
bun run dev
```

All you need to do is replace `npm` with `bun`.

However, Bun is only ready for production in MacOS and Linux operating systems. The Windows version is still experimental. At the moment, only the JavaScript runtime is supported for Windows, and not the package manager, the bundler, or the test runner. You can read more about that [here](https://bun.sh/docs/installation#windows).

## Conclusion

This article shows how you can use Bun as a Node.js alternative and speed up your development time.

You can also check out my video on **[The Node.js killer is here — Bun 1.0 First Look](https://youtu.be/q5UKY_dCmh4?si=satm6TAv6Zmh5OCn)**.

Thanks for reading!

