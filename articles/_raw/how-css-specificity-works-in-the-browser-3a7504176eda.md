---
title: How CSS specificity works in the browser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T23:39:14.000Z'
originalURL: https://freecodecamp.org/news/how-css-specificity-works-in-the-browser-3a7504176eda
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wH2JSH_fw4oiAH2eqTg4qA.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Michael Ozoemena

  A lot of people find CSS really difficult. They blame that on a number of reasons
  like they aren’t wired to understand CSS or CSS is bad or any number of other reasons.
  But most people find CSS difficult because they haven’t taken...'
---

By Michael Ozoemena

A lot of people find CSS really difficult. They blame that on a number of reasons like they aren’t wired to understand CSS or CSS is bad or any number of other reasons. But most people find CSS difficult because they haven’t taken the time to really learn it. If you are reading this, it’s probably because you are interested in becoming better at CSS, and that is awesome!

#### What is CSS specificity?

Have you ever written a style and it just wasn’t working, so you add `!important` (or don’t) and still it didn’t work? So then you take a look at the Devtools only to find that some other style somewhere is overriding your style?

Well, that’s CSS specificity at play there! It’s how the browser chooses which of your competing selectors to apply to an element. When your browser sees that two or more of your selectors match the same element and the selectors have conflicting rules in them, it needs a way to figure out which one of the rules to apply to that element. The way it does that is through this thing called “CSS specificity value”.

Before we get deeper into CSS specificity, you need to **note** these things:

1. CSS specificity is only important when multiple selectors affect the same element. The browser needs a way to figure out what style to apply to a matching element when there are conflicting property values, and CSS specificity is the way it does that.
2. When two or more matching selectors have the same specificity value, the browser picks the “most recent” matching selector — the selector which occurs closer to the bottom of the list of matching selectors. The next point explains what “list of matching selectors” is.
3. The browser forms the “list of matching selectors” by combining all the styles on a web page and filtering out all the styles that do not match the “currently-being-styled” element. The first selectors in the stylesheet are at the top of the list and the last selectors are at the bottom of the list.
4. The `style` property on an element has a greater specificity value than selectors in stylesheets except when there is `!important` in the stylesheet selector.
5. Using `!important` (which is considered bad practice in certain cases) alters the specificity of a selector. When two selectors have equal specificity, the selector with `!important` wins. And when they both have `!important` the “most recent” selector wins.

#### The specificity value.

Now that we have those things out of the way, we can now go into how the browser determines the specificity values of a selector.

The specificity of a selector can be represented as a 3-digit string, delimited with a hyphen (or anything you want): “2–4–1”. The first digit is the number of `ID` selectors present, the second is the number of class selectors, attribute selectors, and pseudo-classes present, and the third is the number of type selectors and pseudo-elements present. For example:

```
#red.blue // 1-1-0
```

```
#green // 1-0-0
```

```
div.yellow#red // 1-1-1
```

```
.red.blue.yellow // 0-3-0
```

#### Determining the most “specific”

In order to determine which selector has more specificity, you can compare each of the three values.

Say you have `1 - 1 - 1` and `0 - 3 - 0`, like the last two examples, and you need to determine which one has more specificity. You first compare the last values `1` and `0`, and in this case `1` wins. That means at this point `div.yellow#red` has a greater specificity value…but we aren’t done comparing values.

Next, you compare the second values `1` and `3`, and `3` wins and again. At this point `.red.blue.yellow` has a greater specificity value but we still aren’t done yet.

Finally, we compare the first values, `1` and `0`, and `1` wins so `div.yellow#red` has more specificity than `.red.blue.yellow`.

This is how the browser determines the CSS specificity of a selector and it gives a good explanation of why no number of class selectors can override an `ID` selector.

#### Little warnings

There are three “gotchas” I’d like to talk about:

1. Earlier, I mentioned that the second number in the three-number sequence of specificity value _“is the number of class selectors, attributes selectors, and pseudo-classes present”_ and that is true in all cases except for when it’s the `:not()` pseudo-class we are talking about. When it’s the `:not()` pseudo-class, we don’t count it, we simply ignore it. But the selectors inside of it aren’t also ignored, they are counted normally.
2. CSS specificity understands the “form” of a selector. This means that when you have `*[id="yellow"]` and `#yellow`, the former is treated as an attribute selector (and it is) even though they both basically are selecting the same thing.
3. The universal selector `*` on its own isn’t counted towards the specificity value of a selector. In the point above, the `[id="yellow"]` part of the selector is what actually counts.

#### Conclusion

I hope that this article was easy to understand and has helped you gain a better understanding of how CSS specificity works. Now you can go about looking at styles and just being able to tell how “specific” a style is.

If that’s not the case and you have any questions or feedback, I’m happy to have a discussion with you in the comments section or on twitter [@theozmic](https://twitter.com/theozmic).

Do remember to leave a clap or two or fifty if you enjoyed this article.

