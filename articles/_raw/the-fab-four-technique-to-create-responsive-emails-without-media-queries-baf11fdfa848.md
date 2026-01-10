---
title: The Fab Four technique to create Responsive Emails without Media Queries
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-11T18:34:38.000Z'
originalURL: https://freecodecamp.org/news/the-fab-four-technique-to-create-responsive-emails-without-media-queries-baf11fdfa848
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8MfWNObJP1mFnYJzKkdflQ.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: email
  slug: email
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Rémi Parmentier

  I think I found a new way to create responsive emails, without media queries. The
  solution involves the CSS calc() function and the three width, min-width and max-width
  properties.

  Or as I like to call them all together: the Fab Fo...'
---

By Rémi Parmentier

I think I found a new way to create responsive emails, without media queries. The solution involves the CSS _calc()_ function and the three _width_, _min-width_ and _max-width_ properties.

Or as I like to call them all together: the Fab Four (in CSS).

![Image](https://cdn-media-1.freecodecamp.org/images/1*8MfWNObJP1mFnYJzKkdflQ.png)
_calc() &amp; width &amp; min-width &amp; max-width, aka The Fab Four (in CSS)._

### The problem

Making responsive emails is hard, especially since email clients on mobile (like Gmail, Yahoo or Outlook.com) don’t support media queries. An [hybrid approach](http://labs.actionrocket.co/the-hybrid-coding-approach), a [Gmail first strategy](https://julie.io/writing/gmail-first-strategy-for-responsive-emails/), or [a responsive email without media queries](http://webdesign.tutsplus.com/tutorials/creating-a-future-proof-responsive-email-without-media-queries--cms-23919) are great ways to adapt to this situation.

That last approach has been my favorite so far. The big idea is to have columns as _<d_iv>s with a fixed width aligned _with “display:inline-_block”. Once a screen can no longer contain two blocks side by side, they will naturally flow below each other. But I’ve always had a problem with this.

Once all the blocks are stacked, they don’t take the full width of the email.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ybAI7RS4xjmQY3Y_B4jUnw.png)
_Without media queries, columns can stack up but not grow full width. [Illustration by Nicole Merlin](http://webdesign.tutsplus.com/tutorials/creating-a-future-proof-responsive-email-without-media-queries--cms-23919" rel="noopener" target="_blank" title=")._

I’ve been looking for ways to solve this problem for a long time. Flexbox is a great contender, but unfortunately [Flexbox support in an email](https://medium.com/@hteumeuleu/using-flexbox-in-an-email-4b1aa7a69886#.83apq23wx) is abysmal.

### A solution

#### _Remembering width_, _min-width_ and _max-width_

On top of the _calc()_ function, the solution I found involves these three CSS properties. In order to fully understand how it works, here’s a reminder of how _width_, _min-width_ and _max-width_ behave when used together (as [clearly summarized](http://goetter.tumblr.com/post/64119638003/quiz-parce-que-la-taille-%C3%A7a-compte) by fellow french front-end developer Raphaël Goetter).

* If the _width_ value is greater than the _max-width_ value, _max-width_ wins.
* If the _min-width_ value is greater than the _width_ or _max-width_ values, _min-width_ wins.

Can guess what the width of a box with the following styles would be ?

```
.box {    width:320px;    min-width:480px;    max-width:160px;}
```

_(Answer : the box would be 480px wide.)_

#### Introducing calc() and the magic formula

Without further ado, here is an example of the Fab Four to create two columns that will stack and grow below 480px.

```
.block {    display:inline-block;    min-width:50%;    max-width:100%;    width:calc((480px — 100%) * 480);}
```

Let’s break it down for each _width_ property.

```
min-width:50%;
```

The _min-width_ property defines our column widths on what we could call our desktop version. We can change this value to add more columns (for example, 25% for a four columns layout), or set columns with fixed pixel widths.

```
max-width:100%;
```

The _max-width_ property defines our column widths on what we could call our mobile version. At 100%, each column will grow and adapt to the full width of their parent container. We can change this value to keep columns on mobile (for example, 50% for a two columns layout).

```
width:calc((480px — 100%) * 480);
```

Thanks to the _calc()_ function, the _width_ property is where the magic happens. The _480_ value matches our desired breakpoint value. The 100% corresponds to the width of the parent container of our columns. The goal of this calculation is to create a value bigger than our _max-width_ or smaller than our _min-width_, so that either one of those property is applied instead.

Here are two examples.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zCzf5ZChfB1WB5FGULzpig.png)

With a parent of 500px, the calculated _width_ equals -9600px. It is smaller than the min-width. So the min-width of 50% wins. Thus we have a two columns layout.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PJANsECXH1VCJ5UxxaJ-5w.png)

With a parent of 400px, the calculated _width_ equals 38400px. It is bigger than the min-width, but max-width is smaller. So the max-width of 100% wins. Thus we have a one column layout.

### Demo

Here is a demo of what this technique can do.   
You can [see the full demo online here](http://emails.hteumeuleu.fr/wp-content/uploads/2016/02/the-fab-four.html) (or [on Litmus Builder](https://litmus.com/builder/9c0fce1) or [on CodePen](http://codepen.io/hteumeuleu/pen/VaZgqg)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*YcVo7AGzJekmg5eupqLK0A.png)
_Illustrations by [Elias Stein](https://dribbble.com/shots/2012203-Paul-George" rel="noopener" target="_blank" title=")_

And here are two screenshots of this demo in Gmail, on the desktop webmail and on the mobile app on iOS. Same code, different render.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GUknMjQDihG2WkqHIEBBUA.png)
_The Fab Four demo as seen on the Gmail desktop webmail and on the Gmail iOS app._

In this demo, I’ve set a few examples of different grids (with two, three, four columns). The first grid, with the images, is built to go from four columns on desktop to two columns on mobile. The other grids are built to grow full width on mobile.

Also, notice how the title switches from a left aligned position on desktop to a centered position on mobile. This is achieved by giving the title a fixed width of 190px and a “_margin:0 auto;_” to center it. On desktop, the title’s parent container has a min-width of 190px applied, so the logo stays on the left. On mobile, the parent container grows full width, so the logo becomes centered.

A great aspect of this technique is that, since everything is based on the grid’s parent width, an email can adapt even on a desktop webmail. For example, on Outlook.com, no matter if you chose to have the reading pane on the bottom or on the right, the email will correctly responds to the reading pane’s width. This would be impossible to do with media queries.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lbGOlHr5J-I2XSlbLrfQCg.png)
_On Outlook.com, the email adapts to the different views._

### Support

In browsers, calc() is [well supported since IE9](http://caniuse.com/#search=calc()). Turns out, calc() also has a pretty good support in email clients. It works in Apple Mail (on iOS and OS X), Thunderbird, Outlook (iOS and Android apps), Gmail (webmail, iOS and Android apps), AOL (webmail), and the old Outlook.com (still present in Europe).

#### The old Outlook.com

Outlook.com has one small quirk, though. The webmail will filter every property with a _calc()_ that includes any parenthesis. This means that “_calc(480px - 100%)_” is supported, but “_calc((480px - 100%) * 480)_” is not. Since my initial formula involves parenthesis, we need to refactor it to avoid parenthesis. So the formula to support the old Outlook.com looks like this.

```
width:calc(480px * 480 — 100% * 480);
```

#### Unsupported clients

Of course, _calc()_ isn’t supported in old email clients like Lotus Notes, or the latest Outlook for Windows (using Word’s HTML rendering engine). It also won’t work on Outlook Web App (both Office 365 and the new Outlook.com) and Yahoo (webmail, iOS and Android apps). These two will strip out any property involving a _calc()_.

#### Fallbacks

In these cases, I would suggest duplicating all involved properties with fixed width values for clients that don’t support _calc()_. In order to hide The Fab Four from those clients, I advise to use _calc()_ functions, even if it’s not technically useful. Our first example would look like the following.

```
.block {    display:inline-block;    min-width:240px;    width:50%;    max-width:100%;    min-width:calc(50%);    width:calc(480px * 480 — 100% * 480);}
```

#### Outlook Web App

However, Outlook Web App (both Office 365 and the new Outlook.com) has one more quirk of its own. When a _calc()_ function contains a multiplication (with the ‘_*_’ character), the new Outlook.com and Office 365 will remove the whole inline _style_ attribute corresponding. This means we need to calculate the multiplications by hand and only keep the resulting substraction. Here’s what the final calculation looks like for a 480px breakpoint.

```
width:calc(230400px — 48000%);
```

#### WebKit Prefixes

Older versions of Android (before Android 5.0) or iOS (before iOS 7) require _-webkit-_ prefixes in order to work. Our final version looks like the following.

```
.block {    display:inline-block;    min-width:240px;    width:50%;    max-width:100%;    min-width:-webkit-calc(50%);    min-width:calc(50%);    width:-webkit-calc(230400px — 48000%);    width:calc(230400px — 48000%);}
```

### Shortcomings and final thoughts

Like anything in the email development world, the Fab Four technique isn’t perfect. Here are a few limitations that I can think of:

* It won’t work on Yahoo. The desktop version of its webmail supports media queries, though. So we could improve things a bit by making a mobile first version of our email, and then enhancing it on desktop with media queries.
* You can only set one breakpoint. This might not be such a problem for emails though, as designs rarely go beyond 600px on desktop and don’t require more than one breakpoint to adapt on mobile.
* You can only diminish the number of columns from a desktop version to a mobile version. While this rarely happens, you couldn’t go from a four columns layout on mobile to a single column layout on desktop.
* The final version of the calculation (to support the old Outlook.com and degrade gracefully on the new one) is hard to read. Using a preprocessor and a mixin to generate all the required properties could be more than helpful.

I still think that this technique will come in very handy in a lot of cases, especially for Gmail optimizations. I’m sure there is also use cases for websites (like widgets, ads, …).

And I can’t wait to see what this will inspire you to create.

