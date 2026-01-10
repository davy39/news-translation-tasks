---
title: CSS tips that you likely won’t see in any tutorial
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T21:43:09.000Z'
originalURL: https://freecodecamp.org/news/css-tips-that-you-likely-wont-see-in-any-tutorial-3af201315a76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5YzOyUp5pIiHVAu8OQhGtg.jpeg
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cristian Traina

  There are CSS rules that you can find in any tutorial.

  And then there are CSS rules that you don’t find in tutorials, but that you faced
  immediately when you started coding. I’m sure you already googled about how to vertical
  align ...'
---

By Cristian Traina

There are CSS rules that you can find in any tutorial.

And then there are CSS rules that you don’t find in tutorials, but that you faced immediately when you started coding. I’m sure you already googled about how to vertical align an element and how to create that complex layout. We won’t talk about this.

Finally, there are those CSS rules that you haven’t met in any tutorial and you could not know. I’ve collected these tips over time, and now I’ve decided to write an article, hoping they can be useful for other people.

The following is what CSS tutorials never taught me.

### Padding-top is relative to parent’s width

How many times have you used relative units in CSS? I’m a big fan of them, because they let you build a responsive website without messing around too much with media queries. If you want to set an element’s height as half of the parent’s height, writing `height: 50%` is enough.

You can use relative units everywhere. If you want to add some distance between two vertical elements, you can write `margin-top: 15%` and it will make the margin. The distance will be 15% of the parent height. I think you already know this, and I don’t want to waste your time. But maybe you don’t know that it’s not so trivial.

In some situations, it’s better if you [use padding in place of the margin](https://stackoverflow.com/questions/2189452/when-to-use-margin-vs-padding-in-css). But when you set `padding-top: 15%` … what the heck?

It doesn’t work as expected. This is not relative to the parent’s height. What’s happening?

#### **Solution**

It’s relative to the parent’s width.

Do you want a practical demonstration? Here it is:

Just play around with changing the parent’s width, and see how the child’s padding is affected.

It can look weird at first, but there is actually a meaningful reason why it happens. You can discover it by reading the [CSS specifications](https://www.w3.org/TR/CSS2/box.html#propdef-padding-top)…

No, I’m joking — there is no explanation why this happens. Or, at least, I didn’t find it anywhere. It just works like this, so keep it in mind.

Even though we might not understand the reason why the engineers did it, we can use this feature to our advantage. If we have an element and we set the following:

```
.parent {  height: auto;  width: 100px;}
```

```
.child {  padding-top: 100%;}
```

Then, the element’s height will be as much as the child’s height, since we set `height: auto`. The child’s height, on the other hand, will be the same as the parent’s width, since we set `padding-top: 100%`. The result is a square, and the element will keep the same ratio at any size.

Here is a working example:

If you change `padding-top: 100%` with any other percentage, you will get a rectangle. Also, if you change the width, the ratio is always kept.

### Transform can stack rules

If you studied computer science, you remember for sure that hideous turtle and its rectractable pen. This educational concept is more formally known as [turtle graphics](https://en.wikipedia.org/wiki/Turtle_graphics), and its goal is to guide the turtle on a path through simple instructions, step by step, such as “20 steps ahead” and “rotate 90 degrees”.

What if, using CSS, you could say a block to move “20 pixels right” in relation to its current position, and not its starting position? And what if I say that you can do it using the `transform` property?

Many developers don’t know that `transform` can pile up more than one rule, and the `n+1`th rule will be relative to the position reached at the `n`th rule, rather than its starting position.

Are you confused?

Maybe this pen can clear your mind:

Note that we didn’t use any JavaScript variables to store the current position or the current rotation. That information isn’t kept anywhere! The solution is simple, if you write:

```
transform: translateX(20px);
```

And then you add a further rule:

```
transform: translateX(20px) translateX(40px)
```

The second rule won’t overwrite the first one, but they will be applied one by one, in sequence. The fact that they are applied in sequence is important. When you rotate an element, you also rotate the reference system, and further rules will be relative to the new reference system. So:

```
transform: rotateZ(20deg) translateX(30px)
```

will be different than:

```
transform: translateX(30px) rotateZ(20deg)
```

You can also combine different units. For example, you can center a 600 pixel large div in this way:

```
transform: translateX(50vw) translateX(-300px)
```

But if you aren’t going to animate it, maybe `calc()` is a better alternative.

If you are wondering about the turtle, I created this other snippet that re-creates the dynamics:

Unluckly, it doesn’t draw yet. But if you want you can always implement the _pen_ function.

### Margins and paddings go from midday to midnight

This is easy, and many of you are going to think it’s trivial, but I saw so many people struggling with quadruplas that I stopped taking it for granted.

Many developers don’t know that almost every CSS property has a shorthand alternative. Other developers know it, but they keep using specific properties because they never remember the order.

Let me give you a tip:

**Margins and borders go from midday to midnight.**

I can explain it better. You can for sure use:

```
padding-top: 3px;padding-left: 6px;padding-right: 6px;padding-bottom: 3px;
```

But, you can also use the shortand alternative:

```
padding: 3px 6px 3px 6px;
```

The rule to remember the order is easy — just watch this clock:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zxqYpjLODfi3RKIZ3tMxWg.png)

Start from 12:00 and proceed clockwise. You’ll get the correct order.

If, instead, you use only two values:

```
padding: 2px 4px;
```

The browser engine will expand it, repeating the couple:

```
padding: 2px 4px 2px 4px;
```

And, in the end, if you use three values:

```
padding: 2px 4px 6px;
```

The browser engine will use the middle value both for left and for right, just like if you wrote:

```
padding: 2px 4px 6px 4px;
```

### Background supports multiple images

This is one of the least known properties, even though it’s widely supported.

You know that you can specify a image URL inside the `background` property, but if you ever need it, you can actually insert as many images as you want. What you need to do is separate them with a comma:

```
background: url('first-image.jpeg') top left,            url('second-image.jpeg') bottom right;
```

Why can this be useful? What do you think about Linus Torvalds in front of a CSS-generated sunrise?

You can also square a rectanglular image, adding those shaded borders that are very famous in Instagram. To achieve this, I needed to repeat the same image twice and zoom the background image 5x:

### Detect touchscreen devices

Thanks to media queries, we can make our websites responsive and let the layout adapt to many screen sizes. But this is not enough!

Smartphones, tablets, and classical personal computers are different in nature. No matter the screen size.

On a touchscreen device, you pin, swipe, and pinch, and tools like [HammerJS](https://hammerjs.github.io/) help you. With a mouse you only click, but with higher precision. If you made your website adaptable to different screen sizes, maybe you could consider making it responsive in other directions as well, and support different input types!

You don’t need complicated JavaScript code to detect the user-agent. All you need is CSS:

```
@media (any-pointer: fine) {  /*    These rules will be applied to not-touchscreen devices  */}
```

```
@media (any-pointer: coarse) {  /*    These rules will be applied to touchscreen devices only  */}
```

Here is an example:

**Pro tip:** You don’t need a smartphone to test the rule, you can simulate a touchscreen device on Google Chrome dev tools just by clicking this icon:

![Image](https://cdn-media-1.freecodecamp.org/images/1*_GCh44P5LmsiXNq1UEx2VQ.png)

I’ve found it very useful and I don’t know why it hasn’t spread, although it’s decently supported. For example, I used it in a carousel to hide _chevrons_ icons in touchscreen devices in order to provide a more native experience.

And, in the end, you can also provide a file `touchscreen.css` and import it conditionally:

```
@import url('touchscreen.css') screen and (any-pointer: coarse);
```

**Note:** this currently not supported by Firefox, as you can see on [caniuse.com](https://caniuse.com/#search=any-pointer)

### Margins like to collapse

![Image](https://cdn-media-1.freecodecamp.org/images/0*9Y4R8_iMsLJNkFX4.jpg)

> **And keep an eye on the staircases. They like to change.**

> _Percy Weasley — Harry Potter_

I like CSS: it’s a clear, regular, and elegant language — everything a developer could ever ask for.

You apply a rule, and it works. But when I thought I knew CSS, this happened:

What the heck is happening here? You probably expect that the text will have a margin **inside** the header, but it tries to pull the header down instead. This is not what I wanted.

Later, I discovered that margins like to collapse.

What does that mean? Let’s suppose we want to create the following nested layout:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ga5LtmwuzDy1ywToOBWg5g.png)

So, we created the markup for three elements and we set a different height and a different margin-top for each of them. It should work, right? Wrong.

If you do it, your browser will notice three adjacent margins blocks, and it will want to join them in one, unique, big margin block.

Therefore, the result will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*pyuE0l73A-G5RRS1iUP6rQ.png)

Why does this happen? I don’t know. This is an historical feature of CSS. I suppose that, when CSS was initially standardized, margins weren’t a big issue and layouts weren’t as complicated as they are nowadays. So engineers might have thought it was a useful feature. Now it makes no sense at all.

If you’ve developed in CSS for years, and you’ve never met this issue, the reason is that margins collapse only when:

* margins are vertical (it doesn’t happen for horizontal margins)
* outer elements don’t contain text or other content
* no padding or borders are set
* display is “block”
* overflow is different than “initial”
* margins are not negative

And the list continues. If you encounter this problem, you can just negate one of these conditions (except the first one) and the margins will be tamed. You can also avoid using `margin-top`, and use `top` and `padding-top` instead.

Note that his can happen also for sibling elements. If you have two sibling elements one on the top of the other, and you set `margin-bottom: 30px` to the first one and `margin-top: 60px` to the second one, the smallest will collapse. The result margin won’t be 30+60=90px, but it will be max(30, 60) = 60px.

### Final thoughts

That’s all! I hope I didn’t waste your time with this article, and that you learned something of value.

If you liked the post, you can click the “applause” button that appears on your left. You can give me up to 50 claps :D

If you have questions, issues, or you just want to tell me what the tutorial didn’t teach you, just leave a comment in the below section and your concern will be appreciated!

— Christian Vincenzo Traina

