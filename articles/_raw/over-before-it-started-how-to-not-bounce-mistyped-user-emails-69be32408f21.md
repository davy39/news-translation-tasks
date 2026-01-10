---
title: Over before it started — how to not bounce mistyped user emails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T18:25:09.000Z'
originalURL: https://freecodecamp.org/news/over-before-it-started-how-to-not-bounce-mistyped-user-emails-69be32408f21
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2Oo1Din32plTMdI8GypK4Q.jpeg
tags:
- name: marketing
  slug: marketing
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: writing
  slug: writing
seo_title: null
seo_desc: 'By Alex Peterson

  I type my email address so much that it has become muscle memory. Whenever I sign
  up for a newsletter or make a new account on a website, that’s what I use. And I
  barely, if ever, double-check to see that the address I typed is actua...'
---

By Alex Peterson

I type my email address so much that it has become muscle memory. Whenever I sign up for a newsletter or make a new account on a website, that’s what I use. And I barely, if ever, double-check to see that the address I typed is actually correct.

What if my fingers slip, or I miss a key?

This is not an uncommon occurrence. It’s a big problem for websites that rely on an email address to verify new users. But it’s an even bigger problem for websites that do not rely on email address verification.

This results in the emails companies send out bouncing.

The “hard bounce” rate is the number of invalid email addresses they send out as a percentage of valid email addresses.

### How big of a problem?

According to MailChimp’s [research](https://mailchimp.com/resources/research/email-marketing-benchmarks/), the “hard bounce” rate for companies sending emails can climb **over 1%**, while the average rate is **0.53%**. Those might not sound like big numbers, but the bounces can add up.

Think of the following emails you may send your customers,

* welcome email
* verification email
* drip campaign
* product announcements
* activity notifications
* App error alerts
* weekly blog roundups

And the list goes on…

As your website or app scales, the number of bounced emails scales with you.

Consistently bouncing emails will start to hurt your reputation as a sender. This will make it less likely that future emails you send will be trusted.

And you can’t email a user asking them to fix their information in your database if you…can’t reach them.

Unless you’ve established a secondary communication channel _beforehand_, users who sign up with an invalid email address are likely to be lost forever.

We should fix that.

#### What can be done?

Generally speaking, it’s a bad idea to edit a user’s input without them knowing about it.

For one thing, no machine is 100% perfect at guessing what [human beans](https://www.youtube.com/watch?v=-DSVDcw6iW8)actually want. But still, if you see something, say something.

I’ve found that giving users a gentle suggestion when the app notices that something’s _probably_ wrong tends to go over the best. That rule of thumb worked well at a former startup job and at the startup I’m currently building.

On my [website for online writing workshops](https://www.penmob.com), there is a simple plugin that helps prevent mistypings when a user signs up with their email address:

You can try it for yourself on the [login page](https://www.penmob.com/login). I’m going to show you how to set this up on your own website.

#### The Brass Tacks

This article assumes you are using [Browserify](https://medium.com/@christopherphillips_88739/a-beginners-guide-to-browserify-1170a724ceb2), [webpack](https://webpack.js.org/), or something similar to build NPM packages on your website’s front end. For example, Penmob uses the [VueJS webpack](https://vuejs.org/v2/guide/installation.html#CLI) installation.

First, install the [Mistyep package](https://www.npmjs.com/package/mistyep):

```
npm install mistyep --save
```

Then add it to your Log in/Sign up page:

```
var mistyep = require('mistyep');
```

Mistyep is a package that checks your user’s input against the most common email providers. The following code ensures that someone who mistypes “gnail” instead of “gmail” can still get in.

```
<input type="email" id="emailInput" />
```

```
<!-- ... -->
```

```
<script>// Get your user's email input from the login form.var emailInput = document.getElementById('emailInput').value;
```

```
// Mistyep returns the original value if no correction is found.var correctedEmail = mistyep.email(emailInput);
```

```
if (emailInput !== correctedEmail) {  // suggest the alternative spelling to the user.}</script>
```

It’s up to you to decide how to handle surfacing the suggestion to the user. In the GIF above, when `emailInput` is not equal to `correctedEmail` I display a box. The box contains the text `Did you mean {{ correctedEmail }}?`. Clicking on that box sets the original `emailInput` field equal to `correctedEmail`, which then hides the box.

Note that it takes a manual click from the user to actually apply the suggestion in this example. You’ll get into trouble pretty fast by auto-updating your database records with the suggestions that Mistyep finds.

You can also use Mistyep to check against an arbitrary list of words — not just email addresses. Feel free to check out the [code example](https://www.npmjs.com/package/mistyep#for-custom-words) and play with the [live demo](https://penmob.github.io/mistyep/).

#### Keep it simple

Validating email addresses is a [black hole](http://emailregex.com/) that I don’t recommend venturing too far down. Mistyep can’t catch every possible mistake (nothing can). But, it’ll provide the right suggestion to users who mistype their email address for the vast majority of cases.

I hope you find this useful for your own app or website. I post engineering insights, writing tips, and product announcements on [Twitter](https://twitter.com/pen_mob). For (infrequent) updates, [follow me](https://twitter.com/pen_mob). Happy building!

