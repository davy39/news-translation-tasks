---
title: How to Use CSS Combinators to Select and Style Elements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-21T23:17:05.000Z'
originalURL: https://freecodecamp.org/news/css-combinators-to-select-elements
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/image--4-.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dillion Megida

  Combinators allow you to combine multiple selectors to target specific elements
  in the DOM. In this article, I''ll explain how four of these combinators with examples.

  In my previous post on CSS Selector Types, I shared seven types o...'
---

By Dillion Megida

Combinators allow you to combine multiple selectors to target specific elements in the DOM. In this article, I'll explain how four of these combinators with examples.

In my previous post on [CSS Selector Types](https://www.freecodecamp.org/news/how-to-select-elements-to-style-in-css/), I shared seven types of selectors for targetting elements that you want to style. 

If you haven't seen that post, I recommend reading through it before you go through this one.

In this tutorial, I talk about **Combinators** which allow you to use multiple selector types for selecting elements. This selection is based on the relationship between elements that match the multiple selector types specified.

There's a [video version](https://www.youtube.com/watch?v=ZKRRUUPl8SA) for this article if you'd prefer that.

Here are four combinators in CSS and how they work.


## 1. How to Use the Descendant Combinator

This combinator allows you to select an element that is a descendant of another element. "Descendants" here can be child, grandchild, great-grandchild, great-great-great...and so on.

To use this combinator, you enter an **empty space** between selectors like this:

```css
.container p {
  color: red;
}
```

This style declaration above selects `p` elements that are descendants of elements with the **div** class. 

Here's how it works with the following HTML:

```html
<p>I am the first p</p>

<div class='container'>
    <p>I am the second p</p>
    
    <div>
        <p>I am the third p</p>
    </div>
</div>

<p>I am the last p</p>
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-396.png)

From the result above, you can see the second and third `p` styled. This is because they are both descendants of the `.container` element. The second `p` is a direct child while the third `p` is grandchild (direct child of the `div`) but they are descendants.

You can also use the descendant combinator with multiple selectors like this:

```css
.container div p {
  color: red;
}
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-405.png)

As you can see, only the third `p` is styled because that is the element that is a descendant of a `div` element which in turn is a descendant of the **container** class element.

## 2. How to Use the Child Combinator

The descendant combinator matches a child, grandchild, and so on. The child combinator selects elements that are direct children of another element. 

You use the **greater than** symbol (**>**) between selectors to specify that one selector is a direct child of the other.

Here's an example:

```css
.container > p {
  color: red;
}
```

This styling will select all `p` elements that are direct children of the elements with the **container** class. Let's see how this works with the HTML example from above:

```html
<p>I am the first p</p>

<div class='container'>
    <p>I am the second p</p>
    
    <div>
        <p>I am the third p</p>
    </div>
</div>

<p>I am the last p</p>
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-397.png)

As you see here, only the second `p` is affected. Even though the second and third `p` elements are descendants of the **container** class element, only the second one is a direct child, as we have specified in the CSS.

You can also use multiple selectors with this combinator like this:

```css
.container > div > p {
  color: red;
}
```

This styling will match all `p` elements that are direct children of `div` elements which are in turn direct children of **container** class elements.

## 3. How to Use the Sibling Combinator

We've looked at descendants, now what about siblings – just like in a family setting? The sibling combinator used between selectors matches elements that are siblings of another element.

To use this combinator, you enter the **tilde** (**~**) symbol. Here is an example:

```css
div ~ p {
  color: red;
}
```

This styling selects all `p` elements that are siblings of `div` elements. Let's say we have the following HTML::

```html
<p>I am the first p</p>

<div class='container'>
    <p>I am the second p</p>
    
    <div>
        <p>I am the third p</p>
    </div>
</div>

<p>I am the last p</p>
<p>I am the very last p</p>
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-399.png)

The last two `p`s have the color styling. This happens because the `div` (that has the **container** class) has these `p`s as siblings.

However, if you notice, the first `p` is also a sibling of that `div`. So why isn't it styled?

The reason for this is that, in our CSS, we used the child combinator like this:

```css
div ~ p
```

This selection means that it is only going to select `p` siblings that are **AFTER** `div` elements. The siblings before do not get affected.

If the selection changes to:

```css
p ~ div
```

Then it is going to select `div` siblings that are **AFTER** `p` elements.

## 4. How to Use the Adjacent Combinator

This combinator is similar to the sibling combinator. The difference is that while the sibling combinator matches all siblings that come AFTER an element, the adjacent combinator matches only the **IMMEDIATE** sibling that comes after an element.

To use this combinator, you use the **plus** (**+**) symbol like this:

```css
div + p {
  color: red;
}
```

This styling affects `p` elements that are IMMEDIATE siblings after `div` elements. Let's say we have the previous HTML example:

```html
<p>I am the first p</p>

<div class='container'>
    <p>I am the second p</p>
    
    <div>
        <p>I am the third p</p>
    </div>
</div>

<p>I am the last p</p>
<p>I am the very last p</p>
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-400.png)

From this result, you can see that only the fourth `p` is styled. This is because this `p` element is an immediate sibling after the `div` element in our HTML code.

Even though the last `p` is also a sibling after the `div` element, it is not an adjacent element to the `div`.

## Wrapping up

As we've seen in this article, combinators allow you to use multiple selector types. Based on the relationship between the elements in the DOM that match these selectors, you can target elements to style.

The combinators we saw are:

* **Descendant Combinator**: for selecting elements that are descendants of other elements
* **Child Combinator**: for selecting elements that are direct children of other elements
* **Sibling Combinator**: for selecting elements that are siblings after other elements
* **Adjacent Combinator**: for selecting elements that are immediate siblings after other elements

If you enjoyed and learned from this article, please share it with others 💜.


