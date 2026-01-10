---
title: HTML URL Encoded Characters Reference
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T21:50:00.000Z'
originalURL: https://freecodecamp.org/news/url-encoded-characters-reference
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d67740569d1a4ca3792.jpg
tags:
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
- name: url
  slug: url
seo_title: null
seo_desc: 'A URL is an address for a website. Just like postal addresses have to follow
  a specific format to be understood by the postman, URLS have to follow a format
  to be understood and get you to the right location.

  There are only certain characters that ar...'
---

A URL is an address for a website. Just like postal addresses have to follow a specific format to be understood by the postman, URLS have to follow a format to be understood and get you to the right location.

There are only certain characters that are allowed in the URL string, alphabetic characters, numerals, and a few characters `; , / ? : @ & = + $ - _ . ! ~ * ' ( ) #` that can have special meanings.

## Reserved Characters

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.55.13-PM.png)

## Encoding

Any character that is not an alphabetic character, a number, or a reserved character being used needs to be encoded.

URLs use the ASCII (“American Standard Code for Information Interchange”) character-set and so encoding must be to a valid ASCII format.

There are functions in most web languages to do this encoding for you, for example in JavaScript `encodeURI()` and in PHP `rawurlencode()`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.57.33-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.57.53-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.06-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.18-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.32-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.43-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.57-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.07-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.18-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.27-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.46-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.55-PM.png)

### Example:

```js
encodeURI(Free Code Camp);
// Free%20Code%20Camp
```

