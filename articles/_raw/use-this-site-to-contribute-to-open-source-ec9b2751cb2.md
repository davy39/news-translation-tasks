---
title: Use this site to contribute to open source
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-22T18:03:11.000Z'
originalURL: https://freecodecamp.org/news/use-this-site-to-contribute-to-open-source-ec9b2751cb2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6RUQ0iJ582gOm5HY
tags:
- name: coding
  slug: coding
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jerry Muzsik

  When I began the transition into being a software developer, I knew that contributing
  to open source projects would greatly assist my job search.

  So, I jumped onto GitHub looking for issues that I could take on. Little did I know
  that...'
---

By Jerry Muzsik

When I began the transition into being a software developer, I knew that contributing to open source projects would greatly assist my job search.

So, I jumped onto GitHub looking for issues that I could take on. Little did I know that _this would be a miserable endeavor_.

### The Realisation

At the beginning, I thought I could simply go to React’s repo page (or another extremely popular repo’s page) and find an issue.

But those repo’s are literally hounded by people looking for an issue. And it is very time consuming to click through repositories.

My second thought was to use [GitHub’s issue search](https://github.com/issues), but I ran into several problems here:

1. You cannot filter issues based upon the amount of stars a repository has
2. You can only filter by language if the issue is literally labeled that language. (So if the project is predominantly a JavaScript repo and the issue is not labeled JavaScript, you have no way of searching for it by language.)

#### How do you look at issues focused on popular projects?

Basically, you have to know of them and look them up manually.

#### How can you find an issue from a popular project in the language you know best?

1. As said before, go to a project’s GitHub page by _learning of its existence in some way_
2. Look through the issues. Now you can filter a little by label (think bug, feature, good-first-issue)
3. If you don’t find something that you can do, you have to start this process over with a new repo!

Needless to say, it took me forever to find an issue that I wanted to take on.

Fast forward a few months. I began to make a website to make open source contribution easier.

### The Process of Creation

![Image](https://cdn-media-1.freecodecamp.org/images/AAV4wgF5o3N1LUEYejtGeXOvW8KhYyrKQJa4)
_Photo by [Unsplash](https://unsplash.com/@luca_tism?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Luca Laurence</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

The main challenge was to get the data that I wanted. I knew I had to use the GitHub API.

As I said earlier, when you search on GitHub for an issue, you cannot search by stars or language. This stems from the fact that GitHub’s Repo API request does not provide this option.

My initial thought was that I should focus on finding repositories of interest. For example, the thousand most starred JavaScript, Python, and a variety of other languages repos.

_Well… you cannot search repos by language nor by star count._

Dynamically fetching data is cool, but how could I do it? Here is a condensed view of why it is ridiculously difficult with the GitHub API.

#### Coming to Terms with the GitHub API

One thing to begin with: you have a limit of 5000 requests per hour to the GitHub API.

This is the only way to get a bunch of repositories at once: [https://api.github.com/repositories](https://api.github.com/repositories) which will give you around 35 repositories but _none of these rows have language or star count._

Though, you can query each of these repositories returned from the initial API request (ex. [https://api.github.com/repos/facebook/react](https://api.github.com/repos/facebook/react)) and **then you get this data!**

But wait… I have to go through every repository on GitHub... there are approximately **90 million** repositories.

#### **A Little Math**

90,257,000 (amount of repos with amount of requests to get repos) / 5000 (hourly rate limit) ~= 18,000 hours or 750 days or around 2 years… ?

![Image](https://cdn-media-1.freecodecamp.org/images/lXGjTRFCUmD2w3-FP0p0EqrTGAuop07sldba)
_Photo by [Unsplash](https://unsplash.com/@kaip?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Kai Pilger</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### The Reluctantly Made Decision

So I had to find the repositories manually… ?. Thank god for this site: h[ttps://gitstar-ranking.com/](https://gitstar-ranking.com/) but still, quite a few hours of clicking through repositories…

But, I got there! And here is the site! ?

### [FindanIssue.org](https://findanissue.org/)

![Image](https://cdn-media-1.freecodecamp.org/images/LCdHAEC6UExXLxVSF6ojXRyWZcjmgAMcWA6O)
_The amazing website_

I made it as simple as possible. Search by the exact repo, by specific language (exact and case sensitive), by label, or the age of the issue. So, you can get to the root of what you are looking for.

If you are a beginner, then search by labels such as _good first issue_ or _docs/ documentation_ as well as specifying your programming language of choice.

![Image](https://cdn-media-1.freecodecamp.org/images/Kapd7zRmeB0Ih47xJ-thgI-wleyKTo47lBfv)
_Beginner Issue Example_

If you are a seasoned developer looking for a challenge, search by labels such as _feature_, _help wanted_, _bug_, or other labels of your choice.

![Image](https://cdn-media-1.freecodecamp.org/images/DZ6U9O8kPo0Q1zhANvILm2-bWno1ZOGtexGI)
_More Advanced Issue Search_

At the moment, the data is refreshed twice daily so old issues are removed and issues that have been labeled are given their proper label.

### Closing Thoughts

There is still a lot of work that can be done:

* The most glaring problem is that only around 900 projects are showcased. So, there are a wide spectrum of amazing projects that are not being given a chance.
* Improving the backend and some additions to the frontend would really make a difference

All in all, I made this because I believe it to be a step towards fulfilling a need in the open source community of linking issues to developers. **Rather then going out into the wild to find an issue to take on, the site aims to make it a simple few minutes of searching through a table.**

I hope you use it and find yourself giving back to the world of open source, that you, as a developer, depend on every single day.

![Image](https://cdn-media-1.freecodecamp.org/images/q9MweeUDqyg9Ucyvzvsp5x1Z3U7T5D9WMqoX)
_Photo by [Unsplash](https://unsplash.com/@pavement_special?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Riccardo Annandale</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

> Here is the repo: [https://github.com/jMuzsik/find-an-issue](https://github.com/jMuzsik/find-an-issue)  
>   
> And here is the site: [https://findanissue.org](https://findanissue.org/)

And thanks for the read!

