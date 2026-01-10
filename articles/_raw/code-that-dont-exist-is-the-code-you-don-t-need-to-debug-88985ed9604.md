---
title: Code That Doesn’t Exist Is The Code You Don’t Need To Debug
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-19T09:02:00.000Z'
originalURL: https://freecodecamp.org/news/code-that-dont-exist-is-the-code-you-don-t-need-to-debug-88985ed9604
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wuV2gWnanM8JoG_8CS09tQ.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Fagner Brack

  As developers, we tend to write more code than necessary

  As a developer, you’re in the business of managing complexity. And code is inherently
  complex.

  By writing as little code as necessary to solve the task at hand, you’ll have fewe...'
---

By Fagner Brack

#### As developers, we tend to write more code than necessary

As a developer, you’re in the business of managing complexity. And code is inherently complex.

By writing as little code as necessary to solve the task at hand, you’ll have fewer concerns down the road.

Less code, less complexity.

%[https://twitter.com/paulg/status/788803863381995520?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Dd04bfffea46d4aeda930ec88cc64b87c%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fpaulg%2Fstatus%2F788803863381995520%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F1824002576%25252Fpg-railsconf_bigger.jpg%2526key%253D4fce0568f2ce49e8b54624ef71a8a5bd]

There are many examples that can illustrate this principle. For the purpose of this post, let’s say you want to test an existing function. It’s an untested legacy function that executes a network request and does something with its response. The important aspect is that the response contains more data than what the code actually uses.

<script async src="//jsfiddle.net/fagnerbrack/gytawzt9/embed/"></script>

The [code](https://jsfiddle.net/fagnerbrack/gytawzt9/) showing a function that only requires the “street”, “number” and “suburb” properties from the “accountDetails”. See the line 27.

When testing that function, you want to stub the network request and provide a fixed dataset that simulates the original one. This way you can verify whether the function works as expected.

<script async src="//jsfiddle.net/fagnerbrack/pmgv0chw/embed/"></script>

The [code](https://jsfiddle.net/fagnerbrack/pmgv0chw/) stubbing the network request with the same dataset. See lines 37 to 47.

But the original dataset is huge and you don't really care about the rest of it. You can just provide the minimum response necessary to satisfy the requirements of the function you’re testing.

<script async src="//jsfiddle.net/fagnerbrack/Lv6cd0v0/embed/"></script>

The [code](https://jsfiddle.net/fagnerbrack/Lv6cd0v0/), stubbing just the minimum amount of properties from the dataset. See lines 37 to 41.

There are a few benefits with the last example:

1. There’s no unused response in the test
2. The dataset won’t be huge, so it’s easier to reason about it (and that also makes the test smaller)
3. If the code starts requiring more data from the response because of another test on the same function, the test will fail and you can start adding the rest of the response on an ad-hoc basis
4. If you always change code by changing the tests first, when the code starts requiring less data, you’ll always be removing it from the tests first in order to keep the minimum amount of code necessary to test it

[Test Driven Development](https://medium.com/@fagnerbrack/why-test-driven-development-4fb92d56487c) (TDD) forces you to write the minimum amount of code that satisfies a use case. In the last example, if you had used TDD, it would have forced you to write the minimum amount of code in the dataset until you needed more data (See number 3 above).

In a great article called [You Are Not Paid to Write Code](http://bravenewgeek.com/you-are-not-paid-to-write-code/), Tyler Treat says:

> _Every time you write code […] you are introducing the possibility of failure into your system._

A software system has a tendency to become more complex over time, increasing [Software Entropy](https://en.wikipedia.org/wiki/Software_entropy). The act of deleting code helps drive the system to a state where there’s only code that is necessary — a state where there's less Software Entropy. But project teams tend to ignore this principle and focus mostly on adding new things.

To avoid that, I believe developers should be rewarded when they remove code. Perhaps the same way (or more) than when they add new features.

> Removing useless code should be rewardable.

Besides complexity, useless code can also represent part of a functionality that doesn't provide any value. For every feature or change related to that functionality, you have more stuff to test, maintain, and support. That’s an unnecessary cost to the project, and a cost that doesn't go away unless explicitly removed.

Evolution has shaped our minds to think of short term benefits. Adding features or fixing bugs to satisfy the project goal leads to **short term benefit** in the context of Software Entropy. This is essential, but shouldn’t come at the expense of adding or leaving code that is not necessary.

The characteristic that makes us humans is our ability to think ahead. Our ability to think about what really matters for a project. What we need is to reinforce the culture of removing code.

**The code that doesn’t exist is the code you don’t need to worry about**.

After all, why having to worry about something you don’t need to?

Thanks for reading. If you have some feedback, reach out to me on [Twitter](https://twitter.com/FagnerBrack), [Facebook](https://www.facebook.com/fagner.brack) or [Github](http://github.com/FagnerMartinsBrack).

