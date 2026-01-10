---
title: The Most Important CSS Concept to Learn
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-11T21:31:21.000Z'
originalURL: https://freecodecamp.org/news/the-most-important-css-concept-to-learn-8e929c944a19
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tf536ftkgQuDPEaiY4QVpg.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Emmanuel Ohans

  The Cascade is how CSS was designed from the very beginning, and there’s a reason
  it’s called CSS — Cascading Style Sheets!

  Sadly, CSS has a poor reputation for the same fundamental concept upon which it
  is built.

  But what exactly i...'
---

By Emmanuel Ohans

The **Cascade** is how CSS was designed from the very beginning, and there’s a reason it’s called CSS — Cascading Style Sheets!

Sadly, CSS has a poor reputation for the same fundamental concept upon which it is built.

But what exactly is the Cascade, and is it as bad as most people make it sound?

### Introduction

Let’s say John writes a bunch of CSS, and then gets on the browser to test it. To his surprise, the styles he wrote aren’t applied to the element he just styled, instead some other styles are!

You see that right there? That’s one of the worst things everyone complains about when they say “CSS sucks”.

With CSS, multiple styles can affect a single element. So, you have a `paragraph` on a web page. But this `paragraph` may be styled by any CSS block, literally.

It’s like having a global JavaScript variable that can be manipulated by any function within the code. A recipe for disaster, it seems.

But again, the Cascade forms the fundamental reasoning behind how CSS was created in the first place.

Embrace it?

Well, you can’t change it.

![Image](https://cdn-media-1.freecodecamp.org/images/QbB17Bt142xYZ-jJhnWY6obhbVf4NUnVBB6p)
_You’ve been there before, haven’t you?_

### What is the Cascade?

The cascade is how the browser determines what styles to apply to a particular element. It’s that simple, and it makes a decent interview question for a front-end developer.

Luckily, the nightmares associated with the cascade can be understood, as it is governed by just two factors:

1. The specificity of the element selectors
2. The order of the styles being written

Let’s have a quick look at those.

### Selector Specificity

You can liken selector specificity to how the human mind interprets instructions.

For example, consider the graphic below:

![Image](https://cdn-media-1.freecodecamp.org/images/Ns6cVPSUw99PFiQDIwswHX22V4GRGsb4BTeP)

If I said to you, “Pass me the red box.”, which would you pass to me? There’s two of them!

You may ask the follow up question, “Which of the boxes, a or b?”_._

Or you may even grab both boxes! Aren’t they both red boxes?

This is the situation the browser finds itself when dealing with specificity.

When you say, style the paragraph a red background color…

```
p {   background-color: red;}
```

Since there could be a lot of paragraph elements on the page, the browser goes, “what paragraph?”

The browser can’t ask you a follow up question, so it goes ahead and attempts to style **every** paragraph on the page with a `red` background.

However, if you had gone ahead to say, style the paragraph with a class name of `reddy` with a red background:

```
p.reddy {  background-color: red;}
```

That is a more specific request!

Now, the browser will style the specific paragraph element(s) you have requested.

That’s it!

Technically, the browser takes a look at every selector that targets a specific element and assigns “scores” to each of them, and the one with a higher specificity score wins.

The way it computes the scores is simple.

Assume the browser — while interpreting your CSS — had 4 goal posts.

![Image](https://cdn-media-1.freecodecamp.org/images/WGT1q9oEHZrKY1R0C2neEvZb45AIN6faLSs5)

1. For every inline style that targets an element using the `style` attribute, 1 goal is assigned to goal post `(a)`.
2. For every `id` selector, 1 goal is assigned to post`(b)`.
3. For every `class` selector, attribute selector, and pseudo-classes present, 1 goal is assigned to post`(c)`.
4. For every element selector and pseudo-element, 1 goal is assigned to post `(d)`.

The way I remember this is by using the acronym, SICAPEP:

![Image](https://cdn-media-1.freecodecamp.org/images/etustqZiytNdLrK6wF1nHWeWzVebiWS11SS4)

Upon assigning points, the total points are calculated by _concatenation_, as digits in a 4-digit number.

#### A Quick Specificity Example

Consider the following style declarations:

```
#nav .removed > a:hover {}
```

```
li:last-child h3 .title {}
```

How would the browser calculate the specificity “points” for these selectors?

`#nav .removed > a:ho`ver

Here’s the breakdown:

(a) There’s no inline style, so the score for the first goal post is 0.

(b) There’s one `id` selector, `#nav`, that’s a score of 1 for the second goal post.

(c ) There’s also one `class` selector, `.removed` and one pseudo-class selector, `:hover`, which sums up to a score of 2 for the third goal post.

(d) There’s one element selector, `a`, that’s a score of 1 in the fourth post.

Here’s the graphical representation of the scores.

![Image](https://cdn-media-1.freecodecamp.org/images/irhfWjR4Pr7OAMpUq8w3jwehB-N8mMV12WSA)

The total specificity score is concatenated as `0121`.

As with regular math, `0001` is smaller than `0005`, and `0121` is greater than `0021`.

Now, you understand how specificity is calculated.

Can you attempt to calculate the specificity for the other selector, `li:last-child h3 .title` ?

Let me know what you arrive at in the comment section :)

### Style Order

The second factor that influences the cascade is the order of styles. A really basic example can be seen with styling the same element in 2 different code blocks.

For example:

```
p.reddy {  background: red;}p.reddy {   background: blue;}
```

Even though both selectors have the same specificity, `0011`, the order of the ruleset comes into play.

The second declaration will overrule the former, and the paragraph will be blue and **not** red.

### Trick Question

Considering the document below, what would be the color of the link text?

```
<!doctype html> <html><head><title>Inline Styles and Specificity</title> <style type="text/css">    #nav-force &gt; ul > li > a.nav-link { 	color: blue;     };</style> </head>   <body>      <nav id="nav-force">	<;ul> 	 <li>	  <a href="/" class="nav-link" style="color: red;">		Link          </a> 	 </li>	</ul>       </nav>  </body> </html>
```

Blue or red?

Note that the link is styled both inline, and within the `<style>&l`t;/style> block.

Oh, if you’re feeling confident, just say the answer loud — to yourself.

But the real answer is, the inline style always wins. The goal is scored in the first post, which beats any goals in any of the other posts.

Why?

The final specificity will be in the order of thousands — 1000 — and that beats 9 goals in the second post. 1000 is greater than 0900.

**NOTE:** As pointed out by [Paul McCann](https://www.freecodecamp.org/news/the-most-important-css-concept-to-learn-8e929c944a19/undefined) in the comment section, the paragraph above is an over simplification. Have a look at [what he says](https://medium.com/@paul_mccann/be-careful-when-explaining-specificity-values-as-numbers-in-the-thousands-theyre-not-153502c3d97f).

### Conclusion

Hopefully, you’ve now being armed with the solid understanding of how the cascade works. Learning more advanced CSS will now probably come easier, and, more importantly, you now know where to look when you have those pesky bugs.

Catch you later!

### Ready to become Pro?

I have created a free CSS guide to get your CSS skills blazing, immediately. [Get the free ebook](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/K5WjZdNM7UT-fafz5nc2H8q-cRcH0Dc36Aja)
_Seven CSS Secrets you didn’t know about_

