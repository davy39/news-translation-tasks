---
title: How to Keep a Historical Record of Lighthouse Reports
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T13:02:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-a-historical-record-of-lighthouse-reports
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/lighthouse-logo-in-water-1.png
tags:
- name: Lighthouse
  slug: lighthouse
- name: SEO
  slug: seo
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: web performance
  slug: web-performance
- name: website development,
  slug: website-development
seo_title: null
seo_desc: "By Adam Henson\nLighthouse is an open-source project from the Google Chrome\
  \ team. It's used to analyze web page quality based on a set of modern, \"user-centric\"\
  \ metrics. \nWhen supporting websites that rely on organic search results for revenue,\
  \ qualit..."
---

By Adam Henson

Lighthouse is an open-source project from the Google Chrome team. It's used to analyze web page quality based on a set of modern, "user-centric" metrics. 

When supporting websites that rely on organic search results for revenue, quality is critical. Performance, accessibility and general SEO best practices are major factors in search engine rankings. 

Lighthouse provides a granular set of metrics that represent these factors and suggestions of improvement in reporting. 

There are [many ways of running Lighthouse](https://developers.google.com/web/tools/lighthouse), but in the real world you may want to compare reports regularly, especially in continuous change workflows. With that said, you might be wondering - **how can I keep track of SEO, performance, and accessibility changes over time**?

This post covers how to use [Automated Lighthouse Check](https://www.foo.software/lighthouse) to analyze website quality over time. But keep in mind that there are many other [Lighthouse integrations](https://github.com/GoogleChrome/lighthouse#lighthouse-integrations) to choose from.

## Saving Reports and Viewing Results in a Timeline

[Lighthouse scoring](https://developers.google.com/web/tools/lighthouse/v3/scoring) is an interesting aspect of the tool that may feel a little dirty at first. Still, it can be a very useful point of comparison when looking at historical data. 

The performance category in particular is quite complicated in its calculation of score and you can find a lot of [great reading about the topic among others on web.dev](https://web.dev/performance-scoring/).

Automated Lighthouse Check provides a means of manually triggering audits or establishing a schedule in which they run automatically throughout the day. These audits are saved in a database so you can visualize and analyze results at a historical level. You can actually drill into any report in time to see full details ([see an example here](https://www.foo.software/dashboard/page/5d1d459641e33a002f256efc)).

For a guide to getting started with Automated Lighthouse Check, [see the documentation](https://www.foo.software/automated-lighthouse-check-getting-started/).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/automated-ligthouse-check-timeline.png)
_Timeline view of Lighthouse scores_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-28-at-8.15.32-AM.png)
_A historical list of Lighthouse audits_

## Lighthouse Automation in DevOps

Not only are there many useful cloud-based Lighthouse tools, but there are also many open-source projects that can be implemented in a variety of DevOps workflows. Some of these solutions support persistence of data in one form or another, to track historically. 

Below are a few examples that I've contributed to.

* [This post covers how to use Lighthouse in CircleCI](https://www.freecodecamp.org/news/how-to-use-lighthouse-in-circleci/). You can save reports as "artifacts" in CircleCI or upload to AWS S3 automatically.
* [This post covers how to use Lighthouse in GitHub Actions](https://www.freecodecamp.org/news/how-to-use-lighthouse-in-github-actions/). This solution also provides a way to save reports as "artifacts" (in GitHub) or upload to AWS S3 automatically.
* [Lighthouse Persist is an NPM package](https://www.npmjs.com/package/@foo-software/lighthouse-persist) that exposes the native Lighthouse API with additional options to set AWS S3 credentials so it can be used to upload reports automatically.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screen-Shot-2020-05-28-at-8.34.59-AM.png)
_A few friends - Octocat, Jenkins, CircleCI_

## Conclusion

I hope this post was helpful in providing solutions for analyzing website quality historically. Help support your local developers by purchasing their software ?

But in all seriousness, I'd love any feedback about Automated Lighthouse Check... comments, suggestions, feature requests, etc. It's about a year old at the time of this writing and has recently been migrated to Kubernetes for high availability. 

Automated Lighthouse Check provides [free and premium plans](https://www.foo.software/pricing).

