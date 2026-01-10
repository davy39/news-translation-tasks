---
title: What the heck is going on with freeCodeCamp's servers?
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2019-10-18T19:36:22.000Z'
originalURL: https://freecodecamp.org/news/freecodecamp-servers-update-october-2019
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/maxresdefault--5--1.jpg
tags:
- name: community
  slug: community
- name: freeCodeCamp.org
  slug: freecodecamp
- name: nonprofit
  slug: nonprofit
seo_title: null
seo_desc: 'Update at 17:00 California time: We have now fixed most of the problems.
  We''re still working on a few known issues, but /learn is now fully operational.

  Here was the culprit - a regular expression-based query that was running against
  millions of data...'
---

**Update at 17:00 California time**: We have now fixed most of the problems. We're still working on a few known issues, but /learn is now fully operational.

Here was the culprit - a regular expression-based query that was running against millions of database records every time a someone tried to authenticate.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/fix_api___revert_regex_based_email_query___37393__-_freeCodeCamp_freeCodeCamp_ebc49be.png)

And here's our cluster's CPU usage before and after we fixed the problem:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-78.png)
_Eureka indeed._

This may seem obvious, but it took [Mrugesh](https://twitter.com/raisedadead) 3 days of detective work to identify the bottleneck.

We've concluded that we could have spotted this earlier with a $30 per month tool, so we broke down and bought it for future usage.

What follows is a more in-depth explanation of what happened.

## In short:

* On Tuesday we rolled out a ton of new code. Including code that allow us to continuously deliver new features and bug fixes.
* We thought we'd load-tested our new code enough. But it wasn't high-performance enough for the sudden weight of 2,000 concurrent users.
* /forum and /news worked fine, but the sign-in functionality on /learn was unreliable for 3 days.

## OK. Now some more detail.

For the past 10 months or so, we've been accumulating new features, bug fixes, and curriculum improvements.

We've continued to merge improvements into our Master branch and deploy them to our beta server at www.freecodecamp.dev.

For the past 2 months, lots of contributors have people using this beta version of freeCodeCamp.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/screen-shot-3.png)

And in celebration of freeCodeCamp's 5th anniversary this month, we wanted to go ahead and push all of these improvements into production at www.freecodecamp.org.

On Tuesday, we went down for what we thought would be 3 minutes of planned maintenance. We did a final testing run, took a database backup, sent out a "we'll be right back" tweet, and pushed 10 months worth of code live all at once.

But Murphy's Law was waiting behind the corner to club us in the knees. And as more and more traffic piled on, our servers buckled.

We were able to get /forum and /news back up almost immediately. But /learn required authentication, and hit some additional API endpoints and servers. So for 3 days we scrambled to get it to work.

It turned out our new code wasn't as high-performance as we'd thought, and we were hitting our API servers a lot more than necessary.

So we identified parts of the codebase that were making unnecessary API calls and refactored them, while also juggling DevOps challenges.

## Why did this happen, though? Really?

At the end of the day, this outage was my fault.

Here's why.

Our total budget for 2019 is only about $300,000. And yet we're helping millions of people learn to code every month.

We now get more traffic than other learn-to-code sites like Udacity and Codecademy. We get even more traffic than mainstream news websites like TechCrunch.

```
+-------------------+------------+
|      Website      | Alexa Rank |
+-------------------+------------+
| stackoverflow.com |         40 |
| github.com        |         85 |
| theverge.com      |        615 |
| wired.com         |      1,435 |
| freeCodeCamp.org  |      1,596 |
| techcrunch.com    |      1,601 |
| codecademy.com    |      2,040 |
| udacity.com       |      2,348 |
| hackernoon.com    |      3,986 |
| dev.to            |      7,684 |
+-------------------+------------+
```

When you operate at such extreme scale with such a paltry budget, you end up clipping coupons.

Those giant servers that could give you comfortable overhead for spikes? Too expensive.

Those fancy DevOps services that identify choke points? Too expensive.

Our team of 5 engineers ends up doing the work of 10.

My point is - it's my fault freeCodeCamp only has $300,000 to work with this year. To put that number perspective, I know individual developers in San Francisco whose salary is larger than $300,000.

There's nothing wrong with having a big salary. San Francisco is an expensive city.

But there is a problem when freeCodeCamp - one of the largest education sites on the internet - is trying to operate on such a comically tiny budget.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/c.jpg)
_What is this? A budget for ants?! (image credit: Zoolander)_

Again, it's my fault.

I'm inexperienced at grassroots fundraising.

I'm still learning how to raise awareness of all the work we're doing for the community.

I am shy when it comes to asking you all to donate money to fund that work.

So I am going to make a concerted effort to get better, and to increase our budget.

I don't want to run ads.

I don't want to say "freeCodeCamp, brought to you by the Acme Corporation."

And of course, I don't ever want to charge learners for our learning resources.

So far, we haven't had to do any of these things.

But this really only leaves us with one source for funding. We, the people.

freeCodeCamp is a grass-roots donor-supported nonprofit. We just need to get better at asking people for money.

We are heading into the holiday season. This is when about 80% of the year's charitable gifts are made here in the US.

So I'm going to stay focused on this. I will document what I learn as I experiment. And I will eventually create a fundraising handbook for other grass-roots donor-supported nonprofits based on what I learn.

This is a bit embarrassing, but our current donate page is down today because our authentication is still wonky.

So I've set up [a PayPal page where you can make tax-deductible one-time donations to freeCodeCamp](https://paypal.me/freecodecamp).

We still welcome your monthly support of freeCodeCamp. Your $5 donations each month are what makes freeCodeCamp possible, and what gives us the stable budget to plan ahead.

But if you do have a some extra cash on hand for a one-time donation, [it would be a huge help](https://paypal.me/freecodecamp).

# Here is my commitment to you:

freeCodeCamp will stay free.

freeCodeCamp will not run ads.

And when we ask you to donate, we will do so tastefully and honestly. We won't use pathos, or make those "we're going bankrupt unless you donate right now" type claims that some other nonprofits resort to.

Because the reality is this: Even if freeCodeCamp completely ran out of money, we would still keep going.

Yes, we would have to lay everyone off, including myself. But I would go get some other job and pay for the servers myself.

Because freeCodeCamp is clearly something that the world needs.

I've poured 5 years of my life into this community. I've poured $150,000 of my personal savings from my teaching career into freeCodeCamp.

freeCodeCamp will never die.

It's just a question of how vibrantly freeCodeCamp can live.

Again, if you have some cash to spare, we are a highly efficient nonprofit, and we will put it to effective use. [Donate here](https://paypal.me/freecodecamp).

And thank you again for your patience with the outage on /learn.

Once we've fixed all this, I will let you all know, and I'll publish my 5th anniversary article that details all the big improvements we have for our 5th anniversary.

Happy coding.

