---
title: Browser modes explained using nostalgia and the saddest little word ever
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-22T14:28:59.000Z'
originalURL: https://freecodecamp.org/news/web-developer-interview-q-a-quirks-mode-almost-standards-mode-and-full-standards-mode-explained-847edba3dc48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bZZLpdpMiwhyzRqKAc7OyQ.jpeg
tags:
- name: internet
  slug: internet
- name: interview questions
  slug: interview-questions
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Zuzana K

  In my last article, I discussed the doctype — what it is and why it is needed. In
  this article, I am going to look into the difference between various modes that
  browsers can run: the full standards mode, the almost standards mode, and th...'
---

By Zuzana K

In my last [article](https://medium.freecodecamp.org/web-developer-interview-q-a-what-does-a-doctype-do-146dd757d7d1), I discussed the doctype — what it is and why it is needed. In this article, I am going to look into the difference between various modes that browsers can run: the full standards mode, the almost standards mode, and the quirks mode.

These two articles are quite related, so you might want to read the previous one first to understand what I am on about.

### Question: What’s the difference between full standards mode, almost standards mode, and quirks mode?

The different modes are all related to the early implementation of [W3C](https://www.w3.org/) standards.

Doctype was introduced to tell browsers what kind of documents they were meant to be rendering. If the developer fails to include the doctype in their HTML document, the browser has no idea what type of document it is dealing with.

So, to be on the safe side, it will render the document to be compatible with the old (quirk) browsers (Navigator 4, Internet Explorer 4 and 5) in what is known as the quirks mode.

And since the old browsers lived in the land of a very bad CSS, this means a lot of your CSS styles will not be applied, and your site will not look the way you expect it to.

Of course, some developers may choose to omit the doctype on purpose because they want their document to render in the quirks mode for various reasons.

Like, what if I want to know what would my website look like in 1998?

Good reason, I’d say.

Now that we know what quirks mode is and what it will do to our poor website (break it), what’s the deal with the full standards and the almost standards modes?

The almost standards mode is also known as the limited quirks mode. As you can imagine, the content rendered in the almost standards mode is almost fully compliant with the full standards mode.

Almost.

The saddest word ever.

> I. Tiny Stories

> The saddest word

> in the whole wide world

> is the word almost.

> He was almost in love.

> She was almost good for him.

> He almost stopped her.

> She almost waited.

> He almost lived.

> They almost made it.

By [Nikita Gill](https://quotecatalog.com/quote/nikita-gill-i-tiny-stories-g7O3RR7/)

Never mind, let’s move on.

The almost standards mode renders the document with only a few quirks that have to do with the vertical sizing of table cells.

On the other hand, the full standards mode renders the document according to the latest HTML and CSS specifications. Even though there are still some differences between how modern browsers render content on the screen, we can use [Normalize.css](https://necolas.github.io/normalize.css/) or [Reset CSS](https://meyerweb.com/eric/tools/css/reset/) to reduce the inconsistencies (and keep our sanity).

So, if there are any quirks on your website, they are probably down to you, not the browser.

Sorry.

Well, here we are. If anyone ever asks you about the difference between the full standards, almost full standards, and the quirks modes, just remember the old browsers, broken CSS, and the saddest word ever.

If you want to read more about activating the different browser modes, there is a fantastic [overview](https://hsivonen.fi/doctype/) written by Henri Sivonen. And a rough list of quirks can be found on [MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Mozilla_quirks_mode_behavior).

Next time I’ll look into the difference between HTML and XHTML. Hope you’ll join me in what is turning out to be quite an exciting topic! See you soon!

The list of questions that I am answering has kindly been provided by [Rose](http://www.verifyrecruitment.com/blog/index.php/tag/askrose/) from the [Verify recruitment agency](http://www.verifyrecruitment.com/) in Dublin, Ireland.

_If you have enjoyed this article and found it beneficial, please consider leaving me a comment or some claps. Thank you!_

