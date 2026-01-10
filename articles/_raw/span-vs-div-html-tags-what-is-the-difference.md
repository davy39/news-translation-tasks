---
title: Span VS Div HTML Tags – What is the Difference?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-08T21:08:38.000Z'
originalURL: https://freecodecamp.org/news/span-vs-div-html-tags-what-is-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/spanvdiv.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'If you inspect a web page with your browser''s developer tools, you''ll
  likely see a bunch of nested div tags, and possibly some content wrapped in a span
  tag.

  Similar content is usually grouped together by these two container elements – span
  and div. ...'
---

If you inspect a web page with your browser's developer tools, you'll likely see a bunch of nested `div` tags, and possibly some content wrapped in a `span` tag.

Similar content is usually grouped together by these two container elements – `span` and `div`. You can use them both as containers, but they don't work quite the same way. 

In this tutorial, I will show you the differences between span and div so you won't be confused by them anytime you have to use both.

## The Key Differences Between `span` and `div` Tags

You can use both the `span` and `div` tags as a container if you want to make a particular part of the web page distinct and style it differently. But again, they don't serve the exact same purpose.

### The HTML div Tag

The div tag is a generic block-level element used for associating and grouping together a larger chunk of a web page – usually a section such as a header, footer, the main content, and so on.
 
In the example below, I group the header of a web page together with the `div` tag and styled it using CSS.

```html
<div class="header">
      <h2 class="logo">freeCodeCamp</h2>

      <ul class="nav">
        <li><a href="">Home</a></li>
        <li><a href="">About</a></li>
        <li><a href="">Serices</a></li>
        <li><a href="">Contact</a></li>
      </ul>
</div>
```

In the CSS below, I laid out the header and the navbar in it with CSS Flexbox. I also removed the default margin and padding assigned to elements by browsers.

```css
* {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

.header {
      padding: 0 70px;
      display: flex;
      align-content: center;
      justify-content: space-between;
      margin-top: 20px;
      margin-bottom: 20px;
      color: crimson;
    }

.nav {
      display: flex;
      align-content: center;
      justify-content: center;
      gap: 60px;
      list-style-type: none;
    }

.nav li a {
      text-decoration: none;
      font-size: 1.2rem;
      color: crimson;
    }
```

![header-with-div](https://www.freecodecamp.org/news/content/images/2021/09/header-with-div.png)

In addition, you can use the div tag to group similar content together. This could be similar text, images, videos, and so on. So, you can always nest divs within divs, and attach unique classes or id attributes to them so you don't get confused.

### The HTML `span` Tag

The `span` tag is an inline element that you use to make a smaller part of content stand out with CSS or JavaScript. You shouldn't nest span unless you thoroughly know what you're doing – but you can put multiple span tags within a block-level element.

In the example below, I made some particular words stand out by wrapping span tags around them and styling them differently.

```html
<p>
      This is a <span class="crimson">crimson text</span> within black texts.
      This is an <span class="indigo">indigo text</span> within others, and this
      is an <span class="orange">orange text</span> within other texts.
</p>
```

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 900px;
    margin: 0 auto;
    height: 100vh;
  }

p {
    font-size: 2.5rem;
  }

.font-style {
    font-style: italic;
  }

.crimson {
    color: crimson;
  }

.indigo {
    color: indigo;
  }

.orange {
    color: orange;
  }
```

![span-in-action](https://www.freecodecamp.org/news/content/images/2021/09/span-in-action.png)

You can see the most important differences between the `span` and `div` tags in the table below:

| `span` Tag      | `div` Tag |
| ----------- | ----------- |
| Inline-level element      | Block-level element       |
| Used for grouping small chunks of text   | Used for grouping large chunks of texts together        |
| Must not be nested to avoid confusion   | Usually nested        |


## When should you use `span` or `div`?

You should use `span` when you want to style a particular part of your content differently or manipulate it with JavaScript. You can also use it as a container for inline elements.

You should use the `div` tag, on the other hand, if you want to group large chunks of content together, and when you want to layout elements on the web page.

## Conclusion
In this tutorial, you have learned about the differences between the span and div tags.

These tags are instrumental in styling and layouts. Just keep in mind that HTML5 introduced semantic elements such as `section`, `header`, `nav`, `footer`, and others.  So in general, you should use either `span` or `div` only when the semantic elements don't fit in with what you want to do.

Thank you for reading, and keep coding.


