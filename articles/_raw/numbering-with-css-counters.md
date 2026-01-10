---
title: How to Automatically Number Elements with CSS Counters
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-19T18:31:54.000Z'
originalURL: https://freecodecamp.org/news/numbering-with-css-counters
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Numbering-with-CSS-Counters.png
tags:
- name: automation
  slug: automation
- name: CSS
  slug: css
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'By Erisan Olasheni

  CSS counters are used to add counts to elements. The count is added by providing
  variables that can be initialized (using counter-reset), and these variables can
  then be incremented by CSS rules.

  Many developers overlook this power...'
---

By Erisan Olasheni

CSS counters are used to add counts to elements. The count is added by providing **variables** that can be initialized (using `counter-reset`), and these variables can then be incremented by CSS rules.

Many developers overlook this powerful CSS feature, and that is why we are going to go over how to work with counters in this tutorial.

## When to Use CSS Counters

CSS counters can be used whenever you need a counting system on your web page. Some of the best use cases are:

* Numbering complex lists
* Create dynamic pagination links
* Numbering steps in an on-boarding system.

In this tutorial, we will be talking about how to use CSS counters to **make complex lists** and **create dynamic pagination**.

## How to Use CSS Counters

The CSS counting system consists of the `counter-reset`, `counter-increment`, `counter()` and `counters()` and `content` properties. These properties take care of everything you need to do in the CSS counting system. 

Let's look more closely at these properties so we understand how they can be used.

### Counter Properties Explained

* `counter-reset`: Used to **reset** or **initialize** your counter. To use CSS counters you must first create one with this property.
* `counter-increment`: Used to **increment** the variable of an already **initialized** counter.
* `counter()`: This function does the magic. It's used inside the content property, on a `:before` or `:after` pseudo selector, to **add up** the counts.
* `counters()`: Used for inherited counting, and generates the instance of a parent counter **variable** in the child.
* `content`: Used to **add up** the count **value** (strings) by manipulating content for `:before` and `:after` [css selectors](https://lyty.dev/css/css-selector.html).

Now that we understand these CSS counter properties and values, let's dive in to our examples.

## Numbering Elements on a Web page

Numbering can be done in HTML, but CSS numbering provides dynamic and easy-to-control ways of doing the job using CSS counters. The following example will number the elements on web page with CSS.

First, we are going to set up some simple numbering that does just one-level numbering. Then we'll move on to a more advanced example where we'll set up a table of contents.

### Simple Numbering

In this example, we'll create a simple items counter with CSS. In your HTML, just create your items structure like this:

```html
<div>
  <p>Mercury</p>
  <p>Venus</p>
  <p>Earth</p>
</div>

```

In the CSS we are going to do three key things:

1. Initialize the counter on the parent div using `counter-reset`
2. Increment the counter value by 1 on the child `div p` using `counter-increment`
3. Add the counter variables before the `div p` content using the `:before` pseudo selector.

Let's go!

```css
div {
  list-style-type: none;
  counter-reset: css-counter 0; /* initializes counter to 0; use -1 for zero-based numbering */
}

div p {
  counter-increment: css-counter 1; /* Increase the counter by 1. */
}

div p:before {
  content: counter(css-counter) ". "; /* Apply counter before children's content. */
}

```

### The Result

![Image](https://paper-attachments.dropbox.com/s_76F886E1B187D46E2BEDCBADBD0CB5649AD0A3F515F1D7BB79358C4B37E1BADB_1592225271319_CSS_Counters_Elements_Numbering_CSS_Do_It_Yourself_Lyty_dev.png)

The above numbering was done with pure CSS. Interesting, right? 

Now we are going to implement some more complex numbering which makes CSS counters worth learning. We will be numbering nested elements with the `counters()` function, which can be used for inherited counting. This generates the instance of a parent counter in the child.

### Table of Contents Numbering

```html
<ul>
  <li>
    Web Development
    <ul>
      <li>HTML</li>
      <li>
        CSS
        <ul>
          <li>CSS Introduction</li>
          <li>CSS Selectors</li>
          <li>CSS Animation</li>
        </ul>
      </li>
      <li>JavaScript</li>
    </ul>
  </li>
  <li>Graphics Design</li>
  <li>Computer Education</li>
</ul>

```

The CSS looks like this:

```css
ul {
  list-style-type: none;
  counter-reset: css-counters 0; /* intializes counter, set -1 for zero-based counters */
}

ul li:before {
  counter-increment: css-counters;
  content: counters(css-counters, ".") " "; /* generates inherited counters from parents */
}

```

### The Result

![Image](https://paper-attachments.dropbox.com/s_76F886E1B187D46E2BEDCBADBD0CB5649AD0A3F515F1D7BB79358C4B37E1BADB_1592225350657_CSS_Counters_Inherited_Element_Counting_Example_CSS_Do_It_Yourself_Lyty_dev.png)

Now you can see the power of nesting counts with `counters()`. This saves you the hassle of improper nesting. To help you avoid mistakes, it inherits the counter properties of the parents, and appends the child's counter to it. 

So now that we are good with numbering elements, what next?

## Making Dynamic Pagination

Making pagination with CSS counters is quite simple. Pagination is usually done with HTML, repeating the same set of elements and changing the numbers inside to create navigation to each page of a result. 

A developer may choose to use something dynamic like making loops that generate the elements, or do it from the server. But today we're going to use CSS to do this dynamically! 

How? With our senior `counters()` function. 

The same way we have been incrementing our values for the numbering above, we can also make a dynamic pagination list with (you guessed it) CSS counters.

Let's start:

```html
<ul>
  <li class="previous">&lt;</li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li></li>
  <li class="next">&gt;</li>
</ul>

```

  
**Note:** You don't need to add numbers inside the `li`, and you can make as many as you want. Our CSS `counters()` are going to do the numbering for us.

The CSS looks like this:

```css
ul {
  list-style-type: none;
  counter-reset: paginate-counter 0;
}

ul li {
  border: solid 3px #ccc;
  color: #36f;
  border: 5px;
  float: left;
  margin: 5px;
  padding: 8px 10px;
  font-size: 14px;
  cursor: pointer;
  text-align: center;
}

/* Setting styles for the inner text */
ul li:not(.previous):not(.next):before {
  counter-increment: paginate-counter;
  content: counter(paginate-counter);
}

```

  
The Result

![Image](https://paper-attachments.dropbox.com/s_76F886E1B187D46E2BEDCBADBD0CB5649AD0A3F515F1D7BB79358C4B37E1BADB_1592225376032_CSS_Counters_CSS_Pagination_Example_CSS_Do_It_Yourself_Lyty_dev.png)

What else can you do with counters? Let me hear your ideas.

Thanks!

