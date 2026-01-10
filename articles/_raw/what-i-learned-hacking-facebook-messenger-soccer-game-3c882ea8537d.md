---
title: What I learned hacking the Facebook Messenger Soccer game
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-25T17:40:49.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-hacking-facebook-messenger-soccer-game-3c882ea8537d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hPTxPQeHPxLnPBOg8ryWpQ.jpeg
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Flavio De Stefano

  Recently, during last European Football Championship, Facebook introduced a little
  game in the Messenger app that makes you lose hours and hours despite its simplicity.

  If you didn’t notice it, read this article on Mashable.

  I ha...'
---

By Flavio De Stefano

Recently, during last European Football Championship, Facebook introduced a little game in the Messenger app that makes you lose hours and hours despite its simplicity.

If you didn’t notice it, read [this article](https://mashable.com/2016/06/15/facebook-messenger-soccer-game-how-to/#fmGutFmQ3Oqx) on Mashable.

I have to admit… I totally suck at this game, so my best score was **9**_._

But, as a Developer, the best thing I could do was to beat my friends by hacking the game.

_I really thought this would be simple._

#### The first way: Listen to HTTP(s) requests

While developing apps, you immediately realize that you need an HTTP debugger tool to analyze incoming /outgoing traffic for you APIs.

[**Charles**](https://www.charlesproxy.com/) is the best tool I’ve found to accomplish this task. It has a very intuitive interface and you can easily use it for debugging and reverse engineering purposes.

It was supposed to end at this point: I would have to analyze the API that the Facebook app used and just replay it with CURL while editing the data and the score sent to the server.

Of course, the API calls are in HTTPS, so they’re encrypted.. but _Charles can be used as a man-in-the-middle HTTPS proxy,_ enabling you to view in plain text the communication between web browser and SSL web server_._

![Image](https://cdn-media-1.freecodecamp.org/images/1*rHRhqfl0hZSYHdEsrJLF_A.png)
_Charles acting as a proxy — with failed requests_

Perfect! So I installed the root Charles certificate on the iPhone, and I tried to inspect the traffic. But all HTTP calls to the Facebook servers were denied upfront during the SSL handshake phase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mjd0P2T-huqFhck7Ii3alA.gif)
_SSL - image courtesy of cisco.com_

Doing some research, I discovered that some company apps like Facebook and Google use an extra layer of security to ensure that the certificate provided by the remote server is the one which is expected. This technique is called **Certificate Pinning.**

You can easily do this by including the public key of the remote server certificate within the application, so that it’s easy to validate the identity of the client for each HTTPS request.

This technique invalidates the [Man in the Middle (MITM)](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) Attack.

Great job Facebook! But…(remember, there’s always a but) there is a way to disable the **SSL certificate pinning** using some system tweaks only available on a jail broken device.

#### The first way (enhanced): Jailbreak a device and install iOS SSL Kill Switch

My iPhone is currently running iOS 9.x, so at the time of this writing it was impossible to jailbreak. So I took an old iPad mini running iOS 8.3.x and easily jailbroke it using the [TaiG](http://www.taig.com/en/) tool**.**

Searching on the web, I found [SSL Kill Switch 2](https://github.com/nabla-c0d3/ssl-kill-switch2), a Blackbox tool to disable SSL certificate validation within iOS and OS X apps.

Once loaded into an iOS or OS X App, SSL Kill Switch 2 patches specific low-level SSL functions within the Secure Transport API in order to _override, and disable the system’s default certificate validation as well as any kind of custom certificate validation_ (such as certificate pinning).

The SSL Kill Switch uses [MobileSubstrate](http://iphonedevwiki.net/index.php/MobileSubstrate) to patch system functions like the [Secure Transport API](https://developer.apple.com/library/ios/DOCUMENTATION/Security/Reference/secureTransportRef/Reference/reference.html). They are the lowest-level TLS implementation on iOS.

This means that disabling SSL certificate validation in the Secure Transport API should affect most (if not all) of the network APIs available within the iOS framework.

Please, do yourself a favor and follow [this blog](https://nabla-c0d3.github.io/) that covers all these concepts.

So, I connected to the iPad using SSH and installed the package:

```
wget https://github.com/nabla-c0d3/ssl-kill-switch2/releases/download/0.10/com.nablac0d3.SSLKillSwitch2_0.10.deb --no-check-certificatedpkg -i com.nablac0d3.SSLKillSwitch2_0.10.debkillall -HUP SpringBoard
```

Once rebooted, I expected to see the plain traffic, but it was an optimistic vision: _I got the same errors._

I tried this way for another hour. I read somewhere that Facebook and Twitter use the SPDY protocol for their API calls, and this could be a problem for Charles. So I installed another tweak that (theoretically) disabled the SPDY protocol, but it didn’t work.

_Starving._

Looking at the project issues, I noticed that someone else had the same problem ([https://github.com/nabla-c0d3/ssl-kill-switch2/issues/13](https://github.com/nabla-c0d3/ssl-kill-switch2/issues/13)), with no resolution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UlNOgv5rpOId_yvnggV3hQ.png)

_Pause._

#### The second way: Simulate touch events within the application

I realized that there are many game cheats that use a “human” approach: _simulate touch events_ (one of the most popular games that many game cheats utilize this strategy on is Clash of Clans).

Browsing the web for a tool that automates these operations, I found this awesome tweak - [AutoTouch](https://autotouch.net/). It can record human touch events and store the data in a LUA script. You can then edit this produced script and simulate whatever you want anywhere on your device.

Once installed with [Cydia](https://cydia.saurik.com/), I saved a BMP screenshot of the Messenger application with the ball visible and obtained the coordinates of where to click.

![Image](https://cdn-media-1.freecodecamp.org/images/1*inmRf5q2zYXB4IAMZYvwrw.png)
_Screenshot made to obtain the coordinate_

What I thought is that, by clicking _exactly_ in the center of X axis of the ball, I only had to simulate repetitive touch events in the same coordinates and then stop the script when I had a score that I was satisfied with.

Here’s what I wrote to accomplish this goal:

```
adaptResolution(768, 1024);adaptOrientation(ORIENTATION_TYPE.PORTRAIT);
```

```
for i=1,2000 do
```

```
  touchDown(1, 544, 954);  usleep(66000);  touchUp(1, 544, 954);
```

```
  usleep(10000);
```

```
end
```

Nope, it didn’t work.

Probably, Facebook developers introduced a random error on touch coordinates to better simulate the game, or to prevent these type of scripts.

_Or, maybe I just clicked at the wrong pixel._

So, for a second chance, I tried to simulate multiple clicks in a larger area, but without luck. Sometimes, I simulated so many touch events that the Springboard _just crashed_ because of memory errors_._

Instead of clicking in the same coordinates every time, I tried a better approach.

Reading the AutoTouch [documentation](https://autotouch.net/server/doc/en.html), I found the following two methods:

* findColor (color, count, region) - Search the coordinates of the pixel points matching the specified color on the current screen.
* getColor (x, y) - Get the color value of the pixel point of the specified coordinate on the current screen.

The idea was to find a unique color inside the ball, and use the _findColor_ method to get the coordinates of the ball in that moment, to simulate a touch event.

```
adaptResolution(768, 1024);adaptOrientation(ORIENTATION_TYPE.PORTRAIT);
```

```
local c = getColor(544, 954);
```

```
for i=1,2000 do  local r = findColor(c, 0, {400, 500, 768, 1024});
```

```
  for i, v in pairs(r) do    touchDown(1, v[1], v[2]);    usleep(66000);    touchUp(1, v[1], v[2]);    usleep(10000);  end
```

```
end
```

I don’t know why, but it simply didn’t work. Maybe the _findColor_ is too slow to intercept the ball, which then makes the script useless.

#### The third way: Reverse engineer the app

I don’t have good native skills in Objective C, but I remember (when I played with the jailbreak ~4 years ago) that there was a tool by [Saurik](https://twitter.com/saurik?lang=en) that could inject itself into iOS processes.

It is released along with Cydia and was called [Cycript](http://www.cycript.org/). _It allowed developers to explore and modify running applications on iOS, by injecting code at run time._

I read some basic tutorials on how to use it, and after a few struggles, I decided to follow this (another) way.

Once you login via SSH into your iOS device, you can easily attach to a process just by typing:

```
cycript -p Messenger
```

I tried to inspect some basic UI classes like _UIApp_, but didn’t find anything interesting. Then I made a complete **class dump**, filtering it for the keyword **soccer.**

```
var C = Object.keys(ObjectiveC.classes);var soccer_classes = []; for (var i = 0; i < C.length; i++)  C[i].match(/soccer/i) && soccer_classes.push( C[i] );
```

It was a slow process.

I [discovered](https://www.reddit.com/r/programming/comments/3h52yk/someone_discovered_that_the_facebook_ios/) that Facebook Messenger has a very large number of classes.

But, in the end, I got a small list.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xiOhf1t00RNyXa_o8m7Hnw.png)
_Output of the script_

Once I obtained the class names, I used a script to print all methods of the class, and, by inspecting the **_MNSoccerGame_** class, the resulting methods were:

![Image](https://cdn-media-1.freecodecamp.org/images/1*VnA--gnGj5wO3ZcF4C8EUQ.png)
_The methods dump of the MNSoccerGame class_

> Note: I still don’t understand what is the method _wasCheatDetected._

Now that I had a complete list of the class methods, I decided to override the __setScore_ method, hoping that other methods didn’t notice that.

To do this, I used the **MobileSubstrate** and its **MS.hookMessage** method.

```
@import com.saurik.substrate.MS; 
```

```
var _setScore_pointer = {}; MS.hookMessage(MNSoccerGame, @selector(_setScore:), function(arg0) {  return _setScore_pointer->call(this, 9999); }, _setScore_pointer);
```

Now you can just play, **lose**, and **anyway score a new record.**

#### What I learned

Never stop yourself. Always try and discover new way to accomplish the same thing. I know, it’s just a game, but if you treat the problem you’re trying to solve like a challenge, you’ll get much more than the satisfaction of beating your friends.

