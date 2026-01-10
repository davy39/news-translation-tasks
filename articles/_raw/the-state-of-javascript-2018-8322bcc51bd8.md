---
title: The State of JavaScript 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T16:01:46.000Z'
originalURL: https://freecodecamp.org/news/the-state-of-javascript-2018-8322bcc51bd8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*elJOIUil9x0O2AgISx7Ckg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sacha Greif

  We surveyed over 20,000 JavaScript developers. Here’s what they told us.


  I’m writing these lines somewhere high above Russia because it turns out there’s
  people willing to fly me halfway across the world for a conference just so they
  ...'
---

By Sacha Greif

#### We surveyed over 20,000 JavaScript developers. Here’s what they told us.

![Image](https://cdn-media-1.freecodecamp.org/images/5TqeXFGtpiqkdymYpTdPSxKILh7l6p6ibRa2)

I’m writing these lines somewhere high above Russia because it turns out there’s people willing to fly me halfway across the world for a conference just so they can hear me talk about JavaScript trends.

If you ask me, that’s a pretty good measure of how popular the [State of JavaScript survey](http://stateofjs.com) has become, and by extension how fast the JavaScript ecosystem keeps growing.

This year again, we surveyed over 20,000 JavaScript developers to figure out what they’re using, what they’re happy with, and what they want to learn. And the result is a unique collection of stats and insights that will hopefully help you make your own way through the JavaScript ecosystem.

#### ? C[heck out the results](https://2018.stateofjs.com)

…or read on to learn more about the project.

### What’s New This Year

#### Dark Mode

![Image](https://cdn-media-1.freecodecamp.org/images/KZ5MsA5bpeOgvH74t379z54LhDWlECvAocNo)

If you’ve seen the survey before, the first thing you’ll notice is probably the new, darker color scheme. We think it switches things up a bit, makes the charts pop more, and just looks pretty cool!

#### Individual Pages

In addition to grouping libraries in broad sections like front-end, back-end, and so on, we also decided to give each library its very own page. This makes it easier to ignore data that’s not relevant to you, while drilling deeper into tools that you do use.

#### Historical Data

![Image](https://cdn-media-1.freecodecamp.org/images/yOfFRfCBNgdmXmJrFmjx9lPqSQg9M2y7dvsX)

Because this is the third edition of the survey, we’re now able to show you historical data over the past two years! This is super helpful to see longer-term trends, and not just a frozen snapshot in time.

#### Likes & Dislikes

![Image](https://cdn-media-1.freecodecamp.org/images/u-z7t3VYkNnz9X9W97p0HarnZa5sj9yPBBEq)

We decided to feature fewer libraries this year, but in turn ask more follow-up questions about each of them. So not only did we ask you what you use, but also _why_ you use it.

#### No CSS

Sadly there will be **no CSS section** this year. CSS is such a vast topic it would almost merit a survey of its own, so rather than do things halfway we decided to focus on just JavaScript this time.

#### More Sharing

We took the extra step of generating image previews for every chart in the survey to make it easier to share them on social media or by email.

### Main Trends

We encourage you to [check out the full results](http://2018.stateofjs.com) but maybe you’re in a hurry and only want the gist of it?

TL;DR: things didn’t change that much this year.

#### JavaScript “Flavors”

We call “flavors” the various syntaxes and languages that can compile to JavaScript, such as TypeScript.

And speaking of TypeScript, [it’s the clear leader in this category.](https://2018.stateofjs.com/javascript-flavors/typescript/) In most places, over 40% of developers said they had used it and would happily use it again, and in some countries that ratio even went over 50%.

![Image](https://cdn-media-1.freecodecamp.org/images/lV92AsP1pjHuWvg431BKhRae4q3e0abjp9pb)
_TypeScript satisfaction ratio worlwide_

#### Front-End Frameworks

Here’s a chart that plots [how satisfied developers are with front-end libraries vs how many users they have](https://2018.stateofjs.com/front-end-frameworks/conclusion/):

![Image](https://cdn-media-1.freecodecamp.org/images/-jRXpzIaFq5bqwU8v6h1Lq4WKvBOC3It0kNl)
_Front-End Frameworks Quadrant Chart_

As you can see, only React has both a high satisfaction ratio and a large user base, although Vue is definitely getting there. Angular on the other hand does boast a large user base, but its users don’t seem too happy.

#### Data Layer

The data layer groups all the technologies used to transmit and manage data. And while Redux is dominant in terms of raw numbers, we think the trend favors GraphQL and adjacent technologies such as Apollo:

![Image](https://cdn-media-1.freecodecamp.org/images/8cNlJIv2Sj5ZqLOrw4J6CLXe-AkmJa0qlAmP)
_Data Layer Trends_

Of course, in theory you can use Redux and GraphQL together, but in practice that combination might end up being replaced by a GraphQL-specific tool like Apollo’s built-in state management.

To find out what’s going on with testing, back-end frameworks, and much more, [read the full results](https://2018.stateofjs.com/)!

### The Stack

It might seem weird to talk about a tech stack for what is, at its core, a simple static site. But this is JavaScript we’re talking about after all! So you know things are never going to be _that_ simple!

* We collected the data using [Typeform](https://www.typeform.com/). We built our own command-line tool to generate surveys from YAML outlines through their API, which was a huge help for iterating quickly.
* We then treated and normalized the data using [Elasticsearch](https://www.elastic.co/).
* We plugged the resulting JSON files into [Gatsby](https://gatsbyjs.org) to generate the site. We used a combination of Gatsby’s GraphQL data-querying features and plain old `import`s to load the data.
* Finally, we generated all the charts using the amazing [Nivo.js](http://nivo.rocks) data visualization library for React.

If you’re curious, the [entire project](https://github.com/StateOfJS/StateOfJS/tree/master/surveys/2018) is available on GitHub for learning purposes.

![Image](https://cdn-media-1.freecodecamp.org/images/uQ1YOSmLEuA7zUQFTLQ01TRGljhmLs42WR26)
_Nivo_

### About The Team

In case you’re curious who’s behind the survey:

#### [Sacha Greif](http://twitter.com/sachagreif) (me!)

I created the survey in 2016 to answer my own questions about the best technologies to learn. Two years later I’m still learning, and also trying to reinvest all that freshly acquired knowledge into my very own JavaScript framework, [Vulcan.js](http://vulcanjs.org).

#### [Raphael Benitte](https://twitter.com/benitteraphael)

Raphael is the creator of [Nivo](http://nivo.rocks), and an all-around data visualization expert, and front-end bad-ass. He also takes care of all data analysis tasks for the survey.

#### [Michael Rambeau](https://twitter.com/michaelrambeau)

Michael is the creator of [BestOfJS](https://bestofjs.org), an aggregator of data and trends about the JavaScript ecosystem. He’s the perfect person to ask when you need data about some obscure JavaScript library!

### What’s Next

Launching this year’s site was the result of over two months of hard work collecting, analyzing, and presenting data. But there’s still a lot more we could do.

For example, we would love to make the results site available in more languages. This will require a little re-engineering on our part, as a lot of strings are currently hardcoded, but it should be possible.

If you’d like to help translate the site in your language, please [check out this GitHub thread](https://github.com/StateOfJS/StateOfJS/issues/87).

And with all the work we’ve put in, we’re starting to think it might be a good idea to reuse our setup for other surveys. How about the State of…Turbo Pascal? Well, maybe not. But do let us know in the comments if you have any suggestions!

