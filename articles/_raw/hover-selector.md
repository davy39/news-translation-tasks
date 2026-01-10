---
title: CSS Hover Selector Explained (with Example)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-29T17:26:00.000Z'
originalURL: https://freecodecamp.org/news/hover-selector
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e6a740569d1a4ca3cf6.jpg
tags:
- name: CSS
  slug: css
seo_title: null
seo_desc: 'The CSS :hover selector is one of many pseudo-classes that are used to
  style elements. :hover is used to select elements that users hover their cursor
  or mouse over. It can be used on all elements, not only on links.

  When used to style links, :hover ...'
---

The CSS `:hover` selector is one of many pseudo-classes that are used to style elements. `:hover` is used to select elements that users hover their cursor or mouse over. It can be used on all elements, not only on links.

When used to style links, `:hover` is often paired with the `:link`, `:visited`, and `:active` selectors which style unvisited, visited, and active links, respectively.

If `:link` and `:visited` rules are in the CSS definition, `:hover` should fall after them. Otherwise, the styles in the `:hover` rule won't be applied to the selected element.

**Syntax:**

```css
a:hover {
  /* CSS declarations */
}
```

The hover selector only applies the styles provided in the rule when an element enters the hover state. This is typically when a user hovers over the element with their mouse.

```css
button {
  color: white;
  background-color: green;
}

button:hover {
  background-color: white;
  border: 2px solid green;
  color: green;
}
```

In the example above, the button’s normal styling is white text on a green button. When a user hovers over the button with their mouse, the rule with the `:hover` selector will become active and the button’s style will change.

Note that `:hover` can be problematic on touchscreens – different hardware and mobile browser implementations can cause the pseudo-class to be triggered in some cases and not in others. Make sure to thoroughly test elements with `:hover` in as many different mobile browsers and devices as possible.

