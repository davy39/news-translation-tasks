---
title: The Ultimate Guide to Web Scraping with Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T00:32:03.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-web-scraping-with-node-js-daa2027dcd3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KkVKtysvgh2hIVRI1Irk-Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By Daniel Ni

  So what’s web scraping anyway? It involves automating away the laborious task of
  collecting information from websites.

  There are a lot of use cases for web scraping: you might want to collect prices
  from various e-commerce sites for a pr...'
---

By Daniel Ni

So what’s web scraping anyway? It involves automating away the laborious task of collecting information from websites.

There are a lot of use cases for web scraping: you might want to collect prices from various e-commerce sites for a price comparison site. Or perhaps you need flight times and hotel/AirBNB listings for a travel site. Maybe you want to collect emails from various directories for sales leads, or use data from the internet to train machine learning/AI models. Or you could even be wanting to build a search engine like Google!

Getting started with web scraping is easy, and the process can be broken down into two main parts:

* acquiring the data using an HTML request library or a headless browser,
* and parsing the data to get the exact information you want.

This guide will walk you through the process with the popular Node.js [request-promise](https://github.com/request/request-promise) module, [CheerioJS](https://github.com/cheeriojs/cheerio), and [Puppeteer](https://github.com/GoogleChrome/puppeteer). Working through the examples in this guide, you will learn all the tips and tricks you need to become a pro at gathering any data you need with Node.js!

We will be gathering a list of all the names and birthdays of U.S. presidents from Wikipedia and the titles of all the posts on the front page of Reddit.

First things first: Let’s install the libraries we’ll be using in this guide (Puppeteer will take a while to install as it needs to download Chromium as well).

### Making your first request

<script src="https://gist.github.com/scraperapi/416fa822eb16e93222b0a836514ca99a.js"></script>


Next, let’s open a new text file (name the file potusScraper.js), and write a quick function to get the HTML of the Wikipedia “List of Presidents” page.

<script src="https://gist.github.com/scraperapi/10273ecc0a32cf9110cfcb2e443b4a14.js"></script>

Output:

<script src="https://gist.github.com/scraperapi/140aa0442cf8cc276bf72ce8f4722702.js"></script>

### Using Chrome DevTools

Cool, we got the raw HTML from the web page! But now we need to make sense of this giant blob of text. To do that, we’ll need to use Chrome DevTools to allow us to easily search through the HTML of a web page.

Using Chrome DevTools is easy: simply open Google Chrome, and right click on the element you would like to scrape (in this case I am right clicking on George Washington, because we want to get links to all of the individual presidents’ Wikipedia pages):

![Image](https://cdn-media-1.freecodecamp.org/images/1*gLKhu_EO-cDqYna1P9WL_w.png)

Now, simply click inspect, and Chrome will bring up its DevTools pane, allowing you to easily inspect the page’s source HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HSUjFgji22vjwvGi2uZe1A.png)

### Parsing HTML with Cheerio.js

Awesome, Chrome DevTools is now showing us the exact pattern we should be looking for in the code (a “big” tag with a hyperlink inside of it). Let’s use Cheerio.js to parse the HTML we received earlier to return a list of links to the individual Wikipedia pages of U.S. presidents.

<script src="https://gist.github.com/scraperapi/104d72fcbcdc2b86af9f44dadca1cde4.js"></script>

Output:

<script src="https://gist.github.com/scraperapi/6bf511c579433289b8e7abd426ef0534.js"></script>

We check to make sure there are exactly 45 elements returned (the number of U.S. presidents), meaning there aren’t any extra hidden “big” tags elsewhere on the page. Now, we can go through and grab a list of links to all 45 presidential Wikipedia pages by getting them from the “attribs” section of each element.

<script src="https://gist.github.com/scraperapi/63be1711b6b7d2ee771095777791d049.js"></script>

Output:

<script src="https://gist.github.com/scraperapi/5be18aa131e2a224f13f79b9d47b830b.js"></script>

Now we have a list of all 45 presidential Wikipedia pages. Let’s create a new file (named potusParse.js), which will contain a function to take a presidential Wikipedia page and return the president’s name and birthday. First things first, let’s get the raw HTML from George Washington’s Wikipedia page.

<script src="https://gist.github.com/scraperapi/6bafd36cf3ba6aa12ce7eb6d45063d6a.js"></script>

Output:

<script src="https://gist.github.com/scraperapi/76c56e2c587809f8b776061627dc2db3.js"></script>

Let’s once again use Chrome DevTools to find the syntax of the code we want to parse, so that we can extract the name and birthday with Cheerio.js.

![Image](https://cdn-media-1.freecodecamp.org/images/1*exzZbuIwfrCcbTM2rr9_bw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*yth6AmHpywM77n0wEprpiA.png)

So we see that the name is in a class called “firstHeading” and the birthday is in a class called “bday”. Let’s modify our code to use Cheerio.js to extract these two classes.

<script src="https://gist.github.com/scraperapi/51d70b35c6b45459038439e5fa118fbc.js"></script>

Output:

<script src="https://gist.github.com/scraperapi/459c6bdf3fd4b6c9252dccbff4dd06db.js"></script>

### Putting it all together

Perfect! Now let’s wrap this up into a function and export it from this module.

<script src="https://gist.github.com/scraperapi/a24369f8f0b1bb805874e3f1229b9fa3.js"></script>

Now let’s return to our original file potusScraper.js and require the potusParse.js module. We’ll then apply it to the list of wikiUrls we gathered earlier.

<script src="https://gist.github.com/scraperapi/b46842acda7e87d5bce57175974ba11c.js"></script>

Output:

<script src="https://gist.github.com/scraperapi/c1f85d62704d4837c9c20fb9f11a9ecd.js"></script>

### Rendering JavaScript Pages

Voilà! A list of the names and birthdays of all 45 U.S. presidents. Using just the request-promise module and Cheerio.js should allow you to scrape the vast majority of sites on the internet.

Recently, however, many sites have begun using JavaScript to generate dynamic content on their websites. This causes a problem for request-promise and other similar HTTP request libraries (such as axios and fetch), because they only get the response from the initial request, but they cannot execute the JavaScript the way a web browser can.

Thus, to scrape sites that require JavaScript execution, we need another solution. In our next example, we will get the titles for all of the posts on the front page of Reddit. Let’s see what happens when we try to use request-promise as we did in the previous example.

Output:

<script src="https://gist.github.com/scraperapi/1767e286bca624f1bc0aff8b35983b06.js"></script>

Here’s what the output looks like:

<script src="https://gist.github.com/scraperapi/a5cb4b9d8d18878ddeefa7e6cfd21ba6.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/1*mKzPVGRR4CFKMwQw5y_YnQ.png)

Hmmm…not quite what we want. That’s because getting the actual content requires you to run the JavaScript on the page! With Puppeteer, that’s no problem.

Puppeteer is an extremely popular new module brought to you by the Google Chrome team that allows you to control a headless browser. This is perfect for programmatically scraping pages that require JavaScript execution. Let’s get the HTML from the front page of Reddit using Puppeteer instead of request-promise.

<script src="https://gist.github.com/scraperapi/d29dc43d7f00451c43b8056f716b07b6.js"></script>

Output:

<script src="https://gist.github.com/scraperapi/1c05f2d36c9a34f93d1c78ff754c105b.js"></script>

Nice! The page is filled with the correct content!

![Image](https://cdn-media-1.freecodecamp.org/images/1*N5HtAiijcMEB_fBQvPd7Ow.png)

Now we can use Chrome DevTools like we did in the previous example.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tHSgjPMvn3M26N2f7Q2B1Q.png)

It looks like Reddit is putting the titles inside “h2” tags. Let’s use Cheerio.js to extract the h2 tags from the page.

<script src="https://gist.github.com/scraperapi/8902791ba6f4b95a7aacebc5ef1348b8.js"></script>

Output:

<script src="https://gist.github.com/scraperapi/636185affefd429503e349f2e1616df2.js"></script>
<style>
.gist { width: 100% !important; overflow:auto; }
</style>


### Additional Resources

And there’s the list! At this point you should feel comfortable writing your first web scraper to gather data from any website. Here are a few additional resources that you may find helpful during your web scraping journey:

* [List of web scraping proxy services](https://www.scraperapi.com/blog/the-10-best-rotating-proxy-services-for-web-scraping)
* [List of handy web scraping tools](https://www.scraperapi.com/blog/the-10-best-web-scraping-tools)
* [List of web scraping tips](https://www.scraperapi.com/blog/5-tips-for-web-scraping)
* [Comparison of web scraping proxies](https://www.scraperapi.com/blog/free-shared-dedicated-datacenter-residential-rotating-proxies-for-web-scraping)
* [Cheerio Documentation](https://github.com/cheeriojs/cheerio)
* [Puppeteer Documentation](https://github.com/GoogleChrome/puppeteer)

