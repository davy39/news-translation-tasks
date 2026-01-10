---
title: How I shipped my first SaaS side-project while working full-time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-19T18:33:43.000Z'
originalURL: https://freecodecamp.org/news/how-i-shipped-my-first-saas-side-project-while-working-full-time-5ad33cf89121
coverImage: https://cdn-media-1.freecodecamp.org/images/0*VzFah4Lrwc4VuYsv.JPG
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tigran Hakobyan

  This is my personal story of how I shipped my very first SaaS side-project while
  working full-time at Buffer. The goal of this article is to inspire you. If you’re
  someone like me who has a full-time job and wants to build a profit...'
---

By Tigran Hakobyan

This is my personal story of how I shipped [my very first SaaS side-project](http://www.cronhub.io) while working full-time at Buffer. The goal of this article is to inspire you. If you’re someone like me who has a full-time job and wants to build a profitable side-business as a source of income, then this story may resonate with you.

With this article, I want to show how I didn’t “hustle” or overwork and was still able to ship a real SaaS product.

I’m a web developer and I’m very lucky that, apart from playing soccer in my free time, I also enjoy coding and building web projects for fun. Most recently, I’ve created [Booknshelf](http://booknshelf.com/) which helps many people organize their books online. While working full-time has a big impact on my engineering growth, some of the developer skills I’ve acquired were from working on my personal projects.

It was only last year when I started to think about having a different source of income apart from my full-time job. The idea of being dependent on a single paycheck is a bit scary. I knew I had the skills and passion to figure something out.

I decided I wanted to start a business, probably an online business considering the skills I have. The other trigger of those thoughts was that I wanted to experience and learn what it means to build a business. I had never run any business in my life, so I saw this as a great learning opportunity, a path on which I could learn skills that I don’t currently have. The worst thing that could happen would be that if I failed, I’d still end up with experience and tons of learnings.

### Idea

As you might have guessed, the first thing that I, as a developer, did was to start thinking about ideas. Ideas were never a problem for me, but figuring out which ideas were a good fit always was. This time, I decided to try a different approach and really think through the idea before I jumped on it. There were some criteria I wanted to run each idea through.

* I wanted to solve a real problem, probably something I personally was facing
* It should be for the market I know well
* It should not be a new idea (it’s not going to change the world)
* It could become a business

The golden rule of any idea is that it has to solve a problem that people face. In the past, I’d added so many ideas to my notes — so it was a matter of visiting the pool of ideas I’d saved.

![Image](https://cdn-media-1.freecodecamp.org/images/QcVMCLohkisTur3kYm5cQA4jBWJ-GUhhvuFz)

I knew from the beginning that I’d probably be more successful if I built something for developers, because I know the market pretty well and most of my close friends and online followers are tech-based. I could use my network and audience to validate my idea and get a solid feedback before I commited to anything.

This really filtered down all my ideas into a list of 2–3 things I could work on. One of the ideas was something I kept coming back to over and over again. It was something I’ve faced both at Buffer and during the work on my previous side-projects: a simple way to monitor scheduled cron jobs.

Since one of the areas I own at work is the analytics data infrastructure, I have run a dozen cron jobs in the background to collect the daily analytics data for our customers. It has to be up to date. The [Datadog](https://www.datadoghq.com/) monitoring service that we use is really great, but it’s primarily designed to monitor continuous services or servers. I wanted a simple dashboard where I could see the list of all my cron jobs, their statuses, and logs. Every day get a report of all run jobs so I know everything is on track.

After picking this idea, I wanted to see if there were any existing solutions on the market. If there were, that’s a good sign that there was a demand for certain tools.

In fact, there were a couple on the market with different paid plans. I didn’t necessarily want to build something completely new, because if I did it would have been so much harder for me to define and validate the market. All the existing solutions had paid plans, so I knew people would pay for it. The next goal was to validate if my thinking was right by building and launching the initial MVP.

### MVP

I spent 2 months building the initial version of Cronhub (yes, I gave it a name). Something viable that I could send to a handful of my friends and Twitter followers to try. For the MVP I wanted something very simple but also valuable enough that people would pay for it. I know you may think that two months is a long time to build an MVP, but I didn’t take the traditional “hustle” approach. Instead, I:

* Worked only 1–2 hours every day
* Slept 8 hours every day
* Watched Netflix whenever I wanted to
* Fully rested on the weekends
* Used the tech stack I felt most comfortable with

Since I have a full-time job, I worked on Cronhub usually from 7 to 8:30 pm. I could also work in early mornings, but I spend most of my mornings at the gym. There were some days when I felt mentally very exhausted after work and I took it easy, but most of the time I stuck to my routine.

I knew if I wanted to finish this project I had to keep the momentum and commit every day even if it was a small change (could be a single line commit). Consistency has always been super useful for me to stay on track and ship. I used Trello to break down my project tasks into small milestones.

![Image](https://cdn-media-1.freecodecamp.org/images/5XEJNRsYL6sFibO6DJF1oJt-7AEYt4b5pvf-)

I tried to make each task very small so I could start and finish in a single day. Keeping tasks small helped me to ship faster and see my daily progress. When you see progress it motivates you a lot and keeps you going. I think it’s a mind trick. Working on big tasks slows you down, and eventually you give up because you get bored and you want to jump on something else.

I never worked overnight. I went to bed around 10:30 every day and woke up at 7. Having proper sleep is my number one priority. It defines the mental energy I have during the day and I can’t sacrifice it. Besides sleeping well, I decided to spend most of my weekends doing something completely different like playing soccer, watching movies, or hanging with friends and family. Even though I love coding, I know it’s easy to burn yourself out. Weekends helped me to refresh my brain.

I think as a developer you always want to use the hottest and coolest technologies. And it’s okay. I want that, too. However, my goal was different and I wanted to build and ship Cronhub as fast as I could with the technologies I already knew. I stayed focused on my goal and used Laravel and Vuejs. Cronhub is a single page application using Laravel for the backend.

### Closed Beta Launch

On Feb 20, I finished the bare-minimum of Cronhub and was ready to invite the first pool of early adopters to try it out. After my tweet, around 20–25 people reached out to me on Twitter asking for an invitation. The feedback I got from them was super valuable.

![Image](https://cdn-media-1.freecodecamp.org/images/VLVa11ILNBYcGbe75C2rxfjabicFmgEAY9ea)

There were a couple reported bugs and some great feature suggestions that I’ve added to my feedback document. Keeping track of user feedback is an important step, because it helps to identify the obvious patterns you can refer to when you make product decisions.

Overall, the first impression and feedback were encouraging. Now I needed to continue improving the product and make it ready for the first public launch. I planned the first public launch to be within a month.

### Public Launch

After three months, I’m launching my first SaaS side-project to the public. Yay!

Of course I’m nervous, and don’t know if this is going to work out or not. However, I know this brings me one step closer to my goal. The goal to make Cronhub into a profitable online business where I can learn and experience all the hidden secrets of running a business. After all, what’s the worst that could happen? I’d learn so much!

I know maybe I’m too much focused on thinking about profitability, but after building a couple side-projects for free in the past I knew it was time for me to take my time a little bit more seriously. Time is the most valuable asset I have and I want to spend it consciously. Building a paid product is way more motivating and it pushes you forward. Also, maintaining side-projects for free is expensive — I know it from my experience.

### Lessons Learned

The past three months have been great for reflection as well as evaluating what worked well and what didn’t. Every time I build a new project, it’s a new learning experience. Each project is unique and requires a different thinking process around the product. As a product engineer, I want to develop my product mindset and this helps.

Overall, I’ve learned many lessons that really helped me to start and launch an idea. I want to share the most important ones with you.

* **Solve a problem you personally face**. This is so key, because essentially you build the product for yourself, always keeping you in mind. This makes it a lot easier to make good product decisions. You know what questions you should ask and chances are higher that you ask the right questions.
* **Keep your tasks small**. When you break down your project into pieces, try to make them smaller. A good way to measure the size of the task is to ask yourself “Can I do this task in a day?” If the answer is “No” then it’s probably a big task and you can break it down further.
* **Sleep well and rest.** I can’t stress how important proper sleep is. You don’t have to work overnight. Focus on incremental progress and small daily commitments. If you don’t take care of yourself you will get tired soon and eventually give up.
* **Choose a market you know well.** I’m a developer and I know this market well. I know what it takes to be a developer and how developer teams collaborate. This gives me a sense of things that will and won’t work out in this market. Of course, I can still be wrong, but chances are a lot smaller.
* **Talk about your project.** This is a challenging one for me and I’m still adapting to this. I don’t really like to talk about myself. I like listening more. It’s not easy for me to talk about the project I’m building, because I’m a bit shy and don’t want to make an impression that I constantly talk about myself. However, I know I have to get the word out and market my project. That’s how others will discover it in the beginning. This article is an example of that.

### To conclude

Thanks so much for reading. I hope you enjoyed this story and learned at least one thing from it. I would love to hear from you, so please feel free to comment with your questions. You can reach out to me on [Twitter](https://twitter.com/@tiggreen) or [email me](mailto:tigran@cronhub.io).

If you’re a developer or part of a team that uses cron jobs, you can try [Cronhub](http://www.cronhub.io/) for free. Use coupon “indiehackers” to get 20% discount if you upgrade to “Developer” plan.

[Cronhub is on PH today](https://www.producthunt.com/posts/cronhub) if you want to support me :)

Keeping shipping — Tigran

_Originally published at [www.indiehackers.com](https://www.indiehackers.com/@tigran/how-i-shipped-my-first-saas-side-project-while-working-full-time-42862e847b)._

