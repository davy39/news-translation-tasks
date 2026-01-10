---
title: How to Choose the Best JavaScript Editor for Web Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-03T20:31:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-a-javascript-code-editor
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/cover-4.jpg
tags:
- name: Developer Tools
  slug: developer-tools
- name: editor
  slug: editor
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'By Arthur Puszynski

  There are a number of options for developers who are looking for a good JavaScript
  editor that provides a more efficient and pleasant working environment.

  Leading JavaScript code editors share many of the same great major features...'
---

By Arthur Puszynski

There are a number of options for developers who are looking for a good JavaScript editor that provides a more efficient and pleasant working environment.

Leading JavaScript code editors share many of the same great major features you might expect, including autocompletion (code completion), git integration, and plugin support. But it's the little things that can make one editor a better fit than another for a given developer.

Once you get comfortable with a code editor and familiar with the workflow that makes you more efficient, it can be difficult to switch editors as you will have to re-learn shortcuts to optimize your development processes. 

Even if you become more efficient in the long run, there is still a large barrier to entry when switching, so it's worthwhile investing a little time up front to pick the best editor for your needs.

Let's go through some of the most popular editor options now.

## [Visual Studio Code](https://code.visualstudio.com/)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-38.png)

VSCode from Microsoft is free, open-source, and pretty lightweight upon installation. This is the de facto editor for beginner JavaScript developers, partly because it is pre-loaded with a good set of functionalities that don't require additional plugins. VSCode is also popular and can be ideal for more advanced users that need to get started quickly.

A unique feature of VSCode is that it can be used through the browser. So the exact same environment you get on the desktop is possible on the go using your tablet. A [code-server](https://github.com/cdr/code-server) must be configured on a network you can access for this feature to work, but it is very convenient once it is set up.

**Tip**: Working on a large project in another IDE where the build process can take some time, I will often open the huge JS output file in VSCode and tweak it to instantly test a change in the browser before applying it. VSCode handles these large files swimmingly.

Git is built into the IDE, but the integration is not as robust as some other editors. For example, users of WebStorm prefer the push/merge experience over that of VSCode.

You can install many additional features you may need as extensions, of which there are thousands. But not all of them are actual features. Code snippets are mixed in with the features and add-ons, which can take time to review and find the best options to add. If you ever run into an issue, VSCode has a huge user community; someone has likely had the same issue and has solved it.

If you are not ready for a full paid IDE with all the bells and whistles, and not familiar enough with all the plugins and features you may need, this is the logical starting point.

## [Atom](https://atom.io/)

![Image](https://www.freecodecamp.org/news/content/images/2019/11/image-36.png)

The free Atom editor was developed by GitHub. It is actually a specialized version of the chromium browser converted into a text and source code editor. Internally it utilizes Node.js for plugin support.

A plethora of plugins are available for any features you may desire, however it's not as strong out of the box. You must gather a number of plugins to build up the dev environment to where you can be as effective as possible.  If you're working with JavaScript, here are some essential Atom plugins to get you started:

* atom-typescript
* file-icons - to colorize and assign icons to different file types
* atom-beautify
* linter

**Tip**: Enable the autosave package which will save edits when focus is lost. It is disabled by default.

Multiple users can work on the same file at the same time, each with multiple cursors on the screen, via the teletype plugin. You can use this for mentoring, pair coding, or collaborating. This feature sets Atom apart from other editors.

The git integration is well implemented, as you would expect from GitHub software. Also useful is a git-plus plugin that lets you run git commands through keyboard shortcuts without using the git terminal.

Atom is customizable to the point where you can edit a .less file to adjust the IDE colors which is nice if you like to tweak every detail of your environment. You can run a .coffe script on startup that can be used to quickly change the editor's behavior.

You can write plugins in JavaScript against a well documented editor API. The possibility of authoring your own functionality and behaviors is nice to have, should the need arise.

The editing experience is smooth and you can enhance it with other plugins like minimap, but there is some initial time investment required to set it up with all the features you want. The benefit is that features you don't need won't take time loading which slows down the experience. However, you can experience some momentary sluggishness when loading large files or switching tabs.

I initially liked the idea of editing CSS styles to customize the IDE environment, or at least having the possibility if I ever wanted to come up with my own themes. It sounds fun but in practice, coming up with themes that include many variables are not trivial projects. Fortunately there are many polished theme plugins available for download.

Atom is a solid editor and it will be a perfect fit for many developers.

## [Sublime Text](https://www.sublimetext.com/)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-34.png)

Sublime Text is a paid editor but a free trial is available. It is not preloaded with many plug-ins to start, but of course they are available to address any needs you may have. Some packages like SideBarEnhancements to rename, move, copy, and paste should probably be built in to the core bundle but you can download them to enable this functionality.

Similar to Atom, it can take a bit of time to get everything set up. But once up and running, the experience is very smooth. Save on lost focus is also available.

Sublime Text is nice because it's lightweight which makes it very fast to load and work with large projects or files. The "goto anything" feature implementation stands out as it can be used with file names, symbols, and line numbers. Most IDEs provide similar features in one form or another, but being able to combine them and search with queries like "fileName@functionName" is quite nice.

Selecting a variable selects all occurrences of that variable and renaming it renames all occurrences automatically, so this common task becomes a very streamlined experience.

In many ways, Sublime Text is very similar to Atom. But Sublime Text has the edge with better general performance and responsiveness, which is superb.

## [VIM](https://www.vim.org/)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-39.png)

Vim is also a free text editor and very configurable. Originally named vi and the first text editor developed for Unix, it was later extended into a more feature rich editor named Vim. It is available on most Linux distributions.

Vim has robust search and syntax highlighting capabilities, and it is super light so it can perform well with even very large files.  But it does require some work to get it set up and ready to use. 

A GUI is available, but it is not the default interface for Vim. Even enabling mouse support requires some action to get it working. The default is a keyboard mode that some may prefer accessing every control and feature through shortcuts. 

That being said, Vim can be your perfect IDE if you spend some time learning the ins and outs of the software and set up all the behaviors and features you want in it. If you are crunched for time and can't make the initial investment to get things dialed in, Vim may not be the best choice for you.

## [WebStorm](https://www.jetbrains.com/webstorm/)

![Image](https://www.freecodecamp.org/news/content/images/2019/06/image-40.png)

WebStorm was developed by JetBrains and stands out from the rest as a true JavaScript IDE, as it has all features integrated right out-of-the-box. The development environment for different platforms like React, Angular, Vue.js, etc. is seamless. You can debug node scripts, and run tests on a built-in server. You can also execute and debug npm scripts through a tree view interface. And it doesn’t require any plugins to do this.

However, plugins are available for some rare features that are not built into the software directly. One plugin that was not included by default was a markdown split edit/preview window. But for the most part everything you may need is already there. The nice thing about this is that you will discover features you didn't know existed and how nice it is to have them.

Files save automatically as you work on them by default.  When you use another app that doesn't do this, manual save feels very primitive in comparison. Though it's not unique to WebStorm, the implementation is a little nicer.

Some people may not always trust the integrity of the ctrl-z undo state stack, but in WebStorm there is built in VSC system that basically does a commit every time a file is saved. This is internal and is separate from your git commits. Files save at least whenever the file content window loses focus. So if you go a while without committing to git and have to go back or see a previous state after your last commit, it's no problem.

**Tip**: Ctrl-shift-up/down arrow lets you move lines or blocks of code up or down while the editor handles commas/block brackets automatically.

When you work on projects that have many files, scrolling the file tree in search of a specific file can slow you down. But if one of those items is already open and in focus, clicking the target icon scrolls the project tree view to this file. It's very convenient.

A couple cons are that it is not free. And at times, it can be a memory hog with very large projects. It has gotten better over the years and file contents are indexed internally so that searching large projects is very fast. A recent update also includes a significant improvement in startup speed.

## General Editor Productivity Tips

The duplicate line/selection shortcut (in WebStorm: ctrl-d, in Atom: ctrl-shift-d, but they all can do it) is one of my favorites and can save a lot of time in many coding scenarios.

This will come up from time to time where you have a list of items and have to modify the first (or some) character on each line from say '.' to ',' but find-replace is not practical to use. WebStorm allows alt-click to place multiple cursors to make the same edits in multiple places. Still, I find the following approach faster in some scenarios:

* Place your cursor after the first period, and start doing the change manually.
* Press backspace, comma, arrow down. Have a finger on each key, and repeat the presses starting slowly then speeding it up as you go. Once you get the pattern down you can speed it up to where you'll go through a list of 200 lines in no time. 

It's almost like playing a melody on a piano (as fast as you can). You can do this with numbering lists as well. Write the first line without the number, duplicate the line 9 times, and do the same process except have one finger press a subsequent number each time. Start the next 10 lines with a '1' and do the same process adding a digit after each '1'.

If you google “[editor name] cheatsheet” you can get a quick summary from users for important configuration or shortcuts for the editor you are trying. Print it and read all the shortcuts to become aware of new features and functionality you may not otherwise be exposed to. 

Considering how the highlighted actions may improve your current processes will be beneficial. If you see one that may help, put a mark next to it so the next time you are in the situation it's easy to recall. Even if you use it rarely and mainly in the beginning, having a quick reference at hand can lower friction to learning more about your editor and can save time context switching and searching in the future. 

I go as far as finding the PDF version, printing and laminating the page for future reference, but for some a bookmark or screenshot may work as well. 

## Conclusion

If you are a beginner hoping to learn JavaScript and use a polished development environment to start, VSCode is the obvious choice because it is easy to use with many strong features built in.

For more experienced developers who know exactly what they want, Sublime and Atom may be preferable as they will give you complete control over your dev environment. You can choose from thousands of features (packages) to install and keep the application startup and resource usage free of extras you don’t need or want. Spending some time with each will help you make the right choice.

For the hard-core power users who feel at home using the keyboard alone working on projects, you can be more effective with Vim than any other editor. Saving the time it takes for your hand to move between the keyboard and mouse will add up, but it will take some time to master this process!

Lastly, if you don't mind maintaining a paid subscription and are not concerned with memory or CPU limitations of your development machine, WebStorm will get you up and running quickly regardless of the JavaScript development platforms, transpilers, or build processes you work with. It provides a very convenient environment to work in.

I personally use WebStorm as my primary IDE, but still regularly use VSCode to edit individual or very large files when performance is a priority.

If you enjoyed this article please consider checking out [JSCharting](https://jscharting.com/), a JavaScript charting library for developers.  You can also view additional blog posts [here](https://jscharting.com/blog/).


