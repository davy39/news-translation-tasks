---
title: Three Controversial Charts From the State of JavaScript 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T08:53:13.000Z'
originalURL: https://freecodecamp.org/news/three-controversial-charts-from-the-state-of-js-2018-ec9dda45749
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2LVJ87Dqia6wmg6ICFs7gw.png
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

  You thought stats and graphs were boring? Think again…


  “Controversial” is literally the most overused word on the Internet, with the possible
  exception of “literally”. But this time it’s true: some of the charts in our 2018
  State of J...'
---

By Sacha Greif

#### You thought stats and graphs were boring? Think again…

![Image](https://cdn-media-1.freecodecamp.org/images/1*2LVJ87Dqia6wmg6ICFs7gw.png)

“Controversial” is literally the most overused word on the Internet, with the possible exception of “literally”. But this time it’s true: some of the charts in our [2018 State of JavaScript survey results](http://2018.stateofjs.com) generated a lot more debate than others. Let’s see why!

### The Gender Gap is Real

I’m sure you’ve heard that there’s a gender gap in tech. If you had asked me last month, I’d probably have said something like 80/20% male/female. What about you, what would your estimate be?

Scroll down to see the answer!

…

Scroll down…

…

Keep scrolling…

…

A little bit more…

…

![Image](https://cdn-media-1.freecodecamp.org/images/1*oOK0MFT-1HBmwlWDrcSo6Q.png)

Imagine my surprise when our data revealed this sea of red dots and a 95/5% breakdown instead!

My first instinct was that something must be wrong with our methodology. After all a lot of people hear about the survey through places like Hacker News or Reddit, which themselves could have skewed demographics.

But the [Stack Overflow developer survey](https://insights.stackoverflow.com/survey/2018/#developer-profile-gender) confirmed that our numbers weren’t that far off:

![Image](https://cdn-media-1.freecodecamp.org/images/1*CLxrnjQUreep9qZs1y8ngw.png)

(Note: it was actually not that easy to find other developer surveys to see if ours and Stack Overflow were outliers or not. If you find any please let me know!)

As you can imagine, this chart generated a lot of disappointed tweets:

So what can be done? Our first instinct was to find ways to reach out to more women and minorities, and that’s certainly a good first step. But while making the survey itself more inclusive is necessary (and we have some ideas around that, starting with [translating it to other languages](https://github.com/StateOfJS/StateOfJS/issues/87)), it’s also important to remember that a survey only reflects reality.

We don’t want to end up focusing on making the numbers look good, and then calling it a day. So the ultimate goal should still be to make the industry as a whole as welcoming as it can be, so that future surveys naturally reflect that new state of things.

### Angular vs Angular

Ever since Angular’s big split into [Angular](http://angular.io) (new hotness) and [AngularJS](https://angularjs.org/) (old version), talking about the framework has been tricky.

And this year, I have to admit we didn’t do an especially good job of handling the matter.

First, here’s how the Angular question has been addressed over all 3 years of the survey:

* 2016: asked about both Angular and AngularJS, in two separate questions
* 2017: asked about both Angular and AngularJS, in two separate questions
* 2018: only asked about Angular

Here’s the resulting chart:

![Image](https://cdn-media-1.freecodecamp.org/images/1*CBbB0aGxHTlduVJbSkmoVw.png)

That chart shows **Angular** for all three years. The 2016 and 2017 data for AngularJS simply doesn’t factor into the chart.

We thought this was the logical thing to do: AngularJS is an old and deprecated technology, so we simply dropped it from the survey and moved on.

The issue of course, as you can maybe guess from the chart, is that many respondents didn’t see things that way. Some of them thought our question about Angular was _also_ about AngularJS, which explains the sudden rise in “would not use again” answers in 2018.

This did not go over well:

In our defense, we simply treated Angular like any other framework mentioned in the survey, using its official name (“Angular”). Maybe we should have taken the initiative to substitute something like “Angular 2+” instead, even though that’s not the official nomenclature; or at least added a special clarifying note to explain the situation.

In any case, I’ll agree that we did do a poor job of explaining the whole issue, and for that we apologize.

#### Sampling Bias

We also heard accusations of sampling bias, usually coming from either people in statistics, or people who’ve read into it a bit on Wikipedia.

Here’s something interesting to note: all three members of the State of JS team are React users, not Angular users. It seems like that’d make us more likely to have access to a React-using audience, right?

While this is certainly a possibility, most respondents found the survey through “neutral” sources like Reddit or Hacker News. Also, apart from the Angular issue already discussed, our data seems to match that of other surveys:

Unless… does the NPM team use React too? Oh the conspiracy…!

But seriously, as you might imagine, we’re already doing everything we can to spread the survey to a broader audience. And we can only hope that as the survey audience grows year after year, whatever sampling bias we might introduce will naturally evaporate.

### Should You Really Avoid Ember.js?

Our final controversy concerns our recommendation to “avoid” certain technologies.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZNfftX6TKNK7AEFiIYaO5A.png)

Well, it does say “AVOID” in all caps right there on the chart, I can’t deny that.

As a user of Ember, Polymer, or any other technology that has the misfortune of ending up in that “avoid” quadrant, this could understandably make you mad. Just because some fraction of developers may have had a bad experience with a library a few years back doesn’t mean everybody should avoid it!

I can certainly understand that sentiment, since I’m in the same boat as you. I’m a heavy [Meteor](http://meteor.com) user myself: I wrote a book about it, I’m even building an [entire open-source framework](http://vulcanjs.org) on it, yet I had to accept that Meteor too falls in the “avoid” quadrant:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fsq7YMXDMTD1KbP77o_Lew.png)

_I_ think Meteor is great, but this is not just about what _I_ think, or what _you_ think. It’s about what 20,000 developers think.

And yes, going from “most developers wouldn’t use X again” to “you should avoid X” does take a leap. We could just give you the data and leave you to form your own conclusions.

But this goes back to the whole reason we’re running the survey in the first place: helping you make decisions. If you already know and love Ember, Meteor, or any other technology, then more power to you! We have no intention of criticizing your choice.

If, on the other hand, you come to use for insight and guidance, then we think the best way to do that is to be clear, and maybe even a little blunt. Saying things like “every library has its pros and cons, and you should pick the best one for your needs” may not offend anybody, but it also doesn’t really help anybody.

### The State of (Some Of) JavaScript

At the end of the day it’s important to remember that a survey can only go so far. We do our best to be representative of the entire JavaScript ecosystem, but 20,000 developers is still only a tiny portion of the community.

We don’t think this means it’s not worth trying, though. And with your help, we believe we can keep improving things year after year.

So keep your feedback coming, whether good or bad. And of course, see you in 2019!

