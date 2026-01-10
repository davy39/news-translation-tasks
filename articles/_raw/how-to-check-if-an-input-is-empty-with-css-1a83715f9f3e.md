---
title: How to check if an input is empty with CSS
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-12-28T23:32:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-an-input-is-empty-with-css-1a83715f9f3e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*1N9VIZ7wJ7Kq_iqQ.gif
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Is it possible to know if an input is empty with only CSS?

  I had that question when I tried to make an autocomplete component for Learn JavaScript.
  Basically, I wanted to:


  Hide a drop-down if the input is empty

  Show the drop-down if the input is fil...'
---

Is it possible to know if an input is empty with only CSS?

I had that question when I tried to make an autocomplete component for Learn JavaScript. Basically, I wanted to:

1. Hide a drop-down if the input is empty
2. Show the drop-down if the input is filled

![Image](https://cdn-media-1.freecodecamp.org/images/yyt7BfywizCAjffJaHpmuVSIGNarprZTgj87)

I found a way to do it. It’s not perfect. There are a few nuances involved, but I want to share it with you.

### The form

First, let’s build a form so we’re on the same page. We’re going to use a simple form with one input.

```
<form>  <label for="input"> Input </label>  <input type="text" id="input" /></form>
```

When the input is filled, we want to change its `border-color` to green. Here’s an example of what we’re creating:

![Image](https://cdn-media-1.freecodecamp.org/images/3Ta3zBaP2zckvzN9II60OJhn1EXzzNRfcwnd)

### Checking if the input is empty

I relied on HTML form validation to check whether the input was empty. That meant I needed a `required` attribute.

```
<form>  <label> Input </label>  <input type="text" name="input" id="input" required /></form>
```

At this point, it worked fine when the input was filled. Borders turned green.

![Image](https://cdn-media-1.freecodecamp.org/images/Fr40-RMCPUjeTD6Y3GJ3MK4VJUf-jqCHSw9e)

But there was a problem: if the user enters a whitespace into the field, the borders turn green too.

![Image](https://cdn-media-1.freecodecamp.org/images/y-kZqMJhxDWcisrzGnyqwMQNJ2BtCUVu1hB5)

Technically, this is correct. The input is filled because the user typed something into it.

But I didn’t want whitespaces to trigger a blank dropdown menu (for the autocomplete component).

It wasn’t enough. I needed a more stringent check.

### Further checks

HTML gives you the ability to validate inputs with regular expressions with the `pattern` attribute. I decided to test it out.

Since I didn’t want whitespaces to be recognized, I started with the `\S+` pattern. This pattern meant: One or more characters that’s not a whitespace.

```
<form>  <label> Input </label>  <input type="text" name="input" id="input" required pattern="\S+"/></form>
```

Sure enough, it worked. If a user enters a whitespace into the field, the input doesn’t get validated.

![Image](https://cdn-media-1.freecodecamp.org/images/jWR2WuP91tUOox5ZmYcKvq6sYRFFGmh09C4g)

But when a whitespace is entered (anywhere) into the input, the input gets invalidated.

![Image](https://cdn-media-1.freecodecamp.org/images/JVKUWbAqxbWQZ2sDtV9XjMYKfEAmaaE46Sg7)

Unfortunately, this pattern didn’t work in my use case.

In Learn JavaScript’s autocomplete component, I taught students how to complete a list of countries. The names of some countries had spaces…

![Image](https://cdn-media-1.freecodecamp.org/images/G0iQiqeU5xFkv7AlHXj30Z8Bn5JQ9Kj2MfxY)

I had to include whitespaces in the mix.

The next best alternative I could think of is `\S+.*`. This means 1 or more non-whitespace characters, followed by zero or more (any) characters.

```
<form>  <label> Input </label>  <input type="text" name="input" id="input" required pattern="\S+.*"/></form>
```

This worked! I can enter whitespaces into the mix now!

![Image](https://cdn-media-1.freecodecamp.org/images/x2YDLSVq2CmaVUd1nlQCqo0IKCrwBOQqymwx)

But there’s one more problem… the input doesn’t validate if you START with a whitespace…

![Image](https://cdn-media-1.freecodecamp.org/images/CT8NoxhJxCE8LM-5j9y6lMNstA3K0z37Okw8)

And that’s the problem I couldn’t resolve. More on this later.

When I worked on this article, I came across another interesting question: Is it possible to style an invalid state when the input is filled incorrectly?

### Invalidating the input

We don’t want to use `:invalid` because we’ll kickstart the input with an invalid state. (When the input is empty, it’s already invalid).

This is where Chris Coyier swooped in to the rescue with “ [Form Validation UX in HTML and CSS](https://css-tricks.com/form-validation-ux-html-css/)”.

In the article, Chris talks about a `:placeholder-shown` pseudo-class. It can be used to check whether a placeholder is shown.

The idea is:

1. You add a placeholder to your input
2. If the input is hidden, it means the user typed something into the field
3. Proceed with validation (or invalidation)

Here’s the CSS (simplified version. For the complete version, check out [Chris’s article](https://css-tricks.com/form-validation-ux-html-css/).)

```
/* Show red borders when filled, but invalid */input:not(:placeholder-shown) {  border-color: hsl(0, 76%, 50%);}
```

Since I had both validation AND invalidation styles, I had to ensure the valid styles came after the invalid styles.

```
/* Show red borders when filled, but invalid */input:not(:placeholder-shown) {  border-color: hsl(0, 76%, 50%);;}
```

```
/* Show green borders when valid */input:valid {  border-color: hsl(120, 76%, 50%);}
```

Here’s a demo for you to play with:

See the Pen [Pure CSS Empty validation](https://codepen.io/zellwk/pen/dgEKxX/) by Zell Liew ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

Note: Edge doesn’t support `:placeholder-shown`, so it’s probably not a good idea to use it in production yet. There’s no good way to detect this feature.

Now back to the problem I couldn’t resolve.

### The problem with pattern

The `pattern` attribute is wonderful because it lets you accept a regular expression. This regular expression lets you validate the input with anything you can think of.

But… **the regular expression must match the text completely**. If the text doesn’t get matched completely, the input gets invalidated.

This created the problem I mentioned above. (Reminder of the problem: If a user enters a whitespace first, the input becomes invalid).

I couldn’t find a regular expression that worked for all use-cases that I thought of. If you want to try your hand at creating a regular expression that I need, I’d be more than happy to receive the help!

Here are the use-cases:

```
// Should not match''' ''  ''   '
```

```
// Should match'one-word''one-word '' one-word'' one-word ''one phrase with whitespace''one phrase with whitespace '' one phrase with whitespace'' one phrase with whitespace '
```

(Then again, I might be overthinking it… ?).

### Update: Problem solved!

Many readers were generous enough to email me their solutions. I want to thank everyone who helped. Thank you so much!

The cleanest solution I received is: `.*\S.*` by [Daniel O’Connor](https://www.nvinteractive.com/). This means:

* `.*`: Any character
* `\S`: Followed _one_ non-whitespace character
* `.*`: Followed by any character

Other regexes I received include:

* `.*\S+.*`by [Matt Mink](https://twitter.com/matthewjmink)
* `\s*\S.*` by [Sungbin Jo](https://github.com/pcr910303)
* `^\s?(?=\S).` with a lookahead by [Konstantin](https://twitter.com/KonstantinRouda)

And many others!

Here’s a [codepen](https://codepen.io/zellwk/pen/NeRaPw/) with the updated solution by Daniel.

### Wrapping up

Yes, it is possible to validate a form with pure CSS. There are potential problems with validation when whitespace characters are involved.

If you don’t mind the whitespaces, it works perfectly. Have fun trying this pattern out! (Sorry, I can’t help it).

Thanks for reading. Did this article help you out? If it did, I hope you consider [sharing it](https://twitter.com/share?text=Checking%20if%20an%20input%20is%20empty%20with%20CSS%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/check-empty-input-css/). You might help someone else out. Thanks so much!

This article was originally posted at [my blog](https://zellwk.com/blog/check-empty-input-css). Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better front-end developer.

