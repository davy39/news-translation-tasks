---
title: How to analyze website performance with Lighthouse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T14:11:19.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-analyze-website-performance-with-lighthouse-8d100966c04b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ydkP__0WxXbUl9Jy8D67DA.jpeg
tags:
- name: 'automation testing '
  slug: automation-testing
- name: Productivity
  slug: productivity
- name: SEO
  slug: seo
- name: 'tech '
  slug: tech
- name: Website performance
  slug: website-performance
seo_title: null
seo_desc: 'By Adam Henson

  Audit website performance manually, programmatically, or automatically


  Cityscape Birds Eye View

  Lighthouse is an open-source project by Google that gives you a way to measure web
  page performance. It has configurable settings for repr...'
---

By Adam Henson

#### Audit website performance manually, programmatically, or automatically

![Image](https://cdn-media-1.freecodecamp.org/images/KZlzVvOb9fZcuBwmwxqRHgrrZyct4MCKNB4X)
_Cityscape Birds Eye View_

Lighthouse is an open-source project by Google that gives you a way to measure web page performance. It has configurable settings for reproducing various conditions. You can set network and device type to simulate, for example.

> You give Lighthouse a URL to audit, it runs a series of audits against the page, and then it generates a report on how well the page did. From there, use the failing audits as indicators on how to improve the page. Each audit has a reference doc explaining why the audit is important, as well as how to fix it. [Lighthouse](https://developers.google.com/web/tools/lighthouse/)

There are many reasons why you’d want to measure performance, but one of the most important is about the impact on SEO. I go into more detail about this and how to address certain metrics in [this article](https://medium.freecodecamp.org/taming-performance-in-todays-web-app-with-lighthouse-webpack-and-react-loadable-components-b2d3fa04e0ab).

### Running Lighthouse with Chrome DevTools

You can run performance audits manually with the [Chrome DevTools browser extension](https://developers.google.com/web/tools/chrome-devtools/). Simply fire up the extension from the web page you’d like to test and select the “Audits” panel.

![Image](https://cdn-media-1.freecodecamp.org/images/CoSD1b8oLEO5ahFg4E4dRazNeo7c5L5y5sHo)
_Chrome DevTools “Audits” Panel_

Among a variety of audits, you can choose “performance”. You can also choose to simulate device type and network throttling. Some information specifically about throttling can be found in the [Lighthouse project Github repo](https://github.com/GoogleChrome/lighthouse/blob/master/docs/throttling.md).

Click on “Run audits” next. Upon completion, Lighthouse provides a report within the extension UI.

![Image](https://cdn-media-1.freecodecamp.org/images/rQqYaIzYRyX4kCF5-V4m7sr0MncTgrI9sJf9)
_Lighthouse Performance Report_

This report is a general overview of important metrics, opportunities, and overall performance score. Thumbnails illustrate the lifecycle of page load. What does this all mean? Google provides a plethora of [documentation describing each metric](https://developers.google.com/web/tools/lighthouse/audits), how to address them and the [overall performance score](https://developers.google.com/web/tools/lighthouse/v3/scoring).

In the top left side of Chrome DevTools panel is a download icon that you can use to download the full report in JSON format. You can then use it to create a PDF report via [Lighthouse Report Viewer](https://github.com/GoogleChrome/lighthouse#using-the-node-cli).

Due to the high volume of factors playing into the lifecycle of page load, it’s important to compare results in batches. Taking an average of 5 runs, for example, will provide better insight.

### Running Lighthouse Programmatically

For our standard “run of the mill” situations, the above should suffice. Another way to run Lighthouse involves installing the open-source package via NPM and following the instructions in the [CLI documentation](https://github.com/GoogleChrome/lighthouse#using-the-node-cli). This can be beneficial if you want to run audits programmatically in a build pipeline, for example.

Similar to the above, you can also run Lighthouse in code by following the [documentation for using the Node module programmatically](https://github.com/GoogleChrome/lighthouse/blob/master/docs/readme.md#using-programmatically). You could create a full-fledged Node.js application with Lighthouse ?!

### Running Lighthouse Automatically Over Time

So now that we’re pros — let’s take this to the next level. There are many [integrations listed in the Lighthouse documentation](https://github.com/GoogleChrome/lighthouse#lighthouse-integrations), so let’s take a look at one of them.

#### Using “Foo” to Run Lighthouse and Compare Results Over Time

In an engineering setting where many developers are deploying application changes on a regular basis, it can be important to monitor website performance over time to associate change sets with performance degradation or improvement. Another example would be teams that have initiatives to improve performance for SEO ranking or other reasons. In these situations, it’s critical to monitor website performance over days, weeks, months, etc.

You can add URLs to track at [www.foo.software](https://www.foo.software) and monitor performance change. Foo also provides email, Slack or PagerDuty notifications when performance has dropped below a threshold defined by the user, when it’s back to normal, and when improvements are identified automatically!

The best part about it is that you can [create an account for free](https://www.foo.software/register)! Once registered and logged in, click the “Pages” link from the top navigation. This is where you can add URLs to monitor. Foo saves results and displays a timeline chart providing a visualization of important metrics. You can toggle through days, weeks, months and drill into detailed reports.

![Image](https://cdn-media-1.freecodecamp.org/images/aMrCtx3sHKfiNW4UbN32f5y7WwUejkJqEKYg)
_Amazon Example Foo Lighthouse Timeline Chart_

### Conclusion

Lighthouse is becoming an industry standard in website performance measurement. There are books worth [documentation about Lighthouse that provides details of important metrics](https://developers.google.com/web/tools/lighthouse/).

