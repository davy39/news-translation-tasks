---
title: How to set up and track YouTube Channel performance with Google Analytics
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-03-18T13:27:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-and-track-youtube-channel-performance-with-google-analytics
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/youtube-analytics-1.jpg
tags:
- name: analytics
  slug: analytics
- name: '#content marketing'
  slug: content-marketing
- name: Google Analytics
  slug: google-analytics
- name: marketing
  slug: marketing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Managing a YouTube channel is a lot of work. It includes content experimentation
  which can make or break your SEO effectiveness for your channel. How can we track
  our channel’s performance to see what works?


  Why is SEO important?

  How is SEO importan...'
---

Managing a YouTube channel is a lot of work. It includes content experimentation which can make or break your SEO effectiveness for your channel. How can we track our channel’s performance to see what works?

* [Why is SEO important?](#heading-why-is-seo-important)
* [How is SEO important to YouTube?](#heading-how-is-seo-important-to-youtube)
* [And what is Google Analytics?](#heading-and-what-is-google-analytics)
* [How do I connect my channel?](#heading-how-do-i-connect-my-channel)
* [What will I be able to see?](#heading-what-will-i-be-able-to-see)
* [What won’t I be able to see?](#heading-what-wont-i-be-able-to-see)
* [What else can I do with YouTube and Google Analytics?](#heading-what-else-can-i-do-with-youtube-and-google-analytics)

%[https://www.youtube.com/watch?v=P8wv4ylc_-s]

## Why is SEO important?

[SEO, or Search Engine Optimization](https://moz.com/learn/seo/what-is-seo), is the practice of writing and organizing content in a way that search engines like Google can crawl and ultimately understand what your website or YouTube channel is about.

Using this information, Google and others make decisions with their algorithms to determine which content is of higher quality, more relevant, and more likely to answer the question you’re looking for on their search engine in the first place. With that information, the search engines rank this content and display their results ordered by those rankings.

## How is SEO important to YouTube?

Just like any other website, YouTube gets crawled by Google and other search engines. Additionally, YouTube has its own internal search that will take these same things into consideration when deciding how to display results on a YouTube search.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/searching-for-code-channels-on-youtube.jpg)
_Searching for "code" channels on YouTube_

This means, depending on how well you create your descriptions, manage your keywords, or name your videos, it could impact how well your videos rank in the results. And this can impact how many views your videos get.

This also applies to your channel. You have opportunities to experiment with effectiveness through the content you feature, your channel description, and the name of your channel.

## And what is Google Analytics?

Google Analytics is a [free analytics tool](https://analytics.google.com/analytics/web/) from Google that will allow you to gain better insights into your traffic. I previously wrote about [what is Google Analytics and how you can make sense of it](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/) which provides a more in depth view. So if you want to learn a little more before diving in, I highly recommend starting there.

## How do I connect my channel?

### Setting up a new tracking code

To start, we’ll need a tracking code from Google Analytics. Google has some great up to date resources on how to do this, so I'm not going to try to re-explain here:

* [Setting up a new property](https://support.google.com/analytics/answer/1042508)
* [Getting your Tracking ID](https://support.google.com/analytics/answer/1008080?hl=en)

Though some say you can use your website’s property and create a filtered View, I recommend starting with a separate property. That way you don’t have to worry about any data crossover or setting up complicated filters.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-tracking-id.jpg)
_Tracking ID in Google Analytics_

Your tracking ID will be in the following format: `UA-######-#`. Once you have that, we're ready to go.

### Adding your tracking code to YouTube

There are a few steps we have to navigate through to find where we can set up our Google Analytics account. If you want to skip to the right place, you can visit [youtube.com/advanced_settings](https://www.youtube.com/advanced_settings).

To take the long route, which will also help you get a little more familiar with your YouTube account, first head over to the **Settings** section from within your **YouTube Studio** page.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/youtube-studio-channel-settings.jpg)
_Finding Settings on your YouTube Studio dashboard_

Once selected, find the **Advanced channel settings** link by visiting **Channel**, **Advanced Settings**, and then scrolling down to the bottom.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/youtube-advanced-channel-settings.jpg)
_**Advanced channel settings** on YouTube_

Finally, scroll down to the bottom of the page again, find the **Google Analytics property tracking ID** field, enter the tracking ID you created, and hit save.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/youtube-advanced-channel-settings-google-analytics-property-1.jpg)
_Setting the Google Analytics property tracking ID for your YouTube channel_

### Sit back and wait

Google Analytics will only show your website traffic from the point it was set up and through the future. Unfortunately we can’t check out that weekend your video first went viral if you didn’t have Google Analytics set up then, but at least we’re prepared for the next time!

![Image](https://www.freecodecamp.org/news/content/images/2020/03/friends-recline-chair.gif)
_Joey and Chandler reclining their chairs_

That said, now's the time to continue working hard on your channel since you have the ability to track how that hard work is paying off as people visit your channel.

### Optional: Setting up Site Search

Setting up [Google Analytic’s Site Search](https://support.google.com/analytics/answer/1012264?hl=en) feature gives us an easy way to separate out search usage to make it easier to gain insight into how people are searching our channel.

To enable Site Search, we want to go to the **Admin** section of our Google Analytics property and then navigate over to **View Settings**. Once there, under the **Site Search** settings at the bottom, first click the button to toggle on **Site search Tracking**, then type “query” into the **Query parameter** input.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-site-search-tracking.jpg)
_**Site search Tracking** in Google Analytics_

Optionally, though recommended, you can select to strip query parameters out of your URL. This means that in your main content view, you will see all traffic as /search instead of many instances of /search?query=[keyword], which can be more cumbersome to analyze.

_Note: before you set this up, it’s [generally recommended to have more than one view for your property](https://www.e-nor.com/blog/google-analytics/best-practices-views-google-analytics). I would recommend having at least 2 views, a Raw Data view and Main view. You would only apply the Site Search feature to your Main view. This will help to make sure you can always see the unfiltered Raw Data view if you want._

## What will I be able to see?

### How many people visited my channel?

The first thing we get immediately with our new data when we open up our Google Analytics property is how many people visited our site.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-home.jpg)
_Google Analytics Home_

The default here is in the past 7 days, but you can change the time range in the bottom left corner of the panel.

What this also provides is a quick insight into how the number of people has changed since the previous period (the 7 days before in this example). As we can see here, the number of people this week has increased by 13.9% which is awesome news for freeCodeCamp’s YouTube channel, proving whatever they did is working.

### How are people finding our channel?

So how do we figure out if the strategies we’re using (like SEO) to get people to our channel are effective? By analyzing our organic search traffic.

By navigating to the **Source/Medium** report by visiting **Acquisition**, **All Traffic**, then **Source/Medium**, we can see what sources are providing our YouTube channel the most traffic.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-source-medium-report.jpg)
_Source/Medium report in Google Analytics_

By clicking in to **google / organic**, we can also see how this has changed over time.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-organic-google-referral-report.jpg)
_Organic Google traffic report in Google Analytics_

While analyzing a single week isn’t the most effective, being able to tell how your organic traffic has changed over multiple weeks will be able to tell you if your strategy is working.

### What websites and pages are people coming from?

Navigating to the **Referrals** report by going to **Acquisition**, **All Traffic**, and then **Referrals**, we can see that most of the referral traffic for the [freeCodeCamp YouTube](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) is from [freeCodeCamp.org](https://www.freecodecamp.org/) itself.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-freecodecamp.org-referral-traffic.jpg)
_Referral traffic showing freecodecamp.org as highest referrer in Google Analytics_

But say we want to see what pages those referrals are coming from. We can find this out by clicking on the **freecodecamp.org** link in the view above where we can see a full breakdown of which pages are giving the channel the most traffic.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-referring-pages-from-freecodecamp.org.jpg)
_freecodecamp.org referral pages on Google Analytics_

### What are people searching for on my channel?

After setting up [Site Search](https://support.google.com/analytics/answer/1012264?hl=en) on your Google Analytics account, you’ll be able to get better insight into how people are actually searching your site.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-search-terms.jpg)
_Search Terms report in Google Analytics_

Here we can see what keywords people want to see the most, meaning we can tailor our content and future videos to those keywords, making our channel more effective.

### More insights

By default, you’ll get a lot of other cool insights from Google Analytics that are baked in like where your visitors are physically located and whether they’re visiting on a desktop or mobile device.

To learn more about what you can see, check out [my article on making sense of Google Analytics](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/).

## What won’t I be able to see?

While the information you’ll discover through Google Analytics is important, it’s not all inclusive. There are many points you’ll need to dive into YouTube’s own Analytics tool to see.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/youtube-studio-analytics-dashboard.jpg)
_Analytics dashboard in YouTube Studio_

### Video analytics

Video states and actions aren’t going to be visible in Google Analytics, which includes things like Play, Pause, and time watched.

However, by using the **Engagement** tab in the [YouTube Studio](https://studio.youtube.com/) **Analytics** section, we can see how long people are watching our videos and a graph of the **Audience retention.** This will help us determine how the content of our videos is performing.

### Subscribers

You’re not going to be able to gain insights into how the visitors on your channel are subscribing.

The good news is you can find this by visiting the the **Analytics** section in your YouTube Studio page, then clicking the **Audience** tab at the top.

### Dig in to YouTube Studio Analytics

There’s a whole lot you can find out if you dig around YouTube Studio Analytics. Take the time to poke around both Analytics report solutions and learn what information is most useful to providing an impactful experience for your channel.

## What else can I do with YouTube and Google Analytics?

### Track links from YouTube to your website

If you have a website outside of your YouTube channel and have Google Analytics set up on it, you can build custom URLs that will allow you to see your YouTube traffic as a campaign. This is useful not only for YouTube, but any other source you’re directing traffic to your website from.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-campaign-url-builder.jpg)
_Building campaign URLs [Campaign URL Builder](https://ga-dev-tools.appspot.com/campaign-url-builder/)_

Google Analytics provides this capability using URL parameters attached to the links. You can learn more about the setup and what you need to do with [Google’s Analytics Help site](https://support.google.com/analytics/answer/1033863?hl=en).

It should also be noted that you don’t really need to set up your YouTube channel with Google Analytics to make use of this feature.

### Track how videos are watched when embedded on your website

YouTube provides an [API](https://developers.google.com/youtube/iframe_api_reference) that developers can use to write custom JavaScript and track usage of embedded videos on a given website.

Using this, we can send custom events based on time references or video actions (like play and pause) to get a better idea of how the videos on our site are being used.

To be clear – this is only for videos embedded on your website and will probably track usage with your website's Google Analytics property unless you configure it otherwise.

Check out [YouTube iFrame Player API](https://developers.google.com/youtube/iframe_api_reference) for more info.

### Pretty much anything Google Analytics provides by default

[There’s a whole lot you can do with Google Analytics](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/), whether it’s getting better visibility into where people are coming from or where they’re physically located. And by connecting your YouTube channel you automatically get those insights.

## The more resources, the more insight you can gain

Though there are benefits to both YouTube Analytics and Google Analytics, having more information will ultimately help you make better judgement calls about how you manage your channel and content. Use these tools to help launch yourself to inevitable YouTube stardom!

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

