---
title: nth-child() vs nth-of-type() Selectors in CSS – What’s the Difference?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2024-01-31T18:33:32.000Z'
originalURL: https://freecodecamp.org/news/nth-child-vs-nth-of-type-selector-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/nth-child-vs-nth-of-type-css-selector-freecodecamp-featured-codesweetly.jpg
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'The :nth-child() and :nth-of-type() CSS selectors select items from a group
  of HTML elements. But they work in different ways.

  Here is the main distinction between them:


  nth-child() selects its items from any group of elements. nth-of-type() selects...'
---

The `:nth-child()` and `:nth-of-type()` CSS selectors select items from a group of HTML elements. But they work in different ways.

Here is the main distinction between them:

![nth-child vs nth-of-type selector in CSS](https://www.freecodecamp.org/news/content/images/2024/01/nth-child-vs-nth-of-type-selector-in-css-codesweetly.png)
_nth-child() selects its items from any group of elements. nth-of-type() selects its items from a specified type of element._

* `:nth-child()` selects items from a general group of elements. For instance, selecting a `<p>` node from a mixed group that includes `<h1>`, `<div>`, and `<section>`.
* `:nth-of-type()` selects items from a specified group of elements. For instance, selecting a `<p>` node from a group of `<p>` siblings.

This article uses examples to show you exactly how the two selectors work in CSS so that you can understand their similarities and differences.

## Table of Contents

1. [What is the CSS :nth-child() Selector?](#heading-what-is-the-css-nth-child-selector)
   - [Syntax of the CSS :nth-child() Selector](#heading-syntax-of-the-css-nth-child-selector)
   - [Examples of the CSS :nth-child() Selector](#heading-examples-of-the-css-nth-child-selector)
2. [What is the CSS :nth-of-type() Selector?](#heading-what-is-the-css-nth-of-type-selector)
   - [Syntax of the CSS :nth-of-type() Selector](#heading-syntax-of-the-css-nth-of-type-selector)
   - [Examples of the CSS :nth-of-type() Selector](#heading-examples-of-the-css-nth-of-type-selector)
3. [Overview](#heading-overview)

So, without any further ado, let’s get started with the `:nth-child()` selector.

## What is the CSS `:nth-child()` Selector?

The CSS `:nth-child()` selector selects one or more child [elements](https://codesweetly.com/web-tech-terms-h#html-element) among their direct siblings regardless of node types.

### Syntax of the CSS `:nth-child()` Selector

The CSS `:nth-child()` selector accepts one argument only. Here is the syntax:

```css
html-element:nth-child(value) {
  style declarations
}
```

The `value` argument can be one of the following:

1. A number: For example, using `3` represents the third child.
2. The keyword `even` or `odd`: We use it to represent even or odd children.
3. The formula `An+B`: We use it to express a series of numbers. For instance, `2n+3` expresses these numbers: `[(2x0)+3]`, `[(2x1)+3]`, `[(2x2)+3]`, `[(2x3)+3]`, and so on.

Note the following:

- `:nth-child()` is a CSS [pseudo-class](https://codesweetly.com/css-pseudo-selectors#what-is-a-css-pseudo-class-selector) selector.
- The `:nth-child()` selector works on direct siblings only.
- In the `An+B` formula,
  - `A` is an [integer](https://codesweetly.com/web-tech-terms-i#integer) value of your choice.
  - `n` is the multiplier that automatically increases from zero (`0`).
  - `+` (or `-`) is the addition (or subtraction) [operator](https://codesweetly.com/web-tech-terms-o#operator).
  - `B` is an optional offset value for increasing (or decreasing) the result derived after multiplying `A` and `n`.

### Examples of the CSS `:nth-child()` Selector

Below are examples of how to use the CSS `:nth-child()` pseudo-class selector.

#### Apply DeepPink to the `<p>` element that is the third child to its parent element

The `:nth-child()` selector below selects the `<p>` element that is the third child to its parent element.

```css
p:nth-child(3) {
  color: DeepPink;
}

```

If the snippet below is the HTML document for the above [CSS ruleset](https://codesweetly.com/css-ruleset), browsers will apply `DeepPink` to the second `<p>` element only.

```html
<h1>First heading 1 element</h1>
<p>First paragraph element</p>
<p>Second paragraph element</p>
<h2>First heading 2 element</h2>
<p>Third paragraph element</p>
<h3>First heading 3 element</h3>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-3c8dkj)

The `:nth-child()` selector works on direct siblings only. For instance, you can re-write the HTML snippet above to include nested elements as follows:

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p>Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's third paragraph element</p>
    <p>Article's fourth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's fifth paragraph element</p>
  <p>Article's sixth paragraph element</p>
</article>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-harjmu)

The `p:nth-child(3)` selector will apply `DeepPink` only to the fourth `<p>` node because it is the third child of its parent element.

#### Apply DeepPink to every odd child that is a `<p>` node

The `:nth-child()` selector below selects every odd child element that is a `<p>` node.

```css
p:nth-child(odd) {
  color: DeepPink;
}

```

**Note:** `1` is the [index](https://codesweetly.com/web-tech-terms-i#index) position of the first child element.

Assuming the snippet below is the HTML document for the above CSS ruleset, browsers will apply `DeepPink` to the fourth `<p>` element only.

```html
<h1>First heading 1 element</h1>
<p>First paragraph element</p>
<h2>First heading 2 element</h2>
<p>Second paragraph element</p>
<h3>First heading 3 element</h3>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-p2tsnq)

#### Apply `DeepPink` to every even child that is a `<p>` node

The `:nth-child()` selector below selects every even child element that is a `<p>` node.

```css
p:nth-child(even) {
  color: DeepPink;
}

```

**Note:** `1` is the index position of the first child element.

Assuming the snippet below is the HTML document for the above CSS ruleset, browsers will apply `DeepPink` to the first, second, fourth, and sixth `<p>` elements.

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p>Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <p>Article's third paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's fourth paragraph element</p>
    <p>Article's fifth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's sixth paragraph element</p>
  <p>Article's seventh paragraph element</p>
</article>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-c9bvm5)

#### Apply DeepPink to the third child element, seventh, eleventh, and so on that is a `<p>` node

The `:nth-child()` selector below selects every `<p>` child element whose index is a multiple of two (`2`) with an offset of three (`+3`).

**Note:** `1` is the index position of the first child element.

```css
p:nth-child(2n+3) {
  color: DeepPink;
}

```

**Fun Quiz:** If the snippet below is the HTML document for the above CSS ruleset, which of the elements will the browser style?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<div><p>Fifth paragraph element</p></div>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<div><p>Nineth paragraph element</p></div>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-ri4zjg)

#### Apply DeepPink to the first child, third, fifth, and so on that is a `<p>` node

The `:nth-child()` selector below selects every `<p>` child element whose index is a multiple of two (`2`) with an offset of negative three (`-3`).

**Note:** `1` is the index position of the first child element.

```css
p:nth-child(2n-3) {
  color: DeepPink;
}

```

**Fun Quiz:** If the snippet below is the HTML document for the above CSS ruleset, which of the elements will the browser style?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<div><p>Fifth paragraph element</p></div>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<div><p>Nineth paragraph element</p></div>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-jc7gyl)

#### Apply DeepPink to the `<p>` nodes that are one of the first three children of their parent

The `:nth-child()` selector below applies DeepPink to `<p>` nodes if they are one of their parent’s first three elements.

```css
p:nth-child(-n+3) {
  color: DeepPink;
}

```

**Fun Quiz:** If the snippet below is the HTML document for the above CSS ruleset, which of the elements will the browser style?

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p>Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <p>Article's third paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's fourth paragraph element</p>
    <p>Article's fifth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's sixth paragraph element</p>
  <p>Article's seventh paragraph element</p>
</article>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-child/js-rjuvvs)

Note that:

- `1` is the index position of the first child element.
- The `-n+3` syntax always selects the first three children because:
  - `-1 + 3 = 2`
  - `-2 + 3 = 1`
  - `-3 + 3 = 0`


So, now that we know how the CSS `:nth-child()` selector works, let’s discuss `:nth-of-type()` so we can see the difference.

## What is the CSS `:nth-of-type()` Selector?

The CSS `:nth-of-type()` selector selects one or more child [elements](https://codesweetly.com/web-tech-terms-h#html-element) among their direct siblings of the same node type.

### Syntax of the CSS `:nth-of-type()` Selector

The CSS `:nth-of-type()` accepts one argument only. Here is the syntax:

```css
html-element:nth-of-type(value) {
  style declarations
}

```

The `value` argument can be one of the following:

1. A number: For instance, using `3` represents the third element type.
2. The keyword `even` or `odd`: We use it to represent even or odd element types.
3. The formula `An+B`: We use it to express a series of numbers. For instance, `2n+3` expresses these numbers: `[(2x0)+3]`, `[(2x1)+3]`, `[(2x2)+3]`, `[(2x3)+3]`, and so on.

Note the following:

- `:nth-of-type()` is a CSS [pseudo-class](https://codesweetly.com/css-pseudo-selectors#what-is-a-css-pseudo-class-selector) selector.
- The `:nth-of-type()` selector works on direct siblings only.
- In the `An+B` formula,
  - `A` is an [integer](https://codesweetly.com/web-tech-terms-i#integer) value of your choice.
  - `n` is the multiplier that automatically increases from zero (`0`).
  - `+` (or `-`) is the addition (or subtraction) [operator](https://codesweetly.com/web-tech-terms-o#operator).
  - `B` is an optional offset value for increasing (or decreasing) the result derived after multiplying `A` and `n`.

### Examples of the CSS `:nth-of-type()` Selector

Below are examples of how to use the CSS `:nth-of-type()` pseudo-class selector.

#### Apply DeepPink to the third `<p>` element type

The `:nth-of-type()` selector below selects the third `<p>` element among its siblings of the same node type.

```css
p:nth-of-type(3) {
  color: DeepPink;
}

```

Assuming the snippet below is the HTML document for the above CSS ruleset, browsers will apply `DeepPink` to the third `<p>` element only.

```html
<h1>First heading 1 element</h1>
<p>First paragraph element</p>
<p>Second paragraph element</p>
<h2>First heading 2 element</h2>
<p>Third paragraph element</p>
<h3>First heading 3 element</h3>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-txtema)

The `:nth-of-type()` selector works on direct siblings only. For instance, you can re-write the HTML snippet above to include nested elements as follows:

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p> Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's third paragraph element</p>
    <p>Article's fourth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's fifth paragraph element</p>
  <p>Article's sixth paragraph element</p>
</article>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-hv18yl)

The `p:nth-of-type(3)` selector will apply `DeepPink` only to the fifth `<p>` node because it is the third `<p>` type of its parent element.

Therefore, if you add one more `<p>` node to the `<section>` element, the `p:nth-of-type(3)` selector will apply `DeepPink` to the fifth and sixth `<p>` items.

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p> Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's third paragraph element</p>
    <p>Article's fourth paragraph element</p>
    <p>Article's fifth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's sixth paragraph element</p>
  <p>Article's seventh paragraph element</p>
</article>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-ydvfhw)

#### Apply DeepPink to every odd `<p>` element type

The `:nth-of-type()` selector below selects every `<p>` child element with an odd [index](https://codesweetly.com/web-tech-terms-i#index).

```css
p:nth-of-type(odd) {
  color: DeepPink;
}

```

**Note:** `1` is the index position of the first child element.

Assuming the snippet below is the HTML document for the above CSS ruleset, browsers will apply `DeepPink` to the first and third `<p>` elements.

```html
<h1>First heading 1 element</h1>
<p>First paragraph element</p>
<h2>First heading 2 element</h2>
<p>Second paragraph element</p>
<h3>First heading 3 element</h3>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-uhbpyv)

#### Apply DeepPink to every even `<p>` element type

The `:nth-of-type()` selector below selects every `<p>` child element with an even index.

```css
p:nth-of-type(even) {
  color: DeepPink;
}

```

**Note:** `1` is the index position of the first child element.

Assuming the snippet below is the HTML document for the above CSS ruleset, browsers will apply `DeepPink` to the second, fifth, and sixth `<p>` elements.

```html
<article>
  <h1>Article's first heading 1 element</h1>
  <p> Article's first paragraph element</p>
  <h2>Article's first heading 2 element</h2>
  <p>Article's second paragraph element</p>
  <p>Article's third paragraph element</p>
  <section>
    <h3>Article's first heading 3 element</h3>
    <p>Article's fourth paragraph element</p>
    <p>Article's fifth paragraph element</p>
  </section>
  <h2>Article's second heading 2 element</h2>
  <p>Article's sixth paragraph element</p>
  <p>Article's seventh paragraph element</p>
</article>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-ueawgj)

**Note:** Browsers will apply `DeepPink` to the fifth paragraph because it is the second `<p>` node of the `<section>` element.

#### Apply DeepPink to the third `<p>` element type, fifth, seventh, and so on

The `:nth-of-type()` selector below selects every `<p>` child element whose index is a multiple of two (`2`) with an offset of three (`+3`).

**Note:** `1` is the index position of the first child element.

```css
p:nth-of-type(2n+3) {
  color: DeepPink;
}

```

**Fun Quiz:** If the snippet below is the HTML document for the above CSS ruleset, which of the elements will the browser style?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<p>Nineth paragraph element</p>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-mbfvqr)

#### Apply DeepPink to the first `<p>` element type, third, fifth, and so on

The `:nth-of-type()` selector below selects every `<p>` child element whose index is a multiple of two (`2`) with an offset of negative three (`-3`).

**Note:** `1` is the index position of the first child element.

```css
p:nth-of-type(2n-3) {
  color: DeepPink;
}

```

**Fun Quiz:** If the snippet below is the HTML document for the above CSS ruleset, which of the elements will the browser style?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<p>Nineth paragraph element</p>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-inivqw)

#### Apply DeepPink to the first three `<p>` element type

The `:nth-of-type()` selector below applies `DeepPink` to the first three `<p>` child elements.

```css
p:nth-of-type(-n+3) {
  color: DeepPink;
}

```

**Fun Quiz:** If the snippet below is the HTML document for the above CSS ruleset, which of the elements will the browser style?

```html
<p>First paragraph element</p>
<p>Second paragraph element</p>
<p>Third paragraph element</p>
<p>Fourth paragraph element</p>
<p>Fifth paragraph element</p>
<p>Sixth paragraph element</p>
<p>Seventh paragraph element</p>
<p>Eight paragraph element</p>
<p>Nineth paragraph element</p>
<p>Tenth paragraph element</p>
<p>Eleventh paragraph element</p>
<p>Twelfth paragraph element</p>

```

[**Try Editing It**](https://codesweetly.com/try-it-sdk/css/selectors/nth-of-type/js-akcgtf)

**Note:**

- `1` is the index position of the first child element.
- The `-n+3` syntax always selects the first three `<p>` child elements because:
  - `-1 + 3 = 2`
  - `-2 + 3 = 1`
  - `-3 + 3 = 0`

## Overview

In this article, we discussed the similarities and differences between the CSS `:nth-child()` and `:nth-of-type()` selectors. We also used examples to see how they work.

Thanks for reading!

### And here’s a useful React.JS resource:

I wrote a book about [Creating NPM Packages](https://amzn.to/48NjBdY)!

It is a beginner-friendly guidebook for mastering the art of creating, testing, and publishing NPM libraries in the React and JavaScript ecosystem.

It uses a scalable project to explain the fundamentals of building and managing NPM packages from scratch.

[![Creating NPM Package ReactJS book is now available at Amazon](https://www.freecodecamp.org/news/content/images/2024/01/creating-npm-package-reactjs-book-codesweetly.png)](https://amzn.to/48NjBdY)


