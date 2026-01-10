---
title: DevDocs is joining the freeCodeCamp community
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2018-03-26T13:06:01.000Z'
originalURL: https://freecodecamp.org/news/devdocs-is-joining-the-freecodecamp-community-ae185a1c14a6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7lX0aAjYhgPsLdjjWIem-g.png
tags: []
seo_title: null
seo_desc: 'DevDocs is an open source web app that combines documentation for lots
  of developer tools into a single searchable interface.

  I’ve been using DevDocs since before freeCodeCamp even existed, and have sung its
  praises over the years.


  The simple, no-no...'
---

DevDocs is an open source web app that combines documentation for lots of developer tools into a single searchable interface.

I’ve been using DevDocs since before freeCodeCamp even existed, and have [sung its praises](https://www.quora.com/Which-reference-book-should-I-have-while-learning-code-through-Free-Code-Camp/answer/Quincy-Larson) over the years.

![Image](https://cdn-media-1.freecodecamp.org/images/5I5NnL3Is1K70JuVme3DZIpQwVQr0nBSG5bF)
_The simple, no-nonsense landing page of DevDocs — with browsable API documentation along the left-hand side_

The speed and simplicity of DevDocs is a real a breath of fresh air. Every API is laid out in the same clear hierarchy.

![Image](https://cdn-media-1.freecodecamp.org/images/QkN3JS9RXTkAQzCtl5VBOkgcH9VfPnMV3SGp)
_A screenshot of DevDocs.io and its intuitive API documentation browsing interface_

So when it came time to design [the freeCodeCamp Guide](https://medium.freecodecamp.org/heres-a-new-way-to-learn-coding-tools-and-concepts-right-when-you-need-them-ee82d15c576d) last summer, I already had a clear template in mind. We were going to create a DevDocs-like interface for exploring programming concepts.

I reached out to DevDocs creator Thibaut Courouble for advice. He was helpful in explaining how DevDocs worked and his reasoning behind some of his design decisions.

![Image](https://cdn-media-1.freecodecamp.org/images/UydWCEFCDVcOv23vnbA9EhMEpZj6q5dJX-rL)
_DevDocs creator Thibaut Courouble_

He and I kept in touch. We exchanged ideas for how to make tools that were more accessible to developers in parts of the world without reliable high-speed internet connections.

Then a couple months ago, Thibaut approached me about the possibility of donating the DevDocs project to the freeCodeCamp community, so that we could continue to grow the project beyond what he is able to do as a lone maintainer.

And today — exactly 5 years after Thibaut created DevDocs — I’m excited to announce that [DevDocs is now officially part of the freeCodeCamp community](https://github.com/freecodecamp/devdocs)!

## A brief history of DevDocs

Thibaut is a French developer who now works as a senior development lead at Shopify in Ottawa, Canada.

Thibaut created DevDocs exactly 5 years ago today, on March 26, 2013. At the time, he just wanted a better way to quickly access the Mozilla Developer Network documentation.

Originally, DevDocs was just an ordinary documentation folder on his hard drive, for his own personal use — the kind that many developers had on hand for reference. Then, after a few months of development, Thibaut launched DevDocs on June 18, 2013, as a free web app.

At first, Thibaut kept DevDocs closed source. But on October 24, 2013, he open-sourced it.

The DevDocs project has since gone on to accumulate more than 17,000 GitHub stars, along with 66 contributors (though Thibaut is still by far its most prolific contributor).

![Image](https://cdn-media-1.freecodecamp.org/images/IME5se6-AC5zmQLYEJFRn0wnA85lwGLaVwU8)

Thibaut wrote dozens of scraping scripts to go out and automatically download documentation from different projects, each carefully-tuned to create a consistent reading experience and generate good search results.

Over the next two years, Thibaut added many improvements such as new documentation, keyboard shortcuts, better search, mobile support, and the ability to switch to a dark theme for night-time viewing.

Then, in 2015, Thibaut made DevDocs fully-functional offline. Suddenly, anyone could download entire sets of documentation for access offline. All of these files would be stored in the browser, thanks to a clever use of a new technology called IndexedDB.

And in early 2016, Thibaut added support for versioning. Instead of being limited to only the most recent version of a documentation, DevDocs now started supporting multiple versions for each project and library.

Those two major new features would turn out to be an inflection point in DevDocs’s user base. The project grew to become one of the most widely-used tools in the developer community.

![Image](https://cdn-media-1.freecodecamp.org/images/SSf07mo9M2H0eJYYZM5t8XIppq0euoGtAH3L)
_DevDocs offline mode preferences, seen here with dark mode enabled._

If you want to see how far DevDocs has come in the past five years, compare these two Hacker News threads:

1. [The first thread from June 2013](https://news.ycombinator.com/item?id=5956958) — mostly people unfavorably comparing DevDocs to other documentation projects (many of which are now defunct).
2. [A second thread from late 2017](https://news.ycombinator.com/item?id=15507871) — in one of Hacker News’s most-upvoted threads of all time, people praise DevDocs — particularly for its speed. The message is clear: your project doesn’t have to be the first of its kind — you just have to stick with it and make consistent improvements to it, and you can emerge the leader.

**Today, more than 100,000 developers use DevDocs as a reference each month.**

## How DevDocs works under the hood

One of the most common questions people ask Thibaut: how did DevDocs get to be so fast?

Thibaut attributes the speed of DevDocs to many factors:

* DevDocs is a single-page Ruby web app with a tiny backend.
* When you visit [DevDocs.io](https://devdocs.io), after the initial page load, all subsequent files (including documentation files) are fetched through a lightning-fast Content Delivery Network (CDN).
* It uses GZIP, HTTP caching, App Cache, concatenated and minified JavaScript and CSS
* There are no ads (ads slow everything down)
* It uses localStorage as an extra level of caching for some assets
* It uses an in memory cache for things like instant backward and forward navigation
* It uses IndexedDB for caching entire sets of documentation locally on your computer
* The documentation is stripped of all remote assets and unnecessary markup, resulting in smaller files
* It uses [optimized client-side search](https://github.com/Thibaut/devdocs/blob/master/assets/javascripts/app/searcher.coffee)
* It has a non-blocking and asynchronous user interface
* It features an optimized DOM tree with a [paginated](https://github.com/Thibaut/devdocs/blob/master/assets/javascripts/views/list/paginated_list.coffee) sidebar list, so that it doesn’t have to render 1,000's of nodes right away
* It has a simple user interface that eschews frills like shadows or animations

Finally, DevDocs doesn’t use any jQuery or any JavaScript frameworks. All of the DOM operations are implemented manually, making them as fast as they can get. (Thibaut says he wouldn’t recommend this no-framework approach for most apps, but it works well for DevDocs.)

## How you can get involved

Right now we’re looking for a passionate and experienced Ruby developer who is interested in becoming a long-term contributor to DevDocs.

We’re also looking for people interested in making DevDocs easier to contribute to, through writing documentation and refactoring code.

You can also help by reporting any bugs or feature requests you have [in the issue tracker](https://github.com/freecodecamp/devdocs/issues), and helping triage or fix those.

You can join [the DevDocs contributor chatroom on Gitter](https://gitter.im/FreeCodeCamp/DevDocs) and introduce yourself.

Lastly, you can help by using DevDocs and sharing it with your friends and colleagues. The next time you need to look up documentation, go to [DevDocs.io](http://devdocs.io/).

You can also search DevDocs with by typing “devdocs” into Chrome’s address bar and hitting tab. And DuckDuckGo has a special `!dd` command to search DevDocs as well.

Join me in welcoming Thibaut and DevDocs to the freeCodeCamp community by [tweeting at him](https://twitter.com/tibc).

Have fun, and happy coding!

