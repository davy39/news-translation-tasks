---
title: How Mozilla takes care of Firefox’s health — and what you can learn from it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T21:55:03.000Z'
originalURL: https://freecodecamp.org/news/here-is-how-we-take-care-of-firefox-health-at-mozilla-8f7f9b085955
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3orZX4NPEQbwNxUgz7Wm4Q.jpeg
tags:
- name: Firefox
  slug: firefox
- name: internships
  slug: internships
- name: Mozilla
  slug: mozilla
- name: open source
  slug: open-source
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Syeda Aimen Batool

  Currently, I’m working on a Firefox health dashboard as a part of my Outreachy internship
  with Mozilla. And here are the major goals we intend to achieve during the internship.


  Add new features to the graphical presentation of ...'
---

By Syeda Aimen Batool

Currently, I’m working on a [Firefox health dashboard](https://github.com/mozilla-frontend-infra/firefox-health-dashboard) as a part of my [Outreachy internship with Mozilla](https://medium.freecodecamp.org/how-i-got-a-remote-paid-internship-at-mozilla-through-outreachy-60958fe9264a). And here are the [major goals](https://github.com/mozilla-frontend-infra/firefox-health-dashboard/projects/2) we intend to achieve during the internship.

* Add new features to the graphical presentation of performance data
* Transfer existing JS Team (Firefox Performance) dashboard to the health dashboard
* Enhance existing information on charts and fix some bugs

The main purpose of this post is to explain the project to someone who is not in the community and not familiar with the stuff we are doing at Mozilla. The intention is to help newbies and other contributors to understand the dashboard so they can contribute to this opensource project with more sense of what is going on inside.

![Image](https://cdn-media-1.freecodecamp.org/images/Amkrf0TIX5AYgBBaD9bSbFGQg0eL7mVGCdrr)
_Photo by [Unsplash](https://unsplash.com/photos/0-SGyQFiDRI?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel</a> on <a href="https://unsplash.com/search/photos/health?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### What is Firefox Health Dashboard?

Firefox health is a project to create dashboards for project managers and engineers. It displays Firefox matrics and insights to help meet release criteria. It allows including data/metrics from Mozilla’s issue tracker (Bugzilla), performance data (Perfherder), product metrics (Telemetry) and few more sources. All data is displayed in the form of graphs using an open source graphing library ChartJS to display insights against different dates and platforms.

It was previously known as Platform Health. It was [refactored in Jan 2018](https://github.com/mozilla-frontend-infra/firefox-health-dashboard/issues/29) as Firefox Health Dashboard. One of the major changes in this refactorization was to separate backend from the front-end. This improved code maintainability.

#### Technologies:

The [backend](https://github.com/mozilla/firefox-health-backend) is written using NodeJS and Koa. The [front-end](https://github.com/mozilla-frontend-infra/firefox-health-dashboard) is built using ReactJS along with an open source graphing library ChartJS. Some of the data is coming from different hosts through different libraries. For example, perf-google is querying Mozilla’s Perfherder for performance data. Information about the reported bug is coming from Bugzilla. So if you are planning to contribute sometime in the future, you need to have an understanding of the technologies mentioned above.

This dashboard caters to performance of different Firefox versions and devices. But today we are going to talk about [Firefox android](https://health.graphics/android) and how engineers at Mozilla take care of its performance.

### Data/metrics for Firefox android

Currently, data for Firefox android is coming from different sources. We display the data in the form of graphs for better understanding and analysis. You can see all insights to [Firefox android on the health dashboard](https://health.graphics/android). Here are some sources and information about Firefox android to help engineers improve the performance of the browser.

#### Bugzilla:

Developed by Mozilla, Bugzilla is a free, open-source tool for tracking bugs, issues and change requests in large complex applications. It is used by thousands of organizations to keep track of their product performance. We are using it in the Health Dashboard to keep an eye on the bugs popping up in Firefox Android.

![Image](https://cdn-media-1.freecodecamp.org/images/dKEOkAJGbvDDvS3M-pUPMS8GvHtasek7oJ1D)
_A graph displaying bugs from Bugzilla_

As mentioned above, we are using ChartJS to display data. Here we have a graph representing the number of bugs reported on different dates for Firefox Android at Bugzilla. Bugs with P1 label have the highest priority. They need to be fixed as soon as possible. Then comes P2 bugs with the 2nd highest priority. P3 level bugs are with lowest priority and engineers can fix them whenever they have time. This helps developers and product managers to review bugs of different priorities more effectively and solve them according to the priority.

#### NimbleDroid:

We are using a third party service called NimbleDroid to get some data insights after running the tests against Firefox Android. NimbleDroid is a functional performance testing service for android and IOS devices.

> Monitor every critical user flow for every build of your mobile app. Pinpoint issues that degrade user experience early in the dev cycle. Seamlessly integrate with your CI workflow. — Official Site

![Image](https://cdn-media-1.freecodecamp.org/images/QtqHkLwQwTP0szF2tkiNZyvA-HWLQ1Sl7jkP)
_Showing data insights given by Nimbledroid_

#### Telemetry:

Telemetry is a tool that has the capability to provide performance and usage information to Mozilla to help engineers and decision makers to measure the performance of Firefox in the real world. It has the ability to collect performance, hardware, usage, customization, and other non-personal information from the user of Firefox and send it to Mozilla on daily bases to help engineers improve the quality and efficiency of the browser.

![Image](https://cdn-media-1.freecodecamp.org/images/xshtOGlnr9LFHhteDt7yxJFkOif5bD80akVO)
_Telemetry graph view_

For an Android device, the browser measures the time taken by it to load a content page on a device and reports it back through Telemetry. We then display it in graphical form. For instance, the screenshot says 75% of the users reported a total content page load time of 4.9 seconds on Sep 19, 2018. And this data is gathered from different devices from different users. This helps the engineers to keep an eye on loading time of the browser to improve its speed and make it more efficient.

#### Perfherder:

Perfherder is a system to help engineers visualize and analyze the performance data produced by the many automated tests run against Mozilla products such as Firefox or Firefox Android. Perfherder is a part of Treeherder project. It is another dashboard for check-ins to Mozilla’s projects. The main goal of this tool is to make sure that the performance of the Firefox gets better over the time. It assists developers in the understanding of their changes and potential fixes by reporting regressions.

In the coming articles, we will talk about Firefox Quantum and JS team dashboard. We will see how these tools are working to improve the performance of the Firefox browser.

#### Contribution guide:

If you care about the health of Firefox or interested in contributing to the project, then here is the way.

* Clone and set up the [project](https://github.com/mozilla-frontend-infra/firefox-health-dashboard) on your local machine
* Follow the [readme](https://github.com/mozilla-frontend-infra/firefox-health-dashboard#firefox-health-dashboard)
* And start with [good-first-issues](https://github.com/mozilla-frontend-infra/firefox-health-dashboard/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) if you are finding it overwhelming to start

Stay tuned to know more about the awesomeness we are doing at Mozilla.

