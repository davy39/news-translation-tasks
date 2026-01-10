---
title: CSS Pseudo-Elements - Before and After Selectors Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-pseudo-elements-before-and-after-selectors-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cfa740569d1a4ca3537.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: "Before Selector\nThe CSS ::before selector can be used to insert content\
  \ before the content of the selected element or elements. It is used by attaching\
  \ ::before to the element it is to be used on.\nLet’s look at some examples:\np::before\
  \ { \n  content: ..."
---

## **Before Selector**

The CSS `::before` selector can be used to insert content before the content of the selected element or elements. It is used by attaching `::before` to the element it is to be used on.

Let’s look at some examples:

```css
p::before { 
  content: "* ";
}

span.comment::before {
  content: "Comment: ";
  color: blue;
}
```

```html
<p> To infinity, and beyond!</p>
<p> I am Buzz Lightyear. I come in peace.</p>

<span class="comment">May the force be with you.</span>
<br/>
<span> Do. Or do not. There is no try.</span>
```

In the example above we are prepending an asterisk and a space before every paragraph element on the page. Also, we're prepending "Comment: " in blue before every `span` element with the class `comment`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-186.png)

## After Selector

The CSS `::after` selector can be used to insert content after the content of the selected element or elements. It's used by attaching `::after` to the element it is to be used on.

Here are some examples:

```css
.buzz::after { 
  content: " - Buzz Lightyear";
  color: blue;
}

.yoda::after { 
  content: " - Yoda";
  color: green;
}
```

```html
<p class="buzz"> To infinity, and beyond!</p>
<p class="yoda"> Do. Or do not. There is no try.</p>
```

In the example above, we're appending " - Buzz Lightyear" in blue to the element with the class `buzz`. Also, we're appending " - Yoda" in green to the element with the class `yoda`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-185.png)

## Single-colon vs. Double-colon

There’s a bit of discussion about the right way of using pseudo-elements – the old style single-colon (`:before`), used in CSS specifications 1 and 2, versus the CSS3 recommendation, double-colon (`::before`), mainly to _“establish a discrimination between pseudo-classes and pseudo-elements”_. 

But for compatibility reasons, the single-colon method is still accepted. Keep in mind that IE8 supports the single-colon notation only.

## More Information:

* [The CSS Handbook: a handy guide to CSS for developers](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/)
* [The Best CSS Examples and CSS3 Examples](https://www.freecodecamp.org/news/css-example-css3/#background-color-example)

