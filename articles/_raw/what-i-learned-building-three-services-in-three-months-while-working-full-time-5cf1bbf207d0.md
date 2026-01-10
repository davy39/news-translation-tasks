---
title: What I learned building three services in three months while working full-time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T17:23:02.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-building-three-services-in-three-months-while-working-full-time-5cf1bbf207d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gxHw9bxhEY-ezPeMC26kOQ.jpeg
tags:
- name: csv
  slug: csv
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: side project
  slug: side-project
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By taira

  To give you a bit of a context, I’ll start off with a little bit about me. I’m a
  self-taught developer currently working in Japan. I’m not special in any way, I
  don’t have any Internet celebrity friends, but I do love coding and have a posit...'
---

By taira

To give you a bit of a context, I’ll start off with a little bit about me. I’m a self-taught developer currently working in Japan. I’m not special in any way, I don’t have any Internet celebrity friends, but I do love coding and have a positive can-do attitude.

At the end of last year, I decided to launch an experimental project, to try to create one service per month in 2018 in my spare time. I wanted to see if I, an Indie-hacker-wanna-be, could work something out. And here’s my story so far.

I’ll break my discussion of each service into these sections:

* How the idea came about
* What the service is
* Tech stack
* How much $ I spent
* Lessons learned

### January: scratch my own itch.

#### **How the idea came about**

The first thing that came to my mind was to build something that I’d use heavily. In the worst case scenario, if my service attracted no one, it would still help me.

I started to look into my day-to-day flow. I realized that I spent quite a lot of time every day going to a variety of websites. So wouldn’t it be nice to have a web service to keep eyes on those sites for me, and send me updates via email? This would help me focus on the important things.

#### **What the service is**

![Image](https://cdn-media-1.freecodecamp.org/images/1*tNX15eL8kX2r5Pz_8L1C7w.png)
_KMPPP_

[Keep Me PPPosted](https://kmppp.com) is what I ended up building. To make the service even more user-friendly, I built a [Chrome extension](https://chrome.google.com/webstore/detail/keep-me-ppposted/fnfioeoaippeenifnfhpblddioiaaeji?utm_source=medium) as well, which allowed the user to subscribe to updates for any website right on the spot. You can check out the detailed user stories and design decisions on the [About](https://kmppp.com/about?perspective=dev) page, and I’m in the progress of opening sourcing this project, here’s the Github [repo](https://github.com/slashbit/spider-less) :)

#### **Tech stack**

I went with what I’m most comfortable with: front-end Vue.js and back-end AWS Lambda Serverless combo. I have been working with these in my current company on a daily basis for the last year and a half. Serverless fits my design very well, considering most parts of my service follow the event-sourcing pattern.

#### **How much I spent**

$22 in total: $7 for the domain, $10 for the Sendgrid subscription (100,000 emails per month, I could use it for my other services as well), and a $5 one-time fee for publishing the extension on the Chrome web store. Everything else was covered by the AWS free tier plan.

#### **Lessons learned**

It was definitely a valuable learning experience, since it was my very first full-scale web service. I posted it on Indie hackers and got a couple of users. But more importantly, I got the chance to talk directly with my users, working as a developer in the company.

In my job, I never get to talk with my end users to get instant feedback and have full control over the product that I build. That alone was worth the time and effort I put into it.

### February: leverage my resources.

#### **How the idea came about**

January was pretty tense, so I decided to take it easy. I thought about what else I could offer, besides my half box of chicken wings in my fridge. Something that others might need.

I’m in Japan, and working here might be something developers would be interested in. On top of that, I often get recruiters sending me job opportunities. Connecting developers and recruiters might be something I could work on.

#### **What the service is**

Instead of jumping right into coding, I created a mailing list using MailChimp. I started to share my experience in developer communities whenever I got the chance. It worked, and my mailing list grew to 500+ subscribers within a month.

In the meantime, whenever a recruiter reached out to me, I would casually mention my mailing list, and ask if I could share that with my subscribers.

#### **How much I spent**

$0. The outgoing mails are covered by the same Sendgrid account, and the backend cron job which was built with AWS Lambda was again covered by my AWS free tier plan.

#### **Lesson learned**

It seems that the less time I spent on coding, and the more time on promoting my service, the more potential users I’d get. Two weeks after I started, I got an email from one of my subscribers thanking me for what I did.

He hadn’t gotten a job using the service yet, he just wanted to thank me for sharing that information. That email just warmed my heart, knowing that what I’m doing actually helps others. That’s just the best feeling ever!

### March: get ideas from others.

#### **How the idea came about**

At this point, I’d kinda run out of ideas. That’s when I started to talk with my non-developer friends. I tried to understand what their day to day life is like, and if there were pain points they have that I could help with.

As part of his job, one of my friends receives CSV files from clients, and then imports those files into an internal system. Often times, the files he receives does not match the requirements, are missing columns, or contain incompatible data types — and so on.

He often has to go back and ask his client to redo and re-send the files. He has tried using Excel to automate the process, but failed because most of the files were really big (300+ MB with 1M+ rows). That sure sounded like something that I could help with.

#### **What the service is**

![Image](https://cdn-media-1.freecodecamp.org/images/1*vlk_6w7yVafO3dkFjFTDyA.png)

I created [CSV Lint](https://csvlint.com), a CSV file validation service for businesses, that allows a user to create a schema easily for validating CSV files once the schema is created. It can be shared with others (who could use it without having an account). This means that once my friend created the schema, he could ask his clients to use it to validate their files before sending them to him.

#### **Tech stack**

Instead of AWS, I went with Google Cloud Platform, Firebase for hosting and database, and Google Cloud Functions to handle the backend logic. Once again, their free tier covered everything.

#### **How much I spent**

$17 in total. I spent $7 for the domain — and it is a pretty awesome domain, I have to say, patting myself on the back. And another $10 on Udemy for a how to make demo video using a Keynote course. It was money well spent, another new skill learned. ?

#### **Lessons learned**

Ideas that I come up with lead to nothing 9 out of 10 times. Talking with others, especially people outside my normal circle, often helps me get new ideas. However, the sad part is I don’t really have a lot of friends that I can talk to — looks like I’ll need to work on that as well. ?

### Wrapping up

So, that’s my journey so far. None of my projects have succeeded big time, and I’m currently making $0 out of them. But each one of those services is helping people one way or another, and that puts a big smile on my face every day as I go to sleep. Also, they cost me close to nothing, there’s still some chicken wings left in my fridge. All good, all good.

