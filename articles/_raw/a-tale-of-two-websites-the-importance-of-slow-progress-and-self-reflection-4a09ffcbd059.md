---
title: A Tale of Two Websites
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:54:24.000Z'
originalURL: https://freecodecamp.org/news/a-tale-of-two-websites-the-importance-of-slow-progress-and-self-reflection-4a09ffcbd059
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j1DjBAA7lRTBVaE17yRQGQ.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sun-Li Beatteay

  The importance of slow progress and self-reflection


  _Photo by [Unsplash](https://unsplash.com/photos/2bFB0Er064Q?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" title="">Tanya Nev...'
---

By Sun-Li Beatteay

#### The importance of slow progress and self-reflection

![Image](https://cdn-media-1.freecodecamp.org/images/1*j1DjBAA7lRTBVaE17yRQGQ.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/2bFB0Er064Q?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Tanya Nevidoma</a> on <a href="https://unsplash.com/search/photos/two?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

“Hey, since you’re learning to code, do you think you could make me a website?”

I’m sure we’ve all heard this question before. It comes with the territory of being a web developer. The first time I ever heard it was in March of 2016. My wife was a graphic designer looking to break into the UI/UX field. She wanted to display her skills in an online portfolio.

I’d only been learning web development for 3 months at that point (I’d started as a New Year’s Resolution). I’d finished a couple of HTML, CSS and JavaScript courses and was anxious to dig my teeth into a juicy project.

“Yeah I can do that for you. Shouldn’t take too long.”

It took three months.

I realized pretty quickly that I’d bitten off too much. However, while I was naïve, I was also determined. I put everything I had into that website. When I wasn’t working at my job, I was either coding or searching Stack Overflow.

Mostly searching Stack Overflow, a lot of it.

Despite the stress and strain that project caused me, I couldn’t have felt more proud when I saw it live for the first time on my browser.

_That was my work. I had done it._

Using her new website, my wife was able to find a role as a UX designer in New York City. We both quit our jobs and made the move from Seattle. This marked the beginning of my head-first dive into programming.

### Two Years Later

“Hey, do you think you could update my website?”

It was June 2018 and quite a few things had changed. In those two short years, my wife had gone from UX designer, to product designer, to design lead of a startup. She wanted a new update to reflect that growth.

“Yeah, I can do that.”

I tried to sound as confident as possible, but I was hesitant. I remembered how long it took to build her website the first time. I wasn’t sure I had the endurance and mental stamina for a second bout. It had exhausted me.

My self-confidence was further shaken when I started digging through the old code. I hadn’t looked at it in two years. It hadn’t aged well. While the UI still worked and looked good, [the front-end was a mess](https://github.com/sunny-b/irisWebsite). It seemed as if it was being held together by duct-tape.

In terms of “code smell”, it reeked like a dumpster fire.

While my wife only wanted an update, navigating through that codebase was laborious. It was going to be easier to start from scratch. I wasn’t thrilled at the idea of starting anew. But while my wife had grown a lot in the past couple years, I had too. I took it as an opportunity to reflect on how much I had learned.

### Starting Fresh

The first day I started building my wife’s new website, I knew it wasn’t going to take 3 months. I was able to do more in that first day than I previously had in a week. In the end, it only took about a weeks worth of time to finish the update.

You can see it live here: [irissprague.co](http://irissprague.co/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*8PRyq64Cm6RAhhoLLkRm_A.png)
_[irissprague.co](http://irissprague.co" rel="noopener" target="_blank" title=")_

While I was impressed with how quickly I was able to build it, I wasn’t exactly sure why it had been so much faster. Sure, I had two more years under my belt, but what exactly had I learned in those two years?

#### Leveraging Tools

The first thing I noticed was my ability to leverage tools. You see, two years earlier, I knew very little about open source tools. My wife’s first website was built using raw HTML, CSS, JavaScript, and a touch of PHP. While that isn’t bad in itself, I had no concept of view templates.

I wrote each HTML file from scratch. To maintain consistency, I copied over any repeated elements. Unfortunately, that meant that changing one page meant changing several.

On my second attempt, I avoided all those hours of copying and debugging by using [HAML templates](https://github.com/sunny-b/updated-iris-portfolio/tree/master/app/views/layouts) and [Flexbox](https://github.com/sunny-b/updated-iris-portfolio/blob/master/app/assets/stylesheets/application.css.scss.erb#L105).

![Image](https://cdn-media-1.freecodecamp.org/images/0*4WNpnLyPMvNmPgAo.gif)
_Thanks Flexbox_

#### Automating the Build Process

Another reason the first website took so long to build was because I had no concept of a build process. For the entire 3 months I was building my wife’s first portfolio site, I was doing it all locally on my machine.

Whenever I made a large change, I would have to pester my wife to come scrutinize the alterations on my laptop. If that wasn’t bad enough, when it came time to push my changes to a production server, I had no idea where to start.

I had been so focused on getting the website working that I hadn’t even considered how I would get it onto the internet. I had never heard of DigitalOcean, Docker, or Heroku.

The only hosting service I knew at the time was Godaddy. Godaddy uses cPanel to upload files onto the server itself. Unfortunately, cPanel only allowed for files to be uploaded one at a time.

It took hours. And whenever I needed to change any of the assets, I would have to re-upload those edited files manually.

With those mistakes burned into my memory, I invested in improving my build process. I automated my CI/CD workflow using Docker Compose. With one `docker-compose up -d` command, I could deploy the entire site to production.

I even created a small bash script to batch my Git and Docker commands together.

Any changes I made could be live in less than a minute. cPanel was a thing of the past.

I also used a DigitalOcean Droplet so that my wife could see any changes I made. She could view the edits on her own machine by visiting the Droplet’s IP address. No more local-only development.

My wife and I also improved our design-to-development pipeline. In 2016, the designs were mainly done through Photoshop and oral cues.

“Can you change this? Can you add that?”

Neither of us enjoyed it.

This time around, my wife and I used [Invision](https://www.invisionapp.com/) to collaborate. I could see her design changes in real time and implement them in minutes.

Power coupling at its finest.

#### Improved Problem Solving

This won’t come as a surprise, but in these past 2 years, I’ve become a better and faster programmer. But the most important improvement was my problem solving abilities.

I didn’t need to look up how to create grids in CSS or build an image carousel in JavaScript. I had the tools and foundation I needed to solve those issues myself. I could spend more time in flow and less time googling every issue I came across.

I also knew how to do more with less. My first site had hundreds of lines of JavaScript to do the simplest of animations. [The new site only has 70 lines](https://github.com/sunny-b/updated-iris-portfolio/blob/master/app/assets/javascripts/carousel.js). CSS transitions and keyframes handle the rest.

Prioritizing CSS over JavaScript improves each page’s performance by reducing DOM painting. Though, that wasn’t the only optimization I made.

#### Optimizations

Two years ago I had no idea how to create a performant website and I didn’t care. I just wanted the damn thing to work. Now that I understood the fundamentals and thought at a higher level of abstraction, I could focus on solving the larger problems. Namely, performance and user experience.

By compiling the static files, serving them through a DigitalOcean CDN, and caching them in the browser, the updated site is able to load at lightening speed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cCFxOR2msa4DecxHNXrUpQ.png)
_Performance rating from [Pingdom](https://tools.pingdom.com" rel="noopener" target="_blank" title=")_

In 2016, that previous sentence would’ve looked like gibberish to me. Oh, how times have changed.

#### Take time to appreciate how much you’ve learned

So why am I saying all this? To toot my own horn? Maybe a little.

The real reason is, I want to emphasize the importance of self-reflection. I was hesitant to update my wife’s site, because I hadn’t realized how much I had grown. It’s hard to see the amount you progress on a day-to-day basis.

Knowledge accumulates inch-by-inch. But by looking back over a long period of time, those inches become leaps and bounds. In Japanese culture, this idea of small daily improvements is known as “kaizen”.

For me, it’s important to remember where I was at the beginning of my career. Visualizing my evolution keeps me motivated when I hit plateaus. Ebbs and flows are inevitable. Committing to progress one inch at a time is how I advance towards my goals.

So as a tribute to mastery and remembering my roots, my wife’s first site will live on as a subdomain of my personal website. You can see it for yourself at [kaizen.sunli.co](http://kaizen.sunli.co/).

I want to give a special shout out to [Launch School](https://medium.com/launch-school) for teaching me the importance of the slow path to mastery. It’s a goal I will continue to pursue.

And another shoutout to my wife [Iris Sprague](https://www.freecodecamp.org/news/a-tale-of-two-websites-the-importance-of-slow-progress-and-self-reflection-4a09ffcbd059/undefined) for just being plain amazing.

So whether you’ve been programming for 10 months, 10 years, or more, take time to reflect on how much you’ve learned. Use it as fuel for when times feel slow. Investing in the slow path to mastery has compounded results. Gradual at first, but with enough time, you’ll be soaring like a rocket.

If this article has resonated with you, please leave some claps ? and let me know how you’ve grown in your own career. I would love to hear about it!

As always, happy coding!

