---
title: How to use GitHub badges to stop feeling like a noob
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-30T14:30:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-badges-to-stop-feeling-like-a-noob-d4e6600d37d2
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cab8d740569d1a4ca9262.jpg
tags:
- name: Shields
  slug: shields
- name: 100DaysOfCode
  slug: 100daysofcode
- name: badge
  slug: badge
- name: GitHub
  slug: github
- name: Imposter syndrome
  slug: imposter-syndrome
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Cam Barts

  Impostor Syndrome is real, and it plagues new developers. We get all the way through
  a tutorial, bootcamp, or even a degree, yet we still shy away from sharing our code.
  We fear negative feedback on our code’s quality. No one suffers mor...'
---

By Cam Barts

Impostor Syndrome is real, and it plagues new developers. We get all the way through a tutorial, bootcamp, or even a degree, yet we still shy away from sharing our code. We fear negative feedback on our code’s quality. No one suffers more from this than self-taught developers. Because we don’t have any “real” or “official” experience or training, we consider our code to be sub-par.

I was there a few months ago. I was working through [Harry Percival’s _Test-Driven Development With Python_](http://www.obeythetestinggoat.com/)_. E_ven though I was following right along with the tutorial, I was self-conscious about sharing my code. Even though my app was working as expected, I didn’t want to share my progress. I didn’t want someone to call me out on some obvious mistake to which I was oblivious. I wanted other people to enjoy my product, but I didn’t want them to see how poor of a developer I was.

After taking a break from [my own project](https://github.com/cam-barts/ObeyTheTestingGoat), I started looking at some other projects on GitHub. I found a few that had a little image on their README pages.

![Image](https://cdn-media-1.freecodecamp.org/images/pPzFRYVv5jJvht3U-2f8KgGIEoF0yqdxNrAD)

Now, being the noob that I was, I thought this was simply an image that Linus Torvalds handed you on a flash drive when you graduated from “Real Developer” school. Never once did it cross my mind to click on it. I thought it was a static image hosted somewhere in the repository. Later on, I stumbled upon a project that displayed that the build was failing.

![Image](https://cdn-media-1.freecodecamp.org/images/LSWK5plwMRtm14FC4QTmVhBKRF4wxeCj591G)

Why would someone take the time to add an image that says their build isn’t passing? Why go through the effort to take down the other image, put up this one? An image that says your project is broken and display it for the world to see? Out of sheer curiosity, I pulled up the raw format for the README. I saw this code:

```
[![Build Status](https://travis-ci.com/username/projectname.svg?branch=master)](https://travis-ci.com/username/projectname)
```

I was savvy enough with markdown to recognize that this was a clickable link. So I clicked the button and it took me to Travis-CI. All at once it made sense to me. This button was not updated by the project developer, Travis-CI updated it. **It’s a dynamic button.**

### My First Badge

So, once I found out about the build badge from Travis-CI, I had to have it for my project. After all, my whole project was about writing and using tests. So why not have something that ran them automatically?

So I [set up](https://docs.travis-ci.com/user/getting-started) Travis-CI to run my unit tests when I pushed changes to GitHub. Right at the top of the page where Travis-CI runs them, there is the badge. I clicked it and got the markdown. I added it to my README. I navigated to the project page on GitHub and VOILA! There was my first badge. I was hooked!

### The Hunt

![Image](https://cdn-media-1.freecodecamp.org/images/mJJxEV72ft2VNl-DYegNLQ5IyvfxICsSxYtg)

I enjoyed that the badge was a clear sign of the current status of my project. I wanted to learn more, so I went on the hunt for other badges. Another common badge I found was code coverage. The coverage report could be sent by Travis-CI to a tool called [CodeCov.](http://codecov.io/) You could get a badge indicating the coverage of your tests, which correlates to how well your app is tested.

![Image](https://cdn-media-1.freecodecamp.org/images/nXweRmbRr3BHhKQA0ChyI2WHrmiky-FBFDA-)

I also found License badges, and it only made sense to have a license badge if I had a license. So I [chose a license](https://choosealicense.com/) and added it to the repo. Getting the badge for that took a quick Google Search, and I found [this gist](https://gist.github.com/lukas-h/2a5d00690736b4c3a7ba) with all the common license badges.

![Image](https://cdn-media-1.freecodecamp.org/images/HoisHZJSio0u2t9dCdOkD8LP6AnWJCpr0JRk)

Coming from a security background in the military, I know that most vulnerabilities come from out-of-date software. As a new developer, I know this also goes for software that your software depends on. I heard about PyUp through [Michael Kennedy](https://medium.com/u/8f2ec0cf186b)’s _Talk Python to Me_ podcast. When I navigated to [the site](http://pyup.io/), I saw the words I’d begun to love seeing, “Free For Open Source”. Being on the hunt for new badges, I was in luck. Sure enough, they provide a badge, so of course, I add it to the README.

![Image](https://cdn-media-1.freecodecamp.org/images/9AZzZesmquR0zMx0JtUNAH80jdZ6QeSaiKLQ)

Finally, I discovered that you could have a badge for style. I’d messed around with [Black](https://github.com/ambv/black) before, and I found an example of the style badge and I knew I had to have it. For my own integrity’s sake, I wanted to ensure that my code was always compliant with Black’s style. I found out about [pre-commit](https://pre-commit.com/), which I could use to format my code before even committing it. After diving down the pre-commit rabbit hole (which also runs my code against [bandit](https://github.com/PyCQA/bandit) for security and sorts my imports and requirements), I felt confident adding the Black badge to my README.

### The End Result

The first result of hunting badges is that **I have a better quality project**. I added a license to my project, ensured my dependencies stayed up to date, and kept my project style compliant because I wanted the badges.

More notably, **I am more confident in my project.** I can speak about it knowing that there aren’t any gaping holes in it. I know I’m a lot less likely to receive feedback on my irresponsibility in regards to security or my lack of style compliance.

To put it simply, I feel better about my code because I have those GitHub badges.

