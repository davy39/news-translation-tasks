---
title: Manually Tuning Webpack Builds
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-22T19:49:37.000Z'
originalURL: https://freecodecamp.org/news/manually-tuning-webpack-builds-284923f47f44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vv4_hp-NqMdSIYWCH32Psg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Jamund Ferguson

  Back in April I shifted into a platform/architect role in my job at PayPal. I was
  tasked with looking at stability, performance and quality. One of the first things
  I did was graph our JavaScript bundle sizes over time.

  After a cou...'
---

By Jamund Ferguson

Back in April I shifted into a platform/architect role in my job at PayPal. I was tasked with looking at stability, performance and quality. One of the first things I did was graph our JavaScript bundle sizes over time.

After a couple of weeks I noticed at several points we had pretty big spikes in our build size which added up to nearly 1mb. Looking into it I discovered that we were duplicating things all over the place.

NPM makes it very easy to install many versions of modules. That is fine in server code, but when bundling for the web this is a big problem. Webpack provides some basic tools for inspecting built files, but making sense of that data requires a few extra shell commands:

Let me walk you through what’s happening here:

* **display-modules** is a flag on **webpack** that will showall of the node modules pulled into the bundle.
* **awk** re-orders the columns and deletes un-needed information.
* **grep** is removing really small files from the output.
* **sort -n** is putting the biggest files at the bottom
* **tail** is only showing the last (largest) 100.

And with that magic you get a list like this:

**EDIT:** it turns out that something like this is built-in to webpack.

```
webpack --display-modules --sort-modules-by size
```

The output is a bit messier, but it does order things in the correct way!

![Image](https://cdn-media-1.freecodecamp.org/images/1*XejQIc5Ql1sFn_Yqnlbkbg.png)

#### Investigating the source of the Duplication

Once you suspect you have more than one version of a module use **npm ls** to determine how that module in included in your project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zqyzstRgV03WaPv556iwbg.png)

While **npm ls** shows everything in your **node_modules** folder, **webpack** may not be including each of those files in the bundle. It only includes files that are being **require()**’d somewhere in your code.

#### Stopping the Duplication Madness

At this point you’re probably feeling a bit of terminal fatigue. You’ve typed a lot of commands, but how do you actually trim your build?

In the example above, this project is directly relying on **React 15,** but one of its dependencies relies on [**react-intl**](https://github.com/yahoo/react-intl)**@1.2.2** which has a dependency on **React 0.13**.

The solution in this case was to swap out our reliance on **react-intl** with an internationalization library that supported a newer version of React. That was a non-trivial amount of work, because we actually ended up writing a simplified alternative.

Thankfully many of the other issues in our build were easier to solve. Here are a few example:

**My lodash is Way too Big**

```
244kB  /Users/.../dev/paypal/web/~/lodash/dist/lodash.compat.js
```

There are several plugins out there that can tune your lodash builds to include the pats that you actually use. This can provide dramatic file size reduction. If you’re using Babel I’d suggest [https://github.com/lodash/babel-plugin-lodash](https://github.com/lodash/babel-plugin-lodash) or if not you can try [https://github.com/lodash/lodash-webpack-plugin](https://github.com/lodash/lodash-webpack-plugin).

Before those plugins came along we actually used the ESLint [**no-restricted-module**](http://eslint.org/docs/rules/no-restricted-modules) rule to ban **lodash** from our **public/** folder (in favor of underscore). This just prevents us from bringing both of them into the project.

**I Have too Many jQuery’s**

```
259kB  /Users/jamuferguson/dev/paypal/web/~/jquery/dist/jquery.js273kB  ./lib/jquery-1.10.2.js
```

In this case we have a local version of jQuery we’ve been using forever that we’ve aliased, but then we also have another module that explicitly depends on the latest version of jQuery.

The easiest fix for this is to remove your local copy and rely on the version installed in NPM. Always use the latest version you possibly can as future dependencies are likely to use the that version as well.

What if you can’t upgrade to the latest version of jQuery because of browser compatibility issues? Try the [jQuery Migrate Plugin](http://jquery.com/download/#jquery-migrate-plugin) if this is an issue for you or encourage the module maintainers (via github issue) to be more inclusive in their package.json file.

```
"jquery": "^1 || ^2"
```

This syntax allows a package to rely on either version 1 or version 2. In many cases this will allow for the backwards compatibility that you need.

**Squashing it Down**

My team was able to reduce the file size of our _minified_ JavaScript bundle by nearly 800kb using these techniques. Others have reported [success shrinking Moment.js](http://stackoverflow.com/questions/25384360/how-to-prevent-moment-js-from-loading-locales-with-webpack) by hundreds of kb using webpack plugins.

Are you having issues keeping your webpack builds small? What are some other approaches you’ve seen to keep the build size down?

