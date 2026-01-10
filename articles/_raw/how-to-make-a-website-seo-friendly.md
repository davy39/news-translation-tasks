---
title: How to Make a Website SEO-Friendly and Keep it That Way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-20T11:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-website-seo-friendly
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/park-pano.png
tags:
- name: 'Digital Marketing '
  slug: digital-marketing
- name: marketing
  slug: marketing
- name: SEO
  slug: seo
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Adam Henson

  Amidst the economic devastation of COVID-19, online businesses have become dependent
  on SEO now more than ever. Times like these illustrate the power and importance
  of Search Engine Optimization.

  What is SEO?

  SEO is the practice of inc...'
---

By Adam Henson

Amidst the economic devastation of COVID-19, online businesses have become dependent on SEO now more than ever. Times like these illustrate the power and importance of Search Engine Optimization.

### What is SEO?

SEO is the practice of increasing quantity and quality of traffic to a web page through organic search engine results. Organic search results are derived from an internal algorithm of the search engine and not the result of paid advertising. Below is a list of related terminology.

* **SERP** or Search Engine Results Page is simply the results page that drive clicks. These pages include a combination of paid search results and organic.
* **SEM** or Search Engine Marketing is the practice of marketing a business using paid advertisements that appear on SERPs.
* **PPC** stands for pay-per-click, a model of internet marketing in which advertisers pay a fee each time one of their ads is clicked.

Learning SEO basics and more advanced topics can be a bewildering process. In this post we'll take a look at simple steps to help create SEO friendly web pages and tools to maintain them.

## Relevant and Meaningful Content

The most important driver of an SEO friendly website is unique, relevant, and meaningful content. Although this seems obvious, it's easier to mess up than get right. 

A deep understanding of the website's users is crucial in mastering content creation. Content that establishes a strong connection to the user will boost interaction and reduce bounce rate. Search engines recognize time users spend on a website and levels of interaction.

**Don't get too clever**. SEO isn't a card game in which you need to outsmart the opponent. "Over-optimizing" is a term that describes age-old techniques that attempt to trick search engines, like "link stuffing" and "content stuffing" for example. In the past, some tricks were proven effective, but they were ultimately short-lived.

**Keyword strategy** can lead to SEO success when done correctly. Finding the right balance between keyword usage and subject relevance is crucial in achieving this success.

**Variety in content** and format is an effective way to hold attention. A rich set of content including imagery, video, tables and lists will captivate those eyeballs.

**Organizing content** in a logical website hierarchy is another fundamental aspect in creating an SEO friendly website. Google's Search Console Help page "[Search Engine Optimization (SEO) Starter Guide](https://support.google.com/webmasters/answer/7451184?hl=en#hierarchy)" provides an elaborate guide in organizing content.

## Semantic Markup and Structured Data

Well-constructed content is key for SEO along with well constructed code that our browsers and search engines use to interpret content. 

Many HTML tags have semantic meaning that help interpreters understand and classify types of content. As web developers, we sometimes feel powerless in the marketing-heavy world of SEO, but writing **semantic markup** is one of the most impactful tools in our tool belt. 

Why write every HTML element as a `div` when we have a full spectrum of tags to identify different types of content. Below are some of the more useful semantic tags.

* Page titles
* Page descriptions
* Paragraphs
* Lists
* Articles
* Sections
* Headers
* Footers
* Etc, etc

Again, it's important to be clever authoring HTML, but not too clever. A well-balanced sprinkling of shared keywords across titles, descriptions, h1s and h2s can go a long way. Titles and descriptions should be unique between pages and relevant in content.

**Structured data** is a newer data format, following the [JSON-LD specification](https://json-ld.org/), that can be embedded on HTML pages. Search engines like Google interpret structured data to understand the content of the page, as well as to gather information about the web and the world in general as explained in "[Understand how structured data works](https://developers.google.com/search/docs/guides/intro-structured-data)". Below is a simple example.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Foo Software | Website Quality Monitoring",
  "url": "https://www.foo.software",
  "sameAs": [
    "https://www.facebook.com/www.foo.software",
    "https://www.instagram.com/foosoftware/",
    "https://github.com/foo-software",
    "https://www.linkedin.com/company/foo-software"
  ]
}
</script>
```

## Website Accessibility and Performance

Search engines will surely continue to raise the bar for acceptable web standards. [In 2018 Google announced the beginning of its migration to mobile-first indexing](https://webmasters.googleblog.com/2018/03/rolling-out-mobile-first-indexing.html) and expanded by announcing [mobile-first indexing for the whole web in 2020](https://webmasters.googleblog.com/2020/03/announcing-mobile-first-indexing-for.html). Web page performance and accessibility encompass user-centric metrics that can ultimately impact SEO.

**Website performance** captures the user journey, marking various moments of the user experience. Below are important performance metrics.

* **[First contentful paint (FCP)](https://web.dev/fcp/):** measures the time from when the page starts loading to when any part of the page's content is rendered on the screen. 
* **[Largest contentful paint (LCP)](https://web.dev/lcp/):** measures the time from when the page starts loading to when the largest text block or image element is rendered on the screen.
* **[First input delay (FID)](https://web.dev/fid/):** measures the time from when a user first interacts with your site (i.e. when they click a link, tap a button, or use a custom, JavaScript-powered control) to the time when the browser is actually able to respond to that interaction.
* **[Time to Interactive (TTI)](https://web.dev/tti/):** measures the time from when the page starts loading to when it's visually rendered, its initial scripts (if any) have loaded, and it's capable of reliably responding to user input quickly.
* **[Total blocking time (TBT)](https://web.dev/tbt/):** measures the total amount of time between FCP and TTI where the main thread was blocked for long enough to prevent input responsiveness.
* **[Cumulative layout shift (CLS)](https://web.dev/cls/):** measures the cumulative score of all unexpected layout shifts that occur between when the page starts loading and when its [lifecycle state](https://developers.google.com/web/updates/2018/07/page-lifecycle-api) changes to hidden.

**Website accessibility** is another important concept to keep in mind when building a search engine optimized website. Not only are there a variety of humans reading our websites, but also a variety of machines like screen-readers doing the same. 

> Improving accessibility makes your site more useable for everyone. ~ Addy Osami | [Accessibility tips for web developers](https://web.dev/a11y-tips-for-web-dev/)

## SEO Tools

In this post we've taken a look at ways to improve SEO, but how do we maintain these standards over time? Many tools can help us analyze and monitor SEO.

[Foo’s Automated Lighthouse Check](https://www.foo.software/lighthouse) monitors quality of web pages with Lighthouse. It provides detailed SEO, performance, and accessibility reporting. Free and premium plans are available.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/automated-lighthouse-check.png)
_Automated Lighthouse Check dashboard_

[**Google Search Console**](https://search.google.com/search-console/about) is a must have for any website owner who cares about SEO. It provides insight into which search terms are receiving organic traffic and a granular level of analysis. You can filter by location, device and more.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/google-search-console.png)
_Google Search Console performance dashboard_

## Conclusion

SEO is not an easy practice to master, but among the trending tricks of the trade that come and go over time, the most effective approach should come naturally. Meaningful, well formed content combined with well formed code, delivered in a performant, accessible way will surely appease the SEO gods.


