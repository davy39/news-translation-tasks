---
title: CSS Functions – How to Use calc(), max(), min(), and clamp()
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2022-05-18T15:11:08.000Z'
originalURL: https://freecodecamp.org/news/css-functions-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-katerina-holmes-5905965.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: CSS
  slug: css
seo_title: null
seo_desc: "In CSS there are a lot of different units of measurement. You have px and\
  \ percentages, vh, vw, em, rem, and others. \nThere will come a time when you want\
  \ to get a value by combining two or more different units. CSS has a function that\
  \ you can use to ..."
---

In CSS there are a lot of different units of measurement. You have px and percentages, vh, vw, em, rem, and others. 

There will come a time when you want to get a value by combining two or more different units. CSS has a function that you can use to make such calculations – `calc()`. And in this tutorial, you'll learn how it works.

There are other functions you can use with these relative units – like `max`, `min` and `clamp` – that, when confronted with different values, use the appropriate one. These are really useful in responsive layouts, and can be an alternative to using media queries.

If you learn to use them appropriately you can avoid the jumpy change of layout that can happen when resizing a window if you used media queries, and with less code!

## How to Use the CSS `calc()` Function

The calc function takes a single parameter. This parameter can be an expression combining any length unit and the four mathematical operators `+`, `-`, `/`, `*`.

You can also use parenthesis to indicate an order of evaluation different than the standard precedence rules.

In the expression inside the `calc()` function you can use CSS variables, values obtained with `[attr()](https://developer.mozilla.org/en-US/docs/Web/CSS/attr)`, and values from the functions `max()`, `min()` and `clamp()`.

`calc()` allows you to calculate a value from complex parameters.

```css
div {
    width: calc(100% - 2em);
}
```

**Note**: always leave a space on either side of the mathematical operators.

## How to Use the CSS `max()` Function

The `max` function accepts a list of comma separated values and returns the biggest one. Each value can also be an expression (whatever you can use as an argument for the `calc()` function can be one of the arguments in this function, too).

The max function can be seen as a way to determine a _minimum value_ for a certain thing.

A use case for this function is making a text responsive, while giving a minimum value to the dimension.

For example:

```css
h1 {
    font-size: max(1rem, 10vh);
}
```

In this way, the text will be a tenth of the viewport height, unless the viewport height becomes too small. The text will always have a `font-size` of at least `1rem` to ensure legibility.

## How to Use the CSS `min()` Function

In the same way as the max function, `min` can take any number of arguments, including other `max`, `min`, or `clamp` functions, and give back the smallest value between them.

The min function can be seen as determining a _maximum value_.

For example, let's say that you are creating a form and you want it to be responsive while the screen width changes. You'll want to give it a maximum width to avoid that horizontally stretched look that can happen on the largest screens.

You could write something like this:

```css
.form {
    width: min(600px, 90vw);
}
```

Your page will have a width equal to 90% of the viewport width, or 600px wide, whatever is smallest. So if the viewport width is larger than ~670px, the form will not stretch horizontally.

## Example for `min()` and `max()`:

You can see the code snippets at work in this pen. Try resizing the pen horizontally and vertically and see the form width and font size change responsively.

%[https://codepen.io/nethleen/pen/XWZMGVd]

## How to Use the CSS `clamp()` Function

The clamp function clamps a value between and upper and lower limit. It selects a value in a range with defined limits.

`clamp` takes three values. The first one will be the minimum value, the second one the preferred value, and the third one the maximum value. 

The clamp function will give back the preferred value, unless it is smaller than the minimum value (in which case it will give back the minimum value) or if it is bigger than the maximum value, in which case it will give back the maximum value.

You can use `clamp` to have layout elements responsively resize within a range.

```css
h1 {
    font-size: clamp(1rem, 10vw, 2rem);
}

div {
    padding: clamp(10px, 6vw, 50px);
    width: clamp(140px, 90vw, 600px);
}
```

## Example of `clamp` Function:

See it in action in this pen! Resize the pen horizontally and see how the various elements change dimensions.

%[https://codepen.io/nethleen/pen/ExQWJZo]

The MDN has more detailed info on all of these functions:

* [calc](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)
* [max](https://developer.mozilla.org/en-US/docs/Web/CSS/max)
* [min](https://developer.mozilla.org/en-US/docs/Web/CSS/min)
* [clamp](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp)

And with this, you have seen an overview of these four marvelous functions. You have learned enough to start using them, so go out there and have fun!


