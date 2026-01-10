---
title: 3 Privacy-Focused Open Source Google Analytics Alternatives for Your Next Project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-04T12:20:06.000Z'
originalURL: https://freecodecamp.org/news/3-privacy-focused-open-source-google-analytics-alternatives-for-your-next-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/markus-winkler-IrRbSND5EUc-unsplash.jpg
tags:
- name: analytics
  slug: analytics
- name: Google Analytics
  slug: google-analytics
- name: open source
  slug: open-source
seo_title: null
seo_desc: "By Leonardo Faria\nAs a content creator, I like to know the page analytics\
  \ of my website. \nOverall, I am curious to know how many people are reading my\
  \ content, where they came from (referrer and countries), and what the most popular\
  \ pages are.\n20 yea..."
---

By Leonardo Faria

As a content creator, I like to know the page analytics of my website. 

Overall, I am curious to know how many people are reading my content, where they came from (referrer and countries), and what the most popular pages are.

20 years ago, tools like [Webalizer](http://www.webalizer.org/) were all that we could count on. Tools like this parsed Apache logs and created static pages with the processed data.

![webalizer screenshot](https://www.freecodecamp.org/news/content/images/2020/09/webalizer.jpg)

Another way to get page analytics was to insert an image - often invisible - on your site. By using the request headers sent to the server, people could count visitors and get a little bit more information such as origin IP, browser, and operating system. This technique is old, but services like [statcounter](https://statcounter.com/) still provide this functionality.

In 2005 Google launched Google Analytics after acquiring [Urchin](https://en.wikipedia.org/wiki/Urchin_(software)), a company which also analyzed server logs. Its presence has been growing since the early days and it has far more usage than any of its competitors. But, there are a few reasons [why you should stop using Google Analytics on your website](https://plausible.io/blog/remove-google-analytics): 

1) It is owned by Google, which uses analytics for their own benefit
2) It affects site speed by adding 45KB to page requests
3) It is too invasive, collecting lots of personal data that you don't need
4) It is blocked by many plugins and browsers, creating inaccurate data

With all this in mind, I want to share a few open source alternatives I have been looking at for the last few months.

## Fathom

[Fathom](https://usefathom.com/) ([demo](https://app.usefathom.com/share/sqqvo/chimp+essentials)) is a light Golang app to collect analytics. 

They have different paid plans which start at $14/month. They also have a lite version that you can install on your server or Heroku for free.

![Fathom screenshot](https://www.freecodecamp.org/news/content/images/2020/09/fathom.jpg)

The lite version uses cookies and it gives you information about unique visitors, page views, average time on site, bounce rate, top pages, and top referrers. Fathom stores data in SQLite, MySQL, or Postgresql databases.

## umami

[umami](https://umami.is/) ([demo](https://app.umami.is/share/ISgW2qz8/flightphp.com)) is a solution created with Next.js, making it very easy to deploy. In my case, used Vercel.

On top of unique visitors, page views, average time on site, bounce rate, top pages, and top referrers, umami also shows you information about countries, browsers, OS and device data.

![umami screenshot](https://www.freecodecamp.org/news/content/images/2020/09/umami.jpg)

## Plausible

I think I first heard about [Plausible](https://plausible.io/) ([demo](https://plausible.io/plausible.io)) in the "[De-Google-ing your website analytics](https://changelog.com/podcast/396)" Changelog podcast. From a product perspective, it is nice to see a [public roadmap](https://plausible.io/roadmap) out in the wild so customers can learn what is coming next.

Their plans start at $6/month and go up according to your page views - like Fathom. They also have an _alpha_ self-hosted option, but I didn't have a chance to test it.

![plausible](https://www.freecodecamp.org/news/content/images/2020/09/plausible.jpg)

## Conclusion

There are alternatives out there, and you don't need to worry about a big corp looking at you or your users with these options. Each service's setup time is very similar, and once you're done, you can add multiple sites just like you would with Google Analytics.

I don't have a favorite. Feature-wise, umami provides all the basic information you would want to know for free. It's also very easy to set up on services like Vercel or Netlify. 

Both Fathom and Plausible offer free trials so you can easily test their solutions before deciding.

_Do you know another minimalist, open source alternative to Google Analytics? Let me know in the [comments](https://leonardofaria.net/2020/09/01/three-privacy-focused-open-source-google-analytics-alternatives/) section of my blog._

If you liked this article, follow me on [Twitter](https://twitter.com/leozera) and [GitHub](https://github.com/leonardofaria). 

Cover photo by [Markus Winkler/Unsplash](https://unsplash.com/photos/IrRbSND5EUc)


