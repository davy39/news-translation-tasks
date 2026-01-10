---
title: My Favorite Chrome Dev Tools Tips and Tricks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-10T16:56:03.000Z'
originalURL: https://freecodecamp.org/news/awesome-chrome-dev-tools-tips-and-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/cover_image.png
tags:
- name: Google Chrome
  slug: chrome
- name: Developer Tools
  slug: developer-tools
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dor Shinar

  Chrome Developer Tools are a super powerful suite of tools for developing web applications.
  They can do so much, from very basic operations like traversing the DOM, to checking
  out network requests or even profiling your application''s p...'
---

By Dor Shinar

Chrome Developer Tools are a super powerful suite of tools for developing web applications. They can do so much, from very basic operations like traversing the DOM, to checking out network requests or even profiling your application's performance.

Among the big, everyday features they enable, there are quite a lot of gems to be found if you look deep enough. Features that might save you a click or two – and isn't that what we're all about here?

## jQuery style DOM queries in the console

jQuery is awesome. It has ruled the web for over a decade, and some statistics state that [more than 70% of the most popular web pages in the world](https://en.wikipedia.org/wiki/JQuery#Popularity) run some version of jQuery. That's crazy for a library dating all the way back to 2006.

The most popular API jQuery provides is the `$`, used for selecting DOM elements. The Chrome dev tools console allows you to make use of that `$` selector, and more. Under the hood, `$` is an alias to `document.querySelector()`.

For example, if you want to simulate a click on an element you can do:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/--selector.png)
_Using the $ selector to click a button_

Similarly, `$$` is an alias to `document.querySelectorAll()`:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/---selector.png)
_Using the $$ selector to print class names_

There are a few more tricks up the `$` sleeve. Sometimes, a selector might be too complicated to write by heart, or you just don't know a selector specific enough. If you pick an element in the Elements tab you can retrieve it with the `$0` variable in the console:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/-0-selector.gif)
_A gif showing usage of the $0 selector in console_

The console goes even further, allowing us to access not only the last selection, but the last 5, in order. The selections are exposed through the `$0` - `$4` variables:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/-0-4-selector.gif)
_A gif showing usage of the $0 - $4 selector in console_

## Copying an element's properties

The elements tab is a really useful tab. It stores our website DOM tree, it allows us to see the CSS applied to each element, and we can make changes to elements on the fly from it.

A really cool trick I've found is the ability to copy properties of an element (and not only properties) from the context menu.

For example, you can copy an element's selector:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/copy-selector.gif)
_A gif showing how to copy an element's selector_

This selector might not be specific enough, or too specific for production, but should make your life a little easier when debugging.

As you can see in the previous gif, the copy context menu hides a few more nifty things you can copy. You can copy the element's styles, JS path (`document.querySelector(SELECTOR)`) or XPath.

## Filtering network requests

Sometimes, you work on a page that has a lot of requests. I mean, A LOT.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/lots-of-requests.gif)
_Scrolling through very long list of network requests_

Working your way through all those requests can be difficult when you look for something specific. Thankfully, you can very easily filter the requests.

The filter toolbar has quick toggles for various request types, such as XHR/Fetch, stylesheets, JS scripts, images and more:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/toolbar-filters.gif)
_Using toolbar filters to filter network requests_

If you need to be even more specific, or so that you might find it quicker, you can just write a filter criteria in the `filter` input right above the toolbar to search in the requests' names:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/filter-by-name.gif)
_Filtering network requests by name_

## Emulating different network speeds

Using the `Network` tab again we can test our site in various internet speeds. The default preset is `online`, and you'll enjoy the full bandwidth of your internet connection.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/network-speed-menu.png)
_A menu allowing selection of various internet speeds_

Besides `online`, there are a few more presets available: `Fast 3G`, `Slow 3G` and `offline`, which vary in upload speed, download speed and latency. If you need to emulate a different, more exotic speed, you can add your own profile through the `Add...` button:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/custom-throttling-profile.png)
_Adding a custom throttling profile_

## Using Live Expressions in console

What are `Live Expressions`?

`Live Expressions` are expressions which evaluate constantly at the top of your console. Say, you want to track a variable's value over time. You can log it over and over and over again:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/print-over-and-over.png)
_Printing a variable over and over again_

With `Live Expressions`, you can focus on your code, and let Chrome do the monitoring:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/live-expression.gif)
_Storing a variable in a live expression_

This applies for variables defined both in the console and in a script.

## Emulating different devices

Those of us working on responsive applications know the feeling where you work really hard to make a beautiful layout, only to see it misbehave on devices with different resolutions.

I'm not here to tell you about media queries, but rather a convenient way to test that they work.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/dev-tools-topbar.png)
_A button to toggle device view_

When you click on the button that looks like a tablet and a phone, you'll see that your browser's viewport changes to reflect a different device's dimensions.

You can choose a device from a list of presets containing various popular devices, such as iPhone X, iPad Pro, Pixel 2, Pixel 2 XL and more. The list is admittedly a bit outdated, but I think it's good enough for most cases.

If you can't find a device that fits your needs, you can set a custom resolution. As you can see, I've set a custom resolution to emulate a OnePlus 6 (which is my daily driver).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/oneplus-6.png)
_OnePlus 6 simulated device_

## Forcing an element's state

Have you ever faced a situation where you wanted to play with an element's `:hover`-specific CSS, but every time you moved your mouse to the styles section in the dev tools the element was no longer hovered?

Well, Chrome dev tools exposes a nice way to lock an element's state, so you can fiddle with its properties with peace. This way you can quickly toggle an element's `:active`, `:hover`, `:focus`, `:focus-within` and `:visited` properties:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/toggle-state.png)
_A menu for toggling an element's state_

Those are my tips and tricks I think everyone can benefit from. Thank you for reading!

This article was previously published on my blog: [dorshinar.me](https://dorshinar.me/themes-using-css-variables-and-react-context). If you want to read more content, you can check out my blog as it would mean a lot to me.

If you want to support me, you can <a href='https://ko-fi.com/L3L116P44' target='_blank'><img height='36' style='left:0;border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>


