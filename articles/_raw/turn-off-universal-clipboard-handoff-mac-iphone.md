---
title: How to Turn Off Universal Clipboard Handoff on your Mac and iPhone (and why
  you should disable this)
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-07-03T17:54:51.000Z'
originalURL: https://freecodecamp.org/news/turn-off-universal-clipboard-handoff-mac-iphone
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99e0740569d1a4ca2234.jpg
tags:
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
seo_title: null
seo_desc: 'I''m about to tell you something that will shock you, and probably make
  you very angry. I hope you won''t hate me for it. Here goes.

  If you are an iPhone user, everything you have copied to your clipboard on your
  iPhone can be secretly accessed by vari...'
---

I'm about to tell you something that will shock you, and probably make you very angry. I hope you won't hate me for it. Here goes.

If you are an iPhone user, everything you have copied to your clipboard on your iPhone can be secretly accessed by various apps. These apps often record the contents of your clipboard several times a minute, and send them to their company servers to store for eternity.

Think about all the things you copy to your clipboard. Links. Passwords. Private messages to your friends and family.

All of these things are being stolen from you and sent to the data centers of multinational corporations, who will use it to figure out what ads to show you so they can make more money.

And that is just the best case scenario. There's no way to know for sure what they are using your clipboard data for.

Apple has known about this for a long time. And they are just now taking steps to restrict apps' access to your clipboard, and to notify you when an app accesses the contents of your clipboard.

This was never an issue for Apple until privacy advocates started raising awareness of this earlier this week.

Here's an insane supercut of several well-known apps stealing the contents of your clipboard (which now triggers a notification in the newest version of iOS.)

%[https://www.youtube.com/watch?v=pRSWdtoUAjo]

Some apps, like TikTok, use this clipboard exploit even while running in the background to steal every single character you type into any app.

Here's an example of this discovered when Apple started showing clipboard notifications in the iOS 14 beta:

%[https://twitter.com/jeremyburge/status/1275832600146391042]

Apps can even use this clipboard exploit to get your location data without you ever granting them permission. Here's how:

%[https://www.youtube.com/watch?v=T2-Ot6MrvVs]

## And it gets worse.

Now I'm going to tell you something else that will really make your blood boil: **If you use a Mac, your iPhone has access to your Mac's clipboard by default.** 

And this means, by extension, the apps installed on your iPhone also have access to things you copy to your Mac's clipboard.

Think about that. How many sensitive things do you do on your laptop every day? How many passwords to you copy/paste from your password manager? How many emails do you type up? How many websites do you copy/paste to share through private messages? 

All of that is going to your clipboard, which is getting shared with your iPhone, which can then be accessed by various companies through their iPhone apps, and stored in their servers around the world.

This "feature" is called Universal Clipboard or "Handoff." And it is enabled by default on every Mac. 

For your privacy, I recommend you turn this feature off immediately. It only takes a few seconds. Here's how to do this.

# How to Turn Off Universal Clipboard Handoff

## Step #1: Open Spotlight Search.

By default, you can open MacOS Spotlight Search by pressing the command key and spacebar at the same time.

Then type the word "Handoff" and double click the "General" option that appears under "System Preferences" in the list below.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Spotlight_and_How_to_Turn_Off_Universal_Clipboard_Handoff_on_your_Mac_and_iPhone__and_why_you_should__-_freeCodeCamp_org.jpg)
_A screenshot of Apple Spotlight Search_

## Step #2: Uncheck Handoff.

A menu will pop up when you click "General" under the "System Preferences" option. If you look all the way at the bottom of this menu, you will see an option that says "Allow handoff between this Mac and your iCloud devices." Uncheck the box next to this.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Menubar_and_General_and_how_to_turn_off_ios_universal_clipboard_-_Google_Search-2.jpg)
_A screenshot of the General section of Mac OS's settings_

# Congratulations. You've just turned off Universal Clipboard Handoff.

My advice would be to uninstall all the apps that have been stealing information from your clipboard without your consent. 

These apps have violated your trust by abusing this "vulnerability" in iOS. (I put the word vulnerability in quotes because, again, Apple has known about this for a long time and initially refused to do anything about it.)

Here's a list of apps who have been caught red-handed stealing your clipboard data:

```
10% Happier: Meditation 
5-0 Radio Police Scanner 
8 Ball Pool
ABC News
Accuweather 
Al Jazeera English 
AliExpress Shopping App 
AMAZE!!!
Bed Bath & Beyond
Bejeweled
Block Puzzle 
CBC News 
CBS News 
Classic Bejeweled 
Classic Bejeweled HD 
CNBC 
Dazn 
FlipTheGun
Fox News
Fruit Ninja
Golfmasters 
Hotel Tonight
Hotels.com 
Letter Soup 
Love Nikki 
My Emma 
New York Times
News Break
NPR 
ntv Nachrichten 
Overstock 
Pigment – Adult Coloring Book 
Plants vs. Zombies
Pooking – Billiards City
PUBG Mobile
Recolor Coloring Book to Color 
Reuters 
Russia Today 
Sky Ticket 
Stern Nachrichten 
The Economist 
The Huffington Post 
The Wall Street Journal 
The Weather Network 
Tomb of the Mask: Color
Total Party Kill 
TikTok
Truecaller
Viber
Vice News 
Watermarbling
Weibo
Zoosk
```

And last but not least, change your passwords! Assume that these passwords have been intercepted by these clipboard-thieving apps are now in private data centers all over the world.

Sure – these companies are unlikely to use your passwords. But they may eventually get hacked. And hackers might try to exploit your passwords or sell them to even worse actors.

It breaks my heart to learn of this. It's been going on for maybe years.

And in case you're curious, Android is just as permissive with letting 3rd party apps access your clipboard data.

Switching to Android won't save you, but switching to a feature phone might, if that's a sacrifice you're willing to make. Me? I just uninstalled basically all 3rd party iPhone apps and use [the Brave browser](https://apps.apple.com/us/app/brave-private-web-browser/id1052879175) or the [Firefox Focus browser](https://apps.apple.com/us/app/firefox-focus-privacy-browser/id1055677337) for everything.

It really is a jungle out there. Stay vigilant friends. Don't let the bad guys win. You can [follow me on Twitter for more no-nonsense security tips](https://www.twitter.com/ossia).

