---
title: “JavaScript is easy!” They Told Me ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-23T09:27:05.000Z'
originalURL: https://freecodecamp.org/news/ok-now-ill-learn-how-to-program-in-javascript-2c7847414830
coverImage: https://cdn-media-1.freecodecamp.org/images/1*E_VitjYO3ku_IhUHasRBHw.png
tags:
- name: agile
  slug: agile
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Fagner Brack

  Junior Developer: Ok, now I’ll learn how to program in JavaScript! Where should
  I start?

  "Senior" Developer: That''s very easy, you don''t even need to write a lot of code!
  Just go to npm, install the Zebra and Koala Open Source modules...'
---

By Fagner Brack

**Junior Developer:** Ok, now I’ll learn how to program in JavaScript! Where should I start?

**"Senior" Developer:** That's very easy, you don't even need to write a lot of code! Just go to npm, install the Zebra and Koala [Open Source](https://hackernoon.com/lets-implement-the-open-source-model-but-which-open-source-a89c82d1b494) modules, and you're done!

**Junior Developer:** Cool!

**npm:** Hi little grasshopper how can I be of assistance?

**Junior Developer:** Give me the Zebra and Koala modules.

**npm:** Of course, here they are.

**Junior Developer:** All tied up. Now my work is done!

*One day later*

**Junior Developer:** Now I need to add this feature. Where should I start?

**“Senior” Developer:** That’s very easy, you don’t even need to write a lot of code! Just go to Zebra's Github repository and ask them to implement it!

**Junior Developer:** Hi Zebra, I need to add this new feature, would you help me out?

**Zebra:** Of course, create a Pull Request.

**Junior Developer:** Here it is.

*2 days later*

**Zebra:** Your Pull Request is not good, you need to fix a few things.

**Junior Developer:** Here it is.

*2 days later*

**Zebra:** Now your Pull Request is good, I have merged.

**Junior Developer:** Thanks. Now my work is done!

*3 hours later*

**Junior Developer:** Now I need to fix this bug. Where should I start?

**“Senior” Developer:** That’s very easy, you don’t even need to write a lot of code! Just go to Koala’s Github repository and report it!

**Junior Developer:** Hi Koala, there's a bug in your module.

*2 days later*

**Junior Developer:** Hi Koala, are you there?

*1 week later*

**Junior Developer:** Is anybody maintaining this module?

*1 week later*

**Junior Developer:** I'll fork and fix it. Done.

*6 months later*

**Junior Developer:** Now I need to add this other feature. Let's look up which module I need to change first:

![Image](https://cdn-media-1.freecodecamp.org/images/1*SRxZPGixj9CQraELn7L2Kw.png)
_The diagram of the Junior Developer project's dependencies. It's a bunch of scratches forming an unreadable spaghetti._

**Junior Developer:** Err… I guess something went really wrong… JavaScript is so hard and complicated! What should I do now?

**Real Developer:** The problem is not JavaScript.

An external dependency tends to be too generic and therefore has a lot of complexity to account for edge cases you probably don’t have.

As a principle, you need to reduce your dependency on an external code as much as you can. Over time dependencies will incur a cost of change if you rely on them for the **core purpose** of your project.

Evaluate their need critically.

It’s possible to write your own code for things a generic module can already do for you without having to reinvent the wheel, **as long as you design it correctly.** That includes (but is not restricted to) [no side-effects](https://hackernoon.com/this-is-how-to-get-the-best-out-of-front-end-components-52ee29dfb4ae), [low coupling](https://medium.com/@fagnerbrack/why-do-you-need-to-know-package-coupling-fundamentals-8e0fa8e33e20), [high cohesion](https://medium.com/@fagnerbrack/why-do-you-need-to-know-package-cohesion-fundamentals-8a3510cba2c1), [proper interface](https://codeburst.io/why-do-you-need-to-know-interface-fundamentals-a129ac6ab0c3), [enough affordance](https://hackernoon.com/affordance-in-software-design-12cc0d9d2721), [no crap testing tools](https://hackernoon.com/a-test-is-as-good-as-its-ability-to-fail-when-it-needs-to-b4b8f212119a), [code that can be deleted](https://medium.freecodecamp.org/code-that-dont-exist-is-the-code-you-don-t-need-to-debug-88985ed9604), [no "over-engineering"](https://hackernoon.com/how-to-accept-over-engineering-for-what-it-really-is-6fca9a919263), [no copy/paste](https://medium.freecodecamp.org/the-benefits-of-typing-instead-of-copying-54ed734ad849), [strict](https://medium.com/@fagnerbrack/the-strictness-principle-9997e483cafb), [small](https://medium.com/@fagnerbrack/why-small-modules-matter-4e4d629321b8) and [without false positive tests](https://medium.com/@fagnerbrack/mocking-can-lean-to-nondeterministic-tests-4ba8aef977a0).

If you don't design it correctly, you'll end up in the same mess, or even worse.

If you’re a plumber and the pipe leaks, it’s your responsibility to fix it. Not somebody else’s.

It’s all about applying software principles and [techniques](https://medium.com/@fagnerbrack/the-trick-to-write-better-software-lies-on-the-technique-944015f84ce4). It’s about learning how to program.

[Don't blame the scalpel.](https://hackernoon.com/the-doctor-and-the-scalpel-78656f508c9a)

**Junior Developer:** Ok, now I’ll learn how to program. Can you help me?

**Real Developer:** Yes.

*7 years later*

**New Junior Developer:** Ok, now I’ll learn how to program in this popular language! Where should I start?

**Former Junior Developer:** I can teach you, but that's **not** easy.

I've been through this.

Sit down.

Let's talk.

Thanks for reading. If you have some feedback, reach out to me on [Twitter](https://twitter.com/FagnerBrack), [Facebook](https://www.facebook.com/fagner.brack) or [Github](http://github.com/FagnerMartinsBrack).

Wanna chat in person? You can find me in the [**Sydney Software Crafters meetup**](https://www.meetup.com/Software-Crafters-Sydney/).

