---
title: How to use jQuery Selectors and CSS Selectors, and the basics of how they work
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-04T13:15:30.000Z'
originalURL: https://freecodecamp.org/news/back-to-basics-demystifying-css-and-jquery-selectors-12d75946b8b7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fvb-U3xoZbIr_AEmPHOQjw.jpeg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Rasheed Bustamam

  The other day, I was interviewing someone who had finished the front-end certification
  of freeCodeCamp. He had also graduated from a rather prestigious bootcamp, where
  attendees coded from 8am to 8pm for six weeks straight. Yikes!...'
---

By Rasheed Bustamam

The other day, I was interviewing someone who had finished the front-end certification of freeCodeCamp. He had also graduated from a rather prestigious bootcamp, where attendees coded from 8am to 8pm for six weeks straight. Yikes!

His programming ability was great, but I was surprised to see that his knowledge in CSS was lacking. And by lacking, I mean he didn’t know how to select a class to apply a style. This doesn’t necessarily reflect negatively on him. If anything, it highlights how a lot of programmers view CSS.

Many people think learning CSS is unimportant, since designers will usually be able to implement the CSS for you. While this is true, there are many times that you (as the programmer) will need to know some basic CSS in order to select an element and tell it to do something when something else happens.

For example, [Green Sock Animation Platform (GSAP)](https://greensock.com/) is probably too program-y to be designer-centric. It requires a developer with a knowledge of CSS as well as programming.

I’m not saying that every developer needs to be a CSS master. But I think if you’re going to call yourself a full-stack developer, you should know the basics of CSS. And the basics start with the **selector**.

Disclaimer: jQuery selectors aren’t actually unique to jQuery — they’re actually CSS selectors. However, if you’re anything like me, you learned jQuery before you properly learned CSS, and therefore automatically associated selectors with jQuery. Though this article is about CSS selectors, it will help you if you need some clarifications on jQuery selectors as well.

### The CSS Selector

I always find it helpful to play with code, so here’s a simple CodePen for playing with basic selectors.

In HTML, there are three ways to label or categorize elements. The first way is the broadest: by tag name. For example, you can select **all** `div`s on your page by using the simple selector `div`. Hey, that was easy!

The second way is probably the one you’ll use the most: the `class` attribute. You can select by class by using a dot (`.`) , so in the example above, to select the **all** elements with class `section` I use `.section` as a selector.

The third way is often overused, but still useful, and that’s the `id` attribute. IDs should identify your elements, just as your SSN (in the US) might identify you as a person. That means that IDs should be unique across the entire page. To select an element with a specific ID, you use the hashtag (`#`), or [octothorpe](https://en.wiktionary.org/wiki/octothorpe) as I like to call it. To select the element with the ID of `other` I use `#other`.

These are the most basic selectors. To recap:

* select by tag name (no prefix)
* select by class name (prefix of `.`)
* select by ID (prefix of `#`)

These three selectors alone will allow you to select almost anything on your webpage.

### Quiz 1

1. How would you select all the paragraph tags on the page? (hint: paragraph tags are `p`)
2. How would you select all items with class of `button-text`?
3. How would you select the element with ID of `form-userinput`?

Feel free to share your answers in the comments!

### Do all IDs need to be unique?

This is a small digression that I feel is very important. But if you’re only here to learn how to use selectors, feel free to skip to the next section

With a name like ID, you’d assume that every HTML ID **must** be unique or your HTML document will not work. After all, trying to have two `const` variables will make many editors yell at you, so wouldn’t HTML yell too?

The problem is, HTML will **not** yell at you. In fact, no one will even tell you anything is wrong. You may find a bug that stems from a non-unique ID. But you will drive yourself crazy trying to figure out the root cause of the bug, because it is a very subtle failure.

The example above demonstrates why having duplicate IDs might cause an issue on your webpage. First, there are actually two `div`s with the ID `other`. If you comment the styles for `#other`, you’ll see that **both** items actually get styled. This might make you think, “well hey, I can use IDs and classnames interchangeably!”

Not so fast. If you look in the JavaScript panel, you’ll see that I selected particular items based on their element label: tag name, class name, or ID. You’ll notice that `document.getElementsByTagName` and `document.getElementsByClassName` return a collection of all matching HTML elements. `document.getElementById` returns only the first HTML element it can find with the matching ID. You can verify this by uncommenting the `getVanillaSelectors` function and checking the console.

![Image](https://cdn-media-1.freecodecamp.org/images/-OPGCXaiU08Jk822L-vhfNCJvRgMkrbYwwGI)
_Using document.getElement(s)By[Type]_

To further complicate things, if you use JavaScript’s `querySelectorAll` method (which takes in a CSS selector as input), you get a totally different result.

![Image](https://cdn-media-1.freecodecamp.org/images/QAIsIoGAXcjxUU3103l-WiGng4GhA2WpZgfp)
_Using document.querySelectorAll_

And just to mess with you, jQuery does something different despite having a similar syntax to `querySelectorAll`.

![Image](https://cdn-media-1.freecodecamp.org/images/7ZCdtrLSCPzJJlXgYD9ltvbmq9Nkffj49vkr)
_Using jQuery selector_

I have no explanation for the different behavior. However, I can tell you how to avoid it. Here are my rules:

1. Never use IDs. Use `class` attributes instead.
2. If I need to use an ID, name-space it such that it will be unique even if a similar item exists on the page; for example `menu-item-01`

Sometimes forms, and their input fields, may need to have IDs. In that case, you can follow rule number 2. Here’s how I would namespace a form for user-signup:

```
<form id="user-signup">  <input id="user-signup-userid" label="user id" />  <input id="user-signup-password" label="password" /></form>
```

That way, if I have two forms on the same page (let’s say `user-signup` and `user-signin`), they are guaranteed to have unique IDs. Even if the userID fields are similar between the forms.

### Combining Selectors

Sometimes a single selector just won’t cut it. Sometimes, you need to get every `div` that has a class name of `section` . Other times, you need every element with a class name of `section` that is a child element to a `div` with ID `user-signup` . There are many possible other selector combinations.

In this section, you will learn three ways of **combining** selectors, and I am confident that these will suit 90% of your needs. If you find that more than 11% of your needs are unfulfilled, come complain to me and I’ll edit that to say 89% of your needs :).

As before, let’s start with a CodePen:

#### Combining selectors for a single element

OK, first let’s cover combining selectors for a single element. This means selecting the element that has tag name of `x`, AND class name of `y`, AND ID of `z`. Of course, you don’t need all three, but you can combine all three.

Let’s say we want to select all `div`s with class of `item`. To do that, we combine the two: `div.item`. It goes from most general to most specific from left to right. That selects all `div` tags that ALSO have the class name of `item`. It’s important to note that there is **no** space between `div` and `.item`. Adding a space changes the selector **completely**, as I will go over in the next section.

If you uncomment the corresponding CSS, you’ll see that the `section` with the class name of `item` did not turn red. That’s because it’s not a `div` tag.

You can do this same pattern with class names and IDs. But if you have an element’s ID, you may as well just use the ID. There’s no reason to select an ID with a specific class name, because if you followed the ID rules above, you only have one item with that ID anyway.

But, just for parity, here’s an example of selecting the `div` with class of `item` and ID of `other`: `div.item#other`. Again, going from left to right, it goes most general to more specific.

Most likely you’ll use this syntax to select an element that has multiple classes. To do this, just separate all the classes with periods. To select all elements that have BOTH classes `item` and `section`, you’d use `.item.section`. The order doesn’t matter when you’re doing it this way, so `.section.item` will work too.

This one trick will allow you to be more specific in your selectors.

#### The “child” selector

The second way you can combine selectors is by using the “child” selector, as I like to call it. There’s two ways of doing this, so I’ll start with the most general.

First, you can select **any** child of a certain element by adding a space. For example, to select all child `item`s of the `#other` element, it’d be `#other .item`. Notice the space between the selectors.

Second, you can select **immediate** children of a certain element by using the `&`gt;. An “immediate child” of an element is one that is only one level deep. In the example, there are t`wo .i`tem elements contained in t`he #ot`her element, but one of t`he .i`tem elements is wrapped up in `a .wrap`per element, so that one **is** not an immediate child.

To give you a visual, if you collapse everything underneath the `#other` element, you’d see this:

![Image](https://cdn-media-1.freecodecamp.org/images/0RUimDp2bmfxmjcXSseuU3mKkJQcEF8WQxEm)
_Collapsed children_

Those two are the only **direct children** of the `#other` element. To select only the direct child `.item` of `#other`, you’d use `#other > .i`tem, which would select the direct child, b**ut** not the one undernea`th .wrap`per. Nifty, huh?

### Quiz 2

1. How would you select all the paragraph tags that belong to `section` elements? (hint: paragraph tags are `p`)
2. How would you select all items with class of `button-text`, that are descendants to items with class of `button`?
3. How would you select the element with class of `form-input` that is a **direct child** of `form` elements?
4. **Bonus question**: explain what this selector selects: `header.title > form.user-signup button.button-dan`ger

As before, feel free to share your answers in the comments!

#### Putting it all together — literally

You can combine combined selectors. Really. The bonus question above shows an example of it, but I’ve added some combinations at the end of the example codepen.

For example, you can choose all `.item`s that are children of `div`s with class of `parent-item` by using `div.parent-item .item`. Whoa!

You can choose direct descendants as well. For example, to select all `div`s with class of `item` that are direct descendants to `div`s with class of `parent-item`: `div.parent-item > div.i`tem.

And finally, just to mess with you, you can walk down the entire DOM tree: `div.parent-item .coolest-item .item`. `item` class that is child to `coolest-item` class that is child to `div` with class of `parent-item`.

Note that it’s generally **not** a good idea to go beyond two or three levels of depth when nesting selectors. Then you get into weird realms of specificity that you can solve more effectively by naming your CSS classes better. But that’s out of the scope of this article. If you want to know more, let me know and I’ll write about it.

### Bonus: Using Chrome DevTools to get a selector

You can use Chrome DevTools to get the selector of any element you can select on the DOM. Here’s how:

1. Open Chrome DevTools. Since you’re selecting an element, go ahead and right click the element you want to select and click on “Inspect”:

![Image](https://cdn-media-1.freecodecamp.org/images/GtfJwCPIBiQk6MwKL2Gh0SXrQP3-9U7gFRvZ)
_Yep, it’s a picture of me writing this article_

2. Right click the DOM element you want to select and hover over “Copy,” then click on “Copy Selector:”

![Image](https://cdn-media-1.freecodecamp.org/images/uA07RG3g28FPzm2R5kxisTCOoyNdebyozg76)
_I like the Dark Theme._

3. That’s it! The selector I copied, by the way, is `#editor_93 > section > div.section-content > div:nth-child(3) > p.graf.graf — p.graf-after — figure.graf — trailing`.is-selected. You can copy the se`lector into document.q`uerySelector or jQuery and get the element.

![Image](https://cdn-media-1.freecodecamp.org/images/PRajyQG7HxHQEEqeg83AGYzMOOCiF9VP8K7L)
_This is the selector for the image above._

Hopefully this writeup was helpful! If you enjoyed it, please give me some claps so more people see it. Thanks!

