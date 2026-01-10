---
title: How to Bypass ES Modules Errors in Next.js with Dynamic Imports
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-19T19:58:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-bypass-es-modules-error-in-next-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/tim-gouw-1K9T5YiZ2WU-unsplash.jpg
tags:
- name: error handling
  slug: error-handling
- name: ES6
  slug: es6
- name: modules
  slug: modules
- name: Next.js
  slug: nextjs
seo_title: null
seo_desc: 'By Caleb Olojo

  When you are building an application that can be accessed on the web, there are
  a lot of dependencies or packages that you will need for your application to function
  well.

  You''ll need most of these packages when you''re building JAMStac...'
---

By Caleb Olojo

When you are building an application that can be accessed on the web, there are a lot of dependencies or packages that you will need for your application to function well.

You'll need most of these packages when you're building JAMStack applications with frameworks or libraries like React, Vuejs, Next.js, or Angular.

In this article, I'll walk you through an error you may get when you are building JavaScript apps with Next.js, and how to bypass it.

## What the Heck are ESModules?

ESModules are the ECMAScript standards for working with JavaScript modules in the browser.

"What does that have to do with these annoying and frustrating errors that I have been seeing for the past few days?" you might ask me.

Well... Node.js has been using the **CommonJS** standards for a very long time to properly structure JavaScript code or modules in this scenario, and the majority of the code we write resides/works in the browser.

There were no standards to properly guide how JavaScript modules were used, or interpreted, at least in web browsers. This challenge brought about the ESModules standards which guide how JavaScript modules work in the browser.

This standard was approved when ES6 (ECMAScript 6) was launched in 2015, and brought about the implementation of the standards in various web browsers like Chrome, Safari, Firefox, and Microsoft's Edge.

Most of the packages we use in building frontend UIs are written in JavaScript. They have modules that are exporting a particular function (it could be a JavaScript component), an object, a string, a bunch of arrays, and so on.

These functions, arrays, or strings can be exposed as libraries to other JavaScript files. Say, for example, we have a function that prints the name of anyone in the console. The syntax will be like this:

```js
// name.js
export default (name) => console.log(name)

```

The snippet above describes a default export, without a specific name. This means that if we want to use the function in this module, we can call it any name, since a name wasn't explicitly assigned to it upon declaration

```js
import printName from "./name.js"

printName("Dodo")

```

## Okay, why do I still get the error though?

Yes. Now on to that error. When we begin to interface with a lot of dependencies or packages in our applications, some things might start going wrong if we don't give proper care to our codebases.

We start to deal with versioning of these packages, breaking changes, and releases sometimes, which we can not keep track of. Then, we might begin to scurry down the rabbit hole of downgrading or upgrading a particular npm package before anything even works at all.

Most of these errors may arise from the maintainers of these packages. Take, for example, the ESModules standard – which is relatively new – that we are discussing in this article. It may take some time for it to be adopted by some frameworks or front-end JavaScript libraries out there, for example, Next.js.

The error in the image below shows that we can't use the CommonJS approach to import a module.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/serialize-1.png)

This new standard and the fact that it's a bit unfamiliar to these tools we use is the reason for this error. [Nirmalya Ghosh wrote this piece on how to maintain large Next.js apps](https://www.smashingmagazine.com/2021/11/maintain-large-nextjs-application/), you should take a look at it.

## How to use Next.js dynamic imports

Now that we've gone through the rudiments of what ESModules are, let's see how we can fix the error that is quite similar to the one we saw in the image above. We'll see how we can fix it with dynamic imports in Next.js.

I'll be assuming you already have a Next.js app running, so I'll just share the corresponding ESModule error I got from my terminal in the code block below:

```bash
Error [ERR_REQUIRE_ESM]: Must use import to load ES Module: /path/to/package

require() of ES modules is not supported. 

ES module file as it is a .js file whose nearest parent package.json contains "type": "module" which defines all .js files in that package scope as ES modules.

Instead rename index.js to end in .cjs, change the requiring code to use import(), or remove "type": "module" from /path/to/package

```

Take a look at the error above so that you're quite familiar with it. Once you've done that, let's proceed.

### What are dynamic imports?

Dynamic imports is a feature of Next.js that allows you to work with JavaScript modules conveniently in the browser.

It provides a means of pre-rendering these modules with SSR (Server-side Rendering) so that users do not need to send requests continuously to the server when they need — say, for example — a page that uses a JavaScript module. With dynamic imports, the modules are already pre-rendered in the browser.

Recently, I was working on a project that had to do with markdown content. I needed to use rehype plugins, but I kept on getting the error in the previous code block.

```js
const rehypeSlug = dynamic(() => import('rehype-slug'), { ssr: false })
const rehypeCodeTitles = dynamic(() => import('rehype-code-titles'), {
  ssr: false,
})
const rehypeAutolinkHeadings = dynamic(
  () => import('rehype-autolink-headings'),
  { ssr: false }
)
const rehypePrism = dynamic(() => import('rehype-prism-plus'), { ssr: false })

```

The snippet above shows how you can import a module with dynamic imports and pass the `ssr` object as an argument to it.

With this approach of using dynamic imports, the ESModule errors that kept on showing up were removed.

## Wrapping Up

So I hope you'll be able to make use of this feature, and I hope it liberates you from that error. 

There's a lot you have to think about when you're building JavaScript applications, so this can be one less thing. Thank you for reading this article, and I hope you enjoyed it.

