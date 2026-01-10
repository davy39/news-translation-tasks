---
title: How to make a custom Reddit notification system with Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-08T16:27:21.000Z'
originalURL: https://freecodecamp.org/news/make-a-custom-reddit-notification-system-with-python-4dd560667b35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jwiUzuo1t9kRdDdqTdoYbw.png
tags:
- name: Heroku
  slug: heroku
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: reddit
  slug: reddit
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kelsey Wang

  Don’t you just love automated emails? I know I do. I mean, who doesn’t enjoy waking
  up to 236 new messages from Nike, Ticketmaster, and Adobe Creative Cloud every morning?
  What a fantastic way to start my day! ??

  Anyway, today I’ll be ...'
---

By Kelsey Wang

Don’t you just _love_ automated emails? I know I do. I mean, who doesn’t enjoy waking up to 236 new messages from Nike, Ticketmaster, and Adobe Creative Cloud every morning? What a fantastic way to start my day! ??

Anyway, today I’ll be showing you how to drown your inbox in more clutter, for God-knows-what reason. We’re going to be **using Python to create a custom Reddit email-notification system.** That means we’ll be writing a script that looks for Reddit posts matching some keywords and then emails us when such posts appear.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jwiUzuo1t9kRdDdqTdoYbw.png)
_Want quality email content like this? Read on!_

There are a few reasons that you might be doing this. Maybe you’re really excited about some topic on Reddit. Maybe you’re trying to discover a new karma-farming technique because Internet points are important to you. Maybe you want to send annoying emails to your friends. Or maybe you just want more emails in your inbox to deal with your crippling loneliness. Oops, sorry — went too far. Let’s get started.

### Looking through Reddit

Reddit has a [nice API](https://www.reddit.com/dev/api/) that you can do a lot with. To make things even easier, we will be using [PRAW](https://praw.readthedocs.io/en/latest/), the Python Reddit API Wrapper.

You’ll need a Reddit account first. Once you have one, go [here](https://www.reddit.com/prefs/apps) to create an app. Name it anything, and make sure “script” is selected. As per the docs, you can just put `[http://localhost:8080](http://localhost:8080)` for your redirect URI.

Now, you’re ready to start that nifty script! In the code below, **I look through a subreddit, picking out posts that match my needs.**

I consider a post a _match_ if it is relevant enough and if it is popular enough. More specifically, the post is relevant enough when it has a `keyword_count` that’s not -1 (I’ll explain this below) and popular enough when it has a `weighted_score` greater than a predefined `MIN_RELEVANT_WEIGHTED_SCORE`. The weighted score simply factors in the score of the post and the number of comments on the post. Anyway, this is what best fit my needs, so feel free to better define what a match means to you.

Now, I promised you I would talk about the `keyword_count` party going on. Spoiler: it’s not really a party. I just devised this simple way of assessing relevancy: there are required terms and secondary terms. A post is relevant if and only if all the required terms are in the title, and at least X number of secondary terms are in the title (where X is some predefined number). Again, this part can be re-imagined in infinitely different ways, but this is just what I did.

Now we have everything to comb through our subreddit and tease out the good stuff about conspiracies or whatever. Cool. So, like my homie Ariana says, “thank u, next.”

### Emailing notifications

Time to start spamming. In the code below, I’m using [smtplib](https://docs.python.org/3/library/smtplib.html) (the Simple Mail Transfer Protocol client) to help me send my emails. I then craft the beautiful email with HTML, using the info from Reddit that we got above to populate it. And the best (or worst?) part is, if you want to notify everyone you know about the latest and greatest Reddit posts, you can simply add more email addresses to the `email_list`.

Important side note: make sure the email you use to send the emails have [less secure app access](https://support.google.com/accounts/answer/6010255?hl=en) enabled if it’s a Gmail address, or this will not work.

### Make it run forever

If you don’t have time to continually browse Reddit, you don’t have time to continually run this script. I used Heroku Scheduler to run this script every 10 minutes, as suggested by this [Stack Overflow](https://stackoverflow.com/questions/39139165/running-simple-python-script-continuously-on-heroku) answer. It’s pretty easy to follow: add in a few additional files and a dummy web server, push to Heroku, add the Heroku Scheduler add-on, and _BAM!_ You’re set until you run out of free dyno-hours. ??

Is this the best solution? No. But is it sufficient for my purposes? Yep. If you know of a similarly trivial way to do this, please let me know!

### In conclusion

That’s pretty much all to this project. This [GitHub repo](https://github.com/kelseyywang/reddit-notifs) contains all my code. Because of all the work that literally everyone else has already done, it’s quite a simple task to build this custom Reddit notification system. Gotta love the ✨magic✨ of software development.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bhzl5sep8VGmZTjM7bWe8Q.jpeg)
_Me after setting up my custom Reddit notifications_

If you made it all the way down to here, please comment “North Dakota is the top producer of barley in the USA” in the box below.

Thanks for reading!

