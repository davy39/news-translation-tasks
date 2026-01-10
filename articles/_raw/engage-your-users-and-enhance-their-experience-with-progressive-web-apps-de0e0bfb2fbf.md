---
title: Engage your users and enhance their experience with Progressive Web Apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T09:44:05.000Z'
originalURL: https://freecodecamp.org/news/engage-your-users-and-enhance-their-experience-with-progressive-web-apps-de0e0bfb2fbf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h2X9ckg3FJr4FGSfwh0F2w.jpeg
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dave Gray

  What is a Progressive Web App?

  A Progressive Web App (aka PWA) is a duality. It is both a website and a web app.
  A PWA provides progressive enhancements to new and existing websites. These mobile-focused
  enhancements are easy to justify....'
---

By Dave Gray

### **What is a Progressive Web App?**

A **Progressive Web App** (aka PWA) is a duality. It is both a website and a web app. A PWA provides [progressive enhancements](https://developers.google.com/web/updates/2015/12/getting-started-pwa) to new and existing websites. These mobile-focused enhancements are easy to justify. [Mobile Internet usage passed desktop Internet usage in the fall of 2016.](https://techcrunch.com/2016/11/01/mobile-internet-use-passes-desktop-for-the-first-time-study-finds/) It is truly a mobile-first world.

One such enhancement is the “Add to Home Screen” option. Websites enable this feature in some browsers by [meeting specific PWA design criteria](https://developers.google.com/web/fundamentals/app-install-banners/#what_are_the_criteria). This feature lets you save the PWA icon to your home screen alongside your other app icons. You can then launch the PWA with the look and feel of an app.

![Image](https://cdn-media-1.freecodecamp.org/images/hfv56qaFb28RtMwcPtMmlxU5xC3tizX4HPTQ)
_The default message from Firefox Beta when visiting a Progressive Web App._

Web developers may now design an “app-like” full screen experience for users. HTML, CSS, and Javascript are the only necessary programming languages. Native mobile device features including push notifications, camera, geolocation, and [much more](https://whatwebcando.today/) are now available for use. Also, a PWA should still provide functionality even if you lose your data connection. It should work offline!

[Google has defined three areas](https://developers.google.com/web/progressive-web-apps/) that are “musts” for Progressive Web Apps: They must be **reliable**, **fast**, and **engaging**. Google states that Progressive Web Apps should “_load instantly, regardless of the network state_”, “_respond quickly to user interactions_”, “_live on the user’s home screen_”, and “_offer an immersive full screen experience_”.

### **Why do I (or why does my company) need a Progressive Web App?**

You can **eliminate the need to develop separate solutions** (iOS, Android, Web) when a Progressive Web App will suffice.

PWAs are not replacements for all mobile apps by any means. There are many mobile apps with features PWAs cannot replicate. However, if your app focuses on information sharing (posts, pics, products, support, social interaction), a PWA is a great choice.

Another answer to the question “Why?” is **reach**.

Referencing the comScore 2017 U.S. Mobile App Report ([request your access here](https://www.comscore.com/Insights/Presentations-and-Whitepapers/2017/The-2017-US-Mobile-App-Report)), 87% of usage time is on mobile apps vs. 13% of usage time on mobile web. Yet when comparing the reach of the Top 500 Mobile Web Apps vs the Top 500 Mobile Web Properties, mobile web has more than double the reach — 15.7 million average monthly unique visitors vs. 7 million for mobile apps.

In addition, comScore notes that 80% of users intentionally moved apps to their home screen in 2017 which is up 5% from 2016.

![Image](https://cdn-media-1.freecodecamp.org/images/AW2wV7m8DAOiyp7gyPyTPwyZ3oK3rT07hi92)
_The Pmount PWA installed on the home screen and ready to send push notifications for daily specials._

Progressive Web Apps combine the capabilities of native app features that drive **high usage times** with the **reach of web properties** and the ability to **install on the home screen**. This hybrid combination makes Progressive Web Apps worth consideration.

Several websites are **already taking the step** to full-functioning Progressive Web Apps.

![Image](https://cdn-media-1.freecodecamp.org/images/1aj7EZIQJsVV120dVqijEx5ykn4frLp04V01)
_The Twitter Lite PWA requesting permissions for push notifications and a home screen icon_

[Twitter Lite](https://mobile.twitter.com/) is a great example utilizing push notifications and offline functionality. Twitter’s PWA “[significantly increases engagement and reduces data usage](https://developers.google.com/web/showcase/2017/twitter)”.

![Image](https://cdn-media-1.freecodecamp.org/images/b7AfNLZRm9FWG8COOXRqKV0VdpzxbP9Tjv3k)
_The Pinterest PWA resulted in an increase of 40% more time spent in the mobile experience_

This [Pinterest PWA case study](https://medium.com/dev-channel/a-pinterest-progressive-web-app-performance-case-study-3bd6ed2e6154) reveals impressive statistics and valuable insights. In comparison to their previous mobile web experience, Pinterest achieved an increase of 60% in core engagements. Their user-generated ad revenue increased by 44%. In addition, time spent is up by 40%.

![Image](https://cdn-media-1.freecodecamp.org/images/gfROMdw0E8X1UM9sVT5gNTbGTq7HphHr3F-y)
_Over half a million Trivago users have already decided to “add to home screen”_

Trivago’s PWA is achieving amazing results. [More than half a million users](https://www.thinkwithgoogle.com/intl/en-gb/consumer-insights/trivago-embrace-progressive-web-apps-as-the-future-of-mobile/) have utilized their “add to home screen” functionality. The engagement of those users is up 150%. [Trivago](https://www.trivago.com/) discusses their PWA decision [in this video](https://youtu.be/pFE3LRRxqlo).

Many other examples of PWAs exist. Start your search at [pwa.rocks](https://pwa.rocks/) and this [list of 5 awesome PWAs](https://deanhume.com/home/blogpost/5-awesome-progressive-web-apps-worth-exploring/10153).

### **How do I get started?**

If you are a web developer, a great place to start is the [Google Developers Progressive Web Apps page](https://developers.google.com/web/progressive-web-apps/). You will need to learn about [Service Workers](https://developers.google.com/web/fundamentals/primers/service-workers/) and [Web App Manifests](https://developers.google.com/web/fundamentals/web-app-manifest/).

Google provides an automated website audit tool called Lighthouse. Lighthouse audits [five categories](https://developers.google.com/web/tools/lighthouse/scoring) for your app: Progressive Web App, Performance, Accessibility, Best Practices, and Search Engine Optimization. The detailed Lighthouse audit report will give you 15 pages of details with over 50 individual audit results.

![Image](https://cdn-media-1.freecodecamp.org/images/6Sqon96qx2nVOJugWsfb2ApTSZsxEEkruXto)
_The five categories of audit results provided by Lighthouse._

If you are not a web developer, you will need to find one to create or update your current website to a progressive web app. PWAs are currently developer-intensive. I am not aware of any service that takes the knowledge of code out of the solution. If you own the local pub or coffee shop, you might find a frequent patron who is also a developer that needs a PWA test project. (See [thepmount.com](http://thepmount.com)) In the coming months, I plan to publish articles on each step of the PWA creation process.

### **Conclusion**

**Progressive Web Apps** provide [progressive enhancement](https://developers.google.com/web/updates/2015/12/getting-started-pwa) to existing websites and set [new criteria](https://developers.google.com/web/fundamentals/app-install-banners/#what_are_the_criteria) for both pre-existing and new web apps to strive for. Meeting the PWA requirements and passing the [Lighthouse audits](https://developers.google.com/web/tools/lighthouse/) will help provide [reliable, fast, and engaging](https://developers.google.com/web/progressive-web-apps/) user experiences on mobile devices… and that is something we should all benefit from.

![Image](https://cdn-media-1.freecodecamp.org/images/jElxr0WSiaE1TRYpVhvO2nrl9HZ1zdgjvEEr)
_Today’s Americano from the local coffee shop_

Reach out to me any time on [LinkedIn](https://www.linkedin.com/in/davidagray/) or [Twitter](https://twitter.com/yesdavidgray). And if you liked this article, give it a few claps. I will sincerely appreciate it.

[**Dave Gray | Professional Profile | LinkedIn**](https://www.linkedin.com/in/davidagray/)  
[_View Dave Gray's professional profile on LinkedIn. LinkedIn is the world's largest business network, helping…_www.linkedin.com](https://www.linkedin.com/in/davidagray/)[**Dave Gray (@yesdavidgray) | Twitter**](https://twitter.com/yesdavidgray)  
[_The latest Tweets from Dave Gray (@yesdavidgray). Instructor @FHSUInformatics * Developer * Musician * Entrepreneur …_twitter.com](https://twitter.com/yesdavidgray)

