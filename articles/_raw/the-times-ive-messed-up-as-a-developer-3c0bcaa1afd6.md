---
title: A brief dive into 2 times I clearly had no clue what I was doing as a developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-10T11:36:37.000Z'
originalURL: https://freecodecamp.org/news/the-times-ive-messed-up-as-a-developer-3c0bcaa1afd6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6dix1lxlAXUO7Gg4EPjgBg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Zachary Kuhn

  Last week I had a short conversation with coworkers about how we had messed up in
  our careers. Being so far removed from those mistakes, it was easy to laugh. More
  than laughs, though, these screw-ups served as powerful lessons for us...'
---

By Zachary Kuhn

Last week I had a short conversation with coworkers about how we had messed up in our careers. Being so far removed from those mistakes, it was easy to laugh. More than laughs, though, these screw-ups served as powerful lessons for us.

It’s important that we share our mistakes so that others can learn from them and maybe feel more comfortable with their own. So here are a couple of my more recent ones.

### Why So Many Dropped Production Databases?

![Image](https://cdn-media-1.freecodecamp.org/images/6Scwn1EYrNsLjS9YXCF0ZaiO600eVCqUp-8F)
_Source: [pexels.com](https://www.pexels.com/photo/interior-of-office-building-325229/" rel="noopener" target="_blank" title=")_

A few months ago, there was [the post on Reddit](https://www.reddit.com/r/cscareerquestions/comments/6ez8ag/accidentally_destroyed_production_database_on/) of an entry level developer who deleted the production database on his first day. We all cringe reading stories like this of those who make those big, unforgettable mistakes. We realize it wouldn’t take much for that to be us—most have had close calls.

In my first job, a senior database administrator dropped the production database on his first day. These stories are everywhere. The team restored his mistake from a week old backup and kept him around. Ten years later they still poked fun at him for it.

One morning earlier this year I was called on to look into a production problem for a client. They were beginning to beta test their site with a small audience when overnight their site’s homepage didn’t have anything on it. I wondered if there was a bug or vulnerability that led to this.

I signed in to the production machine and pulled up the database. The articles table was empty. OK, that confirmed what we were seeing on the website.

The users table still had users. Weird. So we lost all our articles but at least their beta users still had their accounts. We could explain that it’s a beta and these things happen.

The next few moments were a blur. I don’t recall exactly what I did. I don’t _think_ I was dumb enough to type `drop table users` in the console. But there I was, now with no articles and no users table. I sat there in shock for a bit.

Then my mind raced on how to fix this. Did I really drop the users table? Yes. Did we run backups? No. How do we tell the client this? I don’t know.

I remember walking over to the project manager, sitting down next to her, and explaining what had happened. We didn’t have data in our articles table, so that’s why the site looked empty. And oh yeah, I also dropped the users table. They were now going to need to re-invite all those users—if they could figure out who they all were. Yikes.

I went back to my desk feeling defeated.

**Something didn’t sit right with me, though.** How did we lose all those articles in the first place?

I kept digging. Part denial, part wanting to save face. Shortly afterwards, I noticed something important.

There were five other databases on the server. One of them had a name similar to the database I had just been looking at.

When I checked it out, all the articles were there. The users table was fine. It turns out a configuration change had inadvertently made it to production, causing the site to point to a brand new database. Those users I saw? Seed data.

What a relief! A morning of nerves and stomach acid making me feel sick, but we were able to “recover” all the data and I had found the real issue before we were to communicate the bad news.

Lots of lessons learned from the episode. One of the simplest: now we always do backups… perhaps a developer’s most effective antacid.

### Rushing And Never Getting Ahead

![Image](https://cdn-media-1.freecodecamp.org/images/f8o2lgSjOXUuocF8dbdEjcdLZHKDE4qFfDtF)
_Source: [pexels.com](https://www.pexels.com/photo/time-lapse-cars-on-fast-motion-134643/" rel="noopener" target="_blank" title=")_

One of my other recent mistakes that stands out wasn’t near as dramatic. In fact, it was tiny mistake after tiny mistake that led to a mess in the end.

Our challenge was a project on a tight timeline. (Aren’t they all, though?)

In our first meeting, we agreed as a team this would take twice the time we had. With the deadline bearing down on us from the very beginning, I breezed through the authentication piece so we could move on to the functionality the client really cared about.

I had only implemented authentication once before in a single page app and still didn’t fully understand how it was supposed to fit together.

What a mistake to hack it out as fast as I could. **I missed a few important things:**

1. The user loaded from a cookie after sign in, but the page tried to load without waiting. Depending on the order of these events, you’d get responses from the server saying you were unauthorized. The error was rare and tough to reproduce because _most_ of the time, things completed in the right order.
2. The authentication also never checked whether the token had expired. If you didn’t visit the site often, when you’d return the site wouldn’t work and you’d have to sign out and sign back in.
3. The token was supposed to update with every request, but I never had the time to understand the rules around it. So this once again produced a timing issue. If we sent several requests at the same time, depending on the order they returned you’d get the wrong token being used in future requests.

We rushed and we still ended up taking twice the time given. The difference was many more bugs, and then spending even more time tracking down and fixing those bugs.

My work embarrassed me. Then being shamed in public for it made the whole experience that much worse.

I will say one thing: since then, I took the time to learn authentication. I now understand OAuth, JWT, refresh tokens, and expirations. I pored over authentication code others had written in a number of libraries. I built authentication flows in a few different languages and frameworks.

### Turning Failures into Future Successes

That’s the one thing I take away from everything that goes bad. Almost always something good comes from it if you will it.

If someone learns from their mistake, they are now better than they were before. I try not to get down on a teammate who makes a mistake the first time. They usually already know they messed up.

I’m working on not being so hard to those who repeat the same mistake over and over, though. They still deserve compassion.

You’ll continuously grow if you can do four things with mistakes:

1. laugh at having made one
2. learn from it
3. destigmatize making them
4. and share your mistake so others can benefit from it, too

I’ll leave you with a final anecdote about the value of mistakes. IBM’s CEO during the early 1900s, Thomas J Watson, once encountered an employee whose series of bad decisions cost the company greatly. When asked whether Watson was going to fire this employee, Watson responded:

> “No, I just spent $600,000 training him. Why would I want somebody to hire his experience?”

Have an interesting mistake in your past? Share it!

Thank you for reading the article! If you find it helpful and would like to show your support, then please share it and be sure to hit that ? button. For more articles like this, follow t[he publication](https://twitter.com/freeCodeCamp) and t[he author](https://twitter.com/zacharykuhn) on Twitter.

[_Zach Kuhn_](https://www.linkedin.com/in/zacharykuhn/) _is a Director of Development at Smashing Boxes, a Durham, N.C.-based digital agency. He has built web and mobile apps for over a decade, and is involved with startups and emerging technologies like blockchain, IoT, and machine learning._

