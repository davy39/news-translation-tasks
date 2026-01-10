---
title: How to avoid common beginner pitfalls and start coding like a pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-31T22:48:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-common-beginner-pitfalls-and-start-coding-like-a-pro-3de81c6affbe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lQDZ3LDJf5bKwvLtocFGJw.jpeg
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Dmitri Grabov

  Learning to code is tough. We’ve all encountered cryptic errors and code breaking
  for no obvious reason. Sadly, this experience is part of learning to code. There
  are a few steps you can take to improve your code quality and prevent ...'
---

By Dmitri Grabov

Learning to code is tough. We’ve all encountered cryptic errors and code breaking for no obvious reason. Sadly, this experience is part of learning to code. There are a few steps you can take to improve your code quality and prevent common bugs.

### Avoid copy pasting code

A lot of the learning you will do as a beginner will come from repetition. It’s not exactly glamorous, but by the time you’ve written a for loop for the 100th time, you’ll be doing it almost without thinking.

You will often be tempted to copy and paste code to save yourself the hassle of typing it out. You should avoid it at all cost. There might be a subtle difference between the code you want to write and what you are copying. This could introduce a subtle bug that could be tricky to track down.

> _When you copy code, you bypass the cognitive process entirely._

Make sure you understand the code you write as much as you can. When you copy code, you bypass the cognitive process entirely. Even if the code you copied does work as intended, you have not learned much from pasting it. Each time you type your code in full, you become that much more familiar and comfortable with it.

### Sensible names

> There are only two hard things in Computer Science: cache invalidation and naming things.

> — Phil Karlton

Use nouns for variable and property names. Make them as descriptive as possible.

Always use full words and avoid abbreviations. Different people can interpret abbreviations in different ways. This could make it more difficult to understand what the code does. For example, `intlSize` could mean either `internationalSize` or `internalSize`. The important clue in a name is lost because of the abbreviation.

When referring to the same thing across your code base, use the same name. For example, avoid referring to `doorColour` as `colourOfDoor` or `doorColor` in other places. This will save you bugs caused by using wrong variable names. Also, the consistency will save you time looking up the exact variable name each time.

Avoid generic, non-descriptive names like `data` or `process`. They could mean anything and do not provide much information about their purpose.

### Consistent indentation

Consistent code indentation makes it easier to spot potential bugs. This is what professional developers do without thinking. Very few of them talk about it because it is so obvious to them. Yet, few tutorials stress the importance of using consistent indentation.

In the examples below, we indent using tabs, however spaces are also acceptable. The key is to pick which one you want to use and apply it consistently. Do not mix tabs and spaces in your code.

So what does correct indentation look like? Each time you insert an HMTL tag inside another, add a new line and tab in front of the new tag to indent. When you close an HTML tag, add a new line and remove a tab from your indentation.

![Image](https://cdn-media-1.freecodecamp.org/images/uwvEIwAGKDftbiikMfHJROTWS4DO28VzDu3i)

Here the inner tag is the `img` tag. See how it is indented one tab? Also, note how the left edge of the closing `div` tag lines up with the left edge of its opening tag.

This approach becomes super important when you have hundreds of tags on a page. If you have followed the process correctly, your final closing tag should flush with the left hand-side of your page. This makes a convenient check for code correctness.

Let’s see how we can use indentation to spot missing tags.

![Image](https://cdn-media-1.freecodecamp.org/images/NlNKtp8StBvnQLJKAfJLDOzk6iCpzSzJYlSE)

See how in the example above the closing `div` tag on line 14 does not line up with the opening `div` tag on line 1? That is a clue that something is missing. In this case, we missed the closing `ul` tag. Once we add it, the closing `div`falls in line with its opening partner

![Image](https://cdn-media-1.freecodecamp.org/images/o7Wu3YOVNchqWmm-NIeqrZtGaw4dydrW4OUx)

A similar method should be applied when writing JavaScript. We do not have tags in JavaScript, but we do have “braces” or “curly brackets”. They look like this `{}`. Each opening brace must have a matching closing brace. They are used to denote blocks of code. Each opening brace should be followed by a new line and a tab to indent the content. The closing brace should line up on the left hand side with the left hand side of the line of its corresponding opening brace.

![Image](https://cdn-media-1.freecodecamp.org/images/yG56kVIY4ByfAtnVf0fyvXBUAe5FkkKoHUA9)

See how the brace on line 11 is aligned with the left hand side of line 1 where its opening brace is. Similarly, line 4 aligns with line 8 and line 5 aligns with line 7.

When applied correctly, indentation should give your code a clean, pyramid-like structure. This will make it much easier to spot where each block of code ends and begins. Also, missing braces will now be much easier to spot than if they were scattered all over the page.

### Pay attention to syntax highlighting

A modern text editor, such as Sublime or Visual Studio Code, will highlight your code.

![Image](https://cdn-media-1.freecodecamp.org/images/SJA91kb2XkblOkiNIIuqkFqvyzTlJXWX3Q8V)

See how the braces, tag name, attribute name, and attribute value are each highlighted with the same color?

Now take a look at the code below.

![Image](https://cdn-media-1.freecodecamp.org/images/nyAcvhPoWb38HWWg7XTTgHpCfgS5HHdrtctq)

See how the nice, consistent highlighting has suddenly shifted? Orange text, which is used to denote attribute value, has spilled over the next few lines. That is a massive clue that something has gone wrong in our code. In this example, it is because we have missed the closing quote marks on the `href`attribute value. Spotting an error like that without code highlighting would be very difficult and time consuming.

Developers can easily waste days trying to hunt down a subtle error like that. Pay attention to code highlighting to help you spot bugs like this.

### Success will take care of itself

Being a good developer is the sum of attention to detail and dozens of habits.

By paying attention to small things like indentation, you will develop an appreciation for structure and scope. Thinking carefully about function and variable names will help you understand their purpose and how to best accomplish it. Syntax highlighting will help you spot and fix a typo before it becomes a bug. Typing all code out in full is the first step to developing familiarity with syntax, which in turn will lead to an understanding of how code behaves.

All these small details which at first seem insignificant will, with practice, form the foundation of your expertise. Pay attention to getting those details right, and success will take care of itself.

Dmitri Grabov is the founder of [Constructor Labs](http://constructorlabs.com) who run a 12 week, JavaScript [web development bootcamp in London](http://constructorlabs.com/course). Next class starts on 29th May and fees are £3,000. [Applications are open now](http://constructorlabs.com/admission) and places will be allocated on a first come, first served basis.

