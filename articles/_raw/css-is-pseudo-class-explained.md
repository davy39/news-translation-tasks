---
title: CSS Pseudo-Classes – How the :is Pseudo-Class Works with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-02T22:04:37.000Z'
originalURL: https://freecodecamp.org/news/css-is-pseudo-class-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/1.-is.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dillion Megida

  Pseudo-classes allow you to style an element in a specific state. There are many
  supported classes for states in CSS. In this article, I''ll explain how the :is
  pseudo-class works.

  This article is the first in a new series I''ll be wo...'
---

By Dillion Megida

Pseudo-classes allow you to style an element in a specific state. There are many supported classes for states in CSS. In this article, I'll explain how the `:is` pseudo-class works.

This article is the first in a new series I'll be working on over the coming weeks and months: **CSS Pseudo Classes Explained**. I intend to explain as many pseudo-classes as I can, with each standalone article tackling a particular pseudo-class.

I have [a CSS Pseudo Classes Explained YouTube playlist](https://www.youtube.com/playlist?list=PLLdz3KlabJv2sYL287Q_8lpy_jOgwQjN2) that you can check out, too.

Note: Pseudo-classes are different from pseudo-elements. Pseudo-classes apply to different **states** of elements, while Pseudo elements apply to different **parts** of an element. 

You can learn more [about the differences here](https://dillionmegida.com/p/pseudo-elements-vs-pseudo-classes-in-css/).

In this tutorial, you'll learn all the basics of the `:is` pseudo-class.

## How the `:is` pseudo-class works

The `:is` pseudo-class takes a list of selector arguments and matches all elements that apply to any selector in the list. Here's the syntax:

```css
:is(selector1, selector2, selector3) {
  /* styles */
}
```

You specify selectors of any type, and any element in the DOM that "is" a match for any of the selectors will be selected and styled.

I have an article on [Selector Types in CSS](https://www.freecodecamp.org/news/how-to-select-elements-to-style-in-css/) which you can check out to see the different selectors you can use with the `:is` pseudo class. 

The only selector type you cannot use with the class is a **pseudo-element**.

Also, because I like having video versions of my articles (for those who may prefer/enjoy watching videos), you can check out the [video version of the :is pseudo-class on YouTube](https://youtu.be/sDa4zDHv41Y).

Let's see some examples of this pseudo-class.

### Examples of `:is` pseudo-class

Look at this CSS code:

```css
:is(.selector1, #selector2, selector3, :selector4, [selector5]) {
  /* styles */
}
```

As the argument list, we have the **selector1** `class`, **selector2** `id`, **selector3** `tag`, **selector4** `pseudo-class` and **selector5** `attribute` selectors. All elements in the DOM that match at least one of these selectors will be selected for styling.

Let's see a practical example.


```html
<section>
  <p>Paragraph of section</p>
</section>

<div>
  <p>Paragraph of div</p>
</div>

<article>
  <p>Paragraph of article</p>
</article>

<span>
  <p>Paragraph of span</p>
</span>
```

Here, we have a `section`, `div`, `article`, and a `span` element. Each of these elements has a `p` child. If we wanted to style all the `p` children of these elements, we can have the following style declaration:

```css
section p,
div p,
article p,
span p {
  text-decoration: underline;
  color: red;
}
```

Result:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-107.png)

But we can improve the CSS with the `:is` pseudo-class. Here's how:

```css
:is(section, div, article, span) p {
  text-decoration: underline;
  color: red;
}
```

This gives us the same result as above. But what's different?

In the `:is` pseudo-class, we pass four selectors: the tag names `selection`, `div`, `article`, and `span`. Using the [descendant combinator](https://www.freecodecamp.org/news/css-combinators-to-select-elements#1howtousethedescendantcombinator) (a space character), we select `p` tag elements that are descendants of any of the selectors in the list. Which means, this selection will select:

* `p` descendants of `section`
* `p` descendants of `div`
* `p` descendants of `article` and
* `p` descendants of `span`

Using the `:is` pseudo-class, we have shortened the element selectors.

Let's see another example.

```html
<button class="active">Click Me</button>
```

For this button, let's say you want to apply the same style when it is in a `hover` or `focus` state, or when it has an `active` class. Normally, you can have the following code:

```css
button:hover,
button:focus,
button.active {
  background-color: black;
  color: white;
}
```

The result:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-291.png)

You can also improve this with the `:is` pseudo-class:

```css
button:is(:hover, :focus, .active) {
  background-color: black;
  color: white;
}
```

Here, you see that we add the `:is` pseudo-class to the `button`, and for the selectors, we have:
* `:hover` pseudo-class
* `:focus` pseudo-class and
* `.active` class

This would match the button accordingly.

## `:is` doesn't support pseudo-elements

As I mentioned earlier, you can pass selectors of different types as arguments to the `:is` pseudo class with the exception of pseudo-elements.

For example:

```css
:is(::after, ::selection) {
  /* styles */
}
```

Here, we pass the `::after` and [`::selection`](https://dillionmegida.com/p/css-selection-pseudo-element/) pseudo-elements as arguments for the `:is` pseudo class. Such a style declaration will not work.

## What's a Forgiving Selector List?

When you combine multiple selectors together in CSS and one of these selectors is not supported (or is invalid), your style declaration will be ignored. Here's what I mean:

```css
.button, #box, invalid {
  /* styles */
}
```

For our style above, we have the **.button** `class`, **#box** `id`, and **invalid** `tag` selectors. The first and second selectors are valid, but there's no tag name like **invalid**. Because the third one is not supported, the whole style will be ignored. 

But the `:is` pseudo-class allows the concept of a **forgiving selector list**. This means, if one of the selectors you pass as an argument is not supported, you will be "forgiven". That is, the supported selectors will be applied and the target elements styled accordingly. For example:

```css
button:is(:hover, :focuss, .active) {
  background-color: black;
  color: white;
}
```

Here, we pass the **:hover** `pseudo-class`, **:focuss** `pseudo-class`, and **.active** `class` for our styles. The **:focuss** pseudo-class is not supported, but instead of the whole style declaration being ignored, the **:hover** and **.active** selectors will still be applied.

## Wrapping up

You can do a lot of advanced selections with the `:is` pseudo-class. This class allows you to write long selectors in a shorter and easier-to-read manner.

In this article, we've learned about the `:is` pseudo-class. Through examples, we saw how it works and how it makes writing CSS code better.

Keep in mind that this pseudo-class works similarly to the `:where` pseudo-class, with one major difference. I'll explain that in a future article on the difference between the `:is` and `:where` pseudo-classes.

If you enjoyed it, kindly share 😇

