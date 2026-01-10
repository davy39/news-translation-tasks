---
title: How to build a Hacker News Frontpage scraper with just 7 lines of R code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-06T20:54:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-hacker-news-frontpage-scraper-with-just-7-lines-of-r-code-221af6acb98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P7CAV7kEQ4aBBzozOCYGsA.jpeg
tags:
- name: General Programming
  slug: programming
- name: R Programming
  slug: r-programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
- name: web scraping
  slug: web-scraping
seo_title: null
seo_desc: 'By AMR

  Web scraping used to be a difficult task requiring expertise in XML Tree parsing
  and HTTP Requests. But with new-age scraping libraries like beautifulsoup (for Python)
  and rvest (for R), web scraping has become a toy for any beginner to play w...'
---

By AMR

Web scraping used to be a difficult task requiring expertise in XML Tree parsing and HTTP Requests. But with new-age scraping libraries like beautifulsoup (for Python) and rvest (for R), web scraping has become a toy for any beginner to play with.

This post aims to explain how simple it is to use R, a very nice programming language, to perform Data Analysis and Data Visualization. The task ahead is very simple. Build a web scraper that scrapes the content of one of the most popular pages on the Internet (at least among Coders): [Hacker News Front Page](https://news.ycombinator.com/).

### Package Installation and Loading

The R package that we are going to use is `rvest.` `rvest` can be installed from [CRAN](https://cran.r-project.org/web/packages/rvest/index.html) and loaded into R like below:

```
library(rvest)
```

`read_html()` function of `rvest` can be used to extract the HTML content of the url given as the argument for read_html function.

```
content <- read_html('https://news.ycombinator.com/')
```

For `read_html()` to work without any concern, please make sure you are not behind any organization firewall. If so, configure your RStudio with a proxy to bypass the firewall, otherwise you might face a `connection timed out error`.

Below is the screenshot of HN front page layout (with key elements highlighted):

![Image](https://cdn-media-1.freecodecamp.org/images/4rSb9LXlF3ZcRyLEGeKrT2yX8vsQJkACkaXi)

Now, with the HTML content of the Hacker News front page loaded into the R object _content_, let us extract the data that we need — starting with the Title.

There is one particularly important aspect of making any web scraping assignment successful. That is to identify the right CSS selector, or XPath values, of the HTML elements whose values are supposed to be scraped. The easiest way to get the right element value is to use `the inspect tool` in Developer Tools of any browser.

Here’s the screenshot of the CSS selector value. It is highlighted using the Chrome Inspect Tool when hovered over Title of the links present in Hacker News Frontpage.

![Image](https://cdn-media-1.freecodecamp.org/images/IEJOiDb3aUyj90KuhWzWyAO4eoQ3Z1jUcpNM)

```
title <- content %>% html_nodes('a.storylink') %>% html_text()title [1] "Magic Leap One"                                                                   [2] "Show HN: Terminal – native micro-GUIs for shell scripts and command line apps"    [3] "Tokio internals: Understanding Rust's async I/O framework"                        [4] "Funding Yourself as a Free Software Developer"                                    [5] "US Federal Ban on Making Lethal Viruses Is Lifted"                                [6] "Pass-Thru Income Deduction"                                                       [7] "Orson Welles' first attempt at movie-making"                                      [8] "D’s Newfangled Name Mangling"                                                     [9] "Apple Plans Combined iPhone, iPad, and Mac Apps to Create One User Experience"    [10] "LiteDB – A .NET NoSQL Document Store in a Single Data File"                      [11] "Taking a break from Adblock Plus development"                                    [12] "SpaceX’s Falcon Heavy rocket sets up at Cape Canaveral ahead of launch"          [13] "This is not a new year’s resolution"                                             [14] "Artists and writers whose works enter the public domain in 2018"                 [15] "Open Beta of Texpad 1.8, macOS LaTeX editor with integrated real-time typesetting"[16] "The triumph and near-tragedy of the first Moon landing"                          [17] "Retrotechnology – PC desktop screenshots from 1983-2005"                         [18] "Google Maps' Moat"                                                               [19] "Regex Parser in C Using Continuation Passing"                                    [20] "AT&T giving $1000 bonus to all its employees because of tax reform"              [21] "How a PR Agency Stole Our Kickstarter Money"                                     [22] "Google Hangouts now on Firefox without plugins via WebRTC"                       [23] "Ubuntu 17.10 corrupting BIOS of many Lenovo laptop models"                       [24] "I Know What You Download on BitTorrent"                                          [25] "Carrie Fisher’s Private Philosophy Coach"                                        [26] "Show HN: Library of API collections for Postman"                                 [27] "Uber is officially a cab firm, says European court"                              [28] "The end of the Iceweasel Age (2016)"                                             [29] "Google will turn on native ad-blocking in Chrome on February 15"                 [30] "Bitcoin Cash deals frozen as insider trading is probed"
```

The rvest package supports pipe %>% operator. Thus, the R object containing the content of the HTML page (read with read_html) can be piped wi`th html_node`s() that takes a CSS selector or XPath as its argument. It can then extract the respective XML tree (or HTML node value) whose text value could be extracted wi`th html_tex`t() function.

The beauty of rvest is that it abstracts the entire XML parsing operation under the hood of functions like html_nodes() and html_text(). Thus making it easier for us to achieve our scraping goal with minimal code.

Like with Title, the CSS selector value of other required elements of the web page can be identified with the Chrome Inspect tool. They can also be passed as an argument to html_nodes() function and respective values can be extracted and stored in R objects.

```
link_domain <- content %>% html_nodes('span.sitestr') %>% html_text()score <- content %>% html_nodes('span.score') %>% html_text()age <- content %>% html_nodes('span.age') %>% html_text()
```

All the essential pieces of information were extracted from the page. Now an R data frame can be made with the extracted elements to put the extracted data into a structured format.

```
df <- data.frame(title = title, link_domain = link_domain, score = score, age = age)
```

Below is the screenshot of the final dataframe in RStudio viewer:

![Image](https://cdn-media-1.freecodecamp.org/images/hEnsMstgI7-hwhOHGx9LrexwgAEoOb8q5bmK)

Thus, in just 7 lines of code, we have successfully built a Hacker News Frontpage Scraper in R.

R is a wonderful language to perform Data Analysis and Data Visualization. The code used here is available [on my github](https://github.com/amrrs/HN_scraper_in_R).

