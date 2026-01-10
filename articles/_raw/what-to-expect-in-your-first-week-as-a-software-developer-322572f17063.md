---
title: What to expect in your first week as a Software Developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-01T21:21:05.000Z'
originalURL: https://freecodecamp.org/news/what-to-expect-in-your-first-week-as-a-software-developer-322572f17063
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HKru9urHK6ywE91ZZhPbig.jpeg
tags:
- name: jobs
  slug: jobs
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Harriet Ryder

  You know you enjoy coding, but what’s it like doing it for a job? What might you
  expect in your first week?

  I couldn’t imagine my first week in a new job. Do you start coding right away? What
  if they use a language/framework you have...'
---

By Harriet Ryder

You know you enjoy coding, but what’s it like doing it for a job? What might you expect in your first week?

I couldn’t imagine my first week in a new job. Do you start coding right away? What if they use a language/framework you haven’t learned? How do you get up to speed with the codebase, and know what the priorities are? Is it easy to slot into the team? Do you just… open up your editor and start coding? What if you get something horribly wrong and break everything?

I worked for 2 years at a coding bootcamp, and I heard similar questions from lots of students. They knew they liked coding, and loved what they were doing at the bootcamp on a daily basis - but they wanted to know what it feels like to go into a real job.

In this post, I’ll use examples of what I did during the first few days in my most recent role to try and give you an idea of what you might expect.

### Background

I am working as a full stack developer in a smallish company. There are four developers in the engineering team (including me) and a CTO. We also work closely with a Product Owner, who is one of the founders. I went in with a couple of years of coding experience.

All services are on AWS and we use NodeJS and Ruby.

### Day 1: Mostly Setup

I arrived at the office at 9am. A shiny new MacBook Pro was waiting for me on my desk, complete with adaptors and two screens. The dev team took me out for breakfast at a nearby cafe, and when we got back I sat down and started getting my machine set up.

Since I’ve set up countless dev environments before while working at a coding bootcamp, this was pretty straightforward and didn’t take me long. However, I had only set up a Ruby/Rails environment on my own laptop once, so that part took me a little longer.

I was provided with an A4 sheet listing the requirements, version numbers, and so on which I made sure to follow carefully. I was also given access to various sites like BitBucket, a password manager, AWS and Gitlab and set up my SSH keys on my new machine.

Before lunch, I went for a chat with the CTO and we talked in detail about the product, the architecture, and the goals and priorities the dev team have for the foreseeable future.

After lunch, I cloned down some of the services that make up the application and began to familiarise myself with the codebase. Luckily for me, I joined the team at a time when there were some new, fresh parts of the service under development which means I didn’t have **too** much code to get up to speed with.

For the last couple of hours of the day, I sat with one of the senior developers while he implemented a feature. We used it as an opportunity for him to guide me through that part of the app, explaining why things had been done in specific ways, the parts that had caused problems, and the aspects that might end up changing in the future.

### Day 2: Testing

I was given the task of testing a couple of functions in one of the repos for the app. Giving new hires tests to write is a great way of introducing them to a codebase and familiarising them with some of the logic of the application.

I spent a fair bit of time just reading the code, figuring out how it all worked together, and seeing if I could follow the flow of the logic. I was interested in the conventions the team had chosen, the way the code had been split up, and the stylistic choices. Writing the tests was not hard, but I’m always really cautious making my first mark on a codebase I haven’t worked on before!

I didn’t want my work to stick out, so I attempted to observe and absorb the code style that was currently being used. To some extent, having good practices like linting helps a lot, but there’s also just general architectural and stylistic choices that linting can’t help you with.

One slight challenge I had was getting used to the Git workflow that the team used. Every team has their own way of doing things: some teams merge, some teams rebase, some teams squash commits and others don’t, some follow popular workflows like [this one](http://nvie.com/posts/a-successful-git-branching-model/), and others just force push into master willy nilly. Plus there’s the conventions of the commit message and description to get right, the reviewing process, and so on.

All in all, there’s a lot of non-explicit “this is how we do things” stuff to pick up. After going through the process a couple of times, correcting my mistakes and asking questions, it’s now second nature.

All the time I was writing notes in a notebook and keeping code snippets in an application called [Bear](http://www.bear-writer.com/). There was so much to take in — how to do things, the preferred procedures for the team, things I hadn’t done before, and new languages and frameworks to learn.

I needed to be really active in noting down what I was learning. I made it a point at the end or beginning of every day to review my notes, add extra explanations to things I’d written in a hurry, and research stuff I didn’t fully understand. All of this also took up some time.

### Day 3: Spiking AWS

As part of the release we had in progress, we needed to decide how to deploy a service we were building. We were using AWS, but there was a choice between using a EC2 instance which would be the simplest choice, as it’s just a server in the cloud running your application, or something a bit fancier like Elastic Container Service. The benefit of ECS is that it would manage the scaling of multiple EC2 instances and therefore be a good option for the future. But it wasn’t completely essential for the time being.

Given this, I was given (volunteered for) the task of spiking out how easy it would be to deploy our service on ECS. Spiking just means trying something out to explore feasibility. If it was going to be hard, it wasn’t worth it, since it was a future optimisation we didn’t desperately need it right now.

This involved a lot of learning for me, as I hadn’t used Amazon’s ECS before, plus the app was a Rails app and I was much less familiar with the whole Ruby/Rails ecosystem. I had spent maybe a total of 30 hours learning Ruby before joining the company, since I knew it was part of their stack, but I’d barely touched Rails. Plus, the task involved a bit of work with Docker, which was also new to me.

My tech lead got me started off with what was basically a 1-hour intro to Docker which was hugely useful. From there, I spent most of the day creating a new Rails app and following various articles, docs, and examples to see if I could get the thing running on ECS. I almost got there, but getting the database integration to work proved a stumbling block. There was just so much new stuff.

I’m sure someone more familiar with either ECS or Rails wouldn’t have had so much trouble. I couldn’t come away saying that the process was objectively hard. It was hard **for me**, but that didn’t mean it was hard for everyone.

Not a hugely productive day in terms of usable code or output, but I felt like I learned a lot and from that perspective and it was great.

### Day 4: Pairing and mentoring

I arrived at the office at 8am, and while I was waiting for others to arrive I followed part of a Docker course I’d been watching on Pluralsight. I was still keen to finish off the spike from yesterday, but recognised that I needed more of a grounding in at least one of the new technologies that I was working with.

I spent about an hour on the course, before more people arrived at the office and we set about deciding who’d do what. Another new developer, who had started a little before me, had just got back from holiday. We decided we would pair together on a task. We were building a new feature in the Rails app. This was quite a simple task, but Rails was new for both of us so it was great to work through it together. When we needed something explained, we would simply ask one of the other devs, either in person or on Slack. We had some great discussions this way and I began getting the hang of how Rails works.

In the afternoon, I had a mentoring session with the tech lead which was generous since I’d already got a private Docker class just the day before! Mentoring is an opportunity to take questions, run through problems together, learn something together, or just pick someone’s brain. The knowledge transfer is very beneficial.

I had lots of odd questions about database stuff and Rails, but I regret not having one single goal for that first session. I guess I just wasn’t sure what to expect. In subsequent sessions, I’ve asked my mentor to show me how to do something specific like configure an NGINX server or configure an EC2 instance to have access to a database — things which he would already know, but would take me much longer to figure out on my own.

### Day 5: Meetings and merges

Many software teams will use combinations of stand up meetings (often daily), regular retrospectives (about working practices or technical issues), and planning sessions to organise their workflow at a high level, in combination with some sort of tracking tool where the work in progress and work left to do can be visualised.

Our team is no different, and we have the majority of our scheduled meetings on a Friday. Like many teams, the emphasis during our meetings is to reflect on how we’ve been working and what we’ve achieved, to collectively solve any problems or blocks, and to identify and plan upcoming work so we’ve always got something ahead of us ready to move on to.

We also go out to breakfast to bond, which is awesome!

All in all, most of the morning was spent on these activities. I had little to contribute as I was still getting my head around all the terminology and the structure of the product, and I was always about a sentence behind, trying to catch up with what had just been said. I remember during that first week just feeling like my brain was melting as I tried to hold all the various components of the architecture together in my mind (it gets better as time progresses, so don’t worry!).

In the afternoon, my pair and I were able to finish off what we’d been working on, solicit a code review, make amendments, and open a request to merge our work into the app. We didn’t deploy as it was a Friday afternoon but we did on the following Monday. ?

Thanks for reading, I hope this article gave you some idea of what your first week as a developer might look like.

I’d love to hear your comments and experiences!

