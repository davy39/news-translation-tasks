---
title: How non-Chinese developers can leverage WeChat’s 1.1B monthly active users
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T17:24:26.000Z'
originalURL: https://freecodecamp.org/news/how-non-chinese-developers-can-leverage-wechats-1-1b-monthly-active-users-285083836bb9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-YhMcu5J_3HtuxLOJOJgWg.jpeg
tags:
- name: china
  slug: china
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: WeChat
  slug: wechat
seo_title: null
seo_desc: 'By William Kwan

  Over a million WeChat Mini-Programs have been published since the platform launched
  two years ago. By comparison, it took the App Store a decade to reach two million
  apps.

  The average WeChat user spends 66 minutes a day on WeChat. Min...'
---

By William Kwan

Over a million WeChat Mini-Programs have been published since the platform launched two years ago. By comparison, it took the App Store a decade to reach two million apps.

The average WeChat user spends **66 minutes a day on WeChat**. Mini-Programs emulate the experience of a lightweight mobile app, without requiring the user to leave WeChat or wait for a long download. This expedites onboarding, both online (Mini-Programs are predominantly accessed through social sharing) and offline (typically done through QR codes).

This idea that you can get more users by circumventing the download process has been thrown around in the Western tech scene. Around the same time the Mini-Program platform launched, we rode the hype train for Messenger Chatbots. Android Instant found a few niche use cases, but never caught on.

As a Canadian software developer with Chinese heritage, I don’t think we should adopt this all-in-one user experience over here. Mobile-optimized websites and native mobile apps already cover all the important use cases.

But in China, WeChat has been the monolithic app for everything years before there were Mini-Programs. Everything from hailing a cab to paying for a meal, to connecting with nearby strangers is done from WeChat. Mini-Programs are the natural evolution, creating a semi-open platform in a country where the government has historically blocked foreign competitors.

Iconic Western brands in China have already started switching from native apps to Mini-Programs. Fast food chains like McDonald’s and KFC let you order food and claim coupons in their Mini-Program. Luxury brands like [Gucci and Burberry are creating games and promotions](https://jingdaily.com/burberry-wechat-mini-program/) to market their products.

Many Mini-Programs are built to complement local Chinese businesses such as stores, restaurants, and hotels. For technology-focused Mini-Programs, games are leading category. Several game engines offer Mini-Program support, including [Cocos](https://docs.cocos.com/creator/manual/en/publish/publish-wechatgame.html).

But the platform is also a breeding ground for tech startups. The most notable is Pinduoduo, the group buying app which went public in the US in July 2018 with a $23.8B valuation and is currently seeking to raise another $1.5B just six months later.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nzQ2FFx8FyU8Aw05lup4ZQ.png)
_Image credit: GGV Capital_

I’ve been working on a Mini-Program lately, and since I never learned how to read Chinese (despite a childhood of my parents’ bickering), overcoming the language and cultural barriers are really difficult. Not only is much of WeChat’s documentation Chinese-only, but Chinese software has different standards for the user experience. Simply translating an app intended for the Western market doesn’t work.

Furthermore, there are technical challenges involved:

* Mini-Programs are limited to 10 MB in size to ensure fast download
* Hardware access is limited to what WeChat provides through their API (notably, you can’t use NFC)
* Links to websites aren’t allowed (Tencent wants users on WeChat, and WeChat only)

In spite of the obstacles, this opportunity is too large to ignore. The Chinese are the world’s most active social media users, and they already love high-quality Western products, similar to how we admire Japanese manufacturing. “Made in China” is an ironically bad way to promote a product in China. Western tech startups could use this to their advantage, but almost none of them are adopting a China-first strategy.

If you want to be one of the few courageous developers to give the Chinese market a shot, I made this tutorial to teach you how to make your first Mini-Program. If you’re familiar with full stack JavaScript web development, you’ll pick up the tech stack quickly. It consists of a JavaScript client and server, a modified version of HTML/CSS, and a JSON database.

If you found the tutorial helpful, I’d love to create more content like this and build a community for English-speaking WeChat developers. Feel free to ask any WeChat development questions in the comments and I’ll try my best to help you out!

