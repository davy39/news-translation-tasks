---
title: Here are 5 ways you can keep track of trending repositories on GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-06T15:12:51.000Z'
originalURL: https://freecodecamp.org/news/five-ways-of-tracking-trends-on-github-63940fca63b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Wk2sOsVhjtblFT0VM6iRaw.png
tags:
- name: Design
  slug: design
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Vitaliy Potapov

  GitHub trending is a constantly updated list of repositories that provide a view
  of the open-source projects which the community is most excited about.

  Trending repositories are displayed based on the number of times they’ve been s...'
---

By Vitaliy Potapov

[GitHub trending](https://github.com/trending) is a constantly updated list of repositories that provide a view of the open-source projects which the community is most excited about.

Trending repositories are displayed based on the number of times they’ve been starred by users every day, week or month. You can filter them based on a specific programming language so you can see what’s happening in your area of interest.

Tracking this page will also keep you informed of the “hottest” projects that everyone is talking about. I’ve tried five different ways of tracking trends on GitHub and have come up with some comparisons and contrasts as highlighted below.

#### 1. GitHub Explore newsletter

This is the official newsletter from GitHub. You can [subscribe to it here](https://github.com/explore#newsletter). Emails are sent out daily, weekly or monthly, depending on your preference. The email contains the top 5 trending repositories across all programming languages for the selected period:

![Image](https://cdn-media-1.freecodecamp.org/images/rTRRKgydWhUpWPGeh28MgOQp92s8P4umTMFp)
_GitHub Explore newsletter_

The newsletter also contains personalized recommendations. For example, it may contain a list of projects starred by people you are following on GitHub.

**Advantages:**

* Official newsletter
* Daily, weekly or monthly mailing schedule
* Personal recommendations

**Disadvantages:**

* You cannot subscribe to a particular programming language
* Only top 5 repositories are in the list, although there are 25 on the GitHub trending page

#### 2. GitHub notifications

GitHub notification system is a native and convenient way of tracking activity on GitHub. For many developers it is a part of their daily working process. You can receive notifications about new comments, pull requests, mentions and any other activity you might be involved in.

![Image](https://cdn-media-1.freecodecamp.org/images/E1c6i7bh3G4LUKbxGHbuFh-hRqqiVpcUCGPc)
_GitHub web notification bell, from [official docs](https://help.github.com/articles/accessing-your-notifications/" rel="noopener" target="_blank" title=")_

[GitHub-trending-repos](https://github.com/vitalets/github-trending-repos) is a special repository that uses GitHub notifications to send you updates about trends. Every issue in that repository is related to a particular programming language. On daily and weekly basis, the bot checks trending repositories page and drops a comment. You can subscribe to an issue and receive updates on the GitHub web interface or by email.

![Image](https://cdn-media-1.freecodecamp.org/images/mlQrzM0MhtXcsqHLL5z9-3pHEWAkSyj-JsVl)
_GitHub web notification with new trends_

![Image](https://cdn-media-1.freecodecamp.org/images/8l5mrOSoxEhkvEBb76EUbPAIjMCb0k4JNGHc)
_Example of bot’s comment_

**Advantages:**

* You can subscribe to trends of a particular programming language
* You can receive notifications either in the GitHub web interface or by email
* You can choose between daily and weekly updates

**Disadvantages:**

* Not all programming languages are available for subscription as yet

#### 3. Twitter bot

Every 30 minutes [@TrendingGithub](https://twitter.com/TrendingGithub) bot tweets about one actual trending repository or developer:

![Image](https://cdn-media-1.freecodecamp.org/images/QIEvPrCVCagHnnBwVX6YW51CvbVG1DLzJYMP)
_Example of @TrendigGithub tweet_

The followers can easily keep a finger on GitHub trending pulse. Repositories are selected across all programming languages. Internally, the project remembers tweeted items for 30 days to avoid duplication of content.

**Advantages:**

* Twitter is a convenient channel for receiving news
* You can track trending developers as well

**Disadvantages:**

* Not possible to subscribe to a particular programming language
* Receiving updates every 30 minutes may be annoying

Project source is [available on GitHub](https://github.com/andygrunwald/TrendingGithub).

#### 4. Changelog Nightly newsletter

[Changelog Nightly](https://changelog.com/nightly) is an automated newsletter sent every night at 10pm US Central Time (CT). It collects trending repositories across all programming languages and splits them into three groups:

1. _First timers_ - trending repositories not previously emailed
2. _Top new_ - trending repositories open-sourced throughout the day
3. _Repeat performers -_ trending repositories that already appeared in the newsletter before

![Image](https://cdn-media-1.freecodecamp.org/images/9bbKYAzBv642UbMlGbIc1oWyY2QP66UxYRr2)
_Changelog Nightly email_

It is a sub-project of [Changelog](https://changelog.com/) - a digital media company offering a lot of other cool stuff for developers: 7 technical podcasts, news, weekly moderated email and community discussions in Slack.

**Advantages:**

* Items are separated into meaningful groups: first timers, created today and repeat performers

**Disadvantages:**

* The only schedule option available is daily emails
* Not possible to filter by a particular programming language

It’s worth mentioning that Changelog Nightly is powered by [GitHub Archive](https://www.githubarchive.org/)- a database recording all public activity on GitHub. You can access data with any HTTP client and make your own analysis.

#### 5. Manual browsing of daily updated repo

Consider this method if you don’t need any notifications. Every day, a script in [github-trending](https://github.com/josephyzhou/github-trending) repository scrapes trending projects and commits them as markdown files. You can manually browse these files and find out what was trending on a particular date.

![Image](https://cdn-media-1.freecodecamp.org/images/LBkOehionUFg4AyZ3nFkBCi6eSUmYk5lgRz9)
_Daily markdown files with trending repositories_

The content of each file covers 7 programming languages: Swift, Objective-C, Go, JavaScript, Ruby, Rust and Python.

![Image](https://cdn-media-1.freecodecamp.org/images/ZGIwNNGke5UHpWGCahTio-uInYhxKYzb1I3t)
_Trending projects for Swift on 26 Nov 2017_

**Advantages:**

* You can access the full history of trends
* You are not bothered by notifications

**Disadvantages:**

* Only 7 languages are supported
* Only daily trends, no weekly or monthly updates
* No info about acquired stars
* You need to browse manually

### Conclusion

Each method has its own advantages and disadvantages. You can try all of them and select the most suitable for you.

I believe that following new GitHub projects is an important part of the open-source world. It has a win-win effect:

1. As a developer you can improve your own productivity by using modern approaches and tools.
2. As a project author you can receive community feedback and inspiration for future development.

Thanks for reading! You’re welcome to share how you discover trends on GitHub.

