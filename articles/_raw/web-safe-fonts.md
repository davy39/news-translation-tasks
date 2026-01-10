---
title: CSS Font Family and Web Safe Fonts Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-15T19:20:00.000Z'
originalURL: https://freecodecamp.org/news/web-safe-fonts
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c93740569d1a4ca32fe.jpg
tags:
- name: fonts
  slug: fonts
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Web Safe Fonts

  Web safe fonts are fonts that are included with most operating systems, the implication
  of such high availability is that a designer can expect typography involving web
  safe fonts to appear exactly as intended to most users. Below are ...'
---

## **Web Safe Fonts**

Web safe fonts are fonts that are included with most operating systems, the implication of such high availability is that a designer can expect typography involving web safe fonts to appear exactly as intended to most users. Below are non-exhaustive lists of some fonts that are considered web safe at the time of writing, categorized by CSS generic font families.

Web safe serif fonts:

* Georgia
* Times New Roman

Web safe sans-serif fonts:

* Arial
* Tahoma
* Trebuchet MS
* Verdana

Web safe monospaced fonts:

* Courier New

It is worth noting that font stacks with fallback options including a generic font family should still be used even if your design uses only web safe fonts. For example:

```css
p {
  font-family: Tahoma, Arial, sans-serif;
}
```

#### **A Note on Web Fonts**

Just because some fonts are safer than others does not mean you should confine your designs to using only web safe fonts. Modern designs with CSS can also take advantage of web fonts to ensure consistent typography across operating systems.

## More info on fonts:

* [How to load web fonts correctly](https://www.freecodecamp.org/news/web-fonts-in-2018-f191a48367e8/)
* [Google font superfamilies](https://www.freecodecamp.org/news/low-hanging-design-fruit-why-you-should-use-google-font-superfamilies-1dae04b2fc50/)
* [How to use Google Fonts in your next design project](https://www.freecodecamp.org/news/how-to-use-google-fonts-in-your-next-web-design-project-e1ad48f1adfa/)

