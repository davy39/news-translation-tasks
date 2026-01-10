---
title: What is Chromium? How the Chromium web browser is different from Chrome
subtitle: ''
author: Abigail Rennemeyer
co_authors: []
series: null
date: '2019-11-06T19:13:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-chromium-how-the-chromium-web-browser-is-different-from-chrome
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/chromium-image.jpg
tags:
- name: Browsers
  slug: browsers
- name: Google Chrome
  slug: chrome
seo_title: null
seo_desc: 'Chromium...sounds like something on the Periodic Table (it is) or something
  superheroes would use to defeat their enemies.

  Fun fact: it''s also a browser that sounds a lot like Google''s Chrome. And funny
  enough, the two are quite closely related in ce...'
---

Chromium...sounds like something on the Periodic Table ([it is](https://en.wikipedia.org/wiki/Chromium)) or something superheroes would use to defeat their enemies.

Fun fact: it's also a browser that sounds a lot like Google's Chrome. And funny enough, the two are quite closely related in certain ways.

So let's learn a bit more about Chromium - what it is, and how it's different than Chrome.

## What is Chromium?

Chromium is an open source web browser run by [the Chromium Project](https://www.chromium.org/Home), first released in 2008. Any developer can modify or update the source code (but only small number of Chromium devs can actually add their very own code). 

And Chromium has a rather active community of contributors supporting it. Because of this the browser is updated often, which is great. Its different parts are registered under various different licenses, like the [BSD License](https://en.wikipedia.org/wiki/BSD_licenses) (for the parts written by Google - more on that below) and [MIT](https://en.wikipedia.org/wiki/MIT_License), [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License), and others for the rest.

If you wanna check it out, download it [here](https://download-chromium.appspot.com/).

## What is Chrome?

Chrome is Google's web browser. The devs at Google develop, maintain, and release it. But here's a cool fact: Chrome is built on top of Chromium's open-source code.

So how does this work? Well, Google devs take that Chromium code and build their own, proprietary features on top of it. Which gives us Chrome. So Chrome has some extra features like auto-updating, browser data tracking, and native support for Flash. 

Some of these features are helpful, and some (like data tracking) make developers nervous.

If you're a fan, you can download it [here](https://www.google.com/chrome/).

## How they're similar

Since Google's Chrome is actually built on top of Chromium's source code they share the same bones, as we've already established.

Their logos are also quite similar. Chrome's is Google-themed multi-color, and Chromium's is a few shades of blue.

But you're probably far more concerned with the differences, so let's take a look at them.

## The biggest differences between Chromium and Chrome

### They handle updates differently

Chromium updates all the time since devs are constantly modifying the source code. The trouble (or cool thing?) is, you need to manually update the browser as it won't update on its own.

Chrome, on the other hand, updates automatically every so often. So you don't have to remember to update your browser. But it doesn't update nearly as often as Chromium. 

So if you want to see the latest and greatest source code from the Chromium Project right when it's out, then it's best to use the Chromium browser.

### Privacy concerns

Sure, Chrome is super easy to use. But if Chrome is your browser of choice, Google will be [tracking your info](https://www.wired.com/story/google-tracks-you-privacy/). Chromium doesn't do this.

If this makes you uncomfortable, but you still like Chrome as a browser, perhaps Chromium is a better option for you. Your privacy will be more protected but you still get the Chromium source code-based experience.

### Support for Adobe Flash

Google Chrome has built-in support for Adobe's Flash player. But since Flash's code isn't open source the Chromium project won't use it. So if you use Chromium and want to enable Flash, you have to [jump through some hoops](https://helpx.adobe.com/flash-player/kb/flash-player-chromium.html).

Do note, however, that since Flash is being phased out as of 2020 in favor of HTML5 this shouldn't be a huge deal in the near future. 

### My kingdom for a codec

What is a codec, you might ask? A [codec](https://en.wikipedia.org/wiki/Codec) (combo of code and decode) is a computer program that converts between analog and digital sound while compressing and shrinking large file formats. 

Since music and video files are huge, codecs were created to encode (or shrink down) those files and then decode them when ready for viewing or editing.

So why do we need these? If you've had a long week and just want to Netflix and chill this evening you'll need those codecs to allow that content to play.

While Chrome comes with built-in media codecs (like AAC, H.264, and MP3), Chromium does not. Therefore, if you want to stream/binge watch some shows, you'll either need to use Chrome or install those codecs manually in Chromium.

### Google Play store vs outside extensions

If you want to download an extension in Chrome you can only do so from the [Google Play Store](https://play.google.com/store?utm_source=na_Med&utm_medium=hasem&utm_content=Mar0519&utm_campaign=Evergreen&pcampaignid=MKT-DR-na-us-1000189-Med-hasem-py-Evergreen-Mar0519-Text_Search_BKWS-id_100566_%7cEXA%7cONSEM_kwid_43700023142506782&gclid=EAIaIQobChMI-u3I97zx5AIVkcVkCh2ZTAAkEAAYASAAEgKTvPD_BwE&gclsrc=aw.ds) (on Mac and Windows). If you want to get your hands on some outside extensions you have to enable [developer mode](https://developer.chrome.com/extensions/faq).

If you're using Chromium, on the other hand, feel free to grab any extensions you want.

### Security sandbox mode

When you're using plug-ins in Chrome the browser limits their functionality so that they can only perform the function for which you downloaded them. That is, they're "sandboxed" or constrained just to that purpose. Chrome restricts these plugins automatically for you.

This is usually a good thing for security reasons. But Chromium doesn't always have sandbox mode enabled right off the bat. You can learn more about that [here](https://chromium.googlesource.com/chromium/src/+/master/docs/design/sandbox_faq.md).

## Which browser is right for you?

In the end, it depends on what you want out of your browsing experience. 

If you want a simple out-of-the-box browser that doesn't require a lot of attention, Chrome might be for you.

But if you have privacy concerns and don't mind digging in and doing some work, Chromium could provide a rewarding experience.

Happy browsing!

