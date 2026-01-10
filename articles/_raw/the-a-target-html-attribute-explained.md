---
title: The a target HTML Attribute Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T22:47:00.000Z'
originalURL: https://freecodecamp.org/news/the-a-target-html-attribute-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e4b740569d1a4ca3c5e.jpg
tags:
- name: HTML
  slug: html
seo_title: null
seo_desc: "The <a target> attribute specifies where to open the linked document in\
  \ an a (anchor) tag.\nExamples of \nA target attribute with the value of “_blank”\
  \ opens the linked document in a new window or tab.\n    <a href=\"https://www.freecodecamp.org\"\
  \ target=..."
---

The `<a target>` attribute specifies where to open the linked document in an `a` (anchor) tag.

## Examples of <a target>

A target attribute with the value of “_blank” opens the linked document in a new window or tab.

```html
	<a href="https://www.freecodecamp.org" target="_blank">freeCodeCamp</a>
```

A target attribute with the value of “_self” opens the linked document in the same frame as it was clicked (this is the default and usually does not need to be specified).

```html
	<a href="https://www.freecodecamp.org" target="_self">freeCodeCamp</a>
```

```html
	<a href="https://www.freecodecamp.org">freeCodeCamp</a>
```

A target attribute with the value of “_parent” opens the linked document in the parent frame.

```html
	<a href="https://www.freecodecamp.org" target="_parent">freeCodeCamp</a>
```

A target attribute with the value of “_top” opens the linked document in the full body of the window.

```html
	<a href="https://www.freecodecamp.org" target="_top">freeCodeCamp</a>
```

A target attribute with the value of _“_framename_”_ opens the linked document in a specified named frame.

```html
	<a href="https://www.freecodecamp.org" target="framename">freeCodeCamp</a>
```

## Related links:

* [The <a href> attribute](https://guide.freecodecamp.org/html/attributes/a-href-attribute)
* [General info on HTML attributes](https://guide.freecodecamp.org/html/attributes)

