---
title: How (and Why) to Get Started with Google Analytics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-16T01:07:25.000Z'
originalURL: https://freecodecamp.org/news/how-and-why-to-get-started-with-google-analytics-153dc35b7812
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OV9Z2nnWNUHlfeTqyZsotg.jpeg
tags:
- name: Google
  slug: google
- name: Google Analytics
  slug: google-analytics
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Julia Bourbois

  What is Google Analytics?

  Essentially, Google Analytics is the go-to solution for monitoring website usage.
  Though it is frequently used in conjunction with Google Adwords, for e-commerce,
  and in improving website user experience, i...'
---

By Julia Bourbois

### What is Google Analytics?

Essentially, Google Analytics is the go-to solution for monitoring website usage. Though it is frequently used in conjunction with Google Adwords, for e-commerce, and in improving website user experience, it is flexible and powerful enough to be used by any organization that has a website. Indeed, you do not need coding prowess to utilize Google Analytics.

So, this guide is directed principally to individuals who do not consider themselves or their principal professional responsibilities to be tech. It will touch only on the essential elements to get started with Google Analytics.

### What can Google Analytics do for me?

Odds are your organization has a presence on the web. Google Analytics collects and renders a tremendous amount of data. Raw data is curated into a variety of reports depending on your needs. The data-driven insights that are applicable to your organization will depend on your goals for your site and your organization. Even if your goals are not yet defined there are areas of Google Analytics that are useful for most organizations.

Google Analytics can also help you identify underlying issues with the site. For instance, if there are performance or usability issues for mobile users of your site.

#### Acquisition Overview

Acquisition Overview answers questions like: How much traffic does the site receive? What is the origin or top traffic for your site? What is your goal conversation rate? What is the break down of new versus returning users?

This is particularly useful when examining change over time. Comparing weeks or months will give you a better idea of site performance over time.

![Image](https://cdn-media-1.freecodecamp.org/images/XoCS-GRdyo8QcF1FPoyfcUCXhGLj3tn7T-NX)
_courtesy of Google Analytics Demo Site_

#### Behavior Overview

Some pages will be more important to your organization than others. On the Behavior Overview page, individual page performance will help you identify which pages are bringing in the most traffic. It will also provide you with an overview of your site’s technical performance, such as the bounce rate.

![Image](https://cdn-media-1.freecodecamp.org/images/iS-mF9UwYzQrT13PMW8vqV1JWvPLJM-yQQcI)
_courtesy of Google Analytics Demo Site_

If you are working in e-commerce, pages such as the home page, product pages, search results, the shopping cart, check out, and the thank you page, will be critical pages on your site to track.

However, if you’re a museum you may want to track pages for education, exhibition, and programming. You may also be interested in targeting geography to get a better idea of your target audience. Museums, as well as restaurants, diners, and cafes, will want to prioritize the local search optimization.

#### Conversion Overview

For Business impact reports, it is necessary to configure goals or e-commerce transactions. Google Analytics will not automatically establish your goals for you. Goals can be established for your site in the Administration Panel under “View.” Goals are very broadly defined and can be e-commerce transactions, or lead captures from submissions or reservations.

Goals with a dollar value illustrate the strengths and weakness in the pages of the sites. The Conversion Overview will enable you to drill down in your goal conversions and well as learn more about your customer’s path.

![Image](https://cdn-media-1.freecodecamp.org/images/JVBW-ATllweRSBDhbLTMLntZ6syK-YbmZ7AY)
_courtesy of Google Analytics Demo Site_

### How — The Basics

So how do you get started?

Create your account by logging on to [Google Analytics](https://www.google.com/analytics/#?modal_active=none). In the upper right corner, login or create an account if you don’t have one.

![Image](https://cdn-media-1.freecodecamp.org/images/g6GtKsj59vZPgGJxt0yA3krKLIaOAYeJRK2Y)
_courtesy of courtesy of Google Analytics Demo Site_

Then select either website or mobile app. You will provide account name — typically the name of your business. Then set up the URL. Select either [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) or HTTPS — start with HTTP if your site switches between HTTP and HTTPS.

Then select an industry category. This is an important step as it enables Google to set benchmarks for your site and compare your site’s performance with others in the same industry.

![Image](https://cdn-media-1.freecodecamp.org/images/hrG4KeGDDMXLz0PcLRRknqlVLMX5KDY8ZnRo)
_courtesy of Google Analytics Demo Site_

Then select the reporting country and time zone. While not a critical issue, consider the time zone you select to be permanent. Though it can be changed, it will not retroactively change the data. Leave everything checked as these resources can become invaluable. You can read the “ReadMore” to learn how Google uses your data.

![Image](https://cdn-media-1.freecodecamp.org/images/Oz8ADgYEqBeX2zQNDqb5c-O3G45yGiqpBk3r)
_courtesy of Google Analytics Demo Site_

Next, select “Get Tracking ID”. Review terms and services, and select “I accept”.

Now you will install your tracking tag. Select “Tracking Info” and then “Tracking Code”. The tracking code is a snippet of unique code that you will need to copy and paste to every page of your site that you want to be tracked by Google Analytics.

Copy your tracking code just below the `<he`ad> on your HTML page. Then go to “Google Tag Manager.” You can select the link to learn more about this. Click on “Status”. Here Google will let you know whether you are receiving data.

**Note:**   
Here’s how to install the Google Analytics tracking tag on your [Wordpress pages.](http://www.wpbeginner.com/beginners-guide/how-to-install-and-setup-google-tag-manager-in-wordpress/)

Here’s how to install the Google Analytics tracking code onto your [HubSpot pages](https://knowledge.hubspot.com/articles/kcs_article/cos-general/how-do-i-put-my-google-analytics-code-onto-my-new-landing-pages).

#### Creating a View

![Image](https://cdn-media-1.freecodecamp.org/images/CGGFXWaEYdCl7nfG1EeC6Nyk3uCtstcnp69Z)
_courtesy of Google Analytics Demo Site_

It is considered a best practice that the first “View” you create is a Master View. A Master View contains an unfiltered history of the analytics, sort of like a backup.

#### Creating a Filter

Google applies filters to your data before it presents it to you in your reports.   
The most important filter to start with is excluding yourself and your employees from appearing in your data. You do not want your data appearing along with that of your users.

Create a filter that excludes the [IP addresses](https://en.wikipedia.org/wiki/IP_address) for yourself. If you do not know you IP address, simply do a Google search for “what is my IP address?”. You will need to exclude the IP address for each computer used by yourself and your employees for work. These will need to be added individually.

From the Admin Panel, select the “Default View”. From the drop-down menu, select “Add Filter” and give it a name (such as Exclude Employees). Next, you have the option to select from a predefined filter or a custom filter.

![Image](https://cdn-media-1.freecodecamp.org/images/ZI1rnM9kVQp9Y-KbzV-xDtfLUK4G0d4-CRBh)
_courtesy of Google Analytics Demo Site_

A predefined filter acts as a template for what you’d like to do. Select “predefined” and choose from the drop-down menu. Select “Exclude or Include only”. In this case, you will select traffic from the IP addresses and then select the appropriate expression. Enter the data to exclude, such as an IP address. Then “Save.”

From this point moving forward, all of the data in the default view is going to exclude any data that is excluded by this filter, but it is not going to historically exclude data.   
   
It is very common to add multiple filters. However, filter order matters. Filter order affects the subsequent results. Filter order matters because the output of one becomes the input of the next. Explore the filters to see what is most relevant to your organization’s goals.

**Note**: If you want to include/exclude two things, you are essentially creating an “or” Filter. Go to Filter Field, then filter pattern. Type the first term to exclude then the pipe symbol (|) and the second term.

#### Output

Google Analytics makes printing or sharing your analytics reports very easy. In the top right corner, you have the option of printing or sharing your report. It can also be saved and edited.

![Image](https://cdn-media-1.freecodecamp.org/images/TB28LGcdSb-ips3sh60vMUBWeBMYuMCmN7gg)
_courtesy of Google Analytics Demo Site_

![Image](https://cdn-media-1.freecodecamp.org/images/Q1mhFsjEdDkL6cgkJepNGgWNCCEtNEieTgjx)
_courtesy of Google Analytics Demo Site_

### Moving Forward

Google Analytics offers numerous reports, as well as data segmentation options, which are beyond the scope of this article. Find the reports that most closely align with your needs.

With the introduction of Google Analytics 360 Suite, formerly Google Analytics for premium users, Google’s analytics is only getting more advanced. Google Analytics 360 provides analytical data that companies can be used to track return on investment (ROI) and marketing indicators.

### Further Reading

For a deep dive into Google Analytics, read [Google Analytics for Web Designers and Developers](https://www.wpbeaverbuilder.com/google-analytics-web-designers-developers/).

For tutorials for beginners can be found on [Google Analytics for Beginners](https://analytics.google.com/analytics/academy/course/6).

If you are a novice to coding, I recommend [Moms can: Code](https://www.momscancode.com/) and [CodeNewbie](https://www.codenewbie.org/).

Follow me on [Twitter](https://twitter.com/JuliaBourbois).

