---
title: How to Block Annoying Content From Web Pages Using uBlock Origin
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-08-24T19:39:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-block-content-from-web-pages-using-ublock-origin
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/untitled-1.png
tags:
- name: Browsers
  slug: browsers
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'You can use extensions in your browser to remove parts of a webpage you
  don''t want to see. Removing annoyances, distractions, and irrelevant content is
  a great way to stay focused and remain efficient while you consume information on
  the internet.

  Th...'
---

You can use extensions in your browser to remove parts of a webpage you don't want to see. Removing annoyances, distractions, and irrelevant content is a great way to stay focused and remain efficient while you consume information on the internet.

There are many extensions that add this functionality to your browser. I'll be focusing on [uBlock Origin,](https://ublockorigin.com/) as many will already have it. If you don't, then I'd strongly recommend installing it.

## What is uBlock Origin?

[uBlock Origin](https://ublockorigin.com/) is a free and open-source ad blocker available for all major browsers. It also includes an [element picker](https://github.com/gorhill/uBlock/wiki/Element-picker) tool that can remove custom elements, which is what we'll be using in this article.

Having knowledge of CSS selectors or XPath will help you go through this tutorial, but isn't required. uBlock Origin provides visual tools to select elements without technical knowledge. Still, writing the selector manually will usually be more reliable.

## Why Blocking Elements Is Useful

On the internet, we're constantly consuming information, but quite often it's information that simply isn't relevant to us.

If you access particular websites frequently, it can be a big boost to productivity if you can conditionally single out the information you know you won't need and never consume it in the first place.

* Removing certain types of events from activity or social media feeds.
    
* Removing popups that ask you to do things you don't want to.
    
* Removing posts from particular authors on YouTube or social media.
    
* Removing distractions or dynamic elements that draw your attention.
    

## How to Filter HTML Elements

To filter elements, you can click the uBlock Origin icon at the top of your browser, then click the element picker, the one with the eye drop icon. ([More Info](https://github.com/gorhill/uBlock/wiki/Element-picker))

![The uBlock Origin interface, it contains all actions that can be performed such as blocking media, fonts, or elements on the current page.](https://www.freecodecamp.org/news/content/images/2021/08/Untitled.png align="left")

*The uBlock Origin interface, this appears if you click the icon in your browser's toolbar.*

You can start by selecting the content you want to remove. Even if the selection isn't perfect, it's just a starting point.

Once the box appears at the bottom-right, you can use the visual tools with the "Pick" button and sliders, or manually specify a selector.

The content highlighted in red is what will be removed once you select the "Create" button. These changes will persist even after refreshing or revisiting the page at a later date. Let's see how this works.

### CSS Selectors

You can remove most elements you want to remove easily using CSS selectors. This is great for removing static content on the page.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-93.png align="left")

*Removes all release and push events from appearing in my GitHub activity feed. (*`##div.news div.release, div.news div.push`)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-85.png align="left")

*Removes the banner to download Slack. (*`##.p-client__banners`)

### XPath

You'll usually want to use XPath for one of two reasons:

* You need to check against the value of an element.
    
* You need to select an element based on the attributes of its children.
    

This is useful for removing dynamic or user-generated content. We want to remove the entire element, but only if something inside it matches the criteria rather than the element itself.

![Using the uBlock Origin cosmetic filter tool to highlight all elements that would be deleted from my current selection.](https://www.freecodecamp.org/news/content/images/2021/08/image-57.png align="left")

*Removes all plugins from DevilBro. (*`##:xpath(//a[./div/div/p/object/a = "DevilBro"])`)

![Using the uBlock Origin cosmetic filter tool to remove all elements I don't want to see. The site now displays as if they were never there.](https://www.freecodecamp.org/news/content/images/2021/08/image-58.png align="left")

*How it looks after removing all plugins by DevilBro.*

### Troubleshooting your filters

When filtering elements, your selectors can break at any time. Websites change for various reasons, in most cases due to maintenance or updates.

Don't let that deter you from doing what you want, though. It just means you should keep this in mind when you remove elements.

Try to keep your selectors local to what you actually want to remove, but strict enough that it won't falsely select other elements on the page.

There are also many websites that don't appreciate client-side modifications, and try to hinder this by arbitrarily changing HTML attribute values or obfuscating them.

In these cases, it's best to specify [CSS attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) or use XPath to partially match attribute values.

![Selecting the "Active Now" view on Discord using a CSS attribute selector. The "Active Now" component is highlighed in red to indicate it will be removed.](https://www.freecodecamp.org/news/content/images/2021/08/image-91.png align="left")

*Removing the "Active Now" view on Discord using an attribute selector, (*`##div[class^="nowPlayingColumn"]`)

### How to Remove Filters

If you no longer want to block something, or the website has changed, you can go to the settings to remove the old filter before making a new one.

To remove a custom filter:

1. Navigate to the uBlock Origin settings.
    
2. Select the "My filters" tab.
    
3. Delete the lines with the filter(s) you want removed.
    
4. Click "Apply changes" at the top.
    
5. Refresh the page you were on.
    

## Other Helpful Browser Extensions

There are other extensions you can use to remove specific types of content on websites, too.

### Highlight or Hide Search Engine Results

[Highlight or Hide Search Engine Results](https://github.com/pistom/hohser) (HOHSER) supports all major search engines, including [DuckDuckGo](https://duckduckgo.com/) and Google.

I believe domain blacklisting should be a native user-setting available in search engines, but until that's a thing, you can use this extension to hide results under domains you don't like.

* Websites with re-hosted or shady download links.
    
* Search engine optimized junk, like fake coupon websites.
    
* Websites that block users in the EU.
    

### I still don't care about cookies

[I still don't care about cookies](https://github.com/OhMyGuus/I-Still-Dont-Care-About-Cookies) removes cookie warnings from appearing on most websites, that way you don't have to deal with them yourself.

The extension will attempt to hide the cookie message, only accepting cookies if necessary.

I strongly recommend only using this in combination with extensions like uBlock Origin and Privacy Badger, to prevent undesirable cookies from being saved.

## Conclusion

I hope you're not in a situation where you feel the need to block a significant amount of content from the pages you load.

But if you do feel the need, I hope this makes browsing the internet just a little more bearable for you.
