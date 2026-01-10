---
title: My First Hacktoberfest — Experiences of Contributing to Open Source as a First
  Timer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T23:26:06.000Z'
originalURL: https://freecodecamp.org/news/my-first-hacktoberfest-experiences-of-contributing-to-open-source-as-a-first-timer-b538f7c129dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RAY-ZG2pcG1IOHrNuj__-A.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sibylle Sehl

  Contributing to Open Source and projects can seem like a daunting process. Your
  favorite search engine will return a ton of results on guides and repositories to
  get started. But many times, your search does not yield the result you w...'
---

By Sibylle Sehl

Contributing to Open Source and projects can seem like a daunting process. Your favorite search engine will return a ton of results on guides and repositories to get started. But many times, your search does not yield the result you want, you still do not know how to contribute to Open Source even after reading multiple blog posts. The impeding reputation of certain projects and a harsh undertone does not help either and might complicate matters even further.

I have been there myself. I trawled through pages to find great Open Source repositories to contribute to, only to notice that I did not know how to start.

Frustrated and a little disappointed, I started focusing on other projects instead.

But it all changed when I saw a fellow employee’s Hacktoberfest sticker on their laptop. I was intrigued — was this a remnant of yet another Hackathon?

Hacktoberfest turned out to be very different.

### So what is a Hacktoberfest exactly?

Hint: it doesn’t have to do with either beer, or hacking or the Oktoberfest (which actually takes place in September, duh!).

[Hacktoberfest](https://hacktoberfest.digitalocean.com/) is a month-long celebration of contributing to Open Source, running from 1st October to 31st October. It was initiated by DigitalOcean in collaboration with GitHub. During the month of October you are encouraged to contribute and make pull requests to your favourite repositories on GitHub. If you manage to make four in total, you are eligible to receive a swanky T-Shirt like this!

![Image](https://cdn-media-1.freecodecamp.org/images/tvLihMaZR91TmZNQd32VhntPuvtTg3HY0PYw)
_This beauty of a T-Shirt is what you receive after completing Hacktoberfest (Credit: @mahsinger on Twitter)_

### Labels, labels, labels

Hacktoberfest proved to be a great month to get into Open Source. GitHub was filled with issues labelled _Hacktoberfest_ that needed your help. There was enough projects to choose from — ranging from documentation to Python to RUST. During this time, I learned how to search GitHub for issues by _labels_ and how to find good issues to contribute to.

For people like me, who did not have any experience, labels such as _first-timers-only_, _easy_ or _good-first-issue_ proved to be my friend. There are also some good websites which aim to make the process of finding those issues easier. For example, [up-for-grabs.net](http://up-for-grabs.net/) or [code-triage](https://www.codetriage.com/) — there’s probably many more.

Go and sign up to a few of these or check out their issues!

### Learning how to contribute

While trying to make my first contributions, I realised that my biggest unknown was not how to add links to markdown or style a page. But how to make a _good_ pull request using git and the command line.

I found Kent C. Dodds’ [free guide on egghead.io](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github) helpful and took notes of the command line commands I executed while following along.

The instructions could be summarized to something as simple as this:

```
//First you need to find a repository you want to contribute to and fork it! 
```

```
// Then you have to clone the forked repo git clone git@github.com:yourusername/contributing-repo.git
```

```
// Change your directory to the new repo you cloned cd contributing-repo
```

```
// Set the upstream repository to the original repository (not the one you just cloned) git remote add upstream git@github.com:the-owners-username/contributing-repo.git
```

```
// Update any changes git fetch upstream
```

```
// Set our master branch to same as upstream branchgit branch --set-upstream-to=upstream/master master
```

```
// Create your own new branch for your pull requestgit checkout -b pr/my-new-cool-contribution
```

```
// Make any changes in your favourite text editor and save
```

```
//check status (should show the modified files)git status
```

```
// look at changes and reassess workgit diff
```

```
// add any changes to your staging area ( . for all files)git add 
```

```
// Commit all changes and add a message for the maintainer of the repogit commit -m "I added this cool text to your guide repository"
```

```
// Push to source repo and create pull requestgit push origin pr/my-new-cool-contribution
```

This really helped me to understand the purpose of a pull-request and to understand the process of making a contribution. [This blog post](https://medium.com/@mscccc/jr-developers-1-pull-requests-you-39a11c3bdd94) also helped me to understand that being descriptive is your best weapon — as that way you can get support and indicate if a Pull Request is still in progress. Not long after, I made another practice contribution but to receive a T-Shirt I needed to up my game and find another two issues.

### A match made in heaven — contributing to freeCodeCamp guides

I opened Medium one day and saw that Quincy Larson had provided a [complete guide on how people could easily contribute to the freeCodeCamp guides repository](https://medium.freecodecamp.org/i-just-got-my-free-hacktoberfest-shirt-heres-a-quick-way-you-can-get-yours-fa78d6e24307). A source of shared knowledge across development, product, design, and data science. Contributing to this repository was not only highly encouraged but also super easy. You could make the contributions in your browser.

Finding a topic was not hard as the guides repository covered anything from Accessibility to HTML to Game Development.

What intrigued me the most was how easy freeCodeCamp made the process to enable newcomers like me make meaningful contribution. Sharing knowledge with others.

You still learned about making pull request, having your contribution merged and adhering to standards and contributing guidelines. The process was slightly less intimidating . It was perfect for a beginner. In fact, it was that streamlined that freeCodeCamp managed to make a gif about it that sums the process up:

![Image](https://cdn-media-1.freecodecamp.org/images/S6Pfccsc7EvGQR8n4xv720Z4leIRBKKeGhs2)
_Credit: freeCodeCamp — Contributing to the freeCodeCamp guides repository_

After some deliberation, I decided to make a small contribution on different Linux distributions. And write a completely new section on Game Development to complete my four pull requests. I made a game over the summer as part of my dissertation project. Writing about Game Development and tools seemed a good way to share my newly acquired knowledge with others.

In their [Contributing.md guidelines](https://github.com/freeCodeCamp/guides/blob/master/CONTRIBUTING.md), freeCodeCamp had given a lot of detail and a way of making sure that your writing was concise. I did all my research, backed it up with sources and fired it through the [Hemingway app](http://www.hemingwayapp.com/) . Active voice and short sentences for the win!

I made my pull request and was over the moon when it got merged. The encouraging feedback was also a great plus from the freeCodeCamp community.

![Image](https://cdn-media-1.freecodecamp.org/images/-HBwPGWrDEYvOti1MsfsXcmgk7kxwFhH2oMt)
_Pull Request for the Game Development section I wrote for freeCodeCamp guides_

### What can we take away from this?

I would advise you to free yourself from the assumption, that you need to contribute perfect and well-rounded code the first time. Your first contribution does not have to be ground-breaking (or even be code to be precise).

Project maintainers know that this might be your first Open Source contribution if they have labelled the issue as _first-timers-only_ or similar. Your contribution can be anything like correcting a spelling mistake, adding some hyperlinks or a small learning project. Start small to become familiar with the process.

Many project maintainers that label their issues as friendly for beginners are also happy to answer your questions and provide support. So, don’t be shy to ask for clarification, if you do not understand something.

When the Hacktoberfest T-Shirt finally arrived in mid December having been shipped all the way from America, I felt like Christmas had come early. Holding it in my hands made me realise that I had helped to create and extend something that mattered . A feeling I believe many people contributing to Open Source on a regular basis will experience. Wearing it always reminds me to share my knowledge and this year I will also try and make the leap to contribute more code, after all I am not a first-timer anymore!

