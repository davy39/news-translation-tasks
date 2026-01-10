---
title: How to overcome your fears and contribute to open source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-26T00:31:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-over-your-fear-of-contributing-to-open-source-6160e4cdf0d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LhRYLVKVEtj7ujueU1yt8A.jpeg
tags:
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Eumir Gaspar

  Are you a new developer? Or maybe even just an old-timer who has been in a company
  for ten years, working on an in-house project, and now you’re thinking, “Hey, I’ve
  been in my box a long time. What’s new out there?” I have been like ...'
---

By Eumir Gaspar

Are you a new developer? Or maybe even just an old-timer who has been in a company for ten years, working on an in-house project, and now you’re thinking, “_Hey, I’ve been in my box a long time. What’s new out there?”_ I have been like that before, and I had my own fears to conquer during those times.

When I graduated, I had the general direction of my career in mind: web development, games, or both. I **loved** the Internet and I had the knowledge to go to town on it. At that point in time, naïve me felt invincible knowing HTML/CSS. I also knew some Flash and PHP, so I thought I was a very versatile developer (yes, we had our proud moments).

Long story short, I got into some web developer and game dev roles. At some point in time, I was introduced by my good friend [Topher](https://www.engineyard.com/blog/author/christopher-rigor) to the world of [Ruby](https://www.ruby-lang.org/en/).

I was new to everything it offered:

* Git (my form of version control with my Flash work was like FINAL-FINAL-V22.zip)
* Command line: sure, had some experience with PHP, but on a Windows machine, it wasn’t much
* Unix

Back then, I had no clue what open source was. I knew PHP was open source, and that it basically meant the source code was there for everyone to see. That was that.

### Enter Github

In my opinion, [Github](https://github.com/) set the precedent for the boom in open source. Ruby on rails was fairly new back then as well, and when Github was made using Rails, it was the start of my open source journey.

![Image](https://cdn-media-1.freecodecamp.org/images/drmY3I8RECXYLdPkN9ukFRybsvcKxc5zwMad)
_I joined Github almost 10 years ago! WOW!_

It wasn’t until a year and a half later [when I created my “first” open source project](https://github.com/corroded/ijgmaps). It was [actually just a fork of Bob Craven’s work](https://bobcravens.com/2010/06/06/a-google-maps-version-3-jquery-plugin/) in which I modified some parts for another project.

Another year later, I created [my first issue](https://github.com/justinfrench/formtastic/issues/491) and [pull request](https://github.com/mickeyren/jquery-notifications/pull/1). Yes, it took me a year! After this, though, I felt more confident and with encouragement from my boss, who was an open source advocate as well, I contributed more and more to open source.

### So how do I get over that fear?

First and foremost, ask yourself why you’re afraid of contributing. It’s the first step in overcoming a fear (at least for me!).

Here were my own fears in addition to the most common ones I have heard about (that have been to me by students, colleagues, and so on) which may or may not apply to you:

* What if my contribution is not accepted?
* What if I write crap code that nobody likes?
* Will people judge me for the code I write?
* I can’t understand any of their code! :(
* I don’t know how to code / I’m just a newbie.
* I don’t know where to start!

After listing these fears down, address them one by one or at least try to find solutions to how you can address them. As such, I can list some solutions to these and hopefully help some of you to get over that hump and start contributing.

### What if my contribution is not accepted?

To be honest, this is not that huge of a fear for me, but more of an inconvenience. There’s that little part of me that dies when my work is rejected (who doesn’t?), but that’s just the way it is. We just have to learn to accept that sometimes. A pull request may not be accepted because of code quality, duplication, and so on. **And it’s OK**. I can’t stress that enough.

In my early years of contributing, I had a few [rejections](https://github.com/fulcrum-agile/fulcrum/pull/87) and it was a bit disheartening. Take note though, [some actually don’t reject you outright](https://github.com/vwall/compass-twitter-bootstrap/pull/2) since with some projects, [maintainers are overwhelmed by pull requests](https://github.com/cucumber-attic/cucumber-tck) or [some issues are already solved but not yet released](https://github.com/twbs/bootstrap/pull/4802).

My advice is to just move along and look for other options. You can’t dwell on a pull request forever! Try to get something from it. In the rejection I had, I learned to do fewer commits paired with smaller pull requests, and not one epic feature in one go.

### What if I write code that nobody likes?

I don’t think anyone dislikes code, especially something that was supposed to help a project. Sure, there are some projects that will require a higher quality of code than others, but in the end, contributions are what powers them — so hopefully no one will call your code ?.

In most open source projects, people will comment and offer constructive advice on how to improve your contribution. Learn from them and follow their advice. Refactor. Most importantly, ask the maintainers how you can fix it and/or point you in the right direction. You’d be surprised how easily they will provide you with the tools that you need!

### Will people judge me for the code I write?

In my experience, most people don’t judge you for your code (at least the hundreds of developers I have encountered have not). Now, the thing to keep in mind is that whenever you write code you are not sure about, ask for someone else’s opinion, or ask a more senior developer to review it for you. If you don’t know anyone that fits the bill, then let the maintainers know in your pull request description that you probably have some not-so-good code and ask for their opinion.

I think it’s just best to be open on these kinds of things, and if they have the time, they will surely let you know and help you out. The best way to get a good response though is to not just ask “How do I make this better?” Not everyone has the time to help everyone else out, so it would save a lot of time for you (and for the maintainer!), if you first research how to make your code better and **then** ask for help. More like, “Hi, I’m still new here, but here’s what I have done, and some links to sources on why I did it this way. I think it is still not good enough, and was wondering if you have any opinions or if you could point me in the right direction.” That sort of thing.

### I don’t understand any of their code!

This still bugs me sometimes. This is mostly true on many huge open source projects like Rails, React, and others like that. Usually, the only way to understand is to encounter a problem / bug and reproduce it on your end. All I can really say is that you don’t have to understand **everything**, but at least know how things work as a bare minimum.

I once had a student while I was mentoring who asked me about this. He wanted to really push himself and I suggested that one challenge (that I myself haven’t finished!) is to create a pull request to Rails or whatever project he was fond of. A week later, he was beaming when he mentioned he got his first pull request merged. It was a pull request to the Japanese version of the Rails guide. I was a very proud mentor that day.

He didn’t understand Rails fully yet, but he REALLY wanted to contribute to it. So instead of looking at Rails itself, he helped out in another way by fixing translations so non-English speakers / readers could understand it better.

This brings me to another point which actually addresses another fear…

### I don’t know how to code / I am just a newbie

We all have to start somewhere. All the experts, maintainers, and famous developers you know all started as a newbie. The key thing here is that they managed to improve themselves and didn’t let being a new developer block them from doing something great.

Now, I know a LOT of people who don’t even have a Computer Science background, who know a lot more than I do (and I have a CS degree!). Not knowing how to code should not be a source of fear, since you can contribute without coding.

Bear in mind, **contributing does not only mean making pull requests**! It can be participating in a discussion about a feature, pointing out errors, or even filing bugs (be [sure](http://edgeguides.rubyonrails.org/contributing_to_ruby_on_rails.html) to [follow](https://github.com/elixir-lang/elixir#contributing) [their](https://github.com/elixir-lang/elixir#contributing) [contributing](https://github.com/kelseyhightower/nocode#contributing) [procedures](https://github.com/facebook/react#contributing)!)

Most of the time, a project will need translators or proof readers. If you fancy doing those tasks, go look for a project you like and support them. I am an avid fan of Elixir, and while I haven’t written production Elixir code, [I volunteered to help maintain the style guide](https://github.com/christopheradams/elixir_style_guide). Of course, I asked the maintainer first, but it was also my way of training myself to Elixir syntax and project management of sorts. I didn’t have to be an Elixir expert, I mostly managed the issues and double checked the submitted pull requests.

### Great! Where can I start?!

Again, Github is a good place to start. If you have a project you support, try to look there first. Otherwise, if you feel like you can conquer anything, look at the [trending repositories in Github](https://github.com/explore?trending=repositories#trending) or even [Explore Gitlab](https://gitlab.com/explore).

Now go forth and spread the open source love!

_Update: I have also made an article about making your first pull request (and getting it merged) as a supplement to this. [Check it out here](https://medium.com/@corrodedlotus/how-to-get-your-first-pull-request-merged-2826d7295ee9)._

