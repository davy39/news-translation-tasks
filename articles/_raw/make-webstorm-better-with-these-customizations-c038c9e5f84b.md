---
title: Make WebStorm better with these customizations
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-03T17:28:08.000Z'
originalURL: https://freecodecamp.org/news/make-webstorm-better-with-these-customizations-c038c9e5f84b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oCrv_hHYKEzkVxS0zaVwwg.png
tags:
- name: how-to
  slug: how-to
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Victor Savkin

  In this blog post I will show how to make WebStorm look awesome, make it faster,
  and improve the dev ergonomics.

  Make WebStorm Look Awesome

  If you are asking yourself why is my WebStorm UI looks so much cooler than the default
  UI, th...'
---

By Victor Savkin

In this blog post I will show how to make WebStorm look awesome, make it faster, and improve the dev ergonomics.

#### Make WebStorm Look Awesome

If you are asking yourself why is my WebStorm UI looks so much cooler than the default UI, the answer is that I customized it.

To get the same look, do the following:

* Hide the toolbar and tool buttons. WebStorm is a keyboard-friendly environment, so there is absolutely no reason to have any buttons taking valuable real estate.
* [Install the Material UI theme plugin.](https://github.com/ChrisRM/material-theme-jetbrains) It looks gorgeous.
* Don’t settle for the default font. Use the one you really like. (e.g., I use [Operator Mono](http://www.typography.com/fonts/operator/styles/)).

#### Make WebStorm Fast

My WebStorm does not just look better, **it is faster as well**. If you feel the need for speed, do the following:

Open:

```
/Applications/WebStorm.app/Contents/bin
```

Open the idea.properties configuration file, and enable [the experimental zero-latency mode](https://blog.jetbrains.com/idea/2015/08/experimental-zero-latency-typing-in-intellij-idea-15-eap/) by adding the following line:

```
editor.zero.latency.typing=true
```

If you even felt that WebStorm is laggy comparing to text editors, the zero-latency mode will fix this.

Next, open webstorm.vmoptions. Bump up the max heap size to at least 3 gigabytes. Our dev machines have so much memory — might as well use it!

#### Secret Weapon: AceJump

![Image](https://cdn-media-1.freecodecamp.org/images/21TrsXyKsi9uLC4w8vSiMOkguI6IeYlLyxxq)

Finally, do yourself a favor and install the Ace Jump plugin. With it you can move your cursor anywhere on the screen with just two keystrokes. So no more “down down down down down right right right right’. To see it in action, [watch this video by](https://www.youtube.com/watch?v=yK8eM50DsAY) John Lindquist.

[Follow @victorsavkin](https://twitter.com/victorsavkin) to read more about Web Development.

_If you liked this, click the? below so other people will see this here on Medium._

