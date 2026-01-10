---
title: How to leverage the power of the modern Web Inspector
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T22:15:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-leverage-the-power-of-the-modern-web-inspector-b94dd85e1917
coverImage: https://cdn-media-1.freecodecamp.org/images/1*llEGsvQxvCsOvzSvxkdHNg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Craig Fitzpatrick

  The little, handy beast (aka the Web Inspector) has certainly come a long way since
  the days of “view source”!

  For those of you who are too young to remember — back in the prehistoric days of
  website development, the “view source...'
---

By Craig Fitzpatrick

The little, handy beast (aka the Web Inspector) has certainly come a long way since the days of “view source”!

For those of you who are too young to remember — back in the prehistoric days of website development, the “view source” command simply opened up the HTML of a page in Windows Notepad. Wasn’t great.

![Image](https://cdn-media-1.freecodecamp.org/images/Z315UwxriuUc1bIFJZBKuOL9GMrnnVNsA3NG)

![Image](https://cdn-media-1.freecodecamp.org/images/9HzsRSz98dsHAIyxljAA7MEmuPG81wOlLaLq)

Fast forward to today, we’ve got…

…modifiable CSS rules with color pickers built in…

![Image](https://cdn-media-1.freecodecamp.org/images/huO9Eg2fuA3IfS1hnziYbgTJpBjzAL2nbbHZ)

…the ability to nudge pixel values with your keyboard, causing real-time movement of your content…

![Image](https://cdn-media-1.freecodecamp.org/images/vtVRPpwtF0GAW6ROWFWHAPDgRm9V4d0nfiMA)

…and the greatest invention of them all: “look-ahead”, which auto-completes CSS names and values as you type. This saves you hours of debugging time caused by your own horrible spelling:

![Image](https://cdn-media-1.freecodecamp.org/images/7WQBILjFGLGLxGqSFU-vATjY8yRs5dffoGJW)

Many developers haven’t even discovered all the little bits of amazement built into most Web Inspectors.

For example, **did you know** that you can construct an entire HTML page in the Inspector?

Just open a new tab and Inspector (you’ll probably see a Google search page or something as your default) and start deleting nodes right out of the DOM inspector. Once you’re down to just the HTML node, right click and choose EDIT AS HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/GSt70yFCJfH3HgGtGNNf4i1NM63KCaOu1hep)

Build your page from scratch with an automatic, real-time preview of your work in the browser frame above! You can even drag and drop HTML nodes inside the Inspector to move things around.

Don’t even get me started on how amazing the JavaScript console is for inspecting memory, walking up and down the stack, and more.

It’s a great day to be a web developer!

### But

But there’s just one tiny hiccup. Saving your work has only [recently been made available, and it’s a little bit clunky](https://youtu.be/wz1Sy5C039M?t=6m17s)… You have to:

* open up the navigator and select overrides
* enable local overrides
* right-click on the CSS file and save for overrides

Sure… There is some pretty powerful tech here, but how do you quickly get your changes back to your production site? Ugh. So close to perfection!

### PageCloud

When I was writing the first version of [PageCloud](https://www.pagecloud.com), this was one of the things on my mind.

Even though PageCloud is a visual website builder that helps non-techies build web pages, I thought: the DOM inspector is such a powerful tool, wouldn’t it be great if you could simply make some changes and immediately have them sent up into the cloud?

And so I went on a mission to give developers the ability to use the Web Inspector to edit a production site.

However, the only way to accomplish this was to take a step back and rethink how web pages are built, managed, and served.

![Image](https://cdn-media-1.freecodecamp.org/images/fJOKYJXQW7npJiN5Mlux5ngsBWH2QQGf27x5)

There were a whole bunch of technical challenges in the way, like app servers, templates, nesting, databases, caches…

So I decided to take a page out of the desktop publishing playbook. The idea was simple: you launch an app to be able to read, edit, and create documents. Once you hit Save, all your changes stick.

So I asked myself:

> What if we simply considered web pages as documents?

I won’t bore you with the struggles of making this actually work (and the several bottles of wine that helped soothe the pain), but this initial idea was the foundation for everything PageCloud is today. And, so far, we are the only ones to do it.

Building on this concept, we were able let users interact with the web in the same way you would with your desktop apps: such as copy/pasting from the clipboard, layering, resizing, and moving objects freely on the page.

This same idea allowed us to integrate with the Web Inspector, enabling users to tweak anything, hit Save, and be done.

Here’s a quick example:

![Image](https://cdn-media-1.freecodecamp.org/images/tCpOmzM9SMCBJfPnTlZKBo7ZewNNZ7uFvF6r)

Leveraging all the beauty of the modern Web Inspector, you can: edit the HTML, CSS, and create links to external CSS and JS. You can even run commands in the JavaScript console to modify the DOM!

Any means by which you can modify that DOM is fair game. When you “SAVE”, all your changes are persisted and sent back up to the cloud — because your page is a document, after all!

![Image](https://cdn-media-1.freecodecamp.org/images/9Zwy1AALskP8H9q8hJnGROEAPL5FVaTwpjzO)

Thanks to the magic of the web inspector, you can even copy nodes from one browser window and paste them into the DOM of another page.

Yes, we are ambitious. But we believe that this new way of thinking will allow PageCloud to become the first-ever tool that fulfils the needs of the visual designer, while maintaining unrestricted access for developers.

Maybe one day in the not-so-distant future, “Inspect” will be replaced by a user-friendly interface, and join “view source” in the ranks of the outdated. That is, if PageCloud has anything to do with it!

