---
title: So how do we fix Twitter? A user interface revamp would be a good place to
  start.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-09T06:57:52.000Z'
originalURL: https://freecodecamp.org/news/this-ui-revamp-could-make-twitter-successful-again-d4c551b353b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*O3YZrr_LO--eNZykWD17KQ.png
tags:
- name: Design
  slug: design
- name: social media
  slug: social-media
- name: 'tech '
  slug: tech
- name: Twitter
  slug: twitter
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Daryll Santos

  It’s no secret that Twitter has been struggling to grow its user base. To fix this,
  they’ve laid out a long-term strategy to turn around its business by focusing on
  five areas:


  Its core service

  Live-streaming video

  The site’s “creat...'
---

By Daryll Santos

It’s no secret that Twitter has been [struggling to grow its user base](https://phys.org/news/2016-07-twitter-struggling-rivals.html). To fix this, they’ve laid out a long-term strategy to turn around its business by [focusing on five areas](http://www.reuters.com/article/us-twitter-results-idUSKCN1062JW):

1. Its core service
2. Live-streaming video
3. The site’s “creators and influencers”
4. Safety
5. Developers

Two things that stuck out to me in that statement are 1) focus on its core service (tweeting) and 2) live-streaming video (Periscope).

Those stuck out to me because just recently, I convinced a friend to join Twitter. When he landed on the feed, his first questions were “how do I Tweet?” and “how do I go live?”

Seeing as how those are key features of Twitter, I’d think that those should be the most intuitive things to do, even for a new user.

### Objectives

1. **Make Tweeting intuitive:** Tweeting is the driving force behind Twitter; the staple that drives their product. So, right when a new user completes the registration process, the user should know, right away, how to Tweet.
2. **Make going Live more intuitive:** [Twitter spent $86.6M on Periscope](http://www.recode.net/2015/5/11/11562534/twitter-paid-over-86-million-for-periscope-and-niche) to provide their users the ability to live-video stream through their mobile app. It’s also a [huge market](https://medium.com/looklivecam/on-demand-livestreaming-960a492d69d1#.z9u58217s), and it’s no surprise that Facebook is attacking it so aggressively. With that in mind, why isn’t this functionality more accessible? For example, I remember a time when my friend was at a concert trying to live stream an artist walking out onto the stage. He missed the moment because he wasn’t able to go live quickly enough.
3. ***Bonus* Update the Twitter feed**: I’ve always felt that the Home Feed was a little too squished together. A few minor changes would benefit it tremendously. It’s also been some time since they’ve updated this, so a fresh face would be nice!

### User Personas

Of course, it’s always important to know your users. [37% of Twitter’s users are aged 18–29](http://sproutsocial.com/insights/new-social-media-demographics/#twitter) and that’s also their largest user base, meaning that Twitter’s users are largely the tech-savvy, social media addicted, live-video streaming millennials. Knowing this, it’s imperative to make important features of Twitter (Tweeting and Periscope) more accessible to them.

![Image](https://cdn-media-1.freecodecamp.org/images/vlzhq00QVvwI9IoRnuk0GIuSI272xDWC-eO2)

### User Research

To ensure I made the best design choices possible and validate my objectives, I ran a survey to pinpoint the thoughts of Twitter users. Specifically, I aimed to discover:

1. The ease-of-use level of tweeting for new users
2. How aware Twitter users are of the ability to go live (Periscope)
3. The ease-of-use level of live (Periscope)

#### 1. Ease of Use for New Users

I ran a survey and found that only 5/10 users (50%) found Tweeting easy to do at their first go-around. For their core service to only be easy for 5/10 people seems to be a bit of a concern because without it, there is no Twitter. I definitely think a UI improvement could help with this.

![Image](https://cdn-media-1.freecodecamp.org/images/hCxRjbIZ9uxFxR8ScJHpe3jDTvbsJG5q4k0n)

#### 2./3. Awareness of Periscope and Ease-of-Use Level

It amazed me to find that only 43% (10/23) of Twitter users I asked knew that they could live-video stream! Additionally, these weren’t just any random users. These were people that have been using Twitter for years and are in the 18–24 and 25–34 age group.

![Image](https://cdn-media-1.freecodecamp.org/images/Pwlj5dbmhWSZcjjoMISBxN1iDM3CrvnjT6Gf)

![Image](https://cdn-media-1.freecodecamp.org/images/BbO06HpvcQ1z8gGC25ugaHhrC8fL1yM1YmAp)
_“Peri — what?”_

### Technical Analysis

First, understanding Twitter’s current layout will inform us of how it tends to its users’ needs. I’ve laid out the UI and split it up into blocks, as each block has a purpose, and in each block, we’ll see what/how it can be improved. Let’s take a look:

![Image](https://cdn-media-1.freecodecamp.org/images/MjmdyUj71nFQ6h8uVPEfJvE-dujuaAQNiPLR)

* Block 1: This is basically Twitter’s bread and butter since this is where users go to Tweet. I believe it can be improved because the Tweet button is out of the thumb’s natural radius zone (see change 1 below).
* Block 2: This is where the Twitter feed is. There’s nothing wrong with it, but I believe a minor improvement can make it better.
* Block 3: This is where users go to navigate through the different Twitter views. There’s nothing wrong with it, but since users constantly have their eyes down here, a key addition would probably help them reach their long-term goals.

### Results

#### Change #1: Improve Core Service: Relocate and change the Tweet button

![Image](https://cdn-media-1.freecodecamp.org/images/gEW2dpWH1EBltowlm3dy25z-WhDlDbfj9d0h)
_The Thumb Zone_

By moving the Tweet button to the bottom-middle, adding a label, increasing its size, and giving it color, users will know exactly what that button is just by looking at it. Also, by giving it a background color, it acts as a call to action that essentially tells the user “Hey! Press me!”

Most importantly, it’s in an easier location for users to press due to being in a comfortable location for thumbs (see picture above).

![Image](https://cdn-media-1.freecodecamp.org/images/mxOyEv32QmKgMXwv9ZgGSx8nnT2DGegFfbaH)
_Now, Tweeting is “Natural” instead of “Ow”._

#### Change #2: Improve Live-Video Streaming by moving Periscope Live to the Home feed

In conjunction with Twitter focusing on live-streaming (Periscope), the idea for this change came when I saw my buddy miss that moment at a concert he wanted to record live, because it took him too much time to hit Periscope. By the time he had gone live, the intro he wanted to capture had already been missed. Yes, he could have activated it earlier. But sometimes life’s moments need to be caught quickly.

The current 3-step process to go live goes like this:

1. Hit the Tweet button
2. Wait for the Tweet view to slide up
3. Hit “Live”

For the sake of speed, it should be:

1. Hit “Live”

That’s it. Just one step.

To do this, I had to remove the Live button from the Tweet view and bring it to the Home view. By bringing it there, it’s accessible in just 1 step.

![Image](https://cdn-media-1.freecodecamp.org/images/Vut8yUGFO8S1De6WFxfmMrzrrOEZjwc1XDs-)
_Live is for catching life’s moments, so it should be in a place you can get to it fast._

#### Change #3: Update the feed

Twitter’s feed is pretty good, but I believe a few minor changes can improve it.

* I changed the Twitter icon to look less similar to the buttons near it (Messages & Live) because their weights looked too similar. By having drastically different weights, it’s easier for users to know that it’s not a button without having to press it.
* I added space in-between each tweet so they’re less cramped together. This helps people identify conversations on their feeds easier, since chains are spaced from the rest of the Tweets now.
* I changed the AVI frame from a rounded square to a circle.

![Image](https://cdn-media-1.freecodecamp.org/images/Gul3p5jAyISpM1nvj4oNxhCnJw9Q97r4Kj0Z)

### Conclusion

Twitter is one of my favorite apps and I use it daily, so working on this project was fun for me to work on. I also knew this would be a great way for me to hone my design capabilities, seeing as how Twitter is already a great mobile app.

I built an ? i[nteractive prototype here](https://invis.io/SWA9B1RX2) ? using Sketch and Invision.

If you’ve read this far, I appreciate you! Hopefully, I’ve written something that was helpful or interesting to you.

> “Design is not just what it looks like and feels like. Design is how it works.” — Steve Jobs

Thanks for reading and happy designing!

