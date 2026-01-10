---
title: 'VS Code snippets: the most powerful tool to boost your coding productivity'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-16T15:34:08.000Z'
originalURL: https://freecodecamp.org/news/the-most-powerful-tool-to-boost-your-coding-productivity-2dc80e0eff00
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UwAkIPzykbLNqOffgyvegw.gif
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'By Sam Williams

  Write more code with fewer keystrokes


  _Photo by [Unsplash](https://unsplash.com/@dlanor_s?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Dlanor S on <a href="https://unsplash.com?utm_source=medium&utm_...'
---

By Sam Williams

#### Write more code with fewer keystrokes

![Image](https://cdn-media-1.freecodecamp.org/images/0*aEvz1gdQhix8dzTi)
_Photo by [Unsplash](https://unsplash.com/@dlanor_s?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Dlanor S</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Everyone wants to be able to produce more code in fewer keystrokes. Arrow functions in JavaScript have become incredibly popular recently — and they only save you 6 characters!

```
(function(){console.log('a')})() // 32 charachters(()=>{console.log('a')})() // 26 charachters
```

But there is a better way to save typing — and this article will show you the tool to do it.

### Code Snippets

For years, people have used code snippets to save time — whether they are common functions, file structures or even templates for whole systems. This is not a new idea.

The problem with a lot of existing systems is that these snippets were often stored in text files or other file systems and needed to be manually copied and pasted into wherever they were needed.

This was great for large snippets of code. But one-liners were often quicker to type than to search for the file, copy it and paste it in.

The next step was tools such as TextExpander or AutoHotKeys, where special key sequences could be set up to paste code snippets into wherever you were typing. These are great and can save you loads of time… but we can take it one step further.

### VS Code Snippets

![Image](https://cdn-media-1.freecodecamp.org/images/1*UwAkIPzykbLNqOffgyvegw.gif)

VS Code has a system that is more powerful than even TextExpander or AutoHotKeys. Its inbuilt code snippets can be configured to do much more than just pasting the code.

Before we talk about the fancy features, we’ll learn how to create a snippet.

In VS Code, press ctrl+shift+P to open the command palette and search for snippet. Selecting ‘Configure User Snippets’ presents you with a list of coding languages that you can create a snippet for. We’re going to go with JavaScript.

This opens the snippet editor. There is a comment showing you how to create a basic snippet, but we’re going to create our own.

This snippet is one that is [my favourite line of code](https://medium.freecodecamp.org/my-favourite-line-of-code-53627668aab4). It’s a nice pattern for promise handling.

```
const handle = prom => prom.then(res => [null, res]).catch(err => [err, null]);
```

To create our snippet, we need to create a new key in the object. This key points to an object with a `prefix`, `body` and `description` .

```
"insert handle function": {    "prefix": "",    "body": [],    "description": ""}
```

The prefix is the text that we want to enter to trigger this snippet. You need to make sure that this is unique. Calling it `handle` would trigger the snippet every time you call the function so we can go with something like `promHandle` .

The body is an array of the lines in the snippet. If you have multiple lines of code then you’ll have multiple strings in the body array. The description is what will be shown when you see the suggestion in VS Code.

When all of this is completed you get something like this:

```
"insert handlefunction": {    "prefix": "promHandle",    "body": [        "const handle = prom => prom.then(res => [null, res]).catch(err => [err, null]);"    ],    "description": "inserting a 'handle' function"}
```

With your snippet file saved, when you start typing `promhandle` you get a new suggestion. Keying down to that shows the description of the snippet as well as the first line of the code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mi0gmOsCo4I6AyoHHjB24w.gif)

Now you can save yourself hundreds of characters by creating your own snippets. But there are some even more powerful features!

#### Tab Insert Points

When you paste your snippets, there are usually bits of info that you need to add in. Whether it’s the naming a function or choosing the variables, you can set points in your code where you need to enter data. When you past these snippets you can tab between these insertion points.

To add an insert point, you just need to add `$1` for the first point, `$2` for the second and so on. This is really useful for functions where they expect an object.

```
"sendMessage": {    "prefix": "sendMessage",    "body": [        "await botHelper.sendToUser({message$1, userID});"    ],    "description": "await sending a message using bot helper"},
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*1JFkjHn1m1Lpi_fzKrz2Ww.gif)

You can have multiple tab points spread throughout the code, meaning you can quickly and easily populate your snippet without having to click or arrow-key to each point.

#### Language-specific snippets

When we first opened the snippet editor, we were presented with a list of languages. We chose JavaScript, but you could have chosen any of the other 44 languages. The great thing about VS Code snippets is that they can be locked to a specific file type.

If you are writing a HTML file, you won’t get all of your JavaScript or Python snippets. This also means you can have the same prefix produce different snippets based on the file type you’re currently working in! But don’t worry, you can still add global snippets if you want to be able to use them in any file type.

#### Locations-specific snippets

In a similar way to language specific snippets, you can also create folder specific snippets. This can be great when the same named function does a different thing in two different projects.

Just select `New Snippet file for '...'` when choosing your language.

### Creating more snippets

Now you know the powerful ways that VS Code snippets can improve your productivity, you probably want to make loads. Unfortunately, they can be frustrating to create. Luckily there are two solutions:

#### Snippet Generator

[Snippet Generator](https://snippet-generator.app/) is a site that lets you paste in some code and easily convert it into snippet format.

It’s really easy to use and lets you quickly create snippets that you can just copy and paste straight into your snippet files. It’ll work with any language and is completely free.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kw9vrKEgA4mhMurEpniDbg.png)

#### Snippet Extensions

If you use a framework, such as React or Angular, there are lots of snippets that you are going to want to create. Fortunately this is an issue that other people have had before so they have created libraries of common snippets for each framework.

Searching for `snippets` in the VS Code extension marketplace produces hundreds of results that you can install. Everything from React, Angular and Vue to ES6 JS, C# and PHP. These often have a full range of snippets to dramatically cut down you time spent typing.

The one disadvantage of these extensions is that you’ll have to learn what the prefixes (triggers) are, but you’ll quickly memorise the ones you use most.

Thanks for reading this post on increasing your coding productivity with VS Code Snippets. If you’ve learnt something then hit that clap ?button, and follow me for more tips, tricks and tutorials!

![Image](https://cdn-media-1.freecodecamp.org/images/1*LhwiNc46QXzOCEb2QhERBg.gif)

