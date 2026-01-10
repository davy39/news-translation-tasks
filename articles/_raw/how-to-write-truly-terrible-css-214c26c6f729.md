---
title: How to write truly terrible CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T15:49:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-truly-terrible-css-214c26c6f729
coverImage: https://cdn-media-1.freecodecamp.org/images/1*O1a0MYPIXEao7xRij_O7AQ.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Emmanuel Ohans

  Everyone talks about ‘tips’ and ‘pro-tips’ for writing great CSS.

  That’s fine, but maybe seeing what bad CSS looks like will give you a different
  perspective. Heck, it may even do you some good!

  Let me take you through a journey on ...'
---

By Emmanuel Ohans

Everyone talks about ‘tips’ and ‘pro-tips’ for writing great CSS.

That’s fine, but maybe seeing what bad CSS looks like will give you a different perspective. Heck, it may even do you some good!

Let me take you through a journey on how to write really bad CSS.

Ready?

![Image](https://cdn-media-1.freecodecamp.org/images/w3bFCZdYDt-qHJf85m14wVykMZ2vXfwDaHil)

Note: even if you swear by CSS-in-JS and do not love vanilla CSS, we all agree on thing: we all still have to know some CSS…

So, whether you write CSS, or some superset such as [SASS](https://sass-lang.com), or just [CSS-in-JS](https://hackernoon.com/all-you-need-to-know-about-css-in-js-984a72d48ebc), you will still benefit from knowing exactly what bad CSS looks like.

#### Who Writes Comments? No one.

![Image](https://cdn-media-1.freecodecamp.org/images/FbkAby9gdFaRJyOXcXG9D3N2mrSloefCGdtB)
_No comments? Actual code I wrote sometime ago but stripped out all comments ?_

It’s so easy to slip here that you won’t notice very quickly.

We all know it. You’re so smart, everyone else doesn’t come close. Even though CSS isn’t the most expressive of “languages”, you can make assumptions about browser quirks, fix them, and assume you’ll understand what you’ve done few weeks down the line.

How smart, huh?

Put your pride aside, and save yourself and other teammates the stress.

If you’re using a not-so-obvious technique, or have fixed some browser quirk, or anything at all you think isn’t expressive enough, write that comment! It doesn’t hurt.

#### The Land of Complex Selectors

![Image](https://cdn-media-1.freecodecamp.org/images/RxyN6FyWgWoXqbvgn3-a7nC499Qf9ROvgE9j)

Yeah! You just learned CSS and feel on top of the world. So, time to show off some selector muscles.

Bad move.

By making selections with too many CSS selectors, you may have successfully made your CSS extremely unmaintainable. It is now highly dependent on the HTML structure of your app.

If the structure of the markup changes slightly, you need to go refactor your CSS as well. Not the easiest of workflows.

Just add a class to the element and get on with life!

Even in scenarios where you need to qualify selectors with multiple classes, always favour simplicity.

Simple is good, almost always!

#### Performance? Ditch That!

![Image](https://cdn-media-1.freecodecamp.org/images/eg1zeTeOEHbfMYn4FqghXZBXTvumo-7BBWEA)

So, I get it. You just don’t care about performance. You don’t care about the business, clearly. If you did, you wouldn’t annoy your users with your terrible non-performant selectors.

But wait…

I understand that computers have grown faster and browsers continue to be optimised. Regardless, simple selectors should always be preferred, and understanding how the browser traverses the DOM to find your selector is still a thing!

Chances are, you read through your selectors from left to right.

However, the browser matches the selectors from right to left, so it can eliminate elements that don’t match as quickly as possible.

If you knew this, you’d probably be more lenient on the browsers. They deserve your love.

Considering the example graphic above, the browser will match all elements (*) and also check if they are descendants of `body`.

```
body * {  ... } 
```

But why? Almost every visible element is ideally a descendant of the `<bo`dy> element. That’s just a needless inefficient check.

#### I Suck at Naming Things, so I don’t even bother.

> There are only 2 hard things in computer science. Naming things and …

Yeah, I think you already heard that somewhere. Naming things can be hard, but that doesn’t mean you shouldn’t give them some thought, or go completely cryptic.

I doubt there’s any situation where it makes sense to use single letters as class names.

```
.u {  font-size: 60rem;}
```

And what about super-specific class names?

```
.former-black-now-red-paragraph {  color: red;}
```

Those don’t do any good, either.

While the name may seem to convey some meaning, you very likely have broken a huge part of the class’s re-usability. Which, by the way, is the primary reason for having classes.

Now, if you wanted to style a regular `red` the paragraph, the previous name is just so specific, it wouldn’t make sense.

Use meaningful names, but just don’t overdo it.

#### I Heard Classes were Great. Overuse them!

![Image](https://cdn-media-1.freecodecamp.org/images/Lf3jWnJxes3KHuGApVOUOjhq3dgc4TDOBOga)
_hmmm…. When possible, avoid over modularised classes_

Classes are great, and everyone loves them. But, as with everything else, too much of something is generally a bad idea.

You see, if a group of classes will mostly be used together, just group them into one class.

When you choose to group these classes is perhaps subjective. If you’re building an atomic library of some sort, you may tend towards this.

If you’re writing a large app, you’re likely better off grouping classes in a meaningful way, as opposed to having a ton of classes on a single element.

When possible, avoid over modularised classes.

#### I am a CSS Purist. I don’t do SASS, LESS, etc.

You’re a CSS purist, I’m a CSS purist, we’re both purists. Let’s get that out of the way.

Now, to the bone of contention.

There are definitely use cases where just writing vanilla CSS is great! For example, if I’m not using a [CSS-in-JS](https://hackernoon.com/all-you-need-to-know-about-css-in-js-984a72d48ebc) solution for my [React](http://reacts.org) projects, I could decide to go the pure CSS route. It doesn’t hurt.

However, if you’re writing a large app with a ton of vanilla CSS flying around, I bet introducing a CSS preprocessor will make your development more interesting and contribute towards a more maintainable CSS codebase.

Again, I’m not saying use preprocessors every single time. I’m saying don’t just close out that option. It could save you!

#### You’ve got a lot of _Important_ Style there!

![Image](https://cdn-media-1.freecodecamp.org/images/N6QGbrfgLCAKgecAbfzrNyCfMxjXtcebzvHm)

I hate CSS. It just never works. So, what’s the fix?

Have a ton of `!important` all over the place when I need to override any declarations. Haha!

While this sounds like a decent plan to your lazy self, over-using the `!important` rule will only result in a grossly unmaintainable CSS document.

The next time you need to use `!important`, [be sure](https://css-tricks.com/when-using-important-is-the-right-choice/) you’re not doing so because you’re too lazy to fix your cascade issues.

[CSS isn’t that bad. Embrace it.](https://medium.freecodecamp.org/the-most-important-css-concept-to-learn-8e929c944a19)

#### Want to write Better CSS?

I have created a free CSS guide to get your CSS skills blazing, immediately. [Get the free ebook](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/qdjk1yXX4UbyuwxJGbKmQchX4aYmmJAN1VZ2)
_Seven CSS Secrets you didn’t know about_

