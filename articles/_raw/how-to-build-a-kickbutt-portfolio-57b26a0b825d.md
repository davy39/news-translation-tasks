---
title: How to build a kickbutt portfolio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-07T19:46:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-kickbutt-portfolio-57b26a0b825d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*bMH1CrkWPH0FE8EC.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: portfolio
  slug: portfolio
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ali Spittel

  Over the years, I’ve rebuilt my website a few times and have made changes to the
  way my portfolio is displayed. In this article, I’ll share my personal tips and
  provide an in-depth look on what worked and what didn’t to help you build ...'
---

By Ali Spittel

Over the years, I’ve rebuilt my website a few times and have made changes to the way my portfolio is displayed. In this article, I’ll share my personal tips and provide an in-depth look on what worked and what didn’t to help you build an awesome portfolio. I’ll also provide you a few links to other people’s portfolios that I love.

According to GitHub, I’ve had a personal site with my portfolio since September 2016. Looking at the Google Analytics for my site, I got less than 300 views on the two iterations of my portfolio from September 2016 through October 2017. I was pretty demotivated, but I didn’t give up. ?

In October 2017, I did a complete rewrite of [my site](https://www.alispit.tel/), and the results were pretty dramatic. I got 1,861 views in the first month, and I’ve averaged around thousand hits a month since then.

Of course, correlation is not causation, but I do think the redesign definitely had a positive impact. It’s not exactly Facebook, but for a portfolio site that doesn’t provide the viewer with anything but information about me, I think these numbers are pretty good. ?

![Image](https://cdn-media-1.freecodecamp.org/images/wKZto1kSw0ljF-0lsFO7ubnB55yvqoEegeoi)
_Personal Site Visitors_

### What Didn’t Work

Before I get to my current portfolio that I really love, I want to talk about my first two sites.

#### My First Portfolio

The first portfolio was a Jekyll site which used SASS and Pug. I deployed it [here](http://average-cause.surge.sh/) for nostalgia’s sake. Check out the projects, they’re all from college, and most are in C++!

![Image](https://cdn-media-1.freecodecamp.org/images/HTH-VtC1Bw0svffIjWYUrvRGYTwqnlmnwZx1)
_My first iteration - Learning CSS_

This setup was unnecessarily complex for the actual content of the website. I used Jekyll, Materialize (CSS framework), SASS, and Pug for such a simple page. I think the Gulp setup was longer than the actual CSS needed. ?

I was just transitioning to writing frontend code at any capacity, so this was really a learning opportunity for me to use SASS and Gulp. I had no need for Jekyll either. I only had a few projects listed and only one page.

Also, there were a bunch of 404’s showing up in the console for resources that were not found. If I was a developer looking at the site, I would definitely be critical of that.

![Image](https://cdn-media-1.freecodecamp.org/images/3pXkx9ShqDtKFzJk6ozW1RkPvMwXsoE0ogP4)

The screenshots for my projects were not great. They were all either of code or cropped in an un-optimal way.

![Image](https://cdn-media-1.freecodecamp.org/images/Bq-o7U-TmpATdUVhwCKWIqlPPvFSPAPlF8wV)

The fonts were also too small, so it was difficult to read the text. My social icons were not exactly the most prominent, which meant that they probably didn’t have too high of an engagement rate.

There were some things that I did well, though. I really like the highlighted words in the bio. It draws the user to look at those keywords, even if they don’t read the whole bio. I also appreciate that the site was responsive, so users could view the site on different sized screens. Currently, around a third of my traffic comes from mobile sources, so its important to remember those users.

#### My Second Portfolio

![Image](https://cdn-media-1.freecodecamp.org/images/fjugwXZv3v2qPe-JCSK3osT51pgIMlFHGPSY)
_My second iteration - Polka Dots :-)_

The second iteration was an HTML and CSS site with moving polka dots in the background. You can check it out [here](http://third-match.surge.sh/). I will admit that I still have a soft spot for this portfolio.

I really like the moving bubbles, and how they changed with user interaction. I also enjoy the minimalism of the site. I think the quick bio on the homepage was effective and expressed my interests well.

Again, the fonts are somewhat small, and having to navigate to a new HTML page to view any information about me is probably not the best user experience. Also, having my talks and my code projects on the same page makes it look unbalanced and cluttered.

Overall, though, you can see a lot of the themes from this portfolio in my current one.

### What Worked

In October of last year, I started from scratch and built a [portfolio](https://www.alispit.tel/) that was a little bit out of the box. **Your portfolio is one of the only sites that you will build that is a complete creative expression of yourself with no constraints.**

So, I went all in — built interactivity, animations, you name it, the portfolio had it all.

![Image](https://cdn-media-1.freecodecamp.org/images/TyKjfp49ULx9JsaMkN69Zi4-4p7Ok57zs0xM)
_My final iteration - The Works_

If you click anywhere on the homepage, a random shape appears. If you hover over the letters, they animate. If you hover over my picture on the bio page, it spins.

![Image](https://cdn-media-1.freecodecamp.org/images/FcmtJ0IMVq1Fi2vyqp0VzoGqlN8ACNRCjAng)

I used Vue for this portfolio, so it seamlessly transitions from page to page. I also increased the font sizes, so readers could gather information more quickly and easily. My contact page offers large buttons to follow me elsewhere on the internet.

The original version of this design was built in HTML, CSS, and a very few lines of JavaScript. As far as my technology needs go, this was totally fine. I wanted to move to Vue for my own maintainability needs. The reconfigured setup makes adding new projects a lot easier. I also like the smooth routing that Vue Router offers, instead of navigating to an actual new page.

This design grabs people’s attention, and they stay on the site in order to interact with it. Also, people reach out to me about my site a lot, which, if I was looking for a job, would be awesome!

### What I could still do better

Here is a list of few things I could still work on improving

* As far as effectiveness for converting people to my other social media, I could have links to my other social media on each page rather than just the contact page.
* I also probably need to cull through my projects and choose a few to feature, rather than have 26 personal projects listed.
* I also don’t have screenshots of my projects. This is intentional, but I could probably get more traffic to them if I put a screenshot of the project on them. I didn’t like the different color palettes that adding in screenshots of my program would create.

I don’t have many projects that I find super impressive. For the most part, they are pretty small, and I had created them to learn something. I could further optimize my site, but for now, I really like where it is at.

### My tips for building a kickbutt portfolio

* Make a portfolio that is a true expression of yourself. Programming is, in a lot of ways, a creative field, so use your creativity!
* Make the site interactive so people want to stay on your site, and they remember it.
* Buy a domain name. I moved from aspittel.github.io to alispit.tel. I really like the play on my name, and you can get a lot of domains for pretty cheap. I use NameCheap, and it’s totally worth the $8.00 a year for the domain.
* Make sure you don’t have console errors. Alot of technical employers look for this, so make sure that your site is bug-free!
* Don’t use a technology just for the sake of it. If you have a super minimalistic personal website, don’t use a heavy-duty framework or library just for the sake of using it. **Having a simple site that is super slow is a bad user experience.**
* Make sure your website is responsive and works on mobile phones. I would also encourage you to make it work for users that use a split-screen setup.
* I would steer away from using a template found online. To me, it’s pretty apparent when these are used. I understand using them for people who aren’t web developers, but if you are a web developer, show off your skills!
* Use the portfolio to market yourself. If you want to show off specific skills to employers, make sure those skills are featured on your site. I want people to visit [my blog](https://zen-of-programming.com/), so I have it featured on my home page. I also want to do more speaking, so I have a whole page dedicated to my talks. I no longer want to write C++ code professionally, so I took those projects off of my site.
* Make sure your links aren’t broken. I have totally been guilty of this at certain points, but it doesn’t look great, and then your viewers can’t see that destination!
* Keep your portfolio up to date. I’m guilty of not doing this that often too, but I try at least every few months to add new projects and talks to my site.
* Use a critical eye, and be intentional about the design. I use Sketch to draft my sites before moving to code.
* Think about page speed. I run [lighthouse](https://developers.google.com/web/tools/lighthouse/) testing on all of my sites to make sure they are performant.

### A few of my favorite portfolios

* [Timo Becker](https://timobecker.com/) - You connect the dots and create different illustrations — just play with it, it’s awesome.
* [Ben Halpern](http://benhalpern.com/) - this site is so memorable and fun.
* [Julia Khusainova](http://julia.im/) - This site is really minimalistic, but gets the point across.
* [Nik Papic](http://nik.org/) - another simple but pretty one.
* [Robby Leonardi](http://www.rleonardi.com/interactive-resume/) - a game resume!
* [Dinesh Pandiyan](https://flexdinesh.github.io/) - the color change is a really cool feature, and I like the minimalist design.

### Your site

I love looking at other people’s portfolios and offering advice on them. I comment on portfolio feedback threads all the time when I see them. If you have one you’re looking for feedback on, [Tweet](https://twitter.com/aspittel) me a link to your site, and I will look over it and send some feedback! Or, if you just have an awesome one, send it to me too! I would love to add it to my list of favorites.

Also, if you liked this article, [subscribe](https://tinyletter.com/ali_writes_code) to my weekly newsletter that contains my favorite links from the week!

_Originally published at [zen-of-programming.com](https://zen-of-programming.com/kickass-portfolio)._

