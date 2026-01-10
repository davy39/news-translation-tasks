---
title: How to Inspect an Element – Chrome Shortcut
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-15T01:40:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-inspect-an-element-chrome-shortcut
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/inspect-element.png
tags:
- name: Google Chrome
  slug: chrome
- name: Developer Tools
  slug: developer-tools
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'The Inspect Element feature of the Google Chrome browser is a powerful
  yet easy-to-use tool.

  It’s an important part of Chrome Developer Tools that you can use to check the source
  code of any website.

  But it doesn’t end there. You can take things furt...'
---

The Inspect Element feature of the Google Chrome browser is a powerful yet easy-to-use tool.

It’s an important part of Chrome Developer Tools that you can use to check the source code of any website.

But it doesn’t end there. You can take things further by changing the elements and styles that make up the website – that is, the HTML, CSS, and JavaScript code of the website. This is why a lot of developers use the Inspect tool for debugging purposes.

If you’re a beginner in web development, the Inspect tool is a useful feature you can take advantage of to learn about how websites are built, the fonts, icons, and plugins used, and even who made the website.

The good news is that you don’t need to be the developer of the website to use this powerful tool as it is available to users as well. You don’t even need to be a developer at all to use it.

In this article, you will learn how to open the Chrome Developer Tools so you can get access to the Inspect feature, and how to inspect specific elements on a website. I will also show you how you can manipulate the elements of a website by changing the texts and styles.

I'll be using freeCodeCamp.org to show you how things work with the Inspect tool.

## How to Open the Chrome Developer Tools
To open the Chrome Developer Tools, click the vertical dots at the top-right corner of your browser:
![ss1-3](https://www.freecodecamp.org/news/content/images/2022/04/ss1-3.png)

Then hover over “More tools” and select “Developer tools”:
![ss2-5](https://www.freecodecamp.org/news/content/images/2022/04/ss2-5.png)

You will then get access to the tabs of the developer tools such as Elements (the HTML and CSS that makes up the website), Console with which you can run JavaScript, Sources, and many more.

You can drag these tabs around and place them wherever you want:
![drag](https://www.freecodecamp.org/news/content/images/2022/04/drag.gif)

## How Do I Open Inspect Element in Chrome with the Keyboard?
You can open the Inspect element tool on Linux by pressing `CTRL` + `SHIFT` + `C` or `F12` on Windows.

If you are on Mac, press `Command` + `SHIFT` + `C`.

## How to Inspect Specific Elements on a Website 
To inspect any element you see on a website, whether it's text, a button, a video, or an image, right-click on the element and click “Inspect”. 

In this case, I will right-click on the “Learn to code – for free” text on the freeCodeCamp.org landing page.
![ss3-3](https://www.freecodecamp.org/news/content/images/2022/04/ss3-3.png)

The source code will open and the element will be highlighted for you, like this:
![ss4-2](https://www.freecodecamp.org/news/content/images/2022/04/ss4-2.png)

You can see the text is an `h1` element.

## How to Manipulate the Elements of a Website with the Inspect Tool
You can change the text contents of a website with the Inspect tool. 

As an example, I’m going to change the “Build projects” text on the freeCodeCamp.org landing page to “Build real-world projects”.

To do this, right-click on the element you would like to change and click “Inspect”. In this case, it's the “Build projects” text:
![ss5-2](https://www.freecodecamp.org/news/content/images/2022/04/ss5-2.png)

Double-click on the “Build projects” text:
![ss6-2](https://www.freecodecamp.org/news/content/images/2022/04/ss6-2.png)

Type in “Build real-world projects” and hit `ENTER`:
![ss7-1](https://www.freecodecamp.org/news/content/images/2022/04/ss7-1.png)

![ss8-1](https://www.freecodecamp.org/news/content/images/2022/04/ss8-1.png)
You can see the text has been changed to “Build real-world projects”.

## How to Change Styles with the Inspect Tool
Let’s change the background of the “Get started (it’s free)” button to my favorite color – #2ecc71.

Right-click on the button and select “Inspect”:
![ss9-1](https://www.freecodecamp.org/news/content/images/2022/04/ss9-1.png)

Double-click on the value of the “background-image” property on the right, that is `linear-gradient(#fecc4c,#ffac33)`.

Change the colors to `#2ecc71,#2ecc72` and hit `ENTER`:
![ss10-1](https://www.freecodecamp.org/news/content/images/2022/04/ss10-1.png)
You can see the background of the button has changed.

We have now made 2 changes on the freeCodeCamp.org landing page – we changed the “Build projects” text to “Build real-world projects” and we changed the background of the “Get Started (it’s free)” button:
![ss11-1](https://www.freecodecamp.org/news/content/images/2022/04/ss11-1.png)

## Are the changes you make with the Inspect tool permanent?
No. Any change you make with the Inspect tool is not permanent. Once you reload the page, the changes are gone.

This is because the website has been deployed to a server. So when you make another request to that server by reloading the page, the content from the server is loaded by your browser.

So don't worry - you playing around in this way with the Inspect tool won't change a website permanently. It just helps you learn more about it and practice your coding :)

## Conclusion
This article showed you how to get access to the Developer tools of Google Chrome, how to use its Inspect feature to view the source code of a website, and how to change the elements and styles of a website with it.

If you just started learning to code in HTML, CSS, and JavaScript, the Inspect feature of Chrome Dev tools is a powerful tool you can use to view the source code of any website so that you can learn about how they are built.  

Thank you for reading.


