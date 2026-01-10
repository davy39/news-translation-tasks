---
title: What is website accessibility?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-13T14:27:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-website-accessibility-18ce00ec990f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Kg9Y-FRAW_9UK6X0sJE-pg.jpeg
tags:
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ben Robertson

  Web accessibility is getting a lot of attention these days, but it can be intimidating.
  Here’s a simple introduction to web accessibility: what it is, why it’s important,
  and the benefits that come along with accessibility.

  At the mo...'
---

By Ben Robertson

Web accessibility is getting a lot of attention these days, but it can be intimidating. Here’s a simple introduction to web accessibility: what it is, why it’s important, and the benefits that come along with accessibility.

At the most basic level, web accessibility means building websites that are usable by as many people as possible.

In the US alone, 57 million people report having a disability. That’s one in every five people — equivalent to the entire populations of New York and California combined. And around 30 million of those people report having a _severe_ disability.

How can web developers make sure their sites are accessible to as many users as possible?

#### What makes a site inaccessible?

There are many ways that users might find a website to be inaccessible.

Some people may not be able to use a mouse. They may need to be able to scroll, click, navigate and [interact with all parts of a website using only a keyboard](https://benrobertson.io/accessibility/javascript-accessibility#2-plan-for-common-keyboard-interactions) or other device.

Others may have some form of color-blindness, so may have difficulty discerning links and buttons from other text content.

Dyslexia can cause some people to struggle to understand the content of a site.

For people with severe visual impairments, it is necessary for all content and interactivity on a page to be [understandable to a screen reader](https://benrobertson.io/accessibility/understanding-layout-for-screen-readers). This is a program that reads the contents of a webpage to the user and lets them interact with the page.

There are even machines that will provide braille output from webpages.

#### Accessibility is a Web Standard

I’ve barely scratched the surface of the accessibility challenges people can face on the web. It is impossible for the average web team to keep up with all these different situations that can prevent people from using and enjoying websites.

That is why the [World Wide Web Consortium](https://www.w3.org/) first drafted [standards for developing accessible websites](https://www.w3.org/TR/WCAG10/) back in 1999.

This set of standards makes it easier for development teams to ensure their work is accessible to all. These standards are what you may have heard referenced as WCAG (sometimes pronounced wee-kag). It stands for [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG20/).

These guidelines provide a detailed look at common patterns and areas that can cause usability issues in different situations. At a higher level though, they outline the four broad guidelines of web accessibility:

* **Perceivable:** can all people perceive the content on the page?
* **Operable:** can all people interact with the page?
* **Understandable:** can all people understand the content on the page?
* **Robust:** can the content be interpreted by a wide variety of programs and devices, including screen readers?

While these guidelines have been around for a long time, stakeholders at all levels of web projects often aren’t aware of their existence. Or perhaps they don’t believe it is a concern for their organization.

Let’s look at some of the benefits of web accessibility to see why these guidelines are important.

### What are the benefits of web accessibility?

#### Inclusivity

The first benefit of accessibility is inclusivity. When you approach accessibility from the perspective of making a website user-friendly to as many people as possible — well that’s the definition of inclusive isn’t it?

The great thing about following the web accessibility guidelines is that by following them, you provide a better web experience for _all users_.

Consider the [reading level guidelines](https://www.w3.org/TR/UNDERSTANDING-WCAG20/meaning-supplements.html), for example. While these guidelines are intended to make sure people with reading disabilities can understand a website, when implemented they also end up helping people with low literacy or who are not fluent in our language understand our website more easily.

#### SEO Benefits

A second benefit of prioritizing accessibility is improved search engine optimization (SEO).

The same practices that ensure content is understandable to screen readers also benefits the robots that index websites for Google and other search engines.

Many accessibility guidelines focus on providing text-based alternatives to content that is available in video or audio. This allows this content to be visible to both screen readers and search engines.

The guidelines also encourage the use of proper page organization to help users best understand the layout and content of a page. This also helps search engines understand the content of a page better.

Making your web content easier for people to understand will make it easier for Google’s robots to understand as well.

#### Usability Benefits

There are also usability benefits to prioritizing accessibility.

All of us at some point have encountered a website that was unusable. Sometimes text doesn’t have enough contrast with its background, or buttons are too small to easily use on our smartphones.

Focusing on web accessibility can help eliminate basic issues like these. By following the guidelines, we can make sure our site is as usable on mobile devices as it is on larger screens, for everybody.

Additionally, by paying attention to the “**robust**” principle of accessibility and making sure content can be interpreted by a wide variety of programs and devices, we will help people who may be using older technologies or have low bandwidth have access to a web site.

Organizations that prioritize accessibility will not only develop goodwill with their users, but will also ensure they can serve closer to 100% of the marketplace. And they will protect themselves against losing the ability to serve their customers as they age.

### What are the legal requirements for website accessibility?

Besides the benefits following accessibility guidelines can bring, there can also legal requirements to consider.

Accessibility issues have come to the forefront due to a series of lawsuits filed under [Title III](https://www.ada.gov/regs2010/2010ADAStandards/2010ADAstandards.htm) of the Americans with Disabilities Act (ADA). This requires public spaces and commercial facilities to be designed and built so that users with disabilities can enjoy equal access to these facilities.

While the law was originally written with physical spaces in mind, the prevalence of web-based activities including shopping and education has brought inaccessible web experiences under scrutiny as well.

Notably, a [federal judge ruled in June 2017](https://www.forbes.com/sites/legalnewsline/2017/06/13/first-of-its-kind-trial-goes-plaintiffs-way-winn-dixie-must-update-website-for-the-blind/) that Winn-Dixie’s web properties were so integrated into their physical locations that they were subject to Title III of the ADA. The judge ruled in favor of a blind man who filed the suit, requiring Winn-Dixie to update their site to meet the Web Content Accessibility Standards and perform annual audits to ensure they continue to meet these standards. ([The courts full 13 page order is available here](http://www.adatitleiii.com/wp-content/uploads/sites/121/2017/06/16-cv-23020-63-Verdict-Order_WinnDixie.pdf)).

Furthermore, the sheer number of web accessibility-related lawsuits has skyrocketed. The Seyfarth Shaw law firm [reports](https://www.adatitleiii.com/2017/08/website-accessibility-lawsuit-filings-still-going-strong/) that there were approximately 57 federal web-accessibility related lawsuits filed in 2015, 262 in 2016, and 432 between January and August of 2017 alone. Beyond that, the US Department of Education has recently opened [350 web accessibility investigations](http://legalnewsline.com/stories/510738182-department-of-education-increases-investigations-into-website-compliance-with-ada).

### Conclusion

The good news is that there are clear guidelines for developers, product managers, designers, and content editors to follow for developing and maintaining accessible websites.

With good planning, execution, and accountability, an accessible website is an attainable goal for every organization. By being proactive, organizations that embrace an accessibility-first approach will be able to generate goodwill with their customers, stay within relevant legal requirements, and serve a larger market.

_Want to dive into the details of building accessible websites? Join my free email course:_ ? C[_ommon accessibility mistakes and how to avoid them._](https://benrobertson.io/courses/common-accessibility-mistakes/) _30 days, 10 lessons, 100% fun!_ ? Si[_gn up here!_](https://benrobertson.io/courses/common-accessibility-mistakes/) 

_Originally published at [benrobertson.io](https://benrobertson.io/accessibility/what-is-website-accessibility)._

