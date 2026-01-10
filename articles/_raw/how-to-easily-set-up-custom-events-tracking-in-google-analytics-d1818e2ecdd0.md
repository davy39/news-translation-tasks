---
title: How to easily set up custom events tracking in Google Analytics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T17:41:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-set-up-custom-events-tracking-in-google-analytics-d1818e2ecdd0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FnDrSxZXNERxjYqpHoM1mA.jpeg
tags:
- name: data analysis
  slug: data-analysis
- name: Google Analytics
  slug: google-analytics
- name: marketing
  slug: marketing
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pankaj Singh

  The Growing need for Custom Event Tracking

  I am a technologist-turned-analytics professional since five-plus years. Recently,
  a friend asked me how he can set up a custom event tracking on his small business
  website and understand his...'
---

By Pankaj Singh

### **The Growing need for Custom Event Tracking**

I am a technologist-turned-analytics professional since five-plus years. Recently, a friend asked me how he can set up a custom event tracking on his small business website and understand his site’s user behavior better.

Until a few years back small businesses and personal bloggers were satisfied knowing their number of unique visitors and page views on their website. But everyone now wants to understand much more than mere page views. They want to know how many users clicked on different buttons, watched a video, checked details of a product, or clicked on third-party advertisements among other things. There’s an increasing demand to understand how different users are engaging on their digital assets.

There are many objectives you can use your website for, and there are as many activities to monitor on a website. While big businesses have dedicated teams, small companies usually have a single person managing both the analysis and the technical setup of their analytics account.

> "Thankfully setting up basic goals and even the advance custom goals in google analytics isn’t difficult, as long as you know the right steps. And in this article we are going to go through exactly that. I’ll walk you through the steps of setting up custom goals in the simplest way while you enjoy your coffee!" - Google's documentation

## Overview

First, for the sake of revision, let’s go over the four main types of custom goals available in your Google Analytics account. If you are already familiar with them and want to understand only the last one (the “Event” goal type), then scroll down to point 4: “Setting up an Event goal”. A glance at the screenshot below will explain to you the four main goals that you can customize in Google Analytics.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_jVaB9r6Kdv_fxeObzUeKXg.png)
_The 4 Custom Goal Types in Your GA Goal Settings_

You’ll notice that the first 3 goals are very intuitive and directly usable. Once set, they will give you an x% conversion in the past 7 days. But the last one will return a 0% conversion. Let’s first review the three simpler goals and then we’ll be able to understand the event goal in detail.

## **1. Setting a Destination Goal**

All you need for this is to give the URL of the page which you identify as a success on a page visit. For example in e-commerce websites, when a person makes a purchase and reaches a “thank-you” page, it’s a success. So visiting the thank-you page can be a goal.

All you need to do is enter the URL of that page as a destination, _www.yourexamplesite.com/thanks.html_. It’s possible that your website may have different query parameters, so you can use options like “URL Begins with”, “URL Ends with” or “Regex”.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_ijl4io4cmLAvEf1cSOOLiw.png)
_Defining a ‘Destination’ Goal in Google Analytics_

## **2. Setting a Duration Goal**

This refers to the number of minutes (or hours) spent on your website by a user. This goal’s use can vary based on the purpose of a website. Spending more time on your site may be desirable, but it doesn’t mean a sure shot conversion. It can also mean that your website is not easy enough to help users accomplish their tasks quickly.

However, for content-oriented websites such as that of newspapers, bloggers, magazines or video content, a duration goal can be important. So based on your site’s purpose, it might be a good idea to set different time duration goals.

As you can see below, you can enter a time duration for this goal and you’ll be set to track all users who cross that mark.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_oTaECRqhsaVI8eL1P0Y6_Q.png)
_Defining ‘Duration’ goal in Google Analytics_

## **3. Pages/screens per session**

This is the number of pages viewed in a single session or visit. If a visitor closes the website and then returns the next day, or after a gap of 30 minutes on the same day, it’s called a new session.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_LCkKm70Q-_vwKR3gOEpAMQ.png)
_Defining ‘Page Per Session’ in Google Analytics_

## **4. Setting a Custom Event Goal Type**

An ‘event’ is any action taken by a user that marks an interaction with your website after landing on any of its pages. The simplest example is when they click on a button like “Buy Now”, or “Learn More”. It can also be used for options like downloading a PDF or E-book, among other actions.

Clicking on a button is typically referred to as a CTA, short for “Call to Action”. When you choose this option in your custom goals setting, you’ll see this window open up with four options:

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_A0292cpFgkeBgN_nJb2g5Q.png)
_Setting Fields for Google Analytics “Event’ Goal_

All four fields or parameters are simple to enter. GA needs you to define each event with these four fields so that you can easily identify them during analysis.

> _"__You can write anything in these parameters, but it’s recommended that you define them in a way that makes the most business sense for you.__" - Google's documentation_

For example, if you are managing a store selling electronic gadgets and accessories, you may want to fill it like this :

**A. Category:** Category of the product. Example, ‘Headphones’

**B. Action:** Let’s say a user clicked the ‘Add To Cart’ button. Then you could write ‘AddToCartClick’ in your action. In case you have an additional button for ‘Features’ or ‘Learn More’ for that product, you can have an additional goal and define its action as ‘LearnMoreClick’ for that button.

**C. Label**: Label can be anything which helps you recognize or group your events better during your analysis. It can be the name of a ‘Campaign’ or a ‘Brand’. For example, ‘CollegeCampaignSonic’.

**D. Value:** This is an optional value, mostly used to set a revenue number. It can be used to set a specific number like $50, or to take a dynamic value from the revenue variable of your page, like $(“PriceVariable”). Note that $ here is a jquery identifier and not the currency dollar. Picking up an ID would depend on the price or cost variable defined in your HTML.

> "After you define your Event goal type values here, the tricky part starts. Since every other goal in GA is directly usable once defined, it’s confusing to many why the event goal doesn’t start to work right away. That’s why when you click on ‘Verify the conversion’ for this goal, you see a 0% conversion." - Google's documentation

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_CBDM9KgwzQY-5FwcaLtWQQ.png)
_Event goal is not directly usable after configuration_

To correct this 0% conversion, you need to integrate the settings of this goal with the actual click event or the custom action responsible on your website, for this goal.

# **Integrating custom event tracking with the HTML of your website**

Sometimes, business users (especially non-technical ones) tend to feel anxious when anything related to coding comes up while doing their analysis. Thankfully Google has made it very simple to tie any custom event tracking need that needs to be integrated with your website. Only if you’re managing a complex e-commerce website would you need help from a developer, which in most cases you would have access to if you are working in a mid-size company.

For integration, Google has already set up a standard template function that it expects you to use when tracking a custom event on your page. It’s one line of code, for which you have already set values in your GA account. Marketers or coders typically refer it to as the GA-Send call which is in the below format:

```
ga(‘send’, ‘event’, [eventCategory], [eventAction], [eventLabel], [eventValue]);

```

The actual JS function in your HTML page may be in single line or may look like this for easy readability:

```
ga('send', {
  hitType: 'event',
  eventCategory: ‘Headphones',
  eventAction: ‘AddToCartClick',
  eventLabel: ‘CollegeCampaignSony'
});
```

Note that the values in this function must match the values entered in your GA account while setting up the event for its respective parameters. **Now you still need to tie the above GA send call with the actual action on the button_._**

For example, you want to tie the above function with the click on the ‘Add To Cart’ button. The only step you would need to add is to include this function on the ‘onClick’ action event for that button ID.

```
Integrating the above cited Google Analytics Event script inside your HTML
<script>
$(document).ready(function(){
  $("#exampleAddNowButtonID").click(function(){
    ga ('send', 'event', 'Headphones' , 'AddToCartClick' , 'CollegeCampaignSonic');
  });
});
</script>
```

# Wrapping up

This brings me to the end of this article. I have tried to explain with simplicity and details that I felt lacking when I was learning how to set up custom tracking for my own requirements. Hopefully, this step by step guide helps you in setting up tracking for your custom goals that best fit your needs.

Feel free to share your thoughts or ask any clarifying questions related to this post in the comments.

In case you want to take any free online courses on Google Analytics, you can visit [here](http://www.quickcode.co/free/course/learn/Google-Analytics-Basics-For-Beginners-Free--2018/1071).

_Portions of this page are modifications based on work created and_ [_shared by Google_](https://developers.google.com/readme/policies/) _and used according to terms described in the_ [_Creative Commons 3.0 Attribution License_](http://creativecommons.org/licenses/by/3.0/)_._

