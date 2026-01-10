---
title: About Blank – What Does about:blank Mean and Should You Get Rid of It?
subtitle: ''
author: Abigail Rennemeyer
co_authors: []
series: null
date: '2020-06-28T22:55:00.000Z'
originalURL: https://freecodecamp.org/news/about-blank-what-does-about-blank-mean-and-why-is-it-blocked-in-chrome-and-firefox
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/5f9c9a01740569d1a4ca22f9.jpg
tags:
- name: Browsers
  slug: browsers
- name: internet
  slug: internet
seo_title: null
seo_desc: 'Have you ever tried to go to a web page and instead see "about:blank" displayed
  in the address bar where your hoped-for URL should be?

  Don''t worry – it happens sometimes, and it isn''t anything bad. In this article,
  you''ll learn:


  what about:blank mea...'
---

Have you ever tried to go to a web page and instead see "about:blank" displayed in the address bar where your hoped-for URL should be?

Don't worry – it happens sometimes, and it isn't anything bad. In this article, you'll learn:

* what about:blank means
* what causes it to appear
* why you might want to use it
* whether you can get rid of it, and
* whether you need to worry about it 

So let's dive in.

## What is about:blank?

About:blank is a page that appears when your browser has nothing else to display. It's not a page on the internet, but rather something internally inside your browser.

The "about" part of what you see comes from your browser's [about URI or URL scheme](https://en.wikipedia.org/wiki/About_URI_scheme#:~:text=about%20is%20an%20internal%20URI,registered%20scheme%2C%20and%20is%20standardized.&text=An%20exception%20is%20about%3Ablank%20%2C%20which%20is%20not%20translated.). You can type "about:[whatever]" in the address bar to learn more information about your browser.

This works in most major browsers like Chrome, Firefox, Safari, Edge, Chromium, Internet Explorer, and so on.

For example, in Chrome you can type "about:dino" (which Chrome changes to chrome://dino) and you'll get Chrome's infamous "No Internet" dino message:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/about-dino.png)
_Wait, but why?_

If you've never played the no-internet dinosaur game, [learn how here](https://www.freecodecamp.org/news/how-to-play-the-no-internet-google-chrome-dinosaur-game-both-online-and-offline/) (and be prepared to waste hours of your life). But that's neither here nor there.

More usefully, for example, "about:about" displays a list of Chrome URLs:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/about-about-chrome.png)
_So many URLs (and there were more. Screenshots can only be so big.)_

Now back to the ":blank" part of about:blank. It just tells your browser to throw up that blank page when it doesn't have something else to display.

So it literally just shows you a plain white page with nothing on it:

![Image](https://www.freecodecamp.org/news/content/images/2021/06/about-blank.png)
_They named it well._

Now again, this isn't some location on the interwebs - it's a blank page your browser keeps on hand for just such a purpose.

## What causes about:blank?

So why does this blank page sometimes appear? Some of the main reasons are:

* If you've come across a bad link/URL
* If the browser doesn't know where to go or what to do, it has to do **something** – so it shows you about:blank
* If your browser detects something dangerous (like malware), certain browsers will display about:blank instead of proceeding into dangerous territory.

So as you can see, about:blank in and of itself isn't really anything to worry about. But if you're seeing it a lot, you might want to check your computer for malware. More on that below.

## Uses for about:blank

Now you might be wondering – why would I want this blank page to appear on purpose? Seems pretty useless.

Not so fast.

If you have limited bandwidth/a slow internet connection, you can set your browser's homepage to be about:blank. This way, whenever you open your browser or a new tab, it'll load super quickly without wasting a single resource or millisecond.

### How to set about:blank as your homepage

In Chrome, open the menu (those three little vertical dots in the upper right corner of the browser) and scroll down to the "On Startup" section (likely at the bottom):

![Image](https://www.freecodecamp.org/news/content/images/2021/06/make-about-blank-homepage-1.png)

Then select "Open a specific page or set of pages" (the third option) and type in "about:blank" to the text field that appears. 

Then when you open your browser or a new tab, you should see a blank white page.

### Other uses for about:blank

You might also want to make sure that, when you open up your browser, no tabs or anything from your previous browsing session were preserved. 

This is helpful from a privacy perspective, and also allows you to start a browsing session without internet, which uses less bandwidth.

## Can you get rid of about:blank?

About:blank isn't really something you "get rid of" or avoid. But if you're seeing it every time you open your browser, it could be that it's set to display about:blank upon launch.

If you don't want that to happen, simply go in and change your homepage to whatever you want it to be (following the same steps as above).

## Is about:blank malware or a virus?

As we've seen throughout this article, about:blank itself isn't anything malicious. But it could be a sign that your computer is blocking malware. So they can be related.

Some anti-virus and anti-malware software use about:blank when they detect a bad URL or site. So instead of directing you to that malicious site, the browser throws up that blank page to protect you.

The about:blank page can also appear after you've removed malware from your system. If, in the process of removal, something broke, the browser will display about:blank because it can't complete the action you asked it to perform.

In the end, unless you want to set about:blank as your homepage or think you need to investigate possible malware or viruses on your machine, you don't need to worry about about:blank.

