---
title: How to Make Sense of Google Analytics and the Traffic to Your Website
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-09-04T14:32:00.000Z'
originalURL: https://freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/making-sense-of-google-analytics.jpg
tags:
- name: analytics
  slug: analytics
- name: Google Analytics
  slug: google-analytics
- name: '#reporting'
  slug: reporting
- name: SEO
  slug: seo
- name: user experience
  slug: user-experience
- name: website development,
  slug: website-development
seo_title: null
seo_desc: 'Google Analytics is a powerful web service that gives you insights into
  your website. But exactly can it help you?

  I’m going to cover a few things here. If you’re already familiar with the basics,
  feel free to skip around:


  What is Google Analytics? ...'
---

[Google Analytics](https://marketingplatform.google.com/about/analytics/) is a powerful web service that gives you insights into your website. But exactly can it help _you_?

I’m going to cover a few things here. If you’re already familiar with the basics, feel free to skip around:

* [What is Google Analytics?](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/#what-is-google-analytics) (A quick overview)
* [Okay, so where do I start?](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/#okay-so-where-do-i-start) (Quick start install guide)
* [What are some quick insights?](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/#what-are-some-quick-insights) (Basic out of the box reports)
* [Bonus: Advanced Insights](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/#bonus-advanced-insights) (Custom Dimensions)

So let’s start from the top.

## **What is Google Analytics?**

> Google Analytics gives you the tools you need to better understand your customers. You can then use those business insights to take action, such as improving your website, creating tailored audience lists, and more. - [Google's official documentation](https://marketingplatform.google.com/about/analytics/)

More simply put, Google Analytics (GA) is a web analytics service provided by Google on the [Google Marketing Platform](https://marketingplatform.google.com/about/). It allows you to track and measure your website’s traffic with powerful insights and reports.

GA can work a few different ways, but the most common is [using a quick drop-in JavaScript snippet](https://support.google.com/analytics/answer/1008080?hl=en) that goes on every page of your website (typically the `<head>`).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-37.png)
_Google Analytics lets you measure user interaction with websites._

The base version of Google Analytics is free. You have the option of upgrading to the 360 suite, which will open up some feature limits, but most of you probably don’t need this as it is more geared towards high traffic websites.

### **Why do I need Google Analytics?**

You don’t _need_ it. But you can get an incredible amount of insight from GA with even a basic out of the box setup. 

GA is helpful if you're a developer trying to get more traffic out of your blog, or a business trying to optimize your sales funnel. 

GA helps you answer simple questions like:

* Where is my traffic coming from?
* What pages get the most traffic?
* What are the most popular devices people visit on?

Not only can this help you make better-educated decisions with your website. It can also help you unveil user experience concerns, or save money due to site issues by keeping an eye on traffic trends and user interactions.

## **Okay, so where do I start?**

Google makes it’s fairly easy for any developer to jump in and get started. The only real prerequisite is that you set up an account. Google themselves offers a great [step-by-step and constantly updated guide](https://support.google.com/analytics/answer/1008015?hl=en), so I’ll leave it to them.

### **Getting the tag on your page**

Once you’re logged into the Google Analytics Dashboard, go to the Admin section, which you can find on the left hand side of the page:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-42.png)
_Admin link in the Google Analytics Dashboard_

Once in the admin section, you can navigate to Tracking Info then Tracking code under the property you want to track.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-43.png)
_Tracking code link in the Google Analytics Admin_

Finally, you can find the JavaScript snippet that you can throw in the head of your website. Remember, this should be on ALL pages.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-44.png)
_Google Analytic tracking code snippet_

### **Let the traffic flow**

From here you just have to give it time. Google Analytics won’t have historical data, it will only have the the new traffic that hit your page once the snippet was installed. 

You can check it’s working by visiting the Realtime Report and either hitting the page in another tab or seeing your visitors hit the page.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-45.png)
_Google Analytics Realtime Report_

### **More settings, more configuration**

Google Analytics is a complex machine and can do a lot. Start slow and try to understand what’s happening before moving too fast turning every different switch. 

Once you're comfortable, there are a lot of [great guides out there](https://www.google.com/search?q=google+analytics+tips) for beginners and advanced users alike to unleash the full power of your reporting capabilities.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/super-saiyan.gif)
_Goku going Super Saiyan_

## **What are some quick insights?**

Cool, so you have GA installed, you see your traffic, and you’re ready to get started looking at your reports, but where to begin?

### **What pages get the most traffic?**

Let’s start with a simple one. Which pages of my website are getting the most traffic? To find this out we’ll want to view the Behavior Overview, which we can find by visiting Behavior then Overview.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-46.png)
_Finding top page on Google Analytics Behavior Overview Report_

Above we’re looking at the full month of August, which you can change with the date picker in the top right of the report. We can see overall, we had 3,853,265 total pageviews and 121,187 of them were to /news, the freeCodeCamp News homepage, which was our most popular page of the month.

### **Where is my traffic coming from?**

A common question is: “where are people coming from?” How are people actually finding my website? This is a 2 parter, let’s start with overall traffic.

A good way to start is by finding the Acquisition Overview page. You can navigate there by selecting Acquisition than Overview.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-47.png)
_Finding top traffic source on Google Analytics Acquisition Overview Report_

Shown above, the majority of traffic comes from organic searches on Google, a little over 75% in fact. That’s some good [SEO](https://moz.com/beginners-guide-to-seo)!

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-48.png)
_Outstanding Move_

But what if we wanted to see how people are getting to a particular post? This involves a little more work, but let’s dive in.

Let’s go back to Behavior in the sidebar, then Site Content, and finally Landing Pages. Once there, you can use the search to find your post as shown below and select it.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-49.png)
_Searching for a page on the Google Analytics Landing Page Report_

After you found your post, we’re going to add a Secondary dimension. In particular, we’ll want to find and select “Source / Medium” in the Secondary dimension dropdown.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-50.png)
_Adding a Secondary dimension on the Google Analytics Landing Page Report_

Finally we’ll have an idea of where people are coming from to visit our post.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-51.png)
_Finding the top Source / Medium on the Google Analytics Landing Page Report_

It seems like this is following the trend of great Organic SEO. If you notice though, we have “(direct) / (none)” as the second highest source / medium. 

Unfortunately, it’s not always that easy. And if Google Analytics can’t figure out where the user came from, it will mark it as “(direct) / (none)”. [While that’s solvable](https://moz.com/blog/guide-to-direct-traffic-google-analytics), and sometimes actually means something, we can see the majority comes from simple searches on Google itself.

### **What are the most popular devices people visit on?**

Understanding what devices your visitors are using is an incredibly helpful tool for optimizing User Experience, as well as maximizing potential revenue by making sure your site works. 

In a perfect world, your website would work in all browsers. But we may be able to safely rule out certain older browsers.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-52.png)
_Internet Explorer behind a tree_

To get started, find your way to Audience then Overview. Once there, select Browsers in the list as shown below.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-53.png)
_Finding the top browser in the Google Analytics Acquisition Report_

We can see that luckily, our top browsers are dominated by modern ones, with Chrome carrying a cool 76.42%. 

But wait, Internet Explorer is pulling 1.06% or 22,499, which isn’t something to bat an eye at. So let’s dig in a little more by clicking on Internet Explorer.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-54.png)
_Finding the traffic for Internet Explorer versions in the Google Analytics Acquisition Browser Report_

Phew, I think we’re safe. Now we can see how many people visit each version of Internet Explorer and luckily almost 99% of THAT traffic is IE9 or above. While we should be as inclusive as we can, this can help us determine priority and make decisions on [what browser versions to officially support](https://caniuse.com/).

Real talk: 5 people on IE5? ?

## **Bonus: Advanced Insights**

Out of the box, Google Analytics is powerful, but with some customization and deeper integration with your web data, you can give your analytics dashboard extra superpowers.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/darkwing-duck-lets-get-dangerous.gif)
_Darkwing Duck Let's Get Dangerous_

## **Custom Dimensions**

[Custom Dimensions](https://support.google.com/analytics/answer/2709829?hl=en) are what Google specifies as “non-standard data.” Really, they’re just additional data points that we can configure to get a better understanding of what makes our website unique.

For the sake of this article (maybe a later one), I’m not going to go into how to add Custom Dimensions, but Google provides a [great guide to get an in depth understanding](https://support.google.com/analytics/answer/2709828?hl=en) and a [developer guide to go with it](https://developers.google.com/analytics/devguides/collection/analyticsjs/custom-dims-mets). What I’ll go over here is how to explore our reports once some Custom Dimensions are already set up.

### **What are our Custom Dimensions?**

To start, we’ll talk about 2 specific Custom Dimensions: Author and Page Category. 

Author is what it sounds like, it’s the person who wrote the article. Page Category in our case is the primary, top-level category that represents the post. 

On freeCodeCamp News, you can specify as many categories as you want (do so responsibly), but the first one in the list is consider your “primary” category and is used when you see your post in listing views such as the homepage.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-55.png)
_Post on freeCodeCamp News Homepage_

### **What can we do with these?**

The great thing is when we set these up, we attribute them to a page view. Once that page view is collected by Google Analytics, we can use it to search on, which is really what makes it powerful. Let’s start with Author.

### **Finding all posts from a specific Author**

If we wanted to search for any post written by Quincy Larson, we’ll want to navigate back to **Behavior**, then **Site Content**, and finally **All Pages**.

Once there, we’ll want to add a **Secondary dimension**, similar when we added Source / medium, but now we’ll want to search for and select **Author**, which you’ll also find nested under the Custom Dimensions heading of that dropdown.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-56.png)
_Selecting Author as a Secondary dimension on the Google Analytics Behavior Report_

From there, we’ll want to select Advanced on the right (highlighted below), add our author’s name, and finally hit the Apply button.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-57.png)
_Searching for an Author in Advanced Search of Google Analytics Behavior Report_

After hitting apply, we now have all the stats we could ever dream of for the articles written by our author, Quincy Larson.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-58.png)
_All posts from an Author in Google Analytics Behavior Report_

### You can also just type a query into the Google Analytics Search Bar.

Google Analytics has a search bar at the top, and you can just type natural language queries like this one:

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Analytics.png)
_The results of a query for "articles by quincy larson past 30 days" shows the number of views each of Quincy's articles has gotten over the past 30 days._

### **Which categories are doing the best?**

This is a trickier one. There are a lot of questions we may be able to answer with the basic reports like we did with Author, such as “out of all of the JavaScript posts, what has the most traffic?”, but maybe we want to know generally what category is the most popular on the site.

To do this we need to get our hands dirty with Custom Reports. This is too advanced to try to tackle in this post, but [Google does a great job at outlining it in detail](https://support.google.com/analytics/answer/1151300?hl=en).

For now, I’ve done you a favor and set up a report that you can easily import to your account and use right away. So first thing’s first, let’s import the report: [https://analytics.google.com/analytics/web/template?uid=4fHol2S_TZqcQACAwfcmfg](https://analytics.google.com/analytics/web/template?uid=4fHol2S_TZqcQACAwfcmfg)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-59.png)
_Importing a Custom Report in Google Analytics_

Here you should see a screen like the above that asks us 2 things: where should we apply the report and what do we want to call it? If you’re an author of freecodecamp.org with access to GA and want to view this, you would select the All Web Site Data view under the freeCodeCamp News property.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-60.png)
_Selecting a Property and View when importing a Custom Report in Google Analytics_

Once selected, name the report what you’d like, such as “Top Primary Categories”, and click Create.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-61.png)
_Custom Report showing top Primary Categories in Google Analytics_

After it’s done, you’ll then land on the newly imported custom report where you can immediately see the most popular categories on the site, which for August is JavaScript!

## **Breakdown**

This was a lot!

![Image](https://www.freecodecamp.org/news/content/images/2019/09/galaxy-quest-alan-rickman-tired.gif)
_Alan Rickman in Galaxy Quest sinking in chair_

But this is just the tip of the data iceberg. Even with just the above, you can see there’s a lot going on and a lot of configuration to make the most out of Google Analytics for your specific needs.

If this interests you, I encourage you to do some research on your own, [add a new view](https://support.google.com/analytics/answer/1009714?hl=en) (particularly [a Test View](https://www.e-nor.com/blog/google-analytics/best-practices-views-google-analytics) to play around with), and get your hands dirty poking around the different reports. Otherwise, keep an eye out for more of my GA posts covering advanced installation and deeper insights.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

_Originally published at [https://www.colbyfayock.com/2019/09/making-sense-of-google-analytics-and-the-traffic-to-your-website](https://www.colbyfayock.com/2019/09/making-sense-of-google-analytics-and-the-traffic-to-your-website)_

