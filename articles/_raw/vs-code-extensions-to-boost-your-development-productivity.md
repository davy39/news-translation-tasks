---
title: VS Code Extensions That'll Boost Your Development Productivity
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-12-28T14:50:40.000Z'
originalURL: https://freecodecamp.org/news/vs-code-extensions-to-boost-your-development-productivity
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/vscode.jpg
tags:
- name: Productivity
  slug: productivity
- name: Visual Studio Code
  slug: vscode
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Having a good text or code editor that fits into your workflow is crucial
  to productivity as a developer. VS Code comes stocked with a lot of features by
  default, but here are 7 extensions that will help take your workflow up another
  level.


  What is ...'
---

Having a good text or code editor that fits into your workflow is crucial to productivity as a developer. VS Code comes stocked with a lot of features by default, but here are 7 extensions that will help take your workflow up another level.

* [What is VS Code?](#heading-what-is-vs-code)
* [VS Code Extensions](#heading-vs-code-extensions)
* [Sublime Text Keymap and Settings Importer](#heading-sublime-text-keymap-and-settings-importer)
* [Import Cost](#heading-import-cost)
* [indent-rainbow](#heading-indent-rainbow)
* [Rainbow Brackets](#heading-rainbow-brackets)
* [Settings Sync](#heading-settings-sync)
* [Profile Switcher](#heading-profile-switcher)
* [Better Comments](#heading-better-comments)
* [Duplicate Action](#heading-duplicate-action)

%[https://www.youtube.com/watch?v=OIWVJj9yRbA]

## What is VS Code?

A quick note in case you’re not familiar. [VS Code](https://code.visualstudio.com/), which is short for Visual Studio Code, is a popular text or code editor that’s maintained by the Microsoft team.

It’s grown a tremendous share of the developer market over the last year or two making it the go-to editor for web developers.

Coupled with the fact that Microsoft is investing a lot of time into it and independent developers are building a ton of extensions, you can’t go wrong with giving it a shot.

## VS Code Extensions

Part of what makes VS Code great is it’s extensibility. It allows developers to creatively take the editor to another level by implementing features Microsoft may not want to support or even building a whole note-taking experience on top of it with [Foam](https://foambubble.github.io/foam/).

While there are thousands of extensions available in the [VS Code Marketplace](https://marketplace.visualstudio.com/vscode), these are the 7 that are critical to my workflow as an active developer.

## Sublime Text Keymap and Settings Importer

Before moving to VS Code, I was a Sublime Text 3 user. It’s still a great text editor, but when moving to VS Code, a lot of the shortcuts and key mappings weren’t the same.

Sublime Text Keymap and Settings Importer let me first import my settings from Sublime text, but it also set up the default key mappings. This made shortcuts that were available in Sublime immediately available in VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-sublime-keyboard-shortcuts.gif)
_Sublime Text key mappings in VS Code_

This includes two of my favorites like multi-select (selecting something then pressing CMD+D / Ctrl+D) and duplicating a line (adding a cursor on a line and pressing CMD+Shift+D / Ctrl+Shift+D).

[Sublime Text Keymap and Settings Importer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.sublime-keybindings) (marketplace.visualstudio.com)

## Import Cost

Modern day developers have to constantly deal with dependencies coming from various sources. As we pull in a bunch of different code to build our project, that additional code comes at a cost.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-import-cost.jpg)
_Showing import size in VS Code_

[Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) calculates an estimate of the size of an import allowing us to see how much additional weight we would be adding to our project size with that added dependency.

This helps us recognize the size of our dependencies, preventing accidental overload of huge libraries that could impact performance and hurt our customer’s user experience.

[Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) (marketplace.visualstudio.com)

## indent-rainbow

Style is an important factor in making our code readable. Part of that style is how we indent our code, so we understand nesting of different code blocks.

The issue is sometimes that nesting can grow pretty large and it can be difficult to try to find which opening tag belongs to which closing tag.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-indent-rainbow.jpg)
_Rainbow-colored indent spacing in VS Code_

[indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) adds colors to the indent spaces, allowing us to easily line up and see which tags belong to each other.

[indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow)  (marketplace.visualstudio.com)

## Rainbow Brackets

Similar to indenting, complex code, particularly when using math, can create easily confusing lines of code when you have multiple uses of parenthesis within the same statement.

For instance, if we want to apply some simple math:

```
const value = (((1+1)*2)+1)*2;

```

And while that’s a simple example, that can easily get out of hand and hard to track.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-rainbow-brackets.jpg)
_Rainbow-colored brackets in VS Code_

[Rainbow Brackets](https://marketplace.visualstudio.com/items?itemName=2gua.rainbow-brackets) highlights the parenthesis in different colors allowing us to get a better idea which opening bracket belongs to which closing bracket of our equation.

[Rainbow Brackets](https://marketplace.visualstudio.com/items?itemName=2gua.rainbow-brackets) (marketplace.visualstudio.com)

## Settings Sync

If you typically work between two laptops or two different environments, you might have to manually maintain keeping your text editor the same, if you’re particular about your setup (like I am).

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-settings-sync.jpg)
_Configuration for Settings Sync in VS Code_

[Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) allows you to save your VS Code settings in a GitHub Gist. This lets you sync those settings across different VS Code installations

[Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) (marketplace.visualstudio.com)

_Note: if you want to learn more, [I wrote a tutorial](https://www.freecodecamp.org/news/how-to-sync-vs-code-settings-between-multiple-devices-and-environments/) that walks you through setting this up step-by-step!_ 

## Profile Switcher

As a content creator, I need to make sure that when I’m showing my screen to others, that I’m using accessible colors and font sizes that allow people to easily see what I'm demo'ing.

The issue is those settings aren’t what I like to use day-to-day when I’m heads down coding.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-profile-switcher.jpg)
_Switching profiles in VS Code_

[Profile Switcher](https://marketplace.visualstudio.com/items?itemName=aaronpowell.vscode-profile-switcher) allows you to set up multiple VS Code profiles each with their own configuration allowing you to easily switch between different setups.

[Profile Switcher](https://marketplace.visualstudio.com/items?itemName=aaronpowell.vscode-profile-switcher) (marketplace.visualstudio.com)

## Better Comments

While they might not seem important when you’re writing code, comments are critical to helping others understand that code. They also typically help you understand it when you look at it a year down the road.

Those comments are helpful, but they can be hard to read, as they’re typically all one gray color that doesn’t necessarily stand out.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-better-comments.jpg)
_Keyword highlighting of comment blocks in VS Code_

That’s where [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) comes in, which adds a kind of syntax highlighting to the comments, adding color to keywords and statements that helps the readability of your code comments.

[Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) (marketplace.visualstudio.com)

## Duplicate Action

This last one seems like a small thing, but for some reason, VS Code doesn’t come with the ability to right click a file and duplicate it by default.

When I’m heads down in code, I’ll typically duplicate a file, like an existing template, which allows me to only change the content. This makes creating a new page more productive.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/vscode-duplicate-action.jpg)
_Duplicate file or directory option in VS Code_

[Duplicate Action](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-duplicate) simply adds the Duplicate File or Folder option to the context menu when you right click a file or folder.

[Duplicate Action](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-duplicate) (marketplace.visualstudio.com)

## What’s your favorite extension?

There are a ton of extensions out there that do amazing things – what’s your favorite? Let me know by [sharing with me on Twitter](https://twitter.com/colbyfayock)!

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">🐦 Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">📺 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">📫 Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">💝 Sponsor Me</a>
    </li>
  </ul>
</div>

