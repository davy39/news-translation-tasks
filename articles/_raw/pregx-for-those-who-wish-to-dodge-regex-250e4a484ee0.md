---
title: Do you hate regex? Well then, I have a solution for you…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T00:54:09.000Z'
originalURL: https://freecodecamp.org/news/pregx-for-those-who-wish-to-dodge-regex-250e4a484ee0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FJQFtX72NUMaHFebSRIgHw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Regex
  slug: regex
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Bukhari Muhammad

  The following piece presents my latest package on NPM, which is also available on
  GitHub as a repository. I wrote it in hope that it be beneficial to all who may
  need it.

  So… What is PregX?


  PregX — Largest library of popular & co...'
---

By Bukhari Muhammad

The following piece presents my latest [package](http://npmjs.com/package/pregx) on NPM, which is also available on GitHub as a [repository](https://github.com/bukharim96/pregx). I wrote it in hope that it be beneficial to all who may need it.

### So… What is PregX?

![Image](https://cdn-media-1.freecodecamp.org/images/ICoOkdsuimq4rxqdfwgcv6spCf01dvDeG2rP)
_PregX — Largest library of popular &amp; commonly used Regex patterns for JavaScript_

**PregX**, contrary to common belief, refers to: _Popular Regex_ _(Patterns)_, and not Perl Regular Expressions. Speaking of “common”, it is a library — written in JavaScript — that aims to be the largest collection of popular and common **regular expressions**.

Developers unused to regular expressions may face difficulties when trying to use complex **regular expression** notations and syntax. This library should help these developers achieve common tasks that require regular expressions. It leverages the pre-written patterns that we most frequently use in our projects.

### Why not write your own regular expressions?

![Image](https://cdn-media-1.freecodecamp.org/images/XgBx9MtbjoGJVVDMpfC-6DjBD6jHEuBXcR9J)
_[Image source.](https://www.flickr.com/photos/sirexkat/1128067974/in/album-72157601455231098/" rel="noopener" target="_blank" title=")_

The [Don’t Repeat Yourself (DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) approach is that repetition in code should be reduced via automation or abstraction. This is a fundamental principle of programming that ought to be obeyed whenever possible. Since duplication wastes both time and space, I went to some length to find a solution not just for myself, but for others as well.

What’s the point behind the _DRY_ principle if we keep reinventing bread every time a Tom, Dick or Harry discovers wheat?

I found common **regex** patterns. My idea was to abstract each of these popular patterns into a useful pure function of its own. This abstraction would not mutate or alter the state of the given string to match. Each function would then return an array of the items matched in the given string.

**PregX** was not designed to oppose originality. It has two simultaneous aims. One aim is to reduce the time that developers spend on trying to use **regex**. The other aim is to avoid complexity where it does not belong.

Though, guilty as charged, this package is also (indirectly) meant for those lazy-bums that always evade writing regular expressions.

Then again, you may need to write your own **regex**. Your approach totally depends on the needs of the task at hand.

### When should I use PregX?

Good question, when should you?

**PregX** can be used when inbuilt functionality fails to achieve, or is inadequate for, your complex desired outcome. Some might argue that **regex** could achieve this task.

**Regex** might shorten the code effectively. However, it can also lessen the readability of your code, depending on the complexity of the task at hand.

Why not opt for a ready baked solution that’s abstracted into a useful function?

This is where **PregX** comes into play. Patterns are abstracted in functions in line with the [_Functional Programming Paradigm_](https://en.wikipedia.org/wiki/Functional_programming)_._ This makes it the go-to solution for common regex tasks. Using **PregX** achieves the same outcome, without settling for less readable code or reinventing bread.

A broadly accurate principle is: Whatever pattern you’re cooking up, there’s probably a person who’s already written it. **PregX** takes this rule of thumb, by accumulating such patterns for the greater bunch of **non-regex** oriented developers.

Then again, this all depends on what you’re comfortable with. If you’re not hot at writing your own patterns then this is an easy way out.

### When not to use PregX

If you seek an out-of-the-ordinary , pattern that’s super specific to your needs, then **PregX** simply is not the answer. **PregX** is not intended to replace **regex**, that’d be super silly. **Regex** will always remain the best solution when it comes to precise or explicit tasks of this nature. Bottom-line, a good developer will know when to use a loaf tin and when to use a bakery.

### The simplicity and usefulness of PregX

I thought I’d showcase a few practical code samples to demonstrate the awesomeness of this library. That is, if you’re not yet convinced by all the boring talk I’ve written so far. ?

#### Credit card example

The following example shows how to match a credit card number using a string, with `getCreditCardNumber()`. One could even specify the type pf credit card to match, via the `cardType` property of the function’s `config` object. By default, this function matches Visa card numbers. Check this sample:

![Image](https://cdn-media-1.freecodecamp.org/images/OcbvsOcAojZxXioMkhtXRuVFmmjK9l3WqU9K)
_`getCreditCardNumber()`_

Not impressed? I’ve got enough tricks up our sleeve to entice you.

#### Postal code example

If the above code sample didn’t do it, then this one will.

The pattern of the `getPostalCode()` function is among the many patterns that I’ve written myself. There are lots of solutions out there that attempt to do this. None match **PregX**’s standard.

I’ve used [Wikipedia’s Postal Code List](https://en.wikipedia.org/wiki/List_of_postal_codes) as a reference, and cooked up **PregX**’s single greatest function. With **support for matching the postal addresses of over 150 countries**, this function — at least for me — remains the best solution to achieve this common task. Take a look:

![Image](https://cdn-media-1.freecodecamp.org/images/s9cA9wloQL53PU3W2BTw2KiFz-2zWgSWeKs8)
_`getPostalCode()`_

### Currently Supported Patterns

**PregX** supports a curated list of 35 (and counting)different patterns, all well tested to match their appropriate text. Here’s a list of the supported patterns:

![Image](https://cdn-media-1.freecodecamp.org/images/EUb230uJGrGSbnKlsrTVvxkeaOXUUUNNXyLv)
_Supported Patterns_

### Convinced?

These are only two examples of the many patterns that this library contains. For documentation, examples of usage, and more information on **PregX**, check its [repository](http://github.com/bukharim96/pregx) on GitHub. Better yet, clone it or test it out by simply installing it via NPM:

```
npm install pregx --save
```

I’d love to hear your feedback on this package. **PregX** currently consists of 35 patterns, I hope it reaches ~100. So, feel free to contribute any useful patterns. [Star it on git](https://github.com/bukharim96/pregx/).

This is my first open source project on [NPM](http://npmjs.com/package/pregx), but not my first on GitHub. Love it, [fork it](https://github.com/bukharim96/pregx/). Hate it, critique it. To get updates on the progress of this repository along with some cool JavaScript / React related tips, follow me on twitter: [@bukharim96](https://twitter.com/bukharim96)

Thanks for reading this post.

Peace.

