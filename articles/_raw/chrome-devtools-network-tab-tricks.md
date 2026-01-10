---
title: 'Chrome DevTools: How to Filter Network Requests'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T21:26:48.000Z'
originalURL: https://freecodecamp.org/news/chrome-devtools-network-tab-tricks
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a87740569d1a4ca2629.jpg
tags:
- name: browser
  slug: browser
- name: Google Chrome
  slug: chrome
- name: tips
  slug: tips
seo_title: null
seo_desc: "By Adeel Imran\nAs front end developers, most of our time is spent in the\
  \ browser with DevTools open (almost always, unless we are watching YouTube ...\
  \ sometimes even then). \nOne of the major sections in DevTools is the network tab.\
  \ There are a couple..."
---

By Adeel Imran

As front end developers, most of our time is spent in the browser with DevTools open (almost always, unless we are watching YouTube ... sometimes even then). 

One of the major sections in DevTools is the `network` tab. There are a couple of things you can do in the `network` tab, like the following:

* Find network requests by text
* Find network requests by regex expression
* Filter (exclude) out network requests
* Use the property filter to see network requests by a certain domain
* Find network requests by resource type

For the purposes of this tutorial I am using [freeCodeCamp's](https://www.freecodecamp.org/news/) home page, **[freecodecamp.org/news](https://www.freecodecamp.org/news/)**. Simply go to the page and open the `network` tab.

You can see the `network` tab by hitting `cmd + opt + j` on your Mac or `ctrl + shift + j` in Windows. It will open up the `console` tab in DevTools by default.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.18.37.png)
_Clicking "cmd + opt + j" opens up console panel in DevTools_

Once the `console` tab is open, simply click on the `network` tab to make it visible.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.19.57.png)
_Clicking on the "network" tab will show you all network requests being made for a certain page_

Once the `network` tab is open we can begin our tutorial.

## Let's begin

Make sure the correct page is open ([freecodecamp.org/news](https://www.freecodecamp.org/news/)) and the "network" tab panel is open in DevTools:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.12.01.png)
_Illustration on where the filter bar is in network panel._

* The green box here illustrates the icon that can hide/show the filter area in the network panel tab.
* The red box here illustrates the filter area box. With this box we can filter out network requests.

### Find network request by text

Type `analytics` into the Filter text box. Only the files that contain the text `analytics` are shown.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.47.38.png)

### Find network request by regex expression

Type `/.*\min.[c]s+$/`. DevTools filters out any resources with filenames that end with a `min.c` followed by 1 or more `s` characters.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.21.34.png)

### Filter (exclude) out network request

Type `-min.js`. DevTools filters out all files that contain `min.js`. If any other file matches the pattern they will also be filtered out and won't be visible in the network panel.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.51.50.png)

### Use property filter to see network request by a certain domain

Type `domain:code.jquery.com` into the filter area. It will only show network requests that belong to the URL `code.jquery.com`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-22.54.22.png)

### Find network request by resource type

If you only want to see which font(s) file is being used on a certain page click `Font`:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.03.41.png)
_Filtering network requests by "font" type files only_

Or if you only want to see the web socket files being loaded on a certain page click `WS`:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.05.55.png)
_Filtering network requests by "web socket" type files only_

You can also go one step further and view both `Font` & `WS` files together. Simply click on `Font` first and then `cmd` click on `WS` to multi-select tabs. (If you are on a Windows machine you can multi-select by using `ctrl` click).

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-02-at-23.08.48.png)
_Multi selecting multiple resource types by "cmd` click on types_

---

That is it for this tutorial. If you found it useful do share it with your colleagues and let me know what you think as well on [**twitter.com/adeelibr**](https://twitter.com/adeelibr)**.**

