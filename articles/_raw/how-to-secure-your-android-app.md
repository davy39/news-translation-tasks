---
title: How to Secure Your Android App – Four Security Best Practices Every Android
  Dev Should Know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-28T16:01:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-your-android-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/android-app-coding-security.jpg
tags:
- name: android app development
  slug: android-app-development
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
seo_title: null
seo_desc: "By Andrej Kovacevic\nIf you've been following the news lately, you may\
  \ have noticed a worrisome tech trend. The frequency and severity of cybersecurity\
  \ attacks are exploding. \nWe've seen news of a sprawling hack involving the SolarWinds\
  \ management pla..."
---

By Andrej Kovacevic

If you've been following the news lately, you may have noticed a worrisome tech trend. The frequency and severity of cybersecurity attacks are exploding. 

We've seen news of a sprawling hack involving the SolarWinds management platform. That attack may have compromised the systems of [over 18,000 SolarWinds customers](https://www.npr.org/2021/04/16/985439655/a-worst-nightmare-cyberattack-the-untold-story-of-the-solarwinds-hack). 

Then, we found out that a zero-day flaw in Microsoft's ubiquitous Exchange email server caused affected systems to get hacked [faster than experts could count](https://www.zdnet.com/article/microsoft-exchange-server-attacks-theyre-being-hacked-faster-than-we-can-count-says-security-company/).

For the average software developer (like me), that's downright scary. After all, if big multibillion-dollar companies like those aren't immune to disastrous hacks, what chance does my code have to stay safe?

Well, it turns out that there's some good news and bad news on that front. 

The good news is that the types of large-scale attacks we've seen lately are just that – large scale. In other words, the kinds of groups (or nation-states) that can carry out attacks like those don't care all that much about the kinds of small software projects I work on.

But the bad news is this: there are plenty of small-scale hackers who are more than happy to make your life as a developer miserable. And they will do it if you let them. 

But you can do something about it. You can make it your mission to put as many roadblocks in their way as possible. By covering the most likely angles of attack on your software, you can increase the odds that a would-be attacker will pass your code by and look for an easier target.

Now, I've already written extensively about a variety of software security topics. But because I happen to be working on an Android application at the moment – and [because Android is a favorite target of hackers](https://thehackernews.com/2020/05/stranhogg-android-vulnerability.html) – I've decided to share four of the most important Android app security principles you can include in your apps on the platform. I make them a focus of my security efforts, and you should too. 

## 1. Protect Your App's Transport Layer

One of the first things an attacker will look for when targeting an Android app is to see if they can intercept any of the data passing between it and your server's backend. 

By eavesdropping on those communications, they can tell an awful lot about your app. And if you're really unlucky, they might even be able to use the data to figure out how to impersonate your app and gain inappropriate access to server-side data.

So, step one in your effort to secure an Android app is simple: protect its data transfer layer by employing strong encryption. 

You can do this by making use of protocols like [SSL](https://www.freecodecamp.org/news/openssl-command-cheatsheet-b441be1e8c4a/) and [TLS](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/), which are simple to add to your code and are very difficult to compromise. And once you have a solution in place, take the time to do some [threat modeling](https://www.freecodecamp.org/news/threat-modeling-goran-aviani/) to decide if you've done enough to protect your app's traffic.

If you are dealing with particularly sensitive data, you may even want to go a little further and build a VPN-type solution right into your app. If you've never implemented a VPN in an Android app before, you can read up on the basics of adding one [here in the Android developer guide](https://developer.android.com/guide/topics/connectivity/vpn). 

If you go this route, you can even advertise the feature to your customer (or end-users if you're building something public). Android VPN apps are so commonplace these days that the mere mention of the feature will let users know that you're serious about their data's security – and that's always a nice PR bonus.

## 2. Make Authentication Bulletproof

![Image](https://www.freecodecamp.org/news/content/images/2021/05/app-authorization-bulletproof-2fa.jpg)
_Image: thodonal / Adobe Stock_

Besides your app's data streams, the next most common attack vector to eliminate is any weakness in its authentication methods. 

The trouble with doing that is your users. By that, I mean that you need to make your app's authentication process as secure as you can without making it so onerous that your users will revolt (and if I had a dollar for every time a client asked me if 2FA was _really_ necessary, I'd be retired by now).

Regardless of how many times you have to answer the question, though, 2FA is both necessary and worth implementing. 

On top of that, you also need to pay attention to how you handle things like key exchanges. At a minimum, you should be using AES encryption to keep those transactions secure.

And last but not least, you should make certain to [use token-based security](https://auth0.com/learn/token-based-authentication-made-easy/) to authenticate legitimate requests from your app to its backend. That makes making such requests difficult enough that even if an attacker finds a way to view a live data stream, they'll have no way to use that information to launch an attack.

## 3. Guard Against Code Injection

The next thing you should worry about is the public-facing parts of your app. Because most apps are interactive, they will provide users the ability to input data in one form or another. This can be through text-input fields like forms, or through direct data uploads for exchanging things like documents and pictures. 

And every time you add a user input feature, you should take great pains to make sure that nobody can use them against you.

The first way to address this is to use proper input validation. If your app expects specific text in a field, make sure it won't accept anything else. You can do this by adding a [pre-built text validation module](https://www.simplifiedcoding.net/android-form-validation-tutorial/) or by [building your own](https://www.freecodecamp.org/news/form-validation-with-html5-and-javascript/) (if you have the time and inclination). 

If you plan to let a user upload pictures or other specific files, you must include an ability for the app to scan the uploaded file to make sure it is what it claims to be. 

Again, this is possible using any number of pre-built modules. I tend to favor [JMimeMagic](https://github.com/arimus/jmimemagic) because it can handle a variety of MIME types, but you can use whatever solution works best in the context of your project.

## 4. Minimize and Secure Client-Side Storage

Last but not least, you should strive to build your app with the smallest local data footprint that's feasible to get the job done. 

That's because any data you store on a client device is outside of your control and is therefore vulnerable to external threats. 

If a user's device gets compromised by any attack that yields access to the data stored on it, you may inadvertently give the attacker a roadmap to steal information from your app.

Now, storing no client-side data is near-impossible – especially if you need your app to retain some or all of its functionality offline. So, at the very least, make sure any and all client-side data you store remains encrypted at all times. 

And, try to eliminate storage of any data that could pose a problem if an attacker got their hands on it. Things like contact lists, message longs, or any kind of usage history come to mind.

And beyond storage, you'll want to test your app to see that it isn't vulnerable to memory leaks that might expose critical data. 

To do that, you should get familiar with tools like the [OWASP Zed Attack Proxy (ZAP)](https://www.zaproxy.org/). It will help you to find any vulnerabilities in your app's memory usage before attackers can use them against you. 

It can be a bit complex to get the hang of, but there's plenty of good documentation and a fantastic user community that will help you along.

## Locked Up Tight

I wish I could tell you that any app built using these four principles will be invulnerable to every threat. But attackers work to find new flaws every minute of every day, and unless you make countering them your job too, you're unlikely to find a perfect solution. 

But by covering these major attack vectors, you will at least make their work hard enough that it won't be worth it to try (unless your app contains something of immense value locked up inside). 

And at the end of the day, that's all anyone can ask of you as a developer unless they're willing to pay you handsomely to guard against every possible threat – and hey, wouldn't that be nice?

_Featured image: Arthur Shevtsov / Adobe Stock_

