---
title: Don’t copy-paste code. Type it out. ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-21T10:29:51.000Z'
originalURL: https://freecodecamp.org/news/the-benefits-of-typing-instead-of-copying-54ed734ad849
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wgbmuDgBQ6N-kOrbD-qMFA.jpeg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Fagner Brack

  Typing code can help you develop a learning mindset

  Want to break some code? Change it real quick before you even understand what it
  does.

  Now you’re practicing Cargo Cult programming — a style of software development where
  you ignore...'
---

By Fagner Brack

#### Typing code can help you develop a learning mindset

Want to break some code? Change it real quick before you even understand what it does.

Now you’re practicing Cargo Cult programming — a style of software development where you ignore how a piece of code works and its relationship with the code around it.

> The term _cargo cult programmer_ may apply when a computer programmer that is inexperienced with the problem at hand [copies some code](https://en.wikipedia.org/wiki/Copy_and_paste_programming) from one place to another with little or no understanding of how it works or whether it is required in its new position.  
>   
> — [Cargo Cult Programming on Wikipedia](https://en.wikipedia.org/wiki/Cargo_cult_programming)

When a developer **copies** a piece of code that they don't understand and uses it in the hope of fixing some problem, they’re practicing Cargo Cult programming. This increases the risk of unintended side-effects.

When a developer **reads** a piece of code that they don't understand and still changes it in the hope of fixing some problem, they’re also practicing Cargo Cult programming.

The problem, in this case, is not that the developer is copying something. Anyone can copy a snippet of code, understand it, learn from it, use it, and still have a lower risk of unintended side-effects.

Cargo Cult programming, on the other hand, represents a fundamental misunderstanding of proven steps for learning from other people's code.

Here’s the most efficient way to learn in this context:

1. Read a piece of code.
2. Understand all features of the language that are being used there.
3. Understand all the features of the libraries/frameworks that are being used there.
4. Learn the basics of those libraries/frameworks.
5. Understand what every line does and the purpose of those libraries/frameworks in the context of that piece of code.

For someone who starts working with a new language, this is going to be extremely hard. The amount of information a human needs to retain to efficiently understand even a small snippet of code is so huge that it might be forgotten right away. What we can do is leverage certain aspects of how the human brain is used to learning things — consciously or unconsciously — with some proven techniques.

One of those techniques is [blocked practice](https://psychologywod.com/2013/08/18/blocked-practice-vs-random-practice-shake-things-up-in-your-training-and-in-your-life/). It’s basically where you learn by “performing a single skill over and over, with repetition being the key.”

This isn’t the best way to learn, though. [It’s proven](https://psychologywod.com/2013/08/18/blocked-practice-vs-random-practice-shake-things-up-in-your-training-and-in-your-life/) that, when you learn through interleaving different variations of the same skill, you’ll learn more efficiently.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XLZ9M1R2F2BN-YKpqKm_OQ.jpeg)
_The Cone of Experience, from [a post about this](http://ocw.metu.edu.tr/file.php/118/dale_audio-visual_20methods_20in_20teaching_1_.pdf" rel="noopener" target="_blank" title="">Dale, Edgar. Audio-Visual Methods in Teaching (p. 39)</a>. The graph shows two extremes between direct experience (bottom) into pure abstraction (top). Intuitively we could assume that reading or lectures (abstract visual symbols) could have less retention rate than practice (Direct, Purposeful Experiences). Note: There is evidence that the famous <a href="https://www.fitnyc.edu/files/pdfs/CET_Pyramid.pdf" rel="noopener" target="_blank" title="">Learning Pyramid</a> might be a knock-off of the Cone of Experience, with added numbers that seem to <a href="http://www.willatworklearning.com/2006/05/people_remember.html" rel="noopener" target="_blank" title="">have been made up</a> (I have created <a href="https://hackernoon.com/the-danger-of-relying-on-abstractions-dfa04a8d553d" rel="noopener" target="_blank" title="))._

In software engineering, we can leverage both blocked and interleaving learning practices when we **type** the code in different contexts, instead of just **copying and pasting** it.

When copy-pasting snippets, we’re just reading (if we even bother doing that). And according to the relationship of the Cone of Experience, we might learn only a small portion of the information we consume because it’s too abstract.

Contrast this with learning better by actually typing out that piece of code. This is a more direct and purposeful experience. It forces your brain to understand all those different patterns and learn more efficiently.

> Typing code instead of copy-pasting it provides a better learning ROI because we’re practicing instead of just reading.

Naming things is considered one of the most difficult aspects of programming. When we copy code without understanding it, we run the risk of breaking something by overwriting variable names, function names, or classes.

If we instead understand the code first, then type it up in our own words, we can rename things in a way that suits our app and ensures we don’t have any [naming collisions](https://en.wikipedia.org/wiki/Naming_collision), even if the final result is functionally the same as the piece of code we’re basing upon.

Besides that, if we copy the code from one place in our codebase to another, there’s a chance that we’ll copy tokens that are unnecessary or forget to change tokens that should have been changed.

Take the following HTML snippet, for example:

```html
<label for="name"></label>
<div class="input-wrapper">
  <input type="text" id="name">
</div>
```

When duplicating that code to create a new input, we’re likely to forget to change the _for_ attribute of the _label_ element, which will break the intended behavior for the new input.

```html
<label for="name"></label>
<div class="input-wrapper">
  <input type="text" id="name">
</div>

<label for="name"></label>
<div class="input-wrapper">
  <input type="password" id="password">
</div>
```

This example is interesting because it’s the kind of functionality that is hard to test, even with visual regression. It heavily depends on static testing — like a code review — to make sure that the code was written for the intended purpose. (In this case, to propagate mouse events to the input for the same _id_ of the label _for_ attribute.)

The same thing happens with tests. When we copy an already passing test instead of creating a new one from the scratch, we run the risk of not changing necessary tokens that would otherwise cause that test to fail.

In this case, though, we can prevent this mistake by using [Test Driven Development](https://medium.com/@fagnerbrack/why-test-driven-development-4fb92d56487c) — a mindset based on creating a failing test first, then change the application code to make it pass. This mindset allows us to be confident that we’re less likely to miss something or [create false-positives](https://medium.com/@fagnerbrack/mocking-can-lean-to-nondeterministic-tests-4ba8aef977a0).

Instead of copying code without understanding it, learn from other people's code and practice on top of it. This will maximize your learning ROI.

After all, the most valuable resource of a developer is the brain — not the fingers.

Thanks for reading. If you have some feedback, reach out to me on [Twitter](https://twitter.com/FagnerBrack), [Facebook](https://www.facebook.com/fagner.brack) or [Github](http://github.com/FagnerMartinsBrack).

