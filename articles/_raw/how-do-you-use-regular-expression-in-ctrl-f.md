---
title: How to Use Regular Expressions in CTRL F
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-30T13:12:06.000Z'
originalURL: https://freecodecamp.org/news/how-do-you-use-regular-expression-in-ctrl-f
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/start-graph--6-.png
tags:
- name: Regex
  slug: regex
seo_title: null
seo_desc: 'The conventional CTRL + F does not support Regex in many software tools
  we use in our day-to-day lives. But almost nothing is impossible in the tech world.

  Many of these software tools, such as VS Code, Chrome browser, Dreamweaver, Jetbrains,
  and oth...'
---

The conventional `CTRL + F` does not support Regex in many software tools we use in our day-to-day lives. But almost nothing is impossible in the tech world.

Many of these software tools, such as VS Code, Chrome browser, Dreamweaver, Jetbrains, and others, have a built-in mechanism that supports RegEx while using `CTRL + F` to search a page or document.

Let’s look at how you can search with `CTRL + F` using RegEx in VS Code, Chrome browser, and Chrome developer tools.


## What We'll Cover
- [How to Use Regular Expressions in `CTRL + F` Inside VS Code](#heading-how-to-use-regular-expressions-in-ctrl-f-inside-vs-code)
- [How to Use Regular Expressions in `CTRL + F` in Chrome Developer Tools](#heading-how-to-use-regular-expressions-in-ctrl-f-in-chrome-developer-tools)
- [How to Use Regular Expressions in `CTRL + F` on a Chrome Webpage](#heading-how-to-use-regular-expressions-in-ctrl-f-on-a-chrome-webpage)
- [Conclusion](#heading-conclusion)


## How to Use Regular Expressions in `CTRL + F` Inside VS Code
Press `CTRL + F` and the search interface will appear:
![Screenshot-2023-03-30-at-11.09.19](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.09.19.png)

Hover on `.*` and “Use Regular Expression” with some keyboard combinations should appear:
![Screenshot-2023-03-30-at-11.10.50](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.10.50.png)

Anywhere you see the `.*` sign, it means RegEx. Click on it to start searching with RegEx.

Enter your RegEx and the search results show up:
![Screenshot-2023-03-30-at-11.17.13](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.17.13.png)

If the only thing you want to do with `CTRL + F` is to search using RegEx, the `ALT + CTRL + R` keyboard combination toggles `CTRL + F` search with RegEx on and off.


## How to Use Regular Expressions in `CTRL + F` in Chrome Developer Tools
You can also search using RegEx in the Chrome developer tools when you open a page source.

Right-click anywhere on a page and select “Inspect”:
![Screenshot-2023-03-30-at-11.22.21](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.22.21.png)

Click the 3 dots in the top right corner and select search to reveal the dev tools search interface:
![Screenshot-2023-03-30-at-11.23.01](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.23.01.png)

You can also press `CTRL + ALT + F` on Windows or `CMD + ALT + F` on Mac to do this.

Click on the `.*` button to search with RegEx:
![Screenshot-2023-03-30-at-11.24.59](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.24.59.png)

Type in your RegEx and press `ENTER` to reveal the search results:
![Screenshot-2023-03-30-at-11.27.20](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.27.20.png)


## How to Use Regular Expressions in `CTRL + F` on a Chrome Webpage
Since you can search with RegEx in the Chrome developer tools, you might be wondering how to search with RegEx on a web page. 

Although Chrome does not have this functionality built into it, you can install an extension to let you do so.

Head over to [Chrome Web Store](https://chrome.google.com/webstore/category/extensions) and search for RegEx:
![Screenshot-2023-03-30-at-11.33.27](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.33.27.png)

Install the Chrome RegEx search extension:
![Screenshot-2023-03-30-at-11.34.10](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.34.10.png)

Close and reopen your Chrome browser. Then head over to your extensions and select “Chrome Regex Search”:
![Screenshot-2023-03-30-at-11.39.34](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.39.34.png)

Enter your RegEx and the search results show up:
![Screenshot-2023-03-30-at-11.38.35](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-at-11.38.35.png)


## Conclusion
Even though a lot of software doesn’t come with a default `CTRL + F` search with RegEx, there is a way to either enable this functionality or install an extension.

VS Code and Google Chrome have this functionality built-in.

With Chrome developer tools, press `CTRL + SHIFT + F` on Windows and `CMD + SHIFT + F` on Mac, and then the same `.*` button to search with RegEx. You do the exact same in VS Code. 

On a web page, Chrome doesn’t support searching with `CTRL + F` by using RegEx, but you can download extensions that add this functionality.

If you’re using any other tool and want to search using RegEx, a quick web search will point you in the right direction.

Thanks for reading!


