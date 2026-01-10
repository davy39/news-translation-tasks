---
title: The 12 Things You Need to Consider When Evaluating Any New JavaScript Library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-12T20:51:41.000Z'
originalURL: https://freecodecamp.org/news/the-12-things-you-need-to-consider-when-evaluating-any-new-javascript-library-3908c4ed3f49
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PSo6PqzblBfox7FHlG_ITA.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Sacha Greif

  How do you know if a new technology is worth investing time into?

  For this year’s State of JavaScript survey I wanted to dig a little bit deeper,
  and not only know which tools and libraries people were using, but also why they
  were usi...'
---

By Sacha Greif

#### How do you know if a new technology is worth investing time into?

For this year’s [State of JavaScript survey](http://stateofjs.com/) I wanted to dig a little bit deeper, and not only know which tools and libraries people were using, but also _why_ they were using them.

Which means I had to find a way to translate personal preferences into cold, hard data. After some research, I came up with a 12-point scale that covers the main aspects of picking and working with any technology.

### Take the Quiz!

To make it easier for you to apply the scale to any library, I prepared a quick quiz that will take you through all 12 factors and give you a final recommendation:

#### ➡️ [Take the 12-Factor Quiz](https://stateofjs.typeform.com/to/hTRAcc)

If you’re not sure what to evaluate, just do it on a library you’re familiar with (React, Vue, jQuery…) and see how well it scores!

![Image](https://cdn-media-1.freecodecamp.org/images/BPHlsWqIAroX3tV0uIHmC0LZaMotfWjJsejy)

Or, you can read on to find out more about each factor, and see how they can be applied.

### Note: About The State of JavaScript Survey

Like I mentioned, I originally developed this scale as a way to get more granular data for the annual [State of JavaScript](http://stateofjs.com/) survey.

![Image](https://cdn-media-1.freecodecamp.org/images/vidyXkeKU1T83ZLUYmmnMZbCzpp8mU2T813d)

If you’d like to contribute and help identify the latest trends in the JavaScript ecosystem, [go take the survey](http://stateofjs.com)!

Now back to the 12-point scale.

### The Factors

Here’s the full list:

1. **?️ Features**
2. **? Stability**
3. **⚡ Performance**
4. **? Package Ecosystem**
5. ? C**ommunity**
6. **? Learning Curve**
7. **? Documentation**
8. **? Tooling**
9. **?️ Track Record**
10. **? Team**
11. **⚖️ Compatibility**
12. **? Momentum**

I’ll explain the importance of each factor, and also give you a scoring grid to show you how to evaluate it. Let’s go through the list!

### ?️ Features

The first reason why you’d pick any technology is likely for what it does.

But the key question here is knowing how far to go. React is probably the most popular front-end library out there right now, but a common complaint is that it just doesn’t do enough, leaving things like routing and state management to third-party libraries like React-Router and Redux.

In fact, this is a big part of the appeal of Vue, React’s biggest competitor. By providing official packages for these common use cases, it’s managed to offer a more well-rounded solution and gain a lot of ground.

Then again, take this too far and you might end up with a bloated, complex framework that tries to be everything to everyone.

So sometimes, a minimalist approach is what’s needed. Libraries like Lodash or Ramda let you replace your messy nested for loops with terse functional expressions, and that’s enough to make them invaluable tools.

Again, it’s all about finding the right equilibrium!

#### Scoring System

* **A:** Unlocks things that were just not possible before.
* **B:** Lets you do the same things as before, but in a better way.
* **C:** Does less than current solutions.

### ? Stability

You can have the most elegant, full-featured framework ever, but it won’t amount to much if developers run into errors every two minutes.

For that reason, a lot of tools in the current JavaScript ecosystem focus on adding stability and security to the stack. Look no further than TypeScript and Flow’s successes, or even languages like Reason.

And on the data layer side, GraphQL’s type system also contributes to making sure everything runs smoothly.

#### Scoring System

* **A:** Fewer bugs, and issues become easier to debug and solve.
* **B:** Adopting the technology does not have an impact on your software’s stability.
* **C:** New bugs and issues arise as a direct consequence of adopting the technology.

### ⚡ Performance

If you’ve ever trained martial arts, you’ll know that one of the best possible attributes you can have on your side is _speed_, not strength.

Similarly, all the features in the world are no use if it takes your app 15 seconds to load. By that time, the user has already closed the tab and you’ve lost the fight before it even begun!

In the JavaScript ecosystem, look no further than [Preact](https://preactjs.com/) to see an example of focusing on speed: its API is identical to React, so it’s not trying to compete on feature strength. But by being lighter-weight and faster to load than React, it lets you save precious milliseconds and improve your webapp’s performance.

#### Scoring System

* **A:** Lighter bundle, faster load times, or other performance improvements.
* **B:** Adopting the technology does not have an impact on your software’s performance.
* **C:** Adopting the technology slows down your app measurably.

### ? Package Ecosystem

Before investing in any new technology, it’s important to look at the ecosystem that has developed around it.

Not only is a vibrant package ecosystem a huge time-saver since it lets you piggy-back on the work of others, but it’s also a sign that the technology has reached a certain maturity level. For that reason, well-maintained third-party packages are one of the best possible signs that developers have embraced a technology for the long run.

#### Scoring System

* **A:** Ecosystem has unambiguous solutions for common concerns; third-party packages are well-maintained and well-documented.
* **B:** Budding package ecosystem with many competing new options.
* **C:** No package ecosystem to speak of, lots of manual work required.

### ? Community

Another factor to consider is the overall community. A dedicated forum or Slack channel can be a huge help when running into issues.

![Image](https://cdn-media-1.freecodecamp.org/images/PPAbpAV8OeyXs7HpsONNyQJOFjAbnJFB4CLu)
_[Spectrum](https://spectrum.chat/" rel="noopener" target="_blank" title=") is an increasingly popular middle ground between chatrooms and traditional forums._

It’s also helpful to have an existing repository of Stack Overflow answers to look up. And of course, a well-maintained GitHub issues page is a must!

#### Scoring System

* **A:** Forum and/or chatroom (Slack/Discord/etc.) with daily activity, GitHub issues addressed within a day. Many answered Stack Overflow questions.
* **B:** Forum and/or chatroom with infrequent activity.
* **C:** No community beyond GitHub.

### ? Learning Curve

An easy learning curve makes it much more likely that developers will give your framework or library a shot. It’s tempting to think that if a technology is truly disruptive people will push through any obstacle, but it’s often just not true.

A closely related (yet sometimes opposite) concept is the “adoption” curve. When it first launched, [Meteor](http://meteor.com/) was extremely easy to use (at least compared to existing alternatives) but it required you to adopt its entire stack at once, making it very hard to implement for existing projects.

React is also famous for its rough learning curve: for developers used to separating HTML and JavaScript, having to use JSX can be tough. Vue on the other hand makes it a lot easier to get started without having to rethink the way you think about front-end coding as much.

#### Scoring System

* **A:** Possible to get started in a single day.
* **B:** About a week required before becoming productive.
* **C:** More than a week required to learn the basics.

### ? Documentation

A big part of an easy learning curve is having great documentation. This is harder to achieve than it sounds, as the people writing the documentation are usually the ones with the most experience; meaning they’re also furthest removed from the new developer experience.

So writing good documentation requires forgetting what you know for a second and putting yourself in the shoes of someone just discovering your technology.

![Image](https://cdn-media-1.freecodecamp.org/images/gx6MSYtn9YlONOliEwLA07k0hQPzKuv7pldZ)
_Vue.js’ documentation is both well-designed and well-written._

It also requires anticipating common issues, understanding the user’s mental model, and most of all keeping everything up to date as your codebase changes! And all of that takes precious time away from actual coding…

Given all these factors, you can understand why good documentation is a rare and valuable thing!

#### Scoring System

* **A:** Dedicated documentation site, screencasts, example projects, tutorials, API documentation, and well-commented code.
* **B:** Basic Read Me and API documentation.
* **C:** Very succinct Read Me, the only way to know how to use the library is to look at its code.

### ? Tooling

Just like documentation, tooling is one of these things that may seem like a secondary distraction to some maintainers, but is actually vital to the popularity and success of any technology.

![Image](https://cdn-media-1.freecodecamp.org/images/W5mW8fZMfEEVdmMf5XPdtfSSsNtptGDlOamo)
_Redux’s DevTools alone make it worth considering._

I believe a big reason behind Redux’ success is its amazing Devtools browser extension, which lets you visualize the Redux store and actions in a very user-friendly way. Similarly, VS Code’s great TypeScript support has done wonders for its adoption.

#### Scoring System

* **A:** Two or more of: browser extensions, text editor extensions, CLI utility, dedicated third-party SaaS services.
* **B:** One of: browser extensions, text editor extensions, CLI utility, dedicated third-party SaaS services.
* **C:** No external tooling.

### ?️ Track Record

At the end of the day, even the most elegant, best-documented library out there will be easily dismissed as nothing more than a flash in the pan if it’s only been around for six months.

We can all recount stories of adopting the “next big thing”, only to come crawling back to good old Rails/PHP/*insert tried-and-true technology here* when things start to go bad.

![Image](https://cdn-media-1.freecodecamp.org/images/1AaI7f2T0wZ6-AW4G9g1falTwSWg0OEIK48g)
_Express: still a contender even after all these years_

For that reason, nothing can beat a solid track record. Express is one of the examples around: it was originally released in 2010, yet is still considered the default Node.js server framework despite the JavaScript ecosystem’s fast-moving pace.

#### Scoring System

* **A:** Has been around for 4+ years, adopted my major companies and well-known tech consultancies.
* **B:** Has been around for 1–4 years, used by early adopters and smaller-scale consultancies.
* **C:** Has been around for less than a year, no real adoption yet.

### ? Team

Not all projects have an existing track record. When a library is brand new, how do you judge its potential? One reliable way it to look at who’s behind it.

When React first came out, the fact that none other than Facebook was behind it was a big argument to at least try it out. Facebook then went on to release Relay and GraphQL, showing that React’s success wasn’t a fluke!

![Image](https://cdn-media-1.freecodecamp.org/images/cDZb2K2jI518D0NmjO1FX68-LkbJPqHHpe8h)
_Google Open Source: over 2000 projects covering desktop, mobile, and more._

And larger companies also have more resources to invest: Google has been able to continue maintaining the original Angular.js even after releasing newer, incompatible versions.

Of course this doesn’t mean lone maintainers can’t also create major innovations. This is how Vue.js was born after all, to say nothing of 99% of all open-source software out there.

#### Scoring System

* **A:** Maintained by a major company with a dedicated open-source team.
* **B:** Maintained by a medium-sized team of engineers with solid individual track records.
* **C:** Lone maintainer working independently.

### ⚖️ **Compatibility**

The great thing about adopting cutting-edge libraries is that they usually evolve quite fast. Sadly, that can also be a major downside!

A fast improvement rate can also mean frequent breaking changes as new best practices replace old patterns, leaving early adopters to pay the refactoring costs.

React Router generated a lot of gripes when they decided to completely change their API between versions 3 and 4. And so did Angular when they made the switch from Angular.js to the new “just Angular”.

Frequent updates are fun and exciting when you’re just starting out a new project, but once your app is up and running in production the last thing you want is having to spend weeks of refactoring and debugging every time a new version of a library comes out.

#### Scoring System

* **A:** Updates are mostly backwards-compatible, deprecations are handled with warnings, and incompatible older versions are maintained for two years or more.
* **B:** Breaking changes do happen but are well documented and are rolled out gradually.
* **C:** Frequent breaking updates requiring major refactoring without the proper guidance.

### ? Momentum

Last but not least, momentum. In other words, hype.

Hype is often seen as a bad thing (“don’t fall victim to the hype”), as an indicator of style over substance. But it doesn’t always have to be.

With enough momentum, a new software project can attract more users and more contributors, which means bugs are found and fixed faster, a package ecosystem can develop, and everybody ultimately ends up better off.

![Image](https://cdn-media-1.freecodecamp.org/images/FEHGvt7qEHqpX68FPpXtVLep1wkX9CcN8RuY)
_JavaScript Rising Stars, our project charting the growth of popular JavaScript libraries_

But yes, there’s also the other side of the coin: too much hype too early can expose potential users to an unfinished version riddled with issues, turning them off for good. Like they say, you only get one chance at making a first impression.

#### Scoring System

* **A:** Hype Level Over 9000: top of Hacker News, thousands of GitHub stars, talks at major conferences.
* **B:** Some interest around the initial launch, hundreds of GitHub stars.
* **C:** Lone developer toiling away in obscurity. One day I’ll show them! I’ll show them all!!

### Update: A Few More Factors

Some of you suggested a few more great factors to look at. Something to consider for a potential version 2.0 of the scale!

* **Scalability**: how well does the technology work for large projects.
* **Adoption**: who else is using the technology currently?
* **Compatibility**: how well does the technology work with other existing techs?
* **Decoupling**: how easy is it to migrate out of the technology if you want to stop using it?

### Case Study: Apollo Client

Let’s put our scoring system to the test by applying it on an actual, real-world library: [Apollo Client](https://github.com/apollographql/apollo-client).

![Image](https://cdn-media-1.freecodecamp.org/images/XXcqlgMj6hXveo-8JWEyXxCHu09aklqzP6Oi)
_Apollo Client_

Apollo is a GraphQL client, in other words it’s a library that will query a GraphQL endpoint and load its data on the client for you. It also handles things like caching, making sure data is not duplicated, and sending said data to your front-end library of choice.

Let’s see how it does on our scoring system!

#### ?️ Features: B

Apollo gives you better ways to query data, so it’s more of a gradual improvement over existing tools.

#### ? Stability: A

Adopting Apollo and GraphQL does make it easier to reason about your data and track down issues.

#### ⚡ Performance: B

Apollo does include tools to optimize your data loading, but overall should not have an outsized impact on your app’s performance either way.

#### ? Package Ecosystem: A

Apollo supports packages called [links](https://www.apollographql.com/docs/link/#linkslist) in order to enable extra features.

#### ? Community: B

Apollo does have a very active Slack chatroom, but in my experience questions can sometimes go unanswered and it can be hard to get replies from busy core team members.

#### ? Learning Curve: B

Learning all the nuances of Apollo can actually be a challenge, especially if you’re learning to use GraphQL at the same time.

#### ? Documentation: A

Good, well-maintained documentation provided for multiple front-end frameworks, as well as example codebases.

#### ? Tooling: A

Browser extension and a dedicated [metrics platform](https://www.apollographql.com/engine/).

#### ?️ Track Record: B

Apollo itself is still fairly new, but so is the GraphQL space in general.

#### ? Team: A

Highly competent and well-funded team with experience launching other open-source projects ([Meteor](http://meteor.com/)).

#### ⚖️ Stability: B

Breaking update from v1 to v2, but overall good stability and backwards compatibility since.

#### ? Momentum: B

Apollo may not be a household name yet, but it’s the dominant player in its niche despite Relay’s head start.

#### Overall Grade: A ?

With 29 points out of a maximum of 36, Apollo ends up doing really well! Even if there will always be areas for improvement, it’s easy to see why it’s been adopted in production by many teams who need a reliable way to deal with GraphQL data.

### Other Approaches

The folks at NPMS have implemented [a similar rating system](https://npms.io/about), automated from looking at GitHub and NPM data. This makes their scoring less subjective, but no the other hand it doesn’t cover things like documentation or community.

On the raw data side, you can also get some cool stats with NPM Trends:

![Image](https://cdn-media-1.freecodecamp.org/images/9kWi9wu6EnMAdvS80GTY8QkczMZFfopW40bv)
_NPM Trends_

And learn more about which libraries are currently popular on Best of JS:

![Image](https://cdn-media-1.freecodecamp.org/images/Zmb9zNPTaMXGupSBBzzIo2rroBrMfw2RAMbR)
_Best of JS_

And of course, there’s always [last year’s State of JS survey results](https://2017.stateofjs.com/):

![Image](https://cdn-media-1.freecodecamp.org/images/0L1S4aGClqR8O8vKhUFrGICcZ-56yBfZzWuZ)
_The State of JavaScript 2017 survey results_

What about you, how do you usually evaluate libraries? Leave a comment to let me know!

### Conclusion

This scale is by no means an absolute measure of a library’s worth. After all this will always be mostly subjective, and strongly depends on your project and your needs.

Still, we’re hoping it can serve as a useful starting point. If nothing else, it can serve as a checklist to make sure you’re not overlooking anything important before making that big jump into the future!

