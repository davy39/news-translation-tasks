---
title: What growth engineers can teach us about engineering
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-12T15:39:06.000Z'
originalURL: https://freecodecamp.org/news/what-growth-engineers-can-teach-us-about-engineering-f8bd38516e3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oFDCLzwXGS8UHwP2rl6MKA.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jonathan Z White

  I’ve been working as an engineer on the growth team at Airbnb for a couple of months
  now.

  Since I’m in an environment full of passionate developers, I wanted to share some
  of the good engineering traits I’ve observed in the engine...'
---

By Jonathan Z White

I’ve been working as an engineer on the growth team at Airbnb for a couple of months now.

Since I’m in an environment full of passionate developers, **I wanted to share some of the good engineering traits I’ve observed in the engineers around me.** Specifically, the growth engineers.

#### Growth team

First, if you’re not familiar with what a growth team is, here is some background. **Growth teams are data-driven groups that drive the growth of product at companies.** They are composed of data scientists, designers, engineers, product managers, and marketers. A pretty eclectic selection of people.

Growth teams run experiments. Experiments test new product experiences against old ones. The goal of experiments is to optimize metrics like activation, engagement, and conversion.

![Image](https://cdn-media-1.freecodecamp.org/images/wQpmyyMA0PVZewisE9NRF2pswkT22Cv38nJL)
_Growth teams run experiments. They’re like mad scientists itching to make a new discovery. ([image credit](https://dribbble.com/shots/2755418-Mad-Alchemist" rel="noopener" target="_blank" title="))_

You can think of experiments like a game of hot and cold. You run an experiment, you move in a direction, and the data tells you if you’re hot or cold. You keep doing this until you reach the hot spot.

Traditionally, experiments are composed of a **hypothesis, test, outcome,** and **learning.**

**Hypothesis:** A product hypothesis is a statement based on a set of assumptions about a product. For example, the growth team at Medium might make the following hypothesis:

> “If we automatically open the iOS Medium app every time a user goes to Medium on their mobile browser, we will drive more traffic to our iOS app.”

**Test:** A test is a lightweight prototype of the feature or solution suggested in the product hypothesis. It is designed to validate the product hypothesis and its assumptions.

**Outcome:** The outcome is the results of the test.

**Learning:** The learning is the insight that growth teams gain from the data gathered from the experiment.

The main takeaway is that growth teams approach problems in a structured and scientific way. This mentality reflects the problem solving techniques that engineers use to come up with solutions.

#### Growth engineers

Growth engineers use experimentation to move fast and build momentum. They are rigorous in their methodologies and there is a lot that can be learned from them.

![Image](https://cdn-media-1.freecodecamp.org/images/jPL9CNbnwDd6IxrQDvRnq-KqUHrIVNi7pG2t)
_Creation speed is key. ([Image credit](https://dribbble.com/shots/780594-Move-fast-and-break-things" rel="noopener" target="_blank" title="))_

#### Growth engineers are not afraid to be wrong

Growth engineers embrace failure. If a product hypothesis is wrong, as long as there was learning, the growth team can come out net positive.

Because of this mentality, growth engineers understand that they don’t always have to have the right answer. The optimize for learning. They listen and learn from users.

![Image](https://cdn-media-1.freecodecamp.org/images/nPg9LgwEZbu0DOpDg6yJm2S5LbqZYLd3Es-D)

**Good engineers learn from their failures.** Ultimately, this mentality leads to better technical and product outcomes.

#### Growth engineers focus on metrics

Growth engineers carefully instrument their tests. When running an experiment, they define a set of metrics they want to track. Then they add ways to collect anonymized data to what they build.

Let’s say a growth team wanted measure the effectiveness of a modal signup experience. An engineer would build the experience. They would then add tracking to see how many people signed up using the new experience versus the old one.

Using a data-driven approach, growth engineers can iterate toward an optimal product experience.

![Image](https://cdn-media-1.freecodecamp.org/images/aPE0nOVuZT0wJXKsThRT8TNyikYZajARXiOi)
_Growth engineers use data to come up with product insights. ([Image credit](https://dribbble.com/shots/1193016-Mountain-Graph-gif" rel="noopener" target="_blank" title="))_

**Good engineers define success metrics. Metrics move them towards an explicit goal.** Metrics also prevents them from losing focus and getting distracted by things like new technologies and unnecessary complexity.

For example, an infrastructure engineer’s success metric might be to reduce the build time of an app. The engineer could run a series of experiments to identify the severeness of the different performance bottlenecks. Using the data from the experiments, the engineer would be able to better identify where they could have the most impact.

#### Growth engineers test for edge cases

Good growth engineers carefully consider edge cases when building and testing new experiences.

![Image](https://cdn-media-1.freecodecamp.org/images/z2guRNUSYNEeoUY0fUJYGniwwd3fCUFZNxst)
_Edge case… Get it? ([Image credit](https://dribbble.com/shots/2496202-Suitcase-Icon" rel="noopener" target="_blank" title="))_

Imagine an engineer is trying to optimize a signup flow with an experiment. The old experience was a full page redirect to a signup or login page. The new experience is a modal.

An edge case for the modal experience might be that on iOS 8, the modal fails to open. If the engineer fails to cover this case, then the results of the modal experiment might show a drop in signups, even though the modal experience was better.

**Good engineers test for edge cases. They work toward delivering delightful experience for everyone, not just the majority.**

#### Growth engineers are pragmatic

A lot of growth engineers have pragmatic attitudes towards making technical decisions.

A growth team might come up with an idea for a new product feature. A good growth engineer would figure out how to build a prototype to validate the feature. The prototype might not be perfect but it gets the job done.

Once the feature is validated, meaning it’s something users want, then the engineer would go on to refactor the code. This approach reduces the amount of engineering time spent on features that end up getting retired.

![Image](https://cdn-media-1.freecodecamp.org/images/xmbRJN3xocSa6aR8VaHXa8IIjcwnGPIkiZjX)
_You can’t write perfect software. Did that hurt? It shouldn’t. Accept it as an axiom of life. Embrace it. Celebrate it. — Andrew Hunt, The Pragmatic Programmer_

Seasoned software engineers knows that there is a trade off between moving fast and taking the time to ship perfect code. **Being pragmatic means that an engineer can evaluate trade offs and identify the route that ultimately increases the productivity of their team.**

#### Growth engineers have good product intuition

Product intuition is the intangible ability to make good product decisions. It comes from being passionate about building products and observant of the products available today.

![Image](https://cdn-media-1.freecodecamp.org/images/zj3gfOzEw6T3z4xwcdvlcfJFzIVzjDLDTvX2)

Growth engineers need good product intuition. Experiments are designed to collect data to test product assumptions. However, without product intuition, no assumptions can be made.

Product intuition is an asset to all engineers. It brings them one step closer to their users. **The more accurate product assumptions are, the more time teams can spend on building the right features.**

There is a lot we can learn from listening to and observing the engineers around us. Surround yourself with people smarter than you.

A big thanks to [Chris](https://twitter.com/ChrisAWren) for teaching me the ropes as a growth engineer.

What traits do you consider important in an engineer? Leave a note below or [tweet](https://twitter.com/JonathanZWhite) at me.

You can find me on Medium where I publish every week. Or you can follow me on [Twitter](https://twitter.com/JonathanZWhite), where I post non-sensical ramblings about design, front-end development, and virtual reality.

_P.S. If you enjoyed this article, it would mean a lot if you click the ? and share with friends._

![Image](https://cdn-media-1.freecodecamp.org/images/yJGjyJUSWwbfc-pA-UxBeSqNkPX5lSfVTJhY)

![Image](https://cdn-media-1.freecodecamp.org/images/AmLvc2yTvkozjPZYxvh357pnm0uKXZTcqA27)

