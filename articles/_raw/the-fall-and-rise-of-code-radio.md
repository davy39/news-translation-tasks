---
title: The Fall and Rise of Code Radio
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2019-07-08T17:36:33.000Z'
originalURL: https://freecodecamp.org/news/the-fall-and-rise-of-code-radio
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/maxresdefault--3-.jpg
tags:
- name: music
  slug: music
- name: General Programming
  slug: programming
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Code Radio is an internet radio station run by the freeCodeCamp community.
  We play music designed to help you focus while you''re coding.

  Over the past year, Code Radio had grown to be one of the largest music streams
  on YouTube. People played it in t...'
---

Code Radio is an internet radio station run by the freeCodeCamp community. We play music designed to help you focus while you're coding.

Over the past year, Code Radio had grown to be one of the largest music streams on YouTube. People played it in their coffee shops and co-working spaces. Wherever people coded, the familiar groove of Code Radio could be heard not too far off in the distance.

In the past 28 days alone, developers listened to Code Radio for more than 14 million minutes. (That's the equivalent of a whopping 27 years of jamming out and coding.)

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Channel_Analytics_-_YouTube_Studio-2.png)

# The Fall

One of the 1,250+ songs on Code Radio contained a short audio sample from an anime that played over a beat at the end of a song.

It turned out that a Japanese media company - through a series of acquisitions - happened to own the rights to that anime. And they used some sort of automated system to trawl YouTube and identify streams that had any samples from their vast catalog of intellectual property.

One of those streams was Code Radio. And on Wednesday morning, their system filed an automated takedown request to YouTube.

Just like that, the stereos in 1,000 cafes, offices, and hackerspaces around the world fell silent. Our Code Radio stream was replaced with this message from YouTube:

![1__Code_Radio%F0%9F%8E%A7___%F0%9F%92%BB_24_7_concentration_music_for_programmers_%F0%9F%94%A5_jazzy_beats_from_freeCodeCamp_org_-_YouTube|690x422](https://www.freecodecamp.org/news/content/images/2019/07/_1__Code_Radio_--___--_24_7_concentration_music_for_programmers_--_jazzy_beats_from_freeCodeCamp_org_-_YouTube.png)

We immediately contacted YouTube support. This had to be a mistake.

The customer service reps we talked to were friendly. But they didn't know how to fix it. They didn't even know how we could regain access our channel's streaming controls. Instead they said they "would look into it and get back to us."

(As of Monday afternoon, we have yet to hear back from them.)

So in the depths of this confusion - in a sea of tweets and emails from dedicated Code Radio listeners asking what was happening - I came to see the truth: **Code Radio needed a new home - a home where a single questionable automated takedown request couldn't wipe it from existence.**

# Code Radio also rises

![Image](https://media1.tenor.com/images/3637aa31124d333fa35935548ffb7996/tenor.gif)

> "Why do we fall, Mr. Wayne? So we can learn to pick ourselves back up." - Alfred in Batman Begins

Ah - a self-hosted Code Radio! There would be several benefits:

1. Watching YouTube uses a lot of data. Many people have limited data plans. If we self-host Code Radio, we could just serve the MP3 files themselves, rather than a video stream. We could even offer a data-light version of the music at a lower bitrate.
2. YouTube is blocked in a lot of countries where freeCodeCamp is popular - including China. A self-hosted version of Code Radio would be available to everyone, anywhere in the world.
3. With YouTube, you have to keep the YouTube app open or the music will stop playing (unless you pay them US $12 per month for YouTube Premium). A self-hosted Code Radio could continue playing in the background on your phone - even when you switch applications or lock your phone.
4. With a self-hosted version, we could build Code Radio mobile apps, Alexa skills so you can easily listen to Code Radio on an Amazon Echo - the sky is the limit.

But how would we implement a self-hosted version? Wouldn't it be expensive to serve 14 million minutes of audio each month. That's a lot of data.

# Building Code Radio

It turns out that the internet radio community is quite active. We immediately found an awesome [open source self-hosted internet radio project called AzuraCast](https://github.com/AzuraCast/AzuraCast).

I reached out to the project maintainer through Twitter, and within minutes, we had him on a call with us. He was a former terrestrial radio guy. He brought us up to speed on the internet radio tooling ecosystem.

Yes - streaming digital audio to people around the world is a lot more expensive than just serving our coding curriculum data. But with some additional donations from supporters, we should be able to swing it.

With AzuraCast, plus some additional relay tools, we could run a self-hosted internet radio station at our previous scale for less than US $100 per month.

_Side note: If you aren't a supporter yet, we would welcome your support. Every little bit helps: [https://donate.freecodecamp.org](https://donate.freecodecamp.org) - And yes, we accept one-time donations, crypto, employer donation matching, and more: [https://donate.freecodecamp.org/other-ways-to-donate/](https://donate.freecodecamp.org/other-ways-to-donate/))_

# Code Radio is live. Help us load-test it and give us feedback.

You can start listening to Code Radio right now: [Listen to Code Radio](https://coderadio.freecodecamp.org)

We are working on a lot of additional features that we'll roll out over the next few days:

* bitrate controls (so you can save your mobile data by listening at 64 kbps)
* some form of chat - preferably with existing forum accounts and forum moderators
* a chatbot (maybe Nightbot again)
* hotkeys
* a better mobile experience
* bringing back the classic Saron Yitbarek Code Radio animation

I would like to thank @abdolsa, @beaucarnes, @raisedadead, @askmp, @scissorsneedfoodtoo, and of course Code Radio DJ and curator [Lawrence Yeo AKA Trebles and Blues](https://twitter.com/TreblesandBlues). They all pulled together and within 24 hours helped get this prototype up and running.

# YouTube da real MVP

In all seriousness, I would also like to thank YouTube. Through their own bumbling, they inadvertently forced us to take a step back and look into the possibility of self-hosting Code Radio.

We will continue to post in-depth coding tutorials and free programming courses on YouTube. We don't hold their own incompetence against them. We are grateful they exist and provide the infrastructure for nonprofits like ours to serve HD video to 1 Million+ subscribers for free.

This is just the latest chapter in our community's gradual move off of proprietary platforms like Medium and Facebook, and over onto our own tools like Developer News and this forum.

Thanks for reading, thanks for listening, and happy coding!

