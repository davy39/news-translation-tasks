---
title: 'Zero to 1.5 Million coders: nine lessons learned while building Grasshopper'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T17:37:59.000Z'
originalURL: https://freecodecamp.org/news/zero-to-1-5-million-coders-nine-lessons-learned-while-building-grasshopper-3f8fc96acff7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UcFfMkF_js7dYONzi3xYlg.png
tags:
- name: coding
  slug: coding
- name: growth
  slug: growth
- name: Life lessons
  slug: life-lessons
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Laura Holmes

  Two and a half years ago, I set out to teach people to code from scratch on their
  phones. As of today, 1.5 million people have downloaded Grasshopper. Even with 10
  years of Product Management experience at Google, I was in uncharted t...'
---

By Laura Holmes

Two and a half years ago, I set out to teach people to code from scratch on their phones. As of today, 1.5 million people have downloaded [Grasshopper](https://grasshopper.codes/). Even with 10 years of Product Management experience at Google, I was in uncharted territory building Grasshopper. Here are some of the things I’ve learned along the way:

### Build what you know

I arrived at learning to code by accident. I went to a public high school in California where computer class was learning to type. When I arrived at Stanford, I heard about “computer science”, but had no idea what it was. My freshman Resident Assistant recommended taking a class called “CS106A”. I took it on faith. I found out later that it was Stanford’s introductory Computer Science (CS) class.

As soon as I started the class, I loved computer science but got straight Bs. A lot of folks were surprised I was even taking the class since I was a “girl who liked to talk”. There were so many things I didn’t understand. I remember asking a member of my dorm staff for help one time, and them scoffing saying, “You don’t know Unix?! How can you not know Unix?”

There were so many barriers to feeling comfortable learning to code: jargon, the tools, people’s perception of what a coder looked like. All these obstacles made me feel like I didn’t belong. I ended up getting my degree in Computer Science. I landed a job at Google, but hundreds of times I doubted if I could do it.

Fast forward to about a decade of working at Google. I wanted to figure out what I could do to help with more diversity and inclusion in the tech industry. There’s a lot of amazing work out there. Based on my own experience, I wanted to change one thing: I wanted more people to feel like they could code. I wanted people to have an easier time than I did getting into the software industry.

I ended up pitching Google’s [Area 120](https://area120.google.com/) on a gamified learn-to-code app, with minimal instruction and on mobile ([so that more people could use it](http://www.pewinternet.org/fact-sheet/mobile/)).

### Surround yourself with great people

> _“Alone we can do so little, together we can do so much.” — Helen Keller_

A bunch of great people who care about making coding education more accessible built Grasshopper. In the beginning, it was a few of us. Over the last two years, folks have joined and some have moved on. Through every iteration, people decisions were at the very heart of the app.

I’ve learned over the last 2 years that you can be smart, you can be lucky, and you can have folks with deep expertise on your team. That’s not enough. You need to surround yourself with folks who are going to be team players. Skills can be learned. At the end of the day, I was wrong a lot of the time. It was my teammates’ hard work and patience that allowed us to pivot to where Grasshopper is today.

![Image](https://cdn-media-1.freecodecamp.org/images/B-q5s8RqhQGmvK4ljsvjMBj2SoGw-zFC1IUk)
_The Grasshopper Team (top left, clockwise): Heather, Val, Laura (me), Frankie, Lucas, Elliott, Kris, Phil and Ben_

### Get something in front of users as quickly as possible

We started building Grasshopper in September 2016 and did our first user tests in October. We didn’t have anything built yet, we just had hand-drawn [paper prototypes](https://en.wikipedia.org/wiki/Paper_prototyping).

By November, we had our first prototype and sent 10 folks home with it over Thanksgiving (only 2 people used it).

At each iteration, we learned what worked, and what didn’t. We realized early on that coding puzzles were delightful. We had to make sure the games didn’t feel too kid-like (e.g. no turtle graphics). We learned where users wanted to click to add a new line in our code editor (and that our initial controls were confusing).

By June, we had a rough app that had 13 puzzles and we put it up on the Play Store. We bought some traffic. We kept a low profile and kept learning.

![Image](https://cdn-media-1.freecodecamp.org/images/3ayIDPBEQih8462bkfJ2qlyfqEFx0O0Toa2d)
_Our very first “fully functional” paper prototype_

### Good metrics help you say no

We weren’t sure what success would look like when we started Grasshopper. I knew metrics would help us but wasn’t sure which numbers mattered. I read a lot of blogs about growth. Then I started looking at the following metrics to gauge Grasshopper’s success: active users, onboarding success, week 1 retention, cost per acquisition, curriculum completion, and content creation per week.

That’s a lot of different metrics.

Having a lot of metrics made it hard to make decisions.

Did we want to build a feature to increase our daily active users? Or reduce the cost of acquisition? Did we want people to spend more time in the app or get through our lessons? What did it mean when one metric went up and another one went down? Which metrics were the most important?

It took a few months until I realized I needed to narrow. We decided to focus on only two metrics: Day 1 retention and Graduation Rate. We held ourselves accountable to student learning (Graduation Rate), while also building an engaging product that would keep users coming back (Day 1 retention). And we focused on Day 1 retention because it was our first opportunity to measure a user coming back. All other retention goals are downstream of Day 1.

Noticeably absent is any user growth metric. We didn’t need to grow until we’d nailed these other two metrics. If we weren’t keeping users interested and we weren’t teaching our students, we weren’t ready to pour more gasoline on the fire.

Narrowing down to two success metrics was clarifying. We didn’t spend time on marketing beyond some simple paid campaigns. We could look at our list of ideas and focus on the best ones based on whether they helped with retention or graduation. Things like tablet support, making the code editor support more use cases, and referrals were no longer important.

Once we had a shared set of goals, we were able to start making some hard decisions.

### Your users are right

From June to December 2017, things were rough. We had agreed on our success metrics, but we weren’t making either of these numbers go up.

We made a lot of changes to the app. We expanded our curriculum to create a better “end-point”. Nothing seemed to improve our metrics. I kept hoping the next change would be the one, but it wasn’t.

We continued hearing from users that our curriculum was confusing and that they really wanted a progress bar. I didn’t get it. We’d designed our curriculum to be dynamic so that the *perfect* next lesson was picked for the user based on their performance. That way lessons could also be swapped in and out, too. And we’d just added a progress bar. Why weren’t users getting it? Couldn’t they see the progress bar?

At the same time, some folks on my team had started to note that they didn’t feel comfortable with the dynamic curriculum. It was confusing to them, and it was computationally expensive.

![Image](https://cdn-media-1.freecodecamp.org/images/6a36hrhxBZGTWDabJqZgk2NMavkCYcsNoA1O)

That’s when I realized: Our users were right. They’d been telling me all along that our app was confusing, but I just wasn’t understanding. And my teammates had heard them too, and I still wasn’t listening. I was too attached to how we’d been doing things and the investments we’d made.

So we made a pivot to make our curriculum a linear path, with clear progression and progress. We stopped trying to be too smart, and listened. And that’s when everything started to change for the better: all our numbers started to go up and to the right.

### Stick to your core, the rest is just details

When we made the pivot from a dynamic curriculum to a linear one, I was super concerned. Our investors thought that the dynamic curriculum was cool, so did people on our team. Was this new strategy interesting enough to keep our team excited? And this new model had us using points and achievements. Was that cheating?

That’s when I reminded myself of why I wanted to build Grasshopper: I wanted to teach more people to learn to code. The dynamic curriculum wasn’t working; swap it out for a curriculum that did work. Who cares if you’re using a points system, as long as more people learn?

Building Grasshopper has been a learning journey in letting go and empowering the people on my team to make decisions (and it’s a journey I’m still on). It turns out that if you have a great team, the best ideas will come from them. My job as the lead is making sure that we’re all arriving at the same place: teaching more people to learn to code.

Since making our pivot last year and realizing that I was too attached to a version of the app that wasn’t working, I’ve been more open to suggestions and experimentation. I’ve let go a little, and it’s been great to see what my team has done when given more responsibility. My team has built features, developed new courses, and made changes to Grasshopper that I wasn’t initially sold on. But it turned out I was wrong, and the features my team developed increased our core metrics. We’ve also unlaunched some things. But the most important thing has been staying true to our mission and never wavering. The rest is just details.

### Go for growth when the metrics are right

Through my years at Google, I had learned that you don’t want to overpromise and get it wrong. You can never recover user trust. When I worked on [Project/Google Fi](https://fi.google.com/about/), we onboarded users slowly until we knew our customers would have a great experience, and it went well. I wanted to follow a similar model with Grasshopper, and not do marketing and press until we knew we had a great product.

After months and months of flatlined metrics, we returned from the holidays to graphs that went up and to the right. We were so excited. The pivot to the linear curriculum paid off!

In September 2017, we had set some goals for Day 1 Retention and Graduation Rate, and we hit them by February 2018.

In addition to seeing our success metrics go up, we actually saw organic growth taking off. Starting in January, we saw a larger and larger percentage of our growth coming organically.

By February, we knew we were onto something that was working, so we decided to put announcement plans into action. We were surprised that no one had paid attention to Grasshopper even though it was public for months. Because we kept a low profile, we gave ourselves the opportunity to announce and tell our own story once we knew the product was right.

![Image](https://cdn-media-1.freecodecamp.org/images/YLPmPFwHqaXfXz3w5jF01ZmCWcotx2gHC1pd)
_Graph of our 7-day [moving average](https://en.wikipedia.org/wiki/Moving_average" rel="noopener" target="_blank" title=") on Day 1 retention. After months of flatlined success metrics, our pivot resulted in 2x Day 1 retention, even as we added more users._

### Monitoring and scaled support pay off

On announcement day, we got into the office at 5 am PT. [TIME Magazine did an exclusive on Grasshopper](http://time.com/5243949/google-grasshopper-game/), and it was going to hit the site at 6 am PT. Nothing was open, so we brought a waffle iron to the office and cooked some bacon in our microwave.

Once the story launched, we saw our metrics start to climb. It was super exciting! [TechCrunch did an article](https://techcrunch.com/2018/04/18/grasshopper-a-learn-to-code-app-from-googles-area-120-incubator-goes-live/). And then a [bunch](https://www.theverge.com/2018/4/19/17258694/grasshopper-javascript-mini-games) [of](https://www.androidauthority.com/learn-to-code-for-free-grasshopper-856762/) [other](https://www.androidcentral.com/learn-how-code-free-area-120s-new-app-grasshopper?utm_source=ac_tw&utm_medium=tw_card&utm_content=66807&utm_campaign=social) [outlets](https://www.bustle.com/p/googles-grasshopper-mobile-game-teaches-adults-how-to-code-in-easy-accessible-way-its-free-8839675) started to pick us up. By 3 pm, things had leveled out and we decided to go out and grab a beer to celebrate. We’d launched, gotten a lot of new users and nothing broke. Growth was modest, but we were out there in the wild. A job well done. We went home that night feeling good.

The next morning, things were on fire. Asia had picked up our launch. Our engineering team was alerted just in time, and they turned off non-essential services (like our dashboards) before our server load prevented Grasshopper from functioning.

Once we got our data back, we found out that we had 63xed our previous 24-hour record. We had been hoping for 10x. The next few weeks were hard. Our engineering team worked to rewrite our backend to be scalable, and our curriculum and support team handled user issues. We survived because we’d invested in monitoring, in building toggles to turn off services quickly, and in a forum and in-app feedback system that scaled for massive user growth.

If you’re ever in a similar situation, I can’t emphasize enough how helpful it was to have all these things in place *before* we announced.

### There is no such thing as work-life balance; there is a work-life compromise

Fast forward to today, and we have 1.5M users now using [Grasshopper](https://grasshopper.codes/). I’m so proud of the team and what we’ve accomplished, and proud of our students for how much they’ve learned to code. But time to get a little personal:

During all this, I also had my first baby. I was going through first-trimester exhaustion while executing our pivot. I was 35-weeks pregnant when we did our public announcement in April. And I still feel like I’m ramping back from maternity leave, even though I’ve been back at work for a couple of months. Adjusting to parenthood + working on Grasshopper has been filled with unexpected challenges.

I wish I had advice for folks here. I wish I could tell you that with a successful career and lots of resources, work-life balance snaps into place. I can’t. But what I can offer is being real about what it’s like, balancing between being a leader and a mom: It’s f-ing hard. Work-life balance implies that there’s some sort of ideal state of goodness that can be achieved if one works hard enough. Instead, I’m constantly trading off between taking care of my family and my company.

I leave work at 5 pm so that I can have some time with my daughter before putting her to bed. Some nights, I skip time with my husband to work on Grasshopper, only to have my daughter wake up unexpectedly early the next day. I’ll do my best to feed her, but because I’m so tired, we don’t smile as much together before I head to work. And then I’m less creative when thinking about Grasshopper strategy during the day.

Being a working parent feels like I’m doing a complex ROI analysis on every activity, for work and family. All I can hope is that I’m making the right choices along the way, and be humble about the challenges. I hope that being honest about the challenge gives the working parents reading this post permission to celebrate all the amazing daily compromises you make. And if you’re reading this and aren’t a parent, but work with folks who are, maybe think about telling them how great a job you think they’re doing in both their roles.

If you’ve made it this far, thanks so much for reading! Hope you’ve found some of the lessons valuable, and hope to be back to the freeCodeCamp blog soon to share some more insights from Grasshopper. And if you’re looking for a way to get started on your coding journey, download [Grasshopper](https://grasshopper.codes/). I’d love to hear your thoughts and feedback.

_I also write and tweet about diversity and inclusion topics. To follow me, here’s [my Twitter](https://twitter.com/fearofpoets) and [my blog](https://www.fearofpoets.com/)._

