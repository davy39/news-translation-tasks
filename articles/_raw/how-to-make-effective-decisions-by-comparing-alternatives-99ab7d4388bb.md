---
title: How to make effective decisions by comparing alternatives
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-19T23:41:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-effective-decisions-by-comparing-alternatives-99ab7d4388bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D1a3wrXwc0gWi65Na_fdyg.jpeg
tags:
- name: decision making
  slug: decision-making
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: teamwork
  slug: teamwork
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alon Kiriati

  Not better, not worse… just different

  “React.js is so much better than Angular”. “Java sucks, no one uses it anymore…
  we should use Golang”. “Pineapple is the worst pizza topping”. You’ve probably heard
  one of these very straight opin...'
---

By Alon Kiriati

### Not better, not worse… just different

“React.js is so much better than Angular”. “Java sucks, no one uses it anymore… we should use Golang”. “Pineapple is the worst pizza topping”. You’ve probably heard one of these very straight opinions. One option is the best, the other is the worst, X is better than Y and so on. But Java is still one of the most popular languages in the world. Angular gives a decent fight to React.js. Pizza with pineapple… well, that’s Ewwww.

Does that mean that more than half of the people are clueless? Or don’t know how to tell which technology is better or make the right choices? Maybe we should stop using terms like “better”, “worse”, “best” and shallow comparisons when evaluating alternatives. Instead, we should focus on the benefits of each solution, the disadvantages, and which one is a better fit for our specific problem.

### Evaluating alternatives

One way to do this is by creating an alternatives comparison table:

* Write the different alternatives in the header. Use each column to evaluate one alternative. Pick 2–5 alternatives.
* Write the different properties that you think are important for evaluating the different alternatives. Pick 2–5 most important comparison properties.
* Keep the last row for summing up. There is no better/worse solution, focus on why each alternative solves the problem.

### “What would you have to believe to choose this approach?”

For example, let’s assume that we have a problem that can be solved in two ways. One is [S.O.L.I.D](https://en.wikipedia.org/wiki/SOLID) and the other one is hackier. Some might say that we should always use a S.O.L.I.D solution, regardless of the circumstances. Does that mean that anyone who uses hacky code is a bad developer? I doubt it.

Let’s put the alternatives in a table:

![Image](https://cdn-media-1.freecodecamp.org/images/X3S5prczYyEXy32GLl6iID3nPJ1yqrK18z4O)

After composing this table, we can focus on the bottom line, and tie it directly to our goal.

An example of cases for _“shipping as fast as possible, and we are ok with compromising on future quality”_ could be:

* A severe bug that exists in the system. Every day that passes without a solution can cause long-term damage.
* We have a contract with a customer to ship the solution on a specific date. If we miss the deadline, there may be legal consequences.
* The company has cash flow issues. Shipping the solution early can have a huge impact on our business stability.

As you can see, using S.O.L.I.D is not always the better approach. If we care about code quality, we should definitely default to it, but we must make sure that we know the tradeoffs. Choose one solution over the other because you believe this is the best path to reach your goals. Don’t do it just because [Uncle Bob](https://blog.cleancoder.com/) or someone in your company said it’s better.

### Don’t do reviews only to get the “stamp”

![Image](https://cdn-media-1.freecodecamp.org/images/sfygBlLlFvenZwXI2tSWo06x7eoAbkYSxpzD)
_Photo by [Unsplash](https://unsplash.com/photos/hgITU7cj7k8?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Hello Lightbulb</a> on <a href="https://unsplash.com/search/photos/stamp?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

In many companies, reviews ([design](https://hackernoon.com/tagged/design) reviews, product reviews, etc.) have the same ritual. The feature owner writes the spec. Their manager then reviews it. The group schedules a meeting to review the spec. More than once, there is a feeling that the purpose of these meetings is to get the stamp from the stakeholders rather than actually engage in an open discussion. The reasons why this can happen:

* If you already have a spec ready, why would you need 7 or so people to gather in a room and “go over” it?
* The meetings tend to be boring and can turn to be a monologue when the feature owner reads the spec they wrote.
* Sometimes these meetings tend to be nit-picky. The conversation can focus on things that are not crucial for the feature success (_“why do we use int32 and not int16?”, “strings or enums?”, “tabs or spaces?”)._
* Some people are more introverted than others. Are all the voices heard, or are there only a few people that are engaging in the conversation?
* The conversation on some details can take longer than expected. Time then runs out before the feature owner can cover the whole spec, sometimes even less than half of it. This can frustrating. Moreover, if a follow-up meeting is required, it can also postpone the [decision](https://hackernoon.com/tagged/decosion) making and the whole project timeline.

### Be prepared with alternatives and goals, not with the solution

At my current company, we take a different approach. Reviews are made offline, using [Paper](https://paper.dropbox.com/) (benefiting from its features like sharing, comments, tasks which makes the collaboration more efficient). Any other online editor can work.

For the design meetings, we use a different template. The decision maker chooses the 3–4 most important open questions that are critical to the feature’s success. They then compose an alternative table like we saw before. They can also recommend an alternative, but shouldn’t be very opinionated about it. The purpose of the meeting **is** to choose the proper approach based on the project goals.

The meeting then turns from a monologue that is focused on “stamping” a solution to an open conversation about the best approach. The audience turns from being approvers to being advisors. The feature owner doesn’t need to “defend” their selected solution. It turns into a decision maker that bases their solution on the stakeholder advice. By setting time (10–15 min) for each question, you can make sure that you cover all open questions. A decision is taken by the feature owner when the time is up.

Making sure that everyone’s voice is heard, even the introverts, is just as easy as “Hey Jane, we didn’t hear your opinion, which option do you think will serve our goals? X,Y or Z?”

So next time you want to compare two or more alternatives, replace “React.js is better than Angular” with “React.js is easier to learn, more flexible, and is updated more frequently, so if we aim to quickly ramp up new engineers and move faster with the most top-notch technologies, this should be our choice between these two”.

As for “Pineapple is the worst pizza topping” — maybe some things aren’t meant to have alternatives. ?

Thanks for spending 4 minutes of your time, until next time.

-Alon

_Special thanks to:_

* _Eric Suh who drove the creation of the engineering review process at Dropbox_
* _Pierpaolo Baccichet, Steve Eisner, Gal Zellermayer, James Cowling, and Devdatta Akhawe all of whom gave valuable feedback, both as early testers of the process and as reviewers_
* [Rina Artstain](https://www.freecodecamp.org/news/how-to-make-effective-decisions-by-comparing-alternatives-99ab7d4388bb/undefined) & [Keren](https://www.freecodecamp.org/news/how-to-make-effective-decisions-by-comparing-alternatives-99ab7d4388bb/undefined) _for proofreading, reviewing this article and giving awesome technical feedback_

