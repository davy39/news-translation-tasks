---
title: Why Software Documentation Is Part Of Accessibility [with examples]
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-06T11:54:13.000Z'
originalURL: https://freecodecamp.org/news/documentation-is-part-of-accessibility-439d7750267d
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb37d740569d1a4cac934.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technical writing
  slug: technical-writing
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anna Monus

  Accessibility is mostly discussed as a way to enable people with disabilities to
  use a tool (website, application, etc.) with as little information loss as possible.
  However, the accessibility needs of users who don’t have any disabilit...'
---

By Anna Monus

Accessibility is mostly discussed as a way to enable people with disabilities to use a tool (website, application, etc.) with as little information loss as possible. However, the accessibility needs of users who don’t have any disabilities but experience other kinds of hardships are less widely discussed.

The lack of knowledge on a given subject is such a hardship, therefore providing quality technical documentation to users is an essential part of accessibility. In case of open-source tools, it’s probably even more important, as here, users don’t simply want to use the tool but many of them would also contribute to the code.

If you have ever had to use poorly documented software you know what I am talking about. Boring, badly structured, and user-hostile documentation can make people give up on a tool, just like an overly complicated purchasing process can result in shopping cart abandonment on eCommerce websites.

### Two types of technical documentation

Essentially, there are two types of technical documentation (however, you might find more, for instance [this article](https://www.rhyous.com/2011/07/21/the-different-types-of-technical-documentation-for-software-and-why-each-is-important/) mentions eight types):

1. documentation created for end-users
2. documentation created for developers

### End-user documentation

Companies tend to focus more on end-user documentation; you can find [nice and user-friendly examples](http://blog.screensteps.com/10-examples-of-great-end-user-documentation) of this kind of docs. However, even the best designed end-user docs tend to lack crucial accessibility features (e.g. sufficient color contrast, or captioning for instructional videos).

For instance, have a look at Salesforce’s [Learning Centre](https://www.salesforce.com/uk/learning-centre/). Overall, they did a great job with the docs. The information is well-structured and logical, and the docs don’t use too much technical jargon.

On the other hand, you will find that some of the necessary accessibility features are lacking, for example, links are distinguished only by color instead of providing a [non-color designator](https://www.annalytic.com/link-accessibility-colors-not-enough.html) such as an underline.

![Image](https://cdn-media-1.freecodecamp.org/images/kn55f8Ng19dc8tTw0PU0LBsKrOdr99L1H04A)

### Developer documentation

Technical documentations created for developers had been in a poor state for many years. They didn’t simply lack accessibility features but were also badly structured, used unreadable fonts and small line height, lacked table of contents, and were visually unappealing on the whole.

The rise of video tutorials made the scene of developer docs much better, as at about the same time, well-designed documentations began to appear.

The first developer documentation I really liked was the [Zurb Foundation Docs](http://foundation.zurb.com/sites/docs/). It has improved a lot since I first saw it, but even the earlier versions were designed, written, and structured in a way that made me want to learn.

![Image](https://cdn-media-1.freecodecamp.org/images/nxLE9Px7tWxRaIx-wp9XxTfdIS37cMYre9By)

[Atlassian’s Git Tutorials](https://www.atlassian.com/git/tutorials/what-is-version-control) constitute another good example for user-friendly developer documentation. They are just as well-structured as the Foundation Docs but also come with great explanatory illustrations (in SVG!) and a [downloadable cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet).

![Image](https://cdn-media-1.freecodecamp.org/images/tqHAz27roCXcLj49xp9vNTJxAJXBkWXzmAaT)

While both Foundation Docs and Git Tutorials present the information in a way that is accessible to users without any knowledge on the subject, you will find some accessibility problems in both, that may hinder users with disabilities (for instance, color contrast problems).

### Two levels of documentation accessibility

Basically, documentation accessibility has two levels:

1. The docs need to be accessible for users without sufficient knowledge of the tool.
2. The docs need to be accessible for users who may have different disabilities.

The two levels can also intersect, as there can be users who are affected by both problems (i.e. don’t have the sufficient knowledge plus have a disability).

The three examples I mentioned in this article (Salesforce, Foundation, Atlassian) handle the first level of documentation accessibility really well, as they:

* don’t use technical jargon, or if they do they give the necessary explanation
* provide menus / widgets / table of contents to ease navigation
* structure pages (careful typography, enough white space, vertical rhythm, etc.)
* provide illustrations or instructional videos
* provide examples of usage, demos, or code snippets

They also partially implement the second level of accessibility, however you’ll find issues here and there with things such as color contrast, link visibility, video captioning, etc.

### Can documentation be perfectly accessible?

I don’t know if perfectly accessible docs exist or not, but if they do they should implement both levels of documentation accessibility. It’s certainly not something easy to accomplish, as there are so many things to pay attention to.

However, documentation accessibility is still an important part of accessibility. First, because users with disabilities shouldn’t be excluded from adopting new technologies, but also because it greatly impacts how many people are willing to go the extra mile to pick up a new tool.

_You can read more of my blog posts on [annalytic.com](https://www.annalytic.com/documentation-part-of-accessibility/)._

