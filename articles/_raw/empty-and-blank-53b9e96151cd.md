---
title: When to use the :empty and :blank CSS pseudo selectors
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-09-18T22:12:41.000Z'
originalURL: https://freecodecamp.org/news/empty-and-blank-53b9e96151cd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca9e4740569d1a4ca8771.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'I made a terrible mistake when I tweeted about :empty and :blank a while
  ago. I said that :empty wasn’t useful, and :blank is much more useful than :empty.


  I was wrong!

  :empty is actually good enough. We don’t even need :blank!

  A quick introduction

  ...'
---

I made a terrible mistake when I tweeted about `:empty` and `:blank` a while ago. I said that `:empty` wasn’t useful, and `:blank` is much more useful than `:empty`.

![Image](https://cdn-media-1.freecodecamp.org/images/vsw0KkV-ZfP8LtM29iCh0QOcEBaiV9Xy-F9C)

I was wrong!

`:empty` is actually good enough. We don’t even need `:blank`!

#### A quick introduction

Okay, first off, what is `:empty` and what is `:blank`?

`:empty` is a pseudo selector. It lets you select elements that are empty.

```
/* This is CSS */
```

```
:empty { /* do something */}
```

Empty elements are elements that have nothing in them. It cannot even have a whitespace.

```
<!-- This is html -->
```

```
<!-- Example of an empty element --><div></div>
```

Empty elements can have comments though, as long as the comments fill up the entire element.

```
<!-- This is html -->
```

```
<!-- Empty elements can have comments --><div><!-- this is a comment --></div>
```

`:blank` is a powered-up form of `:empty`. It lets you select elements that have whitespaces in them:

```
<!-- This is html -->
```

```
<!-- Matched with :blank but not with :empty --><div> </div>
```

Both `:empty` and `:blank` are useful if need to:

1. Style an empty element
2. Create empty states

#### An example

Let’s say you have a `<d`iv>. You will only fill up `this` <div> with content when an error occurs.

```
<!-- This is html -->
```

```
<!-- Without errors --><div class="error"></div>
```

```
<!-- With errors --><div class="error">Whoops! Something went wrong!</div>
```

Here, you need to style the `.error` div. If you don’t use `:empty`, you need to rely on a class or attribute. This feels redundant.

```
<!-- This is html -->
```

```
<!-- With errors --><div class="error" data-state="error">Whoops! Something went wrong!</div>
```

```
/* This is CSS */
```

```
.error { display: none; background-color: hsl(0, 20%, 50%); padding: 0.5em 0.75em;}
```

```
.error[data-state="error"] { display: block;}
```

But if you use `:empty`, you don’t need the extra class or attribute. You can style the .error class directly. You don’t even need `display: none;`!

```
/* This is CSS */
```

```
.error { background-color: hsl(0, 20%, 50%); padding: 0.5em 0.75em;}
```

```
.error:empty { padding: 0;}
```

Here’s a codepen [Empty Demo](https://codepen.io/zellwk/pen/JaPgdN/) I made for you to play with (try removing the `padding: 0;` from `.error:empty`, you’ll see a red background ?).

Let’s say you want to create a todo-list. When your users see the todo-list for the first time, they will probably see zero todo items.

What do you show when there are zero todos?

This zero todo state is what we call an empty state.

If you want to create an empty state for your todo-list, you can add an extra `<d`iv> after `you`r <ul>. When you do so, you can use a com`binati`on of :em`p`ty and the + (adjacent `s`ibling) or ~ (subsequent sibling) selector to style the empty state.

```
<!-- This is html -->
```

```
<ul> <li>Item 1</li> <li>Item 2</li> <li>Item 3</li></ul><div class="empty-state"></div>
```

```
/* This is CSS */
```

```
.empty-state { display: none;}
```

```
ul:empty + .empty-state { display: block;}
```

I learned how to use `:empty` this way from Heydon Pickering. Check out [Heydon’s article](https://inclusive-components.design/a-todo-list/) on [Inclusive Components](https://inclusive-components.design/) if you want to see the todo-list example at work.

> Note: empty states are important. If you need some convincing, check out [this article](https://www.invisionapp.com/blog/why-empty-states-deserve-more-design-time/) on Invision.

#### Taking apart my reasoning

`:empty` is often enough in practice. I felt `:empty` isn’t good enough because of two reasons:

1. Poor developer experience
2. I’ll need to trim whitespaces manually with JavaScript

The first reason is valid, but it isn’t a big deal.

**The second reason is not valid**. I assumed I had to trim whitespaces, but I don’t need to.

I’ll walk you through both of them.

Let’s go back to the todo-list example. Say we created a todo-list and we have this markup.

```
<!-- This is html -->
```

```
<ul> <li>Item 1</li> <li>Item 2</li> <li>Item 3</li></ul><div class="empty-state"></div>
```

How would you check if `:empty` was working?

Well, I would remove each `<`li> `wi`th `c`md + x. This command cuts the entire line. When I removed all `thre`e <li>, I’ll end up with this markup:

```
<!-- This is html -->
```

```
<ul></ul>
```

By now, you’ll know that the HTML above won’t trigger `:empty`. `:empty` only works when there are no whitespaces in the element.

I had to remove the whitespaces for `:empty` to work, which means a few more keystrokes. This was a chore I hoped I didn’t have to go through.

But then again, it’s a small problem for a big benefit.

I say it again. **You don’t need to trim whitespaces manually in JavaScript** if you use `:empty`. I made a wrong assumption.

Let’s go through an example and you’ll see what I mean. We’ll use the todo-list example one more time.

Say we have this HTML right now:

```
<!-- This is html -->
```

```
<ul> <li>Item 1</li></ul><div class="empty-state"></div>
```

For the empty state to work, we need to remove the final `<`li> item `fro`m <ul>. If you use plain JavaScript, you can d`o this with` removeChild.

```
// This is JavaScript
```

```
const ul = document.querySelector('ul')const li = ul.children[0]
```

```
ul.removeChild(li)
```

I believed (erroneously) that `removeChild` will produce this HTML:

```
<!-- This is html -->
```

```
<ul></ul>
```

If it produces this HTML, I’ll have to trim any whitespace remaining in the list (which is extra JavaScript).

```
// This is JavaScript
```

```
const ul = document.querySelector('ul')const li = ul.children[0]
```

```
ul.removeChild(li)
```

```
if (ul.children.length === 0) { ul.innerHTML = ''}
```

Like I said, I was wrong. It didn’t produce the above HTML. Instead, this is what it produced:

```
<!-- This is html -->
```

```
<ul></ul>
```

Which means we didn’t need the extra JavaScript to trim whitespace!

> Disclaimer: I checked the output on Safari, Chrome, and Firefox. I haven’t checked Edge yet though. I’ll be super grateful if you can help me test it out!

Here’s the code for this example:

See the Pen [Empty demo with todolist](https://codepen.io/zellwk/pen/ZMzgJp/) I made ([@zellwk](https://codepen.io/zellwk)) on [CodePen](https://codepen.io/).

`:empty` is supported on all browsers, and `:blank` has poor browser support. This gives you plenty of reason to use `:empty` over `:blank` today!

![Image](https://cdn-media-1.freecodecamp.org/images/0uAx8kJC7pr98VvkEYqphhJ3BD00BfPuNuJ2)

I hope that browser support for `:blank` improves one day though.

#### Wrapping up

`:empty` and `:blank` let you style empty elements and produce empty states easily.

`:blank` is better than `:empty` because it provides us with a better developer experience. But we can’t use `:blank` because `:blank` doesn’t have enough browser support.

`:empty` is often good enough. You can use it already. Use it all you want! ?

Give `:empty` a go and let me know what you think!

Thanks for reading. Did this article help you in any way? If you did, [I hope you consider sharing it](http://twitter.com/share?text=%3Aempty%20and%20%3Ablank%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/empty-and-blank/&hashtags=). You might help someone out. Thank you!

This article was originally posted at [_my blog_.](https://zellwk.com/blog/empty-and-blank)

Sign up for my [newsletter](https://zellwk.com/) if you want more articles to help you become a better frontend developer.

