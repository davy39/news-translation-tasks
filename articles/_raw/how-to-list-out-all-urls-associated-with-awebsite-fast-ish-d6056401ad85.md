---
title: How to List Out All URLs Associated With a Website Fast-ish
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T22:22:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-list-out-all-urls-associated-with-awebsite-fast-ish-d6056401ad85
coverImage: https://cdn-media-1.freecodecamp.org/images/1*L9q9fUiFwwYYJ49EzTH65g.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: terminal
  slug: terminal
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ty Irvine

  So you need a list containing all the URLs for a website? Are you doing some redirects
  perhaps? Hit the limit on XML Sitemaps? Cool, me too. I’ve got just the tool for
  you that’ll get it done at about the same speed as XML Sitemaps, but ...'
---

By Ty Irvine

So you need a list containing all the URLs for a website? Are you doing some redirects perhaps? Hit the limit on [XML Sitemaps](https://www.xml-sitemaps.com/)? Cool, me too. I’ve got just the tool for you that’ll get it done at about the same speed as XML Sitemaps, but you’ll look way cooler doing it.

### Where the tutorial actually starts

To get your list of URLs, we’re going to use Wget!

### What the Frigg is Wget?

> _“Wget is a free software package for retrieving files using HTTP, HTTPS, and FTP, the most widely-used Internet protocols.” — [Brew ‍Formulas](https://brewformulas.org/wget‍)_

And you can also use it to request a big list of URLs associated with a domain.‍

### ‍1. Installing Wget

To install Wget if you haven’t already, you’re going to need first to install [HomeBrew](https://brew.sh/); aka Brew. ? Brew is a package manager, meaning it installs software for you and manages it. You can check out the instructions on their website or just follow the ones below.

#### Install Brew

Paste this into a Terminal Prompt and hit enter twice ⮐ (It may ask you for a password.)

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"‍
```

#### Install Wget

Now that you have Brew installed it’s time to install Wget. Paste this into a Terminal Prompt and hit enter ⮐

```
brew install wget
```

### 2. Time To Get ‘Dem URLs‍

Now with Wget installed we simply download the website and then display all of its URLs. Start by downloading the website you’d like with

```
Wget -r www.shutterandcode.com
```

Then once the download is complete we’ll list out the URLs with

```
Find www.shutterandcode.com
```

(Make sure to use the same website domain as what was downloaded).

![Image](https://cdn-media-1.freecodecamp.org/images/9ikDkfbIscUaE5AuL01lIhNmIYWZ5YWXqUKV)
_3.7s download time_

#### Conclusion

After a series of casual tests pitting Wget against XML Sitemaps using smaller websites, I found that they are both pretty much on par with each other. Occasionally one would be faster than the other but overall they both had similar speeds.‍

If you’d like to know more about Wget commands simply type this into your prompt

```
wget --help
```

I hope you enjoyed reading this! Don’t forget to like, comment, and subscribe! ?

p.s. don’t actually feel obligated to like, comment, and or subscribe because it is simply a joke for YouTubers :)

> **_UPDATE: if you don’t want the site actually to download to your computer add in ‘ — spider’ after ‘wget’ like_**

```
wget -r --spider www.example.com
```

_Check out the original post and the rest of the Snippets! series at_

[_Shutter&Code — Le Blog_](https://www.shutterandcode.com/post/snippets-list-out-all-urls-associated-with-a-website-fast)

