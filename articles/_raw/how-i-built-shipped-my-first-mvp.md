---
title: How I Built and Shipped My First MVP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T13:15:00.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-shipped-my-first-mvp
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-11-at-8.05.29-PM.png
tags:
- name: JavaScript
  slug: javascript
- name: lessons learned
  slug: lessons-learned
- name: mvp
  slug: mvp
seo_title: null
seo_desc: "By JavaScript Joe\nOn June 29th, I shared the MVP of mentored.dev on Twitter–my\
  \ first \"real\" project that was bigger than anything I'd built before and something\
  \ I was excited for other people to use. \nhttps://twitter.com/jsjoeio/status/11449945802002..."
---

By JavaScript Joe

On June 29th, I shared the MVP of [mentored.dev](https://mentored.dev) on Twitter–my first "real" project that was bigger than anything I'd built before and something I was excited for other people to use. 

%[https://twitter.com/jsjoeio/status/1144994580200210432?s=20]

After sharing this, I received some bits of positive feedback, including a shout-out in the [npm weekly newsletter](https://t.co/7sCziRMC9f?amp=1). 

I thought I'd share the story behind the whole process.

## Origin of the Idea

I can't remember when I first had the idea but a while back when I was introduced to [TwilioQuest](https://www.twilio.com/quest), I thought to myself, 

> Wouldn't it be cool to build a "gamified" learning platform that taught you how to code?

Like many other people, I have these ideas at random times throughout my life. I keep a list of these ideas in a [Trello](https://trello.com/en-US) board called "IDEAS". Looking here, I can see I notated this on January 21st, 2019. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/trello-card1.gif)
_Trello board with original idea from Jan. 21st_

I knew a few things:

* I wanted it to be interactive
* I wanted it to feel like a game
* I wanted it to have quick exercises

---

## Where to Start?

Around that same time, I was wrapping up a freelance project (porting a Jekyll theme to a Gatsby site) so I didn't feel like I was ready to start it just yet. Then, I had a conversation with [@signalnerve](https://twitter.com/signalnerve) on Twitter that sparked my motivation:

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-09-at-6.20.11-PM.png)
_Screenshot of Twitter conversation that motivated me to start._

> Build a small app–a real MVP–validate your idea and then decide if you should keep building. 

So I thought, "What the heck, why not start it?"

---

## March 2019 

I used a Gatsby/TypeScript starter to kickstart the first and pushed my [first commit](https://github.com/jsjoeio/mentored.dev/commit/0e38821f30d1f6f1bca804315fe24ccd5d5baf05). Originally, I named the repo "Life of Code" because that's what came to mind but later I renamed it after buying the mentored.dev domain. 

#### Initial Wireframes

After creating the repo, I sketched up some elementary wireframes in [Figma](https://figma.com)

![Image](https://www.freecodecamp.org/news/content/images/2019/07/figma.gif)
_Initial Wireframes in Figma_

Once I had all this, I felt over the initial "where-do-I-begin-paralysis" and knew I needed to keep the momentum going. 

#### Taking Input

One of the first things I tried was asking for user input and showing that in a message. This would be useful for the dialog between the narrator and the user. 

%[https://twitter.com/jsjoeio/status/1103860530605780998?s=20]

### Basic Dialog Working

Even though it didn't look pretty, the logic for the dialog was working! This felt like a good milestone because most of the hard stuff was done. 

%[https://twitter.com/jsjoeio/status/1106779197614088192?s=20]

### Narrator Character Talking

I struggled a lot figuring out the best way to get the narrator talking but after finding `[react-keyframes](https://github.com/zeit/react-keyframes)`, I was able to figure out a solution. This was huge because previously I hadn't done much with animation.

%[https://twitter.com/jsjoeio/status/1107812366891180032?s=20]

### Getting Feedback on Dialog

As stated earlier, I think it's important to get input from others. I don't know if Twitter is the best place to do it but fortunately for me, the people who responded to my request for feedback were kind.

%[https://twitter.com/jsjoeio/status/1108190126876680193?s=20]

### Migrating to TypeScript

I used a Gatsby-TypeScript starter for this project because I had been meaning to learn TS. However, up until this point, I wasn't actually using TS. The files just had .ts or .tsx endings.

Before the 30th, I had mentioned wanting to learn TS and [@TejasKumar_](https://twitter.com/TejasKumar_) offered to teach me by migrating the mentored.dev codebase over to TS on a Google Hangouts livestream. This was one of the coolest moments of this project. And I learned a ton. 

%[https://twitter.com/jsjoeio/status/1112088320182370304?s=20]

---

## April 2019 

### Adding a "Profile Card" Component

Next up after finishing the dialog part of the project, I decided to focus on the Dashboard - or the page after you logged in. I created a simple "Profile Card" that will eventually show your experience, any code-cash you have, etc.

%[https://twitter.com/jsjoeio/status/1113644342172774400?s=20]

### Designing the Dashboard

In hindsight, I may have gotten ahead of myself here because I designed way more than I could implement in the MVP but at least it gave me an idea for the future. I first added it as hard-coded components but later commented out to maintain a healthy UX.

%[https://twitter.com/jsjoeio/status/1114009915545141249?s=20]

### Designing the Campus Map

This took way longer than I thought. I wanted it to feel like a university campus but drew heavily from [Pallet Town](https://bulbapedia.bulbagarden.net/wiki/Pallet_Town) in Pokemon. The completed version has more but at least I had something I could add to the Dashboard. I designed all of this in Figma and exported it as SVG. Working with SVGs in React has proven to be a delightful experience. 

%[https://twitter.com/jsjoeio/status/1114635991191396352?s=20]

### Adding Gameplay Music

I never realized how hard it is to create or find music for a game. I ended up finding this amazing sound artist named [Eric Matyas](https://www.soundimage.org) who makes music and sounds royalty-free. I wanted the audio to start automatically (because that's how most games do it) but unfortunately that is [not accessible](https://a11yproject.com/posts/never-use-auto-play/) so it does not auto-play. 

However, if you turn it on at the start menu or when you're playing the game, it adds a nice touch.

%[https://twitter.com/jsjoeio/status/1115436705346019328?s=20]

### Changing Maps

This has to be my favorite feature I added–being able to change the map. At first, I had no idea how I was going to do this, then I thought, "why not just swap the map with another map?"

So that's exactly what I did and it worked! 

I extracted the parts of the map that were clickable (like the buildings) and made it so they open up different maps. I don't know how well my solution will scale but hey, it's working right now and that's what matters. 

%[https://twitter.com/jsjoeio/status/1119834245013196801?s=20]

### Courses Page

One of the other challenges I faced was figuring out where and how to show the courses (i.e. the dialog with the narrator).

Same thing–I struggled with this for a bit then decided, "Let's show it in an Overlay component!"

That ended up working out well. Again, I don't know if that will scale well but it works for now.

%[https://twitter.com/jsjoeio/status/1123063970468786176?s=20]

---

## May 2019

In May, I took a little bit of a break. I was getting married so I wanted to focus on prepping for that rather than my game. I still had ideas for things here and there but I didn't put in nearly as much time as March or April. 

Even though it's difficult for me to take breaks and step away, I think it's healthy to go outside, change what you're doing, mediate, etc. As my mother always says, 

> Everything in moderation. 

---

## June 2019

Looking at the Dashboard I created, there was still so much left to do. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Dashboard-v1.1.png)

I felt overwhelmed.

"How am I going to finish all this?"

### A Realization at the Phoenix ReactJS Meetup

I hadn't been to the [Phoenix ReactJS Meetup](https://www.meetup.com/Phoenix-ReactJS/) in a while. My two coworkers and I decided to go hear the lightning talks.

Before the talks, we were crowded around a table, chatting about our side projects. I said I wanted to finish the MVP for mentored.dev by the end of the year.

"How much more do you have to finish?" 

"A decent amount. Everything on the Dashboard page is hard-coded at the moment."

"Drop all that. Finish the core features and ship it."

Those were the wise words from my coworkers. That's when I realized they were right. I decided to cut scope and implement two last features–the streak tracker and the lesson progress.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-10-at-8.06.01-PM.png)
_Screenshot of the streak tracker_

 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-10-at-8.06.13-PM.png)
_Screenshot of lesson progress_

The streak tracker logic was buggy when I first implemented it and didn't work at all. I wasn't sure if I should only increment the streak after 24-48 hours, or just do it by the day, or what. It [seemed a lot more complicated](https://github.com/jsjoeio/mentored.dev/issues/93) than it should have been.

I still don't know if I'm happy with the implementation. But again, it's out the door and the basic functionality works. 

The lesson progress (completed - 1/3) is also rudimentary at best. Again, my focus was to get it out the door. I'll style it in the future. 

### Ship It

June 29th. The big day.

%[https://twitter.com/jsjoeio/status/1144994580200210432?s=20]

As I say in the tweet thread, 

> ...It's nowhere near complete but I think this is a good stopping point to share the MVP.

A while back, I read _[Lean Startup](http://theleanstartup.com/)_ by Eric Ries. One thing that always stuck with me was something he said along the lines of, "You should be embarrassed putting your product out there. That's when you know it's an MVP."

And that's how I felt! So much left to do. It's hard to even consider it a "game"–most real gamers probably wouldn't.

But that's the point–it helped lift a burden off my shoulders and step back to hear what people think.

Most people I've talked to think it's a good start and a neat concept. They're excited to see where it goes.

---

## What I Think Worked

Reflecting on what helped me launch this MVP, a few things come to mind. 

### Accountability - Friends & Twitter Community

As we all know, it's very easy to silo yourself and work alone. This might work for some people and that's fine. But in my case, I think sharing this project with my coworkers held me more accountable than if I hadn't told anyone. Each week on Monday mornings, one of them would ask, "Hey Joe. Did you work on your game?"

Their interest and support meant a lot to me. They wanted to see it succeed as much as I did. That kept me going.

The other part that kept me accountable was sharing it with people on Twitter. Sometimes people would comment and other times they wouldn't. Either way, people were following along. A few would DM me asking how it was coming along.

By sharing it in public, I felt a bit of pressure (in a good way) to finish it.

### Using GitHub Projects, Issues, and Milestones

I treated this project like we treat client/company applications at work. I didn't use sprints per se but I did keep a list of tasks in a [GitHub Project board](https://github.com/jsjoeio/mentored.dev/projects/3) and then select a few and create a milestone. This made the work feel more achievable and less overwhelming. 

I set up a staging environment at [https://staging.mentored.dev](https://staging.mentored.dev) (thanks to [Netlify](https://www.netlify.com/), this was straightforward). Then, each issue I finished, I submitted a PR to merge into staging. I reviewed and merged myself (yes, a bit silly, but good practice). 

Once a [milestone was complete](https://github.com/jsjoeio/mentored.dev/milestones?state=closed), I merged staging into master and created a new release. This process set me up for success. I kept milestones small (something I could finish in 1-3 weeks). 

Having some type of project management in place for your side project I believe will help you reach the finish line sooner. 

### Cutting Scope

I wouldn't have finished this MVP if I hadn't cut a lot of features. For instance, I really wanted to create a repository called "mentored-dev" after the user logged in and store the lesson progress there. But that was going to take more time than I anticipated so I cut it. 

Instead, I store the progress in localstorage. Yes, it's short-term but again, I had to cut scope to ship. If I hadn't, I wouldn't have finished this phase of the project.

---

## Closing Thoughts

Overall, I feel thankful for all the support. I'm proud of the small project I built and the feedback I have received, so thank you. As for the next steps, I've already created the [next milestone](https://github.com/jsjoeio/mentored.dev/milestone/6). The main thing is to finish all the lessons for the basics of the command line and then share that to see what people think.

As far as actual features–I wouldn't promise anything but I'd love to add experience points (XP) which you accumulate based on your score in the lessons or how many times you take each lesson, how often you login, etc.

It would also be nice to give XP for doing things outside the game (i.e. writing a blog post, tweeting something you learned, contributing to open source, helping someone, etc). We'll see what happens though.

Thank you for listening to the journey. 

###

If you enjoyed this article or found it interesting, please share it with others or let me know on [Twitter](https://twitter.com/jsjoeio).

To stay up to date on mentored.dev or other things I'm working on, I have a newsletter you can [sign up for here](https://github.com/jsjoeio/mentored.dev/milestone/6).

Happy coding! 


