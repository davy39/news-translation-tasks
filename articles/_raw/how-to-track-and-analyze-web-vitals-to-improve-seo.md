---
title: How to Track and Analyze Web Vitals to Improve SEO
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-19T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-track-and-analyze-web-vitals-to-improve-seo
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vitals.png
tags:
- name: analytics
  slug: analytics
- name: data
  slug: data
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: SEO
  slug: seo
- name: Software Engineering
  slug: software-engineering
- name: web vitals
  slug: web-vitals
seo_title: null
seo_desc: "By Adam Henson\nGood news - we now have a brand new set of standards by\
  \ which to judge our search engine's worthiness! ? \nIf you're like me, you may\
  \ not have been jumping for joy when you read Google's announcement of its upcoming\
  \ search algorithm cha..."
---

By Adam Henson

Good news - we now have a brand new set of standards by which to judge our search engine's worthiness! ? 

If you're like me, you may not have been jumping for joy when you read [Google's announcement of its upcoming search algorithm change](https://webmasters.googleblog.com/2020/05/evaluating-page-experience.html). But after taking some time to breathe, I believe it's a positive change. 

The announcement emphasizes web page _experience_ and its role in the future of search indexing. By following this new direction, we can not only provide a better experience to website users, but also establish effective strategies to improve SEO.

## What are Web Vitals?

The following metrics encompass Web Vitals as defined at the time of this writing.

* [First Contentful Paint (FCP](https://web.dev/fcp/)) measures the time from when the page starts loading to when any part of the page's content is rendered on the screen.
* [First Input Delay (FID)](https://web.dev/fid/) measures the time from when a user first interacts with a page to the time when the browser is able to respond to that interaction.
* [Largest Contentful Paint (LCP)](https://web.dev/lcp/) metric reports the render time of the largest content element visible within the viewport.
* [Time to First Byte (TTFB)](https://web.dev/time-to-first-byte/) is the time that it takes for a user's browser to receive the first byte of page content.
* [Cumulative Layout Shift (CLS)](https://web.dev/cls/) measures the sum total of all individual _layout shift scores_ for every _unexpected layout shift_ that occurs during the entire lifespan of a page. To calculate the _layout shift score_, the browser looks at the viewport size and the movement of unstable elements in the viewport between two rendered frames.

## Why are Web Vitals Important?

In recent years, [Lighthouse](https://developers.google.com/web/tools/lighthouse), an open-source automated tool for improving the quality of web pages, became widely adopted as an industry standard. 

Now another Google project called [Web Vitals](https://github.com/GoogleChrome/web-vitals) has emerged, deriving metrics from **real users** in a way that accurately matches how they're measured by Chrome and reported to other Google tools. 

With it, we can establish page experience perspective from an SEO point of view, analyze, and adjust accordingly. ?

> Core Web Vitals are the subset of Web Vitals that apply to all web pages, should be measured by all site owners, and will be surfaced across all Google tools. Each of the Core Web Vitals represents a distinct facet of the user experience, is measurable [in the field](https://web.dev/user-centric-performance-metrics/#how-metrics-are-measured), and reflects the real-world experience of a critical [user-centric](https://web.dev/user-centric-performance-metrics/#how-metrics-are-measured) outcome.

%[https://web.dev/vitals/]

## Web Vitals in Google Search Console

Search Console provides reporting of how real users are accessing a website and a variety of data about these users. 

Core Web Vitals are reported as a summary showing the total number of URLs that are good, need improvement, or are just poor. ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-17-at-11.30.00-PM.png)
_Google Search Console Core Web Vitals_

## Sending Web Vitals to Google Analytics and Visualizing in Data Studio

Search Console provides a summary of results in the grand scheme, but in order to get detailed reporting we can take this a step further. The [Web Vitals GitHub project documents a way of capturing metrics as analytics events](https://github.com/GoogleChrome/web-vitals#send-the-results-to-google-analytics) that can be visualized as charts in Google's Data Studio.

Disclaimer: I haven't personally been able to wire analytics Web Vitals events to Data Studio, and the documentation is lacking at this time. But I'll update this post once I can put together an example.

## Visualizing and Analyzing Web Vitals in Real Time with Automated Lighthouse Check

![Image](https://www.freecodecamp.org/news/content/images/2020/06/web-vitals-screenshot-2000.png)
_[Automated Lighthouse Check Web Vitals Demo](https://www.automated-lighthouse-check.com/dashboard/demo/web-vitals)_

Google Analytics and Data Studio are powerful tools that provide great insight. And best of all, they are free! 

Automated Lighthouse Check is a website that monitors websites with Lighthouse and now offers a Web Vitals implementation. You can embed a JS snippet on your website and start collecting Web Vitals metrics in real time. 

One advantage of this tool is its simple setup process and easy filtering. You can [filter data by URL as well as browser, OS, and device](https://www.foo.software/web-vitals).

## Conclusion

The road to SEO success is a winding one, but fortunately we now have a more concrete set of guidelines. If your goal is to achieve high ranking on Google's search engine, it's a good idea to utilize the tools and projects Google recommends including Lighthouse and Web Vitals.


