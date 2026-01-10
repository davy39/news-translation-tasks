---
title: A cheatsheet to help you remember CSS custom properties
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-customs-properties-cheatsheet-c86778541f7d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OkasBr8SDeRPWhLGIGlqnw.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Vincent Humeau

  CSS custom properties, also known as CSS variables, represent custom properties
  that can be declared and be called in your CSS.

  Declare a custom property in CSS

  To declare a Custom property in your CSS, you need to use the -- syntax...'
---

By Vincent Humeau

CSS custom properties, also known as CSS variables, represent custom properties that can be declared and be called in your CSS.

### Declare a custom property in CSS

To declare a Custom property in your CSS, you need to use the `--` syntax:

```css
:root { --colorPrimary: hsla(360, 100%, 74%, 0.6); }
```

Notice the `:root` pseudo-class selector — we can declare our variables globally using it. We can also declare them using other selectors, and they will then be scoped in those.

```css
.theme-dark { --colorPrimary: hsla(360, 100%, 24%, 0.6); }
```

### Use a custom property in CSS

To use a CSS custom property in your CSS, you can use the `var()` function:

```css
:root { --colorPrimary: tomato; } 
.theme-dark { --colorPrimary: lime; } body { background-color: var(--colorPrimary); }
```

In this case, `body` will have a background colour of `tomato`, but a `body.theme-dark` of `lime`.

### Use custom properties without units

CSS custom properties can be declared without units if they are used with the `calc()` function.

```css
:root { --spacing: 2; } 
.container { 
  padding: var(--spacing) px; /*Doesn't Work ?*/ 
  padding: calc(var(--spacing) * 1rem); /*Will output 2rem ?*/ 
}
```

## Use custom properties with JavaScript

To get a custom property, we can use the following:

```js
getComputedStyle(element).getPropertyValue("--my-var"); 
// Or if inline 
element.style.getPropertyValue("--my-var");
```

To update the custom property value:

```
element.style.setProperty("--my-var", newVal);
```

Example of getting and replacing values:

In the following example, we use the [dat.gui controller library](https://workshop.chromeexperiments.com/examples/gui/) to change the value of --scenePerspective, --cubeRotateY, and --cubeRotateX custom properties. This method makes it easier to apply a new style, as you do not have to apply inline style on each DOM element.

Thanks for reading!

### Resources

[Defining Custom Properties: the –* family of properties](https://drafts.csswg.org/css-variables/#defining-variables)

[Custom properties: CSS variables — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

[var() — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/var)

[Using CSS custom properties (variables) — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables)

You can read more of my articles [on my blog](https://vinceumo.github.io/devNotes/css/2019/02/20/css-customs-properties.html).

