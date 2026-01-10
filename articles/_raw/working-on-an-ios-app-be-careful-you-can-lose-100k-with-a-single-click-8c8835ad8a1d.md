---
title: Working on an iOS app? Be careful with this.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-29T19:06:33.000Z'
originalURL: https://freecodecamp.org/news/working-on-an-ios-app-be-careful-you-can-lose-100k-with-a-single-click-8c8835ad8a1d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Yr4cMTyueBsyThzsN31J-g.jpeg
tags:
- name: Apple
  slug: apple
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kevin Natanzon

  Integrating certain SDKs can have irreversible consequences


  At Beta Labs, we’ve been building apps for a long time. Throughout our journey,
  we created many apps that reached the Top 10 charts and that were used by millions
  of users...'
---

By Kevin Natanzon

#### Integrating certain SDKs can have irreversible consequences

![Image](https://cdn-media-1.freecodecamp.org/images/6ocmURQGtecBZ9tJ2DaiJUkBCgv2Cy4jggdo)

At [Beta Labs](http://beta.uy), we’ve been building apps for a long time. Throughout our journey, we created many apps that reached the Top 10 charts and that were used by millions of users. However, like any other startup, we’ve also had a ton of huge failures and setbacks.

We’ve been publishing our discoveries, insights and learnings as much as we could. Mainly because it makes us very happy to know that our stories help others build better things online. A lot of creators, founders, marketers and developers reached out letting us know how much it helped them, and it feels great! This was our last post about [Top Nine](http://Topnine.co):

[**Top Nine is going viral!**](https://blog.beta.uy/top-nine-is-going-viral-1cef13033635)  
[_Announcing the Android version_blog.beta.uy](https://blog.beta.uy/top-nine-is-going-viral-1cef13033635)

Today, we want to share with you one of our setbacks, with the goal of saving other app makers from failing to pay attention to something that may become a really big problem in the future.

### The problem: You can lose $100K+ with a click

Maybe this title was a little clickbaity, but imagine that your app is worth that much, and that someone wants to buy it. But you can’t sell it.

It’s really important for anyone involved in the development of an iOS app (marketer, developer, CEO, PM, etc) to be aware of this important issue:

> If you ever use the Passbook entitlement in your app, you’ll never be able to transfer it.

Here’s from the Apple docs:

![Image](https://cdn-media-1.freecodecamp.org/images/1KC9nGJY1GJyA3oVJzdCZFigA9QjjnVRHkXc)
_[source](https://developer.apple.com/library/content/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/TransferringAndDeletingApps.html" rel="noopener" target="_blank" title=")_

While it’s clear that any version of an app may contain Passbook to be transferred, there’s no warning when the developer is adding the framework to the project.

### Why would transferring an app be so important?

For many reasons, but to list a few:

* You may want to **sell your app** to another company, keeping your developer account with other assets.
* You may have **started with a personal** developer account and continued with a company account, where you need to transfer the apps to.
* You may have **published the app under someone else’s account** (like your dev shop), for the sake of simplicity.

### We learned this the hard way

Two years ago, back when we didn’t know much about how to monetize apps, we decided to integrate the Twitter MoPub mediation. We thought the CPM would be high as the potential of the SDK was really big, enabling the same things that the [Facebook Audience Network is currently doing.](https://developers.facebook.com/products/audience-network/overview/)

As part of the integration, we followed [this tutorial](https://www.mopub.com/resources/docs/ios-sdk-integration/ios-getting-started/) written by MoPub.

In addition, the third party networks require:

* AudioToolbox.framework
* AVFoundation.framework
* Ad.framework
* MessageUI.framework
* MobileCoreServices.framework
* PassKit.framework
* Social.framework

As a developer, all you have to do is add the library to the Xcode project. What negative effect could that have?

![Image](https://cdn-media-1.freecodecamp.org/images/YZhEFYzg1-ugHoKty2vOWdvQXrtxm75XjjqM)

A couple of months later, we were able to position [this app](https://blog.beta.uy/we-are-2-9a7318391630) in the number one spot for the “Truth or Dare” keywords, making more than $15,000 a month from organic installs — mostly house party goers looking for a fun app.

We were really happy to find a buyer early on, so we decided to go ahead and sell “cheap” for a really good amount. After all, an asset making $15K/month is worth at least six figures.

Transferring the app was supposed to be really simple, as Apple already provides a process for this. But , after reaching a deal with the buyer, we realized we had added the Passbook entitlement at some point.

![Image](https://cdn-media-1.freecodecamp.org/images/OzizXcATKuzgAfElgkWXB4ryuzu3kuSKwR3X)

(We’ve just recently integrated Passbook to [Top Nine](http://topnine.co) as well, but this time we did so knowingly as it’s required to integrate Apple Pay)

Completing an ecommerce checkout process in two taps is worth not being able to transfer the app until there’s an acquirer who decides to buy the whole company. But again, this is a tradeoff that developers should think about carefully, not realize they’d casually chosen to make their app untransferrable once it’s too late.

### How Apple could fix this

The best (but least likely) way they could fix is to lift this restriction altogether. This is to say, to allow apps to be transferred even when they might have integrated the passbook entitlement at some point in the past. We tried pushing this with Apple, but after years we had no luck.

![Image](https://cdn-media-1.freecodecamp.org/images/dheKP1-VCmtrzB4CKVHqFYTt8osJ8fpxtgwt)

If supporting this is difficult to achieve for some reason, all I’d ask for is a clear warning of the business implications of adding this library at development time. Integrating the Passbook SDK is a decision not to be taken lightly, so if the developer needs to add this library, I’d expect the action to require elevated permissions, as well as a little heads up:

![Image](https://cdn-media-1.freecodecamp.org/images/SvWh1ZE1ZpDG2x2ShF3-hjsQmj3WgOlhmoDF)

### How you can help

If you’re reading this, then that means you’re involved in app development. If that is the case, you may either help a friend in the space, or help us make Apple fix this.

If you’re an iOS developer, and you’d like to help, we just need you to share this post on Twitter with the following tweet:

> Dear @Apple, can you please fix this? — [Tweet this.](https://twitter.com/intent/tweet?ref_src=twsrc%5Etfw&text=Dear%20%40Apple%2C%20can%20you%20please%20fix%20this%3F&tw_p=tweetbutton&url=https%3A%2F%2Fmedium.com%2F%40kevntz%2Fworking-on-an-ios-app-be-careful-with-this-8c8835ad8a1d)

### Thank you!

