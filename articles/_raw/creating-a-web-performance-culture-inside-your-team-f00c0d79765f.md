---
title: How to create a web performance culture inside your team
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T12:32:57.000Z'
originalURL: https://freecodecamp.org/news/creating-a-web-performance-culture-inside-your-team-f00c0d79765f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f-Ey0tW6O_vFHz_RPZWh_A.jpeg
tags:
- name: Culture
  slug: culture
- name: JavaScript
  slug: javascript
- name: teamwork
  slug: teamwork
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Alex Moldovan

  Those who work with me know that I’m always obsessing about performance. Words like:
  critical rendering path, bundle size and frames-per-second are a common thing around
  the office. But it’s all for a good reason.

  Performance should ...'
---

By Alex Moldovan

Those who work with me know that I’m always obsessing about performance. Words like: critical rendering path, bundle size and frames-per-second are a common thing around the office. But it’s all for a good reason.

Performance should be a **first class citizen** in software engineering.

Having a strong **performance culture** in your team can ensure that you mitigate — ahead of time — any risks associated with bad performance.

But why is it so important? And what are those risks?

## Why performance matters

Remember that as web developers, our goal is to create the best possible experience for our users.

### Performance is about usability.

There are many studies ([[1]](https://www.doubleclickbygoogle.com/articles/mobile-speed-matters/), [[2]](https://wp-rocket.me/blog/speed-up-your-website-make-the-first-few-seconds-count/), [[3]](https://www.fastcompany.com/1825005/how-one-second-could-cost-amazon-16-billion-sales)) that show a direct correlation between business goals and usability on the web.

A fast and snappy website can make the difference between success and failure when it comes to the relationship with your users.

Your fancy UI framework and architecture won’t matter at all if your website is perceived as slow and laggy. Not to mention the scenario in which users leave because they are waiting behind a spinner or a white screen.

[53% of the users will close your website within 3 seconds](https://developer.akamai.com/blog/2016/09/14/mobile-load-time-user-abandonment) if you don’t show any content.

Furthermore, performance is also a metric in mobile page ranking, [according to Google](https://webmasters.googleblog.com/2018/01/using-page-speed-in-mobile-search.html).

### Performance is about accessibility.

Let’s talk about the global market. Performance budgets are also important when it comes to the cost of data. How much does a user pay to visit your website?

You can find out using [this website](https://whatdoesmysitecost.com/#usdCost). Then you can ask yourself: “Am I willing to pay x cents to visit my website?” You might be surprised by your own answer.

Furthermore, there are countries where the vast majority of [internet time is spent via mobile](https://www.smartinsights.com/mobile-marketing/mobile-marketing-analytics/mobile-marketing-statistics/). So you have to take a mobile-first approach in optimizing performance.

By omitting this, you are rendering your product inaccessible for a lot of people!

### Performance is about empathy

We have the tendency to see our work strictly through our own eyes. This is dangerous, as it leads to a superficial understanding of our users’ needs.

Not to mention our constant need to work on the cool stuff (new technology, state of the art frameworks, and so on) and ignore boring and tedious jobs.

Performance matters, and you have to work on optimizing it with **empathy** and **selflessness** in mind. But these qualities, unfortunately, don’t come by default in all working environments.

## Plan for the worst

A colleague showed me an interesting scenario a few weeks ago. There’s a home decor website which is using some CMS system behind the scenes to manage data. Someone uploaded this image:

![Image](https://cdn-media-1.freecodecamp.org/images/4u0XBu8dfPbS9KEEuq0Uc1ad5g9cMbqoJb3g)
_screenshot from Chrome Dev Tools_

It’s **9.3 MegaBytes** of data which takes roughly **7 seconds** to load on an ultra fast Wi-Fi connection and on a MacBook Pro. Can you image how much time this would take on a mobile device? The answer is **infinity**! Because the mobile browser becomes unresponsive when you open the website.

[Here’s the website](http://www.homemade-modern.com/ep106-media-console/) if you’re curious, but please proceed with care as it will potentially block your browser!

We shouldn’t blame the user. They wanted to display a very detailed image of an assembly.

Coming back to the idea of **understanding** our users, we should always prepare for the worst scenarios when it comes to user created content.

As a developer, you are **completely responsible** for the way in which your users interact with your software.

## When to optimize

There are two approaches to performance optimizations. [Ben Schwarz](https://twitter.com/benschwarz?s=17) summarizes the two approaches in his deck, [The Critical Request](https://speakerdeck.com/benschwarz/the-critical-request).

![Image](https://cdn-media-1.freecodecamp.org/images/LQhLZLaEKGlTWi5btGkboK0W2JOjNv6QRxKF)

![Image](https://cdn-media-1.freecodecamp.org/images/fulD0TWIdNZHkuxffOBGWBmxvWBZftfMwpZc)
_**Reactive** (top) vs **Proactive** (bottom) approach to optimizing performance_

On one end, we have the traditional: “Houston we have a problem!” approach. This is a highly **reactive** way of treating performance issues. I also like to call it the: “Oh shoot! Call in the consultant!” problem.

Not only is this costly for your business, but it can also be a great demotivator for the team. It can even lead to conflict when people are not connected with the goals of performance optimization.

On the other end, we have the **proactive** approach. You bake performance optimization into your software development process.

If you need to convince the business side to try the proactive approach, check out [WPO stats](https://wpostats.com/). This is great resource with case studies that show the benefits of performance optimizations.

Once the approach is in place, it’s the team and the culture that solve the problems ahead of time, rather than the consultant who comes in to save the day. And done right, this can be a great motivator for the team.

But performance awareness doesn’t happen over night. You have to create the right context for people to be aware of the impact of what they do.

## Measure and Act

Do you know how many users are landing on your site from mobile devices? How often are you testing in bad network conditions? How often do you take out a mid-range device, like a [Moto G4](https://www.gsmarena.com/motorola_moto_g4-8103.php), and start playing with your application?

These are all relevant scenarios that your users might encounter every day!

Know your user base, and know your device and browser usages. Good and relevant **metrics** are everything if you want to implement a performance culture.

Once you have the metrics, it’s time to establish the **performance budgets**.

Finally, time to act! Here are some tools and practices you can introduce into your regular work environment:

### Step 1: Measure performance indicators

* [Lighthouse](https://developers.google.com/web/tools/lighthouse/) is an amazing project and is available in Chrome Dev Tools. It will give you great insights into potential performance improvements. It will also give you some nice suggestions for SEO, Accessibility, and Best Practices.
* [Webpagetest](https://webpagetest.org/) is great for keeping track of metrics and comparing waterfall charts before and after deploys. I can also recommend [gtmetrix](https://gtmetrix.com/), a less known tool, with a very easy to use interface.

### Step 2: Automate

* Add performance related build steps into your CI. [bundlesize](https://github.com/siddharthkp/bundlesize) is a great package if you want to define some hard limits for your bundles.
* Build automated tests that will fail if loading times or other relevant metrics exceed certain thresholds. [Puppeteer](https://github.com/GoogleChrome/puppeteer) has direct access to the Chrome API so you can leverage that in your tests.

### Step 3: Make it visual

* Everyone in the team should be aware of the impact of the code they write. [Webpack bundle analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) is a great way of visualizing what goes inside the output bundles. People might think twice before using a library which increases the overall size by 10%.
* [import cost](https://github.com/wix/import-cost) for VSCode will show you how much code you are adding to the project by using certain dependencies. Again, it’s all about making sure everyone is fully aware of the impact of what they do.

### Step 4: Enforce and Empower

* You have to be ready to enforce strict rules within the organization. In our case, we created a [performance checklist](https://github.com/FortechRomania/js-team-showcase/blob/master/how-we-work/performance/checklist.md) to be followed on each project.
* Make sure **everyone** in the team gets to work on the performance optimization tasks. You don’t want to have a single person that does that, because you get into the consultant scenario again. By splitting the tasks, everyone gets familiar with the context and with the different ways of preventing problems.

Building a performance oriented **culture** is a step by step process. And it’s a process of **understanding** the problems and **acting** on them.

One constant in the entire process is the need to **educate** people.

Performance optimization techniques are not complicated. But they need some technical background and a good understanding of how the web works.

Building on top of a solid foundation can help your team grasp even the most advanced techniques for speeding up your application.

In our case, we make sure web performance is part of the learning path for all engineers. We don’t just enforce a checklist. We make sure people have a good environment to learn the reasons behind the techniques.

![Image](https://cdn-media-1.freecodecamp.org/images/hkpZovJ1oITO9WFs3xjZzrDaUKIPzwyZ2Ig6)
_[Performance cheatsheet poster](https://github.com/FortechRomania/js-team-showcase/blob/master/how-we-work/performance/performance-cheatsheet.png" rel="noopener" target="_blank" title=") in our office at Fortech_

## Performance as part of software quality

In the end, working on performance is the same as working on UX, security, or accessibility. It is part of the **software** **quality** that you offer.

At times, it might seem like extra effort for something that is not requested of you. Performance might not be part of your non-functional requirements, after all.

But coming back to the idea of responsibility, it is our duty to provide the best possible quality. And performance is one of the pillars of software quality.

If I were to sum up the path towards a performance culture, these are the key takeaways:

* Raise awareness, and build with empathy for the user
* Favour the proactive approach and deal with issues ahead of time
* Measure and act in a continuous loop
* Spread the knowledge and involve the entire team in the process
* Make it part of your software quality as an end goal

## References

Since a lot of people ask for materials on web performance, here are a couple of places you can start from:

* [Google Developers portal](https://developers.google.com/web/fundamentals/performance/why-performance-matters/) has great articles on performance optimization techniques
* [perf-tooling.today](https://www.perf-tooling.today/) offers a lot of great resources on web performance
* [The Chrome DevTeam’s publication](https://medium.com/dev-channel) explores a lot of great ideas and case studies about improving the performance of popular websites.
* Check out our [performance checklist on github](https://github.com/FortechRomania/js-team-showcase/blob/master/how-we-work/performance/checklist.md) and contribute with ideas!
* Also have a look at Smashing Magazine’s 2018 [front-end performance checklist](https://www.smashingmagazine.com/2018/01/front-end-performance-checklist-2018-pdf-pages/), it is really impressive!

I’m super curious to hear your thoughts on this. Is your team embracing a performance culture? What works for you? What doesn’t? Leave a comment and share if you enjoyed this article!

