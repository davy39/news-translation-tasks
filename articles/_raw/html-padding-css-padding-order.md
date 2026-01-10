---
title: HTML Padding – CSS Padding Order
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-08-04T21:33:13.000Z'
originalURL: https://freecodecamp.org/news/html-padding-css-padding-order
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/kobu-agency-ipARHaxETRk-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "In this article, we are going to learn about CSS padding properties, the\
  \ shorthand property, and how padding differs from margin. \nWhat is padding in\
  \ CSS?\nCSS padding creates space around the element's content. This space is within\
  \ the element's bord..."
---

In this article, we are going to learn about CSS padding properties, the shorthand property, and how padding differs from margin. 

## What is padding in CSS?

CSS padding creates space around the element's content. This space is within the element's border and margin. 

Let's take a look at the CSS box model to better understand how padding works. Every HTML element has a box around it and is comprised of four parts: content, padding, border, and margin. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-03-at-1.38.36-AM.png)

The blue section is the element's content while the green section represents the padding. Notice how the padding is inside the border and margin properties. 

Let's look at CSS's padding properties in more detail.

### Padding-top property

This is a CSS property that adds space to the top of an element. 

```css
  padding-top: 20px;
```

%[https://codepen.io/jessica-wilkins/pen/poPOjjw]

### Padding-right property

This is a CSS property that adds space to the right of an element. 

```css
  padding-right: 40px;

```

%[https://codepen.io/jessica-wilkins/pen/ExmeVKp]

### Padding-bottom property

This is a CSS property that adds space to the bottom of an element. 

```css
  padding-bottom: 20px;

```

%[https://codepen.io/jessica-wilkins/pen/QWvVjKv]

### Padding-left property

This is a CSS property that adds space to the left of an element. 

```css
  padding-left: 40px;

```

%[https://codepen.io/jessica-wilkins/pen/GRmXprJ]

## Difference between Padding and Margin in CSS

Margin creates space around the element and outside its border. 

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-03-at-1.38.36-AM.png)

This example adds 50px of margin-bottom to the `h1` element. This creates extra space between the `h1` and `p` elements. 

```css
margin-bottom: 50px;
```

%[https://codepen.io/jessica-wilkins/pen/XWRBVRJ?editors=1100]

## Padding Shorthand Property

The padding shorthand property allows us to set the padding on all four sides at once instead writing out `padding-top`, `padding-right`, `padding-bottom`, `padding-left`. 

When you just use one value, equal amounts of padding will be applied on all sides. 

```css
 padding: 10px;
```

Here is the code without the shorthand property:

```css
  padding-top: 10px;
  padding-right: 10px;
  padding-bottom: 10px;
  padding-left: 10px;
```

This is what the result would look like in the browser.

%[https://codepen.io/jessica-wilkins/pen/YzVjrBb?editors=1100]

When you use two values, the first value adds padding to the top and bottom while the second value adds padding to the left and right.

```css
  padding: 10px 30px;

```

Here is the code without the shorthand property:

```css
  padding-top: 10px;
  padding-right: 30px;
  padding-bottom: 10px;
  padding-left: 30px;
```

%[https://codepen.io/jessica-wilkins/pen/xxdJPgB]

When you use three values, the first value adds padding to the top, the second value adds padding to the right and left, and the third value adds padding to the bottom. 

```css
  padding: 10px 30px 50px;

```

Here is the code without the shorthand property:

```css
  padding-top: 10px;
  padding-right: 30px;
  padding-bottom: 50px;
  padding-left: 30px;
```

%[https://codepen.io/jessica-wilkins/pen/vYmaWjG]

And when you use four values, the first value adds padding to the top, the second value adds padding to the right, the third value adds padding to the bottom and the fourth value adds padding to the left.

The best way to remember the order for all four values is to think clockwise (top, right, bottom, left).

```css
  padding: 10px 20px 30px 40px;
```

Here is the code without the shorthand property:

```css
  padding-top: 10px;
  padding-right: 20px;
  padding-bottom: 30px;
  padding-left: 40px;
```

%[https://codepen.io/jessica-wilkins/pen/jOmpaRp]

You can choose to use pixels, em, rem or percentages for the values. But you are not allowed to use negative values.

## Conclusion

When you want to add space around an HTML element's content then you'll use the padding properties. 

The padding shorthand property allows us to set the padding on all four sides at once instead writing out `padding-top`, `padding-right`, `padding-bottom`, `padding-left`. 

If you want to create space between elements, then you use the margin properties. With margin you can use negative values whereas with padding that is not allowed. 


