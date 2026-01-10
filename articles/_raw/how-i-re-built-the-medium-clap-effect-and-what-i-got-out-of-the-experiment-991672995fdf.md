---
title: How I (re)built the Medium clap effect — and what I got out of the experiment.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T10:22:58.000Z'
originalURL: https://freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2gzBT_k8M-SrIZ1maT7njQ.gif
tags:
- name: Design
  slug: design
- name: learning
  slug: learning
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Emmanuel Ohans

  Four years ago, I read a quote that would change my life forever.

  I don’t remember the surrounding circumstances, but the sun was blazing hot and
  I was on the results page of a Google search.

  A famous Pablo Picasso quote popped up, ...'
---

By Emmanuel Ohans

Four years ago, I read a quote that would change my life forever.

I don’t remember the surrounding circumstances, but the sun was blazing hot and I was on the results page of a Google search.

A famous Pablo Picasso quote popped up, and for the next few weeks I was completely lost in it.

> Good artists copy; great artists steal

> — Pablo Picasso

### What? Did he really mean that?

As multiple questions kept my mind spinning, I had to read more about who Pablo was.

Pablo Picasso was an artist considered one of the most influential and greatest of the 20th century. At this point, I knew he was no failure going around talking trash.

I went on about my life, but that quote never left me.

Years after, I had become an astute follower of the “steal” philosophy. It was so ingrained into my subconscious that I thought I would someday write a New York Times bestseller on the subject.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wukzTeTc2i2-mRahxcjGTw.png)
_Life happened. I never got to write the book :(_

I applied the rule to nearly everything I did.

For example, I spent hours re-writing several codepens (built by others) by hand, all in a bid to learn something by stealing. Earlier this year, I saw [Dan Abramov](https://www.freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf/undefined) talk about something similar.

I wasn’t crazy after all.

The steal rule appears to be a general rule for mastery.

In his book, _Peak: Secrets from the new science of expertise_, Anders Ericsson talks about the feedback loop and how essential it is to mastery. In fact, this was the same technique Benjamin Franklin used to write incredible books. He was arguably one of the best American writers of his time.

This mindset and learning method led me to attempt to recreate the Medium clap effect.

### The experiment

The Medium clap was designed and built by people with at least five times the smarts as I have. But this was not the first time I recreated other people’s stuff. The Medium clap was just one of many such projects.

I’ve always found the Medium clap to be so satisfying. Many times I’ve clapped after the 50 mark just to feel that satisfying animation.

Building the Medium clap was an interesting experiment. The goal wasn't to create an exact clone, just something that worked like it.

### Technology I used

For content, I used good ol’ HTML and some SVG. I got a clap icon from the Noun Project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9M0oeCEgOsovOMz2snw5iw.png)
_SVG Created by Luis Durazo from the [Noun Project](https://thenounproject.com/search/?q=clap&amp;i=28959" rel="noopener" target="_blank" title=")_

I opened up the clap icon in Illustrator and edited it to my heart’s content. I then optimized via [SVGOMG](https://jakearchibald.github.io/svgomg/).

I needed Javascript for Interactivity. So, I built the clap with vanillaJS and then forked it to rebuild via [ReactJS](https://codepen.io/ohansemmanuel/full/zEJpYy/).

For animations, I chose [LegoMushroom](https://www.freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf/undefined)’s mo.js. It seemed to be the best for recreating the Medium clap animations. [Mo.js](http://mojs.io) is a pretty interesting animation library with a declarative API. I find it to be very beginner friendly, too.

### How I started

I wasn’t particularly sure where to start. I had some experience with SVG, but didn't have a lot of experience with mo.js.

At this time there wasn’t any “working” Medium clap on [codepen](http://codepen.io). There was nothing to learn there.

So I stole again.

“There must be something online I can learn from,” I said to myself. After a couple failed searches I found something.

[Mary Lou](https://www.freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf/undefined)’s [Codrops](https://tympanus.net/codrops/) is one hell of a resource for practical frontend stuff. I searched and found some [animated icons](https://github.com/codrops/Animocons) there.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rCTs5mvGAYWofIKz1b4Kfg.gif)
_The codrops animated icons were inspired by this shot by [Daryl Grinn](https://dribbble.com/daryl" rel="noopener" target="_blank" title=")_

The icons were nothing like the Medium clap, but there was certainly something to learn there.

You know what I did, right?

I built the codrops animated icons from the ground up. I copied the entire codebase by hand.

This gave me a lot of perspective, and I knew how to go about the Medium clap afterwards.

### How do you learn really fast?

Other than building the codrops animated icons, I didn't have substantial experience with [mo.js](http://mojs.io)

That wasn’t a big deal. I had always been excited by the prospect of learning something new faster, and I had developed a system for learning stuff fast.

In 2012, Scott Young completed all 33 courses in [MIT’s fabled computer science curriculum](http://www.eecs.mit.edu/academics-admissions/undergraduate-programs/course-6-3-computer-science-and-engineering), from Linear Algebra to Theory of Computation, in less than one year. He quickly became my inspiration.

This MIT curriculum was supposed to be a four-year curriculum, but somehow he managed to systematically tame it in under 12 months.

I believe in ultra learning. It is such an important skill in today’s economy.

So, what was the plan?

First off, I needed coverage. Coverage around the mo.js terrain. Like Scott says, you can’t plan an attack if you don’t have a map of the terrain.

First, I skimmed through the official mo.js tutorials. I skipped some, to be honest. I saw a youtube [video](https://youtu.be/yRxWa8lXasI) where Sarah Drasner explained how the mo.js library worked. I watch the video at 2X speed. I also read Sarah’s book, [SVG Animations](https://www.amazon.com/SVG-Animations-Implementations-Responsive-Animation/dp/1491939702). There was a chapter dedicated to the mo.js library.

I read very fast.

All I needed at this point was coverage on how the library worked and what was possible with it.

After these, I moved on to putting my knowledge to work. It was time to build the [Medium](https://www.freecodecamp.org/news/how-i-re-built-the-medium-clap-effect-and-what-i-got-out-of-the-experiment-991672995fdf/undefined) clap.

After spending a lot of time on the animations, I ended up getting it right. Something that didn’t suck.

![Image](https://cdn-media-1.freecodecamp.org/images/1*whZ-_7SaDzmDXwfpkliMFw.jpeg)
_Example configurations for the animations powered by mo.js_

I got stuck at some points. I made mistakes, and even spent a few days tweaking stuff. But yeah, I got it to work.

### What’s the point?

I believe in continuously challenging myself. Pushing myself just beyond what I think I know or can do.

This was just another experiment in that regard.

### Was it a failed experiment?

I wouldn't say so.

On the 11th of October, the pen was picked, and went on to be viewed by over 2,000 people.

I gave a talk at the ReactJS Summit, Lagos, on [SVG and Microinteractions](http://bit.ly/2xVmb45). There, I talked about micro interactions in the context of ReactJS apps, and got to show how to build the Medium clap effect.

### Conclusion

I have come to find a new love for micro interactions, and I believe they are the little giants that make a great product.

In all, it was an interesting and fruitful experiment. I don’t regret it. Not at all.

Do I plan on recreating some more ambitious projects? Hell yeah!

But hey, that’s a talk for another day :)

Keep building, keep coding!

