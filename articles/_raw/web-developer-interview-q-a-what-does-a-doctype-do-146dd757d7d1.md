---
title: 'How to tackle your Web developer interview Q&A: what does a doctype do?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T22:42:47.000Z'
originalURL: https://freecodecamp.org/news/web-developer-interview-q-a-what-does-a-doctype-do-146dd757d7d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T2mgRWcGugiSXs_kRsRQVg.jpeg
tags:
- name: interview
  slug: interview
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Zuzana K

  One part of the interview process for a web developer position probably involves
  answering some questions. Yes, we are not only expected to do the web stuff, but
  we are also expected to know the web stuff.

  I am very capable of writing an ...'
---

By Zuzana K

One part of the interview process for a web developer position probably involves answering some questions. Yes, we are not only expected to do the web stuff, but we are also expected to know the web stuff.

I am very capable of writing an HTML document, using semantic tags, and following the best web standards, but there are things I never thought of learning.

I recently received a list of web developer interview questions, and when I first glanced at the list, my heart almost stopped.

* What does a doctype do?
* Are there any problems with serving pages as application/xhtml+xml?
* What’s the difference between feature detection, feature inference, and using the UA string?

Well, in all honesty, I couldn’t answer most of the questions.

I guess this is where a CS degree could come in handy.

But, as a self-taught developer, I focused on doing, rather than knowing. Since I am looking for a job myself, however, I thought it might be wise to prepare for a web developer interview and answer some of these questions.

So in the next I-don’t-know-how-many posts, I will take a question from a web developer interview (that has been very graciously provided by [Rose](http://www.verifyrecruitment.com/blog/index.php/tag/askrose/) from the Verify recruitment agency in Dublin, Ireland), and answer it to the best of my ability.

I am going to tackle some HTML, some CSS, and some JavaScript questions.

The answers will not be exhaustive, but they will hopefully give you and me a good head start, should we want to dig a little bit deeper.

### Question: What does a <doctype> do?

Doctype is the abbreviation for the “document type.” Duh, right? I mean, who would have thought?

But seriously, why do we need to specify the doctype when we save the document as an HTML file, which, surely, means that it is an HTML document? The thing is, you also need a <!doctype html> for a ‘.php’ page that includes HTML markup.

This is where it gets confusing. So let’s unpack it a little bit.

Doctype declaration tells the browser what kind of document to expect: HTML5, HTML4.0x, XHTML1.0 (Strict, Transitional or Frameset), XHTML1.1, [and others](https://www.w3.org/QA/2002/04/valid-dtd-list.html).

But why is it required?

For legacy reasons.

In the early days of the Internet, two main browsers were competing against one another. Netscape Navigator and Internet Explorer. They kept coming up with new features that were often incompatible with the other, already existing features or other browsers.

It was a difficult time for the developers (let’s all take a minute and count our blessings).

So the founder of the World Wide Web, Sir Tim Berners-Lee, founded the [World Wide Web Consortium](https://www.w3.org/) (W3C) to standardize the protocols and technologies used to build the web and to make life easier for developers and users alike.

The new protocols were great for the new browsers and implementations, but they would totally break the existing sites.

Enter Document Type Definitions (DTDs).

DTDs tell the parser how to translate the code into what you see on the screen so that the look is uniform across different browsers.

To render a HTML4.01 document, use this code at the very top of your document:

```
<!DOCTYPE HTML PUBLIC “-//W3C//DTD HTML 4.01//EN” “http://www.w3.org/TR/html4/strict.dtd”> 
```

To render a HTML5 document, include this code instead:

```
<!doctype html>
```

HTML5 is, admittedly, much easier to declare.

Using the doctype declaration is a requirement placed upon us by W3C; without it, the [HTML validators](https://validator.w3.org/) won’t work (because they won’t know what standard to check your code against) and the browser might render the document in a quirks mode.

Say what? A quirks mode?

If you don’t declare the doctype, browsers can interpret the document as something else other than HTML and switch into quirks mode, which is, basically, a mode for documents with no doctype declaration.

There can be a lot of quirks in the quirks mode; it can pretty much mess up how your document appears on the screen!

Quirks mode, almost standard mode, and the full standard mode is something I am going to look into next time.

For now, take care of your doctype and see you soon!

_If you have enjoyed this article and found it beneficial, please consider leaving me a comment or some claps. Thank you!_

