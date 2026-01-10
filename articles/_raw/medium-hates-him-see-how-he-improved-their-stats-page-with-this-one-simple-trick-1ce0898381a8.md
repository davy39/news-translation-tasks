---
title: Medium Hates Him! See How He Improved the Stats Page With This One Simple Trick
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-29T10:43:05.000Z'
originalURL: https://freecodecamp.org/news/medium-hates-him-see-how-he-improved-their-stats-page-with-this-one-simple-trick-1ce0898381a8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*y4m4pKrlHu_Scdbl26c0jw.png
tags:
- name: Blogger
  slug: blogger
- name: chrome extension
  slug: chrome-extension
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tomas Trajan

  Yeah, the title, I know… but I had to try it at least once in my life ??

  For many of us, Medium is the go-to platform for writing and publishing content
  online. It provides an extremely slick writing experience and, to be honest, I ca...'
---

By Tomas Trajan

Yeah, the title, I know… but I had to try it at least once in my life ??

For many of us, Medium is the go-to platform for writing and publishing content online. It provides an extremely slick writing experience and, to be honest, I can’t imagine using anything else anymore…

> I have been using Medium for years and I was always curious about the total reach of my articles

Unfortunately, Medium stats can be described only as very basic or, to be frank, utterly lacking in the feature department. Even simple stuff like a summary row with a total count of the views and reads at the bottom of the table is missing.

The only solution is to add the numbers manually which is a boring, error-prone process. It gets progressively more tedious with the increasing number of articles, so you basically get punished for being a productive writer…

But hey, there is hope…

![Image](https://cdn-media-1.freecodecamp.org/images/bGGbeoGFJwryJLAFpK1wjfJJzfl1glkn1vdY)

…at least for the people using [Google Chrome](https://chrome.google.com/webstore/detail/medium-enhanced-stats/jnomnfoenpdinfkpaaigokicgcfkomjo) and Opera with this amazing [Opera addon](https://addons.opera.com/en/extensions/details/install-chrome-extensions/) and then installing [standard Chrome extension](https://chrome.google.com/webstore/detail/medium-enhanced-stats/jnomnfoenpdinfkpaaigokicgcfkomjo).

> Introducing Medium Enhanced Stats

### What is in it for You? ????

To put it briefly, there are four main features of Medium Enhanced Stats:

1. Total reach indicator
2. Bar chart article markers
3. Stats table summary row and extra information
4. Support for users and publications
5. ? An Easter Egg to be found, if you’re not afraid to roll up your sleeves and explore the source ???

> Add [Medium Enhanced Stats](https://chrome.google.com/webstore/detail/medium-enhanced-stats/jnomnfoenpdinfkpaaigokicgcfkomjo) to your Google Chrome now! Yes, it’s 100% FREE!

Or to Opera with this amazing [Install Chrome Extensions addon](https://addons.opera.com/en/extensions/details/install-chrome-extensions/).

### Total reach indicator

![Image](https://cdn-media-1.freecodecamp.org/images/8VrBm8c7TlM1awYV2nGbkiN9DgQdsw2HoDd4)

Total reach is a sum of all the views of your articles and responses.

Instead of being a plain number, indicator contains a next milestone and a progress bar which shows how much you have already accomplished.

Milestone is calculated as a next 10x “round” number.

For example, people with a reach under 1K will achieve their 1K milestone pretty quick, but it will probably take more time to move from 1M to 10M…

> Then again, I would be very happy if you proved my assumption wrong ?

> I would like to thank [Johann Gyger](https://www.freecodecamp.org/news/medium-hates-him-see-how-he-improved-their-stats-page-with-this-one-simple-trick-1ce0898381a8/undefined) for his help with debugging the extension popup! ??????

### Bar chart article markers

Have you ever caught yourself wondering what was the cause of that pronounced views bump 3 months ago? Me too! Luckily the newest feature of Medium Enhanced Stats set out to solve just that…

![Image](https://cdn-media-1.freecodecamp.org/images/OH2aIJYP2j7fUFt7qgjoMukDoRvS5dnXyHvp)
_Check out article markers in the bar chart and discover effect of their publishing on the overall performance…_

Medium’s original bar chart is now enhanced with the article markers. It also works for responses and can handle displaying multiple articles per day.

![Image](https://cdn-media-1.freecodecamp.org/images/w38exCH-FhiHVHANDmnaSq72Yo3QNn5mbBbx)
_Markers can handle also multiple articles per day and the marker size reflects amount of articles… Yes, bigger IS better ?_

### Summary row and extra information

This was the initial feature of the extension, and was basically the way it all started out: having a simple summary row which displays the sum of the values per column.

> You know, Excel sum ∑ stuff…

As it turned out, the retrieved data also contains the amount of claps per article. This is nowadays a much more useful metric, since Medium switched to displaying claps also in the UI of the articles themselves.

![Image](https://cdn-media-1.freecodecamp.org/images/BF-YpLEjIlfOV0TUfZW7DJ9s4ZKYh-piWOIP)
_Summary row is exactly what it sound it is ? Besides that, there is also an additional claps column for every article…_

### Support for users and publications

In the beginning, Medium Enhanced Stats could only display stats for a single currently logged in author. Feedback from the first users came pretty fast: they were asking for the ability to do the same for their publications.

> Just installed a new chrome extension [http://goo.gl/XBvNFu](https://t.co/azWSmxsnFY) by [@tomastrajan](https://twitter.com/tomastrajan). Very convenient. It says I’ve reached more than 1 million people! And it now encourages me to aim for 10 millions :). Great work, [@tomastrajan](https://twitter.com/tomastrajan)! **Can it show stats for a publication?** — [Max NgWizard K](https://www.freecodecamp.org/news/medium-hates-him-see-how-he-improved-their-stats-page-with-this-one-simple-trick-1ce0898381a8/)

**Ask and you shall be given!**

![Image](https://cdn-media-1.freecodecamp.org/images/eTqTvwzoxqvYjX2gS7pWx1rAJ0bXbMxuKphE)
_Click on the user avatar and select from available users and publications_

#### Technical background for my fellow developers

Medium Enhanced Stats is a Chrome Extension. Chrome Extensions are great for enriching existing websites with custom functionality, because we have the possibility to inject custom scripts in a safe way.

Custom script can access and leverage all the visible and invisible data available on the original page. More so, because they now belong to the original site, they can also make requests on its behalf. And let me tell you, it is much easier to calculate totals from JSON data than to scrape an HTML table.

I am planning to write another post which will get much more into details of how to implement Chrome extensions so [stay tuned](https://twitter.com/tomastrajan)…

> **FUN FACT —** Medium Enhanced Stats retrieves and show total stats, right? Well, it’s almost total: you might need to worry if you’ve published more than **100k articles,** which is currently the limit of the paging request ?

Before I forget, Medium Enhanced Stats is also fully open sourced on GitHub, so feel free to [check it out](https://github.com/tomastrajan/medium-enhanced-stats). There is virtually no documentation available yet, but I will definitely add more in the future to enable community-driven efforts!

### Future

Since its inception, the extension has already gone through a couple of major iterations and improvements.

Currently, there is a plan to try to visualise articles which are the major contributors to views each day. It can get rather tricky in situations with lots of articles with small individual contributions. It will be important to strike a good balance to make it useful instead of distracting.

Another opportunity worth exploring is adding a way to download and share a stylized total reach indicator with author’s name, Medium username, and other social media handles. This could be useful because authors would gain an easy way to communicate their contribution as a proxy of their trustworthiness for new members of their communities.

### This is the end!

I hope you will try [**Medium Enhanced Stats**](https://chrome.google.com/webstore/detail/medium-enhanced-stats/jnomnfoenpdinfkpaaigokicgcfkomjo) out and let me know about your experience and possible enhancement ideas!

Please, help spread this article to a wider audience with your ? ? ? and fol[low me on ?️ Twitter to](https://twitter.com/tomastrajan) get notified about my newest blog posts ?

> _And never forget, the future is bright._

![Image](https://cdn-media-1.freecodecamp.org/images/TkU6BdKH0HFXacxUWsDtvHTCtsPv2X54PVab)
_Obviously the bright future (? by S[asha • Stories)](https://unsplash.com/@sanfrancisco" rel="noopener" target="_blank" title=")_

If you made it this far, feel free to check out some of my other articles about frontend software development…

[**How To Stay Up To Date With Releases Of Popular Frameworks**](https://medium.com/@tomastrajan/how-to-stay-up-to-date-with-releases-of-popular-frontend-frameworks-with-twitter-bot-release-butler-86af7b734706)  
[_Introducing Release Butler — A Twitter Bot That Helps You To Stay Up To Date With Releases Of Popular Frontend…_medium.com](https://medium.com/@tomastrajan/how-to-stay-up-to-date-with-releases-of-popular-frontend-frameworks-with-twitter-bot-release-butler-86af7b734706)[**How To Build Responsive Layouts With Bootstrap 4 and Angular 6 ?**](https://medium.com/@tomastrajan/how-to-build-responsive-layouts-with-bootstrap-4-and-angular-6-cfbb108d797b)  
[E_very web app is assumed to be responsive, period.m_edium.com](https://medium.com/@tomastrajan/how-to-build-responsive-layouts-with-bootstrap-4-and-angular-6-cfbb108d797b) [**How To Speed Up Continuous Integration Build With New NPM CI And package-lock.json**](https://medium.com/@tomastrajan/how-to-speed-up-continuous-integration-build-with-new-npm-ci-and-package-lock-json-7647f91751a)  
[_While very controversial, the new npm release 5.7.0 brings some amazing features which will have noticeable positive…_medium.com](https://medium.com/@tomastrajan/how-to-speed-up-continuous-integration-build-with-new-npm-ci-and-package-lock-json-7647f91751a)

![Image](https://cdn-media-1.freecodecamp.org/images/oc3DlDTyqRJBctnhI4GhGrbT28932HJSPMWP)
_Don’t forget ! ?_

