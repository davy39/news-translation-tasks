---
title: How to Use the :has() Selector in CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-22T14:34:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-has-selector-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pexels-alizee-marchand-947457.jpg
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By James Charlesworth\nFor most of the history of CSS, selectors have been\
  \ limited to targeting elements based on their parents in the DOM tree. Consider\
  \ this HTML structure:\n<div>\n    <p>Paragraph 1</p>\n<div>\n<main>\n    <div>\n\
  \        <p>Paragraph 2</..."
---

By James Charlesworth

For most of the history of CSS, selectors have been limited to targeting elements based on their _parents_ in the DOM tree. Consider this HTML structure:

```html
<div>
    <p>Paragraph 1</p>
<div>
<main>
    <div>
    	<p>Paragraph 2</p>
    </div>
 <main>
```

Applying styles to paragraph 2 in CSS is trivial, as it can be targeted by the parent `<main>` node.

```css
main p {
    color: blue;
}
```

This will style _Paragraph 2_ but not _Paragraph 1_, as the second paragraph is contained inside the `<main>` element.

What has not historically been simple however, was styling the `<main>` node based on the presence of the `<p>` tag below it.

```html
<main>
    Don't Style This
</main>
<main>
    <p>Style This</p>
</main>
```

By looking upwards in the DOM tree, there was no way to apply styles to just the second `<main>` element and not the first (without uses classes or IDs of course).

## Introducing the :has() Selector

At its core, the `:has()` selector is a relational [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes). This means it allows you to select an element based on its relationship with other elements. Specifically, it selects an element if it contains another element that matches a given selector. 

In the above example, we can now do the following:

```css
main:has(p) {
    color: blue;
}
```

This opens up numerous possibilities for styling your web pages more efficiently and with less code.

## Example 1 – Highlighting Articles with Images

Consider a webpage that displays a list of articles, each enclosed in an `<article>` tag. If we want to highlight articles that contain images, the `:has()` selector offers a straightforward solution:

```css
article:has(img) {
  border: 2px solid blue;
}
```

%[https://codepen.io/jcharlesworthuk/pen/gOEyGEM]

This CSS rule applies a blue border around any `<article>` tag that contains an `<img>` element, visually distinguishing articles with images from those without.

## Example 2 - Styling Navigation Menus with Sub-Menus

Here is another example. In this example, the `:has()` selector is being used to add a `:before()` pseudo element to any menu item that has sub menus – that is any `<li>` element that contains a child element with the class `.sub-menu`.

```css
.main-menu > li:has(.sub-menu):before {
  content: "▼";
  margin-left: 5px;
  font-size: 0.75em;
}
```

%[https://codepen.io/jcharlesworthuk/pen/LYavOOG]

## Browser Support

As of March 2024, the `:has()` selector is supported by approximately [92% of web browsers globally](https://caniuse.com/css-has), including all the most common modern browsers such as the latest versions of Chrome, Firefox, Safari and Edge. For unsupported browsers, consider using feature detection libraries like [Modernizr](https://modernizr.com/docs/) to apply alternative styles. 

It's also a good idea to design your CSS to degrade gracefully, ensuring that your web pages remain at least functional and visually acceptable in browsers that do not support the `:has()` selector.

## Ready to Use Today

The `:has()` selector offers a new level of flexibility and power in CSS, enabling you to write cleaner, more efficient stylesheets. By selecting elements based on their content, the `:has()` selector simplifies many common styling challenges, from highlighting articles with images to styling responsive layouts. 

As browser support continues to grow, 2024 is the perfect year to begin incorporating the `:has()` selector into your CSS.

Happy styling – and feel free to try putting your CSS into action in one of the beginner projects on [https://traintocode.com/projects](https://traintocode.com/projects).

