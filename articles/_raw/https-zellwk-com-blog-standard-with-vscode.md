---
title: How to Use Standard with VSCode
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-06-14T04:58:21.000Z'
originalURL: https://freecodecamp.org/news/https-zellwk-com-blog-standard-with-vscode
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca207740569d1a4ca5214.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: "I use Visual Studio Code as my text editor. When I write JavaScript, I\
  \ follow JavaScript Standard Style.  \nThere's an easy way to integrate Standard\
  \ in VS Code—with the vscode-standardjs plugin. I made a video for this some time\
  \ ago if you're interes..."
---

I use [Visual Studio Code](https://code.visualstudio.com/) as my text editor. When I write JavaScript, I follow [JavaScript Standard Style](https://standardjs.com).  
  
There's an easy way to integrate Standard in VS Code—with the [vscode-standardjs](https://marketplace.visualstudio.com/items?itemName=chenxsan.vscode-standardjs) plugin. I made a [video](https://youtu.be/Hv8FgxJyI9Y) for this some time ago if you're interested in setting it up.  
  
But, if you follow the instructions in the video (or on vscode-standardjs's readme file), you'll come to notice there's one small detail that needs to be ironed out.  
  
Try writing a `function` the old way, and save it repeatedly. VS code will toggle between having and not having a space before the left-parenthesis of the function.

<figure><img src="https://zellwk.com/images/2019/vscode-standard/functions.gif" alt="VS code toggles between having and not having a space before '('."></figure>

You get the same problem when you write methods with the ES6 method shorthands:

<figure><img src="https://zellwk.com/images/2019/vscode-standard/methods.gif" alt="Same problem happens when you create methods with ES6 method shorthands."></figure>

There's a quick way to fix this issue. What you need to do is set `javascript.format.enable` to `false`. This disables VS Code's default Javascript formatter (and lets vscode-standandjs does the formatting work).

So the minimum configuration you need to get Standard and VS Code to work together is:

```
{
  // Prevents VS Code from formatting JavaScript with the default linter
  "javascript.format.enable": false,

  // Prevents VS Code linting JavaScript with the default linter
  "javascript.validate.enable": false,

  // Lints with Standard JS
  "standard.enable": true,

  // Format files with Standard whenever you save the file
  "standard.autoFixOnSave": true,

  // Files to validate with Standard JS
  "standard.validate": [
    "javascript",
    "javascriptreact"
  ]
}

```



---

  
_This article was originally posted on [my blog](https://zellwk.com/blog/standard-with-vscode)._  
_Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer._


