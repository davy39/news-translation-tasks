---
title: The Pain of Waiting — Navigating the 7 Levels of Progress Indicator Hell
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-26T23:37:38.000Z'
originalURL: https://freecodecamp.org/news/the-pain-of-waiting-navigating-the-7-levels-of-progress-indicator-hell-decd3e019495
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5klWhpvdsBoo163ZB3VKpA.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: user experience
  slug: user-experience
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Mike Zetlow

  How much hell are you willing to put your users through?

  Of course the answer you’d like to give is “None!” But if you’re developing web
  applications, you’re going to make your users wait for results at some point.


  “ While speedy resp...'
---

By Mike Zetlow

How much hell are you willing to put your users through?

Of course the answer you’d like to give is “None!” But if you’re developing web applications, you’re going to make your users wait for results at some point.

> “ While speedy response times are best, there are simply times when even a server upgrade won’t allow you to comply with the guidelines for system speed. In these cases, you simply must reassure the user that the computer isn’t out for lunch but is working faithfully on their request. “ — [Progress Indicators Make a Slow System Less Insufferable](https://www.nngroup.com/articles/progress-indicators/)

Waiting is a pain point. No one’s favorite part of a roller coaster ride is the wait leading up to it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q5f96SlK_akITn_cXLDODg.jpeg)
_Totally looks like fun._

If waiting is a given, we should do everything we can to lessen that pain for the sake of our users. Disney has experimented with “[interactive waiting lines](https://www.youtube.com/watch?v=zuJlaVqe69I)” for their rides. While it’s about as fun as it sounds, at least it’s something.

In web development, we do something almost as fun: progress indicators. (Also called: progress bars, throbbers, loading bars, loading circles, loading icons, spinning pinwheels, or wait cursors.)

Here are the 7 Levels of Progress Indicator Hell from least painful to most painful.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nzvPNWlJloWU0LmbfXGGLg.png)

### The First Level of Progress Indicator Hell

#### Accurate Progress Display

This is a progress indicator that displays the accurate status of your application. It is difficult to do well and requires a lot of extra code (besides doing what the user asked the application to do). It’s great for users — but still belongs in Hell because waiting is a pain point no matter how accurate the wait time is.

The Accurate Progress Display is tough to pull off. Developers have been struggling with the problem for [decades](https://developers.slashdot.org/story/13/02/13/0026234/ask-slashdot-why-is-it-so-hard-to-make-an-accurate-progress-bar). If you’re the UX person pitching it, your team might ask if you can achieve a similar effect without as much dev effort.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qh5F7pw_HG1WaNkc4XpPeQ.png)

### The Second Level of Progress Indicator Hell

#### Semi-Accurate Progress Display

Many applications can approximate the wait time for users. The progress indicator can touch on different stages of a request and let users know. It’s not great because the time spent in each stage can differ wildly, leading to a “jumpy” progress bar.

For example, the call could take 20% of the time, the query 70% of the time, the sort 2% of the time, and the return 8% of the time. The user spends most of their time staring at a bar that is 20% full and then suddenly it jumps a bit and is done.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qdvpTCRuyvZce81cKv2NtQ.png)
_Credit: [https://xkcd.com/612/](https://xkcd.com/612/" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*sSQO33S-CfvxNPYoVX6Y6Q.png)

### The Third Level of Progress Indicator Hell

#### Throbber With Perception Tricks

A [throbber](https://en.wikipedia.org/wiki/Throbber) is a simple spinning or loading indicator that animates infinitely. At this level, we add perception tricks that make the user feel as if the loading is happening faster than it is.

> “It is argued that subjective time is not only the most readily manipulated, but also the most important. After all, our perception is our reality. We do not have to make faster computers to make computers feel faster. “- [Chris Harrison](http://www.chrisharrison.net/index.php/Research/ProgressBars2)

You can use perception tricks on Accurate and Semi-Accurate Progress Displays too. But they are most needed at the Third Level of Progress Indicator Hell and below, where forward progress is not measured and the wait can be most frustrating.

Here’s three of my favorite:

#### Perception Trick #1: Visual Augmentation

Not all progress bar designs are created equal. Some appear to fill faster than others. [Chris Harrison](http://www.chrisharrison.net/index.php/Research/ProgressBars2) has researched this, pitting various designs head-to-head against each other:

UX designers must balance this perception trick with the application / brand design.

#### Perception Trick #2: Textual Status Updates

Provide some text to the user (true or fake) about the status of the application.

> “Many times, if users are informed, they may be more patient. It can be helpful to add additional clarity by including text that tells the user what is happening or explains why the user is waiting.” — [Smashing Magazine](https://www.smashingmagazine.com/2016/12/best-practices-for-animated-progress-indicators/)

Adobe does a good job of this. Check out “Reading brushes…” below. (Adobe cycles through dozens of these statuses depending on how long it takes to load on the user’s machine.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*qxpCiaoDXGmhj2zVtvceDQ.png)

#### Perception Trick #3: Humor

Studies have shown humor’s effectiveness in alleviating anxiety. Savvy businesses, like Southwest Airlines, often use [humor](https://www.youtube.com/watch?v=07LFBydGjaM) during times of potential anxiety:

Waiting on a response from an application definitely raises anxiety levels in users, and humor can be a great tool to alleviate that. (This is best in consumer-facing applications, as it may not be acceptable in some enterprise applications.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CKvZYp5NB9jdIq_p2tuaVg.png)

### The Fourth Level of Progress Indicator Hell

#### The Never-Ending Progress Bar

To users, it appears that a progress bar is moving somewhat quickly, then it slows down and down and down, until finally they can’t tell if it’s moving at all.

This is a pretty mean trick to pull on users, though developers may have had nothing but good intentions. The devs coded a progress indicator that is essentially a throbber but looks like a bar filling up. It slows down as the request takes longer, crawling along the asymptote at an infinitesimal non-zero pace until the request is complete (if the request completes!), and at that point the meter shoots up to full.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WGbU97z9GLS7h_D0Zac61A.png)

To developers this looks like a working solution that is mathematically elegant. Unfortunately, users hate it.

> “Changes in speed will be noticed and will impact user satisfaction: if the progress moves quickly only to hang on the last percentage remaining, the user will become frustrated and the benefits of showing progress will be negated.”— [Progress Indicators Make a Slow System Less Insufferable](https://www.nngroup.com/articles/progress-indicators/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yc24yknEsxUil2RTxb1-BA.png)

### The Fifth Level of Progress Indicator Hell

#### Throbber

You see this all over software applications.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k6UgQB2PF3WLdkWPo7VXGA.gif)

![Image](https://cdn-media-1.freecodecamp.org/images/1*BJ7hHX9V4Ql2E6BxolFPbA.gif)

These are just animations that loop. Throbbers tell users the application is working on a request, but make them wait too long and they’ll abandon it. Throbbers are best used with short requests. If used with perception tricks, they can move up two levels of Progress Indicator Hell. Else, they remain here.

> “Showing an animated graphic on loop offers feedback that the system is working, but it doesn’t give any information about how long the user will have to wait… And if a spinner is rotating indefinitely, users cannot be sure if the system is still working or if it’s stopped, so they may decide to abandon the task entirely. “— [Progress Indicators Make a Slow System Less Insufferable](https://www.nngroup.com/articles/progress-indicators/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*VANUtVFRIsT9-psIeuwZzg.png)

### The Sixth Level of Progress Indicator Hell

#### Static Text

Or:

![Image](https://cdn-media-1.freecodecamp.org/images/1*bPkBdXQYkCcl-pmbsITuMQ.jpeg)

You typically see this on government websites or applications where consumers have little choice in the market. (My health insurance portal recently dropped this one on me.)

Intellectually, there is little difference between this and a infinitely-looped animation. But static text just feels so **_frozen_**.

Users are more likely to feel your app is stuck or broken with this type of progress indicator.

The [Nielsen Norman Group](https://www.nngroup.com/articles/progress-indicators/) says it best: “Static progress indicators: Don’t use them.”

![Image](https://cdn-media-1.freecodecamp.org/images/1*TJ_yLCo5-m9axRYtrL5-kg.png)

### The Seventh Level of Progress Indicator Hell

#### Nothing

No progress indicator whatsoever.

Just the still husk of your application’s frozen interface working hard in the background while the user sits there bewildered, frustrated, praying for the end to come.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5klWhpvdsBoo163ZB3VKpA.jpeg)

### Case Study: Connections Progress Indicator

With [Connections](https://chsiconnections.com/), a web-based insurance management application, we sometimes left users in the Seventh Level of Progress Indicator Hell. It was my goal to get us to at least the Third Level.

We implemented a YouTube-inspired progress bar in our header to display the progress of the user’s database request.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w0w6CucmVdVpCH4_9z_6mw.gif)

It’s basically a throbber, but we used a few perception tricks to ease the anxiety of waiting for our users:

1. **Visual augmentation that matches our brand design** — The striping occurs right to left while waiting and then the bar fills left to right quickly when loaded. The animations also occur at a faster rate than framework defaults suggest (Bootstrap, I’m looking at you) so [it feels faster](https://codepen.io/149203/pen/bWzwrb).
2. **Textual Status Updates** — We display a couple dozen text statuses (“Connecting to database,” “Acquiring connection,” etc.). They’re displayed in random 2 to 4-second intervals to feel real.
3. **Humor** — If the query takes longer than around 12 seconds (painful, but sometimes necessary), our textual status updates get funnier and weirder. We hope queries never take that long, but if they do, we try to reduce the anxiety with humor.

### Waiting Is a Pain

It’s a pain point of every software application. Hopefully I’ve shown that your application can rise from the depths with a little UX and design work. Don’t let your users wallow in the pits of Progress Indicator Hell. The uppermost level of an Accurate Progress Display might not be doable in your application, but with a little creativity, you can rise up and keep the waiting pain low.

