---
title: How to use Babel macros with React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T14:02:42.000Z'
originalURL: https://freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NIQACxrWjnCUOLogiOrW5Q.png
tags:
- name: Babel
  slug: babel
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Karan Thakkar

  A practical use case for solving an i18n problem using codegen.macro


  _Background Photo by [Unsplash](https://unsplash.com/photos/6PF6DaiWz48" rel="noopener"
  target="_blank" title="">Rayi Christian Wicaksono on <a href="https://unspl...'
---

By Karan Thakkar

#### A practical use case for solving an i18n problem using codegen.macro

![Image](https://cdn-media-1.freecodecamp.org/images/jfjrz1ddbDi4Zef64CpbkFH3aucozCj7VNNX)
_Background Photo by [Unsplash](https://unsplash.com/photos/6PF6DaiWz48" rel="noopener" target="_blank" title="">Rayi Christian Wicaksono</a> on <a href="https://unsplash.com" rel="noopener" target="_blank" title=")_

If you follow [Kent C. Dodds](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) or [Sunil Pai](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) on Twitter, you may have read tweets every once in a while about babel macros. So did I. But it was only yesterday that I finally understood what the hype is all about. **And it is glorious!**

So, coming to the problem: I wanted to add some utility to do locale-based number formatting in React Native. Since there is no consistent support for the [Internationalization API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl) in React Native, I used a polyfill for it: [https://github.com/andyearnshaw/Intl.js](https://github.com/andyearnshaw/Intl.js). Now, along with the polyfill, I also needed to import all the supporting locale files. There are two options here:

1. **Load all the locales**: This is straightforward, as I can just import one file. This should usually be avoided, since it can unnecessarily bloat your bundle size if you just need to support some locales.

![Image](https://cdn-media-1.freecodecamp.org/images/m8Pk2rDXI2f6OfOEECt99XwbiR0pw5OxzXXf)
_Load all locales provided by Intl.js_

2. **Load only necessary locales**: With this, I only load the locales that my app supports.

![Image](https://cdn-media-1.freecodecamp.org/images/LzitpUOexDJoOucbHFAbe7kkPP8nOVs2F7k5)
_Load only the necessary locales from Intl.js_

For example, if the app supports 40 locales, I have to manually end up writing 40 imports for each locale. It becomes much harder and more tedious to do this as the list of locales you support increases.

I wanted to automate this in a way that required no manual changes. This is especially useful for us as we have background jobs running on the CI that automatically update our locales file whenever we add support for a new language.

How can I dynamically import multiple files but also allow the React Native packager to have all the file paths at compile time? [**babel-plugin-macros**](https://github.com/kentcdodds/babel-plugin-macros) and [**codegen.macro**](https://github.com/kentcdodds/codegen.macro) ?

### What are these…babel things?

[This](https://babeljs.io/blog/2017/09/11/zero-config-with-babel-macros) blog post by [Kent C. Dodds](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) perfectly describes what [**babel-plugin-macros**](https://github.com/kentcdodds/babel-plugin-macros) is:

> It’s a “new” approach to code transformation. It enables you to have zero-config, importable code transformations.

[**codegen.macro**](https://github.com/kentcdodds/codegen.macro) is one such transformation that you can use to “generate code” at build time.

### How do you set it up?

React Native allows you to configure your own babel settings. You can create our own “.babelrc” file at the root of your project. To make sure that you use the default babel configuration that comes with React Native, install [**babel-preset-react-native**](https://github.com/facebook/react-native/tree/master/babel-preset).

On top of this you have to install another module: [**codegen.macro**](https://github.com/kentcdodds/codegen.macro). The codegen plugin uses [**babel-plugin-macros**](https://github.com/kentcdodds/babel-plugin-macros) under the hood to do its job. We’ll see in a bit what that is.

![Image](https://cdn-media-1.freecodecamp.org/images/9yAnzljqibKRoDn7rKe5AkGMQ63pPWfp4354)
_⬆️️This is how your **.babelrc** file should look_

### What does codegen.macro do?

It takes a piece of code, executes it, and replaces itself with the `export-ed` string. It will make a lot of sense once you see the example below. Given a list of locales and a codegen macro, it generates a list of imports at build time!

![Image](https://cdn-media-1.freecodecamp.org/images/1WKwUJ0aFROJGwvTQNckj87aOJOTvadtYTuv)

![Image](https://cdn-media-1.freecodecamp.org/images/yj8t50UemnN-BaJUUy0q1XAgggZgMDPgelZz)
_LEFT: codegen macro to build imports for all locales · RIGHT: Supported locales list_

![Image](https://cdn-media-1.freecodecamp.org/images/yPXysDYsOX2BytVUIzJKeY7pMK9CblD8oMeH)
_Output from babel after transpilation_

### But, what if I need syntax highlighting?

Since we’re writing all our code in a template string, it is really hard to get proper syntax highlighting. You might end up spending a lot of time trying to figure out why your macro gives an error while transpiling.

Thankfully, babel macros support a [few different ways](https://github.com/kentcdodds/babel-plugin-codegen#usage) to use them. My favorite is using a **codegen.require**. With this, you can move the body of your macro into a separate file and require it wherever you want, as shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/1PuJiRDOV4A2YT6nx1SOTmeViF9XbpG1-L22)

![Image](https://cdn-media-1.freecodecamp.org/images/u1tVA9klTM1XTlJtK5Rj2PE5nxrzkUdtsh9F)
_Import the codegen using a special **codegen.require** call_

#### Advantages of using this syntax:

* well, syntax highlighting ??‍
* no need to escape any escape sequences you need to use like **\n ?**

![Image](https://cdn-media-1.freecodecamp.org/images/EVMYOZ1LD-n8SHTuqvfwVNWXr6wghjIFiND3)

![Image](https://cdn-media-1.freecodecamp.org/images/zJD4HRaNxhHMHsHlhlINJf64K0B0vHin32jG)

* use template literals inside your codegen ?

![Image](https://cdn-media-1.freecodecamp.org/images/MVDROCDmMzE6MY8Osky7BpEJYlh-z5-QO-Ez)

![Image](https://cdn-media-1.freecodecamp.org/images/HXwx6D60GMfXD6DiiMmwqUI78dt4lowhLdrw)

### NOTE: upgrading React Native

If you choose to override the babel config, whenever you upgrade react-native, you must also bump the version of babel-preset-react-native to match the one being used inside that react-native version.

That’s it folks! You’ve setup babel macros with React Native ?? Check out th[ese other available macros i](https://github.com/kentcdodds/babel-plugin-macros/blob/master/other/docs/macros.md)f you wanna try out something different.

PS: Thanks to [Narendra N Shetty](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined), [Siddharth Kshetrapal](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) and [Kent C. Dodds](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) for reviewing the draft and helping shape it better ?

![Image](https://cdn-media-1.freecodecamp.org/images/NeELdCuvtLGOOP54bsUaMrsh3SDAd9cmI3FD)

Hi! ?‍ I’m K[aran Thakkar.](https://twitter.com/geekykaran) I work on React Native infrastructure at S[kyscanner Engineering.](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) Previously, I lead the web team at C[rowdfire.](https://www.freecodecamp.org/news/using-babel-macros-with-react-native-8615aaf5b7df/undefined) I like trying out new technologies in my spare time and I’ve built T[weetify](https://karanjthakkar.com/projects/tweetify) (using React Native) and S[how My PR’s](https://showmyprs.com) (using Golang).

Other articles written by me are:

* [An illustrated guide for setting up your website using GitHub and Cloudflare](https://medium.freecodecamp.org/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465)
* [Using the Let’s Encrypt Certbot to get HTTPS on your Amazon EC2 NGINX box](https://medium.freecodecamp.org/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76)

